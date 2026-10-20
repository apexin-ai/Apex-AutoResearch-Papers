# Director coordination — Part 1 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

[Transcript overview](../director-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/1e/1edf016a3b0527fcc112.json)

## Round 1

## Round 1

80 recorded events


### User

_source line 1 · 2026-05-18T06:45:31.649915+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: faith-evidence-ie
- 论文路径: projects/faith-evidence-ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference Long Paper
- 截止日期: 2026-07-15

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-18T06:45:38.438468+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-18T06:45:38.489455+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-18T06:45:41.503415+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
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

_source line 5 · 2026-05-18T06:45:41.654649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-18T06:45:46.926865+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-18T06:45:46.977556+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-18T06:45:50.894049+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-18T06:45:52.301082+00:00_

{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (200 个)\n\n- **mvp2_sft_eval_r2**: DONE (success) — \n- **mvp2_sft_eval**: DONE (killed) — \n- **mvp2_grpo_flatnli_r2**: DONE (killed) — \n- **mvp2_grpo_extract_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r4**: DONE (killed) — \n- **mvp2_grpo_extract**: DONE (failed) — \n- **mvp2_grpo_flatnli**: DONE (failed) — \n- **mvp2_grpo_ced_r3**: DONE (failed) — \n- **mvp2_grpo_ced_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r1**: DONE (killed) — \n- **mvp2_grpo_ced**: DONE (failed) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **seed_comparison_prep** (killed): —\n- **plan006_1_7b_rsft_eval** (killed): —\n- **rsft_s43_dev_eval_preds** (success): Eval RSFT-s43 (CED-scored) on DocRED dev with predictions saved. Prerequisite for Lead 1 CED evidence filtering: per-sentence NLI scoring requires full prediction outputs.\n\n## 趋势\n成功 98 / 负向 19 / 失败 41 / 共 196\nedcr: 0.6542 ↑（近 3 次 success）\nevi_f1: 0.8063 ↓（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- mvp2_grpo_ced: 训练失败 — unknown\n- mvp2_grpo_flatnli: 训练失败 — unknown\n- mvp2_grpo_extract: 训练失败 — unknown\n- mvp2_sft_eval: 已被终止 — unknown\n- mvp2_grpo_ced_r1: 已被终止 — unknown\n- mvp2_grpo_ced_r2: 已被终止 — unknown\n- mvp2_grpo_ced_r3: 训练失败 — unknown\n- mvp2_grpo_ced_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r4: 已被终止 — unknown\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_multi: 已被
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-18T06:45:52.452119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-18T06:45:52.754477+00:00_

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
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/analysis}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-18T06:45:52.754906+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-18T06:45:53.308438+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-18T06:45:58.842503+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information about EMNLP 2026 and ARR submissions, though the results primarily show inform
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 6087
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-18T06:45:58.843047+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5534
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-18T06:46:04.365008+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-18T06:46:05.369516+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 official website call for papers Budapest submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 official website call for papers Budapest submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-18T06:46:06.676114+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-18T06:46:07.178430+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-18T06:46:07.329834+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
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

_source line 21 · 2026-05-18T06:46:07.380651+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-18T06:46:11.450665+00:00_

Web search results for query: "EMNLP 2026 official website call for papers Budapest submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here's the information about EMNLP 2026:

## Official Website
The official EMNLP 2026 call for papers is at https://2026.emnlp.org/

## Conference Details
The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

## Submission Deadline
The EMNLP 2026 paper submission deadline is 2026-05-25 23
…[truncated 450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 6081
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-18T06:46:12.304921+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines author instructions page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

I found information about ACL Rolling Review submission guidelines. Here are the key details regarding 2026 submissions:

## Page Limits

The search results don't explicitly state the page limit in the excerpts returned. However, based on the ACL 2026 main conference information, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address rev
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 7939
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-18T06:46:16.481486+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-18T06:46:16.632696+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/acl_lualatex.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/acl_latex.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-18T06:46:16.783679+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclrollingreview.org cfp 2026 long paper short paper page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclrollingreview.org cfp 2026 long paper short paper page limit"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-18T06:46:21.607891+00:00_

Web search results for query: "site:aclrollingreview.org cfp 2026 long paper short paper page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"دعوة لتقديم أوراق المؤتمر الرئيسية -","url":"https://translate.google.com/translate?u=https%3A%2F%2F2026.eacl.org%2Fcalls%2Fpapers%2F&hl=ar&sl=en&tl=ar&client=srp"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"LINGUIST List 36.2627 Confs: 19th Conference of the European Chapter of the Association for Computational Linguistics (Morocco)","url":"https://linguistlist.org/issues/36/2627/"},{"title":"Frequently Asked Questions for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/faq/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results from the ACL Rolling Review website, here are the page limits for 2026 submissions:

**Long Papers:** 8 pages (not including limitations and ethical considerations)

**Short Papers:** 4 pages (not including limitations and ethical considerations)

Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 4824
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-18T06:46:24.762063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-18T06:46:25.057169+00:00_

1	\begin{abstract}
2	
3	Large Language Model (LLM) based Document-level Relation Extraction (DocRE) methods now match or exceed encoder baselines in extraction accuracy, yet they produce bare relation triplets without identifying the sentences that support each prediction.
4	In deployment contexts such as clinical knowledge bases and legal due-diligence systems, users cannot verify predictions without manually locating textual evidence across multi-page documents.
5	Encoder-based evidence methods (SAIS, DREEAM) can produce supporting sentences but trail LLM approaches in accuracy. The community therefore faces a gap between extractive precision and output verifiability.
6	
7	We formalize evidence-grounded DocRE as a structured generation task and conduct a systematic comparison of three post-training optimization paradigms: Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT).
8	Our study spans 85+ experimental configurations across four model scales (1.7B to 8B parameters), two model families, and two datasets.
9	We introduce the Evidence-Decoupling Ratio (EDCR) diagnostic and a Contrastive Evidence Discrimination (CED) scoring function for sample selection.
10	
11	Three findings emerge.
12	First, RL optimization pressure correlates with evidence-extraction decoupling severity: GRPO causes catastrophic decoupling, DPO shows gradual degradation, and RSFT preserves stable joint performance.
13	Second, the cost of evidence production is scale-dependent and non-monotonic: at 1.7B parameters evidence provides a +8pp Ign-F1 benefit, at 4B it imposes a $-$7.5pp penalty, and at 8B the cost approaches zero.
14	Third, RSFT with CED scoring is the only effective route: it achieves +4.92pp Ign-F1 over supervised fine-tuning at 4B scale (four-seed mean), and our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT performance (50.51).
15	
16	\end{abstract}
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 295
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-18T06:46:25.057618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-18T06:46:25.961686+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition for end-to-end extraction, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy.
6	Yet every one of them outputs bare relation triplets $(e_h, r, e_t)$ without any indication of \emph{which sentences} in the document support each prediction.
7	In deployment contexts where predictions feed into clinical knowledge bases, legal due-diligence pipelines, or financial compliance systems, end users cannot verify a prediction without manually locating its textual basis across a multi-page document.
8	
9	The absence of verifiable evidence creates a practical bottleneck.
10	Relation extraction outputs are consumed downstream by knowledge graph construction and human decision workflows.
11	When a system predicts that a drug interacts with a gene, or that a contract clause implies a liability, practitioners must trace each prediction back to source text before acting on it.
12	Without machine-generated evidence, this verification requires exhaustive manual review of the input document for every predicted relation.
13	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
14	Both improve extraction quality \emph{and} produce evidence annotations.
15	However, encoder methods now trail LLM-bas
…[truncated 4907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-18T06:46:26.113175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-18T06:46:26.465205+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
5	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
6	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.
7	A parallel thread incorporates sentence-level evidence into these architectures.
8	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
9	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
10	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
11	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
12	Recent work has recast DocRE for large language models.
13	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
14	These methods match or surpass encoder baselines but produce bare triplets without evidence.
15	The critical distinction lies in computational nature: in SAIS and DREEAM, evidence
…[truncated 4221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-18T06:46:26.465659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-18T06:46:26.968203+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support.
8	
9	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.
10	
11	
12	\subsection{Supervised Fine-Tuning Baseline}
13	\label{sec:sft}
14	
15	We fine-tune all models with LoRA~\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to attention projection matrices. The training data consists of DocRED~\citep{yao2019docred} training documents converted to the structured output 
…[truncated 7862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-18T06:46:26.968827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-18T06:46:27.421284+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Dataset.}
8	We conduct experiments on DocRED~\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\citep{tan2022redocred} for cross-dataset generalization evaluation.
9	
10	\paragraph{Models.}
11	Our primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.
12	
13	\paragraph{Training.}
14	All models use LoRA~\citep{hu2022lora} with rank $r{=}64$ and $\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\S\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.
15	
16	\paragraph{Metrics.}
17	We report five metrics. \textbf{Ign-F1} is the primary DocRED metric that ignores triples appearing in the training set, matching the official leaderboard protocol. \textbf{Rel-F1} measures relation extraction F1 on all triples. \textbf{Evi-F1 (TP-only)} measures evidence sentence F1 conditioned on correctly predicted triples, reflecting evidence quality independent of extraction errors. \textbf{Evi-F1 (joint)} includes false-positive and false-negative triples in the denominator following the DREEAM protocol~\citep{ma2023dreeam}, enabling cross-method evidence comparison. \textbf{EDCR} (Evidence-Decoupling Rati
…[truncated 10016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-18T06:46:27.421829+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-18T06:46:27.875535+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{EDCR as a diagnostic.}
5	EDCR (\S\ref{sec:edcr}) correlates strongly with extraction quality at the method level: Spearman $\rho = -0.965$ between EDCR and Rel-F1 (Table~\ref{tab:spectrum}), with GRPO QLoRA at 0.9876, SFT at 0.6982, and RSFT at 0.6503. At the per-relation level, EDCR correlates with Rel-F1 ($\rho = -0.793$) but is independent of Evi-F1 ($\rho = -0.064$), confirming extraction-evidence decoupling across relation types (Appendix~\ref{sec:edcr_per_relation}). RSFT avoids decoupling because discrete output selection prevents trading extraction for evidence quality (Appendix~\ref{sec:rsft_theory}). We provide qualitative examples of these phenomena in Appendix~\ref{sec:qualitative}.
6	
7	\paragraph{CED granularity.}
8	CED operates effectively at the response level for both RSFT selection and inference-time reranking, but fails at sentence-level granularity: filtering individual evidence sentences by NLI score reduces Evi-F1 by 7.7pp (Recall $-$20pp), as it disrupts co-reference chains across evidence sentences. This suggests that evidence quality is a holistic response property rather than a per-sentence attribute.
9	
10	\paragraph{Ablation.}
11	CED and flat-NLI produce comparable performance (Rel-F1 0.4563 vs.\ 0.4561); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\times$ fewer examples (Appendix~\ref{sec:ablation_full}).
12	
13	\paragraph{Practical implications.}
14	Our findings suggest three guidelines for practitioners seeking evidence-grounded IE: (1) avoid online RL for multi-objective generation tasks where capability coupling matters; (2) prefer RSFT with strict selection ($k{=}1$) over training data quantity; (3) consider CED reranking at inference for deployment scenarios requiring both high extraction accuracy and evidence quality.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-18T06:46:27.926409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-18T06:46:28.378769+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task for LLMs and compare three post-training paradigms across 85+ configurations. RL optimization pressure correlates with evidence-extraction decoupling severity (GRPO catastrophic, DPO gradual, RSFT none; EDCR $\rho = -0.965$), and the cost of joint evidence production follows a non-monotonic pattern across scales (+8pp at 1.7B, $-$7.5pp at 4B, near zero at 8B). RSFT with CED scoring yields +4.92pp Ign-F1 at 4B (four-seed mean); our 1.7B RSFT model (50.50 Ign-F1) matches 8B SFT (50.51) at a fraction of the cost.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-18T06:46:28.379201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-18T06:46:28.781038+00:00_

1	\section{Limitations}
2	
3	All results use the DocRED development set; test set submission is pending. Exact-match F1 penalizes surface-form-different entity mentions~\citep{wan2024genres}, likely underestimating absolute extraction capability, though relative comparisons remain valid.
4	
5	We evaluate one algorithm per RL family (GRPO, DPO); other algorithms may yield different results. CED scoring depends on an external NLI model, and the RSFT ablation uses limited seeds (four for CED, two for flat-NLI). The evidence tax pattern observed up to 8B may not extrapolate to larger scales. At 1.7B scale, 44.4\% of outputs exhibit repetitive patterns (vs.\ negligible at 4B+); small models may require decoding-time interventions (e.g., repetition penalty) for reliable deployment.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-18T06:46:28.881958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-18T06:46:28.882803+00:00_

1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to attention projections. SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	Base model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\
16	LoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\
17	LoRA $\alpha$ & 128 & 128 & 128 & 128 & 128 \\
18	Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
19	Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
20	Epochs & 3 & 3 & -- & -- & 1, 3\textsuperscript{$\star$} \\
21	Max steps & -- & -- & 100 & 100 & -- \\
22	Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	Max new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\
24	Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
25	Group size $G$ & -- & -- & 4 & 8 & -- \\
26	KL coefficient & -- & -- & 0.01 & 0.01 & -- \\
27	$\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\
28	Candidates $N$ & -- & 8 & -- & -- & 8 \\
29	Top-$k$ selection & -- & 1 & -- & -- & -- \\
30	Training samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\
31	Scoring function & -- & CED & CED & CED & CED \\
32	\bottomrule
33	\end{tabular}
34	\vspace{1mm}
35	{\raggedright\footnotesize \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction tra
…[truncated 14481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-18T06:46:35.613609+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-18T06:46:35.915283+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-18T06:46:36.418647+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_checklist.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "paper_checklist.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-18T06:46:37.122172+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'faith-evidence-ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-18T06:46:37.122732+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclrollingreview.org authors guidelines 2025 2026 page limit long paper short paper references appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclrollingreview.org authors guidelines 2025 2026 page limit long paper short paper references appendix"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-18T06:46:44.858735+00:00_

Web search results for query: "site:aclrollingreview.org authors guidelines 2025 2026 page limit long paper short paper references appendix"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines","url":"http://aclrollingreview.org/acguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results from the ACL Rolling Review website, here are the key author guidelines for 2025-2026 regarding page limits, papers, references, and appendices:

## Page Limits

Long papers for review versions may have up to eight (8) pages of content plus unlimited pages for references. The search results do not specify distinct page limits for short papers in the main guidelines, though they are mentioned as a separate category.

## References and Appendices

The limitations section, the optional ethical considerations section, references, and appendices should be included in the pdf for the paper (not counting towards the page limit), and not be submitted as a separate PDF.

## Formatting Requirements

Appendices are in double-column format, with the exception of math-heavy sections where single-colum
…[truncated 584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 7735
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-18T06:46:49.228915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-18T06:46:49.330112+00:00_

1	@inproceedings{autore2024,
2	  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},
3	  author    = {{Anonymous}},
4	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
5	  year      = {2024},
6	  url       = {https://arxiv.org/abs/2403.14888}
7	}
8	
9	@inproceedings{chen2025docksrag,
10	  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},
11	  author    = {Xu and others},
12	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
13	  year      = {2025},
14	  url       = {https://proceedings.mlr.press/v267/xu25am.html}
15	}
16	
17	@article{dai2025r1re,
18	  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},
19	  author  = {Dai, Runpeng and Zheng, Tong and others},
20	  journal = {arXiv preprint arXiv:2507.04642},
21	  year    = {2025},
22	  url     = {https://arxiv.org/abs/2507.04642}
23	}
24	
25	@inproceedings{gao2023scaling,
26	  title     = {Scaling Laws for Reward Model Overoptimization},
27	  author    = {Gao, Leo and Schulman, John and Hilton, Jacob},
28	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
29	  year      = {2023},
30	  url       = {https://arxiv.org/abs/2210.10760}
31	}
32	
33	@inproceedings{hu2022lora,
34	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
35	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
36	  booktitle = {International Conference on Learning Representations},
37	  year      = {2022},
38	  url       = {https://arxiv.org/abs/2106.09685}
39	}
40	
41	@article{jin2025rl_panacea,
42	  title   = {{RL} Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for {LLMs}},
43	  author  = {Jin, Hangzhan and others},
44	
…[truncated 10416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-18T06:46:50.033874+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclrollingreview.org cfp \"long papers\" \"8 pages\" \"short papers\" \"4 pages\" anonymity responsible NLP checklist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclrollingreview.org cfp \"long papers\" \"8 pages\" \"short papers\" \"4 pages\" anonymity responsible NLP checklist"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-18T06:46:57.437423+00:00_

Web search results for query: "site:aclrollingreview.org cfp "long papers" "8 pages" "short papers" "4 pages" anonymity responsible NLP checklist"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at master · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/master/cfp.md"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"aclrollingreview/cfp.md at main · vince-nlp/aclrollingreview","url":"https://github.com/vince-nlp/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS","url":"https://aclrollingreview-org.translate.goog/cfp?_x_tr_hl=ar&_x_tr_pto=tc&_x_tr_sch=http&_x_tr_sl=en&_x_tr_tl=ar"},{"title":"Call for Main Conference Papers - NAACL-HLT 2022","url":"https://2022.naacl.org/calls/papers/"}]

Based on the search results from aclrollingreview.org, here are the key findings regarding the CFP requirements you asked about:

**Paper Length Requirements:**
Short papers may consist of up to four (4) pages of content, plus unlimited pages of references. Long papers are limited to 8 pages (excluding the ethical considerations and limitations).

**Anonymity Requirements:**
Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)..." must be avoided.

**Responsible NLP Checklist:**
Authors must complete a responsible NLP research checklist as part of their paper submission. The conten
…[truncated 739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 7403
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-18T06:47:03.265200+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main_conference_papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main_conference_papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-18T06:47:05.277441+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-18T06:47:05.981278+00:00_

FILE_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-18T06:47:06.082338+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/agent/ 2>/dev/null | head -20",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/agent/ 2>/dev/null | head -20",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-18T06:47:06.133026+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-18T06:47:10.452481+00:00_

Web search results for query: "site:2026.emnlp.org calls main_conference_papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

I found the submission guidelines for EMNLP 2026 main conference papers. Here's a summary of the key information:

**Submission Process:**
Papers must follow ARR (ACL Rolling Review) procedures and be submitted by the ARR 2026 May cycle. Papers that have received reviews and meta-reviews from ARR may be committed to EMNLP via a commitment link.

**Paper Types and Scope:**
EMNLP 2026 invites submissions of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce new resources, argue positions, report linguistic insights, or reproduce (or fail to reproduce) previous results.

**Deadlines and Anonymity:**
All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth"). There is no anonymity period requirement.

**Review Process:**
The reviewing process wil
…[truncated 462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 7187
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-18T06:47:14.371634+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -20",
  "description": "Search for external review config in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -20",
    "description": "Search for external review config in project"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-18T06:47:14.573119+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-18T06:47:14.573530+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
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

_source line 65 · 2026-05-18T06:47:14.623986+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-18T06:47:40.672611+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
  "description": "List agent config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
    "description": "List agent config files"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-18T06:47:40.773602+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-18T06:47:44.639823+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ -name \"config*\" -o -name \"project*yaml\" -o -name \"project*json\" 2>/dev/null | head -20",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ -name \"config*\" -o -name \"project*yaml\" -o -name \"project*json\" 2>/dev/null | head -20",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-18T06:47:44.742636+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/.git/config
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/fontTools/config
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/configs

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-18T06:47:48.410304+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/ -maxdepth 3 -name \"project_config*\" -o -name \"projects.yaml\" -o -name \"projects.json\" 2>/dev/null | head -10",
  "description": "Find project config at root level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/ -maxdepth 3 -name \"project_config*\" -o -name \"projects.yaml\" -o -name \"projects.json\" 2>/dev/null | head -10",
    "description": "Find project config at root level"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-18T06:47:48.461074+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-18T06:47:51.826916+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -v \".venv\\|node_modules\\|__pycache__\" | head -20",
  "description": "Find yaml files at root level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -v \".venv\\|node_modules\\|__pycache__\" | head -20",
    "description": "Find yaml files at root level"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-18T06:47:51.877659+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-18T06:47:55.290312+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -l \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0513_6/workspace.yaml 2>/dev/null",
  "description": "Search for external review config in yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -l \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/config/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0513_6/workspace.yaml 2>/dev/null",
    "description": "Search for external review config in yaml files"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-18T06:47:55.405425+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 115
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-18T06:48:28.876418+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 1（方法与实验严谨性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references/appendix\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，禁止 self-identification\n- **附录规则**: 双栏格式，不计页数，reviewers 可选择是否阅读\n\n### 论文路径\n`projects/faith-evidence-ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n\n### 你的审查侧重：方法与实验严谨性\n\n请重点审查以下方面：\n\n1. **方法设计**\n   - Task formulation (§3.1) 是否合理？Evidence-grounded DocRE 的形式化定义是否严谨？\n   - CED scoring function (§3.4) 设计是否合理？NLI-based 对比打分的假设是否成立？\n   - EDCR metric (§3.5) 的定义和解释是否存在漏洞？\n\n2. **实验设计与统计可靠性**\n   - \"85+ configurations\" 的声称是否可验证？\n   - 主要 claim 的统计支撑是否充分？（seed 数量、variance 报告、显著性检验）\n   - Baseline 选择是否公平？是否遗漏关键 baseline？\n   - Evaluation protocol 是否标准？只使用 dev set 是否构成重大局限？\n\n3. **Claims 与证据对齐**\n   - 三个核心 finding（decoupling spectrum、scale-dependent tax、RSFT effectiveness）是否都有充分的实验支撑？\n   - Claim 的强度是否与证据匹配？是否存在过度声称（overclaim）？\n   - 因果性 vs 相关性：论文的因果推断是否合理？\n\n4. **消融与分析完整性**\n   - RSFT ablation（CED vs flat-NLI, k=1 vs k=3）是否充分？\n   - GRPO/DPO 的配置空间是否充分探索？（例如不同 KL 系数、不同 LoRA rank）\n   - Scale analysis 只有 3-4 个数据点，non-monotonic pattern 的 claim 是否 over-interpreted？\n\n5. **可复现性**\n   - Hyperparameters 是否完整报告？\n   - 数据处理 pipeline 是否可复现？\n\n请按 ARR 审稿标准输出完整审稿意见（Strengths / Weaknesses / Questions / Missing References / Overall Assessment）。评分使用 EMNLP 2026 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit。",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 1（方法与实验严谨性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references/appendix\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，禁止 self-identification\n- **附录规则**: 双栏格式，不计页数，reviewers 可选择是否阅读\n\n### 论文路径\n`projects/faith-evidence-ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n\n### 你的审查侧重：方法与实验严谨性\n\n请重点审查以下方面：\n\n1. **方法设计**\n   - Task formulation (§3.1) 是否合理？Evidence-grounded DocRE 的形式化定义是否严谨？\n   - CED scoring function (§3.4) 设计是否合理？NLI-based 对比打分的假设是否成立？\n   - EDCR metric (§3.5) 的定义和解释是否存在漏洞？\n\n2. **实验设计与统计可靠性**\n   - \"85+ configurations\" 的声称是否可验证？\n   - 主要 claim 的统计支撑是否充分？（seed 数量、variance 报告、显著性检验）\n   - Baseline 选择是否公平？是否遗漏关键 baseline？\n   - Evaluation protocol 是否标准？只使用 dev set 是否构成重大局限？\n\n3. **Claims 与证据对齐**\n   - 三个核心 finding（decoupling spectrum、scale-dependent tax、RSFT effectiveness）是否都有充分的实验支撑？\n   - Claim 的强度是否与证据匹配？是否存在过度声称（overclaim）？\n   - 因果性 vs 相关性：论文的因果推断是否合理？\n\n4. **消融与分析完整性**\n   - RSFT ablation（CED vs flat-NLI, k=1 vs k=3）是否充分？\n   - GRPO/DPO 的配置空间是否充分探索？（例如不同 KL 系数、不同 LoRA rank）\n   - Scale analysis 只有 3-4 个数据点，non-monotonic pattern 的 claim 是否 over-interpreted？\n\n5. **可复现性**\n   - Hyperparameters 是否完整报告？\n   - 数据处理 pipeline 是否可复现？\n\n请按 ARR 审稿标准输出完整审稿意见（Strengths / Weaknesses / Questions / Missing References / Overall Assessment）。评分使用 EMNLP 2026 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit。",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-18T06:48:46.060158+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17183
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-18T06:48:46.211294+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 2（新颖性、完整性与呈现质量）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references/appendix\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，禁止 self-identification\n- **附录规则**: 双栏格式，不计页数，reviewers 可选择是否阅读\n\n### 论文路径\n`projects/faith-evidence-ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n\n### 你的审查侧重：新颖性、完整性与呈现质量\n\n请重点审查以下方面：\n\n1. **新颖性与贡献定位**\n   - 核心贡献（decoupling spectrum、evidence tax、RSFT+CED）的新颖性如何？\n   - 是否存在已有工作解决了类似问题但论文未讨论？\n   - RSFT 本身是已有方法（STaR/RAFT 变体），论文对 \"what's new\" 的界定是否清晰？\n   - EDCR 作为 metric 的新颖性和通用性如何？\n\n2. **Related Work 覆盖与定位**\n   - 是否遗漏重要的相关工作？特别关注：\n     - 其他 LLM-based DocRE + evidence 的方法\n     - Multi-objective RL 中的类似 decoupling 现象\n     - NLI-based evidence evaluation 的其他工作\n   - 与已有方法的比较是否公平和完整？\n   - 引用是否充足？（当前 32 篇，EMNLP long paper 通常 40-60 篇）\n\n3. **写作质量**\n   - Abstract 是否在 30 秒内传达论文价值？\n   - Introduction 叙事线是否连贯？\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、黑名单词汇）？\n   - 专有名词是否首次出现时有定义？\n   - 段落过渡是否自然？\n\n4. **格式合规**\n   - 正文是否在 8 页内？（需要编译确认或目测估计）\n   - Limitations section 是否在 references 前且内容充实？\n   - 当前 Limitations 在 references 后（`\\appendix` 之前有 `\\bibliography`）——这是否符合 ARR 要求？\n   - 缺少 Responsible NLP Checklist 和 Ethics Statement——这是否构成 desk reject 风险？\n   - 参考文献格式是否符合 ACL 标准？bib 条目是否完整（注意 author 字段有 \"and others\" 和 \"{Anonymous}\"）？\n\n5. **图表质量**\n   - Figure 和 Table 的信息密度是否足够？\n   - Caption 是否自包含？\n   - 表格格式是否统一（小数精度、加粗/下划线规则）？\n\n6. **叙事统一性**\n   - Abstract → Introduction → Method → Experiments → Analysis → Conclusion 主线是否一致？\n   - 是否存在 \"Introduction 讲故事 A，Method 做故事 B\" 的问题？\n\n请按 ARR 审稿标准输出完整审稿意见（Strengths / Weaknesses / Questions / Missing References / Overall Assessment）。评分使用 EMNLP 2026 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit。",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 2（新颖性、完整性与呈现质量）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026 Main Conference Long Paper (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references/appendix\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind，禁止 self-identification\n- **附录规则**: 双栏格式，不计页数，reviewers 可选择是否阅读\n\n### 论文路径\n`projects/faith-evidence-ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）\n\n### 你的审查侧重：新颖性、完整性与呈现质量\n\n请重点审查以下方面：\n\n1. **新颖性与贡献定位**\n   - 核心贡献（decoupling spectrum、evidence tax、RSFT+CED）的新颖性如何？\n   - 是否存在已有工作解决了类似问题但论文未讨论？\n   - RSFT 本身是已有方法（STaR/RAFT 变体），论文对 \"what's new\" 的界定是否清晰？\n   - EDCR 作为 metric 的新颖性和通用性如何？\n\n2. **Related Work 覆盖与定位**\n   - 是否遗漏重要的相关工作？特别关注：\n     - 其他 LLM-based DocRE + evidence 的方法\n     - Multi-objective RL 中的类似 decoupling 现象\n     - NLI-based evidence evaluation 的其他工作\n   - 与已有方法的比较是否公平和完整？\n   - 引用是否充足？（当前 32 篇，EMNLP long paper 通常 40-60 篇）\n\n3. **写作质量**\n   - Abstract 是否在 30 秒内传达论文价值？\n   - Introduction 叙事线是否连贯？\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、黑名单词汇）？\n   - 专有名词是否首次出现时有定义？\n   - 段落过渡是否自然？\n\n4. **格式合规**\n   - 正文是否在 8 页内？（需要编译确认或目测估计）\n   - Limitations section 是否在 references 前且内容充实？\n   - 当前 Limitations 在 references 后（`\\appendix` 之前有 `\\bibliography`）——这是否符合 ARR 要求？\n   - 缺少 Responsible NLP Checklist 和 Ethics Statement——这是否构成 desk reject 风险？\n   - 参考文献格式是否符合 ACL 标准？bib 条目是否完整（注意 author 字段有 \"and others\" 和 \"{Anonymous}\"）？\n\n5. **图表质量**\n   - Figure 和 Table 的信息密度是否足够？\n   - Caption 是否自包含？\n   - 表格格式是否统一（小数精度、加粗/下划线规则）？\n\n6. **叙事统一性**\n   - Abstract → Introduction → Method → Experiments → Analysis → Conclusion 主线是否一致？\n   - 是否存在 \"Introduction 讲故事 A，Method 做故事 B\" 的问题？\n\n请按 ARR 审稿标准输出完整审稿意见（Strengths / Weaknesses / Questions / Missing References / Overall Assessment）。评分使用 EMNLP 2026 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit。",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-18T06:48:47.825574+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1614
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-18T06:48:53.500134+00:00_

Round 1 已启动。两名 Reviewer 已并行分配：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法与实验严谨性 | 审稿中 |
| R2 | 新颖性、完整性与呈现质量 | 审稿中 |

等待两名 Reviewer 返回初审意见后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 2

## Round 2

2 recorded events


### User

_source line 81 · 2026-05-18T06:53:49.107312+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — 方法与实验严谨性

**论文**: "Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction"
**目标 Venue**: EMNLP 2026 Main Conference Long Paper (ARR May 2026 cycle)

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 研究问题有价值、实验覆盖面广，但核心 claim 的统计支撑不足，多个关键实验存在混淆变量，且全部结果仅在 dev set 上报告，距离 Main Conference 的标准有明显差距。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心 claim（decoupling spectrum、non-monotonic scaling）的实验设计存在混淆变量，统计检验缺失，EDCR 方法级相关性仅基于 6 个数据点 |
| Excitement | 3.5/5 | 研究问题（LLM 时代 DocRE 的证据可验证性 vs 抽取精度权衡）切中实际需求，decoupling spectrum 概念有启发性 |
| Overall Assessment | 3.0/5 | 适合 Findings；需补充统计检验、解混淆 GRPO 实验、增加 test set 结果方可达 Conference 水平 |
| Reproducibility | 3/5 | 超参数基本报告完整，但 prompt template、entity mention 处理细节缺失；NLI 模型指定但 CED 聚合公式的细节不完整 |
| Reviewer Confidence | 4/5 | 熟悉 DocRE、RL alignment、NLI-based evaluation 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果推断

- 具体位置：§4.3 Table 2；§3.3 GRPO paragraph
- 问题：GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了**两个变量**：量化精度和 group size。论文将 catastrophic collapse 归因于"4-bit quantization constrains the effective parameter space"（§4.3 第二段），但无法排除 G=4 vs G=8 的影响。需要至少两个额外实验点：GRPO QLoRA G=8 和 GRPO bf16 G=4，才能解耦 quantization 和 group size 的效果。
- 为什么影响接收：Decoupling spectrum 是论文的第一核心贡献（Contribution 2），如果 GRPO catastrophic collapse 的归因不成立，整个 spectrum 叙事的因果链就断了。论文在 Introduction 第 29-30 行明确声称"QLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause"，这是一个因果性 claim，但实验设计无法支撑。
- 建议修改方向：补充 GRPO bf16 G=4 和 GRPO QLoRA G=8 实验；或将因果性表述降级为观察性表述（"we observe that the combination of QLoRA and smaller group size correlates with..."）。

**N2** [critical] 全部结果仅在 dev set 上报告，test set 结果缺失

- 具体位置：§4.1 Metrics 段最后一句 "All primary results use the development set; test set submission is pending"；Limitations §7 第一句
- 问题：对于一篇声称"85+ experimental configurations"的系统性实证研究，没有任何 test set 结果是严重缺陷。DocRED test set 有公开 leaderboard（CodaLab），提交并获取结果是标准做法。Dev set 可能导致超参数间接过拟合，尤其在多轮实验迭代中。
- 为什么影响接收：ARR soundness 标准要求"sufficient support for all of its claims"。论文在 Abstract 和 Introduction 中的数字（+4.92pp, 50.50 vs 50.51 等）全部基于 dev set，不能视为最终性能指标。审稿人无法判断这些结论是否在 test set 上成立。
- 建议修改方向：至少对 main results（Table 1 的 SFT / RSFT CED）和 scaling results（Table 3）提交 DocRED test set 评估。如果 test set 结果与 dev set 有较大偏差，需要更新叙事。

**N3** [critical] SFT baseline 缺少多 seed 方差，+4.92pp 改进缺乏统计显著性检验

- 具体位置：Table 1；§4.2 第一段
- 问题：RSFT CED 报告了 4-seed 均值 44.66±0.49，但 SFT baseline 仅有单 seed 结果 (39.74)。没有 SFT 的方差估计，无法判断 +4.92pp 的改进是否统计显著。假设 SFT 方差与 RSFT 类似（~0.49），+4.92pp 很可能显著；但 SFT 可能有更大方差（因为没有 CED 筛选的稳定化效果）。论文全文没有进行任何统计显著性检验（t-test、bootstrap、paired permutation test）。
- 为什么影响接收：这是论文的核心数字（出现在 Abstract、Introduction Contribution 4、Conclusion），如果不具备统计意义，所有下游结论都不可靠。
- 建议修改方向：(1) 对 SFT baseline 补充至少 3 个 seed 的结果；(2) 对所有主要对比进行 paired bootstrap 或 t-test；(3) 报告 p-value 和 confidence interval。

**N4** [critical] "Non-monotonic" scaling pattern 仅基于 3 个数据点，over-interpreted

- 具体位置：§4.4 Table 3；Introduction 第 31-33 行；Abstract 第 13 行
- 问题：Scale-dependent evidence tax 的 non-monotonic claim 基于 Qwen3 的 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28）。3 个点无法区分 non-monotonic pattern 与噪声或单点异常。特别是 1.7B 的 +8.04pp "benefit" 有严重的替代解释：论文自己在 Limitations 中承认"44.4% of outputs exhibit repetitive patterns"（§7 第 5 句），说明 1.7B 模型的 no-evidence 输出质量可能因 repetition 而被人为压低，evidence generation 的"benefit"可能仅仅是因为它迫使模型产生更长、更结构化的输出从而减少重复。此外，Abstract 中声称的"+8pp Ign-F1 benefit"在正文 §4.4 中被修正为"On a fair evaluation subset... this benefit is +6.2 points"，但这个 fair subset 的细节几乎没有交代。
- 为什么影响接收：Scale-dependent evidence tax 是 Contribution 3，也是论文标题中"Scaling"一词的核心支撑。如果 non-monotonic claim 不成立，论文的独特贡献大幅缩水。
- 建议修改方向：(1) 增加至少 1 个中间规模点（如 Qwen3-2.5B 或其他 ~3B 模型）验证 non-monotonicity；(2) 详细报告 1.7B "fair evaluation subset" 的构建方法和完整结果；(3) 对 1.7B 的 repetition 问题做 controlled analysis（如加 repetition penalty 后重新测 no-evidence baseline）；(4) 或将 claim 降级为"observed pattern across three scales"而非"non-monotonic"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] EDCR 方法级相关性 (ρ=-0.965) 仅基于 6 个数据点，统计意义存疑

- 具体位置：§3.5 第 64 行；§6 Analysis 第一段；Table 2
- 问题：Table 2 共 6 行（GRPO QLoRA, GRPO bf16, DPO 1ep, DPO 3ep, SFT, RSFT），Spearman ρ=-0.965 在 n=6 时 critical value at α=0.05 约为 0.886，因此虽然统计显著但 power 极低，且结果对单个点高度敏感。GRPO QLoRA 是一个极端 outlier（EDCR=0.9876, Rel-F1=0.0138），移除该点后相关性可能大幅下降。此外，DPO 3-epoch 使用了"pre-D076 evaluation protocol"（Table 2 footnote），与其他行不在同一评估标准下，进一步削弱相关性分析的可比性。
- 建议：(1) 报告去掉 GRPO QLoRA outlier 后的相关性；(2) 要么统一评估 protocol，要么将 DPO 3ep 从相关性计算中移除并标注清楚；(3) 考虑增加更多实验配置（如不同 KL coefficient 的 GRPO、不同 β 的 DPO）来增强样本量。

**W2** [warning] "1.7B RSFT matches 8B SFT" claim 基于单 seed，差异仅 0.01pp

- 具体位置：§4.4 Table 3 最后一句；Introduction Contribution 4；Abstract 第 14 行
- 问题：1.7B RSFT (50.50) vs 8B SFT (50.51) 差异 0.01pp，两者均为单 seed 结果（Table 8 caption："single seed for other scales"）。在没有方差估计的情况下，声称"matches"在统计上没有意义。任何合理的 seed variance 都远超 0.01pp。这个 claim 在 Abstract 和 Introduction 中被重复强调，但证据极弱。
- 建议：补充 1.7B RSFT 和 8B SFT 各 3-4 seeds 的结果，报告 confidence interval；或将 claim 改为"approaches"而非"matches"。

**W3** [warning] CED 与 flat-NLI 差异仅 0.02pp，contrastive component 的贡献未被证明

- 具体位置：§3.4 最后一段；§6 Ablation 段；Appendix Table 6
- 问题：CED (Rel-F1 0.4563) vs flat-NLI (0.4561)，差异 0.02pp，且 flat-NLI 仅有 2 seeds（Appendix §8）。论文承认"CED and flat-NLI produce comparable RSFT outcomes"但仍将 CED 作为默认选择，理由是"interpretable per-triple discrimination scores"。然而论文没有任何实验展示这种 interpretability 带来的实际价值。CED 的 contrastive component 增加了方法复杂度但没有带来可测量的改进，这削弱了 CED 作为方法贡献的意义。
- 建议：(1) flat-NLI 补充到 4 seeds 以做公平对比；(2) 如果差异仍不显著，诚实报告 contrastive component 可能不是必要的；(3) 或提供 case study 展示 CED 的 per-triple discrimination 在实际 error analysis 中如何优于 flat-NLI。

**W4** [warning] Baseline 对比不完整，缺少关键参照系

- 具体位置：§4.2 Table 1；§4.6 最后一段
- 问题：(1) 缺少与 encoder-based evidence methods (SAIS, DREEAM, EIDER) 在相同 evaluation protocol 下的直接对比。论文在 §4.6 提到 DREEAM 的 joint Evi-F1 为 54.01%，而本文最佳为 ~36%，但这个对比被放在 Appendix 中一笔带过。(2) 缺少与其他 LLM-based DocRE 方法（AutoRE、LMRC 等，均在 Related Work 中讨论）的抽取性能对比。(3) Post-hoc evidence 仅测试了 BM25，没有测试更强的 learned retriever。
- 建议：在 main results 中增加 SAIS/DREEAM 的数字作为参照（即使不同 protocol，也应在 Table 中注明并讨论差距来源）；增加至少一个 LLM-based DocRE baseline 的抽取性能对比。

**W5** [warning] RSFT ablation 缺少 random selection baseline

- 具体位置：§6 Ablation 段；Appendix §8
- 问题：RSFT 消融比较了 CED vs flat-NLI 和 k=1 vs k=3，但缺少一个关键 baseline：random selection（从 8 个 candidate 中随机选 1 个作为训练数据）。没有这个 baseline，无法确定 RSFT 的改进是来自"quality-based selection"还是简单的"data augmentation + selection"效应（即使随机选择也可能因为 sampling diversity 带来改进）。
- 建议：增加 random-k=1 baseline；如果 random 也有不错的改进，那 CED scoring 的贡献需要重新评估。

**W6** [warning] GRPO/DPO 超参数探索不足

- 具体位置：§3.3；Appendix Table 5
- 问题：GRPO 仅测试 KL=0.01，DPO 仅测试 β=0.1。在 RL/preference optimization 文献中，KL 系数和 β 对 reward hacking 和 performance tradeoff 有显著影响（Gao et al., 2023; Moskovitz et al., 2024 均被论文引用）。如果 GRPO 在更大 KL penalty 下不 collapse，或 DPO 在更小 β 下不 degrade，decoupling spectrum 的结论需要修改。
- 建议：至少对 GRPO 测试 KL ∈ {0.001, 0.01, 0.1} 和 DPO 测试 β ∈ {0.01, 0.1, 0.5}，或承认当前结论受限于特定超参数设置。

---

## 小问题（不影响接收）

- Table 1 格式不一致：Rel-F1 使用小数 (0.4049)，Evi-F1 使用百分比 (79.86)，EDCR 使用小数 (0.6982)。全表应统一。
- Appendix 中有 7 个 orphan bib entries（Aho:72, APA:83, Ando2005, Chandra:81, Gusfield:97, andrew2007scalable, rasooli-tetrault-2015），疑似 ACL 模板遗留，应清理。
- 引用 `autore2024` 的作者标注为 "Anonymous"，但该论文已正式发表（ACL 2024 System Demos），第一作者为 Xue 等人，应更新。类似地，`zhao2025egrpo`（E-GRPO）也标注 Anonymous。
- 引用 `wang2025relprior`、`zhang2025glidre`、`hu2025reinforcepp`、`wang2025rear` 的第一作者与 OpenAlex 记录不匹配，需核实。
- Appendix §14 Figure 4 caption 说"93 relation types"，但正文 §14 第一句说"76 relation types with ≥5 evaluation samples"，而 §4.1 说 DocRED 有 96 relation types。三个数字互相矛盾。
- §4.3 DPO 3-epoch 的脚注提到"pre-D076 evaluation protocol"，未解释 D076 是什么。内部编号不应出现在投稿论文中。
- §4.4 提到"fair evaluation subset"但未给出构建方法、样本量和完整结果。
- RSFT 的 training samples 为 2,718（Table 5），但 §3.3 说"9,042 training examples (37.3% acceptance rate)"，数字不一致（9,042 × 37.3% ≠ 2,718；24,216 → 9,042 是 ~37.3%，但 Table 5 报告 2,718 training samples）。需要解释 9,042 candidates 如何变成 2,718 training samples。

---

## 主要优势

1. **研究问题重要且定位精准**：LLM-based DocRE 缺乏 evidence grounding 是一个真实的实用性瓶颈，论文清晰地识别了 encoder-based evidence methods（SAIS/DREEAM）与 LLM-based extraction accuracy 之间的 gap（§1 第 16 行），问题动机有说服力。

2. **实验覆盖面广**：跨 4 个模型规模、2 个模型家族、2 个数据集、3 种优化范式的系统性比较在 DocRE 文献中确实罕见。即使个别实验的统计严谨性不足，这种横向覆盖本身也有参考价值。

3. **Decoupling spectrum 概念有启发性**：将 GRPO/DPO/RSFT 按 decoupling 严重程度排序的视角（Table 2）直观且有助于理解多目标生成任务中不同优化策略的行为差异。如果混淆变量问题得到修复，这将是一个有洞察力的贡献。

4. **RSFT 效果稳定**：4-seed 结果方差较低（±0.49），跨数据集（DocRED +4.92pp, Re-DocRED +4.86pp）和跨模型家族（LLaMA +1.74pp）的改进模式一致（§4.6），说明 rejection sampling approach 的鲁棒性。

5. **写作质量较好**：论文叙事结构清晰（问题→形式化→方法→实验→分析），Related Work 做了有效的 positioning（§2 区分了 encoder-based evidence 与 LLM-based generation 的结构性差异），不是简单的论文罗列。

---

## 缺失引用

- **KGC/知识图谱补全视角**：论文讨论了 DocRE 但未引用知识图谱构建相关工作，考虑到 Introduction 明确提到"knowledge graph construction"作为下游应用。
- **Multi-task learning / auxiliary loss 文献**：Evidence generation 作为辅助任务与 extraction 竞争 capacity 的分析框架，应引用 multi-task learning 的经典分析（如 Ruder 2017, Fifty et al. 2021 "Efficiently Identifying Task Groupings for Multi-Task Learning"）。
- **Chain-of-thought / rationale generation**：Evidence generation 在概念上类似 CoT rationale generation，相关的 faithful reasoning 文献（如 Lanham et al. 2023 "Measuring Faithfulness in Chain-of-Thought Reasoning"）可以丰富讨论。

---

## 总结

论文提出了一个有价值的研究问题，实验覆盖面令人印象深刻。但在方法论严谨性上有明显短板：核心实验存在未解耦的混淆变量（N1），全部结果缺少 test set 验证（N2），主要 claim 缺乏统计检验（N3），scaling claim 的数据点不足（N4）。这些问题的共同效果是：论文的 claim 强度系统性地超过了实验证据的支撑力度。如果能补充 test set 结果、解耦 GRPO 实验、增加统计检验，本文有潜力达到 Conference 水平。当前状态建议 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 82 · 2026-05-18T06:54:05.417836+00:00_

Reviewer 1 审稿意见已收到。评分 3.0 (Findings)，提出 4 个 critical issue（GRPO 混淆变量、无 test set、统计检验缺失、scaling claim 数据点不足）和 6 个 warning。

等待 Reviewer 2 审稿意见返回后启动交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 83 · 2026-05-18T06:54:08.093566+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.0 (Findings)** 的评分。论文研究问题有价值、实验覆盖面广，但存在 4 个 critical 问题：

1. **N1**: GRPO 实验同时改变量化精度和 group size，无法支撑 decoupling spectrum 的因果归因
2. **N2**: 全部结果仅在 dev set 上，缺少 test set 验证
3. **N3**: SFT baseline 无多 seed 方差，+4.92pp 改进未做显著性检验
4. **N4**: Non-monotonic scaling pattern 仅 3 个数据点，1.7B 的"benefit"有 repetition artifact 的替代解释

还有 6 个 should-fix 问题（EDCR 样本量不足、1.7B-vs-8B 单 seed claim、CED vs flat-NLI 无差异、baseline 不完整、缺 random selection ablation、GRPO/DPO 超参数探索不足）。核心判断：**claim 强度系统性超过证据支撑力度**，需补充实验后可升级至 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 84 · 2026-05-18T06:54:13.866613+00:00_

Reviewer 1 审稿意见已收到，记录完毕。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 4

## Round 4

6 recorded events


### User

_source line 85 · 2026-05-18T06:54:25.478186+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见 — Round 1

**论文**: "Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性、完整性与呈现质量

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 实验规模可观，scale-dependent evidence tax 是有价值的发现，但核心诊断指标 EDCR 存在定义循环性，CED 的独立贡献被自身消融实验否定，且存在关键数据不一致。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 实验覆盖广但 EDCR 存在定义循环问题，RSFT 训练数据量存在自相矛盾（9,042 vs 2,718），部分结论仅单 seed |
| Excitement | 3/5 | Scale-dependent evidence tax 有意思，decoupling spectrum 有实用价值，但 CED≈flat-NLI 削弱了方法贡献 |
| Reproducibility | 3/5 | 超参数详细，但仅 dev set 结果、部分 seed 不足、"pre-D076 evaluation protocol" 未解释 |
| Confidence | 4/5 | 熟悉 DocRE 和 LLM post-training 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] EDCR 与 Rel-F1 的相关性存在定义循环

- 具体位置：Section 3.5 (Eq. 2), Section 6 Analysis 第 1 段
- 问题：EDCR = Evi-Recall_TP / Rel-Recall。当 Rel-Recall 极低时（如 GRPO QLoRA Rel-F1=0.0138），EDCR 机械性趋近 1.0，与 evidence 质量无关。论文报告 EDCR 与 Rel-F1 的 Spearman ρ = -0.965，但 Rel-Recall 本身是 Rel-F1 的组成部分，这一相关性部分由定义构造而非经验发现。论文声称 "elevated EDCR signals problematic decoupling"，但 EDCR 的分母就是 Rel-Recall，它测量的不是独立于提取质量的 "decoupling"，而是 Rel-Recall 低时的数学必然结果。
- 为什么影响接收：EDCR 是论文四项贡献之一（Contribution 2），也是 decoupling spectrum 叙事的核心量化工具。如果指标本身有循环性问题，整个 spectrum 分析的说服力大打折扣。
- 建议修改方向：(1) 在 N=6 个方法配置上 ρ=-0.965 的统计意义有限（p 值应报告）；(2) 需要提供 EDCR 相对于简单替代指标（如 Evi-F1 - Rel-F1 差值、或 Evi-Recall_TP 本身）的增量诊断价值；(3) 对 EDCR 的分母效应做敏感性分析——当 Rel-Recall 大于某阈值时，EDCR 的诊断能力是否仍然成立？

**N2** [critical] CED 与 flat-NLI 几乎无差异，削弱方法贡献

- 具体位置：Section 3.4 末段, Section 6 Ablation, Appendix Table 5
- 问题：论文将 CED 列为核心贡献之一（"NLI-based Contrastive Evidence Discrimination scoring function"），但消融实验显示 CED 和 flat-NLI 的 Rel-F1 差距仅 0.02pp（0.4563 vs 0.4561），在统计上无法区分。论文承认 "CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection"，并将 CED 的优势归结为 "interpretable per-triple discrimination scores"，但论文正文中从未展示这一可解释性如何被实际利用（Qualitative Analysis 中的 Case 3 展示的是 EDCR，不是 CED）。
- 为什么影响接收：当论文自身的消融否定了 CED 相对于 flat-NLI 的量化优势时，将 CED 作为独立贡献（Contribution 4 中的 "NLI-based CED scoring"）是过度声称。审稿人会质疑：如果去掉 contrastive 项，结果一样，那真正的贡献到底是什么？
- 建议修改方向：(1) 诚实地将 CED 降级为 "一种可选的评分函数"，将真正的贡献定位为 "NLI-based quality filtering for RSFT" 而非 CED 本身；(2) 如果要保留 CED 作为贡献，需要展示 contrastive 项在某些场景下确实优于 flat-NLI（例如在 entity-dense 文档中、或在特定困难关系类型上）。

**N3** [critical] RSFT 训练数据量存在明确的数值矛盾

- 具体位置：Section 3.3 RSFT 段 vs Appendix Table 4
- 问题：Section 3.3 明确写道 "From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3% acceptance rate)"。但 Appendix Table 4 的 RSFT 行显示 "Training samples: 2,718"。如果 k=1（每个文档选最好的 1 个输出），最多得到约 3,053 个样本（=训练文档数），不可能是 9,042。9,042 ≈ 3,027 × 3，更像 k=3 的结果。而 2,718 < 3,053，说明部分文档被完全过滤，与 k=1 一致。这两个数字（9,042 vs 2,718）有 3.3 倍差距且不可调和。
- 为什么影响接收：训练数据量是 RSFT 方法的核心参数，直接影响实验可复现性。如果读者无法确定实际使用了多少训练数据，方法描述的可信度受损。
- 建议修改方向：检查并统一这两个数字，解释差异来源。如果存在额外的过滤步骤，需在方法部分明确描述。

**N4** [critical] 仅 Dev Set 结果，无 Test Set 提交

- 具体位置：Section 4.1 Metrics 末尾, Section 7 Limitations
- 问题：所有实验均在 DocRED dev set 上报告，test set 提交标注为 "pending"。DocRED 是一个有公开 leaderboard 的 benchmark，dev set 和 test set 的分布可能不同。Limitations 虽然承认了这一点，但对于 EMNLP 长文来说，完全缺少 test set 结果是一个重大缺陷。
- 为什么影响接收：审稿人无法验证方法在 held-out 数据上的泛化能力。如果 RSFT 的 4-seed 结果全部来自 dev set 上的调优，存在过拟合风险。
- 建议修改方向：在投稿前提交至少 Qwen3-4B SFT baseline 和 RSFT CED 的 test set 结果。如果 test set 提交受限，应在论文中详细解释原因。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 指标格式严重不一致

- 具体位置：Table 1, 2, 3, 5, 6（所有主要表格）
- 问题：同一表格中，Ign-F1 以百分比格式呈现（39.74），Rel-F1 以小数呈现（0.4049），Evi-F1 又以百分比呈现（79.86）。Ign-F1 39.74 和 Rel-F1 0.4049（≈40.49%）是同一量级的指标，但格式完全不同，极易造成误读。EDCR 0.6982 和 Evi-F1 79.86 并列时，读者需要额外心智负担判断哪个是比例哪个是百分比。
- 建议：全表统一为百分比格式或全统一为小数格式。

**W2** [warning] 引用数量偏低且多条 bib 条目不完整

- 具体位置：references.bib 全文
- 问题：(1) 总计 32 篇引用，EMNLP long paper 通常 40-60 篇。(2) 15/32 条 bib 条目使用 "and others" 代替完整作者列表（如 `chen2025docksrag`, `dai2025r1re`, `jin2025rl_panacea`, `ito2025mogrpo`, `liu2026gdpo`, `liu2025drgrpo`, `yu2025dapo`, `chen2025dragrpo`, `wang2025rear`, `wang2025relprior`, `zhang2025glidre`, `tang2025rsftppo`, `wang2025rullm`）。(3) 两条使用 `{Anonymous}` 作为作者（`autore2024`, `zhao2025egrpo`）。ACL style 要求完整作者列表，"and others" 不是标准 BibTeX 用法（应为 "and others" → 实际作者名 or 至少 "and others" 需改为完整列表）。`autore2024` 有真实作者（Xue et al.），不应标记为 Anonymous。
- 建议：补全所有作者列表，将 Anonymous 替换为真实作者信息（如果已发表）。

**W3** [warning] 1.7B Evidence Benefit 的解释缺乏充分支撑

- 具体位置：Section 4.4, Table 3
- 问题：1.7B 模型从 evidence generation 中获得 +8.04pp 的收益，论文将其归因于 "implicit regularization, forcing the model to attend to supporting context rather than memorizing surface-level patterns"。但：(1) 这一解释是推测性的，无实验支撑（例如 attention pattern 分析、memorization 指标）；(2) Limitations 承认 1.7B 有 44.4% 的 repetitive pattern 问题，这可能严重混淆 evidence benefit 的测量——如果 no-evidence 模型在 1.7B 下更容易产生重复输出，Ign-F1 下降可能是重复导致的，而非 evidence 的正面效应；(3) "fair evaluation subset" 上的 +6.2pp 仅一句话带过，未给出 subset 定义和完整数据。
- 建议：(1) 详细定义 "fair evaluation subset"，将完整结果放入正文或附录表格；(2) 分析 1.7B no-evidence 模型的 repetition rate，排除重复输出对 Ign-F1 差异的贡献；(3) 对 "implicit regularization" 假说提供至少一个定量证据。

**W4** [warning] Multi-seed 覆盖不均匀

- 具体位置：Table 3 (scaling), Appendix Table 6 (cross_detail)
- 问题：4B 的 RSFT 有 4-seed 均值 (sd=0.49)，但 1.7B、8B、LLaMA-3.1-8B 均为单 seed（Appendix Table 6 caption 确认 "single seed for other scales"）。LLaMA 有第二个 seed（s43: 56.19，在 Appendix 文字中提到），但 Qwen3-1.7B 和 Qwen3-8B 的 RSFT 增益（+2.64, +3.82）基于单次运行。考虑到 4B 上 4 个 seed 的范围为 44.16-45.12（接近 1pp），单 seed 结果的 RSFT 增益可信度有限。
- 建议：至少在 1.7B 和 8B 上报告 2-seed 结果，或在论文中明确标注哪些数字基于单 seed 并讨论 variance 风险。

**W5** [warning] Related Work 缺少重要相关方向

- 具体位置：Section 2
- 问题：
  (1) **Multi-task learning / task interference**: 论文的核心发现——extraction 和 evidence 在梯度优化中竞争——与 multi-task learning 中的 negative transfer / gradient conflict 文献直接相关（如 Standley et al. 2020 "Which Tasks Should Be Learned Together"; Yu et al. 2020 "Gradient Surgery for Multi-Task Learning"）。这些工作提供了理论框架来解释为什么 GRPO 导致 decoupling，但论文完全未讨论。
  (2) **Self-consistency / majority voting**: RSFT 的 "sample N, select best" 与 Wang et al. 2023 "Self-Consistency Improves Chain of Thought Reasoning" 在方法论上高度相似。论文引用了 STaR 和 RAFT，但未提及 self-consistency 这一更广泛的范式。
  (3) 缺少与 encoder-based evidence 方法的直接数值比较。论文提到 "our best joint Evi-F1 (0.36) falls below supervised DREEAM (54.01%)"（Section 4.6），但这一比较被放在最后一段轻描淡写处理，且未出现在任何表格中。读者无法快速评估 LLM-based 方法与 encoder-based 方法的整体差距。
- 建议：(1) 增加一段讨论 multi-task learning 中 task interference 的文献并建立联系；(2) 引用 self-consistency；(3) 在 main results 或 generalization 中增加一个表格，直接与 SAIS/DREEAM/EIDER 做 head-to-head 对比（即使在不同模型架构下）。

**W6** [warning] "pre-D076 evaluation protocol" 未解释

- 具体位置：Table 2 脚注, Section 4.3 DPO 段
- 问题：DPO 3-epoch 结果标注为 "Pre-D076 evaluation protocol"，但论文从未解释 D076 是什么、pre-D076 和当前 protocol 有何差异、为什么仍将这些不可比较的结果纳入 Table 2。如果评估协议不同，这些数字是否应该出现在同一个表中？
- 建议：要么解释 D076 并量化 protocol 差异的影响，要么将 DPO 3ep 结果移至附录并在正文中明确说明不可直接比较。

---

## 小问题（不影响接收）

1. **Per-relation EDCR 图的 caption 与正文不一致**: Figure 5 caption 说 "93 relation types"，Analysis 正文说 "76 relation types with ≥5 evaluation samples"，DocRED 标注的是 96 relation types。三个数字互相矛盾。
2. **Abstract 偏长且数据密集**: 当前 Abstract 约 230 words，"Three findings emerge" 之后的三段各带具体数字，读起来像实验结果摘要而非叙事。建议压缩 Finding 3 中的具体数字，保留趋势描述。
3. **Contribution 列表中 "85+ experiments" 的计算方式未交代**: 85+ 如何计算？是 (方法×模型×seed×数据集) 的组合数？读者无法验证。
4. **Section 4.5 Evidence Strategy Comparison 中的 "CED reranking at inference time"**: 这一方法在 Method 部分没有描述，突然出现在实验中。应在 Method 中至少用一段描述 inference-time reranking 的流程。
5. **Appendix 中 GRPO dynamics Figure 3 引用了 "G=4 QLoRA" 和 "G=8 bf16" 但 caption 说 "(a) Relation F1 across checkpoints"**: 无法从当前文本判断图中各曲线是否有 legend 标注。

---

## 主要优势

1. **实验规模和系统性**: 跨 4 个模型规模、2 个模型家族、2 个数据集、3 个优化范式的对比在 LLM-based DocRE 领域是罕见的。85+ 配置的覆盖面使得结论比单模型/单方法的工作更可信。

2. **Scale-dependent evidence tax 是真正有意思的发现**: 1.7B 受益、4B 受损、8B 中性的非单调模式打破了 "evidence 一定损害 extraction" 的简单假设。即使 1.7B 的具体解释需要加强，这一经验发现本身对后续研究有指导意义。

3. **问题定义有价值**: 将 evidence-grounded DocRE 形式化为 LLM 的结构化生成任务，并系统研究 evidence 生产的代价，是一个有意义的问题定义。现有 LLM-based DocRE 工作确实忽略了 evidence 生成。

4. **Decoupling spectrum 的诊断价值**: 尽管 EDCR 的定义有循环性问题，GRPO catastrophic collapse 的定性发现（模型放弃正确关系类型转而生成自由文本标签）是有实践意义的警示，对计划在 IE 任务上使用 GRPO 的研究者有直接参考价值。

5. **写作质量整体良好**: 无 em-dash，无过度 AI 写作标志词，段落过渡自然，叙事主线基本统一。Limitations section 位置正确（references 之前），内容诚实。

6. **RSFT 的 "discrete selection avoids gradient-based trade-off" 洞察有一般性意义**: 这一观察超越了 DocRE 任务本身，对所有多目标 LLM post-training 场景有参考价值。

---

## 叙事统一性评估

Abstract → Introduction → Method → Experiments → Analysis → Conclusion 的主线基本一致：都围绕 "evidence generation 的代价及其与优化方法的关系" 展开。未发现 "Introduction 讲故事 A，Method 做故事 B" 的问题。

但存在一个轻微的叙事张力：Introduction 将 CED 作为关键创新之一推介（Contribution 4），但 Analysis 中的消融显示 CED ≈ flat-NLI。这使得 Introduction 的 framing 与 Analysis 的结论存在落差。建议在 Introduction 中更诚实地定位 CED（作为评分选择的一种实现，而非核心创新）。

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ⚠️ 无法编译确认 | 从 section 数量和内容密度看，8 页可能紧张但未明显超限 |
| Limitations 位置 | ✅ | 在 `\bibliography` 之前，符合 ARR 要求 |
| Double-blind | ✅ | `\author{Anonymous}`，`[review]` option |
| Responsible NLP Checklist | ❌ 缺失 | 论文 .tex 中未见，也未在附录中出现。如果仅通过 OpenReview 提交则无问题，但需确认 |
| Ethics Statement | ⚠️ 缺失 | ARR 鼓励但不强制 |
| 参考文献格式 | ❌ 有问题 | 15/32 条 "and others"，2 条 Anonymous（见 W2） |

---

## 缺失引用建议

1. Standley et al. (2020) "Which Tasks Should Be Learned Together in Multi-Task Learning?" — task interference
2. Yu et al. (2020) "Gradient Surgery for Multi-Task Learning" — gradient conflict
3. Wang et al. (2023) "Self-Consistency Improves Chain of Thought Reasoning in Language Models" — sample-then-select paradigm
4. 建议补充 2-3 篇 encoder-based DocRE 近年工作以增加引用密度


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-18T06:55:00.269952+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验规模可观，scale-dependent evidence tax 是有价值的发现，但核心诊断指标 EDCR 存在定义循环性，CED 的独立贡献被自身消融实验否定，且存在关键数据不一致。\n\n## Must-Fix 问题\n\n**N1** [critical] EDCR 与 Rel-F1 的相关性存在定义循环\n\n- EDCR = Evi-Recall_TP / Rel-Recall。当 Rel-Recall 极低时（如 GRPO QLoRA Rel-F1=0.0138），EDCR 机械性趋近 1.0，与 evidence 质量无关。论文报告 EDCR 与 Rel-F1 的 Spearman ρ = -0.965，但 Rel-Recall 本身是 Rel-F1 的组成部分，这一相关性部分由定义构造而非经验发现。\n- 建议：(1) 报告 p 值；(2) 提供 EDCR 相对于简单替代指标的增量诊断价值；(3) 对分母效应做敏感性分析。\n\n**N2** [critical] CED 与 flat-NLI 几乎无差异，削弱方法贡献\n\n- CED 和 flat-NLI 的 Rel-F1 差距仅 0.02pp。论文承认 \"CED's contrastive design does not substantially outperform simpler NLI scoring\"，但仍将 CED 作为独立贡献。消融否定了 CED 的量化优势。\n- 建议：将 CED 降级为可选评分函数，将贡献定位为 \"NLI-based quality filtering for RSFT\"。\n\n**N3** [critical] RSFT 训练数据量存在明确的数值矛盾\n\n- Section 3.3 说 \"9,042 training examples (37.3% acceptance rate)\"，Appendix Table 4 说 \"Training samples: 2,718\"。9,042 vs 2,718 有 3.3 倍差距且不可调和。\n- 建议：检查并统一这两个数字。\n\n**N4** [critical] 仅 Dev Set 结果，无 Test Set 提交\n\n- 所有实验均在 DocRED dev set 上报告，test set 提交为 \"pending\"。\n\n## Should-Fix 问题\n\n**W1** [warning] 指标格式严重不一致\n- Ign-F1 百分比格式（39.74），Rel-F1 小数格式（0.4049），Evi-F1 百分比（79.86）。\n\n**W2** [warning] 引用数量偏低且多条 bib 条目不完整\n- 32 篇引用（EMNLP long paper 通常 40-60 篇），15/32 条 \"and others\"，2 条 Anonymous。\n\n**W3** [warning] 1.7B Evidence Benefit 的解释缺乏充分支撑\n- \"implicit regularization\" 解释是推测性的，无实验支撑；\"fair evaluation subset\" 未详细定义。\n\n**W4** [warning] Multi-seed 覆盖不均匀\n- 4B 有 4-seed，1.7B/8B/LLaMA 为单 seed 或 2 seed。\n\n**W5** [warning] Related Work 缺少重要相关方向\n- 缺少 multi-task learning / task interference 文献、self-consistency 范式、与 encoder-based 方法的直接数值比较。\n\n**W6** [warning] \"pre-D076 evaluation protocol\" 未解释\n\n## 缺失引用\n1. Standley et al. (2020) \"Which Tasks Should Be Learned Together in Multi-Task Learning?\"\n2. Yu et al. (2020) \"Gradient Surgery for Multi-Task Learning\"\n3. Wang et al. (2023) \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\"\n\n## 主要优势\n1. 实验规模和系统性\n2. Scale-dependent evidence tax 是有意思的发现\n3. 问题定义有价值\n4. Decoupling spectrum 的诊断价值\n5. 写作质量整体良好\n6. RSFT \"discrete selection avoids gradient-based trade-off\" 洞察有一般性意义",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验规模可观，scale-dependent evidence tax 是有价值的发现，但核心诊断指标 EDCR 存在定义循环性，CED 的独立贡献被自身消融实验否定，且存在关键数据不一致。\n\n## Must-Fix 问题\n\n**N1** [critical] EDCR 与 Rel-F1 的相关性存在定义循环\n\n- EDCR = Evi-Recall_TP / Rel-Recall。当 Rel-Recall 极低时（如 GRPO QLoRA Rel-F1=0.0138），EDCR 机械性趋近 1.0，与 evidence 质量无关。论文报告 EDCR 与 Rel-F1 的 Spearman ρ = -0.965，但 Rel-Recall 本身是 Rel-F1 的组成部分，这一相关性部分由定义构造而非经验发现。\n- 建议：(1) 报告 p 值；(2) 提供 EDCR 相对于简单替代指标的增量诊断价值；(3) 对分母效应做敏感性分析。\n\n**N2** [critical] CED 与 flat-NLI 几乎无差异，削弱方法贡献\n\n- CED 和 flat-NLI 的 Rel-F1 差距仅 0.02pp。论文承认 \"CED's contrastive design does not substantially outperform simpler NLI scoring\"，但仍将 CED 作为独立贡献。消融否定了 CED 的量化优势。\n- 建议：将 CED 降级为可选评分函数，将贡献定位为 \"NLI-based quality filtering for RSFT\"。\n\n**N3** [critical] RSFT 训练数据量存在明确的数值矛盾\n\n- Section 3.3 说 \"9,042 training examples (37.3% acceptance rate)\"，Appendix Table 4 说 \"Training samples: 2,718\"。9,042 vs 2,718 有 3.3 倍差距且不可调和。\n- 建议：检查并统一这两个数字。\n\n**N4** [critical] 仅 Dev Set 结果，无 Test Set 提交\n\n- 所有实验均在 DocRED dev set 上报告，test set 提交为 \"pending\"。\n\n## Should-Fix 问题\n\n**W1** [warning] 指标格式严重不一致\n- Ign-F1 百分比格式（39.74），Rel-F1 小数格式（0.4049），Evi-F1 百分比（79.86）。\n\n**W2** [warning] 引用数量偏低且多条 bib 条目不完整\n- 32 篇引用（EMNLP long paper 通常 40-60 篇），15/32 条 \"and others\"，2 条 Anonymous。\n\n**W3** [warning] 1.7B Evidence Benefit 的解释缺乏充分支撑\n- \"implicit regularization\" 解释是推测性的，无实验支撑；\"fair evaluation subset\" 未详细定义。\n\n**W4** [warning] Multi-seed 覆盖不均匀\n- 4B 有 4-seed，1.7B/8B/LLaMA 为单 seed 或 2 seed。\n\n**W5** [warning] Related Work 缺少重要相关方向\n- 缺少 multi-task learning / task interference 文献、self-consistency 范式、与 encoder-based 方法的直接数值比较。\n\n**W6** [warning] \"pre-D076 evaluation protocol\" 未解释\n\n## 缺失引用\n1. Standley et al. (2020) \"Which Tasks Should Be Learned Together in Multi-Task Learning?\"\n2. Yu et al. (2020) \"Gradient Surgery for Multi-Task Learning\"\n3. Wang et al. (2023) \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\"\n\n## 主要优势\n1. 实验规模和系统性\n2. Scale-dependent evidence tax 是有意思的发现\n3. 问题定义有价值\n4. Decoupling spectrum 的诊断价值\n5. 写作质量整体良好\n6. RSFT \"discrete selection avoids gradient-based trade-off\" 洞察有一般性意义",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-18T06:55:35.101987+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34832
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-18T06:55:35.253122+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n---\n\n# Reviewer 1 审稿意见 — Round 1\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 研究问题有价值、实验覆盖面广，但核心 claim 的统计支撑不足，多个关键实验存在混淆变量，且全部结果仅在 dev set 上报告。\n\n## Must-Fix 问题\n\n**N1** [critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果推断\n\n- GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了两个变量：量化精度和 group size。论文将 catastrophic collapse 归因于 \"4-bit quantization constrains the effective parameter space\"，但无法排除 G=4 vs G=8 的影响。\n- Introduction 第 29-30 行声称 \"QLoRA acts as a catastrophic amplifier\" 是因果性 claim，但实验设计无法支撑。\n- 建议：补充 GRPO bf16 G=4 和 GRPO QLoRA G=8 实验；或将因果性表述降级。\n\n**N2** [critical] 全部结果仅在 dev set 上报告，test set 结果缺失\n\n- 85+ configurations 的系统性实证研究没有任何 test set 结果。DocRED test set 有公开 leaderboard（CodaLab），提交是标准做法。\n- 建议：至少对 main results 提交 test set 评估。\n\n**N3** [critical] SFT baseline 缺少多 seed 方差，+4.92pp 改进缺乏统计显著性检验\n\n- RSFT CED 有 4-seed 均值 44.66±0.49，但 SFT baseline 仅单 seed (39.74)。没有 SFT 方差无法判断 +4.92pp 是否显著。全文无统计显著性检验。\n- 建议：SFT 补充 3+ seeds，进行 paired bootstrap 或 t-test。\n\n**N4** [critical] \"Non-monotonic\" scaling pattern 仅基于 3 个数据点，over-interpreted\n\n- 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28）无法区分 non-monotonic pattern 与噪声。1.7B 的 +8.04 有替代解释（44.4% repetition → no-evidence 被人为压低）。Abstract 的 \"+8pp\" 在正文被修正为 \"+6.2 on fair subset\"，fair subset 细节缺失。\n- 建议：增加中间规模点；详细报告 fair evaluation subset；对 repetition 做 controlled analysis；或将 claim 降级。\n\n## Should-Fix 问题\n\n**W1** [warning] EDCR 方法级相关性 (ρ=-0.965) 仅基于 6 个数据点\n- n=6 时 power 极低，GRPO QLoRA 是极端 outlier，DPO 3ep 用了不同评估 protocol。\n- 建议：报告去掉 outlier 后的相关性；统一评估 protocol。\n\n**W2** [warning] \"1.7B RSFT matches 8B SFT\" claim 基于单 seed，差异仅 0.01pp\n- 50.50 vs 50.51，均为单 seed。任何合理方差远超 0.01pp。\n- 建议：补充多 seed 结果或将 \"matches\" 改为 \"approaches\"。\n\n**W3** [warning] CED 与 flat-NLI 差异仅 0.02pp，contrastive component 的贡献未被证明\n- flat-NLI 仅 2 seeds。论文没有实验展示 interpretability 的实际价值。\n- 建议：补充 flat-NLI seeds；或诚实报告 contrastive 可能不必要。\n\n**W4** [warning] Baseline 对比不完整\n- 缺少与 SAIS/DREEAM/EIDER 的直接对比；缺少与 AutoRE/LMRC 的抽取性能对比；post-hoc 仅测 BM25。\n- 建议：增加 encoder-based 和 LLM-based baseline 数字。\n\n**W5** [warning] RSFT ablation 缺少 random selection baseline\n- 无法确定改进来自 quality-based selection 还是 sampling diversity。\n- 建议：增加 random-k=1 baseline。\n\n**W6** [warning] GRPO/DPO 超参数探索不足\n- GRPO 仅 KL=0.01，DPO 仅 β=0.1。\n- 建议：至少测试 KL ∈ {0.001, 0.01, 0.1}，β ∈ {0.01, 0.1, 0.5}。\n\n## 缺失引用\n- Multi-task learning / auxiliary loss 文献（Ruder 2017, Fifty et al. 2021）\n- Chain-of-thought / rationale generation 忠实性文献（Lanham et al. 2023）\n- KGC/知识图谱补全相关工作\n\n## 主要优势\n1. 研究问题重要且定位精准\n2. 实验覆盖面广\n3. Decoupling spectrum 概念有启发性\n4. RSFT 效果稳定（4-seed, 跨数据集, 跨模型家族）\n5. 写作质量较好",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n---\n\n# Reviewer 1 审稿意见 — Round 1\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 研究问题有价值、实验覆盖面广，但核心 claim 的统计支撑不足，多个关键实验存在混淆变量，且全部结果仅在 dev set 上报告。\n\n## Must-Fix 问题\n\n**N1** [critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果推断\n\n- GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了两个变量：量化精度和 group size。论文将 catastrophic collapse 归因于 \"4-bit quantization constrains the effective parameter space\"，但无法排除 G=4 vs G=8 的影响。\n- Introduction 第 29-30 行声称 \"QLoRA acts as a catastrophic amplifier\" 是因果性 claim，但实验设计无法支撑。\n- 建议：补充 GRPO bf16 G=4 和 GRPO QLoRA G=8 实验；或将因果性表述降级。\n\n**N2** [critical] 全部结果仅在 dev set 上报告，test set 结果缺失\n\n- 85+ configurations 的系统性实证研究没有任何 test set 结果。DocRED test set 有公开 leaderboard（CodaLab），提交是标准做法。\n- 建议：至少对 main results 提交 test set 评估。\n\n**N3** [critical] SFT baseline 缺少多 seed 方差，+4.92pp 改进缺乏统计显著性检验\n\n- RSFT CED 有 4-seed 均值 44.66±0.49，但 SFT baseline 仅单 seed (39.74)。没有 SFT 方差无法判断 +4.92pp 是否显著。全文无统计显著性检验。\n- 建议：SFT 补充 3+ seeds，进行 paired bootstrap 或 t-test。\n\n**N4** [critical] \"Non-monotonic\" scaling pattern 仅基于 3 个数据点，over-interpreted\n\n- 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28）无法区分 non-monotonic pattern 与噪声。1.7B 的 +8.04 有替代解释（44.4% repetition → no-evidence 被人为压低）。Abstract 的 \"+8pp\" 在正文被修正为 \"+6.2 on fair subset\"，fair subset 细节缺失。\n- 建议：增加中间规模点；详细报告 fair evaluation subset；对 repetition 做 controlled analysis；或将 claim 降级。\n\n## Should-Fix 问题\n\n**W1** [warning] EDCR 方法级相关性 (ρ=-0.965) 仅基于 6 个数据点\n- n=6 时 power 极低，GRPO QLoRA 是极端 outlier，DPO 3ep 用了不同评估 protocol。\n- 建议：报告去掉 outlier 后的相关性；统一评估 protocol。\n\n**W2** [warning] \"1.7B RSFT matches 8B SFT\" claim 基于单 seed，差异仅 0.01pp\n- 50.50 vs 50.51，均为单 seed。任何合理方差远超 0.01pp。\n- 建议：补充多 seed 结果或将 \"matches\" 改为 \"approaches\"。\n\n**W3** [warning] CED 与 flat-NLI 差异仅 0.02pp，contrastive component 的贡献未被证明\n- flat-NLI 仅 2 seeds。论文没有实验展示 interpretability 的实际价值。\n- 建议：补充 flat-NLI seeds；或诚实报告 contrastive 可能不必要。\n\n**W4** [warning] Baseline 对比不完整\n- 缺少与 SAIS/DREEAM/EIDER 的直接对比；缺少与 AutoRE/LMRC 的抽取性能对比；post-hoc 仅测 BM25。\n- 建议：增加 encoder-based 和 LLM-based baseline 数字。\n\n**W5** [warning] RSFT ablation 缺少 random selection baseline\n- 无法确定改进来自 quality-based selection 还是 sampling diversity。\n- 建议：增加 random-k=1 baseline。\n\n**W6** [warning] GRPO/DPO 超参数探索不足\n- GRPO 仅 KL=0.01，DPO 仅 β=0.1。\n- 建议：至少测试 KL ∈ {0.001, 0.01, 0.1}，β ∈ {0.01, 0.1, 0.5}。\n\n## 缺失引用\n- Multi-task learning / auxiliary loss 文献（Ruder 2017, Fifty et al. 2021）\n- Chain-of-thought / rationale generation 忠实性文献（Lanham et al. 2023）\n- KGC/知识图谱补全相关工作\n\n## 主要优势\n1. 研究问题重要且定位精准\n2. 实验覆盖面广\n3. Decoupling spectrum 概念有启发性\n4. RSFT 效果稳定（4-seed, 跨数据集, 跨模型家族）\n5. 写作质量较好",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-18T06:55:36.862395+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1609
}
```

</details>

---


### Assistant

_source line 90 · 2026-05-18T06:55:40.770584+00:00_

交叉分享已发送。两位 Reviewer 将逐条回应对方的审稿意见（[AGREE]/[REBUT]），等待交叉回应返回后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 91 · 2026-05-18T06:55:43.643196+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交。

**总结**: Overall 3.0 (Findings)。主要 Must-Fix 问题四项：(1) EDCR 与 Rel-F1 的相关性存在定义循环——分母就是 Rel-Recall，高相关性部分是数学构造而非经验发现；(2) CED 与 flat-NLI 的消融差距仅 0.02pp，论文自身的实验否定了 CED 作为独立贡献的合理性；(3) RSFT 训练数据量在方法部分（9,042）和附录超参表（2,718）之间存在 3.3 倍的不可调和矛盾；(4) 全部结果仅在 dev set 上报告。

实验规模和 scale-dependent evidence tax 的发现是论文的核心价值。写作质量整体良好，无明显 AI 痕迹，叙事主线统一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 92 · 2026-05-18T06:55:49.322107+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 93 · 2026-05-18T06:56:47.641502+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: EDCR 与 Rel-F1 的定义循环性**

同意，且我认为 R2 在此点上的分析比我自己的审稿更精确。我在 R1-W1 中指出了 n=6 样本量和 GRPO QLoRA outlier 的问题，但 R2 抓住了更根本的缺陷：EDCR 的分母包含 Rel-Recall，而 Rel-F1 本身是 Rel-Recall 和 Rel-Precision 的调和平均。ρ=-0.965 的相关性在数学上被定义关系部分预设了，不完全是经验发现。

补充证据：§3.5 第 62-63 行的 EDCR 解释案例恰好说明了这个问题。论文说"A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high Evi-Recall_TP and low Rel-Recall, yielding a high EDCR"。这本质上是在说：当 Rel-Recall 低时 EDCR 高。而 Rel-Recall 低自然对应 Rel-F1 低（在 precision 不极端变化的情况下）。因此 EDCR 与 Rel-F1 的负相关性部分是 tautological 的。

进一步地，论文在 §6 声称 per-relation EDCR 与 Evi-F1 独立（ρ=-0.064, p=0.58），将此作为"evidence quality and extraction ability are fully decoupled across relation types"的证据（Appendix §14）。但"不显著相关"不等于"fully decoupled"，这是一个经典的"absence of evidence ≠ evidence of absence"错误，尤其在 76 个 relation types 中可能存在 power 不足的情况。

R2 的三条建议（报告 p 值、增量诊断价值、敏感性分析）均合理。我补充建议：作者应在去除 GRPO QLoRA 极端点后重新计算相关性，并展示 EDCR 相对于更简单替代指标（如 Evi-F1 - Rel-F1 差值）是否提供额外诊断信息。

**[AGREE] R2-N2: CED 与 flat-NLI 几乎无差异**

完全同意，与我的 R1-W3 一致。论文的消融数据（Appendix §8）自己否定了 CED contrastive component 的量化贡献：CED Rel-F1 0.4563 vs flat-NLI 0.4561，差距 0.02pp。flat-NLI 仅有 2 seeds，但即便如此，0.02pp 的差距在任何合理的 variance 下都不可能显著。

R2 的建议（将贡献定位为 "NLI-based quality filtering for RSFT"）比论文当前的表述更准确。论文在 §3.4 最后一段承认了这一点（"CED and flat-NLI produce comparable RSFT outcomes"），但 Introduction Contribution 列表仍然将 CED 作为独立贡献（Contribution 4: "RSFT with NLI-based CED scoring"）。叙事与数据之间存在张力。

补充：§6 Analysis 的 "CED granularity" 段提到 sentence-level CED filtering 失败（Evi-F1 下降 7.7pp），这虽然是有趣的负面发现，但并不证明 CED 优于 flat-NLI，只说明 evidence 质量是 response-level 属性。这个发现对 CED 和 flat-NLI 同样适用。

**[AGREE] R2-N3: RSFT 训练数据量数值矛盾**

同意。我在小问题中也标记了这个不一致。详细分析矛盾：

- §3.3 RSFT 段（method.tex 第 30 行）：N=8 candidates per document, top-k=1, "From 24,216 candidate outputs, this selection yields 9,042 training examples (37.3% acceptance rate)"
- Appendix Table 5（appendix.tex 第 30 行）：Training samples = 2,718
- DocRED 有 3,053 training documents（§4.1）

数学核实：
- 24,216 / 8 = 3,027 documents（与 3,053 接近，可能有些文档生成失败）
- k=1 selection：应产生 ≤3,027 examples（每文档最多 1 个）
- 9,042 / 3,027 ≈ 3.0，暗示实际使用了 k=3 而非 k=1
- 2,718 < 3,027，可能是加了额外的 quality threshold 过滤

这三个数字（9,042 / 2,718 / k=1 from 3,053 docs）互相矛盾，且无法通过合理解释调和。至少存在一处错误。这不仅是格式问题，它影响可复现性：研究者无法确定 RSFT 的实际训练数据规模。

**[AGREE] R2-N4: 仅 Dev Set 结果**

完全同意，与我的 R1-N2 一致。不再赘述。

---

### Should-Fix 问题

**[AGREE] R2-W1: 指标格式不一致**

同意。我在小问题中也指出了这一点。Table 1 中 Ign-F1 = 39.74（百分比）、Rel-F1 = 0.4049（小数）、Evi-F1 = 79.86（百分比）混用确实造成阅读困难。补充一点：这种不一致贯穿全文，不仅限于 Table 1——Table 2、Table 3、Appendix Tables 均存在同样问题。

**[AGREE] R2-W2: 引用数量偏低且 bib 条目不完整**

部分同意。引用验证结果显示：33 unique cited keys，其中 7 条 orphan entries（ACL 模板遗留），5 条作者信息与 OpenAlex 不匹配（autore2024 标注 Anonymous 但实际第一作者为 Xue；wang2025relprior 第一作者应为 Pi 而非 Wang；zhang2025glidre 第一作者应为 Armingaud 而非 Zhang；hu2025reinforcepp 第一作者应为 Jian 而非 Hu；wang2025rear 第一作者应为 Luo 而非 Wang）。这些作者错误是实质性问题，需要修正。

关于引用数量，33 篇确实偏低但不算致命——关键在于覆盖度而非数量。我在 R1 审稿中也指出了缺失的相关方向（multi-task learning、CoT faithful reasoning），R2 的缺失引用建议（Standley et al. 2020, Yu et al. 2020, Wang et al. 2023）合理。

**[AGREE] R2-W3: 1.7B Evidence Benefit 解释缺乏支撑**

强烈同意。这与我的 R1-N4 核心观点一致。"Implicit regularization" 是一个未经检验的假说（§4.4 第 93 行："We hypothesize that..."），论文没有提供任何实验来区分 regularization 效应和 repetition-reduction 效应。Limitations 承认 1.7B 有 44.4% repetitive outputs（§7），这是一个已知的严重干扰因素。"Fair evaluation subset" 在 §4.4 中仅一句提及（"On a fair evaluation subset that controls for output format effects, this benefit is +6.2 points"），无任何细节。

**[AGREE] R2-W4: Multi-seed 覆盖不均匀**

同意。Appendix Table 8 caption 明确说"single seed for other scales"。4B 有 4 seeds，但 1.7B、8B、LLaMA-8B 均为单 seed。这意味着 Table 3 的 scaling analysis（论文 Contribution 3）中，4 行数据有 3 行基于单次实验。特别是 1.7B RSFT (50.50) 和 8B SFT (50.51) 的"matches"claim（我在 R1-W2 中详细分析）完全无统计意义。

**[AGREE] R2-W5: Related Work 缺少重要相关方向**

同意。论文的核心发现（evidence 和 extraction 在 gradient-based optimization 下竞争 capacity）本质上是一个 multi-task learning / task interference 问题，但 Related Work 没有引用 MTL 文献。这是一个显著遗漏，因为 MTL 文献中关于 task gradient conflict 的分析（如 R2 推荐的 Yu et al. 2020 "Gradient Surgery"）直接解释了为什么 GRPO/DPO 出现 decoupling 而 RSFT 不会。

我在 R1 缺失引用中也指出了类似问题，补充推荐了 Ruder (2017) 和 Fifty et al. (2021) 作为 MTL 基础文献，以及 Lanham et al. (2023) 作为 faithful reasoning 文献。

**[AGREE] R2-W6: "pre-D076 evaluation protocol" 未解释**

同意，与我的小问题一致。Table 2 脚注中的 "D076" 是内部实验编号，在投稿论文中不应出现。更重要的是，DPO 3-epoch 使用了不同的 evaluation protocol 但被纳入了 decoupling spectrum 的相关性分析（Table 2），这污染了 ρ=-0.965 的计算。如果该数据点不可比，应从 spectrum 分析中移除或单独标注。

---

### 关于 R2 缺失引用的补充

R2 推荐的三篇引用均合理：
1. Standley et al. (2020) "Which Tasks Should Be Learned Together" — 直接相关于 evidence 和 extraction 作为两个 task 的 grouping/interference 分析
2. Yu et al. (2020) "Gradient Surgery" — 解释了为什么 gradient-based methods (GRPO/DPO) 在多目标下失败而 selection-based methods (RSFT) 不会
3. Wang et al. (2023) "Self-Consistency" — RSFT 的 sample-and-select 策略与 self-consistency 的 sample-and-vote 在概念上相近

---

### R1 与 R2 评分对比

| 维度 | R1 | R2 | 差异说明 |
|------|----|----|----------|
| Soundness | 2.5 | 2.5 | 一致 |
| Excitement | 3.5 | 3.0 | R1 认为问题定位稍好，但差异不大 |
| Overall | 3.0 | 3.0 | 一致：Findings |
| Reproducibility | 3 | 2.5 | R2 因数据不一致 (N3) 打分更低，合理 |

**总体判断**：R2 的审稿与 R1 在核心问题上高度一致（dev-set-only、统计不足、CED 贡献存疑）。R2 在 EDCR 定义循环性（N1）和数据不一致（N3）上的分析比 R1 更尖锐。两份审稿共同指向同一个结论：论文 claim 强度系统性超过证据支撑力度，当前状态适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-18T06:56:56.185450+00:00_

Reviewer 1 的交叉回应已收到，全部 [AGREE]，与 Reviewer 2 高度共识。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 95 · 2026-05-18T06:56:58.833410+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。R2 的 4 个 Must-Fix 和 6 个 Should-Fix 全部标记为 [AGREE]，主要原因：

- **N1 (EDCR 循环性)**：R2 比我更精准地指出了 Rel-Recall 同时出现在 EDCR 分母和 Rel-F1 中的 tautological 问题
- **N2 (CED≈flat-NLI)**：与我的 R1-W3 一致，0.02pp 差异无统计意义
- **N3 (9,042 vs 2,718)**：数学上不可调和的矛盾，影响可复现性
- **N4 (dev-set-only)**：与我的 R1-N2 一致

两份审稿在 Overall 3.0 (Findings) 上完全一致，核心问题高度重叠：claim 强度超过证据支撑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 96 · 2026-05-18T06:57:08.649708+00:00_

Reviewer 1 的交叉回应已收到（全部 [AGREE]）。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 8

## Round 8

6 recorded events


### User

_source line 97 · 2026-05-18T06:57:20.163997+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见

---

## Must-Fix 问题

**[AGREE] R1-N1: GRPO 实验混淆变量**

同意这是本文最严重的实验设计缺陷之一。GRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了量化精度和 group size 两个变量。Section 4.3 第 1 段将 catastrophic collapse 归因于 "4-bit quantization constrains the effective parameter space, forcing the reward signal to optimize whichever sub-task yields easier gradient progress"，但无法排除 G=4 vs G=8 的影响。Introduction 第 30 行 "QLoRA acts as a catastrophic amplifier of the underlying optimization conflict rather than its root cause" 是一个未经控制实验验证的因果性声明。

补充：这一混淆变量问题进一步削弱了 "decoupling spectrum" 叙事的说服力。如果 GRPO 的 catastrophic collapse 实际上由 G=4（样本数不足以估计可靠 advantage）导致而非量化精度，那么 spectrum 的排序逻辑（"RL optimization pressure correlates with decoupling severity"）就需要重新审视。GRPO bf16 G=8 的 EDCR (0.6318) 实际上比 SFT baseline (0.6982) 更低（Table 2），这意味着去除 QLoRA 的极端案例后，GRPO 并未展现明显 decoupling，反而可能是三种方法中耦合最好的。这与论文的核心叙事 "GRPO > DPO > RSFT in decoupling severity" 矛盾。

**[AGREE] R1-N2: 全部结果仅在 dev set 上报告**

完全同意。我在自己的 N4 中也将此列为 critical 问题。DocRED test set 通过 CodaLab 提交是社区标准做法。对于一篇声称 "85+ configurations" 系统性实证研究的 EMNLP long paper，完全缺少 test set 结果是不可接受的。

**[AGREE] R1-N3: SFT baseline 缺少多 seed 方差**

同意，这是我遗漏的一个重要问题。+4.92pp 是论文最核心的效果数字（出现在 Abstract、Introduction Contribution 4、Table 1、Conclusion），但 SFT baseline 39.74 仅单 seed。如果 SFT 本身有 ±1pp 的方差（在 LLM fine-tuning 中完全正常），实际改进可能在 +2.9pp 到 +6.9pp 之间，这对论文价值的判断有本质差别。

补充：Table 5 (Appendix) 显示 RSFT CED k=1 的 4 个 seed 范围为 44.16-45.12（range=0.96pp），说明该任务的 seed 方差并非可忽略。SFT 作为 RSFT 的 base model，其方差应至少与 RSFT 在同一量级。不报告 SFT 方差使得所有基于 "SFT vs RSFT" 差值的结论（包括 evidence tax、RSFT gain）都缺乏统计基础。

**[AGREE] R1-N4: "Non-monotonic" scaling pattern 基于 3 个数据点**

同意核心批评——3 个规模点不足以建立 "non-monotonic pattern" 这样强的 claim。我在自己的 W3 中从 1.7B 解释角度质疑了这一发现，但 R1 的表述更精准：即使 3 个点的值完全准确，3 点也无法区分 non-monotonic pattern 与两段独立趋势。

补充两点：
1. R1 指出 Abstract "+8pp" 与正文 "fair subset +6.2pp" 的不一致。这不仅是数字问题——如果 fair evaluation 后效果缩水 22%（8.04 → 6.2），说明 raw number 受评估方式影响很大，论文应在 Abstract 中使用更保守的数字。
2. Table 3 中 Qwen3-1.7B SFT w/ evi 为 47.86 而 No-evi 为 39.82。但同一 table 中 Qwen3-4B 的关系是 SFT w/ evi 39.74 < No-evi 47.21。1.7B with evidence (47.86) 竟然高于 4B with evidence (39.74)，这一反直觉结果暗示 1.7B 和 4B 的训练可能在某些方面不等价（例如训练 convergence 不同、hyperparameter 对不同 scale 的适配度不同），而非单纯的 scale effect。论文未对此做任何讨论。

---

## Should-Fix 问题

**[AGREE] R1-W1: EDCR 方法级相关性 ρ=-0.965 仅基于 n=6**

完全同意，且这一问题与我的 N1（EDCR 定义循环性）相互加强。n=6 时 Spearman 相关的 critical value 很高（α=0.05 时需 |ρ|>0.886），即使 ρ=-0.965 在统计上接近显著，去掉 GRPO QLoRA 这个极端 outlier 后（n=5），相关性几乎肯定不再显著。再加上 DPO 3ep 使用了不同评估 protocol（Table 2 脚注），实际可比的数据点仅 4 个。在 4 个数据点上报告 ρ=-0.965 并将其作为 EDCR 有效性的核心证据（Section 6 第 1 段）是明显的 over-claim。

**[AGREE] R1-W2: "1.7B RSFT matches 8B SFT" 基于单 seed**

完全同意。50.50 vs 50.51 的 0.01pp 差异远小于合理方差。这一 claim 出现在 Abstract 第 14 行、Introduction Contribution 4、Section 4.4 末段、Conclusion。将其写为 "matches" 而非 "approaches" 是 over-claim。我补充一个角度：即使多 seed 后均值确实接近，这一比较跨越了不同 model size 和不同 base model capability——1.7B with evidence (47.86) 的 SFT 起点远高于 4B with evidence (39.74)，说明 Qwen3-1.7B 可能在 DocRE 任务上有异常优势（或 4B 有异常劣势），"1.7B matches 8B" 可能反映的是 Qwen3 系列特定 scale 的特性而非 RSFT 的通用能力。

**[AGREE] R1-W3: CED vs flat-NLI 差异仅 0.02pp**

完全同意。我在自己的 N2 中将此列为 critical 问题。R1 补充了 flat-NLI 仅 2 seeds 的问题，进一步削弱了比较的可靠性。论文应诚实报告 contrastive 组件在 RSFT selection 中可能不必要。

**[AGREE] R1-W4: Baseline 对比不完整**

同意。我在 W5 中从 Related Work 角度提出了类似问题。缺少与 SAIS/DREEAM/EIDER 的直接表格化对比是一个明显的疏漏。虽然 encoder-based 和 LLM-based 方法不完全 comparable（不同 backbone），但至少应在一个表格中并列呈现 evidence quality（Evi-F1）和 extraction quality（Rel-F1/Ign-F1），让读者自行判断 LLM-based evidence-grounded extraction 相对于 encoder-based 方法的整体位置。Section 4.6 末段的文字提及 "our best joint Evi-F1 (0.36) falls below supervised DREEAM (54.01%)"，但这一关键比较被埋在文字中，不在任何表格中。

**[REBUT] R1-W5: RSFT ablation 缺少 random selection baseline**

部分不同意。R1 认为缺少 random-k=1 baseline 使得 "无法确定改进来自 quality-based selection 还是 sampling diversity"。但论文在 Table 5 中报告了 RSFT CED k=3 (Ign-F1 43.64) vs k=1 (44.66)。k=3 使用了 3 倍数据量但效果更差，这已经间接回答了 "更多 diversity 不等于更好"。同时，RSFT 的训练数据来自 SFT 模型的采样输出，k=1 选最好的和 random k=1 选随机的之间的差异就是 data quality 的差异——如果 random k=1 与原始 SFT 训练数据等价（均为无 selection 的监督学习），那 SFT baseline 本身就是近似的 "no quality selection" baseline。

不过，R1 的建议仍有价值：一个 explicit random-k=1 baseline（从 8 个候选中随机选 1 个）可以更干净地控制 "training on self-generated data" 这一因素，因为 SFT baseline 训练在 gold data 上而 RSFT 训练在 model-generated data 上，data source 不同。建议作者补充。

**[AGREE] R1-W6: GRPO/DPO 超参数探索不足**

同意，但认为严重程度可降一级。论文的核心论点是不同优化范式之间的结构性差异（gradient-based vs selection-based），而非任一方法的最优配置。如果 GRPO 在 KL=0.001 下不出现 collapse，或 DPO 在 β=0.5 下不出现 gradual decay，那 "decoupling spectrum" 叙事就会被根本否定。因此 R1 的建议虽然工作量大，但确实是验证核心 claim 所必需的。至少应测试 1-2 个替代超参数配置。

---

## 缺失引用

**[AGREE]** R1 建议的 multi-task learning 文献（Ruder 2017, Fifty et al. 2021）与我建议的（Standley et al. 2020, Yu et al. 2020）覆盖同一缺口。论文的核心发现——extraction 和 evidence 在梯度优化中竞争——本质上是 multi-task learning 中 negative transfer 的一个实例，不引用这一成熟文献是明显疏漏。

**[AGREE]** Chain-of-thought faithfulness 文献（Lanham et al. 2023）也是相关缺失——evidence generation 可以被视为一种 task-specific rationale generation，其忠实性问题与 CoT faithfulness 直接相关。

---

## 总结

R1 的 4 个 Must-Fix 中我全部同意，其中 N1（混淆变量）和 N3（SFT 缺 multi-seed）是我自己审稿中未充分强调的问题。R1-N1 对 decoupling spectrum 的质疑比我的 N1（EDCR 循环性）更具打击力：如果 GRPO bf16 G=8 的 EDCR (0.6318) 比 SFT (0.6982) 还低，那去除 QLoRA 极端案例后，spectrum 的核心叙事就站不住了。

综合两位 reviewer 的意见，论文的核心问题集中在：
1. **统计严谨性不足**：SFT 单 seed、n=6 相关性、3 点 non-monotonic claim、单 seed cross-scale 比较
2. **混淆变量**：GRPO 的 quantization vs group size、1.7B 的 repetition vs evidence benefit
3. **贡献声明过度**：CED ≈ flat-NLI、EDCR 循环性、"matches" vs "approaches"
4. **Dev-only 结果**

维持我的 Overall 3.0 (Findings) 评分。如果 N1-N4 + R1-N1/N3 得到充分解决，有潜力升至 3.5。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-18T06:58:57.999582+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "faith-evidence-ie",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"GRPO实验同时改变量化精度和group size，无法支撑decoupling spectrum的因果归因\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：去除QLoRA极端案例后GRPO bf16 EDCR(0.6318)比SFT(0.6982)更低，spectrum叙事站不住\"\n    action_items:\n      - round: 1\n        action: \"补充GRPO bf16 G=4和GRPO QLoRA G=8实验解耦两个变量；或将因果性表述降级为观察性表述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"全部结果仅在dev set上报告，缺少test set提交\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位Reviewer独立提出（R1-N2, R2-N4），一致认为对EMNLP long paper不可接受\"\n    action_items:\n      - round: 1\n        action: \"至少对SFT baseline和RSFT CED提交DocRED test set评估\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"SFT baseline缺少多seed方差，+4.92pp改进无统计显著性检验\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充RSFT seed range=0.96pp说明方差不可忽略\"\n    action_items:\n      - round: 1\n        action: \"SFT补充3+seeds；对所有主要对比进行paired bootstrap或t-test；报告p-value和CI\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"Non-monotonic scaling pattern仅基于3个数据点，1.7B benefit有repetition artifact替代解释\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：1.7B w/evi(47.86)高于4B w/evi(39.74)是反直觉结果，暗示scale间训练不等价\"\n    action_items:\n      - round: 1\n        action: \"增加中间规模点；详细报告fair evaluation subset；对1.7B repetition做controlled analysis；或将claim降级\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"EDCR与Rel-F1的相关性存在定义循环——分母Rel-Recall是Rel-F1的组成部分\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并补充：per-relation EDCR与Evi-F1不显著相关不等于fully decoupled（absence of evidence != evidence of absence）\"\n    action_items:\n      - round: 1\n        action: \"报告p值；提供EDCR相对于简单替代指标的增量诊断价值；对分母效应做敏感性分析；去除GRPO QLoRA outlier后重新计算\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"CED与flat-NLI差距仅0.02pp，contrastive component贡献未被证明，但CED被列为核心贡献\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出（N2），R1在W3也独立提出。两位一致认为论文消融自己否定了CED的量化优势\"\n    action_items:\n      - round: 1\n        action: \"将CED降级为可选评分函数，贡献定位为NLI-based quality filtering for RSFT；或提供CED在特定场景下优于flat-NLI的证据\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"RSFT训练数据量在方法部分(9,042)和附录超参表(2,718)存在3.3倍不可调和矛盾\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并做数学核实：k=1 from 3053 docs最多产生~3027 samples，9042与k=1矛盾\"\n    action_items:\n      - round: 1\n        action: \"检查并统一两个数字，解释差异来源；如存在额外过滤步骤需在方法部分明确描述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"EDCR方法级相关性ρ=-0.965仅基于n=6数据点，去除outlier后可能不显著\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：DPO 3ep不同protocol使可比数据点仅4个\"\n    action_items:\n      - round: 1\n        action: \"去除GRPO QLoRA outlier后报告相关性；统一评估protocol或将DPO 3ep从分析中移除\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"1.7B RSFT matches 8B SFT claim基于单seed，0.01pp差异无统计意义\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：1.7B w/evi起点(47.86)高于4B(39.74)可能反映Qwen3特定scale特性而非RSFT通用能力\"\n    action_items:\n      - round: 1\n        action: \"补充多seed结果或将matches改为approaches\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Baseline对比不完整：缺少与SAIS/DREEAM/EIDER的直接表格化对比和LLM-based DocRE baseline\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：DREEAM 54.01%比较被埋在文字中不在表格中\"\n    action_items:\n      - round: 1\n        action: \"在main results或generalization中增加与encoder-based方法的head-to-head表格对比\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"RSFT ablation缺少random selection baseline\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1提出，R2部分REBUT（k=3 vs k=1已间接回答更多diversity不等于更好；SFT近似no-selection baseline），但仍建议补充explicit random-k=1\"\n    action_items:\n      - round: 1\n        action: \"补充random-k=1 baseline以控制training on self-generated data因素\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"GRPO/DPO超参数探索不足：GRPO仅KL=0.01，DPO仅β=0.1\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1提出，R2交叉回应AGREE但认为严重程度可降一级——核心论点是结构性差异而非最优配置\"\n    action_items:\n      - round: 1\n        action: \"至少测试1-2个替代超参数配置验证结论稳健性\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"指标格式严重不一致：Ign-F1百分比、Rel-F1小数、Evi-F1百分比混用\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE。贯穿全文所有表格\"\n    action_items:\n      - round: 1\n        action: \"全表统一为百分比或小数格式\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"引用数量偏低(32篇)且15/32条bib使用and others、2条Anonymous，多条作者信息错误\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并补充5条作者与OpenAlex不匹配的具体条目\"\n    action_items:\n      - round: 1\n        action: \"补全所有作者列表；将Anonymous替换为真实作者；核实并修正作者信息；补充相关方向引用\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"1.7B evidence benefit的implicit regularization解释是推测性的，fair evaluation subset未详细定义\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出（W3），与R1-N4关于repetition artifact的分析相互加强\"\n    action_items:\n      - round: 1\n        action: \"详细定义fair evaluation subset并报告完整结果；分析1.7B repetition rate对Ign-F1差异的贡献；提供至少一个定量证据支撑regularization假说\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"Multi-seed覆盖不均匀：4B有4-seed，1.7B/8B/LLaMA为单seed\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE\"\n    action_items:\n      - round: 1\n        action: \"至少在1.7B和8B上报告2-seed结果；或明确标注单seed并讨论variance风险\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"Related Work缺少multi-task learning/task interference、self-consistency、encoder-based直接数值比较\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并补充推荐Ruder 2017, Fifty et al. 2021\"\n    action_items:\n      - round: 1\n        action: \"补充MTL task interference文献、self-consistency引用、与encoder-based方法的表格化对比\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W6\"\n    summary: \"pre-D076 evaluation protocol未解释，内部编号不应出现在投稿论文中\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并补充：DPO 3ep不同protocol污染了ρ=-0.965的计算\"\n    action_items:\n      - round: 1\n        action: \"解释protocol差异并量化影响；或将DPO 3ep移至附录并从spectrum分析中移除\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-misc1\"\n    summary: \"Appendix Figure caption说93 relation types，正文说76，DocRED有96——三个数字互相矛盾\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位Reviewer均注意到\"\n    action_items:\n      - round: 1\n        action: \"统一relation type数字并解释筛选标准\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-misc2\"\n    summary: \"RSFT训练样本9,042 vs Table 5报告2,718——与R2-N3相同问题\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"与R2-N3重复，详见R2-N3\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-misc1\"\n    summary: \"Inference-time CED reranking在Method部分无描述，突然出现在Section 4.5\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2在小问题中提出\"\n    action_items:\n      - round: 1\n        action: \"在Method中增加inference-time reranking的描述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-misc2\"\n    summary: \"85+ experiments计算方式未交代\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2在小问题中提出\"\n    action_items:\n      - round: 1\n        action: \"解释85+的计算方式\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "faith-evidence-ie",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"GRPO实验同时改变量化精度和group size，无法支撑decoupling spectrum的因果归因\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：去除QLoRA极端案例后GRPO bf16 EDCR(0.6318)比SFT(0.6982)更低，spectrum叙事站不住\"\n    action_items:\n      - round: 1\n        action: \"补充GRPO bf16 G=4和GRPO QLoRA G=8实验解耦两个变量；或将因果性表述降级为观察性表述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"全部结果仅在dev set上报告，缺少test set提交\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位Reviewer独立提出（R1-N2, R2-N4），一致认为对EMNLP long paper不可接受\"\n    action_items:\n      - round: 1\n        action: \"至少对SFT baseline和RSFT CED提交DocRED test set评估\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"SFT baseline缺少多seed方差，+4.92pp改进无统计显著性检验\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充RSFT seed range=0.96pp说明方差不可忽略\"\n    action_items:\n      - round: 1\n        action: \"SFT补充3+seeds；对所有主要对比进行paired bootstrap或t-test；报告p-value和CI\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N4\"\n    summary: \"Non-monotonic scaling pattern仅基于3个数据点，1.7B benefit有repetition artifact替代解释\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：1.7B w/evi(47.86)高于4B w/evi(39.74)是反直觉结果，暗示scale间训练不等价\"\n    action_items:\n      - round: 1\n        action: \"增加中间规模点；详细报告fair evaluation subset；对1.7B repetition做controlled analysis；或将claim降级\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"EDCR与Rel-F1的相关性存在定义循环——分母Rel-Recall是Rel-F1的组成部分\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并补充：per-relation EDCR与Evi-F1不显著相关不等于fully decoupled（absence of evidence != evidence of absence）\"\n    action_items:\n      - round: 1\n        action: \"报告p值；提供EDCR相对于简单替代指标的增量诊断价值；对分母效应做敏感性分析；去除GRPO QLoRA outlier后重新计算\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"CED与flat-NLI差距仅0.02pp，contrastive component贡献未被证明，但CED被列为核心贡献\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出（N2），R1在W3也独立提出。两位一致认为论文消融自己否定了CED的量化优势\"\n    action_items:\n      - round: 1\n        action: \"将CED降级为可选评分函数，贡献定位为NLI-based quality filtering for RSFT；或提供CED在特定场景下优于flat-NLI的证据\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"RSFT训练数据量在方法部分(9,042)和附录超参表(2,718)存在3.3倍不可调和矛盾\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并做数学核实：k=1 from 3053 docs最多产生~3027 samples，9042与k=1矛盾\"\n    action_items:\n      - round: 1\n        action: \"检查并统一两个数字，解释差异来源；如存在额外过滤步骤需在方法部分明确描述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"EDCR方法级相关性ρ=-0.965仅基于n=6数据点，去除outlier后可能不显著\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：DPO 3ep不同protocol使可比数据点仅4个\"\n    action_items:\n      - round: 1\n        action: \"去除GRPO QLoRA outlier后报告相关性；统一评估protocol或将DPO 3ep从分析中移除\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"1.7B RSFT matches 8B SFT claim基于单seed，0.01pp差异无统计意义\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：1.7B w/evi起点(47.86)高于4B(39.74)可能反映Qwen3特定scale特性而非RSFT通用能力\"\n    action_items:\n      - round: 1\n        action: \"补充多seed结果或将matches改为approaches\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Baseline对比不完整：缺少与SAIS/DREEAM/EIDER的直接表格化对比和LLM-based DocRE baseline\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1首次提出，R2交叉回应AGREE并补充：DREEAM 54.01%比较被埋在文字中不在表格中\"\n    action_items:\n      - round: 1\n        action: \"在main results或generalization中增加与encoder-based方法的head-to-head表格对比\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"RSFT ablation缺少random selection baseline\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1提出，R2部分REBUT（k=3 vs k=1已间接回答更多diversity不等于更好；SFT近似no-selection baseline），但仍建议补充explicit random-k=1\"\n    action_items:\n      - round: 1\n        action: \"补充random-k=1 baseline以控制training on self-generated data因素\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"GRPO/DPO超参数探索不足：GRPO仅KL=0.01，DPO仅β=0.1\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1提出，R2交叉回应AGREE但认为严重程度可降一级——核心论点是结构性差异而非最优配置\"\n    action_items:\n      - round: 1\n        action: \"至少测试1-2个替代超参数配置验证结论稳健性\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"指标格式严重不一致：Ign-F1百分比、Rel-F1小数、Evi-F1百分比混用\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE。贯穿全文所有表格\"\n    action_items:\n      - round: 1\n        action: \"全表统一为百分比或小数格式\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"引用数量偏低(32篇)且15/32条bib使用and others、2条Anonymous，多条作者信息错误\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并补充5条作者与OpenAlex不匹配的具体条目\"\n    action_items:\n      - round: 1\n        action: \"补全所有作者列表；将Anonymous替换为真实作者；核实并修正作者信息；补充相关方向引用\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"1.7B evidence benefit的implicit regularization解释是推测性的，fair evaluation subset未详细定义\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出（W3），与R1-N4关于repetition artifact的分析相互加强\"\n    action_items:\n      - round: 1\n        action: \"详细定义fair evaluation subset并报告完整结果；分析1.7B repetition rate对Ign-F1差异的贡献；提供至少一个定量证据支撑regularization假说\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4\"\n    summary: \"Multi-seed覆盖不均匀：4B有4-seed，1.7B/8B/LLaMA为单seed\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE\"\n    action_items:\n      - round: 1\n        action: \"至少在1.7B和8B上报告2-seed结果；或明确标注单seed并讨论variance风险\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"Related Work缺少multi-task learning/task interference、self-consistency、encoder-based直接数值比较\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并补充推荐Ruder 2017, Fifty et al. 2021\"\n    action_items:\n      - round: 1\n        action: \"补充MTL task interference文献、self-consistency引用、与encoder-based方法的表格化对比\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W6\"\n    summary: \"pre-D076 evaluation protocol未解释，内部编号不应出现在投稿论文中\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 1]\n        note: \"R2首次提出，R1交叉回应AGREE并补充：DPO 3ep不同protocol污染了ρ=-0.965的计算\"\n    action_items:\n      - round: 1\n        action: \"解释protocol差异并量化影响；或将DPO 3ep移至附录并从spectrum分析中移除\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-misc1\"\n    summary: \"Appendix Figure caption说93 relation types，正文说76，DocRED有96——三个数字互相矛盾\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位Reviewer均注意到\"\n    action_items:\n      - round: 1\n        action: \"统一relation type数字并解释筛选标准\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-misc2\"\n    summary: \"RSFT训练样本9,042 vs Table 5报告2,718——与R2-N3相同问题\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"与R2-N3重复，详见R2-N3\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-misc1\"\n    summary: \"Inference-time CED reranking在Method部分无描述，突然出现在Section 4.5\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2在小问题中提出\"\n    action_items:\n      - round: 1\n        action: \"在Method中增加inference-time reranking的描述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-misc2\"\n    summary: \"85+ experiments计算方式未交代\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"R2在小问题中提出\"\n    action_items:\n      - round: 1\n        action: \"解释85+的计算方式\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-18T06:58:58.100864+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml\", \"bytes\": 11261}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-18T07:01:12.361711+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "faith-evidence-ie",
  "report": "# 审稿报告 — Round 1\n\n**论文**: \"Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\"\n**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May 2026 cycle)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法与实验严谨性；R2: 新颖性、完整性与呈现质量）\n**审稿模式**: 独立初审 → 交叉分享逐条回应 → 收敛汇总（1 轮收敛）\n\n---\n\n## Summary\n\n论文将 evidence-grounded document-level relation extraction 形式化为 LLM 的结构化生成任务，系统比较了 GRPO、DPO、RSFT 三种 post-training 优化范式在联合生成关系三元组和证据句子时的行为。实验跨越 4 个模型规模（1.7B-8B）、2 个模型家族、2 个数据集。论文提出三个核心发现：(1) RL 优化压力与 evidence-extraction decoupling 严重程度相关（decoupling spectrum）；(2) evidence 生成代价随模型规模非单调变化（scale-dependent evidence tax）；(3) RSFT+CED 是唯一有效路线（+4.92pp Ign-F1 over SFT）。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且定位精准。** LLM-based DocRE 方法产出裸三元组而无证据支撑是真实的实用性瓶颈。论文清晰识别了 encoder-based evidence methods（SAIS/DREEAM）与 LLM extraction accuracy 之间的 gap，问题动机有说服力。[R1, R2 共识]\n\n**S2. 实验覆盖面在 DocRE 领域罕见。** 跨 4 个模型规模、2 个模型家族、2 个数据集、3 种优化范式的系统性比较，横向覆盖面本身有参考价值。[R1, R2 共识]\n\n**S3. Scale-dependent evidence tax 是有价值的经验发现。** 1.7B 受益、4B 受损、8B 中性的模式打破了 \"evidence 一定损害 extraction\" 的简单假设，对后续研究有指导意义。[R2 提出, R1 同意]\n\n**S4. RSFT \"discrete selection avoids gradient-based trade-off\" 洞察有一般性意义。** 这一观察超越 DocRE 任务本身，对所有多目标 LLM post-training 场景有参考价值。[R2 提出, R1 同意]\n\n**S5. RSFT 效果稳定。** 4-seed 方差低（±0.49），跨数据集（DocRED +4.92pp, Re-DocRED +4.86pp）和跨模型家族（LLaMA +1.74pp）改进模式一致。[R1 提出, R2 同意]\n\n**S6. 写作质量整体良好。** 无 em-dash，无明显 AI 写作标志词，段落过渡自然，叙事主线从 Abstract 到 Conclusion 基本统一。[R1, R2 共识]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**W1. [Critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果归因。**\nGRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了量化精度和 group size。论文将 catastrophic collapse 归因于量化（§4.3），Introduction 明确声称 \"QLoRA acts as a catastrophic amplifier\"（因果性 claim），但实验设计无法排除 G=4 vs G=8 的影响。更严重的是：GRPO bf16 G=8 的 EDCR (0.6318) 比 SFT baseline (0.6982) 更低（Table 2），去除 QLoRA 极端案例后 GRPO 并未展现明显 decoupling，spectrum 的核心叙事 \"GRPO > DPO > RSFT in decoupling severity\" 站不住。[R1 提出, R2 强烈同意]\n\n**W2. [Critical] 全部结果仅在 dev set 上报告，test set 缺失。**\n对于声称 \"85+ configurations\" 的系统性实证研究，没有任何 DocRED test set 结果（有公开 CodaLab leaderboard）。论文核心数字（+4.92pp, 50.50 vs 50.51）均基于 dev set，不能视为最终性能指标。[R1, R2 独立提出，共识]\n\n**W3. [Critical] SFT baseline 缺少多 seed 方差，核心改进数字（+4.92pp）缺乏统计显著性检验。**\nRSFT CED 有 4-seed 均值 44.66±0.49，但 SFT baseline 39.74 仅单 seed。全文无统计显著性检验（t-test/bootstrap/permutation test）。考虑 RSFT 自身 seed range = 0.96pp，SFT 方差不可忽略。+4.92pp 出现在 Abstract、Introduction、Conclusion，是论文最核心的效果数字。[R1 提出, R2 强烈同意]\n\n**W4. [Critical] \"Non-monotonic\" scaling pattern 仅基于 3 个数据点，over-interpreted。**\nScale-dependent evidence tax 基于 Qwen3 的 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28），无法区分 non-monotonic pattern 与噪声。1.7B 的 +8.04 有替代解释：44.4% repetitive outputs（Limitations 承认）可能人为压低 no-evidence baseline。Abstract \"+8pp\" 在正文被修正为 fair subset \"+6.2pp\"（缩水 22%），fair subset 细节缺失。1.7B w/evi (47.86) 高于 4B w/evi (39.74) 这一反直觉结果未被讨论。[R1 提出, R2 强烈同意]\n\n**W5. [Critical] EDCR 与 Rel-F1 的相关性存在定义循环。**\nEDCR = Evi-Recall_TP / Rel-Recall，而 Rel-F1 是 Rel-Recall 和 Rel-Precision 的调和平均。ρ=-0.965 部分由定义关系预设，非完全经验发现。当 Rel-Recall 极低时（GRPO QLoRA = 0.0138），EDCR 机械性趋近 1.0。论文将 EDCR 列为四项贡献之一（Contribution 2），但未展示 EDCR 相对于简单替代指标（如 Evi-F1 - Rel-F1 差值）的增量诊断价值。此外，per-relation EDCR 与 Evi-F1 \"不显著相关\" 被解释为 \"fully decoupled\"，存在 absence of evidence ≠ evidence of absence 的逻辑错误。[R2 提出, R1 强烈同意]\n\n**W6. [Critical] CED 与 flat-NLI 几乎无差异（0.02pp），论文自身消融否定了 CED 作为独立贡献。**\nCED Rel-F1 0.4563 vs flat-NLI 0.4561，差距 0.02pp，在任何合理方差下不显著。论文承认 \"comparable outcomes\" 但仍在 Contribution 4 将 CED 作为核心贡献。Contrastive component 增加方法复杂度但无可测量改进。论文声称的 \"interpretable per-triple discrimination\" 优势未在任何实验中展示实际价值。[R2 提出, R1 强烈同意]\n\n**W7. [Critical] RSFT 训练数据量存在不可调和的数值矛盾。**\n§3.3 报告 \"9,042 training examples (37.3% acceptance rate)\"，Appendix Table 5 报告 \"Training samples: 2,718\"。数学核实：k=1 from ~3,027 docs 最多产生 ~3,027 samples（与 2,718 一致），9,042 ≈ 3,027 × 3 更像 k=3。两个数字有 3.3 倍差距，影响可复现性。[R2 提出, R1 核实数学矛盾]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W8.** EDCR ρ=-0.965 仅基于 n=6，去除 GRPO QLoRA outlier 后（n=5 甚至 n=4，考虑 DPO 3ep 不同 protocol）几乎肯定不显著。[R1 提出, R2 同意]\n\n**W9.** \"1.7B RSFT matches 8B SFT\" (50.50 vs 50.51) 基于单 seed，0.01pp 差异远小于合理方差。出现在 Abstract/Introduction/Conclusion。应改为 \"approaches\"。[R1 提出, R2 同意]\n\n**W10.** Baseline 对比不完整：缺少与 SAIS/DREEAM/EIDER 的直接表格化对比（DREEAM 54.01% vs 本文 ~36% 被埋在文字中），缺少 LLM-based DocRE baseline。[R1 提出, R2 同意]\n\n**W11.** GRPO/DPO 超参数探索不足（GRPO 仅 KL=0.01, DPO 仅 β=0.1）。如果替代超参数下不出现 decoupling，核心叙事被否定。[R1 提出, R2 同意但认为可降一级]\n\n**W12.** 指标格式严重不一致：Ign-F1 百分比(39.74)、Rel-F1 小数(0.4049)、Evi-F1 百分比(79.86) 混用，贯穿全文所有表格。[R2 提出, R1 同意]\n\n**W13.** 引用数量偏低（32 篇，EMNLP long paper 通常 40-60 篇），15/32 条 \"and others\"，2 条 Anonymous（autore2024 已发表有真实作者），5 条作者信息与 OpenAlex 不匹配。[R2 提出, R1 核实具体错误]\n\n**W14.** 1.7B evidence benefit 的 \"implicit regularization\" 解释是推测性的（§4.4 \"We hypothesize\"），无实验支撑。\"Fair evaluation subset\" 仅一句提及，无定义和完整数据。[R2 提出, R1 同意]\n\n**W15.** Multi-seed 覆盖不均匀：4B 有 4-seed，1.7B/8B/LLaMA 为单 seed。Table 3 scaling analysis 的 4 行数据有 3 行基于单次实验。[R2 提出, R1 同意]\n\n**W16.** Related Work 缺少 multi-task learning / task interference 文献（核心发现本质上是 negative transfer），缺少 self-consistency 范式引用。[R2 提出, R1 同意]\n\n**W17.** \"pre-D076 evaluation protocol\" 是内部编号，不应出现在投稿论文中。DPO 3ep 不同 protocol 却纳入 spectrum 分析，污染相关性计算。[R2 提出, R1 同意]\n\n**W18.** RSFT ablation 缺少 random selection baseline。[R1 提出, R2 部分 REBUT：k=3 vs k=1 已间接回答，SFT 近似 no-selection baseline，但仍建议补充 explicit random-k=1]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| GRPO 混淆变量 (W1) | N1 [AGREE] | 交叉 [AGREE] | 补实验或降级表述 |\n| Dev-set only (W2) | N2 [AGREE] | N4 [AGREE] | 必须提交 test set |\n| SFT 缺 multi-seed (W3) | N3 [AGREE] | 交叉 [AGREE] | 必须补 seed + 统计检验 |\n| Non-monotonic over-interpreted (W4) | N4 [AGREE] | 交叉 [AGREE] | 增加数据点或降级 claim |\n| EDCR 定义循环 (W5) | 交叉 [AGREE] | N1 [AGREE] | 提供增量诊断价值证据 |\n| CED ≈ flat-NLI (W6) | W3 [AGREE] | N2 [AGREE] | 降级 CED 贡献定位 |\n| 数据量矛盾 (W7) | 小问题 [AGREE] | N3 [AGREE] | 修正数字 |\n| Overall 评分 | 3.0 | 3.0 | **Findings** |\n\n## Reviewer Divergence\n\n仅一处轻微分歧：\n\n| 问题 | R1 | R2 | 分歧 |\n|------|----|----|------|\n| Random selection baseline (W18) | W5: 应补充 | REBUT: k=3 vs k=1 已间接回答 | R2 认为不是必需的但 \"仍建议补充\"，实质上是同意方向、分歧在严重程度 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. RSFT 训练数据量到底是 9,042 还是 2,718？差异来源是什么？\n2. \"Fair evaluation subset\"（§4.4）的构建方法、样本量和完整结果？\n3. 1.7B no-evidence 模型的 repetition rate 是多少？排除重复输出后 evidence tax 还是 +8pp 吗？\n4. GRPO bf16 G=8 的 EDCR (0.6318) 低于 SFT (0.6982)，如何解释 GRPO 在 spectrum 中被归为比 SFT 更严重的 decoupling？\n5. DPO 3-epoch 使用的 \"pre-D076 evaluation protocol\" 具体是什么？与当前 protocol 有何差异？\n6. EDCR 去除 GRPO QLoRA outlier 后的 Spearman ρ 是多少？\n7. 1.7B with evidence (47.86) 高于 4B with evidence (39.74) 的原因？是否暗示 scale 间训练配置不等价？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同建议补充以下方向的引用：\n\n**Multi-task learning / task interference**（核心发现的理论框架）：\n- Ruder (2017) \"An Overview of Multi-Task Learning in Deep Neural Networks\"\n- Standley et al. (2020) \"Which Tasks Should Be Learned Together in Multi-Task Learning?\"\n- Yu et al. (2020) \"Gradient Surgery for Multi-Task Learning\"\n- Fifty et al. (2021) \"Efficiently Identifying Task Groupings for Multi-Task Learning\"\n\n**Chain-of-thought / faithful reasoning**：\n- Wang et al. (2023) \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\"\n- Lanham et al. (2023) \"Measuring Faithfulness in Chain-of-Thought Reasoning\"\n\n**Encoder-based DocRE 数值对比**：应在表格中直接呈现 SAIS/DREEAM/EIDER 数字\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n\n**置信度：高（4/5）**\n\n两位 Reviewer 评分完全一致（3.0），交叉回应后共识进一步强化。\n\n**核心判断**：论文提出了一个有价值的研究问题（LLM-based DocRE 的 evidence 可验证性），实验覆盖面令人印象深刻，scale-dependent evidence tax 和 RSFT discrete selection 的洞察有启发性。但论文存在系统性的 **claim 强度超过证据支撑力度** 的问题：\n\n1. **统计严谨性不足**：SFT 单 seed、n=6 相关性、3 点 non-monotonic claim、单 seed cross-scale 比较、全文无显著性检验\n2. **混淆变量未解耦**：GRPO 的 quantization vs group size、1.7B 的 repetition vs evidence benefit\n3. **贡献声明过度**：CED ≈ flat-NLI（自身消融否定）、EDCR 定义循环性、\"matches\" vs \"approaches\"\n4. **可复现性障碍**：dev-set only、训练数据量矛盾（9,042 vs 2,718）、内部编号（D076）泄露\n\n**升级路径**：如果能 (1) 提交 test set 结果，(2) 补充 SFT multi-seed + 统计检验，(3) 解耦 GRPO 实验或降级因果 claim，(4) 修正数据矛盾和 CED 贡献定位，论文有潜力升至 3.5 (Borderline Conference)。当前状态适合 Findings。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 约 230 words，符合长度要求但数据密集。\"Three findings emerge\" 后连续三段各带具体数字，读起来像实验摘要而非叙事\n- \"+8pp Ign-F1 benefit at 1.7B\" 在正文 fair subset 上为 +6.2pp，Abstract 应使用更保守数字\n- \"50.50 Ign-F1 matches 8B SFT performance (50.51)\" 基于单 seed，统计上无意义\n\n### Introduction\n- 叙事结构清晰（gap → formalization → findings → contributions），无 \"AI 写作\" 痕迹\n- Contribution 2（EDCR）和 Contribution 4（CED scoring）的贡献声明强度需要与 Analysis 消融结果对齐\n- \"QLoRA acts as a catastrophic amplifier\" (L30) 是未经验证的因果 claim\n\n### Related Work\n- Positioning 有效（encoder-based evidence vs LLM generation 的结构性差异讲得清楚）\n- 缺少 multi-task learning / task interference 文献——核心发现本质上是 negative transfer\n- 引用密度偏低（32 篇），bib 条目质量有问题（15 条 \"and others\"，5 条作者错误）\n\n### Method\n- Task formulation (§3.1) 清晰合理\n- CED (§3.4) 设计合理但消融显示 contrastive component 无增量贡献\n- EDCR (§3.5) 定义有循环性问题，需增量诊断价值论证\n- RSFT (§3.3) 训练数据量 9,042 vs Appendix 2,718 矛盾\n\n### Experiments\n- Main results (Table 1)：格式不一致（百分比/小数混用）；SFT 单 seed 无方差\n- Decoupling spectrum (Table 2)：GRPO 混淆变量；DPO 3ep 不同 protocol；n=6 相关性分析 power 不足\n- Scaling (Table 3)：3 点不足以建立 non-monotonic claim；1.7B benefit 有 repetition artifact 替代解释\n- Evidence strategy (§4.5)：inference-time CED reranking 在 Method 中无描述\n- Generalization (§4.6)：DREEAM 对比被埋在文字中，不在表格\n\n### Analysis\n- EDCR diagnostic 的核心论证受定义循环性影响\n- CED granularity 负面发现（sentence-level 失败）有价值但不支撑 CED 优于 flat-NLI\n- Practical implications 段的三条建议合理但证据基础不够牢固\n\n### Formatting\n- 模板正确（ACL review mode），匿名化完成\n- Limitations section 位置正确，内容诚实\n- 缺少 Responsible NLP Checklist（ARR 硬性要求，desk reject 风险）\n- 缺少 Ethics Statement（ARR 鼓励但不强制）\n- Appendix Figure caption relation type 数字矛盾（93 vs 76 vs 96）",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "faith-evidence-ie",
    "report": "# 审稿报告 — Round 1\n\n**论文**: \"Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\"\n**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May 2026 cycle)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法与实验严谨性；R2: 新颖性、完整性与呈现质量）\n**审稿模式**: 独立初审 → 交叉分享逐条回应 → 收敛汇总（1 轮收敛）\n\n---\n\n## Summary\n\n论文将 evidence-grounded document-level relation extraction 形式化为 LLM 的结构化生成任务，系统比较了 GRPO、DPO、RSFT 三种 post-training 优化范式在联合生成关系三元组和证据句子时的行为。实验跨越 4 个模型规模（1.7B-8B）、2 个模型家族、2 个数据集。论文提出三个核心发现：(1) RL 优化压力与 evidence-extraction decoupling 严重程度相关（decoupling spectrum）；(2) evidence 生成代价随模型规模非单调变化（scale-dependent evidence tax）；(3) RSFT+CED 是唯一有效路线（+4.92pp Ign-F1 over SFT）。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且定位精准。** LLM-based DocRE 方法产出裸三元组而无证据支撑是真实的实用性瓶颈。论文清晰识别了 encoder-based evidence methods（SAIS/DREEAM）与 LLM extraction accuracy 之间的 gap，问题动机有说服力。[R1, R2 共识]\n\n**S2. 实验覆盖面在 DocRE 领域罕见。** 跨 4 个模型规模、2 个模型家族、2 个数据集、3 种优化范式的系统性比较，横向覆盖面本身有参考价值。[R1, R2 共识]\n\n**S3. Scale-dependent evidence tax 是有价值的经验发现。** 1.7B 受益、4B 受损、8B 中性的模式打破了 \"evidence 一定损害 extraction\" 的简单假设，对后续研究有指导意义。[R2 提出, R1 同意]\n\n**S4. RSFT \"discrete selection avoids gradient-based trade-off\" 洞察有一般性意义。** 这一观察超越 DocRE 任务本身，对所有多目标 LLM post-training 场景有参考价值。[R2 提出, R1 同意]\n\n**S5. RSFT 效果稳定。** 4-seed 方差低（±0.49），跨数据集（DocRED +4.92pp, Re-DocRED +4.86pp）和跨模型家族（LLaMA +1.74pp）改进模式一致。[R1 提出, R2 同意]\n\n**S6. 写作质量整体良好。** 无 em-dash，无明显 AI 写作标志词，段落过渡自然，叙事主线从 Abstract 到 Conclusion 基本统一。[R1, R2 共识]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**W1. [Critical] GRPO 实验存在严重混淆变量，无法支撑 decoupling spectrum 的因果归因。**\nGRPO QLoRA (G=4, 4-bit) 与 GRPO bf16 (G=8, full-precision) 同时改变了量化精度和 group size。论文将 catastrophic collapse 归因于量化（§4.3），Introduction 明确声称 \"QLoRA acts as a catastrophic amplifier\"（因果性 claim），但实验设计无法排除 G=4 vs G=8 的影响。更严重的是：GRPO bf16 G=8 的 EDCR (0.6318) 比 SFT baseline (0.6982) 更低（Table 2），去除 QLoRA 极端案例后 GRPO 并未展现明显 decoupling，spectrum 的核心叙事 \"GRPO > DPO > RSFT in decoupling severity\" 站不住。[R1 提出, R2 强烈同意]\n\n**W2. [Critical] 全部结果仅在 dev set 上报告，test set 缺失。**\n对于声称 \"85+ configurations\" 的系统性实证研究，没有任何 DocRED test set 结果（有公开 CodaLab leaderboard）。论文核心数字（+4.92pp, 50.50 vs 50.51）均基于 dev set，不能视为最终性能指标。[R1, R2 独立提出，共识]\n\n**W3. [Critical] SFT baseline 缺少多 seed 方差，核心改进数字（+4.92pp）缺乏统计显著性检验。**\nRSFT CED 有 4-seed 均值 44.66±0.49，但 SFT baseline 39.74 仅单 seed。全文无统计显著性检验（t-test/bootstrap/permutation test）。考虑 RSFT 自身 seed range = 0.96pp，SFT 方差不可忽略。+4.92pp 出现在 Abstract、Introduction、Conclusion，是论文最核心的效果数字。[R1 提出, R2 强烈同意]\n\n**W4. [Critical] \"Non-monotonic\" scaling pattern 仅基于 3 个数据点，over-interpreted。**\nScale-dependent evidence tax 基于 Qwen3 的 3 个规模点（1.7B: +8.04, 4B: -7.47, 8B: -0.28），无法区分 non-monotonic pattern 与噪声。1.7B 的 +8.04 有替代解释：44.4% repetitive outputs（Limitations 承认）可能人为压低 no-evidence baseline。Abstract \"+8pp\" 在正文被修正为 fair subset \"+6.2pp\"（缩水 22%），fair subset 细节缺失。1.7B w/evi (47.86) 高于 4B w/evi (39.74) 这一反直觉结果未被讨论。[R1 提出, R2 强烈同意]\n\n**W5. [Critical] EDCR 与 Rel-F1 的相关性存在定义循环。**\nEDCR = Evi-Recall_TP / Rel-Recall，而 Rel-F1 是 Rel-Recall 和 Rel-Precision 的调和平均。ρ=-0.965 部分由定义关系预设，非完全经验发现。当 Rel-Recall 极低时（GRPO QLoRA = 0.0138），EDCR 机械性趋近 1.0。论文将 EDCR 列为四项贡献之一（Contribution 2），但未展示 EDCR 相对于简单替代指标（如 Evi-F1 - Rel-F1 差值）的增量诊断价值。此外，per-relation EDCR 与 Evi-F1 \"不显著相关\" 被解释为 \"fully decoupled\"，存在 absence of evidence ≠ evidence of absence 的逻辑错误。[R2 提出, R1 强烈同意]\n\n**W6. [Critical] CED 与 flat-NLI 几乎无差异（0.02pp），论文自身消融否定了 CED 作为独立贡献。**\nCED Rel-F1 0.4563 vs flat-NLI 0.4561，差距 0.02pp，在任何合理方差下不显著。论文承认 \"comparable outcomes\" 但仍在 Contribution 4 将 CED 作为核心贡献。Contrastive component 增加方法复杂度但无可测量改进。论文声称的 \"interpretable per-triple discrimination\" 优势未在任何实验中展示实际价值。[R2 提出, R1 强烈同意]\n\n**W7. [Critical] RSFT 训练数据量存在不可调和的数值矛盾。**\n§3.3 报告 \"9,042 training examples (37.3% acceptance rate)\"，Appendix Table 5 报告 \"Training samples: 2,718\"。数学核实：k=1 from ~3,027 docs 最多产生 ~3,027 samples（与 2,718 一致），9,042 ≈ 3,027 × 3 更像 k=3。两个数字有 3.3 倍差距，影响可复现性。[R2 提出, R1 核实数学矛盾]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W8.** EDCR ρ=-0.965 仅基于 n=6，去除 GRPO QLoRA outlier 后（n=5 甚至 n=4，考虑 DPO 3ep 不同 protocol）几乎肯定不显著。[R1 提出, R2 同意]\n\n**W9.** \"1.7B RSFT matches 8B SFT\" (50.50 vs 50.51) 基于单 seed，0.01pp 差异远小于合理方差。出现在 Abstract/Introduction/Conclusion。应改为 \"approaches\"。[R1 提出, R2 同意]\n\n**W10.** Baseline 对比不完整：缺少与 SAIS/DREEAM/EIDER 的直接表格化对比（DREEAM 54.01% vs 本文 ~36% 被埋在文字中），缺少 LLM-based DocRE baseline。[R1 提出, R2 同意]\n\n**W11.** GRPO/DPO 超参数探索不足（GRPO 仅 KL=0.01, DPO 仅 β=0.1）。如果替代超参数下不出现 decoupling，核心叙事被否定。[R1 提出, R2 同意但认为可降一级]\n\n**W12.** 指标格式严重不一致：Ign-F1 百分比(39.74)、Rel-F1 小数(0.4049)、Evi-F1 百分比(79.86) 混用，贯穿全文所有表格。[R2 提出, R1 同意]\n\n**W13.** 引用数量偏低（32 篇，EMNLP long paper 通常 40-60 篇），15/32 条 \"and others\"，2 条 Anonymous（autore2024 已发表有真实作者），5 条作者信息与 OpenAlex 不匹配。[R2 提出, R1 核实具体错误]\n\n**W14.** 1.7B evidence benefit 的 \"implicit regularization\" 解释是推测性的（§4.4 \"We hypothesize\"），无实验支撑。\"Fair evaluation subset\" 仅一句提及，无定义和完整数据。[R2 提出, R1 同意]\n\n**W15.** Multi-seed 覆盖不均匀：4B 有 4-seed，1.7B/8B/LLaMA 为单 seed。Table 3 scaling analysis 的 4 行数据有 3 行基于单次实验。[R2 提出, R1 同意]\n\n**W16.** Related Work 缺少 multi-task learning / task interference 文献（核心发现本质上是 negative transfer），缺少 self-consistency 范式引用。[R2 提出, R1 同意]\n\n**W17.** \"pre-D076 evaluation protocol\" 是内部编号，不应出现在投稿论文中。DPO 3ep 不同 protocol 却纳入 spectrum 分析，污染相关性计算。[R2 提出, R1 同意]\n\n**W18.** RSFT ablation 缺少 random selection baseline。[R1 提出, R2 部分 REBUT：k=3 vs k=1 已间接回答，SFT 近似 no-selection baseline，但仍建议补充 explicit random-k=1]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| GRPO 混淆变量 (W1) | N1 [AGREE] | 交叉 [AGREE] | 补实验或降级表述 |\n| Dev-set only (W2) | N2 [AGREE] | N4 [AGREE] | 必须提交 test set |\n| SFT 缺 multi-seed (W3) | N3 [AGREE] | 交叉 [AGREE] | 必须补 seed + 统计检验 |\n| Non-monotonic over-interpreted (W4) | N4 [AGREE] | 交叉 [AGREE] | 增加数据点或降级 claim |\n| EDCR 定义循环 (W5) | 交叉 [AGREE] | N1 [AGREE] | 提供增量诊断价值证据 |\n| CED ≈ flat-NLI (W6) | W3 [AGREE] | N2 [AGREE] | 降级 CED 贡献定位 |\n| 数据量矛盾 (W7) | 小问题 [AGREE] | N3 [AGREE] | 修正数字 |\n| Overall 评分 | 3.0 | 3.0 | **Findings** |\n\n## Reviewer Divergence\n\n仅一处轻微分歧：\n\n| 问题 | R1 | R2 | 分歧 |\n|------|----|----|------|\n| Random selection baseline (W18) | W5: 应补充 | REBUT: k=3 vs k=1 已间接回答 | R2 认为不是必需的但 \"仍建议补充\"，实质上是同意方向、分歧在严重程度 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. RSFT 训练数据量到底是 9,042 还是 2,718？差异来源是什么？\n2. \"Fair evaluation subset\"（§4.4）的构建方法、样本量和完整结果？\n3. 1.7B no-evidence 模型的 repetition rate 是多少？排除重复输出后 evidence tax 还是 +8pp 吗？\n4. GRPO bf16 G=8 的 EDCR (0.6318) 低于 SFT (0.6982)，如何解释 GRPO 在 spectrum 中被归为比 SFT 更严重的 decoupling？\n5. DPO 3-epoch 使用的 \"pre-D076 evaluation protocol\" 具体是什么？与当前 protocol 有何差异？\n6. EDCR 去除 GRPO QLoRA outlier 后的 Spearman ρ 是多少？\n7. 1.7B with evidence (47.86) 高于 4B with evidence (39.74) 的原因？是否暗示 scale 间训练配置不等价？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同建议补充以下方向的引用：\n\n**Multi-task learning / task interference**（核心发现的理论框架）：\n- Ruder (2017) \"An Overview of Multi-Task Learning in Deep Neural Networks\"\n- Standley et al. (2020) \"Which Tasks Should Be Learned Together in Multi-Task Learning?\"\n- Yu et al. (2020) \"Gradient Surgery for Multi-Task Learning\"\n- Fifty et al. (2021) \"Efficiently Identifying Task Groupings for Multi-Task Learning\"\n\n**Chain-of-thought / faithful reasoning**：\n- Wang et al. (2023) \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\"\n- Lanham et al. (2023) \"Measuring Faithfulness in Chain-of-Thought Reasoning\"\n\n**Encoder-based DocRE 数值对比**：应在表格中直接呈现 SAIS/DREEAM/EIDER 数字\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n\n**置信度：高（4/5）**\n\n两位 Reviewer 评分完全一致（3.0），交叉回应后共识进一步强化。\n\n**核心判断**：论文提出了一个有价值的研究问题（LLM-based DocRE 的 evidence 可验证性），实验覆盖面令人印象深刻，scale-dependent evidence tax 和 RSFT discrete selection 的洞察有启发性。但论文存在系统性的 **claim 强度超过证据支撑力度** 的问题：\n\n1. **统计严谨性不足**：SFT 单 seed、n=6 相关性、3 点 non-monotonic claim、单 seed cross-scale 比较、全文无显著性检验\n2. **混淆变量未解耦**：GRPO 的 quantization vs group size、1.7B 的 repetition vs evidence benefit\n3. **贡献声明过度**：CED ≈ flat-NLI（自身消融否定）、EDCR 定义循环性、\"matches\" vs \"approaches\"\n4. **可复现性障碍**：dev-set only、训练数据量矛盾（9,042 vs 2,718）、内部编号（D076）泄露\n\n**升级路径**：如果能 (1) 提交 test set 结果，(2) 补充 SFT multi-seed + 统计检验，(3) 解耦 GRPO 实验或降级因果 claim，(4) 修正数据矛盾和 CED 贡献定位，论文有潜力升至 3.5 (Borderline Conference)。当前状态适合 Findings。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 约 230 words，符合长度要求但数据密集。\"Three findings emerge\" 后连续三段各带具体数字，读起来像实验摘要而非叙事\n- \"+8pp Ign-F1 benefit at 1.7B\" 在正文 fair subset 上为 +6.2pp，Abstract 应使用更保守数字\n- \"50.50 Ign-F1 matches 8B SFT performance (50.51)\" 基于单 seed，统计上无意义\n\n### Introduction\n- 叙事结构清晰（gap → formalization → findings → contributions），无 \"AI 写作\" 痕迹\n- Contribution 2（EDCR）和 Contribution 4（CED scoring）的贡献声明强度需要与 Analysis 消融结果对齐\n- \"QLoRA acts as a catastrophic amplifier\" (L30) 是未经验证的因果 claim\n\n### Related Work\n- Positioning 有效（encoder-based evidence vs LLM generation 的结构性差异讲得清楚）\n- 缺少 multi-task learning / task interference 文献——核心发现本质上是 negative transfer\n- 引用密度偏低（32 篇），bib 条目质量有问题（15 条 \"and others\"，5 条作者错误）\n\n### Method\n- Task formulation (§3.1) 清晰合理\n- CED (§3.4) 设计合理但消融显示 contrastive component 无增量贡献\n- EDCR (§3.5) 定义有循环性问题，需增量诊断价值论证\n- RSFT (§3.3) 训练数据量 9,042 vs Appendix 2,718 矛盾\n\n### Experiments\n- Main results (Table 1)：格式不一致（百分比/小数混用）；SFT 单 seed 无方差\n- Decoupling spectrum (Table 2)：GRPO 混淆变量；DPO 3ep 不同 protocol；n=6 相关性分析 power 不足\n- Scaling (Table 3)：3 点不足以建立 non-monotonic claim；1.7B benefit 有 repetition artifact 替代解释\n- Evidence strategy (§4.5)：inference-time CED reranking 在 Method 中无描述\n- Generalization (§4.6)：DREEAM 对比被埋在文字中，不在表格\n\n### Analysis\n- EDCR diagnostic 的核心论证受定义循环性影响\n- CED granularity 负面发现（sentence-level 失败）有价值但不支撑 CED 优于 flat-NLI\n- Practical implications 段的三条建议合理但证据基础不够牢固\n\n### Formatting\n- 模板正确（ACL review mode），匿名化完成\n- Limitations section 位置正确，内容诚实\n- 缺少 Responsible NLP Checklist（ARR 硬性要求，desk reject 风险）\n- 缺少 Ethics Statement（ARR 鼓励但不强制）\n- Appendix Figure caption relation type 数字矛盾（93 vs 76 vs 96）",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-18T07:01:16.981577+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_84537e1e2f9ef71a90742c2db859c6f2:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4619
}
```

</details>

---


### Assistant

_source line 102 · 2026-05-18T07:01:27.426438+00:00_

审稿报告已投递至 Research Director。

---

**Round 1 审稿完成汇报**

- **评分**：3.0 (Findings)，两位 Reviewer 完全一致
- **关键问题**：7 个 critical + 11 个 warning + 4 个 info = 22 条 issue
- **核心判断**：claim 强度系统性超过证据支撑力度

**Critical 问题摘要**：
1. GRPO 实验混淆变量（量化 vs group size 未解耦），去除 QLoRA 极端案例后 spectrum 叙事不成立
2. 全部结果仅 dev set，无 test set 提交
3. SFT baseline 单 seed，+4.92pp 无统计检验
4. Non-monotonic scaling 仅 3 点，1.7B benefit 有 repetition artifact 替代解释
5. EDCR 定义循环（分母就是 Rel-Recall）
6. CED ≈ flat-NLI（0.02pp），自身消融否定了独立贡献
7. 训练数据量矛盾（9,042 vs 2,718）

**升级路径**：补 test set + SFT multi-seed + 解耦 GRPO 实验 + 修正数据矛盾 → 有潜力至 3.5 Borderline Conference。

Issue Tracker 已同步至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 103 · 2026-05-18T07:01:30.239899+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

要点总结：R1 的 4 个 Must-Fix 全部 [AGREE]，唯一 [REBUT] 的是 W5（random selection baseline），因为 k=3 vs k=1 的消融和 SFT baseline 已部分回答了 data quality vs diversity 的问题，但仍建议补充 explicit random-k=1。我补充了 R1 未发现的额外证据：GRPO bf16 的 EDCR (0.6318) 实际低于 SFT (0.6982)，说明去除 QLoRA 极端案例后 spectrum 叙事可能不成立；1.7B SFT w/evi (47.86) > 4B SFT w/evi (39.74) 这一反直觉结果暗示 scale effect 可能被 model-specific 因素混淆。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 104 · 2026-05-18T07:01:40.639883+00:00_

审稿报告已提交至 Research Director。

**Round 1 审稿总结**：

- **评分**：3.0 (Findings)，两位 Reviewer 完全一致
- **收敛情况**：交叉回应后高度共识，仅 R1-W5（random baseline）存在轻微分歧（方向一致，严重程度不同）
- **7 个 Critical 问题**：GRPO 混淆变量、dev-set only、SFT 缺 multi-seed、non-monotonic over-interpreted、EDCR 定义循环、CED≈flat-NLI、训练数据量矛盾
- **11 个 Warning 问题**：涵盖统计 power、single-seed claims、baseline 缺失、超参数探索、格式不一致、引用不完整、Related Work 缺口等
- **核心判断**：claim 强度系统性超过证据支撑力度。补充 test set 结果、multi-seed 统计检验、解耦 GRPO 实验后有潜力升至 3.5

Issue Tracker 已同步更新（23 条 issues），报告已投递。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 10

## Round 10

62 recorded events


### User

_source line 105 · 2026-05-23T00:48:16.424666+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: faith-evidence-ie
- 论文路径: projects/faith-evidence-ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-07-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-23T00:48:25.341619+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-23T00:48:25.493153+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-23T00:48:33.621751+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-23T00:48:33.675418+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-23T00:48:44.863405+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-23T00:48:45.014985+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-23T00:48:54.504563+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-23T00:48:55.961119+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-23T00:48:59.876157+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-23T00:49:01.233339+00:00_

{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (336 个)\n\n- **mvp2_eval_lr5e6_r1_ckpt20**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_step90**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_step100**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_ckpt10**: DONE (success) — \n- **mvp2_eval_ced_kl001_r4_early**: DONE (negative) — \n- **mvp2_grpo_flatnli_r6**: DONE (negative) — \n- **mvp2_grpo_ced_kl001_r4**: DONE (success) — \n- **mvp2_sft_eval_r3**: DONE (success) — \n- **mvp2_grpo_extract_r3**: DONE (negative) — \n- **mvp2_grpo_ced_r5**: DONE (negative) — \n- **mvp2_sft_eval_r2**: DONE (success) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan017_14b_rsft_s43_generate | 14B RSFT s43 candidate generation: 用 SFT s43 adapter 生成 8 candidates/doc × 3027 docs。2-seed reproducibility pipeline 第 1 步。后续: CED scoring → RSFT train → eval，对比 s42 dev=0.5886/test=0.3849。 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **test_eval_4b_rsft_s42_no_evi** (success): 4B RSFT CED s42 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 with-evi test ign_f1=0.2501 计算 RSFT test evidence tax。完成后 RSFT test tax 表 3/5。 ← 基于 test_eval_4b_rsft_s42_v2\n- **test_eval_llama_rsft_s42_no_evi** (success): LLaMA RSFT s42 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 with-evi test ign_f1=0.3599 计算 RSFT test evidence tax。LLaMA SFT test tax=-4.94pp，RSFT dev tax=-2.17pp@2048。测试 test set 方向。 ← 基于 test_eval_llama_rsft_s42\n- **test_eval_1_7b_rsft_s42_no_evi** (success): 1.7B RSFT CED s42 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 with-evi test ign_f1=0.2933 计算 RSFT test evidence tax。1.7B SFT test tax=-4.31pp（evidence strongly helps），验证 RSFT 是否保持同方向。 ← 基于 test_eval_1_7b_
…[truncated 2529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-23T00:49:01.736019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-23T00:49:01.736438+00:00_

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
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/analysis}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-23T00:49:02.740566+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-23T00:49:02.941761+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 120 · 2026-05-23T00:49:13.542776+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 call for papers, ARR submission guidelines, and author instructions:

## Call for Papers Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important Dates

The ARR submission deadline for long and short papers is
…[truncated 1612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 10802
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-23T00:49:13.594079+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# faith-evidence-ie Memory\\n\\n## 服务器架构（2026-05-20 更新）\\n\\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\\n\\n## GPU 分配教训（2026-05-20）\\n\\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\\n\\n## 🔴 Cron 误判系统性问题（2026-05-22 — 待修复）\\n\\n两个实验（test_eval_4b_rsft_s42_v2, test_eval_1_7b_sft_s42）进程正常完成但被 cron 标记 failed。根因：\\n\\n| # | 问题 | 严重性 |\\n|---|------|--------|\\n| S1 | ssh_execute 提交的实验没有 sentinel 文件，cron 无法判断完成状态 | 高 |\\n| S2 | on_failed hook 重试走 ssh_execute（不走 submit_training_job），不写新 sentinel | 高 |\\n| S3 | cron 不验证 sentinel 时间戳，旧 sentinel 被复用导致重试实验继承前次失败状态 | 高 |\\n\\n**修复方案**（实验全部跑完后统一修）：\\n- 所有实验统一走 submit_training_job（含重试路径）\\n- check_status() 对比 sentinel.finished_at vs cron.created_at\\n- eval 实验增加 test_summary.json 存在性检查作为 W&B 替代信号\\n\\n**追加（2026-05-22）**：新 session 启动时 reconcile_crons 返回 0，6 个实验完成但 cron 全部丢失。需手动注册 cron + 从服务器 metrics.json 回收结果。\\n\\n## 🔴 Adapter 路径教训（2026-05-21 — 严重）\\n\\n**D140 全尺度 no-evi eval 全部用错了 adapter**。错误：用了 plan_014 训练的 \\\"no-evidence training regime\\\" adapter（训练数据本身不含 evidence），而非标准 SFT adapter + `--no_evidence` inference flag。\\n\\n**铁证**：trainer_state.json 中 tokens/step 差 ~18%（no_evidence adapter: 119,651 vs standard: 141,227）。\\n\\n**正确做法**：evidence tax = 同一个标准 SFT adapter，分别有/无 `--no_evidence` 参数，对比 ign_f1。\\n\\n**Qwen 各 scale 标准 SFT adapter 路径**：\\n- 1.7B: `/root/autodl-tmp/sft_outp
…[truncated 9833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10652
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-23T00:49:26.845446+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-23T00:49:28.953720+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 155\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_rewa
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2108
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-23T00:49:29.455476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-23T00:49:29.759393+00:00_

-rw-r--r-- 1 ubuntu ubuntu 434064 May 23 00:17 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-23T00:49:29.759835+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-23T00:49:30.764298+00:00_

-rw-r--r-- 1 ubuntu ubuntu 11804 May 18 07:44 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-23T00:49:30.865154+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
  "description": "Check existing review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-23T00:49:31.819930+00:00_

round_1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-23T00:49:31.820298+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit appendix anonymous review requirements site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission format page limit appendix anonymous review requirements site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-23T00:49:38.393161+00:00_

Web search results for query: "EMNLP 2026 ARR submission format page limit appendix anonymous review requirements site:aclrollingreview.org"

Links: [{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsible-nlp-checklist-appendices"}]

Based on the search results from the ACL Rolling Review website, here's what I found regarding EMNLP 2026 submission requirements:

**Submission Format and Page Limits:**
All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

**Appendix:**
Checkli
…[truncated 929 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 6572
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-23T00:50:04.387591+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-23T00:50:05.793603+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'faith-evidence-ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-23T00:50:05.844220+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/agent/project_config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/agent/project_config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-23T00:50:05.894946+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-23T00:50:12.627349+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-23T00:50:12.778252+00:00_

abstract.tex
analysis.tex
appendix.tex
conclusion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-23T00:50:15.756315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-23T00:50:16.359200+00:00_

1	\begin{abstract}
2	
3	Large Language Model (LLM) based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet these methods output bare relation triplets without identifying which sentences support each prediction.
4	Deployment contexts such as clinical knowledge bases and legal due-diligence systems require verifiable evidence that users can trace to source text.
5	Encoder-based evidence methods (SAIS, DREEAM) provide supporting sentences but trail LLM approaches in accuracy, leaving a gap between extraction performance and output verifiability.
6	
7	We formalize evidence-grounded DocRE as a structured generation task and compare Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets.
8	The na\"{i}ve expectation is that evidence generation always costs extraction accuracy. Our experiments reveal that this cost is not fixed but forms a landscape shaped by capacity, paradigm, and data quality. Within the Qwen3 family, evidence is beneficial at 1.7B ($-$5.63pp Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with Natural Language Inference (NLI) based scoring avoids decoupling entirely through output filtering rather than gradient pressure.
9	
10	RSFT compresses training seed variance 4.6--31$\times$ across Qwen3 and LLaMA (complete pairwise seed separation, Cohen's $d{=}2.58$). Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters. Test-set evaluation preserves model ranking across all evaluated scales (Spearman $\rho{=}1.0$).
11	
12	\end{abstract}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-23T00:50:16.409894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-23T00:50:16.813849+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \emph{which sentences} support each prediction.
6	In deployment contexts---clinical knowledge bases, legal due-diligence pipelines, financial compliance systems---users cannot verify a prediction without manually locating its textual basis across a multi-page document.
7	
8	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
9	Both produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.
10	The community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.
11	
12	This gap reflects a structural difference.
13	In encoder methods, evidence retrieval is classification that regularizes the encoder at negligible cost; in LLM-based DocRE, evidence requires the model to \emph{generate} additional output tokens per triple, increasing output length and decoding complexity.
14	The na\"{i}ve expectation is that this generation cost always harms extraction accuracy.
15	Our experiments show this expectation is wrong.
16	The evidence tax is not
…[truncated 2034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-23T00:50:16.914551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-23T00:50:16.965220+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
5	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
6	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding for multi-label prediction and localized context pooling for entity representations.
7	A parallel thread incorporates sentence-level evidence into these architectures.
8	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
9	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
10	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
11	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
12	Recent work has recast DocRE for large language models.
13	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
14	These methods match or surpass encoder baselines but produce bare triplets without evidence.
15	The critical distinction lies in computational nature: in SAIS and DREEAM, evidence
…[truncated 2627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-23T00:50:17.279363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-23T00:50:17.330178+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support.
8	
9	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.
10	
11	
12	\subsection{Supervised Fine-Tuning Baseline}
13	\label{sec:sft}
14	
15	We fine-tune all models with LoRA~\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to all linear projections (attention and feed-forward). The training data consists of DocRED~\citep{yao2019docred} training documents converted to 
…[truncated 8436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-23T00:50:21.555200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-23T00:50:22.058404+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Dataset.}
8	We conduct experiments on DocRED~\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\citep{tan2022redocred} for cross-dataset generalization evaluation.
9	
10	\paragraph{Models.}
11	Our primary model is Qwen3-4B. To study scale effects, we also train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.
12	
13	\paragraph{Training.}
14	All models use LoRA~\citep{hu2022lora} with rank $r{=}64$ and $\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\S\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.
15	
16	\paragraph{Metrics.}
17	\textbf{Ign-F1} (primary) ignores training-set triples per the official DocRED protocol. \textbf{Rel-F1} measures extraction F1 on all triples. \textbf{Evi-F1 (TP-only)} measures evidence F1 conditioned on correct triples; \textbf{Evi-F1 (joint)} follows the DREEAM protocol~\citep{ma2023dreeam} for cross-method comparison. \textbf{EDCR} (\S\ref{sec:edcr}) diagnoses extraction-evidence decoupling. All results use the development set.
18	
19	
20	\subsection{Main Results}
21	\label{sec:main_results}
22	
23	Table~\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mea
…[truncated 11641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-23T00:50:22.058880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-23T00:50:22.615667+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{EDCR as a diagnostic.}
5	EDCR (\S\ref{sec:edcr}) correlates with extraction quality at two levels: cross-method ($\rho = -0.89$, $n = 7$, $p = 0.007$; Table~\ref{tab:spectrum}) and per-relation ($\rho = -0.79$, $n = 76$, $p < 0.001$), the latter providing validation independent of method-level sample size and orthogonal to Evi-F1 ($\rho = -0.06$, $p = 0.58$; Appendix~\ref{sec:edcr_per_relation}). RSFT avoids decoupling because discrete output selection cannot exploit the extraction-evidence trade-off (Appendix~\ref{sec:rsft_theory}). CED operates effectively at the response level but fails at sentence-level granularity (Evi-F1 $-$7.7pp), as filtering individual sentences disrupts co-reference chains.
6	
7	\paragraph{Ablation.}
8	CED and flat-NLI produce comparable RSFT performance (Rel-F1 45.63 vs.\ 45.61); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\times$ fewer examples; CED filtering is insensitive to NLI scorer capacity (+1.10pp with DeBERTa-v3-large vs.\ v3-base, within seed noise; Appendix~\ref{sec:ablation_full}).
9	
10	\paragraph{Error patterns.}
11	RSFT reduces truncation FN, hallucinated FP, and duplicates by 6--22\% across scales, but evidence quality is unchanged ($\Delta < 0.4$pp; Appendix~\ref{sec:error_analysis}). RSFT improves \emph{what} the model extracts but not \emph{how well} it grounds extractions.
12	
13	\paragraph{Practical implications.}
14	Three guidelines for evidence-grounded IE: (1) avoid online RL for multi-objective generation where capability coupling matters; (2) prefer RSFT with strict selection ($k{=}1$) over training data quantity (4.6--31$\times$ variance compression across Qwen3 and LLaMA); (3) consider CED reranking at inference for deployment scenarios requiring both extraction accuracy and evidence quality.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-23T00:50:22.616166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-23T00:50:22.967838+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task and compare three post-training paradigms across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax is not a fixed penalty: it forms a landscape where capacity determines whether evidence regularizes or is absorbed, optimization paradigm determines decoupling severity, and data quality filtering enables RSFT to navigate without gradient-induced trade-offs.
5	
6	RSFT compresses training variance by up to 31$\times$ while improving mean extraction across all tested scales. A 1.7B RSFT model approaches 8B SFT performance at 4.7$\times$ fewer parameters, demonstrating that evidence-grounded extraction can be both accurate and deployment-efficient.
7	
8	Future work should investigate targeted evidence rewards---RSFT improves extraction but leaves evidence quality largely unchanged---and extend evaluation to non-Wikipedia domains where evidence annotation is currently unavailable.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-23T00:50:22.968198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-23T00:50:23.018699+00:00_

1	\section{Limitations}
2	
3	Primary development is on the DocRED development set; Re-DocRED test-set evaluation preserves model ranking (Spearman $\rho{=}1.0$) but shows a 18.9--21.9pp absolute drop attributable to higher annotation density (2.82$\times$ more gold triples per document). Exact-match F1 penalizes surface-form-different entity mentions~\citep{wan2024genres}, likely underestimating absolute extraction capability of generative models, though relative comparisons between methods remain valid.
4	
5	We evaluate on two datasets (DocRED, Re-DocRED), both derived from Wikipedia. Cross-domain evaluation is constrained by the absence of evidence-annotated DocRE datasets beyond Wikipedia; this limitation is shared by all prior evidence-aware DocRE work (SAIS, DREEAM, EIDER).
6	
7	We evaluate one algorithm per RL family (GRPO, DPO) with single hyperparameter settings (KL coefficient 0.01, $\beta$ 0.1); other algorithms or settings may produce different decoupling behaviors. CED scoring depends on an external NLI model, and the RSFT ablation uses limited seeds (four for CED, two for flat-NLI). Evidence tax patterns span two model families (Qwen3, LLaMA) but may not generalize to other architectures or scales beyond 14B.
8	
9	EDCR correlates with extraction quality at both method level ($\rho{=}{-}0.89$, $n{=}7$) and per-relation level ($\rho{=}{-}0.79$, $n{=}76$), but has not been validated against human judgments of evidence-extraction alignment. Future work should assess whether EDCR rankings correspond to practitioner assessments of output quality.
10	
11	RSFT improves extraction across scales but evidence quality is unchanged (Evi-F1 $\Delta < 0.4$pp at all scales; Appendix~\ref{sec:error_analysis}). CED-based selection filters for joint quality but does not specifically optimize evidence grounding, suggesting that targeted evidence rewards may be needed to improve evidence quality beyond what data selection achieves.
12	
13	At 1.7B scale, 44.4\% of outputs ex
…[truncated 851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-23T00:50:28.145835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-23T00:50:28.799143+00:00_

1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	Base model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\
16	LoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\
17	LoRA $\alpha$ & 128 & 128 & 128 & 128 & 128 \\
18	Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
19	Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
20	Epochs & 3 & 3 & -- & -- & 1, 3\textsuperscript{$\star$} \\
21	Max steps & -- & -- & 100 & 100 & -- \\
22	Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	Max new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\
24	Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
25	Group size $G$ & -- & -- & 4 & 8 & -- \\
26	KL coefficient & -- & -- & 0.01 & 0.01 & -- \\
27	$\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\
28	Candidates $N$ & -- & 8 & -- & -- & 8 \\
29	Top-$k$ selection & -- & 1 & -- & -- & -- \\
30	Training samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\
31	Scoring function & -- & CED & CED & CED & CED \\
32	\bottomrule
33	\end{tabular}
34	\vspace{1mm}
35	{\raggedright\footnotesize \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics 
…[truncated 32273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-23T00:50:28.950838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-23T00:50:28.951398+00:00_

1	@inproceedings{autore2024,
2	  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},
3	  author    = {Xue, Lilong and Zhang, Dan and Dong, Yuxiao and Tang, Jie},
4	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
5	  year      = {2024},
6	  url       = {https://arxiv.org/abs/2403.14888}
7	}
8	
9	@inproceedings{chen2025docksrag,
10	  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},
11	  author    = {Xu, Xiaolong and Zhou, Yibo and Xiang, Haolong and Li, Xiaoyong and Zhang, Xuyun and Qi, Lianyong and Dou, Wanchun},
12	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
13	  year      = {2025},
14	  url       = {https://proceedings.mlr.press/v267/xu25am.html}
15	}
16	
17	@article{dai2025r1re,
18	  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},
19	  author  = {Dai, Runpeng and Zheng, Tong and Yang, Run and Yu, Kaixian and Zhu, Hongtu},
20	  journal = {arXiv preprint arXiv:2507.04642},
21	  year    = {2025},
22	  url     = {https://arxiv.org/abs/2507.04642}
23	}
24	
25	@inproceedings{gao2023scaling,
26	  title     = {Scaling Laws for Reward Model Overoptimization},
27	  author    = {Gao, Leo and Schulman, John and Hilton, Jacob},
28	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
29	  year      = {2023},
30	  url       = {https://arxiv.org/abs/2210.10760}
31	}
32	
33	@inproceedings{hu2022lora,
34	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
35	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
36	  booktitle = {International Conference on Learning Representations},
37	  year      = {2022},
38	  url       = {https://arxiv.org/abs/2106.09685}
39	}
40	
41	@article{jin2025rl_panace
…[truncated 494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-23T00:50:36.128248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-23T00:50:36.783182+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf (423.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-23T00:51:14.375402+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "faith-evidence-ie",
  "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "faith-evidence-ie",
    "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-23T00:51:54.051859+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 39676
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-23T00:51:54.253040+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 论文信息\n- **标题**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n- **路径**: projects/faith-evidence-ie/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf\n- **目标 Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-07-15（commitment deadline）\n\n## Venue 要求\n- ARR 统一审稿，Main/Findings 不分开投稿\n- Long paper: 正文 8 页限制，参考文献不限\n- Mandatory limitations + optional ethics statement 不计入页数\n- Double-blind 匿名审稿\n- ACL 模板\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n1. **CED 评分函数（Section 3.4）的严谨性**：\n   - CED = p⁺ − max_j p⁻_j 这个公式是否合理？正向 NLI 分数和负向 NLI 分数的组合是否有理论依据？\n   - Document-level CED 加权方式（只有正确 triple 贡献 CED）是否引入循环依赖——用 gold label 选择 triple 来评估 scoring function？\n   - CED 与 flat-NLI 效果几乎一样（Rel-F1 差 0.02pp），这是否说明 contrastive formulation 的价值有限？\n\n2. **EDCR 指标（Section 3.5）的统计有效性**：\n   - EDCR = Evi-Recall_TP / Rel-Recall，分子分母共享 Rel-Recall 相关成分。论文声称 cross-method 相关性 (ρ=−0.89, n=7) 但 n=7 样本量极小，p=0.007 在多重比较下是否可靠？\n   - Per-relation 相关性 (ρ=−0.79, n=76) 是否也存在共享成分问题？\n   - EDCR 作为新指标是否有充分验证（论文也承认缺乏 human judgment 验证）？\n\n3. **方差压缩声明的统计基础**：\n   - \"4.6–31× variance compression\" 声明基于 3 个 seed 的 std 比较。n=3 的方差估计极不稳定——3 个观测值的标准差置信区间是多少？\n   - SFT 和 RSFT 测的是不同来源的方差（SFT: 完整训练的 seed 方差；RSFT: 固定基础上的微调方差），直接比较是否公平？论文承认了这一点但仍做了强声明。\n   - Cohen's d=2.58 是从 n=3 计算的——小样本 effect size 估计是否可信？\n\n4. **实验控制与公平性**：\n   - GRPO QLoRA 使用 4-bit 量化 G=4，GRPO bf16 使用 G=8——变量未隔离（精度和 group size 同时变化），collapse 到底是量化还是 group size 导致的？\n   - DPO 3-epoch 用的是 \"earlier evaluation protocol\"，这个差异对 decoupling spectrum 的可比性影响多大？\n   - Evidence tax 在不同 scale 使用不同 seed（1.7B 用 s42, 4B 用 Method B s44），控制变量是否充分？\n   - 4B retrained checkpoint 用于 test（原始不可用），dev 性能 \"comparable\"（43.88 vs 44.23）但有 0.35pp 差距，是否影响结论？\n\n5. **Test set 结果的可靠性**：\n   - Dev 到 test 有 ~20pp drop，论文归因于 annotation density 2.82×。但这个 drop 是否太大，是否有过拟合 dev set 的嫌疑？\n   - 14B RSFT 在 test 上反而低于 SFT（−0.37pp），但论文解释为 \"truncation rate\" 不同——这个解释是否充分？\n\n6. **基线比较的公平性**：\n   - 与 encoder methods (ATLOP, SAIS, DREEAM) 的对比：Ign-F1 差距 16-18pp（encoder ~62, LLM ~45），论文只强调 TP-only Evi-F1 >80%——这是否是 cherry-picking 指标？\n   - 没有与其他 LLM-based RE 方法（AutoRE, LMRC 等）的直接数值对比。\n\n请按以下格式输出审稿意见：\n### Summary（2-3句）\n### Strengths（逐条）\n### Weaknesses（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）\n### Questions（需要作者澄清的）\n### Missing References（如有）\n### Overall Assessment（评分 + 置信度 + 理由）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 论文信息\n- **标题**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n- **路径**: projects/faith-evidence-ie/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf\n- **目标 Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-07-15（commitment deadline）\n\n## Venue 要求\n- ARR 统一审稿，Main/Findings 不分开投稿\n- Long paper: 正文 8 页限制，参考文献不限\n- Mandatory limitations + optional ethics statement 不计入页数\n- Double-blind 匿名审稿\n- ACL 模板\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n1. **CED 评分函数（Section 3.4）的严谨性**：\n   - CED = p⁺ − max_j p⁻_j 这个公式是否合理？正向 NLI 分数和负向 NLI 分数的组合是否有理论依据？\n   - Document-level CED 加权方式（只有正确 triple 贡献 CED）是否引入循环依赖——用 gold label 选择 triple 来评估 scoring function？\n   - CED 与 flat-NLI 效果几乎一样（Rel-F1 差 0.02pp），这是否说明 contrastive formulation 的价值有限？\n\n2. **EDCR 指标（Section 3.5）的统计有效性**：\n   - EDCR = Evi-Recall_TP / Rel-Recall，分子分母共享 Rel-Recall 相关成分。论文声称 cross-method 相关性 (ρ=−0.89, n=7) 但 n=7 样本量极小，p=0.007 在多重比较下是否可靠？\n   - Per-relation 相关性 (ρ=−0.79, n=76) 是否也存在共享成分问题？\n   - EDCR 作为新指标是否有充分验证（论文也承认缺乏 human judgment 验证）？\n\n3. **方差压缩声明的统计基础**：\n   - \"4.6–31× variance compression\" 声明基于 3 个 seed 的 std 比较。n=3 的方差估计极不稳定——3 个观测值的标准差置信区间是多少？\n   - SFT 和 RSFT 测的是不同来源的方差（SFT: 完整训练的 seed 方差；RSFT: 固定基础上的微调方差），直接比较是否公平？论文承认了这一点但仍做了强声明。\n   - Cohen's d=2.58 是从 n=3 计算的——小样本 effect size 估计是否可信？\n\n4. **实验控制与公平性**：\n   - GRPO QLoRA 使用 4-bit 量化 G=4，GRPO bf16 使用 G=8——变量未隔离（精度和 group size 同时变化），collapse 到底是量化还是 group size 导致的？\n   - DPO 3-epoch 用的是 \"earlier evaluation protocol\"，这个差异对 decoupling spectrum 的可比性影响多大？\n   - Evidence tax 在不同 scale 使用不同 seed（1.7B 用 s42, 4B 用 Method B s44），控制变量是否充分？\n   - 4B retrained checkpoint 用于 test（原始不可用），dev 性能 \"comparable\"（43.88 vs 44.23）但有 0.35pp 差距，是否影响结论？\n\n5. **Test set 结果的可靠性**：\n   - Dev 到 test 有 ~20pp drop，论文归因于 annotation density 2.82×。但这个 drop 是否太大，是否有过拟合 dev set 的嫌疑？\n   - 14B RSFT 在 test 上反而低于 SFT（−0.37pp），但论文解释为 \"truncation rate\" 不同——这个解释是否充分？\n\n6. **基线比较的公平性**：\n   - 与 encoder methods (ATLOP, SAIS, DREEAM) 的对比：Ign-F1 差距 16-18pp（encoder ~62, LLM ~45），论文只强调 TP-only Evi-F1 >80%——这是否是 cherry-picking 指标？\n   - 没有与其他 LLM-based RE 方法（AutoRE, LMRC 等）的直接数值对比。\n\n请按以下格式输出审稿意见：\n### Summary（2-3句）\n### Strengths（逐条）\n### Weaknesses（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）\n### Questions（需要作者澄清的）\n### Missing References（如有）\n### Overall Assessment（评分 + 置信度 + 理由）"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-23T00:52:16.163834+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21910
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-23T00:52:16.366610+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 论文信息\n- **标题**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n- **路径**: projects/faith-evidence-ie/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf\n- **目标 Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-07-15（commitment deadline）\n\n## Venue 要求\n- ARR 统一审稿，Main/Findings 不分开投稿\n- Long paper: 正文 8 页限制，参考文献不限\n- Mandatory limitations + optional ethics statement 不计入页数\n- Double-blind 匿名审稿\n- ACL 模板\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n1. **贡献原创性**：\n   - Contribution 1（evidence tax is scale-dependent）：这是一个实验观察，不是方法创新。是否足够构成独立贡献？\n   - Contribution 2（decoupling spectrum）：GRPO/DPO/RSFT 表现不同是一个经验发现。EDCR 是新指标，但定义简单（ratio of two recalls）——是否足够 novel？\n   - Contribution 3（RSFT variance compression）：RSFT 本身不是新方法（论文承认 \"well-established\"），应用于 DocRE + CED scoring 是否足够新颖？\n   - 整体：论文更像 empirical study + scaling analysis，还是有实质性方法贡献？对 EMNLP 来说是否足够？\n\n2. **Related Work 覆盖**：\n   - DocRE 领域是否有遗漏的重要工作？特别是 2024-2025 的 LLM-based DocRE 方法。\n   - RSFT/rejection sampling 在其他 NLP 任务的应用是否充分讨论？\n   - Multi-objective RL 和 reward hacking 的文献是否充分？\n   - NLI-based evaluation 在 IE 领域的先驱工作是否覆盖？\n   - 搜索最新相关工作，检查是否有遗漏。\n\n3. **论文结构与叙事**：\n   - Abstract 是否准确反映论文内容？是否过度声明？\n   - Introduction 的 \"gap\" 叙事（accurate extractors have no evidence, evidence-capable methods are not competitive）是否有力？\n   - Method section 是否清晰？CED 和 EDCR 各自的角色是否容易理解？\n   - Experiments 结构是否合理？主实验、scaling、ablation 的安排是否自然？\n   - Analysis section 是否提供了超越 experiments 的洞察？\n   - Conclusion 是否恰当总结？是否有过度声明？\n\n4. **格式合规检查**：\n   - 正文是否在 8 页以内？\n   - Limitations section 是否存在且内容适当？\n   - Ethics statement 是否存在？\n   - 匿名是否完整（无作者信息泄露、无 self-reference）？\n   - 引用格式是否使用 natbib？\n   - 表格/图片质量是否达到出版标准？\n   - ARR Responsible NLP Checklist 是否在 OpenReview form 中（而非 PDF 中）？\n\n5. **写作质量**：\n   - 技术写作是否清晰、准确？\n   - 是否有语法/拼写错误？\n   - 数字引用是否一致（论文中的数字是否与表格一致）？\n   - 是否有 AI 写作风格的痕迹（过度使用特定短语模式）？\n\n6. **Limitations 评估**：\n   - 论文的 limitations section 是否诚实覆盖了真正的限制？\n   - 是否有未提及的重要限制？\n\n请按以下格式输出审稿意见：\n### Summary（2-3句）\n### Strengths（逐条）\n### Weaknesses（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）\n### Questions（需要作者澄清的）\n### Missing References（如有）\n### Overall Assessment（评分 + 置信度 + 理由）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 论文信息\n- **标题**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n- **路径**: projects/faith-evidence-ie/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_2/submitted.pdf\n- **目标 Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-07-15（commitment deadline）\n\n## Venue 要求\n- ARR 统一审稿，Main/Findings 不分开投稿\n- Long paper: 正文 8 页限制，参考文献不限\n- Mandatory limitations + optional ethics statement 不计入页数\n- Double-blind 匿名审稿\n- ACL 模板\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查重点\n\n1. **贡献原创性**：\n   - Contribution 1（evidence tax is scale-dependent）：这是一个实验观察，不是方法创新。是否足够构成独立贡献？\n   - Contribution 2（decoupling spectrum）：GRPO/DPO/RSFT 表现不同是一个经验发现。EDCR 是新指标，但定义简单（ratio of two recalls）——是否足够 novel？\n   - Contribution 3（RSFT variance compression）：RSFT 本身不是新方法（论文承认 \"well-established\"），应用于 DocRE + CED scoring 是否足够新颖？\n   - 整体：论文更像 empirical study + scaling analysis，还是有实质性方法贡献？对 EMNLP 来说是否足够？\n\n2. **Related Work 覆盖**：\n   - DocRE 领域是否有遗漏的重要工作？特别是 2024-2025 的 LLM-based DocRE 方法。\n   - RSFT/rejection sampling 在其他 NLP 任务的应用是否充分讨论？\n   - Multi-objective RL 和 reward hacking 的文献是否充分？\n   - NLI-based evaluation 在 IE 领域的先驱工作是否覆盖？\n   - 搜索最新相关工作，检查是否有遗漏。\n\n3. **论文结构与叙事**：\n   - Abstract 是否准确反映论文内容？是否过度声明？\n   - Introduction 的 \"gap\" 叙事（accurate extractors have no evidence, evidence-capable methods are not competitive）是否有力？\n   - Method section 是否清晰？CED 和 EDCR 各自的角色是否容易理解？\n   - Experiments 结构是否合理？主实验、scaling、ablation 的安排是否自然？\n   - Analysis section 是否提供了超越 experiments 的洞察？\n   - Conclusion 是否恰当总结？是否有过度声明？\n\n4. **格式合规检查**：\n   - 正文是否在 8 页以内？\n   - Limitations section 是否存在且内容适当？\n   - Ethics statement 是否存在？\n   - 匿名是否完整（无作者信息泄露、无 self-reference）？\n   - 引用格式是否使用 natbib？\n   - 表格/图片质量是否达到出版标准？\n   - ARR Responsible NLP Checklist 是否在 OpenReview form 中（而非 PDF 中）？\n\n5. **写作质量**：\n   - 技术写作是否清晰、准确？\n   - 是否有语法/拼写错误？\n   - 数字引用是否一致（论文中的数字是否与表格一致）？\n   - 是否有 AI 写作风格的痕迹（过度使用特定短语模式）？\n\n6. **Limitations 评估**：\n   - 论文的 limitations section 是否诚实覆盖了真正的限制？\n   - 是否有未提及的重要限制？\n\n请按以下格式输出审稿意见：\n### Summary（2-3句）\n### Strengths（逐条）\n### Weaknesses（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）\n### Questions（需要作者澄清的）\n### Missing References（如有）\n### Overall Assessment（评分 + 置信度 + 理由）"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-23T00:52:17.732066+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1365
}
```

</details>

---


### Assistant

_source line 166 · 2026-05-23T00:52:26.573475+00:00_

已并行派发：
- **视觉审查 Agent**：已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性）：已分配

等待两位 Reviewer 的初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 167 · 2026-05-23T00:57:46.989050+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction
**Venue**: EMNLP 2026 (ACL ARR)

---

### Summary（2-3句）

本文将 evidence-grounded DocRE 形式化为结构化生成任务，系统比较了三种 post-SFT 优化范式（GRPO、DPO、RSFT）在 evidence 生成与 relation extraction 之间的 trade-off。核心发现包括：(1) evidence tax 是 scale-dependent 的（1.7B 有益、4B+ 中性）；(2) 梯度优化方法导致 extraction-evidence decoupling，离散选择方法（RSFT）可避免；(3) RSFT 通过 CED-based 样本选择压缩训练方差。论文覆盖面广（1.7B-14B，Qwen3/LLaMA 两个 model family），分析视角有启发性，但多处统计推断基础薄弱。

---

### Strengths

**S1. 问题定位精准且实用。** Evidence grounding 是 LLM-based IE 部署中的真实痛点——临床知识库、法律尽调等场景需要可溯源的抽取结果。论文清晰地指出 encoder 方法（SAIS、DREEAM）和 LLM 方法在 evidence 处理上的结构性差异（分类 vs. 生成），这一 framing 具有 community 价值。

**S2. Decoupling spectrum 概念有分析价值。** 将 GRPO collapse、GRPO mild decoupling、DPO gradual decay、RSFT no decoupling 组织为一个连续谱（Table 2, Figure 1），从优化机制角度（gradient pressure vs. discrete selection）解释了为什么不同范式表现不同。这种分析视角比简单报告"方法 A 比方法 B 好"更有洞察力。

**S3. 跨尺度 + 跨 model family 的实验覆盖。** 1.7B/4B/8B/14B（Qwen3）+ LLaMA-3.1-8B 的五模型覆盖，加上 Re-DocRED 的 cross-dataset 验证（Table 9-10），在同类工作中覆盖面较好。

**S4. 对自身局限的透明度。** 论文主动承认了多项局限：EDCR 缺乏 human judgment 验证、variance 估计基于 3 seeds、SFT vs RSFT variance 测量的不同来源（Section 7）。这种透明度值得肯定，但承认局限不等于解决了它们。

**S5. 定性分析具体有用。** Section M 的三个 case study（evidence quality、GRPO format gaming、per-relation EDCR diagnostics）用具体例子展示了 EDCR 指标的诊断价值，比如 `date_of_birth` (EDCR=0.119) vs `head_of_government` (EDCR=0.936) 的对比。

---

### Weaknesses

**W1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础。**

论文的第三个核心贡献是 "RSFT compresses training variance 4.6–31×"（Abstract, Section 4.3），并给出 Cohen's d=2.58。但这些都基于 3 个 seed 的 std 比较。

- **置信区间极宽**：n=3 时方差估计的自由度 df=2。根据 χ² 分布，σ 的 95% CI 约为 [0.52s, 6.29s]——即真实 σ 可能比估计值大 6 倍或小 2 倍。当两组各 n=3 时，方差比的 F(2,2) 分布的 95% CI 跨越数个数量级。声称 "31× compression" 在统计上几乎无法从 n=3 中可靠估计。
- **Cohen's d=2.58 不可信**：小样本 effect size 的抽样分布极宽，n=3 时 d 的标准误约为 1.2-1.5，95% CI 覆盖从接近 0 到 >5 的范围。论文不应将其作为核心声明呈现。
- **建议**：至少增加到 5-10 seeds（尤其对 1.7B 这样训练成本低的尺度可行），或将方差压缩声明从 contribution 降级为 observation，并报告 bootstrap CI。

**W2 [CRITICAL] — EDCR 的 shared-component 问题使 cross-method 相关性不可靠。**

EDCR = Evi-Recall_TP / Rel-Recall。展开：

Evi-Recall_TP = TP_evi / TP，Rel-Recall = TP / G（G 为 gold triples 总数）

因此 EDCR = (TP_evi × G) / TP²

TP 同时出现在分子和分母中。当一个方法找到更多正确 relation（TP↑），Rel-Recall 机械性增大（EDCR 分母↑），而新增 TP 如果 evidence 质量较低则 Evi-Recall_TP 下降（EDCR 分子↓）。这构造了一个**机械性负相关**——即使 evidence 能力和 extraction 能力完全独立，EDCR 也会随 Rel-Recall 增加而降低。

- 论文声称 cross-method ρ=−0.89 (n=7, p=0.007)（Section 5），但 n=7 极小，一个 outlier（如 GRPO QLoRA collapse 的极端点 EDCR=0.9876）可能主导相关性。移除该点后相关性是否仍然显著？
- Per-relation ρ=−0.79 (n=76) 面临同样的 shared-component 问题，因为 per-relation EDCR 结构相同。
- **建议**：(1) 报告移除 GRPO QLoRA extreme point 后的 cross-method 相关性；(2) 用 permutation test 或 partial correlation 控制 TP 的共享效应；(3) 展示 EDCR 与 Evi-F1（不含 shared component）的对比来证明 EDCR 的增量诊断价值。

**W3 [MAJOR] — CED contrastive formulation 的增量价值不足。**

Section 3.4 引入 CED = p⁺ − max_j p⁻_j 作为 contrastive evidence discrimination score。但 Appendix B 的消融显示 CED vs flat-NLI（仅用 p⁺）在 RSFT 中的 Rel-F1 差异仅 0.02pp（45.63 vs 45.61）。

- 减法操作（p⁺ − max_j p⁻_j）缺乏理论动机：为什么是差值而非比值（p⁺/max p⁻_j）或 log-ratio？论文仅说 "This formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities"（Section 3.4），但没有解释为什么减法最优。
- 0.02pp 的差异在 noise level 以内（3-seed std 约 0.09pp），contrastive 组件对下游无实质影响。
- 论文说 "confirming that the contrastive formulation is not essential for data selection quality"（Section 3.4 末段），这实际上削弱了 CED 作为方法贡献的分量。
- **建议**：降低 CED 的 novelty claim，或提供 CED 在更困难场景（如 long-tail relation types、entity-dense documents）中优于 flat-NLI 的证据。

**W4 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol 影响 decoupling spectrum 的可比性。**

Footnote 1（page 6）提到 "DPO 3-epoch results use an earlier evaluation protocol, included for trend analysis"。但 Table 2 将 DPO 3-epoch 与其他方法并列在同一个 decoupling spectrum 表中，读者容易将其视为直接可比的数据点。

- Decoupling spectrum（Section 4.3, Figure 1）是本文的核心分析框架之一。如果其中一个数据点（DPO 3-epoch）来自不同 protocol，整个 spectrum 的可靠性受质疑。
- "Earlier evaluation protocol" 具体差异是什么？这会如何影响 Rel-F1 和 Evi-F1 的计算？论文未充分说明。
- **建议**：在相同 protocol 下重跑 DPO 3-epoch 评估，或在 Table 2 中明确标注并从 spectrum 分析中排除。

**W5 [MAJOR] — SFT vs RSFT variance 测量的不同来源使得直接比较不公平。**

SFT 的 variance 来自 3 个独立 full training runs（不同 seed），RSFT 的 variance 来自在固定 SFT base 上的 fine-tuning（不同 seed）。这测量的是不同层次的随机性：

- SFT variance = 数据打乱 + 初始化 + 训练动态的综合方差
- RSFT variance = 候选样本选择 + fine-tuning 的方差（base model 固定）

RSFT 的方差天然更小，因为大部分随机性被 base model 吸收了。论文在 Section 7 承认了这一点（"RSFT reflects additional fine-tuning from a fixed base"），但仍在 Abstract 和 Contribution 中将 "4.6–31× variance compression" 作为核心声明。

- 公平比较应是：从相同 3 个 SFT checkpoint 分别做 RSFT，报告端到端方差（而非仅 RSFT 阶段方差）。
- 或至少将此作为 observation 而非 contribution 呈现，明确说明这是不同方差来源的比较。

**W6 [MAJOR] — Dev→Test 20pp drop 的解释不够充分。**

Table 9 显示 Ign-F1 从 dev ~45 降到 test ~25-28（约 18-20pp drop）。论文归因于 Re-DocRED test set 的 annotation density 是 dev 的 2.82×。

- 2.82× 的 annotation density 差异确实会增加 recall 难度，但 20pp drop 的幅度仍然令人担忧。是否有 dev set overfitting 的可能？例如，hyperparameter tuning 和 model selection 都在 dev 上进行。
- 14B RSFT 在 test 上低于 SFT 0.37pp（Table 9 注释），论文解释为 "truncation rate" 差异。但如果 RSFT 的优势在 test 上消失甚至反转，这是否意味着 RSFT 的 gain 不够 robust？
- **建议**：报告 test set 上的完整 decoupling 分析（不仅是 Ign-F1），展示 dev 上观察到的 pattern 是否在 test 上 replicate。

**W7 [MINOR] — 与 encoder baseline 的比较选择性呈现指标。**

Table 12（Appendix）显示 encoder 方法（ATLOP、SAIS、DREEAM）的 Ign-F1 约 62，而 LLM 方法约 45，差距 16-18pp。论文在主文中主要强调 TP-only Evi-F1（>80%）和 EDCR 优势，未充分讨论这一巨大性能差距的含义。

- 论文第 7 页最后一段提到 "encoder methods achieve substantially higher extraction performance (Rel-F1 60-63 vs. our 45-56)"，但将其归因于 "architecture-specific optimization for the classification formulation"，篇幅很少。
- 对于 deployment 场景的用户，Ign-F1 45 vs 62 是一个实质性差距。论文应更充分讨论 LLM-based 方法何时值得这一性能牺牲。

**W8 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比。**

Related Work（Section 2）讨论了 AutoRE (Xue et al., 2024)、GildRE、ReLLM 等 LLM-based 方法，但 Table 12 仅对比 encoder 方法。虽然这些方法可能不产 evidence，但至少可以在 Rel-F1 上直接比较。

**W9 [MINOR] — 4B retrained checkpoint 的 dev performance 差距 0.35pp 可能影响 evidence tax 分析。**

Section 4.1 提到原始 4B checkpoint 不可用，retrained version 的 dev Ign-F1 为 43.88 vs 原始 44.23（差 0.35pp）。0.35pp 虽然看似小，但论文在 evidence tax 分析中关注的差异也在 0.25-0.47pp 量级（Section 4.4, Appendix E），这意味着 checkpoint 差异可能与被分析的效应大小可比。

---

### Questions（需要作者澄清）

**Q1.** Cross-method EDCR 相关性 (ρ=−0.89, n=7) 中，移除 GRPO QLoRA collapse 的极端数据点后，ρ 和 p-value 变为多少？

**Q2.** RSFT variance 声明中的 "4.6–31×" 区间对应哪些具体 scale？请提供每个 scale 的 SFT std 和 RSFT std 的 95% CI（基于 χ² 分布）。

**Q3.** DPO 3-epoch 的 "earlier evaluation protocol" 与当前 protocol 的具体差异是什么？是 max_new_tokens、format-compliant intersection 筛选规则、还是其他？

**Q4.** 关于 evidence tax（Section 4.4, Appendix E）：Qwen3-1.7B 的 training-time evidence tax（约 −5.19±5.25pp）方差极大——这是否意味着 evidence tax 的 direction 在 1.7B 上也不稳定？

**Q5.** CED 的减法公式 (p⁺ − max p⁻_j) 是否尝试过其他组合方式（ratio、log-ratio、learned combination）？如何确定减法是最佳选择？

**Q6.** Table 2 中 GRPO bf16 G=4 和 G=8 的 Rel-F1 分别是多少？论文是否可以明确隔离 group size vs precision 对 collapse 的独立贡献？

---

### Missing References

- 未发现明显遗漏的关键引用。Related Work 覆盖了 DocRE（DocRED, ATLOP, DREEAM）、LLM-based IE（AutoRE, GildRE）、RL alignment（GRPO, DPO, RAFT）、evidence faithfulness（StAR）等主要线索。
- 可考虑引用 Wadhwa et al. (2023) "Revisiting Relation Extraction in the era of Large Language Models" 作为 LLM-based RE 的综述性参考（如未引用）。

---

### Overall Assessment

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 论文提出了有价值的分析框架（evidence tax、decoupling spectrum、EDCR），实验覆盖面广，但核心统计声明（variance compression、EDCR correlation）的推断基础薄弱，需要加固。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法（CED、RSFT）合理，但多处统计推断基础薄弱：n=3 的 variance claim、EDCR shared-component、CED 增量价值不足。方法假设总体成立但验证不够严格 |
| Excitement | 3.5/5 | Evidence tax 和 decoupling spectrum 概念有新意且对社区有启发价值；RSFT 本身是标准 rejection sampling，方法创新有限；分析型贡献 > 方法型贡献 |
| Reproducibility | 4/5 | Hyperparameters 详尽（Table 4, Appendix A），数据集公开（DocRED），CED 依赖外部 NLI model（DeBERTa-v3-large）有明确说明。代码承诺开源。唯一扣分：CED scoring 需要特定 NLI model 的 prompt 格式细节 |
| Confidence | 4/5 | Quite sure. 论文的核心领域（DocRE、LLM fine-tuning、RL alignment）在我的专业范围内，统计方法论的问题是明确可判断的 |

### 最终判断

本文的分析视角（evidence 不是 free lunch，优化范式决定 decoupling 程度）对 LLM-based IE 社区有实质价值。但三个核心贡献中：
1. **Evidence tax**（扎实）——scale-dependent 的发现有 cross-family 验证支撑
2. **Decoupling spectrum + EDCR**（中等）——概念好但 EDCR 的统计验证有结构性缺陷
3. **Variance compression**（薄弱）——n=3 的统计基础无法支撑量化声明

如果 W1（variance claim 的统计基础）和 W2（EDCR shared-component）能得到实质性回应（如增加 seeds、提供 partial correlation），可上调至 4.0（Conference）。目前判断为 3.5（Borderline Conference），主要因为统计方法论的不足削弱了本应很强的 empirical story。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 168 · 2026-05-23T00:57:58.264447+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），主要关切集中在 n=3 方差声明的统计基础、EDCR shared-component 问题、CED contrastive formulation 增量价值不足。

等待 Reviewer 2 审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 169 · 2026-05-23T00:58:04.103474+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心判断：

- **Overall 3.5（Borderline Conference）**
- 2 个 CRITICAL 问题：n=3 的方差压缩声明统计基础不足（W1）；EDCR 指标存在 shared-component 机械性负相关（W2）
- 3 个 MAJOR 问题：CED contrastive 增量仅 0.02pp（W3）；DPO 3-epoch 用不同 evaluation protocol 影响 spectrum 可比性（W4）；SFT vs RSFT variance 测量不同来源（W5）
- 如果 W1+W2 能实质性回应（增加 seeds、提供 partial correlation），可上调至 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 170 · 2026-05-23T00:58:13.608440+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 13

## Round 13

6 recorded events


### User

_source line 171 · 2026-05-23T01:01:30.997564+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 完整性）

**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction
**Venue**: EMNLP 2026 (ARR)

---

### Summary（2-3句）

本文研究 LLM-based DocRE 中证据生成的代价（"evidence tax"），比较 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3 (1.7B/4B/8B/14B) 和 LLaMA-3.1-8B 上的表现。主要发现：evidence tax 是规模依赖的（1.7B 时证据有益，4B 近似中性），GRPO 导致灾难性抽取-证据解耦而 RSFT 通过离散选择避免解耦，RSFT 将训练方差压缩 4.6–31 倍。论文提出 CED（基于 NLI 的证据评分函数）和 EDCR（Evidence-Decoupling Ratio）作为分析工具。

---

### Strengths（逐条）

**S1. 系统性的多因子实验设计。** 三种优化范式 × 四个 Qwen3 规模 + 一个 cross-family 验证（LLaMA-3.1-8B） × 两个数据集（DocRED + Re-DocRED），coverage 在 LLM-based DocRE 工作中属上乘。controlled evaluation subset（Appendix D）和 matched@2048 协议的设计体现了对实验混淆因素的认真处理。

**S2. CED 评分函数设计合理。** 通过 NLI 模型构建 contrastive premises（Section 3.4），区分"证据确实支持关系"和"仅实体共现"。contrastive formulation 的消融（Appendix B）确认了设计必要性——flat-NLI baseline 虽可产生 comparable RSFT 结果，但 contrastive formulation 在 per-triple discrimination 上更优。

**S3. RSFT 方差压缩具有实际价值。** 4B 训练方差从 3.80pp（SFT）降至 0.51pp（RSFT CED），对需要可重复部署的场景有直接意义。1.7B RSFT（51.19 Ign-F1, std 0.09pp）超过 8B SFT（50.19, std 3.22pp），Cohen's d=2.58，为小模型+质量过滤的部署策略提供了有力经验依据。

**S4. 分析层次丰富。** per-relation EDCR 分析（Figure 4，93 个关系类型的分布）、训练动态可视化（Figure 3，GRPO 崩溃轨迹）、定性案例分析（Section M，三类 EDCR 诊断案例）从统计、过程、实例三层支持核心论点。Table 14 的 evidence citation comparison 尤其有说服力。

**S5. 写作质量高。** "evidence tax" 概念定义清晰并贯穿全文，decoupling spectrum 的叙事框架使三种方法的对比一目了然。Abstract 中给出的关键数字均可在正文中追溯。

---

### Weaknesses（逐条）

**W1 [CRITICAL] 方法论原创性不足——三个贡献均为经验观察**

论文的三个 claim 逐一审视：
- **C1**（evidence tax 规模依赖）：对 4 个规模点的实验观察，不是方法创新。
- **C2**（decoupling spectrum）：GRPO/DPO/RSFT 表现不同本质上反映了 gradient-based optimization vs. selection-based filtering 的已知根本差异——前者可 exploit multi-objective reward landscape，后者天然避免这一问题。EDCR 是两个 recall 的简单比值（公式 2），定义本身缺乏技术深度。
- **C3**（RSFT 方差压缩）：RSFT 论文明确承认是 "well-established"（Section 3.3），应用于 DocRE + CED scoring 的组合虽然有效，但方法贡献有限。

CED 基于现有 NLI 模型（DeBERTa-v3-large），EDCR 是两个 recall 的比值。这些分析工具有用，但作为独立贡献偏弱。整体定位更接近 **empirical study with analytical tools**。对 EMNLP main conference 而言，需要更强的方法创新性。

**W2 [MAJOR] Scaling claim 的数据基础偏弱**

"Scale-dependent evidence tax" 作为第一贡献，在 Qwen3 家族内仅有 4 个规模点（1.7B, 4B, 8B, 14B——其中 14B 仅为 validation），cross-family 仅 1 个点（LLaMA-3.1-8B）。4 个点不足以可靠区分线性、对数、阶梯等 scaling pattern。

更重要的是，不同规模的数据呈现非单调性：1.7B RSFT（51.19 Ign-F1）超过 4B RSFT（44.82, Table 1），甚至超过 8B SFT（50.19）。论文在 Section 4.4 和 Appendix D 讨论了 truncation rate 差异和 matched@2048 协议，但主文中不同规模的数字是否全部来自同一 evaluation protocol 不够清晰——读者需要翻阅 Appendix 才能理解数字间的关系。建议在 Table 1 旁或 Section 4 开头明确列出所有规模在同一协议下的对比表。

**W3 [MAJOR] GRPO 崩溃分析缺乏机制深度**

Section 4.3 对 GRPO QLoRA catastrophic collapse 的分析停留在现象描述层面（"extraction collapses to Rel-F1 1.41, Evi-F1 rises to 85.04"），未提供机制解释。这本质上是 multi-objective reward hacking 的一个实例——optimizer 发现牺牲 extraction accuracy 可以最大化 evidence-weighted reward。论文未：
1. 连接到 reward hacking 文献（如 Weng 2024 综述; Fu et al. 2025 的 reward shaping 原则）
2. 探讨简单缓解策略（reward clipping, 不同 KL 系数如 0.1/0.5, reward normalization）是否能避免 collapse
3. 分析 full-precision GRPO 也部分避免 collapse 是否仅因为梯度精度差异

如果 GRPO collapse 仅在 β=0.01 的 QLoRA 设置下发生，这更像是超参数/精度问题而非方法本质差异，"decoupling spectrum" 的框架就不够稳固。

**W4 [MINOR] Related Work 存在遗漏**

以下近期相关工作未被引用或讨论：
1. **LMRC**（Li & Zhang, 2024; arXiv 2408.13889）——LLM with Relation Classifier for DocRE，针对 LLM 注意力分散问题，在 LLM-based DocRE 中表现突出，应在 Section 2 LLM-based DocRE 部分讨论。
2. **RelPrior**（Huang et al., 2025; arXiv 2511.08143）——"Relation as a Prior" 范式，claim 超越现有 LLM-based DocRE 方法。
3. **SummaC**（Laban et al., 2022, TACL）——NLI-based faithfulness evaluation 的先驱工作，CED 的设计理念（sentence-level NLI scoring 用于 faithfulness 判断）与之直接相关，应在 Section 3.4 讨论设计动机时引用。
4. **Rationale Verification for RE**（Li et al., 2024; AAAI 2025, arXiv 2412.07289）——使用 rationale supervisor 验证 LLM 的 RE 推理，与本文的 evidence verification 主题高度相关。

**W5 [MINOR] CED 对外部 NLI 模型的 sensitivity analysis 不足**

CED 评分完全取决于 NLI 模型能力。论文仅在 Appendix B 比较了 DeBERTa-v3-large vs. v3-base（差异"可忽略"），但：
- 未测试其他 NLI 模型家族（如生成式 NLI 模型）
- 未分析 NLI 模型在 DocRE 领域的 out-of-distribution 行为——DocRE 中的证据句往往包含多个实体和复杂共指，与标准 NLI 训练分布差异较大
- 若 NLI 模型对某些 relation type 存在系统性偏差，EDCR 诊断可能产生误导性结论

**W6 [MINOR] Limitations section 遗漏了若干重要限制**

Limitations（Section 7）覆盖面尚可但遗漏：
- DocRED 的证据标注已知不完整（Re-DocRED 论文已指出），这对 CED/EDCR 基于 gold evidence 的计算可靠性有直接影响
- 三种方法的计算成本差异未提及——GRPO 需要 G 个 candidate generation + value estimation，DPO 需要 preference pair 构建，RSFT 需要 N=5 采样 + CED scoring，公平对比应包含 cost analysis
- 仅评估 DocRE 一种 IE 任务，findings 是否 generalize 到 NER、事件抽取等未讨论

---

### Questions（需要作者澄清的）

**Q1.** Abstract 中 1.7B RSFT 的 51.19 Ign-F1 与 Table 1 中 4B RSFT CED 的 44.82 使用的是同一 evaluation protocol 吗？如果不同（如 matched@2048 vs. standard dev-set），请在主文中明确标注每个数字的 evaluation protocol，避免读者跨表对比时产生困惑。

**Q2.** GRPO collapse 是否在其他 KL 系数（如 0.1, 0.5）或不使用 QLoRA（full-precision）时依然发生？Section 4.3 提到 full-precision GRPO "avoids extreme decoupling"（EDCR 0.6797），那么 QLoRA 的量化精度损失是否是 collapse 的主要原因而非 GRPO 方法本身？

**Q3.** EDCR 与 Rel-F1 的负相关（ρ=−0.93, Section 5）是在仅 7 个 method configurations 上计算的。n=7 的 Spearman 相关有较大的 sampling variability——bootstrap 95% CI 是多少？是否在不同 seed 下稳定？

**Q4.** CED contrastive premise 中收集的 "entity-sharing negatives"（Section 3.4）是否包含了实际成立但未被标注的关系（即 DocRED 的 false negatives）？Re-DocRED 标注密度是 DocRED 的 2.82×，这意味着 DocRED 上大量 "negative" 其实是 false negative，会如何影响 CED score 的可靠性？

**Q5.** RSFT 的 N=5 candidates 是如何选择的？如果增加到 N=50 或 100（更接近 best-of-N scaling），解耦行为是否会改变？论文对 RSFT "avoids decoupling" 的机制解释（Section F, "discrete selection"）在 N→∞ 的极限下是否依然成立？

**Q6.** Table 12 的 encoder-based comparison 显示 TP-only Evi-F1 超过 80%，但 joint Evi-F1 仅 54.15。论文 claim "when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods"——但 joint evaluation 的巨大 gap（54.15 vs. encoder 的更高值）说明 LLM 方法的主要瓶颈不在 evidence quality 而在 extraction precision。这是否削弱了论文对 "evidence-grounded extraction" 实用性的 claim？

---

### Missing References

1. Li, X., & Zhang, M. (2024). LLM with Relation Classifier for Document-Level Relation Extraction. arXiv:2408.13889. — 重要的 LLM-based DocRE baseline
2. Huang, N., et al. (2025). Relation as a Prior for LLM-based Document-level Relation Extraction. arXiv:2511.08143. — 最新 LLM-based DocRE 范式
3. Laban, P., et al. (2022). SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization. TACL. — CED 设计理念的先驱
4. Li, Y., et al. (2025). Enhancing Relation Extraction via Supervised Rationale Verification and Feedback. AAAI 2025. — RE 中的 rationale verification
5. Reward hacking 相关文献（如 Weng 2024 综述）——GRPO collapse 分析的理论背景

---

### Overall Assessment

## 总体评分
**Overall**: 3.0（Findings — 可被 Findings 接收）
**一句话总结**: 设计良好的 empirical study，实验覆盖面和分析深度出色，但三个核心贡献均为经验观察，缺乏足以进入 main conference 的方法创新性。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计扎实，controlled evaluation 和多 seed 验证体现严谨性；但 scaling claim 基于有限数据点，GRPO collapse 的机制分析不足，不同规模数字的 evaluation protocol 对应关系不够清晰 |
| Excitement | 2.5/5 | Evidence tax 概念有趣，RSFT 方差压缩对实践有价值；但方法组件（CED/EDCR/RSFT 应用）各自偏简单，无显著方法创新，核心 insight（selection-based > gradient-based for multi-objective）在 RL 社区不算新颖 |
| Reproducibility | 4/5 | 超参数详细列出（Appendix A），声明将 release code and outputs，多 seed 实验设计好；但 CED 依赖特定 NLI 模型版本，未提供 CED scoring 的独立复现指南 |
| Overall | 3.0/5 | Findings 水平——经验发现有社区参考价值，但缺乏 main conference 所需的方法创新深度 |

**置信度**: 4/5 — 对 DocRE 和 LLM post-training 方法较为熟悉

**理由**: 本文是一项覆盖面广、分析深入的 empirical study。Evidence tax 的规模依赖性发现和 RSFT 方差压缩的实践价值是真实的贡献。但论文的定位困境在于：三个核心贡献均为经验观察（不是方法创新），分析工具（CED = NLI scoring, EDCR = recall ratio）定义简单，RSFT 本身不是新方法。"Decoupling spectrum" 框架虽然叙事有力，但深层机制（为什么 gradient methods 解耦、selection methods 不解耦）在 multi-objective optimization 文献中已有大量讨论（reward hacking, Goodhart's Law），本文未充分连接。

建议以 Findings 接收，但需要以下修改：
1. **弱化 scaling claim 表述**或增加更多规模点/模型家族——当前 4 个 Qwen3 点 + 1 个 LLaMA 点不足以 claim "scale-dependent" 作为一个 general 结论
2. **深化 GRPO collapse 的机制分析**——连接 reward hacking 文献，测试不同 KL 系数/精度，区分"方法问题"和"超参数问题"
3. **主文中统一 evaluation protocol 的展示**——当前不同规模的数字散布在主文、appendix、不同 evaluation 设置中，读者追溯困难
4. **补充 missing references**（至少 LMRC 和 SummaC）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-23T01:02:20.675679+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### Summary\n本文将 evidence-grounded DocRE 形式化为结构化生成任务，系统比较了三种 post-SFT 优化范式（GRPO、DPO、RSFT）在 evidence 生成与 relation extraction 之间的 trade-off。核心发现包括：(1) evidence tax 是 scale-dependent 的（1.7B 有益、4B+ 中性）；(2) 梯度优化方法导致 extraction-evidence decoupling，离散选择方法（RSFT）可避免；(3) RSFT 通过 CED-based 样本选择压缩训练方差。论文覆盖面广（1.7B-14B，Qwen3/LLaMA 两个 model family），分析视角有启发性，但多处统计推断基础薄弱。\n\n### Strengths\nS1. 问题定位精准且实用——evidence grounding 是 LLM-based IE 部署的真实痛点。\nS2. Decoupling spectrum 概念有分析价值——从优化机制角度解释不同范式表现差异。\nS3. 跨尺度+跨 model family 的实验覆盖（1.7B-14B Qwen3 + LLaMA-3.1-8B + Re-DocRED）。\nS4. 对自身局限的透明度——主动承认 EDCR 缺乏 human judgment 验证、variance 基于 3 seeds 等。\nS5. 定性分析具体有用——三个 case study 展示了 EDCR 的诊断价值。\n\n### Weaknesses\nW1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础。置信区间极宽（σ 的 95% CI 约 [0.52s, 6.29s]），Cohen's d=2.58 的标准误约 1.2-1.5。声称\"31× compression\"在统计上无法从 n=3 可靠估计。建议增加到 5-10 seeds 或降级为 observation。\n\nW2 [CRITICAL] — EDCR 的 shared-component 问题使 cross-method 相关性不可靠。EDCR = (TP_evi × G) / TP²，TP 同时出现在分子和分母，构造机械性负相关。n=7 极小，GRPO QLoRA 极端点可能主导相关性。建议移除极端点后重算、用 partial correlation 控制 TP。\n\nW3 [MAJOR] — CED contrastive formulation 增量价值不足。CED vs flat-NLI 的 Rel-F1 差仅 0.02pp，在 noise level 以内。减法操作缺乏理论动机。论文自己承认 contrastive \"not essential\"。\n\nW4 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol 影响 decoupling spectrum 可比性。Footnote 1 提到\"earlier evaluation protocol\"但未充分说明差异。\n\nW5 [MAJOR] — SFT vs RSFT variance 测量来源不同（full training vs fixed-base fine-tuning），RSFT variance 天然更小，直接比较不公平。\n\nW6 [MAJOR] — Dev→Test 20pp drop 解释不够充分，14B RSFT test 上低于 SFT 0.37pp。\n\nW7 [MINOR] — 与 encoder baseline 的比较选择性呈现指标（强调 TP-only Evi-F1 >80%，淡化 Ign-F1 差距 16-18pp）。\n\nW8 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比。\n\nW9 [MINOR] — 4B retrained checkpoint 的 dev 差距 0.35pp 可能影响 evidence tax 分析。\n\n### Overall: 3.5（Borderline Conference）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### Summary\n本文将 evidence-grounded DocRE 形式化为结构化生成任务，系统比较了三种 post-SFT 优化范式（GRPO、DPO、RSFT）在 evidence 生成与 relation extraction 之间的 trade-off。核心发现包括：(1) evidence tax 是 scale-dependent 的（1.7B 有益、4B+ 中性）；(2) 梯度优化方法导致 extraction-evidence decoupling，离散选择方法（RSFT）可避免；(3) RSFT 通过 CED-based 样本选择压缩训练方差。论文覆盖面广（1.7B-14B，Qwen3/LLaMA 两个 model family），分析视角有启发性，但多处统计推断基础薄弱。\n\n### Strengths\nS1. 问题定位精准且实用——evidence grounding 是 LLM-based IE 部署的真实痛点。\nS2. Decoupling spectrum 概念有分析价值——从优化机制角度解释不同范式表现差异。\nS3. 跨尺度+跨 model family 的实验覆盖（1.7B-14B Qwen3 + LLaMA-3.1-8B + Re-DocRED）。\nS4. 对自身局限的透明度——主动承认 EDCR 缺乏 human judgment 验证、variance 基于 3 seeds 等。\nS5. 定性分析具体有用——三个 case study 展示了 EDCR 的诊断价值。\n\n### Weaknesses\nW1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础。置信区间极宽（σ 的 95% CI 约 [0.52s, 6.29s]），Cohen's d=2.58 的标准误约 1.2-1.5。声称\"31× compression\"在统计上无法从 n=3 可靠估计。建议增加到 5-10 seeds 或降级为 observation。\n\nW2 [CRITICAL] — EDCR 的 shared-component 问题使 cross-method 相关性不可靠。EDCR = (TP_evi × G) / TP²，TP 同时出现在分子和分母，构造机械性负相关。n=7 极小，GRPO QLoRA 极端点可能主导相关性。建议移除极端点后重算、用 partial correlation 控制 TP。\n\nW3 [MAJOR] — CED contrastive formulation 增量价值不足。CED vs flat-NLI 的 Rel-F1 差仅 0.02pp，在 noise level 以内。减法操作缺乏理论动机。论文自己承认 contrastive \"not essential\"。\n\nW4 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol 影响 decoupling spectrum 可比性。Footnote 1 提到\"earlier evaluation protocol\"但未充分说明差异。\n\nW5 [MAJOR] — SFT vs RSFT variance 测量来源不同（full training vs fixed-base fine-tuning），RSFT variance 天然更小，直接比较不公平。\n\nW6 [MAJOR] — Dev→Test 20pp drop 解释不够充分，14B RSFT test 上低于 SFT 0.37pp。\n\nW7 [MINOR] — 与 encoder baseline 的比较选择性呈现指标（强调 TP-only Evi-F1 >80%，淡化 Ign-F1 差距 16-18pp）。\n\nW8 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比。\n\nW9 [MINOR] — 4B retrained checkpoint 的 dev 差距 0.35pp 可能影响 evidence tax 分析。\n\n### Overall: 3.5（Borderline Conference）"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-23T01:02:52.647350+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31971
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-23T01:02:52.799065+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性）\n\n### Summary\n本文研究 LLM-based DocRE 中证据生成的代价（\"evidence tax\"），比较 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3 (1.7B/4B/8B/14B) 和 LLaMA-3.1-8B 上的表现。主要发现：evidence tax 是规模依赖的（1.7B 时证据有益，4B 近似中性），GRPO 导致灾难性抽取-证据解耦而 RSFT 通过离散选择避免解耦，RSFT 将训练方差压缩 4.6–31 倍。论文提出 CED 和 EDCR 作为分析工具。\n\n### Strengths\nS1. 系统性多因子实验设计——三种范式 × 四个规模 + cross-family + 两个数据集。\nS2. CED 评分函数设计合理——contrastive formulation 区分\"证据支持关系\"和\"仅实体共现\"。\nS3. RSFT 方差压缩具有实际价值——1.7B RSFT 超过 8B SFT，Cohen's d=2.58。\nS4. 分析层次丰富——per-relation EDCR、训练动态可视化、定性案例分析。\nS5. 写作质量高——\"evidence tax\" 概念清晰，decoupling spectrum 叙事框架清晰。\n\n### Weaknesses\nW1 [CRITICAL] — 方法论原创性不足。三个贡献均为经验观察：C1 是实验观察不是方法创新；C2（decoupling spectrum）反映 gradient-based vs selection-based 的已知差异，EDCR 定义简单；C3（RSFT）论文自己承认是 \"well-established\"。整体定位更接近 empirical study with analytical tools，对 EMNLP main conference 需要更强方法创新性。\n\nW2 [MAJOR] — Scaling claim 数据基础偏弱。仅 4 个 Qwen3 规模点 + 1 个 LLaMA 点，不足以可靠区分 scaling pattern。不同规模数字是否来自同一 evaluation protocol 不够清晰。\n\nW3 [MAJOR] — GRPO 崩溃分析缺乏机制深度。停留在现象描述，未连接 reward hacking 文献，未探讨缓解策略（不同 KL 系数、reward normalization），未分析 full-precision 避免 collapse 是否仅因精度差异。如果 collapse 仅在 QLoRA 设置下发生，\"decoupling spectrum\" 框架不够稳固。\n\nW4 [MINOR] — Related Work 遗漏：LMRC (Li & Zhang, 2024)、RelPrior (Huang et al., 2025)、SummaC (Laban et al., 2022)、Rationale Verification for RE (Li et al., 2025)。\n\nW5 [MINOR] — CED 对外部 NLI 模型的 sensitivity analysis 不足——未测试其他 NLI 模型家族，未分析 DocRE 领域的 OOD 行为。\n\nW6 [MINOR] — Limitations 遗漏：DocRED 证据标注不完整对 CED/EDCR 的影响、三种方法的计算成本差异、仅评估 DocRE 一种 IE 任务。\n\n### Overall: 3.0（Findings）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性）\n\n### Summary\n本文研究 LLM-based DocRE 中证据生成的代价（\"evidence tax\"），比较 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3 (1.7B/4B/8B/14B) 和 LLaMA-3.1-8B 上的表现。主要发现：evidence tax 是规模依赖的（1.7B 时证据有益，4B 近似中性），GRPO 导致灾难性抽取-证据解耦而 RSFT 通过离散选择避免解耦，RSFT 将训练方差压缩 4.6–31 倍。论文提出 CED 和 EDCR 作为分析工具。\n\n### Strengths\nS1. 系统性多因子实验设计——三种范式 × 四个规模 + cross-family + 两个数据集。\nS2. CED 评分函数设计合理——contrastive formulation 区分\"证据支持关系\"和\"仅实体共现\"。\nS3. RSFT 方差压缩具有实际价值——1.7B RSFT 超过 8B SFT，Cohen's d=2.58。\nS4. 分析层次丰富——per-relation EDCR、训练动态可视化、定性案例分析。\nS5. 写作质量高——\"evidence tax\" 概念清晰，decoupling spectrum 叙事框架清晰。\n\n### Weaknesses\nW1 [CRITICAL] — 方法论原创性不足。三个贡献均为经验观察：C1 是实验观察不是方法创新；C2（decoupling spectrum）反映 gradient-based vs selection-based 的已知差异，EDCR 定义简单；C3（RSFT）论文自己承认是 \"well-established\"。整体定位更接近 empirical study with analytical tools，对 EMNLP main conference 需要更强方法创新性。\n\nW2 [MAJOR] — Scaling claim 数据基础偏弱。仅 4 个 Qwen3 规模点 + 1 个 LLaMA 点，不足以可靠区分 scaling pattern。不同规模数字是否来自同一 evaluation protocol 不够清晰。\n\nW3 [MAJOR] — GRPO 崩溃分析缺乏机制深度。停留在现象描述，未连接 reward hacking 文献，未探讨缓解策略（不同 KL 系数、reward normalization），未分析 full-precision 避免 collapse 是否仅因精度差异。如果 collapse 仅在 QLoRA 设置下发生，\"decoupling spectrum\" 框架不够稳固。\n\nW4 [MINOR] — Related Work 遗漏：LMRC (Li & Zhang, 2024)、RelPrior (Huang et al., 2025)、SummaC (Laban et al., 2022)、Rationale Verification for RE (Li et al., 2025)。\n\nW5 [MINOR] — CED 对外部 NLI 模型的 sensitivity analysis 不足——未测试其他 NLI 模型家族，未分析 DocRE 领域的 OOD 行为。\n\nW6 [MINOR] — Limitations 遗漏：DocRED 证据标注不完整对 CED/EDCR 的影响、三种方法的计算成本差异、仅评估 DocRE 一种 IE 任务。\n\n### Overall: 3.0（Findings）"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-23T01:02:54.211102+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Assistant

_source line 176 · 2026-05-23T01:02:57.619445+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 177 · 2026-05-23T01:03:00.176030+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0（Findings）**。

主要发现：
- **方法原创性不足**是最关键问题——CED/EDCR/RSFT 应用三个组件各自偏简单，三个贡献均为经验观察
- **Scaling claim 数据基础偏弱**——仅 4 个 Qwen3 规模点 + 1 个 cross-family 点
- **GRPO collapse 分析停留在现象层面**，未连接 reward hacking 文献，未区分"方法本质"与"超参数/精度问题"
- 实验设计和分析深度是论文的强项，RSFT 方差压缩（4.6–31×）和 1.7B 超过 8B SFT 的发现具有实践价值
- Related work 遗漏 LMRC、RelPrior、SummaC 等相关工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 178 · 2026-05-23T01:03:05.921875+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 179 · 2026-05-23T01:04:34.196048+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

---

### Strengths 回应

**[AGREE] R1-S1**: 问题定位精准。Evidence grounding 确实是 LLM-based IE 部署的真实痛点，论文 Introduction 中 "accurate extractors have no evidence, evidence-capable methods are not competitive" 的 gap 叙事准确。我在自己的审稿中也认可这一点（我的 S1）。

**[AGREE] R1-S2**: Decoupling spectrum 作为分析框架有价值。补充一点：我认为这个框架虽然叙事有力，但机制解释不够深入——gradient-based 方法 exploit multi-objective reward landscape 导致解耦，这在 RL/reward hacking 文献中已有大量讨论，论文未充分连接（我的 W3/CRITICAL 中已指出）。

**[AGREE] R1-S3**: 跨尺度+跨 model family 覆盖在同类工作中确实属上乘。但我对 scaling claim 的数据基础有保留——4 个 Qwen3 点 + 1 个 LLaMA 点是否足以 claim "scale-dependent" 作为 general 结论（我的 W2/MAJOR）。

**[AGREE] R1-S4**: 透明度确实值得肯定。Section 7 (Limitations) 主动承认了 EDCR 缺 human validation、variance 基于少量 seeds、CED 依赖外部 NLI 模型等，这在论文写作中是好的实践。

**[AGREE] R1-S5**: Section M 的三个 case study（date_of_birth EDCR 0.119, head_of_government 0.956, notable_work 0.613）确实展示了 EDCR 作为 per-relation diagnostic 的实际价值，是论文分析中的亮点。

---

### Weaknesses 回应

**[AGREE] R1-W1 (n=3 seeds 统计基础)**: 这是我自己审稿中未充分强调的重要问题。n=3 的方差估计确实统计基础薄弱：
- χ² 分布下，σ 的 95% CI 约 [0.52s, 6.29s]（R1 的估计正确）
- "31× compression" 这个具体倍数在 n=3 下不可靠——真实压缩率可能在 5×-100× 之间
- Cohen's d=2.58 的标准误约 1.2-1.5（R1 正确），CI 极宽

论文在 Abstract 中高度强调此结果（"compresses training variance 4.6-31×"），但统计基础不匹配这一强调程度。建议：要么增加 seeds 到 5-10 个，要么将 claim 降级为定性观察（"RSFT substantially reduces variance"），不给出具体倍数。

**[AGREE] R1-W2 (EDCR shared-component 问题)**: R1 的数学分析精确。EDCR = (TP_evi × G) / TP²，TP 同时出现在分子和分母，确实构造了与 Rel-F1（也是 TP 的函数）的机械性负相关。

进一步补充：
- n=7 configurations 中，GRPO QLoRA（Rel-F1 ≈ 1.41, EDCR 0.9876）是一个极端 outlier。移除此点后，remaining 6 个 configurations 的 ρ 可能大幅变化
- 论文 claim "EDCR validates EDCR's diagnostic utility"（Section 5），但如果相关性主要由 mechanical construction + outlier 驱动，这个 validation 就不成立

R1 建议的 partial correlation（控制 TP）和 remove-outlier sensitivity analysis 是恰当的修复方案。

**[AGREE] R1-W3 (CED contrastive 增量价值)**: Appendix B 的数据确实显示 CED vs flat-NLI 的 Rel-F1 差仅 0.02pp，论文自己也承认 contrastive formulation "not essential for data selection quality"。我在自己的审稿中也指出 CED 作为独立贡献偏弱（我的 W1/CRITICAL）。

补充：论文的辩护角度是 CED 在 "per-triple discrimination scores" 上更优——但如果这个优势不能传导到下游 RSFT 性能，其实际价值存疑。

**[AGREE] R1-W4 (DPO 3-epoch evaluation protocol 差异)**: Footnote 1 提到 DPO 3-epoch 使用 "earlier evaluation protocol" 但未详细说明差异，这确实影响 decoupling spectrum 的可比性。如果 DPO 5-epoch 和 DPO 3-epoch 在不同 protocol 下评估，Table 2 的 severity 排序可能不完全可靠。建议作者在 revision 中统一所有 configurations 的 evaluation protocol 或明确标注差异。

**[AGREE] R1-W5 (SFT vs RSFT variance 来源不同)**: 这是一个精细但重要的统计观点：
- SFT variance = 随机初始化 + 训练随机性 + 数据顺序
- RSFT variance = 固定 SFT base 上的 RSFT 训练随机性

这两者测量不同层面的变异性。RSFT 起点固定，天然 variance 更小。"31× compression" 可能更多反映了固定起点的效果，而非 RSFT 方法本身的优势。

不过，从实践部署角度看：如果用户的 workflow 是 "train SFT → apply RSFT"，那么 RSFT 步骤引入的额外方差确实很小。论文的实践 claim（RSFT 使部署更可预测）仍然成立，但应更精确地描述方差来源。

**[REBUT] R1-W6 (Dev→Test 20pp drop)**: 这个 weakness 的严重性我认为 R1 略有高估。

论文在 Section 4.4（page 7）和 Section 7（Limitations）中已经给出了合理解释：Re-DocRED 标注密度是 DocRED 的 2.82×（更多 gold triples per document），exact-match evaluation 对 generative model 的 surface-form 差异更为敏感。更重要的是，**method ranking 在 test set 上完全保持**（Spearman ρ=1.0, Section 7），说明 absolute performance drop 不影响 relative comparison 的有效性。

但 R1 指出的 "14B RSFT test 上低于 SFT 0.37pp" 值得关注。从 Table 9（page 14）可以看到，这个反转虽然幅度小（0.37pp），但如果 RSFT 的 advantage 在更大规模上消失，这对论文的 scaling narrative 是一个隐患。建议作者在 revision 中分析 14B 反转是否在统计意义上显著。

**[AGREE] R1-W7 (Encoder baseline 选择性呈现)**: Table 12（page 15）确实选择性地强调了 LLM 方法的优势指标（TP-only Evi-F1 > 80%）而淡化了 Ign-F1 gap（16-18pp）。论文的辩护（"closing this gap requires improving extraction precision"）是合理的方向性说明，但不改变当前 LLM 方法在 absolute performance 上的劣势。建议在 Discussion 中更 balanced 地呈现。

**[AGREE] R1-W8 (缺少 LLM-based RE 直接对比)**: 与我的 W4 一致。论文未引用或对比 LMRC（Li & Zhang, 2024）、RelPrior（Huang et al., 2025）等近期 LLM-based DocRE 方法。虽然这些方法不一定做 evidence extraction，但 extraction performance 的对比对 situating 论文贡献至关重要。

**[AGREE] R1-W9 (4B retrained checkpoint 差距)**: Minor issue，0.35pp 差距在 SFT 3.80pp std 的噪声范围内，不太可能实质影响 evidence tax 分析。同意这是 minor。

---

### 综合评价

R1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于我对 **方法论原创性** 的评价更低（我的 W1/CRITICAL）：论文的三个贡献均为经验观察，方法组件（CED、EDCR、RSFT 应用）各自偏简单。R1 的审稿更侧重实验设计和统计严谨性，在这些方面发现了我未充分强调的重要问题（特别是 W1 的 n=3 统计基础和 W5 的方差来源差异）。

综合两份审稿，我认为：
- **论文质量下限**：实验覆盖面和分析深度确实在同类工作中属上乘（双方一致认可）
- **论文质量上限受限于**：(1) 方法原创性不足（我的 W1）；(2) 关键统计声明基础薄弱（R1 的 W1/W2）；(3) GRPO collapse 机制分析不足（我的 W3）
- **建议定位**：3.0-3.5 之间，Findings 接收是合理的；进入 main conference 需要显著加强方法创新或统计严谨性

R1 的 W1（n=3 seeds）和 W2（EDCR shared-component）是我认为最需要作者在 revision 中 address 的问题，因为这些直接影响论文核心 claim 的可信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 180 · 2026-05-23T01:04:39.749793+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 181 · 2026-05-23T01:04:46.412349+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

对 R1 的 9 个 Weaknesses 中，我 AGREE 了 8 条，REBUT 了 1 条（W6 Dev→Test drop 严重性被高估——method ranking 完全保持，Spearman ρ=1.0）。R1 提出的 n=3 统计基础（W1）和 EDCR shared-component 问题（W2）是我自己审稿中未充分强调的重要问题，已在交叉回应中补充认可。综合两份审稿，建议 3.0-3.5 区间，Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 182 · 2026-05-23T01:04:51.937325+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 17

## Round 17

12 recorded events


### User

_source line 183 · 2026-05-23T01:05:40.870205+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths 回应

**[AGREE] R2-S1: 系统性多因子实验设计。**
同意。三种范式 × 四个规模 + cross-family + 两个数据集的覆盖面在同类工作中较好。我在自己的审稿中也将此列为优势（R1-S3）。

**[REBUT] R2-S2: CED 评分函数设计合理。**
部分不同意。CED 的 contrastive 动机（区分真 evidence vs 仅 entity co-occurrence）在**概念**上合理，但 Appendix B 的消融结果（Table 5）显示 CED vs flat-NLI（仅用正向 p⁺）的 Rel-F1 差异仅 0.02pp（45.63 vs 45.61），在 3-seed noise level（std ≈ 0.09pp）之内。论文自己在 Section 3.4 末段承认 "the contrastive formulation is not essential for data selection quality"。因此 R2 将 CED 的 contrastive formulation 列为 strength 过于宽松——这更接近一个**未被验证有实质增量的设计选择**。

**[REBUT] R2-S3: RSFT 方差压缩具有实际价值。**
强烈不同意将 Cohen's d=2.58 列为优势。这正是我 R1-W1 标注为 [CRITICAL] 的问题：

- n=3 时方差估计的 95% CI 为 [0.52s, 6.29s]（基于 χ²(2) 分布），"4.6–31× compression" 和 d=2.58 在统计上不可靠
- SFT 和 RSFT 测量的是不同来源的方差（R1-W5），直接比较不公平
- "1.7B RSFT 超过 8B SFT" 这个 claim 有实际价值，但不应用 effect size 包装——直接报告均值差和 CI 更诚实

R2 在自己的 Weakness 中未对此提出任何质疑，这是其审稿的一个盲区。

**[AGREE] R2-S4: 分析层次丰富。**
同意。Per-relation EDCR（Figure 4）、训练动态（Figure 3）和 qualitative analysis（Section M）从不同角度展示了 decoupling 现象。我在 R1-S5 也肯定了这一点。

**[AGREE] R2-S5: 写作质量高。**
同意。"Evidence tax" 概念和 decoupling spectrum 叙事框架确实清晰易懂，帮助读者快速抓住核心 message。

---

### Weaknesses 回应

**[REBUT] R2-W1: 方法论原创性不足。**
部分不同意。R2 的判断——"三个贡献均为经验观察"——有道理但过于笼统。需区分：

1. **C1（Evidence tax）**：确实是 empirical observation，但 scale-dependent evidence tax 是一个有实际部署价值的发现，cross-family validation（LLaMA-3.1-8B，Appendix H-I）增强了其可信度。好的 empirical finding 在 EMNLP 有先例。
2. **C2（Decoupling spectrum + EDCR）**：R2 说 "反映 gradient-based vs selection-based 的已知差异"——但这过度简化了。GRPO bf16 G=4 和 G=8 都避免 catastrophic collapse 而 QLoRA 不行（Table 2），这说明 decoupling 不是简单的 gradient vs selection 二分法，而是受 precision、capacity 等因素调制。这一观察是新的。EDCR 定义虽简单，但简单不等于无价值——问题是其统计验证不充分（我的 R1-W2）。
3. **C3（RSFT）**：同意不是方法创新，论文也不应将其包装为创新。论文的贡献更准确地说是 RSFT **在 evidence-grounded DocRE 上的应用与分析**。

总体判断：这篇论文更接近"strong empirical study"而非"method paper"。对于 EMNLP，如果 empirical findings 足够扎实且有 community impact，3.5-4.0 是合理分数。**但前提是统计基础要牢固——这恰恰是论文的短板**（R1-W1, R1-W2）。R2 把原创性不足标为 [CRITICAL]，我认为应为 [MAJOR]——真正 critical 的是统计方法论的薄弱。

**[REBUT] R2-W2: Scaling claim 数据基础偏弱。**
部分不同意。

- 论文并未声称建立 scaling law（需要拟合幂律等参数模型），而是观察 scaling trend。4 个 Qwen3 点（1.7B/4B/8B/14B）+ LLaMA-3.1-8B 作为 cross-family validation，对于 trend observation 是合理的。
- R2 说 "不同规模数字是否来自同一 evaluation protocol 不够清晰"——论文在 Section 4.1 和 Appendix C 说明了 matched@2048 fair evaluation protocol（max_new_tokens=2048, format-compliant intersection），并明确标注 DPO 3-epoch 使用了 earlier protocol（Footnote 1）。这个信息是存在的，虽然可以更显眼。
- 真正的问题不是数据点数量，而是每个数据点只有 3 seeds，使得 scale 间的差异难以从噪声中区分（R1-W1）。

**[AGREE] R2-W3: GRPO 崩溃分析缺乏机制深度。**
同意这是一个实质性弱点，但补充两点：

1. **精度 vs group size 的隔离实际上已部分完成**：Table 2 包含 GRPO bf16 G=4 和 GRPO bf16 G=8 两行，两者均避免 catastrophic collapse，而 QLoRA G=4 collapse。这隔离了 precision 作为 collapse 的主要因素。R2 称 "未分析 full-precision 避免 collapse 是否仅因精度差异" 不完全准确——数据在 Table 2 中，但**论文的文字分析确实停留在现象层面**，未深入探讨为什么 4-bit quantization 特别容易导致 reward hacking（例如，量化损失是否使 policy 更容易找到 degenerate shortcuts）。
2. 同意缺乏 KL 系数消融和 reward normalization 测试。GRPO 的超参数空间很大（Table 4 显示仅测试了 G=4 和 G=8，β 值未报告消融），论文对此的 coverage 不足以支撑对 GRPO 的一般性结论。
3. 但 R2 的推论——"如果 collapse 仅在 QLoRA 下发生，decoupling spectrum 不够稳固"——过于绝对。Table 2 的 GRPO bf16 行显示 **mild decoupling**（EDCR 低于 SFT baseline），只是程度不到 catastrophe。Spectrum 中 GRPO 仍然比 RSFT 有更多 decoupling，只是 severity 被 precision 调制。

**[AGREE] R2-W4: Related Work 遗漏。**
部分同意。SummaC (Laban et al., 2022) 作为 NLI-based faithfulness metric 的先驱，与 CED 的设计逻辑直接相关，应当引用。LMRC (Li & Zhang, 2024) 如果涉及 LLM-based RE，也应对比。其余两篇（RelPrior, Rationale Verification）需确认具体相关性。

**[AGREE] R2-W5: CED 对外部 NLI 模型的 sensitivity analysis 不足。**
同意。CED 依赖 DeBERTa-v3-large 的 NLI 输出。论文仅在 Appendix B 测试了 v3-base（Table 5 脚注 "CED filtering is robust to NLI model capacity"），但：

- 仅测试了同一家族（DeBERTa）的两个大小，不算真正的 sensitivity analysis
- DocRED 的 evidence 是 Wikipedia 段落的句子级引用，与标准 NLI 训练数据（如 MNLI）有领域差异，OOD 行为未被分析
- 这对 CED 的实用性主张（Section 6 "CED as a domain-specific quality filter"）是一个实际威胁

**[AGREE] R2-W6: Limitations 遗漏。**
同意所有三点遗漏应在 Limitations 中讨论：

1. **DocRED 证据标注不完整**：已知 DocRED 的 evidence annotation 不完整（部分 triple 缺少标注或标注不全）。CED 计算负例时依赖 "not in the predicted evidence set" 的句子，如果 gold evidence 本身不完整，negative samples 可能包含实际为正的 evidence，影响 CED 分数的可靠性。
2. **计算成本差异**：Table 4 显示 RSFT 训练样本约 3000（1.7B），远少于 GRPO（3,053 documents × N=5 candidates = ~15K），但 RSFT 还需 SFT inference + NLI scoring 的前置成本，论文未报告端到端 wall-clock time 对比。
3. **仅 DocRE 一种 IE 任务**：evidence grounding 的 insight 是否迁移到 NER、EE 等其他 IE 任务未被讨论。

---

### 对 R2 Overall Assessment（3.0, Findings）的评价

R2 给 3.0 的主要依据是方法论原创性不足（R2-W1）。我认为这一判断方向正确但不是论文的最大问题——**统计方法论的薄弱**（n=3 variance claims、EDCR shared-component）才是更实质的 concern，而 R2 在这方面未做深入分析（甚至将 Cohen's d=2.58 列为 strength）。

我的评分 3.5（Borderline Conference），高于 R2 的 3.0，理由是：
- 论文的分析框架（evidence tax、decoupling spectrum）对社区有启发价值，即使不是严格的方法创新
- 跨尺度 + 跨 model family 的实验覆盖在同类工作中属上乘
- 但统计基础的问题阻止我给 4.0

如果作者能回应 R1-W1（增加 seeds 或降级 variance claim）和 R1-W2（EDCR shared-component 的 partial correlation 分析），我愿意上调至 4.0。R2 关注的原创性问题在 rebuttal 中较难根本解决，但如果统计基础加固，empirical study 的定位可以更有说服力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-23T01:06:02.889144+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-23T01:06:03.441945+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T00:51:18.481794+00:00\", \"completed_at\": \"2026-05-23T00:54:31.330429+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-5\", \"message\": \"连续 5 页纯文本无任何 figure 或 table。审稿人前 2 分钟翻阅无法获得视觉锚点，第一印象为\\\"文字墙\\\"。建议将 Figure 1（decoupling spectrum scatter plot，当前在 p13 appendix）或 Figure 2（evidence tax bar chart）提升至主文 Section 3 或 Section 4 开头\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页包含 0 个 figure，所有 4 个 figure 全部在 appendix（p13/p16/p17）。对于实证为主的论文，主文缺少图形可视化会显著削弱核心 message 的传达力度。Figure 1（decoupling spectrum）直接可视化论文核心概念，强烈建议移入主文\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文仅 3 个 display items（全部是 table），低于实证论文 8 页 5-8 个的典型密度。审稿人可能感觉实验呈现不够直观\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 4 per-relation EDCR 分布图列出 93 个关系类型，y 轴标签字号偏小（约正文字号的 50-60%），在打印或小屏阅读时可读性受限\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 4 使用红-绿渐变色标（红=severe decoupling, 绿=healthy），对红绿色盲不友好（约 8% 男性读者）。建议改为红-蓝或使用 Okabe-Ito 色板\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Figure 1 scatter plot 和 Figure 2 bar chart 紧凑排列在同一页，图表本身清晰可读，caption 自包含，质量良好\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"Figure 3 三面板训练动态图在双栏格式下面板较小但仍可读，颜色区分度可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1/2 使用 booktabs 风格，最优值加粗，次优下划线，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 3 格式规范，跨模型规模的结果对比清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文末页（Conclusion + Limitations + Ethics Statement）内容充实，无大面积空白\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"References 格式统一，无 [?] 未解析引用，排版正常\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"EDCR 公式（equation 2）渲染正确，无 LaTeX 错误\"}], \"counts\": {\"critical\": 0
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-23T01:06:03.442380+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-23T01:06:05.149401+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1707
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-23T01:06:05.300531+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-23T01:06:05.451995+00:00_

- id: "W1"
  summary: "GRPO confounded variables (QLoRA+G size changed simultaneously)"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - {round: 1, reviewers: "R1,R2", note: "Cannot support causal attribution of decoupling to QLoRA"}
  action_items:
    - {round: 1, action: "Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect (~8h GPU)", assigned_to: "Agent", status: "pending"}
    - {round: 1, action: "Downgrade causal claim to observational in Intro/Method/Analysis", assigned_to: "Paper Agent", status: "done"}
  resolution: ""
  resolution_round: null

- id: "W2"
  summary: "All results dev-set only, no test set"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - {round: 1, reviewers: "R1,R2", note: "No CodaLab test results for a system claiming 85+ configs"}
  action_items:
    - {round: 1, action: "D102 k=1 retraining then regenerate test predictions + user submits CodaLab", assigned_to: "Agent+User", status: "in_progress"}
  resolution: ""
  resolution_round: null

- id: "W3"
  summary: "SFT baseline single seed, no statistical significance test"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - {round: 1, reviewers: "R1,R2", note: "+4.92pp core claim lacks statistical backing"}
  action_items:
    - {round: 1, action: "Run SFT seed43 + seed44 (~8h GPU), compute bootstrap CI + Cohen's d", assigned_to: "Agent", status: "pending"}
  resolution: ""
  resolution_round: null

- id: "W4"
  summary: "Non-monotonic scaling claim based on only 3 data points"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - {round: 1, reviewers: "R1,R2", note: "1.7B repetition artifact, fair subset undefined, 3 points insufficient"}
  action_items:
    - {round: 1, action
…[truncated 9801 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-23T01:08:49.545948+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "faith-evidence-ie",
  "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO confounded variables (QLoRA+G size changed simultaneously)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W3 re-raised: GRPO collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. R1 cross-response agrees but notes Table 2 partially isolates precision (bf16 G=4 and G=8 both avoid collapse). Text analysis still insufficient.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect (~8h GPU)\", assigned_to: \"Agent\", status: \"pending\"}\n    - {round: 1, action: \"Downgrade causal claim to observational in Intro/Method/Analysis\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results for a system claiming 85+ configs\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9, Appendix I). Dev→Test 20pp drop noted but method ranking preserved (Spearman ρ=1.0). R2 rebuts R1-W6 severity.\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining then regenerate test predictions + user submits CodaLab\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"SFT baseline single seed → n=3 variance compression claim lacks statistical foundation\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"+4.92pp core claim lacks statistical backing\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W1 CRITICAL: now 3 seeds but n=3 still insufficient. σ 95% CI ≈ [0.52s, 6.29s], Cohen's d=2.58 SE≈1.2-1.5. '31× compression' statistically unreliable from n=3. R2 cross-response fully agrees. Both recommend ≥5-10 seeds or downgrade to qualitative observation.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43 + seed44 (~8h GPU), compute bootstrap CI + Cohen's d\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Increase to 5-10 seeds OR downgrade variance claim from contribution to observation, remove specific multipliers from Abstract\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"1.7B repetition artifact, fair subset undefined, 3 points insufficient\"}\n    - {round: 2, reviewers: \"R2\", note: \"R2-W2 MAJOR: 4 Qwen3 points + 1 LLaMA insufficient for general scaling claim. R1 cross-response partially rebuts: trend observation (not scaling law) is reasonable with these points, but per-point n=3 seeds weakens each point.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent'\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 1, action: \"Define fair subset + compute corrected evidence tax\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Add LLaMA as 4th data point, compute 1.7B no-evi repetition rate\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR definition circularity (shares Rel-Recall with Rel-F1)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"rho=-0.965 partially predetermined; absence of evidence != evidence of absence for per-relation\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W2 CRITICAL: TP in both numerator and denominator constructs mechanical negative correlation. n=7 too small, GRPO QLoRA outlier may dominate. R2 cross-response fully agrees, supplements outlier analysis. Both request: remove-outlier sensitivity, partial correlation controlling TP, permutation test.\"}\n  action_items:\n    - {round: 1, action: \"Compute deduplicated rho: n=7 rho=-0.89 p=0.007, per-relation n=76 rho=-0.79 p<0.0001\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR from contribution to diagnostic tool + add shared-component caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Report rho with GRPO QLoRA removed; add partial correlation controlling TP; add permutation test for per-relation analysis\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR rho=-0.965 (n=15) inflated by non-independent data points\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"Deduplicated n=7 gives rho=-0.89 (p=0.007); n=6 (no QLoRA) gives rho=-0.83 (p=0.042); per-relation n=76 rho=-0.79 (p<0.0001)\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Round 2 reviewers independently re-raised same concern. R1 requests remove-outlier analysis. Existing n=6 analysis (rho=-0.83, p=0.042) is borderline significant.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete: n=7 rho=-0.89 p=0.007 (with CED-reranker as 7th point)\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Update paper to report deduplicated rho + per-relation as primary evidence\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED approx equal to flat-NLI (0.02pp), contrastive increment insufficient\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive component adds complexity without measurable improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W3 MAJOR: 0.02pp within noise level (3-seed std≈0.09pp). Subtraction formula lacks theoretical motivation. Paper itself admits contrastive 'not essential'. R1 cross-response rebuts R2-S2 for listing CED as strength.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution, merge into RSFT method description\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"3.3x discrepancy affects reproducibility; k=3 vs k=1 root cause\"}\n    - {round: 2, note: \"Not raised in Round 2. Paper now consistently reports k=1 with ~3000 training samples (Table 4). Likely resolved.\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining fixes this; update section 3.3 to consistent k=1 numbers\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W8\"\n  summary: \"EDCR rho based on n=6, not significant without GRPO outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Now addressed: n=7 rho=-0.89 (p=0.007), per-relation n=76 rho=-0.79 (p<0.0001)\"}\n    - {round: 2, reviewers: \"R1\", note: \"R1-W2 re-raised: n=7 still small, GRPO QLoRA outlier dominance concern persists. Need remove-outlier sensitivity.\"}\n  action_items:\n    - {round: 1, action: \"Addressed by W5-EDCR-INFLATION deduplicated analysis\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 (sans QLoRA) rho and significance\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n    - {round: 2, note: \"Not raised in Round 2. Paper now uses 'approaches' (Abstract line 40-41). Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches' in Abstract/Intro/Conclusion\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Missing direct encoder baseline comparison table (SAIS/DREEAM/EIDER)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"DREEAM 54.01% buried in text, not in table\"}\n    - {round: 2, reviewers: \"R1\", note: \"R1-W7: Table 12 now exists but presentation is selective—emphasizes TP-only Evi-F1 >80%, downplays 16-18pp Ign-F1 gap. R2 agrees.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table in Appendix\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add more balanced discussion of Ign-F1 gap vs TP-only Evi-F1 advantage\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"R2-W3 re-raised: no KL ablation, no reward normalization test. R1 cross-response agrees.\"}\n  action_items:\n    - {round: 1, action: \"plan_015 rerun partially addresses; acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency (percentage vs decimal)\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Ign-F1 percentage, Rel-F1 decimal, throughout all tables\"}\n    - {round: 2, note: \"Not raised in Round 2. Tables now use consistent format. Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Unify all to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format throughout.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references and citation gaps\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', 2 Anonymous, 5 author mismatches\"}\n    - {round: 2, reviewers: \"R2\", note: \"R2-W4: Missing LMRC (Li & Zhang 2024), RelPrior (Huang et al. 2025), SummaC (Laban et al. 2022), Rationale Verification for RE (Li et al. 2025). R1 cross-response agrees on SummaC and LMRC.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors + add new citations\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n    - {round: 2, action: \"Add LMRC, SummaC at minimum; consider RelPrior and Rationale Verification\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n    - {round: 2, note: \"Not raised in Round 2. Fair subset now defined (Appendix D: matched@2048, 971/985 documents). Mechanistic breakdown in Table K (duplication rates). Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Fair subset defined + compute corrected evidence tax\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown with duplication rates added (Table K).\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3 scaling: 3/4 rows single seed\"}\n    - {round: 2, note: \"Improved: 1.7B/4B/8B now 3-seed, LLaMA 3-seed. 14B still single seed. R1-W1 shifts concern to n=3 being insufficient rather than missing seeds.\"}\n  action_items:\n    - {round: 1, action: \"D102 adds seeds for 8B/1.7B; W3 adds SFT seeds; LLaMA acknowledged in Limitations\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n    - {round: 2, note: \"Not raised in Round 2. Section 2 now cites Ruder 2017, Standley et al. 2020, Yu et al. 2020 for MTL/negative transfer. Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Add Related Work subsection on MTL/task interference\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added to Related Work (Ruder 2017, Standley et al. 2020, Yu et al. 2020).\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum analysis\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W4 MAJOR: Footnote 1 mentions 'earlier evaluation protocol' but doesn't specify differences. Table 2 presents DPO 3ep alongside other methods as if directly comparable. Both reviewers agree this undermines decoupling spectrum reliability.\"}\n  action_items:\n    - {round: 1, action: \"Remove all internal numbering\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 1, action: \"Re-eval DPO 3ep with current protocol (~1h GPU)\", assigned_to: \"Agent\", status: \"pending\"}\n    - {round: 2, action: \"Re-evaluate DPO 3ep under same protocol OR clearly exclude from Table 2 spectrum analysis\", assigned_to: \"Agent/Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need explicit random-k=1 to prove NLI-based selection has value\"}\n    - {round: 2, note: \"Not raised in Round 2. Table 5 (Appendix B) now includes RSFT random k=1 baseline (41.14 Ign-F1 vs CED 44.66), confirming CED selection value. Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline (~4h GPU)\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added to Table 5: 41.14 Ign-F1 (+1.40pp over SFT) vs CED RSFT 44.66 (+4.92pp).\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist (ARR requirement)\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory, absence risks desk reject\"}\n    - {round: 2, note: \"Not raised in Round 2. Paper now has comment indicating checklist submitted via OpenReview form per ARR/EMNLP 2026 guidelines (per user-defined rule). Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Add Responsible NLP Checklist after Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Checklist submitted via OpenReview form (not in PDF, per EMNLP 2026 rules).\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency (93 vs 76 vs 96)\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Conflicting numbers in appendix figure captions\"}\n    - {round: 2, note: \"Not raised in Round 2. Figure 4 caption now clarifies: 93 observed types out of 96 defined, 76 with ≥5 samples for correlation analysis. Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Verify correct number and unify\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified: 93 observed / 96 defined / 76 with ≥5 samples.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — three contributions are all empirical observations\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: C1 (evidence tax) = experimental observation; C2 (decoupling spectrum) = known gradient vs selection difference, EDCR = simple ratio; C3 (RSFT) = self-acknowledged 'well-established'. Paper is empirical study, not method paper. R1 cross-response downgrades to MAJOR, argues good empirical findings acceptable at EMNLP if statistics are sound.\"}\n  action_items:\n    - {round: 2, action: \"Reposition paper clearly as empirical study; strengthen statistical foundation to compensate for limited method novelty\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to external NLI model insufficiently analyzed\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"Only tested DeBERTa v3-base vs v3-large (same family). No cross-family NLI test. DocRE evidence may be OOD for standard NLI training data. R1 cross-response agrees.\"}\n  action_items:\n    - {round: 2, action: \"Test at least one non-DeBERTa NLI model OR add OOD analysis in Limitations\", assigned_to: \"Agent/Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measure different sources of randomness\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"MAJOR: SFT variance = full training randomness; RSFT variance = fixed-base fine-tuning randomness. RSFT variance naturally smaller because base model absorbs most randomness. Direct comparison unfair. Paper acknowledges in Section 7 but still makes strong claims in Abstract. R2 cross-response agrees but notes practical deployment value still holds.\"}\n  action_items:\n    - {round: 2, action: \"Either run RSFT from 3 different SFT bases for end-to-end variance, or clearly reframe variance claim as 'RSFT adds minimal additional variance' rather than 'compresses variance'\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions (annotation incompleteness, compute cost, task generalization)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"Three omissions: (1) DocRED evidence annotation known incomplete, affects CED/EDCR reliability; (2) compute cost comparison across GRPO/DPO/RSFT missing; (3) generalization beyond DocRE to other IE tasks not discussed. R1 cross-response agrees on all three.\"}\n  action_items:\n    - {round: 2, action: \"Add these three points to Limitations section\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax analysis\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"MINOR: Original 4B checkpoint unavailable, retrained shows 43.88 vs 44.23 (0.35pp gap). Evidence tax at 4B is 0.25±0.47pp — same order of magnitude as checkpoint gap.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text 8 pages contains 0 figures, all 4 figures in appendix\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"3 warnings: (1) Pages 1-5 no visual anchor; (2) Main text 0 figures, all in appendix; (3) Only 3 display items vs typical 5-8. Figure 1 (decoupling spectrum) directly visualizes core concept, should be in main text.\"}\n  action_items:\n    - {round: 2, action: \"Move Figure 1 (spectrum scatter) into main text Section 4.3; consider moving Figure 2 (scaling bars) into Section 4.4\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "faith-evidence-ie",
    "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO confounded variables (QLoRA+G size changed simultaneously)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W3 re-raised: GRPO collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. R1 cross-response agrees but notes Table 2 partially isolates precision (bf16 G=4 and G=8 both avoid collapse). Text analysis still insufficient.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect (~8h GPU)\", assigned_to: \"Agent\", status: \"pending\"}\n    - {round: 1, action: \"Downgrade causal claim to observational in Intro/Method/Analysis\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results for a system claiming 85+ configs\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9, Appendix I). Dev→Test 20pp drop noted but method ranking preserved (Spearman ρ=1.0). R2 rebuts R1-W6 severity.\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining then regenerate test predictions + user submits CodaLab\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"SFT baseline single seed → n=3 variance compression claim lacks statistical foundation\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"+4.92pp core claim lacks statistical backing\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W1 CRITICAL: now 3 seeds but n=3 still insufficient. σ 95% CI ≈ [0.52s, 6.29s], Cohen's d=2.58 SE≈1.2-1.5. '31× compression' statistically unreliable from n=3. R2 cross-response fully agrees. Both recommend ≥5-10 seeds or downgrade to qualitative observation.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43 + seed44 (~8h GPU), compute bootstrap CI + Cohen's d\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Increase to 5-10 seeds OR downgrade variance claim from contribution to observation, remove specific multipliers from Abstract\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"1.7B repetition artifact, fair subset undefined, 3 points insufficient\"}\n    - {round: 2, reviewers: \"R2\", note: \"R2-W2 MAJOR: 4 Qwen3 points + 1 LLaMA insufficient for general scaling claim. R1 cross-response partially rebuts: trend observation (not scaling law) is reasonable with these points, but per-point n=3 seeds weakens each point.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent'\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 1, action: \"Define fair subset + compute corrected evidence tax\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Add LLaMA as 4th data point, compute 1.7B no-evi repetition rate\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR definition circularity (shares Rel-Recall with Rel-F1)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"rho=-0.965 partially predetermined; absence of evidence != evidence of absence for per-relation\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W2 CRITICAL: TP in both numerator and denominator constructs mechanical negative correlation. n=7 too small, GRPO QLoRA outlier may dominate. R2 cross-response fully agrees, supplements outlier analysis. Both request: remove-outlier sensitivity, partial correlation controlling TP, permutation test.\"}\n  action_items:\n    - {round: 1, action: \"Compute deduplicated rho: n=7 rho=-0.89 p=0.007, per-relation n=76 rho=-0.79 p<0.0001\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR from contribution to diagnostic tool + add shared-component caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Report rho with GRPO QLoRA removed; add partial correlation controlling TP; add permutation test for per-relation analysis\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR rho=-0.965 (n=15) inflated by non-independent data points\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"Deduplicated n=7 gives rho=-0.89 (p=0.007); n=6 (no QLoRA) gives rho=-0.83 (p=0.042); per-relation n=76 rho=-0.79 (p<0.0001)\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Round 2 reviewers independently re-raised same concern. R1 requests remove-outlier analysis. Existing n=6 analysis (rho=-0.83, p=0.042) is borderline significant.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete: n=7 rho=-0.89 p=0.007 (with CED-reranker as 7th point)\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Update paper to report deduplicated rho + per-relation as primary evidence\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED approx equal to flat-NLI (0.02pp), contrastive increment insufficient\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive component adds complexity without measurable improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W3 MAJOR: 0.02pp within noise level (3-seed std≈0.09pp). Subtraction formula lacks theoretical motivation. Paper itself admits contrastive 'not essential'. R1 cross-response rebuts R2-S2 for listing CED as strength.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution, merge into RSFT method description\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"3.3x discrepancy affects reproducibility; k=3 vs k=1 root cause\"}\n    - {round: 2, note: \"Not raised in Round 2. Paper now consistently reports k=1 with ~3000 training samples (Table 4). Likely resolved.\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining fixes this; update section 3.3 to consistent k=1 numbers\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W8\"\n  summary: \"EDCR rho based on n=6, not significant without GRPO outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Now addressed: n=7 rho=-0.89 (p=0.007), per-relation n=76 rho=-0.79 (p<0.0001)\"}\n    - {round: 2, reviewers: \"R1\", note: \"R1-W2 re-raised: n=7 still small, GRPO QLoRA outlier dominance concern persists. Need remove-outlier sensitivity.\"}\n  action_items:\n    - {round: 1, action: \"Addressed by W5-EDCR-INFLATION deduplicated analysis\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 (sans QLoRA) rho and significance\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n    - {round: 2, note: \"Not raised in Round 2. Paper now uses 'approaches' (Abstract line 40-41). Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches' in Abstract/Intro/Conclusion\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Missing direct encoder baseline comparison table (SAIS/DREEAM/EIDER)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"DREEAM 54.01% buried in text, not in table\"}\n    - {round: 2, reviewers: \"R1\", note: \"R1-W7: Table 12 now exists but presentation is selective—emphasizes TP-only Evi-F1 >80%, downplays 16-18pp Ign-F1 gap. R2 agrees.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table in Appendix\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add more balanced discussion of Ign-F1 gap vs TP-only Evi-F1 advantage\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"R2-W3 re-raised: no KL ablation, no reward normalization test. R1 cross-response agrees.\"}\n  action_items:\n    - {round: 1, action: \"plan_015 rerun partially addresses; acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency (percentage vs decimal)\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Ign-F1 percentage, Rel-F1 decimal, throughout all tables\"}\n    - {round: 2, note: \"Not raised in Round 2. Tables now use consistent format. Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Unify all to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format throughout.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references and citation gaps\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', 2 Anonymous, 5 author mismatches\"}\n    - {round: 2, reviewers: \"R2\", note: \"R2-W4: Missing LMRC (Li & Zhang 2024), RelPrior (Huang et al. 2025), SummaC (Laban et al. 2022), Rationale Verification for RE (Li et al. 2025). R1 cross-response agrees on SummaC and LMRC.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors + add new citations\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n    - {round: 2, action: \"Add LMRC, SummaC at minimum; consider RelPrior and Rationale Verification\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n    - {round: 2, note: \"Not raised in Round 2. Fair subset now defined (Appendix D: matched@2048, 971/985 documents). Mechanistic breakdown in Table K (duplication rates). Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Fair subset defined + compute corrected evidence tax\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown with duplication rates added (Table K).\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3 scaling: 3/4 rows single seed\"}\n    - {round: 2, note: \"Improved: 1.7B/4B/8B now 3-seed, LLaMA 3-seed. 14B still single seed. R1-W1 shifts concern to n=3 being insufficient rather than missing seeds.\"}\n  action_items:\n    - {round: 1, action: \"D102 adds seeds for 8B/1.7B; W3 adds SFT seeds; LLaMA acknowledged in Limitations\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n    - {round: 2, note: \"Not raised in Round 2. Section 2 now cites Ruder 2017, Standley et al. 2020, Yu et al. 2020 for MTL/negative transfer. Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Add Related Work subsection on MTL/task interference\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added to Related Work (Ruder 2017, Standley et al. 2020, Yu et al. 2020).\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum analysis\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W4 MAJOR: Footnote 1 mentions 'earlier evaluation protocol' but doesn't specify differences. Table 2 presents DPO 3ep alongside other methods as if directly comparable. Both reviewers agree this undermines decoupling spectrum reliability.\"}\n  action_items:\n    - {round: 1, action: \"Remove all internal numbering\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 1, action: \"Re-eval DPO 3ep with current protocol (~1h GPU)\", assigned_to: \"Agent\", status: \"pending\"}\n    - {round: 2, action: \"Re-evaluate DPO 3ep under same protocol OR clearly exclude from Table 2 spectrum analysis\", assigned_to: \"Agent/Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need explicit random-k=1 to prove NLI-based selection has value\"}\n    - {round: 2, note: \"Not raised in Round 2. Table 5 (Appendix B) now includes RSFT random k=1 baseline (41.14 Ign-F1 vs CED 44.66), confirming CED selection value. Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline (~4h GPU)\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added to Table 5: 41.14 Ign-F1 (+1.40pp over SFT) vs CED RSFT 44.66 (+4.92pp).\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist (ARR requirement)\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory, absence risks desk reject\"}\n    - {round: 2, note: \"Not raised in Round 2. Paper now has comment indicating checklist submitted via OpenReview form per ARR/EMNLP 2026 guidelines (per user-defined rule). Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Add Responsible NLP Checklist after Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Checklist submitted via OpenReview form (not in PDF, per EMNLP 2026 rules).\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency (93 vs 76 vs 96)\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Conflicting numbers in appendix figure captions\"}\n    - {round: 2, note: \"Not raised in Round 2. Figure 4 caption now clarifies: 93 observed types out of 96 defined, 76 with ≥5 samples for correlation analysis. Resolved.\"}\n  action_items:\n    - {round: 1, action: \"Verify correct number and unify\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified: 93 observed / 96 defined / 76 with ≥5 samples.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — three contributions are all empirical observations\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: C1 (evidence tax) = experimental observation; C2 (decoupling spectrum) = known gradient vs selection difference, EDCR = simple ratio; C3 (RSFT) = self-acknowledged 'well-established'. Paper is empirical study, not method paper. R1 cross-response downgrades to MAJOR, argues good empirical findings acceptable at EMNLP if statistics are sound.\"}\n  action_items:\n    - {round: 2, action: \"Reposition paper clearly as empirical study; strengthen statistical foundation to compensate for limited method novelty\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to external NLI model insufficiently analyzed\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"Only tested DeBERTa v3-base vs v3-large (same family). No cross-family NLI test. DocRE evidence may be OOD for standard NLI training data. R1 cross-response agrees.\"}\n  action_items:\n    - {round: 2, action: \"Test at least one non-DeBERTa NLI model OR add OOD analysis in Limitations\", assigned_to: \"Agent/Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measure different sources of randomness\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"MAJOR: SFT variance = full training randomness; RSFT variance = fixed-base fine-tuning randomness. RSFT variance naturally smaller because base model absorbs most randomness. Direct comparison unfair. Paper acknowledges in Section 7 but still makes strong claims in Abstract. R2 cross-response agrees but notes practical deployment value still holds.\"}\n  action_items:\n    - {round: 2, action: \"Either run RSFT from 3 different SFT bases for end-to-end variance, or clearly reframe variance claim as 'RSFT adds minimal additional variance' rather than 'compresses variance'\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions (annotation incompleteness, compute cost, task generalization)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"Three omissions: (1) DocRED evidence annotation known incomplete, affects CED/EDCR reliability; (2) compute cost comparison across GRPO/DPO/RSFT missing; (3) generalization beyond DocRE to other IE tasks not discussed. R1 cross-response agrees on all three.\"}\n  action_items:\n    - {round: 2, action: \"Add these three points to Limitations section\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax analysis\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"MINOR: Original 4B checkpoint unavailable, retrained shows 43.88 vs 44.23 (0.35pp gap). Evidence tax at 4B is 0.25±0.47pp — same order of magnitude as checkpoint gap.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text 8 pages contains 0 figures, all 4 figures in appendix\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"3 warnings: (1) Pages 1-5 no visual anchor; (2) Main text 0 figures, all in appendix; (3) Only 3 display items vs typical 5-8. Figure 1 (decoupling spectrum) directly visualizes core concept, should be in main text.\"}\n  action_items:\n    - {round: 2, action: \"Move Figure 1 (spectrum scatter) into main text Section 4.3; consider moving Figure 2 (scaling bars) into Section 4.4\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-23T01:08:49.647202+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml\", \"bytes\": 21365}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-23T01:11:49.777444+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "faith-evidence-ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告（Round 2）\n\n**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n**Venue**: EMNLP 2026（ARR 统一审稿）\n**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性）\n\n---\n\n## Summary\n\n本文将 evidence-grounded document-level relation extraction (DocRE) 形式化为结构化生成任务，系统比较了 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3（1.7B/4B/8B/14B）和 LLaMA-3.1-8B 上的表现。三个核心发现：(1) evidence tax 是 scale-dependent 的（1.7B 有益，4B+ 近似中性）；(2) gradient-based optimization 导致 extraction-evidence decoupling（GRPO 灾难性、DPO 渐进），而 RSFT 通过离散样本选择避免 decoupling；(3) RSFT 压缩训练方差 4.6–31×。论文提出 CED（基于 NLI 的 contrastive 评分函数）和 EDCR（Evidence-Decoupling Ratio）作为分析工具。\n\n相比 Round 1，论文有显著改进：增加了 test set 评估（5 个 scale）、3-seed 覆盖（1.7B/4B/8B/LLaMA）、matched@2048 fair evaluation protocol、random RSFT baseline、encoder baseline 对比表、MTL 相关文献。但核心统计声明的基础仍然薄弱，方法论原创性问题未解决。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准且实用（R1-S1, R2-S1, 双方一致）。** Evidence grounding 是 LLM-based IE 部署的真实痛点。论文清晰地指出 encoder 方法（SAIS/DREEAM 的分类范式）与 LLM 方法（生成范式）在 evidence 处理上的结构性差异，这一 framing 对社区有价值。\n\n**S2. Decoupling spectrum 分析框架有启发性（R1-S2, R2-S4, 双方一致）。** 将 GRPO collapse → DPO gradual decay → RSFT no decoupling 组织为连续谱，从优化机制角度（gradient pressure vs. discrete selection）解释了不同范式的表现差异。Per-relation EDCR 分析（n=76, ρ=−0.79）和训练动态可视化（Figure 3）从统计和过程两层支撑核心论点。\n\n**S3. 跨尺度 + 跨 model family 的实验覆盖面好（R1-S3, R2-S1, 双方一致）。** 1.7B/4B/8B/14B（Qwen3）+ LLaMA-3.1-8B 的五模型覆盖，DocRED + Re-DocRED 双数据集验证，test set 评估保持 model ranking（Spearman ρ=1.0）。Matched@2048 fair evaluation protocol 和 controlled evaluation subset 体现了对混淆因素的认真处理。\n\n**S4. 对自身局限的透明度（R1-S4, 双方一致）。** 论文在 Section 7 主动承认 EDCR 缺乏 human judgment 验证、variance 基于 3 seeds、SFT vs RSFT variance 测量来源不同等局限。\n\n**S5. 写作质量高（R2-S5）。** \"Evidence tax\"概念和 decoupling spectrum 叙事框架清晰，Abstract 中的关键数字均可在正文追溯。\n\n---\n\n## Weaknesses\n\n### Must-Fix（阻碍接收的核心问题）\n\n**W1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础（R1-W1, R2 交叉回应 AGREE）。**\n论文第三个核心贡献 \"RSFT compresses training variance 4.6–31×\" 基于每组仅 3 个 seed 的标准差比较。n=3 时方差估计的自由度 df=2，σ 的 95% CI 约 [0.52s, 6.29s]——真实 σ 可能比估计值大 6 倍或小 2 倍。\"31× compression\" 在统计上几乎无法从 n=3 可靠估计。Cohen's d=2.58 的标准误约 1.2-1.5，95% CI 覆盖从接近 0 到 >5 的范围。此外，SFT variance（完整训练的 seed 方差）与 RSFT variance（固定基础上的微调方差）测量不同层次的随机性，RSFT variance 天然更小（R1-W5, R2 交叉回应 AGREE）。两个问题叠加使得 Abstract 中的核心声明不可靠。\n**建议**：增加到 5-10 seeds（至少对 1.7B 低成本尺度），或将方差压缩降级为定性观察（\"RSFT substantially reduces variance\"），不在 Abstract 和 Contributions 中给出具体倍数。\n\n**W2 [CRITICAL] — EDCR 的 shared-component 问题使统计验证不可靠（R1-W2, R2 交叉回应 AGREE）。**\nEDCR = Evi-Recall_TP / Rel-Recall = (TP_evi × G) / TP²。TP 同时出现在分子和分母中，构造了与 Rel-F1（也是 TP 的函数）的机械性负相关。Cross-method ρ=−0.89 (n=7, p=0.007) 中 n=7 极小，GRPO QLoRA 极端点（EDCR=0.9876, Rel-F1=1.38）可能主导相关性——移除后 n=6 时 ρ=−0.83 (p=0.042)，仅边际显著。Per-relation ρ=−0.79 (n=76) 面临同样的 shared-component 问题。\n**建议**：报告移除 GRPO QLoRA 后的 ρ；用 partial correlation 控制 TP 共享效应；用 permutation test 验证 per-relation 分析。\n\n**W3 [CRITICAL] — 方法论原创性不足（R2-W1, R1 交叉回应降级为 MAJOR）。**\n三个核心贡献逐一审视：(1) Evidence tax 的 scale-dependency 是实验观察，不是方法创新；(2) Decoupling spectrum 中 gradient-based vs selection-based 的根本差异在 multi-objective optimization/reward hacking 文献中已有讨论，EDCR 是两个 recall 的简单比值；(3) RSFT 论文自己承认是 \"well-established\"，应用于 DocRE + CED 是组合，非创新。CED 的 contrastive formulation 与 flat-NLI 差异仅 0.02pp（R1-W3），论文自己承认 \"not essential\"。整体定位为 empirical study with analytical tools，方法创新深度不足以进入 main conference。\n**R1 部分反驳**：好的 empirical finding 在 EMNLP 有先例；GRPO 在不同 precision 下的不同表现不是简单的 gradient vs selection 二分法。但这需要统计基础更牢固才能成立。\n\n### Should-Fix（显著影响论文质量的问题）\n\n**W4 [MAJOR] — GRPO collapse 分析缺乏机制深度（R2-W3, R1 交叉回应 AGREE）。**\nSection 4.3 对 GRPO QLoRA catastrophic collapse 的分析停留在现象描述。未连接 reward hacking 文献，未探讨简单缓解策略（不同 KL 系数、reward normalization），未分析 quantization precision 导致 collapse 的具体机制。Table 2 数据暗示 precision 是关键因素（bf16 G=4 和 G=8 均避免 catastrophe），但论文文字未深入讨论这一关键区分。如果 collapse 主要是 QLoRA 精度问题而非 GRPO 方法本质，\"decoupling spectrum\" 框架的稳固性受质疑。\n\n**W5 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol（R1-W4, R2 交叉回应 AGREE）。**\nFootnote 1 提到 \"earlier evaluation protocol\" 但未说明具体差异。Table 2 将 DPO 3-epoch 与其他方法并列，读者会视为直接可比。Decoupling spectrum 是论文核心分析框架之一，其中一个数据点来自不同 protocol 影响整个框架可靠性。建议在同一 protocol 下重评 DPO 3-epoch，或明确排除。\n\n**W6 [MAJOR] — CED contrastive formulation 增量价值不足（R1-W3, R2 交叉回应 AGREE）。**\nAppendix B 显示 CED vs flat-NLI 的 Rel-F1 差仅 0.02pp（45.63 vs 45.61），在 3-seed noise level（std≈0.09pp）以内。减法公式（p⁺ − max_j p⁻_j）缺乏理论动机（为什么不是比值或 log-ratio？）。论文自己承认 contrastive formulation \"not essential for data selection quality\"（Section 3.4）。CED 作为方法贡献被实质性削弱。\n\n### Nice-to-Fix（改善论文质量的建议）\n\n**W7 [MINOR] — Related Work 遗漏（R2-W4, R1 部分 AGREE）。**\n缺少：LMRC (Li & Zhang, 2024; arXiv 2408.13889)——LLM-based DocRE baseline；SummaC (Laban et al., 2022, TACL)——NLI-based faithfulness evaluation 先驱，与 CED 设计理念直接相关；RelPrior (Huang et al., 2025)；Rationale Verification for RE (Li et al., 2025)。\n\n**W8 [MINOR] — CED 对外部 NLI 模型的 sensitivity analysis 不足（R2-W5, R1 AGREE）。**\n仅测试 DeBERTa v3-base vs v3-large（同一家族），未测试其他 NLI 模型家族，未分析 DocRE 领域的 OOD 行为。\n\n**W9 [MINOR] — Encoder baseline 对比选择性呈现指标（R1-W7, R2 AGREE）。**\nTable 12 强调 TP-only Evi-F1（>80%），淡化 Ign-F1 16-18pp 差距。应更平衡讨论 LLM-based 方法在 absolute extraction performance 上的劣势。\n\n**W10 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比（R1-W8, R2 AGREE）。**\nRelated Work 讨论了 AutoRE、GLiDRE 等，但未在任何表格中给出 extraction performance 的直接对比。\n\n**W11 [MINOR] — Limitations 遗漏（R2-W6, R1 AGREE）。**\n(1) DocRED 证据标注已知不完整，影响 CED/EDCR 计算可靠性；(2) GRPO/DPO/RSFT 计算成本差异未报告；(3) 仅评估 DocRE 一种 IE 任务，generalization 未讨论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉回应后达成一致：\n\n- **[AGREE]** n=3 variance claim 统计基础不足，需要增加 seeds 或降级声明（R1-W1）\n- **[AGREE]** EDCR shared-component 构造机械性负相关，需要 partial correlation/remove-outlier analysis（R1-W2）\n- **[AGREE]** CED contrastive 增量仅 0.02pp，不足以作为方法贡献（R1-W3 = R2-W6 indirect）\n- **[AGREE]** SFT vs RSFT variance 测量不同来源，直接比较不公平（R1-W5）\n- **[AGREE]** GRPO collapse 分析需要更深机制解释和 reward hacking 文献连接（R2-W3）\n- **[AGREE]** DPO 3-epoch evaluation protocol 差异影响 spectrum 可比性（R1-W4）\n- **[AGREE]** Missing references: SummaC, LMRC（R2-W4）\n- **[AGREE]** 实验覆盖面和分析深度是论文强项（S1-S4）\n\n## Reviewer Divergence\n\n- **方法论原创性的严重程度**：R2 标为 CRITICAL（论文定位为 empirical study，方法创新不足以进入 main conference）；R1 降级为 MAJOR（好的 empirical findings 在 EMNLP 有先例，但需要统计基础更牢固）。最终评分差异（R2: 3.0 vs R1: 3.5）主要源于此分歧。\n- **Dev→Test 20pp drop 的严重性**：R1 标为 MAJOR（可能存在 dev overfitting），R2 REBUT（method ranking 完全保持 ρ=1.0，drop 可归因于 annotation density 差异 2.82×）。R1 在交叉回应中未反驳 R2 的 rebuttal，此分歧倾向 R2 观点——drop 不影响 relative comparison 有效性。\n\n---\n\n## Questions\n\n**Q1.** Cross-method EDCR 相关性 (ρ=−0.89, n=7) 中，移除 GRPO QLoRA collapse 极端数据点后，ρ 和 p-value 变为多少？（R1-Q1, R2-Q3）\n\n**Q2.** RSFT variance 声明中的 \"4.6–31×\" 区间，请提供每个 scale 的 SFT std 和 RSFT std 的 95% CI（基于 χ² 分布）。（R1-Q2）\n\n**Q3.** DPO 3-epoch 的 \"earlier evaluation protocol\" 与当前 protocol 的具体差异是什么？对 Rel-F1 和 Evi-F1 的影响幅度？（R1-Q3）\n\n**Q4.** GRPO collapse 是否在其他 KL 系数（如 0.1, 0.5）或不使用 QLoRA 时依然发生？Quantization precision 是 collapse 的主因还是 GRPO 方法本身？（R2-Q2）\n\n**Q5.** CED 的减法公式 (p⁺ − max p⁻_j) 是否尝试过其他组合方式（ratio、log-ratio）？（R1-Q5）\n\n**Q6.** RSFT \"avoids decoupling\" 的机制解释（Section F, \"discrete selection\"）在 N→∞ 的极限下是否依然成立？（R2-Q5）\n\n**Q7.** DocRED 标注密度 vs Re-DocRED（2.82× 差异）对 CED 的 negative samples 可靠性有何影响？（R2-Q4）\n\n---\n\n## Missing References\n\n1. **LMRC** (Li, X. & Zhang, M., 2024; arXiv 2408.13889) — LLM with Relation Classifier for DocRE，重要 LLM-based DocRE baseline（R2-W4, R1 AGREE）\n2. **SummaC** (Laban et al., 2022, TACL) — NLI-based faithfulness evaluation 先驱，CED 设计理念直接相关（R2-W4, R1 AGREE）\n3. **RelPrior** (Huang et al., 2025; arXiv 2511.08143) — Relation as a Prior for LLM-based DocRE（R2-W4）\n4. **Rationale Verification for RE** (Li et al., 2025, AAAI) — RE 中的 rationale verification（R2-W4）\n5. **Reward hacking 综述** — GRPO collapse 分析的理论背景（R2-W3）\n\n---\n\n## External Review\n\n外部审稿未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。3 个 warnings，9 个 info：\n\n**Warnings：**\n1. **主文无 figure**：8 页主文包含 0 个 figure，所有 4 个 figure 全在 appendix（p13/p16/p17）。对实证为主的论文，审稿人前 5 页翻阅无视觉锚点，第一印象为\"文字墙\"。建议将 Figure 1（decoupling spectrum scatter plot）移入主文 Section 4.3。\n2. **Display items 密度低**：主文仅 3 个 display items（全部 table），低于实证论文 8 页 5-8 个的典型密度。\n3. **Pages 1-5 无视觉元素**：连续 5 页纯文本。\n\n**Info（良好）：**\n- Tables 使用 booktabs 风格，格式规范，最优值加粗\n- References 无 [?] 未解析引用\n- EDCR 公式渲染正确\n- 末页内容充实无大面积空白\n\n**建议**：将 Figure 1（decoupling spectrum）和/或 Figure 2（scaling bars）移入主文。Figure 4 的红绿色标对色盲不友好（约 8% 男性读者），建议改为红蓝或 Okabe-Ito 色板。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 — 方法合理但统计推断基础薄弱（n=3 variance, EDCR shared-component） |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 — 分析视角有启发但方法创新有限，核心 insight (selection > gradient for multi-objective) 不算新颖 |\n| Reproducibility | 4/5 | 4/5 | 4/5 — Hyperparameters 详尽，数据集公开，声明开源 |\n| Overall | 3.5/5 | 3.0/5 | **3.0/5 — Findings** |\n\n### 置信度：4/5（两位 Reviewer 均对 DocRE 和 LLM post-training 方法较为熟悉）\n\n### Overall Score: 3.0（Findings — 可被 Findings 接收）\n\n### 理由\n\n本文是一项覆盖面广、分析深入的 empirical study。Evidence tax 的 scale-dependency 发现和 RSFT variance compression 的实践价值是真实的贡献。但论文面临两层核心问题：\n\n**第一层：统计方法论薄弱（R1 主要关注）。** n=3 的方差压缩声明（\"4.6-31×\"）在统计上不可靠——置信区间跨越数个数量级；EDCR 的 shared-component 构造了与 Rel-F1 的机械性负相关，n=7 的 cross-method 验证受极端点主导。这些问题可在 revision 中通过增加 seeds 和提供 partial correlation 来修复。\n\n**第二层：方法论原创性不足（R2 主要关注）。** 三个贡献均为经验观察：evidence tax 是实验发现、decoupling spectrum 反映已知的 gradient vs selection 差异、RSFT 是 well-established 方法的应用。CED 的 contrastive formulation 与 flat-NLI 差异仅 0.02pp，EDCR 是两个 recall 的简单比值。这一问题在 revision 中较难根本解决。\n\n两层问题叠加：如果统计基础更牢固，empirical study 的定位仍可支撑 Findings 甚至 Borderline Conference（R1 观点）；但在当前统计基础下，empirical findings 的可信度和方法创新的缺乏共同限制了论文水平。\n\n**相比 Round 1 的改进**：test set 评估（5 scale, ρ=1.0）、3-seed 覆盖、matched@2048 protocol、random baseline、encoder comparison table、MTL 引用——这些显著改善了论文质量，从 Round 1 的多项 CRITICAL 格式/数据缺失问题到 Round 2 的主要争议集中在统计方法论和原创性深度。\n\n**上调条件**：\n- 3.0 → 3.5（Borderline Conference）：修复 W1（增加 seeds 或降级声明）+ W2（EDCR partial correlation）+ 移入至少 1 个 figure 到主文\n- 3.5 → 4.0（Conference）：以上 + 深化 GRPO collapse 机制分析 + 补充 missing references + 重新定位 CED 角色\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"Evidence tax\" 概念和 gap 叙事有效，但 \"compresses training variance 4.6-31×\" 在 Abstract 中过于强调。建议改为 \"substantially reduces training variance\"。\n- Contribution 3 的表述 \"RSFT compresses training variance 4.6–31×\" 应附带 caveat 说明 n=3 和方差来源差异。\n\n### Section 3 (Method)\n- CED 的 contrastive formulation（Section 3.4）：既然论文自己确认 flat-NLI 效果相当，应降低 CED 的 novelty claim，将其定位为\"一种可选的评分变体\"而非核心方法贡献。\n- EDCR（Section 3.5）：shared-component caveat 已在论文中提及（\"this correlation should be interpreted as a diagnostic pattern rather than an independent discovery\"），但论文随后仍在 per-relation 分析中声称独立验证——需明确 per-relation EDCR 也有同样的 shared-component 结构。\n\n### Section 4 (Experiments)\n- Table 2 (Decoupling spectrum)：DPO 3-epoch 行应更显眼地标注 \"different evaluation protocol\"，或从 spectrum 分析中排除。\n- Section 4.4 (Scaling)：14B RSFT test 上低于 SFT 0.37pp（Table 9 注释）应在主文讨论，不仅在脚注中。这对 scaling narrative 是一个约束。\n- Table 3 (RSFT performance)：RSFT Tax 列的不同 seeds/methods（1.7B s42; 4B Method B s44; 8B, 14B: s42; LLaMA: 3-seed mean）使跨行比较复杂。建议统一或更清晰标注。\n\n### Section 5 (Analysis)\n- EDCR cross-method ρ=−0.89 (n=7)：建议附报 remove-GRPO-QLoRA 的 ρ（已有 n=6 数据 ρ=−0.83, p=0.042）。\n- Per-relation ρ=−0.79 (n=76)：建议添加 partial correlation controlling for TP。\n\n### Section 7 (Limitations)\n- 缺少：(1) DocRED 证据标注不完整对 CED/EDCR 可靠性的影响；(2) GRPO/DPO/RSFT 计算成本对比；(3) 仅评估 DocRE 的 generalization 限制。\n\n### Format\n- 主文 8 页无 figure：Figure 1 (spectrum scatter) 直接可视化核心概念，强烈建议移入主文。当前 3 个 display items 密度远低于实证论文典型水平。\n- Figure 4 红绿色标建议改为色盲友好配色。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "faith-evidence-ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# 审稿报告（Round 2）\n\n**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n**Venue**: EMNLP 2026（ARR 统一审稿）\n**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性）\n\n---\n\n## Summary\n\n本文将 evidence-grounded document-level relation extraction (DocRE) 形式化为结构化生成任务，系统比较了 GRPO、DPO、RSFT 三种 post-SFT 优化范式在 Qwen3（1.7B/4B/8B/14B）和 LLaMA-3.1-8B 上的表现。三个核心发现：(1) evidence tax 是 scale-dependent 的（1.7B 有益，4B+ 近似中性）；(2) gradient-based optimization 导致 extraction-evidence decoupling（GRPO 灾难性、DPO 渐进），而 RSFT 通过离散样本选择避免 decoupling；(3) RSFT 压缩训练方差 4.6–31×。论文提出 CED（基于 NLI 的 contrastive 评分函数）和 EDCR（Evidence-Decoupling Ratio）作为分析工具。\n\n相比 Round 1，论文有显著改进：增加了 test set 评估（5 个 scale）、3-seed 覆盖（1.7B/4B/8B/LLaMA）、matched@2048 fair evaluation protocol、random RSFT baseline、encoder baseline 对比表、MTL 相关文献。但核心统计声明的基础仍然薄弱，方法论原创性问题未解决。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准且实用（R1-S1, R2-S1, 双方一致）。** Evidence grounding 是 LLM-based IE 部署的真实痛点。论文清晰地指出 encoder 方法（SAIS/DREEAM 的分类范式）与 LLM 方法（生成范式）在 evidence 处理上的结构性差异，这一 framing 对社区有价值。\n\n**S2. Decoupling spectrum 分析框架有启发性（R1-S2, R2-S4, 双方一致）。** 将 GRPO collapse → DPO gradual decay → RSFT no decoupling 组织为连续谱，从优化机制角度（gradient pressure vs. discrete selection）解释了不同范式的表现差异。Per-relation EDCR 分析（n=76, ρ=−0.79）和训练动态可视化（Figure 3）从统计和过程两层支撑核心论点。\n\n**S3. 跨尺度 + 跨 model family 的实验覆盖面好（R1-S3, R2-S1, 双方一致）。** 1.7B/4B/8B/14B（Qwen3）+ LLaMA-3.1-8B 的五模型覆盖，DocRED + Re-DocRED 双数据集验证，test set 评估保持 model ranking（Spearman ρ=1.0）。Matched@2048 fair evaluation protocol 和 controlled evaluation subset 体现了对混淆因素的认真处理。\n\n**S4. 对自身局限的透明度（R1-S4, 双方一致）。** 论文在 Section 7 主动承认 EDCR 缺乏 human judgment 验证、variance 基于 3 seeds、SFT vs RSFT variance 测量来源不同等局限。\n\n**S5. 写作质量高（R2-S5）。** \"Evidence tax\"概念和 decoupling spectrum 叙事框架清晰，Abstract 中的关键数字均可在正文追溯。\n\n---\n\n## Weaknesses\n\n### Must-Fix（阻碍接收的核心问题）\n\n**W1 [CRITICAL] — n=3 seeds 的方差压缩声明缺乏统计基础（R1-W1, R2 交叉回应 AGREE）。**\n论文第三个核心贡献 \"RSFT compresses training variance 4.6–31×\" 基于每组仅 3 个 seed 的标准差比较。n=3 时方差估计的自由度 df=2，σ 的 95% CI 约 [0.52s, 6.29s]——真实 σ 可能比估计值大 6 倍或小 2 倍。\"31× compression\" 在统计上几乎无法从 n=3 可靠估计。Cohen's d=2.58 的标准误约 1.2-1.5，95% CI 覆盖从接近 0 到 >5 的范围。此外，SFT variance（完整训练的 seed 方差）与 RSFT variance（固定基础上的微调方差）测量不同层次的随机性，RSFT variance 天然更小（R1-W5, R2 交叉回应 AGREE）。两个问题叠加使得 Abstract 中的核心声明不可靠。\n**建议**：增加到 5-10 seeds（至少对 1.7B 低成本尺度），或将方差压缩降级为定性观察（\"RSFT substantially reduces variance\"），不在 Abstract 和 Contributions 中给出具体倍数。\n\n**W2 [CRITICAL] — EDCR 的 shared-component 问题使统计验证不可靠（R1-W2, R2 交叉回应 AGREE）。**\nEDCR = Evi-Recall_TP / Rel-Recall = (TP_evi × G) / TP²。TP 同时出现在分子和分母中，构造了与 Rel-F1（也是 TP 的函数）的机械性负相关。Cross-method ρ=−0.89 (n=7, p=0.007) 中 n=7 极小，GRPO QLoRA 极端点（EDCR=0.9876, Rel-F1=1.38）可能主导相关性——移除后 n=6 时 ρ=−0.83 (p=0.042)，仅边际显著。Per-relation ρ=−0.79 (n=76) 面临同样的 shared-component 问题。\n**建议**：报告移除 GRPO QLoRA 后的 ρ；用 partial correlation 控制 TP 共享效应；用 permutation test 验证 per-relation 分析。\n\n**W3 [CRITICAL] — 方法论原创性不足（R2-W1, R1 交叉回应降级为 MAJOR）。**\n三个核心贡献逐一审视：(1) Evidence tax 的 scale-dependency 是实验观察，不是方法创新；(2) Decoupling spectrum 中 gradient-based vs selection-based 的根本差异在 multi-objective optimization/reward hacking 文献中已有讨论，EDCR 是两个 recall 的简单比值；(3) RSFT 论文自己承认是 \"well-established\"，应用于 DocRE + CED 是组合，非创新。CED 的 contrastive formulation 与 flat-NLI 差异仅 0.02pp（R1-W3），论文自己承认 \"not essential\"。整体定位为 empirical study with analytical tools，方法创新深度不足以进入 main conference。\n**R1 部分反驳**：好的 empirical finding 在 EMNLP 有先例；GRPO 在不同 precision 下的不同表现不是简单的 gradient vs selection 二分法。但这需要统计基础更牢固才能成立。\n\n### Should-Fix（显著影响论文质量的问题）\n\n**W4 [MAJOR] — GRPO collapse 分析缺乏机制深度（R2-W3, R1 交叉回应 AGREE）。**\nSection 4.3 对 GRPO QLoRA catastrophic collapse 的分析停留在现象描述。未连接 reward hacking 文献，未探讨简单缓解策略（不同 KL 系数、reward normalization），未分析 quantization precision 导致 collapse 的具体机制。Table 2 数据暗示 precision 是关键因素（bf16 G=4 和 G=8 均避免 catastrophe），但论文文字未深入讨论这一关键区分。如果 collapse 主要是 QLoRA 精度问题而非 GRPO 方法本质，\"decoupling spectrum\" 框架的稳固性受质疑。\n\n**W5 [MAJOR] — DPO 3-epoch 使用不同 evaluation protocol（R1-W4, R2 交叉回应 AGREE）。**\nFootnote 1 提到 \"earlier evaluation protocol\" 但未说明具体差异。Table 2 将 DPO 3-epoch 与其他方法并列，读者会视为直接可比。Decoupling spectrum 是论文核心分析框架之一，其中一个数据点来自不同 protocol 影响整个框架可靠性。建议在同一 protocol 下重评 DPO 3-epoch，或明确排除。\n\n**W6 [MAJOR] — CED contrastive formulation 增量价值不足（R1-W3, R2 交叉回应 AGREE）。**\nAppendix B 显示 CED vs flat-NLI 的 Rel-F1 差仅 0.02pp（45.63 vs 45.61），在 3-seed noise level（std≈0.09pp）以内。减法公式（p⁺ − max_j p⁻_j）缺乏理论动机（为什么不是比值或 log-ratio？）。论文自己承认 contrastive formulation \"not essential for data selection quality\"（Section 3.4）。CED 作为方法贡献被实质性削弱。\n\n### Nice-to-Fix（改善论文质量的建议）\n\n**W7 [MINOR] — Related Work 遗漏（R2-W4, R1 部分 AGREE）。**\n缺少：LMRC (Li & Zhang, 2024; arXiv 2408.13889)——LLM-based DocRE baseline；SummaC (Laban et al., 2022, TACL)——NLI-based faithfulness evaluation 先驱，与 CED 设计理念直接相关；RelPrior (Huang et al., 2025)；Rationale Verification for RE (Li et al., 2025)。\n\n**W8 [MINOR] — CED 对外部 NLI 模型的 sensitivity analysis 不足（R2-W5, R1 AGREE）。**\n仅测试 DeBERTa v3-base vs v3-large（同一家族），未测试其他 NLI 模型家族，未分析 DocRE 领域的 OOD 行为。\n\n**W9 [MINOR] — Encoder baseline 对比选择性呈现指标（R1-W7, R2 AGREE）。**\nTable 12 强调 TP-only Evi-F1（>80%），淡化 Ign-F1 16-18pp 差距。应更平衡讨论 LLM-based 方法在 absolute extraction performance 上的劣势。\n\n**W10 [MINOR] — 缺少与其他 LLM-based RE 方法的直接数值对比（R1-W8, R2 AGREE）。**\nRelated Work 讨论了 AutoRE、GLiDRE 等，但未在任何表格中给出 extraction performance 的直接对比。\n\n**W11 [MINOR] — Limitations 遗漏（R2-W6, R1 AGREE）。**\n(1) DocRED 证据标注已知不完整，影响 CED/EDCR 计算可靠性；(2) GRPO/DPO/RSFT 计算成本差异未报告；(3) 仅评估 DocRE 一种 IE 任务，generalization 未讨论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉回应后达成一致：\n\n- **[AGREE]** n=3 variance claim 统计基础不足，需要增加 seeds 或降级声明（R1-W1）\n- **[AGREE]** EDCR shared-component 构造机械性负相关，需要 partial correlation/remove-outlier analysis（R1-W2）\n- **[AGREE]** CED contrastive 增量仅 0.02pp，不足以作为方法贡献（R1-W3 = R2-W6 indirect）\n- **[AGREE]** SFT vs RSFT variance 测量不同来源，直接比较不公平（R1-W5）\n- **[AGREE]** GRPO collapse 分析需要更深机制解释和 reward hacking 文献连接（R2-W3）\n- **[AGREE]** DPO 3-epoch evaluation protocol 差异影响 spectrum 可比性（R1-W4）\n- **[AGREE]** Missing references: SummaC, LMRC（R2-W4）\n- **[AGREE]** 实验覆盖面和分析深度是论文强项（S1-S4）\n\n## Reviewer Divergence\n\n- **方法论原创性的严重程度**：R2 标为 CRITICAL（论文定位为 empirical study，方法创新不足以进入 main conference）；R1 降级为 MAJOR（好的 empirical findings 在 EMNLP 有先例，但需要统计基础更牢固）。最终评分差异（R2: 3.0 vs R1: 3.5）主要源于此分歧。\n- **Dev→Test 20pp drop 的严重性**：R1 标为 MAJOR（可能存在 dev overfitting），R2 REBUT（method ranking 完全保持 ρ=1.0，drop 可归因于 annotation density 差异 2.82×）。R1 在交叉回应中未反驳 R2 的 rebuttal，此分歧倾向 R2 观点——drop 不影响 relative comparison 有效性。\n\n---\n\n## Questions\n\n**Q1.** Cross-method EDCR 相关性 (ρ=−0.89, n=7) 中，移除 GRPO QLoRA collapse 极端数据点后，ρ 和 p-value 变为多少？（R1-Q1, R2-Q3）\n\n**Q2.** RSFT variance 声明中的 \"4.6–31×\" 区间，请提供每个 scale 的 SFT std 和 RSFT std 的 95% CI（基于 χ² 分布）。（R1-Q2）\n\n**Q3.** DPO 3-epoch 的 \"earlier evaluation protocol\" 与当前 protocol 的具体差异是什么？对 Rel-F1 和 Evi-F1 的影响幅度？（R1-Q3）\n\n**Q4.** GRPO collapse 是否在其他 KL 系数（如 0.1, 0.5）或不使用 QLoRA 时依然发生？Quantization precision 是 collapse 的主因还是 GRPO 方法本身？（R2-Q2）\n\n**Q5.** CED 的减法公式 (p⁺ − max p⁻_j) 是否尝试过其他组合方式（ratio、log-ratio）？（R1-Q5）\n\n**Q6.** RSFT \"avoids decoupling\" 的机制解释（Section F, \"discrete selection\"）在 N→∞ 的极限下是否依然成立？（R2-Q5）\n\n**Q7.** DocRED 标注密度 vs Re-DocRED（2.82× 差异）对 CED 的 negative samples 可靠性有何影响？（R2-Q4）\n\n---\n\n## Missing References\n\n1. **LMRC** (Li, X. & Zhang, M., 2024; arXiv 2408.13889) — LLM with Relation Classifier for DocRE，重要 LLM-based DocRE baseline（R2-W4, R1 AGREE）\n2. **SummaC** (Laban et al., 2022, TACL) — NLI-based faithfulness evaluation 先驱，CED 设计理念直接相关（R2-W4, R1 AGREE）\n3. **RelPrior** (Huang et al., 2025; arXiv 2511.08143) — Relation as a Prior for LLM-based DocRE（R2-W4）\n4. **Rationale Verification for RE** (Li et al., 2025, AAAI) — RE 中的 rationale verification（R2-W4）\n5. **Reward hacking 综述** — GRPO collapse 分析的理论背景（R2-W3）\n\n---\n\n## External Review\n\n外部审稿未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。3 个 warnings，9 个 info：\n\n**Warnings：**\n1. **主文无 figure**：8 页主文包含 0 个 figure，所有 4 个 figure 全在 appendix（p13/p16/p17）。对实证为主的论文，审稿人前 5 页翻阅无视觉锚点，第一印象为\"文字墙\"。建议将 Figure 1（decoupling spectrum scatter plot）移入主文 Section 4.3。\n2. **Display items 密度低**：主文仅 3 个 display items（全部 table），低于实证论文 8 页 5-8 个的典型密度。\n3. **Pages 1-5 无视觉元素**：连续 5 页纯文本。\n\n**Info（良好）：**\n- Tables 使用 booktabs 风格，格式规范，最优值加粗\n- References 无 [?] 未解析引用\n- EDCR 公式渲染正确\n- 末页内容充实无大面积空白\n\n**建议**：将 Figure 1（decoupling spectrum）和/或 Figure 2（scaling bars）移入主文。Figure 4 的红绿色标对色盲不友好（约 8% 男性读者），建议改为红蓝或 Okabe-Ito 色板。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 — 方法合理但统计推断基础薄弱（n=3 variance, EDCR shared-component） |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 — 分析视角有启发但方法创新有限，核心 insight (selection > gradient for multi-objective) 不算新颖 |\n| Reproducibility | 4/5 | 4/5 | 4/5 — Hyperparameters 详尽，数据集公开，声明开源 |\n| Overall | 3.5/5 | 3.0/5 | **3.0/5 — Findings** |\n\n### 置信度：4/5（两位 Reviewer 均对 DocRE 和 LLM post-training 方法较为熟悉）\n\n### Overall Score: 3.0（Findings — 可被 Findings 接收）\n\n### 理由\n\n本文是一项覆盖面广、分析深入的 empirical study。Evidence tax 的 scale-dependency 发现和 RSFT variance compression 的实践价值是真实的贡献。但论文面临两层核心问题：\n\n**第一层：统计方法论薄弱（R1 主要关注）。** n=3 的方差压缩声明（\"4.6-31×\"）在统计上不可靠——置信区间跨越数个数量级；EDCR 的 shared-component 构造了与 Rel-F1 的机械性负相关，n=7 的 cross-method 验证受极端点主导。这些问题可在 revision 中通过增加 seeds 和提供 partial correlation 来修复。\n\n**第二层：方法论原创性不足（R2 主要关注）。** 三个贡献均为经验观察：evidence tax 是实验发现、decoupling spectrum 反映已知的 gradient vs selection 差异、RSFT 是 well-established 方法的应用。CED 的 contrastive formulation 与 flat-NLI 差异仅 0.02pp，EDCR 是两个 recall 的简单比值。这一问题在 revision 中较难根本解决。\n\n两层问题叠加：如果统计基础更牢固，empirical study 的定位仍可支撑 Findings 甚至 Borderline Conference（R1 观点）；但在当前统计基础下，empirical findings 的可信度和方法创新的缺乏共同限制了论文水平。\n\n**相比 Round 1 的改进**：test set 评估（5 scale, ρ=1.0）、3-seed 覆盖、matched@2048 protocol、random baseline、encoder comparison table、MTL 引用——这些显著改善了论文质量，从 Round 1 的多项 CRITICAL 格式/数据缺失问题到 Round 2 的主要争议集中在统计方法论和原创性深度。\n\n**上调条件**：\n- 3.0 → 3.5（Borderline Conference）：修复 W1（增加 seeds 或降级声明）+ W2（EDCR partial correlation）+ 移入至少 1 个 figure 到主文\n- 3.5 → 4.0（Conference）：以上 + 深化 GRPO collapse 机制分析 + 补充 missing references + 重新定位 CED 角色\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"Evidence tax\" 概念和 gap 叙事有效，但 \"compresses training variance 4.6-31×\" 在 Abstract 中过于强调。建议改为 \"substantially reduces training variance\"。\n- Contribution 3 的表述 \"RSFT compresses training variance 4.6–31×\" 应附带 caveat 说明 n=3 和方差来源差异。\n\n### Section 3 (Method)\n- CED 的 contrastive formulation（Section 3.4）：既然论文自己确认 flat-NLI 效果相当，应降低 CED 的 novelty claim，将其定位为\"一种可选的评分变体\"而非核心方法贡献。\n- EDCR（Section 3.5）：shared-component caveat 已在论文中提及（\"this correlation should be interpreted as a diagnostic pattern rather than an independent discovery\"），但论文随后仍在 per-relation 分析中声称独立验证——需明确 per-relation EDCR 也有同样的 shared-component 结构。\n\n### Section 4 (Experiments)\n- Table 2 (Decoupling spectrum)：DPO 3-epoch 行应更显眼地标注 \"different evaluation protocol\"，或从 spectrum 分析中排除。\n- Section 4.4 (Scaling)：14B RSFT test 上低于 SFT 0.37pp（Table 9 注释）应在主文讨论，不仅在脚注中。这对 scaling narrative 是一个约束。\n- Table 3 (RSFT performance)：RSFT Tax 列的不同 seeds/methods（1.7B s42; 4B Method B s44; 8B, 14B: s42; LLaMA: 3-seed mean）使跨行比较复杂。建议统一或更清晰标注。\n\n### Section 5 (Analysis)\n- EDCR cross-method ρ=−0.89 (n=7)：建议附报 remove-GRPO-QLoRA 的 ρ（已有 n=6 数据 ρ=−0.83, p=0.042）。\n- Per-relation ρ=−0.79 (n=76)：建议添加 partial correlation controlling for TP。\n\n### Section 7 (Limitations)\n- 缺少：(1) DocRED 证据标注不完整对 CED/EDCR 可靠性的影响；(2) GRPO/DPO/RSFT 计算成本对比；(3) 仅评估 DocRE 的 generalization 限制。\n\n### Format\n- 主文 8 页无 figure：Figure 1 (spectrum scatter) 直接可视化核心概念，强烈建议移入主文。当前 3 个 display items 密度远低于实证论文典型水平。\n- Figure 4 红绿色标建议改为色盲友好配色。"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-23T01:11:53.948882+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_84537e1e2f9ef71a90742c2db859c6f2:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4171
}
```

</details>

---


### Assistant

_source line 194 · 2026-05-23T01:12:07.029562+00:00_

审稿报告已投递。

**Round 2 审稿完成。**

**最终评分：3.0（Findings）**

核心结论：
- **2 个 CRITICAL（双方共识）**：n=3 方差压缩声明统计基础不足；EDCR 存在 shared-component 机械性负相关
- **1 个 CRITICAL（R2 主张，R1 降为 MAJOR）**：方法论原创性不足，三个贡献均为经验观察
- **3 个 MAJOR**：GRPO collapse 分析缺机制深度；DPO 3-epoch evaluation protocol 不一致；CED contrastive 增量仅 0.02pp
- **相比 Round 1 已修复**：test set 评估、3-seed 覆盖、random baseline、encoder comparison、格式问题等

**上调路径**：修复 variance claim 统计基础 + EDCR partial correlation + 主文加入 figure → 3.5；进一步深化 GRPO 机制分析 + 补引用 → 4.0。

Issue Tracker 已同步更新（7 项 resolved，14 项 open/in_progress，4 项新增）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 195 · 2026-05-23T01:12:09.647541+00:00_

[Reviewer 1 审稿结果]:
逐条回应已提交给 Director。核心立场：

- **R2-S2（CED 设计合理）和 R2-S3（variance compression 价值）**被反驳——CED contrastive 组件仅贡献 0.02pp（Appendix B），Cohen's d=2.58 基于 n=3 不可靠
- **R2-W1（原创性不足）**部分反驳——真正 critical 的不是原创性而是统计方法论薄弱，R2 在这方面存在盲区
- **R2-W3（GRPO 分析缺深度）**同意但补充：Table 2 实际已隔离 precision vs group size，只是文字分析停留在现象层面
- 维持 3.5 评分，高于 R2 的 3.0，因为分析框架有社区价值，但受限于统计基础

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 196 · 2026-05-23T01:12:31.991644+00:00_

审稿报告已投递完毕。

**Round 2 审稿总结**：

- **Overall: 3.0（Findings）**
- R1 评分 3.5（Borderline Conference），R2 评分 3.0（Findings）
- 3 个 CRITICAL：n=3 方差压缩统计基础不足、EDCR shared-component 机械性负相关、方法论原创性不足
- 3 个 MAJOR：GRPO collapse 机制分析不足、DPO 3-epoch protocol 差异、CED contrastive 增量仅 0.02pp
- 核心分歧：原创性是 CRITICAL（R2）还是 MAJOR（R1）——R1 认为统计方法论才是真正的瓶颈
- 相比 Round 1 有显著改进（test set、3-seed、matched@2048、random baseline 等），但统计声明基础和方法创新深度仍是主要障碍
- Issue Tracker 已同步更新（8 项 resolved，多项新增/更新）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 19

## Round 19

58 recorded events


### User

_source line 197 · 2026-05-24T22:49:54.974958+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: faith-evidence-ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-24T22:50:02.546352+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-24T22:50:02.597288+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-24T22:50:17.964261+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-24T22:50:18.115403+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-24T22:50:30.259385+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-24T22:50:30.259785+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-24T22:50:36.687904+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-24T22:50:38.545628+00:00_

{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (370 个)\n\n- **mvp2_eval_lr5e6_r1_ckpt20**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_step90**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_step100**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_ckpt10**: DONE (success) — \n- **mvp2_eval_ced_kl001_r4_early**: DONE (negative) — \n- **mvp2_grpo_flatnli_r6**: DONE (negative) — \n- **mvp2_grpo_ced_kl001_r4**: DONE (success) — \n- **mvp2_sft_eval_r3**: DONE (success) — \n- **mvp2_grpo_extract_r3**: DONE (negative) — \n- **mvp2_grpo_ced_r5**: DONE (negative) — \n- **mvp2_sft_eval_r2**: DONE (success) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d158_14b_rsft_s44_generate | 14B seed=44 candidate generation for 3-seed statistical robustness. Replicates plan017_14b_rsft_s43_generate parameters with seed=44 SFT adapter. | — | — | — |\n\n## 待处理\n- test_eval_4b_rsft_s44_no_evi_v2: 4B RSFT CED k=1 s44 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s44 with-evi ign_f1=0.2525 计算 evidence tax。s42 tax=+1.51pp, s43 tax=+1.99pp。3-seed mean±std 完善 4B evidence tax。v1 因 conda 未激活 EXIT_CODE=127 失败，本次修复。（准备中）\n\n## 近期结论\n- **d102_1_7b_k1_s42** (success): D102 method correction: Qwen3-1.7B RSFT eval using k=1 CED (matching paper methodology) instead of k=3\n- **d102_llama_k1_s42** (success): D102 method correction: LLaMA-8B RSFT eval using k=1 CED (matching paper methodology) instead of k=3\n- **d158_1_7b_rsft_s44_ced_score** (success): 1.7B seed=44 CED/NLI scoring + k=1 selection. 对 24216 个生成样本进行 CED 评分并筛选 top-1。预期保留 ~3021 样本（与 s42/s43 一致）。D158 强制检查点：保留数与 3021 差异 >10% 则暂停 A3。 ← 基于 d158_1_7b_rsft_s44_generate\n\n## 趋势\n成功 234 / 负向 23 / 失败 65 / 共 368\n\n## 下一步\n（无活跃 idea，请通过 ide
…[truncated 2530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-24T22:50:38.997842+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-24T22:50:39.449683+00:00_

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
15	\usepackage{xcolor}
16	\usepackage{multirow}
17	\usepackage{subcaption}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-24T22:50:39.600908+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-24T22:50:39.702068+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-24T22:50:48.704108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-24T22:50:49.156440+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-24T22:50:52.068447+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-24T22:50:52.470493+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1220707 May 24 22:48 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-24T22:50:52.571434+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-24T22:50:52.622119+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-24T22:50:54.530114+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the information about EMNLP 2026 Call for Papers submission deadline through ARR:

## Key Deadline

The ARR submission deadline for EMNLP 2026 is
…[truncated 721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 5826
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-24T22:50:56.540214+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission guidelines:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. The search results indicate guidelines for short papers as well, though the specific page count for short papers isn't explicitly stated in the retrieved results.

## Key Author Instructions

**Formatting and Template:**
The submission must adhere to the format
…[truncated 1050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "WebSearch",
  "elapsed_ms": 7383
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-24T22:51:16.456595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-24T22:51:16.909143+00:00_

1	\begin{abstract}
2	Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet these methods output bare relation triplets without identifying supporting sentences. Encoder-based evidence methods (SAIS, DREEAM) provide supporting sentences but trail LLM approaches in accuracy, creating a gap between extraction performance and output verifiability. We formalize evidence-grounded DocRE as structured generation and compare Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax---extraction cost of generating evidence---is scale-dependent: beneficial at 1.7B ($-$5.63pp dev Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with Natural Language Inference (NLI)-based scoring avoids decoupling entirely through output filtering rather than gradient pressure. RSFT consistently reduces training seed variance (complete pairwise seed separation on LLaMA, Cohen's $d{=}2.58$; non-overlapping $\chi^2$ confidence intervals at 1.7B). Our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters. Test-set evaluation preserves model ranking across all evaluated scales (Spearman $\rho{=}1.0$).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-24T22:51:16.909572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-24T22:51:17.411852+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \emph{which sentences} support each prediction.
6	Without evidence, a clinician reviewing a ten-page case report must manually locate the sentences that support each extracted drug interaction---a bottleneck that undermines trust in automated extraction.
7	
8	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
9	Both produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.
10	The community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.
11	
12	This gap reflects a structural difference.
13	In encoder methods, evidence retrieval is classification that regularizes the encoder at negligible cost; in LLM-based DocRE, evidence requires the model to \emph{generate} additional output tokens per triple, increasing output length and decoding complexity.
14	The na\"{i}ve expectation is that this generation cost always harms extraction accuracy.
15	Our experiments show this expectation is wrong.
16	The evidence tax is not a fixed penalt
…[truncated 2313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-24T22:51:17.412266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-24T22:51:18.366344+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{fig_overview.pdf}
7	\vspace{-2mm}
8	\caption{Evidence-grounded DocRE produces relation triples with supporting sentence indices, unlike standard DocRE which outputs bare triples. RSFT selects the top-$k$ of $N$ CED-scored candidates per document for fine-tuning.}
9	\label{fig:overview}
10	\end{figure*}
11	
12	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
13	\label{sec:task}
14	
15	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\ref{fig:overview}).
16	
17	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sent
…[truncated 9504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-24T22:51:18.366853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-24T22:51:19.070635+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate on DocRED~\citep{yao2019docred} (3,053 training / 998 dev documents, 96 relation types) with Re-DocRED~\citep{tan2022redocred} for cross-dataset validation. Our primary model is Qwen3-4B; we also train Qwen3-1.7B, 8B, and 14B to study scale effects, with LLaMA-3.1-8B for cross-family validation. All models use LoRA~\citep{hu2022lora} ($r{=}64$, $\alpha{=}128$) with structured output jointly producing triples and evidence. RSFT selects the top-$k{=}1$ of $N{=}8$ samples by CED score (\S\ref{sec:ced}); GRPO uses group sizes $G{=}4$ (QLoRA) and $G{=}8$ (bf16); DPO constructs preference pairs from CED-ranked outputs. We report Ign-F1 (primary; ignores training-set triples), Rel-F1, Evi-F1 (TP-only and joint per DREEAM protocol~\citep{ma2023dreeam}), and EDCR (\S\ref{sec:edcr}). Detailed hyperparameters appear in the Appendix.
8	
9	
10	\subsection{Main Results}
11	\label{sec:main_results}
12	
13	Table~\ref{tab:main} presents the primary comparison on Qwen3-4B. The SFT baseline exhibits high seed sensitivity (mean Ign-F1 43.58, std 3.80pp, range 39.74--47.34). Removing evidence entirely (no-evidence SFT, s42) reaches 47.21 Ign-F1.
14	
15	RSFT CED achieves 44.82 Ign-F1 (+1.24 over SFT mean) with substantially lower variance (std 0.51pp), though these reflect different sources of variation (Section~\ref{sec:scaling}). Even the weakest RSFT seed (44.23) exceeds the SFT mean. Evidence quality improves (Evi-F1 80.96 vs.\ 79.61) and coupling tightens (EDCR 0.6487 vs.\ 0.6797). Per-seed results appear in Appendix~\ref{sec:ablation_full}.
16	
17	\begin{table}[t]
18	\centering
19	\caption{Main results on DocRED dev (Qwen3-4B). Ign-F1 shows mean $\pm$ std$^{(\text{seeds})}$; other metrics are same-seed means. Best \textbf{bold}; best evidence-generating \underline{underlined}. Per-seed: Appendix~\ref{tab:ablation_full}.}
20	\label{tab:main}
21	\small
22	\resiz
…[truncated 9856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-24T22:51:19.121359+00:00_

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
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
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

_source line 227 · 2026-05-24T22:51:19.172061+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-24T22:51:33.612409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-24T22:51:34.064326+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Document-Level Relation Extraction}
5	\label{sec:rw_docre}
6	
7	Document-level relation extraction (DocRE) requires reasoning across sentence boundaries to identify relations between entity pairs.
8	DocRED \citep{yao2019docred} established the first large-scale benchmark for this task, catalyzing a line of encoder-based methods that treat DocRE as classification over entity pair representations.
9	ATLOP \citep{zhou2021atlop} introduced adaptive thresholding with localized context pooling, and graph-based methods such as GAIN \citep{zeng2020gain} model inter-sentence reasoning through heterogeneous mention-level and entity-level graphs.
10	
11	A parallel thread incorporates sentence-level evidence into these architectures.
12	SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary training signal and showed that joint evidence prediction improves extraction through data augmentation and ensemble inference.
13	DREEAM \citep{ma2023dreeam} extended this approach with dynamic memory-based evidence retrieval that guides attention to supporting sentences.
14	EIDER \citep{xie2022eider} jointly trains an evidence extractor and fuses evidence representations into the relation classifier.
15	In all three systems, evidence identification is binary sentence classification over a fixed candidate set, a formulation that adds no output complexity.
16	
17	Recent work has recast DocRE for large language models.
18	AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge
…[truncated 4295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-24T22:51:34.064915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-24T22:51:34.569767+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We formalize evidence-grounded document-level relation extraction as a structured generation task and compare three post-training paradigms across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax is not a fixed penalty but a landscape shaped by capacity, optimization paradigm, and data quality filtering.
5	RSFT improves mean extraction across all tested scales and reduces training variance at every evaluated configuration; a 1.7B RSFT model approaches 8B SFT performance at 4.7$\times$ fewer parameters. Future work should investigate targeted evidence rewards during gradient-based training and extend evaluation to non-Wikipedia domains.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-24T22:51:34.620402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-24T22:51:35.072380+00:00_

1	\section{Limitations}
2	
3	\paragraph{Data and architecture scope.}
4	We evaluate on two datasets (DocRED, Re-DocRED), both derived from Wikipedia; cross-domain evaluation is constrained by the absence of evidence-annotated DocRE datasets beyond Wikipedia, a limitation shared by all prior evidence-aware work (SAIS, DREEAM, EIDER).
5	Evidence tax patterns span two model families (Qwen3, LLaMA) with single hyperparameter settings per RL method; other architectures, scales beyond 14B, or alternative KL coefficients may produce different decoupling behaviors.
6	
7	\paragraph{CED scoring sensitivity.}
8	CED scoring operates at the document level using an external NLI model (DeBERTa-v3); sensitivity to other NLI model families is unexplored, and sentence-level CED filtering disrupts co-reference chains (Evi-F1 $-$7.7pp).
9	
10	\paragraph{RSFT mechanistic explanation.}
11	Our explanation for why RSFT avoids decoupling---that discrete selection cannot exploit the extraction--evidence trade-off---is structural rather than empirical. We have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit data augmentation through candidate diversity, or from both. Disentangling these factors would require controlled experiments with fixed training data quality but varied selection mechanisms.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-24T22:51:35.123087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-24T22:51:35.625634+00:00_

1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B with LoRA. A dash indicates non-applicable parameters. \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (\S\ref{sec:spectrum}).}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{l@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	\multicolumn{6}{l}{\textit{Model \& Adapter}} \\
16	\quad LoRA rank $r$ / $\alpha$ & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 \\
17	\quad Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
18	\midrule
19	\multicolumn{6}{l}{\textit{Optimization}} \\
20	\quad Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
21	\quad Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
22	\quad Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	\quad Epochs / Max steps & 3 / -- & 3 / -- & -- / 100 & -- / 100 & 1, 3\textsuperscript{$\star$} / -- \\
24	\midrule
25	\multicolumn{6}{l}{\textit{RL / Selection}} \\
26	\quad Group size $G$ & -- & -- & 4 & 8 & -- \\
27	\quad KL coeff.\ / $\beta$ & -- & -- & 0.01 & 0.01 & 0.1 \\
28	\quad Candidates $N$ / Top-$k$ & -- & 8 / 1 & -- & -- & 8 / -- \\
29	\midrule
30	\multicolumn{6}{l}{\textit{Data}} \\
31	\quad Max new tokens & 1024 & 1024 & 1024 &
…[truncated 40825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-24T22:51:35.626132+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-24T22:51:35.677906+00:00_

1	- id: "W1"
2	  summary: "GRPO confounded variables + collapse mechanism lacks depth"
3	  category: experiment
4	  severity: warning
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 2
8	  mentions:
9	    - {round: 1, reviewers: "R1,R2", note: "Cannot support causal attribution of decoupling to QLoRA"}
10	    - {round: 2, reviewers: "R1,R2", note: "R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor."}
11	  action_items:
12	    - {round: 1, action: "Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect", assigned_to: "Agent", status: "done"}
13	    - {round: 1, action: "Downgrade causal claim to observational", assigned_to: "Paper Agent", status: "done"}
14	    - {round: 2, action: "Deepen GRPO mechanism analysis: add reward hacking lit (Gao et al. 2023), QuRL quantized-actor divergence, explicit mechanistic chain (QLoRA→constrained params→reward shortcut→decoupling)", assigned_to: "Paper Agent", status: "done"}
15	  resolution: ""
16	  resolution_round: null
17	
18	- id: "W2"
19	  summary: "All results dev-set only, no test set"
20	  category: experiment
21	  severity: critical
22	  status: resolved
23	  first_raised_round: 1
24	  last_seen_round: 2
25	  mentions:
26	    - {round: 1, reviewers: "R1,R2", note: "No CodaLab test results"}
27	    - {round: 2, reviewers: "R1,R2", note: "Test set results now exist (Table 9). Method ranking preserved (ρ=1.0)."}
28	  action_items:
29	    - {round: 1, action: "Add test set evaluation for all scales", assigned_to: "Agent+User", status: "done"}
30	  resolution: "Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0)."
31	  resolution_round: 2
32	
33	- id: "W3"
34	  summary: "n=3 variance compression claim statistically unreliable"
35	  category: experiment
36	  severity: critical
37	  status: in_progress
38	  first_raised_round: 1
39	  last_
…[truncated 19735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-24T22:51:55.703580+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool call

_source line 239 · 2026-05-24T22:51:55.805665+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 240 · 2026-05-24T22:51:56.716610+00:00_

{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (370 个)\n\n- **mvp2_eval_lr5e6_r1_ckpt20**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_step90**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_step100**: DONE (negative) — \n- **mvp2_eval_ced_kl001_r4_ckpt10**: DONE (success) — \n- **mvp2_eval_ced_kl001_r4_early**: DONE (negative) — \n- **mvp2_grpo_flatnli_r6**: DONE (negative) — \n- **mvp2_grpo_ced_kl001_r4**: DONE (success) — \n- **mvp2_sft_eval_r3**: DONE (success) — \n- **mvp2_grpo_extract_r3**: DONE (negative) — \n- **mvp2_grpo_ced_r5**: DONE (negative) — \n- **mvp2_sft_eval_r2**: DONE (success) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d158_14b_rsft_s44_generate | 14B seed=44 candidate generation for 3-seed statistical robustness. Replicates plan017_14b_rsft_s43_generate parameters with seed=44 SFT adapter. | — | — | — |\n\n## 待处理\n- test_eval_4b_rsft_s44_no_evi_v2: 4B RSFT CED k=1 s44 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s44 with-evi ign_f1=0.2525 计算 evidence tax。s42 tax=+1.51pp, s43 tax=+1.99pp。3-seed mean±std 完善 4B evidence tax。v1 因 conda 未激活 EXIT_CODE=127 失败，本次修复。（准备中）\n\n## 近期结论\n- **d102_1_7b_k1_s42** (success): D102 method correction: Qwen3-1.7B RSFT eval using k=1 CED (matching paper methodology) instead of k=3\n- **d102_llama_k1_s42** (success): D102 method correction: LLaMA-8B RSFT eval using k=1 CED (matching paper methodology) instead of k=3\n- **d158_1_7b_rsft_s44_ced_score** (success): 1.7B seed=44 CED/NLI scoring + k=1 selection. 对 24216 个生成样本进行 CED 评分并筛选 top-1。预期保留 ~3021 样本（与 s42/s43 一致）。D158 强制检查点：保留数与 3021 差异 >10% 则暂停 A3。 ← 基于 d158_1_7b_rsft_s44_generate\n\n## 趋势\n成功 234 / 负向 23 / 失败 65 / 共 368\n\n## 下一步\n（无活跃 idea，请通过 ide
…[truncated 2530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1013
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-24T22:51:56.767539+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 159\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_rewa
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-24T22:52:04.659261+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-24T22:52:04.710482+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-24T22:52:17.881187+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-24T22:52:17.982428+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-24T22:52:28.936349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/constraints.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/constraints.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-24T22:52:28.987035+00:00_

1	_next_id: 6
2	constraints:
3	- id: C001
4	  added: 2026-05-15 21:52 UTC
5	  summary: 提交 eval 前必须 nvidia-smi 确认目标 GPU 显存占用 < 2GB，否则不提交、换卡或等待
6	  scope: worker
7	  reason: 本 session 已 5 次因 eval 提交到被占用 GPU 导致 OOM，修复 eval 也因此作废。eval 推理需要接近全部显存，与训练共享必然
8	    OOM。
9	  decision_id: D064
10	- id: C002
11	  added: 2026-05-16 00:23 UTC
12	  summary: 提交训练/评估任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map="auto" 自动分配 GPU
13	  scope: worker
14	  reason: plan_011 和 rsft_ced_s45_train_r3 两次因未设 CUDA_VISIBLE_DEVICES 导致 device_map="auto"
15	    跨 GPU 分布，造成 OOM 和资源冲突。已知 bug 重复发生。
16	- id: C003
17	  added: 2026-05-16 00:23 UTC
18	  summary: 提交训练任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map="auto" 自动分配 GPU
19	  scope: worker
20	  reason: plan_011 和 rsft_ced_s45_train_r3 均因未设 CUDA_VISIBLE_DEVICES 导致模型跨 GPU 分布，造成
21	    OOM 或显存冲突。已重复发生两次。
22	- id: C004
23	  added: 2026-05-16 00:29 UTC
24	  summary: Registry 标记 killed 时必须同时 kill -9 PID 并 ps 验证进程已终止，否则 killed 状态不可信
25	  scope: all
26	  reason: rsft_ced_s45_train_r2 (PID 276148) registry 标记 killed 但进程未实际终止，占用 cuda:2
27	    31.6GB 导致 r3 OOM。plan_011 也有类似模式。Reviewer WARNING。
28	- id: C005
29	  added: 2026-05-16 11:15 UTC
30	  summary: no-evidence 模型 eval 必须传 --no_evidence 参数，确保推理时使用 NO_EVIDENCE_SYSTEM_PROMPT
31	    与训练一致
32	  scope: all
33	  reason: 'plan_006 1.7B/8B no-evidence eval 漏传该参数，导致训练/推理提示词不匹配（模型被要求输出未训练过的 evidence
34	    字段），结果全部无效。Reviewer critical #20。'
35	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-24T22:53:00.299322+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "faith-evidence-ie",
  "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "faith-evidence-ie",
    "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-24T22:53:22.633763+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22334
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-24T22:53:23.086672+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "3",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计声明**。\n\n## 论文信息\n- 标题：Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n- 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 通过 ARR）\n- 正文 ≤ 8 页 + 无限参考文献\n- Limitations 必填（≤1 页，不计入页数限制）\n- Double-blind 匿名审稿\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Long/Short 走同一审稿系统\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n1. **EDCR 指标有效性**：EDCR 与 Rel-F1 共享 TP 组分，cross-method ρ 是否有 mechanical correlation 问题？partial correlation 是否充分控制了 shared component？per-relation 分析（n=76）是否足够独立？permutation test 是否令人信服？\n2. **Variance compression 统计可靠性**：n=3 seeds 下的方差压缩声明——χ² CI、Cohen's d、sign test 是否足够支撑\"consistently reduces\"的结论？95% CI 宽度是否令人担忧？\n3. **Evidence tax 因果推断**：1.7B evidence tax 为负（beneficial）——implicit regularization 假说是否有足够证据？matched@2048 fair subset 方法是否充分控制了 confounds？4B/8B near-neutral tax 的 n=3 是否足以排除噪声？\n4. **GRPO/DPO 实验设计**：GRPO 只测了 KL=0.01，DPO 只测了 β=0.1——hyperparameter exploration 是否充分？QLoRA vs bf16 的 confound（quantization precision vs group size）是否充分隔离？DPO checkpoint 重建是否引入了方法论问题？\n5. **RSFT 机制解释**：paper 称 discrete selection \"cannot exploit the trade-off\"——这是结构性论证还是需要实证验证？random selection baseline（41.14 vs 44.66）能否证明 CED scoring 而非 selection 本身驱动改进？\n6. **Test set evaluation**：~20pp dev-test gap 归因于 annotation density（2.82×）——是否令人信服？14B RSFT test 出现 reversal（Δ=-0.37pp）——如何解释？\n\n请完整阅读论文（main.tex 所有 sections + appendix），给出结构化审稿意见（Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment + 置信度 + 分数）。对每个 Weakness 标注严重程度（CRITICAL / MAJOR / MINOR）。",
  "project": "faith-evidence-ie",
  "chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "3",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计声明**。\n\n## 论文信息\n- 标题：Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n- 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 通过 ARR）\n- 正文 ≤ 8 页 + 无限参考文献\n- Limitations 必填（≤1 页，不计入页数限制）\n- Double-blind 匿名审稿\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Long/Short 走同一审稿系统\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n1. **EDCR 指标有效性**：EDCR 与 Rel-F1 共享 TP 组分，cross-method ρ 是否有 mechanical correlation 问题？partial correlation 是否充分控制了 shared component？per-relation 分析（n=76）是否足够独立？permutation test 是否令人信服？\n2. **Variance compression 统计可靠性**：n=3 seeds 下的方差压缩声明——χ² CI、Cohen's d、sign test 是否足够支撑\"consistently reduces\"的结论？95% CI 宽度是否令人担忧？\n3. **Evidence tax 因果推断**：1.7B evidence tax 为负（beneficial）——implicit regularization 假说是否有足够证据？matched@2048 fair subset 方法是否充分控制了 confounds？4B/8B near-neutral tax 的 n=3 是否足以排除噪声？\n4. **GRPO/DPO 实验设计**：GRPO 只测了 KL=0.01，DPO 只测了 β=0.1——hyperparameter exploration 是否充分？QLoRA vs bf16 的 confound（quantization precision vs group size）是否充分隔离？DPO checkpoint 重建是否引入了方法论问题？\n5. **RSFT 机制解释**：paper 称 discrete selection \"cannot exploit the trade-off\"——这是结构性论证还是需要实证验证？random selection baseline（41.14 vs 44.66）能否证明 CED scoring 而非 selection 本身驱动改进？\n6. **Test set evaluation**：~20pp dev-test gap 归因于 annotation density（2.82×）——是否令人信服？14B RSFT test 出现 reversal（Δ=-0.37pp）——如何解释？\n\n请完整阅读论文（main.tex 所有 sections + appendix），给出结构化审稿意见（Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment + 置信度 + 分数）。对每个 Weakness 标注严重程度（CRITICAL / MAJOR / MINOR）。",
    "project": "faith-evidence-ie",
    "chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-24T22:53:42.930838+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19844
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-24T22:53:43.081831+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "3",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 相关工作 + 写作质量**。\n\n## 论文信息\n- 标题：Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n- 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 通过 ARR）\n- 正文 ≤ 8 页 + 无限参考文献\n- Limitations 必填（≤1 页，不计入页数限制）\n- Double-blind 匿名审稿\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Long/Short 走同一审稿系统\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n1. **贡献定位与新颖性**：三个 contributions 均为 empirical observations（evidence tax scale-dependent, gradient decoupling spectrum, RSFT variance compression）——这对 EMNLP 长文是否足够？empirical study 定位是否清晰？是否存在 method-innovation 过度暗示？CED 作为 scoring function 的定位——是工具还是贡献？\n2. **相关工作覆盖**：检查以下领域覆盖是否完整——(a) LLM-based DocRE（AutoRE, LMRC, GLiDRE, RelPrior, Ru-LLM, DocKS-RAG）是否有遗漏？(b) Evidence faithfulness（SummaC, DRIFT, SRVF, EvidenceRL）是否充分？(c) RSFT/rejection sampling（STaR, RFT, RAFT, RSFT≈PPO, RIFT, TrajFusion）是否完整？(d) RL for structured generation 的最新工作（R1-RE, REAR, DAPO, Dr.GRPO, μ-GRPO, Tree-GRPO, MO-GRPO, GDPO）是否覆盖？(e) 是否有重要相关工作被遗漏——用 web search 验证\n3. **写作质量与可读性**：abstract 是否 ≤200 words？叙事线是否清晰（gap → formalization → comparison → findings）？Table/Figure 密度和信息价值是否合适？Appendix 是否组织良好？\n4. **格式合规检查**：(a) 正文是否 ≤8 页？(b) Limitations 是否存在且 ≤1 页？(c) 匿名是否完整（无作者信息泄露）？(d) 参考文献格式是否一致（natbib/acl_natbib.bst）？(e) 是否有 ethical considerations？\n5. **完整性审查**：实验覆盖是否充分？五个模型规模（1.7B/4B/8B/14B + LLaMA-8B）是否形成完整 scaling picture？两个数据集（DocRED + Re-DocRED）是否足以支持 generalization 声明？test set evaluation 是否充分？\n6. **Claim-evidence 对齐**：每个主要声明是否都有充分的实验支持？abstract 中的数字是否与正文/表格一致？\n\n请完整阅读论文（main.tex 所有 sections + appendix），给出结构化审稿意见（Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment + 置信度 + 分数）。对每个 Weakness 标注严重程度（CRITICAL / MAJOR / MINOR）。",
  "project": "faith-evidence-ie",
  "chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "3",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 相关工作 + 写作质量**。\n\n## 论文信息\n- 标题：Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction\n- 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_round_3/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 通过 ARR）\n- 正文 ≤ 8 页 + 无限参考文献\n- Limitations 必填（≤1 页，不计入页数限制）\n- Double-blind 匿名审稿\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Long/Short 走同一审稿系统\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n1. **贡献定位与新颖性**：三个 contributions 均为 empirical observations（evidence tax scale-dependent, gradient decoupling spectrum, RSFT variance compression）——这对 EMNLP 长文是否足够？empirical study 定位是否清晰？是否存在 method-innovation 过度暗示？CED 作为 scoring function 的定位——是工具还是贡献？\n2. **相关工作覆盖**：检查以下领域覆盖是否完整——(a) LLM-based DocRE（AutoRE, LMRC, GLiDRE, RelPrior, Ru-LLM, DocKS-RAG）是否有遗漏？(b) Evidence faithfulness（SummaC, DRIFT, SRVF, EvidenceRL）是否充分？(c) RSFT/rejection sampling（STaR, RFT, RAFT, RSFT≈PPO, RIFT, TrajFusion）是否完整？(d) RL for structured generation 的最新工作（R1-RE, REAR, DAPO, Dr.GRPO, μ-GRPO, Tree-GRPO, MO-GRPO, GDPO）是否覆盖？(e) 是否有重要相关工作被遗漏——用 web search 验证\n3. **写作质量与可读性**：abstract 是否 ≤200 words？叙事线是否清晰（gap → formalization → comparison → findings）？Table/Figure 密度和信息价值是否合适？Appendix 是否组织良好？\n4. **格式合规检查**：(a) 正文是否 ≤8 页？(b) Limitations 是否存在且 ≤1 页？(c) 匿名是否完整（无作者信息泄露）？(d) 参考文献格式是否一致（natbib/acl_natbib.bst）？(e) 是否有 ethical considerations？\n5. **完整性审查**：实验覆盖是否充分？五个模型规模（1.7B/4B/8B/14B + LLaMA-8B）是否形成完整 scaling picture？两个数据集（DocRED + Re-DocRED）是否足以支持 generalization 声明？test set evaluation 是否充分？\n6. **Claim-evidence 对齐**：每个主要声明是否都有充分的实验支持？abstract 中的数字是否与正文/表格一致？\n\n请完整阅读论文（main.tex 所有 sections + appendix），给出结构化审稿意见（Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment + 置信度 + 分数）。对每个 Weakness 标注严重程度（CRITICAL / MAJOR / MINOR）。",
    "project": "faith-evidence-ie",
    "chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-24T22:53:44.443590+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 254 · 2026-05-24T22:54:00.308297+00:00_

已派发：
- **视觉审查 Agent**：已启动（fire-and-forget，不阻塞）
- **Reviewer 1**（方法严谨性 + 实验设计）：已派发
- **Reviewer 2**（新颖性 + 完整性 + 相关工作）：已派发

等待两位 Reviewer 返回独立审稿意见，收齐后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 255 · 2026-05-24T23:01:29.094556+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — Round 3 (方法严谨性 + 实验设计 + 统计声明)

**论文**: Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction
**Venue**: EMNLP 2026 via ARR

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)

**一句话总结**: 系统性实验设计和新颖观察（scale-dependent evidence tax, decoupling spectrum）是有价值的贡献，但多个核心声明的统计证据不足（n=3 方差、单 seed 税率、GRPO 混淆变量），且 14B test reversal 削弱了泛化性论述。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 主要 claim 有方向性支持但统计证据薄弱：方差压缩 n=3 + CI 重叠 3/4 scales；evidence tax threshold 依赖 n=1 seeds；GRPO 实验存在未隔离的混淆变量 |
| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 是有趣的新观察；但实际影响受限于 Wikipedia-only 数据集和 RSFT 对 evidence quality 无改善 |
| Reproducibility | 4/5 | Appendix 详尽（hyperparameters, per-seed results, error analysis），但 CED 实现细节（hypothesis verbalization template）未完整给出 |
| Confidence | 4/5 | 我仔细阅读了全文及附录，此领域在我的专业范围内 |

---

## Must-Fix 问题（影响接收决定）

**N1** [CRITICAL] GRPO QLoRA vs bf16 实验存在未隔离的混淆变量

- 具体位置：Section 4.3, Table 13 (Appendix I)
- 问题：Paper 将 GRPO catastrophic collapse 归因于 "quantization precision rather than group size as the primary factor"（Section 4.3），但两个配置同时改变了 **两个** 变量：quantization（NF4 4-bit vs bf16）**和** group size（G=4 vs G=8）。没有控制实验（QLoRA G=8 或 bf16 G=4）来隔离这两个因素。
- 为什么影响接收：Decoupling spectrum 是本文核心贡献之一。如果 catastrophic collapse 是由 G=4（过小的 group size 导致高 variance advantage estimates）而非 quantization 造成的，则整个 "quantization-constrained precision" 叙事需要修改。Paper 引用了 \citet{li2026qurl} 的 quantized-actor divergence 来支持 quantization 解释，但这是一个没有控制实验支撑的类比。
- 建议修改方向：（1）增加 bf16 G=4 实验以隔离 group size 效应；或（2）将结论从 "quantization precision...as the primary factor" 降级为 "quantization and/or group size"，承认无法区分两个因素。

**N2** [CRITICAL] 方差压缩声明的统计证据不足（n=3 seeds）

- 具体位置：Section 4.4, Table 6 (Appendix D), Abstract
- 问题：
  - 4/4 scales 中仅 1.7B 的 χ² CI 不重叠（SFT lower 1.45 > RSFT upper 0.54）。其余 3 个 scale 的 CI 均重叠。
  - Sign test p=0.0625（one-sided），不满足 α=0.05 显著性水平。Paper 自己说 "underpowered"。
  - Cohen's d 在 4B 仅为 0.46（small effect）。
  - Abstract 中 "consistently reduces training seed variance" 和 "complete pairwise seed separation on LLaMA, Cohen's d=2.58; non-overlapping χ² confidence intervals at 1.7B" 选择性报告了最强结果（cherry-picking）。
- 为什么影响接收：这是本文三大 contribution 之一。"Consistently reduces" 在统计上不成立——方向一致但缺乏统计显著性。n=3 的 χ² CI 宽度极大（例如 SFT 4B: [1.98, 23.89]），几乎没有 discriminative power。
- 建议修改方向：（1）将 "consistently reduces" 改为 "shows a consistent directional pattern with statistical significance only at the 1.7B scale"；（2）Abstract 中展示全景而非选择最强结果；（3）增加 seeds 数量（至少 n=5）以获得有意义的 CI。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [MAJOR] Evidence tax 因果推断——implicit regularization 假说证据不足

- 具体位置：Section 4.4, Appendix E (Table 7), Introduction
- 问题：1.7B evidence tax 为负（-5.63pp），paper 提出 "implicit regularization hypothesis"——evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition。但 Table 16 (Appendix N) 显示 1.7B with-evidence 模型只生成 25.5k predictions vs no-evidence 的 44.6k（1.75×差异）。这意味着有一个更简单的替代解释：evidence 格式使每个 triple 的 output 更长，从而限制了总 prediction 数量，机械性地减少了 duplication 和 FP，提高了 precision-heavy 指标（Ign-F1）。Paper 说 "partly through halving output duplication"（Introduction），但未量化这个 mechanical 效应与 "真正的 regularization" 效应的相对贡献。
- 建议：（1）在 matched prediction count 条件下重新计算 evidence tax（例如，将 no-evidence 模型的 predictions 截断到与 evidence 模型相同的数量，再比较 Ign-F1）；（2）或者将 "implicit regularization" 降级为 "output constraint effect" 并明确承认无法区分因果机制。

**W2** [MAJOR] GRPO/DPO 超参数探索不足

- 具体位置：Section 3.3, Table 3 (Appendix A)
- 问题：GRPO 只测试了 KL=0.01，DPO 只测试了 β=0.1。这些是默认值但可能不适合 evidence-grounded DocRE 的 multi-objective setting。DPO 1-epoch 的 Rel-F1 就已从 SFT 的 44.39 暴跌到 33.37（-11pp），这在 DPO 文献中是异常大的 degradation，更可能是 β 选择不当而非 DPO 的固有限制。如果 β=0.01 或 β=0.5 能维持更好的 extraction，则 "DPO gradual degradation" 的结论不成立。
- 为什么重要：Decoupling spectrum（GRPO catastrophic → DPO gradual → RSFT none）是本文核心贡献。如果 GRPO/DPO 端是因为超参数选择不当而非方法论限制，则 spectrum 的概括性被严重削弱。
- 建议：至少对 DPO β ∈ {0.01, 0.1, 0.5} 和 GRPO KL ∈ {0.001, 0.01, 0.1} 做 sensitivity analysis。

**W3** [MAJOR] 14B test-set reversal 削弱泛化性

- 具体位置：Section 4.6, Table 9 (Appendix H)
- 问题：14B RSFT 在 dev 上 +3.44pp，但在 Re-DocRED test 上 Δ=-0.37pp（reversal）。Paper 的解释是 SFT 的 50.6% truncation rate 使其生成更多 candidate triples 以匹配 test set 的 2.82× 更密集的 annotation。这个解释实际上暗示了一个更深的问题：RSFT 通过 selection 偏好 compact outputs，这在 annotation-sparse 的 dev set 上有利（precision > recall），但在 annotation-dense 的 test set 上不利（需要更高 recall）。如果 RSFT 的改进部分来自匹配 dev set 的 annotation density，则其泛化性存疑。
- 建议：（1）分析 RSFT vs SFT 的 prediction count 和 precision/recall trade-off，明确 RSFT 的改进是来自更好的 extraction quality 还是更保守的 prediction strategy；（2）在不同 annotation density 条件下评估 RSFT。

**W4** [MAJOR] EDCR 与 Rel-F1 的 mechanical correlation 未被 partial correlation 充分控制

- 具体位置：Section 3.5, Appendix L
- 问题：EDCR = Σ|E_pred \ E_gold| / Σ|E_pred|。当模型产生 false-positive triples 时，这些 triple 的所有 evidence 都计入 numerator（因为 E_gold 为空）。FP triples 同时降低 Rel-F1。所以 EDCR 和 Rel-F1 通过 FP triples（extraction precision）共享因果路径。Paper 的 partial correlation 控制的是 Evi-Recall_TP，但 shared component 是通过 extraction precision/FP rate，不是 evidence recall。正确的控制变量应是 precision 或 FP rate。
  - Per-relation 分析（n=76）部分缓解了这个问题，但各 relation type 的数据来自相同 documents，不完全独立。Permutation test 假设一定程度的独立性，可能过于乐观。
- 建议：（1）在 partial correlation 中控制 per-relation precision 而非 Evi-Recall_TP；（2）讨论 per-relation 数据点的 non-independence（shared documents）对 permutation test 的影响。

**W5** [MAJOR] RSFT 的 "cannot exploit the trade-off" 论证是结构性的而非实证的

- 具体位置：Section 2.3 (Related Work), Appendix G
- 问题：Paper 声称 "discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods discover"。这在逻辑上是合理的（RSFT 不微分 reward signal），但 paper 自己在 Limitations 中承认这是 "structural rather than empirical"。缺少的关键实验是：固定 training data quality 但改变 selection mechanism（例如用 Rel-F1-only scoring 或 Evi-F1-only scoring 做 RSFT），看是否出现 decoupling。如果 Rel-F1-only RSFT 也不 decouple，则 "discrete selection" 解释成立；如果它 decouples（牺牲 evidence），则 CED 的 joint scoring 才是关键而非 selection 机制本身。
- 此外，random selection baseline（41.14 Ign-F1）的比较基准是 SFT s42（39.74，最弱 seed）。对比 SFT 3-seed mean（43.58），random RSFT 实际上 **更差**（-2.44pp），仅 CED RSFT 有改善。这说明 "selection 本身" 的贡献可能为负，CED scoring 才是驱动因素。
- 建议：（1）增加 Rel-F1-only RSFT 和 Evi-F1-only RSFT 实验；（2）random baseline 应对比 SFT multi-seed mean 而非最弱 seed。

---

## 小问题（不影响接收）

**M1** [MINOR] 页数边界情况：Main text（Sections 1-5, 含 Conclusion）略微超出 page 8 进入 page 9 顶部（约 8-10 行）。Limitations 和 References 不计入页数限制，但 Conclusion 计入。建议压缩 Discussion (4.7) 或 Conclusion (5) 以严格控制在 8 页内。

**M2** [MINOR] Decoupling spectrum 仅在 Qwen3-4B 上验证。未在其他 scale 或 LLaMA 上测试 GRPO/DPO，无法确认 spectrum 是否在不同 capacity/architecture 下 hold。

**M3** [MINOR] Table 1 (Main Results) 的 SFT no-evidence 仅报告 s42 单个 seed（47.21），而 SFT with-evidence 报告 3-seed mean（43.58±3.80）。最强 SFT seed（s43: 47.34）超过 RSFT mean（44.82），使 "RSFT improves over SFT" 的结论取决于 seed 选择。建议为 no-evidence SFT 也报告 multi-seed 结果。

**M4** [MINOR] CED hypothesis verbalization 的具体 template（"$e_h$ has relation $r$ with $e_t$"）对不同 relation type 可能有不同的自然程度。未讨论 verbalization template 对 NLI 评分的 sensitivity。

**M5** [MINOR] 4B 的 training-time evidence tax 报告为 "+0.25±0.47pp, n=3"，但 inference-time tax（同一 RSFT model with/without evidence）报告为 "+0.94"（Table 2）。这两种 tax 的定义不同（training-time: 不同模型; inference-time: 同一模型不同输出格式），但 paper 在不同位置混用时没有足够清晰地区分。

---

## 主要优势

1. **系统性实验覆盖**：3 optimization paradigms × 4+ model scales × 2 model families × 2 datasets × multiple seeds，在 LLM-based IE 领域是罕见的覆盖广度。
2. **Novel observations**：Scale-dependent evidence tax（1.7B beneficial, ≥4B neutral）和 decoupling spectrum 是有价值的经验发现，即使统计证据需要加强。
3. **透明度高**：Paper 主动讨论了 EDCR mechanical correlation、variance CI overlap、RSFT mechanistic caveat 等 limitations，显示出作者的诚实态度。
4. **实用价值**：1.7B RSFT（51.19 Ign-F1, std 0.09pp）接近 8B SFT（50.19, std 3.23pp）在 4.7× 更少参数下，对部署有实际意义。
5. **Thorough appendix**：11 个 appendix sections 提供了详尽的 ablation、error analysis、qualitative examples，极大增强了可重复性。
6. **RSFT 对 evidence-grounded DocRE 的成功应用**：虽然 RSFT 本身不是新方法，但将其应用于 evidence-grounded IE 并用 CED 作为 domain-specific filter 是合理且有效的。

---

## Missing References

未发现明显遗漏的关键参考文献。Related Work 覆盖了 DocRE（ATLOP, GAIN, SAIS, DREEAM, EIDER, AutoRE 等）、RL for structured generation（GRPO, DPO, PPO 及其变体）、和 evidence faithfulness（NLI-based scoring, STaR, RAFT）三个主要方向。

---

## 总结

本文提出了一个 well-structured 的研究问题并进行了系统性实验。Scale-dependent evidence tax 和 decoupling spectrum 是有价值的概念贡献。但核心统计声明（variance compression、evidence tax threshold、decoupling spectrum universality）的证据基础较薄——n=3 seeds、single hyperparameter settings、confounded GRPO comparison——使得 Contribution 2 和 3 的结论强度显著超过了实验证据的支撑力。14B test reversal 进一步提示 RSFT 的改进可能部分依赖于 dev/test annotation density 的匹配。建议在 rebuttal 中：（1）增加 GRPO bf16 G=4 控制实验；（2）对 DPO β 做 sensitivity analysis；（3）将方差压缩 claim 降级到与统计证据匹配的强度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 256 · 2026-05-24T23:01:41.524887+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），2 个 CRITICAL + 5 个 MAJOR。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 257 · 2026-05-24T23:01:44.019327+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference），Soundness 3/5，Excitement 3/5。

识别了 2 个 Critical 问题（GRPO QLoRA/bf16 混淆变量未隔离；n=3 方差压缩声明过强）、5 个 Major 问题（evidence tax 因果推断不足；GRPO/DPO 超参数探索有限；14B test reversal；EDCR mechanical correlation 控制不当；RSFT 结构性论证缺乏实证验证）、5 个 Minor 问题（页数边界、spectrum 仅在 4B 验证、baseline seed 选择、CED template sensitivity、tax 定义混用）。同时肯定了论文在系统性覆盖、透明度和实用价值方面的优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 258 · 2026-05-24T23:01:50.452676+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 22

## Round 22

6 recorded events


### User

_source line 259 · 2026-05-24T23:02:55.201179+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 一篇实验设计扎实的 empirical study，scale-dependent evidence tax 和 decoupling spectrum 发现有价值，但方法论贡献有限（CED ≈ flat-NLI，RSFT 为已知框架），且存在格式微瑕（abstract 超 200 words、正文疑似溢出 8 页）。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计总体严谨，多 scale/family/dataset 交叉验证充分；但 DPO 仅测试单一 β=0.1，variance 比较方法论存在可比性问题，14B 仅 1-2 seed |
| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 作为 empirical findings 有启发性，但缺乏方法论创新；CED 的 ablation 自证其无必要（vs flat-NLI 差 0.02pp） |
| Reproducibility | 4/5 | 超参数完整报告（Table 3/Appendix A），LoRA 配置清晰，per-seed 结果透明；但未提供代码/数据链接 |
| Confidence | 4/5 | 熟悉 DocRE 和 LLM RL 文献，仔细阅读了全文和附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [CRITICAL] 贡献定位模糊：empirical study 却暗示 method innovation
- 具体位置：Section 1 (Introduction), 三个 contributions (p2)
- 问题：三个 contribution 均为 empirical observation（evidence tax scale-dependent, gradient decoupling spectrum, RSFT variance compression）。RSFT 是已有框架（STaR/RFT/RAFT），论文自己承认"the contribution of RSFT in our setting is not the framework itself"（§3.3 末）。CED 作为 scoring function 被 ablation 自我否定——flat-NLI 与 CED RSFT 的 Rel-F1 差异仅 0.02pp（§4.7, Appendix B Table 4），contrastive 部分实质上无用。但论文 framing 仍然暗示方法创新（"We formalize...", "we propose the Evidence-Decoupling Ratio"），造成读者对 contribution type 的误判。
- 为什么影响接收：EMNLP 长文需要 clear contribution positioning。Empirical study 可以被接收，但需要明确定位为"an empirical investigation of..."而非混合 method-and-finding 叙事。当前 framing 可能让 reviewer/AC 认为方法创新不足，而忽视 empirical findings 的真正价值。
- 建议修改方向：(1) 将 paper 明确定位为 empirical study/benchmark study；(2) 将 CED 降级为 "scoring tool" 而非 "proposed method"，因为 ablation 已经证明 flat-NLI 等价；(3) 强调 findings 本身的独立价值（scale-dependent tax 是挑战既有假设的，decoupling spectrum 是新的分析框架）。

**N2** [MAJOR] Abstract 超过 200 words
- 具体位置：Abstract (p1)
- 问题：经计算 abstract 约 205 words（去除 LaTeX 后），超过 EMNLP 2026 ARR 的 200-word 硬限制。Abstract 过于密集，塞入了大量数字（−5.63pp, +0.25±0.47pp, Cohen's d=2.58, 51.19, 50.19, 4.7×, Spearman ρ=1.0 等），降低可读性。
- 为什么影响接收：格式违规可能导致 desk reject 或 reviewer 负面印象。
- 建议修改方向：删减具体数字（保留 1-2 个关键数字即可），将 statistical detail 移入正文。Abstract 应聚焦 what you found + why it matters，而非 how much exactly。

**N3** [MAJOR] 正文可能超过 8 页
- 具体位置：PDF p8-p9
- 问题：从 PDF 视觉检查，Section 4.7 (Discussion) 的末尾文本和 Section 5 (Conclusion) 均位于第 9 页。即主体正文（§1-§5）超出 8 页限制约 0.1-0.2 页。Limitations 和 References 不计入页数，但 Conclusion 计入。
- 为什么影响接收：8 页是硬限制，超页可能导致 desk reject。
- 建议修改方向：压缩 Discussion（当前 §4.7 内容部分与 Appendix 重复）或将部分 Figure/Table 移入 Appendix 以腾出空间。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [MAJOR] DPO 评估配置不足
- 具体位置：§4.3 (Decoupling Spectrum), Table 13 (Appendix I)
- 问题：DPO 仅测试了 β=0.1 一个配置（Table 3）。在 β=0.1 下 DPO 1-epoch Rel-F1 即暴跌至 33.37（SFT baseline 44.39），3-epoch 进一步降至 31.45。这个极端 degradation 可能是 β 选择不当导致的 artifact，而非 DPO 在 structured generation 中的固有缺陷。不同的 β 值（如 0.01 或 0.5）可能产生完全不同的 decoupling 行为。论文将此现象上升为"DPO gradual degradation"作为 decoupling spectrum 的核心 evidence，但 single-configuration 结论的 generalizability 存疑。
- 建议：至少测试 2-3 个 β 值以验证 degradation 趋势的 robustness，或在 Limitations 中明确承认这一限制。

**W2** [MAJOR] RSFT 与 SFT variance 比较方法论
- 具体位置：§4.4, Figure 5, Table 6 (Appendix D)
- 问题：论文承认 RSFT 和 SFT 的 variance "reflect different sources of variation"（§4.2），但在 abstract 和全文中仍以"RSFT consistently reduces training variance"作为核心贡献之一。SFT variance 来自独立训练 seed 的差异；RSFT variance 来自先固定一个 SFT model 再从其 8 个候选中选 top-1 后重新训练。RSFT 的 sampling-then-retraining 流程天然会压缩 variance——它本质上是对 SFT output distribution 做了平均化处理。Compression ratio（如 1.7B 的 32.6×）的实际意义需要更审慎的解读。
- 建议：(1) 更明确地讨论 variance 来源差异；(2) 考虑报告从多个不同 SFT seed 出发做 RSFT 的 variance（目前所有 RSFT 实验似乎都从同一个 SFT model 出发），这才是公平比较。

**W3** [WARNING] 14B 评估不充分
- 具体位置：Table 2 (§4.4), Table 9 (Appendix H)
- 问题：14B SFT 仅 1 个 seed，RSFT 仅 2 个 seed。在 test set 上 14B RSFT 相比 SFT 反而下降 0.37pp（Table 9），这与其他 scale 的趋势不一致。论文标题和 abstract 频繁使用"across scales"和"consistently"等措辞，但 14B 的证据薄弱。
- 建议：要么增加 14B seeds，要么在 claims 中更谨慎地限定为"three fully evaluated scales"（论文部分地方已经这样做了，但不一致）。

**W4** [WARNING] Evidence quality 未被 RSFT 改善
- 具体位置：§4.7 (Discussion), Table 14 (Appendix K)
- 问题：Error analysis 明确显示 RSFT 改善了 extraction（truncation FN -22%, hallucinated FP -8%, duplicates -20%）但 evidence quality 几乎不变（<0.4pp across all scales）。论文诚实地承认"RSFT improves what the model extracts but not how well it grounds extractions"，但这与 CED scoring 的 design motivation（基于 evidence faithfulness 做 data selection）存在张力。如果 CED 的 evidence 信号没有传导到模型行为，CED 相比 random selection 的优势主要来自 extraction quality filtering 而非 evidence quality filtering。
- 建议：在 Discussion 中更深入分析这一 disconnect——为什么 CED 中的 evidence 信号无法改善 evidence quality？这是否意味着 evidence 能力主要由 SFT 阶段决定，post-training 只能改善 extraction？

**W5** [WARNING] 缺少 DocRED 官方 test set 评测
- 具体位置：§4.6 (Generalization)
- 问题：论文仅在 Re-DocRED test set 上做了 test evaluation，未使用 DocRED 官方 test set（CodaLab leaderboard）。DocRED test set 是该领域的标准评测基准，大多数 prior work（ATLOP, SAIS, DREEAM, AutoRE, RelPrior）都在此报告结果。缺少此评测限制了与 prior work 的直接对比。
- 建议：补充 DocRED test set 结果，或在 Limitations 中明确说明未使用的原因。

---

## 小问题（不影响接收）

- **M1**: Evidence tax 方向约定不一致——Table 2 脚注定义"positive = cost"，但 Figure 7 caption 说"negative values indicate evidence benefits extraction"，Section 4.4 中"$-$5.63pp"表示 benefit。建议统一方向约定并在首次出现时明确定义。

- **M2**: Bibliography key-name 不匹配——`chen2025docksrag`（第一作者 Xu）、`xu2024lmrc`（第一作者 Li）、`wang2025rear`（第一作者 Luo）、`wang2025relprior`（第一作者 Pi）、`wang2025rullm`（第一作者 Zhang）。虽然不影响渲染输出，但暗示 bib 管理粗糙。另外 `wang2025rullm` 使用 `journal = {NLPCC 2025}` 应为 `booktitle`。`wang2025rear` 无 URL。

- **M3**: Section 4.5 (Evidence Strategy Comparison) 仅一段，与其作为独立 subsection 不如合并到 Discussion。BM25 baseline 的 $k=2$ 选择未 justify。

- **M4**: EDCR 的 cross-method correlation（§3.5, ρ=−0.89 但 §4.7 报告 ρ=−0.96, n=7）数值不一致——§3.5 报告 $\rho=-0.89, n=7, p=0.007$，而 §4.7 和 Appendix I 报告 $\rho=-0.96, n=7, p<0.001$。需要统一或解释差异（可能是不同 seed aggregation 方式）。

- **M5**: Table 3 hyperparameters 中 GRPO bf16 的 batch size 为 8，gradient accumulation 为 4，effective batch size 应为 32，但与 GRPO QLoRA（batch 4 × grad_accum 16 = 64）差异显著。这个差异的影响未讨论。

---

## Missing References 检查

已覆盖的关键工作（确认完整）：
- LLM-based DocRE: AutoRE ✓, LMRC ✓, GLiDRE ✓, RelPrior ✓, Ru-LLM ✓, DocKS-RAG ✓
- Evidence faithfulness: SummaC ✓, DRIFT ✓, SRVF ✓, EvidenceRL ✓, InFuse ✓
- RSFT/rejection sampling: STaR ✓, RFT ✓, RAFT ✓, RSFT≈PPO ✓, RIFT ✓, TrajFusion ✓
- RL for structured generation: R1-RE ✓, REAR ✓, DAPO ✓, Dr.GRPO ✓, μ-GRPO ✓, Tree-GRPO ✓, MO-GRPO ✓, GDPO ✓

可能遗漏的相关工作：
1. **DeepSeek-R1** (DeepSeek-AI et al., 2025) — GRPO 最成功的应用实例，论文仅引用了 DeepSeekMath（原始 GRPO 论文），但未提及 DeepSeek-R1。鉴于 GRPO 是论文中三个方法之一且展示了 catastrophic failure，引用 GRPO 的 flagship 成功案例有助于平衡叙事。
2. **ReST** (Gulcehre et al., 2023, "Reinforced Self-Training") — RSFT 的近亲方法，在 iterative self-improvement 文献中具有里程碑地位，但未被引用。

Related work 覆盖总体评价：**良好**。上述遗漏不构成重大缺失，但补充后会使 positioning 更完整。

---

## 主要优势

1. **实验设计全面且透明**：5 个模型规模 × 2 个 model family × 2 个数据集 × 多方法对比，per-seed 结果完整报告，few papers 在 DocRE 领域达到这一实验覆盖度。Appendix 内容详实（error analysis, per-relation EDCR, qualitative examples, inference efficiency），体现了严谨的实验态度。

2. **Scale-dependent evidence tax 是非平凡发现**：1.7B 从 evidence 中获益（−5.63pp，通过减少 duplication）而 ≥4B 近似中性——这一 finding 挑战了"evidence generation always costs accuracy"的朴素假设，且 mechanistic explanation（implicit regularization via output structure constraint, Table 7）具有说服力。

3. **Decoupling spectrum 提供了有用的分析框架**：GRPO catastrophic → DPO gradual → RSFT none 的 continuum 直观地总结了不同 optimization paradigm 在 multi-objective structured generation 中的行为差异。GRPO QLoRA 的 catastrophic collapse（Rel-F1 降至 1.38，Evi-F1 仍有 85.04）是一个令人印象深刻的 negative result。

4. **RSFT 的实际价值清晰**：1.7B RSFT（51.19 Ign-F1, std 0.09pp）接近 8B SFT（50.19, std 3.23pp），在 4.7× fewer parameters 下实现部署效率——这对资源受限场景有直接的 practical implication。

5. **写作质量整体良好**：叙事线清晰（gap → formalization → comparison → findings），technique 解释准确，Figure/Table 信息密度高但可读。§3.5 EDCR 定义和 §3.4 CED 公式表述清晰。

---

## Claim-Evidence 对齐检查

| Claim (Abstract/Intro) | 证据位置 | 对齐状态 |
|---|---|---|
| "beneficial at 1.7B (−5.63pp)" | Table 8 (Appendix F), matched@2048 | ✓ 一致 |
| "approximately neutral at ≥4B (+0.25±0.47pp)" | Table 8, three-seed mean | ✓ 一致 |
| "GRPO catastrophic" | Table 13, Rel-F1=1.38 | ✓ 一致 |
| "Cohen's d=2.58" | Table 6, LLaMA-3.1-8B | ✓ 一致（注意 abstract 说 "on LLaMA"） |
| "1.7B RSFT approaches 8B SFT (51.19 vs 50.19)" | Table 2 | ✓ 一致 |
| "Spearman ρ=1.0" | §4.6, Table 9 | ✓ 一致 |
| "RSFT consistently reduces training variance" | Figure 5, Table 6 | ⚠ 方向一致但可比性存疑（W2） |

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文 ≤8 页 | ⚠ 疑似超页 | §4.7 末尾 + §5 Conclusion 溢出至 p9 |
| Abstract ≤200 words | ✗ ~205 words | 需删减 |
| Limitations 存在 | ✓ | §6, 约 0.5 页，覆盖 3 点 |
| 匿名 | ✓ | "Anonymous ACL submission", 无信息泄露 |
| ACL 模板 [review] | ✓ | `\usepackage[review]{acl}` |
| 参考文献格式 | ⚠ | 大部分一致，个别条目有问题（M2） |
| Ethical considerations | ✓ | Appendix O: AI assistants 使用声明 |

---

**总结**：这是一篇实验功底扎实的 empirical study，核心 findings（scale-dependent tax, decoupling spectrum）对 evidence-grounded IE 社区有价值。主要短板是 (1) 方法论创新有限且 CED 被自己的 ablation 否定了独特性，(2) 格式问题需修正，(3) DPO 单配置和 RSFT variance 比较方法需加强。建议定位为 Findings 论文或在 contribution framing 上做调整后冲击 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-24T23:03:46.834697+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "3",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计总体严谨，多 scale/family/dataset 交叉验证充分；但 DPO 仅测试单一 β=0.1，variance 比较方法论存在可比性问题，14B 仅 1-2 seed |\n| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 作为 empirical findings 有启发性，但缺乏方法论创新；CED 的 ablation 自证其无必要（vs flat-NLI 差 0.02pp） |\n| Reproducibility | 4/5 | 超参数完整报告（Table 3/Appendix A），LoRA 配置清晰，per-seed 结果透明；但未提供代码/数据链接 |\n| Confidence | 4/5 | 熟悉 DocRE 和 LLM RL 文献，仔细阅读了全文和附录 |\n\n### Must-Fix 问题\n\n**N1** [CRITICAL] 贡献定位模糊：empirical study 却暗示 method innovation\n- 三个 contribution 均为 empirical observation。RSFT 是已有框架，论文自己承认\"the contribution of RSFT in our setting is not the framework itself\"（§3.3 末）。CED 被 ablation 自我否定——flat-NLI 与 CED RSFT 的 Rel-F1 差异仅 0.02pp（§4.7, Appendix B Table 4），contrastive 部分实质上无用。但论文 framing 仍然暗示方法创新（\"We formalize...\", \"we propose the Evidence-Decoupling Ratio\"）。\n- 建议：明确定位为 empirical study；将 CED 降级为 \"scoring tool\" 而非 \"proposed method\"；强调 findings 的独立价值。\n\n**N2** [MAJOR] Abstract 超过 200 words\n- 经计算约 205 words，超过 EMNLP 2026 ARR 的 200-word 硬限制。Abstract 过于密集，塞入大量数字。\n- 建议：删减具体数字，聚焦 what you found + why it matters。\n\n**N3** [MAJOR] 正文可能超过 8 页\n- §4.7 末尾和 §5 Conclusion 位于第 9 页。主体正文超出 8 页限制约 0.1-0.2 页。\n- 建议：压缩 Discussion 或移 Figure/Table 入 Appendix。\n\n### Should-Fix 问题\n\n**W1** [MAJOR] DPO 评估配置不足\n- DPO 仅测试 β=0.1。1-epoch Rel-F1 即暴跌至 33.37（SFT 44.39），可能是 β 不当导致的 artifact。\n- 建议：至少测试 2-3 个 β 值。\n\n**W2** [MAJOR] RSFT 与 SFT variance 比较方法论\n- RSFT variance 来自固定 SFT model 再 sampling-then-retraining，天然压缩 variance。所有 RSFT 实验似乎从同一 SFT model 出发，不是公平比较。\n- 建议：报告从多个 SFT seed 出发做 RSFT 的 variance。\n\n**W3** [WARNING] 14B 评估不充分\n- 14B SFT 仅 1 seed，RSFT 仅 2 seed。Test set 上 14B RSFT 反而下降 0.37pp。\n\n**W4** [WARNING] Evidence quality 未被 RSFT 改善\n- RSFT 改善 extraction 但 evidence quality 不变（<0.4pp）。CED 优于 random 可能主要来自 extraction quality filtering。\n\n**W5** [WARNING] 缺少 DocRED 官方 test set 评测\n- 仅在 Re-DocRED test set 上做了 test evaluation，未使用 DocRED CodaLab leaderboard。\n\n### 小问题\n- M1: Evidence tax 方向约定不一致\n- M2: Bibliography key-name 不匹配（chen2025docksrag 第一作者 Xu 等）\n- M3: §4.5 仅一段，BM25 k=2 未 justify\n- M4: EDCR cross-method ρ 数值不一致（§3.5 ρ=−0.89 vs §4.7 ρ=−0.96）\n- M5: GRPO bf16 vs QLoRA effective batch size 差异未讨论\n\n### Missing References\n- DeepSeek-R1（GRPO flagship 成功案例，论文仅引用 DeepSeekMath）\n- ReST（Gulcehre et al., 2023, Reinforced Self-Training）\n\n### 主要优势\n1. 实验设计全面且透明\n2. Scale-dependent evidence tax 是非平凡发现\n3. Decoupling spectrum 提供有用分析框架\n4. RSFT 实际价值清晰\n5. 写作质量整体良好\n\n---\n\n请对以上每一条逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "faith-evidence-ie",
  "chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "3",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计总体严谨，多 scale/family/dataset 交叉验证充分；但 DPO 仅测试单一 β=0.1，variance 比较方法论存在可比性问题，14B 仅 1-2 seed |\n| Excitement | 3/5 | Scale-dependent evidence tax 和 decoupling spectrum 作为 empirical findings 有启发性，但缺乏方法论创新；CED 的 ablation 自证其无必要（vs flat-NLI 差 0.02pp） |\n| Reproducibility | 4/5 | 超参数完整报告（Table 3/Appendix A），LoRA 配置清晰，per-seed 结果透明；但未提供代码/数据链接 |\n| Confidence | 4/5 | 熟悉 DocRE 和 LLM RL 文献，仔细阅读了全文和附录 |\n\n### Must-Fix 问题\n\n**N1** [CRITICAL] 贡献定位模糊：empirical study 却暗示 method innovation\n- 三个 contribution 均为 empirical observation。RSFT 是已有框架，论文自己承认\"the contribution of RSFT in our setting is not the framework itself\"（§3.3 末）。CED 被 ablation 自我否定——flat-NLI 与 CED RSFT 的 Rel-F1 差异仅 0.02pp（§4.7, Appendix B Table 4），contrastive 部分实质上无用。但论文 framing 仍然暗示方法创新（\"We formalize...\", \"we propose the Evidence-Decoupling Ratio\"）。\n- 建议：明确定位为 empirical study；将 CED 降级为 \"scoring tool\" 而非 \"proposed method\"；强调 findings 的独立价值。\n\n**N2** [MAJOR] Abstract 超过 200 words\n- 经计算约 205 words，超过 EMNLP 2026 ARR 的 200-word 硬限制。Abstract 过于密集，塞入大量数字。\n- 建议：删减具体数字，聚焦 what you found + why it matters。\n\n**N3** [MAJOR] 正文可能超过 8 页\n- §4.7 末尾和 §5 Conclusion 位于第 9 页。主体正文超出 8 页限制约 0.1-0.2 页。\n- 建议：压缩 Discussion 或移 Figure/Table 入 Appendix。\n\n### Should-Fix 问题\n\n**W1** [MAJOR] DPO 评估配置不足\n- DPO 仅测试 β=0.1。1-epoch Rel-F1 即暴跌至 33.37（SFT 44.39），可能是 β 不当导致的 artifact。\n- 建议：至少测试 2-3 个 β 值。\n\n**W2** [MAJOR] RSFT 与 SFT variance 比较方法论\n- RSFT variance 来自固定 SFT model 再 sampling-then-retraining，天然压缩 variance。所有 RSFT 实验似乎从同一 SFT model 出发，不是公平比较。\n- 建议：报告从多个 SFT seed 出发做 RSFT 的 variance。\n\n**W3** [WARNING] 14B 评估不充分\n- 14B SFT 仅 1 seed，RSFT 仅 2 seed。Test set 上 14B RSFT 反而下降 0.37pp。\n\n**W4** [WARNING] Evidence quality 未被 RSFT 改善\n- RSFT 改善 extraction 但 evidence quality 不变（<0.4pp）。CED 优于 random 可能主要来自 extraction quality filtering。\n\n**W5** [WARNING] 缺少 DocRED 官方 test set 评测\n- 仅在 Re-DocRED test set 上做了 test evaluation，未使用 DocRED CodaLab leaderboard。\n\n### 小问题\n- M1: Evidence tax 方向约定不一致\n- M2: Bibliography key-name 不匹配（chen2025docksrag 第一作者 Xu 等）\n- M3: §4.5 仅一段，BM25 k=2 未 justify\n- M4: EDCR cross-method ρ 数值不一致（§3.5 ρ=−0.89 vs §4.7 ρ=−0.96）\n- M5: GRPO bf16 vs QLoRA effective batch size 差异未讨论\n\n### Missing References\n- DeepSeek-R1（GRPO flagship 成功案例，论文仅引用 DeepSeekMath）\n- ReST（Gulcehre et al., 2023, Reinforced Self-Training）\n\n### 主要优势\n1. 实验设计全面且透明\n2. Scale-dependent evidence tax 是非平凡发现\n3. Decoupling spectrum 提供有用分析框架\n4. RSFT 实际价值清晰\n5. 写作质量整体良好\n\n---\n\n请对以上每一条逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "faith-evidence-ie",
    "chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-24T23:04:20.528089+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33693
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-24T23:04:20.930202+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "3",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness 3/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5**\n\n### Must-Fix 问题\n\n**N1** [CRITICAL] GRPO QLoRA vs bf16 实验存在未隔离的混淆变量\n- 两个配置同时改变了 quantization（NF4 4-bit vs bf16）**和** group size（G=4 vs G=8）。没有控制实验（QLoRA G=8 或 bf16 G=4）来隔离这两个因素。\n- Paper 将 collapse 归因于 \"quantization precision rather than group size as the primary factor\"（§4.3），但这是没有控制实验支撑的归因。\n- 建议：增加 bf16 G=4 实验，或将结论降级为 \"quantization and/or group size\"。\n\n**N2** [CRITICAL] 方差压缩声明的统计证据不足（n=3 seeds）\n- 4/4 scales 中仅 1.7B 的 χ² CI 不重叠。Sign test p=0.0625，不满足 α=0.05。Cohen's d 在 4B 仅为 0.46。\n- Abstract 选择性报告最强结果（cherry-picking）。\n- 建议：将 \"consistently reduces\" 改为 \"shows a consistent directional pattern with statistical significance only at 1.7B\"；增加 seeds。\n\n### Should-Fix 问题\n\n**W1** [MAJOR] Evidence tax 因果推断——implicit regularization 假说证据不足\n- 1.7B evidence 模型只生成 25.5k vs no-evidence 44.6k predictions。更简单的替代解释：evidence 格式限制总 prediction 数量，机械性减少 duplication/FP。\n- 建议：在 matched prediction count 下重新计算 tax，或降级为 \"output constraint effect\"。\n\n**W2** [MAJOR] GRPO/DPO 超参数探索不足\n- GRPO 只测 KL=0.01，DPO 只测 β=0.1。DPO 1-epoch Rel-F1 暴跌 -11pp 可能是 β 不当。\n- 建议：至少 β ∈ {0.01, 0.1, 0.5}, KL ∈ {0.001, 0.01, 0.1}。\n\n**W3** [MAJOR] 14B test-set reversal 削弱泛化性\n- 14B RSFT dev +3.44pp，test Δ=-0.37pp。RSFT 可能偏好 compact outputs，在 annotation-sparse dev 上有利但 annotation-dense test 上不利。\n- 建议：分析 precision/recall trade-off。\n\n**W4** [MAJOR] EDCR 与 Rel-F1 的 mechanical correlation 未被 partial correlation 充分控制\n- FP triples 同时影响 EDCR numerator 和 Rel-F1，正确控制变量应是 precision/FP rate 而非 Evi-Recall_TP。Per-relation 数据来自相同 documents，不完全独立。\n- 建议：控制 per-relation precision；讨论 non-independence。\n\n**W5** [MAJOR] RSFT 的 \"cannot exploit the trade-off\" 论证是结构性的而非实证的\n- 缺少 Rel-F1-only 或 Evi-F1-only RSFT 实验来验证。Random selection（41.14）对比 SFT mean（43.58）实际更差，说明 selection 本身贡献可能为负。\n- 建议：增加 single-objective RSFT 实验；random baseline 应对比 SFT multi-seed mean。\n\n### 小问题\n- M1: 正文可能超 8 页（§5 溢出至 p9）\n- M2: Decoupling spectrum 仅在 4B 验证\n- M3: SFT no-evidence 仅 s42 单 seed\n- M4: CED hypothesis verbalization template sensitivity 未讨论\n- M5: Training-time vs inference-time tax 定义混用\n\n### 主要优势\n1. 系统性实验覆盖（3 paradigms × 4+ scales × 2 families × 2 datasets × multiple seeds）\n2. Novel observations（scale-dependent tax, decoupling spectrum）\n3. 透明度高（主动讨论 limitations）\n4. 实用价值（1.7B RSFT ≈ 8B SFT at 4.7× fewer params）\n5. Thorough appendix（11 sections）\n6. RSFT + CED 组合在 evidence-grounded DocRE 中的有效应用\n\n### Missing References\n未发现明显遗漏。\n\n---\n\n请对以上每一条逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "faith-evidence-ie",
  "chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "3",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness 3/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5**\n\n### Must-Fix 问题\n\n**N1** [CRITICAL] GRPO QLoRA vs bf16 实验存在未隔离的混淆变量\n- 两个配置同时改变了 quantization（NF4 4-bit vs bf16）**和** group size（G=4 vs G=8）。没有控制实验（QLoRA G=8 或 bf16 G=4）来隔离这两个因素。\n- Paper 将 collapse 归因于 \"quantization precision rather than group size as the primary factor\"（§4.3），但这是没有控制实验支撑的归因。\n- 建议：增加 bf16 G=4 实验，或将结论降级为 \"quantization and/or group size\"。\n\n**N2** [CRITICAL] 方差压缩声明的统计证据不足（n=3 seeds）\n- 4/4 scales 中仅 1.7B 的 χ² CI 不重叠。Sign test p=0.0625，不满足 α=0.05。Cohen's d 在 4B 仅为 0.46。\n- Abstract 选择性报告最强结果（cherry-picking）。\n- 建议：将 \"consistently reduces\" 改为 \"shows a consistent directional pattern with statistical significance only at 1.7B\"；增加 seeds。\n\n### Should-Fix 问题\n\n**W1** [MAJOR] Evidence tax 因果推断——implicit regularization 假说证据不足\n- 1.7B evidence 模型只生成 25.5k vs no-evidence 44.6k predictions。更简单的替代解释：evidence 格式限制总 prediction 数量，机械性减少 duplication/FP。\n- 建议：在 matched prediction count 下重新计算 tax，或降级为 \"output constraint effect\"。\n\n**W2** [MAJOR] GRPO/DPO 超参数探索不足\n- GRPO 只测 KL=0.01，DPO 只测 β=0.1。DPO 1-epoch Rel-F1 暴跌 -11pp 可能是 β 不当。\n- 建议：至少 β ∈ {0.01, 0.1, 0.5}, KL ∈ {0.001, 0.01, 0.1}。\n\n**W3** [MAJOR] 14B test-set reversal 削弱泛化性\n- 14B RSFT dev +3.44pp，test Δ=-0.37pp。RSFT 可能偏好 compact outputs，在 annotation-sparse dev 上有利但 annotation-dense test 上不利。\n- 建议：分析 precision/recall trade-off。\n\n**W4** [MAJOR] EDCR 与 Rel-F1 的 mechanical correlation 未被 partial correlation 充分控制\n- FP triples 同时影响 EDCR numerator 和 Rel-F1，正确控制变量应是 precision/FP rate 而非 Evi-Recall_TP。Per-relation 数据来自相同 documents，不完全独立。\n- 建议：控制 per-relation precision；讨论 non-independence。\n\n**W5** [MAJOR] RSFT 的 \"cannot exploit the trade-off\" 论证是结构性的而非实证的\n- 缺少 Rel-F1-only 或 Evi-F1-only RSFT 实验来验证。Random selection（41.14）对比 SFT mean（43.58）实际更差，说明 selection 本身贡献可能为负。\n- 建议：增加 single-objective RSFT 实验；random baseline 应对比 SFT multi-seed mean。\n\n### 小问题\n- M1: 正文可能超 8 页（§5 溢出至 p9）\n- M2: Decoupling spectrum 仅在 4B 验证\n- M3: SFT no-evidence 仅 s42 单 seed\n- M4: CED hypothesis verbalization template sensitivity 未讨论\n- M5: Training-time vs inference-time tax 定义混用\n\n### 主要优势\n1. 系统性实验覆盖（3 paradigms × 4+ scales × 2 families × 2 datasets × multiple seeds）\n2. Novel observations（scale-dependent tax, decoupling spectrum）\n3. 透明度高（主动讨论 limitations）\n4. 实用价值（1.7B RSFT ≈ 8B SFT at 4.7× fewer params）\n5. Thorough appendix（11 sections）\n6. RSFT + CED 组合在 evidence-grounded DocRE 中的有效应用\n\n### Missing References\n未发现明显遗漏。\n\n---\n\n请对以上每一条逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "faith-evidence-ie",
    "chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-24T23:04:22.291434+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_186574e43a82a9df336fe62a846a7b52:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 264 · 2026-05-24T23:04:26.053555+00:00_

交叉分享已派发。等待两位 Reviewer 逐条回应后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 265 · 2026-05-24T23:04:28.541440+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。

主要发现：
- **3 个 Must-Fix**：贡献定位模糊（empirical study 但暗示 method innovation，CED 被自己的 ablation 否定）、abstract 超 200 words (~205)、正文疑似溢出 8 页
- **5 个 Should-Fix**：DPO 仅测试单一 β=0.1、RSFT vs SFT variance 可比性存疑、14B 仅 1-2 seed、evidence quality 未被 RSFT 改善、缺少 DocRED 官方 test set
- **5 个 Minor**：evidence tax 方向约定不一致、bib key-name 不匹配、§4.5 篇幅过短、EDCR correlation 数值不一致（§3.5 vs §4.7）、GRPO batch size 差异未讨论
- **Missing references**：DeepSeek-R1、ReST（非重大遗漏）
- **Claim-evidence 对齐**：数字均可验证，总体一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 266 · 2026-05-24T23:04:33.312793+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 24

## Round 24

20 recorded events


### User

_source line 267 · 2026-05-24T23:06:37.268887+00:00_

[Reviewer 2 审稿结果]:
逐条回应 Reviewer 1 的审稿意见。

---

## 交叉回应：Reviewer 2 对 Reviewer 1

### Must-Fix 问题

**[AGREE] R1-N1: GRPO QLoRA vs bf16 存在未隔离的混淆变量**

同意这是一个实验设计缺陷。Table 3 明确显示 QLoRA G=4 和 bf16 G=8 同时改变了两个变量（quantization + group size），§4.3 的归因"confirming quantization precision rather than group size as the primary factor"缺乏控制实验支撑。论文引用 QuRL (Li et al., 2026) 的 quantized-actor divergence 提供了间接旁证，但这不能替代直接的消融实验。建议至少增加 bf16 G=4 或 QLoRA G=8 中的一组。若计算资源有限，应将结论降级为"quantization and/or group size"。

---

**[AGREE] R1-N2: 方差压缩声明的统计证据不足**

同意。我在自己的审稿中也标注了类似问题（我的 W2）。核心数据来自 Table 6 (Appendix D)：仅 1.7B 的 χ² CI 不重叠（SFT lower bound 1.45pp > RSFT upper bound 0.54pp），其余 3 个 scale 均重叠；sign test p=0.0625 不满足 α=0.05；4B Cohen's d=0.46 属于 small effect。论文自身的脚注已承认"underpowered"，但 abstract 仍以"RSFT consistently reduces training seed variance"作为第三条 contribution，且选择性报告了 LLaMA 的 Cohen's d=2.58 和 1.7B 的 non-overlapping CI——这确实构成 cherry-picking。

补充一个我的独立观察（我的 W2）：RSFT 和 SFT 的 variance 来源不同。SFT variance 是独立训练 seed 的差异；RSFT 从固定 SFT model 出发做 sampling + retraining，天然压缩了上游 variance。论文 §4.2 承认"these reflect different sources of variation"，但后续 claims 未贯彻这一限定。

---

### Should-Fix 问题

**[AGREE] R1-W1: Implicit regularization 假说证据不足**

同意更简约的解释是 output constraint effect。Table 7 (Appendix E) 显示 1.7B evidence model 生成 25.5k predictions vs no-evidence 44.6k（1.75× 差异），duplication rate 从 60.5% 降至 33.0%。这更直接地解释为：evidence 格式占用 token budget → 模型物理上只能生成更少 triples → 更少的 FP 和 duplicates → 更高的 precision。将此称为"implicit regularization"暗示模型内部表征发生了改善，但现有证据无法区分"模型学到了更好的表征"和"模型只是被迫生成更少output"。

不过，我补充一个细节：Appendix E 的 matched@2048 fair evaluation（971/985 documents）在相同 max_new_tokens 下仍然观察到 −5.63pp benefit。如果纯粹是 token budget constraint，那么在 @2048 下（evidence model 不再受限于 1024 tokens）这个 benefit 应该减弱。论文未充分讨论这一点，但它对纯 output constraint 解释构成了部分挑战。建议论文区分讨论这两种机制的贡献。

---

**[AGREE] R1-W2: GRPO/DPO 超参数探索不足**

强烈同意。我在自己的审稿中提出了相同问题（我的 W1）。DPO β=0.1 下 1-epoch Rel-F1 暴跌至 33.37（从 SFT 44.39），降幅达 11pp——在 DPO 文献中这种程度的 degradation 通常指向超参数不当而非方法固有缺陷。Decoupling spectrum 的"DPO gradual degradation"结论建立在单一 β 值上，generalizability 成问题。GRPO KL=0.01 同理。

---

**[AGREE] R1-W3: 14B test-set reversal**

同意。我同样标注了此问题（我的 W3）。补充 Reviewer 1 的分析：Table 9 (Appendix H) 显示 14B SFT truncation rate 50.6% vs RSFT 仅 13.4%。在 annotation-dense test set (34.7 triples/doc vs dev 12.3) 下，higher truncation = longer outputs = more candidate triples to match，SFT 的高 truncation rate 反而可能在 recall-heavy 场景中有利。论文对此的解释（§H, "the SFT model's 50.6% truncation rate implies longer outputs"）方向正确但分析不充分——应该分解为 precision 和 recall 的独立变化来验证。

---

**[REBUT] R1-W4: EDCR mechanical correlation 未被充分控制**

部分反驳。Reviewer 1 关于 FP 同时驱动 EDCR 和 Rel-F1 的 concern 在 cross-method 层面是成立的——这也是论文自己承认的（§3.5："Because EDCR is mechanically influenced by false-positive triples...this correlation should be interpreted as a diagnostic pattern rather than an independent discovery"）。

但 Reviewer 1 对 per-relation analysis 的质疑（"来自相同 documents，不完全独立"）过于严格。Per-relation EDCR（§I, Appendix I）在同一模型配置内按 relation type 分组计算，ρ=−0.79 (n=76, p<0.001) 且与 Evi-F1 正交（ρ=−0.06, p=0.58）。这一分析的关键优势是：per-relation 级别不存在 cross-method 层面的 shared-component concern——同一模型的所有 relation types 共享相同的整体 FP 倾向，但不同 relation types 的 FP 率是独立变化的。论文还报告了 10,000-iteration permutation test (p<0.0001)，这在统计上是充分的。

建议论文增加 per-relation precision 作为额外控制变量的 partial correlation（Reviewer 1 的具体建议），但现有 per-relation evidence 已经提供了 reasonable validation。将此问题的严重性从 MAJOR 降级为 WARNING 更合适。

---

**[AGREE] R1-W5: RSFT "cannot exploit trade-off" 论证缺乏实证**

同意核心观点：§G (Appendix G) 的论证完全是 structural/logical 的（"because the selection is discrete...there is no gradient pathway"），缺少实证验证。Single-objective RSFT（仅按 Rel-F1 或仅按 Evi-F1 选择）是一个 natural 且 computationally cheap 的实验，能直接测试"CED 的 joint scoring 是否是 RSFT 保持 coupling 的关键因素"。

但在 random selection 解读上部分反驳 Reviewer 1 的说法。Reviewer 1 说"Random selection（41.14）对比 SFT mean（43.58）实际更差，说明 selection 本身贡献可能为负"——这里的 baseline 选择有误。Random RSFT 从 SFT s42（39.74）出发，应与 SFT s42 比较（+1.40pp），而非与 SFT three-seed mean（43.58）比较。SFT mean 高是因为 s43（43.65）和 s44（47.34）远强于 s42；用 multi-seed mean 作 baseline 会将 RSFT 不使用的 seed 的性能纳入比较，不公平。正确解读是：random selection 贡献 +1.40pp（来自 retraining on own outputs 的一般 benefit），CED scoring 在此基础上再贡献 +3.52pp。

---

### 小问题

**[AGREE] R1-M1: 正文超 8 页** — 我同样标注了此问题（我的 N3）。§4.7 末尾和 §5 Conclusion 溢出至 p9。

**[AGREE] R1-M2: Decoupling spectrum 仅在 4B 验证** — 合理 concern。GRPO/DPO 实验仅在 4B scale 做了，无法确认 spectrum 在其他 scale 是否保持。不过考虑到 GRPO/DPO 训练的计算成本，single-scale 验证作为 initial evidence 可以接受，应在 Limitations 中声明。

**[AGREE] R1-M3: SFT no-evidence 仅 s42 单 seed** — 部分同意。Table 8 (Appendix F) 显示 4B training-time tax 使用了 three-seed mean (+0.25±0.47pp)，是充分的。但 1.7B 和 8B 均为单 seed (s42)，且 1.7B 的 s42 是 SFT 最强 seed（论文自己承认"s42 is the strongest SFT seed, +3.22pp above three-seed mean"），可能放大了 evidence tax benefit。

**[AGREE] R1-M4: CED hypothesis verbalization template sensitivity** — 我未在自己的审稿中提到此点，但认为有效。CED 依赖 NLI 模型对"$e_h$ has relation $r$ with $e_t$"的 entailment 判断，不同 verbalization 模板（如"$e_h$'s $r$ is $e_t$"或更自然的表述）可能产生不同的 CED scores。论文未讨论 template sensitivity。不过，考虑到 CED vs flat-NLI 差异仅 0.02pp（Table 4, Appendix B），CED 的 fine-grained scoring 本身贡献有限，template sensitivity 对最终结果的影响可能也有限。

**[AGREE] R1-M5: Training-time vs inference-time tax 定义混用** — 我在自己的审稿中也指出了 evidence tax 方向约定不一致（我的 M1）。Table 2 脚注定义"positive = cost"，Figure 7 caption 说"negative = benefit"，Appendix F Table 8 又说"positive = cost"——方向一致但正负 convention 的首次出现位置较晚，增加认知负担。

---

### 对 Reviewer 1 优势评价的回应

Reviewer 1 列出的 6 条优势与我的评估高度一致。补充一点：Reviewer 1 提到"RSFT + CED 组合在 evidence-grounded DocRE 中的有效应用"——我对此持保留态度，因为 CED 被 ablation 证明与 flat-NLI 等价（Rel-F1 差 0.02pp, Table 4），CED 的独特贡献主要在 interpretability（per-triple discrimination scores for error analysis）而非 data selection quality。

---

### 总结

与 Reviewer 1 的评分一致（Overall 3.5 Borderline Conference, Soundness 3-3.5, Excitement 3）。两位 reviewer 在以下核心问题上达成共识：
1. **GRPO/DPO 超参数探索不足**（R1-W2 = R2-W1）
2. **14B 证据薄弱**（R1-W3 = R2-W3）
3. **正文超页**（R1-M1 = R2-N3）
4. **方差压缩统计不足**（R1-N2 ≈ R2-W2）

唯一实质分歧在 R1-W4（EDCR mechanical correlation）——我认为 per-relation analysis 已提供了 adequate validation，严重性应为 WARNING 而非 MAJOR。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-24T23:07:16.613547+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_project_file,update_review_issues,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_project_file,update_review_issues,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-24T23:07:16.614040+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-24T23:07:20.881270+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-24T23:07:20.931881+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-24T23:07:25.851731+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-24T23:07:26.303991+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-24T23:07:26.304467+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-24T23:07:27.436510+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T22:53:03.793680+00:00\", \"completed_at\": \"2026-05-24T22:56:14.134838+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续3页纯文本无任何 display item。审稿人从 Abstract 读到 Related Work 末尾没有任何视觉锚点，第一印象偏\\\"文字墙\\\"。Figure 1 直到第4页才出现。建议将 Figure 1（架构图）或一个精简版核心结果表提前到第2页（Introduction 末尾或 Related Work 之前）\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1 出现后信息传达清晰——pipeline 图用彩色框区分 Standard DocRE vs Evidence-Grounded DocRE，caption 自包含，RSFT 流程一目了然。作为第一个 display item 质量合格，但位置偏晚\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（CED scoring example）较小但功能明确，彩色标注清晰区分 positive/negative evidence。排版位置合理（紧跟 §3.4 定义）\"}, {\"severity\": \"info\", \"dimension\": \"page 6-8\", \"message\": \"Display item 密度优秀：Table 1 + Figure 3（p6）、Figure 4 + Figure 5（p7）、Figure 6 + Table 2 + Figure 7（p8）。结果区视觉节奏很好，审稿人可以快速扫描核心实验\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（Decoupling Spectrum）和 Figure 5（Variance Compression）并排呈现，信息互补，布局紧凑高效\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 6 三个子图（GRPO training dynamics）的轴标签和 legend 字号偏小，但在 150dpi 渲染下仍可辨识。打印时可能需要放大查看\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗，Ign-F1 显示 ± 标准差，格式规范。列宽合理无溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 2 格式整洁，booktabs + 加粗最优值 + 脚注说明清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落紧凑（3个点），符合 EMNLP 要求。Conclusion 和 Limitations 同页，不浪费空间\"}, {\"severity\": \"info\", \"dimension\": \"page 10-11\", \"message\": \"参考文献排版正常，双栏对齐，无 overfull box，无 [?] 未解析引用\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Table 3（Training Hyperparameters）全宽表格，booktabs 风格，dash 表示 N/A，清晰专业\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\":
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1132
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-24T23:07:27.460588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-24T23:07:27.461451+00:00_

1	- id: "W1"
2	  summary: "GRPO confounded variables + collapse mechanism lacks depth"
3	  category: experiment
4	  severity: warning
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 2
8	  mentions:
9	    - {round: 1, reviewers: "R1,R2", note: "Cannot support causal attribution of decoupling to QLoRA"}
10	    - {round: 2, reviewers: "R1,R2", note: "R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor."}
11	  action_items:
12	    - {round: 1, action: "Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect", assigned_to: "Agent", status: "done"}
13	    - {round: 1, action: "Downgrade causal claim to observational", assigned_to: "Paper Agent", status: "done"}
14	    - {round: 2, action: "Deepen GRPO mechanism analysis: add reward hacking lit (Gao et al. 2023), QuRL quantized-actor divergence, explicit mechanistic chain (QLoRA→constrained params→reward shortcut→decoupling)", assigned_to: "Paper Agent", status: "done"}
15	  resolution: ""
16	  resolution_round: null
17	
18	- id: "W2"
19	  summary: "All results dev-set only, no test set"
20	  category: experiment
21	  severity: critical
22	  status: resolved
23	  first_raised_round: 1
24	  last_seen_round: 2
25	  mentions:
26	    - {round: 1, reviewers: "R1,R2", note: "No CodaLab test results"}
27	    - {round: 2, reviewers: "R1,R2", note: "Test set results now exist (Table 9). Method ranking preserved (ρ=1.0)."}
28	  action_items:
29	    - {round: 1, action: "Add test set evaluation for all scales", assigned_to: "Agent+User", status: "done"}
30	  resolution: "Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0)."
31	  resolution_round: 2
32	
33	- id: "W3"
34	  summary: "n=3 variance compression claim statistically unreliable"
35	  category: experiment
36	  severity: critical
37	  status: in_progress
38	  first_raised_round: 1
39	  last_
…[truncated 19735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-24T23:08:01.554727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-24T23:08:01.673182+00:00_

0	---
1	name: review-director-session-start
2	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
3	priority: 9
4	scope: global
5	tags:
6	- workflow
7	- review
8	- session
9	version: 3
10	roles:
11	- review_director
12	---
13	
14	# Review Director Session 启动流程（圆桌会议模式）
15	
16	## 初始化
17	
18	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
19	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
20	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
21	4. 向用户简要汇报：
22	   - **投稿目标**：venue 和 deadline
23	   - **论文状态**：当前草稿位置和版本
24	   - **资料完整性**：提交的材料是否齐全
25	   - **下一步**：即将开始的圆桌审稿流程
26	
27	## 评审流程（收到论文提交后执行）
28	
29	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
30	
31	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
32	2. 确认目标投稿 venue（从提交消息中获取）
33	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
34	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
35	   - `"&lt;venue name> 2026 submission deadline"`
36	   - `"&lt;venue name> 2026 author guidelines"`
37	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
38	5. 提取当前版本的格式要求：
39	   - 页数限制（正文 / 附录 / 参考文献）
40	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
41	   - 匿名规则（double-blind / single-blind / open）
42	   - 附录规则（是否允许、是否参与审稿）
43	   - 引用格式（natbib / biblatex / 特定 .bst）
44	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
45	
46	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
47	
48	### Step 0.5 — 决定 Reviewer 编排
49	
50	根据 venue 类型和论文特点，决定：
51	- 需要几个 Reviewer（1-5 人）
52	- 每个 Reviewer 的审查侧重
53	
54	参考：
55	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
56	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
57	- **Workshop / 短文**：1 人（全面审查）
58	
59	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
60	
61	### Step 0.6 — 外部审稿线（与 Step 1 并行）
62	
63	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
64	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
65	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
66	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
67	- 如果到 Step
…[truncated 872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 118
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-24T23:08:05.372226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-24T23:08:05.416704+00:00_

100	
101	收集所有 Reviewer 的审稿结果。
102	
103	### Step 2 — 交叉分享（原文转发 + 逐条回应）
104	
105	将每位 Reviewer 的**完整审稿原文**转发给其他 Reviewer，要求逐条回应：
106	
107	```
108	director_post_to_reviewer(reviewer_id="2", round_number=N, text="""
109	以下是 Reviewer 1 的完整审稿意见：
110	
111	{Reviewer 1 的原文}
112	
113	请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。
114	""")
115	```
116	
117	对每位 Reviewer 重复此步骤（每人看到其他所有 Reviewer 的原文）。
118	
119	收集所有交叉回应。
120	
121	### Step 3 — 收敛判断
122	
123	分析所有 Reviewer 的意见和交叉回应：
124	
125	- **关键问题已达成共识**（`[AGREE]` 占多数，无未解决的 `[REBUT]` 矛盾）→ 进入 Step 4
126	- **存在重大分歧**（关键 issue 上有 `[REBUT]` 且双方各有道理）→ 回到 Step 1 开始下一轮，附带聚焦问题
127	- **最多 3 轮**：如果第 3 轮仍有分歧，在报告中如实记录各方观点
128	
129	### Step 4 — 汇总报告 & 投递
130	
131	合并所有轮次的发现，形成统一审稿报告：
132	
133	1. 报告结构：
134	   - **Summary**：论文概述（2-3 句）
135	   - **Strengths**：优点（逐条列出）
136	   - **Weaknesses**：缺点（逐条列出，这是重点，必须严格）
137	   - **Reviewer Consensus**：所有 Reviewer 达成共识的关键问题（标注 `[AGREE]`）
138	   - **Reviewer Divergence**：分歧点及各方理由（标注 `[REBUT]`，如有）
139	   - **Questions**：需要作者澄清的问题
140	   - **Missing References**：遗漏的重要相关工作
141	   - **External Review (Stanford Agentic Reviewer)**：如有外部审稿结果，单独列出其 7 维评分、关键发现、以及与内部审稿的差异；如未返回则标注状态
142	   - **Visual Layout Check**（非评分项，不阻塞报告）：调用 `get_visual_check_status(project)` 读一次状态——
143	     - `done` → 直接拼入 findings
144	     - `running` → 写"仍在进行中，本报告不等待，完成后会自动补发到 Group C"
145	     - `timeout` / `error` → 写失败原因 + 提示用户可重新触发
146	     - `not_started` → 写未派发
147	     不要为视觉审查推迟报告投递。视觉 Agent 完成后会自己把结果发到 Group C，与本报告解耦。可直接调用 `format_visual_findings_for_report(project)` 拿到现成的 markdown section
148	   - **Overall Assessment**：总评 + 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度
149	   - **Detailed Comments**：逐节详细意见
150	2. **同步 Issue Tracker**（投递前必做）：
151	   - 用 `read_local_file("projects/{project}/artifacts/review_issues.yaml")` 读当前 tracker（不存在视为空）
152	   - 对本轮所有 Weakness/Must-Fix/Should-Fix:
153	     - 与已有 issue 匹配（同 category + 相似 summary）→ 在 `mentions` 追加本轮记录,更新 `last_seen_round`
154	 
…[truncated 416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "Read",
  "elapsed_ms": 44
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-24T23:11:42.476620+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "faith-evidence-ie",
  "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO QLoRA vs bf16 confounded variables — quantization and group size not isolated\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution 'confirming quantization precision rather than group size as the primary factor' unsupported. Need bf16 G=4 or QLoRA G=8 control. Both AGREE Must-Fix.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade causal claim to observational\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Deepen GRPO mechanism analysis: add reward hacking lit (Gao et al. 2023), QuRL quantized-actor divergence, explicit mechanistic chain (QLoRA→constrained params→reward shortcut→decoupling)\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add bf16 G=4 control OR downgrade claim to 'quantization and/or group size'\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9). Method ranking preserved (ρ=1.0).\"}\n  action_items:\n    - {round: 1, action: \"Add test set evaluation for all scales\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"Variance compression claim statistically underpowered + cherry-picking in abstract\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"SFT single seed, +4.92pp lacks stats\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W1 CRITICAL: n=3 per config, σ 95% CI [0.52s,6.29s], '31×' unreliable. Both recommend ≥5 seeds or downgrade.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Only 1.7B χ² CI non-overlapping (SFT lower 1.45pp > RSFT upper 0.54pp); other 3 scales overlap. Sign test p=0.0625 (not α=0.05). 4B Cohen's d=0.46 (small). Abstract 'RSFT consistently reduces training seed variance' as 3rd contribution cherry-picks LLaMA d=2.58 and 1.7B CI. Both AGREE Must-Fix.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43+seed44, compute bootstrap CI\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Downgrade Abstract/Contributions to 'consistently reduces' (not specific multiplier). Sign test p=0.0625 (4/4, n=4 structural limit) + 1.7B χ² CI non-overlapping + Cohen's d 3/4 large. Three-layer evidence in appendix.\", assigned_to: \"Paper Agent + Agent (compute)\", status: \"done\"}\n    - {round: 3, action: \"Remove variance as standalone contribution from abstract; report as observation with explicit statistical limitations; stop selective reporting\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"3 points insufficient, 1.7B repetition artifact\"}\n    - {round: 2, reviewers: \"R2\", note: \"4 Qwen + 1 LLaMA still limited for general scaling claim. R1 partially rebuts: trend observation reasonable.\"}\n    - {round: 3, note: \"Not directly re-raised in Round 3. Subsumed into other concerns.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent', define fair subset, add LLaMA\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR shared-component mechanical negative correlation with Rel-F1\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"ρ=-0.965 partially predetermined\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W2 CRITICAL: TP in numerator and denominator. n=7 too small. Request partial correlation, permutation test, remove-outlier sensitivity.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"DIVERGENCE. R1: cross-method FP drives both EDCR and Rel-F1, per-relation analysis from same docs not fully independent — wants partial correlation controlling for per-relation precision. R2: per-relation ρ=-0.79 (n=76, p<0.001) adequate because within-model relation types don't share cross-method FP bias; permutation p<0.0001 sufficient. R2 downgrades to WARNING.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicate to n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR to diagnostic tool + shared-component caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Compute partial correlation controlling for TP (ρ=-0.8541, Δ0.15%) + permutation test (p<0.0001) + 48 similar-TP different-EDCR pairs\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Add partial correlation + permutation test + similar-TP pairs to appendix; update Section 5 caveat with specific numbers\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Consider adding per-relation precision as partial correlation control (R1 request) — but existing evidence may suffice (R2 position)\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR ρ inflated by non-independent data points and GRPO QLoRA outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"n=7 ρ=-0.89, n=6 (no QLoRA) ρ=-0.83 p=0.042\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Re-raised: n=6 borderline significant. Need remove-outlier sensitivity report in paper.\"}\n    - {round: 3, note: \"Subsumed into W5 cross-response discussion. R2 considers per-relation analysis (n=76) as sufficient alternative evidence path.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 sans-QLoRA ρ=-0.83 p=0.042 + n=17 partial ρ=-0.8541 + n=7 unique partial ρ=-0.9617 in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED ≈ flat-NLI (0.02pp), contrastive formulation adds no measurable value\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive adds complexity without improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W3 MAJOR: 0.02pp within noise. Subtraction formula lacks theoretical motivation. Paper admits 'not essential'. Both agree CED cannot be method contribution.\"}\n    - {round: 3, reviewers: \"R2\", note: \"R2 cross-response notes CED's unique contribution is interpretability (per-triple scores for error analysis), not data selection quality. Confirmed no method contribution language.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Confirm no remaining CED-as-contribution language. Position as 'one possible NLI-based scoring variant'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"k=3 vs k=1 root cause\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining + update section 3.3\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Paper now consistently reports k=1 with ~3000 training samples. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W8\"\n  summary: \"EDCR ρ based on n=6, not significant without outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\"}\n    - {round: 2, reviewers: \"R1\", note: \"n=7 still small, GRPO QLoRA outlier dominance concern.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion. R2 argues per-relation n=76 sufficient; R1 maintains cross-method n=7 problematic.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 remove-outlier ρ + partial correlation + permutation test in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Encoder baseline comparison selective in metrics presentation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DREEAM 54.01% buried in text\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W7: Table 12 exists but emphasizes TP-only Evi-F1 >80%, downplays 16-18pp Ign-F1 gap.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Balance discussion: acknowledge 16-18pp Ign-F1 gap alongside TP-only Evi-F1 advantage\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"No KL ablation, no reward normalization test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both strongly agree. DPO β=0.1 causes 11pp Rel-F1 drop (44.39→33.37) — typical of hyperparameter mismatch, not method failure. Decoupling spectrum conclusion built on single β value. GRPO KL=0.01 similarly unvalidated.\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add explicit KL caveat to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Either run β={0.01,0.05,0.5} sweep OR explicitly downgrade spectrum claims to 'under these specific hyperparameters'\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Percentage vs decimal mixed\"}\n  action_items:\n    - {round: 1, action: \"Unify to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references (LMRC, SummaC, RelPrior, Rationale Verification)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', author mismatches\"}\n    - {round: 2, reviewers: \"R2,R1\", note: \"R2-W4: Missing LMRC, SummaC, RelPrior, Rationale Verification for RE.\"}\n    - {round: 3, note: \"Not explicitly re-raised in Round 3.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add LMRC, SummaC, RelPrior, Rationale Verification, reward hacking survey (QuRL)\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n  action_items:\n    - {round: 1, action: \"Define fair subset + mechanistic breakdown\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown with duplication rates added. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3: 3/4 rows single seed\"}\n    - {round: 2, note: \"Improved: 1.7B/4B/8B/LLaMA now 3-seed. 14B still single seed. R1-W1 shifts concern to n=3 insufficient.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M3: SFT no-evidence baseline only s42 for 1.7B/8B. 1.7B s42 is strongest SFT seed (+3.22pp above mean) — may inflate evidence tax benefit.\"}\n  action_items:\n    - {round: 1, action: \"Add seeds for 8B/1.7B/LLaMA\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n  action_items:\n    - {round: 1, action: \"Add MTL references to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added (Ruder 2017, Standley et al. 2020, Yu et al. 2020). Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol — checkpoint lost\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W4 MAJOR: Footnote 1 insufficient. DPO 3ep alongside others as if comparable. Checkpoint confirmed lost by Reviewer.\"}\n  action_items:\n    - {round: 1, action: \"Remove internal numbering\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"DPO rebuild: regenerate pairs from SFT generations + CED scores → retrain 1ep+3ep → unified matched@2048 eval\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Update paper: DPO 1ep Rel-F1=33.38 Evi-F1=80.90 EDCR=0.8123; DPO 3ep Rel-F1=31.45 Evi-F1=84.84 EDCR=0.7503. Remove earlier-protocol footnote from §5.3 and tab:spectrum.\", assigned_to: \"Director+Paper Agent\", status: \"done\"}\n  resolution: \"DPO rebuilt from scratch, both 1ep and 3ep evaluated under matched@2048 protocol (bs=16, max_new_tokens=2048, DocRED dev 985 docs). Paper text (§5.3) and appendix (tab:spectrum) updated with new numbers. Earlier-protocol footnote removed.\"\n  resolution_round: 3\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need random-k=1 to prove selection value\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added: 41.14 Ign-F1 vs CED RSFT 44.66. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory\"}\n  action_items:\n    - {round: 1, action: \"Checklist via OpenReview form\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Submitted via OpenReview form per EMNLP 2026 rules. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"93 vs 76 vs 96 conflicting\"}\n  action_items:\n    - {round: 1, action: \"Clarify caption\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified: 93 observed / 96 defined / 76 with ≥5 samples. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — contributions are empirical observations, not method innovations\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: all 3 contributions are empirical observations. R1 downgrades to MAJOR, argues empirical findings acceptable at EMNLP if statistics sound.\"}\n    - {round: 3, note: \"Not re-raised as standalone issue in Round 3. Implicitly addressed by empirical study framing.\"}\n  action_items:\n    - {round: 2, action: \"Reposition paper as empirical study. Remove method-innovation language. CED confirmed no contribution language remains. Statistical foundation strengthened (partial correlation, χ² CI, sign test).\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to NLI model family not analyzed\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Only DeBERTa v3 family tested. No cross-family NLI test.\"}\n    - {round: 3, reviewers: \"R1\", note: \"R1-M4: CED hypothesis verbalization template sensitivity — different templates ('$e_h$ has relation $r$ with $e_t$' vs natural language) may yield different CED scores. R2 agrees but notes CED vs flat-NLI diff only 0.02pp, so impact limited.\"}\n  action_items:\n    - {round: 2, action: \"Added to Limitations: CED relies on DeBERTa-v3, sensitivity to other NLI families unexplored\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measures different sources of randomness\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"SFT = full training randomness; RSFT = fixed-base fine-tuning. Direct comparison unfair. R2 notes practical deployment value still holds.\"}\n    - {round: 3, reviewers: \"R2\", note: \"R2 independently confirms: RSFT from fixed SFT model 'naturally compresses upstream variance'. §4.2 acknowledges different sources but subsequent claims don't maintain this qualification. Both AGREE.\"}\n  action_items:\n    - {round: 2, action: \"Downgraded to 'consistently reduces' + acknowledged measurement asymmetry. χ² CI + Cohen's d provide effect-size evidence beyond direct ratio.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions (DocRED annotations, compute cost, task generalization)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Three omissions: annotation incompleteness, compute cost, IE task generalization.\"}\n  action_items:\n    - {round: 2, action: \"Added 4 points to Limitations: DocRED annotation incompleteness, compute cost, IE task generalization, NLI model family sensitivity\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All 4 points added to Section 7 Limitations.\"\n  resolution_round: null\n\n- id: \"R2-W10-LLM-BASELINE\"\n  summary: \"Missing direct numerical comparison with LLM-based RE methods (LMRC, AutoRE, GLiDRE)\"\n  category: experiment\n  severity: info\n  status: done\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W8: Related Work discusses AutoRE/GLiDRE but no table with extraction performance numbers.\"}\n  action_items:\n    - {round: 2, action: \"Added inline comparison in Related Work: 8B RSFT 54.33 vs AutoRE 52.14 (+2.19pp) vs RelPrior 55.50 (-1.17pp). AutoRE ign_f1 source annotated as RelPrior reproduction (footnote). GLiDRE noted as encoder-based, not directly comparable.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Inline numerical comparison added to Related Work with source annotation.\"\n  resolution_round: null\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text figures insufficient\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Pages 1-5 no visual anchor. Only 3 display items vs typical 5-8.\"}\n  action_items:\n    - {round: 2, action: \"Added fig_overview (Figure 1, full-width §3), fig_spectrum (Figure 2, §5.3), fig_evidence_tax (Figure 3, §5.4). Table 2 (spectrum) moved to appendix to make room.\", assigned_to: \"Paper Agent + Director\", status: \"done\"}\n  resolution: \"Main text now has 3 figures + 2 tables = 5 display items. fig_evidence_tax added per user directive. Paper compiles at exactly 8 pages.\"\n  resolution_round: 3\n\n- id: \"VISUAL-COLORBLIND\"\n  summary: \"Figure 4 red-green color scheme not colorblind-friendly\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Red-green affects ~8% male readers. Suggest red-blue or Okabe-Ito palette.\"}\n  action_items:\n    - {round: 2, action: \"Changed RdYlGn_r → Okabe-Ito gradient (blue→yellow→orange-red). PDF+PNG regenerated.\", assigned_to: \"Agent (Worker)\", status: \"done\"}\n  resolution: \"Colorblind-friendly palette applied to Figure 4.\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax analysis\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"Original 4B checkpoint unavailable, retrained 43.88 vs 44.23 (0.35pp). Evidence tax 0.25±0.47pp same order.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1-IMPLICIT-REG\"\n  summary: \"Implicit regularization hypothesis indistinguishable from output constraint effect\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Evidence model generates 25.5k vs no-evidence 44.6k predictions (1.75× difference, Table 7 Appendix E). More parsimonious explanation: evidence format occupies token budget → fewer triples → fewer FP/duplicates → higher precision. 'Implicit regularization' implies internal representation improvement unsupported by evidence. However, R2 notes matched@2048 evaluation (971/985 docs) still shows -5.63pp benefit — partially challenges pure output-constraint explanation. Paper should distinguish and discuss both mechanisms.\"}\n  action_items:\n    - {round: 3, action: \"Rename 'implicit regularization' to 'output constraint effect' or discuss both mechanisms with matched@2048 as counter-evidence\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2-14B-REVERSAL\"\n  summary: \"14B test-set reversal: SFT outperforms RSFT, explanation insufficient\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Table 9 (Appendix H): 14B SFT truncation rate 50.6% vs RSFT 13.4%. Annotation-dense test set (34.7 triples/doc vs dev 12.3) means high truncation = longer outputs = more candidate triples = higher recall. §H explanation directionally correct but insufficient — need precision/recall decomposition to verify mechanism.\"}\n  action_items:\n    - {round: 3, action: \"Add precision/recall decomposition for 14B test-set to verify truncation-driven recall explanation\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3-RSFT-TRADEOFF\"\n  summary: \"RSFT 'cannot exploit trade-off' claim is purely structural, lacks empirical test\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE core concern. §G (Appendix G) argument entirely logical ('discrete selection, no gradient pathway'). Need single-objective RSFT (select by Rel-F1 only or Evi-F1 only) to empirically test whether CED joint scoring maintains coupling. R2 partially rebuts R1's random-selection interpretation: random RSFT (41.14) should compare to SFT s42 (39.74, +1.40pp), not SFT 3-seed mean (43.58). CED scoring contributes additional +3.52pp above random.\"}\n  action_items:\n    - {round: 3, action: \"Run single-objective RSFT (Rel-F1 only, Evi-F1 only) OR downgrade 'cannot exploit' to hypothesis with structural reasoning only\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-PAGELIMIT\"\n  summary: \"Main text exceeds 8-page limit (§4.7 and §5 overflow to page 9)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. EMNLP 2026 strict 8-page limit for main text. §4.7 末尾和 §5 Conclusion 溢出至 p9. Desk reject risk.\"}\n  action_items:\n    - {round: 3, action: \"Cut main text to ≤8 pages. Move content to appendix or compress existing sections.\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1-SPECTRUM-SCALE\"\n  summary: \"Decoupling spectrum validated only at 4B scale\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M2: GRPO/DPO experiments only at 4B. Cannot confirm spectrum pattern at other scales. Both agree single-scale acceptable as initial evidence given compute cost, but should appear in Limitations.\"}\n  action_items:\n    - {round: 3, action: \"Add to Limitations: decoupling spectrum validated only at 4B\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2-TAX-CONVENTION\"\n  summary: \"Evidence tax positive/negative sign convention inconsistent across sections\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M5: Table 2 footnote 'positive = cost', Figure 7 caption 'negative = benefit', Appendix F Table 8 'positive = cost'. Direction consistent but convention introduction late, increases cognitive load.\"}\n  action_items:\n    - {round: 3, action: \"Unify sign convention and introduce it at first mention\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "faith-evidence-ie",
    "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO QLoRA vs bf16 confounded variables — quantization and group size not isolated\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution 'confirming quantization precision rather than group size as the primary factor' unsupported. Need bf16 G=4 or QLoRA G=8 control. Both AGREE Must-Fix.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade causal claim to observational\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Deepen GRPO mechanism analysis: add reward hacking lit (Gao et al. 2023), QuRL quantized-actor divergence, explicit mechanistic chain (QLoRA→constrained params→reward shortcut→decoupling)\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add bf16 G=4 control OR downgrade claim to 'quantization and/or group size'\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9). Method ranking preserved (ρ=1.0).\"}\n  action_items:\n    - {round: 1, action: \"Add test set evaluation for all scales\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"Variance compression claim statistically underpowered + cherry-picking in abstract\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"SFT single seed, +4.92pp lacks stats\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W1 CRITICAL: n=3 per config, σ 95% CI [0.52s,6.29s], '31×' unreliable. Both recommend ≥5 seeds or downgrade.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Only 1.7B χ² CI non-overlapping (SFT lower 1.45pp > RSFT upper 0.54pp); other 3 scales overlap. Sign test p=0.0625 (not α=0.05). 4B Cohen's d=0.46 (small). Abstract 'RSFT consistently reduces training seed variance' as 3rd contribution cherry-picks LLaMA d=2.58 and 1.7B CI. Both AGREE Must-Fix.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43+seed44, compute bootstrap CI\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Downgrade Abstract/Contributions to 'consistently reduces' (not specific multiplier). Sign test p=0.0625 (4/4, n=4 structural limit) + 1.7B χ² CI non-overlapping + Cohen's d 3/4 large. Three-layer evidence in appendix.\", assigned_to: \"Paper Agent + Agent (compute)\", status: \"done\"}\n    - {round: 3, action: \"Remove variance as standalone contribution from abstract; report as observation with explicit statistical limitations; stop selective reporting\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"3 points insufficient, 1.7B repetition artifact\"}\n    - {round: 2, reviewers: \"R2\", note: \"4 Qwen + 1 LLaMA still limited for general scaling claim. R1 partially rebuts: trend observation reasonable.\"}\n    - {round: 3, note: \"Not directly re-raised in Round 3. Subsumed into other concerns.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent', define fair subset, add LLaMA\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR shared-component mechanical negative correlation with Rel-F1\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"ρ=-0.965 partially predetermined\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W2 CRITICAL: TP in numerator and denominator. n=7 too small. Request partial correlation, permutation test, remove-outlier sensitivity.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"DIVERGENCE. R1: cross-method FP drives both EDCR and Rel-F1, per-relation analysis from same docs not fully independent — wants partial correlation controlling for per-relation precision. R2: per-relation ρ=-0.79 (n=76, p<0.001) adequate because within-model relation types don't share cross-method FP bias; permutation p<0.0001 sufficient. R2 downgrades to WARNING.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicate to n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR to diagnostic tool + shared-component caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Compute partial correlation controlling for TP (ρ=-0.8541, Δ0.15%) + permutation test (p<0.0001) + 48 similar-TP different-EDCR pairs\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Add partial correlation + permutation test + similar-TP pairs to appendix; update Section 5 caveat with specific numbers\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Consider adding per-relation precision as partial correlation control (R1 request) — but existing evidence may suffice (R2 position)\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR ρ inflated by non-independent data points and GRPO QLoRA outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"n=7 ρ=-0.89, n=6 (no QLoRA) ρ=-0.83 p=0.042\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Re-raised: n=6 borderline significant. Need remove-outlier sensitivity report in paper.\"}\n    - {round: 3, note: \"Subsumed into W5 cross-response discussion. R2 considers per-relation analysis (n=76) as sufficient alternative evidence path.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 sans-QLoRA ρ=-0.83 p=0.042 + n=17 partial ρ=-0.8541 + n=7 unique partial ρ=-0.9617 in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED ≈ flat-NLI (0.02pp), contrastive formulation adds no measurable value\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive adds complexity without improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W3 MAJOR: 0.02pp within noise. Subtraction formula lacks theoretical motivation. Paper admits 'not essential'. Both agree CED cannot be method contribution.\"}\n    - {round: 3, reviewers: \"R2\", note: \"R2 cross-response notes CED's unique contribution is interpretability (per-triple scores for error analysis), not data selection quality. Confirmed no method contribution language.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Confirm no remaining CED-as-contribution language. Position as 'one possible NLI-based scoring variant'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"k=3 vs k=1 root cause\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining + update section 3.3\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Paper now consistently reports k=1 with ~3000 training samples. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W8\"\n  summary: \"EDCR ρ based on n=6, not significant without outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\"}\n    - {round: 2, reviewers: \"R1\", note: \"n=7 still small, GRPO QLoRA outlier dominance concern.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion. R2 argues per-relation n=76 sufficient; R1 maintains cross-method n=7 problematic.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 remove-outlier ρ + partial correlation + permutation test in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Encoder baseline comparison selective in metrics presentation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DREEAM 54.01% buried in text\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W7: Table 12 exists but emphasizes TP-only Evi-F1 >80%, downplays 16-18pp Ign-F1 gap.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Balance discussion: acknowledge 16-18pp Ign-F1 gap alongside TP-only Evi-F1 advantage\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"No KL ablation, no reward normalization test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both strongly agree. DPO β=0.1 causes 11pp Rel-F1 drop (44.39→33.37) — typical of hyperparameter mismatch, not method failure. Decoupling spectrum conclusion built on single β value. GRPO KL=0.01 similarly unvalidated.\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add explicit KL caveat to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Either run β={0.01,0.05,0.5} sweep OR explicitly downgrade spectrum claims to 'under these specific hyperparameters'\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Percentage vs decimal mixed\"}\n  action_items:\n    - {round: 1, action: \"Unify to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references (LMRC, SummaC, RelPrior, Rationale Verification)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', author mismatches\"}\n    - {round: 2, reviewers: \"R2,R1\", note: \"R2-W4: Missing LMRC, SummaC, RelPrior, Rationale Verification for RE.\"}\n    - {round: 3, note: \"Not explicitly re-raised in Round 3.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add LMRC, SummaC, RelPrior, Rationale Verification, reward hacking survey (QuRL)\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n  action_items:\n    - {round: 1, action: \"Define fair subset + mechanistic breakdown\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown with duplication rates added. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3: 3/4 rows single seed\"}\n    - {round: 2, note: \"Improved: 1.7B/4B/8B/LLaMA now 3-seed. 14B still single seed. R1-W1 shifts concern to n=3 insufficient.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M3: SFT no-evidence baseline only s42 for 1.7B/8B. 1.7B s42 is strongest SFT seed (+3.22pp above mean) — may inflate evidence tax benefit.\"}\n  action_items:\n    - {round: 1, action: \"Add seeds for 8B/1.7B/LLaMA\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n  action_items:\n    - {round: 1, action: \"Add MTL references to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added (Ruder 2017, Standley et al. 2020, Yu et al. 2020). Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol — checkpoint lost\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W4 MAJOR: Footnote 1 insufficient. DPO 3ep alongside others as if comparable. Checkpoint confirmed lost by Reviewer.\"}\n  action_items:\n    - {round: 1, action: \"Remove internal numbering\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"DPO rebuild: regenerate pairs from SFT generations + CED scores → retrain 1ep+3ep → unified matched@2048 eval\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Update paper: DPO 1ep Rel-F1=33.38 Evi-F1=80.90 EDCR=0.8123; DPO 3ep Rel-F1=31.45 Evi-F1=84.84 EDCR=0.7503. Remove earlier-protocol footnote from §5.3 and tab:spectrum.\", assigned_to: \"Director+Paper Agent\", status: \"done\"}\n  resolution: \"DPO rebuilt from scratch, both 1ep and 3ep evaluated under matched@2048 protocol (bs=16, max_new_tokens=2048, DocRED dev 985 docs). Paper text (§5.3) and appendix (tab:spectrum) updated with new numbers. Earlier-protocol footnote removed.\"\n  resolution_round: 3\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need random-k=1 to prove selection value\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added: 41.14 Ign-F1 vs CED RSFT 44.66. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory\"}\n  action_items:\n    - {round: 1, action: \"Checklist via OpenReview form\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Submitted via OpenReview form per EMNLP 2026 rules. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"93 vs 76 vs 96 conflicting\"}\n  action_items:\n    - {round: 1, action: \"Clarify caption\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified: 93 observed / 96 defined / 76 with ≥5 samples. Not re-raised in Round 2.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — contributions are empirical observations, not method innovations\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: all 3 contributions are empirical observations. R1 downgrades to MAJOR, argues empirical findings acceptable at EMNLP if statistics sound.\"}\n    - {round: 3, note: \"Not re-raised as standalone issue in Round 3. Implicitly addressed by empirical study framing.\"}\n  action_items:\n    - {round: 2, action: \"Reposition paper as empirical study. Remove method-innovation language. CED confirmed no contribution language remains. Statistical foundation strengthened (partial correlation, χ² CI, sign test).\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to NLI model family not analyzed\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Only DeBERTa v3 family tested. No cross-family NLI test.\"}\n    - {round: 3, reviewers: \"R1\", note: \"R1-M4: CED hypothesis verbalization template sensitivity — different templates ('$e_h$ has relation $r$ with $e_t$' vs natural language) may yield different CED scores. R2 agrees but notes CED vs flat-NLI diff only 0.02pp, so impact limited.\"}\n  action_items:\n    - {round: 2, action: \"Added to Limitations: CED relies on DeBERTa-v3, sensitivity to other NLI families unexplored\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measures different sources of randomness\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"SFT = full training randomness; RSFT = fixed-base fine-tuning. Direct comparison unfair. R2 notes practical deployment value still holds.\"}\n    - {round: 3, reviewers: \"R2\", note: \"R2 independently confirms: RSFT from fixed SFT model 'naturally compresses upstream variance'. §4.2 acknowledges different sources but subsequent claims don't maintain this qualification. Both AGREE.\"}\n  action_items:\n    - {round: 2, action: \"Downgraded to 'consistently reduces' + acknowledged measurement asymmetry. χ² CI + Cohen's d provide effect-size evidence beyond direct ratio.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions (DocRED annotations, compute cost, task generalization)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Three omissions: annotation incompleteness, compute cost, IE task generalization.\"}\n  action_items:\n    - {round: 2, action: \"Added 4 points to Limitations: DocRED annotation incompleteness, compute cost, IE task generalization, NLI model family sensitivity\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All 4 points added to Section 7 Limitations.\"\n  resolution_round: null\n\n- id: \"R2-W10-LLM-BASELINE\"\n  summary: \"Missing direct numerical comparison with LLM-based RE methods (LMRC, AutoRE, GLiDRE)\"\n  category: experiment\n  severity: info\n  status: done\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W8: Related Work discusses AutoRE/GLiDRE but no table with extraction performance numbers.\"}\n  action_items:\n    - {round: 2, action: \"Added inline comparison in Related Work: 8B RSFT 54.33 vs AutoRE 52.14 (+2.19pp) vs RelPrior 55.50 (-1.17pp). AutoRE ign_f1 source annotated as RelPrior reproduction (footnote). GLiDRE noted as encoder-based, not directly comparable.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Inline numerical comparison added to Related Work with source annotation.\"\n  resolution_round: null\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text figures insufficient\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Pages 1-5 no visual anchor. Only 3 display items vs typical 5-8.\"}\n  action_items:\n    - {round: 2, action: \"Added fig_overview (Figure 1, full-width §3), fig_spectrum (Figure 2, §5.3), fig_evidence_tax (Figure 3, §5.4). Table 2 (spectrum) moved to appendix to make room.\", assigned_to: \"Paper Agent + Director\", status: \"done\"}\n  resolution: \"Main text now has 3 figures + 2 tables = 5 display items. fig_evidence_tax added per user directive. Paper compiles at exactly 8 pages.\"\n  resolution_round: 3\n\n- id: \"VISUAL-COLORBLIND\"\n  summary: \"Figure 4 red-green color scheme not colorblind-friendly\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Red-green affects ~8% male readers. Suggest red-blue or Okabe-Ito palette.\"}\n  action_items:\n    - {round: 2, action: \"Changed RdYlGn_r → Okabe-Ito gradient (blue→yellow→orange-red). PDF+PNG regenerated.\", assigned_to: \"Agent (Worker)\", status: \"done\"}\n  resolution: \"Colorblind-friendly palette applied to Figure 4.\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax analysis\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"Original 4B checkpoint unavailable, retrained 43.88 vs 44.23 (0.35pp). Evidence tax 0.25±0.47pp same order.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1-IMPLICIT-REG\"\n  summary: \"Implicit regularization hypothesis indistinguishable from output constraint effect\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Evidence model generates 25.5k vs no-evidence 44.6k predictions (1.75× difference, Table 7 Appendix E). More parsimonious explanation: evidence format occupies token budget → fewer triples → fewer FP/duplicates → higher precision. 'Implicit regularization' implies internal representation improvement unsupported by evidence. However, R2 notes matched@2048 evaluation (971/985 docs) still shows -5.63pp benefit — partially challenges pure output-constraint explanation. Paper should distinguish and discuss both mechanisms.\"}\n  action_items:\n    - {round: 3, action: \"Rename 'implicit regularization' to 'output constraint effect' or discuss both mechanisms with matched@2048 as counter-evidence\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2-14B-REVERSAL\"\n  summary: \"14B test-set reversal: SFT outperforms RSFT, explanation insufficient\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Table 9 (Appendix H): 14B SFT truncation rate 50.6% vs RSFT 13.4%. Annotation-dense test set (34.7 triples/doc vs dev 12.3) means high truncation = longer outputs = more candidate triples = higher recall. §H explanation directionally correct but insufficient — need precision/recall decomposition to verify mechanism.\"}\n  action_items:\n    - {round: 3, action: \"Add precision/recall decomposition for 14B test-set to verify truncation-driven recall explanation\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3-RSFT-TRADEOFF\"\n  summary: \"RSFT 'cannot exploit trade-off' claim is purely structural, lacks empirical test\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE core concern. §G (Appendix G) argument entirely logical ('discrete selection, no gradient pathway'). Need single-objective RSFT (select by Rel-F1 only or Evi-F1 only) to empirically test whether CED joint scoring maintains coupling. R2 partially rebuts R1's random-selection interpretation: random RSFT (41.14) should compare to SFT s42 (39.74, +1.40pp), not SFT 3-seed mean (43.58). CED scoring contributes additional +3.52pp above random.\"}\n  action_items:\n    - {round: 3, action: \"Run single-objective RSFT (Rel-F1 only, Evi-F1 only) OR downgrade 'cannot exploit' to hypothesis with structural reasoning only\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-PAGELIMIT\"\n  summary: \"Main text exceeds 8-page limit (§4.7 and §5 overflow to page 9)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. EMNLP 2026 strict 8-page limit for main text. §4.7 末尾和 §5 Conclusion 溢出至 p9. Desk reject risk.\"}\n  action_items:\n    - {round: 3, action: \"Cut main text to ≤8 pages. Move content to appendix or compress existing sections.\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1-SPECTRUM-SCALE\"\n  summary: \"Decoupling spectrum validated only at 4B scale\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M2: GRPO/DPO experiments only at 4B. Cannot confirm spectrum pattern at other scales. Both agree single-scale acceptable as initial evidence given compute cost, but should appear in Limitations.\"}\n  action_items:\n    - {round: 3, action: \"Add to Limitations: decoupling spectrum validated only at 4B\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2-TAX-CONVENTION\"\n  summary: \"Evidence tax positive/negative sign convention inconsistent across sections\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M5: Table 2 footnote 'positive = cost', Figure 7 caption 'negative = benefit', Appendix F Table 8 'positive = cost'. Direction consistent but convention introduction late, increases cognitive load.\"}\n  action_items:\n    - {round: 3, action: \"Unify sign convention and introduce it at first mention\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-24T23:11:42.579334+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml\", \"bytes\": 28481}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-24T23:13:36.646866+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 3 审稿报告\n\n## Summary\n\n本文研究 evidence-grounded document-level relation extraction 中训练方法对 relation extraction 与 evidence grounding 耦合度的影响。提出 RSFT（Rejection Sampling Fine-Tuning）+ CED scoring pipeline，并在 Qwen2.5 (1.7B–14B) 和 LLaMA-3.1-8B 上系统比较 SFT/RSFT/GRPO/DPO 四种训练范式。核心发现：(1) evidence-grounded 训练引入可量化的 accuracy tax；(2) RSFT 维持 RE-evidence coupling 而 GRPO/DPO 产生 decoupling；(3) RSFT 降低 seed variance。论文定位为实证研究。\n\n## Strengths\n\n1. **系统性实验覆盖**：5 个 model scales × 4 种训练范式，加上 cross-architecture (LLaMA) 验证，实验矩阵在 DocRE + evidence grounding 领域属于最全面的之一。\n\n2. **Decoupling spectrum 概念有洞察力**：将不同训练方法按 RE-evidence coupling 程度排列（SFT → RSFT → DPO → GRPO），提供了有用的 conceptual framework。\n\n3. **Evidence tax 量化分析**：将 evidence grounding 的成本与收益分离为 training-time 和 inference-time 两个维度，并提供了定量估计（training: +0.25±0.47pp; inference: −5.63pp at matched tokens）。\n\n4. **Re-DocRED 测试集验证**：Table 9 显示所有 5 个 scale 的 dev-test method ranking 完全一致（Spearman ρ=1.0），提升了结论可靠性。\n\n5. **充分的 ablation 设计**：random selection baseline（区分 retraining effect vs. scoring effect）、matched@2048 evaluation（控制 token budget）、no-evidence SFT（量化 evidence overhead）。\n\n6. **统计分析尝试**：χ² CI、Cohen's d、permutation test、partial correlation 等多层统计验证，虽然部分证据力度不足，但展示了正确的方法论意识。\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**[W-MF1] GRPO QLoRA vs bf16 存在未隔离的混淆变量**\n- Table 3: GRPO QLoRA G=4 vs bf16 G=8 同时改变了 quantization 和 group size\n- §4.3 \"confirming quantization precision rather than group size as the primary factor\" 缺乏控制实验支撑\n- 引用 QuRL (Li et al., 2026) 提供间接旁证不能替代直接消融\n- **要求**：增加 bf16 G=4 或 QLoRA G=8 控制组；若计算资源不足，将结论降级为 \"quantization and/or group size\"\n- *[R1: Must-Fix, R2: AGREE]*\n\n**[W-MF2] 方差压缩声明的统计证据不足 + Abstract cherry-picking**\n- Table 6 (Appendix D): 仅 1.7B 的 χ² CI 不重叠（SFT lower 1.45pp > RSFT upper 0.54pp），其余 3 个 scale 均重叠\n- Sign test p=0.0625，不满足 α=0.05\n- 4B Cohen's d=0.46 属于 small effect（非 large）\n- Abstract 以 \"RSFT consistently reduces training seed variance\" 作为第三条 contribution，选择性报告 LLaMA d=2.58 和 1.7B non-overlapping CI\n- 额外问题：SFT variance = independent training seeds randomness; RSFT variance = fixed-base fine-tuning — 不同 variance 来源直接比较有 methodological concern\n- **要求**：移除 variance 作为独立 contribution；改为 observation with explicit statistical limitations；停止选择性报告\n- *[R1: Must-Fix, R2: AGREE]*\n\n**[W-MF3] 正文超 8 页——EMNLP 2026 违规**\n- §4.7 末尾和 §5 Conclusion 溢出至 page 9\n- EMNLP 2026 严格限制 long paper 正文 8 页（references 无限制，Limitations 不计入）\n- **Desk reject 风险**\n- *[R1: Minor → R2 升级: AGREE 但强调 desk reject 风险]*\n\n### Should-Fix（两位 Reviewer 共识）\n\n**[W-SF1] Implicit regularization 假说无法与 output constraint effect 区分**\n- Table 7 (Appendix E): 1.7B evidence model 生成 25.5k predictions vs no-evidence 44.6k（1.75×差异），duplication rate 60.5%→33.0%\n- 更简约解释：evidence 格式占用 token budget → 物理上只能生成更少 triples → 更少 FP/duplicates → higher precision\n- \"Implicit regularization\" 暗示模型表征改善，但现有证据无法区分这两种机制\n- R2 补充：matched@2048 下仍有 −5.63pp benefit，对纯 output constraint 解释构成部分挑战\n- **要求**：区分讨论两种机制的贡献，或将 \"implicit regularization\" 改为更中性的表述\n- *[R1: Should-Fix, R2: AGREE with nuance]*\n\n**[W-SF2] GRPO/DPO 超参数探索严重不足**\n- DPO β=0.1: Rel-F1 从 SFT 44.39 暴跌至 33.37（−11pp），在 DPO 文献中通常指向超参不当\n- GRPO KL=0.01: 同样只测试了单一值\n- Decoupling spectrum 的 \"DPO gradual degradation\" 结论建立在单一 β 上\n- **要求**：运行 β={0.01, 0.05, 0.5} sweep 或明确限定 spectrum 结论为 \"under these specific hyperparameters\"\n- *[R1: Should-Fix, R2: 强烈 AGREE]*\n\n**[W-SF3] 14B test-set reversal 解释不充分**\n- Table 9 (Appendix H): 14B SFT truncation 50.6% vs RSFT 13.4%\n- Annotation-dense test set (34.7 triples/doc vs dev 12.3): higher truncation = longer outputs = more candidate triples = potentially higher recall\n- §H 方向正确但缺乏 precision/recall 分解验证\n- **要求**：提供 14B test-set 的 precision/recall 分解，验证 truncation-driven recall 假说\n- *[R1: Should-Fix, R2: AGREE]*\n\n**[W-SF4] RSFT \"cannot exploit trade-off\" 论证仅有结构性/逻辑性推理，缺实证**\n- §G (Appendix G): \"because the selection is discrete...there is no gradient pathway\"\n- Single-objective RSFT（仅按 Rel-F1 或仅按 Evi-F1 选择）是一个 natural 且 cheap 的验证实验\n- **要求**：运行 single-objective RSFT 或降级为 hypothesis with structural reasoning\n- Random RSFT baseline 解读注意：应与 SFT s42 (39.74) 比较（+1.40pp），而非 SFT 3-seed mean (43.58)\n- *[R1: Should-Fix, R2: AGREE with baseline clarification]*\n\n### Reviewer 分歧\n\n**[W-DIV1] EDCR mechanical correlation 控制是否充分**\n- **R1 立场 (MAJOR)**：FP 同时驱动 EDCR 和 Rel-F1 → cross-method ρ=-0.965 部分由 shared component 预决定。Per-relation analysis 来自相同 documents，不完全独立。需要 partial correlation controlling for per-relation precision。\n- **R2 立场 (WARNING)**：Per-relation ρ=-0.79 (n=76, p<0.001) 不存在 cross-method shared-component concern（同一模型内，不同 relation types 的 FP 率独立变化）。Evi-F1 正交（ρ=-0.06, p=0.58）。10,000-iteration permutation test (p<0.0001) 统计充分。现有 per-relation evidence 提供 reasonable validation。\n- **Director 判定**：Paper 已有 §3.5 caveat + partial correlation + permutation test。Per-relation analysis 确实回避了 cross-method concern。建议增加 per-relation precision partial correlation 作为额外 robustness check（low cost），但现有证据不构成 rejection ground。**最终定级：WARNING。**\n\n### Minor Issues\n\n| ID | 问题 | 共识 |\n|---|---|---|\n| M1 | Decoupling spectrum 仅在 4B 验证，无法确认其他 scale 是否保持 | AGREE — 加入 Limitations |\n| M2 | SFT no-evidence baseline 仅 s42 单 seed (1.7B/8B)；1.7B s42 是最强 seed (+3.22pp above mean) | AGREE — 可能放大 evidence tax benefit |\n| M3 | CED hypothesis verbalization template sensitivity 未讨论 | AGREE — 但 CED vs flat-NLI 仅 0.02pp，实际影响有限 |\n| M4 | Evidence tax 正负号约定跨节不一致（Table 2 footnote vs Figure 7 caption vs Table 8） | AGREE — 增加认知负担 |\n\n## Questions for Authors\n\n1. 是否可以提供 bf16 G=4 的 GRPO 实验结果以隔离 quantization effect？\n2. 在 matched@2048 evaluation 下，evidence model 仍然获得 −5.63pp benefit——这如何与 \"pure output constraint\" 解释调和？如果确实存在表征层面的改善，有什么直接证据（如 attention pattern、hidden state analysis）？\n3. 如何解释 4B Cohen's d=0.46 (small) 而论文 §4.2 称 variance compression \"consistently\" 存在？\n4. 是否考虑过 DPO β < 0.1 的设置？文献中 β=0.01-0.05 常用于避免过度偏离 reference policy。\n\n## Missing References\n\n本轮未发现新的关键遗漏。Round 2 提出的 LMRC、SummaC、RelPrior、Rationale Verification、QuRL 已添加。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3 分钟)\n\n| 严重性 | 位置 | 发现 |\n|---|---|---|\n| ⚠️ WARNING | p1-3 | 连续 3 页纯文本无 display item。Figure 1 直到 p4 才出现。审稿人第一印象偏\"文字墙\"。建议将 Figure 1 或精简核心结果表提前至 p2 |\n| ⚠️ WARNING | p18 | Figure 10 (Per-Relation EDCR Distribution) 使用红/绿/蓝三色——红绿对比对色盲读者不友好。建议改用 Okabe-Ito 色板或 hatching 辅助 |\n| ✅ | p4-8 | 结果区 display item 密度优秀。Figure/Table 紧跟首次引用，无 float 漂移 |\n| ✅ | 全文 | booktabs 统一、无 overfull box、无 [?] 未解析引用、ACL 匿名格式正确 |\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评分 | 说明 |\n|---|---|---|\n| Soundness | 3 | 核心实验设计合理但多处统计证据不充分；GRPO confound 和 variance claim 是关键薄弱点 |\n| Excitement | 3 | Decoupling spectrum 概念有启发性，但作为实证研究 novelty 受限；findings 对社区有实用价值但非突破性 |\n| Reproducibility | 4 | 代码+数据承诺开源，hyperparameters 详尽（Table 3），evaluation protocol 明确 |\n| Clarity | 3.5 | 整体写作清晰，但 8 页超限、sign convention 混乱、implicit regularization 命名误导 |\n| Overall | 3.5 | Borderline Conference — 实验规模和系统性值得肯定，但两个 Must-Fix（GRPO confound + variance cherry-picking）和页数超限必须解决 |\n\n**置信度：4/5** — 两位 Reviewer 背景互补（方法严谨性 + 新颖性/完整性），交叉验证充分，核心判断一致。\n\n**推荐决定：** 如果 Must-Fix 问题（特别是 GRPO confound 隔离实验和 variance claim 降级）能在 camera-ready 前解决，论文可达到 Conference 水平。当前状态下更适合 Findings。\n\n## Detailed Comments\n\n### §1 Introduction\n- Evidence tax 概念引入清晰，动机充分\n- 第三条 contribution（variance compression）需降级或移除——统计证据不支持作为独立 contribution\n\n### §3 Method\n- RSFT pipeline 描述完整，CED scoring 公式清晰\n- CED 已正确定位为 scoring variant 而非方法 contribution\n- \"Implicit regularization\" 术语需修改——当前证据仅支持 \"output constraint effect\"\n\n### §4 Results\n- Table 1 核心结果可信，cross-scale trend 清晰\n- §4.2 variance compression: 措辞需全面降级，避免 \"consistently\" 等暗示统计显著性的词汇\n- §4.3 GRPO analysis: 移除 causal attribution 或增加控制实验\n\n### §5 Analysis (Decoupling Spectrum)\n- 概念框架有价值，但建立在有限证据上（单一 hyperparameter × 单一 scale）\n- DPO 结果可能是 β 不当导致的 artifact 而非方法固有特征\n\n### Appendix\n- 内容丰富且必要（test set、fair evaluation、statistical tests）\n- Figure 10 需修复色盲问题\n- §G \"cannot exploit\" 论证需补充实证或降级\n\n---\n\n*本报告由 2 位 Reviewer 独立审稿 + 交叉回应后合成。Round 1 完成独立审稿，交叉回应确认收敛（1 轮达成共识）。*",
  "project": "faith-evidence-ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 3 审稿报告\n\n## Summary\n\n本文研究 evidence-grounded document-level relation extraction 中训练方法对 relation extraction 与 evidence grounding 耦合度的影响。提出 RSFT（Rejection Sampling Fine-Tuning）+ CED scoring pipeline，并在 Qwen2.5 (1.7B–14B) 和 LLaMA-3.1-8B 上系统比较 SFT/RSFT/GRPO/DPO 四种训练范式。核心发现：(1) evidence-grounded 训练引入可量化的 accuracy tax；(2) RSFT 维持 RE-evidence coupling 而 GRPO/DPO 产生 decoupling；(3) RSFT 降低 seed variance。论文定位为实证研究。\n\n## Strengths\n\n1. **系统性实验覆盖**：5 个 model scales × 4 种训练范式，加上 cross-architecture (LLaMA) 验证，实验矩阵在 DocRE + evidence grounding 领域属于最全面的之一。\n\n2. **Decoupling spectrum 概念有洞察力**：将不同训练方法按 RE-evidence coupling 程度排列（SFT → RSFT → DPO → GRPO），提供了有用的 conceptual framework。\n\n3. **Evidence tax 量化分析**：将 evidence grounding 的成本与收益分离为 training-time 和 inference-time 两个维度，并提供了定量估计（training: +0.25±0.47pp; inference: −5.63pp at matched tokens）。\n\n4. **Re-DocRED 测试集验证**：Table 9 显示所有 5 个 scale 的 dev-test method ranking 完全一致（Spearman ρ=1.0），提升了结论可靠性。\n\n5. **充分的 ablation 设计**：random selection baseline（区分 retraining effect vs. scoring effect）、matched@2048 evaluation（控制 token budget）、no-evidence SFT（量化 evidence overhead）。\n\n6. **统计分析尝试**：χ² CI、Cohen's d、permutation test、partial correlation 等多层统计验证，虽然部分证据力度不足，但展示了正确的方法论意识。\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**[W-MF1] GRPO QLoRA vs bf16 存在未隔离的混淆变量**\n- Table 3: GRPO QLoRA G=4 vs bf16 G=8 同时改变了 quantization 和 group size\n- §4.3 \"confirming quantization precision rather than group size as the primary factor\" 缺乏控制实验支撑\n- 引用 QuRL (Li et al., 2026) 提供间接旁证不能替代直接消融\n- **要求**：增加 bf16 G=4 或 QLoRA G=8 控制组；若计算资源不足，将结论降级为 \"quantization and/or group size\"\n- *[R1: Must-Fix, R2: AGREE]*\n\n**[W-MF2] 方差压缩声明的统计证据不足 + Abstract cherry-picking**\n- Table 6 (Appendix D): 仅 1.7B 的 χ² CI 不重叠（SFT lower 1.45pp > RSFT upper 0.54pp），其余 3 个 scale 均重叠\n- Sign test p=0.0625，不满足 α=0.05\n- 4B Cohen's d=0.46 属于 small effect（非 large）\n- Abstract 以 \"RSFT consistently reduces training seed variance\" 作为第三条 contribution，选择性报告 LLaMA d=2.58 和 1.7B non-overlapping CI\n- 额外问题：SFT variance = independent training seeds randomness; RSFT variance = fixed-base fine-tuning — 不同 variance 来源直接比较有 methodological concern\n- **要求**：移除 variance 作为独立 contribution；改为 observation with explicit statistical limitations；停止选择性报告\n- *[R1: Must-Fix, R2: AGREE]*\n\n**[W-MF3] 正文超 8 页——EMNLP 2026 违规**\n- §4.7 末尾和 §5 Conclusion 溢出至 page 9\n- EMNLP 2026 严格限制 long paper 正文 8 页（references 无限制，Limitations 不计入）\n- **Desk reject 风险**\n- *[R1: Minor → R2 升级: AGREE 但强调 desk reject 风险]*\n\n### Should-Fix（两位 Reviewer 共识）\n\n**[W-SF1] Implicit regularization 假说无法与 output constraint effect 区分**\n- Table 7 (Appendix E): 1.7B evidence model 生成 25.5k predictions vs no-evidence 44.6k（1.75×差异），duplication rate 60.5%→33.0%\n- 更简约解释：evidence 格式占用 token budget → 物理上只能生成更少 triples → 更少 FP/duplicates → higher precision\n- \"Implicit regularization\" 暗示模型表征改善，但现有证据无法区分这两种机制\n- R2 补充：matched@2048 下仍有 −5.63pp benefit，对纯 output constraint 解释构成部分挑战\n- **要求**：区分讨论两种机制的贡献，或将 \"implicit regularization\" 改为更中性的表述\n- *[R1: Should-Fix, R2: AGREE with nuance]*\n\n**[W-SF2] GRPO/DPO 超参数探索严重不足**\n- DPO β=0.1: Rel-F1 从 SFT 44.39 暴跌至 33.37（−11pp），在 DPO 文献中通常指向超参不当\n- GRPO KL=0.01: 同样只测试了单一值\n- Decoupling spectrum 的 \"DPO gradual degradation\" 结论建立在单一 β 上\n- **要求**：运行 β={0.01, 0.05, 0.5} sweep 或明确限定 spectrum 结论为 \"under these specific hyperparameters\"\n- *[R1: Should-Fix, R2: 强烈 AGREE]*\n\n**[W-SF3] 14B test-set reversal 解释不充分**\n- Table 9 (Appendix H): 14B SFT truncation 50.6% vs RSFT 13.4%\n- Annotation-dense test set (34.7 triples/doc vs dev 12.3): higher truncation = longer outputs = more candidate triples = potentially higher recall\n- §H 方向正确但缺乏 precision/recall 分解验证\n- **要求**：提供 14B test-set 的 precision/recall 分解，验证 truncation-driven recall 假说\n- *[R1: Should-Fix, R2: AGREE]*\n\n**[W-SF4] RSFT \"cannot exploit trade-off\" 论证仅有结构性/逻辑性推理，缺实证**\n- §G (Appendix G): \"because the selection is discrete...there is no gradient pathway\"\n- Single-objective RSFT（仅按 Rel-F1 或仅按 Evi-F1 选择）是一个 natural 且 cheap 的验证实验\n- **要求**：运行 single-objective RSFT 或降级为 hypothesis with structural reasoning\n- Random RSFT baseline 解读注意：应与 SFT s42 (39.74) 比较（+1.40pp），而非 SFT 3-seed mean (43.58)\n- *[R1: Should-Fix, R2: AGREE with baseline clarification]*\n\n### Reviewer 分歧\n\n**[W-DIV1] EDCR mechanical correlation 控制是否充分**\n- **R1 立场 (MAJOR)**：FP 同时驱动 EDCR 和 Rel-F1 → cross-method ρ=-0.965 部分由 shared component 预决定。Per-relation analysis 来自相同 documents，不完全独立。需要 partial correlation controlling for per-relation precision。\n- **R2 立场 (WARNING)**：Per-relation ρ=-0.79 (n=76, p<0.001) 不存在 cross-method shared-component concern（同一模型内，不同 relation types 的 FP 率独立变化）。Evi-F1 正交（ρ=-0.06, p=0.58）。10,000-iteration permutation test (p<0.0001) 统计充分。现有 per-relation evidence 提供 reasonable validation。\n- **Director 判定**：Paper 已有 §3.5 caveat + partial correlation + permutation test。Per-relation analysis 确实回避了 cross-method concern。建议增加 per-relation precision partial correlation 作为额外 robustness check（low cost），但现有证据不构成 rejection ground。**最终定级：WARNING。**\n\n### Minor Issues\n\n| ID | 问题 | 共识 |\n|---|---|---|\n| M1 | Decoupling spectrum 仅在 4B 验证，无法确认其他 scale 是否保持 | AGREE — 加入 Limitations |\n| M2 | SFT no-evidence baseline 仅 s42 单 seed (1.7B/8B)；1.7B s42 是最强 seed (+3.22pp above mean) | AGREE — 可能放大 evidence tax benefit |\n| M3 | CED hypothesis verbalization template sensitivity 未讨论 | AGREE — 但 CED vs flat-NLI 仅 0.02pp，实际影响有限 |\n| M4 | Evidence tax 正负号约定跨节不一致（Table 2 footnote vs Figure 7 caption vs Table 8） | AGREE — 增加认知负担 |\n\n## Questions for Authors\n\n1. 是否可以提供 bf16 G=4 的 GRPO 实验结果以隔离 quantization effect？\n2. 在 matched@2048 evaluation 下，evidence model 仍然获得 −5.63pp benefit——这如何与 \"pure output constraint\" 解释调和？如果确实存在表征层面的改善，有什么直接证据（如 attention pattern、hidden state analysis）？\n3. 如何解释 4B Cohen's d=0.46 (small) 而论文 §4.2 称 variance compression \"consistently\" 存在？\n4. 是否考虑过 DPO β < 0.1 的设置？文献中 β=0.01-0.05 常用于避免过度偏离 reference policy。\n\n## Missing References\n\n本轮未发现新的关键遗漏。Round 2 提出的 LMRC、SummaC、RelPrior、Rationale Verification、QuRL 已添加。\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未启用外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时 ~3 分钟)\n\n| 严重性 | 位置 | 发现 |\n|---|---|---|\n| ⚠️ WARNING | p1-3 | 连续 3 页纯文本无 display item。Figure 1 直到 p4 才出现。审稿人第一印象偏\"文字墙\"。建议将 Figure 1 或精简核心结果表提前至 p2 |\n| ⚠️ WARNING | p18 | Figure 10 (Per-Relation EDCR Distribution) 使用红/绿/蓝三色——红绿对比对色盲读者不友好。建议改用 Okabe-Ito 色板或 hatching 辅助 |\n| ✅ | p4-8 | 结果区 display item 密度优秀。Figure/Table 紧跟首次引用，无 float 漂移 |\n| ✅ | 全文 | booktabs 统一、无 overfull box、无 [?] 未解析引用、ACL 匿名格式正确 |\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评分 | 说明 |\n|---|---|---|\n| Soundness | 3 | 核心实验设计合理但多处统计证据不充分；GRPO confound 和 variance claim 是关键薄弱点 |\n| Excitement | 3 | Decoupling spectrum 概念有启发性，但作为实证研究 novelty 受限；findings 对社区有实用价值但非突破性 |\n| Reproducibility | 4 | 代码+数据承诺开源，hyperparameters 详尽（Table 3），evaluation protocol 明确 |\n| Clarity | 3.5 | 整体写作清晰，但 8 页超限、sign convention 混乱、implicit regularization 命名误导 |\n| Overall | 3.5 | Borderline Conference — 实验规模和系统性值得肯定，但两个 Must-Fix（GRPO confound + variance cherry-picking）和页数超限必须解决 |\n\n**置信度：4/5** — 两位 Reviewer 背景互补（方法严谨性 + 新颖性/完整性），交叉验证充分，核心判断一致。\n\n**推荐决定：** 如果 Must-Fix 问题（特别是 GRPO confound 隔离实验和 variance claim 降级）能在 camera-ready 前解决，论文可达到 Conference 水平。当前状态下更适合 Findings。\n\n## Detailed Comments\n\n### §1 Introduction\n- Evidence tax 概念引入清晰，动机充分\n- 第三条 contribution（variance compression）需降级或移除——统计证据不支持作为独立 contribution\n\n### §3 Method\n- RSFT pipeline 描述完整，CED scoring 公式清晰\n- CED 已正确定位为 scoring variant 而非方法 contribution\n- \"Implicit regularization\" 术语需修改——当前证据仅支持 \"output constraint effect\"\n\n### §4 Results\n- Table 1 核心结果可信，cross-scale trend 清晰\n- §4.2 variance compression: 措辞需全面降级，避免 \"consistently\" 等暗示统计显著性的词汇\n- §4.3 GRPO analysis: 移除 causal attribution 或增加控制实验\n\n### §5 Analysis (Decoupling Spectrum)\n- 概念框架有价值，但建立在有限证据上（单一 hyperparameter × 单一 scale）\n- DPO 结果可能是 β 不当导致的 artifact 而非方法固有特征\n\n### Appendix\n- 内容丰富且必要（test set、fair evaluation、statistical tests）\n- Figure 10 需修复色盲问题\n- §G \"cannot exploit\" 论证需补充实证或降级\n\n---\n\n*本报告由 2 位 Reviewer 独立审稿 + 交叉回应后合成。Round 1 完成独立审稿，交叉回应确认收敛（1 轮达成共识）。*",
    "project": "faith-evidence-ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_186574e43a82a9df336fe62a846a7b52"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-24T23:13:40.468546+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_84537e1e2f9ef71a90742c2db859c6f2:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3821
}
```

</details>

---


### Assistant

_source line 286 · 2026-05-24T23:13:50.113599+00:00_

Round 3 审稿报告已投递至 Research Director。

**本轮结论**：Overall 3.5（Borderline Conference）。

**核心共识**（两位 Reviewer 一致）：
1. **Must-Fix**: GRPO confound 未隔离（需 bf16 G=4 控制）+ variance claim cherry-picking（需降级或移除）
2. **Must-Fix**: 正文超 8 页（desk reject 风险）
3. **Should-Fix**: implicit regularization 命名误导、DPO/GRPO 超参数单一、14B reversal 分析不足、RSFT trade-off 论证缺实证

**唯一分歧**：EDCR mechanical correlation——R1 认为 MAJOR（需 partial correlation controlling for per-relation precision），R2 认为 WARNING（per-relation n=76 已充分）。Director 最终定级 WARNING。

Issue Tracker 已同步更新，新增 5 条 Round 3 issue（R3-W1 至 R3-FMT-PAGELIMIT + 2 条 minor）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director"
}
```

</details>

---


## Round 25

## Round 25

6 recorded events


### User

_source line 287 · 2026-05-24T23:13:51.622355+00:00_

[Reviewer 1 审稿结果]:
以下是我对 Reviewer 2 各条意见的逐条回应。

---

### Must-Fix 问题

**[AGREE] R2-N1: 贡献定位模糊——empirical study 却暗示 method innovation**

同意 R2 的观察。Paper 的三个 contribution（Introduction enumerated list）均为 empirical findings，而非方法论创新：(1) evidence tax 是 scale-dependent 的——观察；(2) gradient pressure 导致 decoupling——观察 + EDCR 诊断工具；(3) RSFT reduces variance——观察。Paper 在 §3.3 末明确承认 "the contribution of RSFT in our setting is not the framework itself"，且 Appendix B Table 4 的 ablation 证实 CED 与 flat-NLI 仅差 0.02pp Rel-F1，contrastive 组件实质无效。论文用 "We formalize..." 和 "we propose EDCR" 的措辞确实暗示了方法创新。

**补充**：但我认为严重程度应为 MAJOR 而非 CRITICAL。Empirical study 在 *ACL 有明确的接收空间（多个 best paper 是 empirical studies），关键是 findings 是否足够 non-trivial。重新定位为 empirical study + diagnostic tool 并不需要大幅重写，而是 framing 调整。

---

**[AGREE] R2-N2: Abstract 超过 200 words**

我没有精确计数，但 abstract 信息密度极高，包含大量具体数字（-5.63pp、+0.25±0.47pp、Cohen's d=2.58、4.7× 等）。即使精确字数在 200 ± 5 的边界，也应主动压缩以避免 desk reject 风险。EMNLP 2026 CLAUDE.md 明确标注 "abstract 不要超过 200 words" 为硬约束。

---

**[AGREE] R2-N3: 正文可能超过 8 页**

与我在 M1 中标注的问题一致。PDF 页面 9 顶部包含 §4.7 Discussion 末尾和 §5 Conclusion（约 8-10 行正文），之后才是 Limitations 和 References。主体正文（Sections 1-5）确实略超 8 页。但我将此评为 MINOR——溢出量很小（<0.2 页），压缩 Discussion 或将 Figure 4/5 移入 Appendix 即可解决。R2 评为 MAJOR 偏重。

---

### Should-Fix 问题

**[AGREE] R2-W1: DPO 评估配置不足**

与我的 W2 完全一致。DPO 1-epoch Rel-F1 从 44.39 暴跌至 33.37（-11pp），这在 DPO 文献中是异常大的 degradation。单一 β=0.1 无法区分"DPO 固有限制"和"超参数不当"。需要至少 β ∈ {0.01, 0.1, 0.5} 的 sensitivity analysis 才能支撑 "DPO gradual degradation" 结论。

---

**[AGREE] R2-W2: RSFT 与 SFT variance 比较方法论存在可比性问题**

这是我自己 review 中遗漏的重要问题。Paper §3.3 描述 RSFT 流程："the SFT model generates N=8 candidate outputs per training document"（单数 "the SFT model"），暗示所有 RSFT seeds 从**同一个** SFT checkpoint 出发。如果是这样，SFT variance 包含 LoRA 初始化的全流程方差，而 RSFT variance 仅包含第二阶段微调的方差——两者测量的是不同层级的随机性。Paper 在 §4.2 提到 "though these reflect different sources of variation (Section 4.4)"，但 abstract 和 contribution 3 中的 "RSFT consistently reduces training seed variance" 并未传达这个关键 caveat。这显著削弱了 Contribution 3 的可信度。

**补充**：如果每个 RSFT seed（s42/s43/s44/s45）分别从对应的 SFT seed 出发生成 candidates 并训练，则比较更公平。但 paper 未明确说明这一点，且 RSFT training samples 固定为 2,718（Table 3），暗示共用同一 candidate pool。

---

**[AGREE] R2-W3: 14B 评估不充分**

与我的 W3 一致。14B SFT 仅 1 seed（Table 2 footnote），RSFT 仅 2 seeds。在 test set 上出现 reversal（Δ=-0.37pp, Table 9 Appendix H），但没有足够 seeds 来判断这是噪声还是系统性效应。14B 被定位为 "validation" 而非 "fully evaluated"（Introduction: "three fully evaluated scales (1.7B, 4B, 8B) with 14B validation"），这是合理的框架设计，但 test reversal 仍然值得更多 seeds 来验证。

---

**[AGREE] R2-W4: Evidence quality 未被 RSFT 改善**

Paper 自己在 Appendix K 中承认 "evidence quality is unchanged (Δ < 0.4pp)"，§4.7 中也明确指出 "RSFT improves what the model extracts but not how well it grounds extractions"。R2 的延伸推论——CED 优于 random 可能主要来自 extraction quality filtering——也有 textual support：CED document-level score "weights by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit"（§3.4）。这意味着 CED 的 selection 信号同时包含 extraction quality 和 evidence quality，前者可能是主要驱动力。

---

**[REBUT] R2-W5: 缺少 DocRED 官方 test set 评测**

部分不同意。DocRED 官方 test set 通过 CodaLab 提交，但 CodaLab leaderboard 不评估 evidence 指标——它只报 Ign-F1 和 F1。本文的核心贡献关于 evidence-extraction interaction，DocRED test 无法评估这些维度。此外，Re-DocRED test set 是对 DocRED 的重新标注，annotation quality 更高（修复了 DocRED 中 ~20% 的 missing annotations），是更严格的评估。Paper 使用 Re-DocRED test 并报告了完整的 5-model comparison（Table 9, Appendix H），这是合理的评估策略。

但我同意，为了与先前工作（ATLOP, SAIS, DREEAM）的可比性，报告 DocRED test 的 Ign-F1 仍然有价值。这应是 MINOR 建议而非 WARNING。

---

### 小问题

**[REBUT] R2-M1: Evidence tax 方向约定不一致**

我检查了论文中所有 evidence tax 的定义：
- Table 2 footnote: "Tax = no-evi − with-evi; positive = cost"
- §4.4: "Ign-F1(no-evidence) − Ign-F1(with-evidence)"
- Table 8 (Appendix F): "Tax = no-evi − with-evi; positive = cost"
- Table 10 (Appendix H): "Tax = no-evi − with-evi; negative = benefit"
- Table 11 (Appendix H): "Tax = no-evi − with-evi; positive = cost"
- Figure 7 caption: "Negative values indicate evidence benefits extraction"

数学定义完全一致。R2 可能指的是语义上的混淆——将 benefit 称为 "negative tax" 确实不直觉，但这是 naming awkwardness 而非 inconsistency。

---

**[AGREE] R2-M2: Bibliography key-name 不匹配**

无法直接验证（需要检查 references.bib），但 R2 如果确认 chen2025docksrag 的第一作者实际是 Xu 等人，则 bib key 有误导性。应检查并修正。

---

**[AGREE] R2-M3: §4.5 仅一段，BM25 k=2 未 justify**

Section 4.5（Evidence Strategy Comparison）确实过于简略。BM25 的 k=2 选择缺乏 justification。作为 evidence strategy 的主要对比实验，至少应讨论 k 的选择依据或提供 k 的 sensitivity。

---

**[AGREE] R2-M4: EDCR cross-method ρ 数值不一致**

这是一个真实的数值不一致。§3.5 报告 cross-method ρ=−0.89（n=7, p=0.007），§4.7 报告 ρ=−0.96（n=7, p<0.001），Appendix L 报告 raw ρ=−0.9643（n=7）。三个位置声称相同的 n=7 但给出不同的 ρ 值。可能的解释：§3.5 使用 3-seed mean per method，而 Appendix L 使用不同聚合方式。但论文未解释这一差异。**这是一个需要修正的错误**。

---

**[AGREE] R2-M5: GRPO bf16 vs QLoRA effective batch size 差异未讨论**

Table 3 显示 QLoRA (batch=4, grad_accum=16, G=4) vs bf16 (batch=8, grad_accum=4, G=8)。Effective input batch: 64 vs 32。虽然总 response 数量可能相同（256 vs 256），每步看到的 unique input documents 数量不同（64 vs 32），这影响 gradient estimation quality。这是 GRPO 实验中另一个未控制的变量，进一步削弱了将 collapse 归因于 quantization 的结论。与我的 N1 中指出的 confound 一致。

---

### Missing References

**[AGREE] DeepSeek-R1**：作为 GRPO 最成功的应用案例，仅引用 DeepSeekMath（GRPO 原论文）而遗漏 DeepSeek-R1 确实是一个明显的 gap。

**[AGREE] ReST (Gulcehre et al., 2023)**：作为 rejection sampling 在 LLM training 中的重要工作（在 STaR 和 RFT 之间），与 RSFT 直接相关，应该被引用。

---

### 总结

R2 的 12 个具体问题中，我 **[AGREE] 10 条**，**[REBUT] 2 条**（M1 evidence tax 方向约定实际一致；W5 缺少 DocRED test 的严重性被高估）。

R2 最有价值的独特贡献是 **W2（RSFT vs SFT variance 可比性）**——如果所有 RSFT 从同一 SFT checkpoint 出发，Contribution 3 的统计比较在方法论上不成立。这一点我自己的 review 中遗漏了，是对我 N2 的重要补充。

我与 R2 在 Overall 评分上一致（3.5 Borderline Conference）。核心判断相同：有价值的 empirical findings，但统计证据和实验设计存在多个可修复但当前未修复的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-24T23:17:16.043801+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "faith-evidence-ie",
  "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO QLoRA vs bf16 confounded variables — quantization, group size, AND effective batch size not isolated\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution unsupported. R1 cross-response adds: effective input batch also differs (QLoRA 64 vs bf16 32 unique docs per step), further weakening causal attribution. Both AGREE Must-Fix.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade causal claim to observational\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Deepen GRPO mechanism analysis: add reward hacking lit (Gao et al. 2023), QuRL quantized-actor divergence, explicit mechanistic chain\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add bf16 G=4 control OR downgrade claim to 'quantization and/or group size'; acknowledge effective batch size confound\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9). Method ranking preserved (ρ=1.0).\"}\n  action_items:\n    - {round: 1, action: \"Add test set evaluation for all scales\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"Variance compression claim statistically underpowered + cherry-picking in abstract + methodological comparability issue\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"SFT single seed, +4.92pp lacks stats\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W1 CRITICAL: n=3 per config, σ 95% CI [0.52s,6.29s], '31×' unreliable.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Stats underpowered (sign test p=0.0625, 3/4 scales CI overlap, 4B d=0.46 small). Abstract cherry-picks. R1 cross-response confirms R2's methodological concern: if all RSFT from same SFT checkpoint, comparison measures different randomness levels. §3.3 'the SFT model' (singular) implies shared checkpoint. Contribution 3 methodologically compromised.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43+seed44, compute bootstrap CI\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Downgrade to 'consistently reduces'\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n    - {round: 3, action: \"Remove variance as standalone contribution; clarify whether RSFT seeds use same or different SFT checkpoints; if same, acknowledge fundamental comparability limitation\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"3 points insufficient, 1.7B repetition artifact\"}\n    - {round: 2, reviewers: \"R2\", note: \"4 Qwen + 1 LLaMA still limited for general scaling claim.\"}\n    - {round: 3, note: \"Not directly re-raised in Round 3. Subsumed into other concerns.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent', define fair subset, add LLaMA\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR shared-component mechanical negative correlation with Rel-F1\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"ρ=-0.965 partially predetermined\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"CRITICAL: TP in numerator and denominator. n=7 too small.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"DIVERGENCE on severity. R1: MAJOR (per-relation from same docs not independent). R2: WARNING (per-relation n=76 adequate, permutation p<0.0001). Director: WARNING. Additional finding: EDCR ρ numerical inconsistency across sections (see R3-ERR-EDCR-RHO).\"}\n  action_items:\n    - {round: 1, action: \"Deduplicate to n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR to diagnostic tool + shared-component caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Compute partial correlation + permutation test + similar-TP pairs\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Consider per-relation precision partial correlation; fix ρ numerical inconsistency across sections\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR ρ inflated by non-independent data points and GRPO QLoRA outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"n=7 ρ=-0.89, n=6 (no QLoRA) ρ=-0.83 p=0.042\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Re-raised: n=6 borderline significant.\"}\n    - {round: 3, note: \"Subsumed into W5. R2 considers per-relation n=76 sufficient alternative.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 sans-QLoRA ρ + partial correlation + permutation test in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED ≈ flat-NLI (0.02pp), contrastive formulation adds no measurable value\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive adds complexity without improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"0.02pp within noise. Both agree CED cannot be method contribution.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 cross-response confirms: Table 4 ablation proves contrastive component ineffective. CED correctly positioned as scoring variant not contribution. R2 notes unique value is interpretability only.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Position as scoring variant not contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"k=3 vs k=1 root cause\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining + update section 3.3\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Paper now consistently reports k=1 with ~3000 training samples.\"\n  resolution_round: 2\n\n- id: \"W8\"\n  summary: \"EDCR ρ based on n=6, not significant without outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\"}\n    - {round: 2, reviewers: \"R1\", note: \"n=7 still small, GRPO QLoRA outlier dominance concern.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 remove-outlier ρ + partial correlation + permutation test\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Encoder baseline comparison selective in metrics presentation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DREEAM 54.01% buried in text\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 12 emphasizes TP-only Evi-F1, downplays 16-18pp Ign-F1 gap.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Balance discussion\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"No KL ablation, no reward normalization test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both strongly agree. DPO β=0.1 → -11pp drop typical of hyperparameter mismatch. Need β∈{0.01,0.1,0.5} sensitivity. R1 cross-response: 'DPO 文献中 β=0.01-0.05 常用于避免过度偏离 reference policy'.\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add explicit KL caveat to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run β={0.01,0.05,0.5} sweep OR limit spectrum claims to 'under β=0.1'\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Percentage vs decimal mixed\"}\n  action_items:\n    - {round: 1, action: \"Unify to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', author mismatches\"}\n    - {round: 2, reviewers: \"R2,R1\", note: \"Missing LMRC, SummaC, RelPrior, Rationale Verification for RE.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 cross-response: DeepSeek-R1 (most successful GRPO application) and ReST (Gulcehre et al., 2023, rejection sampling for LLM training) both missing. Both AGREE.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add LMRC, SummaC, RelPrior, Rationale Verification, QuRL\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add DeepSeek-R1 and ReST (Gulcehre et al., 2023)\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n  action_items:\n    - {round: 1, action: \"Define fair subset + mechanistic breakdown\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown with duplication rates added.\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3: 3/4 rows single seed\"}\n    - {round: 2, note: \"Improved: 1.7B/4B/8B/LLaMA now 3-seed. 14B still single seed.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M3: SFT no-evidence only s42 for 1.7B/8B (strongest seed). R2-W3: 14B only 1 SFT seed + 2 RSFT seeds.\"}\n  action_items:\n    - {round: 1, action: \"Add seeds for 8B/1.7B/LLaMA\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n  action_items:\n    - {round: 1, action: \"Add MTL references to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added.\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol — checkpoint lost\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Checkpoint confirmed lost. Rebuilt.\"}\n  action_items:\n    - {round: 2, action: \"DPO rebuild from scratch\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Update paper with new DPO numbers\", assigned_to: \"Director+Paper Agent\", status: \"done\"}\n  resolution: \"DPO rebuilt, unified matched@2048 evaluation.\"\n  resolution_round: 3\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need random-k=1 to prove selection value\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added: 41.14 vs CED RSFT 44.66.\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory\"}\n  action_items:\n    - {round: 1, action: \"Checklist via OpenReview form\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Submitted via OpenReview form.\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"93 vs 76 vs 96 conflicting\"}\n  action_items:\n    - {round: 1, action: \"Clarify caption\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — contributions are empirical observations, not method innovations\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: all 3 contributions are empirical observations.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 AGREES but downgrades to MAJOR: empirical studies have clear acceptance space at *ACL (multiple best papers are empirical). Framing adjustment needed, not major rewrite. 'We formalize...' and 'we propose EDCR' language implies method innovation.\"}\n  action_items:\n    - {round: 2, action: \"Reposition paper as empirical study\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Remove remaining method-innovation language ('We formalize...', 'we propose EDCR')\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to NLI model family and verbalization template not analyzed\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Only DeBERTa v3 family tested.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M4 adds template sensitivity concern. R2 agrees but notes CED vs flat-NLI 0.02pp limits practical impact.\"}\n  action_items:\n    - {round: 2, action: \"Added to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measures different sources of randomness — methodological comparability compromised\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"SFT = full training randomness; RSFT = fixed-base fine-tuning.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 cross-response: §3.3 uses singular 'the SFT model' implying all RSFT from same checkpoint. If so, SFT variance = LoRA init full-process randomness, RSFT variance = second-stage-only randomness. Different levels of randomness being compared. Contribution 3 'RSFT consistently reduces training seed variance' doesn't convey this caveat. R1 calls this 'most valuable unique contribution' from R2.\"}\n  action_items:\n    - {round: 2, action: \"Acknowledged measurement asymmetry\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Clarify RSFT seed protocol; if same SFT checkpoint → acknowledge fundamental limitation; if different SFT per seed → clarify in text\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Three omissions: annotation incompleteness, compute cost, IE task generalization.\"}\n  action_items:\n    - {round: 2, action: \"Added 4 points to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All 4 points added to Section 7 Limitations.\"\n  resolution_round: null\n\n- id: \"R2-W10-LLM-BASELINE\"\n  summary: \"Missing direct numerical comparison with LLM-based RE methods\"\n  category: experiment\n  severity: info\n  status: done\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Related Work discusses AutoRE/GLiDRE but no numbers.\"}\n  action_items:\n    - {round: 2, action: \"Added inline comparison in Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Inline numerical comparison added.\"\n  resolution_round: null\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text figures insufficient\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Pages 1-5 no visual anchor.\"}\n  action_items:\n    - {round: 2, action: \"Added figures\", assigned_to: \"Paper Agent + Director\", status: \"done\"}\n  resolution: \"Main text now has 3 figures + 2 tables = 5 display items.\"\n  resolution_round: 3\n\n- id: \"VISUAL-COLORBLIND\"\n  summary: \"Figure 4 red-green color scheme not colorblind-friendly\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Red-green affects ~8% male readers.\"}\n  action_items:\n    - {round: 2, action: \"Changed to Okabe-Ito\", assigned_to: \"Agent (Worker)\", status: \"done\"}\n  resolution: \"Colorblind-friendly palette applied.\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax analysis\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"Original 4B checkpoint unavailable, retrained 43.88 vs 44.23 (0.35pp).\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1-IMPLICIT-REG\"\n  summary: \"Implicit regularization hypothesis indistinguishable from output constraint effect\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. 25.5k vs 44.6k predictions (1.75×). Output constraint more parsimonious. But matched@2048 still -5.63pp — partially challenges pure constraint explanation. R1 cross-response adds: R2-W4 shows evidence quality unchanged (Appendix K Δ<0.4pp) — RSFT improves what model extracts but not how well it grounds. CED selection signal includes extraction quality component.\"}\n  action_items:\n    - {round: 3, action: \"Rename 'implicit regularization' or discuss both mechanisms; address matched@2048 counter-evidence\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2-14B-REVERSAL\"\n  summary: \"14B test-set reversal: SFT outperforms RSFT, explanation insufficient\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. 14B SFT truncation 50.6% vs RSFT 13.4%. Need precision/recall decomposition. R1 adds: 14B only 1 SFT seed + 2 RSFT seeds, cannot determine if reversal is noise or systematic.\"}\n  action_items:\n    - {round: 3, action: \"Add precision/recall decomposition; consider additional 14B seeds\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3-RSFT-TRADEOFF\"\n  summary: \"RSFT 'cannot exploit trade-off' claim purely structural, lacks empirical test\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. §G logical only. Need single-objective RSFT. R2 partially rebuts random baseline interpretation (should compare to SFT s42 not 3-seed mean). R1 AGREES with R2's baseline clarification.\"}\n  action_items:\n    - {round: 3, action: \"Run single-objective RSFT OR downgrade to hypothesis\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-PAGELIMIT\"\n  summary: \"Main text exceeds 8-page limit (§4.7 and §5 overflow to page 9)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. R2: MAJOR (desk reject risk). R1: MINOR (overflow <0.2 page, easily fixable). Director: MUST-FIX regardless of severity — format violation is binary.\"}\n  action_items:\n    - {round: 3, action: \"Cut to ≤8 pages\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-ABSTRACT\"\n  summary: \"Abstract may exceed 200-word EMNLP 2026 limit\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"R2-N2: Abstract information-dense with many specific numbers (-5.63pp, +0.25±0.47pp, Cohen's d=2.58, 4.7×). EMNLP 2026 硬约束 ≤200 words. R1 AGREES — desk reject risk even at boundary. Both AGREE Must-Fix.\"}\n  action_items:\n    - {round: 3, action: \"Compress abstract to ≤200 words; remove specific numbers that can be found in body\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-ERR-EDCR-RHO\"\n  summary: \"EDCR cross-method ρ numerical inconsistency: §3.5 (-0.89) vs §4.7 (-0.96) vs Appendix L (-0.9643), all claiming n=7\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"R1 cross-response confirms R2-M4: three locations report different ρ values for supposedly same n=7 analysis. Possible explanation: different aggregation methods (3-seed mean vs single-run). Paper never explains discrepancy. This is a factual error.\"}\n  action_items:\n    - {round: 3, action: \"Identify root cause of ρ inconsistency; unify or explain differences\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1-SPECTRUM-SCALE\"\n  summary: \"Decoupling spectrum validated only at 4B scale\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Single-scale acceptable given compute cost, but needs Limitations mention.\"}\n  action_items:\n    - {round: 3, action: \"Add to Limitations\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2-TAX-CONVENTION\"\n  summary: \"Evidence tax sign convention introduction location unclear\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R2\", note: \"R2-M1: convention introduced late. R1 REBUTS: math definition consistent across all locations (Tax = no-evi − with-evi). Issue is 'negative tax' naming awkwardness, not actual inconsistency. Both agree minor.\"}\n  action_items:\n    - {round: 3, action: \"Introduce sign convention at first mention; consider renaming 'negative tax' to 'benefit'\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4-EVI-QUALITY\"\n  summary: \"RSFT does not improve evidence quality — CED selection may primarily filter by extraction quality\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 cross-response: Appendix K confirms Δ<0.4pp evidence quality. §4.7 'RSFT improves what model extracts but not how well it grounds'. CED document-level scoring weights by extraction correctness (correct triples get CED score, incorrect get zero) → selection signal is partly extraction quality filter. R2 originally raised (R2-W4), R1 AGREES with elaboration.\"}\n  action_items:\n    - {round: 3, action: \"Discuss implications: CED improvement may be extraction-quality-driven rather than evidence-quality-driven\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "faith-evidence-ie",
    "issues_yaml": "- id: \"W1\"\n  summary: \"GRPO QLoRA vs bf16 confounded variables — quantization, group size, AND effective batch size not isolated\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Cannot support causal attribution of decoupling to QLoRA\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R2-W4 MAJOR: collapse analysis lacks mechanism depth, no reward hacking connection, no KL ablation. bf16 G=4/G=8 both avoid catastrophe → precision is key factor.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Table 3 shows QLoRA G=4 vs bf16 G=8 — two variables changed simultaneously. §4.3 attribution unsupported. R1 cross-response adds: effective input batch also differs (QLoRA 64 vs bf16 32 unique docs per step), further weakening causal attribution. Both AGREE Must-Fix.\"}\n  action_items:\n    - {round: 1, action: \"Rerun plan_015 GRPO bf16 G=4 to isolate quantization effect\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade causal claim to observational\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Deepen GRPO mechanism analysis: add reward hacking lit (Gao et al. 2023), QuRL quantized-actor divergence, explicit mechanistic chain\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add bf16 G=4 control OR downgrade claim to 'quantization and/or group size'; acknowledge effective batch size confound\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W2\"\n  summary: \"All results dev-set only, no test set\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"No CodaLab test results\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Test set results now exist (Table 9). Method ranking preserved (ρ=1.0).\"}\n  action_items:\n    - {round: 1, action: \"Add test set evaluation for all scales\", assigned_to: \"Agent+User\", status: \"done\"}\n  resolution: \"Test set results added in Table 9 (Appendix I). All 5 scales evaluated. Method ranking preserved (ρ=1.0).\"\n  resolution_round: 2\n\n- id: \"W3\"\n  summary: \"Variance compression claim statistically underpowered + cherry-picking in abstract + methodological comparability issue\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"SFT single seed, +4.92pp lacks stats\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"R1-W1 CRITICAL: n=3 per config, σ 95% CI [0.52s,6.29s], '31×' unreliable.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Stats underpowered (sign test p=0.0625, 3/4 scales CI overlap, 4B d=0.46 small). Abstract cherry-picks. R1 cross-response confirms R2's methodological concern: if all RSFT from same SFT checkpoint, comparison measures different randomness levels. §3.3 'the SFT model' (singular) implies shared checkpoint. Contribution 3 methodologically compromised.\"}\n  action_items:\n    - {round: 1, action: \"Run SFT seed43+seed44, compute bootstrap CI\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Downgrade to 'consistently reduces'\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n    - {round: 3, action: \"Remove variance as standalone contribution; clarify whether RSFT seeds use same or different SFT checkpoints; if same, acknowledge fundamental comparability limitation\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W4\"\n  summary: \"Scaling claim based on limited data points\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"3 points insufficient, 1.7B repetition artifact\"}\n    - {round: 2, reviewers: \"R2\", note: \"4 Qwen + 1 LLaMA still limited for general scaling claim.\"}\n    - {round: 3, note: \"Not directly re-raised in Round 3. Subsumed into other concerns.\"}\n  action_items:\n    - {round: 1, action: \"Replace 'non-monotonic' with 'scale-dependent', define fair subset, add LLaMA\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5\"\n  summary: \"EDCR shared-component mechanical negative correlation with Rel-F1\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"ρ=-0.965 partially predetermined\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"CRITICAL: TP in numerator and denominator. n=7 too small.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"DIVERGENCE on severity. R1: MAJOR (per-relation from same docs not independent). R2: WARNING (per-relation n=76 adequate, permutation p<0.0001). Director: WARNING. Additional finding: EDCR ρ numerical inconsistency across sections (see R3-ERR-EDCR-RHO).\"}\n  action_items:\n    - {round: 1, action: \"Deduplicate to n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 1, action: \"Downgrade EDCR to diagnostic tool + shared-component caveat\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Compute partial correlation + permutation test + similar-TP pairs\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 3, action: \"Consider per-relation precision partial correlation; fix ρ numerical inconsistency across sections\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W5-EDCR-INFLATION\"\n  summary: \"EDCR ρ inflated by non-independent data points and GRPO QLoRA outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"Research Reviewer\", note: \"n=7 ρ=-0.89, n=6 (no QLoRA) ρ=-0.83 p=0.042\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Re-raised: n=6 borderline significant.\"}\n    - {round: 3, note: \"Subsumed into W5. R2 considers per-relation n=76 sufficient alternative.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 sans-QLoRA ρ + partial correlation + permutation test in paper\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W6\"\n  summary: \"CED ≈ flat-NLI (0.02pp), contrastive formulation adds no measurable value\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Contrastive adds complexity without improvement\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"0.02pp within noise. Both agree CED cannot be method contribution.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 cross-response confirms: Table 4 ablation proves contrastive component ineffective. CED correctly positioned as scoring variant not contribution. R2 notes unique value is interpretability only.\"}\n  action_items:\n    - {round: 1, action: \"Remove CED as independent contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Position as scoring variant not contribution\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W7\"\n  summary: \"Training data quantity contradiction (9042 vs 2718)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"k=3 vs k=1 root cause\"}\n  action_items:\n    - {round: 1, action: \"D102 k=1 retraining + update section 3.3\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Paper now consistently reports k=1 with ~3000 training samples.\"\n  resolution_round: 2\n\n- id: \"W8\"\n  summary: \"EDCR ρ based on n=6, not significant without outlier\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"n=7 ρ=-0.89 p=0.007, per-relation n=76 ρ=-0.79\"}\n    - {round: 2, reviewers: \"R1\", note: \"n=7 still small, GRPO QLoRA outlier dominance concern.\"}\n    - {round: 3, note: \"Subsumed into W5 discussion.\"}\n  action_items:\n    - {round: 1, action: \"Deduplicated analysis complete\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Report n=6 remove-outlier ρ + partial correlation + permutation test\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W9\"\n  summary: \"'matches' 50.50 vs 50.51 statistically meaningless\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Single seed, 0.01pp < any reasonable variance\"}\n  action_items:\n    - {round: 1, action: \"Change 'matches' to 'approaches'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Changed to 'approaches' throughout.\"\n  resolution_round: 2\n\n- id: \"W10\"\n  summary: \"Encoder baseline comparison selective in metrics presentation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DREEAM 54.01% buried in text\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 12 emphasizes TP-only Evi-F1, downplays 16-18pp Ign-F1 gap.\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n  action_items:\n    - {round: 1, action: \"Add encoder baseline comparison table\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Balance discussion\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W11\"\n  summary: \"GRPO/DPO hyperparameter exploration insufficient\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"GRPO only KL=0.01, DPO only beta=0.1\"}\n    - {round: 2, reviewers: \"R2\", note: \"No KL ablation, no reward normalization test.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both strongly agree. DPO β=0.1 → -11pp drop typical of hyperparameter mismatch. Need β∈{0.01,0.1,0.5} sensitivity. R1 cross-response: 'DPO 文献中 β=0.01-0.05 常用于避免过度偏离 reference policy'.\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add explicit KL caveat to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Run β={0.01,0.05,0.5} sweep OR limit spectrum claims to 'under β=0.1'\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W12\"\n  summary: \"Metric format inconsistency\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Percentage vs decimal mixed\"}\n  action_items:\n    - {round: 1, action: \"Unify to percentage format\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Unified to percentage format.\"\n  resolution_round: 2\n\n- id: \"W13\"\n  summary: \"Missing references\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"15 'and others', author mismatches\"}\n    - {round: 2, reviewers: \"R2,R1\", note: \"Missing LMRC, SummaC, RelPrior, Rationale Verification for RE.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 cross-response: DeepSeek-R1 (most successful GRPO application) and ReST (Gulcehre et al., 2023, rejection sampling for LLM training) both missing. Both AGREE.\"}\n  action_items:\n    - {round: 1, action: \"Fix bib errors\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 2, action: \"Add LMRC, SummaC, RelPrior, Rationale Verification, QuRL\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Add DeepSeek-R1 and ReST (Gulcehre et al., 2023)\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W14\"\n  summary: \"1.7B implicit regularization speculation without evidence\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Fair evaluation subset undefined\"}\n  action_items:\n    - {round: 1, action: \"Define fair subset + mechanistic breakdown\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Fair subset defined in Appendix D. Mechanistic breakdown with duplication rates added.\"\n  resolution_round: 2\n\n- id: \"W15\"\n  summary: \"Multi-seed coverage uneven\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Table 3: 3/4 rows single seed\"}\n    - {round: 2, note: \"Improved: 1.7B/4B/8B/LLaMA now 3-seed. 14B still single seed.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M3: SFT no-evidence only s42 for 1.7B/8B (strongest seed). R2-W3: 14B only 1 SFT seed + 2 RSFT seeds.\"}\n  action_items:\n    - {round: 1, action: \"Add seeds for 8B/1.7B/LLaMA\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"W16\"\n  summary: \"Missing multi-task learning / task interference references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Core finding is negative transfer, needs MTL literature\"}\n  action_items:\n    - {round: 1, action: \"Add MTL references to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"MTL references added.\"\n  resolution_round: 2\n\n- id: \"W17\"\n  summary: \"DPO 3-epoch uses different evaluation protocol — checkpoint lost\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"DPO 3ep different protocol, pollutes spectrum\"}\n    - {round: 2, reviewers: \"R1,R2\", note: \"Checkpoint confirmed lost. Rebuilt.\"}\n  action_items:\n    - {round: 2, action: \"DPO rebuild from scratch\", assigned_to: \"Agent\", status: \"done\"}\n    - {round: 2, action: \"Update paper with new DPO numbers\", assigned_to: \"Director+Paper Agent\", status: \"done\"}\n  resolution: \"DPO rebuilt, unified matched@2048 evaluation.\"\n  resolution_round: 3\n\n- id: \"W18\"\n  summary: \"Missing random selection baseline for RSFT\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1\", note: \"Need random-k=1 to prove selection value\"}\n  action_items:\n    - {round: 1, action: \"Run random k=1 RSFT baseline\", assigned_to: \"Agent\", status: \"done\"}\n  resolution: \"Random k=1 baseline added: 41.14 vs CED RSFT 44.66.\"\n  resolution_round: 2\n\n- id: \"FMT-CHECKLIST\"\n  summary: \"Responsible NLP Checklist\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"ARR mandatory\"}\n  action_items:\n    - {round: 1, action: \"Checklist via OpenReview form\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Submitted via OpenReview form.\"\n  resolution_round: 2\n\n- id: \"FMT-APPENDIX-RELCOUNT\"\n  summary: \"Appendix figure relation type count inconsistency\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"93 vs 76 vs 96 conflicting\"}\n  action_items:\n    - {round: 1, action: \"Clarify caption\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Caption clarified.\"\n  resolution_round: 2\n\n- id: \"R2-W1-NOVELTY\"\n  summary: \"Method novelty insufficient — contributions are empirical observations, not method innovations\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R2\", note: \"CRITICAL: all 3 contributions are empirical observations.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 AGREES but downgrades to MAJOR: empirical studies have clear acceptance space at *ACL (multiple best papers are empirical). Framing adjustment needed, not major rewrite. 'We formalize...' and 'we propose EDCR' language implies method innovation.\"}\n  action_items:\n    - {round: 2, action: \"Reposition paper as empirical study\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Remove remaining method-innovation language ('We formalize...', 'we propose EDCR')\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5-NLI-SENSITIVITY\"\n  summary: \"CED sensitivity to NLI model family and verbalization template not analyzed\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Only DeBERTa v3 family tested.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1-M4 adds template sensitivity concern. R2 agrees but notes CED vs flat-NLI 0.02pp limits practical impact.\"}\n  action_items:\n    - {round: 2, action: \"Added to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-VARIANCE-SOURCE\"\n  summary: \"SFT vs RSFT variance measures different sources of randomness — methodological comparability compromised\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"SFT = full training randomness; RSFT = fixed-base fine-tuning.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 cross-response: §3.3 uses singular 'the SFT model' implying all RSFT from same checkpoint. If so, SFT variance = LoRA init full-process randomness, RSFT variance = second-stage-only randomness. Different levels of randomness being compared. Contribution 3 'RSFT consistently reduces training seed variance' doesn't convey this caveat. R1 calls this 'most valuable unique contribution' from R2.\"}\n  action_items:\n    - {round: 2, action: \"Acknowledged measurement asymmetry\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 3, action: \"Clarify RSFT seed protocol; if same SFT checkpoint → acknowledge fundamental limitation; if different SFT per seed → clarify in text\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-LIMITATIONS\"\n  summary: \"Limitations section omissions\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R2,R1\", note: \"Three omissions: annotation incompleteness, compute cost, IE task generalization.\"}\n  action_items:\n    - {round: 2, action: \"Added 4 points to Limitations\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"All 4 points added to Section 7 Limitations.\"\n  resolution_round: null\n\n- id: \"R2-W10-LLM-BASELINE\"\n  summary: \"Missing direct numerical comparison with LLM-based RE methods\"\n  category: experiment\n  severity: info\n  status: done\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Related Work discusses AutoRE/GLiDRE but no numbers.\"}\n  action_items:\n    - {round: 2, action: \"Added inline comparison in Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Inline numerical comparison added.\"\n  resolution_round: null\n\n- id: \"VISUAL-MAIN-FIGURES\"\n  summary: \"Main text figures insufficient\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Pages 1-5 no visual anchor.\"}\n  action_items:\n    - {round: 2, action: \"Added figures\", assigned_to: \"Paper Agent + Director\", status: \"done\"}\n  resolution: \"Main text now has 3 figures + 2 tables = 5 display items.\"\n  resolution_round: 3\n\n- id: \"VISUAL-COLORBLIND\"\n  summary: \"Figure 4 red-green color scheme not colorblind-friendly\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"Visual Agent\", note: \"Red-green affects ~8% male readers.\"}\n  action_items:\n    - {round: 2, action: \"Changed to Okabe-Ito\", assigned_to: \"Agent (Worker)\", status: \"done\"}\n  resolution: \"Colorblind-friendly palette applied.\"\n  resolution_round: null\n\n- id: \"R1-W9-4B-CHECKPOINT\"\n  summary: \"4B retrained checkpoint dev gap 0.35pp may affect evidence tax analysis\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: \"R1\", note: \"Original 4B checkpoint unavailable, retrained 43.88 vs 44.23 (0.35pp).\"}\n    - {round: 3, note: \"Not raised in Round 3.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1-IMPLICIT-REG\"\n  summary: \"Implicit regularization hypothesis indistinguishable from output constraint effect\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. 25.5k vs 44.6k predictions (1.75×). Output constraint more parsimonious. But matched@2048 still -5.63pp — partially challenges pure constraint explanation. R1 cross-response adds: R2-W4 shows evidence quality unchanged (Appendix K Δ<0.4pp) — RSFT improves what model extracts but not how well it grounds. CED selection signal includes extraction quality component.\"}\n  action_items:\n    - {round: 3, action: \"Rename 'implicit regularization' or discuss both mechanisms; address matched@2048 counter-evidence\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2-14B-REVERSAL\"\n  summary: \"14B test-set reversal: SFT outperforms RSFT, explanation insufficient\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. 14B SFT truncation 50.6% vs RSFT 13.4%. Need precision/recall decomposition. R1 adds: 14B only 1 SFT seed + 2 RSFT seeds, cannot determine if reversal is noise or systematic.\"}\n  action_items:\n    - {round: 3, action: \"Add precision/recall decomposition; consider additional 14B seeds\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3-RSFT-TRADEOFF\"\n  summary: \"RSFT 'cannot exploit trade-off' claim purely structural, lacks empirical test\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. §G logical only. Need single-objective RSFT. R2 partially rebuts random baseline interpretation (should compare to SFT s42 not 3-seed mean). R1 AGREES with R2's baseline clarification.\"}\n  action_items:\n    - {round: 3, action: \"Run single-objective RSFT OR downgrade to hypothesis\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-PAGELIMIT\"\n  summary: \"Main text exceeds 8-page limit (§4.7 and §5 overflow to page 9)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. R2: MAJOR (desk reject risk). R1: MINOR (overflow <0.2 page, easily fixable). Director: MUST-FIX regardless of severity — format violation is binary.\"}\n  action_items:\n    - {round: 3, action: \"Cut to ≤8 pages\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-FMT-ABSTRACT\"\n  summary: \"Abstract may exceed 200-word EMNLP 2026 limit\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"R2-N2: Abstract information-dense with many specific numbers (-5.63pp, +0.25±0.47pp, Cohen's d=2.58, 4.7×). EMNLP 2026 硬约束 ≤200 words. R1 AGREES — desk reject risk even at boundary. Both AGREE Must-Fix.\"}\n  action_items:\n    - {round: 3, action: \"Compress abstract to ≤200 words; remove specific numbers that can be found in body\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-ERR-EDCR-RHO\"\n  summary: \"EDCR cross-method ρ numerical inconsistency: §3.5 (-0.89) vs §4.7 (-0.96) vs Appendix L (-0.9643), all claiming n=7\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"R1 cross-response confirms R2-M4: three locations report different ρ values for supposedly same n=7 analysis. Possible explanation: different aggregation methods (3-seed mean vs single-run). Paper never explains discrepancy. This is a factual error.\"}\n  action_items:\n    - {round: 3, action: \"Identify root cause of ρ inconsistency; unify or explain differences\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M1-SPECTRUM-SCALE\"\n  summary: \"Decoupling spectrum validated only at 4B scale\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Both AGREE. Single-scale acceptable given compute cost, but needs Limitations mention.\"}\n  action_items:\n    - {round: 3, action: \"Add to Limitations\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2-TAX-CONVENTION\"\n  summary: \"Evidence tax sign convention introduction location unclear\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R2\", note: \"R2-M1: convention introduced late. R1 REBUTS: math definition consistent across all locations (Tax = no-evi − with-evi). Issue is 'negative tax' naming awkwardness, not actual inconsistency. Both agree minor.\"}\n  action_items:\n    - {round: 3, action: \"Introduce sign convention at first mention; consider renaming 'negative tax' to 'benefit'\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4-EVI-QUALITY\"\n  summary: \"RSFT does not improve evidence quality — CED selection may primarily filter by extraction quality\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"R1 cross-response: Appendix K confirms Δ<0.4pp evidence quality. §4.7 'RSFT improves what model extracts but not how well it grounds'. CED document-level scoring weights by extraction correctness (correct triples get CED score, incorrect get zero) → selection signal is partly extraction quality filter. R2 originally raised (R2-W4), R1 AGREES with elaboration.\"}\n  action_items:\n    - {round: 3, action: \"Discuss implications: CED improvement may be extraction-quality-driven rather than evidence-quality-driven\", assigned_to: \"TBD\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-24T23:17:16.195390+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/review_issues.yaml\", \"bytes\": 27189}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_186574e43a82a9df336fe62a846a7b52:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---

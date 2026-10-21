# Director coordination — Part 1 of 8

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/e0/e0d2e26e51128e828a96.json)

## Round 1

## Round 1

68 recorded events


### User

_source line 1 · 2026-05-16T18:52:41.640590+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Efficient Methods for NLP
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-16T18:52:47.658046+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-16T18:52:47.709174+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-16T18:52:51.273866+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-16T18:52:51.274362+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-16T18:52:55.359976+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-16T18:52:55.415700+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-16T18:52:59.951689+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-16T18:53:00.002564+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-16T18:53:03.568185+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-16T18:53:05.478528+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (80 个)\n\n- **ste_kl_s42**: DONE (killed) — \n- **bce_comp_staged_s42**: DONE (negative) — \n- **spon_training_seq2048**: DONE (killed) — \n- **kl_only_s0**: DONE (success) — \n- **kl_only_s1**: DONE (success) — \n- **mvp_bce_s456**: DONE (success) — \n- **mvp_bce_s123**: DONE (success) — \n- **mvp_bce_s42**: DONE (success) — \n- **mvp_kl_norm_v2_s123**: DONE (success) — \n- **mvp_kl_norm_v2_s42**: DONE (success) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n- **kl_lagrangian_quicktest**: DONE (negative) — \n- **mvp_kl_s42**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- mvp_kl_norm_s456（准备中）\n- spon_kl_s42（准备中）\n- diag_30pct_downstream（准备中）\n- diag_gsm8k_gencomp（准备中）\n- diag_teal_downstream（准备中）\n\n## 近期结论\n- **longbench_kl30_uniform_v6** (negative): —\n- **longbench_kl30_uniform_v2** (failed): —\n- **longbench_dense_v2** (failed): —\n\n## 趋势\n成功 36 / 负向 13 / 失败 15 / 共 72\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- mvp_kl_s123: 已被终止 — unknown\n- mvp_kl_s456: 已被终止 — unknown\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123: 训练失败 — unknown\n- spon_training_seq2048: 已被终止 — unknown\n- ste_kl_s42: 已被终止 — unknown\n- bce_isocompute_s42: 训练失败 — unknown\n- eval_spon_supp_retry: 训练失败 — unknown\n- bce_isocompute_s42_v2: 已被终止 — unknown\n- spon_supp_eval_retry: 训练失败 — unknown\n- kl_sparsity30_s42: 已被终止 — unknown\n- kl_sparsity70_s42: 已被终止 — unknown\n- lm_eval_dense_test: 训练失败 — unknown\n- lm_eval_mistral_downstream: 训练失败 — unknown\n- bench_mistral_kl50_s42: 已被终止 — unknown\n- longbench_kl30_uniform: 训练失败 — unknown\n- longbench_dense: 训练失败 — unknown\n- longbench_kl30_uniform_v2: 训练失败 — unknown\n- long
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1910
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-16T18:53:05.478941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-16T18:53:06.031419+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-16T18:53:06.082114+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-16T18:53:11.956667+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Call for Papers: NLP for Science Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/nlp-science"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"[Call for participation] Present your Findings of EMNLP paper at the NLP4MusA (NLP for Music and Audio) workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-present-your-findings-emnlp-paper-nlp4musa-nlp-music-and-audio-workshop"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the web search results, I found information about various calls for papers and submissions, but the search did not return a
…[truncated 1248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5874
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-16T18:53:16.325194+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline main conference papers ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline main conference papers ARR"
  }
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-16T18:53:16.879790+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 submission format page limit guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 submission format page limit guidelines"
  }
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-16T18:53:22.653268+00:00_

Web search results for query: "EMNLP 2026 submission deadline main conference papers ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"}]

Based on the search results, here is the information about EMNLP 2026 submission deadlines for main conference papers via ARR:

## Key Deadline

The ARR submission deadline is May 25, 2026.

## Important Details

- All deadlines ar
…[truncated 685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6328
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-16T18:53:23.908272+00:00_

Web search results for query: ""ACL Rolling Review" 2026 submission format page limit guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on my search results, here's the information about ACL Rolling Review 2026 submission format, page limits, and guidelines:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

Final versions of accepted papers will be given one additional page o
…[truncated 1116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7028
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-16T18:53:27.623350+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for papers main conference submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org call for papers main conference submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-16T18:53:29.330637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-16T18:53:29.381274+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-16T18:53:35.363508+00:00_

Web search results for query: "site:2026.emnlp.org call for papers main conference submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Update EMNLP System Demonstrations Track with 2026 conference data · huggingface/ai-deadlines at 6a94f2c","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/6a94f2c940ba976564775b34f6b224b0f9ad638d"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

Based on the search results, here is information about EMNLP 2026 main conference submission guidelines:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Submission Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both submissions of articles for review and commitment of reviewed articles to the confer
…[truncated 1270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7740
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-16T18:53:40.835708+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-16T18:53:41.538918+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-16T18:53:41.689932+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 27 · 2026-05-16T18:53:41.690324+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-16T18:53:47.413846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-16T18:53:47.765750+00:00_

1	Activation sparsity can accelerate SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
6	Cross-architecture evaluation on Mistral-7B-v0.3 yields +63\% degradation from dense, compared to +93\% on LLaMA.
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---that govern the quality-sparsity tradeoff.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-16T18:53:47.766164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-16T18:53:48.218487+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can in principle yield substantial inference speedup by pruning 50\% of FFN neurons per token---without modifying the pretrained weights---once structured sparse kernels are available.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}---a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This cr
…[truncated 4950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-16T18:53:48.218866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-16T18:53:48.620779+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 12973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-16T18:53:48.621290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-16T18:53:48.672012+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \times 10^{-3}$ and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presen
…[truncated 11401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-16T18:53:53.540336+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-16T18:53:54.092791+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction---adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	All use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
14	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.
15	
16	\paragraph{Static Bias Correction.}
17	SPON~\cite{xu2026spon} learns input-independent bias vectors via KL divergence, absorbed into parameters at zero inference cost.
18	However, static correction cannot adapt to token-specific patterns.
19	We show SPON's vectors are near-orthogonal to our predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79)---confirming the KL predictor captures most recoverable signal.
20	
21	\paragraph{Activation
…[truncated 623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-16T18:53:54.193676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-16T18:53:54.244342+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We have shown that training sparsity predictors with KL divergence eliminates the need for error compensation networks in activation sparsity for LLMs.
5	The mechanism is structural: BCE's per-neuron gradient is independent of other neurons' mask states, creating a mismatch with global top-$k$ inference allocation that no amount of additional training resolves.
6	KL divergence couples all neurons through the output distribution, aligning the training objective with the inference mechanism.
7	The resulting predictor---a two-layer MLP with 2.37M parameters per layer (75.9M total, $<$1\% of the base model)---achieves PPL 11.79 at 50\% sparsity on LLaMA-3.1-8B under TEAL's global allocation, compared to 23.31 for vanilla TEAL and 27.97 for BCE.
8	Three-seed evaluation under uniform allocation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\%).
9	Our two-dimensional taxonomy (correction granularity $\times$ training signal coupling) situates this result within the broader landscape of activation sparsity methods and identifies the previously unexplored cell of per-token contextual prediction with coupled training signals.
10	
11	Several empirical findings deserve emphasis.
12	The KL advantage grows disproportionately with sparsity---18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%---indicating that distributional coupling becomes increasingly important as more neurons are pruned.
13	The non-monotonic allocation preference reveals three distinct regimes: budget-surplus ($\leq$30\%), where uniform allocation suffices and even outperforms global allocation on MMLU; budget-constrained ($\sim$40\%), where global allocation provides measurable gains; and capacity-limited ($\geq$50\%), where both strategies fail to preserve downstream reasoning.
14	SPON's static bias correction achieves only cosine similarity 0.196 with the predictor's effect and provides only 2.4\% relative PPL improvement (12.08
…[truncated 1817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-16T18:53:54.545863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-16T18:53:54.597282+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The full pipeline adds $\sim$6.4\% 
…[truncated 723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-16T18:53:58.651246+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-16T18:53:59.454884+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-16T18:53:59.455263+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 45 · 2026-05-16T18:53:59.505673+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-16T18:54:02.618078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-16T18:54:02.970133+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{xu2026spon,
6	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
7	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
8	  year = {2026},
9	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
10	  url = {https://arxiv.org/abs/2512.12744},
11	}
12	
13	@inproceedings{muralidharan2024minitron,
14	  title = {Compact Language Models via Pruning and Knowledge Distillation},
15	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
16	  year = {2024},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  url = {https://arxiv.org/abs/2407.14679},
19	}
20	
21	
22	% =============================================================================
23	% Direction 3: SPON and learnable bias correction for sparsity
24	% =============================================================================
25	
26	@article{gautam2026fastforward,
27	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
28	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},
29	  year = {2026},
30	  journal = {arXiv preprint arXiv:2602.00397},
31	  url = {https://arxiv.org/abs/2602.00397},
32	}
33	
34	
35	% =============================================================================
36	% Direction 4: Predictor-based activation sparsity
37	% =============================================================================
38	
39	@inproceedings{liu2025teal,
40	  title = {Training-Free Act
…[truncated 7714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-16T18:54:03.322072+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-16T18:54:03.422966+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:6:{"ts": "2026-05-16T18:52:55.359976+00:00", "role": "tool", "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status", "max_results": "4"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:48:{"ts": "2026-05-16T18:54:03.322072+00:00", "role": "tool", "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review", "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu", "output_mode": "content"}}
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-16T18:54:09.352496+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-16T18:54:09.404034+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-16T18:54:12.468248+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "glob": "config*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
    "glob": "config*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-16T18:54:12.570187+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-16T18:54:15.483195+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-16T18:54:15.584229+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-16T18:54:18.647918+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-16T18:54:18.698940+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-16T18:54:22.112873+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paperreview_ai|external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "glob": "*.{yaml,yml,json,toml}\"",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "paperreview_ai|external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
    "glob": "*.{yaml,yml,json,toml}\"",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-16T18:54:22.213916+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-16T18:54:41.395970+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-16T18:54:41.747771+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-16T18:54:41.848586+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-16T18:54:41.899400+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-16T18:55:29.393240+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 审稿任务分配 — Reviewer 1\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**目标 Venue**: EMNLP 2026 (Main Conference, Efficient Methods for NLP track)\n**ARR 提交截止**: 2026-05-25\n**格式**: Long paper, ≤8 页正文 + 无限参考文献, ACL 模板, double-blind\n**匿名规则**: 严格 double-blind, 禁止自引暴露身份\n\n**论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`\n（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）\n\n---\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **方法论正确性**\n   - §3.5 梯度分析（BCE vs KL）的数学推导是否正确？链式法则展开是否准确？\n   - Gumbel-Sigmoid relaxation 的使用是否恰当？温度退火策略的理论依据？\n   - Lagrangian 约束的对偶更新公式是否有收敛保证？\n\n2. **实验设计严谨性**\n   - 训练 setup（1000 steps, WikiText-103, batch=4）是否充分？是否存在过拟合 WikiText-2 评估集的风险？\n   - Iso-compute 对比（BCE 2700 steps vs KL 1000 steps）是否公平？BCE 的超参是否经过充分调优？\n   - Multi-seed 稳定性（3 seeds, std=0.07）的种子数是否足够？\n   - \"Relative advantage\" 的计算方式是否合理（(TEAL-KL)/TEAL × 100%）？\n\n3. **统计声明与数值一致性**\n   - 论文中多处重复出现的数字（11.79, 23.31, 27.97 等）在不同 section 间是否一致？\n   - \"18% at 30%, 49% at 50%, 82% at 70%\" — 验证这些百分比计算\n   - SPON 贡献 \"2.4% relative improvement (12.08→11.79)\" — 验证 (12.08-11.79)/12.08\n   - Appendix latency 数字与正文 claims 是否一致（6.4% overhead, 2.7% predictor）\n\n4. **消融实验充分性**\n   - 缺少哪些关键消融？（例如：bottleneck 维度 d_b 的敏感性？温度退火 schedule 的影响？训练步数的影响曲线？）\n   - Gumbel vs STE 的对比是否充分？是否有其他 relaxation 方法应该对比？\n\n5. **Claim 强度 vs 证据**\n   - \"eliminates the need for error compensation\" — 证据是否足够支撑？\n   - \"structural failure, not computational\" — BCE 是否给了公平的超参搜索？\n   - Cross-architecture 声明只有 Mistral 一个额外模型，是否过度泛化？\n\n请输出完整审稿报告，包含 Strengths、Weaknesses (逐条编号)、Questions、Overall Assessment。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 审稿任务分配 — Reviewer 1\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**目标 Venue**: EMNLP 2026 (Main Conference, Efficient Methods for NLP track)\n**ARR 提交截止**: 2026-05-25\n**格式**: Long paper, ≤8 页正文 + 无限参考文献, ACL 模板, double-blind\n**匿名规则**: 严格 double-blind, 禁止自引暴露身份\n\n**论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`\n（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）\n\n---\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **方法论正确性**\n   - §3.5 梯度分析（BCE vs KL）的数学推导是否正确？链式法则展开是否准确？\n   - Gumbel-Sigmoid relaxation 的使用是否恰当？温度退火策略的理论依据？\n   - Lagrangian 约束的对偶更新公式是否有收敛保证？\n\n2. **实验设计严谨性**\n   - 训练 setup（1000 steps, WikiText-103, batch=4）是否充分？是否存在过拟合 WikiText-2 评估集的风险？\n   - Iso-compute 对比（BCE 2700 steps vs KL 1000 steps）是否公平？BCE 的超参是否经过充分调优？\n   - Multi-seed 稳定性（3 seeds, std=0.07）的种子数是否足够？\n   - \"Relative advantage\" 的计算方式是否合理（(TEAL-KL)/TEAL × 100%）？\n\n3. **统计声明与数值一致性**\n   - 论文中多处重复出现的数字（11.79, 23.31, 27.97 等）在不同 section 间是否一致？\n   - \"18% at 30%, 49% at 50%, 82% at 70%\" — 验证这些百分比计算\n   - SPON 贡献 \"2.4% relative improvement (12.08→11.79)\" — 验证 (12.08-11.79)/12.08\n   - Appendix latency 数字与正文 claims 是否一致（6.4% overhead, 2.7% predictor）\n\n4. **消融实验充分性**\n   - 缺少哪些关键消融？（例如：bottleneck 维度 d_b 的敏感性？温度退火 schedule 的影响？训练步数的影响曲线？）\n   - Gumbel vs STE 的对比是否充分？是否有其他 relaxation 方法应该对比？\n\n5. **Claim 强度 vs 证据**\n   - \"eliminates the need for error compensation\" — 证据是否足够支撑？\n   - \"structural failure, not computational\" — BCE 是否给了公平的超参搜索？\n   - Cross-architecture 声明只有 Mistral 一个额外模型，是否过度泛化？\n\n请输出完整审稿报告，包含 Strengths、Weaknesses (逐条编号)、Questions、Overall Assessment。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-16T18:55:46.727725+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17334
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-16T18:55:46.979215+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 审稿任务分配 — Reviewer 2\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**目标 Venue**: EMNLP 2026 (Main Conference, Efficient Methods for NLP track)\n**ARR 提交截止**: 2026-05-25\n**格式**: Long paper, ≤8 页正文 + 无限参考文献, ACL 模板, double-blind\n**匿名规则**: 严格 double-blind, 禁止自引暴露身份\n\n**论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`\n（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）\n\n---\n\n### 你的审查侧重：新颖性 + 完整性 + 格式合规\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**\n   - \"KL distillation for sparsity prediction\" 的 novelty 是否足够？SPON 已经用了 KL for sparsity，本文的增量贡献是什么？\n   - 2D taxonomy (correction granularity × training signal coupling) 是否有实质性学术贡献，还是简单的 post-hoc 分类？\n   - \"Three regimes\" 的发现是否具有普适性，还是仅适用于 LLaMA-3.1-8B？\n\n2. **Related Work 覆盖度**\n   - 是否遗漏重要的相关工作？特别关注：\n     - 2025-2026 年的 activation sparsity 新工作\n     - MoE (Mixture of Experts) 与 contextual sparsity 的关联\n     - Knowledge distillation for compression 的经典和最新工作\n     - 其他使用 Gumbel relaxation 做 pruning 的工作\n   - SPON、FastForward 等引用是否准确？（注意 SPON 引用为 2026 ICML，FastForward 为 arXiv 2026）\n\n3. **格式合规性（ARR/ACL 要求）**\n   - ⚠️ **Limitations section**：ARR 要求独立 `\\section*{Limitations}`（在 conclusion 之后、references 之前，不计入页数）。当前论文将 Limitations 作为 conclusion 内的 `\\paragraph{}`，这是**不合规的**。\n   - 是否有 Ethics Statement？（ARR 建议但不强制）\n   - 匿名性检查：是否有任何暴露作者身份的线索（自引、致谢、代码链接等）？\n   - 页数检查：正文（abstract 到 conclusion 结尾，不含 limitations/references/appendix）是否 ≤8 页？\n   - 参考文献格式是否符合 ACL natbib 规范？\n\n4. **引用完整性与准确性**\n   - 所有 claim 是否有引用支撑？\n   - 引用的 venue/year 信息是否正确？\n   - 是否存在疑似虚构引用？（特别注意 2026 年的引用：SPON, FastForward）\n\n5. **论文整体质量**\n   - 写作清晰度和逻辑连贯性\n   - Figure/Table 是否自包含（caption 是否充分）\n   - 实验结论是否与 abstract/intro 的 claim 一致\n   - 是否存在过度宣称 (overclaiming)？\n\n请输出完整审稿报告，包含 Strengths、Weaknesses (逐条编号)、Questions、Missing References、Overall Assessment。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 审稿任务分配 — Reviewer 2\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**目标 Venue**: EMNLP 2026 (Main Conference, Efficient Methods for NLP track)\n**ARR 提交截止**: 2026-05-25\n**格式**: Long paper, ≤8 页正文 + 无限参考文献, ACL 模板, double-blind\n**匿名规则**: 严格 double-blind, 禁止自引暴露身份\n\n**论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`\n（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）\n\n---\n\n### 你的审查侧重：新颖性 + 完整性 + 格式合规\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**\n   - \"KL distillation for sparsity prediction\" 的 novelty 是否足够？SPON 已经用了 KL for sparsity，本文的增量贡献是什么？\n   - 2D taxonomy (correction granularity × training signal coupling) 是否有实质性学术贡献，还是简单的 post-hoc 分类？\n   - \"Three regimes\" 的发现是否具有普适性，还是仅适用于 LLaMA-3.1-8B？\n\n2. **Related Work 覆盖度**\n   - 是否遗漏重要的相关工作？特别关注：\n     - 2025-2026 年的 activation sparsity 新工作\n     - MoE (Mixture of Experts) 与 contextual sparsity 的关联\n     - Knowledge distillation for compression 的经典和最新工作\n     - 其他使用 Gumbel relaxation 做 pruning 的工作\n   - SPON、FastForward 等引用是否准确？（注意 SPON 引用为 2026 ICML，FastForward 为 arXiv 2026）\n\n3. **格式合规性（ARR/ACL 要求）**\n   - ⚠️ **Limitations section**：ARR 要求独立 `\\section*{Limitations}`（在 conclusion 之后、references 之前，不计入页数）。当前论文将 Limitations 作为 conclusion 内的 `\\paragraph{}`，这是**不合规的**。\n   - 是否有 Ethics Statement？（ARR 建议但不强制）\n   - 匿名性检查：是否有任何暴露作者身份的线索（自引、致谢、代码链接等）？\n   - 页数检查：正文（abstract 到 conclusion 结尾，不含 limitations/references/appendix）是否 ≤8 页？\n   - 参考文献格式是否符合 ACL natbib 规范？\n\n4. **引用完整性与准确性**\n   - 所有 claim 是否有引用支撑？\n   - 引用的 venue/year 信息是否正确？\n   - 是否存在疑似虚构引用？（特别注意 2026 年的引用：SPON, FastForward）\n\n5. **论文整体质量**\n   - 写作清晰度和逻辑连贯性\n   - Figure/Table 是否自包含（caption 是否充分）\n   - 实验结论是否与 abstract/intro 的 claim 一致\n   - 是否存在过度宣称 (overclaiming)？\n\n请输出完整审稿报告，包含 Strengths、Weaknesses (逐条编号)、Questions、Missing References、Overall Assessment。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-16T18:55:48.239177+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1259
}
```

</details>

---


### Assistant

_source line 68 · 2026-05-16T18:55:54.708847+00:00_

Round 1 审稿任务已分配：

- **Reviewer 1** → 方法严谨性 + 实验设计（梯度分析、统计声明、消融充分性）
- **Reviewer 2** → 新颖性 + 完整性 + 格式合规（contribution novelty、related work、ARR 合规）

等待两位 Reviewer 返回独立审稿意见后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 2

## Round 2

2 recorded events


### User

_source line 69 · 2026-05-16T18:59:10.336130+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 Main Conference (Efficient Methods for NLP track)

---

## 总体评分

**Overall**: 3 (Findings track acceptance recommended)
**一句话总结**: 核心 idea（用 KL 替代 BCE 训练 sparsity predictor）合理且有实验支撑，但实验规模过小、关键消融缺失、"structural failure"声明证据不足，且论文未实现任何实际加速。

---

## 官方维度打分（ACL ARR Review Form, 2025-2026）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 claim 有基本实验支撑，但"structural failure"断言缺少充分 hyperparameter search 证据；梯度分析是 informal argument 而非 formal proof；Lagrangian 无收敛分析 |
| Excitement | 3/5 | KL+Gumbel-Sigmoid 用于 sparsity predictor 训练是 reasonable contribution，但实际未实现 wall-clock 加速，限制了实践影响力 |
| Reproducibility | 4/5 | 训练 setup 清晰（1000 steps, WikiText-103, batch=4, AdamW），代码细节足够复现，但缺少关键超参（η_λ, Gumbel noise scale） |
| Confidence | 4/5 | 本 reviewer 熟悉 activation sparsity、知识蒸馏和 Gumbel relaxation 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 训练/评估数据同源，存在过拟合风险

- 具体位置：§4.1 Training & Evaluation
- 问题：训练数据为 WikiText-103，评估指标为 WikiText-2 perplexity。两者来自同一 Wikipedia 数据源，共享领域分布和文本风格。在仅 1000 steps（~8M tokens）的极少训练量下，predictor 可能学到 WikiText 特有的 neuron importance pattern 而非通用 pattern。论文的 primary metric（PPL 11.79 vs 23.31）完全依赖此评估，但未提供任何 out-of-domain 评估（如 C4、The Pile test set）来排除过拟合。
- 为什么影响接收：如果 PPL improvement 主要来自 domain overfitting，核心 contribution 不成立。
- 建议修改方向：至少补充一个 out-of-domain PPL 评估（C4 或 Pile test），或在不同训练数据上训练后评估 WikiText-2。

**N2** [critical] "Structural failure, not computational" 声明缺少充分证据

- 具体位置：§4.2 (Iso-Compute Analysis), §3.5 最后一段
- 问题：论文断言 BCE 的失败是"structural"而非"computational"，证据是：(a) 2700 steps 后仍不如 KL 1000 steps; (b) BCE loss 在 500-2700 steps 间仅下降 0.006。但这不排除以下可能性：
  1. BCE 需要不同的 learning rate / schedule（论文未报告 BCE 的 LR 是否做过搜索）
  2. BCE 需要更大的 predictor architecture（也许 d_b=256 或 512 对 BCE 更关键）
  3. BCE loss 饱和可能仅说明当前 LR 太小或处于 local minimum
  4. "Loss saturation"不等于"structural limitation"——任何已收敛的模型都有 loss saturation

  论文只试了**一个** BCE configuration 就做出"structural"断言。对比之下，KL 用了 Gumbel relaxation + Lagrangian constraint + temperature annealing 等多个 tricks。
- 为什么影响接收：这是论文的核心 narrative，如果证据不足，贡献被严重削弱。
- 建议修改方向：(1) 对 BCE 做基本的 hyperparameter search（至少 LR grid + architecture size），报告所有结果；(2) 或弱化 claim 为"under our setting, KL is significantly more effective"而非绝对的"structural failure"。

**N3** [critical] 消融实验严重不足

- 具体位置：Table 3 (§4.3)
- 问题：消融表只有 4 行，对一个有多个 design choice 的方法论文远远不够。关键缺失：
  1. **Bottleneck 维度 d_b 的敏感性**：论文选 d_b=128 无任何理由，不知 64/256/512 的效果如何
  2. **温度退火 schedule**：cosine 从 1.0→0.1 完全无 justification，无 linear/exponential/fixed 对比
  3. **训练步数的影响曲线**：1000 steps 是否足够？learning curve 是什么样？
  4. **Lagrangian learning rate η_λ**：这是关键超参，完全未报告
  5. **训练数据 domain 的影响**：换 C4 训练会怎样？
- 为什么影响接收：读者无法判断 method 的鲁棒性和 sensitivity，也无法在自己的场景中 tune。
- 建议修改方向：至少补充 d_b sensitivity（3-4 个值）和 training steps curve。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 论文实际增加了推理延迟，未实现任何 wall-clock 加速

- 具体位置：§4 最后一段 "Inference Efficiency" + Appendix A
- 问题：论文整体 motivation 是"accelerate SwiGLU-based LLMs"（Abstract, §1），但实验表明 pipeline 增加 6.4% latency overhead。Appendix 明确承认"unstructured element-wise masks...do not translate to wall-clock speedup without sparse kernel support"。这意味着方法**当前不能加速推理**，只能在假设未来有 sparse kernel 的情况下才有价值。
- 建议：在 Abstract/Introduction 中更诚实地 frame 贡献为"prediction quality"研究而非"acceleration"研究，或提供至少一个 sparse kernel 的 PoC。

**W2** [warning] Cross-architecture 验证仅一个模型，泛化 claim 过强

- 具体位置：§4 "Cross-Architecture Validation" 段
- 问题：仅额外评估 Mistral-7B-v0.3 一个模型，就称"cross-architecture validation"和"transferability to other SwiGLU architectures"。LLaMA-3.1-8B 和 Mistral-7B 都是 ~7-8B SwiGLU decoder-only transformers，极其相似。真正的 cross-architecture 应包括不同 FFN 类型（如 GeGLU）、不同规模（13B/70B）、或不同家族（Qwen、Gemma）。
- 建议：弱化措辞为"preliminary evaluation on one additional model"，或补充一个更不同的架构。

**W3** [warning] 三 seed 稳定性评估 (n=3) 统计效力不足

- 具体位置：§4 "Training Stability", Appendix B
- 问题：3 个 seed（42, 123, 456）得到 std=0.07 是不够的。n=3 时标准误差的估计本身就极不可靠——95% CI for σ 在 n=3 时的宽度约为 [0.45σ, 3.2σ]。无法从 3 个点得出"training is stable"的可靠结论。
- 建议：扩展到至少 5-10 seeds，或明确标注这是 preliminary evidence。

**W4** [warning] 梯度分析（§3.5）是 informal argument，非 formal proof

- 具体位置：§3.5
- 问题：链式法则展开本身正确，但论文从"KL gradient depends on all neurons"跳到"KL is better"缺少严格推理。Coupled gradient 也可能带来劣势：(a) gradient variance 更高导致优化困难；(b) high-dimensional Jacobian 的 condition number 可能很差；(c) Gumbel noise 进一步增加 variance。论文没有讨论这些 trade-offs，也没有 formal characterization（如 gradient SNR 对比）。
- 建议：要么提供 gradient variance/SNR 的实证对比，要么明确标注§3.5为"intuitive motivation"而非"theoretical contribution"。

**W5** [warning] Lagrangian 对偶更新无收敛保证

- 具体位置：§3.4, Eq. 9-10
- 问题：对于非凸目标（neural network + Gumbel relaxation），Lagrangian dual ascent 不保证收敛到可行解。论文完全没讨论：(a) λ 是否实际收敛？(b) sparsity constraint 最终是否被满足？(c) 是否有 oscillation？这些在实践中可能不是问题（多数 DL 论文忽略这点），但既然论文把 Lagrangian 作为方法 contribution 之一，应该至少实证展示 λ 和 sparsity ratio 的训练曲线。
- 建议：Appendix 中补充 λ 和实际 sparsity ratio over training steps 的图。

---

## 小问题（不影响接收）

- "2.71×" (§4.2) 应为 2.70× (2700/1000=2.7)，微小数值错误
- "saves ~2.7% latency" (§4 Inference Efficiency): 在 50% sparsity 下实际为 2.46% ((129.71-126.78)/119.11)，2.7% 对应 30% sparsity 的数据。文本未说明使用哪个 sparsity level 的数据
- Table 1 caption 称"Multi-seed variance (3 seeds, 50% uniform): PPL std=0.07"，但 main text 报的 PPL 11.79 是 global allocation (seed=42)。multi-seed 用 uniform allocation 得到 11.92±0.07——这两个数字的区别（11.79 vs 11.92）应该更清楚地解释（footnote 已有但容易混淆）
- "Relative advantage" 定义为 (TEAL-KL)/TEAL，这是一种对方法有利的 metric 选择。相比之下，(TEAL-KL)/(TEAL-Dense) 即"recovery of degradation"在某些情况下更有信息量

---

## 主要优势

- **Clear central insight**：BCE per-neuron decomposition vs global top-k inference 的 mismatch 观察敏锐且 well-articulated
- **Solid core result**：PPL 11.79 vs 23.31 (TEAL) / 27.97 (BCE) 的差距显著且consistent across sparsity levels
- **Well-structured paper**：2D taxonomy 有效地 situate 了 contribution；三个 sparsity regime 的分析有 insight
- **Honest limitations section**：论文坦诚承认无 wall-clock speedup、单一规模、PPL 作为 proxy 的局限
- **Reproducibility**：训练 setup 详细，17 min on A6000，practical for reproduction
- **Gumbel vs STE ablation**：+3.98 PPL gap 证明 relaxation choice matters

---

## Questions to Authors (for rebuttal)

1. BCE 实验中使用的 learning rate 和 schedule 是什么？是否做过 LR search？
2. d_b=128 是如何选择的？是否有 preliminary 实验？
3. 能否提供 C4 test set 或其他 OOD 数据上的 PPL，以排除 WikiText 过拟合？
4. Lagrangian multiplier λ 在训练过程中的轨迹如何？实际 sparsity ratio 是否精确达到 target？
5. 如果给 BCE 同样的 Gumbel-Sigmoid + Lagrangian 框架（仅把 KL loss 换成对应的 BCE target），性能如何？这能更 cleanly 隔离 loss function 的贡献 vs 训练框架的贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-16T18:59:18.303380+00:00_

Reviewer 1 审稿报告已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 71 · 2026-05-16T18:59:20.764307+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：评分 Overall 3/5（Findings track），Soundness 3/5，Excitement 3/5。主要问题：(1) 训练/评估同源（WikiText-103→WikiText-2）有过拟合风险且无 OOD 验证；(2) "structural failure"断言仅基于一个 BCE configuration，缺少 hyperparameter search；(3) 消融实验仅 4 行，缺 d_b sensitivity、温度 schedule 对比、training curve 等关键消融。次要问题包括未实现实际加速、cross-architecture 验证不足（仅 1 个额外模型）、3-seed 统计效力弱。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 72 · 2026-05-16T18:59:27.512233+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 4

## Round 4

6 recorded events


### User

_source line 73 · 2026-05-16T19:00:29.819227+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 Main Conference (Efficient Methods for NLP track)

---

## 总体评分

**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 方法思路清晰、实验扎实，但核心 novelty 有限（KL distillation for sparsity 已有 SPON 先例），且实验仅覆盖 7-8B 模型，不足以支撑 main conference。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要 claims 有实验支撑，但模型规模（仅 7-8B）和数据多样性（WikiText only）有限 |
| Excitement | 3/5 (Interesting) | 方法合理、结果实用，但增量贡献属于 "已知技术的新组合" |
| Reproducibility | 4/5 | 训练细节充分（步数、学习率、batch size、架构参数均明确），但代码未公开 |
| Confidence | 4/5 | 对 activation sparsity 和 KD 领域较为熟悉 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Limitations section 格式不合规

- 具体位置：conclusion.tex line 17，`\paragraph{Limitations.}` 在 Section 5 Conclusion 内部
- 问题：ARR 明确要求 `\section*{Limitations}` 作为独立 unnumbered section，置于 conclusion 之后、references 之前，且不计入页数限制。当前论文将 Limitations 作为 conclusion 内的 `\paragraph{}`，(1) 格式不合规，(2) Limitations 内容计入正文页数。
- 为什么影响接收：这是 ARR desk-reject 条件之一。ARR reviewer guidelines 明确要求检查 Limitations section 的存在和位置。
- 建议修改方向：将 `\paragraph{Limitations.}` 和 `Future work...` 段落拆分为 `\section*{Limitations}` 独立 section，放在 `\section{Conclusion}` 之后、`\bibliography{}` 之前。

**N2** [critical] 页数超限

- 具体位置：PDF 第 8-9 页
- 问题：从 PDF 渲染结果看，Section 5 Conclusion 的正文（含嵌入的 Limitations 和 Future work 段落）延伸至第 9 页顶部，之后才是 References。ACL long paper 正文限制 ≤8 页（abstract 到 conclusion 结尾，不含 limitations/references/appendix）。即使将 Limitations 拆为独立 section 后可能刚好 8 页，但当前状态**超限**。
- 为什么影响接收：页数超限是 hard reject 条件。
- 建议修改方向：拆出 Limitations section 后重新检查页数。如仍超限，需压缩 Section 4 的实验描述（Table 5 和 Table 4 有信息重复，可合并）。

**N3** [critical] 新颖性有限——与 SPON 的区分度不充分

- 具体位置：Section 1 Introduction line 19-20, Section 3.4 KL Divergence Training Objective, Table 1 (taxonomy)
- 问题：论文的核心贡献是 "用 KL divergence 训练 sparsity predictor"，但 SPON (Xu et al., 2026) **已经**使用 KL divergence 训练 sparsity correction。论文在 Table 1 taxonomy 中将 SPON 归入 "Static × Coupled (KL)" 格，而本方法占据 "Per-token × Coupled (KL)" 格，声称这是 "previously unexplored cell"。但从技术上看，差异仅在于 (1) 预测的是 per-token contextual mask 而非 static bias，(2) 使用 Gumbel-Sigmoid relaxation。这更像是 SPON 方法的自然延伸（从 static 到 per-token）而非根本性创新。
  - 论文自身的 SPON orthogonality analysis (Section 4.6) 也证实 SPON 的贡献仅为 2.4%——这反过来说明 SPON 的 KL training 已经覆盖了大部分信号，本文只是将同一思路应用于更精细的粒度。
- 为什么影响接收：对于 EMNLP main conference，novelty bar 要求方法层面有足够的新颖性。当前工作的技术贡献更适合 Findings。
- 建议修改方向：需要更深入地 formalize per-token vs. static KL training 的差异（如理论分析 per-token adaptation 的 expressiveness 优势），或增加显著性更强的实验证据（如在 13B/70B 模型上验证）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 遗漏重要相关工作：MaskLLM (NeurIPS 2024 Spotlight)

- 具体位置：Section 2 Related Work
- 问题：MaskLLM (Fang et al., NeurIPS 2024) 同样使用 Gumbel Softmax 进行可学习的 LLM sparsity mask 训练（针对 N:M semi-structured sparsity），在 LLaMA-2/Nemotron-4/GPT-3 上取得了 PPL 6.72 vs. 其他方法 >10 的显著优势。该工作与本文共享关键技术组件（Gumbel relaxation + learnable mask + frozen weights），且是 NeurIPS 2024 spotlight，未引用是明显遗漏。
- 建议：在 Related Work 增加讨论，说明本文与 MaskLLM 的区别（MaskLLM 针对 N:M structured pattern，本文针对 unstructured top-k activation sparsity；MaskLLM 直接学习 mask distribution，本文通过 predictor 网络生成 context-dependent mask）。

**W2** [warning] MoE 与 contextual sparsity 的关联未讨论

- 具体位置：Section 2 Related Work
- 问题：Per-token neuron selection（contextual sparsity）在概念上与 Mixture of Experts 的 per-token expert routing 高度相关——两者都是根据输入动态选择计算子集。2025 年 ICLR workshop on Sparsity in LLMs 明确将 MoE 和 activation sparsity 列为同一研究主题。论文完全没有讨论这一关联，也没有与 MoE routing 的 Gumbel-based gating 方法对比。
- 建议：添加简短讨论，说明 contextual sparsity prediction 和 MoE routing 的概念联系与技术差异。

**W3** [warning] "Structural mismatch" 论述过度

- 具体位置：Section 1 line 16-17, Section 3.6 全段
- 问题：论文将 BCE 的失败描述为 "structural mismatch"，暗示这是本文的理论发现。但 "proxy loss vs. end-to-end objective 的 misalignment 导致性能下降" 是 ML 中的基本认知——任何不直接优化最终目标的 surrogate loss 都可能有此问题。Section 3.6 的 gradient analysis 虽然正确，但本质上是在数学上展示 KL gradient 包含 Jacobian chain rule 而 BCE gradient 不包含，这并非深刻的理论贡献。
- 建议：弱化 "structural mismatch" 的 novelty claim，改为强调这是 "将 end-to-end distillation 原则应用于 sparsity prediction 的首次系统验证"。

**W4** [warning] BCE baseline 不充分——仅比较了 vanilla BCE

- 具体位置：Section 4.2 Iso-Compute Analysis, Table 2
- 问题：论文将 BCE 的失败归因于 "structural" 缺陷，但只测试了 vanilla BCE（per-neuron independent classification）。BCE 有多种改进变体：
  - Weighted BCE（根据 neuron importance 加权）
  - BCE + auxiliary ranking loss（添加 pairwise ranking 约束）
  - BCE trained against soft oracle targets（而非 hard 0/1 mask）
  - BCE + learned temperature
  如果这些改进后的 BCE 仍然大幅落后于 KL，"structural" 论断才有说服力。仅用 vanilla BCE 作为 straw-man 对比，论证力不够。
- 建议：至少添加 BCE + soft targets 或 BCE + ranking loss 的对比实验。

**W5** [warning] 三个 regime 的发现缺乏普适性验证

- 具体位置：Section 4.5, Table 4
- 问题：Budget-surplus / budget-constrained / capacity-limited 三个 regime 的边界（30% / 40% / 50%）仅在 LLaMA-3.1-8B 上确定。Mistral-7B 只测了 50% 一个点（Section 4.6 最后一段）。这些 regime 边界可能随模型规模、架构、训练数据变化。论文将此作为 contribution 之一（Introduction line 46），但实际只有单模型的证据。
- 建议：(1) 在 Mistral-7B 上补测 30% 和 40% 验证 regime 边界是否转移，或 (2) 弱化普适性 claim，明确限定为 "on LLaMA-3.1-8B"。

**W6** [warning] 2D taxonomy 学术贡献有限

- 具体位置：Section 3.7, Table 1, Figure 1
- 问题：2D taxonomy（correction granularity × training signal coupling）本质上是对现有方法的 post-hoc 分类。它确实帮助 organize related work，但作为 contribution（Introduction line 45 列为第二条贡献）值得商榷：
  - 仅有 5 个方法填入 3×3 矩阵（大部分格子为空）
  - 分类维度的选择缺乏理论动机（为什么选这两个轴而非其他？）
  - 没有预测性——不能用来预测 "下一个好方法" 应该在哪个格子
- 建议：降级为 "organizational framework" 而非 "contribution"，或添加实证证据支持这一分类对预测方法有效性有价值。

**W7** [warning] 无实际 wall-clock speedup 展示

- 具体位置：Section 4.6 Inference Efficiency, Appendix A
- 问题：论文声称 "activation sparsity can accelerate SwiGLU-based LLMs"（Abstract line 1），但 Appendix A Table 6 显示 KL-sparse pipeline 实际上 **增加** 了 6.4% 的延迟（126.78 vs. 119.11 ms）。论文也承认 "unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support"（Appendix A 最后段）。这意味着标题和 abstract 暗示的 "acceleration" 在当前实现中并不存在。
- 建议：Abstract 和 Introduction 应更明确地 scope 贡献为 "prediction quality" 而非 "acceleration"，避免误导读者。

---

## 小问题（不影响接收）

- **S1**: SPON 引用标注为 2026 ICML，但 OpenAlex 检索显示该论文发表时间为 2025。请核实 venue year。
- **S2**: Table 3 caption 说 "unified benchmark protocol"，Table 2 footnote 说 SPON analysis 用 `evaluate.py` protocol——两个 protocol 的差异未充分解释，读者难以判断 11.79 在两个 protocol 下的 "coincidental equality" 是否可信。
- **S3**: Introduction line 7 提到 FastForward 的 compensation network 有 67.2M 参数和 ~2.7% latency overhead，但未给出这一数字的来源（是否来自 FastForward 原文？Table 6 的 "+compensation" 行也恰好是 ~2.7%）。
- **S4**: Mistral-7B 实验（Section 4.6）PPL 8.98 恰好等于 LLaMA 30% sparsity 的 PPL 8.98（Table 3）——这一巧合值得注明以避免混淆。
- **S5**: WikiText-2 和 WikiText-103 分别用于评估和训练，但两者有 domain overlap——应讨论是否存在 train/eval leakage 风险。
- **S6**: 缺少 Ethics Statement（ARR 推荐但不强制）。
- **S7**: 匿名性检查通过——作者标注为 "Anonymous ACL submission"，未发现自引或代码链接暴露身份的线索。

---

## 主要优势

- **S+1**: 问题定义清晰，research question well-motivated——"proxy loss (BCE) vs. end-to-end loss (KL) for sparsity prediction" 是一个自然且重要的问题。
- **S+2**: 实验设计系统，ablation 分解合理——Table 2 逐步剥离 Gumbel/STE/BCE/compensation 的贡献，逻辑清晰。
- **S+3**: SPON orthogonality analysis (Section 4.6) 是有洞察力的分析——cosine similarity 0.196 和 L2 norm ratio 提供了定量证据说明 static correction 与 contextual prediction 的互补性。
- **S+4**: 三个 regime 的发现有实用价值——虽然普适性待验证，但 "30% sparsity 保下游任务、50% PPL 好但下游崩溃" 的实证规律对从业者有参考意义。
- **S+5**: 写作质量整体较好，gradient analysis (Section 3.6) 虽非深刻理论但展示清晰。
- **S+6**: Multi-seed stability (PPL std=0.07, CV<1%) 增强了结果的可靠性。

---

## 遗漏引用清单

1. **MaskLLM** (Fang et al., NeurIPS 2024 Spotlight): Learnable Semi-Structured Sparsity for Large Language Models — 使用 Gumbel Softmax 学习 N:M sparsity mask，技术组件高度相关
2. **MoE 相关综述/方法**: 建议讨论 contextual sparsity 与 MoE routing 的概念联系（如 Switch Transformer, GShard 等经典 MoE routing 使用的 Gumbel-based gating）
3. **KD for LLM compression 更新文献**: 除 Hinton (2015) 外，应引用更近期的 LLM-specific KD 工作（如 MiniLLM, GKD 等 2023-2024 工作）

---

## 引用准确性

通过 OpenAlex 自动验证，21 条引用全部为真实论文，无虚构引用。但有以下 mismatch：
- `xu2026spon`: bib 标注 year=2026 ICML，OpenAlex 返回 matched_year=2025（可能是 arXiv 2025 / ICML 2026 的差异）
- `grattafiori2024llama3`: OpenAlex 显示 matched_year=2025，bib 标注 2024（arXiv 发布 vs. 正式出版的差异）

---

## 总结评价

这是一篇执行扎实的 empirical paper，清晰展示了 KL distillation 在 sparsity prediction 任务上相对 BCE 的优势。但核心 novelty 不足以支撑 main conference：(1) SPON 已经使用 KL for sparsity，本文的增量是 per-token contextual prediction；(2) "end-to-end loss 优于 proxy loss" 在 ML 中是已知原则，gradient analysis 只是其形式化而非新发现；(3) 实验仅覆盖 7-8B 单一规模。建议投 Findings 或补充 13B+ 实验后重投 main conference。

格式方面，Limitations section 不合规和页数超限是 **必须立即修复** 的 desk-reject 风险。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-16T19:01:02.202283+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题存在，并简述理由\n- **[REBUT]**：反驳该问题，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 报告摘要\n\n**Overall**: 3/5 (Findings track)\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 训练/评估数据同源，存在过拟合风险\n- 训练数据 WikiText-103，评估 WikiText-2，两者来自同一 Wikipedia 数据源\n- 仅 1000 steps (~8M tokens) 极少训练量，可能学到 WikiText 特有 pattern\n- 无任何 OOD 评估（C4, The Pile）\n- 如果 PPL improvement 主要来自 domain overfitting，核心 contribution 不成立\n\n**N2** [critical] \"Structural failure, not computational\" 声明缺少充分证据\n- 仅试了一个 BCE configuration（未报告 LR search）\n- BCE 可能需要不同 LR/schedule、更大 predictor（d_b=256/512）\n- \"Loss saturation\" 不等于 \"structural limitation\"\n- KL 有 Gumbel + Lagrangian + temperature annealing 等多个 tricks，对比不公平\n\n**N3** [critical] 消融实验严重不足\n- Table 3 仅 4 行，缺失：d_b sensitivity、温度退火 schedule 对比、training steps curve、Lagrangian LR η_λ、训练数据 domain\n\n---\n\n### Should-Fix 问题\n\n**W1** 论文实际增加 6.4% 推理延迟，未实现 wall-clock 加速\n**W2** Cross-architecture 验证仅 Mistral-7B 一个模型，泛化 claim 过强\n**W3** 三 seed (n=3) 统计效力不足，95% CI for σ 在 n=3 时极宽\n**W4** 梯度分析是 informal argument 非 formal proof，缺 gradient SNR 对比\n**W5** Lagrangian 对偶更新无收敛保证，缺 λ 和 sparsity ratio 训练曲线\n\n---\n\n### 小问题\n- \"2.71×\" 应为 2.70×\n- \"saves ~2.7% latency\" 数值不精确\n- Table 1 multi-seed (uniform) vs main result (global) 的 PPL 差异容易混淆\n- \"Relative advantage\" metric 选择对方法有利\n\n---\n\n请逐条回应以上所有问题（Must-Fix N1-N3, Should-Fix W1-W5, 小问题）。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题存在，并简述理由\n- **[REBUT]**：反驳该问题，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 报告摘要\n\n**Overall**: 3/5 (Findings track)\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 训练/评估数据同源，存在过拟合风险\n- 训练数据 WikiText-103，评估 WikiText-2，两者来自同一 Wikipedia 数据源\n- 仅 1000 steps (~8M tokens) 极少训练量，可能学到 WikiText 特有 pattern\n- 无任何 OOD 评估（C4, The Pile）\n- 如果 PPL improvement 主要来自 domain overfitting，核心 contribution 不成立\n\n**N2** [critical] \"Structural failure, not computational\" 声明缺少充分证据\n- 仅试了一个 BCE configuration（未报告 LR search）\n- BCE 可能需要不同 LR/schedule、更大 predictor（d_b=256/512）\n- \"Loss saturation\" 不等于 \"structural limitation\"\n- KL 有 Gumbel + Lagrangian + temperature annealing 等多个 tricks，对比不公平\n\n**N3** [critical] 消融实验严重不足\n- Table 3 仅 4 行，缺失：d_b sensitivity、温度退火 schedule 对比、training steps curve、Lagrangian LR η_λ、训练数据 domain\n\n---\n\n### Should-Fix 问题\n\n**W1** 论文实际增加 6.4% 推理延迟，未实现 wall-clock 加速\n**W2** Cross-architecture 验证仅 Mistral-7B 一个模型，泛化 claim 过强\n**W3** 三 seed (n=3) 统计效力不足，95% CI for σ 在 n=3 时极宽\n**W4** 梯度分析是 informal argument 非 formal proof，缺 gradient SNR 对比\n**W5** Lagrangian 对偶更新无收敛保证，缺 λ 和 sparsity ratio 训练曲线\n\n---\n\n### 小问题\n- \"2.71×\" 应为 2.70×\n- \"saves ~2.7% latency\" 数值不精确\n- Table 1 multi-seed (uniform) vs main result (global) 的 PPL 差异容易混淆\n- \"Relative advantage\" metric 选择对方法有利\n\n---\n\n请逐条回应以上所有问题（Must-Fix N1-N3, Should-Fix W1-W5, 小问题）。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-16T19:01:17.890374+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15688
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-16T19:01:18.041561+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题存在，并简述理由\n- **[REBUT]**：反驳该问题，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 报告摘要\n\n**Overall**: 3.0/5 (Findings)\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] Limitations section 格式不合规\n- 当前为 conclusion 内 `\\paragraph{Limitations.}`\n- ARR 要求独立 `\\section*{Limitations}`（conclusion 之后、references 之前、不计页数）\n- 这是 desk-reject 条件之一\n\n**N2** [critical] 页数超限\n- Conclusion 含 Limitations 和 Future work 延伸至第 9 页顶部\n- ACL long paper 正文限制 ≤8 页\n- 即使拆出 Limitations 后可能刚好 8 页，当前状态超限\n\n**N3** [critical] 新颖性有限——与 SPON 的区分度不充分\n- SPON 已使用 KL divergence 训练 sparsity correction\n- 本文差异仅在于 per-token contextual mask + Gumbel-Sigmoid\n- 更像 SPON 的自然延伸而非根本性创新\n- SPON orthogonality analysis 反过来说明 SPON 的 KL training 已覆盖大部分信号\n\n---\n\n### Should-Fix 问题\n\n**W1** 遗漏重要相关工作：MaskLLM (NeurIPS 2024 Spotlight) — 使用 Gumbel Softmax 学 N:M sparsity mask\n**W2** MoE 与 contextual sparsity 的关联未讨论\n**W3** \"Structural mismatch\" 论述过度——\"proxy loss vs end-to-end loss\" 是 ML 基本认知\n**W4** BCE baseline 不充分——仅 vanilla BCE，缺 weighted BCE / BCE+ranking loss / soft targets 对比\n**W5** 三个 regime 的发现仅单模型验证，缺乏普适性\n**W6** 2D taxonomy 学术贡献有限——post-hoc 分类，无预测性\n**W7** 无实际 wall-clock speedup 展示\n\n---\n\n### 遗漏引用\n1. MaskLLM (Fang et al., NeurIPS 2024 Spotlight)\n2. MoE routing 相关工作 (Switch Transformer, GShard)\n3. LLM-specific KD (MiniLLM, GKD)\n\n### 小问题\n- S1: SPON year mismatch (bib=2026 ICML, OpenAlex=2025)\n- S2: 两个 evaluation protocol 差异未充分解释\n- S3: FastForward 67.2M/2.7% 数字来源不明\n- S4: Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合易混淆\n- S5: WikiText train/eval leakage 风险\n- S6: 缺 Ethics Statement\n- S7: 匿名性检查通过\n\n---\n\n请逐条回应以上所有问题（Must-Fix N1-N3, Should-Fix W1-W7, 遗漏引用, 小问题 S1-S7）。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题存在，并简述理由\n- **[REBUT]**：反驳该问题，并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 报告摘要\n\n**Overall**: 3.0/5 (Findings)\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] Limitations section 格式不合规\n- 当前为 conclusion 内 `\\paragraph{Limitations.}`\n- ARR 要求独立 `\\section*{Limitations}`（conclusion 之后、references 之前、不计页数）\n- 这是 desk-reject 条件之一\n\n**N2** [critical] 页数超限\n- Conclusion 含 Limitations 和 Future work 延伸至第 9 页顶部\n- ACL long paper 正文限制 ≤8 页\n- 即使拆出 Limitations 后可能刚好 8 页，当前状态超限\n\n**N3** [critical] 新颖性有限——与 SPON 的区分度不充分\n- SPON 已使用 KL divergence 训练 sparsity correction\n- 本文差异仅在于 per-token contextual mask + Gumbel-Sigmoid\n- 更像 SPON 的自然延伸而非根本性创新\n- SPON orthogonality analysis 反过来说明 SPON 的 KL training 已覆盖大部分信号\n\n---\n\n### Should-Fix 问题\n\n**W1** 遗漏重要相关工作：MaskLLM (NeurIPS 2024 Spotlight) — 使用 Gumbel Softmax 学 N:M sparsity mask\n**W2** MoE 与 contextual sparsity 的关联未讨论\n**W3** \"Structural mismatch\" 论述过度——\"proxy loss vs end-to-end loss\" 是 ML 基本认知\n**W4** BCE baseline 不充分——仅 vanilla BCE，缺 weighted BCE / BCE+ranking loss / soft targets 对比\n**W5** 三个 regime 的发现仅单模型验证，缺乏普适性\n**W6** 2D taxonomy 学术贡献有限——post-hoc 分类，无预测性\n**W7** 无实际 wall-clock speedup 展示\n\n---\n\n### 遗漏引用\n1. MaskLLM (Fang et al., NeurIPS 2024 Spotlight)\n2. MoE routing 相关工作 (Switch Transformer, GShard)\n3. LLM-specific KD (MiniLLM, GKD)\n\n### 小问题\n- S1: SPON year mismatch (bib=2026 ICML, OpenAlex=2025)\n- S2: 两个 evaluation protocol 差异未充分解释\n- S3: FastForward 67.2M/2.7% 数字来源不明\n- S4: Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合易混淆\n- S5: WikiText train/eval leakage 风险\n- S6: 缺 Ethics Statement\n- S7: 匿名性检查通过\n\n---\n\n请逐条回应以上所有问题（Must-Fix N1-N3, Should-Fix W1-W7, 遗漏引用, 小问题 S1-S7）。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-16T19:01:19.353221+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1311
}
```

</details>

---


### Assistant

_source line 78 · 2026-05-16T19:01:26.612450+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 79 · 2026-05-16T19:01:29.062868+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：

**Overall 3.0/5 (Findings)**。格式有两个 must-fix 问题（Limitations section 不合规 + 页数超限，均为 desk-reject 风险）。新颖性方面，SPON 已使用 KL for sparsity，本文的增量贡献是将 KL 扩展到 per-token contextual prediction，属于 "已知技术的新组合" 而非根本性创新。遗漏了重要相关工作 MaskLLM (NeurIPS 2024 Spotlight)。实验仅覆盖 7-8B 模型，"three regimes" 发现的普适性未验证。建议 Findings 或补充更大模型实验后重投 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-16T19:01:34.150435+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 81 · 2026-05-16T19:02:41.901422+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 训练/评估数据同源，存在过拟合风险**

同意这是实质性问题。WikiText-103（训练）和 WikiText-2（评估）确实源自同一 Wikipedia 语料库（Merity et al., 2017），predictor 可能学到 WikiText 特有的 activation pattern 分布。

但需补充两点细化：
1. 论文**有** OOD 评估——Table 3/4 的 ARC-c、WinoGrande、MMLU、GSM8K 均为非 WikiText domain，且这些结果确实显示了 KL 方法的优势（如 50% sparsity 下 WinoGrande 63.46 vs. TEAL 53.04）。因此"核心 contribution 不成立"的结论过强。
2. 更精确的担忧应该是：**PPL 层面的 improvement 幅度**（49% relative advantage at 50%）可能因 domain overlap 而被高估，但方法本身的方向性优势（KL > BCE > magnitude-only）在下游 benchmark 上仍成立。

建议作者补充 C4 或 The Pile 上的 PPL 评估，以确认 improvement 幅度的 domain robustness。

---

**[AGREE] R1-N2: "Structural failure" 声明缺少充分证据**

同意，这也是我在 W3 和 W4 中独立指出的问题。具体而言：

1. **对比不公平**：KL 训练有 Gumbel relaxation + Lagrangian constraint + cosine temperature annealing 三个关键 trick，而 BCE baseline 是 vanilla 版本。R1 正确指出应至少测试 BCE + soft targets 或 BCE + ranking auxiliary loss。我在 W4 中已提出相同建议。
2. **"Loss saturation" ≠ "structural limitation"**：R1 的论证逻辑正确。BCE loss 在 500-2700 steps 间仅下降 0.006（Section 4.2），但这可能是 learning rate 过大/过小导致的 optimization issue，而非 objective function 的根本缺陷。论文未报告 BCE 的 LR search 范围。
3. 不过，Section 3.6 的 gradient analysis（Eq. 7-8）在数学上是正确的：BCE gradient 确实是 per-neuron factorized（Eq. 8: $\partial \mathcal{L}_{BCE}/\partial s_j = \sigma(s_j) - m_j^*$），而 KL gradient 通过 Jacobian chain（Eq. 9 factor (b)）耦合所有 neuron。这一**数学事实**本身成立，但论文过度声称这是"发现"而非"已知原则的应用"。

总结：梯度分析正确，但"structural failure"的**实验证明**不充分。需要更 controlled 的 ablation 才能排除 optimization/hyperparameter confound。

---

**[PARTIALLY AGREE] R1-N3: 消融实验严重不足**

同意缺乏重要消融维度，但"严重不足"稍有过度：

**同意缺失的关键消融**：
- Bottleneck dimension $d_b$ sensitivity（当前固定 128，未测试 64/256/512）
- Temperature annealing schedule 对比（cosine vs. linear vs. fixed）
- Training steps learning curve（是否 1000 steps 已收敛？）
- Lagrangian dual LR $\eta_\lambda$（当前未报告具体值）

**但 Table 2 并非仅 4 行**——论文实际提供了以下消融维度：
- KL+Gumbel vs. KL+STE（Table 2: 11.79 vs. 15.77）
- BCE ± compensation（Table 2: 27.97 vs. 25.44）
- Global vs. uniform allocation at 3 sparsity levels（Table 4: 6 rows of KL results）
- Multi-seed stability（Appendix B: 3 seeds, std=0.07）
- SPON ± analysis（Section 4.6: orthogonality decomposition）

所以消融并非"严重不足"，而是**缺少几个关键维度**（特别是 $d_b$ 和 training schedule），但现有消融覆盖了 relaxation method 和 allocation strategy 两个核心设计选择。

---

### Should-Fix 问题

**[AGREE] R1-W1: 未实现 wall-clock 加速**

完全同意。我在 W7 中独立指出了相同问题。Appendix A Table 6 明确显示 KL-sparse pipeline **增加** 6.4% latency（126.78 vs. 119.11 ms），而非加速。Abstract 第一句 "can accelerate SwiGLU-based LLMs" 与实际结果矛盾。

---

**[AGREE] R1-W2: Cross-architecture 验证不足**

同意。仅 Mistral-7B-v0.3 一个额外模型，且只测了 50% sparsity 一个点（Section 4.6 最后段），无法支撑 "transferability to other SwiGLU architectures" 的 claim。我在 W5 中也指出应补测 Mistral 30%/40% 以验证 regime 边界是否转移。

补充：LLaMA-3.1-8B 和 Mistral-7B 都是 ~7-8B 参数、SwiGLU FFN、类似训练数据的模型——它们的相似性远大于差异性。真正的 cross-architecture 验证应包括不同规模（13B/70B）或不同 FFN 类型。

---

**[REBUT] R1-W3: 三 seed 统计效力不足**

部分不同意。R1 的统计论述本身正确（n=3 时 95% CI for σ 极宽），但需要 contextualize：

1. **ML 领域惯例**：3 seeds 是 NeurIPS/ICML/EMNLP 的常见做法（许多论文仅报告 single seed）。论文主动提供 3-seed variance 已经高于 baseline 标准。
2. **CV < 1% 的信号**：PPL 11.92 ± 0.07 的 coefficient of variation 为 0.6%，即使考虑 n=3 的 confidence interval 宽度，实际变异范围也很小。方法间的差异（KL 11.79 vs. BCE 27.97）远大于 seed variance，不存在 "方法间差异可能被 seed variance 解释" 的风险。
3. **但 R1 的建议仍有价值**：5 seeds 确实更好，且计算成本低（~17 min × 5 = ~85 min on A6000）。这是 easy win。

结论：统计效力的担忧在理论上成立，但在实践中不影响核心结论的可靠性。

---

**[AGREE] R1-W4: 梯度分析非 formal proof**

同意。Section 3.6 是 informal gradient decomposition，不构成 formal proof。论文将 Eq. 8-9 的 gradient chain 呈现为 "structural argument"（Introduction line 44: "provide a formal gradient analysis"），但实际上：
- 没有证明 KL gradient 的 coupling 一定导致更好的优化 landscape
- 没有 gradient SNR 或 gradient variance 的实证对比
- 没有排除 "KL 只是更好的 surrogate 但不是因为 coupling" 的可能性

这与我在 W3 中的判断一致：gradient analysis 数学正确但 novelty 有限，应弱化为 "motivation" 而非 "theoretical contribution"。

---

**[AGREE] R1-W5: Lagrangian 对偶更新缺收敛分析**

同意。Section 3.5 介绍了 Lagrangian relaxation（Eq. 11-12），但：
- 未报告 $\eta_\lambda$ 的具体值
- 未展示 $\lambda$ 的训练曲线（是否收敛？是否振荡？）
- 未展示实际 sparsity ratio 在训练过程中的变化（是否精确达到目标 $\rho$？）
- 无 convergence guarantee（虽然实践中 Lagrangian dual ascent 通常可行，但在有 Gumbel noise 的 non-convex setting 下理论保证缺失）

这是 reproducibility 层面的问题——读者无法从当前论文完全复现 Lagrangian 的调参细节。

---

### 小问题

**[AGREE] "2.71×" vs. "2.70×"**: 2700/1000 = 2.7，不是 2.71。Minor arithmetic error。

**[AGREE] "saves ~2.7% latency" 不精确**: Table 6 显示 compensation 版本（129.71 ms）vs. predictor-only（126.78 ms），差值 2.93 ms，约 2.3%——与 "~2.7%" 有出入。

**[AGREE] Table 1 multi-seed (uniform) vs main result (global) 容易混淆**: Table 1 caption 的 footnote 说 "Multi-seed variance (3 seeds, 50% uniform): PPL std=0.07"，但 Table 1 主行的 KL global 报的是 PPL 11.79（单 seed）。两个 protocol 的 PPL 差异（11.79 global vs. 11.92 uniform mean）在同一个 table 的 caption 中出现，确实容易误导。

**[REBUT] "Relative advantage" metric 选择对方法有利**: Table 3 的 "Relative advantage" 定义为 $(PPL_{TEAL} - PPL_{KL}) / PPL_{TEAL}$，这是标准的 relative improvement metric。任何 baseline 更差时 relative improvement 都会更大——这是 relative metric 的数学性质，不是 cherry-picking。但论文确实没有显式定义这个 metric 的计算公式，应在 caption 或正文中明确。

---

### 交叉回应总结

| R1 Issue | R2 Verdict | 理由 |
|----------|------------|------|
| N1 Data overlap | AGREE (with nuance) | PPL 幅度可能高估，但下游 benchmark 提供了部分 OOD 验证 |
| N2 Structural claim | AGREE | 对比不公平 + loss saturation ≠ structural limitation |
| N3 Ablation gaps | PARTIALLY AGREE | 缺 $d_b$/schedule/Lagrangian LR，但现有消融非"严重不足" |
| W1 No speedup | AGREE | 与我的 W7 独立一致 |
| W2 Limited cross-arch | AGREE | 与我的 W5 独立一致 |
| W3 Three seeds | REBUT | ML 惯例 + 方法间差异远大于 seed variance |
| W4 Informal gradient | AGREE | 与我的 W3 独立一致 |
| W5 Lagrangian missing | AGREE | Reproducibility concern |

两位 Reviewer 独立一致的 critical issues：(1) 对比公平性不足（N2/W3-W4），(2) 实验规模有限（W2/W5），(3) 无实际加速（W1/W7）。这些共同指向 Findings track 而非 Main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 82 · 2026-05-16T19:02:47.258360+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 83 · 2026-05-16T19:02:49.713741+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 的 7 个 Should-Fix 和 3 个 Must-Fix 中，我同意 N1（data overlap，但 nuanced——下游 benchmark 提供部分 OOD 验证）、N2（structural claim 不充分）、W1/W2/W4/W5，部分同意 N3（消融不足但非"严重"），反驳 W3（3 seeds 在 ML 惯例下可接受）。两位 Reviewer 独立一致认为论文更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 84 · 2026-05-16T19:02:55.491534+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 8

## Round 8

8 recorded events


### User

_source line 85 · 2026-05-16T19:02:56.996555+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2

---

### Must-Fix 问题

**[AGREE] R2-N1: Limitations section 格式不合规**

同意。我确认 `conclusion.tex` 中使用的是 `\paragraph{Limitations.}` 嵌在 Conclusion 内，而非独立的 `\section*{Limitations}`。ARR Author Guidelines 明确要求 Limitations 为独立 section（conclusion 之后、references 之前、不占页数）。这确实是 desk-reject 条件。我在自己的审稿中未将此列为单独问题（我的审查侧重在方法/实验），但 R2 的判断完全正确。

**[AGREE] R2-N2: 页数超限**

同意这是一个需要确认的 formatting risk。当前 Conclusion 包含 Limitations + Future work 共约 25 行正文（conclusion.tex），加上 Method 和 Experiments 的密度（多个 table 和 figure），很可能超 8 页。不过我无法 100% 确认——需要编译 PDF 实测。如果拆出 Limitations 并 tighten future work，可能刚好 8 页。我建议作者编译确认并必要时压缩。

**[REBUT] R2-N3: 新颖性有限——与 SPON 的区分度不充分**

R2 的核心论点是"本文仅是 SPON 的自然延伸"，我不同意这个判断。理由：

1. **方法差异是 fundamental 的，不是 incremental 的**：SPON 学习的是 input-independent per-layer bias vector（§2 Related Work: "learns input-independent bias vectors via KL divergence, absorbed into parameters at zero inference cost"）。本文学习的是 input-dependent per-token contextual mask（2.37M 参数/层的 MLP predictor）。这是"static correction"与"dynamic prediction"的根本区别——一个是加法偏置，一个是乘法 gating。

2. **SPON orthogonality analysis 的正确解读**：R2 称"SPON 的 KL training 已覆盖大部分信号"，但§4.4 的数据说的恰恰相反——cosine similarity 0.196 意味着 SPON 的修正方向与 predictor 几乎正交，SPON 只贡献 2.4% relative improvement (12.08→11.79)。这证明 **SPON 未能捕获 predictor 捕获的信号**，而非"SPON 已覆盖大部分"。Predictor 的 L2 norm 为 482.65，SPON 为 76.2（仅 15.8%）——信号主体在 predictor 而非 SPON。

3. **技术框架完全不同**：SPON 不需要 Gumbel relaxation（因为它不做 discrete mask decision），不需要 Lagrangian constraint（因为它不控制 sparsity ratio），不需要 end-to-end differentiable forward pass through masks。本文的技术贡献在于如何让 KL training work for discrete mask decisions——这是 SPON 完全没有解决的问题。

不过，我承认论文可以更好地 articulate 这一区别。当前写法（§2, §4.4）分散在多处，reader 需要自行拼合。

---

### Should-Fix 问题

**[AGREE] R2-W1: 遗漏 MaskLLM (NeurIPS 2024 Spotlight)**

强烈同意。MaskLLM 使用 Gumbel-Softmax 学习 N:M sparsity masks，与本文在技术手法（Gumbel relaxation for discrete mask learning）和问题设置（learned sparsity prediction for LLMs）上高度相关。遗漏此引用是一个明显的疏忽。论文应在 Related Work 中讨论 MaskLLM 并明确区分（MaskLLM 针对 N:M structured pattern，本文针对 unstructured contextual sparsity with global top-k allocation）。

**[AGREE] R2-W2: MoE 与 contextual sparsity 的关联未讨论**

部分同意。Contextual sparsity prediction 确实与 MoE routing 有 conceptual similarity（both 做 input-dependent computation selection）。一两句讨论 MoE routing literature 和本文 setting 的区别（MoE 选 expert = coarse-grained block selection；本文选 neurons = fine-grained element selection）会 strengthen related work。但我不认为这是 critical omission——问题域和粒度差异足够大。

**[AGREE] R2-W3: "Structural mismatch" 论述过度**

同意。我在自己的 W4 中也提出了类似观点。"Per-neuron proxy loss vs end-to-end loss performs worse" 确实是 ML 的 common wisdom（distillation > classification in many settings）。论文将此 frame 为"structural insight"并用一整个 §3.5 展开梯度分析有些 overselling。核心贡献应定位在 **empirical demonstration + practical recipe**（Gumbel + Lagrangian + temperature annealing 使其 work）而非 theoretical novelty。

**[AGREE] R2-W4: BCE baseline 不充分**

强烈同意。这与我的 N2 (Must-Fix) 完全一致。论文只试了 vanilla BCE 一个配置就宣称"structural failure"，缺少 weighted BCE、BCE + ranking loss、soft-target BCE、不同 LR/architecture 的对比。这严重削弱了核心 narrative。

**[AGREE] R2-W5: 三个 regime 仅单模型验证**

同意。Budget-surplus / budget-constrained / capacity-limited 的 regime 划分是有 insight 的观察，但基于单模型（LLaMA-3.1-8B）。这些 boundary 是否在不同 model sizes 下 shift？在 13B 上 50% sparsity 是否仍是 capacity-limited？缺乏验证使这个 finding 的 generalizability 存疑。

**[REBUT] R2-W6: 2D taxonomy 学术贡献有限**

部分反驳。我同意 taxonomy 是 post-hoc classification 而非有预测性的理论框架。但我认为它仍有 organizational value：
1. 它清晰地 identify 了本文 contribution 相对于 prior work 的位置（Table 1, §3.6）
2. 它帮助 reader 快速理解方法空间的 landscape
3. "Post-hoc"不等于"无价值"——periodic table 也是 post-hoc classification

不过 R2 的批评对于将 taxonomy 作为 "contribution" 列在 bullet points 中是合理的——它更适合作为 presentation device 而非 standalone contribution。

**[AGREE] R2-W7: 无实际 wall-clock speedup 展示**

完全同意。我在自己的 W1 中提出了同样的问题。Appendix A 明确承认当前实现增加 6.4% overhead 且 unstructured masks 不产生实际加速。论文应更诚实地 frame 为 prediction quality 研究。

---

### 遗漏引用

**[AGREE] MaskLLM (Fang et al., NeurIPS 2024)**：直接相关，必须引用。

**[AGREE partially] MoE routing (Switch Transformer, GShard)**：值得在 Related Work 中简短提及以 discuss connection/distinction，但非 critical omission。

**[AGREE partially] LLM-specific KD (MiniLLM, GKD)**：与本文的 KL distillation 有方法论 overlap，值得引用。不过本文的 distillation 目标是 mask predictor（不改变 base model weights），与 MiniLLM/GKD 的 model distillation 有 fundamental 区别。

---

### 小问题

**[AGREE] S1: SPON year mismatch**：如果 bib 标注 2026 ICML 但实际发表于 2025，这是 citation accuracy 问题，应修正。

**[AGREE] S2: 两个 evaluation protocol 差异未充分解释**：我在自己的小问题中也指出了这点。Table 1 footnote 尝试解释但不够清晰。两个 protocol 下 PPL=11.79 的"coincidental equality"增加了混淆。

**[AGREE] S3: FastForward 67.2M/2.7% 数字来源不明**：论文多次引用"67.2M parameters and ~2.7% additional latency"作为 compensation network 的 cost，但这些数字是否来自 FastForward 原文、作者自己的 reimplementation、还是估算？应标注来源。

**[AGREE] S4: Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合**：确实容易让 reader 混淆。建议加一句 clarification 或在 Table 中并排呈现时加注。

**[AGREE] S5: WikiText train/eval leakage 风险**：这与我的 N1 (Must-Fix) 一致。WikiText-103 训练 + WikiText-2 评估存在 domain overlap 风险。

**[AGREE] S6: 缺 Ethics Statement**：ARR 要求 Ethics Statement section。如果确实缺失，与 N1 (Limitations) 同属格式合规问题。

**[AGREE] S7: 匿名性检查通过**：确认。

---

### 总结

R2 的审稿与我的审稿高度互补。我们在以下关键问题上达成共识：
1. BCE baseline 给的不公平（我的 N2 = R2 的 W4）
2. 无 wall-clock speedup（我的 W1 = R2 的 W7）
3. WikiText leakage 风险（我的 N1 = R2 的 S5）
4. "Structural failure" claim 过强（我的 N2 ≈ R2 的 W3）

我与 R2 的主要分歧在 **N3 (novelty vs SPON)**：我认为本文与 SPON 的技术差异是 fundamental 的（static bias vs dynamic contextual mask, 完全不同的训练框架），SPON orthogonality 数据支持本文而非削弱本文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-16T19:03:21.884286+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-16T19:03:21.935065+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-16T19:04:11.886975+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规——当前为 conclusion 内 paragraph，ARR 要求独立 section*\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 交叉回应 AGREE。desk-reject 条件。\"}\n    action_items:\n      - {round: 1, action: \"将 \\\\paragraph{Limitations.} 和 Future work 拆为独立 \\\\section*{Limitations}，置于 conclusion 之后 bibliography 之前\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"页数超限——正文含 Limitations/Future work 延伸至第 9 页，long paper 限 8 页\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 AGREE（需编译确认）。拆 Limitations 后可能刚好 8 页。\"}\n    action_items:\n      - {round: 1, action: \"拆出 Limitations 后编译确认页数；如仍超限，压缩 Section 4（Table 4/5 有信息重复可合并）\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N1\"\n    summary: \"训练/评估数据同源（WikiText-103→WikiText-2），缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 critical。R2 AGREE with nuance: 下游 benchmark 提供部分 OOD 验证，但 PPL improvement 幅度可能高估。\"}\n    action_items:\n      - {round: 1, action: \"补充 C4 或 The Pile test set 的 PPL 评估，或在不同训练数据上训练后评估\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"'Structural failure' 声明缺充分证据——BCE 仅测一个 configuration，对比不公平\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 critical，R2 在 W3/W4 独立指出相同问题并交叉 AGREE。BCE 有 Gumbel+Lagrangian+annealing 而 KL 没有对等控制。\"}\n    action_items:\n      - {round: 1, action: \"对 BCE 做 LR grid search + 至少测试 soft-target BCE 或 BCE+ranking loss；或弱化 claim 为 'under our setting'\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"消融实验缺关键维度——d_b sensitivity、温度 schedule、training curve、Lagrangian LR\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 列为 critical，R2 交叉回应 PARTIALLY AGREE（现有消融覆盖 relaxation 和 allocation，但缺几个关键维度）。降为 warning。\"}\n    action_items:\n      - {round: 1, action: \"补充 d_b={64,128,256,512} sensitivity + training steps learning curve\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"论文增加 6.4% 推理延迟，未实现 wall-clock 加速，与 abstract/intro framing 矛盾\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7，两人独立一致 AGREE。\"}\n    action_items:\n      - {round: 1, action: \"Abstract/Intro 重新 frame 为 prediction quality 研究，弱化 acceleration claim\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Cross-architecture 验证仅 Mistral-7B 一个模型且仅 50% 一个点，泛化 claim 过强\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W2 = R2-W5，两人独立一致 AGREE。\"}\n    action_items:\n      - {round: 1, action: \"弱化措辞为 'preliminary evaluation on one additional model'，或补测 Mistral 30%/40%\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"新颖性有限——与 SPON 区分度不充分，核心技术为已知方法的新组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 列为 critical，R1 交叉 REBUT（技术差异 fundamental: static bias vs dynamic mask, orthogonality 数据支持差异）。存在分歧，降为 warning。\"}\n    action_items:\n      - {round: 1, action: \"更清晰地 formalize per-token vs static KL 的差异，或补充更强实验证据\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"遗漏重要相关工作 MaskLLM (Fang et al., NeurIPS 2024 Spotlight)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 强烈 AGREE。MaskLLM 使用 Gumbel-Softmax 学 N:M sparsity mask，技术高度相关。\"}\n    action_items:\n      - {round: 1, action: \"Related Work 增加 MaskLLM 讨论并区分（N:M structured vs unstructured top-k）\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 (§3.5) 是 informal argument，论文 oversell 为 theoretical contribution\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W4 ≈ R2-W3，两人独立一致 AGREE。数学正确但非深刻理论贡献。\"}\n    action_items:\n      - {round: 1, action: \"弱化为 'intuitive motivation' 而非 'formal gradient analysis'；或补充 gradient SNR 实证\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Lagrangian 对偶更新缺收敛分析——未报告 η_λ、λ 轨迹、实际 sparsity ratio 曲线\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出，R2 交叉 AGREE（reproducibility concern）。\"}\n    action_items:\n      - {round: 1, action: \"Appendix 补充 λ 和 sparsity ratio over training steps 的曲线图\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W6\"\n    summary: \"2D taxonomy 作为 contribution 列出，但实为 post-hoc classification，贡献有限\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出 warning，R1 部分 REBUT（有 organizational value 但同意不应为 standalone contribution）。降为 info。\"}\n    action_items:\n      - {round: 1, action: \"降级为 organizational framework，不作为独立 contribution bullet\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"三 seed (n=3) 统计效力弱\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 warning，R2 REBUT（ML 惯例可接受，方法间差异远大于 seed variance）。降为 info。\"}\n    action_items:\n      - {round: 1, action: \"如时间允许扩展到 5 seeds（easy win），否则保持现状\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规——当前为 conclusion 内 paragraph，ARR 要求独立 section*\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 交叉回应 AGREE。desk-reject 条件。\"}\n    action_items:\n      - {round: 1, action: \"将 \\\\paragraph{Limitations.} 和 Future work 拆为独立 \\\\section*{Limitations}，置于 conclusion 之后 bibliography 之前\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"页数超限——正文含 Limitations/Future work 延伸至第 9 页，long paper 限 8 页\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 AGREE（需编译确认）。拆 Limitations 后可能刚好 8 页。\"}\n    action_items:\n      - {round: 1, action: \"拆出 Limitations 后编译确认页数；如仍超限，压缩 Section 4（Table 4/5 有信息重复可合并）\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N1\"\n    summary: \"训练/评估数据同源（WikiText-103→WikiText-2），缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 critical。R2 AGREE with nuance: 下游 benchmark 提供部分 OOD 验证，但 PPL improvement 幅度可能高估。\"}\n    action_items:\n      - {round: 1, action: \"补充 C4 或 The Pile test set 的 PPL 评估，或在不同训练数据上训练后评估\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"'Structural failure' 声明缺充分证据——BCE 仅测一个 configuration，对比不公平\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 critical，R2 在 W3/W4 独立指出相同问题并交叉 AGREE。BCE 有 Gumbel+Lagrangian+annealing 而 KL 没有对等控制。\"}\n    action_items:\n      - {round: 1, action: \"对 BCE 做 LR grid search + 至少测试 soft-target BCE 或 BCE+ranking loss；或弱化 claim 为 'under our setting'\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"消融实验缺关键维度——d_b sensitivity、温度 schedule、training curve、Lagrangian LR\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 列为 critical，R2 交叉回应 PARTIALLY AGREE（现有消融覆盖 relaxation 和 allocation，但缺几个关键维度）。降为 warning。\"}\n    action_items:\n      - {round: 1, action: \"补充 d_b={64,128,256,512} sensitivity + training steps learning curve\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1\"\n    summary: \"论文增加 6.4% 推理延迟，未实现 wall-clock 加速，与 abstract/intro framing 矛盾\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7，两人独立一致 AGREE。\"}\n    action_items:\n      - {round: 1, action: \"Abstract/Intro 重新 frame 为 prediction quality 研究，弱化 acceleration claim\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Cross-architecture 验证仅 Mistral-7B 一个模型且仅 50% 一个点，泛化 claim 过强\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W2 = R2-W5，两人独立一致 AGREE。\"}\n    action_items:\n      - {round: 1, action: \"弱化措辞为 'preliminary evaluation on one additional model'，或补测 Mistral 30%/40%\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"新颖性有限——与 SPON 区分度不充分，核心技术为已知方法的新组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 列为 critical，R1 交叉 REBUT（技术差异 fundamental: static bias vs dynamic mask, orthogonality 数据支持差异）。存在分歧，降为 warning。\"}\n    action_items:\n      - {round: 1, action: \"更清晰地 formalize per-token vs static KL 的差异，或补充更强实验证据\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"遗漏重要相关工作 MaskLLM (Fang et al., NeurIPS 2024 Spotlight)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 强烈 AGREE。MaskLLM 使用 Gumbel-Softmax 学 N:M sparsity mask，技术高度相关。\"}\n    action_items:\n      - {round: 1, action: \"Related Work 增加 MaskLLM 讨论并区分（N:M structured vs unstructured top-k）\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 (§3.5) 是 informal argument，论文 oversell 为 theoretical contribution\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W4 ≈ R2-W3，两人独立一致 AGREE。数学正确但非深刻理论贡献。\"}\n    action_items:\n      - {round: 1, action: \"弱化为 'intuitive motivation' 而非 'formal gradient analysis'；或补充 gradient SNR 实证\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"Lagrangian 对偶更新缺收敛分析——未报告 η_λ、λ 轨迹、实际 sparsity ratio 曲线\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出，R2 交叉 AGREE（reproducibility concern）。\"}\n    action_items:\n      - {round: 1, action: \"Appendix 补充 λ 和 sparsity ratio over training steps 的曲线图\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W6\"\n    summary: \"2D taxonomy 作为 contribution 列出，但实为 post-hoc classification，贡献有限\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出 warning，R1 部分 REBUT（有 organizational value 但同意不应为 standalone contribution）。降为 info。\"}\n    action_items:\n      - {round: 1, action: \"降级为 organizational framework，不作为独立 contribution bullet\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"三 seed (n=3) 统计效力弱\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 warning，R2 REBUT（ML 惯例可接受，方法间差异远大于 seed variance）。降为 info。\"}\n    action_items:\n      - {round: 1, action: \"如时间允许扩展到 5 seeds（easy win），否则保持现状\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-16T19:04:11.937778+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 6785}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-16T19:05:48.736744+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 1\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 Main Conference (Efficient Methods for NLP)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+格式合规）\n**审稿轮次**: Round 1（独立审稿 + 交叉分享，1 轮收敛）\n\n---\n\n## Summary\n\n本文提出用 KL divergence（配合 Gumbel-Sigmoid relaxation 和 Lagrangian sparsity constraint）训练 SwiGLU LLM 的轻量级 contextual sparsity predictor，替代传统 BCE 训练目标。在 LLaMA-3.1-8B 上 50% sparsity 下达到 PPL 11.79（vs TEAL 23.31, BCE 27.97），无需 compensation network。论文还提出 2D taxonomy 和三 sparsity regime 分析。\n\n---\n\n## Strengths\n\n1. **问题定义清晰且重要** — \"BCE per-neuron decomposition vs global top-k allocation 的 mismatch\" 观察敏锐，research question well-motivated [R1, R2 一致]\n2. **核心实验结果显著** — PPL 11.79 vs 23.31 (TEAL) / 27.97 (BCE) 的差距大且一致，KL advantage 随 sparsity 增长（18%→49%→82%）[R1, R2 一致]\n3. **SPON orthogonality 分析有洞察** — cosine similarity 0.196 + L2 norm ratio 定量证明 static correction 与 contextual prediction 的互补性 [R1, R2 一致]\n4. **论文整体写作质量好** — 结构清晰，gradient analysis 展示明白，三个 regime 分析有实用价值 [R1, R2 一致]\n5. **Reproducibility 良好** — 训练细节充分（1000 steps, AdamW, lr=1e-3, A6000 17min），实用性强 [R1 4/5, R2 4/5]\n6. **Honest limitations** — 坦诚承认无 wall-clock speedup、单一规模、PPL 作为 proxy 的局限 [R1]\n\n---\n\n## Weaknesses\n\n### Critical（Must-Fix，影响接收决定）\n\n**C1. Limitations section 格式不合规 [desk-reject risk]**\n- 当前为 `\\paragraph{Limitations.}` 嵌在 Conclusion 内\n- ARR 要求独立 `\\section*{Limitations}`（conclusion 之后、references 之前、不计页数）\n- [R2 提出, R1 AGREE] — 这是 ARR desk-reject 条件\n\n**C2. 页数超限 [desk-reject risk]**\n- Conclusion + Limitations + Future work 延伸至第 9 页，long paper 正文限 ≤8 页\n- 拆出 Limitations 后需重新编译确认\n- [R2 提出, R1 AGREE]\n\n**C3. 训练/评估数据同源，缺 OOD 验证**\n- WikiText-103（训练）→ WikiText-2（评估）共享 Wikipedia domain\n- 1000 steps (~8M tokens) 极少训练量下存在 domain overfitting 风险\n- PPL improvement 幅度（49% relative）可能因 domain overlap 被高估\n- 下游 benchmark（ARC-c, WinoGrande, MMLU, GSM8K）提供部分 OOD 验证，但 PPL 是 primary metric\n- [R1 提出 critical, R2 AGREE with nuance]\n\n**C4. \"Structural failure\" 声明证据不足**\n- 仅测试一个 vanilla BCE configuration，未做 LR search / architecture size sweep\n- KL 有 Gumbel + Lagrangian + temperature annealing 三个 trick，BCE 无对等优化\n- \"Loss saturation\" 可能是 optimization issue 而非 structural limitation\n- 需要至少 soft-target BCE 或 BCE + ranking loss 对比才能支撑 \"structural\" 断言\n- [R1 提出 critical, R2 在 W3/W4 独立提出相同观点, 交叉 AGREE]\n\n### Warning（Should-Fix，影响评分）\n\n**W1. 消融实验缺关键维度**\n- 缺 d_b sensitivity（仅用 128，无 64/256/512 对比）\n- 缺温度退火 schedule 对比（cosine vs linear vs fixed）\n- 缺 training steps learning curve\n- 缺 Lagrangian LR η_λ 报告\n- [R1 列为 critical, R2 PARTIALLY AGREE — 现有消融覆盖 relaxation/allocation 但缺几个维度, 协商降为 warning]\n\n**W2. 无 wall-clock 加速，framing 误导**\n- Appendix A: pipeline 增加 6.4% latency（126.78 vs 119.11 ms）\n- Abstract/Intro 暗示 \"acceleration\" 但实际无法实现\n- 应 frame 为 prediction quality 研究\n- [R1-W1 = R2-W7, 两人独立一致]\n\n**W3. Cross-architecture 验证不足**\n- 仅 Mistral-7B-v0.3 一个额外模型，仅 50% 一个 sparsity point\n- LLaMA-8B 和 Mistral-7B 极为相似（同规模、同 FFN 类型）\n- \"Transferability\" claim 过强\n- [R1-W2 = R2-W5, 两人独立一致]\n\n**W4. 遗漏重要相关工作 MaskLLM**\n- MaskLLM (Fang et al., NeurIPS 2024 Spotlight) 使用 Gumbel-Softmax 学 N:M sparsity mask for LLMs\n- 技术组件高度相关（Gumbel relaxation + learnable mask + frozen weights）\n- 必须在 Related Work 讨论并区分\n- [R2 提出, R1 强烈 AGREE]\n\n**W5. 梯度分析 overselling**\n- §3.5 数学正确但非深刻理论贡献\n- \"Proxy loss vs end-to-end loss 的差异\" 是 ML 基本认知\n- 论文称 \"formal gradient analysis\" 但实为 informal argument\n- 缺 gradient SNR / variance 的实证对比\n- [R1-W4 ≈ R2-W3, 两人独立一致]\n\n**W6. Lagrangian 缺收敛分析**\n- 未报告 η_λ 具体值、λ 训练曲线、实际 sparsity ratio 是否达标\n- 在 non-convex + Gumbel noise setting 下无理论收敛保证\n- Reproducibility concern\n- [R1-W5, R2 交叉 AGREE]\n\n**W7. 三个 regime 仅单模型验证**\n- Budget-surplus / budget-constrained / capacity-limited 边界仅 LLaMA-3.1-8B 确定\n- 未验证 regime 边界是否随 model scale 变化\n- [R2-W5, R1 交叉 AGREE]\n\n### Info（Minor Issues）\n\n- 2D taxonomy 作为 contribution 列出但实为 post-hoc classification [R2-W6, R1 部分 REBUT — 有 organizational value]\n- 3-seed (n=3) 统计效力弱 [R1-W3, R2 REBUT — ML 惯例可接受]\n- \"2.71×\" 应为 2.70× (2700/1000=2.7)\n- \"~2.7% latency saving\" 数值不精确（实际 ~2.3%）\n- Table 1 multi-seed (uniform, 11.92) vs main result (global, 11.79) 容易混淆\n- Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合未注明\n- SPON bib year=2026 ICML vs OpenAlex=2025，需核实\n- FastForward 67.2M/2.7% 数字来源未标注\n- 两个 evaluation protocol 差异未充分解释\n- 缺 Ethics Statement（ARR 推荐但不强制）\n- 缺 MoE routing 概念关联讨论\n- 缺 LLM-specific KD 更新文献 (MiniLLM, GKD)\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上独立达成一致：\n1. BCE baseline 不公平 → \"structural failure\" claim 过强 (C4)\n2. 无 wall-clock 加速与 framing 矛盾 (W2)\n3. WikiText data overlap 风险 (C3)\n4. Cross-architecture 验证不足 (W3)\n5. MaskLLM 引用遗漏 (W4)\n6. Lagrangian 缺细节 (W6)\n7. 格式不合规 (C1, C2)\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**Novelty vs SPON (R2-N3 vs R1-REBUT)**\n\n- R2 认为：本文与 SPON 的差异仅为 per-token vs static，属于 \"自然延伸\"，novelty 不足以支撑 main conference\n- R1 反驳：(1) Static bias vs dynamic contextual mask 是 fundamental 差异（加法偏置 vs 乘法 gating）；(2) SPON orthogonality data（cosine 0.196, L2 ratio 15.8%）证明 SPON 未捕获 predictor 的信号；(3) 技术框架完全不同（SPON 无需 Gumbel/Lagrangian/end-to-end differentiable mask）\n- **Director 判断**：R1 的论据更强——SPON 和本文解决的是不同子问题（static correction vs contextual prediction），技术栈无交集。但 R2 的 concern 仍部分成立：论文 framing 可以更清晰地 articulate 与 SPON 的差异。记录为 warning 而非 critical。\n\n---\n\n## Questions to Authors\n\n1. BCE 实验中使用的 learning rate 和 schedule？是否做过 LR search？\n2. d_b=128 是如何选择的？preliminary 实验数据？\n3. 能否提供 C4 或 Pile test set 上的 PPL？\n4. Lagrangian multiplier λ 的训练轨迹？实际 sparsity ratio 是否达标？\n5. 给 BCE 同样的 Gumbel-Sigmoid + Lagrangian 框架（仅换 loss），性能如何？——这能更 cleanly 隔离 loss function 的贡献\n6. MaskLLM 与本文的关系和区别？\n\n---\n\n## Missing References\n\n1. **MaskLLM** (Fang et al., NeurIPS 2024 Spotlight) — Learnable Semi-Structured Sparsity, Gumbel-Softmax for N:M mask learning [必须引用]\n2. **MoE routing** (Switch Transformer, GShard) — 概念关联讨论 [建议引用]\n3. **LLM-specific KD** (MiniLLM, GKD) — 方法论 overlap [建议引用]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 / 5 — Borderline (Findings track recommended)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立给出相同评分（R1: 3/5, R2: 3.0/5），均推荐 Findings track。\n\n**核心判断**：论文有清晰的 research question 和显著的 empirical result（KL >> BCE >> magnitude-only），但存在以下系统性不足：\n1. **格式风险**：Limitations 不合规 + 页数超限 = desk-reject 可能\n2. **实验严谨性**：OOD 验证缺失、BCE baseline 不公平、关键消融缺失\n3. **Claim 校准**：\"structural failure\" 和 \"acceleration\" 的 claim 超出了证据支撑范围\n4. **规模局限**：仅 7-8B 模型，cross-architecture/cross-scale 验证不足\n\n如果作者能解决 C1-C2（格式）、C3（OOD eval）、C4（BCE fairness），并弱化 overclaiming，论文质量可提升至 weak accept 水平。当前状态更适合 Findings track。\n\n---\n\n## Detailed Comments (按 section)\n\n### Abstract & Introduction\n- \"can accelerate SwiGLU-based LLMs\" 与实际 6.4% overhead 矛盾，需 reframe\n- \"formal gradient analysis\" 应降为 \"gradient-based motivation\"\n- 三条 contribution 中 taxonomy 可降为 organizational framework\n\n### Method (§3)\n- 梯度分析数学正确但非 novel theoretical contribution\n- Lagrangian §3.4 缺 η_λ 值和收敛讨论\n- Gumbel-Sigmoid 的选择 well-motivated (vs STE ablation)\n\n### Experiments (§4)\n- Core result (Table 2) 强且 consistent\n- Iso-compute analysis (§4.2) 需更 controlled 对比（BCE + same framework tricks）\n- SPON analysis (§4.4) 有 insight\n- Cross-architecture (§4.6) 仅 1 model, 1 sparsity point — 不足以支撑 claim\n- Latency (Appendix A) 诚实但与 framing 矛盾\n\n### Related Work (§2)\n- MaskLLM 遗漏是 major gap\n- MoE connection 值得一提\n- 现有引用准确（经 OpenAlex 验证，21 条均为真实论文）\n\n### Format\n- Limitations: 必须拆为独立 section*\n- 页数: 需编译确认（可能 border-line）\n- 匿名性: 通过 ✓\n- 模板: ACL review style ✓\n",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 1\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 Main Conference (Efficient Methods for NLP)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+格式合规）\n**审稿轮次**: Round 1（独立审稿 + 交叉分享，1 轮收敛）\n\n---\n\n## Summary\n\n本文提出用 KL divergence（配合 Gumbel-Sigmoid relaxation 和 Lagrangian sparsity constraint）训练 SwiGLU LLM 的轻量级 contextual sparsity predictor，替代传统 BCE 训练目标。在 LLaMA-3.1-8B 上 50% sparsity 下达到 PPL 11.79（vs TEAL 23.31, BCE 27.97），无需 compensation network。论文还提出 2D taxonomy 和三 sparsity regime 分析。\n\n---\n\n## Strengths\n\n1. **问题定义清晰且重要** — \"BCE per-neuron decomposition vs global top-k allocation 的 mismatch\" 观察敏锐，research question well-motivated [R1, R2 一致]\n2. **核心实验结果显著** — PPL 11.79 vs 23.31 (TEAL) / 27.97 (BCE) 的差距大且一致，KL advantage 随 sparsity 增长（18%→49%→82%）[R1, R2 一致]\n3. **SPON orthogonality 分析有洞察** — cosine similarity 0.196 + L2 norm ratio 定量证明 static correction 与 contextual prediction 的互补性 [R1, R2 一致]\n4. **论文整体写作质量好** — 结构清晰，gradient analysis 展示明白，三个 regime 分析有实用价值 [R1, R2 一致]\n5. **Reproducibility 良好** — 训练细节充分（1000 steps, AdamW, lr=1e-3, A6000 17min），实用性强 [R1 4/5, R2 4/5]\n6. **Honest limitations** — 坦诚承认无 wall-clock speedup、单一规模、PPL 作为 proxy 的局限 [R1]\n\n---\n\n## Weaknesses\n\n### Critical（Must-Fix，影响接收决定）\n\n**C1. Limitations section 格式不合规 [desk-reject risk]**\n- 当前为 `\\paragraph{Limitations.}` 嵌在 Conclusion 内\n- ARR 要求独立 `\\section*{Limitations}`（conclusion 之后、references 之前、不计页数）\n- [R2 提出, R1 AGREE] — 这是 ARR desk-reject 条件\n\n**C2. 页数超限 [desk-reject risk]**\n- Conclusion + Limitations + Future work 延伸至第 9 页，long paper 正文限 ≤8 页\n- 拆出 Limitations 后需重新编译确认\n- [R2 提出, R1 AGREE]\n\n**C3. 训练/评估数据同源，缺 OOD 验证**\n- WikiText-103（训练）→ WikiText-2（评估）共享 Wikipedia domain\n- 1000 steps (~8M tokens) 极少训练量下存在 domain overfitting 风险\n- PPL improvement 幅度（49% relative）可能因 domain overlap 被高估\n- 下游 benchmark（ARC-c, WinoGrande, MMLU, GSM8K）提供部分 OOD 验证，但 PPL 是 primary metric\n- [R1 提出 critical, R2 AGREE with nuance]\n\n**C4. \"Structural failure\" 声明证据不足**\n- 仅测试一个 vanilla BCE configuration，未做 LR search / architecture size sweep\n- KL 有 Gumbel + Lagrangian + temperature annealing 三个 trick，BCE 无对等优化\n- \"Loss saturation\" 可能是 optimization issue 而非 structural limitation\n- 需要至少 soft-target BCE 或 BCE + ranking loss 对比才能支撑 \"structural\" 断言\n- [R1 提出 critical, R2 在 W3/W4 独立提出相同观点, 交叉 AGREE]\n\n### Warning（Should-Fix，影响评分）\n\n**W1. 消融实验缺关键维度**\n- 缺 d_b sensitivity（仅用 128，无 64/256/512 对比）\n- 缺温度退火 schedule 对比（cosine vs linear vs fixed）\n- 缺 training steps learning curve\n- 缺 Lagrangian LR η_λ 报告\n- [R1 列为 critical, R2 PARTIALLY AGREE — 现有消融覆盖 relaxation/allocation 但缺几个维度, 协商降为 warning]\n\n**W2. 无 wall-clock 加速，framing 误导**\n- Appendix A: pipeline 增加 6.4% latency（126.78 vs 119.11 ms）\n- Abstract/Intro 暗示 \"acceleration\" 但实际无法实现\n- 应 frame 为 prediction quality 研究\n- [R1-W1 = R2-W7, 两人独立一致]\n\n**W3. Cross-architecture 验证不足**\n- 仅 Mistral-7B-v0.3 一个额外模型，仅 50% 一个 sparsity point\n- LLaMA-8B 和 Mistral-7B 极为相似（同规模、同 FFN 类型）\n- \"Transferability\" claim 过强\n- [R1-W2 = R2-W5, 两人独立一致]\n\n**W4. 遗漏重要相关工作 MaskLLM**\n- MaskLLM (Fang et al., NeurIPS 2024 Spotlight) 使用 Gumbel-Softmax 学 N:M sparsity mask for LLMs\n- 技术组件高度相关（Gumbel relaxation + learnable mask + frozen weights）\n- 必须在 Related Work 讨论并区分\n- [R2 提出, R1 强烈 AGREE]\n\n**W5. 梯度分析 overselling**\n- §3.5 数学正确但非深刻理论贡献\n- \"Proxy loss vs end-to-end loss 的差异\" 是 ML 基本认知\n- 论文称 \"formal gradient analysis\" 但实为 informal argument\n- 缺 gradient SNR / variance 的实证对比\n- [R1-W4 ≈ R2-W3, 两人独立一致]\n\n**W6. Lagrangian 缺收敛分析**\n- 未报告 η_λ 具体值、λ 训练曲线、实际 sparsity ratio 是否达标\n- 在 non-convex + Gumbel noise setting 下无理论收敛保证\n- Reproducibility concern\n- [R1-W5, R2 交叉 AGREE]\n\n**W7. 三个 regime 仅单模型验证**\n- Budget-surplus / budget-constrained / capacity-limited 边界仅 LLaMA-3.1-8B 确定\n- 未验证 regime 边界是否随 model scale 变化\n- [R2-W5, R1 交叉 AGREE]\n\n### Info（Minor Issues）\n\n- 2D taxonomy 作为 contribution 列出但实为 post-hoc classification [R2-W6, R1 部分 REBUT — 有 organizational value]\n- 3-seed (n=3) 统计效力弱 [R1-W3, R2 REBUT — ML 惯例可接受]\n- \"2.71×\" 应为 2.70× (2700/1000=2.7)\n- \"~2.7% latency saving\" 数值不精确（实际 ~2.3%）\n- Table 1 multi-seed (uniform, 11.92) vs main result (global, 11.79) 容易混淆\n- Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合未注明\n- SPON bib year=2026 ICML vs OpenAlex=2025，需核实\n- FastForward 67.2M/2.7% 数字来源未标注\n- 两个 evaluation protocol 差异未充分解释\n- 缺 Ethics Statement（ARR 推荐但不强制）\n- 缺 MoE routing 概念关联讨论\n- 缺 LLM-specific KD 更新文献 (MiniLLM, GKD)\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上独立达成一致：\n1. BCE baseline 不公平 → \"structural failure\" claim 过强 (C4)\n2. 无 wall-clock 加速与 framing 矛盾 (W2)\n3. WikiText data overlap 风险 (C3)\n4. Cross-architecture 验证不足 (W3)\n5. MaskLLM 引用遗漏 (W4)\n6. Lagrangian 缺细节 (W6)\n7. 格式不合规 (C1, C2)\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**Novelty vs SPON (R2-N3 vs R1-REBUT)**\n\n- R2 认为：本文与 SPON 的差异仅为 per-token vs static，属于 \"自然延伸\"，novelty 不足以支撑 main conference\n- R1 反驳：(1) Static bias vs dynamic contextual mask 是 fundamental 差异（加法偏置 vs 乘法 gating）；(2) SPON orthogonality data（cosine 0.196, L2 ratio 15.8%）证明 SPON 未捕获 predictor 的信号；(3) 技术框架完全不同（SPON 无需 Gumbel/Lagrangian/end-to-end differentiable mask）\n- **Director 判断**：R1 的论据更强——SPON 和本文解决的是不同子问题（static correction vs contextual prediction），技术栈无交集。但 R2 的 concern 仍部分成立：论文 framing 可以更清晰地 articulate 与 SPON 的差异。记录为 warning 而非 critical。\n\n---\n\n## Questions to Authors\n\n1. BCE 实验中使用的 learning rate 和 schedule？是否做过 LR search？\n2. d_b=128 是如何选择的？preliminary 实验数据？\n3. 能否提供 C4 或 Pile test set 上的 PPL？\n4. Lagrangian multiplier λ 的训练轨迹？实际 sparsity ratio 是否达标？\n5. 给 BCE 同样的 Gumbel-Sigmoid + Lagrangian 框架（仅换 loss），性能如何？——这能更 cleanly 隔离 loss function 的贡献\n6. MaskLLM 与本文的关系和区别？\n\n---\n\n## Missing References\n\n1. **MaskLLM** (Fang et al., NeurIPS 2024 Spotlight) — Learnable Semi-Structured Sparsity, Gumbel-Softmax for N:M mask learning [必须引用]\n2. **MoE routing** (Switch Transformer, GShard) — 概念关联讨论 [建议引用]\n3. **LLM-specific KD** (MiniLLM, GKD) — 方法论 overlap [建议引用]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 / 5 — Borderline (Findings track recommended)**\n**Confidence: 4/5**\n\n两位 Reviewer 独立给出相同评分（R1: 3/5, R2: 3.0/5），均推荐 Findings track。\n\n**核心判断**：论文有清晰的 research question 和显著的 empirical result（KL >> BCE >> magnitude-only），但存在以下系统性不足：\n1. **格式风险**：Limitations 不合规 + 页数超限 = desk-reject 可能\n2. **实验严谨性**：OOD 验证缺失、BCE baseline 不公平、关键消融缺失\n3. **Claim 校准**：\"structural failure\" 和 \"acceleration\" 的 claim 超出了证据支撑范围\n4. **规模局限**：仅 7-8B 模型，cross-architecture/cross-scale 验证不足\n\n如果作者能解决 C1-C2（格式）、C3（OOD eval）、C4（BCE fairness），并弱化 overclaiming，论文质量可提升至 weak accept 水平。当前状态更适合 Findings track。\n\n---\n\n## Detailed Comments (按 section)\n\n### Abstract & Introduction\n- \"can accelerate SwiGLU-based LLMs\" 与实际 6.4% overhead 矛盾，需 reframe\n- \"formal gradient analysis\" 应降为 \"gradient-based motivation\"\n- 三条 contribution 中 taxonomy 可降为 organizational framework\n\n### Method (§3)\n- 梯度分析数学正确但非 novel theoretical contribution\n- Lagrangian §3.4 缺 η_λ 值和收敛讨论\n- Gumbel-Sigmoid 的选择 well-motivated (vs STE ablation)\n\n### Experiments (§4)\n- Core result (Table 2) 强且 consistent\n- Iso-compute analysis (§4.2) 需更 controlled 对比（BCE + same framework tricks）\n- SPON analysis (§4.4) 有 insight\n- Cross-architecture (§4.6) 仅 1 model, 1 sparsity point — 不足以支撑 claim\n- Latency (Appendix A) 诚实但与 framing 矛盾\n\n### Related Work (§2)\n- MaskLLM 遗漏是 major gap\n- MoE connection 值得一提\n- 现有引用准确（经 OpenAlex 验证，21 条均为真实论文）\n\n### Format\n- Limitations: 必须拆为独立 section*\n- 页数: 需编译确认（可能 border-line）\n- 匿名性: 通过 ✓\n- 模板: ACL review style ✓\n",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-16T19:05:52.754698+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Assistant

_source line 92 · 2026-05-16T19:06:01.398841+00:00_

---

**圆桌审稿完成。**

审稿报告已投递给 Research Director。总结：

| 维度 | 结果 |
|------|------|
| **Overall** | 3.0/5 Borderline — Findings track recommended |
| **Reviewer 共识** | R1=3/5, R2=3.0/5，独立一致 |
| **Critical Issues** | 4 个（格式不合规×2 + OOD 验证缺失 + "structural failure" 证据不足） |
| **Warning Issues** | 7 个（消融不足、无加速、cross-arch 弱、MaskLLM 遗漏、梯度 oversell、Lagrangian 缺细节、regime 普适性） |
| **关键分歧** | Novelty vs SPON — R1 认为 fundamental 差异，R2 认为 incremental；Director 判定 R1 论据更强，记为 warning |
| **升级路径** | 修复格式 + 补 OOD eval + 公平 BCE 对比 + 弱化 overclaim → 可能 weak accept |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 93 · 2026-05-16T19:06:03.851630+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。我逐条回应了 R2 的所有问题：
- Must-Fix: N1 [AGREE], N2 [AGREE], N3 [REBUT]（与 SPON 的差异是 fundamental 的）
- Should-Fix: W1-W5, W7 [AGREE]; W6 [部分 REBUT]（taxonomy 有 organizational value）
- 遗漏引用和小问题基本同意

与 R2 的主要分歧在 novelty 判断——我认为 per-token contextual mask + Gumbel-Sigmoid + Lagrangian 框架与 SPON 的 static bias vector 有根本性区别，orthogonality 数据支持本文的 claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-16T19:06:14.746755+00:00_

审稿流程已全部完成。R1 的交叉回应在报告提交前已纳入考量。

**审稿结果汇总**：
- **评分**: 3.0/5 — Borderline (Findings track recommended)
- **4 个 Critical 问题**: Limitations 格式不合规、页数超限、OOD 验证缺失、"structural failure" 证据不足
- **7 个 Warning 问题**: 消融缺维度、无加速、cross-arch 不足、MaskLLM 遗漏、梯度分析 overselling、Lagrangian 缺细节、regime 普适性未验证
- **1 个分歧**: Novelty vs SPON（R1 认为 fundamental, R2 认为 incremental）→ 记为 warning

报告已投递至 Research Director，Issue Tracker 已同步更新（13 条 issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 10

## Round 10

54 recorded events


### User

_source line 95 · 2026-05-17T02:27:00.418136+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (Efficient Methods for NLP)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-17T02:27:07.050360+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-17T02:27:07.102255+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-17T02:27:09.918824+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 99 · 2026-05-17T02:27:09.969490+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-17T02:27:13.996616+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-17T02:27:14.047630+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-17T02:27:16.665593+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-17T02:27:16.716377+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-17T02:27:19.288284+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-17T02:27:19.389540+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-17T02:27:22.463101+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-17T02:27:22.513793+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-17T02:27:22.965963+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "request_external_review",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "request_external_review",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-17T02:27:22.966421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-17T02:27:23.120088+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update_review_issues",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update_review_issues",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-17T02:27:23.170752+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-17T02:27:27.541650+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-17T02:27:27.993990+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (93 个)\n\n- **ste_kl_s42**: DONE (killed) — \n- **bce_comp_staged_s42**: DONE (negative) — \n- **spon_training_seq2048**: DONE (killed) — \n- **kl_only_s0**: DONE (success) — \n- **kl_only_s1**: DONE (success) — \n- **mvp_bce_s456**: DONE (success) — \n- **mvp_bce_s123**: DONE (success) — \n- **mvp_bce_s42**: DONE (success) — \n- **mvp_kl_norm_v2_s123**: DONE (success) — \n- **mvp_kl_norm_v2_s42**: DONE (success) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n- **kl_lagrangian_quicktest**: DONE (negative) — \n- **mvp_kl_s42**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- steps_curve_s42_v3（准备中）\n- steps_curve_s42_v2（准备中）\n- steps_curve_s42（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- mvp_kl_norm_s456（准备中）\n- spon_kl_s42（准备中）\n- diag_30pct_downstream（准备中）\n- diag_gsm8k_gencomp（准备中）\n- …另有 1 项\n\n## 近期结论\n- **bench_teal70** (success): TEAL vanilla baseline at 70% sparsity on LLaMA-3.1-8B provides reference point showing magnitude-based pruning degradation at high sparsity\n- **bench_kl70_global** (success): LLaMA-3.1-8B KL predictor at 70% sparsity (teal_global eval) completes the symmetric cross-architecture comparison showing consistent KL advantage pattern\n- **mistral_teal50_baseline** (success): TEAL vanilla baseline on Mistral-7B at 50% sparsity provides cross-architecture reference point for KL advantage quantification\n\n## 趋势\n成功 46 / 负向 13 / 失败 15 / 共 82\ndense_ppl: 6.12 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- mvp_kl_s123: 已被终止 — unknown\n- mvp_kl_s456: 已被终止 — unknown\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123: 训练失败 — unknown\n- spon_training_seq2048: 已被终止 — unknown\n- ste_kl_s42: 已被终止 — 
…[truncated 649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-17T02:27:28.044729+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-17T02:27:29.852493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-17T02:27:29.903384+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-17T02:27:35.363858+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

I've found the EMNLP 2026 call for papers information. Here's a summary of the key submission guidelines and author instructions:

## Submission Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Submission Process

Authors submit articles to ARR (ACL Rolling Review), where submi
…[truncated 1553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7319
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-17T02:27:42.094064+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 paper format page limit long paper short paper requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 paper format page limit long paper short paper requirements"
  }
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-17T02:27:42.596745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 120 · 2026-05-17T02:27:42.860102+00:00_

1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures of similar scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---that govern the quality-sparsity tradeoff.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 263
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-17T02:27:42.860532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-17T02:27:42.911205+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can simplify inference by pruning 50\% of FFN neurons per token---without modifying the pretrained weights---eliminating the need for auxiliary compensation networks.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}---a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This creates a structural
…[truncated 4994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-17T02:27:48.237543+00:00_

Web search results for query: "ACL Rolling Review 2026 paper format page limit long paper short paper requirements"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Student Research Workshop - ACL 2026","url":"https://2026.aclweb.org/calls/student_research_workshop/"}]

Based on the search results, here is information about ACL Rolling Review 2026 paper format and page limit requirements:

## Paper Types

The conference accepts submissions of long papers and short papers.

## Long Papers

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page -- up to nine (9) pages of content plus unlimited pages for a
…[truncated 959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6143
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-17T02:27:52.456264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-17T02:27:52.908630+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction---adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.
14	In contrast, our method learns \emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.
15	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
16	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation
…[truncated 1589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-17T02:27:52.909257+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-17T02:27:53.311278+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 13338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-17T02:27:53.361900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-17T02:27:53.362433+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \times 10^{-3}$ and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presen
…[truncated 12486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-17T02:27:58.137591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-17T02:27:58.590383+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Training sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.
5	The resulting predictor (75.9M params, $<$1\% of base) achieves PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, transfers across SwiGLU architectures of similar scale (within 7\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-17T02:27:58.590882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-17T02:27:59.043469+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
7	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-17T02:27:59.043910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-17T02:27:59.094553+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 7564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-17T02:28:05.275001+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-17T02:28:05.626870+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-17T02:28:05.627705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-17T02:28:05.680134+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2026},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 8151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-17T02:28:09.460414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-17T02:28:09.912741+00:00_

1	issues:
2	  - id: "R2-N1"
3	    summary: "Limitations section 格式不合规——当前为 conclusion 内 paragraph，ARR 要求独立 section*"
4	    category: format
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - {round: 1, reviewers: [1, 2], note: "R2 提出，R1 交叉回应 AGREE。desk-reject 条件。"}
11	    action_items:
12	      - {round: 1, action: "将 \\paragraph{Limitations.} 拆为独立 \\section*{Limitations}", assigned_to: "paper_agent", status: done}
13	    resolution: "Paper Agent commit 7018701: Limitations 拆为独立 section*，8p 正文确认合规"
14	    resolution_round: 1
15	
16	  - id: "R2-N2"
17	    summary: "页数超限——正文含 Limitations/Future work 延伸至第 9 页，long paper 限 8 页"
18	    category: format
19	    severity: critical
20	    status: resolved
21	    first_raised_round: 1
22	    last_seen_round: 1
23	    mentions:
24	      - {round: 1, reviewers: [1, 2], note: "R2 提出，R1 AGREE。"}
25	    action_items:
26	      - {round: 1, action: "拆出 Limitations 后编译确认页数", assigned_to: "paper_agent", status: done}
27	    resolution: "编译确认: main content 结束于 page 8, Limitations ARR exempt, 总 10p PDF"
28	    resolution_round: 1
29	
30	  - id: "R1-N1"
31	    summary: "训练/评估数据同源（WikiText-103→WikiText-2），缺 OOD PPL 评估"
32	    category: experiment
33	    severity: critical
34	    status: resolved
35	    first_raised_round: 1
36	    last_seen_round: 1
37	    mentions:
38	      - {round: 1, reviewers: [1, 2], note: "R1 提出 critical。R2 AGREE with nuance。"}
39	    action_items:
40	      - {round: 1, action: "用已训练好的 predictor 在 C4 validation set 上评估 PPL（含 dense + TEAL baseline）", assigned_to: "main_agent", status: done}
41	    resolution: "C4 validation (200 samples, streaming): Dense=9.21, KL 50%=18.40, TEAL 50%=38.75. KL 在 OOD 上保持 2.1× 优于 TEAL，相对优势泛化。"
42	    resolution_round: 1
43	
44	  - id: "R1-N2"
45	    summary: "'Structural failure' 声明缺充分证据——BCE 仅测一个 configuration，对比不公平"
46	    category: method
47	    severity: critical
48	    status: resolved
49	    first_raise
…[truncated 6497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-17T02:28:10.115186+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-17T02:28:10.216505+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_1.md:170:外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未启用）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:6:{"ts": "2026-05-16T18:52:55.359976+00:00", "role": "tool", "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status", "max_results": "4"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:48:{"ts": "2026-05-16T18:54:03.322072+00:00", "role": "tool", "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review", "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu", "output_mode": "content"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:49:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl:50:{"ts": "2026-05-16T18:54:09.352496+00:00", "role": "tool", "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:dire
…[truncated 3860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-17T02:29:22.930958+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务分配 — Reviewer 1（方法严谨性 + 实验方法论）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 8 页正文 + unlimited references\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须独立 `\\section*{Limitations}`（不计入页数）\n- **Appendix**: 不计入页数，审稿人不强制阅读但可参考\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n\n**核心任务**：评估方法的技术严谨性和实验的可靠性。\n\n重点审查维度：\n1. **KL distillation 框架**：Gumbel-Sigmoid relaxation 的数学正确性、与 inference 的 gap（soft mask training vs hard mask inference）、forward KL 选择的合理性\n2. **梯度分析（§3.5）**：BCE vs KL 的 structural mismatch argument 是否 rigorous、是否存在 logical gap\n3. **Lagrangian sparsity constraint**：multiplicative dual variable controller 的收敛性、deadzone 设计、是否有更好的替代方案\n4. **实验设计**：\n   - Iso-compute 对比是否公平（KL 1000 steps vs BCE 2700 steps，但 KL 需要 full forward pass 梯度）\n   - 消融实验的完整性（d_b sensitivity、τ schedule、training convergence）\n   - 统计可靠性（3 seeds, CV<1%）\n   - OOD 评估（WikiText-103 训练 → WikiText-2 评估 → C4 验证）\n5. **Inference 实际收益**：6.4% overhead claim、compensation 消除的实际影响\n6. **可复现性**：训练细节是否充分（lr, batch size, hardware, time）\n\n### 已知 open issues（来自 Issue Tracker）\n- R1-N3 (in_progress): 消融实验维度——d_b sensitivity、温度 schedule、training curve 是否已补充到 Appendix\n- R1-W5 (in_progress): Lagrangian 收敛分析——λ 轨迹和 sparsity ratio 曲线是否已加入\n- R1-W3 (open): 三 seed (n=3) 统计效力\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条，标号 S1, S2, ...）\n3. Weaknesses（逐条，标号 W1, W2, ...，标注 severity: critical/warning/info）\n4. Questions（需要作者澄清的技术问题）\n5. Missing References（如有）\n6. Overall Assessment（score + confidence + 1-2 句总评）\n\n评分标准：strong reject / weak reject / borderline / weak accept / strong accept\n置信度：1-5（5=expert）",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务分配 — Reviewer 1（方法严谨性 + 实验方法论）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 8 页正文 + unlimited references\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须独立 `\\section*{Limitations}`（不计入页数）\n- **Appendix**: 不计入页数，审稿人不强制阅读但可参考\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n\n**核心任务**：评估方法的技术严谨性和实验的可靠性。\n\n重点审查维度：\n1. **KL distillation 框架**：Gumbel-Sigmoid relaxation 的数学正确性、与 inference 的 gap（soft mask training vs hard mask inference）、forward KL 选择的合理性\n2. **梯度分析（§3.5）**：BCE vs KL 的 structural mismatch argument 是否 rigorous、是否存在 logical gap\n3. **Lagrangian sparsity constraint**：multiplicative dual variable controller 的收敛性、deadzone 设计、是否有更好的替代方案\n4. **实验设计**：\n   - Iso-compute 对比是否公平（KL 1000 steps vs BCE 2700 steps，但 KL 需要 full forward pass 梯度）\n   - 消融实验的完整性（d_b sensitivity、τ schedule、training convergence）\n   - 统计可靠性（3 seeds, CV<1%）\n   - OOD 评估（WikiText-103 训练 → WikiText-2 评估 → C4 验证）\n5. **Inference 实际收益**：6.4% overhead claim、compensation 消除的实际影响\n6. **可复现性**：训练细节是否充分（lr, batch size, hardware, time）\n\n### 已知 open issues（来自 Issue Tracker）\n- R1-N3 (in_progress): 消融实验维度——d_b sensitivity、温度 schedule、training curve 是否已补充到 Appendix\n- R1-W5 (in_progress): Lagrangian 收敛分析——λ 轨迹和 sparsity ratio 曲线是否已加入\n- R1-W3 (open): 三 seed (n=3) 统计效力\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条，标号 S1, S2, ...）\n3. Weaknesses（逐条，标号 W1, W2, ...，标注 severity: critical/warning/info）\n4. Questions（需要作者澄清的技术问题）\n5. Missing References（如有）\n6. Overall Assessment（score + confidence + 1-2 句总评）\n\n评分标准：strong reject / weak reject / borderline / weak accept / strong accept\n置信度：1-5（5=expert）",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-17T02:29:40.293679+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17362
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-17T02:29:40.796960+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务分配 — Reviewer 2（新颖性 + 完整性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 8 页正文 + unlimited references\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须独立 `\\section*{Limitations}`（不计入页数）\n- **Appendix**: 不计入页数，审稿人不强制阅读但可参考\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n\n**核心任务**：评估论文的新颖性、学术贡献度、writing quality 和完整性。\n\n重点审查维度：\n1. **新颖性评估**：\n   - KL distillation + Gumbel-Sigmoid 用于 activation sparsity prediction 是否有足够 novelty\n   - 与 SPON（同样用 KL）的区分是否 convincing（static vs contextual）\n   - 与 MaskLLM（同样用 Gumbel relaxation + learnable masks）的区分是否充分\n   - 2D taxonomy 的学术贡献度（是 insight 还是 trivial classification）\n2. **Related Work 完整性**：\n   - 引用是否覆盖所有直接相关方法\n   - 是否遗漏 2024-2026 年重要 activation sparsity 工作\n   - Positioning 是否准确（claim 的 gap 是否真实存在）\n3. **Cross-architecture claims**：\n   - 仅 2 个模型（LLaMA-8B + Mistral-7B）是否足以支撑 \"transfers across SwiGLU architectures\" 的 claim\n   - \"within 7%\" consistency claim 的 evidence 强度\n4. **Writing quality**（按 EMNLP 标准）：\n   - 叙事结构是否清晰连贯\n   - Abstract 是否在 30 秒内传达核心贡献\n   - 是否有 AI writing 痕迹（em-dash、-ing phrases、过度分段）\n   - 术语定义是否充分\n5. **Contribution vs claim calibration**：\n   - 声明的贡献是否与实际 evidence 匹配\n   - 是否有 overclaim（特别是 \"eliminates compensation\" 和 \"structural mismatch\" 的强度）\n6. **格式合规性**：页数、匿名、引用格式、Limitations section\n\n### 已知 open issues（来自 Issue Tracker）\n- R2-N3 (resolved): 与 SPON 区分度——之前已修复，请确认当前版本是否充分\n- R2-W1 (resolved): MaskLLM 遗漏——已添加，请确认讨论是否充分\n- R2-W6 (resolved): 2D taxonomy 贡献度——已降级为 organizational framework，请确认 framing 是否合理\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条，标号 S1, S2, ...）\n3. Weaknesses（逐条，标号 W1, W2, ...，标注 severity: critical/warning/info）\n4. Questions（需要作者澄清的技术问题）\n5. Missing References（如有）\n6. Overall Assessment（score + confidence + 1-2 句总评）\n\n评分标准：strong reject / weak reject / borderline / weak accept / strong accept\n置信度：1-5（5=expert）",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务分配 — Reviewer 2（新颖性 + 完整性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review May cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 8 页正文 + unlimited references\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须独立 `\\section*{Limitations}`（不计入页数）\n- **Appendix**: 不计入页数，审稿人不强制阅读但可参考\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n\n**核心任务**：评估论文的新颖性、学术贡献度、writing quality 和完整性。\n\n重点审查维度：\n1. **新颖性评估**：\n   - KL distillation + Gumbel-Sigmoid 用于 activation sparsity prediction 是否有足够 novelty\n   - 与 SPON（同样用 KL）的区分是否 convincing（static vs contextual）\n   - 与 MaskLLM（同样用 Gumbel relaxation + learnable masks）的区分是否充分\n   - 2D taxonomy 的学术贡献度（是 insight 还是 trivial classification）\n2. **Related Work 完整性**：\n   - 引用是否覆盖所有直接相关方法\n   - 是否遗漏 2024-2026 年重要 activation sparsity 工作\n   - Positioning 是否准确（claim 的 gap 是否真实存在）\n3. **Cross-architecture claims**：\n   - 仅 2 个模型（LLaMA-8B + Mistral-7B）是否足以支撑 \"transfers across SwiGLU architectures\" 的 claim\n   - \"within 7%\" consistency claim 的 evidence 强度\n4. **Writing quality**（按 EMNLP 标准）：\n   - 叙事结构是否清晰连贯\n   - Abstract 是否在 30 秒内传达核心贡献\n   - 是否有 AI writing 痕迹（em-dash、-ing phrases、过度分段）\n   - 术语定义是否充分\n5. **Contribution vs claim calibration**：\n   - 声明的贡献是否与实际 evidence 匹配\n   - 是否有 overclaim（特别是 \"eliminates compensation\" 和 \"structural mismatch\" 的强度）\n6. **格式合规性**：页数、匿名、引用格式、Limitations section\n\n### 已知 open issues（来自 Issue Tracker）\n- R2-N3 (resolved): 与 SPON 区分度——之前已修复，请确认当前版本是否充分\n- R2-W1 (resolved): MaskLLM 遗漏——已添加，请确认讨论是否充分\n- R2-W6 (resolved): 2D taxonomy 贡献度——已降级为 organizational framework，请确认 framing 是否合理\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条，标号 S1, S2, ...）\n3. Weaknesses（逐条，标号 W1, W2, ...，标注 severity: critical/warning/info）\n4. Questions（需要作者澄清的技术问题）\n5. Missing References（如有）\n6. Overall Assessment（score + confidence + 1-2 句总评）\n\n评分标准：strong reject / weak reject / borderline / weak accept / strong accept\n置信度：1-5（5=expert）",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-17T02:29:42.212226+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1415
}
```

</details>

---


### Assistant

_source line 148 · 2026-05-17T02:29:51.428472+00:00_

审稿任务已分配：

- **Reviewer 1**（方法严谨性）：已派发，侧重 KL distillation 框架、梯度分析、Lagrangian 机制、实验设计公平性、统计可靠性
- **Reviewer 2**（新颖性/完整性）：已派发，侧重 novelty 评估、SPON/MaskLLM 区分度、cross-architecture claims、writing quality、格式合规

两位 Reviewer 独立审稿中，等待 Round 1 初审结果返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 11

## Round 11

30 recorded events


### User

_source line 149 · 2026-05-17T04:45:46.239565+00:00_

[Reviewer 2 审稿结果]:
我已完成论文全文阅读和相关文献调研。现在将审稿意见汇报给 Director。

---

[Reviewer 1 审稿结果]:
I have now read the full paper including abstract, introduction, related work, method, experiments, conclusion, limitations, and appendix. I also have the ACL ARR review form scoring dimensions. Let me compile my review.

---

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: long paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-17T04:45:52.852821+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-17T04:45:52.903959+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-17T04:45:56.676224+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,get_external_review_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,get_external_review_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-17T04:45:56.676585+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-17T04:46:00.792193+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-17T04:46:00.792643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-17T04:46:06.864611+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-17T04:46:08.274839+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (97 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- steps_curve_s42_v3（准备中）\n- steps_curve_s42_v2（准备中）\n- steps_curve_s42（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- mvp_kl_norm_s456（准备中）\n- spon_kl_s42（准备中）\n- diag_30pct_downstream（准备中）\n- diag_gsm8k_gencomp（准备中）\n- …另有 1 项\n\n## 近期结论\n- **gradient_snr_constrained_v2** (success): Under fair Lagrangian-constrained training (both KL and BCE targeting 50% sparsity), KL still provides dramatically higher gradient SNR than BCE, confirming the advantage is from end-to-end coupling not from unconstrained regime ← 基于 gradient_snr_kl_vs_bce\n- **teal_kl_overlap_analysis** (success): KL predictor and TEAL prune different neuron sets; KL sacrifices high-magnitude knowledge neurons (concentrated in middle layers) to optimize output distribution matching, explaining why TEAL retains MMLU advantage despite worse PPL\n  [teal_kl_overlap_analysis](/api/workspace-files/projects/distill_sparse_swiglu/artifacts/teal_kl_overlap_analysis/data/teal_kl_overlap_analysis.txt)\n- **natural_sparsity_floor_30pct** (success): KL predictor at 30% sparsity has a significant static sparsity floor (always-pruned neurons), explaining why actual sparsity (2
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-17T04:46:08.325786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-17T04:46:08.782077+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-17T04:46:08.832731+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 161 · 2026-05-17T04:46:08.885073+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-17T04:46:13.875588+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-17T04:46:15.538531+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-17T04:46:15.841103+00:00_

issues:
  - id: "R2-N1"
    summary: "Limitations section 格式不合规——当前为 conclusion 内 paragraph，ARR 要求独立 section*"
    category: format
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - {round: 1, reviewers: [1, 2], note: "R2 提出，R1 交叉回应 AGREE。desk-reject 条件。"}
    action_items:
      - {round: 1, action: "将 \\paragraph{Limitations.} 拆为独立 \\section*{Limitations}", assigned_to: "paper_agent", status: done}
    resolution: "Paper Agent commit 7018701: Limitations 拆为独立 section*，8p 正文确认合规"
    resolution_round: 1

  - id: "R2-N2"
    summary: "页数超限——正文含 Limitations/Future work 延伸至第 9 页，long paper 限 8 页"
    category: format
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - {round: 1, reviewers: [1, 2], note: "R2 提出，R1 AGREE。"}
    action_items:
      - {round: 1, action: "拆出 Limitations 后编译确认页数", assigned_to: "paper_agent", status: done}
    resolution: "编译确认: main content 结束于 page 8, Limitations ARR exempt, 总 10p PDF"
    resolution_round: 1

  - id: "R1-N1"
    summary: "训练/评估数据同源（WikiText-103→WikiText-2），缺 OOD PPL 评估"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - {round: 1, reviewers: [1, 2], note: "R1 提出 critical。R2 AGREE with nuance。"}
    action_items:
      - {round: 1, action: "用已训练好的 predictor 在 C4 validation set 上评估 PPL（含 dense + TEAL baseline）", assigned_to: "main_agent", status: done}
    resolution: "C4 validation (200 samples, streaming): Dense=9.21, KL 50%=18.40, TEAL 50%=38.75. KL 在 OOD 上保持 2.1× 优于 TEAL，相对优势泛化。"
    resolution_round: 1

  - id: "R1-N2"
    summary: "'Structural failure' 声明缺充分证据——BCE 仅测一个 configuration，对比不公平"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - {round: 1, reviewers: [1, 2], note: "R1 提出 critical，R2 独立指出相同问题。"}
    action_item
…[truncated 6129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-17T04:46:15.941939+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/distill_sparse_swiglu/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/distill_sparse_swiglu/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-17T04:46:15.992615+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-17T04:46:21.525740+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the web search results, here are the key submission guidelines and author instructions for EMNLP 2026:

## Paper Types & Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a 
…[truncated 1434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7650
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-17T04:46:24.706460+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long paper template guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long paper template guidelines"
  }
}
```

</details>

---


### Tool call

_source line 169 · 2026-05-17T04:46:26.865542+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-17T04:46:26.865971+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-17T04:46:31.037977+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long paper template guidelines"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here is the information about ACL Rolling Review 2026 submission format, page limits, and template guidelines:

## Page Limits

Long papers may have up to eight (8) pages of content plus unlimited pages for references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

The "Limitations" section does not count towards the page limit and 
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6331
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-17T04:47:29.149750+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references; Limitations 不计页数\n- **模板**: ACL template with `[review]` option\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n1. **方法严谨性**：KL distillation framework 的理论支撑、Gumbel-Sigmoid 采样、Lagrangian 对偶约束的正确性\n2. **实验设计**：baseline 对比公平性、统计显著性、消融实验完整性\n3. **重点验证 Round 1 遗留 in_progress issues**：\n   - **R1-W4** (in_progress): §3.5 梯度分析从 \"theoretical contribution\" 弱化为 \"gradient-based motivation\"，且需添加实证 gradient SNR 数据 (KL/BCE=5.76×)。检查是否已完成、数据是否可信、framing 是否合理。\n   - **R1-W5** (in_progress): Lagrangian 对偶更新缺收敛分析。Appendix C 已有 convergence table (4 targets × final λ + actual sparsity)，还需 λ/sparsity 时序曲线。检查 Appendix C 是否充分。\n   - **R1-W3** (open/info): 三 seed (n=3) 统计效力——检查是否有改善或 adequate justification。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 sentences)\n2. Strengths (bullet points)\n3. Weaknesses (bullet points, 标注 severity: critical/warning/info)\n4. Round 1 Issue Status (逐条确认 R1-W4, R1-W5, R1-W3 是否已修复)\n5. Questions for authors\n6. Missing references\n7. Overall score (strong reject / weak reject / borderline / weak accept / strong accept) + confidence (1-5)",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references; Limitations 不计页数\n- **模板**: ACL template with `[review]` option\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n1. **方法严谨性**：KL distillation framework 的理论支撑、Gumbel-Sigmoid 采样、Lagrangian 对偶约束的正确性\n2. **实验设计**：baseline 对比公平性、统计显著性、消融实验完整性\n3. **重点验证 Round 1 遗留 in_progress issues**：\n   - **R1-W4** (in_progress): §3.5 梯度分析从 \"theoretical contribution\" 弱化为 \"gradient-based motivation\"，且需添加实证 gradient SNR 数据 (KL/BCE=5.76×)。检查是否已完成、数据是否可信、framing 是否合理。\n   - **R1-W5** (in_progress): Lagrangian 对偶更新缺收敛分析。Appendix C 已有 convergence table (4 targets × final λ + actual sparsity)，还需 λ/sparsity 时序曲线。检查 Appendix C 是否充分。\n   - **R1-W3** (open/info): 三 seed (n=3) 统计效力——检查是否有改善或 adequate justification。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 sentences)\n2. Strengths (bullet points)\n3. Weaknesses (bullet points, 标注 severity: critical/warning/info)\n4. Round 1 Issue Status (逐条确认 R1-W4, R1-W5, R1-W3 是否已修复)\n5. Questions for authors\n6. Missing references\n7. Overall score (strong reject / weak reject / borderline / weak accept / strong accept) + confidence (1-5)",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-17T04:47:39.409939+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10260
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-17T04:47:40.363506+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## Round 2 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references; Limitations 不计页数\n- **模板**: ACL template with `[review]` option\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n1. **新颖性评估**：与 SPON、MaskLLM、TEAL、DejaVu 等已有方法的区分度；核心贡献是否超越\"已知方法的组合\"\n2. **完整性**：Related Work 覆盖度、引用充足度、实验覆盖是否全面\n3. **写作质量**：\n   - 叙事连贯性（Abstract → Intro → Method → Experiments → Conclusion 主线一致性）\n   - AI 写作痕迹（em-dash、-ing phrases、过度分段、黑名单用词）\n   - 专有名词定义、缩写规范\n   - 图表知识密度和视觉规范\n4. **Round 1 已 resolved issues 抽检**：\n   - R1-W1 (resolved): 推理延迟 framing 是否不再矛盾\n   - R1-W2 (resolved): Cross-architecture claim 是否已弱化\n   - R2-N3 (resolved): 与 SPON 的区分度是否充分\n   - R2-W1 (resolved): MaskLLM 是否已加入 Related Work\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 sentences)\n2. Strengths (bullet points)\n3. Weaknesses (bullet points, 标注 severity: critical/warning/info)\n4. Round 1 Resolved Issues Spot-Check (逐条确认上述 4 项是否修复到位)\n5. Questions for authors\n6. Missing references\n7. Overall score (strong reject / weak reject / borderline / weak accept / strong accept) + confidence (1-5)",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## Round 2 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references; Limitations 不计页数\n- **模板**: ACL template with `[review]` option\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n1. **新颖性评估**：与 SPON、MaskLLM、TEAL、DejaVu 等已有方法的区分度；核心贡献是否超越\"已知方法的组合\"\n2. **完整性**：Related Work 覆盖度、引用充足度、实验覆盖是否全面\n3. **写作质量**：\n   - 叙事连贯性（Abstract → Intro → Method → Experiments → Conclusion 主线一致性）\n   - AI 写作痕迹（em-dash、-ing phrases、过度分段、黑名单用词）\n   - 专有名词定义、缩写规范\n   - 图表知识密度和视觉规范\n4. **Round 1 已 resolved issues 抽检**：\n   - R1-W1 (resolved): 推理延迟 framing 是否不再矛盾\n   - R1-W2 (resolved): Cross-architecture claim 是否已弱化\n   - R2-N3 (resolved): 与 SPON 的区分度是否充分\n   - R2-W1 (resolved): MaskLLM 是否已加入 Related Work\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 sentences)\n2. Strengths (bullet points)\n3. Weaknesses (bullet points, 标注 severity: critical/warning/info)\n4. Round 1 Resolved Issues Spot-Check (逐条确认上述 4 项是否修复到位)\n5. Questions for authors\n6. Missing references\n7. Overall score (strong reject / weak reject / borderline / weak accept / strong accept) + confidence (1-5)",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-17T04:47:42.034566+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1671
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-17T04:47:42.035052+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "paper_pdf_path": "projects/distill_sparse_swiglu/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "Round 2 review. 论文修订后重新提交外部审稿。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "paper_pdf_path": "projects/distill_sparse_swiglu/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "Round 2 review. 论文修订后重新提交外部审稿。"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-17T04:47:42.650773+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 615
}
```

</details>

---


### Assistant

_source line 178 · 2026-05-17T04:47:53.180691+00:00_

**Round 2 审稿已启动**

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性 + 实验设计（重点验证 R1-W4/R1-W5 修复） | ✅ 已分配 |
| Reviewer 2 | 新颖性 + 完整性 + 写作质量（抽检 resolved issues） | ✅ 已分配 |
| 外部审稿 (Stanford Agentic Reviewer) | 全面审稿 | ⏳ pending |

**Round 1 遗留重点关注**：
- R1-W4 (in_progress): §3.5 梯度分析 framing + 实证 SNR 数据
- R1-W5 (in_progress): Lagrangian 收敛曲线
- R1-W3 (open/info): 三 seed 统计效力

等待两位 Reviewer 返回审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 179 · 2026-05-17T04:51:14.118587+00:00_

[Reviewer 1 审稿意见]:
## Round 2 Review — Reviewer 1（方法严谨性 + 实验设计）

### 1. Summary

本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。方法在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。论文还提出了二维分类法和三种稀疏 regime 的分析框架。

---

### 2. Strengths

- **核心贡献清晰且可验证**：KL vs BCE 的结构性差异论证（§3.6 梯度分析）逻辑自洽，且有实证 SNR 数据支撑（5.76×）。
- **消融设计良好**：Table 3 系统隔离了 loss function（ΔP=26.23）vs relaxation method（ΔP=3.98），明确了 KL 是主要贡献因素。BCE+Gumbel+Lagrangian 实验（PPL 38.02）特别有说服力，排除了 Gumbel 本身带来改进的假设。
- **Iso-compute 分析**（§4.3）：BCE 2700 步 loss 饱和（Δ=-0.006）证明了结构性失败而非计算不足。
- **Cross-architecture 验证**：两个不同架构（LLaMA/Mistral）上 advantage ratio 的一致性（≤50% 时 within 7%）增强了泛化性 claim 的可信度。
- **Regime 分析有实用价值**：budget-surplus/constrained/capacity-limited 三分法对实践者选择稀疏度有指导意义。
- **Limitations 诚实**：明确承认无实际加速、仅 7-8B 模型、per-target 训练的限制。

---

### 3. Weaknesses

**W1 [critical] "Lagrangian" 术语不准确，非标准对偶方法**
- 具体位置：§3.5, Eq. 9-10
- 问题：Eq. 9 是带 deadzone 的二次惩罚项 λ·clamp(|s̄-(1-ρ)|-ε, min=0)²，Eq. 10 的更新规则是几何倍增/减半（×2/×0.5），这既不是标准 augmented Lagrangian（需 λ ← λ + η·violation），也不是对偶上升法。将其称为 "Lagrangian" 和 "dual variable" 存在术语误导。这是一个带自适应权重的惩罚方法（penalty method with adaptive coefficient）。
- 影响：审稿人可能质疑作者对优化理论的理解深度；更重要的是，penalty method 不保证满足 KKT 条件，论文也未讨论这一局限。
- 建议：(1) 改称 "adaptive penalty controller" 或明确说明这是对 Lagrangian 的工程化简化；(2) 讨论为何不使用标准对偶上升以及当前方案的收敛保证。

**W2 [critical] Appendix C 缺少 λ/sparsity 时序曲线（R1-W5 未完全修复）**
- 具体位置：Appendix C (§C, Table 7)
- 问题：Table 7 仅报告最终状态（final λ + actual sparsity + deviation），满足"是否收敛"的验证。但缺少训练过程中 λ 和 actual sparsity 随 step 变化的时序曲线。Director 明确要求 "还需 λ/sparsity 时序曲线"。
- 为什么重要：(1) 30% 和 70% target 的 λ 均 hit cap（5000 和 1000），表明系统可能在 cap boundary 震荡而非真正收敛；(2) 文中提到 "最后 ~100 步 loss 轻微上升"（Appendix C 末段），时序曲线可以展示这是否与 λ 动态相关；(3) 无曲线无法验证 "~10 步达到稳态" 的 claim。
- 建议：补充 Figure 展示至少 30%/50%/70% 三个 target 的 (step, λ) 和 (step, actual_sparsity) 曲线。

**W3 [warning] 梯度 SNR 定义不明确且样本量小**
- 具体位置：§3.6, "Empirical verification" 段落
- 问题：(1) "gradient SNR" 未给出数学定义——是 mean(|grad|)/std(|grad|) over steps? over neurons? over layers? 读者无法 verify 或 reproduce 这个数字。(2) 仅 80 步的测量，对于 SNR 估计（尤其是分层报告 early/late layers）样本量偏小。(3) 数值 5.77×10⁻⁵ vs 1.00×10⁻⁵ 的 ratio 是 5.77×，但文中写 "5.76×"——小数点精度不一致。
- 建议：(1) 明确 SNR 的数学公式；(2) 增加到至少 200+ steps 或报告 bootstrap CI；(3) 修正 5.77/1.00=5.77 vs claim 5.76 的不一致。

**W4 [warning] n=3 seeds 统计效力不足（R1-W3 未改善）**
- 具体位置：§4.7, Appendix E
- 问题：论文仍使用 3 seeds，仅以 CV<1% 作为 justification。CV<1% 说明方法 variance 小，但不等于效力足够检测方法间差异。对于主表中 KL global (11.79) vs KL uniform (11.96) 之差（0.17），以 std=0.07 计算，即使 paired t-test 也仅有 n=3 自由度=2，无法确信 p<0.05。
- 此外，cross-arch claim "within 7%" 完全基于点估计（无 CI），无法区分真实差异与噪声。
- 建议：(1) 至少补充 5 seeds，或明确声明 "global vs uniform 差异不显著"；(2) 对 cross-arch ratio 报告 bootstrap CI。

**W5 [warning] 无实际推理加速，且 overhead 表述可能误导读者**
- 具体位置：Appendix A, Table 5
- 问题：论文动机强调 "reduces effective computation"（Abstract 第一句），但实测增加 6.4% latency overhead。虽然 Limitations 中诚实说明了这一点，但 Abstract/Introduction 的 framing 可能让读者期望实际加速。"Eliminating compensation network" 节省的 2.7% latency 被 predictor 自身的 6.4% overhead 抵消，net effect 是变慢。
- 建议：Abstract 首句明确 "prediction quality" 而非暗示 "reduces computation"；或在 Experiments 主文中简要说明当前无加速。

**W6 [info] 30% 稀疏度 MMLU 异常未充分解释**
- 具体位置：Table 2, §4.5
- 问题：KL global 在 30% 稀疏度的 MMLU 仅 25.27%（接近随机），而 KL uniform 达 40.61%。这是 15pp 差异，暗示全局分配在低稀疏度时 actively harmful for knowledge tasks。论文将此归因于 "global top-k starves knowledge-critical layers"，但缺乏进一步分析：具体哪些 layers 被 starved？layer-wise allocation 分布是什么样？
- 建议：补充 30% 稀疏度下 global top-k 的 per-layer 实际保留率分布，验证 "starve" 假设。

---

### 4. Round 1 Issue Status

| Issue | Status | 评估 |
|-------|--------|------|
| **R1-W4** (gradient motivation reframing + SNR data) | ✅ 基本完成 | §3.6 标题改为 "Gradient-Based Motivation"，framing 合理。SNR 5.76× 数据已添加且与 layer-depth 理论一致。但 SNR 定义不明确（see W3 above）。 |
| **R1-W5** (Lagrangian convergence) | ⚠️ 部分完成 | Table 7 提供了 4 targets 的最终收敛状态，满足基本验证。但缺少 λ/sparsity 时序曲线（see W2 above），且两个 target hit cap 的情况未充分讨论。 |
| **R1-W3** (n=3 statistical power) | ❌ 未改善 | 仍为 3 seeds，仅增加了 downstream metric 的 std 报告。未增加 seed 数量，也未提供 adequate justification（如 power analysis 或 paired comparison CI）。 |

---

### 5. Questions for Authors

1. Eq. 10 的几何倍增如何保证收敛？当 λ hit cap 时（30%: λ=5000, 70%: λ=1000），是否意味着约束无法被精确满足？30% 的 5% deviation 是否可接受？
2. Gradient SNR 的精确定义是什么？是 E[grad²] / Var[grad] 还是 |E[grad]| / std(grad)？over what dimensions (neurons? steps? sequences)?
3. 如果将 KL global 在 30% 稀疏度的 MMLU 25.27% 与 dense 的 65.27% 比较，这是 40pp 的退化。论文推荐的实际使用方案是什么——30% uniform？还是 50% global？
4. BCE+Gumbel+Lagrangian (PPL 38.02) 比 vanilla BCE (27.97) 更差，作者解释为 "Lagrangian 干扰 per-neuron optimization"。但这是否也说明 Gumbel-Sigmoid 本身引入了噪声？如果去掉 Lagrangian 只用 BCE+Gumbel 结果如何？
5. 论文 claim SPON cosine similarity 0.196 为 "near-orthogonal"，但 0.196 并不特别接近 0。在 14336 维空间中，随机向量的 expected cosine similarity ≈ 0。0.196 是否实际上表示 moderate positive correlation？

---

### 6. Missing References

- **Wanda (Sun et al., 2024)**: 结构化/非结构化剪枝的重要 baseline，尤其在讨论 neuron importance 时应对比。
- **SparseGPT (Frantar & Alistarh, 2023)**: one-shot pruning 的代表方法，作为 broader pruning landscape 的参照。
- **Mixture-of-Experts (Fedus et al., 2022)**: conditional computation 的另一范式，Related Work 中应 acknowledge。
- 缺少对 Gumbel-Sigmoid 变体的直接引用——Jang et al. 2017 是 Gumbel-Softmax (categorical)，Gumbel-Sigmoid (binary) 的标准引用应为 Maddison et al. 2017 (Concrete distribution) 或 Louizos et al. 2018 (L0 regularization)。

---

### 7. Overall Assessment

**Soundness**: 3.5/5
核心 KL vs BCE 的结构性论证正确且实验支撑充分。但 "Lagrangian" 术语误用、SNR 定义缺失、n=3 统计效力不足降低了 rigor。消融实验设计良好。

**Excitement**: 3.5/5
贡献有实用价值（消除 compensation network、regime 分析），但 scope 限于 7-8B 模型 + WikiText，且无实际加速演示，限制了 impact。

**Reproducibility**: 4/5
超参数详尽，实验 protocol 清晰。缺少代码发布承诺和 SNR 测量的精确定义。

**Overall**: 3.5 (Borderline Conference)
论文有一个清晰的核心贡献（KL training for sparsity prediction），消融充分，跨架构验证有说服力。但 Lagrangian 术语问题（W1）和缺少收敛曲线（W2）是方法严谨性的硬伤；n=3 统计效力（W4）和 SNR 定义缺失（W3）进一步削弱可信度。如果 W1+W2 能在 revision 中修复（改称 penalty method + 补充曲线），且 W3 的 SNR 给出明确定义，可升至 weak accept。

**Confidence**: 4/5
"Quite sure. I tried to check the important points carefully." 对优化理论和稀疏推理均有经验，仔细检查了梯度推导和实验设计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 180 · 2026-05-17T04:51:30.534798+00:00_

已收到 Reviewer 1 的 Round 2 审稿意见。2 个 critical（Lagrangian 术语误用 + 缺收敛曲线），3 个 warning，1 个 info。

等待 Reviewer 2 的审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 13

## Round 13

6 recorded events


### User

_source line 181 · 2026-05-17T04:51:31.568847+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：整体评分 **3.5/5 (Borderline Conference)**。核心贡献（KL 替代 BCE 训练稀疏预测器）有效且消融充分，但存在三个需修复的问题：(1) "Lagrangian" 术语实际是 penalty method，需正名；(2) Appendix C 缺 λ/sparsity 时序曲线（R1-W5 未完全关闭）；(3) gradient SNR 定义缺失。R1-W3（n=3 统计效力）未改善，仍是减分项但非 deal-breaker。

---

[Reviewer 2 审稿意见]:
## Round 2 审稿意见 — Reviewer 2（新颖性 + 完整性 + 写作质量）

### 1. Summary

This paper proposes training lightweight MLP sparsity predictors with KL divergence (instead of BCE) combined with Gumbel-Sigmoid relaxation to predict which FFN neurons to prune at inference in SwiGLU-based LLMs. The key argument is that KL couples all neurons through the output distribution, resolving BCE's structural mismatch with global top-k allocation. Experiments on LLaMA-3.1-8B and Mistral-7B show substantial PPL improvements over TEAL baselines, with analysis of sparsity regimes and a 2D taxonomy positioning the contribution.

### 2. Strengths

- **Clear structural argument**: The BCE vs. KL gradient analysis (§3.5) is well-motivated and the formal derivation (Eq. 7-8) makes the "coupling through downstream Jacobian" argument concrete and verifiable.
- **Thorough ablation design**: The loss-function isolation experiment (BCE + Gumbel + Lagrangian → PPL 38.02) cleanly demonstrates that the KL objective, not the relaxation mechanism, is the decisive factor.
- **Honest limitations**: The paper explicitly acknowledges that 6.4% overhead does NOT translate to speedup without sparse kernels, and that PPL is a poor proxy for reasoning (§4.4). The regime analysis (budget-surplus vs. capacity-limited) is a genuinely useful framework.
- **Reproducibility**: Training details are sufficient (1000 steps, WikiText-103, batch=4, AdamW, lr=1e-3, cosine decay). Three-seed variance reported.
- **SPON orthogonality analysis is convincing**: Cosine similarity 0.196 with quantitative PPL decomposition clearly separates the two methods' contributions.

### 3. Weaknesses

**W1 [critical] — Novelty is incremental: known components in a predictable configuration**

The paper combines: (1) KL distillation (standard in model compression since Hinton 2015), (2) Gumbel-Sigmoid relaxation (Jang et al. 2017), (3) lightweight MLP predictor (DejaVu 2023). The 2D taxonomy frames this as "filling an unexplored cell," but the combination is the obvious next step once you observe that SPON uses KL (static) and FastForward uses per-token (BCE). A reviewer could ask: why hadn't anyone done this already? If the answer is "it's straightforward to combine," the novelty bar for a main conference paper may not be met. The paper needs a stronger argument for why this specific combination required non-obvious insight beyond "replace BCE with KL and use Gumbel to make it differentiable."

**W2 [critical] — The "relative advantage grows with sparsity" claim is partially an artifact of baseline collapse**

The paper's central scaling narrative (18% → 49% → 82% advantage) measures (TEAL - KL) / TEAL. When TEAL collapses from 23.31 to 100.11, any reasonable method will show a growing "relative advantage" — this doesn't demonstrate that the KL predictor is doing something increasingly sophisticated at high sparsity. It would be more informative to report the KL predictor's PPL relative to dense (KL/Dense ratio) across sparsity levels: 8.98/6.12=1.47× at 30%, 11.79/6.12=1.93× at 50%, 17.91/6.12=2.93× at 70%. This shows the KL predictor also degrades substantially, just less catastrophically than TEAL.

**W3 [warning] — Scale limitation undermines generality claims**

Only two models are tested (LLaMA-3.1-8B and Mistral-7B-v0.3), both 7-8B parameters with SwiGLU. Claiming "transfers across SwiGLU architectures" from N=2 at a single scale is weak. No experiments on 13B, 70B, or non-SwiGLU architectures. The Limitations section acknowledges this but the Introduction and Abstract still frame the finding as if it's a general structural property of SwiGLU networks.

**W4 [warning] — Downstream task collapse at 50% sparsity raises practical concerns**

The paper shows that at 50% sparsity, all methods collapse on MMLU (27.89% ≈ random) and GSM8K (<2.2%). At 30%, KL-global actually hurts MMLU (25.27% vs. TEAL's 38.61%), and only uniform allocation recovers it (40.61%). The practical operating point is therefore ≤30%, where the PPL advantage is modest (8.98 vs. 10.97). The paper's flagship 50% results are impressive for PPL but useless for actual deployment if downstream tasks are destroyed.

**W5 [warning] — Em-dash usage signals AI-generated text**

12+ instances of explanatory em-dashes (---) in running text (introduction.tex lines 4, 6, 12, 28, 32, 35, 46; method.tex lines 41, 129, 148; abstract.tex line 8; related_work.tex line 11). This is a well-known AI writing marker that experienced reviewers will notice. While the writing is otherwise clean (no blacklist words, no -ing phrase abuse), the dash density is conspicuous.

**W6 [warning] — "Lagrangian" formulation is misleading terminology**

Eq. 7-8 describe a squared penalty with deadzone and multiplicative weight update, not a true Lagrangian relaxation (which uses $\lambda \cdot g(x)$ with dual ascent). The convergence properties of this heuristic controller differ fundamentally from Lagrangian duality. Calling it "Lagrangian" may confuse reviewers expecting formal dual convergence guarantees. "Adaptive penalty method" would be more accurate.

**W7 [info] — Reference count is low for EMNLP**

22 unique references is below typical EMNLP papers (30-50). Missing coverage includes:
- Mixture-of-Experts (conditional computation: Switch Transformer, GShard)
- Weight pruning baselines (Wanda, SparseGPT) — relevant for positioning
- Sparse kernel implementations (Triton block-sparse, STK) — referenced in Limitations but not cited
- Knowledge distillation beyond Hinton 2015 (Kim & Rush 2016, Sanh et al. 2019 DistilBERT)

### 4. Round 1 Resolved Issues Spot-Check

**R1-W1 (inference latency framing): ✅ RESOLVED**
The paper now clearly states in Limitations and Appendix A: "The pipeline adds ~6.4% overhead; net acceleration requires kernel-level sparse computation optimizations... Our contribution is prediction quality and inference simplification (eliminating the compensation network), not end-to-end latency reduction." No contradictory speedup claims remain.

**R1-W2 (cross-architecture claim): ✅ RESOLVED**
Framing now says "transfers across SwiGLU architectures of similar scale" (not "across architectures" broadly), with "within 7% at ≤50% sparsity" and explicit variance caveat at 70%. Table 5 reports exact numbers.

**R2-N3 (SPON distinction): ✅ RESOLVED**
Dedicated Related Work paragraph (§2, "Static Bias Correction") with clear differentiation: "SPON solves a static per-layer problem; we solve a global dynamic prediction problem." Quantitative orthogonality analysis (cosine 0.196) in §4.5.

**R2-W1 (MaskLLM in Related Work): ✅ RESOLVED**
MaskLLM discussed in §2 paragraph 2 with explicit differentiation: weight vs. activation sparsity, static N:M patterns vs. contextual per-token masks, Gumbel-Softmax vs. Gumbel-Sigmoid.

### 5. Questions for Authors

1. Have you measured per-neuron prediction accuracy of the KL predictor against the oracle top-k mask? If it's lower than BCE's >90% yet produces better output quality, that would strengthen the "structural mismatch" argument considerably.
2. What happens when you train a single predictor on multiple sparsity targets (e.g., with sparsity level as conditioning input)? The Limitations mention this as future work but it seems feasible.
3. The gradient SNR analysis reports absolute values of ~10⁻⁵. Is this measured on the raw gradient or after optimizer adaptation (Adam's second moment)? The interpretation differs significantly.
4. At 30% sparsity, KL-global MMLU (25.27%) is significantly worse than both TEAL (38.61%) and KL-uniform (40.61%). Can you explain why a KL-trained predictor under global allocation would hurt knowledge benchmarks despite better PPL?

### 6. Missing References

- Fedus et al. (2022), "Switch Transformers: Scaling to Trillion Parameter Models" — conditional computation via routing
- Sun et al. (2024), "A Simple and Effective Pruning Approach for Large Language Models" (Wanda) — magnitude pruning baseline
- Frantar & Alistarh (2023), "SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot" — structured pruning
- Kim & Rush (2016), "Sequence-Level Knowledge Distillation" — sequence-level KD for NLP
- Sanh et al. (2019), "DistilBERT, a distilled version of BERT" — KD for LMs
- Triton block-sparse documentation or relevant systems papers (since Triton is referenced in Limitations)

### 7. Overall Score

**Soundness: 3/5 (Acceptable)** — Main claims are supported but limited to 2 models at one scale. The "relative advantage grows" framing (W2) somewhat overstates the result. The Lagrangian terminology (W6) is imprecise.

**Excitement: 3/5 (Interesting)** — The structural mismatch argument is elegant and the regime analysis is useful, but the contribution is a predictable combination of known techniques. The practical operating point (≤30%) has modest gains.

**Overall: 3/5 (Findings)** — Solid execution of a logical idea with clear experimental validation, but novelty is incremental and scale is limited. Suitable for Findings of EMNLP rather than the main conference. Would be strengthened by: (a) experiments at 13B+ scale, (b) per-neuron accuracy comparison showing KL is worse on proxy but better on true objective, (c) addressing the practical utility question (at the one useful sparsity level of 30%, gains are moderate).

**Confidence: 4/5** — I am familiar with the activation sparsity and knowledge distillation literature. The one area of lower confidence is whether the novelty bar for main-track EMNLP 2026 has shifted enough that this combination counts as sufficient.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-17T04:52:06.461261+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness：对每一条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Summary\nThis paper proposes training lightweight MLP sparsity predictors with KL divergence (instead of BCE) combined with Gumbel-Sigmoid relaxation to predict which FFN neurons to prune at inference in SwiGLU-based LLMs. The key argument is that KL couples all neurons through the output distribution, resolving BCE's structural mismatch with global top-k allocation. Experiments on LLaMA-3.1-8B and Mistral-7B show substantial PPL improvements over TEAL baselines, with analysis of sparsity regimes and a 2D taxonomy positioning the contribution.\n\n### Strengths\n- Clear structural argument: The BCE vs. KL gradient analysis (§3.5) is well-motivated and the formal derivation (Eq. 7-8) makes the \"coupling through downstream Jacobian\" argument concrete and verifiable.\n- Thorough ablation design: The loss-function isolation experiment (BCE + Gumbel + Lagrangian → PPL 38.02) cleanly demonstrates that the KL objective, not the relaxation mechanism, is the decisive factor.\n- Honest limitations: The paper explicitly acknowledges that 6.4% overhead does NOT translate to speedup without sparse kernels, and that PPL is a poor proxy for reasoning (§4.4). The regime analysis (budget-surplus vs. capacity-limited) is a genuinely useful framework.\n- Reproducibility: Training details are sufficient (1000 steps, WikiText-103, batch=4, AdamW, lr=1e-3, cosine decay). Three-seed variance reported.\n- SPON orthogonality analysis is convincing: Cosine similarity 0.196 with quantitative PPL decomposition clearly separates the two methods' contributions.\n\n### Weaknesses\n\n**W1 [critical] — Novelty is incremental: known components in a predictable configuration**\nThe paper combines: (1) KL distillation (standard in model compression since Hinton 2015), (2) Gumbel-Sigmoid relaxation (Jang et al. 2017), (3) lightweight MLP predictor (DejaVu 2023). The 2D taxonomy frames this as \"filling an unexplored cell,\" but the combination is the obvious next step once you observe that SPON uses KL (static) and FastForward uses per-token (BCE). A reviewer could ask: why hadn't anyone done this already? If the answer is \"it's straightforward to combine,\" the novelty bar for a main conference paper may not be met.\n\n**W2 [critical] — The \"relative advantage grows with sparsity\" claim is partially an artifact of baseline collapse**\nThe paper's central scaling narrative (18% → 49% → 82% advantage) measures (TEAL - KL) / TEAL. When TEAL collapses from 23.31 to 100.11, any reasonable method will show a growing \"relative advantage.\" It would be more informative to report KL/Dense ratio across sparsity levels: 1.47× at 30%, 1.93× at 50%, 2.93× at 70%.\n\n**W3 [warning] — Scale limitation undermines generality claims**\nOnly two models tested (LLaMA-3.1-8B and Mistral-7B-v0.3), both 7-8B parameters with SwiGLU. No experiments on 13B, 70B, or non-SwiGLU architectures. Introduction/Abstract still frame it as if it's a general structural property.\n\n**W4 [warning] — Downstream task collapse at 50% sparsity raises practical concerns**\nAt 50% sparsity, all methods collapse on MMLU (27.89% ≈ random) and GSM8K (<2.2%). At 30%, KL-global hurts MMLU (25.27% vs. TEAL 38.61%). The practical operating point is ≤30%, where PPL advantage is modest (8.98 vs. 10.97).\n\n**W5 [warning] — Em-dash usage signals AI-generated text**\n12+ instances of explanatory em-dashes (---) in running text across introduction.tex, method.tex, abstract.tex, related_work.tex.\n\n**W6 [warning] — \"Lagrangian\" formulation is misleading terminology**\nEq. 7-8 describe a squared penalty with deadzone and multiplicative weight update, not a true Lagrangian relaxation. \"Adaptive penalty method\" would be more accurate.\n\n**W7 [info] — Reference count is low for EMNLP**\n22 unique references is below typical EMNLP papers (30-50). Missing: MoE, Wanda, SparseGPT, sequence-level KD, Triton.\n\n### Questions for Authors\n1. Have you measured per-neuron prediction accuracy of the KL predictor against the oracle top-k mask?\n2. What happens when you train a single predictor on multiple sparsity targets?\n3. The gradient SNR analysis reports absolute values of ~10⁻⁵. Is this measured on the raw gradient or after optimizer adaptation?\n4. At 30% sparsity, KL-global MMLU (25.27%) is significantly worse than both TEAL (38.61%) and KL-uniform (40.61%). Can you explain why?\n\n### Overall Score\n3/5 (Findings) — Solid execution of a logical idea with clear experimental validation, but novelty is incremental and scale is limited. Suitable for Findings of EMNLP rather than the main conference.\nConfidence: 4/5",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness：对每一条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Summary\nThis paper proposes training lightweight MLP sparsity predictors with KL divergence (instead of BCE) combined with Gumbel-Sigmoid relaxation to predict which FFN neurons to prune at inference in SwiGLU-based LLMs. The key argument is that KL couples all neurons through the output distribution, resolving BCE's structural mismatch with global top-k allocation. Experiments on LLaMA-3.1-8B and Mistral-7B show substantial PPL improvements over TEAL baselines, with analysis of sparsity regimes and a 2D taxonomy positioning the contribution.\n\n### Strengths\n- Clear structural argument: The BCE vs. KL gradient analysis (§3.5) is well-motivated and the formal derivation (Eq. 7-8) makes the \"coupling through downstream Jacobian\" argument concrete and verifiable.\n- Thorough ablation design: The loss-function isolation experiment (BCE + Gumbel + Lagrangian → PPL 38.02) cleanly demonstrates that the KL objective, not the relaxation mechanism, is the decisive factor.\n- Honest limitations: The paper explicitly acknowledges that 6.4% overhead does NOT translate to speedup without sparse kernels, and that PPL is a poor proxy for reasoning (§4.4). The regime analysis (budget-surplus vs. capacity-limited) is a genuinely useful framework.\n- Reproducibility: Training details are sufficient (1000 steps, WikiText-103, batch=4, AdamW, lr=1e-3, cosine decay). Three-seed variance reported.\n- SPON orthogonality analysis is convincing: Cosine similarity 0.196 with quantitative PPL decomposition clearly separates the two methods' contributions.\n\n### Weaknesses\n\n**W1 [critical] — Novelty is incremental: known components in a predictable configuration**\nThe paper combines: (1) KL distillation (standard in model compression since Hinton 2015), (2) Gumbel-Sigmoid relaxation (Jang et al. 2017), (3) lightweight MLP predictor (DejaVu 2023). The 2D taxonomy frames this as \"filling an unexplored cell,\" but the combination is the obvious next step once you observe that SPON uses KL (static) and FastForward uses per-token (BCE). A reviewer could ask: why hadn't anyone done this already? If the answer is \"it's straightforward to combine,\" the novelty bar for a main conference paper may not be met.\n\n**W2 [critical] — The \"relative advantage grows with sparsity\" claim is partially an artifact of baseline collapse**\nThe paper's central scaling narrative (18% → 49% → 82% advantage) measures (TEAL - KL) / TEAL. When TEAL collapses from 23.31 to 100.11, any reasonable method will show a growing \"relative advantage.\" It would be more informative to report KL/Dense ratio across sparsity levels: 1.47× at 30%, 1.93× at 50%, 2.93× at 70%.\n\n**W3 [warning] — Scale limitation undermines generality claims**\nOnly two models tested (LLaMA-3.1-8B and Mistral-7B-v0.3), both 7-8B parameters with SwiGLU. No experiments on 13B, 70B, or non-SwiGLU architectures. Introduction/Abstract still frame it as if it's a general structural property.\n\n**W4 [warning] — Downstream task collapse at 50% sparsity raises practical concerns**\nAt 50% sparsity, all methods collapse on MMLU (27.89% ≈ random) and GSM8K (<2.2%). At 30%, KL-global hurts MMLU (25.27% vs. TEAL 38.61%). The practical operating point is ≤30%, where PPL advantage is modest (8.98 vs. 10.97).\n\n**W5 [warning] — Em-dash usage signals AI-generated text**\n12+ instances of explanatory em-dashes (---) in running text across introduction.tex, method.tex, abstract.tex, related_work.tex.\n\n**W6 [warning] — \"Lagrangian\" formulation is misleading terminology**\nEq. 7-8 describe a squared penalty with deadzone and multiplicative weight update, not a true Lagrangian relaxation. \"Adaptive penalty method\" would be more accurate.\n\n**W7 [info] — Reference count is low for EMNLP**\n22 unique references is below typical EMNLP papers (30-50). Missing: MoE, Wanda, SparseGPT, sequence-level KD, Triton.\n\n### Questions for Authors\n1. Have you measured per-neuron prediction accuracy of the KL predictor against the oracle top-k mask?\n2. What happens when you train a single predictor on multiple sparsity targets?\n3. The gradient SNR analysis reports absolute values of ~10⁻⁵. Is this measured on the raw gradient or after optimizer adaptation?\n4. At 30% sparsity, KL-global MMLU (25.27%) is significantly worse than both TEAL (38.61%) and KL-uniform (40.61%). Can you explain why?\n\n### Overall Score\n3/5 (Findings) — Solid execution of a logical idea with clear experimental validation, but novelty is incremental and scale is limited. Suitable for Findings of EMNLP rather than the main conference.\nConfidence: 4/5",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-17T04:52:39.850869+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33389
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-17T04:52:40.404040+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness：对每一条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Summary\n本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。方法在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。\n\n### Strengths\n- 核心贡献清晰且可验证：KL vs BCE 的结构性差异论证（§3.6 梯度分析）逻辑自洽，且有实证 SNR 数据支撑（5.76×）。\n- 消融设计良好：Table 3 系统隔离了 loss function（ΔP=26.23）vs relaxation method（ΔP=3.98）。\n- Iso-compute 分析（§4.3）：BCE 2700 步 loss 饱和证明结构性失败。\n- Cross-architecture 验证：两个不同架构上 advantage ratio 一致性（≤50% 时 within 7%）。\n- Regime 分析有实用价值。\n- Limitations 诚实。\n\n### Weaknesses\n\n**W1 [critical] \"Lagrangian\" 术语不准确，非标准对偶方法**\n- Eq. 9 是带 deadzone 的二次惩罚项 λ·clamp(|s̄-(1-ρ)|-ε, min=0)²，Eq. 10 的更新规则是几何倍增/减半（×2/×0.5），既不是标准 augmented Lagrangian，也不是对偶上升法。将其称为 \"Lagrangian\" 和 \"dual variable\" 存在术语误导。Penalty method 不保证满足 KKT 条件。\n\n**W2 [critical] Appendix C 缺少 λ/sparsity 时序曲线（R1-W5 未完全修复）**\n- Table 7 仅报告最终状态。30% 和 70% target 的 λ 均 hit cap（5000 和 1000），表明系统可能在 cap boundary 震荡。缺少训练过程中 λ 和 actual sparsity 随 step 变化的时序曲线。\n\n**W3 [warning] 梯度 SNR 定义不明确且样本量小**\n- \"gradient SNR\" 未给出数学定义。仅 80 步的测量样本量偏小。5.77 vs 5.76 精度不一致。\n\n**W4 [warning] n=3 seeds 统计效力不足（R1-W3 未改善）**\n- 论文仍使用 3 seeds，仅以 CV<1% 作为 justification。KL global (11.79) vs KL uniform (11.96) 之差 0.17，以 std=0.07 计算，n=3 自由度=2 无法确信 p<0.05。Cross-arch \"within 7%\" 无 CI。\n\n**W5 [warning] 无实际推理加速，且 overhead 表述可能误导读者**\n- Abstract/Introduction 的 \"reduces effective computation\" framing 让读者期望实际加速，但实测增加 6.4% latency。\n\n**W6 [info] 30% 稀疏度 MMLU 异常未充分解释**\n- KL global 在 30% MMLU 仅 25.27%（接近随机），论文归因于 \"global top-k starves knowledge-critical layers\" 但缺乏 layer-wise 分析。\n\n### Questions for Authors\n1. Eq. 10 的几何倍增如何保证收敛？当 λ hit cap 时约束能否精确满足？\n2. Gradient SNR 的精确定义是什么？over what dimensions?\n3. 30% KL global MMLU 退化 40pp，推荐的实际使用方案是什么？\n4. BCE+Gumbel+Lagrangian (38.02) 比 vanilla BCE (27.97) 更差，是否说明 Gumbel-Sigmoid 本身引入噪声？\n5. SPON cosine similarity 0.196 为 \"near-orthogonal\"——在 14336 维空间中 0.196 是否 moderate positive correlation?\n\n### Missing References\n- Wanda (Sun et al., 2024), SparseGPT (Frantar & Alistarh, 2023), Mixture-of-Experts (Fedus et al., 2022), Gumbel-Sigmoid 标准引用（Maddison et al. 2017 / Louizos et al. 2018）\n\n### Overall Score\n3.5/5 (Borderline Conference) — 核心贡献有效且消融充分，但 Lagrangian 术语误用、收敛曲线缺失、n=3 效力不足降低 rigor。如 W1+W2 修复可升至 weak accept。\nConfidence: 4/5",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness：对每一条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Summary\n本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。方法在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。\n\n### Strengths\n- 核心贡献清晰且可验证：KL vs BCE 的结构性差异论证（§3.6 梯度分析）逻辑自洽，且有实证 SNR 数据支撑（5.76×）。\n- 消融设计良好：Table 3 系统隔离了 loss function（ΔP=26.23）vs relaxation method（ΔP=3.98）。\n- Iso-compute 分析（§4.3）：BCE 2700 步 loss 饱和证明结构性失败。\n- Cross-architecture 验证：两个不同架构上 advantage ratio 一致性（≤50% 时 within 7%）。\n- Regime 分析有实用价值。\n- Limitations 诚实。\n\n### Weaknesses\n\n**W1 [critical] \"Lagrangian\" 术语不准确，非标准对偶方法**\n- Eq. 9 是带 deadzone 的二次惩罚项 λ·clamp(|s̄-(1-ρ)|-ε, min=0)²，Eq. 10 的更新规则是几何倍增/减半（×2/×0.5），既不是标准 augmented Lagrangian，也不是对偶上升法。将其称为 \"Lagrangian\" 和 \"dual variable\" 存在术语误导。Penalty method 不保证满足 KKT 条件。\n\n**W2 [critical] Appendix C 缺少 λ/sparsity 时序曲线（R1-W5 未完全修复）**\n- Table 7 仅报告最终状态。30% 和 70% target 的 λ 均 hit cap（5000 和 1000），表明系统可能在 cap boundary 震荡。缺少训练过程中 λ 和 actual sparsity 随 step 变化的时序曲线。\n\n**W3 [warning] 梯度 SNR 定义不明确且样本量小**\n- \"gradient SNR\" 未给出数学定义。仅 80 步的测量样本量偏小。5.77 vs 5.76 精度不一致。\n\n**W4 [warning] n=3 seeds 统计效力不足（R1-W3 未改善）**\n- 论文仍使用 3 seeds，仅以 CV<1% 作为 justification。KL global (11.79) vs KL uniform (11.96) 之差 0.17，以 std=0.07 计算，n=3 自由度=2 无法确信 p<0.05。Cross-arch \"within 7%\" 无 CI。\n\n**W5 [warning] 无实际推理加速，且 overhead 表述可能误导读者**\n- Abstract/Introduction 的 \"reduces effective computation\" framing 让读者期望实际加速，但实测增加 6.4% latency。\n\n**W6 [info] 30% 稀疏度 MMLU 异常未充分解释**\n- KL global 在 30% MMLU 仅 25.27%（接近随机），论文归因于 \"global top-k starves knowledge-critical layers\" 但缺乏 layer-wise 分析。\n\n### Questions for Authors\n1. Eq. 10 的几何倍增如何保证收敛？当 λ hit cap 时约束能否精确满足？\n2. Gradient SNR 的精确定义是什么？over what dimensions?\n3. 30% KL global MMLU 退化 40pp，推荐的实际使用方案是什么？\n4. BCE+Gumbel+Lagrangian (38.02) 比 vanilla BCE (27.97) 更差，是否说明 Gumbel-Sigmoid 本身引入噪声？\n5. SPON cosine similarity 0.196 为 \"near-orthogonal\"——在 14336 维空间中 0.196 是否 moderate positive correlation?\n\n### Missing References\n- Wanda (Sun et al., 2024), SparseGPT (Frantar & Alistarh, 2023), Mixture-of-Experts (Fedus et al., 2022), Gumbel-Sigmoid 标准引用（Maddison et al. 2017 / Louizos et al. 2018）\n\n### Overall Score\n3.5/5 (Borderline Conference) — 核心贡献有效且消融充分，但 Lagrangian 术语误用、收敛曲线缺失、n=3 效力不足降低 rigor。如 W1+W2 修复可升至 weak accept。\nConfidence: 4/5",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-17T04:52:41.715286+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1311
}
```

</details>

---


### Assistant

_source line 186 · 2026-05-17T04:52:45.473337+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应（[AGREE]/[REBUT]）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 187 · 2026-05-17T04:52:46.980248+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Findings 级别（3/5）**。论文执行扎实，结构论证清晰（BCE vs. KL 梯度分析），但新颖性有限（已知技术的可预期组合），且实验规模仅限 7-8B 两个模型。主要问题包括：

1. **新颖性不足**（critical）：KL distillation + Gumbel-Sigmoid + MLP predictor 是已有技术的自然组合
2. **"相对优势随 sparsity 增长"部分是 baseline 崩溃的假象**（critical）
3. 实际可用 sparsity（≤30%）的增益有限（PPL 8.98 vs. 10.97）
4. 12+ 处解释性 em-dash 是 AI 写作信号
5. Round 1 的四项 resolved issues 全部确认已修复到位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 188 · 2026-05-17T04:52:55.429826+00:00_

交叉分享已发送给两位 Reviewer，等待逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 189 · 2026-05-17T04:53:26.491927+00:00_

[Reviewer 1 审稿意见]:
## 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应

---

**[REBUT] R2-W1: Novelty is incremental**

不完全同意 "predictable combination" 的判断。关键证据是 Table 3 的 BCE+Gumbel+Lagrangian 实验（PPL 38.02）：如果组合是 "obvious"，那为什么将 Gumbel-Sigmoid 和 Lagrangian 直接应用于 BCE 反而比 vanilla BCE（27.97）更差？这说明 Gumbel 松弛与 loss function 之间存在非平凡的交互——Lagrangian penalty 在 BCE 下会干扰 per-neuron optimization（§4.4 第三段明确讨论）。仅仅 "填表格" 不足以构成贡献，但论文的核心洞察不是 "KL 比 BCE 好" 这个 general statement，而是具体机制：BCE 梯度 factorize per-neuron（Eq. 8）导致无法学到 global top-k 所需的 inter-neuron coupling。这个 mismatch 的诊断（§3.6 gradient analysis）+ 实证验证（iso-compute saturation）超越了简单 component combination。

但 R2 的质疑并非无理：论文 2D taxonomy 的 framing 确实有 "填空" 嫌疑，且 KL distillation 本身不新。如果这篇论文去掉 gradient analysis 和 regime analysis，只剩 "KL 比 BCE 好"，那确实 incremental。目前版本的 contribution 在 borderline。

---

**[AGREE] R2-W2: Relative advantage 部分是 baseline collapse 的 artifact**

完全同意。(TEAL-KL)/TEAL 作为 metric 在 TEAL 崩溃时会 inflate。Table 4 数据：
- 30%: KL/Dense = 8.98/6.12 = 1.47×
- 50%: KL/Dense = 11.79/6.12 = 1.93×
- 70%: KL/Dense = 17.91/6.12 = 2.93×

这个 framing 更诚实地反映了 KL predictor 自身的质量退化曲线。论文 Abstract 第 5 行 "18% at 30%, 49% at 50%, and 82% at 70%" 的叙事过度依赖于 TEAL 的失败来 inflate 自己的优势。建议作者至少同时报告 KL/Dense ratio。

不过补充一点：即使 reframe 为 KL/Dense，从 1.47× 到 2.93× 的增长仍然表明 KL predictor 在高稀疏度下也显著退化（dense 到 2.93× 的 gap 并不小）。这更凸显了 capacity-limited regime（§4.5）的诚实性。

---

**[AGREE] R2-W3: Scale limitation undermines generality claims**

同意。两个 7-8B SwiGLU 模型不足以支撑 "structural property of SwiGLU networks"（§4.6 末句）的泛化 claim。尤其是：
- 13B/70B 模型的 layer 数和 d_ff 不同，Jacobian chain（factor (b) in Eq. 12）的 depth 效应可能质变
- Limitations 中承认了这一点，但 Introduction 和 Abstract 的 framing 仍然偏 general

不过严格来说，论文使用的措辞是 "transfers across SwiGLU architectures of similar scale"（Abstract 第 6 行），加了 "of similar scale" 的限定词，这在 Round 1 后已有改进。问题在于 §4.6 最后一句 "evidence that the method exploits a structural property of SwiGLU networks" 仍然过强——应加 "at 7-8B scale" 限定。

---

**[AGREE] R2-W4: Downstream collapse raises practical concerns**

同意这是一个重要的实践限制。数据支撑：
- 50% sparsity: MMLU 27.89% ≈ random（Table 2）
- 30% KL-global: MMLU 25.27%，甚至比 TEAL 的 38.61% 更差（Table 2）
- 实际推荐操作点仅为 30% uniform（MMLU 40.61%），PPL 优势仅 8.82 vs 10.97

论文的 regime 分析（§4.5）诚实地展示了这些数据，并且 Limitations 中推荐 30% 为 "recommended operating point for downstream fidelity"。但 R2 的批评是合理的：如果实际有用的区间只有 ≤30%，那 50%/70% 的大幅 PPL 优势在实践中意义有限（downstream 都崩了）。

论文核心贡献仍然成立（方法论 + 分析框架），但 impact 确实被这一限制约束。

---

**[REBUT] R2-W5: Em-dash usage signals AI-generated text**

部分不同意将此列为 [warning] 级别问题。

首先事实确认：LaTeX 中 `---` 产生 em-dash，论文中确实有多处使用（如 Abstract 第 8 行 "three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---"；Introduction 中也有类似用法）。

但作为审稿意见，这属于 stylistic preference 而非学术质量问题。Em-dash 在英文学术写作中是合法标点（Chicago Manual of Style 认可），许多人类作者也使用。将 em-dash 等同于 "AI-generated" 是一种 heuristic，不是 evidence。这个问题最多属于 [info] 级别的 minor suggestion，不应影响接收决定。

如果真要修，建议作者减少使用频率即可（改为逗号或拆分句子），但这不应是审稿意见中的 warning。

---

**[AGREE] R2-W6: "Lagrangian" formulation is misleading terminology**

完全同意，这与我 Round 2 review 中的 W1 是同一问题。Eq. 9 是二次惩罚 + deadzone，Eq. 10 是几何倍增/减半——这不是 Lagrangian dual ascent。"Adaptive penalty controller" 更准确。两位 reviewer 独立指出同一问题，增强了这个 concern 的权重。

---

**[AGREE] R2-W7: Reference count is low**

同意。我在自己的 review 中也指出缺少 Wanda、SparseGPT、MoE、Louizos et al. 2018 (L0/Concrete distribution) 等引用。22 refs 对 EMNLP main 偏少，30-40 是更合理的密度。尤其是 pruning 领域的经典工作（Wanda, SparseGPT）和 conditional computation（MoE）应该在 Related Work 中有所 acknowledge。

---

### 总结

与 Reviewer 2 的主要分歧点：
1. **W1 (novelty)**: 我认为论文的 gradient mismatch 诊断 + iso-compute verification + regime analysis 超越了简单 component combination，但同意 2D taxonomy framing 有填空嫌疑。Overall novelty borderline。
2. **W5 (em-dash)**: 不应作为 warning 级别问题。

与 Reviewer 2 的一致点：
- W2 (relative advantage inflation)、W3 (scale)、W4 (downstream collapse)、W6 (Lagrangian 术语)、W7 (reference count) 均为有效批评。

我的 overall 评价维持 3.5 (Borderline Conference)，略高于 R2 的 3.0 (Findings)。分歧在于对 novelty 和 analytical contribution 的权重：如果重视方法论洞察（gradient coupling mechanism + regime analysis），主会可接受；如果要求 novel algorithm 或 scaling evidence，Findings 更合适。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 190 · 2026-05-17T04:53:36.693405+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 191 · 2026-05-17T04:53:39.209280+00:00_

[Reviewer 1 审稿结果]:
已提交交叉回应。总结：

- **REBUT**: W1 (novelty) — BCE+Gumbel+Lagrangian 实验 (PPL 38.02 > vanilla BCE 27.97) 证明组合并非 trivial；W5 (em-dash) — stylistic preference 不应为 warning 级别
- **AGREE**: W2 (relative advantage inflation)、W3 (scale)、W4 (downstream collapse)、W6 (Lagrangian 术语)、W7 (reference count)

两位 reviewer 在 Lagrangian 术语误用和 reference 不足上完全一致；主要分歧在 novelty 评估和 overall score（我 3.5 vs R2 3.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 192 · 2026-05-17T04:53:48.085357+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 17

## Round 17

8 recorded events


### User

_source line 193 · 2026-05-17T04:54:09.553899+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 各 Weakness 逐条评议

---

**[AGREE] R1-W1: "Lagrangian" 术语不准确**

完全同意。我在自己的审稿意见中也独立提出了同一问题（R2-W6）。Eq. 9 的 clamp(|·|-ε, min=0)² 是带 deadzone 的二次惩罚，Eq. 10 的 ×2/×0.5 几何更新是启发式 schedule，两者均不符合标准 augmented Lagrangian 或对偶上升法的形式定义。标准 Lagrangian 对偶法使用 λ←λ+α·g(x) 且在适当步长下保证收敛到 KKT 点；论文的方法虽然实验中 work（Table 7 shows <5% deviation），但缺乏收敛保证。两位 reviewer 独立识别此问题进一步确认这不是挑剔，而是 rigor 问题。

---

**[AGREE] R1-W2: Appendix C 缺 λ/sparsity 时序曲线**

同意这是一个缺失。Table 7 确实只报告最终状态：30% target → λ=5000 (cap), actual=0.285 (deviation 5.0%)；70% target → λ=1000 (cap), actual=0.688 (deviation 1.7%)。λ 撞到 cap 意味着约束可能未被精确满足（30% 的 5% deviation 已经相当大）。没有时序曲线，无法判断：(a) λ 是否在 cap boundary 震荡；(b) sparsity 是否在训练后期稳定。论文声称 "~10 steps to reach steady state" (Appendix C) 但没有可视化证据。

不过我补充一点：即使 30% 的 actual sparsity 偏低到 0.285（即少剪了 1.5pp），这对最终 PPL 的影响可能很小（论文已经展示 30%→40% 的 PPL 变化是连续的）。所以这更多是 presentation rigor 问题，不太会改变核心结论。

---

**[REBUT] R1-W3: 梯度 SNR 定义不明确且样本量小**

部分不同意 severity。

1. **定义问题**：确实论文未给出显式数学定义，这是写作缺陷。但 gradient SNR 在优化文献中有标准含义：SNR = E[g]² / Var[g]（或 ||E[g]|| / ||Var[g]||^0.5），其中 g 是 mini-batch 梯度。上下文足以推断意图，但应在 revision 中显式定义。

2. **样本量**：80 steps 并不算"小"。这不是一个统计检验——它是一个诊断测量（类似于 profiling），报告 average SNR over training trajectory。每个 step 本身涉及 batch_size×seq_len = 4×2048 = 8192 个 token 位置的梯度，所以底层样本量远大于 80。80 步覆盖了训练早期（step 1-80），正是论文想要展示 "BCE collapses to ~10⁻⁸ after step 10" 的关键区间。

3. **精度问题**（5.77 vs 5.76）：这确实是 typo-level 的不一致（§3.5 写 "5.76× higher" 然后报告值 5.77×10⁻⁵），但影响可忽略。

建议降低为 info 级别。核心观察（KL 梯度信号质量显著优于 BCE）通过 PPL 结果本身得到间接验证，SNR 分析是补充解释而非核心证据。

---

**[AGREE] R1-W4: n=3 seeds 统计效力不足**

同意方向但略有保留。

论文报告 PPL 11.92±0.07 (CV<1%)，如果仅用于证明"训练稳定"则 n=3 可接受。但问题出在论文同时用这些数字来支持 global vs. uniform 的 regime 比较（11.79 vs. 11.96，差值 0.17 = 2.4 sigma），这确实需要更多 seeds 或 paired test 来确认。

但我注意到论文的 regime 分析（§4.4 Table 4）不依赖 50% 的 global/uniform 差异——它依赖 30% 的 MMLU 差异 (25.27% vs 40.61% = 15pp) 和 40% 的反转 (38.06% vs 30.68% = 7pp)，这些差距远大于 noise floor。所以 R1-W4 对 stability claim 有效，但不影响 regime 分析的核心结论。

---

**[REBUT] R1-W5: "reduces effective computation" framing 误导**

部分不同意。

Abstract 第一句 "Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference" 是对这个 **研究领域** 的 general statement，不是对本文方法的 claim。论文自己的 contribution framing 始终是 "eliminates the need for error compensation networks"（架构简化）而非 "speeds up inference"。

Appendix A 明确写道："Our contribution is prediction quality and inference simplification (eliminating the compensation network), not end-to-end latency reduction."（App. A 最后一段）

Limitations 进一步写道："While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations..."

我认为 R1-W1（resolved check）已确认此问题在 Round 1 后已修复。如果 Reviewer 1 仍觉得 framing 有误导性，可能是对 Abstract 首句的解读差异。但从严格文本分析看，论文没有 claim 自己的方法提供了实际加速。

---

**[AGREE] R1-W6: 30% MMLU 异常未充分解释**

同意。这是我自己 Questions for Authors Q4 中也提出的问题。

论文给出的解释是 "global top-k starves knowledge-critical layers"（§4.4），但这只是一个 hypothesis，没有支撑证据。需要的证据包括：
- Layer-wise budget distribution 可视化（哪些层在 global 分配下被 starve？）
- 具体哪些层对 MMLU-type factual recall 关键（已有文献如 Geva et al. 2021 指出 early/middle layers 存储 factual knowledge）
- 为什么同样的 "starving" 不影响 PPL 但影响 MMLU？

这个异常实际上对论文的实用 message 有重大影响：如果推荐操作点是 30% + uniform allocation（PPL 8.82, MMLU 40.61%），那论文的 "global TEAL allocation" 推理协议反而不是最优选择。这个 tension 需要在正文中更显式讨论。

---

### 总结

| R1 Issue | 我的判断 | 备注 |
|----------|---------|------|
| W1 Lagrangian 术语 | AGREE (critical) | 与我的 R2-W6 完全一致 |
| W2 时序曲线缺失 | AGREE (warning→) | 影响 rigor 但不影响核心结论 |
| W3 SNR 定义/样本量 | REBUT (降为 info) | 80 步覆盖关键区间，样本量底层足够 |
| W4 n=3 效力 | AGREE (warning) | 对 stability ok，但 global/uniform 对比需 more seeds |
| W5 Computation framing | REBUT | 论文已在 R1 后修复，文本分析不支持 "误导" |
| W6 30% MMLU 异常 | AGREE (warning) | 缺 layer-wise 分析；影响实用建议 |

**两位 reviewer 共识问题**：W1（Lagrangian 术语）、W6（30% MMLU）、scale limitation（我的 R2-W3，R1 未显式提但在 Q 中 implied）。这些是 revision 的优先修复项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-17T04:54:31.876442+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-17T04:54:31.977337+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"projects/distill_sparse_swiglu/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-17T04:47:42.616400+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_dbbf8d2c695f1e79e11713aebc107790\", \"skipped_at\": \"2026-05-17T04:49:47.064547+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-17T04:56:24.257878+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规——当前为 conclusion 内 paragraph，ARR 要求独立 section*\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 交叉回应 AGREE。desk-reject 条件。\"}\n    action_items:\n      - {round: 1, action: \"将 \\\\paragraph{Limitations.} 拆为独立 \\\\section*{Limitations}\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 7018701: Limitations 拆为独立 section*，8p 正文确认合规\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限——正文含 Limitations/Future work 延伸至第 9 页，long paper 限 8 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 AGREE。\"}\n    action_items:\n      - {round: 1, action: \"拆出 Limitations 后编译确认页数\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"编译确认: main content 结束于 page 8, Limitations ARR exempt, 总 10p PDF\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"训练/评估数据同源（WikiText-103→WikiText-2），缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 critical。R2 AGREE with nuance。\"}\n    action_items:\n      - {round: 1, action: \"用已训练好的 predictor 在 C4 validation set 上评估 PPL（含 dense + TEAL baseline）\", assigned_to: \"main_agent\", status: done}\n    resolution: \"C4 validation (200 samples, streaming): Dense=9.21, KL 50%=18.40, TEAL 50%=38.75. KL 在 OOD 上保持 2.1× 优于 TEAL，相对优势泛化。\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"'Structural failure' 声明缺充分证据——BCE 仅测一个 configuration，对比不公平\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 critical，R2 独立指出相同问题。\"}\n    action_items:\n      - {round: 1, action: \"BCE+Gumbel+Lagrangian ×3 LR (1e-4/1e-3/3e-3) 对照实验\", assigned_to: \"main_agent\", status: done}\n    resolution: \"Clean isolation 完成: BCE+Gumbel best PPL=38.02 (lr=3e-3) vs KL=11.79, 甚至比原始 BCE+STE (22.51) 更差。唯一变量是 loss function → structural mismatch confirmed。\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融实验缺关键维度——d_b sensitivity、温度 schedule、training curve、Lagrangian LR\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 列为 critical，R2 PARTIALLY AGREE。降为 warning。\"}\n    action_items:\n      - {round: 1, action: \"d_b={64,128,256,512} sensitivity sweep + training loss curve + λ curve\", assigned_to: \"main_agent\", status: done}\n    resolution: \"Appendix B: d_b sensitivity (<3% PPL range), B.1: τ schedule (<1.8% range), B.2: Training convergence (800 steps saturation), C: Lagrangian dynamics (λ trajectory table across 4 targets). All dimensions covered.\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"论文增加 6.4% 推理延迟，未实现 wall-clock 加速，与 abstract/intro framing 矛盾\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7，两人独立一致。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R2 spot-check 确认已修复。R1 仍有轻微顾虑但 R2 REBUT 认为文本分析不支持误导。\"}\n    action_items:\n      - {round: 1, action: \"Abstract/Intro reframe 为 prediction quality + inference simplification\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: 'accelerate'→'reduces effective computation', 'speedup'→'simplify inference', Appendix A caveat added. Round 2 confirmed fixed.\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Cross-architecture 验证仅 Mistral-7B 一个模型且仅 50% 一个点，泛化 claim 过强\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W2 = R2-W5，两人独立一致。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R2 spot-check 确认已修复。R1 AGREE scale limitation 仍在但 framing 已弱化。\"}\n    action_items:\n      - {round: 1, action: \"弱化措辞为 'preliminary evaluation on one additional model'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: 删除 'verify generality'/'transferability', 改为 'preliminary evaluation...suggests may generalize'. Round 2 confirmed.\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"新颖性有限——与 SPON 区分度不充分，核心技术为已知方法的新组合\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 列为 critical，R1 REBUT。降为 warning。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R2 spot-check 确认 SPON 区分已修复。但 novelty 整体仍存争议（见 R2-W1-Rd2）。\"}\n    action_items:\n      - {round: 1, action: \"更清晰 formalize per-token vs static KL 的差异\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: 明确 'closed-form static KL' vs 'end-to-end contextual KL with Gumbel-Sigmoid'. Round 2 SPON distinction confirmed.\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"遗漏重要相关工作 MaskLLM (Fang et al., NeurIPS 2024 Spotlight)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 强烈 AGREE。\"}\n      - {round: 2, reviewers: [2], note: \"R2 spot-check 确认已修复。\"}\n    action_items:\n      - {round: 1, action: \"Related Work 增加 MaskLLM 讨论并区分\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: MaskLLM added to Related Work + bib. Round 2 confirmed.\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 (§3.5) 是 informal argument，论文 oversell 为 theoretical contribution\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W4 ≈ R2-W3，两人独立一致。\"}\n      - {round: 2, reviewers: [1], note: \"R1 确认 framing 已修复为 'Gradient-Based Motivation'，SNR 5.76× 数据已添加。但 SNR 定义缺失仍为小问题（见 R1-W3-Rd2）。\"}\n    action_items:\n      - {round: 1, action: \"弱化为 'gradient-based motivation'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 1, action: \"添加实证 gradient SNR 数据 (KL/BCE=5.76×, early layers 34-156×)\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"§3.6 标题改为 'Gradient-Based Motivation'，framing 合理。SNR 5.76× 数据已添加。Round 2 R1 确认基本完成。\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"Lagrangian 对偶更新缺收敛分析——未报告 η_λ、λ 轨迹、实际 sparsity ratio 曲线\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出，R2 交叉 AGREE。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R1 列为 critical (W2)：Table 7 仅最终状态，缺时序曲线。R2 AGREE 但认为不影响核心结论。\"}\n    action_items:\n      - {round: 1, action: \"从训练 log 提取 λ 和 sparsity ratio over training steps 的曲线图，加入 Appendix\", assigned_to: \"main_agent\", status: in_progress}\n      - {round: 2, action: \"补充 Figure: 30%/50%/70% 的 (step, λ) 和 (step, actual_sparsity) 时序曲线\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W6\"\n    summary: \"2D taxonomy 作为 contribution 列出，但实为 post-hoc classification，贡献有限\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 部分 REBUT。\"}\n    action_items:\n      - {round: 1, action: \"降级为 organizational framework\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 7018701: contribution list 改为 'organize prior work via 2D framework'\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"三 seed (n=3) 统计效力弱\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出，R2 REBUT（ML 惯例可接受）。降为 info。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R1 维持 warning；R2 AGREE 方向但指出 regime 分析不受影响（差异远大于 noise floor）。共识：对 global/uniform 对比影响有限。\"}\n    action_items:\n      - {round: 1, action: \"保持现状\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型验证，边界是否随 scale 变化未知\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2-W5, R1 交叉 AGREE。\"}\n    action_items:\n      - {round: 1, action: \"加 caveat 承认 boundaries 是 model-specific\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: §4.5 caveat added about boundaries being model-specific\"\n    resolution_round: 1\n\n  # Round 2 新发现\n  - id: \"R1-W1-Rd2\"\n    summary: \"'Lagrangian' 术语误用——实为 adaptive penalty method with deadzone + geometric schedule，非标准对偶方法\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R1 列为 critical W1，R2 独立提出 W6。交叉回应双方均 AGREE。两位 reviewer 独立一致。\"}\n    action_items:\n      - {round: 2, action: \"将 'Lagrangian' 改称 'adaptive penalty controller' 或 'adaptive penalty method'；讨论为何不用标准对偶上升及收敛保证缺失\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1-Rd2\"\n    summary: \"新颖性有限——KL distillation + Gumbel-Sigmoid + MLP predictor 是已知技术的可预期组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 critical。R1 REBUT：BCE+Gumbel 实验 (38.02>27.97) 证明组合非 trivial，gradient mismatch 诊断超越简单 combination。但同意 2D taxonomy framing 有填空嫌疑。分歧未解决。\"}\n    action_items:\n      - {round: 2, action: \"强化 'why non-trivial' 论证：(1) 突出 BCE+Gumbel 反效果作为 non-obvious evidence；(2) 弱化 2D taxonomy 的 contribution 权重\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"'相对优势随 sparsity 增长' claim 部分是 baseline (TEAL) 崩溃的假象，应同时报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 critical。R1 AGREE：(TEAL-KL)/TEAL inflate；应同时报告 KL/Dense ratio (1.47×/1.93×/2.93×)。\"}\n    action_items:\n      - {round: 2, action: \"Abstract 和 §4 同时报告 KL/Dense ratio；弱化 '18%→49%→82%' 的叙事依赖\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale limitation——仅 2 个 7-8B SwiGLU 模型，§4.6 'structural property of SwiGLU networks' claim 过强\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 提出 warning。R1 AGREE：§4.6 末句应加 'at 7-8B scale' 限定。\"}\n    action_items:\n      - {round: 2, action: \"§4.6 末句加 'at 7-8B scale' 限定；Abstract 'similar scale' 已有但正文需统一\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"Downstream task collapse at ≥50% sparsity + 30% KL-global MMLU 异常 (25.27%)——实际有效操作点仅 ≤30% uniform\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 warning (W4)，R1 AGREE (W6 + cross-response)。缺 layer-wise budget 分析解释 30% global MMLU 异常。\"}\n    action_items:\n      - {round: 2, action: \"补充 30% global top-k 的 per-layer 实际保留率分布；在正文中显式讨论 recommended operating point (30% uniform)\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"12+ 处解释性 em-dash (---) 是 AI 写作信号\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 warning。R1 REBUT：em-dash 是合法标点，降为 info/stylistic suggestion。共识：减少频率即可。\"}\n    action_items:\n      - {round: 2, action: \"全文 grep '---' 和 ' -- '，将解释性 em-dash 替换为逗号或拆分句子\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"Gradient SNR (§3.6) 缺显式数学定义\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R1 列为 warning (W3)。R2 REBUT 降为 info：80 步覆盖关键区间，底层样本量足够，但定义确实应补。\"}\n    action_items:\n      - {round: 2, action: \"在 §3.6 添加 SNR 数学定义公式（如 SNR = E[g]²/Var[g]）\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"Reference count 偏低 (22 refs)——缺 MoE、Wanda、SparseGPT、sequence-level KD、Concrete distribution 等\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 info。R1 AGREE 并补充同样的缺失引用。升为 warning（两人一致）。\"}\n    action_items:\n      - {round: 2, action: \"补充引用：Wanda, SparseGPT, Switch Transformer/GShard, Kim&Rush 2016, DistilBERT, Louizos et al. 2018 (L0/Concrete)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规——当前为 conclusion 内 paragraph，ARR 要求独立 section*\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 交叉回应 AGREE。desk-reject 条件。\"}\n    action_items:\n      - {round: 1, action: \"将 \\\\paragraph{Limitations.} 拆为独立 \\\\section*{Limitations}\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 7018701: Limitations 拆为独立 section*，8p 正文确认合规\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限——正文含 Limitations/Future work 延伸至第 9 页，long paper 限 8 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 AGREE。\"}\n    action_items:\n      - {round: 1, action: \"拆出 Limitations 后编译确认页数\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"编译确认: main content 结束于 page 8, Limitations ARR exempt, 总 10p PDF\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"训练/评估数据同源（WikiText-103→WikiText-2），缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 critical。R2 AGREE with nuance。\"}\n    action_items:\n      - {round: 1, action: \"用已训练好的 predictor 在 C4 validation set 上评估 PPL（含 dense + TEAL baseline）\", assigned_to: \"main_agent\", status: done}\n    resolution: \"C4 validation (200 samples, streaming): Dense=9.21, KL 50%=18.40, TEAL 50%=38.75. KL 在 OOD 上保持 2.1× 优于 TEAL，相对优势泛化。\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"'Structural failure' 声明缺充分证据——BCE 仅测一个 configuration，对比不公平\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出 critical，R2 独立指出相同问题。\"}\n    action_items:\n      - {round: 1, action: \"BCE+Gumbel+Lagrangian ×3 LR (1e-4/1e-3/3e-3) 对照实验\", assigned_to: \"main_agent\", status: done}\n    resolution: \"Clean isolation 完成: BCE+Gumbel best PPL=38.02 (lr=3e-3) vs KL=11.79, 甚至比原始 BCE+STE (22.51) 更差。唯一变量是 loss function → structural mismatch confirmed。\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融实验缺关键维度——d_b sensitivity、温度 schedule、training curve、Lagrangian LR\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 列为 critical，R2 PARTIALLY AGREE。降为 warning。\"}\n    action_items:\n      - {round: 1, action: \"d_b={64,128,256,512} sensitivity sweep + training loss curve + λ curve\", assigned_to: \"main_agent\", status: done}\n    resolution: \"Appendix B: d_b sensitivity (<3% PPL range), B.1: τ schedule (<1.8% range), B.2: Training convergence (800 steps saturation), C: Lagrangian dynamics (λ trajectory table across 4 targets). All dimensions covered.\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"论文增加 6.4% 推理延迟，未实现 wall-clock 加速，与 abstract/intro framing 矛盾\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7，两人独立一致。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R2 spot-check 确认已修复。R1 仍有轻微顾虑但 R2 REBUT 认为文本分析不支持误导。\"}\n    action_items:\n      - {round: 1, action: \"Abstract/Intro reframe 为 prediction quality + inference simplification\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: 'accelerate'→'reduces effective computation', 'speedup'→'simplify inference', Appendix A caveat added. Round 2 confirmed fixed.\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Cross-architecture 验证仅 Mistral-7B 一个模型且仅 50% 一个点，泛化 claim 过强\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W2 = R2-W5，两人独立一致。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R2 spot-check 确认已修复。R1 AGREE scale limitation 仍在但 framing 已弱化。\"}\n    action_items:\n      - {round: 1, action: \"弱化措辞为 'preliminary evaluation on one additional model'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: 删除 'verify generality'/'transferability', 改为 'preliminary evaluation...suggests may generalize'. Round 2 confirmed.\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"新颖性有限——与 SPON 区分度不充分，核心技术为已知方法的新组合\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 列为 critical，R1 REBUT。降为 warning。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R2 spot-check 确认 SPON 区分已修复。但 novelty 整体仍存争议（见 R2-W1-Rd2）。\"}\n    action_items:\n      - {round: 1, action: \"更清晰 formalize per-token vs static KL 的差异\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: 明确 'closed-form static KL' vs 'end-to-end contextual KL with Gumbel-Sigmoid'. Round 2 SPON distinction confirmed.\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"遗漏重要相关工作 MaskLLM (Fang et al., NeurIPS 2024 Spotlight)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 强烈 AGREE。\"}\n      - {round: 2, reviewers: [2], note: \"R2 spot-check 确认已修复。\"}\n    action_items:\n      - {round: 1, action: \"Related Work 增加 MaskLLM 讨论并区分\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: MaskLLM added to Related Work + bib. Round 2 confirmed.\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 (§3.5) 是 informal argument，论文 oversell 为 theoretical contribution\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W4 ≈ R2-W3，两人独立一致。\"}\n      - {round: 2, reviewers: [1], note: \"R1 确认 framing 已修复为 'Gradient-Based Motivation'，SNR 5.76× 数据已添加。但 SNR 定义缺失仍为小问题（见 R1-W3-Rd2）。\"}\n    action_items:\n      - {round: 1, action: \"弱化为 'gradient-based motivation'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 1, action: \"添加实证 gradient SNR 数据 (KL/BCE=5.76×, early layers 34-156×)\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"§3.6 标题改为 'Gradient-Based Motivation'，framing 合理。SNR 5.76× 数据已添加。Round 2 R1 确认基本完成。\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"Lagrangian 对偶更新缺收敛分析——未报告 η_λ、λ 轨迹、实际 sparsity ratio 曲线\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出，R2 交叉 AGREE。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R1 列为 critical (W2)：Table 7 仅最终状态，缺时序曲线。R2 AGREE 但认为不影响核心结论。\"}\n    action_items:\n      - {round: 1, action: \"从训练 log 提取 λ 和 sparsity ratio over training steps 的曲线图，加入 Appendix\", assigned_to: \"main_agent\", status: in_progress}\n      - {round: 2, action: \"补充 Figure: 30%/50%/70% 的 (step, λ) 和 (step, actual_sparsity) 时序曲线\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W6\"\n    summary: \"2D taxonomy 作为 contribution 列出，但实为 post-hoc classification，贡献有限\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 部分 REBUT。\"}\n    action_items:\n      - {round: 1, action: \"降级为 organizational framework\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 7018701: contribution list 改为 'organize prior work via 2D framework'\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"三 seed (n=3) 统计效力弱\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出，R2 REBUT（ML 惯例可接受）。降为 info。\"}\n      - {round: 2, reviewers: [1, 2], note: \"R1 维持 warning；R2 AGREE 方向但指出 regime 分析不受影响（差异远大于 noise floor）。共识：对 global/uniform 对比影响有限。\"}\n    action_items:\n      - {round: 1, action: \"保持现状\", assigned_to: \"author\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型验证，边界是否随 scale 变化未知\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2-W5, R1 交叉 AGREE。\"}\n    action_items:\n      - {round: 1, action: \"加 caveat 承认 boundaries 是 model-specific\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Paper Agent commit 028bca6: §4.5 caveat added about boundaries being model-specific\"\n    resolution_round: 1\n\n  # Round 2 新发现\n  - id: \"R1-W1-Rd2\"\n    summary: \"'Lagrangian' 术语误用——实为 adaptive penalty method with deadzone + geometric schedule，非标准对偶方法\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R1 列为 critical W1，R2 独立提出 W6。交叉回应双方均 AGREE。两位 reviewer 独立一致。\"}\n    action_items:\n      - {round: 2, action: \"将 'Lagrangian' 改称 'adaptive penalty controller' 或 'adaptive penalty method'；讨论为何不用标准对偶上升及收敛保证缺失\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1-Rd2\"\n    summary: \"新颖性有限——KL distillation + Gumbel-Sigmoid + MLP predictor 是已知技术的可预期组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 critical。R1 REBUT：BCE+Gumbel 实验 (38.02>27.97) 证明组合非 trivial，gradient mismatch 诊断超越简单 combination。但同意 2D taxonomy framing 有填空嫌疑。分歧未解决。\"}\n    action_items:\n      - {round: 2, action: \"强化 'why non-trivial' 论证：(1) 突出 BCE+Gumbel 反效果作为 non-obvious evidence；(2) 弱化 2D taxonomy 的 contribution 权重\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"'相对优势随 sparsity 增长' claim 部分是 baseline (TEAL) 崩溃的假象，应同时报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 critical。R1 AGREE：(TEAL-KL)/TEAL inflate；应同时报告 KL/Dense ratio (1.47×/1.93×/2.93×)。\"}\n    action_items:\n      - {round: 2, action: \"Abstract 和 §4 同时报告 KL/Dense ratio；弱化 '18%→49%→82%' 的叙事依赖\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale limitation——仅 2 个 7-8B SwiGLU 模型，§4.6 'structural property of SwiGLU networks' claim 过强\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 提出 warning。R1 AGREE：§4.6 末句应加 'at 7-8B scale' 限定。\"}\n    action_items:\n      - {round: 2, action: \"§4.6 末句加 'at 7-8B scale' 限定；Abstract 'similar scale' 已有但正文需统一\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"Downstream task collapse at ≥50% sparsity + 30% KL-global MMLU 异常 (25.27%)——实际有效操作点仅 ≤30% uniform\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 warning (W4)，R1 AGREE (W6 + cross-response)。缺 layer-wise budget 分析解释 30% global MMLU 异常。\"}\n    action_items:\n      - {round: 2, action: \"补充 30% global top-k 的 per-layer 实际保留率分布；在正文中显式讨论 recommended operating point (30% uniform)\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"12+ 处解释性 em-dash (---) 是 AI 写作信号\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 warning。R1 REBUT：em-dash 是合法标点，降为 info/stylistic suggestion。共识：减少频率即可。\"}\n    action_items:\n      - {round: 2, action: \"全文 grep '---' 和 ' -- '，将解释性 em-dash 替换为逗号或拆分句子\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"Gradient SNR (§3.6) 缺显式数学定义\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R1 列为 warning (W3)。R2 REBUT 降为 info：80 步覆盖关键区间，底层样本量足够，但定义确实应补。\"}\n    action_items:\n      - {round: 2, action: \"在 §3.6 添加 SNR 数学定义公式（如 SNR = E[g]²/Var[g]）\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"Reference count 偏低 (22 refs)——缺 MoE、Wanda、SparseGPT、sequence-level KD、Concrete distribution 等\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R2 列为 info。R1 AGREE 并补充同样的缺失引用。升为 warning（两人一致）。\"}\n    action_items:\n      - {round: 2, action: \"补充引用：Wanda, SparseGPT, Switch Transformer/GShard, Kim&Rush 2016, DistilBERT, Louizos et al. 2018 (L0/Concrete)\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-17T04:56:24.359089+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 13536}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-17T04:57:44.767457+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "report": "# Round 2 审稿报告 — distill_sparse_swiglu → EMNLP 2026\n\n## Summary\n\n本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。Round 1 的多数 issues 已修复到位，但 Round 2 发现了新的方法学严谨性问题（术语误用）和 framing 问题（relative advantage inflation）。\n\n## Strengths\n\n- **核心结构论证有效**：BCE 梯度 factorize per-neuron（Eq. 8）导致无法学到 global top-k 所需的 inter-neuron coupling，这一诊断有理论支撑且通过 iso-compute saturation 和 BCE+Gumbel+Lagrangian (PPL 38.02 > vanilla BCE 27.97) 实证验证。\n- **消融设计系统且充分**：Table 3 隔离 loss function (ΔP=26.23) vs relaxation method (ΔP=3.98)，结论清晰。\n- **Regime 分析有实用价值**：budget-surplus / budget-constrained / capacity-limited 三分法对实践者有指导意义。\n- **Limitations 诚实**：明确承认无实际加速、仅 7-8B 模型、per-target 训练的限制。\n- **SPON 区分度充分**：cosine similarity 0.196 + PPL 分解定量展示两方法互补性。\n- **Round 1 修复到位**：12 个 Round 1 issues 中 9 个已完全 resolved，验证确认无退步。\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**1. [R1-W1-Rd2] \"Lagrangian\" 术语误用 [两位 Reviewer 独立一致, AGREE]**\n- Eq. 9 是带 deadzone 的二次惩罚项，Eq. 10 是几何倍增/减半 schedule。这既不是 augmented Lagrangian (需 λ←λ+α·g(x))，也不是对偶上升法。将其称为 \"Lagrangian\" 和 \"dual variable\" 存在术语误导。Penalty method 不保证满足 KKT 条件，论文未讨论收敛保证。\n- **修复方向**：改称 \"adaptive penalty controller\"；讨论为何选择启发式 schedule 而非标准对偶上升。\n\n### Should-Fix (Warning)\n\n**2. [R1-W5 / R1-W2-Rd2] λ/sparsity 时序曲线缺失 [两位 AGREE]**\n- Appendix C Table 7 仅报告最终状态。30% 和 70% target 的 λ hit cap (5000/1000) 暗示可能存在 boundary 震荡。缺少 (step, λ) 和 (step, actual_sparsity) 时序曲线。\"~10 步达到稳态\" 的 claim 无可视化证据。\n- **修复方向**：补充 3 个 target 的时序 figure。\n\n**3. [R2-W2-Rd2] \"相对优势随 sparsity 增长\" 是 baseline collapse artifact [R1 AGREE]**\n- (TEAL-KL)/TEAL 在 TEAL 崩溃时自动 inflate（18%→49%→82%）。应同时报告 KL/Dense ratio (1.47×→1.93×→2.93×) 以诚实反映 KL predictor 自身的退化曲线。\n- **修复方向**：Abstract 和 §4 同时报告 KL/Dense ratio。\n\n**4. [R2-W3-Rd2] Scale limitation 与 claim 不匹配 [R1 AGREE]**\n- 仅 2 个 7-8B 模型，§4.6 末句 \"structural property of SwiGLU networks\" 过强。\n- **修复方向**：加 \"at 7-8B scale\" 限定。\n\n**5. [R2-W4-Rd2] Downstream collapse + 30% MMLU 异常 [两位 AGREE]**\n- 50% 时 MMLU≈random；30% KL-global (25.27%) 比 TEAL (38.61%) 更差。实际有效操作点仅 ≤30% uniform。论文归因 \"global top-k starves layers\" 但缺 layer-wise 分析。\n- **修复方向**：补充 30% global 的 per-layer 保留率分布；正文显式推荐 30% uniform 为实际操作点。\n\n**6. [R2-W7-Rd2] Reference count 偏低 (22 refs) [两位 AGREE]**\n- 缺 Wanda, SparseGPT, Switch Transformer, Kim & Rush 2016, DistilBERT, Louizos et al. 2018 (L0/Concrete distribution)。EMNLP 典型 30-50 refs。\n- **修复方向**：补充上述引用并在 Related Work 中简要 positioning。\n\n### Nice-to-Fix (Info)\n\n**7. [R2-W5-Rd2] 12+ 处 em-dash 是 AI 写作信号 [R1 降为 info]**\n- R2 列为 warning，R1 REBUT 认为 em-dash 是合法标点，最多 info。共识：减少频率即可。\n\n**8. [R1-W3-Rd2] Gradient SNR 缺显式数学定义 [R2 降为 info]**\n- R1 列为 warning，R2 REBUT 认为上下文足以推断但应补定义。\n\n**9. [R1-W3] n=3 seeds 统计效力 [维持 info]**\n- 两位均认为对 regime 分析核心结论不构成威胁（差异远大于 noise floor），但 global/uniform PPL 差异 (0.17) 的显著性无法确认。\n\n## Reviewer Consensus [AGREE]\n\n1. **Lagrangian 术语误用** — 必须改称 adaptive penalty method (critical)\n2. **Relative advantage framing inflate** — 应加 KL/Dense ratio (warning)\n3. **Scale limitation** — §4.6 claim 过强 (warning)\n4. **30% MMLU 异常** — 缺 layer-wise 分析 (warning)\n5. **Reference count** — 偏低需补充 (warning)\n6. **λ/sparsity 曲线缺失** — Round 1 遗留未完全修复 (warning)\n\n## Reviewer Divergence [REBUT]\n\n**新颖性评估**：\n- **Reviewer 2** (critical): KL+Gumbel+MLP 是 \"predictable combination\"，novelty 不足以 main conference\n- **Reviewer 1** (REBUT): BCE+Gumbel 实验 (38.02>27.97) 证明组合非 trivial；gradient mismatch 诊断 + iso-compute verification 超越简单 combination；但同意 2D taxonomy framing 有 \"填空\" 嫌疑\n\nDirector 判断：novelty 处于 borderline。核心洞察（per-neuron factorization → global allocation failure）有分析深度，但论文 framing 过于依赖 \"filling a cell\"。如果强化 \"why non-trivial\" 的论证（突出反直觉的 BCE+Gumbel 反效果），novelty 勉强够 main conference。\n\n## Questions for Authors\n\n1. Eq. 10 几何倍增的收敛保证是什么？λ hit cap 后约束是否可精确满足？\n2. Gradient SNR 的精确数学定义？Over what dimensions (neurons/steps/sequences)?\n3. 30% KL-global MMLU 退化 40pp 的 layer-wise mechanism 是什么？\n4. BCE+Gumbel (no Lagrangian) 的 PPL 是多少？能否分离 Gumbel noise 的影响？\n5. Per-neuron prediction accuracy: KL predictor vs oracle top-k mask 的 F1 是多少？如果低于 BCE 但 PPL 更好，可强化 structural mismatch argument。\n\n## Missing References\n\n- Wanda (Sun et al., 2024) — magnitude-based pruning baseline\n- SparseGPT (Frantar & Alistarh, 2023) — one-shot structured pruning\n- Switch Transformer (Fedus et al., 2022) — conditional computation via routing\n- Kim & Rush (2016), \"Sequence-Level Knowledge Distillation\" — sequence-level KD\n- Sanh et al. (2019), \"DistilBERT\" — KD for language models\n- Louizos et al. (2018), \"Learning Sparse Neural Networks through L0 Regularization\" — Concrete/Gumbel-Sigmoid 标准引用\n- Maddison et al. (2017), \"The Concrete Distribution\" — binary relaxation 理论基础\n\n## External Review (Stanford Agentic Reviewer)\n\n状态：**已跳过 (skipped)**。未纳入本轮评估。\n\n## Overall Assessment\n\n**Score: Borderline (3.25/5)**\n\n论文执行扎实：核心 KL vs BCE 的结构性论证正确、消融充分、regime 分析有实用价值、Round 1 修复到位。但存在三个层面的问题：(1) 方法学严谨性——Lagrangian 术语误用和收敛曲线缺失；(2) framing 诚实性——relative advantage 部分是 baseline collapse artifact；(3) 实际 impact——有效操作点仅 ≤30%，gains 有限。\n\nnovelty 是核心分歧点：如果接受 gradient mismatch 诊断作为分析贡献，加上足够的修复，论文处于 main conference 下限。如果要求 novel algorithm 或 scaling evidence，更适合 Findings。\n\n**Recommendation**: 修复 Lagrangian 术语 + 补时序曲线 + reframe relative advantage 后，可达 **weak accept** 水平。当前版本 borderline，偏向 Findings。\n\n**Confidence: 4/5** — 两位 Reviewer 在关键问题上达成共识，唯一分歧（novelty）已充分辩论。\n\n## Detailed Comments\n\n### §3 Method\n- Eq. 9-10: 全文 \"Lagrangian\" → \"adaptive penalty controller\"，明确这是工程近似而非理论最优\n- §3.6: 补充 SNR 数学定义 (e.g., SNR_l = ||E[∂L/∂θ_l]||² / Var[∂L/∂θ_l])\n\n### §4 Experiments\n- Abstract/§4.2: 报告 (TEAL-KL)/TEAL 的同时，报告 KL/Dense ratio\n- §4.4/Table 2: 30% global MMLU 异常需 layer-wise budget 分析（哪些层被 starved）\n- §4.6 末句: \"structural property of SwiGLU networks\" → \"structural property of SwiGLU networks at the 7-8B scale tested\"\n\n### Appendix\n- Appendix C: 补充 (step, λ) 和 (step, actual_sparsity) 时序 figure（至少 30%/50%/70%）\n\n### Related Work & References\n- 补充 6-8 篇关键引用（见 Missing References）\n- 增加 conditional computation (MoE) 段落\n\n### Writing\n- 全文 grep `---` 和 ` -- `，将解释性 em-dash 替换为逗号或拆分句子（目标：≤3 处）",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "report": "# Round 2 审稿报告 — distill_sparse_swiglu → EMNLP 2026\n\n## Summary\n\n本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。Round 1 的多数 issues 已修复到位，但 Round 2 发现了新的方法学严谨性问题（术语误用）和 framing 问题（relative advantage inflation）。\n\n## Strengths\n\n- **核心结构论证有效**：BCE 梯度 factorize per-neuron（Eq. 8）导致无法学到 global top-k 所需的 inter-neuron coupling，这一诊断有理论支撑且通过 iso-compute saturation 和 BCE+Gumbel+Lagrangian (PPL 38.02 > vanilla BCE 27.97) 实证验证。\n- **消融设计系统且充分**：Table 3 隔离 loss function (ΔP=26.23) vs relaxation method (ΔP=3.98)，结论清晰。\n- **Regime 分析有实用价值**：budget-surplus / budget-constrained / capacity-limited 三分法对实践者有指导意义。\n- **Limitations 诚实**：明确承认无实际加速、仅 7-8B 模型、per-target 训练的限制。\n- **SPON 区分度充分**：cosine similarity 0.196 + PPL 分解定量展示两方法互补性。\n- **Round 1 修复到位**：12 个 Round 1 issues 中 9 个已完全 resolved，验证确认无退步。\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**1. [R1-W1-Rd2] \"Lagrangian\" 术语误用 [两位 Reviewer 独立一致, AGREE]**\n- Eq. 9 是带 deadzone 的二次惩罚项，Eq. 10 是几何倍增/减半 schedule。这既不是 augmented Lagrangian (需 λ←λ+α·g(x))，也不是对偶上升法。将其称为 \"Lagrangian\" 和 \"dual variable\" 存在术语误导。Penalty method 不保证满足 KKT 条件，论文未讨论收敛保证。\n- **修复方向**：改称 \"adaptive penalty controller\"；讨论为何选择启发式 schedule 而非标准对偶上升。\n\n### Should-Fix (Warning)\n\n**2. [R1-W5 / R1-W2-Rd2] λ/sparsity 时序曲线缺失 [两位 AGREE]**\n- Appendix C Table 7 仅报告最终状态。30% 和 70% target 的 λ hit cap (5000/1000) 暗示可能存在 boundary 震荡。缺少 (step, λ) 和 (step, actual_sparsity) 时序曲线。\"~10 步达到稳态\" 的 claim 无可视化证据。\n- **修复方向**：补充 3 个 target 的时序 figure。\n\n**3. [R2-W2-Rd2] \"相对优势随 sparsity 增长\" 是 baseline collapse artifact [R1 AGREE]**\n- (TEAL-KL)/TEAL 在 TEAL 崩溃时自动 inflate（18%→49%→82%）。应同时报告 KL/Dense ratio (1.47×→1.93×→2.93×) 以诚实反映 KL predictor 自身的退化曲线。\n- **修复方向**：Abstract 和 §4 同时报告 KL/Dense ratio。\n\n**4. [R2-W3-Rd2] Scale limitation 与 claim 不匹配 [R1 AGREE]**\n- 仅 2 个 7-8B 模型，§4.6 末句 \"structural property of SwiGLU networks\" 过强。\n- **修复方向**：加 \"at 7-8B scale\" 限定。\n\n**5. [R2-W4-Rd2] Downstream collapse + 30% MMLU 异常 [两位 AGREE]**\n- 50% 时 MMLU≈random；30% KL-global (25.27%) 比 TEAL (38.61%) 更差。实际有效操作点仅 ≤30% uniform。论文归因 \"global top-k starves layers\" 但缺 layer-wise 分析。\n- **修复方向**：补充 30% global 的 per-layer 保留率分布；正文显式推荐 30% uniform 为实际操作点。\n\n**6. [R2-W7-Rd2] Reference count 偏低 (22 refs) [两位 AGREE]**\n- 缺 Wanda, SparseGPT, Switch Transformer, Kim & Rush 2016, DistilBERT, Louizos et al. 2018 (L0/Concrete distribution)。EMNLP 典型 30-50 refs。\n- **修复方向**：补充上述引用并在 Related Work 中简要 positioning。\n\n### Nice-to-Fix (Info)\n\n**7. [R2-W5-Rd2] 12+ 处 em-dash 是 AI 写作信号 [R1 降为 info]**\n- R2 列为 warning，R1 REBUT 认为 em-dash 是合法标点，最多 info。共识：减少频率即可。\n\n**8. [R1-W3-Rd2] Gradient SNR 缺显式数学定义 [R2 降为 info]**\n- R1 列为 warning，R2 REBUT 认为上下文足以推断但应补定义。\n\n**9. [R1-W3] n=3 seeds 统计效力 [维持 info]**\n- 两位均认为对 regime 分析核心结论不构成威胁（差异远大于 noise floor），但 global/uniform PPL 差异 (0.17) 的显著性无法确认。\n\n## Reviewer Consensus [AGREE]\n\n1. **Lagrangian 术语误用** — 必须改称 adaptive penalty method (critical)\n2. **Relative advantage framing inflate** — 应加 KL/Dense ratio (warning)\n3. **Scale limitation** — §4.6 claim 过强 (warning)\n4. **30% MMLU 异常** — 缺 layer-wise 分析 (warning)\n5. **Reference count** — 偏低需补充 (warning)\n6. **λ/sparsity 曲线缺失** — Round 1 遗留未完全修复 (warning)\n\n## Reviewer Divergence [REBUT]\n\n**新颖性评估**：\n- **Reviewer 2** (critical): KL+Gumbel+MLP 是 \"predictable combination\"，novelty 不足以 main conference\n- **Reviewer 1** (REBUT): BCE+Gumbel 实验 (38.02>27.97) 证明组合非 trivial；gradient mismatch 诊断 + iso-compute verification 超越简单 combination；但同意 2D taxonomy framing 有 \"填空\" 嫌疑\n\nDirector 判断：novelty 处于 borderline。核心洞察（per-neuron factorization → global allocation failure）有分析深度，但论文 framing 过于依赖 \"filling a cell\"。如果强化 \"why non-trivial\" 的论证（突出反直觉的 BCE+Gumbel 反效果），novelty 勉强够 main conference。\n\n## Questions for Authors\n\n1. Eq. 10 几何倍增的收敛保证是什么？λ hit cap 后约束是否可精确满足？\n2. Gradient SNR 的精确数学定义？Over what dimensions (neurons/steps/sequences)?\n3. 30% KL-global MMLU 退化 40pp 的 layer-wise mechanism 是什么？\n4. BCE+Gumbel (no Lagrangian) 的 PPL 是多少？能否分离 Gumbel noise 的影响？\n5. Per-neuron prediction accuracy: KL predictor vs oracle top-k mask 的 F1 是多少？如果低于 BCE 但 PPL 更好，可强化 structural mismatch argument。\n\n## Missing References\n\n- Wanda (Sun et al., 2024) — magnitude-based pruning baseline\n- SparseGPT (Frantar & Alistarh, 2023) — one-shot structured pruning\n- Switch Transformer (Fedus et al., 2022) — conditional computation via routing\n- Kim & Rush (2016), \"Sequence-Level Knowledge Distillation\" — sequence-level KD\n- Sanh et al. (2019), \"DistilBERT\" — KD for language models\n- Louizos et al. (2018), \"Learning Sparse Neural Networks through L0 Regularization\" — Concrete/Gumbel-Sigmoid 标准引用\n- Maddison et al. (2017), \"The Concrete Distribution\" — binary relaxation 理论基础\n\n## External Review (Stanford Agentic Reviewer)\n\n状态：**已跳过 (skipped)**。未纳入本轮评估。\n\n## Overall Assessment\n\n**Score: Borderline (3.25/5)**\n\n论文执行扎实：核心 KL vs BCE 的结构性论证正确、消融充分、regime 分析有实用价值、Round 1 修复到位。但存在三个层面的问题：(1) 方法学严谨性——Lagrangian 术语误用和收敛曲线缺失；(2) framing 诚实性——relative advantage 部分是 baseline collapse artifact；(3) 实际 impact——有效操作点仅 ≤30%，gains 有限。\n\nnovelty 是核心分歧点：如果接受 gradient mismatch 诊断作为分析贡献，加上足够的修复，论文处于 main conference 下限。如果要求 novel algorithm 或 scaling evidence，更适合 Findings。\n\n**Recommendation**: 修复 Lagrangian 术语 + 补时序曲线 + reframe relative advantage 后，可达 **weak accept** 水平。当前版本 borderline，偏向 Findings。\n\n**Confidence: 4/5** — 两位 Reviewer 在关键问题上达成共识，唯一分歧（novelty）已充分辩论。\n\n## Detailed Comments\n\n### §3 Method\n- Eq. 9-10: 全文 \"Lagrangian\" → \"adaptive penalty controller\"，明确这是工程近似而非理论最优\n- §3.6: 补充 SNR 数学定义 (e.g., SNR_l = ||E[∂L/∂θ_l]||² / Var[∂L/∂θ_l])\n\n### §4 Experiments\n- Abstract/§4.2: 报告 (TEAL-KL)/TEAL 的同时，报告 KL/Dense ratio\n- §4.4/Table 2: 30% global MMLU 异常需 layer-wise budget 分析（哪些层被 starved）\n- §4.6 末句: \"structural property of SwiGLU networks\" → \"structural property of SwiGLU networks at the 7-8B scale tested\"\n\n### Appendix\n- Appendix C: 补充 (step, λ) 和 (step, actual_sparsity) 时序 figure（至少 30%/50%/70%）\n\n### Related Work & References\n- 补充 6-8 篇关键引用（见 Missing References）\n- 增加 conditional computation (MoE) 段落\n\n### Writing\n- 全文 grep `---` 和 ` -- `，将解释性 em-dash 替换为逗号或拆分句子（目标：≤3 处）",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-17T04:57:48.846722+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4079
}
```

</details>

---


### Assistant

_source line 200 · 2026-05-17T04:57:59.976108+00:00_

Round 2 审稿完成。

**最终评分：Borderline (3.25/5)**

审稿报告已投递给 Research Director。核心发现：

| 优先级 | Issue | 状态 |
|--------|-------|------|
| Must-Fix | "Lagrangian" 术语误用 → adaptive penalty method | 两人一致 |
| Should-Fix | λ/sparsity 时序曲线（R1 遗留） | 两人一致 |
| Should-Fix | Relative advantage inflation → 加 KL/Dense ratio | 两人一致 |
| Should-Fix | §4.6 scale claim 过强 | 两人一致 |
| Should-Fix | 30% MMLU 异常缺 layer-wise 分析 | 两人一致 |
| Should-Fix | Reference count 偏低 (22→30+) | 两人一致 |
| 分歧 | Novelty 评估（R1: borderline main / R2: Findings） | 未收敛 |

修复 Lagrangian 术语 + 补时序曲线 + reframe relative advantage 后可升至 weak accept。当前版本偏向 Findings of EMNLP。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 201 · 2026-05-17T04:58:02.509864+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 Reviewer 1 的 6 条 Weakness：AGREE 4 条（W1/W2/W4/W6），REBUT 2 条（W3 降级为 info、W5 论文已修复）。两位 reviewer 的共识集中在 Lagrangian 术语误用和 30% MMLU 异常缺乏 layer-wise 解释。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 202 · 2026-05-17T04:58:12.935096+00:00_

Round 2 圆桌审稿已完成。审稿报告已投递给 Research Director。

**最终评分：Borderline (3.25/5)**

核心结论：
- **Must-Fix**: Lagrangian 术语误用（改称 adaptive penalty method）
- **Should-Fix**: λ/sparsity 时序曲线、relative advantage reframe、scale claim 限定、30% MMLU layer-wise 分析、补充 6-8 篇引用
- **分歧**: novelty 评估（R1: 3.5 borderline main vs R2: 3.0 Findings），已如实记录

修复上述问题后可达 weak accept 水平。当前版本偏向 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 19

## Round 19

54 recorded events


### User

_source line 203 · 2026-05-17T08:08:10.567393+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-17T08:08:16.908217+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-17T08:08:16.959556+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-17T08:08:20.778647+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-17T08:08:20.829442+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-17T08:08:25.155559+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,request_external_review,get_external_review_status,read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,request_external_review,get_external_review_status,read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-17T08:08:25.258193+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-17T08:08:29.078205+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-17T08:08:29.179208+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-17T08:08:32.548206+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-17T08:08:32.899610+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-17T08:08:33.204036+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (104 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 今日完成的分析任务（全部 success 或 negative，已写入 paper）\n\n| exp_id | 结论 | 关键发现 |\n|--------|------|---------|\n| kl_bce_f1_oracle | success | BCE F1=0.613 > KL F1=0.540，但 KL PPL=11.79 远优于 BCE PPL=22.51。证明 per-neuron mask accuracy 是错误优化目标 |\n| global_30pct_retention | negative | 30% 全局 top-k 饿死 late layers (L27-31)，L31 仅 28.4% retention。原 hypothesis \"中层知识层挨饿\" 被推翻 |\n| global_50pct_retention | success | 50% 下 late layers retention 降至 0.342，knowledge layers (L12-20) 保持 0.606，确认全局分配优先喂中层 |\n| global_70pct_retention | success | 70% 下 starvation 扩散到 L10-L12（min=0.167），相变：全局分配无法同时保护中层和早期层 |\n| reverse_kl_50pct_s42 | negative | PPL=12.8 vs Forward KL=11.79（+8.6%），Forward KL 仍最优 |\n| jsd_50pct_s42 | negative | PPL=12.54 vs Forward KL=11.79（+6.4%），Forward KL 仍最优 |\n| gradient_snr_constrained | success | 带 Lagrangian 约束下 KL SNR 仍 103.2× > BCE，直接回应 R1-W5 |\n| lagrangian_dynamics_fix | success | 重新生成完整 1000-step Lagrangian 动态图（50% 数据修复） |\n| teal_kl_overlap_corrected | success | 排列检验 z=7260，确认 TEAL-KL 重叠非随机（回应选择偏差） |\n| natural_sparsity_floor_extended | success | 30/50/70% 三级自然稀疏下限分析完成 |\n\n## 产出物（已同步/待同步到本地）\n- `figures/paper/lagrangian_dynamics.pdf` — 已同步\n- `figures/paper/per_layer_retention_
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 655
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-17T08:08:42.198864+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view
…[truncated 1649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 9299
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-17T08:08:46.396648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit template ACL rolling review ARR guidelines",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 paper format page limit template ACL rolling review ARR guidelines",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-17T08:08:48.254376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-17T08:08:48.254837+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-17T08:08:52.821343+00:00_

Web search results for query: "EMNLP 2026 paper format page limit template ACL rolling review ARR guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on my search results, here's what I found about EMNLP 2026 paper format, page limits, template, and ACL Rolling Review guidelines:

## EMNLP 2026 and ARR

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but fin
…[truncated 1171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6424
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-17T08:08:57.238912+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL rolling review 2026 long paper short paper page limit 8 pages 4 pages format",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL rolling review 2026 long paper short paper page limit 8 pages 4 pages format",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-17T08:08:57.992207+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-17T08:08:58.042952+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology_6e294a.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/related_work_c10e4f.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-17T08:09:02.062574+00:00_

Web search results for query: "ACL rolling review 2026 long paper short paper page limit 8 pages 4 pages format"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here's the information about ACL Rolling Review 2026 page limits and format:

## Paper Formats and Page Limits


…[truncated 706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 4823
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-17T08:09:10.961926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-17T08:09:11.464340+00:00_

1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\% (PPL 17.91 vs.\ 100.11); KL itself incurs $2.93\times$ the dense baseline, demonstrating substantial output fidelity even at extreme sparsity.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes (budget-surplus, budget-constrained, and capacity-limited) that govern the quality-sparsity tradeoff.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-17T08:09:11.514960+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-17T08:09:11.917496+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can simplify inference by pruning 50\% of FFN neurons per token (without modifying the pretrained weights), eliminating the need for auxiliary compensation networks.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This creates a structural mi
…[truncated 4883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-17T08:09:12.018219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-17T08:09:12.018748+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 13358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-17T08:09:16.606601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-17T08:09:17.109302+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$ and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	
…[truncated 12662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-17T08:09:17.109669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-17T08:09:17.160206+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.
14	In contrast, our method learns \emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.
15	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
16	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.
…[truncated 2049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-17T08:09:22.382062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-17T08:09:22.784404+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Training sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.
5	The resulting predictor (75.9M params, $<$1\% of base) achieves PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, transfers across SwiGLU architectures at the 7--8B parameter scale (within 7\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-17T08:09:22.935438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-17T08:09:23.086407+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
7	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-17T08:09:23.086762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-17T08:09:23.137345+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 8907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-17T08:09:31.622165+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-17T08:09:32.576723+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 47\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 C
…[truncated 1457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-17T08:09:32.627584+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-17T08:09:32.628297+00:00_

1	issues:
2	  - id: "R2-N1"
3	    summary: "Limitations section 格式不合规"
4	    category: format
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - {round: 1, reviewers: [1, 2], note: "desk-reject 条件"}
11	    action_items:
12	      - {round: 1, action: "拆为独立 section*", assigned_to: "paper_agent", status: done}
13	    resolution: "Commit 7018701"
14	    resolution_round: 1
15	
16	  - id: "R2-N2"
17	    summary: "页数超限"
18	    category: format
19	    severity: critical
20	    status: resolved
21	    first_raised_round: 1
22	    last_seen_round: 1
23	    mentions:
24	      - {round: 1, reviewers: [1, 2], note: "R2 提出，R1 AGREE"}
25	    action_items:
26	      - {round: 1, action: "拆出 Limitations 后确认页数", assigned_to: "paper_agent", status: done}
27	    resolution: "Main content p.8, total 10p"
28	    resolution_round: 1
29	
30	  - id: "R1-N1"
31	    summary: "缺 OOD PPL 评估"
32	    category: experiment
33	    severity: critical
34	    status: resolved
35	    first_raised_round: 1
36	    last_seen_round: 1
37	    mentions:
38	      - {round: 1, reviewers: [1, 2], note: "R1 critical, R2 AGREE"}
39	    action_items:
40	      - {round: 1, action: "C4 validation PPL", assigned_to: "main_agent", status: done}
41	    resolution: "C4: Dense=9.21, KL 50%=18.40, TEAL 50%=38.75"
42	    resolution_round: 1
43	
44	  - id: "R1-N2"
45	    summary: "Structural failure 证据不足"
46	    category: method
47	    severity: critical
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    mentions:
52	      - {round: 1, reviewers: [1, 2], note: "两位独立指出"}
53	    action_items:
54	      - {round: 1, action: "BCE+Gumbel ×3 LR 对照", assigned_to: "main_agent", status: done}
55	    resolution: "BCE best=38.02 vs KL=11.79"
56	    resolution_round: 1
57	
58	  - id: "R1-N3"
59	    summary: "消融缺关键维度"
60	    category: experiment
61	    severity: warning
62	    status: resolved
63	    first_raised_round: 1
64	   
…[truncated 7152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-17T08:09:39.816106+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-17T08:09:40.572045+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-17T08:09:40.723106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-17T08:09:40.723588+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2026},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-17T08:09:44.283206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
  "offset": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
    "offset": "50"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-17T08:09:44.341042+00:00_

50	  year = {2025},
51	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
52	  url = {https://arxiv.org/abs/2408.14690},
53	}
54	
55	@inproceedings{liu2023dejavu,
56	  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},
57	  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},
58	  year = {2023},
59	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
60	  url = {https://arxiv.org/abs/2310.17157},
61	}
62	
63	@inproceedings{akhauri2024shadowllm,
64	  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},
65	  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},
66	  year = {2024},
67	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
68	  url = {https://arxiv.org/abs/2406.16635},
69	}
70	
71	
72	@article{lee2024cats,
73	  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},
74	  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},
75	  year = {2024},
76	  journal = {arXiv preprint arXiv:2404.08763},
77	  url = {https://arxiv.org/abs/2404.08763},
78	}
79	
80	@inproceedings{zhang2025rsparse,
81	  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},
82	  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},
83	  year = {2025},
84	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
85	  url = {https://arxiv.org/abs/2504.19449},
86	}
87	
88	@inproceedings{federici2025dip,
89	  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking
…[truncated 9575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 57
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-17T08:10:24.445484+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-17T08:10:24.445966+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-17T08:10:49.624538+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你负责**方法严谨性 + 实验有效性**的审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix\n- **模板**: ACL format with `[review]` option\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，reviewer 可选择性阅读\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n## 你的审查侧重\n\n1. **方法正确性**：\n   - KL 梯度分析（Eq. 7-8）是否数学上严格？factor (a)-(d) 的分解是否完整？\n   - Gumbel-Sigmoid relaxation 的使用是否正确？与标准 Concrete distribution 的关系是否清晰？\n   - Adaptive penalty controller (Eq. 5-6) 的收敛保证——论文称其为 \"adaptive penalty controller\" 而非 Lagrangian，这个表述是否准确？multiplicative schedule 是否有理论支撑？\n   - BCE vs KL structural mismatch argument 是否有逻辑漏洞？\n\n2. **实验有效性**：\n   - 主实验对比是否公平？KL 和 BCE 的计算量对比（1000 vs 2700 steps）是否充分说明 structural failure？\n   - 消融实验是否覆盖所有关键设计选择？是否有遗漏的 confounding factors？\n   - 三 seed 统计（PPL 11.92±0.07）——3 seeds 的统计效力是否足够？\n   - Cross-architecture evaluation (Mistral-7B) 是否充分验证 generalization？仅两个 7-8B 模型是否足够？\n   - OOD evaluation (C4) 是否足够？训练和评估都在 WikiText 系列上是否存在 data leakage concern？\n   - Downstream task collapse（MMLU/GSM8K 在 50% 时 ≈ random）——这是否 undermines the practical value？\n\n3. **可重复性**：\n   - 超参数是否充分报告？\n   - 训练细节（WikiText-103, 1000 steps, batch=4, seq=2048）是否足够 reproduce？\n   - Inference protocol（predictor-TEAL）是否描述清晰？\n\n4. **Latency claim**：\n   - 论文声称 6.4% overhead 但目前没有 wall-clock speedup——这对一篇 efficiency-motivated paper 意味着什么？\n   - \"eliminates compensation network\" 节省 2.7% latency，但 predictor 本身加 6.4%——净效果是增加 overhead，这与 paper framing 是否矛盾？\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Soundness (1-5) → Overall (1-5)",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你负责**方法严谨性 + 实验有效性**的审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix\n- **模板**: ACL format with `[review]` option\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，reviewer 可选择性阅读\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n## 你的审查侧重\n\n1. **方法正确性**：\n   - KL 梯度分析（Eq. 7-8）是否数学上严格？factor (a)-(d) 的分解是否完整？\n   - Gumbel-Sigmoid relaxation 的使用是否正确？与标准 Concrete distribution 的关系是否清晰？\n   - Adaptive penalty controller (Eq. 5-6) 的收敛保证——论文称其为 \"adaptive penalty controller\" 而非 Lagrangian，这个表述是否准确？multiplicative schedule 是否有理论支撑？\n   - BCE vs KL structural mismatch argument 是否有逻辑漏洞？\n\n2. **实验有效性**：\n   - 主实验对比是否公平？KL 和 BCE 的计算量对比（1000 vs 2700 steps）是否充分说明 structural failure？\n   - 消融实验是否覆盖所有关键设计选择？是否有遗漏的 confounding factors？\n   - 三 seed 统计（PPL 11.92±0.07）——3 seeds 的统计效力是否足够？\n   - Cross-architecture evaluation (Mistral-7B) 是否充分验证 generalization？仅两个 7-8B 模型是否足够？\n   - OOD evaluation (C4) 是否足够？训练和评估都在 WikiText 系列上是否存在 data leakage concern？\n   - Downstream task collapse（MMLU/GSM8K 在 50% 时 ≈ random）——这是否 undermines the practical value？\n\n3. **可重复性**：\n   - 超参数是否充分报告？\n   - 训练细节（WikiText-103, 1000 steps, batch=4, seq=2048）是否足够 reproduce？\n   - Inference protocol（predictor-TEAL）是否描述清晰？\n\n4. **Latency claim**：\n   - 论文声称 6.4% overhead 但目前没有 wall-clock speedup——这对一篇 efficiency-motivated paper 意味着什么？\n   - \"eliminates compensation network\" 节省 2.7% latency，但 predictor 本身加 6.4%——净效果是增加 overhead，这与 paper framing 是否矛盾？\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Soundness (1-5) → Overall (1-5)",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-17T08:11:10.222223+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20597
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-17T08:11:10.674541+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你负责**新颖性 + 完整性**的审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix\n- **模板**: ACL format with `[review]` option\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，reviewer 可选择性阅读\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n## 你的审查侧重\n\n1. **新颖性评估**：\n   - 核心贡献（KL distillation for sparsity prediction）的技术新颖性——KL distillation 本身是标准技术，Gumbel relaxation 也是已有方法，组合是否构成足够的 novelty？\n   - 2D taxonomy（correction granularity × training signal coupling）是否提供真正的 insight，还是事后合理化？\n   - \"structural mismatch\" argument 是否是真正的新洞察？BCE 的局限性在 prior work 中是否已被讨论？\n   - 与 MaskLLM (Fang et al. 2024) 的区别是否充分？MaskLLM 也用 Gumbel + KL + frozen weights，区别仅在 activation vs weight sparsity？\n   - 与 SPON (Xu et al. 2026) 的区别——SPON 也用 KL training，区别仅在 static vs per-token？\n\n2. **Related Work 完整性**：\n   - 引用是否覆盖所有直接相关方法？（31 refs）\n   - 是否遗漏重要的 recent work？特别是 2025-2026 年的 activation sparsity 文献\n   - Positioning 是否公平？是否有 strawman 嫌疑（如 BCE baseline 的设置是否对 BCE 不公平）？\n\n3. **叙事质量与 Framing**：\n   - Abstract 是否在 30s 内传达核心价值？\n   - Introduction 的叙事线是否连贯？从 problem → insight → method → results 是否流畅？\n   - \"eliminates compensation networks\" 是核心 selling point，但实际没有 speedup——framing 是否 misleading？\n   - 论文标题 \"Output-Distribution Distillation for Contextual Sparsity Prediction\" 是否准确反映贡献？\n   - Three regime analysis 是 contribution 之一，但证据仅来自 2 个模型 × 3 个 sparsity levels——claim 的强度是否与证据匹配？\n\n4. **格式合规**：\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否独立存在（ARR 要求）？\n   - 是否有 Ethics Statement / Responsible NLP Checklist？（ARR 要求）\n   - 引用格式是否正确（natbib）？\n   - 图表 caption 是否自包含？\n   - AI 写作痕迹检查：em-dash、-ing phrases、过度分段\n\n5. **Missing References 检查**：\n   - 用你的知识检查是否遗漏了 2024-2026 年的关键 activation sparsity 论文\n   - 特别关注：Griffin (DeepMind 2024)、Mixture of Depths、any EMNLP 2025 sparsity papers\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Novelty (1-5) → Overall (1-5)",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你负责**新颖性 + 完整性**的审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix\n- **模板**: ACL format with `[review]` option\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，reviewer 可选择性阅读\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n## 你的审查侧重\n\n1. **新颖性评估**：\n   - 核心贡献（KL distillation for sparsity prediction）的技术新颖性——KL distillation 本身是标准技术，Gumbel relaxation 也是已有方法，组合是否构成足够的 novelty？\n   - 2D taxonomy（correction granularity × training signal coupling）是否提供真正的 insight，还是事后合理化？\n   - \"structural mismatch\" argument 是否是真正的新洞察？BCE 的局限性在 prior work 中是否已被讨论？\n   - 与 MaskLLM (Fang et al. 2024) 的区别是否充分？MaskLLM 也用 Gumbel + KL + frozen weights，区别仅在 activation vs weight sparsity？\n   - 与 SPON (Xu et al. 2026) 的区别——SPON 也用 KL training，区别仅在 static vs per-token？\n\n2. **Related Work 完整性**：\n   - 引用是否覆盖所有直接相关方法？（31 refs）\n   - 是否遗漏重要的 recent work？特别是 2025-2026 年的 activation sparsity 文献\n   - Positioning 是否公平？是否有 strawman 嫌疑（如 BCE baseline 的设置是否对 BCE 不公平）？\n\n3. **叙事质量与 Framing**：\n   - Abstract 是否在 30s 内传达核心价值？\n   - Introduction 的叙事线是否连贯？从 problem → insight → method → results 是否流畅？\n   - \"eliminates compensation networks\" 是核心 selling point，但实际没有 speedup——framing 是否 misleading？\n   - 论文标题 \"Output-Distribution Distillation for Contextual Sparsity Prediction\" 是否准确反映贡献？\n   - Three regime analysis 是 contribution 之一，但证据仅来自 2 个模型 × 3 个 sparsity levels——claim 的强度是否与证据匹配？\n\n4. **格式合规**：\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否独立存在（ARR 要求）？\n   - 是否有 Ethics Statement / Responsible NLP Checklist？（ARR 要求）\n   - 引用格式是否正确（natbib）？\n   - 图表 caption 是否自包含？\n   - AI 写作痕迹检查：em-dash、-ing phrases、过度分段\n\n5. **Missing References 检查**：\n   - 用你的知识检查是否遗漏了 2024-2026 年的关键 activation sparsity 论文\n   - 特别关注：Griffin (DeepMind 2024)、Mixture of Depths、any EMNLP 2025 sparsity papers\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Novelty (1-5) → Overall (1-5)",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-17T08:11:12.033219+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1358
}
```

</details>

---


### Assistant

_source line 256 · 2026-05-17T08:11:16.509223+00:00_

Round 1 任务已分配给两位 Reviewer：

- **Reviewer 1** → 方法严谨性 + 实验有效性（梯度分析、消融、统计、latency claim）
- **Reviewer 2** → 新颖性 + 完整性（novelty、related work、叙事质量、格式合规）

等待两位 Reviewer 返回独立审稿意见后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 257 · 2026-05-17T08:18:03.266476+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

## Paper Summary

本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 activation sparsity predictor。核心论点是 BCE 梯度按 neuron 分解（Eq. 7: ∂L/∂s_j = σ(s_j) − m_j*），与推理时 TEAL 的 global top-k allocation 存在"结构性不匹配"；KL 梯度通过下游 Jacobian（factor (b)）耦合所有 neuron。方法使用 Gumbel-Sigmoid relaxation 实现可微训练，adaptive penalty controller 控制稀疏度。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 11.79 vs TEAL 的 23.31（无 compensation network）。跨架构验证于 Mistral-7B-v0.3。提出 correction granularity × training signal coupling 的 2D taxonomy，识别三种 sparsity regime。

---

## Summary of Strengths

**S1. 清晰的理论洞察与形式化。** §3.5 的梯度分析是本文最强贡献。Factor (a)-(d) 分解清楚说明了 KL 和 BCE 的结构性差异：factor (b) 的 Jacobian ∂z/∂h^(ℓ) 使 KL 梯度依赖所有下游层的 mask 状态，而 BCE 的 Eq. 7 只依赖 neuron j 自身。这个观察数学上严格，且有直接的实证支撑。

**S2. Oracle F1 分析揭示 proxy mismatch 的深度（§4.2）。** BCE 达到 F1=0.613（比 KL 的 0.540 高 +13pp）但 PPL 差 91%；KL 的 near-random precision (0.51) 表明它学到的 mask 与 magnitude oracle 完全不同，优化的是 distributional fidelity 而非 magnitude matching。这是全文最有说服力的实验证据，直接支撑了"正确目标 > 高精度代理"的核心论点。

**S3. 消融设计覆盖关键设计选择。** Table 3 系统覆盖：loss direction（Forward KL vs JSD vs Reverse KL）、relaxation（Gumbel vs STE, Δ=3.98）、compensation 效果、以及关键的 isolation 实验（BCE + Gumbel + Penalty = 38.02，证明 penalty 框架本身不提供增益）。Loss effect (ΔPPL=26.23) 是 relaxation effect (ΔPPL=3.98) 的 6.6×，清晰分离了各组件贡献。

**S4. 2D taxonomy 和 regime 分析有组织价值。** Table 1 的 correction granularity × training signal coupling 分类法简洁有效地定位了本文在文献中的位置。三 regime 分析（budget-surplus / budget-constrained / capacity-limited）发现 allocation preference 的非单调性（30% 偏好 uniform，40% 偏好 global，50% 无差异）是有意义的实证发现。

**S5. SPON 正交性分析（§4.5）。** Cosine similarity 0.196 + 仅 2.4% PPL 改善的定量分解说明 KL predictor 已捕获大部分可恢复信号，static correction 与 learned prediction 接近正交，这对未来工作有指导意义。

---

## Summary of Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 论文以 efficiency 为动机，但实际无 wall-clock speedup，且 framing 产生误导。**
- 具体位置：§1 ("simplify inference by pruning 50% of FFN neurons"), §4.6 ("eliminates the compensation network, −2.7% latency"), Appendix A (Table 6)
- 问题：Table 6 (Appendix A) 显示 KL predictor-only 在 50% sparsity 下为 126.78ms（dense 119.11ms），overhead = +6.4%。消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。与 compensation-based 方法相比净效果是 +6.4% vs +8.9%——仅节省 2.5pp overhead，且两者都比 dense 慢。更关键的是，unstructured element-wise mask 不产生任何 sparse computation speedup，论文自己在 Appendix A 和 Limitations 中承认 "net acceleration requires kernel-level sparse computation optimizations"。
- 为什么影响接收：论文 Introduction 的 framing 暗示 "simplify inference" 和 "eliminating compensation" 带来效率增益。但实际效果是：(1) 比 dense 慢 6.4%；(2) 比有 compensation 的方案快 2.5pp 但仍然更慢。一篇以 sparsity prediction 为核心的论文，在没有任何实际加速的情况下，需要将 framing 从 "efficiency" 调整为 "prediction quality / understanding"。
- 建议修改方向：重新定位论文贡献为"理解 loss function 对 sparsity prediction 的影响"和"elimination of compensation as architectural simplification"。在 Introduction 和 Abstract 中明确说明当前无 wall-clock speedup，将加速留作 future work with structured sparsity。

**N2 [critical] 下游任务在实用稀疏度下崩溃，严重削弱 practical value。**
- 具体位置：Table 2 (30% KL global: MMLU 25.27%, 50%: MMLU 27.89% ≈ random), Table 4
- 问题：Dense MMLU = 65.27%。30% sparsity + global TEAL: MMLU = 25.27%（−40pp，接近 random 25%）；uniform 恢复到 40.61% 但仍损失 24.7pp。50% 时所有方法 MMLU ≈ 28%，GSM8K < 2.2%。PPL 的大幅改善（11.79 vs 23.31）未转化为 reasoning 能力保持。论文在 §4.3 提到 "PPL is a poor proxy for reasoning"，但这个结论在 Limitations 中才被充分讨论，而非贯穿全文。
- 为什么影响接收：论文的核心评价指标（PPL）与实际应用关注的指标（downstream task performance）之间存在严重脱节。如果 50% sparsity 下模型在所有知识/推理任务上退化到 random，这意味着论文展示的"最引人注目"的改善点（49% PPL reduction at 50%）在实践中可能不相关。审稿人需要知道：在什么稀疏度下，该方法能同时保持合理的 PPL 和 downstream performance？
- 建议修改方向：(1) 在主实验中更突出讨论 PPL-downstream disconnect；(2) 将 30% 的 downstream 结果提升到与 50% PPL 同等重要的位置；(3) 考虑补充 10-20% sparsity 下的 downstream 评估，找到 practical sweet spot。

**N3 [critical] 训练-推理 mask 不匹配未被分析，且残差退化来源不明。**
- 具体位置：§3.3 (Gumbel-Sigmoid, τ annealed to 0.1), §4.1 (predictor-TEAL inference), Appendix B Table 5
- 问题：训练使用 soft Gumbel-Sigmoid mask（即使 τ=0.1 也非完全 binary），推理使用 TEAL 的 hard top-k allocation。Table 5 (Appendix B) 揭示了关键数据：d_b=128 在 per-token 评估下 PPL=9.218，在 TEAL global 下 PPL=11.963——差距约 30%。这意味着从 dense (6.12) 到 KL-TEAL (11.79) 的全部退化（Δ=5.67）中，有相当一部分可能来自 soft→hard mismatch 和 TEAL global allocation 的信息丢失，而非 sparsity 本身的 capacity loss。论文从未正式分析这一 gap 的来源。
- 为什么影响接收：不分析这个 gap，读者无法判断剩余退化是方法可以改进的（通过 better allocation 或 better train-test alignment）还是 fundamental limit。这直接关系到方法的 ceiling 和 future improvement 空间。
- 建议修改方向：添加分解分析，例如：(1) per-token hard mask evaluation（控制 allocation）；(2) per-token soft mask evaluation（Table 5 已有）；(3) global hard mask with oracle scores。分离 mask quality loss、discretization loss 和 allocation loss。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] BCE 对比的公平性问题：系统差异超过 loss function。**
- 具体位置：Table 3 ablation
- 问题：KL 系统 = Forward KL + Gumbel-Sigmoid + penalty controller；BCE 系统 = BCE + hard mask + compensation。消融中 "BCE + Gumbel + Penalty" 达到 38.02（比 vanilla BCE 的 27.97 更差），说明 penalty 框架与 BCE 不兼容。这意味着 Table 2 中的 KL vs BCE 对比不仅是 loss function 的差异，而是整个 training pipeline 的差异。KL+STE (15.77) 提供了更接近的对比，但 STE 本身的 gradient bias 也是 confound。
- 建议：明确说明 KL 的优势来自 loss function + compatible training infrastructure 的组合，而非单独的 loss function。或提供一个更直接的 fair comparison（例如 MSE on output logits + Gumbel，控制 training infrastructure 的同时对比 loss）。

**W2 [warning] "Parameter-free" penalty controller 表述不准确。**
- 具体位置：§3.4, footnote ("parameter-free, no step-size tuning"), Table 7
- 问题：λ_max 在不同 sparsity target 下取不同值（30% 和 70% 用 5000，50% 用 1000），这本身就是 hyperparameter。Table 7 显示 30% target 时 λ 达到 cap (5000)，actual sparsity = 0.285（偏差 5%）。Controller 无法在所有 target 下精确收敛。
- 建议：去掉 "parameter-free" 措辞；讨论 λ_max 选择对结果的影响；说明 30% 时 5% deviation 对 PPL 的影响。

**W3 [warning] 统计效力不足。**
- 具体位置：Appendix F (3 seeds, 50% uniform only)
- 问题：(1) 3 seeds 的 95% CI（≈ [11.73, 12.11]，t-distribution）较宽，对 Table 3 中差异 <1 的 ablation 结果（如 Forward KL 11.79 vs JSD 12.54），无法判断统计显著性。(2) Multi-seed 仅在 50% uniform 下做，主结果（50% global TEAL, PPL 11.79）无方差估计。(3) Downstream metrics 更 noisy（ARC-c 33.8±1.2%），3 seeds 不足以支撑 downstream 的 regime 分析结论。
- 建议：至少在 primary configuration (50% global TEAL) 也报告 multi-seed；考虑增加到 5 seeds。

**W4 [warning] 实验规模受限。**
- 具体位置：§4.1, §4.6, Limitations
- 问题：仅 7-8B 模型（LLaMA-3.1-8B, Mistral-7B-v0.3），同一参数量级，同为 SwiGLU。论文多处使用 "transfers across SwiGLU architectures" 但实际上 (a) 仅测试了一个 scale，(b) 两个模型的 d_ff / d_model ratio 相同（14336/4096），(c) Mistral 的主要差异是 GQA + sliding window attention，这些差异与 FFN sparsity prediction 关系不大。
- 建议：弱化 generalization claims，改为 "verified on two 7-8B SwiGLU models"。如果可能，增加 13B 或更大模型的验证。

**W5 [warning] Gradient SNR 测量与训练设置不一致。**
- 具体位置：§3.5 empirical verification
- 问题：SNR 在 C4 数据上测量（"80 steps on LLaMA-3.1-8B (C4 data)"），但训练使用 WikiText-103。不同数据分布可能影响 SNR，使该测量不能直接代表训练过程中的实际 gradient quality。
- 建议：在 WikiText-103 上重复 SNR 测量，或解释为何选择 C4 及其对结论的影响。

**W6 [warning] 训练数据集过小且与评估数据同源。**
- 具体位置：§4.1 ("trained for 1000 steps on WikiText-103 with batch size 4")
- 问题：1000 steps × batch 4 × seq 2048 = ~8M tokens，仅为 WikiText-103 全集的一小部分。评估在 WikiText-2 上——与 WikiText-103 同源（都是 Wikipedia）。虽然 Appendix D 的 C4 OOD 评估有所缓解，但仅有一个 sparsity level (50%) 和一个 metric (PPL)。
- 建议：在 C4 上补充 30% 和 70% 的评估；如果条件允许，考虑在非 Wikipedia 数据上训练一版 predictor 验证泛化性。

---

### 小问题（不影响接收）

- **M1**: AdamW 的 weight decay 值未报告（§4.1）。
- **M2**: BCE 的 oracle mask 生成方式（per-layer top-k 还是 global top-k？）未明确说明（§3.5 "oracle masks m_j* = 1[|g_j| ≥ top-k threshold]"，但 threshold 的作用域不清楚）。
- **M3**: Table 1 将 ShadowLLM 归为 "Per-layer"，但 ShadowLLM 使用 attention-based routing，可能更接近 per-token。需核实分类准确性。
- **M4**: loshchilov2019adamw 引用年份为 2019，OpenAlex 匹配到的原始 arXiv 年份为 2017。会议发表年份与 arXiv 年份不一致，建议统一。
- **M5**: Appendix A 的 latency 测量在 RTX PRO 6000 Blackwell 上，但训练在 A6000 上（Limitations 提到 "~17 minutes on A6000"）。两个 GPU 架构差异较大，latency 数据的可迁移性不明。

---

## Questions to Authors

**Q1.** Table 5 (Appendix B) 显示 d_b=128 per-token PPL = 9.218, TEAL global PPL = 11.963。这 ~30% 的 gap 中，有多少来自 soft→hard discretization，多少来自 TEAL global 的 budget allocation 策略？能否提供 per-token hard mask evaluation 来分离这两个因素？

**Q2.** BCE 对比中，BCE 的 learning rate 和 optimizer 设置是否与 KL 完全一致？如果不一致，BCE 是否经过独立的 hyperparameter tuning？

**Q3.** 论文称 "KL's near-random precision (0.51)"——这是否意味着 KL predictor 学到的 mask 与 magnitude-based oracle 几乎无相关性？如果是，KL predictor 到底保留了哪些 neuron——是否有 per-layer 的分析可以说明 KL mask 与 oracle mask 的差异模式？

**Q4.** 30% sparsity 下 penalty controller 达到 λ cap (5000) 且 actual sparsity = 28.5%。如果 λ_max 设为更大的值（如 10000），sparsity 能否达到 30%？如果能，PPL 会如何变化？

**Q5.** 是否尝试过在训练中使用 hard top-k (with STE) 替代 Gumbel-Sigmoid 来缩小 train-test gap？Table 3 已有 KL+STE 但未说明其是否使用 top-k selection。

---

## 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心梯度分析数学正确，factor (a)-(d) 分解完整。Gumbel-Sigmoid 使用正确。但 BCE 对比的公平性有 confound (W1)；train-test mask mismatch 未分析 (N3)；penalty controller 在边界情况下表现不佳 (W2)。 |
| Excitement | 2.5/5 | "正确 loss > 高精度 proxy" 的洞察有价值，oracle F1 分析令人信服。2D taxonomy 有组织贡献。但无实际 speedup (N1) 和 downstream collapse (N2) 严重限制了实际影响力。 |
| Reproducibility | 3.5/5 | 训练设置报告较全（model, data, steps, LR, optimizer, τ schedule）。缺少 weight decay、gradient clipping、evaluation batch size。未提及代码是否会开源。Appendix 的超参数 sensitivity 分析有利于复现。 |
| Overall | 3/5 | Findings 边界。理论洞察清晰且有实证支撑，但 practical impact 受限于 (1) 无 wall-clock speedup, (2) downstream collapse, (3) limited scale。 |
| Confidence | 4/5 | 对 activation sparsity 和 knowledge distillation 领域较熟悉，仔细阅读了全文和附录。 |

---

## 总体评分

**Overall**: 3/5 (Findings acceptance)

**一句话总结**: 论文提供了有价值的理论洞察（KL 梯度耦合解决 BCE 的结构性不匹配），实验设计合理但存在 BCE 对比公平性和 train-test mismatch 未分析的问题；无实际推理加速和下游任务崩溃严重限制了实用价值，适合 Findings 而非主会议。

---

## 主要优势

- 梯度分析形式化清晰，factor (a)-(d) 分解为理解 loss function 设计提供了有用的分析框架
- Oracle F1 分析（BCE F1=0.613 > KL F1=0.540，但 PPL 差 91%）是全文最有说服力的实验，直接 falsify 了 "per-neuron accuracy = output quality" 的隐含假设
- 消融设计系统全面，loss isolation 实验（BCE + Gumbel + Penalty = 38.02）有效分离了 loss function 和 training infrastructure 的贡献
- 三 regime 分析发现了 allocation preference 的非单调性，对部署决策有实用指导价值
- 写作质量好，结构清晰，主线统一


---

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：运行时长 4h4m
  本轮累计 26 条消息 / 4h 4min

⚠️ 你自己的 context 状态：已 26 条消息 / 4h 4min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 258 · 2026-05-17T08:18:20.895642+00:00_

Reviewer 1 审稿意见已收到。3 个 critical（efficiency framing 误导、downstream collapse、train-test mask mismatch 未分析）+ 6 个 warning。Overall 3/5。

等待 Reviewer 2 审稿意见返回。

对于 RESET REQUEST：**[RESET AGENT]** — Reviewer 1 已完成本轮审稿，重置该 agent 即可，我继续等 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 259 · 2026-05-17T08:18:23.453875+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3/5 (Findings 边界)**
- **3 个 critical 问题**：(1) 无 wall-clock speedup 与 efficiency framing 矛盾；(2) 下游任务在 50% sparsity 崩溃至 random，PPL 改善不转化为 reasoning 保持；(3) 训练时 soft Gumbel mask vs 推理时 hard top-k 的 mismatch（~30% PPL gap）未被分析
- **6 个 warning 问题**：BCE 对比公平性、"parameter-free" 表述不准确、3-seed 统计效力不足、仅 7-8B 规模、SNR 测量数据不一致、训练评估数据同源
- **主要优势**：梯度分析形式化清晰，oracle F1 分析令人信服，消融覆盖全面，regime 分析有实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 260 · 2026-05-17T08:18:28.510650+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 22

## Round 22

6 recorded events


### User

_source line 261 · 2026-05-17T08:19:12.484497+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）

### 总体评分
**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 核心方法是已有技术（KL distillation + Gumbel relaxation）在新场景（per-token activation sparsity）的组合应用，执行质量扎实但新颖性有限；downstream metrics 与 PPL 叙事存在系统性矛盾，削弱了核心 claim 的说服力。

### 官方维度打分（ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 实验设计合理，但 downstream metrics 与 PPL 叙事矛盾（MMLU: KL 劣于 TEAL at 30%），三 regime 分析证据不足 |
| Excitement | 2.5 / 5 | KL + Gumbel mask learning 在 MaskLLM 中已有先例，contribution 为场景迁移 + gradient analysis |
| Overall | 3.0 / 5 | 执行质量较高（ablation 充分、cross-arch 验证），novelty 为增量组合 |
| Confidence | 4 / 5 | 熟悉 activation sparsity 和 knowledge distillation 文献 |
| Reproducibility | 4 / 5 | 超参数详尽，训练细节充分，无代码承诺 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] Responsible NLP Research Checklist 缺失，desk rejection 风险
- ARR 自 2024-12 起强制要求此 checklist，缺失可直接 desk reject。论文无 checklist 也无 Ethics Statement。
- 建议：参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。

**N2** [critical] Downstream metrics 与 PPL-centric 叙事系统性矛盾
- Table 1: 30% sparsity KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) 低 13.3pp。50% sparsity MMLU 全部 ≈28%（近随机），KL (27.89%) vs TEAL (28.32%) 无差异。GSM8K 50% KL (1.29%) 比 TEAL (1.97%) 更差。
- 论文核心叙事围绕 PPL 改善（11.79 vs 23.31），但 downstream 讲了不同的故事。如果 PPL 改善不转化为 downstream 收益，"eliminates compensation networks" 的实际价值需重新评估。
- Limitations 承认 PPL is poor proxy for reasoning，但 Abstract/Introduction 仍以 PPL 为核心 framing，自相矛盾。
- 建议：Abstract/Introduction 诚实呈现 downstream mixed results；讨论 KL 训练为何恶化 MMLU（可能过度偏向 PPL-dominant layers）。

**N3** [critical] 与 MaskLLM 核心技术重叠未充分辨析
- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。Related Work 仅以 "weight vs activation, static vs contextual" 区分，但这是应用场景差异而非方法论差异。核心 pipeline（KL + Gumbel mask learning with frozen weights）相同。
- 论文未讨论：(1) Gumbel-Softmax (MaskLLM) vs Gumbel-Sigmoid (本文) 的技术原因；(2) MaskLLM 是否已隐含解决 structural mismatch；(3) 如果 MaskLLM 的 mask 改为 input-dependent 是否等价于本文方法。
- 建议：明确讨论方法论层面的区别和联系。

---

### Should-Fix 问题

**W1** [warning] 三 regime 分析证据不足以支撑 claim 强度
- 三 regime 定义来自 2 个模型 × 3 个 sparsity levels = 6 数据点。具体边界阈值（≤30%, ~40%, ≥50%）的跨规模/跨架构泛化性完全未验证，但论文作为 Contribution 之一呈现。
- 建议：弱化 claim，限定为 "observed on 7-8B SwiGLU models"。

**W2** [warning] D2DMoE (NeurIPS 2024) 遗漏
- Dense-to-Dynamic-k MoE 训练 router 用 ℓ2-norm regression 预测 expert 贡献，实现 per-token activation sparsity。其 training signal 既非 BCE 也非 KL，应位于 taxonomy 的 Per-token × Intermediate cell。遗漏使 taxonomy 不完整。
- 建议：讨论并纳入 taxonomy。

**W3** [warning] Abstract 数据堆砌（18+ 个数字），审稿人 30 秒内无法消化
- 建议：保留 3-4 个核心数字。

**W4** [warning] 无实际 wall-clock speedup（+6.4% overhead），但 framing 暗示 efficiency gain
- Title "Sparsity Prediction" + Abstract "eliminating compensation" 让读者预期加速。实际 sparse model 比 dense 更慢。
- 建议：Abstract 明确定位为 prediction quality and architectural simplification。

**W5** [warning] Taxonomy 可能 post-hoc rationalization
- 3×3 中仅 4 cell 填充，5 cell 空。两个轴恰好让本文独占一 cell。DejaVu 被归类为 Per-token × Decomposed 但 Table 2 中缺失。
- 建议：补充 DejaVu 和 D2DMoE，讨论轴选择依据。

**W6** [warning] WAS (EMNLP 2025 main) 可能遗漏
- Weight-Aware Activation Sparsity 使用 constrained Bayesian optimization，投 EMNLP 2026 应引用上届主会相关工作。

---

### 小问题
- Abstract 中 "-ing" 分词短语有轻微 AI 写作痕迹（L3 "confirming", L5 "demonstrating"）
- BiB: xu2026spon bib year=2026 vs OpenAlex=2025，需确认
- Table 2 缺 DejaVu（Introduction 提到但 Table 未列）
- Figure 1 label "fig:taxonomy" 但内容是 method overview 不是 taxonomy
- Conclusion 仅 3 行过短

---

### 主要优势
1. Gradient analysis（§3.5 Eq. 8-9）清晰有力，SNR 实验验证（early layer 34-156× 差异）
2. Ablation 设计系统全面，特别是 loss isolation（BCE+Gumbel = 38.02 PPL，证明 Gumbel 无法拯救 BCE）
3. Cross-architecture 验证 Mistral-7B 显示一致 KL-over-TEAL ratio
4. F1 oracle analysis 优雅说明 proxy vs end-to-end metric 的 misalignment
5. 训练成本低（1000 steps / ~17 min on A6000）

---

### 引用验证
31 条引用全部通过 OpenAlex 验证（29 verified, 2 minor mismatch: grattafiori2024llama3 first_author field, loshchilov2019adamw year 2019 vs 2017）。无虚假引用。无 orphan/missing bib entries。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-17T08:19:42.648369+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）\n\n### 总体评分\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 核心方法是已有技术（KL distillation + Gumbel relaxation）在新场景（per-token activation sparsity）的组合应用，执行质量扎实但新颖性有限；downstream metrics 与 PPL 叙事存在系统性矛盾，削弱了核心 claim 的说服力。\n\n### Must-Fix 问题\n\n**N1** [critical] Responsible NLP Research Checklist 缺失，desk rejection 风险\n- ARR 自 2024-12 起强制要求此 checklist，缺失可直接 desk reject。论文无 checklist 也无 Ethics Statement。\n- 建议：参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。\n\n**N2** [critical] Downstream metrics 与 PPL-centric 叙事系统性矛盾\n- Table 1: 30% sparsity KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) 低 13.3pp。50% sparsity MMLU 全部 ≈28%（近随机），KL (27.89%) vs TEAL (28.32%) 无差异。GSM8K 50% KL (1.29%) 比 TEAL (1.97%) 更差。\n- 论文核心叙事围绕 PPL 改善（11.79 vs 23.31），但 downstream 讲了不同的故事。如果 PPL 改善不转化为 downstream 收益，\"eliminates compensation networks\" 的实际价值需重新评估。\n- Limitations 承认 PPL is poor proxy for reasoning，但 Abstract/Introduction 仍以 PPL 为核心 framing，自相矛盾。\n- 建议：Abstract/Introduction 诚实呈现 downstream mixed results；讨论 KL 训练为何恶化 MMLU（可能过度偏向 PPL-dominant layers）。\n\n**N3** [critical] 与 MaskLLM 核心技术重叠未充分辨析\n- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。Related Work 仅以 \"weight vs activation, static vs contextual\" 区分，但这是应用场景差异而非方法论差异。核心 pipeline（KL + Gumbel mask learning with frozen weights）相同。\n- 论文未讨论：(1) Gumbel-Softmax (MaskLLM) vs Gumbel-Sigmoid (本文) 的技术原因；(2) MaskLLM 是否已隐含解决 structural mismatch；(3) 如果 MaskLLM 的 mask 改为 input-dependent 是否等价于本文方法。\n- 建议：明确讨论方法论层面的区别和联系。\n\n### Should-Fix 问题\n\n**W1** [warning] 三 regime 分析证据不足以支撑 claim 强度\n- 三 regime 定义来自 2 个模型 × 3 个 sparsity levels = 6 数据点。具体边界阈值（≤30%, ~40%, ≥50%）的跨规模/跨架构泛化性完全未验证，但论文作为 Contribution 之一呈现。\n\n**W2** [warning] D2DMoE (NeurIPS 2024) 遗漏\n- Dense-to-Dynamic-k MoE 训练 router 用 ℓ2-norm regression 预测 expert 贡献，实现 per-token activation sparsity。其 training signal 既非 BCE 也非 KL，应位于 taxonomy 的 Per-token × Intermediate cell。遗漏使 taxonomy 不完整。\n\n**W3** [warning] Abstract 数据堆砌（18+ 个数字），审稿人 30 秒内无法消化\n\n**W4** [warning] 无实际 wall-clock speedup（+6.4% overhead），但 framing 暗示 efficiency gain\n\n**W5** [warning] Taxonomy 可能 post-hoc rationalization\n- 3×3 中仅 4 cell 填充，5 cell 空。两个轴恰好让本文独占一 cell。DejaVu 被归类为 Per-token × Decomposed 但 Table 2 中缺失。\n\n**W6** [warning] WAS (EMNLP 2025 main) 可能遗漏\n\n### 小问题\n- Abstract 中 \"-ing\" 分词短语有轻微 AI 写作痕迹\n- xu2026spon bib year=2026 vs OpenAlex=2025\n- Table 2 缺 DejaVu\n- Figure 1 label \"fig:taxonomy\" 但内容是 method overview\n- Conclusion 仅 3 行过短\n\n### 主要优势\n1. Gradient analysis 清晰有力，SNR 验证\n2. Ablation 系统全面，loss isolation 有力\n3. Cross-architecture Mistral 验证一致\n4. F1 oracle analysis 优雅\n5. 训练成本低",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）\n\n### 总体评分\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 核心方法是已有技术（KL distillation + Gumbel relaxation）在新场景（per-token activation sparsity）的组合应用，执行质量扎实但新颖性有限；downstream metrics 与 PPL 叙事存在系统性矛盾，削弱了核心 claim 的说服力。\n\n### Must-Fix 问题\n\n**N1** [critical] Responsible NLP Research Checklist 缺失，desk rejection 风险\n- ARR 自 2024-12 起强制要求此 checklist，缺失可直接 desk reject。论文无 checklist 也无 Ethics Statement。\n- 建议：参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。\n\n**N2** [critical] Downstream metrics 与 PPL-centric 叙事系统性矛盾\n- Table 1: 30% sparsity KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) 低 13.3pp。50% sparsity MMLU 全部 ≈28%（近随机），KL (27.89%) vs TEAL (28.32%) 无差异。GSM8K 50% KL (1.29%) 比 TEAL (1.97%) 更差。\n- 论文核心叙事围绕 PPL 改善（11.79 vs 23.31），但 downstream 讲了不同的故事。如果 PPL 改善不转化为 downstream 收益，\"eliminates compensation networks\" 的实际价值需重新评估。\n- Limitations 承认 PPL is poor proxy for reasoning，但 Abstract/Introduction 仍以 PPL 为核心 framing，自相矛盾。\n- 建议：Abstract/Introduction 诚实呈现 downstream mixed results；讨论 KL 训练为何恶化 MMLU（可能过度偏向 PPL-dominant layers）。\n\n**N3** [critical] 与 MaskLLM 核心技术重叠未充分辨析\n- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。Related Work 仅以 \"weight vs activation, static vs contextual\" 区分，但这是应用场景差异而非方法论差异。核心 pipeline（KL + Gumbel mask learning with frozen weights）相同。\n- 论文未讨论：(1) Gumbel-Softmax (MaskLLM) vs Gumbel-Sigmoid (本文) 的技术原因；(2) MaskLLM 是否已隐含解决 structural mismatch；(3) 如果 MaskLLM 的 mask 改为 input-dependent 是否等价于本文方法。\n- 建议：明确讨论方法论层面的区别和联系。\n\n### Should-Fix 问题\n\n**W1** [warning] 三 regime 分析证据不足以支撑 claim 强度\n- 三 regime 定义来自 2 个模型 × 3 个 sparsity levels = 6 数据点。具体边界阈值（≤30%, ~40%, ≥50%）的跨规模/跨架构泛化性完全未验证，但论文作为 Contribution 之一呈现。\n\n**W2** [warning] D2DMoE (NeurIPS 2024) 遗漏\n- Dense-to-Dynamic-k MoE 训练 router 用 ℓ2-norm regression 预测 expert 贡献，实现 per-token activation sparsity。其 training signal 既非 BCE 也非 KL，应位于 taxonomy 的 Per-token × Intermediate cell。遗漏使 taxonomy 不完整。\n\n**W3** [warning] Abstract 数据堆砌（18+ 个数字），审稿人 30 秒内无法消化\n\n**W4** [warning] 无实际 wall-clock speedup（+6.4% overhead），但 framing 暗示 efficiency gain\n\n**W5** [warning] Taxonomy 可能 post-hoc rationalization\n- 3×3 中仅 4 cell 填充，5 cell 空。两个轴恰好让本文独占一 cell。DejaVu 被归类为 Per-token × Decomposed 但 Table 2 中缺失。\n\n**W6** [warning] WAS (EMNLP 2025 main) 可能遗漏\n\n### 小问题\n- Abstract 中 \"-ing\" 分词短语有轻微 AI 写作痕迹\n- xu2026spon bib year=2026 vs OpenAlex=2025\n- Table 2 缺 DejaVu\n- Figure 1 label \"fig:taxonomy\" 但内容是 method overview\n- Conclusion 仅 3 行过短\n\n### 主要优势\n1. Gradient analysis 清晰有力，SNR 验证\n2. Ablation 系统全面，loss isolation 有力\n3. Cross-architecture Mistral 验证一致\n4. F1 oracle analysis 优雅\n5. 训练成本低",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-17T08:20:18.916639+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 36268
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-17T08:20:21.578214+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验有效性）\n\n### 总体评分\n**Overall**: 3/5 (Findings)\n**一句话总结**: 论文提供了有价值的理论洞察（KL 梯度耦合解决 BCE 的结构性不匹配），实验设计合理但存在 BCE 对比公平性和 train-test mismatch 未分析的问题；无实际推理加速和下游任务崩溃严重限制了实用价值，适合 Findings 而非主会议。\n\n### Must-Fix 问题\n\n**N1** [critical] 论文以 efficiency 为动机，但实际无 wall-clock speedup，且 framing 产生误导。\n- Table 6 (Appendix A) 显示 KL predictor-only 在 50% sparsity 下为 126.78ms（dense 119.11ms），overhead = +6.4%。消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。\n- 论文 Introduction 的 framing 暗示 \"simplify inference\" 和 \"eliminating compensation\" 带来效率增益。但实际 sparse model 比 dense 慢。\n- 建议：重新定位为 prediction quality / understanding。\n\n**N2** [critical] 下游任务在实用稀疏度下崩溃，严重削弱 practical value。\n- Dense MMLU = 65.27%。30% KL global: MMLU = 25.27%（−40pp）；50%: MMLU ≈ 28%（≈ random）。PPL 大幅改善未转化为 reasoning 保持。\n- 建议：突出 PPL-downstream disconnect；补充 10-20% 评估找 practical sweet spot。\n\n**N3** [critical] 训练-推理 mask 不匹配未被分析，且残差退化来源不明。\n- Table 5 (Appendix B): d_b=128 per-token PPL=9.218 vs TEAL global PPL=11.963——差距约 30%。从 dense (6.12) 到 KL-TEAL (11.79) 的全部退化（Δ=5.67）中，有相当一部分可能来自 soft→hard mismatch 和 TEAL global allocation 信息丢失。\n- 建议：分解分析 mask quality loss、discretization loss、allocation loss。\n\n### Should-Fix 问题\n\n**W1** [warning] BCE 对比的公平性：KL 和 BCE 使用不同 training pipeline（Gumbel vs hard mask, penalty vs fixed threshold），不仅是 loss function 差异。\n- BCE + Gumbel + Penalty = 38.02（比 vanilla BCE 27.97 更差）说明 penalty 与 BCE 不兼容。\n\n**W2** [warning] \"Parameter-free\" penalty controller 表述不准确。\n- λ_max 在不同 sparsity target 下不同（1000 vs 5000），本身是 hyperparameter。30% 时达到 cap 且偏差 5%。\n\n**W3** [warning] 统计效力不足。\n- 3 seeds 的 95% CI 较宽，Table 3 中差异 <1 的 ablation 无法判断统计显著性。Multi-seed 仅在 50% uniform 下做。\n\n**W4** [warning] 仅 7-8B 模型，同一参数量级。\n\n**W5** [warning] Gradient SNR 在 C4 数据上测量，但训练使用 WikiText-103，数据不一致。\n\n**W6** [warning] 训练数据集过小且与评估数据同源。\n- 1000 steps × batch 4 × seq 2048 ≈ 8M tokens。WikiText-103 和 WikiText-2 同源。\n\n### 小问题\n- M1: AdamW weight decay 未报告\n- M2: BCE oracle mask 的 threshold 作用域不清楚\n- M3: ShadowLLM 在 Table 1 分类可能不准确\n- M4: loshchilov2019adamw 年份不一致\n- M5: Latency 测量 GPU (RTX PRO 6000 Blackwell) 与训练 GPU (A6000) 不同\n\n### Questions to Authors\nQ1. Table 5 per-token vs TEAL global 的 ~30% PPL gap 来源分解？\nQ2. BCE 的 learning rate 和 optimizer 是否与 KL 一致？\nQ3. KL predictor 保留了哪些 neuron？per-layer mask 差异分析？\nQ4. 30% 时 λ_max 增大能否达到目标？对 PPL 影响？\nQ5. 是否尝试过训练中使用 hard top-k with STE？\n\n### 主要优势\n1. 梯度分析形式化清晰，factor (a)-(d) 分解\n2. Oracle F1 分析（BCE F1=0.613 > KL F1=0.540, 但 PPL 差 91%）全文最有说服力\n3. 消融系统全面，loss isolation 有效\n4. 三 regime 分析发现非单调性\n5. SPON 正交性分析有指导价值",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验有效性）\n\n### 总体评分\n**Overall**: 3/5 (Findings)\n**一句话总结**: 论文提供了有价值的理论洞察（KL 梯度耦合解决 BCE 的结构性不匹配），实验设计合理但存在 BCE 对比公平性和 train-test mismatch 未分析的问题；无实际推理加速和下游任务崩溃严重限制了实用价值，适合 Findings 而非主会议。\n\n### Must-Fix 问题\n\n**N1** [critical] 论文以 efficiency 为动机，但实际无 wall-clock speedup，且 framing 产生误导。\n- Table 6 (Appendix A) 显示 KL predictor-only 在 50% sparsity 下为 126.78ms（dense 119.11ms），overhead = +6.4%。消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。\n- 论文 Introduction 的 framing 暗示 \"simplify inference\" 和 \"eliminating compensation\" 带来效率增益。但实际 sparse model 比 dense 慢。\n- 建议：重新定位为 prediction quality / understanding。\n\n**N2** [critical] 下游任务在实用稀疏度下崩溃，严重削弱 practical value。\n- Dense MMLU = 65.27%。30% KL global: MMLU = 25.27%（−40pp）；50%: MMLU ≈ 28%（≈ random）。PPL 大幅改善未转化为 reasoning 保持。\n- 建议：突出 PPL-downstream disconnect；补充 10-20% 评估找 practical sweet spot。\n\n**N3** [critical] 训练-推理 mask 不匹配未被分析，且残差退化来源不明。\n- Table 5 (Appendix B): d_b=128 per-token PPL=9.218 vs TEAL global PPL=11.963——差距约 30%。从 dense (6.12) 到 KL-TEAL (11.79) 的全部退化（Δ=5.67）中，有相当一部分可能来自 soft→hard mismatch 和 TEAL global allocation 信息丢失。\n- 建议：分解分析 mask quality loss、discretization loss、allocation loss。\n\n### Should-Fix 问题\n\n**W1** [warning] BCE 对比的公平性：KL 和 BCE 使用不同 training pipeline（Gumbel vs hard mask, penalty vs fixed threshold），不仅是 loss function 差异。\n- BCE + Gumbel + Penalty = 38.02（比 vanilla BCE 27.97 更差）说明 penalty 与 BCE 不兼容。\n\n**W2** [warning] \"Parameter-free\" penalty controller 表述不准确。\n- λ_max 在不同 sparsity target 下不同（1000 vs 5000），本身是 hyperparameter。30% 时达到 cap 且偏差 5%。\n\n**W3** [warning] 统计效力不足。\n- 3 seeds 的 95% CI 较宽，Table 3 中差异 <1 的 ablation 无法判断统计显著性。Multi-seed 仅在 50% uniform 下做。\n\n**W4** [warning] 仅 7-8B 模型，同一参数量级。\n\n**W5** [warning] Gradient SNR 在 C4 数据上测量，但训练使用 WikiText-103，数据不一致。\n\n**W6** [warning] 训练数据集过小且与评估数据同源。\n- 1000 steps × batch 4 × seq 2048 ≈ 8M tokens。WikiText-103 和 WikiText-2 同源。\n\n### 小问题\n- M1: AdamW weight decay 未报告\n- M2: BCE oracle mask 的 threshold 作用域不清楚\n- M3: ShadowLLM 在 Table 1 分类可能不准确\n- M4: loshchilov2019adamw 年份不一致\n- M5: Latency 测量 GPU (RTX PRO 6000 Blackwell) 与训练 GPU (A6000) 不同\n\n### Questions to Authors\nQ1. Table 5 per-token vs TEAL global 的 ~30% PPL gap 来源分解？\nQ2. BCE 的 learning rate 和 optimizer 是否与 KL 一致？\nQ3. KL predictor 保留了哪些 neuron？per-layer mask 差异分析？\nQ4. 30% 时 λ_max 增大能否达到目标？对 PPL 影响？\nQ5. 是否尝试过训练中使用 hard top-k with STE？\n\n### 主要优势\n1. 梯度分析形式化清晰，factor (a)-(d) 分解\n2. Oracle F1 分析（BCE F1=0.613 > KL F1=0.540, 但 PPL 差 91%）全文最有说服力\n3. 消融系统全面，loss isolation 有效\n4. 三 regime 分析发现非单调性\n5. SPON 正交性分析有指导价值",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-17T08:20:22.944131+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1365
}
```

</details>

---


### Assistant

_source line 266 · 2026-05-17T08:20:25.643297+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 267 · 2026-05-17T08:20:28.189222+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：论文在执行层面（ablation、cross-arch 验证、gradient analysis）质量扎实，但三个 critical 问题影响接收判断：(1) 缺失 ARR 强制要求的 Responsible NLP Checklist（desk rejection 风险）；(2) downstream metrics（MMLU、GSM8K）与 PPL-centric 叙事系统性矛盾，核心 claim 的实际价值需重新定位；(3) 与 MaskLLM 在方法论层面的核心重叠（KL + Gumbel + frozen weights）未充分辨析，留下新颖性不足的质疑空间。建议评分 Overall 3.0（Findings level）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 268 · 2026-05-17T08:20:33.382598+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 269 · 2026-05-17T08:22:27.177647+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 Round 1 意见的交叉回应

---

## Must-Fix 问题

### [AGREE] R2-N1: Responsible NLP Research Checklist 缺失

同意。我在 Round 1 审稿中遗漏了这一检查。main.tex 中确无 checklist 或 Ethics Statement。ARR 自 2024-12 起强制要求，缺失确实构成 desk rejection 风险。这是纯粹的格式合规问题，作者应立即补充。

---

### [AGREE] R2-N2: Downstream metrics 与 PPL-centric 叙事系统性矛盾

强烈同意，这与我自己的 N2 一致。R2 进一步指出了一个我未充分强调的关键数据点：**30% sparsity 下 KL global 的 MMLU (25.27%) 比 TEAL vanilla (38.61%) 低 13.3pp**（Table 2）。这意味着 KL predictor 在 PPL 维度改善的同时，MMLU 反而显著恶化，KL 训练可能过度优化 token prediction 分布而牺牲了知识保留。

补充我的观察：Table 4 (§4.4) 显示 KL uniform 在 30% 时恢复 MMLU 到 40.61%（+15.3pp over global），说明问题可能不在 KL 训练本身，而在 global top-k allocation 对 late layers（logit-forming layers）的 starvation 效应。§4.4 提到 "L31 retention 28.4%"，知识密集层被剥夺 budget 是 MMLU 崩溃的直接原因。但论文对此的讨论仅限于 regime analysis（§4.4），未反映到 Abstract/Introduction 的核心叙事中——R2 的 "自相矛盾" 判断准确。

---

### [REBUT] R2-N3: 与 MaskLLM 核心技术重叠

**部分同意论文讨论不足，但不同意"核心技术重叠"的判断。**

R2 正确指出 Related Work (§5 第2段) 对 MaskLLM 的区分过于简略——仅以 "weight vs activation, static vs contextual" 一笔带过。论文确实应更深入讨论方法论层面的联系。但 R2 将两者描述为 "核心 pipeline 相同" 忽略了关键的结构差异：

1. **优化问题本质不同。** MaskLLM 学习 static masks（每个 N:M group 内选哪些 weight 保留），优化空间是 $\binom{M}{N}$ 的 categorical distribution per group。本文学习 per-token contextual masks（每个 input position 独立决定哪些 neurons 保留），优化空间是 $\{0,1\}^{L \times d_{ff}}$ 的 combinatorial space，受 global budget constraint。MaskLLM 没有 "structural mismatch" 问题——它的 masks 在训练和推理中都是 group-local 的，不存在 per-element 训练 vs. global allocation 推理的矛盾。

2. **本文的核心贡献不是 "KL + Gumbel" pipeline 本身，而是 §3.5 的梯度分析。** Factor (a)-(d) 分解证明了 per-neuron BCE 和 end-to-end KL 在 contextual prediction + global top-k 设定下的结构性差异（factor (b) 的 downstream Jacobian 耦合）。这个分析对 MaskLLM 不适用——MaskLLM 的 masks 是 input-independent 的，不涉及 contextual prediction 的 gradient flow。

3. **R2 的第三个问题 "如果 MaskLLM 改为 input-dependent 是否等价" 值得讨论**，但答案是否定的：(a) MaskLLM 用 Gumbel-Softmax 在 N:M group 内做 categorical selection，本文用 Gumbel-Sigmoid 做 binary per-neuron decisions + global budget constraint——relaxation 机制不同；(b) MaskLLM 的 allocation 是 per-group structured (2:4)，本文是 unstructured global top-k——inference protocol 不同；(c) 即使改为 input-dependent，MaskLLM 的 per-group 结构不产生 global coupling 问题。

**结论：同意论文应更充分讨论 MaskLLM（especially 技术原因 for Gumbel-Softmax vs Sigmoid），但 "核心技术重叠" 的判断不成立。本文的核心新颖性在于 structural mismatch 的识别和梯度分析（§3.5），这在 MaskLLM 的设定中不存在。** 建议作者添加一段专门的 MaskLLM 技术对比。

---

## Should-Fix 问题

### [AGREE] R2-W1: 三 regime 分析证据不足

同意。2 models × 3 sparsity levels = 6 个数据点。具体 regime 边界（≤30%, ~40%, ≥50%）的泛化性完全未验证。这与我的 W4（实验规模受限）一致。作为 Contribution 之一呈现，claim 强度应降低为 "empirical observation on 7-8B models" 而非 general framework。补充：regime 边界可能与模型规模、架构、预训练数据量密切相关，论文未讨论这些 confounds。

---

### [AGREE] R2-W2: D2DMoE 遗漏

同意。如果 D2DMoE (NeurIPS 2024) 使用 ℓ2-norm regression（intermediate objective）进行 per-token router training，它应填入 Table 1 的 Per-token × Intermediate cell（当前为空）。这不仅是引用遗漏，还影响 taxonomy 的完整性——本文 claim "no prior work has combined per-token contextual prediction with a coupled training signal"（§3.6 末段），但 taxonomy 中应先确认所有 cell 的 occupancy 状态。

---

### [AGREE] R2-W3: Abstract 数据堆砌

同意。我统计 Abstract 中至少有 **25 个数字/百分比**（2.37M, 75.9M, <1%, 11.79, 50%, 23.31, 27.97, 2.71×, 11.92±0.07, CV<1%, 18%, 30%, 49%, 50%, 82%, 70%, 17.91, 100.11, 2.93×, 7-8B, 7%, ≤50%, 0.196, 2.4%, 12.08→11.79）。审稿人在 30 秒内无法从中提取核心信息。按照 ACL 论文写作规范，Abstract 应以叙事为主、最多引用 2-3 个关键数字。当前 Abstract 更像 Results 的压缩版，不是独立的故事。

---

### [AGREE] R2-W4: 无实际 wall-clock speedup

同意，与我的 N1 一致。Appendix A Table 6 明确显示 +6.4% overhead。

---

### [AGREE] R2-W5: Taxonomy 可能 post-hoc rationalization

部分同意。5/9 cells 空的确引发 post-hoc 质疑，尤其是两个轴恰好让本文独占一 cell。但我认为两个轴本身有独立的组织价值（correction granularity 和 training signal coupling 是文献中可辨认的真实维度），因此判断为 "presentation concern" 而非 "validity concern"。

补充：R2 指出 DejaVu 在 Table 1 中被归类但 Table 2 中缺失——这确实是一个重要遗漏。如果 DejaVu 是 Per-token × Decomposed 的代表方法，它应该作为 baseline 出现在实验对比中。当前 Table 2 的 BCE baseline 未说明是否等同于 DejaVu 的实现。

---

### [REBUT] R2-W6: WAS (EMNLP 2025) 可能遗漏

无法确认。R2 未提供 WAS 的完整标题、作者或链接。如果 R2 能提供具体引用信息，我可以评估其与本文的相关性。仅凭缩写无法判断是否确实是重要遗漏。

---

## 小问题

**[AGREE]** Abstract -ing 分词短语。Abstract 确有多处 -ing 结尾："eliminating the need for compensation", "confirming a structural rather than computational failure", "confirming training stability", "demonstrating substantial output fidelity"。这是典型的 AI 写作标志，应改写。

**[AGREE]** xu2026spon bib year 不一致。references.bib 中 `year = {2026}`，如果 OpenAlex 显示 2025，应核实论文实际发表/接收年份。

**[AGREE]** Table 2 缺 DejaVu。如 W5 中所述，taxonomy 中提到的方法应尽可能出现在实验对比中。

**[AGREE]** Figure 1 label 为 `fig:taxonomy` 但内容是 method overview。§3.6 最后一段 "Figure~\ref{fig:taxonomy}" 引用的是 Figure 1（method overview），但 taxonomy 实际在 Table 1。标签应改为 `fig:overview` 或类似。

**[AGREE]** Conclusion 仅 3 行过短。§6 只有一段（conclusion.tex 仅 6 行 LaTeX），没有 future work discussion、没有 broader implications。对于一篇 long paper 这不符合预期。

---

## 对 R2 总体判断的评价

R2 给出 Overall 3.0/5 (Findings)，与我的判断一致。R2 的新颖性质疑（R2-N3 MaskLLM overlap）是本次评审的核心分歧点。我的立场是：方法论工具确实不新（KL + Gumbel），但 structural mismatch 的识别和梯度分析（§3.5）是本文真正的贡献所在，这在 MaskLLM 的设定中不存在。论文应通过更充分的 MaskLLM 对比来突出这一点。

R2 的 checklist 缺失（R2-N1）和 D2DMoE 遗漏（R2-W2）是我 Round 1 遗漏的有价值发现。Abstract 数据堆砌（R2-W3）的具体量化（18+ 数字）也比我更到位。

两位 Reviewer 一致认为的核心问题：(1) downstream collapse vs PPL framing 矛盾，(2) 无 wall-clock speedup，(3) 实验规模有限。这三点是决定接收/拒绝的关键。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 270 · 2026-05-17T08:22:36.321882+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 25

## Round 25

8 recorded events


### User

_source line 271 · 2026-05-17T08:22:37.332527+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

要点总结：
- **R2-N1 (Checklist)**: [AGREE]，我 Round 1 遗漏的有效发现，desk reject 风险
- **R2-N2 (Downstream)**: [AGREE]，与我的 N2 一致，R2 补充了 MMLU 在 KL global 下比 TEAL 更差的关键数据点
- **R2-N3 (MaskLLM overlap)**: [REBUT]，同意讨论不足但不同意"核心技术重叠"——本文的核心贡献是 §3.5 structural mismatch 梯度分析，这在 MaskLLM 的 static N:M 设定中不存在
- **R2-W1~W5**: 全部 [AGREE]，其中 D2DMoE 遗漏和 Abstract 数据堆砌是我 Round 1 未充分覆盖的
- **R2-W6 (WAS)**: [REBUT]，信息不足无法判断

两位 Reviewer 一致的三个核心问题：downstream collapse vs PPL framing、无 wall-clock speedup、实验规模有限。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### 逐条回应摘要

**Must-Fix:**
- [AGREE] R1-N1 (无 speedup + misleading framing): 强同意。Introduction "simplify inference" 与 Limitations "focuses on prediction quality" 直接矛盾。
- [AGREE] R1-N2 (downstream 崩溃): 强同意。补充更尖锐的数据：30% sparsity KL global MMLU=25.27% 比 TEAL vanilla 38.61% 低 13.3pp，KL 训练在 MMLU 上可能造成 active harm。
- [AGREE with nuance] R1-N3 (train-inference mismatch): 核心观点同意。但澄清：per-token vs TEAL global gap 主要来自 allocation strategy 差异，非 soft→hard discretization（per-token eval 也用 hard mask）。三向分解建议有价值。

**Should-Fix:**
- [AGREE] R1-W1 (BCE 对比公平性): KL 优势与 Gumbel 不可分离，论文不应归因于 loss alone。
- [AGREE] R1-W2 ("parameter-free" 不准确): λ_max 在不同 target 取不同值，是 hyperparameter。
- [AGREE] R1-W3 (统计效力): JSD vs Reverse KL 差异 0.26 无 CI，结论过于确定。Global allocation 的 multi-seed 缺失。
- [AGREE] R1-W4 (仅 7-8B): 同意。
- [REBUT] R1-W5 (SNR 数据不一致): SNR 分析目的是揭示 loss 结构性质，不依赖数据分布。C4 ≠ WikiText-103 反而表明结论不是数据特有的。建议降级为 minor。
- [AGREE with nuance] R1-W6 (训练数据小+同源): 部分同意，但 Appendix D C4 OOD evaluation（52.5% advantage）已部分缓解。建议降级为 minor。

**小问题**: 全部同意（M1-M5）。

**Questions**: Q1（per-token vs TEAL gap 分解）和 Q5（hard top-k + STE）最有价值，直接触及技术盲区。

### 与我的审稿的互补性

R1 在 train-inference mismatch (N3) 和 BCE 对比公平性 (W1) 上比我更深入。我在 novelty 问题上更深入（MaskLLM 技术重叠、taxonomy post-hoc、missing references D2DMoE/WAS）。两份审稿互补性强。

### 综合判断

R1 和我的审稿一致指向 Findings 评级（Overall 3.0）。核心共识：
1. 理论洞察（gradient analysis）有价值
2. 执行质量较高（ablation、cross-arch）
3. Novelty 为增量组合（R2 关注）+ 实用性受限（R1 关注）
4. 叙事需重新定位（PPL-centric → 承认 downstream 局限）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-17T08:22:57.541596+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 273 · 2026-05-17T08:22:57.592200+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-17T08:24:52.179253+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ===== Round 1-2 历史 issues（已 resolved）=====\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"desk-reject 条件\"}\n    action_items:\n      - {round: 1, action: \"拆为独立 section*\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit 7018701\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 AGREE\"}\n    action_items:\n      - {round: 1, action: \"拆出 Limitations 后确认页数\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Main content p.8, total 10p\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 critical, R2 AGREE\"}\n    action_items:\n      - {round: 1, action: \"C4 validation PPL\", assigned_to: \"main_agent\", status: done}\n    resolution: \"C4: Dense=9.21, KL 50%=18.40, TEAL 50%=38.75\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Structural failure 证据不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"两位独立指出\"}\n    action_items:\n      - {round: 1, action: \"BCE+Gumbel ×3 LR 对照\", assigned_to: \"main_agent\", status: done}\n    resolution: \"BCE best=38.02 vs KL=11.79\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融缺关键维度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 critical → 降 warning\"}\n    action_items:\n      - {round: 1, action: \"d_b/τ/steps/Lagrangian sweep\", assigned_to: \"main_agent\", status: done}\n    resolution: \"Appendix B-C 全覆盖\"\n    resolution_round: 1\n\n  - id: \"R1-W1-Rd2\"\n    summary: \"Lagrangian 术语误用\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n    action_items:\n      - {round: 2, action: \"全文术语替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 2, action: \"启发式 schedule 说明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commits fe7c034 + e00d270\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"λ/sparsity 时序曲线缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出\"}\n      - {round: 2, reviewers: [1, 2], note: \"遗留未修复\"}\n    action_items:\n      - {round: 2, action: \"生成 + 修复 50% + 集成\", assigned_to: \"main_agent+paper_agent\", status: done}\n    resolution: \"lagrangian_dynamics.pdf 集成到 Appendix C\"\n    resolution_round: 2\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"需报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}\n    action_items:\n      - {round: 2, action: \"Abstract + §4.2 添加 KL/Dense ratio\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}\n    action_items:\n      - {round: 2, action: \"加 scale qualifier\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"30% MMLU 异常缺 per-layer 分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n    action_items:\n      - {round: 2, action: \"Per-layer retention 分析 + 叙事修正\", assigned_to: \"main_agent+paper_agent\", status: done}\n    resolution: \"Commits f22d330 + 377ed61\"\n    resolution_round: 2\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"引用偏低\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n    action_items:\n      - {round: 2, action: \"补引用到 30+\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit e00d270: 31 refs\"\n    resolution_round: 2\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"Em-dash AI 写作信号\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"降为 info\"}\n    action_items:\n      - {round: 2, action: \"全文清理\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"SNR 缺数学定义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"降为 info\"}\n    action_items:\n      - {round: 2, action: \"§3.5 加 SNR 公式\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit cb05c11\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 informal\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W4 ≈ R2-W3 Round 1\"}\n    action_items:\n      - {round: 1, action: \"弱化 + SNR 数据\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Gradient-Based Motivation + SNR 5.76×\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"6.4% 延迟与 framing 矛盾\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7 Round 1\"}\n      - {round: 3, reviewers: [1, 2], note: \"再次被两位 Reviewer 独立 raise 为 critical (R1-N1-Rd3, R2-W4-Rd3)，framing 仍暗示 efficiency gain\"}\n    action_items:\n      - {round: 1, action: \"Reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 3, action: \"Abstract/Introduction 重新定位为 prediction quality + architectural simplification，明确声明无 wall-clock speedup\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Cross-arch 仅 1 点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W2 = R2-W5 Round 1\"}\n    action_items:\n      - {round: 1, action: \"6-point table\", assigned_to: \"main_agent\", status: done}\n    resolution: \"Cross-arch 6-point table\"\n    resolution_round: 2\n\n  - id: \"R2-N3\"\n    summary: \"与 SPON 区分度不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"降为 warning\"}\n    action_items:\n      - {round: 1, action: \"formalize per-token vs static KL\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"三 seed 统计效力弱\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出，R2 REBUT\"}\n      - {round: 2, reviewers: [1, 2], note: \"维持 info\"}\n      - {round: 3, reviewers: [1, 2], note: \"R1 升为 warning (R1-W3-Rd3)，R2 AGREE。JSD vs ReverseKL 差异 0.26 无 CI；multi-seed 仅 50% uniform，主结果 50% global 无方差\"}\n    action_items:\n      - {round: 3, action: \"50% global TEAL 也报告 multi-seed；考虑增加到 5 seeds\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2-W5 Round 1\"}\n    action_items:\n      - {round: 1, action: \"加 caveat\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  # ===== Round 3 新 issues =====\n\n  - id: \"R1-N1-Rd3\"\n    summary: \"无 wall-clock speedup，efficiency framing 误导\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise 并交叉 AGREE。Table 6: +6.4% overhead vs dense。Introduction 'simplify inference' 与实际矛盾\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 重新定位为 prediction quality + architectural simplification；明确声明无 wall-clock speedup\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2-Rd3\"\n    summary: \"Downstream collapse 与 PPL-centric 叙事系统性矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise 并交叉 AGREE。30% KL global MMLU=25.27% < TEAL 38.61% (-13.3pp)；50% MMLU≈random。PPL 改善不转化为 reasoning 保持\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 诚实呈现 downstream mixed results；讨论 KL 训练为何恶化 MMLU；突出 PPL-downstream disconnect 作为发现而非隐藏\", assigned_to: \"paper_agent\", status: open}\n      - {round: 3, action: \"考虑补充 10-20% sparsity downstream 评估找 practical sweet spot\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3-Rd3\"\n    summary: \"训练-推理 mask mismatch 未分析（soft Gumbel vs hard top-k）\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE with nuance（gap 主要来自 allocation strategy 非 discretization）。Table 5: per-token PPL=9.218 vs TEAL global PPL=11.963，~30% gap 未分解\"}\n    action_items:\n      - {round: 3, action: \"三向分解分析：per-token hard mask / per-token soft mask / global hard mask with oracle scores，分离 mask quality / discretization / allocation loss\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1-Rd3\"\n    summary: \"Responsible NLP Research Checklist 缺失（desk reject 风险）\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise，R1 交叉 AGREE。ARR 自 2024-12 强制要求，缺失可直接 desk reject\"}\n    action_items:\n      - {round: 3, action: \"参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写 checklist + Ethics Statement\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3-Rd3\"\n    summary: \"与 MaskLLM 核心技术重叠未充分辨析\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise 为 critical，R1 REBUT 降为 warning。R1 论证：MaskLLM 是 static N:M weight masks，无 structural mismatch 问题；本文核心贡献是 §3.5 梯度分析，在 MaskLLM 设定中不存在。但两位均同意论文讨论不足\"}\n    action_items:\n      - {round: 3, action: \"Related Work 添加专门 MaskLLM 技术对比段落：Gumbel-Softmax vs Sigmoid 原因、N:M vs global top-k 区别、为何 structural mismatch 不适用于 MaskLLM\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1-Rd3\"\n    summary: \"BCE 对比公平性：系统差异超过 loss function\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE。KL 系统=Gumbel+penalty，BCE 系统=hard mask+compensation。BCE+Gumbel+Penalty=38.02 比 vanilla BCE 27.97 更差\"}\n    action_items:\n      - {round: 3, action: \"明确说明 KL 优势来自 loss+infrastructure 组合；考虑添加 MSE on logits + Gumbel 作为 intermediate control\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2-Rd3\"\n    summary: \"'Parameter-free' penalty controller 表述不准确\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE。λ_max 在不同 target 取不同值（1000 vs 5000），30% 时达 cap 且偏差 5%\"}\n    action_items:\n      - {round: 3, action: \"去掉 'parameter-free' 措辞；讨论 λ_max 选择及 30% 偏差影响\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4-Rd3\"\n    summary: \"实验规模受限（仅 7-8B）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。两个模型 d_ff/d_model ratio 相同，Mistral 差异与 FFN sparsity 关系不大\"}\n    action_items:\n      - {round: 3, action: \"弱化 generalization claims 为 'verified on two 7-8B SwiGLU models'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1-Rd3\"\n    summary: \"三 regime 分析证据不足以支撑 claim 强度\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。2 models × 3 levels = 6 点，regime 边界泛化性未验证\"}\n    action_items:\n      - {round: 3, action: \"弱化 claim 为 empirical observation on 7-8B models\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2-Rd3\"\n    summary: \"D2DMoE (NeurIPS 2024) 遗漏\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise，R1 AGREE。应填入 taxonomy Per-token × Intermediate cell，影响 taxonomy 完整性\"}\n    action_items:\n      - {round: 3, action: \"引用 D2DMoE 并更新 Table 1 taxonomy\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3-Rd3\"\n    summary: \"Abstract 数据堆砌（25+ 个数字）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise，R1 AGREE 并量化为 25 个数字。审稿人 30s 内无法消化\"}\n    action_items:\n      - {round: 3, action: \"Abstract 精简到 3-4 个核心数字，以叙事为主\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-Rd3\"\n    summary: \"Taxonomy 可能 post-hoc rationalization\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise，R1 部分 AGREE（presentation concern 非 validity concern）。5/9 cells 空，DejaVu 在 taxonomy 中提到但 Table 2 缺失\"}\n    action_items:\n      - {round: 3, action: \"补充 DejaVu 到 Table 2 或讨论缺失原因；补充 D2DMoE 到 taxonomy；讨论轴选择依据\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6-Rd3\"\n    summary: \"训练数据过小且与评估数据同源\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise warning，R2 降为 info（C4 OOD eval 已部分缓解）。8M tokens 训练，WikiText-103/2 同源\"}\n    action_items:\n      - {round: 3, action: \"C4 补充 30%/70% 评估\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5-Rd3\"\n    summary: \"SNR 测量数据与训练数据不一致\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise warning，R2 REBUT 降为 info（C4 上测 SNR 反而表明结论跨数据分布）\"}\n    action_items:\n      - {round: 3, action: \"添加一句解释为何在 C4 上测量（跨分布验证）\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ===== Round 3 小问题 =====\n\n  - id: \"R2-M1-Rd3\"\n    summary: \"Abstract -ing 分词短语 AI 写作痕迹\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。'confirming', 'demonstrating', 'eliminating' 结尾\"}\n    action_items:\n      - {round: 3, action: \"改写 Abstract 中 -ing 结尾句\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-M2-Rd3\"\n    summary: \"Figure 1 label fig:taxonomy 与内容不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。Figure 1 是 method overview 不是 taxonomy\"}\n    action_items:\n      - {round: 3, action: \"改 label 为 fig:overview\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-M3-Rd3\"\n    summary: \"Conclusion 仅 3 行过短\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。无 future work、无 broader implications\"}\n    action_items:\n      - {round: 3, action: \"扩展 Conclusion，加 future work 和 broader implications\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M1-Rd3\"\n    summary: \"AdamW weight decay 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE\"}\n    action_items:\n      - {round: 3, action: \"§4.1 补充 weight decay 值\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M2-Rd3\"\n    summary: \"BCE oracle mask threshold 作用域不清楚\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE\"}\n    action_items:\n      - {round: 3, action: \"§3.5 明确 oracle mask 是 per-layer 还是 global top-k\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M3-Rd3\"\n    summary: \"ShadowLLM 在 Table 1 分类可能不准确\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE。ShadowLLM 用 attention-based routing 可能更接近 per-token\"}\n    action_items:\n      - {round: 3, action: \"核实 ShadowLLM 分类准确性\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ===== Round 1-2 历史 issues（已 resolved）=====\n  - id: \"R2-N1\"\n    summary: \"Limitations section 格式不合规\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"desk-reject 条件\"}\n    action_items:\n      - {round: 1, action: \"拆为独立 section*\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit 7018701\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"页数超限\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2 提出，R1 AGREE\"}\n    action_items:\n      - {round: 1, action: \"拆出 Limitations 后确认页数\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Main content p.8, total 10p\"\n    resolution_round: 1\n\n  - id: \"R1-N1\"\n    summary: \"缺 OOD PPL 评估\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 critical, R2 AGREE\"}\n    action_items:\n      - {round: 1, action: \"C4 validation PPL\", assigned_to: \"main_agent\", status: done}\n    resolution: \"C4: Dense=9.21, KL 50%=18.40, TEAL 50%=38.75\"\n    resolution_round: 1\n\n  - id: \"R1-N2\"\n    summary: \"Structural failure 证据不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"两位独立指出\"}\n    action_items:\n      - {round: 1, action: \"BCE+Gumbel ×3 LR 对照\", assigned_to: \"main_agent\", status: done}\n    resolution: \"BCE best=38.02 vs KL=11.79\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"消融缺关键维度\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 critical → 降 warning\"}\n    action_items:\n      - {round: 1, action: \"d_b/τ/steps/Lagrangian sweep\", assigned_to: \"main_agent\", status: done}\n    resolution: \"Appendix B-C 全覆盖\"\n    resolution_round: 1\n\n  - id: \"R1-W1-Rd2\"\n    summary: \"Lagrangian 术语误用\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n    action_items:\n      - {round: 2, action: \"全文术语替换\", assigned_to: \"paper_agent\", status: done}\n      - {round: 2, action: \"启发式 schedule 说明\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commits fe7c034 + e00d270\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"λ/sparsity 时序曲线缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出\"}\n      - {round: 2, reviewers: [1, 2], note: \"遗留未修复\"}\n    action_items:\n      - {round: 2, action: \"生成 + 修复 50% + 集成\", assigned_to: \"main_agent+paper_agent\", status: done}\n    resolution: \"lagrangian_dynamics.pdf 集成到 Appendix C\"\n    resolution_round: 2\n\n  - id: \"R2-W2-Rd2\"\n    summary: \"需报告 KL/Dense ratio\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}\n    action_items:\n      - {round: 2, action: \"Abstract + §4.2 添加 KL/Dense ratio\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W3-Rd2\"\n    summary: \"Scale claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"R1 AGREE\"}\n    action_items:\n      - {round: 2, action: \"加 scale qualifier\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R2-W4-Rd2\"\n    summary: \"30% MMLU 异常缺 per-layer 分析\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n    action_items:\n      - {round: 2, action: \"Per-layer retention 分析 + 叙事修正\", assigned_to: \"main_agent+paper_agent\", status: done}\n    resolution: \"Commits f22d330 + 377ed61\"\n    resolution_round: 2\n\n  - id: \"R2-W7-Rd2\"\n    summary: \"引用偏低\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"两位 AGREE\"}\n    action_items:\n      - {round: 2, action: \"补引用到 30+\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit e00d270: 31 refs\"\n    resolution_round: 2\n\n  - id: \"R2-W5-Rd2\"\n    summary: \"Em-dash AI 写作信号\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"降为 info\"}\n    action_items:\n      - {round: 2, action: \"全文清理\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit fe7c034\"\n    resolution_round: 2\n\n  - id: \"R1-W3-Rd2\"\n    summary: \"SNR 缺数学定义\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - {round: 2, reviewers: [1, 2], note: \"降为 info\"}\n    action_items:\n      - {round: 2, action: \"§3.5 加 SNR 公式\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Commit cb05c11\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"梯度分析 informal\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W4 ≈ R2-W3 Round 1\"}\n    action_items:\n      - {round: 1, action: \"弱化 + SNR 数据\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Gradient-Based Motivation + SNR 5.76×\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"6.4% 延迟与 framing 矛盾\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W1 = R2-W7 Round 1\"}\n      - {round: 3, reviewers: [1, 2], note: \"再次被两位 Reviewer 独立 raise 为 critical (R1-N1-Rd3, R2-W4-Rd3)，framing 仍暗示 efficiency gain\"}\n    action_items:\n      - {round: 1, action: \"Reframe\", assigned_to: \"paper_agent\", status: done}\n      - {round: 3, action: \"Abstract/Introduction 重新定位为 prediction quality + architectural simplification，明确声明无 wall-clock speedup\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Cross-arch 仅 1 点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1-W2 = R2-W5 Round 1\"}\n    action_items:\n      - {round: 1, action: \"6-point table\", assigned_to: \"main_agent\", status: done}\n    resolution: \"Cross-arch 6-point table\"\n    resolution_round: 2\n\n  - id: \"R2-N3\"\n    summary: \"与 SPON 区分度不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"降为 warning\"}\n    action_items:\n      - {round: 1, action: \"formalize per-token vs static KL\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"三 seed 统计效力弱\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R1 提出，R2 REBUT\"}\n      - {round: 2, reviewers: [1, 2], note: \"维持 info\"}\n      - {round: 3, reviewers: [1, 2], note: \"R1 升为 warning (R1-W3-Rd3)，R2 AGREE。JSD vs ReverseKL 差异 0.26 无 CI；multi-seed 仅 50% uniform，主结果 50% global 无方差\"}\n    action_items:\n      - {round: 3, action: \"50% global TEAL 也报告 multi-seed；考虑增加到 5 seeds\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"三 regime 仅单模型\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - {round: 1, reviewers: [1, 2], note: \"R2-W5 Round 1\"}\n    action_items:\n      - {round: 1, action: \"加 caveat\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"Round 2 未再 raise\"\n    resolution_round: 1\n\n  # ===== Round 3 新 issues =====\n\n  - id: \"R1-N1-Rd3\"\n    summary: \"无 wall-clock speedup，efficiency framing 误导\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise 并交叉 AGREE。Table 6: +6.4% overhead vs dense。Introduction 'simplify inference' 与实际矛盾\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 重新定位为 prediction quality + architectural simplification；明确声明无 wall-clock speedup\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2-Rd3\"\n    summary: \"Downstream collapse 与 PPL-centric 叙事系统性矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位独立 raise 并交叉 AGREE。30% KL global MMLU=25.27% < TEAL 38.61% (-13.3pp)；50% MMLU≈random。PPL 改善不转化为 reasoning 保持\"}\n    action_items:\n      - {round: 3, action: \"Abstract/Intro 诚实呈现 downstream mixed results；讨论 KL 训练为何恶化 MMLU；突出 PPL-downstream disconnect 作为发现而非隐藏\", assigned_to: \"paper_agent\", status: open}\n      - {round: 3, action: \"考虑补充 10-20% sparsity downstream 评估找 practical sweet spot\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3-Rd3\"\n    summary: \"训练-推理 mask mismatch 未分析（soft Gumbel vs hard top-k）\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE with nuance（gap 主要来自 allocation strategy 非 discretization）。Table 5: per-token PPL=9.218 vs TEAL global PPL=11.963，~30% gap 未分解\"}\n    action_items:\n      - {round: 3, action: \"三向分解分析：per-token hard mask / per-token soft mask / global hard mask with oracle scores，分离 mask quality / discretization / allocation loss\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1-Rd3\"\n    summary: \"Responsible NLP Research Checklist 缺失（desk reject 风险）\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise，R1 交叉 AGREE。ARR 自 2024-12 强制要求，缺失可直接 desk reject\"}\n    action_items:\n      - {round: 3, action: \"参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写 checklist + Ethics Statement\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3-Rd3\"\n    summary: \"与 MaskLLM 核心技术重叠未充分辨析\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise 为 critical，R1 REBUT 降为 warning。R1 论证：MaskLLM 是 static N:M weight masks，无 structural mismatch 问题；本文核心贡献是 §3.5 梯度分析，在 MaskLLM 设定中不存在。但两位均同意论文讨论不足\"}\n    action_items:\n      - {round: 3, action: \"Related Work 添加专门 MaskLLM 技术对比段落：Gumbel-Softmax vs Sigmoid 原因、N:M vs global top-k 区别、为何 structural mismatch 不适用于 MaskLLM\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W1-Rd3\"\n    summary: \"BCE 对比公平性：系统差异超过 loss function\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE。KL 系统=Gumbel+penalty，BCE 系统=hard mask+compensation。BCE+Gumbel+Penalty=38.02 比 vanilla BCE 27.97 更差\"}\n    action_items:\n      - {round: 3, action: \"明确说明 KL 优势来自 loss+infrastructure 组合；考虑添加 MSE on logits + Gumbel 作为 intermediate control\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2-Rd3\"\n    summary: \"'Parameter-free' penalty controller 表述不准确\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE。λ_max 在不同 target 取不同值（1000 vs 5000），30% 时达 cap 且偏差 5%\"}\n    action_items:\n      - {round: 3, action: \"去掉 'parameter-free' 措辞；讨论 λ_max 选择及 30% 偏差影响\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4-Rd3\"\n    summary: \"实验规模受限（仅 7-8B）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。两个模型 d_ff/d_model ratio 相同，Mistral 差异与 FFN sparsity 关系不大\"}\n    action_items:\n      - {round: 3, action: \"弱化 generalization claims 为 'verified on two 7-8B SwiGLU models'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1-Rd3\"\n    summary: \"三 regime 分析证据不足以支撑 claim 强度\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。2 models × 3 levels = 6 点，regime 边界泛化性未验证\"}\n    action_items:\n      - {round: 3, action: \"弱化 claim 为 empirical observation on 7-8B models\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2-Rd3\"\n    summary: \"D2DMoE (NeurIPS 2024) 遗漏\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise，R1 AGREE。应填入 taxonomy Per-token × Intermediate cell，影响 taxonomy 完整性\"}\n    action_items:\n      - {round: 3, action: \"引用 D2DMoE 并更新 Table 1 taxonomy\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3-Rd3\"\n    summary: \"Abstract 数据堆砌（25+ 个数字）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise，R1 AGREE 并量化为 25 个数字。审稿人 30s 内无法消化\"}\n    action_items:\n      - {round: 3, action: \"Abstract 精简到 3-4 个核心数字，以叙事为主\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5-Rd3\"\n    summary: \"Taxonomy 可能 post-hoc rationalization\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R2 raise，R1 部分 AGREE（presentation concern 非 validity concern）。5/9 cells 空，DejaVu 在 taxonomy 中提到但 Table 2 缺失\"}\n    action_items:\n      - {round: 3, action: \"补充 DejaVu 到 Table 2 或讨论缺失原因；补充 D2DMoE 到 taxonomy；讨论轴选择依据\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6-Rd3\"\n    summary: \"训练数据过小且与评估数据同源\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise warning，R2 降为 info（C4 OOD eval 已部分缓解）。8M tokens 训练，WikiText-103/2 同源\"}\n    action_items:\n      - {round: 3, action: \"C4 补充 30%/70% 评估\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5-Rd3\"\n    summary: \"SNR 测量数据与训练数据不一致\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise warning，R2 REBUT 降为 info（C4 上测 SNR 反而表明结论跨数据分布）\"}\n    action_items:\n      - {round: 3, action: \"添加一句解释为何在 C4 上测量（跨分布验证）\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ===== Round 3 小问题 =====\n\n  - id: \"R2-M1-Rd3\"\n    summary: \"Abstract -ing 分词短语 AI 写作痕迹\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。'confirming', 'demonstrating', 'eliminating' 结尾\"}\n    action_items:\n      - {round: 3, action: \"改写 Abstract 中 -ing 结尾句\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-M2-Rd3\"\n    summary: \"Figure 1 label fig:taxonomy 与内容不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。Figure 1 是 method overview 不是 taxonomy\"}\n    action_items:\n      - {round: 3, action: \"改 label 为 fig:overview\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-M3-Rd3\"\n    summary: \"Conclusion 仅 3 行过短\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"两位 AGREE。无 future work、无 broader implications\"}\n    action_items:\n      - {round: 3, action: \"扩展 Conclusion，加 future work 和 broader implications\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M1-Rd3\"\n    summary: \"AdamW weight decay 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE\"}\n    action_items:\n      - {round: 3, action: \"§4.1 补充 weight decay 值\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M2-Rd3\"\n    summary: \"BCE oracle mask threshold 作用域不清楚\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE\"}\n    action_items:\n      - {round: 3, action: \"§3.5 明确 oracle mask 是 per-layer 还是 global top-k\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-M3-Rd3\"\n    summary: \"ShadowLLM 在 Table 1 分类可能不准确\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - {round: 3, reviewers: [1, 2], note: \"R1 raise，R2 AGREE。ShadowLLM 用 attention-based routing 可能更接近 per-token\"}\n    action_items:\n      - {round: 3, action: \"核实 ShadowLLM 分类准确性\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-17T08:24:52.331460+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 18788}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-17T08:26:58.345725+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 3\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**目标 Venue**: EMNLP 2026 (via ARR May cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）\n**审稿模式**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）\n\n---\n\n## Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 activation sparsity predictor，核心论点是 BCE 梯度按 neuron 分解而推理时 TEAL 使用 global top-k allocation，存在\"结构性不匹配\"；KL 通过 Gumbel-Sigmoid relaxation 耦合所有 neuron 的梯度。在 LLaMA-3.1-8B 上 50% sparsity PPL 11.79 vs TEAL 23.31（无 compensation network）。跨架构验证于 Mistral-7B-v0.3。提出 2D taxonomy 和三 sparsity regime 分析。\n\n---\n\n## Strengths\n\n**S1. 梯度分析形式化清晰（§3.5）。** Factor (a)-(d) 分解严格说明 KL 和 BCE 的结构性差异：factor (b) 的 downstream Jacobian 使 KL 梯度依赖所有下游层 mask 状态。SNR 实验验证（early layer 34-156× 差异）提供定量支撑。[R1, R2 一致]\n\n**S2. Oracle F1 分析（§4.2）揭示 proxy mismatch 的深度。** BCE F1=0.613 > KL F1=0.540（+13pp），但 KL PPL 优 91%。KL 的 near-random precision (0.51) 证明它学到的 mask 与 magnitude oracle 完全不同，直接 falsify \"per-neuron accuracy = output quality\" 的隐含假设。全文最有说服力的实验。[R1, R2 一致]\n\n**S3. 消融覆盖全面。** Loss direction（Forward KL vs JSD vs Reverse KL）、relaxation（Gumbel vs STE, Δ=3.98）、loss isolation（BCE+Gumbel+Penalty=38.02，证明 penalty 与 BCE 不兼容）。Loss effect (ΔPPL=26.23) 是 relaxation effect (ΔPPL=3.98) 的 6.6×，清晰分离各组件。[R1, R2 一致]\n\n**S4. 执行质量较高。** Cross-architecture 验证一致（KL-over-TEAL ratio within 7% at ≤50%）；训练成本低（~17 min on A6000）；超参数 sensitivity 分析充分（d_b, τ, steps）。[R1, R2 一致]\n\n**S5. SPON 正交性分析（§4.5）。** Cosine similarity 0.196 + 2.4% PPL 改善定量说明 KL predictor 已捕获大部分可恢复信号。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[W-C1] Responsible NLP Research Checklist 缺失 — desk rejection 风险** [R2 raise, R1 AGREE]\n- ARR 自 2024-12 起强制要求。论文无 checklist 也无 Ethics Statement。缺失可直接 desk reject。\n- **Action**: 参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。\n\n**[W-C2] Downstream collapse 与 PPL-centric 叙事系统性矛盾** [R1, R2 独立 raise, 交叉强 AGREE]\n- 30% KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) **低 13.3pp**——KL 训练在 MMLU 上造成 active harm。\n- 50% MMLU ≈ 28%（≈ random），GSM8K < 2.2%，KL (1.29%) 比 TEAL (1.97%) 更差。\n- PPL 大幅改善（49% at 50%）完全未转化为 reasoning 保持。\n- Abstract/Introduction 以 PPL 为核心 framing，Limitations 才承认 \"PPL is poor proxy for reasoning\"——自相矛盾。\n- **Action**: (1) Abstract/Intro 诚实呈现 downstream mixed results；(2) 讨论 KL 训练为何恶化 MMLU（global top-k late-layer starvation vs loss function 本身的影响需分离）；(3) 补充 10-20% sparsity downstream 评估找 practical sweet spot。\n\n**[W-C3] 无 wall-clock speedup，efficiency framing 误导** [R1, R2 独立 raise, 交叉强 AGREE]\n- Table 6: KL predictor 50% sparsity = 126.78ms vs dense 119.11ms = **+6.4% overhead**。\n- 消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。净效果：比 dense 慢，仅比 compensation-based 方案快 2.5pp。\n- Unstructured masks 不产生 sparse computation speedup（论文自己在 Appendix A 和 Limitations 中承认）。\n- Introduction \"simplify inference by pruning 50% of FFN neurons\" 暗示效率增益，与实际矛盾。\n- **Action**: 重新定位为 prediction quality + architectural simplification；Abstract/Intro 明确声明无 wall-clock speedup。\n\n**[W-C4] 训练-推理 mask mismatch 未分析** [R1 raise, R2 AGREE with nuance]\n- Table 5 (Appendix B): d_b=128 per-token PPL=9.218 vs TEAL global PPL=11.963——~30% gap。\n- Dense (6.12) → KL-TEAL (11.79) 的全部退化（Δ=5.67）中，相当部分可能来自 allocation strategy 信息丢失，而非 sparsity capacity loss。\n- 论文从未分解这一 gap 的来源。R2 澄清 gap 主要来自 allocation strategy（per-token eval 也用 hard mask），非 soft→hard discretization。\n- **Action**: 三向分解分析（per-token hard / per-token soft / global hard with oracle scores），分离 mask quality loss、discretization loss、allocation loss。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W-S1] 与 MaskLLM 技术重叠讨论不足** [R2 raise critical, R1 REBUT → 降为 warning]\n- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。\n- R1 论证两者存在关键结构差异：MaskLLM 是 static N:M weight masks（per-group categorical, Gumbel-Softmax），本文是 per-token contextual activation masks（binary per-neuron, Gumbel-Sigmoid, global budget constraint）。MaskLLM 的设定中不存在 structural mismatch 问题。\n- **共识**：论文讨论确实不足，应添加专门 MaskLLM 技术对比段落。但\"核心技术重叠\"判断不成立——本文核心贡献是 structural mismatch 识别和梯度分析（§3.5），这在 MaskLLM 的设定中不适用。\n- **Action**: Related Work 添加 MaskLLM 深度对比。\n\n**[W-S2] BCE 对比公平性** [R1 raise, R2 AGREE]\n- KL 系统 = Forward KL + Gumbel + penalty；BCE 系统 = BCE + hard mask + compensation。不仅是 loss function 差异，是整个 pipeline 差异。\n- BCE+Gumbel+Penalty = 38.02（比 vanilla BCE 27.97 更差）说明 penalty 与 BCE 不兼容，KL 优势与 Gumbel+penalty infrastructure 不可分离。\n- **Action**: 明确说明优势来自 loss + infrastructure 组合。\n\n**[W-S3] 三 seed 统计效力不足** [R1, R2 AGREE]\n- 3 seeds 95% CI 较宽，JSD vs Reverse KL 差异 0.26 无 CI。Multi-seed 仅在 50% uniform 下做，主结果（50% global TEAL）无方差估计。\n- **Action**: 50% global TEAL 补 multi-seed。\n\n**[W-S4] 实验规模受限（仅 7-8B）** [R1, R2 AGREE]\n- 两模型 d_ff/d_model ratio 相同，Mistral 差异（GQA + sliding window）与 FFN sparsity 关系不大。\n- **Action**: 弱化 generalization claims。\n\n**[W-S5] 三 regime 分析证据不足** [R1, R2 AGREE]\n- 2 models × 3 levels = 6 数据点。Regime 边界泛化性未验证。\n- **Action**: 降为 empirical observation on 7-8B models。\n\n**[W-S6] \"Parameter-free\" penalty controller 表述不准确** [R1 raise, R2 AGREE]\n- λ_max 在不同 target 取不同值（1000 vs 5000），是 hyperparameter。30% 时达 cap 且偏差 5%。\n- **Action**: 去掉 \"parameter-free\" 措辞。\n\n**[W-S7] D2DMoE (NeurIPS 2024) 遗漏** [R2 raise, R1 AGREE]\n- 应填入 taxonomy Per-token × Intermediate cell。影响 taxonomy 完整性和 \"no prior work\" claim。\n- **Action**: 引用并更新 Table 1。\n\n**[W-S8] Abstract 数据堆砌** [R2 raise, R1 AGREE]\n- 25+ 个数字，审稿人 30s 无法消化。\n- **Action**: 精简到 3-4 个核心数字，以叙事为主。\n\n**[W-S9] Taxonomy post-hoc 质疑** [R2 raise, R1 部分 AGREE]\n- 5/9 cells 空。DejaVu 在 taxonomy 中提到但 Table 2 实验中缺失。\n- **Action**: 补充 DejaVu/D2DMoE，讨论轴选择依据。\n\n### Minor Issues（不影响接收）\n\n| ID | 问题 | 来源 |\n|----|------|------|\n| M1 | AdamW weight decay 未报告 | R1 |\n| M2 | BCE oracle mask threshold 作用域不清楚 | R1 |\n| M3 | ShadowLLM 在 Table 1 分类可能不准确（per-layer vs per-token） | R1 |\n| M4 | loshchilov2019adamw 年份不一致（2019 vs 2017） | R1 |\n| M5 | Latency 测量 GPU 与训练 GPU 不同 | R1 |\n| M6 | Abstract -ing 分词短语 AI 写作痕迹 | R2, R1 AGREE |\n| M7 | xu2026spon bib year 不一致 | R2, R1 AGREE |\n| M8 | Figure 1 label fig:taxonomy 与内容不匹配 | R2, R1 AGREE |\n| M9 | Conclusion 仅 3 行过短，无 future work | R2, R1 AGREE |\n| M10 | 训练数据小且同源（C4 OOD 已部分缓解） | R1, R2 降级 |\n| M11 | SNR 在 C4 上测量（R2 认为反而跨分布验证） | R1, R2 降级 |\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：\n1. **Downstream collapse 与 PPL framing 矛盾是最严重的问题**——30% KL global MMLU 比 TEAL 更差 13.3pp\n2. **无 wall-clock speedup**——efficiency framing 需重新定位\n3. **Responsible NLP Checklist 缺失**——desk reject 风险\n4. **Train-test mask mismatch 需分析**——per-token vs TEAL global 的 ~30% gap 未分解\n5. **实验规模有限**——仅 7-8B，regime 分析证据不足\n6. **Abstract 数据堆砌**——需精简\n7. **梯度分析和 Oracle F1 分析是最强贡献**——两位均高度评价 §3.5 和 §4.2\n\n## Reviewer Divergence\n\n**MaskLLM 技术重叠（R2-N3 vs R1 REBUT）**：\n- R2 认为核心 pipeline（KL + Gumbel + frozen weights）与 MaskLLM 相同，属 critical 新颖性问题\n- R1 认为 MaskLLM（static N:M weight masks）和本文（per-token contextual activation masks）的优化问题本质不同，structural mismatch 在 MaskLLM 设定中不存在\n- **Director 判断**：R1 的 REBUT 论证充分——MaskLLM 的 per-group categorical selection 与本文的 global budget-constrained binary prediction 是不同优化问题。降为 warning（讨论不足）而非 critical（新颖性不足）。\n\n---\n\n## Questions to Authors\n\n1. Table 5 per-token PPL=9.218 vs TEAL global PPL=11.963 的 ~30% gap 如何分解？能否提供 per-token hard mask evaluation 分离 allocation loss？\n2. 30% sparsity 下 KL global MMLU (25.27%) 比 TEAL (38.61%) 低 13.3pp。KL 训练为何在 MMLU 上造成 active harm？是 global allocation 的 late-layer starvation 还是 KL loss 本身过度偏向 PPL-dominant layers？\n3. BCE 的 learning rate、optimizer、weight decay 是否与 KL 完全一致？\n4. KL predictor 学到的 mask 与 magnitude oracle 几乎无相关（precision 0.51）——per-layer 分析能否揭示 KL mask 的具体模式？\n5. 是否尝试过 hard top-k with STE 替代 Gumbel-Sigmoid 来缩小 train-test gap？\n\n---\n\n## Missing References\n\n1. **D2DMoE** (NeurIPS 2024) — Dense-to-Dynamic-k MoE，per-token router 用 ℓ2-norm regression，应填入 taxonomy Per-token × Intermediate cell\n2. **WAS** (EMNLP 2025) — Weight-Aware Activation Sparsity（待确认完整引用信息）\n\n---\n\n## Overall Assessment\n\n**Overall Score: weak reject (3.0/5, Findings 边界)**\n**置信度: 4/5**\n\n两位 Reviewer 独立给出一致评分（R1: 3/5, R2: 3/5）。\n\n**核心判断**：论文在理论洞察（gradient coupling analysis, §3.5）和实验执行（systematic ablation, cross-arch verification）方面质量较高。Oracle F1 分析优雅地证明了\"正确目标 > 高精度代理\"这一核心论点。\n\n但三个结构性问题严重限制了论文的影响力：\n1. **PPL-downstream disconnect**: 最引人注目的改善点（50% sparsity, 49% PPL reduction）在 downstream tasks 上完全不相关（MMLU ≈ random），且 30% 时 KL 训练反而 active harm MMLU（-13.3pp vs TEAL）。论文的核心叙事建立在一个与实际应用脱节的指标上。\n2. **无实际加速**: 作为一篇以 sparsity prediction 为核心的论文，全部实验仅展示 prediction quality 而无任何 wall-clock speedup，且 framing 存在误导。\n3. **分析不完整**: per-token vs TEAL global 的 ~30% PPL gap 未分解，读者无法判断方法的 ceiling 和改进空间。\n\n如果作者能 (a) 诚实重新定位叙事（prediction understanding 而非 efficiency），(b) 补充 downstream 分析解释 PPL-MMLU disconnect，(c) 分解 train-test gap 来源，论文有潜力达到 borderline accept。当前版本适合 Findings track。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 25+ 个数字，信息密度过高（W-S8）\n- 多处 -ing 分词短语（M6）\n- 以 PPL 为核心 framing 但 downstream 讲不同故事（W-C2）\n\n### Introduction (§1)\n- \"simplify inference by pruning 50% of FFN neurons\" 暗示效率增益（W-C3）\n- 叙事线整体清晰，structural mismatch 论证有力\n- Contribution 列表第三条（三 regime 分析）claim 过强（W-S5）\n\n### Related Work (§5)\n- MaskLLM 讨论不足（W-S1）\n- D2DMoE 遗漏影响 taxonomy 完整性（W-S7）\n- ShadowLLM 分类可能不准确（M3）\n- 31 refs 数量基本达标\n\n### Method (§3)\n- 梯度分析（§3.5）是最强贡献（S1）\n- Gumbel-Sigmoid 使用正确\n- \"Parameter-free\" 表述需修正（W-S6）\n- Penalty controller footnote 与正文 \"adaptive penalty controller\" 术语一致，但 λ_max 的 hyperparameter 性质未充分讨论\n- BCE oracle mask 的 threshold 作用域不清楚（M2）\n\n### Experiments (§4)\n- Table 2 主结果清晰\n- 30% KL global MMLU 问题需要突出讨论（W-C2）\n- BCE 对比是 pipeline 差异而非仅 loss 差异（W-S2）\n- Multi-seed 缺 50% global 的方差（W-S3）\n- Cross-arch 验证有价值但 generalization claim 需弱化（W-S4）\n\n### Conclusion (§6)\n- 3 行过短（M9）\n\n### Limitations\n- 存在且独立，但 PPL-downstream disconnect 应更突出\n\n### Appendix\n- Table 5 (d_b sensitivity) 揭示了 per-token vs TEAL global 的关键 gap 但未分析（W-C4）\n- Lagrangian dynamics figure 已补充（历史 issue 已修复）\n- OOD C4 评估仅 50%，建议补充 30%/70%\n\n### Format Compliance\n- ✅ ACL template with [review] option\n- ✅ Anonymous (\\author{Anonymous})\n- ✅ Limitations section 独立\n- ❌ **Responsible NLP Research Checklist 缺失**（W-C1, desk reject 风险）\n- ❌ **Ethics Statement 缺失**\n- Figure 1 label 错误（M8）\n",
  "project": "distill_sparse_swiglu",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 3\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**目标 Venue**: EMNLP 2026 (via ARR May cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）\n**审稿模式**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）\n\n---\n\n## Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 activation sparsity predictor，核心论点是 BCE 梯度按 neuron 分解而推理时 TEAL 使用 global top-k allocation，存在\"结构性不匹配\"；KL 通过 Gumbel-Sigmoid relaxation 耦合所有 neuron 的梯度。在 LLaMA-3.1-8B 上 50% sparsity PPL 11.79 vs TEAL 23.31（无 compensation network）。跨架构验证于 Mistral-7B-v0.3。提出 2D taxonomy 和三 sparsity regime 分析。\n\n---\n\n## Strengths\n\n**S1. 梯度分析形式化清晰（§3.5）。** Factor (a)-(d) 分解严格说明 KL 和 BCE 的结构性差异：factor (b) 的 downstream Jacobian 使 KL 梯度依赖所有下游层 mask 状态。SNR 实验验证（early layer 34-156× 差异）提供定量支撑。[R1, R2 一致]\n\n**S2. Oracle F1 分析（§4.2）揭示 proxy mismatch 的深度。** BCE F1=0.613 > KL F1=0.540（+13pp），但 KL PPL 优 91%。KL 的 near-random precision (0.51) 证明它学到的 mask 与 magnitude oracle 完全不同，直接 falsify \"per-neuron accuracy = output quality\" 的隐含假设。全文最有说服力的实验。[R1, R2 一致]\n\n**S3. 消融覆盖全面。** Loss direction（Forward KL vs JSD vs Reverse KL）、relaxation（Gumbel vs STE, Δ=3.98）、loss isolation（BCE+Gumbel+Penalty=38.02，证明 penalty 与 BCE 不兼容）。Loss effect (ΔPPL=26.23) 是 relaxation effect (ΔPPL=3.98) 的 6.6×，清晰分离各组件。[R1, R2 一致]\n\n**S4. 执行质量较高。** Cross-architecture 验证一致（KL-over-TEAL ratio within 7% at ≤50%）；训练成本低（~17 min on A6000）；超参数 sensitivity 分析充分（d_b, τ, steps）。[R1, R2 一致]\n\n**S5. SPON 正交性分析（§4.5）。** Cosine similarity 0.196 + 2.4% PPL 改善定量说明 KL predictor 已捕获大部分可恢复信号。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[W-C1] Responsible NLP Research Checklist 缺失 — desk rejection 风险** [R2 raise, R1 AGREE]\n- ARR 自 2024-12 起强制要求。论文无 checklist 也无 Ethics Statement。缺失可直接 desk reject。\n- **Action**: 参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。\n\n**[W-C2] Downstream collapse 与 PPL-centric 叙事系统性矛盾** [R1, R2 独立 raise, 交叉强 AGREE]\n- 30% KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) **低 13.3pp**——KL 训练在 MMLU 上造成 active harm。\n- 50% MMLU ≈ 28%（≈ random），GSM8K < 2.2%，KL (1.29%) 比 TEAL (1.97%) 更差。\n- PPL 大幅改善（49% at 50%）完全未转化为 reasoning 保持。\n- Abstract/Introduction 以 PPL 为核心 framing，Limitations 才承认 \"PPL is poor proxy for reasoning\"——自相矛盾。\n- **Action**: (1) Abstract/Intro 诚实呈现 downstream mixed results；(2) 讨论 KL 训练为何恶化 MMLU（global top-k late-layer starvation vs loss function 本身的影响需分离）；(3) 补充 10-20% sparsity downstream 评估找 practical sweet spot。\n\n**[W-C3] 无 wall-clock speedup，efficiency framing 误导** [R1, R2 独立 raise, 交叉强 AGREE]\n- Table 6: KL predictor 50% sparsity = 126.78ms vs dense 119.11ms = **+6.4% overhead**。\n- 消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。净效果：比 dense 慢，仅比 compensation-based 方案快 2.5pp。\n- Unstructured masks 不产生 sparse computation speedup（论文自己在 Appendix A 和 Limitations 中承认）。\n- Introduction \"simplify inference by pruning 50% of FFN neurons\" 暗示效率增益，与实际矛盾。\n- **Action**: 重新定位为 prediction quality + architectural simplification；Abstract/Intro 明确声明无 wall-clock speedup。\n\n**[W-C4] 训练-推理 mask mismatch 未分析** [R1 raise, R2 AGREE with nuance]\n- Table 5 (Appendix B): d_b=128 per-token PPL=9.218 vs TEAL global PPL=11.963——~30% gap。\n- Dense (6.12) → KL-TEAL (11.79) 的全部退化（Δ=5.67）中，相当部分可能来自 allocation strategy 信息丢失，而非 sparsity capacity loss。\n- 论文从未分解这一 gap 的来源。R2 澄清 gap 主要来自 allocation strategy（per-token eval 也用 hard mask），非 soft→hard discretization。\n- **Action**: 三向分解分析（per-token hard / per-token soft / global hard with oracle scores），分离 mask quality loss、discretization loss、allocation loss。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W-S1] 与 MaskLLM 技术重叠讨论不足** [R2 raise critical, R1 REBUT → 降为 warning]\n- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。\n- R1 论证两者存在关键结构差异：MaskLLM 是 static N:M weight masks（per-group categorical, Gumbel-Softmax），本文是 per-token contextual activation masks（binary per-neuron, Gumbel-Sigmoid, global budget constraint）。MaskLLM 的设定中不存在 structural mismatch 问题。\n- **共识**：论文讨论确实不足，应添加专门 MaskLLM 技术对比段落。但\"核心技术重叠\"判断不成立——本文核心贡献是 structural mismatch 识别和梯度分析（§3.5），这在 MaskLLM 的设定中不适用。\n- **Action**: Related Work 添加 MaskLLM 深度对比。\n\n**[W-S2] BCE 对比公平性** [R1 raise, R2 AGREE]\n- KL 系统 = Forward KL + Gumbel + penalty；BCE 系统 = BCE + hard mask + compensation。不仅是 loss function 差异，是整个 pipeline 差异。\n- BCE+Gumbel+Penalty = 38.02（比 vanilla BCE 27.97 更差）说明 penalty 与 BCE 不兼容，KL 优势与 Gumbel+penalty infrastructure 不可分离。\n- **Action**: 明确说明优势来自 loss + infrastructure 组合。\n\n**[W-S3] 三 seed 统计效力不足** [R1, R2 AGREE]\n- 3 seeds 95% CI 较宽，JSD vs Reverse KL 差异 0.26 无 CI。Multi-seed 仅在 50% uniform 下做，主结果（50% global TEAL）无方差估计。\n- **Action**: 50% global TEAL 补 multi-seed。\n\n**[W-S4] 实验规模受限（仅 7-8B）** [R1, R2 AGREE]\n- 两模型 d_ff/d_model ratio 相同，Mistral 差异（GQA + sliding window）与 FFN sparsity 关系不大。\n- **Action**: 弱化 generalization claims。\n\n**[W-S5] 三 regime 分析证据不足** [R1, R2 AGREE]\n- 2 models × 3 levels = 6 数据点。Regime 边界泛化性未验证。\n- **Action**: 降为 empirical observation on 7-8B models。\n\n**[W-S6] \"Parameter-free\" penalty controller 表述不准确** [R1 raise, R2 AGREE]\n- λ_max 在不同 target 取不同值（1000 vs 5000），是 hyperparameter。30% 时达 cap 且偏差 5%。\n- **Action**: 去掉 \"parameter-free\" 措辞。\n\n**[W-S7] D2DMoE (NeurIPS 2024) 遗漏** [R2 raise, R1 AGREE]\n- 应填入 taxonomy Per-token × Intermediate cell。影响 taxonomy 完整性和 \"no prior work\" claim。\n- **Action**: 引用并更新 Table 1。\n\n**[W-S8] Abstract 数据堆砌** [R2 raise, R1 AGREE]\n- 25+ 个数字，审稿人 30s 无法消化。\n- **Action**: 精简到 3-4 个核心数字，以叙事为主。\n\n**[W-S9] Taxonomy post-hoc 质疑** [R2 raise, R1 部分 AGREE]\n- 5/9 cells 空。DejaVu 在 taxonomy 中提到但 Table 2 实验中缺失。\n- **Action**: 补充 DejaVu/D2DMoE，讨论轴选择依据。\n\n### Minor Issues（不影响接收）\n\n| ID | 问题 | 来源 |\n|----|------|------|\n| M1 | AdamW weight decay 未报告 | R1 |\n| M2 | BCE oracle mask threshold 作用域不清楚 | R1 |\n| M3 | ShadowLLM 在 Table 1 分类可能不准确（per-layer vs per-token） | R1 |\n| M4 | loshchilov2019adamw 年份不一致（2019 vs 2017） | R1 |\n| M5 | Latency 测量 GPU 与训练 GPU 不同 | R1 |\n| M6 | Abstract -ing 分词短语 AI 写作痕迹 | R2, R1 AGREE |\n| M7 | xu2026spon bib year 不一致 | R2, R1 AGREE |\n| M8 | Figure 1 label fig:taxonomy 与内容不匹配 | R2, R1 AGREE |\n| M9 | Conclusion 仅 3 行过短，无 future work | R2, R1 AGREE |\n| M10 | 训练数据小且同源（C4 OOD 已部分缓解） | R1, R2 降级 |\n| M11 | SNR 在 C4 上测量（R2 认为反而跨分布验证） | R1, R2 降级 |\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：\n1. **Downstream collapse 与 PPL framing 矛盾是最严重的问题**——30% KL global MMLU 比 TEAL 更差 13.3pp\n2. **无 wall-clock speedup**——efficiency framing 需重新定位\n3. **Responsible NLP Checklist 缺失**——desk reject 风险\n4. **Train-test mask mismatch 需分析**——per-token vs TEAL global 的 ~30% gap 未分解\n5. **实验规模有限**——仅 7-8B，regime 分析证据不足\n6. **Abstract 数据堆砌**——需精简\n7. **梯度分析和 Oracle F1 分析是最强贡献**——两位均高度评价 §3.5 和 §4.2\n\n## Reviewer Divergence\n\n**MaskLLM 技术重叠（R2-N3 vs R1 REBUT）**：\n- R2 认为核心 pipeline（KL + Gumbel + frozen weights）与 MaskLLM 相同，属 critical 新颖性问题\n- R1 认为 MaskLLM（static N:M weight masks）和本文（per-token contextual activation masks）的优化问题本质不同，structural mismatch 在 MaskLLM 设定中不存在\n- **Director 判断**：R1 的 REBUT 论证充分——MaskLLM 的 per-group categorical selection 与本文的 global budget-constrained binary prediction 是不同优化问题。降为 warning（讨论不足）而非 critical（新颖性不足）。\n\n---\n\n## Questions to Authors\n\n1. Table 5 per-token PPL=9.218 vs TEAL global PPL=11.963 的 ~30% gap 如何分解？能否提供 per-token hard mask evaluation 分离 allocation loss？\n2. 30% sparsity 下 KL global MMLU (25.27%) 比 TEAL (38.61%) 低 13.3pp。KL 训练为何在 MMLU 上造成 active harm？是 global allocation 的 late-layer starvation 还是 KL loss 本身过度偏向 PPL-dominant layers？\n3. BCE 的 learning rate、optimizer、weight decay 是否与 KL 完全一致？\n4. KL predictor 学到的 mask 与 magnitude oracle 几乎无相关（precision 0.51）——per-layer 分析能否揭示 KL mask 的具体模式？\n5. 是否尝试过 hard top-k with STE 替代 Gumbel-Sigmoid 来缩小 train-test gap？\n\n---\n\n## Missing References\n\n1. **D2DMoE** (NeurIPS 2024) — Dense-to-Dynamic-k MoE，per-token router 用 ℓ2-norm regression，应填入 taxonomy Per-token × Intermediate cell\n2. **WAS** (EMNLP 2025) — Weight-Aware Activation Sparsity（待确认完整引用信息）\n\n---\n\n## Overall Assessment\n\n**Overall Score: weak reject (3.0/5, Findings 边界)**\n**置信度: 4/5**\n\n两位 Reviewer 独立给出一致评分（R1: 3/5, R2: 3/5）。\n\n**核心判断**：论文在理论洞察（gradient coupling analysis, §3.5）和实验执行（systematic ablation, cross-arch verification）方面质量较高。Oracle F1 分析优雅地证明了\"正确目标 > 高精度代理\"这一核心论点。\n\n但三个结构性问题严重限制了论文的影响力：\n1. **PPL-downstream disconnect**: 最引人注目的改善点（50% sparsity, 49% PPL reduction）在 downstream tasks 上完全不相关（MMLU ≈ random），且 30% 时 KL 训练反而 active harm MMLU（-13.3pp vs TEAL）。论文的核心叙事建立在一个与实际应用脱节的指标上。\n2. **无实际加速**: 作为一篇以 sparsity prediction 为核心的论文，全部实验仅展示 prediction quality 而无任何 wall-clock speedup，且 framing 存在误导。\n3. **分析不完整**: per-token vs TEAL global 的 ~30% PPL gap 未分解，读者无法判断方法的 ceiling 和改进空间。\n\n如果作者能 (a) 诚实重新定位叙事（prediction understanding 而非 efficiency），(b) 补充 downstream 分析解释 PPL-MMLU disconnect，(c) 分解 train-test gap 来源，论文有潜力达到 borderline accept。当前版本适合 Findings track。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 25+ 个数字，信息密度过高（W-S8）\n- 多处 -ing 分词短语（M6）\n- 以 PPL 为核心 framing 但 downstream 讲不同故事（W-C2）\n\n### Introduction (§1)\n- \"simplify inference by pruning 50% of FFN neurons\" 暗示效率增益（W-C3）\n- 叙事线整体清晰，structural mismatch 论证有力\n- Contribution 列表第三条（三 regime 分析）claim 过强（W-S5）\n\n### Related Work (§5)\n- MaskLLM 讨论不足（W-S1）\n- D2DMoE 遗漏影响 taxonomy 完整性（W-S7）\n- ShadowLLM 分类可能不准确（M3）\n- 31 refs 数量基本达标\n\n### Method (§3)\n- 梯度分析（§3.5）是最强贡献（S1）\n- Gumbel-Sigmoid 使用正确\n- \"Parameter-free\" 表述需修正（W-S6）\n- Penalty controller footnote 与正文 \"adaptive penalty controller\" 术语一致，但 λ_max 的 hyperparameter 性质未充分讨论\n- BCE oracle mask 的 threshold 作用域不清楚（M2）\n\n### Experiments (§4)\n- Table 2 主结果清晰\n- 30% KL global MMLU 问题需要突出讨论（W-C2）\n- BCE 对比是 pipeline 差异而非仅 loss 差异（W-S2）\n- Multi-seed 缺 50% global 的方差（W-S3）\n- Cross-arch 验证有价值但 generalization claim 需弱化（W-S4）\n\n### Conclusion (§6)\n- 3 行过短（M9）\n\n### Limitations\n- 存在且独立，但 PPL-downstream disconnect 应更突出\n\n### Appendix\n- Table 5 (d_b sensitivity) 揭示了 per-token vs TEAL global 的关键 gap 但未分析（W-C4）\n- Lagrangian dynamics figure 已补充（历史 issue 已修复）\n- OOD C4 评估仅 50%，建议补充 30%/70%\n\n### Format Compliance\n- ✅ ACL template with [review] option\n- ✅ Anonymous (\\author{Anonymous})\n- ✅ Limitations section 独立\n- ❌ **Responsible NLP Research Checklist 缺失**（W-C1, desk reject 风险）\n- ❌ **Ethics Statement 缺失**\n- Figure 1 label 错误（M8）\n",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-17T08:27:03.230969+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4885
}
```

</details>

---


### Assistant

_source line 278 · 2026-05-17T08:27:09.542814+00:00_

审稿报告已投递至 Research Director。

---

**Round 3 审稿完成。**

**总评：weak reject (3.0/5, Findings 边界)**

4 个 critical 问题：
1. **Responsible NLP Checklist 缺失** — desk reject 风险
2. **Downstream collapse 与 PPL 叙事矛盾** — 30% KL global MMLU 比 TEAL 差 13.3pp，50% 全部 ≈ random
3. **无 wall-clock speedup** — +6.4% overhead，efficiency framing 误导
4. **Train-test mask mismatch 未分析** — per-token vs TEAL global ~30% PPL gap 未分解

9 个 warning 问题，11 个 minor 问题。Issue tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 279 · 2026-05-17T08:27:11.048078+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：R1 的 3 个 Must-Fix 我全部同意核心观点，6 个 Should-Fix 中同意 5 个（仅 W5 SNR 数据一致性建议降级）。两份审稿互补：R1 侧重 train-inference mismatch 和 BCE 公平性，我侧重 MaskLLM novelty 重叠和 taxonomy 问题。综合判断一致为 Findings level (3.0/5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 280 · 2026-05-17T08:27:21.588452+00:00_

审稿报告已提交给 Research Director。

**本轮审稿总结：**

- **Overall: weak reject (3.0/5, Findings 边界)**
- **4 个 Must-Fix**: Checklist 缺失(desk reject 风险)、downstream collapse 与 PPL 叙事矛盾、无 speedup + framing 误导、train-test mask mismatch 未分析
- **9 个 Should-Fix**: MaskLLM 讨论不足、BCE 对比公平性、统计效力、规模受限、regime 证据不足、parameter-free 表述、D2DMoE 遗漏、Abstract 堆砌、taxonomy post-hoc
- **11 个 Minor**: 格式/写作细节

两位 Reviewer 独立评分一致（3/5），交叉分享后在所有核心问题上收敛。唯一分歧（MaskLLM 新颖性）经 R1 充分 REBUT 后降为 warning。Issue tracker 已同步更新 26 条 issues（16 条历史 resolved + 10 条本轮新 open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 27

## Round 27

60 recorded events


### User

_source line 281 · 2026-05-17T09:01:00.738153+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-17T09:01:49.098063+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-17T09:01:49.098971+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-17T09:01:53.432312+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,director_post_to_reviewer,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,director_post_to_reviewer,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-17T09:01:53.483170+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-17T09:01:57.051337+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-17T09:01:57.051829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-17T09:02:02.375737+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-17T09:02:02.878156+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (104 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 今日完成的分析任务（全部 success 或 negative，已写入 paper）\n\n| exp_id | 结论 | 关键发现 |\n|--------|------|---------|\n| kl_bce_f1_oracle | success | BCE F1=0.613 > KL F1=0.540，但 KL PPL=11.79 远优于 BCE PPL=22.51。证明 per-neuron mask accuracy 是错误优化目标 |\n| global_30pct_retention | negative | 30% 全局 top-k 饿死 late layers (L27-31)，L31 仅 28.4% retention。原 hypothesis \"中层知识层挨饿\" 被推翻 |\n| global_50pct_retention | success | 50% 下 late layers retention 降至 0.342，knowledge layers (L12-20) 保持 0.606，确认全局分配优先喂中层 |\n| global_70pct_retention | success | 70% 下 starvation 扩散到 L10-L12（min=0.167），相变：全局分配无法同时保护中层和早期层 |\n| reverse_kl_50pct_s42 | negative | PPL=12.8 vs Forward KL=11.79（+8.6%），Forward KL 仍最优 |\n| jsd_50pct_s42 | negative | PPL=12.54 vs Forward KL=11.79（+6.4%），Forward KL 仍最优 |\n| gradient_snr_constrained | success | 带 Lagrangian 约束下 KL SNR 仍 103.2× > BCE，直接回应 R1-W5 |\n| lagrangian_dynamics_fix | success | 重新生成完整 1000-step Lagrangian 动态图（50% 数据修复） |\n| teal_kl_overlap_corrected | success | 排列检验 z=7260，确认 TEAL-KL 重叠非随机（回应选择偏差） |\n| natural_sparsity_floor_extended | success | 30/50/70% 三级自然稀疏下限分析完成 |\n\n## 产出物（已同步/待同步到本地）\n- `figures/paper/lagrangian_dynamics.pdf` — 已同步\n- `figures/paper/per_layer_retention_
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-17T09:02:04.335280+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-17T09:02:04.787921+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-17T09:02:04.788373+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 293 · 2026-05-17T09:02:04.939168+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-17T09:02:23.634450+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 295 · 2026-05-17T09:02:23.634810+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-17T09:02:24.086737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-17T09:02:25.042052+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-17T09:02:25.092887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-17T09:02:25.093735+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	We show this creates a structural mismatch: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 91\% worse perplexity, because per-neuron accuracy is a misaligned proxy for output-distribution preservation.
4	A lightweight predictor (75.9M params, $<$1\% of the base model) trained with forward KL divergence and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution.
5	On LLaMA-3.1-8B at 50\% sparsity, the KL predictor achieves PPL 11.79 vs.\ 23.31 for magnitude-based TEAL (49\% reduction), with consistent improvements on Mistral-7B-v0.3 at the 7--8B scale.
6	However, perplexity gains do not uniformly transfer to downstream tasks: global allocation starves late layers (L31 retention 28.4\%), degrading MMLU to 25.27\%, while uniform allocation recovers it to 40.61\%, comparable to TEAL's 38.61\%.
7	We identify three sparsity regimes (budget-surplus, budget-constrained, capacity-limited) that govern this allocation-quality tradeoff on 7--8B models and provide gradient coupling analysis explaining why distributional objectives outperform decomposed per-neuron losses for global budget allocation.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-17T09:02:25.646633+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-17T09:02:25.699388+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-17T09:03:02.742821+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-17T09:03:03.546561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 304 · 2026-05-17T09:03:03.999633+00:00_

1	issues:
2	  # === Round 1-2 resolved issues (compact) ===
3	  - id: "R2-N1"
4	    summary: "Limitations section 格式不合规"
5	    category: format
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 1
10	    mentions: [{round: 1, reviewers: [1, 2], note: "desk-reject 条件"}]
11	    action_items: [{round: 1, action: "拆为独立 section*", assigned_to: "paper_agent", status: done}]
12	    resolution: "Commit 7018701"
13	    resolution_round: 1
14	
15	  - id: "R2-N2"
16	    summary: "页数超限"
17	    category: format
18	    severity: critical
19	    status: resolved
20	    first_raised_round: 1
21	    last_seen_round: 1
22	    mentions: [{round: 1, reviewers: [1, 2], note: "R2 提出"}]
23	    action_items: [{round: 1, action: "确认页数", assigned_to: "paper_agent", status: done}]
24	    resolution: "8p main + 2p appendix"
25	    resolution_round: 1
26	
27	  - id: "R1-N1"
28	    summary: "缺 OOD PPL 评估"
29	    category: experiment
30	    severity: critical
31	    status: resolved
32	    first_raised_round: 1
33	    last_seen_round: 1
34	    mentions: [{round: 1, reviewers: [1, 2], note: "R1 critical"}]
35	    action_items: [{round: 1, action: "C4 validation PPL", assigned_to: "main_agent", status: done}]
36	    resolution: "C4: Dense=9.21, KL=18.40, TEAL=38.75"
37	    resolution_round: 1
38	
39	  - id: "R1-N2"
40	    summary: "Structural failure 证据不足"
41	    category: method
42	    severity: critical
43	    status: resolved
44	    first_raised_round: 1
45	    last_seen_round: 1
46	    mentions: [{round: 1, reviewers: [1, 2], note: "两位独立指出"}]
47	    action_items: [{round: 1, action: "BCE+Gumbel ×3 LR 对照", assigned_to: "main_agent", status: done}]
48	    resolution: "BCE best=38.02 vs KL=11.79"
49	    resolution_round: 1
50	
51	  - id: "R1-N3"
52	    summary: "消融缺关键维度"
53	    category: experiment
54	    severity: warning
55	    status: resolved
56	    first_raised_round: 1
57	    last_seen_round: 1
58	    mentions: [{round: 1, reviewers: [1, 2], no
…[truncated 13458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-17T09:03:04.050448+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-17T09:03:04.502721+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 91\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preserv
…[truncated 2412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 307 · 2026-05-17T09:03:04.503151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 308 · 2026-05-17T09:03:04.956676+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 14119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-17T09:03:04.957186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-17T09:03:05.459944+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25
…[truncated 14147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-17T09:03:05.510856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-17T09:03:05.561644+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision, providing intermediate coupling within each layer but no end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
14	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
15	The structural mismatch we identify (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns
…[truncated 2398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-17T09:03:11.907376+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on my search results, here's a comprehensive overview of the EMNLP 2026 call for papers submission guidelines and author instructions:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. In addition to traditional research results, papers may contribute negative
…[truncated 1948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 9164
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-17T09:03:19.648009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-17T09:03:20.055401+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that KL distillation resolves the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation in SwiGLU sparsity prediction.
5	The coupled gradient signal enables a lightweight predictor (75.9M params, $<$1\% of base) to achieve PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, with consistent improvements on both LLaMA-3.1-8B and Mistral-7B-v0.3 (within 7\% ratio consistency at $\leq$50\% sparsity).
6	Regime analysis reveals that allocation strategy, not predictor quality, is the primary bottleneck for downstream tasks: global top-$k$ starves late layers, degrading MMLU, while uniform allocation recovers performance comparable to TEAL.
7	
8	Two directions remain open.
9	First, allocation-aware training (jointly optimizing the predictor and per-layer budgets) could address late-layer starvation without sacrificing the perplexity advantages of global selection.
10	Second, evaluating at larger scales (13B--70B) and with structured sparsity patterns that enable wall-clock speedup would determine the practical deployment value of distributional training for sparsity prediction.
11	
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 407
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-17T09:03:20.055759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-17T09:03:20.507835+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
7	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-17T09:03:20.508372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-17T09:03:21.010758+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$17 minutes on a single GPU), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText and C4 are public
…[truncated 1802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-17T09:03:21.011177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-17T09:03:21.563651+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 8907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-17T09:03:21.564445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-17T09:03:22.418691+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 12601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-17T09:03:22.419225+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit template requirements site:aclweb.org OR site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission format page limit template requirements site:aclweb.org OR site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-17T09:03:28.197358+00:00_

Web search results for query: "EMNLP 2026 ARR submission format page limit template requirements site:aclweb.org OR site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"}]

Based on the search results, I found information about EMNLP 2026 submission policies. Here's what I found regarding ARR submission for EMNLP 2026:

## Key EMNLP 2026 ARR Submission Information

For the ARR 2026 May cycle aligned with EMNLP, authors must explicitly declare which conference they intend
…[truncated 1057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5778
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-17T09:03:43.161340+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long paper short paper template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long paper short paper template"
  }
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-17T09:03:43.765250+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-17T09:03:54.668491+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long paper short paper template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's the information about ACL Rolling Review 2026 submission format, page limits, and templates:

## Page Limits

Long papers may have up to eight (8) pages of content plus unlimited pages for references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

ACL currently requires all submissions to have a section titled
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 11507
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-17T09:03:54.669562+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 48\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 C
…[truncated 10971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10904
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-17T09:03:59.491519+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 responsible NLP research checklist ARR submission requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 responsible NLP research checklist ARR submission requirements"
  }
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-17T09:04:02.253912+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml 2>/dev/null || echo \"not found in constraints.yaml\"; grep -rn \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.yaml 2>/dev/null || echo \"not found\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml 2>/dev/null || echo \"not found in constraints.yaml\"; grep -rn \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.yaml 2>/dev/null || echo \"not found\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-17T09:04:02.405189+00:00_

not found in constraints.yaml
not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-17T09:04:06.423088+00:00_

Web search results for query: "ACL Rolling Review 2026 responsible NLP research checklist ARR submission requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Responsible NLP Research checklist","url":"http://aclrollingreview.org/responsibleNLPresearch/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Responsible NLP Research Checklist","url":"https://aclrollingreview.org/static/responsibleNLPresearch.pdf"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's information about ACL Rolling Review 2026 responsible NLP research checklist and ARR submission requirements:

## Responsible NLP Research Checklist Requirements

Authors must complete a responsible NLP research checklist as part of their paper submission, with the content of checklists being used in the review process, and incorrect, incomplete or misleading information in the checklist potentially res
…[truncated 1276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6931
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-17T09:04:11.797216+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -20; echo \"---\"; grep -rn \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/config/ 2>/dev/null | head -20",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -20; echo \"---\"; grep -rn \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/config/ 2>/dev/null | head -20",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-17T09:04:11.948227+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-17T09:05:14.536232+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 `[review]`，Long paper 8 页正文 + 无限引用页\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计页数，位于 conclusion 之后 references 之前\n- **Responsible NLP Checklist**: 必填，错误/遗漏可 desk reject\n- **附录**: 允许，在 references 之后，双栏\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- §3.5 梯度分析（BCE vs KL gradient structure）的数学正确性——chain rule 推导、因子分解是否严谨\n- §3.4 Adaptive Penalty Controller 的收敛保证——multiplicative schedule 的理论依据、与 formal Lagrangian 的区别是否充分说明\n- Gumbel-Sigmoid relaxation 在 train-inference mismatch 下的影响分析是否充分\n- \"structural mismatch\" claim 的证据链是否完整（gradient analysis → oracle F1 → PPL gap）\n\n### 2. 实验设计与公平性\n- KL vs BCE 对比的公平性：是否存在 pipeline 差异（loss 以外的变量未控制）\n- Iso-compute analysis 是否充分（2700 steps BCE vs 1000 steps KL）\n- 统计效力：3-seed 评估的充分性，报告的 std=0.07 是否覆盖关键结论\n- Cross-architecture validation（仅 LLaMA-8B + Mistral-7B）的范围是否支撑 claim\n- Downstream evaluation：MMLU 25.27% 与 PPL 改善的 disconnect 是否充分解释\n\n### 3. 消融完整性\n- Table 3 ablation：是否所有关键设计选择都被隔离\n- Regime analysis（3 regimes, 6 data points）：证据是否支撑 \"regime\" 级别的 claim\n- Gap decomposition（53% predictor error vs 47% allocation loss）的方法论\n\n### 4. 技术细节\n- Training setup（WikiText-103, 1000 steps, seq_len=2048, batch=4）是否 standard/sufficient\n- Inference protocol：predictor-TEAL 与 vanilla TEAL 的精确对应关系\n- Appendix 数据与正文 claim 的一致性\n\n请按 ACL reviewer guidelines 格式输出完整审稿报告：Summary, Strengths, Weaknesses (逐条编号，标注 severity: critical/warning/info), Questions, Missing References, Overall Assessment (score + confidence)。\n\n**审查标准**：像顶会最严格的审稿人一样评估。不留情面。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 `[review]`，Long paper 8 页正文 + 无限引用页\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计页数，位于 conclusion 之后 references 之前\n- **Responsible NLP Checklist**: 必填，错误/遗漏可 desk reject\n- **附录**: 允许，在 references 之后，双栏\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- §3.5 梯度分析（BCE vs KL gradient structure）的数学正确性——chain rule 推导、因子分解是否严谨\n- §3.4 Adaptive Penalty Controller 的收敛保证——multiplicative schedule 的理论依据、与 formal Lagrangian 的区别是否充分说明\n- Gumbel-Sigmoid relaxation 在 train-inference mismatch 下的影响分析是否充分\n- \"structural mismatch\" claim 的证据链是否完整（gradient analysis → oracle F1 → PPL gap）\n\n### 2. 实验设计与公平性\n- KL vs BCE 对比的公平性：是否存在 pipeline 差异（loss 以外的变量未控制）\n- Iso-compute analysis 是否充分（2700 steps BCE vs 1000 steps KL）\n- 统计效力：3-seed 评估的充分性，报告的 std=0.07 是否覆盖关键结论\n- Cross-architecture validation（仅 LLaMA-8B + Mistral-7B）的范围是否支撑 claim\n- Downstream evaluation：MMLU 25.27% 与 PPL 改善的 disconnect 是否充分解释\n\n### 3. 消融完整性\n- Table 3 ablation：是否所有关键设计选择都被隔离\n- Regime analysis（3 regimes, 6 data points）：证据是否支撑 \"regime\" 级别的 claim\n- Gap decomposition（53% predictor error vs 47% allocation loss）的方法论\n\n### 4. 技术细节\n- Training setup（WikiText-103, 1000 steps, seq_len=2048, batch=4）是否 standard/sufficient\n- Inference protocol：predictor-TEAL 与 vanilla TEAL 的精确对应关系\n- Appendix 数据与正文 claim 的一致性\n\n请按 ACL reviewer guidelines 格式输出完整审稿报告：Summary, Strengths, Weaknesses (逐条编号，标注 severity: critical/warning/info), Questions, Missing References, Overall Assessment (score + confidence)。\n\n**审查标准**：像顶会最严格的审稿人一样评估。不留情面。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-17T09:05:36.055551+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21519
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-17T09:05:36.207230+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 `[review]`，Long paper 8 页正文 + 无限引用页\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计页数，位于 conclusion 之后 references 之前\n- **Responsible NLP Checklist**: 必填，错误/遗漏可 desk reject\n- **附录**: 允许，在 references 之后，双栏\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）\n\n## 你的审查侧重\n\n### 1. Contribution Novelty\n- 核心 contribution（KL distillation for activation sparsity prediction）的新颖性：MaskLLM 已用 Gumbel + KL + frozen weights 做 weight sparsity，本文在 activation sparsity 上的 delta 是否足够\n- \"structural mismatch\" 分析：是 novel insight 还是 well-known 的 BCE-vs-end-to-end 对比的直接应用\n- Taxonomy (Table 1) 的贡献价值：是 post-hoc organization 还是 predictive framework\n- 三 regime 分析的新颖性：budget-surplus/constrained/limited 划分是否有独立价值\n\n### 2. Related Work 覆盖\n- 引用数量（31 篇）对 EMNLP 是否充足\n- 遗漏的重要工作（特别是 activation sparsity 领域近期 2024-2026 论文）\n- MaskLLM 对比是否充分区分——两者 share \"frozen weights + learnable masks + KL training\" 的高层框架\n- D2DMoE 在 taxonomy 中的 positioning 是否准确（MSE 是否真的只是 intermediate coupling）\n- 是否遗漏 dynamic sparsity prediction 的其他工作\n\n### 3. Framing 一致性\n- Abstract → Introduction → Method → Experiments → Conclusion 的主线是否统一\n- PPL 改善 vs downstream degradation 的叙事处理：是否存在过度宣传 PPL 结果而淡化 MMLU 问题\n- \"mechanistic understanding\" framing vs \"efficiency\" framing：论文是否清楚定位自己\n- Wall-clock speedup 缺失的处理方式——是否在 Introduction 给读者正确预期\n- Contribution list 每条是否有对应 evidence\n\n### 4. 写作质量\n- AI 写作痕迹检查：em-dash（—）、en-dash（–）解释性使用、-ing 短语结尾、过度分段\n- 专有名词首次定义\n- 段落过渡自然度\n- Figure/Table caption 自包含性\n- 数字堆砌 vs 叙事驱动\n\n### 5. 格式合规\n- 页数（正文 8 页限制）\n- Limitations section 格式和位置\n- Responsible NLP Research Checklist 完整性和正确性\n- Ethics Statement\n- 匿名化（是否有 de-anonymization 风险）\n- 引用格式（natbib/ACL style）\n- 附录双栏格式\n\n请按 ACL reviewer guidelines 格式输出完整审稿报告：Summary, Strengths, Weaknesses (逐条编号，标注 severity: critical/warning/info), Questions, Missing References, Overall Assessment (score + confidence)。\n\n**审查标准**：像顶会最严格的审稿人一样评估。不留情面。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 `[review]`，Long paper 8 页正文 + 无限引用页\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计页数，位于 conclusion 之后 references 之前\n- **Responsible NLP Checklist**: 必填，错误/遗漏可 desk reject\n- **附录**: 允许，在 references 之后，双栏\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）\n\n## 你的审查侧重\n\n### 1. Contribution Novelty\n- 核心 contribution（KL distillation for activation sparsity prediction）的新颖性：MaskLLM 已用 Gumbel + KL + frozen weights 做 weight sparsity，本文在 activation sparsity 上的 delta 是否足够\n- \"structural mismatch\" 分析：是 novel insight 还是 well-known 的 BCE-vs-end-to-end 对比的直接应用\n- Taxonomy (Table 1) 的贡献价值：是 post-hoc organization 还是 predictive framework\n- 三 regime 分析的新颖性：budget-surplus/constrained/limited 划分是否有独立价值\n\n### 2. Related Work 覆盖\n- 引用数量（31 篇）对 EMNLP 是否充足\n- 遗漏的重要工作（特别是 activation sparsity 领域近期 2024-2026 论文）\n- MaskLLM 对比是否充分区分——两者 share \"frozen weights + learnable masks + KL training\" 的高层框架\n- D2DMoE 在 taxonomy 中的 positioning 是否准确（MSE 是否真的只是 intermediate coupling）\n- 是否遗漏 dynamic sparsity prediction 的其他工作\n\n### 3. Framing 一致性\n- Abstract → Introduction → Method → Experiments → Conclusion 的主线是否统一\n- PPL 改善 vs downstream degradation 的叙事处理：是否存在过度宣传 PPL 结果而淡化 MMLU 问题\n- \"mechanistic understanding\" framing vs \"efficiency\" framing：论文是否清楚定位自己\n- Wall-clock speedup 缺失的处理方式——是否在 Introduction 给读者正确预期\n- Contribution list 每条是否有对应 evidence\n\n### 4. 写作质量\n- AI 写作痕迹检查：em-dash（—）、en-dash（–）解释性使用、-ing 短语结尾、过度分段\n- 专有名词首次定义\n- 段落过渡自然度\n- Figure/Table caption 自包含性\n- 数字堆砌 vs 叙事驱动\n\n### 5. 格式合规\n- 页数（正文 8 页限制）\n- Limitations section 格式和位置\n- Responsible NLP Research Checklist 完整性和正确性\n- Ethics Statement\n- 匿名化（是否有 de-anonymization 风险）\n- 引用格式（natbib/ACL style）\n- 附录双栏格式\n\n请按 ACL reviewer guidelines 格式输出完整审稿报告：Summary, Strengths, Weaknesses (逐条编号，标注 severity: critical/warning/info), Questions, Missing References, Overall Assessment (score + confidence)。\n\n**审查标准**：像顶会最严格的审稿人一样评估。不留情面。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-17T09:05:37.565651+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1358
}
```

</details>

---


### Assistant

_source line 340 · 2026-05-17T09:05:45.697939+00:00_

两位 Reviewer 已分配任务，正在独立审稿中：

| Reviewer | 审查侧重 | 状态 |
|----------|---------|------|
| R1 | 方法严谨性 + 实验设计 | 审稿中 |
| R2 | 新颖性 + 完整性 | 审稿中 |

等待 Reviewer 报告返回后进入交叉分享环节（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 341 · 2026-05-17T09:23:29.059662+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

## 总体评分

**Overall**: 2.5 (Borderline Findings)
**一句话总结**: 技术思路清晰但新颖性有限（核心框架与 MaskLLM 高度重叠），且主打的效率动机被实际 6.4% overhead 和 downstream collapse 严重削弱。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 梯度分析和 ablation 设计合理，但 PPL-centric 评估掩盖了 downstream collapse（§4.2 Table 2: MMLU 25-28%），且无 wall-clock speedup |
| Excitement | 2/5 | 核心贡献（frozen weights + Gumbel + KL training）与 MaskLLM 共享高层框架，novelty delta 有限；structural mismatch 分析可预测 |
| Reproducibility | 4/5 | 超参完整报告，3-seed 验证，训练成本低（17min），但代码未释放 |
| Confidence | 4/5 | 该领域是我的核心研究方向 |

---

## Summary

本文提出用 forward KL 蒸馏替代传统 BCE 来训练 SwiGLU LLM 的 activation sparsity predictor。核心论点是 BCE 的 per-neuron 梯度与全局 top-k 推理分配存在结构性不匹配（structural mismatch），而 KL 目标通过计算图耦合所有神经元。方法在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上评测，PPL 改善显著（50% sparsity: 11.79 vs TEAL 23.31），但 downstream tasks 严重退化（MMLU 降至 25-28%，近乎随机）。论文还提出一个 2D 分类体系（Table 1）和三个 sparsity regime 的分析。

---

## 主要优势

**S1. 清晰的梯度分析框架**
§3.6 对 BCE vs KL 梯度结构的形式化分析（Eq. 7-10）思路清楚。将 KL 梯度分解为 4 个 factor，用 SNR 实验验证（早期层 34-156× 优势），构成了论文的分析核心。这部分写作紧凑、论证有力。

**S2. 系统的 ablation 设计**
Table 3 的 ablation 覆盖了关键变量：Gumbel vs STE（+3.98 PPL）、forward vs reverse vs JSD KL、loss function isolation（BCE+Gumbel+Penalty = 38.02, 证明不是组件的简单组合）。每个 ablation 都有独立实验 ID，可溯源。

**S3. 诚实报告负面结果**
论文没有回避 downstream collapse（§4.5 Table 5: MMLU 25-28%、GSM8K < 2.2%），并尝试给出机制性解释（late-layer starvation, L31 retention 28.4%）。三 regime 分析虽不深但方向正确。

**S4. 跨架构一致性**
Table 7 在 Mistral-7B-v0.3 上验证了 KL/TEAL advantage ratio 的一致性（≤50% sparsity 内 7% 偏差），增强了结论的泛化性。

**S5. 写作质量**
全文无 AI 写作典型标志（无 em-dash、无 en-dash 解释性使用、无 -ing 结尾短语），段落过渡自然，数学符号一致。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心新颖性不足：与 MaskLLM 的区分过于薄弱

- 具体位置：§2 Related Work (lines 13-16), Table 1
- 问题：MaskLLM (Fang et al., NeurIPS 2024) 的高层框架与本文几乎完全一致：frozen base model weights + learnable masks + Gumbel relaxation + KL divergence training。论文在 §2 (related_work.tex:13-15) 声称区别在于 "weight vs activation sparsity" 和 "static N:M vs dynamic per-token"。但这本质上是将一个已被验证有效的训练范式（MaskLLM）应用到一个不同的 sparsity type，属于 application-level 的迁移而非方法论创新。
- 论文声称 "The structural mismatch we identify (per-neuron gradient decomposition vs. global top-k) does not arise in MaskLLM's per-group categorical setting"（related_work.tex:15），但这恰恰说明 structural mismatch 分析是 task-specific 的适配，而非通用性洞察。
- 为什么影响接收：对于 EMNLP，novelty bar 要求方法有清晰的 conceptual advance。当前的 delta（从 weight sparsity 搬到 activation sparsity）更适合作为 MaskLLM 的 follow-up 或 extension，而非独立 contribution。
- 建议修改方向：(1) 深入对比 MaskLLM 在 activation sparsity 设定下的表现（如果 MaskLLM 的方法直接迁移到 activation sparsity 效果如何？）；(2) 明确论证为什么 activation sparsity 的 per-token dynamic 特性带来了 MaskLLM 框架中不存在的技术挑战。

**N2** [critical] 实际推理无加速，效率动机不成立

- 具体位置：Appendix A (Table 8), §4.5 最后两段, Limitations §
- 问题：论文以 inference efficiency 为核心动机（title 中的 "Sparsity Prediction" 暗示加速），但 Table 8 明确显示 pipeline 增加 6.4% overhead（126.78 vs 119.11 ms/fwd），因为 unstructured element-wise masks 无法利用硬件稀疏加速。这意味着 50% 的神经元被 "pruned" 但推理实际更慢。
- Appendix A (appendix.tex:32-33) 坦承 "the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup"，但 Introduction 和 Abstract 没有给读者这一预期。Abstract (abstract.tex:5) 的 "49% reduction" PPL 结果容易让读者误认为有速度提升。
- 为什么影响接收：没有 wall-clock speedup 的 sparsity prediction 方法，其实际价值严重受限。审稿人和读者的第一个问题就会是 "so what's the point?"
- 建议修改方向：(1) 在 Abstract 和 Introduction 明确声明本文聚焦 prediction quality / mechanistic understanding，而非 end-to-end speedup；(2) 或者实现 structured (N:M) sparsity variant 以展示实际加速潜力。

**N3** [critical] PPL-centric 叙事掩盖 downstream collapse 的严重性

- 具体位置：Abstract (abstract.tex:5-6), Table 2, Table 5
- 问题：Abstract 中 headline result 是 "PPL 11.79 vs 23.31 (49% reduction)"，downstream collapse 被放在之后用 "However" 引出。但实际数据显示：
  - 30% sparsity, KL global: MMLU 25.27%（dense 65.27%，降 40pp，近乎随机）
  - 50% sparsity: MMLU 27.89%, GSM8K 1.29%（完全失效）
  - 即使 uniform allocation: 50% sparsity MMLU 仍为 27.77%
  - 唯一 MMLU "可用" 的配置是 30% uniform (40.61%)，但这仍比 dense 低 24.7pp
- 论文 §4.5 试图将问题归因于 "allocation strategy rather than KL training quality"，但 KL global 是论文的 primary inference protocol（experiments.tex:18-19），而 KL global 在所有设置下 MMLU 都很差。
- 为什么影响接收：一个让模型在 MMLU 上从 65% 降到 25% 的方法，仅以 PPL 改善为 headline，存在 overclaiming 风险。ARR guidelines 明确列出 "R4: overclaiming or misleading framing" 为需要关注的问题。
- 建议修改方向：(1) Abstract 中 equal prominence 地报告 PPL 改善和 downstream degradation；(2) 重新定位 30% uniform 为推荐配置而非 50% global；(3) 讨论 PPL vs downstream 的 disconnect 作为核心发现而非附带观察。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Structural mismatch" 洞察的新颖性可质疑

- 具体位置：§3.6, Introduction (introduction.tex:6-15)
- 问题：end-to-end 目标优于 decomposed per-component 目标，这是深度学习的基本原则（从 joint training vs pipeline training 以来）。论文将 "BCE per-neuron gradient 独立，KL 通过 Jacobian 耦合所有神经元" 包装为 novel insight，但这本质上是 "end-to-end loss 能捕获组件间交互" 的直接推论。
- SNR 实验（method.tex:151-153）验证了梯度差异的存在，但不构成对差异的解释——为什么 KL 更好基本上是 "因为它是 end-to-end 的"，这并不意外。
- 建议：降低 "structural mismatch" 在叙事中的权重，或提供 non-obvious 的定量 prediction（如：预测在什么条件下 BCE 可以接近 KL，并实验验证）。

**W2** [warning] Taxonomy (Table 1) 贡献价值有限

- 具体位置：§3.7, Table 1
- 问题：2D taxonomy（correction granularity × training signal coupling）是 post-hoc organization。两个轴在阅读完论文后显而易见：一个是 "mask 是否依赖 input"（static vs per-token），另一个是 "loss 是否 end-to-end"（decomposed/intermediate/coupled）。Taxonomy 没有做出可验证的预测（如 "unexplored cell 应该优于其他 cell"），也没有揭示非显然的关系。
- Table 1 的 "Static × Decomposed" 和 "Static × Intermediate" 是空的（marked as ---），但论文没有讨论为什么这些 cell 是空的或不可行的。
- 建议：要么给出 taxonomy 的 predictive power（如：沿 coupling 轴预测性能排序并验证），要么降低其在 contribution list 中的位置。

**W3** [warning] 三 regime 分析数据点过少

- 具体位置：§4.5, Table 5
- 问题：Budget-surplus/constrained/limited 三个 regime 的划分基于 3 个 sparsity level（30%, 40%, 50%）在 2 个模型上的观察。这不足以支撑 "regime" 级别的 claim：
  - 30% → 40% 之间 MMLU preference 翻转（global 从 25.27% 到 38.06%），但没有中间点（如 35%）来确认边界
  - "Capacity-limited (≥50%)" 只有 50% 一个数据点在 downstream 指标上
  - 70% 的 downstream 数据完全缺失（Table 4 只有 PPL）
- 建议：(1) 增加 35%, 45%, 60% 等中间点；(2) 或者将措辞从 "three regimes" 降级为 "preliminary observations"。

**W4** [warning] Related work 遗漏重要引用

- 具体位置：§2 Related Work
- 遗漏工作列表：
  1. **MiniLLM** (Gu et al., ICLR 2024): 直接讨论了 forward vs reverse KL 在 LLM 蒸馏中的对比，与本文 §4.3 ablation (forward KL vs reverse KL) 直接相关。MiniLLM 认为 reverse KL 优于 forward KL（与本文结论相反），需要讨论为什么在 sparsity prediction 设定下结论翻转。
  2. **SVD Contextual Sparsity Predictors** (arxiv 2603.14110, March 2026): Training-free 的 contextual sparsity prediction，用 SVD of gate projection 作为 predictor。虽然发表时间可能在投稿截止之后，但如果在 3 个月窗口内应提及。
  3. **SparseLoRA** (ICML 2025): Contextual sparsity for fine-tuning，与本文 contextual sparsity prediction 主题直接相关。
  4. 论文缺少与 broader LLM distillation 文献的连接——仅引用了 Hinton (2015) 和 Kim & Rush (2016) 作为蒸馏基础，忽略了 2023-2025 期间 LLM-specific distillation 的大量工作。
- 32 篇引用对于 EMNLP long paper 偏少（typical: 40-60）。

**W5** [warning] D2DMoE 在 taxonomy 中的 positioning 需要更细致

- 具体位置：Table 1, §3.7 (method.tex:186)
- 问题：D2DMoE (Szatkowski et al., NeurIPS 2024) 被归类为 "Intermediate (MSE)"，但 D2DMoE 的训练实际包含 router training 和 expert conversion，不仅仅是 MSE on hidden states。将其简单归为 "intermediate coupling" 可能过度简化了 D2DMoE 的训练信号结构。论文没有验证 D2DMoE 在本文的评测设定下的表现作为 baseline。
- 建议：核实 D2DMoE 的具体训练目标，如果其 routing 机制包含了 end-to-end 信号，应更新 taxonomy 分类。

**W6** [warning] Training/evaluation domain overlap

- 具体位置：§4.1 (experiments.tex:10-15)
- 问题：在 WikiText-103 上训练，在 WikiText-2 上评测 PPL。虽然 Appendix D 有 C4 OOD 评测（PPL 18.40 vs TEAL 38.75），但主表（Table 2）的 headline 数字全部基于 in-domain 评测。C4 上的 PPL 18.40 比 WikiText-2 的 11.79 高 56%，暗示 in-domain 评测高估了方法优势。
- 建议：将 C4 OOD 结果放入主表或至少在正文 §4.2 中并行报告。

**W7** [warning] Framing 不一致：mechanistic understanding vs efficiency

- 具体位置：Abstract, Introduction, Conclusion
- 问题：Abstract 和 Introduction 用 "structural mismatch" 和 "gradient coupling analysis" 包装为 mechanistic understanding，但 Conclusion (conclusion.tex:9-10) 又提到 "wall-clock speedup" 和 "practical deployment value" 作为 future directions。论文在 "understanding paper" 和 "systems paper" 之间摇摆，导致定位模糊。
- 建议：选择一个主定位并一以贯之。如果是 understanding paper，减少效率叙事；如果是 efficiency paper，需要 wall-clock 数据。

---

## 小问题（不影响接收）

- **P1** [info] experiments.tex:103 SPON 分析使用了不同的 evaluation protocol（evaluate.py vs unified benchmark），脚注说明了但容易遗漏。建议统一或更显著标注。
- **P2** [info] §4.1 training 仅 1000 steps，但 Appendix C Table 12 显示 800 和 1000 steps PPL 差异 < 0.001。建议在正文提到 early saturation 作为 efficiency 优势。
- **P3** [info] Table 2 caption 中 "BCE uses a different inference protocol (hard mask + compensation network)" 放在 caption 中不够显眼，考虑到 BCE 行使用完全不同的 inference pipeline，应在正文讨论公平性。
- **P4** [info] bib 中 `xu2026spon` 的 key 用 2026 但实际 venue 是 ICML 2025（bib year = 2025），key 和 year 不一致。
- **P5** [info] 论文声称 predictor 是 "lightweight (75.9M params, <1% of base)"，但 75.9M 仍然不小——接近 DistilBERT 的规模。"lightweight" 的标准应更明确。

---

## Questions to Authors

**Q1.** MaskLLM 的核心框架（frozen weights + Gumbel + KL）直接迁移到 per-token activation sparsity prediction 的效果如何？是否做过这个实验？如果 MaskLLM 的方法在 activation sparsity 上同样有效，本文的 novelty claim 如何成立？

**Q2.** 30% sparsity + global allocation 下 MMLU = 25.27%，但 uniform allocation 恢复到 40.61%。这是否说明 KL predictor 与 TEAL 的 global top-k 存在根本性不兼容？如果推荐用 uniform allocation，为什么还要强调 global allocation 的 PPL 优势？

**Q3.** 论文用 forward KL 并声称优于 reverse KL（Table 3: 11.79 vs 12.80）。但 MiniLLM (Gu et al., ICLR 2024) 在 LLM distillation 中系统性地证明 reverse KL 优于 forward KL。能否解释这一矛盾？是 sparsity prediction 和 model distillation 的任务差异导致的吗？

**Q4.** Wall-clock 没有加速（Table 8: +6.4% overhead）。在什么硬件/kernel 条件下，本方法的 unstructured sparsity 能实现实际加速？有没有对 N:M structured variant 的初步结果？

**Q5.** 三 regime 的边界在哪里？30% 是 surplus，40% 是 constrained，50% 是 limited，但 35% 和 45% 属于哪个 regime？这些边界是 model-specific 的还是 universal 的？

---

## Missing References

1. Gu et al., "MiniLLM: Knowledge Distillation of Large Language Models", ICLR 2024 — forward vs reverse KL for LLM distillation
2. SVD Contextual Sparsity Predictors, arxiv 2603.14110, March 2026 — training-free contextual sparsity prediction（时间窗口内可能需要引用）
3. SparseLoRA, ICML 2025 — contextual sparsity for fine-tuning
4. Broader LLM distillation literature 2023-2025（GKD, DistiLLM 等）

---

## Overall Assessment

**Score: 2.5 / 5 (Borderline Findings)**
**Confidence: 4 / 5**

本文的核心贡献（KL + Gumbel 训练 activation sparsity predictor）在技术上是 sound 的，但新颖性有限。最关键的问题有三个：

1. **与 MaskLLM 的区分不够**：共享 frozen weights + Gumbel + KL 的高层框架，本文的 delta 是从 weight sparsity 迁移到 activation sparsity，这是 application-level transfer 而非 conceptual advance。

2. **效率动机与实际结果不匹配**：以 sparsity prediction 为题暗示推理加速，但实际增加 6.4% overhead，且 unstructured masks 无法利用硬件稀疏加速。

3. **PPL 改善 vs downstream collapse 的叙事不平衡**：headline 是 "49% PPL reduction"，但在同一设置下 MMLU 从 65% 降到 25%。论文试图用 allocation strategy 解释，但 global allocation 是论文自己的 primary inference protocol。

如果论文能 (1) 深入实验性地区分与 MaskLLM 的差异、(2) 重新定位为 mechanistic understanding 而非 efficiency、(3) 诚实地将 downstream degradation 提升为核心发现，可能达到 Findings 水平。当前版本的 claim 超出了 evidence 的支撑范围。

Strengths 中梯度分析框架和 ablation 设计值得肯定，但不足以独立支撑 conference acceptance。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 342 · 2026-05-17T09:23:43.560341+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 343 · 2026-05-17T09:23:46.053426+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：评分 **2.5/5 (Borderline Findings)**，核心问题三个：

1. **新颖性不足** — 核心框架（frozen weights + Gumbel + KL training）与 MaskLLM 高度重叠，本文的 delta 是 weight → activation sparsity 的迁移应用，非 conceptual advance
2. **效率动机空洞** — 以 sparsity prediction 为题暗示加速，实际增加 6.4% overhead，unstructured masks 无 wall-clock speedup
3. **叙事失衡** — Headline "49% PPL reduction" 掩盖了同设置下 MMLU 25%（近乎随机）的 downstream collapse

另有 7 个 should-fix 问题（MiniLLM 等重要引用遗漏、regime 分析数据不足、D2DMoE taxonomy positioning、training/eval domain overlap 等）和 5 个小问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 344 · 2026-05-17T09:23:51.436281+00:00_

收到 Reviewer 2 报告。等待 Reviewer 1 完成后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 30

## Round 30

6 recorded events


### User

_source line 345 · 2026-05-17T09:23:54.881638+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性 + 实验设计

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿标准**: ACL Rolling Review official review form (2025 updated, three-point scoring)

---

## Paper Summary

本文研究用 forward KL divergence 替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的 contextual sparsity predictor。核心观察是 BCE 梯度按 neuron 独立分解，与 TEAL 推理时 global top-k 分配机制存在结构性不匹配。作者训练一个轻量 predictor (75.9M params)，通过 Gumbel-Sigmoid relaxation 实现端到端 KL 蒸馏，在 LLaMA-3.1-8B 50% sparsity 下 PPL 11.79 vs TEAL 23.31 (49% 改善)。论文同时分析了 global vs uniform allocation 在不同 sparsity 水平下的 downstream 表现，提出了 three-regime 框架，并给出 2D taxonomy 分类先前方法。

---

## 总体评分

**Overall**: 2.5 / 5 (Borderline Findings)
**一句话总结**: 问题定义清晰，梯度分析有启发性，但关键数据不一致、实验对比存在 pipeline 混淆变量、headline method 在最重要的 downstream task 上退化至随机水平，整体证据链不足以支撑 claims 的强度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5 / 5 | 梯度分析数学正确但属 chain rule 的标准应用；BCE vs KL 对比存在严重 pipeline 混淆；22.51 PPL 幽灵数据；regime claim 证据密度不足 |
| Excitement | 2.5 / 5 | 问题本身有意义（per-neuron vs global allocation mismatch），但实际结果令人失望：无 wall-clock 加速、MMLU 退化至 random、仅 7-8B scale |
| Overall | 2.5 / 5 | 分析贡献有价值但实验缺陷削弱了可信度；需要修复数据一致性、补充 controlled comparison、调低 claim 强度 |
| Reproducibility | 3.5 / 5 | 大部分超参和实验细节已报告；但主表结果为单 seed、22.51 数字不可追溯 |
| Reviewer Confidence | 4 / 5 | 熟悉 activation sparsity、KD、Gumbel relaxation 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **数据完整性：PPL 22.51 幽灵数字**
- 具体位置：§4.3 (experiments.tex:66), Abstract, Introduction
- 问题：§4.3 写到 "BCE achieves +13pp oracle F1 (0.613 vs. 0.540) with 91% worse PPL (22.51 vs. 11.79)"。然而 22.51 这个数字**不出现在论文任何表格中**。Table 2 中 BCE (2700 steps) = 27.97, BCE+Compensation = 25.44。如果 22.51 是 1000-step BCE 的结果，它需要在 Table 2 或 Table 3 中显示。数学验证：22.51/11.79 = 1.909 ≈ "91% worse"，但如果用 Table 2 的 27.97，则是 137% worse。Abstract 和 Introduction 反复使用 "91% worse perplexity" 这个数字作为核心 claim，但该 claim 所依赖的 baseline 数据无法从论文本身验证。
- 为什么影响接收：论文最核心的 quantitative claim 之一不可追溯。审稿人无法从提交材料中 verify 该数字的来源。这不是 typo，是 **数据溯源链断裂**。
- 建议：在 Table 2 或 Table 3 中补充 BCE 1000-step 的 PPL 数据行，或者用 Table 中已有的数字（27.97）重新计算百分比。

---

**N2** [critical] **Headline method 在最重要 downstream task 上退化至随机水平**
- 具体位置：Table 2, Table 5, §4.5
- 问题：论文主推方法 "KL global (Ours)" 在 30% sparsity 下 MMLU = 25.27%，而 4-choice random baseline = 25%。同一设定下 TEAL vanilla = 38.61%。即论文的核心方法在最广泛使用的知识评测上**比 baseline 差 13.3pp**，且约等于随机。论文的解释是 global top-k allocation 导致 late-layer starvation（L31 retention 28.4%），并提出 uniform allocation 作为修复（恢复至 40.61%）。但这实质上承认：**论文提出的 KL + TEAL global 组合在 downstream tasks 上不可用**，实际可用配置是 KL + uniform allocation——但 uniform allocation 本身消除了 global top-k 的概念，也就是说论文花大量篇幅分析的 "global allocation quality" 在实践中需要被绕过。
- 为什么影响接收：论文的 framing 围绕 "KL optimizes for global allocation quality" (Abstract, §1, §3.5)，但实验结论表明 global allocation 在实践中损害 downstream performance。这是一个 **narrative vs evidence 的根本矛盾**。
- 建议：(1) 重新定位主推方法为 KL + uniform，将 global 作为分析对象而非推荐配置；(2) 在 Table 2 中将 KL uniform 标为 Ours (recommended)；(3) 调整 Abstract/Introduction 的 framing，诚实反映 "global allocation reveals a quality advantage in PPL but not downstream tasks"。

---

**N3** [critical] **BCE vs KL 对比存在严重的 pipeline 混淆变量**
- 具体位置：§4.3, §4.4, Table 3
- 问题：KL 和 BCE 使用了完全不同的训练 pipeline：
  - KL: Gumbel-Sigmoid soft masks + adaptive penalty controller + forward KL loss
  - BCE: hard masks + compensation network (optional) + per-neuron BCE loss
  
  论文 claim "the failure is structural, not due to architectural or compute differences" (§4.3)，但这个 claim 无法从现有实验中得出，因为 loss function 和 relaxation method 是 **jointly varied** 的。Table 3 的 isolation 实验 "BCE + Gumbel + Penalty (no KL)" = 38.02（比 vanilla BCE 的 27.97 更差）恰好说明了这个问题：Gumbel + penalty 机制与 BCE loss 互不兼容，无法简单分离。

  更公平的对比需要：(a) BCE + Gumbel + KL-style global objective (e.g., MSE on hidden states) 作为中间点；(b) KL + hard masks (STE) + no penalty 作为对照。Table 3 中 "Forward KL + STE" = 15.77 提供了部分信息，但仍然混杂了 relaxation 和 penalty 两个变量。

  论文称 "loss effect (ΔPPL=26.23) is 6.6× the relaxation effect (ΔPPL=3.98)"，但 loss effect 的计算用了 BCE+Gumbel+Penalty=38.02 vs KL+Gumbel=11.79，而不是 controlled comparison。BCE+Gumbel+Penalty 之所以差，可能是因为 penalty controller 破坏了 BCE 的 per-neuron convergence（论文自己也指出 "the penalty interferes with per-neuron optimization"），而非 KL 本身有多好。
- 为什么影响接收：无法从实验中 cleanly 区分 "KL loss 的贡献" vs "Gumbel relaxation + penalty controller 对 KL 恰好有效的贡献"。核心 claim "distributional objectives outperform decomposed per-neuron losses" 在 controlled experiment 意义上未被证明。
- 建议：(1) 补充 MSE (intermediate coupling) ablation，对应 taxonomy 中的 intermediate 列；(2) 补充 per-layer KL (解耦 cross-layer coupling) 作为 controlled variant；(3) 明确 claim 是关于 "KL+Gumbel+Penalty 组合" 而非单独的 loss function。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **"Three regimes" 从 3 个数据点归纳——证据密度不足**
- 具体位置：§4.5, Table 5
- 问题：论文定义了 budget-surplus (≤30%), budget-constrained (~40%), capacity-limited (≥50%) 三个 regime。但整个分析基于 3 个 sparsity level（30%, 40%, 50%）× 2 个 allocation = 6 个数据点。每个 "regime" 实际上只有 1 个数据点。regime boundary 的精确位置（30%→40% 之间、40%→50% 之间）完全没有被定位。论文说 "this boundary is consistent on both 7-8B models"，但 Mistral 上没有 regime analysis 数据（Table 6 只有 PPL，无 downstream）。
- 建议：(1) 补充 35%, 45% 的数据以定位 regime transition；(2) 降低 claim 强度为 "we observe non-monotonic behavior suggestive of distinct operating regimes"；(3) 在 Mistral 上补充 downstream 数据。

**W2** [warning] **无 wall-clock 加速——6.4% overhead**
- 具体位置：Appendix A, Table 7
- 问题：在 50% sparsity 下，KL predictor 的推理延迟为 126.78ms vs dense 的 119.11ms，即 **增加** 6.4% 延迟。论文在 Limitations 中承认需要 sparse kernel support，但 title ("Contextual Sparsity Prediction") 和 motivation (§1 第一段) 暗示了推理效率提升。一个增加延迟的 "sparsity" 方法在实用性上存在根本性问题。
- 建议：在 Abstract 中明确这是一个 prediction quality 研究，而非推理加速工作。

**W3** [warning] **Train-inference mismatch 未量化**
- 具体位置：§3.3, Appendix B.1
- 问题：训练使用 Gumbel-Sigmoid soft masks（τ=0.1 时仍是 soft），推理使用 hard top-k binary masks。这两者之间的 gap 从未被直接量化。Appendix B.1 的 temperature sensitivity 实验只测了不同 τ schedule 下的 TEAL global PPL，但没有报告 "soft mask at τ=0.1 PPL" vs "hard mask PPL"。Appendix B (Table 8) 的 per-token evaluation (9.218) 与 TEAL global (11.963) 的差距混合了 train-inference mismatch 和 allocation loss，无法分离。
- 建议：报告训练末期 soft mask (τ=0.1) 下的 PPL 与 hard mask 下的 PPL 对比。

**W4** [warning] **主表结果为单 seed**
- 具体位置：Table 2 caption, Appendix E
- 问题：Table 2 的所有关键对比（KL global 11.79, TEAL 23.31 等）都是 **单 seed** 结果。三 seed 评估仅在 50% uniform 配置下进行（11.92±0.07），且仅报告 PPL。核心 claim "49% PPL reduction" 基于单 seed。30% sparsity 下 KL global MMLU=25.27% 如果有 ±2pp 的方差就可能与 random baseline 无显著差异。Downstream metrics 的多 seed 数据仅在 Appendix E 简要提及一行。
- 建议：至少对 Table 2 的关键行（KL global 30%、50%，TEAL 30%、50%）做 3-seed 评估。

**W5** [warning] **模型规模局限**
- 具体位置：§4 全文, Limitations
- 问题：仅在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上测试。Title 说 "SwiGLU LLMs" 暗示广泛适用性。两个同规模（7-8B）模型不能代表 13B、70B 或更大模型上的表现。论文的 "structural mismatch" 是关于 SwiGLU 架构的一般性 claim，但实验范围不支撑。
- 建议：在 Title 中限定为 "7-8B SwiGLU LLMs"，或补充至少一个 13B 模型的实验。

**W6** [warning] **Adaptive Penalty Controller 无收敛保证**
- 具体位置：§3.4, Appendix C (Table 11)
- 问题：multiplicative schedule 是一个 heuristic，论文已在脚注中承认 "不保证 KKT 满足"。Appendix Table 11 显示 30% target 的 λ saturate at cap (5000) 且 deviation = 5.0%，意味着 controller 在该操作点 **没有收敛** 而是 **hit ceiling**。70% target 同样 saturate at cap (1000)。只有 40% 和 50% 真正收敛。这与正文 "converges within 40-110 steps across all targets" (§3.4) 的 claim 矛盾——hit cap 不等于 convergence。
- 建议：(1) 修正 §3.4 的 convergence claim，区分 "convergence" 和 "saturation at cap"；(2) 讨论 cap saturation 对训练质量的潜在影响。

---

## 小问题（不影响接收）

- §4.4 SPON analysis 脚注提到 "SPON analysis uses evaluate.py; main results use the unified benchmark"——这意味着 SPON 的 2.4% improvement (12.08→11.79) 可能是在不同 evaluation protocol 下比较的数字，不够严谨。
- Table 5 的 40% KL uniform PPL=8.36 footnote 标注该 predictor "uses a predictor trained at the respective sparsity target"，但 exp_id 标注为 "d030_kl40_uniform"（d030 暗示 predictor 在 30% 下训练，评估在 40% 下），需要澄清。
- Abstract 中 "7-8B scale" 的 claim 实际基于两个具体模型（LLaMA-8B, Mistral-7B），措辞给人更广泛验证的错觉。
- Table 1 (taxonomy) 的 "Static × Decomposed" 和 "Static × Intermediate" 两个 cell 标为 "---"，但 magnitude pruning (TEAL itself) 可被视为 static × decomposed，应讨论。
- 引用 xu2026spon 的 bib key 写成 2026 但论文年份为 2025 (ICML 2025)，虽是小问题但可能导致误解。

---

## 主要优势

1. **问题定义清晰、有启发性**：per-neuron BCE 与 global top-k 之间的 structural mismatch 是一个真实问题，gradient analysis 虽然本质上是 chain rule 的标准应用，但将其 formalize 并与 oracle F1 / SNR 实验联系起来的分析框架有价值。
2. **消融设计合理**：Table 3 覆盖了 divergence direction (forward/reverse/JSD)、relaxation (Gumbel/STE)、BCE variants (±compensation, +Gumbel)，多维度隔离了设计选择。
3. **诚实的 failure analysis**：论文没有隐瞒 MMLU 退化、无 wall-clock 加速等问题，而是将其作为分析对象（regime analysis, late-layer starvation），这是值得赞赏的。
4. **2D Taxonomy 有组织价值**：correction granularity × training signal coupling 的分类框架是理解 sparsity prediction 文献的有用工具。
5. **OOD 泛化评估**：C4 validation 上 52.5% advantage 的 OOD 实验（Appendix D）部分回应了 WikiText 训练/评估同源的担忧。
6. **Reproducibility 细节充分**：hyperparameter 全量报告、training convergence curve、bottleneck sensitivity sweep，大部分实验可复现。

---

## Missing References

- **MSE-based distillation for sparsity**: 论文 taxonomy 定义了 "Intermediate (MSE)" 这一列，cite 了 ShadowLLM 和 D2DMoE，但 **没有实验对比 MSE baseline**。如果要声称 KL (coupled) 优于 MSE (intermediate)，需要实验支撑。
- **Larger-scale activation sparsity**: 论文应讨论 Griffin (De et al., 2024) 或 Mixture-of-Depths (Raposo et al., 2024) 等涉及 dynamic compute allocation 的工作，因为它们从不同角度解决了 conditional computation 的 allocation 问题。

---

## Questions for Authors

1. §4.3 中 BCE PPL=22.51 对应哪个具体实验配置？为什么不在任何表格中？是 1000-step BCE 还是另一个 variant？
2. 是否尝试过 MSE on hidden states 作为中间 coupling 水平的 ablation？这对验证 "coupling 程度越强越好" 的 claim 很关键。
3. Table 5 中 40% KL uniform (exp_id: d030_kl40_uniform) 是否使用了在 30% 下训练的 predictor？如果是，这意味着不同行使用了不同的 predictor，影响 regime 分析的公平性。
4. 是否测量过训练结束时 soft mask (τ=0.1) 与 hard mask 之间的 PPL gap？
5. Appendix C (Table 11) 中 30% target λ=5000 (cap) with 5% deviation：如果 λ_max 设为更大值（如 10000），deviation 是否进一步降低？当前的 cap saturation 是否影响了 30% 的训练质量？

---

## Overall Assessment

本文提出了一个有意义的问题（per-neuron BCE 与 global allocation 的 mismatch），gradient analysis 提供了清晰的 motivation。但实验执行存在几个关键缺陷：(1) 核心数字 22.51 无法追溯，(2) headline method 在 MMLU 上严重退化与论文叙事矛盾，(3) BCE vs KL 对比被 pipeline 差异混淆。这些问题共同削弱了论文的核心 contribution claim 的可信度。

如果作者能 (a) 修复数据一致性、(b) 补充 controlled ablation（特别是 MSE baseline 和 per-layer KL）、(c) 重新 framing 以诚实反映 method 的实际适用范围，本文可以成为 Findings 级别的扎实 analytical contribution。当前状态需要 substantial revision。

**推荐**: Resubmit next cycle (2 / 5)，修复后有 Findings 潜力。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-17T09:24:48.178048+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、小问题 (P1-P5) 和 Questions (Q1-Q5)，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿报告\n\n## Must-Fix 问题\n\n**N1** [critical] 核心新颖性不足：与 MaskLLM 的区分过于薄弱\n- MaskLLM (Fang et al., NeurIPS 2024) 的高层框架与本文几乎完全一致：frozen base model weights + learnable masks + Gumbel relaxation + KL divergence training。论文在 §2 声称区别在于 \"weight vs activation sparsity\" 和 \"static N:M vs dynamic per-token\"。但这本质上是将一个已被验证有效的训练范式应用到一个不同的 sparsity type，属于 application-level 的迁移而非方法论创新。\n- 论文声称 \"The structural mismatch we identify does not arise in MaskLLM's per-group categorical setting\"，但这恰恰说明 structural mismatch 分析是 task-specific 的适配，而非通用性洞察。\n\n**N2** [critical] 实际推理无加速，效率动机不成立\n- Table 8 明确显示 pipeline 增加 6.4% overhead。unstructured element-wise masks 无法利用硬件稀疏加速。Abstract 的 \"49% reduction\" PPL 结果容易让读者误认为有速度提升。\n\n**N3** [critical] PPL-centric 叙事掩盖 downstream collapse 的严重性\n- 30% sparsity, KL global: MMLU 25.27%（dense 65.27%，降 40pp，近乎随机）\n- 50% sparsity: MMLU 27.89%, GSM8K 1.29%（完全失效）\n- KL global 是论文的 primary inference protocol，而 KL global 在所有设置下 MMLU 都很差\n- 论文试图将问题归因于 allocation strategy，但 global allocation 是论文自己的 primary protocol\n\n## Should-Fix 问题\n\n**W1** [warning] \"Structural mismatch\" 洞察的新颖性可质疑\n- end-to-end 目标优于 decomposed per-component 目标是深度学习的基本原则。论文将 BCE 独立梯度 vs KL Jacobian 耦合包装为 novel insight，但本质上是 \"end-to-end loss 能捕获组件间交互\" 的直接推论。\n\n**W2** [warning] Taxonomy (Table 1) 贡献价值有限\n- 2D taxonomy 是 post-hoc organization，没有做出可验证的预测。\"Static × Decomposed\" 和 \"Static × Intermediate\" 是空的但未讨论原因。\n\n**W3** [warning] 三 regime 分析数据点过少\n- 3 个 sparsity level × 2 个模型 = 6 个数据点，每个 regime 只有 1 个数据点。regime boundary 精确位置未被定位。\n\n**W4** [warning] Related work 遗漏重要引用\n- MiniLLM (forward vs reverse KL for LLM distillation, ICLR 2024)\n- SVD Contextual Sparsity Predictors (arxiv 2603.14110)\n- SparseLoRA (ICML 2025)\n- Broader LLM distillation literature\n- 32 篇引用对 EMNLP long paper 偏少（typical: 40-60）\n\n**W5** [warning] D2DMoE taxonomy positioning 需更细致\n- D2DMoE 的训练包含 router training 和 expert conversion，不仅仅是 MSE on hidden states。\n\n**W6** [warning] Training/evaluation domain overlap\n- WikiText-103 训练, WikiText-2 评测。C4 OOD PPL 18.40 比 WikiText-2 的 11.79 高 56%。\n\n**W7** [warning] Framing 不一致：mechanistic understanding vs efficiency\n- Conclusion 提到 wall-clock speedup 和 practical deployment value 作为 future directions，与 understanding framing 矛盾。\n\n## 小问题 P1-P5\n- P1: SPON eval protocol 不一致\n- P2: 早 saturation 可作 efficiency 优势\n- P3: BCE 不同 inference pipeline 的公平性说明不够显眼\n- P4: bib xu2026spon key vs year 不一致\n- P5: 75.9M \"lightweight\" 标准不明确\n\n## Questions Q1-Q5\n- Q1: MaskLLM 直接迁移到 activation sparsity 的效果？\n- Q2: KL predictor 与 TEAL global top-k 是否根本性不兼容？\n- Q3: Forward vs reverse KL 与 MiniLLM 结论矛盾？\n- Q4: 什么条件下 unstructured sparsity 能实现实际加速？\n- Q5: 三 regime 的精确边界？\n\n---\n\n请逐条用 [AGREE] 或 [REBUT] 回应。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、小问题 (P1-P5) 和 Questions (Q1-Q5)，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿报告\n\n## Must-Fix 问题\n\n**N1** [critical] 核心新颖性不足：与 MaskLLM 的区分过于薄弱\n- MaskLLM (Fang et al., NeurIPS 2024) 的高层框架与本文几乎完全一致：frozen base model weights + learnable masks + Gumbel relaxation + KL divergence training。论文在 §2 声称区别在于 \"weight vs activation sparsity\" 和 \"static N:M vs dynamic per-token\"。但这本质上是将一个已被验证有效的训练范式应用到一个不同的 sparsity type，属于 application-level 的迁移而非方法论创新。\n- 论文声称 \"The structural mismatch we identify does not arise in MaskLLM's per-group categorical setting\"，但这恰恰说明 structural mismatch 分析是 task-specific 的适配，而非通用性洞察。\n\n**N2** [critical] 实际推理无加速，效率动机不成立\n- Table 8 明确显示 pipeline 增加 6.4% overhead。unstructured element-wise masks 无法利用硬件稀疏加速。Abstract 的 \"49% reduction\" PPL 结果容易让读者误认为有速度提升。\n\n**N3** [critical] PPL-centric 叙事掩盖 downstream collapse 的严重性\n- 30% sparsity, KL global: MMLU 25.27%（dense 65.27%，降 40pp，近乎随机）\n- 50% sparsity: MMLU 27.89%, GSM8K 1.29%（完全失效）\n- KL global 是论文的 primary inference protocol，而 KL global 在所有设置下 MMLU 都很差\n- 论文试图将问题归因于 allocation strategy，但 global allocation 是论文自己的 primary protocol\n\n## Should-Fix 问题\n\n**W1** [warning] \"Structural mismatch\" 洞察的新颖性可质疑\n- end-to-end 目标优于 decomposed per-component 目标是深度学习的基本原则。论文将 BCE 独立梯度 vs KL Jacobian 耦合包装为 novel insight，但本质上是 \"end-to-end loss 能捕获组件间交互\" 的直接推论。\n\n**W2** [warning] Taxonomy (Table 1) 贡献价值有限\n- 2D taxonomy 是 post-hoc organization，没有做出可验证的预测。\"Static × Decomposed\" 和 \"Static × Intermediate\" 是空的但未讨论原因。\n\n**W3** [warning] 三 regime 分析数据点过少\n- 3 个 sparsity level × 2 个模型 = 6 个数据点，每个 regime 只有 1 个数据点。regime boundary 精确位置未被定位。\n\n**W4** [warning] Related work 遗漏重要引用\n- MiniLLM (forward vs reverse KL for LLM distillation, ICLR 2024)\n- SVD Contextual Sparsity Predictors (arxiv 2603.14110)\n- SparseLoRA (ICML 2025)\n- Broader LLM distillation literature\n- 32 篇引用对 EMNLP long paper 偏少（typical: 40-60）\n\n**W5** [warning] D2DMoE taxonomy positioning 需更细致\n- D2DMoE 的训练包含 router training 和 expert conversion，不仅仅是 MSE on hidden states。\n\n**W6** [warning] Training/evaluation domain overlap\n- WikiText-103 训练, WikiText-2 评测。C4 OOD PPL 18.40 比 WikiText-2 的 11.79 高 56%。\n\n**W7** [warning] Framing 不一致：mechanistic understanding vs efficiency\n- Conclusion 提到 wall-clock speedup 和 practical deployment value 作为 future directions，与 understanding framing 矛盾。\n\n## 小问题 P1-P5\n- P1: SPON eval protocol 不一致\n- P2: 早 saturation 可作 efficiency 优势\n- P3: BCE 不同 inference pipeline 的公平性说明不够显眼\n- P4: bib xu2026spon key vs year 不一致\n- P5: 75.9M \"lightweight\" 标准不明确\n\n## Questions Q1-Q5\n- Q1: MaskLLM 直接迁移到 activation sparsity 的效果？\n- Q2: KL predictor 与 TEAL global top-k 是否根本性不兼容？\n- Q3: Forward vs reverse KL 与 MiniLLM 结论矛盾？\n- Q4: 什么条件下 unstructured sparsity 能实现实际加速？\n- Q5: 三 regime 的精确边界？\n\n---\n\n请逐条用 [AGREE] 或 [REBUT] 回应。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-17T09:25:22.098326+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33920
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-17T09:25:22.249305+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、小问题和 Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿报告\n\n## Must-Fix 问题\n\n**N1** [critical] 数据完整性：PPL 22.51 幽灵数字\n- §4.3 写到 \"BCE achieves +13pp oracle F1 (0.613 vs. 0.540) with 91% worse PPL (22.51 vs. 11.79)\"。然而 22.51 不出现在论文任何表格中。Table 2 中 BCE (2700 steps) = 27.97, BCE+Compensation = 25.44。Abstract 和 Introduction 反复使用 \"91% worse perplexity\" 这个核心 claim，但依赖的 baseline 数据无法从论文本身验证。数据溯源链断裂。\n\n**N2** [critical] Headline method 在最重要 downstream task 上退化至随机水平\n- KL global (Ours) 在 30% sparsity 下 MMLU = 25.27%，4-choice random baseline = 25%。同设定下 TEAL vanilla = 38.61%。论文花大量篇幅分析的 \"global allocation quality\" 在实践中需要被绕过（用 uniform allocation）。这是 narrative vs evidence 的根本矛盾。\n\n**N3** [critical] BCE vs KL 对比存在严重的 pipeline 混淆变量\n- KL 使用 Gumbel-Sigmoid soft masks + adaptive penalty controller + forward KL loss\n- BCE 使用 hard masks + compensation network (optional) + per-neuron BCE loss\n- 论文 claim \"the failure is structural, not due to architectural or compute differences\"，但 loss function 和 relaxation method 是 jointly varied 的。\n- Table 3 \"BCE + Gumbel + Penalty (no KL)\" = 38.02（比 vanilla BCE 更差）恰好说明 Gumbel + penalty 与 BCE 互不兼容，无法简单分离。\n- 缺少 controlled comparison：MSE on hidden states 作中间点、per-layer KL 解耦 cross-layer coupling。\n- \"loss effect (ΔPPL=26.23) is 6.6× the relaxation effect (ΔPPL=3.98)\" 的计算方法混淆了变量。\n\n## Should-Fix 问题\n\n**W1** [warning] Three regimes 从 3 个数据点归纳——证据密度不足\n- 每个 regime 只有 1 个数据点。regime boundary 精确位置未定位。Mistral 上无 downstream regime 数据。\n\n**W2** [warning] 无 wall-clock 加速——6.4% overhead\n- 50% sparsity 增加 6.4% 延迟。title 和 motivation 暗示推理效率提升。\n\n**W3** [warning] Train-inference mismatch 未量化\n- 训练 soft masks (τ=0.1) vs 推理 hard top-k binary masks，gap 未直接量化。Appendix B per-token (9.218) vs TEAL global (11.963) 混合了 mismatch 和 allocation loss。\n\n**W4** [warning] 主表结果为单 seed\n- Table 2 所有关键对比都是单 seed。三 seed 仅在 50% uniform 配置下（11.92±0.07），且仅报告 PPL。\n\n**W5** [warning] 模型规模局限\n- 仅 7-8B 规模。Title \"SwiGLU LLMs\" 暗示广泛适用性。\n\n**W6** [warning] Adaptive Penalty Controller 无收敛保证\n- 30% target λ saturate at cap (5000) 且 deviation = 5.0%，70% 同样 saturate。正文 claim \"converges within 40-110 steps across all targets\" 与 hit cap 矛盾。\n\n## 小问题\n- SPON analysis 使用不同 eval protocol\n- Table 5 d030_kl40_uniform exp_id 暗示 predictor 在 30% 下训练但评估在 40% 下\n- Abstract \"7-8B scale\" 措辞给人更广泛验证的错觉\n- Table 1 TEAL 可被视为 static × decomposed\n- bib xu2026spon key/year 不一致\n\n## Questions\n1. BCE PPL=22.51 对应哪个实验配置？\n2. 是否尝试过 MSE on hidden states 作为中间 coupling ablation？\n3. Table 5 d030_kl40_uniform 是否用了 30% 训练的 predictor？\n4. soft mask (τ=0.1) 与 hard mask 之间的 PPL gap？\n5. 30% λ_max=5000 cap saturation 是否影响训练质量？\n\n---\n\n请逐条用 [AGREE] 或 [REBUT] 回应。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、小问题和 Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿报告\n\n## Must-Fix 问题\n\n**N1** [critical] 数据完整性：PPL 22.51 幽灵数字\n- §4.3 写到 \"BCE achieves +13pp oracle F1 (0.613 vs. 0.540) with 91% worse PPL (22.51 vs. 11.79)\"。然而 22.51 不出现在论文任何表格中。Table 2 中 BCE (2700 steps) = 27.97, BCE+Compensation = 25.44。Abstract 和 Introduction 反复使用 \"91% worse perplexity\" 这个核心 claim，但依赖的 baseline 数据无法从论文本身验证。数据溯源链断裂。\n\n**N2** [critical] Headline method 在最重要 downstream task 上退化至随机水平\n- KL global (Ours) 在 30% sparsity 下 MMLU = 25.27%，4-choice random baseline = 25%。同设定下 TEAL vanilla = 38.61%。论文花大量篇幅分析的 \"global allocation quality\" 在实践中需要被绕过（用 uniform allocation）。这是 narrative vs evidence 的根本矛盾。\n\n**N3** [critical] BCE vs KL 对比存在严重的 pipeline 混淆变量\n- KL 使用 Gumbel-Sigmoid soft masks + adaptive penalty controller + forward KL loss\n- BCE 使用 hard masks + compensation network (optional) + per-neuron BCE loss\n- 论文 claim \"the failure is structural, not due to architectural or compute differences\"，但 loss function 和 relaxation method 是 jointly varied 的。\n- Table 3 \"BCE + Gumbel + Penalty (no KL)\" = 38.02（比 vanilla BCE 更差）恰好说明 Gumbel + penalty 与 BCE 互不兼容，无法简单分离。\n- 缺少 controlled comparison：MSE on hidden states 作中间点、per-layer KL 解耦 cross-layer coupling。\n- \"loss effect (ΔPPL=26.23) is 6.6× the relaxation effect (ΔPPL=3.98)\" 的计算方法混淆了变量。\n\n## Should-Fix 问题\n\n**W1** [warning] Three regimes 从 3 个数据点归纳——证据密度不足\n- 每个 regime 只有 1 个数据点。regime boundary 精确位置未定位。Mistral 上无 downstream regime 数据。\n\n**W2** [warning] 无 wall-clock 加速——6.4% overhead\n- 50% sparsity 增加 6.4% 延迟。title 和 motivation 暗示推理效率提升。\n\n**W3** [warning] Train-inference mismatch 未量化\n- 训练 soft masks (τ=0.1) vs 推理 hard top-k binary masks，gap 未直接量化。Appendix B per-token (9.218) vs TEAL global (11.963) 混合了 mismatch 和 allocation loss。\n\n**W4** [warning] 主表结果为单 seed\n- Table 2 所有关键对比都是单 seed。三 seed 仅在 50% uniform 配置下（11.92±0.07），且仅报告 PPL。\n\n**W5** [warning] 模型规模局限\n- 仅 7-8B 规模。Title \"SwiGLU LLMs\" 暗示广泛适用性。\n\n**W6** [warning] Adaptive Penalty Controller 无收敛保证\n- 30% target λ saturate at cap (5000) 且 deviation = 5.0%，70% 同样 saturate。正文 claim \"converges within 40-110 steps across all targets\" 与 hit cap 矛盾。\n\n## 小问题\n- SPON analysis 使用不同 eval protocol\n- Table 5 d030_kl40_uniform exp_id 暗示 predictor 在 30% 下训练但评估在 40% 下\n- Abstract \"7-8B scale\" 措辞给人更广泛验证的错觉\n- Table 1 TEAL 可被视为 static × decomposed\n- bib xu2026spon key/year 不一致\n\n## Questions\n1. BCE PPL=22.51 对应哪个实验配置？\n2. 是否尝试过 MSE on hidden states 作为中间 coupling ablation？\n3. Table 5 d030_kl40_uniform 是否用了 30% 训练的 predictor？\n4. soft mask (τ=0.1) 与 hard mask 之间的 PPL gap？\n5. 30% λ_max=5000 cap saturation 是否影响训练质量？\n\n---\n\n请逐条用 [AGREE] 或 [REBUT] 回应。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-17T09:25:23.670118+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1420
}
```

</details>

---


### Assistant

_source line 350 · 2026-05-17T09:25:26.924442+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 351 · 2026-05-17T09:25:29.432669+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审查总结**：

核心发现 3 个 critical 问题 + 6 个 warning 问题：

**Critical**:
1. **数据完整性**：§4.3 中 BCE PPL=22.51 不存在于任何表格中，但 "91% worse PPL" 这个核心 claim（出现在 Abstract、Introduction、Experiments）依赖此数字
2. **Headline method MMLU 退化**：KL global 在 30% sparsity 下 MMLU=25.27%（≈random），比 TEAL 差 13pp，与论文 "optimizes for global allocation quality" 的叙事矛盾
3. **Pipeline 混淆变量**：KL 和 BCE 使用完全不同的训练 pipeline（Gumbel vs hard mask, penalty vs none），无法 cleanly 隔离 loss function 的贡献

**评分**: Overall 2.5/5 (Borderline Findings), Soundness 2.5/5, Excitement 2.5/5。修复数据一致性、补充 controlled ablation、调整 framing 后有 Findings 潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 352 · 2026-05-17T09:25:34.383558+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 32

## Round 32

2 recorded events


### User

_source line 353 · 2026-05-17T09:27:27.129881+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

**[AGREE] R2-N1: 与 MaskLLM 的区分薄弱**

同意 R2 的判断。论文 §2 Related Work 已承认两者共享 "frozen weights + learnable masks + KL training" 范式，区别仅在 sparsity type（weight N:M vs activation per-token）和 mask generation（static categorical vs dynamic per-neuron）。论文的辩护是 "structural mismatch does not arise in MaskLLM's per-group categorical setting"（§2 第二段），但正如 R2 所指出，这恰好说明论文的核心 "insight" 是 MaskLLM 范式在新 setting 下的 task-specific 适配，而非通用性方法论贡献。

**补充证据**：论文的方法部分（§3.1-§3.4）除了 Adaptive Penalty Controller（§3.4）外，每个组件都有直接对应的已有工作：Gumbel-Sigmoid relaxation → MaskLLM/Concrete distribution，KL distillation → MaskLLM/standard KD，per-layer MLP predictor → DejaVu/FastForward。唯一的方法论新增是 multiplicative penalty schedule，但这只是 augmented Lagrangian 的一个简化 heuristic（§3.4 脚注自承）。

如果论文重新定位为 **empirical analysis paper**（"我们验证了 KL 范式在 activation sparsity + global allocation 设定下的表现，发现了 structural mismatch 现象"），novelty 问题会缓解。但当前 framing 混合了 method contribution 和 analytical contribution，导致 novelty expectation 被拉高。

---

**[AGREE] R2-N2: 无 wall-clock 加速**

完全同意。Table 8（Appendix A）显示 KL predictor 在 50% sparsity 下 latency 126.78ms vs dense 119.11ms，即 **增加 6.4% 延迟**。论文在 Limitations 中承认 "actual wall-clock acceleration depends on sparse kernel implementations"，但 Abstract 和 Introduction 的 motivation 从 "contextual sparsity" 的 inference efficiency 角度切入，给读者建立了效率提升的预期。

**补充**：我在自己的审稿中将此列为 W2 (warning) 而非 critical。R2 升级为 critical 有其道理——如果论文的 motivation 是 efficiency 但实际结果是 overhead，这是一个叙事诚信问题。但论文 Limitations 的坦诚报告和 Conclusion 的 "prediction quality rather than systems optimization" 定位部分缓解了这一点。我倾向于 **介于 critical 和 warning 之间**：不至一票否决，但需要在 Abstract 中明确 "本文研究 prediction quality，不提供 wall-clock 加速"。

---

**[AGREE] R2-N3: PPL-centric 叙事掩盖 downstream collapse**

强烈同意。这与我自己的 N2 (critical) 完全一致。数据清晰：

- Table 2：30% KL global MMLU = 25.27%（≈ 4-choice random），TEAL vanilla = 38.61%
- Table 2：50% KL global MMLU = 27.89%，GSM8K = 1.29%
- Table 5：即使是 "best case" 的 30% KL uniform = 40.61%，也比 dense 65.27% 低 24.7pp

论文的 primary inference protocol "KL + TEAL global" 在所有设定下 MMLU 都不可用。论文试图用 regime analysis（§4.5）和 "allocation strategy vs predictor quality" 的归因来化解，但实际效果是：读者读完论文后不清楚这个方法在什么条件下 **真正可用**。

R2 和我对此问题的 severity 评估完全一致：critical。

---

## Should-Fix 问题

**[AGREE] R2-W1: "Structural mismatch" insight 新颖性可质疑**

部分同意，有补充。R2 说 "end-to-end 目标优于 decomposed 目标是基本原则"，这个判断是对的。§3.5 的梯度分析本质上是对 chain rule 的展开——factor (b) 的 Jacobian 耦合是任何 end-to-end loss 的固有性质，不是 KL 特有的。

**但有一个有价值的 empirical 观察**：BCE F1=0.613 > KL F1=0.540，但 KL PPL 远优（§4.3）。这个 "高 accuracy 反而差 performance" 的现象不是先验显然的——直觉上 per-neuron 更准确应该更好。论文将此解释为 proxy misalignment，这个 empirical finding 本身有贡献。但把它包装成 "formal gradient analysis" 级别的理论贡献确实过度了。

---

**[REBUT] R2-W2: Taxonomy 贡献有限**

部分不同意。Taxonomy（Table 1）虽然是 post-hoc 的描述性分类，但在 activation sparsity prediction 领域没有先前工作做过这种系统化整理。2D 框架（correction granularity × training signal coupling）确实帮助定位了方法空间中的空白（Per-token × Coupled cell），并为 reader 提供了快速理解方法关系的入口。

但我同意 R2 的两个具体批评：(1) 空 cell（Static × Decomposed, Static × Intermediate）未讨论原因——TEAL 可以被视为 Static × Decomposed，这个遗漏需要修正；(2) taxonomy 不做可验证预测，限制了其科学贡献。

**结论**：taxonomy 有 organizational utility，但不应作为 contribution 列表中的独立条目。它更适合作为 Related Work 的组织框架。

---

**[AGREE] R2-W3: 三 regime 分析数据点不足**

完全同意，这与我自己的 W1 一致。3 个 sparsity level × 2 allocation = 6 data points，每个 "regime" 仅 1 个观测。regime boundary 的位置（30%→40% 之间 surplus→constrained 转变、40%→50% 之间 constrained→limited 转变）完全没有被细粒度定位。论文说 "this boundary is consistent on both 7-8B models"（§4.5），但 Mistral 上根本没有 downstream regime 数据（Table 6 只有 PPL）。

---

**[AGREE] R2-W4: Missing references**

同意引用不足。32 篇对 EMNLP long paper 偏少（R2 给出的 typical range 40-60 是合理的）。具体遗漏：

- **MiniLLM (Gu et al., ICLR 2024)**：直接相关——研究 forward vs reverse KL 在 LLM distillation 中的差异，论文 §4.4 ablation 测了 forward vs reverse KL 但未讨论 MiniLLM 的结论。这对 Q3 尤其重要。
- **Broader LLM distillation 文献**：论文 cite 了 Hinton (2015)、DistilBERT、Sequence-KD，但缺少近年 LLM-specific distillation 工作（GKD, MiniLLM 等）。

R2 提到的 SVD Contextual Sparsity Predictors (arxiv 2603.14110) 我无法确认是否已公开（arXiv 2603 prefix 暗示 2026年3月），如果在 submission deadline 之前公开则应引用。

---

**[AGREE] R2-W5: D2DMoE taxonomy positioning 简化**

同意。论文将 D2DMoE 归类为 "Intermediate (MSE)" coupling，但 D2DMoE 的训练流程包含 expert conversion（将 dense FFN 重组为 MoE）+ router training + fine-tuning，远比单纯 MSE 监督复杂。§2 的描述 "converts dense FFNs to dynamic-k experts with MSE supervision on hidden states" 遗漏了 expert conversion 的结构性变化。这影响了 taxonomy 中 D2DMoE 的准确定位。

---

**[REBUT] R2-W6: Training/evaluation domain overlap**

部分不同意。WikiText-103 训练 / WikiText-2 评测的同源性确实是一个 concern，但论文在 Appendix D 提供了 C4 OOD 评估。R2 指出 "C4 PPL 18.40 比 WikiText-2 的 11.79 高 56%"，但这个 gap 主要反映 domain shift 对 absolute PPL 的影响（dense 模型本身也从 6.12 升至 9.21，即 50.5% increase）。更重要的指标是 **relative advantage**：WikiText-2 上 KL vs TEAL = 49% improvement，C4 上 = 52.5% improvement。Relative advantage 在 OOD 数据上 **保持甚至略增**，说明 predictor 学到了可迁移的 neuron importance patterns。

**但**：OOD 评估仅在 50% sparsity 下进行，缺少 30% 和 40% 的 OOD 数据。鉴于 30% 的 downstream 表现（MMLU 25.27%）是论文最薄弱的环节，OOD 下 30% 的表现尤为关键。这一点上 R2 的 concern 有道理。

---

**[AGREE] R2-W7: Framing 不一致**

同意。Introduction 的 reframing 侧重 "mechanistic understanding"（梯度分析、structural mismatch、regime taxonomy），但 Conclusion 最后一段直接提到 "wall-clock speedup" 和 "practical deployment value" 作为 future directions（§5 最后一句）。如果论文定位是 analytical/mechanistic contribution，Conclusion 不应将效率作为核心 future direction，否则暗示当前工作的 motivation 仍然是效率。应改为以 allocation-aware training、scale validation 等分析方向收尾。

---

## 小问题 P1-P5

**[AGREE] R2-P1: SPON eval protocol 不一致**
同意。§4.4 脚注说明 SPON 用 evaluate.py 而 main results 用 unified benchmark，2.4% improvement (12.08→11.79) 可能在不同 evaluation 下不可比。我在自己的 review 中也标记了此问题。

**[AGREE] R2-P2: 早 saturation 可作 efficiency 优势**
同意。Appendix B.3 Table 10 显示 800 步即饱和（PPL 11.907 vs 1000步 11.906），可以节省 20% 训练时间。论文未将此作为 efficiency advantage 强调，是一个轻度遗漏。

**[AGREE] R2-P3: BCE inference pipeline 差异说明不够显眼**
同意。Table 2 caption 有脚注 "BCE uses a different inference protocol"，但正文 §4.3 的 iso-compute 对比直接比较 27.97 vs 11.79 而未在对比句中重申 pipeline 差异。

**[AGREE] R2-P4: bib key xu2026spon vs actual year**
同意，与我自己的小问题一致。

**[REBUT] R2-P5: 75.9M "lightweight" 标准不明确**
不同意这是一个问题。论文 §3.2 明确给出了比较基准："less than 1% of the 8B base model"。在 8B 模型上下文中，75.9M 占比 <1% 在 predictor-based sparsity 文献中属于标准量级（DejaVu 和 FastForward 的 predictor 规模相当）。"Lightweight" 的含义在上下文中是清晰的。

---

## Questions Q1-Q5

**Q1: MaskLLM 直接迁移到 activation sparsity 的效果？**
这是一个好问题，但超出了作者当前实验范围。MaskLLM 使用 Gumbel-Softmax 进行 per-group N:M categorical selection，直接迁移到 unstructured per-token activation sparsity 需要重新设计 mask generation 机制（从 categorical → binary）。但如果作者能展示 "MaskLLM-style baseline" 的表现，会大大增强 novelty 论证。建议作者在 revision 中补充此对比。

**Q2: KL predictor 与 TEAL global top-k 是否根本不兼容？**
[AGREE] 这是一个关键问题。Table 2 和 Table 5 的数据显示：在所有 sparsity 水平下，KL global 的 MMLU 都严重退化（30%: 25.27%, 40%: 38.06%, 50%: 27.89%）。如果 KL + global 在 downstream 上始终不可用，论文的 "optimize for global allocation quality" narrative 就存在根本矛盾。这个问题与我的 N2 和 R2 的 N3 直接相关。

**Q3: Forward vs reverse KL 与 MiniLLM 结论矛盾？**
[AGREE] 这是一个需要讨论的重要点。MiniLLM (Gu et al., ICLR 2024) 发现 reverse KL（避免 mode-averaging）在 LLM distillation 中更好，但本文 Table 3 显示 forward KL (11.79) > reverse KL (12.80)。两者的 context 不同（model distillation vs mask training），但论文应该讨论为什么结论相反——可能是因为 mask training 的 mode structure 与 model output distribution 不同，forward KL 的 mean-seeking 性质在 mask 优化中更有利（§3.4 简要提了一句 "preserve the dense model's primary predictions" 但未深入）。

**Q4: 什么条件下 unstructured sparsity 能实现实际加速？**
这是一个合理但超出论文范围的问题。论文 Limitations 已指出需要 "Triton block-sparse, cuSPARSE" 支持。当前 unstructured sparsity 在 GPU 上几乎无法加速是领域共识。

**Q5: 三 regime 的精确边界？**
[AGREE] 与我的 W1 和 R2 的 W3 一致。需要更细粒度的 sparsity sweep（35%, 45% 等）来定位 transition points。

---

## 总结

R2 的审稿意见整体准确且有深度。在 13 个具体 issue 中，我 **同意 10 项**、**部分反驳 3 项**（W2 taxonomy、W6 domain overlap、P5 lightweight 标准）。

R2 与我的审稿最大的共识在于：
1. **Downstream collapse 是核心问题**（R2-N3 = 我的 N2）
2. **Regime analysis 数据不足**（R2-W3 = 我的 W1）
3. **实际效率缺失**（R2-N2 = 我的 W2）

R2 提出而我未覆盖的最有价值的新观点是 **N1（与 MaskLLM 的 novelty 区分）** 和 **W4（missing references，特别是 MiniLLM）**。这两点我完全同意，会影响整体评分。

结合 R2 的意见，我维持 **Overall 2.5/5 (Resubmit next cycle)** 的评分，可能下调至 2.0。核心障碍是 downstream 失效 + 数据不一致 + novelty 有限的组合。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 354 · 2026-05-17T09:27:33.387186+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 355 · 2026-05-17T09:27:35.900884+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部意见的逐条回应。

总结：在 R2 的 13 个具体 issue 中，我同意 10 项（含 3 个 critical 全部同意），部分反驳 3 项（taxonomy 有组织价值、OOD relative advantage 保持、75.9M 在上下文中属 lightweight）。R2 提出的 MaskLLM novelty 问题和 MiniLLM missing reference 是我自己审稿未充分覆盖的重要新观点。维持 Overall 2.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 356 · 2026-05-17T09:27:41.158699+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 34

## Round 34

6 recorded events


### User

_source line 357 · 2026-05-17T09:29:00.537296+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### R1-N1: PPL 22.51 幽灵数字

**[AGREE]** 这是论文中最严重的数据完整性问题。

经核实：22.51 出现在 experiments.tex:66（§4.3 Iso-Compute Analysis），并在 abstract.tex:3 和 introduction.tex:15 通过 "91% worse perplexity" 被间接引用。但论文中没有任何表格包含 22.51 这个数字：

- Table 2: BCE (2700 steps) = 27.97
- Table 3: BCE (no compensation) = 27.97, BCE + Compensation = 25.44, BCE + Gumbel + Penalty = 38.02

22.51 / 11.79 = 1.909 → 91%，数学自洽。但 27.97 / 11.79 = 2.37 → 137%。这两个 BCE PPL（22.51 和 27.97）在同一段落中出现（experiments.tex:65-66），指向相同 exp_id（bce_isocompute_s42），令人困惑。

可能的解释：22.51 可能来自 BCE 1000-step（与 KL 同 budget），而 27.97 是 BCE 2700-step。但这一假设会导致更大问题——BCE 训练更久反而更差，与正文叙事矛盾。也可能 22.51 是不同 evaluation protocol 下的数字（类似 SPON 分析使用了不同 protocol），但论文没有说明。

无论如何，"91% worse" 是贯穿 Abstract、Introduction、Experiments 三处的核心 claim，其数据基础无法从论文本身验证。这是不可接受的。

**补充我的审稿发现**：我在自己的 Round 1 审稿中未独立发现此问题（P3 仅提到 BCE 使用不同 inference protocol 的 caption 问题），R1 的这个发现比我的相关观察更为尖锐和关键。

---

### R1-N2: Headline method MMLU 退化至随机水平

**[AGREE]** 与我的 N3 完全一致，但 R1 的措辞更精准。

补充证据：
- KL global 30%: MMLU 25.27%（4-choice random = 25%，差 0.27pp）
- 同一设置 TEAL vanilla: MMLU 38.61%（比 KL global 高 13.34pp）
- 论文的 primary inference protocol 是 KL global（experiments.tex:18-19 明确定义为 "predictor-TEAL"）

R1 正确指出了 narrative vs evidence 的根本矛盾：论文的核心方法（KL + global allocation）在最重要的 downstream task 上反而不如它声称要改进的 baseline（TEAL）。论文 §4.5 的 "allocation strategy rather than KL training quality" 解释虽然技术上可能正确，但在叙事上是自我矛盾的——如果你的方法必须搭配不同的 allocation strategy 才能工作，而你的论文全篇以 global allocation 为主线，这就是 framing 失败。

---

### R1-N3: BCE vs KL 对比的 pipeline 混淆变量

**[REBUT]**（部分同意技术观察，但反驳 severity 为 critical）

R1 的观察在技术上是准确的：KL 和 BCE 确实同时改变了 loss function 和 relaxation method。但我认为这个问题的严重性被 R1 高估了，理由如下：

1. **Table 3 的 isolation 逻辑是自洽的**：
   - "BCE + Gumbel + Penalty (no KL)" = 38.02 确实比 vanilla BCE (27.97) 更差。但论文的解释是合理的：Gumbel relaxation 产生 soft masks 并通过 penalty 控制 global sparsity，而 BCE 的 per-neuron 梯度无法利用这种 global coordination（experiments.tex:106-107）。这正是 "structural mismatch" 的又一个证据——不是 Gumbel 与 BCE "不兼容"，而是 BCE 的 decomposed gradient 与 global budget constraint 天然冲突。

2. **关键 controlled pair 存在**：
   - Forward KL + Gumbel (11.79) vs Forward KL + STE (15.77)：同一 loss，不同 relaxation → 隔离了 relaxation 效果 (+3.98)
   - Forward KL + Gumbel (11.79) vs BCE + Gumbel + Penalty (38.02)：同一 relaxation，不同 loss → 隔离了 loss 效果 (+26.23)

3. **但 R1 关于缺少 MSE 中间点的建议是有价值的**：MSE on hidden states 作为 "intermediate coupling" 的 ablation（与 Table 1 taxonomy 的 intermediate column 对应）确实缺失。如果 MSE 介于 BCE 和 KL 之间，会更有力地支持 "coupling degree" 的连续谱假说。如果 MSE 与 BCE 差不多甚至更差，则说明 coupling 不是线性递增的。

4. **Per-layer KL 解耦的建议同样有价值**：Per-layer KL（只优化当层输出 divergence，不通过下游层传播）可以隔离 factor (b)——跨层 Jacobian coupling 的贡献。

**结论**：降级为 Should-Fix。论文的 ablation 提供了 reasonable（但不完美的）evidence for loss as primary factor。MSE 和 per-layer KL 是有价值的补充实验，但缺失不构成 critical flaw。

---

## Should-Fix 问题

### R1-W1: Three regimes 证据密度不足

**[AGREE]** 与我的 W3 一致。3 个数据点定义 3 个 regime，每个 regime 恰好 1 个数据点，没有冗余验证。特别是 30%→40% 之间的 preference reversal 需要至少 35% 的数据来确认边界位置。

---

### R1-W2: 无 wall-clock 加速

**[AGREE]** 与我的 N2 一致。我在自己的审稿中将此列为 critical（N2），R1 列为 warning。我倾向于维持 critical 级别——inference efficiency 是论文的核心动机之一，实际增加 6.4% overhead 是对此动机的根本性削弱。

---

### R1-W3: Train-inference mismatch 未量化

**[AGREE]** 这是我在 Round 1 中遗漏的重要问题。

论文训练时最终 τ=0.1 的 soft masks（Gumbel-Sigmoid 输出接近但不等于 binary），推理时使用 hard binary masks from global top-k。Appendix B Table 9 的 per-token (9.218) vs TEAL global (11.963) 确实混合了两个效应：

- Soft→hard discretization gap
- Per-token→global allocation loss

需要的 controlled comparison（R1 没有明确列出但隐含）：
1. Soft per-token → Hard per-token：隔离 discretization effect
2. Hard per-token → Hard global：隔离 allocation effect

论文 §4.5 的 gap decomposition（experiments.tex:196）声称 "53% predictor approximation error + 47% allocation loss"，但这个分解的 "predictor approximation error" 可能同时包含了 soft-hard mismatch 和 predictor capacity limitation，无法进一步分离。

---

### R1-W4: 主表单 seed

**[AGREE]** Table 2 的所有关键对比（30% KL global, 50% KL global vs TEAL）都是单 seed。三 seed 验证仅限于 50% uniform 一个配置（PPL 11.92±0.07）。虽然 CV<1% 暗示 variance 可能普遍较低，但在最关键的 headline comparison（50% KL global = 11.79 vs TEAL = 23.31）上缺少 error bars 不符合 best practice。

---

### R1-W5: 模型规模局限

**[AGREE]** 与我的审稿一致。Title "SwiGLU LLMs" 过于宽泛。仅 7-8B 的结论能否推广到 13B-70B 未知。特别是 late-layer starvation 的 regime boundaries 很可能是 scale-dependent 的。

---

### R1-W6: Adaptive Penalty Controller 收敛问题

**[AGREE]** 这个问题我在 Round 1 中未发现。

核实 Appendix C Table 10（appendix.tex:125-131）：
- 30%: λ=5000 (cap), deviation=5.0%
- 70%: λ=1000 (cap), deviation=1.7%

正文 §3.5 (method.tex:105) claim "converges within 40-110 steps across all targets"。但 λ hit cap 不是 "converge"——是 saturation。如果 λ_max 设得更高，sparsity 可能继续改善。30% 的 5.0% deviation 意味着实际 sparsity = 28.5%，与标称 30% 的差距不小。

论文脚注（method.tex:105）承认 "we term it an adaptive penalty controller to distinguish from formal dual methods that guarantee KKT satisfaction"，这是诚实的，但正文的 "converges" 措辞仍然 misleading。

---

## 小问题

### SPON analysis 不同 eval protocol
**[AGREE]** 与我的 P1 一致。

### d030_kl40_uniform exp_id

**[AGREE]** 这是 R1 最敏锐的发现之一。

核实 experiments.tex 中所有 `d030` 开头的 exp_id：
- `d030_kl50_uniform`：出现在 Table 2（50% KL uniform = 11.96）和 Table 5
- `d030_kl40_uniform`：出现在 Table 5（40% KL uniform, PPL = 8.36）

而对应的 global allocation 行使用不同命名：`bench_kl40_global`, `bench_kl50_global`。

如果 `d030` 确实表示 "predictor trained at 30% sparsity"，则 Table 5 的 caption "Each row uses a predictor trained at the respective sparsity target" 是**虚假陈述**。这意味着：

1. 40% uniform (d030) 用的是 30%-trained predictor → 与 40% global (properly trained) 的对比不公平
2. 50% uniform (d030) 用的是 30%-trained predictor → 同理不公平
3. 整个 regime analysis 的 global vs uniform preference reversal 可能是 artifact of mismatched predictor training targets

这如果成立，会将 R1-W1（regime 分析证据不足）从 warning 升级为 critical。

**但也需谨慎**：`d030` 也可能是实验 batch 编号或其他命名约定。没有实验 registry 无法完全确认。但 circumstantial evidence 非常强。

### Abstract "7-8B scale" 措辞
**[AGREE]** 仅测了 2 个模型（LLaMA-3.1-8B, Mistral-7B-v0.3），"scale" 暗示了不存在的广度。

### Table 1 TEAL 缺失
**[REBUT]** TEAL 是 training-free 方法（不学习 predictor），不适合放在 "learned sparsity prediction methods" 的 taxonomy 中。Table 1 caption 明确限定为 "learned sparsity prediction methods"，TEAL 的排除是合理的。

### bib key 不一致
**[AGREE]** 与我的 P4 一致。

---

## Questions 回应

### Q1: BCE PPL=22.51 对应哪个实验？
**[AGREE]** 关键问题。我补充：22.51 和 27.97 在 experiments.tex:65-66 相邻两句出现，指向相同 exp_id (bce_isocompute_s42)，这本身就是矛盾。

### Q2: MSE on hidden states 作为中间 ablation
**[AGREE]** 如上述 N3 回应，这是有价值的补充实验。

### Q3: d030_kl40_uniform 是否用了 30% predictor
**[AGREE]** 如上述分析，circumstantial evidence 强烈暗示是。

### Q4: Soft mask (τ=0.1) 与 hard mask 的 PPL gap
**[AGREE]** 如 W3 回应，这个 gap 需要 clean isolation。

### Q5: 30% λ_max cap saturation
**[AGREE]** 如 W6 回应，cap saturation 导致 5% deviation 且正文 claim "converges" 是 misleading。

---

## 综合评价

R1 的审稿质量很高，特别是以下发现我完全赞同且在自己的 Round 1 中未充分覆盖：

1. **N1 (22.51 ghost number)**: 最关键发现。贯穿全文的 "91% worse" claim 依赖于无法验证的数字，这是硬伤。
2. **d030 exp_id 问题**: 如果确认 uniform allocation 行使用了错误 sparsity target 的 predictor，regime analysis 整体不可信。
3. **W3 train-inference mismatch**: 我遗漏的重要 gap。
4. **W6 penalty convergence**: 我遗漏的问题。

我与 R1 的主要分歧在 **N3**：R1 认为 BCE vs KL 的 pipeline confound 是 critical，我认为论文的 ablation（虽不完美）提供了 reasonable evidence，应降级为 Should-Fix。其余分歧仅在 severity level（如 W2 我列为 N2）。

**总体判断维持**：2.5 (Borderline Findings)。R1 的发现（特别是 N1 和 d030 问题）进一步加强了我对论文数据完整性的担忧。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---

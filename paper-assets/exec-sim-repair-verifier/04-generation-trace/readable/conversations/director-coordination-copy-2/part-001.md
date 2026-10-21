# Director coordination — Part 1 of 7

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/0d/0d5b5d57f8a45f2c2330.json)

## Round 1

## Round 1

96 recorded events


### User

_source line 1 · 2026-05-15T11:32:31.718290+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-15T11:32:40.923489+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-15T11:32:40.975163+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-15T11:32:44.945338+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 5 · 2026-05-15T11:32:44.945702+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-15T11:32:50.568672+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-15T11:32:51.224949+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (121 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-15T11:32:25Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 121 个实验 — DONE 115, PREPARING 3, RUNNING 3\n**DONE 分布**: failed 28, killed 11, negative 4, success 72\n\n### GPU 占用\n- **分配**: 1 张 — home-1x5090:cuda:0\n- **实际运行**: 2 张 — seetacloud-westd-4x5090:cuda:1(repo-level-cls-8b-s42-resume), seetacloud-westd-4x5090:cuda:0(cls8b-seed123-ckpt200-test-eval)\n- **空闲（分配了没跑）**: home-1x5090:cuda:0\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `repo-level-cwm-8b-conda-v4` | ? | cuda:2 | ? | `…uns/exec-sim-repair-verifier/repo-level-cwm-8b-conda-v4.log` |\n| `repo-level-cls-8b-s42-resume` | seetacloud-westd-4x5090 | cuda:1 | 295789 | `…s/exec-sim-repair-verifier/repo-level-cls-8b-s42-resume.log` |\n| `cls8b-seed123-ckpt200-test-eval` | seetacloud-westd-4x5090 | cuda:0 | 363037 | `…xec-sim-repair-verifier/cls8b-seed123-ckpt200-test-eval.log` |\n\n### 📌 最近完成 (top 5)\n- `cls4b-v5-ckpt4000-test5120-eval` [failed] — 2026-05-15T11:32:23 — SSH check failed 5x — last error: timed out\n- `cls8b-s42-ckpt1000-test-seq2048-ablation` [success] — 2026-05-15T11:29:21\n- `cls8b-seed123-ckpt6
…[truncated 1834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-15T11:32:52.129887+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-15T11:32:52.130437+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-15T11:32:59.661349+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-15T11:32:59.661771+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-15T11:33:02.523904+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-15T11:33:04.885012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-15T11:33:05.337577+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\fone}{F\textsubscript{1}}
26	\newcommand{\pp}{\,\text{pp}}
27	
28	\title{Classification Scales Where Generation Stalls:\\Reformulating Execution Simulation for Code Repair Verification}
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{abstract}
35	
36	\input{introduction}
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
41	\caption{Three verification formulations. \textbf{Left:} \cwm{} generates execution output, derives verdict by exact match. \textbf{Center:} \cls{} predicts binary pass/fail per test. \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved. \cls{} eliminates generation failure modes while preserving per-test diagnostic granularity.}
42	\label{fig:reformulation}
43	\end{figure*}
44	
45	\input{method}
46	
47	\input{experiments}
48	
49	\begin{figure}[t]
50	\centering
51	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
52	\caption{\cls{} vs.\ \cwm{} scaling from 4B to 8B. \cls{} gains +0.99\pp{} while \cwm{} loses $-$0.27\pp{}, widening the gap from 1.18 to 2.43\pp{}.}
53	\label{fig:scaling_gap}
54	\end{figure}
55	
56	\begin{figure}[t]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
59	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
60	\label{fig:oracl
…[truncated 142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-15T11:33:05.438345+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-15T11:33:13.318175+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view
…[truncated 3121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 10794
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-15T11:33:13.368994+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'exec-sim-repair-verifier'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7930
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-15T11:33:25.515990+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-15T11:33:26.018612+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-15T11:33:26.119652+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-15T11:33:26.220717+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml\", \"content\": \"_next_id: 95\\ndecisions:\\n- id: D001\\n  date: 2026-05-11 18:01 UTC\\n  summary: 'MVP 方案: Monte Carlo oracle 模拟 + 函数级 pilot，不依赖 Docker 基础设施'\\n  rationale: '完整 Part 1 需要 Docker 重新评估 8K 个 patch 获取 per-test labels（16-24h），基础设施搭建成本高。MVP\\n    改用 Monte Carlo 模拟参数化真实测试数分布验证理论信息增益，函数级 pilot (HumanEval/MBPP) 验证可学习性。两者均无需 Docker，2-3\\n    天可完成。Pass 标准: per-test 在 70-85% 精度下 resolve rate 比 trajectory-level 高 ≥5%; 函数级\\n    pilot 精度 >70%。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-11 19:07 UTC\\n  summary: MVP-A 有条件通过：F2P-only block-corr 10.88%>5%；需补跑 Total(F2P+P2P) 模拟确认全图\\n  rationale: 真实 SWE-bench F2P median=1（69% 实例仅 1 个 F2P 测试），但 P2P median=50.5。F2P-only\\n    下 per-test 优势收窄但仍过阈值（block-corr 10.88%）。P2P regression 检测是更大的信号源——Total 分布(median=52)下优势预期更强。研究方向需校准：per-test\\n    价值主要来自 P2P regression 检测 + F2P multi-test 精确定位，而非单纯的 F2P 粒度。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: F2P-only block-corr advantage 10.88%, i.i.d. 1.98%\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-11 19:38 UTC\\n  summary: P2P regression rate 是项目关键前提——≥10% per-test 有效，<5% 则有害；需实测\\n  rationale: Total 模拟(F2P+P2P)显示 per-test 优势强烈依赖 P2P regression rate：5% 时优势为负(-1%)，10%\\n    时 13.2%，20% 时 35.7%。这是从 F2P-only 分析未发现的关键变量。真实 regression rate 未知，需从 SWE-bench\\n    数据/文献中实测。此数据点决定项目是否可行及论文 story 如何构建。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: 'Total sim: reg=5% adv=-1%, reg=10% adv=13.2%, reg=20% adv=35.7%'\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-11 20:05 UTC\\n  summary: P2P 回归率 ~1%，原始 Total 优势前提不成立；项目 reframe 而非 kill\\n  rationale: P2P 回归率 ~1%（mean=1.04%, median=0%, 仅 22.6% 错误 patch 破坏任何 P2P 测试），远低于\\n    per-test 有效的 10% 阈值。Total(F2P+P2P) 模型下 per-test 实际有害（噪声>信号）。但项目核心价值不在信号
…[truncated 3562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-15T11:33:33.599443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-15T11:33:33.599823+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair faces a granularity--accuracy tradeoff: generation-based approaches (Code World Models) predict execution output strings but suffer from token-budget exhaustion, string-value prediction errors, and format compliance collapse as code complexity grows, while trajectory-level verifiers provide binary patch verdicts but discard per-test diagnostic information.
3	%
4	We reformulate execution simulation from open-ended output generation to per-test binary pass/fail classification, and systematically compare classification (\cls{}), generation (\cwm{}), and trajectory-level formulations at controlled model sizes.
5	%
6	On function-level benchmarks, \cls{} and \cwm{} achieve near-equivalent accuracy at 4B parameters (88.43\% vs.\ 87.19\%, 5 seeds, gap 1.24\pp{}). At 8B the gap widens to 2.43\pp{} (bootstrap mean 2.26\pp{}, $p{=}0.0066$, 3 seeds), with \cwm{} failing to benefit from scaling (\cls{} +0.99\pp{} vs.\ \cwm{} $-$0.27\pp{}, 4B$\to$8B). Per-test \cls{} matches trajectory-level accuracy (TOST equivalence $p{=}0.007$, $\pm$2\pp{} margin) while providing free diagnostic granularity---which specific tests fail. Oracle analysis on SWE-bench Verified shows this advantage concentrates in instances with $\geq$2 failing tests (31\% of instances, 55\% of total advantage); an oracle ensemble reaches 90.63\%. At repository level, the gap amplifies to 25.59\pp{} (83.63\% vs.\ 58.04\%, 4B, single seed), with \cwm{} falling ${\sim}$14\pp{} below majority baseline (72.96\%). Format non-compliance produces 53.7--67.2\% unparseable \cwm{} outputs, and even parseable outputs score only 42--43\%---below chance level (50\%)---while \cls{} remains robust with 0\% unparseable.
7	%
8	These results support classification as a promising alternative to generation-based execution simulation, with an advantage that grows with code complexity---from modest at function level to critical at repository level.
9	\end{abstrac
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-15T11:33:33.750642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-15T11:33:33.751155+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Test-time compute scaling~\cite{snell2024scaling} for LLM-based code repair depends critically on verification: given $K$ candidate patches, a verifier must rank and filter them by predicted correctness. Full execution verification is reliable but expensive---running test suites against each candidate costs \$1--3 and several minutes at repository scale, making it prohibitive for large $K$. Execution-free alternatives must therefore balance accuracy, diagnostic granularity, and computational cost. Yet the choice of \emph{how} to formulate the verification task---what the model predicts and in what format---has received surprisingly little attention.
5	
6	Two dominant paradigms have emerged for execution-free verification, each with distinct limitations. \textbf{Generation-based simulation}~\cite{meta2025cwm,ding2025selfexecution}: Code World Models predict the execution output string for each test, then derive pass/fail verdicts by exact match against expected outputs. This approach works well when outputs are short and structurally simple, but suffers from three systematic failure modes as complexity increases. First, \emph{token-budget exhaustion}: when the true output length exceeds the generation budget, the predicted string is truncated, producing a spurious failure verdict regardless of model capability. Second, \emph{string-value prediction errors}: complex return types---floating-point numbers, nested dictionaries, sets with arbitrary ordering---require exact string reproduction, and minor formatting differences cause false rejections even when the model has correctly inferred the semantic output. Third, \emph{format compliance collapse}: at repository-level complexity, the model fails to produce outputs in the required structured format altogether---53.7--67.2\% of \cwm{} predictions are unparseable across seeds, and among the parseable remainder, accuracy drops to 42--43\%, below chance level (50\%).
…[truncated 3637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-15T11:33:33.862609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-15T11:33:33.901394+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	We compare three formulations for execution-free code repair verification, differing in output granularity and generation requirements. Given a candidate patch and its associated test suite, each formulation predicts correctness at a different level of abstraction. We then analyze the failure modes specific to generation-based verification and develop an oracle framework that characterizes when per-test granularity provides value.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem-setup}
9	
10	Let $p$ denote a candidate code patch and $T = \{t_1, \ldots, t_n\}$ its associated test suite. Each test $t_i$ has a ground-truth label $y_i \in \{\textsc{Pass}, \textsc{Fail}\}$ determined by actual execution. The test suite decomposes into two disjoint subsets: \emph{fail-to-pass} tests $T_{\text{f2p}} \subseteq T$, which fail before the patch and should pass after a correct fix, and \emph{pass-to-pass} tests $T_{\text{p2p}} \subseteq T$, which pass before and should continue passing. A patch is correct if and only if all tests pass: $\forall\, t_i \in T{:}\ y_i = \textsc{Pass}$.
11	
12	The verification task is to predict patch correctness without executing the code. We study three formulations that differ in prediction granularity and output format.
13	
14	\subsection{Verification Formulations}
15	\label{sec:formulations}
16	
17	We compare three formulations differing in output granularity. Let $c_p$ denote the code context (unified git diff) of patch $p$.
18	
19	\paragraph{\textsc{CLS} (per-test classification).} A function $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\textsc{Pass}, \textsc{Fail}\}$ predicts a single binary token per test, trained with cross-entropy loss. The patch-level verdict is obtained by conjunction: $\hat{y}_p = \bigwedge_{i=1}^{n} [\hat{y}_i = \textsc{Pass}]$. Inference cost is exactly one token per test, independent of output complexity.
20	
21	\paragraph{\textsc{CWM} (output generation).} Following C
…[truncated 4469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 38
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-15T11:33:33.957909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-15T11:33:33.958647+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate \cls{}, \cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Function-level dataset.}
10	We construct a function-level benchmark from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} by generating mutated variants (five mutation types: \texttt{wrong\_operator}, \texttt{off\_by\_one}, \texttt{boundary\_error}, \texttt{return\_value}, \texttt{type\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	
12	\paragraph{Repo-level dataset.}
13	We construct a repo-level benchmark from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\%. Mutation type composition differs between validation and test due to the non-overlapping problem split; this is a consequence of the design (no data leakage), and val-based checkpoint selection is standard practice~\cite{jimenez2024swebench}.
14	
15	\paragraph{Models and training.}
16	We fine-tune Qwen3-4B and Qwen3-8B~\cite{yang2024qwen25} with LoRA~\cite{hu2022lora} (rank 16, lr $2{\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\cite{meta2025cwm}. Repo-level models u
…[truncated 18740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-15T11:33:34.122096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-15T11:33:34.122576+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation for Code.}
5	Code World Models~\cite{meta2025cwm} mid-train a 32B LLM on execution traces to predict output strings, establishing the generation-based paradigm.
6	Self-Execution~\cite{ding2025selfexecution} extends this with step-by-step trace prediction for self-verification.
7	CodeMind~\cite{liu2024codemind} evaluates code reasoning along multiple dimensions including independent and dependent execution reasoning.
8	SolidCoder~\cite{chen2025solidcoder} bridges mental simulation and actual execution via concrete execution feedback.
9	Ye et al.~\cite{ye2025demystifying} identify systematic failure modes in LLM trace prediction.
10	All share a generation formulation whose cost scales with output length and whose reliability degrades when outputs are complex---at repository-level complexity, we observe format compliance collapse (53--67\% unparseable outputs; \S\ref{sec:experiments}). We reformulate as per-test classification and show the advantage is complexity-dependent.
11	
12	\paragraph{LLM-based Verification for Code Repair.}
13	SWE-RM~\cite{zhang2025swerm} trains a 30B MoE reward model for trajectory-level execution-free patch ranking.
14	Patch Reasoner~\cite{wu2025patchreasoner} uses chain-of-thought reasoning for patch verification.
15	Snell et al.~\cite{snell2024scaling} show test-time compute scaling via verification can outperform parameter scaling.
16	S*~\cite{zhang2025sstar} combines execution-grounded selection with model-based scoring.
17	VG-Search~\cite{wang2025vgsearch} studies how verification granularity affects compute-efficient scaling.
18	We formally compare per-test and trajectory-level granularity, showing statistical equivalence (TOST $p = 0.007$) with additional per-test diagnostic signals.
19	
20	\paragraph{Automated Program Repair.}
21	SWE-bench~\cite{jimenez2024swebench} and SWE-bench Verified~\cite{chowdhury2024swebenchverified} provide standard bench
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-15T11:33:34.173169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-15T11:33:34.223757+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification. Our central finding is that the advantage of this reformulation is complexity-dependent: on function-level code with short, structurally simple outputs, classification and generation achieve near-equivalent accuracy; at repository scale, classification dominates by a wide margin. The generation formulation suffers a compounding failure on complex code---format non-compliance discards the majority of predictions, and the surviving parseable outputs are themselves unreliable, falling below chance-level accuracy (50\%). Classification is immune to this failure mode by construction, as binary verdicts require no structured output parsing. Moreover, at function level, scaling model capacity does not resolve the generation bottleneck: larger \cwm{} models show no accuracy improvement, consistent with a formulation-level rather than capacity-level limitation. Independently, per-test classification provides fine-grained diagnostic signals---identifying which specific tests a patch fails---at equivalent trajectory-level accuracy, with the advantage concentrating in instances that contain multiple fail-to-pass tests.
5	
6	These results carry practical implications for verification in test-time scaling pipelines. When patches are evaluated against multi-test suites---as in best-of-$N$ sampling or reranking---the choice of verification formulation matters: classification avoids the compounding failure that degrades generation on complex code. At function level, the formulation bottleneck we identify is distinct from model capacity, though whether this extends to repository scale awaits \cwm{} 8B results. Per-test verdicts also unlock downstream applications that trajectory-level verifiers cannot support, including targeted re-repair guided by per-test failure localization rather than binary ac
…[truncated 1311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-15T11:33:40.774942+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-15T11:33:41.176659+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-15T11:33:42.180559+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-15T11:33:42.682616+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-15T11:33:42.833560+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-15T11:33:42.884125+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-15T11:33:46.652018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-15T11:33:47.154444+00:00_

1	% === Execution Simulation ===
2	
3	@article{ding2025selfexecution,
4	  title={Self-Execution Simulation Improves Coding Models},
5	  author={Ding, Yangruibo and others},
6	  journal={arXiv preprint arXiv:2604.03253},
7	  year={2025}
8	}
9	
10	@article{meta2025cwm,
11	  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},
12	  author={{Meta AI}},
13	  journal={arXiv preprint arXiv:2510.02387},
14	  year={2025}
15	}
16	
17	@article{liu2024codemind,
18	  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},
19	  author={Liu, Changshu and others},
20	  journal={arXiv preprint arXiv:2402.09664},
21	  year={2024}
22	}
23	
24	@article{ye2025demystifying,
25	  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
26	  author={Ye, Yanzhuo and others},
27	  journal={arXiv preprint arXiv:2512.00215},
28	  year={2025}
29	}
30	
31	@article{chen2025solidcoder,
32	  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
33	  author={Chen, Xinyun and others},
34	  journal={arXiv preprint arXiv:2604.19825},
35	  year={2025}
36	}
37	
38	% === LLM Verification for Code ===
39	
40	@article{zhang2025swerm,
41	  title={{SWE-RM}: Execution-free Feedback for Software Engineering Agents},
42	  author={Zhang, Jiayi and others},
43	  journal={arXiv preprint arXiv:2512.21919},
44	  year={2025}
45	}
46	
47	@article{wu2025patchreasoner,
48	  title={Scalable Supervising Software Agents with Patch Reasoner},
49	  author={Wu, Zuxin and others},
50	  journal={arXiv preprint arXiv:2510.22775},
51	  year={2025}
52	}
53	
54	@article{wang2025vgsearch,
55	  title={Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling},
56	  author={Wang, Jinghan and others},
57	  journal={arXiv preprint arXiv:2505.11730},
58	  year={2025}
59	}
60	
61	@article{snell2024scaling,
62	  title={Scaling {LLM} Test-Time Compute O
…[truncated 5103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-15T11:33:47.606546+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-15T11:33:47.707513+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/memory.md\", \"content\": \"# Memory — exec-sim-repair-verifier\\n\\n## 硬教训：标 FAILED 前必须确认进程已退出 (2026-05-15)\\n- **事故**：v1 ckpt-3000 test eval (PID 345441) 被误标 DONE/failed，但进程实际在跑。随后 v2 提交到同 GPU 导致 OOM。\\n- **规则**：标 FAILED/DONE(failed) 前必须 `ps -p PID` 确认进程已退出。标 RUNNING 的实验所在 GPU 不得提交新任务。\\n- **适用范围**：所有 registry 状态变更操作\\n\\n## 硬教训：eval 不要用 --max_samples (2026-05-15)\\n- **事故**：seed123 ckpt-6200/6400 test eval 用了 `--max_samples 8192`，只评了 8192/9784 样本，与主表 n=9784 不可比。被 Reviewer 抓出后需 kill+重跑。\\n- **规则**：test eval 禁止 --max_samples 参数，必须评完整 test set (n=9784)。val eval 同理 (n=9335)。\\n- **例外**：debug/dry-run 时可以用，但结果不入正式表。\\n\\n## 硬教训：s42 resume 从 ckpt-600 开始 (2026-05-15)\\n- s42 resume 的 checkpoint 目录 `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/` 从 ckpt-600 开始（200步间隔），不含 ckpt-200/400。\\n- 原始训练 ckpt-200/400 在 `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/`，但那是 s42 原始训练目录不是 resume 目录。\\n- **提交 s42 val eval 前检查 checkpoint 是否存在于 resume 目录**。\\n\\n## D088 Checkpoint 选择 — Val Sweep 完成 (2026-05-15)\\n- **主指标回到 val-selected checkpoint**（ML 社区规范）\\n- **8B s42 Val-best = ckpt-1000 (88.23%, F1m=82.72%)** ← 8/8 checkpoint 全完成\\n- 完整 val curve: 200(63.5%) → 400(81.0%) → 800(84.5%) → **1000(88.2%)** → 1200(87.8%) → 1400(86.0%) → 1600(86.8%)\\n- **Test curve 完整**: 400(84.79%) → 600(79.05%) → 800(83.53%) → 1000(83.52%) → 1200(83.84%) → **1400(85.47%)** → 1600(84.99%)\\n- Test-best = ckpt-1400 (85.47%), Val-best = ckpt-1000 (88.23%, test=83.52%)\\n\\n## seed123 8B Val Sweep 完成 (2026-05-15)\\n- **ckpt-3000: 88.69%** ← **val-best confirmed**\\n- ckpt-6200: 87.52%\\n- ckpt-6400: 87.48%\\n- ckpt-6600: 87.23%\\n- ckpt-6633: 87.10%\\n- **ckpt-3000 test@8192 = 85.60%** (F1m=78.38%, gap=+12.64pp)\\n- save_total_limit=5 导致中段 checkpoint 被删，只剩 200, 6200, 6400, 6600, 6633 + backup 3000\\n\\n## Multi-seed 最终数字 (D093, 2026-05-15)\\n| seed | val-best | val | te
…[truncated 1420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-15T11:33:55.247079+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check external review config",
  "subagent_type": "Explore",
  "prompt": "Search for project configuration files that contain \"external_review\" or \"paperreview\" settings in /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/. Check YAML, JSON, and TOML config files. Report whether external_review.paperreview_ai.enabled is set to true or false. Quick search."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check external review config",
    "subagent_type": "Explore",
    "prompt": "Search for project configuration files that contain \"external_review\" or \"paperreview\" settings in /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/. Check YAML, JSON, and TOML config files. Report whether external_review.paperreview_ai.enabled is set to true or false. Quick search."
  }
}
```

</details>

---


### Tool call

_source line 45 · 2026-05-15T11:33:56.860091+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.{yaml,yml,json,toml}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.{yaml,yml,json,toml}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-15T11:33:57.011165+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_PREPARING_20260511T180203.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_PREPARING_20260511T180203.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_env-check_20260511T180230_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_gpu-cleanup_20260511T182535_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_QUEUED_20260511T183926.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_RUNNING_20260511T183930.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_RUNNING_20260511T183937.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-a-oracle-sim_DONE_20260511T183941.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_mvp-a-oracle-sim_20260511T182340_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_PENDING_20260511T185932.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_QUEUED_20260511T185944.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_RUNNING_20260511T185948.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_RUNNING_20260511T185959.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/mvp-b-data-prep_DONE_20260511T190003.json
/home/ubun
…[truncated 12854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 47 · 2026-05-15T11:33:57.213012+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "type": "yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
    "type": "yaml"
  }
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-15T11:33:57.414165+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-15T11:33:57.617350+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "type": "json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
    "type": "json"
  }
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-15T11:33:57.819985+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-15T11:33:57.820444+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "type": "toml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
    "type": "toml"
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-15T11:33:57.870988+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-15T11:33:59.929663+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -maxdepth 3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" \\) | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -maxdepth 3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" \\) | head -30"
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-15T11:34:00.081545+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_eval_home-seed123-ckpt800-then-v5-sweep_20260514T210725_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_fix-repo-level-sample-weight_20260512T112618_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_train_s42-8b-resume-immediate_20260514T204620_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_read-pr-results_20260512T060822_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_collect_critical-ckpt600-test8192-result_20260514T220030_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_fix-repo-level-sample-weight_20260512T141229_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_repo-level-data-prep_20260512T093859_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_research_swebench-pipeline-design_20260511T235646_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_investigate_cwm-v6-sigterm_20260512T203626_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_urgent_cls-8b-s123-recover-and-resume_20260514T142548_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_poll_westd-cuda0-ckpt6633-v2_20260515T080129_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worke
…[truncated 2771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-15T11:34:01.640032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/*.{yaml,yml,json,toml} 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/*.{yaml,yml,json,toml} 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-15T11:34:01.690717+00:00_

-rw------- 1 ubuntu ubuntu  82320 May 15 11:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml
-rw------- 1 ubuntu ubuntu   4454 May 12 00:01 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml
-rw------- 1 ubuntu ubuntu   5679 May 14 00:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml
-rw-r--r-- 1 ubuntu ubuntu  14089 May 15 08:54 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/literature_map.yaml
-rw------- 1 ubuntu ubuntu  23547 May 15 11:00 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_provenance.yaml
-rw------- 1 ubuntu ubuntu 215377 May 15 11:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml
-rw-r--r-- 1 ubuntu ubuntu  16255 May 15 10:28 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-15T11:34:03.498027+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-15T11:34:06.458710+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 2960
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-15T11:34:06.459241+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-15T11:34:06.459473+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-15T11:34:06.509977+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -type f -name \"*.yaml\" -o -name \"*.json\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -type f -name \"*.yaml\" -o -name \"*.json\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-15T11:34:06.610911+00:00_

Exit code 123

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-15T11:34:08.189379+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -type f -name \"*config*\" -o -name \"*settings*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier -type f -name \"*config*\" -o -name \"*settings*\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-15T11:34:08.290244+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_check_cwm-8b-seq-config_20260515T103846.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_ops_diagnose-seed123-vs-v5-config_20260513T204513_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_check_cwm-8b-seq-config_20260515T103846_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_ssh_prep-seed123-launch-configs_20260513T014331.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_ssh_prep-seed123-launch-configs_20260513T014331_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_ops_diagnose-seed123-vs-v5-config_20260513T204513.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.venv/bin/numpy-config
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.venv/lib/python3.14/site-packages/numpy/__config__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.venv/lib/python3.14/site-packages/numpy/__config__.pyi
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.venv/lib/python3.14/site-packages/numpy/typing/tests/data/fail/ufunc_config.pyi
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.venv/lib/python3.14/site-packages/numpy/typing/tests/data/pass/__pycache__/ufunc_config.cpython-314.pyc
/h
…[truncated 1152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-15T11:34:09.846467+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude -type f 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-15T11:34:09.897174+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_015d731a/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_015d731a/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_c38df6bb/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_c38df6bb/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_afc9591d/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_afc9591d/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_2281d02c/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_2281d02c/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_bc5a0163/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_bc5a0163/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_56f4e197/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_56f4e197/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent_52e634ba/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/agent
…[truncated 519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 67 · 2026-05-15T11:34:11.497629+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ | grep -E \"^-\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ | grep -E \"^-\""
  }
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-15T11:34:11.553545+00:00_

-rw-r--r--  1 ubuntu ubuntu  12803 May 15 11:32 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu      0 May 11 18:00 ROADMAP.lock
-rw-------  1 ubuntu ubuntu   4089 May 15 11:32 ROADMAP.md
-rw-r--r--  1 ubuntu ubuntu  11685 May 14 15:22 analyze_cwm_eval.py
-rw-r--r--  1 ubuntu ubuntu   6425 May 11 21:10 build_cwm_data.py
-rw-r--r--  1 ubuntu ubuntu  19740 May 11 18:28 build_data.py
-rw-r--r--  1 ubuntu ubuntu      0 May 11 18:01 decisions.lock
-rw-------  1 ubuntu ubuntu  82320 May 15 11:32 decisions.yaml
-rwxr-xr-x  1 ubuntu ubuntu      0 May 11 21:48 dream_registry.lock
-rw-------  1 ubuntu ubuntu   4454 May 12 00:01 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   4459 May 12 00:01 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu  12573 May 11 21:12 eval_cwm_baseline.py
-rw-r--r--  1 ubuntu ubuntu  12632 May 12 08:23 eval_majority_voting.py
-rw-r--r--  1 ubuntu ubuntu      0 May 12 09:07 experiment_plan.lock
-rw-------  1 ubuntu ubuntu   5679 May 14 00:57 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  14089 May 15 08:54 literature_map.yaml
-rw-r--r--  1 ubuntu ubuntu   9482 May 12 05:54 llm_judge_zeroshot.py
-rw-r--r--  1 ubuntu ubuntu   4798 May 15 11:31 memory.md
-rw-r--r--  1 ubuntu ubuntu  10931 May 11 19:32 mvp_a_total_sim.py
-rw-r--r--  1 ubuntu ubuntu   6793 May 12 17:09 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu      0 May 12 18:08 paper_provenance.lock
-rw-------  1 ubuntu ubuntu  23547 May 15 11:00 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu      0 May 11 18:02 registry.lock
-rw-------  1 ubuntu ubuntu 215377 May 15 11:32 registry.yaml
-rw-r--r--  1 ubuntu ubuntu   5429 May 15 11:32 report.md
-rw-r--r--  1 ubuntu ubuntu   3256 May 12 21:07 run_repo_eval.sh
-rwxr-xr-x  1 ubuntu ubuntu      0 May 11 17:56 study_status.lock
-rw-r--r--  1 ubuntu ubuntu   7768 May 11 21:11 train_cwm_baseline.py
-rw-r--r--  1 ubuntu ubuntu   6615 May 14 17:31 val5120_sweep_commands.txt
-rw-r--r--  1 ubuntu ubuntu  16255 May 15 10:28 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-15T11:34:13.274052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/AGENTS.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/AGENTS.md"
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-15T11:34:13.575724+00:00_

1	## 当前项目
2	当前绑定项目：**exec-sim-repair-verifier**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("exec-sim-repair-verifier")` 或 `load_project_config("exec-sim-repair-verifier", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/`（写文件后用 `register_artifact` 注册）
9	
10	## Worker 操作规范
11	
12	### ssh-env-setup
13	
14	# 远程服务器环境搭建规范
15	
16	## 核心原则
17	
18	**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。
19	
20	**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。
21	
22	**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**
23	
24	## Phase 1: 环境探测（用 ssh_read_only）
25	
26	连接到服务器后，第一步永远是收集信息，不要直接装东西：
27	
28	```bash
29	# 1. Python 环境
30	which python3 && python3 --version
31	pip3 --version 2>/dev/null || echo "NO_PIP"
32	
33	# 2. CUDA 环境
34	nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo "NO_GPU"
35	nvcc --version 2>/dev/null | grep "release" || echo "NO_NVCC"
36	
37	# 3. 包管理器
38	ls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo "NO_CONDA"
39	ls -d .venv venv env 2>/dev/null || echo "NO_VENV"
40	pip3 list --format=freeze 2>/dev/null | grep -iE "torch|transformers|flash" || echo "NO_ML_PKGS"
41	
42	# 4. PEP 668 检查
43	python3 -c "import sysconfig; print(sysconfig.get_path('stdlib'))" 2>/dev/null
44	ls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo "PEP668_MANAGED" || echo "PEP668_OK"
45	```
46	
47	根据探测结果决定安装策略，不要猜。
48	
49	## Phase 2: 环境策略选择
50	
51	根据 Phase 1 结果选择**一个**策略，不要混用：
52	
53	| 探测结果 | 策略 | 说明 |
54	|----------|------|------|
55	| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |
56	| 有 conda 且有写权限 | `conda activate base` 或创
…[truncated 7939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-15T11:34:13.576268+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/*.md 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/*.md 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-15T11:34:13.626825+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-15T11:34:16.037019+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -maxdepth 2 -name \"*.yaml\" -o -name \"*.json\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null || echo \"No config files found with these keywords\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -maxdepth 2 -name \"*.yaml\" -o -name \"*.json\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null || echo \"No config files found with these keywords\""
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-15T11:34:16.087740+00:00_

No config files found with these keywords

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-15T11:34:17.644182+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.json\" -o -name \"config*\" \\) | grep -v projects | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.json\" -o -name \"config*\" \\) | grep -v projects | head -20"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-15T11:34:17.694840+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_83ba13f19a2bf382207991b32ac820f6.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_5304abbd56fd7a7f12edca904ca28ec0.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_paper_agent.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_dream_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_989d6bec30d6e522ac76518ad7326d74.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_b84c6bb36ce09564ec2e2c82b7fe5407.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_8270323eb698ed2e3e1beae8b02b7217.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/session_state.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/mcp_config_worker_95ed9d3a48d9b066b8694f036b259f2a.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-15T11:34:19.152754+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/ 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-15T11:34:19.203412+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-15T11:34:20.458230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-15T11:34:20.508890+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-prod7-0512
5	  my_token: 51b6d0da4e34fec969d66cbdcc0b2e661f6da5a858db345f5a2b2ed7cd803b89
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-15T11:34:22.166785+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -type f -name \"*.yaml\" -o -name \"*.json\" | xargs grep -l \"paperreview\\|external.*review\\|review.*ai\" 2>/dev/null || echo \"No files containing review configuration found\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -type f -name \"*.yaml\" -o -name \"*.json\" | xargs grep -l \"paperreview\\|external.*review\\|review.*ai\" 2>/dev/null || echo \"No files containing review configuration found\""
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-15T11:34:22.317791+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/logs/workers/registry.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_diagnose_cwm-v9-exit2_20260512T232019_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_cwm-v10-diagnose-fix_20260512T233005_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_analysis_majority-voting-results_20260512T093118_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_infra_seetacloud-env-cuda0_20260512T032225_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_research_p2p-regression-rate_20260511T194309_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_ssh_cwm-v10-early-check_20260512T234741_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_diagnose_repo-level-oom-v3_20260512T171155_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_analysis_cwm-error-analysis-and-cls4b-val_20260514T194511_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T214810/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/projects/exec-sim-repair-verifier.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-15T11:34:23.472602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/projects/exec-sim-repair-verifier.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/projects/exec-sim-repair-verifier.yaml"
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-15T11:34:23.472986+00:00_

1	execution:
2	  gpu_ids:
3	  - cuda:0
4	  - cuda:1
5	  - cuda:2
6	  - cuda:3
7	  project_path: /home/sonny/exec-sim-repair-verifier
8	  servers:
9	  - account: root
10	    server: seetacloud-westd-4x5090
11	  - account: sonny
12	    server: home-1x5090
13	feishu:
14	  chat_id: oc_061c4b1115e483e8fdad01cae91c873a
15	  operational_chat_id: oc_b2cf3b1eba4db851529b6a1a7a34c4e8
16	  review_paper_path: projects/exec-sim-repair-verifier/docs/paper/main.tex
17	  review_round: 1
18	  review_supplementary_paths: ''
19	  submission_chat_id: oc_0ae20ec1ce60f9c0589d629648584eff
20	project:
21	  created_at: '2026-05-11T17:56:20.272Z'
22	  description: Per-Test Execution Simulation as Fine-Grained Verifier for Repair Scaling
23	  name: exec-sim-repair-verifier
24	  phase: research
25	  source_idea_id: idea_005
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-15T11:34:25.530978+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -type f \\( -name \"*.yaml\" -o -name \"*.json\" \\) -exec grep -l \"paperreview_ai\" {} \\;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_16 -type f \\( -name \"*.yaml\" -o -name \"*.json\" \\) -exec grep -l \"paperreview_ai\" {} \\;"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-15T11:34:27.538415+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 2007
}
```

</details>

---


### Tool call

_source line 87 · 2026-05-15T11:34:28.893897+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/*.json 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/*.json 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-15T11:34:28.944562+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-15T11:34:30.552163+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -maxdepth 3 -type f -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | xargs grep -l \"external_review\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -maxdepth 3 -type f -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | xargs grep -l \"external_review\" 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-15T11:34:30.603824+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-15T11:34:34.536579+00:00_

Based on my thorough search of the project directory and configuration files, here is my finding:

## Summary

I performed a comprehensive search for project configuration files containing "external_review" or "paperreview" settings in `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/` and the parent configuration directories.

**Search Results:**

1. **Project-level configuration files checked:**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml` - No matches
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml` - No matches
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/*.md` files - No matches

2. **Global configuration files checked:**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/projects/exec-sim-repair-verifier.yaml` - Contains execution settings, chat IDs, and review paths, but NO external_review or paperreview settings
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/config/backend.yaml` - Service configuration only, no review settings

3. **Comprehensive grep searches:**
   - No YAML, JSON, or TOML files found containing "external_review" or "paperreview" keywords
   - No instances of "paperreview_ai.enabled" found anywhere

**Conclusion:**

The setting `external_review.paperreview_ai.enabled` is **not configured** in any configuration file in the project or its parent directories. There are no external review settings present in the codebase—neither enabled (true) nor disabled (false).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Agent",
  "elapsed_ms": 39289
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-15T11:35:32.793017+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**：EMNLP 2026 Main Conference（ARR May cycle）\n- **截止日期**：2026-05-25\n- **格式**：ACL 两栏模板，长文 8 页（不含引用），double-blind 匿名审稿\n- **必须包含**：Limitations section（已有）\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）\n\n### 你的审查侧重\n\n**核心任务：以 EMNLP 最严格审稿人标准，评估论文的方法论严谨性和实验设计。**\n\n请重点审查以下方面：\n\n1. **实验设计公平性**\n   - CLS vs CWM 对比是否 controlled：训练数据、模型大小、超参数、训练 epoch 是否一致？\n   - CWM baseline 是 LoRA fine-tuned 4B/8B，原始 CWM 论文用 32B mid-training。这个对比是否公平？论文是否充分讨论了这一差异？\n   - CLS eval 时用 max_seq_length=5120/8192，CWM 有效输入窗口仅 ~1024（因为要留 1024 给 generation）。这是 confound 还是 formulation 固有属性？论文的 ablation 是否充分回应？\n\n2. **统计声明可靠性**\n   - Repo-level 同尺寸对比仅 1 个 seed（4B s42）。论文声称 25.59pp gap，单 seed 能支撑这个声明吗？\n   - 4B seed123 test=75.33%（vs s42 的 83.63%），seed 方差极大。这是否削弱了 repo-level 结论？\n   - Function-level 3-seed bootstrap p=0.0066 的统计效力：3 个 model instance 能否分离 seed variance 和 systematic scaling effect？\n   - TOST equivalence test with ±2pp margin：这个 margin 的选择是否有依据？\n\n3. **消融分析充分性**\n   - seq_length ablation（CLS@2048 vs CLS@8192，drop 0.69pp）是否充分排除 input context confound？\n   - 是否缺少关键消融：不同 LoRA rank？不同 learning rate？不同数据量？\n   - majority voting 失败（-0.68pp）的讨论是否充分？\n\n4. **数据集构造**\n   - Function-level 数据集来自 HumanEval/MBPP mutation：5 种 mutation type 是否覆盖充分？人工突变 vs 真实 bug 的 gap 是否讨论？\n   - Repo-level 数据：val-test 零 problem overlap 但 mutation type 分布不同（operator_swap val 19.1% → test 34.3%），这是否引入 distribution shift？论文是否充分讨论？\n\n5. **缺失实验**\n   - CWM 8B repo-level 结果缺失（论文说 \"in progress\"）。缺少这个结果，核心 claim（formulation bottleneck vs capacity limitation）能否成立？\n   - 无下游 re-repair 实验验证 diagnostic signal 的实际价值\n   - 无其他模型家族（非 Qwen3）验证\n\n6. **Limitations section 评估**\n   - 当前 Limitations 是否诚实、全面？是否遗漏了关键限制？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary（2-3 句概述）\n\n## Strengths（逐条列出）\n\n## Weaknesses（逐条列出，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有）\n\n## Overall Assessment\n- Score: [strong reject / weak reject / borderline / weak accept / strong accept]\n- Confidence: [1-5]\n- 简要总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**：EMNLP 2026 Main Conference（ARR May cycle）\n- **截止日期**：2026-05-25\n- **格式**：ACL 两栏模板，长文 8 页（不含引用），double-blind 匿名审稿\n- **必须包含**：Limitations section（已有）\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）\n\n### 你的审查侧重\n\n**核心任务：以 EMNLP 最严格审稿人标准，评估论文的方法论严谨性和实验设计。**\n\n请重点审查以下方面：\n\n1. **实验设计公平性**\n   - CLS vs CWM 对比是否 controlled：训练数据、模型大小、超参数、训练 epoch 是否一致？\n   - CWM baseline 是 LoRA fine-tuned 4B/8B，原始 CWM 论文用 32B mid-training。这个对比是否公平？论文是否充分讨论了这一差异？\n   - CLS eval 时用 max_seq_length=5120/8192，CWM 有效输入窗口仅 ~1024（因为要留 1024 给 generation）。这是 confound 还是 formulation 固有属性？论文的 ablation 是否充分回应？\n\n2. **统计声明可靠性**\n   - Repo-level 同尺寸对比仅 1 个 seed（4B s42）。论文声称 25.59pp gap，单 seed 能支撑这个声明吗？\n   - 4B seed123 test=75.33%（vs s42 的 83.63%），seed 方差极大。这是否削弱了 repo-level 结论？\n   - Function-level 3-seed bootstrap p=0.0066 的统计效力：3 个 model instance 能否分离 seed variance 和 systematic scaling effect？\n   - TOST equivalence test with ±2pp margin：这个 margin 的选择是否有依据？\n\n3. **消融分析充分性**\n   - seq_length ablation（CLS@2048 vs CLS@8192，drop 0.69pp）是否充分排除 input context confound？\n   - 是否缺少关键消融：不同 LoRA rank？不同 learning rate？不同数据量？\n   - majority voting 失败（-0.68pp）的讨论是否充分？\n\n4. **数据集构造**\n   - Function-level 数据集来自 HumanEval/MBPP mutation：5 种 mutation type 是否覆盖充分？人工突变 vs 真实 bug 的 gap 是否讨论？\n   - Repo-level 数据：val-test 零 problem overlap 但 mutation type 分布不同（operator_swap val 19.1% → test 34.3%），这是否引入 distribution shift？论文是否充分讨论？\n\n5. **缺失实验**\n   - CWM 8B repo-level 结果缺失（论文说 \"in progress\"）。缺少这个结果，核心 claim（formulation bottleneck vs capacity limitation）能否成立？\n   - 无下游 re-repair 实验验证 diagnostic signal 的实际价值\n   - 无其他模型家族（非 Qwen3）验证\n\n6. **Limitations section 评估**\n   - 当前 Limitations 是否诚实、全面？是否遗漏了关键限制？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary（2-3 句概述）\n\n## Strengths（逐条列出）\n\n## Weaknesses（逐条列出，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有）\n\n## Overall Assessment\n- Score: [strong reject / weak reject / borderline / weak accept / strong accept]\n- Confidence: [1-5]\n- 简要总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 93 · 2026-05-15T11:35:55.320325+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22527
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-15T11:35:55.471488+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**：EMNLP 2026 Main Conference（ARR May cycle）\n- **截止日期**：2026-05-25\n- **格式**：ACL 两栏模板，长文 8 页（不含引用），double-blind 匿名审稿\n- **必须包含**：Limitations section（已有）\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）\n\n### 你的审查侧重\n\n**核心任务：以 EMNLP 最严格审稿人标准，评估论文的贡献新颖性、完整性和写作质量。**\n\n请重点审查以下方面：\n\n1. **贡献新颖性**\n   - \"将 execution simulation 从 generation 改为 classification\" 是否足够新颖？这在 NLP 中是常见的 task reformulation（T5, BART, SQuAD 都做过），应用到 code verification 是否构成足够的贡献？\n   - Complexity-dependent advantage 是 novel insight 还是 obvious observation（generation 在复杂输出上自然更难）？\n   - Oracle accuracy-utility framework（block correlation model）的理论贡献有多大？\n   - 对于 EMNLP main conference 来说，贡献量是否足够？\n\n2. **Framing 和 Story**\n   - 论文 title \"Classification Scales Where Generation Stalls\" 是否准确反映了实际发现？特别是 \"scales\" 这个词——CLS 8B repo-level 实际上没有比 4B 提升（83.63→83.52），所以 \"scales\" 指的是什么？\n   - Introduction 中的三个 contribution 是否都有充分的实验支撑？\n   - \"Per-test diagnostic granularity\" 被作为主要贡献之一，但没有任何下游实验证明其价值。framing 是否 overclaim？\n   - 论文将 CWM failure modes 归因于 \"generation formulation\"，但这些 failure 可能是因为用的模型太小（4B vs 原始 CWM 32B）。framing 是否 misleading？\n\n3. **Related Work 覆盖**\n   - 是否遗漏了重要的相关工作？特别是：\n     - 其他 code execution prediction 工作\n     - Code repair verification 领域的其他方法\n     - Classification vs generation 在其他领域的对比研究\n     - SWE-bench 上的最新 verification 方法\n   - 与 VG-Search (Wang et al., 2025) 的关系讨论是否充分？它也研究 verification granularity\n   - 引用格式是否符合 ACL 规范？引用是否都是真实的？\n\n4. **写作质量**\n   - 论文组织结构是否清晰？各节之间的逻辑衔接？\n   - 数学符号使用是否一致？\n   - 图表是否清晰、信息丰富？Caption 是否 self-contained？\n   - 是否有语法错误、拼写错误、格式问题？\n   - 论文是否在 8 页限制内？（请估算）\n\n5. **格式合规（EMNLP/ACL）**\n   - `\\usepackage[review]{acl}` ✓\n   - 匿名性：是否有任何去匿名化信息？\n   - Limitations section 位置是否正确（conclusion 之后）？\n   - Ethics statement 是否需要？（如涉及人类数据、偏见等）\n   - 引用格式：是否使用 natbib？`\\cite` vs `\\citet` vs `\\citep` 使用是否正确？\n\n6. **引用质量**\n   - 24 条引用是否足够？\n   - 是否有引用看起来可疑（假引用、arXiv ID 不存在等）？\n   - bib 条目格式是否完整（作者列表是否用 \"and others\" 省略太多）？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary（2-3 句概述）\n\n## Strengths（逐条列出）\n\n## Weaknesses（逐条列出，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有）\n\n## Overall Assessment\n- Score: [strong reject / weak reject / borderline / weak accept / strong accept]\n- Confidence: [1-5]\n- 简要总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**：EMNLP 2026 Main Conference（ARR May cycle）\n- **截止日期**：2026-05-25\n- **格式**：ACL 两栏模板，长文 8 页（不含引用），double-blind 匿名审稿\n- **必须包含**：Limitations section（已有）\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）\n\n### 你的审查侧重\n\n**核心任务：以 EMNLP 最严格审稿人标准，评估论文的贡献新颖性、完整性和写作质量。**\n\n请重点审查以下方面：\n\n1. **贡献新颖性**\n   - \"将 execution simulation 从 generation 改为 classification\" 是否足够新颖？这在 NLP 中是常见的 task reformulation（T5, BART, SQuAD 都做过），应用到 code verification 是否构成足够的贡献？\n   - Complexity-dependent advantage 是 novel insight 还是 obvious observation（generation 在复杂输出上自然更难）？\n   - Oracle accuracy-utility framework（block correlation model）的理论贡献有多大？\n   - 对于 EMNLP main conference 来说，贡献量是否足够？\n\n2. **Framing 和 Story**\n   - 论文 title \"Classification Scales Where Generation Stalls\" 是否准确反映了实际发现？特别是 \"scales\" 这个词——CLS 8B repo-level 实际上没有比 4B 提升（83.63→83.52），所以 \"scales\" 指的是什么？\n   - Introduction 中的三个 contribution 是否都有充分的实验支撑？\n   - \"Per-test diagnostic granularity\" 被作为主要贡献之一，但没有任何下游实验证明其价值。framing 是否 overclaim？\n   - 论文将 CWM failure modes 归因于 \"generation formulation\"，但这些 failure 可能是因为用的模型太小（4B vs 原始 CWM 32B）。framing 是否 misleading？\n\n3. **Related Work 覆盖**\n   - 是否遗漏了重要的相关工作？特别是：\n     - 其他 code execution prediction 工作\n     - Code repair verification 领域的其他方法\n     - Classification vs generation 在其他领域的对比研究\n     - SWE-bench 上的最新 verification 方法\n   - 与 VG-Search (Wang et al., 2025) 的关系讨论是否充分？它也研究 verification granularity\n   - 引用格式是否符合 ACL 规范？引用是否都是真实的？\n\n4. **写作质量**\n   - 论文组织结构是否清晰？各节之间的逻辑衔接？\n   - 数学符号使用是否一致？\n   - 图表是否清晰、信息丰富？Caption 是否 self-contained？\n   - 是否有语法错误、拼写错误、格式问题？\n   - 论文是否在 8 页限制内？（请估算）\n\n5. **格式合规（EMNLP/ACL）**\n   - `\\usepackage[review]{acl}` ✓\n   - 匿名性：是否有任何去匿名化信息？\n   - Limitations section 位置是否正确（conclusion 之后）？\n   - Ethics statement 是否需要？（如涉及人类数据、偏见等）\n   - 引用格式：是否使用 natbib？`\\cite` vs `\\citet` vs `\\citep` 使用是否正确？\n\n6. **引用质量**\n   - 24 条引用是否足够？\n   - 是否有引用看起来可疑（假引用、arXiv ID 不存在等）？\n   - bib 条目格式是否完整（作者列表是否用 \"and others\" 省略太多）？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary（2-3 句概述）\n\n## Strengths（逐条列出）\n\n## Weaknesses（逐条列出，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有）\n\n## Overall Assessment\n- Score: [strong reject / weak reject / borderline / weak accept / strong accept]\n- Confidence: [1-5]\n- 简要总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 95 · 2026-05-15T11:35:56.933861+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 96 · 2026-05-15T11:36:03.320106+00:00_

Round 1 任务已分配：
- **Reviewer 1**（方法严谨性）→ 已触发
- **Reviewer 2**（新颖性/完整性）→ 已触发

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 2

## Round 2

2 recorded events


### User

_source line 97 · 2026-05-15T11:41:14.025154+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

**论文**: Classification Scales Where Generation Stalls: Reformulating Execution Simulation for Code Repair Verification
**审查侧重**: 方法论严谨性 + 实验设计
**Venue**: EMNLP 2026 Main Conference (ARR May cycle)

---

## Summary（2-3 句概述）

本文提出将代码修复验证中的执行模拟从开放式输出生成（CWM）重新表述为逐测试二分类（CLS），并在 function-level 和 repo-level 两个复杂度层级进行对比实验。核心发现是 CLS 优势随代码复杂度增长：function-level 差距微小（1.24pp），repo-level 差距剧增至 25.59pp，主要由 CWM 的输出格式合规崩溃驱动。论文同时展示 per-test 分类在 variant-level 准确率上等价于 trajectory-level 评分（TOST p=0.007），同时额外提供逐测试诊断信号。

---

## Strengths

**S1. 干净的受控实验设计框架。** 三种 formulation（CLS/CWM/TRAJ）共享相同基座模型、LoRA 配置、训练数据和 seed，这使得 formulation 差异的归因比较干净。这是论文最大的方法论优势。

**S2. 严谨的统计方法论意识。** 使用 clustered bootstrap 处理 within-problem 相关性（ICC=0.191, DEFF=3.97），TOST 等价检验，以及 block-correlated oracle 模型，展现了高于平均水平的统计素养。论文明确指出 naive i.i.d. CI 会窄约 2×，并在所有检验中修正。

**S3. Oracle accuracy-utility framework 优雅且实用。** Section 3.4 的 block-correlation 模型和 F2P test count 分层分析（Table 3）清晰地刻画了 per-test 粒度的价值边界：69% 的 SWE-bench 实例（T=1）无额外价值，优势集中在 T≥2 的 31% 实例。这为下游部署提供了实用决策框架。

**S4. 诚实的局限性披露。** 论文在多处主动标注限制：repo-level 单 seed、CWM 8B 缺失、hyperparameter 未重新调优、checkpoint selection variance 等。Section 4.6 的 Limitations 段落和 Section 6 的 Limitations 段落互相补充，覆盖面较广。

**S5. Error complementarity 分析有实用价值。** CLS 偏假阴性（75.5%），CWM 偏假阳性（83.1%），oracle 组合达到 90.63%。这自然地指向 ensemble 方向，且对下游系统设计有指导意义。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [Must-Fix] Repo-level 核心 claim 基于单 seed，且 seed 方差极大，不足以支撑论文最突出的数字。**
- 具体位置：Abstract ("the gap amplifies to 25.59pp"), Section 4.6 Table 4, Section 1 贡献列表
- 问题：Repo-level same-size 对比（CLS 4B vs CWM 4B）仅有 seed 42 一个数据点。CLS 4B seed 123 的 val-best checkpoint 准确率仅 75.33%（Section 4.6 Limitations），与 seed 42 的 83.63% 相差 8.3pp。即使论文将此归因于 val-best checkpoint 选择在 early step (800) 放大了 val-test distribution shift，这恰恰说明该实验设置（val-selected checkpoint + distribution shift）的稳定性不足以支撑精确到 25.59pp 的声明。如果取 seed 42 和 seed 123 的均值（~79.5%），CLS-CWM 的 gap 缩小至约 20pp，仍然显著但与 25.59pp 有实质差距。论文在 abstract、introduction 和 conclusion 中反复使用 25.59pp 这一数字作为 headline result，但未在这些位置充分传达其来自单 seed 且存在极大 checkpoint selection variance 的事实。
- 为什么影响接收：这是论文最引人注目的实证 claim，也是 "complexity-dependent advantage" narrative 的关键锚点。单 seed claim 在顶会审稿中会受到严格质疑。
- 建议修改方向：(1) 至少补充 CLS 4B seed 123 vs CWM 4B seed 123 的 same-size 对比（已有两端数据：75.33% vs 59.09%，gap~16pp），在正文中报告多 seed 范围而非单点；(2) 在 abstract 和 introduction 中将 25.59pp 替换为包含方差的区间表述（如 "16-26pp"）；(3) 分析为什么 seed 42 和 seed 123 的 CLS checkpoint selection 差异如此大——是 mutation type distribution shift 的系统性效应还是 checkpoint selection 的随机噪声？

**N2 [Must-Fix] CWM 8B repo-level 结果缺失，核心 claim（"formulation bottleneck vs capacity limitation"）在 repo-level 无法验证。**
- 具体位置：Table 4 ("CWM 8B: ---"), Section 6 Conclusion ("whether this extends to repository scale awaits CWM 8B results")
- 问题：论文的核心叙事是 CWM 的失败是 formulation-level bottleneck 而非 capacity limitation。这一论断在 function-level 有间接支持（CWM 4B→8B 无改善），但在 repo-level（论文声称差距最大、formulation 差异最明显的层级）完全缺乏验证。如果 CWM 8B 在 repo-level 显著好于 CWM 4B，则 "formulation bottleneck" 叙事将被削弱。论文自己在 conclusion 中承认 "whether this extends to repository scale awaits CWM 8B results"，但仍然在 abstract 和 introduction 中以肯定语气阐述该 claim。
- 为什么影响接收：这是论文最核心的理论贡献之一。在最关键的实验条件下缺少数据，论文的 claim 超出了证据支撑范围。
- 建议修改方向：(1) 完成 CWM 8B repo-level 训练（deadline 前 10 天应可完成）；(2) 如无法完成，需在 abstract/introduction 中显著弱化 "formulation bottleneck" 的叙述，改为条件性表述（"if CWM 8B shows similar patterns, this would suggest..."）；(3) 至少讨论如果 CWM 8B repo-level 显著改善会对论文结论产生什么影响。

**N3 [Must-Fix] CWM baseline 的 LoRA fine-tuning 方案可能系统性地低估 generation formulation 的能力，削弱关于 formulation-level limitation 的 claim。**
- 具体位置：Section 4.1 ("Our CWM baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model")
- 问题：原始 CWM 论文使用 32B 模型的 mid-training（大规模持续预训练），而本文的 CWM baseline 是 4B/8B 的 LoRA fine-tuning（rank 16）。LoRA rank 16 给模型增加的可训练参数非常有限（~0.1% of total），这对 generation 任务的影响可能比 classification 大——generation 需要学习从 code context 到 output string 的复杂映射，而 classification 只需学习一个二值决策边界。因此，LoRA 的低秩约束可能不对称地惩罚了 CWM。论文在 Section 4.3 承认 "LoRA rank and learning rate were not re-tuned for 8B"，间接承认了 hyperparameter 配置可能对 CWM 不利。但更根本的问题是：使用 LoRA fine-tuned 4B/8B 模型的 format compliance collapse 来推论 generation formulation 的固有局限是不充分的——一个 32B mid-trained CWM 的 unparseable rate 可能远低于 53-67%。
- 为什么影响接收：论文声称 "the three CWM failure modes are artifacts of the generation formulation, not inherent to the task"（Section 3.3），以及 "format compliance collapse reflects a breakdown in the model's ability to follow the output format"（Section 3.3）。但实验证据来自一个可能因 LoRA 容量不足而被系统性削弱的 CWM 变体。这使得论文无法区分 "generation formulation inherently struggles" 和 "small LoRA-finetuned models struggle to generate complex outputs"。
- 建议修改方向：(1) 增加 LoRA rank 消融实验（如 rank 32, 64, 128），观察 CWM 的 unparseable rate 和准确率是否随 LoRA rank 增加而显著改善——如果是，则说明问题在于模型容量而非 formulation；(2) 在 Section 3.3 和 Section 5 (Related Work) 中明确限定 claim 的范围：当前结论适用于 "LoRA fine-tuned small models"，不应推广到 "generation formulation in general"；(3) 在 Limitations 中讨论 mid-training vs LoRA fine-tuning 的差异对结论的潜在影响。

### Should-Fix（影响评分但不一票否决）

**W1 [Should-Fix] TOST 等价检验的 ±2pp margin 缺乏依据。**
- 具体位置：Section 4.4 ("TOST equivalence test... ±2pp margin"), Section 4.1 ("TOST with ±2pp margin")
- 问题：TOST 等价检验的效力高度依赖 margin 选择。±2pp 是一个看似合理但未被论证的选择。在药物生物等效性（TOST 的原始应用领域），margin 通常设为参考值的 ±20%。若按此标准，88% 准确率的 20% margin 为 ±17.6pp，远大于 ±2pp。论文选择的 ±2pp 实际上是一个非常严格的 margin（~2.3% relative），但如果选择 ±1pp，TOST 可能不 reject；如果选择 ±3pp，结论不变但 claim 更弱。Margin 的选择实质上决定了 "equivalence" 的含义，不应留给读者猜测。
- 建议：(1) 解释 ±2pp 的选择依据——是基于实际应用中可接受的准确率差异、先验工作、还是数据驱动？(2) 报告不同 margin 下 TOST 的结果（如 ±1pp, ±2pp, ±3pp），让读者自行判断。

**W2 [Should-Fix] "Formulation bottleneck" 的 scaling argument 被 hyperparameter 未调优所混淆。**
- 具体位置：Section 4.3 ("The CWM regression (−0.27pp) falls within seed noise... could reflect suboptimal hyperparameter transfer")
- 问题：论文用 CWM 4B→8B 的 -0.27pp 回归来支持 "formulation bottleneck" 论断。但 (1) -0.27pp 在 3-seed std ~0.5pp 内，统计上不显著；(2) 论文承认 LoRA rank 和 lr 未针对 8B 重新调优；(3) 仅 3 个 seed 无法分离 seed variance 和 systematic effect。这三个因素叠加使得 "CWM does not benefit from scaling" 的 claim 过强。一个更准确的表述是 "with the current hyperparameter configuration, CWM does not show measurable scaling improvement, though this may reflect suboptimal hyperparameter transfer."
- 建议：(1) 针对 8B 模型重新搜索 LoRA rank 和 lr；(2) 若无法重做，弱化 scaling argument 的表述，将其降级为 "suggestive evidence" 而非 confirmatory evidence。

**W3 [Should-Fix] Val-test mutation type distribution shift 对 checkpoint selection 的影响未充分分析。**
- 具体位置：Section 4.1 ("Mutation type composition differs between validation and test due to the non-overlapping problem split"), Section 4.6 Limitations ("val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift")
- 问题：Repo-level val 和 test 的 mutation type 分布差异显著（如 operator_swap: val 19.1% → test 34.3%，但这些数字来自 Director 的审稿请求，论文本身未报告具体分布）。CLS 4B seed 123 选中了 step 800 的 early checkpoint，准确率仅 75.33%，而 seed 42 选中的 checkpoint 达到 83.63%——8.3pp 的 seed 间差异远大于 function-level 的 0.78pp std。这种不稳定性暗示 val-based checkpoint selection 在 distribution shift 下可能不可靠。论文将此归因于 "val-best selection at an early checkpoint amplifies the val-test distribution shift"，但未进一步分析：(1) 各 mutation type 的 per-type 准确率是否不同？(2) 分布偏移量与准确率下降之间是否存在系统关系？(3) 是否有更鲁棒的 checkpoint selection 策略？
- 建议：(1) 报告 val/test 的 mutation type 分布；(2) 报告 per-mutation-type 准确率；(3) 考虑使用 per-type validation accuracy 加权的 checkpoint selection。

**W4 [Should-Fix] CWM 使用 exact string matching，未尝试任何 relaxed matching，系统性低估 generation formulation 准确率。**
- 具体位置：Section 3.2 ("The verdict is derived by exact match"), footnote 1 ("Exact string matching is a conservative lower bound... Semantic equivalences are not counted")
- 问题：CWM 的准确率由 exact string matching 决定。footnote 1 承认这是 "conservative lower bound" 并声称与原始 CWM 论文一致。但论文的 claim 是关于 formulation 优劣的因果推断——如果 CWM 在 relaxed matching（如数值近似匹配、忽略空白差异、集合元素顺序无关比较）下准确率显著提高，则 function-level 的 1.24pp gap 可能翻转，scaling argument 也可能改变。论文未提供任何 relaxed matching 的数据点，使读者无法评估 exact matching 对 CWM 准确率的惩罚幅度。
- 建议：至少在 function-level 报告一种 relaxed matching variant 的 CWM 准确率，量化 exact matching 的 penalty。

**W5 [Should-Fix] 人工突变 vs 真实 bug 的生态效度未讨论。**
- 具体位置：Section 4.1 ("generating mutated variants... five mutation types")
- 问题：Function-level 数据集来自 HumanEval/MBPP 的 5 种人工突变（wrong_operator, off_by_one, boundary_error, return_value, type_error）。Mutation testing 文献（如 Andrews et al. 2005, Just et al. 2014）已反复讨论人工突变和真实 bug 之间的 coupling effect 和覆盖差异。5 种突变类型是否充分覆盖真实 bug 的分布？Repo-level 数据来自 SWE-bench Verified mutants，同样是人工突变，不是真实 bug。论文完全未讨论这一 ecological validity concern。
- 建议：在 Limitations 中添加关于人工突变 vs 真实 bug 的讨论，包括为何选择这 5 种突变类型、它们与真实 bug 分布的已知差异、以及这对结论泛化性的影响。

### Minor（不影响接收）

**M1 [Minor] "Below chance level (50%)" 的表述在类别不平衡场景下易引起误解。**
- 具体位置：Section 4.6 ("parseable outputs score only 42–43%—below chance level (50%)")
- 问题：Repo-level 数据集 majority baseline 为 72.96%（always predict pass）。"Chance level" 在不平衡场景下通常指 majority baseline 或 informed random baseline（~60.6%），而非 50%。论文用 50% 作为参照点在技术上是 coin-flip 概率，但在类别不平衡语境下，读者可能认为 50% 是 informative baseline，从而低估 CWM 的实际劣势（相对于 majority baseline 的 -30pp 比相对于 50% 的 -8pp 更触目惊心）。
- 建议：明确说明 50% 指 coin-flip random，并同时报告相对于 majority baseline 的差距。

**M2 [Minor] 引用 yang2024qwen25（Qwen2.5 Technical Report）用于 Qwen3 模型可能不准确。**
- 具体位置：Section 4.1 ("Qwen3-4B and Qwen3-8B (Yang et al., 2024)")
- 问题：论文使用的是 Qwen3 系列模型，但引用的 yang2024qwen25 是 Qwen2.5 的技术报告。如果 Qwen3 有独立的技术报告或发布公告，应引用正确的文献。
- 建议：核实并更新引用。

**M3 [Minor] 混合精度 seed 的处理。**
- 具体位置：Section 4.1 ("Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization")
- 问题：5-seed 统计（Table 1）混合了两种精度的结果。虽然 Section 4.3 的 scaling 分析正确地只使用了 matched-precision (bfloat16) 的 3 个 seed，但 Table 1 的 5-seed mean 和 std 包含了 NF4 量化的 seed，这可能引入非 seed variance 的精度效应。
- 建议：在 Table 1 中标注哪些 seed 使用了 NF4 量化，或报告 matched-precision 子集的统计量。

**M4 [Minor] Unparseable outputs 的处理策略未明确说明。**
- 具体位置：Section 4.6 Table 4
- 问题：CWM 产生 53.7-67.2% 的 unparseable outputs，但论文未明确说明这些 unparseable outputs 在计算 overall accuracy 时如何处理（assign to majority class? random? always wrong?）。
- 建议：明确说明 unparseable outputs 的 verdict assignment 策略。

---

## Questions（需要作者回答的问题）

**Q1.** CWM 在 repo-level 训练时的 max_seq_length 也是 2048，eval 时的 total budget 是否也是 2048（即 ~1024 input + ~1024 generation）？如果将 CWM 的 eval 时 max_seq_length 提高到 8192（~7168 input + 1024 generation），unparseable rate 和 accuracy 是否会变化？论文的 matched-context ablation 只调了 CLS 的 context downward，但未尝试 CWM 的 context upward。

**Q2.** CLS 4B seed 123 选中 step 800 的 checkpoint，CLS 4B seed 42 选中了哪个 step？两者的 val accuracy 和 test accuracy 是否存在系统性关系（如 val accuracy 高但 test accuracy 低），暗示 val-test distribution shift 的方向性？

**Q3.** LoRA rank 16 对 CWM 是否足够？是否尝试过更大的 rank（32, 64）？如果 rank 增加后 CWM 的 unparseable rate 下降，这将支持 "capacity limitation" 解释而非 "formulation bottleneck"。

**Q4.** Majority voting 失效（-0.68pp）的分析中，3 个 seed 的 pairwise agreement rate 是多少？errors 在 seed 间的 overlap 比例是多少？

**Q5.** Oracle ensemble（CLS+CWM）达到 90.63%，但这是在 function-level。Repo-level 的 oracle ensemble 结果如何？如果 CWM 在 repo-level 是 anti-informative 的，oracle ensemble 是否反而更差？

**Q6.** 5 种 mutation type 的选择依据是什么？是否有覆盖率分析或与真实 bug 分布的对比？

---

## Missing References

- Andrews, J.H., Briand, L.C., & Labiche, Y. (2005). Is Mutation an Appropriate Tool for Testing Experiments? ICSE. — 人工突变 vs 真实 fault 的经典讨论，与数据集构造直接相关。
- Just, R., Jalali, D., Inozemtseva, L., et al. (2014). Are Mutants a Valid Substitute for Real Faults in Software Testing? FSE. — 同上。
- 论文 Section 5 (Related Work) 中的 VG-Search (Wang et al., 2025) 讨论了 verification granularity 对 test-time scaling 的影响，与本文的 per-test vs trajectory-level 对比直接相关。建议在 introduction 中更早提及，以建立更强的 motivation。

---

## Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 2.5/5 | Repo-level 核心 claim 基于单 seed 且 seed 方差极大；CWM baseline 的 LoRA fine-tuning 可能系统性低估 generation formulation 能力；CWM 8B repo-level 缺失使 "formulation bottleneck" claim 无法在最关键条件下验证。Function-level 实验设计较好但统计效力受限于 3 model instances。|
| **Excitement** | 3/5 | 将 execution simulation 从 generation 重新表述为 classification 的思路新颖且有实用价值；oracle accuracy-utility framework 优雅。但当前实验证据不足以支撑论文的 claim 强度。|
| **Overall** | 2.5/5 | 核心思路值得发表，但实验设计存在多处方法论缺陷：单 seed claim、缺失实验、CWM baseline 可能被系统性削弱。需要至少完成 CWM 8B repo-level 实验、补充 LoRA rank 消融、以及在 abstract/introduction 中校准 claim 强度。建议在下一个 ARR cycle 重新提交。|
| **Confidence** | 4/5 | 仔细阅读全文，熟悉 code LLM verification、LoRA fine-tuning 和统计检验方法。不确定的部分：CWM original paper 的具体 mid-training 细节。|
| **Reproducibility** | 3/5 | Seeds、hyperparameters、数据集规模有详细报告。但 unparseable output 的处理策略未明确、mutation generation 的具体实现未提供代码链接。|

### 简要总评

**Score: 2.5（Resubmit next cycle）**

论文提出了一个有价值的 research question（execution simulation 是否必须通过 generation 实现），实验设计框架本身（controlled formulation comparison）值得肯定，统计方法论（clustered bootstrap, TOST, ICC）展现了专业水准。

然而，三个 Must-Fix 问题共同削弱了论文的核心 claim：(1) 最突出的 repo-level 数字（25.59pp）来自单 seed 且存在极大 checkpoint selection variance；(2) "formulation bottleneck" 叙事在最关键的 repo-level 层级缺少 CWM 8B 数据验证；(3) CWM baseline 可能因 LoRA 容量限制而被系统性低估，使得论文无法区分 "generation formulation inherently struggles" 和 "small LoRA-finetuned models struggle to generate complex outputs"。

这三个问题中，(1) 和 (2) 可以通过补充实验在一个 ARR cycle 内解决。(3) 需要 LoRA rank 消融实验来量化 capacity vs formulation 的贡献。如果这些补充实验支持当前结论，论文将是一篇扎实的 Findings 级工作；如果 CWM 8B 或 larger LoRA rank 显著改善了 CWM 的 repo-level 表现，则需要重新校准 claim 的范围和强度。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 98 · 2026-05-15T11:41:27.652175+00:00_

Reviewer 1 审稿意见已收到。评分 2.5/5，提出 3 个 Must-Fix（单 seed claim、CWM 8B 缺失、LoRA baseline 公平性）、5 个 Should-Fix、4 个 Minor。

等待 Reviewer 2 审稿意见返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 99 · 2026-05-15T11:41:30.262488+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成要点：**

- **总分 2.5/5（建议下 cycle 重投）**，Soundness 2.5、Excitement 3
- 识别 **3 个 Must-Fix 问题**：(1) repo-level 25.59pp claim 基于单 seed，另一 seed 差距仅 ~16pp；(2) CWM 8B repo-level 缺失无法验证 "formulation bottleneck" 核心论断；(3) LoRA rank 16 的 CWM baseline 可能系统性低估 generation formulation 能力，无法区分 formulation limitation 和 model capacity limitation
- 识别 **5 个 Should-Fix**：TOST margin 无依据、scaling argument 被未调优 hyperparameter 混淆、val-test distribution shift 分析不充分、CWM exact matching 未尝试 relaxed variant、人工突变 ecological validity 未讨论
- 识别 **4 个 Minor** 问题和 **6 个 Questions**
- 统计方法论（clustered bootstrap、ICC、TOST）获得正面评价；oracle framework 被认为优雅实用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 100 · 2026-05-15T11:41:38.854028+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 4

## Round 4

6 recorded events


### User

_source line 101 · 2026-05-15T11:42:14.336235+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性 + 写作质量）

### Summary（2-3 句概述）

本文将代码修复验证中的执行模拟从开放式输出生成（CWM）重新表述为逐测试二分类（CLS），并在函数级和仓库级基准上系统比较 CLS、CWM 和 trajectory-level 三种形式化。核心发现是重新表述的优势随代码复杂度递增：函数级差距仅 1.24pp，仓库级差距扩大到 25.59pp（主要由 CWM 格式崩溃驱动）。此外，逐测试分类在 variant 级准确率上与 trajectory-level 等效，同时提供诊断粒度。

---

### Strengths

**S1. 控制严格的实验设计。** 三种形式化使用相同模型（Qwen3-4B/8B）、相同数据、相同训练配置（LoRA rank/lr/epochs），排除了模型和数据差异带来的混淆因素。这是该领域少见的 apples-to-apples 比较（Section 4.1）。

**S2. 统计方法扎实。** 使用 clustered bootstrap（114 problem clusters, 10K resamples）处理 within-problem correlation，用 TOST 等价检验（而非简单 t-test）确认 CLS-TRAJ 等价性，报告 ICC 和 design effect（Section 4.2, 4.4）。

**S3. CWM 仓库级失败模式的定量刻画有实用价值。** 53.7-67.2% unparseable + parseable 部分 42-43% 准确率（低于 chance），这对实践者有直接警示意义（Section 4.5, Table 3）。

**S4. Oracle accuracy-utility framework 提供了实用决策框架。** ICC-based block correlation model 量化了逐测试粒度的价值分布（Section 3.4, Table 2）。

**S5. 局限性披露诚实。** 主动承认单 seed、CWM 8B 缺失、无下游实验等局限。

---

### Weaknesses

#### Must-Fix（影响接收决定）

**W1 [Must-Fix] 核心贡献新颖性不足以支撑 EMNLP main。**
- "将 generation 改为 classification"是 NLP 成熟技术路线（论文自己在 Related Work Section 5 para 4 引用 T5/BART/SQuAD）。
- "Complexity-dependent advantage"定性方向可预期：generation 在复杂输出上退化是已知局限。Ye et al. [ye2025demystifying] 已识别 failure modes；CodeMind [liu2024codemind] 已发现 performance drops with complexity。
- 贡献是量化已知趋势，而非发现新现象。

**W2 [Must-Fix] 仓库级核心结论（25.59pp gap）基于单 seed，checkpoint selection variance 极大。**
- CLS 4B seed 42: 83.63%，但 seed 123: 75.33%——差异 8.3pp。
- 换 seed 后 CLS 仅比 majority baseline 高 2.4pp，结论可能完全不同。
- 标题和 abstract 仍以 25.59pp 作为核心宣传数字，对读者有误导。

**W3 [Must-Fix] CWM baseline 是 4B LoRA，但结论推广到 "generation formulation" 整体，存在 overclaim。**
- Introduction para 3："CWM failure modes are artifacts of the generation formulation, not inherent to the task"
- 但原始 CWM 是 32B mid-trained 模型。4B LoRA 的 format compliance collapse 可能反映模型容量不足，而非 generation 固有缺陷。
- 无证据表明 32B CWM 会有同样问题。CWM 8B 结果缺失（Table 3 标"---"）。

**W4 [Must-Fix] 标题 "scales" 缺乏数据支撑。**
- 函数级 4B→8B: CLS +0.99pp（微弱）
- 仓库级 4B→8B: CLS 83.63→83.52（seed 42, 无改善）
- Section 4.5 自己承认 "classification may be approaching a capacity ceiling"

#### Should-Fix

**W5 [Should-Fix] "Per-test diagnostic granularity" 被列为主要贡献但无下游实验验证。** Contribution 2 声称 "enables targeted re-repair"，但 Conclusion 承认没有实验验证。Overclaim。

**W6 [Should-Fix] 遗漏重要相关工作 LEVER (Ni et al., ICML 2023)。** LEVER 训练分类器验证代码生成结果，与 CLS 精神上高度相似。还遗漏 CodeT (Chen et al., ICLR 2023)。

**W7 [Should-Fix] TOST ±2pp margin 无正当性论证。** 为什么是 2pp？用 ±1pp 结论是否改变？

**W8 [Should-Fix] 多条引用 first author 与 arXiv/OpenAlex 记录不一致。** wu2025patchreasoner（bib: Wu Zuxin, arXiv: Xu Junjielong）、ding2025selfexecution（bib: Ding, API: Maimon）等。

**W9 [Should-Fix] 数据集为合成 mutant，未讨论 synthetic-to-real gap。**

#### Minor

**M1** Abstract 信息密度过高（15+ 数字）。**M2** "D088 protocol" 未定义。**M3** 关键数字四次重复出现（abstract/intro/experiments/conclusion）。**M4** \cite vs \citep 使用不完全一致。**M5** 26 条引用对 EMNLP 长文偏少。

---

### Questions

**Q1.** 32B CWM 仓库级是否仍有 format compliance collapse？若无，核心 claim 是否成立？
**Q2.** CLS 4B seed 42 vs 123 差 8.3pp 的根源？
**Q3.** TOST ±2pp margin 依据？±1pp 时结论是否改变？
**Q4.** CWM 低方差被解释为 bottleneck hypothesis，但也可能是更稳定的特征——如何排除？
**Q5.** 匹配上下文消融仅有 CLS 8B 单 seed，能否补充 4B？
**Q6.** Per-test granularity "enables re-repair" 有任何初步实验支持吗？

---

### Missing References

1. LEVER (Ni et al., ICML 2023) — learned code verifier
2. CodeT (Chen et al., ICLR 2023) — dual execution agreement
3. 建议增加 "Learned Code Verifiers" 讨论段

---

### Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 函数级严谨，仓库级单 seed + 极大 variance；从 4B LoRA 推广到 generation formulation 整体缺乏支撑 |
| Excitement | 2/5 | "CLS > GEN on complex output" 可预期；Oracle framework 有一定新意但有限 |
| Overall | 2.5/5 | 介于 Findings 和 Resubmit；实验工艺好但新颖性不足 |
| Reproducibility | 3.5/5 | 训练细节充分但数据集构造细节不完整 |
| Confidence | 4/5 | 熟悉相关文献 |

**Score: Borderline (leaning weak reject)**

核心障碍：（1）定量确认可预期结论的新颖性有限；（2）仓库级结果单 seed + 极大 variance；（3）从 4B LoRA CWM 推广到 generation formulation 一般性缺陷证据不足。当前状态更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-15T11:43:09.717446+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：你和 R1 在 \"新颖性\" 维度有分歧——R1 给 Excitement 3/5 认为思路新颖有价值，你给 2/5 认为可预期。请在交叉回应中重点论证你的立场。\n\n---\n\n# Reviewer 1 — Round 1 审稿意见（完整原文）\n\n**论文**: Classification Scales Where Generation Stalls: Reformulating Execution Simulation for Code Repair Verification\n**审查侧重**: 方法论严谨性 + 实验设计\n\n## Summary\n本文提出将代码修复验证中的执行模拟从开放式输出生成（CWM）重新表述为逐测试二分类（CLS），并在 function-level 和 repo-level 两个复杂度层级进行对比实验。核心发现是 CLS 优势随代码复杂度增长：function-level 差距微小（1.24pp），repo-level 差距剧增至 25.59pp，主要由 CWM 的输出格式合规崩溃驱动。论文同时展示 per-test 分类在 variant-level 准确率上等价于 trajectory-level 评分（TOST p=0.007），同时额外提供逐测试诊断信号。\n\n## Strengths\n\n**S1.** 干净的受控实验设计框架。三种 formulation 共享相同基座模型、LoRA 配置、训练数据和 seed。\n\n**S2.** 严谨的统计方法论意识。Clustered bootstrap、TOST、ICC、block-correlated oracle model。\n\n**S3.** Oracle accuracy-utility framework 优雅且实用。Block-correlation model 和 F2P test count 分层分析清晰刻画 per-test 粒度的价值边界。\n\n**S4.** 诚实的局限性披露。\n\n**S5.** Error complementarity 分析有实用价值。CLS 偏假阴性，CWM 偏假阳性，oracle 组合达 90.63%。\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [Must-Fix]** Repo-level 核心 claim 基于单 seed，且 seed 方差极大（CLS 4B: s42=83.63% vs s123=75.33%，差 8.3pp）。25.59pp 在 abstract/intro/conclusion 反复使用但未充分传达其来自单 seed。建议报告多 seed 范围（16-26pp）。\n\n**N2 [Must-Fix]** CWM 8B repo-level 结果缺失，\"formulation bottleneck vs capacity limitation\" 在 repo-level 无法验证。论文在 conclusion 承认但在 abstract/intro 中以肯定语气阐述。\n\n**N3 [Must-Fix]** CWM baseline 的 LoRA fine-tuning（rank 16, ~0.1% params）可能系统性低估 generation formulation 能力。LoRA 低秩约束对 generation 的惩罚可能比 classification 大。无法区分 \"generation formulation inherently struggles\" 和 \"small LoRA-finetuned models struggle\"。建议增加 LoRA rank 消融。\n\n### Should-Fix\n\n**W1 [Should-Fix]** TOST ±2pp margin 缺乏依据。\n\n**W2 [Should-Fix]** Scaling argument 被未调优 hyperparameter 混淆（CWM -0.27pp 在 seed noise 内，LoRA rank/lr 未为 8B 重新调优）。\n\n**W3 [Should-Fix]** Val-test mutation type distribution shift 对 checkpoint selection 的影响未充分分析。\n\n**W4 [Should-Fix]** CWM exact string matching 未尝试 relaxed matching，系统性低估 generation 准确率。\n\n**W5 [Should-Fix]** 人工突变 vs 真实 bug 的 ecological validity 未讨论。\n\n### Minor\n\n**M1** \"Below chance level (50%)\" 在类别不平衡场景下易误解。\n**M2** Qwen3 引用了 Qwen2.5 技术报告。\n**M3** 混合精度 seed 处理。\n**M4** Unparseable outputs 处理策略未明确。\n\n## Questions\n\nQ1. CWM eval 时提高 max_seq_length 到 8192，unparseable rate 是否变化？\nQ2. CLS 4B seed 42 选中了哪个 step？\nQ3. 是否尝试过更大的 LoRA rank？\nQ4. Majority voting 失效的 pairwise agreement rate？\nQ5. Repo-level oracle ensemble 结果？\nQ6. 5 种 mutation type 选择依据？\n\n## Missing References\n- Andrews et al. (2005) ICSE — mutation vs real faults\n- Just et al. (2014) FSE — same topic\n- VG-Search 应在 introduction 更早提及\n\n## Overall Assessment\nScore: 2.5（Resubmit next cycle）, Confidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：你和 R1 在 \"新颖性\" 维度有分歧——R1 给 Excitement 3/5 认为思路新颖有价值，你给 2/5 认为可预期。请在交叉回应中重点论证你的立场。\n\n---\n\n# Reviewer 1 — Round 1 审稿意见（完整原文）\n\n**论文**: Classification Scales Where Generation Stalls: Reformulating Execution Simulation for Code Repair Verification\n**审查侧重**: 方法论严谨性 + 实验设计\n\n## Summary\n本文提出将代码修复验证中的执行模拟从开放式输出生成（CWM）重新表述为逐测试二分类（CLS），并在 function-level 和 repo-level 两个复杂度层级进行对比实验。核心发现是 CLS 优势随代码复杂度增长：function-level 差距微小（1.24pp），repo-level 差距剧增至 25.59pp，主要由 CWM 的输出格式合规崩溃驱动。论文同时展示 per-test 分类在 variant-level 准确率上等价于 trajectory-level 评分（TOST p=0.007），同时额外提供逐测试诊断信号。\n\n## Strengths\n\n**S1.** 干净的受控实验设计框架。三种 formulation 共享相同基座模型、LoRA 配置、训练数据和 seed。\n\n**S2.** 严谨的统计方法论意识。Clustered bootstrap、TOST、ICC、block-correlated oracle model。\n\n**S3.** Oracle accuracy-utility framework 优雅且实用。Block-correlation model 和 F2P test count 分层分析清晰刻画 per-test 粒度的价值边界。\n\n**S4.** 诚实的局限性披露。\n\n**S5.** Error complementarity 分析有实用价值。CLS 偏假阴性，CWM 偏假阳性，oracle 组合达 90.63%。\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [Must-Fix]** Repo-level 核心 claim 基于单 seed，且 seed 方差极大（CLS 4B: s42=83.63% vs s123=75.33%，差 8.3pp）。25.59pp 在 abstract/intro/conclusion 反复使用但未充分传达其来自单 seed。建议报告多 seed 范围（16-26pp）。\n\n**N2 [Must-Fix]** CWM 8B repo-level 结果缺失，\"formulation bottleneck vs capacity limitation\" 在 repo-level 无法验证。论文在 conclusion 承认但在 abstract/intro 中以肯定语气阐述。\n\n**N3 [Must-Fix]** CWM baseline 的 LoRA fine-tuning（rank 16, ~0.1% params）可能系统性低估 generation formulation 能力。LoRA 低秩约束对 generation 的惩罚可能比 classification 大。无法区分 \"generation formulation inherently struggles\" 和 \"small LoRA-finetuned models struggle\"。建议增加 LoRA rank 消融。\n\n### Should-Fix\n\n**W1 [Should-Fix]** TOST ±2pp margin 缺乏依据。\n\n**W2 [Should-Fix]** Scaling argument 被未调优 hyperparameter 混淆（CWM -0.27pp 在 seed noise 内，LoRA rank/lr 未为 8B 重新调优）。\n\n**W3 [Should-Fix]** Val-test mutation type distribution shift 对 checkpoint selection 的影响未充分分析。\n\n**W4 [Should-Fix]** CWM exact string matching 未尝试 relaxed matching，系统性低估 generation 准确率。\n\n**W5 [Should-Fix]** 人工突变 vs 真实 bug 的 ecological validity 未讨论。\n\n### Minor\n\n**M1** \"Below chance level (50%)\" 在类别不平衡场景下易误解。\n**M2** Qwen3 引用了 Qwen2.5 技术报告。\n**M3** 混合精度 seed 处理。\n**M4** Unparseable outputs 处理策略未明确。\n\n## Questions\n\nQ1. CWM eval 时提高 max_seq_length 到 8192，unparseable rate 是否变化？\nQ2. CLS 4B seed 42 选中了哪个 step？\nQ3. 是否尝试过更大的 LoRA rank？\nQ4. Majority voting 失效的 pairwise agreement rate？\nQ5. Repo-level oracle ensemble 结果？\nQ6. 5 种 mutation type 选择依据？\n\n## Missing References\n- Andrews et al. (2005) ICSE — mutation vs real faults\n- Just et al. (2014) FSE — same topic\n- VG-Search 应在 introduction 更早提及\n\n## Overall Assessment\nScore: 2.5（Resubmit next cycle）, Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-15T11:43:32.559621+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22842
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-15T11:43:32.861195+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：你在 Excitement 给了 3/5，R2 给了 2/5 并认为新颖性不足是核心障碍。请在交叉回应中重点论证你的立场。另外 R2 提出了标题 \"scales\" 缺乏支撑（W4）和遗漏 LEVER/CodeT 引用（W6），请评估这些观点。\n\n---\n\n# Reviewer 2 — Round 1 审稿意见（完整原文）\n\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n## Summary\n本文将代码修复验证中的执行模拟从开放式输出生成（CWM）重新表述为逐测试二分类（CLS），并在函数级和仓库级基准上系统比较 CLS、CWM 和 trajectory-level 三种形式化。核心发现是重新表述的优势随代码复杂度递增：函数级差距仅 1.24pp，仓库级差距扩大到 25.59pp。\n\n## Strengths\nS1. 控制严格的实验设计。\nS2. 统计方法扎实。\nS3. CWM 仓库级失败模式的定量刻画有实用价值。\nS4. Oracle accuracy-utility framework 提供实用决策框架。\nS5. 局限性披露诚实。\n\n## Weaknesses\n\n### Must-Fix\n\n**W1 [Must-Fix]** 核心贡献新颖性不足以支撑 EMNLP main。\"将 generation 改为 classification\"是 NLP 成熟路线（T5/BART/SQuAD）。\"Complexity-dependent advantage\"可预期——generation 在复杂输出上退化是已知局限（Ye et al., CodeMind 已识别）。贡献是量化已知趋势而非发现新现象。\n\n**W2 [Must-Fix]** 仓库级核心结论（25.59pp gap）基于单 seed，checkpoint selection variance 极大。CLS 4B seed 42: 83.63%，seed 123: 75.33%——差异 8.3pp。标题和 abstract 仍以 25.59pp 作为核心宣传数字。\n\n**W3 [Must-Fix]** CWM baseline 是 4B LoRA，但结论推广到 \"generation formulation\" 整体，存在 overclaim。Introduction para 3：\"CWM failure modes are artifacts of the generation formulation, not inherent to the task\"。无证据表明 32B CWM 会有同样问题。\n\n**W4 [Must-Fix]** 标题 \"scales\" 缺乏数据支撑。函数级 4B→8B: CLS +0.99pp（微弱）。仓库级 4B→8B: CLS 83.63→83.52（seed 42, 无改善）。Section 4.5 自己承认 \"classification may be approaching a capacity ceiling\"。\n\n### Should-Fix\n\n**W5 [Should-Fix]** \"Per-test diagnostic granularity\" 列为主要贡献但无下游实验验证。\n\n**W6 [Should-Fix]** 遗漏重要相关工作 LEVER (Ni et al., ICML 2023) 和 CodeT (Chen et al., ICLR 2023)。\n\n**W7 [Should-Fix]** TOST ±2pp margin 无正当性论证。\n\n**W8 [Should-Fix]** 多条引用 first author 与 arXiv/OpenAlex 记录不一致。\n\n**W9 [Should-Fix]** 数据集为合成 mutant，未讨论 synthetic-to-real gap。\n\n### Minor\nM1. Abstract 信息密度过高。M2. \"D088 protocol\" 未定义。M3. 关键数字四次重复。M4. \\cite vs \\citep 不一致。M5. 26 条引用偏少。\n\n## Questions\nQ1. 32B CWM 仓库级是否仍有 format compliance collapse？\nQ2. CLS 4B seed 42 vs 123 差 8.3pp 的根源？\nQ3. TOST ±2pp 依据？±1pp 时结论是否改变？\nQ4. CWM 低方差被解释为 bottleneck，也可能是更稳定特征？\nQ5. 匹配上下文消融仅有 CLS 8B 单 seed，能否补充 4B？\nQ6. Per-test granularity \"enables re-repair\" 有初步实验支持吗？\n\n## Missing References\n1. LEVER (Ni et al., ICML 2023)\n2. CodeT (Chen et al., ICLR 2023)\n3. 建议增加 \"Learned Code Verifiers\" 讨论段\n\n## Overall Assessment\nScore: Borderline (leaning weak reject), Confidence: 4/5\n核心障碍：新颖性不足 + 仓库级单 seed + LoRA overclaim。当前状态更适合 Findings。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：你在 Excitement 给了 3/5，R2 给了 2/5 并认为新颖性不足是核心障碍。请在交叉回应中重点论证你的立场。另外 R2 提出了标题 \"scales\" 缺乏支撑（W4）和遗漏 LEVER/CodeT 引用（W6），请评估这些观点。\n\n---\n\n# Reviewer 2 — Round 1 审稿意见（完整原文）\n\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n## Summary\n本文将代码修复验证中的执行模拟从开放式输出生成（CWM）重新表述为逐测试二分类（CLS），并在函数级和仓库级基准上系统比较 CLS、CWM 和 trajectory-level 三种形式化。核心发现是重新表述的优势随代码复杂度递增：函数级差距仅 1.24pp，仓库级差距扩大到 25.59pp。\n\n## Strengths\nS1. 控制严格的实验设计。\nS2. 统计方法扎实。\nS3. CWM 仓库级失败模式的定量刻画有实用价值。\nS4. Oracle accuracy-utility framework 提供实用决策框架。\nS5. 局限性披露诚实。\n\n## Weaknesses\n\n### Must-Fix\n\n**W1 [Must-Fix]** 核心贡献新颖性不足以支撑 EMNLP main。\"将 generation 改为 classification\"是 NLP 成熟路线（T5/BART/SQuAD）。\"Complexity-dependent advantage\"可预期——generation 在复杂输出上退化是已知局限（Ye et al., CodeMind 已识别）。贡献是量化已知趋势而非发现新现象。\n\n**W2 [Must-Fix]** 仓库级核心结论（25.59pp gap）基于单 seed，checkpoint selection variance 极大。CLS 4B seed 42: 83.63%，seed 123: 75.33%——差异 8.3pp。标题和 abstract 仍以 25.59pp 作为核心宣传数字。\n\n**W3 [Must-Fix]** CWM baseline 是 4B LoRA，但结论推广到 \"generation formulation\" 整体，存在 overclaim。Introduction para 3：\"CWM failure modes are artifacts of the generation formulation, not inherent to the task\"。无证据表明 32B CWM 会有同样问题。\n\n**W4 [Must-Fix]** 标题 \"scales\" 缺乏数据支撑。函数级 4B→8B: CLS +0.99pp（微弱）。仓库级 4B→8B: CLS 83.63→83.52（seed 42, 无改善）。Section 4.5 自己承认 \"classification may be approaching a capacity ceiling\"。\n\n### Should-Fix\n\n**W5 [Should-Fix]** \"Per-test diagnostic granularity\" 列为主要贡献但无下游实验验证。\n\n**W6 [Should-Fix]** 遗漏重要相关工作 LEVER (Ni et al., ICML 2023) 和 CodeT (Chen et al., ICLR 2023)。\n\n**W7 [Should-Fix]** TOST ±2pp margin 无正当性论证。\n\n**W8 [Should-Fix]** 多条引用 first author 与 arXiv/OpenAlex 记录不一致。\n\n**W9 [Should-Fix]** 数据集为合成 mutant，未讨论 synthetic-to-real gap。\n\n### Minor\nM1. Abstract 信息密度过高。M2. \"D088 protocol\" 未定义。M3. 关键数字四次重复。M4. \\cite vs \\citep 不一致。M5. 26 条引用偏少。\n\n## Questions\nQ1. 32B CWM 仓库级是否仍有 format compliance collapse？\nQ2. CLS 4B seed 42 vs 123 差 8.3pp 的根源？\nQ3. TOST ±2pp 依据？±1pp 时结论是否改变？\nQ4. CWM 低方差被解释为 bottleneck，也可能是更稳定特征？\nQ5. 匹配上下文消融仅有 CLS 8B 单 seed，能否补充 4B？\nQ6. Per-test granularity \"enables re-repair\" 有初步实验支持吗？\n\n## Missing References\n1. LEVER (Ni et al., ICML 2023)\n2. CodeT (Chen et al., ICLR 2023)\n3. 建议增加 \"Learned Code Verifiers\" 讨论段\n\n## Overall Assessment\nScore: Borderline (leaning weak reject), Confidence: 4/5\n核心障碍：新颖性不足 + 仓库级单 seed + LoRA overclaim。当前状态更适合 Findings。"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-15T11:43:34.221996+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1360
}
```

</details>

---


### Assistant

_source line 106 · 2026-05-15T11:43:37.871208+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 107 · 2026-05-15T11:43:40.564905+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **Borderline (leaning weak reject)**，Overall 2.5/5。四个 Must-Fix 问题：（1）核心贡献新颖性不足——"分类优于生成"是可预期结论；（2）仓库级 25.59pp gap 基于单 seed，另一 seed 差 8.3pp；（3）从 4B LoRA CWM 推广到 generation formulation 整体属于 overclaim；（4）标题中 "scales" 缺乏数据支撑。五个 Should-Fix，包括遗漏 LEVER (ICML 2023) 等重要相关工作、TOST margin 缺乏论证、per-test granularity 无下游验证。当前状态更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 108 · 2026-05-15T11:43:47.360586+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 109 · 2026-05-15T11:45:52.300783+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应

### Strengths
- [AGREE] R1-S1 至 R1-S5：全部同意。与我的 R2-S1/S2/S4/S5 一致。R1-S5（error complementarity）是我 Round 1 未单独列出但认同的 strength。

### Must-Fix
- [AGREE] R1-N1（单 seed repo-level）：与 R2-W2 一致。补充：seed 123 的 val-best 是 step 800（Section 4.5），seed 间差异可能叠加 checkpoint 阶段的系统性偏差。
- [AGREE] R1-N2（CWM 8B 缺失）：与 R2-W3 重叠。论文的核心因果声明在 repo-level 是未验证假设，不是结论。
- [AGREE] R1-N3（LoRA rank 16 对 generation 的不对称惩罚）：**R1 独有的重要观察**，我 Round 1 未从此角度分析。LoRA 低秩约束对 generation（需学习精确 token 序列）的限制可能大于 classification（仅二分类），引入未控制的混淆因素。LoRA rank 消融是必要的控制实验。这与 R1-W2（hyperparameter 未 retune）形成链式论证。

### Should-Fix
- [AGREE] R1-W1（TOST ±2pp）、R1-W2（hyperparameter 混淆）、R1-W3（val-test shift）、R1-W5（synthetic mutations）：与我的 R2-W7/W9 一致。
- [AGREE] R1-W4（CWM exact matching 未尝试 relaxed matching）：**我 Round 1 遗漏的重要问题**。Section 3.2 footnote 称 exact match 是"conservative lower bound"，但不尝试 relaxed matching 就无法量化 string-value prediction errors 的实际贡献。如果 relaxed matching 显著提升 CWM 准确率，部分"formulation 缺陷"可能是 evaluation metric 的 artifact。

### Minor
- [AGREE] R1-M1 至 R1-M4 全部同意。
- R1-M1（"below chance 50%"）是我 Round 1 未捕捉的好观察——repo-level majority baseline 73%，"50% chance level"不准确。
- R1-M4（unparseable 处理策略未明确）影响 58.04% 这个数字的可解读性。

### Questions
- [AGREE] R1-Q1 至 R1-Q6 全部合理。Q1（CWM 提高 max_seq_length）和 Q3（更大 LoRA rank）尤为关键。

### Missing References
- [AGREE] Andrews et al. (2005) 和 Just et al. (2014) 是显著遗漏。
- 补充我的发现：LEVER (Ni et al., ICML 2023) 也应被引用。

---

### Excitement 分歧：我维持 2/5（vs R1 的 3/5）

核心论点：
1. 定性方向从第一性原理可预测——"generation 在复杂输出上更难"不需要实验即可推断。
2. Ye et al. 和 CodeMind 已识别关键 failure modes，CLS 是 obvious next step。
3. 最有潜力的贡献（per-test → re-repair）无实验验证。
4. ARR Excitement 3 = "might mention or attend"——对"CLS > CWM on complex output"这一 expected 发现不成立。
5. Controlled comparison methodology 的价值属于 soundness 维度，不应与 idea novelty 混淆。

论文的价值在于工程严谨性和实用警示，而非概念突破。2/5 更准确。

### 最终评分（更新后）
Overall: 2.5/5（维持不变）
Excitement: 2/5（维持不变）
与 R1 在 Overall 上一致（2.5），在 Excitement 上分歧（R1: 3, R2: 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 110 · 2026-05-15T11:45:57.468507+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 111 · 2026-05-15T11:46:00.013514+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

**核心结论**：与 R1 在 25 项具体评审点上全部达成 [AGREE]，无反驳项。两位 Reviewer 在 Overall 评分上一致（均 2.5/5），唯一分歧在 Excitement（R1: 3/5, R2: 2/5）。我维持 2/5，核心论点是该 reformulation 的定性方向从第一性原理可预期，先验工作已识别关键 failure modes，CLS 是 obvious next step 而非概念突破。

R1 提出的 N3（LoRA rank 对 generation 的不对称惩罚）和 W4（未尝试 relaxed matching）是我 Round 1 遗漏的两个重要问题，已在交叉回应中明确认同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 112 · 2026-05-15T11:46:09.378047+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 8

## Round 8

6 recorded events


### User

_source line 113 · 2026-05-15T11:46:43.538029+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 意见的逐条评价

---

## 对 R2 Strengths 的回应

**[AGREE] R2-S1 至 R2-S5**：R2 识别的五项优势与我的评估一致。控制严格的实验设计（S1）、统计方法扎实（S2）、CWM 失败模式的定量刻画（S3）、oracle framework（S4）、诚实的局限性披露（S5）——这些确实是论文的主要亮点。无补充。

---

## 对 R2 Weaknesses 的回应

### Must-Fix

**[REBUT] R2-W1: "核心贡献新颖性不足以支撑 EMNLP main"**

R2 的论点有三层：(a) generation→classification 是 NLP 成熟路线；(b) complexity-dependent advantage 可预期；(c) 贡献是量化已知趋势而非发现新现象。我逐层回应：

(a) **Reformulation 本身不是 novelty claim——应用层面的实证发现才是。** T5/BART/SQuAD 确实展示了 task framing 对 NLP 性能的影响，但这些工作的领域是自然语言理解/生成，而非 code execution simulation。论文的 novelty 不在于"把 generation 改成 classification"这一通用思路，而在于将其应用于 execution simulation 并揭示了 **特定于代码领域的失败模式**。Format compliance collapse（53-67% unparseable outputs，Section 4.6 Table 4）是一个此前未被文献记录的具体现象——Ye et al. (2025) 识别的是 trace prediction 中的推理错误类型，CodeMind (2024) 评估的是代码推理能力维度，二者均未报告 repo-level 结构化输出的全面崩溃。

(b) **"Generation 在复杂输出上退化是已知局限"这一表述过于笼统。** 已知的是 generation 成本随输出长度增长、exact match 随输出复杂度下降。但本文发现的 repo-level 现象在性质上不同于已知趋势的量化延伸：parseable CWM outputs 的准确率低于 majority baseline（42-43% vs 72.96%，Section 4.6），即模型在**能够**产生格式正确输出的情况下仍然是 anti-informative 的。这不是"退化"，是**质变**——从 noisy-but-useful 到 worse-than-trivial。这一发现对下游系统设计有实际意义（不应在 repo-level 使用 CWM formulation）。

(c) **Oracle accuracy-utility framework（Section 3.4）是独立的分析贡献。** Block-correlation model（Eq. 1-2）将 per-test 粒度的价值条件化为 F2P test count 和 ICC，得出的 concentration result（Table 3：69% 的实例无额外价值，31% 贡献几乎全部优势）提供了可操作的部署决策框架。这不是"量化已知趋势"，因为此前没有工作分析过 per-test vs trajectory-level verification 的 accuracy-utility tradeoff。

**我的立场**：我维持 Excitement 3/5。论文的 novelty 确实主要是实证性的而非算法性的，这限制了其 Main conference 的竞争力。但 R2 将其评为 ~2/5 并认为是"量化已知趋势"低估了以下发现的价值：(1) format compliance collapse 的定量刻画；(2) parseable outputs 的 anti-informativeness；(3) oracle framework。**综合来看，我认为论文的 novelty 处于 Findings 级别——不够 Main，但超过 R2 的 "weak reject" 判断。** 如果补充了 N1-N3 中的 Must-Fix 实验（CWM 8B repo-level、LoRA rank 消融、多 seed），empirical contribution 的扎实度将足以支撑 Findings acceptance。

---

**[AGREE] R2-W2: "仓库级核心结论基于单 seed，checkpoint selection variance 极大"**

完全同意，此问题与我的 N1 一致。补充一点：R2 正确指出标题和 abstract 仍以 25.59pp 作为核心宣传数字。即使作者在 Section 4.6 Limitations 中披露了 seed 123 的 75.33% 结果，**这种信息的不对称分布（abstract 用最好数字，limitations 放最差数字）构成了 framing bias**。建议作者在 abstract 中使用区间表述（如 "16–26pp depending on seed"）而非单点最优值。

---

**[AGREE] R2-W3: "CWM baseline 是 4B LoRA，结论推广到 generation formulation 整体，存在 overclaim"**

完全同意，此问题与我的 N3 一致。R2 引用的具体语句——Introduction para 3 "CWM failure modes are artifacts of the generation formulation, not inherent to the task"——精准地定位了 overclaim。我的补充：Section 3.3 同样声称 "format compliance collapse reflects a breakdown in the model's ability to follow the output format, not a limitation of the format itself"——这一因果推断同样超出了实验证据的支撑范围（实验仅覆盖 LoRA rank 16 的 4B/8B 模型）。

---

**[AGREE with nuance] R2-W4: "标题 'scales' 缺乏数据支撑"**

R2 的论据：function-level CLS 4B→8B 仅 +0.99pp；repo-level CLS 4B→8B 无改善（83.63→83.52, seed 42）。我同意这些数据点的解读。

但我认为 R2 可能采用了过窄的解读。标题 "Classification **Scales** Where Generation **Stalls**" 有两种可能的语义：

- **解读 A（model-size scaling）**：classification 随模型规模提升而改善。证据薄弱——function-level +0.99pp（微弱），repo-level seed 42 无改善。R2 的批评完全成立。
- **解读 B（complexity scaling）**：classification 能扩展到更高代码复杂度而 generation 不能。证据较强——CLS 从 function-level 88% 到 repo-level 84% 保持 robustness，CWM 从 87% 崩溃到 58%。

如果作者意图的是解读 B，标题有一定道理，但 "scales" 在 ML 语境中的默认含义是 model/data scaling（解读 A），读者极大概率会按解读 A 理解。**这构成了 misleading framing**：标题暗示 CLS 随规模增长而改善，但实际数据不支持。

**建议**：如果作者意图表达 complexity scaling，标题应明确化，如 "Classification Generalizes Where Generation Collapses: ..." 或 "Classification Persists Where Generation Fails: ..."。当前标题的 "scales" 过于含混。

---

### Should-Fix

**[AGREE] R2-W5: "Per-test diagnostic granularity 列为主要贡献但无下游实验验证"**

同意。论文 Introduction 第三个 contribution bullet 和 Section 4.4 都强调 per-test 信号可 "enable targeted re-repair"，但全文无任何下游 re-repair 实验。Oracle analysis（Table 3）展示了理论上限，但 oracle 假设 ground-truth test labels，实际场景中 classifier 有 ~12% 错误率，per-test 信号的实际 utility 可能远低于 oracle bound。这一 contribution 在当前形态下更像是 "future work suggestion" 而非已验证的 contribution。建议降级为 "potential application" 或补充哪怕是初步的 re-repair pilot 实验。

---

**[AGREE with qualification] R2-W6: "遗漏重要相关工作 LEVER (Ni et al., ICML 2023) 和 CodeT (Chen et al., ICLR 2023)"**

同意这两篇应被引用，但我对 "重要" 的程度有不同评估：

- **LEVER (Ni et al., 2023)** 训练 learned verifier 对 code generation 输出进行 classification-based reranking，与 CLS 的思路有概念相似性（都是用 classifier 判断代码正确性）。**应在 Related Work "LLM-based Verification for Code" 段落中讨论。** 但 LEVER 的验证目标是 code generation（not repair），且没有 per-test granularity 的设计——差异足够大，不构成 novelty 威胁，但需要 positioning。

- **CodeT (Chen et al., 2023)** 使用 dual execution（generated code + generated tests）进行一致性检验。这与本文的 execution-free setting 有本质区别（CodeT 依赖真实执行）。相关性较弱，可在 Related Work 中简短提及但不需要深入讨论。

- **R2 建议增加 "Learned Code Verifiers" 讨论段**：这个建议有价值。当前 Related Work 的 "LLM-based Verification for Code Repair" 段落以 SWE-RM 和 Patch Reasoner 为代表，但缺少更广泛的 learned verification 文献（LEVER、CodeT、以及 AlphaCode 的 filtering mechanism 等）。增加一个 paragraph 将强化 positioning。

---

**[AGREE] R2-W7: "TOST ±2pp margin 无正当性论证"**

与我的 W1 完全一致。无补充。

---

**[AGREE conditionally] R2-W8: "多条引用 first author 与 arXiv/OpenAlex 记录不一致"**

我在初审中未逐条核查引用（标注了 M2 关于 Qwen3 vs Qwen2.5 的引用问题）。如果 R2 有具体的不一致条目，应列出以便作者修正。仅笼统说 "多条不一致" 不足以让作者 actionable。建议 R2 提供具体列表。

---

**[AGREE] R2-W9: "数据集为合成 mutant，未讨论 synthetic-to-real gap"**

与我的 W5 一致。我在 Missing References 中建议了 Andrews et al. (2005) 和 Just et al. (2014) 两篇 mutation testing 经典文献——这两篇专门讨论人工突变与真实 fault 的关系，作者应引用并讨论。

---

### Minor

**[REBUT] R2-M1: "Abstract 信息密度过高"**

不同意。Abstract 确实包含大量数字（1.24pp, 2.43pp, 25.59pp, 53.7-67.2%, 42-43%, 90.63% 等），但这些数字直接对应论文的核心 claims，且每个数字都附有必要的实验条件说明（model size, seed count, p-value）。对于一篇以 controlled empirical comparison 为核心的论文，abstract 中包含具体数字比模糊描述更有信息量。ARR reviewer guidelines 并未对 abstract 信息密度设限。如果需要精简，建议删除 oracle ensemble (90.63%) 这一相对次要的数字，但其余数字都是核心 claim 的直接证据，应保留。

---

**[AGREE] R2-M2: "D088 protocol 未定义"**

同意。Section 4.1 提到 "D088 protocol" 但未解释含义。如果这是一个内部编号或特定的 checkpoint selection 流程，应展开定义或用描述性语言替代。

---

**[AGREE partially] R2-M3: "关键数字四次重复"**

部分同意。25.59pp 和 53.7-67.2% 确实在 abstract、introduction、experiments、conclusion 中各出现一次。一定程度的重复有助于独立阅读各 section 的读者（reviewer 经常只读 abstract+intro 或跳到 experiments），但四次完整重复确实偏多。建议 conclusion 中改为引用 Section/Table 编号而非重复完整数字。

---

**[REBUT] R2-M4: "\\cite vs \\citep 不一致"**

查看论文源码（main.tex, introduction.tex, method.tex, experiments.tex, related_work.tex），论文使用 ACL style (`\usepackage[review]{acl}`)，全文统一使用 `\cite` 和 `\citep`。ACL style 下 `\cite` 产生 "Author (Year)" 而 `\citep` 产生 "(Author, Year)"。粗看论文的引用使用中，叙述性引用（如 "Code World Models~\cite{meta2025cwm}"）和括号引用在上下文中的使用基本合理。如果 R2 有具体不一致的实例，应标出行号。仅笼统指出 "不一致" 难以判断严重程度。

---

**[REBUT] R2-M5: "26 条引用偏少"**

不同意。引用数量应由 related work 的覆盖充分性决定，而非绝对数量。论文的 Related Work（Section 5）覆盖了四个相关方向（execution simulation, LLM verification, automated repair, classification vs generation in NLP），每个方向引用了代表性工作。**引用数量不足的问题应通过指出具体遗漏来论证**（如 R2-W6 中的 LEVER/CodeT），而非设定数量下限。如果补充 LEVER、CodeT、Andrews et al.、Just et al. 等遗漏引用，总数将达到 ~30，对于一篇聚焦方法对比的 8 页论文属于正常范围。

---

## 对 R2 Questions 的回应

**[AGREE] R2-Q1: "32B CWM 仓库级是否仍有 format compliance collapse？"**

关键问题，与 N3/W3 直接相关。如果 32B CWM 在 repo-level 的 unparseable rate 显著低于 53-67%，论文的 "formulation-level limitation" claim 将被严重削弱。作者应讨论这一可能性，即使无法直接实验（32B mid-training 成本高昂）。

---

**[AGREE] R2-Q2: "CLS 4B seed 42 vs 123 差 8.3pp 的根源？"**

同意这是必须回答的问题。我在 N1 中也要求作者分析：是 mutation type distribution shift 的系统性效应还是 checkpoint selection 的随机噪声？补充：作者可以报告两个 seed 选中的 checkpoint step、val accuracy、以及 per-mutation-type test accuracy，以诊断差异来源。

---

**[AGREE] R2-Q3: "TOST ±2pp 依据？±1pp 时结论是否改变？"**

与我的 W1 一致。建议作者报告 ±1pp, ±2pp, ±3pp 的 TOST 结果。

---

**[AGREE] R2-Q4: "CWM 低方差被解释为 bottleneck，也可能是更稳定特征？"**

这是一个有价值的 alternative interpretation，我在初审中未充分考虑。论文 Section 4.8(c) 将 CWM 的 5-seed std 0.37pp（vs CLS 0.78pp）解释为 bottleneck 证据——"如果性能被输出格式约束 cap 住，seed 方差自然被压缩"。但 R2 指出的替代解释同样合理：CWM 的 generation objective 可能学到了更稳定的 representation（因为必须预测完整输出，强制模型对输入建立更鲁棒的理解）。**论文无法区分这两种解释**，因此 variance compression 不应作为 bottleneck 的证据，而应作为需要进一步研究的观察。

---

**[AGREE] R2-Q5: "匹配上下文消融仅有 CLS 8B 单 seed，能否补充 4B？"**

合理请求。我在 Q1 中进一步问了：CWM 的 eval 时 max_seq_length 能否提高到 8192？如果 CWM 在更大 input context 下 unparseable rate 下降，这将提供关于 input truncation vs formulation bottleneck 的额外信号。

---

**[AGREE] R2-Q6: "Per-test granularity 'enables re-repair' 有初步实验支持吗？"**

与 W5 一致。无补充。

---

## 对 R2 Missing References 的回应

**[AGREE]** LEVER (Ni et al., ICML 2023) 应引用（见 W6 讨论）。
**[AGREE with qualification]** CodeT (Chen et al., ICLR 2023) 相关性较弱（依赖真实执行），但值得简短提及。
**[AGREE]** 增加 "Learned Code Verifiers" 讨论段是好建议。

---

## 对 R2 Overall Assessment 的回应

**R2 评分**：Borderline (leaning weak reject), 核心障碍：新颖性不足 + 仓库级单 seed + LoRA overclaim。

**我的评估**：我同意 R2 识别的三个核心障碍中的两个（仓库级单 seed、LoRA overclaim），但在新颖性判断上与 R2 有分歧。

**分歧焦点：novelty 是否足够。**

R2 认为论文是 "quantifying a known trend"（量化已知趋势）。我的立场是：

1. Format compliance collapse 的具体现象（53-67% unparseable + parseable outputs anti-informative at 42-43%）此前未被记录。这不是"generation 在复杂输出上退化"的简单延伸——它是一个 **qualitative failure mode**，parseable outputs 低于 majority baseline 的事实意味着即使解决了 parsing 问题，CWM 在 repo-level 仍然无用。这对实践者有直接影响。

2. Oracle accuracy-utility framework 是一个新的分析工具，将 per-test 粒度的价值条件化为 F2P test count 和 within-problem correlation，得出了 actionable 的部署建议（69% 实例无需 per-test，31% 集中受益）。

3. 然而，**我同意论文的 novelty 主要是 empirical，缺少 algorithmic innovation**。没有提出新模型、新训练方法或新推理策略——只是改变了 output format 并做了 controlled comparison。这限制了 excitement。

**综合判断**：我维持 Overall 2.5/5。论文在当前状态下不够 Main conference（与 R2 一致），但如果补充了 Must-Fix 实验并校准了 claim 强度，其 empirical contribution 足以支撑 Findings（比 R2 的 "leaning weak reject" 更积极）。**我们的实质分歧约 0.5 分**，集中在 novelty 是否达到 Findings 门槛——我认为达到了（给定实验补充），R2 认为不确定。

---

## 总结：R1 与 R2 的一致和分歧

| 议题 | R1 | R2 | 一致性 |
|------|----|----|--------|
| 单 seed repo-level | Must-Fix (N1) | Must-Fix (W2) | **完全一致** |
| LoRA overclaim | Must-Fix (N3) | Must-Fix (W3) | **完全一致** |
| CWM 8B 缺失 | Must-Fix (N2) | 未单独列出 | R1 额外识别 |
| Novelty 不足 | 未列为 Must-Fix | Must-Fix (W1) | **分歧**：R1 认为 Findings 级够，R2 认为不够 Main |
| 标题 "scales" | 未识别 | Must-Fix (W4) | R2 新识别，R1 同意有问题但认为 Should-Fix 而非 Must-Fix |
| TOST margin | Should-Fix (W1) | Should-Fix (W7) | **完全一致** |
| No re-repair exp | 评论中提及 | Should-Fix (W5) | **一致** |
| Missing LEVER/CodeT | 未识别 | Should-Fix (W6) | R2 新识别，R1 同意 |
| Synthetic-to-real gap | Should-Fix (W5) | Should-Fix (W9) | **完全一致** |
| Abstract 信息密度 | 无意见 | Minor (M1) | **分歧**：R1 认为可接受 |
| 引用数量 | 无意见 | Minor (M5) | **分歧**：R1 认为应按遗漏而非数量评判 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-15T11:48:11.477477+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "issues:\n- id: \"R1-N1\"\n  summary: \"Repo-level 核心 claim (25.59pp) 基于单 seed，seed 方差极大 (8.3pp)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2 完全一致。CLS 4B s42=83.63% vs s123=75.33%，abstract/intro 用单点最优值 25.59pp 构成 framing bias。建议报告区间 16-26pp。\"\n  action_items:\n    - round: 1\n      action: \"补充 CLS 4B seed 123 vs CWM 4B seed 123 same-size 对比；abstract/intro 改为区间表述\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失，formulation bottleneck claim 在最关键条件下无法验证\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-N2，R2 在 W3 中附议。论文 conclusion 承认 awaits CWM 8B results 但 abstract/intro 以肯定语气阐述。\"\n  action_items:\n    - round: 1\n      action: \"完成 CWM 8B repo-level 训练或在 abstract/intro 显著弱化 formulation bottleneck 叙述\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力，无法区分 formulation vs capacity limitation\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2-W3。LoRA 低秩约束对 generation 惩罚可能大于 classification。Introduction 'artifacts of the generation formulation' 超出证据支撑。R2 交叉回应中明确认同此为 R1 独有的重要观察。\"\n  action_items:\n    - round: 1\n      action: \"增加 LoRA rank 消融 (rank 32/64/128)；限定 claim 范围为 LoRA fine-tuned small models\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"核心贡献新颖性不足以支撑 EMNLP main conference\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2-W1 Must-Fix。R1 交叉回应 [REBUT]：认为 format compliance collapse 是未被记录的新现象，oracle framework 是独立贡献，novelty 达 Findings 级。R2 维持 2/5。分歧点：R1 Excitement 3/5 vs R2 2/5，约 0.5 分差距。\"\n  action_items:\n    - round: 1\n      action: \"考虑投 Findings track；或补充实验强化 empirical contribution\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑，CLS 4B→8B repo-level 无改善\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2-W4 Must-Fix。R1 交叉回应 [AGREE with nuance]：同意 model-size scaling 解读不成立，但 complexity scaling 解读有一定道理。建议改为 'Generalizes' 或 'Persists'。\"\n  action_items:\n    - round: 1\n      action: \"修改标题，避免 'scales' 一词引起 model-size scaling 的误解\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正当性论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W7 完全一致。未解释为何选 ±2pp，未报告不同 margin 下的结果。\"\n  action_items:\n    - round: 1\n      action: \"解释 ±2pp 选择依据，报告 ±1pp/±2pp/±3pp 的 TOST 结果\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Scaling argument (CWM -0.27pp) 被未调优 hyperparameter 混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-W2。CWM -0.27pp 在 seed noise 内，LoRA rank/lr 未为 8B 重调。R2 交叉回应同意。\"\n  action_items:\n    - round: 1\n      action: \"弱化 scaling argument 表述或针对 8B 重新搜索 hyperparameter\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Val-test mutation type distribution shift 对 checkpoint selection 影响未充分分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-W3。operator_swap val 19.1% → test 34.3%。CLS 4B seed 123 选中 early checkpoint 放大了 shift。\"\n  action_items:\n    - round: 1\n      action: \"报告 val/test mutation type 分布和 per-type 准确率\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching，系统性低估 generation 准确率\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-W4。R2 交叉回应认同为自己 Round 1 遗漏的重要问题。\"\n  action_items:\n    - round: 1\n      action: \"至少在 function-level 报告一种 relaxed matching variant 的 CWM 准确率\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"人工突变 vs 真实 bug 的 ecological validity 未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W9 一致。缺少 Andrews et al. (2005) 和 Just et al. (2014) 引用。\"\n  action_items:\n    - round: 1\n      action: \"在 Limitations 讨论 synthetic-to-real gap，引用 mutation testing 经典文献\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"Per-test diagnostic granularity 列为主要贡献但无下游 re-repair 实验验证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2-W5，R1 交叉回应完全同意。Oracle 假设 ground-truth labels，实际 ~12% 错误率下 utility 未知。\"\n  action_items:\n    - round: 1\n      action: \"降级为 potential application 或补充初步 re-repair pilot 实验\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"遗漏重要相关工作 LEVER (Ni et al., ICML 2023) 和 CodeT (Chen et al., ICLR 2023)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2-W6。R1 交叉回应同意 LEVER 应在 Related Work 讨论，CodeT 相关性较弱可简短提及。建议增加 Learned Code Verifiers 段。\"\n  action_items:\n    - round: 1\n      action: \"引用 LEVER/CodeT，增加 Learned Code Verifiers 讨论段\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"多条引用 first author 与 arXiv/OpenAlex 记录不一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2-W8。R1 条件同意但要求提供具体不一致列表。wu2025patchreasoner 和 ding2025selfexecution 被具体指出。\"\n  action_items:\n    - round: 1\n      action: \"逐条核查 bib 条目 first author 与 arXiv 记录是否一致\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M1\"\n  summary: \"'Below chance level (50%)' 在类别不平衡场景下易引起误解\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-M1。majority baseline 73%，应同时报告相对于 majority baseline 的差距。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M2\"\n  summary: \"Qwen3 模型引用了 Qwen2.5 技术报告 (yang2024qwen25)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-M2。应核实 Qwen3 是否有独立技术报告。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M3\"\n  summary: \"5-seed 统计混合了 bfloat16 和 NF4 量化精度\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-M3。Table 1 应标注哪些 seed 使用 NF4。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M4\"\n  summary: \"Unparseable CWM outputs 的 verdict assignment 策略未明确说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-M4。影响 58.04% 数字的可解读性。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M2\"\n  summary: \"'D088 protocol' 未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2-M2。R1 交叉回应同意。应展开定义或用描述性语言替代。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "issues:\n- id: \"R1-N1\"\n  summary: \"Repo-level 核心 claim (25.59pp) 基于单 seed，seed 方差极大 (8.3pp)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2 完全一致。CLS 4B s42=83.63% vs s123=75.33%，abstract/intro 用单点最优值 25.59pp 构成 framing bias。建议报告区间 16-26pp。\"\n  action_items:\n    - round: 1\n      action: \"补充 CLS 4B seed 123 vs CWM 4B seed 123 same-size 对比；abstract/intro 改为区间表述\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失，formulation bottleneck claim 在最关键条件下无法验证\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-N2，R2 在 W3 中附议。论文 conclusion 承认 awaits CWM 8B results 但 abstract/intro 以肯定语气阐述。\"\n  action_items:\n    - round: 1\n      action: \"完成 CWM 8B repo-level 训练或在 abstract/intro 显著弱化 formulation bottleneck 叙述\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力，无法区分 formulation vs capacity limitation\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2-W3。LoRA 低秩约束对 generation 惩罚可能大于 classification。Introduction 'artifacts of the generation formulation' 超出证据支撑。R2 交叉回应中明确认同此为 R1 独有的重要观察。\"\n  action_items:\n    - round: 1\n      action: \"增加 LoRA rank 消融 (rank 32/64/128)；限定 claim 范围为 LoRA fine-tuned small models\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"核心贡献新颖性不足以支撑 EMNLP main conference\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2-W1 Must-Fix。R1 交叉回应 [REBUT]：认为 format compliance collapse 是未被记录的新现象，oracle framework 是独立贡献，novelty 达 Findings 级。R2 维持 2/5。分歧点：R1 Excitement 3/5 vs R2 2/5，约 0.5 分差距。\"\n  action_items:\n    - round: 1\n      action: \"考虑投 Findings track；或补充实验强化 empirical contribution\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑，CLS 4B→8B repo-level 无改善\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2-W4 Must-Fix。R1 交叉回应 [AGREE with nuance]：同意 model-size scaling 解读不成立，但 complexity scaling 解读有一定道理。建议改为 'Generalizes' 或 'Persists'。\"\n  action_items:\n    - round: 1\n      action: \"修改标题，避免 'scales' 一词引起 model-size scaling 的误解\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正当性论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W7 完全一致。未解释为何选 ±2pp，未报告不同 margin 下的结果。\"\n  action_items:\n    - round: 1\n      action: \"解释 ±2pp 选择依据，报告 ±1pp/±2pp/±3pp 的 TOST 结果\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Scaling argument (CWM -0.27pp) 被未调优 hyperparameter 混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-W2。CWM -0.27pp 在 seed noise 内，LoRA rank/lr 未为 8B 重调。R2 交叉回应同意。\"\n  action_items:\n    - round: 1\n      action: \"弱化 scaling argument 表述或针对 8B 重新搜索 hyperparameter\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Val-test mutation type distribution shift 对 checkpoint selection 影响未充分分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-W3。operator_swap val 19.1% → test 34.3%。CLS 4B seed 123 选中 early checkpoint 放大了 shift。\"\n  action_items:\n    - round: 1\n      action: \"报告 val/test mutation type 分布和 per-type 准确率\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching，系统性低估 generation 准确率\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-W4。R2 交叉回应认同为自己 Round 1 遗漏的重要问题。\"\n  action_items:\n    - round: 1\n      action: \"至少在 function-level 报告一种 relaxed matching variant 的 CWM 准确率\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"人工突变 vs 真实 bug 的 ecological validity 未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W9 一致。缺少 Andrews et al. (2005) 和 Just et al. (2014) 引用。\"\n  action_items:\n    - round: 1\n      action: \"在 Limitations 讨论 synthetic-to-real gap，引用 mutation testing 经典文献\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"Per-test diagnostic granularity 列为主要贡献但无下游 re-repair 实验验证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2-W5，R1 交叉回应完全同意。Oracle 假设 ground-truth labels，实际 ~12% 错误率下 utility 未知。\"\n  action_items:\n    - round: 1\n      action: \"降级为 potential application 或补充初步 re-repair pilot 实验\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"遗漏重要相关工作 LEVER (Ni et al., ICML 2023) 和 CodeT (Chen et al., ICLR 2023)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2-W6。R1 交叉回应同意 LEVER 应在 Related Work 讨论，CodeT 相关性较弱可简短提及。建议增加 Learned Code Verifiers 段。\"\n  action_items:\n    - round: 1\n      action: \"引用 LEVER/CodeT，增加 Learned Code Verifiers 讨论段\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"多条引用 first author 与 arXiv/OpenAlex 记录不一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2-W8。R1 条件同意但要求提供具体不一致列表。wu2025patchreasoner 和 ding2025selfexecution 被具体指出。\"\n  action_items:\n    - round: 1\n      action: \"逐条核查 bib 条目 first author 与 arXiv 记录是否一致\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M1\"\n  summary: \"'Below chance level (50%)' 在类别不平衡场景下易引起误解\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-M1。majority baseline 73%，应同时报告相对于 majority baseline 的差距。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M2\"\n  summary: \"Qwen3 模型引用了 Qwen2.5 技术报告 (yang2024qwen25)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-M2。应核实 Qwen3 是否有独立技术报告。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M3\"\n  summary: \"5-seed 统计混合了 bfloat16 和 NF4 量化精度\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-M3。Table 1 应标注哪些 seed 使用 NF4。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M4\"\n  summary: \"Unparseable CWM outputs 的 verdict assignment 策略未明确说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1-M4。影响 58.04% 数字的可解读性。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M2\"\n  summary: \"'D088 protocol' 未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2-M2。R1 交叉回应同意。应展开定义或用描述性语言替代。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-15T11:48:11.580619+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 8547}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-15T11:50:58.810414+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "report": "# 审稿报告 — Round 1\n\n**论文**: Classification Scales Where Generation Stalls: Reformulating Execution Simulation for Code Repair Verification\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**截止日期**: 2026-05-25\n**Reviewer**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作）\n**圆桌模式**: Round 1 独立审稿 → Step 2 交叉分享 → Step 3 收敛判定（1 轮收敛）\n\n---\n\n## Summary\n\n本文提出将代码修复验证中的执行模拟从开放式输出生成（CWM）重新表述为逐测试二分类（CLS），在函数级和仓库级两个复杂度层级与 CWM 及 trajectory-level 评分进行受控对比。核心发现：CLS 优势随代码复杂度增长——函数级差距 1.24pp（5 seeds），仓库级差距扩大到 25.59pp（单 seed），主要由 CWM 输出格式合规崩溃驱动（53-67% unparseable，parseable 部分 42-43% 准确率低于 majority baseline）。论文同时展示 per-test 分类与 trajectory-level 评分在 variant 级准确率上统计等价（TOST p=0.007），并提出 block-correlation oracle framework 刻画 per-test 粒度的价值边界。\n\n---\n\n## Strengths\n\n**S1. 干净的受控实验设计（R1-S1, R2-S1, 共识）。** 三种 formulation（CLS/CWM/TRAJ）共享相同基座模型（Qwen3-4B/8B）、LoRA 配置、训练数据和 seed，使 formulation 差异的归因比较干净。这是该领域少见的 apples-to-apples 对比。\n\n**S2. 严谨的统计方法论（R1-S2, R2-S2, 共识）。** Clustered bootstrap（114 problem clusters, 10K resamples）处理 within-problem 相关性，TOST 等价检验，ICC 和 design effect 报告。论文明确指出 naive i.i.d. CI 窄约 2×，并在所有检验中修正。统计素养高于该领域平均水平。\n\n**S3. Oracle accuracy-utility framework 优雅实用（R1-S3, R2-S4, 共识）。** Section 3.4 的 block-correlation model 将 per-test 粒度的价值条件化为 F2P test count 和 ICC，得出可操作的部署决策框架：69% 的 SWE-bench 实例（T=1）无额外价值，优势集中在 T≥2 的 31% 实例。\n\n**S4. CWM 仓库级失败模式的定量刻画（R2-S3）。** Format compliance collapse 的量化（53.7-67.2% unparseable + parseable 部分 anti-informative at 42-43%）对实践者有直接警示价值。\n\n**S5. Error complementarity 分析（R1-S5）。** CLS 偏假阴性（75.5%），CWM 偏假阳性（83.1%），oracle 组合达 90.63%。自然指向 ensemble 方向，对下游系统设计有指导意义。\n\n**S6. 诚实的局限性披露（R1-S4, R2-S5, 共识）。** 主动标注单 seed、CWM 8B 缺失、hyperparameter 未重新调优、checkpoint selection variance 等限制。\n\n---\n\n## Weaknesses\n\n### Critical（两位 Reviewer 共识的核心问题）\n\n**[C1] Repo-level 核心 claim (25.59pp) 基于单 seed，seed 方差极大。（R1-N1 + R2-W2, 完全一致）**\nCLS 4B s42=83.63% vs s123=75.33%，seed 间差异 8.3pp。论文在 abstract、introduction、conclusion 中反复使用 25.59pp 作为 headline result，但仅在 Section 4.6 Limitations 中披露 seed 123 的 75.33%——信息不对称分布构成 framing bias。如取两 seed 均值（~79.5%），gap 缩小至约 20pp（vs CWM 均值 ~58.6%），仍然显著但与 25.59pp 有实质差距。\n- **要求**：(1) 报告多 seed 范围（如 16-26pp）而非单点最优值；(2) 分析 seed 42 vs 123 差异的根因（checkpoint stage、mutation type distribution shift、或随机噪声）。\n\n**[C2] CWM 8B repo-level 结果缺失，\"formulation bottleneck\" claim 在最关键条件下未验证。（R1-N2, R2 附议）**\n论文核心叙事是 CWM 失败为 formulation-level bottleneck。此论断在函数级有间接支持（CWM 4B→8B 无改善），但在 repo-level 完全缺乏验证。若 CWM 8B repo-level 显著优于 CWM 4B，\"formulation bottleneck\" 叙事将被削弱。论文 conclusion 承认 \"awaits CWM 8B results\" 但 abstract/introduction 以肯定语气阐述。\n- **要求**：(1) 完成 CWM 8B repo-level 训练（deadline 前应可完成）；(2) 若无法完成，需在 abstract/introduction 中显著弱化为条件性表述。\n\n**[C3] CWM baseline 的 LoRA fine-tuning (rank 16) 可能系统性低估 generation formulation 能力。（R1-N3 + R2-W3, 完全一致）**\n原始 CWM 是 32B mid-trained 模型，本文 CWM 是 4B/8B LoRA（rank 16, ~0.1% trainable params）。LoRA 低秩约束对 generation（需学习精确 token 序列映射）的惩罚可能大于 classification（仅二值决策边界）——这是 R1 独到的观察，R2 交叉回应明确认同。论文无法区分 \"generation formulation inherently struggles\" 和 \"small LoRA-finetuned models struggle to generate complex outputs\"。Introduction \"CWM failure modes are artifacts of the generation formulation\" 超出证据支撑。\n- **要求**：(1) 增加 LoRA rank 消融（32/64/128），观察 unparseable rate 和准确率变化；(2) 限定 claim 范围为 \"LoRA fine-tuned small models\"。\n\n**[C4] 核心贡献新颖性争议。（R2-W1, R1 部分反驳——唯一分歧点）**\n- **R2 立场（Excitement 2/5）**：generation→classification 是 NLP 成熟路线（T5/BART/SQuAD）；complexity-dependent advantage 可从第一性原理预期；Ye et al. 和 CodeMind 已识别关键 failure modes，CLS 是 obvious next step。贡献是量化已知趋势而非发现新现象。当前状态更适合 Findings。\n- **R1 立场（Excitement 3/5）**：Format compliance collapse 的具体现象（parseable outputs anti-informative at 42-43%）此前未被记录，这是质变而非量变；oracle framework 是独立分析贡献。Novelty 达 Findings 级别。\n- **Director 判断**：两位 Reviewer 在 Overall 评分上一致（均 2.5/5），分歧仅在 Excitement（0.5 分差距）。novelty 确实主要是实证性的，缺少 algorithmic innovation。建议投 Findings track 或通过补充实验（CWM 8B、LoRA rank 消融、re-repair pilot）显著强化 empirical contribution。\n\n### Warning（Should-Fix 问题）\n\n**[W1] 标题 \"scales\" 缺乏数据支撑。（R2-W4, R1 同意有问题）**\n函数级 CLS 4B→8B: +0.99pp（微弱）。仓库级 CLS 4B→8B: 83.63→83.52（seed 42, 无改善）。\"Scales\" 在 ML 语境中默认含义为 model/data scaling，但数据不支持。如意图表达 complexity scaling，应明确化（如 \"Generalizes\" 或 \"Persists\"）。R1 提供了有价值的双重语义分析。\n\n**[W2] TOST ±2pp equivalence margin 缺乏正当性论证。（R1-W1 + R2-W7, 完全一致）**\nMargin 选择决定 \"equivalence\" 含义。未解释 ±2pp 依据，未报告不同 margin 下结果。建议报告 ±1pp/±2pp/±3pp 的 TOST 结果。\n\n**[W3] Scaling argument (CWM -0.27pp) 被未调优 hyperparameter 混淆。（R1-W2）**\nCWM -0.27pp 在 3-seed std ~0.5pp 内，统计上不显著。LoRA rank/lr 未为 8B 重新调优。\"CWM does not benefit from scaling\" 的 claim 过强。\n\n**[W4] CWM exact string matching 未尝试 relaxed matching。（R1-W4, R2 交叉回应认同遗漏）**\nFootnote 1 称 exact match 是 \"conservative lower bound\"，但未提供 relaxed matching 数据点。若 relaxed matching 显著提升 CWM 准确率，部分 \"formulation 缺陷\" 可能是 evaluation metric artifact。至少在函数级报告一种 relaxed matching variant。\n\n**[W5] Per-test diagnostic granularity 列为主要贡献但无下游 re-repair 实验验证。（R2-W5, R1 同意）**\nContribution 2 声称 \"enables targeted re-repair\" 但全文无任何下游实验。Oracle analysis 假设 ground-truth labels，实际 ~12% 错误率下 utility 未知。建议降级为 \"potential application\" 或补充 pilot 实验。\n\n**[W6] 遗漏重要相关工作。（R2-W6, R1 同意）**\n- LEVER (Ni et al., ICML 2023)：训练 learned verifier 做 classification-based reranking，概念上高度相似。应在 Related Work 讨论。\n- CodeT (Chen et al., ICLR 2023)：dual execution agreement。相关性较弱但值得提及。\n- 建议增加 \"Learned Code Verifiers\" 讨论段。\n\n**[W7] 人工突变 vs 真实 bug 的 ecological validity 未讨论。（R1-W5 + R2-W9, 完全一致）**\n5 种 mutation type 覆盖充分性、synthetic-to-real gap 均未讨论。缺少 Andrews et al. (2005, ICSE) 和 Just et al. (2014, FSE) 引用。\n\n**[W8] Val-test mutation type distribution shift 对 checkpoint selection 影响未充分分析。（R1-W3）**\noperator_swap val 19.1% → test 34.3%。未报告 per-type 准确率或 val/test 分布。\n\n**[W9] 多条引用 first author 与 arXiv 记录不一致。（R2-W8）**\nwu2025patchreasoner（bib: Wu Zuxin, arXiv: Xu Junjielong）、ding2025selfexecution（bib: Ding, API: Maimon）等。需逐条核查。\n\n### Info（Minor 问题）\n\n- [I1] \"Below chance level (50%)\" 在类别不平衡场景下易误解（majority baseline 73%）（R1-M1）\n- [I2] Qwen3 模型引用了 Qwen2.5 技术报告（R1-M2）\n- [I3] 5-seed 统计混合 bfloat16 和 NF4 量化精度（R1-M3）\n- [I4] Unparseable CWM outputs 的 verdict assignment 策略未明确（R1-M4）\n- [I5] \"D088 protocol\" 未定义（R2-M2, R1 同意）\n\n---\n\n## Reviewer Consensus（[AGREE] 项）\n\n两位 Reviewer 在以下 25 项评审点上达成完全一致（[AGREE]）：\n- **所有 Strengths**（S1-S5 + R2-S3）\n- **核心 Weaknesses**：单 seed claim (C1)、CWM 8B 缺失 (C2)、LoRA overclaim (C3)、TOST margin (W2)、synthetic-to-real gap (W7)、no re-repair experiment (W5)、LEVER/CodeT 遗漏 (W6)\n- R1 提出的 W4（relaxed matching）：R2 交叉回应中明确认同为自己遗漏的重要问题\n- R2 提出的 W4（标题 \"scales\"）：R1 同意有问题（with nuanced dual-interpretation analysis）\n\n---\n\n## Reviewer Divergence（[REBUT] 项）\n\n**唯一实质分歧：Novelty / Excitement 评分**\n| | R1 | R2 |\n|---|---|---|\n| Excitement | 3/5 | 2/5 |\n| 立场 | Format compliance collapse 是未记录的质变现象；oracle framework 是独立贡献；novelty 达 Findings 级 | 定性方向可预期；先验工作已识别 failure modes；CLS 是 obvious next step；贡献是量化已知趋势 |\n| 对论文的影响 | 补充实验后可接受为 Findings | 不确定是否达到 Findings 门槛 |\n\n**Minor 分歧**（不影响结论）：\n- Abstract 信息密度：R2 认为过高（M1），R1 反驳认为对 empirical paper 合理\n- 引用数量：R2 认为偏少（M5），R1 反驳认为应按遗漏而非数量评判\n- 标题 \"scales\" 严重性：R2 列为 Must-Fix，R1 降为 Should-Fix\n\n---\n\n## Questions（汇总，需作者回答）\n\n1. CWM eval 时提高 max_seq_length 到 8192，unparseable rate 和 accuracy 是否变化？（R1-Q1）\n2. CLS 4B seed 42 选中哪个 checkpoint step？与 seed 123 (step 800) 的 val/test accuracy 关系？（R1-Q2, R2-Q2）\n3. 是否尝试过 LoRA rank 32/64？CWM unparseable rate 是否随 rank 下降？（R1-Q3）\n4. Majority voting pairwise agreement rate 和 error overlap？（R1-Q4）\n5. Repo-level oracle ensemble (CLS+CWM) 结果？CWM anti-informative 时 ensemble 是否反而更差？（R1-Q5）\n6. 5 种 mutation type 选择依据和覆盖率分析？（R1-Q6）\n7. 32B CWM 在 repo-level 是否仍有 format compliance collapse？（R2-Q1）\n8. TOST ±1pp 时结论是否改变？（R2-Q3）\n9. CWM 低方差是 bottleneck 还是 representation stability？如何区分？（R2-Q4）\n10. Per-test granularity \"enables re-repair\" 有任何初步实验？（R2-Q6）\n\n---\n\n## Missing References\n\n1. **LEVER** (Ni et al., ICML 2023) — learned code verifier，classification-based reranking\n2. **CodeT** (Chen et al., ICLR 2023) — dual execution agreement\n3. **Andrews et al.** (2005, ICSE) — mutation vs real faults 经典讨论\n4. **Just et al.** (2014, FSE) — mutants as valid substitute for real faults\n5. **VG-Search** (Wang et al., 2025) — 应在 introduction 更早提及以建立 motivation\n6. Qwen3 独立技术报告（如存在，替换 Qwen2.5 引用）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**Overall Score: Weak Reject（建议 Resubmit 或转投 Findings）**\n\n**评分依据**：\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 2.5/5 | 2.5/5 | **2.5/5** |\n| Excitement | 3/5 | 2/5 | **2.5/5** |\n| Overall | 2.5/5 | 2.5/5 | **2.5/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**核心判断**：\n\n论文提出了一个有价值的 research question，实验设计框架（controlled formulation comparison）和统计方法论展现了专业水准。但四个核心问题共同削弱了论文的可接收性：\n\n1. **证据不足以支撑 claim 强度**：repo-level 最突出数字（25.59pp）来自单 seed 且 seed 方差极大（8.3pp）；CWM 8B repo-level 缺失使 \"formulation bottleneck\" claim 在最关键条件下无法验证。\n2. **实验设计可能系统性偏向 CLS**：LoRA rank 16 对 generation 的惩罚可能大于 classification；CWM 使用 exact string matching 而非 relaxed matching。\n3. **Claim 超出证据范围**：从 4B LoRA CWM 推广到 \"generation formulation\" 整体；标题 \"scales\" 暗示 model-size scaling 但数据不支持；per-test diagnostic granularity 作为 contribution 但无下游验证。\n4. **Novelty 争议**：贡献主要是实证性的（量化 complexity-dependent advantage），缺少 algorithmic innovation。R2 认为可预期，R1 认为 format compliance collapse 的质变特征有独立价值。\n\n**建议路径**：\n- **最优路径**：补充 CWM 8B repo-level + LoRA rank 消融 + 校准 claim 强度 → 投 Findings track\n- **快速路径**：不补实验，但大幅弱化 claim（去掉 \"formulation bottleneck\" 因果推断，改为观察性描述）+ 修改标题 + 补引用 → 投 Findings track（竞争力较弱）\n- **不建议**：当前状态直接投 Main conference\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度高但可接受（R1 立场）；15+ 数字对 empirical paper 合理\n- 25.59pp 应改为区间表述（C1）\n- \"scales\" 一词需修改（W1）\n\n### Introduction\n- 三个 contribution 的支撑程度不均：Contribution 1（complexity-dependent advantage）需多 seed 支撑；Contribution 2（diagnostic granularity at equivalent accuracy）需弱化为 potential application；Contribution 3（accuracy-utility frontier）支撑最充分\n- \"CWM failure modes are artifacts of the generation formulation\" 需限定范围（C3）\n\n### Method (Section 3)\n- Problem setup 和 formulation comparison 清晰\n- CWM failure modes 分析（Section 3.3）需添加 caveat 关于 LoRA 容量限制\n- Oracle framework（Section 3.4）是论文最强贡献之一\n\n### Experiments (Section 4)\n- Function-level (Section 4.2)：设计较好，5-seed 覆盖，但需标注 NF4 seed（I3）\n- Scaling (Section 4.3)：CWM -0.27pp 论证过强，需弱化（W3）\n- Equivalence (Section 4.4)：TOST margin 需论证（W2）\n- Oracle (Section 4.5)：分析扎实\n- Repo-level (Section 4.6)：核心问题集中地——单 seed（C1）、CWM 8B 缺失（C2）、unparseable 处理策略不明（I4）\n\n### Related Work (Section 5)\n- 缺少 LEVER/CodeT 讨论（W6）\n- 建议增加 \"Learned Code Verifiers\" 段\n- VG-Search 讨论过晚（应在 introduction 建立 motivation）\n\n### Conclusion (Section 6)\n- Limitations 段落覆盖面较广但缺少 synthetic-to-real gap 讨论（W7）\n- \"Formulation bottleneck\" 的条件性表述在 conclusion 中有但在 abstract/introduction 中缺失（C2）\n\n---\n\n## Issue Tracker 同步\n\n已更新 `projects/exec-sim-repair-verifier/artifacts/review_issues.yaml`，共 17 个 issue：\n- Critical (4): C1 单 seed, C2 CWM 8B 缺失, C3 LoRA overclaim, C4 novelty 争议\n- Warning (9): W1-W9\n- Info (5): I1-I5\n\n---\n\n*圆桌审稿 Round 1 完成。两位 Reviewer 经交叉分享后在关键问题上达成共识，唯一分歧（Excitement 3 vs 2）已如实记录。*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "report": "# 审稿报告 — Round 1\n\n**论文**: Classification Scales Where Generation Stalls: Reformulating Execution Simulation for Code Repair Verification\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**截止日期**: 2026-05-25\n**Reviewer**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作）\n**圆桌模式**: Round 1 独立审稿 → Step 2 交叉分享 → Step 3 收敛判定（1 轮收敛）\n\n---\n\n## Summary\n\n本文提出将代码修复验证中的执行模拟从开放式输出生成（CWM）重新表述为逐测试二分类（CLS），在函数级和仓库级两个复杂度层级与 CWM 及 trajectory-level 评分进行受控对比。核心发现：CLS 优势随代码复杂度增长——函数级差距 1.24pp（5 seeds），仓库级差距扩大到 25.59pp（单 seed），主要由 CWM 输出格式合规崩溃驱动（53-67% unparseable，parseable 部分 42-43% 准确率低于 majority baseline）。论文同时展示 per-test 分类与 trajectory-level 评分在 variant 级准确率上统计等价（TOST p=0.007），并提出 block-correlation oracle framework 刻画 per-test 粒度的价值边界。\n\n---\n\n## Strengths\n\n**S1. 干净的受控实验设计（R1-S1, R2-S1, 共识）。** 三种 formulation（CLS/CWM/TRAJ）共享相同基座模型（Qwen3-4B/8B）、LoRA 配置、训练数据和 seed，使 formulation 差异的归因比较干净。这是该领域少见的 apples-to-apples 对比。\n\n**S2. 严谨的统计方法论（R1-S2, R2-S2, 共识）。** Clustered bootstrap（114 problem clusters, 10K resamples）处理 within-problem 相关性，TOST 等价检验，ICC 和 design effect 报告。论文明确指出 naive i.i.d. CI 窄约 2×，并在所有检验中修正。统计素养高于该领域平均水平。\n\n**S3. Oracle accuracy-utility framework 优雅实用（R1-S3, R2-S4, 共识）。** Section 3.4 的 block-correlation model 将 per-test 粒度的价值条件化为 F2P test count 和 ICC，得出可操作的部署决策框架：69% 的 SWE-bench 实例（T=1）无额外价值，优势集中在 T≥2 的 31% 实例。\n\n**S4. CWM 仓库级失败模式的定量刻画（R2-S3）。** Format compliance collapse 的量化（53.7-67.2% unparseable + parseable 部分 anti-informative at 42-43%）对实践者有直接警示价值。\n\n**S5. Error complementarity 分析（R1-S5）。** CLS 偏假阴性（75.5%），CWM 偏假阳性（83.1%），oracle 组合达 90.63%。自然指向 ensemble 方向，对下游系统设计有指导意义。\n\n**S6. 诚实的局限性披露（R1-S4, R2-S5, 共识）。** 主动标注单 seed、CWM 8B 缺失、hyperparameter 未重新调优、checkpoint selection variance 等限制。\n\n---\n\n## Weaknesses\n\n### Critical（两位 Reviewer 共识的核心问题）\n\n**[C1] Repo-level 核心 claim (25.59pp) 基于单 seed，seed 方差极大。（R1-N1 + R2-W2, 完全一致）**\nCLS 4B s42=83.63% vs s123=75.33%，seed 间差异 8.3pp。论文在 abstract、introduction、conclusion 中反复使用 25.59pp 作为 headline result，但仅在 Section 4.6 Limitations 中披露 seed 123 的 75.33%——信息不对称分布构成 framing bias。如取两 seed 均值（~79.5%），gap 缩小至约 20pp（vs CWM 均值 ~58.6%），仍然显著但与 25.59pp 有实质差距。\n- **要求**：(1) 报告多 seed 范围（如 16-26pp）而非单点最优值；(2) 分析 seed 42 vs 123 差异的根因（checkpoint stage、mutation type distribution shift、或随机噪声）。\n\n**[C2] CWM 8B repo-level 结果缺失，\"formulation bottleneck\" claim 在最关键条件下未验证。（R1-N2, R2 附议）**\n论文核心叙事是 CWM 失败为 formulation-level bottleneck。此论断在函数级有间接支持（CWM 4B→8B 无改善），但在 repo-level 完全缺乏验证。若 CWM 8B repo-level 显著优于 CWM 4B，\"formulation bottleneck\" 叙事将被削弱。论文 conclusion 承认 \"awaits CWM 8B results\" 但 abstract/introduction 以肯定语气阐述。\n- **要求**：(1) 完成 CWM 8B repo-level 训练（deadline 前应可完成）；(2) 若无法完成，需在 abstract/introduction 中显著弱化为条件性表述。\n\n**[C3] CWM baseline 的 LoRA fine-tuning (rank 16) 可能系统性低估 generation formulation 能力。（R1-N3 + R2-W3, 完全一致）**\n原始 CWM 是 32B mid-trained 模型，本文 CWM 是 4B/8B LoRA（rank 16, ~0.1% trainable params）。LoRA 低秩约束对 generation（需学习精确 token 序列映射）的惩罚可能大于 classification（仅二值决策边界）——这是 R1 独到的观察，R2 交叉回应明确认同。论文无法区分 \"generation formulation inherently struggles\" 和 \"small LoRA-finetuned models struggle to generate complex outputs\"。Introduction \"CWM failure modes are artifacts of the generation formulation\" 超出证据支撑。\n- **要求**：(1) 增加 LoRA rank 消融（32/64/128），观察 unparseable rate 和准确率变化；(2) 限定 claim 范围为 \"LoRA fine-tuned small models\"。\n\n**[C4] 核心贡献新颖性争议。（R2-W1, R1 部分反驳——唯一分歧点）**\n- **R2 立场（Excitement 2/5）**：generation→classification 是 NLP 成熟路线（T5/BART/SQuAD）；complexity-dependent advantage 可从第一性原理预期；Ye et al. 和 CodeMind 已识别关键 failure modes，CLS 是 obvious next step。贡献是量化已知趋势而非发现新现象。当前状态更适合 Findings。\n- **R1 立场（Excitement 3/5）**：Format compliance collapse 的具体现象（parseable outputs anti-informative at 42-43%）此前未被记录，这是质变而非量变；oracle framework 是独立分析贡献。Novelty 达 Findings 级别。\n- **Director 判断**：两位 Reviewer 在 Overall 评分上一致（均 2.5/5），分歧仅在 Excitement（0.5 分差距）。novelty 确实主要是实证性的，缺少 algorithmic innovation。建议投 Findings track 或通过补充实验（CWM 8B、LoRA rank 消融、re-repair pilot）显著强化 empirical contribution。\n\n### Warning（Should-Fix 问题）\n\n**[W1] 标题 \"scales\" 缺乏数据支撑。（R2-W4, R1 同意有问题）**\n函数级 CLS 4B→8B: +0.99pp（微弱）。仓库级 CLS 4B→8B: 83.63→83.52（seed 42, 无改善）。\"Scales\" 在 ML 语境中默认含义为 model/data scaling，但数据不支持。如意图表达 complexity scaling，应明确化（如 \"Generalizes\" 或 \"Persists\"）。R1 提供了有价值的双重语义分析。\n\n**[W2] TOST ±2pp equivalence margin 缺乏正当性论证。（R1-W1 + R2-W7, 完全一致）**\nMargin 选择决定 \"equivalence\" 含义。未解释 ±2pp 依据，未报告不同 margin 下结果。建议报告 ±1pp/±2pp/±3pp 的 TOST 结果。\n\n**[W3] Scaling argument (CWM -0.27pp) 被未调优 hyperparameter 混淆。（R1-W2）**\nCWM -0.27pp 在 3-seed std ~0.5pp 内，统计上不显著。LoRA rank/lr 未为 8B 重新调优。\"CWM does not benefit from scaling\" 的 claim 过强。\n\n**[W4] CWM exact string matching 未尝试 relaxed matching。（R1-W4, R2 交叉回应认同遗漏）**\nFootnote 1 称 exact match 是 \"conservative lower bound\"，但未提供 relaxed matching 数据点。若 relaxed matching 显著提升 CWM 准确率，部分 \"formulation 缺陷\" 可能是 evaluation metric artifact。至少在函数级报告一种 relaxed matching variant。\n\n**[W5] Per-test diagnostic granularity 列为主要贡献但无下游 re-repair 实验验证。（R2-W5, R1 同意）**\nContribution 2 声称 \"enables targeted re-repair\" 但全文无任何下游实验。Oracle analysis 假设 ground-truth labels，实际 ~12% 错误率下 utility 未知。建议降级为 \"potential application\" 或补充 pilot 实验。\n\n**[W6] 遗漏重要相关工作。（R2-W6, R1 同意）**\n- LEVER (Ni et al., ICML 2023)：训练 learned verifier 做 classification-based reranking，概念上高度相似。应在 Related Work 讨论。\n- CodeT (Chen et al., ICLR 2023)：dual execution agreement。相关性较弱但值得提及。\n- 建议增加 \"Learned Code Verifiers\" 讨论段。\n\n**[W7] 人工突变 vs 真实 bug 的 ecological validity 未讨论。（R1-W5 + R2-W9, 完全一致）**\n5 种 mutation type 覆盖充分性、synthetic-to-real gap 均未讨论。缺少 Andrews et al. (2005, ICSE) 和 Just et al. (2014, FSE) 引用。\n\n**[W8] Val-test mutation type distribution shift 对 checkpoint selection 影响未充分分析。（R1-W3）**\noperator_swap val 19.1% → test 34.3%。未报告 per-type 准确率或 val/test 分布。\n\n**[W9] 多条引用 first author 与 arXiv 记录不一致。（R2-W8）**\nwu2025patchreasoner（bib: Wu Zuxin, arXiv: Xu Junjielong）、ding2025selfexecution（bib: Ding, API: Maimon）等。需逐条核查。\n\n### Info（Minor 问题）\n\n- [I1] \"Below chance level (50%)\" 在类别不平衡场景下易误解（majority baseline 73%）（R1-M1）\n- [I2] Qwen3 模型引用了 Qwen2.5 技术报告（R1-M2）\n- [I3] 5-seed 统计混合 bfloat16 和 NF4 量化精度（R1-M3）\n- [I4] Unparseable CWM outputs 的 verdict assignment 策略未明确（R1-M4）\n- [I5] \"D088 protocol\" 未定义（R2-M2, R1 同意）\n\n---\n\n## Reviewer Consensus（[AGREE] 项）\n\n两位 Reviewer 在以下 25 项评审点上达成完全一致（[AGREE]）：\n- **所有 Strengths**（S1-S5 + R2-S3）\n- **核心 Weaknesses**：单 seed claim (C1)、CWM 8B 缺失 (C2)、LoRA overclaim (C3)、TOST margin (W2)、synthetic-to-real gap (W7)、no re-repair experiment (W5)、LEVER/CodeT 遗漏 (W6)\n- R1 提出的 W4（relaxed matching）：R2 交叉回应中明确认同为自己遗漏的重要问题\n- R2 提出的 W4（标题 \"scales\"）：R1 同意有问题（with nuanced dual-interpretation analysis）\n\n---\n\n## Reviewer Divergence（[REBUT] 项）\n\n**唯一实质分歧：Novelty / Excitement 评分**\n| | R1 | R2 |\n|---|---|---|\n| Excitement | 3/5 | 2/5 |\n| 立场 | Format compliance collapse 是未记录的质变现象；oracle framework 是独立贡献；novelty 达 Findings 级 | 定性方向可预期；先验工作已识别 failure modes；CLS 是 obvious next step；贡献是量化已知趋势 |\n| 对论文的影响 | 补充实验后可接受为 Findings | 不确定是否达到 Findings 门槛 |\n\n**Minor 分歧**（不影响结论）：\n- Abstract 信息密度：R2 认为过高（M1），R1 反驳认为对 empirical paper 合理\n- 引用数量：R2 认为偏少（M5），R1 反驳认为应按遗漏而非数量评判\n- 标题 \"scales\" 严重性：R2 列为 Must-Fix，R1 降为 Should-Fix\n\n---\n\n## Questions（汇总，需作者回答）\n\n1. CWM eval 时提高 max_seq_length 到 8192，unparseable rate 和 accuracy 是否变化？（R1-Q1）\n2. CLS 4B seed 42 选中哪个 checkpoint step？与 seed 123 (step 800) 的 val/test accuracy 关系？（R1-Q2, R2-Q2）\n3. 是否尝试过 LoRA rank 32/64？CWM unparseable rate 是否随 rank 下降？（R1-Q3）\n4. Majority voting pairwise agreement rate 和 error overlap？（R1-Q4）\n5. Repo-level oracle ensemble (CLS+CWM) 结果？CWM anti-informative 时 ensemble 是否反而更差？（R1-Q5）\n6. 5 种 mutation type 选择依据和覆盖率分析？（R1-Q6）\n7. 32B CWM 在 repo-level 是否仍有 format compliance collapse？（R2-Q1）\n8. TOST ±1pp 时结论是否改变？（R2-Q3）\n9. CWM 低方差是 bottleneck 还是 representation stability？如何区分？（R2-Q4）\n10. Per-test granularity \"enables re-repair\" 有任何初步实验？（R2-Q6）\n\n---\n\n## Missing References\n\n1. **LEVER** (Ni et al., ICML 2023) — learned code verifier，classification-based reranking\n2. **CodeT** (Chen et al., ICLR 2023) — dual execution agreement\n3. **Andrews et al.** (2005, ICSE) — mutation vs real faults 经典讨论\n4. **Just et al.** (2014, FSE) — mutants as valid substitute for real faults\n5. **VG-Search** (Wang et al., 2025) — 应在 introduction 更早提及以建立 motivation\n6. Qwen3 独立技术报告（如存在，替换 Qwen2.5 引用）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**Overall Score: Weak Reject（建议 Resubmit 或转投 Findings）**\n\n**评分依据**：\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 2.5/5 | 2.5/5 | **2.5/5** |\n| Excitement | 3/5 | 2/5 | **2.5/5** |\n| Overall | 2.5/5 | 2.5/5 | **2.5/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**核心判断**：\n\n论文提出了一个有价值的 research question，实验设计框架（controlled formulation comparison）和统计方法论展现了专业水准。但四个核心问题共同削弱了论文的可接收性：\n\n1. **证据不足以支撑 claim 强度**：repo-level 最突出数字（25.59pp）来自单 seed 且 seed 方差极大（8.3pp）；CWM 8B repo-level 缺失使 \"formulation bottleneck\" claim 在最关键条件下无法验证。\n2. **实验设计可能系统性偏向 CLS**：LoRA rank 16 对 generation 的惩罚可能大于 classification；CWM 使用 exact string matching 而非 relaxed matching。\n3. **Claim 超出证据范围**：从 4B LoRA CWM 推广到 \"generation formulation\" 整体；标题 \"scales\" 暗示 model-size scaling 但数据不支持；per-test diagnostic granularity 作为 contribution 但无下游验证。\n4. **Novelty 争议**：贡献主要是实证性的（量化 complexity-dependent advantage），缺少 algorithmic innovation。R2 认为可预期，R1 认为 format compliance collapse 的质变特征有独立价值。\n\n**建议路径**：\n- **最优路径**：补充 CWM 8B repo-level + LoRA rank 消融 + 校准 claim 强度 → 投 Findings track\n- **快速路径**：不补实验，但大幅弱化 claim（去掉 \"formulation bottleneck\" 因果推断，改为观察性描述）+ 修改标题 + 补引用 → 投 Findings track（竞争力较弱）\n- **不建议**：当前状态直接投 Main conference\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度高但可接受（R1 立场）；15+ 数字对 empirical paper 合理\n- 25.59pp 应改为区间表述（C1）\n- \"scales\" 一词需修改（W1）\n\n### Introduction\n- 三个 contribution 的支撑程度不均：Contribution 1（complexity-dependent advantage）需多 seed 支撑；Contribution 2（diagnostic granularity at equivalent accuracy）需弱化为 potential application；Contribution 3（accuracy-utility frontier）支撑最充分\n- \"CWM failure modes are artifacts of the generation formulation\" 需限定范围（C3）\n\n### Method (Section 3)\n- Problem setup 和 formulation comparison 清晰\n- CWM failure modes 分析（Section 3.3）需添加 caveat 关于 LoRA 容量限制\n- Oracle framework（Section 3.4）是论文最强贡献之一\n\n### Experiments (Section 4)\n- Function-level (Section 4.2)：设计较好，5-seed 覆盖，但需标注 NF4 seed（I3）\n- Scaling (Section 4.3)：CWM -0.27pp 论证过强，需弱化（W3）\n- Equivalence (Section 4.4)：TOST margin 需论证（W2）\n- Oracle (Section 4.5)：分析扎实\n- Repo-level (Section 4.6)：核心问题集中地——单 seed（C1）、CWM 8B 缺失（C2）、unparseable 处理策略不明（I4）\n\n### Related Work (Section 5)\n- 缺少 LEVER/CodeT 讨论（W6）\n- 建议增加 \"Learned Code Verifiers\" 段\n- VG-Search 讨论过晚（应在 introduction 建立 motivation）\n\n### Conclusion (Section 6)\n- Limitations 段落覆盖面较广但缺少 synthetic-to-real gap 讨论（W7）\n- \"Formulation bottleneck\" 的条件性表述在 conclusion 中有但在 abstract/introduction 中缺失（C2）\n\n---\n\n## Issue Tracker 同步\n\n已更新 `projects/exec-sim-repair-verifier/artifacts/review_issues.yaml`，共 17 个 issue：\n- Critical (4): C1 单 seed, C2 CWM 8B 缺失, C3 LoRA overclaim, C4 novelty 争议\n- Warning (9): W1-W9\n- Info (5): I1-I5\n\n---\n\n*圆桌审稿 Round 1 完成。两位 Reviewer 经交叉分享后在关键问题上达成共识，唯一分歧（Excitement 3 vs 2）已如实记录。*"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-15T11:51:03.992523+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5182
}
```

</details>

---


### Assistant

_source line 118 · 2026-05-15T11:51:10.773232+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿 Round 1 完成，总结：**

- **Overall Score: Weak Reject（2.5/5）**，建议 Resubmit 或转投 Findings track
- 4 个 Critical issue、9 个 Warning、5 个 Info，共 17 个 issue 已写入 tracker
- 两位 Reviewer 在 25 项评审点上达成共识，唯一分歧在 Excitement（R1: 3/5 vs R2: 2/5）
- 建议路径：补充 CWM 8B repo-level + LoRA rank 消融 + 校准 claim 强度 → 投 Findings

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 119 · 2026-05-15T11:51:13.337016+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心立场：与 R2 在单 seed repo-level（W2）和 LoRA overclaim（W3）上完全一致；在 novelty 判断上有 ~0.5 分分歧——我认为 format compliance collapse 的定量发现和 oracle framework 构成 Findings 级 novelty，R2 认为不够 Main。标题 "scales" 的问题（W4）我认同 R2 的观察但建议降为 Should-Fix，因为 complexity scaling 的解读有一定道理，只是措辞含混。LEVER/CodeT 遗漏（W6）确认应补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 120 · 2026-05-15T11:51:19.994668+00:00_

审稿报告已投递至 Research Director，圆桌审稿 Round 1 完成。

**最终结论：Weak Reject（建议 Resubmit 或转投 Findings）**

4 个 Critical issue、9 个 Warning、5 个 Info，Issue Tracker 已同步。报告已通过 `submit_review_report_to_research_director` 送达。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 10

## Round 10

8 recorded events


### User

_source line 121 · 2026-05-18T18:11:53.663294+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 2 审稿意见（修订版论文：新颖性 + 完整性 + 写作质量）

**论文**：The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study
**注意**：论文已从 v1 大幅修订。新标题、新 contributions、新增 DeepSeek 跨模型验证、多项消融实验、47 条引用（v1: 26 条）。

---

### 1. Summary

本文系统比较 execution-free verification 三种形式化（CLS/CWM/TRAJ），使用 Qwen3 + DeepSeek-Coder 在函数级和仓库级进行受控实验。核心发现：函数级三种形式化等效；仓库级 CWM 大幅退化（19-26pp），方向 formulation-inherent，幅度 model-contingent。相比 v1 改进显著。

### 2. Strengths

- **S1.** Framing 从 advocacy 转为中性描述（design space study），诚实度大幅提升
- **S2.** DeepSeek 跨模型验证是关键补充——两个模型家族一致方向提供 formulation-inherent 证据
- **S3.** 消融实验堵住多个替代假设：LoRA rank 32 无改善、relaxed matching 反降 CWM、匹配上下文 98% gap 来自 formulation
- **S4.** TOST sensitivity 分析（Table 4）直接回应 Round 1 W7
- **S5.** 217× throughput advantage 和 CLS-TRAJ crossover 分析有部署实用价值
- **S6.** 47 references 全面覆盖 LEVER/CodeT/process supervision/mutation validity 等

### 3. Weaknesses

- **W1 [High]** %%SCENARIO-A%% 条件标记仍可见于 abstract/intro/experiments/conclusion。暗示 work-in-progress。
- **W2 [High]** 仓库级 same-size 比较仍为单 seed（CLS 4B: s42=83.63% vs s123=75.33%，差 8.3pp 未解决）。
- **W3 [Medium-High]** DeepSeek CWM repo-level 为 preliminary 数据，但 cross-model claims 以确定语气陈述。
- **W4 [Medium]** 核心 insight 定性方向仍可预期（generation 在复杂输出上退化更严重 = expected）。
- **W5 [Medium]** Oracle framework 用 function-level ICC (0.191) 应用于 repo-level 分析，但 repo-level ICC = 0.3146 未用于 oracle 计算。
- **W6 [Low-Medium]** Pilot re-repair study 给出负面结果但埋在 Future Work；Contribution 4 仍以正面语气呈现 diagnostic granularity。

### 4. Questions

Q1. %%SCENARIO-A%% 标记在 PDF 中是否可见？
Q2. DeepSeek CWM final results 何时完成？是否能赶上 ARR deadline？
Q3. Pilot re-repair negative result 的具体设置？是否应更突出报告？
Q4. CWM 8B parseable acc 低于 4B 是否可能是 Qwen3-specific？
Q5. ICC = 0.191 是否在 DeepSeek 上复现？

### 5. Overall Assessment

**Score: 3 (Weak Reject) / 对应 ARR Overall: 2.5-3**

| ARR 维度 | 分数 | 变化 | 理由 |
|----------|------|------|------|
| Soundness | 3.5/5 | ↑ (from 2.5) | 消融实验和跨模型验证显著增强；但单 seed repo-level 和 preliminary data 仍限制信度 |
| Excitement | 2.5/5 | ↑ (from 2) | Interaction framing 比 v1 更有趣；但定性方向仍可预期 |
| Overall | 3/5 | ↑ (from 2.5) | 介于 Findings 和 Conference；实验工艺优秀但 novelty 有限 |
| Confidence | 4/5 | 不变 | |

**vs Round 1 变化总结：** Soundness +1.0（消融堵住替代假设），Excitement +0.5（interaction framing 更好），Overall +0.5（整体改善但核心局限未完全解决）。如果 multi-seed repo + final DeepSeek CWM 完成，可升至 Overall 3.5。当前状态推荐 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-18T18:12:30.017742+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-18T18:12:31.374127+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (190 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-18T13:56:50Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 190 个实验 — ALLOCATED 1, ANALYZING 1, DONE 182, PREPARING 6\n**DONE 分布**: failed 41, killed 26, negative 7, success 108\n\n### 💾 磁盘余量\n- **seetacloud-westd-4x5090**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 436G/879G 可用（已用 48%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `deepseek-0shot-func-baseline` [success] — 2026-05-18T00:10:08\n- `qwen3-0shot-func-baseline` [success] — 2026-05-18T00:10:06\n- `deepseek-0shot-repo-baseline` [success] — 2026-05-18T00:10:04\n- `repo-level-0shot-baseline` [success] — 2026-05-17T23:29:33\n- `deepseek-cwm-repo-s123` [failed] — 2026-05-17T16:16:42 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n\n### 🔴 最近失败原因 (top 3)\n- `deepseek-cwm-repo-s123`: process dead 5× with no sentinel/W&B — auto-resolved as failed\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cls-repo-s123 | DeepSeek CLS repo-level seed 
…[truncated 1841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-18T18:12:31.425173+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-18T18:12:31.576347+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\traj}{\textsc{Traj}}
26	\newcommand{\fone}{F\textsubscript{1}}
27	\newcommand{\pp}{\,\text{pp}}
28	
29	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Controlled Empirical Study}
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{abstract}
36	
37	\input{introduction}
38	
39	\begin{figure*}[t]
40	\centering
41	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
42	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
43	\label{fig:reformulation}
44	\end{figure*}
45	
46	\input{method}
47	
48	\input{experiments}
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
53	\caption{Gap amplification from function-level to repo-level complexity. Function-level: \cls{}--\cwm{} gap is 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B (2 matched seeds, bootstrap $p{<}.01$). Repo-level same-size 4B: the gap explodes to 25.59\pp{}, with \cwm{} falling below the majority baseline (72.96\%).}
54	\label{fig:scaling_gap}
55	\end{figure}
56	
57	
58	\input{related_work}
59	
60	\input{con
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-18T18:12:31.627267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-18T18:12:31.678596+00:00_

1	issues:
2	- id: "R1-N1"
3	  summary: "Repo-level 核心 claim (25.59pp) 基于单 seed，seed 方差极大 (8.3pp)"
4	  category: experiment
5	  severity: critical
6	  status: in_progress
7	  first_raised_round: 1
8	  last_seen_round: 1
9	  mentions:
10	    - round: 1
11	      reviewers: [1, 2]
12	      note: "R1-N1 + R2-W2 完全一致。CLS 4B s42=83.63% vs s123=75.33%，abstract/intro 用单点最优值 25.59pp 构成 framing bias。"
13	  action_items:
14	    - round: 1
15	      action: "保留 25.59pp 作为 primary same-size 数字；补充展示 24.8-26.5pp across configurations（context-matched 到 cross-size）；分析 s42 vs s123 差异根因（checkpoint stage / mutation type sensitivity）"
16	      assigned_to: "agent+paper"
17	      status: in_progress
18	      progress_note: "8B-8B 双 seed gap 稳健（s42: 25.48pp, s123: 26.51pp）。D096 已切换主表为 8B-8B。等 DeepSeek repo 结果提供跨模型验证后统一更新 abstract/intro。"
19	  resolution: ""
20	  resolution_round: null
21	
22	- id: "R1-N2"
23	  summary: "CWM 8B repo-level 结果缺失，formulation bottleneck claim 在最关键条件下无法验证"
24	  category: experiment
25	  severity: critical
26	  status: in_progress
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  mentions:
30	    - round: 1
31	      reviewers: [1, 2]
32	      note: "R1-N2，R2 在 W3 中附议。"
33	  action_items:
34	    - round: 1
35	      action: "CWM 8B repo-level 训练 + DeepSeek CWM repo 训练"
36	      assigned_to: "agent"
37	      status: in_progress
38	      progress_note: "Qwen CWM 8B 已完成（65.17%, 73.8% unparse）。DeepSeek CWM repo 训练中（seetacloud cuda:1 s42 98%, cuda:3 s123 67%）。"
39	  resolution: ""
40	  resolution_round: null
41	
42	- id: "R1-N3"
43	  summary: "CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力"
44	  category: method
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  mentions:
50	    - round: 1
51	      reviewers: [1, 2]
52	      note: "R1-N3 + R2-W3。LoRA 低秩约束对 generation 惩罚可能大于 classification。"
53	  action_items:
54	    - round: 1
55	      action: "函数级 CWM 4B LoRA rank 32/64 消融"
56	      assigned_to: "agen
…[truncated 10188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 128 · 2026-05-18T18:13:01.066112+00:00_

上下文已恢复。

**Round 1 → Round 2 变化梳理**（基于 Issue Tracker）：

| Issue | Round 1 状态 | Round 2 状态 |
|-------|-------------|-------------|
| R1-N1 单 seed | critical/open | in_progress（8B-8B 双 seed 稳健，切换主表） |
| R1-N2 CWM 8B 缺失 | critical/open | in_progress（Qwen CWM 8B 完成 65.17%；DeepSeek CWM 训练中） |
| R1-N3 LoRA rank | critical/open | **resolved**（rank 32 消融完成，无改善） |
| R2-W1 novelty | critical/open | in_progress（framing pivot to design space study） |
| R2-W4 标题 "scales" | warning/open | **resolved**（新标题） |
| R1-W1 TOST margin | warning/open | **resolved**（sensitivity table） |
| R1-W2 scaling argument | warning/open | **resolved**（弱化表述） |
| R1-W3 val-test shift | warning/open | **resolved**（appendix table） |
| R1-W4 relaxed matching | warning/open | **resolved**（实验完成，反降 CWM） |
| 其余 8 项 | info/warning | **全部 resolved** |

**R2 Round 2 收到**：Overall 3/5（↑0.5），Soundness 3.5/5（↑1.0），Excitement 2.5/5（↑0.5）。新增问题：%%SCENARIO-A%% 标记残留（W1 High）、单 seed 仍未完全解决（W2 High）、DeepSeek preliminary data（W3）、ICC 不匹配（W5）。

等待 R1 Round 2 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 11

## Round 11

6 recorded events


### User

_source line 129 · 2026-05-18T18:13:02.033963+00:00_

[Reviewer 2 审稿结果]:
Round 2 审稿意见已提交。

核心评估：论文从 v1 有实质性改进（Soundness 2.5→3.5, Excitement 2→2.5, Overall 2.5→3）。消融实验（LoRA rank、relaxed matching、sequence length）和 DeepSeek 跨模型验证堵住了 Round 1 多个替代假设。但两个核心障碍仍存在：(1) 仓库级单 seed + DeepSeek CWM preliminary data；(2) 定性方向可预期。推荐 Findings 而非 main conference。

---

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见（修订版论文）

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study"
**审查侧重**: 实验方法论 + 统计严谨性 + 结果有效性 + 完整性
**Venue**: EMNLP 2026 Main Conference (ARR May cycle)

---

## 1. Summary

本文是关于 execution-free 代码修复验证的首个受控 formulation 对比研究，系统比较了 per-test 分类（CLS）、输出生成（CWM）和 trajectory-level 评分（TRAJ）三种 formulation，跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function/repo）和多 seed。核心发现是 formulation 等价性在 function-level 成立、在 repo-level 剧烈分化，且分化方向是 formulation-inherent 但幅度是 model-contingent。相比前一版本，论文增加了 DeepSeek 跨模型验证、TOST sensitivity 分析、LoRA rank 消融、relaxed matching 实验和 re-repair pilot 负结果，claim 校准程度大幅提高。

---

## 2. Strengths

**S1. Framing 的根本性改善。** 标题从 "Classification Scales Where Generation Stalls"（advocacy 语气）改为 "The Formulation Design Space..."（neutral comparison 语气）。核心叙事从 "CLS is superior" 转向 "formulation × model × complexity interaction"，每个 claim 都用条件性表述限定范围。这一转变使论文的科学姿态与证据强度匹配。Abstract 中用 "19–26pp" 范围替代了之前的单点 "25.59pp"。

**S2. DeepSeek 跨模型验证是本修订最重要的实质性改进。** Table 1 中 DeepSeek-Coder-6.7B 的三 formulation 结果（CLS 86.85%, CWM 86.83%, TRAJ 84.16%）独立确认了 function-level 等价性。Repo-level 的 degradation pattern（Qwen3: ~5/22pp for CLS/CWM; DeepSeek: ~12/25pp）支持 "formulation-inherent direction, model-contingent magnitude" 的核心 claim。这从根本上提升了论文从单模型观察到 generalizable finding 的转变。

**S3. 消融实验系统地封堵了替代解释。** (1) LoRA rank 消融（rank 32, -0.51pp, Appendix Table 6）排除了 adapter capacity bottleneck 解释。(2) Relaxed matching 实验（Section 4.7c, 58.04→56.98%）反转了 "exact match 不公平惩罚 CWM" 的假设——relaxed matching 反而降低 CWM 准确率，因为 unparseable outputs 的 majority-class default 比 parseable predictions 更准确。(3) 匹配上下文消融（CLS@2048: 83.04%, 98% of full gap, Appendix）排除了 input context disparity 解释。这三个消融共同收窄了因果解释空间。

**S4. TOST sensitivity 分析（Table, Section 4.3）回应了 ±2pp 任意性质疑。** 报告了 ±1pp/±2pp/±3pp 三档结果，给出 minimum margin ±1.63pp，并以 deployment-significance 论证了 ±2pp 选择。这是比之前版本显著的改进。

**S5. 负结果的诚实报告。** (1) Re-repair pilot（n=44, p=0.42, Conclusion Future Work）发现 per-test diagnostics 无可测量的下游改善；(2) Majority voting -0.68pp（Appendix paragraph g）；(3) CWM 8B parseable-only accuracy 低于 4B（38.52% vs 42.88%, Table 6 footnote）。这些负结果增强了论文的可信度。

**S6. 全面的超参数和分布报告。** Appendix Table 8（hyperparams）覆盖所有 6 个配置、Appendix Table 9（mutation distribution）报告了 val-test shift 并与 per-type accuracy 交叉分析。Reproducibility 显著提高。

---

## 3. Weaknesses (ranked by severity)

**W1 [High] Repo-level 证据仍然稀疏：多个核心比较基于单 seed，Table 6 含多个 TBD/preliminary 条目。**
- 位置：Table 6, Section 4.6
- 问题：Table 6 的完整性问题：Qwen3-4B CLS/CWM 是单 seed（42）；Qwen3-8B CWM 单 seed（42）；DeepSeek CWM "~60" 标注 "preliminary (training in progress)"；Qwen3 TRAJ 两行都是 "TBD"。一个投稿论文的核心 result table 包含两个 TBD、一个 ~approximate 和一个 footnote "running accuracy; final values pending"，这在审稿中是红旗。
- 为什么重要：Repo-level 是论文最有差异化价值的层级。Function-level 结论（formulation 等价）虽然有价值但 novelty 有限（正如 R2 Round 1 指出的）。论文的核心 impact 在于 repo-level divergence 的发现，但恰恰是这个层级的证据最不完整。
- 影响评估：如果 Qwen3 TRAJ repo-level 表现强于 CLS（如 DeepSeek TRAJ 75.35% vs CLS 74.93%），这将改变论文的 contribution ranking——TRAJ 可能是 repo-level 的更好选择（同等准确率、无 per-test aggregation 噪声），削弱 per-test granularity 的 motivation。
- 建议：完成所有 TBD 实验后再提交。如果 deadline 前无法完成，在 abstract 中明确标注哪些是 final、哪些是 preliminary，并在 Table 6 caption 中系统列出每个条目的 seed 数。

**W2 [High] DeepSeek CLS repo-level 仅 74.93%，几乎不高于 majority baseline（72.96%），削弱了 "CLS is the preferred repo-level formulation" 的叙事。**
- 位置：Table 6, Section 4.6 Cross-model validation
- 问题：DeepSeek TRAJ（75.35 ± 5.00, 6 seeds）实际上 slightly outperforms DeepSeek CLS（74.93%）。虽然差异在 TRAJ 的巨大方差（±5pp）内不显著，但这至少表明 CLS 在 DeepSeek repo-level 并不优于 TRAJ。论文的 contribution 4 声称 "per-test classification provides diagnostic granularity at equivalent trajectory-level accuracy"——但 DeepSeek repo-level 的数据显示 CLS 可能比 TRAJ *更差*（74.93 vs 75.35），这与该 contribution 矛盾。论文目前的处理方式是将 DeepSeek 定位为 "confirms formulation-inherent divergence"（CWM 差于 CLS），但回避了 CLS vs TRAJ 在 DeepSeek repo-level 的比较。
- 为什么重要：如果 per-test granularity 的价值在于下游 utility（re-repair），而 re-repair pilot 是负结果（W3），且 CLS 在 DeepSeek repo-level 并不优于 TRAJ，那么 per-test granularity 的实际价值很薄。
- 建议：在 Section 4.6 中增加 DeepSeek CLS vs TRAJ 的明确比较和讨论。如果 CLS 不 consistently 优于 TRAJ at repo level，应在 contribution 4 中限定 "at function level" 或 "on Qwen3"。

**W3 [Medium-High] Re-repair 负结果（n=44, p=0.42）被低调处理，但实质上削弱了 contribution 4 的实际价值。**
- 位置：Section 6 Conclusion, Future Work 段落（单句提及）
- 问题：论文在 Introduction contribution 4 中声称 "per-test diagnostic information at 217× higher throughput than generation"，motivation 多次提到 "targeted re-repair guided by per-test failure localization"（Introduction, Section 4.4, Conclusion）。但 Future Work 中透露 "A pilot study with 8B-scale repair agents found no measurable benefit from per-test diagnostics over binary accept/reject feedback"。这是一个与论文核心 motivation 直接矛盾的负结果，目前仅用一句话提及。
- 为什么重要：如果 per-test diagnostics 不能改善下游 re-repair，那么 per-test granularity 的价值缩减为 (a) 理论上的 oracle advantage（10.93pp, Table in Appendix）和 (b) 推理效率（217× throughput）。Oracle advantage 假设 ground-truth labels，real-world per-test advantage 被 ~12% error rate 上界。Throughput advantage 虽是 formulation 固有属性但对 *verifier* 而言不是独立贡献——it's an engineering property。
- 建议：将 re-repair 负结果从 Future Work 提升到 main text（如 Analysis section），报告实验细节（n=44 如何选取、什么 repair agent、什么 feedback format），并讨论为什么 per-test diagnostics 未能帮助 re-repair（可能原因：repair agent 的错误不在 test localization 而在 patch generation？）。调整 contribution 4 的表述，避免暗示 per-test diagnostics 有已验证的下游 utility。

**W4 [Medium] TRAJ 训练配置与 CLS/CWM 不完全受控：learning rate 不同（2×10⁻⁴ vs 5×10⁻⁵）、训练集大小不同（~8K vs 70K）。**
- 位置：Appendix Table 8 caption ("TRAJ models use lr = 2×10⁻⁴ due to the smaller training set (~8K instances vs. 70K for CLS/CWM)")
- 问题：TRAJ 因 formulation 固有属性（per-variant prediction）只能有 ~8K 训练样本，而 CLS/CWM 有 70K（per-test prediction）。这是 formulation 差异的一部分，但它意味着 CLS-TRAJ 的 TOST 等价检验混淆了 formulation effect 和 data volume effect。如果 TRAJ 有更多训练数据（例如通过 data augmentation 或 multi-instance sampling），其准确率可能高于当前的 86.30%，改变等价性结论。
- 为什么重要：TOST 等价（Section 4.3）是 contribution 4 的基础——"per-test classification provides diagnostic granularity at equivalent trajectory-level accuracy"。如果 TRAJ 因训练数据不足而被低估，等价性可能不成立。
- 建议：在 Section 4.3 或 Limitations 中明确讨论这一混淆因素。可以用 data ablation（将 CLS 训练数据降采样到 ~8K，观察准确率下降幅度）来部分量化 data volume 的 contribution。

**W5 [Medium] DeepSeek TRAJ repo-level 的 ±5pp 方差（6 seeds）表明该条件下结果极不稳定，但论文未充分分析。**
- 位置：Table 6 ("TRAJ 75.35 ± 5.00")
- 问题：6 seeds 的 ±5pp 标准差意味着 95% CI 大约 [65, 86]——跨越了 majority baseline（72.96%）。这意味着某些 seeds 的 TRAJ 显著低于 majority baseline。这种极端方差值得单独分析：是某些 seed 训练发散了？还是 checkpoint selection 的不稳定性？论文未讨论这一异常。
- 建议：报告 6 个 seed 的逐个准确率，标识异常 seed，分析方差来源。

**W6 [Low-Medium] 论文源码中的 `%%SCENARIO-A%%` 条件编译标记。**
- 位置：abstract.tex (line 4), introduction.tex (line 15), experiments.tex (lines 170-172), conclusion.tex (line 6)
- 问题：这些 LaTeX 注释标记意味着论文存在多个版本（Scenario A vs 非 A）。被注释掉的内容包括 CWM seed sensitivity 数据（~5pp vs ~2pp）、checkpoint sensitivity 分析、evaluation sensitivity 分析。如果这些内容在渲染 PDF 中不可见，那么论文缺失了几个重要的 robustness 分析。如果可见（即标记只是开发备注而实际内容未被注释），则不影响内容但在提交前应清理。
- 建议：确认渲染 PDF 的实际内容，移除所有内部标记后提交。

---

## 4. Questions for Authors

**Q1.** DeepSeek TRAJ repo-level 6 seeds 的逐个准确率是多少？±5pp 标准差中是否有 seed 低于 majority baseline？方差来源是 training instability 还是 checkpoint selection？

**Q2.** Table 6 中 DeepSeek CLS（74.93%）低于 DeepSeek TRAJ（75.35%）。这是否意味着在 DeepSeek + repo-level 条件下，per-test classification 不优于 trajectory-level？如果是，contribution 4 的 scope 如何限定？

**Q3.** Re-repair pilot（n=44, p=0.42）的实验设计细节：使用了什么 repair agent？per-test 信号如何传递给 repair agent（prompt format 还是 structured input）？repair agent 在看到 per-test failure localization 后的行为与看到 binary accept/reject 有何不同？n=44 的 statistical power 是否足以检测合理的 effect size（如 Cohen's d=0.3）？

**Q4.** TRAJ 的训练集（~8K）是 CLS/CWM 的 ~11%。是否有 CLS/CWM 在降采样到 ~8K 训练集后的准确率数据？这将量化 data volume 对 CLS-TRAJ 等价性结论的影响。

**Q5.** Table 2 scaling 分析使用 2 matched seeds（42, 123），但 clustered bootstrap p-value (0.0066) 来自 "3-seed superset (42, 123, 456)"。请澄清：scaling table 的数据基础和统计检验的数据基础是否一致？

---

## 5. Score

**Score: 4 (Weak Accept)**

**理由**：论文填补了 execution-free verification formulation 对比研究的空白，实验设计框架（controlled comparison, matched capacity）是 sound 的，消融实验系统地封堵了替代解释，claim 校准显著优于前一版本。DeepSeek 跨模型验证将论文从单模型观察提升为初步的 generalizable finding。

不给更高分的主要原因：(1) repo-level 证据仍不完整（Table 6 的 TBD/preliminary 条目）；(2) per-test granularity 的 practical value 被 re-repair 负结果和 DeepSeek CLS≈TRAJ 的 repo-level 结果共同削弱；(3) function-level formulation 等价是论文最 robust 的 finding，但也是 novelty 最低的 finding（"在简单任务上 generation 和 classification 差不多"不令人意外）。

论文的 novelty 主要是 empirical：没有新算法，但首次提供了 controlled comparison evidence，这对实践者选择 verification formulation 有直接价值。如果 Table 6 的所有 TBD 实验完成且结论一致，这是一篇扎实的 Findings 级工作。

## 6. Confidence

**Confidence: 4/5**

熟悉 code LLM、LoRA fine-tuning、TOST/bootstrap 统计方法和 SWE-bench 生态。对 DeepSeek-Coder 的具体 tokenizer 特性和 CWM 原始论文的 mid-training 细节不完全确认。

---

## 附：对 Director 实验覆盖度清单的评估

| 实验项 | 覆盖状态 | 评价 |
|--------|---------|------|
| Multi-seed core (CLS/CWM/TRAJ) | ✅ 5 seeds Qwen3, 2 seeds DeepSeek | 充分 |
| Model size scaling (4B→8B) | ✅ 三 formulation 均覆盖 (Table 2) | 充分（仅 Qwen3） |
| LLM Judge 0-shot baselines | ✅ Table 1: 0-shot, ZS judge, 3-shot ICL | 充分 |
| Per-test precision/recall | ✅ Section 4.7(e) | 充分（单 seed） |
| Oracle F2P stratified | ✅ Appendix Table | 充分 |
| Block correlation | ✅ Section 4.7(f), 两层 ICC | 充分 |
| Repo-level CLS/CWM/TRAJ | ⚠️ Qwen3 TRAJ: TBD; DeepSeek CWM: preliminary | 不完整 |
| TOST sensitivity | ✅ 新 Table, 3 档 margin | 充分 |
| Downstream re-repair | ⚠️ 负结果, n=44, 仅 Future Work 单句 | 有结果但报告不充分 |
| Cross-model validation | ✅ DeepSeek-Coder-6.7B | 重大改进 |
| LoRA rank ablation | ✅ Appendix Table 6 | 充分 |
| Relaxed matching | ✅ Section 4.7(c) | 充分，结果反直觉 |
| Mutation distribution | ✅ Appendix Table 9 | 充分 |
| Inference efficiency | ✅ Section 4.7(i) | 充分 |
| Trace-then-judge | ❌ 未在论文中出现 | 如有实验应报告 |

**总结**：覆盖度约 85%。关键缺口是 Qwen3 repo-level TRAJ 和 DeepSeek repo-level CWM 的 final 结果。Re-repair 负结果需要更充分的报告。


---

[Reviewer 1 审稿结果]:
审稿意见已提交。

核心评估：论文从前一版本大幅改进（更中性的 framing、DeepSeek 跨模型验证、消融实验、TOST sensitivity），给出 **Weak Accept (4/6)**。主要保留意见：(1) repo-level Table 仍有 TBD/preliminary 条目；(2) DeepSeek CLS repo-level 仅比 majority baseline 高 2pp 且不优于 TRAJ，削弱了 per-test granularity 的跨模型 claim；(3) re-repair 负结果需更充分报告。如果 TBD 实验完成且结论一致，是扎实的 Findings 级工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-18T18:13:48.670936+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的 Round 2 审稿意见\n\n以下是 Reviewer 1 的 Round 2 完整审稿原文。请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n**重点关注**：\n1. R1 给了 4/5 (Weak Accept)，你给了 3/5。请在交叉回应中论证你们的分歧——是否因为 R1 低估了 novelty 问题，还是你低估了修订版的改进？\n2. R1 新提出的 W2（DeepSeek CLS≈TRAJ 削弱 C4）和 W4（TRAJ 训练配置 confound）是你 Round 2 未覆盖的重要问题，请评估。\n\n---\n\n# Reviewer 1 — Round 2 审稿意见（完整原文）\n\n## 1. Summary\n本文是关于 execution-free 代码修复验证的首个受控 formulation 对比研究，系统比较了 CLS/CWM/TRAJ 三种 formulation，跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function/repo）和多 seed。核心发现是 formulation 等价性在 function-level 成立、在 repo-level 剧烈分化，且分化方向是 formulation-inherent 但幅度是 model-contingent。\n\n## 2. Strengths\nS1. Framing 的根本性改善（neutral comparison 语气，条件性表述）\nS2. DeepSeek 跨模型验证是最重要的实质性改进\nS3. 消融实验系统封堵替代解释（LoRA rank, relaxed matching, 匹配上下文）\nS4. TOST sensitivity 分析回应了 ±2pp 质疑\nS5. 负结果的诚实报告（re-repair pilot, majority voting, CWM 8B parseable<4B）\nS6. 全面的超参数和分布报告（Appendix Table 8/9）\n\n## 3. Weaknesses\n\n**W1 [High]** Table 6 含 TBD/preliminary 条目。Qwen3 TRAJ repo-level \"TBD\"，DeepSeek CWM \"~60 preliminary\"。投稿论文核心 result table 的 TBD 是红旗。如果 Qwen3 TRAJ 强于 CLS，将改变 contribution ranking。\n\n**W2 [High]** DeepSeek CLS repo-level 仅 74.93%（vs majority 72.96%），DeepSeek TRAJ 75.35±5.00 略优于 CLS。CLS 在 DeepSeek repo-level 并不优于 TRAJ，削弱 contribution 4（\"per-test diagnostic granularity at equivalent accuracy\"）。论文回避了 CLS vs TRAJ 在 DeepSeek repo-level 的比较。\n\n**W3 [Medium-High]** Re-repair 负结果（n=44, p=0.42）仅在 Future Work 单句提及，但实质上削弱了 contribution 4 的下游 utility motivation。应提升到 main text，报告实验细节。\n\n**W4 [Medium]** TRAJ 训练配置不完全受控：lr 2×10⁻⁴ vs CLS/CWM 5×10⁻⁵，训练集 ~8K vs 70K。CLS-TRAJ TOST 等价混淆了 formulation effect 和 data volume effect。建议 CLS 降采样到 ~8K 的消融。\n\n**W5 [Medium]** DeepSeek TRAJ repo-level ±5pp std（6 seeds）表明极端不稳定，95% CI 跨越 majority baseline。论文未分析。\n\n**W6 [Low-Medium]** %%SCENARIO-A%% 条件编译标记仍可见。\n\n## 4. Questions\nQ1. DeepSeek TRAJ 6 seeds 的逐个准确率？\nQ2. DeepSeek CLS < TRAJ at repo-level，contribution 4 scope 如何限定？\nQ3. Re-repair pilot 实验设计细节？n=44 的 power？\nQ4. CLS/CWM 降采样到 ~8K 的准确率？\nQ5. Table 2 的 2 matched seeds vs bootstrap 的 3-seed superset 是否一致？\n\n## 5. Score\n**Score: 4/5 (Weak Accept)**。Findings 级工作。关键缺口：Table 6 TBD、DeepSeek CLS≈TRAJ、re-repair 报告不充分。\n\n## 6. Confidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的 Round 2 审稿意见\n\n以下是 Reviewer 1 的 Round 2 完整审稿原文。请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n**重点关注**：\n1. R1 给了 4/5 (Weak Accept)，你给了 3/5。请在交叉回应中论证你们的分歧——是否因为 R1 低估了 novelty 问题，还是你低估了修订版的改进？\n2. R1 新提出的 W2（DeepSeek CLS≈TRAJ 削弱 C4）和 W4（TRAJ 训练配置 confound）是你 Round 2 未覆盖的重要问题，请评估。\n\n---\n\n# Reviewer 1 — Round 2 审稿意见（完整原文）\n\n## 1. Summary\n本文是关于 execution-free 代码修复验证的首个受控 formulation 对比研究，系统比较了 CLS/CWM/TRAJ 三种 formulation，跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function/repo）和多 seed。核心发现是 formulation 等价性在 function-level 成立、在 repo-level 剧烈分化，且分化方向是 formulation-inherent 但幅度是 model-contingent。\n\n## 2. Strengths\nS1. Framing 的根本性改善（neutral comparison 语气，条件性表述）\nS2. DeepSeek 跨模型验证是最重要的实质性改进\nS3. 消融实验系统封堵替代解释（LoRA rank, relaxed matching, 匹配上下文）\nS4. TOST sensitivity 分析回应了 ±2pp 质疑\nS5. 负结果的诚实报告（re-repair pilot, majority voting, CWM 8B parseable<4B）\nS6. 全面的超参数和分布报告（Appendix Table 8/9）\n\n## 3. Weaknesses\n\n**W1 [High]** Table 6 含 TBD/preliminary 条目。Qwen3 TRAJ repo-level \"TBD\"，DeepSeek CWM \"~60 preliminary\"。投稿论文核心 result table 的 TBD 是红旗。如果 Qwen3 TRAJ 强于 CLS，将改变 contribution ranking。\n\n**W2 [High]** DeepSeek CLS repo-level 仅 74.93%（vs majority 72.96%），DeepSeek TRAJ 75.35±5.00 略优于 CLS。CLS 在 DeepSeek repo-level 并不优于 TRAJ，削弱 contribution 4（\"per-test diagnostic granularity at equivalent accuracy\"）。论文回避了 CLS vs TRAJ 在 DeepSeek repo-level 的比较。\n\n**W3 [Medium-High]** Re-repair 负结果（n=44, p=0.42）仅在 Future Work 单句提及，但实质上削弱了 contribution 4 的下游 utility motivation。应提升到 main text，报告实验细节。\n\n**W4 [Medium]** TRAJ 训练配置不完全受控：lr 2×10⁻⁴ vs CLS/CWM 5×10⁻⁵，训练集 ~8K vs 70K。CLS-TRAJ TOST 等价混淆了 formulation effect 和 data volume effect。建议 CLS 降采样到 ~8K 的消融。\n\n**W5 [Medium]** DeepSeek TRAJ repo-level ±5pp std（6 seeds）表明极端不稳定，95% CI 跨越 majority baseline。论文未分析。\n\n**W6 [Low-Medium]** %%SCENARIO-A%% 条件编译标记仍可见。\n\n## 4. Questions\nQ1. DeepSeek TRAJ 6 seeds 的逐个准确率？\nQ2. DeepSeek CLS < TRAJ at repo-level，contribution 4 scope 如何限定？\nQ3. Re-repair pilot 实验设计细节？n=44 的 power？\nQ4. CLS/CWM 降采样到 ~8K 的准确率？\nQ5. Table 2 的 2 matched seeds vs bootstrap 的 3-seed superset 是否一致？\n\n## 5. Score\n**Score: 4/5 (Weak Accept)**。Findings 级工作。关键缺口：Table 6 TBD、DeepSeek CLS≈TRAJ、re-repair 报告不充分。\n\n## 6. Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-18T18:14:10.494001+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21823
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-18T18:14:10.696154+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的 Round 2 审稿意见\n\n以下是 Reviewer 2 的 Round 2 完整审稿原文。请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n**重点关注**：\n1. 你给了 4/5 (Weak Accept)，R2 给了 3/5。请论证你的更高分是否合理——R2 的 novelty concern (W4) 是否仍构成接收障碍？\n2. R2 的 W5（Oracle ICC 不匹配）是你未覆盖的问题，请评估。\n\n---\n\n# Reviewer 2 — Round 2 审稿意见（完整原文）\n\n## 1. Summary\n本文系统比较 execution-free verification 三种形式化（CLS/CWM/TRAJ），使用 Qwen3 + DeepSeek-Coder 在函数级和仓库级进行受控实验。核心发现：函数级三种形式化等效；仓库级 CWM 大幅退化（19-26pp），方向 formulation-inherent，幅度 model-contingent。相比 v1 改进显著。\n\n## 2. Strengths\nS1. Framing 从 advocacy 转为中性描述（design space study），诚实度大幅提升\nS2. DeepSeek 跨模型验证是关键补充\nS3. 消融实验堵住多个替代假设（LoRA rank 32、relaxed matching、匹配上下文 98%）\nS4. TOST sensitivity 分析直接回应 Round 1 W7\nS5. 217× throughput advantage 和 CLS-TRAJ crossover 分析有部署价值\nS6. 47 references 全面覆盖\n\n## 3. Weaknesses\n**W1 [High]** %%SCENARIO-A%% 条件标记仍可见于 abstract/intro/experiments/conclusion。暗示 work-in-progress。\n**W2 [High]** 仓库级 same-size 比较仍为单 seed（CLS 4B s42=83.63% vs s123=75.33%，差 8.3pp 未解决）。\n**W3 [Medium-High]** DeepSeek CWM repo-level 为 preliminary 数据，但 cross-model claims 以确定语气陈述。\n**W4 [Medium]** 核心 insight 定性方向仍可预期（generation 在复杂输出上退化更严重 = expected）。\n**W5 [Medium]** Oracle framework 用 function-level ICC (0.191) 应用于 repo-level 分析，但 repo-level ICC = 0.3146 未用于 oracle 计算。\n**W6 [Low-Medium]** Pilot re-repair study 负面结果埋在 Future Work；Contribution 4 仍以正面语气呈现。\n\n## 4. Questions\nQ1. %%SCENARIO-A%% 标记在 PDF 中是否可见？\nQ2. DeepSeek CWM final results 何时完成？\nQ3. Pilot re-repair negative result 的具体设置？\nQ4. CWM 8B parseable acc 低于 4B 是否 Qwen3-specific？\nQ5. ICC = 0.191 是否在 DeepSeek 上复现？\n\n## 5. Score\n**Score: 3/5 (Weak Reject) / ARR Overall: 2.5-3**\nSoundness 3.5 (↑from 2.5), Excitement 2.5 (↑from 2), Overall 3 (↑from 2.5)\n如果 multi-seed repo + final DeepSeek CWM 完成，可升至 3.5。当前推荐 Findings。\n\n## 6. Confidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的 Round 2 审稿意见\n\n以下是 Reviewer 2 的 Round 2 完整审稿原文。请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n**重点关注**：\n1. 你给了 4/5 (Weak Accept)，R2 给了 3/5。请论证你的更高分是否合理——R2 的 novelty concern (W4) 是否仍构成接收障碍？\n2. R2 的 W5（Oracle ICC 不匹配）是你未覆盖的问题，请评估。\n\n---\n\n# Reviewer 2 — Round 2 审稿意见（完整原文）\n\n## 1. Summary\n本文系统比较 execution-free verification 三种形式化（CLS/CWM/TRAJ），使用 Qwen3 + DeepSeek-Coder 在函数级和仓库级进行受控实验。核心发现：函数级三种形式化等效；仓库级 CWM 大幅退化（19-26pp），方向 formulation-inherent，幅度 model-contingent。相比 v1 改进显著。\n\n## 2. Strengths\nS1. Framing 从 advocacy 转为中性描述（design space study），诚实度大幅提升\nS2. DeepSeek 跨模型验证是关键补充\nS3. 消融实验堵住多个替代假设（LoRA rank 32、relaxed matching、匹配上下文 98%）\nS4. TOST sensitivity 分析直接回应 Round 1 W7\nS5. 217× throughput advantage 和 CLS-TRAJ crossover 分析有部署价值\nS6. 47 references 全面覆盖\n\n## 3. Weaknesses\n**W1 [High]** %%SCENARIO-A%% 条件标记仍可见于 abstract/intro/experiments/conclusion。暗示 work-in-progress。\n**W2 [High]** 仓库级 same-size 比较仍为单 seed（CLS 4B s42=83.63% vs s123=75.33%，差 8.3pp 未解决）。\n**W3 [Medium-High]** DeepSeek CWM repo-level 为 preliminary 数据，但 cross-model claims 以确定语气陈述。\n**W4 [Medium]** 核心 insight 定性方向仍可预期（generation 在复杂输出上退化更严重 = expected）。\n**W5 [Medium]** Oracle framework 用 function-level ICC (0.191) 应用于 repo-level 分析，但 repo-level ICC = 0.3146 未用于 oracle 计算。\n**W6 [Low-Medium]** Pilot re-repair study 负面结果埋在 Future Work；Contribution 4 仍以正面语气呈现。\n\n## 4. Questions\nQ1. %%SCENARIO-A%% 标记在 PDF 中是否可见？\nQ2. DeepSeek CWM final results 何时完成？\nQ3. Pilot re-repair negative result 的具体设置？\nQ4. CWM 8B parseable acc 低于 4B 是否 Qwen3-specific？\nQ5. ICC = 0.191 是否在 DeepSeek 上复现？\n\n## 5. Score\n**Score: 3/5 (Weak Reject) / ARR Overall: 2.5-3**\nSoundness 3.5 (↑from 2.5), Excitement 2.5 (↑from 2), Overall 3 (↑from 2.5)\n如果 multi-seed repo + final DeepSeek CWM 完成，可升至 3.5。当前推荐 Findings。\n\n## 6. Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-18T18:14:12.112200+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1416
}
```

</details>

---


### Assistant

_source line 134 · 2026-05-18T18:14:16.813275+00:00_

交叉分享已分配。等待两位 Reviewer 的逐条回应，完成后进入收敛判断和最终报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 135 · 2026-05-18T18:16:10.085270+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 2 意见的逐条评价

---

## 对 R2 Strengths 的回应

**[AGREE] R2-S1 至 R2-S6**：全部同意。R2 正确识别了修订版的六个主要改进，与我的 S1-S6 高度重叠。特别同意 S3（消融堵住替代假设）和 S5（throughput + crossover 分析的部署价值）的评估。无补充。

---

## 对 R2 Weaknesses 的回应

**[AGREE] R2-W1: "%%SCENARIO-A%% 条件标记仍可见于 abstract/intro/experiments/conclusion"**

同意。我在自己的 W6 中也标注了这个问题。补充一个 R2 未展开的关键点：如果这些标记在 LaTeX 中作为 `%` 注释处理（标准行为），那么被注释掉的内容——包括 CWM seed sensitivity 数据（~5pp vs ~2pp）、checkpoint sensitivity 分析、evaluation sensitivity 分析——在渲染 PDF 中不可见。这意味着论文的两种解读取决于作者的意图：

- **如果 SCENARIO-A 内容确实被排除**：论文丢失了几个重要的 robustness finding，特别是 "同一 CWM checkpoint 在不同 max_seq_length 下产生 ~9pp accuracy variation"（Section 4.6 Evaluation sensitivity）——这是一个对 practitioner 极有价值的发现。
- **如果 SCENARIO-A 内容通过某种机制包含在内**：条件标记本身暗示 work-in-progress 状态。

无论哪种情况，提交前必须清理。这是一个 formatting issue 而非 scientific issue，但审稿中属于 desk-reject-level 的不专业表现。

---

**[AGREE] R2-W2: "仓库级 same-size 比较仍为单 seed（CLS 4B s42=83.63% vs s123=75.33%，差 8.3pp 未解决）"**

完全同意。这与我在 Round 1 N1 和 Round 2 W1 中反复提出的问题一致。修订版在 abstract 中改用 "19–26pp" 范围表述（改进），但 Table 6 的数据基础没有变化：同尺寸 4B-4B 对比仍然只有 seed 42 一个数据点。CLS 4B seed 123 的 75.33% 在 Section 4.6 Limitations 中被披露但不出现在 Table 6 中——信息分布仍然不对称。

我的补充：修订版新增了 CWM 8B 数据（65.17%, 单 seed），但这也是单 seed。Table 6 的所有 Qwen3 CLS/CWM 同尺寸比较都是单 seed，这是论文在 repo-level 的核心统计弱点。**这个问题从 Round 1 到 Round 2 没有实质性改善。**

---

**[AGREE with nuance] R2-W3: "DeepSeek CWM repo-level 为 preliminary，但 cross-model claims 以确定语气陈述"**

同意核心观点：以 preliminary 数据支撑确定性 claim 不合适。Section 4.6 Cross-model validation 段落写道 "Cross-model validation with DeepSeek-Coder confirms the formulation-inherent nature of the divergence"——但 DeepSeek CWM 结果是 "~60" 加 footnote "running accuracy; final values pending"。用 "confirms" 修饰 preliminary data 确实过强。

**但我补充一点 R2 未提及的 nuance**：DeepSeek CLS 的 repo-level 结果（74.93%）是 final 的。即使 CWM preliminary result "~60" 的最终值有所变动（比如最终为 65%），CLS-CWM 的 gap 仍在 10-15pp 量级，方向不会翻转。因此 "direction is formulation-inherent" 这一定性结论大概率不会被 final data 推翻；问题在于 magnitude 的精确度和可信度。建议措辞改为 "preliminary cross-model results are consistent with formulation-inherent divergence, pending final CWM training completion."

---

**[REBUT partially] R2-W4: "核心 insight 定性方向仍可预期（generation 在复杂输出上退化更严重 = expected）"**

这是 R1-R2 从 Round 1 延续到 Round 2 的核心分歧点。R2 维持 Excitement 2.5/5，认为 "generation 在复杂输出上退化更严重" 是可预期的。

**我反驳的部分**：

R2 的论点过度简化了论文的实际 contribution。"Generation 在复杂输出上退化" 是一个定性预期，但论文的贡献不止于确认这一定性方向：

1. **Magnitude 量化是新的**。Prior work 没有报告 repo-level CWM 性能。论文发现 CWM 不仅退化，而且 parseable-only accuracy（42-43% at 4B, 38-39% at 8B, Table 6 footnote）低于 majority baseline（72.96%）和 random chance（50%）——即 CWM 的 parseable predictions 是 anti-informative 的。这不是 "退化更严重" 的量化延伸，而是一个 qualitative threshold crossing（从 noisy-but-useful 到 worse-than-trivial）。知道 "generation 退化" 和知道 "generation 变成反指标" 对 practitioner 的决策影响不同。

2. **Formulation × model interaction 是新发现**。R2 没有反驳这一点。"方向 formulation-inherent 但幅度 model-contingent"（Qwen3 CLS degradation ~5pp vs DeepSeek ~12pp）不是从 "generation 退化" 可以预期的——它表明 formulation 选择与模型选择之间存在交互效应，这对部署决策有直接意义。

3. **消融结果的反直觉发现**。Relaxed matching 降低而非提高 CWM 准确率（Section 4.7c）——这违反了 "exact match 不公平惩罚 CWM" 的直觉。LoRA rank 32 不改善 CWM（Appendix Table 6）——这排除了 capacity explanation。CWM 8B parseable-only accuracy 低于 4B（38.52% vs 42.88%）——这违反了 "更大模型更好" 的默认预期。这些消融结果中的多个违反了 prior expectations。

**我同意的部分**：

论文的 novelty 确实主要是 empirical 而非 algorithmic。没有新模型、新训练方法或新推理策略被提出。对于 EMNLP Main，这确实限制了 excitement。如果标准是 "is this a new method that opens a new research direction?"，答案是 no。如果标准是 "is this a rigorous empirical study that changes how practitioners make design decisions?"，答案是 yes。

**我的立场**：从 Round 1 到 Round 2，我的 excitement 评估没有变化（3/5）。论文处于 Findings 的 solid 区间——对于 Main conference 稍弱，但超过 "Weak Reject" 的门槛。R2 从 Round 1 的 2/5 提升到 2.5/5，这个方向是合理的。**我们的实质分歧约 0.5 分，集中在 "rigorous empirical comparison 的 novelty 是否足以支撑 Findings"。我认为足以。**

---

**[AGREE — 这是我未覆盖的有效批评] R2-W5: "Oracle framework 用 function-level ICC (0.191) 应用于 repo-level 分析，但 repo-level ICC = 0.3146 未用于 oracle 计算"**

**这是 R2 的一个好发现，我在两轮审稿中均未识别。**

具体问题：Appendix Table（Oracle accuracy-utility frontier）使用 ICC=0.191 进行 block-correlated oracle 计算。这个 ICC 来自 function-level TOST 分析（Section 4.3, "ICC = 0.191, p < 0.0001, DEFF = 3.97"）。但论文在 Section 4.6（或 Appendix 的 ICC sensitivity 段落）报告了 repo-level ICC = 0.3146（DEFF = 114.4）。

Oracle analysis 的 target population 是 SWE-bench Verified（repo-level），但使用的 ICC parameter 来自 function-level。这是一个 parameter mismatch。论文在 Appendix 中有一段 "Sensitivity to ICC estimate" 定性讨论了这一点，声称 function-level ICC "provides a conservative lower bound on the per-test advantage"，并指出 "the repo-level correlation structure would yield an even larger gap." 这个论证方向是正确的（更高的 ICC 意味着更强的 block correlation，放大 per-test 的优势），但如果 repo-level ICC 已经可用，为什么不直接用 repo-level ICC 重新计算 oracle table？

**影响评估**：

- 方向性影响：using repo-level ICC (0.3146) 而非 function-level ICC (0.191) 会**增大** block-correlated advantage 的估计值。因此当前的 oracle table 是 conservative 的——实际优势可能更大。这意味着 R2-W5 不会削弱论文的 claim（claim 是 "per-test advantage concentrates in T≥2 instances"），但会使 claim 的定量估计偏保守。
- 方法论影响：使用错误层级的 ICC 是统计分析中的 level-of-analysis 错误。即使结论方向不变，方法论上不够严谨。
- Practical fix：作者应同时报告 function-level ICC 和 repo-level ICC 下的 oracle 结果，作为 sensitivity analysis 的两端。

**我的建议**：这是一个 Should-Fix 级别的问题，不影响接收决定但应在 camera-ready 中修正。

---

**[AGREE] R2-W6: "Pilot re-repair study 负面结果埋在 Future Work；Contribution 4 仍以正面语气呈现"**

与我的 W3 完全一致。补充：Introduction 中 Contribution 4 写道 "per-test diagnostic information at 217× higher throughput than generation"，用 throughput 数字作为 headline metric。但 throughput 是 formulation 的固有物理属性（1 token vs O(L) tokens），不需要实验验证。真正需要验证的是 diagnostic granularity 的 downstream utility，而这恰恰是负结果。当前表述将 trivially true 的 throughput claim 和 empirically unvalidated 的 utility claim 混合在同一个 contribution 中，掩盖了后者的弱点。

建议将 Contribution 4 拆分为：(4a) 推理效率（217× throughput，formulation-inherent，trivially true）；(4b) 诊断粒度（oracle 上界 10.93pp，但 pilot re-repair 未检测到下游改善，n=44）。

---

## 对 R2 Questions 的回应

**[AGREE] R2-Q1: "%%SCENARIO-A%% 标记在 PDF 中是否可见？"**

必须回答的 formatting 问题。如我在 W1 回应中分析的，标准 LaTeX 行为下 `%%` 后内容被注释掉——即 SCENARIO-A 内容在 PDF 中不可见。但作者需要确认。

**[AGREE] R2-Q2: "DeepSeek CWM final results 何时完成？"**

合理要求。如果在 ARR cycle 内（~7 days to deadline）无法完成，论文应将所有基于 DeepSeek CWM 的 claim 降级为 preliminary。

**[AGREE] R2-Q3: "Pilot re-repair negative result 的具体设置？"**

与我的 Q3 完全一致。n=44, p=0.42 的实验缺乏足够报告细节。

**[AGREE — 好问题] R2-Q4: "CWM 8B parseable acc 低于 4B 是否 Qwen3-specific？"**

这是一个重要的 generalizability 问题。论文当前将 CWM 8B parseable accuracy degradation（42.88→38.52%）作为 "generation bottleneck" 的证据（Section 4.6 Default assignment artifact）。如果这仅在 Qwen3 上发生而在 DeepSeek 上不复现，则归因应从 "formulation-level" 降级为 "model-specific"。论文在 Section 4.7(b) 最后一句 actually 已经承认了这种可能性："per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-inherent one"——但这与主文 narrative 中反复使用的 "formulation bottleneck" 术语存在张力。

**[AGREE] R2-Q5: "ICC = 0.191 是否在 DeepSeek 上复现？"**

好问题。如果 DeepSeek 的 function-level ICC 显著不同于 0.191，TOST 等价检验的 clustered bootstrap 需要使用不同的 cluster structure。但更重要的是，这关系到 oracle framework 的 generalizability——如果 ICC 是 model-contingent 的，oracle advantage 估计也应按模型分别报告。

---

## R1 vs R2 Score 分歧分析

**分歧幅度**：R1 给 4/6（Weak Accept），R2 给 3/6（Weak Reject）。差距 1 分。

**分歧根源**：核心集中在 **novelty threshold** 上。

| 维度 | R1 评估 | R2 评估 | 差异来源 |
|------|---------|---------|----------|
| Soundness | ~3.5 (methodology sound, evidence incomplete) | 3.5 (↑from 2.5) | **一致** |
| Excitement/Novelty | 3 (rigorous empirical study, no new method) | 2.5 (expected direction) | **分歧核心** |
| Overall | 4/6 ≈ ARR 3 (Findings) | 3/6 ≈ ARR 2.5-3 (Borderline Findings) | **~0.5 分差距** |

**我维持 4/6 的理由**：

1. **Soundness 的改善超出预期。** 从 Round 1 到 Round 2，论文不仅增加了跨模型验证，还系统地封堵了 LoRA capacity、exact matching penalty、input context disparity 三个替代解释。这种 "address every alternative hypothesis" 的实验风格在 empirical papers 中值得鼓励。

2. **对 practitioner 的决策价值是具体的。** 论文的结论可以直接翻译为部署建议：function-level 选哪个 formulation 都行（省去了不必要的 engineering effort）；repo-level 不要用 CWM formulation（避免浪费 compute on anti-informative predictions）；throughput-sensitive 场景优先 CLS（217× speedup）；>50 tests 的 instance 用 TRAJ。这种 actionable specificity 在 EMNLP Findings 中有价值。

3. **Negative results 的诚实报告是 feature 而非 bug。** 论文报告了 majority voting 失败、re-repair 无效、CWM relaxed matching 更差、CWM 8B parseable accuracy 下降。这些 negative results 增强了论文作为 "field guide" 的信息密度。

**R2 的 concern 也有道理**：如果 EMNLP Findings 的隐含标准是 "至少有一个 surprising finding"，那么论文最 surprising 的 finding 是 relaxed matching 降低 CWM 准确率（Section 4.7c）和 CWM 8B parseable accuracy 低于 4B（Table 6 footnote）。这些确实违反直觉，但是否足够 "surprising" 来跨过 Findings 门槛，reasonable reviewers 可以 disagree。

**最终立场**：我维持 4/6（Weak Accept），conditioned on Table 6 TBD 实验完成。如果 final DeepSeek CWM 结果显著改变 cross-model narrative（例如 DeepSeek CWM repo-level ≥ 70%，接近 majority baseline），我会降至 3/6。当前的 preliminary "~60" 与论文 narrative 一致，conditional on confirmation。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 136 · 2026-05-18T18:16:29.283299+00:00_

R1 交叉回应已收到。等待 R2 交叉回应。

R1 交叉回应要点：
- 与 R2 在 W1(%%SCENARIO-A%%)、W2(单seed)、W3(preliminary data)、W6(re-repair) 上全部 [AGREE]
- **认同 R2-W5（Oracle ICC 不匹配）为自己两轮审稿均遗漏的有效批评**
- 在 novelty (R2-W4) 上 **[REBUT partially]**：承认 empirical novelty 限制 Main 竞争力，但论证 magnitude 量化（anti-informative parseable outputs）、formulation×model interaction、反直觉消融结果超出"可预期"范畴。维持 4/5，与 R2 (3/5) 差距约 1 分
- 提出将 Contribution 4 拆分为 (4a) 推理效率 trivially true + (4b) 诊断粒度 empirically unvalidated 的建议

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 137 · 2026-05-18T18:16:31.861838+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结核心分歧：

- **与 R2 一致**：W1（SCENARIO-A 标记）、W2（单 seed repo-level）、W3（preliminary data 支撑确定性 claim）、W6（re-repair 负结果低调处理）。
- **新认同**：W5（Oracle ICC 层级不匹配）是 R2 Round 2 的有效新发现，我两轮均未识别。Function-level ICC=0.191 被用于 repo-level oracle 计算，而 repo-level ICC=0.3146 已可用但未用。论文虽声称这是 conservative bound，但方法论上应同时报告两种 ICC 下的结果。
- **核心分歧**：W4（novelty），我维持 Excitement 3/5，R2 为 2.5/5。我的论据：anti-informative parseable predictions、formulation × model interaction、反直觉消融结果超越了单纯 "quantifying expected trend"。但我同意论文 novelty 主要是 empirical，适合 Findings 而非 Main。
- **Score**：维持 4/6（Weak Accept → Findings），R2 为 3/6。差距约 0.5 ARR 分，conditioned on Table 6 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 138 · 2026-05-18T18:16:45.128292+00:00_

R1 交叉回应已收到。等待 R2 交叉回应后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 14

## Round 14

8 recorded events


### User

_source line 139 · 2026-05-18T18:16:45.138149+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 R1 Round 2 的逐条回应

### Strengths
- [AGREE] R1-S1 至 S6 全部同意。Framing 改善（S1）和 DeepSeek 跨模型验证（S2）是最重要的改进。消融实验系统封堵替代解释（S3）直接解决了我 Round 1 最核心的 W3。

### Weaknesses
- [AGREE] R1-W1 [High]: Table 6 TBD 是红旗。Qwen3 TRAJ repo-level 未知引入 asymmetric 风险——若 TRAJ > CLS，论文叙事需重大调整。
- [AGREE] R1-W2 [High]: **R1 独有的重要发现**。DeepSeek CLS 74.93% < TRAJ 75.35±5.00% at repo-level。Contribution 4 的 "diagnostic granularity at equivalent accuracy" 在 DeepSeek repo-level 不成立。C4 scope 实质上缩窄为 "Qwen3 函数级"。论文 Introduction C4 和 Conclusion 的措辞未限定此条件——scope overclaim。
- [AGREE] R1-W3 [Medium-High]: Re-repair 负结果应提升到 main text。Conclusion Future Work 单句提及无实验细节。n=44 power 极低。C4 的 practical motivation 空悬。
- [AGREE] R1-W4 [Medium]: **R1 独有的重要观察**。TRAJ lr 4× 于 CLS/CWM，训练集 ~8K vs 70K。CLS-TRAJ TOST 等价混淆了 formulation effect 和 data volume effect。TRAJ 评估集也不同（1,032 vs 1,890 samples）。CLS 降采样消融是必要的。
- [AGREE] R1-W5 [Medium]: DeepSeek TRAJ ±5pp std 的 95% CI 下界低于 majority baseline，论文未讨论。
- [AGREE] R1-W6 [Low-Medium]: %%SCENARIO-A%% 标记仍可见。

### Questions
- [AGREE] Q1-Q4 全部合理且必要。
- [REBUT] Q5: Table 2 (2 seeds) 和 bootstrap (3-seed superset) 服务不同目的，论文已在 Section 4.3 说明。方向一致，不构成方法论缺陷。

### 分歧论证：R1 的 4/5 vs R2 的 3/5

**我维持 3/5（Findings），低于 R1 的 4/5（Weak Accept），理由：**

1. Table 6 TBD 的 asymmetric 风险 + R1 自己的 W1 识别了这个问题，但评分仍给 4/5——我认为核心表格 TBD 是投稿质量的硬伤。
2. C4 scope 被 W2（DeepSeek CLS≈TRAJ）和 W3（re-repair 负结果）实质性缩窄，从"跨条件的 diagnostic granularity"降为"Qwen3 函数级的 CLS-TRAJ 等价"。
3. C2 跨模型声明依赖 DeepSeek CWM "~60★ preliminary"——preliminary 数字不应支撑 contribution 级声明。

**承认修订版显著改善（从 Round 1 的 2.5 上调到 3/5）**：Framing 不再 overclaim、三组消融封堵替代解释、47 条引用全面覆盖、负结果诚实报告。函数级结果（5 seeds × 2 families × 3 formulations）扎实。

**结论：Findings 级的扎实方法论对比研究，但 TBD + scope 缩窄 + preliminary 数据使其达不到 Conference 门槛。3/5。**

---

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心要点：
- **全部 6 条 Weaknesses [AGREE]**，其中 W2（DeepSeek CLS < TRAJ at repo-level）和 W4（TRAJ 训练配置 confound）是 R1 独有的重要发现
- **唯一 [REBUT]：Q5**，Table 2 和 bootstrap 使用不同 seed 子集是设计选择而非方法论缺陷
- **评分分歧**：维持 3/5（Findings），低于 R1 的 4/5。核心论据：Table 6 TBD 是投稿硬伤、C4 scope 被实际数据大幅缩窄、C2 跨模型声明依赖 preliminary 数据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-18T18:18:26.008163+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "issues:\n# === Round 1 Critical Issues ===\n\n- id: \"R1-N1\"\n  summary: \"Repo-level 核心 claim 基于单 seed，seed 方差极大 (8.3pp)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2。CLS 4B s42=83.63% vs s123=75.33%。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W2 + R1-W1 仍然存在。Abstract 改用 19-26pp 范围（改进），但 Table 6 的 4B-4B 同尺寸对比仍为单 seed。CWM 8B 也是单 seed。信息分布仍然不对称。\"\n  action_items:\n    - round: 1\n      action: \"补充多 seed 同尺寸对比\"\n      assigned_to: \"agent+paper\"\n      status: in_progress\n      progress_note: \"8B-8B 双 seed 已有（s42/s123），但 4B-4B 仍为单 seed。DeepSeek repo 也是部分单 seed。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CWM 8B repo-level 缺失。\"\n    - round: 2\n      reviewers: [1]\n      note: \"CWM 8B 已完成（65.17%, 73.8% unparse, 单 seed）。R1 确认此 issue resolved。\"\n  action_items:\n    - round: 1\n      action: \"CWM 8B repo-level 训练\"\n      assigned_to: \"agent\"\n      status: done\n  resolution: \"CWM 8B 完成。Parseable-only acc 38.52% < 4B 42.88%，进一步支持 formulation bottleneck。\"\n  resolution_round: 2\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"LoRA 低秩约束对 generation 惩罚可能大于 classification。\"\n  action_items:\n    - round: 1\n      action: \"LoRA rank 消融\"\n      assigned_to: \"agent+paper\"\n      status: done\n  resolution: \"rank-32 消融完成 (87.0% vs 87.51%)，排除 capacity bottleneck。两轮 Reviewer 均确认 resolved。\"\n  resolution_round: 1\n\n- id: \"R2-W1\"\n  summary: \"核心贡献新颖性不足以支撑 EMNLP main conference\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2-W1。Excitement R1:3 vs R2:2。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 维持 Excitement 2.5/5，R1 维持 3/5。R1 反驳：anti-informative parseable predictions + formulation×model interaction + 反直觉消融超越'quantifying expected trend'。两人均同意适合 Findings 而非 Main。分歧缩小至 ~0.5 分。\"\n  action_items:\n    - round: 1\n      action: \"Framing pivot + 补充实验\"\n      assigned_to: \"director\"\n      status: done\n      progress_note: \"D116 framing pivot 完成。Design space study framing 获两人正面评价。\"\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 1 Resolved Issues (confirmed Round 2) ===\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Title changed to 'The Formulation Design Space...'. Round 2 S1 正面确认。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R1-W1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正当性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Table added with ±1/±2/±3pp. Round 2 S4 正面确认。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R1-W2\"\n  summary: \"Scaling argument (CWM -0.27pp) 被未调优 hyperparameter 混淆\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"弱化为条件性表述。Round 2 未再提出。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-W3\"\n  summary: \"Val-test mutation type distribution shift\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Appendix Table 9 报告分布。Round 2 S6 确认。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Relaxed matching 反而降低准确率。Round 2 S3 确认为反直觉发现。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R1-W5\"\n  summary: \"人工突变 vs 真实 bug ecological validity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Limitations 增加讨论 + Andrews/Just 引用。Round 2 S6 确认。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R2-W5-r1\"\n  summary: \"Per-test diagnostic granularity 无下游验证\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"无 re-repair 实验。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Pilot re-repair 负结果（n=44, p=0.42）已报告但仅 Future Work 单句。R1-W3 + R2-W6 均要求提升到 main text 并报告实验细节。C4 practical motivation 空悬。\"\n  action_items:\n    - round: 2\n      action: \"提升 re-repair 负结果到 main text Analysis section，报告实验细节，调整 C4 表述\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"遗漏 LEVER 和 CodeT\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已添加。Round 2 S6 确认 47 references 全面覆盖。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R2-W8\"\n  summary: \"引用 first author 不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"全量核查完成。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"resolved\"\n\n# === Round 2 New Issues ===\n\n- id: \"R2-2-W1\"\n  summary: \"%%SCENARIO-A%% 条件编译标记仍可见于源码\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W1 + R1-W6 完全一致。LaTeX %% 注释下内容在 PDF 中不可见，但暗示 work-in-progress。被注释内容可能包含有价值的 robustness 分析（CWM seed sensitivity、checkpoint sensitivity）。提交前必须清理。\"\n  action_items:\n    - round: 2\n      action: \"移除所有 %%SCENARIO-A%% 标记，决定被注释内容是否纳入正文\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-2-W1\"\n  summary: \"Table 6 含 TBD/preliminary 条目，核心结果表不完整\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W1/W3 一致。Qwen3 TRAJ repo-level TBD，DeepSeek CWM '~60 preliminary'。投稿论文核心表格 TBD 是红旗。若 TRAJ > CLS，叙事需重大调整。\"\n  action_items:\n    - round: 2\n      action: \"完成所有 TBD 实验后再提交；若无法完成则在 abstract 明确标注 preliminary\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-2-W2\"\n  summary: \"DeepSeek CLS (74.93%) < TRAJ (75.35±5.00) at repo-level，削弱 C4\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W2，R2 交叉回应 AGREE 称'R1独有的重要发现'。CLS 在 DeepSeek repo-level 不优于 TRAJ，C4 scope 实质缩窄为 'Qwen3 函数级'。论文回避了此比较。\"\n  action_items:\n    - round: 2\n      action: \"Section 4.6 增加 DeepSeek CLS vs TRAJ 明确比较；C4 限定 scope\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-2-W4\"\n  summary: \"TRAJ 训练配置与 CLS/CWM 不完全受控 (lr/data volume)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W4，R2 交叉回应 AGREE 称'R1独有的重要观察'。TRAJ lr=2e-4 vs CLS/CWM 5e-5，训练集 8K vs 70K。TOST 等价混淆了 formulation 和 data volume effect。\"\n  action_items:\n    - round: 2\n      action: \"CLS 降采样到 ~8K 的消融实验，或在 Limitations 明确讨论此 confound\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-2-W5\"\n  summary: \"DeepSeek TRAJ repo-level ±5pp std (6 seeds) 极端不稳定，未分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W5，R2 AGREE。95% CI 跨越 majority baseline。某些 seed 可能低于 majority baseline。未报告逐 seed 准确率。\"\n  action_items:\n    - round: 2\n      action: \"报告 6 seed 逐个准确率，分析方差来源\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-2-W5\"\n  summary: \"Oracle framework 用 function-level ICC (0.191) 应用于 repo-level 分析，ICC 层级不匹配\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W5，R1 交叉回应 AGREE 称'R2 好发现，我两轮均未识别'。Repo-level ICC=0.3146 已可用但未用于 oracle 计算。当前结果 conservative（方向不变），但方法论上是 level-of-analysis 错误。\"\n  action_items:\n    - round: 2\n      action: \"同时报告 function-level 和 repo-level ICC 下的 oracle 结果\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 1 Info Issues (all resolved) ===\n\n- id: \"R1-M1\"\n  summary: \"'Below chance level (50%)' 在不平衡场景下易误解\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修改为 'below random binary chance (50%)'。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-M2\"\n  summary: \"Qwen3 引用了 Qwen2.5 技术报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修正。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-M3\"\n  summary: \"5-seed 混合 bfloat16 和 NF4\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Table 1 caption 已标注。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-M4\"\n  summary: \"Unparseable outputs verdict assignment 未明确\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"method.tex 已明确。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R2-M2\"\n  summary: \"'D088 protocol' 未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已移除。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "issues:\n# === Round 1 Critical Issues ===\n\n- id: \"R1-N1\"\n  summary: \"Repo-level 核心 claim 基于单 seed，seed 方差极大 (8.3pp)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2。CLS 4B s42=83.63% vs s123=75.33%。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W2 + R1-W1 仍然存在。Abstract 改用 19-26pp 范围（改进），但 Table 6 的 4B-4B 同尺寸对比仍为单 seed。CWM 8B 也是单 seed。信息分布仍然不对称。\"\n  action_items:\n    - round: 1\n      action: \"补充多 seed 同尺寸对比\"\n      assigned_to: \"agent+paper\"\n      status: in_progress\n      progress_note: \"8B-8B 双 seed 已有（s42/s123），但 4B-4B 仍为单 seed。DeepSeek repo 也是部分单 seed。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"CWM 8B repo-level 缺失。\"\n    - round: 2\n      reviewers: [1]\n      note: \"CWM 8B 已完成（65.17%, 73.8% unparse, 单 seed）。R1 确认此 issue resolved。\"\n  action_items:\n    - round: 1\n      action: \"CWM 8B repo-level 训练\"\n      assigned_to: \"agent\"\n      status: done\n  resolution: \"CWM 8B 完成。Parseable-only acc 38.52% < 4B 42.88%，进一步支持 formulation bottleneck。\"\n  resolution_round: 2\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"LoRA 低秩约束对 generation 惩罚可能大于 classification。\"\n  action_items:\n    - round: 1\n      action: \"LoRA rank 消融\"\n      assigned_to: \"agent+paper\"\n      status: done\n  resolution: \"rank-32 消融完成 (87.0% vs 87.51%)，排除 capacity bottleneck。两轮 Reviewer 均确认 resolved。\"\n  resolution_round: 1\n\n- id: \"R2-W1\"\n  summary: \"核心贡献新颖性不足以支撑 EMNLP main conference\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2-W1。Excitement R1:3 vs R2:2。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 维持 Excitement 2.5/5，R1 维持 3/5。R1 反驳：anti-informative parseable predictions + formulation×model interaction + 反直觉消融超越'quantifying expected trend'。两人均同意适合 Findings 而非 Main。分歧缩小至 ~0.5 分。\"\n  action_items:\n    - round: 1\n      action: \"Framing pivot + 补充实验\"\n      assigned_to: \"director\"\n      status: done\n      progress_note: \"D116 framing pivot 完成。Design space study framing 获两人正面评价。\"\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 1 Resolved Issues (confirmed Round 2) ===\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Title changed to 'The Formulation Design Space...'. Round 2 S1 正面确认。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R1-W1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正当性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Table added with ±1/±2/±3pp. Round 2 S4 正面确认。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R1-W2\"\n  summary: \"Scaling argument (CWM -0.27pp) 被未调优 hyperparameter 混淆\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"弱化为条件性表述。Round 2 未再提出。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-W3\"\n  summary: \"Val-test mutation type distribution shift\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Appendix Table 9 报告分布。Round 2 S6 确认。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Relaxed matching 反而降低准确率。Round 2 S3 确认为反直觉发现。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R1-W5\"\n  summary: \"人工突变 vs 真实 bug ecological validity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Limitations 增加讨论 + Andrews/Just 引用。Round 2 S6 确认。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R2-W5-r1\"\n  summary: \"Per-test diagnostic granularity 无下游验证\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"无 re-repair 实验。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Pilot re-repair 负结果（n=44, p=0.42）已报告但仅 Future Work 单句。R1-W3 + R2-W6 均要求提升到 main text 并报告实验细节。C4 practical motivation 空悬。\"\n  action_items:\n    - round: 2\n      action: \"提升 re-repair 负结果到 main text Analysis section，报告实验细节，调整 C4 表述\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"遗漏 LEVER 和 CodeT\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已添加。Round 2 S6 确认 47 references 全面覆盖。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\"\n\n- id: \"R2-W8\"\n  summary: \"引用 first author 不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"全量核查完成。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"resolved\"\n\n# === Round 2 New Issues ===\n\n- id: \"R2-2-W1\"\n  summary: \"%%SCENARIO-A%% 条件编译标记仍可见于源码\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W1 + R1-W6 完全一致。LaTeX %% 注释下内容在 PDF 中不可见，但暗示 work-in-progress。被注释内容可能包含有价值的 robustness 分析（CWM seed sensitivity、checkpoint sensitivity）。提交前必须清理。\"\n  action_items:\n    - round: 2\n      action: \"移除所有 %%SCENARIO-A%% 标记，决定被注释内容是否纳入正文\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-2-W1\"\n  summary: \"Table 6 含 TBD/preliminary 条目，核心结果表不完整\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W1/W3 一致。Qwen3 TRAJ repo-level TBD，DeepSeek CWM '~60 preliminary'。投稿论文核心表格 TBD 是红旗。若 TRAJ > CLS，叙事需重大调整。\"\n  action_items:\n    - round: 2\n      action: \"完成所有 TBD 实验后再提交；若无法完成则在 abstract 明确标注 preliminary\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-2-W2\"\n  summary: \"DeepSeek CLS (74.93%) < TRAJ (75.35±5.00) at repo-level，削弱 C4\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W2，R2 交叉回应 AGREE 称'R1独有的重要发现'。CLS 在 DeepSeek repo-level 不优于 TRAJ，C4 scope 实质缩窄为 'Qwen3 函数级'。论文回避了此比较。\"\n  action_items:\n    - round: 2\n      action: \"Section 4.6 增加 DeepSeek CLS vs TRAJ 明确比较；C4 限定 scope\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-2-W4\"\n  summary: \"TRAJ 训练配置与 CLS/CWM 不完全受控 (lr/data volume)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W4，R2 交叉回应 AGREE 称'R1独有的重要观察'。TRAJ lr=2e-4 vs CLS/CWM 5e-5，训练集 8K vs 70K。TOST 等价混淆了 formulation 和 data volume effect。\"\n  action_items:\n    - round: 2\n      action: \"CLS 降采样到 ~8K 的消融实验，或在 Limitations 明确讨论此 confound\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-2-W5\"\n  summary: \"DeepSeek TRAJ repo-level ±5pp std (6 seeds) 极端不稳定，未分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1-W5，R2 AGREE。95% CI 跨越 majority baseline。某些 seed 可能低于 majority baseline。未报告逐 seed 准确率。\"\n  action_items:\n    - round: 2\n      action: \"报告 6 seed 逐个准确率，分析方差来源\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-2-W5\"\n  summary: \"Oracle framework 用 function-level ICC (0.191) 应用于 repo-level 分析，ICC 层级不匹配\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2-W5，R1 交叉回应 AGREE 称'R2 好发现，我两轮均未识别'。Repo-level ICC=0.3146 已可用但未用于 oracle 计算。当前结果 conservative（方向不变），但方法论上是 level-of-analysis 错误。\"\n  action_items:\n    - round: 2\n      action: \"同时报告 function-level 和 repo-level ICC 下的 oracle 结果\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 1 Info Issues (all resolved) ===\n\n- id: \"R1-M1\"\n  summary: \"'Below chance level (50%)' 在不平衡场景下易误解\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修改为 'below random binary chance (50%)'。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-M2\"\n  summary: \"Qwen3 引用了 Qwen2.5 技术报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修正。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-M3\"\n  summary: \"5-seed 混合 bfloat16 和 NF4\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Table 1 caption 已标注。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-M4\"\n  summary: \"Unparseable outputs verdict assignment 未明确\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"method.tex 已明确。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R2-M2\"\n  summary: \"'D088 protocol' 未定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已移除。\"\n  resolution_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"resolved\""
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-18T18:18:26.110191+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 10618}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-18T18:20:20.787383+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "report": "# 审稿报告 — Round 2\n\n**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**截止日期**: 2026-05-25\n**Reviewer**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作）\n**圆桌模式**: Round 2 独立审稿 → Step 2 交叉分享 → Step 3 收敛判定（1 轮收敛）\n\n---\n\n## 修订版 vs Round 1 变化概要\n\n论文从 Round 1 进行了大幅修订：\n- **标题**：从 advocacy (\"Classification Scales Where Generation Stalls\") 改为中性 (\"The Formulation Design Space...\")\n- **新实验**：DeepSeek-Coder 跨模型验证、CWM 8B repo-level、LoRA rank 32 消融、relaxed matching 消融、匹配上下文消融、TOST sensitivity 分析、0-shot/3-shot baselines、re-repair pilot\n- **引用**：26 → 47 条，补充 LEVER/CodeT/Andrews/Just 等\n- **Framing**：从 \"CLS is superior\" 转为 \"formulation × model × complexity interaction\"\n- **Claim 校准**：条件性表述、abstract 用 19-26pp 范围、负结果诚实报告\n\nRound 1 的 17 个 issue 中，**12 个已 resolved**（LoRA rank 消融、relaxed matching、TOST sensitivity、标题、scaling argument、val-test shift、ecological validity、LEVER/CodeT、引用核查、chance level、Qwen3 引用、D088、NF4 标注、unparseable 策略），**3 个仍 in_progress**，**2 个演化为 Round 2 新问题**。\n\n---\n\n## Summary\n\n本文系统比较 execution-free 代码修复验证的三种 formulation（CLS/CWM/TRAJ），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function/repo），使用受控实验设计。核心发现：函数级三种 formulation 近似等效（5 seeds × 2 model families）；仓库级 CWM 大幅退化（19-26pp across configurations），方向 formulation-inherent，幅度 model-contingent。修订版通过消融实验系统封堵了 LoRA capacity、exact matching penalty、input context disparity 三个替代解释，claim 校准程度远优于 Round 1。\n\n---\n\n## Strengths（两轮共识）\n\n**S1. Framing 根本性改善（R1-S1, R2-S1, 共识）。** 从 advocacy 转为中性 design space study。条件性表述、abstract 范围数字、honest negative results。科学姿态与证据强度匹配。\n\n**S2. DeepSeek 跨模型验证是最重要的实质性改进（R1-S2, R2-S2, 共识）。** 函数级 DeepSeek 三 formulation 结果独立确认等价性。Repo-level degradation pattern 跨模型一致方向支持 formulation-inherent claim。从单模型观察提升为初步 generalizable finding。\n\n**S3. 消融实验系统封堵替代解释（R1-S3, R2-S3, 共识）。** LoRA rank 32 排除 capacity bottleneck；relaxed matching 反降 CWM（反直觉）；匹配上下文 98% gap 来自 formulation。三组消融共同收窄因果解释空间。\n\n**S4. TOST sensitivity 分析（R1-S4, R2-S4, 共识）。** 三档 margin (±1/±2/±3pp) + minimum margin 1.63pp，直接回应 Round 1 质疑。\n\n**S5. 负结果诚实报告（R1-S5, R2-S1, 共识）。** Re-repair pilot (n=44, p=0.42) 负结果、majority voting 失败、CWM 8B parseable<4B、relaxed matching 降低 CWM——增强了论文的可信度和信息密度。\n\n**S6. 全面的实验覆盖和报告质量（R1-S6, R2-S6, 共识）。** 47 references、Appendix hyperparameter table、mutation distribution table、0-shot/3-shot baselines、217× throughput benchmark。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**[C1] Table 6 核心结果表含 TBD/preliminary 条目。（R1-W1 + R2-W1/W3, 完全一致）**\nQwen3 TRAJ repo-level 标注 \"TBD\"，DeepSeek CWM repo-level 标注 \"~60 preliminary (training in progress)\"。投稿论文核心表格的 TBD 是审稿红旗。\n- **Asymmetric risk（R1 独到分析）**：如果 Qwen3 TRAJ repo-level 强于 CLS，论文的 contribution ranking 需重大调整——TRAJ 可能是 repo-level 更好选择。\n- **Preliminary data 支撑确定性 claim**：Section 4.6 写 \"confirms formulation-inherent divergence\"，但 DeepSeek CWM 数据标注 \"final values pending\"。\n- **要求**：完成所有 TBD 实验后再提交。若 deadline 前无法完成，在 abstract 和 Table caption 中系统标注每条数据的 seed 数和 final/preliminary 状态。\n\n**[C2] DeepSeek CLS (74.93%) ≤ TRAJ (75.35±5.00) at repo-level，Contribution 4 scope 实质性缩窄。（R1-W2, R2 AGREE \"R1独有重要发现\"）**\n论文 C4 声称 \"per-test diagnostic granularity at equivalent trajectory-level accuracy\"。但 DeepSeek repo-level 数据显示 CLS 不优于 TRAJ（甚至略低），直接矛盾该 claim。论文回避了 CLS vs TRAJ 在 DeepSeek repo-level 的比较。\n- C4 scope 从 \"跨条件通用\" 实质缩窄为 \"Qwen3 函数级\"。\n- 叠加 re-repair 负结果（C3），per-test granularity 的实际价值很薄。\n- **要求**：Section 4.6 增加 DeepSeek CLS vs TRAJ 明确比较；C4 限定适用范围。\n\n**[C3] Re-repair 负结果 (n=44, p=0.42) 被低调处理，但实质削弱 C4 的下游 utility motivation。（R1-W3 + R2-W6, 完全一致）**\nIntroduction 多次以 \"targeted re-repair\" 作为 per-test granularity 的 motivation，但 pilot 负结果仅在 Conclusion Future Work 单句提及，无实验细节。\n- C4 当前将 trivially true 的 throughput claim (217×) 和 empirically unvalidated 的 utility claim 混合在同一 contribution 中。\n- **要求**：(1) 提升 re-repair 负结果到 main text Analysis section，报告实验细节（repair agent、feedback format、n=44 power analysis）；(2) C4 拆分为 efficiency (formulation-inherent) 和 diagnostic utility (unvalidated)。\n\n**[C4] 单 seed repo-level 同尺寸对比仍未实质解决。（Round 1 遗留，R1+R2 一致）**\nAbstract 改用 19-26pp 范围（改进），但 Table 6 中 Qwen3 4B-4B 仍为单 seed (s42)。CLS 4B s123=75.33% 仅在 Limitations 披露不出现在 Table 6——信息分布不对称从 Round 1 到 Round 2 未改善。CWM 8B 也是单 seed。\n\n### Warning（应修复但不一票否决）\n\n**[W1] TRAJ 训练配置与 CLS/CWM 不完全受控。（R1-W4, R2 AGREE \"R1独有重要观察\"）**\nTRAJ lr=2×10⁻⁴（CLS/CWM 5×10⁻⁵），训练集 ~8K（CLS/CWM 70K）。CLS-TRAJ TOST 等价混淆了 formulation effect 和 data volume effect。如果 TRAJ 有更多数据，其准确率可能高于 86.30%，改变等价性结论。建议 CLS 降采样到 ~8K 的消融。\n\n**[W2] DeepSeek TRAJ repo-level ±5pp std (6 seeds) 极端不稳定。（R1-W5, R2 AGREE）**\n95% CI 约 [65, 86]，跨越 majority baseline (72.96%)。某些 seed 可能低于 majority baseline。论文未分析方差来源（训练发散？checkpoint selection？）。应报告逐 seed 准确率。\n\n**[W3] Oracle framework ICC 层级不匹配。（R2-W5, R1 AGREE \"好发现，我两轮未识别\"）**\nOracle accuracy-utility frontier 使用 function-level ICC=0.191，但 repo-level ICC=0.3146 已可用。虽然结果方向不变（repo-level ICC 更大 → advantage 更大，当前估计 conservative），但方法论上是 level-of-analysis 错误。应同时报告两种 ICC 下的 oracle 结果。\n\n**[W4] %%SCENARIO-A%% 条件编译标记未清理。（R1-W6 + R2-W1, 完全一致）**\nabstract/intro/experiments/conclusion 中可见。标准 LaTeX 下为注释不影响 PDF，但暗示 work-in-progress。被注释内容可能包含有价值的 robustness 分析。提交前必须清理。\n\n---\n\n## Reviewer Consensus（[AGREE] 项）\n\nRound 2 交叉分享中，两位 Reviewer 在以下评审点上达成一致：\n- **所有 Strengths** (S1-S6)\n- **所有 Weaknesses**：Table 6 TBD (C1)、DeepSeek CLS≈TRAJ (C2)、re-repair 负结果 (C3)、单 seed (C4)、TRAJ confound (W1)、DeepSeek TRAJ 方差 (W2)、Oracle ICC (W3)、SCENARIO-A (W4)\n- R1 新提出的 W2（DeepSeek CLS≈TRAJ）和 W4（TRAJ confound）：R2 均 AGREE 并称 \"R1独有的重要发现/观察\"\n- R2 新提出的 W5（Oracle ICC 不匹配）：R1 AGREE 并称 \"好发现，我两轮均未识别\"\n\n---\n\n## Reviewer Divergence\n\n**唯一实质分歧：Overall Score 和 Novelty**\n\n| | R1 Round 2 | R2 Round 2 |\n|---|---|---|\n| Soundness | ~3.5/5 | 3.5/5 |\n| Excitement | 3/5 | 2.5/5 |\n| Overall | **4/5 (Weak Accept)** | **3/5 (borderline)** |\n\n**分歧根源**：R1 认为 conditional on TBD 完成可 Findings accept（anti-informative parseable predictions + formulation×model interaction + 反直觉消融超越 \"expected trend\"）。R2 认为 Table 6 TBD 是投稿硬伤 + C4 scope 被实际数据大幅缩窄。\n\n**Director 判断**：两位 Reviewer 均推荐 **Findings track**。分歧在于 \"当前状态 conditional accept\" (R1) vs \"需完成后才达标\" (R2)。综合 R1 的 conditional 和 R2 的 concern，实质差距约 0.5 ARR 分。\n\n---\n\n## Questions（汇总）\n\n1. DeepSeek TRAJ 6 seeds 逐个准确率？±5pp 中是否有 seed < majority baseline？方差来源？（R1-Q1）\n2. DeepSeek CLS (74.93%) < TRAJ (75.35%)，C4 scope 如何限定？（R1-Q2, R2 AGREE）\n3. Re-repair pilot 实验设计细节：repair agent、feedback format、n=44 power analysis？（R1-Q3, R2-Q3）\n4. CLS/CWM 降采样到 ~8K 的准确率？（R1-Q4）\n5. Table 2 scaling 的 2 matched seeds vs bootstrap 3-seed superset 是否一致？（R1-Q5, R2 REBUT 认为不构成缺陷）\n6. %%SCENARIO-A%% 标记在 PDF 中是否可见？被注释内容是否应纳入？（R2-Q1）\n7. DeepSeek CWM final results 何时完成？（R2-Q2）\n8. CWM 8B parseable acc < 4B 是否 Qwen3-specific？（R2-Q4）\n9. ICC=0.191 是否在 DeepSeek 上复现？（R2-Q5）\n\n---\n\n## Round 1 → Round 2 Issue Resolution 追踪\n\n| Round 1 Issue | Status | 说明 |\n|---|---|---|\n| R1-N1 单 seed | **in_progress** | Abstract 改用范围（改进），Table 6 仍单 seed |\n| R1-N2 CWM 8B 缺失 | **resolved** | CWM 8B 完成 (65.17%, 73.8% unparse) |\n| R1-N3 LoRA rank | **resolved** | rank-32 消融排除 capacity bottleneck |\n| R2-W1 novelty | **in_progress** | Framing pivot 获正面评价，但 novelty 仍有争议 |\n| R2-W4 标题 \"scales\" | **resolved** | 新标题获正面评价 |\n| R1-W1 TOST margin | **resolved** | 三档 sensitivity + justification |\n| R1-W2 scaling argument | **resolved** | 弱化为条件性表述 |\n| R1-W3 val-test shift | **resolved** | Appendix Table 9 |\n| R1-W4 relaxed matching | **resolved** | 反直觉：relaxed 降低 CWM |\n| R1-W5 ecological validity | **resolved** | Limitations + Andrews/Just 引用 |\n| R2-W5 re-repair 无验证 | **in_progress** → **Round 2 C3** | Pilot 负结果存在但报告不充分 |\n| R2-W6 LEVER/CodeT | **resolved** | 已添加 |\n| R2-W8 引用不一致 | **resolved** | 全量核查完成 |\n| All 5 Info issues | **resolved** | 全部修正 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: Borderline（ARR 3 / Findings borderline）**\n**对应 ARR 评分：R1 给 3.5（Borderline Conference），R2 给 2.5-3（Borderline Findings）。综合 ≈ 3（Findings）。**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | ~3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 3/5 | 2.5/5 | **2.75/5** |\n| Overall | 4/5 | 3/5 | **3.5/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 从 Round 1 到 Round 2 的评分变化\n\n| | Round 1 | Round 2 | 变化 |\n|---|---|---|---|\n| R1 Overall | 2.5/5 | 4/5 | **+1.5** |\n| R2 Overall | 2.5/5 | 3/5 | **+0.5** |\n| 综合 | 2.5/5 | 3.5/5 | **+1.0** |\n\n### 核心判断\n\n**修订版在方法论严谨性上有实质性进步**。Round 1 的 3 个 critical issue 中 1 个 fully resolved（LoRA rank 消融），1 个 partially resolved（CWM 8B 完成但仍单 seed），1 个 partially addressed（novelty concern 通过 framing pivot 改善但未消除）。消融实验、跨模型验证、TOST sensitivity、负结果报告共同将 Soundness 从 2.5 提升到 3.5。\n\n**当前仍存在的核心障碍**：\n\n1. **Table 6 不完整**：核心结果表含 TBD 和 preliminary 数据，是投稿质量问题。需完成后再提交。\n2. **C4 (diagnostic granularity) 证据基础薄弱**：DeepSeek CLS ≤ TRAJ at repo-level + re-repair 负结果 + oracle ICC 层级不匹配，三者叠加使 C4 的 scope 大幅缩窄。\n3. **Novelty 仍有争议**：两位 Reviewer 均同意 Findings 级别，但对是否 solid Findings vs borderline Findings 有 ~0.5 分分歧。\n\n### 建议路径\n\n- **推荐路径**：完成 Table 6 全部 TBD 实验 → 根据 TRAJ repo-level 结果调整 C4 scope → 提升 re-repair 负结果到 main text → 清理 SCENARIO-A 标记 → 投 ARR May cycle（Findings track）。\n- **如果 Qwen3 TRAJ repo-level > CLS**：需重构 C4 叙事——从 \"CLS provides equivalent accuracy + diagnostic granularity\" 转为 \"formulation choice is context-dependent: CLS for function-level diagnostic, TRAJ for repo-level robustness\"。\n- **不建议**：当前状态（含 TBD）直接提交。\n\n---\n\n*圆桌审稿 Round 2 完成。论文从 Round 1 的 Weak Reject (2.5/5) 改善为 Borderline Findings (3-3.5/5)。两位 Reviewer 经交叉分享后在所有 weakness 上达成共识，唯一分歧为 novelty threshold (~0.5 分)。Issue Tracker 已同步更新。*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "report": "# 审稿报告 — Round 2\n\n**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**截止日期**: 2026-05-25\n**Reviewer**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作）\n**圆桌模式**: Round 2 独立审稿 → Step 2 交叉分享 → Step 3 收敛判定（1 轮收敛）\n\n---\n\n## 修订版 vs Round 1 变化概要\n\n论文从 Round 1 进行了大幅修订：\n- **标题**：从 advocacy (\"Classification Scales Where Generation Stalls\") 改为中性 (\"The Formulation Design Space...\")\n- **新实验**：DeepSeek-Coder 跨模型验证、CWM 8B repo-level、LoRA rank 32 消融、relaxed matching 消融、匹配上下文消融、TOST sensitivity 分析、0-shot/3-shot baselines、re-repair pilot\n- **引用**：26 → 47 条，补充 LEVER/CodeT/Andrews/Just 等\n- **Framing**：从 \"CLS is superior\" 转为 \"formulation × model × complexity interaction\"\n- **Claim 校准**：条件性表述、abstract 用 19-26pp 范围、负结果诚实报告\n\nRound 1 的 17 个 issue 中，**12 个已 resolved**（LoRA rank 消融、relaxed matching、TOST sensitivity、标题、scaling argument、val-test shift、ecological validity、LEVER/CodeT、引用核查、chance level、Qwen3 引用、D088、NF4 标注、unparseable 策略），**3 个仍 in_progress**，**2 个演化为 Round 2 新问题**。\n\n---\n\n## Summary\n\n本文系统比较 execution-free 代码修复验证的三种 formulation（CLS/CWM/TRAJ），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function/repo），使用受控实验设计。核心发现：函数级三种 formulation 近似等效（5 seeds × 2 model families）；仓库级 CWM 大幅退化（19-26pp across configurations），方向 formulation-inherent，幅度 model-contingent。修订版通过消融实验系统封堵了 LoRA capacity、exact matching penalty、input context disparity 三个替代解释，claim 校准程度远优于 Round 1。\n\n---\n\n## Strengths（两轮共识）\n\n**S1. Framing 根本性改善（R1-S1, R2-S1, 共识）。** 从 advocacy 转为中性 design space study。条件性表述、abstract 范围数字、honest negative results。科学姿态与证据强度匹配。\n\n**S2. DeepSeek 跨模型验证是最重要的实质性改进（R1-S2, R2-S2, 共识）。** 函数级 DeepSeek 三 formulation 结果独立确认等价性。Repo-level degradation pattern 跨模型一致方向支持 formulation-inherent claim。从单模型观察提升为初步 generalizable finding。\n\n**S3. 消融实验系统封堵替代解释（R1-S3, R2-S3, 共识）。** LoRA rank 32 排除 capacity bottleneck；relaxed matching 反降 CWM（反直觉）；匹配上下文 98% gap 来自 formulation。三组消融共同收窄因果解释空间。\n\n**S4. TOST sensitivity 分析（R1-S4, R2-S4, 共识）。** 三档 margin (±1/±2/±3pp) + minimum margin 1.63pp，直接回应 Round 1 质疑。\n\n**S5. 负结果诚实报告（R1-S5, R2-S1, 共识）。** Re-repair pilot (n=44, p=0.42) 负结果、majority voting 失败、CWM 8B parseable<4B、relaxed matching 降低 CWM——增强了论文的可信度和信息密度。\n\n**S6. 全面的实验覆盖和报告质量（R1-S6, R2-S6, 共识）。** 47 references、Appendix hyperparameter table、mutation distribution table、0-shot/3-shot baselines、217× throughput benchmark。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**[C1] Table 6 核心结果表含 TBD/preliminary 条目。（R1-W1 + R2-W1/W3, 完全一致）**\nQwen3 TRAJ repo-level 标注 \"TBD\"，DeepSeek CWM repo-level 标注 \"~60 preliminary (training in progress)\"。投稿论文核心表格的 TBD 是审稿红旗。\n- **Asymmetric risk（R1 独到分析）**：如果 Qwen3 TRAJ repo-level 强于 CLS，论文的 contribution ranking 需重大调整——TRAJ 可能是 repo-level 更好选择。\n- **Preliminary data 支撑确定性 claim**：Section 4.6 写 \"confirms formulation-inherent divergence\"，但 DeepSeek CWM 数据标注 \"final values pending\"。\n- **要求**：完成所有 TBD 实验后再提交。若 deadline 前无法完成，在 abstract 和 Table caption 中系统标注每条数据的 seed 数和 final/preliminary 状态。\n\n**[C2] DeepSeek CLS (74.93%) ≤ TRAJ (75.35±5.00) at repo-level，Contribution 4 scope 实质性缩窄。（R1-W2, R2 AGREE \"R1独有重要发现\"）**\n论文 C4 声称 \"per-test diagnostic granularity at equivalent trajectory-level accuracy\"。但 DeepSeek repo-level 数据显示 CLS 不优于 TRAJ（甚至略低），直接矛盾该 claim。论文回避了 CLS vs TRAJ 在 DeepSeek repo-level 的比较。\n- C4 scope 从 \"跨条件通用\" 实质缩窄为 \"Qwen3 函数级\"。\n- 叠加 re-repair 负结果（C3），per-test granularity 的实际价值很薄。\n- **要求**：Section 4.6 增加 DeepSeek CLS vs TRAJ 明确比较；C4 限定适用范围。\n\n**[C3] Re-repair 负结果 (n=44, p=0.42) 被低调处理，但实质削弱 C4 的下游 utility motivation。（R1-W3 + R2-W6, 完全一致）**\nIntroduction 多次以 \"targeted re-repair\" 作为 per-test granularity 的 motivation，但 pilot 负结果仅在 Conclusion Future Work 单句提及，无实验细节。\n- C4 当前将 trivially true 的 throughput claim (217×) 和 empirically unvalidated 的 utility claim 混合在同一 contribution 中。\n- **要求**：(1) 提升 re-repair 负结果到 main text Analysis section，报告实验细节（repair agent、feedback format、n=44 power analysis）；(2) C4 拆分为 efficiency (formulation-inherent) 和 diagnostic utility (unvalidated)。\n\n**[C4] 单 seed repo-level 同尺寸对比仍未实质解决。（Round 1 遗留，R1+R2 一致）**\nAbstract 改用 19-26pp 范围（改进），但 Table 6 中 Qwen3 4B-4B 仍为单 seed (s42)。CLS 4B s123=75.33% 仅在 Limitations 披露不出现在 Table 6——信息分布不对称从 Round 1 到 Round 2 未改善。CWM 8B 也是单 seed。\n\n### Warning（应修复但不一票否决）\n\n**[W1] TRAJ 训练配置与 CLS/CWM 不完全受控。（R1-W4, R2 AGREE \"R1独有重要观察\"）**\nTRAJ lr=2×10⁻⁴（CLS/CWM 5×10⁻⁵），训练集 ~8K（CLS/CWM 70K）。CLS-TRAJ TOST 等价混淆了 formulation effect 和 data volume effect。如果 TRAJ 有更多数据，其准确率可能高于 86.30%，改变等价性结论。建议 CLS 降采样到 ~8K 的消融。\n\n**[W2] DeepSeek TRAJ repo-level ±5pp std (6 seeds) 极端不稳定。（R1-W5, R2 AGREE）**\n95% CI 约 [65, 86]，跨越 majority baseline (72.96%)。某些 seed 可能低于 majority baseline。论文未分析方差来源（训练发散？checkpoint selection？）。应报告逐 seed 准确率。\n\n**[W3] Oracle framework ICC 层级不匹配。（R2-W5, R1 AGREE \"好发现，我两轮未识别\"）**\nOracle accuracy-utility frontier 使用 function-level ICC=0.191，但 repo-level ICC=0.3146 已可用。虽然结果方向不变（repo-level ICC 更大 → advantage 更大，当前估计 conservative），但方法论上是 level-of-analysis 错误。应同时报告两种 ICC 下的 oracle 结果。\n\n**[W4] %%SCENARIO-A%% 条件编译标记未清理。（R1-W6 + R2-W1, 完全一致）**\nabstract/intro/experiments/conclusion 中可见。标准 LaTeX 下为注释不影响 PDF，但暗示 work-in-progress。被注释内容可能包含有价值的 robustness 分析。提交前必须清理。\n\n---\n\n## Reviewer Consensus（[AGREE] 项）\n\nRound 2 交叉分享中，两位 Reviewer 在以下评审点上达成一致：\n- **所有 Strengths** (S1-S6)\n- **所有 Weaknesses**：Table 6 TBD (C1)、DeepSeek CLS≈TRAJ (C2)、re-repair 负结果 (C3)、单 seed (C4)、TRAJ confound (W1)、DeepSeek TRAJ 方差 (W2)、Oracle ICC (W3)、SCENARIO-A (W4)\n- R1 新提出的 W2（DeepSeek CLS≈TRAJ）和 W4（TRAJ confound）：R2 均 AGREE 并称 \"R1独有的重要发现/观察\"\n- R2 新提出的 W5（Oracle ICC 不匹配）：R1 AGREE 并称 \"好发现，我两轮均未识别\"\n\n---\n\n## Reviewer Divergence\n\n**唯一实质分歧：Overall Score 和 Novelty**\n\n| | R1 Round 2 | R2 Round 2 |\n|---|---|---|\n| Soundness | ~3.5/5 | 3.5/5 |\n| Excitement | 3/5 | 2.5/5 |\n| Overall | **4/5 (Weak Accept)** | **3/5 (borderline)** |\n\n**分歧根源**：R1 认为 conditional on TBD 完成可 Findings accept（anti-informative parseable predictions + formulation×model interaction + 反直觉消融超越 \"expected trend\"）。R2 认为 Table 6 TBD 是投稿硬伤 + C4 scope 被实际数据大幅缩窄。\n\n**Director 判断**：两位 Reviewer 均推荐 **Findings track**。分歧在于 \"当前状态 conditional accept\" (R1) vs \"需完成后才达标\" (R2)。综合 R1 的 conditional 和 R2 的 concern，实质差距约 0.5 ARR 分。\n\n---\n\n## Questions（汇总）\n\n1. DeepSeek TRAJ 6 seeds 逐个准确率？±5pp 中是否有 seed < majority baseline？方差来源？（R1-Q1）\n2. DeepSeek CLS (74.93%) < TRAJ (75.35%)，C4 scope 如何限定？（R1-Q2, R2 AGREE）\n3. Re-repair pilot 实验设计细节：repair agent、feedback format、n=44 power analysis？（R1-Q3, R2-Q3）\n4. CLS/CWM 降采样到 ~8K 的准确率？（R1-Q4）\n5. Table 2 scaling 的 2 matched seeds vs bootstrap 3-seed superset 是否一致？（R1-Q5, R2 REBUT 认为不构成缺陷）\n6. %%SCENARIO-A%% 标记在 PDF 中是否可见？被注释内容是否应纳入？（R2-Q1）\n7. DeepSeek CWM final results 何时完成？（R2-Q2）\n8. CWM 8B parseable acc < 4B 是否 Qwen3-specific？（R2-Q4）\n9. ICC=0.191 是否在 DeepSeek 上复现？（R2-Q5）\n\n---\n\n## Round 1 → Round 2 Issue Resolution 追踪\n\n| Round 1 Issue | Status | 说明 |\n|---|---|---|\n| R1-N1 单 seed | **in_progress** | Abstract 改用范围（改进），Table 6 仍单 seed |\n| R1-N2 CWM 8B 缺失 | **resolved** | CWM 8B 完成 (65.17%, 73.8% unparse) |\n| R1-N3 LoRA rank | **resolved** | rank-32 消融排除 capacity bottleneck |\n| R2-W1 novelty | **in_progress** | Framing pivot 获正面评价，但 novelty 仍有争议 |\n| R2-W4 标题 \"scales\" | **resolved** | 新标题获正面评价 |\n| R1-W1 TOST margin | **resolved** | 三档 sensitivity + justification |\n| R1-W2 scaling argument | **resolved** | 弱化为条件性表述 |\n| R1-W3 val-test shift | **resolved** | Appendix Table 9 |\n| R1-W4 relaxed matching | **resolved** | 反直觉：relaxed 降低 CWM |\n| R1-W5 ecological validity | **resolved** | Limitations + Andrews/Just 引用 |\n| R2-W5 re-repair 无验证 | **in_progress** → **Round 2 C3** | Pilot 负结果存在但报告不充分 |\n| R2-W6 LEVER/CodeT | **resolved** | 已添加 |\n| R2-W8 引用不一致 | **resolved** | 全量核查完成 |\n| All 5 Info issues | **resolved** | 全部修正 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: Borderline（ARR 3 / Findings borderline）**\n**对应 ARR 评分：R1 给 3.5（Borderline Conference），R2 给 2.5-3（Borderline Findings）。综合 ≈ 3（Findings）。**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | ~3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 3/5 | 2.5/5 | **2.75/5** |\n| Overall | 4/5 | 3/5 | **3.5/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 从 Round 1 到 Round 2 的评分变化\n\n| | Round 1 | Round 2 | 变化 |\n|---|---|---|---|\n| R1 Overall | 2.5/5 | 4/5 | **+1.5** |\n| R2 Overall | 2.5/5 | 3/5 | **+0.5** |\n| 综合 | 2.5/5 | 3.5/5 | **+1.0** |\n\n### 核心判断\n\n**修订版在方法论严谨性上有实质性进步**。Round 1 的 3 个 critical issue 中 1 个 fully resolved（LoRA rank 消融），1 个 partially resolved（CWM 8B 完成但仍单 seed），1 个 partially addressed（novelty concern 通过 framing pivot 改善但未消除）。消融实验、跨模型验证、TOST sensitivity、负结果报告共同将 Soundness 从 2.5 提升到 3.5。\n\n**当前仍存在的核心障碍**：\n\n1. **Table 6 不完整**：核心结果表含 TBD 和 preliminary 数据，是投稿质量问题。需完成后再提交。\n2. **C4 (diagnostic granularity) 证据基础薄弱**：DeepSeek CLS ≤ TRAJ at repo-level + re-repair 负结果 + oracle ICC 层级不匹配，三者叠加使 C4 的 scope 大幅缩窄。\n3. **Novelty 仍有争议**：两位 Reviewer 均同意 Findings 级别，但对是否 solid Findings vs borderline Findings 有 ~0.5 分分歧。\n\n### 建议路径\n\n- **推荐路径**：完成 Table 6 全部 TBD 实验 → 根据 TRAJ repo-level 结果调整 C4 scope → 提升 re-repair 负结果到 main text → 清理 SCENARIO-A 标记 → 投 ARR May cycle（Findings track）。\n- **如果 Qwen3 TRAJ repo-level > CLS**：需重构 C4 叙事——从 \"CLS provides equivalent accuracy + diagnostic granularity\" 转为 \"formulation choice is context-dependent: CLS for function-level diagnostic, TRAJ for repo-level robustness\"。\n- **不建议**：当前状态（含 TBD）直接提交。\n\n---\n\n*圆桌审稿 Round 2 完成。论文从 Round 1 的 Weak Reject (2.5/5) 改善为 Borderline Findings (3-3.5/5)。两位 Reviewer 经交叉分享后在所有 weakness 上达成共识，唯一分歧为 novelty threshold (~0.5 分)。Issue Tracker 已同步更新。*"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-18T18:20:20.838315+00:00_

{"result":"{\"success\": false, \"data\": {\"existing_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_1.md\", \"round\": 1}, \"error\": \"Round 1 report ALREADY submitted (persisted at `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_1.md`). Research Director was triggered once and may still be processing it; re-submitting silently would trigger the protocol again with conflicting content.\\n\\nExisting report frontmatter (first 400 chars):\\n---\\nround: 1\\noverall_score: weak reject\\ntimestamp: 2026-05-15T11:50:58.862629+00:00\\nreviewer_ids: [1, 2]\\ncross_response_reviewer_ids: [1, 2]\\nforce_resubmit: False\\n---\\n\\n# 审稿报告 — Round 1\\n\\n**论文**: Classification Scales Where Generation Stalls: Reformulating Execution Simulation for Code Repair Verification\\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\\n**截止日期**: 2026-05-25\\n**Reviewer**: R1（\\n\\nIf you intentionally want to replace it (e.g. caught a Step 2 cross-sharing gap and synthesized a corrected report), call again with force_resubmit=True. Otherwise the original submission stands — pause and verify before forcing.\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-18T18:22:14.427115+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "force_resubmit": "True",
  "report": "# 审稿报告 — Round 2（修订版论文）\n\n**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**截止日期**: 2026-05-25\n**Reviewer**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作）\n**圆桌模式**: Round 2 独立审稿 → Step 2 交叉分享 → Step 3 收敛判定（1 轮收敛）\n**注意**: 本报告覆盖修订版论文，是对 Round 1 报告（Overall 2.5/5 Weak Reject）的更新。\n\n---\n\n## 修订版 vs Round 1 变化概要\n\n论文从 Round 1 进行了大幅修订：\n- **标题**：从 advocacy (\"Classification Scales Where Generation Stalls\") 改为中性 (\"The Formulation Design Space...\")\n- **新实验**：DeepSeek-Coder 跨模型验证、CWM 8B repo-level (65.17%)、LoRA rank 32 消融、relaxed matching 消融（反直觉降低 CWM）、匹配上下文消融（98% gap 来自 formulation）、TOST sensitivity 分析（±1/±2/±3pp）、0-shot/3-shot baselines、re-repair pilot (n=44, p=0.42 负结果)\n- **引用**：26 → 47 条，补充 LEVER/CodeT/Andrews/Just 等\n- **Framing**：从 \"CLS is superior\" 转为 \"formulation × model × complexity interaction\"\n- **Claim 校准**：条件性表述、abstract 用 19-26pp 范围、负结果诚实报告\n\nRound 1 的 17 个 issue 中 **12 个已 resolved**，3 个 in_progress，2 个演化为 Round 2 新问题。\n\n---\n\n## Summary\n\n本文系统比较 execution-free 代码修复验证的三种 formulation（CLS/CWM/TRAJ），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function/repo），使用受控实验设计。核心发现：函数级三种 formulation 近似等效（5 seeds × 2 model families）；仓库级 CWM 大幅退化（19-26pp），方向 formulation-inherent，幅度 model-contingent。修订版通过消融实验系统封堵了 LoRA capacity、exact matching penalty、input context disparity 三个替代解释。\n\n---\n\n## Strengths（Round 2 共识）\n\n**S1. Framing 根本性改善（R1-S1, R2-S1, 共识）。** 从 advocacy 转为中性 design space study。每个 claim 以条件性表述限定范围。Abstract 用 \"19-26pp\" 范围替代单点 \"25.59pp\"。科学姿态与证据强度匹配。\n\n**S2. DeepSeek 跨模型验证——最重要的实质性改进（R1-S2, R2-S2, 共识）。** Table 1 中 DeepSeek-Coder-6.7B 的三 formulation 结果独立确认函数级等价性。Repo-level degradation pattern 跨模型一致方向（CWM 退化）支持 \"formulation-inherent direction, model-contingent magnitude\"。从单模型观察提升为初步 generalizable finding。\n\n**S3. 消融实验系统封堵替代解释（R1-S3, R2-S3, 共识）。** (1) LoRA rank 32 排除 capacity bottleneck；(2) Relaxed matching 反降 CWM 准确率（反直觉，排除 exact match penalty）；(3) 匹配上下文消融 98% gap 来自 formulation（排除 input context disparity）。三组消融共同收窄因果解释空间。\n\n**S4. TOST sensitivity 分析（R1-S4, R2-S4, 共识）。** 三档 margin (±1/±2/±3pp) + minimum margin 1.63pp + deployment-significance 论证。直接回应 Round 1 质疑。\n\n**S5. 负结果诚实报告（R1-S5, R2-S1, 共识）。** Re-repair pilot 负结果、majority voting 失败、CWM 8B parseable<4B、relaxed matching 更差。增强论文可信度和信息密度。\n\n**S6. 全面覆盖和报告质量（R1-S6, R2-S6, 共识）。** 47 references、Appendix hyperparameter/mutation distribution tables、0-shot/3-shot baselines、217× throughput benchmark。Reproducibility 显著提高。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**[C1] Table 6 核心结果表含 TBD/preliminary 条目。（R1-W1 + R2-W1/W3, 完全一致）**\nQwen3 TRAJ repo-level \"TBD\"，DeepSeek CWM \"~60 preliminary\"。投稿论文核心表格的 TBD 是审稿红旗。\n- **Asymmetric risk**：若 Qwen3 TRAJ repo-level 强于 CLS（如 DeepSeek TRAJ 75.35% > CLS 74.93%），论文 contribution ranking 需重大调整。\n- **Preliminary → 确定性 claim**：Section 4.6 用 \"confirms formulation-inherent divergence\" 修饰 preliminary data。\n- **要求**：完成所有 TBD 实验后再提交。若 deadline 前无法完成，在 abstract 和 Table caption 系统标注 final/preliminary 状态。\n\n**[C2] DeepSeek CLS (74.93%) ≤ TRAJ (75.35±5.00) at repo-level，Contribution 4 scope 实质缩窄。（R1-W2, R2 AGREE \"R1独有重要发现\"）**\nC4 声称 \"per-test diagnostic granularity at equivalent trajectory-level accuracy\"。但 DeepSeek repo-level 显示 CLS 不优于 TRAJ（甚至略低）。论文回避了此比较。\n- C4 scope 从 \"跨条件通用\" 缩窄为 \"Qwen3 函数级\"。\n- 叠加 re-repair 负结果 (C3)，per-test granularity 实际价值薄弱。\n- **要求**：(1) Section 4.6 增加 DeepSeek CLS vs TRAJ 明确比较和讨论；(2) C4 限定适用范围。\n\n**[C3] Re-repair 负结果 (n=44, p=0.42) 低调处理，实质削弱 C4 下游 utility。（R1-W3 + R2-W6, 完全一致）**\nIntroduction 多次以 \"targeted re-repair\" 作为 motivation，但 pilot 负结果仅 Conclusion Future Work 单句。C4 混合 trivially true 的 throughput claim (217×) 和 unvalidated 的 utility claim。\n- **要求**：(1) 提升负结果到 main text，报告实验细节（agent、format、power analysis）；(2) C4 拆分为 efficiency (formulation-inherent) 和 diagnostic utility (unvalidated)。\n\n**[C4] 单 seed repo-level 同尺寸对比仍未实质解决。（Round 1 遗留, R1+R2 一致）**\nAbstract 改用 19-26pp 范围（改进），但 Table 6 中 Qwen3 4B-4B 仍为 seed 42 单点。CLS 4B s123=75.33% 仅在 Limitations 披露。CWM 8B 也是单 seed。从 Round 1 到 Round 2 此问题未实质改善。\n\n### Warning（应修复）\n\n**[W1] TRAJ 训练配置与 CLS/CWM 不完全受控。（R1-W4, R2 AGREE \"R1独有重要观察\"）**\nTRAJ lr=2×10⁻⁴ (CLS/CWM 5×10⁻⁵)，训练集 ~8K (CLS/CWM 70K)。CLS-TRAJ TOST 等价混淆 formulation effect 和 data volume effect。建议 CLS 降采样 ~8K 消融。\n\n**[W2] DeepSeek TRAJ repo-level ±5pp std (6 seeds) 极端不稳定。（R1-W5, R2 AGREE）**\n95% CI 约 [65,86]，跨越 majority baseline (72.96%)。未报告逐 seed 准确率，未分析方差来源。\n\n**[W3] Oracle ICC 层级不匹配。（R2-W5, R1 AGREE \"好发现，两轮未识别\"）**\nOracle frontier 使用 function-level ICC=0.191，但 repo-level ICC=0.3146 已可用未用。当前估计 conservative（方向不变），但方法论上是 level-of-analysis 错误。应同时报告两种 ICC 下的 oracle 结果。\n\n**[W4] %%SCENARIO-A%% 条件标记未清理。（R1-W6 + R2-W1, 完全一致）**\nabstract/intro/experiments/conclusion 中可见。标准 LaTeX 下为注释不影响 PDF，但暗示 work-in-progress。被注释内容可能包含有价值的 robustness 分析。提交前必须清理。\n\n---\n\n## Reviewer Consensus\n\nRound 2 交叉分享中两位 Reviewer 在所有 Weakness 上达成一致。关键新发现：\n- R1 新提出 C2（DeepSeek CLS≈TRAJ）和 W1（TRAJ confound）：R2 均 AGREE\n- R2 新提出 W3（Oracle ICC 不匹配）：R1 AGREE\n\n---\n\n## Reviewer Divergence\n\n**唯一实质分歧：Overall Score**\n\n| | R1 | R2 |\n|---|---|---|\n| Soundness | ~3.5/5 | 3.5/5 |\n| Excitement | 3/5 | 2.5/5 |\n| **Overall** | **4/5 (Weak Accept)** | **3/5 (borderline)** |\n\nR1 理由：conditional on TBD 完成，anti-informative parseable predictions + formulation×model interaction + 反直觉消融超越 \"quantifying expected trend\"。practitioner 决策价值具体。\nR2 理由：Table 6 TBD 是投稿硬伤；C4 scope 被 DeepSeek CLS≈TRAJ + re-repair 负结果大幅缩窄；C2 跨模型 claim 依赖 preliminary 数据。\n\n**两人均推荐 Findings track。**\n\n---\n\n## Questions（汇总）\n\n1. DeepSeek TRAJ 6 seeds 逐个准确率？方差来源？（R1-Q1）\n2. DeepSeek CLS < TRAJ at repo-level，C4 scope？（R1-Q2）\n3. Re-repair pilot 实验设计细节？n=44 power？（R1-Q3, R2-Q3）\n4. CLS/CWM 降采样 ~8K 准确率？（R1-Q4）\n5. Table 2 seed 基础 vs bootstrap seed 基础是否一致？（R1-Q5）\n6. %%SCENARIO-A%% 在 PDF 中是否可见？（R2-Q1）\n7. DeepSeek CWM final results 何时完成？（R2-Q2）\n8. CWM 8B parseable acc < 4B 是否 Qwen3-specific？（R2-Q4）\n9. ICC=0.191 是否在 DeepSeek 上复现？（R2-Q5）\n\n---\n\n## Round 1 → Round 2 Issue Resolution\n\n| Issue | R1 Status | R2 Status | 综合 |\n|---|---|---|---|\n| R1-N1 单 seed | in_progress | in_progress | **未解决** |\n| R1-N2 CWM 8B | resolved | resolved | **已解决** |\n| R1-N3 LoRA rank | resolved | resolved | **已解决** |\n| R2-W1 novelty | improved | improved | **改善但未消除** |\n| R2-W4 标题 | resolved | resolved | **已解决** |\n| R1-W1 TOST margin | resolved | resolved | **已解决** |\n| R1-W2 scaling arg | resolved | resolved | **已解决** |\n| R1-W3 val-test shift | resolved | resolved | **已解决** |\n| R1-W4 relaxed match | resolved | resolved | **已解决** |\n| R1-W5 ecology | resolved | resolved | **已解决** |\n| R2-W5 re-repair | evolved → C3 | evolved → C3 | **负结果存在但报告不充分** |\n| R2-W6 LEVER/CodeT | resolved | resolved | **已解决** |\n| R2-W8 引用 | resolved | resolved | **已解决** |\n| 5× Info issues | all resolved | all resolved | **全部已解决** |\n\n**Resolution rate: 12/17 (71%) fully resolved, 3 partially addressed, 2 evolved into new issues.**\n\n---\n\n## Overall Assessment\n\n**Overall Score: Borderline (ARR 3 / Findings)**\n\n**综合评分：**\n\n| 维度 | R1 | R2 | 综合 | vs Round 1 |\n|------|----|----|------|-----------|\n| Soundness | ~3.5/5 | 3.5/5 | **3.5/5** | **+1.0** |\n| Excitement | 3/5 | 2.5/5 | **2.75/5** | **+0.75** |\n| Overall | 4/5 | 3/5 | **3.5/5** | **+1.0** |\n| Confidence | 4/5 | 4/5 | **4/5** | 不变 |\n\n### 核心判断\n\n修订版在方法论严谨性上有实质性进步。消融实验、跨模型验证、TOST sensitivity、负结果报告共同将 Soundness 从 2.5 提升到 3.5。Framing pivot 和 claim 校准使论文的科学姿态与证据匹配。\n\n**仍存在的核心障碍**：\n\n1. **Table 6 不完整**（C1）：核心结果表含 TBD/preliminary 是投稿质量问题。\n2. **C4 证据基础薄弱**（C2+C3）：DeepSeek CLS ≤ TRAJ at repo-level + re-repair 负结果 → per-test granularity 的跨条件价值和下游 utility 均未充分验证。\n3. **单 seed 未解决**（C4）：4B-4B 同尺寸 repo-level 对比仍为单 seed。\n4. **Novelty 有限但有争议**（~0.5 分差距）：两人均认为适合 Findings 而非 Main。\n\n### 建议路径\n\n**推荐**：完成 Table 6 所有 TBD → 根据 TRAJ repo-level 结果调整 C4 → 提升 re-repair 负结果到 main text → 清理 SCENARIO-A → 投 Findings track。\n\n**如果 Qwen3 TRAJ repo-level > CLS**：重构 C4 为 context-dependent formulation choice（CLS for function-level + diagnostic, TRAJ for repo-level robustness）。\n\n**不建议**：当前状态（含 TBD）直接提交。\n\n---\n\n*圆桌审稿 Round 2 完成。论文从 Round 1 的 Weak Reject (2.5/5) 改善为 Borderline Findings (3-3.5/5)。两位 Reviewer 在所有 weakness 上达成共识，唯一分歧为 novelty/overall score (~0.5-1 分)。Issue Tracker 已同步更新（26 issues: 15 resolved, 6 open, 5 in_progress）。*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "force_resubmit": "True",
    "report": "# 审稿报告 — Round 2（修订版论文）\n\n**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**截止日期**: 2026-05-25\n**Reviewer**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作）\n**圆桌模式**: Round 2 独立审稿 → Step 2 交叉分享 → Step 3 收敛判定（1 轮收敛）\n**注意**: 本报告覆盖修订版论文，是对 Round 1 报告（Overall 2.5/5 Weak Reject）的更新。\n\n---\n\n## 修订版 vs Round 1 变化概要\n\n论文从 Round 1 进行了大幅修订：\n- **标题**：从 advocacy (\"Classification Scales Where Generation Stalls\") 改为中性 (\"The Formulation Design Space...\")\n- **新实验**：DeepSeek-Coder 跨模型验证、CWM 8B repo-level (65.17%)、LoRA rank 32 消融、relaxed matching 消融（反直觉降低 CWM）、匹配上下文消融（98% gap 来自 formulation）、TOST sensitivity 分析（±1/±2/±3pp）、0-shot/3-shot baselines、re-repair pilot (n=44, p=0.42 负结果)\n- **引用**：26 → 47 条，补充 LEVER/CodeT/Andrews/Just 等\n- **Framing**：从 \"CLS is superior\" 转为 \"formulation × model × complexity interaction\"\n- **Claim 校准**：条件性表述、abstract 用 19-26pp 范围、负结果诚实报告\n\nRound 1 的 17 个 issue 中 **12 个已 resolved**，3 个 in_progress，2 个演化为 Round 2 新问题。\n\n---\n\n## Summary\n\n本文系统比较 execution-free 代码修复验证的三种 formulation（CLS/CWM/TRAJ），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function/repo），使用受控实验设计。核心发现：函数级三种 formulation 近似等效（5 seeds × 2 model families）；仓库级 CWM 大幅退化（19-26pp），方向 formulation-inherent，幅度 model-contingent。修订版通过消融实验系统封堵了 LoRA capacity、exact matching penalty、input context disparity 三个替代解释。\n\n---\n\n## Strengths（Round 2 共识）\n\n**S1. Framing 根本性改善（R1-S1, R2-S1, 共识）。** 从 advocacy 转为中性 design space study。每个 claim 以条件性表述限定范围。Abstract 用 \"19-26pp\" 范围替代单点 \"25.59pp\"。科学姿态与证据强度匹配。\n\n**S2. DeepSeek 跨模型验证——最重要的实质性改进（R1-S2, R2-S2, 共识）。** Table 1 中 DeepSeek-Coder-6.7B 的三 formulation 结果独立确认函数级等价性。Repo-level degradation pattern 跨模型一致方向（CWM 退化）支持 \"formulation-inherent direction, model-contingent magnitude\"。从单模型观察提升为初步 generalizable finding。\n\n**S3. 消融实验系统封堵替代解释（R1-S3, R2-S3, 共识）。** (1) LoRA rank 32 排除 capacity bottleneck；(2) Relaxed matching 反降 CWM 准确率（反直觉，排除 exact match penalty）；(3) 匹配上下文消融 98% gap 来自 formulation（排除 input context disparity）。三组消融共同收窄因果解释空间。\n\n**S4. TOST sensitivity 分析（R1-S4, R2-S4, 共识）。** 三档 margin (±1/±2/±3pp) + minimum margin 1.63pp + deployment-significance 论证。直接回应 Round 1 质疑。\n\n**S5. 负结果诚实报告（R1-S5, R2-S1, 共识）。** Re-repair pilot 负结果、majority voting 失败、CWM 8B parseable<4B、relaxed matching 更差。增强论文可信度和信息密度。\n\n**S6. 全面覆盖和报告质量（R1-S6, R2-S6, 共识）。** 47 references、Appendix hyperparameter/mutation distribution tables、0-shot/3-shot baselines、217× throughput benchmark。Reproducibility 显著提高。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**[C1] Table 6 核心结果表含 TBD/preliminary 条目。（R1-W1 + R2-W1/W3, 完全一致）**\nQwen3 TRAJ repo-level \"TBD\"，DeepSeek CWM \"~60 preliminary\"。投稿论文核心表格的 TBD 是审稿红旗。\n- **Asymmetric risk**：若 Qwen3 TRAJ repo-level 强于 CLS（如 DeepSeek TRAJ 75.35% > CLS 74.93%），论文 contribution ranking 需重大调整。\n- **Preliminary → 确定性 claim**：Section 4.6 用 \"confirms formulation-inherent divergence\" 修饰 preliminary data。\n- **要求**：完成所有 TBD 实验后再提交。若 deadline 前无法完成，在 abstract 和 Table caption 系统标注 final/preliminary 状态。\n\n**[C2] DeepSeek CLS (74.93%) ≤ TRAJ (75.35±5.00) at repo-level，Contribution 4 scope 实质缩窄。（R1-W2, R2 AGREE \"R1独有重要发现\"）**\nC4 声称 \"per-test diagnostic granularity at equivalent trajectory-level accuracy\"。但 DeepSeek repo-level 显示 CLS 不优于 TRAJ（甚至略低）。论文回避了此比较。\n- C4 scope 从 \"跨条件通用\" 缩窄为 \"Qwen3 函数级\"。\n- 叠加 re-repair 负结果 (C3)，per-test granularity 实际价值薄弱。\n- **要求**：(1) Section 4.6 增加 DeepSeek CLS vs TRAJ 明确比较和讨论；(2) C4 限定适用范围。\n\n**[C3] Re-repair 负结果 (n=44, p=0.42) 低调处理，实质削弱 C4 下游 utility。（R1-W3 + R2-W6, 完全一致）**\nIntroduction 多次以 \"targeted re-repair\" 作为 motivation，但 pilot 负结果仅 Conclusion Future Work 单句。C4 混合 trivially true 的 throughput claim (217×) 和 unvalidated 的 utility claim。\n- **要求**：(1) 提升负结果到 main text，报告实验细节（agent、format、power analysis）；(2) C4 拆分为 efficiency (formulation-inherent) 和 diagnostic utility (unvalidated)。\n\n**[C4] 单 seed repo-level 同尺寸对比仍未实质解决。（Round 1 遗留, R1+R2 一致）**\nAbstract 改用 19-26pp 范围（改进），但 Table 6 中 Qwen3 4B-4B 仍为 seed 42 单点。CLS 4B s123=75.33% 仅在 Limitations 披露。CWM 8B 也是单 seed。从 Round 1 到 Round 2 此问题未实质改善。\n\n### Warning（应修复）\n\n**[W1] TRAJ 训练配置与 CLS/CWM 不完全受控。（R1-W4, R2 AGREE \"R1独有重要观察\"）**\nTRAJ lr=2×10⁻⁴ (CLS/CWM 5×10⁻⁵)，训练集 ~8K (CLS/CWM 70K)。CLS-TRAJ TOST 等价混淆 formulation effect 和 data volume effect。建议 CLS 降采样 ~8K 消融。\n\n**[W2] DeepSeek TRAJ repo-level ±5pp std (6 seeds) 极端不稳定。（R1-W5, R2 AGREE）**\n95% CI 约 [65,86]，跨越 majority baseline (72.96%)。未报告逐 seed 准确率，未分析方差来源。\n\n**[W3] Oracle ICC 层级不匹配。（R2-W5, R1 AGREE \"好发现，两轮未识别\"）**\nOracle frontier 使用 function-level ICC=0.191，但 repo-level ICC=0.3146 已可用未用。当前估计 conservative（方向不变），但方法论上是 level-of-analysis 错误。应同时报告两种 ICC 下的 oracle 结果。\n\n**[W4] %%SCENARIO-A%% 条件标记未清理。（R1-W6 + R2-W1, 完全一致）**\nabstract/intro/experiments/conclusion 中可见。标准 LaTeX 下为注释不影响 PDF，但暗示 work-in-progress。被注释内容可能包含有价值的 robustness 分析。提交前必须清理。\n\n---\n\n## Reviewer Consensus\n\nRound 2 交叉分享中两位 Reviewer 在所有 Weakness 上达成一致。关键新发现：\n- R1 新提出 C2（DeepSeek CLS≈TRAJ）和 W1（TRAJ confound）：R2 均 AGREE\n- R2 新提出 W3（Oracle ICC 不匹配）：R1 AGREE\n\n---\n\n## Reviewer Divergence\n\n**唯一实质分歧：Overall Score**\n\n| | R1 | R2 |\n|---|---|---|\n| Soundness | ~3.5/5 | 3.5/5 |\n| Excitement | 3/5 | 2.5/5 |\n| **Overall** | **4/5 (Weak Accept)** | **3/5 (borderline)** |\n\nR1 理由：conditional on TBD 完成，anti-informative parseable predictions + formulation×model interaction + 反直觉消融超越 \"quantifying expected trend\"。practitioner 决策价值具体。\nR2 理由：Table 6 TBD 是投稿硬伤；C4 scope 被 DeepSeek CLS≈TRAJ + re-repair 负结果大幅缩窄；C2 跨模型 claim 依赖 preliminary 数据。\n\n**两人均推荐 Findings track。**\n\n---\n\n## Questions（汇总）\n\n1. DeepSeek TRAJ 6 seeds 逐个准确率？方差来源？（R1-Q1）\n2. DeepSeek CLS < TRAJ at repo-level，C4 scope？（R1-Q2）\n3. Re-repair pilot 实验设计细节？n=44 power？（R1-Q3, R2-Q3）\n4. CLS/CWM 降采样 ~8K 准确率？（R1-Q4）\n5. Table 2 seed 基础 vs bootstrap seed 基础是否一致？（R1-Q5）\n6. %%SCENARIO-A%% 在 PDF 中是否可见？（R2-Q1）\n7. DeepSeek CWM final results 何时完成？（R2-Q2）\n8. CWM 8B parseable acc < 4B 是否 Qwen3-specific？（R2-Q4）\n9. ICC=0.191 是否在 DeepSeek 上复现？（R2-Q5）\n\n---\n\n## Round 1 → Round 2 Issue Resolution\n\n| Issue | R1 Status | R2 Status | 综合 |\n|---|---|---|---|\n| R1-N1 单 seed | in_progress | in_progress | **未解决** |\n| R1-N2 CWM 8B | resolved | resolved | **已解决** |\n| R1-N3 LoRA rank | resolved | resolved | **已解决** |\n| R2-W1 novelty | improved | improved | **改善但未消除** |\n| R2-W4 标题 | resolved | resolved | **已解决** |\n| R1-W1 TOST margin | resolved | resolved | **已解决** |\n| R1-W2 scaling arg | resolved | resolved | **已解决** |\n| R1-W3 val-test shift | resolved | resolved | **已解决** |\n| R1-W4 relaxed match | resolved | resolved | **已解决** |\n| R1-W5 ecology | resolved | resolved | **已解决** |\n| R2-W5 re-repair | evolved → C3 | evolved → C3 | **负结果存在但报告不充分** |\n| R2-W6 LEVER/CodeT | resolved | resolved | **已解决** |\n| R2-W8 引用 | resolved | resolved | **已解决** |\n| 5× Info issues | all resolved | all resolved | **全部已解决** |\n\n**Resolution rate: 12/17 (71%) fully resolved, 3 partially addressed, 2 evolved into new issues.**\n\n---\n\n## Overall Assessment\n\n**Overall Score: Borderline (ARR 3 / Findings)**\n\n**综合评分：**\n\n| 维度 | R1 | R2 | 综合 | vs Round 1 |\n|------|----|----|------|-----------|\n| Soundness | ~3.5/5 | 3.5/5 | **3.5/5** | **+1.0** |\n| Excitement | 3/5 | 2.5/5 | **2.75/5** | **+0.75** |\n| Overall | 4/5 | 3/5 | **3.5/5** | **+1.0** |\n| Confidence | 4/5 | 4/5 | **4/5** | 不变 |\n\n### 核心判断\n\n修订版在方法论严谨性上有实质性进步。消融实验、跨模型验证、TOST sensitivity、负结果报告共同将 Soundness 从 2.5 提升到 3.5。Framing pivot 和 claim 校准使论文的科学姿态与证据匹配。\n\n**仍存在的核心障碍**：\n\n1. **Table 6 不完整**（C1）：核心结果表含 TBD/preliminary 是投稿质量问题。\n2. **C4 证据基础薄弱**（C2+C3）：DeepSeek CLS ≤ TRAJ at repo-level + re-repair 负结果 → per-test granularity 的跨条件价值和下游 utility 均未充分验证。\n3. **单 seed 未解决**（C4）：4B-4B 同尺寸 repo-level 对比仍为单 seed。\n4. **Novelty 有限但有争议**（~0.5 分差距）：两人均认为适合 Findings 而非 Main。\n\n### 建议路径\n\n**推荐**：完成 Table 6 所有 TBD → 根据 TRAJ repo-level 结果调整 C4 → 提升 re-repair 负结果到 main text → 清理 SCENARIO-A → 投 Findings track。\n\n**如果 Qwen3 TRAJ repo-level > CLS**：重构 C4 为 context-dependent formulation choice（CLS for function-level + diagnostic, TRAJ for repo-level robustness）。\n\n**不建议**：当前状态（含 TBD）直接提交。\n\n---\n\n*圆桌审稿 Round 2 完成。论文从 Round 1 的 Weak Reject (2.5/5) 改善为 Borderline Findings (3-3.5/5)。两位 Reviewer 在所有 weakness 上达成共识，唯一分歧为 novelty/overall score (~0.5-1 分)。Issue Tracker 已同步更新（26 issues: 15 resolved, 6 open, 5 in_progress）。*"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-18T18:22:18.922220+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4495
}
```

</details>

---


### Assistant

_source line 146 · 2026-05-18T18:22:26.032215+00:00_

Round 2 审稿报告已投递至 Research Director。

**审稿圆桌会议总结：**

| | Round 1 | Round 2 | 变化 |
|---|---|---|---|
| R1 Overall | 2.5/5 | 4/5 | +1.5 |
| R2 Overall | 2.5/5 | 3/5 | +0.5 |
| 综合 | 2.5/5 (Weak Reject) | 3.5/5 (Borderline Findings) | +1.0 |
| Issue resolved | 0/17 | 12/17 (71%) | — |

**当前状态**：论文方法论严谨性显著提升（Soundness 2.5→3.5），但 4 个 critical issue 仍需解决（Table 6 TBD、DeepSeek CLS≤TRAJ、re-repair 报告不充分、单 seed）。两位 Reviewer 均推荐 Findings track，conditional on TBD 实验完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 15

## Round 15

56 recorded events


### User

_source line 147 · 2026-05-19T02:42:55.414312+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-19T02:43:03.592392+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-19T02:43:03.593288+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-19T02:43:06.208345+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 151 · 2026-05-19T02:43:06.258950+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-19T02:43:10.981596+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,request_external_review,get_external_review_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,request_external_review,get_external_review_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-19T02:43:11.082600+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-19T02:43:14.750199+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-19T02:43:14.750749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-19T02:43:19.205478+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-19T02:43:19.658289+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-19T02:43:20.562974+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (206 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- D124-cwm-s42-epoch2-eval（准备中）\n- repo-level-3shot-baseline: 3-shot few-shot 在 repo-level 能否作为 baseline，预期因 context 长度限制表现差于 fine-tuned models（准备中）\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (58.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\n- deepseek-traj-func-v2-s123-fixed（准备中）\n- deepseek-traj-func-v2-fixed（准备中）\n\n## 近期结论\n- **qwen3-8b-traj-repo-s42-v2** (failed): Qwen3-8B TRAJ repo-level training retry with seq4096 (v1 OOM at seq8192). Table 4 completion. DeepSeek TRAJ s42=81.25%; Qwen3-4B TRAJ=72.92%. Qwen3-8B expected ~78-85% variant-level. Lower seq_length may truncate some long repo-level diffs but DeepSeek non-8k variant showed comparable results. ← 基于 qwen3-8b-traj-repo-s42\n  [qwen3-8b-traj-repo-s42-v2-analysis](/api/workspace-files/projects/exec-sim-repair-verifier/artifacts/qwen3-8b-traj-repo-s42-v2/report/qwen3-8b-traj-repo-s42-v2-analysis.md)\n- **deepseek-cls-repo-s123** (success): DeepSeek CLS repo-level seed 123 repl
…[truncated 1827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 159 · 2026-05-19T02:43:20.563626+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit template guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit template guidelines"
  }
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-19T02:43:21.617994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-19T02:43:21.668749+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\traj}{\textsc{Traj}}
26	\newcommand{\fone}{F\textsubscript{1}}
27	\newcommand{\pp}{\,\text{pp}}
28	
29	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Controlled Empirical Study}
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{abstract}
36	
37	\input{introduction}
38	
39	\begin{figure*}[t]
40	\centering
41	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
42	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
43	\label{fig:reformulation}
44	\end{figure*}
45	
46	\input{method}
47	
48	\input{experiments}
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
53	\caption{Gap amplification from function-level to repo-level complexity. Function-level: \cls{}--\cwm{} gap is 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B (2 matched seeds, bootstrap $p{<}.01$). Repo-level same-size 4B: the gap explodes to 25.59\pp{}, with \cwm{} falling below the majority baseline (72.96\%).}
54	\label{fig:scaling_gap}
55	\end{figure}
56	
57	
58	\input{related_work}
59	
60	\input{con
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-19T02:43:36.336031+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here's information about EMNLP 2026 call for papers and ARR submission guidelines:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and rep
…[truncated 1560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 16677
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-19T02:43:37.942772+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit template guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission format, page limits, and guidelines:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given on
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 17379
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-19T02:43:44.753645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-19T02:43:45.205846+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair can be formulated in multiple ways, yet no controlled comparison exists across formulations at matched model capacity. We systematically evaluate three formulations: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring, training on identical data with controlled model sizes (4B, 8B).
3	
4	At function level, the three formulations achieve near-equivalent accuracy (\cls{} 88.43\% vs.\ \cwm{} 87.19\% at 4B, 5 seeds; Two One-Sided Tests (TOST) equivalence with trajectory-level at $p{=}0.007$). At repository level, formulation divergence amplifies to 19--26\pp{}, with \cwm{} falling below majority baseline. Cross-model validation with DeepSeek-Coder reveals a formulation $\times$ model interaction: repo-level \cwm{} degradation is formulation-inherent (both families show \cwm{} $\gg$ \cls{} performance drop from function to repo level), but its magnitude is model-contingent (Qwen3: ${\sim}$5/22\pp{} \cls{}/\cwm{} degradation; DeepSeek: 4--12/25--30\pp{}). \cwm{} additionally exhibits fragility at repo level along two dimensions: format non-compliance (51--74\% unparseable outputs) and higher seed variance at repo level (preliminary; \cls{} variance is model-contingent, ${\sim}$1--8\pp{} across families).
5	
6	Two findings generalize across conditions. First, per-test classification provides diagnostic granularity (which specific tests fail) at equivalent trajectory-level accuracy at function level, with the advantage concentrating in instances with $\geq$2 failing tests (31\% of instances, 55\% of oracle advantage). Second, formulations exhibit complementary error patterns: an oracle ensemble reaches 90.63\%. This motivates complexity-aware routing rather than a single universal formulation.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-19T02:43:45.206238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-19T02:43:45.658139+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a controlled comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic comparison of these three formulations across two model families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our results reveal a three-layer structure in the verification desi
…[truncated 3447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-19T02:43:45.708698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-19T02:43:46.562379+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-19T02:43:46.562926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-19T02:43:47.115830+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two model families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, defaulting to the final epoch checkpoint (affects DeepSeek s123 and all \cwm{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with LoRA~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. For cross-model validation, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Fu
…[truncated 17033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-19T02:43:47.116306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-19T02:43:47.618549+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Code World Models~\cite{meta2025cwm} predict output strings via 32B mid-training on execution traces; extensions address step-by-step prediction~\cite{maimon2026selfexecution}, code reasoning~\cite{liu2024codemind}, simulation-execution bridging~\cite{lee2026solidcoder}, and failure mode analysis~\cite{abdollahi2025demystifying}. Alternative formulations include trajectory-level reward models~\cite{shum2025swerm}, chain-of-thought verification~\cite{xu2025patchreasoner}, per-test classifiers~\cite{ni2023lever,chen2023codet}, and learned quality metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} further demonstrate verification value. None compare formulations at controlled capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	Lightman et al.~\cite{lightman2023letsverify} and Uesato et al.~\cite{uesato2022solving} show process-level verification outperforms outcome-level for mathematical reasoning; DreamPRM-Code~\cite{dreamprm2025code} and PRL-Coder~\cite{ye2025prlcoder} apply this to code. Our per-test classification is structurally analogous; TOST equivalence ($p = 0.007$) confirms per-test matches trajectory-level accuracy with additional diagnostic value.
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023reflexion} use execution feedback for iterative improvement. SWE-bench~\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides standard benchmarks; SWE-agent~\cite{yang2024sweagent} and Agentless~\cite{xia2024agentless} demonstrate repair pipelines where verification is a persistent bottleneck~\cite{yang2025aprsurvey}. Predictive mutation testing~\cite{tufano2019predictive
…[truncated 448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-19T02:43:47.619081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-19T02:43:48.071212+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first controlled comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). No single formulation dominates; the design space is governed by a formulation $\times$ model $\times$ complexity interaction.
5	
6	At function level, all three formulations achieve near-equivalent accuracy (TOST $p{=}0.007$). At repository level, divergence amplifies to 19--26\pp{}; cross-model validation confirms this is formulation-inherent but model-contingent in magnitude (Qwen3: ${\sim}$5/22\pp{}; DeepSeek: 4--12/25--30\pp{} for \cls{}/\cwm{}). Seed variance and evaluation protocol add further sensitivity (${\sim}$9\pp{} for the same \cwm{} checkpoint).
7	
8	Two properties generalize across models. First, per-test classification provides diagnostic granularity at equivalent trajectory-level accuracy at function level; at repo level, aggregation penalty is configuration-dependent (1.36--19\pp{}). Second, classification yields 217$\times$ throughput over generation. Error complementarity (oracle ensemble: 90.63\%) motivates routing that selects formulations by instance complexity.
9	
10	\paragraph{Limitations and future work.}
11	Most repo-level comparisons use a single seed; training data comprises synthetic mutations~\cite{andrews2005mutation,just2014mutants}; our \cwm{} (4--8B LoRA) differs from the 32B Code World Model~\cite{meta2025cwm}. Multi-seed replication and complexity-aware routing are natural extensions; a re-repair pilot ($n{=}44$, $p{=}0.42$; Appendix~\ref{app:extended_analysis}(j)) found no benefit from per-test diagnostics. Extended discussion appears in Appendix~\ref{app:limitations}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-19T02:43:48.121944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-19T02:43:49.005050+00:00_

1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level TOST analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from TOST equivalence analysis). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies rela
…[truncated 25479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 883
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-19T02:43:49.037056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-19T02:43:49.092237+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: single-seed repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and single-seed constraints.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified unde
…[truncated 4236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-19T02:43:49.092709+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-19T02:43:49.971217+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (206 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- D124-cwm-s42-epoch2-eval（准备中）\n- repo-level-3shot-baseline: 3-shot few-shot 在 repo-level 能否作为 baseline，预期因 context 长度限制表现差于 fine-tuned models（准备中）\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (58.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\n- deepseek-traj-func-v2-s123-fixed（准备中）\n- deepseek-traj-func-v2-fixed（准备中）\n\n## 近期结论\n- **qwen3-8b-traj-repo-s42-v2** (failed): Qwen3-8B TRAJ repo-level training retry with seq4096 (v1 OOM at seq8192). Table 4 completion. DeepSeek TRAJ s42=81.25%; Qwen3-4B TRAJ=72.92%. Qwen3-8B expected ~78-85% variant-level. Lower seq_length may truncate some long repo-level diffs but DeepSeek non-8k variant showed comparable results. ← 基于 qwen3-8b-traj-repo-s42\n  [qwen3-8b-traj-repo-s42-v2-analysis](/api/workspace-files/projects/exec-sim-repair-verifier/artifacts/qwen3-8b-traj-repo-s42-v2/report/qwen3-8b-traj-repo-s42-v2-analysis.md)\n- **deepseek-cls-repo-s123** (success): DeepSeek CLS repo-level seed 123 repl
…[truncated 1827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 878
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-19T02:43:54.271020+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-19T02:43:54.773323+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-19T02:43:56.379284+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-19T02:43:56.680761+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-19T02:43:57.135316+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-19T02:43:57.186177+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/literature_map.yaml\", \"content\": \"papers:\\n  # === Execution Simulation (5/5) ===\\n  - bibtex_key: maimon2026selfexecution\\n    title: \\\"Self-Execution Simulation Improves Coding Models\\\"\\n    authors: \\\"Maimon et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2604.03253\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"Train code LLMs to simulate program execution step-by-step; self-verification by filtering code solutions based on predicted output.\\\"\\n    relevance: \\\"Closest prior work — trains LLMs for execution prediction via generation, we reformulate as classification.\\\"\\n\\n  - bibtex_key: meta2025cwm\\n    title: \\\"CWM: An Open-Weights LLM for Research on Code Generation with World Models\\\"\\n    authors: \\\"Meta AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2510.02387\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"32B open-weights LLM mid-trained on Python execution traces; 65.8% on SWE-bench Verified.\\\"\\n    relevance: \\\"Production-scale CWM approach; our CWM baseline follows their generation formulation at smaller scale.\\\"\\n\\n  - bibtex_key: liu2024codemind\\n    title: \\\"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    arxiv: \\\"2402.09664\\\"\\n    doi: \\\"\\\"\\n    category: \\\"Execution Simulation\\\"\\n    verified: true\\n    abstract_snippet: \\\"Framework for evaluating LLM code reasoning: IER, DER, SR, DSR tasks. Performance drops with higher complexity.\\\"\\n    relevance: \\\"Evaluates execution reasoning capabilities; our work proposes classification as more robust formulat
…[truncated 4019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-19T02:44:22.203088+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 189 · 2026-05-19T02:44:22.203551+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/*.tex",
  "description": "Count lines in each tex file to estimate paper length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/*.tex",
    "description": "Count lines in each tex file to estimate paper length"
  }
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-19T02:44:22.203972+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/decisions.yaml\", \"content\": \"_next_id: 147\\ndecisions:\\n- id: D001\\n  date: 2026-05-11 18:01 UTC\\n  summary: 'MVP 方案: Monte Carlo oracle 模拟 + 函数级 pilot，不依赖 Docker 基础设施'\\n  rationale: '完整 Part 1 需要 Docker 重新评估 8K 个 patch 获取 per-test labels（16-24h），基础设施搭建成本高。MVP\\n    改用 Monte Carlo 模拟参数化真实测试数分布验证理论信息增益，函数级 pilot (HumanEval/MBPP) 验证可学习性。两者均无需 Docker，2-3\\n    天可完成。Pass 标准: per-test 在 70-85% 精度下 resolve rate 比 trajectory-level 高 ≥5%; 函数级\\n    pilot 精度 >70%。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-11 19:07 UTC\\n  summary: MVP-A 有条件通过：F2P-only block-corr 10.88%>5%；需补跑 Total(F2P+P2P) 模拟确认全图\\n  rationale: 真实 SWE-bench F2P median=1（69% 实例仅 1 个 F2P 测试），但 P2P median=50.5。F2P-only\\n    下 per-test 优势收窄但仍过阈值（block-corr 10.88%）。P2P regression 检测是更大的信号源——Total 分布(median=52)下优势预期更强。研究方向需校准：per-test\\n    价值主要来自 P2P regression 检测 + F2P multi-test 精确定位，而非单纯的 F2P 粒度。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: F2P-only block-corr advantage 10.88%, i.i.d. 1.98%\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-11 19:38 UTC\\n  summary: P2P regression rate 是项目关键前提——≥10% per-test 有效，<5% 则有害；需实测\\n  rationale: Total 模拟(F2P+P2P)显示 per-test 优势强烈依赖 P2P regression rate：5% 时优势为负(-1%)，10%\\n    时 13.2%，20% 时 35.7%。这是从 F2P-only 分析未发现的关键变量。真实 regression rate 未知，需从 SWE-bench\\n    数据/文献中实测。此数据点决定项目是否可行及论文 story 如何构建。\\n  related_experiments:\\n  - exp_id: mvp-a-oracle-sim\\n    role: evidence\\n    result: 'Total sim: reg=5% adv=-1%, reg=10% adv=13.2%, reg=20% adv=35.7%'\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-11 20:05 UTC\\n  summary: P2P 回归率 ~1%，原始 Total 优势前提不成立；项目 reframe 而非 kill\\n  rationale: P2P 回归率 ~1%（mean=1.04%, median=0%, 仅 22.6% 错误 patch 破坏任何 P2P 测试），远低于\\n    per-test 有效的 10% 阈值。Total(F2P+P2P) 模型下 per-test 实际有害（噪声>信号）。但项目核心价值不在信
…[truncated 1464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-19T02:44:22.354947+00:00_

    6 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex
  304 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex
   57 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex
   10 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex
  173 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex
   20 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex
   68 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
   33 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex
   11 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex
  682 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-19T02:44:36.617991+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && ls -la main.pdf 2>/dev/null && pdfinfo main.pdf 2>/dev/null | grep Pages || echo \"No PDF or pdfinfo not available\"",
  "description": "Check if compiled PDF exists and page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && ls -la main.pdf 2>/dev/null && pdfinfo main.pdf 2>/dev/null | grep Pages || echo \"No PDF or pdfinfo not available\"",
    "description": "Check if compiled PDF exists and page count"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-19T02:44:37.572569+00:00_

-rw-r--r-- 1 ubuntu ubuntu 514203 May 19 02:32 main.pdf
Pages:           17
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-19T02:44:37.926005+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && grep -c \"\\\\\\\\section\" introduction.tex method.tex experiments.tex related_work.tex conclusion.tex 2>/dev/null; grep -n \"Limitations\" conclusion.tex 2>/dev/null",
  "description": "Check section structure and Limitations placement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && grep -c \"\\\\\\\\section\" introduction.tex method.tex experiments.tex related_work.tex conclusion.tex 2>/dev/null; grep -n \"Limitations\" conclusion.tex 2>/dev/null",
    "description": "Check section structure and Limitations placement"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-19T02:44:38.026970+00:00_

introduction.tex:1
method.tex:1
experiments.tex:1
related_work.tex:1
conclusion.tex:1
10:\paragraph{Limitations and future work.}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-19T02:44:55.862979+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "目标 EMNLP 2026 via ARR，截止 2026-05-25。论文标题：The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "目标 EMNLP 2026 via ARR，截止 2026-05-25。论文标题：The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study。"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-19T02:45:21.904489+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 26041
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-19T02:45:22.055405+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n- **论文路径**: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex）\n- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求（实时搜索确认）\n- **页数限制**: 长文 8 页正文 + 无限参考文献页；短文 4 页 + 无限参考文献\n- **模板**: ACL 官方模板（Overleaf），2026 年 3 月起不接受 Word 模板\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有独立的 \"Limitations\" section，置于 Conclusion 之后、References 之前，否则 desk reject\n- **附录**: 允许，不计入页数限制\n- **引用格式**: natbib + ACL .bst\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **实验设计合理性**\n   - \"controlled comparison\" 的 claim 是否成立？训练数据、模型容量、compute 是否真正 matched？\n   - 跨模型验证（Qwen3 vs DeepSeek-Coder）是否充分？种子数量是否足够支撑统计结论？\n   - Repo-level 实验大量使用单种子，对结论的影响如何？\n   - CWM baseline 是 4-8B LoRA fine-tuned，而原始 CWM 是 32B mid-trained，这个对比的公平性和可解释性？\n\n2. **统计方法严谨性**\n   - TOST 等价性检验的 margin 选择（±2pp）是否合理？\n   - Clustered bootstrap 的设计是否正确（cluster structure、resample 策略）？\n   - ICC 估计的可靠性（function-level ICC 用于 repo-level oracle 分析是否合适）？\n   - 单种子 repo-level 比较缺乏统计效力，论文是否充分 acknowledge？\n\n3. **因果推断与 confound**\n   - \"formulation-inherent vs model-contingent\" 的 claim 是否有充分证据？\n   - Preprocessing 差异（drop vs truncate）、checkpoint 选择差异、eval seq_length 差异是否构成严重 confound？\n   - DeepSeek s123 的 NaN validation loss 导致使用 final epoch checkpoint，这是否系统性偏差？\n\n4. **Claim 与证据匹配**\n   - 每个 contribution 是否有足够的实验证据支撑？\n   - \"No single formulation dominates\" 的 claim 是否过度谨慎（CLS 在所有条件下都不差于其他方法）？\n   - Re-repair pilot (n=44, p=0.42) 作为 contribution 之一，样本量和 power 是否足够？\n   - Oracle ensemble (90.63%) 作为 claim 基础但只是 upper bound，实际 routing 可行性未验证\n\n5. **消融充分性**\n   - LoRA rank 消融只在 CWM 4B 上做，是否足够？\n   - 缺少哪些关键消融（如不同 training data size、不同 epoch、learning rate sensitivity）？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (使用 EMNLP 2026 ARR 评分标准 1-5 分) → Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n- **论文路径**: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex）\n- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求（实时搜索确认）\n- **页数限制**: 长文 8 页正文 + 无限参考文献页；短文 4 页 + 无限参考文献\n- **模板**: ACL 官方模板（Overleaf），2026 年 3 月起不接受 Word 模板\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有独立的 \"Limitations\" section，置于 Conclusion 之后、References 之前，否则 desk reject\n- **附录**: 允许，不计入页数限制\n- **引用格式**: natbib + ACL .bst\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **实验设计合理性**\n   - \"controlled comparison\" 的 claim 是否成立？训练数据、模型容量、compute 是否真正 matched？\n   - 跨模型验证（Qwen3 vs DeepSeek-Coder）是否充分？种子数量是否足够支撑统计结论？\n   - Repo-level 实验大量使用单种子，对结论的影响如何？\n   - CWM baseline 是 4-8B LoRA fine-tuned，而原始 CWM 是 32B mid-trained，这个对比的公平性和可解释性？\n\n2. **统计方法严谨性**\n   - TOST 等价性检验的 margin 选择（±2pp）是否合理？\n   - Clustered bootstrap 的设计是否正确（cluster structure、resample 策略）？\n   - ICC 估计的可靠性（function-level ICC 用于 repo-level oracle 分析是否合适）？\n   - 单种子 repo-level 比较缺乏统计效力，论文是否充分 acknowledge？\n\n3. **因果推断与 confound**\n   - \"formulation-inherent vs model-contingent\" 的 claim 是否有充分证据？\n   - Preprocessing 差异（drop vs truncate）、checkpoint 选择差异、eval seq_length 差异是否构成严重 confound？\n   - DeepSeek s123 的 NaN validation loss 导致使用 final epoch checkpoint，这是否系统性偏差？\n\n4. **Claim 与证据匹配**\n   - 每个 contribution 是否有足够的实验证据支撑？\n   - \"No single formulation dominates\" 的 claim 是否过度谨慎（CLS 在所有条件下都不差于其他方法）？\n   - Re-repair pilot (n=44, p=0.42) 作为 contribution 之一，样本量和 power 是否足够？\n   - Oracle ensemble (90.63%) 作为 claim 基础但只是 upper bound，实际 routing 可行性未验证\n\n5. **消融充分性**\n   - LoRA rank 消融只在 CWM 4B 上做，是否足够？\n   - 缺少哪些关键消融（如不同 training data size、不同 epoch、learning rate sensitivity）？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (使用 EMNLP 2026 ARR 评分标准 1-5 分) → Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-19T02:45:49.895199+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27839
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-19T02:45:51.955602+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n- **论文路径**: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex）\n- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求（实时搜索确认）\n- **页数限制**: 长文 8 页正文 + 无限参考文献页；短文 4 页 + 无限参考文献\n- **模板**: ACL 官方模板（Overleaf），2026 年 3 月起不接受 Word 模板\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有独立的 \"Limitations\" section，置于 Conclusion 之后、References 之前，否则 desk reject\n- **附录**: 允许，不计入页数限制\n- **引用格式**: natbib + ACL .bst\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性评估**\n   - 核心贡献是\"三种已知 formulation 的 controlled comparison\"——这属于 empirical study，新颖性本质来源于实验发现而非方法创新。发现本身是否足够有 insight？\n   - \"Formulation × model × complexity interaction\" 是否是一个有价值的发现，还是可以从先验知识预测？\n   - CWM 在 repo-level 失败是否早已可预期（open-ended generation + long output → exact match → failure）？\n   - 与 process vs outcome supervision 文献的关系是否被充分讨论？\n\n2. **叙事完整性 + 主线统一**\n   - Abstract → Introduction → Method → Experiments → Conclusion 是否讲述同一个故事？\n   - Introduction 的 contribution 列表是否与实验结果完全对应？\n   - 论文是否有实验报告（\"我们做了 X 得到了 Y\"）的感觉而非 insight-driven 叙事？\n   - \"Complexity-aware routing\" 在 Conclusion 中提出但未实现——是否是空头支票？\n\n3. **写作质量（按 CLAUDE.md paper-writing-norms 严格检查）**\n   - 全文 grep 检查 em-dash（—）和解释性 en-dash（–）：这些是 AI 写作最显著的标志\n   - 检查 -ing 短语结尾（\", highlighting...\"、\", demonstrating...\"等）\n   - 检查过度分段（是否每 2-3 句就换段）\n   - 检查连续过渡词（Furthermore/Moreover/Additionally 连用）\n   - 用词黑名单：delve, leverage, utilize, facilitate, myriad, plethora, paradigm shift\n   - 代词/指示词（this, that, it）指代是否明确？\n   - Abstract 是否在 150-250 words？是否自包含？\n\n4. **格式合规（desk reject 风险）**\n   - Limitations 是否为独立 section（非 Conclusion 中的 paragraph）？当前实现是 `\\paragraph{Limitations and future work.}` 在 Conclusion 内——ARR 要求独立 section，这可能导致 desk reject\n   - 正文是否在 8 页以内？\n   - 匿名化是否完全（author = Anonymous，无 GitHub link，无致谢中泄露身份信息）？\n   - 行号是否开启（review mode）？\n   - Checklist 是否每项都认真填写（非全 N/A）？\n   - 附录中的内容在正文中是否都有引用？\n\n5. **Related Work + 引用覆盖**\n   - Related Work 是否做了归纳和比较，而非论文堆砌？\n   - 引用是否覆盖：直接相关方法、baseline 论文、评测 benchmark 论文、理论基础？\n   - 是否有重要的 missing references（特别是 2025-2026 年的最新工作）？\n   - Related Work 的 positioning 是否准确？\n\n6. **图表质量**\n   - Figure 1/2/3 的信息密度是否足够？\n   - 表格格式是否统一（小数精度、加粗/下划线规则）？\n   - Caption 是否自包含？\n   - 图表是否占用过多篇幅？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (使用 EMNLP 2026 ARR 评分标准 1-5 分) → Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n- **论文路径**: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex）\n- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求（实时搜索确认）\n- **页数限制**: 长文 8 页正文 + 无限参考文献页；短文 4 页 + 无限参考文献\n- **模板**: ACL 官方模板（Overleaf），2026 年 3 月起不接受 Word 模板\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有独立的 \"Limitations\" section，置于 Conclusion 之后、References 之前，否则 desk reject\n- **附录**: 允许，不计入页数限制\n- **引用格式**: natbib + ACL .bst\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性评估**\n   - 核心贡献是\"三种已知 formulation 的 controlled comparison\"——这属于 empirical study，新颖性本质来源于实验发现而非方法创新。发现本身是否足够有 insight？\n   - \"Formulation × model × complexity interaction\" 是否是一个有价值的发现，还是可以从先验知识预测？\n   - CWM 在 repo-level 失败是否早已可预期（open-ended generation + long output → exact match → failure）？\n   - 与 process vs outcome supervision 文献的关系是否被充分讨论？\n\n2. **叙事完整性 + 主线统一**\n   - Abstract → Introduction → Method → Experiments → Conclusion 是否讲述同一个故事？\n   - Introduction 的 contribution 列表是否与实验结果完全对应？\n   - 论文是否有实验报告（\"我们做了 X 得到了 Y\"）的感觉而非 insight-driven 叙事？\n   - \"Complexity-aware routing\" 在 Conclusion 中提出但未实现——是否是空头支票？\n\n3. **写作质量（按 CLAUDE.md paper-writing-norms 严格检查）**\n   - 全文 grep 检查 em-dash（—）和解释性 en-dash（–）：这些是 AI 写作最显著的标志\n   - 检查 -ing 短语结尾（\", highlighting...\"、\", demonstrating...\"等）\n   - 检查过度分段（是否每 2-3 句就换段）\n   - 检查连续过渡词（Furthermore/Moreover/Additionally 连用）\n   - 用词黑名单：delve, leverage, utilize, facilitate, myriad, plethora, paradigm shift\n   - 代词/指示词（this, that, it）指代是否明确？\n   - Abstract 是否在 150-250 words？是否自包含？\n\n4. **格式合规（desk reject 风险）**\n   - Limitations 是否为独立 section（非 Conclusion 中的 paragraph）？当前实现是 `\\paragraph{Limitations and future work.}` 在 Conclusion 内——ARR 要求独立 section，这可能导致 desk reject\n   - 正文是否在 8 页以内？\n   - 匿名化是否完全（author = Anonymous，无 GitHub link，无致谢中泄露身份信息）？\n   - 行号是否开启（review mode）？\n   - Checklist 是否每项都认真填写（非全 N/A）？\n   - 附录中的内容在正文中是否都有引用？\n\n5. **Related Work + 引用覆盖**\n   - Related Work 是否做了归纳和比较，而非论文堆砌？\n   - 引用是否覆盖：直接相关方法、baseline 论文、评测 benchmark 论文、理论基础？\n   - 是否有重要的 missing references（特别是 2025-2026 年的最新工作）？\n   - Related Work 的 positioning 是否准确？\n\n6. **图表质量**\n   - Figure 1/2/3 的信息密度是否足够？\n   - 表格格式是否统一（小数精度、加粗/下划线规则）？\n   - Caption 是否自包含？\n   - 图表是否占用过多篇幅？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (使用 EMNLP 2026 ARR 评分标准 1-5 分) → Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-19T02:45:53.722991+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1767
}
```

</details>

---


### Assistant

_source line 202 · 2026-05-19T02:46:03.154484+00:00_

**圆桌审稿会议 — Round 1 已启动**

| 项目 | 详情 |
|------|------|
| 论文 | The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study |
| 目标 | EMNLP 2026 via ARR |
| 截止 | 2026-05-25（距今 6 天） |
| 页数 | 17 页（含正文+参考文献+checklist+附录） |
| 格式 | ACL review mode, anonymous ✓ |

**Reviewer 编排：**
- **Reviewer 1**（方法严谨性 + 实验设计 + 统计分析）— 已分派
- **Reviewer 2**（新颖性 + 完整性 + 写作质量 + 格式合规）— 已分派
- **外部审稿**（Stanford Agentic Reviewer）— 已请求，异步等待

**初步发现的格式风险：** Limitations 目前嵌入 Conclusion 中作为 `\paragraph{}`，ARR 要求独立 section 置于 Conclusion 后 References 前，否则可能 desk reject。已指示 Reviewer 2 重点核查。

等待两名 Reviewer 的独立初审报告返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 203 · 2026-05-19T02:52:26.338005+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study  
**Venue**: EMNLP 2026 (ACL Rolling Review)  
**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)  
**一句话总结**: 实验设计有方法论意识，但"controlled comparison"这一核心卖点被多个未控制的混淆因素（Traj 训练数据量差异 175×、NaN validation loss 导致的 checkpoint 选择失控、跨模型 CWM eval seq_length 不一致）实质性削弱；主要发现（CWM 在 repo-level 因 exact match + long output 而崩溃）从 formulation 的 first principles 可预期，缺乏足够的非显然 insight 支撑主会议接收。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 实验框架合理，但多个关键混淆因素未控制（详见 N1-N3），削弱核心 claim |
| Excitement | 2.5/5 | 实用导向的 empirical study，但主要发现的可预测性降低了 insight 价值 |
| Reproducibility | 3.5/5 | Hyperparameter 表格详尽，但代码/数据未公开，NaN validation loss 的复现路径不清晰 |
| Confidence | 4/5 | 仔细阅读全文及全部附录，熟悉 execution-free verification 和 process supervision 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Traj 训练数据量差异 175× 根本性破坏 "controlled comparison" 框架**
- 具体位置：Section 3.1 (setup), Appendix E (limitations)
- 问题：CLS/CWM 使用 ~70K 训练样本，Traj 仅使用 ~400 实例（Introduction 原文未提及此差异，需在 Appendix E 才能找到）。在一个以 "controlled comparison" 为核心卖点的论文中，175× 的训练数据量差异是不可接受的混淆因素。论文声称 "training on identical data with controlled model sizes"（Abstract, line 2），但 Traj 的数据量与 CLS/CWM 相差两个数量级。
- 为什么影响接收：这意味着所有涉及 Traj 的结论（包括 TOST equivalence、per-test vs trajectory-level 的核心 contribution #4）都无法归因于 formulation 差异而非数据量差异。Abstract 的 "identical data" 表述构成 overclaim。
- 建议修改方向：(1) 在 Abstract/Introduction 明确披露 Traj 数据量差异；(2) 训练 Traj 使用与 CLS/CWM 相同的 ~70K 数据（从 per-test 标签聚合为 variant-level），或 (3) 将 Traj 明确降级为 secondary baseline 而非 controlled comparison 的平等 formulation。

**N2** [critical] **NaN validation loss 导致 checkpoint 选择失控，多个关键比较受影响**
- 具体位置：Section 3.1 (setup, line 11), Table 3 footnotes, Appendix D
- 问题：DeepSeek s123、所有 CWM runs 出现 NaN validation loss，被迫使用 final epoch checkpoint 而非 val-best。这意味着这些实验配置的 checkpoint 选择策略与其他配置不同。Table 3 中 DeepSeek CLS 的 82.61% (s42, val-best) vs 74.93% (s123, final epoch) 的 7.68pp 差异，论文自己也承认 "conflates seed, preprocessing, and checkpoint selection differences"。
- 为什么影响接收：在一个强调 controlled 实验的论文中，checkpoint 选择这一关键超参数在不同配置间不一致，且原因是技术故障（NaN loss）而非设计选择。这污染了 cross-model validation（contribution #2 的核心支撑），因为无法区分 formulation 效果和 checkpoint 选择效果。
- 建议修改方向：(1) 对所有配置统一使用 final-epoch checkpoint 作为 ablation，报告统一标准下的结果；(2) 诊断并修复 NaN validation loss 的根因（truncate preprocessing 导致 length-mismatched sequences），确保所有配置都有有效的 val-based checkpoint selection。

**N3** [critical] **Desk reject 风险：Limitations 不是独立 section**
- 具体位置：conclusion.tex line 10: `\paragraph{Limitations and future work.}`
- 问题：ARR 明确要求 Limitations 为独立 section，置于 Conclusion 之后、References 之前。当前实现是 Conclusion 中的一个 `\paragraph`，不符合 ARR 格式要求。
- 为什么影响接收：这是 ARR 的 desk reject 标准之一。即使 AC 不因此 desk reject，审稿人也会将其视为对 submission guidelines 的不遵守。
- 建议修改方向：将 `\paragraph{Limitations and future work.}` 改为 `\section{Limitations}`，置于 `\section{Conclusion}` 之后、`\bibliography` 之前。Future work 部分可保留在 Conclusion 或 Limitations 中。

**N4** [critical] **CWM 比较公平性：4-8B LoRA vs 原始 32B 中训 model 的 framing 问题**
- 具体位置：Section 3.1 (line 14), Section 4.4 (constrained decoding paragraph)
- 问题：论文承认 "Our CWM baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model"，但 Abstract 和 Introduction 的叙事将此作为对 CWM *formulation* 的评判（"execution output generation" 作为一种 formulation 在 repo-level 失败）。CWM 的失败可能是 (a) formulation-inherent（如论文所称），(b) 模型容量不足（4-8B vs 32B），或 (c) 缺乏 execution trace mid-training（原始 CWM 的核心训练策略）。论文声称通过 cross-model validation 排除了 (b)，但仅在 4B-8B 范围内验证，远低于原始 CWM 的 32B。
- 为什么影响接收：如果 formulation 的表现高度依赖于模型规模和训练方式（论文自己发现 "formulation × model interaction"），那么在 4-8B 范围内的结论不能可靠外推到 32B。这削弱了 "CWM formulation 在 repo-level 本质上不可行" 这一核心 claim 的普遍性。
- 建议修改方向：(1) 更审慎的 claim：将结论限制为 "在 4-8B LoRA fine-tuning 条件下，generation formulation 在 repo-level 失败"，而非对 formulation 本身的普遍判断；(2) 如果可行，在更大规模模型上验证（即使只做 0-shot CWM）；(3) 讨论 execution trace mid-training 可能改变结论的可能性。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Abstract 数据密度过高，不符合 "30秒判断" 标准**
- 具体位置：abstract.tex
- 问题：Abstract 约 211 词，塞入了大量具体数字（88.43%, 87.19%, 19-26pp, 51-74%, 217×, 90.63%, 等等）。审稿人在 30 秒内难以提取核心 message。第二段整段都是数字和括号注释，读起来像 results summary 而非 narrative。
- 建议：保留 2-3 个最关键的数字，其余用定性描述替代。例如 "the gap amplifies to 19-26pp" 可以替代整段定量描述。

**W2** [warning] **"Complexity-aware routing" 在 Conclusion 中提出但未实现或初步验证**
- 具体位置：conclusion.tex line 8
- 问题：Conclusion 提出 "complexity-aware routing rather than a single universal formulation" 作为核心 implication，但论文没有实现或初步评估任何 routing 机制。Oracle ensemble (90.63%) 只证明了 upper bound，不代表 routing 可行。
- 建议：(1) 降低 routing 主张的语气（"potential direction" 而非 "motivates"），或 (2) 实现一个简单的 complexity-based routing（例如 function-level 用 CWM，repo-level 用 CLS），报告实际改进。

**W3** [warning] **CWM 跨模型 eval seq_length 不一致（Qwen3: 8192 vs DeepSeek: 4096）**
- 具体位置：Section 4.4 (training and evaluation sensitivity paragraph), Table 3 footnotes
- 问题：论文发现 eval seq_length 导致 ~9pp 变化（同一 checkpoint），但 cross-model CWM 比较使用了不同的 eval seq_length。论文在 Table 3 footnote 中承认 "cross-model CWM values are not directly comparable"，但 Section 4.4 "Cross-model validation" 段落仍然声称 "DeepSeek-Coder confirms the divergence is formulation-inherent"，并使用了不可比的 CWM 数值。
- 建议：在统一 eval seq_length 下重新报告 cross-model CWM 结果，或将 cross-model CWM 比较的 claim 限制为定性方向性结论。

**W4** [warning] **Related Work 过于压缩，三段 paragraph 覆盖整个领域**
- 具体位置：related_work.tex（仅 12 行 LaTeX）
- 问题：Related Work section 只有三个 paragraph，每个 paragraph 用大量密集引用堆砌。第一段 "Execution Simulation and Verification" 在 4 行内引用了 15 篇论文，读起来是 "[A] ...; [B] ...; [C] ...; [D] ..." 的列表格式，这恰恰是 writing norm 中明确禁止的 "论文堆砌"。缺乏对每类工作的归纳总结和与本文的明确对比。
- 建议：(1) 每个 paragraph 开头先写归纳性 claim，再引用支撑；(2) 对最直接的 competitor（CWM, SWE-RM, PatchReasoner）给出 1-2 句具体对比；(3) 考虑增加 "Constrained Decoding for Structured Output" 子段（论文在 Section 4.4 讨论了 constrained decoding 但未引用任何相关工作）。

**W5** [warning] **Re-repair pilot (n=44) 的统计功效不足以支撑结论**
- 具体位置：Introduction contribution #4, Appendix F(j)
- 问题：Re-repair pilot 的 sample size 只有 44，论文自己承认 "statistical power is ~0.3 for a medium effect size"。但 Introduction 的 contribution #4 将 "A re-repair pilot (n=44, p=0.42) found no benefit" 作为与其他 contribution 平列的结果呈现。Power = 0.3 意味着有 70% 的概率漏掉真实的中等效应，这个 pilot 缺乏统计效力来支撑 "no benefit" 的结论。
- 建议：(1) 从 contribution 列表中移除 re-repair pilot 或降级为 "inconclusive preliminary result"；(2) 明确声明 "absence of evidence is not evidence of absence"。

**W6** [warning] **缺失重要相关工作：REDO (Execution-Free Runtime Error Detection)**
- 具体位置：related_work.tex
- 问题：REDO (Chen et al., 2024, arXiv:2410.09117) 提出了 execution-free 的 runtime error detection 方法，结合 LLM 和静态分析工具，并基于 SWE-bench 构建了 SWEDE benchmark。这与本文的 execution-free code verification 主题直接相关，但未被引用。
- 建议：在 Related Work 中讨论 REDO 及其与本文方法的区别（REDO 关注 runtime error detection，本文关注 test outcome prediction）。

---

## 小问题（不影响接收）

- **M1**: Table 1 caption 中 "1,032-sample subset" 对 Traj 评估集的解释需要更早出现（method section），而非首次在 table caption 中提及。
- **M2**: Section 3 "Oracle Accuracy-Utility Framework" 的 $k_{\text{eff}}$ 公式假设 within-patch correlation 可用 function-level ICC 估计 repo-level 行为，但 Appendix A 自己指出 repo-level ICC = 0.3146 远高于 function-level 0.191。Framework 的定量预测基于错误的参数。
- **M3**: Figure 2 在 main.tex 中放在 related_work.tex 之前（line 50-55），但 caption 引用的是 Section 4 的内容。逻辑上应在实验结果部分出现。
- **M4**: Table 3 的 Traj 列报告的是 variant-level accuracy (n=48)，而 CLS/CWM 列是 per-test accuracy (n=9,784)。虽然 footnote 有说明，但在同一列中混合两种不同 granularity 的指标容易误导。建议分开或更显著标注。
- **M5**: Appendix Table 7 (hyperparams) 中 Qwen3-8B CWM 只有 seed 42，但 Table 2 (scaling) 报告了 s42 和 s123 的 CWM 8B 数据。这两处是否一致？（Table 2 的 CWM 8B s123 = 86.98 数据来源不清。）
- **M6**: checklist.tex C4 回答 "Partially" — 版本号应在 review 版本中就提供，camera-ready 补充不够。

---

## 主要优势

1. **实验设计的方法论意识较强**：使用 TOST equivalence testing（而非仅报告 p-value）、clustered bootstrap（考虑 within-problem correlation）、ICC 量化、sensitivity analysis。这些统计方法在 SE/NLP 实证研究中属于高标准。

2. **对自身局限的透明度**：论文明确讨论了 NaN validation loss、单种子限制、val-test distribution mismatch、eval seq_length sensitivity 等问题。这种坦诚在投稿论文中不常见，值得肯定。

3. **Failure mode taxonomy 有实用价值**：Table 4 的三种 failure mode（format collapse, decision collapse, aggregation penalty）和 qualitative error analysis（Appendix G）为从业者选择 formulation 提供了实用参考。

4. **消融实验覆盖面广**：LoRA rank ablation、majority voting、sequence-length ablation、relaxed matching、constrained decoding 讨论，涵盖了审稿人可能提出的多数 "what if" 问题。

5. **Efficiency 分析有部署价值**：CLS 217× throughput 和 CLS-Traj crossover 分析（|T| ≈ 50）是实用的工程指导。

---

## Questions for Authors

1. Traj 的 ~400 训练实例 vs CLS/CWM 的 ~70K：是否尝试过将 per-test labels 聚合为 variant-level labels 来为 Traj 构建等规模训练集？如果没有，请解释为什么这个巨大的数据量差异不会根本性地混淆 formulation 比较。

2. NaN validation loss 的根因是否已确认为 truncate preprocessing 导致的 length-mismatched sequences？如果是，为什么不统一使用 drop preprocessing？

3. 如果在所有配置上统一使用 final-epoch checkpoint（消除 checkpoint selection 混淆），核心 conclusions 是否仍然成立？

4. 论文是否考虑过在 CWM formulation 上使用 constrained decoding（论文讨论了但未实验）？即使 parseable-only accuracy 低于 majority baseline，constrained decoding 至少消除了 format collapse failure mode，可能改变 repo-level 的 failure mode taxonomy。

5. Oracle ensemble 的 90.63% 是基于 function-level 数据。Repo-level 的 oracle ensemble 结果是什么？如果 repo-level error complementarity 不存在，routing 的 motivation 就不成立。

---

## Missing References

1. **REDO** (Chen et al., 2024): Execution-free runtime error detection for coding agents, 使用 LLM + static analysis, 基于 SWE-bench 构建 SWEDE benchmark。直接相关。
2. **Constrained decoding 文献**: 论文 Section 4.4 讨论了 constrained decoding 但未引用任何相关工作。至少应引用 grammar-constrained decoding 的代表工作。
3. **SWE-bench Pro / SWE-bench++**: 更新的 benchmark 扩展，与 repo-level evaluation 相关。
4. 建议检查 `xu2025patchreasoner` 和 `li2025sstar` 在 OpenAlex 上未验证通过的问题。

---

## Overall Assessment

**Overall**: 3.0 — Findings  
**Soundness**: 3/5  
**Excitement**: 2.5/5  
**Confidence**: 4/5

**理由**: 这是一篇有方法论意识的实证研究，实验覆盖面广，对自身局限的披露比较诚实。但 "controlled comparison" 这一核心定位被多个未控制的混淆因素（N1: Traj 数据量差异 175×, N2: NaN loss 导致 checkpoint 失控, N4: 4-8B vs 32B 的 generalizability 问题）实质性削弱。主要发现的非显然性有限：CWM 在 long-output + exact match 条件下失败是可以从 formulation 设计推导出的；function-level equivalence 也符合 "short output → generation ≈ classification" 的直觉。格式问题（N3: Limitations 不是独立 section）有 desk reject 风险。建议作为 Findings 考虑接收，但需先解决 N1-N4 的核心混淆因素。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 204 · 2026-05-19T02:52:37.223236+00:00_

Reviewer 2 审稿报告已收到（3.0 / Findings）。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 205 · 2026-05-19T02:52:39.859744+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心发现摘要：

**Overall: 3.0 (Findings)**

4 个 Must-Fix 问题：
1. **Traj 训练数据量差异 175×**（~400 vs ~70K）根本性破坏 "controlled comparison" 框架，Abstract "identical data" 表述构成 overclaim
2. **NaN validation loss** 导致多个配置的 checkpoint 选择策略不一致，污染 cross-model validation
3. **Limitations 不是独立 section**（是 Conclusion 中的 `\paragraph`），有 desk reject 风险
4. **CWM 4-8B LoRA vs 原始 32B 的 framing 问题** — 结论不能从 4-8B 外推到 formulation 本身的普遍判断

6 个 Should-Fix：Abstract 数据过密、routing 未实现、CWM eval seq_length 跨模型不一致、Related Work 论文堆砌、re-repair pilot 统计功效不足、缺失 REDO 等相关工作。

优势方面：统计方法论水准高（TOST、clustered bootstrap、ICC）、自身局限披露诚实、failure mode taxonomy 有实用价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 206 · 2026-05-19T02:52:45.884202+00:00_

Reviewer 2 的报告已收到。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 18

## Round 18

6 recorded events


### User

_source line 207 · 2026-05-19T02:54:47.530067+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## 总体评分

**Overall Assessment**: 3 (Findings — 可被 Findings 接收)
**一句话总结**: 研究问题重要且统计方法论值得认可，但"controlled comparison"的核心 claim 因推理时输入上下文长度严重不对称这一未消除 confound 而被削弱，repo-level 统计效力严重不足。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | Function-level 结果有充分统计支撑（5 seeds, TOST, clustered bootstrap）；但 repo-level claims 缺乏统计效力，且存在未消除的 context-length confound |
| Excitement | 3/5 (Interesting) | 研究问题有明确实践价值（verification formulation 选择影响 repair pipeline），但结论可靠性被方法学问题削弱 |
| Reproducibility | 4/5 | 超参数、训练配置、统计方法描述详细；代码未提供但 Checklist 承诺 release |
| Confidence | 4/5 | 仔细阅读全文 + 全部附录，检查了统计方法和实验设计细节 |

---

## 主要优势

**S1. 研究问题重要且定义清晰。** 三种 execution-free verification formulation（CLS/CWM/TRAJ）之间缺乏系统比较，这是 LLM-based repair pipeline 中的实际选择困难。论文把这个工程问题提升为科学问题。

**S2. 统计方法论值得认可。** 使用 TOST 等价性检验（而非仅报 p-value 的 NHST）、clustered bootstrap（尊重 problem-level 相关结构）、ICC（量化 within-problem correlation），这在 NLP 实证研究中不常见。Section 3.1 的统计设计是本文最强的方面之一。

**S3. Function-level 结果稳健。** 5 seeds × 2 model families × 3 formulations 的 function-level 比较有足够的统计效力。TOST 等价性结论（p=0.007）和 clustered bootstrap CI 互相印证。

**S4. Failure mode taxonomy 有分析深度。** Section 2.2 和 Table 4 对 CWM 的 generation failure modes（format collapse, decision collapse, aggregation penalty）的分类分析，以及 Appendix G 的 qualitative error analysis，提供了超越数字的 insight。

**S5. 错误互补性分析有实践启示。** Section 3.6 和 Appendix I 显示 CLS 和 CWM 产生结构性不同的错误模式（CLS: false negative 偏向; CWM: format/parsing failure），oracle ensemble 达到 90.63%。这为 ensemble/routing 方向提供了 empirical motivation。

---

## Must-Fix 问题（影响接收决定）

**N1 [critical] 推理时输入上下文长度严重不对称，构成系统性 confound**

- **具体位置**: Section 3.1, Appendix B (sequence-length ablation), Appendix E (Table 10)
- **问题**: 训练时三种 formulation 统一使用 max_seq_length=2048。但推理时：
  - CWM 预留 512 tokens 给 output generation，剩余 **~1,536 tokens** 用于 input
  - CLS 只输出 1 token，可将 **5,120–8,192 tokens** 全部用于 input（Appendix B）
  
  在 repo-level 任务中，输入包含完整 repo context，通常很长。CWM 仅看到 ~1,536 tokens 的 truncated input，而 CLS 看到 **3–5 倍** 的 input context。Section 3.5 报告的 CLS 25pp+ 优势可能大部分甚至全部来自 input context 的 asymmetry，而非 formulation 本身的属性。

  Appendix B 标题为 "sequence-length ablation" 但内容是 CLS 内部的 context-length matching（限制 CLS 到 training context），**不是**跨 formulation 的 matched-context 比较。论文从未让 CLS 和 CWM 在相同 effective input length 下比较。

- **为什么影响接收**: 这直接动摇论文最核心的 claim——"formulation choice matters at repo-level complexity"（Introduction contribution 2）。如果 divergence 主要由 context asymmetry 驱动，则这不是 formulation 的属性，而是 inference-time resource allocation 的属性。
- **建议修改方向**: 增加一组实验，将 CLS 在 repo-level 推理时的 input 限制到 ~1,536 tokens（与 CWM 相同），观察 accuracy 下降幅度。如果 CLS 在 matched context 下仍显著优于 CWM，则 "formulation-inherent" claim 成立；否则需重新 frame 结论。

---

**N2 [critical] Repo-level 统计效力严重不足，不支持当前 strength 的 claims**

- **具体位置**: Section 3.5, Table 3, Appendix D (Table 9), Appendix J (Extended Limitations)
- **问题**: 多数 repo-level 配置仅使用 1–2 个 seed。Table 9 显示：
  - DeepSeek CLS variant-level accuracy 跨 seed/config 波动 ~7pp（65.17% 到 72.92%）
  - Qwen3-8B 跨 seed 波动 ~5pp
  - DeepSeek-6.7B TRAJ 仅 "preliminary: evaluated on ~72% of test instances"（Table 9 footnote）
  
  在如此高的 seed variance 下，用 1–2 个 seed 做 formulation 间比较，无法区分 formulation effect 和 seed noise。但主文 Section 3.5 的表述——"CLS achieves 19–26pp higher accuracy"、"the divergence is formulation-inherent"——读起来像 robust findings。

  Appendix J 承认 "Most repo-level comparisons use a single seed"，但这个 caveat 与主文 claim 的 strength 不匹配。
  
- **为什么影响接收**: 论文约一半贡献（repo-level complexity-dependent divergence + cross-model confirmation）建立在统计效力不足的证据上。
- **建议修改方向**: (a) 增加到 ≥3 seeds per configuration（如时间不允许，至少对 CLS vs CWM 的 key comparison 增加种子）；(b) 或者显著弱化 repo-level 结论表述，明确标注为 "preliminary observations" 而非 "established findings"；(c) 在主文而非仅附录中报告 seed variance 的量级。

---

**N3 [critical] "Controlled comparison" 的 claim 存在多个未充分处理的 confound**

- **具体位置**: Title, Abstract, Section 3.1, Appendix E
- **问题**: 论文标题和核心贡献强调 "controlled"，但以下 confound 未被消除或充分讨论：

  **(a) Preprocessing 差异**: Section 3.1 脚注提到 "s42 uses drop preprocessing; s123 uses truncate preprocessing"。Truncate 保留序列头部但截断尾部，drop 随机丢弃超长序列。对于需要看完整 output structure 的 CWM 和只需分类的 CLS，这两种 preprocessing 的影响可能不同。当论文比较 s42 vs s123 的结果时，formulation effect 和 preprocessing effect 是 confounded。

  **(b) Checkpoint 选择差异**: "runs with NaN validation loss use the final epoch checkpoint"——这影响 DeepSeek s123 **和所有 CWM runs**（Section 3.1）。论文自己指出 "Val-based checkpoint selection optimizes per-test accuracy, which biases toward predicting pass under the all-pass rule"。如果所有 CWM runs 都被迫使用 final checkpoint 而 CLS 使用 val-best checkpoint，这是系统性偏差。

  **(c) Learning rate 4x 差异**: Appendix E (Table 10) 显示 DeepSeek 使用 2×10⁻⁴，Qwen3 使用 5×10⁻⁵。不同 formulation 对 learning rate 的 sensitivity 可能不同，但论文未做 LR sensitivity analysis。

  **(d) CWM capacity 限制**: 原始 CWM 是 32B mid-trained model（FAIR CodeGen team, 2025）。本文使用 4–8B LoRA fine-tuned variant（Section 3.1: "not a reproduction of the 32B Code World Model"）。LoRA fine-tuned 4B 模型可能没有足够的 generation capacity 来产生高质量 execution output，这不是 CWM formulation 的固有缺陷，而是 capacity/training-method 的限制。

- **为什么影响接收**: "Controlled" 是论文的核心 selling point。Reviewer 和读者会据此相信结论的 internal validity。如果 comparison 不够 controlled，论文的价值命题被严重削弱。
- **建议修改方向**: (a) 统一 preprocessing 或做 preprocessing × formulation 交叉分析；(b) 量化 checkpoint selection 差异对结果的影响（如对有 val-best 的 runs 也报告 final checkpoint 的结果）；(c) 明确将结论限定为 "at 4–8B LoRA fine-tuning scale"，不做 formulation-general 的 claim。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] TOST ±2pp 等价 margin 对结论的 sensitivity 未在主文充分讨论**

- **具体位置**: Section 3.2, Appendix H (Table 12)
- **问题**: Appendix H 显示 margin sensitivity 极强：±1pp 时 TOST p=0.871（不显著 → 不等价），±2pp 时 p=0.007（显著 → 等价），±3pp 时 p<0.001。核心 "formulation equivalence" 结论完全取决于接受 ±2pp 作为 practical equivalence boundary。主文仅用一句话 justify："formulation differences below 2pp are unlikely to affect deployment decisions"——这是 pragmatic argument，但缺乏 formal grounding。
- **建议**: 在主文 Section 3.2 报告 margin sensitivity 结果；引用 bioequivalence 文献中 margin 选择的标准做法；讨论 ±1.5pp 和 ±2.5pp 的结论变化。

---

**W2 [warning] "No single formulation dominates" 的 framing 与证据不匹配**

- **具体位置**: Abstract, Section 5 (Conclusion)
- **问题**: 实际证据显示 CLS **在所有条件下都不差于**其他 formulation：function-level 等价（TOST confirmed），repo-level 显著优于 CWM（25pp+）且略优于 TRAJ（Table 3）。这不是 "no single formulation dominates"——CLS clearly dominates or ties in every setting。
  
  更准确的 characterization："CLS is the safest choice across complexity levels; CWM carries substantial degradation risk at repo-level; TRAJ offers intermediate performance with reduced diagnostic granularity."
- **建议**: 修改 framing 以准确反映 CLS 的 consistent advantage。当前过度 cautious 的 framing 可能误导 practitioners。

---

**W3 [warning] Re-repair pilot (n=44) 作为 contribution 证据不足**

- **具体位置**: Introduction (contribution list), Appendix J
- **问题**: Re-repair pilot: n=44, p=0.42, effect size ≈ 0, statistical power < 0.3 for medium effect (d=0.5)。论文自己承认 power 不足。但 Introduction 仍将 diagnostic feedback 的实用价值列为 contribution 之一。一个 null result with n=44 不构成 contribution。
- **建议**: 从 contribution list 中移除或降级为 "preliminary exploration"，在 future work 中讨论。

---

**W4 [warning] Oracle ensemble (90.63%) 缺乏 practical routing 验证**

- **具体位置**: Section 3.6, Appendix A, I
- **问题**: 90.63% 是 oracle upper bound。实际 routing 需要 selector model，但论文未验证任何 routing 机制。Oracle 到 best single formulation (~86%) 只有 ~4.6pp gap，考虑到 imperfect routing 的 overhead，actual gain 可能 ≤2pp。
- **建议**: 实现一个 simple routing baseline（如基于 input length 或 problem complexity 选择 formulation）来验证 complementarity 的 practical value，或弱化 "motivates complexity-aware routing" 的 claim。

---

**W5 [warning] ICC 跨 complexity-level 外推不当**

- **具体位置**: Appendix A
- **问题**: Oracle analysis 使用 function-level ICC = 0.191，但 Appendix A 自己报告 repo-level ICC = 0.3146（DEFF = 114.4 vs function-level DEFF = 3.97）。用 lower ICC 作为 primary estimate understate 了 repo-level 的 within-problem correlation，可能 overstate oracle advantage 的 statistical significance。
- **建议**: 使用 repo-level ICC (0.3146) 作为 repo-level oracle analysis 的 primary estimate。

---

## 小问题（不影响接收）

1. **Limitations section 格式**: Page 8 的 "Limitations and future work" 是 Conclusion (Section 5) 内的段落，非独立 section。ARR 要求 Limitations 作为独立 unnumbered section 置于 Conclusion 之后、References 之前。建议改为 `\section*{Limitations}`。

2. **Table 3 footnote**: "CWM preliminary (training in progress)"——投稿论文中不应出现 "training in progress" 表述，暗示实验未完成。如果实验未完成，不应投稿。

3. **Seed notation**: "s42"、"s123" 首次出现时（Section 3.1）未定义。建议说明 "s42 denotes random seed 42"。

4. **Figure 2 可读性**: Y 轴从 0 开始，function-level 区域的差异在视觉上几乎不可见。建议使用 broken axis 或 inset 放大。

5. **引用完整性**: verify_references 工具报告 47/47 cited keys 全部在 bib 中匹配，0 orphan/0 missing。8 篇 "not_found" 为 OpenAlex 数据库覆盖问题（如 Lightman et al. 2023, AlphaCode 2 Technical Report），非伪造风险。4 篇 minor author name encoding mismatch。引用诚信无问题。

---

## Questions for Authors

**Q1**: 如果将 CLS 在 repo-level 推理时的 input truncate 到 ~1,536 tokens（与 CWM 相同 effective input length），CLS 的 repo-level accuracy 会下降多少？这个实验是否可在 rebuttal 期间完成？

**Q2**: Section 3.1 提到 "all CWM runs" 出现 NaN validation loss 而使用 final checkpoint。这是否意味着 CWM 的 training 在 LoRA 设置下本质上不稳定？如果是，这是 formulation 问题还是 hyperparameter tuning 问题？

**Q3**: LoRA rank ablation 仅在 CWM 4B 上做到 rank 32（Appendix B, Table 6）。如果使用 full fine-tuning 或更高 rank，CWM 的 generation quality 是否会显著改善？这对 "formulation-inherent" claim 的影响如何？

**Q4**: DeepSeek 的 learning rate 是 Qwen3 的 4 倍（2×10⁻⁴ vs 5×10⁻⁵, Table 10）。这个差异是如何确定的？是否做过 LR sensitivity analysis across formulations？

**Q5**: Appendix C 报告 "gold mutation (unmodified code) parse rate collapses from 43.5% (4B) to 23.9% (8B)"。更大的模型在 unmodified code 上反而更差，这是否暗示 training data 或 evaluation 存在系统性问题？

---

## Missing References

1. **ScratchPad** (Nye et al., 2021): Execution trace generation 的开创性工作，与 CWM formulation 直接相关——模型生成 intermediate execution states。论文讨论了 Code World Models 但未引用这个 foundational work。

2. **Math-Shepherd** (Wang et al., 2024) / **OmegaPRM** (Luo et al., 2024): Process reward model training 的重要方法论参考。论文在 Related Work Section 4 讨论了 PRM 但仅引用了 Lightman et al. 和 Uesato et al.，缺少这些 recent PRM training methodology 的引用。

3. **CodeExecutor** (Liu et al., 2024, ACL 2024): 训练模型模拟 code execution 的工作，与 CWM formulation 高度相关。

---

## 总结

本文提出了一个重要的研究问题并展示了值得认可的统计方法论意识。Function-level 的等价性结论有足够证据支撑。但论文最有新意的贡献——repo-level complexity-dependent divergence——受到三个 critical 问题的制约：(1) 推理时 context-length asymmetry 是一个未被隔离的 major confound，(2) repo-level seed 数量不足以支撑 statistical claims，(3) 多个其他 confound（preprocessing, checkpoint, learning rate, model capacity）削弱了 "controlled" 的 claim。

如果 N1（context-length ablation）能在 rebuttal 期间完成并确认 formulation effect 独立于 context effect，加上适当弱化 repo-level claims 的 strength，本文可达到 Findings 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-19T02:55:15.011972+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 — Overall: 3.0 (Findings)\n\n**Must-Fix 问题：**\n\n**N1 [critical] Traj 训练数据量差异 175×（~400 vs ~70K）根本性破坏 \"controlled comparison\" 框架**\n- CLS/CWM 使用 ~70K 训练样本，Traj 仅使用 ~400 实例。Abstract \"training on identical data with controlled model sizes\" 构成 overclaim。所有涉及 Traj 的结论（包括 TOST equivalence）都无法归因于 formulation 差异而非数据量差异。\n\n**N2 [critical] NaN validation loss 导致 checkpoint 选择失控**\n- DeepSeek s123、所有 CWM runs 出现 NaN validation loss，被迫使用 final epoch checkpoint。Table 3 中 7.68pp 差异 \"conflates seed, preprocessing, and checkpoint selection differences\"。污染 cross-model validation。\n\n**N3 [critical] Desk reject 风险：Limitations 不是独立 section**\n- 当前是 Conclusion 中的 `\\paragraph{Limitations and future work.}`，ARR 要求独立 section。\n\n**N4 [critical] CWM 4-8B LoRA vs 原始 32B 的 framing 问题**\n- 在 4-8B 范围内的结论不能外推到 32B。CWM 失败可能是 capacity/training-method 限制而非 formulation-inherent。\n\n**Should-Fix 问题：**\n\n**W1** Abstract 数据密度过高（~211 词塞入大量具体数字），不符合 \"30秒判断\" 标准。\n\n**W2** \"Complexity-aware routing\" 在 Conclusion 中提出但未实现，Oracle ensemble 只证明 upper bound。\n\n**W3** CWM 跨模型 eval seq_length 不一致（Qwen3: 8192 vs DeepSeek: 4096），但 cross-model validation 仍声称 \"divergence is formulation-inherent\"。\n\n**W4** Related Work 仅 3 段 paragraph，第一段 4 行内引用 15 篇论文，属于 \"论文堆砌\"。\n\n**W5** Re-repair pilot (n=44, power~0.3) 作为 contribution 证据不足。\n\n**W6** 缺失 REDO (Chen et al., 2024) 等重要相关工作。\n\n**Missing References**: REDO, constrained decoding 文献, SWE-bench Pro/SWE-bench++。\n\n---\n\n请对以上每个 N 和 W 点逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 — Overall: 3.0 (Findings)\n\n**Must-Fix 问题：**\n\n**N1 [critical] Traj 训练数据量差异 175×（~400 vs ~70K）根本性破坏 \"controlled comparison\" 框架**\n- CLS/CWM 使用 ~70K 训练样本，Traj 仅使用 ~400 实例。Abstract \"training on identical data with controlled model sizes\" 构成 overclaim。所有涉及 Traj 的结论（包括 TOST equivalence）都无法归因于 formulation 差异而非数据量差异。\n\n**N2 [critical] NaN validation loss 导致 checkpoint 选择失控**\n- DeepSeek s123、所有 CWM runs 出现 NaN validation loss，被迫使用 final epoch checkpoint。Table 3 中 7.68pp 差异 \"conflates seed, preprocessing, and checkpoint selection differences\"。污染 cross-model validation。\n\n**N3 [critical] Desk reject 风险：Limitations 不是独立 section**\n- 当前是 Conclusion 中的 `\\paragraph{Limitations and future work.}`，ARR 要求独立 section。\n\n**N4 [critical] CWM 4-8B LoRA vs 原始 32B 的 framing 问题**\n- 在 4-8B 范围内的结论不能外推到 32B。CWM 失败可能是 capacity/training-method 限制而非 formulation-inherent。\n\n**Should-Fix 问题：**\n\n**W1** Abstract 数据密度过高（~211 词塞入大量具体数字），不符合 \"30秒判断\" 标准。\n\n**W2** \"Complexity-aware routing\" 在 Conclusion 中提出但未实现，Oracle ensemble 只证明 upper bound。\n\n**W3** CWM 跨模型 eval seq_length 不一致（Qwen3: 8192 vs DeepSeek: 4096），但 cross-model validation 仍声称 \"divergence is formulation-inherent\"。\n\n**W4** Related Work 仅 3 段 paragraph，第一段 4 行内引用 15 篇论文，属于 \"论文堆砌\"。\n\n**W5** Re-repair pilot (n=44, power~0.3) 作为 contribution 证据不足。\n\n**W6** 缺失 REDO (Chen et al., 2024) 等重要相关工作。\n\n**Missing References**: REDO, constrained decoding 文献, SWE-bench Pro/SWE-bench++。\n\n---\n\n请对以上每个 N 和 W 点逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-19T02:55:28.769092+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13757
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-19T02:55:28.920213+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 — Overall: 3 (Findings)\n\n**Must-Fix 问题：**\n\n**N1 [critical] 推理时输入上下文长度严重不对称，构成系统性 confound**\n- 训练时统一 max_seq_length=2048，但推理时 CWM 仅 ~1,536 tokens input（预留 512 给 output），CLS 可用 5,120-8,192 tokens。CLS 25pp+ 优势可能大部分来自 input context asymmetry 而非 formulation 本身。\n- Appendix B 的 \"sequence-length ablation\" 是 CLS 内部的 context-length matching，不是跨 formulation 的 matched-context 比较。\n- 建议：将 CLS 在 repo-level 推理时限制到 ~1,536 tokens，观察 accuracy 下降幅度。\n\n**N2 [critical] Repo-level 统计效力严重不足**\n- 多数 repo-level 配置仅 1-2 个 seed。DeepSeek CLS variant-level accuracy 跨 seed/config 波动 ~7pp。在如此高的 seed variance 下用 1-2 seed 做比较无法区分 formulation effect 和 seed noise。\n- 主文表述（\"CLS achieves 19-26pp higher accuracy\"、\"divergence is formulation-inherent\"）读起来像 robust findings，与实际 statistical power 不匹配。\n\n**N3 [critical] \"Controlled comparison\" 的 claim 存在多个未充分处理的 confound**\n- (a) Preprocessing 差异（drop vs truncate）\n- (b) Checkpoint 选择差异（val-best vs final epoch，所有 CWM runs 被迫用 final checkpoint）\n- (c) Learning rate 4x 差异（DeepSeek 2×10⁻⁴ vs Qwen3 5×10⁻⁵）\n- (d) CWM capacity 限制（4-8B LoRA vs 原始 32B mid-trained）\n\n**Should-Fix 问题：**\n\n**W1** TOST ±2pp margin 对结论 sensitivity 极强（±1pp → p=0.871 不等价，±2pp → p=0.007 等价），主文 justification 不足。\n\n**W2** \"No single formulation dominates\" 的 framing 与证据不匹配——CLS 在所有条件下都不差于其他 formulation，actually dominates or ties。\n\n**W3** Re-repair pilot (n=44, power<0.3) 作为 contribution 证据不足。\n\n**W4** Oracle ensemble (90.63%) 缺乏 practical routing 验证。\n\n**W5** ICC 跨 complexity-level 外推不当（function-level ICC=0.191 用于 repo-level oracle analysis，但 repo-level ICC=0.3146）。\n\n**Missing References**: ScratchPad (Nye et al., 2021), Math-Shepherd/OmegaPRM, CodeExecutor (Liu et al., 2024 ACL)。\n\n---\n\n请对以上每个 N 和 W 点逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 — Overall: 3 (Findings)\n\n**Must-Fix 问题：**\n\n**N1 [critical] 推理时输入上下文长度严重不对称，构成系统性 confound**\n- 训练时统一 max_seq_length=2048，但推理时 CWM 仅 ~1,536 tokens input（预留 512 给 output），CLS 可用 5,120-8,192 tokens。CLS 25pp+ 优势可能大部分来自 input context asymmetry 而非 formulation 本身。\n- Appendix B 的 \"sequence-length ablation\" 是 CLS 内部的 context-length matching，不是跨 formulation 的 matched-context 比较。\n- 建议：将 CLS 在 repo-level 推理时限制到 ~1,536 tokens，观察 accuracy 下降幅度。\n\n**N2 [critical] Repo-level 统计效力严重不足**\n- 多数 repo-level 配置仅 1-2 个 seed。DeepSeek CLS variant-level accuracy 跨 seed/config 波动 ~7pp。在如此高的 seed variance 下用 1-2 seed 做比较无法区分 formulation effect 和 seed noise。\n- 主文表述（\"CLS achieves 19-26pp higher accuracy\"、\"divergence is formulation-inherent\"）读起来像 robust findings，与实际 statistical power 不匹配。\n\n**N3 [critical] \"Controlled comparison\" 的 claim 存在多个未充分处理的 confound**\n- (a) Preprocessing 差异（drop vs truncate）\n- (b) Checkpoint 选择差异（val-best vs final epoch，所有 CWM runs 被迫用 final checkpoint）\n- (c) Learning rate 4x 差异（DeepSeek 2×10⁻⁴ vs Qwen3 5×10⁻⁵）\n- (d) CWM capacity 限制（4-8B LoRA vs 原始 32B mid-trained）\n\n**Should-Fix 问题：**\n\n**W1** TOST ±2pp margin 对结论 sensitivity 极强（±1pp → p=0.871 不等价，±2pp → p=0.007 等价），主文 justification 不足。\n\n**W2** \"No single formulation dominates\" 的 framing 与证据不匹配——CLS 在所有条件下都不差于其他 formulation，actually dominates or ties。\n\n**W3** Re-repair pilot (n=44, power<0.3) 作为 contribution 证据不足。\n\n**W4** Oracle ensemble (90.63%) 缺乏 practical routing 验证。\n\n**W5** ICC 跨 complexity-level 外推不当（function-level ICC=0.191 用于 repo-level oracle analysis，但 repo-level ICC=0.3146）。\n\n**Missing References**: ScratchPad (Nye et al., 2021), Math-Shepherd/OmegaPRM, CodeExecutor (Liu et al., 2024 ACL)。\n\n---\n\n请对以上每个 N 和 W 点逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-19T02:55:30.531535+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 212 · 2026-05-19T02:55:34.289262+00:00_

交叉分享已发送给两位 Reviewer。等待交叉回应返回后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 19

## Round 19

1 recorded events


### User

_source line 213 · 2026-05-19T02:55:37.095302+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论概要**:

- **Overall Assessment**: 3/5 (Findings)
- **Soundness**: 3/5 — Function-level 结果稳健，但 repo-level 存在严重 confound
- **Excitement**: 3/5 — 研究问题有实践价值

**3 个 Must-Fix 问题**:
1. **推理时 input context 长度不对称** — CWM 仅 ~1536 tokens vs CLS 5120-8192 tokens，这是 repo-level 25pp 差距的潜在主因，未做 matched-context ablation
2. **Repo-level 统计效力不足** — 多数配置仅 1-2 seeds，seed variance 可达 ~7pp，无法支撑当前 strength 的 claims
3. **多个未消除 confound** — preprocessing 差异、checkpoint 选择差异、learning rate 4x 差异、CWM capacity 受限，削弱 "controlled comparison" 的核心 claim

**5 个 Should-Fix**: TOST margin sensitivity 应在主文讨论、"No single formulation dominates" framing 与证据不符（CLS 在所有条件下不差于其他方法）、re-repair pilot (n=44) 不足以作为 contribution、oracle ensemble 缺 practical routing 验证、ICC 跨 level 外推不当。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 214 · 2026-05-19T02:58:04.399275+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1

---

### Must-Fix

**[REBUT] R1-N1: 推理时输入上下文长度严重不对称**

R1 声称 Appendix B 的消融"是 CLS 内部的 context-length matching，不是跨 formulation 的 matched-context 比较"。这一判断不准确。Appendix B（line 70）明确报告了跨 formulation 的 matched-context 比较：

> "The matched-context gap (CLS@2,048 vs. CWM@2,048) is 25.00pp (98% of the full 25.59pp gap), confirming that input context disparity explains at most 3% of the difference."

这里 CLS@2,048 和 CWM@2,048 是在相同总 sequence length 下的跨 formulation 比较。需要承认的 nuance 是：即使总 seq_length 匹配，CWM 仍需预留 512 tokens 给 output（有效输入 ~1,536），而 CLS 几乎全部用于输入（~2,047）。但根据 CLS@8192→CLS@2048 仅下降 1.44pp 的趋势，进一步从 2,048→1,536 的额外下降预计不超过 ~1pp，不会实质性改变 25pp 的跨 formulation gap。

R1 的关切方向合理（input context 是一个 confound），但论文已提供了直接的消融证据证明其影响 <3%。建议作者补充一句明确说明 CLS@2048 和 CWM@2048 之间仍有 ~500 token 的 effective input 差异，但影响可忽略。

**严重性评估：R1 高估了此问题。论文已有充分消融。降级为 Should-Fix（建议补充说明 effective input tokens 差异）。**

---

**[AGREE] R1-N2: Repo-level 统计效力严重不足**

完全同意。与我的 N2（NaN validation loss 导致 checkpoint 选择失控）共同构成对 repo-level claims 可靠性的核心质疑。具体数据：

- DeepSeek CLS 跨 seed/config 波动 7.68pp（Table 3 footnote）
- Qwen3-4B CLS 只有 seed 42（Appendix E line 304 确认）
- Qwen3-8B CLS 有 s42 和 s123，但 s123 使用 truncate preprocessing + final epoch，与 s42 不可比
- CWM 所有 repo-level runs 都被迫用 final epoch checkpoint

论文在 Appendix E 坦诚列出了这些限制，但主文中 "CLS achieves 19-26pp higher accuracy"、"divergence is formulation-inherent" 的表述暗示了比实际证据更强的 robustness。我在自己的 N2 中也提出了同样的问题。

---

**[AGREE] R1-N3(a)(b)(d): Confounds — preprocessing、checkpoint、CWM capacity**

与我的 N1（Traj 数据量差异 175×）和 N4（4-8B vs 32B）一致。R1 和我从不同角度指向同一个核心问题：**论文的 "controlled comparison" framing 被多个未控制的 confounds 实质性削弱。**

补充一个 R1 未提及但同样严重的 confound：**Traj 训练数据量差异**。CLS/CWM 使用 ~70K 训练样本，Traj 仅 ~400 实例（Appendix E line 304, Table 7 caption）。这是 175× 的差异，Abstract 中 "identical data" 的表述构成 overclaim。

**[REBUT] R1-N3(c): Learning rate 4× 差异（DeepSeek 2×10⁻⁴ vs Qwen3 5×10⁻⁵）**

R1 将 LR 差异列为 confound，但需要区分：这是 **跨模型** 差异，不是 **跨 formulation** 差异。Table 7 (Appendix D) 明确显示：同一模型家族内，CLS 和 CWM 使用完全相同的 learning rate（Qwen3: 5×10⁻⁵ for both；DeepSeek: 2×10⁻⁴ for both）。跨模型 LR 差异是 per-model tuning 的结果（"tuned on a held-out validation split"），这在 cross-model validation 中是标准做法，不构成 formulation 比较的 confound。

如果 R1 的意思是 DeepSeek 和 Qwen3 之间的 LR 差异影响 cross-model generalizability，这有一定道理，但不影响 within-model formulation 比较的有效性。

---

### Should-Fix

**[AGREE] R1-W1: TOST ±2pp margin sensitivity**

Appendix G（Table 8）已展示 sensitivity：±1pp → p=0.871（不等价），±2pp → p=0.007（等价），最小等价 margin = ±1.63pp。论文的 practical justification（"below 2pp, seed/checkpoint/hyperparameter variance dominates"）在 Appendix 中陈述，但主文只用一句话带过（Section 4.2 line 98: "sensitivity analysis across margins appears in Appendix"）。

核心问题是：选择 ±1.63pp 还是 ±2pp 作为 margin 直接决定了 "equivalence" 这一 contribution 是否成立。建议在主文中增加 1-2 句解释 ±2pp 的 practical rationale。

不过，±2pp 作为 practical significance threshold 在应用领域并非不合理（类似于 Cohen's d=0.2 作为 "small effect"）。论文的 justification 有逻辑基础，只是披露不够充分。

---

**[AGREE] R1-W2: "No single formulation dominates" framing**

从纯 accuracy 维度看，R1 说得对：CLS 在所有条件下都 ≥ 其他 formulation。论文主张 "No single formulation dominates" 的合理性仅来自 **非 accuracy 维度**（CWM 的 error complementarity、Traj 避免 aggregation penalty）。但 Conclusion line 2 的原文 "No single formulation dominates; the design space is governed by a formulation × model × complexity interaction" 读起来像是在说 accuracy dimension，而非多维权衡。建议改为更精确的表述，如 "CLS achieves the best or equivalent accuracy across all tested conditions, but..."。

---

**[AGREE] R1-W3: Re-repair pilot 证据不足**

与我的 W5 一致。n=44, power<0.3，作为 contribution #4 的证据不充分。

---

**[AGREE] R1-W4: Oracle ensemble 缺乏 practical routing 验证**

与我的 W2 一致。Oracle ensemble (90.63%) 是 upper bound，不等于 routing 可行。

---

**[REBUT] R1-W5: ICC 跨 complexity-level 外推**

R1 指出 function-level ICC=0.191 被用于 repo-level oracle analysis，而 repo-level ICC=0.3146。但论文在 Appendix A（line 38-39）已经 **明确讨论了这个问题** 并给出了方法论上站得住脚的论证：

> "Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each T stratum... The function-level ICC = 0.191 used in Table 5 thus provides a **conservative lower bound** on the per-test advantage."

使用较低的 ICC 值会低估（而非高估）per-test 的优势，因此不会导致论文的 claim 被 inflate。Oracle analysis 的结论 "per-test advantage concentrates at T≥2" 在更高 ICC 下只会更强，不会更弱。这个设计选择是方法论上保守的，不是 bug。

**严重性评估：R1 低估了论文已有的讨论。论文已显式说明 ICC=0.191 是 conservative lower bound。此问题不需修改。**

---

### Missing References

**[AGREE]** CodeExecutor (Liu et al., 2024 ACL) 和 ScratchPad (Nye et al., 2021) 与本文 CWM formulation 直接相关，应引用。

**[AGREE]** Math-Shepherd / OmegaPRM 与 per-test vs trajectory-level 的 process/outcome supervision 类比相关。论文引用了 Lightman et al. (2023) 但缺少这两篇。

补充我在 Round 1 提出的：**REDO** (Chen et al., 2024, arXiv:2410.09117) 也应引用——execution-free runtime error detection for coding agents。

---

### 总结

R1 和我在以下问题上高度一致（独立发现）：
1. Repo-level 统计效力不足（R1-N2 ≈ 我的 N2）
2. "Controlled comparison" 被多个 confounds 削弱（R1-N3 ≈ 我的 N1/N4）
3. Re-repair pilot 证据不足（R1-W3 ≈ 我的 W5）
4. Oracle routing 无实际验证（R1-W4 ≈ 我的 W2）

**我与 R1 的分歧**：
1. **R1-N1（context length asymmetry）**：R1 高估了此问题。论文已有 CLS@2048 vs CWM@2048 的直接消融，证明 input context 差异仅解释 <3% 的 gap。建议降级为 Should-Fix。
2. **R1-N3(c)（LR 差异）**：这是跨模型差异，不是跨 formulation 差异。同一模型内 CLS/CWM 使用相同 LR。
3. **R1-W5（ICC 外推）**：论文已在 Appendix A 显式论证 ICC=0.191 是 conservative lower bound。此问题无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 215 · 2026-05-19T02:58:10.482241+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 216 · 2026-05-19T02:58:13.207973+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

与 Reviewer 1 的关键共识和分歧：

**高度一致**（独立发现相同问题）：
- Repo-level 统计效力不足
- "Controlled comparison" 被多个 confounds 削弱
- Re-repair pilot 和 oracle routing 证据不足

**分歧点**：
1. **R1-N1 context length asymmetry** — 我认为 R1 高估了此问题，论文已有 CLS@2048 vs CWM@2048 消融证明影响 <3%，建议降级为 Should-Fix
2. **R1-N3(c) LR 差异** — 这是跨模型差异，同一模型内 CLS/CWM 使用相同 LR，不构成 formulation confound
3. **R1-W5 ICC 外推** — 论文已显式论证 ICC=0.191 是 conservative lower bound，无需修改

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 217 · 2026-05-19T02:58:18.065871+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 22

## Round 22

10 recorded events


### User

_source line 218 · 2026-05-19T02:59:52.587116+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

### Must-Fix 问题

**[AGREE] R2-N1: TRAJ 训练数据量差异 175×**

R2 指出了一个我在 Round 1 中遗漏的重要 confound。根据论文 Section 3.1（page 4）：CLS/CWM 在 repo-level 有 ~70K per-test 训练样本，而 TRAJ 按 patch-level 标注，SWE-bench Verified 训练集约 ~400 个 unique patches，数据量差异确实约 175×。在 function-level，CLS/CWM 有 ~15,280 per-test 样本 vs TRAJ 约 ~500-600 variant-level 样本，比例约 27×。

Abstract 声称 "training on identical data with controlled model sizes"——这在 underlying dataset 意义上是对的（同一批 patches 和 tests），但在 effective training examples 数量上是误导性的。TOST 等价性结论（Section 3.2）无法区分 "formulation 等价" 和 "TRAJ 在 27× 更少数据下仍达到相同准确率（即 TRAJ 更 data-efficient）" 这两种解释。

**补充我的观察**: 这个 data asymmetry 在一定程度上是 formulation-inherent 的——TRAJ 按设计就只能有 patch-level 标注。但论文应当明确讨论这一点：(a) 在 "controlled comparison" 的 claim 中加入 caveat；(b) 讨论 TRAJ 是否可以通过 data augmentation（如 per-test auxiliary signal）来缩小差距；(c) 至少在 function-level 做一个 data-size matched 实验（如 downsample CLS 到与 TRAJ 相同数量）。

这个问题的优先级应该与我的 N1（context-length confound）和 N3（多个 confound）并列。R2 正确地指出它根本性地影响所有涉及 TRAJ 的结论。

---

**[AGREE] R2-N2: NaN validation loss 导致 checkpoint 选择失控**

与我 Round 1 的 N3(b) 一致。R2 的表述更精确：Table 3（page 6）中 DeepSeek CLS s42 vs s123 的 ~7.68pp 差异 "conflates seed, preprocessing, and checkpoint selection differences"。

补充一个论文自身的矛盾：Section 3.5（page 7）的 "Checkpoint selection confound" 段落明确承认 "Val-based selection optimizes per-test accuracy, which biases toward predicting pass under the all-pass rule; this has penalties variant-level performance."——即论文知道 checkpoint selection 是 confound，但同一段的 "Cross-model validation" 段落仍用包含此 confound 的 DeepSeek 结果声称 "confirms the divergence is formulation-inherent"。

这是 internal inconsistency：如果 checkpoint selection 是 acknowledged confound，就不能同时用受该 confound 污染的结果作为 causal claim 的 evidence。

---

**[AGREE on substance, REBUT on severity] R2-N3: Limitations 不是独立 section**

R2 指出的格式问题是准确的。Page 8 的 "Limitations and future work." 确实是 `\paragraph{}` 级别，在 Section 5 Conclusion 内部，不是独立的 `\section*{Limitations}`。ARR 明确要求 "All papers must include a discussion of limitations at the end of the paper, in a dedicated section titled 'Limitations'."

但我对 "critical" 严重程度有异议。理由：
1. 这是一个 **30 秒的 LaTeX 修复**（`\paragraph{...}` → `\section*{Limitations}`），不涉及任何实质性内容改动。
2. Limitations 的 **内容本身是充分的**：主文段落 + Appendix J (Extended Limitations) 覆盖了 single-seed limitations, mutation vs real faults, training scale 等关键局限。
3. 与 N1（175× 数据差异）和 N2（checkpoint confound）相比，这不是 "影响接收决定" 级别的问题，而是 "投稿前 checklist 遗漏" 级别。

建议降级为 Should-Fix/高优先 Minor，但承认它确实需要在投稿前修复以避免 desk reject 风险。

---

**[AGREE] R2-N4: CWM 4-8B LoRA vs 原始 32B 的 framing 问题**

与我 Round 1 的 N3(d) 完全一致。Section 3.1（page 4）自己说 "Our CWM baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model"，但论文的 conclusion 仍做 formulation-general 的 claim。

R2 的 framing 比我的更直接："在 4-8B 范围内的结论不能外推到 32B"。我同意。LoRA fine-tuned 4B 模型的 generation capacity 可能根本不足以产生高质量 execution output——这不能归因于 CWM formulation 的固有缺陷。

论文需要将所有关于 CWM 的结论明确限定为 "at 4-8B LoRA fine-tuning scale"，或增加更高 capacity 的实验点（如 full fine-tuning 或使用原始 32B CWM 的 inference-only evaluation）。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract 数据密度过高**

Abstract（page 1）在约 211 词内塞入了 CLS 88.43%、CWM 87.19%、TOST p=0.007、19-26pp gap、90.63% oracle 等大量数字。审稿人在 30 秒内无法 parse 这些数字的含义和关系。Abstract 应侧重故事线（问题 → 洞察 → 关键发现），最多保留 2-3 个支撑核心 claim 的数字。

---

**[AGREE] R2-W2: Routing 未实现**

与我 Round 1 的 W4 一致。Oracle ensemble 90.63% 是 upper bound；没有任何 practical routing 机制被验证。Conclusion（page 8）提出 "complexity-aware routing" 作为 implication，但缺乏 empirical support。

---

**[AGREE] R2-W3: CWM 跨模型 eval seq_length 不一致**

R2 指出 Qwen3 CWM 使用 eval seq_length=8192，DeepSeek CWM 使用 4096。论文自己在 page 7 承认："Table 3 CWM values use different eval lengths across models (Qwen3: 8192, DeepSeek: 4096); cross-model CWM numbers are not directly comparable."

但这与 Section 3.5 的 "Cross-model validation confirms the divergence is formulation-inherent" claim 直接矛盾。如果 CWM 跨模型的数字 "not directly comparable"，那 cross-model validation 对于 CWM 就不成立。加上我在 N1 中指出的 CWM vs CLS 的 input context 不对称（CWM ~1536 vs CLS 5120-8192 tokens），repo-level 的 cross-model "validation" 实际上是在不可比条件下做的。

R2 的这个点与我的 N1 互补：我关注的是 formulation 间的 context asymmetry，R2 关注的是同一 formulation 跨模型的 seq_length inconsistency。两者共同削弱 "formulation-inherent" 的 causal claim。

---

**[REBUT] R2-W4: Related Work 仅 3 段，属于 "论文堆砌"**

R2 的批评有一定道理但过度了。反驳理由：

1. **Page constraints**: 8 页正文限制下，Related Work 占约 2/3 column（page 7-8）是 top-venue empirical papers 的 norm。EMNLP 2024 Best Paper "Scaling Data-Constrained Language Models"（Muennighoff et al.）的 Related Work 同样只有 ~2/3 column。

2. **Thematic organization is correct**: Section 4 分为三个清晰的 thematic groups——(a) Execution Simulation and Verification, (b) Process vs Outcome Supervision, (c) Repair, Mutation Testing, and Task Framing。这不是 "A proposed X, B proposed Y" 的 flat listing，而是有 positioning 的归纳。

3. **Citation count adequate**: 47 篇引用对一篇 bridging SE and NLP 的 empirical study 而言在合理范围内。

我承认第一段的 citation density 确实偏高（约 10 篇 in 4 行），可以通过更有选择性地讨论 2-3 篇最相关的工作来改善。但将整个 Related Work 定性为 "论文堆砌" 不公平。

---

**[AGREE] R2-W5: Re-repair pilot (n=44, power~0.3) 证据不足**

与我 Round 1 的 W3 完全一致。n=44, p=0.42, power < 0.3 for medium effect。不足以支撑 contribution claim。

---

**[AGREE] R2-W6: 缺失 REDO 等重要相关工作**

R2 提到的 REDO (Chen et al., 2024) 处理 code execution/debugging，与本文的 execution-free verification formulation 直接相关。SWE-bench Pro 和 SWE-bench++ 作为 SWE-bench 生态中的后续 benchmark 也应被讨论。Constrained decoding 文献与论文 Section 3.5 讨论的 CWM format compliance failures（Table 4: format collapse 占 repo-level CWM 错误的重要比例）直接相关，可能提供 mitigation strategy。

---

### 综合评估

R2 的审稿意见整体质量高。最大贡献是 **N1（TRAJ 175× 数据差异）**——这是我 Round 1 完全遗漏的关键 confound，与我的 N1（context-length asymmetry）和 N3（多个 confound）共同构成对 "controlled comparison" claim 的三重挑战。

将 R2 的发现整合到我的评估中，论文的核心 weakness 可以总结为：

**"Controlled" comparison 存在至少 4 个未消除的 confound**：
1. TRAJ 训练数据量差异 175×（R2-N1）
2. 推理时 input context 长度不对称 3-5×（R1-N1）
3. Checkpoint 选择差异（R1-N3b, R2-N2）
4. CWM eval seq_length 跨模型不一致（R2-W3）

这些 confound 的累积效应意味着：论文对 formulation 差异的 attribution 可靠性不足。每个 confound 单独看可能不致命，但 4 个同时存在使得 "the first controlled comparison" 的 claim 实质上不成立。

**Overall Assessment 维持 3 (Findings)**。Function-level 结果（5 seeds, TOST, clustered bootstrap）仍然 solid，论文的统计方法论意识值得认可。但 repo-level claims 和 "controlled comparison" framing 需要 substantial revision。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-19T03:00:12.225892+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-19T03:00:12.427305+00:00_

issues:
# === Round 1 Critical Issues ===

- id: "R1-N1"
  summary: "Repo-level 核心 claim 基于单 seed，seed 方差极大 (8.3pp)"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 2
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "R1-N1 + R2-W2。CLS 4B s42=83.63% vs s123=75.33%。"
    - round: 2
      reviewers: [1, 2]
      note: "R2-C4。Abstract 改用 19-26pp 范围（改进），但 4B-4B 仍单 seed。CWM 8B 也是单 seed。"
  action_items:
    - round: 1
      action: "补充多 seed 同尺寸对比"
      assigned_to: "agent+paper"
      status: in_progress
      progress_note: "8B-8B 双 seed 已有。DeepSeek CLS v5 retrain 中 (~May 20)。4B-4B 无法在 DDL 前补 seed。"
  resolution: ""
  resolution_round: null

- id: "R1-N2"
  summary: "CWM 8B repo-level 结果缺失"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "CWM 8B repo-level 缺失。"
    - round: 2
      reviewers: [1]
      note: "CWM 8B 已完成（65.17%, 73.8% unparse, 单 seed）。R1 确认 resolved。"
  action_items:
    - round: 1
      action: "CWM 8B repo-level 训练"
      assigned_to: "agent"
      status: done
  resolution: "CWM 8B 完成。Round 2 确认 resolved。"
  resolution_round: 2

- id: "R1-N3"
  summary: "CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "rank-32 消融完成。两轮均确认 resolved。"
  resolution_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "resolved"

- id: "R2-W1"
  summary: "核心贡献新颖性不足以支撑 EMNLP main conference"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 2
  mentions:
    - round: 1
      reviewers: [2]
      note: "Excitement R1:3 vs R2:2。"
    - round: 2
      reviewers: [1, 2]
      note: "R2 Excitement 2.5/5, R1 3/5。两人均推荐 Findings 而非 Main。分歧缩小至 ~0.5 分。"
  action_items:
    - round: 1
  
…[truncated 9571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-19T03:00:12.478736+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-19T03:00:12.529387+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-19T02:44:59.045975+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_061c4b1115e483e8fdad01cae91c873a\", \"skipped_at\": \"2026-05-19T02:49:39.948903+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-19T03:02:16.663170+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "issues:\n# === Round 3 Critical Issues (fresh review) ===\n\n- id: \"R3-N1\"\n  summary: \"TRAJ 训练数据量差异 175×（~400 vs ~70K）破坏 controlled comparison 框架\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 首次提出。Abstract 'identical data' 构成 overclaim。所有涉及 TRAJ 的结论无法归因于 formulation 差异。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 交叉回应 AGREE。补充指出数据不对称部分是 formulation-inherent（TRAJ 按设计只有 patch-level 标注），建议 downsample CLS 做 matched 实验或明确降级 TRAJ 为 secondary baseline。\"\n  action_items:\n    - round: 3\n      action: \"三选一：(1) Abstract/Intro 明确披露数据量差异并加 caveat；(2) 训练 TRAJ 用 ~70K 聚合数据；(3) 降级 TRAJ 为 secondary baseline\"\n      assigned_to: \"paper+agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Repo-level 统计效力严重不足，多数配置仅 1-2 seeds\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现。DeepSeek CLS 跨 seed/config 波动 7.68pp，Qwen3-4B 仅 seed 42，CWM 8B 单 seed。主文 claim strength 与实际 statistical power 不匹配。\"\n  action_items:\n    - round: 3\n      action: \"增加种子至 ≥3 per key comparison，或显著弱化 repo-level 结论表述为 preliminary observations\"\n      assigned_to: \"agent+paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"NaN validation loss 导致 checkpoint 选择策略跨配置不一致\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"DeepSeek s123 + 所有 CWM runs 使用 final epoch checkpoint（NaN loss），其余用 val-best。论文承认 checkpoint confound 但仍用受污染数据声称 'formulation-inherent'，构成 internal inconsistency。\"\n  action_items:\n    - round: 3\n      action: \"统一 checkpoint 策略做 ablation（如所有配置报告 final-epoch 结果），或修复 NaN 根因\"\n      assigned_to: \"agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"CWM 4-8B LoRA 结论不能外推为 generation formulation 的普遍判断\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现。4-8B LoRA fine-tuned 可能容量不足以支撑高质量 generation。原始 CWM 是 32B mid-trained，训练策略完全不同。结论需限定为 'at 4-8B LoRA scale'。\"\n  action_items:\n    - round: 3\n      action: \"将所有 CWM 结论限定为 '4-8B LoRA fine-tuning 条件下'；讨论 execution trace mid-training 可能改变结论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 3 Should-Fix Issues ===\n\n- id: \"R3-W1\"\n  summary: \"Limitations 不是独立 section，有 desk reject 风险\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 列为 critical。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 同意事实但降级为高优先 Should-Fix（30秒 LaTeX 修复，内容本身充分）。\"\n  action_items:\n    - round: 3\n      action: \"将 \\\\paragraph{Limitations and future work.} 改为 \\\\section*{Limitations}，置于 Conclusion 之后 References 之前\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Abstract 数据密度过高，不符合 30 秒可判断标准\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。211 词内塞入过多数字，应保留 2-3 个关键数字，其余定性描述。\"\n  action_items:\n    - round: 3\n      action: \"精简 Abstract 数字，保留核心 claim 支撑数据\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"'No single formulation dominates' framing 与证据不符\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE。CLS 在所有条件下 ≥ 其他 formulation。当前 framing 可能误导 practitioners。\"\n  action_items:\n    - round: 3\n      action: \"改为更精确表述，如 'CLS achieves the best or equivalent accuracy across all tested conditions, but error complementarity suggests multi-formulation value'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"CWM 跨模型 eval seq_length 不一致（Qwen3: 8192, DeepSeek: 4096）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 提出。论文承认 'not directly comparable' 但仍声称 cross-model validation 确认 formulation-inherent。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 AGREE，指出与 context length asymmetry 互补，共同削弱 causal claim。\"\n  action_items:\n    - round: 3\n      action: \"统一 eval seq_length 重新报告，或将 cross-model CWM 结论限制为定性方向性\"\n      assigned_to: \"agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"Re-repair pilot (n=44, power<0.3) 不足以作为 contribution\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现且交叉确认。n=44, p=0.42, power~0.3。应从 contribution list 移除或降级为 inconclusive preliminary。\"\n  action_items:\n    - round: 3\n      action: \"从 Introduction contribution list 移除或降级；明确 'absence of evidence ≠ evidence of absence'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Oracle ensemble (90.63%) 缺乏 practical routing 验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现。Oracle 是 upper bound，routing 未实现。Conclusion 的 'motivates routing' 缺乏 empirical support。\"\n  action_items:\n    - round: 3\n      action: \"弱化 routing claim 或实现 simple routing baseline\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"TOST ±2pp margin sensitivity 主文披露不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出。Appendix 有 sensitivity table 但主文仅一句话引用。±1pp→不等价, ±2pp→等价, 结论高度 margin-sensitive。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 AGREE，但认为 ±2pp practical significance threshold 有合理基础，只是披露不够充分。\"\n  action_items:\n    - round: 3\n      action: \"主文 Section 4.2 增加 1-2 句 sensitivity 结果和 margin 选择 rationale\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W8\"\n  summary: \"缺失重要相关工作：REDO, ScratchPad, CodeExecutor, Math-Shepherd/OmegaPRM\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1: ScratchPad (Nye 2021), Math-Shepherd/OmegaPRM, CodeExecutor (Liu 2024 ACL)。R2: REDO (Chen 2024), constrained decoding 文献。两人交叉确认。\"\n  action_items:\n    - round: 3\n      action: \"补充引用并在 Related Work 中讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W9\"\n  summary: \"推理时 context length asymmetry（CWM ~1536 vs CLS 5120-8192 tokens）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 列为 critical。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 REBUT：论文已有 CLS@2048 vs CWM@2048 消融，影响 <3%。建议降级为 Should-Fix，补充说明 effective input tokens 差异。R1 未反驳。\"\n  action_items:\n    - round: 3\n      action: \"补充一句说明 CLS@2048 和 CWM@2048 之间仍有 ~500 token effective input 差异\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 3 Minor Issues ===\n\n- id: \"R3-M1\"\n  summary: \"Table 1 caption Traj 评估子集 (1,032-sample) 应在 method section 更早说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"首次在 table caption 而非 method section 提及。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Oracle framework $k_{eff}$ 用 function-level ICC=0.191，repo-level ICC=0.3146 更合适\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 提出。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 列为 W5。R2 REBUT：论文已论证 ICC=0.191 是 conservative lower bound，更高 ICC 只会强化结论。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"Figure 2 在 main.tex 中位置（related_work 前）与内容（Section 4）不匹配\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"逻辑上应在实验结果部分。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Table 3 TRAJ 列 (n=48 variant-level) 与 CLS/CWM 列 (n=9784 per-test) 混合不同指标\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"Footnote 有说明但容易误导，建议分开或更显著标注。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Appendix Table 7 CWM 8B 仅列 seed 42，但 Table 2 报告了 s42+s123 数据\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"数据来源不一致。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M6\"\n  summary: \"Checklist C4 回答 Partially，版本号应在 review 版本提供\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"Camera-ready 补充不够。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M7\"\n  summary: \"Seed notation (s42, s123) 首次出现未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"建议说明 s42 denotes random seed 42。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M8\"\n  summary: \"Figure 2 可读性：function-level 差异在当前 Y 轴尺度下几乎不可见\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"建议 broken axis 或 inset 放大。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Previous Rounds — Resolved Issues (carried forward) ===\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CWM 8B 完成。Round 2 确认 resolved。\"\n  resolution_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"rank-32 消融完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Title changed.\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正当性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"TOST sensitivity table 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Relaxed matching 反降准确率。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"人工突变 vs 真实 bug ecological validity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Limitations 增加讨论。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"遗漏 LEVER 和 CodeT\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已添加。\"\n  resolution_round: 1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "issues:\n# === Round 3 Critical Issues (fresh review) ===\n\n- id: \"R3-N1\"\n  summary: \"TRAJ 训练数据量差异 175×（~400 vs ~70K）破坏 controlled comparison 框架\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 首次提出。Abstract 'identical data' 构成 overclaim。所有涉及 TRAJ 的结论无法归因于 formulation 差异。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 交叉回应 AGREE。补充指出数据不对称部分是 formulation-inherent（TRAJ 按设计只有 patch-level 标注），建议 downsample CLS 做 matched 实验或明确降级 TRAJ 为 secondary baseline。\"\n  action_items:\n    - round: 3\n      action: \"三选一：(1) Abstract/Intro 明确披露数据量差异并加 caveat；(2) 训练 TRAJ 用 ~70K 聚合数据；(3) 降级 TRAJ 为 secondary baseline\"\n      assigned_to: \"paper+agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N2\"\n  summary: \"Repo-level 统计效力严重不足，多数配置仅 1-2 seeds\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现。DeepSeek CLS 跨 seed/config 波动 7.68pp，Qwen3-4B 仅 seed 42，CWM 8B 单 seed。主文 claim strength 与实际 statistical power 不匹配。\"\n  action_items:\n    - round: 3\n      action: \"增加种子至 ≥3 per key comparison，或显著弱化 repo-level 结论表述为 preliminary observations\"\n      assigned_to: \"agent+paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"NaN validation loss 导致 checkpoint 选择策略跨配置不一致\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"DeepSeek s123 + 所有 CWM runs 使用 final epoch checkpoint（NaN loss），其余用 val-best。论文承认 checkpoint confound 但仍用受污染数据声称 'formulation-inherent'，构成 internal inconsistency。\"\n  action_items:\n    - round: 3\n      action: \"统一 checkpoint 策略做 ablation（如所有配置报告 final-epoch 结果），或修复 NaN 根因\"\n      assigned_to: \"agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N4\"\n  summary: \"CWM 4-8B LoRA 结论不能外推为 generation formulation 的普遍判断\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现。4-8B LoRA fine-tuned 可能容量不足以支撑高质量 generation。原始 CWM 是 32B mid-trained，训练策略完全不同。结论需限定为 'at 4-8B LoRA scale'。\"\n  action_items:\n    - round: 3\n      action: \"将所有 CWM 结论限定为 '4-8B LoRA fine-tuning 条件下'；讨论 execution trace mid-training 可能改变结论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 3 Should-Fix Issues ===\n\n- id: \"R3-W1\"\n  summary: \"Limitations 不是独立 section，有 desk reject 风险\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 列为 critical。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 同意事实但降级为高优先 Should-Fix（30秒 LaTeX 修复，内容本身充分）。\"\n  action_items:\n    - round: 3\n      action: \"将 \\\\paragraph{Limitations and future work.} 改为 \\\\section*{Limitations}，置于 Conclusion 之后 References 之前\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Abstract 数据密度过高，不符合 30 秒可判断标准\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。211 词内塞入过多数字，应保留 2-3 个关键数字，其余定性描述。\"\n  action_items:\n    - round: 3\n      action: \"精简 Abstract 数字，保留核心 claim 支撑数据\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W3\"\n  summary: \"'No single formulation dominates' framing 与证据不符\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE。CLS 在所有条件下 ≥ 其他 formulation。当前 framing 可能误导 practitioners。\"\n  action_items:\n    - round: 3\n      action: \"改为更精确表述，如 'CLS achieves the best or equivalent accuracy across all tested conditions, but error complementarity suggests multi-formulation value'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W4\"\n  summary: \"CWM 跨模型 eval seq_length 不一致（Qwen3: 8192, DeepSeek: 4096）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 提出。论文承认 'not directly comparable' 但仍声称 cross-model validation 确认 formulation-inherent。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 AGREE，指出与 context length asymmetry 互补，共同削弱 causal claim。\"\n  action_items:\n    - round: 3\n      action: \"统一 eval seq_length 重新报告，或将 cross-model CWM 结论限制为定性方向性\"\n      assigned_to: \"agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W5\"\n  summary: \"Re-repair pilot (n=44, power<0.3) 不足以作为 contribution\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现且交叉确认。n=44, p=0.42, power~0.3。应从 contribution list 移除或降级为 inconclusive preliminary。\"\n  action_items:\n    - round: 3\n      action: \"从 Introduction contribution list 移除或降级；明确 'absence of evidence ≠ evidence of absence'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Oracle ensemble (90.63%) 缺乏 practical routing 验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两人独立发现。Oracle 是 upper bound，routing 未实现。Conclusion 的 'motivates routing' 缺乏 empirical support。\"\n  action_items:\n    - round: 3\n      action: \"弱化 routing claim 或实现 simple routing baseline\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W7\"\n  summary: \"TOST ±2pp margin sensitivity 主文披露不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出。Appendix 有 sensitivity table 但主文仅一句话引用。±1pp→不等价, ±2pp→等价, 结论高度 margin-sensitive。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 AGREE，但认为 ±2pp practical significance threshold 有合理基础，只是披露不够充分。\"\n  action_items:\n    - round: 3\n      action: \"主文 Section 4.2 增加 1-2 句 sensitivity 结果和 margin 选择 rationale\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W8\"\n  summary: \"缺失重要相关工作：REDO, ScratchPad, CodeExecutor, Math-Shepherd/OmegaPRM\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1: ScratchPad (Nye 2021), Math-Shepherd/OmegaPRM, CodeExecutor (Liu 2024 ACL)。R2: REDO (Chen 2024), constrained decoding 文献。两人交叉确认。\"\n  action_items:\n    - round: 3\n      action: \"补充引用并在 Related Work 中讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W9\"\n  summary: \"推理时 context length asymmetry（CWM ~1536 vs CLS 5120-8192 tokens）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 列为 critical。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 REBUT：论文已有 CLS@2048 vs CWM@2048 消融，影响 <3%。建议降级为 Should-Fix，补充说明 effective input tokens 差异。R1 未反驳。\"\n  action_items:\n    - round: 3\n      action: \"补充一句说明 CLS@2048 和 CWM@2048 之间仍有 ~500 token effective input 差异\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 3 Minor Issues ===\n\n- id: \"R3-M1\"\n  summary: \"Table 1 caption Traj 评估子集 (1,032-sample) 应在 method section 更早说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"首次在 table caption 而非 method section 提及。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M2\"\n  summary: \"Oracle framework $k_{eff}$ 用 function-level ICC=0.191，repo-level ICC=0.3146 更合适\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"R2 提出。\"\n    - round: 3\n      reviewers: [1]\n      note: \"R1 列为 W5。R2 REBUT：论文已论证 ICC=0.191 是 conservative lower bound，更高 ICC 只会强化结论。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"Figure 2 在 main.tex 中位置（related_work 前）与内容（Section 4）不匹配\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"逻辑上应在实验结果部分。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M4\"\n  summary: \"Table 3 TRAJ 列 (n=48 variant-level) 与 CLS/CWM 列 (n=9784 per-test) 混合不同指标\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"Footnote 有说明但容易误导，建议分开或更显著标注。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M5\"\n  summary: \"Appendix Table 7 CWM 8B 仅列 seed 42，但 Table 2 报告了 s42+s123 数据\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"数据来源不一致。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M6\"\n  summary: \"Checklist C4 回答 Partially，版本号应在 review 版本提供\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"Camera-ready 补充不够。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M7\"\n  summary: \"Seed notation (s42, s123) 首次出现未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"建议说明 s42 denotes random seed 42。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M8\"\n  summary: \"Figure 2 可读性：function-level 差异在当前 Y 轴尺度下几乎不可见\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"建议 broken axis 或 inset 放大。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === Previous Rounds — Resolved Issues (carried forward) ===\n\n- id: \"R1-N2\"\n  summary: \"CWM 8B repo-level 结果缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"CWM 8B 完成。Round 2 确认 resolved。\"\n  resolution_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"resolved\"\n\n- id: \"R1-N3\"\n  summary: \"CWM baseline LoRA rank 16 可能系统性低估 generation formulation 能力\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"rank-32 消融完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"标题 'scales' 缺乏数据支撑\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Title changed.\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"TOST ±2pp equivalence margin 缺乏正当性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"TOST sensitivity table 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"CWM exact string matching 未尝试 relaxed matching\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Relaxed matching 反降准确率。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"人工突变 vs 真实 bug ecological validity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Limitations 增加讨论。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"遗漏 LEVER 和 CodeT\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已添加。\"\n  resolution_round: 1"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-19T03:02:16.815062+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 12216}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-19T03:04:14.278812+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# Round 3 审稿报告（Fresh Review）\n\n**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n**Venue**: EMNLP 2026 (ACL Rolling Review)\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作质量+格式合规）\n**外部审稿**: 已跳过（用户未提交）\n\n---\n\n## Summary\n\n本文对三种 execution-free code verification formulation（per-test classification CLS、execution output generation CWM、trajectory-level patch scoring TRAJ）进行了系统对比，使用两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别（function-level, repo-level）、多个随机种子。核心发现：function-level 三种 formulation 准确率等价（TOST $p=0.007$）；repo-level CLS 显著优于 CWM（19-26pp）；CWM 在 repo-level 因 format collapse 失效（51-74% 不可解析输出）；CLS 和 CWM 存在互补错误模式（oracle ensemble 90.63%）。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且定义清晰。** 三种 execution-free verification formulation 之间缺乏系统比较，论文将工程选择问题提升为科学问题，对 LLM-based repair pipeline 从业者有直接实用价值。[R1-S1, R2 共识]\n\n**S2. 统计方法论水准高。** 使用 TOST 等价性检验（非仅 NHST）、clustered bootstrap（尊重 problem-level 相关结构）、ICC 量化 within-problem correlation、margin sensitivity analysis。这在 NLP 实证研究中属于高标准。[R1-S2, R2 优势 #1]\n\n**S3. Function-level 结果稳健。** 5 seeds × 2 model families × 3 formulations 的 function-level 比较有充分统计效力，TOST 等价性结论和 clustered bootstrap CI 互相印证。[R1-S3]\n\n**S4. Failure mode taxonomy 有实用价值。** Table 4 的三种 failure mode 分类（format collapse, decision collapse, aggregation penalty）和 Appendix G 的 qualitative error analysis 为从业者选择 formulation 提供了实用参考。[R1-S4, R2 优势 #3]\n\n**S5. 对自身局限的透明度。** 论文明确讨论了 NaN validation loss、单种子限制、val-test distribution mismatch、eval seq_length sensitivity 等问题。这种坦诚在投稿论文中不常见。[R2 优势 #2]\n\n**S6. 消融实验覆盖面广。** LoRA rank ablation、majority voting、sequence-length ablation、relaxed matching、constrained decoding 讨论，涵盖了审稿人可能提出的多数 \"what if\" 问题。[R2 优势 #4]\n\n**S7. Efficiency 分析有部署价值。** CLS 217× throughput 和 CLS-TRAJ crossover 分析（|T| ≈ 50）提供了实用的工程指导。[R2 优势 #5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] TRAJ 训练数据量差异 175× 根本性破坏 \"controlled comparison\" 框架** [R2 提出, R1 AGREE]\n\nCLS/CWM 使用 ~70K 训练样本，TRAJ 仅 ~400 实例（175× 差异）。Abstract 声称 \"training on identical data with controlled model sizes\"，在 effective training examples 数量上构成 overclaim。所有涉及 TRAJ 的结论（包括 TOST equivalence、per-test vs trajectory-level 的 contribution #4）无法可靠归因于 formulation 差异而非数据量差异。R1 补充指出此数据不对称部分是 formulation-inherent（TRAJ 按设计只有 patch-level 标注），但论文应明确讨论这一点。\n\n*建议*：(1) Abstract/Introduction 明确披露数据量差异；(2) 将 TRAJ 降级为 secondary baseline 而非 controlled comparison 的平等 formulation；(3) 或在 function-level 做 data-size matched 实验（downsample CLS 到与 TRAJ 相同数量）。\n\n**N2 [critical] Repo-level 统计效力严重不足** [R1 提出, R2 AGREE]\n\n多数 repo-level 配置仅 1-2 个 seed。DeepSeek CLS 跨 seed/config 波动 7.68pp，Qwen3-4B CLS 仅 seed 42。在如此高的 seed variance 下，1-2 seed 无法区分 formulation effect 和 seed noise。但主文 \"CLS achieves 19-26pp higher accuracy\"、\"divergence is formulation-inherent\" 的表述暗示了远超实际证据的 robustness。\n\n*建议*：增加到 ≥3 seeds per key comparison，或显著弱化 repo-level 结论表述为 \"preliminary observations\"。\n\n**N3 [critical] NaN validation loss 导致 checkpoint 选择策略跨配置不一致** [R2 提出, R1 AGREE]\n\nDeepSeek s123 + 所有 CWM runs 出现 NaN validation loss，被迫使用 final epoch checkpoint，而其他配置使用 val-best。论文 Section 4.4 自己承认 \"Val-based selection optimizes per-test accuracy, which biases toward predicting pass\"，但 \"Cross-model validation\" 段落仍用包含此 confound 的结果声称 \"confirms the divergence is formulation-inherent\"。这构成 internal inconsistency。\n\n*建议*：(1) 对所有配置统一报告 final-epoch checkpoint 的结果作为 ablation；(2) 修复 NaN loss 根因（truncate preprocessing）。\n\n**N4 [critical] CWM 4-8B LoRA 结论不能外推为 generation formulation 的普遍判断** [R1, R2 独立发现]\n\n论文承认 \"Our CWM baseline is a LoRA fine-tuned variant, not a reproduction of the 32B Code World Model\"，但叙事层面仍做 formulation-general 的 claim。CWM 的失败可能反映 (a) formulation-inherent 属性（论文所称），(b) 4-8B 容量不足（原始 CWM 32B），或 (c) 缺乏 execution trace mid-training。论文仅在 4-8B 范围验证了 (b)，远不足以排除。\n\n*建议*：将所有 CWM 结论限定为 \"at 4-8B LoRA fine-tuning scale\"；讨论 execution trace mid-training 可能改变结论的可能性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [high-priority] Limitations 不是独立 section，有 desk reject 风险** [R2 提出, R1 AGREE on fact]\n\n当前是 Conclusion 中的 `\\paragraph{Limitations and future work.}`，ARR 要求独立 `\\section*{Limitations}` 置于 Conclusion 之后 References 之前。R1 认为 30 秒 LaTeX 修复不构成 critical，但投稿前必须修复。\n\n**W2 Abstract 数据密度过高** [R2 提出, R1 AGREE]\n\n~211 词内塞入大量具体数字，审稿人 30 秒内难以提取核心 message。建议保留 2-3 个关键数字，其余定性描述。\n\n**W3 \"No single formulation dominates\" framing 与证据不符** [R1 提出, R2 AGREE]\n\nCLS 在所有条件下 ≥ 其他 formulation。\"No single formulation dominates\" 仅在非 accuracy 维度（error complementarity）成立，当前表述易误导 practitioners。建议改为更精确的 framing。\n\n**W4 CWM 跨模型 eval seq_length 不一致** [R2 提出, R1 AGREE]\n\nQwen3 CWM eval 8192, DeepSeek CWM eval 4096。论文承认 \"not directly comparable\" 但仍声称 cross-model validation。与 N3 的 checkpoint confound 共同削弱 \"formulation-inherent\" causal claim。\n\n**W5 Re-repair pilot (n=44, power<0.3) 不足以作为 contribution** [R1, R2 独立发现]\n\nn=44, p=0.42, power ~0.3。应从 contribution list 移除或降级为 \"inconclusive preliminary result\"。\n\n**W6 Oracle ensemble (90.63%) 缺乏 practical routing 验证** [R1, R2 独立发现]\n\nOracle 是 upper bound。Conclusion 提出 \"complexity-aware routing\" 但未实现任何 routing 机制。建议弱化 claim 或实现 simple routing baseline。\n\n**W7 TOST ±2pp margin sensitivity 主文披露不足** [R1 提出, R2 AGREE]\n\n±1pp → 不等价 (p=0.871), ±2pp → 等价 (p=0.007)。核心 equivalence 结论高度 margin-sensitive。主文应增加 sensitivity 结果和 margin 选择 rationale。\n\n**W8 缺失重要相关工作** [R1, R2 交叉确认]\n\nR1: ScratchPad (Nye et al., 2021), Math-Shepherd/OmegaPRM, CodeExecutor (Liu et al., 2024 ACL)。R2: REDO (Chen et al., 2024), constrained decoding 文献。\n\n**W9 推理时 context length asymmetry** [R1 提出, R2 REBUT 并降级]\n\nCWM ~1536 tokens vs CLS 5120-8192 tokens。R2 提供论文 Appendix B 证据：matched-context ablation (CLS@2048 vs CWM@2048) 显示 input context 差异仅解释 <3% 的 gap。R1 未反驳。降级为 Should-Fix，建议补充说明 effective input tokens 差异。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识（独立发现 + 交叉确认）：\n\n1. **Repo-level 统计效力不足**（N2）：证据最薄弱的环节恰是论文最核心的贡献\n2. **\"Controlled comparison\" 被多个 confounds 削弱**（N1, N3, N4）：TRAJ 数据量 175×、checkpoint 不一致、CWM capacity 限制\n3. **Re-repair pilot 证据不足**（W5）：n=44 不支撑 contribution claim\n4. **Oracle routing 无实际验证**（W6）：upper bound ≠ 可行性\n5. **CWM 结论需限定规模**（N4）：4-8B LoRA ≠ formulation 普遍判断\n\n## Reviewer Divergence [REBUT]\n\n以下分歧已在交叉回应中解决：\n\n1. **R1-N1 context length asymmetry**：R1 列为 critical，R2 REBUT 引用 Appendix B 消融证据（<3%），R1 未反驳 → 降级为 Should-Fix (W9)\n2. **R1-N3c LR 4× 差异**：R2 正确指出同一模型内 CLS/CWM 使用相同 LR，跨模型差异是标准做法 → 不构成 formulation confound，已消解\n3. **R2-W4 Related Work 论文堆砌**：R1 反驳 page constraints 下 2/3 column 是 norm，thematic organization 正确 → 降级为 minor（第一段 citation density 偏高可改善）\n4. **R2-N3 Limitations 格式**：R1 同意事实但降级（30 秒修复）→ 共识为高优先 Should-Fix (W1)\n5. **R1-W5 ICC 外推**：R2 引用 Appendix A conservative lower bound 论证 → 已消解，无需修改\n\n---\n\n## Questions for Authors\n\n1. 是否可在 rebuttal 期间为 key repo-level comparison（至少 CLS vs CWM at 8B）补充到 ≥3 seeds？\n2. TRAJ 如果使用 ~70K 聚合数据训练（per-test labels → variant-level），function-level TOST equivalence 是否仍然成立？\n3. 对所有配置统一使用 final-epoch checkpoint 后，core conclusions 是否仍成立？\n4. 论文是否考虑过在更大规模（如 32B inference-only）验证 CWM formulation 的 repo-level 表现？\n5. Repo-level oracle ensemble 结果是什么？如果 repo-level error complementarity 不存在，routing motivation 不成立。\n\n---\n\n## Missing References\n\n1. **ScratchPad** (Nye et al., 2021) — execution trace generation foundational work\n2. **REDO** (Chen et al., 2024, arXiv:2410.09117) — execution-free runtime error detection\n3. **CodeExecutor** (Liu et al., 2024, ACL) — code execution simulation\n4. **Math-Shepherd** (Wang et al., 2024) / **OmegaPRM** (Luo et al., 2024) — process reward model training\n5. **Constrained decoding** 代表性工作 — 与 Section 4.4 CWM format compliance 讨论相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：已跳过**（用户未提交至 paperreview.ai）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Excitement | 3/5 | 2.5/5 | 2.75/5 |\n| Reproducibility | 4/5 | 3.5/5 | 3.75/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**理由**：\n\n论文提出了一个重要的研究问题并展示了值得认可的统计方法论意识。Function-level 的等价性结论有充分证据支撑（5 seeds, TOST, clustered bootstrap），failure mode taxonomy 和 efficiency 分析有实用价值。\n\n但 \"controlled comparison\" 这一核心定位被多个未控制的混淆因素实质性削弱：(1) TRAJ 训练数据量差异 175×，Abstract \"identical data\" 构成 overclaim；(2) repo-level 多数配置仅 1-2 seeds，seed variance 可达 7-8pp，远超 formulation 间差异的可靠检测范围；(3) NaN validation loss 导致 checkpoint 选择策略不一致，与 \"formulation-inherent\" causal claim 冲突；(4) 4-8B LoRA fine-tuned CWM 的结论不能外推为 generation formulation 的普遍判断。\n\n主要发现的非显然性有限：CWM 在 long-output + exact match 条件下失败可从 formulation first principles 推导；function-level equivalence 符合 \"short output → generation ≈ classification\" 的直觉。\n\n建议作为 Findings 考虑接收，前提是解决 N1-N4 的核心 confound 问题并适当弱化 repo-level claims 的 strength。若能在 rebuttal 期间补充多种子实验和统一 checkpoint 的 ablation，论文质量将显著提升。\n\n---\n\n## Detailed Comments by Section\n\n**Abstract**: 数据密度过高（W2）。\"identical data\" 表述需修正（N1）。建议精简至 2-3 个关键数字。\n\n**Introduction**: Contribution #4 中 re-repair pilot 应移除或降级（W5）。\"No single formulation dominates\" 需修正为更精确的 framing（W3）。\n\n**Method**: Oracle Accuracy-Utility Framework 使用 function-level ICC=0.191，Appendix 已论证为 conservative lower bound（已消解），但建议同时报告 repo-level ICC 下的结果。\n\n**Experiments (Function-level)**: 稳健，统计方法论到位。TOST ±2pp margin sensitivity 应在主文补充（W7）。\n\n**Experiments (Repo-level)**: 论文最核心但证据最薄弱的部分。N2（统计效力）、N3（checkpoint confound）、N4（scale generalizability）共同削弱。\"Cross-model validation confirms formulation-inherent\" 的 claim 需大幅弱化：CWM eval seq_length 不一致（W4）、checkpoint 策略不一致（N3）、context length asymmetry 未完全消除（W9，虽影响 <3%）。\n\n**Related Work**: 总体组织合理（thematic grouping），但第一段 citation density 过高。缺失 5 篇重要引用（W8）。\n\n**Conclusion**: \"complexity-aware routing\" 缺乏 empirical support（W6）。Limitations 需改为独立 section（W1）。\n\n**Appendix**: 内容充实，消融覆盖面广。Extended Limitations 的坦诚值得认可。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# Round 3 审稿报告（Fresh Review）\n\n**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\n**Venue**: EMNLP 2026 (ACL Rolling Review)\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+写作质量+格式合规）\n**外部审稿**: 已跳过（用户未提交）\n\n---\n\n## Summary\n\n本文对三种 execution-free code verification formulation（per-test classification CLS、execution output generation CWM、trajectory-level patch scoring TRAJ）进行了系统对比，使用两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度级别（function-level, repo-level）、多个随机种子。核心发现：function-level 三种 formulation 准确率等价（TOST $p=0.007$）；repo-level CLS 显著优于 CWM（19-26pp）；CWM 在 repo-level 因 format collapse 失效（51-74% 不可解析输出）；CLS 和 CWM 存在互补错误模式（oracle ensemble 90.63%）。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且定义清晰。** 三种 execution-free verification formulation 之间缺乏系统比较，论文将工程选择问题提升为科学问题，对 LLM-based repair pipeline 从业者有直接实用价值。[R1-S1, R2 共识]\n\n**S2. 统计方法论水准高。** 使用 TOST 等价性检验（非仅 NHST）、clustered bootstrap（尊重 problem-level 相关结构）、ICC 量化 within-problem correlation、margin sensitivity analysis。这在 NLP 实证研究中属于高标准。[R1-S2, R2 优势 #1]\n\n**S3. Function-level 结果稳健。** 5 seeds × 2 model families × 3 formulations 的 function-level 比较有充分统计效力，TOST 等价性结论和 clustered bootstrap CI 互相印证。[R1-S3]\n\n**S4. Failure mode taxonomy 有实用价值。** Table 4 的三种 failure mode 分类（format collapse, decision collapse, aggregation penalty）和 Appendix G 的 qualitative error analysis 为从业者选择 formulation 提供了实用参考。[R1-S4, R2 优势 #3]\n\n**S5. 对自身局限的透明度。** 论文明确讨论了 NaN validation loss、单种子限制、val-test distribution mismatch、eval seq_length sensitivity 等问题。这种坦诚在投稿论文中不常见。[R2 优势 #2]\n\n**S6. 消融实验覆盖面广。** LoRA rank ablation、majority voting、sequence-length ablation、relaxed matching、constrained decoding 讨论，涵盖了审稿人可能提出的多数 \"what if\" 问题。[R2 优势 #4]\n\n**S7. Efficiency 分析有部署价值。** CLS 217× throughput 和 CLS-TRAJ crossover 分析（|T| ≈ 50）提供了实用的工程指导。[R2 优势 #5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] TRAJ 训练数据量差异 175× 根本性破坏 \"controlled comparison\" 框架** [R2 提出, R1 AGREE]\n\nCLS/CWM 使用 ~70K 训练样本，TRAJ 仅 ~400 实例（175× 差异）。Abstract 声称 \"training on identical data with controlled model sizes\"，在 effective training examples 数量上构成 overclaim。所有涉及 TRAJ 的结论（包括 TOST equivalence、per-test vs trajectory-level 的 contribution #4）无法可靠归因于 formulation 差异而非数据量差异。R1 补充指出此数据不对称部分是 formulation-inherent（TRAJ 按设计只有 patch-level 标注），但论文应明确讨论这一点。\n\n*建议*：(1) Abstract/Introduction 明确披露数据量差异；(2) 将 TRAJ 降级为 secondary baseline 而非 controlled comparison 的平等 formulation；(3) 或在 function-level 做 data-size matched 实验（downsample CLS 到与 TRAJ 相同数量）。\n\n**N2 [critical] Repo-level 统计效力严重不足** [R1 提出, R2 AGREE]\n\n多数 repo-level 配置仅 1-2 个 seed。DeepSeek CLS 跨 seed/config 波动 7.68pp，Qwen3-4B CLS 仅 seed 42。在如此高的 seed variance 下，1-2 seed 无法区分 formulation effect 和 seed noise。但主文 \"CLS achieves 19-26pp higher accuracy\"、\"divergence is formulation-inherent\" 的表述暗示了远超实际证据的 robustness。\n\n*建议*：增加到 ≥3 seeds per key comparison，或显著弱化 repo-level 结论表述为 \"preliminary observations\"。\n\n**N3 [critical] NaN validation loss 导致 checkpoint 选择策略跨配置不一致** [R2 提出, R1 AGREE]\n\nDeepSeek s123 + 所有 CWM runs 出现 NaN validation loss，被迫使用 final epoch checkpoint，而其他配置使用 val-best。论文 Section 4.4 自己承认 \"Val-based selection optimizes per-test accuracy, which biases toward predicting pass\"，但 \"Cross-model validation\" 段落仍用包含此 confound 的结果声称 \"confirms the divergence is formulation-inherent\"。这构成 internal inconsistency。\n\n*建议*：(1) 对所有配置统一报告 final-epoch checkpoint 的结果作为 ablation；(2) 修复 NaN loss 根因（truncate preprocessing）。\n\n**N4 [critical] CWM 4-8B LoRA 结论不能外推为 generation formulation 的普遍判断** [R1, R2 独立发现]\n\n论文承认 \"Our CWM baseline is a LoRA fine-tuned variant, not a reproduction of the 32B Code World Model\"，但叙事层面仍做 formulation-general 的 claim。CWM 的失败可能反映 (a) formulation-inherent 属性（论文所称），(b) 4-8B 容量不足（原始 CWM 32B），或 (c) 缺乏 execution trace mid-training。论文仅在 4-8B 范围验证了 (b)，远不足以排除。\n\n*建议*：将所有 CWM 结论限定为 \"at 4-8B LoRA fine-tuning scale\"；讨论 execution trace mid-training 可能改变结论的可能性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [high-priority] Limitations 不是独立 section，有 desk reject 风险** [R2 提出, R1 AGREE on fact]\n\n当前是 Conclusion 中的 `\\paragraph{Limitations and future work.}`，ARR 要求独立 `\\section*{Limitations}` 置于 Conclusion 之后 References 之前。R1 认为 30 秒 LaTeX 修复不构成 critical，但投稿前必须修复。\n\n**W2 Abstract 数据密度过高** [R2 提出, R1 AGREE]\n\n~211 词内塞入大量具体数字，审稿人 30 秒内难以提取核心 message。建议保留 2-3 个关键数字，其余定性描述。\n\n**W3 \"No single formulation dominates\" framing 与证据不符** [R1 提出, R2 AGREE]\n\nCLS 在所有条件下 ≥ 其他 formulation。\"No single formulation dominates\" 仅在非 accuracy 维度（error complementarity）成立，当前表述易误导 practitioners。建议改为更精确的 framing。\n\n**W4 CWM 跨模型 eval seq_length 不一致** [R2 提出, R1 AGREE]\n\nQwen3 CWM eval 8192, DeepSeek CWM eval 4096。论文承认 \"not directly comparable\" 但仍声称 cross-model validation。与 N3 的 checkpoint confound 共同削弱 \"formulation-inherent\" causal claim。\n\n**W5 Re-repair pilot (n=44, power<0.3) 不足以作为 contribution** [R1, R2 独立发现]\n\nn=44, p=0.42, power ~0.3。应从 contribution list 移除或降级为 \"inconclusive preliminary result\"。\n\n**W6 Oracle ensemble (90.63%) 缺乏 practical routing 验证** [R1, R2 独立发现]\n\nOracle 是 upper bound。Conclusion 提出 \"complexity-aware routing\" 但未实现任何 routing 机制。建议弱化 claim 或实现 simple routing baseline。\n\n**W7 TOST ±2pp margin sensitivity 主文披露不足** [R1 提出, R2 AGREE]\n\n±1pp → 不等价 (p=0.871), ±2pp → 等价 (p=0.007)。核心 equivalence 结论高度 margin-sensitive。主文应增加 sensitivity 结果和 margin 选择 rationale。\n\n**W8 缺失重要相关工作** [R1, R2 交叉确认]\n\nR1: ScratchPad (Nye et al., 2021), Math-Shepherd/OmegaPRM, CodeExecutor (Liu et al., 2024 ACL)。R2: REDO (Chen et al., 2024), constrained decoding 文献。\n\n**W9 推理时 context length asymmetry** [R1 提出, R2 REBUT 并降级]\n\nCWM ~1536 tokens vs CLS 5120-8192 tokens。R2 提供论文 Appendix B 证据：matched-context ablation (CLS@2048 vs CWM@2048) 显示 input context 差异仅解释 <3% 的 gap。R1 未反驳。降级为 Should-Fix，建议补充说明 effective input tokens 差异。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识（独立发现 + 交叉确认）：\n\n1. **Repo-level 统计效力不足**（N2）：证据最薄弱的环节恰是论文最核心的贡献\n2. **\"Controlled comparison\" 被多个 confounds 削弱**（N1, N3, N4）：TRAJ 数据量 175×、checkpoint 不一致、CWM capacity 限制\n3. **Re-repair pilot 证据不足**（W5）：n=44 不支撑 contribution claim\n4. **Oracle routing 无实际验证**（W6）：upper bound ≠ 可行性\n5. **CWM 结论需限定规模**（N4）：4-8B LoRA ≠ formulation 普遍判断\n\n## Reviewer Divergence [REBUT]\n\n以下分歧已在交叉回应中解决：\n\n1. **R1-N1 context length asymmetry**：R1 列为 critical，R2 REBUT 引用 Appendix B 消融证据（<3%），R1 未反驳 → 降级为 Should-Fix (W9)\n2. **R1-N3c LR 4× 差异**：R2 正确指出同一模型内 CLS/CWM 使用相同 LR，跨模型差异是标准做法 → 不构成 formulation confound，已消解\n3. **R2-W4 Related Work 论文堆砌**：R1 反驳 page constraints 下 2/3 column 是 norm，thematic organization 正确 → 降级为 minor（第一段 citation density 偏高可改善）\n4. **R2-N3 Limitations 格式**：R1 同意事实但降级（30 秒修复）→ 共识为高优先 Should-Fix (W1)\n5. **R1-W5 ICC 外推**：R2 引用 Appendix A conservative lower bound 论证 → 已消解，无需修改\n\n---\n\n## Questions for Authors\n\n1. 是否可在 rebuttal 期间为 key repo-level comparison（至少 CLS vs CWM at 8B）补充到 ≥3 seeds？\n2. TRAJ 如果使用 ~70K 聚合数据训练（per-test labels → variant-level），function-level TOST equivalence 是否仍然成立？\n3. 对所有配置统一使用 final-epoch checkpoint 后，core conclusions 是否仍成立？\n4. 论文是否考虑过在更大规模（如 32B inference-only）验证 CWM formulation 的 repo-level 表现？\n5. Repo-level oracle ensemble 结果是什么？如果 repo-level error complementarity 不存在，routing motivation 不成立。\n\n---\n\n## Missing References\n\n1. **ScratchPad** (Nye et al., 2021) — execution trace generation foundational work\n2. **REDO** (Chen et al., 2024, arXiv:2410.09117) — execution-free runtime error detection\n3. **CodeExecutor** (Liu et al., 2024, ACL) — code execution simulation\n4. **Math-Shepherd** (Wang et al., 2024) / **OmegaPRM** (Luo et al., 2024) — process reward model training\n5. **Constrained decoding** 代表性工作 — 与 Section 4.4 CWM format compliance 讨论相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：已跳过**（用户未提交至 paperreview.ai）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Excitement | 3/5 | 2.5/5 | 2.75/5 |\n| Reproducibility | 4/5 | 3.5/5 | 3.75/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**理由**：\n\n论文提出了一个重要的研究问题并展示了值得认可的统计方法论意识。Function-level 的等价性结论有充分证据支撑（5 seeds, TOST, clustered bootstrap），failure mode taxonomy 和 efficiency 分析有实用价值。\n\n但 \"controlled comparison\" 这一核心定位被多个未控制的混淆因素实质性削弱：(1) TRAJ 训练数据量差异 175×，Abstract \"identical data\" 构成 overclaim；(2) repo-level 多数配置仅 1-2 seeds，seed variance 可达 7-8pp，远超 formulation 间差异的可靠检测范围；(3) NaN validation loss 导致 checkpoint 选择策略不一致，与 \"formulation-inherent\" causal claim 冲突；(4) 4-8B LoRA fine-tuned CWM 的结论不能外推为 generation formulation 的普遍判断。\n\n主要发现的非显然性有限：CWM 在 long-output + exact match 条件下失败可从 formulation first principles 推导；function-level equivalence 符合 \"short output → generation ≈ classification\" 的直觉。\n\n建议作为 Findings 考虑接收，前提是解决 N1-N4 的核心 confound 问题并适当弱化 repo-level claims 的 strength。若能在 rebuttal 期间补充多种子实验和统一 checkpoint 的 ablation，论文质量将显著提升。\n\n---\n\n## Detailed Comments by Section\n\n**Abstract**: 数据密度过高（W2）。\"identical data\" 表述需修正（N1）。建议精简至 2-3 个关键数字。\n\n**Introduction**: Contribution #4 中 re-repair pilot 应移除或降级（W5）。\"No single formulation dominates\" 需修正为更精确的 framing（W3）。\n\n**Method**: Oracle Accuracy-Utility Framework 使用 function-level ICC=0.191，Appendix 已论证为 conservative lower bound（已消解），但建议同时报告 repo-level ICC 下的结果。\n\n**Experiments (Function-level)**: 稳健，统计方法论到位。TOST ±2pp margin sensitivity 应在主文补充（W7）。\n\n**Experiments (Repo-level)**: 论文最核心但证据最薄弱的部分。N2（统计效力）、N3（checkpoint confound）、N4（scale generalizability）共同削弱。\"Cross-model validation confirms formulation-inherent\" 的 claim 需大幅弱化：CWM eval seq_length 不一致（W4）、checkpoint 策略不一致（N3）、context length asymmetry 未完全消除（W9，虽影响 <3%）。\n\n**Related Work**: 总体组织合理（thematic grouping），但第一段 citation density 过高。缺失 5 篇重要引用（W8）。\n\n**Conclusion**: \"complexity-aware routing\" 缺乏 empirical support（W6）。Limitations 需改为独立 section（W1）。\n\n**Appendix**: 内容充实，消融覆盖面广。Extended Limitations 的坦诚值得认可。"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-19T03:04:19.052547+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4773
}
```

</details>

---


### Assistant

_source line 227 · 2026-05-19T03:04:26.214165+00:00_

审稿报告已投递至 Research Director。

**Round 3（Fresh Review）审稿完成。** 汇总：

- **Overall: 3.0（Findings）**，R1 和 R2 完全一致
- **4 个 Must-Fix**：TRAJ 数据量 175× 差异、repo-level 统计效力不足、checkpoint 选择不一致、CWM 4-8B 结论不可外推
- **9 个 Should-Fix**：Limitations 格式、Abstract 过密、framing 不精确、CWM eval seq_length 不一致、re-repair pilot 证据不足、oracle routing 未验证、TOST margin sensitivity 披露不足、缺失引用、context length 补充说明
- **8 个 Minor**
- **外部审稿**：已跳过

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 228 · 2026-05-19T03:04:28.951382+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

**同意 R2 的 9/10 个点**：
- **N1 [AGREE]** — TRAJ 175× 数据差异是我 Round 1 遗漏的关键 confound，与我的 context-length 和 checkpoint confound 共同瓦解 "controlled comparison" claim
- **N2 [AGREE]** — NaN validation loss 的 checkpoint confound 与我的 N3(b) 一致，补充指出论文存在 internal inconsistency（承认 confound 但仍用受污染数据做 causal claim）
- **N3 [AGREE substance, REBUT severity]** — 格式确需修复，但 30 秒 LaTeX 改动不应与方法论 critical issues 并列
- **N4 [AGREE]** — 与我的 N3(d) 一致
- **W1-W3, W5-W6 全部 AGREE**

**唯一部分反驳**：
- **W4 [REBUT]** — Related Work 在 8 页限制下有合理的 thematic organization，称整体为"论文堆砌"不准确，但第一段 citation density 确实偏高

**关键新发现**：整合 R2 的 N1 后，论文的 "controlled comparison" claim 面临 **4 个累积 confound**（TRAJ 数据量 175×、input context 3-5×、checkpoint selection、eval seq_length 跨模型不一致），使得标题中 "Controlled" 的可靠性实质上不成立。Overall 维持 3 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 229 · 2026-05-19T03:04:41.063614+00:00_

审稿报告已投递至 Research Director。Round 3 圆桌审稿完成。

**最终结果摘要：**

**Overall: 3.0 (Findings)**，两位 Reviewer 完全一致。

**4 个 Must-Fix：**
1. TRAJ 训练数据量差异 175×，"identical data" overclaim
2. Repo-level 统计效力不足（多数配置 1-2 seeds，variance 7-8pp）
3. NaN validation loss 导致 checkpoint 选择策略不一致
4. CWM 4-8B LoRA 结论不能外推为 formulation 普遍判断

**9 个 Should-Fix：** Limitations 格式（desk reject 风险）、Abstract 数据过密、"No single formulation dominates" framing 不准确、CWM eval seq_length 跨模型不一致、re-repair pilot 证据不足、oracle routing 未验证、TOST margin sensitivity 披露不足、缺失 5 篇引用、context length asymmetry 补充说明。

**核心判断：** Function-level 结果稳健（S2-S3），failure mode taxonomy 和 efficiency 分析有实用价值（S4, S7），但 "controlled comparison" 核心定位被 4 个累积 confound 实质性削弱。建议 Findings 接收，前提是解决 N1-N4 并弱化 repo-level claims。

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 24

## Round 24

64 recorded events


### User

_source line 230 · 2026-05-19T08:19:17.843048+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2025-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-19T08:19:24.300205+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-19T08:19:24.351394+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-19T08:19:28.017407+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-19T08:19:28.017778+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-19T08:19:28.570958+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,TodoWrite",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,TodoWrite",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-19T08:19:28.571324+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-19T08:19:34.700858+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 238 · 2026-05-19T08:19:35.708206+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (216 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T07:07:07Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 216 个实验 — ALLOCATED 1, DONE 200, PREPARING 14, RUNNING 1\n**DONE 分布**: failed 47, killed 26, negative 7, success 120\n\n### GPU 占用\n- **实际运行**: 1 张 — seetacloud-westd-4x5090:cuda:0(qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval)\n\n### 💾 磁盘余量\n- **seetacloud-westd-4x5090**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 436G/879G 可用（已用 48%）\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval` | seetacloud-westd-4x5090 | cuda:0 | 778328 | `…air-verifier/qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval.log` |\n\n### 📌 最近完成 (top 5)\n- `exp-downsample-cls-func-v3-eval` [failed] — 2026-05-19T07:07:03 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `exp-downsample-cls-func-v3` [success] — 2026-05-19T06:57:21\n- `deepseek-cwm-repo-s123` [failed] — 2026-05-19T04:38:19 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `repo-level-3shot-baseline` [success] — 2026-05-19T04:36:55 — CORRECTED: initial
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 239 · 2026-05-19T08:19:35.759053+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-19T08:19:36.916152+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-19T08:19:36.966973+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-19T08:19:42.690254+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on my web search, I found several results related to ACL conferences and ARR submissions, 
…[truncated 1515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 6931
}
```

</details>

---


### Tool call

_source line 243 · 2026-05-19T08:19:47.588364+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2025 2026 submission guidelines page limits formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2025 2026 submission guidelines page limits formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-19T08:19:48.443295+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR cycle May June 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 commitment deadline ARR cycle May June 2025"
  }
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-19T08:19:48.946037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-19T08:19:49.448886+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\traj}{\textsc{Traj}}
26	\newcommand{\fone}{F\textsubscript{1}}
27	\newcommand{\pp}{\,\text{pp}}
28	
29	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Controlled Empirical Study}
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{abstract}
36	
37	\input{introduction}
38	
39	\begin{figure*}[t]
40	\centering
41	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
42	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
43	\label{fig:reformulation}
44	\end{figure*}
45	
46	\input{method}
47	
48	\input{experiments}
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
53	\caption{Gap amplification from function-level to repo-level complexity. Function-level: \cls{}--\cwm{} gap is 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B (2 matched seeds, bootstrap $p{<}.01$). Repo-level same-size 4B: the gap explodes to 25.59\pp{}, with \cwm{} falling below the majority baseline (72.96\%).}
54	\label{fig:scaling_gap}
55	\end{figure}
56	
57	
58	\input{related_work}
59	
60	\input{con
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-19T08:19:49.449355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-19T08:19:49.700746+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair can be formulated as per-test binary classification (\cls{}), execution output generation (\cwm{}), or trajectory-level patch scoring, yet no controlled comparison exists across formulations. We evaluate all three on the same source data with formulation-appropriate label granularity at controlled model sizes (4--8B LoRA fine-tuning).
3	
4	At function level, formulations achieve near-equivalent accuracy (\cls{} 88.4\% vs.\ \cwm{} 87.2\% at 4B, 5 seeds; Two One-Sided Tests (TOST) confirm variant-level equivalence between per-test and trajectory formulations at $p{=}0.007$). At repository level, divergence amplifies to 19--26\pp{}, with \cwm{} falling below majority baseline due to format non-compliance and output space complexity. Cross-model validation (Qwen3, DeepSeek-Coder) confirms this pattern is consistent across both families but model-contingent in magnitude.
5	
6	Two findings generalize. First, per-test classification provides diagnostic granularity (which tests fail) at comparable accuracy at function level, with a configuration-dependent aggregation cost at repository level and the advantage concentrating in multi-failure instances. Second, formulations exhibit complementary errors (oracle ensemble: 90.63\%). \cls{} achieves the highest or equivalent accuracy across conditions, but aggregation penalty and error complementarity motivate complexity-aware routing.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-19T08:19:49.701286+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-19T08:19:53.719909+00:00_

Web search results for query: "EMNLP 2026 commitment deadline ARR cycle May June 2025"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the search results, here's the information about EMNLP 2026 commitment deadline in the ARR cycle context:

## EMNLP 2026 Commitment Deadline

The EMNLP 2026 commitment deadline is August 2, 2026. This applies to papers that have received reviews and a meta-review from ARR.

## ARR 2026 May Cycle Submission

The ARR submission deadline (long & short papers) is May 25, 2026. Papers must be submitted, at latest, by the ARR 2026 May cycle, and papers that have receiv
…[truncated 514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 5276
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-19T08:19:54.218687+00:00_

Web search results for query: "ACL Rolling Review 2025 2026 submission guidelines page limits formatting requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Submission and Style Guidelines - COLING 2025","url":"https://coling2025.org/calls/submission_guidlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2025-2026:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. For short papers, similar guidelines apply with fewer pages permitted.

## Formatting Requirements

All long, short, and theme papers must follow the ACL Author Guidelines. Mor
…[truncated 1119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 6630
}
```

</details>

---


### Tool result

_source line 252 · 2026-05-19T08:19:55.340961+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (216 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T07:07:07Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 216 个实验 — ALLOCATED 1, DONE 200, PREPARING 14, RUNNING 1\n**DONE 分布**: failed 47, killed 26, negative 7, success 120\n\n### GPU 占用\n- **实际运行**: 1 张 — seetacloud-westd-4x5090:cuda:0(qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval)\n\n### 💾 磁盘余量\n- **seetacloud-westd-4x5090**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 436G/879G 可用（已用 48%）\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval` | seetacloud-westd-4x5090 | cuda:0 | 778328 | `…air-verifier/qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval.log` |\n\n### 📌 最近完成 (top 5)\n- `exp-downsample-cls-func-v3-eval` [failed] — 2026-05-19T07:07:03 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `exp-downsample-cls-func-v3` [success] — 2026-05-19T06:57:21\n- `deepseek-cwm-repo-s123` [failed] — 2026-05-19T04:38:19 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `repo-level-3shot-baseline` [success] — 2026-05-19T04:36:55 — CORRECTED: initial
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 5639
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-19T08:20:03.608070+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'in_progress', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'pending', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'pending', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'in_progress', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'pending', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'pending', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-19T08:20:03.608590+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 255 · 2026-05-19T08:20:05.630180+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits (long paper, short paper), formatting template, anonymity rules, appendix rules, deadline dates (ARR submission, commitment), responsible NLP checklist requirements, any special rules."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits (long paper, short paper), formatting template, anonymity rules, appendix rules, deadline dates (ARR submission, commitment), responsible NLP checklist requirements, any special rules."
  }
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-19T08:20:06.888539+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-19T08:20:07.090729+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a controlled comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic comparison of these three formulations across two model families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our results reveal a three-layer structure in the verification desi
…[truncated 3466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-19T08:20:07.091567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-19T08:20:07.142146+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 260 · 2026-05-19T08:20:10.779182+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers:** 8 pages (9 pages for camera-ready after acceptance)
- **Short Papers:** 4 pages (5 pages for camera-ready after acceptance)

## Formatting & Templates
Submit according to "ARR submission requirements" including paper submission templates available on the ACL Rolling Review website.

## Anonymity Rules
The reviewing process maintains double-blind standards: reviewers cannot identify authors, and authors cannot see reviewers or reviews. "However, authors will be given the option through ARR to make their anonymized submitted articles publicly visible." Two-way anonymized review instructions apply.

## Appendix/Supplementary Materials
Optional supplementary materials, appendices, software, and data are permitted under ARR guidelines.

## Key Deadlines
- **ARR Submission (May cycle):** May 25, 2026
- **Reviewer Registration:** May 27, 2026
- **EMNLP Commitment:** August 2, 2026
- **Camera-ready Due:** September 20, 2026

All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth").

## Responsible NLP Requirements
Authors must complete the "responsible NLP research checklist" and address limitations sections. Papers must comply with ACL's Publication Ethics Policy and ARR's Ethics Policy.

## Special Rules
- Authors must declare intended conference commitment at ARR submission time
- Dual submissions prohibited
- Author list modifications disallowed during commitment phase; only author order changes permitted
- All accepted papers require in-person or virtual presentation by registered author

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebFetch",
  "elapsed_ms": 5148
}
```

</details>

---


### Tool call

_source line 261 · 2026-05-19T08:20:15.518640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-19T08:20:15.771374+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two model families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, defaulting to the final epoch checkpoint (affects DeepSeek s123 and all \cwm{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora}. For cross-model validation, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Zero-shot baselines use Qwen3-
…[truncated 17851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 263 · 2026-05-19T08:20:15.771885+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 264 · 2026-05-19T08:20:16.023309+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Scratchpad-based execution trace generation~\cite{nye2021scratchpad} established that intermediate computation steps improve neural execution prediction. Code World Models~\cite{meta2025cwm} predict output strings via 32B mid-training on execution traces; extensions address step-by-step prediction~\cite{maimon2026selfexecution}, code reasoning~\cite{liu2024codemind}, pre-trained execution simulation~\cite{liu2023codeexecutor}, simulation-execution bridging~\cite{lee2026solidcoder}, failure mode analysis~\cite{abdollahi2025demystifying}, and execution-free error detection~\cite{li2024redo}. Alternative formulations include trajectory-level reward models~\cite{shum2025swerm}, chain-of-thought verification~\cite{xu2025patchreasoner}, per-test classifiers~\cite{ni2023lever,chen2023codet}, and learned quality metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} further demonstrate verification value. None compare formulations at controlled capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	Lightman et al.~\cite{lightman2023letsverify} and Uesato et al.~\cite{uesato2022solving} show process-level verification outperforms outcome-level for mathematical reasoning; Math-Shepherd~\cite{wang2024mathshepherd} and OmegaPRM~\cite{luo2024omegaprm} scale process supervision via automated annotation. DreamPRM-Code~\cite{dreamprm2025code} and PRL-Coder~\cite{ye2025prlcoder} apply this to code. Our per-test classification is structurally analogous; TOST confirms per-test--trajectory equivalence ($p = 0.007$); per-test classification matches trajectory-level accuracy at function level with additional diagnostic value.
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-19T08:20:16.023838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 266 · 2026-05-19T08:20:16.074388+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first controlled comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). \cls{} achieves the highest per-test accuracy across all tested conditions; at variant level, aggregation penalty makes the advantage configuration-dependent, motivating complexity-aware routing.
5	
6	At function level, all three formulations achieve near-equivalent accuracy (TOST $p{=}0.007$, 5 seeds). At repository level under our training protocol, divergence amplifies to 19--26\pp{}; cross-model validation confirms this is consistent across both families but model-contingent in magnitude (Qwen3: ${\sim}$5/22\pp{}; DeepSeek: 4--12/25--30\pp{} for \cls{}/\cwm{}). Seed variance and evaluation protocol add further sensitivity (${\sim}$9\pp{} for the same \cwm{} checkpoint).
7	
8	Two properties generalize across models. First, per-test classification provides diagnostic granularity at comparable or better accuracy at function level; at repo level, aggregation penalty is configuration-dependent (1.36--19\pp{}). Second, classification yields 217$\times$ throughput over generation. Error complementarity (oracle ensemble: 90.63\%) further motivates instance-level routing.
9	
10	\section*{Limitations}
11	
12	Most repo-level comparisons use a single seed; training data comprises synthetic mutations~\cite{andrews2005mutation,just2014mutants}. Our \cwm{} baseline uses 4--8B LoRA fine-tuning; the original 32B Code World Model with execution trace mid-training~\cite{meta2025cwm} may exhibit different scaling behavior at repository level. \traj{} training uses variant-level labels (386 instances at repo level vs.\ ${\sim}$70K for \cls{}/\cwm{}); this asymmetry is inherent to the formulation design but limits direct training-data-controlled comparison. Multi-seed replication and complexity-aware routing are natural extensions; a re-repair pilot ($n{=}44$, $p{=}0.42$; Appendix~\ref{app:extended_analysis}(j))
…[truncated 107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 267 · 2026-05-19T08:20:20.606580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 268 · 2026-05-19T08:20:21.109508+00:00_

1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlat
…[truncated 27101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 269 · 2026-05-19T08:20:21.109938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-19T08:20:21.362185+00:00_

1	% === Execution Simulation ===
2	
3	@article{maimon2026selfexecution,
4	  title={Self-Execution Simulation Improves Coding Models},
5	  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},
6	  journal={arXiv preprint arXiv:2604.03253},
7	  year={2026}
8	}
9	
10	@article{meta2025cwm,
11	  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},
12	  author={{FAIR CodeGen team} and Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and Gehring, Jonas and Kahn, Jacob and Kossen, Jannik and Kreuk, Felix and McMilin, Emily and Meyer, Michel and Wei, Yuxiang and Zhang, David and Zheng, Kunhao and others},
13	  journal={arXiv preprint arXiv:2510.02387},
14	  year={2025}
15	}
16	
17	@article{liu2024codemind,
18	  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},
19	  author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh},
20	  journal={arXiv preprint arXiv:2402.09664},
21	  year={2024}
22	}
23	
24	@article{abdollahi2025demystifying,
25	  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
26	  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},
27	  journal={arXiv preprint arXiv:2512.00215},
28	  year={2025}
29	}
30	
31	@article{lee2026solidcoder,
32	  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
33	  author={Lee, Woojin and Huang, Jin-Xia},
34	  journal={arXiv preprint arXiv:2604.19825},
35	  year={2026}
36	}
37	
38	@article{nye2021scratchpad,
39	  title={Show Your Work: Scratchpads for Intermediate Computation with Language Models},
40	  author={Nye, Maxwell and Andreassen, Anders Johan and Gur-Ari, Guy and Michalewski, Henryk and Austin, Jacob and Biber, David and Dohan, David and Lewkowycz, Aito
…[truncated 15240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 271 · 2026-05-19T08:20:21.362545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-19T08:20:21.463239+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: single-seed repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and single-seed constraints.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified unde
…[truncated 4224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-19T08:20:31.821563+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-19T08:20:32.022735+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 275 · 2026-05-19T08:20:32.023351+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 276 · 2026-05-19T08:20:32.073927+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-19T08:20:35.946232+00:00_

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
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
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

_source line 278 · 2026-05-19T08:20:35.996993+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-19T08:20:40.026195+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-19T08:20:40.278184+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 281 · 2026-05-19T08:20:40.429374+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
  }
}
```

</details>

---


### Tool result

_source line 282 · 2026-05-19T08:20:40.580416+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-19T08:20:43.443721+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-19T08:20:43.796790+00:00_

1	issues:
2	# === Round 3 Critical Issues (fresh review) ===
3	
4	- id: "R3-N1"
5	  summary: "TRAJ 训练数据量差异 175×（~400 vs ~70K）破坏 controlled comparison 框架"
6	  category: experiment
7	  severity: critical
8	  status: in_progress
9	  first_raised_round: 3
10	  last_seen_round: 3
11	  mentions:
12	    - round: 3
13	      reviewers: [2]
14	      note: "R2 首次提出。Abstract 'identical data' 构成 overclaim。"
15	    - round: 3
16	      reviewers: [1]
17	      note: "R1 AGREE。数据不对称是 formulation-inherent。"
18	  action_items:
19	    - round: 3
20	      action: "写作: Abstract 'identical data' → 'same source data with formulation-appropriate granularity'"
21	      assigned_to: "paper"
22	      status: in_progress
23	    - round: 3
24	      action: "实验: Downsample CLS function-level 15290→8052 (匹配 TRAJ)，重训+eval TOST"
25	      assigned_to: "agent"
26	      status: in_progress
27	    - round: 3
28	      action: "写作: Limitations 增加 TRAJ 数据量是 formulation-inherent 的说明"
29	      assigned_to: "paper"
30	      status: in_progress
31	  resolution: ""
32	  resolution_round: null
33	
34	- id: "R3-N2"
35	  summary: "Repo-level 统计效力严重不足，多数配置仅 1-2 seeds"
36	  category: experiment
37	  severity: critical
38	  status: in_progress
39	  first_raised_round: 3
40	  last_seen_round: 3
41	  mentions:
42	    - round: 3
43	      reviewers: [1, 2]
44	      note: "两人独立发现。seed variance 可达 7.68pp。"
45	  action_items:
46	    - round: 3
47	      action: "写作: 弱化 'formulation-inherent' → 'observed consistently across both model families'; 强调 cross-model > multi-seed"
48	      assigned_to: "paper"
49	      status: in_progress
50	  resolution: ""
51	  resolution_round: null
52	
53	- id: "R3-N3"
54	  summary: "NaN validation loss 导致 checkpoint 选择策略跨配置不一致"
55	  category: experiment
56	  severity: critical
57	  status: in_progress
58	  first_raised_round: 3
59	  last_seen_round: 3
60	  mentions:
61	    - round: 3
62	      reviewers: [1, 2]
63	      note: "DeepSeek s123 + CWM runs 用 final epoch，其余用 val-best。"
64	  action_ite
…[truncated 10764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 285 · 2026-05-19T08:20:44.049133+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "output_mode": "content",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
    "output_mode": "content",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-19T08:20:44.100780+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 287 · 2026-05-19T08:21:10.301484+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'completed', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'in_progress', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'completed', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'in_progress', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 288 · 2026-05-19T08:21:10.303026+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-19T08:21:43.066082+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + 无限参考文献\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，不计页数，参与审稿\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（包含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n\n### 论文概述\n标题: \"The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\"\n比较三种 execution-free code verification formulations (CLS/CWM/TRAJ) 在两个模型家族、两个复杂度级别上的表现。\n\n### 你需要重点审查的方面\n\n1. **统计方法的恰当性**\n   - TOST 等价检验的 margin 选择（±2pp）是否合理？sensitivity 分析是否充分？\n   - Clustered bootstrap 的实施（114 clusters, 10K resamples）是否恰当？\n   - ICC 分析和 design effect 的使用是否正确？\n   - 多重比较问题是否存在？\n\n2. **实验设计的控制变量**\n   - \"Controlled comparison\" 的声称是否成立？三种 formulation 之间是否有未控制的混杂因素？\n   - 训练数据量差异（CLS/CWM ~70K vs TRAJ ~400-8K）是否破坏了 controlled comparison？\n   - Checkpoint 选择策略不一致（val-best vs final epoch due to NaN loss）对结论的影响？\n   - Seed 数量是否足够支撑统计推断（repo-level 多为 1-2 seeds）？\n\n3. **实验充分性**\n   - 跨模型验证（Qwen3 + DeepSeek）是否足够支撑 generalizability claims？\n   - CWM baseline 用 4-8B LoRA vs 原始 32B mid-trained CWM 的 external validity？\n   - Repo-level n=48 variant-level 评估的统计效力？\n   - Re-repair pilot (n=44) 是否足以作为 contribution？\n\n4. **Claims 与证据的匹配度**\n   - 每条 contribution 是否有充分的实验支撑？\n   - Causal language 的使用是否过强（\"formulation-inherent\" 等）？\n   - Cross-model 结论在 single-seed 条件下的可靠性？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n4. **Questions** (需要作者回答的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (使用 EMNLP 2026 ARR 评分: 1-5 scale)\n7. **Confidence** (1-5)\n\n审稿标准参考 EMNLP 2026 ARR:\n5 = Consider for Award（约前2.5%）\n4.5 = Borderline Award\n4 = Conference（可被主会议接收）\n3.5 = Borderline Conference\n3 = Findings（可被Findings接收）\n2.5 = Borderline Findings\n2 = Resubmit next cycle\n1.5 = Resubmit after next cycle\n1 = Do not resubmit",
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + 无限参考文献\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，不计页数，参与审稿\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（包含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n\n### 论文概述\n标题: \"The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\"\n比较三种 execution-free code verification formulations (CLS/CWM/TRAJ) 在两个模型家族、两个复杂度级别上的表现。\n\n### 你需要重点审查的方面\n\n1. **统计方法的恰当性**\n   - TOST 等价检验的 margin 选择（±2pp）是否合理？sensitivity 分析是否充分？\n   - Clustered bootstrap 的实施（114 clusters, 10K resamples）是否恰当？\n   - ICC 分析和 design effect 的使用是否正确？\n   - 多重比较问题是否存在？\n\n2. **实验设计的控制变量**\n   - \"Controlled comparison\" 的声称是否成立？三种 formulation 之间是否有未控制的混杂因素？\n   - 训练数据量差异（CLS/CWM ~70K vs TRAJ ~400-8K）是否破坏了 controlled comparison？\n   - Checkpoint 选择策略不一致（val-best vs final epoch due to NaN loss）对结论的影响？\n   - Seed 数量是否足够支撑统计推断（repo-level 多为 1-2 seeds）？\n\n3. **实验充分性**\n   - 跨模型验证（Qwen3 + DeepSeek）是否足够支撑 generalizability claims？\n   - CWM baseline 用 4-8B LoRA vs 原始 32B mid-trained CWM 的 external validity？\n   - Repo-level n=48 variant-level 评估的统计效力？\n   - Re-repair pilot (n=44) 是否足以作为 contribution？\n\n4. **Claims 与证据的匹配度**\n   - 每条 contribution 是否有充分的实验支撑？\n   - Causal language 的使用是否过强（\"formulation-inherent\" 等）？\n   - Cross-model 结论在 single-seed 条件下的可靠性？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n4. **Questions** (需要作者回答的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (使用 EMNLP 2026 ARR 评分: 1-5 scale)\n7. **Confidence** (1-5)\n\n审稿标准参考 EMNLP 2026 ARR:\n5 = Consider for Award（约前2.5%）\n4.5 = Borderline Award\n4 = Conference（可被主会议接收）\n3.5 = Borderline Conference\n3 = Findings（可被Findings接收）\n2.5 = Borderline Findings\n2 = Resubmit next cycle\n1.5 = Resubmit after next cycle\n1 = Do not resubmit",
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-19T08:22:06.158830+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23092
}
```

</details>

---


### Tool call

_source line 291 · 2026-05-19T08:22:06.460721+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + 无限参考文献\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，不计页数，参与审稿\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（包含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n\n### 论文概述\n标题: \"The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\"\n比较三种 execution-free code verification formulations (CLS/CWM/TRAJ) 在两个模型家族、两个复杂度级别上的表现。核心发现：function-level 三者等价；repo-level CLS 远优于 CWM（19-26pp gap）；error complementarity 支持 routing。\n\n### 你需要重点审查的方面\n\n1. **新颖性评估**\n   - 研究问题本身是否有足够新颖性？\"Formulation comparison\" 是否构成 paper-worthy contribution？\n   - 发现的新颖性：function-level equivalence 是否是 expected/trivial result？\n   - Repo-level divergence 的发现是否能提供超越 \"CWM doesn't scale well\" 的深层洞察？\n   - 与已有 process vs outcome supervision (Lightman et al., Uesato et al.) 工作的增量在哪里？\n\n2. **Related Work 覆盖度**\n   - 引用是否完整？是否有遗漏的重要相关工作？\n   - 与 Code World Models (Meta, 2025)、SWE-RM (Shum et al., 2025)、PatchReasoner (Xu et al., 2025) 的 positioning 是否准确？\n   - 是否有近期（2025-2026）在 execution simulation 或 code verification 方面的重要工作被遗漏？\n   - 引用密度是否达到 EMNLP 录用论文的水平？\n\n3. **写作质量（严格按照论文写作规范检查）**\n   - Abstract: 是否在 150-250 words？是否回答了四个必答问题？是否数据堆砌？\n   - Introduction: 叙事线是否清晰（背景→问题→不足→方法→贡献）？每条 contribution 是否有对应支撑？\n   - Related Work: 是否有 \"A proposed X. B proposed Y.\" 的堆砌模式？是否做了归纳比较？\n   - **AI 写作痕迹检查**（硬规则）：\n     - 是否有解释性 em-dash (—) 或 en-dash (–)？\n     - 是否有 -ing 短语结尾？\n     - 是否有过度分段？\n     - 是否有 \"Furthermore/Moreover/Additionally\" 连续使用？\n     - 是否有黑名单用词（delve/leverage/utilize/facilitate/myriad/plethora）？\n   - 图表信息密度是否足够？Caption 是否自包含？\n   - 专有名词/缩写是否首次出现时有定义？\n\n4. **完整性检查**\n   - Limitations 是否独立 section（ARR 格式要求）？\n   - Responsible NLP Checklist 是否完整认真？\n   - 论文主线是否统一（Abstract→Intro→Method→Results→Conclusion 一致性）？\n   - 8 页限制是否满足？\n\n5. **格式检查**\n   - ACL template 使用正确性\n   - 表格格式（小数精度、加粗/下划线最优/次优）\n   - 图片可读性（字体≥7pt）\n   - Reference 格式一致性\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n4. **Questions** (需要作者回答的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (使用 EMNLP 2026 ARR 评分: 1-5 scale)\n7. **Confidence** (1-5)\n\n审稿标准参考 EMNLP 2026 ARR:\n5 = Consider for Award（约前2.5%）\n4.5 = Borderline Award\n4 = Conference（可被主会议接收）\n3.5 = Borderline Conference\n3 = Findings（可被Findings接收）\n2.5 = Borderline Findings\n2 = Resubmit next cycle\n1.5 = Resubmit after next cycle\n1 = Do not resubmit",
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + 无限参考文献\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，不计页数，参与审稿\n\n### 论文路径\n`projects/exec-sim-repair-verifier/docs/paper/main.tex`（包含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, appendix.tex, checklist.tex, references.bib）\n\n### 论文概述\n标题: \"The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study\"\n比较三种 execution-free code verification formulations (CLS/CWM/TRAJ) 在两个模型家族、两个复杂度级别上的表现。核心发现：function-level 三者等价；repo-level CLS 远优于 CWM（19-26pp gap）；error complementarity 支持 routing。\n\n### 你需要重点审查的方面\n\n1. **新颖性评估**\n   - 研究问题本身是否有足够新颖性？\"Formulation comparison\" 是否构成 paper-worthy contribution？\n   - 发现的新颖性：function-level equivalence 是否是 expected/trivial result？\n   - Repo-level divergence 的发现是否能提供超越 \"CWM doesn't scale well\" 的深层洞察？\n   - 与已有 process vs outcome supervision (Lightman et al., Uesato et al.) 工作的增量在哪里？\n\n2. **Related Work 覆盖度**\n   - 引用是否完整？是否有遗漏的重要相关工作？\n   - 与 Code World Models (Meta, 2025)、SWE-RM (Shum et al., 2025)、PatchReasoner (Xu et al., 2025) 的 positioning 是否准确？\n   - 是否有近期（2025-2026）在 execution simulation 或 code verification 方面的重要工作被遗漏？\n   - 引用密度是否达到 EMNLP 录用论文的水平？\n\n3. **写作质量（严格按照论文写作规范检查）**\n   - Abstract: 是否在 150-250 words？是否回答了四个必答问题？是否数据堆砌？\n   - Introduction: 叙事线是否清晰（背景→问题→不足→方法→贡献）？每条 contribution 是否有对应支撑？\n   - Related Work: 是否有 \"A proposed X. B proposed Y.\" 的堆砌模式？是否做了归纳比较？\n   - **AI 写作痕迹检查**（硬规则）：\n     - 是否有解释性 em-dash (—) 或 en-dash (–)？\n     - 是否有 -ing 短语结尾？\n     - 是否有过度分段？\n     - 是否有 \"Furthermore/Moreover/Additionally\" 连续使用？\n     - 是否有黑名单用词（delve/leverage/utilize/facilitate/myriad/plethora）？\n   - 图表信息密度是否足够？Caption 是否自包含？\n   - 专有名词/缩写是否首次出现时有定义？\n\n4. **完整性检查**\n   - Limitations 是否独立 section（ARR 格式要求）？\n   - Responsible NLP Checklist 是否完整认真？\n   - 论文主线是否统一（Abstract→Intro→Method→Results→Conclusion 一致性）？\n   - 8 页限制是否满足？\n\n5. **格式检查**\n   - ACL template 使用正确性\n   - 表格格式（小数精度、加粗/下划线最优/次优）\n   - 图片可读性（字体≥7pt）\n   - Reference 格式一致性\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n4. **Questions** (需要作者回答的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (使用 EMNLP 2026 ARR 评分: 1-5 scale)\n7. **Confidence** (1-5)\n\n审稿标准参考 EMNLP 2026 ARR:\n5 = Consider for Award（约前2.5%）\n4.5 = Borderline Award\n4 = Conference（可被主会议接收）\n3.5 = Borderline Conference\n3 = Findings（可被Findings接收）\n2.5 = Borderline Findings\n2 = Resubmit next cycle\n1.5 = Resubmit after next cycle\n1 = Do not resubmit",
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 292 · 2026-05-19T08:22:08.084082+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1623
}
```

</details>

---


### Assistant

_source line 293 · 2026-05-19T08:22:15.968192+00:00_

Round 1 任务已分配：
- **Reviewer 1**（方法严谨性 + 实验设计）— 已派发
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）— 已派发

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 294 · 2026-05-19T08:26:12.126618+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 1 审稿意见

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study"
**审查侧重**: 方法严谨性 + 实验设计
**审稿标准**: ACL ARR (EMNLP 2026)

---

## Summary

This paper compares three execution-free code verification formulations (CLS, CWM, TRAJ) under controlled conditions across two model families and two complexity levels. The main finding is that formulations achieve near-equivalent accuracy at function level but diverge sharply at repository level, with CLS consistently outperforming CWM. The study is well-motivated and addresses a genuine practical gap, but several methodological issues undermine the "controlled comparison" framing: inconsistent checkpoint selection, cross-model evaluation sequence length differences, single-seed repo-level results, and an underjustified TOST equivalence margin.

---

## Strengths

**S1. Practically important and clearly scoped research question.** Practitioners building verification pipelines must choose a formulation; no prior work provides a head-to-head comparison. The paper fills a real gap (§1, Introduction).

**S2. Multi-dimensional experimental design.** The study varies formulation (3), model family (2), model size (2), complexity level (2), and seeds (up to 5). This factorial structure is more informative than the typical single-axis comparison.

**S3. Rigorous statistical framework for the function-level analysis.** Clustered bootstrap (114 clusters, 10K resamples) correctly accounts for within-problem dependence; TOST for equivalence testing is the right tool for the null-result claim; ICC with design effect quantifies correlation structure (§4.4, §4.5). This level of statistical care is rare in NLP empirical papers.

**S4. Thorough failure mode taxonomy.** The identification of three distinct failure modes (format collapse, decision collapse, aggregation penalty) in Table 4 / §4.5, with configuration-dependent assignment, is a genuinely useful contribution for practitioners.

**S5. Honest limitations disclosure.** The paper is commendably transparent about single-seed constraints, NaN validation loss issues, checkpoint selection confounds, and evaluation sequence length differences (§4.5, Appendix F). Many of my concerns below were already flagged by the authors.

**S6. Comprehensive ablation suite.** LoRA rank ablation, majority voting, matched-context sequence length ablation, training data downsampling, and few-shot baselines systematically address obvious confounds (Appendix B).

---

## Weaknesses

### Must-Fix 问题

**N1** [critical] **TOST equivalence margin (±2pp) 缺乏正式论证和敏感性分析**
- 具体位置: §4.4 (Per-Test vs. Trajectory-Level Equivalence)
- 问题: 论文声称 CLS 和 TRAJ 在 function level 具有统计等价性 (TOST p=0.007, ±2pp margin)，但 ±2pp margin 的选择仅以一句话论证："formulation differences below 2pp are unlikely to affect deployment decisions where absolute accuracy dominates the cost-benefit analysis." 在药学 TOST 应用中，equivalence margin 基于临床显著性阈值，有行业标准和历史先例。本文的 ±2pp 是一个 ad hoc 断言，没有基于 deployment cost model 或 decision-theoretic analysis 的支撑。更关键的是，论文缺少 margin 敏感性分析：如果 margin 收窄至 ±1pp，TOST 是否仍然显著？如果 margin 放宽至 ±3pp，结论是否改变？这直接影响 "formulation equivalence at low complexity" 这一核心贡献的可信度。
- 为什么影响接收: 这是四条 contributions 中的第一条。如果 margin 选择不够稳健，该贡献的基础不牢。
- 建议: (1) 报告 TOST 在 ±1pp, ±1.5pp, ±2pp, ±3pp 下的 p 值，展示 equivalence 结论对 margin 的敏感性；(2) 给出 smallest margin at which equivalence holds (即 equivalence bound)；(3) 如果 ±2pp 确实是合理的实践阈值，需要更实质的论证（如验证流水线中 2pp 对下游 repair success rate 的影响量级）。

**N2** [critical] **"Controlled comparison" 声称与实际实验设计之间存在系统性裂隙**
- 具体位置: Title, §1 ("the first systematic comparison"), §4 ("systematically compare"), §4.5
- 问题: 论文的核心卖点是 "controlled comparison"，但多个维度上的控制不完整，且这些不一致性在方向上可能系统性地偏向 CLS：
  - (a) **Checkpoint selection inconsistency**: CLS 使用 val-best checkpoint；CWM 和 DeepSeek s123 因 NaN validation loss 使用 final epoch checkpoint (§4.1)。Checkpoint selection 是 fine-tuning 中对结果影响最大的超参数之一。Table 5 已经展示了 Qwen3-4B 在不同 checkpoint 下 variant-level accuracy 从 64.58% 到 68.75% 的变化。CWM 没有得到 val-best selection 的机会，这可能系统性低估了 CWM 的表现。
  - (b) **Evaluation sequence length asymmetry**: CWM 评估中 Qwen3 使用 8192 tokens，DeepSeek 使用 4096 tokens (§4.5, Table 3 footnote)。论文自己承认这导致 cross-model CWM 数字 "not directly comparable"，且 ~9pp 的 variation 来自 seq_length 差异。但 cross-model validation 恰恰是论文的核心论证策略之一。
  - (c) **Preprocessing differences**: DeepSeek s42 用 drop preprocessing (丢弃 3,405 个长序列)，s123 用 truncate preprocessing (Table 7 footnote)。这引入了 training data composition 差异。
  - (d) **TRAJ training regime**: TRAJ 使用不同的 learning rate (2e-4 vs 5e-5)，远小的训练集 (~400 vs ~70K at repo level)，和 variant-level evaluation (n=48 vs per-test n=9,784)。虽然 downsampling ablation 部分控制了 data volume (Appendix B)，但 lr 差异未控制。
- 为什么影响接收: 如果控制不完整，"formulation-driven" 的因果归因就不可靠。论文目前在某些段落使用因果语言（"formulation-driven rather than data-volume-driven", §4.5），但在其他地方又承认 "single-seed constraints limit causal attribution"（§4.5）。这种不一致会让审稿人质疑核心结论的内部效度。
- 建议: (1) 在 Method 或 Setup 中增加一个显式的 "threats to internal validity" 段落，逐条列出哪些因素被控制、哪些未被控制，以及每个 uncontrolled factor 的可能偏向方向；(2) 将 title 或 framing 从 "controlled" 调整为更精确的措辞（如 "systematic" 或 "matched-capacity"），因为当前多个维度上并非真正 controlled；(3) 修复 NaN validation loss 问题以实现 CWM 的 val-best checkpoint selection，或至少报告 CWM 在不同 epoch checkpoint 下的表现作为 sensitivity check。

**N3** [critical] **Repo-level 统计效力严重不足，n=48 variant-level 结论缺乏可靠性**
- 具体位置: Table 3, §4.5, Table 5 (Appendix D)
- 问题: Repo-level variant-level 评估仅有 n=48 个实例。在 n=48 下：
  - 单个 variant 翻转导致 ~2.08pp accuracy 变化，这与报告的 formulation 差异量级可比（如 CLS Qwen3-8B s42 vs s123 差异为 72.92% vs 81.25%，即 4 个 variants 的差异）
  - Table 3 中 TRAJ 报告 72.92%（Qwen3）和 75.35% ± 5.00（DeepSeek 6 seeds）。5pp 的 seed 标准差在 n=48 下意味着结论高度不稳定
  - CLS Qwen3-8B 的两个 seed 分别得到 72.92% 和 81.25%，8.33pp 的 spread 对应仅 4 个 variant 的差异
  - 论文使用这些 n=48 的结果来做 formulation 之间的排序和比较（如 "CLS variant-level brackets TRAJ"），但没有报告这些比较的 confidence intervals 或 p 值
  - 论文同时在 Table 3 中并列报告 per-test accuracy (n=9784) 和 variant-level accuracy (n=48)，虽然有 footnote 说明，但表格布局容易误导读者将两个精度完全不同的数字直接比较
- 为什么影响接收: Repo-level divergence 是本文第二条核心贡献。如果 variant-level 结论在统计上不可靠，整个 complexity-dependent divergence 的故事线就只能依赖 per-test accuracy——但 per-test accuracy 又被作者自己论证为 "not a reliable proxy for variant-level accuracy" (§4.6)。
- 建议: (1) 报告所有 variant-level 比较的 bootstrap confidence intervals（n=48 下 CI 会很宽，但这恰恰是读者需要看到的）；(2) 进行 power analysis：在 n=48, α=0.05 下能检测到的最小效应量是多少？(3) 明确将 variant-level 结论标记为 preliminary/exploratory，避免在 contributions 列表中将其与 function-level 的 5-seed 结论等量齐观；(4) Table 3 拆分为两个表，分别报告 per-test 和 variant-level 结果，避免混淆。

### Should-Fix 问题

**W1** [warning] **多重比较问题未处理**
- 具体位置: 全文
- 问题: 论文在多个维度上进行了大量统计检验：CLS vs CWM at function level, CLS vs TRAJ (TOST), CLS vs CWM at repo level, scaling gap significance (p=0.0066), 以及 Appendix 中的多个分析。没有应用任何多重比较校正（Bonferroni, Holm, BH-FDR）。虽然主要结论的效应量足够大（repo-level 19-26pp gap 不会被 correction 翻转），但 function-level 的 marginal results（如 scaling gap p=0.0066 在 correction 后可能不再显著）需要明确讨论。
- 建议: 至少在 Statistics 段落中声明哪些是 pre-registered/primary comparisons，哪些是 exploratory analysis，并对 primary comparisons 应用 correction。

**W2** [warning] **CWM baseline 的 external validity 严重受限但论文仍做 formulation-level 归因**
- 具体位置: §1 ("generation-based simulation"), §4.5, Limitations
- 问题: 论文的 CWM baseline 是 4-8B LoRA fine-tuned 模型，而原始 CWM (Meta, 2025) 是 32B 模型经过 execution trace mid-training。Limitations 承认了这一点，但正文中大量使用 "generation formulation" / "output space complexity" 等 formulation-level 的归因语言。当 CWM 在 repo level 失败时，我们无法区分这是 (a) generation formulation 固有的问题，还是 (b) 4-8B 模型容量不足以进行可靠的 string generation，还是 (c) LoRA fine-tuning（而非 mid-training）不足以学习 execution simulation。事实上，论文自己的 scaling 数据（CWM 4B→8B 无改善）更可能指向 (b) 或 (c) 而非 (a)。
- 建议: (1) 在正文中明确区分 "under our training protocol" 和 "formulation-inherent" 的结论；(2) 考虑增加一个更大模型（如 Qwen3-32B NF4 QLoRA）的 CWM 数据点，即使只是 function-level，也能提供 scaling evidence。

**W3** [warning] **Re-repair pilot (n=44) 不应作为 contribution 呈现**
- 具体位置: Abstract ("Second, formulations exhibit complementary errors"), Conclusion, Appendix E(j)
- 问题: Re-repair pilot 仅有 n=44，power ~0.3 for medium effect，p=0.42，effect size ≈ 0。作者自己在 Appendix 中承认这些限制。但 Abstract 和 Conclusion 仍然讨论 "diagnostic granularity" 和 "complexity-aware routing" 作为动机，而唯一的下游验证实验（re-repair）是 negative result。一个 underpowered 的 negative result 既不能作为 positive contribution，也不能作为 evidence against 诊断信息的价值。
- 建议: 将 re-repair pilot 明确标记为 "exploratory/inconclusive"；不在 Abstract 或 Contribution 列表中暗示诊断粒度有下游价值——目前的证据不支持这一方向。

**W4** [warning] **Cross-model "validation" 的力度被夸大**
- 具体位置: §4.5 "Cross-model validation", §1 Contribution 2
- 问题: DeepSeek 的 repo-level 数据是 single-seed，且 CLS 的两个 seed 展现出巨大差异（s42: 82.61%, s123: 74.93%，差 7.68pp）。论文承认这 "conflates seed, preprocessing, and checkpoint selection differences"。在这种条件下使用 "validation" 一词过强。两个模型家族中一个家族的 repo-level 数据高度不稳定，另一个也仅有 1-2 seeds。"Consistent direction" 是一个弱声称（任何 non-trivial effect 在两个样本中都有 ~50% 概率同方向），需要更强的统计检验或更多 seeds 才能称为 "validation"。
- 建议: 将 "cross-model validation" 改为 "cross-model observation" 或 "directional evidence"；在 Contribution 2 中降低语气强度。

**W5** [warning] **Function-level ICC 用于 repo-level oracle analysis 的转移假设不充分**
- 具体位置: Appendix A, §4.4
- 问题: Oracle accuracy-utility analysis (Table 6) 使用 function-level ICC=0.191，但 repo-level ICC=0.3146 (§4.5)。虽然 Appendix A 的 sensitivity 段落论证了 function-level ICC 是 "conservative lower bound"，但主表只展示了 function-level ICC 的结果。读者无法判断结论在 repo-level ICC 下有多少量化差异。此外，function-level ICC 来自完全不同的数据分布（HumanEval+MBPP mutants vs SWE-bench Verified），ICC 的转移可靠性未论证。
- 建议: 在 Table 6 中增加 repo-level ICC=0.3146 下的结果列，让读者看到两个 bound。

### 小问题

**M1** Table 3 的 CLS 8B 和 DeepSeek 列使用 "/" 分隔两个 seed 的值，但 CWM 列只报告一个值。应统一格式或在 caption 中更明确说明。

**M2** §4.5 "matched-context ablation confirms input disparity explains <3% of this gap" — 引用 Appendix B 的数据是 CLS@2048 vs CWM@2048 相差 25.00pp vs full gap 25.59pp。但这个 ablation 只控制了 eval-time context，没有控制 training-time context（CWM 在 training 时的 effective input context 也受限于 generation token budget）。这一区分应明确。

**M3** §3.1 CWM 的 unparseable default 策略 "defaults to the majority class verdict" — 论文应讨论这个选择对结果的方向性影响。当 majority class 是 pass (72.96%) 时，default-to-pass 在高 unparseable rate 下人为推高 CWM accuracy。Table 3 footnote 已经暗示了这一点（parseable-only accuracy 更低），但应在正文中更明确讨论。

**M4** §4.3 scaling analysis 使用 2 matched seeds (42, 123)，但 p 值 0.0066 和 CI [1.80, 2.71] 来自 "3-seed superset (42, 123, 456)"。应明确说明哪个分析使用哪些 seeds。

**M5** References: `maimon2026selfexecution` (2026年), `lee2026solidcoder` (2026年) — 如果这些在投稿截止日前不到3个月发布，根据 ARR policy 不应作为 "prior work"（但可以 cite for context）。需确认时间线。

---

## Questions for Authors

**Q1.** TOST equivalence 在 ±1pp margin 下是否仍然成立？请提供 margin sensitivity 数据。

**Q2.** 是否尝试过为 CWM runs 修复 NaN validation loss 问题以实现 val-best checkpoint selection？如果是，结果如何？如果未尝试，这是技术限制还是时间限制？

**Q3.** Repo-level CLS 的 two Qwen3-8B seeds 差异为 8.33pp (72.92% vs 81.25% variant-level)。作者如何解释同一 formulation 下如此大的 seed variance，并仍然将 formulation 间的差异归因于 formulation choice？

**Q4.** 如果 CWM 使用 constrained decoding 消除 format compliance failures，parseable-only accuracy (38-43%) 仍远低于 majority baseline——但 parseable subset 是否 representative？即 parseable outputs 是否系统性地偏向 harder instances？

**Q5.** Oracle ensemble 90.63% 来自 seed 42 的单次实验。这个数字在其他 seeds 下是否稳定？

---

## Missing References

- **CodeRM / Reward Model for Code**: 论文讨论了 verification formulation 但未引用近期专门做 code reward model 的工作，如 CodeRM (Zhang et al., 2025) 或类似工作。
- **Constrained Decoding**: 论文在 §4.5 讨论 grammar-constrained decoding 但未引用相关方法论文（如 Willard & Louf 2023, "Efficient Guided Generation for LLMs"）。
- **Mutation Testing 代表性**: 论文使用 synthetic mutations 但仅引用了 Andrews et al. (2005) 和 Just et al. (2014)。近年来关于 mutation-real fault coupling 有更新的 meta-analysis。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | Function-level analysis 统计方法扎实；repo-level 分析受限于 n=48, single-seed, 和多个 uncontrolled confounds。"Controlled comparison" 在 repo-level 有系统性裂隙。 |
| Excitement | 3.5/5 | 研究问题实际且重要，failure mode taxonomy 有洞察力，但结论的 generalizability 受限于 2 个模型家族和特定 training protocol。 |

## Overall Assessment

**Overall**: **3 — Findings**

**一句话总结**: 研究问题重要且实验设计有野心，但 "controlled comparison" 的执行在 repo-level 有多个系统性缺陷（checkpoint selection asymmetry, n=48 statistical power, evaluation protocol inconsistency），需要在因果归因语言和 framing 上做实质性调整后方可接收。

**理由**: Function-level 分析是扎实的——5 seeds, clustered bootstrap, TOST equivalence testing 都是正确的工具选择，这部分达到了 conference-level rigor。但 repo-level 分析承载了论文最引人注目的结论（19-26pp divergence），而这部分的统计支撑最薄弱：n=48 variant-level evaluation, 1-2 seeds, inconsistent checkpoint selection, cross-model CWM eval sequence length 不可比。论文的 honest limitations 段落几乎涵盖了我的所有 concerns，但 contributions list 和 abstract 的措辞并未反映这些 caveats 的严重程度。如果作者能 (1) 增加 TOST sensitivity analysis, (2) 在 framing 上从 "controlled" 调整为 "systematic", (3) 为 variant-level results 增加 confidence intervals 和 power analysis, (4) 降低 cross-model "validation" 的语气，这篇论文有潜力达到 conference acceptance。当前状态适合 Findings。

**Confidence**: 4/5 (Quite sure. I tried to check the important points carefully.)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 295 · 2026-05-19T08:26:19.628917+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 296 · 2026-05-19T08:26:22.445693+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**: 给出 Overall 3 (Findings)，Soundness 3/5，Excitement 3.5/5，Confidence 4/5。

三个 Must-Fix 问题：
1. TOST ±2pp margin 缺乏正式论证和敏感性分析，直接动摇第一条 contribution
2. "Controlled comparison" 声称与实际设计存在系统性裂隙（checkpoint selection asymmetry, eval seq_length 不一致, preprocessing 差异, TRAJ training regime 差异）
3. Repo-level n=48 variant-level 评估统计效力严重不足，缺少 confidence intervals 和 power analysis

四个 Should-Fix 问题涉及多重比较校正、CWM external validity、re-repair pilot 不应作为 contribution、cross-model "validation" 措辞过强。

核心判断：function-level 分析扎实（5 seeds, proper statistics），但承载最重要结论的 repo-level 分析在统计支撑上最薄弱。论文的 limitations 段落已经覆盖了大部分问题，但 abstract/contributions 的 framing 未反映这些 caveats 的严重程度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 297 · 2026-05-19T08:26:28.521172+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 27

## Round 27

8 recorded events


### User

_source line 298 · 2026-05-19T08:30:47.036135+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — Round 1 审稿意见

**论文**: "The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study"
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 1. Summary

本文对 execution-free code verification 的三种 formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹级评分）进行了控制实验比较，覆盖两个模型家族（Qwen3-8B、DeepSeek-Coder-6.7B）和两个复杂度级别（function-level、repo-level）。核心发现：function-level 三者统计等价（TOST p=0.007, ±2pp margin）；repo-level CLS 显著优于 CWM（19–26pp gap）；错误互补性支持 ensemble routing。研究设计严谨（统一 seed、统一数据、统一训练配置），统计方法得当（TOST、bootstrap CI、ICC），但新颖性有限且 repo-level 结论的单 seed 可靠性不足。

---

## 2. Strengths

**S1. 严格的控制实验设计。** 本文对训练数据、模型大小、超参数、checkpoint 选择等变量进行了系统控制（Section 3.1），这是该领域许多先前工作缺乏的。使用同一 mutation-based 数据为三种 formulation 构建训练集（Section 2），使得比较结果可信度高。

**S2. 统计方法规范。** 使用 TOST 等价性检验（而非仅用 p-value 证明"无显著差异"）来验证 function-level equivalence 是方法论上的正确选择（Section 3.2, Section 3.4）。Bootstrap CI 和 ICC 分析增加了结论的可靠性。

**S3. 错误互补性分析有实用价值。** Section 3.2 中 oracle ensemble 达到 90.63%（+3.12pp），以及 CLS 偏向 false negatives 而 CWM 偏向 false positives 的互补模式（Appendix H），为 routing/ensemble 策略提供了可操作的依据。

**S4. Failure mode taxonomy 有洞察。** Table 4（Section 3.5）将 CWM repo-level 失败归类为 format collapse、decision collapse、aggregation penalty 三种模式，提供了超越单纯数值对比的诊断性分析。

**S5. 附录内容充实。** Appendices A–I 涵盖 LoRA rank ablation、序列长度消融、prompt baselines、变异类型分布、per-mutation 分析、error breakdown、extended limitations 等，展现了完整的实验工作量。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 新颖性有限："design space" 仅含 3 个离散点，缺乏深层机制洞察。**
- 具体位置：Title, Section 2, Section 5
- 问题：论文标题宣称探索 "Formulation Design Space"，但实际上只比较了 3 种已有的 formulation。这不是一个连续的设计空间，也没有系统地变化设计维度（如输出粒度、loss 函数类型、输出长度约束等）。更关键的是，核心发现的深度不足：
  - Function-level equivalence（Section 3.2）：三种 formulation 在简单任务上表现相当，这是一个相对符合预期的结论——当输出短且结构化时，不同 formulation 的差异自然会缩小。论文用 TOST 量化了这一点，但 insight 本身不令人意外。
  - Repo-level divergence（Section 3.5）：CWM 在 repo-level 退化的主要原因归结为 "format collapse" 和 "longer output difficulty"（Table 4, Section 3.5），这基本等价于说 "生成更长的输出更难"，缺乏更深层的分析（如 CWM 在哪些代码结构/错误类型上系统性失败？是 tokenizer 限制、注意力退化还是训练数据覆盖不足？）。
- 与已有工作的增量：Section 4 引用了 process vs. outcome supervision（Lightman et al., 2023; Uesato et al., 2022）的框架，但论文本质上是在 code 领域重新验证了 "outcome-level supervision 在简单任务上够用，process-level 在复杂任务上有优势" 这一已知结论——只是这里的 "process" 和 "outcome" 被换成了 CWM 和 CLS。论文未充分论证其发现超越了这一已有框架的具体新增量。
- 为什么影响接收：EMNLP 期望 Excitement 分数反映论文对社区的启发性。一个设计空间仅 3 个点、核心发现可从已有文献预测的 empirical study，难以达到 Conference 级别的 excitement threshold。
- 建议修改方向：(1) 深入分析 CWM 失败的机制（按代码结构、依赖深度、变异类型细粒度分解）；(2) 将 "design space" 真正展开为多维度分析（如 output granularity × loss type × context window），而不仅是 3 个点的比较；(3) 更明确地论证相对于 PRM/ORM 文献的具体新发现。

**N2 [critical] Repo-level 核心结论依赖单 seed，统计可靠性不足。**
- 具体位置：Section 3.5, Table 3, Limitations (page 18)
- 问题：论文最重要的发现——CLS 在 repo-level 大幅优于 CWM（19–26pp gap）——在 Table 3 中主要基于单个 seed（Qwen3 primary seed 42）。虽然论文在 Limitations 中诚实承认了这一点（"Most repo-level comparisons use a single seed"），但这严重削弱了核心结论的可信度。SWE-bench Verified 的 test set 约 700 条，单 seed 下的 variance 可能非常大。Appendix B 的 LoRA rank ablation 显示 rank-16 的 2-seed variance 已经不可忽略（Table 6: Acc 从 87.00 到 97.1 across configs），而 repo-level 的 variance 只会更大。
- 论文 Table 2 显示 CLS 和 TRAJ 在 4B 和 8B 上有 2 matched seeds，但 CWM 的 "stagnation" 结论（-0.03pp from 4B to 8B）同样基于有限 seed。Section 3.3 提到 CWM gap 从 ~4pp (s42) 到 ~12pp (s123)——这种跨 seed 差异本身就说明 repo-level 结论对 seed 高度敏感。
- 为什么影响接收：一个以 controlled comparison 为核心卖点的论文，其最关键的 repo-level 结论却缺乏足够的统计重复，构成内部矛盾。审稿人会质疑：如果多 seed 实验推翻了 19–26pp 的 gap 大小（尽管方向可能不变），论文的 framing 和 claims 都需要大幅调整。
- 建议修改方向：至少为 repo-level 的 CLS 和 CWM 各跑 3 个 seed，报告均值和 CI；如果资源不足以做完整重复，应大幅降低 repo-level 结论的 claim 强度（从 "CLS 远优于 CWM" 调整为 "初步证据表明..."），并在 Section 3.5 而非仅在 Limitations 中明确标注单 seed 限制。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] Abstract 数据堆砌，叙事性不足。**
- 具体位置：Abstract (page 1)
- 问题：Abstract 在约 250 words 内包含了至少 7 个具体数字（88.43 vs. 97.25, p<0.007, 0.02–1.24pp, 19–26pp, 90.63%, 217×）。这使 Abstract 读起来像实验结果摘要而非论文叙事。审稿人在 30 秒内难以从这些数字中提取核心价值判断。
- 建议：保留最多 2–3 个关键数字（如 TOST equivalence result 和 repo-level gap），其余用定性描述替代。

**W2 [warning] 合成数据（mutation-based）的外部效度未充分讨论。**
- 具体位置：Section 3.1 (data construction), Section 5 (Conclusion), Limitations
- 问题：全部训练数据基于 mutation operators 合成。虽然论文引用了 Andrews et al. (2005) 和 Just et al. (2014) 关于 mutation 对真实 fault 代理有效性的证据（Conclusion, line reference），但这些经典研究针对的是 software testing 场景，其结论是否可迁移到 LLM training data 场景并不显然。关键问题是：formulation 之间的差异是否可能是 mutation 分布的 artifact？例如，CWM 在 repo-level 的失败可能部分源于 mutation 生成的代码与真实 bug 在结构复杂度上的差异。Limitations 中提到 "synthetic-to-real transfer gap remains untested"（page 18），但未讨论这对 formulation comparison 结论本身的影响。
- 建议：增加一段分析，讨论 mutation 类型分布（Appendix F, Table 12）是否可能系统性地偏向某种 formulation；或在 Limitations 中明确指出 formulation ranking 可能因训练数据来源而变化。

**W3 [warning] Related Work 过于压缩，对 "design space" 论文的 positioning 不够深入。**
- 具体位置：Section 4 (page 8)
- 问题：对于一篇声称探索 "formulation design space" 的论文，Related Work 只占不到一页。三个子领域（Execution Simulation、Process vs Outcome Supervision、Repair/Mutation Testing/Task Framing）各用一段覆盖，缺乏对本文 positioning 的深入讨论。特别是：
  - 与 CodePRM（ACL 2025 Findings）的关系未讨论——CodePRM 也探索了 process-level verification 在 code generation 中的应用。
  - 与 CodeScaler（arxiv 2602.17684, 2026）的关系未讨论——这篇工作直接研究 execution-free reward models 在 test-time scaling 中的应用，与本文主题高度相关。
  - 与 FunPRM（arxiv 2601.22249, 2026）的关系未讨论——function-as-step PRM 与本文的 TRAJ formulation 直接相关。
- 建议：扩展 Related Work，特别是加入上述遗漏工作，并在 Process vs Outcome Supervision 段落中更明确地论述本文相对于 math reasoning PRM 文献的具体新发现。

**W4 [warning] CWM baseline 的忠实度存疑。**
- 具体位置：Section 3.1, footnote 1 (page 1), Appendix E
- 问题：论文使用的 CWM 不是 FAIR 的原始 32B CWM 模型，而是在 4–8B 模型上用相同数据"复现"的版本（Section 3.1: "Our CWM baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model"）。这个"复现"的 CWM 是否准确反映了 CWM formulation 的真实能力？CWM 的原始设计可能依赖于更大模型的能力来进行精确的执行模拟。用 4–8B 模型在有限训练数据上训练 CWM 可能系统性地低估了 CWM formulation 的潜力。
- 虽然控制变量（模型大小、数据）的实验设计目的是公平比较，但如果 CWM formulation 天然需要更大模型容量才能发挥作用，那么在 4–8B 上的比较就不是公平的——它测量的是 "小模型上哪种 formulation 更好"，而非 "哪种 formulation 更好"。
- 建议：在 Discussion 中明确限定结论的适用范围（"在 ≤8B 参数规模下"），或增加与原始 CWM-32B 的零样本/少样本对比作为参考点。

**W5 [warning] 计算成本缺乏系统比较。**
- 具体位置：Section 2.1 (formulation descriptions)
- 问题：三种 formulation 的推理成本差异显著——CLS 输出 1 token，CWM 输出 N tokens，TRAJ 输出 1 token。Section 2.1 提到了这些差异，但正文中缺乏系统的推理成本对比（tokens/sample、wall-clock time、throughput）。对于实际部署决策，成本-精度 tradeoff 是关键因素。Appendix G 提到了部分效率分析（"Inference efficiency"），但这应该在正文中出现。
- 建议：在 Section 3 中增加一个 efficiency comparison subsection，或在 Table 1/2 中增加 throughput 列。

### Minor 问题（不影响接收）

**M1.** Table 1 caption 提到 "LLM-as-judge" 用于 TRAJ 评估，但正文中 TRAJ 的定义（Section 2.1）使用的是 "trajectory-level scoring"。这两个概念的关系需要在 caption 中澄清。

**M2.** Figure 2 信息密度不高——仅 4 个 bar 展示 function-to-repo gap amplification，占据了约 1/4 页空间。建议缩小或与其他分析合并。

**M3.** Section 3.4 (Per-Test vs. Trajectory-Level Equivalence) 引用的 footnote 7 提到 "Seeds 788 and 0 use NF4 quantized inference; the remaining three use bfloat16"——不同 seed 使用不同精度可能引入系统性偏差，虽然影响可能小，但应在正文中说明原因。

**M4.** Appendix I (Extended Limitations) 标题使用 "Extended"——如果 Limitations 部分已经在正文中出现，附录应标注为 "Additional Limitations" 或在正文 Limitations 中引用附录。当前的 "Extended" 暗示正文 Limitations 不完整。

**M5.** Table 2 中 CWM 在 Qwen3-8B 4B→8B 的 scaling 结果为 -0.03pp，但 Section 3.3 第二段将此描述为 "CWM stagnation"。-0.03pp 在统计上与 0 不可区分（Section 3.3 也承认 "we do not claim generation cannot benefit from scale"），措辞可以更中性。

---

## 4. Questions（需要作者回答）

**Q1.** TOST equivalence 的 ±2pp margin 选择依据是什么？论文声称 "formulation differences below 2pp are unlikely to affect deployment decisions"（Section 3.4），但不同应用场景的阈值可能差异很大。如果使用 ±1pp margin，equivalence 是否仍然成立？

**Q2.** Table 3 的 repo-level 结果中，CLS 在 Qwen3-8B 上达到 83.63%，但 TRAJ 达到 84.17%——两者差异不到 1pp。如果 TRAJ 在 repo-level 也能匹配 CLS，那 "CLS 优于 CWM" 的结论是否应更精确地表述为 "CWM 落后于 CLS 和 TRAJ"？

**Q3.** Section 2.2 描述了 CWM 的三种 failure modes（truncation、stray prediction、format compliance collapse），但 Table 4 的 "format collapse" 类别在 CWM (all) 中占比为 N/A，variant-level 为 48–52%。如何理解 CWM (all) 的 N/A——是指所有 CWM 输出都有 format 问题，还是该类别不适用？

**Q4.** 论文使用 mutation-based 数据训练所有模型。如果改用 real bug data（如 SWE-bench 的真实 bug patches），formulation ranking 是否可能改变？特别是 CWM 对真实 bug 的建模能力可能与对 mutation 的建模能力有系统性差异。

**Q5.** Appendix B 的 LoRA rank ablation 只测试了 rank=16 和 baseline（无 LoRA?）。为什么不测试更高 rank（如 32, 64）或 full fine-tuning？对于 CWM 这种需要精确输出的 formulation，LoRA 的低秩约束可能是限制因素。

---

## 5. Missing References

以下近期工作与本文主题直接相关但未被引用：

1. **CodePRM** (ACL 2025 Findings): "Execution Feedback-enhanced Process Reward Model for Code Generation" — 探索 process-level verification 在 code generation 中的应用，与本文的 TRAJ formulation 和 process supervision 讨论直接相关。
2. **CodeScaler** (arxiv 2602.17684, 2026): "Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models" — 直接研究 execution-free reward models 的 scaling 行为，与本文的 formulation comparison 和 scaling analysis (Section 3.3) 高度相关。
3. **FunPRM** (arxiv 2601.22249, 2026): "Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation" — function-as-step 的 PRM 设计与本文的 per-test vs trajectory-level 粒度比较直接对应。
4. **CodeRL+** (arxiv 2510.18471, 2025): "Improving Code Generation via Reinforcement with Execution Semantics Alignment" — 探索 execution semantics 在 reward 设计中的作用。

---

## 6. Overall Assessment

**Overall**: **3.0 — Findings**

**一句话总结**: 一个方法论严谨但新颖性有限的 controlled empirical study，核心 repo-level 发现受限于单 seed 可靠性，适合 Findings 但不足以进入主会议。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨、统计方法得当，但 repo-level 单 seed 问题和合成数据外部效度削弱了结论的 soundness |
| Excitement | 2.5/5 | 设计空间仅 3 个点，function-level equivalence 较为预期，repo-level 分析缺乏深层机制洞察；错误互补性分析是亮点但不足以支撑整篇论文的 excitement |
| Overall | 3.0/5 | Findings 级别——对实践者有参考价值，但 contribution 深度不足以被主会议接收 |

## 7. Confidence

**Confidence: 4/5** — 我对 code verification、process/outcome reward models 和 LLM fine-tuning 领域有较好的了解。对论文的实验设计和统计方法有清晰判断。唯一的不确定性在于是否有更多 2026 年的最新相关工作被遗漏。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-19T08:30:59.891155+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'completed', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'completed', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'in_progress', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'completed', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'completed', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'in_progress', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-19T08:30:59.891722+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-19T08:31:26.070042+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每个 Weakness 逐条回应：\n- **[AGREE]**：同意该观点，并说明理由\n- **[REBUT]**：反驳该观点，并提供具体证据（cite 论文中的 Section/Table/Figure）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Summary\n本文对 execution-free code verification 的三种 formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹级评分）进行了控制实验比较，覆盖两个模型家族（Qwen3-8B、DeepSeek-Coder-6.7B）和两个复杂度级别（function-level、repo-level）。核心发现：function-level 三者统计等价（TOST p=0.007, ±2pp margin）；repo-level CLS 显著优于 CWM（19–26pp gap）；错误互补性支持 ensemble routing。研究设计严谨，统计方法得当，但新颖性有限且 repo-level 结论的单 seed 可靠性不足。\n\n### Strengths\nS1. 严格的控制实验设计\nS2. 统计方法规范（TOST、bootstrap CI、ICC）\nS3. 错误互补性分析有实用价值\nS4. Failure mode taxonomy 有洞察\nS5. 附录内容充实\n\n### Weaknesses — Must-Fix\n\n**N1 [critical] 新颖性有限：\"design space\" 仅含 3 个离散点，缺乏深层机制洞察。**\n- 标题宣称 \"Formulation Design Space\"，实际只比较 3 种已有 formulation\n- Function-level equivalence 是相对预期的结论\n- Repo-level divergence 的分析归结为 \"生成更长输出更难\"，缺乏深层机制分析\n- 与 process vs. outcome supervision 文献的增量不明确\n\n**N2 [critical] Repo-level 核心结论依赖单 seed，统计可靠性不足。**\n- 19–26pp gap 主要基于 Qwen3 seed 42\n- CLS 跨 seed 差异 ~4pp (s42) 到 ~12pp (s123) 说明对 seed 高度敏感\n- \"Controlled comparison\" 核心卖点与单 seed 构成内部矛盾\n\n### Weaknesses — Should-Fix\n\n**W1 [warning] Abstract 数据堆砌（~250 words, 7+ 数字）**\n**W2 [warning] 合成数据外部效度未充分讨论**\n**W3 [warning] Related Work 过于压缩（不到一页），缺失 CodePRM, CodeScaler, FunPRM 等近期工作**\n**W4 [warning] CWM baseline 忠实度存疑（4-8B LoRA vs 原始 32B mid-trained）**\n**W5 [warning] 计算成本缺乏正文中的系统比较**\n\n### Minor\nM1. Table 1 caption 中 LLM-as-judge vs trajectory-level scoring 概念关系需澄清\nM2. Figure 2 信息密度不高\nM3. 不同 seed 使用不同精度（NF4 vs bf16）可能引入偏差\nM4. Appendix \"Extended Limitations\" 暗示正文 Limitations 不完整\nM5. \"CWM stagnation\" 措辞可更中性\n\n### Missing References\n1. CodePRM (ACL 2025 Findings)\n2. CodeScaler (arxiv 2602.17684, 2026)\n3. FunPRM (arxiv 2601.22249, 2026)\n4. CodeRL+ (arxiv 2510.18471, 2025)\n\n### Overall: 3.0 (Findings), Soundness 3.5/5, Excitement 2.5/5, Confidence 4/5\n\n---\n\n请逐条回应上述 Weaknesses（N1, N2, W1-W5, M1-M5），使用 [AGREE] 或 [REBUT] 格式。",
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每个 Weakness 逐条回应：\n- **[AGREE]**：同意该观点，并说明理由\n- **[REBUT]**：反驳该观点，并提供具体证据（cite 论文中的 Section/Table/Figure）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Summary\n本文对 execution-free code verification 的三种 formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹级评分）进行了控制实验比较，覆盖两个模型家族（Qwen3-8B、DeepSeek-Coder-6.7B）和两个复杂度级别（function-level、repo-level）。核心发现：function-level 三者统计等价（TOST p=0.007, ±2pp margin）；repo-level CLS 显著优于 CWM（19–26pp gap）；错误互补性支持 ensemble routing。研究设计严谨，统计方法得当，但新颖性有限且 repo-level 结论的单 seed 可靠性不足。\n\n### Strengths\nS1. 严格的控制实验设计\nS2. 统计方法规范（TOST、bootstrap CI、ICC）\nS3. 错误互补性分析有实用价值\nS4. Failure mode taxonomy 有洞察\nS5. 附录内容充实\n\n### Weaknesses — Must-Fix\n\n**N1 [critical] 新颖性有限：\"design space\" 仅含 3 个离散点，缺乏深层机制洞察。**\n- 标题宣称 \"Formulation Design Space\"，实际只比较 3 种已有 formulation\n- Function-level equivalence 是相对预期的结论\n- Repo-level divergence 的分析归结为 \"生成更长输出更难\"，缺乏深层机制分析\n- 与 process vs. outcome supervision 文献的增量不明确\n\n**N2 [critical] Repo-level 核心结论依赖单 seed，统计可靠性不足。**\n- 19–26pp gap 主要基于 Qwen3 seed 42\n- CLS 跨 seed 差异 ~4pp (s42) 到 ~12pp (s123) 说明对 seed 高度敏感\n- \"Controlled comparison\" 核心卖点与单 seed 构成内部矛盾\n\n### Weaknesses — Should-Fix\n\n**W1 [warning] Abstract 数据堆砌（~250 words, 7+ 数字）**\n**W2 [warning] 合成数据外部效度未充分讨论**\n**W3 [warning] Related Work 过于压缩（不到一页），缺失 CodePRM, CodeScaler, FunPRM 等近期工作**\n**W4 [warning] CWM baseline 忠实度存疑（4-8B LoRA vs 原始 32B mid-trained）**\n**W5 [warning] 计算成本缺乏正文中的系统比较**\n\n### Minor\nM1. Table 1 caption 中 LLM-as-judge vs trajectory-level scoring 概念关系需澄清\nM2. Figure 2 信息密度不高\nM3. 不同 seed 使用不同精度（NF4 vs bf16）可能引入偏差\nM4. Appendix \"Extended Limitations\" 暗示正文 Limitations 不完整\nM5. \"CWM stagnation\" 措辞可更中性\n\n### Missing References\n1. CodePRM (ACL 2025 Findings)\n2. CodeScaler (arxiv 2602.17684, 2026)\n3. FunPRM (arxiv 2601.22249, 2026)\n4. CodeRL+ (arxiv 2510.18471, 2025)\n\n### Overall: 3.0 (Findings), Soundness 3.5/5, Excitement 2.5/5, Confidence 4/5\n\n---\n\n请逐条回应上述 Weaknesses（N1, N2, W1-W5, M1-M5），使用 [AGREE] 或 [REBUT] 格式。",
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-19T08:31:54.683650+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28613
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-19T08:31:54.885250+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请对每个 Weakness 逐条回应：\n- **[AGREE]**：同意该观点，并说明理由\n- **[REBUT]**：反驳该观点，并提供具体证据（cite 论文中的 Section/Table/Figure）\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\nThis paper compares three execution-free code verification formulations (CLS, CWM, TRAJ) under controlled conditions across two model families and two complexity levels. The main finding is that formulations achieve near-equivalent accuracy at function level but diverge sharply at repository level, with CLS consistently outperforming CWM. The study is well-motivated and addresses a genuine practical gap, but several methodological issues undermine the \"controlled comparison\" framing.\n\n### Strengths\nS1. Practically important and clearly scoped research question\nS2. Multi-dimensional experimental design (formulation×model×size×complexity×seeds)\nS3. Rigorous statistical framework for function-level analysis\nS4. Thorough failure mode taxonomy\nS5. Honest limitations disclosure\nS6. Comprehensive ablation suite\n\n### Weaknesses — Must-Fix\n\n**N1 [critical] TOST equivalence margin (±2pp) 缺乏正式论证和敏感性分析**\n- ±2pp margin 的选择仅以一句话论证\n- 缺少 margin 敏感性分析（±1pp, ±1.5pp, ±2pp, ±3pp 下的 p 值）\n- 直接影响 \"formulation equivalence at low complexity\" 核心贡献的可信度\n- 建议：报告 smallest margin at which equivalence holds\n\n**N2 [critical] \"Controlled comparison\" 声称与实际设计存在系统性裂隙**\n- (a) Checkpoint selection inconsistency: CLS val-best vs CWM/DeepSeek s123 final epoch\n- (b) Evaluation seq_length asymmetry: Qwen3 CWM 8192 vs DeepSeek CWM 4096\n- (c) Preprocessing differences: DeepSeek s42 drop vs s123 truncate\n- (d) TRAJ training regime: different lr, different data size, different evaluation granularity\n- 建议：增加 \"threats to internal validity\" 段落；将 \"controlled\" 调整为 \"systematic\"\n\n**N3 [critical] Repo-level n=48 variant-level 结论缺乏可靠性**\n- 单个 variant 翻转 = ~2.08pp accuracy 变化\n- CLS Qwen3-8B 两个 seed 差异 8.33pp（4 个 variant 差异）\n- TRAJ DeepSeek 6 seeds 的 5pp std dev\n- 缺少 variant-level 比较的 confidence intervals 和 power analysis\n- 建议：增加 bootstrap CI；进行 power analysis；将 variant-level 结论标记为 preliminary\n\n### Weaknesses — Should-Fix\n\n**W1 [warning] 多重比较问题未处理**\n**W2 [warning] CWM baseline external validity 严重受限但仍做 formulation-level 归因**\n**W3 [warning] Re-repair pilot (n=44) 不应作为 contribution 呈现**\n**W4 [warning] Cross-model \"validation\" 措辞过强**\n**W5 [warning] Function-level ICC 用于 repo-level oracle analysis 的转移假设不充分**\n\n### Minor\nM1. Table 3 格式不统一（\"/\" 分隔 vs 单值）\nM2. Matched-context ablation 只控制 eval-time 未控制 training-time context\nM3. CWM unparseable default-to-pass 的方向性影响应在正文讨论\nM4. Scaling analysis seeds 使用说明不清\nM5. 2026 年引用的 ARR policy 合规性\n\n### Questions\nQ1. TOST 在 ±1pp 下是否成立？\nQ2. CWM NaN validation loss 是否尝试修复？\nQ3. 如何解释同一 formulation 8.33pp seed variance 后仍归因于 formulation choice？\nQ4. Parseable CWM outputs 是否系统偏向 harder instances？\nQ5. Oracle ensemble 90.63% 在其他 seeds 下是否稳定？\n\n### Missing References\n- CodeRM (code reward model)\n- Constrained Decoding (Willard & Louf 2023)\n- 近年 mutation-real fault coupling meta-analysis\n\n### Overall: 3 (Findings), Soundness 3/5, Excitement 3.5/5, Confidence 4/5\n\n---\n\n请逐条回应上述 Weaknesses（N1, N2, N3, W1-W5, M1-M5），使用 [AGREE] 或 [REBUT] 格式。",
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请对每个 Weakness 逐条回应：\n- **[AGREE]**：同意该观点，并说明理由\n- **[REBUT]**：反驳该观点，并提供具体证据（cite 论文中的 Section/Table/Figure）\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\nThis paper compares three execution-free code verification formulations (CLS, CWM, TRAJ) under controlled conditions across two model families and two complexity levels. The main finding is that formulations achieve near-equivalent accuracy at function level but diverge sharply at repository level, with CLS consistently outperforming CWM. The study is well-motivated and addresses a genuine practical gap, but several methodological issues undermine the \"controlled comparison\" framing.\n\n### Strengths\nS1. Practically important and clearly scoped research question\nS2. Multi-dimensional experimental design (formulation×model×size×complexity×seeds)\nS3. Rigorous statistical framework for function-level analysis\nS4. Thorough failure mode taxonomy\nS5. Honest limitations disclosure\nS6. Comprehensive ablation suite\n\n### Weaknesses — Must-Fix\n\n**N1 [critical] TOST equivalence margin (±2pp) 缺乏正式论证和敏感性分析**\n- ±2pp margin 的选择仅以一句话论证\n- 缺少 margin 敏感性分析（±1pp, ±1.5pp, ±2pp, ±3pp 下的 p 值）\n- 直接影响 \"formulation equivalence at low complexity\" 核心贡献的可信度\n- 建议：报告 smallest margin at which equivalence holds\n\n**N2 [critical] \"Controlled comparison\" 声称与实际设计存在系统性裂隙**\n- (a) Checkpoint selection inconsistency: CLS val-best vs CWM/DeepSeek s123 final epoch\n- (b) Evaluation seq_length asymmetry: Qwen3 CWM 8192 vs DeepSeek CWM 4096\n- (c) Preprocessing differences: DeepSeek s42 drop vs s123 truncate\n- (d) TRAJ training regime: different lr, different data size, different evaluation granularity\n- 建议：增加 \"threats to internal validity\" 段落；将 \"controlled\" 调整为 \"systematic\"\n\n**N3 [critical] Repo-level n=48 variant-level 结论缺乏可靠性**\n- 单个 variant 翻转 = ~2.08pp accuracy 变化\n- CLS Qwen3-8B 两个 seed 差异 8.33pp（4 个 variant 差异）\n- TRAJ DeepSeek 6 seeds 的 5pp std dev\n- 缺少 variant-level 比较的 confidence intervals 和 power analysis\n- 建议：增加 bootstrap CI；进行 power analysis；将 variant-level 结论标记为 preliminary\n\n### Weaknesses — Should-Fix\n\n**W1 [warning] 多重比较问题未处理**\n**W2 [warning] CWM baseline external validity 严重受限但仍做 formulation-level 归因**\n**W3 [warning] Re-repair pilot (n=44) 不应作为 contribution 呈现**\n**W4 [warning] Cross-model \"validation\" 措辞过强**\n**W5 [warning] Function-level ICC 用于 repo-level oracle analysis 的转移假设不充分**\n\n### Minor\nM1. Table 3 格式不统一（\"/\" 分隔 vs 单值）\nM2. Matched-context ablation 只控制 eval-time 未控制 training-time context\nM3. CWM unparseable default-to-pass 的方向性影响应在正文讨论\nM4. Scaling analysis seeds 使用说明不清\nM5. 2026 年引用的 ARR policy 合规性\n\n### Questions\nQ1. TOST 在 ±1pp 下是否成立？\nQ2. CWM NaN validation loss 是否尝试修复？\nQ3. 如何解释同一 formulation 8.33pp seed variance 后仍归因于 formulation choice？\nQ4. Parseable CWM outputs 是否系统偏向 harder instances？\nQ5. Oracle ensemble 90.63% 在其他 seeds 下是否稳定？\n\n### Missing References\n- CodeRM (code reward model)\n- Constrained Decoding (Willard & Louf 2023)\n- 近年 mutation-real fault coupling meta-analysis\n\n### Overall: 3 (Findings), Soundness 3/5, Excitement 3.5/5, Confidence 4/5\n\n---\n\n请逐条回应上述 Weaknesses（N1, N2, N3, W1-W5, M1-M5），使用 [AGREE] 或 [REBUT] 格式。",
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 304 · 2026-05-19T08:31:56.466566+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1581
}
```

</details>

---


### Assistant

_source line 305 · 2026-05-19T08:31:59.216977+00:00_

交叉分享任务已分配。等待两位 Reviewer 完成逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 306 · 2026-05-19T08:32:01.997843+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**: Overall 3.0（Findings 级别），Soundness 3.5，Excitement 2.5，Confidence 4/5。

**两个 critical 问题**：
1. 新颖性有限——"design space" 仅 3 个离散点，function-level equivalence 较预期，repo-level 分析缺深层机制洞察
2. Repo-level 核心结论（19–26pp gap）依赖单 seed，统计可靠性不足

**四个 warning 问题**：Abstract 数据堆砌、合成数据外部效度、Related Work 压缩（遗漏 CodePRM/CodeScaler/FunPRM）、CWM baseline 在小模型上的忠实度、缺乏推理成本系统对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 307 · 2026-05-19T08:32:07.938244+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 308 · 2026-05-19T08:33:26.766285+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

### Must-Fix

**[AGREE] R2-N1: 新颖性有限，"design space" 仅含 3 个离散点**

同意大方向，但程度上有保留。

同意点：标题 "Formulation Design Space" 确实 overselling——3 个离散 formulation 不构成连续 "space"，更准确的描述是 "formulation comparison"。Function-level equivalence（§4.2, Table 1: CLS 88.43% vs CWM 87.19% vs TRAJ 86.30%）确实是一个相对可预期的结果——当输出短且结构化时，generation 和 classification 差异不大是直觉可推导的。

保留点：我认为 R2 低估了两个贡献。(1) Failure mode taxonomy（Table 4）不仅仅是 "生成长输出更难" 的同义反复——它区分了 format collapse、decision collapse、aggregation penalty 三种机制，且展示了 same model family 在不同 configuration 下触发不同 failure mode（DeepSeek s42 vs s123, §4.5）。这种 formulation × configuration 交互效应是非平凡的洞察。(2) Checkpoint selection confound（§4.6）——val-best 优化 per-test accuracy 但在 all-pass rule 下反而损害 variant-level accuracy——是一个有实用意义的发现。但 R2 关于与 process vs. outcome supervision 文献增量不明确的批评是成立的：论文在 §5 中 draw parallel to Lightman et al. (2023) 但未做实质性的区分分析。

总结：标题需调整，function-level null result 的贡献度应降权，但 failure mode taxonomy 和交互效应仍有增量价值。建议 novelty 定位为 "empirical methodology contribution"。

---

**[AGREE] R2-N2: Repo-level 核心结论依赖单 seed**

完全同意，这与我的 N3 一致。补充以下证据加强 R2 的论点：

- Table 5 (Appendix D) 显示 CLS Qwen3-8B 的两个 seed 在 variant-level accuracy 上差 8.33pp（72.92% vs 81.25%），这个 intra-formulation variance 与论文声称的 inter-formulation difference 量级可比
- DeepSeek CLS 的两个 seed 差 7.68pp（82.61% vs 74.93%, Table 3 footnote），但这里的差异还 conflate 了 preprocessing 和 checkpoint selection
- CWM repo-level 在 Qwen3 只有 seed 42；DeepSeek CWM 的 variant-level 数据标记为 "preliminary"（Table 5 footnote: "evaluated on ~75% of test instances"）
- TRAJ repo-level 虽然有 DeepSeek 6 seeds，但标准差 5.00pp（75.35% ± 5.00）本身就说明结论不稳定

论文在正文中承认 "single-seed constraints limit causal attribution"（§4.5），但 Contribution 2 仍然写 "Complexity-dependent divergence with formulation × model interaction"——语气远强于证据支撑。我在 N2 中建议将 framing 从 "controlled" 调整为 "systematic"，这与 R2 的批评方向一致。

---

### Should-Fix

**[AGREE] R2-W1: Abstract 数据堆砌**

同意。重新数了一下 abstract 中的数字：88.4%, 87.2%, 4B, 5 seeds, p=0.007, ±2pp, 19-26pp, 72.96%, 86.9%, 86.8%, 2 seeds, 4-12pp, 25-30pp, 217×, 90.63%, 1.36pp, 75.35%——超过 15 个数值。CLAUDE.md 的写作规范明确要求 "Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim"。当前 abstract 读起来确实像实验报告的压缩版而非 narrative。

---

**[AGREE] R2-W2: 合成数据外部效度**

同意，但程度有限。论文确实引用了 Andrews et al. (2005) 和 Just et al. (2014) 关于 mutation-real fault coupling 的经典文献（references.bib），且 Limitations 提到 "synthetic-to-real transfer gap remains untested"。但讨论仅一句话。对于一篇以 "practitioners choosing a formulation" (§1) 为动机的论文，合成数据到真实 bug 的迁移是 external validity 的核心威胁——至少应讨论：(1) mutation types 与真实 bug 分布的已知差异；(2) SWE-bench Verified 的 mutants 是否保持了原始 benchmark 的 difficulty distribution。

---

**[REBUT] R2-W3: Related Work 过于压缩，缺失 CodePRM/CodeScaler/FunPRM/CodeRL+**

部分反驳。

(1) 篇幅问题：Related Work（§5）确实只有 3 段，但这是 8 页正文限制下的常见取舍。每段按主题组织（Execution Simulation & Verification; Process vs. Outcome Supervision; Repair, Mutation Testing, & Task Framing），有归纳和 positioning，不是简单的 citation list。对于一篇以实验方法论为核心的论文，将更多篇幅分配给 Method 和 Experiments 是合理的。

(2) Missing references 的实质影响：R2 列出的 4 篇缺失引用中，CodePRM 和 FunPRM 属于 process reward model 领域，与本文的 "per-test classification" 结构类似——这些确实应该引用以 strengthen §5 第 2 段的 positioning。但 CodeScaler (2602.17684) 和 CodeRL+ (2510.18471) 需要验证是否与本文直接相关——R2 未说明这两篇与本文的具体关联。如果仅因为名字含 "Code" 就列为 missing reference，这不够充分。

建议：补充 CodePRM 和 FunPRM 的引用是合理的；CodeScaler 和 CodeRL+ 需要 R2 进一步说明相关性。

---

**[AGREE] R2-W4: CWM baseline 忠实度存疑**

完全同意，这与我的 W2 一致。4-8B LoRA fine-tuned CWM 与原始 32B mid-trained CWM (Meta, 2025) 在训练范式上有质的差异。论文在 §4.1 明确声明 "Our CWM baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model"，但正文中反复使用 "generation formulation" 做归因（§4.5: "the fundamental bottleneck is output space complexity, not format compliance"）。如果 bottleneck 是 output space complexity，那更大的模型（32B）或更深的 training（mid-training on execution traces）可能就能突破这个 bottleneck——这时 "formulation-inherent" 的归因就不成立了。Scaling data 显示 CWM 4B→8B 无改善（§4.3, Table 2: -0.03pp），但 4B→8B 只是 2× scale，远不足以推断 formulation-level 的天花板。

---

**[REBUT] R2-W5: 计算成本缺乏正文中的系统比较**

不同意这是 Should-Fix 级别。

正文 §4.6 最后一段明确报告了核心效率数据："CLS achieves 217× higher throughput than CWM (853 vs. 3.9 inferences/min; 1 output token vs. avg 477)"。Appendix E(i) 进一步提供了 CLS-TRAJ 的 per-call 和 per-instance 效率比较，包括 crossover point (|T| ≈ 50)。对于一篇以 formulation accuracy 为核心的论文，efficiency 数据放在 appendix 是合理的空间分配。如果要在 8 页正文中加入完整的 cost-accuracy tradeoff 表，需要削减其他内容（如 ablation discussion）。这更接近 Minor 而非 Should-Fix。

---

### Minor

**[AGREE] R2-M1:** 同意。Table 1 中 "ZS LLM-as-judge" 是 prompting baseline，不是 fine-tuned trajectory scoring，但与 TRAJ 列并列容易混淆。Caption 应明确 LLM-as-judge 的评估方式。

**[REBUT] R2-M2:** 不同意 Figure 2 信息密度低。Figure 2 可视化了从 function-level 到 repo-level 的 gap amplification（1.32pp → 2.62pp → 25.59pp），这是论文核心叙事 "complexity-dependent divergence" 的视觉锚点。虽然只有少量数据点，但 figure 的叙事功能（让读者直观看到数量级跳跃）是有价值的。

**[AGREE] R2-M3:** 同意 NF4 vs bf16 mixing 是潜在偏差源。不过论文在 Appendix F 已报告："Restricting to three bfloat16 seeds yields a comparable mean gap with wider confidence interval; the NF4 seeds do not systematically shift the equivalence result." 这个 robustness check 应提升到正文或至少在 §4.4 中 inline 提及。

**[REBUT] R2-M4:** 不同意 "Extended Limitations" 暗示正文不完整。8 页正文限制下，将详细的 per-configuration 限制讨论放在 appendix 是标准做法。正文 Limitations 段落覆盖了主要威胁（single-seed, synthetic data, CWM baseline gap, TRAJ data asymmetry, re-repair negative result），Appendix F 补充 per-seed 和 per-configuration 的细粒度讨论。这恰恰是 responsible 的做法。

**[AGREE] R2-M5:** 同意 "stagnation" 措辞偏强。§4.3 写 "CWM stagnation (−0.03pp) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation"——qualifier 是对的，但 "stagnation" 本身暗示了一种负面判断。建议改为 "plateau" 或 "flat scaling"。

---

### Missing References

R2 列出 CodePRM (ACL 2025 Findings)、CodeScaler (2602.17684)、FunPRM (2601.22249)、CodeRL+ (2510.18471)。我同意 CodePRM 和 FunPRM 与 per-test/process supervision 直接相关，应引用。另外我在自己的审稿中也指出了 constrained decoding 方法论文献的缺失（§4.5 讨论了 constrained decoding 但未引用相关工作）。

---

### Overall Assessment 对比

R2 给出 3.0 (Findings)，与我的评分一致。我们在 repo-level 单 seed 可靠性（R2-N2 ≈ R1-N3）和 CWM baseline 忠实度（R2-W4 ≈ R1-W2）上高度一致。主要分歧在于 novelty 评估：R2 的 Excitement 2.5/5 偏低，我给 3.5/5。我认为 failure mode taxonomy 和 formulation × configuration 交互效应的增量价值被 R2 低估，但 R2 关于 "design space" framing 过强的批评是成立的。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 309 · 2026-05-19T08:33:31.873397+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 30

## Round 30

2 recorded events


### User

_source line 310 · 2026-05-19T08:33:35.544072+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **与 R2 高度一致的问题**：repo-level 单 seed 可靠性 (N2)、CWM baseline 忠实度 (W4)、abstract 数据堆砌 (W1)、Overall 3.0 Findings
- **部分同意**：novelty 批评 (N1) 方向正确但 failure mode taxonomy 被低估；合成数据外部效度 (W2) 已有 flag 但讨论不足
- **反驳**：Related Work 篇幅 (W3) 在 8 页限制下合理但应补充 CodePRM/FunPRM；计算成本 (W5) 正文已有核心数据不需要升级为 Should-Fix；Figure 2 (M2) 有叙事功能；Extended Limitations (M4) 是 responsible practice

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 311 · 2026-05-19T08:33:40.638334+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 31

## Round 31

10 recorded events


### User

_source line 312 · 2026-05-19T08:36:54.421932+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1

---

### Must-Fix 问题

**[AGREE] R1-N1: TOST ±2pp margin 缺乏正式论证和敏感性分析**

同意。Section 3.4 对 ±2pp margin 的论证仅一句话（"formulation differences below 2 pp are unlikely to affect deployment decisions"），缺乏领域标准或先例支撑。Appendix I (page 18) 提供了 NF4 vs bfloat16 的 seed 稳健性分析，但这回答的是 seed/precision 敏感性而非 margin 敏感性。R1 要求的 ±1pp/±1.5pp/±2pp/±3pp 下的 p 值梯度表完全缺失。

补充我的视角：在准确率 85–97% 的范围内（Table 1），2pp 是一个不小的差异。如果 ±1pp 下 TOST 不成立，"equivalence" 结论需要显著降级为 "near-equivalence"。报告 smallest equivalence margin 是标准做法（如 bioequivalence 文献中的 practice），论文应遵循。

---

**[AGREE] R1-N2: "Controlled comparison" 与实际设计存在系统性裂隙**

同意 R1 列举的四项 confound 均为事实：

**(a) Checkpoint selection inconsistency:** Section 3.1 (page 4) 明确写道 CWM runs 因 NaN validation loss 而 default to final epoch checkpoint，而 CLS 使用 val-best。这意味着 CLS 系统性地获得了更优的 checkpoint，构成对 CWM 不利的 confound。虽然 NaN loss 本身反映了 CWM formulation 的训练困难，但论文未将此作为 CWM 的 inherent weakness 来论述，而是作为工程 workaround 一笔带过。

**(b) Evaluation seq_length asymmetry:** Appendix D (page 14) 的序列长度消融显示 max_new_tokens=512 对 CWM 的性能有显著影响（truncation introduces 136 unparseable outputs, 1.3% of test samples）。不同模型使用不同 eval context length 是一个未充分讨论的变量。

**(c) Preprocessing differences:** Footnote 2 (page 6) 确认 s42 用 drop preprocessing、s123 用 truncate preprocessing。Section 3.3 承认 CLS degradation 从 ~4pp (s42, drop) 到 ~12pp (s123, truncate)，这说明 preprocessing 对结果有 3× 的影响，是一个主要 confound 而非噪声。

**(d) TRAJ training regime:** Table 11 (page 16) 确认 TRAJ 使用不同 lr (5×10⁻⁵ vs 2×10⁻⁴)、不同数据量 (~400 vs ~70K instances)、不同评估粒度 (variant-level n=48 vs per-test n=9,784)。这些差异使 TRAJ 与 CLS/CWM 的比较不在同一基线上。

R1 建议将 "controlled" 改为 "systematic" 是合理的。当前的 "Controlled Empirical Study" 标题暗示所有变量均被控制，但实际上只控制了模型大小和训练数据来源，其余多个关键变量（checkpoint selection、preprocessing、seq_length、lr、evaluation granularity）均存在差异。

补充：我在 Round 1 审稿中未对这些 confound 逐一拆解，R1 的分析比我更细致。这些 confound 单独看可能不致命（repo-level 的 19–26pp gap 足够大），但合在一起确实削弱了 "controlled" 的 claim。

---

**[AGREE] R1-N3: Repo-level n=48 variant-level结论缺乏可靠性**

同意，并补充定量论据。

n=48 variant-level 样本下，accuracy 在 ~80% 附近的 standard error 为 sqrt(0.8×0.2/48) ≈ 5.8pp，95% CI 宽度为 ±11.3pp。Table 10 (page 15) 显示 CLS Qwen3-8B variant-level accuracy 为 72.92%（seed 42），CWM 为 45.83%（seed 42）——差异 27.09pp 超过 2 倍标准误，方向上可信。但 Table 3 (page 6) 的 CLS Qwen3-8B 两个 seed 差异（per-test 83.63% vs 75.30%, 8.33pp gap）相当于 ~4 个 variant 翻转，说明 variant-level 结论对 seed 极度敏感。

R1 提到 TRAJ DeepSeek 6 seeds 的 5pp std dev (Table 3: 75.35 ± 5.00)。这进一步佐证了 repo-level 结论的不稳定性。

Per-test 级别（n ≈ 700+）的结论更可靠，但论文在多处混用 per-test 和 variant-level 结果而未充分区分其统计可靠性。R1 建议增加 bootstrap CI 和 power analysis，并将 variant-level 结论标记为 preliminary，我完全赞同。

---

### Should-Fix 问题

**[AGREE] R1-W1: 多重比较问题未处理**

同意。论文执行了至少以下独立统计检验：TOST equivalence、per-formulation bootstrap CIs、ICC、Table 1 中多对 formulation 比较、Table 2 的 scaling comparisons、Table 3 的 repo-level comparisons。在 α=0.05 下，未校正的多重比较显著增加 family-wise error rate。虽然 ML 经验论文中多重比较校正不如临床研究严格，但论文的 core claim 之一正是统计严谨性（TOST、ICC），因此应自洽地处理多重比较。至少应报告 Bonferroni-adjusted p 值或采用 Holm 校正。

---

**[AGREE] R1-W2: CWM baseline external validity 受限但仍做 formulation-level 归因**

同意，这与我 Round 1 的 W4 完全一致。Section 3.1 (page 4) 明确声明 "Our CWM baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model"。但 Section 3.5 和 Conclusion (page 8) 的 claims 使用的是 "CWM formulation" 而非 "our CWM implementation"。原始 CWM 设计在 32B 参数上运行，CWM formulation 的核心假设（精确模拟执行输出）可能天然需要更大模型容量。在 4–8B 上的结论不能直接推广到 CWM formulation 本身。

R1 正确指出了 formulation-level 归因与 implementation-level 证据之间的 gap。论文应将所有 CWM 相关结论限定为 "at ≤8B parameter scale with LoRA fine-tuning"。

---

**[REBUT] R1-W3: Re-repair pilot (n=44) 不应作为 contribution 呈现**

不同意 R1 的定性。

1. Re-repair pilot 位于 Appendix G section (j) (page 17–18)，不在正文中。
2. 论文 Introduction (page 2) 的 contribution list 仅包含两条：(1) formulation equivalence at low complexity, (2) complexity-dependent divergence。Re-repair 未被列为 contribution。
3. 该 pilot 报告了**负面结果**（Δ₁ = −2.3%, p = 0.42, effect size δ = 0），并明确标注为 "pilot"，且讨论了 sample size 不足（"statistical power is ~0.3 for a medium effect size"）。
4. 负面结果在附录中报告是合理的学术实践——它防止了其他研究者重复相同死路。

R1 的担忧如果 re-repair 出现在正文或 contribution list 中是成立的，但当前它仅作为附录中的负面 pilot 呈现，定位恰当。

---

**[AGREE] R1-W4: Cross-model "validation" 措辞过强**

同意。Section 3.5 (page 6) 使用 "Cross-model validation" 作为小标题，但仅有 DeepSeek-Coder 一个额外模型家族。n=2 model families 不构成 "validation"——至多是 "partial replication" 或 "consistency check"。虽然 page 6 同段后文加了 hedge（"though single-seed constraints limit causal attribution"），但小标题本身已传递了过强的信号。审稿人读到 "Cross-model validation" 会期望 3+ 模型家族的系统验证。

---

**[AGREE] R1-W5: Function-level ICC 向 repo-level oracle analysis 的转移假设不充分**

同意。Section 3.2 的 ICC (0.191) 和 oracle ensemble (90.63%, +3.12pp) 均在 function-level 计算。Conclusion (page 8) 将 "error complementarity" 作为一般性发现提出，隐含其可推广到 repo-level。但 repo-level 的错误模式与 function-level 结构性不同：

- Function-level: CLS 和 CWM 有互补的 false negative/positive 模式 (Appendix H, page 16)
- Repo-level: CWM 存在大规模 format collapse (Table 4, page 6)，其错误不是 "互补" 的，而是系统性的能力不足

当 CWM 在 repo-level 的 variant-level accuracy 低于 majority baseline (45.83% vs 54.17%, Table 10)，将其纳入 ensemble 不太可能有正面贡献。论文应明确限定 error complementarity 结论仅适用于 function-level，或在 repo-level 提供独立的 oracle analysis。

---

### Minor 问题

**[AGREE] R1-M1: Table 3 格式不统一**

Table 3 (page 6) 混用 "/" 分隔（如 "83.63 / 75.30"）和单值。应统一为相同格式。

---

**[AGREE] R1-M2: Matched-context ablation 只控制 eval-time 未控制 training-time context**

同意。Appendix D (page 14) 的序列长度消融改变了 eval-time 的 max_new_tokens 和 context length，但训练时的 context length 保持不变。CWM 对上下文长度敏感，training-time context 差异可能同样重要。不过这对所有 formulation 同等适用，不太可能系统性偏向某一 formulation。

---

**[AGREE] R1-M3: CWM unparseable default-to-pass 应在正文讨论**

同意。Appendix G section (c) (page 16–17) 讨论了 "Relaxed matching does not rescue CWM" 和 default-to-pass 行为。但 default-to-pass 直接影响 CWM 准确率的解读——当大量 CWM 输出不可解析时，默认为 PASS 使得 CWM 的 accuracy 数字包含了大量"猜对"的成分。从 Table 9 (page 15) 看，CWM parseable-only accuracy 与 overall accuracy 有显著差异。这对 CWM-CLS 比较的公平性有直接影响，应在正文 Section 3.5 讨论而非仅放在附录。

---

**[AGREE] R1-M4: Scaling analysis seeds 使用说明不清**

同意。Section 3.3 (page 5) 提到 "two matched seeds (42, 123)" 但 footnote 2 (page 6) 说明 s42 和 s123 使用不同 preprocessing 和不同 checkpoint selection。这不是真正的 "matched seeds"——它们在 preprocessing 和 checkpoint 维度上都不匹配。措辞应改为 "two configurations" 而非 "matched seeds"。

---

**[REBUT] R1-M5: 2026 年引用的 ARR policy 合规性**

不认为这是实质问题。ARR 的匿名审稿政策允许引用公开的 arXiv 预印本，无论年份。论文引用的 2026 年工作（maimon2026selfexecution, lee2026solidcoder）均为公开的 arXiv 论文，不违反 double-blind 政策。引用近期相关工作是审稿人期望的——不引用反而会被视为调研不充分。除非这些引用可被追溯至作者身份（如自引），但从引用内容看并非如此。

---

### 对 R1 Questions 的补充意见

**Q1 (TOST ±1pp):** 我在 Round 1 Q1 中提出了相同问题，完全一致。

**Q2 (CWM NaN validation loss):** 好的追问。NaN validation loss 不仅影响 checkpoint selection (N2a)，还说明 CWM 的训练本身存在稳定性问题。论文应讨论是否尝试过 gradient clipping、loss masking、或更小 lr 来解决。

**Q3 (8.33pp seed variance 后的 formulation 归因):** 与 N3 一致，是核心方法论问题。当同一 formulation 的 seed variance (8.33pp) 接近 formulation 间差异的量级时，formulation-level 归因的可信度大幅降低。

**Q4 (Parseable CWM outputs 是否偏向更难 instances):** 这是一个我未想到的好问题。如果 unparseable outputs 集中在简单 instances（CWM 对简单代码反而 format collapse），那么 parseable-only accuracy 会被人为降低。反之亦然。Table 9 (page 15) 的 parse rate 和 parseable-only accuracy 数据可以回答此问题，但论文未做此分析。

**Q5 (Oracle ensemble 跨 seed 稳定性):** 与 N3 一致。Oracle ensemble 90.63% 仅报告了单一设置，跨 seed 稳定性未知。

---

### 总体评价

R1 的审稿意见质量很高。核心发现与我的 Round 1 评估高度一致：

- **方向一致**: 我们都认为论文的 soundness 被 repo-level 单 seed 问题和 CWM baseline external validity 削弱，新颖性中等。
- **R1 比我更细致的地方**: N2 中对 confound 的逐项拆解（checkpoint, seq_length, preprocessing, TRAJ regime）比我的笼统批评更有诊断价值。M4 指出 "matched seeds" 实际上 preprocessing 不匹配，是一个精准的发现。
- **我比 R1 更关注的地方**: 我的 N1 更侧重 "design space" 仅 3 个点的新颖性不足，以及 Related Work 遗漏的具体近期论文（CodePRM、FunPRM、CodeScaler）。R1 的新颖性评价（Excitement 3.5/5）略高于我的（2.5/5）。
- **评分差异**: R1 Overall 3.0, Soundness 3/5, Excitement 3.5/5; 我 Overall 3.0, Soundness 3.5/5, Excitement 2.5/5。总分一致但维度分布不同——R1 对 soundness 更严（方法论 confound），我对 excitement 更严（新颖性不足）。
- **唯一分歧**: W3 (re-repair pilot) 和 M5 (2026 引用政策)——我认为这两项不构成实质问题。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 313 · 2026-05-19T08:37:30.678687+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'completed', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料完整性检查', 'status': 'completed', 'activeForm': '执行 Venue 调研和资料完整性检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行 Reviewer 交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿收敛'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-19T08:37:30.679339+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

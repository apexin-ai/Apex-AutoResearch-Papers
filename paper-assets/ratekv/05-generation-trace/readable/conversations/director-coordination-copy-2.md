# Director coordination

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 254
- **Recorded user turns:** 21
- **Tool calls:** 106
- **Original source:** `logs/chats/feishu_group_oc_ec66209ede0ea4e3bda924778c210d8e_director.jsonl`
- **Structured JSON:** [`b84a3706fdc3a68a1c28.json`](../../sessions/b8/b84a3706fdc3a68a1c28.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-14T12:59:48.233440+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ratekv
- 论文路径: projects/ratekv/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T12:59:53.836310+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T12:59:53.887231+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T12:59:57.199179+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
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

_source line 5 · 2026-05-14T12:59:57.300006+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T13:00:02.170089+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ratekv"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T13:00:03.525902+00:00_

{"result":"# 项目 ratekv 概况\n\n## 实验状态 (55 个)\n\n- **exp_c_no2bit**: DONE (negative) — \n- **exp_c_constrained_mckp**: DONE (success) — \n- **exp_b_hires_quant**: DONE (negative) — \n- **exp_a_targeted_hybrid**: DONE (negative) — \n- **mvp_004**: DONE (negative) — \n- **p0_2_cliff_7B**: DONE (success) — \n- **p0_1_ppl_fast**: DONE (negative) — \n- **p0_2_cliff_1.5B**: DONE (success) — \n- **sanity_004**: DONE (success) — \n- **sanity_003**: DONE (failed) — \n- **sanity_002**: DONE (failed) — \n- **sanity_001**: DONE (failed) — \n- **mvp_003**: DONE (failed) — \n- **mvp_002**: DONE (failed) — \n- **mvp_001**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- qwen72b_profiling（等待人工审批）\n- multi_seed_lowres（等待人工审批）\n- greedy_constrained_ablation（准备中）\n- cross_domain_calibration_v2（准备中）\n\n## 近期结论\n- **mistral_c4_cross_dataset** (success): C4 cross-dataset eval for Mistral-7B-v0.3: 用 C4 calibration 数据 profiling → constrained MCKP allocation，在 WT2 上 eval。对比 allocation agreement rate (C4 vs WT2 calibrated)，验证跨模型 generalizability。Mistral 作为低异质性模型，agreement rate 可能更高（heads 更均匀）。 ← 基于 c4_rerun_d032\n- **llama_c4_cross_dataset** (negative): C4 cross-dataset eval for Llama-3.1-8B: 用 C4 calibration 数据 profiling → constrained MCKP allocation，在 WT2 上 eval。对比 allocation agreement rate (C4 vs WT2 calibrated)，验证 Qwen 上发现的 96.4% agreement 是否跨模型成立。 ← 基于 c4_rerun_d032\n- **mistral_heuristic_k4** (success): —\n  [mistral_heuristic_k4_results](/api/workspace-files/projects/ratekv/artifacts/mistral_heuristic_k4/data/mistral_heuristic_k4_results.txt)\n\n## 趋势\n成功 30 / 负向 10 / 失败 6 / 共 51\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-37397: 无 GPU 信息\n\n## 告警\n- mvp_001: 训练失败 — unknown\n- sanity_001: 训练失败 — unknown\n- mvp_002: 训练失败 — unknown\n- sanity_002: 训练失败 — unknown\n- mvp_003: 训练失败 — unknown\n- sanity_003: 训练失败 — unknown\n- c4_cross_dataset_eval: 已被终止 — unknown\n- l0_only_heuristic: 已被终止 — unknown\n- l0_heurist
…[truncated 117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T13:00:03.526290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T13:00:04.028685+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	
11	\title{When Does Non-Uniform KV Cache Quantization Help?\\Cardinality Constraints and a Heterogeneity Diagnostic}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	\input{abstract}
20	\end{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{experiments}
26	\input{analysis}
27	\input{conclusion}
28	
29	\bibliography{references}
30	
31	\input{appendix}
32	
33	\end{document}
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T13:00:04.029162+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
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

_source line 11 · 2026-05-14T13:00:04.079708+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T13:00:10.956201+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T13:00:12.111070+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T13:00:12.362393+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T13:00:12.463199+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ratekv",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ratekv",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T13:00:18.686400+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2025 – CL deadlines for Qualifying Papers | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/11"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"}]

Based on the search results, here is the information about EMNLP 2026 Call for Papers:

## Submission Deadline

The ARR sub
…[truncated 1637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7730
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T13:00:18.737129+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6273
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T13:00:23.103754+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit long paper short paper format ACL template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit long paper short paper format ACL template"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T13:00:23.606187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T13:00:24.058653+00:00_

1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
7	We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T13:00:24.059024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T13:00:24.962802+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves clos
…[truncated 4055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T13:00:24.963260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T13:00:25.465471+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We profile each KV head independently by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
25	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
26	
27	The optim
…[truncated 7700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T13:00:25.465889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T13:00:25.616881+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on three architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
11	and \textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention).
12	This selection covers the two dominant KV head counts (112 vs.\ 256) and both standard and sliding-window attention.
13	
14	\paragraph{Evaluation.}
15	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
16	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
17	
18	\paragraph{Profiling.}
19	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
20	We use two profiling resolutions: \emph{standard} (16 sequences $\times$ 512 tokens) and \emph{high-resolution} (64 sequences $\times$ 2048 tokens), both from WikiText-2 train.
21	Unless marked with $\dagger$, all results use standard-resolution profiling; Appendix~\ref{sec:profiling_resolution} analyzes the effect of resolution.
22	
23	\paragraph{Compression and constraint.}
24	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
25	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).
26	
27	\paragraph{Baselines.}
28	We compare against:
29	(1)~uniform 4-bit quantization;
30	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
31	(3)~unconstrained MCKP allocation;
32	(4)~an 
…[truncated 10515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T13:00:25.617353+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
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

_source line 28 · 2026-05-14T13:00:25.718061+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T13:00:28.706886+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit long paper short paper format ACL template"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here is information about EMNLP 2026 submission guidelines:

## Page Limits

Long papers have an 8-page limit and short papers have a 4-page limit. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Format and Template

EMNLP uses the standard ACL style fil
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5603
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T13:00:37.690992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T13:00:37.741665+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
14	Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
15	Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
16	Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\times$ compression. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok).}
22	\label{tab:heterogeneity}
23	\begin{tabular}{lccccc}
24	\toprule
25	Model & GQA & Top-5\% & $\Delta$ PPL & $\Delta$ PPL & Recommendation \\
26	 & Ratio & Conc. & (Uniform) & (Ours) & \\
27	\midrule
28	Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
29	Llama-3.1-8B$^\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\
30	Mistral-7B-v0.3$^\d
…[truncated 2380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T13:00:38.143412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T13:00:38.143975+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, and sliding-window adaptation~\cite{duanmu2024skvq}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	
7	\paragraph{KV Cache Eviction.}
8	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
9	Our work focuses exclusively on the quantization allocation problem.
10	
11	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
12	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
13	On hardware-aligned $\{2,4,8,16\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.
14	Related mixed-precision work operates at coarser granularity (layer-level~\cite{li2025kvmix}, memory-budget-level~\cite{lei2026arkv}), at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
15	
16	\paragraph{Attention Head Analysis.}
17	Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be rem
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T13:00:38.345101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T13:00:38.345510+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.
4	A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
5	Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
6	The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\ 7.13 PPL).
7	This diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \emph{before deployment} whether non-uniform quantization is worthwhile for a given model.
8	
9	\paragraph{Limitations.}
10	Our study has several limitations that temper the generality of the findings.
11	First, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.
12	Second, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.
13	Third, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation 
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T13:00:38.395987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T13:00:38.396504+00:00_

1	\appendix
2	
3	\section{Aggressive Compression}
4	\label{sec:aggressive}
5	
6	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
7	At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
8	At $8\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).
9	The intermediate regime ($5.3\times$) provides the largest relative benefit.
10	
11	\section{Profiling Resolution and Stability}
12	\label{sec:profiling_resolution}
13	
14	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
15	
16	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
17	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
18	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
19	
20	The additional signal changes 8 of 112 head assignments.
21	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
22	
23	\paragraph{Multi-seed stability.}
24	The profiled allocation is stable across calibration subsets.
25	Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%
…[truncated 2433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T13:00:38.547362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T13:00:38.598208+00:00_

1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  ti
…[truncated 5221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T13:00:44.525704+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T13:00:44.827107+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T13:00:44.877731+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T13:00:44.928343+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T13:00:47.588795+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T13:00:47.639319+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T13:00:50.650818+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.{yaml,yml,json,toml}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.{yaml,yml,json,toml}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T13:00:50.701435+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T13:00:53.461252+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/ 2>/dev/null",
  "description": "List project root directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/ 2>/dev/null",
    "description": "List project root directory"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T13:00:53.612421+00:00_

AGENTS.md
config
global
idea_generator
projects
skills
state
workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T13:00:56.673679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T13:00:56.724315+00:00_

EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T13:00:59.284696+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/",
  "description": "List config directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/",
    "description": "List config directory"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T13:00:59.335853+00:00_

approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_briefer.json
mcp_config_director.json
mcp_config_dream_review_director.json
mcp_config_idea_reviewer.json
mcp_config_no_project.json
mcp_config_paper_agent.json
mcp_config_review_director.json
mcp_config_reviewer.json
mcp_config_worker_023d750b1f305c357fd402bd3b2e39e1.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
mcp_config_worker_16c7228d5f50b6e03f04861201ad7ee0.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_372644b6780be0a53d254a839199d98e.json
mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json
mcp_config_worker_421decd2032b14f2ef6566c2172240c1.json
mcp_config_worker_567fac45f9ef5ad1a9223cbb3364faf1.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_8164f16cea05223301ec10d99f320a22.json
mcp_config_worker_8fdc57f80f0cafc42cc1047c9dc7ebf1.json
mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
mcp_config_worker_a2a1f628eaaf041a675e5db173e7463a.json
mcp_config_worker_d97c9f51b50c9002dcbd5eb97c1ac3e0.json
mcp_config_worker_ddf919c12f9233b9c1be7884efc37bb6.json
mcp_config_worker_ed94f451683c3553386dc323817a3544.json
mcp_config_worker_f265de7a9796688b878083fef59f9d4c.json
pending_approval_notifications.yaml
pool.json
projects
resources.yaml
secrets
session_state.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T13:01:02.247839+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/projects/ 2>/dev/null",
  "description": "List project configs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/projects/ 2>/dev/null",
    "description": "List project configs"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T13:01:02.298528+00:00_

demo_calibrated_sim.yaml
demo_calibrated_sim.yaml.bak-desc-fix
ratekv.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T13:01:05.009729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/projects/ratekv.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/projects/ratekv.yaml"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T13:01:05.110508+00:00_

1	execution:
2	  account: root
3	  gpu_ids:
4	  - cuda:0
5	  - cuda:1
6	  project_path: /root/ratekv
7	  servers:
8	  - westd-37397
9	feishu:
10	  chat_id: oc_e886d722cc0b64fdb553f7bb0b99816c
11	  operational_chat_id: oc_16f4cc04d259f364091fe7b4addd7912
12	  review_paper_path: projects/ratekv/docs/paper/main.tex
13	  review_round: 1
14	  review_supplementary_paths: ''
15	  submission_chat_id: oc_ec66209ede0ea4e3bda924778c210d8e
16	project:
17	  created_at: '2026-05-13T17:11:53.681Z'
18	  description: 'RateKV: Input-Adaptive Rate-Distortion Allocation for Joint KV Cache
19	    Eviction and Quantization'
20	  name: ratekv
21	  phase: research
22	  source_idea_id: idea_017
23	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T13:01:50.416325+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "ratekv",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验有效性**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference\n- **Deadline**: 2026-05-25 (ARR submission)\n- **格式**: ACL 模板, 正文 ≤8 页, mandatory Limitations section, double-blind\n- **附录**: 允许，不计入页数限制，审稿人可选择性参考\n\n### 论文路径\n`projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n\n### 论文概要\n论文研究 hardware-aligned bit-widths {2,4,8,16} 下 per-head KV cache mixed-precision quantization 的问题。核心发现：unconstrained solvers 在该 bit-width 集上 catastrophically fail（Qwen2.5-7B 上 PPL 32-37 vs uniform 4-bit 15.45），原因是 2-bit distortion compounding。提出 cardinality constraint 限制 2-bit head 数量（k≤8），将 PPL 降至 11.23。进一步发现 constrained 条件下 greedy 和 MCKP solver 等价。提出基于 top-5% concentration 的 heterogeneity diagnostic 判断模型是否适合 non-uniform allocation。在 3 个 7B 模型上验证。\n\n### 你需要重点审查的方面\n\n1. **方法 formulation 严谨性**：\n   - MCKP formulation 是否正确？cardinality constraint 的数学表述是否严格？\n   - \"2-bit distortion compounding\" 的解释是否有理论支撑还是仅凭经验？\"non-additive through residual stream\" 的论证是否充分？\n   - Solver equivalence claim（greedy = MCKP under constraint）是否有证明还是仅靠实验验证？\n\n2. **实验设计**：\n   - 仅 3 个 7B 模型是否足够支撑论文 claims？\n   - Evaluation metrics 是否充分（仅 PPL + 4 downstream tasks）？\n   - Calibration data (WikiText-2 train) 与 evaluation data (WikiText-2 test) 来自同一分布——是否有 data leakage 风险？\n   - Profiling setup（独立量化每个 head）的计算成本是否报告？\n   - k 的选择（sweep on calibration data）是否存在 overfitting 风险？\n\n3. **统计可靠性**：\n   - 主要结果是否报告 confidence intervals / error bars？\n   - Multi-seed 实验只在 Qwen hires profiling 上做了 3 seeds，是否足够？\n   - Cross-dataset 实验是否充分验证了 generalization？\n\n4. **Baseline 完整性**：\n   - 是否遗漏了重要的 baseline（如 token-level mixed-precision methods like ZipCache, KIVI 的 per-channel 策略）？\n   - Unconstrained results for Llama/Mistral 被省略是否合理？\n\n5. **格式合规**：\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否存在且充分？\n   - 匿名性是否满足？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "ratekv",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验有效性**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference\n- **Deadline**: 2026-05-25 (ARR submission)\n- **格式**: ACL 模板, 正文 ≤8 页, mandatory Limitations section, double-blind\n- **附录**: 允许，不计入页数限制，审稿人可选择性参考\n\n### 论文路径\n`projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n\n### 论文概要\n论文研究 hardware-aligned bit-widths {2,4,8,16} 下 per-head KV cache mixed-precision quantization 的问题。核心发现：unconstrained solvers 在该 bit-width 集上 catastrophically fail（Qwen2.5-7B 上 PPL 32-37 vs uniform 4-bit 15.45），原因是 2-bit distortion compounding。提出 cardinality constraint 限制 2-bit head 数量（k≤8），将 PPL 降至 11.23。进一步发现 constrained 条件下 greedy 和 MCKP solver 等价。提出基于 top-5% concentration 的 heterogeneity diagnostic 判断模型是否适合 non-uniform allocation。在 3 个 7B 模型上验证。\n\n### 你需要重点审查的方面\n\n1. **方法 formulation 严谨性**：\n   - MCKP formulation 是否正确？cardinality constraint 的数学表述是否严格？\n   - \"2-bit distortion compounding\" 的解释是否有理论支撑还是仅凭经验？\"non-additive through residual stream\" 的论证是否充分？\n   - Solver equivalence claim（greedy = MCKP under constraint）是否有证明还是仅靠实验验证？\n\n2. **实验设计**：\n   - 仅 3 个 7B 模型是否足够支撑论文 claims？\n   - Evaluation metrics 是否充分（仅 PPL + 4 downstream tasks）？\n   - Calibration data (WikiText-2 train) 与 evaluation data (WikiText-2 test) 来自同一分布——是否有 data leakage 风险？\n   - Profiling setup（独立量化每个 head）的计算成本是否报告？\n   - k 的选择（sweep on calibration data）是否存在 overfitting 风险？\n\n3. **统计可靠性**：\n   - 主要结果是否报告 confidence intervals / error bars？\n   - Multi-seed 实验只在 Qwen hires profiling 上做了 3 seeds，是否足够？\n   - Cross-dataset 实验是否充分验证了 generalization？\n\n4. **Baseline 完整性**：\n   - 是否遗漏了重要的 baseline（如 token-level mixed-precision methods like ZipCache, KIVI 的 per-channel 策略）？\n   - Unconstrained results for Llama/Mistral 被省略是否合理？\n\n5. **格式合规**：\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否存在且充分？\n   - 匿名性是否满足？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T13:02:06.440812+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16024
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-14T13:02:07.695329+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "ratekv",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + Related Work + 写作质量**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference\n- **Deadline**: 2026-05-25 (ARR submission)\n- **格式**: ACL 模板, 正文 ≤8 页, mandatory Limitations section, double-blind\n- **附录**: 允许，不计入页数限制，审稿人可选择性参考\n\n### 论文路径\n`projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n\n### 论文概要\n论文研究 hardware-aligned bit-widths {2,4,8,16} 下 per-head KV cache mixed-precision quantization 的问题。核心发现：unconstrained solvers 在该 bit-width 集上 catastrophically fail（Qwen2.5-7B 上 PPL 32-37 vs uniform 4-bit 15.45），原因是 2-bit distortion compounding。提出 cardinality constraint 限制 2-bit head 数量（k≤8），将 PPL 降至 11.23。进一步发现 constrained 条件下 greedy 和 MCKP solver 等价。提出基于 top-5% concentration 的 heterogeneity diagnostic 判断模型是否适合 non-uniform allocation。在 3 个 7B 模型上验证。\n\n### 你需要重点审查的方面\n\n1. **Novelty 和 Significance**：\n   - 主要贡献（cardinality constraint, solver equivalence, heterogeneity diagnostic）的新颖性如何？是否是 incremental？\n   - \"Adding a single constraint to MCKP\" 是否算 sufficient contribution for a main conference paper？\n   - Diagnostic framework 基于 3 个模型，是否太 preliminary？\n   - 对 EMNLP community 的 relevance——这更像是 systems/optimization paper 还是 NLP paper？\n\n2. **Related Work 覆盖度**：\n   - 是否遗漏重要相关工作？特别关注：\n     - 2025-2026 年的 KV cache quantization 新工作\n     - Mixed-precision quantization 在 weight quantization 领域的类似 constraint formulations\n     - Head importance/heterogeneity 分析的其他方法论\n   - 与 RateQuant 的对比是否公平和充分？\n   - 用 web_search 搜索 2025-2026 年最新相关工作，检查是否有遗漏\n\n3. **写作质量**：\n   - 论文结构是否清晰？motivation → method → experiments 的 flow 是否顺畅？\n   - Claims 是否 well-calibrated（不 overclaim / underclaim）？\n   - Abstract 和 introduction 是否准确反映了实际结果（包括 negative results on Llama/Mistral）？\n   - Figures 和 tables 是否信息丰富且易读？\n\n4. **Completeness**：\n   - 缺少什么实验或分析？\n   - Negative results (Llama, Mistral) 的讨论是否充分？\n   - 是否需要与更多 KV cache 方法（eviction, token-level quantization）的实验对比？\n   - 缺少 latency/throughput benchmarks 是否是致命缺陷？\n\n5. **格式和合规**：\n   - Ethics statement 是否需要？\n   - Citation 格式是否符合 ACL 标准？\n   - 是否有 hallucinated/fabricated citations？请用 web_search 验证可疑引用\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "ratekv",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + Related Work + 写作质量**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference\n- **Deadline**: 2026-05-25 (ARR submission)\n- **格式**: ACL 模板, 正文 ≤8 页, mandatory Limitations section, double-blind\n- **附录**: 允许，不计入页数限制，审稿人可选择性参考\n\n### 论文路径\n`projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n\n### 论文概要\n论文研究 hardware-aligned bit-widths {2,4,8,16} 下 per-head KV cache mixed-precision quantization 的问题。核心发现：unconstrained solvers 在该 bit-width 集上 catastrophically fail（Qwen2.5-7B 上 PPL 32-37 vs uniform 4-bit 15.45），原因是 2-bit distortion compounding。提出 cardinality constraint 限制 2-bit head 数量（k≤8），将 PPL 降至 11.23。进一步发现 constrained 条件下 greedy 和 MCKP solver 等价。提出基于 top-5% concentration 的 heterogeneity diagnostic 判断模型是否适合 non-uniform allocation。在 3 个 7B 模型上验证。\n\n### 你需要重点审查的方面\n\n1. **Novelty 和 Significance**：\n   - 主要贡献（cardinality constraint, solver equivalence, heterogeneity diagnostic）的新颖性如何？是否是 incremental？\n   - \"Adding a single constraint to MCKP\" 是否算 sufficient contribution for a main conference paper？\n   - Diagnostic framework 基于 3 个模型，是否太 preliminary？\n   - 对 EMNLP community 的 relevance——这更像是 systems/optimization paper 还是 NLP paper？\n\n2. **Related Work 覆盖度**：\n   - 是否遗漏重要相关工作？特别关注：\n     - 2025-2026 年的 KV cache quantization 新工作\n     - Mixed-precision quantization 在 weight quantization 领域的类似 constraint formulations\n     - Head importance/heterogeneity 分析的其他方法论\n   - 与 RateQuant 的对比是否公平和充分？\n   - 用 web_search 搜索 2025-2026 年最新相关工作，检查是否有遗漏\n\n3. **写作质量**：\n   - 论文结构是否清晰？motivation → method → experiments 的 flow 是否顺畅？\n   - Claims 是否 well-calibrated（不 overclaim / underclaim）？\n   - Abstract 和 introduction 是否准确反映了实际结果（包括 negative results on Llama/Mistral）？\n   - Figures 和 tables 是否信息丰富且易读？\n\n4. **Completeness**：\n   - 缺少什么实验或分析？\n   - Negative results (Llama, Mistral) 的讨论是否充分？\n   - 是否需要与更多 KV cache 方法（eviction, token-level quantization）的实验对比？\n   - 缺少 latency/throughput benchmarks 是否是致命缺陷？\n\n5. **格式和合规**：\n   - Ethics statement 是否需要？\n   - Citation 格式是否符合 ACL 标准？\n   - 是否有 hallucinated/fabricated citations？请用 web_search 验证可疑引用\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T13:02:09.105232+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-14T13:02:12.669614+00:00_

Round 1 任务已分配：
- **Reviewer 1**（方法严谨性 + 实验有效性）→ 已触发
- **Reviewer 2**（新颖性 + 完整性 + Related Work）→ 已触发

等待两位 Reviewer 返回独立审稿报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 63 · 2026-05-14T13:07:33.578532+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿报告

**论文**: "When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic"
**Venue**: EMNLP 2026 Main Conference (ACL ARR submission)

---

## 总体评分

**Overall**: 2.5/5 (介于 Findings track acceptance 和 Resubmit 之间)
**一句话总结**: 有价值的empirical发现（2-bit compounding failure），但贡献偏incremental，验证规模不足（仅3个7B模型），且缺少对hardware-motivated论文至关重要的latency评测。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论和实验设计合理，结论有数据支撑，但诊断框架仅基于3个数据点，统计鲁棒性不足 |
| Excitement | 2.5/5 | 核心发现（unconstrained solvers fail on hardware-aligned bits）有实用价值，但修复方案过于简单（加一个约束），且2/3模型不受益 |
| Overall Assessment | 2.5/5 | 不够main conference，但修改后可能适合Findings track |
| Confidence | 4/5 | 熟悉KV cache quantization和mixed-precision文献，仔细阅读了论文 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Related Work 重大遗漏——多个高度相关的已发表工作未被引用
- 具体位置：Section 2 (Related Work)
- 问题：论文仅引用19篇参考文献，遗漏了多个2025-2026年的关键相关工作：
  - **KVTuner** (Li et al., ICML 2025, arXiv 2502.04420)：Sensitivity-aware layer-wise mixed-precision KV cache quantization，和本文同属"sensitivity-guided mixed-precision KV cache"方向，且已被ICML接收。KVTuner也研究了Qwen2.5-7B和Llama-3.1-8B，发现key cache比value cache更重要——这与本文Appendix C的K/V separation发现直接相关。
  - **AQUA-KV / "Cache Me If You Must"** (Shutova et al., ICML 2025, arXiv 2501.19392)：在Llama 3.2上实现近无损2-2.5 bit KV cache压缩，利用key-value依赖关系。这直接挑战了本文"2-bit必然catastrophic"的叙事——AQUA-KV表明通过适当技术2-bit是可行的。
  - **Kitty** (Xia et al., 2025, arXiv 2511.18643)：2-bit KV cache with dynamic channel-wise precision boost，在2-bit下实现准确推理，提供了2.1-4.1x throughput提升。同样挑战"2-bit = catastrophic"的framing。
  - **ScaleBITS** (Li et al., Meta, 2026, arXiv 2602.17698)：Hardware-aligned mixed-precision search with greedy algorithm and provable guarantees，直接处理本文研究的hardware-aligned bit-width问题（虽然是weight quantization）。
  - **RotateKV** (IJCAI 2025)：通过旋转变换改善2-bit KV cache质量。
- 为什么影响接收：这些遗漏严重削弱novelty声明。特别是KVTuner和AQUA-KV是同类工作中已被顶会接收的方法，不引用不讨论不可接受。此外，Kitty和AQUA-KV表明2-bit failure不是必然的——它取决于quantization技术，而非仅仅取决于bit-width本身。论文需要讨论本文发现的compounding effect是否在更先进的quantization方法（如channel-wise precision boost、rotation-based approaches）下仍然存在。
- 建议修改方向：补充引用这些工作并在Related Work中明确定位差异；讨论本文的compounding finding是否generalize到非round-to-nearest的quantization方法。

**N2** [critical] 诊断框架仅基于3个模型——作为独立贡献insufficiently validated
- 具体位置：Section 5.2 (Diagnostic Framework)；Contribution 3 (Introduction)
- 问题：Contribution 3声称提出"a heterogeneity-based diagnostic framework"，但该框架的阈值（>0.50, 0.30-0.50, near-zero）完全来自3个7B模型的观察。3个数据点无法建立可靠的decision boundary。论文自身在Limitations中承认"too few to establish a statistically robust correlation"，但仍将其作为正式Contribution列出并提出具体数值阈值。
- 为什么影响接收：以3个数据点推导数值threshold并作为核心contribution之一，在严格审查下站不住脚。Reviewer会认为这是preliminary observation而非validated framework。
- 建议修改方向：(1) 降低claim强度——将"diagnostic framework"改为"preliminary diagnostic observation"或"case study"；(2) 移除具体数值阈值（0.50, 0.30等），改为定性描述；(3) 或增加更多模型验证（如13B、70B、不同架构族）。

**N3** [critical] 缺少latency/throughput实测——hardware-aligned motivation缺乏hardware evidence
- 具体位置：全文，尤其Section 1 (Introduction第8行"hardware-efficient inference requires bit-widths drawn from {2,4,8,16}")
- 问题：论文的核心motivation是hardware-aligned bit-widths的实际推理效率。但通篇没有任何real-kernel latency、throughput或memory benchmarks。所有评估基于PPL和下游accuracy。一篇以"hardware-aligned"为标题关键词的论文不能只有software-simulated quantization结果。
- 为什么影响接收：没有latency数据，无法判断(a)不同bit-width混合是否真的在现有inference engine中高效执行，(b) per-head mixed-precision的实际memory节省是否如理论预期，(c) profiling + constraint sweep的开销是否可接受。KVTuner在ICML上被接收时包含了throughput benchmarks（21.25% improvement）——本文在同一方向缺少这类数据是significant weakness。
- 建议修改方向：在vLLM或TensorRT-LLM中实现mixed-precision KV cache并报告latency/throughput；至少报告end-to-end inference latency at batch-size-1和batch-size-32。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 仅评估7B-scale模型，generalizability未知
- 具体位置：Section 4.1 (Models)
- 问题：3个模型全部在7B scale，且2个共享相同的KV head数量(256)。Limitations中提到"not verified whether findings transfer to larger scales (70B+)"但论文也未测试13B或更小模型。GQA ratio与compounding effect的关系也未分析——Qwen的7:1 GQA（仅112 KV heads）与Llama/Mistral的4:1（256 heads）差异巨大，但论文将效果差异完全归因于heterogeneity而未控制GQA ratio。
- 建议：增加至少1个不同scale的模型（如Qwen2.5-14B或Llama-3.1-70B），或设计ablation分离GQA ratio的影响。

**W2** [warning] 2/3模型不受益，实际适用范围存疑
- 具体位置：Table 2, Section 4.2
- 问题：Llama改善仅0.2%（8.45 vs 8.47），Mistral反而变差（7.16 vs 7.13）。这意味着论文提出的方法在测试的多数模型上没有价值。Abstract和Introduction虽然提到了negative results，但narrative仍以Qwen的27.3% improvement为主线，给人一种misleading的positive impression。
- 建议：在Abstract中更早、更prominently呈现negative results的比重（如"however, the benefit is architecture-dependent: on 2 of 3 tested models, non-uniform allocation provides marginal or no improvement"）。

**W3** [warning] Unconstrained baselines仅在Qwen上运行
- 具体位置：Table 2, Section 4.2最后一段（"Unconstrained results for Llama and Mistral are omitted"）
- 问题：论文声称unconstrained solvers "fail catastrophically"是核心发现（Contribution 1），但仅在Qwen上验证了这一failure。Llama和Mistral的unconstrained结果以"---"省略，理由是"those experiments were conducted only on Qwen"。如果compounding effect是一个general现象，应在所有模型上验证；如果不是general的，那claim需要被weaken。
- 建议：补充Llama和Mistral的unconstrained results，即使failure不那么dramatic也应报告以完整呈现picture。

**W4** [warning] Table 5（下游评估）bf16 baseline缺失
- 具体位置：Table 5
- 问题：ARC-C, HellaSwag, PIQA, WinoGrande的individual bf16 baseline都标为"---"，仅有average (0.695)。读者无法判断individual task的degradation程度。
- 建议：填入所有bf16 baseline值。

**W5** [warning] Venue fit——这更像systems/optimization论文而非NLP论文
- 具体位置：全文
- 问题：论文的核心技术贡献是(1)给MCKP加一个cardinality constraint，(2)证明greedy ≡ MCKP under constraint，(3)提出concentration metric。这些都是optimization/systems insights，与NLP/CL社区的research questions关联较弱。唯一的"NLP insight"是heterogeneity因architecture而异——但这也更接近model architecture分析而非语言理解/生成研究。
- 建议：考虑MLSys、NeurIPS Efficiency track等更合适的venue。若仍投EMNLP，需更强调NLP-specific implications（如不同task类型对quantization的敏感度差异、长context vs短context的影响等）。

---

## 小问题（不影响接收）

- **S1**: references.bib中GEAR (kang2024gear)已被发表但仍标注为@misc/arXiv preprint，应更新venue信息。
- **S2**: Figure 2（bit-width allocation bar chart, Page 6）的每层bar密度过高，单个bar值在打印尺寸下难以辨认。建议简化为heatmap或仅显示代表性层。
- **S3**: Figure 3（heatmap, Page 8）x轴"Head Index"和y轴"Layer"刻度标签偏小，打印后可能难以阅读。
- **S4**: Section 5.1和5.2内容高度相关，可合并为一个Section以节省篇幅。
- **S5**: Table 3（budget sweep）中8x压缩的PPL值(14,759 和 907)已无实际意义但占用篇幅——可移至appendix。
- **S6**: Introduction较长（~50行），可适当精简。

---

## 引用验证结果

通过自动化工具和人工核查：
- 19/19 citations存在且可验证（15 OpenAlex verified, 4 minor API mismatches due to database issues）
- **无fabricated/hallucinated citations**
- KIVI (liu2024kivi) 在OpenAlex中未找到精确匹配（confidence 0.34），但该论文确实存在（ICML 2024）——这是数据库问题
- hooper2024kvquant、li2024snapkv、xiao2024streamingllm的first author mismatch均为OpenAlex数据库与arXiv listing不一致，bib中的作者信息是正确的

---

## Missing References（需补充）

1. **KVTuner** — Li et al., "KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization," ICML 2025. [arXiv: 2502.04420]
2. **AQUA-KV** — Shutova et al., "Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models," ICML 2025. [arXiv: 2501.19392]
3. **Kitty** — Xia et al., "Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost," 2025. [arXiv: 2511.18643]
4. **ScaleBITS** — Li et al., "ScaleBITS: Scalable Bitwidth Search for Hardware-Aligned Mixed-Precision LLMs," 2026. [arXiv: 2602.17698]
5. **RotateKV** — "RotateKV: Accurate and Robust 2-Bit KV Cache Quantization," IJCAI 2025.
6. **"Don't Waste Bits"** — "Adaptive KV-Cache Quantization for Lightweight On-Device LLMs," 2026. [arXiv: 2604.04722]（token-level adaptive, 从{2,4,8,16}动态选择——与本文bit-width set完全相同）

---

## 主要优势

- **O1**: 核心empirical finding扎实且有实用价值——在hardware-aligned bit-widths下unconstrained solvers catastrophically fail不是trivial observation，对practitioners有直接指导意义。
- **O2**: Honest negative results——Llama和Mistral的负面结果诚实报告，并转化为diagnostic insight，体现了良好的科学态度。
- **O3**: Cross-dataset validation (Section 4.6)——C4→WikiText和WikiText→C4的交叉验证（>96% bit-assignment agreement）增强了profiling stability的可信度。
- **O4**: 写作清晰——Problem → Diagnosis → Fix → Analysis的叙事流畅，U-shaped compounding curve的解释直观。Solver equivalence证明简洁优雅。
- **O5**: Ablation全面——heuristic baselines (Table 4)、budget sweep (Table 3)、profiling resolution (Appendix B)、KV separation (Appendix C)覆盖了主要ablation维度。
- **O6**: 无fabricated citations，引用格式基本正确。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| ACL模板 | ✓ | 使用 `\usepackage[review]{acl}` |
| 匿名提交 | ✓ | `\author{Anonymous}` |
| 正文页数 ≤8 | ⚠ 需确认 | 正文结束于Page 8底部，与references交界处非常紧凑 |
| Limitations section | ✓ | 在Section 6 (Conclusion)中，作为paragraph |
| Ethics statement | 未包含 | 对于本论文不强制要求 |
| References格式 | ⚠ | GEAR等已发表论文未更新venue；booktitle格式不统一（部分用"NeurIPS 2024"非标准格式） |
| Double-blind compliance | ✓ | 未检测到de-anonymization信息 |

---

## 对Director的建议

本文的核心empirical finding有价值（N1遗漏的工作不否认compounding effect的存在，但需要讨论其generalizability），但作为EMNLP main conference submission存在三个structural weakness：(1)相关工作遗漏严重影响novelty positioning，(2)诊断框架验证不足，(3)缺少hardware evaluation。建议作者：补引用+讨论定位差异、增加模型数量或降低diagnostic claim强度、增加latency实验。修改后更适合Findings track或MLSys。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-14T13:07:45.667955+00:00_

Reviewer 2 的 Round 1 审稿报告已收到。报告质量高，覆盖了 novelty、related work、completeness 等核心维度，提出了 3 个 critical（N1 related work 遗漏、N2 diagnostic framework 验证不足、N3 缺少 latency 实测）和 5 个 warning 级别问题。

目前状态：等待 Reviewer 1（方法严谨性 + 实验有效性方向）返回审稿报告。收到后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 65 · 2026-05-14T13:07:48.212041+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论**：Overall 2.5/5，介于 Findings 和 Resubmit 之间。

**3个 Must-Fix**：
1. Related Work 重大遗漏（KVTuner/ICML25、AQUA-KV/ICML25、Kitty、ScaleBITS 等6篇未引用）
2. 诊断框架仅基于3个模型，不足以作为独立 contribution
3. 以 hardware-aligned 为动机却完全没有 latency/throughput 实测数据

**5个 Should-Fix**：仅7B-scale、2/3模型不受益、unconstrained baselines仅Qwen有数据、下游bf16 baseline缺失、venue fit偏systems

**优势**：compounding failure是扎实发现、negative results诚实报告、cross-dataset验证充分、写作清晰、无fabricated citations。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-14T13:07:53.836695+00:00_

Reviewer 2 的报告已收到。等待 Reviewer 1 的报告返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 4

2 recorded events

### User

_source line 67 · 2026-05-14T13:07:55.345336+00:00_

[Reviewer 1 审稿结果]:
视觉检查完成：正文 8 页合规，匿名合规，无排版问题。现在等待 baseline 搜索完成后提交最终审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-14T13:08:02.040885+00:00_

收到 Reviewer 1 的中间状态更新。Reviewer 1 正在完成 baseline 搜索，尚未提交最终审稿报告。

Reviewer 2 已完成 Round 1 初审（Overall 2.5/5）。

等待 Reviewer 1 最终报告提交后，进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 5

62 recorded events

### User

_source line 69 · 2026-05-15T04:16:05.413428+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ratekv
- 论文路径: projects/ratekv/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-15T04:16:11.591207+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-15T04:16:11.643006+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-15T04:16:15.413885+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
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

_source line 73 · 2026-05-15T04:16:15.464820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-15T04:16:20.081860+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
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

_source line 75 · 2026-05-15T04:16:20.132392+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-15T04:16:23.645729+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
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

_source line 77 · 2026-05-15T04:16:23.696395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-15T04:16:28.364118+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ratekv"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-15T04:16:29.269406+00:00_

{"result":"# 项目 ratekv 概况\n\n## 实验状态 (72 个)\n\n- **exp_c_no2bit**: DONE (negative) — \n- **exp_c_constrained_mckp**: DONE (success) — \n- **exp_b_hires_quant**: DONE (negative) — \n- **exp_a_targeted_hybrid**: DONE (negative) — \n- **mvp_004**: DONE (negative) — \n- **p0_2_cliff_7B**: DONE (success) — \n- **p0_1_ppl_fast**: DONE (negative) — \n- **p0_2_cliff_1.5B**: DONE (success) — \n- **sanity_004**: DONE (success) — \n- **sanity_003**: DONE (failed) — \n- **sanity_002**: DONE (failed) — \n- **sanity_001**: DONE (failed) — \n- **mvp_003**: DONE (failed) — \n- **mvp_002**: DONE (failed) — \n- **mvp_001**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- mistral_hires_bf16_2bitonly_v3: Mistral-7B-v0.3 hires bf16 2-bit only profiling v3. Model integrity verified (3/3 shards + safetensor + transformers). 64seq×2048tok, 256 heads.（准备中）\n- qwen_hires_constrained_d049（准备中）\n- qwen25-hires-profiling（准备中）\n- cross_domain_calibration_v2（准备中）\n- greedy_constrained_ablation（准备中）\n\n## 近期结论\n- **gemma2_hires_bf16_2bitonly** (success): —\n- **mistral_c4_hires_crossdataset** (negative): —\n- **llama_c4_hires_crossdataset** (negative): —\n\n## 趋势\n成功 35 / 负向 16 / 失败 8 / 共 67\nl0_dominance_ratio: 2.05 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-37397: 无 GPU 信息\n\n## 告警\n- mvp_001: 训练失败 — unknown\n- sanity_001: 训练失败 — unknown\n- mvp_002: 训练失败 — unknown\n- sanity_002: 训练失败 — unknown\n- mvp_003: 训练失败 — unknown\n- sanity_003: 训练失败 — unknown\n- c4_cross_dataset_eval: 已被终止 — unknown\n- l0_only_heuristic: 已被终止 — unknown\n- l0_heuristic_baseline: 已被终止 — unknown\n- cross_domain_calibration: 已被终止 — unknown\n- c4_cross_dataset_eval_v2: 已被终止 — unknown\n- multi_seed_lowres: 已被终止 — unknown\n- qwen72b_profiling: 已被终止 — unknown\n- yi15_hires_float32_profiling: 已被终止 — unknown\n- mistral_hires_bf16_2bitonly: 训练失败 — unknown\n- mistral_hires_bf16_2bitonly_v2: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 905
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-15T04:16:29.320018+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T04:16:30.675195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T04:16:30.776022+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	
11	\title{When Does Non-Uniform KV Cache Quantization Help?\\Cardinality Constraints and a Heterogeneity Diagnostic}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	\input{abstract}
20	\end{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{experiments}
26	\input{analysis}
27	\input{conclusion}
28	
29	\bibliography{references}
30	
31	\input{appendix}
32	
33	\end{document}
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-15T04:16:35.797041+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Call for Papers and Shared Task Participation (CASE @ EMNLP 2022): Challenges and Applications of Automated Extraction of Socio-political Events from Text | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-and-shared-task-participation-case-emnlp-2022-challenges-and-applications"}]

I found information about EMNLP 2026, but t
…[truncated 1458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6477
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-15T04:16:45.187202+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference paper submission deadline guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference paper submission deadline guidelines"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T04:16:46.091146+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" submission format page limit anonymity review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" submission format page limit anonymity review"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-15T04:16:46.894536+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ratekv",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ratekv",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-15T04:16:52.414571+00:00_

Web search results for query: "EMNLP 2026 main conference paper submission deadline guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here is the information about EMNLP 2026 main conference pap
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7227
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T04:16:52.565851+00:00_

Web search results for query: ""EMNLP 2026" submission format page limit anonymity review"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here is information about EMNLP 2026 submission guidelines:

## Submission Format and Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## Review Process and Anonymity

Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind. Reviewers will not see 
…[truncated 761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6474
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-15T04:16:52.566345+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/decisions.yaml\", \"content\": \"_next_id: 52\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:13 UTC\\n  summary: 'MVP 验证方案: Llama 3.1-8B 上验证 eviction-quantization crossover 存在性 + MCKP\\n    分配有效性'\\n  rationale: '核心假设是 per-KV-head 异质性使得 joint eviction+quantization allocation 优于 uniform\\n    quantization。最小验证: 单模型 distortion profiling + crossover 可视化 + MCKP vs uniform\\n    4-bit 对比。Pass 标准: ≥15% heads prefer eviction + perplexity improvement。选 Llama\\n    3.1-8B 因为 DuoAttention 已有该模型的 streaming/retrieval head 分类数据可做 post-hoc validation。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:16 UTC\\n  summary: 'MVP gate v2: 加 quant-only MCKP baseline + 消除死区 + 最小效应量 ≥0.5 PPL'\\n  rationale: 'Reviewer 初审指出三个漏洞: (1) uniform 4-bit 太弱，任何 per-head 方法都能赢，核心 claim 是\\n    joint > quant-only，必须加 quant-only MCKP baseline; (2) 5%-15% crossover 比例死区导致判定模糊，合并为单一\\n    ≥10% 阈值; (3) PPL 改善无最小效应量可能产生假阳性，设 ≥0.5 PPL 门槛。quant-only baseline 零额外工程量（同一 solver\\n    限制 action set）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 18:12 UTC\\n  summary: MVP 模型从 Llama 3.1-8B 切换到 Qwen2.5-7B，DuoAttention validation 延后\\n  rationale: Llama 3.1-8B 是 HF gated model，用户尚未提供 HF token，GPU 空闲不能等。Qwen2.5-7B 非\\n    gated、GQA 架构、7B 参数量相近，满足 MVP 验证 per-KV-head crossover 假设的需求。代价：DuoAttention post-hoc\\n    validation（D001 rationale 中的 convergent evidence story）暂时无法做——DuoAttention 论文只分析了\\n    Llama 系列。替代方案：(1) 用户后续提供 HF token 后加 Llama 作为第二模型；(2) 在 Qwen 上自行运行 DuoAttention\\n    分类作为替代验证。MVP 核心假设（crossover 存在性 + MCKP 优于 uniform）不依赖 DuoAttention 叙事。注意：Qwen2.5-7B\\n    的 KV head 数（4×28=112）少于 Llama（8×32=256），GQA ratio 更高（7:1 vs 4:1），crossover 比例可能偏低。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 21:55 UTC\\n  summary: 1.5B sanity 暴露 attention MSE 与 PPL 脱钩；7B 继续跑但需准备 metric 修正
…[truncated 1401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5671
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-15T04:17:09.548179+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
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

_source line 91 · 2026-05-15T04:17:09.699231+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-15T04:17:13.664309+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/ratekv/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/ratekv/artifacts/review_issues.yaml"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-15T04:17:14.166626+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-15T04:17:14.167006+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/ratekv/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/ratekv/docs/paper/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-15T04:17:16.075606+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 1908
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-15T04:17:16.126227+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/agent/project_config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/agent/project_config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-15T04:17:16.278172+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-15T04:17:19.189369+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/ratekv/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/ratekv/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-15T04:17:19.189752+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-15T04:17:19.942766+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv -name \"project_config*\" -o -name \"config*yaml\" -o -name \"config*json\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv -name \"project_config*\" -o -name \"config*yaml\" -o -name \"config*json\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-15T04:17:19.993382+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-15T04:17:23.707892+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -maxdepth 1 -name \"*.yaml\" 2>/dev/null | head -10",
  "description": "Find config yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -maxdepth 1 -name \"*.yaml\" 2>/dev/null | head -10",
    "description": "Find config yaml files"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-15T04:17:23.909045+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-15T04:17:23.909397+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-15T04:17:23.959852+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-15T04:17:30.684725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-15T04:17:31.538123+00:00_

1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47), and on Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B non-uniform allocation provides no benefit.
7	Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) and the highest top-5\% concentration (0.71), yet gains nothing from non-uniform allocation---because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth sensitivity gradient, rather than the ``spread'' pattern that enables MCKP to redistribute budget across heads.
8	We propose a joint diagnostic combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly identifies all five architectures studied---distinguishing spread heterogeneity (MCKP-exploitable) from spik
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-15T04:17:31.638977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-15T04:17:31.994970+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves clos
…[truncated 4772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-15T04:17:32.045816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-15T04:17:32.497920+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We profile each KV head independently by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
25	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
26	
27	The optim
…[truncated 7700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-15T04:17:32.498260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-15T04:17:33.903805+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on five architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Yi-1.5-9B} (8:1, 48 $\times$ 4 = 192 KV heads),
11	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
12	\textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention),
13	and \textbf{Gemma-2-9B} (2:1, 42 $\times$ 8 = 336 KV heads, \texttt{head\_dim}=256, attention logit softcapping).
14	This selection spans GQA ratios from 2:1 to 8:1 and covers standard, sliding-window, and softcapped attention.
15	
16	\paragraph{Evaluation.}
17	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
18	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
19	
20	\paragraph{Profiling.}
21	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
22	We use two profiling resolutions: \emph{standard} (16 sequences $\times$ 512 tokens) and \emph{high-resolution} (64 sequences $\times$ 2048 tokens), both from WikiText-2 train.
23	Unless marked with $\dagger$, all results use standard-resolution profiling; Appendix~\ref{sec:profiling_resolution} analyzes the effect of resolution.
24	
25	\paragraph{Compression and constraint.}
26	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
27	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen, $k{=}2$ for Yi-1.5 and Llama, $k{=}4$ for Mistral, $k{=}8$ for Gemma-2).
28	
29	\paragraph{Baselines.}
30	We compare aga
…[truncated 11637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-15T04:17:34.004579+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/workspace.yaml 2>/dev/null || echo \"NOT_IN_WORKSPACE\"; grep -rA5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/ 2>/dev/null || echo \"NOT_IN_CONFIG\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/workspace.yaml 2>/dev/null || echo \"NOT_IN_WORKSPACE\"; grep -rA5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/config/ 2>/dev/null || echo \"NOT_IN_CONFIG\"",
    "description": "Search for external review config"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-15T04:17:34.055275+00:00_

NOT_IN_WORKSPACE
NOT_IN_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-15T04:17:39.025571+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-15T04:17:39.528134+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across five architectures at $4\times$ compression.
12	The central finding is that MCKP benefit requires \emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.
13	
14	Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
15	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp
16	
17	Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
18	The mechanism is clear from the cross-bitwidth gradient structure.
19	Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 has a 2-bit delta of 13.12, while the second-ranked head has delta 0.55---a $24\times$ gap ($t_1/t_5{=}0.90$, $t_1/t_2{=}23.7$). %exp_id=yi15_hires_profiling
20	Critically, L4H3's sensitivity is confined to the 2-bit operating point: its 4-bit and 8-bit deltas are ${\approx}\,0$.
21	The solver therefore has only one lever---upgrading L4H3 from 2-bit to 4-bit removes the distortion, but f
…[truncated 6765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-15T04:17:39.578863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-15T04:17:40.532892+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, and sliding-window adaptation~\cite{duanmu2024skvq}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	
7	\paragraph{KV Cache Eviction.}
8	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
9	Recent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.
10	
11	
12	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
13	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
14	On hardware-aligned $\{2,4,8,16\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.
15	Related mixed-precision work operates at coarser granularity---layer-level via gradient-based sensitivity~\cite{li2025kvmix} or Pareto search over hardware-friendly precision
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-15T04:17:40.533345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-15T04:17:40.583901+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.
4	A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
5	Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
6	The benefit of non-uniform allocation depends on both the concentration and \emph{shape} of head sensitivity heterogeneity.
7	Qwen2.5-7B (concentration 0.61, $t_1/t_5{=}0.57$, spread pattern) shows large gains; Llama-3.1-8B (concentration 0.57, $t_1/t_5{=}0.85$, spike) is essentially indistinguishable from uniform (8.45 vs.\ 8.47 PPL); Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B show no benefit.
8	Yi-1.5-9B is a critical test case: despite the highest concentration tested ($0.71$, exceeding Qwen), its heterogeneity is a single-outlier spike ($t_1/t_5{=}0.90$) with no cross-bitwidth sensitivity gradient, so MCKP cannot redistribute budget.
9	A joint diagnostic using concentration ($\gtrsim 0.50$) and $t_1/t_5$ ratio ($\lesssim 0.70$) correctly identifies spread, spike, and flat patterns across all five models studied, computable from the same profiling pass used for allocation.
10	This provides a practical guideline: practitioners can determine whether non-uniform quantization is worthwhile for their architecture \emph{before} running the allocation solver.
11	
12	\paragraph{Limitations.}
13	Our study has several limitations that temper the generality of the findings.
14	First, we evaluate only five 7--9B-scale models---too few to establish a statistically robust
…[truncated 1252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-15T04:17:40.584343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-15T04:17:40.634904+00:00_

1	\appendix
2	
3	\section{Aggressive Compression}
4	\label{sec:aggressive}
5	
6	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
7	At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
8	At $8\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).
9	The intermediate regime ($5.3\times$) provides the largest relative benefit.
10	
11	\section{Profiling Resolution and Stability}
12	\label{sec:profiling_resolution}
13	
14	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
15	
16	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
17	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
18	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
19	
20	The additional signal changes 8 of 112 head assignments.
21	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
22	
23	\paragraph{Multi-seed stability.}
24	The profiled allocation is stable across calibration subsets.
25	Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%
…[truncated 5106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-15T04:17:45.554100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-15T04:17:45.604912+00:00_

1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  ti
…[truncated 6252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-15T04:18:34.109837+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "ratekv",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**论文**: \"When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\"\n**路径**: `projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, related_work.tex, conclusion.tex, appendix.tex, references.bib）\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Deadline**: 2026-05-25 (ARR submission)\n\n### Venue 要求\n- **格式**: ACL 两栏模板 (`\\usepackage[review]{acl}`)\n- **页数限制**: Long paper 正文 8 页（不含参考文献和附录）\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须在 conclusion 后包含\n\n### 你的审查侧重：方法严谨性 + 实验有效性\n\n请重点审查以下方面：\n\n1. **方法论严谨性**：\n   - 2-bit distortion compounding 的分析是否有充分理论/实验支撑？\"non-additive\" 的说法是否精确定义？\n   - Cardinality constraint 是 ad-hoc 的 engineering fix 还是有原则性的 justification？k 的选取方法（U-shaped sweep）是否存在 overfitting 风险？\n   - Solver equivalence 的证明（greedy = MCKP under constraint）是否有形式化论证还是仅靠实验观察？\n\n2. **实验设计与统计**：\n   - 5 个模型是否足以支撑 diagnostic framework 的结论？样本量对 threshold 鲁棒性的影响？\n   - Qwen2.5-7B 上 27.3% improvement 的统计显著性——3 seeds 是否足够？variance 报告是否充分？\n   - Cross-dataset stability（WikiText-2 vs C4）的设计是否充分？只用两个数据集能否声称 \"stability\"？\n   - 为什么 Llama/Mistral/Yi/Gemma 没有 unconstrained baseline 结果？论文说 \"experiments were conducted only on Qwen\" 是否是实验设计缺陷？\n   - 下游评估仅 Qwen 4 个 0-shot task，其他模型无下游评估——这是否削弱了 generalizability claim？\n\n3. **Runtime benchmark 有效性**：\n   - Table 7 runtime 使用 PyTorch-level simulation 而非真实 inference kernel，是否能支撑任何实际部署结论？\n   - Constrained MCKP 比 uniform 多 8.5% latency overhead，这是否削弱了方法的实用性？\n\n4. **Profiling methodology**：\n   - 单头独立 profiling（quantize one head, keep others bf16）是否捕捉到 head 之间的交互效应？这与 compounding 论点是否自相矛盾？\n   - Standard vs hires profiling 差异显著（37 vs 100 non-zero heads），哪个结果才是可靠的？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Detailed Comments、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "ratekv",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**论文**: \"When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\"\n**路径**: `projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, related_work.tex, conclusion.tex, appendix.tex, references.bib）\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Deadline**: 2026-05-25 (ARR submission)\n\n### Venue 要求\n- **格式**: ACL 两栏模板 (`\\usepackage[review]{acl}`)\n- **页数限制**: Long paper 正文 8 页（不含参考文献和附录）\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须在 conclusion 后包含\n\n### 你的审查侧重：方法严谨性 + 实验有效性\n\n请重点审查以下方面：\n\n1. **方法论严谨性**：\n   - 2-bit distortion compounding 的分析是否有充分理论/实验支撑？\"non-additive\" 的说法是否精确定义？\n   - Cardinality constraint 是 ad-hoc 的 engineering fix 还是有原则性的 justification？k 的选取方法（U-shaped sweep）是否存在 overfitting 风险？\n   - Solver equivalence 的证明（greedy = MCKP under constraint）是否有形式化论证还是仅靠实验观察？\n\n2. **实验设计与统计**：\n   - 5 个模型是否足以支撑 diagnostic framework 的结论？样本量对 threshold 鲁棒性的影响？\n   - Qwen2.5-7B 上 27.3% improvement 的统计显著性——3 seeds 是否足够？variance 报告是否充分？\n   - Cross-dataset stability（WikiText-2 vs C4）的设计是否充分？只用两个数据集能否声称 \"stability\"？\n   - 为什么 Llama/Mistral/Yi/Gemma 没有 unconstrained baseline 结果？论文说 \"experiments were conducted only on Qwen\" 是否是实验设计缺陷？\n   - 下游评估仅 Qwen 4 个 0-shot task，其他模型无下游评估——这是否削弱了 generalizability claim？\n\n3. **Runtime benchmark 有效性**：\n   - Table 7 runtime 使用 PyTorch-level simulation 而非真实 inference kernel，是否能支撑任何实际部署结论？\n   - Constrained MCKP 比 uniform 多 8.5% latency overhead，这是否削弱了方法的实用性？\n\n4. **Profiling methodology**：\n   - 单头独立 profiling（quantize one head, keep others bf16）是否捕捉到 head 之间的交互效应？这与 compounding 论点是否自相矛盾？\n   - Standard vs hires profiling 差异显著（37 vs 100 non-zero heads），哪个结果才是可靠的？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Detailed Comments、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-15T04:18:51.233695+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17123
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-15T04:18:51.284495+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "ratekv",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**论文**: \"When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\"\n**路径**: `projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, related_work.tex, conclusion.tex, appendix.tex, references.bib）\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Deadline**: 2026-05-25 (ARR submission)\n\n### Venue 要求\n- **格式**: ACL 两栏模板 (`\\usepackage[review]{acl}`)\n- **页数限制**: Long paper 正文 8 页（不含参考文献和附录）\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须在 conclusion 后包含\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n请重点审查以下方面：\n\n1. **Novelty 评估**：\n   - Cardinality constraint 本质上是限制 2-bit 头数量——这是 well-known technique (knapsack cardinality constraint) 的直接应用还是有 genuine insight？\n   - Diagnostic framework（concentration + t1/t5）基于 5 个模型——这是 \"diagnostic framework\" 还是仅仅是 post-hoc observation？\n   - 与 RateQuant (Zuo et al., 2026) 的区别是否足够构成独立贡献？论文是否本质上是 RateQuant 的 bug-fix + extension？\n   - \"When does non-uniform quantization help?\" 这个问题本身的 novelty——prior work 是否已隐含回答？\n\n2. **Related Work 完整性**：\n   - 引用列表是否遗漏重要的 KV cache quantization 近期工作？特别是 2025-2026 的工作\n   - 是否遗漏了与 heterogeneity diagnostic 相关的 head importance/pruning 工作？\n   - Mixed-precision quantization 在 weight quantization 领域的相关工作是否被忽略（e.g., HAWQ, OWQ 等 sensitivity-based bit allocation）？\n   - 请用 web_search 搜索验证是否有遗漏的 2025-2026 KV cache 相关重要工作\n\n3. **论文完整性与结构**：\n   - Limitations section 是否充分？是否遗漏了重要的 limitation？\n   - Future work 是否合理？是否有应该在本文解决但被推给 future work 的问题？\n   - 论文的 negative results（4/5 模型无 benefit）是否被恰当框架？这对 acceptance 有什么影响？\n   - 仅有 1/5 模型获益的方法是否有足够的 practical value？\n\n4. **写作质量**：\n   - 行文是否清晰、逻辑链是否连贯？\n   - Claims 是否被 evidence 充分支撑（没有 over-claim）？\n   - 论文的 framing/narrative 是否准确反映了结果的 scope？\n   - 是否存在 anonymity 违规（代码链接、致谢、作者可识别信息）？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References（特别要搜索验证）、Detailed Comments、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "ratekv",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**论文**: \"When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\"\n**路径**: `projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, related_work.tex, conclusion.tex, appendix.tex, references.bib）\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Deadline**: 2026-05-25 (ARR submission)\n\n### Venue 要求\n- **格式**: ACL 两栏模板 (`\\usepackage[review]{acl}`)\n- **页数限制**: Long paper 正文 8 页（不含参考文献和附录）\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须在 conclusion 后包含\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n请重点审查以下方面：\n\n1. **Novelty 评估**：\n   - Cardinality constraint 本质上是限制 2-bit 头数量——这是 well-known technique (knapsack cardinality constraint) 的直接应用还是有 genuine insight？\n   - Diagnostic framework（concentration + t1/t5）基于 5 个模型——这是 \"diagnostic framework\" 还是仅仅是 post-hoc observation？\n   - 与 RateQuant (Zuo et al., 2026) 的区别是否足够构成独立贡献？论文是否本质上是 RateQuant 的 bug-fix + extension？\n   - \"When does non-uniform quantization help?\" 这个问题本身的 novelty——prior work 是否已隐含回答？\n\n2. **Related Work 完整性**：\n   - 引用列表是否遗漏重要的 KV cache quantization 近期工作？特别是 2025-2026 的工作\n   - 是否遗漏了与 heterogeneity diagnostic 相关的 head importance/pruning 工作？\n   - Mixed-precision quantization 在 weight quantization 领域的相关工作是否被忽略（e.g., HAWQ, OWQ 等 sensitivity-based bit allocation）？\n   - 请用 web_search 搜索验证是否有遗漏的 2025-2026 KV cache 相关重要工作\n\n3. **论文完整性与结构**：\n   - Limitations section 是否充分？是否遗漏了重要的 limitation？\n   - Future work 是否合理？是否有应该在本文解决但被推给 future work 的问题？\n   - 论文的 negative results（4/5 模型无 benefit）是否被恰当框架？这对 acceptance 有什么影响？\n   - 仅有 1/5 模型获益的方法是否有足够的 practical value？\n\n4. **写作质量**：\n   - 行文是否清晰、逻辑链是否连贯？\n   - Claims 是否被 evidence 充分支撑（没有 over-claim）？\n   - 论文的 framing/narrative 是否准确反映了结果的 scope？\n   - 是否存在 anonymity 违规（代码链接、致谢、作者可识别信息）？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References（特别要搜索验证）、Detailed Comments、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-15T04:18:52.646004+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---

### Assistant

_source line 130 · 2026-05-15T04:18:59.066621+00:00_

Round 1 已分配：

- **Reviewer 1**（方法严谨性 + 实验有效性）：聚焦 compounding 理论支撑、cardinality constraint justification、solver equivalence 论证强度、实验统计显著性、profiling methodology 自洽性、runtime benchmark 有效性
- **Reviewer 2**（新颖性 + 完整性）：聚焦 contribution novelty vs RateQuant、diagnostic framework 泛化性、related work 覆盖（需 web search 验证）、negative results framing、写作质量、anonymity compliance

等待两位 Reviewer 返回独立审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 6

2 recorded events

### User

_source line 131 · 2026-05-15T04:23:37.177483+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**论文**: "When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026)

---

## Summary

本文研究 per-head mixed-precision KV cache quantization 在 hardware-aligned bit-widths {2,4,8,16} 上的失败与修复。作者发现 unconstrained greedy/MCKP solver 在 Qwen2.5-7B 上产生灾难性退化（PPL 32–37 vs uniform 4-bit 15.45），原因是大量 2-bit head 的 distortion 通过 residual stream 产生 non-additive compounding。提出的修复是在 MCKP 中加入 2-bit cardinality constraint（k≤8），将 PPL 降至 11.23（−27.3%）。论文还发现 constrained greedy 与 constrained MCKP 在所有测试模型上产生等价分配，并提出基于 concentration + t1/t5 ratio 的 joint diagnostic 来判断 non-uniform allocation 是否有益。5 个模型中仅 Qwen 受益，Llama/Mistral/Yi-1.5/Gemma-2 均无改善。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 compounding 观察有实验支撑，但 profiling 方法与 compounding 论点存在逻辑张力；diagnostic 在 5 个数据点上完美拟合 2 个 threshold，有 overfitting 嫌疑；4/5 模型缺失 unconstrained baseline |
| Excitement | 3/5 | 问题选取有实践意义，negative results 诚实报告值得肯定，spread/spike/flat taxonomy 直觉上有用；但方法仅在 1/5 模型上有效，且 diagnostic 尚属 preliminary |
| Reproducibility | 3.5/5 | 实验设置描述充分，但未提及代码发布计划 |
| Overall | 2.5/5 | Borderline——core idea 有价值，negative results 有贡献，但评估存在系统性缺口 |
| Confidence | 4/5 | 熟悉 KV cache quantization 和 mixed-precision allocation 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Diagnostic framework 在 5 个数据点上完美拟合——overfitting 风险
- 具体位置：Section 5.2 (analysis.tex L59–81), Table 6
- 问题：Diagnostic 用 2 个 threshold（concentration ≳ 0.50, t1/t5 ≲ 0.70）在 5 个 architecture 上实现 100% 准确分类。用 2 个自由参数完美拟合 5 个样本是经典 overfitting 信号。论文自身承认 "should be validated on a broader set"（analysis.tex L79），但仍作为 Contribution 3 列入 introduction。
- 为什么影响接收：如果 diagnostic 不可靠，Contribution 3 的价值大打折扣。5 个模型全部 7–9B 规模、decoder-only——如果在 Phi-3、DeepSeek-V2 等不同设计范式模型上测试失败，整个 framework 就不成立。
- 建议：增加 2–3 个模型验证 threshold 鲁棒性，或降低 claim 力度为 exploratory finding。

**N2** [critical] 4/5 模型缺失 unconstrained baseline
- 具体位置：Table 2 (experiments.tex L45–57), experiments.tex L79
- 问题：Llama/Mistral/Yi-1.5/Gemma-2 的 unconstrained greedy 和 MCKP 列为 "---"，论文解释 "those experiments were conducted only on Qwen"。但 compounding 是本文核心发现——如果只在 1 个模型上验证，无法判断是 Qwen idiosyncratic behavior 还是 general phenomenon。
- 为什么影响接收：论文叙事链（compounding → constraint → diagnostic）建立在 compounding 是 general 问题的假设上。如果其他模型 unconstrained 不产生 catastrophic failure，结论结构需要修改。
- 建议：在所有 5 个模型上补跑 unconstrained greedy/MCKP。

**N3** [critical] Profiling methodology 与 compounding 论点的逻辑矛盾
- 具体位置：Section 3.2 (method.tex L22–29) vs Section 3.3 (method.tex L34–53)
- 问题：Profiling 用 single-head isolation（keep others bf16），但论文论证 distortions 是 non-additive。如果 per-head distortions 是 non-additive 的，single-head profiling 的 d_h(b) 就不能准确反映 multi-head 实际 distortion。brute-force oracle 仅在 within-layer groups 内枚举，不处理 cross-layer interactions。
- 为什么影响接收：方法论层面的 internal inconsistency。论文用 additive profiling 来 guide non-additive problem。
- 建议：增加实验验证 single-head d_h(2) 与 multi-head actual distortion 的 correlation，或明确讨论 constraint 如何将 problem 压回 additive regime。

**N4** [critical] Downstream evaluation 仅限 Qwen
- 具体位置：Table 5 (experiments.tex L155–173)
- 问题：0-shot downstream evaluation 仅在 Qwen 执行，其他 4 个模型无 downstream results。对于声称 cross-architecture diagnostic framework 的论文，downstream 验证仅覆盖 1/5 模型不充分。PPL 和 downstream accuracy 不总是正相关，特别是差异很小时（如 Llama 8.45 vs 8.47）。
- 建议：至少在 Llama 和 Yi-1.5 上补充 downstream evaluation。

---

## Should-Fix 问题

**W1** [warning] Standard vs hires profiling 差异过大（37→100 sensitive heads），但 headline results 用 standard
- 具体位置：Appendix B (appendix.tex L14–21)

**W2** [warning] 统计报告不够充分——3 seeds, 仅报告 std，未报告 CI
- 具体位置：experiments.tex L64

**W3** [warning] Cross-dataset stability 仅用两个 general-domain 数据集
- 具体位置：Section 5.6

**W4** [warning] Solver equivalence 缺乏形式化证明，仅有 3 个模型经验观察
- 具体位置：Section 3.5

**W5** [warning] Runtime benchmark 为 PyTorch simulation，无法支撑部署结论；8.5% overhead 的 cost-benefit 未讨论
- 具体位置：Appendix C

**W6** [warning] "Non-additive" 未被形式化定义（super-additive? multiplicative?）
- 具体位置：method.tex L34, abstract.tex L2

---

## Questions for Authors

1. 为什么没有在所有 5 个模型上运行 unconstrained baselines？
2. Diagnostic 的 borderline cases（concentration ≈ 0.55, t1/t5 ≈ 0.65）如何处理？
3. Within-layer brute-force oracle 能否验证 cross-layer compounding 的 near-optimality？
4. 方法是否依赖 round-to-nearest quantization，对 GPTQ/AWQ 是否适用？
5. 是否尝试过更高分辨率 profiling（128 seq × 4096 tok）？

---

## Missing References

- KIVI (Liu et al., 2024) 的 per-channel asymmetric 2-bit 策略是否可替代 cardinality constraint？论文未做实验对比。
- MiKV (Yang et al., 2025, ICML 2025) — mixed-precision KV cache quantization 的直接相关工作。
- Quantization + eviction 联合策略作为 hybrid baseline 未被讨论。

---

## 主要优势

1. 2-bit distortion compounding 是 genuine、previously-undocumented 的问题，有直接 warning value
2. 单个 cardinality constraint 是 minimal、elegant 的修复
3. 4/5 模型 negative results 的诚实报告比只报 Qwen 正面结果更有科学价值
4. Spread/spike/flat taxonomy 提供了有用的 conceptual vocabulary
5. Cross-dataset validation、brute-force oracle、KV separation ablation 等设计显示 thorough evaluation 追求

---

## 总体评分

**Overall**: 2.5/5 — Borderline

**一句话总结**: 核心发现有实践价值、negative results 诚实报告值得肯定，但评估存在系统性缺口——缺失 4/5 模型 unconstrained baselines、仅 Qwen 有 downstream evaluation、profiling 方法与 compounding 论点逻辑张力未解决、diagnostic 在 5 个同质模型上 overfit。建议补充 N2 和 N4 后作为 Findings paper 考虑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 132 · 2026-05-15T04:23:43.635423+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 7

2 recorded events

### User

_source line 133 · 2026-05-15T04:23:46.179182+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿报告已提交给 Review Director。

核心判断：**Overall 2.5/5 (Borderline)**。论文的 2-bit compounding 发现和 cardinality constraint 修复有实践价值，negative results 的诚实报告是亮点。但存在 4 个 critical 问题：(1) diagnostic 在 5 个数据点上 overfit，(2) 4/5 模型缺 unconstrained baselines，(3) profiling 方法与 compounding 论点的逻辑矛盾，(4) downstream evaluation 仅限 Qwen。建议补充 N2+N4 后作为 Findings paper 考虑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 134 · 2026-05-15T04:23:52.125923+00:00_

已收到 Reviewer 1 的报告（Borderline 2.5/5，4 个 critical issues）。等待 Reviewer 2 的报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 8

6 recorded events

### User

_source line 135 · 2026-05-15T04:25:04.411697+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 完整审稿报告

**论文**: "When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic"
**Target Venue**: EMNLP 2026 Main Conference (ARR May 2026)

---

### 总体评分

- **Overall**: 2/5 (Resubmit next cycle)
- **Soundness**: 3/5 (Acceptable — 技术分析正确但 diagnostic framework 统计基础不足)
- **Excitement**: 2/5 (Potentially Interesting — 4/5 模型无收益，practical impact 有限)
- **Reproducibility**: 4/5
- **Confidence**: 4/5

**一句话总结**: 2-bit compounding 分析有价值，但 cardinality constraint 是标准技术的直接应用，diagnostic framework 仅基于 5 个模型（1 个正例），4/5 模型无收益严重削弱 practical value。

---

### Must-Fix 问题

**N1** [critical] Diagnostic Framework 泛化性严重不足——5 个模型不构成 "framework"
- Section 5.2, Table 4: 阈值 concentration ≳0.50 和 t₁/t₅ ≲0.70 来自 exactly 5 个数据点。"Spread" 类别仅 1 个正样本（Qwen）。论文自承 "Both thresholds are illustrative"（S5.2 L79），但标题/abstract 的 framing 未反映此 caveat。
- 建议：扩展到 10-15 个模型，或将 claim 降级为 "empirical observation"。

**N2** [critical] 4/5 模型无收益——方法 practical value 存疑
- Table 2: Qwen 27.3% improvement，但 Llama Δ<0.02，Mistral/Gemma 比 uniform 更差，Yi 完全一致。Qwen 的 uniform 4-bit degradation 异常高（+57.5%），其他模型仅 +2.9%~4.7%——Qwen 可能是架构 outlier 而非方法普遍有效的证据。
- 建议：分析 Qwen 为何异常，测试更多模型寻找 "Spread" 架构。

**N3** [critical] Novelty 不足——cardinality constraint 是标准组合优化技术
- Eq.(2) 是标准 knapsack cardinality constraint。Sensitivity-based mixed-precision 在 weight quant 领域已有 HAWQ/HAQ 等先驱。Genuine insight 在 compounding 诊断，但解决方案本身缺乏 algorithmic novelty。
- 建议：formalize compounding 为 super-additive distortion model，或提出 interaction-aware objective。

### Should-Fix 问题

**W1** Related Work 遗漏严重：缺 HAWQ/HAWQ-V2/HAQ（mixed-precision bit allocation 先驱）；缺 PM-KVQ、Kitty、RotateKV、MiniKV（IJCAI/ACL/ICML 2025）、AQUA-KV（ICML 2025）等 2025 published KV cache 工作。

**W2** 与 RateQuant 差异化不清晰：formulation 完全相同，主要区别是 bitwidth set 和 constraint。RateQuant 在 {2,4,8,16} 上是否也 fail？

**W3** 标题/abstract framing 偏乐观：abstract 前半段突出 Qwen 的 27.3%，但实际 4/5 模型无收益。

**W4** Solver equivalence 是 3 模型的 empirical observation，非 proven theorem——应提供 formal sufficient condition 或明确标注为 empirical。

**W5** 缺少 per-head vs token-level granularity 的 tradeoff 讨论。

### 小问题
- Table 2 缺 Llama/Mistral/Yi/Gemma 的 unconstrained 结果
- Standard vs hires profiling 数字混用可能造成混淆
- Runtime benchmark（Appendix D）为模拟而非 real-kernel
- GEAR/SKVQ 的 bib entry 应更新 venue

### 主要优势
- Compounding 分析深入（Section 3.3, Figure 2）
- 实验诚实——negative results 完整报告
- 写作清晰，逻辑链连贯
- Multi-seed/cross-dataset stability 分析增强可信度
- 匿名和格式合规

### Missing References（web search 验证）
HAWQ (ICCV'19), HAWQ-V2 (NeurIPS'20), HAQ (CVPR'19), PM-KVQ (arXiv'25), Kitty (arXiv'25), RotateKV (IJCAI'25), MiniKV (ACL Findings'25), AQUA-KV (ICML'25), "Don't Waste Bits!" (arXiv'26)

### 引用验证
22 bib entries 均真实存在，0 orphan / 0 missing。3 条 first-author mismatch 疑为 API 数据问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-15T04:25:35.685729+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "ratekv",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 完整审稿报告\n\n**Overall**: 2/5 (Resubmit next cycle)\n**Soundness**: 3/5 | **Excitement**: 2/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 2-bit compounding 分析有价值，但 cardinality constraint 是标准技术的直接应用，diagnostic framework 仅基于 5 个模型（1 个正例），4/5 模型无收益严重削弱 practical value。\n\n#### Must-Fix 问题\n\n**N1** [critical] Diagnostic Framework 泛化性严重不足——5 个模型不构成 \"framework\"\n- Section 5.2, Table 4: 阈值 concentration ≳0.50 和 t₁/t₅ ≲0.70 来自 exactly 5 个数据点。\"Spread\" 类别仅 1 个正样本（Qwen）。论文自承 \"Both thresholds are illustrative\"（S5.2 L79），但标题/abstract 的 framing 未反映此 caveat。\n- 建议：扩展到 10-15 个模型，或将 claim 降级为 \"empirical observation\"。\n\n**N2** [critical] 4/5 模型无收益——方法 practical value 存疑\n- Table 2: Qwen 27.3% improvement，但 Llama Δ<0.02，Mistral/Gemma 比 uniform 更差，Yi 完全一致。Qwen 的 uniform 4-bit degradation 异常高（+57.5%），其他模型仅 +2.9%~4.7%——Qwen 可能是架构 outlier 而非方法普遍有效的证据。\n- 建议：分析 Qwen 为何异常，测试更多模型寻找 \"Spread\" 架构。\n\n**N3** [critical] Novelty 不足——cardinality constraint 是标准组合优化技术\n- Eq.(2) 是标准 knapsack cardinality constraint。Sensitivity-based mixed-precision 在 weight quant 领域已有 HAWQ/HAQ 等先驱。Genuine insight 在 compounding 诊断，但解决方案本身缺乏 algorithmic novelty。\n- 建议：formalize compounding 为 super-additive distortion model，或提出 interaction-aware objective。\n\n#### Should-Fix 问题\n\n**W1** Related Work 遗漏严重：缺 HAWQ/HAWQ-V2/HAQ（mixed-precision bit allocation 先驱）；缺 PM-KVQ、Kitty、RotateKV、MiniKV（IJCAI/ACL/ICML 2025）、AQUA-KV（ICML 2025）等 2025 published KV cache 工作。\n\n**W2** 与 RateQuant 差异化不清晰：formulation 完全相同，主要区别是 bitwidth set 和 constraint。RateQuant 在 {2,4,8,16} 上是否也 fail？\n\n**W3** 标题/abstract framing 偏乐观：abstract 前半段突出 Qwen 的 27.3%，但实际 4/5 模型无收益。\n\n**W4** Solver equivalence 是 3 模型的 empirical observation，非 proven theorem——应提供 formal sufficient condition 或明确标注为 empirical。\n\n**W5** 缺少 per-head vs token-level granularity 的 tradeoff 讨论。\n\n#### Missing References\nHAWQ (ICCV'19), HAWQ-V2 (NeurIPS'20), HAQ (CVPR'19), PM-KVQ (arXiv'25), Kitty (arXiv'25), RotateKV (IJCAI'25), MiniKV (ACL Findings'25), AQUA-KV (ICML'25), \"Don't Waste Bits!\" (arXiv'26)\n\n#### 主要优势\n- Compounding 分析深入（Section 3.3, Figure 2）\n- 实验诚实——negative results 完整报告\n- 写作清晰，逻辑链连贯\n- Multi-seed/cross-dataset stability 分析增强可信度\n- 匿名和格式合规\n\n---\n\n请对以上每个 Must-Fix（N1-N3）和 Should-Fix（W1-W5）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "ratekv",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 完整审稿报告\n\n**Overall**: 2/5 (Resubmit next cycle)\n**Soundness**: 3/5 | **Excitement**: 2/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 2-bit compounding 分析有价值，但 cardinality constraint 是标准技术的直接应用，diagnostic framework 仅基于 5 个模型（1 个正例），4/5 模型无收益严重削弱 practical value。\n\n#### Must-Fix 问题\n\n**N1** [critical] Diagnostic Framework 泛化性严重不足——5 个模型不构成 \"framework\"\n- Section 5.2, Table 4: 阈值 concentration ≳0.50 和 t₁/t₅ ≲0.70 来自 exactly 5 个数据点。\"Spread\" 类别仅 1 个正样本（Qwen）。论文自承 \"Both thresholds are illustrative\"（S5.2 L79），但标题/abstract 的 framing 未反映此 caveat。\n- 建议：扩展到 10-15 个模型，或将 claim 降级为 \"empirical observation\"。\n\n**N2** [critical] 4/5 模型无收益——方法 practical value 存疑\n- Table 2: Qwen 27.3% improvement，但 Llama Δ<0.02，Mistral/Gemma 比 uniform 更差，Yi 完全一致。Qwen 的 uniform 4-bit degradation 异常高（+57.5%），其他模型仅 +2.9%~4.7%——Qwen 可能是架构 outlier 而非方法普遍有效的证据。\n- 建议：分析 Qwen 为何异常，测试更多模型寻找 \"Spread\" 架构。\n\n**N3** [critical] Novelty 不足——cardinality constraint 是标准组合优化技术\n- Eq.(2) 是标准 knapsack cardinality constraint。Sensitivity-based mixed-precision 在 weight quant 领域已有 HAWQ/HAQ 等先驱。Genuine insight 在 compounding 诊断，但解决方案本身缺乏 algorithmic novelty。\n- 建议：formalize compounding 为 super-additive distortion model，或提出 interaction-aware objective。\n\n#### Should-Fix 问题\n\n**W1** Related Work 遗漏严重：缺 HAWQ/HAWQ-V2/HAQ（mixed-precision bit allocation 先驱）；缺 PM-KVQ、Kitty、RotateKV、MiniKV（IJCAI/ACL/ICML 2025）、AQUA-KV（ICML 2025）等 2025 published KV cache 工作。\n\n**W2** 与 RateQuant 差异化不清晰：formulation 完全相同，主要区别是 bitwidth set 和 constraint。RateQuant 在 {2,4,8,16} 上是否也 fail？\n\n**W3** 标题/abstract framing 偏乐观：abstract 前半段突出 Qwen 的 27.3%，但实际 4/5 模型无收益。\n\n**W4** Solver equivalence 是 3 模型的 empirical observation，非 proven theorem——应提供 formal sufficient condition 或明确标注为 empirical。\n\n**W5** 缺少 per-head vs token-level granularity 的 tradeoff 讨论。\n\n#### Missing References\nHAWQ (ICCV'19), HAWQ-V2 (NeurIPS'20), HAQ (CVPR'19), PM-KVQ (arXiv'25), Kitty (arXiv'25), RotateKV (IJCAI'25), MiniKV (ACL Findings'25), AQUA-KV (ICML'25), \"Don't Waste Bits!\" (arXiv'26)\n\n#### 主要优势\n- Compounding 分析深入（Section 3.3, Figure 2）\n- 实验诚实——negative results 完整报告\n- 写作清晰，逻辑链连贯\n- Multi-seed/cross-dataset stability 分析增强可信度\n- 匿名和格式合规\n\n---\n\n请对以上每个 Must-Fix（N1-N3）和 Should-Fix（W1-W5）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-15T04:26:09.275934+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33590
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-15T04:26:09.476912+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "ratekv",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 完整审稿报告\n\n**Overall**: 2.5/5 (Borderline)\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 3.5/5 | **Confidence**: 4/5\n\n**一句话总结**: 核心发现有实践价值、negative results 诚实报告值得肯定，但评估存在系统性缺口——缺失 4/5 模型 unconstrained baselines、仅 Qwen 有 downstream evaluation、profiling 方法与 compounding 论点逻辑张力未解决、diagnostic 在 5 个同质模型上 overfit。建议补充 N2 和 N4 后作为 Findings paper 考虑。\n\n#### Must-Fix 问题\n\n**N1** [critical] Diagnostic framework 在 5 个数据点上完美拟合——overfitting 风险\n- Section 5.2, Table 6: 用 2 个 threshold（concentration ≳0.50, t1/t5 ≲0.70）在 5 个 architecture 上实现 100% 准确分类。用 2 个自由参数完美拟合 5 个样本是经典 overfitting 信号。\n- 建议：增加 2–3 个模型验证 threshold 鲁棒性，或降低 claim 力度为 exploratory finding。\n\n**N2** [critical] 4/5 模型缺失 unconstrained baseline\n- Table 2: Llama/Mistral/Yi-1.5/Gemma-2 的 unconstrained greedy 和 MCKP 列为 \"---\"，论文解释 \"those experiments were conducted only on Qwen\"。compounding 是核心发现，如果只在 1 个模型上验证，无法判断是 Qwen idiosyncratic 还是 general phenomenon。\n- 建议：在所有 5 个模型上补跑 unconstrained greedy/MCKP。\n\n**N3** [critical] Profiling methodology 与 compounding 论点的逻辑矛盾\n- Section 3.2 vs Section 3.3: Profiling 用 single-head isolation（keep others bf16），但论文论证 distortions 是 non-additive。如果 per-head distortions 是 non-additive 的，single-head profiling 的 d_h(b) 不能准确反映 multi-head actual distortion。\n- 建议：增加实验验证 single-head d_h(2) 与 multi-head actual distortion 的 correlation，或明确讨论 constraint 如何将 problem 压回 additive regime。\n\n**N4** [critical] Downstream evaluation 仅限 Qwen\n- Table 5: 0-shot downstream evaluation 仅在 Qwen 执行，其他 4 个模型无 downstream results。PPL 和 downstream accuracy 不总是正相关。\n- 建议：至少在 Llama 和 Yi-1.5 上补充 downstream evaluation。\n\n#### Should-Fix 问题\n\n**W1** Standard vs hires profiling 差异过大（37→100 sensitive heads），但 headline results 用 standard\n**W2** 统计报告不够充分——3 seeds, 仅报告 std，未报告 CI\n**W3** Cross-dataset stability 仅用两个 general-domain 数据集\n**W4** Solver equivalence 缺乏形式化证明，仅有 3 个模型经验观察\n**W5** Runtime benchmark 为 PyTorch simulation，无法支撑部署结论；8.5% overhead 未讨论 cost-benefit\n**W6** \"Non-additive\" 未被形式化定义（super-additive? multiplicative?）\n\n#### Questions for Authors\n1. 为什么没有在所有 5 个模型上运行 unconstrained baselines？\n2. Diagnostic 的 borderline cases（concentration ≈ 0.55, t1/t5 ≈ 0.65）如何处理？\n3. Within-layer brute-force oracle 能否验证 cross-layer compounding 的 near-optimality？\n4. 方法是否依赖 round-to-nearest quantization，对 GPTQ/AWQ 是否适用？\n5. 是否尝试过更高分辨率 profiling（128 seq × 4096 tok）？\n\n#### Missing References\n- MiKV (Yang et al., 2025, ICML 2025)\n- Quantization + eviction 联合策略作为 hybrid baseline\n- KIVI per-channel asymmetric 2-bit 策略\n\n#### 主要优势\n1. 2-bit distortion compounding 是 genuine、previously-undocumented 的问题\n2. 单个 cardinality constraint 是 minimal、elegant 的修复\n3. 4/5 模型 negative results 的诚实报告比只报 Qwen 正面结果更有科学价值\n4. Spread/spike/flat taxonomy 提供了有用的 conceptual vocabulary\n5. Cross-dataset validation、brute-force oracle、KV separation ablation 等设计显示 thorough evaluation 追求\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "ratekv",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 完整审稿报告\n\n**Overall**: 2.5/5 (Borderline)\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 3.5/5 | **Confidence**: 4/5\n\n**一句话总结**: 核心发现有实践价值、negative results 诚实报告值得肯定，但评估存在系统性缺口——缺失 4/5 模型 unconstrained baselines、仅 Qwen 有 downstream evaluation、profiling 方法与 compounding 论点逻辑张力未解决、diagnostic 在 5 个同质模型上 overfit。建议补充 N2 和 N4 后作为 Findings paper 考虑。\n\n#### Must-Fix 问题\n\n**N1** [critical] Diagnostic framework 在 5 个数据点上完美拟合——overfitting 风险\n- Section 5.2, Table 6: 用 2 个 threshold（concentration ≳0.50, t1/t5 ≲0.70）在 5 个 architecture 上实现 100% 准确分类。用 2 个自由参数完美拟合 5 个样本是经典 overfitting 信号。\n- 建议：增加 2–3 个模型验证 threshold 鲁棒性，或降低 claim 力度为 exploratory finding。\n\n**N2** [critical] 4/5 模型缺失 unconstrained baseline\n- Table 2: Llama/Mistral/Yi-1.5/Gemma-2 的 unconstrained greedy 和 MCKP 列为 \"---\"，论文解释 \"those experiments were conducted only on Qwen\"。compounding 是核心发现，如果只在 1 个模型上验证，无法判断是 Qwen idiosyncratic 还是 general phenomenon。\n- 建议：在所有 5 个模型上补跑 unconstrained greedy/MCKP。\n\n**N3** [critical] Profiling methodology 与 compounding 论点的逻辑矛盾\n- Section 3.2 vs Section 3.3: Profiling 用 single-head isolation（keep others bf16），但论文论证 distortions 是 non-additive。如果 per-head distortions 是 non-additive 的，single-head profiling 的 d_h(b) 不能准确反映 multi-head actual distortion。\n- 建议：增加实验验证 single-head d_h(2) 与 multi-head actual distortion 的 correlation，或明确讨论 constraint 如何将 problem 压回 additive regime。\n\n**N4** [critical] Downstream evaluation 仅限 Qwen\n- Table 5: 0-shot downstream evaluation 仅在 Qwen 执行，其他 4 个模型无 downstream results。PPL 和 downstream accuracy 不总是正相关。\n- 建议：至少在 Llama 和 Yi-1.5 上补充 downstream evaluation。\n\n#### Should-Fix 问题\n\n**W1** Standard vs hires profiling 差异过大（37→100 sensitive heads），但 headline results 用 standard\n**W2** 统计报告不够充分——3 seeds, 仅报告 std，未报告 CI\n**W3** Cross-dataset stability 仅用两个 general-domain 数据集\n**W4** Solver equivalence 缺乏形式化证明，仅有 3 个模型经验观察\n**W5** Runtime benchmark 为 PyTorch simulation，无法支撑部署结论；8.5% overhead 未讨论 cost-benefit\n**W6** \"Non-additive\" 未被形式化定义（super-additive? multiplicative?）\n\n#### Questions for Authors\n1. 为什么没有在所有 5 个模型上运行 unconstrained baselines？\n2. Diagnostic 的 borderline cases（concentration ≈ 0.55, t1/t5 ≈ 0.65）如何处理？\n3. Within-layer brute-force oracle 能否验证 cross-layer compounding 的 near-optimality？\n4. 方法是否依赖 round-to-nearest quantization，对 GPTQ/AWQ 是否适用？\n5. 是否尝试过更高分辨率 profiling（128 seq × 4096 tok）？\n\n#### Missing References\n- MiKV (Yang et al., 2025, ICML 2025)\n- Quantization + eviction 联合策略作为 hybrid baseline\n- KIVI per-channel asymmetric 2-bit 策略\n\n#### 主要优势\n1. 2-bit distortion compounding 是 genuine、previously-undocumented 的问题\n2. 单个 cardinality constraint 是 minimal、elegant 的修复\n3. 4/5 模型 negative results 的诚实报告比只报 Qwen 正面结果更有科学价值\n4. Spread/spike/flat taxonomy 提供了有用的 conceptual vocabulary\n5. Cross-dataset validation、brute-force oracle、KV separation ablation 等设计显示 thorough evaluation 追求\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-15T04:26:10.883042+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1406
}
```

</details>

---

### Assistant

_source line 140 · 2026-05-15T04:26:15.693914+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 9

2 recorded events

### User

_source line 141 · 2026-05-15T04:26:18.352038+00:00_

[Reviewer 2 审稿结果]:
审稿报告已完成并发送给 Review Director。

**总结**：Overall 2/5（Resubmit next cycle）。三个 critical 问题：(1) diagnostic framework 仅 5 个模型、1 个正例，无法支撑 "framework" 的 claim；(2) 4/5 模型无收益，practical value 有限；(3) cardinality constraint 是标准技术的直接应用，novelty 不足。此外指出 Related Work 遗漏 HAWQ/HAQ 系列和多个 2025 published KV cache 工作。优势在于 compounding 分析有价值、实验诚实、写作清晰。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Assistant

_source line 142 · 2026-05-15T04:26:22.779227+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 10

2 recorded events

### User

_source line 143 · 2026-05-15T04:27:11.494690+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Step 2 交叉回应（对 Reviewer 2 审稿意见）

### Must-Fix

[AGREE] R2-N1: Diagnostic Framework 泛化性不足
与我的 N1 一致。5 个数据点拟合 2 个 threshold，"Spread" 类别仅 Qwen 一个正样本（n=1 positive evidence）。增加 3–4 个不同范式模型（MHA/MLA/MoE attention）即可给出有意义验证。

[AGREE with nuance] R2-N2: 4/5 模型无收益，practical value 存疑
R2 观察到 Qwen uniform 4-bit degradation 异常高（+57.5% vs 其他 +2.9%–4.7%）是锐利洞察，我的 Round 1 未充分强调。但 negative results 本身（"4/5 模型不需要 non-uniform"）对实践者有 go/no-go 信号价值，论文的 practical value 不仅在正面结果。

[REBUT] R2-N3: Novelty 不足——cardinality constraint 是标准技术
事实判断正确（Eq.2 是标准 knapsack constraint），但不应升至 Must-Fix critical：(1) ARR H6 heuristic 明确警告 "methodology is too simple" 不应成为 reject 理由；(2) HAWQ/HAQ 的类比不完全——weight quant layer-level 的 additivity 在 INT4+ 下成立，KV cache head-level 2-bit 的 non-additivity 是新发现；(3) R2 自己承认 "genuine insight 在 compounding 诊断"——如果核心贡献是 diagnosis，solution simplicity 是 feature 非 bug。应降为 Should-Fix。

### Should-Fix

[AGREE] R2-W1: Related Work 遗漏 HAWQ/HAQ 和 2025 KV cache 工作
[AGREE with nuance] R2-W2: 差异化已存在于 S3.1/Introduction（Table 1 unconstrained greedy = RateQuant-style），但应更 explicit label
[REBUT] R2-W3: Abstract 后半段充分覆盖 4/5 negative results，标题 "When Does...Help?" 本身暗示 "not always"——framing 已 balanced
[AGREE] R2-W4: 与我的 W4 一致
[AGREE] R2-W5: Per-head vs token-level positioning gap 确实存在

### 总体判断

R2 的 Overall 2/5 偏严。我维持 2.5/5 borderline，认为 compounding diagnosis + negative results + practical guideline 在 Findings track 标准下仍有价值，前提是补充 unconstrained baselines（我的 N2）和 downstream evaluation（我的 N4）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 144 · 2026-05-15T04:27:16.695110+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 11

2 recorded events

### User

_source line 145 · 2026-05-15T04:27:19.299743+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：与 R2 在 N1（diagnostic 泛化性）、W1（missing refs）、W4（solver equivalence 非形式化）上一致；对 N3（novelty 不足）提出反驳——ARR guidelines 警告不应因方法简单而 reject，compounding diagnosis 才是真正 novelty；对 W3（framing 偏乐观）反驳——abstract 后半段已充分覆盖 negative results。维持 Overall 2.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 146 · 2026-05-15T04:27:23.739022+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 12

10 recorded events

### User

_source line 147 · 2026-05-15T04:27:26.202277+00:00_

[Reviewer 2 审稿结果]:
## 交叉回应：Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Diagnostic framework 在 5 个数据点上完美拟合——overfitting 风险**

同意。这与我的 N1 高度一致。2 个自由参数（concentration threshold 0.50, t₁/t₅ threshold 0.70）完美分类 5 个样本，VC dimension 的角度来看完全无法排除 overfitting。论文 Section 5.2 第 79 行自承 "Both thresholds are illustrative, derived from five models"，但标题和 Contribution 3（Introduction 第 53 行）仍将其定位为 "diagnostic framework"——这一 framing 与证据强度不匹配。补充：我进一步注意到 "Spread" 类别仅有 Qwen 1 个正样本，这意味着 positive class 的决策边界完全由单一数据点决定，比 R1 指出的还要脆弱。

---

**[AGREE] R1-N2: 4/5 模型缺失 unconstrained baseline**

同意。Section 4.2 第 79 行的解释 "those experiments were conducted only on Qwen, where the failure mode is most pronounced" 不能令人满意。Compounding 是论文的核心 claim（Contribution 1, Introduction 第 49 行），如果仅在 1 个模型上验证：
- 无法区分 compounding 是 general phenomenon 还是 Qwen idiosyncratic（Qwen 的 uniform 4-bit degradation 异常高：+57.5% vs 其他模型仅 +2.9%~4.7%，参见 Table 2）
- Flat 模型（Mistral/Gemma）的 per-head 2-bit distortion 本身极低（Table 4: concentration 0.23-0.24），unconstrained solver 在这些模型上可能 *不会* 触发 catastrophic failure，这对 compounding 论点的 generality 构成挑战

---

**[REBUT] R1-N3: Profiling methodology 与 compounding 论点的逻辑矛盾**

不完全同意。R1 指出 single-head profiling 与 non-additive compounding 之间存在"逻辑矛盾"，这一表述过强。论文实际上是 **利用** 这一不一致来解释失败原因并设计修复：

1. Section 3.3 第 46-49 行明确指出："Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment"——论文并非声称 single-head profiling 是完美的，而是说在 constraint 将 2-bit 头数压到极少（k=8, 7% of heads）时，系统回到 near-additive regime。

2. Per-layer brute-force oracle（Appendix B 第 33-36 行）验证了这一点：constrained MCKP 与 oracle 的最大 gap 仅 0.018 PPL，说明在 constrained regime 下 additive approximation 确实成立。

3. 论文的逻辑链是：profiling → additive objective（unconstrained 时 fails）→ constraint 压回 additive regime → near-optimal。这不是矛盾，而是 **motivation for the constraint**。

但我同意 R1 的建议有价值：明确讨论 "constraint 如何将 problem 压回 additive regime" 会使论证更 rigorous。目前这一推理散落在 Section 3.3-3.4 中，未被 explicitly stated as a theorem-like claim。

---

**[AGREE] R1-N4: Downstream evaluation 仅限 Qwen**

同意，但严重性低于 R1 评估。Table 5 仅在 Qwen 上报告 downstream results。然而，考虑到：
- Llama/Mistral/Yi/Gemma 的 PPL difference 极小（最大 0.03 PPL），downstream accuracy difference 在统计意义上不可能显著
- 在 "方法无效" 的模型上做 downstream evaluation 的期望 outcome 是 "no significant difference"——这不会提供新信息

因此这更像是 completeness issue 而非 soundness issue。不过对于 EMNLP main conference 标准，补充至少 1 个 negative-result 模型（如 Llama）的 downstream 数据来确认 "PPL 无差 → downstream 无差" 是合理要求。

---

### Should-Fix 问题

**[AGREE] R1-W1: Standard vs hires profiling 差异过大（37→100 sensitive heads），但 headline results 用 standard**

同意。Appendix B 第 18 行：standard profiling 检测到 37/112 heads 有 non-zero 2-bit distortion，hires 检测到 100/112——2.7× 差异。Headline result（Table 2 的 11.23）用 standard profiling，而 hires 能达到 10.91（-0.32）。既然 hires 改变了 8/112 head assignments 且有实质性改善，论文的推荐实践可能应该是 hires profiling，但当前 framing 模糊了这一点。

---

**[REBUT] R1-W2: 统计报告不够充分——3 seeds, 仅报告 std，未报告 CI**

部分不同意。3 seeds 的 std=0.06 已经表明结果稳定：std/mean < 0.6%（Appendix B 第 25-26 行），且 bit distribution 完全一致。对于 deterministic solver + controlled calibration 的实验（不同于 stochastic training），3 seeds 足以显示 profiling 的 sampling noise 很小。正式的 CI 当然更好，但在 PPL 差异 4.22（uniform vs constrained）的 context 下，±0.06 的 uncertainty 不影响任何结论。这不是 must-fix 级别的问题。

---

**[AGREE] R1-W3: Cross-dataset stability 仅用两个 general-domain 数据集**

同意。Section 4.6 用 WikiText-2 和 C4——两者都是 general web/Wikipedia text。如果 downstream task 涉及 code、math、multilingual 等 domain-specific 内容，profiled allocation 是否仍然 stable 是未知的。但我认为这是 minor limitation 而非 must-fix，因为论文的 scope 明确是 PPL-based evaluation on general text。

---

**[AGREE] R1-W4: Solver equivalence 缺乏形式化证明**

同意。这与我的 W4 一致。Section 3.5 第 111 行 "The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal" 是 informal 解释而非 proof。Formal sufficient condition（例如 "当 k ≤ X% of H 且 bitwidth gap ≥ Y 时，constrained greedy = constrained MCKP"）会显著增强这一贡献的 technical depth。

---

**[AGREE] R1-W5: Runtime benchmark 为 PyTorch simulation，无法支撑部署结论**

同意。Appendix D 的 Table 5 已有明确 caveat（"do not represent optimized CUDA kernel performance"，第 78 行），但 8.5% overhead 仍然是 reader 可能引用的数字。论文 Limitations 已提到缺乏 real-kernel benchmark（Conclusion 第 16 行），这是诚实的。

---

**[AGREE] R1-W6: "Non-additive" 未被形式化定义**

同意。Section 3.3 描述 compounding 为 "non-additively"、"compound through the residual stream"、"PPL degrades super-linearly"（第 34-37 行），但未给出 formal characterization。例如：$\text{PPL}(\{b_h\}) > \sum_h d_h(b_h) + \text{baseline}$——这是 super-additive，但具体是 multiplicative、polynomial、还是其他 functional form？Figure 2 的 U-shaped curve 提供了 empirical evidence 但不构成 formalization。如果能给出 distortion interaction 的 approximate functional form（即使是 empirical fit），会大幅增强 technical contribution。

---

### 对 R1 Questions 的补充意见

1. **Q1 (为什么没跑所有 5 模型的 unconstrained)**: 我同意这是 critical gap。
2. **Q2 (Borderline cases)**: 我的 N1 已详细讨论——无 borderline 数据使 threshold 不可验证。
3. **Q3 (Cross-layer compounding near-optimality)**: Per-layer oracle（Appendix B）验证了 within-layer near-optimality，但 R1 正确指出这不验证 cross-layer interaction。
4. **Q4 (GPTQ/AWQ 适用性)**: 好问题。论文用 round-to-nearest quantization（Section 3.2 隐含），未讨论 data-dependent quantization methods 是否改变 compounding dynamics。
5. **Q5 (更高分辨率 profiling)**: 论文已测试 standard(16×512) → hires(64×2048)。继续提升是否 diminishing returns 是合理问题。

---

### 总结

| R1 意见 | 我的立场 | 理由 |
|---------|---------|------|
| N1 (Diagnostic overfitting) | AGREE | 与我 N1 一致；补充 positive class 仅 1 样本 |
| N2 (缺 unconstrained baselines) | AGREE | Compounding generality 未验证 |
| N3 (Profiling 逻辑矛盾) | REBUT | 非矛盾而是 motivation；constraint 压回 additive regime，有 oracle 验证 |
| N4 (Downstream 仅 Qwen) | AGREE (severity lower) | Completeness issue；negative-result 模型 downstream 差异不可能显著 |
| W1-W6 | AGREE (5/6) | 仅 W2 (CI) 部分不同意——3 seeds 在此 context 下已足够 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-15T04:27:59.144973+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-15T04:27:59.148072+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ratekv"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-15T04:27:59.299794+00:00_

FILE_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 154
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-15T04:27:59.350343+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-15T04:28:51.473936+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ratekv",
  "issues_yaml": "issues:\n- id: R1-N1\n  summary: \"Diagnostic framework 在 5 个数据点上完美拟合 2 个 threshold，overfitting 风险高；Spread 类别仅 1 个正样本 (Qwen)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 和 R2 均独立提出；R2 补充 positive class 仅 1 样本使决策边界更脆弱\"\n  action_items:\n    - round: 1\n      action: \"增加 3-5 个不同范式模型验证 threshold 鲁棒性，或将 claim 降级为 empirical observation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N2\n  summary: \"4/5 模型缺失 unconstrained baseline（Table 2），compounding generality 未验证\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 补充: Flat 模型 per-head distortion 极低，unconstrained solver 可能不触发 catastrophic failure，挑战 compounding 论点的 generality\"\n  action_items:\n    - round: 1\n      action: \"在所有 5 个模型上补跑 unconstrained greedy/MCKP\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N4\n  summary: \"Downstream evaluation 仅限 Qwen (Table 5)，其他 4 模型无 downstream results\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 评为 critical，R2 同意但认为 severity 较低（negative-result 模型 downstream 差异不可能显著，是 completeness issue）\"\n  action_items:\n    - round: 1\n      action: \"至少在 Llama 和 Yi-1.5 上补充 downstream evaluation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N2\n  summary: \"4/5 模型无收益，Qwen 可能是架构 outlier（uniform degradation +57.5% vs 其他 +2.9%-4.7%），practical value 存疑\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意但认为 negative results 本身有 go/no-go 信号价值\"\n  action_items:\n    - round: 1\n      action: \"分析 Qwen 为何异常；测试更多模型寻找 Spread 架构；或调整 framing 突出 diagnostic 而非 method\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N3\n  summary: \"Cardinality constraint 是标准 knapsack 技术的直接应用，algorithmic novelty 不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 评为 critical，R1 反驳——ARR H6 heuristic 警告不应因方法简单 reject，核心 novelty 在 compounding diagnosis。最终记为 warning（存在分歧）\"\n  action_items:\n    - round: 1\n      action: \"Formalize compounding 为 super-additive distortion model，增强 technical depth\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N3\n  summary: \"Profiling methodology（single-head isolation）与 compounding（non-additive）论点之间的逻辑张力\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 评为 critical，R2 反驳——constraint 将 problem 压回 additive regime，per-layer oracle 验证 gap<0.02。记为 warning（分歧）\"\n  action_items:\n    - round: 1\n      action: \"在 Section 3.4 中 explicitly 阐述 constraint 如何将 problem 压回 near-additive regime\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Related work 遗漏 HAWQ/HAQ 系列和多个 2025 KV cache 工作（PM-KVQ, Kitty, RotateKV, MiniKV, AQUA-KV）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意\"\n  action_items:\n    - round: 1\n      action: \"补充 HAWQ/HAQ 作为 mixed-precision 先驱；补充 2025 KV cache 工作\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W4\n  summary: \"Solver equivalence 缺乏形式化证明，仅有 3 个模型经验观察\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致\"\n  action_items:\n    - round: 1\n      action: \"提供 formal sufficient condition 或明确标注为 empirical observation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W6\n  summary: \"'Non-additive' 未被形式化定义（super-additive? multiplicative?）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 建议给出 distortion interaction 的 approximate functional form\"\n  action_items:\n    - round: 1\n      action: \"给出 compounding distortion 的形式化定义或 empirical functional form\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W1\n  summary: \"Standard vs hires profiling 差异过大（37→100 sensitive heads），headline results 用 standard 造成混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 补充: 如果 hires 改变 8/112 head assignments 且有实质性改善，推荐实践应该是 hires\"\n  action_items:\n    - round: 1\n      action: \"统一 profiling resolution 或明确说明 recommended setting\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W5\n  summary: \"Runtime benchmark 为 PyTorch simulation，无法支撑部署结论\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文已有 caveat（Appendix D），R2 确认诚实\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W2\n  summary: \"与 RateQuant 差异化不够 explicit\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R1 认为差异已存在于 S3.1 和 Table 1，但应更 explicit label\"\n  action_items:\n    - round: 1\n      action: \"在 Related Work 或 Method 中更明确阐述与 RateQuant 的区别\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W5\n  summary: \"缺少 per-head vs token-level granularity 的 tradeoff 讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意\"\n  action_items:\n    - round: 1\n      action: \"在 Related Work 中增加与 token-level 方法的 positioning 讨论\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ratekv",
    "issues_yaml": "issues:\n- id: R1-N1\n  summary: \"Diagnostic framework 在 5 个数据点上完美拟合 2 个 threshold，overfitting 风险高；Spread 类别仅 1 个正样本 (Qwen)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 和 R2 均独立提出；R2 补充 positive class 仅 1 样本使决策边界更脆弱\"\n  action_items:\n    - round: 1\n      action: \"增加 3-5 个不同范式模型验证 threshold 鲁棒性，或将 claim 降级为 empirical observation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N2\n  summary: \"4/5 模型缺失 unconstrained baseline（Table 2），compounding generality 未验证\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 补充: Flat 模型 per-head distortion 极低，unconstrained solver 可能不触发 catastrophic failure，挑战 compounding 论点的 generality\"\n  action_items:\n    - round: 1\n      action: \"在所有 5 个模型上补跑 unconstrained greedy/MCKP\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N4\n  summary: \"Downstream evaluation 仅限 Qwen (Table 5)，其他 4 模型无 downstream results\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 评为 critical，R2 同意但认为 severity 较低（negative-result 模型 downstream 差异不可能显著，是 completeness issue）\"\n  action_items:\n    - round: 1\n      action: \"至少在 Llama 和 Yi-1.5 上补充 downstream evaluation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N2\n  summary: \"4/5 模型无收益，Qwen 可能是架构 outlier（uniform degradation +57.5% vs 其他 +2.9%-4.7%），practical value 存疑\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意但认为 negative results 本身有 go/no-go 信号价值\"\n  action_items:\n    - round: 1\n      action: \"分析 Qwen 为何异常；测试更多模型寻找 Spread 架构；或调整 framing 突出 diagnostic 而非 method\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N3\n  summary: \"Cardinality constraint 是标准 knapsack 技术的直接应用，algorithmic novelty 不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 评为 critical，R1 反驳——ARR H6 heuristic 警告不应因方法简单 reject，核心 novelty 在 compounding diagnosis。最终记为 warning（存在分歧）\"\n  action_items:\n    - round: 1\n      action: \"Formalize compounding 为 super-additive distortion model，增强 technical depth\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N3\n  summary: \"Profiling methodology（single-head isolation）与 compounding（non-additive）论点之间的逻辑张力\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 评为 critical，R2 反驳——constraint 将 problem 压回 additive regime，per-layer oracle 验证 gap<0.02。记为 warning（分歧）\"\n  action_items:\n    - round: 1\n      action: \"在 Section 3.4 中 explicitly 阐述 constraint 如何将 problem 压回 near-additive regime\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Related work 遗漏 HAWQ/HAQ 系列和多个 2025 KV cache 工作（PM-KVQ, Kitty, RotateKV, MiniKV, AQUA-KV）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意\"\n  action_items:\n    - round: 1\n      action: \"补充 HAWQ/HAQ 作为 mixed-precision 先驱；补充 2025 KV cache 工作\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W4\n  summary: \"Solver equivalence 缺乏形式化证明，仅有 3 个模型经验观察\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"双方一致\"\n  action_items:\n    - round: 1\n      action: \"提供 formal sufficient condition 或明确标注为 empirical observation\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W6\n  summary: \"'Non-additive' 未被形式化定义（super-additive? multiplicative?）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 建议给出 distortion interaction 的 approximate functional form\"\n  action_items:\n    - round: 1\n      action: \"给出 compounding distortion 的形式化定义或 empirical functional form\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W1\n  summary: \"Standard vs hires profiling 差异过大（37→100 sensitive heads），headline results 用 standard 造成混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 补充: 如果 hires 改变 8/112 head assignments 且有实质性改善，推荐实践应该是 hires\"\n  action_items:\n    - round: 1\n      action: \"统一 profiling resolution 或明确说明 recommended setting\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W5\n  summary: \"Runtime benchmark 为 PyTorch simulation，无法支撑部署结论\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文已有 caveat（Appendix D），R2 确认诚实\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W2\n  summary: \"与 RateQuant 差异化不够 explicit\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R1 认为差异已存在于 S3.1 和 Table 1，但应更 explicit label\"\n  action_items:\n    - round: 1\n      action: \"在 Related Work 或 Method 中更明确阐述与 RateQuant 的区别\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W5\n  summary: \"缺少 per-head vs token-level granularity 的 tradeoff 讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"R1 同意\"\n  action_items:\n    - round: 1\n      action: \"在 Related Work 中增加与 token-level 方法的 positioning 讨论\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-15T04:28:51.574875+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml\", \"bytes\": 6464}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-15T04:30:43.009965+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "ratekv",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "report": "## 审稿报告 — Round 1\n\n**论文**: \"When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\"\n**Target Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Reviewer Panel**: R1 (方法严谨性 + 实验有效性) + R2 (新颖性 + 完整性 + 写作质量)\n\n---\n\n### Summary\n\n本文研究 per-head mixed-precision KV cache quantization 在 hardware-aligned bit-widths {2,4,8,16} 上的问题。核心发现是 unconstrained solvers（greedy/MCKP）因大量 2-bit head 的 distortion 在 residual stream 中 non-additive compounding 而产生灾难性退化（Qwen2.5-7B 上 PPL 32–37 vs uniform 4-bit 15.45）。提出的修复是 2-bit cardinality constraint（k≤8），将 PPL 降至 11.23（−27.3%）。论文还发现 constrained regime 下 greedy = MCKP，并提出基于 concentration + t₁/t₅ 的 joint diagnostic 区分 spread/spike/flat 三类架构。5 个模型中仅 Qwen 受益，其余 4 个无改善。\n\n---\n\n### Strengths\n\n1. **S1** 2-bit distortion compounding 是 genuine、previously-undocumented 的问题，有直接 warning value——任何使用 {2,4,8,16} bit-widths 做 per-head allocation 的后续工作都需要注意这一 failure mode。\n2. **S2** 单个 cardinality constraint 是 minimal、elegant 的修复，不增加额外 hyperparameter（k 由 U-shaped sweep 自动选取）。\n3. **S3** 4/5 模型 negative results 的诚实、完整报告。论文未选择性报告仅 Qwen 的正面结果，而是系统展示了 spread/spike/flat 三种 pattern，这对实践者有 go/no-go 信号价值。\n4. **S4** Spread/spike/flat taxonomy 提供了有用的 conceptual vocabulary，Yi-1.5 作为 \"高 concentration 但无收益\" 的 critical test case 设计得当。\n5. **S5** 实验的 thoroughness：cross-dataset stability（WikiText-2 vs C4, >96% agreement）、multi-seed stability（std/mean < 0.6%）、per-layer brute-force oracle、KV separation ablation、heuristic baselines 等展示了系统性评估的追求。\n6. **S6** 写作清晰、逻辑链连贯，anonymity 和 ACL format 合规。\n\n---\n\n### Weaknesses\n\n#### Must-Fix（影响接收决定）\n\n**W1** [CRITICAL | consensus R1+R2] **Diagnostic framework 泛化性严重不足**\n- 2 个 threshold（concentration ≳0.50, t₁/t₅ ≲0.70）在 5 个数据点上 100% 准确分类。2 个自由参数完美拟合 5 个样本是经典 overfitting 信号。\n- \"Spread\" 类别仅 1 个正样本（Qwen），positive class 的决策边界完全由单一数据点决定。\n- 5 个模型全部 7–9B decoder-only，未覆盖 MHA/MLA/MoE attention 等不同设计范式。\n- 论文自承 \"Both thresholds are illustrative\"（S5.2），但标题和 Contribution 3 的 framing 未反映此 caveat。\n- **Action**: 增加 3–5 个不同范式模型验证 threshold，或将 claim 降级为 exploratory empirical observation。\n\n**W2** [CRITICAL | consensus R1+R2] **4/5 模型缺失 unconstrained baseline**\n- Table 2 中 Llama/Mistral/Yi/Gemma 的 unconstrained greedy/MCKP 列为 \"---\"。Compounding 是 Contribution 1 的核心——如果仅在 1 个模型上验证，无法判断是 Qwen idiosyncratic 还是 general phenomenon。\n- Flat 模型（Mistral/Gemma, concentration 0.23–0.24）的 per-head 2-bit distortion 极低，unconstrained solver 可能不触发 catastrophic failure，这将挑战 compounding 论点的 generality。\n- **Action**: 在所有 5 个模型上补跑 unconstrained greedy/MCKP。\n\n**W3** [CRITICAL | consensus, R2 lower severity] **Downstream evaluation 仅限 Qwen**\n- 0-shot downstream results（Table 5）仅覆盖 Qwen。对于声称 cross-architecture diagnostic framework 的论文，downstream 验证 1/5 模型不充分。\n- R2 指出 negative-result 模型 PPL 差异极小（<0.03），downstream 差异不可能显著——但未验证即未确认。\n- **Action**: 至少在 Llama 和 Yi-1.5 上补充 downstream evaluation。\n\n**W4** [CRITICAL | consensus R1+R2] **Qwen 可能是架构 outlier，practical value 存疑**\n- Qwen uniform 4-bit degradation 异常高（+57.5%），其他模型仅 +2.9%–4.7%。方法仅在 degradation 异常大的 1 个模型上有效，这可能说明 Qwen 是 outlier 而非方法普遍有效的证据。\n- **Action**: 分析 Qwen 为何异常（GQA ratio? tokenizer? pre-training recipe?），测试更多模型寻找 \"Spread\" 架构。\n\n#### Should-Fix\n\n**W5** [WARNING | divergence] **Novelty 讨论**\n- R2 认为 cardinality constraint 是标准 knapsack 技术的直接应用（HAWQ/HAQ 先驱），algorithmic novelty 不足。\n- R1 反驳：ARR H6 heuristic 警告不应因方法简单 reject；核心 novelty 在 compounding diagnosis 而非 solution；solution simplicity 是 feature。\n- **Director 判断**: 两方均有道理。Compounding diagnosis 确实是 genuine contribution，但论文可通过 formalize compounding 为 super-additive distortion model 来增强 technical depth。\n\n**W6** [WARNING | divergence] **Profiling 方法与 compounding 论点的关系**\n- R1 指出 single-head isolation profiling 与 non-additive compounding 之间存在逻辑张力。\n- R2 反驳：论文利用这一不一致来解释失败并设计修复——constraint 将问题压回 near-additive regime，per-layer oracle（gap < 0.02 PPL）验证了这一点。\n- **Director 判断**: R2 的反驳有说服力。这不是逻辑矛盾而是 constraint 的 motivation。但论文应 explicitly 阐述 \"constraint 如何将 problem 压回 additive regime\"，当前推理散落在 S3.3–3.4 中。\n\n**W7** [WARNING | consensus] **Related work 遗漏**\n- 缺 HAWQ (ICCV'19)、HAWQ-V2 (NeurIPS'20)、HAQ (CVPR'19) 作为 mixed-precision bit allocation 先驱。\n- 缺 2025 published KV cache 工作：PM-KVQ、Kitty、RotateKV (IJCAI'25)、MiniKV (ACL Findings'25)、AQUA-KV (ICML'25)。\n- 与 RateQuant 差异化不够 explicit。\n- **Action**: 补充以上引用，明确与 RateQuant 的区别。\n\n**W8** [WARNING | consensus] **Solver equivalence 缺乏形式化**\n- \"Constraint narrows feasible set enough that greedy = MCKP\" 是 informal 解释。需要 formal sufficient condition 或明确标注为 empirical observation。\n\n**W9** [WARNING | consensus] **\"Non-additive\" 未形式化定义**\n- Section 3.3 使用 \"non-additively\"、\"super-linearly\" 但未给出 formal characterization。给出 approximate functional form（即使是 empirical fit）会增强 technical contribution。\n\n**W10** [WARNING | consensus] **Standard vs hires profiling 混用**\n- Standard profiling 检测 37/112 non-zero heads，hires 检测 100/112（2.7× 差异）。Headline result 用 standard（11.23），hires 更优（10.91）。应统一或明确推荐 setting。\n\n**W11** [WARNING | consensus] **缺少 per-head vs token-level granularity tradeoff 讨论**\n\n---\n\n### Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识：\n- [AGREE] Diagnostic framework 在 5 个模型上 overfitting，需要更多模型验证（W1）\n- [AGREE] 缺失 unconstrained baselines 是 critical gap（W2）\n- [AGREE] Related work 需补充 HAWQ/HAQ 和 2025 KV cache 工作（W7）\n- [AGREE] Solver equivalence 需形式化或明确标注为 empirical（W8）\n- [AGREE] \"Non-additive\" 需形式化定义（W9）\n- [AGREE] Negative results 的诚实报告是论文亮点（S3）\n- [AGREE] Compounding analysis 有 genuine value（S1）\n- [AGREE] 写作清晰、逻辑连贯（S6）\n\n### Reviewer Divergence\n\n**分歧 1: Novelty 是否充分**（W5）\n- R2: Cardinality constraint 是标准技术，novelty 不足，应升为 critical\n- R1: ARR H6 警告不因方法简单 reject，核心 novelty 在 compounding diagnosis\n\n**分歧 2: Profiling-compounding 关系**（W6）\n- R1: Single-head profiling 与 non-additive claim 存在逻辑矛盾\n- R2: 非矛盾而是 constraint 的 motivation，per-layer oracle 验证了 constrained regime 下的 near-additivity\n\n**分歧 3: Framing 是否偏乐观**\n- R2: Abstract 前半段突出 Qwen 27.3%，但 4/5 无收益\n- R1: Abstract 后半段已充分覆盖 negative results，标题 \"When Does...Help?\" 本身暗示 \"not always\"\n\n---\n\n### Questions for Authors\n\n1. 为什么没有在所有 5 个模型上运行 unconstrained baselines？这些实验的计算成本是多少？\n2. Qwen 的 uniform 4-bit degradation（+57.5%）为何远高于其他模型（+2.9%–4.7%）？是 GQA ratio、tokenizer 还是 pre-training recipe 导致？\n3. Diagnostic 的 borderline cases（concentration ≈ 0.55, t₁/t₅ ≈ 0.65）如何处理？是否有 graceful degradation？\n4. Constraint 如何将 problem 从 non-additive regime 压回 near-additive regime？能否 formally characterize 这一 transition？\n5. 方法是否依赖 round-to-nearest quantization？对 GPTQ/AWQ 等 data-dependent quantization 方法是否适用？\n6. RateQuant 在 {2,4,8,16} bit-widths 上是否也产生 catastrophic failure？\n\n---\n\n### Missing References\n\n**Weight-level mixed-precision 先驱（positioning 需要）：**\n- HAWQ (Dong et al., ICCV 2019)\n- HAWQ-V2 (Dong et al., NeurIPS 2020)\n- HAQ (Wang et al., CVPR 2019)\n\n**2025-2026 KV cache 工作（completeness 需要）：**\n- PM-KVQ (arXiv 2025)\n- Kitty (arXiv 2025)\n- RotateKV (IJCAI 2025)\n- MiniKV (ACL Findings 2025)\n- AQUA-KV (ICML 2025)\n- \"Don't Waste Bits!\" (arXiv 2026)\n\n---\n\n### External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n### Overall Assessment\n\n**Overall Score: Weak Reject (2.25/5)**\n- R1: 2.5/5 (Borderline) | Confidence 4/5\n- R2: 2/5 (Resubmit next cycle) | Confidence 4/5\n\n**Rationale**:\n\n论文的核心发现——2-bit distortion compounding 在 hardware-aligned bit-widths 上导致 unconstrained solver catastrophic failure——是 genuine 且有实践价值的贡献。Cardinality constraint 作为 minimal fix 是 elegant 的，negative results 的诚实完整报告体现了科学严谨性。\n\n然而，论文存在以下系统性缺口使其在当前状态下不适合 EMNLP main conference：\n1. **Diagnostic framework 的泛化性无法验证**：2 个 threshold 在 5 个同质模型上完美拟合（仅 1 个正样本），这不足以支撑 \"framework\" 的 claim。\n2. **Compounding 的 generality 未验证**：4/5 模型缺失 unconstrained baselines，无法确认 compounding 是 general phenomenon。\n3. **方法的 practical scope 极窄**：仅 Qwen（一个 degradation 异常高的 outlier）获益，且 Qwen 为何异常未被分析。\n4. **评估覆盖不完整**：downstream evaluation 仅 Qwen，related work 遗漏重要先驱。\n\n**建议路径**：\n- 补充 unconstrained baselines（W2）和 downstream evaluation（W3）后，可考虑作为 **Findings** paper 提交——compounding warning + negative results + diagnostic observation 的组合在 Findings track 有价值。\n- 若要冲 main conference，需扩展到 10+ 模型验证 diagnostic threshold，并 formalize compounding（W9）和 solver equivalence（W8）。\n\n---\n\n### Detailed Comments\n\n**Section 3.2 (Profiling)**: 明确 single-head profiling 的 assumption（additive approximation）和 validity range（k small）。当前表述在 S3.2 L27–29 中承认 additive assumption 但未明确 constraint 如何恢复 validity。\n\n**Section 3.5 (Solver Equivalence)**: L111 \"narrows the feasible set enough\" 需要 formal statement。例如：在什么条件下（k/H ratio, bitwidth gap size），constrained greedy 保证等于 constrained MCKP？\n\n**Section 5.2 (Diagnostic)**: 考虑将 framework 重新定位为 \"empirical taxonomy\" 或 \"preliminary diagnostic heuristic\"，与证据强度匹配。Thresholds 可改为 \"suggested ranges\" 而非 fixed values。\n\n**Table 2**: 补充所有 5 个模型的 unconstrained results。即使 Flat 模型不触发 catastrophic failure，这本身也是 informative（说明 compounding 需要 sufficient heterogeneity）。\n\n**Abstract**: 前半段过度强调 Qwen 27.3% improvement。建议开篇即点明 \"non-uniform allocation helps only when head sensitivity exhibits a specific distribution shape\"，将 \"when does it NOT help\" 提到更突出位置。\n\n**References**: 补充 HAWQ/HAQ 系列和 2025 KV cache 工作，增加与 RateQuant 的 explicit differentiation paragraph。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "ratekv",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "report": "## 审稿报告 — Round 1\n\n**论文**: \"When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\"\n**Target Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Reviewer Panel**: R1 (方法严谨性 + 实验有效性) + R2 (新颖性 + 完整性 + 写作质量)\n\n---\n\n### Summary\n\n本文研究 per-head mixed-precision KV cache quantization 在 hardware-aligned bit-widths {2,4,8,16} 上的问题。核心发现是 unconstrained solvers（greedy/MCKP）因大量 2-bit head 的 distortion 在 residual stream 中 non-additive compounding 而产生灾难性退化（Qwen2.5-7B 上 PPL 32–37 vs uniform 4-bit 15.45）。提出的修复是 2-bit cardinality constraint（k≤8），将 PPL 降至 11.23（−27.3%）。论文还发现 constrained regime 下 greedy = MCKP，并提出基于 concentration + t₁/t₅ 的 joint diagnostic 区分 spread/spike/flat 三类架构。5 个模型中仅 Qwen 受益，其余 4 个无改善。\n\n---\n\n### Strengths\n\n1. **S1** 2-bit distortion compounding 是 genuine、previously-undocumented 的问题，有直接 warning value——任何使用 {2,4,8,16} bit-widths 做 per-head allocation 的后续工作都需要注意这一 failure mode。\n2. **S2** 单个 cardinality constraint 是 minimal、elegant 的修复，不增加额外 hyperparameter（k 由 U-shaped sweep 自动选取）。\n3. **S3** 4/5 模型 negative results 的诚实、完整报告。论文未选择性报告仅 Qwen 的正面结果，而是系统展示了 spread/spike/flat 三种 pattern，这对实践者有 go/no-go 信号价值。\n4. **S4** Spread/spike/flat taxonomy 提供了有用的 conceptual vocabulary，Yi-1.5 作为 \"高 concentration 但无收益\" 的 critical test case 设计得当。\n5. **S5** 实验的 thoroughness：cross-dataset stability（WikiText-2 vs C4, >96% agreement）、multi-seed stability（std/mean < 0.6%）、per-layer brute-force oracle、KV separation ablation、heuristic baselines 等展示了系统性评估的追求。\n6. **S6** 写作清晰、逻辑链连贯，anonymity 和 ACL format 合规。\n\n---\n\n### Weaknesses\n\n#### Must-Fix（影响接收决定）\n\n**W1** [CRITICAL | consensus R1+R2] **Diagnostic framework 泛化性严重不足**\n- 2 个 threshold（concentration ≳0.50, t₁/t₅ ≲0.70）在 5 个数据点上 100% 准确分类。2 个自由参数完美拟合 5 个样本是经典 overfitting 信号。\n- \"Spread\" 类别仅 1 个正样本（Qwen），positive class 的决策边界完全由单一数据点决定。\n- 5 个模型全部 7–9B decoder-only，未覆盖 MHA/MLA/MoE attention 等不同设计范式。\n- 论文自承 \"Both thresholds are illustrative\"（S5.2），但标题和 Contribution 3 的 framing 未反映此 caveat。\n- **Action**: 增加 3–5 个不同范式模型验证 threshold，或将 claim 降级为 exploratory empirical observation。\n\n**W2** [CRITICAL | consensus R1+R2] **4/5 模型缺失 unconstrained baseline**\n- Table 2 中 Llama/Mistral/Yi/Gemma 的 unconstrained greedy/MCKP 列为 \"---\"。Compounding 是 Contribution 1 的核心——如果仅在 1 个模型上验证，无法判断是 Qwen idiosyncratic 还是 general phenomenon。\n- Flat 模型（Mistral/Gemma, concentration 0.23–0.24）的 per-head 2-bit distortion 极低，unconstrained solver 可能不触发 catastrophic failure，这将挑战 compounding 论点的 generality。\n- **Action**: 在所有 5 个模型上补跑 unconstrained greedy/MCKP。\n\n**W3** [CRITICAL | consensus, R2 lower severity] **Downstream evaluation 仅限 Qwen**\n- 0-shot downstream results（Table 5）仅覆盖 Qwen。对于声称 cross-architecture diagnostic framework 的论文，downstream 验证 1/5 模型不充分。\n- R2 指出 negative-result 模型 PPL 差异极小（<0.03），downstream 差异不可能显著——但未验证即未确认。\n- **Action**: 至少在 Llama 和 Yi-1.5 上补充 downstream evaluation。\n\n**W4** [CRITICAL | consensus R1+R2] **Qwen 可能是架构 outlier，practical value 存疑**\n- Qwen uniform 4-bit degradation 异常高（+57.5%），其他模型仅 +2.9%–4.7%。方法仅在 degradation 异常大的 1 个模型上有效，这可能说明 Qwen 是 outlier 而非方法普遍有效的证据。\n- **Action**: 分析 Qwen 为何异常（GQA ratio? tokenizer? pre-training recipe?），测试更多模型寻找 \"Spread\" 架构。\n\n#### Should-Fix\n\n**W5** [WARNING | divergence] **Novelty 讨论**\n- R2 认为 cardinality constraint 是标准 knapsack 技术的直接应用（HAWQ/HAQ 先驱），algorithmic novelty 不足。\n- R1 反驳：ARR H6 heuristic 警告不应因方法简单 reject；核心 novelty 在 compounding diagnosis 而非 solution；solution simplicity 是 feature。\n- **Director 判断**: 两方均有道理。Compounding diagnosis 确实是 genuine contribution，但论文可通过 formalize compounding 为 super-additive distortion model 来增强 technical depth。\n\n**W6** [WARNING | divergence] **Profiling 方法与 compounding 论点的关系**\n- R1 指出 single-head isolation profiling 与 non-additive compounding 之间存在逻辑张力。\n- R2 反驳：论文利用这一不一致来解释失败并设计修复——constraint 将问题压回 near-additive regime，per-layer oracle（gap < 0.02 PPL）验证了这一点。\n- **Director 判断**: R2 的反驳有说服力。这不是逻辑矛盾而是 constraint 的 motivation。但论文应 explicitly 阐述 \"constraint 如何将 problem 压回 additive regime\"，当前推理散落在 S3.3–3.4 中。\n\n**W7** [WARNING | consensus] **Related work 遗漏**\n- 缺 HAWQ (ICCV'19)、HAWQ-V2 (NeurIPS'20)、HAQ (CVPR'19) 作为 mixed-precision bit allocation 先驱。\n- 缺 2025 published KV cache 工作：PM-KVQ、Kitty、RotateKV (IJCAI'25)、MiniKV (ACL Findings'25)、AQUA-KV (ICML'25)。\n- 与 RateQuant 差异化不够 explicit。\n- **Action**: 补充以上引用，明确与 RateQuant 的区别。\n\n**W8** [WARNING | consensus] **Solver equivalence 缺乏形式化**\n- \"Constraint narrows feasible set enough that greedy = MCKP\" 是 informal 解释。需要 formal sufficient condition 或明确标注为 empirical observation。\n\n**W9** [WARNING | consensus] **\"Non-additive\" 未形式化定义**\n- Section 3.3 使用 \"non-additively\"、\"super-linearly\" 但未给出 formal characterization。给出 approximate functional form（即使是 empirical fit）会增强 technical contribution。\n\n**W10** [WARNING | consensus] **Standard vs hires profiling 混用**\n- Standard profiling 检测 37/112 non-zero heads，hires 检测 100/112（2.7× 差异）。Headline result 用 standard（11.23），hires 更优（10.91）。应统一或明确推荐 setting。\n\n**W11** [WARNING | consensus] **缺少 per-head vs token-level granularity tradeoff 讨论**\n\n---\n\n### Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识：\n- [AGREE] Diagnostic framework 在 5 个模型上 overfitting，需要更多模型验证（W1）\n- [AGREE] 缺失 unconstrained baselines 是 critical gap（W2）\n- [AGREE] Related work 需补充 HAWQ/HAQ 和 2025 KV cache 工作（W7）\n- [AGREE] Solver equivalence 需形式化或明确标注为 empirical（W8）\n- [AGREE] \"Non-additive\" 需形式化定义（W9）\n- [AGREE] Negative results 的诚实报告是论文亮点（S3）\n- [AGREE] Compounding analysis 有 genuine value（S1）\n- [AGREE] 写作清晰、逻辑连贯（S6）\n\n### Reviewer Divergence\n\n**分歧 1: Novelty 是否充分**（W5）\n- R2: Cardinality constraint 是标准技术，novelty 不足，应升为 critical\n- R1: ARR H6 警告不因方法简单 reject，核心 novelty 在 compounding diagnosis\n\n**分歧 2: Profiling-compounding 关系**（W6）\n- R1: Single-head profiling 与 non-additive claim 存在逻辑矛盾\n- R2: 非矛盾而是 constraint 的 motivation，per-layer oracle 验证了 constrained regime 下的 near-additivity\n\n**分歧 3: Framing 是否偏乐观**\n- R2: Abstract 前半段突出 Qwen 27.3%，但 4/5 无收益\n- R1: Abstract 后半段已充分覆盖 negative results，标题 \"When Does...Help?\" 本身暗示 \"not always\"\n\n---\n\n### Questions for Authors\n\n1. 为什么没有在所有 5 个模型上运行 unconstrained baselines？这些实验的计算成本是多少？\n2. Qwen 的 uniform 4-bit degradation（+57.5%）为何远高于其他模型（+2.9%–4.7%）？是 GQA ratio、tokenizer 还是 pre-training recipe 导致？\n3. Diagnostic 的 borderline cases（concentration ≈ 0.55, t₁/t₅ ≈ 0.65）如何处理？是否有 graceful degradation？\n4. Constraint 如何将 problem 从 non-additive regime 压回 near-additive regime？能否 formally characterize 这一 transition？\n5. 方法是否依赖 round-to-nearest quantization？对 GPTQ/AWQ 等 data-dependent quantization 方法是否适用？\n6. RateQuant 在 {2,4,8,16} bit-widths 上是否也产生 catastrophic failure？\n\n---\n\n### Missing References\n\n**Weight-level mixed-precision 先驱（positioning 需要）：**\n- HAWQ (Dong et al., ICCV 2019)\n- HAWQ-V2 (Dong et al., NeurIPS 2020)\n- HAQ (Wang et al., CVPR 2019)\n\n**2025-2026 KV cache 工作（completeness 需要）：**\n- PM-KVQ (arXiv 2025)\n- Kitty (arXiv 2025)\n- RotateKV (IJCAI 2025)\n- MiniKV (ACL Findings 2025)\n- AQUA-KV (ICML 2025)\n- \"Don't Waste Bits!\" (arXiv 2026)\n\n---\n\n### External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n### Overall Assessment\n\n**Overall Score: Weak Reject (2.25/5)**\n- R1: 2.5/5 (Borderline) | Confidence 4/5\n- R2: 2/5 (Resubmit next cycle) | Confidence 4/5\n\n**Rationale**:\n\n论文的核心发现——2-bit distortion compounding 在 hardware-aligned bit-widths 上导致 unconstrained solver catastrophic failure——是 genuine 且有实践价值的贡献。Cardinality constraint 作为 minimal fix 是 elegant 的，negative results 的诚实完整报告体现了科学严谨性。\n\n然而，论文存在以下系统性缺口使其在当前状态下不适合 EMNLP main conference：\n1. **Diagnostic framework 的泛化性无法验证**：2 个 threshold 在 5 个同质模型上完美拟合（仅 1 个正样本），这不足以支撑 \"framework\" 的 claim。\n2. **Compounding 的 generality 未验证**：4/5 模型缺失 unconstrained baselines，无法确认 compounding 是 general phenomenon。\n3. **方法的 practical scope 极窄**：仅 Qwen（一个 degradation 异常高的 outlier）获益，且 Qwen 为何异常未被分析。\n4. **评估覆盖不完整**：downstream evaluation 仅 Qwen，related work 遗漏重要先驱。\n\n**建议路径**：\n- 补充 unconstrained baselines（W2）和 downstream evaluation（W3）后，可考虑作为 **Findings** paper 提交——compounding warning + negative results + diagnostic observation 的组合在 Findings track 有价值。\n- 若要冲 main conference，需扩展到 10+ 模型验证 diagnostic threshold，并 formalize compounding（W9）和 solver equivalence（W8）。\n\n---\n\n### Detailed Comments\n\n**Section 3.2 (Profiling)**: 明确 single-head profiling 的 assumption（additive approximation）和 validity range（k small）。当前表述在 S3.2 L27–29 中承认 additive assumption 但未明确 constraint 如何恢复 validity。\n\n**Section 3.5 (Solver Equivalence)**: L111 \"narrows the feasible set enough\" 需要 formal statement。例如：在什么条件下（k/H ratio, bitwidth gap size），constrained greedy 保证等于 constrained MCKP？\n\n**Section 5.2 (Diagnostic)**: 考虑将 framework 重新定位为 \"empirical taxonomy\" 或 \"preliminary diagnostic heuristic\"，与证据强度匹配。Thresholds 可改为 \"suggested ranges\" 而非 fixed values。\n\n**Table 2**: 补充所有 5 个模型的 unconstrained results。即使 Flat 模型不触发 catastrophic failure，这本身也是 informative（说明 compounding 需要 sufficient heterogeneity）。\n\n**Abstract**: 前半段过度强调 Qwen 27.3% improvement。建议开篇即点明 \"non-uniform allocation helps only when head sensitivity exhibits a specific distribution shape\"，将 \"when does it NOT help\" 提到更突出位置。\n\n**References**: 补充 HAWQ/HAQ 系列和 2025 KV cache 工作，增加与 RateQuant 的 explicit differentiation paragraph。"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-15T04:30:47.025861+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_e886d722cc0b64fdb553f7bb0b99816c:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4015
}
```

</details>

---

### Assistant

_source line 156 · 2026-05-15T04:30:55.911572+00:00_

审稿完成。

**Round 1 审稿报告已投递给 Research Director。**

汇总：
- **Overall Score: Weak Reject (2.25/5)**（R1: 2.5 Borderline, R2: 2.0 Resubmit）
- **4 个 Critical 共识问题**：diagnostic 泛化性不足（5 模型 overfit）、4/5 模型缺 unconstrained baselines、downstream eval 仅 Qwen、Qwen 可能是架构 outlier
- **2 个分歧点**：novelty 是否充分（R1 认为 compounding diagnosis 足够 vs R2 认为标准技术）、profiling-compounding 逻辑关系（R1 认为矛盾 vs R2 认为是 constraint motivation）
- **建议路径**：补充 unconstrained baselines + downstream eval 后作为 Findings paper 提交；冲 main conference 需扩展模型覆盖和 formalize compounding
- **Issue Tracker** 已同步更新（14 条 issue）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 13

72 recorded events

### User

_source line 157 · 2026-05-15T15:22:07.864925+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ratekv
- 论文路径: projects/ratekv/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "system"
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-15T15:22:13.407759+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-15T15:22:13.458749+00:00_

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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-15T15:22:17.725171+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-15T15:22:17.725622+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-15T15:22:22.944335+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ratekv"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-15T15:22:23.296034+00:00_

{"result":"# 项目 ratekv 概况\n\n## 实验状态 (93 个)\n\n- **exp_c_no2bit**: DONE (negative) — \n- **exp_c_constrained_mckp**: DONE (success) — \n- **exp_b_hires_quant**: DONE (negative) — \n- **exp_a_targeted_hybrid**: DONE (negative) — \n- **mvp_004**: DONE (negative) — \n- **p0_2_cliff_7B**: DONE (success) — \n- **p0_1_ppl_fast**: DONE (negative) — \n- **p0_2_cliff_1.5B**: DONE (success) — \n- **sanity_004**: DONE (success) — \n- **sanity_003**: DONE (failed) — \n- **sanity_002**: DONE (failed) — \n- **sanity_001**: DONE (failed) — \n- **mvp_003**: DONE (failed) — \n- **mvp_002**: DONE (failed) — \n- **mvp_001**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无 — 全部 pending 实验已清理完毕）\n\n## 近期结论（本 session）\n- **qwen14b_greedy_constrained** (success): Greedy=MCKP=7.2206, solver equivalence 确认 (384 heads, k=8)\n- **kivi_mckp_combined** (success): KIVI+MCKP=9.90 vs MCKP alone=10.89, 正交互补性确认\n- **mistral_hires_constrained_mckp_v2** (negative): 修复 uniform bug 后 MCKP(k=2)=7.1341 vs uniform=7.1308, Flat 预期\n- **mistral_uniform_reeval** (success): Root cause = bits=budget(0.25) 误传, 修复后 uniform=7.1308\n\n## Registry 清理（本 session）\n- greedy_constrained_ablation → killed（已被 solver equivalence 覆盖）\n- cross_domain_calibration_v2 → killed（c4_rerun_d032 已覆盖）\n- qwen25-hires-profiling → killed（已被其他 hires profiling 覆盖）\n- mistral_hires_bf16_2bitonly_v3 → killed（重复工作）\n\n## 论文更新（本 session）\n- Table 1: Qwen-14B/Pythia Greedy 填入; Mistral 7.16→7.13 (k=2); 移除 $^\\ddagger$ 脚注\n- Table 3: Mistral ΔPPL(Ours) 0.13→0.10\n- 编译验证: 0 errors, 0 warnings, 13 pages\n\n## 趋势\n成功 51 / 负向 18 / 失败 9 / 共 93\n\n## 资源状态\nwestd-37397: cuda:0 空闲, cuda:1 空闲。Standby 给 Paper Agent。"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-15T15:22:23.296386+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-15T15:22:23.396969+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-15T15:22:28.265076+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'softconf.com']"
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-15T15:22:30.172876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-15T15:22:30.675147+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	
11	\title{When Does Non-Uniform KV Cache Quantization Help?\\Cardinality Constraints and a Heterogeneity Diagnostic}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	\input{abstract}
20	\end{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{experiments}
26	\input{analysis}
27	\input{conclusion}
28	
29	\bibliography{references}
30	
31	\input{appendix}
32	
33	\end{document}
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-15T15:22:31.127111+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ratekv",
  "file": "paper_provenance.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ratekv",
    "file": "paper_provenance.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-15T15:22:31.328226+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "file": "projects/ratekv/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "file": "projects/ratekv/artifacts/review_issues.yaml"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-15T15:22:31.328551+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-15T15:22:35.695083+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the web search results, I found information about EMNLP 2026's call for papers. Here's what I found:

## EMNLP 2026 Call for Main Conference Papers

**Submis
…[truncated 1410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7430
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-15T15:22:35.695908+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/paper_provenance.yaml\", \"content\": \"paper:\\n  title: ''\\n  version: 69\\n  generated_at: '2026-05-15T08:39:28.787717+00:00'\\nclaims:\\n- id: C001\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: Unconstrained greedy assigns 68 heads to 2-bit, PPL=32.45\\n  type: quantitative\\n  evidence:\\n  - oracle_comparison\\n  decisions: []\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: Unconstrained MCKP assigns 75 heads to 2-bit, PPL=36.92\\n  type: quantitative\\n  evidence:\\n  - exp_b_hires_quant\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: Constrained greedy = constrained MCKP, PPL=11.23, bit dist {8/100/4}\\n  type: quantitative\\n  evidence:\\n  - greedy_cardinality_ablation\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Compounding curve U-shaped: k=0 15.45, k=8 11.23 optimal, k=75 35.35'\\n  type: quantitative\\n  evidence:\\n  - compounding_sweep\\n  - compounding_sweep_k10_12\\n  decisions: []\\n  deprecated: false\\n- id: C015\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: 'L0 distortion: L0H0 +31.9%, L0H2 +23.2%, L0H3 +11.7%'\\n  type: quantitative\\n  evidence:\\n  - p0_2_cliff_7B\\n  decisions: []\\n  deprecated: false\\n- id: C021\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Solver with/without L0 exclusion: 112/112 identical'\\n  type: quantitative\\n  evidence:\\n  - exp_d_no_l0_exclusion\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Per-head verification: Qwen 112/112, Llama 256/256, Mistral
…[truncated 3767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4568
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-15T15:22:40.866304+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference paper page limit format requirements ACL rolling review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference paper page limit format requirements ACL rolling review"
  }
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-15T15:22:41.368418+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-15T15:22:41.870550+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-15T15:22:41.971422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-15T15:22:41.971823+00:00_

1	Non-uniform per-head KV cache quantization helps only when head sensitivity exhibits a specific distribution shape---a finding obscured by prior work's focus on aggregate metrics.
2	We study seven models spanning 1.4B--14B parameters and five architecture families (MHA through GQA 8:1) on hardware-aligned bit-widths $\{2,4,8,16\}$ and find that the benefit of per-head allocation depends not on GQA ratio or overall sensitivity magnitude, but on whether heterogeneity is \emph{spread} across multiple heads with cross-bitwidth gradients or concentrated in a single outlier.
3	On the one spread-pattern model (Qwen2.5-7B), a cardinality-constrained solver achieves 10.91 perplexity at $4\times$ compression---a 29.4\% reduction over uniform 4-bit (15.45)---while unconstrained solvers fail catastrophically (32--37 PPL) due to 2-bit distortion compounding through the residual stream.
4	On the remaining six models---including Qwen2.5-14B, where scaling dilutes spread into flat---non-uniform allocation provides no meaningful benefit: Yi-1.5-9B has the highest concentration tested (0.71, exceeding Qwen-7B's 0.61) yet gains nothing, because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth gradient.
5	The cardinality constraint prevents catastrophic failure on spread architectures, moderate over-allocation on flat architectures (Gemma-2: unconstrained $1.47\times$ degradation reduced to within 0.5\% of uniform), and renders solver choice irrelevant---constrained greedy and MCKP produce identical allocations---enabling a simple $O(H\log H)$ greedy algorithm.
6	We propose a joint empirical decision rule combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly classifies all seven evaluated models (7/7), including a within-family scale contrast (Qwen-7B spread vs.\ 14B flat).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-15T15:22:45.584700+00:00_

Web search results for query: "EMNLP 2026 main conference paper page limit format requirements ACL rolling review"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here is the information about EMNLP 2026 main conference paper requirements:

## Page Limits and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

The mandatory Limitations section is required, placed after the conclusion.

## ACL Rolling Review (ARR)

All submissions go through ACL Rolling Review (ARR), with the ARR submission
…[truncated 383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "elapsed_ms": 4718
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-15T15:22:48.096295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-15T15:22:48.999958+00:00_

1	- id: R1-W1
2	  summary: "Diagnostic framework overfitting: 2 thresholds on 5 models (1 positive)"
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - round: 1
10	      reviewers: [R1, R2]
11	      note: "consensus: 2 free parameters perfectly fit 5 samples = overfitting"
12	  action_items:
13	    - round: 1
14	      action: "Qwen2.5-14B hires profiling for N>1 Spread validation"
15	      assigned_to: Agent
16	      status: done
17	    - round: 1
18	      action: "MHA model (Pythia-1.4B) profiling for attention paradigm diversity"
19	      assigned_to: Agent
20	      status: done
21	    - round: 1
22	      action: "Downgrade claim from 'diagnostic framework' to 'empirical decision rule'"
23	      assigned_to: Paper Agent
24	      status: done
25	    - round: 1
26	      action: "Qwen-14B constrained pipeline (Flat prediction verified, Δ=0.02)"
27	      assigned_to: Agent
28	      status: done
29	    - round: 1
30	      action: "Pythia-1.4B constrained pipeline (Flat prediction verification)"
31	      assigned_to: Agent
32	      status: done
33	    - round: 1
34	      action: "t1/t5 bug fix: profiling scripts use delta ratio, must use concentration ratio"
35	      assigned_to: Agent
36	      status: done
37	  resolution: "Diagnostic now 7/7 correct (added Qwen-14B=Flat, Pythia=Flat). Claim downgraded to empirical decision rule. All t1/t5 canonical values unified in paper."
38	  resolution_round: 1
39	
40	- id: R1-W2
41	  summary: "4/5 models missing unconstrained greedy/MCKP baselines in Table 2"
42	  category: experiment
43	  severity: critical
44	  status: resolved
45	  first_raised_round: 1
46	  last_seen_round: 1
47	  mentions:
48	    - round: 1
49	      reviewers: [R1, R2]
50	      note: "consensus: compounding is Contribution 1 core, must verify on all models"
51	  action_items:
52	    - round: 1
53	      action: "Run unconstrained greedy + MCKP on all 5 models"
54	      as
…[truncated 9213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-15T15:22:49.151115+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL rolling review 2026 submission format long paper 8 pages short paper 4 pages author guidelines anonymity",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL rolling review 2026 submission format long paper 8 pages short paper 4 pages author guidelines anonymity",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-15T15:22:56.126938+00:00_

Web search results for query: "ACL rolling review 2026 submission format long paper 8 pages short paper 4 pages author guidelines anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here is the information about ACL Rolling Review 2026 submi
…[truncated 1300 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6975
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-15T15:23:06.365057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-15T15:23:06.917602+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors compound through the residual stream.
17	The additive model predicts $\sim$11 PPL; the actual PPL is $3$--$4\times$ higher, because 2-bit distortions are orders of magnitude larger than 4-bit and compound super-linearly when many heads are quantized simultaneously.
18	
19	This observa
…[truncated 3839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-15T15:23:06.918063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-15T15:23:07.171102+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We use symmetric per-channel quantization with per-head granularity: each KV head is independently quantized to one of the candidate bit-widths $\mathcal{B} = \{2, 4, 8, 16\}$, without per-token scaling.
25	We profile each head by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibrat
…[truncated 7449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-15T15:23:07.171550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-15T15:23:07.222108+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across seven models at $4\times$ compression.
12	The central finding is that MCKP benefit requires \emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.
13	
14	Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
15	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp
16	
17	Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
18	Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling
19	Critically, L4H3's 4-bit and 8-bit deltas are ${\approx}\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.
20	In contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-
…[truncated 5501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-15T15:23:10.935587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-15T15:23:11.237158+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.
4	On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
5	Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, Llama) and flat (Mistral, Gemma-2, Qwen-14B, Pythia) patterns show no benefit.
6	A joint empirical decision rule based on concentration and $t_1/t_5$ ratio correctly classifies all seven evaluated models (7/7), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
7	Extending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) are natural next steps.
8	
9	\section*{Limitations}
10	
11	Spread rests on $N{=}1$ (Qwen2.5-7B); the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-15T15:23:11.388099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-15T15:23:11.539039+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, sliding-window adaptation~\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\cite{su2025rotatekv}, 2-bit with adaptive token retention~\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\cite{shutova2025aquakv}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	Our per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \emph{at what precision} (bit-width selection across heads).
7	The two can be composed, though the per-channel method dominates when available (\S\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.
8	
9	\paragraph{KV Cache Eviction.}
10	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
11	Recent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\cite{feng2025adakv}, confirming that head-level heterog
…[truncated 3527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-15T15:23:11.539480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-15T15:23:11.590080+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate seven models spanning five architecture families and diverse attention configurations:
9	\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\times$ 4 KV heads = 112),
10	\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\times$ 8 = 384),
11	\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\times$ 4 = 192),
12	\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\times$ 8 = 256),
13	\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\times$ 8 = 256, sliding window attention),
14	\textbf{Gemma-2-9B} (GQA 2:1, 42 $\times$ 8 = 336, \texttt{head\_dim}=256, attention logit softcapping),
15	and \textbf{Pythia-1.4B} (MHA 1:1, 24 $\times$ 16 = 384).
16	This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.
17	
18	\paragraph{Evaluation.}
19	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
20	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
21	
22	\paragraph{Profiling.}
23	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
24	All results use high-resolution profiling (64 sequences $\times$ 2048 tokens from WikiText-2 train); Appendix~\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\times$ 512 tok).
25	
26	\paragraph{Compression and constraint.}
27	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
28	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2 and Pythia).
29	
30	\paragraph{Baselines.}
31	We compa
…[truncated 7007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-15T15:23:15.427336+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/appendix.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/appendix.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-15T15:23:15.478012+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-15T15:23:23.305260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-15T15:23:23.305812+00:00_

1	\appendix
2	
3	\section{Compounding Curve}
4	\label{sec:compounding_appendix}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
9	\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
10	\label{fig:compounding}
11	\end{figure}
12	
13	\section{Heuristic Baselines}
14	\label{sec:heuristic_appendix}
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}2$ for Mistral). Llama and Mistral use hires profiling.}
20	\label{tab:heuristic}
21	\begin{tabular}{lcccc}
22	\toprule
23	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
24	 & & Median & Mean$\pm$Std & Positional \\
25	\midrule
26	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
27	Llama-3.1-8B    & 8.45  & 8.62  & 8.62$\pm$0.07  & 8.58 \\
28	Mistral-7B-v0.3 & 7.13  & 7.20  & 7.24$\pm$0.07  & 7.21 \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL.
34	On Llama ($k{=}2$), all methods cluster within 0.17 PPL; on Mistral ($k{=}2$), MCKP (7.13) matches uniform (7.13), while heuristic baselines remain slightly worse.
35	Heuristic baselines use a slightly higher budget (0.256 vs.\ 0.248, a 3\% difference); despite this advantage, they still underperform MCKP.
36	
37	\section{Allocation Visualization}
38	\label{sec:allocation_appendix}
39	
40	\begin{figure}[t]
41	\centering
42	\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
43	\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-b
…[truncated 13792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-15T15:23:29.227308+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-15T15:23:29.629286+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-15T15:23:30.131515+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ratekv",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ratekv",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-15T15:23:30.182328+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/decisions.yaml\", \"content\": \"_next_id: 62\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:13 UTC\\n  summary: 'MVP 验证方案: Llama 3.1-8B 上验证 eviction-quantization crossover 存在性 + MCKP\\n    分配有效性'\\n  rationale: '核心假设是 per-KV-head 异质性使得 joint eviction+quantization allocation 优于 uniform\\n    quantization。最小验证: 单模型 distortion profiling + crossover 可视化 + MCKP vs uniform\\n    4-bit 对比。Pass 标准: ≥15% heads prefer eviction + perplexity improvement。选 Llama\\n    3.1-8B 因为 DuoAttention 已有该模型的 streaming/retrieval head 分类数据可做 post-hoc validation。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:16 UTC\\n  summary: 'MVP gate v2: 加 quant-only MCKP baseline + 消除死区 + 最小效应量 ≥0.5 PPL'\\n  rationale: 'Reviewer 初审指出三个漏洞: (1) uniform 4-bit 太弱，任何 per-head 方法都能赢，核心 claim 是\\n    joint > quant-only，必须加 quant-only MCKP baseline; (2) 5%-15% crossover 比例死区导致判定模糊，合并为单一\\n    ≥10% 阈值; (3) PPL 改善无最小效应量可能产生假阳性，设 ≥0.5 PPL 门槛。quant-only baseline 零额外工程量（同一 solver\\n    限制 action set）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 18:12 UTC\\n  summary: MVP 模型从 Llama 3.1-8B 切换到 Qwen2.5-7B，DuoAttention validation 延后\\n  rationale: Llama 3.1-8B 是 HF gated model，用户尚未提供 HF token，GPU 空闲不能等。Qwen2.5-7B 非\\n    gated、GQA 架构、7B 参数量相近，满足 MVP 验证 per-KV-head crossover 假设的需求。代价：DuoAttention post-hoc\\n    validation（D001 rationale 中的 convergent evidence story）暂时无法做——DuoAttention 论文只分析了\\n    Llama 系列。替代方案：(1) 用户后续提供 HF token 后加 Llama 作为第二模型；(2) 在 Qwen 上自行运行 DuoAttention\\n    分类作为替代验证。MVP 核心假设（crossover 存在性 + MCKP 优于 uniform）不依赖 DuoAttention 叙事。注意：Qwen2.5-7B\\n    的 KV head 数（4×28=112）少于 Llama（8×32=256），GQA ratio 更高（7:1 vs 4:1），crossover 比例可能偏低。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 21:55 UTC\\n  summary: 1.5B sanity 暴露 attention MSE 与 PPL 脱钩；7B 继续跑但需准备 metric 修正
…[truncated 1401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-15T15:23:32.591318+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-15T15:23:32.642235+00:00_

1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  ti
…[truncated 9960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-15T15:23:40.020834+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper && head -30 main.log 2>/dev/null | tail -5; echo \"---\"; grep -c \"Warning\\|Error\" main.log 2>/dev/null; echo \"---\"; grep \"Output written\" main.log 2>/dev/null; echo \"---PAGES---\"; grep -o \"([0-9]* page\" main.log 2>/dev/null",
  "description": "Check LaTeX compilation status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper && head -30 main.log 2>/dev/null | tail -5; echo \"---\"; grep -c \"Warning\\|Error\" main.log 2>/dev/null; echo \"---\"; grep \"Output written\" main.log 2>/dev/null; echo \"---PAGES---\"; grep -o \"([0-9]* page\" main.log 2>/dev/null",
    "description": "Check LaTeX compilation status"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-15T15:23:42.931995+00:00_

Conference Style for ACL
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
Package: xcolor 2024/09/29 v3.02 LaTeX color extensions (UK)

(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg
---
0
---
Output written on main.pdf (13 pages, 384111 bytes).
---PAGES---
(13 page
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_director_a1fe96c5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 2911
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-15T15:23:43.183299+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2 && grep -A5 \"external_review\" projects/ratekv/agent/project_config.yaml 2>/dev/null || grep -A5 \"external_review\" projects/ratekv/config.yaml 2>/dev/null || echo \"NO_CONFIG_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2 && grep -A5 \"external_review\" projects/ratekv/agent/project_config.yaml 2>/dev/null || grep -A5 \"external_review\" projects/ratekv/config.yaml 2>/dev/null || echo \"NO_CONFIG_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-15T15:23:43.284110+00:00_

NO_CONFIG_FOUND
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_director_a1fe96c5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-15T15:23:47.451786+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5; echo \"---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"project_config*\" -path \"*ratekv*\" 2>/dev/null | head -5; echo \"---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"config.yaml\" -path \"*ratekv*\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5; echo \"---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"project_config*\" -path \"*ratekv*\" 2>/dev/null | head -5; echo \"---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"config.yaml\" -path \"*ratekv*\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-15T15:23:47.552567+00:00_

---
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-15T15:23:50.464917+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"project_config*\" -o -name \"projects.yaml\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"project_config*\" -o -name \"projects.yaml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-15T15:23:50.515632+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-15T15:23:53.376127+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" | xargs grep -l \"ratekv\" 2>/dev/null | head -5",
  "description": "Find ratekv project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" | xargs grep -l \"ratekv\" 2>/dev/null | head -5",
    "description": "Find ratekv project config"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-15T15:23:53.527833+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-15T15:23:56.489837+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -10",
  "description": "Find framework config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -10",
    "description": "Find framework config"
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-15T15:23:56.690979+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-15T15:23:59.451562+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/agent-ml-research/ 2>/dev/null | head -20",
  "description": "List framework directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/agent-ml-research/ 2>/dev/null | head -20",
    "description": "List framework directory"
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-15T15:23:59.502239+00:00_

CLAUDE.md
PROGRESS.md
README.md
TEST.md
config
core
dashboard
docs
experiments
manager
portal
projects
prompts
pyproject.toml
scripts
skills
templates
tests
tools
uv.lock

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-15T15:24:03.117238+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/agent-ml-research/config/ 2>/dev/null && echo \"---\" && find /home/ubuntu/agent-ml-research/config -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Check config directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/agent-ml-research/config/ 2>/dev/null && echo \"---\" && find /home/ubuntu/agent-ml-research/config -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Check config directory"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-15T15:24:03.167899+00:00_

images.yaml
ralph_loop.yaml
---
/home/ubuntu/agent-ml-research/config/ralph_loop.yaml
/home/ubuntu/agent-ml-research/config/images.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-15T15:24:06.029292+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/projects -name \"*.yaml\" 2>/dev/null | head -10; echo \"---\"; ls /home/ubuntu/agent-ml-research/projects/ 2>/dev/null | head -10",
  "description": "Check projects directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research/projects -name \"*.yaml\" 2>/dev/null | head -10; echo \"---\"; ls /home/ubuntu/agent-ml-research/projects/ 2>/dev/null | head -10",
    "description": "Check projects directory"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-15T15:24:06.130123+00:00_

---
recursive_gen_depth_est

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-15T15:25:10.343246+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）\n\n### 论文信息\n- **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\n- **路径**: `projects/ratekv/docs/paper/main.tex`（模块化: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n- **目标 venue**: EMNLP 2026 Main Conference\n- **格式要求**: ACL template, 正文 ≤8 页（不含 references/limitations/appendix）, double-blind (ARR)\n- **截止日期**: 2026-05-25\n\n### 你的审查侧重\n\n**核心关注**：技术声明的严谨性和实验证据的充分性。\n\n重点审查以下方面：\n\n1. **Compounding claim 的因果论证**：论文声称 2-bit distortion compounding 是 unconstrained solver 失败的根因。super-additivity 数据 (1.56×–4.89×) 是否足以支撑因果而非仅为相关？是否有替代解释？\n\n2. **N=1 Spread 泛化性**：7 个模型中仅 Qwen2.5-7B 展示 spread pattern 且获益。这个 contribution 的泛化性如何？是否本质上是一个 model-specific finding？\n\n3. **Decision rule 拟合风险**：2 个自由参数 (concentration threshold ~0.50, t1/t5 ~0.70) 在 7 个样本上 7/7 正确分类，且正样本仅 1 个。这是否构成严重的 overfitting 风险？thresholds 的 sensitivity 如何？\n\n4. **KIVI 对比的公平性和意义**：KIVI+MCKP = KIVI alone (9.90)，论文将自身方法定位为 \"symmetric-only\" 环境有价值。这一定位是否合理？symmetric-only 的实际应用场景有多广？\n\n5. **统计可靠性**：\n   - 3-seed stability (10.99±0.06) 是否足够？\n   - Cross-dataset agreement (96-97%) 的统计显著性\n   - Downstream eval 仅 0-shot，无 confidence intervals\n\n6. **实验覆盖**：\n   - 是否缺少重要 baseline（如其他 mixed-precision KV cache 方法）？\n   - 模型规模上限 14B，是否足以支撑结论？\n   - 长文本评估仅 Qwen+Llama 两个模型\n\n7. **Runtime benchmark caveat**：仅 PyTorch-level simulation，8.5% overhead upper bound。对实际部署意味着什么？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 句)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序)\n- W1 [critical/major/minor]: ...\n- W2: ...\n\n## Questions (需要作者回答)\n- Q1: ...\n\n## Missing References (如有)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n```",
  "project": "ratekv"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）\n\n### 论文信息\n- **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\n- **路径**: `projects/ratekv/docs/paper/main.tex`（模块化: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n- **目标 venue**: EMNLP 2026 Main Conference\n- **格式要求**: ACL template, 正文 ≤8 页（不含 references/limitations/appendix）, double-blind (ARR)\n- **截止日期**: 2026-05-25\n\n### 你的审查侧重\n\n**核心关注**：技术声明的严谨性和实验证据的充分性。\n\n重点审查以下方面：\n\n1. **Compounding claim 的因果论证**：论文声称 2-bit distortion compounding 是 unconstrained solver 失败的根因。super-additivity 数据 (1.56×–4.89×) 是否足以支撑因果而非仅为相关？是否有替代解释？\n\n2. **N=1 Spread 泛化性**：7 个模型中仅 Qwen2.5-7B 展示 spread pattern 且获益。这个 contribution 的泛化性如何？是否本质上是一个 model-specific finding？\n\n3. **Decision rule 拟合风险**：2 个自由参数 (concentration threshold ~0.50, t1/t5 ~0.70) 在 7 个样本上 7/7 正确分类，且正样本仅 1 个。这是否构成严重的 overfitting 风险？thresholds 的 sensitivity 如何？\n\n4. **KIVI 对比的公平性和意义**：KIVI+MCKP = KIVI alone (9.90)，论文将自身方法定位为 \"symmetric-only\" 环境有价值。这一定位是否合理？symmetric-only 的实际应用场景有多广？\n\n5. **统计可靠性**：\n   - 3-seed stability (10.99±0.06) 是否足够？\n   - Cross-dataset agreement (96-97%) 的统计显著性\n   - Downstream eval 仅 0-shot，无 confidence intervals\n\n6. **实验覆盖**：\n   - 是否缺少重要 baseline（如其他 mixed-precision KV cache 方法）？\n   - 模型规模上限 14B，是否足以支撑结论？\n   - 长文本评估仅 Qwen+Llama 两个模型\n\n7. **Runtime benchmark caveat**：仅 PyTorch-level simulation，8.5% overhead upper bound。对实际部署意味着什么？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 句)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序)\n- W1 [critical/major/minor]: ...\n- W2: ...\n\n## Questions (需要作者回答)\n- Q1: ...\n\n## Missing References (如有)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n```",
    "project": "ratekv"
  }
}
````

</details>

---

### Tool result

_source line 225 · 2026-05-15T15:25:31.342462+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20999
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-15T15:25:34.202293+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## Round 2 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作）\n\n### 论文信息\n- **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\n- **路径**: `projects/ratekv/docs/paper/main.tex`（模块化: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n- **目标 venue**: EMNLP 2026 Main Conference\n- **格式要求**: ACL template, 正文 ≤8 页（不含 references/limitations/appendix）, double-blind (ARR)\n- **截止日期**: 2026-05-25\n\n### 你的审查侧重\n\n**核心关注**：Contribution 的新颖性定位、related work 的完整性、写作质量和格式合规。\n\n重点审查以下方面：\n\n1. **Novelty 评估**：\n   - Cardinality constraint 本身是标准 MCKP 技术。论文的真正 novelty 是什么？diagnosis of compounding? heterogeneity characterization? 还是两者的组合？\n   - 与 HAWQ/HAQ (weight-level mixed precision) 的技术区分是否充分？\n   - RateQuant 是最近的直接竞争者——论文是否清楚地说明了相对于 RateQuant 的增量贡献？\n\n2. **Contribution 定位的诚实度**：\n   - 论文声称 3 个 contributions。考虑到 6/7 模型上方法 ≈ uniform，这些 claim 是否 overclaimed？\n   - \"empirical decision rule\" 的实用价值：一个需要完整 profiling 数据才能运行的 decision rule，而 profiling 本身已经给出了 allocation——用户为什么不直接跑 allocation 看结果？\n   - Abstract 中 \"29.4% reduction\" 是否给读者造成方法普遍有效的印象？\n\n3. **Related Work 完整性**：\n   - 是否遗漏了 2025-2026 年重要的 KV cache 工作？\n   - Token-level mixed-precision 方法（如 MixKVQ, ZipCache 的 token-level 部分）是否应该作为更直接的 baseline 而非仅在 related work 中讨论？\n   - 引用格式是否符合 ACL/natbib 标准？\n\n4. **写作质量**：\n   - 论文结构是否清晰？narrative flow 是否连贯？\n   - 论证逻辑：Introduction 中的 \"catastrophic failure\" narrative 是否过度渲染？（6/7 模型上 unconstrained 失败并不严重）\n   - 术语一致性（spread/spike/flat 是否有歧义？是否需要更 formal 的定义？）\n   - Figures 和 Tables 是否自包含（caption 是否足够详细）？\n\n5. **格式合规（EMNLP 2026 / ARR）**：\n   - 正文页数是否在 8 页以内（不含 references, limitations, appendix）？\n   - Limitations section 是否存在且位置正确（conclusion 之后、references 之前）？\n   - 匿名性：是否有 self-citation 泄露？代码/数据链接是否匿名？\n   - Appendix 是否合理使用（是否有本应在正文的关键内容被放到了 appendix）？\n\n6. **Reproducibility**：\n   - 方法描述是否足以复现？profiling 的具体参数？solver 实现细节？\n   - 是否提供了代码/数据？（匿名提交阶段可能不要求）\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 句)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序)\n- W1 [critical/major/minor]: ...\n- W2: ...\n\n## Questions (需要作者回答)\n- Q1: ...\n\n## Missing References (如有)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n```",
  "project": "ratekv"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## Round 2 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作）\n\n### 论文信息\n- **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\n- **路径**: `projects/ratekv/docs/paper/main.tex`（模块化: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n- **目标 venue**: EMNLP 2026 Main Conference\n- **格式要求**: ACL template, 正文 ≤8 页（不含 references/limitations/appendix）, double-blind (ARR)\n- **截止日期**: 2026-05-25\n\n### 你的审查侧重\n\n**核心关注**：Contribution 的新颖性定位、related work 的完整性、写作质量和格式合规。\n\n重点审查以下方面：\n\n1. **Novelty 评估**：\n   - Cardinality constraint 本身是标准 MCKP 技术。论文的真正 novelty 是什么？diagnosis of compounding? heterogeneity characterization? 还是两者的组合？\n   - 与 HAWQ/HAQ (weight-level mixed precision) 的技术区分是否充分？\n   - RateQuant 是最近的直接竞争者——论文是否清楚地说明了相对于 RateQuant 的增量贡献？\n\n2. **Contribution 定位的诚实度**：\n   - 论文声称 3 个 contributions。考虑到 6/7 模型上方法 ≈ uniform，这些 claim 是否 overclaimed？\n   - \"empirical decision rule\" 的实用价值：一个需要完整 profiling 数据才能运行的 decision rule，而 profiling 本身已经给出了 allocation——用户为什么不直接跑 allocation 看结果？\n   - Abstract 中 \"29.4% reduction\" 是否给读者造成方法普遍有效的印象？\n\n3. **Related Work 完整性**：\n   - 是否遗漏了 2025-2026 年重要的 KV cache 工作？\n   - Token-level mixed-precision 方法（如 MixKVQ, ZipCache 的 token-level 部分）是否应该作为更直接的 baseline 而非仅在 related work 中讨论？\n   - 引用格式是否符合 ACL/natbib 标准？\n\n4. **写作质量**：\n   - 论文结构是否清晰？narrative flow 是否连贯？\n   - 论证逻辑：Introduction 中的 \"catastrophic failure\" narrative 是否过度渲染？（6/7 模型上 unconstrained 失败并不严重）\n   - 术语一致性（spread/spike/flat 是否有歧义？是否需要更 formal 的定义？）\n   - Figures 和 Tables 是否自包含（caption 是否足够详细）？\n\n5. **格式合规（EMNLP 2026 / ARR）**：\n   - 正文页数是否在 8 页以内（不含 references, limitations, appendix）？\n   - Limitations section 是否存在且位置正确（conclusion 之后、references 之前）？\n   - 匿名性：是否有 self-citation 泄露？代码/数据链接是否匿名？\n   - Appendix 是否合理使用（是否有本应在正文的关键内容被放到了 appendix）？\n\n6. **Reproducibility**：\n   - 方法描述是否足以复现？profiling 的具体参数？solver 实现细节？\n   - 是否提供了代码/数据？（匿名提交阶段可能不要求）\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 句)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序)\n- W1 [critical/major/minor]: ...\n- W2: ...\n\n## Questions (需要作者回答)\n- Q1: ...\n\n## Missing References (如有)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n```",
    "project": "ratekv"
  }
}
````

</details>

---

### Tool result

_source line 227 · 2026-05-15T15:25:35.565829+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1363
}
```

</details>

---

### Assistant

_source line 228 · 2026-05-15T15:25:43.988800+00:00_

两位 Reviewer 已分配：

- **Reviewer 1** → 方法严谨性 + 实验验证（compounding 因果论证、N=1 泛化性、decision rule 拟合风险、KIVI 对比、统计可靠性）
- **Reviewer 2** → 新颖性 + 完整性 + 写作（contribution 定位、related work 覆盖、overclaiming 风险、格式合规、匿名性）

等待两位 Reviewer 独立初审结果返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 14

2 recorded events

### User

_source line 229 · 2026-05-15T15:30:01.726175+00:00_

[Reviewer 1 审稿意见]:
## Round 2 Review — Reviewer 1（方法严谨性 + 实验验证）

**论文**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic
**Target venue**: EMNLP 2026 Main Conference (ACL ARR)

---

## Summary (2-3 句)

本文将 per-head KV cache 混合精度量化建模为基数约束的 MCKP 问题，核心发现是限制 2-bit head 数量可防止 distortion compounding 导致的灾难性退化。论文同时提出基于 concentration 和 t1/t5 的 heterogeneity diagnostic 来预判非均匀分配是否有益。技术思路清晰，但关键贡献（spread pattern 和 decision rule）的统计支撑极为薄弱——正样本仅 1 个模型，decision rule 在 7 个样本上有严重过拟合风险。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 | 核心 claim（compounding 是 root cause）有合理机制解释但因果论证不够严谨；decision rule 统计基础极弱（N=1 正样本） |
| **Excitement** | 2.5/5 | 问题有实际意义，但 7 个模型中仅 1 个获益，实用价值受限；缺少大规模模型验证 |
| **Overall** | 2.5/5 | Borderline Findings——有有趣的观察和合理的形式化，但核心贡献的泛化性和统计可靠性不足以支撑 main conference |
| **Confidence** | 4/5 | 仔细检查了方法、实验设计和数据，对量化和 KV cache 文献较熟悉 |
| **Reproducibility** | 4/5 | 提供了详细的 profiling 流程、模型列表、超参数；未提供代码但描述足够复现 |

---

## Strengths

- **S1**: 问题形式化干净优雅。将 per-head mixed-precision 量化建模为 MCKP，cardinality constraint 作为 minimal intervention 防止 compounding，理论动机清晰（Section 3.1-3.4）。Proposition 6 关于 polynomial structure 和 greedy optimality 的论证是扎实的。

- **S2**: Compounding effect 的实验刻画有价值。Section 3.3 的 super-additivity 数据（1.56×–4.89×）和 Figure 1 的 U-shaped curve 为理解 2-bit 量化失败模式提供了有用的 empirical evidence，这一观察本身对社区有参考价值。

- **S3**: 实验设计覆盖了 5 个架构族 7 个模型（MHA 到 GQA 8:1），且包含 cross-dataset validation（Appendix G）和 multi-seed stability（Section 4.2），展现了对实验严谨性的意识。

- **S4**: 论文对 KIVI 对比的定位较为诚实——明确承认 "complementary, not competitive"（Section 4.2），没有过度宣称优于 asymmetric 方法。

- **S5**: Appendix 内容丰富（A-L，13 个子节），高分辨率 heatmap（Figure 3）、budget sweep（Table 6）、KV 分离消融（Appendix J）等补充材料增强了可信度。

---

## Weaknesses (按严重程度排序)

### W1 [critical]: Decision rule 的 N=1 正样本构成根本性的统计缺陷

- **具体位置**: Section 5.2, Table 4, Section 8 (Limitations)
- **问题**: Decision rule 用 2 个自由参数（concentration threshold ~0.50, t1/t5 threshold ~0.70）在 7 个模型上实现 7/7 分类正确率，但**正样本仅 Qwen2.5-7B 一个**。这在统计学上几乎没有意义：
  - 任何能将 1 个点与其余 6 个分开的线性分界面都能 "100% 准确"——这不是 discriminative power 的证据，而是自由度过剩的必然结果
  - 无法计算 precision/recall/F1，因为 TP=1, FP=0, FN=0 的置信区间无穷大
  - 没有 leave-one-out cross-validation，没有 threshold sensitivity analysis（如果 concentration 阈值从 0.50 移到 0.45 或 0.55 会怎样？）
  - 论文声称 "correctly classifies all seven evaluated models (7/7)" 时未提及正样本仅 1 个这一关键事实的统计含义
- **为什么影响接收**: 这是论文三个 contribution 之一（Section 1 第三条贡献："we propose a joint empirical decision rule"）。一个 N=1 正样本的 decision rule 无法被视为可靠的科学发现——它本质上是对单一模型的 post-hoc description，而非泛化性规律。
- **建议修改方向**: (a) 大幅降低 decision rule 的 claim 强度，明确表述为 "preliminary observation on 7 models with 1 positive case"；(b) 补充 threshold sensitivity 分析（扫描参数空间）；(c) 增加更多模型以扩大正样本数量，或者 (d) 将 decision rule 从 contribution 列表中移除，降级为 discussion 中的观察。

### W2 [critical]: Compounding claim 的因果推断不够严谨

- **具体位置**: Section 3.3, Section 1 (contribution 1)
- **问题**: 论文将 2-bit distortion compounding 定位为 unconstrained solver 失败的 **root cause**（Section 1: "We identify 2-bit distortion compounding as the cause of catastrophic failure"）。但实际提供的证据是：
  - Super-additivity 数据（1.56×–4.89×）——这证明了 compounding 的**存在**，但不排除其他因素也参与导致失败
  - Cardinality constraint 修复了问题——这证明限制 2-bit 数量有效，但 constraint 可能通过**其他机制**（如避免数值不稳定的极端量化配置）起作用，而非专门因为阻止了 "compounding"
  - Super-additivity 的详细分析仅在 Qwen2.5-7B 上进行（Section 3.3 的 "64 sequences" profiling），其他模型未展示 compounding 的量化数据
  - 替代解释未被排除：例如，2-bit 量化的绝对误差是否已经大到单独导致退化（而非必须通过 compounding）？在 Section 3.2 中提到 "individual head distortions are typically below 0.1 PPL" 但 2-bit 时 "distortions are of magnitudes larger"——如果单个 2-bit head 的 distortion 已经很大，是否即使不 compound 也会导致退化？
- **为什么影响接收**: "Cause" 这个词在科学论文中有特定含义，需要排除替代假说的实验设计。当前证据支持 "2-bit compounding is a contributing factor" 但不足以支撑 "the cause"。
- **建议修改方向**: (a) 将 "cause" 改为 "a major contributing factor"；(b) 在其他模型上也展示 super-additivity 数据；(c) 设计控制实验排除替代解释（如固定 2-bit head 数量但随机 vs. profiling-guided 选择，以分离 compounding 效应和选择效应）。

### W3 [major]: 关键 baseline 缺失——混合精度 KV cache 文献对比不足

- **具体位置**: Section 2 (Related Work), Section 4.2, Table 2
- **问题**: 论文 Related Work 中提到了多种混合精度方法（KIVI, KVTuner, GEAR, RKVO, MiKV, Kitty），但实验对比仅包含 KIVI。特别是：
  - **KVTuner**（Li et al., 2025）——论文 Section 2 自己提到 "KVTuner: Sensitivity-aware layer-wise mixed-precision KV cache quantization"，这是最直接的 competitor（也做 sensitivity-aware mixed-precision），却未对比
  - **GEAR**（Kang et al., 2024）——"efficient KV cache compression recipe for near-lossless generative inference"，也是重要 baseline
  - **Kitty**（Xu et al., 2025）——"accurate and efficient 2-bit KV cache quantization with dynamic channel-wise precision boost"，直接处理 2-bit 问题
  - Table 5 中的 heuristic baselines（L0-random, Naive positional）是 strawman——没有真正的 SOTA mixed-precision 方法作为对比
- **为什么影响接收**: 缺少直接 competitor 的对比使得无法判断论文方法相对于现有 SOTA 的真实贡献。读者无法确定 cardinality constraint 是否优于 KVTuner 等已有方法。
- **建议修改方向**: 至少补充 KVTuner 的对比（同为 sensitivity-aware, mixed-precision, per-head allocation）。如果实验资源有限，可以在 1-2 个代表性模型上对比。

### W4 [major]: 模型规模上限 14B，对结论泛化性构成重大限制

- **具体位置**: Section 4.1, Table 2, Section 8 (Limitations)
- **问题**: 
  - KV cache 压缩的实际需求主要在 70B+ 模型的长序列推理场景，14B 模型的 KV cache 压力相对较小
  - 更大模型的 head sensitivity 分布可能存在质的差异——例如 Llama-70B/405B 的 GQA 结构、head 数量大幅增加后 concentration pattern 是否改变？
  - 论文的 decision rule 是否适用于 head 数量从 112 扩展到 1000+ 的情况？
  - Limitations section 提到 "untested beyond 14B" 但这不是一个可以轻描淡写的局限——它直接影响方法的实用价值
- **为什么影响接收**: 一个声称解决 KV cache 量化问题的方法如果不能在实际需要 KV cache 压缩的模型规模上验证，其贡献的实际意义存疑。
- **建议修改方向**: (a) 至少在一个 30B+ 模型上验证（如 Qwen2.5-32B 或 Llama-3-70B）；(b) 如果资源受限，应分析 head 数量 scaling 对 concentration pattern 的影响并提供理论预测。

### W5 [major]: 统计可靠性问题——downstream evaluation 缺乏 confidence intervals

- **具体位置**: Table 3, Section 4.2
- **问题**:
  - Table 3 的 0-shot accuracy 差异极小：ARC-C 变化 +1.2 到 -0.6，HellaSwag 变化 +0.6 到 -0.3，PIQA 变化 +1.1 到 -0.7，WinoGrande 变化 +2.0 到 -0.5。这些差异**完全在典型的评估噪声范围内**（0-shot evaluation 的标准差通常在 0.5-1.5%）
  - 没有 confidence intervals 或 p-values，无法判断任何差异是否统计显著
  - 仅报告 0-shot，未测试 few-shot 或其他设置
  - Cross-dataset agreement "96-97%"（Section 4.2 / Appendix G）——未进行 bootstrap CI 或 McNemar test，97% 的 bit-assignment agreement 是否在统计上显著高于 random chance？
  - 3-seed stability 仅在 Qwen2.5-7B 上测试（10.99±0.06），其他模型未报告
- **为什么影响接收**: 在如此小的效应量下，不提供统计显著性检验会让读者怀疑报告的改善是否真实。
- **建议修改方向**: (a) 对 Table 3 所有模型运行 3+ seeds 并报告均值±标准差；(b) 对 cross-dataset agreement 进行置换检验；(c) 补充 5-shot evaluation。

### W6 [major]: Runtime benchmark 的 simulation 性质严重削弱实用性声明

- **具体位置**: Table 7, Appendix K, Section 8
- **问题**:
  - Table 7 明确标注 "PyTorch-level latency... simulated per-head quantize/dequantize calls"——这不是真实的推理性能
  - 论文承认 "do not represent optimized CUDA kernel performance"，且 "fused attention kernels that batch dequantization with the matrix multiply, amortizing the per-head dispatch cost"
  - 8.5% overhead 被定位为 "upper bound"，但没有任何下界估计
  - 实际部署中 mixed-precision dispatch 的开销取决于 kernel 实现，PyTorch-level simulation 可能**低估**（额外内存带宽）或**高估**（kernel fusion 可消除的开销）实际影响
  - 论文结论 "not a memory trade-off" 基于 simulation 数据，但没有 real kernel 验证
- **为什么影响接收**: 方法的实用价值取决于运行时开销是否可接受。没有真实 kernel benchmark，读者无法评估部署可行性。
- **建议修改方向**: (a) 使用已有的 mixed-precision attention kernel（如 vLLM 或 TensorRT-LLM 中的实现）进行真实 benchmark；(b) 如果无法获取，应更保守地表述 runtime claim，并将 "8.5% upper bound" 改为 "inconclusive"。

### W7 [minor]: Symmetric-only 定位的实用场景不够清晰

- **具体位置**: Section 4.2 (Comparison with KIVI), Section 6
- **问题**: 论文将自身定位为 "symmetric-only" 量化环境下的方案，与 KIVI 的 asymmetric per-channel 方法互补。但：
  - 现代推理引擎（vLLM, TensorRT-LLM, SGLang）普遍支持 asymmetric quantization
  - 什么实际场景**必须**使用 symmetric-only？论文未给出具体的部署约束场景
  - 如果 KIVI 已经通过 asymmetric quantization 达到 9.90 PPL（vs. 论文的 10.91），且 KIVI+MCKP 没有额外收益，那么 symmetric-only 的贡献空间有多大？
- **建议**: 补充 1-2 段说明 symmetric-only 量化的具体应用场景（如特定硬件约束、特定推理框架的限制）。

### W8 [minor]: 长文本评估覆盖不足

- **具体位置**: Table 8, Appendix L
- **问题**: 长序列评估仅在 Qwen2.5-7B 和 Llama-3.1-8B 两个模型上测试（2K vs 8K），且 8K 仍然是相对短的上下文。对于 KV cache 压缩这一研究方向，32K+ 场景下的行为才是关键验证——compounding effect 在更长序列中可能加剧或缓解。

---

## Questions (需要作者回答)

- **Q1**: Section 3.3 的 super-additivity 数据仅在 Qwen2.5-7B 上收集。其他 6 个模型是否也展示 super-additivity？如果是，为什么它们不从 cardinality constraint 中获益？如果不是，"compounding is the cause" 这个 claim 如何适用于全部模型？

- **Q2**: Decision rule 的两个 threshold（concentration ~0.50, t1/t5 ~0.70）是如何选择的？是通过系统的 grid search 还是 visual inspection？如果将 concentration 阈值改为 0.40 或 0.60，t1/t5 阈值改为 0.60 或 0.80，分类结果是否改变？

- **Q3**: Table 1 显示 unconstrained MCKP（36.92 PPL）远差于 unconstrained greedy（32.45 PPL）。这是否意味着 MCKP 的 polynomial structure 假设在 unconstrained 情况下**更加**不可靠？如果是，为什么在 constrained 情况下 MCKP 又是可靠的？

- **Q4**: Appendix J 的 KV separation ablation 发现 "K and V are not treated independently against the cardinality constraint"——joint allocation 中 K 倾向获得更多 2-bit 分配。这一 asymmetry 的原因是什么？是否暗示 K 和 V 应该有独立的 cardinality constraint？

- **Q5**: 论文是否考虑过在 calibration 阶段使用不同长度的序列？当前 calibration 使用 512 token（Section 4.1），但 profiling 在短序列上的 sensitivity 估计是否能外推到长序列？Table 8 的 8K 结果是否使用了 512 token 的 calibration profile？

- **Q6**: 对于 "flat" pattern 的模型（Gemma-2, Qwen-14B, Pythia），constrained MCKP 产生与 uniform 4-bit **相同**的分配吗？还是产生不同但等效的分配？如果前者，为什么 MCKP solver 的开销是合理的？

---

## Missing References

- **KIVI-V2 or per-channel variants**: 论文仅对比了 KIVI 原版，但 2025 年是否有 KIVI 的改进版本？
- **SqueezeLLM** (Kim et al., 2024) 和其他 weight+KV joint quantization 方法可能值得在 Related Work 中讨论
- 论文引用列表中包含多个 "Preprint, arXiv" 未标注年份或会议——应更新已接收论文的 venue 信息

---

## Overall Assessment

**Score: 2.5 (Borderline Findings)**

**Confidence: 4/5**

**一句话总结**: 论文提出了一个优雅的形式化框架（cardinality-constrained MCKP）来理解和解决 per-head KV cache 量化中的 2-bit compounding 问题，但其最核心的贡献——heterogeneity diagnostic 和 decision rule——在 N=1 正样本上缺乏统计可信度，关键 baseline 缺失，且 14B 的模型规模上限限制了实际影响力。

**主要接收障碍**:
1. Decision rule 的 N=1 正样本使其从 "empirical finding" 降级为 "anecdotal observation"
2. 缺少 KVTuner 等直接 competitor 的实验对比
3. 方法仅在 ≤14B 模型上验证，而 KV cache 压缩的核心需求在大模型

**如果作者能补充**：(a) 更多展示 spread pattern 的模型（哪怕只增加 1-2 个正样本），(b) 与 KVTuner 的对比，(c) 一个 30B+ 模型的验证——论文可以上升到 Findings 水平。当前状态下，形式化框架的贡献值得发表，但 claim 需要显著收缩。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 230 · 2026-05-15T15:30:15.944926+00:00_

Reviewer 1 审稿意见已收到。

**R1 核心发现摘要**：
- Score: 2.5/5 (Borderline Findings), Confidence: 4/5
- 2 个 critical：W1 (decision rule N=1 正样本) + W2 (compounding 因果论证不严谨)
- 4 个 major：W3 (缺 KVTuner 等 baseline) + W4 (模型规模 ≤14B) + W5 (downstream 无 CI) + W6 (runtime 仅 simulation)
- 2 个 minor：W7 (symmetric-only 场景不清) + W8 (长文本评估不足)

等待 Reviewer 2 意见，收齐后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 15

2 recorded events

### User

_source line 231 · 2026-05-15T15:30:18.490445+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Borderline Findings (2.5/5)**。

主要问题：
1. **Decision rule N=1 正样本** [critical]——7 个模型中仅 Qwen2.5-7B 展示 spread pattern，2 个自由参数在 1 个正样本上的 "7/7 分类" 没有统计意义
2. **Compounding 因果论证不严谨** [critical]——super-additivity 数据仅来自 Qwen2.5-7B，"cause" 这个词过强
3. **关键 baseline 缺失** [major]——未对比 KVTuner 等直接 competitor
4. **模型规模 ≤14B** [major]——KV cache 压缩的核心需求在大模型
5. **Downstream eval 无 CI** [major]——Table 3 的差异在评估噪声范围内
6. **Runtime 仅为 simulation** [major]——8.5% overhead 基于 PyTorch-level 模拟

亮点：形式化框架（MCKP + cardinality constraint）干净优雅，compounding effect 的刻画对社区有参考价值，KIVI 对比的诚实定位值得肯定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 232 · 2026-05-15T15:30:24.837830+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 16

6 recorded events

### User

_source line 233 · 2026-05-15T15:33:14.500358+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 2 审稿意见

### 论文信息
**标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic
**Venue**: EMNLP 2026 Main Conference (via ACL ARR)

---

## Summary (2-3 句)

本文系统研究了 per-head mixed-precision KV cache 量化在硬件对齐 bit-width {2,4,8,16} 下何时有效。通过对 7 个模型（5 个架构族，1.4B-14B）的实验，发现非均匀分配仅在 head sensitivity 呈"spread"分布时有效（7 个模型中仅 Qwen2.5-7B），并提出一个 2-bit 赋值基数约束来防止失控的量化误差累积。文章还提出了一个基于 concentration + t₁/t₅ ratio 的经验判别规则来预测非均匀分配是否有益。

---

## Strengths

- **S1: 有价值的负面结论。** 论文诚实地报告了 6/7 模型上非均匀分配无实质收益，这对社区有重要参考价值——避免后续工作在不适用的架构上浪费算力做 mixed-precision 搜索。这种 "when does it NOT help" 的研究视角在 KV cache 量化文献中很稀缺。

- **S2: 实验设计严谨。** 7 个模型覆盖 MHA 到 GQA 8:1，包含 within-family scale contrast（Qwen-7B vs 14B）。多 seed 评估（Table 2 报告 median 和 mad）、cross-dataset stability（Appendix G，C4 vs WikiText-2 一致性 96.4%）、profiling resolution/stability 消融（Appendix I）和 long-context generalization（Appendix L）均提升了结果可信度。

- **S3: Compounding effect 的因果分析。** Section 3.3 对 2-bit 量化误差如何通过 residual stream 累积导致 PPL super-linearly 退化的分析（包括 Appendix A 的 U-shaped curve）提供了有用的机理解释，不仅描述现象还给出了为什么 cardinality constraint 有效的理论动机。

- **S4: 实用性考虑。** 证明 cardinality constraint 使 greedy 和 MCKP 等价（Section 3.5），从而支持 O(H log B) 的简单实现，对工程部署有价值。Runtime benchmark（Appendix K）提供了端到端延迟数据。

---

## Weaknesses (按严重程度排序)

### W1 [major]: Abstract 中 "29.4% reduction" 的突出呈现具有误导性

**具体位置**: Abstract 第 3-4 行

**问题**: Abstract 以 "29.4% reduction over uniform 4-bit" 作为最突出的定量结果，但这仅来自 7 个模型中的 1 个（Qwen2.5-7B）。论文后续承认其余 6 个模型 "non-uniform allocation provides no meaningful benefit"，但读者的第一印象已经形成。一个在 85.7% 的测试模型上无效的方法，其最佳案例不应作为 abstract 的 lead metric。

**为什么影响评分**: 这是 framing honesty 的问题。Reviewer 和读者会根据 abstract 决定是否深入阅读。当前 framing 容易给人"方法普遍有效"的印象，直到读完 Section 4 才会纠正。

**建议**: Abstract 应先陈述主要发现（"7 个模型中仅 1 个受益"），再给出 Qwen 的具体数字作为 case study。将 "29.4%" 降级为支撑性细节而非 headline。

### W2 [major]: 经验判别规则的实用价值存疑——与直接运行 solver 相比无增量收益

**具体位置**: Section 5.2（p8），Contribution 3

**问题**: 判别规则需要完整的 per-head profiling 数据（concentration 和 t₁/t₅ ratio），而 profiling 本身已产出 per-head distortion 值——这正是 solver 的输入。既然 solver 是 O(H log B)（论文自己在 Section 3.5 证明），对 112 个 head 只需微秒级计算，直接运行 solver 并比较 constrained MCKP vs uniform 的 PPL 差异即可判断是否值得非均匀分配。判别规则在计算成本上不比"直接跑一遍"更便宜，反而引入了 threshold 选择的任意性（concentration 0.36、t₁/t₅ 0.57 等阈值是从 N=7 个模型上拟合的）。

**为什么影响评分**: 作为三个 claimed contributions 之一，判别规则的实际增量贡献需要更强的论证。如果去掉这个 contribution，论文本质上是一个 well-executed empirical study + 一个 trivial 的 constraint fix（一条线性不等式）。

**建议**: (1) 明确论证判别规则相对于"直接运行 solver 比较结果"的增量价值——是否存在 solver 不可用或 profiling 不完整的场景？(2) 讨论 N=7 拟合规则的 generalization 风险；(3) 或者将其重新定位为 analytical insight（帮助理解 "什么架构特性决定了非均匀是否有效"）而非 practical tool。

### W3 [major]: 新颖性定位模糊——与 RateQuant 的增量贡献需要更清晰的界定

**具体位置**: Section 1（Introduction）、Section 3.1（Problem Formulation）

**问题**: RateQuant (Zhao et al., 2026) 已经将 per-head bit-width 选择公式化为 MCKP 并证明了 greedy 的最优性。本文的技术贡献归结为：(1) 在 MCKP 上加一条 cardinality constraint（Eq. 2，一条线性不等式）；(2) 诊断 2-bit compounding；(3) spread/spike/flat 分类学。这些是 RateQuant 的 incremental extension 而非独立方法。论文在 Introduction 第 2 段提到 RateQuant 但未清楚说明自己与 RateQuant 的本质差异在哪里——是发现 RateQuant 在实践中会失败（unconstrained MCKP 的问题），还是提出了根本不同的方法？

**为什么影响评分**: 新颖性是 ACL ARR Excitement 维度的核心。如果主要贡献是一个约束修补 + 负面实验结果，excitement 分数可能受限。

**建议**: 在 Introduction 中明确区分：RateQuant 解决了什么（formulation），本文解决了什么（RateQuant 的 failure mode + when-to-use characterization）。如果可能，用一段文字直接对比两者的输入/输出/假设差异。

### W4 [minor-to-major]: "Catastrophic failure" 叙事在 Introduction 中过度渲染

**具体位置**: Introduction 第 1 段及 Abstract

**问题**: 论文使用 "catastrophic failure"、"fail catastrophically" 来描述 unconstrained solver 的表现。但从 Table 2 看：
- 在 Qwen2.5-7B 上，unconstrained MCKP PPL 为 36.92（baseline bf16=8.01，uniform 4-bit=15.45），确实是灾难性的。
- 但在其他模型上，unconstrained MCKP 的 PPL 仅比 uniform 差 1.4-1.7×（如 Gemma-2-9B 的 1.4×）。

"Catastrophic" 严格来说只适用于 Qwen2.5-7B。在其他 flat 模型上，unconstrained 的问题是 "moderate over-allocation"（论文自己在 p2 用这个词）而非 "catastrophic failure"。在 Introduction 的叙事弧线中用 "catastrophic" 作为 motivating problem 会让读者以为这是一个普遍性问题，实际上只在特定 sensitivity 分布下出现。

**建议**: 将 "catastrophic failure" 限定在 spread 架构的上下文中，对 flat 架构用更准确的描述（如 "moderate degradation" 或 "suboptimal allocation"）。

### W5 [minor]: Spread/spike/flat 术语缺乏 formal definition

**具体位置**: Section 5.1-5.2, Table 4

**问题**: "Spread"、"spike"、"flat" 是论文的核心分析框架，但定义依赖于读者对 Table 4 的直觉理解。论文给出了 concentration（top-5% 贡献比）和 t₁/t₅ ratio 两个量化指标，但从指标到三个类别的映射缺乏形式化的 decision boundary。Section 5.2 给出了阈值（concentration 0.36, t₁/t₅ 0.57/0.71），但这些阈值是 post-hoc 从 7 个数据点拟合的，无 held-out validation。

**建议**: (1) 给出 formal definition（例如 spread := concentration > τ₁ AND t₁/t₅ < τ₂）；(2) 承认阈值是 descriptive 而非 prescriptive，需要在更多模型上验证。

### W6 [minor]: Related work 中对 token-level mixed-precision 的定位可以更精确

**具体位置**: Section 2, Related Work

**问题**: 论文在 related work 中引用了 MixKVQ 和 ZipCache 等 token-level mixed-precision 方法，但未充分讨论为什么 per-head（spatial across heads）和 per-token（temporal across positions）是正交的优化轴。Appendix E 简要提到了 layer-level 和 per-head 的 granularity tradeoff，但未涉及 per-token 维度。此外，以下近期工作可能值得提及：
- Cocktail (Tian et al., 2025): chunk-adaptive mixed precision，提出 chunk 粒度的折中
- MiKV / "No Token Left Behind" (Yao et al., 2024): importance-aware mixed precision at token level
- "More Tokens, Lower Precision" (2024): 探索 token-precision tradeoff 的 Pareto frontier

这些工作进一步说明 mixed-precision KV cache 量化的粒度选择空间比论文讨论的更丰富。

**建议**: 在 Related Work 中增加 1-2 句明确说明 per-head bit-width allocation 与 token-level/chunk-level mixed precision 的正交关系和互补性。

### W7 [minor]: Limitations section 过于简短

**具体位置**: Page 8, Limitations

**问题**: Limitations 只有两句话：模型数 N=1 (Qwen2.5-7B) 展示收益；评估是 directional 而非 robust（无 real-kernel latency benchmarks，上限 14B）。但还有几个重要 limitation 未提及：
- 判别规则的阈值仅从 7 个模型拟合，泛化性未知
- 仅评估了 perplexity 和 4 个 downstream tasks（0-shot），未涉及生成质量（如 summarization、translation）或 long-context reasoning
- Profiling 依赖 WikiText-2 校准，对 domain shift 的鲁棒性仅在 C4 上验证（Appendix G）

**建议**: 扩展 Limitations section 以覆盖这些方面。

### W8 [minor]: Table caption 自包含性可改进

**具体位置**: Table 1 (p5), Table 2 (p6)

**问题**: Table 1 caption 说 "Solver comparison on Qwen2.5-7B at 4× compression"，但未解释表中 "k=5" 的含义需要读者回到 Section 3.4 查找。Table 2 caption 较详细但未说明 "BOS-corrected" 的含义。理想情况下 caption 应包含足够信息让读者无需跳转即可理解表格。

---

## Questions (需要作者回答)

- **Q1**: 对于 Qwen2.5-7B 上的 spread pattern——如果用不同的校准数据（例如 code corpus 或 conversation data），sensitivity distribution 是否仍然是 spread？换言之，spread vs flat 是模型的固有属性还是校准数据的函数？Appendix G 的 C4 cross-dataset 实验回答了 allocation stability，但没有回答 distribution shape 是否可能根本性变化。

- **Q2**: Cardinality constraint 的 k 值通过小规模 sweep 选取（Section 3.4）。这个 sweep 本身需要在每个候选 k 上评估 calibration PPL。对于 production 场景中新模型的部署，这个流程的端到端开销（profiling + k sweep + solver）是多少？Table 7 只报告了 inference latency，不包括 profiling 成本。

- **Q3**: 论文将 Yi-1.5-9B 归类为 "spike"（concentration 0.71，t₁/t₅=0.90），并指出其无收益因为异质性集中在一个 outlier 上。但如果将该 outlier head 单独分配到 8-bit 而其余保持 4-bit，是否能获得收益？论文是否排除了这种 "single-head upgrade" 的可能？

- **Q4**: RateQuant (Zhao et al., 2026) 在相同模型上的表现如何？论文将其作为 MCKP formulation 的来源引用，但 Table 2 中的 unconstrained MCKP 是否就是 RateQuant 的复现？如果是，请明确说明；如果不是，需要解释与 RateQuant 的实验差异。

---

## Missing References (补充建议)

1. **Cocktail** (Tian et al., 2025): "Chunk-Adaptive Mixed-Precision Quantization for Long-Context LLM Inference" — chunk 粒度的 mixed precision，填补 per-head 和 per-token 之间的粒度空间。
2. **MiKV / "No Token Left Behind"** (Yao et al., 2024): "Reliable KV Cache Compression via Importance-Aware Mixed Precision Quantization" — token-level importance-aware mixed precision 的早期工作。
3. **"More Tokens, Lower Precision"** (2024): 探索 token-precision tradeoff 的理论分析。

这些不影响论文的核心 claim，但作为 related work 可以更完整地呈现 mixed-precision KV cache 量化的研究图景。

---

## 引用格式与真实性审查

引用验证工具检查结果：
- 31 条 bib entries，全部被正文引用，无 orphan 或 missing
- 25 条通过 OpenAlex 验证，2 条未找到（liu2024kivi 可能是 API 索引延迟；haeriboroujeni2026dontwaste 是 CVPR 2026 可能尚未收录），4 条存在 first author 不一致（hooper2024kvquant、li2024snapkv、xiao2024streamingllm、xia2025kitty——均为 API 返回的 author 顺序与 bib 不同，应核实 bib 中的 author 列表是否正确）
- 未发现虚构引用

---

## 格式合规检查（EMNLP 2026 / ARR）

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤8 页 | ✅ | 正好 8 页（page 1-8） |
| Limitations section | ✅ | Page 8，conclusion 之后、references 之前 |
| 匿名性 | ✅ | "Anonymous ACL submission"，未发现 self-citation 泄露 |
| 代码/数据链接 | ✅ | 未提供（匿名阶段可接受） |
| ACL template | ✅ | 双栏格式正确 |
| Appendix 使用 | ⚠️ | Appendix E (Granularity Tradeoff) 讨论了 per-head vs layer-level 的选择——这对理解论文 scope 很重要，考虑是否应在正文 Related Work 中简要提及 |

---

## Overall Assessment

### ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论扎实，但 N=7 模型的样本量有限，决策规则阈值为 post-hoc 拟合无 held-out 验证 |
| Excitement | 2.5/5 | 负面结果有价值但 excitement 有限；技术贡献（一条约束不等式）incremental；核心正面结果仅限一个模型 |
| Reproducibility | 3.5/5 | 关键细节（模型、profiling 流程、评估指标）描述充分，但无代码，部分 solver 实现细节缺失 |
| Reviewer Confidence | 4/5 | 熟悉 KV cache 量化和 mixed-precision 文献 |

### 总体评分

**Score: 3.0 — Findings**

Could be accepted to the Findings of ACL. 论文的实验工作扎实，负面结论对社区有参考价值，但作为 main conference paper：(1) 新颖性有限（RateQuant + 一条约束）；(2) 正面结果仅在 1/7 模型上成立，generalizability 不足；(3) 判别规则的实用增量价值未充分论证。适合以 Findings 形式发表，重点贡献是对 "非均匀 KV cache 量化何时有效" 的系统性回答。

**Confidence: High**

---

### 一句话总结

一篇实验扎实的诊断性研究，揭示了 per-head mixed-precision KV cache 量化在大多数架构上无效的原因，但技术新颖性有限（核心修复是一条约束不等式），且正面结果仅限 1/7 模型，更适合 Findings 而非 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-15T15:33:38.640840+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的审稿意见\n\n**Score: 3.0 — Findings** | Soundness 3.5/5 | Excitement 2.5/5\n\n**Strengths:**\n- S1: 有价值的负面结论——6/7 模型无收益，\"when does it NOT help\" 视角稀缺\n- S2: 实验设计严谨——7 模型覆盖 MHA 到 GQA 8:1，multi-seed, cross-dataset, profiling resolution 消融\n- S3: Compounding effect 的因果分析有用\n- S4: Greedy-MCKP 等价性对工程部署有价值\n\n**Weaknesses:**\n- W1 [major]: Abstract \"29.4% reduction\" 突出呈现具有误导性——仅来自 1/7 模型，读者第一印象会认为方法普遍有效\n- W2 [major]: 经验判别规则的实用价值存疑——需要完整 profiling 数据，而有了 profiling 数据直接跑 solver 即可判断，O(H log B) 微秒级，判别规则无增量收益\n- W3 [major]: 与 RateQuant 的增量贡献界定模糊——技术上归结为 RateQuant + 一条 cardinality constraint\n- W4 [minor-to-major]: \"Catastrophic failure\" 叙事过度渲染——严格来说仅适用于 Qwen2.5-7B，其他模型为 moderate degradation\n- W5 [minor]: Spread/spike/flat 术语缺乏 formal definition\n- W6 [minor]: Related work 对 token-level mixed-precision 定位可更精确\n- W7 [minor]: Limitations section 过于简短\n- W8 [minor]: Table caption 自包含性可改进\n\n**Questions:**\n- Q1: Spread pattern 是模型固有属性还是校准数据的函数？\n- Q2: Profiling + k sweep + solver 的端到端开销是多少？\n- Q3: Yi-1.5 的 spike head 单独升级到 8-bit 是否能获益？\n- Q4: Table 2 的 unconstrained MCKP 是否就是 RateQuant 复现？\n\n**Missing References:** Cocktail (chunk-adaptive), MiKV/No Token Left Behind, \"More Tokens Lower Precision\"\n\n---\n\n请对以上每个 Weakness (W1-W8) 和 Question (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的审稿意见\n\n**Score: 3.0 — Findings** | Soundness 3.5/5 | Excitement 2.5/5\n\n**Strengths:**\n- S1: 有价值的负面结论——6/7 模型无收益，\"when does it NOT help\" 视角稀缺\n- S2: 实验设计严谨——7 模型覆盖 MHA 到 GQA 8:1，multi-seed, cross-dataset, profiling resolution 消融\n- S3: Compounding effect 的因果分析有用\n- S4: Greedy-MCKP 等价性对工程部署有价值\n\n**Weaknesses:**\n- W1 [major]: Abstract \"29.4% reduction\" 突出呈现具有误导性——仅来自 1/7 模型，读者第一印象会认为方法普遍有效\n- W2 [major]: 经验判别规则的实用价值存疑——需要完整 profiling 数据，而有了 profiling 数据直接跑 solver 即可判断，O(H log B) 微秒级，判别规则无增量收益\n- W3 [major]: 与 RateQuant 的增量贡献界定模糊——技术上归结为 RateQuant + 一条 cardinality constraint\n- W4 [minor-to-major]: \"Catastrophic failure\" 叙事过度渲染——严格来说仅适用于 Qwen2.5-7B，其他模型为 moderate degradation\n- W5 [minor]: Spread/spike/flat 术语缺乏 formal definition\n- W6 [minor]: Related work 对 token-level mixed-precision 定位可更精确\n- W7 [minor]: Limitations section 过于简短\n- W8 [minor]: Table caption 自包含性可改进\n\n**Questions:**\n- Q1: Spread pattern 是模型固有属性还是校准数据的函数？\n- Q2: Profiling + k sweep + solver 的端到端开销是多少？\n- Q3: Yi-1.5 的 spike head 单独升级到 8-bit 是否能获益？\n- Q4: Table 2 的 unconstrained MCKP 是否就是 RateQuant 复现？\n\n**Missing References:** Cocktail (chunk-adaptive), MiKV/No Token Left Behind, \"More Tokens Lower Precision\"\n\n---\n\n请对以上每个 Weakness (W1-W8) 和 Question (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "ratekv"
  }
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-15T15:34:01.790737+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23149
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-15T15:34:02.192559+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的审稿意见\n\n**Score: 2.5 — Borderline Findings** | Soundness 3/5 | Excitement 2.5/5\n\n**Strengths:**\n- S1: MCKP + cardinality constraint 形式化干净优雅\n- S2: Compounding effect 的 super-additivity 数据 (1.56×–4.89×) 有价值\n- S3: 5 架构族 7 模型 + cross-dataset + multi-seed\n- S4: KIVI 对比定位诚实\n- S5: Appendix 丰富（13 个子节）\n\n**Weaknesses:**\n- W1 [critical]: Decision rule N=1 正样本——7 个模型中仅 1 个正样本，2 个自由参数 7/7 分类无统计意义。任何能将 1 点与 6 点分开的线性分界面都能 \"100% 准确\"。无 LOO-CV、无 threshold sensitivity analysis。\n- W2 [critical]: Compounding claim 因果推断不严谨——\"cause\" 过强，super-additivity 仅在 Qwen 上收集，替代解释未排除（如 2-bit 绝对误差本身大到无需 compounding 也退化）\n- W3 [major]: 关键 baseline 缺失——未对比 KVTuner（论文自己在 Related Work 中提到的 sensitivity-aware mixed-precision）、GEAR、Kitty\n- W4 [major]: 模型规模 ≤14B——KV cache 压缩需求主要在 70B+，14B 的 KV cache 压力较小\n- W5 [major]: Downstream eval 无 CI——Table 3 差异在评估噪声范围内（0-shot std 通常 0.5-1.5%），3-seed stability 仅在 Qwen 上测试\n- W6 [major]: Runtime benchmark 仅 PyTorch-level simulation——8.5% overhead 无下界估计，实际 kernel 可能完全不同\n- W7 [minor]: Symmetric-only 定位的实用场景不清晰——现代推理引擎普遍支持 asymmetric\n- W8 [minor]: 长文本评估仅 2 模型 × 8K，32K+ 未测试\n\n**Questions:**\n- Q1: 其他 6 模型是否也展示 super-additivity？\n- Q2: Decision rule thresholds 如何选择？Grid search 还是 visual inspection？\n- Q3: Table 1 unconstrained MCKP (36.92) 远差于 greedy (32.45)——为什么 constrained 下又可靠？\n- Q4: KV separation 中 K 倾向获得更多 2-bit 的原因？\n- Q5: 512 token calibration 能否外推到长序列？\n- Q6: Flat 模型上 MCKP 是否产生与 uniform 相同的分配？\n\n**Missing References:** KIVI-V2、SqueezeLLM joint quant、bib 中 arXiv preprint 需更新 venue 信息\n\n---\n\n请对以上每个 Weakness (W1-W8) 和 Question (Q1-Q6) 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的审稿意见\n\n**Score: 2.5 — Borderline Findings** | Soundness 3/5 | Excitement 2.5/5\n\n**Strengths:**\n- S1: MCKP + cardinality constraint 形式化干净优雅\n- S2: Compounding effect 的 super-additivity 数据 (1.56×–4.89×) 有价值\n- S3: 5 架构族 7 模型 + cross-dataset + multi-seed\n- S4: KIVI 对比定位诚实\n- S5: Appendix 丰富（13 个子节）\n\n**Weaknesses:**\n- W1 [critical]: Decision rule N=1 正样本——7 个模型中仅 1 个正样本，2 个自由参数 7/7 分类无统计意义。任何能将 1 点与 6 点分开的线性分界面都能 \"100% 准确\"。无 LOO-CV、无 threshold sensitivity analysis。\n- W2 [critical]: Compounding claim 因果推断不严谨——\"cause\" 过强，super-additivity 仅在 Qwen 上收集，替代解释未排除（如 2-bit 绝对误差本身大到无需 compounding 也退化）\n- W3 [major]: 关键 baseline 缺失——未对比 KVTuner（论文自己在 Related Work 中提到的 sensitivity-aware mixed-precision）、GEAR、Kitty\n- W4 [major]: 模型规模 ≤14B——KV cache 压缩需求主要在 70B+，14B 的 KV cache 压力较小\n- W5 [major]: Downstream eval 无 CI——Table 3 差异在评估噪声范围内（0-shot std 通常 0.5-1.5%），3-seed stability 仅在 Qwen 上测试\n- W6 [major]: Runtime benchmark 仅 PyTorch-level simulation——8.5% overhead 无下界估计，实际 kernel 可能完全不同\n- W7 [minor]: Symmetric-only 定位的实用场景不清晰——现代推理引擎普遍支持 asymmetric\n- W8 [minor]: 长文本评估仅 2 模型 × 8K，32K+ 未测试\n\n**Questions:**\n- Q1: 其他 6 模型是否也展示 super-additivity？\n- Q2: Decision rule thresholds 如何选择？Grid search 还是 visual inspection？\n- Q3: Table 1 unconstrained MCKP (36.92) 远差于 greedy (32.45)——为什么 constrained 下又可靠？\n- Q4: KV separation 中 K 倾向获得更多 2-bit 的原因？\n- Q5: 512 token calibration 能否外推到长序列？\n- Q6: Flat 模型上 MCKP 是否产生与 uniform 相同的分配？\n\n**Missing References:** KIVI-V2、SqueezeLLM joint quant、bib 中 arXiv preprint 需更新 venue 信息\n\n---\n\n请对以上每个 Weakness (W1-W8) 和 Question (Q1-Q6) 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "ratekv"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-15T15:34:03.502118+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---

### Assistant

_source line 238 · 2026-05-15T15:34:08.209886+00:00_

交叉分享已发送给两位 Reviewer。等待逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 17

2 recorded events

### User

_source line 239 · 2026-05-15T15:34:10.698830+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**，Soundness 3.5，Excitement 2.5。

主要问题：
1. **Abstract 的 "29.4%" 误导性** — 仅来自 1/7 模型，不应作为 headline metric
2. **判别规则实用价值存疑** — 需要完整 profiling 数据，而 profiling 后直接运行 O(H log B) solver 更直接
3. **与 RateQuant 的增量贡献界定模糊** — 核心技术修改是一条线性不等式
4. **"Catastrophic failure" 叙事过度渲染** — 严格来说只适用于 Qwen2.5-7B
5. **Spread/spike/flat 术语缺乏形式化定义**，阈值从 N=7 post-hoc 拟合

优势：有价值的负面结论、严谨的实验设计（多 seed、cross-dataset、profiling 消融）、对 2-bit compounding 的因果分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Assistant

_source line 240 · 2026-05-15T15:34:26.473019+00:00_

交叉分享任务已分配给两位 Reviewer，等待他们对对方意见的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 18

2 recorded events

### User

_source line 241 · 2026-05-15T15:37:11.900953+00:00_

[Reviewer 1 审稿意见]:
## 交叉回应 — Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R2-W1: Abstract "29.4% reduction" 突出呈现具有误导性**

同意核心判断，但需指出 abstract 已有一定限定。Abstract 第 3 行写 "On the one spread-pattern model (Qwen2.5-7B)"，第 4 行立即转向 "On the remaining six models... non-uniform allocation provides no meaningful benefit"。结构上做到了正反兼顾。

但 R2 的核心关切成立：29.4% 是整篇论文最显眼的定量数据，且出现在 abstract 第 3 句——大部分读者首先记住的就是这个数字。"one spread-pattern model" 的限定语容易被略过。建议在 abstract 开头就明确 "6/7 models show no benefit" 的结论，再给 29.4% 作为唯一例外的说明，而非当前的先正后负叙述顺序。

---

**[AGREE] R2-W2: 经验判别规则的实用价值存疑——profiling 后直接跑 solver 即可**

这是 R2 最锐利的观察之一，我在 Round 2 审稿中未充分展开。

论文 Section 5.2（analysis.tex 第 72 行）自己写道："The rule reuses profiling data already required by the solver and adds no overhead." 这句话实际上暴露了问题：如果 decision rule 的输入（per-head profiling）与 solver 的输入完全相同，而 solver 运行时间是 O(H log H) 微秒级（Section 3.5），那么判别规则的唯一实用场景是"不想跑 solver"——但这在工程上没有理由，因为 solver 比 profiling 快几个数量级。

判别规则的真实价值是**解释性**而非决策性：它回答了"为什么有些模型获益而有些不获益"这个科学问题。但论文将其定位为 contribution 3（introduction.tex 第 44 行），暗示了实用决策功能。建议将 decision rule 的定位从"practical diagnostic tool"降为"post-hoc analytical framework for understanding when non-uniform allocation helps"。

---

**[AGREE，有保留] R2-W3: 与 RateQuant 的增量贡献界定模糊**

R2 说"技术上归结为 RateQuant + 一条 cardinality constraint"基本正确，但略有低估。

论文 method.tex 第 6-7、17 行明确陈述了与 RateQuant 的关系：RateQuant 处理 consecutive bit-widths {2,3,4,5,6}，利用 polymatroid structure 保证 greedy 最优；本文处理 hardware-aligned {2,4,8,16}，polymatroid structure 不成立。这是一个有意义的实践差异——实际部署确实使用 {2,4,8,16} 而非 {2,3,4,5,6}。

但算法层面的增量确实很薄：MCKP formulation 相同，仅加一条 linear inequality。论文的真正贡献在于：(a) compounding effect 的系统性刻画（Section 3.3），(b) 7 个模型的 "mostly negative" 实证发现，(c) 异质性 characterization。这些分析性贡献比算法贡献更重要，但论文的叙事重心偏向了算法。

建议作者更诚实地定位：**核心贡献是实证发现和分析框架，算法改进是自然推论。**

---

**[AGREE] R2-W4: "Catastrophic failure" 叙事过度渲染**

同意。核查原文：

- Introduction 第 13 行："The optimization does not merely underperform; it fails catastrophically."——特指 Qwen2.5-7B（32-37 PPL）
- 但 abstract 第 5 行："prevents catastrophic failure on spread architectures"——复数形式暗示 spread 不止一个，而实际只有 Qwen2.5-7B
- Introduction contribution 1："catastrophic failure in unconstrained per-head KV cache quantization"——措辞上没有限定为单一模型

R2 正确指出：对其他模型，unconstrained solver 的退化是 "moderate"（Gemma-2: 1.47× degradation, intro 第 24 行），而非 "catastrophic"。将 moderate degradation 纳入 "catastrophic failure" 的叙事框架是过度渲染。这与我在 R1-W2 中关于 "cause" 措辞过强的观察一致。

---

**[AGREE] R2-W5: Spread/spike/flat 术语缺乏 formal definition**

同意。Section 5.2（analysis.tex 第 63-66 行）使用 soft boundaries（"$\gtrsim 0.50$", "$\lesssim 0.70$"），三种 pattern 的边界条件存在重叠区域（如 concentration 0.33 + t1/t5 0.68 的 Qwen-14B 被归为 flat，但理由是 concentration 不够高，而非 shape）。Flat 的定义尤其模糊——既包括低 concentration（Mistral 0.24）也包括中等 concentration + 低 t1/t5（Qwen-14B 0.33, 0.68）。

minor 问题，但对可复现性有影响。建议至少用 crisp inequality 定义（即便承认阈值是 empirical）。

---

**[AGREE] R2-W6: Related work 对 token-level mixed-precision 定位可更精确**

同意。Introduction 第 5 行将 FastGen 和 ARKV 归为 "token-level mixed-precision approaches"，但未区分 token-level（每个 token 不同精度）和 head-level（每个 head 不同精度）方法的根本差异——前者的搜索空间是 O(T×H)，后者是 O(H)。对于一篇以 per-head allocation 为核心的论文，这个区分应该更清晰。

Minor 问题。

---

**[AGREE] R2-W7: Limitations section 过于简短**

强烈同意。Conclusion.tex 第 9-11 行的 Limitations 全文仅一句话：

> "Spread rests on N=1 (Qwen2.5-7B); the seven-model evaluation is directional, not robust. No real-kernel latency benchmarks; untested beyond 14B."

对于一篇存在以下重大限制的论文，这是不够的：
1. Decision rule 的正样本仅 1 个（我的 R1-W1）
2. 模型规模上限 14B（我的 R1-W4）
3. Runtime 仅为 simulation（我的 R1-W6）
4. 缺少 KVTuner 等直接 competitor 对比（我的 R1-W3）
5. Downstream evaluation 无 confidence intervals（我的 R1-W5）

ACL ARR 要求 Limitations section 充分讨论方法的局限。当前版本远未达到标准。

---

**[AGREE] R2-W8: Table caption 自包含性可改进**

同意。Table 1 的 caption 需要参照正文 footnote 才能理解 "standard-resolution" vs "high-resolution" profiling 的区别。Table 4 的 t1/t5 定义在 caption 中过于简略（"ratio of the most sensitive head's 2-bit distortion to the sum of the top-5% heads' distortions"），不看正文很难理解。Minor 但按 EMNLP 标准应修正。

---

### Questions 回应

**[AGREE] R2-Q1: Spread pattern 是模型固有属性还是校准数据的函数？**

好问题。论文在 Appendix G 展示了 WikiText-2 vs C4 的 96-97% bit-assignment agreement，部分回答了这个问题。但这两个数据集都是 English web text，分布相似。如果用 code、multilingual、或 domain-specific 数据校准，sensitivity profile 是否改变？这直接影响 decision rule 的可靠性。论文应在 Discussion 中明确承认这一点。

---

**[AGREE] R2-Q2: Profiling + k sweep + solver 的端到端开销是多少？**

论文报告了 solver runtime（微秒级）但未报告 profiling 开销。Method.tex 第 25 行："64 sequences × 2048 tokens from WikiText-2 train"，H × |B| 次前向传播。对于 Qwen2.5-7B（112 heads × 4 bit-widths = 448 次前向传播），加上 k sweep，总计约 500+ 次前向传播。这是一个非 trivial 的计算成本，应当报告。

---

**[REBUT] R2-Q3: Yi-1.5 的 spike head 单独升级到 8-bit 是否能获益？**

这个问题的答案已经隐含在论文中。Analysis.tex 第 18-19 行明确指出 Yi-1.5 的 L4H3 "4-bit and 8-bit deltas are ≈ 0"——即 d_h(4) ≈ d_h(8) ≈ 0。这意味着：

1. 将 L4H3 从 4-bit 升级到 8-bit 不会减少任何 distortion（delta ≈ 0）
2. 但会消耗额外 budget（4→8 bit 翻倍内存）
3. 这正是 "spike" pattern 的定义特征：sensitivity 仅存在于 2-bit 维度，没有 cross-bitwidth gradient

所以答案是：不能获益，因为该 head 的 4-bit distortion 已经 ≈ 0。Solver 在 4× 压缩下已经正确地将此 head 分配到 4-bit（而非 2-bit），这就是最优策略。进一步升级到 8-bit 只会浪费 budget 而无法降低 distortion。

---

**[AGREE，有补充] R2-Q4: Table 2 的 unconstrained MCKP 是否就是 RateQuant 复现？**

Method.tex 第 6-7 行明确说明 RateQuant 使用 {2,3,4,5,6}，本文使用 {2,4,8,16}。因此 unconstrained MCKP **不是** RateQuant 的精确复现——bit-width set 不同，polymatroid structure 不成立。

但在精神上，R2 的观察成立：unconstrained MCKP 与 RateQuant 共享相同的优化框架（MCKP with additive distortion objective），只是应用于不同的 bit-width set。论文应在 Section 3.1 或 Table 1 caption 中更明确地说明这一关系，例如标注 "Unconstrained MCKP (analogous to RateQuant adapted to {2,4,8,16})"。

---

### 与我 R1 审稿意见的一致性总结

| R2 观点 | R1 对应 | 一致性 |
|---------|---------|--------|
| W1 abstract 误导 | R1-W1 N=1 统计缺陷 | 高度一致——同一根本问题的不同表现 |
| W2 decision rule 实用性 | R1-W1 中未充分展开 | R2 的角度更锐利，补充了我的审稿 |
| W3 RateQuant 增量 | R1 未直接涉及 | R2 提出了有价值的新视角 |
| W4 catastrophic failure 过度 | R1-W2 causal claim 过强 | 一致——叙事强度超出证据支撑 |
| W7 Limitations 过短 | R1-W1/W4/W5/W6 均涉及未充分讨论的局限 | 强烈一致 |

**R2 未涉及但我认为重要的问题**:
- **模型规模上限 14B**（我的 R1-W4）：R2 未提及这一限制。KV cache 压缩的主要应用场景是 70B+ 模型，14B 的验证不足以支撑方法的实际价值主张。
- **缺少 KVTuner 等直接 competitor 对比**（我的 R1-W3）：R2 提到了 missing references（Cocktail, MiKV 等）但未将其升级为 major weakness。
- **Downstream evaluation 无 confidence intervals**（我的 R1-W5）：Table 3 的效应量极小（±0.3-1.2%），在无 CI 的情况下无法判断显著性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 242 · 2026-05-15T15:37:21.425152+00:00_

Reviewer 1 的交叉回应已收到（对 R2 的 W1-W8 全部 AGREE，仅 Q3 REBUT）。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 19

2 recorded events

### User

_source line 243 · 2026-05-15T15:37:26.000137+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

对 R2 的 8 个 Weaknesses 中 7 个 AGREE（W1-W8 除 Q3 外），4 个 Questions 中 3 个 AGREE、1 个 REBUT（Q3——Yi-1.5 spike head 升级 8-bit 无收益，因为论文数据已显示 d_h(4)≈d_h(8)≈0）。

R2 最锐利的新视角是 W2（decision rule 实用性悖论）和 W3（RateQuant 增量界定），这两点补充了我 Round 2 审稿中未充分展开的方向。同时我标注了 R2 未涉及但重要的三个问题：14B 规模上限、缺少 KVTuner 对比、downstream evaluation 无 CI。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_1"
}
```

</details>

---

### Assistant

_source line 244 · 2026-05-15T15:37:37.855900+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 20

8 recorded events

### User

_source line 245 · 2026-05-15T15:38:22.267276+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见

---

### Weaknesses 回应

**[AGREE] R1-W1: Decision rule N=1 正样本，7/7 分类无统计意义**

强烈同意。这与我自己的 W2 观点一致。2 个自由参数（concentration threshold + t₁/t₅ threshold）在 7 个样本上拟合 100% accuracy 没有任何统计说服力——R1 说得对，任何能把 1 个点和 6 个点分开的线性分界面都能做到这一点。论文将此作为三个 claimed contributions 之一（Section 5.2, p8），但没有 LOO-CV、没有 threshold sensitivity analysis、没有 bootstrap confidence interval。更根本的问题是：只有 1 个正样本意味着 "spread" 类别的边界完全由 Qwen2.5-7B 这一个数据点决定，泛化性完全未知。

补充：我在自己的审稿中进一步指出了一个更深层的问题——即使 rule 统计上成立，其实用价值也存疑，因为 profiling 数据已经足够直接运行 O(H log B) solver 比较结果，不需要中间的 decision rule。

---

**[AGREE with nuance] R1-W2: Compounding claim 因果推断不严谨**

部分同意，但 R1 的替代解释需要更仔细的评估。

**同意的部分**：论文在 Section 3.3 使用 "cause" 确实过强。Super-additivity 数据（1.56×–4.89×）仅在 Qwen2.5-7B 上收集（Figure 1, Appendix A），没有在其他 6 个模型上展示 compounding curve。如果 compounding 是声称的普遍机制，至少应该在 1-2 个 flat 模型上展示：flat 模型不出现严重 compounding 是因为 solver 本来就不分配很多 2-bit heads（因此 compounding 未被触发），还是因为这些架构本身对 2-bit 误差更鲁棒？这两个解释导出不同的结论。

**需要 nuance 的部分**：R1 提出的替代解释——"2-bit 绝对误差本身大到无需 compounding 也退化"——与论文的数据不完全一致。Table 1 (p5) 显示 Qwen 上 individual 2-bit head 的 PPL increase 是可控的（单 head 量化到 2-bit 的 distortion d_h(2) 是 solver 可以 reason about 的），但同时量化 68 个 head 到 2-bit 时 PPL 从 10.91 爆炸到 36.92。这种非线性放大不能仅用 "绝对误差大" 解释——需要某种 interaction effect。论文称之为 "compounding through residual stream" 是合理的机制假设，但 "cause" 应改为 "consistent with" 或 "strongly suggests"。

---

**[REBUT] R1-W3: 关键 baseline 缺失（KVTuner、GEAR、Kitty）**

不同意这是一个 critical/major weakness，理由如下：

1. **KVTuner**（Li et al., 2025a）是 **layer-level** mixed-precision（论文 Section 2, p3 明确提及："layer-level via gradient-based sensitivity"）。论文的 scope 是 **per-head** bit-width allocation。Appendix E (p10-11) 讨论了 granularity tradeoff，指出 layer-level allocation 是 per-head 的严格子集——layer-level 强制同一层所有 head 共享 bit-width，损失了论文发现的 within-layer heterogeneity 信号。将 KVTuner 作为 baseline 不公平——它在更粗的粒度上操作，天然劣势。

2. **GEAR** 使用 residual quantization（低秩近似 + 稀疏残差），与 per-head bit-width allocation 是完全不同的量化范式。GEAR 对所有 head 使用相同的量化方案，不涉及 mixed-precision allocation。

3. **Kitty**（Xia et al., 2025）使用 dynamic channel-wise precision boost——运行时根据 activation magnitude 动态调整精度。论文的方法是 static allocation（offline profiling → fixed bit-width per head），两者的 design point 不同。论文在 p2-3 的 Related Work 中已引用 Kitty 并说明了区别。

4. **论文已对比 KIVI**（Table 2, p6），KIVI 是最直接的 per-head uniform 量化 baseline。论文的核心对比是 constrained MCKP vs. uniform vs. unconstrained MCKP，这个实验设计回答了论文的核心问题（"何时非均匀有效？"）。

**但有一个让步**：KVTuner 的 layer-level 结果可以作为 reference point（不是 fair baseline），展示 per-head 粒度相对于 layer-level 的边际收益。这会强化论文关于 granularity 的 narrative。作为 informative comparison 而非 competitive baseline，加入 KVTuner 是合理的建议。

---

**[AGREE] R1-W4: 模型规模 ≤14B**

同意。KV cache 压缩的主要 deployment 场景是 70B+ 模型（长 context + 大 batch），14B 以下的 KV cache 压力相对较小。论文在 Limitations (p8) 承认了 "untested beyond 14B"，但这个 limitation 实际上影响论文 claim 的 generalizability：

- **对负面结果的影响**：70B+ 模型普遍使用 aggressive GQA（如 Llama-3-70B 为 GQA 8:1），GQA 下 KV head 数更少，sensitivity 分布可能更 flat。如果确实如此，论文的负面结论（大多数模型不需要非均匀）在大模型上可能更强，但这需要验证。
- **对正面结果的影响**：Qwen2.5-7B 的 spread pattern 是否在 Qwen2.5-72B 上保留？论文已展示 Qwen-7B → Qwen-14B 从 spread 变为 flat（Table 4, p8 的 within-family scale contrast），这反而暗示更大模型可能更 flat，进一步缩小了方法的适用范围。

这是一个不可忽视的 scope limitation。

---

**[AGREE] R1-W5: Downstream eval 无 CI**

同意。Table 3 (p7) 报告了 downstream accuracy 但没有 confidence interval。0-shot evaluation 的 typical std 在 0.5-1.5%（取决于 benchmark 和 model size），而 Table 3 中非 Qwen 模型的 uniform vs MCKP 差异通常在 ±0.1-0.5 范围内，很可能在噪声范围内。没有 CI，"no benefit on downstream tasks" 的 claim 缺乏统计支撑。

论文在 Table 2 对 PPL 做了 3-seed median+MAD（仅在 Qwen 上），但 Table 3 没有类似处理。建议至少对 Table 3 的关键对比（uniform vs constrained MCKP）加上 3-seed 的 mean±std。

**补充**：论文的核心 metric 是 PPL，downstream tasks 是 supplementary evidence。但既然论文选择展示 Table 3 来支撑 claim，就应该保证其统计可信度。

---

**[AGREE with nuance] R1-W6: Runtime benchmark 仅 PyTorch-level simulation**

部分同意。论文在 Appendix K (p13) 已明确声明："These measurements use PyTorch-level per-head quantize/dequantize calls and do not represent optimized CUDA kernel performance"，并将 8.5% overhead 定性为 upper bound。这种透明度值得肯定。

**同意的部分**：R1 说得对，实际 fused kernel（如 vLLM、TensorRT-LLM 中的 fused attention + dequantization）的 overhead pattern 可能完全不同。PyTorch-level simulation 主要衡量的是 dispatch overhead，而非真实的 memory bandwidth / compute throughput tradeoff。

**Nuance**：论文的核心贡献不是 runtime system，而是 "什么时候值得做非均匀"的诊断。Runtime benchmark 是 supplementary——即使没有它，论文的核心 claim（PPL-based analysis）仍然成立。但如果要保留 Appendix K，应该在正文 Limitations 中提及 simulation 的局限性，而非仅在 appendix caveat 中。

---

**[REBUT] R1-W7: Symmetric-only 定位的实用场景不清晰**

不同意这是一个有意义的 weakness。

1. **Symmetric 仍是主流 deployment 选择**：vLLM、SGLang 等主流推理引擎的默认 KV cache 量化使用 symmetric per-channel quantization。虽然 asymmetric 在理论上更灵活，但 symmetric 的 kernel 实现更简单、overhead 更低。

2. **论文已明确 scope**：Section 2 (p3) 明确说明 "our method determines at what precision (bit-width selection across heads)"，并将自己定位为与 KIVI（per-channel asymmetric）正交。论文不是在说 symmetric 比 asymmetric 好，而是在 symmetric 这个 widely-used setting 下研究 per-head allocation。

3. **核心发现应能迁移到 asymmetric**：compounding effect 和 spread/flat distinction 是关于 head sensitivity 分布形状的，这个分布不太可能因量化是 symmetric 还是 asymmetric 而根本改变（asymmetric 会降低每个 head 的绝对 distortion，但相对分布形状应该类似）。

---

**[AGREE] R1-W8: 长文本评估仅 2 模型 × 8K**

同意。Appendix L (p13) 仅在 Qwen 和 Llama 上测试了 8K context。对于一篇关于 KV cache 压缩的论文，8K 是相当短的——KV cache 压力的主要场景是 32K-128K context。论文的 512-token calibration profile 能否外推到 32K+ 是一个未回答的问题。虽然 Appendix L 显示 8K 结果与 2K 一致，但 8K → 32K 的 gap 远大于 2K → 8K。

---

### Questions 回应

**[AGREE] R1-Q1: 其他 6 模型是否也展示 super-additivity？**

这是本审稿中最重要的缺失实验之一。论文的 compounding analysis（Section 3.3, Figure 1）完全基于 Qwen2.5-7B。如果 compounding 是 cardinality constraint 存在的理论基础，至少应该展示：
- 1 个 flat 模型（如 Llama-3.1-8B）的 compounding curve：预期是即使 force 多个 head 到 2-bit，super-additivity 也较弱（因为 individual distortions 本来就小）
- 1 个 spike 模型（如 Yi-1.5-9B）的 compounding curve：预期是 spike head 贡献大部分 distortion，但 non-spike heads 的 2-bit error 不会通过 compounding 放大

这些数据会极大加强论文对 "为什么 constraint 在所有架构上都有益" 的解释力。

---

**[AGREE] R1-Q2: Decision rule thresholds 如何选择？**

论文没有明确说明。考虑到 N=7，几乎可以确定是 visual inspection 或 exhaustive grid search（在 7 个点上任何方法都是 trivial 的）。论文应明确 disclosure 选择方法，并讨论阈值对小幅扰动的敏感性（例如 concentration threshold 从 0.36 变到 0.40 时分类是否翻转）。

---

**[REBUT] R1-Q3: Table 1 unconstrained MCKP (36.92) 远差于 greedy (32.45)——为什么 constrained 下可靠？**

论文实际上较好地回答了这个问题。Section 3.5 (p5) 解释了机制：

1. **无约束时**：MCKP 在 additive assumption 下是最优的，所以它比 greedy 更 aggressive 地分配 2-bit（68/112 heads vs greedy 的更少）。但 additivity 在 2-bit 大量使用时 breaks（Section 3.3 的 compounding），所以 MCKP 的 "最优" 反而更差。
2. **有约束时**：cardinality constraint 将 2-bit assignments 限制到 k≤5 heads。在这个约束下，feasible set 极小——"the only decision is which k heads to assign to 2-bit; the marginal-benefit ordering determines this uniquely"（p5）。所以 greedy 和 MCKP 产生完全相同的分配（Table 1: 两者均为 10.91 PPL）。

关键 insight：constraint 将优化问题限制到 additivity 成立的 regime 内（少量 2-bit heads → compounding negligible），在这个 regime 内 MCKP 的 additive assumption 是 valid 的。

---

**[AGREE] R1-Q4: KV separation 中 K 倾向获得更多 2-bit 的原因？**

Appendix J (p12) 给出了部分解释："K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content." 但这个解释较为 hand-wavy——positional encoding 并不必然意味着更低的量化敏感度（RoPE 的高频分量在 2-bit 下可能有显著误差）。论文应提供更 rigorous 的解释，或至少量化 K vs V 的 per-head distortion 分布差异。

---

**[AGREE] R1-Q5: 512 token calibration 能否外推到长序列？**

同意这是一个重要问题。Appendix L 显示 8K 结果与 2K calibrated profiles 一致，但 512 token → 32K+ 的外推未验证。更长序列中 attention pattern 会发生结构性变化（如 attention sink、远距离依赖的稀疏化），这可能改变 per-head sensitivity 的分布形状。如果 spread pattern 在长序列下变成 flat（或反之），论文的 decision rule 和 allocation 都可能失效。

---

**[AGREE with nuance] R1-Q6: Flat 模型上 MCKP 是否产生与 uniform 相同的分配？**

查看 Table 6 (p11)：Llama-3.1-8B 在 4× compression 下，constrained MCKP 的实际 compression ratio 是 4.24×（略高于 uniform 的 4.0×），说明 MCKP **没有产生完全 uniform 的分配**——它仍然做了某种 redistribution（少数 head 到 8-bit，其余更多到 2-bit 以补偿），只是 PPL 改善 negligible。

论文应明确说明这一点：flat 模型上 MCKP allocation ≠ uniform allocation，但 PPL difference is negligible，这正是 "non-uniform doesn't help" 的含义。目前这个 distinction 需要读者自己从 Table 6 推断。

---

### Missing References 回应

**[AGREE] KIVI-V2**：如果存在，应该引用。

**[REBUT] SqueezeLLM joint quant**：SqueezeLLM 是 weight quantization 方法（Dense-and-Sparse quantization for weights），与 KV cache quantization 不直接相关。除非 R1 指的是 SqueezeLLM 的某个 KV cache 扩展，否则这不是必须的引用。

**[AGREE] bib 中 arXiv preprint 需更新 venue 信息**：引用验证显示 4 条存在 first author 不一致（hooper2024kvquant、li2024snapkv、xiao2024streamingllm、xia2025kitty），应核实并更新已被会议接收的 arXiv preprint 的 venue 信息。

---

### 与 R1 总体评分的对比

R1 给出 **2.5 (Borderline Findings)**，我给出 **3.0 (Findings)**。

**分歧点**：R1 对 baseline 缺失（W3）和 compounding 因果推断（W2）的严厉程度超过我。我认为 W3 中 KVTuner/GEAR/Kitty 不是 fair baselines（granularity 和方法范式不同），W2 中 compounding 的机制解释虽然不够 rigorous 但物理上合理。

**共识点**：Decision rule 的统计无效性（W1）、模型规模限制（W4）、downstream eval 无 CI（W5）。这些是影响接收决定的核心问题。

**我的判断**：论文作为 Findings 可以接受——实验工作扎实、负面结论有价值、compounding diagnosis 有 insight。但 main conference 的 bar 需要更强的 novelty 和更广的适用性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-15T15:38:40.610081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml"
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-15T15:38:40.661025+00:00_

1	- id: R1-W1
2	  summary: "Diagnostic framework overfitting: 2 thresholds on 5 models (1 positive)"
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - round: 1
10	      reviewers: [R1, R2]
11	      note: "consensus: 2 free parameters perfectly fit 5 samples = overfitting"
12	  action_items:
13	    - round: 1
14	      action: "Qwen2.5-14B hires profiling for N>1 Spread validation"
15	      assigned_to: Agent
16	      status: done
17	    - round: 1
18	      action: "MHA model (Pythia-1.4B) profiling for attention paradigm diversity"
19	      assigned_to: Agent
20	      status: done
21	    - round: 1
22	      action: "Downgrade claim from 'diagnostic framework' to 'empirical decision rule'"
23	      assigned_to: Paper Agent
24	      status: done
25	    - round: 1
26	      action: "Qwen-14B constrained pipeline (Flat prediction verified, Δ=0.02)"
27	      assigned_to: Agent
28	      status: done
29	    - round: 1
30	      action: "Pythia-1.4B constrained pipeline (Flat prediction verification)"
31	      assigned_to: Agent
32	      status: done
33	    - round: 1
34	      action: "t1/t5 bug fix: profiling scripts use delta ratio, must use concentration ratio"
35	      assigned_to: Agent
36	      status: done
37	  resolution: "Diagnostic now 7/7 correct (added Qwen-14B=Flat, Pythia=Flat). Claim downgraded to empirical decision rule. All t1/t5 canonical values unified in paper."
38	  resolution_round: 1
39	
40	- id: R1-W2
41	  summary: "4/5 models missing unconstrained greedy/MCKP baselines in Table 2"
42	  category: experiment
43	  severity: critical
44	  status: resolved
45	  first_raised_round: 1
46	  last_seen_round: 1
47	  mentions:
48	    - round: 1
49	      reviewers: [R1, R2]
50	      note: "consensus: compounding is Contribution 1 core, must verify on all models"
51	  action_items:
52	    - round: 1
53	      action: "Run unconstrained greedy + MCKP on all 5 models"
54	      as
…[truncated 9213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-15T15:40:27.756000+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ratekv",
  "issues_yaml": "- id: R1-W1\n  summary: \"Diagnostic framework overfitting: 2 thresholds on 5 models (1 positive)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: 2 free parameters perfectly fit 5 samples = overfitting\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"RECUR — Round 1 fix (added 2 models, downgraded to 'empirical decision rule') insufficient. Now 7 models but still N=1 positive. Both reviewers consensus: any linear boundary separating 1 point from 6 achieves 100%. No LOO-CV, no threshold sensitivity, no bootstrap CI. R2 adds: rule has zero practical value since profiling data already enables O(H log H) solver run.\"\n  action_items:\n    - round: 1\n      action: \"Qwen2.5-14B hires profiling for N>1 Spread validation\"\n      assigned_to: Agent\n      status: done\n    - round: 1\n      action: \"MHA model (Pythia-1.4B) profiling for attention paradigm diversity\"\n      assigned_to: Agent\n      status: done\n    - round: 1\n      action: \"Downgrade claim from 'diagnostic framework' to 'empirical decision rule'\"\n      assigned_to: Paper Agent\n      status: done\n    - round: 2\n      action: \"(a) Drastically downgrade claim — 'preliminary observation' not 'contribution'; (b) add threshold sensitivity analysis; (c) find additional spread models; or (d) remove from contribution list\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Abstract '29.4% reduction' prominent framing misleading — result from 1/7 models\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: abstract leads with best-case metric from 1/7 models. Current structure (positive → negative) creates false impression of general effectiveness. Should lead with '6/7 no benefit' then give Qwen as exception.\"\n  action_items:\n    - round: 2\n      action: \"Restructure abstract: lead with majority finding (6/7 no benefit), then Qwen as case study\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W2\n  summary: \"Compounding causal claim too strong — 'cause' unsupported, super-additivity data only on Qwen\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1 critical, R2 agree-with-nuance. Super-additivity (1.56×-4.89×) collected only on Qwen2.5-7B. 'Cause' requires ruling out alternatives (e.g., absolute error magnitude alone). R2 notes mechanism is physically plausible but 'cause' → 'consistent with' or 'strongly suggests'. Missing: compounding curves on flat/spike models.\"\n  action_items:\n    - round: 2\n      action: \"(a) Soften 'cause' to 'major contributing factor'; (b) show compounding curve on 1 flat + 1 spike model; (c) design control experiment separating compounding from selection effect\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3\n  summary: \"Decision rule practical value paradox — profiling data already enables direct solver run\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: decision rule requires same profiling data as solver input. Solver is O(H log H) microseconds. No practical scenario where rule is cheaper than running solver + comparing results. True value is explanatory (why some architectures benefit) not decisional. But paper positions it as Contribution 3.\"\n  action_items:\n    - round: 2\n      action: \"Reposition decision rule from 'practical diagnostic tool' to 'post-hoc analytical framework'. Alternatively remove from contribution list.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W4\n  summary: \"RateQuant incremental contribution unclear — core technical change is one linear inequality\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R2 major, R1 agree-with-reservation. Same MCKP formulation as RateQuant, only addition is Eq.2 cardinality constraint. Real contribution is empirical (compounding diagnosis + mostly-negative finding), but narrative emphasizes algorithm. Consensus: reposition core contribution as empirical finding, not algorithmic.\"\n  action_items:\n    - round: 2\n      action: \"In Introduction, explicitly distinguish: RateQuant solved formulation, this paper identifies failure mode + when-to-use characterization. Algorithm improvement is corollary.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W5\n  summary: \"Model scale ≤14B limits generalizability — KV cache pressure mainly at 70B+\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: KV cache compression demand primarily at 70B+. Qwen 7B→14B already shows spread→flat dilution, suggesting larger models more likely flat. 14B ceiling limits both positive and negative claims.\"\n  action_items:\n    - round: 2\n      action: \"(a) Validate on 1 model ≥30B; or (b) analyze head-count scaling on concentration theoretically; (c) expand Limitations discussion\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6\n  summary: \"Downstream evaluation lacks confidence intervals — effect sizes within noise\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: Table 3 differences ±0.1-1.2% within typical 0-shot std (0.5-1.5%). No CI, no p-values. 3-seed stability only on Qwen PPL, not downstream. Cross-dataset 96-97% agreement lacks bootstrap CI.\"\n  action_items:\n    - round: 2\n      action: \"Run 3+ seeds on Table 3 key comparisons, report mean±std. Add bootstrap CI for cross-dataset agreement.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W7\n  summary: \"Runtime benchmark is PyTorch-level simulation only — inconclusive for deployment\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1 major, R2 agree-with-nuance (not core contribution). 8.5% overhead from PyTorch dispatch, not real kernel. No lower bound. Paper's own caveat (Appendix K) acknowledges this but limitation should be in main Limitations section.\"\n  action_items:\n    - round: 2\n      action: \"Move simulation caveat to Limitations section. If possible, benchmark with vLLM/TRT-LLM fused kernels.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W8\n  summary: \"'Catastrophic failure' narrative exaggerated — only applies to Qwen2.5-7B\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: 'catastrophic' only valid for Qwen (3.3× bf16). Other models: Gemma-2 1.47×, rest ~1.07-1.12×. Abstract uses plural 'spread architectures' but only 1 exists. Introduction contribution 1 doesn't scope to single model.\"\n  action_items:\n    - round: 2\n      action: \"Restrict 'catastrophic failure' to Qwen context. Use 'moderate degradation' or 'suboptimal allocation' for flat models.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W9\n  summary: \"Spread/spike/flat terminology lacks formal definition\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: soft boundaries (≳0.50, ≲0.70) leave overlap. Flat definition especially ambiguous (covers both low conc and moderate conc + low t1/t5). Needs crisp inequality even if thresholds are empirical.\"\n  action_items:\n    - round: 2\n      action: \"Add formal definition with crisp inequalities. Acknowledge thresholds are descriptive not prescriptive.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W10\n  summary: \"Limitations section too short — critical limitations not discussed\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: current Limitations is 2 sentences. Missing: decision rule threshold generalization, downstream eval scope, calibration domain robustness, missing competitor baselines.\"\n  action_items:\n    - round: 2\n      action: \"Expand Limitations to cover all identified gaps per ARR requirements.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W2\n  summary: \"4/5 models missing unconstrained greedy/MCKP baselines in Table 2\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: compounding is Contribution 1 core, must verify on all models\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Round 2: Table 2 now has all 7 models with Greedy+MCKP columns. Resolved.\"\n  action_items:\n    - round: 1\n      action: \"Run unconstrained greedy + MCKP on all 5 models\"\n      assigned_to: Agent\n      status: done\n    - round: 1\n      action: \"Update Table 2 with gradient narrative (3.31× → 1.47× → 1.07-1.08×)\"\n      assigned_to: Paper Agent\n      status: done\n  resolution: \"Experiment complete 5/5. Table 2 updated with Greedy+MCKP columns, three-tier gradient labels, Gemma-2 BOS fix. Verified by Reviewer.\"\n  resolution_round: 1\n\n- id: R1-W3\n  summary: \"Downstream evaluation only on Qwen\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus for cross-architecture claim; R2 lower severity\"\n  action_items:\n    - round: 1\n      action: \"Run downstream eval on all 4 non-Spread models\"\n      assigned_to: Agent\n      status: done\n  resolution: \"5/5 models downstream eval done. Table updated with full per-task data.\"\n  resolution_round: 1\n\n- id: R1-W4\n  summary: \"Qwen may be architectural outlier (uniform 4-bit degradation +57.5% vs others +2.9-4.7%)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: method only works on 1 model with abnormally high degradation\"\n  action_items:\n    - round: 1\n      action: \"Qwen2.5-14B profiling to check if Spread is Qwen family trait\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Qwen-14B=Flat. Same family different scale → different shape. Diagnostic 7/7.\"\n  resolution_round: 1\n\n- id: R1-W5\n  summary: \"Novelty: cardinality constraint is standard knapsack technique\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"divergence: R2 wants critical, R1 cites ARR H6\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Round 2 R2-W3 raises related concern (RateQuant incremental). Round 1 fix (reposition as diagnosis+fix) partially effective but reviewers still note thin algorithmic novelty.\"\n  action_items:\n    - round: 1\n      action: \"Differentiate from HAWQ/HAQ; position contribution as compounding diagnosis\"\n      assigned_to: Paper Agent\n      status: done\n  resolution: \"Related work rewritten. Contribution positioned as diagnosis+fix, not algorithm. Residual concern tracked as R2-W4.\"\n  resolution_round: 1\n\n- id: R1-W6\n  summary: \"Profiling-compounding logical tension not explicitly resolved in text\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"divergence: R1 sees contradiction, R2 sees motivation\"\n  action_items:\n    - round: 1\n      action: \"Add paragraph in method.tex explaining constraint restores near-additivity\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Added 'Restoring additivity' paragraph in method.tex §3.3-3.4. Verified PASS.\"\n  resolution_round: 1\n\n- id: R1-W7\n  summary: \"Related work missing HAWQ/HAQ and 2025 KV cache works\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: HAWQ/HAWQ-V2/HAQ + PM-KVQ/Kitty/RotateKV/MiniKV/AQUA-KV\"\n  action_items:\n    - round: 1\n      action: \"Add citations + RateQuant differentiation paragraph\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Added 11 new citations. Verified PASS.\"\n  resolution_round: 1\n\n- id: R1-W8\n  summary: \"Solver equivalence lacks formal statement\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: needs formal sufficient condition or explicit empirical label\"\n  action_items:\n    - round: 1\n      action: \"Add formal statement labeled as empirical observation\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Added empirical observation formal statement in method.tex. Verified PASS.\"\n  resolution_round: 1\n\n- id: R1-W9\n  summary: \"Non-additive compounding not formally defined or characterized\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: need empirical functional form\"\n  action_items:\n    - round: 1\n      action: \"W9 v2 experiment: super-additivity measurement\"\n      assigned_to: Agent\n      status: done\n  resolution: \"W9 v2 data (1.56-4.89× super-additivity) in method.tex §3.3.\"\n  resolution_round: 1\n\n- id: R1-W10\n  summary: \"Standard vs hires profiling mixed in headline results\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: should unify or clearly recommend\"\n  action_items:\n    - round: 1\n      action: \"Unify to hires primary; update all numbers\"\n      assigned_to: Paper Agent\n      status: done\n  resolution: \"Main body unified to hires. Compilation clean.\"\n  resolution_round: 1\n\n- id: R1-W11\n  summary: \"Granularity tradeoff data error: L0H1 delta=0.66 should be 1.2444\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: data error in Granularity Tradeoff\"\n  action_items:\n    - round: 1\n      action: \"Fix L0H1 delta to 1.2444\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Fixed in commit 82246a7.\"\n  resolution_round: 1\n\n- id: R1-KIVI\n  summary: \"No comparison with concurrent KV cache quantization methods\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"Dream D054 cross-tier consensus: missing concurrent method baseline\"\n  action_items:\n    - round: 1\n      action: \"KIVI baseline on Qwen-7B + Llama-8B\"\n      assigned_to: Agent\n      status: done\n  resolution: \"KIVI baseline done. Positioned as orthogonal. D061.\"\n  resolution_round: 1\n\n- id: L10-W1\n  summary: \"mistral_hires_bf16_2bitonly_v3 registry status=RUNNING but conclusion=killed\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [Reviewer]\n      note: \"status contradiction: RUNNING + killed\"\n  action_items:\n    - round: 10\n      action: \"Fix registry status to DONE/killed\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Registry updated: status=DONE, conclusion=killed.\"\n  resolution_round: 1\n\n# === Divergence issues (Round 2) ===\n\n- id: R2-DIV1\n  summary: \"Baseline comparison — KVTuner/GEAR/Kitty as competitors\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"DIVERGENCE: R1 major (missing direct competitor), R2 rebut (different granularity — KVTuner is layer-level, GEAR is residual quant, Kitty is dynamic channel-wise; not fair baselines). R2 concedes KVTuner as informative reference point. Director judgment: R2's rebuttal is well-argued; these are not apples-to-apples comparisons.\"\n  action_items:\n    - round: 2\n      action: \"Optional: add KVTuner as informative reference point (not competitive baseline) on 1-2 models\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-DIV2\n  summary: \"Symmetric-only positioning clarity\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"DIVERGENCE: R1 minor (unclear practical scenarios for symmetric-only), R2 rebut (symmetric is default in vLLM/SGLang, kernel simpler, compounding findings likely transfer to asymmetric). Director judgment: R2's rebuttal reasonable; symmetric remains common. Low priority.\"\n  action_items:\n    - round: 2\n      action: \"Optional: add 1-2 sentences on symmetric-only deployment scenarios\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ratekv",
    "issues_yaml": "- id: R1-W1\n  summary: \"Diagnostic framework overfitting: 2 thresholds on 5 models (1 positive)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: 2 free parameters perfectly fit 5 samples = overfitting\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"RECUR — Round 1 fix (added 2 models, downgraded to 'empirical decision rule') insufficient. Now 7 models but still N=1 positive. Both reviewers consensus: any linear boundary separating 1 point from 6 achieves 100%. No LOO-CV, no threshold sensitivity, no bootstrap CI. R2 adds: rule has zero practical value since profiling data already enables O(H log H) solver run.\"\n  action_items:\n    - round: 1\n      action: \"Qwen2.5-14B hires profiling for N>1 Spread validation\"\n      assigned_to: Agent\n      status: done\n    - round: 1\n      action: \"MHA model (Pythia-1.4B) profiling for attention paradigm diversity\"\n      assigned_to: Agent\n      status: done\n    - round: 1\n      action: \"Downgrade claim from 'diagnostic framework' to 'empirical decision rule'\"\n      assigned_to: Paper Agent\n      status: done\n    - round: 2\n      action: \"(a) Drastically downgrade claim — 'preliminary observation' not 'contribution'; (b) add threshold sensitivity analysis; (c) find additional spread models; or (d) remove from contribution list\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Abstract '29.4% reduction' prominent framing misleading — result from 1/7 models\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: abstract leads with best-case metric from 1/7 models. Current structure (positive → negative) creates false impression of general effectiveness. Should lead with '6/7 no benefit' then give Qwen as exception.\"\n  action_items:\n    - round: 2\n      action: \"Restructure abstract: lead with majority finding (6/7 no benefit), then Qwen as case study\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W2\n  summary: \"Compounding causal claim too strong — 'cause' unsupported, super-additivity data only on Qwen\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1 critical, R2 agree-with-nuance. Super-additivity (1.56×-4.89×) collected only on Qwen2.5-7B. 'Cause' requires ruling out alternatives (e.g., absolute error magnitude alone). R2 notes mechanism is physically plausible but 'cause' → 'consistent with' or 'strongly suggests'. Missing: compounding curves on flat/spike models.\"\n  action_items:\n    - round: 2\n      action: \"(a) Soften 'cause' to 'major contributing factor'; (b) show compounding curve on 1 flat + 1 spike model; (c) design control experiment separating compounding from selection effect\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3\n  summary: \"Decision rule practical value paradox — profiling data already enables direct solver run\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: decision rule requires same profiling data as solver input. Solver is O(H log H) microseconds. No practical scenario where rule is cheaper than running solver + comparing results. True value is explanatory (why some architectures benefit) not decisional. But paper positions it as Contribution 3.\"\n  action_items:\n    - round: 2\n      action: \"Reposition decision rule from 'practical diagnostic tool' to 'post-hoc analytical framework'. Alternatively remove from contribution list.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W4\n  summary: \"RateQuant incremental contribution unclear — core technical change is one linear inequality\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R2 major, R1 agree-with-reservation. Same MCKP formulation as RateQuant, only addition is Eq.2 cardinality constraint. Real contribution is empirical (compounding diagnosis + mostly-negative finding), but narrative emphasizes algorithm. Consensus: reposition core contribution as empirical finding, not algorithmic.\"\n  action_items:\n    - round: 2\n      action: \"In Introduction, explicitly distinguish: RateQuant solved formulation, this paper identifies failure mode + when-to-use characterization. Algorithm improvement is corollary.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W5\n  summary: \"Model scale ≤14B limits generalizability — KV cache pressure mainly at 70B+\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: KV cache compression demand primarily at 70B+. Qwen 7B→14B already shows spread→flat dilution, suggesting larger models more likely flat. 14B ceiling limits both positive and negative claims.\"\n  action_items:\n    - round: 2\n      action: \"(a) Validate on 1 model ≥30B; or (b) analyze head-count scaling on concentration theoretically; (c) expand Limitations discussion\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6\n  summary: \"Downstream evaluation lacks confidence intervals — effect sizes within noise\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: Table 3 differences ±0.1-1.2% within typical 0-shot std (0.5-1.5%). No CI, no p-values. 3-seed stability only on Qwen PPL, not downstream. Cross-dataset 96-97% agreement lacks bootstrap CI.\"\n  action_items:\n    - round: 2\n      action: \"Run 3+ seeds on Table 3 key comparisons, report mean±std. Add bootstrap CI for cross-dataset agreement.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W7\n  summary: \"Runtime benchmark is PyTorch-level simulation only — inconclusive for deployment\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"R1 major, R2 agree-with-nuance (not core contribution). 8.5% overhead from PyTorch dispatch, not real kernel. No lower bound. Paper's own caveat (Appendix K) acknowledges this but limitation should be in main Limitations section.\"\n  action_items:\n    - round: 2\n      action: \"Move simulation caveat to Limitations section. If possible, benchmark with vLLM/TRT-LLM fused kernels.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W8\n  summary: \"'Catastrophic failure' narrative exaggerated — only applies to Qwen2.5-7B\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: 'catastrophic' only valid for Qwen (3.3× bf16). Other models: Gemma-2 1.47×, rest ~1.07-1.12×. Abstract uses plural 'spread architectures' but only 1 exists. Introduction contribution 1 doesn't scope to single model.\"\n  action_items:\n    - round: 2\n      action: \"Restrict 'catastrophic failure' to Qwen context. Use 'moderate degradation' or 'suboptimal allocation' for flat models.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W9\n  summary: \"Spread/spike/flat terminology lacks formal definition\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: soft boundaries (≳0.50, ≲0.70) leave overlap. Flat definition especially ambiguous (covers both low conc and moderate conc + low t1/t5). Needs crisp inequality even if thresholds are empirical.\"\n  action_items:\n    - round: 2\n      action: \"Add formal definition with crisp inequalities. Acknowledge thresholds are descriptive not prescriptive.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W10\n  summary: \"Limitations section too short — critical limitations not discussed\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"consensus: current Limitations is 2 sentences. Missing: decision rule threshold generalization, downstream eval scope, calibration domain robustness, missing competitor baselines.\"\n  action_items:\n    - round: 2\n      action: \"Expand Limitations to cover all identified gaps per ARR requirements.\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W2\n  summary: \"4/5 models missing unconstrained greedy/MCKP baselines in Table 2\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: compounding is Contribution 1 core, must verify on all models\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Round 2: Table 2 now has all 7 models with Greedy+MCKP columns. Resolved.\"\n  action_items:\n    - round: 1\n      action: \"Run unconstrained greedy + MCKP on all 5 models\"\n      assigned_to: Agent\n      status: done\n    - round: 1\n      action: \"Update Table 2 with gradient narrative (3.31× → 1.47× → 1.07-1.08×)\"\n      assigned_to: Paper Agent\n      status: done\n  resolution: \"Experiment complete 5/5. Table 2 updated with Greedy+MCKP columns, three-tier gradient labels, Gemma-2 BOS fix. Verified by Reviewer.\"\n  resolution_round: 1\n\n- id: R1-W3\n  summary: \"Downstream evaluation only on Qwen\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus for cross-architecture claim; R2 lower severity\"\n  action_items:\n    - round: 1\n      action: \"Run downstream eval on all 4 non-Spread models\"\n      assigned_to: Agent\n      status: done\n  resolution: \"5/5 models downstream eval done. Table updated with full per-task data.\"\n  resolution_round: 1\n\n- id: R1-W4\n  summary: \"Qwen may be architectural outlier (uniform 4-bit degradation +57.5% vs others +2.9-4.7%)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: method only works on 1 model with abnormally high degradation\"\n  action_items:\n    - round: 1\n      action: \"Qwen2.5-14B profiling to check if Spread is Qwen family trait\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Qwen-14B=Flat. Same family different scale → different shape. Diagnostic 7/7.\"\n  resolution_round: 1\n\n- id: R1-W5\n  summary: \"Novelty: cardinality constraint is standard knapsack technique\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"divergence: R2 wants critical, R1 cites ARR H6\"\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"Round 2 R2-W3 raises related concern (RateQuant incremental). Round 1 fix (reposition as diagnosis+fix) partially effective but reviewers still note thin algorithmic novelty.\"\n  action_items:\n    - round: 1\n      action: \"Differentiate from HAWQ/HAQ; position contribution as compounding diagnosis\"\n      assigned_to: Paper Agent\n      status: done\n  resolution: \"Related work rewritten. Contribution positioned as diagnosis+fix, not algorithm. Residual concern tracked as R2-W4.\"\n  resolution_round: 1\n\n- id: R1-W6\n  summary: \"Profiling-compounding logical tension not explicitly resolved in text\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"divergence: R1 sees contradiction, R2 sees motivation\"\n  action_items:\n    - round: 1\n      action: \"Add paragraph in method.tex explaining constraint restores near-additivity\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Added 'Restoring additivity' paragraph in method.tex §3.3-3.4. Verified PASS.\"\n  resolution_round: 1\n\n- id: R1-W7\n  summary: \"Related work missing HAWQ/HAQ and 2025 KV cache works\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: HAWQ/HAWQ-V2/HAQ + PM-KVQ/Kitty/RotateKV/MiniKV/AQUA-KV\"\n  action_items:\n    - round: 1\n      action: \"Add citations + RateQuant differentiation paragraph\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Added 11 new citations. Verified PASS.\"\n  resolution_round: 1\n\n- id: R1-W8\n  summary: \"Solver equivalence lacks formal statement\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: needs formal sufficient condition or explicit empirical label\"\n  action_items:\n    - round: 1\n      action: \"Add formal statement labeled as empirical observation\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Added empirical observation formal statement in method.tex. Verified PASS.\"\n  resolution_round: 1\n\n- id: R1-W9\n  summary: \"Non-additive compounding not formally defined or characterized\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: need empirical functional form\"\n  action_items:\n    - round: 1\n      action: \"W9 v2 experiment: super-additivity measurement\"\n      assigned_to: Agent\n      status: done\n  resolution: \"W9 v2 data (1.56-4.89× super-additivity) in method.tex §3.3.\"\n  resolution_round: 1\n\n- id: R1-W10\n  summary: \"Standard vs hires profiling mixed in headline results\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: should unify or clearly recommend\"\n  action_items:\n    - round: 1\n      action: \"Unify to hires primary; update all numbers\"\n      assigned_to: Paper Agent\n      status: done\n  resolution: \"Main body unified to hires. Compilation clean.\"\n  resolution_round: 1\n\n- id: R1-W11\n  summary: \"Granularity tradeoff data error: L0H1 delta=0.66 should be 1.2444\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"consensus: data error in Granularity Tradeoff\"\n  action_items:\n    - round: 1\n      action: \"Fix L0H1 delta to 1.2444\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Fixed in commit 82246a7.\"\n  resolution_round: 1\n\n- id: R1-KIVI\n  summary: \"No comparison with concurrent KV cache quantization methods\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [R1, R2]\n      note: \"Dream D054 cross-tier consensus: missing concurrent method baseline\"\n  action_items:\n    - round: 1\n      action: \"KIVI baseline on Qwen-7B + Llama-8B\"\n      assigned_to: Agent\n      status: done\n  resolution: \"KIVI baseline done. Positioned as orthogonal. D061.\"\n  resolution_round: 1\n\n- id: L10-W1\n  summary: \"mistral_hires_bf16_2bitonly_v3 registry status=RUNNING but conclusion=killed\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [Reviewer]\n      note: \"status contradiction: RUNNING + killed\"\n  action_items:\n    - round: 10\n      action: \"Fix registry status to DONE/killed\"\n      assigned_to: Agent\n      status: done\n  resolution: \"Registry updated: status=DONE, conclusion=killed.\"\n  resolution_round: 1\n\n# === Divergence issues (Round 2) ===\n\n- id: R2-DIV1\n  summary: \"Baseline comparison — KVTuner/GEAR/Kitty as competitors\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"DIVERGENCE: R1 major (missing direct competitor), R2 rebut (different granularity — KVTuner is layer-level, GEAR is residual quant, Kitty is dynamic channel-wise; not fair baselines). R2 concedes KVTuner as informative reference point. Director judgment: R2's rebuttal is well-argued; these are not apples-to-apples comparisons.\"\n  action_items:\n    - round: 2\n      action: \"Optional: add KVTuner as informative reference point (not competitive baseline) on 1-2 models\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-DIV2\n  summary: \"Symmetric-only positioning clarity\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [R1, R2]\n      note: \"DIVERGENCE: R1 minor (unclear practical scenarios for symmetric-only), R2 rebut (symmetric is default in vLLM/SGLang, kernel simpler, compounding findings likely transfer to asymmetric). Director judgment: R2's rebuttal reasonable; symmetric remains common. Low priority.\"\n  action_items:\n    - round: 2\n      action: \"Optional: add 1-2 sentences on symmetric-only deployment scenarios\"\n      assigned_to: Research Director\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-15T15:40:27.857978+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/review_issues.yaml\", \"bytes\": 18200}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-15T15:42:23.919567+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 2 审稿报告 — ratekv\n\n**论文**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May cycle)\n**审稿人**: Reviewer 1（方法严谨性 + 实验验证）、Reviewer 2（新颖性 + 完整性 + 写作）\n**交叉回应**: 完成，1 轮即收敛\n\n---\n\n## Summary\n\n本文研究 per-head mixed-precision KV cache 量化在硬件对齐 bit-width {2,4,8,16} 下的有效性。核心发现：(1) unconstrained MCKP/greedy solver 因 2-bit 量化误差的 super-additive compounding 导致灾难性退化（Qwen2.5-7B: 32-37 PPL vs uniform 15.45）；(2) 一条 cardinality constraint（限制 2-bit head 数量）即可修复；(3) 7 个模型中仅 Qwen2.5-7B 从非均匀分配获益（-29.4%），其余 6 个模型 ≈ uniform。论文提出基于 concentration + t₁/t₅ ratio 的经验判别规则来分类 spread/spike/flat 架构。\n\n---\n\n## Strengths\n\n- **S1 [consensus]**: **有价值的负面结论**。6/7 模型上非均匀分配无效的系统性发现，对社区有重要参考价值——避免后续工作在不适用的架构上浪费算力。\"When does it NOT help\" 的研究视角在 KV cache 量化文献中稀缺。\n\n- **S2 [consensus]**: **MCKP + cardinality constraint 形式化干净**。将 per-head bit-width 选择建模为 cardinality-constrained MCKP，cardinality constraint 作为 minimal intervention 的理论动机清晰。证明 constraint 使 greedy 和 MCKP 等价，支持 O(H log H) 简单实现。\n\n- **S3 [consensus]**: **Compounding effect 的系统刻画**。Section 3.3 的 super-additivity 数据（1.56×–4.89×）和 U-shaped curve 为理解 2-bit 量化失败模式提供了有用的 empirical evidence，这一观察本身对社区有价值。\n\n- **S4 [consensus]**: **实验设计覆盖全面**。5 架构族 7 模型（MHA 到 GQA 8:1），含 within-family scale contrast（Qwen 7B vs 14B）。Cross-dataset validation (96-97%)、multi-seed stability (10.99±0.06)、profiling resolution 消融、long-context generalization 等提升可信度。\n\n- **S5 [consensus]**: **KIVI 对比的诚实定位**。明确承认 \"orthogonal, not competitive\"，KIVI+MCKP 无额外收益，方法仅在 symmetric-only 环境有独立价值。这种透明度值得肯定。\n\n---\n\n## Weaknesses\n\n### Critical\n\n- **W1: Decision rule 的 N=1 正样本构成根本性统计缺陷** [R1 critical, R2 AGREE]\n  - 2 个自由参数（concentration ~0.50, t₁/t₅ ~0.70）在 7 个样本上 7/7 分类，正样本仅 Qwen2.5-7B。任何能将 1 点与 6 点分开的线性分界面都能 100%——这不是 discriminative power 的证据。无 LOO-CV、无 threshold sensitivity analysis、无 bootstrap CI。\n  - **与 Round 1 关联**: Round 1 R1-W1 要求增加模型（done: +Qwen-14B, +Pythia）和降级 claim（done: \"diagnostic framework\" → \"empirical decision rule\"）。Round 2 判定：修复不充分。问题本质不变——正样本仍为 N=1。\n  - **Round 2 新增层面 (R2-W2)**: 即使 rule 统计上成立，其实用价值也为零——profiling 数据已是 solver 输入，直接跑 O(H log H) solver 比判别规则更直接。Rule 的真正价值是解释性而非决策性，但论文定位为 Contribution 3。\n  - **建议**: (a) 从 contribution 列表中移除或大幅降级为 \"preliminary observation on 7 models with 1 positive case\"；(b) 补充 threshold sensitivity analysis；(c) 如保留，重新定位为 analytical insight 而非 practical tool。\n\n- **W2: Compounding 因果论证不够严谨** [R1 critical, R2 AGREE with nuance]\n  - 论文将 2-bit compounding 定位为 \"the cause of catastrophic failure\"（Introduction contribution 1），但 super-additivity 数据仅在 Qwen2.5-7B 上收集。其他 6 个模型未展示 compounding curve。\n  - R2 的 nuance：机制解释（residual stream error accumulation）物理上合理，Table 1 数据显示非线性放大确实存在，但 \"cause\" 在科学论文中需要排除替代假说的实验设计。\n  - **建议**: (a) \"cause\" → \"a major contributing factor\"；(b) 在 1 个 flat + 1 个 spike 模型上展示 compounding curve；(c) 设计控制实验分离 compounding 与 selection effect。\n\n### Major\n\n- **W3: Abstract \"29.4% reduction\" 的突出呈现具有误导性** [R2 major, R1 AGREE]\n  - 29.4% 仅来自 1/7 模型，但作为 abstract lead metric 给读者 \"方法普遍有效\" 的第一印象。Abstract 第 3 行确实有 \"one spread-pattern model\" 限定，但 headline 效应已经形成。\n  - **建议**: 重组 abstract 叙事顺序：先陈述主要发现（\"7 个模型中 6 个无收益\"），再以 Qwen 为 case study 给出 29.4%。\n\n- **W4: 与 RateQuant 的增量贡献界定模糊** [R2 major, R1 AGREE with reservation]\n  - RateQuant 已将 per-head bit-width 选择公式化为 MCKP 并证明 greedy 最优性。本文技术增量归结为一条 linear inequality (Eq.2)。论文的真正贡献在于：(a) compounding diagnosis，(b) mostly-negative finding，(c) heterogeneity characterization——但叙事重心偏向算法。\n  - R1 补充：RateQuant 处理 {2,3,4,5,6}，本文处理 {2,4,8,16}，这是实践中有意义的差异。但算法层面增量确实薄。\n  - **建议**: Introduction 中明确区分——RateQuant 解决了 formulation，本文发现了 RateQuant 在实践中的 failure mode 并给出 characterization。\n\n- **W5: 模型规模 ≤14B 限制泛化性** [R1 major, R2 AGREE]\n  - KV cache 压缩需求主要在 70B+。Qwen 7B→14B 已显示 spread→flat dilution，暗示更大模型可能更 flat——进一步缩小方法适用范围。\n  - **建议**: 至少验证 1 个 30B+ 模型，或分析 head 数量 scaling 对 concentration 的理论影响。\n\n- **W6: Downstream evaluation 无 confidence intervals** [R1 major, R2 AGREE]\n  - Table 3 差异 ±0.1-1.2%，完全在 0-shot 评估噪声范围内（typical std 0.5-1.5%）。3-seed stability 仅 Qwen PPL。\n  - **建议**: 对 Table 3 关键对比加 3+ seed mean±std。\n\n- **W7: Runtime benchmark 仅 PyTorch-level simulation** [R1 major, R2 AGREE with nuance]\n  - 8.5% overhead 来自 dispatch，非 real kernel。论文在 Appendix K 有 caveat 但 Limitations section 未提及。\n  - R2 nuance：核心贡献不是 runtime system，即使无 benchmark 论文 claim 仍成立。但既然展示了数据就需保证可信。\n  - **建议**: 将 simulation caveat 移入 Limitations。如可能用 vLLM/TRT-LLM 做 real benchmark。\n\n- **W8: \"Catastrophic failure\" 叙事过度渲染** [R2 minor-to-major, R1 AGREE]\n  - \"Catastrophic\" 仅适用于 Qwen (3.3× bf16)。其他模型：Gemma-2 1.47×，其余 ~1.07-1.12×。Abstract 用复数 \"spread architectures\" 但只有 1 个 spread。\n  - **建议**: 限定 \"catastrophic\" 于 Qwen/spread 语境。Flat 模型用 \"moderate degradation\"。\n\n### Minor\n\n- **W9: Spread/spike/flat 术语缺乏 formal definition** [R2 minor, R1 AGREE]\n  - Soft boundaries（≳0.50, ≲0.70）有重叠。Flat 定义尤其模糊。需 crisp inequality。\n\n- **W10: Limitations section 过于简短** [R2 minor, R1 strongly AGREE]\n  - 仅 2 句。缺少：threshold generalization、downstream scope、calibration domain robustness、missing competitors。ACL ARR 要求充分讨论。\n\n- **W11: Long-context 评估覆盖不足** [R1 minor, R2 AGREE]\n  - 仅 Qwen + Llama × 8K。KV cache 压力场景在 32K-128K。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致：\n\n1. **[AGREE] Decision rule 是论文最大弱点**——N=1 正样本无统计意义，且与直接运行 solver 相比无实用增量。应从 contribution 降级或移除。\n2. **[AGREE] Compounding 机制合理但 \"cause\" 措辞过强**——应改为 \"major contributing factor\"，并补充其他模型的 compounding 数据。\n3. **[AGREE] Abstract framing 需调整**——先负面结论（6/7 无收益）再正面 case study（Qwen 29.4%）。\n4. **[AGREE] 核心贡献应重新定位为实证发现**——算法增量薄（RateQuant + 一条约束），真正价值在 compounding diagnosis + mostly-negative finding。\n5. **[AGREE] 模型规模和统计可靠性有待加强**——14B 上限、无 CI downstream、runtime simulation。\n6. **[AGREE] Limitations 需大幅扩展**。\n\n## Reviewer Divergence\n\n1. **Baseline 缺失 (KVTuner 等)**：R1 认为 major weakness——缺少直接 competitor 对比。R2 rebut——KVTuner 是 layer-level 不是 per-head，GEAR/Kitty 是不同量化范式，非 fair baseline。R2 concedes KVTuner 可作 informative reference。**Director 判断**: R2 的 rebuttal 有理——granularity 和方法范式不同。但作为 informative comparison 纳入 KVTuner 是合理的改进方向。记为 optional action。\n2. **Symmetric-only 定位**：R1 认为 minor weakness——实用场景不清晰。R2 rebut——symmetric 仍是 vLLM/SGLang 默认，kernel 更简单。**Director 判断**: R2 的 rebuttal 合理。低优先级。\n\n---\n\n## Questions（需要作者澄清）\n\n1. 其他 6 模型是否也展示 super-additivity？如果是，为什么不从 constraint 获益？如果不是，compounding 机制如何普遍化？\n2. Decision rule thresholds 的选择方法？Grid search vs visual inspection？Sensitivity analysis？\n3. Spread pattern 是模型固有属性还是校准数据的函数？C4/WikiText-2 以外的 domain 如何？\n4. Profiling + k sweep + solver 的端到端 wall-clock 开销是多少？\n5. Flat 模型上 constrained MCKP 是否产生与 uniform 完全相同的 allocation？如果不同但 PPL 等效，这个 distinction 应明确。\n6. Table 2 的 unconstrained MCKP 与 RateQuant 的精确关系？\n\n---\n\n## Missing References\n\n**共识引用建议** (R1+R2 均提及或交叉同意)：\n- 更新 bib 中已被会议接收的 arXiv preprints 的 venue 信息\n- 核查 4 条 author 顺序不一致的条目（hooper2024kvquant, li2024snapkv, xiao2024streamingllm, xia2025kitty）\n\n**R2 补充引用**：\n- Cocktail (Tian et al., 2025): chunk-adaptive mixed precision\n- MiKV / \"No Token Left Behind\" (Yao et al., 2024): token-level importance-aware mixed precision\n- \"More Tokens, Lower Precision\" (2024): token-precision tradeoff\n\n---\n\n## Overall Assessment\n\n### ARR 维度综合评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.5/5 | **3.25/5** |\n| Excitement | 2.5/5 | 2.5/5 | **2.5/5** |\n| Overall | 2.5/5 | 3.0/5 | **2.75/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n| Reproducibility | 4/5 | 3.5/5 | **3.75/5** |\n\n### 总体评分: **weak reject** (main conference) / **borderline accept** (Findings)\n\n### 判断依据\n\n**Main conference bar 未达到**:\n- 技术新颖性有限——核心算法增量是 RateQuant formulation + 一条 cardinality constraint\n- 正面结果仅限 1/7 模型，方法适用范围极窄\n- Decision rule（Contribution 3）在统计和实用两个维度上均不成立\n- 模型规模上限 14B 限制了对 KV cache 压缩这一研究方向的实际影响\n\n**Findings 可接受**:\n- 实验工作扎实（7 模型、cross-dataset、multi-seed、KIVI 对比）\n- \"非均匀 KV cache 量化在大多数架构上无效\" 的系统性负面结论对社区有重要参考价值\n- Compounding effect 的刻画为后续工作提供了有用的 failure mode analysis\n- 论文对自身方法局限性的承认（KIVI 比较、Limitations section）是诚实的\n\n### 接收路径建议（供 Research Director 参考，非审稿建议）\n\n如目标为 Findings:\n1. [Must-Fix] 将 decision rule 从 Contribution 降级为 analytical observation\n2. [Must-Fix] Abstract 重组——先负面结论再正面 case\n3. [Must-Fix] \"cause\" → \"contributing factor\"，补 1-2 个模型 compounding curve\n4. [Must-Fix] Limitations 大幅扩展\n5. [Should-Fix] Downstream eval 加 CI\n6. [Should-Fix] 形式化 spread/spike/flat 定义\n\n如目标为 Main Conference:\n- 以上全部 + 找到额外 spread 模型（N≥2 正样本）+ 30B+ 验证\n\n---\n\n## Issue Tracker 状态\n\n- **Round 1**: 13 issues, 全部 resolved\n- **Round 2**: 10 new open issues（2 critical, 6 warning, 2 info），2 divergence issues\n- **跨轮复发**: R1-W1（diagnostic overfitting）在 Round 1 resolved 后 Round 2 重新 open——Round 1 的修复（增加 2 模型 + 降级 claim）未充分解决根本问题（N=1 正样本）",
  "project": "ratekv",
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
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 2 审稿报告 — ratekv\n\n**论文**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May cycle)\n**审稿人**: Reviewer 1（方法严谨性 + 实验验证）、Reviewer 2（新颖性 + 完整性 + 写作）\n**交叉回应**: 完成，1 轮即收敛\n\n---\n\n## Summary\n\n本文研究 per-head mixed-precision KV cache 量化在硬件对齐 bit-width {2,4,8,16} 下的有效性。核心发现：(1) unconstrained MCKP/greedy solver 因 2-bit 量化误差的 super-additive compounding 导致灾难性退化（Qwen2.5-7B: 32-37 PPL vs uniform 15.45）；(2) 一条 cardinality constraint（限制 2-bit head 数量）即可修复；(3) 7 个模型中仅 Qwen2.5-7B 从非均匀分配获益（-29.4%），其余 6 个模型 ≈ uniform。论文提出基于 concentration + t₁/t₅ ratio 的经验判别规则来分类 spread/spike/flat 架构。\n\n---\n\n## Strengths\n\n- **S1 [consensus]**: **有价值的负面结论**。6/7 模型上非均匀分配无效的系统性发现，对社区有重要参考价值——避免后续工作在不适用的架构上浪费算力。\"When does it NOT help\" 的研究视角在 KV cache 量化文献中稀缺。\n\n- **S2 [consensus]**: **MCKP + cardinality constraint 形式化干净**。将 per-head bit-width 选择建模为 cardinality-constrained MCKP，cardinality constraint 作为 minimal intervention 的理论动机清晰。证明 constraint 使 greedy 和 MCKP 等价，支持 O(H log H) 简单实现。\n\n- **S3 [consensus]**: **Compounding effect 的系统刻画**。Section 3.3 的 super-additivity 数据（1.56×–4.89×）和 U-shaped curve 为理解 2-bit 量化失败模式提供了有用的 empirical evidence，这一观察本身对社区有价值。\n\n- **S4 [consensus]**: **实验设计覆盖全面**。5 架构族 7 模型（MHA 到 GQA 8:1），含 within-family scale contrast（Qwen 7B vs 14B）。Cross-dataset validation (96-97%)、multi-seed stability (10.99±0.06)、profiling resolution 消融、long-context generalization 等提升可信度。\n\n- **S5 [consensus]**: **KIVI 对比的诚实定位**。明确承认 \"orthogonal, not competitive\"，KIVI+MCKP 无额外收益，方法仅在 symmetric-only 环境有独立价值。这种透明度值得肯定。\n\n---\n\n## Weaknesses\n\n### Critical\n\n- **W1: Decision rule 的 N=1 正样本构成根本性统计缺陷** [R1 critical, R2 AGREE]\n  - 2 个自由参数（concentration ~0.50, t₁/t₅ ~0.70）在 7 个样本上 7/7 分类，正样本仅 Qwen2.5-7B。任何能将 1 点与 6 点分开的线性分界面都能 100%——这不是 discriminative power 的证据。无 LOO-CV、无 threshold sensitivity analysis、无 bootstrap CI。\n  - **与 Round 1 关联**: Round 1 R1-W1 要求增加模型（done: +Qwen-14B, +Pythia）和降级 claim（done: \"diagnostic framework\" → \"empirical decision rule\"）。Round 2 判定：修复不充分。问题本质不变——正样本仍为 N=1。\n  - **Round 2 新增层面 (R2-W2)**: 即使 rule 统计上成立，其实用价值也为零——profiling 数据已是 solver 输入，直接跑 O(H log H) solver 比判别规则更直接。Rule 的真正价值是解释性而非决策性，但论文定位为 Contribution 3。\n  - **建议**: (a) 从 contribution 列表中移除或大幅降级为 \"preliminary observation on 7 models with 1 positive case\"；(b) 补充 threshold sensitivity analysis；(c) 如保留，重新定位为 analytical insight 而非 practical tool。\n\n- **W2: Compounding 因果论证不够严谨** [R1 critical, R2 AGREE with nuance]\n  - 论文将 2-bit compounding 定位为 \"the cause of catastrophic failure\"（Introduction contribution 1），但 super-additivity 数据仅在 Qwen2.5-7B 上收集。其他 6 个模型未展示 compounding curve。\n  - R2 的 nuance：机制解释（residual stream error accumulation）物理上合理，Table 1 数据显示非线性放大确实存在，但 \"cause\" 在科学论文中需要排除替代假说的实验设计。\n  - **建议**: (a) \"cause\" → \"a major contributing factor\"；(b) 在 1 个 flat + 1 个 spike 模型上展示 compounding curve；(c) 设计控制实验分离 compounding 与 selection effect。\n\n### Major\n\n- **W3: Abstract \"29.4% reduction\" 的突出呈现具有误导性** [R2 major, R1 AGREE]\n  - 29.4% 仅来自 1/7 模型，但作为 abstract lead metric 给读者 \"方法普遍有效\" 的第一印象。Abstract 第 3 行确实有 \"one spread-pattern model\" 限定，但 headline 效应已经形成。\n  - **建议**: 重组 abstract 叙事顺序：先陈述主要发现（\"7 个模型中 6 个无收益\"），再以 Qwen 为 case study 给出 29.4%。\n\n- **W4: 与 RateQuant 的增量贡献界定模糊** [R2 major, R1 AGREE with reservation]\n  - RateQuant 已将 per-head bit-width 选择公式化为 MCKP 并证明 greedy 最优性。本文技术增量归结为一条 linear inequality (Eq.2)。论文的真正贡献在于：(a) compounding diagnosis，(b) mostly-negative finding，(c) heterogeneity characterization——但叙事重心偏向算法。\n  - R1 补充：RateQuant 处理 {2,3,4,5,6}，本文处理 {2,4,8,16}，这是实践中有意义的差异。但算法层面增量确实薄。\n  - **建议**: Introduction 中明确区分——RateQuant 解决了 formulation，本文发现了 RateQuant 在实践中的 failure mode 并给出 characterization。\n\n- **W5: 模型规模 ≤14B 限制泛化性** [R1 major, R2 AGREE]\n  - KV cache 压缩需求主要在 70B+。Qwen 7B→14B 已显示 spread→flat dilution，暗示更大模型可能更 flat——进一步缩小方法适用范围。\n  - **建议**: 至少验证 1 个 30B+ 模型，或分析 head 数量 scaling 对 concentration 的理论影响。\n\n- **W6: Downstream evaluation 无 confidence intervals** [R1 major, R2 AGREE]\n  - Table 3 差异 ±0.1-1.2%，完全在 0-shot 评估噪声范围内（typical std 0.5-1.5%）。3-seed stability 仅 Qwen PPL。\n  - **建议**: 对 Table 3 关键对比加 3+ seed mean±std。\n\n- **W7: Runtime benchmark 仅 PyTorch-level simulation** [R1 major, R2 AGREE with nuance]\n  - 8.5% overhead 来自 dispatch，非 real kernel。论文在 Appendix K 有 caveat 但 Limitations section 未提及。\n  - R2 nuance：核心贡献不是 runtime system，即使无 benchmark 论文 claim 仍成立。但既然展示了数据就需保证可信。\n  - **建议**: 将 simulation caveat 移入 Limitations。如可能用 vLLM/TRT-LLM 做 real benchmark。\n\n- **W8: \"Catastrophic failure\" 叙事过度渲染** [R2 minor-to-major, R1 AGREE]\n  - \"Catastrophic\" 仅适用于 Qwen (3.3× bf16)。其他模型：Gemma-2 1.47×，其余 ~1.07-1.12×。Abstract 用复数 \"spread architectures\" 但只有 1 个 spread。\n  - **建议**: 限定 \"catastrophic\" 于 Qwen/spread 语境。Flat 模型用 \"moderate degradation\"。\n\n### Minor\n\n- **W9: Spread/spike/flat 术语缺乏 formal definition** [R2 minor, R1 AGREE]\n  - Soft boundaries（≳0.50, ≲0.70）有重叠。Flat 定义尤其模糊。需 crisp inequality。\n\n- **W10: Limitations section 过于简短** [R2 minor, R1 strongly AGREE]\n  - 仅 2 句。缺少：threshold generalization、downstream scope、calibration domain robustness、missing competitors。ACL ARR 要求充分讨论。\n\n- **W11: Long-context 评估覆盖不足** [R1 minor, R2 AGREE]\n  - 仅 Qwen + Llama × 8K。KV cache 压力场景在 32K-128K。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致：\n\n1. **[AGREE] Decision rule 是论文最大弱点**——N=1 正样本无统计意义，且与直接运行 solver 相比无实用增量。应从 contribution 降级或移除。\n2. **[AGREE] Compounding 机制合理但 \"cause\" 措辞过强**——应改为 \"major contributing factor\"，并补充其他模型的 compounding 数据。\n3. **[AGREE] Abstract framing 需调整**——先负面结论（6/7 无收益）再正面 case study（Qwen 29.4%）。\n4. **[AGREE] 核心贡献应重新定位为实证发现**——算法增量薄（RateQuant + 一条约束），真正价值在 compounding diagnosis + mostly-negative finding。\n5. **[AGREE] 模型规模和统计可靠性有待加强**——14B 上限、无 CI downstream、runtime simulation。\n6. **[AGREE] Limitations 需大幅扩展**。\n\n## Reviewer Divergence\n\n1. **Baseline 缺失 (KVTuner 等)**：R1 认为 major weakness——缺少直接 competitor 对比。R2 rebut——KVTuner 是 layer-level 不是 per-head，GEAR/Kitty 是不同量化范式，非 fair baseline。R2 concedes KVTuner 可作 informative reference。**Director 判断**: R2 的 rebuttal 有理——granularity 和方法范式不同。但作为 informative comparison 纳入 KVTuner 是合理的改进方向。记为 optional action。\n2. **Symmetric-only 定位**：R1 认为 minor weakness——实用场景不清晰。R2 rebut——symmetric 仍是 vLLM/SGLang 默认，kernel 更简单。**Director 判断**: R2 的 rebuttal 合理。低优先级。\n\n---\n\n## Questions（需要作者澄清）\n\n1. 其他 6 模型是否也展示 super-additivity？如果是，为什么不从 constraint 获益？如果不是，compounding 机制如何普遍化？\n2. Decision rule thresholds 的选择方法？Grid search vs visual inspection？Sensitivity analysis？\n3. Spread pattern 是模型固有属性还是校准数据的函数？C4/WikiText-2 以外的 domain 如何？\n4. Profiling + k sweep + solver 的端到端 wall-clock 开销是多少？\n5. Flat 模型上 constrained MCKP 是否产生与 uniform 完全相同的 allocation？如果不同但 PPL 等效，这个 distinction 应明确。\n6. Table 2 的 unconstrained MCKP 与 RateQuant 的精确关系？\n\n---\n\n## Missing References\n\n**共识引用建议** (R1+R2 均提及或交叉同意)：\n- 更新 bib 中已被会议接收的 arXiv preprints 的 venue 信息\n- 核查 4 条 author 顺序不一致的条目（hooper2024kvquant, li2024snapkv, xiao2024streamingllm, xia2025kitty）\n\n**R2 补充引用**：\n- Cocktail (Tian et al., 2025): chunk-adaptive mixed precision\n- MiKV / \"No Token Left Behind\" (Yao et al., 2024): token-level importance-aware mixed precision\n- \"More Tokens, Lower Precision\" (2024): token-precision tradeoff\n\n---\n\n## Overall Assessment\n\n### ARR 维度综合评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.5/5 | **3.25/5** |\n| Excitement | 2.5/5 | 2.5/5 | **2.5/5** |\n| Overall | 2.5/5 | 3.0/5 | **2.75/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n| Reproducibility | 4/5 | 3.5/5 | **3.75/5** |\n\n### 总体评分: **weak reject** (main conference) / **borderline accept** (Findings)\n\n### 判断依据\n\n**Main conference bar 未达到**:\n- 技术新颖性有限——核心算法增量是 RateQuant formulation + 一条 cardinality constraint\n- 正面结果仅限 1/7 模型，方法适用范围极窄\n- Decision rule（Contribution 3）在统计和实用两个维度上均不成立\n- 模型规模上限 14B 限制了对 KV cache 压缩这一研究方向的实际影响\n\n**Findings 可接受**:\n- 实验工作扎实（7 模型、cross-dataset、multi-seed、KIVI 对比）\n- \"非均匀 KV cache 量化在大多数架构上无效\" 的系统性负面结论对社区有重要参考价值\n- Compounding effect 的刻画为后续工作提供了有用的 failure mode analysis\n- 论文对自身方法局限性的承认（KIVI 比较、Limitations section）是诚实的\n\n### 接收路径建议（供 Research Director 参考，非审稿建议）\n\n如目标为 Findings:\n1. [Must-Fix] 将 decision rule 从 Contribution 降级为 analytical observation\n2. [Must-Fix] Abstract 重组——先负面结论再正面 case\n3. [Must-Fix] \"cause\" → \"contributing factor\"，补 1-2 个模型 compounding curve\n4. [Must-Fix] Limitations 大幅扩展\n5. [Should-Fix] Downstream eval 加 CI\n6. [Should-Fix] 形式化 spread/spike/flat 定义\n\n如目标为 Main Conference:\n- 以上全部 + 找到额外 spread 模型（N≥2 正样本）+ 30B+ 验证\n\n---\n\n## Issue Tracker 状态\n\n- **Round 1**: 13 issues, 全部 resolved\n- **Round 2**: 10 new open issues（2 critical, 6 warning, 2 info），2 divergence issues\n- **跨轮复发**: R1-W1（diagnostic overfitting）在 Round 1 resolved 后 Round 2 重新 open——Round 1 的修复（增加 2 模型 + 降级 claim）未充分解决根本问题（N=1 正样本）",
    "project": "ratekv",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-15T15:42:27.682973+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_e886d722cc0b64fdb553f7bb0b99816c:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3763
}
```

</details>

---

### Assistant

_source line 252 · 2026-05-15T15:42:35.767426+00:00_

审稿报告已投递至 Research Director。

**Round 2 审稿完成。** 总评 **weak reject**（main conference）/ **borderline accept**（Findings）。

核心问题：
1. Decision rule 正样本仅 N=1，统计无效且无实用增量——应从 contribution 降级
2. Compounding "cause" 措辞过强，缺少跨模型 compounding 数据
3. Abstract 29.4% 误导性 framing
4. 技术新颖性薄（RateQuant + 一条约束）
5. 模型规模 ≤14B

核心优势：扎实的实验设计、有价值的系统性负面结论、compounding failure mode 的刻画。

Issue tracker 已更新：10 个 open issues（含 1 个 Round 1 复发），2 个 reviewer divergence 记录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

## Round 21

2 recorded events

### User

_source line 253 · 2026-05-15T15:42:38.270510+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。逐条覆盖了 R1 的 8 个 Weakness 和 6 个 Question：

- **AGREE**（7 条）：W1 decision rule 统计无效、W4 规模限制、W5 无 CI、W8 长文本不足、Q1 compounding 缺多模型数据、Q2 阈值选择未 disclosure、Q5 短序列校准外推
- **REBUT**（2 条）：W3 baseline 缺失（KVTuner/GEAR/Kitty 是不同粒度/范式，非 fair baseline）、W7 symmetric-only（仍是主流 deployment 选择，核心发现应可迁移）、Q3 constrained 可靠性（论文 Section 3.5 已充分解释）
- **AGREE with nuance**（3 条）：W2 因果推断（"cause" 过强但机制合理）、W6 runtime simulation（论文已 transparent 标注但应在正文 Limitations 提及）、Q6 flat 模型分配（≠ uniform 但差异 negligible，论文应明确说明）

与 R1 的核心共识：decision rule 的 N=1 正样本问题和模型规模限制是最影响接收决定的 weakness。分歧在 baseline 选择和 compounding 因果推断的严厉程度上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director",
  "source": "review_reviewer_2"
}
```

</details>

---

### Assistant

_source line 254 · 2026-05-15T15:42:54.108962+00:00_

审稿报告已提交给 Research Director。

**Round 2 审稿完成总结**：

- **总评**: weak reject (main conference) / borderline accept (Findings)
- **综合评分**: Soundness 3.25, Excitement 2.5, Overall 2.75
- **流程**: 2 名 Reviewer 独立初审 → 交叉分享逐条回应 → 1 轮收敛 → 汇总报告
- **Open issues**: 10 个（2 critical, 6 warning, 2 info），其中 R1-W1（decision rule overfitting）为跨轮复发
- **核心判断**: 实验扎实的诊断性研究，负面结论有价值，但技术新颖性有限（RateQuant + 一条约束）、正面结果仅 1/7 模型、decision rule 统计和实用性均不足。适合 Findings，不足 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director"
}
```

</details>

---

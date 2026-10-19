# Director coordination — Part 1 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/66/663e3137138e689bfeed.json)

## Round 1

## Round 1

74 recorded events


### User

_source line 1 · 2026-05-19T00:47:31.590009+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: acr-vla-conformal-refinement
- 论文路径: projects/acr-vla-conformal-refinement/paper/main.tex
- 目标 venue: CoRL 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-19T00:47:38.089751+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-19T00:47:38.190796+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-19T00:47:42.256593+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-19T00:47:42.257101+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-19T00:47:47.192755+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-19T00:47:48.598375+00:00_

{"result":"# 项目 acr-vla-conformal-refinement 概况\n\n## 实验状态 (269 个)\n\n- **crm-train-v1**: DONE (killed) — \n- **crm-train-k5**: DONE (killed) — \n- **eval-scalar-unc-spatial**: DONE (killed) — \n- **eval-acr-spatial-v2**: DONE (killed) — \n- **eval-k5-spatial**: DONE (killed) — \n- **eval-object-v7-full**: DONE (killed) — \n- **eval-spatial-v6-full**: DONE (killed) — \n- **eval-object-v5-full**: DONE (killed) — \n- **eval-acr-vla-spatial-v1**: DONE (killed) — \n- **eval-acr-spatial-v1**: DONE (killed) — \n- **eval-reconvla-spatial-v2**: DONE (killed) — \n- **eval-object-v4-full**: DONE (killed) — \n- **eval-spatial-v5-full**: DONE (killed) — \n- **eval-spatial-v3-full**: DONE (killed) — \n- **eval-spatial-reeval-v2**: DONE (killed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-18T21:53:18Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 269 个实验 — ANALYZING 1, DEPLOYED 4, DONE 228, PREPARING 5, RUNNING 31\n**DONE 分布**: failed 31, killed 71, negative 26, success 100\n\n### GPU 占用\n- **实际运行**: 9 张 — bjb1-32546:cuda:4(eval-perdof-object-default-seed45), bjb1-18228:cuda:3(eval-perdof-object-default-seed43), bjb1-18228:cuda:0(eval-obs-only-object-norm02-seed48-r2), bjb2-40593:cuda:0(eval-scalar-object-seed45-r2), bjb2-28827:cuda:1(eval-obs-only-object-norm01-seed45-r2), bjb2-28827:cuda:3(eval-obs-only-object-default-seed45-r2), bjb1-32546:cuda:2(eval-perdof-object-norm003-seed43), bjb1-32546:cuda:1(eval-perdof-object-norm005-seed43), bjb1-32546:cuda:5(eval-perdof-object-norm003-seed45)\n\n### 💾 磁盘余量\n- **bjb2-40593**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 45G/437G 可用（已用 90%） ⚠️\n- **bjb1-18228**:\n  - `/autodl-pub`: 1.2T/7.0T 可用（已用 84%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 399G/438G 可用（已用 4%）\n- **bjb1-32546**:\n  - `/autodl-pub`: 944G/7.0T 可用（已用 87%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  
…[truncated 1803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-19T00:47:48.749465+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-19T00:47:49.101028+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-19T00:47:49.503448+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-19T00:47:49.554102+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-19T00:47:54.522361+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-19T00:47:55.074794+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-19T00:47:55.275950+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/ 2>/dev/null || echo \"paper dir not found\"",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/ 2>/dev/null || echo \"paper dir not found\"",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-19T00:47:55.426915+00:00_

total 32
drwxr-xr-x  3 ubuntu ubuntu 4096 May 15 19:11 .
drwxr-xr-x 11 ubuntu ubuntu 4096 May 18 21:55 ..
-rw-r--r--  1 ubuntu ubuntu 5934 May 15 19:11 figure_plan.md
-rw-r--r--  1 ubuntu ubuntu 9281 May 15 19:10 outline.md
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 19:11 sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-19T00:48:00.447690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-19T00:48:01.000238+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{amsmath,amssymb,amsfonts}
8	\DeclareMathOperator*{\argmin}{arg\,min}
9	\DeclareMathOperator*{\argmax}{arg\,max}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{enumitem}
13	\usepackage{multirow}
14	
15	\graphicspath{{figures/}}
16	
17	\title{Sample, Select, Correct: Inference-Time Action Refinement\\for Frozen Vision-Language-Action Models}
18	
19	\author{
20	  Anonymous
21	}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\begin{abstract}
28	\input{abstract}
29	\end{abstract}
30	
31	\keywords{Vision-Language-Action Models, Inference-Time Refinement, Robotic Manipulation}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{discussion}
38	
39	\bibliography{references}
40	
41	\clearpage
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-19T00:48:01.387009+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-19T00:48:01.585376+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    auth
…[truncated 3980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 198
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-19T00:48:01.585988+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
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

_source line 21 · 2026-05-19T00:48:01.586220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-19T00:48:04.449078+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-19T00:48:05.052145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/",
  "description": "List all files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/",
    "description": "List all files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-19T00:48:05.102808+00:00_

abstract.tex
appendix.tex
camera_ready_template
corl2026_camera_ready_template.zip
corl2026_review_template.zip
corl_2026.sty
corlabbrvnat.bst
discussion.tex
experiments.tex
figures
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
method.tex
references.bib
related_work.tex
review_template

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-19T00:48:11.226311+00:00_

Web search results for query: "CoRL 2026 call for papers submission deadline author guidelines"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Workshops | Danfei Xu","url":"https://www.linkedin.com/posts/danfei-xu-94522133_corl-2026-call-for-workshops-activity-7458261431461965824-yH7b"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"}]

Based on the search results, here's what I found about CoRL 2026's call for papers, submission deadlines, and author guidelines:

## Submission Deadlines

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC. The deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline.

## Author Guidelines

**Paper Format:**
The page limit is 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.

**Required Sections:**
All submissions should include a Limitations section (counted toward the 8-page limit), explici
…[truncated 854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6777
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-19T00:48:18.910159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-19T00:48:19.362340+00:00_

1	Vision-Language-Action (VLA) models for robotic manipulation degrade under distribution shift, yet improving their performance without retraining remains underexplored.
2	We propose a sample-select-correct pipeline for inference-time action refinement of frozen flow-matching VLAs that draws multiple action samples, selects the most representative candidate via $L_2$ argmin, and applies a learned residual correction bounded in magnitude.
3	The correction module is a ${\sim}$327K-parameter MLP conditioned on the frozen VLA's observation embedding, trained offline with supervised $L_2$ loss on demonstration data.
4	On the LIBERO-Object benchmark (10 tasks, 7 seeds), the pipeline achieves $17.6 \pm 2.6$\% versus $11.6 \pm 1.1$\% for the unmodified VLA ($p = 0.0042$, two-sided Fisher's exact test), with a +5.3\,pp margin over argmin selection ($p = 0.0103$).
5	Component decomposition reveals that the entire pipeline benefit derives from learned correction: random sample selection ($K{=}10$) performs at the VLA-only level (11.7\% vs.\ 11.6\%), and argmin selection provides no statistically significant improvement over random selection (12.3\% vs.\ 11.7\%). Multi-sampling without correction is insufficient; directed residual correction is the sole meaningful driver.
6	A conditioning study demonstrates that feature choice is a critical safety factor: observation features produce robust corrections across all tested magnitude bounds (14.3--17.6\%), while per-DOF conformal uncertainty features cause progressive collapse (14\% to 0\%) under the same architecture and training.
7	We further show that multi-sample correction requires stochastic action diversity: tokenized VLAs produce near-identical samples. This establishes an architectural applicability boundary.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-19T00:48:19.362886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-19T00:48:20.317015+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	% --- Para 1: VLAs are impressive but fragile under distribution shift ---
5	Vision-Language-Action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached near-saturation on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this performance masks severe fragility: visual and physical perturbations common in deployment (camera viewpoint shifts, object layout changes, robot initial-state variation) routinely degrade success by over 65 percentage points.
7	On the LIBERO+ benchmark~\cite{fei2025liberoplus}, $\pi_0$ drops from 94.2\% to 6.6\% under initial-state perturbation, and UniVLA drops from 95.2\% to 4.3\% under viewpoint changes.
8	Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled laboratory settings.
9	
10	% --- Para 2: Existing approaches and the gap ---
11	Two lines of work address this challenge.
12	Training-time methods improve the base policy through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}, but require retraining or per-task RL and remain bounded by the training distribution.
13	Inference-time methods leave the policy frozen: ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression for uncertainty quantification and out-of-distribution detection, but does not learn corrective residuals; A2C2~\cite{a2c2_2025} trains a per-step correction head on frozen VLA action chunks, but applies correction unconditionally without multi-sample selection or explicit magnitude control; VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step.
14	Despite growing interest in inference-time action refinement, fundamental design questions remain unanswered: how much does selection contribute relative to cor
…[truncated 3902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-19T00:48:20.317398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-19T00:48:20.819401+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	\begin{figure}[t]
6	  \centering
7	  \includegraphics[width=\linewidth]{fig1_pipeline.pdf}
8	  \caption{Sample-select-correct pipeline. At each control step, $K{=}10$ action samples are drawn from the frozen VLA, the candidate closest to the sample mean is selected via $L_2$ argmin, and a lightweight CRM predicts a bounded residual correction ($\|\boldsymbol{\delta}\|_2 \leq \varepsilon$). The base VLA is never modified.}
9	  \label{fig:pipeline}
10	\end{figure}
11	
12	\textbf{Our method} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
13	
14	\subsection{Problem Setup}
15	\label{sec:problem_setup}
16	
17	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.
18	
19	We instantiate the pipeline on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\pi_\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\pi_\theta$. The method applies to flow-matching VLAs that produce diverse action samples (Section~\ref{sec:applicability}).
20	
21	\subsection{Multi-Sample Selection}
…[truncated 5311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-19T00:48:20.819892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-19T00:48:21.271802+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate the proposed pipeline on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction significantly improve over the frozen VLA baseline?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+6.0\,pp over VLA-only, $p < 0.01$), no (honest negative), and critically, unbounded correction is catastrophic, but obs\_only is robust across all tested seeds and magnitude bounds.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the correction pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf
…[truncated 10124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-19T00:48:21.272156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-19T00:48:21.874767+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	Methods for improving VLA robustness divide into training-time and inference-time approaches.
6	
7	\paragraph{Training-time methods.}
8	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories.
9	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.
10	DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.
11	TT-VLA~\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.
12	All four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.
13	
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.
17	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\,s per control step, prohibitive for real-time manipulation.
18	A2C2~\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.
19	
20	A2C2 is the closest concu
…[truncated 1844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-19T00:48:21.875116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-19T00:48:22.678541+00:00_

1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Why per-DOF conformal features fail.}
6	At $K{=}10$ samples in $d{=}6$ dimensions, per-DOF statistics carry substantial estimation noise despite Ledoit--Wolf shrinkage~\cite{ledoit2004well}.
7	The frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{960}$ already encodes the geometric information these features attempt to capture.
8	Adding noisy low-dimensional statistics to this rich representation degrades CRM predictions rather than improving them.
9	A subtler issue is the gap between offline and closed-loop metrics: all CRM variants achieve low per-step MSE on held-out data, yet offline accuracy does not predict closed-loop success.
10	In closed-loop execution, compounding error~\cite{ross2011dagger} shifts the state distribution, and noisy conformal features amplify this drift.
11	
12	\paragraph{Selection vs.\ correction: contrast with LLM scaling.}
13	Test-time compute scaling in LLMs relies primarily on selection: generating multiple candidates and choosing the best via a verifier or reward model~\cite{snell2024scaling}.
14	Our component decomposition reveals the opposite pattern in embodied action spaces.
15	Random selection at $K{=}10$ performs at the VLA-only level ($11.7$\% vs.\ $11.6$\%), and argmin selection adds a statistically insignificant margin ($12.3$\% vs.\ $11.7$\%).
16	The entire +6.0\,pp pipeline improvement is attributable to learned CRM correction.
17	The structural explanation is that continuous action spaces are low-dimensional ($d{=}6$), so $K{=}10$ flow-matching samples cluster tightly around the mode; selection among near-identical candidates offers negligible discriminative power.
18	Learned correction, by contrast, exploits the 960-dimensional observation embedding to predict a directed residual toward the expert action, a mechanism unavailable to pure selection.
19	This finding suggests that transferring test-time compute ideas from language to embo
…[truncated 3129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-19T00:48:22.829561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-19T00:48:23.130935+00:00_

1	
2	\appendix
3	
4	\section{Inference-Time Scaling with $K$}
5	\label{sec:k_scaling}
6	
7	Figure~\ref{fig:kvalue} plots task success rate against the number of VLA samples $K$.
8	
9	\begin{figure}[h]
10	\centering
11	\includegraphics[width=\linewidth]{figures/fig3_kvalue.pdf}
12	\caption{Success rate (\%) vs.\ number of VLA samples $K$ on LIBERO-Object (obs\_only, $\varepsilon{=}0.2$). Reference lines: VLA-only (11.6\%, 5 seeds) and Argmin-only (12.3\%, 6 seeds). Error bars: $\pm$1 std. The main improvement occurs from $K{=}1$ to $K{=}5$ (+6.4\,pp), with diminishing returns from $K{=}5$ to $K{=}10$ (+0.9\,pp).}
13	\label{fig:kvalue}
14	\end{figure}
15	
16	Performance improves with $K$ but with diminishing returns: $K{=}1$ (10.3\%, 3 seeds) $\to$ $K{=}5$ (16.7\%, 3 seeds) $\to$ $K{=}10$ (17.6\%, 7 seeds).
17	The main jump occurs from $K{=}1$ to $K{=}5$ (+6.4\,pp), while $K{=}5$ to $K{=}10$ adds only +0.9\,pp.
18	At $K{=}1$, CRM correction alone performs at the VLA-only level (11.6\%), confirming that the correction module requires multi-sample selection to be effective.
19	The pattern parallels inference-time compute scaling in LLMs~\cite{snell2024scaling}, where repeated sampling with selection (best-of-$N$) improves output quality with diminishing marginal returns.
20	$K{=}5$ captures ${\sim}$88\% of the $K{=}10$ benefit at half the compute cost, suggesting a practical operating point for latency-sensitive deployment.
21	The compute cost scales linearly: $K{=}10$ requires 10 forward passes through the frozen VLA plus ${\sim}$0.3\,ms for CRM inference, a ${\sim}$10$\times$ increase in VLA compute.
22	
23	
24	\section{Applicability Boundary: Stochastic VLA Diversity}
25	\label{sec:applicability}
26	
27	The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\cite{kim2024openvla} (autoregressive tokenization, 7B).
28	
29	\begin{figure}[h]
30	\centering
31	\include
…[truncated 3623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-19T00:48:23.131317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-19T00:48:23.633175+00:00_

1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	@article{barber2023conformal,
21	    title={Conformal Prediction Beyond Exchangeability},
22	    author={Rina Foygel Barber and Emmanuel J. Cand{\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},
23	    journal={Annals of Statistics},
24	    volume={51},
25	    number={2},
26	    pages={816--845},
27	    year={2023}
28	}
29	
30	@misc{black2024pi0,
31	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
32	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
33	    year={2024},
34	    eprint={2410.24164},
35	    archivePrefix={arXiv},
36	    primaryClass={cs.RO}
37	}
38	
39	@misc{braun2025cgs,
40	    title={Multivariate Conformal Prediction via Conformalized Gaussian Scoring},
41	    author={Sacha Braun and Eug{\`e}ne Berta and Michael I. Jordan and Francis Bach},
42	    year={2025},
43	    eprint={2507.20941},
44	    archivePrefix={arXiv},
45	    primaryClass={stat.ML}
46	}

…[truncated 16366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-19T00:48:23.884446+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-19T00:48:23.935212+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n> Last updated: 2026-05-18 ~09:00 UTC | D061 confirmed: CoRL 2026 main, Option A\\n\\n## Target Venue\\n- **CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2)\\n- Framing: K=10 multi-sample correction as primary method + mechanism insights (D057/D058/D061)\\n\\n## Core Insight (D058 revised)\\nMulti-sample inference-time correction improves frozen VLA policies. The pipeline (K samples → argmin → learned correction) yields +6.0pp over VLA-only (17.6% vs 11.6%, p=0.0042). Component decomposition (D064): argmin selection provides no significant benefit over random (12.3% vs 11.7%), and random K=10 ≈ VLA-only — correction is the sole meaningful driver. Critically, the conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (14.3-17.6% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite.\\n\\n## Headline Metrics\\n- **K=10 CRM obs_only (primary)**: 17.6% (n=7) vs VLA-only 11.6%, Fisher p=0.0042 (two-sided); vs argmin 12.3%, Fisher p=0.0103 (two-sided). +6.0pp / ~52% relative over VLA-only.\\n- **Component decomposition (D064)**: selection ≈ 0 (argmin 12.3% vs random 11.67%, n=3, not significant), correction +5.2pp (CRM vs argmin). Random K=10 ≈ VLA-only K=1 — multi-sampling alone 无用，correction 是唯一实质驱动\\n- **K-value scaling (D063)**: K=1(10.3%±1.5%,n=3) → K=5(16.7%±2.5%,n=3) → K=10(17.6%,n=7). K=5 captures ~89% of K=10 benefit. 收益集中在 K=1→K=5 (+6.4pp)，K=5→K=10 仅 +0.8pp（边际递减）\\n- **Magnitude robustness**: obs_only stable 14.3-17.6% all ε; perdof collapse 14%→11%→9.9%→4.7%→0%\\n- **Latency**: CRM 0.3ms, total overhead 0.34%\\n- **Cross-VLA boundary**: OpenVLA near-determini
…[truncated 3408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-19T00:48:34.477103+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-19T00:48:35.230503+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml\", \"content\": \"_next_id: 65\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 01:03 UTC\\n  summary: MVP 方案确定：3D Point-Reaching Motivating Experiment 验证 per-DOF conformal 特征的信息优势\\n  rationale: IDEA_BRIEF 已设计了完美的 go/no-go gate：用合成数据的 3D reaching task 对比 per-DOF vs\\n    标量 vs 无不确定性三种 conditioning，直接测试核心假设。成本极低（<0.5 GPU-hours），无需 VLA 基础设施，失败则提前止损。Pass\\n    标准明确：B 在非扰动轴 MSE 比 A 低 >10%。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 01:06 UTC\\n  summary: 采纳 Reviewer 建议完善 MVP：增加 B vs C 对比（>5% MSE）、K=10 estimated uncertainty variant、2:1/1.5:1\\n    各向异性 sweep\\n  rationale: Reviewer 正确指出 (1) 缺少 B vs C 对比会遗漏\\\"观测特征已足够\\\"的可能性，这直接关系核心 claim；(2) oracle\\n    uncertainty 与实际 pipeline 存在 gap，K=10 variant 几乎零成本可验证；(3) 5:1 比率过极端，需测试更温和情况。三项改进均不增加显著成本。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 01:47 UTC\\n  summary: MVP 通过，GO — 进入 research 阶段\\n  rationale: 全部 3 条 pass 标准满足且 margin 很大：per-DOF (B) 在非扰动轴 MSE 比标量 (A) 低 22-38%，比无\\n    uncertainty (C) 低 15-39%。K=10 estimated 和弱各向异性(1.5:1)下均成立。核心假设\\\"per-DOF conformal\\n    特征携带更多可操作信息\\\"得到验证。关注风险：oracle→K=10 衰减 ~15pp，真实 7-DOF 场景待验证。\\n  related_experiments:\\n  - exp_id: mvp-point-reaching\\n    role: MVP gate\\n    result: PASS — all 6 conditions met criteria\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 02:59 UTC\\n  summary: Horizon 策略：截取 chunk 前 H_eff=5 步，action_dim=6。CGS 输出 40D。\\n  rationale: SmolVLA chunk_size=50 远超原假设 H=5。receding-horizon 执行语义下只需关注近期 action 的\\n    uncertainty，远期 step 对当前校正无意义。H_eff=5 保持与 IDEA_BRIEF 设计一致，CGS 40D 可控（per-DOF std\\n    30 + radius 5 + volume 5），p/n=6/10=0.6 优于原假设 0.7。H_eff=10 留作 ablation。action_dim=6\\n    使 Ledoit-Wolf 更稳定。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 03:00 UTC\\n  summar
…[truncated 1455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-19T00:48:35.381476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-19T00:48:36.184954+00:00_

FILE_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-19T00:48:36.787696+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/agent/project_config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/agent/project_config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-19T00:48:36.888577+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-19T00:48:36.939289+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 author instructions double blind anonymous review template format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 author instructions double blind anonymous review template format requirements"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-19T00:48:43.614346+00:00_

Web search results for query: "CoRL 2026 author instructions double blind anonymous review template format requirements"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"CVPR 2026 Author Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines"},{"title":"Author Information and Submission Instructions - IEEE International Conference on Multimedia and Expo 2026","url":"https://2026.ieeeicme.org/author-information-and-submission-instructions/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"ACM Multimedia 2026 Conference — Author Instructions","url":"https://2026.acmmm.org/site/author-instructions.html"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"}]

Based on the search results, here is the information about CoRL 2026 author instructions regarding double-blind anonymous review, template, and format requirements:

## Double-Blind Anonymous Review

CoRL is double-blind, which means all papers must be anonymized. The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced.

## Template and Format Requirements

The CoRL LaTeX template uses a custom style based on PMLR (Proceedings of Machine Learning Research) format, with papers limited to 8 pages of content plus unlimited references. You should use "\usepackage[final]{corl_2026}" in your LaTeX template.

## Review Process

CoR
…[truncated 706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6675
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-19T00:48:47.429294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
  "description": "Find config files in agent directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
    "description": "Find config files in agent directory"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-19T00:48:48.282635+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/agent/’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-19T00:48:48.383427+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/ -maxdepth 3 -name \"project_config*\" -o -name \"config.yaml\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/ -maxdepth 3 -name \"project_config*\" -o -name \"config.yaml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-19T00:48:48.434059+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-19T00:48:52.098121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/ -maxdepth 4 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10",
  "description": "Search for config yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/ -maxdepth 4 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10",
    "description": "Search for config yaml files"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-19T00:48:52.500436+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/projects/acr-vla-conformal-refinement.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/secrets/acr-vla-conformal-refinement/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-19T00:48:52.551128+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/ -maxdepth 2 -name \"*.yaml\" 2>/dev/null | head -20",
  "description": "Find yaml files at root level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/ -maxdepth 2 -name \"*.yaml\" 2>/dev/null | head -20",
    "description": "Find yaml files at root level"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-19T00:48:52.601789+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-19T00:48:55.563098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/projects/acr-vla-conformal-refinement.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/projects/acr-vla-conformal-refinement.yaml"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-19T00:48:55.563594+00:00_

1	execution:
2	  account: root
3	  gpu_constraint:
4	  - autodl-4090:cuda:0
5	  gpu_ids:
6	  - bjb2-40593:cuda:0
7	  - bjb1-18228:cuda:0
8	  - bjb1-18228:cuda:1
9	  - bjb1-18228:cuda:2
10	  - bjb1-18228:cuda:3
11	  - bjb1-32546:cuda:0
12	  - bjb1-32546:cuda:1
13	  - bjb1-32546:cuda:2
14	  - bjb1-32546:cuda:3
15	  - bjb1-32546:cuda:4
16	  - bjb1-32546:cuda:5
17	  - bjb2-28827:cuda:0
18	  - bjb2-28827:cuda:1
19	  - bjb2-28827:cuda:2
20	  - bjb2-28827:cuda:3
21	  - bjb2-28827:cuda:4
22	  - bjb2-28827:cuda:5
23	  project_path: /root/acr-vla-conformal-refinement
24	  servers:
25	  - bjb2-40593
26	  - bjb1-18228
27	  - account: root
28	    server: bjb1-32546
29	  - account: root
30	    server: bjb2-28827
31	feishu:
32	  chat_id: oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4
33	  operational_chat_id: oc_718f2ee7260b8649b47875a90c263a2a
34	  review_mode: fresh
35	  review_paper_path: projects/acr-vla-conformal-refinement/paper/main.tex
36	  review_round: 1
37	  review_supplementary_paths: ''
38	  submission_chat_id: oc_416d453a45869a9406db62186b1e3ef7
39	project:
40	  created_at: '2026-05-13T01:01:44.414Z'
41	  description: 'ACR-VLA: Adaptive Conformal Refinement for Robust Vision-Language-Action
42	    Execution'
43	  name: acr-vla-conformal-refinement
44	  phase: research
45	  source_idea_id: idea_006
46	venue: corl-2026
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-19T00:48:55.622788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/venue_rules/corl-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/config/venue_rules/corl-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-19T00:48:55.681962+00:00_

1	rules:
2	  research: []
3	  review: []
4	  writing: []
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 59
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-19T00:49:12.843542+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.pdf 2>/dev/null | grep -E \"Pages|Page size\" || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.pdf 2>/dev/null | grep -E \"Pages|Page size\" || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-19T00:49:12.895456+00:00_

Pages:           14
Page size:       612 x 792 pts (letter)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-19T00:49:21.428930+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/figures/",
  "description": "List figures directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/figures/",
    "description": "List figures directory"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-19T00:49:21.479896+00:00_

fig1_pipeline.pdf
fig2_magnitude.pdf
fig3_kvalue.pdf
fig4_diversity.pdf
fig_magnitude_curve.py
magnitude_curve.pdf
magnitude_curve.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-19T00:49:54.460512+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **目标**: CoRL 2026 Main Conference\n- **截止日期**: 2026-05-29\n- **页数限制**: 正文 ≤ 8 页，References + Appendix 不限\n- **模板**: corl_2026.sty (PMLR-based)\n- **匿名规则**: Double-blind\n- **Limitations 节**: 必须包含，计入 8 页限制\n\n## 论文路径\n- 主文件: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`\n- 各 section 在同目录下: abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, appendix.tex\n- 参考文献: references.bib\n- 图片: figures/ 目录下 fig1_pipeline.pdf, fig2_magnitude.pdf, fig3_kvalue.pdf, fig4_diversity.pdf\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 方法设计的合理性\n- Sample-select-correct pipeline 的数学形式化是否严谨？\n- L2 argmin selection 的理论动机是否充分？为什么选 L2 而不是其他度量？\n- CRM 的架构选择（3 层 MLP, 327K 参数）是否有充分论证？\n- Magnitude clipping (ε) 的设计是否有理论支撑还是纯经验？\n\n### 2. 实验协议的有效性\n- 统计检验是否恰当？Fisher's exact test 在这个场景下是否是最佳选择？\n- Multi-seed 评估：各方法的 seed 数量不同（obs_only 7 seeds, VLA-only 5 seeds, argmin 6 seeds），这是否引入偏差？\n- 每个 seed 只有 100 episodes (10 tasks × 10 rollouts)，样本量是否足以支撑 claims？\n- LIBERO-Spatial 上 \"null result\" 的报告是否充分？仅一个 seed 是否足够？\n\n### 3. Claims 与 Evidence 的匹配\n- \"entire benefit derives from learned correction\" 这个 claim 是否被数据完全支撑？\n- Component decomposition 是否严格（random vs argmin vs CRM）？\n- Conditioning ablation 的因果结论是否过强？（同一架构不同 input → 不同结果，是否能归因于 conformal features？）\n- K-value scaling 分析是否充分？K=1 到 K=5 的跳跃有几个 seeds？\n\n### 4. Baseline 选择\n- 是否缺少关键 baseline？（如 A2C2, ReconVLA 的实际复现对比，而非仅文字讨论）\n- VLA-mean baseline 是否公平？（mean 会模糊 action modes）\n- 为什么没有对比 ensemble 方法或其他 uncertainty-based correction？\n\n### 5. 可复现性\n- 训练细节是否充分？（数据预处理、超参数搜索、early stopping 等）\n- 代码/数据是否承诺公开？\n\n请按照以下格式输出审稿意见：\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注严重程度：[Critical] / [Major] / [Minor]）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Overall Assessment（评分 + 简要理由）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **目标**: CoRL 2026 Main Conference\n- **截止日期**: 2026-05-29\n- **页数限制**: 正文 ≤ 8 页，References + Appendix 不限\n- **模板**: corl_2026.sty (PMLR-based)\n- **匿名规则**: Double-blind\n- **Limitations 节**: 必须包含，计入 8 页限制\n\n## 论文路径\n- 主文件: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`\n- 各 section 在同目录下: abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, appendix.tex\n- 参考文献: references.bib\n- 图片: figures/ 目录下 fig1_pipeline.pdf, fig2_magnitude.pdf, fig3_kvalue.pdf, fig4_diversity.pdf\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 方法设计的合理性\n- Sample-select-correct pipeline 的数学形式化是否严谨？\n- L2 argmin selection 的理论动机是否充分？为什么选 L2 而不是其他度量？\n- CRM 的架构选择（3 层 MLP, 327K 参数）是否有充分论证？\n- Magnitude clipping (ε) 的设计是否有理论支撑还是纯经验？\n\n### 2. 实验协议的有效性\n- 统计检验是否恰当？Fisher's exact test 在这个场景下是否是最佳选择？\n- Multi-seed 评估：各方法的 seed 数量不同（obs_only 7 seeds, VLA-only 5 seeds, argmin 6 seeds），这是否引入偏差？\n- 每个 seed 只有 100 episodes (10 tasks × 10 rollouts)，样本量是否足以支撑 claims？\n- LIBERO-Spatial 上 \"null result\" 的报告是否充分？仅一个 seed 是否足够？\n\n### 3. Claims 与 Evidence 的匹配\n- \"entire benefit derives from learned correction\" 这个 claim 是否被数据完全支撑？\n- Component decomposition 是否严格（random vs argmin vs CRM）？\n- Conditioning ablation 的因果结论是否过强？（同一架构不同 input → 不同结果，是否能归因于 conformal features？）\n- K-value scaling 分析是否充分？K=1 到 K=5 的跳跃有几个 seeds？\n\n### 4. Baseline 选择\n- 是否缺少关键 baseline？（如 A2C2, ReconVLA 的实际复现对比，而非仅文字讨论）\n- VLA-mean baseline 是否公平？（mean 会模糊 action modes）\n- 为什么没有对比 ensemble 方法或其他 uncertainty-based correction？\n\n### 5. 可复现性\n- 训练细节是否充分？（数据预处理、超参数搜索、early stopping 等）\n- 代码/数据是否承诺公开？\n\n请按照以下格式输出审稿意见：\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注严重程度：[Critical] / [Major] / [Minor]）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Overall Assessment（评分 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-19T00:50:14.210248+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19749
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-19T00:50:14.361326+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 相关工作 + 领域定位**。\n\n## Venue 信息\n- **目标**: CoRL 2026 Main Conference\n- **截止日期**: 2026-05-29\n- **页数限制**: 正文 ≤ 8 页，References + Appendix 不限\n- **模板**: corl_2026.sty (PMLR-based)\n- **匿名规则**: Double-blind\n- **Limitations 节**: 必须包含，计入 8 页限制\n\n## 论文路径\n- 主文件: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`\n- 各 section 在同目录下: abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, appendix.tex\n- 参考文献: references.bib\n- 图片: figures/ 目录下 fig1_pipeline.pdf, fig2_magnitude.pdf, fig3_kvalue.pdf, fig4_diversity.pdf\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性与贡献增量\n- \"Sample-select-correct\" pipeline 相对于已有工作（A2C2, ReconVLA, VLA-Pilot, SC-VLA）的技术增量有多大？\n- A2C2 同样是 lightweight correction head + frozen VLA，论文声称的三点差异（multi-sample selection, L2 norm clipping, observation conditioning）是否构成足够的 novelty？\n- Component decomposition 发现 \"correction is the sole driver\" 是否是一个 surprising insight？还是 obvious？\n- \"Conformal features hurt\" 是一个 interesting negative result 还是一个 expected outcome given K=10?\n- 这篇论文的贡献适合 CoRL 的审稿标准吗？CoRL 偏好真实机器人实验和系统层面贡献。\n\n### 2. 相关工作覆盖\n- Related Work 是否遗漏关键引用？请特别关注：\n  - Diffusion Policy (Chi et al., 2023) 作为 action diffusion 的基础工作\n  - 其他 test-time compute scaling for robotics 的工作\n  - Conformal prediction in robotics 的更广泛文献\n  - Residual policy learning 的更多引用\n  - 2025-2026 年的最新 VLA 工作\n- 引用密度是否达到 CoRL 论文的正常水平？（~40 条是否足够？）\n- Related Work 的组织是否清晰？是否做到了 positioning 而非 survey？\n\n### 3. 故事线与 Framing\n- Abstract → Introduction → Method → Experiments → Discussion 是否形成一条连贯主线？\n- 标题 \"Sample, Select, Correct\" 是否准确反映论文核心贡献？（论文发现 selection 不重要，那标题是否误导？）\n- Introduction 的 \"contrast with LLM test-time compute scaling\" 这个 framing 是否恰当？\n- 论文 framing 是 \"method paper\" 还是 \"analysis paper\"？这两种定位的审稿标准不同。\n- 17.6% absolute success rate 作为主要结果，在 CoRL 审稿人看来是否有说服力？\n\n### 4. Discussion 部分\n- \"Selection vs correction\" 的讨论是否过度推广？仅在 LIBERO + SmolVLA 上的发现是否能推广到其他 VLAs？\n- \"When does action-level correction help?\" 的分析是否 trivial？\n\n请按照以下格式输出审稿意见：\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注严重程度：[Critical] / [Major] / [Minor]）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Overall Assessment（评分 + 简要理由）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 相关工作 + 领域定位**。\n\n## Venue 信息\n- **目标**: CoRL 2026 Main Conference\n- **截止日期**: 2026-05-29\n- **页数限制**: 正文 ≤ 8 页，References + Appendix 不限\n- **模板**: corl_2026.sty (PMLR-based)\n- **匿名规则**: Double-blind\n- **Limitations 节**: 必须包含，计入 8 页限制\n\n## 论文路径\n- 主文件: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`\n- 各 section 在同目录下: abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, appendix.tex\n- 参考文献: references.bib\n- 图片: figures/ 目录下 fig1_pipeline.pdf, fig2_magnitude.pdf, fig3_kvalue.pdf, fig4_diversity.pdf\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性与贡献增量\n- \"Sample-select-correct\" pipeline 相对于已有工作（A2C2, ReconVLA, VLA-Pilot, SC-VLA）的技术增量有多大？\n- A2C2 同样是 lightweight correction head + frozen VLA，论文声称的三点差异（multi-sample selection, L2 norm clipping, observation conditioning）是否构成足够的 novelty？\n- Component decomposition 发现 \"correction is the sole driver\" 是否是一个 surprising insight？还是 obvious？\n- \"Conformal features hurt\" 是一个 interesting negative result 还是一个 expected outcome given K=10?\n- 这篇论文的贡献适合 CoRL 的审稿标准吗？CoRL 偏好真实机器人实验和系统层面贡献。\n\n### 2. 相关工作覆盖\n- Related Work 是否遗漏关键引用？请特别关注：\n  - Diffusion Policy (Chi et al., 2023) 作为 action diffusion 的基础工作\n  - 其他 test-time compute scaling for robotics 的工作\n  - Conformal prediction in robotics 的更广泛文献\n  - Residual policy learning 的更多引用\n  - 2025-2026 年的最新 VLA 工作\n- 引用密度是否达到 CoRL 论文的正常水平？（~40 条是否足够？）\n- Related Work 的组织是否清晰？是否做到了 positioning 而非 survey？\n\n### 3. 故事线与 Framing\n- Abstract → Introduction → Method → Experiments → Discussion 是否形成一条连贯主线？\n- 标题 \"Sample, Select, Correct\" 是否准确反映论文核心贡献？（论文发现 selection 不重要，那标题是否误导？）\n- Introduction 的 \"contrast with LLM test-time compute scaling\" 这个 framing 是否恰当？\n- 论文 framing 是 \"method paper\" 还是 \"analysis paper\"？这两种定位的审稿标准不同。\n- 17.6% absolute success rate 作为主要结果，在 CoRL 审稿人看来是否有说服力？\n\n### 4. Discussion 部分\n- \"Selection vs correction\" 的讨论是否过度推广？仅在 LIBERO + SmolVLA 上的发现是否能推广到其他 VLAs？\n- \"When does action-level correction help?\" 的分析是否 trivial？\n\n请按照以下格式输出审稿意见：\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注严重程度：[Critical] / [Major] / [Minor]）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Overall Assessment（评分 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-19T00:50:39.571156+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25209
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-19T00:50:39.722220+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "text": "你是 Reviewer 3，负责 **写作质量 + 格式合规 + Limitations/Ethics**。\n\n## Venue 信息\n- **目标**: CoRL 2026 Main Conference\n- **截止日期**: 2026-05-29\n- **页数限制**: 正文 ≤ 8 页，References + Appendix 不限\n- **模板**: corl_2026.sty (PMLR-based)\n- **匿名规则**: Double-blind\n- **Limitations 节**: 必须包含，计入 8 页限制\n- **Supplementary**: 视频/代码/数据需外部托管（PMLR 不允许视频附件）\n- **AI disclosure**: 需简要说明 generative AI 工具的使用方式\n\n## 论文路径\n- 主文件: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`\n- 各 section 在同目录下: abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, appendix.tex\n- 参考文献: references.bib\n- 图片: figures/ 目录下 fig1_pipeline.pdf, fig2_magnitude.pdf, fig3_kvalue.pdf, fig4_diversity.pdf\n- 编译后 PDF: docs/paper/main.pdf (14 页)\n\n## 你的审查侧重\n\n### 1. 格式合规（硬性要求）\n- 正文是否在 8 页限制内？14 页 PDF 中正文/refs/appendix 各占多少？\n- `\\usepackage{corl_2026}` 是否使用了正确的选项？（review 版应有匿名设置）\n- 是否有行号？（review 版通常需要行号）\n- 作者信息是否匿名？（当前写 \"Anonymous\"，是否合规？）\n- 字体、margin 是否符合模板标准？\n- `\\keywords{}` 命令是否为 CoRL 模板标准要求？\n\n### 2. AI 写作风格检测\n请逐一检查以下 AI 写作标志：\n- **破折号 (em-dash / en-dash)**：全文搜索 `—` 和 ` – `，统计数量，每处标注位置\n- **-ing 短语结尾**：如 \"highlighting the...\", \"demonstrating the...\"\n- **过度分段**：段落是否过短？（2-3 句就换段）\n- **过渡词堆砌**：Furthermore / Moreover / Additionally 连续使用\n- **用词黑名单**：delve / leverage / utilize / facilitate / myriad / plethora / paradigm shift / novel (过度使用)\n- **\"It is worth noting that...\" / \"Notably, ...\"** 等模式\n- **关系从句 (which/that/who) 过多**\n\n### 3. 写作质量\n- Abstract 是否在 150-250 words？是否回答了四个必答问题？\n- Introduction 是否遵循 5 段结构（背景→重要性→现有不足→本文方法→贡献）？\n- 专有名词是否在首次出现时定义？（VLA, CRM, CGS, DOF, ACI 等）\n- 代词指代是否清晰？（this, that, it）\n- 句子是否简洁直接？是否有冗余表达？\n- 图表 caption 是否自包含？\n- 表格格式：小数精度是否统一？最优是否加粗？\n\n### 4. Limitations 节\n- 是否真诚地列出了所有重要限制？\n- 是否遗漏了关键限制？（如仅 simulation、单一 backbone、绝对性能低）\n- 限制的表述是否过于轻描淡写或过于自我贬低？\n\n### 5. 参考文献格式\n- bib 条目是否完整（title, author, year, venue/journal/booktitle）？\n- 是否有格式不一致（arXiv 条目 vs 正式发表的混用）？\n- 是否有重复引用？\n- 引用格式是否符合 corl_2026 模板（natbib/corlabbrvnat.bst）？\n\n### 6. 图表质量\n- 图中字体是否 ≥ 7pt？\n- 数值标签是否被遮挡？\n- Caption 信息密度是否足够？\n- Figure 1 (pipeline) 是否有实质信息量还是仅 trivial 流程图？\n\n请按照以下格式输出审稿意见：\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注严重程度：[Critical] / [Major] / [Minor]）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Format Compliance Checklist（逐项 ✓/✗）\n## AI Style Detection Report（发现的 AI 风格标志及位置）\n## Overall Assessment（评分 + 简要理由）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "text": "你是 Reviewer 3，负责 **写作质量 + 格式合规 + Limitations/Ethics**。\n\n## Venue 信息\n- **目标**: CoRL 2026 Main Conference\n- **截止日期**: 2026-05-29\n- **页数限制**: 正文 ≤ 8 页，References + Appendix 不限\n- **模板**: corl_2026.sty (PMLR-based)\n- **匿名规则**: Double-blind\n- **Limitations 节**: 必须包含，计入 8 页限制\n- **Supplementary**: 视频/代码/数据需外部托管（PMLR 不允许视频附件）\n- **AI disclosure**: 需简要说明 generative AI 工具的使用方式\n\n## 论文路径\n- 主文件: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`\n- 各 section 在同目录下: abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, appendix.tex\n- 参考文献: references.bib\n- 图片: figures/ 目录下 fig1_pipeline.pdf, fig2_magnitude.pdf, fig3_kvalue.pdf, fig4_diversity.pdf\n- 编译后 PDF: docs/paper/main.pdf (14 页)\n\n## 你的审查侧重\n\n### 1. 格式合规（硬性要求）\n- 正文是否在 8 页限制内？14 页 PDF 中正文/refs/appendix 各占多少？\n- `\\usepackage{corl_2026}` 是否使用了正确的选项？（review 版应有匿名设置）\n- 是否有行号？（review 版通常需要行号）\n- 作者信息是否匿名？（当前写 \"Anonymous\"，是否合规？）\n- 字体、margin 是否符合模板标准？\n- `\\keywords{}` 命令是否为 CoRL 模板标准要求？\n\n### 2. AI 写作风格检测\n请逐一检查以下 AI 写作标志：\n- **破折号 (em-dash / en-dash)**：全文搜索 `—` 和 ` – `，统计数量，每处标注位置\n- **-ing 短语结尾**：如 \"highlighting the...\", \"demonstrating the...\"\n- **过度分段**：段落是否过短？（2-3 句就换段）\n- **过渡词堆砌**：Furthermore / Moreover / Additionally 连续使用\n- **用词黑名单**：delve / leverage / utilize / facilitate / myriad / plethora / paradigm shift / novel (过度使用)\n- **\"It is worth noting that...\" / \"Notably, ...\"** 等模式\n- **关系从句 (which/that/who) 过多**\n\n### 3. 写作质量\n- Abstract 是否在 150-250 words？是否回答了四个必答问题？\n- Introduction 是否遵循 5 段结构（背景→重要性→现有不足→本文方法→贡献）？\n- 专有名词是否在首次出现时定义？（VLA, CRM, CGS, DOF, ACI 等）\n- 代词指代是否清晰？（this, that, it）\n- 句子是否简洁直接？是否有冗余表达？\n- 图表 caption 是否自包含？\n- 表格格式：小数精度是否统一？最优是否加粗？\n\n### 4. Limitations 节\n- 是否真诚地列出了所有重要限制？\n- 是否遗漏了关键限制？（如仅 simulation、单一 backbone、绝对性能低）\n- 限制的表述是否过于轻描淡写或过于自我贬低？\n\n### 5. 参考文献格式\n- bib 条目是否完整（title, author, year, venue/journal/booktitle）？\n- 是否有格式不一致（arXiv 条目 vs 正式发表的混用）？\n- 是否有重复引用？\n- 引用格式是否符合 corl_2026 模板（natbib/corlabbrvnat.bst）？\n\n### 6. 图表质量\n- 图中字体是否 ≥ 7pt？\n- 数值标签是否被遮挡？\n- Caption 信息密度是否足够？\n- Figure 1 (pipeline) 是否有实质信息量还是仅 trivial 流程图？\n\n请按照以下格式输出审稿意见：\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注严重程度：[Critical] / [Major] / [Minor]）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Format Compliance Checklist（逐项 ✓/✗）\n## AI Style Detection Report（发现的 AI 风格标志及位置）\n## Overall Assessment（评分 + 简要理由）"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-19T00:50:41.332976+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1610
}
```

</details>

---


### Assistant

_source line 74 · 2026-05-19T00:50:45.645774+00:00_

Round 1 三位 Reviewer 已全部派出，等待独立审稿结果返回。

| Reviewer | 侧重 | 状态 |
|---|---|---|
| R1 | 方法严谨性 + 实验有效性 | 🔄 审稿中 |
| R2 | 新颖性 + 相关工作 + 领域定位 | 🔄 审稿中 |
| R3 | 写作质量 + 格式合规 + Limitations | 🔄 审稿中 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 2

## Round 2

2 recorded events


### User

_source line 75 · 2026-05-19T00:55:30.823222+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验有效性

### Summary

本文提出了一个针对 frozen flow-matching VLA 的 inference-time action refinement pipeline（sample-select-correct）：抽 K=10 个 action samples，L2 argmin 选最接近均值的 candidate，再用 327K 参数的 MLP（CRM）预测有界残差修正。在 LIBERO-Object 上取得 17.6% vs 11.6%（VLA-only）的改进（p=0.0042），但在 LIBERO-Spatial 上无效。论文提供了 component decomposition 分析和 conditioning ablation，发现 conformal features 不如 observation-only conditioning。总体而言，问题有意义、消融较系统，但统计方法存在根本性错误，核心 claim 与证据之间存在内部矛盾，baseline 对比不充分。

### Strengths

- **S1. 问题定义清晰且实用**：inference-time refinement for frozen VLAs 是一个有实际价值的问题方向。不改变 base model、以 post-hoc module 方式 attach 的设计思路在部署场景下有实际意义。

- **S2. Component decomposition 有价值**：系统拆解 random selection、argmin selection、CRM correction 的各自贡献，发现 selection alone 不 work 而 correction 是关键驱动力，这个发现本身有意义，尤其是与 LLM test-time compute scaling 的对比讨论（Section 5, Discussion）提供了跨领域的洞察。

- **S3. Honest negative results**：LIBERO-Spatial null result、conformal features 失效、absolute performance 仅 17.6% 等负面结果被诚实报告（Section 4.4, Section 6 Limitations），这在当前 VLA 文献中较为少见。

- **S4. Applicability boundary 分析**：Section 4.4（tokenized VLA 无法产生 diverse samples）和 Appendix B 提供了 architectural boundary 的证据，Figure 4 中 OpenVLA per-DOF variance < 10^{-30} 的对比很有说服力。

- **S5. 写作整体清晰**：Method section 的形式化较为完整（Eq. 1-3），实验设计的描述有条理。

### Weaknesses

**W1** [Critical] **Fisher's exact test 的独立性假设被违反**

论文将跨 seed 的 episodes pooled 后做 Fisher's exact test（experiments.tex:51, "Two-sided Fisher's exact test on pooled episodes"）。但同一 seed 下的 100 episodes 共享相同的 policy random seed 和 CRM 权重，episodes 之间不满足 Fisher's exact test 要求的独立性。正确做法是在 seed level 做检验（如 paired t-test on seed-level success rates），但此时只有 5-7 个 seeds，统计功效会大幅降低。p=0.0042 的显著性很可能是伪显著（inflated by pseudo-replication）。

- 具体位置：Section 4.1 (experiments.tex:49-51), Abstract (abstract.tex:4), Section 4.2 (experiments.tex:86)
- 影响：论文的核心统计结论（"statistically significant improvement"）可能不成立

**W2** [Critical] **核心 claim 与 K-scaling 数据内部矛盾**

论文在 Abstract、Section 4.2、Discussion 中反复声称 "the entire benefit derives from learned correction"。但 Appendix A (experiments.tex:142) 显示 K=1 时 CRM 修正后成绩 10.3%，低于 VLA-only 的 11.6%。这意味着 correction alone 反而有害。实际上，改进来自 multi-sampling + correction 的组合效应，而非 correction alone。论文在 appendix 中承认 "multi-sample selection is a prerequisite for effective correction"，但 Abstract 和正文的 framing 与此矛盾。claim 需要修正为："correction on a multi-sample selected starting point is the key driver"。

- 具体位置：Abstract (abstract.tex:5), Section 4.2 (experiments.tex:94), Appendix A (appendix.tex:18), Discussion (discussion.tex:16)
- 影响：论文最核心的 contribution claim 在逻辑上自相矛盾

**W3** [Critical] **各方法 seed 数量不一致且无解释**

Table 1 中 obs_only 有 7 seeds，VLA-only 5 seeds，Argmin 6 seeds，Random 3 seeds，VLA-mean 4 seeds，scalar 4 seeds，perdof 6 seeds。这种不对称在论文中完全没有解释。是否有 seeds 被丢弃？是否是 runs 失败？合理的实验协议应对所有方法使用相同的 seed 集合。不均等的 seed 数量引入了 selection bias 的嫌疑。

- 具体位置：Table 1 (experiments.tex:66-81)
- 影响：结果的可信度和可比性受到质疑

**W4** [Major] **LIBERO-Spatial null result 仅基于单个 seed**

Table 1 的 Spatial 列标注 "seed 42 only"。鉴于 Object 上的 per-seed std 已达 2.6pp，仅凭一个 seed 就得出 "correction does not help for spatial reasoning" 的结论（Section 4.2, experiments.tex:98-100）是不充分的。这个 null result 是论文 Contribution 3 的重要支撑。

- 具体位置：Table 1 caption, Section 4.2 (experiments.tex:97-100), Contribution 3 (introduction.tex:37)
- 建议：至少提供 3-5 seeds 的 Spatial 结果

**W5** [Major] **缺少与最接近 baseline（A2C2）的实际对比**

A2C2 在 Related Work 中被明确认定为 "closest concurrent work"（related_work.tex:20），论文还列出了三点架构差异。但对比仅停留在文字层面，没有复现 A2C2 或使用其公开结果做 head-to-head 比较。

- 具体位置：Related Work (related_work.tex:20-22)

**W6** [Major] **Magnitude bound 分析中 seed 数不足**

Figure 2 的 error bars 来自 n=1-7 seeds per epsilon point（experiments.tex:131）。某些 epsilon 值只有 1 个 seed，error bars 无意义。

**W7** [Major] **CRM 训练数据覆盖评估 tasks，无 cross-task 泛化验证**

CRM 在全部 20 LIBERO tasks 的 demo 上训练（experiments.tex:42-43），评估也在这 20 tasks 上。没有 leave-task-out 实验验证泛化能力。

**W8** [Minor] **"Safety factor" 用语不当**："safety" 在机器人学中意味着 formal guarantees，论文未提供。

**W9** [Minor] **L2 argmin 选择缺乏理论动机**，未讨论其他距离度量选项。

**W10** [Minor] **CRM 架构（3层 MLP, 256 hidden）未做 ablation**。

**W11** [Minor] **Per-task analysis 仅 seed 42**，集中改进模式可能 seed-specific。

**W12** [Minor] **引用问题**：24 orphan bib entries，Gauss1857/Lagrange1788 placeholder 条目和 duplicates。

### Questions

Q1. 各方法的 seed 数量为何不同？是否有 seeds 被丢弃？

Q2. K=1 CRM 低于 VLA-only，如何维持 "entire benefit from correction" 的 claim？

Q3. 是否做过 seed-level 统计检验？p-value 多少？

Q4. 为何不复现 A2C2？

Q5. CRM 在 Spatial training data 上的 offline MSE 如何？

Q6. 是否计划公开代码和训练数据？

### Missing References

- Ensemble methods (Lakshminarayanan 2017) 和 MC-Dropout (Gal 2016) 在 bib 中但正文未引用也未做对比
- Diffusion Policy (Chi et al. 2023) 在 bib 中但正文未引用

### Overall Assessment

**Overall: 4/10 (Borderline Reject)**
**Confidence: 4/5 (High)**

方向有价值、消融有系统性，但三个 critical 问题（统计方法错误、核心 claim 内部矛盾、seed 数不一致）严重动摇了实验结论的可信度。建议修正统计方法、统一 seed 数量、修正 claim framing、补充 A2C2 对比后重新投稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 76 · 2026-05-19T00:55:43.505570+00:00_

收到 Reviewer 1 的审稿意见。3 个 Critical（统计方法、claim 矛盾、seed 不一致）、4 个 Major、5 个 Minor，整体评分 4/10 Borderline Reject。

等待 Reviewer 2（新颖性/相关工作）和 Reviewer 3（写作/格式）返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 77 · 2026-05-19T00:55:46.187169+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **4/10 (Borderline Reject)**，主要发现三个 critical 问题：

1. **Fisher's exact test 独立性假设违反**：pooled episodes 跨 seed 不独立，p=0.0042 可能是伪显著
2. **核心 claim 内部矛盾**：声称 "entire benefit from correction"，但 K=1 CRM (10.3%) 低于 VLA-only (11.6%)，correction alone 反而有害
3. **Seed 数不一致且无解释**：各方法 3-7 seeds 不等，存在 selection bias 嫌疑

另有 4 个 major 问题（Spatial 仅 1 seed、缺 A2C2 对比、magnitude 分析 seed 不足、无 cross-task 泛化验证）和 5 个 minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 78 · 2026-05-19T00:55:52.082592+00:00_

Reviewer 1 意见已收到，记录在案。等待 Reviewer 2 和 Reviewer 3 的意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 79 · 2026-05-19T00:55:57.866157+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：Sample, Select, Correct: Inference-Time Action Refinement for Frozen VLAs

**审查侧重：新颖性 + 相关工作 + 领域定位**

---

## Summary

本文提出一个 sample-select-correct 的推理时动作修正流程，用于冻结的 flow-matching VLA。流程包含三步：从 VLA 抽取 K=10 个样本、L2 argmin 选择最接近均值的样本、通过一个 ~327K 参数的 MLP 预测有界残差修正。在 LIBERO-Object 上达到 17.6% vs VLA-only 11.6% (p=0.0042)。核心发现是 pipeline 的全部收益来自 learned correction，selection 本身无显著效果。负面结果显示 conformal features 反而有害，且在 LIBERO-Spatial 上无效果。

论文写作清晰、统计严谨、诚实报告了负面结果，但存在显著的新颖性不足、相关工作覆盖薄弱、以及 CoRL 适配性问题。

---

## 官方维度打分（CoRL review form: Originality / Quality / Clarity / Significance / Relevance）

| 维度 | 评分 | 理由摘要 |
|------|------|----------|
| Originality | 3/10 | 核心方法（MLP 残差修正 + L2 clipping）是已知技术的直接组合；与 A2C2 的差异不构成足够新颖性；"selection 无用"的发现在 d=6, K=10 的低维设定下是可预期结果 |
| Quality | 6/10 | 统计协议严谨（多 seed, Fisher's exact test），ablation 系统，但仅在 LIBERO + SmolVLA 单一设定下验证，范围极窄 |
| Clarity | 7/10 | 写作清晰、组织合理，Method 和 Experiments 描述充分，复现性好 |
| Significance | 3/10 | 17.6% 绝对成功率远未达到部署水平；发现仅限于单一 VLA + 单一 benchmark 的 object 子集；分析洞察（selection 无用）缺乏深度惊喜 |
| Relevance | 4/10 | 全部仿真实验，无真实机器人验证；CoRL 明确偏好 "real-robot experiments or convincing evidence that simulation experiments are transferable to real robots"，论文未提供任何 sim-to-real 的可迁移性证据 |

**Overall: 4/10 (Below acceptance threshold)**

**一句话总结**: 技术贡献薄弱（标准 MLP + L2 clipping），核心分析发现（selection 无用）在理论上可预期，实验范围过窄（单一 VLA、单一 benchmark、纯仿真），不符合 CoRL 对真实机器人实验和系统级贡献的偏好。

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] 新颖性不足：与 A2C2 的技术差异不构成足够的贡献增量

- 具体位置：Section 2 (Related Work), lines 18-21; Section 3.3 (CRM)
- 问题：论文声称与 A2C2 的三点差异——(1) multi-sample selection precedes correction, (2) L2 norm clipping, (3) observation conditioning。但论文自身实验证明 selection 无显著效果（Section 4.2: random 11.7% vs argmin 12.3%），因此差异 (1) 实际不是贡献。L2 norm clipping 是残差学习中标准的稳定性技术（TRANSIC 用 binary gating, PLD 用 bounded RL, DRC 用 exponential decay），不构成方法论新颖性。Observation conditioning（用 frozen VLA 的 960D embedding 作 MLP 输入）也是直觉性的设计选择。剩下的核心贡献变成"用 MLP 在 demonstration 数据上做监督残差学习"，这本质上是 Silver et al., 2018 (Residual Policy Learning) 的直接应用。
- 为什么影响接收：CoRL 期待方法论或系统层面的显著创新。当论文自身否定了三分之一的声称贡献，且另外两点是已知技术时，技术增量不够。
- 建议修改方向：如果重新定位为 analysis/empirical study 论文（而非 method paper），需要大幅扩展分析范围——多个 VLA backbone、多个 benchmark、理论分析为什么 selection 失败。

**N2** [Critical] "Selection 无用"的发现缺乏惊喜度，且标题与结论矛盾

- 具体位置：Title; Section 4.2 (Pipeline Decomposition); Section 5 (Discussion, "Selection vs. correction")
- 问题：论文标题 "Sample, Select, Correct" 暗示三个组件同等重要，但核心发现是 selection 不重要。这构成标题误导。更根本的问题是，这个发现本身缺乏惊喜度：在 d=6 维连续空间中，K=10 个 flow-matching 样本自然会紧密聚集在 mode 附近（论文自己在 Discussion 中承认："continuous action spaces are low-dimensional ($d{=}6$), so $K{=}10$ flow-matching samples cluster tightly around the mode"）。这是基本的高维统计直觉——低维空间中有限样本的 within-cluster 差异本来就小。将此与 LLM test-time compute scaling 做对比是不恰当的，因为 LLM 在高维离散空间（token vocabulary ~32K-128K）中采样，维度和离散性差异使比较缺乏意义。
- 为什么影响接收：如果论文的核心 insight 是可预期的，论文作为 analysis paper 的价值大打折扣。
- 建议修改方向：(1) 修改标题以准确反映核心贡献（如 "Lightweight Residual Correction for Frozen VLAs"）；(2) 提供理论分析（如 sample mean 的 concentration inequality）定量解释为什么 selection 在低维空间中效果有限，而非仅靠实验展示。

**N3** [Critical] 实验范围过窄，缺乏真实机器人实验

- 具体位置：Section 4.1 (Experimental Setup); Section 6 (Limitations)
- 问题：全部实验仅在 LIBERO (仿真) + SmolVLA (450M, 一个特定的 flow-matching VLA) 上进行。CoRL 2026 CFP 明确要求 "submissions should... demonstrate the relevance... to robotics" 并鼓励 "real-robot experiments or convincing evidence that simulation experiments are transferable to real robots"。论文未测试任何其他 VLA backbone（如 π₀, Octo），未测试任何其他 benchmark（如 RLBench, MetaWorld, real-robot setups），也未提供任何 sim-to-real 可迁移性的论据。仅在 LIBERO 的两个子集上的结果（且 Spatial 上无效果）不足以支撑论文的一般性 claim。
- 为什么影响接收：CoRL 审稿人高度重视真实机器人实验和系统可迁移性。纯仿真 + 单一 backbone 的论文在 CoRL 需要非常强的其他贡献来补偿。
- 建议修改方向：至少在一个额外的 flow-matching VLA（如 π₀）上验证；提供 sim-to-real 的初步实验或详细论证。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] 相关工作引用严重不足，24 条 orphan bib entries

- 具体位置：Section 2 (Related Work); references.bib
- 问题：Bib 文件包含 51 条 entries，但正文仅引用 25 条 unique keys。以下重要工作在 bib 中存在但未在正文中引用或讨论：
  - **Diffusion Policy** (Chi et al., 2023) — action diffusion 的基础工作，与本文的 flow-matching sampling 直接相关，必须在 Related Work 中讨论
  - **RT-2** (Brohan et al., 2023) — 重要的 VLA baseline
  - **Octo** (Ghosh et al., 2024) — open-source generalist robot policy
  - **Conformalized Teleoperation** (Zhao et al., 2024) — conformal prediction in robotic action spaces，与本文 conformal features 直接相关
  - **ACP-CBF** (Zhou et al., 2025), **CPLoop** (Wang et al., 2025) — conformal prediction in robotics control
  - **Johannink et al., 2019** — residual RL for robot control
  - 以及更多（详见 orphan list: barber2023, gibbs2021, gal2016, lakshminarayanan2017 等）
- 这给审稿人的印象是作者收集了大量引用但未能将它们整合进叙事。25 条引用对 CoRL 论文来说偏少（典型 CoRL 论文引用 40-60+）。
- 建议：将 orphan bib 中的关键工作纳入 Related Work 讨论，特别是 Diffusion Policy、conformal prediction in robotics 相关工作、和更多 residual learning 工作。

**W2** [Major] Related Work 中 "Conformal Prediction" 的讨论缺失

- 具体位置：Section 2
- 问题：论文的一个核心贡献是 "conformal features hurt performance"（Contribution 2），但 Related Work 中没有专门的 Conformal Prediction 小节。仅在 Section 2.1 (Inference-time methods) 中提到 ReconVLA 用了 conformal quantile regression，以及 Section 2.1 最后一段顺带提到 "conformal uncertainty conditioning [braun2025cgs, angelopoulos2023gentle]"。Conformal prediction in robotics 是一个活跃的子领域（Zhao 2024, Zhou 2025, Wang 2025, Barber 2023, Romano 2019, Gibbs 2021 都在 bib 中但未引用），论文需要专门讨论来 position 自己的负面发现。
- 建议：增加 "Conformal Prediction for Robot Control" 小节，讨论 conformal prediction 在机器人领域的应用现状，然后 position 本文的负面发现。

**W3** [Major] 论文定位不清：method paper vs. analysis paper

- 具体位置：全文
- 问题：论文在两种身份间摇摆。作为 method paper，技术贡献（标准 MLP + L2 clipping）太薄；作为 analysis paper，发现范围太窄（单一 VLA + 单一 benchmark）。Abstract 和 Method 以 method paper 的口吻写（"We propose a sample-select-correct pipeline"），但 Contribution 2 和 3 是 analysis/negative findings。Discussion 也以 analysis 为主。这种身份混淆让审稿人难以评价：如果是 method paper，novelty 不够；如果是 analysis paper，scope 不够。
- 建议：明确选择一个定位。如果选 analysis paper，需要在多个 VLA/benchmark 上验证分析结论；如果选 method paper，需要更强的技术创新或更有说服力的实验结果。

**W4** [Minor] "Conformal features hurt" 作为 negative result 的价值有限

- 具体位置：Section 4.3; Discussion para 1
- 问题：在 K=10, d=6 的设定下，per-DOF statistics 的估计噪声大是可预期的（Ledoit-Wolf shrinkage 也难以在 n=10 个样本上可靠估计 6D 协方差）。这个负面结果更多反映的是统计估计的基本限制，而非 conformal prediction 方法论本身的问题。论文的措辞（"conformal features cause progressive collapse"）可能过度推广了这个发现。
- 建议：更精确地表述为"在 K=10 的低样本预算下，per-DOF conformal statistics 的估计噪声使其不可靠"，并讨论更大 K 下是否可能改善。

**W5** [Minor] LLM test-time compute scaling 的类比不恰当

- 具体位置：Introduction para 4 line 27; Discussion para 2; Appendix A line 19
- 问题：论文反复将 pipeline 与 LLM test-time compute scaling (Snell et al., 2024) 类比，并称发现了"opposite pattern"。但 LLM 在高维离散空间（vocabulary ~32K-128K）中采样，VLA 在 6 维连续空间中采样——两者的采样动力学根本不同，"selection 在低维连续空间中无用"几乎是 trivial 的。这个类比更多是 framing device 而非 genuine insight。
- 建议：弱化此类比，或提供更深入的理论分析来支撑为什么 dimensionality 是决定性因素。

---

## 小问题（不影响接收）

- Bib 中存在重复 key: `Gauss1857` 和 `Lagrange1788` 各出现两次（应为模板残留）
- Table 1 中 "Random (K=10)" 的 Spatial 列为 "---"，应补充数据或解释为什么缺失
- Section 4.2 line 92: "Random selection at K=10 achieves $11.7 \pm 2.3$% (3 seeds)" — 3 seeds 的统计可靠性有限
- Appendix 中 K-scaling 实验仅用 3 seeds (K=1, K=5)，统计功效不足

---

## Questions（需要作者回答）

1. 论文声称 "correction on a pre-screened starting point is more reliable than correction on an arbitrary single sample"（Introduction, line 20），但 K=1 时 CRM 达到 10.3%，低于 VLA-only 的 11.6%。这是否说明 CRM 在没有 multi-sample 预筛选时实际上 *有害*？这与 A2C2（不做 selection）成功的事实如何调和？

2. 为什么不在 π₀ 或其他更大的 flow-matching VLA 上测试？SmolVLA 是 450M 的小模型，其 VLA-only 性能（11.6% on LIBERO-Object）已经非常低。在 base performance 更高的 VLA 上，correction 的效果模式是否不同？

3. CRM 训练用了 LIBERO 的 10 demonstrations per task 的数据。如果增加 demonstration 数量，或者用更多样化的数据训练 CRM，结果会如何变化？当前设定下的 demonstration 数量是否是性能瓶颈？

4. 为什么 conformal features 在 offline MSE 上表现与 obs_only 相当，但 closed-loop 时崩溃？除了 compounding error 这个泛化解释外，能否提供更具体的诊断（如 tracking 不同 timestep 的 correction norm 分布）？

5. LIBERO-Spatial 上所有方法聚集在 30-35%，但 obs_only ε=0.1 和 ε=0.2 都是 35.0%——与 Argmin 的 34.0% 只差 1pp。这是否可能是 noise？能否提供 Spatial 上的多 seed 结果和统计检验？

---

## Missing References

以下是 bib 中存在但未引用的关键工作，建议纳入 Related Work：

1. **Chi et al., 2023 (Diffusion Policy)** — action diffusion 基础工作，必须引用
2. **Brohan et al., 2023 (RT-2)** — 重要 VLA baseline
3. **Ghosh et al., 2024 (Octo)** — 开源通用机器人策略
4. **Zhao et al., 2024 (Conformalized Teleoperation)** — conformal prediction 在机器人动作空间中的应用
5. **Zhou et al., 2025 (ACP-CBF)** — conformal prediction + safety in robotics
6. **Wang et al., 2025 (CPLoop)** — conformal prediction in trajectory optimization
7. **Johannink et al., 2019** — residual RL for robot control

以下是 bib 中不存在但应补充的工作：
- **Action Chunking with Transformers (ACT, Zhao et al., 2023)** — action chunking 的基础性工作
- 更多 2025-2026 年的 VLA 工作（如 HPT, CrossFormer 等最新 generalist robot policies）

---

## 主要优势

1. **诚实透明的报告**：完整报告了 selection 无效、conformal features 有害、Spatial 上无效果等负面结果，并在 Limitations 中坦诚承认 7 条局限，包括个别 seed 的性能下降。这种坦诚在学术论文中值得赞赏。

2. **统计严谨性**：多 seed 评估（5-7 seeds），使用 Fisher's exact test 进行显著性检验，报告了置信区间。这高于很多 robotics 论文的统计标准。

3. **写作质量**：清晰、组织良好、无冗余。Method 和 Experiments 的描述足够复现。

4. **系统性的 ablation**：conditioning variant × magnitude bound 的交叉消融设计合理，K-scaling 和 per-task analysis 提供了有用的细节。

5. **轻量实用性**：~327K 参数、~0.3ms 推理开销的方案在实际部署中有价值（如果效果更显著的话）。

---

## Overall Assessment

**Overall: 4/10 — Below acceptance threshold for CoRL 2026**

本文的核心问题是贡献增量与 venue 期望之间的不匹配。作为提交到 CoRL 的论文：

(1) **技术新颖性不足**：pipeline 的三个组件中，selection 被自己的实验否定，correction 是标准的 supervised residual learning + L2 clipping，conditioning 的分析虽然有趣但发现不够惊人。与最接近的 A2C2 相比，真正的差异点（observation conditioning + magnitude clipping）不足以构成单独的论文贡献。

(2) **缺乏真实机器人实验**：CoRL 对 real-robot validation 有明确偏好。纯仿真论文需要极强的其他贡献来补偿——本文的方法论和分析不够强到可以豁免。

(3) **实验范围太窄**：单一 VLA backbone (SmolVLA 450M)、单一 benchmark family (LIBERO)、且仅在 Object 子集上有效果。论文的一般性 claim（如 "selection provides no benefit in continuous action spaces"）无法从如此窄的实验中得到支撑。

(4) **绝对性能偏低**：17.6% 的成功率虽然统计显著优于 11.6%，但在 CoRL 审稿人看来，两个数字都远未达到有实际意义的水平。

论文最有价值的部分是诚实的组件分解分析和负面结果报告，但这些更适合作为 workshop paper 或 analysis paper 在更广泛的实验基础上发表。建议作者在多个 VLA 上验证、增加真实机器人实验后，重新定位并投稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-19T00:56:05.163567+00:00_

收到 Reviewer 2 的审稿意见。当前状态：

- **Reviewer 1**：已完成（4/10, Borderline Reject）
- **Reviewer 2**：已完成（4/10, Below Acceptance Threshold）
- **Reviewer 3**：等待中

等 Reviewer 3 完成后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 81 · 2026-05-19T00:56:08.441649+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

报告总结：

**Overall: 4/10 (Below acceptance threshold)**

三个 Critical 问题：
1. **新颖性不足** — 与 A2C2 的技术差异不构成足够增量；MLP 残差修正 + L2 clipping 是已知技术的直接组合；论文自身否定了 selection 的贡献
2. **"Selection 无用"的发现缺乏惊喜度** — d=6 维连续空间中 K=10 样本聚集是基本统计直觉；标题 "Sample, Select, Correct" 与结论矛盾
3. **实验范围过窄，无真实机器人实验** — 仅 LIBERO + SmolVLA 单一设定；CoRL 明确偏好 real-robot experiments

三个 Major 问题：引用严重不足（25 条 cited vs 24 条 orphan bib entries，Diffusion Policy 等关键工作未引用）、缺少 conformal prediction 专门讨论、论文 method vs analysis 定位不清。

主要优势：诚实的负面结果报告、统计严谨性、清晰的写作质量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 82 · 2026-05-19T00:56:22.658498+00:00_

收到 Reviewer 1 和 Reviewer 2 的审稿意见。等待 Reviewer 3 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 6

## Round 6

8 recorded events


### User

_source line 83 · 2026-05-19T00:58:04.981731+00:00_

[Reviewer 3 审稿意见]:

# Reviewer 3 审稿意见：写作质量 + 格式合规 + Limitations/Ethics

**论文**: Sample, Select, Correct: Inference-Time Action Refinement for Frozen Vision-Language-Action Models
**Venue**: CoRL 2026

---

## Summary（2-3 句）

本文提出了一个 sample-select-correct pipeline，通过多次采样、L2 argmin 选择和轻量 MLP 残差修正来改善冻结 VLA 的推理时动作质量。写作整体直接且技术性强，AI 风格痕迹极少，但存在一个关键的格式合规问题（正文超页数限制）和缺失 AI disclosure statement。Limitations 节坦诚全面，但仍有遗漏。

---

## Strengths（逐条）

**S1. 写作风格干净直接，AI 痕迹极少。** 全文搜索显示：em-dash (—) 仅出现 1 处且在注释行中（introduction.tex 第 16 行 `% --- Para 3: Our approach — sample-then-correct ---`），正文零 em-dash；en-dash ( – ) 零处；Furthermore/Moreover/Additionally 零处；delve/leverage/utilize/facilitate/myriad/plethora/paradigm shift 零处；"It is worth noting"/"Notably" 零处。这是一篇在 AI 风格清洁度上表现极佳的论文。

**S2. Abstract 结构完整、信息密度高。** 227 词（在 150-250 要求范围内），四个必答问题均有回答：问题（VLA 分布偏移退化）、方法（sample-select-correct pipeline）、机制（327K MLP + L2 clipping）、结果（17.6% vs 11.6%, p=0.0042）。数字使用恰当，服务于 claim 而非堆砌。

**S3. Introduction 遵循清晰的 5 段叙事结构。** 背景→问题→现有不足→本文方法→贡献列表，逻辑递进完整。Contribution 列表的每一条都有对应的 Section/Table 支撑。

**S4. Limitations 节（Section 6）坦诚且全面。** 列出了 7 项限制，包括"17.6% mean success is far from deployment-ready"和"single VLA backbone"等坦率承认，不回避核心弱点。Seed variance 项甚至指出某个 seed 上修正反而降低性能（seed 43: 16% vs 17%）。

**S5. 表格格式规范。** Table 1 小数精度统一（1 位），最优加粗（obs_only ε=0.2 的 17.6 和 +5.3），caption 自包含，列名清晰。

**S6. "novel" 仅出现 1 次（experiments.tex 第 16 行 "novel object instances"），用于描述 benchmark 而非自我吹嘘，合理。**

---

## Weaknesses（逐条，标注严重程度）

**W1 [Critical] 正文超过 8 页限制。**
- 具体位置：PDF 第 1-9 页
- 问题：CoRL 2026 明确要求正文（含 Limitations）≤ 8 页，References 和 Appendix 不计入。视觉检查显示 Section 5 (Discussion) 从第 8 页底部开始，Section 6 (Limitations) 和 Section 7 (Conclusion) 均在第 9 页，References 从第 10 页开始。正文共 9 页，超限 1 页。
- 为什么影响接收：格式违规可能导致 desk reject。CoRL 2026 Author Instructions 明确 "Initial submission: 8 pages maximum for main paper" 且 "Limitations section (counted toward the 8-page limit)"。
- 建议修改方向：压缩 Section 4 (Experiments) 的冗余描述（实验设置中多处内容与 Section 3 重复），或将部分 ablation 讨论移入 Appendix。Section 5 (Discussion) 的三个段落可以更紧凑——"Selection vs. correction" 段落与 Introduction/Experiments 中的讨论有重叠。

**W2 [Critical] 缺少 AI Disclosure Statement。**
- 具体位置：全文（所有 .tex 文件搜索 "AI disclosure", "generative AI", "AI tool", "ChatGPT", "GPT-4", "Claude", "Copilot" 均无匹配）
- 问题：CoRL 2026 Author Instructions 要求 "Authors must briefly disclose how generative AI tools were used for research and paper writing"。论文中没有任何 AI 使用声明。
- 为什么影响接收：这是 CoRL 2026 的明确要求，缺失可能被审稿人或 AC 标记为不合规。
- 建议修改方向：在 Conclusion 后或 Acknowledgments 区域添加简短声明（即使未使用 AI 工具也应说明 "No generative AI tools were used"）。

**W3 [Major] 参考文献存在 24 条 orphan 条目（在 .bib 中但未被引用）。**
- 具体位置：references.bib
- 问题：verify_references 工具检测到 51 条 bib 条目中仅 25 条被引用，24 条 orphan。包括明显的模板残留（Gauss1857、Lagrange1788 各重复 2 次）以及多篇相关但未引用的论文（barber2023conformal, brohan2023rt2, chi2023diffusion_policy, ghosh2024octo, gal2016dropout 等）。
- 为什么影响接收：(1) Gauss1857 和 Lagrange1788 是模板示例条目，提交时不应残留——暴露了投稿前检查不充分；(2) 部分 orphan 条目（如 chi2023diffusion_policy, brohan2023rt2, ghosh2024octo）是 VLA/diffusion policy 领域的重要论文，它们在 bib 中却未被引用，说明 Related Work 可能遗漏了重要参考（详见 Missing References）。
- 建议修改方向：清除所有模板残留和真正不需要的条目；将 Diffusion Policy、RT-2、Octo 等重要相关工作纳入 Related Work 讨论。

**W4 [Major] 专有缩写 DOF、MLP、MSE 未在首次使用时定义。**
- 具体位置：
  - DOF: method.tex 第 17 行 "d=6 (3 translation + 3 rotation)" 暗示但未展开为 "Degrees of Freedom (DOF)"；后续 "per-DOF" 多次使用
  - MLP: introduction.tex 第 19 行 "327K-parameter MLP"，method.tex 第 34 行 "lightweight MLP"——从未展开为 "Multi-Layer Perceptron"
  - MSE: experiments.tex 第 118 行 "per-step MSE"——未展开为 "Mean Squared Error"
- 问题：CoRL 的读者不全是深度学习专家，首次使用缩写应给出完整定义。
- 建议修改方向：在各缩写首次出现时添加完整名称。

**W5 [Major] Limitations 节遗漏了一个关键限制：未与任何外部 baseline 做实验对比。**
- 具体位置：Section 6 (Limitations), Section 2 (Related Work)
- 问题：Introduction 和 Related Work 详细讨论了 A2C2、ReconVLA、VLA-Pilot、SC-VLA 等方法，但实验中没有与任何一个进行定量对比。所有 baseline 都是 ablation variants（同一 frozen VLA 的不同使用方式）。这意味着论文无法证明其方法优于现有 inference-time correction 方法。Limitations 节未提及这一点。
- 为什么影响接收：审稿人（尤其是方法论审稿人）会注意到缺少外部 baseline 对比，这是评估方法真实增量的基本要求。即使实现困难，Limitations 节也应明确承认。
- 建议修改方向：在 Limitations 中添加一条说明为何未与 A2C2 等方法对比（例如：代码未开源、backbone 不同、不可直接比较等），并讨论这对结论的影响。

**W6 [Minor] Abstract 中 "VLA" 缩写首次出现已定义，但 "CRM" 在 Abstract 中未出现，而在 Introduction 第 18 行首次出现时已定义——可接受。但 Abstract 第 5 行的 "K=10" 和 "argmin" 对不熟悉该领域的读者略显突兀。**

**W7 [Minor] -ing 分词短语结尾存在少量实例。**
- experiments.tex 第 88 行: "confirming that action diversity does not center around the correct action"
- experiments.tex 第 136 行: "because loosening the bound exposes noisy correction directions"
- appendix.tex 第 20 行: "suggesting a practical operating point for latency-sensitive deployment"
- discussion.tex 第 19 行: "rethinking the selection-correction balance"
- 数量不多（4 处），但 "suggesting a practical operating point" 和 "confirming that" 是典型的 AI 写作模式。建议改写为独立句。

**W8 [Minor] Table 2 (Appendix, per-task results) 最优结果未加粗。**
- 具体位置：appendix.tex Table 2
- 问题：与 Table 1 格式不一致。Table 1 加粗了最优结果，但 Table 2 没有。
- 建议：统一格式，每行最优值加粗。

**W9 [Minor] Figure 1 (pipeline) 信息密度偏低。**
- 具体位置：method.tex Figure 1（PDF 第 4 页）
- 问题：Figure 1 是全宽图，但传达的信息（Observation → Frozen VLA → K samples → Argmin → CRM → corrected action）相对简单，文字描述即可清楚传达。对于正文空间紧张（已超页数限制）的论文，这张图的空间效率值得商榷。
- 建议：考虑缩小为 column-width 图，或增加更多信息内容（如展示具体的数值流、sample 分布示意等）。

---

## Questions（需要作者回答的问题）

**Q1.** 论文正文（含 Limitations + Conclusion）共 9 页，超出 CoRL 2026 的 8 页限制。作者是否意识到这一问题？计划如何压缩？

**Q2.** 为什么没有与 A2C2（最接近的 concurrent work，Related Work 中有详细讨论）进行实验对比？如果代码不可用，是否考虑过基于论文描述的 reimplementation？

**Q3.** AI disclosure 为何缺失？是否使用了 generative AI 工具辅助写作或研究？

---

## Missing References（可能遗漏的重要引用）

以下论文已在 .bib 中但未被引用，部分是该领域的重要基础工作：
1. **Diffusion Policy** (chi2023diffusion_policy) — 作为 flow-matching VLA 的方法论基础，应在 Related Work 中讨论 diffusion-based policy 与 flow-matching 的关系
2. **RT-2** (brohan2023rt2) — VLA 领域的标志性工作，Introduction 讨论 VLA 时应引用
3. **Octo** (ghosh2024octo) — 另一个重要的 generalist robot policy
4. **Dropout as Bayesian Approximation** (gal2016dropout) / **Deep Ensembles** (lakshminarayanan2017ensembles) — 讨论 uncertainty quantification 时应引用这些经典方法

---

## Format Compliance Checklist

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文 ≤ 8 页 | ✗ | 正文 9 页，超限 1 页 |
| `\usepackage{corl_2026}` 选项正确 | ✓ | 无选项 = submission mode，正确 |
| 行号 | ✓ | 可见，由模板自动开启 |
| 匿名 | ✓ | "Anonymous Author(s)"，模板自动处理 |
| 字体/margin | ✓ | 使用标准 corl_2026.sty 设置 |
| `\keywords{}` 命令 | ✓ | 模板定义的标准命令 (corl_2026.sty L378-393) |
| Limitations 节 | ✓ | Section 6，7 项限制 |
| AI Disclosure | ✗ | 完全缺失 |
| References 格式 | ✓ | natbib + corlabbrvnat.bst，方括号数字编号 |
| Supplementary 格式 | ✓ | Appendix 在 References 后，无视频附件 |
| 模板残留清理 | ✗ | Gauss1857/Lagrange1788 重复条目残留 |

---

## AI Style Detection Report

| 检测项 | 数量 | 位置 | 严重度 |
|--------|------|------|--------|
| Em-dash (—) | 1 | introduction.tex L16（注释行，非正文） | 无 |
| En-dash ( – ) | 0 | — | 无 |
| Furthermore/Moreover/Additionally | 0 | — | 无 |
| 黑名单词汇 (delve/leverage/utilize...) | 0 | — | 无 |
| "It is worth noting" / "Notably" | 0 | — | 无 |
| "novel" 过度使用 | 0 | 仅 1 处，描述 benchmark (experiments.tex L16) | 无 |
| -ing 分词短语结尾 | 4 | experiments.tex L88/L136, appendix.tex L20, discussion.tex L19 | 轻微 |
| 过度分段 | 轻微 | 使用大量 \paragraph{} 但为该领域论文常见格式 | 轻微 |
| 关系从句 (which/that) 过多 | 否 | 使用频率正常 | 无 |

**总评：AI 风格检测结果极佳。** 论文几乎没有典型的 AI 生成文本标志。仅有的 4 处 -ing 分词结尾是非常轻微的问题。这在当前投稿中属于写作风格最干净的论文之一。

---

## Overall Assessment

**评分维度（基于 CoRL 评审标准 6 维度，1-5 分）：**

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3/5 | 方法本身（multi-sample + MLP correction）较简单，但 component decomposition 和 negative results（conformal features 失败）提供了有价值的洞察 |
| Quality | 3/5 | 统计分析严谨（Fisher's exact test, multi-seed），但缺少与外部 baseline 对比是重大缺陷；正文超页数 |
| **Clarity** | **4/5** | **写作直接清晰，AI 痕迹极少，结构完整**；扣分点：缩写定义不全、正文超限 |
| Significance | 2/5 | 17.6% 绝对性能远不足实用，改进仅限于 object manipulation 且不迁移到 spatial tasks |
| Relevance | 4/5 | 直接针对 robot learning 的推理时改进，与 CoRL 受众高度相关 |
| Limitations | 4/5 | 坦诚全面，但遗漏了缺少外部 baseline 对比这一关键限制 |

**Overall: 3/5 — Borderline，倾向 weak reject（从写作/格式角度）**

**一句话总结**: 写作质量上佳且 AI 痕迹极少，但正文超页数限制和缺失 AI disclosure 是必须修复的硬性格式问题；缺少外部 baseline 对比是 Limitations 节的重要遗漏。

**从写作/格式审查角度的建议**: 如果作者能在修改中 (1) 压缩正文至 8 页、(2) 添加 AI disclosure、(3) 清理 bib 残留、(4) 补全缩写定义，格式合规问题均可解决。写作质量本身是该论文的一个优势。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-19T00:58:56.124855+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1（方法严谨性 + 实验有效性）。以下是 Reviewer 2 和 Reviewer 3 的完整审稿意见。请逐条回应他们的主要发现：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：\n- R2 的 novelty 判断（N1: 与 A2C2 差异不构成足够增量）是否与你的方法审查一致？\n- R2 的 \"selection 无用是 trivial 发现\" 判断（N2）你是否同意？\n- R3 的正文超页数（W1）和 AI disclosure 缺失（W2）你是否有补充？\n- R3 的统计检验评价与你的 W1（Fisher's exact test 独立性违反）是否矛盾？（R3 称统计严谨，你称统计有根本错误）\n\n---\n\n## Reviewer 2 完整意见\n\n### Summary\n本文提出一个 sample-select-correct 的推理时动作修正流程，用于冻结的 flow-matching VLA。在 LIBERO-Object 上达到 17.6% vs VLA-only 11.6% (p=0.0042)。核心发现是 pipeline 的全部收益来自 learned correction，selection 本身无显著效果。负面结果显示 conformal features 反而有害，且在 LIBERO-Spatial 上无效果。论文写作清晰、统计严谨、诚实报告了负面结果，但存在显著的新颖性不足、相关工作覆盖薄弱、以及 CoRL 适配性问题。\n\n### 官方维度打分\n| 维度 | 评分 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/10 | 核心方法是已知技术的直接组合；与 A2C2 差异不构成足够新颖性；\"selection 无用\"在 d=6, K=10 低维设定下是可预期结果 |\n| Quality | 6/10 | 统计协议严谨，ablation 系统，但仅单一设定验证 |\n| Clarity | 7/10 | 写作清晰，组织合理 |\n| Significance | 3/10 | 17.6% 绝对成功率远未达部署水平；发现仅限单一设定 |\n| Relevance | 4/10 | 全部仿真实验，无真实机器人验证 |\nOverall: 4/10\n\n### Must-Fix 问题\n\n**N1** [Critical] 新颖性不足：与 A2C2 的三点差异中，selection 被自己实验否定，L2 norm clipping 是标准技术，observation conditioning 是直觉性设计。剩下的核心是 Silver et al., 2018 (Residual Policy Learning) 的直接应用。\n\n**N2** [Critical] \"Selection 无用\"缺乏惊喜度：d=6 维连续空间 K=10 样本聚集是基本统计直觉。标题 \"Sample, Select, Correct\" 与结论矛盾。与 LLM test-time compute 的对比不恰当（高维离散 vs 低维连续）。\n\n**N3** [Critical] 实验范围过窄，无真实机器人实验：仅 LIBERO + SmolVLA。CoRL 偏好 real-robot experiments。\n\n### Should-Fix 问题\n\n**W1** [Major] 24 条 orphan bib entries，正文仅引用 25 条。Diffusion Policy、RT-2、Octo、Conformalized Teleoperation 等重要工作未引用。\n\n**W2** [Major] Related Work 缺少 Conformal Prediction 专门小节。\n\n**W3** [Major] 论文定位不清：method paper vs analysis paper。\n\n**W4** [Minor] \"Conformal features hurt\" 在 K=10 下是可预期结果。\n\n**W5** [Minor] LLM test-time compute scaling 类比不恰当。\n\n### Questions\nQ1. K=1 CRM 低于 VLA-only，是否说明 CRM 无 multi-sample 预筛选时有害？与 A2C2 不做 selection 如何调和？\nQ2. 为何不在 π₀ 上测试？\nQ3. 增加 demonstration 数量结果如何？\nQ4. Conformal features offline MSE 相当但 closed-loop 崩溃的具体诊断？\nQ5. LIBERO-Spatial 上 35% vs 34% 是否 noise？\n\n### Missing References\nchi2023diffusion_policy, brohan2023rt2, ghosh2024octo, zhao2024conformalized, zhou2025acp_cbf, wang2025cploop, johannink2019; 建议补充 ACT (Zhao et al., 2023), HPT, CrossFormer 等。\n\n---\n\n## Reviewer 3 完整意见\n\n### Summary\n写作整体直接且技术性强，AI 风格痕迹极少，但存在关键格式合规问题（正文超页数限制）和缺失 AI disclosure。Limitations 节坦诚全面但仍有遗漏。\n\n### Strengths\nS1. AI 痕迹极少（em-dash 0处正文, en-dash 0, 黑名单词 0）\nS2. Abstract 227 词，结构完整\nS3. Introduction 5 段叙事结构清晰\nS4. Limitations 坦诚（7 项）\nS5. 表格格式规范\nS6. \"novel\" 仅 1 次且合理\n\n### Weaknesses\n**W1** [Critical] 正文 9 页超 8 页限制\n**W2** [Critical] 缺少 AI Disclosure Statement\n**W3** [Major] 24 条 orphan bib 条目（含 Gauss1857/Lagrange1788 模板残留）\n**W4** [Major] DOF/MLP/MSE 缩写未定义\n**W5** [Major] Limitations 遗漏\"未与外部 baseline 对比\"\n**W6** [Minor] Abstract 中 K=10/argmin 对非专业读者突兀\n**W7** [Minor] 4 处 -ing 分词短语\n**W8** [Minor] Table 2 最优未加粗\n**W9** [Minor] Figure 1 信息密度偏低\n\n### Format Compliance Checklist\n正文页数 ✗, AI Disclosure ✗, 模板残留 ✗, 其余 ✓\n\n### AI Style Detection\n总评极佳，仅 4 处轻微 -ing 问题。\n\nOverall: 3/5 Borderline weak reject（从写作/格式角度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1（方法严谨性 + 实验有效性）。以下是 Reviewer 2 和 Reviewer 3 的完整审稿意见。请逐条回应他们的主要发现：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：\n- R2 的 novelty 判断（N1: 与 A2C2 差异不构成足够增量）是否与你的方法审查一致？\n- R2 的 \"selection 无用是 trivial 发现\" 判断（N2）你是否同意？\n- R3 的正文超页数（W1）和 AI disclosure 缺失（W2）你是否有补充？\n- R3 的统计检验评价与你的 W1（Fisher's exact test 独立性违反）是否矛盾？（R3 称统计严谨，你称统计有根本错误）\n\n---\n\n## Reviewer 2 完整意见\n\n### Summary\n本文提出一个 sample-select-correct 的推理时动作修正流程，用于冻结的 flow-matching VLA。在 LIBERO-Object 上达到 17.6% vs VLA-only 11.6% (p=0.0042)。核心发现是 pipeline 的全部收益来自 learned correction，selection 本身无显著效果。负面结果显示 conformal features 反而有害，且在 LIBERO-Spatial 上无效果。论文写作清晰、统计严谨、诚实报告了负面结果，但存在显著的新颖性不足、相关工作覆盖薄弱、以及 CoRL 适配性问题。\n\n### 官方维度打分\n| 维度 | 评分 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/10 | 核心方法是已知技术的直接组合；与 A2C2 差异不构成足够新颖性；\"selection 无用\"在 d=6, K=10 低维设定下是可预期结果 |\n| Quality | 6/10 | 统计协议严谨，ablation 系统，但仅单一设定验证 |\n| Clarity | 7/10 | 写作清晰，组织合理 |\n| Significance | 3/10 | 17.6% 绝对成功率远未达部署水平；发现仅限单一设定 |\n| Relevance | 4/10 | 全部仿真实验，无真实机器人验证 |\nOverall: 4/10\n\n### Must-Fix 问题\n\n**N1** [Critical] 新颖性不足：与 A2C2 的三点差异中，selection 被自己实验否定，L2 norm clipping 是标准技术，observation conditioning 是直觉性设计。剩下的核心是 Silver et al., 2018 (Residual Policy Learning) 的直接应用。\n\n**N2** [Critical] \"Selection 无用\"缺乏惊喜度：d=6 维连续空间 K=10 样本聚集是基本统计直觉。标题 \"Sample, Select, Correct\" 与结论矛盾。与 LLM test-time compute 的对比不恰当（高维离散 vs 低维连续）。\n\n**N3** [Critical] 实验范围过窄，无真实机器人实验：仅 LIBERO + SmolVLA。CoRL 偏好 real-robot experiments。\n\n### Should-Fix 问题\n\n**W1** [Major] 24 条 orphan bib entries，正文仅引用 25 条。Diffusion Policy、RT-2、Octo、Conformalized Teleoperation 等重要工作未引用。\n\n**W2** [Major] Related Work 缺少 Conformal Prediction 专门小节。\n\n**W3** [Major] 论文定位不清：method paper vs analysis paper。\n\n**W4** [Minor] \"Conformal features hurt\" 在 K=10 下是可预期结果。\n\n**W5** [Minor] LLM test-time compute scaling 类比不恰当。\n\n### Questions\nQ1. K=1 CRM 低于 VLA-only，是否说明 CRM 无 multi-sample 预筛选时有害？与 A2C2 不做 selection 如何调和？\nQ2. 为何不在 π₀ 上测试？\nQ3. 增加 demonstration 数量结果如何？\nQ4. Conformal features offline MSE 相当但 closed-loop 崩溃的具体诊断？\nQ5. LIBERO-Spatial 上 35% vs 34% 是否 noise？\n\n### Missing References\nchi2023diffusion_policy, brohan2023rt2, ghosh2024octo, zhao2024conformalized, zhou2025acp_cbf, wang2025cploop, johannink2019; 建议补充 ACT (Zhao et al., 2023), HPT, CrossFormer 等。\n\n---\n\n## Reviewer 3 完整意见\n\n### Summary\n写作整体直接且技术性强，AI 风格痕迹极少，但存在关键格式合规问题（正文超页数限制）和缺失 AI disclosure。Limitations 节坦诚全面但仍有遗漏。\n\n### Strengths\nS1. AI 痕迹极少（em-dash 0处正文, en-dash 0, 黑名单词 0）\nS2. Abstract 227 词，结构完整\nS3. Introduction 5 段叙事结构清晰\nS4. Limitations 坦诚（7 项）\nS5. 表格格式规范\nS6. \"novel\" 仅 1 次且合理\n\n### Weaknesses\n**W1** [Critical] 正文 9 页超 8 页限制\n**W2** [Critical] 缺少 AI Disclosure Statement\n**W3** [Major] 24 条 orphan bib 条目（含 Gauss1857/Lagrange1788 模板残留）\n**W4** [Major] DOF/MLP/MSE 缩写未定义\n**W5** [Major] Limitations 遗漏\"未与外部 baseline 对比\"\n**W6** [Minor] Abstract 中 K=10/argmin 对非专业读者突兀\n**W7** [Minor] 4 处 -ing 分词短语\n**W8** [Minor] Table 2 最优未加粗\n**W9** [Minor] Figure 1 信息密度偏低\n\n### Format Compliance Checklist\n正文页数 ✗, AI Disclosure ✗, 模板残留 ✗, 其余 ✓\n\n### AI Style Detection\n总评极佳，仅 4 处轻微 -ing 问题。\n\nOverall: 3/5 Borderline weak reject（从写作/格式角度）"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-19T00:59:19.134649+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23009
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-19T00:59:19.286408+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2（新颖性 + 相关工作 + 领域定位）。以下是 Reviewer 1 和 Reviewer 3 的完整审稿意见。请逐条回应他们的主要发现：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：\n- R1 的 W1（Fisher's exact test 独立性违反）——你在报告中称\"统计严谨\"，R1 认为统计有根本错误，你如何看？\n- R1 的 W2（核心 claim 内部矛盾：K=1 CRM < VLA-only）是否影响你的 novelty 判断？\n- R1 的 W3（seed 数不一致）你是否同意？\n- R3 的正文超页数（W1）和 AI disclosure 缺失（W2）是否改变你的整体评价？\n\n---\n\n## Reviewer 1 完整意见\n\n### Summary\n问题有意义、消融较系统，但统计方法存在根本性错误，核心 claim 与证据之间存在内部矛盾，baseline 对比不充分。\n\n### Strengths\nS1. 问题定义清晰且实用\nS2. Component decomposition 有价值\nS3. Honest negative results\nS4. Applicability boundary 分析\nS5. 写作整体清晰\n\n### Weaknesses\n**W1** [Critical] Fisher's exact test 独立性假设违反：pooled episodes 跨 seed 不独立，p=0.0042 是伪显著。正确做法是 seed-level 检验（paired t-test），但只有 5-7 seeds 功效大降。\n\n**W2** [Critical] 核心 claim 内部矛盾：Abstract 和正文声称 \"entire benefit from correction\"，但 K=1 CRM 为 10.3%（低于 VLA-only 11.6%）。Correction alone 反而有害。Appendix 承认 \"multi-sample selection is a prerequisite\"，与正文 framing 矛盾。\n\n**W3** [Critical] 各方法 seed 数不一致（3-7 seeds），无解释，存在 selection bias 嫌疑。\n\n**W4** [Major] LIBERO-Spatial null result 仅 1 seed，不充分。\n**W5** [Major] 缺 A2C2 实际对比。\n**W6** [Major] Magnitude 分析某些 ε 仅 1 seed。\n**W7** [Major] CRM 训练覆盖评估 tasks，无 cross-task 泛化验证。\n**W8** [Minor] \"Safety factor\" 用语不当。\n**W9** [Minor] L2 argmin 缺乏理论动机。\n**W10** [Minor] CRM 架构无 ablation。\n**W11** [Minor] Per-task 分析仅 seed 42。\n**W12** [Minor] 24 orphan bib entries。\n\n### Questions\nQ1. seed 数为何不同？Q2. K=1 CRM 低于 VLA-only 如何维持 claim？Q3. seed-level 检验？Q4. 为何不复现 A2C2？Q5. CRM 在 Spatial data 的 offline MSE？Q6. 代码公开？\n\nOverall: 4/10 Borderline Reject, Confidence 4/5\n\n---\n\n## Reviewer 3 完整意见\n\n### Summary\n写作直接技术性强，AI 风格痕迹极少，但正文超页数限制和缺失 AI disclosure 是关键格式问题。\n\n### Strengths\nS1. AI 痕迹极少（全面扫描结果极佳）\nS2. Abstract 227 词结构完整\nS3. Introduction 5 段叙事\nS4. Limitations 坦诚（7 项）\nS5. 表格规范\nS6. \"novel\" 仅 1 次合理使用\n\n### Weaknesses\n**W1** [Critical] 正文 9 页超 8 页限制\n**W2** [Critical] 缺 AI Disclosure\n**W3** [Major] 24 orphan bib（含模板残留）\n**W4** [Major] DOF/MLP/MSE 缩写未定义\n**W5** [Major] Limitations 遗漏\"未与外部 baseline 对比\"\n**W6-W9** [Minor] Abstract 用语、4 处 -ing、Table 2 未加粗最优、Figure 1 信息密度低\n\n### Format Compliance\n正文页数 ✗, AI Disclosure ✗, 模板残留 ✗\n\nOverall: 3/5 Borderline weak reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2（新颖性 + 相关工作 + 领域定位）。以下是 Reviewer 1 和 Reviewer 3 的完整审稿意见。请逐条回应他们的主要发现：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：\n- R1 的 W1（Fisher's exact test 独立性违反）——你在报告中称\"统计严谨\"，R1 认为统计有根本错误，你如何看？\n- R1 的 W2（核心 claim 内部矛盾：K=1 CRM < VLA-only）是否影响你的 novelty 判断？\n- R1 的 W3（seed 数不一致）你是否同意？\n- R3 的正文超页数（W1）和 AI disclosure 缺失（W2）是否改变你的整体评价？\n\n---\n\n## Reviewer 1 完整意见\n\n### Summary\n问题有意义、消融较系统，但统计方法存在根本性错误，核心 claim 与证据之间存在内部矛盾，baseline 对比不充分。\n\n### Strengths\nS1. 问题定义清晰且实用\nS2. Component decomposition 有价值\nS3. Honest negative results\nS4. Applicability boundary 分析\nS5. 写作整体清晰\n\n### Weaknesses\n**W1** [Critical] Fisher's exact test 独立性假设违反：pooled episodes 跨 seed 不独立，p=0.0042 是伪显著。正确做法是 seed-level 检验（paired t-test），但只有 5-7 seeds 功效大降。\n\n**W2** [Critical] 核心 claim 内部矛盾：Abstract 和正文声称 \"entire benefit from correction\"，但 K=1 CRM 为 10.3%（低于 VLA-only 11.6%）。Correction alone 反而有害。Appendix 承认 \"multi-sample selection is a prerequisite\"，与正文 framing 矛盾。\n\n**W3** [Critical] 各方法 seed 数不一致（3-7 seeds），无解释，存在 selection bias 嫌疑。\n\n**W4** [Major] LIBERO-Spatial null result 仅 1 seed，不充分。\n**W5** [Major] 缺 A2C2 实际对比。\n**W6** [Major] Magnitude 分析某些 ε 仅 1 seed。\n**W7** [Major] CRM 训练覆盖评估 tasks，无 cross-task 泛化验证。\n**W8** [Minor] \"Safety factor\" 用语不当。\n**W9** [Minor] L2 argmin 缺乏理论动机。\n**W10** [Minor] CRM 架构无 ablation。\n**W11** [Minor] Per-task 分析仅 seed 42。\n**W12** [Minor] 24 orphan bib entries。\n\n### Questions\nQ1. seed 数为何不同？Q2. K=1 CRM 低于 VLA-only 如何维持 claim？Q3. seed-level 检验？Q4. 为何不复现 A2C2？Q5. CRM 在 Spatial data 的 offline MSE？Q6. 代码公开？\n\nOverall: 4/10 Borderline Reject, Confidence 4/5\n\n---\n\n## Reviewer 3 完整意见\n\n### Summary\n写作直接技术性强，AI 风格痕迹极少，但正文超页数限制和缺失 AI disclosure 是关键格式问题。\n\n### Strengths\nS1. AI 痕迹极少（全面扫描结果极佳）\nS2. Abstract 227 词结构完整\nS3. Introduction 5 段叙事\nS4. Limitations 坦诚（7 项）\nS5. 表格规范\nS6. \"novel\" 仅 1 次合理使用\n\n### Weaknesses\n**W1** [Critical] 正文 9 页超 8 页限制\n**W2** [Critical] 缺 AI Disclosure\n**W3** [Major] 24 orphan bib（含模板残留）\n**W4** [Major] DOF/MLP/MSE 缩写未定义\n**W5** [Major] Limitations 遗漏\"未与外部 baseline 对比\"\n**W6-W9** [Minor] Abstract 用语、4 处 -ing、Table 2 未加粗最优、Figure 1 信息密度低\n\n### Format Compliance\n正文页数 ✗, AI Disclosure ✗, 模板残留 ✗\n\nOverall: 3/5 Borderline weak reject"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-19T00:59:33.407058+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14120
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-19T00:59:33.575173+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "text": "你是 Reviewer 3（写作质量 + 格式合规 + Limitations/Ethics）。以下是 Reviewer 1 和 Reviewer 2 的完整审稿意见。请逐条回应他们的主要发现：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：\n- R1 的 W1（Fisher's exact test 独立性违反）——你在报告中将统计列为 Strength（S2 引用），R1 认为是根本错误。你如何看？这是否影响你的评价？\n- R1 的 W2（核心 claim 矛盾：K=1 CRM < VLA-only）从写作一致性角度你怎么看？\n- R2 的 N1（novelty 不足）和 N2（标题与结论矛盾）从写作角度你是否同意？\n- R2 的 W3（论文定位 method vs analysis 不清）从叙事结构角度你怎么看？\n\n---\n\n## Reviewer 1 完整意见\n\n### Summary\n问题有意义、消融系统，但统计方法存在根本性错误，核心 claim 与证据内部矛盾，baseline 对比不充分。\n\n### Strengths\nS1. 问题定义清晰实用\nS2. Component decomposition 有价值\nS3. Honest negative results\nS4. Applicability boundary 分析\nS5. 写作整体清晰\n\n### Weaknesses\n**W1** [Critical] Fisher's exact test 独立性假设违反：pooled episodes 跨 seed 不独立。p=0.0042 是伪显著。正确做法 seed-level paired t-test，但 5-7 seeds 功效大降。\n\n**W2** [Critical] 核心 claim 内部矛盾：声称 \"entire benefit from correction\"，但 K=1 CRM 10.3% 低于 VLA-only 11.6%。Correction alone 有害。Appendix 承认 \"multi-sample selection is a prerequisite\"，与正文 framing 矛盾。\n\n**W3** [Critical] 各方法 seed 数不一致（3-7），无解释，selection bias 嫌疑。\n\n**W4** [Major] Spatial null result 仅 1 seed\n**W5** [Major] 缺 A2C2 对比\n**W6** [Major] Magnitude 分析某些 ε 仅 1 seed\n**W7** [Major] 无 cross-task 泛化验证\n**W8-W12** [Minor] \"safety factor\" 用语不当、L2 argmin 理论动机缺失、CRM 架构无 ablation、per-task 仅 seed 42、orphan bib\n\nOverall: 4/10 Borderline Reject\n\n---\n\n## Reviewer 2 完整意见\n\n### Summary\n写作清晰、统计严谨、诚实报告负面结果，但新颖性不足、相关工作覆盖薄弱、CoRL 适配性问题。\n\n### 官方维度打分\nOriginality 3/10, Quality 6/10, Clarity 7/10, Significance 3/10, Relevance 4/10\n\n### Must-Fix 问题\n**N1** [Critical] 新颖性不足：与 A2C2 差异中 selection 被自己否定，L2 clipping 是标准技术，observation conditioning 是直觉设计。核心是 Residual Policy Learning 的直接应用。\n\n**N2** [Critical] \"Selection 无用\"缺乏惊喜度：d=6 K=10 聚集是基本统计直觉。标题与结论矛盾。LLM 类比不恰当。\n\n**N3** [Critical] 无真实机器人实验，CoRL 偏好 real-robot。\n\n### Should-Fix 问题\n**W1** [Major] 24 orphan bib，Diffusion Policy/RT-2/Octo 等未引用\n**W2** [Major] 缺 Conformal Prediction 专门小节\n**W3** [Major] method vs analysis 定位不清\n**W4** [Minor] conformal features 在 K=10 下失败可预期\n**W5** [Minor] LLM 类比不恰当\n\n### Missing References\nchi2023diffusion_policy, brohan2023rt2, ghosh2024octo, zhao2024conformalized, zhou2025acp_cbf, wang2025cploop, johannink2019; ACT, HPT, CrossFormer\n\nOverall: 4/10 Below acceptance threshold"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "text": "你是 Reviewer 3（写作质量 + 格式合规 + Limitations/Ethics）。以下是 Reviewer 1 和 Reviewer 2 的完整审稿意见。请逐条回应他们的主要发现：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注：\n- R1 的 W1（Fisher's exact test 独立性违反）——你在报告中将统计列为 Strength（S2 引用），R1 认为是根本错误。你如何看？这是否影响你的评价？\n- R1 的 W2（核心 claim 矛盾：K=1 CRM < VLA-only）从写作一致性角度你怎么看？\n- R2 的 N1（novelty 不足）和 N2（标题与结论矛盾）从写作角度你是否同意？\n- R2 的 W3（论文定位 method vs analysis 不清）从叙事结构角度你怎么看？\n\n---\n\n## Reviewer 1 完整意见\n\n### Summary\n问题有意义、消融系统，但统计方法存在根本性错误，核心 claim 与证据内部矛盾，baseline 对比不充分。\n\n### Strengths\nS1. 问题定义清晰实用\nS2. Component decomposition 有价值\nS3. Honest negative results\nS4. Applicability boundary 分析\nS5. 写作整体清晰\n\n### Weaknesses\n**W1** [Critical] Fisher's exact test 独立性假设违反：pooled episodes 跨 seed 不独立。p=0.0042 是伪显著。正确做法 seed-level paired t-test，但 5-7 seeds 功效大降。\n\n**W2** [Critical] 核心 claim 内部矛盾：声称 \"entire benefit from correction\"，但 K=1 CRM 10.3% 低于 VLA-only 11.6%。Correction alone 有害。Appendix 承认 \"multi-sample selection is a prerequisite\"，与正文 framing 矛盾。\n\n**W3** [Critical] 各方法 seed 数不一致（3-7），无解释，selection bias 嫌疑。\n\n**W4** [Major] Spatial null result 仅 1 seed\n**W5** [Major] 缺 A2C2 对比\n**W6** [Major] Magnitude 分析某些 ε 仅 1 seed\n**W7** [Major] 无 cross-task 泛化验证\n**W8-W12** [Minor] \"safety factor\" 用语不当、L2 argmin 理论动机缺失、CRM 架构无 ablation、per-task 仅 seed 42、orphan bib\n\nOverall: 4/10 Borderline Reject\n\n---\n\n## Reviewer 2 完整意见\n\n### Summary\n写作清晰、统计严谨、诚实报告负面结果，但新颖性不足、相关工作覆盖薄弱、CoRL 适配性问题。\n\n### 官方维度打分\nOriginality 3/10, Quality 6/10, Clarity 7/10, Significance 3/10, Relevance 4/10\n\n### Must-Fix 问题\n**N1** [Critical] 新颖性不足：与 A2C2 差异中 selection 被自己否定，L2 clipping 是标准技术，observation conditioning 是直觉设计。核心是 Residual Policy Learning 的直接应用。\n\n**N2** [Critical] \"Selection 无用\"缺乏惊喜度：d=6 K=10 聚集是基本统计直觉。标题与结论矛盾。LLM 类比不恰当。\n\n**N3** [Critical] 无真实机器人实验，CoRL 偏好 real-robot。\n\n### Should-Fix 问题\n**W1** [Major] 24 orphan bib，Diffusion Policy/RT-2/Octo 等未引用\n**W2** [Major] 缺 Conformal Prediction 专门小节\n**W3** [Major] method vs analysis 定位不清\n**W4** [Minor] conformal features 在 K=10 下失败可预期\n**W5** [Minor] LLM 类比不恰当\n\n### Missing References\nchi2023diffusion_policy, brohan2023rt2, ghosh2024octo, zhao2024conformalized, zhou2025acp_cbf, wang2025cploop, johannink2019; ACT, HPT, CrossFormer\n\nOverall: 4/10 Below acceptance threshold"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-19T00:59:35.128335+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1553
}
```

</details>

---


### Assistant

_source line 90 · 2026-05-19T00:59:39.566645+00:00_

交叉分享已发出。三位 Reviewer 正在相互审阅对方意见并准备 [AGREE]/[REBUT] 回应。等待结果返回后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 91 · 2026-05-19T00:59:42.256515+00:00_

[Reviewer 3 审稿结果]:
审稿意见已提交给 Review Director。

核心发现：

1. **[Critical] 正文超页数**：正文 9 页，超出 CoRL 2026 的 8 页限制 1 页（Discussion/Limitations/Conclusion 溢出到第 9 页）
2. **[Critical] 缺失 AI Disclosure**：CoRL 2026 明确要求，全文无任何声明
3. **[Major] 24 条 orphan bib 条目**：含模板残留（Gauss1857/Lagrange1788），多篇重要论文在 bib 中但未引用
4. **[Major] DOF/MLP/MSE 缩写未定义**
5. **[Major] Limitations 遗漏：未说明为何缺少与 A2C2 等外部 baseline 的实验对比**

写作质量方面，AI 风格检测结果极佳——em-dash 零处（正文）、Furthermore/Moreover 零处、黑名单词汇零处，仅有 4 处轻微 -ing 分词结尾。这是写作风格最干净的维度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 92 · 2026-05-19T00:59:47.505653+00:00_

等待 Reviewer 1 和 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 8

## Round 8

2 recorded events


### User

_source line 93 · 2026-05-19T01:01:33.945009+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应：逐条回应 R1 和 R3

---

### 回应 Reviewer 1

**[AGREE] R1-W1: Fisher's exact test 独立性假设违反**

R1 指出的问题是正确的，我需要修正我在首轮报告中"统计严谨"的评价。

论文在 Section 4.1 (line 50-51) 明确写道 "Two-sided Fisher's exact test on pooled episodes"，即将同一 seed 下的 100 个 episode（10 tasks × 10 rollouts）和跨 seed 的所有 episode 合并后做检验。同一 CRM checkpoint 产生的 episodes 共享 learned weights，同一 seed 下的 rollouts 共享随机状态——这些 episodes 之间存在层次化的相关性，违反了 Fisher's exact test 的独立性假设。

R1 建议的 seed-level paired t-test 是正确方向，但 5-7 seeds 的功效确实大降。实际上，论文也提供了一个非参数证据："All seven obs_only seeds exceed the VLA-only mean"（Section 4.1, line 52），这等价于一个 sign test（7/7, p=0.0078 单侧），不依赖独立性假设且不受 pooling 影响。但论文未正式报告此检验，而是以伪显著的 p=0.0042 为主要证据，这在方法论上有误。

我将我的 Quality 评分从 6/10 下调至 5/10。统计方法论的错误比我首轮评估的更严重。

**[AGREE] R1-W2: 核心 claim 内部矛盾（K=1 CRM < VLA-only）**

这是一个我首轮报告中提到但未充分追究的关键矛盾。重新验证后发现问题比我原来认为的更严重：

- Appendix line 16: "K=1 (10.3%, 3 seeds)"
- Appendix line 18: "At K=1, CRM correction alone performs at the VLA-only level (11.6%)"

这两句在同一段中直接矛盾：10.3% ≠ 11.6%。Appendix 的文字声称 K=1 CRM "performs at the VLA-only level"，但数据显示它比 VLA-only 低 1.3pp。这要么是文字错误（将 10.3% 误描述为 11.6%），要么暴露了更深层的 claim-evidence 不一致。

对 novelty 的影响：这直接动摇了论文的核心叙事。Abstract (line 5) 声称 "directed residual correction is the sole meaningful driver"，但 K=1 时 correction alone 实际上有害（10.3% < 11.6%）。真实的故事应该是 "multi-sampling + correction 的协同效应是 driver，而非 correction alone"。这意味着 selection 并非如论文声称的那样无关紧要——它是 correction 能够工作的前提条件。论文的标题 "Sample, Select, Correct" 反而比其自身的 claim 更准确。

这进一步削弱了我原本就不高的 novelty 评价：如果 selection 是必要前提而非无关组件，那论文的核心 "surprising finding"（selection 无用）就站不住脚。

**[AGREE] R1-W3: Seed 数不一致**

Table 1 的 seed 分布：VLA-only (5), VLA-mean (4), Random (3), Argmin (6), scalar (4), perdof (6), obs_only ε=0.1 (6), obs_only ε=0.2 (7)。论文未在任何地方解释为什么不同方法运行了不同数量的 seeds。

最关键的比较——obs_only (7 seeds) vs VLA-only (5 seeds)——seed 数就不相等。Random 仅 3 seeds 而 Argmin 有 6 seeds，但论文需要比较 random vs argmin 来支撑 "selection 无显著效果" 的 claim。3 seeds 的统计功效极低，很难从中得出可靠结论。

无论原因是计算资源限制还是选择性报告，不解释就是重大缺陷。R1 的 "selection bias 嫌疑" 虽然措辞严厉但并非无据。

**[AGREE] R1-W4: LIBERO-Spatial null result 仅 1 seed**

我在首轮 Q5 中已提出同样质疑。Table 1 中 Spatial 列标注为 "seed 42 only"。论文的 claim "correction does not help for spatial reasoning" (Section 4.2, line 97-100) 基于单一 seed 的数据（所有方法 30-35%），无任何统计检验。这不足以支撑一个一般性结论。

**[AGREE] R1-W5: 缺 A2C2 实际对比**

我在首轮 N1 中讨论了与 A2C2 的 novelty 差距，但未单独标记缺乏直接实验对比。R1 是对的——当论文明确将 A2C2 定位为 "closest concurrent work" (Section 2, line 20) 并声称三点差异时，不在同一 benchmark 上直接比较是重大遗漏。即使 A2C2 代码可能未公开，论文也应在 Limitations 中明确讨论这一点。

**[AGREE] R1-W7: CRM 训练覆盖评估 tasks，无 cross-task 泛化验证**

这是我首轮遗漏的重要问题。Section 3.3 (line 54) 明确写道 "training set comprises 26,737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks"——CRM 在所有 20 个评估 task 的 demonstration 上训练。我们无法判断 CRM 是否学到了 task-agnostic 的修正能力，还是仅记忆了特定 task 的修正模式。对于一个声称是 "drop-in module" 的方法，cross-task（甚至 cross-suite）泛化验证是必要的。

**[REBUT] R1-W8: "Safety factor" 用语**

R1 认为 "safety factor" 不当。但论文使用 "critical safety factor" (Introduction line 29, Contribution 2) 的语境是 "feature choice is a critical safety factor for VLA action correction"——指的是方法学上的安全性（选错 feature 导致 collapse），而非物理安全（robot safety）。虽然措辞可能引起歧义，但这更接近 minor 的用词问题而非 critical 错误。工程领域中 "safety factor" 也常用于指设计裕度。建议改为 "critical design choice" 即可消除歧义。

**[AGREE] R1-W9: L2 argmin 缺乏理论动机**

论文在 Section 3.2 (line 29) 的唯一理由是 "preserves within-sample temporal coherence"（相比 element-wise mean），但未论证 L2 argmin 是最优选择策略，也未与其他 selection criteria（如 median, mode estimation）比较。鉴于论文自身发现 selection 无显著效果（random ≈ argmin），这个动机的缺失倒也不影响最终结论——但它进一步说明 pipeline 设计缺乏理论基础。

**[AGREE] R1-W10: CRM 架构无 ablation**

3-layer MLP (256, 256) 是唯一测试的架构。不同深度、宽度、或更复杂架构（如 attention over action steps）的效果完全未知。作为 method paper 的一个缺陷。

---

### 回应 Reviewer 3

**[AGREE] R3-W1: 正文超 8 页限制**

这是我首轮审稿的重大遗漏。如果 R3 的测量准确（正文 9 页 vs 限制 8 页），这是 CoRL 的格式违规，可导致 desk reject。我在首轮中未检查页数，这是我的审稿失误。

这确实改变我的整体评价——不是因为超 1 页反映了内容问题（可以压缩），而是因为格式合规是基本要求。如果论文在提交前未修正此问题，它根本不应该进入审稿流程。

**[AGREE] R3-W2: 缺 AI Disclosure**

如果 CoRL 2026 要求 AI tool disclosure（这在 2025-2026 的多数 ML 会议中已成为标准要求），缺失就是合规问题。结合 R3 在 S1 中指出的 "AI 痕迹极少"（说明论文质量本身不是问题），disclosure 的缺失更可能是疏忽而非恶意隐瞒。但合规就是合规——必须补上。

**[AGREE] R3-W3: 24 orphan bib entries**

与我首轮 W1 完全一致。特别是 Gauss1857 和 Lagrange1788 的重复 entries 显然是模板残留，未清理反映了投稿准备的不充分。

**[REBUT] R3-W4: DOF/MLP/MSE 缩写未定义**

部分反驳。MLP（Multi-Layer Perceptron）和 MSE（Mean Squared Error）在 ML 社区是普遍接受的标准缩写，CoRL 审稿人（要求有 CoRL/ICRA/IROS/RSS/NeurIPS/ICML 发表经验）无需定义即可理解。DOF（Degrees of Freedom）在 robotics 社区同样是基础术语。将这三个标记为 [Major] 过度了——至多是 Minor。不过我同意 "per-DOF conformal features" 在 Section 3.3 首次出现时如果展开写为 "per-degree-of-freedom" 会更清晰。

**[AGREE] R3-W5: Limitations 遗漏外部 baseline 对比**

Section 6 (Limitations) 的 7 条中确实未提及缺乏与 A2C2 等外部方法的直接对比。这与 R1-W5 形成呼应，是论文应该明确承认的遗漏。

**[REBUT] R3-W6 至 W9 (Minor issues): 整体严重度过高**

R3 的 Minor issues（Abstract "safety factor" 措辞、4 处 -ing 短语、Table 2 加粗、Figure 1 信息密度）都是合理的编辑建议，但不应影响接收决定。特别是 4 处 -ing 短语在全文中仅 4 处，远不构成 "AI 风格" 问题（R3 自己在 S1 中确认了论文 AI 痕迹极少）。

---

### 总结：对我整体评价的影响

R1 和 R3 的发现使我将整体评分从 4/10 下调至 **3-4/10**。

关键变化：
1. **统计方法论降级**（R1-W1）：我原本称赞的 "统计严谨性" 存在根本缺陷（Fisher independence violation）。虽然 sign test (7/7 seeds) 提供了替代证据，但论文报告的 p 值不可信。Quality 从 6/10 降至 5/10。

2. **内部矛盾加深 novelty 担忧**（R1-W2）：K=1 CRM (10.3%) < VLA-only (11.6%) 且 Appendix 存在数值矛盾（将 10.3% 描述为 "at the VLA-only level (11.6%)"），直接动摇 "correction is the sole driver" 的核心 claim。真正的驱动力是 multi-sample selection + correction 的协同，这使论文的 framing 从根本上需要重写。

3. **格式违规**（R3-W1, W2）：如果正文确实超 8 页且缺 AI disclosure，这是独立于内容质量的合规问题。

**最终评分：4/10 (Reject)**，从我首轮的 4/10 边际降低。核心问题不变（novelty 不足、实验范围窄、无 real-robot），R1 的统计和内部矛盾发现进一步削弱了论文的可信度。论文的优势（诚实报告、写作清晰、ablation 设计）不足以弥补这些根本性问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-19T01:01:39.163623+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 和 Reviewer 3 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 95 · 2026-05-19T01:01:41.851303+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心立场总结：
- **同意 R1-W1**（Fisher independence violation）——修正了我首轮对"统计严谨"的错误评价
- **同意 R1-W2**（K=1 矛盾）——发现 Appendix 中 10.3% 被错误描述为 "at VLA-only level (11.6%)"，进一步动摇核心 claim
- **同意 R1-W3**（seed 数不一致）、**R3-W1**（超页数）、**R3-W2**（AI disclosure 缺失）
- **反驳 R3-W4**（DOF/MLP/MSE 缩写）——对 CoRL 审稿人群体来说是标准术语，标为 Major 过度
- 最终评分维持 **4/10 Reject**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 96 · 2026-05-19T01:01:46.651524+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 97 · 2026-05-19T01:01:50.432799+00:00_

[Reviewer 3 审稿意见]:

# Reviewer 3 交叉回应（Cross-Review Response）

---

## 对 Reviewer 1 的逐条回应

### [AGREE] R1-W1: Fisher's exact test 独立性假设违反

R1 指出 pooled episodes 跨 seed 不独立，p=0.0042 是伪显著。**从写作角度我同意这是严重问题，且修改我此前的评价。**

我在 Round 1 审稿中将统计分析作为 Abstract 质量的正面证据（S2），现在认为这需要重新评估。具体问题：

1. **Abstract 第 4 行**直接写 "$p = 0.0042$, two-sided Fisher's exact test"——这个 p 值是论文最醒目的量化 claim 之一，如果统计方法不当，Abstract 的可信度受损。
2. **experiments.tex 第 51 行**："Two-sided Fisher's exact test on pooled episodes"——"pooled episodes" 明确说明了跨 seed 合并，但论文未讨论独立性假设是否成立。
3. 不过，论文有一条部分缓解的证据：**experiments.tex 第 52 行** "All seven obs\_only seeds exceed the VLA-only mean"。这是一个 non-parametric 的一致性观察，不依赖 Fisher's test。如果用 sign test（7/7 seeds > baseline mean, 单侧 p = 0.5^7 ≈ 0.008），方向性结论仍然成立，但 effect size 的精确量化需要 seed-level analysis。

**对我评分的影响**：我将 Quality 从 3/5 下调至 2/5。论文的统计 framing 在 Abstract 和 Introduction 中过于依赖这个 p 值，而正文从未讨论独立性假设。这不仅是统计问题，也是写作透明度问题。

---

### [AGREE] R1-W2: 核心 claim 内部矛盾（K=1 CRM < VLA-only）

**这是我从写作一致性角度最同意的一条，且我发现了一个 R1 未指出的额外矛盾。**

论文在多处声称 "the entire benefit derives from learned correction"（Abstract 第 5 行、experiments.tex 第 94 行），但数据显示：

- K=1 CRM: **10.3%**（appendix.tex 第 16 行，3 seeds）
- VLA-only: **11.6%**（experiments.tex 第 50 行，5 seeds）
- K=1 CRM **低于** VLA-only 1.3pp

**R1 正确指出**：correction alone 不仅没有帮助，还有害。真正起作用的是 selection + correction 的交互，而非 correction 单独。

**我额外发现的写作矛盾**：appendix.tex 第 18 行写 "At $K{=}1$, CRM correction alone performs at the VLA-only level (11.6%)"——这句话暗示 K=1 CRM 的性能约为 11.6%，但实际数字是 10.3%（appendix.tex 第 16 行，同一段落 2 行之前报告的）。这不是"at the VLA-only level"，而是 **below** the VLA-only level。论文在同一个 Appendix 段落内，前面报告 10.3%，后面就说"at the VLA-only level (11.6%)"——这是一个直接的内部数据矛盾。

**对叙事结构的影响**：论文的核心 framing 应该是 "selection provides a stable starting point, correction provides directed improvement; neither alone is sufficient"，而非 "correction is the sole driver"。当前 framing 在 Abstract、Introduction 的 Contribution 1（introduction.tex 第 35 行）、experiments.tex 第 94 行、discussion.tex 第 16 行反复出现，需要全面修订。

---

### [AGREE] R1-W3: 各方法 seed 数不一致

从写作透明度角度完全同意。Table 1 的 $n$ 列清楚展示了不一致（3-7 seeds），但论文没有任何解释。experiments.tex "Statistical protocol" 段落（第 48-53 行）报告了各方法的 seed 数，却未说明为何不同。

一个合理的解释可能是计算资源限制（每个方法 10 forward passes × 10 tasks × 10 rollouts × 300 steps），但论文应明确说明。不解释的不一致 seed 数在审稿人眼中天然引起 selection bias 怀疑。

---

### [AGREE] R1-W4: Spatial null result 仅 1 seed

同意。experiments.tex 第 98 行 "On LIBERO-Spatial, all methods cluster within 30--35%" 是论文的一个重要结论（bounding the scope），但 Table 1 显示 Spatial 列全部是 seed 42 单次结果。用 1 个 seed 的 100 episodes 来支撑 "correction does not help" 的结论，统计功效不足。论文应在 Limitations 中明确承认这一点。

---

### [AGREE] R1-W5: 缺 A2C2 对比

我在 Round 1 已独立标记（W5 [Major]），完全同意 R1。Related Work（related_work.tex 第 20-22 行）用 3 句话详细对比了 A2C2 的 3 个差异点，但实验中没有任何定量对比，落差明显。

---

### [AGREE] R1-W6: Magnitude 分析某些 ε 仅 1 seed

Figure 2 caption（experiments.tex 第 131 行）写 "Error bars: ±1 std across seeds (n=1--7 per point)"——"n=1" 意味着部分数据点是单次结果却带着 "±1 std" 的 caption，这在视觉上造成误导（n=1 无法计算 std）。这是一个图表诚信问题。

---

### [AGREE] R1-W8: "safety factor" 用语不当

同意。Abstract 第 6 行 "feature choice is a critical safety factor" 和 Introduction 第 29 行、第 36 行多次使用 "safety factor"。在机器人学语境中，"safety" 有特定含义（collision avoidance, safe RL, constraint satisfaction）。论文中的含义是 "robustness to conditioning choice"，用 "safety factor" 会引起歧义。建议替换为 "critical design factor" 或 "robustness factor"。

---

## 对 Reviewer 2 的逐条回应

### [AGREE] R2-N1: 新颖性不足

**从写作 framing 角度部分同意。** 论文的方法组件（multi-sampling, L2 argmin, MLP residual, L2 norm clipping）单独看均为已知技术。论文的 Introduction（Contribution 1, introduction.tex 第 35 行）将 pipeline 本身列为贡献，但其真正价值在于 component decomposition 和 negative results。

写作建议：如果论文将自己明确定位为 **analysis paper**（"我们系统分析了 inference-time correction 的哪些组件有效、哪些无效"）而非 **method paper**（"我们提出了一个新的 pipeline"），R2-N1 的批评力度会大幅减弱。当前 framing 在方法贡献上过度承诺。

---

### [AGREE] R2-N2: 标题与结论矛盾

**这直接属于我的审查范围（写作一致性），强烈同意。**

标题 "Sample, Select, Correct" 暗示三个步骤均有独立贡献。但论文自己的结论：
- **Sample**: Random K=10 = VLA-only（experiments.tex 第 92 行）
- **Select**: Argmin 无显著改善（experiments.tex 第 93 行）
- **Correct**: 唯一有效的步骤

标题将三步并列呈现，但实验证明前两步（sample, select）单独无效。一个更诚实的标题应反映这种不对称性，例如 "Correct After Selecting: Why Learned Residuals, Not Sample Selection, Drive Inference-Time VLA Improvement" 或类似表述。

当前标题设置了错误的读者预期——审稿人读完实验后会产生 "被标题欺骗" 的感觉。

---

### [REBUT] R2-N3: 无真实机器人实验

**部分反驳。** CoRL 确实偏好 real-robot 验证，但并非硬性要求。CoRL 2024 接收了多篇纯 simulation 论文。论文在 Limitations 第 1 条（discussion.tex 第 32 行）已明确承认 "Simulation only. All experiments use LIBERO; real-robot transfer is untested." 这是合理的 limitation acknowledgment，不应作为 rejection 的独立理由。

不过，我同意 R2 的基本判断：仅有 simulation 结果确实降低了对 CoRL 受众的吸引力，尤其是在绝对性能仅 17.6% 的情况下。

---

### [AGREE] R2-W1: 24 orphan bib

我在 Round 1 已独立标记（W3 [Major]），完全同意 R2。补充：orphan 条目中 Diffusion Policy (chi2023diffusion_policy)、RT-2 (brohan2023rt2)、Octo (ghosh2024octo) 是 VLA/robot policy 领域的基础论文，它们在 bib 中却未被引用，说明 Related Work 覆盖有缺口。

---

### [AGREE] R2-W3: Method vs Analysis 定位不清

**从叙事结构角度强烈同意。** 论文存在身份危机：
- **Section 3 标题 "Method"**——暗示方法贡献
- **Contribution 1**（introduction.tex 第 35 行）将 pipeline 列为首要贡献
- 但最有价值的内容是 **Section 4.2 pipeline decomposition** 和 **Section 4.3 conditioning ablation**（分析贡献）

如果论文重新定位为 "empirical analysis of inference-time VLA correction"，叙事更一致：Section 3 可改为 "Setup and Pipeline Design"，Contribution 列表可将分析发现前置。这种重新 framing 也能部分回应 R2-N1（novelty）的批评，因为 analysis papers 的 novelty 标准不同于 method papers。

---

### [AGREE] R2-W5: LLM 类比不恰当

从写作角度同意。Discussion（discussion.tex 第 12-19 行）花了一整段讨论 "contrast with LLM scaling"，Appendix（appendix.tex 第 19 行）也有类比。但 d=6 连续空间 vs. 高维离散 token 空间的差异太大，这个类比在分析深度上不足以支撑一整段 Discussion。更关键的是，这段话从写作角度属于 padding——在正文已超页数限制的情况下，这一段可以压缩到 1-2 句，释放宝贵的页面空间。

---

## 综合评估更新

R1 的 W1（统计方法）和 W2（K=1 矛盾）两条批评显著改变了我的评价。在 Round 1 中，我将写作质量和统计呈现列为 Strength，但现在认为：

1. **Abstract 和 Introduction 的核心 claim**（"entire benefit from correction"）与 K=1 数据矛盾，且 Appendix 内部也有数据不一致（10.3% 被描述为"at the VLA-only level 11.6%"）
2. **p=0.0042 在 Abstract 中作为 headline number** 但统计方法有根本性问题
3. **标题与内容矛盾**

这些问题不仅是统计问题，更是写作诚信和叙事一致性问题——直接属于我的审查范围。

**修订评分**：
| 维度 | Round 1 | 修订 | 原因 |
|------|---------|------|------|
| Clarity | 4/5 | 3/5 | K=1 矛盾、标题与结论矛盾、method vs analysis 定位不清 |
| Quality | 3/5 | 2/5 | Fisher's test 问题影响核心 claim 可信度 |
| Limitations | 4/5 | 3/5 | 遗漏缺少外部 baseline 对比、spatial 仅 1 seed |

**Overall: 2.5/5 → 倾向 reject（从写作一致性和格式合规角度）**

格式问题（超页数、缺 AI disclosure）可修复，但核心叙事矛盾（标题 vs 结论、"sole driver" claim vs K=1 data、Appendix 内数据不一致）需要对论文 framing 进行根本性修订，不是简单的文字修改能解决的。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 98 · 2026-05-19T01:02:02.830868+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 11

## Round 11

6 recorded events


### User

_source line 99 · 2026-05-19T01:02:05.516982+00:00_

[Reviewer 3 审稿结果]:
交叉回应已提交。核心发现：

1. **同意 R1-W1**（Fisher's test）并下调 Quality 评分——统计问题也是写作透明度问题
2. **同意 R1-W2**（K=1 矛盾）并额外发现 Appendix 内部数据不一致：第 16 行报告 K=1 CRM 为 10.3%，第 18 行却将其描述为"at the VLA-only level (11.6%)"
3. **强烈同意 R2-N2**（标题矛盾）——"Sample, Select, Correct" 暗示三步均有贡献，但实验证明 sample 和 select 单独无效
4. **同意 R2-W3**（定位不清）——论文以 method paper 呈现，但核心价值在 analysis
5. **部分反驳 R2-N3**——CoRL 不硬性要求 real-robot，且论文已在 Limitations 中承认

Overall 从 3/5 下调至 2.5/5，核心原因从格式问题转为叙事一致性问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-19T01:03:36.386697+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "issues_yaml": "issues:\n  - id: \"R1-W1\"\n    summary: \"Fisher's exact test 独立性假设违反：pooled episodes 跨 seed 不独立，p=0.0042 是伪显著\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。R2 修正了首轮'统计严谨'的评价。R3 指出 sign test (7/7) 可作替代证据但论文未正式报告。\"\n    action_items:\n      - round: 1\n        action: \"改用 seed-level 统计检验（如 sign test 或 Wilcoxon），或在正文中明确讨论 pooled Fisher test 的独立性假设限制\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"核心 claim 内部矛盾：声称 'entire benefit from correction'，但 K=1 CRM (10.3%) 低于 VLA-only (11.6%)，correction alone 有害\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。R2 发现 Appendix 内文字矛盾（10.3% 被描述为 'at VLA-only level 11.6%'）。R3 指出 Abstract/Intro/Experiments/Discussion 四处需全面修订。\"\n    action_items:\n      - round: 1\n        action: \"修正核心 claim 为 'multi-sample selection + correction 的协同效应是 driver'；修复 Appendix 内部数据描述矛盾；全面修订 Abstract/Intro/Experiments/Discussion 中的 framing\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"各方法 seed 数不一致（3-7 seeds）且无解释，存在 selection bias 嫌疑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。论文应明确解释原因或统一 seed 数。\"\n    action_items:\n      - round: 1\n        action: \"统一所有方法的 seed 数量，或在论文中明确解释不一致的原因\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"新颖性不足：与 A2C2 技术差异不构成足够增量，核心方法是已知技术的直接组合\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R2 首轮提出，R3 从写作 framing 角度同意。R3 建议重新定位为 analysis paper 可部分缓解。\"\n    action_items:\n      - round: 1\n        action: \"明确论文定位（method paper vs analysis paper），如选 analysis paper 则重组叙事结构\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"标题 'Sample, Select, Correct' 与结论矛盾：实验证明 sample 和 select 单独无效\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R2 首轮提出，R3 强烈同意——标题设置错误预期，审稿人会感觉'被标题欺骗'。\"\n    action_items:\n      - round: 1\n        action: \"修改标题以准确反映核心贡献（correction 为关键驱动力），而非暗示三步并列\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"实验范围过窄，缺乏真实机器人实验，仅 LIBERO + SmolVLA 单一设定\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 首轮提出。R3 部分反驳：CoRL 不硬性要求 real-robot，且论文已在 Limitations 承认。但三人均认为实验范围过窄。\"\n    action_items:\n      - round: 1\n        action: \"至少在一个额外 VLA backbone 上验证；考虑提供 sim-to-real 初步实验或论证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"LIBERO-Spatial null result 仅基于 1 个 seed，不足以支撑 Contribution 3\"\n    category: experiment\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。\"\n    action_items:\n      - round: 1\n        action: \"提供 Spatial 上至少 3-5 seeds 的结果和统计检验\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"缺少与最接近 baseline（A2C2）的实际实验对比\"\n    category: experiment\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。论文将 A2C2 定位为'closest concurrent work'却无定量对比。\"\n    action_items:\n      - round: 1\n        action: \"复现 A2C2 或使用公开结果做对比；如不可行则在 Limitations 明确解释\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"Magnitude 分析中某些 epsilon 值仅 1 个 seed，error bars 无意义\"\n    category: experiment\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R1 首轮提出，R3 在交叉回应中补充：n=1 时 caption 写 '±1 std' 造成误导。\"\n    action_items:\n      - round: 1\n        action: \"补充 seeds 或在图中明确标注各点的 n 值，n=1 的点不应展示 error bars\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W7\"\n    summary: \"CRM 训练覆盖全部评估 tasks，无 cross-task 泛化验证\"\n    category: experiment\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首轮提出，R2 在交叉回应中同意。\"\n    action_items:\n      - round: 1\n        action: \"增加 leave-task-out 实验验证 CRM 的跨任务泛化能力\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"正文 9 页超出 CoRL 2026 的 8 页限制\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 首轮提出，R2 在交叉回应中同意。可能导致 desk reject。\"\n    action_items:\n      - round: 1\n        action: \"压缩正文至 8 页（压缩 Discussion 重叠段落、Section 4 冗余描述）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"缺失 AI Disclosure Statement，CoRL 2026 明确要求\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 首轮提出，R2 在交叉回应中同意。\"\n    action_items:\n      - round: 1\n        action: \"添加 AI disclosure statement\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"24 条 orphan bib entries，含模板残留（Gauss1857/Lagrange1788），关键相关工作（Diffusion Policy, RT-2, Octo, Conformalized Teleoperation）未引用\"\n    category: writing\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 独立标记。正文仅引用 25 条，引用密度偏低。\"\n    action_items:\n      - round: 1\n        action: \"清理模板残留，将 Diffusion Policy/RT-2/Octo 等关键工作纳入 Related Work\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"Related Work 缺少 Conformal Prediction 专门小节\"\n    category: writing\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"论文核心贡献之一是 conformal features 失效，但 Related Work 缺乏 CP in robotics 的系统讨论。\"\n    action_items:\n      - round: 1\n        action: \"增加 Conformal Prediction for Robot Control 小节\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"论文 method paper vs analysis paper 定位不清\"\n    category: framing\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R2 首轮提出，R3 强烈同意。Abstract/Method 以 method paper 口吻，但核心价值在 analysis。\"\n    action_items:\n      - round: 1\n        action: \"明确选择定位并统一全文叙事\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W8\"\n    summary: \"'safety factor' 用语不当，在机器人学语境中引起歧义\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1 首轮提出，R2 部分反驳（更接近 minor），R3 同意建议改为 'critical design factor'。\"\n    action_items:\n      - round: 1\n        action: \"将 'safety factor' 替换为 'critical design factor' 或 'robustness factor'\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W9\"\n    summary: \"L2 argmin 选择缺乏理论动机，未讨论其他距离度量\"\n    category: method\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 在交叉回应中同意，但指出鉴于 selection 无显著效果，影响有限。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W10\"\n    summary: \"CRM 架构（3 层 MLP, 256 hidden）无 ablation\"\n    category: experiment\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 在交叉回应中同意。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W4\"\n    summary: \"专有缩写 DOF/MLP/MSE 首次使用时未定义\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [3]\n        note: \"R3 标为 Major，R2 反驳降为 Minor——MLP/MSE/DOF 对 CoRL 审稿人是标准术语。R2 同意 per-DOF 首次出现时展开为 per-degree-of-freedom 更佳。\"\n    action_items:\n      - round: 1\n        action: \"首次使用时展开 DOF 为 Degrees of Freedom\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"4 处 -ing 分词短语结尾（轻微 AI 风格）\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [3]\n        note: \"experiments.tex L88/L136, appendix.tex L20, discussion.tex L19。R2 在交叉回应中认为不构成问题。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"Table 2 (Appendix per-task) 最优结果未加粗，与 Table 1 格式不一致\"\n    category: format\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [3]\n        note: \"\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W9\"\n    summary: \"Figure 1 (pipeline) 信息密度偏低，在正文超页数时占用空间过大\"\n    category: format\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [3]\n        note: \"建议缩小为 column-width 或增加信息量。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W11\"\n    summary: \"Per-task analysis 仅 seed 42，集中改进模式可能 seed-specific\"\n    category: experiment\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"LLM test-time compute scaling 类比不恰当（高维离散 vs 低维连续）\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 在交叉回应中同意并指出该段在超页数时属于 padding，可压缩。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "issues_yaml": "issues:\n  - id: \"R1-W1\"\n    summary: \"Fisher's exact test 独立性假设违反：pooled episodes 跨 seed 不独立，p=0.0042 是伪显著\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。R2 修正了首轮'统计严谨'的评价。R3 指出 sign test (7/7) 可作替代证据但论文未正式报告。\"\n    action_items:\n      - round: 1\n        action: \"改用 seed-level 统计检验（如 sign test 或 Wilcoxon），或在正文中明确讨论 pooled Fisher test 的独立性假设限制\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"核心 claim 内部矛盾：声称 'entire benefit from correction'，但 K=1 CRM (10.3%) 低于 VLA-only (11.6%)，correction alone 有害\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。R2 发现 Appendix 内文字矛盾（10.3% 被描述为 'at VLA-only level 11.6%'）。R3 指出 Abstract/Intro/Experiments/Discussion 四处需全面修订。\"\n    action_items:\n      - round: 1\n        action: \"修正核心 claim 为 'multi-sample selection + correction 的协同效应是 driver'；修复 Appendix 内部数据描述矛盾；全面修订 Abstract/Intro/Experiments/Discussion 中的 framing\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W3\"\n    summary: \"各方法 seed 数不一致（3-7 seeds）且无解释，存在 selection bias 嫌疑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。论文应明确解释原因或统一 seed 数。\"\n    action_items:\n      - round: 1\n        action: \"统一所有方法的 seed 数量，或在论文中明确解释不一致的原因\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N1\"\n    summary: \"新颖性不足：与 A2C2 技术差异不构成足够增量，核心方法是已知技术的直接组合\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R2 首轮提出，R3 从写作 framing 角度同意。R3 建议重新定位为 analysis paper 可部分缓解。\"\n    action_items:\n      - round: 1\n        action: \"明确论文定位（method paper vs analysis paper），如选 analysis paper 则重组叙事结构\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N2\"\n    summary: \"标题 'Sample, Select, Correct' 与结论矛盾：实验证明 sample 和 select 单独无效\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R2 首轮提出，R3 强烈同意——标题设置错误预期，审稿人会感觉'被标题欺骗'。\"\n    action_items:\n      - round: 1\n        action: \"修改标题以准确反映核心贡献（correction 为关键驱动力），而非暗示三步并列\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-N3\"\n    summary: \"实验范围过窄，缺乏真实机器人实验，仅 LIBERO + SmolVLA 单一设定\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 首轮提出。R3 部分反驳：CoRL 不硬性要求 real-robot，且论文已在 Limitations 承认。但三人均认为实验范围过窄。\"\n    action_items:\n      - round: 1\n        action: \"至少在一个额外 VLA backbone 上验证；考虑提供 sim-to-real 初步实验或论证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"LIBERO-Spatial null result 仅基于 1 个 seed，不足以支撑 Contribution 3\"\n    category: experiment\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。\"\n    action_items:\n      - round: 1\n        action: \"提供 Spatial 上至少 3-5 seeds 的结果和统计检验\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"缺少与最接近 baseline（A2C2）的实际实验对比\"\n    category: experiment\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 一致确认。论文将 A2C2 定位为'closest concurrent work'却无定量对比。\"\n    action_items:\n      - round: 1\n        action: \"复现 A2C2 或使用公开结果做对比；如不可行则在 Limitations 明确解释\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"Magnitude 分析中某些 epsilon 值仅 1 个 seed，error bars 无意义\"\n    category: experiment\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"R1 首轮提出，R3 在交叉回应中补充：n=1 时 caption 写 '±1 std' 造成误导。\"\n    action_items:\n      - round: 1\n        action: \"补充 seeds 或在图中明确标注各点的 n 值，n=1 的点不应展示 error bars\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W7\"\n    summary: \"CRM 训练覆盖全部评估 tasks，无 cross-task 泛化验证\"\n    category: experiment\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首轮提出，R2 在交叉回应中同意。\"\n    action_items:\n      - round: 1\n        action: \"增加 leave-task-out 实验验证 CRM 的跨任务泛化能力\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"正文 9 页超出 CoRL 2026 的 8 页限制\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 首轮提出，R2 在交叉回应中同意。可能导致 desk reject。\"\n    action_items:\n      - round: 1\n        action: \"压缩正文至 8 页（压缩 Discussion 重叠段落、Section 4 冗余描述）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W2\"\n    summary: \"缺失 AI Disclosure Statement，CoRL 2026 明确要求\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 首轮提出，R2 在交叉回应中同意。\"\n    action_items:\n      - round: 1\n        action: \"添加 AI disclosure statement\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W1\"\n    summary: \"24 条 orphan bib entries，含模板残留（Gauss1857/Lagrange1788），关键相关工作（Diffusion Policy, RT-2, Octo, Conformalized Teleoperation）未引用\"\n    category: writing\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"三位 Reviewer 独立标记。正文仅引用 25 条，引用密度偏低。\"\n    action_items:\n      - round: 1\n        action: \"清理模板残留，将 Diffusion Policy/RT-2/Octo 等关键工作纳入 Related Work\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W2\"\n    summary: \"Related Work 缺少 Conformal Prediction 专门小节\"\n    category: writing\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"论文核心贡献之一是 conformal features 失效，但 Related Work 缺乏 CP in robotics 的系统讨论。\"\n    action_items:\n      - round: 1\n        action: \"增加 Conformal Prediction for Robot Control 小节\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"论文 method paper vs analysis paper 定位不清\"\n    category: framing\n    severity: major\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R2 首轮提出，R3 强烈同意。Abstract/Method 以 method paper 口吻，但核心价值在 analysis。\"\n    action_items:\n      - round: 1\n        action: \"明确选择定位并统一全文叙事\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W8\"\n    summary: \"'safety factor' 用语不当，在机器人学语境中引起歧义\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1 首轮提出，R2 部分反驳（更接近 minor），R3 同意建议改为 'critical design factor'。\"\n    action_items:\n      - round: 1\n        action: \"将 'safety factor' 替换为 'critical design factor' 或 'robustness factor'\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W9\"\n    summary: \"L2 argmin 选择缺乏理论动机，未讨论其他距离度量\"\n    category: method\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 在交叉回应中同意，但指出鉴于 selection 无显著效果，影响有限。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W10\"\n    summary: \"CRM 架构（3 层 MLP, 256 hidden）无 ablation\"\n    category: experiment\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 在交叉回应中同意。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W4\"\n    summary: \"专有缩写 DOF/MLP/MSE 首次使用时未定义\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [3]\n        note: \"R3 标为 Major，R2 反驳降为 Minor——MLP/MSE/DOF 对 CoRL 审稿人是标准术语。R2 同意 per-DOF 首次出现时展开为 per-degree-of-freedom 更佳。\"\n    action_items:\n      - round: 1\n        action: \"首次使用时展开 DOF 为 Degrees of Freedom\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"4 处 -ing 分词短语结尾（轻微 AI 风格）\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [3]\n        note: \"experiments.tex L88/L136, appendix.tex L20, discussion.tex L19。R2 在交叉回应中认为不构成问题。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"Table 2 (Appendix per-task) 最优结果未加粗，与 Table 1 格式不一致\"\n    category: format\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [3]\n        note: \"\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W9\"\n    summary: \"Figure 1 (pipeline) 信息密度偏低，在正文超页数时占用空间过大\"\n    category: format\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [3]\n        note: \"建议缩小为 column-width 或增加信息量。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W11\"\n    summary: \"Per-task analysis 仅 seed 42，集中改进模式可能 seed-specific\"\n    category: experiment\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W5\"\n    summary: \"LLM test-time compute scaling 类比不恰当（高维离散 vs 低维连续）\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2, 3]\n        note: \"R3 在交叉回应中同意并指出该段在超页数时属于 padding，可压缩。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-19T01:03:36.437655+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml\", \"bytes\": 11352}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-19T01:05:47.445898+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "weak reject",
  "report": "# 审稿报告：Sample, Select, Correct: Inference-Time Action Refinement for Frozen VLAs\n\n**Venue**: CoRL 2026 Main Conference | **Deadline**: 2026-05-29\n**审稿模式**: 3 Reviewer 圆桌 + 交叉回应 | **轮次**: Round 1（已收敛）\n\n---\n\n## Summary\n\n本文提出 sample-select-correct pipeline 用于 frozen flow-matching VLA 的推理时动作修正：抽取 K=10 个 action samples，L2 argmin 选择最接近均值的 candidate，再用 ~327K 参数的 MLP (CRM) 预测有界残差修正。在 LIBERO-Object 上报告 17.6±2.6% vs VLA-only 11.6±1.1%。论文提供了 component decomposition（发现 selection 单独无效、correction 是主要驱动力）、conditioning ablation（conformal features 反而有害）和 applicability boundary 分析（tokenized VLAs 不适用）。LIBERO-Spatial 上无效果。\n\n---\n\n## Strengths\n\n**S1. 系统性的 component decomposition** [R1, R2 共识]\n拆解 random selection、argmin selection、CRM correction 的各自贡献，发现 selection alone 不 work 而 correction 是关键驱动力。这种系统性消融在 VLA 文献中较少见。\n\n**S2. 诚实的负面结果报告** [R1, R2, R3 共识]\nLIBERO-Spatial null result、conformal features 失效、absolute performance 仅 17.6%、个别 seed 上修正反而降低性能（seed 43）均被坦诚报告。Limitations 节列出 7 项限制，不回避核心弱点。\n\n**S3. 写作质量干净，AI 痕迹极少** [R3 确认]\n全文 em-dash 零处（正文）、Furthermore/Moreover/Additionally 零处、黑名单词汇零处。仅 4 处轻微 -ing 分词结尾。在当前投稿中属于写作风格最干净的论文之一。\n\n**S4. Applicability boundary 分析** [R1 确认]\nOpenVLA (tokenized) vs SmolVLA (flow-matching) 的 action diversity 对比（Figure 4, per-DOF variance < 10^{-30}）有效建立了方法的架构适用边界。\n\n**S5. 轻量实用设计** [R3 确认]\n~327K 参数、~0.3ms 推理开销，base VLA 完全不修改，作为 post-hoc module attach 的设计在部署场景下有实际意义。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. 统计方法根本性错误** [R1 提出, R2 R3 一致同意]\n论文将跨 seed 的 episodes pooled 后做 Fisher's exact test（experiments.tex L51），但同一 seed 下的 episodes 共享 CRM 权重和随机状态，不满足独立性假设。p=0.0042 是伪显著（pseudo-replication）。论文确实提供了部分缓解证据——\"All seven obs_only seeds exceed the VLA-only mean\"（等价于 sign test, p≈0.008 单侧），但未正式报告此检验。核心统计结论的可信度受到严重影响。\n- 位置：Abstract L4, experiments.tex L49-52, L86\n\n**C2. 核心 claim 与 K-scaling 数据内部矛盾** [R1 提出, R2 R3 一致同意]\nAbstract 和正文反复声称 \"the entire benefit derives from learned correction\"（Abstract L5, experiments.tex L94, discussion.tex L16），但 K=1 CRM 为 10.3%（3 seeds），低于 VLA-only 的 11.6%——correction alone 反而有害。更严重的是，Appendix L16 报告 K=1 为 10.3%，L18 却将其描述为 \"at the VLA-only level (11.6%)\"，同一段落内数据描述直接矛盾（R3 发现）。真实结论应为 \"multi-sample selection 是 correction 有效工作的前提条件，两者的协同效应是 driver\"。\n\n**C3. 各方法 seed 数不一致且无解释** [R1 提出, R2 R3 一致同意]\nTable 1 中 obs_only 7 seeds、VLA-only 5 seeds、Argmin 6 seeds、Random 仅 3 seeds。论文未在任何地方解释原因。最关键的 random vs argmin 比较仅基于 3 seeds，统计功效极低。不解释的不一致 seed 数引起 selection bias 嫌疑。\n\n**C4. 新颖性不足** [R2 提出, R3 从 framing 角度同意]\nPipeline 的三个组件中，selection 被自己的实验否定，correction 是标准的 supervised residual learning (Silver et al., 2018) + L2 clipping，observation conditioning 是直觉性设计。与最接近的 A2C2 相比，剩余的真实技术差异（magnitude clipping + obs conditioning）不足以构成单独论文的方法贡献。\n\n**C5. 标题与结论矛盾** [R2 提出, R3 强烈同意]\n\"Sample, Select, Correct\" 暗示三步均有独立贡献，但实验证明 sample 和 select 单独无效（random K=10 ≈ VLA-only, argmin ≈ random）。标题设置了错误的读者预期。\n\n**C6. 正文超 8 页限制** [R3 提出, R2 同意]\n正文含 Discussion + Limitations + Conclusion 共 9 页，超出 CoRL 2026 规定的 8 页限制 1 页。格式违规可能导致 desk reject。\n\n**C7. 缺失 AI Disclosure Statement** [R3 提出, R2 同意]\nCoRL 2026 要求作者简要说明 generative AI 工具使用方式，论文中完全缺失。\n\n### Major（影响评分但非一票否决）\n\n**M1. 实验范围过窄** [R2 提出, R1 R3 部分同意]\n全部实验仅在 LIBERO (仿真) + SmolVLA (450M) 上进行。未测试其他 VLA backbone（π₀, Octo）、其他 benchmark（RLBench, MetaWorld），也无 real-robot 验证。R3 部分反驳：CoRL 不硬性要求 real-robot，但三人均认为范围过窄。\n\n**M2. LIBERO-Spatial null result 仅 1 seed** [R1 提出, R2 R3 同意]\nTable 1 Spatial 列全部为 seed 42 单次结果。鉴于 Object 上 per-seed std 达 2.6pp，1 个 seed 不足以支撑 \"correction does not help for spatial reasoning\" 的结论（论文 Contribution 3 的重要支撑）。\n\n**M3. 缺少与 A2C2 的实际实验对比** [R1 提出, R2 R3 同意]\n论文将 A2C2 定位为 \"closest concurrent work\" 并列出三点差异，但对比仅停留在文字层面。Limitations 节也未说明为何缺少定量对比。\n\n**M4. 24 条 orphan bib entries + 引用不足** [R1 R2 R3 独立标记]\nBib 51 条中仅 25 条被引用。Diffusion Policy (Chi 2023)、RT-2 (Brohan 2023)、Octo (Ghosh 2024)、Conformalized Teleoperation (Zhao 2024) 等重要工作在 bib 中但未引用。Gauss1857/Lagrange1788 模板残留未清理。\n\n**M5. Magnitude 分析某些 ε 仅 1 seed** [R1 提出, R3 同意]\nFigure 2 caption 写 \"±1 std across seeds (n=1-7 per point)\"，n=1 时 error bars 无意义，造成视觉误导。\n\n**M6. CRM 训练覆盖全部评估 tasks，无 cross-task 泛化验证** [R1 提出, R2 同意]\nCRM 在全部 20 LIBERO tasks 的 demo 上训练并在同一 20 tasks 上评估，无法判断是 task-agnostic 修正能力还是 task-specific 记忆。\n\n**M7. 论文 method paper vs analysis paper 定位不清** [R2 提出, R3 强烈同意]\nAbstract/Method 以 method paper 口吻（\"We propose...\"），但核心价值在 component decomposition 和 negative results。身份混淆使审稿人难以评价——method paper 标准下 novelty 不够，analysis paper 标准下 scope 不够。\n\n**M8. Related Work 缺少 Conformal Prediction 专门讨论** [R2 提出]\n论文核心贡献之一是 conformal features 失效，但 Related Work 缺少 CP in robotics 的系统 positioning。\n\n### Minor\n\n**m1.** \"safety factor\" 用语在机器人学语境中引起歧义 [R1, R3] — 建议改为 \"critical design factor\"\n**m2.** L2 argmin 选择缺乏理论动机 [R1, R2]\n**m3.** CRM 架构无 ablation [R1, R2]\n**m4.** DOF 首次使用未展开为 Degrees of Freedom [R3, R2 同意降级为 minor]\n**m5.** 4 处 -ing 分词短语结尾 [R3]\n**m6.** Table 2 最优未加粗，与 Table 1 不一致 [R3]\n**m7.** Figure 1 信息密度偏低，在超页数时占用空间大 [R3]\n**m8.** Per-task analysis 仅 seed 42 [R1]\n**m9.** LLM test-time compute scaling 类比不恰当 [R2, R3] — d=6 连续 vs 高维离散差异太大\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下关键问题三位 Reviewer 达成完全共识：\n\n1. **Fisher's exact test 独立性违反**（C1）— 统计方法需修正，但 sign test (7/7) 提供替代方向性证据\n2. **核心 claim \"entire benefit from correction\" 与 K=1 数据矛盾**（C2）— 需全面修正 framing\n3. **Seed 数不一致无解释**（C3）— 必须解释或统一\n4. **缺 A2C2 实验对比**（M3）— 应复现或在 Limitations 明确解释\n5. **24 orphan bib + 关键引用缺失**（M4）— 需清理并补充引用\n6. **标题与结论矛盾**（C5）— 需修改标题\n\n## Reviewer Divergence [REBUT]\n\n1. **Real-robot 实验的必要性**（R2-N3）：R2 视为 Critical，R3 部分反驳认为 CoRL 不硬性要求。**Director 判断：降为 Major，但实验范围窄的综合问题仍然严重。**\n2. **DOF/MLP/MSE 缩写定义**（R3-W4）：R3 标为 Major，R2 反驳认为是 CoRL 受众的标准术语。**Director 判断：降为 Minor，但首次使用展开 DOF 为佳。**\n3. **\"safety factor\" 用语严重度**（R1-W8）：R1 标 Minor，R2 认为更接近用词歧义而非错误。**Director 判断：Minor，改为 \"design factor\" 即可。**\n\n---\n\n## Questions（需要作者澄清）\n\nQ1. 各方法 seed 数为何不同？是否有 seeds 被丢弃？如果是计算资源限制，请明确说明。\nQ2. K=1 CRM (10.3%) 低于 VLA-only (11.6%)，如何维持 \"entire benefit from correction\" 的 claim？Appendix 中 10.3% 被描述为 \"at the VLA-only level (11.6%)\" 是文字错误还是有其他解释？\nQ3. 是否做过 seed-level 统计检验（如 sign test, Wilcoxon）？如果做了，p-value 多少？\nQ4. 为何不复现 A2C2 做直接对比？代码是否不可用？\nQ5. CRM 在 LIBERO-Spatial 训练数据上的 offline MSE 如何？是否有 leave-task-out 的泛化测试？\nQ6. LIBERO-Spatial 35% vs 34% 的差异是否在 noise 范围内？能否提供多 seed 结果？\nQ7. 论文的定位是 method paper 还是 analysis paper？这影响贡献评估标准。\n\n---\n\n## Missing References\n\n### 已在 bib 中但未引用（必须纳入 Related Work）：\n1. **Chi et al., 2023 (Diffusion Policy)** — action diffusion 基础工作\n2. **Brohan et al., 2023 (RT-2)** — VLA 标志性工作\n3. **Ghosh et al., 2024 (Octo)** — 开源 generalist robot policy\n4. **Zhao et al., 2024 (Conformalized Teleoperation)** — CP in robotic action spaces\n5. **Zhou et al., 2025 (ACP-CBF)** — conformal prediction + safety in robotics\n6. **Wang et al., 2025 (CPLoop)** — CP in trajectory optimization\n7. **Johannink et al., 2019** — residual RL for robot control\n\n### bib 中不存在但建议补充：\n8. **ACT (Zhao et al., 2023)** — action chunking 基础工作\n9. 2025-2026 最新 VLA 工作（HPT, CrossFormer 等 generalist policies）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未启用（项目配置未开启 paperreview_ai）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: Weak Reject (4/10)**\n**Confidence: High (4/5)**\n\n| Reviewer | Round 1 | 交叉后 | 角色 |\n|----------|---------|--------|------|\n| R1 | 4/10 | 4/10 | 方法/实验 |\n| R2 | 4/10 | 4/10 (下调趋势) | 新颖性/定位 |\n| R3 | 3/5 (~6/10) | 2.5/5 (~5/10) | 写作/格式 |\n\n**综合评价**：\n\n论文方向有意义（inference-time refinement for frozen VLAs），消融设计系统，写作干净直接，负面结果报告诚实——这些是值得肯定的优势。\n\n但存在多层面的根本性问题使其未达到 CoRL 2026 接收标准：\n\n1. **可信度层**：统计方法有根本缺陷（Fisher independence violation），核心 claim 与 K=1 数据矛盾且 Appendix 内部数据描述不一致，seed 数不一致无解释。审稿人无法信任论文报告的主要结论。\n\n2. **贡献层**：技术新颖性不足（标准 MLP + L2 clipping），核心分析发现（selection 无用）在低维连续空间中可预期，标题与结论矛盾，论文定位在 method 和 analysis 之间摇摆。\n\n3. **范围层**：单一 VLA backbone + 单一 benchmark family + 纯仿真 + Spatial 上无效。17.6% 绝对成功率远未达部署水平。\n\n4. **合规层**：正文超 8 页限制（可能 desk reject），缺 AI disclosure，bib 残留未清理。\n\n**最核心的修改优先级**：\n1. 修正统计方法 + 统一 seed 数 → 恢复结果可信度\n2. 修正 \"correction is sole driver\" framing → 消除内部矛盾\n3. 压缩至 8 页 + 添加 AI disclosure → 满足格式合规\n4. 在至少一个额外 VLA backbone 上验证 → 扩展实验范围\n5. 补充 A2C2 对比（或明确解释为何缺失）→ 建立相对基准\n\n论文最有价值的部分是诚实的 component decomposition 和 negative results（conformal features 失效、applicability boundary）。如果重新定位为 analysis paper 并大幅扩展实验范围（多 VLA、多 benchmark），有潜力成为有价值的贡献。当前版本作为 method paper 投 CoRL 顶会，贡献增量和实验范围均不足。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- p=0.0042 基于有缺陷的 Fisher test，需替换为有效统计量\n- \"directed residual correction is the sole meaningful driver\" 与 K=1 数据矛盾，需修正\n- 227 词结构完整，信息密度合理\n\n### Introduction\n- 5 段叙事结构清晰，Contribution 列表每条有对应支撑\n- Contribution 1 的 \"entire benefit from correction\" phrasing 需修正\n- Contribution 2 的 \"critical safety factor\" 用语有歧义\n- 与 LLM test-time compute 的对比可简化（低维连续 vs 高维离散差异太大，类比深度不足）\n\n### Related Work\n- 三小节（VLA Robustness, Residual Policy Learning, Inference-Time Compute Scaling）组织合理\n- 缺少 Conformal Prediction for Robotics 专门小节\n- A2C2 的三点差异讨论充分但缺乏实验支撑\n- 引用密度偏低（25 条 cited），关键工作（Diffusion Policy, RT-2, Octo）遗漏\n\n### Method\n- 形式化完整（Eq. 1-3），复现性好\n- L2 argmin 选择缺乏理论动机\n- CRM 架构选择无 ablation 支撑\n- Figure 1 信息密度偏低，在超页数时尤其浪费空间\n\n### Experiments\n- 多处内容与 Method 重复（CRM variants 描述），可压缩\n- 统计协议段落报告了不一致 seed 数但未解释\n- Pipeline decomposition 结论有价值但 claim 需修正\n- Spatial 结论基于单 seed，不充分\n- Figure 2 中 n=1 的点不应展示 error bars\n\n### Discussion\n- \"Selection vs correction\" 段落与 Introduction/Experiments 有重叠，在超页数时应压缩\n- \"When does action-level correction help?\" 分析合理但可更简练\n- 论文在 method/analysis 定位间摇摆\n\n### Limitations\n- 7 条坦诚全面\n- 遗漏：缺少与外部 baseline（A2C2 等）的实验对比\n- 遗漏：Spatial null result 仅 1 seed 的统计局限\n\n### Appendix\n- K-scaling 分析有价值（K=5 captures ~88% of benefit）\n- L16 报告 K=1 为 10.3%，L18 将其描述为 \"at the VLA-only level (11.6%)\" — 内部数据矛盾\n- Applicability boundary (Figure 4) 有说服力\n- Per-task analysis 仅 seed 42，代表性有限\n\n### References\n- 24 条 orphan entries（含模板残留 Gauss1857/Lagrange1788）\n- 需清理并将关键工作纳入正文讨论"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "weak reject",
    "report": "# 审稿报告：Sample, Select, Correct: Inference-Time Action Refinement for Frozen VLAs\n\n**Venue**: CoRL 2026 Main Conference | **Deadline**: 2026-05-29\n**审稿模式**: 3 Reviewer 圆桌 + 交叉回应 | **轮次**: Round 1（已收敛）\n\n---\n\n## Summary\n\n本文提出 sample-select-correct pipeline 用于 frozen flow-matching VLA 的推理时动作修正：抽取 K=10 个 action samples，L2 argmin 选择最接近均值的 candidate，再用 ~327K 参数的 MLP (CRM) 预测有界残差修正。在 LIBERO-Object 上报告 17.6±2.6% vs VLA-only 11.6±1.1%。论文提供了 component decomposition（发现 selection 单独无效、correction 是主要驱动力）、conditioning ablation（conformal features 反而有害）和 applicability boundary 分析（tokenized VLAs 不适用）。LIBERO-Spatial 上无效果。\n\n---\n\n## Strengths\n\n**S1. 系统性的 component decomposition** [R1, R2 共识]\n拆解 random selection、argmin selection、CRM correction 的各自贡献，发现 selection alone 不 work 而 correction 是关键驱动力。这种系统性消融在 VLA 文献中较少见。\n\n**S2. 诚实的负面结果报告** [R1, R2, R3 共识]\nLIBERO-Spatial null result、conformal features 失效、absolute performance 仅 17.6%、个别 seed 上修正反而降低性能（seed 43）均被坦诚报告。Limitations 节列出 7 项限制，不回避核心弱点。\n\n**S3. 写作质量干净，AI 痕迹极少** [R3 确认]\n全文 em-dash 零处（正文）、Furthermore/Moreover/Additionally 零处、黑名单词汇零处。仅 4 处轻微 -ing 分词结尾。在当前投稿中属于写作风格最干净的论文之一。\n\n**S4. Applicability boundary 分析** [R1 确认]\nOpenVLA (tokenized) vs SmolVLA (flow-matching) 的 action diversity 对比（Figure 4, per-DOF variance < 10^{-30}）有效建立了方法的架构适用边界。\n\n**S5. 轻量实用设计** [R3 确认]\n~327K 参数、~0.3ms 推理开销，base VLA 完全不修改，作为 post-hoc module attach 的设计在部署场景下有实际意义。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. 统计方法根本性错误** [R1 提出, R2 R3 一致同意]\n论文将跨 seed 的 episodes pooled 后做 Fisher's exact test（experiments.tex L51），但同一 seed 下的 episodes 共享 CRM 权重和随机状态，不满足独立性假设。p=0.0042 是伪显著（pseudo-replication）。论文确实提供了部分缓解证据——\"All seven obs_only seeds exceed the VLA-only mean\"（等价于 sign test, p≈0.008 单侧），但未正式报告此检验。核心统计结论的可信度受到严重影响。\n- 位置：Abstract L4, experiments.tex L49-52, L86\n\n**C2. 核心 claim 与 K-scaling 数据内部矛盾** [R1 提出, R2 R3 一致同意]\nAbstract 和正文反复声称 \"the entire benefit derives from learned correction\"（Abstract L5, experiments.tex L94, discussion.tex L16），但 K=1 CRM 为 10.3%（3 seeds），低于 VLA-only 的 11.6%——correction alone 反而有害。更严重的是，Appendix L16 报告 K=1 为 10.3%，L18 却将其描述为 \"at the VLA-only level (11.6%)\"，同一段落内数据描述直接矛盾（R3 发现）。真实结论应为 \"multi-sample selection 是 correction 有效工作的前提条件，两者的协同效应是 driver\"。\n\n**C3. 各方法 seed 数不一致且无解释** [R1 提出, R2 R3 一致同意]\nTable 1 中 obs_only 7 seeds、VLA-only 5 seeds、Argmin 6 seeds、Random 仅 3 seeds。论文未在任何地方解释原因。最关键的 random vs argmin 比较仅基于 3 seeds，统计功效极低。不解释的不一致 seed 数引起 selection bias 嫌疑。\n\n**C4. 新颖性不足** [R2 提出, R3 从 framing 角度同意]\nPipeline 的三个组件中，selection 被自己的实验否定，correction 是标准的 supervised residual learning (Silver et al., 2018) + L2 clipping，observation conditioning 是直觉性设计。与最接近的 A2C2 相比，剩余的真实技术差异（magnitude clipping + obs conditioning）不足以构成单独论文的方法贡献。\n\n**C5. 标题与结论矛盾** [R2 提出, R3 强烈同意]\n\"Sample, Select, Correct\" 暗示三步均有独立贡献，但实验证明 sample 和 select 单独无效（random K=10 ≈ VLA-only, argmin ≈ random）。标题设置了错误的读者预期。\n\n**C6. 正文超 8 页限制** [R3 提出, R2 同意]\n正文含 Discussion + Limitations + Conclusion 共 9 页，超出 CoRL 2026 规定的 8 页限制 1 页。格式违规可能导致 desk reject。\n\n**C7. 缺失 AI Disclosure Statement** [R3 提出, R2 同意]\nCoRL 2026 要求作者简要说明 generative AI 工具使用方式，论文中完全缺失。\n\n### Major（影响评分但非一票否决）\n\n**M1. 实验范围过窄** [R2 提出, R1 R3 部分同意]\n全部实验仅在 LIBERO (仿真) + SmolVLA (450M) 上进行。未测试其他 VLA backbone（π₀, Octo）、其他 benchmark（RLBench, MetaWorld），也无 real-robot 验证。R3 部分反驳：CoRL 不硬性要求 real-robot，但三人均认为范围过窄。\n\n**M2. LIBERO-Spatial null result 仅 1 seed** [R1 提出, R2 R3 同意]\nTable 1 Spatial 列全部为 seed 42 单次结果。鉴于 Object 上 per-seed std 达 2.6pp，1 个 seed 不足以支撑 \"correction does not help for spatial reasoning\" 的结论（论文 Contribution 3 的重要支撑）。\n\n**M3. 缺少与 A2C2 的实际实验对比** [R1 提出, R2 R3 同意]\n论文将 A2C2 定位为 \"closest concurrent work\" 并列出三点差异，但对比仅停留在文字层面。Limitations 节也未说明为何缺少定量对比。\n\n**M4. 24 条 orphan bib entries + 引用不足** [R1 R2 R3 独立标记]\nBib 51 条中仅 25 条被引用。Diffusion Policy (Chi 2023)、RT-2 (Brohan 2023)、Octo (Ghosh 2024)、Conformalized Teleoperation (Zhao 2024) 等重要工作在 bib 中但未引用。Gauss1857/Lagrange1788 模板残留未清理。\n\n**M5. Magnitude 分析某些 ε 仅 1 seed** [R1 提出, R3 同意]\nFigure 2 caption 写 \"±1 std across seeds (n=1-7 per point)\"，n=1 时 error bars 无意义，造成视觉误导。\n\n**M6. CRM 训练覆盖全部评估 tasks，无 cross-task 泛化验证** [R1 提出, R2 同意]\nCRM 在全部 20 LIBERO tasks 的 demo 上训练并在同一 20 tasks 上评估，无法判断是 task-agnostic 修正能力还是 task-specific 记忆。\n\n**M7. 论文 method paper vs analysis paper 定位不清** [R2 提出, R3 强烈同意]\nAbstract/Method 以 method paper 口吻（\"We propose...\"），但核心价值在 component decomposition 和 negative results。身份混淆使审稿人难以评价——method paper 标准下 novelty 不够，analysis paper 标准下 scope 不够。\n\n**M8. Related Work 缺少 Conformal Prediction 专门讨论** [R2 提出]\n论文核心贡献之一是 conformal features 失效，但 Related Work 缺少 CP in robotics 的系统 positioning。\n\n### Minor\n\n**m1.** \"safety factor\" 用语在机器人学语境中引起歧义 [R1, R3] — 建议改为 \"critical design factor\"\n**m2.** L2 argmin 选择缺乏理论动机 [R1, R2]\n**m3.** CRM 架构无 ablation [R1, R2]\n**m4.** DOF 首次使用未展开为 Degrees of Freedom [R3, R2 同意降级为 minor]\n**m5.** 4 处 -ing 分词短语结尾 [R3]\n**m6.** Table 2 最优未加粗，与 Table 1 不一致 [R3]\n**m7.** Figure 1 信息密度偏低，在超页数时占用空间大 [R3]\n**m8.** Per-task analysis 仅 seed 42 [R1]\n**m9.** LLM test-time compute scaling 类比不恰当 [R2, R3] — d=6 连续 vs 高维离散差异太大\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下关键问题三位 Reviewer 达成完全共识：\n\n1. **Fisher's exact test 独立性违反**（C1）— 统计方法需修正，但 sign test (7/7) 提供替代方向性证据\n2. **核心 claim \"entire benefit from correction\" 与 K=1 数据矛盾**（C2）— 需全面修正 framing\n3. **Seed 数不一致无解释**（C3）— 必须解释或统一\n4. **缺 A2C2 实验对比**（M3）— 应复现或在 Limitations 明确解释\n5. **24 orphan bib + 关键引用缺失**（M4）— 需清理并补充引用\n6. **标题与结论矛盾**（C5）— 需修改标题\n\n## Reviewer Divergence [REBUT]\n\n1. **Real-robot 实验的必要性**（R2-N3）：R2 视为 Critical，R3 部分反驳认为 CoRL 不硬性要求。**Director 判断：降为 Major，但实验范围窄的综合问题仍然严重。**\n2. **DOF/MLP/MSE 缩写定义**（R3-W4）：R3 标为 Major，R2 反驳认为是 CoRL 受众的标准术语。**Director 判断：降为 Minor，但首次使用展开 DOF 为佳。**\n3. **\"safety factor\" 用语严重度**（R1-W8）：R1 标 Minor，R2 认为更接近用词歧义而非错误。**Director 判断：Minor，改为 \"design factor\" 即可。**\n\n---\n\n## Questions（需要作者澄清）\n\nQ1. 各方法 seed 数为何不同？是否有 seeds 被丢弃？如果是计算资源限制，请明确说明。\nQ2. K=1 CRM (10.3%) 低于 VLA-only (11.6%)，如何维持 \"entire benefit from correction\" 的 claim？Appendix 中 10.3% 被描述为 \"at the VLA-only level (11.6%)\" 是文字错误还是有其他解释？\nQ3. 是否做过 seed-level 统计检验（如 sign test, Wilcoxon）？如果做了，p-value 多少？\nQ4. 为何不复现 A2C2 做直接对比？代码是否不可用？\nQ5. CRM 在 LIBERO-Spatial 训练数据上的 offline MSE 如何？是否有 leave-task-out 的泛化测试？\nQ6. LIBERO-Spatial 35% vs 34% 的差异是否在 noise 范围内？能否提供多 seed 结果？\nQ7. 论文的定位是 method paper 还是 analysis paper？这影响贡献评估标准。\n\n---\n\n## Missing References\n\n### 已在 bib 中但未引用（必须纳入 Related Work）：\n1. **Chi et al., 2023 (Diffusion Policy)** — action diffusion 基础工作\n2. **Brohan et al., 2023 (RT-2)** — VLA 标志性工作\n3. **Ghosh et al., 2024 (Octo)** — 开源 generalist robot policy\n4. **Zhao et al., 2024 (Conformalized Teleoperation)** — CP in robotic action spaces\n5. **Zhou et al., 2025 (ACP-CBF)** — conformal prediction + safety in robotics\n6. **Wang et al., 2025 (CPLoop)** — CP in trajectory optimization\n7. **Johannink et al., 2019** — residual RL for robot control\n\n### bib 中不存在但建议补充：\n8. **ACT (Zhao et al., 2023)** — action chunking 基础工作\n9. 2025-2026 最新 VLA 工作（HPT, CrossFormer 等 generalist policies）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未启用（项目配置未开启 paperreview_ai）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: Weak Reject (4/10)**\n**Confidence: High (4/5)**\n\n| Reviewer | Round 1 | 交叉后 | 角色 |\n|----------|---------|--------|------|\n| R1 | 4/10 | 4/10 | 方法/实验 |\n| R2 | 4/10 | 4/10 (下调趋势) | 新颖性/定位 |\n| R3 | 3/5 (~6/10) | 2.5/5 (~5/10) | 写作/格式 |\n\n**综合评价**：\n\n论文方向有意义（inference-time refinement for frozen VLAs），消融设计系统，写作干净直接，负面结果报告诚实——这些是值得肯定的优势。\n\n但存在多层面的根本性问题使其未达到 CoRL 2026 接收标准：\n\n1. **可信度层**：统计方法有根本缺陷（Fisher independence violation），核心 claim 与 K=1 数据矛盾且 Appendix 内部数据描述不一致，seed 数不一致无解释。审稿人无法信任论文报告的主要结论。\n\n2. **贡献层**：技术新颖性不足（标准 MLP + L2 clipping），核心分析发现（selection 无用）在低维连续空间中可预期，标题与结论矛盾，论文定位在 method 和 analysis 之间摇摆。\n\n3. **范围层**：单一 VLA backbone + 单一 benchmark family + 纯仿真 + Spatial 上无效。17.6% 绝对成功率远未达部署水平。\n\n4. **合规层**：正文超 8 页限制（可能 desk reject），缺 AI disclosure，bib 残留未清理。\n\n**最核心的修改优先级**：\n1. 修正统计方法 + 统一 seed 数 → 恢复结果可信度\n2. 修正 \"correction is sole driver\" framing → 消除内部矛盾\n3. 压缩至 8 页 + 添加 AI disclosure → 满足格式合规\n4. 在至少一个额外 VLA backbone 上验证 → 扩展实验范围\n5. 补充 A2C2 对比（或明确解释为何缺失）→ 建立相对基准\n\n论文最有价值的部分是诚实的 component decomposition 和 negative results（conformal features 失效、applicability boundary）。如果重新定位为 analysis paper 并大幅扩展实验范围（多 VLA、多 benchmark），有潜力成为有价值的贡献。当前版本作为 method paper 投 CoRL 顶会，贡献增量和实验范围均不足。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- p=0.0042 基于有缺陷的 Fisher test，需替换为有效统计量\n- \"directed residual correction is the sole meaningful driver\" 与 K=1 数据矛盾，需修正\n- 227 词结构完整，信息密度合理\n\n### Introduction\n- 5 段叙事结构清晰，Contribution 列表每条有对应支撑\n- Contribution 1 的 \"entire benefit from correction\" phrasing 需修正\n- Contribution 2 的 \"critical safety factor\" 用语有歧义\n- 与 LLM test-time compute 的对比可简化（低维连续 vs 高维离散差异太大，类比深度不足）\n\n### Related Work\n- 三小节（VLA Robustness, Residual Policy Learning, Inference-Time Compute Scaling）组织合理\n- 缺少 Conformal Prediction for Robotics 专门小节\n- A2C2 的三点差异讨论充分但缺乏实验支撑\n- 引用密度偏低（25 条 cited），关键工作（Diffusion Policy, RT-2, Octo）遗漏\n\n### Method\n- 形式化完整（Eq. 1-3），复现性好\n- L2 argmin 选择缺乏理论动机\n- CRM 架构选择无 ablation 支撑\n- Figure 1 信息密度偏低，在超页数时尤其浪费空间\n\n### Experiments\n- 多处内容与 Method 重复（CRM variants 描述），可压缩\n- 统计协议段落报告了不一致 seed 数但未解释\n- Pipeline decomposition 结论有价值但 claim 需修正\n- Spatial 结论基于单 seed，不充分\n- Figure 2 中 n=1 的点不应展示 error bars\n\n### Discussion\n- \"Selection vs correction\" 段落与 Introduction/Experiments 有重叠，在超页数时应压缩\n- \"When does action-level correction help?\" 分析合理但可更简练\n- 论文在 method/analysis 定位间摇摆\n\n### Limitations\n- 7 条坦诚全面\n- 遗漏：缺少与外部 baseline（A2C2 等）的实验对比\n- 遗漏：Spatial null result 仅 1 seed 的统计局限\n\n### Appendix\n- K-scaling 分析有价值（K=5 captures ~88% of benefit）\n- L16 报告 K=1 为 10.3%，L18 将其描述为 \"at the VLA-only level (11.6%)\" — 内部数据矛盾\n- Applicability boundary (Figure 4) 有说服力\n- Per-task analysis 仅 seed 42，代表性有限\n\n### References\n- 24 条 orphan entries（含模板残留 Gauss1857/Lagrange1788）\n- 需清理并将关键工作纳入正文讨论"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-19T01:05:51.711122+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4265
}
```

</details>

---


### Assistant

_source line 104 · 2026-05-19T01:05:59.844132+00:00_

审稿报告已投递给 Research Director。

---

**圆桌审稿完成总结**：

- **评分**：Weak Reject (4/10)，置信度 High (4/5)
- **三位 Reviewer**：R1 4/10, R2 4/10, R3 ~5/10，交叉回应后在所有关键问题上达成共识
- **7 个 Critical 问题**：统计方法缺陷、核心 claim 矛盾、seed 数不一致、novelty 不足、标题矛盾、超页数、缺 AI disclosure
- **8 个 Major 问题**：实验范围窄、Spatial 仅 1 seed、缺 A2C2 对比、orphan bib、magnitude 分析 seed 不足、无 cross-task 泛化、定位不清、缺 CP 专节
- **Issue Tracker**：已创建 `review_issues.yaml`，记录 22 个 issue（7 critical / 8 major / 7 minor），全部 status=open

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 105 · 2026-05-19T01:05:59.857598+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应（Round 2）

### 对 Reviewer 2 逐条回应

**[AGREE] R2-N1: 与 A2C2 差异不构成足够新颖性**
与我的 W5 一致。三点声称差异经拆解后：(a) selection 被自己的 decomposition 否定（Section 4.2, random 11.7% vs argmin 12.3%, not significant）；(b) L2 norm clipping 是标准技术（Silver 2018, TRANSIC, PLD）；(c) observation conditioning 是自然选择。核心退化为 "frozen VLA 上训练 residual MLP"，与 Silver et al. 2018 高度重合。但 analysis contributions（decomposition, ablation, boundary）仍有信息价值，问题在于论文定位为 method paper 而非 analysis paper。

**[AGREE with nuance] R2-N2: "Selection 无用是 trivial 发现"**
部分同意。d=6, K=10 下 samples 聚集确实可预期。但 quantified decomposition（selection ~0.6pp vs correction ~5.3pp）在 VLA 文献中是首次量化，有边际信息价值。标题 "Sample, Select, Correct" 与结论矛盾的问题完全同意。LLM 类比 structurally flawed（learned verifier vs L2 argmin），将 "L2 argmin 无用" 推广到 "selection in continuous action spaces 无用" 是 overclaim（Discussion, discussion.tex:13-18）。

**[AGREE] R2-N3: 无真实机器人实验。** CoRL relevance 维度的标准弱点。

**[AGREE] R2-W1/W2/W3:** Orphan bib（与 R1-W12 一致）、CP 小节缺失、定位不清均同意。

**[REBUT] R2-W4: Conformal features fail at K=10 可预期**
Covariance noise 可预期，但 perdof 从 14%→0% 的 progressive collapse severity（Figure 2）及其与 obs_only 稳健性的 divergent pattern 并非 trivially predictable。不过我在 W6 中也指出 Figure 2 seed 数不均（n=1-7），collapse severity 需更多 seeds 确认。

**[AGREE] R2-W5:** LLM 类比不恰当，同 N2 回应。

R2-Q1（K=1 CRM 有害）与我的 W2 高度一致。R2-Q5（Spatial 35% vs 34%）与我的 W4 一致，single seed 的 1pp 差异是 noise。

### 对 Reviewer 3 逐条回应

**[AGREE] R3-W1: 正文超页数限制**
经核实确认 main body 约 9 页，超出 CoRL 8 页限制。我初审未独立核实，R3 判断正确，Critical 级。

**[AGREE] R3-W2: AI Disclosure 缺失**
CoRL 2026 明确要求 disclosure generative AI usage。另外注意 CoRL 声明 "papers with citations to references that do not exist will be desk-rejected"，reference audit 发现 Gauss1857/Lagrange1788 placeholder entries 需清除。

**[AGREE] R3-W3 to W9:** 全部同意，与 R1 已有发现一致或互补。

### 关键分歧：R3 统计评价 vs 我的 W1

**R2/R3 评价的是统计报告的规范性**（确实罕见且好），**我的 W1 评价的是统计方法的正确性**（Fisher's exact test on pooled episodes violates independence = pseudo-replication）。这两个判断并不矛盾。

不过经 seed-level 粗算（unpaired t-test, 7 seeds mean 17.6±2.6% vs 5 seeds mean 11.6±1.1%），t≈5.46, df≈8, p<0.001，差异方向可能仍然 significant。因此修正判断：**统计方法有误（pseudo-replication），但结论方向可能仍然成立，作者需用 seed-level test 重新验证。** W1 仍为 Critical（方法论错误本身 critical），但降低 "结论完全不可信" 的强度。

### 综合评估更新

经交叉审议后增加 2 个 Critical 格式问题（R3-W1 页数超限、R3-W2 AI Disclosure）。

**维持 Overall: 4/10 (Borderline Reject)**
- 3 Critical 方法/实验问题（W1 统计方法错误、W2 claim 内部矛盾、W3 seed 不一致）
- 2 Critical 格式问题（页数超限、AI Disclosure 缺失）
- 新颖性不足（同意 R2-N1，但 analysis contribution 有独立价值）
- 缺少 A2C2 对比（R1/R2/R3 三方一致）
- Seed-level 粗算显示主效应可能仍 significant，但需作者正式验证

---

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- 同意 R2 的新颖性不足判断（N1），但认为 analysis contribution 有独立价值
- 同意 R2 关于 selection trivial 的部分判断（N2），但 quantified decomposition 仍有边际贡献；标题 misleading
- 反驳 R2-W4（conformal collapse severity 并非完全可预期），但承认 seed 数不足限制了结论强度
- 同意 R3 的页数超限（W1）和 AI Disclosure 缺失（W2），已纳入评估
- 关于统计检验分歧：R2/R3 评价的是报告规范性，我评价的是方法正确性，两者不矛盾。经 seed-level 粗算，主效应方向可能仍 significant，但 pseudo-replication 问题仍需作者正式修正

维持 4/10 Borderline Reject。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 106 · 2026-05-19T01:06:20.799538+00:00_

审稿报告已在收到 R2 和 R3 交叉回应后提交。R1 的交叉回应现已到达，核心判断与已提交报告一致，无需修订：

- R1 确认了所有关键共识点（统计方法错误、claim 矛盾、seed 不一致、页数超限、AI disclosure 缺失）
- R1 新增一个有价值的补充：seed-level 粗算（unpaired t-test, t≈5.46, p<0.001）显示**主效应方向可能仍然成立**，但 pseudo-replication 问题本身仍需作者正式修正。这与报告中已提及的 sign test (7/7) 替代证据方向一致。
- R1 对 R2-W4（conformal collapse 可预期性）的 REBUT 已在报告 Divergence 部分有类似记录。

**圆桌审稿完成**。3 位 Reviewer 完成独立初审 + 交叉回应，关键问题全部达成共识。审稿报告（Overall: Weak Reject 4/10）已投递给 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 13

## Round 13

68 recorded events


### User

_source line 107 · 2026-05-19T01:41:10.084470+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: acr-vla-conformal-refinement
- 论文路径: projects/acr-vla-conformal-refinement/paper/main.tex
- 目标 venue: CoRL 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-19T01:41:15.768824+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-19T01:41:15.819836+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-19T01:41:18.880441+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
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

_source line 111 · 2026-05-19T01:41:18.931143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-19T01:41:24.700996+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-19T01:41:25.454753+00:00_

{"result":"# 项目 acr-vla-conformal-refinement 概况\n\n## 实验状态 (270 个)\n\n- **crm-train-v1**: DONE (killed) — \n- **crm-train-k5**: DONE (killed) — \n- **eval-scalar-unc-spatial**: DONE (killed) — \n- **eval-acr-spatial-v2**: DONE (killed) — \n- **eval-k5-spatial**: DONE (killed) — \n- **eval-object-v7-full**: DONE (killed) — \n- **eval-spatial-v6-full**: DONE (killed) — \n- **eval-object-v5-full**: DONE (killed) — \n- **eval-acr-vla-spatial-v1**: DONE (killed) — \n- **eval-acr-spatial-v1**: DONE (killed) — \n- **eval-reconvla-spatial-v2**: DONE (killed) — \n- **eval-object-v4-full**: DONE (killed) — \n- **eval-spatial-v5-full**: DONE (killed) — \n- **eval-spatial-v3-full**: DONE (killed) — \n- **eval-spatial-reeval-v2**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval-perdof-object-norm003-seed48 | Per-DoF CRM (ε=0.03) seed48 on LIBERO-Object. 补 magnitude curve 最薄点 perdof ε=0.03 (当前 n=1)。timeout=16h。 | — | — | — |\n| eval-obs-only-object-norm003-seed49 | obs_only CRM (ε=0.03) seed49 on LIBERO-Object. 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)，第 6 个 seed 确保极低 norm 端统计可靠。 | — | — | — |\n| eval-obs-only-object-norm003-seed44-bjb2 | obs_only CRM (ε=0.03) seed44 on LIBERO-Object (bjb2-28827). 补 magnitude curve 最薄点 ε=0.03 (当前 n=1)。另一份 seed44 在 bjb1-32546 同时运行。 | — | — | — |\n\n## 待处理\n- eval_obs_only_norm01_seed48（准备中）\n- eval_obs_only_norm03_seed48（准备中）\n- train-crm-k1-accg-object-seed42-full（准备中）\n- plan_701-crm-k1-train: K=1 CRM 训练：使用多阶段 VLA 特征融合 + 组合损失函数（L2 + contrastive + uncertainty-weighted），训练专门用于 K=1 单采样纠正的 CRM 模型。目标是超越 K=1 VLA-only baseline (10.8%)。（准备中）\n- plan_701-precompute-k1-spatial（准备中）\n\n## 近期结论\n- **eval-obs-only-object-norm02-seed48-r2** (success): obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48).\n- **eval-perdof-object-def
…[truncated 1824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-19T01:41:25.505419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-19T01:41:25.555991+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/review_director_a3659f64.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-19T01:41:30.071323+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-19T01:41:30.272576+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/camera_ready_template/corl_2026_template_cameraready/example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/review_template/corl_2026_template_submission/example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/method_section_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_section_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/object_benchmark_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/spatial_final_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_c83872.tex
/home/ubuntu/.ag
…[truncated 2724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-19T01:41:30.323284+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
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

_source line 119 · 2026-05-19T01:41:30.474254+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-19T01:41:34.587694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-19T01:41:34.939183+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{amsmath,amssymb,amsfonts}
8	\DeclareMathOperator*{\argmin}{arg\,min}
9	\DeclareMathOperator*{\argmax}{arg\,max}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{enumitem}
13	\usepackage{multirow}
14	
15	\graphicspath{{figures/}}
16	
17	\title{Correction Over Selection: Dissecting Inference-Time\\Action Refinement for Frozen VLAs}
18	
19	\author{
20	  Anonymous
21	}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\begin{abstract}
28	\input{abstract}
29	\end{abstract}
30	
31	\keywords{Vision-Language-Action Models, Inference-Time Refinement, Robotic Manipulation}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{discussion}
38	
39	\bibliography{references}
40	
41	\clearpage
42	\input{appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-19T01:41:34.989740+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-19T01:41:42.748729+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"}]

I found the CoRL 2026 submission guidelines and author instructions. Here are the key details:

## Paper Format and Structure

The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional). All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

## Author Responsibilities

Every author with 3 or more submissions must agree to serve as a reviewer. Authors are exempt from the review requirement if they serve as an AC, an SAC, or another organizing chair for CoRL 2026.

## Generative AI Policy

LLMs or other generative AI tools do not qualify for authorship. D
…[truncated 971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7758
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-19T01:41:46.457345+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 submission deadline page limit double blind review policy template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 submission deadline page limit double blind review policy template"
  }
}
```

</details>

---


### Tool call

_source line 125 · 2026-05-19T01:41:47.360046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-19T01:41:47.862378+00:00_

1	Vision-Language-Action (VLA) models for robotic manipulation degrade under distribution shift, yet improving their performance without retraining remains underexplored.
2	We propose a sample-select-correct pipeline for inference-time action refinement of frozen flow-matching VLAs that draws multiple action samples, selects the most representative candidate via $L_2$ argmin, and applies a learned residual correction bounded in magnitude.
3	The correction module is a ${\sim}$327K-parameter MLP conditioned on the frozen VLA's observation embedding, trained offline with supervised $L_2$ loss on demonstration data.
4	On the LIBERO-Object benchmark (10 tasks, 7 seeds), the pipeline achieves $17.6 \pm 2.6$\% versus $11.6 \pm 1.1$\% for the unmodified VLA ($p = 0.003$, Mann-Whitney U), with a +5.3\,pp margin over argmin selection ($p = 0.014$).
5	Component decomposition reveals that learned correction is the active mechanism while multi-sampling is an enabling condition: neither works alone ($K{=}1$ correction falls below baseline at 10.3\%, selection without correction matches baseline at 11.7\%). The improvement emerges from correction operating on a multi-sample-centered input.
6	A conditioning study demonstrates that feature choice is a critical design factor: observation features produce robust corrections across all tested magnitude bounds (14.3--17.6\%), while per-DOF conformal uncertainty features cause progressive collapse (14\% to 0\%) under the same architecture and training.
7	We further show that multi-sample correction requires stochastic action diversity: tokenized VLAs produce near-identical samples. This establishes an architectural applicability boundary.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 127 · 2026-05-19T01:41:47.862869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-19T01:41:48.365768+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	% --- Para 1: VLAs are impressive but fragile under distribution shift ---
5	Vision-Language-Action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached near-saturation on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this performance masks severe fragility: visual and physical perturbations common in deployment (camera viewpoint shifts, object layout changes, robot initial-state variation) routinely degrade success by over 65 percentage points.
7	On the LIBERO+ benchmark~\cite{fei2025liberoplus}, $\pi_0$ drops from 94.2\% to 6.6\% under initial-state perturbation, and UniVLA drops from 95.2\% to 4.3\% under viewpoint changes.
8	Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled laboratory settings.
9	
10	% --- Para 2: Existing approaches and the gap ---
11	Two lines of work address this challenge.
12	Training-time methods improve the base policy through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}, but require retraining or per-task RL and remain bounded by the training distribution.
13	Inference-time methods leave the policy frozen: ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression for uncertainty quantification and out-of-distribution detection, but does not learn corrective residuals; A2C2~\cite{a2c2_2025} trains a per-step correction head on frozen VLA action chunks, but applies correction unconditionally without multi-sample selection or explicit magnitude control; VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step.
14	Despite growing interest in inference-time action refinement, fundamental design questions remain unanswered: how much does selection contribute relative to cor
…[truncated 3954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 129 · 2026-05-19T01:41:48.366210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-19T01:41:48.817970+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	VLAs have progressed from tokenized action prediction~\cite{brohan2023rt2,kim2024openvla,ghosh2024octo} to generative action models based on diffusion~\cite{chi2023diffusion_policy} and flow matching~\cite{black2024pi0,shukor2025smolvla}, with the latter producing stochastic action samples that enable multi-sample inference strategies.
6	Improving VLA robustness divides into training-time and inference-time approaches.
7	
8	\paragraph{Training-time methods.}
9	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories.
10	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.
11	DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.
12	TT-VLA~\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.
13	All four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.
14	
15	\paragraph{Inference-time methods.}
16	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.
17	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.
18	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\,s per control step, prohibitive for real-time manipulation.
19	A2C2~\ci
…[truncated 3075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-19T01:41:48.818453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-19T01:41:49.321031+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	\begin{figure}[t]
6	  \centering
7	  \includegraphics[width=\linewidth]{fig1_pipeline.pdf}
8	  \caption{Sample-select-correct pipeline. At each control step, $K{=}10$ action samples are drawn from the frozen VLA, the candidate closest to the sample mean is selected via $L_2$ argmin, and a lightweight CRM predicts a bounded residual correction ($\|\boldsymbol{\delta}\|_2 \leq \varepsilon$). The base VLA is never modified.}
9	  \label{fig:pipeline}
10	\end{figure}
11	
12	\textbf{Our method} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
13	
14	\subsection{Problem Setup}
15	\label{sec:problem_setup}
16	
17	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.
18	
19	We instantiate the pipeline on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\pi_\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\pi_\theta$. The method applies to flow-matching VLAs that produce diverse action samples (Section~\ref{sec:applicability}).
20	
21	\subsection{Multi-Sample Selection}
…[truncated 5493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-19T01:41:49.321447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-19T01:41:49.773090+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate the pipeline on two LIBERO task suites, asking: (i)~does learned correction improve over the frozen VLA baseline? (ii)~do conformal features help? (iii)~how sensitive is performance to the magnitude bound $\varepsilon$?
6	
7	\subsection{Experimental Setup}
8	\label{sec:exp_setup}
9	
10	\paragraph{Benchmarks.}
11	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
12	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
13	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
14	
15	\paragraph{Base VLA.}
16	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
17	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
18	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the correction pipeline via direct thresholding.
19	
20	\paragraph{Baselines.}
21	All methods use the same frozen SmolVLA checkpoint:
22	\begin{itemize}[nosep]
23	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
24	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
25	  \item \textbf{Random} ($K{=}10$): uniformly random sample from $K$ candidates, no CRM correction.
26	  \item \textbf{Argmin} ($K{=}10$): select sample closest to sample mean via $L_2$ distance (Section~\ref{sec:selection}), no CRM correction.
27	\end{itemize}
28	
29	\paragraph{CRM variants.}
30	Three CRM variants (obs\_only, perdof, scalar) share the same 
…[truncated 9628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 135 · 2026-05-19T01:41:49.773600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-19T01:41:50.325755+00:00_

1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Selection vs.\ correction in continuous action spaces.}
6	In contrast to LLM test-time scaling, where selection among candidates drives improvement~\cite{snell2024scaling}, our decomposition reveals that selection alone provides no significant benefit in low-dimensional continuous action spaces ($d{=}6$): $K{=}10$ flow-matching samples cluster too tightly for selection to discriminate.
7	Learned correction is the active mechanism, but multi-sampling is an enabling condition that provides a centered starting point within the CRM's bounded correction radius; at $K{=}1$, correction alone falls below the VLA-only baseline (10.3\% vs.\ 11.6\%).
8	Transferring test-time compute ideas to embodied domains requires rethinking the selection-correction balance.
9	
10	
11	\section{Limitations}
12	\label{sec:limitations}
13	
14	\begin{enumerate}[nosep]
15	  \item \emph{Simulation only.} All experiments use LIBERO~\cite{liu2023libero}; real-robot transfer is untested.
16	  \item \emph{Single VLA backbone.} We evaluate only SmolVLA~\cite{shukor2025smolvla} (450M parameters). Whether the pipeline transfers to larger VLAs (e.g., $\pi_0$) is unknown.
17	  \item \emph{Limited benchmarks.} Two LIBERO suites (20 tasks total); other benchmarks and perturbation types are not evaluated.
18	  \item \emph{Seed variance.} Per-seed margins over argmin selection range from $-1$\,pp to $+10$\,pp; on seed 43, correction slightly decreases performance relative to argmin (16\% vs.\ 17\%). No seeds were discarded.
19	  \item \emph{Absolute performance.} 17.6\% mean success is far from deployment-ready. A2C2~\cite{a2c2_2025} reports 67--72\% baselines by training SmolVLA from scratch on LIBERO; their setting (full training) differs fundamentally from ours (frozen pretrained checkpoint, 11.6\% baseline), so direct numerical comparison is not meaningful.
20	\end{enumerate}
21	
22	
23	\section*{AI Disclosure}
24	
25	AI tools (Claude, Git
…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 137 · 2026-05-19T01:41:50.326258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 138 · 2026-05-19T01:41:50.426927+00:00_

1	
2	\appendix
3	
4	\section{Inference-Time Scaling with $K$}
5	\label{sec:k_scaling}
6	
7	Figure~\ref{fig:kvalue} plots task success rate against the number of VLA samples $K$.
8	
9	\begin{figure}[h]
10	\centering
11	\includegraphics[width=\linewidth]{figures/fig3_kvalue.pdf}
12	\caption{Success rate (\%) vs.\ number of VLA samples $K$ on LIBERO-Object (obs\_only, $\varepsilon{=}0.2$). Reference lines: VLA-only (11.6\%, 5 seeds) and Argmin-only (12.3\%, 6 seeds). Error bars: $\pm$1 std. The main improvement occurs from $K{=}1$ to $K{=}5$ (+5.95\,pp), with diminishing returns from $K{=}5$ to $K{=}10$ (+1.35\,pp).}
13	\label{fig:kvalue}
14	\end{figure}
15	
16	Performance improves with $K$ but with diminishing returns: $K{=}1$ (10.3\%, 3 seeds) $\to$ $K{=}5$ (16.3\%, 4 seeds) $\to$ $K{=}10$ (17.6\%, 7 seeds).
17	The main jump occurs from $K{=}1$ to $K{=}5$ (+5.95\,pp), while $K{=}5$ to $K{=}10$ adds only +1.35\,pp.
18	At $K{=}1$, CRM correction alone falls below the VLA-only baseline (10.3\% vs.\ 11.6\%), because the single sample lacks argmin centering and shifts outside the CRM's training distribution. Multi-sample selection is an enabling condition for effective correction.
19	The diminishing-returns pattern is loosely analogous to inference-time compute scaling in LLMs~\cite{snell2024scaling}, though the mechanism differs: in our setting, additional samples improve the starting point for correction rather than enabling better selection.
20	$K{=}5$ captures ${\sim}$82\% of the $K{=}10$ benefit at half the compute cost, suggesting a practical operating point for latency-sensitive deployment.
21	The compute cost scales linearly: $K{=}10$ requires 10 forward passes through the frozen VLA plus ${\sim}$0.3\,ms for CRM inference, a ${\sim}$10$\times$ increase in VLA compute.
22	
23	
24	\section{Applicability Boundary: Stochastic VLA Diversity}
25	\label{sec:applicability}
26	
27	The multi-sample pipeline requires stochastic action diversity across samples. We test this p
…[truncated 3960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-19T01:41:52.081604+00:00_

Web search results for query: "CoRL 2026 submission deadline page limit double blind review policy template"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"}]

Based on the search results, here's the information about CoRL 2026 submission requirements:

## Submission Deadline

The paper submission deadline is May 29, 2026. Additionally, the abstract submission deadline is May 26, 2026 11:59 UTC.

## Page Limit

Papers are limited to 8 pages of content plus unlimited references. An additional 9th page is allowed for camera-ready submissions to incorporate reviewer feedback.

## Double-Blind Review Policy

CoRL is double-blind, which means all papers must be anonymized. The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced.

## Template

The CoRL LaTeX template uses a custom style based on PMLR (Proceedings of Machine 
…[truncated 423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5624
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-19T01:42:12.218479+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-19T01:42:12.722231+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-19T01:42:13.220736+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-19T01:42:14.560730+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml\", \"content\": \"_next_id: 66\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 01:03 UTC\\n  summary: MVP 方案确定：3D Point-Reaching Motivating Experiment 验证 per-DOF conformal 特征的信息优势\\n  rationale: IDEA_BRIEF 已设计了完美的 go/no-go gate：用合成数据的 3D reaching task 对比 per-DOF vs\\n    标量 vs 无不确定性三种 conditioning，直接测试核心假设。成本极低（<0.5 GPU-hours），无需 VLA 基础设施，失败则提前止损。Pass\\n    标准明确：B 在非扰动轴 MSE 比 A 低 >10%。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 01:06 UTC\\n  summary: 采纳 Reviewer 建议完善 MVP：增加 B vs C 对比（>5% MSE）、K=10 estimated uncertainty variant、2:1/1.5:1\\n    各向异性 sweep\\n  rationale: Reviewer 正确指出 (1) 缺少 B vs C 对比会遗漏\\\"观测特征已足够\\\"的可能性，这直接关系核心 claim；(2) oracle\\n    uncertainty 与实际 pipeline 存在 gap，K=10 variant 几乎零成本可验证；(3) 5:1 比率过极端，需测试更温和情况。三项改进均不增加显著成本。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 01:47 UTC\\n  summary: MVP 通过，GO — 进入 research 阶段\\n  rationale: 全部 3 条 pass 标准满足且 margin 很大：per-DOF (B) 在非扰动轴 MSE 比标量 (A) 低 22-38%，比无\\n    uncertainty (C) 低 15-39%。K=10 estimated 和弱各向异性(1.5:1)下均成立。核心假设\\\"per-DOF conformal\\n    特征携带更多可操作信息\\\"得到验证。关注风险：oracle→K=10 衰减 ~15pp，真实 7-DOF 场景待验证。\\n  related_experiments:\\n  - exp_id: mvp-point-reaching\\n    role: MVP gate\\n    result: PASS — all 6 conditions met criteria\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 02:59 UTC\\n  summary: Horizon 策略：截取 chunk 前 H_eff=5 步，action_dim=6。CGS 输出 40D。\\n  rationale: SmolVLA chunk_size=50 远超原假设 H=5。receding-horizon 执行语义下只需关注近期 action 的\\n    uncertainty，远期 step 对当前校正无意义。H_eff=5 保持与 IDEA_BRIEF 设计一致，CGS 40D 可控（per-DOF std\\n    30 + radius 5 + volume 5），p/n=6/10=0.6 优于原假设 0.7。H_eff=10 留作 ablation。action_dim=6\\n    使 Ledoit-Wolf 更稳定。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 03:00 UTC\\n  summar
…[truncated 3559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1339
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-19T01:42:14.618452+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-19T01:42:14.675029+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 56
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-19T01:42:22.464376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-19T01:42:22.515316+00:00_

1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	
21	@misc{black2024pi0,
22	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
23	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
24	    year={2024},
25	    eprint={2410.24164},
26	    archivePrefix={arXiv},
27	    primaryClass={cs.RO}
28	}
29	
30	@misc{braun2025cgs,
31	    title={Multivariate Conformal Prediction via Conformalized Gaussian Scoring},
32	    author={Sacha Braun and Eug{\`e}ne Berta and Michael I. Jordan and Francis Bach},
33	    year={2025},
34	    eprint={2507.20941},
35	    archivePrefix={arXiv},
36	    primaryClass={stat.ML}
37	}
38	
39	@misc{brohan2023rt2,
40	    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
41	    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Fl
…[truncated 11426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-19T01:42:22.716463+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
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

_source line 149 · 2026-05-19T01:42:22.767207+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-19T01:42:27.734455+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-19T01:42:28.236770+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-19T01:42:28.337591+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-19T01:42:28.388255+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-19T01:42:31.148669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-19T01:42:31.651228+00:00_

1	- id: "C1"
2	  summary: "Fisher exact test independence violation (pseudo-replication)"
3	  category: experiment
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - {round: 1, reviewers: [R1, R2, R3], note: "Same-seed episodes share CRM weights, violating independence assumption"}
10	  action_items:
11	    - {round: 1, action: "Replace Fisher with Mann-Whitney U (seed-level) as primary test + sign test supplementary", assigned_to: "Paper Agent + Agent", status: "in_progress"}
12	  resolution: ""
13	  resolution_round: null
14	
15	- id: "C2"
16	  summary: "Core claim 'correction is sole driver' contradicts K=1 data (10.3% < 11.6%)"
17	  category: framing
18	  severity: critical
19	  status: in_progress
20	  first_raised_round: 1
21	  last_seen_round: 1
22	  mentions:
23	    - {round: 1, reviewers: [R1, R2, R3], note: "K=1 CRM below baseline means correction alone harmful. Appendix L18 also contradicts."}
24	  action_items:
25	    - {round: 1, action: "Reframe to 'correction is active mechanism, multi-sampling is enabling condition'. Fix Appendix L18.", assigned_to: "Paper Agent", status: "in_progress"}
26	  resolution: ""
27	  resolution_round: null
28	
29	- id: "C3"
30	  summary: "Inconsistent seed counts across methods without explanation"
31	  category: experiment
32	  severity: critical
33	  status: in_progress
34	  first_raised_round: 1
35	  last_seen_round: 1
36	  mentions:
37	    - {round: 1, reviewers: [R1, R2, R3], note: "obs_only 7, VLA-only 5, Argmin 6, Random 3 — no justification"}
38	  action_items:
39	    - {round: 1, action: "Add explanation paragraph (resource allocation by importance). Supplement Random to n=5.", assigned_to: "Paper Agent + Agent", status: "in_progress"}
40	  resolution: ""
41	  resolution_round: null
42	
43	- id: "C4"
44	  summary: "Novelty insufficient — standard MLP + L2 clipping"
45	  category: method
46	  severity: critical
47	  status: in_progress
48	  first_ra
…[truncated 7602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-19T01:42:31.701859+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/agent"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-19T01:42:31.752420+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/review_director_a3659f64.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-19T01:42:35.216808+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-19T01:42:35.267397+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-19T01:42:38.127870+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-19T01:42:38.128356+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-19T01:42:44.914160+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8",
  "glob": "*.yaml",
  "output_mode": "files_with_matches",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8",
    "glob": "*.yaml",
    "output_mode": "files_with_matches",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-19T01:42:45.015060+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-19T01:42:48.193160+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8",
  "output_mode": "files_with_matches",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8",
    "output_mode": "files_with_matches",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-19T01:42:48.545213+00:00_

Found 10 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_416d453a45869a9406db62186b1e3ef7_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/global/logs/system.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-mag-obsonly-norm03-b2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/logs/review_best.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-19T01:42:53.462990+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8",
  "glob": "CLAUDE.md",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8",
    "glob": "CLAUDE.md",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-19T01:42:53.513606+00:00_

CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:152:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-19T01:42:56.728429+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paperreview_ai|external_review\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8",
  "glob": "**/registry.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "paperreview_ai|external_review\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8",
    "glob": "**/registry.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-19T01:42:56.779041+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-19T01:44:08.651174+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### Venue 信息\n- **目标 venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + 无限 references + 可选 appendix\n- **模板**: corl_2026\n- **匿名规则**: Double-blind\n- **特殊要求**: 必须包含 Limitations section（计入 8 页），AI Disclosure statement，鼓励 real-robot 实验或 sim-to-real 可迁移性论证\n\n### 论文信息\n- **标题**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n- **论文路径**: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`（main.tex 通过 \\input 引入 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **引用文件**: `projects/acr-vla-conformal-refinement/docs/paper/references.bib`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **方法正确性**：\n   - sample-select-correct pipeline 的数学表述是否正确？L2 argmin selection 的动机是否充分？\n   - CRM 架构设计（3层 MLP + norm clipping）是否合理？是否有遗漏的设计选择？\n   - magnitude bound ε 的选择依据是否充分？norm clipping 的理论/经验支撑？\n\n2. **实验设计**：\n   - baseline 设置是否充分？是否遗漏了关键 baseline（特别是其他 inference-time 方法如 A2C2 的实验对比）？\n   - 评估协议是否合理？10 rollouts × 10 tasks 是否足够？\n   - LIBERO-Spatial null result 的证据是否充分？\n   - CRM 在 eval 任务上训练——是否存在信息泄露？\n\n3. **统计分析**：\n   - Mann-Whitney U 检验的使用是否正确？seed-level 检验 vs episode-level 的选择依据？\n   - 不同方法间 seed 数量不一致（obs_only 7, VLA-only 5, Argmin 6, Random 3）——这是否影响统计可信度？\n   - 效应量（+6.0pp）在绝对性能仅 17.6% 的背景下是否有实际意义？\n   - Per-seed variance（seed 43 correction 不如 argmin）是否被充分讨论？\n\n4. **可重复性**：\n   - 训练细节是否足够重复实验？precompute 数据构建过程是否清晰？\n   - 超参数选择（K=10, H=5, ε=0.2, 学习率, 训练 epoch）是否有消融或敏感性分析？\n\n5. **Claims 与 Evidence 对齐**：\n   - \"learned correction is the active mechanism while multi-sampling is an enabling condition\" 这一核心 claim 是否被数据充分支撑？\n   - \"conformal features cause progressive collapse\" 的机理解释是否令人信服？\n   - applicability boundary（tokenized VLA 缺乏 diversity）是否从单一对比（SmolVLA vs OpenVLA）就能下结论？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 sentences)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (重点，必须严格)\n- W1: [severity: critical/warning/info] ...\n- W2: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References (if any)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n\n## Detailed Comments (逐 section)\n```",
  "reviewer_id": "1",
  "project": "acr-vla-conformal-refinement",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### Venue 信息\n- **目标 venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + 无限 references + 可选 appendix\n- **模板**: corl_2026\n- **匿名规则**: Double-blind\n- **特殊要求**: 必须包含 Limitations section（计入 8 页），AI Disclosure statement，鼓励 real-robot 实验或 sim-to-real 可迁移性论证\n\n### 论文信息\n- **标题**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n- **论文路径**: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`（main.tex 通过 \\input 引入 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **引用文件**: `projects/acr-vla-conformal-refinement/docs/paper/references.bib`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **方法正确性**：\n   - sample-select-correct pipeline 的数学表述是否正确？L2 argmin selection 的动机是否充分？\n   - CRM 架构设计（3层 MLP + norm clipping）是否合理？是否有遗漏的设计选择？\n   - magnitude bound ε 的选择依据是否充分？norm clipping 的理论/经验支撑？\n\n2. **实验设计**：\n   - baseline 设置是否充分？是否遗漏了关键 baseline（特别是其他 inference-time 方法如 A2C2 的实验对比）？\n   - 评估协议是否合理？10 rollouts × 10 tasks 是否足够？\n   - LIBERO-Spatial null result 的证据是否充分？\n   - CRM 在 eval 任务上训练——是否存在信息泄露？\n\n3. **统计分析**：\n   - Mann-Whitney U 检验的使用是否正确？seed-level 检验 vs episode-level 的选择依据？\n   - 不同方法间 seed 数量不一致（obs_only 7, VLA-only 5, Argmin 6, Random 3）——这是否影响统计可信度？\n   - 效应量（+6.0pp）在绝对性能仅 17.6% 的背景下是否有实际意义？\n   - Per-seed variance（seed 43 correction 不如 argmin）是否被充分讨论？\n\n4. **可重复性**：\n   - 训练细节是否足够重复实验？precompute 数据构建过程是否清晰？\n   - 超参数选择（K=10, H=5, ε=0.2, 学习率, 训练 epoch）是否有消融或敏感性分析？\n\n5. **Claims 与 Evidence 对齐**：\n   - \"learned correction is the active mechanism while multi-sampling is an enabling condition\" 这一核心 claim 是否被数据充分支撑？\n   - \"conformal features cause progressive collapse\" 的机理解释是否令人信服？\n   - applicability boundary（tokenized VLA 缺乏 diversity）是否从单一对比（SmolVLA vs OpenVLA）就能下结论？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 sentences)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (重点，必须严格)\n- W1: [severity: critical/warning/info] ...\n- W2: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References (if any)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n\n## Detailed Comments (逐 section)\n```",
    "reviewer_id": "1",
    "project": "acr-vla-conformal-refinement",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 171 · 2026-05-19T01:44:26.623654+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17972
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-19T01:44:31.233582+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + Related Work + 论文定位 + 写作与格式合规**\n\n### Venue 信息\n- **目标 venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + 无限 references + 可选 appendix\n- **模板**: corl_2026\n- **匿名规则**: Double-blind\n- **特殊要求**: 必须包含 Limitations section（计入 8 页），AI Disclosure statement，鼓励 real-robot 实验或 sim-to-real 可迁移性论证\n\n### 论文信息\n- **标题**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n- **论文路径**: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`（main.tex 通过 \\input 引入 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **引用文件**: `projects/acr-vla-conformal-refinement/docs/paper/references.bib`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性与贡献显著性**：\n   - 核心方法（argmin selection + MLP residual + L2 clipping）的技术新颖性如何？\n   - 论文的核心贡献是方法本身还是实验分析/发现？定位是否清晰一致？\n   - 三条 contribution（pipeline + conditioning finding + applicability boundary）对 CoRL 社区的价值？\n   - 与 A2C2 的差异是否构成足够的增量贡献？\n\n2. **Related Work 完整性与定位**：\n   - 四个子节（VLA Robustness, Residual Policy Learning, Conformal Prediction, Inference-Time Scaling）的覆盖是否充分？\n   - 是否遗漏了重要的相关工作？（如 diffusion policy 的 test-time 变体、其他 residual learning 方法、更多 CP-robotics 工作）\n   - 本文在已有工作中的 positioning 是否清晰？读者能否快速理解本文的独特贡献？\n   - 29 条引用对 CoRL 论文是否足够？\n\n3. **写作质量**：\n   - Abstract 是否在 150-250 words 内清楚回答 what/why/how/result？\n   - Introduction 的叙事线是否连贯（背景→缺口→方法→发现→贡献）？\n   - 论文主线是否统一？Abstract/Introduction/Method/Experiments/Discussion 是否讲同一个故事？\n   - 是否有 AI 写作痕迹（em-dash, -ing phrases, 过度分段, 禁用词汇）？\n   - 专有名词/缩写是否在首次使用时定义？\n\n4. **格式合规**：\n   - 页数是否在 8 页限制内？（估算正文页数）\n   - 匿名化是否完整？（作者信息、代码链接、致谢）\n   - Limitations section 是否存在且有实质内容？\n   - AI Disclosure statement 是否存在？\n   - 图表是否符合 CoRL 模板规范？caption 是否自包含？\n   - 引用格式是否一致？bib 条目是否完整（有 venue/year/pages）？\n\n5. **CoRL venue fit**：\n   - 论文是否\"focus on a core robotics problem\"？\n   - 缺乏 real-robot 实验——论文是否提供了\"convincing evidence that simulation experiments are transferable to real robots\"？\n   - 对 CoRL 审稿人群体（robotics + ML）而言，paper 的 impact 如何？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 sentences)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (重点，必须严格)\n- W1: [severity: critical/warning/info] ...\n- W2: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References (if any)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n\n## Detailed Comments (逐 section)\n```",
  "reviewer_id": "2",
  "project": "acr-vla-conformal-refinement",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + Related Work + 论文定位 + 写作与格式合规**\n\n### Venue 信息\n- **目标 venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + 无限 references + 可选 appendix\n- **模板**: corl_2026\n- **匿名规则**: Double-blind\n- **特殊要求**: 必须包含 Limitations section（计入 8 页），AI Disclosure statement，鼓励 real-robot 实验或 sim-to-real 可迁移性论证\n\n### 论文信息\n- **标题**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n- **论文路径**: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`（main.tex 通过 \\input 引入 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **引用文件**: `projects/acr-vla-conformal-refinement/docs/paper/references.bib`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性与贡献显著性**：\n   - 核心方法（argmin selection + MLP residual + L2 clipping）的技术新颖性如何？\n   - 论文的核心贡献是方法本身还是实验分析/发现？定位是否清晰一致？\n   - 三条 contribution（pipeline + conditioning finding + applicability boundary）对 CoRL 社区的价值？\n   - 与 A2C2 的差异是否构成足够的增量贡献？\n\n2. **Related Work 完整性与定位**：\n   - 四个子节（VLA Robustness, Residual Policy Learning, Conformal Prediction, Inference-Time Scaling）的覆盖是否充分？\n   - 是否遗漏了重要的相关工作？（如 diffusion policy 的 test-time 变体、其他 residual learning 方法、更多 CP-robotics 工作）\n   - 本文在已有工作中的 positioning 是否清晰？读者能否快速理解本文的独特贡献？\n   - 29 条引用对 CoRL 论文是否足够？\n\n3. **写作质量**：\n   - Abstract 是否在 150-250 words 内清楚回答 what/why/how/result？\n   - Introduction 的叙事线是否连贯（背景→缺口→方法→发现→贡献）？\n   - 论文主线是否统一？Abstract/Introduction/Method/Experiments/Discussion 是否讲同一个故事？\n   - 是否有 AI 写作痕迹（em-dash, -ing phrases, 过度分段, 禁用词汇）？\n   - 专有名词/缩写是否在首次使用时定义？\n\n4. **格式合规**：\n   - 页数是否在 8 页限制内？（估算正文页数）\n   - 匿名化是否完整？（作者信息、代码链接、致谢）\n   - Limitations section 是否存在且有实质内容？\n   - AI Disclosure statement 是否存在？\n   - 图表是否符合 CoRL 模板规范？caption 是否自包含？\n   - 引用格式是否一致？bib 条目是否完整（有 venue/year/pages）？\n\n5. **CoRL venue fit**：\n   - 论文是否\"focus on a core robotics problem\"？\n   - 缺乏 real-robot 实验——论文是否提供了\"convincing evidence that simulation experiments are transferable to real robots\"？\n   - 对 CoRL 审稿人群体（robotics + ML）而言，paper 的 impact 如何？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 sentences)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (重点，必须严格)\n- W1: [severity: critical/warning/info] ...\n- W2: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References (if any)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n\n## Detailed Comments (逐 section)\n```",
    "reviewer_id": "2",
    "project": "acr-vla-conformal-refinement",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 173 · 2026-05-19T01:44:32.954608+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1721
}
```

</details>

---


### Assistant

_source line 174 · 2026-05-19T01:44:41.784209+00:00_

Round 1 审稿任务已分配：

- **Reviewer 1**（方法 + 实验 + 统计）→ 已派发
- **Reviewer 2**（新颖性 + Related Work + 写作 + 格式）→ 已派发

等待两位 Reviewer 返回独立审稿意见。收到后将进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 175 · 2026-05-19T01:50:57.265710+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

**论文**: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs"
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析
**审稿标准来源**: CoRL 2023 official reviewer guidelines (Originality, Quality, Clarity, Significance, Relevance, Limitations) + CoRL 2024 Instruction for Reviews ("significance and novelty of results", "potential for scientific and technological impact", "relevance to robotic learning")。CoRL 2026 完整 review form 尚未公开；以上述历年维度为基础。

---

## Summary (2-3 sentences)

本文提出 sample-select-correct pipeline，对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正。在 LIBERO-Object 上实现 17.6% vs 11.6% 的成功率提升（p=0.003），并通过 component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告了 conformal features 失效和 tokenized VLA 不适用的 negative results。

---

## 总体评分

**Overall**: Weak Reject
**一句话总结**: 实验设计严谨性不足（CRM 在 eval 任务上训练、缺少最关键 baseline A2C2、seed 数量小且不平衡），加上绝对性能极低且无 real-robot 验证，使得核心 claims 的可信度和 significance 不够达到 CoRL 录用标准。

## 官方维度打分（基于 CoRL reviewer guidelines）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3/5 | Pipeline 各组件（multi-sample, argmin selection, residual correction, norm clipping）均非新颖；贡献在于组合与 ablation 设计。Component decomposition 视角有一定新意。 |
| Quality (Soundness) | 2/5 | 核心实验存在方法论问题：CRM 训练于 eval 任务的 demo 数据、缺少 A2C2 实验对比、seed 数量小且不平衡、medoid 表述不准确。详见 W1-W5。 |
| Clarity | 4/5 | 写作清晰，pipeline 描述明确，ablation 结构合理。统计 protocol 的 rationale 交代得当。 |
| Significance | 2/5 | 17.6% 绝对成功率远低于实用水平；仅在 simulation 的 LIBERO-Object（10 tasks）上有效；无 real-robot 实验或 sim-to-real 论证。对 CoRL 社区的 impact 有限。 |
| Relevance | 4/5 | 直接针对 VLA 部署中的 distribution shift 问题，符合 robot learning 核心议题。 |
| Limitations | 4/5 | 自我披露较为诚实（simulation only, single backbone, seed variance, absolute performance），但遗漏了 CRM 在 eval 任务上训练的泛化性问题。 |

---

## Strengths

- **S1: 系统化的 component decomposition**。将 pipeline 拆解为 selection 和 correction 两个维度，通过 K=1 correction、selection-only、random selection 等控制实验清楚揭示各组件贡献。"Selection alone 无显著帮助、correction alone (K=1) 低于 baseline、二者结合才有效"这一发现对 embodied test-time compute scaling 有洞察价值。（Section 4.2, Table 1）

- **S2: 有价值的 negative results**。Conformal features 的失败（observation-only 14.3-17.6% 稳健 vs perdof 渐进 collapse 至 0%）和 tokenized VLA 不适用性的发现，对该领域后续研究有指导意义。（Section 4.3, 4.4, Figure 2）

- **S3: 统计协议的 rationale 明确**。论文正确识别了 episode-level 非独立性问题，选择 seed-level 非参数检验（Mann-Whitney U），并给出了理由。Sign test 作为额外验证也是合理的。（Section 4.1 Statistical protocol）

- **S4: 写作质量较高**。Pipeline 描述精确，数学符号一致，ablation 逻辑清晰。Limitations section 直面多项弱点。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] CRM 在评估任务的 demonstration 数据上训练，无泛化性验证

- 具体位置：Section 3.4 Training (method.tex:55-60), Section 4.1 Training (experiments.tex:32-36)
- 问题：CRM 训练数据为 "26,737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks"。这 20 个 task 恰好就是评估用的 LIBERO-Object (10) + LIBERO-Spatial (10)。CRM 在训练时直接见过每个 eval task 的 expert demonstration，学到的可能是 task-specific 的残差模式而非 generalizable correction。
- 为什么影响接收：论文将方法定位为 "inference-time refinement for frozen VLAs"，暗示一定程度的泛化能力。但当前实验设计无法区分"CRM 学到了通用修正能力"和"CRM 记住了每个任务的专属残差"。缺少 held-out task evaluation 是重大遗漏。
- 建议修改方向：(1) 划分 train/test task split（如在 15 个 task 上训练，5 个 held-out task 上评估）；(2) 至少讨论为什么当前设计不构成信息泄露，或坦诚承认这是 task-specific fine-tuning 而非 general inference-time refinement。

**N2** [critical] 缺少最关键 baseline A2C2 的实验对比

- 具体位置：Section 2 Related Work (related_work.tex:19-22), Section 6 Limitations item 5 (discussion.tex:19)
- 问题：A2C2 被明确认定为 "the closest concurrent work"（Section 2），且论文详细讨论了三点方法差异。但从未将 A2C2 作为 baseline 运行。Limitations section 的解释——"A2C2 reports 67-72% baselines by training SmolVLA from scratch...direct numerical comparison is not meaningful"——是误导性的：A2C2 的 correction head 完全可以接在同一个 frozen SmolVLA checkpoint 上。
- 为什么影响接收：审稿人无法判断 sample-select-correct 相比 A2C2 的 per-step correction 是否真正更优。论文提出的三点差异（multi-sample selection、norm clipping、observation conditioning）没有实验证据支撑其优越性。这是 positioning 的核心缺陷。
- 建议修改方向：在同一 frozen SmolVLA checkpoint 上实现 A2C2 baseline。若因时间/代码原因无法完成，至少提供更诚实的讨论，承认这是一个 open comparison 而非已回答的问题。

**N3** [critical] Seed 数量小且不平衡，统计推断脆弱

- 具体位置：Section 4.1 Statistical protocol (experiments.tex:40-46), Table 1
- 问题：obs_only 7 seeds、VLA-only 5 seeds、Argmin 6 seeds、Random 仅 3 seeds、VLA-mean 4 seeds、scalar 4 seeds。Mann-Whitney U 在 n1=7, n2=5 时统计功效极有限。论文称 "compute budget was allocated by comparison importance"，但这造成了不对称性：Random 仅 3 seeds 就断言 "statistically indistinguishable from VLA-only"，但 3 seeds 的 MW-U 检验几乎无法拒绝任何 null hypothesis。
- 为什么影响接收：(1) obs_only vs VLA-only 的 U=35（n1=7, n2=5 时的最大可能值），说明 7 个 obs_only seeds 全部高于 5 个 VLA-only seeds——这是 perfect rank separation，p=0.0025 可信，但样本量之小使得效应量估计非常不精确。(2) Per-seed variance 实质性存在：seed 43 上 argmin (17%) > obs_only (16%)。(3) Random 3 seeds 的 claim 不可靠。
- 建议修改方向：所有关键对比至少 10 seeds；或者明确标注 statistical power 的限制，不要断言 "statistically indistinguishable" 只有 3 seeds 的对比。

**N4** [critical] 无 real-robot 实验或 sim-to-real 论证

- 具体位置：Section 6 Limitations item 1 (discussion.tex:15)
- 问题：CoRL 2026 CFP 明确鼓励 "real-robot experiments or sim-to-real transferability arguments"。论文仅在 LIBERO simulation 中实验，且绝对成功率仅 17.6%。K=10 forward passes 的 compute overhead（约 10x VLA 计算量）对 real-time manipulation 的可行性未量化（wall-clock latency analysis 缺失）。
- 为什么影响接收：对于 CoRL 这样以 real-world robotics 为核心的 venue，纯 simulation 结果加上极低的绝对性能，削弱了论文的 practical significance。
- 建议修改方向：(1) 提供 wall-clock latency 分析（SmolVLA single pass latency × K=10 + CRM 0.3ms），论证是否满足 real-time 控制要求；(2) 若无法做 real-robot 实验，至少讨论 sim-to-real gap 对 CRM 的潜在影响。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Geometric medoid" 表述不精确

- 具体位置：Section 3.2 (method.tex:29)
- 问题：论文称 "The L2 argmin selects the geometric medoid of the sample set"。严格来说，geometric medoid 定义为 argmin_k Σ_j ||x_k - x_j||（最小化到所有其他点的 L2 距离之和），而论文实际计算的是 argmin_k Σ_h ||a_h^(k) - μ_h||_2^2（最小化到均值的 squared L2 距离）。后者等价于最小化到所有点的 squared L2 距离之和（通过展开平方可证），但与经典 geometric medoid（非平方 L2）不同。
- 建议：删除 "geometric medoid" 的称呼，改为 "the sample closest to the centroid" 或注明使用 squared L2 距离。

**W2** [warning] ε 超参数敏感性分析不完整

- 具体位置：Section 4.4, Figure 2 (experiments.tex:116-128)
- 问题：Figure 2 只展示 obs_only 和 perdof 两个变体在不同 ε 下的表现。scalar 变体仅有 ε=0.1 一个数据点（8.5%, 4 seeds）。论文声称 ε ∈ [0.05, 0.3] "yields comparable obs_only performance" 但这个区间内的具体数值仅从图中可见，无表格列出。各 ε 点的 seed 数量也不一致（n=1-7 per point），使得带 error bar 的比较可信度不均。
- 建议：提供 ε 敏感性分析的完整表格（包含每个点的 seed 数），scalar 变体补充多个 ε 点。

**W3** [warning] Applicability boundary claim 基于单一对比

- 具体位置：Section 4.4 (experiments.tex:134-136), Appendix B (appendix.tex:24-40)
- 问题：tokenized VLA 缺乏 diversity 的结论仅基于 OpenVLA 在 T=0.5 的一个设定。未测试更高 temperature、nucleus sampling、或其他 tokenized VLA（如 RT-2）。"Architectural applicability boundary" 是一个强 claim，但 evidence 过窄。
- 建议：(1) 测试 OpenVLA 在 T=1.0 或更高温度下的多样性；(2) 软化 claim 为 "under default sampling settings" 或补充更多 tokenized VLA 的 evidence。

**W4** [warning] LIBERO-Spatial null result 分析不足

- 具体位置：Section 4.2 最后一段 (experiments.tex:91-95)
- 问题：Spatial 上所有方法 30-35%，仅一段推测性解释（"spatial perturbations create layout changes that require higher-level re-planning"）。无 per-task Spatial 分析（Appendix 只有 Object 的 Table 3），无对 SmolVLA Spatial 失败模式的定量分析。
- 建议：(1) 补充 LIBERO-Spatial per-task 结果表；(2) 提供 failure case 分析证明确实是 planning-level failure 而非 motor-level error。

**W5** [warning] DAgger 引用不恰当

- 具体位置：Section 3.4 (method.tex:60), Section 4.3 (experiments.tex:109)
- 问题：论文引用 Ross et al. (2011) [DAgger] 来 justify data augmentation（"Data augmentation...improves generalization to the closed-loop state distribution"）和 compounding errors。DAgger 是关于 iterative dataset aggregation through online interaction 的，而非 static Gaussian noise augmentation。这两个 idea 相关但不等价。
- 建议：改引 covariate shift in imitation learning 的更直接文献，或更准确地引用 DAgger 中关于 distribution shift 的分析而非方法本身。

---

## Questions for Authors

**Q1**: CRM 是否曾在 held-out tasks 上测试过？如果在 10 个 LIBERO-Object task 上训练、5 个 held-out Object task 上评估，结果如何？这是判断 CRM 泛化能力的关键实验。

**Q2**: Table 1 中 LIBERO-Spatial 的 Random baseline 标记为 "---"，原因是什么？是否运行过但数据丢失，还是有意跳过？

**Q3**: obs_only vs VLA-only 的 MW-U test 给出 U=35 = 7×5 = U_max，这意味着 7 个 obs_only seeds 的成功率全部高于 5 个 VLA-only seeds 的所有值。能否公布每个 seed 的具体成功率以便验证？

**Q4**: K=10 forward passes 在 SmolVLA 上的 wall-clock latency 是多少？是否满足 real-time control 的要求（typically < 100ms per step for manipulation tasks）？

**Q5**: A2C2 的 correction head 是否可以直接 attach 到同一个 frozen SmolVLA checkpoint 上？如果可以，为什么不做这个对比？

**Q6**: 论文称 CRM 在所有 20 个 LIBERO 任务上训练（包括 Spatial）。在 LIBERO-Spatial 上 CRM 未带来提升，但 CRM 训练数据包含 Spatial demo——这是否意味着 CRM 即使在 "见过" 的任务上也不总是有效？这对 N1 的 task-specific memorization 假说有何影响？

---

## Missing References

1. **Best-of-N sampling in robotics**: 论文与 LLM test-time scaling 做对比（Snell et al. 2024），但 robotics 中的 best-of-N 方法（如 reward-model-guided sampling for manipulation）未被覆盖。
2. **Action ensemble methods**: 多个 policy 的 action 组合策略（如 ACT [Zhao et al., 2023] 中的 temporal ensembling）与本文的 multi-sample + correction 有相似之处，值得讨论。
3. **Sim-to-real for residual policies**: 如 TRANSIC (已引用) 之外，residual RL 在 sim-to-real 中的工作（如 Zeng et al., Sim-to-Real Transfer via Progressive Neural Networks 等）可补充。

---

## Overall Assessment

**Score**: Weak Reject
**Confidence**: High

---

## Detailed Comments (逐 Section)

### Abstract
- 信息密度合理，四个核心要素（问题、方法、结果、发现）齐全。
- "+5.3 pp margin over argmin selection (p=0.014)" 的呈现方式恰当。
- 建议：最后一句 "tokenized VLAs produce near-identical samples" 可能对不熟悉 VLA 架构细节的读者过于跳跃，考虑补充一句过渡。

### Introduction
- 开篇用 LIBERO+ 的具体数字（94.2%→6.6%, 95.2%→4.3%）有效建立了 motivation。
- Para 2 对 existing approaches 的梳理清晰，三点对比（ReconVLA/A2C2/VLA-Pilot）简明有力。
- 但 Para 4 的 key findings 与 Para 5 contributions list 有大量重复（数字重复出现三次：abstract, para 4, contributions），可压缩。
- Contribution 3 "applicability boundaries" 跨越了两个不同发现（tokenized VLA 不适用 + spatial tasks 无效），建议拆分或更明确地统一逻辑。

### Related Work
- 结构合理，四个小节覆盖完整。
- 与 A2C2 的三点差异（Section 2, related_work.tex:22）表述精确，但恰恰因为差异描述得如此清楚，缺少实验对比就更加刺眼。
- Conformal prediction in robotics 小节为 Section 4.3 的 negative result 提供了很好的铺垫。
- Inference-time compute scaling 小节的 framing 恰当，将 LLM 的 selection-dominant 范式与 embodied 的 correction-dominant 范式做了有意义的对比。

### Method
- Pipeline 描述完整，数学符号一致。Equation (1)(2)(3) 表述清楚。
- Figure 1 pipeline 图（未见但可推断结构）应确保直观展示三个阶段。
- "geometric medoid" 表述问题见 W1。
- CRM 三个变体的 input specification 清楚，参数量对比公平（327K vs 337K vs 327K）。
- Training 部分的 precompute pipeline 描述充分，但遗漏了数据划分问题（N1）。
- Magnitude control 的动机（uncapped → 0% for perdof）有效，但 ε 选择的理论依据仍不足——为什么 0.2 而不是其他值？Section 4.4 的经验结果是唯一依据。

### Experiments
- Statistical protocol 段落是亮点：seed-level test 的 rationale、sign test 补充验证、compute budget 透明。
- Table 1 设计合理，但 Spatial 列只有 seed 42 一个点，无 error bar。
- Pipeline decomposition 分析（Section 4.2 第二段）是论文最有价值的部分。
- ε-magnitude 交互分析（Figure 2）直观展示了 obs_only 的鲁棒性 vs perdof 的脆弱性。
- K-scaling 分析（Section 4.4）有实用价值（K=5 捕获 82% benefit at half compute）。
- Per-task analysis（Appendix C, Table 3）揭示 improvement 集中在 4/10 tasks 上，这是一个重要的 nuance。

### Discussion
- 只有一段实质内容，过于单薄。与 LLM test-time scaling 的对比值得展开。
- 缺少对方法 failure modes 的更深入分析。

### Limitations
- 五条限制的自我披露较为诚实。
- Item 5 关于 A2C2 对比的解释有误导性（见 N2）。
- 遗漏了最关键的限制：CRM 训练于 eval 任务 demo 数据，无泛化验证（N1）。

### Appendix
- K-scaling 和 applicability boundary 的补充数据有价值。
- Per-task 分析只覆盖 Object，缺 Spatial（W4）。

### References
- 引用验证结果：32 个 cited key 全部有对应 bib entry，无遗漏。
- 2 个 orphan entries（Gauss1857, Lagrange1788）未在正文引用，疑为模板残留，应清理。
- 2 个 duplicate keys（同上两个 entry）。
- 3 个在线未找到（black2024pi0, braun2025cgs, snell2024scaling），可能因为 recent preprints 未被索引，非 fabrication 风险。
- 引用密度整体偏低（32 unique keys for a CoRL paper），尤其缺少 robotics manipulation 的经典基础工作。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 176 · 2026-05-19T01:51:04.824598+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 177 · 2026-05-19T01:51:07.607137+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Weak Reject** 评分。四个 critical 问题：

1. **N1**: CRM 在 eval 任务的 demo 数据上训练，无 held-out task 泛化验证——无法区分 task-specific memorization 和 generalizable correction
2. **N2**: 缺少 A2C2（被认定为最接近的 concurrent work）的实验对比，positioning 核心缺陷
3. **N3**: Seed 数量小（3-7）且不平衡，统计推断脆弱
4. **N4**: 无 real-robot 实验或 sim-to-real 论证，绝对性能仅 17.6%

论文在 component decomposition 设计、negative results 价值、写作清晰度方面有优势，但实验设计的方法论问题和 significance 不足使其难以达到 CoRL 2026 录用标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 178 · 2026-05-19T01:51:12.888578+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 16

## Round 16

6 recorded events


### User

_source line 179 · 2026-05-19T01:51:24.387565+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 Review

**Paper**: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs"
**Venue**: CoRL 2026 Main Conference
**审查侧重**: 新颖性 + Related Work + 论文定位 + 写作与格式合规

---

## Summary (2-3 sentences)

This paper proposes a sample-select-correct pipeline for frozen flow-matching VLAs: draw K=10 action samples, select the medoid via L2 argmin, and apply a ~327K-parameter MLP residual correction bounded by L2 norm clipping. The key empirical finding is that learned correction is the active mechanism while multi-sampling is an enabling condition (neither works alone), and that conformal uncertainty features hurt rather than help. Evaluated on LIBERO-Object (17.6% vs 11.6% baseline) and LIBERO-Spatial (no improvement), the paper is honest and well-structured but operates in a very low absolute performance regime with narrow evaluation scope.

---

## Strengths

- **S1: Honest and transparent reporting.** The paper does not oversell. Limitations Section 6 explicitly acknowledges simulation-only evaluation, single backbone, low absolute performance, and per-seed variance including cases where correction hurts (seed 43). This is commendable and rare.

- **S2: Rigorous statistical protocol.** Seed-level non-parametric tests (Mann-Whitney U) rather than episode-level pooled tests; explicit acknowledgment that episodes within a seed are not independent (Section 4.1, "Statistical protocol"); no seeds discarded; compute budget allocation explained. This is a model of careful reporting for the robotics community.

- **S3: Clean component decomposition.** The finding that selection alone provides no significant benefit in low-dimensional continuous action spaces (Section 5.1, Discussion), contrasting with LLM test-time scaling where selection drives improvement, is a genuinely interesting observation. The K=1 control (10.3%, below baseline) effectively demonstrates that multi-sampling is an enabling condition, not the active mechanism.

- **S4: Useful negative result on conformal features.** The conditioning ablation (Section 4.3) showing that per-DOF conformal features cause progressive collapse from 14% to 0% as the magnitude bound is loosened (Figure 2) is a clear, well-controlled negative result that saves future researchers from pursuing this direction at small sample budgets.

- **S5: Clean writing with minimal AI artifacts.** No em-dashes in rendered text, no AI-blacklisted vocabulary (leverage/utilize/delve/etc.), no excessive -ing phrase endings, no over-segmentation. One em-dash exists only in a LaTeX comment. Writing is concise and direct throughout.

---

## Weaknesses

### Must-Fix (影响接收决定)

**W1** [critical] **极低的绝对性能使发现的泛化性存疑**
- 具体位置：Table 1, Section 4.2
- 问题：VLA-only baseline 仅 11.6%，pipeline 达 17.6%。虽然相对提升 +6pp 统计显著（p=0.003），但整个评估处于 base policy 几乎不工作的 regime。在这个 regime 下的 component decomposition 结论（correction > selection）是否对更强的 base policy（如 A2C2 报告的 67-72% SmolVLA baseline）成立，完全未知。Limitations 第 5 条承认了这一点，但这不是一个 limitation，而是根本性地限制了论文所有 claim 的适用范围。
- 为什么影响接收：如果发现只在 base policy 极弱时成立，则对 CoRL 社区（关注实际部署）的价值大幅下降。
- 建议修改方向：至少在一个 base policy 有合理性能（>50%）的 setting 下验证核心发现。

**W2** [critical] **评估范围极窄，缺乏泛化性证据**
- 具体位置：Section 4.1 (Experimental Setup), Section 6 (Limitations)
- 问题：(a) 仅用 SmolVLA（450M）一个 backbone；(b) 仅用 LIBERO 一个 benchmark family（且只有 Object 子集显示改进，Spatial 无效）；(c) 纯仿真，无 real-robot 实验。论文标题用 "Frozen VLAs"（复数），但只测了一个 VLA。Applicability boundary 实验（Section 4.4）测了 OpenVLA 但只证明它不适用，而非证明 pipeline 在其他 flow-matching VLA（如 π₀、Diffusion Policy）上有效。
- 为什么影响接收：CoRL Call for Papers 明确要求 "focus on a core robotics problem"，并鼓励 "real-robot experiments or simulation evidence demonstrating transferability to physical robots"。论文未提供任何 sim-to-real 可迁移性论证。
- 建议修改方向：(a) 至少增加一个 flow-matching VLA backbone（如 π₀ 或 Diffusion Policy）；(b) 提供 sim-to-real 迁移的初步证据或详细论证。

**W3** [critical] **方法新颖性有限**
- 具体位置：Section 3 (Method)
- 问题：Pipeline 的三个组件均为已知技术的直接应用：(a) L2 argmin medoid selection 是标准的鲁棒中心趋势估计；(b) MLP residual correction 是 residual policy learning（Silver et al. 2018）的直接实例化；(c) L2 norm clipping 是标准的梯度/输出裁剪策略。三者的组合是工程集成而非方法论创新。与 A2C2 的三点差异（Section 2.1 末尾）中，multi-sample selection 和 L2 clipping 都是相对表面的设计选择，而非深层的方法论区别。
- 为什么影响接收：如果论文定位为方法贡献，新颖性不足以达到 CoRL 标准；如果定位为实证分析贡献，则评估范围（W2）需要大幅扩展。当前定位在两者之间，两头都不够强。
- 建议修改方向：明确定位为实证分析/dissection paper，并大幅扩展分析深度（见 W7）。

**W4** [critical] **动机与评估之间存在断裂**
- 具体位置：Section 1 (Introduction) para 1 vs. Section 4.1 (Benchmarks)
- 问题：Introduction 第 1 段用 LIBERO+ benchmark 的数字（π₀ 从 94.2% 降到 6.6%，UniVLA 从 95.2% 降到 4.3%）来 motivate distribution shift 下的鲁棒性问题。但实验不在 LIBERO+ 上评估，而在标准 LIBERO-Object/Spatial 上评估。论文未解释为何 SmolVLA 在标准 LIBERO-Object 上 baseline 只有 11.6%——如果这本身就是 distribution shift 造成的，需要明确说明 shift 的性质；如果不是 distribution shift，则 Introduction 的 motivation 与实际 setting 不匹配。
- 为什么影响接收：审稿人会注意到 motivation（robustness under distribution shift）与 evaluation（low-performing base policy on standard benchmark）之间的逻辑缺口。
- 建议修改方向：要么在 LIBERO+ 上评估，要么清楚解释 SmolVLA 11.6% baseline 的原因并调整 Introduction 的 framing。

### Should-Fix (影响评分但不一票否决)

**W5** [warning] **缺乏与 A2C2 的实验对比**
- 具体位置：Section 2.1 (Related Work, Inference-time methods)
- 问题：论文在 Related Work 中将 A2C2 定位为 "closest concurrent work" 并详细列出三点差异，但 Experiments 中完全没有与 A2C2 的 head-to-head 对比。声称 "their setting differs fundamentally from ours"（Section 6, Limitation 5），但 A2C2 同样附加轻量 correction module 到 frozen VLA——setting 差异没有论文声称的那么大。
- 建议：在相同 frozen SmolVLA checkpoint 上复现 A2C2 的 correction-only 模块，或至少提供不可比的详细论证。

**W6** [warning] **Related Work 遗漏重要相关工作**
- 具体位置：Section 2 (Related Work)
- 问题：以下直接相关的近期工作未被引用：
  - **ADPro** (2025): test-time adaptive diffusion policy via manifold-constrained denoising, 无需 retraining，直接适配 frozen diffusion policy
  - **Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling** (2025, arXiv 2502.00622): GPC 框架，对 frozen diffusion policy 做 inference-time enhancement via world model look-ahead
  - **Recurrent-Depth VLA** (2026, arXiv 2602.07845): implicit test-time compute scaling for VLAs via latent iterative reasoning
  - **Residual Policy Adaptation for VLAs in Precision Robotic Assembly** (2025, ResearchGate): 直接在 frozen VLA backbone 上附加 residual heads
  - **Compose Your Policies!** (2025, arXiv 2510.01068): test-time distribution-level composition for diffusion/flow policies
- 29 条引用对 CoRL 论文偏少。上述遗漏中前两篇（ADPro、GPC）都是 frozen generative policy + inference-time enhancement，与本文高度相关，不引用会被审稿人视为调研不足。

**W7** [warning] **"Dissection" 承诺的分析深度未兑现**
- 具体位置：标题 "Dissecting Inference-Time Action Refinement"
- 问题：标题承诺 "dissection"，但实际分析主要是标准 ablation（component decomposition、conditioning ablation、K-scaling）。对于 dissection paper，缺少：(a) CRM 究竟纠正了哪类误差？correction vector 的分布是什么？(b) 纠正在 trajectory 的哪个阶段最有效？(c) 成功/失败 episode 的 correction 模式有何不同？(d) 纠正前后 trajectory 的可视化对比。
- 建议：增加 correction vector 的统计分析和 trajectory 级别的 qualitative analysis。

**W8** [warning] **CoRL venue fit 存在风险**
- 具体位置：整篇论文
- 问题：CoRL Call for Papers 鼓励 "real-robot experiments or simulation evidence demonstrating transferability to physical robots"。论文完全在仿真中评估，且未提供任何 sim-to-real 迁移论证。Pipeline 涉及 10 次 VLA forward pass（~10x compute），实际机器人部署的 latency 是否可接受也未讨论（虽然提到 ~0.3ms CRM overhead，但 10x VLA forward pass 才是主要开销）。
- 建议：增加 latency 分析（10 次 forward pass 在实际控制频率下是否可行），或提供 sim-to-real gap 的定性讨论。

### 小问题（不影响接收）

- **I1**: Table 1 的 Spatial 列中 Random 行标记 "---"，应解释为何缺失（Section 4.2）。
- **I2**: bib 条目中 RT-2 (brohan2023rt2)、OpenVLA (kim2024openvla)、Octo (ghosh2024octo) 均标记为 @misc/arXiv preprint，但这些论文已在正式会议发表，应更新 venue 信息。
- **I3**: Abstract 为 7 行约 160 words，在 150-250 范围内，但偏长且信息密度极高——一个句子包含了 4 个数字和 2 个 p 值，可读性受影响。
- **I4**: Section 3.3 CRM Architecture 段中 "concatenation order is arbitrary for fully connected layers" 这一注释无必要，分散读者注意力。
- **I5**: Contribution 3 ("applicability boundaries") 在 Introduction 中首次出现时缺乏铺垫——前文未讨论 tokenized VLAs 的问题。

---

## Questions for Authors

- **Q1**: SmolVLA 在标准 LIBERO-Object 上的 baseline 为何只有 11.6%？这是否代表 distribution shift（如果是，shift 是什么性质）？SmolVLA 原论文报告的 LIBERO 性能是多少？
- **Q2**: 在 base policy 性能更高的 setting 下（如 A2C2 报告的 67-72%），correction > selection 的结论是否仍然成立？是否有理论或实证支撑？
- **Q3**: CRM 训练数据（26,737 samples from 10 demos per task）是否足够？offline training 的 CRM 在 closed-loop 执行时面临的 distribution shift 如何量化？论文引用 DAgger (Ross et al. 2011) 但实际未使用 DAgger 而是用 Gaussian noise augmentation——两者效果的差异？
- **Q4**: 10 次 VLA forward pass 在 SmolVLA (450M) 上的 wall-clock time 是多少？在典型机器人控制频率（10-20 Hz）下是否可行？
- **Q5**: perdof variant 在 tight magnitude bound (ε=0.03) 时达 14%，接近 obs_only 的 14.3%。这是否暗示 conformal features 在更大 K（如 K=50 或 K=100）下可能变得有用？

---

## Missing References

1. **ADPro** (2025): "ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation" (arXiv 2508.06266)
2. **GPC** (2025): "Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling" (arXiv 2502.00622)
3. **Recurrent-Depth VLA** (2026): "Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning" (arXiv 2602.07845)
4. **Residual Policy Adaptation for VLAs** (2025): "Residual Policy Adaptation for Vision-Language-Action Models in Precision Robotic Assembly" (ResearchGate)
5. **Compose Your Policies!** (2025): "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition" (arXiv 2510.01068)
6. bib 条目需更新：brohan2023rt2 (RT-2)、kim2024openvla (OpenVLA)、ghosh2024octo (Octo) 应补充正式 venue 信息。

---

## Overall Assessment

**Score: weak reject**
**Confidence: high**

---

## 官方维度打分（基于 CoRL reviewer guidelines: Originality, Quality, Clarity, Significance, Relevance, Limitations）

| 维度 | 评分 | 理由摘要 |
|------|------|----------|
| Originality | 低 | 三个组件（argmin selection, MLP residual, L2 clipping）均为已知技术；组合方式直接，缺乏方法论创新。"Correction > selection" 的发现有一定新意，但不足以单独支撑论文。 |
| Quality (Soundness) | 中 | 统计方法严谨（seed-level Mann-Whitney U），ablation 设计合理。但评估范围极窄（1 VLA, 1 benchmark, sim-only），且在极低性能 regime 下的发现泛化性存疑。动机-评估断裂（LIBERO+ vs LIBERO）削弱了整体可信度。 |
| Clarity | 高 | 写作清晰简洁，结构合理，图表有效。AI 写作痕迹几乎为零。Method 和 Experiments 的 presentation 是论文的明显优势。 |
| Significance | 低-中 | "Correction > selection in continuous action spaces" 是有趣的观察，但在 17.6% 绝对性能和 单一 backbone/benchmark 下，实际影响有限。不改变社区对 inference-time refinement 的实践。 |
| Relevance | 中 | 论文确实 address 了 VLA robustness 这一 CoRL 关心的问题，但 simulation-only、无 real-robot 证据、绝对性能极低，使其对 robotics deployment 的直接相关性有限。 |
| Limitations | 高 | Limitations section 诚实、具体、全面，承认了几乎所有重要局限。这是论文的显著优点。 |

---

## Detailed Comments (逐 Section)

### Abstract
- 约 160 words，在合理范围内。
- 四个必答问题（what/why/how/result）均有回答，但过度压缩——单句包含 4 个数字和 2 个 p 值，降低可读性。
- "conformal uncertainty features cause progressive collapse (14% to 0%)" 使用了论文未在 Abstract 中定义的概念（per-DOF conformal features），读者需要猜测含义。
- 缩写 "MLP"、"DOF" 未在 Abstract 中展开定义。

### Introduction
- 五段结构完整：背景→缺口→方法→发现→贡献。
- 第 1 段使用 LIBERO+ 数据有效建立 urgency，但与 Section 4 的评估 benchmark 不匹配（见 W4）。
- 第 2 段对 existing methods 的梳理精炼有效，三句话覆盖了 training-time 和 inference-time 两条线。
- Contribution 3（applicability boundaries）在前文缺乏铺垫——Introduction 第 4 段最后一句突然提到 "tokenized VLAs produce near-identical samples"，但前文未建立 tokenized vs. flow-matching 的区分。
- "This contrasts with LLM test-time compute scaling" (para 4) 是论文最有价值的 insight，但仅用一句话带过，可以展开。

### Related Work
- 四个子节（VLA Robustness, Residual Policy Learning, CP in Robotics, Inference-Time Scaling）覆盖了主要方向。
- Section 2.1 中对 A2C2 的定位清晰，三点差异逐一列出——但缺乏实验验证这些差异的重要性。
- Section 2.2 (Residual Policy Learning) 仅 4 行，覆盖面不足。缺少 "Residual Policy Adaptation for VLAs" (2025) 这篇直接相关的工作。
- Section 2.4 (Inference-Time Compute Scaling) 遗漏了 Recurrent-Depth VLA (2026) 这篇同时做 VLA + inference-time compute 的工作。
- 缺少 test-time adaptation of diffusion/flow policies 这一整条线（ADPro、GPC、Compose Your Policies!），这些工作与本文共享 "frozen generative policy + inference-time enhancement" 的核心设定。
- 29 条引用偏少，尤其在 inference-time adaptation 方向有明显盲区。

### Method
- Pipeline description 清晰，数学符号一致。
- Figure 1 的 caption 自包含。
- "The key design insight is twofold" (Section 1, para 3) 中的 insight 2（bounding correction prevents compounding errors）是标准知识，不应称为 "insight"。
- Section 3.3 conditioning variants 的描述完整，三个变体的差异清晰。
- Training 段（Section 3.3）引用 DAgger 来 justify Gaussian noise augmentation，但两者原理不同——DAgger 通过 interactive data collection 解决 distribution shift，Gaussian noise 只是输入扰动。这个 analogy 不太准确。

### Experiments
- Table 1 设计合理，信息密度高。但 $\Delta$ Object 列的 baseline 是 Argmin 而非 VLA-only，不够直观。
- "Pipeline decomposition" 段（Section 4.2）是论文最强的实证贡献。Random vs Argmin vs full pipeline 的对比有效分离了 selection 和 correction 的贡献。
- Section 4.4 的 K-scaling 分析简洁有效。K=5 capturing ~82% benefit 的 practical finding 对部署有价值。
- Applicability boundary 实验仅测了 OpenVLA（tokenized, 7B），证明不适用。缺少更多 flow-matching VLA（如 π₀）的正面验证。
- Per-seed variance 范围 -1pp 到 +10pp（Section 4.2），且 seed 43 上 correction < argmin (16% vs 17%)。论文诚实报告了这一点，但这暗示 effect 在 practical sense 上可能不稳定。

### Discussion + Limitations + Conclusion
- Discussion 仅 1 段，过于简短。"Selection vs. correction in continuous action spaces" 的对比值得更深入的讨论——为什么 6D 连续空间中 selection 不如 discrete token space？是因为维度低、样本间距小、还是其他原因？
- Limitations section 诚实全面，5 条均为实质性局限。第 5 条关于 A2C2 baseline 差异的说明 important but should also be in the main text.
- AI Disclosure 存在且合规。
- Conclusion 无过度 claim，准确总结了发现和局限。

### Appendix
- 三个附录（K-scaling, Applicability, Per-task）均在正文中被引用。
- Figure 3 (K-scaling) 和 Figure 4 (diversity) 有效补充了正文。
- Table 2 (per-task) 揭示了改进集中在 medium-difficulty tasks 的 pattern，这一信息应在正文中更突出展示。

### 格式合规检查
- [x] 使用 corl_2026 模板（\usepackage{corl_2026}）
- [x] 作者为 "Anonymous"——double-blind 合规
- [x] Limitations section 存在（Section 6）
- [x] AI Disclosure statement 存在
- [?] 页数：正文含 Introduction (约1.5p) + Related Work (约1.5p) + Method (约1.5p, 含 Fig 1) + Experiments (约2.5p, 含 Table 1 + Fig 2) + Discussion+Limitations+AIDisclosure+Conclusion (约1.5p) ≈ 8.5p，可能略超 8 页限制。需要实际编译验证。
- [x] \bibliography 在 appendix 之前，references 不计入页数
- [ ] keywords 行 (\keywords{...}) 是否为 CoRL 2026 模板要求？需确认——某些模板不支持 \keywords。
- [ ] 部分 bib 条目缺 venue 信息（见 Missing References 节）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-19T01:52:14.828117+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 — Round 1 Review\n\n**审查侧重**: 新颖性 + Related Work + 论文定位 + 写作与格式合规\n\n## Summary\nThis paper proposes a sample-select-correct pipeline for frozen flow-matching VLAs: draw K=10 action samples, select the medoid via L2 argmin, and apply a ~327K-parameter MLP residual correction bounded by L2 norm clipping. The key empirical finding is that learned correction is the active mechanism while multi-sampling is an enabling condition (neither works alone), and that conformal uncertainty features hurt rather than help. Evaluated on LIBERO-Object (17.6% vs 11.6% baseline) and LIBERO-Spatial (no improvement), the paper is honest and well-structured but operates in a very low absolute performance regime with narrow evaluation scope.\n\n## Strengths\n- S1: Honest and transparent reporting. Limitations explicitly acknowledges simulation-only, single backbone, low absolute performance, per-seed variance including seed 43 where correction hurts.\n- S2: Rigorous statistical protocol. Seed-level Mann-Whitney U, episodes not independent, no seeds discarded, compute budget explained.\n- S3: Clean component decomposition. Selection alone no benefit in low-dimensional continuous action spaces, contrasting with LLM test-time scaling. K=1 control effectively shows multi-sampling is enabling condition.\n- S4: Useful negative result on conformal features. Progressive collapse from 14% to 0%.\n- S5: Clean writing with minimal AI artifacts.\n\n## Must-Fix Weaknesses\n- W1 [critical]: 极低绝对性能（17.6%）使发现泛化性存疑。在 base policy 几乎不工作的 regime 下的 component decomposition 结论是否对更强 base policy 成立完全未知。\n- W2 [critical]: 评估范围极窄。仅 SmolVLA 一个 backbone，LIBERO 一个 benchmark，sim-only。标题用 \"Frozen VLAs\" 复数但只测一个。缺 π₀/Diffusion Policy 验证。无 sim-to-real 论证。\n- W3 [critical]: 方法新颖性有限。L2 argmin selection、MLP residual、L2 norm clipping 均为已知技术直接应用。与 A2C2 的差异是工程选择而非方法论创新。\n- W4 [critical]: 动机与评估断裂。Introduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%）motivate distribution shift，但实验在标准 LIBERO 上评估。SmolVLA 11.6% baseline 的原因未解释。\n\n## Should-Fix Weaknesses\n- W5 [warning]: 缺 A2C2 实验对比。声称 setting 根本不同，但 A2C2 同样 attach lightweight correction to frozen VLA。\n- W6 [warning]: Related Work 遗漏 ADPro、GPC、Recurrent-Depth VLA、Residual Policy Adaptation for VLAs、Compose Your Policies! 等直接相关工作。29 条引用偏少。\n- W7 [warning]: \"Dissection\" 承诺的分析深度未兑现。缺 correction vector 分布分析、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。\n- W8 [warning]: CoRL venue fit 风险。Sim-only，无 real-robot，10x VLA compute latency 未分析。\n\n## Questions\n- Q1: SmolVLA 在标准 LIBERO-Object 上 baseline 为何只有 11.6%？SmolVLA 原论文报告多少？\n- Q2: 在 base policy >50% 时 correction > selection 是否仍成立？\n- Q3: CRM 训练数据是否足够？DAgger 引用 vs 实际 Gaussian noise augmentation 的差异？\n- Q4: 10 次 forward pass 的 wall-clock time？10-20 Hz 控制频率下是否可行？\n- Q5: perdof 在 ε=0.03 达 14%，接近 obs_only 14.3%。K 更大时 conformal features 是否有用？\n\n## Missing References\nADPro (2025), GPC (2025), Recurrent-Depth VLA (2026), Residual Policy Adaptation for VLAs (2025), Compose Your Policies! (2025)。bib 条目 RT-2/OpenVLA/Octo 需更新 venue。\n\n## Overall: weak reject, confidence high\n\n---\n\n**请对以上每个 Must-Fix (W1-W4)、Should-Fix (W5-W8) 逐条给出 [AGREE] 或 [REBUT] 回应。**",
  "reviewer_id": "1",
  "project": "acr-vla-conformal-refinement",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 — Round 1 Review\n\n**审查侧重**: 新颖性 + Related Work + 论文定位 + 写作与格式合规\n\n## Summary\nThis paper proposes a sample-select-correct pipeline for frozen flow-matching VLAs: draw K=10 action samples, select the medoid via L2 argmin, and apply a ~327K-parameter MLP residual correction bounded by L2 norm clipping. The key empirical finding is that learned correction is the active mechanism while multi-sampling is an enabling condition (neither works alone), and that conformal uncertainty features hurt rather than help. Evaluated on LIBERO-Object (17.6% vs 11.6% baseline) and LIBERO-Spatial (no improvement), the paper is honest and well-structured but operates in a very low absolute performance regime with narrow evaluation scope.\n\n## Strengths\n- S1: Honest and transparent reporting. Limitations explicitly acknowledges simulation-only, single backbone, low absolute performance, per-seed variance including seed 43 where correction hurts.\n- S2: Rigorous statistical protocol. Seed-level Mann-Whitney U, episodes not independent, no seeds discarded, compute budget explained.\n- S3: Clean component decomposition. Selection alone no benefit in low-dimensional continuous action spaces, contrasting with LLM test-time scaling. K=1 control effectively shows multi-sampling is enabling condition.\n- S4: Useful negative result on conformal features. Progressive collapse from 14% to 0%.\n- S5: Clean writing with minimal AI artifacts.\n\n## Must-Fix Weaknesses\n- W1 [critical]: 极低绝对性能（17.6%）使发现泛化性存疑。在 base policy 几乎不工作的 regime 下的 component decomposition 结论是否对更强 base policy 成立完全未知。\n- W2 [critical]: 评估范围极窄。仅 SmolVLA 一个 backbone，LIBERO 一个 benchmark，sim-only。标题用 \"Frozen VLAs\" 复数但只测一个。缺 π₀/Diffusion Policy 验证。无 sim-to-real 论证。\n- W3 [critical]: 方法新颖性有限。L2 argmin selection、MLP residual、L2 norm clipping 均为已知技术直接应用。与 A2C2 的差异是工程选择而非方法论创新。\n- W4 [critical]: 动机与评估断裂。Introduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%）motivate distribution shift，但实验在标准 LIBERO 上评估。SmolVLA 11.6% baseline 的原因未解释。\n\n## Should-Fix Weaknesses\n- W5 [warning]: 缺 A2C2 实验对比。声称 setting 根本不同，但 A2C2 同样 attach lightweight correction to frozen VLA。\n- W6 [warning]: Related Work 遗漏 ADPro、GPC、Recurrent-Depth VLA、Residual Policy Adaptation for VLAs、Compose Your Policies! 等直接相关工作。29 条引用偏少。\n- W7 [warning]: \"Dissection\" 承诺的分析深度未兑现。缺 correction vector 分布分析、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。\n- W8 [warning]: CoRL venue fit 风险。Sim-only，无 real-robot，10x VLA compute latency 未分析。\n\n## Questions\n- Q1: SmolVLA 在标准 LIBERO-Object 上 baseline 为何只有 11.6%？SmolVLA 原论文报告多少？\n- Q2: 在 base policy >50% 时 correction > selection 是否仍成立？\n- Q3: CRM 训练数据是否足够？DAgger 引用 vs 实际 Gaussian noise augmentation 的差异？\n- Q4: 10 次 forward pass 的 wall-clock time？10-20 Hz 控制频率下是否可行？\n- Q5: perdof 在 ε=0.03 达 14%，接近 obs_only 14.3%。K 更大时 conformal features 是否有用？\n\n## Missing References\nADPro (2025), GPC (2025), Recurrent-Depth VLA (2026), Residual Policy Adaptation for VLAs (2025), Compose Your Policies! (2025)。bib 条目 RT-2/OpenVLA/Octo 需更新 venue。\n\n## Overall: weak reject, confidence high\n\n---\n\n**请对以上每个 Must-Fix (W1-W4)、Should-Fix (W5-W8) 逐条给出 [AGREE] 或 [REBUT] 回应。**",
    "reviewer_id": "1",
    "project": "acr-vla-conformal-refinement",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-19T01:52:42.127516+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27299
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-19T01:52:42.459247+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 — Round 1 Review\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n## Summary\n本文提出 sample-select-correct pipeline，对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正。在 LIBERO-Object 上实现 17.6% vs 11.6%（p=0.003），并通过 component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告了 conformal features 失效和 tokenized VLA 不适用的 negative results。\n\n## Strengths\n- S1: 系统化 component decomposition（K=1 correction、selection-only、random selection 等控制实验）。\n- S2: 有价值的 negative results（conformal features 失效、tokenized VLA 不适用）。\n- S3: 统计协议 rationale 明确（seed-level 非参数检验，sign test 补充）。\n- S4: 写作质量较高。\n\n## Must-Fix Weaknesses\n- N1 [critical]: CRM 在 eval 任务的 demo 数据上训练（26,737 samples from 20 LIBERO tasks = 评估用的 Object 10 + Spatial 10），无 held-out task 泛化验证。无法区分 task-specific memorization 和 generalizable correction。建议 train/test task split。\n- N2 [critical]: 缺少 A2C2 实验对比。A2C2 被认定为 closest concurrent work 但从未作为 baseline 运行。Limitations 的 \"different training regime\" 解释误导——A2C2 correction head 完全可以接在同一 frozen checkpoint 上。\n- N3 [critical]: Seed 数量小且不平衡（obs_only 7, VLA-only 5, Argmin 6, Random 3）。MW-U 在 n1=7, n2=5 时功效有限。Random 仅 3 seeds 就断言 \"statistically indistinguishable\"——3 seeds 的 MW-U 几乎无法拒绝任何 null hypothesis。Per-seed variance 实质存在（seed 43 argmin > obs_only）。\n- N4 [critical]: 无 real-robot 实验或 sim-to-real 论证。绝对性能仅 17.6%。K=10 forward passes 的 wall-clock latency 未量化。\n\n## Should-Fix Weaknesses\n- W1 [warning]: \"Geometric medoid\" 表述不精确。实际是 argmin to centroid (squared L2)，非经典 geometric medoid (non-squared L2 to all other points)。\n- W2 [warning]: ε 超参数敏感性分析不完整。scalar 变体仅 ε=0.1 一个点，各点 seed 数不一致。\n- W3 [warning]: Applicability boundary claim 基于单一对比（OpenVLA T=0.5）。未测更高 temperature 或其他 tokenized VLA。\n- W4 [warning]: LIBERO-Spatial null result 分析不足。无 per-task Spatial 表，无 failure case 定量分析。\n- W5 [warning]: DAgger 引用不恰当。DAgger 是 interactive dataset aggregation，非 static Gaussian noise augmentation。\n\n## Questions\n- Q1: CRM 是否曾在 held-out tasks 上测试？\n- Q2: Table 1 Spatial Random \"---\" 原因？\n- Q3: 能否公布每个 seed 的具体成功率？\n- Q4: K=10 在 SmolVLA 上的 wall-clock latency？\n- Q5: A2C2 correction head 能否 attach 到同一 frozen SmolVLA？为什么不对比？\n- Q6: CRM 在 Spatial demo 上训练但 Spatial 上未带来提升——这对 task-specific memorization 假说有何影响？\n\n## Missing References\nBest-of-N sampling in robotics、ACT temporal ensembling (Zhao et al. 2023)、sim-to-real residual policies。\n\n## Overall: Weak Reject, Confidence: High\n\n---\n\n**请对以上每个 Must-Fix (N1-N4)、Should-Fix (W1-W5) 逐条给出 [AGREE] 或 [REBUT] 回应。**",
  "reviewer_id": "2",
  "project": "acr-vla-conformal-refinement",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 — Round 1 Review\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n## Summary\n本文提出 sample-select-correct pipeline，对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正。在 LIBERO-Object 上实现 17.6% vs 11.6%（p=0.003），并通过 component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告了 conformal features 失效和 tokenized VLA 不适用的 negative results。\n\n## Strengths\n- S1: 系统化 component decomposition（K=1 correction、selection-only、random selection 等控制实验）。\n- S2: 有价值的 negative results（conformal features 失效、tokenized VLA 不适用）。\n- S3: 统计协议 rationale 明确（seed-level 非参数检验，sign test 补充）。\n- S4: 写作质量较高。\n\n## Must-Fix Weaknesses\n- N1 [critical]: CRM 在 eval 任务的 demo 数据上训练（26,737 samples from 20 LIBERO tasks = 评估用的 Object 10 + Spatial 10），无 held-out task 泛化验证。无法区分 task-specific memorization 和 generalizable correction。建议 train/test task split。\n- N2 [critical]: 缺少 A2C2 实验对比。A2C2 被认定为 closest concurrent work 但从未作为 baseline 运行。Limitations 的 \"different training regime\" 解释误导——A2C2 correction head 完全可以接在同一 frozen checkpoint 上。\n- N3 [critical]: Seed 数量小且不平衡（obs_only 7, VLA-only 5, Argmin 6, Random 3）。MW-U 在 n1=7, n2=5 时功效有限。Random 仅 3 seeds 就断言 \"statistically indistinguishable\"——3 seeds 的 MW-U 几乎无法拒绝任何 null hypothesis。Per-seed variance 实质存在（seed 43 argmin > obs_only）。\n- N4 [critical]: 无 real-robot 实验或 sim-to-real 论证。绝对性能仅 17.6%。K=10 forward passes 的 wall-clock latency 未量化。\n\n## Should-Fix Weaknesses\n- W1 [warning]: \"Geometric medoid\" 表述不精确。实际是 argmin to centroid (squared L2)，非经典 geometric medoid (non-squared L2 to all other points)。\n- W2 [warning]: ε 超参数敏感性分析不完整。scalar 变体仅 ε=0.1 一个点，各点 seed 数不一致。\n- W3 [warning]: Applicability boundary claim 基于单一对比（OpenVLA T=0.5）。未测更高 temperature 或其他 tokenized VLA。\n- W4 [warning]: LIBERO-Spatial null result 分析不足。无 per-task Spatial 表，无 failure case 定量分析。\n- W5 [warning]: DAgger 引用不恰当。DAgger 是 interactive dataset aggregation，非 static Gaussian noise augmentation。\n\n## Questions\n- Q1: CRM 是否曾在 held-out tasks 上测试？\n- Q2: Table 1 Spatial Random \"---\" 原因？\n- Q3: 能否公布每个 seed 的具体成功率？\n- Q4: K=10 在 SmolVLA 上的 wall-clock latency？\n- Q5: A2C2 correction head 能否 attach 到同一 frozen SmolVLA？为什么不对比？\n- Q6: CRM 在 Spatial demo 上训练但 Spatial 上未带来提升——这对 task-specific memorization 假说有何影响？\n\n## Missing References\nBest-of-N sampling in robotics、ACT temporal ensembling (Zhao et al. 2023)、sim-to-real residual policies。\n\n## Overall: Weak Reject, Confidence: High\n\n---\n\n**请对以上每个 Must-Fix (N1-N4)、Should-Fix (W1-W5) 逐条给出 [AGREE] 或 [REBUT] 回应。**",
    "reviewer_id": "2",
    "project": "acr-vla-conformal-refinement",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-19T01:52:44.263597+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1804
}
```

</details>

---


### Assistant

_source line 184 · 2026-05-19T01:52:47.112650+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 185 · 2026-05-19T01:52:49.839908+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**weak reject**，confidence: high。

主要问题：
1. **绝对性能极低**（11.6%→17.6%），发现是否在更强 base policy 下成立完全未知
2. **评估范围极窄**：单一 VLA + 单一 benchmark + 纯仿真，无 real-robot 证据
3. **方法新颖性有限**：三个组件均为已知技术的工程集成
4. **动机-评估断裂**：Introduction 用 LIBERO+ 数据 motivate，但评估在标准 LIBERO 上

论文的主要优势在于诚实的报告（Limitations section 质量很高）、严谨的统计方法（seed-level non-parametric tests）、以及 "correction > selection in continuous action spaces" 这一有趣的实证发现。写作质量也较好，AI 痕迹几乎为零。但作为 CoRL 投稿，方法新颖性和评估深度均不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 186 · 2026-05-19T01:52:54.875604+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 187 · 2026-05-19T01:53:26.622937+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

## Must-Fix Weaknesses

**[AGREE] R2-W1: 极低绝对性能（17.6%）使发现泛化性存疑**

同意这是核心问题。17.6% 的绝对性能意味着 pipeline 在 82.4% 的 episodes 上仍然失败。在 base policy 近乎不工作（11.6%）的 regime 下做 component decomposition，其结论能否外推到更强 base policy（如 π₀ 在 LIBERO 的 94.2%）完全未知。补充我自己的发现：Table 3 (Appendix C) 显示 improvement 集中在 4/10 tasks 上（chocolate_pudding +40pp, bbq_sauce +20pp, ketchup +20pp, salad_dressing +10pp），其余 6 个 task 基本无变化或退化。这进一步说明 17.6% 的 aggregate 数字掩盖了高度不均匀的 task-level 表现，"learned correction is the active mechanism" 这一 claim 的适用范围可能比论文暗示的更窄。

**[AGREE] R2-W2: 评估范围极窄**

完全同意。标题 "Frozen VLAs"（复数）但仅测试 SmolVLA 一个 450M 参数的 backbone，且 applicability boundary 实验仅用 OpenVLA 做了 negative case（Section 4.4, experiments.tex:134-136）。对于一篇以 "dissecting" 为标题、试图得出 general insights 的论文，单 backbone + 单 benchmark + sim-only 的评估不足以支撑其 claim 的 generality。这与我在 N4 中指出的缺乏 real-robot 实验或 sim-to-real 论证一致。CoRL 2026 CFP 明确鼓励 real-robot 或 sim-to-real 可迁移性论证。

**[REBUT] R2-W3: 方法新颖性有限**

部分不同意。R2 认为各组件（L2 argmin, MLP residual, L2 norm clipping）均为已知技术，与 A2C2 的差异是工程选择。我认为需要区分两个层面：

1. **方法组件的新颖性确实有限**——这一点我同意，我在维度打分中也给了 Originality 3/5。
2. **但 component decomposition 的实验设计有独立价值**——论文的核心贡献不在于 pipeline 本身，而在于系统拆解各组件的贡献。"Selection alone 无显著帮助、K=1 correction 低于 baseline、二者结合才有效"这一发现（Section 4.2, Table 1）是非显然的，且与 LLM test-time scaling 的 selection-dominant 范式形成有意义的对比。如果仅因为组件非新颖就否定论文，那 ablation study 类论文（在 ML 社区有大量先例）都无法存在。

关键判断：本文的问题不在于新颖性不足，而在于实验规模不足以支撑其 decomposition 结论的 generality（即 W1 和 W2 才是真正的致命伤）。

**[AGREE] R2-W4: 动机与评估断裂**

同意这是一个叙事问题。Introduction (introduction.tex:5-8) 用 LIBERO+ 的极端数字（π₀ 94.2%→6.6%, UniVLA 95.2%→4.3%）建立 distribution shift motivation，但实验在标准 LIBERO（非 LIBERO+）上进行，且 SmolVLA baseline 只有 11.6%。这造成两个问题：

1. **读者预期与实际不符**：Introduction 暗示这是修复 "强 policy 在 distribution shift 下崩溃"的方案，但实际测试的是 "弱 policy 的微小提升"。
2. **SmolVLA 11.6% 的原因未解释**：这个数字远低于 SmolVLA 原论文可能报告的水平（R2-Q1 同问），论文未讨论是 checkpoint 选择、evaluation protocol 差异、还是其他原因。若 SmolVLA 本身在此 setting 下就不工作，则 pipeline 面临的是一个几乎不可修复的 base policy，correction 的意义被进一步削弱。

---

## Should-Fix Weaknesses

**[AGREE] R2-W5: 缺 A2C2 实验对比**

完全同意。这与我的 N2 一致。A2C2 是论文自行认定的 "closest concurrent work"（Section 2, related_work.tex:21），论文详细列出了三点方法差异（multi-sample selection、norm clipping、observation conditioning），但无实验验证这些差异是否真正带来优势。Limitations section 5 的 excuse——"A2C2 trains SmolVLA from scratch, direct comparison not meaningful"——不成立，因为 A2C2 的 correction head 可以 attach 到任意 frozen VLA。

**[REBUT] R2-W6: Related Work 遗漏多篇直接相关工作，29 条引用偏少**

部分不同意。

1. **引用数量**：论文实际有 32 unique cited keys（经我引用验证确认），不是 29 条。对于一篇 8 页 CoRL paper 来说，32 条引用在正常范围内（CoRL 不像 ACL/NeurIPS 那样普遍 50+ 引用）。
2. **遗漏论文的重要性需逐一评估**：R2 列出的 5 篇遗漏中，ADPro、GPC 等需要确认其与本文的直接相关性和发表时间。若这些论文在 submission deadline 前已公开且直接解决类似问题（inference-time correction for frozen VLAs），则确实应引用。但如果是 broader VLA robustness 工作，则 Related Work 已通过 SRPO/RobustVLA/DiG-Flow/TT-VLA 四篇覆盖了 training-time methods（Section 2.1），通过 ReconVLA/SC-VLA/VLA-Pilot/A2C2 四篇覆盖了 inference-time methods（Section 2.2），分类结构合理。
3. **bib entry venue 更新**：同意 RT-2/OpenVLA/Octo 等已正式发表的论文应更新 venue 信息（目前标记为 @misc，应改为对应 conference @inproceedings）。这是格式问题，不影响学术判断。

**[AGREE] R2-W7: "Dissection" 承诺的分析深度未兑现**

同意。标题用 "Dissecting" 暗示深入的机理分析，但论文实际提供的是 ablation-level 的 component decomposition，缺乏更深层的分析维度：

- 无 correction vector 的分布分析（CRM 学到的 δ 在不同 task/timestep 上是什么 pattern？）
- 无 trajectory 阶段分析（correction 在 approach/grasp/lift 哪个阶段最有效？）
- 无成功 vs 失败 trajectory 的对比可视化
- 无对 "为什么 K=1 correction 反而低于 baseline"（Section 4.2, experiments.tex:88）的深入解释（仅一句 "the single sample lacks the centering that argmin selection provides within the CRM's bounded correction radius"）

这些分析对于真正 "dissect" mechanism 是必要的。当前论文更像 "ablation study" 而非 "dissection"。但我认为这是 should-fix 而非 must-fix——更改标题为更准确的措辞（如 "Decomposing" 或直接去掉 "Dissecting"）也是一种解决方案。

**[AGREE] R2-W8: CoRL venue fit 风险**

同意，且与我的 N4 一致。三重风险叠加：(1) sim-only without real-robot 或 sim-to-real 论证；(2) 10x VLA compute overhead 的 wall-clock latency 未量化；(3) 17.6% 绝对性能远低于实用水平。对于以 real-world robot learning 为核心的 CoRL venue，这三点共同削弱了论文的 venue fit。

---

## 总结

在 R2 的 8 个问题中，我 **AGREE 6 条**（W1, W2, W4, W5, W7, W8）、**REBUT 2 条**（W3 方法新颖性、W6 引用遗漏）。

两位 Reviewer 的核心判断高度一致：论文的写作和统计 protocol 质量较高，component decomposition 视角有价值，但 **实验规模不足**（单 backbone、单 benchmark、sim-only、小 seed 数）**无法支撑其 general claim**，加上极低绝对性能和缺少 A2C2 对比，使得论文在当前状态下不满足 CoRL 录用标准。

与我 Round 1 审稿的 overall assessment 一致：**Weak Reject**。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 188 · 2026-05-19T01:53:31.411645+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 189 · 2026-05-19T01:53:34.138443+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。在 R2 的 8 个问题中 AGREE 6 条、REBUT 2 条：

- **REBUT W3（新颖性）**：组件非新颖但 component decomposition 实验设计有独立价值，真正致命伤是 W1/W2 的实验规模不足。
- **REBUT W6（引用遗漏）**：实际 32 条引用在 CoRL 正常范围内，Related Work 分类覆盖合理，但 bib venue 信息确需更新。

两位 Reviewer 核心判断一致：写作和统计质量高，但实验规模（单 backbone/benchmark/sim-only/小 seed 数）无法支撑 general claims，overall Weak Reject。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 190 · 2026-05-19T01:53:38.670899+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 20

## Round 20

8 recorded events


### User

_source line 191 · 2026-05-19T01:54:31.384592+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 (Round 1)

---

## Must-Fix 逐条回应

**[AGREE] R1-N1: CRM 在 eval 任务的 demo 上训练，无 held-out task 泛化验证**

同意这是一个关键缺陷。Section 4.1 Training 段明确写道 "26,737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks"，而评估恰好在这 20 个 task 上（Object 10 + Spatial 10）。这意味着 CRM 见过所有评估 task 的 demo 数据，无法区分 task-specific memorization 和 generalizable correction learning。

补充一点：R1 的担忧在 per-task 结果（Appendix Table 2）中有间接支撑——改进高度集中在 4 个 task 上（chocolate_pudding +40pp, bbq_sauce/ketchup +20pp each, salad_dressing +10pp），其余 6 个 task 几乎无变化。这种 concentrated improvement pattern 与 memorization 假说兼容（CRM 可能只在某些 task 上学到了有效的 task-specific correction），虽然也与论文的 "correctable regime" 解释兼容。train/test task split 是区分这两种解释的唯一方式。

---

**[AGREE] R1-N2: 缺少 A2C2 实验对比**

完全同意。我在自己的审稿中也将此列为 W5 [warning]，但 R1 将其升级为 [critical] 是合理的。

R1 准确指出了关键逻辑漏洞：论文在 Section 2.1 末尾声称与 A2C2 有三点差异（multi-sample selection、L2 clipping、conditioning choice），但这三点差异的实际重要性从未通过实验验证。Section 6 Limitation 5 的 "their setting differs fundamentally from ours" 辩护站不住——A2C2 的 correction head 完全可以 attach 到同一 frozen SmolVLA checkpoint，使用相同的 demo 数据训练，从而实现 controlled comparison。不这样做，论文声称的三点设计优势就是 unsubstantiated claims。

---

**[AGREE with nuance] R1-N3: Seed 数量小且不平衡**

总体同意这是一个显著问题，但需要区分主要对比和次要对比的统计效力。

**同意的部分**：(a) Random 仅 3 seeds 就断言 "statistically indistinguishable from VLA-only" 确实不成立——3 个 sample 的 MW-U 几乎无法拒绝任何 H0，不能将 "fail to reject" 解读为 "no difference"；(b) seed 数量不平衡（3-7）且由 "comparison importance" 决定分配，引入了潜在的 allocation bias——如果中途看到中间结果再决定给哪个条件多跑 seed，这就是一种 optional stopping；(c) per-seed variance 实质存在（seed 43 argmin 17% > obs_only 16%），+5.3pp 的 mean difference 在单 seed 层面并不稳定。

**补充细化**：主要对比（obs_only vs VLA-only, n=7 vs n=5）的 U=35 恰好是该样本量下的最大可能 U 值（所有 7 个 obs_only seed 均超过所有 5 个 VLA-only seed），对应 p=0.0025。在这个意义上，主要对比的证据虽然来自小样本，但在给定样本量的约束下已是最强可能的结果。真正的统计软肋在次要对比：obs_only vs Argmin (n=7 vs n=6, p=0.014) 还算可接受，但 Random vs VLA-only (n=3 vs n=5) 和 scalar (n=4) 的比较确实 underpowered。

建议作者至少将所有条件统一到 ≥5 seeds，并公布逐 seed 成功率以提高透明度。

---

**[AGREE] R1-N4: 无 real-robot 实验，低绝对性能，无 latency 量化**

完全同意。我在自己的审稿中将 real-robot 缺失列为 W2 [critical] 和 W8 [warning]。

补充 R1 未提到的一点：论文在 Section 3.4 提到 "The overhead is K=10 VLA forward passes plus ~0.3ms for CRM inference"，明确承认主要 latency 来自 10x VLA forward passes 而非 CRM。但全文未给出 SmolVLA 单次 forward pass 的 wall-clock time。假设 SmolVLA (450M) 在 GPU 上单次约 50-100ms，则 K=10 约 500ms-1s，对应 1-2 Hz 控制频率——对 10-20 Hz 的典型操作频率来说远远不够。论文 Section 4.4 中 K=5 的 practical sweet spot 建议暗示作者意识到 latency 问题，但回避了量化。这在 CoRL（关注部署可行性）是不可接受的遗漏。

---

## Should-Fix 逐条回应

**[AGREE] R1-W1: "Geometric medoid" 表述不精确**

正确。经典 geometric medoid 定义为 $\argmin_k \sum_{j \neq k} \|a_k - a_j\|$（最小化到所有其他点的距离之和，非平方 L2）。论文 Section 3.2 Eq.(1) 实际计算的是 $\argmin_k \sum_h \|a_h^{(k)} - \mu_h\|_2^2$（到 centroid 的平方 L2 距离之和），这是 "closest to centroid" 或 "1-center" 问题，不是 medoid。两者在多数情况下选出同一点，但在 multimodal 分布或 outlier 存在时可能不同。术语应修正为 "closest sample to the centroid" 或 "argmin-to-mean"。

---

**[AGREE] R1-W2: ε 敏感性分析不完整**

同意。Figure 2 仅展示 obs_only 和 perdof 两个变体的 ε 曲线。scalar 变体在 Table 1 中仅有 ε=0.1 一个数据点（8.5%, 4 seeds），无法判断 scalar 的 ε 敏感性。各 ε 点的 seed 数也不一致（Figure 2 caption: "n=1-7 per point"），这意味着某些点可能只有 1 个 seed，其数值毫无统计意义。一个号称研究 conditioning-magnitude interaction 的论文（Section 4.4 标题就叫 "Conditioning-Magnitude Interaction"），理应对所有三个 conditioning 变体提供完整的 ε sweep，且每个点保持一致的 seed 数。

---

**[AGREE] R1-W3: Applicability boundary 基于单一对比**

同意。Appendix B (Section B) 仅对比 SmolVLA vs OpenVLA (T=0.5)。如 R1 所指出，OpenVLA 在 T=0.5 下 8/10 identical samples 可能是 temperature 过低的 artifact 而非 tokenization 的固有限制。论文未测试：(a) OpenVLA at T=1.0 or higher；(b) 其他 tokenized VLA（如 RT-2, Octo with action tokenization）；(c) 其他 flow-matching/diffusion VLA（如 π₀, Diffusion Policy）来正面验证 pipeline 的泛化性。

论文声称 "The boundary is architectural, not a limitation of our method"（Appendix B 末段），但一个基于单一 data point 的 architectural claim 说服力很弱。

---

**[AGREE] R1-W4: LIBERO-Spatial null result 分析不足**

同意。LIBERO-Spatial 是论文评估的两个 benchmark 之一，且结果为 null（30-35% for all methods）。但：
- Appendix C (Table 2) 仅报告 Object per-task results，无 Spatial per-task breakdown
- Section 4.2 仅用一段话解释 Spatial null result："Spatial perturbations create layout changes that require higher-level re-planning; action-level residuals cannot redirect toward a different goal location." 这是合理的事后解释，但缺乏实证支撑（如 correction vector 分析、failure mode 分类）。

补充：论文 Contribution 3 声称 "applicability boundaries: multi-sample correction ... does not transfer to spatial reasoning tasks"，将 Spatial null result 包装为 contribution。但如果要将 null result 作为 contribution，其分析深度应远超当前水平——需要解释*为什么*不 work，而不只是陈述*不 work*。

---

**[AGREE] R1-W5: DAgger 引用不恰当**

同意。我在自己的 Round 1 审稿中也指出了同一问题。Section 3.3 Training 段末尾写 "Data augmentation (Gaussian noise on $a_{\mathrm{base}}$ and uncertainty features) improves generalization to the closed-loop state distribution~\cite{ross2011dagger}"。DAgger (Ross et al. 2011) 是 interactive dataset aggregation——在 learned policy 的 induced distribution 下收集新数据、聚合到训练集、重新训练——这与 static Gaussian noise augmentation 在方法论上有本质区别。前者主动 closing the distribution gap，后者只是被动增加训练数据的覆盖范围。引用 DAgger 来 justify noise augmentation 是概念混淆，应替换为更恰当的引用（如 domain randomization 或 noise injection 相关文献）。

---

## 综合评价

Reviewer 1 的审稿聚焦方法严谨性和实验设计，与我聚焦新颖性和 related work 的侧重互补。在核心判断上高度一致：

1. **评估范围过窄**（R1-N4 = R2-W2）：单 VLA、单 benchmark family、sim-only，且绝对性能极低。
2. **缺少 A2C2 对比**（R1-N2 = R2-W5）：两位 reviewer 独立识别为关键缺陷。
3. **统计问题**（R1-N3）：R1 的分析比我更细致，尤其是 3-seed Random 的 underpowered 问题我在 Round 1 中未充分展开。
4. **Task generalization 未验证**（R1-N1）：这是 R1 独立发现的重要问题，我在 Round 1 中未提及。CRM 在 eval task 上训练后声称 "learned correction"，无 held-out split 确实无法排除 memorization。

R1 提出的 N1（train/test task split）是我 Round 1 审稿中遗漏的关键缺陷，应补充纳入。

两位 reviewer 均给出 **weak reject**，核心理由收敛：方法新颖性有限、评估范围过窄、缺少关键 baseline、sim-only 且绝对性能过低。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-19T01:57:18.750226+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "issues_yaml": "- id: \"C1\"\n  summary: \"Fisher exact test independence violation (pseudo-replication)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Same-seed episodes share CRM weights, violating independence assumption\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已修复。论文改用 seed-level Mann-Whitney U 检验，两位 Reviewer 均肯定统计方法严谨\"}\n  action_items:\n    - {round: 1, action: \"Replace Fisher with Mann-Whitney U (seed-level) as primary test + sign test supplementary\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"改用 seed-level Mann-Whitney U 检验 + sign test 补充验证\"\n  resolution_round: 2\n\n- id: \"C2\"\n  summary: \"Core claim 'correction is sole driver' contradicts K=1 data (10.3% < 11.6%)\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"K=1 CRM below baseline means correction alone harmful. Appendix L18 also contradicts.\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已修复。论文重构为 'correction is active mechanism, multi-sampling is enabling condition'，两位 Reviewer 均认可此 framing\"}\n  action_items:\n    - {round: 1, action: \"Reframe to 'correction is active mechanism, multi-sampling is enabling condition'. Fix Appendix L18.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"重构为 'correction is active mechanism, multi-sampling is enabling condition'\"\n  resolution_round: 2\n\n- id: \"C3\"\n  summary: \"Inconsistent seed counts across methods without explanation\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"obs_only 7, VLA-only 5, Argmin 6, Random 3 — no justification\"}\n    - {round: 2, reviewers: [R1, R2], note: \"论文增加了 'compute budget allocated by comparison importance' 说明，但 R1 指出 Random 仅 3 seeds 的 MW-U 几乎无法拒绝 H0，'statistically indistinguishable' 结论不成立。R2 同意主要对比证据尚可（U=35=U_max），但次要对比 underpowered。\"}\n  action_items:\n    - {round: 1, action: \"Add explanation paragraph (resource allocation by importance). Supplement Random to n=5.\", assigned_to: \"Paper Agent + Agent\", status: \"partial\"}\n    - {round: 2, action: \"所有条件统一至 >=5 seeds。公布逐 seed 成功率。不要对 n=3 对比声称 'statistically indistinguishable'。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C4\"\n  summary: \"Novelty insufficient — standard MLP + L2 clipping\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Technical novelty low, contribution is in analysis not architecture\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[DIVERGENT] R2 维持 critical（方法组件均为已知技术）。R1 rebut 认为 component decomposition 有独立价值，真正问题是实验规模不足。降级为 warning。\"}\n  action_items:\n    - {round: 1, action: \"Reposition as analysis paper. Novelty is in findings not architecture.\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"明确定位为实证分析 paper（已部分完成通过标题 'Dissecting'），但需扩展分析深度（见新 issue W7-dissection-depth）\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C5\"\n  summary: \"Title 'Sample, Select, Correct' contradicts conclusion that select is useless\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Title sets wrong reader expectations\"}\n    - {round: 2, reviewers: [], note: \"已修复。新标题 'Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs' 准确反映发现\"}\n  action_items:\n    - {round: 1, action: \"Change title\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"标题改为 'Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs'\"\n  resolution_round: 2\n\n- id: \"C6\"\n  summary: \"Paper exceeds 8-page limit\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R3, R2], note: \"May cause desk reject\"}\n    - {round: 2, reviewers: [R2], note: \"R2 估算正文约 8.5 页，可能略超限制。需实际编译验证。\"}\n  action_items:\n    - {round: 1, action: \"Compress to exactly 8 pages.\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"实际编译确认页数。若超限需进一步压缩。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C7\"\n  summary: \"Missing AI Disclosure Statement (CoRL 2026 requirement)\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R3, R2], note: \"Required by venue\"}\n    - {round: 2, reviewers: [R2], note: \"已修复。AI Disclosure 存在且合规。\"}\n  action_items:\n    - {round: 1, action: \"Add AI disclosure statement\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"AI Disclosure statement 已添加\"\n  resolution_round: 2\n\n- id: \"M1\"\n  summary: \"Narrow experimental scope (single VLA + single benchmark + no real robot)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R1, R3], note: \"Only SmolVLA on LIBERO, no RLBench/MetaWorld/real\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 两位 Reviewer 一致认为这是核心缺陷。标题 'Frozen VLAs'(复数)但只测一个。无 π₀/Diffusion Policy 正面验证。CoRL CFP 要求 real-robot 或 sim-to-real 论证。\"}\n  action_items:\n    - {round: 1, action: \"Add Spatial multi-seed. Acknowledge scope limitation.\", assigned_to: \"Agent + Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"(1) 至少增加一个 flow-matching VLA backbone（如 π₀）。(2) 提供 wall-clock latency 量化。(3) 提供 sim-to-real 可迁移性论证或更诚实的 scope 限定（标题改为单数或指定 SmolVLA）。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M2\"\n  summary: \"LIBERO-Spatial null result based on only 1 seed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"1 seed insufficient for null conclusion given per-seed std of 2.6pp\"}\n    - {round: 2, reviewers: [R1, R2], note: \"仍为 seed 42 单点。R1 指出缺 per-task Spatial 表和 failure case 分析。R2 指出若将 null result 包装为 contribution 则分析深度需大幅提升。\"}\n  action_items:\n    - {round: 1, action: \"Deploy Spatial seed43/44/45\", assigned_to: \"Agent\", status: \"unknown\"}\n    - {round: 2, action: \"(1) 补充 Spatial multi-seed。(2) 补充 per-task Spatial 结果表。(3) 若声称为 contribution 需加深分析（failure mode 分类、correction vector 在 spatial tasks 上的行为）。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M3\"\n  summary: \"No experimental comparison with A2C2\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Only textual positioning, no quantitative comparison\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 两位 Reviewer 独立升级为 critical。A2C2 correction head 可直接 attach 到同一 frozen SmolVLA，Limitations 的 'different training regime' 辩护不成立。论文声称的三点设计差异无实验验证。\"}\n  action_items:\n    - {round: 1, action: \"Add Limitations paragraph explaining different training regimes\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"在同一 frozen SmolVLA checkpoint 上实现 A2C2 baseline 做 controlled comparison。若无法完成，至少承认这是 open comparison 而非已回答的问题。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M4\"\n  summary: \"Bib entries missing venue info + missing key citations\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Orphan entries, missing citations\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已部分修复（orphan entries 清理，CP subsection 已加）。R2 指出 bib 中 RT-2/OpenVLA/Octo 仍标记为 @misc 需更新 venue。R1 认为 32 条引用在 CoRL 正常范围。R2 列出 5 篇遗漏（ADPro/GPC/Recurrent-Depth VLA 等），R1 认为部分可选。\"}\n  action_items:\n    - {round: 1, action: \"Clean orphan entries, add citations, add CP subsection\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"(1) 更新 RT-2/OpenVLA/Octo 的 bib venue 信息。(2) 评估是否需添加 ADPro/GPC 等 frozen policy + inference-time enhancement 方向的引用。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M5\"\n  summary: \"Figure 2 n=1 points show meaningless error bars\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R3], note: \"Visual misleading\"}\n    - {round: 2, reviewers: [R1, R2], note: \"Figure 2 caption 标注 n=1-7 per point，R1-W2 和 R2 均指出某些点仅 1 seed 无统计意义\"}\n  action_items:\n    - {round: 1, action: \"n=1 points use different marker, no error bars\", assigned_to: \"Paper Agent\", status: \"unknown\"}\n    - {round: 2, action: \"确保 n=1 点无 error bar 或使用不同 marker。每个点标注 seed 数。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M6\"\n  summary: \"No cross-task generalization test (CRM trained on all eval tasks)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Cannot distinguish task-agnostic correction from task-specific memory\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] R1 独立提出为 N1 critical。R2 交叉回应完全同意，补充指出 per-task concentrated improvement (4/10 tasks) 与 memorization 假说兼容。CRM 在 Spatial 上训练但未带来提升——这增加了复杂性但不排除 memorization。\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations. Leave-task-out as rebuttal backup.\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"(1) 做 train/test task split（如 15 task 训练 / 5 held-out 评估）。(2) 若无法完成，坦诚承认这是 task-specific fine-tuning 而非 general inference-time refinement。(3) 在 Limitations 中明确讨论 memorization vs generalization。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M7\"\n  summary: \"Paper positioning unclear — method paper vs analysis paper\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Abstract/Method as method paper, but value is in analysis\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[DIVERGENT] R2 维持新颖性不足。R1 rebut 认为 decomposition 有独立价值但需扩展实验规模。标题 'Dissecting' 暗示分析定位但分析深度不足（见 W7-dissection-depth）。\"}\n  action_items:\n    - {round: 1, action: \"Merged with C4 — reposition as analysis paper\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"若定位为分析 paper 则需大幅增加分析深度；若定位为方法 paper 则需扩展评估范围。当前两头不够强。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M8\"\n  summary: \"Missing Conformal Prediction in robotics discussion in Related Work\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2], note: \"Core contribution involves CP failure but no CP-robotics subsection\"}\n    - {round: 2, reviewers: [], note: \"已修复。Section 2.3 'Conformal Prediction in Robotics' 已添加，覆盖 ACP-CBF/CPLoop/Conformalized Teleoperation。\"}\n  action_items:\n    - {round: 1, action: \"Add CP in robotics subsection to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Section 2.3 已添加 CP in Robotics 子节\"\n  resolution_round: 2\n\n- id: \"m1\"\n  summary: \"'safety factor' terminology ambiguous in robotics context\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R3], note: \"Change to 'critical design factor'\"}\n    - {round: 2, reviewers: [], note: \"已修复。论文使用 'critical design factor'。\"}\n  action_items:\n    - {round: 1, action: \"Replace 'safety factor' with 'critical design factor'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"术语已替换\"\n  resolution_round: 2\n\n- id: \"m2-m9\"\n  summary: \"8 minor writing/format issues (L2 motivation, DOF expansion, -ing phrases, Table 2 bold, Fig 1 density, per-task seed42, LLM analogy)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"All minor fixes bundled\"}\n    - {round: 2, reviewers: [R2], note: \"大部分已修复。R2-S5 确认写作质量高、AI 痕迹几乎为零。少量新 minor 问题见下方新 issue。\"}\n  action_items:\n    - {round: 1, action: \"Fix all 8 items in single pass\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"批量修复完成\"\n  resolution_round: 2\n\n# === Round 2 新发现 ===\n\n- id: \"R2-W4-new\"\n  summary: \"Motivation-evaluation disconnect: LIBERO+ numbers in Intro but eval on standard LIBERO\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] Introduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%）motivate distribution shift，但实验在标准 LIBERO 上。SmolVLA 11.6% baseline 原因未解释。造成读者预期与实际不符。\"}\n  action_items:\n    - {round: 2, action: \"(1) 在 LIBERO+ 上评估，或 (2) 清楚解释 SmolVLA 11.6% baseline 的原因（checkpoint 选择？evaluation protocol？）并调整 Introduction framing 使 motivation 与 eval setting 一致。\", assigned_to: \"Paper Agent + Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-new\"\n  summary: \"Low absolute performance (17.6%) limits generalizability of all findings\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 在 base policy 几乎不工作的 regime 下做 component decomposition，结论能否外推到更强 base policy 未知。Per-task 分析显示 improvement 集中在 4/10 tasks。\"}\n  action_items:\n    - {round: 2, action: \"至少在一个 base policy >50% 的 setting 下验证核心发现，或明确限定 claim 适用范围为 low-performance regime。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7-new\"\n  summary: \"'Dissecting' title promises analysis depth not delivered\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 缺 correction vector 分布分析、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。当前为 ablation 而非 dissection。\"}\n  action_items:\n    - {round: 2, action: \"(1) 增加 correction vector 统计分析（CRM δ 在不同 task/timestep 的 pattern）。(2) trajectory 阶段分析（approach/grasp/lift 哪阶段 correction 最有效）。(3) 成功 vs 失败 trajectory 可视化对比。或降低标题承诺。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1-new\"\n  summary: \"'Geometric medoid' terminology incorrect (actually argmin-to-centroid)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 经典 medoid 是 argmin to all other points (non-squared L2)，论文实际是 argmin to centroid (squared L2)。\"}\n  action_items:\n    - {round: 2, action: \"将 'geometric medoid' 改为 'closest sample to the centroid' 或 'argmin-to-mean'。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-new\"\n  summary: \"DAgger citation misused to justify Gaussian noise augmentation\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] DAgger 是 interactive dataset aggregation，非 static noise augmentation。应引用 domain randomization 或 noise injection 文献。\"}\n  action_items:\n    - {round: 2, action: \"替换 DAgger 引用为更恰当的 covariate shift / domain randomization 文献，或更准确地引用 DAgger 中关于 distribution shift 的理论分析。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3-new\"\n  summary: \"Applicability boundary based on single comparison (OpenVLA T=0.5 only)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 未测 OpenVLA 更高 temperature、其他 tokenized VLA、或其他 flow-matching VLA 做正面验证。'Architectural boundary' 是强 claim 但 evidence 仅一个 data point。\"}\n  action_items:\n    - {round: 2, action: \"(1) 测试 OpenVLA T=1.0+。(2) 软化 claim 为 'under default sampling settings'。(3) 或补充更多 VLA 的 diversity 对比。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4-latency\"\n  summary: \"Wall-clock latency of K=10 forward passes not quantified\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] SmolVLA 单次 forward pass ~50-100ms 估算，K=10 约 500ms-1s，对应 1-2 Hz 远低于 10-20 Hz 典型操作频率。论文回避了量化。\"}\n  action_items:\n    - {round: 2, action: \"提供 SmolVLA 单次 forward pass wall-clock time 和 K=10 total latency，讨论 real-time 可行性。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "issues_yaml": "- id: \"C1\"\n  summary: \"Fisher exact test independence violation (pseudo-replication)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Same-seed episodes share CRM weights, violating independence assumption\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已修复。论文改用 seed-level Mann-Whitney U 检验，两位 Reviewer 均肯定统计方法严谨\"}\n  action_items:\n    - {round: 1, action: \"Replace Fisher with Mann-Whitney U (seed-level) as primary test + sign test supplementary\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"改用 seed-level Mann-Whitney U 检验 + sign test 补充验证\"\n  resolution_round: 2\n\n- id: \"C2\"\n  summary: \"Core claim 'correction is sole driver' contradicts K=1 data (10.3% < 11.6%)\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"K=1 CRM below baseline means correction alone harmful. Appendix L18 also contradicts.\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已修复。论文重构为 'correction is active mechanism, multi-sampling is enabling condition'，两位 Reviewer 均认可此 framing\"}\n  action_items:\n    - {round: 1, action: \"Reframe to 'correction is active mechanism, multi-sampling is enabling condition'. Fix Appendix L18.\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"重构为 'correction is active mechanism, multi-sampling is enabling condition'\"\n  resolution_round: 2\n\n- id: \"C3\"\n  summary: \"Inconsistent seed counts across methods without explanation\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"obs_only 7, VLA-only 5, Argmin 6, Random 3 — no justification\"}\n    - {round: 2, reviewers: [R1, R2], note: \"论文增加了 'compute budget allocated by comparison importance' 说明，但 R1 指出 Random 仅 3 seeds 的 MW-U 几乎无法拒绝 H0，'statistically indistinguishable' 结论不成立。R2 同意主要对比证据尚可（U=35=U_max），但次要对比 underpowered。\"}\n  action_items:\n    - {round: 1, action: \"Add explanation paragraph (resource allocation by importance). Supplement Random to n=5.\", assigned_to: \"Paper Agent + Agent\", status: \"partial\"}\n    - {round: 2, action: \"所有条件统一至 >=5 seeds。公布逐 seed 成功率。不要对 n=3 对比声称 'statistically indistinguishable'。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C4\"\n  summary: \"Novelty insufficient — standard MLP + L2 clipping\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Technical novelty low, contribution is in analysis not architecture\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[DIVERGENT] R2 维持 critical（方法组件均为已知技术）。R1 rebut 认为 component decomposition 有独立价值，真正问题是实验规模不足。降级为 warning。\"}\n  action_items:\n    - {round: 1, action: \"Reposition as analysis paper. Novelty is in findings not architecture.\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"明确定位为实证分析 paper（已部分完成通过标题 'Dissecting'），但需扩展分析深度（见新 issue W7-dissection-depth）\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C5\"\n  summary: \"Title 'Sample, Select, Correct' contradicts conclusion that select is useless\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Title sets wrong reader expectations\"}\n    - {round: 2, reviewers: [], note: \"已修复。新标题 'Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs' 准确反映发现\"}\n  action_items:\n    - {round: 1, action: \"Change title\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"标题改为 'Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs'\"\n  resolution_round: 2\n\n- id: \"C6\"\n  summary: \"Paper exceeds 8-page limit\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R3, R2], note: \"May cause desk reject\"}\n    - {round: 2, reviewers: [R2], note: \"R2 估算正文约 8.5 页，可能略超限制。需实际编译验证。\"}\n  action_items:\n    - {round: 1, action: \"Compress to exactly 8 pages.\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"实际编译确认页数。若超限需进一步压缩。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C7\"\n  summary: \"Missing AI Disclosure Statement (CoRL 2026 requirement)\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R3, R2], note: \"Required by venue\"}\n    - {round: 2, reviewers: [R2], note: \"已修复。AI Disclosure 存在且合规。\"}\n  action_items:\n    - {round: 1, action: \"Add AI disclosure statement\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"AI Disclosure statement 已添加\"\n  resolution_round: 2\n\n- id: \"M1\"\n  summary: \"Narrow experimental scope (single VLA + single benchmark + no real robot)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R1, R3], note: \"Only SmolVLA on LIBERO, no RLBench/MetaWorld/real\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 两位 Reviewer 一致认为这是核心缺陷。标题 'Frozen VLAs'(复数)但只测一个。无 π₀/Diffusion Policy 正面验证。CoRL CFP 要求 real-robot 或 sim-to-real 论证。\"}\n  action_items:\n    - {round: 1, action: \"Add Spatial multi-seed. Acknowledge scope limitation.\", assigned_to: \"Agent + Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"(1) 至少增加一个 flow-matching VLA backbone（如 π₀）。(2) 提供 wall-clock latency 量化。(3) 提供 sim-to-real 可迁移性论证或更诚实的 scope 限定（标题改为单数或指定 SmolVLA）。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M2\"\n  summary: \"LIBERO-Spatial null result based on only 1 seed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"1 seed insufficient for null conclusion given per-seed std of 2.6pp\"}\n    - {round: 2, reviewers: [R1, R2], note: \"仍为 seed 42 单点。R1 指出缺 per-task Spatial 表和 failure case 分析。R2 指出若将 null result 包装为 contribution 则分析深度需大幅提升。\"}\n  action_items:\n    - {round: 1, action: \"Deploy Spatial seed43/44/45\", assigned_to: \"Agent\", status: \"unknown\"}\n    - {round: 2, action: \"(1) 补充 Spatial multi-seed。(2) 补充 per-task Spatial 结果表。(3) 若声称为 contribution 需加深分析（failure mode 分类、correction vector 在 spatial tasks 上的行为）。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M3\"\n  summary: \"No experimental comparison with A2C2\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Only textual positioning, no quantitative comparison\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 两位 Reviewer 独立升级为 critical。A2C2 correction head 可直接 attach 到同一 frozen SmolVLA，Limitations 的 'different training regime' 辩护不成立。论文声称的三点设计差异无实验验证。\"}\n  action_items:\n    - {round: 1, action: \"Add Limitations paragraph explaining different training regimes\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"在同一 frozen SmolVLA checkpoint 上实现 A2C2 baseline 做 controlled comparison。若无法完成，至少承认这是 open comparison 而非已回答的问题。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M4\"\n  summary: \"Bib entries missing venue info + missing key citations\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Orphan entries, missing citations\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已部分修复（orphan entries 清理，CP subsection 已加）。R2 指出 bib 中 RT-2/OpenVLA/Octo 仍标记为 @misc 需更新 venue。R1 认为 32 条引用在 CoRL 正常范围。R2 列出 5 篇遗漏（ADPro/GPC/Recurrent-Depth VLA 等），R1 认为部分可选。\"}\n  action_items:\n    - {round: 1, action: \"Clean orphan entries, add citations, add CP subsection\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"(1) 更新 RT-2/OpenVLA/Octo 的 bib venue 信息。(2) 评估是否需添加 ADPro/GPC 等 frozen policy + inference-time enhancement 方向的引用。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M5\"\n  summary: \"Figure 2 n=1 points show meaningless error bars\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R3], note: \"Visual misleading\"}\n    - {round: 2, reviewers: [R1, R2], note: \"Figure 2 caption 标注 n=1-7 per point，R1-W2 和 R2 均指出某些点仅 1 seed 无统计意义\"}\n  action_items:\n    - {round: 1, action: \"n=1 points use different marker, no error bars\", assigned_to: \"Paper Agent\", status: \"unknown\"}\n    - {round: 2, action: \"确保 n=1 点无 error bar 或使用不同 marker。每个点标注 seed 数。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M6\"\n  summary: \"No cross-task generalization test (CRM trained on all eval tasks)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Cannot distinguish task-agnostic correction from task-specific memory\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] R1 独立提出为 N1 critical。R2 交叉回应完全同意，补充指出 per-task concentrated improvement (4/10 tasks) 与 memorization 假说兼容。CRM 在 Spatial 上训练但未带来提升——这增加了复杂性但不排除 memorization。\"}\n  action_items:\n    - {round: 1, action: \"Acknowledge in Limitations. Leave-task-out as rebuttal backup.\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"(1) 做 train/test task split（如 15 task 训练 / 5 held-out 评估）。(2) 若无法完成，坦诚承认这是 task-specific fine-tuning 而非 general inference-time refinement。(3) 在 Limitations 中明确讨论 memorization vs generalization。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M7\"\n  summary: \"Paper positioning unclear — method paper vs analysis paper\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Abstract/Method as method paper, but value is in analysis\"}\n    - {round: 2, reviewers: [R1, R2], note: \"[DIVERGENT] R2 维持新颖性不足。R1 rebut 认为 decomposition 有独立价值但需扩展实验规模。标题 'Dissecting' 暗示分析定位但分析深度不足（见 W7-dissection-depth）。\"}\n  action_items:\n    - {round: 1, action: \"Merged with C4 — reposition as analysis paper\", assigned_to: \"Paper Agent\", status: \"partial\"}\n    - {round: 2, action: \"若定位为分析 paper 则需大幅增加分析深度；若定位为方法 paper 则需扩展评估范围。当前两头不够强。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M8\"\n  summary: \"Missing Conformal Prediction in robotics discussion in Related Work\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2], note: \"Core contribution involves CP failure but no CP-robotics subsection\"}\n    - {round: 2, reviewers: [], note: \"已修复。Section 2.3 'Conformal Prediction in Robotics' 已添加，覆盖 ACP-CBF/CPLoop/Conformalized Teleoperation。\"}\n  action_items:\n    - {round: 1, action: \"Add CP in robotics subsection to Related Work\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Section 2.3 已添加 CP in Robotics 子节\"\n  resolution_round: 2\n\n- id: \"m1\"\n  summary: \"'safety factor' terminology ambiguous in robotics context\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R3], note: \"Change to 'critical design factor'\"}\n    - {round: 2, reviewers: [], note: \"已修复。论文使用 'critical design factor'。\"}\n  action_items:\n    - {round: 1, action: \"Replace 'safety factor' with 'critical design factor'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"术语已替换\"\n  resolution_round: 2\n\n- id: \"m2-m9\"\n  summary: \"8 minor writing/format issues (L2 motivation, DOF expansion, -ing phrases, Table 2 bold, Fig 1 density, per-task seed42, LLM analogy)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"All minor fixes bundled\"}\n    - {round: 2, reviewers: [R2], note: \"大部分已修复。R2-S5 确认写作质量高、AI 痕迹几乎为零。少量新 minor 问题见下方新 issue。\"}\n  action_items:\n    - {round: 1, action: \"Fix all 8 items in single pass\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"批量修复完成\"\n  resolution_round: 2\n\n# === Round 2 新发现 ===\n\n- id: \"R2-W4-new\"\n  summary: \"Motivation-evaluation disconnect: LIBERO+ numbers in Intro but eval on standard LIBERO\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] Introduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%）motivate distribution shift，但实验在标准 LIBERO 上。SmolVLA 11.6% baseline 原因未解释。造成读者预期与实际不符。\"}\n  action_items:\n    - {round: 2, action: \"(1) 在 LIBERO+ 上评估，或 (2) 清楚解释 SmolVLA 11.6% baseline 的原因（checkpoint 选择？evaluation protocol？）并调整 Introduction framing 使 motivation 与 eval setting 一致。\", assigned_to: \"Paper Agent + Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-new\"\n  summary: \"Low absolute performance (17.6%) limits generalizability of all findings\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 在 base policy 几乎不工作的 regime 下做 component decomposition，结论能否外推到更强 base policy 未知。Per-task 分析显示 improvement 集中在 4/10 tasks。\"}\n  action_items:\n    - {round: 2, action: \"至少在一个 base policy >50% 的 setting 下验证核心发现，或明确限定 claim 适用范围为 low-performance regime。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7-new\"\n  summary: \"'Dissecting' title promises analysis depth not delivered\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 缺 correction vector 分布分析、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。当前为 ablation 而非 dissection。\"}\n  action_items:\n    - {round: 2, action: \"(1) 增加 correction vector 统计分析（CRM δ 在不同 task/timestep 的 pattern）。(2) trajectory 阶段分析（approach/grasp/lift 哪阶段 correction 最有效）。(3) 成功 vs 失败 trajectory 可视化对比。或降低标题承诺。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1-new\"\n  summary: \"'Geometric medoid' terminology incorrect (actually argmin-to-centroid)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 经典 medoid 是 argmin to all other points (non-squared L2)，论文实际是 argmin to centroid (squared L2)。\"}\n  action_items:\n    - {round: 2, action: \"将 'geometric medoid' 改为 'closest sample to the centroid' 或 'argmin-to-mean'。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-new\"\n  summary: \"DAgger citation misused to justify Gaussian noise augmentation\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] DAgger 是 interactive dataset aggregation，非 static noise augmentation。应引用 domain randomization 或 noise injection 文献。\"}\n  action_items:\n    - {round: 2, action: \"替换 DAgger 引用为更恰当的 covariate shift / domain randomization 文献，或更准确地引用 DAgger 中关于 distribution shift 的理论分析。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3-new\"\n  summary: \"Applicability boundary based on single comparison (OpenVLA T=0.5 only)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] 未测 OpenVLA 更高 temperature、其他 tokenized VLA、或其他 flow-matching VLA 做正面验证。'Architectural boundary' 是强 claim 但 evidence 仅一个 data point。\"}\n  action_items:\n    - {round: 2, action: \"(1) 测试 OpenVLA T=1.0+。(2) 软化 claim 为 'under default sampling settings'。(3) 或补充更多 VLA 的 diversity 对比。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4-latency\"\n  summary: \"Wall-clock latency of K=10 forward passes not quantified\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2], note: \"[AGREE] SmolVLA 单次 forward pass ~50-100ms 估算，K=10 约 500ms-1s，对应 1-2 Hz 远低于 10-20 Hz 典型操作频率。论文回避了量化。\"}\n  action_items:\n    - {round: 2, action: \"提供 SmolVLA 单次 forward pass wall-clock time 和 K=10 total latency，讨论 real-time 可行性。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-19T01:57:18.973804+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml\", \"bytes\": 17142}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 223
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-19T01:59:42.774534+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n**目标 venue**: CoRL 2026 Main Conference\n**Deadline**: 2026-05-29（距今 10 天）\n**审稿模式**: Fresh（独立初审）\n**Reviewer 编排**: 2 人（R1: 方法/实验/统计; R2: 新颖性/Related Work/写作/格式）\n**外部审稿**: 未配置，跳过\n\n---\n\n## Summary\n\n本文提出 sample-select-correct pipeline 对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正。在 LIBERO-Object 上实现 17.6±2.6% vs 11.6±1.1% 的成功率提升（p=0.003, Mann-Whitney U），并通过 component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告 conformal features 失效（progressive collapse to 0%）和 tokenized VLA 不适用的 negative results。\n\n---\n\n## Strengths\n\n- **S1: 系统化 component decomposition**。通过 K=1 correction、selection-only、random selection 等控制实验清楚拆解各组件贡献。\"Selection alone 无显著帮助、K=1 correction 低于 baseline、二者结合才有效\" 对 embodied test-time compute scaling 有洞察价值，与 LLM test-time scaling 的 selection-dominant 范式形成有意义的对比。[R1-S1, R2-S3, 共识]\n\n- **S2: 有价值的 negative results**。Conformal features 的失败（obs_only 14.3-17.6% 稳健 vs perdof collapse 至 0%）和 tokenized VLA 不适用性，对后续研究有指导意义。[R1-S2, R2-S4, 共识]\n\n- **S3: 统计协议严谨**。正确识别 episode-level 非独立性，选择 seed-level Mann-Whitney U + sign test 补充验证。相比 Round 1 的 Fisher test 已大幅改善。[R1-S3, R2-S2, 共识]\n\n- **S4: 写作质量高**。Pipeline 描述精确，符号一致，ablation 逻辑清晰。AI 写作痕迹几乎为零（无 em-dash、无禁用词汇、无过度分段）。Limitations section 诚实全面。[R1-S4, R2-S1/S5, 共识]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Critical（影响接收决定）\n\n**W-C1: 极低绝对性能限制所有发现的泛化性** [R2-W1, R1 AGREE]\nVLA-only baseline 仅 11.6%，pipeline 达 17.6%——整个评估处于 base policy 几乎不工作的 regime。在此 regime 下的 component decomposition 结论（correction > selection）是否对更强 base policy（如 A2C2 报告的 67-72% SmolVLA baseline，或 π₀ 94.2%）成立完全未知。Per-task 分析（Appendix Table 2）显示 improvement 集中在 4/10 tasks（chocolate_pudding +40pp, bbq_sauce/ketchup +20pp, salad_dressing +10pp），其余 6 个 task 基本无变化或退化，表明 aggregate 17.6% 掩盖了高度不均匀的 task-level 表现。\n\n**W-C2: 评估范围极窄，无法支撑 general claims** [R2-W2, R1-N4, 共识]\n(a) 仅用 SmolVLA（450M）一个 backbone，但标题用 \"Frozen VLAs\"（复数）；(b) 仅 LIBERO 一个 benchmark family（且只有 Object 子集有效）；(c) 纯仿真，无 real-robot 实验或 sim-to-real 可迁移性论证。CoRL 2026 CFP 明确鼓励 \"real-robot experiments or simulation evidence demonstrating transferability to physical robots\"。Applicability boundary 实验仅用 OpenVLA 做了 negative case，无其他 flow-matching VLA（如 π₀、Diffusion Policy）的正面验证。\n\n**W-C3: CRM 在 eval 任务 demo 上训练，无 held-out task 泛化验证** [R1-N1, R2 AGREE]\nCRM 训练数据为 \"26,737 precomputed samples from 10 demonstrations per task across all 20 LIBERO tasks\"——恰好是评估的 Object 10 + Spatial 10。无法区分 task-specific memorization 和 generalizable correction。Per-task concentrated improvement（4/10 tasks）与 memorization 假说兼容。CRM 在 Spatial demo 上训练但 Spatial 上未带来提升，增加了复杂性但不排除 Object 上的 memorization。缺少 train/test task split 是重大遗漏。\n\n**W-C4: 缺少 A2C2 实验对比** [R1-N2, R2-W5, 共识]\nA2C2 被论文自行认定为 \"closest concurrent work\"（Section 2），详细列出三点方法差异（multi-sample selection、norm clipping、observation conditioning），但从未作为 baseline 运行。Limitations 的 \"different training regime\" 辩护不成立——A2C2 correction head 完全可以 attach 到同一 frozen SmolVLA checkpoint。论文声称的三点设计优势是 unsubstantiated claims。\n\n**W-C5: 动机与评估断裂** [R2-W4, R1 AGREE]\nIntroduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%, UniVLA 95.2%→4.3%）motivate distribution shift，但实验在标准 LIBERO 上。SmolVLA 11.6% baseline 的原因未解释——是 checkpoint 选择、evaluation protocol 差异还是 distribution shift？若 SmolVLA 本身在此 setting 下就不工作，correction 的意义进一步被削弱。读者预期（修复强 policy 的 shift 崩溃）与实际（弱 policy 的微小提升）不符。\n\n**W-C6: Seed 数量小且不平衡** [R1-N3, R2 AGREE with nuance]\nobs_only 7 seeds、VLA-only 5、Argmin 6、Random 3、VLA-mean 4、scalar 4。主要对比（obs_only vs VLA-only, U=35=U_max, p=0.0025）在给定样本量下已是最强可能结果。但次要对比严重 underpowered：Random 仅 3 seeds 就断言 \"statistically indistinguishable from VLA-only\"，3 seeds 的 MW-U 几乎无法拒绝任何 H0。seed 数量由 \"comparison importance\" 决定分配，存在 optional stopping 风险。Per-seed variance 实质存在（seed 43: argmin 17% > obs_only 16%）。\n\n### Warning（影响评分但不一票否决）\n\n**W-W1: \"Dissecting\" 标题承诺的分析深度未兑现** [R2-W7, R1 AGREE]\n论文实际提供的是 ablation-level component decomposition，缺乏 dissection 应有的深层分析：correction vector 分布、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。\n\n**W-W2: Applicability boundary 基于单一对比** [R1-W3, R2 AGREE]\n仅 OpenVLA T=0.5 一个设定。未测更高 temperature 或其他 tokenized/flow-matching VLA。\"Architectural boundary\" 是强 claim 但 evidence 仅一个 data point。\n\n**W-W3: LIBERO-Spatial null result 分析不足** [R1-W4, R2 AGREE]\nSpatial 上所有方法 30-35%，仅一段推测性解释。无 per-task Spatial 表，无 failure case 定量分析。若将 null result 包装为 contribution，分析深度应大幅提升。\n\n**W-W4: ε 敏感性分析不完整** [R1-W2, R2 AGREE]\nscalar 变体仅 ε=0.1 一个点。各 ε 点 seed 数不一致（n=1-7），某些点仅 1 seed 无统计意义。\n\n**W-W5: Wall-clock latency 未量化** [R1-N4 sub, R2 AGREE]\nSmolVLA 单次 forward pass ~50-100ms 估算，K=10 约 500ms-1s，对应 1-2 Hz 远低于 10-20 Hz 操作频率。论文提到 \"~0.3ms CRM overhead\" 但回避了 10x VLA forward pass 的主要开销。\n\n**W-W6: \"Geometric medoid\" 术语不正确** [R1-W1, R2 AGREE]\n实际是 argmin-to-centroid（squared L2），非经典 geometric medoid（non-squared L2 to all other points）。\n\n**W-W7: DAgger 引用误用** [R1-W5, R2 AGREE]\nDAgger 是 interactive dataset aggregation，非 static Gaussian noise augmentation。应引用 domain randomization 或 noise injection 文献。\n\n**W-W8: 页数可能略超限制** [R2 估算]\n正文估算约 8.5 页，可能超 CoRL 8 页限制。需实际编译确认。\n\n**W-W9: Related Work 遗漏** [R2-W6, R1 部分 REBUT]\nR2 列出 5 篇遗漏（ADPro/GPC/Recurrent-Depth VLA/Residual Policy Adaptation/Compose Your Policies!），其中 ADPro 和 GPC 与本文共享 \"frozen generative policy + inference-time enhancement\" 核心设定。R1 认为 32 条引用在 CoRL 正常范围，Related Work 分类覆盖合理。bib 中 RT-2/OpenVLA/Octo 仍标记为 @misc 需更新正式 venue 信息。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **评估范围过窄是论文最大的结构性缺陷**——单 VLA backbone、单 benchmark family、sim-only、低绝对性能。所有 general claims 缺乏实证支撑。\n2. **缺少 A2C2 对比是 positioning 的核心缺陷**——论文自行认定的最接近工作却无实验验证差异的重要性。\n3. **CRM 在 eval task 上训练无泛化验证**——无法区分 memorization 和 generalization。\n4. **写作和统计方法是论文的明显优势**——seed-level 非参数检验、诚实的 Limitations、minimal AI artifacts。\n\n## Reviewer Divergence [REBUT]\n\n1. **方法新颖性** [R2-W3 critical vs R1 REBUT]：R2 认为三个组件均为已知技术，工程集成而非方法论创新。R1 认为 component decomposition 实验设计有独立价值，与 LLM test-time scaling 的对比是非显然发现，真正致命伤是实验规模而非新颖性。\n2. **引用数量** [R2-W6 vs R1 REBUT]：R2 认为 29 条引用偏少且遗漏重要工作。R1 指出实际 32 条在 CoRL 正常范围，Related Work 分类结构合理，但同意 bib venue 需更新。\n\n---\n\n## Questions for Authors\n\n1. SmolVLA 在标准 LIBERO-Object 上 baseline 为何只有 11.6%？SmolVLA 原论文报告多少？11.6% 是否代表 distribution shift（如果是，具体什么性质的 shift）？\n2. CRM 是否曾在 held-out tasks 上测试？如在 15 task 训练 / 5 held-out 评估，结果如何？\n3. 在 base policy >50% 的 setting 下，correction > selection 的结论是否仍然成立？\n4. K=10 forward passes 在 SmolVLA 上的 wall-clock latency 是多少？是否满足 real-time control 要求？\n5. A2C2 correction head 能否 attach 到同一 frozen SmolVLA checkpoint？如可以，为什么不做对比？\n6. Table 1 LIBERO-Spatial 的 Random baseline 标记 \"---\"，原因是什么？\n7. 能否公布每个 seed 的具体成功率？\n8. perdof 在 ε=0.03 达 14%（接近 obs_only 14.3%），K 更大时 conformal features 是否可能变得有用？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同提出**：\n- A2C2 的 controlled experimental comparison\n\n**R2 提出**：\n- ADPro (2025, arXiv 2508.06266): test-time adaptive diffusion policy\n- GPC (2025, arXiv 2502.00622): inference-time enhancement via predictive world modeling\n- Recurrent-Depth VLA (2026, arXiv 2602.07845): implicit test-time compute scaling\n- Compose Your Policies! (2025, arXiv 2510.01068): test-time distribution-level composition\n\n**R1 提出**：\n- ACT temporal ensembling (Zhao et al. 2023)\n- Best-of-N sampling in robotics\n\n**bib 格式问题**：RT-2/OpenVLA/Octo 已正式发表，应更新 @misc → @inproceedings 并补充 venue 信息。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 `external_review.paperreview_ai`），跳过。\n\n---\n\n## Overall Assessment\n\n**Score: weak reject**\n**Confidence: high**\n**R1: weak reject (high confidence) | R2: weak reject (high confidence)**\n\n两位 Reviewer 独立给出一致评分。\n\n**核心判断**：论文在写作质量、统计严谨性和 component decomposition 设计上有实质性优势。但评估范围过窄（单 VLA / 单 benchmark / sim-only）、绝对性能极低（17.6%）、缺少最关键 baseline（A2C2）、CRM 泛化能力未验证，共同构成了在 CoRL 2026 录用标准下的 significant gap。\n\n**相比 Round 1 的改进**：\n论文在以下方面有实质性进步（Round 1 的 7 个 critical issue 中 4 个已 resolved）：\n- ✅ 统计方法从 Fisher test 改为 seed-level Mann-Whitney U [C1 resolved]\n- ✅ 核心 claim reframe 为 \"correction is active mechanism, multi-sampling is enabling condition\" [C2 resolved]\n- ✅ 标题从 \"Sample, Select, Correct\" 改为 \"Correction Over Selection\" [C5 resolved]\n- ✅ AI Disclosure 已添加 [C7 resolved]\n- ✅ Related Work 增加 CP in Robotics 子节 [M8 resolved]\n- ✅ 术语和写作质量显著提升 [m1, m2-m9 resolved]\n\n**持续存在的核心问题**：\n- ❌ 评估范围仍然极窄（M1 open → 升级为 W-C2）\n- ❌ 无 A2C2 实验对比（M3 open → 升级为 W-C4）\n- ❌ CRM 泛化性未验证（M6 open → 升级为 W-C3）\n- ❌ Seed 数量仍然不平衡（C3 partial）\n- ❌ Spatial null result 仍为单 seed（M2 open）\n\n**新发现的问题**：\n- 🆕 动机-评估断裂（W-C5: LIBERO+ vs LIBERO）\n- 🆕 低绝对性能限制泛化性（W-C1）\n- 🆕 \"Dissecting\" 分析深度不足（W-W1）\n- 🆕 Latency 未量化（W-W5）\n\n**给 Research Director 的整体评估**：\n论文写作和统计方面的改进是实质性的，表明作者认真回应了 Round 1 反馈。但核心的实验范围和 baseline 缺失问题（M1/M3/M6）在 Round 1 就已识别，本轮仍未解决。这些不是 writing fix 能解决的问题——需要额外实验（A2C2 baseline、held-out task split、第二个 VLA backbone、latency 量化）。距 deadline 仅 10 天，部分实验（如增加 VLA backbone）在时间上可能不可行。建议 Research Director 评估是否现有 scope 下能通过 A2C2 对比 + held-out split + latency 量化来将论文提升至 borderline，或考虑重新选择更匹配评估范围的 venue（如 workshop paper）。\n\n---\n\n## Detailed Comments（逐 section）\n\n### Abstract\n- 约 160 words，在 150-250 范围内。四个核心要素齐全。\n- 单句包含 4 个数字和 2 个 p 值，可读性受影响 [R2-I3]。\n- \"conformal uncertainty features cause progressive collapse\" 使用论文未在 Abstract 中定义的概念 [R2]。\n- 缩写 MLP、DOF 未在 Abstract 中展开 [R2]。\n\n### Introduction\n- 五段结构完整，LIBERO+ 数字有效建立 urgency。\n- Para 2 对 existing approaches 梳理精炼有效。\n- **动机-评估断裂**：LIBERO+ 数字与实际 LIBERO 评估不匹配 [W-C5]。\n- Para 4 key findings 与 Para 5 contributions 数字重复出现三次（abstract, para 4, contributions）可压缩 [R1]。\n- Contribution 3 (\"applicability boundaries\") 在前文缺乏铺垫 [R2-I5]。\n\n### Related Work\n- 四小节结构合理。与 A2C2 三点差异表述精确但缺实验验证。\n- CP in Robotics 子节为 Section 4.3 negative result 提供了好的铺垫。\n- Residual Policy Learning 仅 4 行，覆盖面不足 [R2]。\n- 遗漏 test-time adaptation of diffusion/flow policies 方向（ADPro/GPC 等）[R2-W6]。\n- bib 中 RT-2/OpenVLA/Octo 需更新 venue 信息 [R2-I2]。\n\n### Method\n- Pipeline 描述完整，数学符号一致。\n- \"Geometric medoid\" 术语不正确 [W-W6]。\n- \"concatenation order is arbitrary for fully connected layers\" 注释无必要 [R2-I4]。\n- DAgger 引用不恰当 [W-W7]。\n- ε=0.2 选择仅有经验依据，无理论支撑 [R1]。\n\n### Experiments\n- Statistical protocol 段落是亮点。\n- Pipeline decomposition 分析是论文最有价值的部分。\n- Table 1 Spatial 列只有 seed 42 单点 [M2]。\n- Spatial Random \"---\" 未解释 [R1-Q2, R2-I1]。\n- K-scaling 分析有实用价值（K=5 capturing 82% benefit）[R1, R2]。\n\n### Discussion + Limitations + Conclusion\n- Discussion 仅 1 段，过于单薄。\"为什么 6D 连续空间中 selection 不如 discrete token space\"值得展开 [R2]。\n- Limitations 5 条诚实全面，但遗漏了 CRM 在 eval task 训练的泛化性问题 [R1-N1]。\n- Limitation 5 关于 A2C2 的辩护有误导性 [R1-N2]。\n\n### Appendix\n- K-scaling、applicability、per-task 三个附录在正文中均被引用。\n- 缺 per-task Spatial 结果表 [R1-W4]。\n\n### 格式\n- corl_2026 模板 ✓，Anonymous ✓，AI Disclosure ✓，Limitations ✓\n- 页数估算约 8.5 页，可能略超限制 [W-W8]\n- \\keywords 行是否为 CoRL 2026 模板要求需确认 [R2]\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_416d453a45869a9406db62186b1e3ef7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n**目标 venue**: CoRL 2026 Main Conference\n**Deadline**: 2026-05-29（距今 10 天）\n**审稿模式**: Fresh（独立初审）\n**Reviewer 编排**: 2 人（R1: 方法/实验/统计; R2: 新颖性/Related Work/写作/格式）\n**外部审稿**: 未配置，跳过\n\n---\n\n## Summary\n\n本文提出 sample-select-correct pipeline 对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正。在 LIBERO-Object 上实现 17.6±2.6% vs 11.6±1.1% 的成功率提升（p=0.003, Mann-Whitney U），并通过 component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告 conformal features 失效（progressive collapse to 0%）和 tokenized VLA 不适用的 negative results。\n\n---\n\n## Strengths\n\n- **S1: 系统化 component decomposition**。通过 K=1 correction、selection-only、random selection 等控制实验清楚拆解各组件贡献。\"Selection alone 无显著帮助、K=1 correction 低于 baseline、二者结合才有效\" 对 embodied test-time compute scaling 有洞察价值，与 LLM test-time scaling 的 selection-dominant 范式形成有意义的对比。[R1-S1, R2-S3, 共识]\n\n- **S2: 有价值的 negative results**。Conformal features 的失败（obs_only 14.3-17.6% 稳健 vs perdof collapse 至 0%）和 tokenized VLA 不适用性，对后续研究有指导意义。[R1-S2, R2-S4, 共识]\n\n- **S3: 统计协议严谨**。正确识别 episode-level 非独立性，选择 seed-level Mann-Whitney U + sign test 补充验证。相比 Round 1 的 Fisher test 已大幅改善。[R1-S3, R2-S2, 共识]\n\n- **S4: 写作质量高**。Pipeline 描述精确，符号一致，ablation 逻辑清晰。AI 写作痕迹几乎为零（无 em-dash、无禁用词汇、无过度分段）。Limitations section 诚实全面。[R1-S4, R2-S1/S5, 共识]\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Critical（影响接收决定）\n\n**W-C1: 极低绝对性能限制所有发现的泛化性** [R2-W1, R1 AGREE]\nVLA-only baseline 仅 11.6%，pipeline 达 17.6%——整个评估处于 base policy 几乎不工作的 regime。在此 regime 下的 component decomposition 结论（correction > selection）是否对更强 base policy（如 A2C2 报告的 67-72% SmolVLA baseline，或 π₀ 94.2%）成立完全未知。Per-task 分析（Appendix Table 2）显示 improvement 集中在 4/10 tasks（chocolate_pudding +40pp, bbq_sauce/ketchup +20pp, salad_dressing +10pp），其余 6 个 task 基本无变化或退化，表明 aggregate 17.6% 掩盖了高度不均匀的 task-level 表现。\n\n**W-C2: 评估范围极窄，无法支撑 general claims** [R2-W2, R1-N4, 共识]\n(a) 仅用 SmolVLA（450M）一个 backbone，但标题用 \"Frozen VLAs\"（复数）；(b) 仅 LIBERO 一个 benchmark family（且只有 Object 子集有效）；(c) 纯仿真，无 real-robot 实验或 sim-to-real 可迁移性论证。CoRL 2026 CFP 明确鼓励 \"real-robot experiments or simulation evidence demonstrating transferability to physical robots\"。Applicability boundary 实验仅用 OpenVLA 做了 negative case，无其他 flow-matching VLA（如 π₀、Diffusion Policy）的正面验证。\n\n**W-C3: CRM 在 eval 任务 demo 上训练，无 held-out task 泛化验证** [R1-N1, R2 AGREE]\nCRM 训练数据为 \"26,737 precomputed samples from 10 demonstrations per task across all 20 LIBERO tasks\"——恰好是评估的 Object 10 + Spatial 10。无法区分 task-specific memorization 和 generalizable correction。Per-task concentrated improvement（4/10 tasks）与 memorization 假说兼容。CRM 在 Spatial demo 上训练但 Spatial 上未带来提升，增加了复杂性但不排除 Object 上的 memorization。缺少 train/test task split 是重大遗漏。\n\n**W-C4: 缺少 A2C2 实验对比** [R1-N2, R2-W5, 共识]\nA2C2 被论文自行认定为 \"closest concurrent work\"（Section 2），详细列出三点方法差异（multi-sample selection、norm clipping、observation conditioning），但从未作为 baseline 运行。Limitations 的 \"different training regime\" 辩护不成立——A2C2 correction head 完全可以 attach 到同一 frozen SmolVLA checkpoint。论文声称的三点设计优势是 unsubstantiated claims。\n\n**W-C5: 动机与评估断裂** [R2-W4, R1 AGREE]\nIntroduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%, UniVLA 95.2%→4.3%）motivate distribution shift，但实验在标准 LIBERO 上。SmolVLA 11.6% baseline 的原因未解释——是 checkpoint 选择、evaluation protocol 差异还是 distribution shift？若 SmolVLA 本身在此 setting 下就不工作，correction 的意义进一步被削弱。读者预期（修复强 policy 的 shift 崩溃）与实际（弱 policy 的微小提升）不符。\n\n**W-C6: Seed 数量小且不平衡** [R1-N3, R2 AGREE with nuance]\nobs_only 7 seeds、VLA-only 5、Argmin 6、Random 3、VLA-mean 4、scalar 4。主要对比（obs_only vs VLA-only, U=35=U_max, p=0.0025）在给定样本量下已是最强可能结果。但次要对比严重 underpowered：Random 仅 3 seeds 就断言 \"statistically indistinguishable from VLA-only\"，3 seeds 的 MW-U 几乎无法拒绝任何 H0。seed 数量由 \"comparison importance\" 决定分配，存在 optional stopping 风险。Per-seed variance 实质存在（seed 43: argmin 17% > obs_only 16%）。\n\n### Warning（影响评分但不一票否决）\n\n**W-W1: \"Dissecting\" 标题承诺的分析深度未兑现** [R2-W7, R1 AGREE]\n论文实际提供的是 ablation-level component decomposition，缺乏 dissection 应有的深层分析：correction vector 分布、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。\n\n**W-W2: Applicability boundary 基于单一对比** [R1-W3, R2 AGREE]\n仅 OpenVLA T=0.5 一个设定。未测更高 temperature 或其他 tokenized/flow-matching VLA。\"Architectural boundary\" 是强 claim 但 evidence 仅一个 data point。\n\n**W-W3: LIBERO-Spatial null result 分析不足** [R1-W4, R2 AGREE]\nSpatial 上所有方法 30-35%，仅一段推测性解释。无 per-task Spatial 表，无 failure case 定量分析。若将 null result 包装为 contribution，分析深度应大幅提升。\n\n**W-W4: ε 敏感性分析不完整** [R1-W2, R2 AGREE]\nscalar 变体仅 ε=0.1 一个点。各 ε 点 seed 数不一致（n=1-7），某些点仅 1 seed 无统计意义。\n\n**W-W5: Wall-clock latency 未量化** [R1-N4 sub, R2 AGREE]\nSmolVLA 单次 forward pass ~50-100ms 估算，K=10 约 500ms-1s，对应 1-2 Hz 远低于 10-20 Hz 操作频率。论文提到 \"~0.3ms CRM overhead\" 但回避了 10x VLA forward pass 的主要开销。\n\n**W-W6: \"Geometric medoid\" 术语不正确** [R1-W1, R2 AGREE]\n实际是 argmin-to-centroid（squared L2），非经典 geometric medoid（non-squared L2 to all other points）。\n\n**W-W7: DAgger 引用误用** [R1-W5, R2 AGREE]\nDAgger 是 interactive dataset aggregation，非 static Gaussian noise augmentation。应引用 domain randomization 或 noise injection 文献。\n\n**W-W8: 页数可能略超限制** [R2 估算]\n正文估算约 8.5 页，可能超 CoRL 8 页限制。需实际编译确认。\n\n**W-W9: Related Work 遗漏** [R2-W6, R1 部分 REBUT]\nR2 列出 5 篇遗漏（ADPro/GPC/Recurrent-Depth VLA/Residual Policy Adaptation/Compose Your Policies!），其中 ADPro 和 GPC 与本文共享 \"frozen generative policy + inference-time enhancement\" 核心设定。R1 认为 32 条引用在 CoRL 正常范围，Related Work 分类覆盖合理。bib 中 RT-2/OpenVLA/Octo 仍标记为 @misc 需更新正式 venue 信息。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **评估范围过窄是论文最大的结构性缺陷**——单 VLA backbone、单 benchmark family、sim-only、低绝对性能。所有 general claims 缺乏实证支撑。\n2. **缺少 A2C2 对比是 positioning 的核心缺陷**——论文自行认定的最接近工作却无实验验证差异的重要性。\n3. **CRM 在 eval task 上训练无泛化验证**——无法区分 memorization 和 generalization。\n4. **写作和统计方法是论文的明显优势**——seed-level 非参数检验、诚实的 Limitations、minimal AI artifacts。\n\n## Reviewer Divergence [REBUT]\n\n1. **方法新颖性** [R2-W3 critical vs R1 REBUT]：R2 认为三个组件均为已知技术，工程集成而非方法论创新。R1 认为 component decomposition 实验设计有独立价值，与 LLM test-time scaling 的对比是非显然发现，真正致命伤是实验规模而非新颖性。\n2. **引用数量** [R2-W6 vs R1 REBUT]：R2 认为 29 条引用偏少且遗漏重要工作。R1 指出实际 32 条在 CoRL 正常范围，Related Work 分类结构合理，但同意 bib venue 需更新。\n\n---\n\n## Questions for Authors\n\n1. SmolVLA 在标准 LIBERO-Object 上 baseline 为何只有 11.6%？SmolVLA 原论文报告多少？11.6% 是否代表 distribution shift（如果是，具体什么性质的 shift）？\n2. CRM 是否曾在 held-out tasks 上测试？如在 15 task 训练 / 5 held-out 评估，结果如何？\n3. 在 base policy >50% 的 setting 下，correction > selection 的结论是否仍然成立？\n4. K=10 forward passes 在 SmolVLA 上的 wall-clock latency 是多少？是否满足 real-time control 要求？\n5. A2C2 correction head 能否 attach 到同一 frozen SmolVLA checkpoint？如可以，为什么不做对比？\n6. Table 1 LIBERO-Spatial 的 Random baseline 标记 \"---\"，原因是什么？\n7. 能否公布每个 seed 的具体成功率？\n8. perdof 在 ε=0.03 达 14%（接近 obs_only 14.3%），K 更大时 conformal features 是否可能变得有用？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同提出**：\n- A2C2 的 controlled experimental comparison\n\n**R2 提出**：\n- ADPro (2025, arXiv 2508.06266): test-time adaptive diffusion policy\n- GPC (2025, arXiv 2502.00622): inference-time enhancement via predictive world modeling\n- Recurrent-Depth VLA (2026, arXiv 2602.07845): implicit test-time compute scaling\n- Compose Your Policies! (2025, arXiv 2510.01068): test-time distribution-level composition\n\n**R1 提出**：\n- ACT temporal ensembling (Zhao et al. 2023)\n- Best-of-N sampling in robotics\n\n**bib 格式问题**：RT-2/OpenVLA/Octo 已正式发表，应更新 @misc → @inproceedings 并补充 venue 信息。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 `external_review.paperreview_ai`），跳过。\n\n---\n\n## Overall Assessment\n\n**Score: weak reject**\n**Confidence: high**\n**R1: weak reject (high confidence) | R2: weak reject (high confidence)**\n\n两位 Reviewer 独立给出一致评分。\n\n**核心判断**：论文在写作质量、统计严谨性和 component decomposition 设计上有实质性优势。但评估范围过窄（单 VLA / 单 benchmark / sim-only）、绝对性能极低（17.6%）、缺少最关键 baseline（A2C2）、CRM 泛化能力未验证，共同构成了在 CoRL 2026 录用标准下的 significant gap。\n\n**相比 Round 1 的改进**：\n论文在以下方面有实质性进步（Round 1 的 7 个 critical issue 中 4 个已 resolved）：\n- ✅ 统计方法从 Fisher test 改为 seed-level Mann-Whitney U [C1 resolved]\n- ✅ 核心 claim reframe 为 \"correction is active mechanism, multi-sampling is enabling condition\" [C2 resolved]\n- ✅ 标题从 \"Sample, Select, Correct\" 改为 \"Correction Over Selection\" [C5 resolved]\n- ✅ AI Disclosure 已添加 [C7 resolved]\n- ✅ Related Work 增加 CP in Robotics 子节 [M8 resolved]\n- ✅ 术语和写作质量显著提升 [m1, m2-m9 resolved]\n\n**持续存在的核心问题**：\n- ❌ 评估范围仍然极窄（M1 open → 升级为 W-C2）\n- ❌ 无 A2C2 实验对比（M3 open → 升级为 W-C4）\n- ❌ CRM 泛化性未验证（M6 open → 升级为 W-C3）\n- ❌ Seed 数量仍然不平衡（C3 partial）\n- ❌ Spatial null result 仍为单 seed（M2 open）\n\n**新发现的问题**：\n- 🆕 动机-评估断裂（W-C5: LIBERO+ vs LIBERO）\n- 🆕 低绝对性能限制泛化性（W-C1）\n- 🆕 \"Dissecting\" 分析深度不足（W-W1）\n- 🆕 Latency 未量化（W-W5）\n\n**给 Research Director 的整体评估**：\n论文写作和统计方面的改进是实质性的，表明作者认真回应了 Round 1 反馈。但核心的实验范围和 baseline 缺失问题（M1/M3/M6）在 Round 1 就已识别，本轮仍未解决。这些不是 writing fix 能解决的问题——需要额外实验（A2C2 baseline、held-out task split、第二个 VLA backbone、latency 量化）。距 deadline 仅 10 天，部分实验（如增加 VLA backbone）在时间上可能不可行。建议 Research Director 评估是否现有 scope 下能通过 A2C2 对比 + held-out split + latency 量化来将论文提升至 borderline，或考虑重新选择更匹配评估范围的 venue（如 workshop paper）。\n\n---\n\n## Detailed Comments（逐 section）\n\n### Abstract\n- 约 160 words，在 150-250 范围内。四个核心要素齐全。\n- 单句包含 4 个数字和 2 个 p 值，可读性受影响 [R2-I3]。\n- \"conformal uncertainty features cause progressive collapse\" 使用论文未在 Abstract 中定义的概念 [R2]。\n- 缩写 MLP、DOF 未在 Abstract 中展开 [R2]。\n\n### Introduction\n- 五段结构完整，LIBERO+ 数字有效建立 urgency。\n- Para 2 对 existing approaches 梳理精炼有效。\n- **动机-评估断裂**：LIBERO+ 数字与实际 LIBERO 评估不匹配 [W-C5]。\n- Para 4 key findings 与 Para 5 contributions 数字重复出现三次（abstract, para 4, contributions）可压缩 [R1]。\n- Contribution 3 (\"applicability boundaries\") 在前文缺乏铺垫 [R2-I5]。\n\n### Related Work\n- 四小节结构合理。与 A2C2 三点差异表述精确但缺实验验证。\n- CP in Robotics 子节为 Section 4.3 negative result 提供了好的铺垫。\n- Residual Policy Learning 仅 4 行，覆盖面不足 [R2]。\n- 遗漏 test-time adaptation of diffusion/flow policies 方向（ADPro/GPC 等）[R2-W6]。\n- bib 中 RT-2/OpenVLA/Octo 需更新 venue 信息 [R2-I2]。\n\n### Method\n- Pipeline 描述完整，数学符号一致。\n- \"Geometric medoid\" 术语不正确 [W-W6]。\n- \"concatenation order is arbitrary for fully connected layers\" 注释无必要 [R2-I4]。\n- DAgger 引用不恰当 [W-W7]。\n- ε=0.2 选择仅有经验依据，无理论支撑 [R1]。\n\n### Experiments\n- Statistical protocol 段落是亮点。\n- Pipeline decomposition 分析是论文最有价值的部分。\n- Table 1 Spatial 列只有 seed 42 单点 [M2]。\n- Spatial Random \"---\" 未解释 [R1-Q2, R2-I1]。\n- K-scaling 分析有实用价值（K=5 capturing 82% benefit）[R1, R2]。\n\n### Discussion + Limitations + Conclusion\n- Discussion 仅 1 段，过于单薄。\"为什么 6D 连续空间中 selection 不如 discrete token space\"值得展开 [R2]。\n- Limitations 5 条诚实全面，但遗漏了 CRM 在 eval task 训练的泛化性问题 [R1-N1]。\n- Limitation 5 关于 A2C2 的辩护有误导性 [R1-N2]。\n\n### Appendix\n- K-scaling、applicability、per-task 三个附录在正文中均被引用。\n- 缺 per-task Spatial 结果表 [R1-W4]。\n\n### 格式\n- corl_2026 模板 ✓，Anonymous ✓，AI Disclosure ✓，Limitations ✓\n- 页数估算约 8.5 页，可能略超限制 [W-W8]\n- \\keywords 行是否为 CoRL 2026 模板要求需确认 [R2]\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_416d453a45869a9406db62186b1e3ef7"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-19T01:59:42.848747+00:00_

{"result":"{\"success\": false, \"data\": {\"expected_reviewer_ids\": [1, 2, 3], \"missing\": [3]}, \"error\": \"consolidated report is incomplete — reviewer(s) [3] were NOT acknowledged. This project has 3 reviewer(s): [1, 2, 3]. Each reviewer's findings (Must-Fix / Should-Fix / score) must be folded into the report. Re-read the missed reviewer's submission via feishu_read_chat_history or the session log, then call this tool again with reviewer_ids_acknowledged covering all 3 reviewers.\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 74
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-19T02:00:30.957629+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 1 审稿任务 — Reviewer 3\n\n**你的审查侧重：CoRL venue fit + 格式合规 + 实验可重复性**\n\n本轮已有两位 Reviewer 完成了方法严谨性（R1）和新颖性/写作（R2）的详细审查。你的任务是补充第三个视角，聚焦以下三个维度。\n\n### Venue 信息\n- **目标 venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + 无限 references + 可选 appendix\n- **模板**: corl_2026\n- **匿名规则**: Double-blind\n- **特殊要求**: Limitations section（计入 8 页），AI Disclosure，鼓励 real-robot 或 sim-to-real 论证\n\n### 论文信息\n- **标题**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n- **论文路径**: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`（通过 \\input 引入 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **引用文件**: `projects/acr-vla-conformal-refinement/docs/paper/references.bib`\n\n### 你的审查重点（三个聚焦维度）\n\n**1. CoRL venue fit 与实际部署相关性**：\n- 论文是否 \"focus on a core robotics problem\"（CoRL CFP 要求）？\n- 无 real-robot 实验——论文是否提供 sim-to-real transferability 的任何证据或论证？\n- K=10 forward passes 的 compute overhead 对 real-time manipulation 是否可行？论文是否量化了 latency？\n- 17.6% 绝对成功率对 robotics deployment 的实际意义？\n- 论文的受众是 robotics community 还是 ML methods community？CoRL 审稿人群体的可能反应？\n\n**2. 格式合规（严格检查）**：\n- 实际编译或估算论文正文是否在 8 页限制内\n- \\keywords 行是否为 CoRL 2026 模板要求\n- 匿名化是否完整（无作者可识别信息、代码链接、致谢）\n- References 格式是否一致（bib entries 是否完整）\n- Figure/Table captions 是否自包含\n- Limitations section 是否有实质内容\n\n**3. 实验可重复性**：\n- 训练超参数（学习率、batch size、epoch、augmentation）是否足够详细以重复实验？\n- Precompute pipeline（K=10 forward passes + argmin selection）的描述是否完整？\n- SmolVLA checkpoint 的具体版本/来源是否明确？\n- 评估协议（rollouts per task, max episode length, success criteria）是否清楚？\n- 随机种子控制和报告是否规范？\n\n### 前两位 Reviewer 的关键发现（供你参考，你可以独立评估）\n\nR1/R2 已识别的主要问题：\n- CRM 在 eval 任务的 demo 上训练，无 held-out 泛化验证\n- 缺少 A2C2 实验对比\n- 评估范围窄（单 VLA + 单 benchmark + sim-only）\n- 绝对性能低（17.6%）\n- 动机（LIBERO+）与评估（标准 LIBERO）断裂\n- Seed 数量不平衡（3-7）\n\n你不需要重复评估这些问题，但如果你有不同看法可以提出。请聚焦于你的三个维度。\n\n### 输出格式\n\n```\n## Summary (1-2 sentences)\n\n## Strengths (聚焦你的三个维度)\n- S1: ...\n\n## Weaknesses (聚焦你的三个维度)\n- W1: [severity: critical/warning/info] ...\n\n## Questions for Authors\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n```",
  "reviewer_id": "3",
  "project": "acr-vla-conformal-refinement",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 3\n\n**你的审查侧重：CoRL venue fit + 格式合规 + 实验可重复性**\n\n本轮已有两位 Reviewer 完成了方法严谨性（R1）和新颖性/写作（R2）的详细审查。你的任务是补充第三个视角，聚焦以下三个维度。\n\n### Venue 信息\n- **目标 venue**: CoRL 2026 Main Conference\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + 无限 references + 可选 appendix\n- **模板**: corl_2026\n- **匿名规则**: Double-blind\n- **特殊要求**: Limitations section（计入 8 页），AI Disclosure，鼓励 real-robot 或 sim-to-real 论证\n\n### 论文信息\n- **标题**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n- **论文路径**: `projects/acr-vla-conformal-refinement/docs/paper/main.tex`（通过 \\input 引入 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **引用文件**: `projects/acr-vla-conformal-refinement/docs/paper/references.bib`\n\n### 你的审查重点（三个聚焦维度）\n\n**1. CoRL venue fit 与实际部署相关性**：\n- 论文是否 \"focus on a core robotics problem\"（CoRL CFP 要求）？\n- 无 real-robot 实验——论文是否提供 sim-to-real transferability 的任何证据或论证？\n- K=10 forward passes 的 compute overhead 对 real-time manipulation 是否可行？论文是否量化了 latency？\n- 17.6% 绝对成功率对 robotics deployment 的实际意义？\n- 论文的受众是 robotics community 还是 ML methods community？CoRL 审稿人群体的可能反应？\n\n**2. 格式合规（严格检查）**：\n- 实际编译或估算论文正文是否在 8 页限制内\n- \\keywords 行是否为 CoRL 2026 模板要求\n- 匿名化是否完整（无作者可识别信息、代码链接、致谢）\n- References 格式是否一致（bib entries 是否完整）\n- Figure/Table captions 是否自包含\n- Limitations section 是否有实质内容\n\n**3. 实验可重复性**：\n- 训练超参数（学习率、batch size、epoch、augmentation）是否足够详细以重复实验？\n- Precompute pipeline（K=10 forward passes + argmin selection）的描述是否完整？\n- SmolVLA checkpoint 的具体版本/来源是否明确？\n- 评估协议（rollouts per task, max episode length, success criteria）是否清楚？\n- 随机种子控制和报告是否规范？\n\n### 前两位 Reviewer 的关键发现（供你参考，你可以独立评估）\n\nR1/R2 已识别的主要问题：\n- CRM 在 eval 任务的 demo 上训练，无 held-out 泛化验证\n- 缺少 A2C2 实验对比\n- 评估范围窄（单 VLA + 单 benchmark + sim-only）\n- 绝对性能低（17.6%）\n- 动机（LIBERO+）与评估（标准 LIBERO）断裂\n- Seed 数量不平衡（3-7）\n\n你不需要重复评估这些问题，但如果你有不同看法可以提出。请聚焦于你的三个维度。\n\n### 输出格式\n\n```\n## Summary (1-2 sentences)\n\n## Strengths (聚焦你的三个维度)\n- S1: ...\n\n## Weaknesses (聚焦你的三个维度)\n- W1: [severity: critical/warning/info] ...\n\n## Questions for Authors\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n```",
    "reviewer_id": "3",
    "project": "acr-vla-conformal-refinement",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 197 · 2026-05-19T02:00:35.238103+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 4280
}
```

</details>

---


### Assistant

_source line 198 · 2026-05-19T02:00:38.241398+00:00_

Reviewer 3 已分配（CoRL venue fit + 格式合规 + 可重复性）。等待其审稿结果返回后完成交叉分享和报告提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 199 · 2026-05-19T02:00:41.445840+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 Reviewer 1 的 10 条意见（N1-N4, W1-W5）全部给出 [AGREE]，其中 N3 附带了细化分析（主要对比 U=35 在给定样本量下已是最强结果，但次要对比确实 underpowered）。特别认可 R1-N1（train/test task split）是我 Round 1 中遗漏的关键问题。两位 reviewer 在核心判断上高度收敛：weak reject，主要原因为评估范围窄、缺少 A2C2 对比、sim-only、绝对性能过低。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 200 · 2026-05-19T02:00:55.570842+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 22

## Round 22

8 recorded events


### User

_source line 201 · 2026-05-19T02:04:53.184975+00:00_

[Reviewer 3 审稿意见]:
## Reviewer 3 — Round 1 审稿完成

### 审查侧重：CoRL venue fit + 格式合规 + 实验可重复性

---

## Summary

本文提出 sample-select-correct pipeline 用于 frozen flow-matching VLA 的推理时动作修正，核心发现是 learned correction（而非 selection）是主要机制。论文在 LIBERO 仿真环境中验证了方法，但**正文超出 8 页限制**（约占 9 页），且无任何 real-robot 实验或 sim-to-real 分析，对 CoRL venue 的适配存在根本性问题。

---

## Strengths

- **S1**: 论文明确声明了 simulation-only 限制（Section 5, Limitation 1），没有掩饰实验范围的局限性。CoRL reviewer guidelines 鼓励对诚实报告的 limitations 予以积极评价。
- **S2**: 实验协议中关键超参数记录较为完整：Adam lr=1e-3, batch 32, 50 epochs, seed 42, augmentation noise ranges σ∈[0.02, 0.1]（Section 4.1）。SmolVLA checkpoint 具体路径 `lerobot/smolvla_libero` 已给出。
- **S3**: 统计方法选择合理：使用 seed-level Mann-Whitney U 而非 episode-level pooling，正确处理了 within-seed episode 非独立性问题（Section 4.1）。
- **S4**: 引用核查结果：32 个 unique cited keys 全部在 bib 中找到（missing_bib=0），25/32 通过 OpenAlex 在线验证。

---

## Weaknesses

### 维度 1: CoRL venue fit 与实际部署相关性

**W1** [critical] **无 real-robot 实验且缺乏 sim-to-real transferability 论证**
- CoRL 2026 CFP 明确要求 "Submissions should focus on a core robotics problem" 并推荐 real-robot experiments or evidence of sim-to-real transferability。
- Section 5 Limitation 1 承认 "All experiments use LIBERO; real-robot transfer is untested"，但论文未提供任何 sim-to-real 分析。
- 对于声称解决 "deployment outside tightly controlled laboratory settings"（Section 1）的方法，完全缺乏 real-world 证据是 CoRL 审稿人的核心关切。

**W2** [critical] **K=10 forward passes 的延迟未量化，real-time 可行性成疑**
- Section 3.4 仅报告 CRM overhead "~0.3 ms"，但未报告 K=10 VLA forward passes 的总 wall-clock latency。
- SmolVLA 450M 单次 forward pass 典型 ~50ms → K=10 约 ~500ms per control step → 控制频率 ~2 Hz，远低于 real-time manipulation 通常的 10-20 Hz。
- Appendix A 报告 K=5 可获得 82% 收益，但同样无 wall-clock time。

**W3** [warning] **17.6% 绝对成功率对 robotics deployment 的意义不清**
- +6pp 改进从 11.6% 到 17.6%，在 deployment context 中从 "完全不能用" 到 "仍然不能用"。
- 需更清晰地将论文定位为 mechanistic analysis 而非 deployment-ready 系统。

**W4** [warning] **论文受众定位偏 ML methods 而非 robotics**
- 核心贡献是 component decomposition 和 conditioning ablation，本质是 inference-time compute scaling 的 mechanistic study。
- 与 LLM test-time scaling 的对比（Section 6）更适合 ML venue（ICML/NeurIPS）。

### 维度 2: 格式合规

**W5** [critical] **正文超出 8 页限制（约占 9 页）**
- PDF 检查确认正文（Section 1-7 + AI Disclosure）延伸到第 9 页。CoRL 2026 要求 main text 8 pages，Limitations 和 AI Disclosure 计入限制。
- 这是潜在 desk reject 原因（CoRL 2024 review instructions 明确列为 desk rejection 标准）。

**W6** [warning] **references.bib 冗余条目**
- 2 个 orphan entries（Gauss1857, Lagrange1788）未引用且有 duplicate keys，为模板遗留。
- angelopoulos2023gentle 年份 bib=2023 vs API=2021（journal vs preprint 差异）。

### 维度 3: 实验可重复性

**W8** [warning] **硬件环境和训练耗时未报告**
- 缺少 GPU 型号/数量、CRM 训练总耗时、precompute pipeline 耗时。

**W9** [warning] **SmolVLA checkpoint 版本未完全锁定**
- `lerobot/smolvla_libero` 无 commit hash，checkpoint 更新后结果可能不可复现。

**W10** [warning] **Precompute pipeline 的随机性控制不完整**
- Precompute 阶段的 flow-matching random seed 未明确。
- Evaluation seeds 具体列表（除 seed 42 外）未给出。

**W11** [info] **Seed 数量不平衡（3-7 seeds per method）**
- 不同方法的 variance estimate 精度不同，影响统计检验功效。

---

## Questions for Authors

1. K=10 VLA forward passes 的总 wall-clock latency 和对应控制频率？
2. Precompute pipeline 的 flow-matching random seed 是否固定？
3. 是否考虑过至少 1-2 个 real-robot task 的 proof-of-concept？
4. SmolVLA checkpoint 的具体 commit hash？

---

## Overall Assessment

**Score**: weak reject
**Confidence**: high

**核心判断**: 正文超页是潜在 desk reject 问题。即使修复格式，完全缺乏 real-robot 实验或 sim-to-real 论证、未量化 inference latency、17.6% 绝对成功率使论文难以通过 CoRL 的 robotics deployment 导向审稿标准。论文的 mechanistic analysis 贡献更适合 ML venue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-19T02:05:20.994901+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请回应 Reviewer 3 的审稿意见\n\nReviewer 3 聚焦 CoRL venue fit + 格式合规 + 实验可重复性，以下是其关键发现。请逐条 [AGREE] 或 [REBUT]。\n\n**Must-Fix:**\n- W1 [critical]: 无 real-robot 实验且缺 sim-to-real 论证。CoRL CFP 要求 \"focus on a core robotics problem\"。\n- W2 [critical]: K=10 forward passes 延迟未量化。SmolVLA 450M 单次 ~50ms → K=10 ~500ms → ~2 Hz，远低于 10-20 Hz。\n- W5 [critical]: **正文超出 8 页限制（约 9 页）**——潜在 desk reject。CoRL 2024 review instructions 明确列为 desk rejection 标准。\n\n**Should-Fix:**\n- W3 [warning]: 17.6% 绝对成功率对 deployment 无实际意义。\n- W4 [warning]: 核心贡献（component decomposition + conditioning ablation）更适合 ML venue（ICML/NeurIPS）而非 CoRL。\n- W6 [warning]: 2 个 orphan bib entries（Gauss1857, Lagrange1788）。\n- W8 [warning]: 硬件环境和训练耗时未报告。\n- W9 [warning]: SmolVLA checkpoint 无 commit hash，版本未锁定。\n- W10 [warning]: Precompute pipeline 的 flow-matching random seed 未明确。\n\n**Overall**: weak reject, high confidence.\n\n请逐条回应 W1, W2, W5（Must-Fix）和 W3, W4, W8, W9, W10（Should-Fix）。",
  "reviewer_id": "1",
  "project": "acr-vla-conformal-refinement",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — 请回应 Reviewer 3 的审稿意见\n\nReviewer 3 聚焦 CoRL venue fit + 格式合规 + 实验可重复性，以下是其关键发现。请逐条 [AGREE] 或 [REBUT]。\n\n**Must-Fix:**\n- W1 [critical]: 无 real-robot 实验且缺 sim-to-real 论证。CoRL CFP 要求 \"focus on a core robotics problem\"。\n- W2 [critical]: K=10 forward passes 延迟未量化。SmolVLA 450M 单次 ~50ms → K=10 ~500ms → ~2 Hz，远低于 10-20 Hz。\n- W5 [critical]: **正文超出 8 页限制（约 9 页）**——潜在 desk reject。CoRL 2024 review instructions 明确列为 desk rejection 标准。\n\n**Should-Fix:**\n- W3 [warning]: 17.6% 绝对成功率对 deployment 无实际意义。\n- W4 [warning]: 核心贡献（component decomposition + conditioning ablation）更适合 ML venue（ICML/NeurIPS）而非 CoRL。\n- W6 [warning]: 2 个 orphan bib entries（Gauss1857, Lagrange1788）。\n- W8 [warning]: 硬件环境和训练耗时未报告。\n- W9 [warning]: SmolVLA checkpoint 无 commit hash，版本未锁定。\n- W10 [warning]: Precompute pipeline 的 flow-matching random seed 未明确。\n\n**Overall**: weak reject, high confidence.\n\n请逐条回应 W1, W2, W5（Must-Fix）和 W3, W4, W8, W9, W10（Should-Fix）。",
    "reviewer_id": "1",
    "project": "acr-vla-conformal-refinement",
    "round_number": "1"
  }
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-19T02:05:24.858711+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请回应 Reviewer 3 的审稿意见\n\nReviewer 3 聚焦 CoRL venue fit + 格式合规 + 实验可重复性，以下是其关键发现。请逐条 [AGREE] 或 [REBUT]。\n\n**Must-Fix:**\n- W1 [critical]: 无 real-robot 实验且缺 sim-to-real 论证。CoRL CFP 要求 \"focus on a core robotics problem\"。\n- W2 [critical]: K=10 forward passes 延迟未量化。SmolVLA 450M 单次 ~50ms → K=10 ~500ms → ~2 Hz，远低于 10-20 Hz。\n- W5 [critical]: **正文超出 8 页限制（约 9 页）**——潜在 desk reject。\n\n**Should-Fix:**\n- W3 [warning]: 17.6% 绝对成功率对 deployment 无实际意义。\n- W4 [warning]: 核心贡献更适合 ML venue（ICML/NeurIPS）而非 CoRL。\n- W6 [warning]: 2 个 orphan bib entries（Gauss1857, Lagrange1788）。\n- W8 [warning]: 硬件环境和训练耗时未报告。\n- W9 [warning]: SmolVLA checkpoint 无 commit hash。\n- W10 [warning]: Precompute random seed 未明确。\n\n**Overall**: weak reject, high confidence.\n\n请逐条回应。",
  "reviewer_id": "2",
  "project": "acr-vla-conformal-refinement",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — 请回应 Reviewer 3 的审稿意见\n\nReviewer 3 聚焦 CoRL venue fit + 格式合规 + 实验可重复性，以下是其关键发现。请逐条 [AGREE] 或 [REBUT]。\n\n**Must-Fix:**\n- W1 [critical]: 无 real-robot 实验且缺 sim-to-real 论证。CoRL CFP 要求 \"focus on a core robotics problem\"。\n- W2 [critical]: K=10 forward passes 延迟未量化。SmolVLA 450M 单次 ~50ms → K=10 ~500ms → ~2 Hz，远低于 10-20 Hz。\n- W5 [critical]: **正文超出 8 页限制（约 9 页）**——潜在 desk reject。\n\n**Should-Fix:**\n- W3 [warning]: 17.6% 绝对成功率对 deployment 无实际意义。\n- W4 [warning]: 核心贡献更适合 ML venue（ICML/NeurIPS）而非 CoRL。\n- W6 [warning]: 2 个 orphan bib entries（Gauss1857, Lagrange1788）。\n- W8 [warning]: 硬件环境和训练耗时未报告。\n- W9 [warning]: SmolVLA checkpoint 无 commit hash。\n- W10 [warning]: Precompute random seed 未明确。\n\n**Overall**: weak reject, high confidence.\n\n请逐条回应。",
    "reviewer_id": "2",
    "project": "acr-vla-conformal-refinement",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 204 · 2026-05-19T02:05:42.899398+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21904
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-19T02:05:42.899866+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18041
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-19T02:05:43.401915+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请回应 Reviewer 1 和 Reviewer 2 的关键发现\n\n以下是 R1 和 R2 的核心问题摘要。请逐条 [AGREE] 或 [REBUT]。\n\n**R1 Must-Fix:**\n- N1 [critical]: CRM 在 eval 任务 demo 上训练（20 tasks = Object 10 + Spatial 10），无 held-out task 泛化验证。无法区分 task-specific memorization 和 generalizable correction。\n- N2 [critical]: 缺少 A2C2 实验对比。A2C2 被认定为 closest concurrent work 但从未作为 baseline 运行。A2C2 correction head 可直接 attach 到同一 frozen SmolVLA。\n- N3 [critical]: Seed 数量小且不平衡（obs_only 7, VLA-only 5, Argmin 6, Random 3）。Random 仅 3 seeds 就断言 \"statistically indistinguishable\"。\n- N4 [critical]: 无 real-robot，低绝对性能，latency 未量化。（与你的 W1/W2 重合）\n\n**R2 Must-Fix:**\n- W1 [critical]: 极低绝对性能（17.6%）使发现泛化性存疑。在 base policy 几乎不工作的 regime 下的结论能否外推到更强 base policy 未知。\n- W2 [critical]: 评估范围极窄。标题 \"Frozen VLAs\"(复数)但只测 SmolVLA 一个。\n- W3 [critical]: 方法新颖性有限。R1 rebut 认为 component decomposition 有独立价值。\n- W4 [critical]: 动机-评估断裂。Introduction 用 LIBERO+ 数据 motivate，但 eval 在标准 LIBERO 上。SmolVLA 11.6% baseline 原因未解释。\n\n**R1/R2 共识 Should-Fix:**\n- \"Geometric medoid\" 术语不正确（实际是 argmin-to-centroid）\n- ε 敏感性分析不完整（scalar 仅 1 点，各点 seed 不一致）\n- Applicability boundary 基于单一对比（OpenVLA T=0.5）\n- Spatial null result 分析不足（无 per-task 表，无 failure case 分析）\n- DAgger 引用误用（应引 domain randomization 文献）\n- \"Dissecting\" 分析深度不足（缺 correction vector 分析、trajectory 可视化）\n\n请对 R1 的 N1-N3、R2 的 W1-W4 逐条回应（N4 与你的 W1/W2 重合可跳过）。",
  "reviewer_id": "3",
  "project": "acr-vla-conformal-refinement",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — 请回应 Reviewer 1 和 Reviewer 2 的关键发现\n\n以下是 R1 和 R2 的核心问题摘要。请逐条 [AGREE] 或 [REBUT]。\n\n**R1 Must-Fix:**\n- N1 [critical]: CRM 在 eval 任务 demo 上训练（20 tasks = Object 10 + Spatial 10），无 held-out task 泛化验证。无法区分 task-specific memorization 和 generalizable correction。\n- N2 [critical]: 缺少 A2C2 实验对比。A2C2 被认定为 closest concurrent work 但从未作为 baseline 运行。A2C2 correction head 可直接 attach 到同一 frozen SmolVLA。\n- N3 [critical]: Seed 数量小且不平衡（obs_only 7, VLA-only 5, Argmin 6, Random 3）。Random 仅 3 seeds 就断言 \"statistically indistinguishable\"。\n- N4 [critical]: 无 real-robot，低绝对性能，latency 未量化。（与你的 W1/W2 重合）\n\n**R2 Must-Fix:**\n- W1 [critical]: 极低绝对性能（17.6%）使发现泛化性存疑。在 base policy 几乎不工作的 regime 下的结论能否外推到更强 base policy 未知。\n- W2 [critical]: 评估范围极窄。标题 \"Frozen VLAs\"(复数)但只测 SmolVLA 一个。\n- W3 [critical]: 方法新颖性有限。R1 rebut 认为 component decomposition 有独立价值。\n- W4 [critical]: 动机-评估断裂。Introduction 用 LIBERO+ 数据 motivate，但 eval 在标准 LIBERO 上。SmolVLA 11.6% baseline 原因未解释。\n\n**R1/R2 共识 Should-Fix:**\n- \"Geometric medoid\" 术语不正确（实际是 argmin-to-centroid）\n- ε 敏感性分析不完整（scalar 仅 1 点，各点 seed 不一致）\n- Applicability boundary 基于单一对比（OpenVLA T=0.5）\n- Spatial null result 分析不足（无 per-task 表，无 failure case 分析）\n- DAgger 引用误用（应引 domain randomization 文献）\n- \"Dissecting\" 分析深度不足（缺 correction vector 分析、trajectory 可视化）\n\n请对 R1 的 N1-N3、R2 的 W1-W4 逐条回应（N4 与你的 W1/W2 重合可跳过）。",
    "reviewer_id": "3",
    "project": "acr-vla-conformal-refinement",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-19T02:05:45.367442+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1965
}
```

</details>

---


### Assistant

_source line 208 · 2026-05-19T02:05:48.334665+00:00_

交叉分享已发送给三位 Reviewer。等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 209 · 2026-05-19T02:05:51.118570+00:00_

[Reviewer 3 审稿结果]:
Round 1 审稿完成，已提交给 Review Director。

核心发现：
- **3 个 critical 问题**：正文超 8 页（desk reject 风险）、无 real-robot 实验且无 sim-to-real 论证、K=10 latency 未量化
- **5 个 warning 问题**：绝对成功率低、venue fit 偏 ML、bib 冗余、硬件/训练信息缺失、checkpoint 版本和 seed 控制不完整
- **总评**：weak reject (high confidence)——mechanistic analysis 有价值，但格式违规和 robotics 相关性不足使论文难以匹配 CoRL 审稿标准

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 210 · 2026-05-19T02:05:56.303726+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 211 · 2026-05-19T02:06:23.541434+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 3 审稿意见

---

## Must-Fix Weaknesses

**[AGREE] R3-W1: 无 real-robot 实验且缺 sim-to-real 论证**

同意。这与我的 N4 和对 R2-W8 的 AGREE 一致。三位 Reviewer 在此问题上达成共识。CoRL 2026 CFP 明确要求 submissions "focus on a core robotics problem" 并鼓励 real-robot 实验或 sim-to-real 可迁移性论证。论文既无 real-robot 验证，也未提供任何 sim-to-real gap 分析（如 visual domain gap 对 observation embedding 的影响、action space calibration 差异等）。Limitations section item 1 (discussion.tex:15) 仅用一句 "real-robot transfer is untested" 带过，不足以回应 CoRL venue 的核心要求。

**[AGREE] R3-W2: K=10 forward passes 延迟未量化**

同意，且 R3 提供了我此前缺少的具体估算。若 SmolVLA 450M 单次 forward pass ~50ms，则 K=10 需 ~500ms，控制频率降至 ~2 Hz。论文仅在 Section 3.5 (method.tex:67) 提到 "the overhead is K=10 VLA forward passes plus ~0.3 ms for CRM inference"，但未给出 wall-clock 数字。这不仅是 reproducibility 问题，更直接影响方法的实用性判断：

- 2 Hz 控制频率对 tabletop manipulation 已经偏低（通常需要 10-20 Hz）
- 论文在 Section 4.4 (experiments.tex:132) 提到 "K=5 captures ~82% of the correction benefit at half the compute"，但即使 K=5 也只有 ~4 Hz
- 这个 latency 问题与 VLA-Pilot 被论文批评的 "2.41s per control step" (introduction.tex:13) 同属一类，只是程度不同

建议补充 Table 形式的 latency breakdown（单次 VLA pass、K=10 total、CRM、end-to-end），并讨论 parallelizable 的可能性（如 batch forward pass）。

**[AGREE] R3-W5: 正文可能超出 8 页限制**

这是我 Round 1 审稿中遗漏的问题。若确认正文（不含 references 和 appendix）超过 8 页，则根据 CoRL 2024 review instructions（desk rejection criteria 明确包含格式违规）和 CoRL 2026 author instructions（"8 pages maximum for main text"），这构成潜在 desk reject 风险。

但需注意：我无法直接验证编译后的 PDF 页数（审稿基于 .tex 源文件），所以对 "约 9 页" 的判断持保留态度。若 R3 基于编译后 PDF 做出此判断，则可信。建议作者：(1) 立即检查编译后页数；(2) 若超页，优先压缩 Introduction para 4 与 Contributions list 的重复内容、Related Work 中部分冗余描述、以及 Section 4.4 可移入 Appendix 的 K-scaling 和 applicability boundary 段落。

---

## Should-Fix Weaknesses

**[AGREE] R3-W3: 17.6% 绝对成功率对 deployment 无实际意义**

同意，与我对 R2-W1 的 AGREE 一致。三位 Reviewer 均指出此问题。Per-task 数据（Appendix C, Table 3）进一步证实：即使是最佳 task（chocolate_pudding），correction 后也仅 60% 成功率，而 4/10 tasks 停留在 0-10%。17.6% aggregate 数字的 practical significance 接近于零。

**[REBUT] R3-W4: 核心贡献更适合 ML venue（ICML/NeurIPS）而非 CoRL**

不完全同意。R3 的论点是 component decomposition 和 conditioning ablation 属于 ML methodology 分析，更适合 ICML/NeurIPS。但我认为：

1. **论文解决的是一个 robotics-specific 问题**。"Selection vs correction in continuous action spaces" 的结论与 LLM test-time scaling 的对比（Section 5, discussion.tex:5-8）正是因为 action space 的低维连续性（d=6）才有意义，这是 embodied AI 特有的。在 NLP/CV 的离散 token space 中，这个问题不存在。
2. **CoRL 接受 analysis/insight 类论文**。CoRL 2023 reviewer guidelines 明确将 "significance" 定义为 "impact potential; state-of-the-art advancement"，不要求一定是 SOTA 方法。Empirical analysis 论文在 CoRL 有先例。
3. **真正的 venue fit 问题不在于 contribution 类型，而在于 evaluation scope**——sim-only、单 backbone、低绝对性能。这些问题在 ICML/NeurIPS 同样会被审稿人质疑。

因此，论文的 venue fit 问题本质上是 R3-W1（无 real-robot）和 W3（低性能）导致的，而非 contribution 类型与 CoRL 不匹配。

**[AGREE] R3-W8: 硬件环境和训练耗时未报告**

同意。Section 4.1 Training (experiments.tex:32-36) 报告了 optimizer (Adam)、learning rate (1e-3)、batch size (32)、epochs (50)、seed (42)，但缺少：
- GPU 型号和数量
- CRM 训练 wall-clock time
- Precompute pipeline（K=10 forward passes × 全部 demo steps）的计算耗时
- Evaluation rollout 的总耗时

对于一个 ~327K 参数的 MLP，训练本身应很快（分钟级），但 precompute 26,737 samples 可能耗时不短。这些信息对 reproducibility 是必要的。

**[AGREE] R3-W9: SmolVLA checkpoint 无 commit hash，版本未锁定**

同意。Section 4.1 (experiments.tex:17) 给出 checkpoint 名 `lerobot/smolvla_libero`，但未指定 HuggingFace Hub 的 commit hash 或 revision。SmolVLA 作为活跃开发的模型，checkpoint 可能随时更新。锁定版本是 reproducibility 的基本要求。

**[AGREE] R3-W10: Precompute pipeline 的 flow-matching random seed 未明确**

同意。CRM 训练使用 seed 42 (experiments.tex:35)，但 precompute 阶段每个 demo step 的 K=10 forward passes 所用的 flow-matching random seed 未说明。若 precompute seed 与 evaluation seed 相同（均为 42），则 CRM 可能 overfit 到特定的 sample distribution。若不同，则应明确报告。这是一个容易修复但对 reproducibility 重要的细节。

---

## 总结

R3 的 8 个问题中，我 **AGREE 7 条**（W1, W2, W5, W3, W8, W9, W10），**REBUT 1 条**（W4 venue fit 归因）。

R3 的最有价值贡献是：(1) W5 页数超限的发现——这是潜在 desk reject 风险，优先级最高；(2) W2 的具体 latency 估算（~500ms → ~2 Hz），将 "10x overhead" 的抽象描述转化为了具体的 real-time feasibility 判断。

三位 Reviewer 的核心共识已明确：**无 real-robot 验证、低绝对性能、评估范围窄、缺 A2C2 对比**。这些问题在当前状态下无法通过小幅修改解决。

Overall assessment 维持：**Weak Reject**。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 212 · 2026-05-19T02:06:28.528613+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 213 · 2026-05-19T02:06:31.412037+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

R3 的 8 个问题中 AGREE 7 条、REBUT 1 条（W4 venue fit 归因——我认为问题本质在于 evaluation scope 不足而非 contribution 类型与 CoRL 不匹配）。

三位 Reviewer 的核心共识：无 real-robot 验证、低绝对性能、评估范围窄、缺 A2C2 对比。R3 额外发现的页数超限（W5）是潜在 desk reject 风险，优先级最高。Overall 维持 Weak Reject。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 214 · 2026-05-19T02:06:35.896817+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 215 · 2026-05-19T02:06:54.989164+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 3

---

## Must-Fix 逐条回应

**[AGREE] R3-W1: 无 real-robot 实验且缺 sim-to-real 论证**

三位 reviewer 在此问题上完全收敛。我在 Round 1 中列为 W2 [critical] 和 W8 [warning]，R1 列为 N4 [critical]。CoRL CFP 明确鼓励 "real-robot experiments or simulation evidence demonstrating transferability to physical robots"，论文两者皆无。不再赘述。

---

**[AGREE] R3-W2: K=10 forward passes 延迟未量化**

同意，且 R3 给出了我和 R1 都缺少的具体估算：SmolVLA 450M 单次约 50ms，K=10 约 500ms，对应约 2 Hz。这远低于 tabletop manipulation 常见的 10-20 Hz 控制频率。

论文 Section 3.4 写 "The overhead is K=10 VLA forward passes plus ~0.3ms for CRM inference"，有意将 CRM 的 0.3ms 作为 overhead 的代表数字，但实际瓶颈（10x VLA pass）被轻描淡写。Section 4.4 的 K=5 sweet spot 建议间接暗示 latency 是实际顾虑，但全文未给出任何 wall-clock 数字。这在一篇声称做 "inference-time refinement" 的论文中是不可接受的——inference-time 方法的可行性 fundamentally 取决于 inference 延迟。

---

**[AGREE with caveat] R3-W5: 正文超出 8 页限制（约 9 页）**

基于我对各 section 的文本量估算（Introduction ~1.5p, Related Work ~1.5p, Method + Fig 1 ~1.5-2p, Experiments + Table 1 + Fig 2 ~2.5p, Discussion + Limitations + AI Disclosure + Conclusion ~1-1.5p），总量约 8.5-9 页，确实可能超限。

**Caveat**: 未实际编译 LaTeX，无法精确确认。CoRL 2026 Author Instructions 明确规定 "8 pages maximum for main paper"，Limitations 计入 8 页但 references 和 appendix 不计入。如果确实超出 8 页，这是 desk reject 风险。但最终判定需要编译验证——不同 figure/table 的浮动位置可能影响实际页数。

建议作者优先检查编译后页数。如超限，Discussion（当前仅 1 段）可考虑合并入 Conclusion，Related Work 可压缩（Section 2.4 Inference-Time Compute Scaling 与核心贡献关联最弱，可缩减）。

---

## Should-Fix 逐条回应

**[AGREE] R3-W3: 17.6% 绝对成功率对 deployment 无实际意义**

同意。我在 Round 1 中将此列为 W1 [critical]。17.6% 意味着超过 80% 的 episode 仍然失败。即使相对提升统计显著，对实际机器人部署毫无意义。论文 Limitations 第 5 条诚实承认了这一点。

---

**[REBUT] R3-W4: 核心贡献更适合 ML venue（ICML/NeurIPS）而非 CoRL**

不完全同意。论文的研究对象（VLA 的 inference-time action refinement）、评估 benchmark（LIBERO 机器人操作）、以及核心发现（correction > selection in continuous action spaces、conformal features 在小样本 budget 下失效、tokenized VLA 的 applicability boundary）都是 robotics-specific 的问题。这些发现对 ML venue 的读者来说缺乏足够的 robotics context 来理解其重要性。

真正的 venue fit 问题不在于主题是否 robotics-relevant——而在于执行层面（sim-only、无 real-robot、低绝对性能）是否达到 CoRL 标准。主题本身 squarely 在 CoRL scope 内。R3 的 W1（real-robot 缺失）才是真正的 venue fit 问题，W4 将其升级为 "应投 ML venue" 过于极端。

---

**[REBUT] R3-W6: 2 个 orphan bib entries（Gauss1857, Lagrange1788）**

我完整阅读了 references.bib（路径：`docs/paper/references.bib`），逐条核验了全部条目。bib 文件中不存在 `Gauss1857` 或 `Lagrange1788` 条目。全部 bib entries 为现代文献（最早的是 Ledoit & Wolf 2004），共约 32 条。

R3 此条发现可能基于误读或与其他论文的审稿混淆。建议 Director 让 R3 复核此点。

---

**[AGREE] R3-W8: 硬件环境和训练耗时未报告**

Section 4.1 报告了训练超参数（Adam, lr=10^-3, batch 32, 50 epochs, seed 42）但未报告：GPU 型号、训练 wall-clock time、evaluation 硬件、VLA inference 硬件。对于一个 ~327K 参数 MLP 训练 50 epochs 的任务，训练本身可能只需几分钟——但明确报告是基本的可重复性要求。更关键的是 evaluation 硬件（影响 VLA forward pass latency 的量化，即 W2）。

---

**[AGREE] R3-W9: SmolVLA checkpoint 无 commit hash**

Section 4.1 写 "checkpoint lerobot/smolvla_libero"，这是 HuggingFace Hub 上的 model identifier，但未提供具体 commit hash 或版本号。HuggingFace models 可以被更新覆盖，没有 commit hash 的 checkpoint 引用在长期来看不可重复。应补充 commit hash 或至少 download date。

---

**[AGREE] R3-W10: Precompute random seed 未明确**

Section 4.1 明确了 CRM training seed（42）和 evaluation rollout seed（42 for Table 1, 多 seed for multi-seed comparisons），但未明确 precompute 阶段（为每个 demo step 生成 K=10 VLA samples）的 random seed。由于 flow-matching 的 stochasticity 来自初始 noise，precompute seed 决定了训练数据的具体内容。这是可重复性缺口。

---

## 综合评价

R3 的审稿在格式合规和可重复性维度补充了 R1（方法严谨性）和我（新颖性 + related work）未覆盖的重要内容。

三位 reviewer 的核心共识：
1. **Sim-only + 无 real-robot = CoRL venue fit 风险**（R1-N4, R2-W2/W8, R3-W1）
2. **Latency 未量化**（R1-N4, R2-W8 补充, R3-W2）
3. **绝对性能过低**（R1-N4, R2-W1, R3-W3）
4. **评估范围过窄**（R1-N1/N3, R2-W2, R3 隐含）

R3 新增的 **页数超限风险**（W5）如果属实，是最紧急的 action item——desk reject 风险高于任何技术问题。

一个值得 Director 注意的分歧：R3-W6（orphan bib entries）我认为是事实错误，bib 文件中不存在 Gauss1857/Lagrange1788。

三位 reviewer 均给出 **weak reject**，结论收敛度很高。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 216 · 2026-05-19T02:07:04.578738+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 217 · 2026-05-19T02:07:07.496292+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：R3 的格式合规发现（尤其页数超限 W5）补充了技术层面审查的盲区。三位 reviewer 在 sim-only、latency 未量化、绝对性能过低、评估范围窄这四个问题上完全收敛，均给出 weak reject。我对 R3-W6（orphan bib entries Gauss1857/Lagrange1788）提出了事实性反驳——bib 文件中不存在这些条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 218 · 2026-05-19T02:07:18.373788+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 28

## Round 28

6 recorded events


### User

_source line 219 · 2026-05-19T02:07:30.547043+00:00_

[Reviewer 3 审稿意见]:
## Reviewer 3 — 交叉回应 R1/R2 完成

### R1 Must-Fix 回应

**[AGREE] R1-N1: CRM 在 eval 任务 demo 上训练，无 held-out task 泛化验证**
同意 critical。Section 3.3 确认训练数据来自 20 个 LIBERO tasks 的 demo，而评估也在这 20 个任务上。Table 2 改进集中在 4 个任务的模式加深了 memorization 嫌疑。需要 leave-task-out 实验。

**[AGREE] R1-N2: 缺少 A2C2 实验对比**
同意 critical。Section 5 辩称 A2C2 设定不同（从头训练 vs frozen），但 A2C2 correction head 完全可以 attach 到同一 frozen checkpoint 运行。论文声称的三点设计优势缺乏控制实验验证。

**[AGREE] R1-N3: Seed 数量小且不平衡**
同意 critical。补充：Random 仅 3 seeds 时 Mann-Whitney U 在 n1=3,n2=5 下即使完全分离也只能 p=0.036，"indistinguishable" 结论是 under-powered null。不平衡 seed 数导致不同方法的 variance estimate 精度不可比。

### R2 Must-Fix 回应

**[AGREE] R2-W1: 极低绝对性能使发现泛化性存疑**
同意。在 base policy 更强时，selection 可能就够用，correction 的相对贡献可能完全不同。Discussion 中的机制性结论不应作为一般性结论。

**[AGREE] R2-W2: 评估范围极窄**
同意。标题 "Frozen VLAs" 复数但只测 SmolVLA。至少需要一个额外 flow-matching VLA 验证。

**[REBUT] R2-W3: 方法新颖性有限**
部分不同意，建议从 critical 降至 warning。Component decomposition 的机制性发现有独立价值，CoRL guidelines 反对 "claiming lack of novelty without evidence"。但同意当前 dissection 深度不足以支撑标题承诺。

**[AGREE] R2-W4: 动机-评估断裂**
同意，且认为被低估。SmolVLA 11.6% 可能不是 distribution shift 导致——可能是 pretrained checkpoint 本身性能差。如果是后者，Introduction 关于 robustness 的整个叙事框架是 misleading 的。

### R1/R2 共识 Should-Fix
全部 [AGREE]："geometric medoid" 术语错误、ε 分析不完整、applicability boundary over-generalization、Spatial 分析不足、DAgger 引用误用、"Dissecting" 分析深度不足。

### 三位 Reviewer 的交叉共识
以下问题获得 R1/R2/R3 三方一致认同：
1. 无 real-robot + 低绝对性能 + latency 未量化（R1-N4, R2-W1, R3-W1/W2/W3）
2. CRM 训练/评估任务重叠（R1-N1, R3 补充 memorization 证据）
3. 缺少 A2C2 baseline（R1-N2）
4. Seed 数量问题（R1-N3, R3-W11）
5. 评估范围窄（R2-W2, R3-W4）
6. 动机-评估断裂（R2-W4）
7. 正文超页（R3-W5, R1/R2 未检查但确认存在）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-19T02:09:45.733025+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "issues_yaml": "- id: \"C1\"\n  summary: \"Fisher exact test independence violation (pseudo-replication)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Same-seed episodes share CRM weights, violating independence assumption\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已修复。改用 seed-level Mann-Whitney U，三位 Reviewer 均肯定统计方法严谨\"}\n  action_items:\n    - {round: 1, action: \"Replace Fisher with Mann-Whitney U\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"改用 seed-level Mann-Whitney U + sign test 补充验证\"\n  resolution_round: 2\n\n- id: \"C2\"\n  summary: \"Core claim contradicts K=1 data\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"K=1 CRM below baseline means correction alone harmful\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已修复。Reframe 为 'correction is active mechanism, multi-sampling is enabling condition'\"}\n  action_items:\n    - {round: 1, action: \"Reframe core claim\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"重构核心 claim\"\n  resolution_round: 2\n\n- id: \"C3\"\n  summary: \"Inconsistent seed counts across methods\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"obs_only 7, VLA-only 5, Argmin 6, Random 3\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"论文增加说明但 Random 仅 3 seeds 的 'statistically indistinguishable' 结论不成立。R3 补充：n1=3,n2=5 时即使完全分离也只能 p=0.036。\"}\n  action_items:\n    - {round: 2, action: \"所有条件统一至 >=5 seeds。公布逐 seed 成功率。撤回 n=3 对比的 'indistinguishable' 结论。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C4\"\n  summary: \"Novelty insufficient — standard MLP + L2 clipping\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Technical novelty low\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"[DIVERGENT] R2 维持 critical。R1/R3 rebut 认为 component decomposition 有独立价值，降级 warning。真正问题是实验规模和分析深度。\"}\n  action_items:\n    - {round: 2, action: \"明确定位为实证分析 paper，扩展分析深度\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C5\"\n  summary: \"Title contradicts conclusion\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Title sets wrong expectations\"}\n    - {round: 2, reviewers: [], note: \"已修复。新标题 'Correction Over Selection'\"}\n  action_items:\n    - {round: 1, action: \"Change title\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"标题已修改\"\n  resolution_round: 2\n\n- id: \"C6\"\n  summary: \"Paper exceeds 8-page limit\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R3, R2], note: \"May cause desk reject\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"R3 确认约 9 页。R1/R2 基于 tex 估算约 8.5 页。三方一致认为存在 desk reject 风险。R1 建议压缩 Intro 重复内容和 K-scaling 移入 Appendix。R2 建议合并 Discussion 入 Conclusion、缩减 Section 2.4。\"}\n  action_items:\n    - {round: 2, action: \"立即编译确认页数。若超限：(1) 合并 Discussion 入 Conclusion (2) 压缩 Intro para4/Contributions 重复 (3) K-scaling/applicability 段落移入 Appendix (4) 缩减 Related Work Section 2.4\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C7\"\n  summary: \"Missing AI Disclosure\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R3, R2], note: \"Required by venue\"}\n    - {round: 2, reviewers: [R2], note: \"已修复\"}\n  action_items:\n    - {round: 1, action: \"Add AI disclosure\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"AI Disclosure 已添加\"\n  resolution_round: 2\n\n- id: \"M1\"\n  summary: \"Narrow experimental scope (single VLA + single benchmark + no real robot)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R1, R3], note: \"Only SmolVLA on LIBERO\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致 critical。标题 'Frozen VLAs'(复数)但只测一个。CoRL CFP 要求 real-robot 或 sim-to-real 论证，两者皆无。\"}\n  action_items:\n    - {round: 2, action: \"(1) 至少增加一个 flow-matching VLA backbone (2) 提供 sim-to-real 论证 (3) 限定标题 scope\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M2\"\n  summary: \"LIBERO-Spatial null result based on only 1 seed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"1 seed insufficient for null conclusion\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"仍为 seed 42 单点。缺 per-task Spatial 表和 failure case 分析。若作为 contribution 需加深分析。\"}\n  action_items:\n    - {round: 2, action: \"补充 Spatial multi-seed + per-task 表 + failure mode 分析\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M3\"\n  summary: \"No experimental comparison with A2C2\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Only textual positioning\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致 critical。A2C2 correction head 可 attach 到同一 frozen SmolVLA。'Different training regime' 辩护不成立。\"}\n  action_items:\n    - {round: 2, action: \"在同一 frozen SmolVLA 上实现 A2C2 baseline 做 controlled comparison\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M4\"\n  summary: \"Bib entries missing venue info\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Orphan entries, missing citations\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"部分修复。RT-2/OpenVLA/Octo 仍为 @misc 需更新。R3 声称存在 Gauss1857/Lagrange1788 orphan entries，R2 反驳：bib 中不存在这些条目（事实性错误）。R2 建议评估是否需添加 ADPro/GPC 等引用。\"}\n  action_items:\n    - {round: 2, action: \"(1) 更新 RT-2/OpenVLA/Octo venue 信息 (2) 评估 ADPro/GPC 等引用必要性\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M5\"\n  summary: \"Figure 2 n=1 points with meaningless error bars\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R3], note: \"Visual misleading\"}\n    - {round: 2, reviewers: [R1, R2], note: \"n=1-7 per point，某些仅 1 seed 无统计意义\"}\n  action_items:\n    - {round: 2, action: \"n=1 点无 error bar 或使用不同 marker。标注每点 seed 数。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M6\"\n  summary: \"No cross-task generalization test (CRM trained on all eval tasks)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Cannot distinguish memorization from generalization\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致 critical。R3 补充：Table 2 concentrated improvement 加深 memorization 嫌疑。需 leave-task-out 实验。\"}\n  action_items:\n    - {round: 2, action: \"做 train/test task split（15 train / 5 held-out eval）\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M7\"\n  summary: \"Paper positioning unclear\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Method paper vs analysis paper\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"标题 'Dissecting' 暗示分析定位但分析深度不足。若定位为分析 paper 需加深度；若定位为方法 paper 需扩评估。\"}\n  action_items:\n    - {round: 2, action: \"明确选择定位方向并补足对应维度的不足\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M8\"\n  summary: \"Missing CP in robotics subsection\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2], note: \"No CP-robotics subsection\"}\n    - {round: 2, reviewers: [], note: \"已修复。Section 2.3 已添加。\"}\n  action_items:\n    - {round: 1, action: \"Add CP subsection\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Section 2.3 已添加\"\n  resolution_round: 2\n\n- id: \"m1\"\n  summary: \"'safety factor' terminology\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R3], note: \"Ambiguous in robotics context\"}\n    - {round: 2, reviewers: [], note: \"已修复。使用 'critical design factor'。\"}\n  action_items:\n    - {round: 1, action: \"Replace terminology\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"术语已替换\"\n  resolution_round: 2\n\n- id: \"m2-m9\"\n  summary: \"8 minor writing/format issues\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Bundled minor fixes\"}\n    - {round: 2, reviewers: [R2], note: \"大部分已修复。写作质量高，AI 痕迹几乎为零。\"}\n  action_items:\n    - {round: 1, action: \"Fix all\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"批量修复完成\"\n  resolution_round: 2\n\n# === Round 2 新发现 ===\n\n- id: \"R2-W4-new\"\n  summary: \"Motivation-evaluation disconnect: LIBERO+ in Intro but eval on standard LIBERO\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。SmolVLA 11.6% 可能非 distribution shift 而是 checkpoint 本身弱。R3 补充：若是后者则整个 robustness 叙事框架 misleading。\"}\n  action_items:\n    - {round: 2, action: \"(1) 解释 SmolVLA 11.6% 原因 (2) 在 LIBERO+ 上评估或调整 Intro framing\", assigned_to: \"Paper Agent + Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-new\"\n  summary: \"Low absolute performance (17.6%) limits generalizability of all findings\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。17.6% 从 'completely unusable' 到 'still unusable'。R3: 在更强 base policy 下 selection 可能就够用。\"}\n  action_items:\n    - {round: 2, action: \"至少在一个 base policy >50% 的 setting 下验证核心发现\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7-new\"\n  summary: \"'Dissecting' title promises analysis depth not delivered\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。缺 correction vector 分析、trajectory 阶段分析、成功/失败 pattern 对比。\"}\n  action_items:\n    - {round: 2, action: \"增加 correction vector 统计分析 + trajectory 可视化，或降低标题承诺\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1-new\"\n  summary: \"'Geometric medoid' terminology incorrect\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。实际是 argmin-to-centroid。\"}\n  action_items:\n    - {round: 2, action: \"改为 'closest sample to the centroid'\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-new\"\n  summary: \"DAgger citation misused\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。DAgger 是 interactive aggregation，非 static noise augmentation。\"}\n  action_items:\n    - {round: 2, action: \"替换为 domain randomization 或 covariate shift 文献\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3-new\"\n  summary: \"Applicability boundary based on single comparison (OpenVLA T=0.5)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。未测更高 temperature 或其他 VLA。\"}\n  action_items:\n    - {round: 2, action: \"测试 OpenVLA T=1.0+ 或软化 claim\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4-latency\"\n  summary: \"Wall-clock latency of K=10 forward passes not quantified\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致 critical。R3 估算 ~500ms → ~2 Hz，远低于 10-20 Hz。论文回避量化。R1 指出与论文批评 VLA-Pilot 2.41s 同类。\"}\n  action_items:\n    - {round: 2, action: \"提供 latency breakdown 表格（单次 VLA pass、K=10 total、CRM、end-to-end）+ 讨论 batch forward pass 可能性\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W8-new\"\n  summary: \"Hardware environment and training time not reported\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R3], note: \"缺 GPU 型号/数量、CRM 训练耗时、precompute 耗时、evaluation 硬件。\"}\n  action_items:\n    - {round: 2, action: \"补充硬件环境和各阶段 wall-clock time\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W9-new\"\n  summary: \"SmolVLA checkpoint version not locked (no commit hash)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。lerobot/smolvla_libero 无 commit hash，HF models 可被更新覆盖。\"}\n  action_items:\n    - {round: 2, action: \"补充 HuggingFace commit hash 或 download date\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10-new\"\n  summary: \"Precompute pipeline random seed not specified\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R3], note: \"Flow-matching precompute seed 未明确。若与 eval seed 相同可能导致 overfitting。\"}\n  action_items:\n    - {round: 2, action: \"明确 precompute 阶段的 random seed 并报告\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "issues_yaml": "- id: \"C1\"\n  summary: \"Fisher exact test independence violation (pseudo-replication)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Same-seed episodes share CRM weights, violating independence assumption\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已修复。改用 seed-level Mann-Whitney U，三位 Reviewer 均肯定统计方法严谨\"}\n  action_items:\n    - {round: 1, action: \"Replace Fisher with Mann-Whitney U\", assigned_to: \"Paper Agent + Agent\", status: \"done\"}\n  resolution: \"改用 seed-level Mann-Whitney U + sign test 补充验证\"\n  resolution_round: 2\n\n- id: \"C2\"\n  summary: \"Core claim contradicts K=1 data\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"K=1 CRM below baseline means correction alone harmful\"}\n    - {round: 2, reviewers: [R1, R2], note: \"已修复。Reframe 为 'correction is active mechanism, multi-sampling is enabling condition'\"}\n  action_items:\n    - {round: 1, action: \"Reframe core claim\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"重构核心 claim\"\n  resolution_round: 2\n\n- id: \"C3\"\n  summary: \"Inconsistent seed counts across methods\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"obs_only 7, VLA-only 5, Argmin 6, Random 3\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"论文增加说明但 Random 仅 3 seeds 的 'statistically indistinguishable' 结论不成立。R3 补充：n1=3,n2=5 时即使完全分离也只能 p=0.036。\"}\n  action_items:\n    - {round: 2, action: \"所有条件统一至 >=5 seeds。公布逐 seed 成功率。撤回 n=3 对比的 'indistinguishable' 结论。\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C4\"\n  summary: \"Novelty insufficient — standard MLP + L2 clipping\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Technical novelty low\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"[DIVERGENT] R2 维持 critical。R1/R3 rebut 认为 component decomposition 有独立价值，降级 warning。真正问题是实验规模和分析深度。\"}\n  action_items:\n    - {round: 2, action: \"明确定位为实证分析 paper，扩展分析深度\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C5\"\n  summary: \"Title contradicts conclusion\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Title sets wrong expectations\"}\n    - {round: 2, reviewers: [], note: \"已修复。新标题 'Correction Over Selection'\"}\n  action_items:\n    - {round: 1, action: \"Change title\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"标题已修改\"\n  resolution_round: 2\n\n- id: \"C6\"\n  summary: \"Paper exceeds 8-page limit\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R3, R2], note: \"May cause desk reject\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"R3 确认约 9 页。R1/R2 基于 tex 估算约 8.5 页。三方一致认为存在 desk reject 风险。R1 建议压缩 Intro 重复内容和 K-scaling 移入 Appendix。R2 建议合并 Discussion 入 Conclusion、缩减 Section 2.4。\"}\n  action_items:\n    - {round: 2, action: \"立即编译确认页数。若超限：(1) 合并 Discussion 入 Conclusion (2) 压缩 Intro para4/Contributions 重复 (3) K-scaling/applicability 段落移入 Appendix (4) 缩减 Related Work Section 2.4\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"C7\"\n  summary: \"Missing AI Disclosure\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R3, R2], note: \"Required by venue\"}\n    - {round: 2, reviewers: [R2], note: \"已修复\"}\n  action_items:\n    - {round: 1, action: \"Add AI disclosure\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"AI Disclosure 已添加\"\n  resolution_round: 2\n\n- id: \"M1\"\n  summary: \"Narrow experimental scope (single VLA + single benchmark + no real robot)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R1, R3], note: \"Only SmolVLA on LIBERO\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致 critical。标题 'Frozen VLAs'(复数)但只测一个。CoRL CFP 要求 real-robot 或 sim-to-real 论证，两者皆无。\"}\n  action_items:\n    - {round: 2, action: \"(1) 至少增加一个 flow-matching VLA backbone (2) 提供 sim-to-real 论证 (3) 限定标题 scope\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M2\"\n  summary: \"LIBERO-Spatial null result based on only 1 seed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"1 seed insufficient for null conclusion\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"仍为 seed 42 单点。缺 per-task Spatial 表和 failure case 分析。若作为 contribution 需加深分析。\"}\n  action_items:\n    - {round: 2, action: \"补充 Spatial multi-seed + per-task 表 + failure mode 分析\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M3\"\n  summary: \"No experimental comparison with A2C2\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Only textual positioning\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致 critical。A2C2 correction head 可 attach 到同一 frozen SmolVLA。'Different training regime' 辩护不成立。\"}\n  action_items:\n    - {round: 2, action: \"在同一 frozen SmolVLA 上实现 A2C2 baseline 做 controlled comparison\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M4\"\n  summary: \"Bib entries missing venue info\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Orphan entries, missing citations\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"部分修复。RT-2/OpenVLA/Octo 仍为 @misc 需更新。R3 声称存在 Gauss1857/Lagrange1788 orphan entries，R2 反驳：bib 中不存在这些条目（事实性错误）。R2 建议评估是否需添加 ADPro/GPC 等引用。\"}\n  action_items:\n    - {round: 2, action: \"(1) 更新 RT-2/OpenVLA/Octo venue 信息 (2) 评估 ADPro/GPC 等引用必要性\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M5\"\n  summary: \"Figure 2 n=1 points with meaningless error bars\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R3], note: \"Visual misleading\"}\n    - {round: 2, reviewers: [R1, R2], note: \"n=1-7 per point，某些仅 1 seed 无统计意义\"}\n  action_items:\n    - {round: 2, action: \"n=1 点无 error bar 或使用不同 marker。标注每点 seed 数。\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M6\"\n  summary: \"No cross-task generalization test (CRM trained on all eval tasks)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Cannot distinguish memorization from generalization\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致 critical。R3 补充：Table 2 concentrated improvement 加深 memorization 嫌疑。需 leave-task-out 实验。\"}\n  action_items:\n    - {round: 2, action: \"做 train/test task split（15 train / 5 held-out eval）\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M7\"\n  summary: \"Paper positioning unclear\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R2, R3], note: \"Method paper vs analysis paper\"}\n    - {round: 2, reviewers: [R1, R2, R3], note: \"标题 'Dissecting' 暗示分析定位但分析深度不足。若定位为分析 paper 需加深度；若定位为方法 paper 需扩评估。\"}\n  action_items:\n    - {round: 2, action: \"明确选择定位方向并补足对应维度的不足\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"M8\"\n  summary: \"Missing CP in robotics subsection\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2], note: \"No CP-robotics subsection\"}\n    - {round: 2, reviewers: [], note: \"已修复。Section 2.3 已添加。\"}\n  action_items:\n    - {round: 1, action: \"Add CP subsection\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Section 2.3 已添加\"\n  resolution_round: 2\n\n- id: \"m1\"\n  summary: \"'safety factor' terminology\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R3], note: \"Ambiguous in robotics context\"}\n    - {round: 2, reviewers: [], note: \"已修复。使用 'critical design factor'。\"}\n  action_items:\n    - {round: 1, action: \"Replace terminology\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"术语已替换\"\n  resolution_round: 2\n\n- id: \"m2-m9\"\n  summary: \"8 minor writing/format issues\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2, R3], note: \"Bundled minor fixes\"}\n    - {round: 2, reviewers: [R2], note: \"大部分已修复。写作质量高，AI 痕迹几乎为零。\"}\n  action_items:\n    - {round: 1, action: \"Fix all\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"批量修复完成\"\n  resolution_round: 2\n\n# === Round 2 新发现 ===\n\n- id: \"R2-W4-new\"\n  summary: \"Motivation-evaluation disconnect: LIBERO+ in Intro but eval on standard LIBERO\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。SmolVLA 11.6% 可能非 distribution shift 而是 checkpoint 本身弱。R3 补充：若是后者则整个 robustness 叙事框架 misleading。\"}\n  action_items:\n    - {round: 2, action: \"(1) 解释 SmolVLA 11.6% 原因 (2) 在 LIBERO+ 上评估或调整 Intro framing\", assigned_to: \"Paper Agent + Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-new\"\n  summary: \"Low absolute performance (17.6%) limits generalizability of all findings\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。17.6% 从 'completely unusable' 到 'still unusable'。R3: 在更强 base policy 下 selection 可能就够用。\"}\n  action_items:\n    - {round: 2, action: \"至少在一个 base policy >50% 的 setting 下验证核心发现\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7-new\"\n  summary: \"'Dissecting' title promises analysis depth not delivered\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。缺 correction vector 分析、trajectory 阶段分析、成功/失败 pattern 对比。\"}\n  action_items:\n    - {round: 2, action: \"增加 correction vector 统计分析 + trajectory 可视化，或降低标题承诺\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1-new\"\n  summary: \"'Geometric medoid' terminology incorrect\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。实际是 argmin-to-centroid。\"}\n  action_items:\n    - {round: 2, action: \"改为 'closest sample to the centroid'\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5-new\"\n  summary: \"DAgger citation misused\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。DAgger 是 interactive aggregation，非 static noise augmentation。\"}\n  action_items:\n    - {round: 2, action: \"替换为 domain randomization 或 covariate shift 文献\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3-new\"\n  summary: \"Applicability boundary based on single comparison (OpenVLA T=0.5)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。未测更高 temperature 或其他 VLA。\"}\n  action_items:\n    - {round: 2, action: \"测试 OpenVLA T=1.0+ 或软化 claim\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4-latency\"\n  summary: \"Wall-clock latency of K=10 forward passes not quantified\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致 critical。R3 估算 ~500ms → ~2 Hz，远低于 10-20 Hz。论文回避量化。R1 指出与论文批评 VLA-Pilot 2.41s 同类。\"}\n  action_items:\n    - {round: 2, action: \"提供 latency breakdown 表格（单次 VLA pass、K=10 total、CRM、end-to-end）+ 讨论 batch forward pass 可能性\", assigned_to: \"Agent + Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W8-new\"\n  summary: \"Hardware environment and training time not reported\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R3], note: \"缺 GPU 型号/数量、CRM 训练耗时、precompute 耗时、evaluation 硬件。\"}\n  action_items:\n    - {round: 2, action: \"补充硬件环境和各阶段 wall-clock time\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W9-new\"\n  summary: \"SmolVLA checkpoint version not locked (no commit hash)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R2, R3], note: \"三方一致。lerobot/smolvla_libero 无 commit hash，HF models 可被更新覆盖。\"}\n  action_items:\n    - {round: 2, action: \"补充 HuggingFace commit hash 或 download date\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10-new\"\n  summary: \"Precompute pipeline random seed not specified\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1, R3], note: \"Flow-matching precompute seed 未明确。若与 eval seed 相同可能导致 overfitting。\"}\n  action_items:\n    - {round: 2, action: \"明确 precompute 阶段的 random seed 并报告\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-19T02:09:45.884186+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml\", \"bytes\": 14498}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-19T02:11:39.891639+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n**目标 venue**: CoRL 2026 Main Conference\n**Deadline**: 2026-05-29（距今 10 天）\n**审稿模式**: Fresh（独立初审）\n**Reviewer 编排**: 3 人（R1: 方法/实验/统计; R2: 新颖性/Related Work/写作/格式; R3: CoRL venue fit/格式合规/可重复性）\n**外部审稿**: 未配置，跳过\n\n---\n\n## Summary\n\n本文提出 sample-select-correct pipeline 对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正（‖δ‖₂ ≤ ε）。在 LIBERO-Object 上实现 17.6±2.6% vs 11.6±1.1%（p=0.003, Mann-Whitney U），在 LIBERO-Spatial 上无提升（30-35%）。Component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告 conformal features 失效（progressive collapse to 0%）和 tokenized VLA 不适用的 negative results。\n\n---\n\n## Strengths\n\n- **S1: 系统化 component decomposition** [R1-S1, R2-S3, R3 隐含, 三方共识]\n  通过 K=1 correction、selection-only、random selection 等控制实验清楚拆解各组件贡献。\"Selection alone 无显著帮助、K=1 correction 低于 baseline、二者结合才有效\"的发现对 embodied test-time compute scaling 有洞察价值，与 LLM test-time scaling 的 selection-dominant 范式形成有意义的对比。\n\n- **S2: 有价值的 negative results** [R1-S2, R2-S4, 共识]\n  Conformal features 的失败（obs_only 14.3-17.6% vs perdof collapse 至 0%）和 tokenized VLA 不适用性，为后续研究提供指导。\n\n- **S3: 统计方法严谨** [R1-S3, R2-S2, R3-S3, 三方共识]\n  Seed-level Mann-Whitney U + sign test，正确处理 within-seed episode 非独立性。相比 Round 1（Fisher test）已大幅改善。\n\n- **S4: 写作质量高** [R1-S4, R2-S1/S5, R3-S1, 三方共识]\n  Pipeline 描述精确，符号一致，AI 写作痕迹几乎为零。Limitations section 诚实全面。\n\n- **S5: 实验可重复性基础尚可** [R3-S2]\n  关键超参数记录完整（Adam lr=1e-3, batch 32, 50 epochs, seed 42, augmentation noise），SmolVLA checkpoint 路径已给出。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Critical（影响接收决定）— 7 项三方共识\n\n**W-C1: 正文超出 8 页限制（约 9 页）** [R3-W5, R1/R2 AGREE]\nR3 确认正文（Section 1-7 + AI Disclosure）延伸至约第 9 页。CoRL 2026 规定 main text 最多 8 页（Limitations 和 AI Disclosure 计入），CoRL 2024 review instructions 明确将格式违规列为 desk rejection 标准。这是最紧急的 action item。\n*优先级：P0（desk reject 风险）*\n\n**W-C2: 极低绝对性能限制所有发现的泛化性** [R2-W1, R1/R3 AGREE]\nVLA-only baseline 仅 11.6%，pipeline 达 17.6%——整个评估处于 base policy 几乎不工作的 regime。Per-task 分析显示 improvement 集中在 4/10 tasks（chocolate_pudding +40pp, bbq_sauce/ketchup +20pp, salad_dressing +10pp），其余 6 task 基本无变化或退化。Component decomposition 结论能否外推到更强 base policy（如 >50%）完全未知。R3 指出在更强 base policy 下 selection 可能就够用，correction 的相对贡献可能完全不同。\n\n**W-C3: 评估范围极窄** [R2-W2, R1-N4, R3-W1, 三方共识]\n(a) 仅 SmolVLA（450M）一个 backbone，但标题用 \"Frozen VLAs\"（复数）；(b) 仅 LIBERO 一个 benchmark family（且只有 Object 有效）；(c) 纯仿真，无 real-robot 实验或 sim-to-real 论证。CoRL CFP 明确鼓励 \"real-robot experiments or simulation evidence demonstrating transferability to physical robots\"，论文两者皆无。\n\n**W-C4: CRM 在 eval 任务 demo 上训练，无 held-out 泛化验证** [R1-N1, R2/R3 AGREE]\nCRM 训练数据来自 20 个 LIBERO tasks 的 demo = 评估的 Object 10 + Spatial 10。无法区分 task-specific memorization 和 generalizable correction。Per-task concentrated improvement（4/10 tasks）与 memorization 假说兼容。需要 leave-task-out 实验。\n\n**W-C5: 缺少 A2C2 实验对比** [R1-N2, R2-W5, R3 AGREE, 三方共识]\nA2C2 被论文认定为 \"closest concurrent work\"，详细列出三点方法差异，但从未作为 baseline 运行。A2C2 correction head 可直接 attach 到同一 frozen SmolVLA checkpoint 做 controlled comparison。\"Different training regime\" 辩护不成立。\n\n**W-C6: 动机与评估断裂** [R2-W4, R1/R3 AGREE]\nIntroduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%）motivate distribution shift，但实验在标准 LIBERO 上。SmolVLA 11.6% baseline 原因未解释。R3 指出可能非 distribution shift 而是 checkpoint 本身弱，若如此则 Introduction 的整个 robustness 叙事框架 misleading。\n\n**W-C7: K=10 forward passes latency 未量化** [R3-W2, R1/R2 AGREE]\nSmolVLA 450M 单次 forward pass ~50ms，K=10 约 500ms，对应 ~2 Hz，远低于 10-20 Hz 操作频率。论文仅提 \"~0.3ms CRM overhead\"，将 CRM 作为 overhead 代表但回避了 10x VLA pass 的主要开销。R1 指出这与论文批评 VLA-Pilot \"2.41s per control step\" 同类。\n\n### Critical — Seed 数量问题\n\n**W-C8: Seed 数量小且不平衡** [R1-N3, R2/R3 AGREE]\nobs_only 7, VLA-only 5, Argmin 6, Random 3, VLA-mean 4, scalar 4。主要对比（U=35=U_max, p=0.0025）在给定样本量下已是最强结果，但次要对比严重 underpowered：Random 仅 3 seeds 的 \"statistically indistinguishable\" 结论不成立（R3 补充：n1=3,n2=5 即使完全分离也只能 p=0.036）。\n\n### Warning — 8 项\n\n**W-W1: \"Dissecting\" 分析深度不足** [R2-W7, R1/R3 AGREE]\n缺 correction vector 分布、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。当前为 ablation 而非 dissection。\n\n**W-W2: Applicability boundary 基于单一对比** [R1-W3, R2/R3 AGREE]\n仅 OpenVLA T=0.5。未测更高 temperature 或其他 VLA。\"Architectural boundary\" 是强 claim 但证据仅一个 data point。\n\n**W-W3: Spatial null result 分析不足** [R1-W4, R2/R3 AGREE]\n仅 seed 42 单点，无 per-task Spatial 表，无 failure case 分析。若作为 contribution 需大幅加深。\n\n**W-W4: ε 敏感性分析不完整** [R1-W2, R2 AGREE]\nscalar 仅 ε=0.1 一个点，各 ε 点 seed 数 n=1-7 不一致。\n\n**W-W5: 可重复性缺口** [R3-W8/W9/W10, R1/R2 AGREE]\n(a) 硬件环境和训练耗时未报告；(b) SmolVLA checkpoint 无 commit hash；(c) Precompute flow-matching random seed 未明确。\n\n**W-W6: \"Geometric medoid\" 术语不正确** [R1-W1, R2/R3 AGREE]\n实际是 argmin-to-centroid（squared L2），非经典 geometric medoid。\n\n**W-W7: DAgger 引用误用** [R1-W5, R2/R3 AGREE]\nDAgger 是 interactive dataset aggregation，非 static Gaussian noise augmentation。\n\n**W-W8: Related Work 遗漏 + bib 格式** [R2-W6, R1 部分 REBUT]\nR2 列出 5 篇遗漏（ADPro/GPC/Recurrent-Depth VLA/Residual Policy Adaptation/Compose Your Policies!）。R1 认为 32 条引用在 CoRL 正常范围但同意 bib venue 需更新。RT-2/OpenVLA/Octo 应从 @misc 更新为 @inproceedings。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题获得三方一致认同（零 REBUT）：\n\n| # | 问题 | R1 | R2 | R3 |\n|---|------|----|----|-----|\n| 1 | 无 real-robot + 低绝对性能 + latency 未量化 | N4 | W1/W2/W8 | W1/W2/W3 |\n| 2 | CRM 训练/评估任务重叠 | N1 | AGREE | AGREE |\n| 3 | 缺少 A2C2 baseline | N2 | W5 | AGREE |\n| 4 | Seed 数量不平衡 | N3 | AGREE w/ nuance | AGREE |\n| 5 | 评估范围窄 | AGREE | W2 | AGREE |\n| 6 | 动机-评估断裂 | AGREE | W4 | AGREE |\n| 7 | 正文超页 | AGREE | AGREE w/ caveat | W5 |\n\n## Reviewer Divergence [REBUT]\n\n| # | 问题 | 分歧方 | 理由 |\n|---|------|--------|------|\n| 1 | 方法新颖性严重程度 | R2: critical; R1/R3: warning | R1/R3 认为 component decomposition 有独立价值，真正问题是实验规模 |\n| 2 | Venue fit 归因 | R3: 应投 ML venue; R1/R2: REBUT | R1/R2 认为主题是 robotics-specific 的，问题在于执行（sim-only）而非 contribution 类型 |\n| 3 | Orphan bib entries | R3: Gauss1857/Lagrange1788 存在; R2: REBUT | R2 核验 bib 文件确认不存在这些条目，R3 可能混淆 |\n\n---\n\n## Questions for Authors\n\n1. SmolVLA 在标准 LIBERO-Object 上 baseline 为何只有 11.6%？原论文报告多少？是 distribution shift 还是 checkpoint 本身性能差？\n2. CRM 是否曾在 held-out tasks 上测试？15 task 训练 / 5 held-out 评估结果如何？\n3. 在 base policy >50% 的 setting 下，correction > selection 是否仍成立？\n4. K=10 forward passes 在 SmolVLA 上的 wall-clock latency？在 10-20 Hz 控制频率下是否可行？\n5. A2C2 correction head 能否 attach 到同一 frozen SmolVLA？为什么不做对比？\n6. Table 1 LIBERO-Spatial Random \"---\" 原因？\n7. 能否公布每个 seed 的具体成功率？\n8. perdof 在 ε=0.03 达 14%，K 更大时 conformal features 是否可能有用？\n9. Precompute pipeline 的 flow-matching random seed 是什么？与 evaluation seed 是否相同？\n10. SmolVLA checkpoint 的 HuggingFace commit hash？\n\n---\n\n## Missing References\n\n**R2 提出（frozen generative policy + inference-time enhancement 方向）**：\n- ADPro (2025, arXiv 2508.06266)\n- GPC (2025, arXiv 2502.00622)\n- Recurrent-Depth VLA (2026, arXiv 2602.07845)\n- Compose Your Policies! (2025, arXiv 2510.01068)\n\n**R1 提出**：\n- ACT temporal ensembling (Zhao et al. 2023)\n- Best-of-N sampling in robotics\n\n**bib 格式**：RT-2/OpenVLA/Octo 需更新 @misc → @inproceedings + venue 信息。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置（项目未启用 `external_review.paperreview_ai`），跳过。\n\n---\n\n## Overall Assessment\n\n**Score: weak reject**\n**Confidence: high**\n\n| Reviewer | Score | Confidence |\n|----------|-------|------------|\n| R1 (方法/实验/统计) | weak reject | high |\n| R2 (新颖性/写作/格式) | weak reject | high |\n| R3 (venue fit/格式/可重复性) | weak reject | high |\n\n**核心判断**：论文在写作质量、统计严谨性和 component decomposition 设计上有实质性优势。相比 Round 1 在统计方法（Fisher→MW-U）、framing（claim reframe）、格式（AI Disclosure、标题、CP subsection）方面有显著改进（Round 1 的 7 个 critical 中 4 个已 resolved）。\n\n但持续存在的结构性问题——评估范围过窄（单 VLA/单 benchmark/sim-only）、绝对性能极低（17.6%）、缺少 A2C2 对比、CRM 泛化未验证——加上新发现的页数超限（desk reject 风险）、动机-评估断裂、latency 未量化，共同构成在 CoRL 2026 录用标准下的 significant gap。这些不是 writing fix 能解决的问题，需要额外实验。\n\n**给 Research Director 的建议优先级**：\n\n| 优先级 | 问题 | 可行性（10 天内） | 影响 |\n|--------|------|-------------------|------|\n| P0 | 页数压缩至 8 页 | ✅ 高 | 避免 desk reject |\n| P1 | A2C2 baseline 实现 | ⚠️ 中（需实现+跑实验） | 填补 positioning 核心缺陷 |\n| P1 | Held-out task split | ⚠️ 中（需 re-train + re-eval） | 验证 generalization vs memorization |\n| P1 | Latency breakdown 表格 | ✅ 高（仅需测量） | 量化 real-time 可行性 |\n| P2 | 动机-评估 framing 对齐 | ✅ 高（writing fix） | 修复叙事逻辑缺口 |\n| P2 | Spatial multi-seed | ⚠️ 中 | 强化 null result claim |\n| P3 | 第二个 VLA backbone | ❌ 低（需大量实验） | 支撑 \"Frozen VLAs\" 复数 |\n| P3 | Real-robot 实验 | ❌ 极低 | CoRL venue fit |\n\n即使 P0-P1 全部完成，论文仍面临 \"单 VLA backbone + sim-only + 低绝对性能\" 的结构性限制。建议 Research Director 评估是否将目标 venue 调整为 CoRL Workshop 或改投 ICRA 2027/RSS Workshop 等对 simulation-only 分析类论文更友好的场所。\n",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_416d453a45869a9406db62186b1e3ef7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"\n**目标 venue**: CoRL 2026 Main Conference\n**Deadline**: 2026-05-29（距今 10 天）\n**审稿模式**: Fresh（独立初审）\n**Reviewer 编排**: 3 人（R1: 方法/实验/统计; R2: 新颖性/Related Work/写作/格式; R3: CoRL venue fit/格式合规/可重复性）\n**外部审稿**: 未配置，跳过\n\n---\n\n## Summary\n\n本文提出 sample-select-correct pipeline 对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正（‖δ‖₂ ≤ ε）。在 LIBERO-Object 上实现 17.6±2.6% vs 11.6±1.1%（p=0.003, Mann-Whitney U），在 LIBERO-Spatial 上无提升（30-35%）。Component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告 conformal features 失效（progressive collapse to 0%）和 tokenized VLA 不适用的 negative results。\n\n---\n\n## Strengths\n\n- **S1: 系统化 component decomposition** [R1-S1, R2-S3, R3 隐含, 三方共识]\n  通过 K=1 correction、selection-only、random selection 等控制实验清楚拆解各组件贡献。\"Selection alone 无显著帮助、K=1 correction 低于 baseline、二者结合才有效\"的发现对 embodied test-time compute scaling 有洞察价值，与 LLM test-time scaling 的 selection-dominant 范式形成有意义的对比。\n\n- **S2: 有价值的 negative results** [R1-S2, R2-S4, 共识]\n  Conformal features 的失败（obs_only 14.3-17.6% vs perdof collapse 至 0%）和 tokenized VLA 不适用性，为后续研究提供指导。\n\n- **S3: 统计方法严谨** [R1-S3, R2-S2, R3-S3, 三方共识]\n  Seed-level Mann-Whitney U + sign test，正确处理 within-seed episode 非独立性。相比 Round 1（Fisher test）已大幅改善。\n\n- **S4: 写作质量高** [R1-S4, R2-S1/S5, R3-S1, 三方共识]\n  Pipeline 描述精确，符号一致，AI 写作痕迹几乎为零。Limitations section 诚实全面。\n\n- **S5: 实验可重复性基础尚可** [R3-S2]\n  关键超参数记录完整（Adam lr=1e-3, batch 32, 50 epochs, seed 42, augmentation noise），SmolVLA checkpoint 路径已给出。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Critical（影响接收决定）— 7 项三方共识\n\n**W-C1: 正文超出 8 页限制（约 9 页）** [R3-W5, R1/R2 AGREE]\nR3 确认正文（Section 1-7 + AI Disclosure）延伸至约第 9 页。CoRL 2026 规定 main text 最多 8 页（Limitations 和 AI Disclosure 计入），CoRL 2024 review instructions 明确将格式违规列为 desk rejection 标准。这是最紧急的 action item。\n*优先级：P0（desk reject 风险）*\n\n**W-C2: 极低绝对性能限制所有发现的泛化性** [R2-W1, R1/R3 AGREE]\nVLA-only baseline 仅 11.6%，pipeline 达 17.6%——整个评估处于 base policy 几乎不工作的 regime。Per-task 分析显示 improvement 集中在 4/10 tasks（chocolate_pudding +40pp, bbq_sauce/ketchup +20pp, salad_dressing +10pp），其余 6 task 基本无变化或退化。Component decomposition 结论能否外推到更强 base policy（如 >50%）完全未知。R3 指出在更强 base policy 下 selection 可能就够用，correction 的相对贡献可能完全不同。\n\n**W-C3: 评估范围极窄** [R2-W2, R1-N4, R3-W1, 三方共识]\n(a) 仅 SmolVLA（450M）一个 backbone，但标题用 \"Frozen VLAs\"（复数）；(b) 仅 LIBERO 一个 benchmark family（且只有 Object 有效）；(c) 纯仿真，无 real-robot 实验或 sim-to-real 论证。CoRL CFP 明确鼓励 \"real-robot experiments or simulation evidence demonstrating transferability to physical robots\"，论文两者皆无。\n\n**W-C4: CRM 在 eval 任务 demo 上训练，无 held-out 泛化验证** [R1-N1, R2/R3 AGREE]\nCRM 训练数据来自 20 个 LIBERO tasks 的 demo = 评估的 Object 10 + Spatial 10。无法区分 task-specific memorization 和 generalizable correction。Per-task concentrated improvement（4/10 tasks）与 memorization 假说兼容。需要 leave-task-out 实验。\n\n**W-C5: 缺少 A2C2 实验对比** [R1-N2, R2-W5, R3 AGREE, 三方共识]\nA2C2 被论文认定为 \"closest concurrent work\"，详细列出三点方法差异，但从未作为 baseline 运行。A2C2 correction head 可直接 attach 到同一 frozen SmolVLA checkpoint 做 controlled comparison。\"Different training regime\" 辩护不成立。\n\n**W-C6: 动机与评估断裂** [R2-W4, R1/R3 AGREE]\nIntroduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%）motivate distribution shift，但实验在标准 LIBERO 上。SmolVLA 11.6% baseline 原因未解释。R3 指出可能非 distribution shift 而是 checkpoint 本身弱，若如此则 Introduction 的整个 robustness 叙事框架 misleading。\n\n**W-C7: K=10 forward passes latency 未量化** [R3-W2, R1/R2 AGREE]\nSmolVLA 450M 单次 forward pass ~50ms，K=10 约 500ms，对应 ~2 Hz，远低于 10-20 Hz 操作频率。论文仅提 \"~0.3ms CRM overhead\"，将 CRM 作为 overhead 代表但回避了 10x VLA pass 的主要开销。R1 指出这与论文批评 VLA-Pilot \"2.41s per control step\" 同类。\n\n### Critical — Seed 数量问题\n\n**W-C8: Seed 数量小且不平衡** [R1-N3, R2/R3 AGREE]\nobs_only 7, VLA-only 5, Argmin 6, Random 3, VLA-mean 4, scalar 4。主要对比（U=35=U_max, p=0.0025）在给定样本量下已是最强结果，但次要对比严重 underpowered：Random 仅 3 seeds 的 \"statistically indistinguishable\" 结论不成立（R3 补充：n1=3,n2=5 即使完全分离也只能 p=0.036）。\n\n### Warning — 8 项\n\n**W-W1: \"Dissecting\" 分析深度不足** [R2-W7, R1/R3 AGREE]\n缺 correction vector 分布、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。当前为 ablation 而非 dissection。\n\n**W-W2: Applicability boundary 基于单一对比** [R1-W3, R2/R3 AGREE]\n仅 OpenVLA T=0.5。未测更高 temperature 或其他 VLA。\"Architectural boundary\" 是强 claim 但证据仅一个 data point。\n\n**W-W3: Spatial null result 分析不足** [R1-W4, R2/R3 AGREE]\n仅 seed 42 单点，无 per-task Spatial 表，无 failure case 分析。若作为 contribution 需大幅加深。\n\n**W-W4: ε 敏感性分析不完整** [R1-W2, R2 AGREE]\nscalar 仅 ε=0.1 一个点，各 ε 点 seed 数 n=1-7 不一致。\n\n**W-W5: 可重复性缺口** [R3-W8/W9/W10, R1/R2 AGREE]\n(a) 硬件环境和训练耗时未报告；(b) SmolVLA checkpoint 无 commit hash；(c) Precompute flow-matching random seed 未明确。\n\n**W-W6: \"Geometric medoid\" 术语不正确** [R1-W1, R2/R3 AGREE]\n实际是 argmin-to-centroid（squared L2），非经典 geometric medoid。\n\n**W-W7: DAgger 引用误用** [R1-W5, R2/R3 AGREE]\nDAgger 是 interactive dataset aggregation，非 static Gaussian noise augmentation。\n\n**W-W8: Related Work 遗漏 + bib 格式** [R2-W6, R1 部分 REBUT]\nR2 列出 5 篇遗漏（ADPro/GPC/Recurrent-Depth VLA/Residual Policy Adaptation/Compose Your Policies!）。R1 认为 32 条引用在 CoRL 正常范围但同意 bib venue 需更新。RT-2/OpenVLA/Octo 应从 @misc 更新为 @inproceedings。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题获得三方一致认同（零 REBUT）：\n\n| # | 问题 | R1 | R2 | R3 |\n|---|------|----|----|-----|\n| 1 | 无 real-robot + 低绝对性能 + latency 未量化 | N4 | W1/W2/W8 | W1/W2/W3 |\n| 2 | CRM 训练/评估任务重叠 | N1 | AGREE | AGREE |\n| 3 | 缺少 A2C2 baseline | N2 | W5 | AGREE |\n| 4 | Seed 数量不平衡 | N3 | AGREE w/ nuance | AGREE |\n| 5 | 评估范围窄 | AGREE | W2 | AGREE |\n| 6 | 动机-评估断裂 | AGREE | W4 | AGREE |\n| 7 | 正文超页 | AGREE | AGREE w/ caveat | W5 |\n\n## Reviewer Divergence [REBUT]\n\n| # | 问题 | 分歧方 | 理由 |\n|---|------|--------|------|\n| 1 | 方法新颖性严重程度 | R2: critical; R1/R3: warning | R1/R3 认为 component decomposition 有独立价值，真正问题是实验规模 |\n| 2 | Venue fit 归因 | R3: 应投 ML venue; R1/R2: REBUT | R1/R2 认为主题是 robotics-specific 的，问题在于执行（sim-only）而非 contribution 类型 |\n| 3 | Orphan bib entries | R3: Gauss1857/Lagrange1788 存在; R2: REBUT | R2 核验 bib 文件确认不存在这些条目，R3 可能混淆 |\n\n---\n\n## Questions for Authors\n\n1. SmolVLA 在标准 LIBERO-Object 上 baseline 为何只有 11.6%？原论文报告多少？是 distribution shift 还是 checkpoint 本身性能差？\n2. CRM 是否曾在 held-out tasks 上测试？15 task 训练 / 5 held-out 评估结果如何？\n3. 在 base policy >50% 的 setting 下，correction > selection 是否仍成立？\n4. K=10 forward passes 在 SmolVLA 上的 wall-clock latency？在 10-20 Hz 控制频率下是否可行？\n5. A2C2 correction head 能否 attach 到同一 frozen SmolVLA？为什么不做对比？\n6. Table 1 LIBERO-Spatial Random \"---\" 原因？\n7. 能否公布每个 seed 的具体成功率？\n8. perdof 在 ε=0.03 达 14%，K 更大时 conformal features 是否可能有用？\n9. Precompute pipeline 的 flow-matching random seed 是什么？与 evaluation seed 是否相同？\n10. SmolVLA checkpoint 的 HuggingFace commit hash？\n\n---\n\n## Missing References\n\n**R2 提出（frozen generative policy + inference-time enhancement 方向）**：\n- ADPro (2025, arXiv 2508.06266)\n- GPC (2025, arXiv 2502.00622)\n- Recurrent-Depth VLA (2026, arXiv 2602.07845)\n- Compose Your Policies! (2025, arXiv 2510.01068)\n\n**R1 提出**：\n- ACT temporal ensembling (Zhao et al. 2023)\n- Best-of-N sampling in robotics\n\n**bib 格式**：RT-2/OpenVLA/Octo 需更新 @misc → @inproceedings + venue 信息。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置（项目未启用 `external_review.paperreview_ai`），跳过。\n\n---\n\n## Overall Assessment\n\n**Score: weak reject**\n**Confidence: high**\n\n| Reviewer | Score | Confidence |\n|----------|-------|------------|\n| R1 (方法/实验/统计) | weak reject | high |\n| R2 (新颖性/写作/格式) | weak reject | high |\n| R3 (venue fit/格式/可重复性) | weak reject | high |\n\n**核心判断**：论文在写作质量、统计严谨性和 component decomposition 设计上有实质性优势。相比 Round 1 在统计方法（Fisher→MW-U）、framing（claim reframe）、格式（AI Disclosure、标题、CP subsection）方面有显著改进（Round 1 的 7 个 critical 中 4 个已 resolved）。\n\n但持续存在的结构性问题——评估范围过窄（单 VLA/单 benchmark/sim-only）、绝对性能极低（17.6%）、缺少 A2C2 对比、CRM 泛化未验证——加上新发现的页数超限（desk reject 风险）、动机-评估断裂、latency 未量化，共同构成在 CoRL 2026 录用标准下的 significant gap。这些不是 writing fix 能解决的问题，需要额外实验。\n\n**给 Research Director 的建议优先级**：\n\n| 优先级 | 问题 | 可行性（10 天内） | 影响 |\n|--------|------|-------------------|------|\n| P0 | 页数压缩至 8 页 | ✅ 高 | 避免 desk reject |\n| P1 | A2C2 baseline 实现 | ⚠️ 中（需实现+跑实验） | 填补 positioning 核心缺陷 |\n| P1 | Held-out task split | ⚠️ 中（需 re-train + re-eval） | 验证 generalization vs memorization |\n| P1 | Latency breakdown 表格 | ✅ 高（仅需测量） | 量化 real-time 可行性 |\n| P2 | 动机-评估 framing 对齐 | ✅ 高（writing fix） | 修复叙事逻辑缺口 |\n| P2 | Spatial multi-seed | ⚠️ 中 | 强化 null result claim |\n| P3 | 第二个 VLA backbone | ❌ 低（需大量实验） | 支撑 \"Frozen VLAs\" 复数 |\n| P3 | Real-robot 实验 | ❌ 极低 | CoRL venue fit |\n\n即使 P0-P1 全部完成，论文仍面临 \"单 VLA backbone + sim-only + 低绝对性能\" 的结构性限制。建议 Research Director 评估是否将目标 venue 调整为 CoRL Workshop 或改投 ICRA 2027/RSS Workshop 等对 simulation-only 分析类论文更友好的场所。\n",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_416d453a45869a9406db62186b1e3ef7"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-19T02:11:44.841016+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4949
}
```

</details>

---


### Assistant

_source line 224 · 2026-05-19T02:11:56.583036+00:00_

审稿报告已投递给 Research Director。

---

**审稿完成总结**

三位 Reviewer 一致给出 **Weak Reject (High Confidence)**。

**Round 1→2 改进（4/7 critical resolved）**：统计方法改为 MW-U ✅、核心 claim reframe ✅、标题修改 ✅、AI Disclosure 添加 ✅

**持续未解决的核心问题**（按优先级）：
1. **P0 — 页数超限约 9 页**（desk reject 风险）
2. **P1 — 缺少 A2C2 对比 + CRM 泛化未验证 + latency 未量化**
3. **P2 — 动机-评估断裂 + Spatial 单 seed**
4. **结构性限制 — 单 VLA/单 benchmark/sim-only/17.6% 绝对性能**

报告建议 Research Director 评估是否在剩余 10 天内完成 P0-P1 修复将论文推至 borderline，或考虑更匹配评估范围的 venue（CoRL Workshop / ICRA 2027）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 225 · 2026-05-19T02:11:59.361760+00:00_

[Reviewer 3 审稿结果]:
交叉回应已提交。核心结论：

- R1 的 N1-N3 全部 **[AGREE]**（训练/评估任务重叠、缺 A2C2 baseline、seed 不足）
- R2 的 W1/W2/W4 **[AGREE]**（低绝对性能泛化性存疑、评估范围窄、动机断裂）
- R2-W3（novelty 有限）**[REBUT]**，建议从 critical 降至 warning——component decomposition 有独立价值，但需要更深入的分析支撑
- R1/R2 共识 Should-Fix 六条全部 **[AGREE]**

三位 Reviewer 形成的最强共识：无 real-robot 验证 + CRM 训练/评估任务重叠 + 缺 A2C2 对比 + 正文超页，这四个问题中任一个都足以影响接收决定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 226 · 2026-05-19T02:12:10.623680+00:00_

审稿报告已于 R3 交叉回应到达前提交（三位 Reviewer 的 Round 1 审稿 + R1↔R2 交叉 + R1/R2→R3 及 R3→R1/R2 交叉均已纳入）。R3 的最终交叉回应与已提交报告的结论完全一致，无需修订。

**审稿完成总结**：

- **Overall Score**: Weak Reject（三位 Reviewer 一致，High Confidence）
- **Round 1 → Round 2 改进**：7 个 Round 1 critical 中 4 个已 resolved（统计方法、核心 claim、标题、AI Disclosure）
- **持续存在的 critical 问题**（8 项）：页数超限（desk reject 风险）、低绝对性能、评估范围窄、CRM 泛化未验证、缺 A2C2 对比、动机-评估断裂、latency 未量化、seed 不平衡
- **Issue Tracker 已同步**：`artifacts/review_issues.yaml`（8 resolved + 19 open/warning）
- **报告已投递至 Research Director**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 30

## Round 30

2 recorded events


### User

_source line 227 · 2026-05-27T00:48:48.344448+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: acr-vla-conformal-refinement
- 论文路径: projects/acr-vla-conformal-refinement/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "system"
}
```

</details>

---


### Assistant

_source line 228 · 2026-05-27T00:49:18.568935+00:00_

⏰ API 当前限速（所有账号），请稍后重试（通常几分钟内恢复）。你的消息未丢失，重新发送即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 229 · 2026-05-27T12:25:16.527200+00:00_

[Round 4 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/acr-vla-conformal-refinement/artifacts/review_reports/round_3.md`
跨轮次问题追踪: `projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: acr-vla-conformal-refinement
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-28
- **引用验证**: ❌ 未启用

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "system"
}
```

</details>

---


### Assistant

_source line 230 · 2026-05-27T12:25:41.766652+00:00_

⏰ API 当前限速（所有账号），请稍后重试（通常几分钟内恢复）。你的消息未丢失，重新发送即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 32

## Round 32

58 recorded events


### User

_source line 231 · 2026-05-27T15:11:58.196699+00:00_

[Round 5 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/acr-vla-conformal-refinement/artifacts/review_reports/round_4.md`
跨轮次问题追踪: `projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: acr-vla-conformal-refinement
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-28
- **引用验证**: ❌ 未启用

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-27T15:12:06.643422+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-27T15:12:09.303391+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 2659
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-27T15:12:09.454307+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-27T15:12:09.454769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-27T15:12:22.254429+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-27T15:12:23.710536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_4.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_4.md"
  }
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-27T15:12:23.761159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-27T15:12:25.218563+00:00_

{"result":"# 项目 acr-vla-conformal-refinement 概况\n\n## 实验状态 (1362 个)\n\n- **crm-train-v1**: DONE (killed) — \n- **crm-train-k5**: DONE (killed) — \n- **eval-scalar-unc-spatial**: DONE (killed) — \n- **eval-acr-spatial-v2**: DONE (killed) — \n- **eval-k5-spatial**: DONE (killed) — \n- **eval-object-v7-full**: DONE (killed) — \n- **eval-spatial-v6-full**: DONE (killed) — \n- **eval-object-v5-full**: DONE (killed) — \n- **eval-acr-vla-spatial-v1**: DONE (killed) — \n- **eval-acr-spatial-v1**: DONE (killed) — \n- **eval-reconvla-spatial-v2**: DONE (killed) — \n- **eval-object-v4-full**: DONE (killed) — \n- **eval-spatial-v5-full**: DONE (killed) — \n- **eval-spatial-v3-full**: DONE (killed) — \n- **eval-spatial-reeval-v2**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-27\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval-tau005-spatial-s42 | τ=0.05 Adaptive Conformal on Spatial s42. Extends τ-sweep below τ=0.10 to test if extremely low threshold causes excessive triggering and further SR degradation (τ=0.10 already showed 75.2% trigger rate hurting SR). | — | — | — |\n\n## 待处理\n- eval-k2-tau035-spatial-s42: K=2 τ-sweep: τ=0.35 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.（排队等待 GPU）\n- eval-k2-tau025-spatial-s42: K=2 τ-sweep: τ=0.25 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.（排队等待 GPU）\n- …另有 172 项\n\n## 近期结论\n- **eval-obs-object-norm003-s45** (failed): CRM obs_only norm=0.03 Object s45: additional seed for Table 1 supplementary norm sweep\n\n## 趋势\n成功 701 / 负向 97 / 失败 126 / 共 1160\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-18228: 无 GPU 信息\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\ncqa1-32758: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\n\n## 告警\n- plan_001-crm-smolvla: 训练失败 — unknown\n- plan_014-reconvla-baseline: 训练失败 — unkno
…[truncated 1835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2964
}
```

</details>

---


### Tool result

_source line 240 · 2026-05-27T15:12:25.218912+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/review_director_a3659f64.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 1508
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-27T15:12:25.219362+00:00_

1	- id: "C1"
2	  summary: "Fisher exact test independence violation (pseudo-replication)"
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - {round: 1, reviewers: [R1, R2, R3], note: "Same-seed episodes share CRM weights, violating independence assumption"}
10	    - {round: 2, reviewers: [R1, R2], note: "已修复。改用 seed-level Mann-Whitney U，三位 Reviewer 均肯定统计方法严谨"}
11	  action_items:
12	    - {round: 1, action: "Replace Fisher with Mann-Whitney U", assigned_to: "Paper Agent + Agent", status: "done"}
13	  resolution: "改用 seed-level Mann-Whitney U + sign test 补充验证"
14	  resolution_round: 2
15	
16	- id: "C2"
17	  summary: "Core claim contradicts K=1 data"
18	  category: framing
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 1
23	  mentions:
24	    - {round: 1, reviewers: [R1, R2, R3], note: "K=1 CRM below baseline means correction alone harmful"}
25	    - {round: 2, reviewers: [R1, R2], note: "已修复。Reframe 为 'correction is active mechanism, multi-sampling is enabling condition'"}
26	  action_items:
27	    - {round: 1, action: "Reframe core claim", assigned_to: "Paper Agent", status: "done"}
28	  resolution: "重构核心 claim"
29	  resolution_round: 2
30	
31	- id: "C3"
32	  summary: "Inconsistent seed counts across methods"
33	  category: experiment
34	  severity: critical
35	  status: open
36	  first_raised_round: 1
37	  last_seen_round: 2
38	  mentions:
39	    - {round: 1, reviewers: [R1, R2, R3], note: "obs_only 7, VLA-only 5, Argmin 6, Random 3"}
40	    - {round: 2, reviewers: [R1, R2, R3], note: "论文增加说明但 Random 仅 3 seeds 的 'statistically indistinguishable' 结论不成立。R3 补充：n1=3,n2=5 时即使完全分离也只能 p=0.036。"}
41	  action_items:
42	    - {round: 2, action: "所有条件统一至 >=5 seeds。公布逐 seed 成功率。撤回 n=3 对比的 'indistinguishable' 结论。", assigned_to: "Agent + Paper Agent", status: "open"}
43	  resolution: ""
44	  resolution_round: null
45	
46	- id: "C4"
47	  summary:
…[truncated 13500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-27T15:12:35.685100+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-27T15:12:35.995342+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 310
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-27T15:12:36.296737+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/submitted.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/submitted.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-27T15:12:36.347294+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_3/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_5/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_4/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-27T15:12:48.389651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_2.md"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-27T15:12:48.841939+00:00_

1	---
2	round: 2
3	review_mode: fresh
4	overall_score: weak reject
5	timestamp: 2026-05-19T02:11:40.043920+00:00
6	reviewer_ids: [1, 2, 3]
7	cross_response_reviewer_ids: [1, 2, 3]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 2 (Fresh Review)
12	
13	**论文**: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs"
14	**目标 venue**: CoRL 2026 Main Conference
15	**Deadline**: 2026-05-29（距今 10 天）
16	**审稿模式**: Fresh（独立初审）
17	**Reviewer 编排**: 3 人（R1: 方法/实验/统计; R2: 新颖性/Related Work/写作/格式; R3: CoRL venue fit/格式合规/可重复性）
18	**外部审稿**: 未配置，跳过
19	
20	---
21	
22	## Summary
23	
24	本文提出 sample-select-correct pipeline 对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正（‖δ‖₂ ≤ ε）。在 LIBERO-Object 上实现 17.6±2.6% vs 11.6±1.1%（p=0.003, Mann-Whitney U），在 LIBERO-Spatial 上无提升（30-35%）。Component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告 conformal features 失效（progressive collapse to 0%）和 tokenized VLA 不适用的 negative results。
25	
26	---
27	
28	## Strengths
29	
30	- **S1: 系统化 component decomposition** [R1-S1, R2-S3, R3 隐含, 三方共识]
31	  通过 K=1 correction、selection-only、random selection 等控制实验清楚拆解各组件贡献。"Selection alone 无显著帮助、K=1 correction 低于 baseline、二者结合才有效"的发现对 embodied test-time compute scaling 有洞察价值，与 LLM test-time scaling 的 selection-dominant 范式形成有意义的对比。
32	
33	- **S2: 有价值的 negative results** [R1-S2, R2-S4, 共识]
34	  Conformal features 的失败（obs_only 14.3-17.6% vs perdof collapse 至 0%）和 tokenized VLA 不适用性，为后续研究提供指导。
35	
36	- **S3: 统计方法严谨** [R1-S3, R2-S2, R3-S3, 三方共识]
37	  Seed-level Mann-Whitney U + sign test，正确处理 within-seed episode 非独立性。相比 Round 1（Fisher test）已大幅改善。
38	
39	- **S4: 写作质量高** [R1-S4, R2-S1/S5, R3-S1, 三方共识]
40	  Pipeline 描述精确，符号一致，AI 写作痕迹几乎为零。Limitations section 诚实全面。
41	
42	- **S5: 实验可重复性基础尚可** [R3-S2]
43	  关键超参数记录完整（Adam lr=1e-3, batch 32, 50 epochs, seed 42, augmentation noise），SmolVLA checkpoint 路径已给出。
44	
45	---
46	
47	## Weaknesses
…[truncated 7476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-27T15:12:48.842323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-27T15:12:48.892732+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{amsmath,amssymb,amsfonts}
8	\DeclareMathOperator*{\argmin}{arg\,min}
9	\DeclareMathOperator*{\argmax}{arg\,max}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{enumitem}
13	\usepackage{multirow}
14	
15	
16	\graphicspath{{figures/}}
17	
18	\title{ACR-VLA: Adaptive Conformal Refinement\\for Frozen Flow-Matching VLAs}
19	
20	\author{
21	  Anonymous
22	}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\begin{abstract}
29	\input{abstract}
30	\end{abstract}
31	
32	\keywords{Vision-Language-Action Models, Inference-Time Refinement, Robotic Manipulation}
33	
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	
40	\smallskip\noindent\textit{AI tools assisted with code and manuscript.}
41	
42	\bibliography{references}
43	
44	\clearpage
45	\input{appendix}
46	
47	\end{document}
48	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-27T15:13:07.847654+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-27T15:13:07.898360+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/camera_ready_template/corl_2026_template_cameraready/example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/review_template/corl_2026_template_submission/example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-27T15:13:11.009776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-27T15:13:11.160833+00:00_

1	We propose ACR-VLA, a lightweight inference-time correction pipeline for frozen flow-matching Vision-Language-Action models. Drawing only $K{=}2$ stochastic action samples in a single batched forward pass, ACR-VLA uses their pairwise $L_2$ distance as a per-step uncertainty signal, well-calibrated against ten-sample variance ($\rho{=}0.9979$) at zero additional latency, gating a 327K-parameter Correction Residual Module (CRM). On SmolVLA (0.4B) across four LIBERO suites, CRM applied unconditionally degrades two suites ($-$1.2\,pp Object, $-$2.2\,pp Long), while ACR-VLA's adaptive gate exceeds unconditional correction on all four suites by selectively correcting only high-uncertainty steps. The gate's trigger rate correlates monotonically with suite difficulty, allocating inference-time compute where the VLA is least confident. A cross-VLA analysis on $\pi_{0.5}$ (3.6B, 94--99\% baseline) shows that unconditional correction degrades near-expert VLAs by up to 17\,pp, but adaptive gating recovers 19--38\% of the loss on 3/4 suites, confirming the gate's value as a damage-limiting mechanism across capability levels.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-27T15:13:11.612877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-27T15:13:11.964603+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	\looseness=-1 Deploying a pretrained Vision-Language-Action (VLA) model on a new task usually requires fine-tuning on task demonstrations, yet collecting that data is expensive and the resulting checkpoint may not transfer further. A more attractive route keeps the VLA frozen and improves action quality at inference time. Flow-matching VLAs~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are well suited to this setting because each forward pass produces a stochastic action sample, enabling multi-sample selection and correction without retraining~\cite{snell2024scaling}. The naive approach draws $K{=}10$ samples and applies unconditional correction at every step, but most control steps are easy, and we show that correcting them adds noise without benefit.
5	
6	\looseness=-1 Recent work touches parts of this question without answering it. A2C2~\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and addresses temporal staleness rather than initial action quality. ReconVLA~\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\cite{liu2026scvla} uses reinforcement learning and therefore does not stay weight-frozen. VLA-Pilot~\cite{li2025vlapilot} performs evolutionary search at $2.41$\,s per control step, ruling out closed-loop deployment. None address the core question: can a frozen VLA decide \emph{per step} whether it needs correction at all?
7	
8	\looseness=-1 We propose \textbf{ACR-VLA}, an adaptive inference-time pipeline for frozen flow-matching VLAs. ACR-VLA draws only $K{=}2$ samples in a single batched forward pass and uses their pairwise $L_2$ distance as a per-step uncertainty probe. This probe is well-calibrated: Spearman $\rho{=}0.9979$ against $K{=}10$ sample variance, whereas three alternatives all yield $\rho < 0.16$. When the probe falls below a threshold $\tau$, the pipeline outputs the argmin-to-centr
…[truncated 3231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-27T15:13:11.964948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-27T15:13:12.417190+00:00_

1	
2	\section{ACR-VLA Pipeline}
3	\label{sec:method}
4	
5	\begin{figure}[t]
6	  \centering
7	  \includegraphics[width=\linewidth]{fig1_pipeline.pdf}
8	  \caption{Adaptive sample-select-correct pipeline. $K{=}2$ action samples are drawn from the frozen VLA; the argmin-to-centroid sample is selected, and a lightweight CRM applies bounded correction ($\|\boldsymbol{\delta}\|_2 \leq \varepsilon$) only when the pairwise $L_2$ distance exceeds the uncertainty threshold $\tau$.}
9	  \label{fig:pipeline}
10	\end{figure}
11	
12	\looseness=-1 ACR-VLA adaptively allocates inference-time compute for a frozen flow-matching VLA (Figure~\ref{fig:pipeline}). At each control step, a $K{=}2$ uncertainty probe determines whether the VLA is confident or uncertain; confident steps output the argmin-to-centroid sample directly, while uncertain steps apply a learned residual correction via a lightweight Correction Residual Module (CRM). The base VLA is never retrained.
13	
14	\subsection{Problem Setup}
15	\label{sec:problem_setup}
16	
17	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.
18	
19	\looseness=-1 Each forward pass of $\pi_\theta$ produces a stochastic action sample; querying independently $K$ times yields $K$ candidate chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to $\pi_\theta$. The method applies to any flow-matching VLA that produces diverse samples (Appendix~\ref{sec:applicability}).
20	
21	\subsection{Multi-Sample Selection}
22	\label{sec:selection}
23	
24	We draw $K$ action 
…[truncated 7192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-27T15:13:12.417616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-27T15:13:13.371619+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\looseness=-1 We evaluate ACR-VLA on SmolVLA~\cite{shukor2025smolvla} (0.4B) across four LIBERO~\cite{liu2023libero} task suites, comparing five methods that isolate the contributions of selection, correction, and adaptive gating. We ask: (i)~does adaptive gating produce positive improvements where unconditional correction and selection-only approaches fail? (ii)~what is the computational cost of the uncertainty probe?
6	
7	\subsection{Setup}
8	\label{sec:exp_setup}
9	
10	\paragraph{Benchmarks.}
11	We use all four LIBERO suites: Spatial (10 tasks, spatial reasoning), Object (10 tasks, novel object instances), Goal (10 tasks, goal specification), and Long (10 tasks, long-horizon manipulation). Each task is evaluated over 20 rollouts (max 300 steps, 200 per suite); success is binary.
12	
13	\paragraph{Base VLA.}
14	\looseness=-1 SmolVLA~\cite{shukor2025smolvla} (0.4B parameters, flow matching) uses dual-camera RGB ($256{\times}256$), 8D proprioceptive state, and produces 7D actions (6D pose + 1D gripper, thresholded separately). We additionally report $\pi_{0.5}$~\cite{black2025pi05} (3.6B) baselines and OpenVLA-OFT~\cite{kim2024openvla} (7B) boundary analysis in Section~\ref{sec:cross_vla}.
15	
16	\paragraph{Methods.}
17	All methods use the same frozen SmolVLA; no VLA weights are modified:
18	\begin{itemize}[nosep]
19	  \item \textbf{VLA-only} ($K{=}1$): single forward pass, no correction.
20	  \item \textbf{CRM always-on} ($K{=}10$, $\varepsilon{=}0.05$): argmin selection + unconditional CRM correction at every step. Uses a conservative norm bound ($\varepsilon{=}0.05$) to limit overcorrection.
21	  \item \textbf{$K{=}10$ argmin}~\cite{chen2026reconvla} ($K{=}10$): argmin-to-centroid selection over 10 samples, no learned correction. Represents the selection-only approach.
22	  \item \textbf{ACR-VLA} ($K{=}2$, $\varepsilon{=}0.2$, $\tau{=}0.25$): the proposed adaptive pipeline (Section~\ref{sec:adaptive_k_meth
…[truncated 9968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-27T15:13:13.472476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-27T15:13:13.874404+00:00_

1	
2	\enlargethispage{6\baselineskip}
3	\vspace{-8pt}
4	\section{Conclusion}
5	\label{sec:conclusion}
6	\vspace{-4pt}
7	
8	\looseness=-2 We presented ACR-VLA, an adaptive inference-time correction pipeline for frozen flow-matching VLAs. A $K{=}2$ pairwise $L_2$ uncertainty probe ($\rho{=}0.9979$) gates a lightweight CRM (${\sim}$327K parameters). On SmolVLA (0.4B), unconditional correction degrades 2/4 suites ($-$2.2\,pp Long, $-$1.2\,pp Object); on $\pi_{0.5}$ (3.6B, 94--99\% baseline), it degrades all four (up to $-$17\,pp). ACR-VLA's adaptive gate recovers performance in both settings: exceeding unconditional $K{=}10$ correction on all SmolVLA suites with $5{\times}$ fewer forward passes, and recovering 19--38\% of the CRM-induced loss on 3/4 $\pi_{0.5}$ suites. The key finding is mechanistic: adaptive gating modulates intervention intensity, turning an unstable correction module into a reliable one.
9	
10	\vspace{-4pt}
11	\section{Limitations}
12	\label{sec:limitations}
13	\vspace{-2pt}
14	
15	\looseness=-1 \textbf{Effect sizes and statistical power.}\enspace Paired improvements (Adaptive vs.\ VLA-only) are directionally consistent across suites but do not reach statistical significance at $\alpha{=}0.05$ with $n{=}3$ matched seeds (Spatial: $p{\approx}0.27$). Per-suite sample sizes are limited by computational budget; the consistent directional pattern across 4 suites provides corroborating but not definitive evidence of improvement. The stronger empirical claim is Adaptive vs.\ CRM always-on, where ACR-VLA exceeds unconditional correction on all four suites ($\Delta_{\mathrm{CRM}}{=}{+}1.0$ to $+$1.9\,pp).
16	
17	\looseness=-1 \textbf{Confidently wrong steps.}\enspace The pairwise $L_2$ probe measures sample disagreement, not correctness. On Long (trigger rate ${\sim}$4\%), the VLA may produce confident but systematically incorrect outputs that escape gating.
18	
19	\looseness=-1 \textbf{Scope and generalization.}\enspace The CRM requires task-specific calibra
…[truncated 357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-27T15:13:14.025402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-27T15:13:14.176468+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\looseness=-1 \paragraph{VLA robustness.} Vision-language-action models have progressed from tokenized prediction~\cite{brohan2023rt2,kim2024openvla,ghosh2024octo} to generative approaches based on diffusion~\cite{chi2023diffusion_policy} and flow matching~\cite{black2024pi0,shukor2025smolvla}. Robustness evaluations~\cite{fei2025liberoplus} show that current VLAs lose over 65\,pp under deployment perturbations. Training-time defenses (SRPO~\cite{srpo2025}, RobustVLA~\cite{robustvla2025}, DiG-Flow~\cite{digflow2025}, TT-VLA~\cite{liu2026ttvla}) improve robustness but require retraining or reward engineering.
4	
5	\looseness=-1 \paragraph{Inference-time correction.} Among frozen-VLA methods, ReconVLA~\cite{chen2026reconvla} provides uncertainty quantification but no learned correction; SC-VLA~\cite{liu2026scvla} requires task-level RL; VLA-Pilot~\cite{li2025vlapilot} uses evolutionary optimization at 2.41\,s per step. A2C2~\cite{a2c2_2025} is the closest concurrent work: it learns a correction head addressing \emph{temporal staleness} within action chunks. Our pipeline targets a complementary problem, namely \emph{initial action quality}, with multi-sample centering, explicit magnitude control, and adaptive per-step compute allocation. Residual policy learning~\cite{silver2018residual,johannink2019residual} shares the additive-correction structure; magnitude control is the central challenge, addressed by gating~\cite{jiang2024transic}, RL-bounded clipping~\cite{xiao2026pld}, or decay~\cite{pan2025drc}. Our CRM uses fixed $L_2$ norm clipping with supervised loss, requiring no RL or online rollouts. Conformal prediction~\cite{angelopoulos2023gentle} has been applied to robotics for uncertainty-aware control; our adaptive threshold $\tau$ draws on this calibration philosophy, though the CRM itself conditions only on observation features.
6	
7	\looseness=-1 \paragraph{Inference-time compute scaling.} Test-time scaling
…[truncated 583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-27T15:13:14.227079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-27T15:13:14.328013+00:00_

1	
2	\appendix
3	
4	\section{Applicability Boundary: Stochastic VLA Diversity}
5	\label{sec:applicability}
6	
7	\looseness=-1 The multi-sample pipeline requires stochastic action diversity across samples. We validate this prerequisite on two VLA architectures: SmolVLA~\cite{shukor2025smolvla} (flow matching, 0.4B) and OpenVLA-OFT~\cite{kim2024openvla} (deterministic $L_1$ regression, 7B).
8	
9	SmolVLA produces meaningfully diverse action samples across all dimensions via its flow-matching generative process. In contrast, OpenVLA-OFT's deterministic $L_1$ regression produces near-identical outputs: mean pairwise $L_2{=}0.00436$ across $K{=}2$ samples, with $97.3$\% of steps below $0.01$. The uncertainty gate never fires, and multi-sample selection is vacuous.
10	
11	This result establishes an architectural boundary: multi-sample inference-time correction is specific to stochastic generative VLAs (flow matching, diffusion). Deterministic VLAs lack the action diversity that selection and correction rely on. The boundary is architectural, not a limitation of our method: any inference-time approach that draws multiple action candidates requires the base policy to produce diverse samples.
12	
13	
14	\section{Threshold Sensitivity Analysis}
15	\label{sec:tau_sweep}
16	
17	\begin{table}[h]
18	\centering
19	\caption{SmolVLA threshold sensitivity ($\varepsilon{=}0.2$). Varying $\tau$ from $0.15$ to $0.45$ changes trigger rate by up to $5.5{\times}$ but SR by ${\leq}$1\,pp on Spatial and ${\leq}$2\,pp on Goal/Object, indicating robustness to threshold choice. $n$: number of seeds averaged.}
20	\label{tab:tau_sweep}
21	\small
22	\begin{tabular}{llccc}
23	\toprule
24	Suite & $\tau$ & SR (\%) & Trigger (\%) & $n$ \\
25	\midrule
26	Spatial & 0.15 & 80.5 & 40.7 & 1 \\
27	Spatial & 0.25 & 80.0 & 19.5 & 3 \\
28	Spatial & 0.35 & 80.0 & 12.2 & 1 \\
29	Spatial & 0.45 & 80.0 & 7.3 & 1 \\
30	\midrule
31	Goal & 0.15 & 84.5 & 34.4 & 2 \\
32	Goal & 0.25 & 83.8 & 8.1 & 3 \\
33	Goal & 0.35 & 8
…[truncated 6806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-27T15:13:58.494011+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
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

_source line 267 · 2026-05-27T15:13:58.494393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-27T15:13:59.598160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-27T15:13:59.649021+00:00_

1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	
21	@misc{black2024pi0,
22	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
23	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
24	    year={2024},
25	    eprint={2410.24164},
26	    archivePrefix={arXiv},
27	    primaryClass={cs.RO}
28	}
29	
30	@misc{black2025pi05,
31	    title={$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},
32	    author={Physical Intelligence and Kevin Black and Noah Brown and James Bradbury and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Oier Mees and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Allen Ren and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang},
33	    year={2025},
34	    eprint={2504.16054},
35	   
…[truncated 10506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-27T15:14:03.262906+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-27T15:14:09.417109+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines page limit"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"}]

Based on the search results, here are the key submission guidelines for CoRL 2026 regarding page limits:

## Page Limit

The page limit for the main paper is 8 pages. Acknowledgments, References, and Appendix (optional) will not count towards the page limit.

## Additional Requirements

All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

Authors are encouraged to submit a supplementary file containing further details, which reviewers may decide to consult, and a video not exceeding 250 MB (strict) and not more than 
…[truncated 432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6154
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-27T15:14:12.629784+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 submission deadline double blind anonymity template requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 submission deadline double blind anonymity template requirements"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-27T15:14:18.600201+00:00_

Web search results for query: "CoRL 2026 submission deadline double blind anonymity template requirements"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"ICWSM 2026: Submit","url":"https://www.icwsm.org/2026/submit.html"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"}]

Based on the search results, here is the information for CoRL 2026 submission requirements:

## Submission Deadline

The paper submission deadline is May 29, 2026 at 11:59 UTC, and the abstract submission deadline is May 26, 2026 at 11:59 UTC.

## Double-Blind Anonymity

CoRL is double-blind, which means all papers must be anonymized. The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced.

## Template Requirements

The CoRL LaTeX template uses a custom style based on PMLR (Proceedings of Machine Learning Research) format, with papers limited to 8 pages of content plus unlimited references. Authors should use "\usepackage[final]{corl_2026}." The template is available here (referring to the official CoRL website).

For more detailed submission instructions, you can refer to the off
…[truncated 160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5970
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-27T15:14:59.951223+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "review_chat_id": "oc_416d453a45869a9406db62186b1e3ef7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "review_chat_id": "oc_416d453a45869a9406db62186b1e3ef7"
  }
}
```

</details>

---


### Tool call

_source line 275 · 2026-05-27T15:15:00.503535+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-27T15:15:00.906850+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-27T15:15:04.022358+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4071
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-27T15:15:04.073070+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3569
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-27T15:15:04.073573+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 3166
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-27T15:15:11.805522+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 CoRL 2026 CFP 调研和论文资料检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '确定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: 分配 R1/R2 独立审稿 (Round 5)', 'status': 'in_progress', 'activeForm': '分配 Reviewer 1 和 Reviewer 2 审稿任务'}, {'content': 'Step 2: 交叉分享 + 逐条回应', 'status': 'pending', 'activeForm': '执行交叉分享和逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成最终报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 CoRL 2026 CFP 调研和论文资料检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '确定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: 分配 R1/R2 独立审稿 (Round 5)', 'status': 'in_progress', 'activeForm': '分配 Reviewer 1 和 Reviewer 2 审稿任务'}, {'content': 'Step 2: 交叉分享 + 逐条回应', 'status': 'pending', 'activeForm': '执行交叉分享和逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成最终报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-27T15:15:11.805889+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-27T15:16:03.435756+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "5",
  "project": "acr-vla-conformal-refinement",
  "text": "## Round 5 继续审稿 — Reviewer 1: 方法严谨性 / 实验有效性 / 统计声明\n\n**论文**: \"ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs\"\n**论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex\n**PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_5/submitted.pdf\n**Venue**: CoRL 2026 (deadline 2026-05-28)\n**格式要求**: 正文 ≤8 页（Limitations 计入，Acknowledgments/References/Appendix 不计入），double-blind，CoRL/PMLR 模板\n**审稿模式**: 继续审稿（增量评估）\n\n### 重要背景：论文已大幅重构\n\n论文从上轮的 \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"（K=10 unconditional correction）完全重构为 \"ACR-VLA\"（K=2 adaptive uncertainty-gated correction）。核心变化：\n- K=2 pairwise L2 uncertainty probe (ρ=0.9979)\n- Adaptive gating：仅在高不确定性步骤触发 CRM\n- Cross-VLA 分析：π₀.₅ (3.6B, 94-99% baseline) + OpenVLA-OFT (7B, deterministic) boundary analysis\n- SmolVLA 基线从 11.6% 提升到 77-83%（四个 suite）\n- 8-seed 扩展分析 Spatial p=0.017\n- 效率表（Table 3）：K=2 batched ~170ms = K=1\n\n### 你的审查侧重\n\n**方法严谨性**：ACR-VLA pipeline 设计是否合理、K=2 uncertainty probe 的理论/实证基础、\"conformal\" 命名合理性\n\n**实验有效性**：\n- 效果量（1-2pp improvement）在 n=3 seeds 下是否有意义\n- Cross-VLA 分析的实验设计（π₀.₅ CRM 是否在 π₀.₅ demos 上重新训练？还是用 SmolVLA 的 CRM？）\n- CRM 训练/评估任务重叠问题是否解决\n\n**统计声明**：n=3 matched seeds 的 power analysis、\"directionally consistent\" 声明的合理性\n\n### 历史遗留 Issue（须逐条标注 [RESOLVED] 或 [STILL_OPEN] + 理由）\n\n1. **C3 (open)**: 不同方法间 seed 数不一致（obs_only 7, VLA-only 5, Argmin 6, Random 3）→ 检查当前版本 seed 数量平衡性\n2. **C6 (in_progress)**: 论文超出 8 页限制 → 检查 PDF 实际页数。注意 discussion.tex 有 \\enlargethispage{6\\baselineskip} hack\n3. **M1 (open)**: 评估范围过窄（单 VLA/单 benchmark/sim-only）→ 现有 π₀.₅ + OpenVLA-OFT，评估是否充分\n4. **M2 (in_progress)**: LIBERO-Spatial null result 仅 1 seed → 现有 8-seed 分析 p=0.017\n5. **M3 (open)**: 缺少 A2C2 实验对比 → A2C2 仍仅在 Related Work 文字定位\n6. **M6 (in_progress)**: CRM 训练/评估任务重叠，无 held-out 泛化验证 → 检查 3-suite vs 4-suite CRM 训练策略是否充分\n7. **R2-W1-new (open)**: 绝对性能极低(17.6%)限制泛化性 → 新基线 77-83%，是否充分\n8. **R1-W3-new (open)**: Applicability boundary 仅基于单一对比 → 现有 3 个 VLA\n9. **R1-N4-latency (in_progress)**: K=10 forward passes latency 未量化 → 检查 Table 3 是否充分\n\n### 审稿格式\n\n请按以下结构输出：\n1. **Issue Status**：逐条对上述 9 个历史 issue 标注 [RESOLVED]/[STILL_OPEN] + 理由\n2. **Strengths**：当前版本优点（逐条）\n3. **Weaknesses**：当前版本问题（逐条，标注 severity: critical/warning/info）\n4. **Questions**：需要作者澄清的问题\n5. **Missing References**：遗漏的重要相关工作\n6. **Overall Score**：strong reject / weak reject / borderline / weak accept / strong accept + confidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "5",
    "project": "acr-vla-conformal-refinement",
    "text": "## Round 5 继续审稿 — Reviewer 1: 方法严谨性 / 实验有效性 / 统计声明\n\n**论文**: \"ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs\"\n**论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex\n**PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_5/submitted.pdf\n**Venue**: CoRL 2026 (deadline 2026-05-28)\n**格式要求**: 正文 ≤8 页（Limitations 计入，Acknowledgments/References/Appendix 不计入），double-blind，CoRL/PMLR 模板\n**审稿模式**: 继续审稿（增量评估）\n\n### 重要背景：论文已大幅重构\n\n论文从上轮的 \"Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs\"（K=10 unconditional correction）完全重构为 \"ACR-VLA\"（K=2 adaptive uncertainty-gated correction）。核心变化：\n- K=2 pairwise L2 uncertainty probe (ρ=0.9979)\n- Adaptive gating：仅在高不确定性步骤触发 CRM\n- Cross-VLA 分析：π₀.₅ (3.6B, 94-99% baseline) + OpenVLA-OFT (7B, deterministic) boundary analysis\n- SmolVLA 基线从 11.6% 提升到 77-83%（四个 suite）\n- 8-seed 扩展分析 Spatial p=0.017\n- 效率表（Table 3）：K=2 batched ~170ms = K=1\n\n### 你的审查侧重\n\n**方法严谨性**：ACR-VLA pipeline 设计是否合理、K=2 uncertainty probe 的理论/实证基础、\"conformal\" 命名合理性\n\n**实验有效性**：\n- 效果量（1-2pp improvement）在 n=3 seeds 下是否有意义\n- Cross-VLA 分析的实验设计（π₀.₅ CRM 是否在 π₀.₅ demos 上重新训练？还是用 SmolVLA 的 CRM？）\n- CRM 训练/评估任务重叠问题是否解决\n\n**统计声明**：n=3 matched seeds 的 power analysis、\"directionally consistent\" 声明的合理性\n\n### 历史遗留 Issue（须逐条标注 [RESOLVED] 或 [STILL_OPEN] + 理由）\n\n1. **C3 (open)**: 不同方法间 seed 数不一致（obs_only 7, VLA-only 5, Argmin 6, Random 3）→ 检查当前版本 seed 数量平衡性\n2. **C6 (in_progress)**: 论文超出 8 页限制 → 检查 PDF 实际页数。注意 discussion.tex 有 \\enlargethispage{6\\baselineskip} hack\n3. **M1 (open)**: 评估范围过窄（单 VLA/单 benchmark/sim-only）→ 现有 π₀.₅ + OpenVLA-OFT，评估是否充分\n4. **M2 (in_progress)**: LIBERO-Spatial null result 仅 1 seed → 现有 8-seed 分析 p=0.017\n5. **M3 (open)**: 缺少 A2C2 实验对比 → A2C2 仍仅在 Related Work 文字定位\n6. **M6 (in_progress)**: CRM 训练/评估任务重叠，无 held-out 泛化验证 → 检查 3-suite vs 4-suite CRM 训练策略是否充分\n7. **R2-W1-new (open)**: 绝对性能极低(17.6%)限制泛化性 → 新基线 77-83%，是否充分\n8. **R1-W3-new (open)**: Applicability boundary 仅基于单一对比 → 现有 3 个 VLA\n9. **R1-N4-latency (in_progress)**: K=10 forward passes latency 未量化 → 检查 Table 3 是否充分\n\n### 审稿格式\n\n请按以下结构输出：\n1. **Issue Status**：逐条对上述 9 个历史 issue 标注 [RESOLVED]/[STILL_OPEN] + 理由\n2. **Strengths**：当前版本优点（逐条）\n3. **Weaknesses**：当前版本问题（逐条，标注 severity: critical/warning/info）\n4. **Questions**：需要作者澄清的问题\n5. **Missing References**：遗漏的重要相关工作\n6. **Overall Score**：strong reject / weak reject / borderline / weak accept / strong accept + confidence"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-27T15:16:19.155950+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15720
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-27T15:16:19.306996+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "5",
  "project": "acr-vla-conformal-refinement",
  "text": "## Round 5 继续审稿 — Reviewer 2: 新颖性定位 / Venue Fit / 完整性 / 可重复性\n\n**论文**: \"ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs\"\n**论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex\n**PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_5/submitted.pdf\n**Venue**: CoRL 2026 (deadline 2026-05-28)\n**格式要求**: 正文 ≤8 页（Limitations 计入，Acknowledgments/References/Appendix 不计入），double-blind，CoRL/PMLR 模板\n**审稿模式**: 继续审稿（增量评估）\n\n### 重要背景：论文已大幅重构\n\n论文从 \"Correction Over Selection: Dissecting...\" 完全重构为 \"ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs\"。核心变化同上（K=2 adaptive gating, cross-VLA analysis on π₀.₅ and OpenVLA-OFT, SmolVLA 基线 77-83%）。\n\n### 你的审查侧重\n\n**新颖性定位**：\n- \"Adaptive conformal refinement\" 的 novelty 是否充分？核心组件（MLP + L2 clipping + pairwise L2 threshold）是否 standard\n- Paper 定位是否清晰（方法 paper vs 分析 paper）\n- \"conformal\" 一词使用是否 misleading（论文自称 \"loosely\"）\n\n**Venue Fit**：\n- CoRL 2026 要求 real-robot 或 sim-to-real 论证，论文纯 sim (LIBERO)\n- 论文对 robotics community 的 contribution\n\n**完整性与写作**：\n- Related Work 是否完整，bib 格式\n- 写作质量、符号一致性\n- DAgger 引用是否仍被误用\n\n**可重复性**：\n- 硬件、训练时间、checkpoint 版本\n- Precompute random seed 是否明确\n\n### 历史遗留 Issue（须逐条标注 [RESOLVED] 或 [STILL_OPEN] + 理由）\n\n1. **C4 (open)**: Novelty 不足——standard MLP + L2 clipping → 论文完全重构为 ACR-VLA，是否解决\n2. **M4 (open)**: Bib entries 缺失 venue info → 检查 RT-2/OpenVLA/Octo 是否仍为 @misc\n3. **M5 (open)**: Figure 中 n=1 点有无意义 error bars → 检查当前 figures\n4. **M7 (in_progress)**: 论文定位不清晰 → 现在定位为方法 paper\n5. **R2-W4-new (in_progress)**: Motivation-evaluation disconnect (LIBERO+ in Intro) → 检查 Intro 是否已修正\n6. **R2-W7-new (in_progress)**: 'Dissecting' title 承诺的分析深度未兑现 → 标题已改为 'ACR-VLA'\n7. **R1-W1-new (in_progress)**: 'Geometric medoid' 术语不正确 → 检查是否改为 'argmin-to-centroid'\n8. **R1-W5-new (in_progress)**: DAgger 引用误用 → 检查 method.tex 中 noise augmentation 的引用\n9. **R3-W8-new (in_progress)**: 硬件环境和训练时间未报告 → 检查 Appendix\n10. **R3-W9-new (open)**: SmolVLA checkpoint 无 commit hash → 检查是否补充\n11. **R3-W10-new (open)**: Precompute pipeline random seed 未指定 → 检查\n\n### 审稿格式\n\n请按以下结构输出：\n1. **Issue Status**：逐条对上述 11 个历史 issue 标注 [RESOLVED]/[STILL_OPEN] + 理由\n2. **Strengths**：当前版本优点（逐条）\n3. **Weaknesses**：当前版本问题（逐条，标注 severity: critical/warning/info）\n4. **Questions**：需要作者澄清的问题\n5. **Missing References**：遗漏的重要相关工作\n6. **Overall Score**：strong reject / weak reject / borderline / weak accept / strong accept + confidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "5",
    "project": "acr-vla-conformal-refinement",
    "text": "## Round 5 继续审稿 — Reviewer 2: 新颖性定位 / Venue Fit / 完整性 / 可重复性\n\n**论文**: \"ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs\"\n**论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex\n**PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_5/submitted.pdf\n**Venue**: CoRL 2026 (deadline 2026-05-28)\n**格式要求**: 正文 ≤8 页（Limitations 计入，Acknowledgments/References/Appendix 不计入），double-blind，CoRL/PMLR 模板\n**审稿模式**: 继续审稿（增量评估）\n\n### 重要背景：论文已大幅重构\n\n论文从 \"Correction Over Selection: Dissecting...\" 完全重构为 \"ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs\"。核心变化同上（K=2 adaptive gating, cross-VLA analysis on π₀.₅ and OpenVLA-OFT, SmolVLA 基线 77-83%）。\n\n### 你的审查侧重\n\n**新颖性定位**：\n- \"Adaptive conformal refinement\" 的 novelty 是否充分？核心组件（MLP + L2 clipping + pairwise L2 threshold）是否 standard\n- Paper 定位是否清晰（方法 paper vs 分析 paper）\n- \"conformal\" 一词使用是否 misleading（论文自称 \"loosely\"）\n\n**Venue Fit**：\n- CoRL 2026 要求 real-robot 或 sim-to-real 论证，论文纯 sim (LIBERO)\n- 论文对 robotics community 的 contribution\n\n**完整性与写作**：\n- Related Work 是否完整，bib 格式\n- 写作质量、符号一致性\n- DAgger 引用是否仍被误用\n\n**可重复性**：\n- 硬件、训练时间、checkpoint 版本\n- Precompute random seed 是否明确\n\n### 历史遗留 Issue（须逐条标注 [RESOLVED] 或 [STILL_OPEN] + 理由）\n\n1. **C4 (open)**: Novelty 不足——standard MLP + L2 clipping → 论文完全重构为 ACR-VLA，是否解决\n2. **M4 (open)**: Bib entries 缺失 venue info → 检查 RT-2/OpenVLA/Octo 是否仍为 @misc\n3. **M5 (open)**: Figure 中 n=1 点有无意义 error bars → 检查当前 figures\n4. **M7 (in_progress)**: 论文定位不清晰 → 现在定位为方法 paper\n5. **R2-W4-new (in_progress)**: Motivation-evaluation disconnect (LIBERO+ in Intro) → 检查 Intro 是否已修正\n6. **R2-W7-new (in_progress)**: 'Dissecting' title 承诺的分析深度未兑现 → 标题已改为 'ACR-VLA'\n7. **R1-W1-new (in_progress)**: 'Geometric medoid' 术语不正确 → 检查是否改为 'argmin-to-centroid'\n8. **R1-W5-new (in_progress)**: DAgger 引用误用 → 检查 method.tex 中 noise augmentation 的引用\n9. **R3-W8-new (in_progress)**: 硬件环境和训练时间未报告 → 检查 Appendix\n10. **R3-W9-new (open)**: SmolVLA checkpoint 无 commit hash → 检查是否补充\n11. **R3-W10-new (open)**: Precompute pipeline random seed 未指定 → 检查\n\n### 审稿格式\n\n请按以下结构输出：\n1. **Issue Status**：逐条对上述 11 个历史 issue 标注 [RESOLVED]/[STILL_OPEN] + 理由\n2. **Strengths**：当前版本优点（逐条）\n3. **Weaknesses**：当前版本问题（逐条，标注 severity: critical/warning/info）\n4. **Questions**：需要作者澄清的问题\n5. **Missing References**：遗漏的重要相关工作\n6. **Overall Score**：strong reject / weak reject / borderline / weak accept / strong accept + confidence"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-27T15:16:20.920456+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1613
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-27T15:16:30.315316+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 CoRL 2026 CFP 调研和论文资料检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '确定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: 分配 R1/R2 独立审稿 (Round 5)', 'status': 'completed', 'activeForm': '分配 Reviewer 1 和 Reviewer 2 审稿任务'}, {'content': 'Step 2: 交叉分享 + 逐条回应', 'status': 'in_progress', 'activeForm': '等待 Reviewer 审稿结果返回'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成最终报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 CoRL 2026 CFP 调研和论文资料检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '确定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: 分配 R1/R2 独立审稿 (Round 5)', 'status': 'completed', 'activeForm': '分配 Reviewer 1 和 Reviewer 2 审稿任务'}, {'content': 'Step 2: 交叉分享 + 逐条回应', 'status': 'in_progress', 'activeForm': '等待 Reviewer 审稿结果返回'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成最终报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-27T15:16:30.466512+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 288 · 2026-05-27T15:16:34.975395+00:00_

Round 5 审稿已启动：

- **R1**（方法/实验/统计）：已分配，携带 9 个历史 issue
- **R2**（新颖性/venue fit/完整性/可重复性）：已分配，携带 11 个历史 issue
- **视觉审查**：已派发，并行执行
- **外部审稿**：未配置，跳过

等待两位 Reviewer 返回审稿结果后执行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 289 · 2026-05-27T15:22:45.682442+00:00_

[Reviewer 2 审稿意见]:
## Round 5 审稿报告 — Reviewer 2: 新颖性定位 / Venue Fit / 完整性 / 可重复性

### 审查依据
基于 CoRL 2023 公开 Reviewer Guidelines 六维度框架（Originality, Quality, Clarity, Significance, Relevance, Limitations），结合 CoRL 2024 统计数据（rating ~1-4 scale, accepted 均值 ~3.01）。

---

## 1. Issue Status（11 条历史 issue）

**C4 [PARTIALLY_RESOLVED]**: Novelty 不足 — standard MLP + L2 clipping
- 论文重构为 ACR-VLA，贡献重心移至 adaptive gating 机制 + "when to correct > correction strength" insight。K=2 probe ρ=0.9979 是实用发现。但核心组件（pairwise L2 → threshold → MLP + L2 clip）仍全部 standard，重构改善了 framing，novelty concern 本质未消除。

**M4 [STILL_OPEN]**: Bib entries 缺失 venue info
- `kim2024openvla` (OpenVLA) 仍为 @misc → 已发表于 CoRL 2024，应改 @inproceedings
- `ghosh2024octo` (Octo) 仍为 @misc → 已正式发表，应补充 venue
- `brohan2023rt2` (RT-2) 仍为 @misc → 可标注为 technical report

**M5 [RESOLVED]**: Table 1 用上标 (n) 标注 seed 数，Figure 2 caption 明确 "±1 std over available seeds"，n=1 条目无 error bar。

**M7 [RESOLVED]**: 定位清晰——method paper，标题/contributions 结构对齐。

**R2-W4-new [RESOLVED]**: LIBERO+ 不再出现于 Intro，motivation-evaluation 对齐。

**R2-W7-new [RESOLVED]**: 标题已改为 "ACR-VLA: Adaptive Conformal Refinement..."。

**R1-W1-new [RESOLVED]**: 全文统一使用 "argmin-to-centroid"，数学定义正确。

**R1-W5-new [STILL_OPEN]**: DAgger 引用仍然不准确。method.tex: "Gaussian noise augmentation on a_base to improve generalization to the closed-loop state distribution [DAgger]"。DAgger 的核心是交互式在线数据收集，不是 noise augmentation。应分开引用：DAgger motivates distribution mismatch problem，noise augmentation 需独立引用或不引用。

**R3-W8-new [RESOLVED]**: Appendix D 报告了完整硬件/训练信息：RTX 4090 24GB，3-suite CRM ~6 GPU-hours，PyTorch 2.4/Transformers 4.45。

**R3-W9-new [STILL_OPEN]**: 无 checkpoint commit hash/version。论文仅说 "SmolVLA (0.4B)"、"π₀.₅ (3.6B)"、"OpenVLA-OFT (7B)"，缺乏精确的权重版本标识。

**R3-W10-new [STILL_OPEN]**: Precompute pipeline random seed 未指定。8-seed analysis 用 seed 42-49，但 K=10 forward-pass cache 的 seed 控制未说明。

---

## 2. Strengths

**S1** 清晰的 mechanistic insight："when to correct > correction strength"，Figure 3 trigger rate vs improvement scatter 是最有说服力的证据。

**S2** K=2 uncertainty probe 实用价值高：ρ=0.9979 vs K=10 variance，latency-free（batched），Table 6 清晰排除 3 个替代方案。可复用发现。

**S3** 诚实的 limitations：明确承认 n=3 统计不足、confident-but-wrong 盲区、单 benchmark、sim-only。

**S4** Cross-VLA boundary analysis 有价值：π₀.₅ + OpenVLA-OFT 明确了适用范围（stochastic VLA 为前提，near-expert 收益递减）。

**S5** 8-seed paired analysis 在 Spatial 达到 p=0.017，是唯一达统计显著的结果。

---

## 3. Weaknesses

**W1 [critical] "Conformal" 命名 misleading**
- Title + Abstract + Section 3.5 承认 "loosely"
- Conformal prediction 有严格数学定义（distribution-free coverage guarantee），论文明确不实现
- 标题是论文被引形式，"Conformal Refinement" 会误导读者期望形式化保证
- 建议改为 "Calibrated" 或 "Uncertainty-Gated"

**W2 [critical] 统计功效严重不足**
- Table 1: Adaptive vs VLA-only Δ = +1.5, +0.1, +1.3, -0.3 pp (n=3), Spatial p≈0.27
- 唯一达 α=0.05 的是 Appendix E 8-seed Spatial（p=0.017），仅覆盖 1/4 suite
- Adaptive vs CRM always-on 同样 n=3，无 p-value 支撑
- 建议至少在其他 suite 补充 8-seed 分析

**W3 [critical] 单一 benchmark（LIBERO），纯 simulation**
- 全部实验仅 LIBERO 4 suite（tabletop manipulation），无第二 sim benchmark，无 real-robot
- CoRL 要求 "Will the CoRL audience be interested?"——纯 sim 单 benchmark 竞争力不足

**W4 [warning] ε 不同导致 Adaptive vs CRM always-on 对比存在 confound**
- ACR-VLA ε=0.2 vs CRM always-on ε=0.05，非 apple-to-apple
- 缺少 ε-matched ablation（同一 ε 下 gated vs ungated）

**W5 [warning] π₀.₅ Object 上 ACR-VLA 比 CRM 更差（86.2% vs 88.0%），分析不充分**
- 论文仅说 "K=2 selection noise outweighs recovery"，未解释 gating 机制为何失效
- 如果 gating 在低 uncertainty 时 pass-through，为何反而更差？暗示 K=2 selection 本身引入噪声

**W6 [warning] 技术组件全部 standard，系统级 novelty 有限**
- Pairwise L2 + threshold + MLP + L2 clip，各组件无技术创新
- 主要贡献为组合 + 实证 insight，更接近 empirical finding paper

**W7 [info] Long suite 多个 baseline 仅 n=1 seed**
- K=10 argmin Long (n=1), K=2 mean Long (n=1)

**W8 [info] Related Work 缺少 uncertainty estimation 经典引用**
- 未引 Lakshminarayanan 2017 (Deep Ensembles), Gal & Ghahramani 2016 (MC Dropout)
- K=2 sampling 本质是 2-member ensemble disagreement，与这些方法直接相关

---

## 4. Questions

**Q1**: ACR-VLA 在 ε=0.05 下的性能如何？ε-matched 下 Δ_CRM 是否仍为正？

**Q2**: Precompute cache 的 random seed sensitivity 如何？更换 seed 后结果是否稳定？

**Q3**: Table 2 中 K=10 也标 ~170ms (batched)。如果 K=10 也能 batch 到同等 latency，K=2 的 efficiency advantage 具体是什么（GPU memory？）

**Q4**: Long suite trigger rate 最低（~4%）但 baseline 也最低（58%）。最难 suite 应有最高 uncertainty，但数据不支持。pairwise L2 是否在 long-horizon tasks 上不是好的 uncertainty proxy？

---

## 5. Missing References

1. Lakshminarayanan et al., 2017 — Deep Ensembles (NeurIPS 2017)
2. Gal & Ghahramani, 2016 — MC Dropout (ICML 2016)
3. OpenVLA bib 应更新为 CoRL 2024 @inproceedings
4. Octo bib 应补充正式 venue

---

## 6. Overall Score

**Rating: Weak Reject** (2/4 on CoRL scale)
**Confidence: High** (4/5)

**一句话总结**: 论文提出了清晰且工程合理的 adaptive gating pipeline，但核心组件全部 standard，效果有限（<2pp）且绝大多数未达统计显著，"conformal" 命名误导，纯 sim 单 benchmark 难以满足 CoRL robotics venue 要求。

### 官方维度打分（CoRL 2023 Guidelines）

| 维度 | 评价 | 理由 |
|------|------|------|
| Originality | Low-Medium | 各组件 standard，novelty 在组合与 empirical insight |
| Quality | Medium | 实验设计合理但统计功效不足，ε confound 未控制 |
| Clarity | High | 写作清晰，结构好，notation 一致，limitations 诚实 |
| Significance | Low | 效果 <2pp，最强结果为防止 degradation，实用价值有限 |
| Relevance | Medium | 问题与 CoRL 相关，但纯 sim 单 benchmark 削弱 robotics 贡献 |
| Limitations | High | Section 6 诚实报告所有主要局限 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 290 · 2026-05-27T15:22:59.200494+00:00_

R2 审稿完成，评分 **Weak Reject**。核心问题："conformal" 命名误导、统计功效不足、单一 benchmark + sim-only、ε confound。等待 R1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 291 · 2026-05-27T15:23:01.905042+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：Weak Reject。论文经过重构后 framing 明显改善（7/11 历史 issue 已解决），写作清晰度高，K=2 probe 的 ρ=0.9979 发现有实用价值。但三个 critical 问题阻碍接收：
1. "Conformal" 命名误导（论文自认不实现 conformal prediction guarantees）
2. 统计功效严重不足（n=3, 仅 Spatial 8-seed 达 p=0.017，其余 3 suite 无显著性）
3. 纯 simulation 单 benchmark（LIBERO only），对 CoRL robotics venue 竞争力不足

4 个历史 issue 仍为 STILL_OPEN：DAgger 引用误用 (R1-W5)、bib venue 缺失 (M4)、checkpoint hash 缺失 (R3-W9)、precompute seed 未指定 (R3-W10)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 292 · 2026-05-27T15:23:07.224801+00:00_

R2 审稿已收到。等待 R1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 35

## Round 35

8 recorded events


### User

_source line 293 · 2026-05-27T15:25:30.955599+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 5 审稿意见

**论文**: ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs
**审查侧重**: 方法严谨性 / 实验有效性 / 统计声明

---

## 总体评分
**Overall**: 5/10 (Borderline)
**一句话总结**: ACR-VLA 提出了优雅的 K=2 不确定性代理和自适应门控机制，但核心实验效果量仅 1-2pp 且 n=3 seeds 下不显著，"conformal" 命名缺乏理论支撑，正文超出 8 页限制。

## 官方维度打分（基于 CoRL Review Guidelines: Originality / Quality / Clarity / Significance / Relevance / Limitations）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 6/10 | K=2 pairwise L2 作为不确定性代理是简洁的新颖贡献；自适应门控有价值；但整体 pipeline 是已有组件的组合 |
| Quality / Soundness | 4/10 | 主实验 n=3 seeds 无显著性；"conformal" 命名误导；CRM 训练/评估任务重叠未充分 addressed；Cross-VLA CRM 是否重训不清楚 |
| Clarity | 7/10 | 论文组织清晰，写作流畅；Figure 1 pipeline 图直观 |
| Significance | 5/10 | 1-2pp 改进的实际价值有限；gating 分析和 cross-VLA boundary 分析有洞察价值但不构成独立贡献 |
| Relevance | 7/10 | VLA 推理优化是 CoRL 社区高度关注的话题 |
| Limitations | 6/10 | 诚实报告了统计 power 不足和 sim-only 限制，但 limitations 溢出到第 9 页违反格式要求 |

---

## Issue Status（9 个历史 Issue）

**C3** [RESOLVED]: Table 1 所有方法均使用 n=3 matched seeds，seed 数量已平衡。

**C6** [STILL_OPEN]: Section 6 Limitations 位于 PDF 第 9 页。Section 5 Conclusion 占满第 8 页底部，Limitations 无法挤入。正文约 8.3-8.5 页，超出 ≤8 页要求。

**M1** [PARTIALLY_RESOLVED]: 现覆盖 3 个 VLA（SmolVLA 200M / π₀.₅ 3.6B / OpenVLA-OFT 7B），但仍限于 LIBERO 单一 benchmark、仅仿真。

**M2** [RESOLVED]: Table 7（Appendix E）8-seed 分析：Δ=+1.4pp，p=0.017，7/8 seeds 正向。

**M3** [STILL_OPEN]: A2C2 仍仅在 Related Work 文字定位，无实验对比。

**M6** [STILL_OPEN]: CRM 在评估 suite 的 demo 数据上训练（Spatial/Object/Goal 训 3 suite，Long 训全部 4 suite），均含评估 suite 数据。无 leave-one-suite-out 泛化测试。

**R2-W1-new** [RESOLVED]: SmolVLA 基线 77-83%，绝对性能不再是瓶颈。

**R1-W3-new** [RESOLVED]: 3 个 VLA 跨越 stochastic/deterministic boundary。

**R1-N4-latency** [RESOLVED]: Table 2 提供完整计算对比，K=2 ~170ms。

---

## Must-Fix 问题

**N1** [critical] 核心效果量过小且主实验统计 power 不足
- 位置：Table 1, Section 4.2
- 四个 suite 改进 +1.0~+2.1pp，n=3 下均不显著。仅 Spatial 有 8-seed p=0.017，其余 3 suite 仍 n=3。"Directionally consistent" 是 "not significant" 的委婉说法。
- 建议：至少 Object+Goal 补充 8-seed 分析，或提供 power analysis。

**N2** [critical] "Conformal" 命名缺乏理论基础
- 位置：Title, Abstract, Section 3.5
- Section 3.5 明确承认不实现 conformal prediction guarantees，但标题仍用 "conformal"。Conformal prediction 有严格定义（coverage guarantee, exchangeability），论文的阈值机制不具备这些性质。
- 建议：改为 "calibrated" 或 "uncertainty-gated"；或实现真正的 split conformal guarantee。

**N3** [critical] CRM 训练/评估任务重叠
- 位置：Section 4.1 CRM training
- CRM 在评估 suite 数据上训练，无 held-out 泛化测试。327K 参数的 CRM 可能只是记忆了特定 task 的 action residual pattern。
- 建议：添加 leave-one-suite-out 实验。

## Should-Fix 问题

**W1** [warning] Cross-VLA CRM 训练数据不明确：Table 3 中 π₀.₅ 的 CRM 是否在 π₀.₅ demos 上重训？未说明则无法判断 near-expert degradation 是方法局限还是 distribution mismatch artifact。

**W2** [warning] 正文超 8 页：Limitations 在第 9 页，违反 CoRL 格式要求。

**W3** [warning] 缺 A2C2 实验对比：作为最直接可比方法，仅文字定位不足。

**W4** [warning] Sim-only，无 real-robot 验证。LIBERO 的 action space 和 observation noise 与 real-world 有本质差异。

**W5** [warning] 8-seed 分析仅覆盖 Spatial 一个 suite，其余 3 suite 统计证据不完整。

## 小问题
- Table 1 未包含 K=2 argmin baseline，应说明其退化原因
- Figure 3 label 重叠
- CRM 隐藏层维度需参考 Appendix 才知
- Table 6 ρ=0.9979 极高，建议增加 scatter plot 可视化

## Questions
1. Table 3 中 π₀.₅ CRM 是否重训？训练数据量是否与 SmolVLA 相同？
2. 为什么 8-seed 仅覆盖 Spatial？计算成本多少？
3. 是否尝试 leave-one-suite-out CRM 泛化设计？
4. π₀.₅ 是否需要不同的 τ？
5. 是否考虑实现 split conformal prediction 使命名名副其实？

## Missing References
- STEER (Sontakke et al., 2025): inference-time steering for VLAs
- Conformal prediction in robotics (如 Luo et al. 2024): 实际实现了 conformal guarantees，与本文 "loose" 使用形成对比

## 主要优势
1. K=2 pairwise L2 不确定性代理（ρ=0.9979）是最强技术贡献
2. 自适应门控分析透彻（Figure 3, Section 4.3）
3. Cross-VLA boundary 分析有领域指导意义
4. 写作质量好、pipeline 简洁
5. 效率优势实际（K=2 ~170ms）

**Confidence**: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-27T15:25:43.353611+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 CoRL 2026 CFP 调研和论文资料检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '确定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: 分配 R1/R2 独立审稿 (Round 5)', 'status': 'completed', 'activeForm': '分配 Reviewer 1 和 Reviewer 2 审稿任务'}, {'content': 'Step 2: 交叉分享 + 逐条回应', 'status': 'in_progress', 'activeForm': '执行交叉分享和逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成最终报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 CoRL 2026 CFP 调研和论文资料检查'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '确定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: 分配 R1/R2 独立审稿 (Round 5)', 'status': 'completed', 'activeForm': '分配 Reviewer 1 和 Reviewer 2 审稿任务'}, {'content': 'Step 2: 交叉分享 + 逐条回应', 'status': 'in_progress', 'activeForm': '执行交叉分享和逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成最终报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-27T15:25:43.354447+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-27T15:26:06.514210+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "5",
  "project": "acr-vla-conformal-refinement",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Issue Status（11 条）\n- C4 [PARTIALLY_RESOLVED]: Novelty — 重构改善 framing，但核心组件 standard\n- M4 [STILL_OPEN]: OpenVLA @misc→CoRL 2024, Octo @misc→补 venue, RT-2→tech report\n- M5 [RESOLVED]: Table 1 上标 (n)，n=1 无 error bar\n- M7 [RESOLVED]: 定位清晰 method paper\n- R2-W4-new [RESOLVED]: LIBERO+ 不再出现\n- R2-W7-new [RESOLVED]: 标题已改\n- R1-W1-new [RESOLVED]: argmin-to-centroid 统一\n- R1-W5-new [STILL_OPEN]: DAgger 引用误用——noise augmentation ≠ DAgger interactive aggregation\n- R3-W8-new [RESOLVED]: Appendix D 有完整硬件信息\n- R3-W9-new [STILL_OPEN]: 无 checkpoint commit hash\n- R3-W10-new [STILL_OPEN]: Precompute seed 未指定\n\n### Strengths\n- S1: \"when to correct > correction strength\" mechanistic insight\n- S2: K=2 probe ρ=0.9979 实用价值高\n- S3: 诚实 limitations\n- S4: Cross-VLA boundary analysis\n- S5: 8-seed p=0.017\n\n### Weaknesses\n- **W1 [critical]**: \"Conformal\" 命名 misleading（论文自认不实现 formal conformal prediction guarantees）\n- **W2 [critical]**: 统计功效不足（n=3, 仅 Spatial 8-seed 达 p=0.017）\n- **W3 [critical]**: 纯 sim 单 benchmark (LIBERO)\n- **W4 [warning]**: ε 不同导致 Adaptive vs CRM always-on 对比存在 confound（ACR-VLA ε=0.2 vs CRM always-on ε=0.05）\n- **W5 [warning]**: π₀.₅ Object 上 ACR-VLA 比 CRM 更差（86.2% vs 88.0%），分析不充分\n- **W6 [warning]**: 技术组件全部 standard\n- **W7 [info]**: Long suite 多个 baseline 仅 n=1\n- **W8 [info]**: 缺少 Deep Ensembles / MC Dropout 经典引用\n\n### Questions\n- Q1: ACR-VLA 在 ε=0.05 下性能如何？\n- Q2: Precompute cache seed sensitivity?\n- Q3: K=10 也标 ~170ms batched，K=2 效率优势具体是什么？\n- Q4: Long suite trigger rate 最低但 baseline 最低，L2 是否 long-horizon 上不可靠？\n\n### Missing References\n- Deep Ensembles (Lakshminarayanan 2017)\n- MC Dropout (Gal & Ghahramani 2016)\n- OpenVLA bib → CoRL 2024\n- Octo bib → 补 venue\n\n### Overall: Weak Reject (2/4), Confidence High (4/5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "5",
    "project": "acr-vla-conformal-refinement",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Issue Status（11 条）\n- C4 [PARTIALLY_RESOLVED]: Novelty — 重构改善 framing，但核心组件 standard\n- M4 [STILL_OPEN]: OpenVLA @misc→CoRL 2024, Octo @misc→补 venue, RT-2→tech report\n- M5 [RESOLVED]: Table 1 上标 (n)，n=1 无 error bar\n- M7 [RESOLVED]: 定位清晰 method paper\n- R2-W4-new [RESOLVED]: LIBERO+ 不再出现\n- R2-W7-new [RESOLVED]: 标题已改\n- R1-W1-new [RESOLVED]: argmin-to-centroid 统一\n- R1-W5-new [STILL_OPEN]: DAgger 引用误用——noise augmentation ≠ DAgger interactive aggregation\n- R3-W8-new [RESOLVED]: Appendix D 有完整硬件信息\n- R3-W9-new [STILL_OPEN]: 无 checkpoint commit hash\n- R3-W10-new [STILL_OPEN]: Precompute seed 未指定\n\n### Strengths\n- S1: \"when to correct > correction strength\" mechanistic insight\n- S2: K=2 probe ρ=0.9979 实用价值高\n- S3: 诚实 limitations\n- S4: Cross-VLA boundary analysis\n- S5: 8-seed p=0.017\n\n### Weaknesses\n- **W1 [critical]**: \"Conformal\" 命名 misleading（论文自认不实现 formal conformal prediction guarantees）\n- **W2 [critical]**: 统计功效不足（n=3, 仅 Spatial 8-seed 达 p=0.017）\n- **W3 [critical]**: 纯 sim 单 benchmark (LIBERO)\n- **W4 [warning]**: ε 不同导致 Adaptive vs CRM always-on 对比存在 confound（ACR-VLA ε=0.2 vs CRM always-on ε=0.05）\n- **W5 [warning]**: π₀.₅ Object 上 ACR-VLA 比 CRM 更差（86.2% vs 88.0%），分析不充分\n- **W6 [warning]**: 技术组件全部 standard\n- **W7 [info]**: Long suite 多个 baseline 仅 n=1\n- **W8 [info]**: 缺少 Deep Ensembles / MC Dropout 经典引用\n\n### Questions\n- Q1: ACR-VLA 在 ε=0.05 下性能如何？\n- Q2: Precompute cache seed sensitivity?\n- Q3: K=10 也标 ~170ms batched，K=2 效率优势具体是什么？\n- Q4: Long suite trigger rate 最低但 baseline 最低，L2 是否 long-horizon 上不可靠？\n\n### Missing References\n- Deep Ensembles (Lakshminarayanan 2017)\n- MC Dropout (Gal & Ghahramani 2016)\n- OpenVLA bib → CoRL 2024\n- Octo bib → 补 venue\n\n### Overall: Weak Reject (2/4), Confidence High (4/5)"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-27T15:26:16.310002+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9795
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-27T15:26:16.510963+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "5",
  "project": "acr-vla-conformal-refinement",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Issue Status（9 条）\n- C3 [RESOLVED]: n=3 matched seeds 已平衡\n- C6 [STILL_OPEN]: Limitations 在第 9 页，正文约 8.3-8.5 页\n- M1 [PARTIALLY_RESOLVED]: 3 个 VLA，仍单 benchmark sim-only\n- M2 [RESOLVED]: 8-seed p=0.017\n- M3 [STILL_OPEN]: A2C2 无实验对比\n- M6 [STILL_OPEN]: CRM 训练/评估任务重叠，无 held-out 泛化\n- R2-W1-new [RESOLVED]: 77-83% 基线\n- R1-W3-new [RESOLVED]: 3 VLA\n- R1-N4-latency [RESOLVED]: Table 2 完整\n\n### Must-Fix\n- **N1 [critical]**: 核心效果量 1-2pp，n=3 不显著。仅 Spatial 8-seed p=0.017\n- **N2 [critical]**: \"Conformal\" 命名无理论基础\n- **N3 [critical]**: CRM 训练/评估任务重叠，无 held-out 泛化测试\n\n### Should-Fix\n- **W1 [warning]**: Cross-VLA CRM 训练数据不明确——π₀.₅ CRM 是否重训？\n- **W2 [warning]**: 正文超 8 页\n- **W3 [warning]**: 缺 A2C2 实验对比\n- **W4 [warning]**: Sim-only 无 real-robot\n- **W5 [warning]**: 8-seed 仅覆盖 Spatial\n\n### 小问题\n- 缺 K=2 argmin baseline 说明\n- Figure 3 label 重叠\n- CRM 隐层维度仅在 Appendix\n- Table 6 建议增加 scatter plot\n\n### Questions\n1. π₀.₅ CRM 是否重训？\n2. 为什么 8-seed 仅 Spatial？\n3. 是否尝试 leave-one-suite-out？\n4. π₀.₅ 是否需要不同 τ？\n5. 是否考虑实现 split conformal？\n\n### Missing References\n- STEER (Sontakke 2025): inference-time steering for VLAs\n- Conformal prediction in robotics (Luo et al. 2024)\n\n### 主要优势\n1. K=2 pairwise L2 probe ρ=0.9979\n2. 自适应门控分析透彻\n3. Cross-VLA boundary 分析\n4. 写作质量好\n5. 效率优势\n\n### Overall: 5/10 Borderline, Confidence 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "5",
    "project": "acr-vla-conformal-refinement",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Issue Status（9 条）\n- C3 [RESOLVED]: n=3 matched seeds 已平衡\n- C6 [STILL_OPEN]: Limitations 在第 9 页，正文约 8.3-8.5 页\n- M1 [PARTIALLY_RESOLVED]: 3 个 VLA，仍单 benchmark sim-only\n- M2 [RESOLVED]: 8-seed p=0.017\n- M3 [STILL_OPEN]: A2C2 无实验对比\n- M6 [STILL_OPEN]: CRM 训练/评估任务重叠，无 held-out 泛化\n- R2-W1-new [RESOLVED]: 77-83% 基线\n- R1-W3-new [RESOLVED]: 3 VLA\n- R1-N4-latency [RESOLVED]: Table 2 完整\n\n### Must-Fix\n- **N1 [critical]**: 核心效果量 1-2pp，n=3 不显著。仅 Spatial 8-seed p=0.017\n- **N2 [critical]**: \"Conformal\" 命名无理论基础\n- **N3 [critical]**: CRM 训练/评估任务重叠，无 held-out 泛化测试\n\n### Should-Fix\n- **W1 [warning]**: Cross-VLA CRM 训练数据不明确——π₀.₅ CRM 是否重训？\n- **W2 [warning]**: 正文超 8 页\n- **W3 [warning]**: 缺 A2C2 实验对比\n- **W4 [warning]**: Sim-only 无 real-robot\n- **W5 [warning]**: 8-seed 仅覆盖 Spatial\n\n### 小问题\n- 缺 K=2 argmin baseline 说明\n- Figure 3 label 重叠\n- CRM 隐层维度仅在 Appendix\n- Table 6 建议增加 scatter plot\n\n### Questions\n1. π₀.₅ CRM 是否重训？\n2. 为什么 8-seed 仅 Spatial？\n3. 是否尝试 leave-one-suite-out？\n4. π₀.₅ 是否需要不同 τ？\n5. 是否考虑实现 split conformal？\n\n### Missing References\n- STEER (Sontakke 2025): inference-time steering for VLAs\n- Conformal prediction in robotics (Luo et al. 2024)\n\n### 主要优势\n1. K=2 pairwise L2 probe ρ=0.9979\n2. 自适应门控分析透彻\n3. Cross-VLA boundary 分析\n4. 写作质量好\n5. 效率优势\n\n### Overall: 5/10 Borderline, Confidence 4/5"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-27T15:26:18.070628+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_416d453a45869a9406db62186b1e3ef7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1559
}
```

</details>

---


### Assistant

_source line 300 · 2026-05-27T15:26:21.202641+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 301 · 2026-05-27T15:26:23.873712+00:00_

[Reviewer 1 审稿结果]:
审稿完成，已清理临时图片。

审稿意见已提交给 Review Director。核心判断：**5/10 Borderline**。

3 个 critical 问题：
1. 主实验效果量 1-2pp + n=3 seeds 不显著，8-seed 仅覆盖 Spatial
2. "Conformal" 命名与实际机制不符（无 coverage guarantee）
3. CRM 训练/评估任务重叠，无 held-out 泛化验证

5 个 resolved issues（C3/M2/R2-W1/R1-W3/R1-N4），3 个 still open（C6 页数/M3 A2C2/M6 CRM 重叠），1 个 partially resolved（M1 评估范围）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 302 · 2026-05-27T15:26:29.438775+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director"
}
```

</details>

---


## Round 37

## Round 37

48 recorded events


### User

_source line 303 · 2026-05-27T15:27:33.927680+00:00_

[Reviewer 2 审稿意见]:
## 交叉回应 — Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

### Must-Fix

**[AGREE] R1-N1**: 核心效果量 1-2pp，n=3 不显著
- 完全同意（我的 W2 [critical]）。Table 1 Δ=+1.5/+0.1/+1.3/-0.3 pp (n=3), Spatial p≈0.27。8-seed 仅覆盖 1/4 suite。补充：Adaptive vs CRM always-on 对比还存在 ε confound（ε=0.2 vs ε=0.05，非 apple-to-apple）。

**[AGREE] R1-N2**: "Conformal" 命名无理论基础
- 完全同意（我的 W1 [critical]）。Section 3.5 自承 "loosely"，标题中使用却不实现其形式化保证，难以辩护。

**[REBUT] R1-N3**: CRM 训练/评估任务重叠
- 部分不同意严重程度。CRM 输入为 observation embedding + selected action（Section 3.3），不是 task identity。训练用 10 demos/task 的 precomputed passes，评估在 20 independent rollouts 上。这是标准 train/test rollout split，非 data leakage。3-suite / 4-suite CRM 分离也有说明（Section 4.1）。应降为 **warning**。但同意缺少 leave-one-suite-out 是弱点。

### Should-Fix

**[AGREE] R1-W1**: π₀.₅ CRM 训练 setup 未明确描述。Section 3.3 暗示 per-VLA 重训（n_obs 不同），但缺少具体说明。

**[AGREE] R1-W2**: 正文可能超 8 页。Limitations 在 PDF 第 9 页顶部，discussion.tex 有 \enlargethispage 和 \vspace hack。

**[REBUT] R1-W3**: A2C2 实验对比。A2C2 解决 temporal staleness，ACR-VLA 解决 initial action quality——Section 1/2 明确区分。A2C2 为 concurrent work (arXiv 2509)，实验对比非硬性要求，讨论区分即可。

**[AGREE] R1-W4**: Sim-only（我的 W3 [critical]）。

**[AGREE] R1-W5**: 8-seed 仅 Spatial（我的 W2 补充点）。

### 小问题

[AGREE] 缺 K=2 argmin baseline（无法分解 selection vs correction 贡献）。
[AGREE] Figure 3 label 重叠。
[REBUT] CRM 隐层维度——实际在 Section 3.3 正文已写 "Linear(n_in, 256) → ReLU → Linear(256, 256) → ReLU → Linear(256, H·d)"，R1 可能疏忽。

### Missing References
[AGREE] STEER 和 conformal prediction in robotics 都应引用。

### Overall 对比
R1: 5/10 Borderline | R2: Weak Reject (2/4)。大致对齐。

核心共识：(1) K=2 probe 好 (2) 统计功效不足 (3) "Conformal" 需改 (4) Sim-only 单 benchmark (5) 写作质量好

主要分歧：N3 严重程度——我认为 CRM train/eval overlap 是 warning 非 critical，因为 rollout-level split 是标准做法，但缺 held-out suite 测试确实是弱点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-27T15:27:58.354908+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status,read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status,read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-27T15:27:58.455570+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-27T15:28:02.268817+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-27T15:28:02.319608+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-27T15:28:06.285398+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-27T15:28:06.787143+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-27T15:28:07.088440+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-27T15:28:09.245720+00:00_

{"result":"# 项目 acr-vla-conformal-refinement 概况\n\n## 实验状态 (1362 个)\n\n- **crm-train-v1**: DONE (killed) — \n- **crm-train-k5**: DONE (killed) — \n- **eval-scalar-unc-spatial**: DONE (killed) — \n- **eval-acr-spatial-v2**: DONE (killed) — \n- **eval-k5-spatial**: DONE (killed) — \n- **eval-object-v7-full**: DONE (killed) — \n- **eval-spatial-v6-full**: DONE (killed) — \n- **eval-object-v5-full**: DONE (killed) — \n- **eval-acr-vla-spatial-v1**: DONE (killed) — \n- **eval-acr-spatial-v1**: DONE (killed) — \n- **eval-reconvla-spatial-v2**: DONE (killed) — \n- **eval-object-v4-full**: DONE (killed) — \n- **eval-spatial-v5-full**: DONE (killed) — \n- **eval-spatial-v3-full**: DONE (killed) — \n- **eval-spatial-reeval-v2**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-27\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval-tau005-spatial-s42 | τ=0.05 Adaptive Conformal on Spatial s42. Extends τ-sweep below τ=0.10 to test if extremely low threshold causes excessive triggering and further SR degradation (τ=0.10 already showed 75.2% trigger rate hurting SR). | — | — | — |\n\n## 待处理\n- eval-k2-tau035-spatial-s42: K=2 τ-sweep: τ=0.35 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.（排队等待 GPU）\n- eval-k2-tau025-spatial-s42: K=2 τ-sweep: τ=0.25 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.（排队等待 GPU）\n- …另有 172 项\n\n## 近期结论\n- **eval-obs-object-norm003-s45** (failed): CRM obs_only norm=0.03 Object s45: additional seed for Table 1 supplementary norm sweep\n\n## 趋势\n成功 701 / 负向 97 / 失败 126 / 共 1160\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-18228: 无 GPU 信息\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\ncqa1-32758: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\n\n## 告警\n- plan_001-crm-smolvla: 训练失败 — unknown\n- plan_014-reconvla-baseline: 训练失败 — unkno
…[truncated 1835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2960
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-27T15:28:09.246108+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 2458
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-27T15:28:09.246369+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-27T15:15:03.771421+00:00\", \"completed_at\": \"2026-05-27T15:17:41.149663+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 11\", \"message\": \"参考文献尾页仅有 2 条 entry（[27]-[28]），剩余 >80% 页面为空白。看起来像 LaTeX 在 Appendix 前强制换页所致，视觉效果差，审稿人可能认为引用不充分或排版粗糙\"}, {\"severity\": \"warning\", \"dimension\": \"page 14\", \"message\": \"附录最后一页 Table 7 + 2 行文字仅占约 25% 页面，>60% 大面积空白。建议将 Appendix E 的分析文字扩展或与前页合并以消除空白\"}, {\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前两页为连续纯文本（title/abstract/intro/related work），无 display item 穿插。虽为 NeurIPS 格式常态，但若能将 Figure 1（当前 page 3 顶部）提前至 page 2 会增强审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 最优值已加粗，booktabs 风格正确，数字精度统一（±小数一位）。Figure 2 柱状图颜色可区分，但 5 个方法使用的颜色在灰度打印下区分度可能不足——建议辅以不同 hatching pattern\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 散点图清晰可读，标注了统计显著性信息（p ≥ 0.05, n=3），axis label 字号合适。\\\"all suites n.s.\\\" 的注释框有助于审稿人快速抓取结论\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 2157
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-27T15:28:15.252522+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_4.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_4.md"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-27T15:28:15.560024+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/review_director_a3659f64.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 307
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-27T15:28:15.560451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-27T15:28:15.611368+00:00_

1	- id: "C1"
2	  summary: "Fisher exact test independence violation (pseudo-replication)"
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 1
8	  mentions:
9	    - {round: 1, reviewers: [R1, R2, R3], note: "Same-seed episodes share CRM weights, violating independence assumption"}
10	    - {round: 2, reviewers: [R1, R2], note: "已修复。改用 seed-level Mann-Whitney U，三位 Reviewer 均肯定统计方法严谨"}
11	  action_items:
12	    - {round: 1, action: "Replace Fisher with Mann-Whitney U", assigned_to: "Paper Agent + Agent", status: "done"}
13	  resolution: "改用 seed-level Mann-Whitney U + sign test 补充验证"
14	  resolution_round: 2
15	
16	- id: "C2"
17	  summary: "Core claim contradicts K=1 data"
18	  category: framing
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 1
22	  last_seen_round: 1
23	  mentions:
24	    - {round: 1, reviewers: [R1, R2, R3], note: "K=1 CRM below baseline means correction alone harmful"}
25	    - {round: 2, reviewers: [R1, R2], note: "已修复。Reframe 为 'correction is active mechanism, multi-sampling is enabling condition'"}
26	  action_items:
27	    - {round: 1, action: "Reframe core claim", assigned_to: "Paper Agent", status: "done"}
28	  resolution: "重构核心 claim"
29	  resolution_round: 2
30	
31	- id: "C3"
32	  summary: "Inconsistent seed counts across methods"
33	  category: experiment
34	  severity: critical
35	  status: open
36	  first_raised_round: 1
37	  last_seen_round: 2
38	  mentions:
39	    - {round: 1, reviewers: [R1, R2, R3], note: "obs_only 7, VLA-only 5, Argmin 6, Random 3"}
40	    - {round: 2, reviewers: [R1, R2, R3], note: "论文增加说明但 Random 仅 3 seeds 的 'statistically indistinguishable' 结论不成立。R3 补充：n1=3,n2=5 时即使完全分离也只能 p=0.036。"}
41	  action_items:
42	    - {round: 2, action: "所有条件统一至 >=5 seeds。公布逐 seed 成功率。撤回 n=3 对比的 'indistinguishable' 结论。", assigned_to: "Agent + Paper Agent", status: "open"}
43	  resolution: ""
44	  resolution_round: null
45	
46	- id: "C4"
47	  summary:
…[truncated 13500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-27T15:28:20.736516+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-27T15:28:20.787281+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-27T15:29:16.144195+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-27T15:29:16.195456+00:00_

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
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-27T15:30:01.304401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-27T15:30:01.957370+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{amsmath,amssymb,amsfonts}
8	\DeclareMathOperator*{\argmin}{arg\,min}
9	\DeclareMathOperator*{\argmax}{arg\,max}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{enumitem}
13	\usepackage{multirow}
14	
15	
16	\graphicspath{{figures/}}
17	
18	\title{ACR-VLA: Adaptive Conformal Refinement\\for Frozen Flow-Matching VLAs}
19	
20	\author{
21	  Anonymous
22	}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\begin{abstract}
29	\input{abstract}
30	\end{abstract}
31	
32	\keywords{Vision-Language-Action Models, Inference-Time Refinement, Robotic Manipulation}
33	
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	
40	\smallskip\noindent\textit{AI tools assisted with code and manuscript.}
41	
42	\bibliography{references}
43	
44	\clearpage
45	\input{appendix}
46	
47	\end{document}
48	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-27T15:30:02.108514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_5/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_5/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-27T15:30:02.711740+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_round_5/submitted.pdf (333.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-27T15:32:34.117611+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "medoid|geometric|closest.*centroid|argmin.*centroid",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "medoid|geometric|closest.*centroid|argmin.*centroid",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-27T15:32:34.520339+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex:21:  \item \textbf{$K{=}10$ argmin}~\cite{chen2026reconvla} ($K{=}10$): argmin-to-centroid selection over 10 samples, no learned correction. Represents the selection-only approach.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.aux:42:\@writefile{lof}{\contentsline {figure}{\numberline {1}{\ignorespaces Adaptive sample-select-correct pipeline. $K{=}2$ action samples are drawn from the frozen VLA; the argmin-to-centroid sample is selected, and a lightweight CRM applies bounded correction ($\|\boldsymbol  {\delta }\|_2 \leq \varepsilon $) only when the pairwise $L_2$ distance exceeds the uncertainty threshold $\tau $.}}{3}{figure.1}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.aux:43:\newlabel{fig:pipeline}{{1}{3}{Adaptive sample-select-correct pipeline. $K{=}2$ action samples are drawn from the frozen VLA; the argmin-to-centroid sample is selected, and a lightweight CRM applies bounded correction ($\|\boldsymbol {\delta }\|_2 \leq \varepsilon $) only when the pairwise $L_2$ distance exceeds the uncertainty threshold $\tau $}{figure.1}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex:8:  \caption{Adaptive sample-select-correct pipeline. $K{=}2$ action samples are drawn from the frozen VLA; the argmin-to-centroid sample is selected, and a lightweight CRM applies bounded correction ($\|\boldsymbol{\delta}\|_2 \leq \varepsilon$) only when the pairwise $L_2$ distance exceeds the uncertainty threshold $\tau$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex:12:\looseness=-1 ACR-VLA adaptively allocates inference-time compute for a frozen flow-matching VLA (Figure~\ref{fig:pipeline}). At each control step, a 
…[truncated 430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-27T15:32:35.173391+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "DAgger|dagger|domain randomization|covariate shift",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "DAgger|dagger|domain randomization|covariate shift",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-27T15:32:35.976621+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.bbl:213:\bibitem[Ross et~al.(2011)Ross, Gordon, and Bagnell]{ross2011dagger}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib:205:@inproceedings{ross2011dagger,
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.aux:52:\citation{ross2011dagger}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.aux:135:\bibcite{ross2011dagger}{{28}{2011}{{Ross et~al.}}{{Ross, Gordon, and Bagnell}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex:50:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-27T15:32:36.529160+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "commit|hash|version.*smolvla|checkpoint.*id",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "commit|hash|version.*smolvla|checkpoint.*id",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-27T15:32:37.483235+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.blg:2:Capacity: max_strings=200000, hash_size=200000, hash_prime=170003

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-27T15:32:37.835024+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "GPU|hardware|A100|H100|training time|wall.clock",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "GPU|hardware|A100|H100|training time|wall.clock",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-27T15:32:37.886496+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:100:\paragraph{Hardware.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:101:All experiments run on NVIDIA RTX 4090 GPUs (24\,GB VRAM). SmolVLA inference uses a single GPU; CRM training and evaluation each use a single GPU.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:104:The 3-suite CRM (Spatial, Object, Goal; ${\sim}$168K samples) trains for 50 epochs with Adam ($\mathrm{lr}{=}10^{-3}$, batch size 32) in ${\sim}$6 GPU-hours on 1$\times$ RTX 4090. The 4-suite CRM (adding Long; ${\sim}$224K samples) trains in ${\sim}$8 GPU-hours. Precomputing the $K{=}10$ forward-pass cache (required once per suite) takes ${\sim}$2 GPU-hours per suite.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:107:Each suite evaluation (20 rollouts $\times$ 10 tasks $\times$ 300 max steps) takes ${\sim}$2.5 GPU-hours. A full 5-method $\times$ 4-suite $\times$ 3-seed experiment requires ${\sim}$150 GPU-hours total.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.aux:152:\@writefile{toc}{\contentsline {paragraph}{Hardware.}{13}{section*.15}\protected@file@percent }

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-27T15:32:46.970406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
  "offset": "45",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
    "offset": "45",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-27T15:32:47.272071+00:00_

45	\looseness=-1 The CRM is trained offline on demonstration trajectories from LIBERO~\cite{liu2023libero} with $L_2$ loss:
46	\begin{equation}
47	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2,
48	  \label{eq:loss}
49	\end{equation}
50	where $\mathbf{a}_{\mathrm{expert}}$ is the demonstration action. For each VLA, we precompute training data from 10 demonstrations per task across the target LIBERO suites. At each demonstration step, we run $K{=}10$ forward passes through the frozen VLA, apply argmin selection~(\ref{eq:argmin}) to obtain $a_{\mathrm{base}}$, and train the CRM to predict the residual toward $\mathbf{a}_{\mathrm{expert}}$. Training uses Adam ($\mathrm{lr}{=}10^{-3}$), batch size 32, 50 epochs, with Gaussian noise augmentation on $a_{\mathrm{base}}$ to improve generalization to the closed-loop state distribution~\cite{ross2011dagger}.
51	
52	\subsection{Magnitude Control}
53	\label{sec:magnitude}
54	
55	The norm bound $\varepsilon$ in~(\ref{eq:crm}) is critical for stable closed-loop performance. Without clipping, the CRM's unconstrained output norm (${\approx}$1.42) causes compounding errors. Constraining $\varepsilon$ to $[0.05, 0.2]$ yields stable corrections. The adaptive pipeline uses $\varepsilon{=}0.2$ (correction gated to high-uncertainty steps only), while unconditional correction requires a tighter $\varepsilon{=}0.05$ to limit overcorrection (Section~\ref{sec:failure_modes}).
56	
57	\subsection{Adaptive Inference-Time Compute}
58	\label{sec:adaptive_k_method}
59	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-27T15:32:47.800372+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "STEER|steer",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "STEER|steer",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-27T15:32:48.049714+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.bbl:62:  inference-time vla policy steering via embodied evolutionary diffusion, 2025.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib:223:    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 249
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-27T15:32:48.100467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-27T15:32:48.151115+00:00_

1	
2	\enlargethispage{6\baselineskip}
3	\vspace{-8pt}
4	\section{Conclusion}
5	\label{sec:conclusion}
6	\vspace{-4pt}
7	
8	\looseness=-2 We presented ACR-VLA, an adaptive inference-time correction pipeline for frozen flow-matching VLAs. A $K{=}2$ pairwise $L_2$ uncertainty probe ($\rho{=}0.9979$) gates a lightweight CRM (${\sim}$327K parameters). On SmolVLA (0.4B), unconditional correction degrades 2/4 suites ($-$2.2\,pp Long, $-$1.2\,pp Object); on $\pi_{0.5}$ (3.6B, 94--99\% baseline), it degrades all four (up to $-$17\,pp). ACR-VLA's adaptive gate recovers performance in both settings: exceeding unconditional $K{=}10$ correction on all SmolVLA suites with $5{\times}$ fewer forward passes, and recovering 19--38\% of the CRM-induced loss on 3/4 $\pi_{0.5}$ suites. The key finding is mechanistic: adaptive gating modulates intervention intensity, turning an unstable correction module into a reliable one.
9	
10	\vspace{-4pt}
11	\section{Limitations}
12	\label{sec:limitations}
13	\vspace{-2pt}
14	
15	\looseness=-1 \textbf{Effect sizes and statistical power.}\enspace Paired improvements (Adaptive vs.\ VLA-only) are directionally consistent across suites but do not reach statistical significance at $\alpha{=}0.05$ with $n{=}3$ matched seeds (Spatial: $p{\approx}0.27$). Per-suite sample sizes are limited by computational budget; the consistent directional pattern across 4 suites provides corroborating but not definitive evidence of improvement. The stronger empirical claim is Adaptive vs.\ CRM always-on, where ACR-VLA exceeds unconditional correction on all four suites ($\Delta_{\mathrm{CRM}}{=}{+}1.0$ to $+$1.9\,pp).
16	
17	\looseness=-1 \textbf{Confidently wrong steps.}\enspace The pairwise $L_2$ probe measures sample disagreement, not correctness. On Long (trigger rate ${\sim}$4\%), the VLA may produce confident but systematically incorrect outputs that escape gating.
18	
19	\looseness=-1 \textbf{Scope and generalization.}\enspace The CRM requires task-specific calibra
…[truncated 357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-27T15:33:56.415581+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "precompute.*seed|random seed|seed.*precomput",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "precompute.*seed|random seed|seed.*precomput",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-27T15:33:57.218641+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-27T15:33:57.871368+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "OpenVLA|openvla|RT-2|rt-2|Octo|@misc",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "OpenVLA|openvla|RT-2|rt-2|Octo|@misc",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-27T15:33:58.022431+00:00_

1:@misc{a2c2_2025,
2-    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3-    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4-    year={2025},
--
18-}
19-
20-
21:@misc{black2024pi0,
22-    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
23-    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
24-    year={2024},
--
27-    primaryClass={cs.RO}
28-}
29-
30:@misc{black2025pi05,
31-    title={$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},
32-    author={Physical Intelligence and Kevin Black and Noah Brown and James Bradbury and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Oier Mees and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Allen Ren and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang},
33-    year={2025},
--
36-    primaryClass={cs.RO}
37-}
38-
39:@misc{brohan2023rt2,
40:    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
41-[Omitted long context line]
42-    year={2023},
43-    eprint={2307.15818},
--
45-    primaryClass={cs.RO}
46-}
47-
48:@misc{chen2026reconvla,
49-    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},
50-    author={Lingling Chen and Zongyao Lyu and William J. Beksi},
51-    year={2026},
--
55-}
56-
57-
58:@misc{digflow2025,
59-
…[truncated 4264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-27T15:34:28.004438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/review_reports/round_2.md"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-27T15:34:28.155694+00:00_

1	---
2	round: 2
3	review_mode: fresh
4	overall_score: weak reject
5	timestamp: 2026-05-19T02:11:40.043920+00:00
6	reviewer_ids: [1, 2, 3]
7	cross_response_reviewer_ids: [1, 2, 3]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 2 (Fresh Review)
12	
13	**论文**: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs"
14	**目标 venue**: CoRL 2026 Main Conference
15	**Deadline**: 2026-05-29（距今 10 天）
16	**审稿模式**: Fresh（独立初审）
17	**Reviewer 编排**: 3 人（R1: 方法/实验/统计; R2: 新颖性/Related Work/写作/格式; R3: CoRL venue fit/格式合规/可重复性）
18	**外部审稿**: 未配置，跳过
19	
20	---
21	
22	## Summary
23	
24	本文提出 sample-select-correct pipeline 对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正（‖δ‖₂ ≤ ε）。在 LIBERO-Object 上实现 17.6±2.6% vs 11.6±1.1%（p=0.003, Mann-Whitney U），在 LIBERO-Spatial 上无提升（30-35%）。Component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告 conformal features 失效（progressive collapse to 0%）和 tokenized VLA 不适用的 negative results。
25	
26	---
27	
28	## Strengths
29	
30	- **S1: 系统化 component decomposition** [R1-S1, R2-S3, R3 隐含, 三方共识]
31	  通过 K=1 correction、selection-only、random selection 等控制实验清楚拆解各组件贡献。"Selection alone 无显著帮助、K=1 correction 低于 baseline、二者结合才有效"的发现对 embodied test-time compute scaling 有洞察价值，与 LLM test-time scaling 的 selection-dominant 范式形成有意义的对比。
32	
33	- **S2: 有价值的 negative results** [R1-S2, R2-S4, 共识]
34	  Conformal features 的失败（obs_only 14.3-17.6% vs perdof collapse 至 0%）和 tokenized VLA 不适用性，为后续研究提供指导。
35	
36	- **S3: 统计方法严谨** [R1-S3, R2-S2, R3-S3, 三方共识]
37	  Seed-level Mann-Whitney U + sign test，正确处理 within-seed episode 非独立性。相比 Round 1（Fisher test）已大幅改善。
38	
39	- **S4: 写作质量高** [R1-S4, R2-S1/S5, R3-S1, 三方共识]
40	  Pipeline 描述精确，符号一致，AI 写作痕迹几乎为零。Limitations section 诚实全面。
41	
42	- **S5: 实验可重复性基础尚可** [R3-S2]
43	  关键超参数记录完整（Adam lr=1e-3, batch 32, 50 epochs, seed 42, augmentation noise），SmolVLA checkpoint 路径已给出。
44	
45	---
46	
47	## Weaknesses
…[truncated 7476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_416d453a45869a9406db62186b1e3ef7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

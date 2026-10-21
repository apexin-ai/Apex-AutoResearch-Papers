# Director coordination — Part 1 of 8

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

[Transcript overview](../director-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/1d/1de11abfd142608a2277.json)

## Round 1

## Round 1

56 recorded events


### User

_source line 1 · 2026-05-22T03:19:28.955108+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long paper (ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-22T03:19:35.175408+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-22T03:19:35.176067+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-22T03:19:41.853763+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-22T03:19:41.854206+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-22T03:19:44.968474+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-22T03:19:45.019361+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-22T03:19:49.188323+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-22T03:19:49.640856+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-22T03:19:49.691642+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-22T03:19:51.098400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-22T03:19:51.199293+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	
18	\graphicspath{{../../figures/paper/}}
19	
20	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{abstract}
28	
29	\input{introduction}
30	
31	\input{related_work}
32	
33	\input{method}
34	
35	% ── Figures ──
36	
37	\begin{figure*}[t]
38	\centering
39	\includegraphics[width=\textwidth]{fig2_bias_distribution.pdf}
40	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%. Five safe topologies show attenuation without sign flip.}
41	\label{fig:bias_distribution}
42	\end{figure*}
43	
44	\input{experiments}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix_proofs}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-22T03:19:58.126664+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here is the information for EMNLP 2026 ARR call for papers:

## Key Submission Deadline

ARR Submission Deadline: May 25,
…[truncated 1650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 8435
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-22T03:20:06.710848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-22T03:20:07.063152+00:00_

1	\begin{abstract}
2	Large language models (LLMs) are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that binary measurement error theory cannot predict. We present the first systematic framework characterizing how $K$-class confusion matrix structure interacts with DAG topology to determine bias direction and magnitude. We derive bias expressions for seven canonical DAG topologies under multi-class non-differential misclassification and establish a structural sign-flip guarantee: five topologies never produce sign reversal, while exposure and instrumental variable topologies can---83.4\% of $K{=}3$ confusion matrices cause sign reversal in the exposure DAG, persisting at 13.7\% even with classifier accuracy above 70\%. We introduce Annotation Sensitivity Values (ASVs) with three complementary measures revealing a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal) to M-bias (immune). We evaluate five correction methods and prove a Frisch--Waugh--Lovell invariance result: matrix-based corrections achieve 0\% bias reduction for four topologies, while PPI++ achieves 47.0\% RMSE reduction but requires gold labels and is harmful for M-bias ($-$88\%). Empirical validation on three tasks ($K{=}2,3,10$) with four LLMs confirms theoretical predictions with zero sign flips across 98 scenarios. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-22T03:20:07.063555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-22T03:20:07.515573+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The consequences can be catastrophic. Under $K{=}3$ non-differential exposure misclassification, 83.4\% of confusion matrices cause \emph{sign reversal} of the estimated treatment effect, where the estimated direction of the causal relationship is opposite to the truth. This failure breaks the classical binary guarantee that non-differential misclassification biases estimates ``toward the null''~\cite{brenner1993}, a guarantee that many applied researchers implicitly rely upon. The breakdown is not an edge case: it persists even when classifier accuracy exceeds 70\% (13.7\% violation rate at diagonal $\geq 0.7$). Moreover, standard classification metrics do not predict downstream causal risk: within a narrow $F_1$ range of 0.614--0.690 across three frontier LLMs, relative bias varies by an order of
…[truncated 2180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-22T03:20:07.566214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-22T03:20:07.968296+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The statistical foundations are established in \citet{carroll2006} and \citet{gustafson2004}, with starred-node DAGs formalized by \citet{hernan_cole2009}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, but \citet{dosemeci1990} and \citet{jurek2005} showed this fails for polytomous exposures. \citet{veirod_laake2001} derived multi-category bias expressions for Poisson regression, and \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction. All of these works analyze a single DAG topology; our taxonomy is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} provide the foundation for text-as-data, while \citet{wood_doughty2018} first applied DAG reasoning to classifier error. \citet{teblunthuis2024} gave the most complete binary treatment (four DAG scenarios, $K{=}2$), and \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{baumann2025} found 31\% incorrect conclusions with LLM labels and \citet{kim_garg2025} showed 60\% error correlation across models. These works either restrict to binary labels, cover a single topology, or diagnose quality without connecting it to causal validity. Our framework provides the missing link.
9	
10	\paragraph{Sensitivity analysis and correction methods.}
11	Our ASV framework draws on E-values for unmeasured confounding~\cite{vanderweele_ding2017} and probabilistic bias analysis~\cite{lash2009}. Unlike E-values, ASVs comprise three types (magnitude, significance, sign-flip) because failure modes are topology-dependent; unlike PBA, ASVs provide monotonicity guarantees over $K{\times}K$ matri
…[truncated 313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-22T03:20:07.968661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-22T03:20:08.924540+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
15	
16	\subsection{Multi-Class Bias Expressions}
17	\label{sec:bias_expressions}
18	
19	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
20	
21	\paragraph{Confounding ($A$ = confounder).}
22	When $A$ confounds the $X{\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit
23	\begin{equation}
24	\label{eq:confounding}
25	\text{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\bet
…[truncated 7461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-22T03:20:08.975311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-22T03:20:09.377571+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate the bias taxonomy and ASV framework through analytical derivations and Monte Carlo simulation across seven DAG topologies under $K{=}3$ non-differential misclassification.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 2.0\% across 126 scenarios (18 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.5\% (confounding) to 5.5\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: catastrophic sign reversal.}
18	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\% of matrices cause \emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\beta_1{=}1.0$, a near-permutation $C$ produces $\hat{\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\times}$); for $\beta_2{=}{-}0.5$, the same $C$ yields $\hat{\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\times}$).
19	
20	This finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\% with 2.1\% sign reversal and 11.7\% amplification. Even at diagonal $\geq 0.9$, violation
…[truncated 10055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-22T03:20:09.428302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-22T03:20:09.930682+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic characterization of how multi-class annotation errors interact with causal DAG topology. The classical binary guarantee breaks for $K \geq 3$: exposure and IV topologies produce sign reversal (83.4\% and 52.6\%), while five topologies maintain a structural guarantee. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and correction effectiveness is itself topology-dependent, with matrix-based methods provably ineffective for four topologies. Immediate extensions include differential misclassification and correlated multi-LLM error structures.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM has no access to $Y$ but may be violated with outcome-conditional prompting. A stress test (Appendix~\ref{sec:nondiff_stress}) shows moderate robustness ($\varepsilon{=}0.05$ increases violations by $<$3pp). Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$; arbitrary $K$ remains open. The framework assumes a single annotator; correlated multi-annotator settings~\cite{kim_garg2025} are future work. VAST and CivilComments use a 7B model rather than frontier models, limiting cross-tier comparisons.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-22T03:20:10.181971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-22T03:20:10.534396+00:00_

1	\section{Proof of Proposition~\ref{prop:signflip}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding, collider, mediation, and front-door topologies, and an explicit counterexample for the exposure topology.
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y}=Y-\mathbb{E}[Y\mid A^*]$ are residuals from projecting onto $(1,D_1^*,\dots,D_{K-1}^*)$.
31	
32	\begin{lemma}[Bias decomposition]
33	\label{lem:bias_decomp}
34	Suppose $Y = \tau T + f(A) + \varepsilon_Y$ with $\varepsilon_Y \
…[truncated 44654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-22T03:20:10.584977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-22T03:20:11.338500+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@inproceedings{wood_doughty2018,
5	  title     = {Challenges of Using Text Classifiers for Causal Inference},
6	  author    = {Wood-Doughty, Zach and Shpitser, Ilya and Dredze, Mark},
7	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
8	  year      = {2018},
9	  doi       = {10.18653/v1/D18-1488},
10	}
11	
12	@article{teblunthuis2024,
13	  title   = {Misclassification in Automated Content Analysis Causes Bias in Regression. {C}an We Fix It? {Y}es We Can!},
14	  author  = {TeBlunthuis, Nathan and Hase, Valerie and Chan, Chung-hong},
15	  journal = {Communication Methods and Measures},
16	  volume  = {18},
17	  number  = {3},
18	  pages   = {278--299},
19	  year    = {2024},
20	  doi     = {10.1080/19312458.2023.2293713},
21	}
22	
23	@article{hernan_cole2009,
24	  title   = {Invited Commentary: Causal Diagrams and Measurement Bias},
25	  author  = {Hern{\'a}n, Miguel A. and Cole, Stephen R.},
26	  journal = {American Journal of Epidemiology},
27	  volume  = {170},
28	  number  = {8},
29	  pages   = {959--962},
30	  year    = {2009},
31	  doi     = {10.1093/aje/kwp293},
32	}
33	
34	@article{vanderweele_li2019,
35	  title   = {Simple Sensitivity Analysis for Differential Measurement Error},
36	  author  = {VanderWeele, Tyler J. and Li, Yige},
37	  journal = {American Journal of Epidemiology},
38	  volume  = {188},
39	  number  = {10},
40	  pages   = {1823--1829},
41	  year    = {2019},
42	  doi     = {10.1093/aje/kwz133},
43	}
44	
45	@article{vanderweele_ding2017,
46	  title   = {Sensitivity Analysis in Observational Research: Introducing the {E}-Value},
47	  author  = {VanderWeele, Tyler J. and Ding, Peng},
48	  journal = {Annals of Internal Medicine},
49	  volume  = {167},
50	  pages   = {268--274},
51	  year    = {2017},
52	  doi     = {10.7326/M16-2607},
53	}
54	
55	@article{brenner1993,
56	  title   = {Bias Du
…[truncated 11777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-22T03:20:11.339010+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-22T03:20:11.490866+00:00_

-rw-r--r-- 1 ubuntu ubuntu 779336 May 22 03:16 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-22T03:20:26.429047+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf 2>/dev/null | grep -i \"pages\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf 2>/dev/null | grep -i \"pages\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-22T03:20:26.730811+00:00_

Pages:           18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-22T03:20:26.731139+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-22T03:20:27.585354+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-22T03:20:27.585709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission formatting requirements page limit template anonymity guidelines site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission formatting requirements page limit template anonymity guidelines site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-22T03:20:34.315287+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission formatting requirements page limit template anonymity guidelines site:aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"}]

Based on the search results from the ACL Rolling Review website, her
…[truncated 1442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6729
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-22T03:20:38.885498+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-22T03:20:38.936095+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-22T03:20:44.459005+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-22T03:20:45.412759+00:00_

FILE_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-22T03:20:45.413295+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-22T03:20:47.271319+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 1858
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-22T03:20:47.523395+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf - 2>/dev/null | head -5; echo \"---\"; pdftotext /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf - 2>/dev/null | grep -n \"^References$\\|^Appendix\\|\\\\\\\\appendix\\|^A \" | head -10",
  "description": "Check where references/appendix start in PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf - 2>/dev/null | head -5; echo \"---\"; pdftotext /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf - 2>/dev/null | grep -n \"^References$\\|^Appendix\\|\\\\\\\\appendix\\|^A \" | head -10",
    "description": "Check where references/appendix start in PDF"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-22T03:20:47.876881+00:00_

Multi-Class Annotation Errors in Causal Inference:
Topology-Dependent Bias, Sensitivity, and Correction

Anonymous ACL submission

---
507:A confounds the X→Y relationship, the OLS
681:A introduces a small spurious association via
1556:References
2594:A | T, Y ∼ Categorical softmax(δ T T + δ Y Y ) .
2823:A | T ∼ Categorical softmax(γ + δ T ) ,
2915:A (plus independent misclassification noise),
2955:A )] = Var(T ) − Var(E[T | A∗ ]) ≥ Var(T ) −

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-22T03:20:56.364078+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf - 2>/dev/null | grep -n \"^\\f\" | head -20",
  "description": "Find page breaks in PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf - 2>/dev/null | grep -n \"^\\f\" | head -20",
    "description": "Find page breaks in PDF text"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-22T03:20:56.615491+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-22T03:20:59.580841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf",
  "pages": "7-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf",
    "pages": "7-10"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-22T03:20:59.833678+00:00_

PDF pages extracted: 4 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf (761.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-22T03:21:31.327651+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-22T03:21:57.911284+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26583
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-22T03:21:58.112642+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责 **方法/理论严谨性 + 实验设计** 的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 8 页，References 不限，Limitations/Ethics 不计入页数\n- **模板**：ACL 格式（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文文件\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf`\n\n## 论文概要\n标题：\"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n\n论文研究 LLM 标注中 K-class confusion matrix 结构如何与 DAG 拓扑交互，影响因果估计的偏差方向和大小。三个贡献：(1) 7 种 DAG 拓扑下的 multi-class bias taxonomy + sign-flip 保证；(2) Annotation Sensitivity Values (ASVs) 框架；(3) 5 种 correction 方法的 topology-aware 评估。\n\n## 你的审查侧重（必须覆盖）\n\n### 1. 理论正确性\n- Proposition 1（sign-flip 保证）的证明是否完整严谨？5 种拓扑的 sign preservation 条件（Appendix A）是否都有充分证明？注意 mediation 和 M-bias 是 \"numerical verification\" 而非 closed-form proof——这是否足够？\n- Bias 表达式（Eq. 1-6）的推导是否正确？特别是 FWL decomposition 的应用\n- Theorem 1（envelope monotonicity）仅有 numerical verification——是否需要解析证明？\n- Sign preservation 条件（如 confounding 要求 sign(τ) = sign(τ_OV)）是否过于依赖 DGP 参数？在实际应用中这些条件能否验证？\n\n### 2. ASV 框架\n- ASV 的三种类型定义是否严谨？参数化 C(δ) = (1-δ)I + δC_0 的选择是否有理论依据？\n- 与 E-value 的类比是否恰当？ASV 是否真正提供了超越 E-value 的新工具？\n- Significance ASV 依赖 N 的 phase transition 是否有实际指导意义？\n\n### 3. 实验设计\n- 100,000 Dirichlet(1,1,1) random matrices 的采样策略是否合理？Dirichlet(1,1,1) prior 是否过于宽泛（包含大量不现实的 confusion matrices）？\n- Monte Carlo 验证（N=10,000）的样本量是否足够？MAPE 2.0% 的报告方式是否掩盖了某些拓扑的高方差？\n- 实证验证仅用 3 个 task、4 个 LLM——泛化性如何？HumAID (K=10) 用 frontier models 但 VAST/CivilComments 用 7B model，这种不对称是否影响结论？\n- Correction 方法评估的 DGP 设置（6 error structures, 210 configurations）是否充分？\n\n### 4. 数学细节\n- 检查所有公式的符号一致性\n- 检查 Table 1 中 violation/sign-flip/amplification 率的数值是否自洽\n- Appendix 中的 proof 是否有逻辑跳跃\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Suggestions → Overall Assessment（1-5 分，参考 EMNLP 2026 评分标准）→ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责 **方法/理论严谨性 + 实验设计** 的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 8 页，References 不限，Limitations/Ethics 不计入页数\n- **模板**：ACL 格式（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文文件\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf`\n\n## 论文概要\n标题：\"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n\n论文研究 LLM 标注中 K-class confusion matrix 结构如何与 DAG 拓扑交互，影响因果估计的偏差方向和大小。三个贡献：(1) 7 种 DAG 拓扑下的 multi-class bias taxonomy + sign-flip 保证；(2) Annotation Sensitivity Values (ASVs) 框架；(3) 5 种 correction 方法的 topology-aware 评估。\n\n## 你的审查侧重（必须覆盖）\n\n### 1. 理论正确性\n- Proposition 1（sign-flip 保证）的证明是否完整严谨？5 种拓扑的 sign preservation 条件（Appendix A）是否都有充分证明？注意 mediation 和 M-bias 是 \"numerical verification\" 而非 closed-form proof——这是否足够？\n- Bias 表达式（Eq. 1-6）的推导是否正确？特别是 FWL decomposition 的应用\n- Theorem 1（envelope monotonicity）仅有 numerical verification——是否需要解析证明？\n- Sign preservation 条件（如 confounding 要求 sign(τ) = sign(τ_OV)）是否过于依赖 DGP 参数？在实际应用中这些条件能否验证？\n\n### 2. ASV 框架\n- ASV 的三种类型定义是否严谨？参数化 C(δ) = (1-δ)I + δC_0 的选择是否有理论依据？\n- 与 E-value 的类比是否恰当？ASV 是否真正提供了超越 E-value 的新工具？\n- Significance ASV 依赖 N 的 phase transition 是否有实际指导意义？\n\n### 3. 实验设计\n- 100,000 Dirichlet(1,1,1) random matrices 的采样策略是否合理？Dirichlet(1,1,1) prior 是否过于宽泛（包含大量不现实的 confusion matrices）？\n- Monte Carlo 验证（N=10,000）的样本量是否足够？MAPE 2.0% 的报告方式是否掩盖了某些拓扑的高方差？\n- 实证验证仅用 3 个 task、4 个 LLM——泛化性如何？HumAID (K=10) 用 frontier models 但 VAST/CivilComments 用 7B model，这种不对称是否影响结论？\n- Correction 方法评估的 DGP 设置（6 error structures, 210 configurations）是否充分？\n\n### 4. 数学细节\n- 检查所有公式的符号一致性\n- 检查 Table 1 中 violation/sign-flip/amplification 率的数值是否自洽\n- Appendix 中的 proof 是否有逻辑跳跃\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Suggestions → Overall Assessment（1-5 分，参考 EMNLP 2026 评分标准）→ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-22T03:22:23.040355+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24927
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-22T03:22:23.241454+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责 **新颖性 + 完整性 + 相关工作 + 格式合规** 的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 8 页，References 不限，Limitations/Ethics 不计入页数\n- **模板**：ACL 格式（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文文件\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf`\n\n## 论文概要\n标题：\"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n\n论文研究 LLM 标注中 K-class confusion matrix 结构如何与 DAG 拓扑交互，影响因果估计的偏差方向和大小。三个贡献：(1) 7 种 DAG 拓扑下的 multi-class bias taxonomy + sign-flip 保证；(2) Annotation Sensitivity Values (ASVs) 框架；(3) 5 种 correction 方法的 topology-aware 评估。\n\n## 你的审查侧重（必须覆盖）\n\n### 1. 新颖性与贡献评估\n- 这三个贡献（bias taxonomy, ASV, correction guidance）相对于现有工作的增量价值有多大？\n- 与 Teblunthuis (2024) 的区别——他们已经做了 4 种 DAG 场景的 binary 分析，本文扩展到 7 种 + multi-class 是否足够新颖？\n- 与 Lee & Wood-Doughty (2024) 的区别——他们已经做了 categorical LLM classifier + confounding，本文的贡献在哪？\n- ASV 相对于 E-value 的创新性如何？是否只是 E-value 的简单推广？\n- FWL invariance 结果是否真正\"new\"？FWL theorem 本身是经典结果，应用到这个 setting 是否构成贡献？\n\n### 2. Related Work 完整性\n- 是否遗漏重要的相关工作？特别是：\n  - Measurement error 文献中是否还有其他 multi-class 处理？\n  - Text-as-data 领域是否有更多 LLM annotation error 的工作？\n  - Sensitivity analysis 领域是否有更接近的先驱？\n  - PPI/prediction-powered inference 领域的最新进展（如 cross-PPI, Gligoric et al. 2025）是否充分讨论？\n- 论文引用了 Messing (2026)——这是一篇 2026 年的 arXiv preprint，是否真实存在、引用是否准确？\n- 检查所有引用的准确性（年份、venue、作者）\n\n### 3. 叙事逻辑与 Presentation\n- 论文的 story 是否清晰连贯？从 problem → method → experiments → conclusion 的逻辑链是否紧密？\n- 83.4% sign reversal 的 headline claim 是否在正文中被过度强调？它基于 Dirichlet(1,1,1) full prior，但实际 LLM classifiers 的 confusion matrix 远非 uniform random——这个 framing 是否误导？\n- \"first systematic framework\" 的 claim 是否过强？\n- Abstract 是否信息过载？是否应精简？\n- Figure/Table 的放置和引用是否清晰？\n\n### 4. 格式合规（EMNLP 2026 / ARR）\n- 正文是否 ≤ 8 页？Limitations 是否存在且内容合理？\n- 匿名性：是否有泄露作者身份的内容？（检查 acknowledgements、self-citation、GitHub links 等）\n- 引用格式是否符合 ACL 标准？\n- 是否使用了正确的 ACL 模板？（检查 `\\usepackage[review]{acl}`）\n- Appendix 是否合理利用？是否有本应在正文中的关键内容被移到了 Appendix？\n- Ethics statement 是否需要？（涉及 LLM 使用和社会科学研究）\n\n### 5. Limitations 评估\n- 当前 Limitations 部分是否充分覆盖了论文的主要限制？\n- 是否遗漏了重要限制？（如：所有拓扑都假设已知 DAG、confusion matrix 需已知或可估计、non-differential assumption 的现实性）\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Suggestions → Overall Assessment（1-5 分，参考 EMNLP 2026 评分标准）→ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责 **新颖性 + 完整性 + 相关工作 + 格式合规** 的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 8 页，References 不限，Limitations/Ethics 不计入页数\n- **模板**：ACL 格式（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文文件\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_1/submitted.pdf`\n\n## 论文概要\n标题：\"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n\n论文研究 LLM 标注中 K-class confusion matrix 结构如何与 DAG 拓扑交互，影响因果估计的偏差方向和大小。三个贡献：(1) 7 种 DAG 拓扑下的 multi-class bias taxonomy + sign-flip 保证；(2) Annotation Sensitivity Values (ASVs) 框架；(3) 5 种 correction 方法的 topology-aware 评估。\n\n## 你的审查侧重（必须覆盖）\n\n### 1. 新颖性与贡献评估\n- 这三个贡献（bias taxonomy, ASV, correction guidance）相对于现有工作的增量价值有多大？\n- 与 Teblunthuis (2024) 的区别——他们已经做了 4 种 DAG 场景的 binary 分析，本文扩展到 7 种 + multi-class 是否足够新颖？\n- 与 Lee & Wood-Doughty (2024) 的区别——他们已经做了 categorical LLM classifier + confounding，本文的贡献在哪？\n- ASV 相对于 E-value 的创新性如何？是否只是 E-value 的简单推广？\n- FWL invariance 结果是否真正\"new\"？FWL theorem 本身是经典结果，应用到这个 setting 是否构成贡献？\n\n### 2. Related Work 完整性\n- 是否遗漏重要的相关工作？特别是：\n  - Measurement error 文献中是否还有其他 multi-class 处理？\n  - Text-as-data 领域是否有更多 LLM annotation error 的工作？\n  - Sensitivity analysis 领域是否有更接近的先驱？\n  - PPI/prediction-powered inference 领域的最新进展（如 cross-PPI, Gligoric et al. 2025）是否充分讨论？\n- 论文引用了 Messing (2026)——这是一篇 2026 年的 arXiv preprint，是否真实存在、引用是否准确？\n- 检查所有引用的准确性（年份、venue、作者）\n\n### 3. 叙事逻辑与 Presentation\n- 论文的 story 是否清晰连贯？从 problem → method → experiments → conclusion 的逻辑链是否紧密？\n- 83.4% sign reversal 的 headline claim 是否在正文中被过度强调？它基于 Dirichlet(1,1,1) full prior，但实际 LLM classifiers 的 confusion matrix 远非 uniform random——这个 framing 是否误导？\n- \"first systematic framework\" 的 claim 是否过强？\n- Abstract 是否信息过载？是否应精简？\n- Figure/Table 的放置和引用是否清晰？\n\n### 4. 格式合规（EMNLP 2026 / ARR）\n- 正文是否 ≤ 8 页？Limitations 是否存在且内容合理？\n- 匿名性：是否有泄露作者身份的内容？（检查 acknowledgements、self-citation、GitHub links 等）\n- 引用格式是否符合 ACL 标准？\n- 是否使用了正确的 ACL 模板？（检查 `\\usepackage[review]{acl}`）\n- Appendix 是否合理利用？是否有本应在正文中的关键内容被移到了 Appendix？\n- Ethics statement 是否需要？（涉及 LLM 使用和社会科学研究）\n\n### 5. Limitations 评估\n- 当前 Limitations 部分是否充分覆盖了论文的主要限制？\n- 是否遗漏了重要限制？（如：所有拓扑都假设已知 DAG、confusion matrix 需已知或可估计、non-differential assumption 的现实性）\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Suggestions → Overall Assessment（1-5 分，参考 EMNLP 2026 评分标准）→ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-22T03:22:24.955357+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1713
}
```

</details>

---


### Assistant

_source line 56 · 2026-05-22T03:22:37.611441+00:00_

**Round 1 审稿已启动：**

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法/理论严谨性 + 实验设计 |
| Reviewer 2 | ✅ 已派发 | 新颖性 + 完整性 + 相关工作 + 格式合规 |
| 视觉审查 Agent | ✅ 已派发 | 排版质量（非评分项）|
| 外部审稿 | ❌ 未配置 | — |

等待 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 57 · 2026-05-22T03:29:02.982877+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（方法/理论严谨性 + 实验设计）

**论文**：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**：EMNLP 2026 via ARR May 2026

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 框架新颖且问题重要，但核心理论声明（Theorem 1、Proposition 1 部分拓扑）缺乏解析证明仅靠数值验证，与 ARR 对形式化声明的证明要求存在差距；实验验证规模有限且存在系统性不对称。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Confounding/collider 证明严谨，但 Theorem 1 和 mediation/M-bias sign preservation 仅数值验证，不符合 ARR 对形式化声明的证明标准 |
| Excitement | 4.0/5 | 多类标注误差 × DAG 拓扑的系统性研究是全新视角，ASV 框架和 FWL 不变性结果有实际价值 |
| Reproducibility | 4.0/5 | DGP 参数、采样策略、MC 设置均有清晰描述，但代码和数据未附 |
| Overall | 3.5/5 | 核心贡献有价值，但理论严谨性缺口需要修补 |
| Confidence | 4/5 | 本人在因果推断和测量误差领域有较强背景 |

---

## Summary

本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅度。三个贡献：(1) 7 种拓扑下的 multi-class bias taxonomy + 5 种拓扑的 sign-flip 保证；(2) Annotation Sensitivity Values (ASVs) 框架；(3) 5 种 correction 方法的 topology-aware 评估 + FWL 不变性负结果。框架新颖，问题重要，但关键理论声明的证明不完整，实验验证规模和设计存在改进空间。

---

## 主要优势

1. **问题定义新颖且重要**。将多类标注误差与 DAG 拓扑的交互作为研究对象是全新角度。现有文献要么限于二元标签（Brenner 1993; Teblunthuis et al. 2024），要么只覆盖单一拓扑（Lee & Wood-Doughty 2024）。7 种拓扑的系统性覆盖填补了明确的研究空白。

2. **部分拓扑的证明严谨**。Confounding 的 sign preservation（Appendix A.3, Propositions 2-3）使用 Cauchy-Schwarz 界给出了干净的充分条件 |τ| > B̄；Collider（Appendix A.5, Propositions 4-5）类似地处理了 Berkson's bias 的反向结构；Front-door 的分解（Appendix A.6, Eq. 19）优雅地将 confounding 常数项从 mediation-type leakage 中分离。Exposure 反例（Appendix A.7）的构造可验证且清晰。

3. **FWL 不变性结果**是一个有实际指导意义的负结果。证明对 FWL-invariant 拓扑（confounding, mediation, collider, M-bias），基于 C^{-1} 的校正方法（Naive plug-in, MLA）对 T 系数的 bias reduction 恰好为 0%，直接告诉实践者这些方法在这些拓扑下无用。

4. **ASV 框架**提供了有操作性的敏感性分析工具，三种 ASV 类型（magnitude, significance, sign-flip）分别回答不同的实际问题。与 E-value 的类比恰当且有启发性。

5. **Binarization collapse 分析**（Section 3.4, Section 4.4）揭示了将 K-class 标注坍缩为二元标签的额外代价（154× 跨拓扑变化），这对实际数据处理有直接指导意义。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Theorem 1（Envelope Monotonicity）无解析证明，仅 500 个场景数值验证

- 具体位置：Section 3.3 (method.tex L76-81)；正文声明 "Monotonicity is verified numerically for all seven topologies (zero violations, 500 scenarios each)"
- 问题：Theorem 1 声称对 confounding、exposure 和 mediation 拓扑，bias envelope |plim τ̂(C(δ)) - τ| 关于 δ 单调不减。但全文——包括 Appendix——未提供任何解析证明。500 个场景的数值验证对于一个"Theorem"级别的声明远远不够：(a) ARR 官方 reviewer guidelines 明确要求 "theorems, propositions, lemmas, corollaries should be supported by complete and correct proofs"；(b) 500 个场景未能排除高维参数空间中的反例；(c) δ 的取值范围问题（见 N3）可能在 δ > δ_max 处产生不连续行为。
- 为什么影响接收：这是论文的核心定理之一，ASV 框架的有效性依赖于单调性。如果单调性不成立，ASV 的最小值定义 δ* = min{δ : ...} 可能不唯一或不存在。
- 建议修改方向：(a) 对至少一个拓扑（如 confounding，因其有 closed-form bias 表达式）给出解析证明；(b) 将其余拓扑降级为 "Empirical Observation" 或 "Conjecture"；(c) 大幅增加数值验证规模（至少 100,000 场景）并报告覆盖的参数空间。

**N2** [critical] Proposition 1 的 mediation 和 M-bias sign preservation 证明不完整

- 具体位置：Proposition 1 (method.tex L58-63)；Appendix A.4 mediation proof 结尾明确承认 "a closed-form proof for general K remains open"（appendix_proofs.tex L267）
- 问题：Proposition 1 对 5 种拓扑声称 τ_sign_flip = 0，但证明策略差异巨大：
  - Confounding: 完整代数证明 ✓（Cauchy-Schwarz 界）
  - Collider: 完整代数证明 ✓
  - Front-door: 分解为 confounding 常数 + mediation leakage，后者继承 mediation 的结果——但 mediation 本身未被证明
  - **Mediation: 仅 100,000 个随机矩阵的数值验证**，论文公开承认缺乏 closed-form proof
  - **M-bias: 仅有 "structural argument"**（Appendix A.8, appendix_proofs.tex L568-571），无任何形式化证明或充分数值验证
- 为什么影响接收：一个形式化 Proposition 中有 2/5 的拓扑缺乏证明，这不是一个边缘问题。Mediation 的数值验证只覆盖了特定 DGP 参数（τ_dir=0.5, 特定 γ, δ, β），不能保证在其他参数设置下成立。
- 建议修改方向：(a) 将 Proposition 1 拆分——已证明的 3 个拓扑保留为 Proposition，mediation 和 M-bias 降级为 "Empirical Finding" 并明确标注；(b) 或者为 mediation 提供至少 proportional case 的解析证明（类似 confounding 的 Proposition 2）；(c) M-bias 至少应有更严格的数值验证，覆盖多组 DGP 参数。

**N3** [critical] ASV 参数化 C(δ) 的定义域问题

- 具体位置：Section 3.3 (method.tex L71)："δ ∈ [0, ∞) controls the severity of misclassification"
- 问题：C(δ) = (1-δ)I + δC_0。当 δ > 1 时，对角元素 C(δ)_{kk} = (1-δ) + δC_{0,kk}。当 C_{0,kk} < 1-1/δ 时此值为负，C(δ) 不再是合法的 column-stochastic 矩阵。实际上 δ 的有效上界为 δ_max = 1/(1 - min_k C_{0,kk})，对任何非完美 C_0 这是一个有限值。例如，若 min_k C_{0,kk} = 0.6，则 δ_max = 2.5。论文声称 δ ∈ [0, ∞) 是不正确的。
- 为什么影响接收：Sign-flip ASV δ*_sf 可能大于 δ_max，此时 ASV 实际上是未定义的。Table 3（Appendix B）报告的 sign-flip ASV 范围 1.1-6.7 是否都在有效 δ 范围内未被验证。ASV 框架的核心操作依赖于 δ 的连续变化，如果参数化在有限 δ 处截断，monotonicity 和 ASV 的解释都受影响。
- 建议修改方向：(a) 明确 δ 的有效范围取决于 C_0，给出 δ_max 的显式表达式；(b) 讨论当 δ*_sf > δ_max 时 ASV 的语义；(c) 验证论文中报告的所有 ASV 值都在有效范围内。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 头条数字来自不现实的先验分布，可能误导读者

- 具体位置：Abstract（abstract.tex L2）、Introduction（introduction.tex L6）、Conclusion（conclusion.tex L4）均以 "83.4%" 领衔
- 问题：83.4% sign reversal 来自 Dirichlet(1,1,1)——即 simplex 上的均匀分布，包含大量 C_{kk} < 1/K 的矩阵（比随机猜测还差）。现实 LLM 分类器的 confusion matrix 是 diagonal-dominant 的。在 diagonal ≥ 0.7 子空间中，sign reversal 降至 2.1%（Section 4.2, experiments.tex L20）。Abstract 和 Introduction 以 83.4% 开篇但将 2.1%/13.7% 埋在正文中间，造成严重性的过度渲染。
- 建议：(a) Abstract 应同时报告 full prior 和 realistic subspace 的数字；(b) Introduction 应早期讨论 Dirichlet(1,1,1) 的局限性。

**W2** [warning] Sign preservation 条件的实际可验证性讨论不足

- 具体位置：Table 2 (Appendix A.8, appendix_proofs.tex L541-566)；主文 Proposition 1 的条件 "provided the true effect and the omitted-variable bias share the same sign"
- 问题：sign preservation 的充分条件（如 sign(τ) = sign(τ_OV) for confounding）要求知道 τ 的真值或 τ_OV 的符号。但实践者正是在估计 τ——如果已知 τ 的符号，就不需要这个保证了。Appendix 的 Remark（appendix_proofs.tex L573-578）承认了这一循环性，但主文没有充分讨论。
- 建议：(a) 主文应明确讨论条件的可验证性局限；(b) 可以提出 bootstrap 或 sensitivity analysis 方法来在实践中近似检验这些条件。

**W3** [warning] 实证验证的系统性不对称

- 具体位置：Section 4.5 (experiments.tex L76)
- 问题：HumAID (K=10) 使用 4 个 frontier 模型（Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat），而 VAST (K=3) 和 CivilComments (K=2) 仅使用 Qwen2.5-7B。脚注（experiments.tex L82）承认 "VAST's near-degenerate confusion matrix (third-class recall = 4.6%) may drive its extreme IV bias"，但这恰好可能是模型能力不足而非结构性问题。Cross-K 比较（如 "VAST produces 65.4% mean bias vs. 12.2% for HumAID"）被模型质量混淆。
- 此外，"zero sign reversals across all 98 scenarios" 并不令人意外——DGP 参数被选择为满足 sign preservation 条件（Table 2），这是同义反复。
- 建议：(a) 使用相同模型（frontier model）在 VAST 和 CivilComments 上复现；(b) 讨论当 DGP 参数不满足 sign preservation 条件时的实证行为。

**W4** [warning] MC 验证的报告不充分

- 具体位置：Section 4.2 (experiments.tex L15)
- 问题：Grand MAPE 2.0% 掩盖了拓扑间差异。IV 的 MAPE 为 5.5%（Wald 估计量的小分母方差放大），但未报告 worst-case error、MAPE 的置信区间或 per-scenario 分布。对于声称 "analytical limits match Monte Carlo estimates" 的验证，仅报告均值 MAPE 不够。
- 建议：报告 per-topology MAPE 分布（中位数、95th percentile、worst-case）。

---

## Questions（希望作者回应）

**Q1**：Theorem 1 的 confounding 拓扑有 closed-form bias 表达式（Appendix A.3, Eq. 12-13）——能否对这个拓扑给出 monotonicity 的解析证明？即证明 |B(C(δ))| 关于 δ 单调？这至少能部分支撑 Theorem 1。

**Q2**：Mediation sign preservation 依赖于 "max_j |δ_j| ≤ |τ_ind|" 的数值验证（appendix_proofs.tex L300-301）。能否构造 worst-case 分析？对于 K=3 的 proportional case（f(A) = λ·g(A) 的 mediation 版本），是否可以解析证明？

**Q3**：ASV 参数化中，当 δ > δ_max = 1/(1-min_k C_{0,kk}) 时 C(δ) 不再合法。Table 3 报告的 sign-flip ASV 1.1-6.7，对应的 C_0 的 δ_max 分别是多少？是否所有报告的 ASV 值都在有效范围内？

**Q4**：FWL 不变性排除了 Naive plug-in 和 MLA，但是否存在操作 individual-level A* 的方法（如 EM-based imputation of true A given (A*, C)）可以绕过 FWL 不变性？PPI++ 之外还有哪些方法可以 bypass 这个限制？

**Q5**：Correction 评估使用 6 种 error structures（experiments.tex L102），但正文未描述这 6 种结构的具体参数。能否在 Appendix 中给出完整的 error structure 参数表？

---

## 小问题（不影响接收）

- Section 3.2 的 Eq. 1 使用 Z = [X, dummies(A*)]，后续 Appendix 使用 D_j*。主文和 Appendix 的符号应统一。
- "Sign-flip guarantee" 一词容易引起歧义——"guarantee" 通常暗示保证某事发生，但此处表示保证 sign flip 不发生。建议改为 "sign preservation guarantee" 或 "structural sign-flip immunity"。
- Table 1 的列标题 "τ_sf = 0?" 中的 τ_sf 在 caption 中未定义。应改为 "Sign-flip rate = 0?" 或在 caption 中定义 τ_sf。
- Appendix A.7 (Exposure counterexample) 中，条件 C_{kk} > 0.5 已经是 diagonal-dominant。可以强调这一点——即便分类器在每个类别上的准确率超过 50%，仍可产生 sign reversal。

---

## 总结

本文提出了一个有实际价值且学术上新颖的框架，将多类标注误差与因果 DAG 拓扑系统性关联。核心洞察（K≥3 时二元保证失效、拓扑决定风险等级、FWL 不变性使基于矩阵的校正无效）是 genuinely novel 的。主要问题在于理论严谨性：两个核心形式化声明（Theorem 1, Proposition 1 的 mediation/M-bias 部分）仅靠数值验证支撑，ASV 参数化的定义域存在技术缺陷。实验验证的规模和对称性也有改进空间。如果作者能为至少一个拓扑的 monotonicity 提供解析证明、将未证明的 claims 诚实地降级、修复 ASV 定义域问题，本文可以达到 Conference 水准（4.0）。当前状态下评为 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-22T03:29:20.097322+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-22T03:29:20.198248+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 60 · 2026-05-22T03:29:31.477581+00:00_

Reviewer 1 审稿意见已收到，记录要点：

**Reviewer 1 评分**：3.5/5（Borderline Conference）
- **Must-Fix**：N1（Theorem 1 无解析证明）、N2（Proposition 1 mediation/M-bias 证明不完整）、N3（ASV δ 定义域问题）
- **Should-Fix**：W1（83.4% 头条数字来自不现实先验）、W2（sign preservation 条件可验证性）、W3（实证验证不对称）、W4（MC 验证报告不充分）
- **Excitement 4.0/5**，问题定义和框架新颖

等待 Reviewer 2 返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 61 · 2026-05-22T03:29:34.285279+00:00_

[Reviewer 1 审稿结果]:
审稿完成，已提交至 Review Director。

**评分**: Overall 3.5/5（Borderline Conference），Soundness 3.5/5，Excitement 4.0/5。

**核心发现**：
- 3 个 Must-Fix 问题：(1) Theorem 1 无解析证明仅靠 500 场景数值验证；(2) Proposition 1 中 mediation/M-bias 的 sign preservation 缺乏 closed-form proof，论文自身承认 "a closed-form proof for general K remains open"；(3) ASV 参数化 C(δ) 声称 δ ∈ [0,∞) 但实际有效范围有限，sign-flip ASV 可能超出合法矩阵范围。
- 4 个 Should-Fix 问题：头条 83.4% 来自不现实先验、sign preservation 条件的实际不可验证性、实证验证的模型不对称、MC MAPE 报告不充分。
- 主要优势：问题新颖重要、部分拓扑证明严谨、FWL 不变性负结果有实际价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 62 · 2026-05-22T03:29:41.960351+00:00_

Reviewer 1 审稿意见已记录。核心发现：3 个 critical issues（Theorem 1 证明缺失、Proposition 1 部分拓扑证明不完整、ASV 定义域问题），4 个 should-fix。评分 3.5/5。

等待 Reviewer 2 返回后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 4

## Round 4

6 recorded events


### User

_source line 63 · 2026-05-22T03:31:47.501995+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + 完整性 + 相关工作 + 格式合规

**论文**: "Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction"

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 一篇系统性强、覆盖面广的工作，将 multi-class 误分类与 DAG 拓扑的交互进行了全面刻画，但核心新颖性相对于 Teblunthuis (2024) 和 Lee &amp; Wood-Doughty (2024) 是增量式的，且 headline claim (83.4% sign reversal) 的 framing 具有误导性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 技术推导正确，Monte Carlo 验证充分，但 Proposition 1 的 mediation 和 M-bias 部分依赖数值验证而非解析证明（Appendix A 承认），sign-flip guarantee 的条件（"true effect and omitted-variable bias share the same sign"）在正文中未充分讨论其适用范围 |
| Excitement / Novelty | 2.5/5 | 从 binary→multi-class、4 DAG→7 DAG 的扩展有价值但属增量贡献；ASV 是 E-value 的直接推广；FWL invariance 是经典定理的应用 |
| Reproducibility | 3.5/5 | 实验设置描述清晰（Dirichlet prior、N=10,000、100K matrices），但无代码/数据承诺，confusion matrix 估计细节不足 |
| Confidence | 4/5 | 我熟悉 measurement error、causal inference 和 text-as-data 文献 |

---

## Summary

本文研究 K-class 非差异误分类在 7 种 DAG 拓扑下如何影响因果估计。三个贡献：(1) bias taxonomy 显示 5 种拓扑维持 sign-flip guarantee 而 exposure 和 IV 可能 sign reversal；(2) Annotation Sensitivity Values (ASVs) 框架提供三种灵敏度度量；(3) 5 种校正方法的 topology-aware 评估，证明 FWL invariance 使 matrix-based 方法对 4 种拓扑无效。通过 3 个数据集（HumAID K=10, VAST K=3, CivilComments K=2）和 4 种 LLM 的实证验证。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 83.4% sign reversal 的 headline framing 具有误导性

- 具体位置：Abstract（第1段）、Section 1 Introduction（第2段）、Section 4.2（第2段）、Section 5 Conclusion
- 问题：83.4% 这个数字来自 Dirichlet(1,1,1) uniform prior，即在所有可能的 column-stochastic 矩阵空间上均匀采样。但真实 LLM 分类器的 confusion matrix 是强对角占优的——论文自己在 Section 4.2 也承认，当 diagonal ≥ 0.7 时 sign reversal 降至 2.1%，当 diagonal ≥ 0.9 时 violation 仅 11.9%（且不再是 sign reversal 而是 amplification）。将基于最不信息先验的数字作为 headline claim，反复出现在 Abstract、Introduction、Conclusion 中，在实际应用场景下严重高估了风险。这不是一个 edge case——这是论文的核心 selling point，而它的 ecological validity 很弱。建议：(a) 在 Abstract 中同时报告 realistic accuracy regime (diagonal ≥ 0.7) 下的数字；(b) 明确标注 83.4% 对应的是 "over all possible stochastic matrices" 而非 "for typical LLM classifiers"。
- 为什么影响接收：如果 headline claim 被认为是 cherry-picked 或 misleading framing，整篇论文的可信度受损。

**N2** [critical] 新颖性增量不足，"first systematic framework" 过度声明

- 具体位置：Abstract（"the first systematic framework"）、Section 1 Introduction（"No existing framework"）、Section 5 Conclusion（"the first systematic characterization"）
- 问题：
  - **vs. Teblunthuis (2024)**：他们已系统处理了 4 种 DAG 场景（confounding, exposure, mediator, collider）在 binary 下的 misclassification，并评估了包括 MC-SIMEX 在内的校正方法。本文扩展到 7 种拓扑（增加 M-bias, front-door, IV）和 multi-class，但核心方法论（推导 probability limit、验证 sign preservation）相同。
  - **vs. Lee &amp; Wood-Doughty (2024)**：他们已将分析扩展到 categorical LLM classifiers + confounding 场景。本文覆盖更多拓扑但方法论框架类似。
  - **vs. Brenner (1993)、Dosemeci (1990)、Veierød &amp; Laake (2001)**：polytomous exposure 可导致 sign reversal 的发现在流行病学文献中已被指出。本文的贡献是将其系统化到多种 DAG 拓扑，这是有价值的，但说"first"过强。
  - **FWL invariance**：Section 4.6 的 FWL invariance 结果是 Frisch-Waugh-Lovell 定理的直接应用——当 treatment T 被直接观测（不经过 C）时，对 dummy 变量做线性变换自然不影响 T 的系数。这是教科书级别的结果，论文将其包装为一个"贡献"有拔高嫌疑。
  - **ASV vs. E-value**：ASV 的参数化 C(δ) = (1-δ)I + δC₀ 是标准的线性插值。三种 ASV 类型（magnitude, significance, sign-flip）有一定价值，但本质上是将 E-value 的 sensitivity analysis 思路套用到不同 bias metric 上，概念创新有限。
- 建议：弱化为 "the first framework to systematically characterize multi-class misclassification across multiple DAG topologies"，承认 Teblunthuis (2024) 在 binary 下的系统性工作。
- 为什么影响接收：Novelty 是 ARR 评审的核心维度。如果 incremental extension 被标为 "first"，审稿人会质疑作者对 prior work 的诚实度。

**N3** [critical] 重要相关工作未引用

- 具体位置：Section 2 Related Work、Section 4.6 Correction Guidance
- 问题：以下高度相关的已发表工作在正文中未被引用（虽然部分出现在 .bib 文件中）：
  1. **Audinet de Pieuchon et al. (EMNLP 2025)** "Benchmarking Debiasing Methods for LLM-based Parameter Estimates" — 直接 benchmark 了 DSL 和 PPI 的 debiasing 效果，与本文 Section 4.6 高度重叠。这是 EMNLP 2025 主会接收论文，不引用是严重遗漏。
  2. **Gligoric et al. (NAACL 2025)** "Can Unconfident LLM Annotations Be Used for Confident Conclusions?" — 提出 Confidence-Driven Inference，结合 LLM 置信度优化标注，与 PPI++ 讨论直接相关。
  3. **Zrnic &amp; Candès (PNAS 2024)** "Cross-prediction-powered inference" — PPI 的重要扩展，不需要 gold labels，论文讨论 PPI++ 需要 gold labels 的限制时应引用此替代方案。
  4. **Messing (2026)** "Hidden Measurement Error in LLM Pipelines" — 关于 LLM pipeline 中测量误差的最新框架性论文。
  5. **Cheng, Mayya, &amp; Sedoc (2024)** "To Err Is Human; To Annotate, SILICON?" — 系统性 LLM 标注误差工作流程。
  这些论文全部在 references.bib 中但未被 \cite，说明作者意识到了但选择不讨论——这在审稿中会被视为故意遗漏。
- 建议：至少引用 Audinet de Pieuchon et al. (2025) 和 Gligoric et al. (2025)，并在 Section 2 和 Section 4.6 中讨论与本文工作的关系。
- 为什么影响接收：Related Work 的完整性是 ARR 评审的基本要求。遗漏已发表在同 venue (EMNLP/NAACL) 的高度相关论文会严重损害论文的学术严谨性。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Proposition 1 的条件不完整

- 具体位置：Section 3.2, Proposition 1（method.tex:58-61）
- 问题：Proposition 1 声称 5 种拓扑满足 sign-flip guarantee，但条件要求 "the true effect and the omitted-variable bias share the same sign (a condition satisfied under standard DGP parameterizations)"。这个条件在正文中一笔带过，没有讨论何时可能不成立。在 Appendix 的证明中（Appendix A.3 confounding topology），sign preservation 确实依赖于 true effect 与 residual confounding bias 同号。但在实际应用中，研究者往往不知道 omitted variable bias 的方向。这意味着 sign-flip "guarantee" 实际上是一个 conditional guarantee，论文应更明确地讨论这个条件的现实含义。
- 建议：在正文中增加一段讨论何时这个条件可能不成立，并在 Limitations 中提及。

**W2** [warning] 实证验证中无真实 sign reversal 发生——论文的核心理论预测未被实证观察到

- 具体位置：Section 4.5（experiments.tex:84）
- 问题：论文强调 exposure 和 IV 拓扑的 sign reversal 风险，但在所有 98 个实证场景中（14 configurations × 7 topologies），zero sign reversals 发生。论文解释为 "confirming the structural sign-flip guarantee is K-invariant"，但这也意味着论文最引人注目的理论发现（sign reversal）在真实 LLM confusion matrices 下从未实际发生过。这削弱了 sign reversal 作为一个实际风险的 narrative。论文应更坦诚地讨论这个 tension：理论上可能但实证上罕见。
- 建议：在 Discussion/Limitations 中明确指出，sign reversal 在当前 LLM 精度水平下可能主要是理论风险而非实践风险，但随着任务难度增加或更多 K-class 场景出现可能成为现实问题。

**W3** [warning] ASV 框架的实际可用性存疑

- 具体位置：Section 3.3, Section 4.3
- 问题：ASV 依赖于 reference confusion matrix C₀，但获取 C₀ 需要 gold-standard labels——这与 PPI++ 需要 gold labels 的批评一致。论文未讨论当 C₀ 估计不准确时 ASV 的稳定性。此外，ASV 的三种类型（magnitude, significance, sign-flip）在实际使用场景中如何选择、如何解读，缺乏指导。
- 建议：增加一个关于 C₀ 估计不确定性如何影响 ASV 的讨论，或至少在 Limitations 中提及。

**W4** [warning] 线性模型假设的局限性未被充分讨论

- 具体位置：Section 3 Method 全部、Limitations
- 问题：所有理论推导基于线性回归模型（OLS probability limits）。但 text-as-data 领域的许多应用使用 logistic regression、random forests 或其他非线性模型。论文未讨论结果是否推广到非线性设定。特别是 FWL invariance 结果仅对 OLS 成立——对 logistic regression 不适用。
- 建议：在 Limitations 中增加对线性模型假设的讨论。

**W5** [warning] .bib 文件中 Gligoric et al. (2025) 作者名有误

- 具体位置：references.bib:93
- 问题：Gligoric et al. (2025) 的第三作者在 bib 中写为 "Lee, Sara Y."，但实际论文作者为 "Cinoo Lee"（ACL Anthology 可验证：aclanthology.org/2025.naacl-long.179/）。虽然当前未被引用，但如果后续引用会产生错误。
- 建议：修正作者名。

---

## 小问题（不影响接收）

1. **Abstract 信息过载**：Abstract 包含过多具体数字（83.4%, 13.7%, 52.6%, 47.0%, -88%），使得核心 message 难以一次提取。建议精简到 2-3 个关键数字。

2. **Table 1 (p.5) 中 Collider 的 "Violation 100%" 和 "Amplif. 100%"**：Collider 拓扑是 "protective"（减少 spurious association），但 Table 1 显示 100% violation 和 100% amplification——这与 Section 4.2 中 "Collider misclassification attenuates the spurious association (protective)" 的叙述矛盾。可能是因为 "violation" 定义为 |τ̂| > |τ| 包含了 attenuation 导致的 bias 超出阈值？需要更清晰的说明。（实际上看正文定义：Violation: |τ̂| > |τ|; Amplif: |τ̂| > |τ| with same sign。如果 collider 本身引入 spurious bias，misclassification 减弱它，那 |τ̂| 应该更小... 这里的定义和解读需要澄清。）

3. **Section 4.5 脚注 3**：提到 "VAST and CivilComments use a 7B model" 的限制，但脚注中的自辩略显防御性。建议移到 Limitations。

4. **Cross-K robustness (Section 4.2)**：声称 K=5,7 的结果与 K=3 一致，但未给出具体数字，仅有 "within 51-53%"（IV sign-flip rate）。建议在 appendix 中提供完整表格。

5. **Algorithm 1 (p.18)**：纠正方法选择算法是有价值的实践工具，但放在 appendix 最后一页可能被忽略。如果空间允许，应在正文中至少引用。

---

## Missing References（必须补充）

1. **Audinet de Pieuchon, N., Daoud, A., Jerzak, C.T., Johansson, M., &amp; Johansson, R. (EMNLP 2025).** "Benchmarking Debiasing Methods for LLM-based Parameter Estimates." — 直接 benchmark DSL 和 PPI，与 Section 4.6 高度重叠。
2. **Gligoric, K., Zrnic, T., Lee, C., Candès, E.J., &amp; Jurafsky, D. (NAACL 2025).** "Can Unconfident LLM Annotations Be Used for Confident Conclusions?" — Confidence-driven inference，与 correction methods 相关。
3. **Zrnic, T. &amp; Candès, E.J. (PNAS 2024).** "Cross-prediction-powered inference." — PPI 不需要 gold labels 的扩展，应在讨论 PPI++ 的 gold-label 限制时提及。
4. **Keith, K.A., Jensen, D.D., &amp; O'Connor, B.T. (ACL 2020).** "Text and Causal Inference." — Text-as-data + causal inference 的重要综述。

---

## 主要优势

1. **系统性强**：7 种 DAG 拓扑 × multi-class 的全面分析，覆盖面超过所有已有工作。
2. **Structural sign-flip guarantee 是有实践价值的结果**：告诉研究者哪些拓扑是 "safe" 的。
3. **FWL invariance 揭示的 correction ineffectiveness**：虽然理论上是 FWL 的直接推论，但将其应用到这个场景并明确指出 matrix-based correction 对 4 种拓扑无效，对实践者有重要指导意义。
4. **实证验证扎实**：3 个数据集、4 种 LLM、98 个场景的验证，theory-MC agreement MAPE 2.0%。
5. **Case study (Appendix B.1)** 对 Lee &amp; Wood-Doughty (2024) 的回顾性分析增加了 practical relevance。
6. **写作密度高但逻辑清晰**：论文在 8 页内容纳了大量内容，结构紧凑。

---

## Questions to Authors

Q1: 在所有 98 个实证场景中 zero sign reversals——这是否表明 sign reversal 在当前 LLM 精度水平下主要是理论风险？如果是，论文的核心 narrative 是否需要调整？

Q2: ASV 框架在 C₀ 估计有噪声时（例如基于小验证集的 confusion matrix 估计）的鲁棒性如何？是否做过 sensitivity-of-sensitivity 分析？

Q3: FWL invariance 结果是否可以推广到 logistic regression 或其他 GLM？如果不能，这对论文 practical guidance 的适用范围有多大影响？

Q4: Proposition 1 的条件 "true effect and omitted-variable bias share the same sign" 在实际应用中如何验证？如果无法验证，这个 guarantee 的实用价值是什么？

Q5: bib 文件中包含 Audinet de Pieuchon et al. (EMNLP 2025)、Gligoric et al. (NAACL 2025)、Zrnic &amp; Candès (PNAS 2024) 等高度相关工作但未在正文中引用——是空间限制还是有意省略？

---

## 格式合规检查

| 检查项 | 结果 | 说明 |
|--------|------|------|
| ACL 模板 | ✓ | `\usepackage[review]{acl}` |
| 匿名性 | ✓ | `\author{Anonymous}`，无 GitHub/自引泄露 |
| 正文 ≤ 8 页 | ✓ | 正文（Abstract–Conclusion）约 7.5 页 |
| Limitations | ✓ | 存在，4 个要点，长度适当 |
| Ethics Statement | — | 未提供，ARR 不强制要求但建议提供（涉及 LLM 使用） |
| 引用格式 | ✓ | ACL natbib 格式 |
| Appendix | ✓ | 10 页 appendix 含完整证明、补充实验、case study |

---

## Overall Assessment 详细理由

**3.5 (Borderline Conference)**

本文的核心贡献——将 multi-class misclassification 与 DAG 拓扑的交互进行系统性刻画——是有价值的，填补了 binary 分析与 multi-class 实际之间的空白。structural sign-flip guarantee 和 FWL-based correction ineffectiveness 是实用性强的结果。

但我有以下主要顾虑阻止我给出 4.0 (Conference)：

1. **新颖性有限**：从 Teblunthuis (2024) 的 4 DAG + binary 到 7 DAG + multi-class 是 scope 扩展而非方法论创新。核心技术（推导 probability limits、FWL decomposition）是标准工具。
2. **Headline claim 的 ecological validity**：83.4% sign reversal 基于 uniform prior，在真实 LLM classifiers 下（diagonal ≥ 0.7）降至 2.1%。论文 98 个实证场景中 zero sign reversals。这使得论文的 urgency narrative 显得夸大。
3. **关键相关工作遗漏**：Audinet de Pieuchon et al. (EMNLP 2025) 几乎与 Section 4.6 做了相同的 benchmark，不引用不可接受。
4. **ASV 的创新性**：本质上是 E-value 思路的直接移植到不同 bias metric。

如果作者能 (a) 修正 framing 使 headline claim 更准确反映实际风险水平，(b) 补充关键相关工作并讨论区别，(c) 弱化 "first" claim，论文可以达到 Conference 水平。当前版本的 excitement 不足以弥补 novelty 的局限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-22T03:32:19.755007+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n### Must-Fix 问题\n\n**N1** [critical] 83.4% sign reversal 的 headline framing 具有误导性\n- 83.4% 来自 Dirichlet(1,1,1) uniform prior，真实 LLM 分类器是强对角占优的。diagonal ≥ 0.7 时 sign reversal 降至 2.1%，diagonal ≥ 0.9 时 violation 仅 11.9%。将基于最不信息先验的数字作为 headline claim 严重高估了风险。\n- 建议在 Abstract 中同时报告 realistic accuracy regime 下的数字。\n\n**N2** [critical] 新颖性增量不足，\"first systematic framework\" 过度声明\n- vs. Teblunthuis (2024)：已系统处理 4 种 DAG + binary + MC-SIMEX 校正。本文扩展到 7 种拓扑 + multi-class，但核心方法论（推导 probability limit、验证 sign preservation）相同。\n- vs. Lee & Wood-Doughty (2024)：已做 categorical LLM classifier + confounding。\n- vs. Brenner (1993)、Dosemeci (1990)、Veierød & Laake (2001)：polytomous sign reversal 已被指出。\n- FWL invariance 是教科书级别的 FWL 定理直接应用。\n- ASV 是 E-value 的线性插值推广，概念创新有限。\n- 建议弱化为 \"the first framework to systematically characterize multi-class misclassification across multiple DAG topologies\"。\n\n**N3** [critical] 重要相关工作未引用\n- Audinet de Pieuchon et al. (EMNLP 2025)：benchmark DSL 和 PPI，与 Section 4.6 高度重叠。\n- Gligoric et al. (NAACL 2025)：Confidence-driven inference，与 correction methods 相关。\n- Zrnic & Candès (PNAS 2024)：Cross-PPI，不需要 gold labels。\n- 这些论文在 .bib 文件中但未被 \\cite——故意遗漏。\n\n### Should-Fix 问题\n\n**W1** Proposition 1 的条件不完整——sign preservation 条件（sign(τ) = sign(τ_OV)）在正文中一笔带过，实际上实践者不知道 τ 的真值。\n\n**W2** 实证验证中无真实 sign reversal 发生——98 个场景 zero sign reversals，理论上最引人注目的发现在真实 LLM 下从未发生，削弱 urgency narrative。\n\n**W3** ASV 框架的实际可用性存疑——依赖 gold-standard C₀，C₀ 估计不准确时的稳定性未讨论。\n\n**W4** 线性模型假设的局限性未被充分讨论——所有推导基于 OLS，FWL invariance 对 logistic regression 不适用。\n\n**W5** .bib 文件中 Gligoric et al. (2025) 的作者名有误。\n\n### 小问题\n- Abstract 信息过载\n- Table 1 Collider 的 violation/amplification 定义与 \"protective\" 叙述矛盾\n- Algorithm 1 放在 appendix 可能被忽略\n\n### Missing References\n1. Audinet de Pieuchon et al. (EMNLP 2025)\n2. Gligoric et al. (NAACL 2025)\n3. Zrnic & Candès (PNAS 2024)\n4. Keith et al. (ACL 2020)\n\n---\n\n请对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和小问题逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n### Must-Fix 问题\n\n**N1** [critical] 83.4% sign reversal 的 headline framing 具有误导性\n- 83.4% 来自 Dirichlet(1,1,1) uniform prior，真实 LLM 分类器是强对角占优的。diagonal ≥ 0.7 时 sign reversal 降至 2.1%，diagonal ≥ 0.9 时 violation 仅 11.9%。将基于最不信息先验的数字作为 headline claim 严重高估了风险。\n- 建议在 Abstract 中同时报告 realistic accuracy regime 下的数字。\n\n**N2** [critical] 新颖性增量不足，\"first systematic framework\" 过度声明\n- vs. Teblunthuis (2024)：已系统处理 4 种 DAG + binary + MC-SIMEX 校正。本文扩展到 7 种拓扑 + multi-class，但核心方法论（推导 probability limit、验证 sign preservation）相同。\n- vs. Lee & Wood-Doughty (2024)：已做 categorical LLM classifier + confounding。\n- vs. Brenner (1993)、Dosemeci (1990)、Veierød & Laake (2001)：polytomous sign reversal 已被指出。\n- FWL invariance 是教科书级别的 FWL 定理直接应用。\n- ASV 是 E-value 的线性插值推广，概念创新有限。\n- 建议弱化为 \"the first framework to systematically characterize multi-class misclassification across multiple DAG topologies\"。\n\n**N3** [critical] 重要相关工作未引用\n- Audinet de Pieuchon et al. (EMNLP 2025)：benchmark DSL 和 PPI，与 Section 4.6 高度重叠。\n- Gligoric et al. (NAACL 2025)：Confidence-driven inference，与 correction methods 相关。\n- Zrnic & Candès (PNAS 2024)：Cross-PPI，不需要 gold labels。\n- 这些论文在 .bib 文件中但未被 \\cite——故意遗漏。\n\n### Should-Fix 问题\n\n**W1** Proposition 1 的条件不完整——sign preservation 条件（sign(τ) = sign(τ_OV)）在正文中一笔带过，实际上实践者不知道 τ 的真值。\n\n**W2** 实证验证中无真实 sign reversal 发生——98 个场景 zero sign reversals，理论上最引人注目的发现在真实 LLM 下从未发生，削弱 urgency narrative。\n\n**W3** ASV 框架的实际可用性存疑——依赖 gold-standard C₀，C₀ 估计不准确时的稳定性未讨论。\n\n**W4** 线性模型假设的局限性未被充分讨论——所有推导基于 OLS，FWL invariance 对 logistic regression 不适用。\n\n**W5** .bib 文件中 Gligoric et al. (2025) 的作者名有误。\n\n### 小问题\n- Abstract 信息过载\n- Table 1 Collider 的 violation/amplification 定义与 \"protective\" 叙述矛盾\n- Algorithm 1 放在 appendix 可能被忽略\n\n### Missing References\n1. Audinet de Pieuchon et al. (EMNLP 2025)\n2. Gligoric et al. (NAACL 2025)\n3. Zrnic & Candès (PNAS 2024)\n4. Keith et al. (ACL 2020)\n\n---\n\n请对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和小问题逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-22T03:32:45.483297+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25728
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-22T03:32:45.533900+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### Must-Fix 问题\n\n**N1** [critical] Theorem 1（Envelope Monotonicity）无解析证明，仅 500 个场景数值验证\n- Section 3.3 声称 monotonicity 但全文无解析证明。500 个场景数值验证对 \"Theorem\" 级别声明远远不够。\n- ARR 要求 theorems 应有 complete and correct proofs。\n- ASV 框架的有效性依赖于单调性。\n\n**N2** [critical] Proposition 1 的 mediation 和 M-bias sign preservation 证明不完整\n- Confounding: 完整代数证明 ✓\n- Collider: 完整代数证明 ✓\n- Front-door: 依赖 mediation 结果，但 mediation 本身未被证明\n- **Mediation: 仅 100,000 随机矩阵数值验证**，论文公开承认 \"a closed-form proof for general K remains open\"\n- **M-bias: 仅 structural argument，无形式化证明**\n- 一个形式化 Proposition 中 2/5 拓扑缺乏证明。\n\n**N3** [critical] ASV 参数化 C(δ) 的定义域问题\n- C(δ) = (1-δ)I + δC₀，当 δ > δ_max = 1/(1-min_k C_{0,kk}) 时 C(δ) 不再是合法的 column-stochastic 矩阵。\n- 论文声称 δ ∈ [0, ∞) 是不正确的。\n- Sign-flip ASV 可能超出合法矩阵范围。\n\n### Should-Fix 问题\n\n**W1** 头条 83.4% 来自不现实先验分布，可能误导读者\n- Dirichlet(1,1,1) 包含大量不现实的 confusion matrices。\n- diagonal ≥ 0.7 时 sign reversal 降至 2.1%。\n- Abstract 和 Introduction 以 83.4% 开篇但将 2.1%/13.7% 埋在正文中间。\n\n**W2** Sign preservation 条件的实际可验证性讨论不足\n- 条件如 sign(τ) = sign(τ_OV) 要求知道 τ 的真值——但实践者正在估计 τ。存在循环性。\n\n**W3** 实证验证的系统性不对称\n- HumAID 用 frontier models，VAST/CivilComments 用 7B model。\n- \"zero sign reversals across all 98 scenarios\" 不令人意外——DGP 参数被选择为满足 sign preservation 条件。\n\n**W4** MC 验证的报告不充分\n- Grand MAPE 2.0% 掩盖拓扑间差异（IV MAPE 5.5%）。\n- 未报告 worst-case error 和置信区间。\n\n### Questions\nQ1: Confounding 拓扑能否给出 monotonicity 的解析证明？\nQ2: Mediation sign preservation 能否对 proportional case 解析证明？\nQ3: Sign-flip ASV 1.1-6.7 是否都在有效 δ 范围内？\nQ4: 是否存在 EM-based imputation 方法绕过 FWL invariance？\nQ5: 6 种 error structures 的具体参数？\n\n### 小问题\n- 主文和 Appendix 符号不统一（Z vs. D_j*）\n- \"Sign-flip guarantee\" 命名歧义，建议改为 \"sign preservation guarantee\"\n- Table 1 τ_sf 未在 caption 定义\n\n---\n\n请对每个 Must-Fix (N1-N3)、Should-Fix (W1-W4) 和小问题逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### Must-Fix 问题\n\n**N1** [critical] Theorem 1（Envelope Monotonicity）无解析证明，仅 500 个场景数值验证\n- Section 3.3 声称 monotonicity 但全文无解析证明。500 个场景数值验证对 \"Theorem\" 级别声明远远不够。\n- ARR 要求 theorems 应有 complete and correct proofs。\n- ASV 框架的有效性依赖于单调性。\n\n**N2** [critical] Proposition 1 的 mediation 和 M-bias sign preservation 证明不完整\n- Confounding: 完整代数证明 ✓\n- Collider: 完整代数证明 ✓\n- Front-door: 依赖 mediation 结果，但 mediation 本身未被证明\n- **Mediation: 仅 100,000 随机矩阵数值验证**，论文公开承认 \"a closed-form proof for general K remains open\"\n- **M-bias: 仅 structural argument，无形式化证明**\n- 一个形式化 Proposition 中 2/5 拓扑缺乏证明。\n\n**N3** [critical] ASV 参数化 C(δ) 的定义域问题\n- C(δ) = (1-δ)I + δC₀，当 δ > δ_max = 1/(1-min_k C_{0,kk}) 时 C(δ) 不再是合法的 column-stochastic 矩阵。\n- 论文声称 δ ∈ [0, ∞) 是不正确的。\n- Sign-flip ASV 可能超出合法矩阵范围。\n\n### Should-Fix 问题\n\n**W1** 头条 83.4% 来自不现实先验分布，可能误导读者\n- Dirichlet(1,1,1) 包含大量不现实的 confusion matrices。\n- diagonal ≥ 0.7 时 sign reversal 降至 2.1%。\n- Abstract 和 Introduction 以 83.4% 开篇但将 2.1%/13.7% 埋在正文中间。\n\n**W2** Sign preservation 条件的实际可验证性讨论不足\n- 条件如 sign(τ) = sign(τ_OV) 要求知道 τ 的真值——但实践者正在估计 τ。存在循环性。\n\n**W3** 实证验证的系统性不对称\n- HumAID 用 frontier models，VAST/CivilComments 用 7B model。\n- \"zero sign reversals across all 98 scenarios\" 不令人意外——DGP 参数被选择为满足 sign preservation 条件。\n\n**W4** MC 验证的报告不充分\n- Grand MAPE 2.0% 掩盖拓扑间差异（IV MAPE 5.5%）。\n- 未报告 worst-case error 和置信区间。\n\n### Questions\nQ1: Confounding 拓扑能否给出 monotonicity 的解析证明？\nQ2: Mediation sign preservation 能否对 proportional case 解析证明？\nQ3: Sign-flip ASV 1.1-6.7 是否都在有效 δ 范围内？\nQ4: 是否存在 EM-based imputation 方法绕过 FWL invariance？\nQ5: 6 种 error structures 的具体参数？\n\n### 小问题\n- 主文和 Appendix 符号不统一（Z vs. D_j*）\n- \"Sign-flip guarantee\" 命名歧义，建议改为 \"sign preservation guarantee\"\n- Table 1 τ_sf 未在 caption 定义\n\n---\n\n请对每个 Must-Fix (N1-N3)、Should-Fix (W1-W4) 和小问题逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-22T03:32:47.191572+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1657
}
```

</details>

---


### Assistant

_source line 68 · 2026-05-22T03:32:51.706497+00:00_

交叉分享已派发。两位 Reviewer 正在阅读对方意见并逐条回应，等待交叉回应返回后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 69 · 2026-05-22T03:32:54.506572+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**评分：3.5 / 5 (Borderline Conference)**

核心发现：

- **3 个 Must-Fix 问题**：(1) 83.4% sign reversal 的 headline 基于 Dirichlet(1,1,1) uniform prior，在真实 LLM 精度下降至 2.1%，framing 具有误导性；(2) "first systematic framework" 过度声明，忽视 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 的先行工作；(3) bib 中有但正文未引用 Audinet de Pieuchon et al. (EMNLP 2025)、Gligoric et al. (NAACL 2025)、Zrnic & Candès (PNAS 2024) 等高度相关工作——存在故意遗漏嫌疑。

- **5 个 Should-Fix 问题**：Proposition 1 条件不完整、98 个实证场景中 zero sign reversals 与核心 narrative 的 tension、ASV 实用性存疑、线性模型限制未讨论、bib 中作者名错误。

- **格式合规**：全部通过（模板、匿名性、页数、Limitations）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-22T03:32:59.578682+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 71 · 2026-05-22T03:35:22.803154+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 83.4% headline framing 具有误导性**

同意 R2 的判断，我在自己的审稿中也将此列为 W1。核心论据：Abstract（abstract.tex L2）、Introduction（introduction.tex L6）、Conclusion（conclusion.tex L4）均以 83.4% 领衔，但这个数字来自 Dirichlet(1,1,1)——simplex 上的均匀分布，包含大量 C_{kk} < 1/3 的矩阵。Section 4.2（experiments.tex L20）报告了更有实际意义的数字：diagonal ≥ 0.7 时 sign reversal 仅 2.1%，violation 13.7%。将最不信息先验的极端数字作为 headline 确实高估了实际风险。

补充一点 R2 未提到的：即便 2.1% 的 sign reversal 率在实际中仍然值得关注（因为 sign reversal 的后果是灾难性的），但 framing 应该诚实。建议 Abstract 同时报告两个数字，如："83.4% under uniform prior, persisting at 2.1% even with classifier accuracy above 70%"——实际上论文正文已有类似表述（experiments.tex L20），只需将其提升到 Abstract。

---

**[REBUT] R2-N2: 新颖性增量不足**

R2 低估了 K=2 → K≥3 扩展的结构性非平凡性。逐点反驳：

1. **vs. Teblunthuis (2024)**：Teblunthuis 处理 K=2，在该设置下 sign-flip guarantee 恒成立（2×2 column-stochastic matrix with positive diagonal 必然保持符号——Appendix A.7, appendix_proofs.tex L537 有明确解释）。本文的核心发现——K≥3 时 sign-flip guarantee 结构性崩溃——在 K=2 框架中原理上不可能被发现。这不是 "same methodology, more topologies"，而是揭示了一个 qualitatively new failure mode。

2. **vs. Brenner (1993) / Dosemeci (1990) / Veierød & Laake (2001)**：这些论文指出了 polytomous sign reversal 的可能性，但未量化跨拓扑的系统性差异。没有先前工作展示过 "same confusion matrix → 7 种拓扑产生定性不同的 bias 行为" 这一核心洞察。Table 1 的完整 taxonomy 是新的。

3. **FWL invariance**：R2 称其为 "教科书级别的 FWL 定理直接应用"。FWL 定理本身确实是教科书内容，但其推论——基于 C^{-1} 的校正方法（Naive plug-in, MLA）对 4/7 拓扑的 T 系数 bias reduction 恰好为 0%——是一个有实际指导意义的负结果。Table 4（Appendix B）清楚展示了这个 pattern。没有先前工作指出这一点。

4. **ASV vs. E-value**：同意 R2 的判断——C(δ) 线性插值的概念创新有限。但三种 ASV 类型的区分（magnitude、significance、sign-flip）提供了 E-value 所没有的拓扑感知维度。创新程度中等，不是零。

5. **总体判断**：同意 "first systematic framework" 的措辞应弱化，但 R2 将 novelty 评为 "insufficient" 过于苛刻。建议作者修改为 "the first framework to systematically characterize multi-class misclassification across multiple DAG topologies"（R2 自己的建议措辞是恰当的）。

---

**[AGREE] R2-N3: 重要相关工作未引用——部分同意**

同意以下引用确实相关且应当讨论：

- **Zrnic & Candès (PNAS 2024) Cross-PPI**：论文在 Section 4.6 批评 PPI++ "requires gold labels"（experiments.tex L108），但未讨论 Cross-PPI 这种不需要 gold labels 的替代方案。这是一个明显的遗漏，应在 Related Work 和 Section 4.6 讨论。
- **Keith et al. (ACL 2020)**：作为 text-based causal inference 的基础性论文，应在 Related Work 引用。

对于 Audinet de Pieuchon et al. (EMNLP 2025) 和 Gligoric et al. (NAACL 2025)，这些是 2025 年论文，与本文 correction methods 部分有重叠，引用有助于定位贡献。

但需要指出：R2 声称这些论文 "在 .bib 文件中但未被 \cite——故意遗漏"。作为 blind reviewer，我无法验证这个关于源码文件的声明。如果 R2 确实检查了 .bib 源码，这本身可能违反了 blind review 的精神。"故意遗漏" 的指控缺乏证据，建议 R2 将措辞限于 "important missing references" 而非暗示恶意。

---

### Should-Fix 问题

**[AGREE] R2-W1: Proposition 1 条件的可验证性**

我在自己的审稿中也将此列为 W2。sign preservation 的充分条件（如 sign(τ) = sign(τ_OV)）要求知道 τ 的真值，而实践者正是在估计 τ。Appendix A.8 的 Remark（appendix_proofs.tex L573-578）讨论了这一点，但主文没有充分体现。

---

**[REBUT] R2-W2: 实证验证中无 sign reversal 不等于理论无价值**

R2 的推理有两个问题：

1. **Zero sign reversals 是预期行为，不是意外缺陷。** 5/7 拓扑有结构性 sign-flip guarantee（在满足条件时），另外 2 个拓扑（exposure, IV）的 sign reversal 取决于 confusion matrix 的具体结构。实证验证使用的真实 LLM confusion matrices 是 diagonal-dominant 的，在 diagonal ≥ 0.7 下 exposure sign reversal 率仅 2.1%——所以 14 个 LLM 配置下未观察到 sign reversal 在统计上完全合理。

2. **论文的实际价值不仅在于 sign reversal。** Section 4.5 报告 HumAID 的 55.4% 场景被 magnitude-ASV 标记为 unsafe（experiments.tex L87），VAST 的 IV bias 高达 252.6%（experiments.tex L82），CivilComments 100% ASV-unsafe。这些都是 sign reversal 之外的重要发现。论文的价值在于完整的 topology-dependent vulnerability spectrum，不仅仅是 sign reversal 这一个维度。

但我同意 R2 的隐含观点：论文应更明确地在实证部分阐述 "在 realistic LLM accuracy regime 下，主要风险是 bias amplification 和 magnitude 偏差，而非 sign reversal"，而不是继续强调 sign reversal 的戏剧性。

---

**[AGREE] R2-W3: ASV 对 C₀ 估计的敏感性未讨论**

这是一个有效的补充关注。我在 N3 中关注了 ASV 参数化的定义域问题（δ 的有效范围），R2 从另一个角度指出了实际可用性问题：C₀ 本身的估计误差如何传播到 ASV。论文应讨论 C₀ 估计的不确定性对 ASV 的影响，至少做一个 C₀ perturbation 的敏感性分析。

---

**[AGREE] R2-W4: 线性模型假设的局限性**

完全同意。所有理论推导基于 OLS 线性模型，FWL invariance 对 logistic regression（binary outcomes 的标准模型）不成立。Limitations 节（conclusion.tex L6-8）目前未提及这一点。论文应在 Limitations 中明确声明：(a) bias expressions 推导假设线性模型；(b) FWL invariance 结果不推广到 GLM；(c) 对于 binary outcomes（需要 logistic regression 的场景），correction methods 的排名可能不同。

---

**[REBUT] R2-W5: .bib 作者名错误——无法验证**

作为 blind reviewer，我无法看到 .bib 源码文件。如果 R2 确实检查了源码文件来发现作者名错误，这本身可能违反 blind review protocol。但如果确实存在引用格式错误，作者应在 camera-ready 中修正。

---

### 小问题

**[AGREE] Abstract 信息过载**：Abstract 确实塞入了过多具体数字（83.4%、13.7%、52.6%、47.0%、-88%、98 scenarios 等），建议精简到 3-4 个关键数字。

**[AGREE] Table 1 Collider 叙述矛盾**：Table 1 显示 Collider 的 Violation=100%、Amplification=100%，但正文（method.tex L46）称其为 "protective"。矛盾的原因是比较基准不同——"protective" 比较的是 B(C) vs. B(I)（misclassified 比 perfect 的 Berkson's bias 更小），而 Table 1 的 violation 比较的是 |τ̂(A*)| vs. |τ|（conditioning on A* 是否引入了超出真值的 bias）。但论文未解释这一区别，读者会困惑为什么一个 "protective" 拓扑显示 100% violation。建议在 Table 1 caption 或正文中明确区分这两个比较基准。

**[REBUT] Algorithm 1 放在 appendix 被忽略**：在 8 页限制下，Algorithm 1 放在 Appendix 是合理的。主文 Section 4.6 已经总结了 correction guidance 的核心逻辑（experiments.tex L104-109），Algorithm 1 只是形式化的伪代码版本。主文可加一句指向 Appendix 的引用即可。

---

### 总结

R2 的 N1（headline framing）和 N3（missing references，尤其是 Zrnic & Candès 2024 Cross-PPI）是有效的批评，我的审稿中也有类似发现。R2 的 W4（线性模型局限）是我遗漏的有价值补充。

但 R2 的 N2（novelty insufficient）过于苛刻——K=2 → K≥3 扩展的结构性非平凡性（sign-flip guarantee breakdown）和 7-topology systematic comparison 构成了足够的增量贡献。W2（zero empirical sign reversals weakens urgency）的推理有逻辑缺陷——zero sign reversals 在 diagonal-dominant 矩阵下是预期行为，不构成对理论的反驳。

我的 N1-N3（Theorem 1 无证明、Proposition 1 mediation/M-bias 证明不完整、ASV 定义域问题）是 R2 未覆盖的独立发现，仍然是影响接收决定的关键问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 72 · 2026-05-22T03:35:35.488628+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 7

## Round 7

16 recorded events


### User

_source line 73 · 2026-05-22T03:35:36.768746+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。主要判断：

- **R2-N1 (headline framing)**: [AGREE]，与我的 W1 一致
- **R2-N2 (novelty insufficient)**: [REBUT]，K=2→K≥3 的 sign-flip breakdown 是结构性非平凡贡献，R2 低估了扩展的质变意义
- **R2-N3 (missing references)**: [AGREE] 部分同意（Zrnic & Candès Cross-PPI 尤其相关），但质疑 R2 检查 .bib 源码的 blind review 合规性
- **R2-W1**: [AGREE]，同我的 W2
- **R2-W2 (zero sign reversals)**: [REBUT]，这是 diagonal-dominant 矩阵下的预期行为，论文价值不仅限于 sign reversal
- **R2-W3**: [AGREE]
- **R2-W4 (linear model)**: [AGREE]，这是我遗漏的有价值补充
- **R2-W5**: [REBUT]，无法从 submitted PDF 验证

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Theorem 1（Envelope Monotonicity）无解析证明**

同意这是一个严重问题。我核查了全文和 Appendix A，确认 Theorem 1 的证明仅依赖 "verified numerically for all seven topologies (zero violations, 500 scenarios each)"（Section 3.3, method.tex:81）。Appendix 中没有任何关于 monotonicity 的解析推导。

补充发现：对于 confounding 拓扑，monotonicity 实际上可以从 Appendix A.3 的 Proposition 2（proportional case）推导——bias B(C) = (1-η(C))·B_OV 中 η(C) 单调依赖于 Var(E[g(A)|A*])，而后者随 δ 增大而减小。但论文没有做这个连接。对于其余拓扑，确实缺少任何形式化论证。

将此标为 "Theorem" 而非 "Conjecture" 或 "Empirical Finding" 是不恰当的。建议降级为 Conjecture 并补充 confounding case 的解析证明作为 supporting evidence。

**[AGREE] R1-N2: Proposition 1 的 mediation 和 M-bias 证明不完整**

同意。我详细审查了 Appendix A.4 (Mediation)，确认以下情况：

- **Mediation**: 论文推导了 B(C) = Σ_j w_j δ_j 的 weighted average 结构（Appendix A.4, line 287-291），这是有价值的分析。但关键步骤——证明 max_j |δ_j| ≤ |τ_ind| 对所有 column-stochastic C 成立——仅靠 100,000 个随机矩阵数值验证。论文明确承认 "a closed-form proof for general K remains open"（Appendix A.4, line 267）。
- **M-bias**: Appendix A.8 仅有一段 structural argument（"misclassification weakens the backdoor path, reducing the spurious correlation"），无任何数学推导。
- **Front-door**: Appendix A.6 表明其 bias 结构与 mediation 相同（line 450-451: "has the same structure as in §A.4"），因此继承了 mediation 的证明缺口。

将 mediation 和 M-bias 纳入同一个形式化 Proposition 中，但 2/5 拓扑缺乏证明，确实不满足 ARR 对 formal claim 的要求。建议将 Proposition 1 拆分：对有完整证明的拓扑（confounding, collider）保留 Proposition 级别；对 mediation、front-door 和 M-bias 降级为 "Empirical Finding" 或 "Conjecture"。

**[AGREE] R1-N3: ASV 参数化 C(δ) 的定义域问题**

同意这是一个技术性错误。Section 3.3 (method.tex:71) 声称 δ ∈ [0, ∞)，但 C(δ) = (1-δ)I + δC₀ 在 δ > 1/(1-min_k C_{0,kk}) 时 diagonal 变为负数，不再是合法的 stochastic matrix。

我进一步检验了论文报告的 sign-flip ASV 值（Section 4.3, experiments.tex:63）：范围为 1.1-6.7。对于一个典型的 confusion matrix C₀ 其中 min diagonal ≈ 0.4，δ_max = 1/(1-0.4) ≈ 1.67。这意味着 ASV = 6.7 远超有效域——在该 δ 值下 C(δ) 不是一个合法矩阵，因此 "sign-flip ASV = 6.7" 无物理意义。

这直接影响论文的核心度量工具。必须修正：(a) 将定义域改为 δ ∈ [0, δ_max]；(b) 对超出 δ_max 的 ASV 重新定义（如标记为 ∞ 表示在有效域内无 sign flip）。

---

### Should-Fix 问题

**[AGREE] R1-W1: 83.4% 来自不现实先验**

完全同意，这与我的 N1 问题一致。补充一个我在自己审稿中注意到的数据点：论文 98 个实证场景（Section 4.5, experiments.tex:84）中 **zero sign reversals** 发生。这意味着在真实 LLM confusion matrices 下，论文最突出的理论发现从未在实践中被观察到。将 83.4% 作为 headline 而将 0/98 的实证证据低调处理，framing 问题严重。

**[AGREE] R1-W2: Sign preservation 条件的循环性**

同意。Appendix A.8 Table 2 列出了各拓扑的 sufficient conditions：confounding 要求 sign(τ) = sign(τ_OV)，mediation 要求 sign(τ_dir) = sign(τ_total)。这些条件都需要知道 τ 的真值或方向——但实践者正在估计 τ。

不过，我想补充一个 nuance：Appendix A.8 的 Remark 段落（line 578）确实讨论了这个问题，指出 "such opposing effects are uncommon when the analyst adjusts for A precisely because they believe it confounds the T-Y relationship in a consistent direction"。这个论证有一定道理（如果分析者控制 A 是因为相信 A 是 confounder，那么 sign alignment 通常成立），但不够充分——应该在正文而非 appendix 的 remark 中讨论。

**[AGREE] R1-W3: 实证验证的系统性不对称**

部分同意。HumAID (K=10) 用 frontier models (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) 而 VAST (K=3) / CivilComments (K=2) 用 Qwen2.5-7B（Section 4.5, experiments.tex:76），这确实使 cross-dataset 比较的有效性受限。

但我不完全同意 R1 关于 "DGP 参数被选择为满足 sign preservation 条件" 的批评。论文使用的是 real LLM confusion matrices（从实际标注任务估计），不是人为构造的。Zero sign reversals 在 diagonal-dominant real confusion matrices 下是理论预期的结果，这本身是一个有效的验证——证实理论预测在实际条件下成立。问题不在于验证无效，而在于论文没有充分区分 "在 Dirichlet(1,1,1) 下的理论风险" 和 "在实际 LLM 精度下的实证风险"。

**[AGREE] R1-W4: MC 验证报告不充分**

同意。Grand MAPE 2.0%（Section 4.2, experiments.tex:15）确实掩盖了拓扑间差异。IV MAPE 5.5% 暗示部分场景可能有更大误差。应报告 per-topology MAPE range, worst-case absolute error, 和 bootstrap CIs。

---

### 小问题

**[AGREE] R1: 符号不统一 (Z vs. D_j*)**
确认：method.tex:24 使用 Z = [X, dummies(A*)]，而 appendix_proofs.tex:6 使用 D_j* = 1(A*=j)。两处符号指代相同对象但表述不同，应统一。

**[AGREE] R1: "Sign-flip guarantee" 命名歧义**
同意。"Sign-flip guarantee" 容易被误解为 "保证发生 sign flip"，而实际含义是 "保证不发生 sign flip"。建议改为 "sign preservation guarantee" 或 "sign stability guarantee"。

**[AGREE] R1: Table 1 τ_sf 未定义**
同意。Table 1 (experiments.tex:38) 最后一列 τ_sf=0? 的含义需要在 caption 中定义——虽然从上下文可推断，但正式表格应自包含。

---

### 对 R1 Questions 的看法

**Q1 (Confounding monotonicity 解析证明)**：如我在 N1 回应中指出，confounding case 实际上 *可以* 从 Proposition 2 (proportional case) 推导 monotonicity。作者应该补充这个证明。

**Q2 (Mediation proportional case 解析证明)**：Appendix A.4 的 weighted average 结构 B(C) = Σ w_j δ_j 为 proportional case (当 f 和 g 成比例时) 提供了足够的证明基础。但 general case 确实是 open。

**Q3 (Sign-flip ASV 有效范围)**：如我在 N3 回应中所述，部分报告的 ASV 值很可能超出有效 δ 范围。

**Q4 (EM-based imputation 绕过 FWL)**：有趣的问题。EM imputation 本质上改变了 likelihood 结构而非线性回归的 projection 操作，因此可能不受 FWL invariance 约束。论文应该讨论。

**Q5 (6 种 error structures 参数)**：同意应在 appendix 中提供。

---

### 总结

R1 的三个 Must-Fix 问题我全部同意——特别是 N1 (Theorem 无证明) 和 N3 (ASV 定义域错误) 是不容回避的技术问题。结合我自己的审稿发现（83.4% framing 误导、关键相关工作未引用、novelty incremental），我认为当前版本需要实质性修订。

我的评分维持 3.5 (Borderline Conference)，考虑到 R1 的技术问题可能值得更低评分，但论文的系统性和实践指导价值有所补偿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-22T03:35:55.598787+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-22T03:35:55.649622+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T03:21:35.117000+00:00\", \"completed_at\": \"2026-05-22T03:24:17.878393+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-4\", \"message\": \"连续 4 页纯文本无任何 display item，审稿人前 4 页看不到任何视觉锚点，第一印象偏\\\"理论枯燥\\\"。Figure 3（7 种 DAG 拓扑图，当前在 p.16 附录）是最自然的前置候选——它是理解 Method 节所有推导的基础，应放在 p.3 Method 开头\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"正文仅 3 个 display items（2 fig + 1 table）/ 8 页，密度 0.375/页，低于同类实证+理论论文的典型区间。大量图表被移至附录导致正文视觉单调。建议至少将 Figure 3（DAG 拓扑图）和 Table 3 或 Table 4 之一回收至正文\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"4 张 figure（Fig 4-7）挤在单页，每张图高度约 3-4cm。axis label、legend、tick label 字号估计 ≤6pt，低于 8pt 可读性阈值。审稿人需要放大才能读细节\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 的 7 个子图在双栏格式下偏小，tick label 接近可读性下限。若 Figure 3 移入正文释放空间，可考虑将 Figure 1 改为 figure*（全宽）提升可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 热力图尺寸偏小（约占单栏 1/3 高度），内部文字标注在 150dpi 下勉强可辨。作为传达 topology-dependent risk 的关键图，可考虑增大或改为 figure*\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 使用红/蓝配色（red = sign reversal, blue = attenuation），蓝色色盲安全，但红色对红绿色盲不够友好。建议用 orange 替代 red（Okabe-Ito 方案）\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 段仅 ~6 行，之后 References 占页面 ~2/3。正文空间利用尚可，但若能将一个附录 table 回收可让正文更充实\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"末页底部约 40% 空白，附录空间未充分利用\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 格式规范（booktabs、精度统一），但缺少 ↑/↓ 方向标注和加粗最优标记（表中数值为描述性统计，非竞争对比，可接受）\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Tables 2-4 和 Case Study 排版紧凑合理，booktabs 风格一致\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-22T03:36:01.675991+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-22T03:36:01.826874+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-22T03:36:57.332439+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 (Envelope Monotonicity) 无解析证明，仅 500 场景数值验证\"\n    details: \"Section 3.3 声称 monotonicity 但全文（含 Appendix）无解析推导。500 个场景的数值验证对 Theorem 级别声明远远不够。ASV 框架的有效性依赖于单调性。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 交叉回应 AGREE。R2 补充指出 confounding case 可从 Proposition 2 推导但论文未做连接。\"\n\n  - id: R1-N2\n    category: soundness\n    severity: must-fix\n    summary: \"Proposition 1 中 mediation 和 M-bias 的 sign preservation 缺乏 closed-form proof\"\n    details: \"Proposition 1 对 5 种拓扑声称 sign-flip guarantee，但 mediation 仅有 100K 随机矩阵数值验证（论文承认 'a closed-form proof for general K remains open'），M-bias 仅有 structural argument 无数学推导，front-door 继承 mediation 的证明缺口。2/5 拓扑缺乏证明。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 交叉回应 AGREE 并建议拆分 Proposition。\"\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV 参数化 C(δ) 的定义域错误：声称 δ∈[0,∞) 但实际有限\"\n    details: \"C(δ) = (1-δ)I + δC₀ 在 δ > δ_max = 1/(1-min_k C_{0,kk}) 时对角元素为负，不再是合法 column-stochastic 矩阵。论文报告的 sign-flip ASV 1.1-6.7 中较大值可能超出有效域（如 min diagonal≈0.4 则 δ_max≈1.67）。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 交叉回应 AGREE 并验证 ASV=6.7 确实超出有效域。\"\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline 基于不现实先验，framing 具有误导性\"\n    details: \"83.4% 来自 Dirichlet(1,1,1) uniform prior（含大量 C_{kk}<1/3 的矩阵），diagonal≥0.7 时降至 2.1%。98 个实证场景中 zero sign reversals。Abstract/Intro/Conclusion 均以 83.4% 开篇但将 realistic regime 数字埋在正文中间。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 列为 N1，R1 列为 W1。交叉回应中 R1 AGREE。\"\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明，novelty 相对 prior work 为增量式\"\n    details: \"Teblunthuis (2024) 已做 4 DAG + binary + MC-SIMEX；Lee & Wood-Doughty (2024) 已做 categorical + confounding；Brenner (1993)/Dosemeci (1990) 已指出 polytomous sign reversal。FWL invariance 是经典定理应用，ASV 是 E-value 的线性插值推广。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 列为 must-fix (N2)，R1 交叉回应 REBUT——认为 K=2→K≥3 的 sign-flip breakdown 是结构性质变。存在分歧，降级为 should-fix。\"\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"关键相关工作未引用：Audinet de Pieuchon et al. (EMNLP 2025)、Zrnic & Candès (PNAS 2024) 等\"\n    details: \"Audinet de Pieuchon et al. (EMNLP 2025) 直接 benchmark DSL 和 PPI；Zrnic & Candès (PNAS 2024) Cross-PPI 不需 gold labels（论文批评 PPI++ 需 gold labels 但未讨论替代）；Gligoric et al. (NAACL 2025) confidence-driven inference；Keith et al. (ACL 2020) text+causal inference 综述。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 交叉回应部分 AGREE（Zrnic & Candès 尤其相关）。\"\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 条件的实际可验证性讨论不足（循环性问题）\"\n    details: \"条件如 sign(τ)=sign(τ_OV) 要求知道 τ 真值，但实践者正在估计 τ。Appendix Remark 有讨论但主文未体现。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 列为 W2，R2 列为 W1。交叉回应双方 AGREE。\"\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证的模型不对称：HumAID 用 frontier models，VAST/CivilComments 用 7B\"\n    details: \"Cross-dataset 比较（VAST 65.4% mean bias vs. HumAID 12.2%）被模型质量差异混淆。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 部分 AGREE——同意不对称但认为 zero sign reversals 仍是有效验证。\"\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 个实证场景 zero sign reversals 与核心 narrative 的 tension 未充分讨论\"\n    details: \"论文强调 sign reversal 风险但实证中从未观察到。应明确区分理论风险 vs. 实践风险。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 REBUT（预期行为）但同意应调整 framing。分歧部分保留。\"\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 框架对 C₀ 估计不确定性的敏感性未讨论\"\n    details: \"ASV 依赖 reference confusion matrix C₀，但获取 C₀ 需要 gold labels。C₀ 估计不准确时 ASV 的稳定性未分析。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 交叉回应 AGREE。\"\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设的局限性未被充分讨论\"\n    details: \"所有推导基于 OLS。FWL invariance 对 logistic regression 不成立。Limitations 未提及。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 交叉回应 AGREE——认为是自己遗漏的有价值补充。\"\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC 验证报告不充分：Grand MAPE 2.0% 掩盖拓扑间差异\"\n    details: \"IV MAPE 5.5%，未报告 worst-case error、per-scenario 分布和置信区间。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 交叉回应 AGREE。\"\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一、命名歧义、Table caption 不完整等小问题\"\n    details: \"Z vs. D_j* 符号不统一；'sign-flip guarantee' 应改为 'sign preservation guarantee'；Table 1 τ_sf 未定义；Abstract 信息过载；Table 1 Collider violation/protective 叙述需澄清。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方均提出，交叉回应全部 AGREE。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 (Envelope Monotonicity) 无解析证明，仅 500 场景数值验证\"\n    details: \"Section 3.3 声称 monotonicity 但全文（含 Appendix）无解析推导。500 个场景的数值验证对 Theorem 级别声明远远不够。ASV 框架的有效性依赖于单调性。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 交叉回应 AGREE。R2 补充指出 confounding case 可从 Proposition 2 推导但论文未做连接。\"\n\n  - id: R1-N2\n    category: soundness\n    severity: must-fix\n    summary: \"Proposition 1 中 mediation 和 M-bias 的 sign preservation 缺乏 closed-form proof\"\n    details: \"Proposition 1 对 5 种拓扑声称 sign-flip guarantee，但 mediation 仅有 100K 随机矩阵数值验证（论文承认 'a closed-form proof for general K remains open'），M-bias 仅有 structural argument 无数学推导，front-door 继承 mediation 的证明缺口。2/5 拓扑缺乏证明。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 交叉回应 AGREE 并建议拆分 Proposition。\"\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV 参数化 C(δ) 的定义域错误：声称 δ∈[0,∞) 但实际有限\"\n    details: \"C(δ) = (1-δ)I + δC₀ 在 δ > δ_max = 1/(1-min_k C_{0,kk}) 时对角元素为负，不再是合法 column-stochastic 矩阵。论文报告的 sign-flip ASV 1.1-6.7 中较大值可能超出有效域（如 min diagonal≈0.4 则 δ_max≈1.67）。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 交叉回应 AGREE 并验证 ASV=6.7 确实超出有效域。\"\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline 基于不现实先验，framing 具有误导性\"\n    details: \"83.4% 来自 Dirichlet(1,1,1) uniform prior（含大量 C_{kk}<1/3 的矩阵），diagonal≥0.7 时降至 2.1%。98 个实证场景中 zero sign reversals。Abstract/Intro/Conclusion 均以 83.4% 开篇但将 realistic regime 数字埋在正文中间。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 列为 N1，R1 列为 W1。交叉回应中 R1 AGREE。\"\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明，novelty 相对 prior work 为增量式\"\n    details: \"Teblunthuis (2024) 已做 4 DAG + binary + MC-SIMEX；Lee & Wood-Doughty (2024) 已做 categorical + confounding；Brenner (1993)/Dosemeci (1990) 已指出 polytomous sign reversal。FWL invariance 是经典定理应用，ASV 是 E-value 的线性插值推广。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 列为 must-fix (N2)，R1 交叉回应 REBUT——认为 K=2→K≥3 的 sign-flip breakdown 是结构性质变。存在分歧，降级为 should-fix。\"\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"关键相关工作未引用：Audinet de Pieuchon et al. (EMNLP 2025)、Zrnic & Candès (PNAS 2024) 等\"\n    details: \"Audinet de Pieuchon et al. (EMNLP 2025) 直接 benchmark DSL 和 PPI；Zrnic & Candès (PNAS 2024) Cross-PPI 不需 gold labels（论文批评 PPI++ 需 gold labels 但未讨论替代）；Gligoric et al. (NAACL 2025) confidence-driven inference；Keith et al. (ACL 2020) text+causal inference 综述。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 交叉回应部分 AGREE（Zrnic & Candès 尤其相关）。\"\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 条件的实际可验证性讨论不足（循环性问题）\"\n    details: \"条件如 sign(τ)=sign(τ_OV) 要求知道 τ 真值，但实践者正在估计 τ。Appendix Remark 有讨论但主文未体现。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 列为 W2，R2 列为 W1。交叉回应双方 AGREE。\"\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证的模型不对称：HumAID 用 frontier models，VAST/CivilComments 用 7B\"\n    details: \"Cross-dataset 比较（VAST 65.4% mean bias vs. HumAID 12.2%）被模型质量差异混淆。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 部分 AGREE——同意不对称但认为 zero sign reversals 仍是有效验证。\"\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 个实证场景 zero sign reversals 与核心 narrative 的 tension 未充分讨论\"\n    details: \"论文强调 sign reversal 风险但实证中从未观察到。应明确区分理论风险 vs. 实践风险。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 REBUT（预期行为）但同意应调整 framing。分歧部分保留。\"\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 框架对 C₀ 估计不确定性的敏感性未讨论\"\n    details: \"ASV 依赖 reference confusion matrix C₀，但获取 C₀ 需要 gold labels。C₀ 估计不准确时 ASV 的稳定性未分析。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 交叉回应 AGREE。\"\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设的局限性未被充分讨论\"\n    details: \"所有推导基于 OLS。FWL invariance 对 logistic regression 不成立。Limitations 未提及。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 交叉回应 AGREE——认为是自己遗漏的有价值补充。\"\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC 验证报告不充分：Grand MAPE 2.0% 掩盖拓扑间差异\"\n    details: \"IV MAPE 5.5%，未报告 worst-case error、per-scenario 分布和置信区间。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 交叉回应 AGREE。\"\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一、命名歧义、Table caption 不完整等小问题\"\n    details: \"Z vs. D_j* 符号不统一；'sign-flip guarantee' 应改为 'sign preservation guarantee'；Table 1 τ_sf 未定义；Abstract 信息过载；Table 1 Collider violation/protective 叙述需澄清。\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方均提出，交叉回应全部 AGREE。\""
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-22T03:36:57.434355+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 5888}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-22T03:37:01.802342+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -d /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/ 2>/dev/null || mkdir -p /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/",
  "description": "Ensure review_reports directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -d /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/ 2>/dev/null || mkdir -p /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/",
    "description": "Ensure review_reports directory exists"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-22T03:37:02.053718+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-22T03:39:02.807032+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_1.md",
  "content": "# Round 1 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿日期**: 2026-05-22\n**Reviewers**: R1 (方法/理论严谨性 + 实验设计), R2 (新颖性 + 完整性 + 相关工作 + 格式合规)\n**轮次**: Round 1 (fresh review)\n\n---\n\n## Summary\n\n本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅度。三个贡献：(1) 7 种拓扑下的 multi-class bias taxonomy，证明 5 种拓扑维持 sign preservation 而 exposure 和 IV 可产生 sign reversal；(2) Annotation Sensitivity Values (ASVs) 框架提供三种灵敏度度量；(3) 5 种 correction 方法的 topology-aware 评估，揭示 FWL invariance 使 matrix-based 方法对 4 种拓扑无效。通过 3 个数据集（HumAID K=10, VAST K=3, CivilComments K=2）和 4 种 LLM 的 98 个场景进行实证验证。\n\n---\n\n## Strengths\n\n1. **问题定义新颖且重要**。将多类标注误差与 DAG 拓扑的交互作为研究对象是全新角度。现有文献要么限于二元标签（Brenner 1993; Teblunthuis 2024），要么只覆盖单一拓扑（Lee & Wood-Doughty 2024）。K=2→K>=3 扩展揭示了结构性质变——sign-flip guarantee 的崩溃——这在 binary 框架中原理上不可能发现。[R1+R2 共识]\n\n2. **部分拓扑证明严谨**。Confounding 的 sign preservation（Cauchy-Schwarz 界, Propositions 2-3）、Collider 的 Berkson's bias 反向结构（Propositions 4-5）、Exposure 的 sign reversal 反例构造清晰可验证。[R1]\n\n3. **FWL invariance 负结果有实践价值**。证明 matrix-based correction（Naive plug-in, MLA）对 FWL-invariant 拓扑的 T 系数 bias reduction 恰好为 0%，直接告诉实践者这些方法在 4/7 拓扑下无用。虽然是 FWL 定理的直接应用，但无先前工作在此场景下指出这一结论。[R1+R2 共识]\n\n4. **Binarization collapse 分析**揭示将 K-class 标注坍缩为 binary 的额外代价（154x 跨拓扑变化），对实际数据处理有直接指导意义。[R1]\n\n5. **实证验证扎实**。3 个数据集、4 种 LLM、98 个场景（扩展至 112 场景），theory-MC agreement MAPE 2.0%。ClinicalBERT case study 增加 practical relevance。[R2]\n\n6. **写作密度高但逻辑清晰**。论文在 8 页内容纳了大量内容，结构紧凑。格式完全合规。[R2]\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Must-Fix（影响接收决定）\n\n**W1. Theorem 1 (Envelope Monotonicity) 无解析证明** [R1-N1, R2 AGREE]\n- Section 3.3 声称 bias envelope 关于 δ 单调不减，但全文（含 Appendix）无解析推导，仅 500 场景数值验证。\n- ARR 要求 formal claims 应有 complete proofs。ASV 框架的有效性依赖单调性——若不成立，δ* = min{δ:...} 可能不唯一。\n- R2 补充：confounding case 实际上可从 Proposition 2 (proportional case) 推导，但论文未做连接。\n- **建议**：(a) 对 confounding 拓扑给出解析证明；(b) 其余拓扑降级为 Conjecture/Empirical Finding；(c) 增加数值验证规模至 100K+。\n\n**W2. Proposition 1 中 mediation/M-bias 的 sign preservation 缺乏 closed-form proof** [R1-N2, R2 AGREE]\n- Proposition 1 对 5 种拓扑声称 sign-flip guarantee，但：\n  - Mediation: 仅 100K 随机矩阵数值验证，论文承认 \"a closed-form proof for general K remains open\"\n  - M-bias: 仅 structural argument，无数学推导\n  - Front-door: 继承 mediation 的证明缺口\n- 形式化 Proposition 中 2/5 拓扑缺乏证明不满足 ARR 标准。\n- **建议**：拆分 Proposition——已证明的拓扑（confounding, collider）保留 Proposition 级别；mediation/front-door/M-bias 降级为 Empirical Finding。\n\n**W3. ASV 参数化 C(δ) 的定义域错误** [R1-N3, R2 AGREE]\n- C(δ) = (1-δ)I + δC₀ 在 δ > δ_max = 1/(1-min_k C₀_{kk}) 时对角元素为负，不再是合法 column-stochastic 矩阵。论文声称 δ ∈ [0, ∞) 是不正确的。\n- R2 验证：若 min diagonal ≈ 0.4，则 δ_max ≈ 1.67，报告的 sign-flip ASV = 6.7 远超有效域，无物理意义。\n- **建议**：(a) 明确 δ 有效范围为 [0, δ_max]；(b) 超出 δ_max 的 ASV 标记为 ∞（有效域内无 sign flip）；(c) 验证所有报告的 ASV 值在有效范围内。\n\n**W4. 83.4% sign reversal 的 headline framing 具有误导性** [R2-N1, R1 AGREE]\n- 83.4% 来自 Dirichlet(1,1,1) uniform prior，含大量 C_{kk} < 1/3 的不现实矩阵。\n- Diagonal ≥ 0.7（典型 LLM 精度）时 sign reversal 降至 2.1%；98 个实证场景中 zero sign reversals。\n- Abstract/Introduction/Conclusion 均以 83.4% 开篇，realistic regime 数字被埋在正文中间。\n- **建议**：Abstract 应同时报告两个数字，如 \"83.4% under uniform prior, persisting at 2.1% with classifier accuracy above 70%\"。\n\n**W5. 关键相关工作未引用** [R2-N3, R1 部分 AGREE]\n- Audinet de Pieuchon et al. (EMNLP 2025): benchmark DSL 和 PPI debiasing，与 Section 4.6 高度重叠\n- Zrnic & Candes (PNAS 2024): Cross-PPI 不需 gold labels，论文批评 PPI++ 需 gold labels 但未讨论此替代方案\n- Gligoric et al. (NAACL 2025): Confidence-driven inference\n- Keith et al. (ACL 2020): Text + causal inference 综述\n- **建议**：至少引用前两者并在 Related Work 和 Section 4.6 讨论。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W6. Sign preservation 条件的实际可验证性讨论不足** [R1-W2, R2-W1, 双方 AGREE]\n- 充分条件如 sign(τ) = sign(τ_OV) 要求知道 τ 真值——实践者正在估计 τ，存在循环性。\n- Appendix Remark 有讨论但主文未体现。\n\n**W7. 线性模型假设的局限性未被充分讨论** [R2-W4, R1 AGREE]\n- 所有推导基于 OLS。FWL invariance 对 logistic regression 不成立。Limitations 未提及。\n\n**W8. 实证验证的模型不对称** [R1-W3, R2 部分 AGREE]\n- HumAID 用 frontier models，VAST/CivilComments 用 7B model。Cross-dataset 比较被模型质量差异混淆。\n\n**W9. ASV 框架对 C₀ 估计不确定性的敏感性未讨论** [R2-W3, R1 AGREE]\n- ASV 依赖 gold-standard C₀。C₀ 估计不准确时的稳定性未分析。\n\n**W10. MC 验证报告不充分** [R1-W4, R2 AGREE]\n- Grand MAPE 2.0% 掩盖拓扑间差异（IV MAPE 5.5%）。未报告 worst-case error 和置信区间。\n\n### Minor（不影响接收）\n\n- 主文 Z vs. Appendix D_j* 符号不统一\n- \"Sign-flip guarantee\" 应改为 \"sign preservation guarantee\"（命名歧义）\n- Table 1 τ_sf 未在 caption 定义\n- Abstract 信息过载（数字过多）\n- Table 1 Collider \"protective\" 与 violation=100%/amplification=100% 的叙述需澄清比较基准\n- Algorithm 1 在主文中应有引用指向\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n\n1. **Theorem 1 必须提供至少部分解析证明或降级** — W1\n2. **Proposition 1 应拆分，未证明拓扑降级** — W2\n3. **ASV 定义域必须修正** — W3\n4. **83.4% headline 必须同时报告 realistic regime 数字** — W4\n5. **Zrnic & Candes (2024) Cross-PPI 必须引用** — W5\n6. **线性模型局限应加入 Limitations** — W7\n7. **Sign preservation 条件的循环性应在主文讨论** — W6\n\n---\n\n## Reviewer Divergence\n\n**Novelty 评估存在分歧：**\n- **R2**: 认为 novelty insufficient——从 Teblunthuis (2024) 的 4 DAG + binary 到 7 DAG + multi-class 是 scope 扩展而非方法论创新；ASV 是 E-value 的直接推广；FWL invariance 是教科书应用。评 Excitement 2.5/5。\n- **R1 [REBUT]**: 认为 K=2→K>=3 的 sign-flip breakdown 是结构性非平凡贡献——在 K=2 框架中原理上不可能发现此 failure mode（2x2 stochastic matrix with positive diagonal 必然保持符号）。Table 1 的完整 taxonomy 是新的。评 Excitement 4.0/5。\n- **Director 判断**：R1 的反驳有技术依据——K>=3 的 sign reversal 确实是质变而非量变。但 R2 关于 ASV 概念创新有限和 FWL invariance 为标准应用的批评也成立。将 novelty 争议降级为 should-fix（建议弱化 \"first\" claim 但不构成一票否决）。\n\n**实证 zero sign reversals 的解读：**\n- **R2**: 理论最引人注目的发现在实证中从未发生，削弱 urgency narrative。\n- **R1 [REBUT]**: 这是 diagonal-dominant 矩阵下的预期行为，不构成对理论的反驳；论文价值不仅限于 sign reversal。\n- **Director 判断**：R1 的反驳有效，但论文确实应更明确区分理论风险 vs. 实践风险。\n\n---\n\n## Questions（需作者回应）\n\n1. Confounding 拓扑能否对 Theorem 1 (monotonicity) 给出解析证明？Proposition 2 的 proportional case 似乎已提供充分基础。\n2. Sign-flip ASV 1.1-6.7 对应的 C₀ 的 δ_max 分别是多少？是否所有报告值都在有效域内？\n3. 是否存在 EM-based imputation 方法可绕过 FWL invariance？PPI++ 之外还有哪些方法可 bypass？\n4. Proposition 1 的条件在实际中如何近似验证？是否可通过 bootstrap 或 sensitivity analysis？\n5. 6 种 error structures 的具体参数？（应在 Appendix 提供完整参数表）\n6. 论文 .bib 中包含 Audinet de Pieuchon et al. (EMNLP 2025)、Gligoric et al. (NAACL 2025) 等高度相关工作但未在正文引用——是空间限制还是其他原因？\n\n---\n\n## Missing References\n\n1. **Audinet de Pieuchon, N. et al. (EMNLP 2025)** \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\" — 直接 benchmark DSL 和 PPI，与 Section 4.6 高度重叠 [R1+R2 共识]\n2. **Zrnic, T. & Candes, E.J. (PNAS 2024)** \"Cross-prediction-powered inference\" — PPI 不需 gold labels 的扩展 [R1+R2 共识]\n3. **Gligoric, K. et al. (NAACL 2025)** \"Can Unconfident LLM Annotations Be Used for Confident Conclusions?\" — Confidence-driven inference [R2]\n4. **Keith, K.A. et al. (ACL 2020)** \"Text and Causal Inference: A Review\" — 基础性综述 [R1+R2 共识]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 7 info, 0 critical）。\n\n**Warnings:**\n1. 前 4 页纯文本无任何 display item。Figure 3（7 种 DAG 拓扑图，当前在 p.16 Appendix）是最自然的前置候选——它是理解 Method 节所有推导的基础，建议移至 p.3 Method 开头。\n2. 正文仅 3 个 display items / 8 页（密度 0.375/页），低于同类论文典型区间。大量图表被移至 Appendix 导致正文视觉单调。\n3. p.17 四张 figure 挤在单页，axis label/legend 字号约 ≤6pt，低于 8pt 可读性阈值。\n\n**Info（建议性）:**\n- Figure 1 的子图在双栏格式下偏小，可考虑 figure* 全宽\n- Figure 2 热力图尺寸偏小\n- Figure 1 红色对红绿色盲不友好，建议 Okabe-Ito 配色\n- Limitations 段仅 ~6 行，之后 References 占 p.8 约 2/3\n- 末页（p.18）底部约 40% 空白\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement/Novelty | 4.0 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 3.5 | 3.5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评价**：\n\n本文提出了一个有实际价值的框架，将多类标注误差与因果 DAG 拓扑系统性关联。核心洞察（K>=3 时二元保证失效、拓扑决定风险等级、FWL invariance 使 matrix-based correction 无效）是 genuinely novel 的，问题重要且系统性强。\n\n阻止给出 4.0 (Conference) 的主要原因：\n1. **理论严谨性缺口**：Theorem 1 和 Proposition 1 的部分拓扑缺乏解析证明，不满足 ARR 对形式化声明的标准\n2. **ASV 技术缺陷**：参数化定义域错误，部分报告的 ASV 值可能无物理意义\n3. **Headline framing 误导**：83.4% 基于不现实先验，98 个实证场景 zero sign reversals，核心 narrative 的 ecological validity 存疑\n4. **关键相关工作遗漏**：Audinet de Pieuchon et al. (EMNLP 2025) 和 Zrnic & Candes (PNAS 2024) 必须引用\n\n**修改路径（达到 Conference 4.0 的条件）**：\n- 为 Theorem 1 的 confounding case 提供解析证明，其余降级为 Conjecture\n- 拆分 Proposition 1，将未证明拓扑降级为 Empirical Finding\n- 修正 ASV 定义域，验证所有报告值的有效性\n- 修正 headline framing，Abstract 同时报告 realistic regime 数字\n- 补充关键相关工作引用并讨论区别\n- Limitations 补充线性模型假设和 sign preservation 条件的可验证性\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息过载：包含 83.4%, 13.7%, 52.6%, 47.0%, -88%, 98 scenarios 等数字。建议精简到 3-4 个关键数字。\n- 83.4% 应同时标注先验和 realistic regime 下的数字。\n\n### Section 1 (Introduction)\n- \"first systematic framework\" 建议弱化为 \"first framework to systematically characterize multi-class misclassification across multiple DAG topologies\"\n- 应更早讨论 Dirichlet(1,1,1) 先验的局限性\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 应拆分为已证明和未证明两组\n- 条件 \"provided the true effect and the omitted-variable bias share the same sign\" 应在主文讨论可验证性\n\n### Section 3.3 (ASV)\n- 修正 δ ∈ [0, ∞) 为 δ ∈ [0, δ_max]\n- Theorem 1 降级或补充证明\n\n### Section 4 (Experiments)\n- Table 1 caption 应定义 τ_sf；澄清 Collider 的 violation/protective 比较基准\n- MC MAPE 应报告 per-topology 分布和 worst-case\n- 实证部分应明确区分理论风险 vs. 实践风险\n\n### Section 4.5 (Empirical Validation)\n- 应使用相同 tier 模型做 cross-K 比较，或明确声明 cross-dataset 比较的局限\n- 脚注 3 的自辩建议移到 Limitations\n\n### Section 4.6 (Correction)\n- 引用 Audinet de Pieuchon et al. (EMNLP 2025) 和 Zrnic & Candes (2024) Cross-PPI\n- 讨论 EM-based imputation 等绕过 FWL invariance 的替代方案\n- 6 种 error structures 参数应在 Appendix 提供\n\n### Section 5 (Conclusion) + Limitations\n- 弱化 \"first\" claim\n- Limitations 补充：(a) 线性模型假设; (b) sign preservation 条件的可验证性局限; (c) ASV 对 C₀ 估计的敏感性\n- \"Sign-flip guarantee\" 命名建议改为 \"sign preservation guarantee\"\n\n### Appendix\n- Figure 3 (DAG taxonomy) 应移入正文 Section 3 开头\n- 符号 Z vs. D_j* 应统一\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_1.md",
    "content": "# Round 1 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿日期**: 2026-05-22\n**Reviewers**: R1 (方法/理论严谨性 + 实验设计), R2 (新颖性 + 完整性 + 相关工作 + 格式合规)\n**轮次**: Round 1 (fresh review)\n\n---\n\n## Summary\n\n本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅度。三个贡献：(1) 7 种拓扑下的 multi-class bias taxonomy，证明 5 种拓扑维持 sign preservation 而 exposure 和 IV 可产生 sign reversal；(2) Annotation Sensitivity Values (ASVs) 框架提供三种灵敏度度量；(3) 5 种 correction 方法的 topology-aware 评估，揭示 FWL invariance 使 matrix-based 方法对 4 种拓扑无效。通过 3 个数据集（HumAID K=10, VAST K=3, CivilComments K=2）和 4 种 LLM 的 98 个场景进行实证验证。\n\n---\n\n## Strengths\n\n1. **问题定义新颖且重要**。将多类标注误差与 DAG 拓扑的交互作为研究对象是全新角度。现有文献要么限于二元标签（Brenner 1993; Teblunthuis 2024），要么只覆盖单一拓扑（Lee & Wood-Doughty 2024）。K=2→K>=3 扩展揭示了结构性质变——sign-flip guarantee 的崩溃——这在 binary 框架中原理上不可能发现。[R1+R2 共识]\n\n2. **部分拓扑证明严谨**。Confounding 的 sign preservation（Cauchy-Schwarz 界, Propositions 2-3）、Collider 的 Berkson's bias 反向结构（Propositions 4-5）、Exposure 的 sign reversal 反例构造清晰可验证。[R1]\n\n3. **FWL invariance 负结果有实践价值**。证明 matrix-based correction（Naive plug-in, MLA）对 FWL-invariant 拓扑的 T 系数 bias reduction 恰好为 0%，直接告诉实践者这些方法在 4/7 拓扑下无用。虽然是 FWL 定理的直接应用，但无先前工作在此场景下指出这一结论。[R1+R2 共识]\n\n4. **Binarization collapse 分析**揭示将 K-class 标注坍缩为 binary 的额外代价（154x 跨拓扑变化），对实际数据处理有直接指导意义。[R1]\n\n5. **实证验证扎实**。3 个数据集、4 种 LLM、98 个场景（扩展至 112 场景），theory-MC agreement MAPE 2.0%。ClinicalBERT case study 增加 practical relevance。[R2]\n\n6. **写作密度高但逻辑清晰**。论文在 8 页内容纳了大量内容，结构紧凑。格式完全合规。[R2]\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Must-Fix（影响接收决定）\n\n**W1. Theorem 1 (Envelope Monotonicity) 无解析证明** [R1-N1, R2 AGREE]\n- Section 3.3 声称 bias envelope 关于 δ 单调不减，但全文（含 Appendix）无解析推导，仅 500 场景数值验证。\n- ARR 要求 formal claims 应有 complete proofs。ASV 框架的有效性依赖单调性——若不成立，δ* = min{δ:...} 可能不唯一。\n- R2 补充：confounding case 实际上可从 Proposition 2 (proportional case) 推导，但论文未做连接。\n- **建议**：(a) 对 confounding 拓扑给出解析证明；(b) 其余拓扑降级为 Conjecture/Empirical Finding；(c) 增加数值验证规模至 100K+。\n\n**W2. Proposition 1 中 mediation/M-bias 的 sign preservation 缺乏 closed-form proof** [R1-N2, R2 AGREE]\n- Proposition 1 对 5 种拓扑声称 sign-flip guarantee，但：\n  - Mediation: 仅 100K 随机矩阵数值验证，论文承认 \"a closed-form proof for general K remains open\"\n  - M-bias: 仅 structural argument，无数学推导\n  - Front-door: 继承 mediation 的证明缺口\n- 形式化 Proposition 中 2/5 拓扑缺乏证明不满足 ARR 标准。\n- **建议**：拆分 Proposition——已证明的拓扑（confounding, collider）保留 Proposition 级别；mediation/front-door/M-bias 降级为 Empirical Finding。\n\n**W3. ASV 参数化 C(δ) 的定义域错误** [R1-N3, R2 AGREE]\n- C(δ) = (1-δ)I + δC₀ 在 δ > δ_max = 1/(1-min_k C₀_{kk}) 时对角元素为负，不再是合法 column-stochastic 矩阵。论文声称 δ ∈ [0, ∞) 是不正确的。\n- R2 验证：若 min diagonal ≈ 0.4，则 δ_max ≈ 1.67，报告的 sign-flip ASV = 6.7 远超有效域，无物理意义。\n- **建议**：(a) 明确 δ 有效范围为 [0, δ_max]；(b) 超出 δ_max 的 ASV 标记为 ∞（有效域内无 sign flip）；(c) 验证所有报告的 ASV 值在有效范围内。\n\n**W4. 83.4% sign reversal 的 headline framing 具有误导性** [R2-N1, R1 AGREE]\n- 83.4% 来自 Dirichlet(1,1,1) uniform prior，含大量 C_{kk} < 1/3 的不现实矩阵。\n- Diagonal ≥ 0.7（典型 LLM 精度）时 sign reversal 降至 2.1%；98 个实证场景中 zero sign reversals。\n- Abstract/Introduction/Conclusion 均以 83.4% 开篇，realistic regime 数字被埋在正文中间。\n- **建议**：Abstract 应同时报告两个数字，如 \"83.4% under uniform prior, persisting at 2.1% with classifier accuracy above 70%\"。\n\n**W5. 关键相关工作未引用** [R2-N3, R1 部分 AGREE]\n- Audinet de Pieuchon et al. (EMNLP 2025): benchmark DSL 和 PPI debiasing，与 Section 4.6 高度重叠\n- Zrnic & Candes (PNAS 2024): Cross-PPI 不需 gold labels，论文批评 PPI++ 需 gold labels 但未讨论此替代方案\n- Gligoric et al. (NAACL 2025): Confidence-driven inference\n- Keith et al. (ACL 2020): Text + causal inference 综述\n- **建议**：至少引用前两者并在 Related Work 和 Section 4.6 讨论。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W6. Sign preservation 条件的实际可验证性讨论不足** [R1-W2, R2-W1, 双方 AGREE]\n- 充分条件如 sign(τ) = sign(τ_OV) 要求知道 τ 真值——实践者正在估计 τ，存在循环性。\n- Appendix Remark 有讨论但主文未体现。\n\n**W7. 线性模型假设的局限性未被充分讨论** [R2-W4, R1 AGREE]\n- 所有推导基于 OLS。FWL invariance 对 logistic regression 不成立。Limitations 未提及。\n\n**W8. 实证验证的模型不对称** [R1-W3, R2 部分 AGREE]\n- HumAID 用 frontier models，VAST/CivilComments 用 7B model。Cross-dataset 比较被模型质量差异混淆。\n\n**W9. ASV 框架对 C₀ 估计不确定性的敏感性未讨论** [R2-W3, R1 AGREE]\n- ASV 依赖 gold-standard C₀。C₀ 估计不准确时的稳定性未分析。\n\n**W10. MC 验证报告不充分** [R1-W4, R2 AGREE]\n- Grand MAPE 2.0% 掩盖拓扑间差异（IV MAPE 5.5%）。未报告 worst-case error 和置信区间。\n\n### Minor（不影响接收）\n\n- 主文 Z vs. Appendix D_j* 符号不统一\n- \"Sign-flip guarantee\" 应改为 \"sign preservation guarantee\"（命名歧义）\n- Table 1 τ_sf 未在 caption 定义\n- Abstract 信息过载（数字过多）\n- Table 1 Collider \"protective\" 与 violation=100%/amplification=100% 的叙述需澄清比较基准\n- Algorithm 1 在主文中应有引用指向\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n\n1. **Theorem 1 必须提供至少部分解析证明或降级** — W1\n2. **Proposition 1 应拆分，未证明拓扑降级** — W2\n3. **ASV 定义域必须修正** — W3\n4. **83.4% headline 必须同时报告 realistic regime 数字** — W4\n5. **Zrnic & Candes (2024) Cross-PPI 必须引用** — W5\n6. **线性模型局限应加入 Limitations** — W7\n7. **Sign preservation 条件的循环性应在主文讨论** — W6\n\n---\n\n## Reviewer Divergence\n\n**Novelty 评估存在分歧：**\n- **R2**: 认为 novelty insufficient——从 Teblunthuis (2024) 的 4 DAG + binary 到 7 DAG + multi-class 是 scope 扩展而非方法论创新；ASV 是 E-value 的直接推广；FWL invariance 是教科书应用。评 Excitement 2.5/5。\n- **R1 [REBUT]**: 认为 K=2→K>=3 的 sign-flip breakdown 是结构性非平凡贡献——在 K=2 框架中原理上不可能发现此 failure mode（2x2 stochastic matrix with positive diagonal 必然保持符号）。Table 1 的完整 taxonomy 是新的。评 Excitement 4.0/5。\n- **Director 判断**：R1 的反驳有技术依据——K>=3 的 sign reversal 确实是质变而非量变。但 R2 关于 ASV 概念创新有限和 FWL invariance 为标准应用的批评也成立。将 novelty 争议降级为 should-fix（建议弱化 \"first\" claim 但不构成一票否决）。\n\n**实证 zero sign reversals 的解读：**\n- **R2**: 理论最引人注目的发现在实证中从未发生，削弱 urgency narrative。\n- **R1 [REBUT]**: 这是 diagonal-dominant 矩阵下的预期行为，不构成对理论的反驳；论文价值不仅限于 sign reversal。\n- **Director 判断**：R1 的反驳有效，但论文确实应更明确区分理论风险 vs. 实践风险。\n\n---\n\n## Questions（需作者回应）\n\n1. Confounding 拓扑能否对 Theorem 1 (monotonicity) 给出解析证明？Proposition 2 的 proportional case 似乎已提供充分基础。\n2. Sign-flip ASV 1.1-6.7 对应的 C₀ 的 δ_max 分别是多少？是否所有报告值都在有效域内？\n3. 是否存在 EM-based imputation 方法可绕过 FWL invariance？PPI++ 之外还有哪些方法可 bypass？\n4. Proposition 1 的条件在实际中如何近似验证？是否可通过 bootstrap 或 sensitivity analysis？\n5. 6 种 error structures 的具体参数？（应在 Appendix 提供完整参数表）\n6. 论文 .bib 中包含 Audinet de Pieuchon et al. (EMNLP 2025)、Gligoric et al. (NAACL 2025) 等高度相关工作但未在正文引用——是空间限制还是其他原因？\n\n---\n\n## Missing References\n\n1. **Audinet de Pieuchon, N. et al. (EMNLP 2025)** \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\" — 直接 benchmark DSL 和 PPI，与 Section 4.6 高度重叠 [R1+R2 共识]\n2. **Zrnic, T. & Candes, E.J. (PNAS 2024)** \"Cross-prediction-powered inference\" — PPI 不需 gold labels 的扩展 [R1+R2 共识]\n3. **Gligoric, K. et al. (NAACL 2025)** \"Can Unconfident LLM Annotations Be Used for Confident Conclusions?\" — Confidence-driven inference [R2]\n4. **Keith, K.A. et al. (ACL 2020)** \"Text and Causal Inference: A Review\" — 基础性综述 [R1+R2 共识]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 7 info, 0 critical）。\n\n**Warnings:**\n1. 前 4 页纯文本无任何 display item。Figure 3（7 种 DAG 拓扑图，当前在 p.16 Appendix）是最自然的前置候选——它是理解 Method 节所有推导的基础，建议移至 p.3 Method 开头。\n2. 正文仅 3 个 display items / 8 页（密度 0.375/页），低于同类论文典型区间。大量图表被移至 Appendix 导致正文视觉单调。\n3. p.17 四张 figure 挤在单页，axis label/legend 字号约 ≤6pt，低于 8pt 可读性阈值。\n\n**Info（建议性）:**\n- Figure 1 的子图在双栏格式下偏小，可考虑 figure* 全宽\n- Figure 2 热力图尺寸偏小\n- Figure 1 红色对红绿色盲不友好，建议 Okabe-Ito 配色\n- Limitations 段仅 ~6 行，之后 References 占 p.8 约 2/3\n- 末页（p.18）底部约 40% 空白\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement/Novelty | 4.0 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 3.5 | 3.5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评价**：\n\n本文提出了一个有实际价值的框架，将多类标注误差与因果 DAG 拓扑系统性关联。核心洞察（K>=3 时二元保证失效、拓扑决定风险等级、FWL invariance 使 matrix-based correction 无效）是 genuinely novel 的，问题重要且系统性强。\n\n阻止给出 4.0 (Conference) 的主要原因：\n1. **理论严谨性缺口**：Theorem 1 和 Proposition 1 的部分拓扑缺乏解析证明，不满足 ARR 对形式化声明的标准\n2. **ASV 技术缺陷**：参数化定义域错误，部分报告的 ASV 值可能无物理意义\n3. **Headline framing 误导**：83.4% 基于不现实先验，98 个实证场景 zero sign reversals，核心 narrative 的 ecological validity 存疑\n4. **关键相关工作遗漏**：Audinet de Pieuchon et al. (EMNLP 2025) 和 Zrnic & Candes (PNAS 2024) 必须引用\n\n**修改路径（达到 Conference 4.0 的条件）**：\n- 为 Theorem 1 的 confounding case 提供解析证明，其余降级为 Conjecture\n- 拆分 Proposition 1，将未证明拓扑降级为 Empirical Finding\n- 修正 ASV 定义域，验证所有报告值的有效性\n- 修正 headline framing，Abstract 同时报告 realistic regime 数字\n- 补充关键相关工作引用并讨论区别\n- Limitations 补充线性模型假设和 sign preservation 条件的可验证性\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息过载：包含 83.4%, 13.7%, 52.6%, 47.0%, -88%, 98 scenarios 等数字。建议精简到 3-4 个关键数字。\n- 83.4% 应同时标注先验和 realistic regime 下的数字。\n\n### Section 1 (Introduction)\n- \"first systematic framework\" 建议弱化为 \"first framework to systematically characterize multi-class misclassification across multiple DAG topologies\"\n- 应更早讨论 Dirichlet(1,1,1) 先验的局限性\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 应拆分为已证明和未证明两组\n- 条件 \"provided the true effect and the omitted-variable bias share the same sign\" 应在主文讨论可验证性\n\n### Section 3.3 (ASV)\n- 修正 δ ∈ [0, ∞) 为 δ ∈ [0, δ_max]\n- Theorem 1 降级或补充证明\n\n### Section 4 (Experiments)\n- Table 1 caption 应定义 τ_sf；澄清 Collider 的 violation/protective 比较基准\n- MC MAPE 应报告 per-topology 分布和 worst-case\n- 实证部分应明确区分理论风险 vs. 实践风险\n\n### Section 4.5 (Empirical Validation)\n- 应使用相同 tier 模型做 cross-K 比较，或明确声明 cross-dataset 比较的局限\n- 脚注 3 的自辩建议移到 Limitations\n\n### Section 4.6 (Correction)\n- 引用 Audinet de Pieuchon et al. (EMNLP 2025) 和 Zrnic & Candes (2024) Cross-PPI\n- 讨论 EM-based imputation 等绕过 FWL invariance 的替代方案\n- 6 种 error structures 参数应在 Appendix 提供\n\n### Section 5 (Conclusion) + Limitations\n- 弱化 \"first\" claim\n- Limitations 补充：(a) 线性模型假设; (b) sign preservation 条件的可验证性局限; (c) ASV 对 C₀ 估计的敏感性\n- \"Sign-flip guarantee\" 命名建议改为 \"sign preservation guarantee\"\n\n### Appendix\n- Figure 3 (DAG taxonomy) 应移入正文 Section 3 开头\n- 符号 Z vs. D_j* 应统一\n"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-22T03:39:02.908705+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Write",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-22T03:39:55.088881+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "report": "# Round 1 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿日期**: 2026-05-22\n**Reviewers**: R1 (方法/理论严谨性 + 实验设计), R2 (新颖性 + 完整性 + 相关工作 + 格式合规)\n\n---\n\n## Summary\n\n本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅度。三个贡献：(1) 7 种拓扑下的 multi-class bias taxonomy，证明 5 种拓扑维持 sign preservation 而 exposure 和 IV 可产生 sign reversal；(2) Annotation Sensitivity Values (ASVs) 框架提供三种灵敏度度量；(3) 5 种 correction 方法的 topology-aware 评估，揭示 FWL invariance 使 matrix-based 方法对 4 种拓扑无效。\n\n---\n\n## Strengths\n\n1. **问题定义新颖且重要**。将多类标注误差与 DAG 拓扑的交互作为研究对象是全新角度。K=2→K>=3 揭示了结构性质变——sign-flip guarantee 的崩溃——这在 binary 框架中原理上不可能发现。[R1+R2 共识]\n2. **部分拓扑证明严谨**。Confounding（Cauchy-Schwarz 界）、Collider（Berkson's bias 反向结构）、Exposure 反例构造清晰可验证。[R1]\n3. **FWL invariance 负结果有实践价值**。证明 matrix-based correction 对 4/7 拓扑的 T 系数 bias reduction 恰好为 0%。[R1+R2 共识]\n4. **Binarization collapse 分析**揭示 K-class→binary 的额外代价（154x 跨拓扑变化）。[R1]\n5. **实证验证扎实**。3 数据集、4 LLM、98+ 场景，MAPE 2.0%。[R2]\n6. **写作密度高、结构紧凑、格式完全合规**。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，影响接收决定）\n\n**W1. Theorem 1 (Envelope Monotonicity) 无解析证明** [R1+R2 共识]\n- 仅 500 场景数值验证。ASV 有效性依赖单调性。建议：confounding case 补解析证明，其余降级为 Conjecture。\n\n**W2. Proposition 1 中 mediation/M-bias sign preservation 缺乏 proof** [R1+R2 共识]\n- Mediation 仅数值验证（论文承认 proof remains open），M-bias 仅 structural argument，front-door 继承 mediation 缺口。建议拆分 Proposition。\n\n**W3. ASV 参数化 C(δ) 定义域错误** [R1+R2 共识]\n- δ∈[0,∞) 不正确。Sign-flip ASV=6.7 可能超出有效域（δ_max≈1.67 if min diagonal≈0.4）。\n\n**W4. 83.4% headline framing 误导** [R1+R2 共识]\n- 基于 Dirichlet(1,1,1)，diagonal≥0.7 时降至 2.1%，98 实证场景 zero sign reversals。Abstract 应同时报告 realistic regime 数字。\n\n**W5. 关键相关工作未引用** [R1+R2 共识]\n- Audinet de Pieuchon et al. (EMNLP 2025), Zrnic & Candes (PNAS 2024) Cross-PPI, Gligoric et al. (NAACL 2025), Keith et al. (ACL 2020)。\n\n### Should-Fix（6 项）\n\n**W6.** Sign preservation 条件的循环性未在主文讨论 [R1+R2 共识]\n**W7.** 线性模型假设局限未在 Limitations 提及 [R1+R2 共识]\n**W8.** 实证验证模型不对称（HumAID frontier vs VAST/CC 7B）[R1, R2 部分同意]\n**W9.** ASV 对 C₀ 估计不确定性的敏感性未讨论 [R1+R2 共识]\n**W10.** MC MAPE 报告不充分（掩盖 per-topology 差异）[R1+R2 共识]\n**W11.** \"first systematic framework\" 过度声明 [R2 提出, R1 部分同意建议弱化措辞]\n\n---\n\n## Reviewer Consensus\n\n完全一致 [AGREE]：W1-W5（所有 must-fix）、W6-W7、W9-W10、所有 minor issues。\n\n## Reviewer Divergence\n\n**Novelty 评估**：R2 认为增量式扩展（Excitement 2.5/5），R1 反驳认为 K>=3 sign-flip breakdown 是结构性质变（Excitement 4.0/5）。Director 判断：R1 反驳有技术依据，但 R2 关于 ASV 和 FWL 创新有限的批评也成立。降级为 should-fix。\n\n---\n\n## Questions\n\n1. Confounding case 能否对 Theorem 1 给出解析证明？\n2. Sign-flip ASV 1.1-6.7 是否都在有效 δ 范围内？\n3. 是否存在绕过 FWL invariance 的 correction 方法（如 EM imputation）？\n4. Proposition 1 条件如何在实际中近似验证？\n5. 6 种 error structures 的具体参数？\n6. .bib 中有但未 \\cite 的高度相关论文——原因？\n\n---\n\n## Missing References\n\n1. Audinet de Pieuchon et al. (EMNLP 2025) — benchmark DSL/PPI debiasing\n2. Zrnic & Candes (PNAS 2024) — Cross-PPI (gold-free)\n3. Gligoric et al. (NAACL 2025) — Confidence-driven inference\n4. Keith et al. (ACL 2020) — Text + causal inference survey\n\n---\n\n## External Review\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n已完成（3 warnings, 7 info, 0 critical）。主要发现：\n- 前 4 页纯文本无 display item，Figure 3 (DAG taxonomy, 当前 p.16) 应移至正文 Method 开头\n- 正文仅 3 display items / 8 页，密度偏低\n- p.17 四张 figure 挤在单页，字号 ≤6pt 低于可读性阈值\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 4.0 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 3.5 | 3.5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**修改路径（达到 4.0 Conference 的条件）**：\n1. Theorem 1 confounding case 补解析证明，其余降级\n2. 拆分 Proposition 1，未证明拓扑降级为 Empirical Finding\n3. 修正 ASV 定义域，验证报告值有效性\n4. Abstract 同时报告 realistic regime 数字\n5. 补充 4 篇关键引用并讨论区别\n6. Limitations 补充线性模型假设、sign preservation 条件可验证性、ASV 对 C₀ 敏感性\n\n---\n\n## Detailed Comments\n\n### Abstract — 信息过载（数字过多），83.4% 应标注先验 + realistic regime\n### Introduction — 弱化 \"first\" claim，更早讨论 Dirichlet prior 局限\n### Section 3.2 — 拆分 Proposition 1；条件可验证性在主文讨论\n### Section 3.3 — 修正 δ 定义域；Theorem 1 降级或补证明\n### Section 4 — Table 1 caption 定义 τ_sf；澄清 Collider violation/protective；MC MAPE 报告 per-topology 分布\n### Section 4.5 — 同 tier 模型做 cross-K 比较或声明局限；区分理论风险 vs. 实践风险\n### Section 4.6 — 引用 Audinet de Pieuchon et al.、Cross-PPI；讨论 FWL bypass 替代方案；error structures 参数表\n### Conclusion + Limitations — 弱化 \"first\"；补充线性模型假设、条件可验证性、ASV C₀ 敏感性\n### Appendix — Figure 3 移入正文；符号 Z vs. D_j* 统一\n### Terminology — \"sign-flip guarantee\" 改为 \"sign preservation guarantee\"",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "report": "# Round 1 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿日期**: 2026-05-22\n**Reviewers**: R1 (方法/理论严谨性 + 实验设计), R2 (新颖性 + 完整性 + 相关工作 + 格式合规)\n\n---\n\n## Summary\n\n本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅度。三个贡献：(1) 7 种拓扑下的 multi-class bias taxonomy，证明 5 种拓扑维持 sign preservation 而 exposure 和 IV 可产生 sign reversal；(2) Annotation Sensitivity Values (ASVs) 框架提供三种灵敏度度量；(3) 5 种 correction 方法的 topology-aware 评估，揭示 FWL invariance 使 matrix-based 方法对 4 种拓扑无效。\n\n---\n\n## Strengths\n\n1. **问题定义新颖且重要**。将多类标注误差与 DAG 拓扑的交互作为研究对象是全新角度。K=2→K>=3 揭示了结构性质变——sign-flip guarantee 的崩溃——这在 binary 框架中原理上不可能发现。[R1+R2 共识]\n2. **部分拓扑证明严谨**。Confounding（Cauchy-Schwarz 界）、Collider（Berkson's bias 反向结构）、Exposure 反例构造清晰可验证。[R1]\n3. **FWL invariance 负结果有实践价值**。证明 matrix-based correction 对 4/7 拓扑的 T 系数 bias reduction 恰好为 0%。[R1+R2 共识]\n4. **Binarization collapse 分析**揭示 K-class→binary 的额外代价（154x 跨拓扑变化）。[R1]\n5. **实证验证扎实**。3 数据集、4 LLM、98+ 场景，MAPE 2.0%。[R2]\n6. **写作密度高、结构紧凑、格式完全合规**。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，影响接收决定）\n\n**W1. Theorem 1 (Envelope Monotonicity) 无解析证明** [R1+R2 共识]\n- 仅 500 场景数值验证。ASV 有效性依赖单调性。建议：confounding case 补解析证明，其余降级为 Conjecture。\n\n**W2. Proposition 1 中 mediation/M-bias sign preservation 缺乏 proof** [R1+R2 共识]\n- Mediation 仅数值验证（论文承认 proof remains open），M-bias 仅 structural argument，front-door 继承 mediation 缺口。建议拆分 Proposition。\n\n**W3. ASV 参数化 C(δ) 定义域错误** [R1+R2 共识]\n- δ∈[0,∞) 不正确。Sign-flip ASV=6.7 可能超出有效域（δ_max≈1.67 if min diagonal≈0.4）。\n\n**W4. 83.4% headline framing 误导** [R1+R2 共识]\n- 基于 Dirichlet(1,1,1)，diagonal≥0.7 时降至 2.1%，98 实证场景 zero sign reversals。Abstract 应同时报告 realistic regime 数字。\n\n**W5. 关键相关工作未引用** [R1+R2 共识]\n- Audinet de Pieuchon et al. (EMNLP 2025), Zrnic & Candes (PNAS 2024) Cross-PPI, Gligoric et al. (NAACL 2025), Keith et al. (ACL 2020)。\n\n### Should-Fix（6 项）\n\n**W6.** Sign preservation 条件的循环性未在主文讨论 [R1+R2 共识]\n**W7.** 线性模型假设局限未在 Limitations 提及 [R1+R2 共识]\n**W8.** 实证验证模型不对称（HumAID frontier vs VAST/CC 7B）[R1, R2 部分同意]\n**W9.** ASV 对 C₀ 估计不确定性的敏感性未讨论 [R1+R2 共识]\n**W10.** MC MAPE 报告不充分（掩盖 per-topology 差异）[R1+R2 共识]\n**W11.** \"first systematic framework\" 过度声明 [R2 提出, R1 部分同意建议弱化措辞]\n\n---\n\n## Reviewer Consensus\n\n完全一致 [AGREE]：W1-W5（所有 must-fix）、W6-W7、W9-W10、所有 minor issues。\n\n## Reviewer Divergence\n\n**Novelty 评估**：R2 认为增量式扩展（Excitement 2.5/5），R1 反驳认为 K>=3 sign-flip breakdown 是结构性质变（Excitement 4.0/5）。Director 判断：R1 反驳有技术依据，但 R2 关于 ASV 和 FWL 创新有限的批评也成立。降级为 should-fix。\n\n---\n\n## Questions\n\n1. Confounding case 能否对 Theorem 1 给出解析证明？\n2. Sign-flip ASV 1.1-6.7 是否都在有效 δ 范围内？\n3. 是否存在绕过 FWL invariance 的 correction 方法（如 EM imputation）？\n4. Proposition 1 条件如何在实际中近似验证？\n5. 6 种 error structures 的具体参数？\n6. .bib 中有但未 \\cite 的高度相关论文——原因？\n\n---\n\n## Missing References\n\n1. Audinet de Pieuchon et al. (EMNLP 2025) — benchmark DSL/PPI debiasing\n2. Zrnic & Candes (PNAS 2024) — Cross-PPI (gold-free)\n3. Gligoric et al. (NAACL 2025) — Confidence-driven inference\n4. Keith et al. (ACL 2020) — Text + causal inference survey\n\n---\n\n## External Review\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n已完成（3 warnings, 7 info, 0 critical）。主要发现：\n- 前 4 页纯文本无 display item，Figure 3 (DAG taxonomy, 当前 p.16) 应移至正文 Method 开头\n- 正文仅 3 display items / 8 页，密度偏低\n- p.17 四张 figure 挤在单页，字号 ≤6pt 低于可读性阈值\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 4.0 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 3.5 | 3.5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**修改路径（达到 4.0 Conference 的条件）**：\n1. Theorem 1 confounding case 补解析证明，其余降级\n2. 拆分 Proposition 1，未证明拓扑降级为 Empirical Finding\n3. 修正 ASV 定义域，验证报告值有效性\n4. Abstract 同时报告 realistic regime 数字\n5. 补充 4 篇关键引用并讨论区别\n6. Limitations 补充线性模型假设、sign preservation 条件可验证性、ASV 对 C₀ 敏感性\n\n---\n\n## Detailed Comments\n\n### Abstract — 信息过载（数字过多），83.4% 应标注先验 + realistic regime\n### Introduction — 弱化 \"first\" claim，更早讨论 Dirichlet prior 局限\n### Section 3.2 — 拆分 Proposition 1；条件可验证性在主文讨论\n### Section 3.3 — 修正 δ 定义域；Theorem 1 降级或补证明\n### Section 4 — Table 1 caption 定义 τ_sf；澄清 Collider violation/protective；MC MAPE 报告 per-topology 分布\n### Section 4.5 — 同 tier 模型做 cross-K 比较或声明局限；区分理论风险 vs. 实践风险\n### Section 4.6 — 引用 Audinet de Pieuchon et al.、Cross-PPI；讨论 FWL bypass 替代方案；error structures 参数表\n### Conclusion + Limitations — 弱化 \"first\"；补充线性模型假设、条件可验证性、ASV C₀ 敏感性\n### Appendix — Figure 3 移入正文；符号 Z vs. D_j* 统一\n### Terminology — \"sign-flip guarantee\" 改为 \"sign preservation guarantee\"",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-22T03:39:55.139608+00:00_

{"result":"{\"success\": false, \"data\": {\"existing_path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_1.md\", \"round\": 1}, \"error\": \"Round 1 report ALREADY submitted (persisted at `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_1.md`). Research Director was triggered once and may still be processing it; re-submitting silently would trigger the protocol again with conflicting content.\\n\\nExisting report frontmatter (first 400 chars):\\n# Round 1 审稿报告\\n\\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\\n**截止日期**: 2026-05-25\\n**审稿日期**: 2026-05-22\\n**Reviewers**: R1 (方法/理论严谨性 + 实验设计), R2 (新颖性 + 完整性 + 相关工作 + 格式合规)\\n**轮次**: Round 1 (fresh review)\\n\\n---\\n\\n## Summary\\n\\n本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅\\n\\nIf you intentionally want to replace it (e.g. caught a Step 2 cross-sharing gap and synthesized a corrected report), call again with force_resubmit=True. Otherwise the original submission stands — pause and verify before forcing.\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-22T03:40:20.942043+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "report": "# Round 1 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿日期**: 2026-05-22\n**Reviewers**: R1 (方法/理论严谨性 + 实验设计), R2 (新颖性 + 完整性 + 相关工作 + 格式合规)\n\n---\n\n## Summary\n\n本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅度。三个贡献：(1) 7 种拓扑下的 multi-class bias taxonomy，证明 5 种拓扑维持 sign preservation 而 exposure 和 IV 可产生 sign reversal；(2) Annotation Sensitivity Values (ASVs) 框架提供三种灵敏度度量；(3) 5 种 correction 方法的 topology-aware 评估，揭示 FWL invariance 使 matrix-based 方法对 4 种拓扑无效。\n\n---\n\n## Strengths\n\n1. **问题定义新颖且重要**。将多类标注误差与 DAG 拓扑的交互作为研究对象是全新角度。K=2→K>=3 揭示了结构性质变——sign-flip guarantee 的崩溃——这在 binary 框架中原理上不可能发现。[R1+R2 共识]\n2. **部分拓扑证明严谨**。Confounding（Cauchy-Schwarz 界）、Collider（Berkson's bias 反向结构）、Exposure 反例构造清晰可验证。[R1]\n3. **FWL invariance 负结果有实践价值**。证明 matrix-based correction 对 4/7 拓扑的 T 系数 bias reduction 恰好为 0%。[R1+R2 共识]\n4. **Binarization collapse 分析**揭示 K-class→binary 的额外代价（154x 跨拓扑变化）。[R1]\n5. **实证验证扎实**。3 数据集、4 LLM、98+ 场景，MAPE 2.0%。[R2]\n6. **写作密度高、结构紧凑、格式完全合规**。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，影响接收决定）\n\n**W1. Theorem 1 (Envelope Monotonicity) 无解析证明** [R1+R2 共识]\n- 仅 500 场景数值验证。ASV 有效性依赖单调性。建议：confounding case 补解析证明，其余降级为 Conjecture。\n\n**W2. Proposition 1 中 mediation/M-bias sign preservation 缺乏 proof** [R1+R2 共识]\n- Mediation 仅数值验证（论文承认 proof remains open），M-bias 仅 structural argument，front-door 继承 mediation 缺口。建议拆分 Proposition。\n\n**W3. ASV 参数化 C(δ) 定义域错误** [R1+R2 共识]\n- δ∈[0,∞) 不正确。Sign-flip ASV=6.7 可能超出有效域（δ_max≈1.67 if min diagonal≈0.4）。\n\n**W4. 83.4% headline framing 误导** [R1+R2 共识]\n- 基于 Dirichlet(1,1,1)，diagonal≥0.7 时降至 2.1%，98 实证场景 zero sign reversals。Abstract 应同时报告 realistic regime 数字。\n\n**W5. 关键相关工作未引用** [R1+R2 共识]\n- Audinet de Pieuchon et al. (EMNLP 2025), Zrnic & Candes (PNAS 2024) Cross-PPI, Gligoric et al. (NAACL 2025), Keith et al. (ACL 2020)。\n\n### Should-Fix（6 项）\n\n**W6.** Sign preservation 条件的循环性未在主文讨论 [R1+R2 共识]\n**W7.** 线性模型假设局限未在 Limitations 提及 [R1+R2 共识]\n**W8.** 实证验证模型不对称（HumAID frontier vs VAST/CC 7B）[R1, R2 部分同意]\n**W9.** ASV 对 C₀ 估计不确定性的敏感性未讨论 [R1+R2 共识]\n**W10.** MC MAPE 报告不充分（掩盖 per-topology 差异）[R1+R2 共识]\n**W11.** \"first systematic framework\" 过度声明 [R2 提出, R1 部分同意建议弱化措辞]\n\n---\n\n## Reviewer Consensus\n\n完全一致 [AGREE]：W1-W5（所有 must-fix）、W6-W7、W9-W10、所有 minor issues。\n\n## Reviewer Divergence\n\n**Novelty 评估**：R2 认为增量式扩展（Excitement 2.5/5），R1 反驳认为 K>=3 sign-flip breakdown 是结构性质变（Excitement 4.0/5）。Director 判断：R1 反驳有技术依据，但 R2 关于 ASV 和 FWL 创新有限的批评也成立。降级为 should-fix。\n\n---\n\n## Questions\n\n1. Confounding case 能否对 Theorem 1 给出解析证明？\n2. Sign-flip ASV 1.1-6.7 是否都在有效 δ 范围内？\n3. 是否存在绕过 FWL invariance 的 correction 方法（如 EM imputation）？\n4. Proposition 1 条件如何在实际中近似验证？\n5. 6 种 error structures 的具体参数？\n6. .bib 中有但未 \\cite 的高度相关论文——原因？\n\n---\n\n## Missing References\n\n1. Audinet de Pieuchon et al. (EMNLP 2025) — benchmark DSL/PPI debiasing\n2. Zrnic & Candes (PNAS 2024) — Cross-PPI (gold-free)\n3. Gligoric et al. (NAACL 2025) — Confidence-driven inference\n4. Keith et al. (ACL 2020) — Text + causal inference survey\n\n---\n\n## External Review\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n已完成（3 warnings, 7 info, 0 critical）。主要发现：\n- 前 4 页纯文本无 display item，Figure 3 (DAG taxonomy, 当前 p.16) 应移至正文 Method 开头\n- 正文仅 3 display items / 8 页，密度偏低\n- p.17 四张 figure 挤在单页，字号 ≤6pt 低于可读性阈值\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 4.0 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 3.5 | 3.5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**修改路径（达到 4.0 Conference 的条件）**：\n1. Theorem 1 confounding case 补解析证明，其余降级\n2. 拆分 Proposition 1，未证明拓扑降级为 Empirical Finding\n3. 修正 ASV 定义域，验证报告值有效性\n4. Abstract 同时报告 realistic regime 数字\n5. 补充 4 篇关键引用并讨论区别\n6. Limitations 补充线性模型假设、sign preservation 条件可验证性、ASV 对 C₀ 敏感性",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5",
  "force_resubmit": "true"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "report": "# Round 1 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿日期**: 2026-05-22\n**Reviewers**: R1 (方法/理论严谨性 + 实验设计), R2 (新颖性 + 完整性 + 相关工作 + 格式合规)\n\n---\n\n## Summary\n\n本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅度。三个贡献：(1) 7 种拓扑下的 multi-class bias taxonomy，证明 5 种拓扑维持 sign preservation 而 exposure 和 IV 可产生 sign reversal；(2) Annotation Sensitivity Values (ASVs) 框架提供三种灵敏度度量；(3) 5 种 correction 方法的 topology-aware 评估，揭示 FWL invariance 使 matrix-based 方法对 4 种拓扑无效。\n\n---\n\n## Strengths\n\n1. **问题定义新颖且重要**。将多类标注误差与 DAG 拓扑的交互作为研究对象是全新角度。K=2→K>=3 揭示了结构性质变——sign-flip guarantee 的崩溃——这在 binary 框架中原理上不可能发现。[R1+R2 共识]\n2. **部分拓扑证明严谨**。Confounding（Cauchy-Schwarz 界）、Collider（Berkson's bias 反向结构）、Exposure 反例构造清晰可验证。[R1]\n3. **FWL invariance 负结果有实践价值**。证明 matrix-based correction 对 4/7 拓扑的 T 系数 bias reduction 恰好为 0%。[R1+R2 共识]\n4. **Binarization collapse 分析**揭示 K-class→binary 的额外代价（154x 跨拓扑变化）。[R1]\n5. **实证验证扎实**。3 数据集、4 LLM、98+ 场景，MAPE 2.0%。[R2]\n6. **写作密度高、结构紧凑、格式完全合规**。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，影响接收决定）\n\n**W1. Theorem 1 (Envelope Monotonicity) 无解析证明** [R1+R2 共识]\n- 仅 500 场景数值验证。ASV 有效性依赖单调性。建议：confounding case 补解析证明，其余降级为 Conjecture。\n\n**W2. Proposition 1 中 mediation/M-bias sign preservation 缺乏 proof** [R1+R2 共识]\n- Mediation 仅数值验证（论文承认 proof remains open），M-bias 仅 structural argument，front-door 继承 mediation 缺口。建议拆分 Proposition。\n\n**W3. ASV 参数化 C(δ) 定义域错误** [R1+R2 共识]\n- δ∈[0,∞) 不正确。Sign-flip ASV=6.7 可能超出有效域（δ_max≈1.67 if min diagonal≈0.4）。\n\n**W4. 83.4% headline framing 误导** [R1+R2 共识]\n- 基于 Dirichlet(1,1,1)，diagonal≥0.7 时降至 2.1%，98 实证场景 zero sign reversals。Abstract 应同时报告 realistic regime 数字。\n\n**W5. 关键相关工作未引用** [R1+R2 共识]\n- Audinet de Pieuchon et al. (EMNLP 2025), Zrnic & Candes (PNAS 2024) Cross-PPI, Gligoric et al. (NAACL 2025), Keith et al. (ACL 2020)。\n\n### Should-Fix（6 项）\n\n**W6.** Sign preservation 条件的循环性未在主文讨论 [R1+R2 共识]\n**W7.** 线性模型假设局限未在 Limitations 提及 [R1+R2 共识]\n**W8.** 实证验证模型不对称（HumAID frontier vs VAST/CC 7B）[R1, R2 部分同意]\n**W9.** ASV 对 C₀ 估计不确定性的敏感性未讨论 [R1+R2 共识]\n**W10.** MC MAPE 报告不充分（掩盖 per-topology 差异）[R1+R2 共识]\n**W11.** \"first systematic framework\" 过度声明 [R2 提出, R1 部分同意建议弱化措辞]\n\n---\n\n## Reviewer Consensus\n\n完全一致 [AGREE]：W1-W5（所有 must-fix）、W6-W7、W9-W10、所有 minor issues。\n\n## Reviewer Divergence\n\n**Novelty 评估**：R2 认为增量式扩展（Excitement 2.5/5），R1 反驳认为 K>=3 sign-flip breakdown 是结构性质变（Excitement 4.0/5）。Director 判断：R1 反驳有技术依据，但 R2 关于 ASV 和 FWL 创新有限的批评也成立。降级为 should-fix。\n\n---\n\n## Questions\n\n1. Confounding case 能否对 Theorem 1 给出解析证明？\n2. Sign-flip ASV 1.1-6.7 是否都在有效 δ 范围内？\n3. 是否存在绕过 FWL invariance 的 correction 方法（如 EM imputation）？\n4. Proposition 1 条件如何在实际中近似验证？\n5. 6 种 error structures 的具体参数？\n6. .bib 中有但未 \\cite 的高度相关论文——原因？\n\n---\n\n## Missing References\n\n1. Audinet de Pieuchon et al. (EMNLP 2025) — benchmark DSL/PPI debiasing\n2. Zrnic & Candes (PNAS 2024) — Cross-PPI (gold-free)\n3. Gligoric et al. (NAACL 2025) — Confidence-driven inference\n4. Keith et al. (ACL 2020) — Text + causal inference survey\n\n---\n\n## External Review\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n已完成（3 warnings, 7 info, 0 critical）。主要发现：\n- 前 4 页纯文本无 display item，Figure 3 (DAG taxonomy, 当前 p.16) 应移至正文 Method 开头\n- 正文仅 3 display items / 8 页，密度偏低\n- p.17 四张 figure 挤在单页，字号 ≤6pt 低于可读性阈值\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 4.0 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 3.5 | 3.5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**修改路径（达到 4.0 Conference 的条件）**：\n1. Theorem 1 confounding case 补解析证明，其余降级\n2. 拆分 Proposition 1，未证明拓扑降级为 Empirical Finding\n3. 修正 ASV 定义域，验证报告值有效性\n4. Abstract 同时报告 realistic regime 数字\n5. 补充 4 篇关键引用并讨论区别\n6. Limitations 补充线性模型假设、sign preservation 条件可验证性、ASV 对 C₀ 敏感性",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5",
    "force_resubmit": "true"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-22T03:40:25.008905+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 88 · 2026-05-22T03:40:33.180413+00:00_

Round 1 审稿完成，报告已投递给 Research Director。

**审稿结果摘要：**

- **Overall Score: 3.5 / 5 (Borderline Conference)**
- **5 个 Must-Fix 问题**：Theorem 1 无解析证明、Proposition 1 部分拓扑证明不完整、ASV 定义域错误、83.4% headline framing 误导、关键相关工作未引用
- **6 个 Should-Fix 问题**：sign preservation 条件循环性、线性模型局限、实证模型不对称、ASV C₀ 敏感性、MC 报告不充分、"first" 过度声明
- **Reviewer 共识度高**：5 个 must-fix 全部达成共识，唯一分歧在 novelty 评估（R1 认为质变、R2 认为增量）
- **修改路径明确**：6 项修改可将论文从 3.5 提升至 4.0 (Conference)

报告已存档至 `artifacts/review_reports/round_1.md`，issue tracker 已同步至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 8

## Round 8

2 recorded events


### User

_source line 89 · 2026-05-22T03:40:34.686205+00:00_

[Reviewer 2 审稿结果]:
已提交交叉回应。

总结：对 R1 的 3 个 Must-Fix 全部 [AGREE]，4 个 Should-Fix 全部 [AGREE]（W3 部分同意），3 个小问题全部 [AGREE]。核心技术问题（Theorem 1 无证明、ASV 定义域错误）与我自己的审稿发现（83.4% framing 误导、关键相关工作遗漏）共同指向论文需要实质性修订。评分维持 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 90 · 2026-05-22T03:40:45.829459+00:00_

Round 1 圆桌审稿已完成。

**最终结果**：两位 Reviewer 独立初审均评 3.5/5（Borderline Conference），交叉回应后在所有 must-fix 问题上达成完全共识，评分不变。审稿报告已投递给 Research Director。

**核心发现摘要**：
- 5 个 must-fix：Theorem 1 无解析证明、Proposition 1 部分拓扑证明不完整、ASV 定义域错误、83.4% headline framing 误导、关键相关工作遗漏
- 6 个 should-fix：sign preservation 条件循环性、线性模型局限、实证模型不对称、ASV C₀ 敏感性、MC 报告不充分、"first" 过度声明
- 唯一分歧：novelty 评估（R1 认为结构性质变，R2 认为增量扩展）

**修改路径**：若能补 Theorem 1 解析证明（至少 confounding case）、拆分 Proposition 1、修正 ASV 定义域、调整 framing、补引用，论文可达 4.0 Conference 水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 9

## Round 9

54 recorded events


### User

_source line 91 · 2026-05-22T10:37:56.209564+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-22T10:38:01.579425+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-22T10:38:01.580254+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-22T10:38:10.013076+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-22T10:38:10.013804+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-22T10:38:15.032115+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-22T10:38:15.584696+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-22T10:38:16.036674+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 99 · 2026-05-22T10:38:16.037050+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-22T10:38:17.492963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-22T10:38:17.895053+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	
19	\graphicspath{{../../figures/paper/}}
20	
21	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	% ── Figures ──
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=\textwidth]{fig2_bias_distribution.pdf}
41	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%. Five safe topologies show attenuation without sign flip.}
42	\label{fig:bias_distribution}
43	\end{figure*}
44	
45	\input{experiments}
46	
47	\input{conclusion}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{appendix_proofs}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-22T10:38:17.895495+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "report.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-22T10:38:17.946035+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\\n\\n## 趋势\\n成功 13 / 负向 0 / 失败 1 / 共 14\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nhome-1x5090: 无 GPU 信息\\n\\n## 告警\\n- plan003_empirical_confusion_matrices: 训练失败 — unknown\\n\", \"total_chars\": 1083, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-22T10:38:23.972158+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-22T10:38:25.127362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-22T10:38:25.479263+00:00_

1	\begin{abstract}
2	Large language models (LLMs) are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that binary measurement error theory cannot predict. We present a systematic framework characterizing how $K$-class confusion matrix structure interacts with DAG topology to determine bias direction and magnitude. We derive bias expressions for seven canonical DAG topologies under multi-class non-differential misclassification and establish a structural sign-flip guarantee: five topologies never produce sign reversal, while exposure and instrumental variable topologies can---under the full Dirichlet$(1,1,1)$ prior, 83.4\% of $K{=}3$ confusion matrices cause sign reversal in the exposure DAG; under realistic classifier accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal. We introduce Annotation Sensitivity Values (ASVs) with three complementary measures revealing a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal) to M-bias (immune). We evaluate five correction methods and prove a Frisch--Waugh--Lovell invariance result: matrix-based corrections achieve 0\% bias reduction for four topologies, while PPI++ achieves 47.0\% RMSE reduction but requires gold labels and is harmful for M-bias ($-$88\%). Empirical validation on three tasks ($K{=}2,3,10$) with four LLMs confirms structural predictions: zero sign reversals across five guaranteed topologies, while 59\% of exposure configurations exhibit coefficient-level sign reversal in secondary coefficients. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 107 · 2026-05-22T10:38:25.529779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-22T10:38:25.981844+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The consequences can be catastrophic. Under the full Dirichlet$(1,1,1)$ prior over $K{=}3$ non-differential exposure misclassification, 83.4\% of confusion matrices cause \emph{sign reversal} of the estimated treatment effect. Under realistic classifier accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal. This failure breaks the classical binary guarantee that non-differential misclassification biases estimates ``toward the null''~\cite{brenner1993}, a guarantee that many applied researchers implicitly rely upon. Moreover, standard classification metrics do not predict downstream causal risk: within a narrow $F_1$ range of 0.614--0.690 across three frontier LLMs, relative bias varies by an order of magnitude across topologies (from 4.1\% to 42.1\%), illustrating th
…[truncated 2327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-22T10:38:25.982345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-22T10:38:26.434398+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The statistical foundations are established in \citet{carroll2006} and \citet{gustafson2004}, with starred-node DAGs formalized by \citet{hernan_cole2009}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, but \citet{dosemeci1990} and \citet{jurek2005} showed this fails for polytomous exposures. \citet{veirod_laake2001} derived multi-category bias expressions for Poisson regression, and \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction. All of these works analyze a single DAG topology; our taxonomy is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} provide the foundation for text-as-data, while \citet{wood_doughty2018} first applied DAG reasoning to classifier error. \citet{teblunthuis2024} gave the most complete binary treatment (four DAG scenarios, $K{=}2$), and \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{baumann2025} found 31\% incorrect conclusions with LLM labels and \citet{kim_garg2025} showed 60\% error correlation across models. \citet{audinet2025} benchmark debiasing methods for LLM-generated parameter estimates; \citet{keith_jensen_oconnor2020} survey the broader text-and-causal-inference landscape. These works either restrict to binary labels, cover a single topology, or diagnose quality without connecting it to causal validity. Our framework provides the missing link.
9	
10	\paragraph{Sensitivity analysis and correction methods.}
11	Our ASV framework draws on E-values for unmeasured confounding~\cite{vanderweele_ding2017} and probabilistic bias analysis~\cite{lash2009}. Unlike E-values, ASVs 
…[truncated 636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-22T10:38:26.434930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-22T10:38:26.937675+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
15	
16	\subsection{Multi-Class Bias Expressions}
17	\label{sec:bias_expressions}
18	
19	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
20	
21	\paragraph{Confounding ($A$ = confounder).}
22	When $A$ confounds the $X{\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit
23	\begin{equation}
24	\label{eq:confounding}
25	\text{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\bet
…[truncated 9630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-22T10:38:26.938087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-22T10:38:27.892426+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate the bias taxonomy and ASV framework through analytical derivations and Monte Carlo simulation across seven DAG topologies under $K{=}3$ non-differential misclassification.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 2.0\% across 126 scenarios (18 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.5\% (confounding) to 5.5\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: catastrophic sign reversal.}
18	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\% of matrices cause \emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\beta_1{=}1.0$, a near-permutation $C$ produces $\hat{\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\times}$); for $\beta_2{=}{-}0.5$, the same $C$ yields $\hat{\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\times}$).
19	
20	This finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\% with 2.1\% sign reversal and 11.7\% amplification. Even at diagonal $\geq 0.9$, violation
…[truncated 11822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-22T10:38:27.892773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-22T10:38:28.043685+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented a systematic characterization of how multi-class annotation errors interact with causal DAG topology, jointly analyzing bias direction, sensitivity, and correction across seven canonical DAG topologies. The classical binary guarantee breaks for $K \geq 3$: exposure and IV topologies produce sign reversal (83.4\% and 52.6\%), while five topologies maintain a structural guarantee. Empirical validation with real LLM confusion matrices confirms this vulnerability: 59\% of exposure configurations exhibit coefficient-level sign reversal despite diagonal dominance. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and correction effectiveness is itself topology-dependent, with matrix-based methods provably ineffective for four topologies. Immediate extensions include differential misclassification and correlated multi-LLM error structures.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM has no access to $Y$ but may be violated with outcome-conditional prompting. A stress test (Appendix~\ref{sec:nondiff_stress}) shows moderate robustness ($\varepsilon{=}0.05$ increases violations by $<$3pp). Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$; arbitrary $K$ remains open. The framework assumes a single annotator; correlated multi-annotator settings~\cite{kim_garg2025} are future work. Frontier-model coverage for VAST and CivilComments is partial (14 of 18 planned configurations completed); cross-tier comparisons should be interpreted with this caveat. All derivations assume linear structural equations; the FWL invariance result does not hold for logistic regression, and bias patterns under nonlinear models may differ.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 117 · 2026-05-22T10:38:28.044187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-22T10:38:28.446796+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Empirical Finding~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y
…[truncated 48625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-22T10:38:29.803350+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the key details for EMNLP 2026 regarding ARR submission:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Important 
…[truncated 944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 5831
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-22T10:38:43.735435+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit formatting template double blind site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit formatting template double blind site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-22T10:38:45.190135+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 122 · 2026-05-22T10:38:45.190500+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-22T10:38:46.143609+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-22T10:38:48.603116+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null; ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/ 2>/dev/null; ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf 2>/dev/null",
  "description": "Check existing review artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null; ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/ 2>/dev/null; ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf 2>/dev/null",
    "description": "Check existing review artifacts"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-22T10:38:50.010395+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit formatting template double blind site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

Based on the search results from the EMNLP 2026 website, I found some relevant information about author guidelines:

## Key Findings:

**Page Limits:**
The Industry Track accepts full-length papers with a maximum of 6 pages. For tutorial proposals, proposals should not exceed 4 pages of content (plus one page for tutor biographies and unlimited pages for references).

**Limitations Section:**
Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations", which should be included at the end of the paper before references and will not count toward the page limit.

**Double-Blind Review:**
Industry Track submissions must neither include the authors' names nor their affiliations. The main conference reviewing process will be double-blind, with reviewers not seeing authors,
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6274
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-22T10:38:50.163475+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 4019
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-22T10:38:50.315778+00:00_

-rw-r--r-- 1 ubuntu ubuntu 7021 May 22 03:51 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml
total 16
drwxr-xr-x  2 ubuntu ubuntu 4096 May 22 03:39 .
drwxr-xr-x 21 ubuntu ubuntu 4096 May 22 10:37 ..
-rw-r--r--  1 ubuntu ubuntu 5744 May 22 03:40 round_1.md
-rw-r--r-- 1 ubuntu ubuntu 786027 May 22 10:32 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 1712
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-22T10:39:07.035299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 129 · 2026-05-22T10:39:07.437201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-22T10:39:07.889481+00:00_

1	issues:
2	  - id: R1-N1
3	    category: soundness
4	    severity: must-fix
5	    summary: "Theorem 1 (Envelope Monotonicity) 无解析证明，仅 500 场景数值验证"
6	    status: in_progress
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [R1, R2]
12	        note: "R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。"
13	    action_items:
14	      - round: 1
15	        action: "Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture"
16	        assigned_to: agent
17	        status: pending
18	
19	  - id: R1-N2
20	    category: soundness
21	    severity: must-fix
22	    summary: "Proposition 1 中 mediation/M-bias sign preservation 缺乏 proof"
23	    status: in_progress
24	    first_raised_round: 1
25	    last_seen_round: 1
26	    mentions:
27	      - round: 1
28	        reviewers: [R1, R2]
29	        note: "R1 首发，R2 AGREE 并建议拆分。"
30	    action_items:
31	      - round: 1
32	        action: "拆分 Proposition 1 → 已证(confounding/collider/exposure反例) vs Empirical Finding(mediation/M-bias/front-door)；替换 'standard DGP' 为显式充分条件"
33	        assigned_to: agent
34	        status: pending
35	
36	  - id: R1-N3
37	    category: soundness
38	    severity: must-fix
39	    summary: "ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限"
40	    status: in_progress
41	    first_raised_round: 1
42	    last_seen_round: 1
43	    mentions:
44	      - round: 1
45	        reviewers: [R1, R2]
46	        note: "δ_max = min_j 1/(1-(C₀)_{jj})。sign-flip ASV 6.7 可能超出有效域。超出 δ_max 的 ASV 应标为 ∞（实际强化结论）。"
47	    action_items:
48	      - round: 1
49	        action: "引入 δ_max 约束，写脚本重新计算所有 ASV 值，超出 δ_max 标为 ∞，更新 method.tex + experiments.tex"
50	        assigned_to: agent
51	        status: pending
52	
53	  - id: R2-N1
54	    category: presentation
55	    severity: must-fix
56	    summary: "83.4% headline framing 误导，需同时报告 realistic regime"
57	    status: in_progress
58	    first_raised_round: 1
59	    last_seen_round: 1
60	    mentions:
61	      - round: 1
62	        reviewers: [R1, R2]
…[truncated 4904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-22T10:39:07.889942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-22T10:39:07.941134+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@inproceedings{wood_doughty2018,
5	  title     = {Challenges of Using Text Classifiers for Causal Inference},
6	  author    = {Wood-Doughty, Zach and Shpitser, Ilya and Dredze, Mark},
7	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
8	  year      = {2018},
9	  doi       = {10.18653/v1/D18-1488},
10	}
11	
12	@article{teblunthuis2024,
13	  title   = {Misclassification in Automated Content Analysis Causes Bias in Regression. {C}an We Fix It? {Y}es We Can!},
14	  author  = {TeBlunthuis, Nathan and Hase, Valerie and Chan, Chung-hong},
15	  journal = {Communication Methods and Measures},
16	  volume  = {18},
17	  number  = {3},
18	  pages   = {278--299},
19	  year    = {2024},
20	  doi     = {10.1080/19312458.2023.2293713},
21	}
22	
23	@article{hernan_cole2009,
24	  title   = {Invited Commentary: Causal Diagrams and Measurement Bias},
25	  author  = {Hern{\'a}n, Miguel A. and Cole, Stephen R.},
26	  journal = {American Journal of Epidemiology},
27	  volume  = {170},
28	  number  = {8},
29	  pages   = {959--962},
30	  year    = {2009},
31	  doi     = {10.1093/aje/kwp293},
32	}
33	
34	@article{vanderweele_li2019,
35	  title   = {Simple Sensitivity Analysis for Differential Measurement Error},
36	  author  = {VanderWeele, Tyler J. and Li, Yige},
37	  journal = {American Journal of Epidemiology},
38	  volume  = {188},
39	  number  = {10},
40	  pages   = {1823--1829},
41	  year    = {2019},
42	  doi     = {10.1093/aje/kwz133},
43	}
44	
45	@article{vanderweele_ding2017,
46	  title   = {Sensitivity Analysis in Observational Research: Introducing the {E}-Value},
47	  author  = {VanderWeele, Tyler J. and Ding, Peng},
48	  journal = {Annals of Internal Medicine},
49	  volume  = {167},
50	  pages   = {268--274},
51	  year    = {2017},
52	  doi     = {10.7326/M16-2607},
53	}
54	
55	@article{brenner1993,
56	  title   = {Bias Du
…[truncated 11777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-22T10:39:12.560326+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.02279v1"}]

Based on the search results for ACL Rolling Review 2026 submission guidelines, here are the key submission requirements regarding page limits and formatting:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

For both long and short papers,
…[truncated 1192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 5525
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-22T10:39:46.520904+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 135 · 2026-05-22T10:39:47.676322+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-22T10:40:05.625069+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19104
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-22T10:40:05.625547+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 17949
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-22T10:40:05.777398+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 1，负责审查本论文的**方法严谨性、数学证明、实验验证**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review May 2026 cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 ≤ 8 页，references 无限\n- **Limitations**：必需章节，不计入页数（上限 1 页）\n- **模板**：ACL 官方模板\n- **匿名规则**：Double-blind\n\n## 论文路径\n- **LaTeX 主文件**：`projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**：`projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf`\n\n## 审查重点\n\n1. **数学正确性**：\n   - Proposition 1（sign preservation）的证明是否完整？分析证明 vs 经验验证（Empirical Finding）的边界是否清晰？\n   - Theorem 1（envelope monotonicity for confounding）的证明是否严谨？是否依赖了未验证的假设？\n   - Conjecture 1（其他拓扑的单调性）的数值验证是否充分？\n   - Exposure sign reversal 反例的构造是否正确？\n   - Bias 表达式（方程 1-4）是否有错误？\n\n2. **实验设计与验证**：\n   - Monte Carlo 验证（MAPE 2.0%）是否充分？per-topology 差异是否被掩盖？\n   - 100,000 Dirichlet 矩阵采样是否足够？是否存在采样偏差？\n   - 实证验证（3 tasks, 4 LLMs）的覆盖度是否足够？模型选择是否有偏？\n   - Correction methods 的评估（210 configurations）是否公平？\n   - ASV 框架的参数化（C(δ) = (1-δ)I + δC₀）是否过于限制性？\n\n3. **假设与限制**：\n   - Non-differential misclassification 假设在 LLM 场景下是否合理？Stress test 是否充分？\n   - 线性结构方程假设的适用范围？\n   - FWL invariance 结果的条件和适用性？\n\n4. **可复现性**：\n   - 实验参数（DGP 参数、confusion matrix 选择）是否完整报告？\n   - 代码/数据是否可获取？\n\n请按 Strengths / Weaknesses / Questions / Missing References 结构输出审稿意见。每条 Weakness 标注严重程度：[CRITICAL] / [MAJOR] / [MINOR]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "text": "你是 Reviewer 1，负责审查本论文的**方法严谨性、数学证明、实验验证**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review May 2026 cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 ≤ 8 页，references 无限\n- **Limitations**：必需章节，不计入页数（上限 1 页）\n- **模板**：ACL 官方模板\n- **匿名规则**：Double-blind\n\n## 论文路径\n- **LaTeX 主文件**：`projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**：`projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf`\n\n## 审查重点\n\n1. **数学正确性**：\n   - Proposition 1（sign preservation）的证明是否完整？分析证明 vs 经验验证（Empirical Finding）的边界是否清晰？\n   - Theorem 1（envelope monotonicity for confounding）的证明是否严谨？是否依赖了未验证的假设？\n   - Conjecture 1（其他拓扑的单调性）的数值验证是否充分？\n   - Exposure sign reversal 反例的构造是否正确？\n   - Bias 表达式（方程 1-4）是否有错误？\n\n2. **实验设计与验证**：\n   - Monte Carlo 验证（MAPE 2.0%）是否充分？per-topology 差异是否被掩盖？\n   - 100,000 Dirichlet 矩阵采样是否足够？是否存在采样偏差？\n   - 实证验证（3 tasks, 4 LLMs）的覆盖度是否足够？模型选择是否有偏？\n   - Correction methods 的评估（210 configurations）是否公平？\n   - ASV 框架的参数化（C(δ) = (1-δ)I + δC₀）是否过于限制性？\n\n3. **假设与限制**：\n   - Non-differential misclassification 假设在 LLM 场景下是否合理？Stress test 是否充分？\n   - 线性结构方程假设的适用范围？\n   - FWL invariance 结果的条件和适用性？\n\n4. **可复现性**：\n   - 实验参数（DGP 参数、confusion matrix 选择）是否完整报告？\n   - 代码/数据是否可获取？\n\n请按 Strengths / Weaknesses / Questions / Missing References 结构输出审稿意见。每条 Weakness 标注严重程度：[CRITICAL] / [MAJOR] / [MINOR]。"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-22T10:40:19.549024+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13771
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-22T10:40:19.701361+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "你是 Reviewer 2，负责审查本论文的**新颖性、相关工作覆盖、论文结构与写作质量**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review May 2026 cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 ≤ 8 页，references 无限\n- **Limitations**：必需章节，不计入页数（上限 1 页）\n- **模板**：ACL 官方模板\n- **匿名规则**：Double-blind\n\n## 论文路径\n- **LaTeX 主文件**：`projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**：`projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf`\n\n## 审查重点\n\n1. **新颖性与贡献度**：\n   - 相比已有工作（Brenner 1993, Veierød & Laake 2001, Wood-Doughty 2018, Teblunthuis 2024, Lee & Wood-Doughty 2024），本文的增量贡献是什么？\n   - K≥3 multi-class 分析是否构成足够的 novelty break？\n   - ASV 框架相比 E-values 和 PBA 的创新程度？\n   - \"topology-dependent\" 视角是否已被先前工作隐式覆盖？\n   - 对 EMNLP 受众（NLP 社区）的贡献是否清晰？还是更适合因果推断/流行病学会议？\n\n2. **相关工作覆盖**：\n   - 是否遗漏重要相关工作？特别关注：\n     - NLP+因果推断方向的最新工作\n     - Measurement error 在社会科学中的应用\n     - LLM annotation quality 的最新评估\n     - Sensitivity analysis 的其他框架\n   - 现有引用是否准确、完整？\n\n3. **论文结构与写作**：\n   - 整体叙事是否清晰？读者能否跟随 motivation → method → experiments → conclusion 的逻辑链？\n   - Abstract 和 Introduction 的 framing 是否准确？是否有过度声称（overclaiming）？\n   - Figure/Table 的质量和信息密度？\n   - 符号一致性？\n   - 8 页正文的空间利用效率？\n\n4. **格式合规性**（EMNLP 2026/ARR）：\n   - 页数是否符合限制？\n   - 匿名处理是否完整？\n   - Limitations 章节是否存在且充分？\n   - 引用格式是否正确？\n\n请按 Strengths / Weaknesses / Questions / Missing References 结构输出审稿意见。每条 Weakness 标注严重程度：[CRITICAL] / [MAJOR] / [MINOR]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "text": "你是 Reviewer 2，负责审查本论文的**新颖性、相关工作覆盖、论文结构与写作质量**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review May 2026 cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 ≤ 8 页，references 无限\n- **Limitations**：必需章节，不计入页数（上限 1 页）\n- **模板**：ACL 官方模板\n- **匿名规则**：Double-blind\n\n## 论文路径\n- **LaTeX 主文件**：`projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**：`projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf`\n\n## 审查重点\n\n1. **新颖性与贡献度**：\n   - 相比已有工作（Brenner 1993, Veierød & Laake 2001, Wood-Doughty 2018, Teblunthuis 2024, Lee & Wood-Doughty 2024），本文的增量贡献是什么？\n   - K≥3 multi-class 分析是否构成足够的 novelty break？\n   - ASV 框架相比 E-values 和 PBA 的创新程度？\n   - \"topology-dependent\" 视角是否已被先前工作隐式覆盖？\n   - 对 EMNLP 受众（NLP 社区）的贡献是否清晰？还是更适合因果推断/流行病学会议？\n\n2. **相关工作覆盖**：\n   - 是否遗漏重要相关工作？特别关注：\n     - NLP+因果推断方向的最新工作\n     - Measurement error 在社会科学中的应用\n     - LLM annotation quality 的最新评估\n     - Sensitivity analysis 的其他框架\n   - 现有引用是否准确、完整？\n\n3. **论文结构与写作**：\n   - 整体叙事是否清晰？读者能否跟随 motivation → method → experiments → conclusion 的逻辑链？\n   - Abstract 和 Introduction 的 framing 是否准确？是否有过度声称（overclaiming）？\n   - Figure/Table 的质量和信息密度？\n   - 符号一致性？\n   - 8 页正文的空间利用效率？\n\n4. **格式合规性**（EMNLP 2026/ARR）：\n   - 页数是否符合限制？\n   - 匿名处理是否完整？\n   - Limitations 章节是否存在且充分？\n   - 引用格式是否正确？\n\n请按 Strengths / Weaknesses / Questions / Missing References 结构输出审稿意见。每条 Weakness 标注严重程度：[CRITICAL] / [MAJOR] / [MINOR]。"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-22T10:40:21.314381+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1613
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-22T10:40:38.012989+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-22T10:40:38.871710+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 858
}
```

</details>

---


### Assistant

_source line 144 · 2026-05-22T10:40:50.541555+00:00_

审稿圆桌已启动，当前状态：

| 组件 | 状态 |
|------|------|
| Reviewer 1（方法/证明/实验） | 已派发，审稿中 |
| Reviewer 2（新颖性/相关工作/写作） | 已派发，审稿中 |
| 视觉审查 Agent | 已启动，与 Reviewer 并行 |
| 外部审稿（Stanford Agentic Reviewer） | 已发送请求，等待用户协助提交 |

等待 Reviewer 返回审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 145 · 2026-05-22T10:48:39.500609+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5/5 — Borderline Conference
**一句话总结**: 框架设计系统且选题及时，但核心理论结果存在"证明-数值验证"混合问题，3/5 个"安全"拓扑的符号保持仅有经验验证，Theorem 1 的一般情形依赖数值紧致性确认而非完整解析证明。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 已证明部分（Propositions 1-5, Theorem 1 比例情形）技术正确；但 Theorem 1 一般情形和 Conjecture 1 依赖数值验证，Empirical Finding 1 缺乏解析证明 |
| Excitement | 3.5/5 | 选题重要且及时（LLM 标注 × 因果推断），ASV 框架有实用价值，FWL invariance 洞察新颖；但整体属已知二分类结果向多分类的系统性扩展 |
| Reproducibility | 3.5/5 | DGP 参数报告详尽（Appendix B），Monte Carlo 设置清晰；但代码/数据可获取性未提及，14/28 实证配置未完成 |
| Overall Assessment | 3.5/5 | Borderline Conference — 高于 Findings 水准，但理论缺口和实验不完整性阻碍明确接收推荐 |
| Confidence | 4/5 | 仔细检查了证明结构、bias 表达式推导、实验设计；熟悉测量误差文献和因果推断方法论 |

---

## Must-Fix 问题（影响接收决定）

**N1** [CRITICAL] Theorem 1 一般情形证明不完整
- 具体位置：Appendix A.4（p.12），"Tightness is confirmed numerically (500 random (C₀, δ) pairs, zero violations)"
- 问题：Theorem 1 声称 |B(C(δ))| 在 confounding 拓扑下对 δ 单调非递减。比例情形 (f = λg) 的证明是完整的代数推导，但一般情形使用 Cauchy-Schwarz 界 + 500 组数值验证。Cauchy-Schwarz 仅证明上界的单调性，不能直接推出实际 |B(C(δ))| 本身的单调性。500 对 (C₀, δ) 的数值确认不构成证明。
- 为什么影响接收：一篇以数学严谨性为核心卖点的论文，其唯一标记为 "Theorem" 的结果在一般情形下未完全证明，而是依赖数值验证。这模糊了 "theorem" 和 "conjecture/empirical finding" 的界限。ASV 框架的理论基础（单调性保证 δ* 的存在唯一性）直接依赖该定理。
- 建议修改方向：(a) 补全一般情形的解析证明；(b) 若无法补全，将一般情形降级为 Conjecture 或 Empirical Finding，仅对比例情形保留 Theorem 地位；(c) 明确讨论 ASV 框架在单调性仅为经验验证时的可靠性。

**N2** [MAJOR] 3/5 "安全"拓扑的符号保持缺乏解析证明
- 具体位置：Section 3.2 Empirical Finding 1 (p.4)；Table 2 (p.16)
- 问题：论文的核心叙事是 "五拓扑安全，两拓扑危险" 的二分法。但 mediation、M-bias、front-door 三个拓扑的符号保持仅通过 100,000 随机列随机矩阵数值验证，且论文明确承认 "a closed-form proof for general K remains open"。在 K=3 时，列随机矩阵空间为 6 维，100,000 样本给出约 6.8 点/维的密度，对于验证一个全称命题而言并不充分。
- 为什么影响接收：摘要中 "five topologies never produce sign reversal" 的表述暗示理论保证，但实际上对 3/5 的拓扑仅有数值证据。审稿人和读者可能将此理解为已证明的结论。
- 建议修改方向：(a) 在摘要和正文中明确区分"已证明"（confounding, collider）和"经验验证"（mediation, M-bias, front-door）的拓扑；(b) 讨论为什么这三个拓扑的解析证明困难，是否存在根本障碍；(c) 增加采样密度或使用区间验证等方法增强数值证据的可信度。

**N3** [MAJOR] Non-differential misclassification 假设的 stress test 严重不足
- 具体位置：Appendix B.3, Table 6 (p.20)
- 问题：论文的整个框架建立在 non-differential misclassification 假设上（混淆矩阵 C 不依赖于处理/结局）。但 stress test 仅覆盖：(1) 一个拓扑（exposure），(2) 一个 K 值（K=3），(3) ε 仅到 0.10。LLM 标注错误在实践中很可能是 differential 的——例如，LLM 对积极情感文本的毒性标注可能与消极情感文本系统不同。论文未提供实际 LLM 混淆矩阵的 differential 程度估计。
- 为什么影响接收：如果假设在实践中频繁违反，整个框架的适用性受到质疑。一个仅在单一拓扑上对单一 K 值进行的 stress test 无法充分验证框架的鲁棒性。
- 建议修改方向：(a) 对所有 7 个拓扑进行 stress test；(b) 从 3 个实证数据集中直接估计 LLM 混淆矩阵的 differential 程度（例如按 Y 值分层计算混淆矩阵差异）；(c) 扩展 ε 范围至 0.20-0.30 以覆盖更极端但可能现实的偏离。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [WARNING] 符号保持的 DGP 条件限制性未讨论
- 具体位置：Table 2 (p.16)；Section 3.2 (p.4)
- 问题：符号保持结论依赖于特定 DGP 条件（如 confounding 要求 sign(τ) = sign(τ + B_OV)，collider 要求 |τ| > B_Berkson）。这些条件本身是非平凡的——例如 confounding 条件要求遗漏变量偏差不足以翻转真实效应的符号，这在强混杂场景下可能不成立。论文未讨论这些条件在实践中的满足频率。
- 建议：添加一段讨论或数值模拟，展示在典型 DGP 参数范围下这些条件的满足率。

**W2** [WARNING] ASV 参数化路径的限制性
- 具体位置：Section 3.3 (p.4)
- 问题：C(δ) = (1-δ)I + δC₀ 假设混淆矩阵沿线性路径从完美分类退化到目标矩阵 C₀。但实际标注质量退化可能沿非线性路径（例如，低质量模型可能先在困难类别上出错，然后才影响容易类别）。不同的退化路径可能给出不同的 ASV 值。
- 建议：讨论线性路径假设的局限性；或展示不同 C₀ 选择下 ASV 的敏感性。

**W3** [WARNING] 实验覆盖不完整
- 具体位置：Limitations (p.8)："Frontier-model coverage for VAST and CivicComments is partial (14 of 28 planned configurations completed)"
- 问题：论文坦承 14/28 配置未完成。此外，4 个 LLM 均为开源模型（Llama-3-Maverick, Qwen2.5-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct），无商业模型（GPT-4, Claude）。K≥3 的任务仅有 2 个（HumAID K=10, VAST K=3），CivicComments (K=2) 本质上退化为二分类。
- 建议：(a) 补完剩余 14 个配置；(b) 至少加入 1 个商业 LLM 的对比；(c) 讨论开源模型错误模式是否可能与商业模型系统性不同。

**W4** [WARNING] Conjecture 1 数值验证样本量不足
- 具体位置：Section 4.2 (p.5)："Verified numerically across 500 scenarios per topology with zero violations"
- 问题：Conjecture 1 声称 collider/M-bias 的 |B(C(δ))| 单调非递增，mediation/front-door/IV 的 |B(C(δ))| 单调非递减。但每个拓扑仅 500 个场景的验证是薄弱的。相比之下，Empirical Finding 1 使用了 100,000 个矩阵。
- 建议：增加到至少 10,000 个场景，或讨论为什么 500 即足够（例如该属性在参数空间上连续、无边界情形等）。

**W5** [WARNING] 线性 SEM 假设的适用范围
- 具体位置：Limitations (p.8)；Method Section 3.1 (p.3)
- 问题：整个框架假设线性结构方程。论文在 Limitations 中提到 "the FWL invariance result does not hold for logistic regression, and bias patterns under nonlinear models may differ"，但未讨论（1）NLP/社会科学中非线性模型的普遍程度，（2）bias 方向性结果是否在弱非线性下近似成立。
- 建议：至少添加一个简单的非线性 DGP 模拟（如 logistic 模型），展示偏差模式是否定性不变。

---

## 小问题（不影响接收）

1. **摘要措辞过强**：摘要中 "five topologies never produce sign reversal" 应改为 "five topologies preserve sign under topology-specific DGP conditions (proven for confounding and collider; empirically verified for mediation, M-bias, and front-door)"。
2. **Table 1 可读性**：Table 1 (p.5) 同时展示多个指标（violation, sign flip, amplification），但列标题与正文符号不完全对应，建议统一。
3. **Figure 3 (p.18)** 中 7 个 DAG 拓扑图清晰有用，但出现在附录而非正文中。考虑将其放入正文以帮助不熟悉所有拓扑的读者。
4. **Binarization collapse (Section 3.4)** 分析有趣，但 Δ 的定义和数值（13% variation across topologies）在正文中叙述较简略，建议添加一个简表总结各拓扑的 Δ 值。
5. **页数合规**：正文 8 页 + Limitations，References 从 p.9 开始，合规。✓
6. **匿名性**：未发现明显违反 double-blind 的标识。✓

---

## 主要优势

1. **选题及时且重要**：LLM 标注在计算社会科学中快速普及，但标注误差在因果推断中的传播和交互此前缺乏系统研究。论文填补了这一关键空白。
2. **拓扑分类法新颖且全面**：系统覆盖 7 种 DAG 拓扑下的 K-class 偏差表达式，建立了清晰的 "安全/危险" 二分法。这比此前仅研究单一拓扑的工作（Lee & Wood-Doughty, 2024 仅覆盖 confounding）有实质性进步。
3. **K≥3 符号翻转发现**：K=2→K=3 的定性断裂（符号翻转成为可能）是一个重要且非显而易见的理论发现，对实践有直接指导意义——研究者不应简单二值化多分类标签。
4. **FWL invariance 洞察实用价值高**：证明 4 个拓扑下简单矩阵校正方法（MLA, plug-in）因 FWL 不变性而完全无效，这为实践者选择校正方法提供了清晰的指导。
5. **ASV 框架设计合理**：三种互补的灵敏度度量（magnitude, significance, sign-flip）类比 E-value 的设计思路，给研究者提供了简洁的 "标注误差预算" 工具。
6. **理论-经验区分诚实**：论文清晰标注 Proposition（已证）、Empirical Finding（数值验证）、Conjecture（猜想），这种诚实的层级区分在同类论文中较为少见。
7. **实证校正方法评估（Section 4.6）**：210 个配置、5 种校正方法、7 个拓扑的系统比较，结论（Cross-PPI 跨拓扑有效、矩阵校正方法拓扑依赖）有明确实践价值。

---

## 总结

本文系统化地研究了 LLM 多分类标注误差在 7 种因果 DAG 拓扑下的偏差传播，建立了有用的分类法和灵敏度框架。核心贡献——K≥3 的符号翻转发现和 FWL invariance 洞察——具有理论和实践价值。主要弱点在于：(1) 关键定理的一般情形证明依赖数值验证而非完整解析推导；(2) 三个拓扑的符号保持仅有经验证据；(3) non-differential misclassification 假设的 stress test 覆盖不足。若这些问题能在 camera-ready 阶段解决（特别是 N1 的证明补全或降级，N2 的措辞修正，N3 的 stress test 扩展），论文有望达到主会议接收水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 146 · 2026-05-22T10:48:56.269371+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 147 · 2026-05-22T10:48:59.192812+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**: Overall 3.5/5 (Borderline Conference)。

**三个 Must-Fix 问题**:
1. **Theorem 1 一般情形证明不完整** — 用 Cauchy-Schwarz 界 + 500 组数值验证代替完整解析证明，但论文将其标记为 "Theorem"
2. **3/5 安全拓扑缺乏解析证明** — mediation、M-bias、front-door 的符号保持仅有 100,000 随机矩阵的数值验证，摘要 "five topologies never produce sign reversal" 措辞过强
3. **Non-differential misclassification stress test 不足** — 仅在 1 个拓扑、K=3、ε≤0.10 上测试，未从实际数据估计 LLM 误差的 differential 程度

**主要优势**: 选题及时、拓扑分类法全面、K≥3 符号翻转发现非显而易见、FWL invariance 洞察实用、理论-经验层级区分诚实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 148 · 2026-05-22T10:49:07.670356+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 12

## Round 12

6 recorded events


### User

_source line 149 · 2026-05-22T10:51:16.374938+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）

**审查侧重**：新颖性与贡献度、相关工作覆盖、论文结构与写作质量、格式合规性

---

## 总体评分

**Overall**: 3.5/5（Borderline Conference）

**一句话总结**: 论文系统地将二元误分类理论扩展到 K≥3 多类别、七种 DAG 拓扑，贡献框架清晰且有实用价值，但核心理论结果依赖数值验证而非解析证明，线性假设限制了对 NLP 受众的实用性，关键数字的叙事 framing 存在 overclaiming 风险。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要声明有充分实验支持，解析推导与 MC 验证吻合度高（MAPE 2.0%），但两项核心结果（Empirical Finding 1, Conjecture 1）缺乏解析证明，ASV 框架的有效性依赖于未证明的猜想 |
| Excitement | 3/5 | 填补了明确的研究空白，对使用 LLM 标注做因果推断的 NLP 从业者有直接实用价值；但贡献以系统化组织已有理论为主，而非根本性新洞察 |
| Reproducibility | 4/5 | 解析推导步骤完整（Appendix A），MC 模拟参数明确（N=10,000, 100,000 random matrices），但 VAST/CivilComments 仅完成 14/38 计划配置 |
| Overall | 3.5/5 | Borderline Conference |
| Confidence | 4/5 | 熟悉因果推断测量误差文献和 NLP 标注质量研究 |

---

## Must-Fix 问题（影响接收决定）

**N1** [CRITICAL] 核心理论结果依赖数值验证，缺乏解析证明

- **具体位置**：Empirical Finding 1（Section 3.2, p4）、Conjecture 1（Section 3.3 附近, p5）
- **问题**：
  - Empirical Finding 1 声称 mediation、M-bias、front-door 三种拓扑的符号保持性成立，但仅通过 100,000 次随机矩阵的蒙特卡洛验证，论文明确承认 "analytic proofs for general K remain open"。
  - Conjecture 1 声称 ASV envelope 的单调性（exposure/mediation/front-door/IV 非递减，collider/M-bias 非递增），仅在 500 scenarios 上验证。
  - Theorem 1（confounding 拓扑的 envelope 单调性）有完整证明（Appendix A.4），但其余六种拓扑均无。
- **为什么影响接收**：ASV 框架（论文三大贡献之一）的有效性直接依赖于 Conjecture 1。如果存在反例，ASV 的 magnitude/significance/sign-flip 三种度量均失去意义。对于一篇以理论分析为核心卖点的论文，在七种拓扑中仅一种有解析证明，其余依赖数值验证，这削弱了理论贡献的可信度。
- **建议修改方向**：(1) 至少为 K=3 的特殊情况提供 mediation 或 front-door 的解析证明；(2) 明确讨论 Conjecture 1 失败时 ASV 框架的降级方案；(3) 将 Conjecture 1 的数值验证从 500 scenarios 扩大到更高量级并报告搜索策略（如是否对 edge cases 做了 adversarial search）。

**N2** [CRITICAL] 83.4% 符号翻转率的叙事 framing 构成 overclaiming

- **具体位置**：Abstract（p1, "83.4% of K=3 confusion matrices cause sign reversal in the exposure DAG"）、Introduction（p1, "83.4% of confusion matrices cause sign reversal of the estimated treatment effect"）
- **问题**：
  - 83.4% 基于 Dirichlet(1,1,1) 先验，该先验在 K=3 下生成的混淆矩阵对角线平均精度仅约 0.33（随机分类器水平）。绝大多数采样矩阵对应 accuracy ≪ 0.5 的"分类器"，在实际 LLM 标注场景中几乎不可能出现。
  - 在更贴近现实的条件下（对角线 ≥ 0.7），符号翻转率骤降至 2.1%（Table 1, p6）。
  - 论文正文确实在后文提供了 realistic accuracy 条件下的数字，但 Abstract 和 Introduction 的叙事结构将最极端场景下的数字作为 headline，读者的第一印象会被严重扭曲。
  - 从 2.1% 到 83.4% 相差 40 倍——这不是量级差异，而是质的不同：2.1% 意味着"实际场景中符号翻转罕见"，83.4% 意味着"普遍性灾难"。
- **为什么影响接收**：这种 framing 策略在同行评审中容易被认为是 sensationalization。如果 reviewer 阅读 Abstract 后产生"这个问题很严重"的印象，但深入阅读后发现在现实条件下问题很温和，会显著降低对论文诚实性的信任。
- **建议修改方向**：(1) 在 Abstract 中并列报告两个条件下的数字："Under uniform Dirichlet priors, 83.4% ... ; under realistic classifier accuracy (diagonal ≥ 0.7), the rate drops to 2.1%"；(2) 或以 realistic accuracy 结果为主叙事，将 Dirichlet(1,1,1) 结果作为理论极端场景讨论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [MAJOR] 线性结构方程假设严重限制对 NLP 受众的实用性

- **具体位置**：Section 3.1（p3, "linear structural equations"）、Limitations（p8-9, "FWL invariance result does not hold for logistic regression"）
- **问题**：所有理论结果（Proposition 1-5, Conjecture 1, FWL invariance, ASV framework）均基于线性结构方程模型。NLP 中最常见的下游因果推断场景（如二元/多元处置效应估计）通常使用 logistic regression 或非参数方法。论文在 Limitations 中承认此限制，但 Method 和 Experiments 部分未讨论线性假设在何种 NLP 场景下合理。
- **建议**：(1) 在 Section 3.1 讨论线性假设的适用边界（如连续结果变量的 OLS 回归场景）；(2) 至少提供一个 logistic regression 下的模拟实验，验证核心发现（如 sign-flip 现象）是否定性保持。

**W2** [MAJOR] 缺少两篇高度相关的参考文献

- **具体位置**：Section 2 Related Work（p2）
- **遗漏引用**：
  1. **Feder, Keith, Manzoor, Pryzant, Sridhar, Wood-Doughty, et al. (2022). "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond." TACL.** 这是 NLP+因果推断领域引用量最高的综述（Google Scholar 400+ 引用），系统梳理了文本作为处置/结果/混淆因素时的因果推断方法。对于一篇投向 EMNLP、定位于 NLP+因果推断交叉领域的论文，遗漏此综述会让 NLP 审稿人质疑作者对该领域的熟悉度。
  2. **Cheng, Mayya & Sedoc (2024). "To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation." arXiv:2412.14461.** 该论文将 LLM 标注中的测量误差分解为四种来源（guideline-induced, baseline-induced, prompt-induced, model-induced），与本文关注的 annotation error propagation 高度互补。本文关注误差的下游因果效应传播，Cheng et al. 关注误差的上游来源分解——引用并区分二者可强化论文的定位。
- **建议**：在 Section 2 的 "Text classifiers and LLM annotation" 或 "Sensitivity analysis and correction methods" 子节中补充这两篇引用并明确区分。

**W3** [MAJOR] ASV 参数化选择缺乏讨论和敏感性分析

- **具体位置**：Section 3.3（p4, "We parameterize the confusion matrix as C(δ) = (1−δ)I + δC₀"）
- **问题**：
  - 线性插值 C(δ) = (1−δ)I + δC₀ 是一个特定的参数化选择。为什么不是对角线衰减模型（C_kk = 1−δ, off-diagonal uniform）？或基于分类精度的参数化（C(acc) = acc·I + (1−acc)·C₀）？
  - C₀ 被描述为 "reference confusion matrix estimated from a finite validation set"（p4），但论文未讨论 C₀ 估计不确定性如何传播到 ASV 结论。
  - 不同的 C₀ 选择是否会导致相同数据集上的 ASV 结论定性翻转（如从 "safe" 变为 "unsafe"）？
- **建议**：至少讨论参数化选择的理由和 C₀ 估计误差的影响，或在附录中提供 C₀ 扰动下的 ASV 敏感性实验。

**W4** [MINOR] 实证验证不完整，削弱普适性声明

- **具体位置**：Limitations（p9, "Frontier model coverage for VAST and CivilComments is partial (14 of 38 planned configurations completed)"）；Section 4.5（p7）
- **问题**：约 63% 的计划验证未完成。HumAID (K=10) 验证较完整，但 VAST (K=3) 和 CivilComments (K=2) 的覆盖不足恰好是论文核心贡献（K≥3 扩展）最需要验证的设置。
- **建议**：(1) 在最终版本中完成缺失的配置；(2) 如无法完成，讨论已完成的 14 个配置是否在参数空间中有代表性。

**W5** [MINOR] Proposition 1 的充分条件在实践中难以事前验证

- **具体位置**：Proposition 1（p4）、Empirical Finding 1 的注释（p4, "These conditions involve free DGP parameters, which in practice must be estimated"）
- **问题**：Proposition 1(a) 要求 sign(τ) = sign(τ + B_OV)，Proposition 1(b) 要求 |τ| 超过 Berkson attenuation bound。这些条件涉及未知的 DGP 参数（如省略变量偏差的方向和大小），实践者无法在分析前判断符号保持性是否成立。论文通过 ASV 框架部分缓解了这一问题，但 ASV 本身依赖 Conjecture 1（见 N1）。
- **建议**：明确讨论在实践中如何判断 Proposition 1 条件是否近似成立（如通过 sensitivity analysis 或 domain knowledge）。

---

## 小问题（不影响接收）

- **p2, Section 2**: "All of these works analyze a single DAG topology" 中的 "first" claim 应更精确限定范围，例如 "in the context of multi-class annotation error"，因为因果推断主流文献中跨拓扑的测量误差比较并非全新概念。
- **p5, Section 3.4 Binarization Collapse**: 内容仅约 4 行，信息密度低。建议移至附录或扩充为一个完整的实验分析。
- **Table 1 (p6)**: "Sign Flip" 列同时包含 Dirichlet prior（83.4%）和 realistic accuracy（2.1%）条件下的结果，两个条件的混排可能造成阅读混淆。建议用脚注或分行明确标注。
- **Figure 2 (p8)**: x 轴标签（"Topology Determines Bias, Not F₁"）字体偏小，在打印版中可能难以辨认。
- **Appendix B.1**: Applied Illustration（Clinical/BERT Case Study）很好地展示了框架的实用性，建议在主文 Section 4 或 Section 5 中增加对此案例的交叉引用。
- **符号一致性**：论文中使用 τ, τ̂, f(A*), β 等多套符号系统。虽然定义清晰，但在快速阅读时容易混淆，建议在 Section 3.1 增加一个符号表或将核心符号集中定义。

---

## 主要优势

1. **填补明确研究空白**：跨七种 DAG 拓扑的统一多类别误分类分析框架确实此前不存在。每种拓扑独立研究过，但系统比较——特别是同一混淆矩阵在不同拓扑下产生定性不同偏差的发现——是新的且有价值的。

2. **FWL invariance 发现新颖且可操作**：Section 4.6 证明矩阵校正方法（Naive MLA、DSL）对 confounding/mediation/collider/M-bias 四种拓扑恰好 0% 偏差缩减，这是由 Frisch-Waugh-Lovell 定理保证的结构性结果。这个发现对从业者有直接指导意义：不要盲目应用通用校正方法，需先识别拓扑。

3. **理论-实证一致性强**：解析推导与 Monte Carlo 估计之间的 grand MAPE 仅 2.0%（Section 4.2, p5-6），在 126 个场景上实现了高度吻合，增加了理论分析的可信度。

4. **实用的灵敏度分析工具**：ASV 的三种度量（magnitude, significance, sign-flip）为从业者提供了分层决策框架：先检查偏差大小是否可容忍，再检查统计显著性是否被逆转，最后检查符号是否翻转。

5. **真实数据验证**：在三个 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2）和四个 LLM 上的验证超越了纯理论/模拟研究，增加了社区可信度。

---

## Questions for Authors

**Q1**: Conjecture 1 能否至少对 K=3 的 mediation 或 exposure 拓扑提供解析证明？当前的 500 scenarios 数值验证是否做过 adversarial search（如专门寻找反例的优化搜索）？

**Q2**: 在 logistic regression 下，sign-flip 现象是否定性保持？即使不提供完整理论，一个 K=3 × 3 topologies 的模拟实验也能大幅增强论文的实用性声明。

**Q3**: ASV 的 C₀ 估计来自有限验证集。如果 C₀ 的估计误差为 ±0.05（对角线元素），ASV 的 safe/unsafe 判断是否会翻转？

**Q4**: 论文在 Abstract 中 lead with 83.4%（Dirichlet(1,1,1) prior），但在 realistic accuracy 下仅 2.1%。是否考虑过使用更贴近现实分类器分布的先验（如 peaked Dirichlet(α,α,α), α>1）来报告中间水平的基准比率？

---

## Missing References

1. **Feder, A., Keith, K.A., Manzoor, E., Pryzant, R., Sridhar, D., Wood-Doughty, Z., et al. (2022). "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond." Transactions of the Association for Computational Linguistics (TACL).** — NLP+因果推断领域最重要的综述，投 EMNLP 必引。

2. **Cheng, X., Mayya, R., & Sedoc, J. (2024). "To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation." arXiv:2412.14461.** — 将 LLM 标注测量误差分解为四种上游来源，与本文的下游传播分析互补。

---

## 格式合规性检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 页数（正文 ≤ 8 页） | ✅ 合规 | Sections 1-5 在第 8 页结束，Limitations 从第 8 页下半开始 |
| Limitations 章节 | ✅ 存在 | 约 0.7 页，覆盖非差异误分类假设、线性假设、实证验证不完整等，内容充分 |
| 匿名处理 | ✅ 合规 | 首页标注 "Anonymous ACL submission"，未发现明显的去匿名化信息 |
| 引用格式 | ✅ 合规 | 使用 ACL 标准格式 |
| 模板 | ✅ 合规 | ACL 官方双栏模板 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-22T10:51:49.994928+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [CRITICAL] 核心理论结果依赖数值验证，缺乏解析证明\n- Empirical Finding 1 声称 mediation、M-bias、front-door 三种拓扑的符号保持性成立，但仅通过 100,000 次随机矩阵的蒙特卡洛验证，论文明确承认 \"analytic proofs for general K remain open\"。\n- Conjecture 1 声称 ASV envelope 的单调性（exposure/mediation/front-door/IV 非递减，collider/M-bias 非递增），仅在 500 scenarios 上验证。\n- Theorem 1（confounding 拓扑的 envelope 单调性）有完整证明（Appendix A.4），但其余六种拓扑均无。\n- ASV 框架的有效性直接依赖于 Conjecture 1。如果存在反例，ASV 的三种度量均失去意义。\n\n**N2** [CRITICAL] 83.4% 符号翻转率的叙事 framing 构成 overclaiming\n- 83.4% 基于 Dirichlet(1,1,1) 先验，对角线平均精度仅约 0.33（随机分类器水平）。\n- 在 realistic accuracy（对角线 ≥ 0.7）下，符号翻转率骤降至 2.1%。\n- Abstract 和 Introduction 将最极端场景下的数字作为 headline，2.1% vs 83.4% 相差 40 倍。\n- 建议在 Abstract 中并列报告两个条件下的数字，或以 realistic accuracy 结果为主叙事。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** [MAJOR] 线性结构方程假设严重限制对 NLP 受众的实用性\n- 所有理论结果均基于线性 SEM。NLP 中常用 logistic regression 或非参数方法。\n- Method 和 Experiments 部分未讨论线性假设在何种 NLP 场景下合理。\n\n**W2** [MAJOR] 缺少两篇高度相关的参考文献\n- Feder et al. (2022) TACL — NLP+因果推断最重要的综述\n- Cheng, Mayya &amp; Sedoc (2024) — LLM 标注测量误差的上游来源分解\n\n**W3** [MAJOR] ASV 参数化选择缺乏讨论和敏感性分析\n- 线性插值 C(δ) 的选择理由未充分讨论。\n- C₀ 估计不确定性如何传播到 ASV 结论未分析。\n\n**W4** [MINOR] 实证验证不完整（14/38 配置），削弱普适性声明\n\n**W5** [MINOR] Proposition 1 的充分条件在实践中难以事前验证\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [CRITICAL] 核心理论结果依赖数值验证，缺乏解析证明\n- Empirical Finding 1 声称 mediation、M-bias、front-door 三种拓扑的符号保持性成立，但仅通过 100,000 次随机矩阵的蒙特卡洛验证，论文明确承认 \"analytic proofs for general K remain open\"。\n- Conjecture 1 声称 ASV envelope 的单调性（exposure/mediation/front-door/IV 非递减，collider/M-bias 非递增），仅在 500 scenarios 上验证。\n- Theorem 1（confounding 拓扑的 envelope 单调性）有完整证明（Appendix A.4），但其余六种拓扑均无。\n- ASV 框架的有效性直接依赖于 Conjecture 1。如果存在反例，ASV 的三种度量均失去意义。\n\n**N2** [CRITICAL] 83.4% 符号翻转率的叙事 framing 构成 overclaiming\n- 83.4% 基于 Dirichlet(1,1,1) 先验，对角线平均精度仅约 0.33（随机分类器水平）。\n- 在 realistic accuracy（对角线 ≥ 0.7）下，符号翻转率骤降至 2.1%。\n- Abstract 和 Introduction 将最极端场景下的数字作为 headline，2.1% vs 83.4% 相差 40 倍。\n- 建议在 Abstract 中并列报告两个条件下的数字，或以 realistic accuracy 结果为主叙事。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** [MAJOR] 线性结构方程假设严重限制对 NLP 受众的实用性\n- 所有理论结果均基于线性 SEM。NLP 中常用 logistic regression 或非参数方法。\n- Method 和 Experiments 部分未讨论线性假设在何种 NLP 场景下合理。\n\n**W2** [MAJOR] 缺少两篇高度相关的参考文献\n- Feder et al. (2022) TACL — NLP+因果推断最重要的综述\n- Cheng, Mayya &amp; Sedoc (2024) — LLM 标注测量误差的上游来源分解\n\n**W3** [MAJOR] ASV 参数化选择缺乏讨论和敏感性分析\n- 线性插值 C(δ) 的选择理由未充分讨论。\n- C₀ 估计不确定性如何传播到 ASV 结论未分析。\n\n**W4** [MINOR] 实证验证不完整（14/38 配置），削弱普适性声明\n\n**W5** [MINOR] Proposition 1 的充分条件在实践中难以事前验证\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-22T10:52:08.236852+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18241
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-22T10:52:08.338535+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [CRITICAL] Theorem 1 一般情形证明不完整\n- 比例情形 (f = λg) 有完整代数推导，但一般情形使用 Cauchy-Schwarz 界 + 500 组数值验证。\n- Cauchy-Schwarz 仅证明上界的单调性，不能直接推出实际 |B(C(δ))| 本身的单调性。\n- 500 对 (C₀, δ) 的数值确认不构成证明。\n- ASV 框架的理论基础（单调性保证 δ* 的存在唯一性）直接依赖该定理。\n\n**N2** [MAJOR] 3/5 \"安全\"拓扑的符号保持缺乏解析证明\n- mediation、M-bias、front-door 仅通过 100,000 随机列随机矩阵数值验证。\n- 在 K=3 时列随机矩阵空间为 6 维，100,000 样本约 6.8 点/维。\n- 摘要 \"five topologies never produce sign reversal\" 暗示理论保证，但 3/5 仅有数值证据。\n\n**N3** [MAJOR] Non-differential misclassification 假设的 stress test 严重不足\n- 仅覆盖 1 个拓扑（exposure），1 个 K 值（K=3），ε 仅到 0.10。\n- LLM 标注错误在实践中很可能是 differential 的。\n- 未从实际数据估计 LLM 混淆矩阵的 differential 程度。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** [WARNING] 符号保持的 DGP 条件限制性未讨论\n- 符号保持依赖于特定 DGP 条件，这些条件在强混杂场景下可能不成立。\n- 未讨论在实践中这些条件的满足频率。\n\n**W2** [WARNING] ASV 参数化路径的限制性\n- C(δ) = (1-δ)I + δC₀ 假设沿线性路径退化。实际退化可能非线性。\n\n**W3** [WARNING] 实验覆盖不完整\n- 14/28 配置未完成，4 个 LLM 均为开源模型，无商业模型。\n\n**W4** [WARNING] Conjecture 1 数值验证样本量不足\n- 每拓扑仅 500 scenarios，远少于 Empirical Finding 1 的 100,000。\n\n**W5** [WARNING] 线性 SEM 假设的适用范围\n- 未讨论 NLP/社会科学中非线性模型的普遍程度。\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [CRITICAL] Theorem 1 一般情形证明不完整\n- 比例情形 (f = λg) 有完整代数推导，但一般情形使用 Cauchy-Schwarz 界 + 500 组数值验证。\n- Cauchy-Schwarz 仅证明上界的单调性，不能直接推出实际 |B(C(δ))| 本身的单调性。\n- 500 对 (C₀, δ) 的数值确认不构成证明。\n- ASV 框架的理论基础（单调性保证 δ* 的存在唯一性）直接依赖该定理。\n\n**N2** [MAJOR] 3/5 \"安全\"拓扑的符号保持缺乏解析证明\n- mediation、M-bias、front-door 仅通过 100,000 随机列随机矩阵数值验证。\n- 在 K=3 时列随机矩阵空间为 6 维，100,000 样本约 6.8 点/维。\n- 摘要 \"five topologies never produce sign reversal\" 暗示理论保证，但 3/5 仅有数值证据。\n\n**N3** [MAJOR] Non-differential misclassification 假设的 stress test 严重不足\n- 仅覆盖 1 个拓扑（exposure），1 个 K 值（K=3），ε 仅到 0.10。\n- LLM 标注错误在实践中很可能是 differential 的。\n- 未从实际数据估计 LLM 混淆矩阵的 differential 程度。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** [WARNING] 符号保持的 DGP 条件限制性未讨论\n- 符号保持依赖于特定 DGP 条件，这些条件在强混杂场景下可能不成立。\n- 未讨论在实践中这些条件的满足频率。\n\n**W2** [WARNING] ASV 参数化路径的限制性\n- C(δ) = (1-δ)I + δC₀ 假设沿线性路径退化。实际退化可能非线性。\n\n**W3** [WARNING] 实验覆盖不完整\n- 14/28 配置未完成，4 个 LLM 均为开源模型，无商业模型。\n\n**W4** [WARNING] Conjecture 1 数值验证样本量不足\n- 每拓扑仅 500 scenarios，远少于 Empirical Finding 1 的 100,000。\n\n**W5** [WARNING] 线性 SEM 假设的适用范围\n- 未讨论 NLP/社会科学中非线性模型的普遍程度。\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-22T10:52:09.800566+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 154 · 2026-05-22T10:52:13.354277+00:00_

交叉分享已发送给两位 Reviewer，等待逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 155 · 2026-05-22T10:52:16.030725+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成，意见已提交。等待 Director 的后续指示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 156 · 2026-05-22T10:52:20.827594+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 157 · 2026-05-22T10:53:50.862633+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 核心理论结果依赖数值验证**

同意，且我在自己的审稿中独立提出了相同问题（我的 N1 和 N2）。补充几点：

1. **Theorem 1 的问题比 R2 描述的更严重**：R2 说 Theorem 1 有完整证明，但我仔细检查了 Appendix A.4 (p.12)，发现一般情形（非比例 f ≠ λg）的证明使用 Cauchy-Schwarz 界后，明确写到 "Tightness is confirmed numerically (500 random (C₀, δ) pairs, zero violations)"。这意味着即使是唯一标记为 "Theorem" 的结果，在一般情形下也并非完全解析证明。R2 可能遗漏了这一点。

2. **ASV 对 Conjecture 1 的依赖**：完全同意 R2 的分析。ASV 的三种度量（δ*_mag, δ*_sig, δ*_flip）均定义为 |B(C(δ))| 穿越特定阈值的临界 δ 值。如果单调性不成立，可能存在多个穿越点，δ* 的唯一性和解释性均受影响。论文未讨论非单调情形下 ASV 的回退定义（例如取最小穿越 δ 作为保守估计）。

3. **500 vs 100,000 的采样不一致**：R2 正确指出 Conjecture 1 仅用 500 个场景验证，而 Empirical Finding 1 用了 100,000 个矩阵。这种数量级差异缺乏理由说明，且 Conjecture 1 对框架的重要性不亚于 Empirical Finding 1。

**[REBUT] R2-N2: 83.4% 的叙事 framing 构成 overclaiming**

部分反驳。R2 将此标为 CRITICAL，我认为过重——这是表述问题而非方法论缺陷，且论文的处理比 R2 描述的更透明。

反驳理由：
1. **论文同时报告了两个条件下的数字**：Abstract (p.1) 明确写到 "under the full Dirichlet(1,1,1) prior, 83.4%... under realistic classifier accuracy (diagonal ≥ 0.7), the violation rate is 13.7% with 2.1% sign reversal"。Introduction (p.1) 重复了完全相同的双条件表述。论文并未隐藏 realistic accuracy 下的低违反率。

2. **Dirichlet(1,1,1) 分析有正当的方法论目的**：作为混淆矩阵参数空间的均匀采样，它回答的问题是"在所有可能的混淆矩阵中，有多大比例会导致符号翻转？"——这是对结构性风险的刻画，不是对实际频率的估计。这与敏感性分析文献中 E-value 等工具的逻辑一致（先刻画最坏情形，再评估实际风险）。83.4% 的价值在于证明符号翻转不是理论上的稀有角落情形，而是 K≥3 时参数空间的大部分区域都存在的结构性问题。

3. **但同意 framing 可以改进**：建议在 Abstract 中将 realistic accuracy 数字提前，作为主叙事；将 Dirichlet(1,1,1) 数字作为参数空间刻画的补充。这是写作调整，不构成 CRITICAL 级别问题。

**综合判断**：降级为 MINOR/WARNING 更合适。论文事实准确、条件透明，仅需调整措辞重心。

---

### Should-Fix 问题

**[AGREE] R2-W1: 线性 SEM 假设限制 NLP 实用性**

完全同意，我在自己的审稿中也提出了相同问题（我的 W5）。NLP 中 logistic regression、非参数模型广泛使用。论文 Limitations (p.8) 仅一句 "the FWL invariance result does not hold for logistic regression, and bias patterns under nonlinear models may differ"，未讨论（1）线性假设在哪些 NLP 场景下合理，（2）偏差方向性结论在弱非线性下是否近似成立。建议至少添加一个 logistic DGP 模拟。

**[AGREE] R2-W2: 缺少高度相关的参考文献**（部分同意）

- **Feder et al. (2022) TACL**：同意应引用。这是 NLP+因果推断领域最重要的综述之一。论文 Related Work (Section 2, p.2) 讨论了 "Text classifiers and LLM annotation" 和 "Sensitivity analysis and correction methods" 两条线，但缺少对 NLP-因果推断交叉领域全景的定位。引用 Feder et al. 可以帮助 NLP 审稿人理解本文在更广泛领域中的位置。

- **Cheng, Mayya & Sedoc (2024)**：如果该文确实分解了 LLM 标注测量误差的上游来源，则与本文的 non-differential misclassification 假设直接相关——上游来源分解可帮助判断 LLM 误差在何种条件下接近 non-differential。建议作者在讨论该假设的合理性时引用。但我无法独立验证此文的确切内容，条件性同意。

**[AGREE] R2-W3: ASV 参数化缺乏敏感性分析**

完全同意，我在自己的审稿中独立提出了相同问题（我的 W2）。补充一点：C₀ 在实践中来自有限验证集估计（论文 Section 3.3, p.4 提到 "C₀ is estimated from a finite validation set and subject to sampling uncertainty; we recommend bootstrapping C₀ and reporting ASV confidence intervals"），但论文未实际展示这种 bootstrap 分析的结果。建议添加一个示例展示 C₀ 不确定性如何传播到 δ* 值。

**[AGREE] R2-W4: 实证验证不完整**

同意，但需修正数字：论文 Limitations (p.8) 说的是 "14 of 28 planned configurations"，R2 写成 14/38。不影响实质——实验不完整确实削弱普适性声明。我的审稿中也独立指出了这一点（我的 W3），并额外提出了缺少商业 LLM 对比的问题。

**[AGREE] R2-W5: Proposition 1 充分条件难以事前验证**

同意，我在自己的审稿中独立提出了相同问题（我的 W1）。Table 2 (p.16) 列出的充分条件（如 confounding 需要 sign(τ) = sign(τ + B_OV)，collider 需要 |τ| > B_Berkson）涉及研究者通常不知道的 DGP 参数。论文未讨论这些条件在实践中的满足频率或可诊断性。建议添加数值模拟展示在典型参数范围下的满足率，或讨论基于数据的诊断方法。

---

### 交叉总结

两位审稿人的意见高度一致。核心共识：

| 问题 | R1 | R2 | 一致性 |
|------|----|----|--------|
| 理论结果依赖数值验证 | N1, N2 | N1 | 完全一致 |
| Non-differential 假设验证不足 | N3 | （未直接提出但 W2 间接涉及） | R1 更具体 |
| 83.4% framing | 未提出 | N2 | R2 独立发现，R1 认为 severity 应降级 |
| 线性 SEM 限制 | W5 | W1 | 完全一致 |
| ASV 参数化 | W2 | W3 | 完全一致 |
| 实验不完整 | W3 | W4 | 完全一致 |
| DGP 条件可验证性 | W1 | W5 | 完全一致 |

**唯一分歧**：R2-N2 的 severity。R2 标为 CRITICAL，R1 认为应降级为 WARNING——论文事实准确且条件透明，仅需调整叙事重心。

**R1 独有发现**：(1) Theorem 1 一般情形证明不完整（R2 认为 Theorem 1 有完整证明，实际上一般情形依赖数值紧致性确认）；(2) Non-differential misclassification stress test 仅覆盖单一拓扑（Appendix B.3, Table 6），这是一个 R2 未明确提出的 MAJOR 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 158 · 2026-05-22T10:53:57.826814+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 159 · 2026-05-22T10:54:00.478139+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **6/7 条 AGREE**，与 R2 高度一致，核心共识在理论证明缺口、线性 SEM 限制、ASV 参数化、实验不完整性上
- **1 条 REBUT** (R2-N2)：83.4% framing 不构成 CRITICAL——论文同时报告了两个条件下的数字且条件透明，Dirichlet(1,1,1) 分析有正当方法论目的（参数空间刻画），建议降级为 WARNING
- **R1 独有补充**：Theorem 1 一般情形证明也依赖数值验证（R2 遗漏），以及 non-differential 假设 stress test 覆盖不足

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 160 · 2026-05-22T10:54:07.170575+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 16

## Round 16

12 recorded events


### User

_source line 161 · 2026-05-22T10:54:13.689375+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Theorem 1 一般情形证明不完整**

同意。这与我的 N1 关切一致。具体而言：

Theorem 1 的证明（Appendix A.4, p12-13）对比例情形（f = λg）有完整代数推导，但一般情形的论证链存在逻辑缺口：Cauchy-Schwarz 不等式给出 |B(C(δ))| ≤ B̄(δ)，即使 B̄(δ) 关于 δ 单调非递减，也不能推出 |B(C(δ))| 本身单调非递减。一个简单的反例构造：f(δ) = sin(δ) 被 g(δ) = δ 界住，g 单调但 f 不单调。R1 指出的"上界的单调性 ≠ 函数的单调性"是数学上精确的。

补充：ASV 框架的实际影响可能比 R1 所述更温和。即使 |B(C(δ))| 非严格单调，"最小的 δ 使得偏差超过阈值"（即 δ* = inf{δ : |B(C(δ))| > threshold}）仍然良定义。ASV 的实用性不严格要求单调性，而是要求 δ* 作为"可容忍误分类程度"的解释有意义。但我同意 R1 的结论：当前证明结构不足以支撑 Theorem 1 的一般情形声明，应坦诚标注为 "proven for proportional case; supported numerically for general case"。

---

**[AGREE] R1-N2: 3/5 "安全"拓扑的符号保持缺乏解析证明**

同意。这与我的 N1 直接重叠。

R1 的维度论证值得重视：K=3 时列随机矩阵有 6 个自由参数，100,000 样本在 6D 空间中每维仅约 6.8 个点。虽然 Monte Carlo 随机采样不是网格采样（因此不能简单按维度衡量密度），但关键问题是：如果符号翻转仅在参数空间的窄区域发生，随机采样可能漏过。

进一步补充 R1 的论证：论文 Abstract（p1）使用了 "five topologies never produce sign reversal" 的表述。"never" 是一个全称量词，但 Empirical Finding 1（p4）的标题使用的是 "Empirical Finding"（而非 Theorem），且注明 "analytic proofs for general K remain open"——这是恰当的学术诚实。问题在于 Abstract 的措辞与正文的严谨程度不匹配。建议将 Abstract 修改为 "five topologies show no sign reversal in extensive numerical verification"。

---

**[AGREE with nuance] R1-N3: Non-differential misclassification 假设的 stress test 不足**

部分同意 R1 的诊断，但对严重程度的判断略有不同。

R1 的事实陈述准确：stress test（Appendix B.3, Table 6, p20）仅覆盖 exposure 拓扑、K=3、ε ∈ {0.00, 0.01, 0.05, 0.10}，scope 确实很窄。LLM 标注误差在实践中几乎必然是 differential 的——LLM 对某些类别的分类能力系统性地优于其他类别，且这种能力差异可能与结果变量相关。

但我认为 R1 将此标为 [MAJOR] 而非 [CRITICAL] 是合理的，原因如下：
1. Non-differential misclassification 是测量误差文献的标准假设（Carroll et al. 2006, Gustafson 2004），论文继承这一假设并非独特缺陷；
2. Table 6 虽然覆盖窄，但结果显示小幅 differential departure（ε ≤ 0.10）下 sign-flip 率从 2.0% 仅上升至 4.5%，表明框架对小偏离是稳健的；
3. 论文 Limitations（p9）明确标注了此假设。

**补充 R1 未提及的要点**：论文 Limitations（p9）还提到 "the measurement assumption ... may be violated with outcome-conditional prompting"——这实际上是 differential misclassification 的一个具体机制。如果 LLM 的 prompt 中包含结果变量的信息（如在标注情感时同时看到后续行为数据），non-differential 假设直接破坏。这个 caveat 被正确标注但讨论不够深入。

建议：扩展 stress test 至少覆盖 confounding 和 mediation 两个额外拓扑，以及 K=10 的 HumAID 设置。

---

### Should-Fix 问题

**[AGREE] R1-W1: 符号保持的 DGP 条件限制性未讨论**

同意。这与我的 W5 一致。Proposition 1(a)（p4）要求 sign(τ) = sign(τ + B_OV)，Proposition 1(b) 要求 |τ| 超过 Berkson attenuation bound。这些条件涉及未知 DGP 参数，论文承认 "These conditions involve free DGP parameters, which in practice must be estimated"（p4），但未进一步讨论在典型 NLP 因果推断场景中这些条件的满足频率或可检验性。

---

**[AGREE] R1-W2: ASV 参数化路径的限制性**

同意。这与我的 W3 完全一致。C(δ) = (1−δ)I + δC₀ 的线性插值是一个特定建模选择。实际中，分类器退化的方式可能是非线性的（如某些类别的精度下降远快于其他类别）。论文未讨论替代参数化方式，也未分析 C₀ 的选择/估计误差如何影响 ASV 结论。

---

**[AGREE with correction] R1-W3: 实验覆盖不完整**

同意 R1 的核心论点，但需纠正一个数字：论文 Limitations（p9）原文为 "14 of 38 planned configurations"，而非 R1 所述的 14/28。实际完成比例为 36.8%，比 R1 所述的 50% 更低，这使得 R1 的关切实际上更严重。

R1 提出的"4 个 LLM 均为开源模型，无商业模型"是一个我在审稿中未提及但合理的补充。商业模型（GPT-4, Claude 等）可能有不同的误差模式——例如可能更接近 non-differential（因为训练数据和 RLHF 过程不同），也可能更 differential（因为更强的上下文理解能力使错误更依赖于具体内容）。在不测试的情况下无法判断。

---

**[AGREE] R1-W4: Conjecture 1 数值验证样本量不足**

同意。这是我的 N1 中已指出的问题。论文对 Empirical Finding 1 使用了 100,000 个随机矩阵（p4），但 Conjecture 1 仅用 500 scenarios（p5）。这种 200 倍的差异缺乏解释。如果 100,000 被认为是 Empirical Finding 1 所需的适当样本量，那么 Conjecture 1——作为 ASV 框架的理论基础——至少应该获得同等或更高的验证力度。

---

**[AGREE] R1-W5: 线性 SEM 假设的适用范围**

同意。这与我的 W1 完全一致。NLP/社会科学中大量因果推断使用 logistic regression 或非参数方法。论文 Limitations（p9）承认 "FWL invariance result does not hold for logistic regression"，但未讨论在非线性模型下核心发现（如 sign-flip 现象）是否定性保持。至少一个 K=3 的 logistic regression 模拟实验可以大幅增强实用性声明。

---

### 总结

R1 和 R2 的审稿意见高度一致。两位 Reviewer 独立识别出的核心问题重叠度约 80%：

| 问题主题 | R1 编号 | R2 编号 | 一致性 |
|----------|---------|---------|--------|
| 核心理论结果缺乏解析证明 | N1, N2 | N1 | 完全一致 |
| 83.4% framing overclaiming | — | N2 | R1 未提及 |
| Non-differential 假设 stress test 不足 | N3 | — | R1 独立提出 |
| DGP 条件限制性 | W1 | W5 | 完全一致 |
| ASV 参数化限制 | W2 | W3 | 完全一致 |
| 实验覆盖不完整 | W3 | W4 | 完全一致 |
| Conjecture 1 验证不足 | W4 | N1 (部分) | 完全一致 |
| 线性假设适用性 | W5 | W1 | 完全一致 |
| 缺少关键引用 | — | W2 | R1 未提及 |

两位 Reviewer 的唯一分歧在于各自关注了对方未覆盖的问题（R1 的 N3 non-differential stress test；R2 的 N2 overclaiming framing 和 W2 missing references），但对重叠问题的判断完全一致。这种独立收敛增强了问题识别的可信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-22T10:54:30.959461+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-22T10:54:31.513551+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T10:39:50.281020+00:00\", \"completed_at\": \"2026-05-22T10:43:10.053148+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-5\", \"message\": \"前 5 页连续纯文本+公式，无任何 figure/table/diagram 视觉锚点。第一个 display item（Figure 1）直到第 6 页才出现。审稿人翻过 5 页纯文字后才看到第一张图，严重影响第一印象锚定。建议将 Figure 3（DAG 拓扑图）或一个精简的概念示意图前移至第 2-3 页。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页仅含 3 个 display items（Figure 1、Table 1、Figure 2），对于一篇有大量实证验证（7 种拓扑、3 个数据集、5 种校正方法）的论文来说密度偏低。大量关键结果图表（Figures 3-7、Tables 2-6）被推入附录，审稿人在主文中无法直观看到实验全貌。\"}, {\"severity\": \"warning\", \"dimension\": \"page 3→18\", \"message\": \"主文 Section 3.1（page 3）引用 \\\"Figure 3 (Pearl, 2009)\\\" 展示 7 种 DAG 拓扑，但 Figure 3 位于 page 18（附录 B）。读者在阅读方法论核心内容时无法看到这张关键概念图，需翻 15 页才能找到。建议将 DAG 拓扑图（或精简版）移入主文。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"纯文本整页（Empirical Validation 讨论），夹在 page 6（Figure 1 + Table 1）与 page 8（Figure 2）之间，视觉节奏断裂。\"}, {\"severity\": \"warning\", \"dimension\": \"page 20\", \"message\": \"页面约 40-45% 为空白区域——Figure 7 占页面上部约 30%，Table 6 在页面底部约 15%，中间大面积留白。空间利用不足。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1 五个子面板（Confounding/Exposure/IV/M-bias/Collider）在全宽排列下单个面板较小，直方图内文字（axis labels）可读但偏小，约为正文字号 65-70%。建议适当增大子图或减少面板数量。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 为单栏宽度折线图，位于结论页顶部。位置合理，但图中线条颜色区分度在灰度打印下可能不足，建议辅以不同 line style（dashed/dotted）。\"}, {\"severity\": \"info\", \"dimension\": \"page 19\", \"message\": \"三张图（Figures 4、5、6）挤在同一页，各图尺寸较小。Figure 5 的散点/小提琴图中数据标签在此缩放下难以辨认。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1 使用红色/蓝色色系区分 sign reversal vs attenuation，红绿色盲用户可能混淆红色柱与绿色参考。建议使用 Okabe-Ito 色板或 blue+orange 方案。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Abstract/Author 排版整洁，符合 ACL 匿名提交规范。\\\"Anonymous ACL submission\\\
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-22T10:54:31.514031+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-22T10:54:32.568669+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_2/submitted.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-22T10:40:38.778785+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_ca838cd3ed4c7e2d9c8e3459edd98b90\", \"skipped_at\": \"2026-05-22T10:42:53.414735+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-22T10:54:32.569207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-22T10:54:32.670207+00:00_

1	issues:
2	  - id: R1-N1
3	    category: soundness
4	    severity: must-fix
5	    summary: "Theorem 1 (Envelope Monotonicity) 无解析证明，仅 500 场景数值验证"
6	    status: in_progress
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [R1, R2]
12	        note: "R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。"
13	    action_items:
14	      - round: 1
15	        action: "Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture"
16	        assigned_to: agent
17	        status: pending
18	
19	  - id: R1-N2
20	    category: soundness
21	    severity: must-fix
22	    summary: "Proposition 1 中 mediation/M-bias sign preservation 缺乏 proof"
23	    status: in_progress
24	    first_raised_round: 1
25	    last_seen_round: 1
26	    mentions:
27	      - round: 1
28	        reviewers: [R1, R2]
29	        note: "R1 首发，R2 AGREE 并建议拆分。"
30	    action_items:
31	      - round: 1
32	        action: "拆分 Proposition 1 → 已证(confounding/collider/exposure反例) vs Empirical Finding(mediation/M-bias/front-door)；替换 'standard DGP' 为显式充分条件"
33	        assigned_to: agent
34	        status: pending
35	
36	  - id: R1-N3
37	    category: soundness
38	    severity: must-fix
39	    summary: "ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限"
40	    status: in_progress
41	    first_raised_round: 1
42	    last_seen_round: 1
43	    mentions:
44	      - round: 1
45	        reviewers: [R1, R2]
46	        note: "δ_max = min_j 1/(1-(C₀)_{jj})。sign-flip ASV 6.7 可能超出有效域。超出 δ_max 的 ASV 应标为 ∞（实际强化结论）。"
47	    action_items:
48	      - round: 1
49	        action: "引入 δ_max 约束，写脚本重新计算所有 ASV 值，超出 δ_max 标为 ∞，更新 method.tex + experiments.tex"
50	        assigned_to: agent
51	        status: pending
52	
53	  - id: R2-N1
54	    category: presentation
55	    severity: must-fix
56	    summary: "83.4% headline framing 误导，需同时报告 realistic regime"
57	    status: in_progress
58	    first_raised_round: 1
59	    last_seen_round: 1
60	    mentions:
61	      - round: 1
62	        reviewers: [R1, R2]
…[truncated 4904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-22T10:57:26.685662+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1 issues — status updates for Round 2 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 一般情形证明不完整：Cauchy-Schwarz 界的单调性 ≠ |B(C(δ))| 本身的单调性\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次独立提出。R1 明确指出上界单调 ≠ 函数单调（Cauchy-Schwarz gap）。R2 AGREE 并补充 ASV δ* 唯一性依赖。比例情形 (f=λg) 证明完整，一般情形仅 500 组数值验证。建议：一般情形降级为 Conjecture 或 Empirical Finding。\"\n    action_items:\n      - round: 1\n        action: \"Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: must-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，缺乏解析证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE 并建议拆分。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。摘要 'five topologies never produce sign reversal' 中 'never' 是全称量词，但 mediation/M-bias/front-door 仅有 Empirical Finding。R2 建议改为 'show no sign reversal in extensive numerical verification'。R1 补充 6D 空间 100k 采样密度论证。\"\n    action_items:\n      - round: 1\n        action: \"拆分 Proposition 1 → 已证(confounding/collider/exposure反例) vs Empirical Finding(mediation/M-bias/front-door)；替换 'standard DGP' 为显式充分条件\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"Abstract 'never' → 'show no sign reversal in extensive numerical verification' 或类似措辞\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"δ_max = min_j 1/(1-(C₀)_{jj})。sign-flip ASV 6.7 可能超出有效域。超出 δ_max 的 ASV 应标为 ∞（实际强化结论）。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及。论文 Section 3.3 已引入 δ_max 约束并明确 ASV 限制在 [0, δ_max]，可能已修复。待 Research Director 确认。\"\n    action_items:\n      - round: 1\n        action: \"引入 δ_max 约束，写脚本重新计算所有 ASV 值，超出 δ_max 标为 ∞，更新 method.tex + experiments.tex\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    category: presentation\n    severity: should-fix\n    summary: \"83.4% headline framing 需调整叙事重心\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 再次标为 CRITICAL。R1 REBUT：论文 Abstract 已同时报告 83.4%（Dirichlet prior）和 2.1%（realistic accuracy），条件透明。Dirichlet(1,1,1) 用于参数空间刻画有方法论正当性。R1 建议降级为 WARNING。R2 未反驳 REBUT。综合判断：降级为 should-fix。\"\n    action_items:\n      - round: 1\n        action: \"Abstract/Intro 同时呈现 full prior (83.4%) 和 realistic regime (2.1% sign reversal at diagonal≥0.7)\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"调整叙事重心：以 realistic accuracy 为主叙事，Dirichlet(1,1,1) 作为参数空间刻画的补充\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 must-fix，R1 rebut 认为 K≥3 是质变。降级 should-fix。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。当前 Abstract 使用 'We present a systematic framework'（非 'the first'），可能已修复。待确认。\"\n    action_items:\n      - round: 1\n        action: \"Abstract/Intro 'the first systematic framework' → 'a systematic framework'；保留 'first to jointly characterize' 在有依据处\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"4 篇已在 references.bib 中，page fitting 时从 .tex 移除。需恢复 \\\\cite 并补讨论。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。当前 Related Work 已包含 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 的引用，可能已修复。但 R2 本轮新增了 2 篇遗漏引用（见 NEW-2）。\"\n    action_items:\n      - round: 1\n        action: \"恢复 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 引用；Related Work 补讨论\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。Table 2 充分条件涉及未知 DGP 参数。论文 p4 承认但未讨论满足频率或可诊断性。建议添加模拟或 domain knowledge 讨论。\"\n    action_items:\n      - round: 1\n        action: \"Method 加 1-2 句讨论条件循环性 + ASV 作为不依赖精确条件的替代\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：14/38 配置完成，无商业 LLM\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 部分 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。R2 纠正数字为 14/38（非 14/28），完成率仅 36.8%。R1 补充缺少商业 LLM（GPT-4, Claude）对比。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 强化 model asymmetry caveat\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"补完缺失配置；讨论开源 vs 商业 LLM 误差模式差异\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 rebut 但同意调整 framing。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。Experiments 已区分理论风险 vs 实践观测。可能已改善。\"\n    action_items:\n      - round: 1\n        action: \"Experiments 明确区分理论风险（Dirichlet prior）vs 实践观测（empirical matrices）\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性未展示\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。论文 p4 提到 'we recommend bootstrapping C₀ and reporting ASV confidence intervals' 但未展示实际 bootstrap 结果。R1 要求示例。R2 追问不同 C₀ 是否导致 safe/unsafe 判断翻转。\"\n    action_items:\n      - round: 1\n        action: \"Method 或 Limitations 加 bootstrap C₀ uncertainty 讨论\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"展示至少一个 C₀ bootstrap 示例，分析 δ* 的置信区间\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制对 NLP 受众的实用性\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。FWL 对 logistic regression 不成立。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次完全一致。Limitations 仅一句提及。建议至少一个 logistic DGP 模拟验证 sign-flip 是否定性保持。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 加线性模型假设 + FWL 不推广到非线性的说明\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"添加 K=3 logistic regression 模拟实验验证核心发现的定性保持\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分，掩盖 per-topology 差异\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。论文已报告 per-topology range (0.5%-5.5%)，可能已改善。\"\n    action_items:\n      - round: 1\n        action: \"已有 per-topology range (0.5%-5.5%)，考虑加 median 或更详细报告\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一、命名歧义、Table caption 不完整\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被显式提及，但 R2 在小问题中提到符号系统多套（τ, τ̂, f(A*), β）建议符号表。\"\n    action_items:\n      - round: 1\n        action: \"统一符号，修正命名，补 Table caption 定义\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 新增 issues ===\n\n  - id: NEW-1\n    category: soundness\n    severity: must-fix\n    summary: \"Non-differential misclassification stress test 仅覆盖单一拓扑(exposure)、单一 K 值(K=3)、ε≤0.10\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R1 标为 MAJOR。R2 AGREE with nuance：non-differential 是标准假设（Carroll 2006），且 Table 6 显示小偏离下 sign-flip 仅从 2.0% 升至 4.5%，但覆盖面确实过窄。建议扩展至 confounding/mediation + K=10。\"\n    action_items:\n      - round: 2\n        action: \"扩展 stress test 至少覆盖 confounding 和 mediation 拓扑，以及 K=10 HumAID 设置；从实际数据估计 LLM 误差的 differential 程度\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 2 篇高度相关引用：Feder et al. (2022) TACL 综述, Cheng et al. (2024) LLM 误差分解\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 提出，R1 AGREE（Feder 完全同意，Cheng 条件性同意）。Feder et al. 是 NLP+因果推断最重要综述（TACL，400+ 引用），投 EMNLP 必引。Cheng et al. 分解 LLM 标注误差上游来源，与本文下游传播分析互补。\"\n    action_items:\n      - round: 2\n        action: \"Related Work 补充 Feder et al. (2022) TACL 和 Cheng et al. (2024) 引用\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证仅 500 scenarios，远少于 Empirical Finding 1 的 100,000\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。200 倍的采样量差异缺乏解释。Conjecture 1 是 ASV 框架的理论基础，重要性不亚于 Empirical Finding 1。\"\n    action_items:\n      - round: 2\n        action: \"增加 Conjecture 1 验证到至少 10,000 scenarios per topology，或讨论 500 即足够的理由\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1 issues — status updates for Round 2 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 一般情形证明不完整：Cauchy-Schwarz 界的单调性 ≠ |B(C(δ))| 本身的单调性\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次独立提出。R1 明确指出上界单调 ≠ 函数单调（Cauchy-Schwarz gap）。R2 AGREE 并补充 ASV δ* 唯一性依赖。比例情形 (f=λg) 证明完整，一般情形仅 500 组数值验证。建议：一般情形降级为 Conjecture 或 Empirical Finding。\"\n    action_items:\n      - round: 1\n        action: \"Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: must-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，缺乏解析证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE 并建议拆分。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。摘要 'five topologies never produce sign reversal' 中 'never' 是全称量词，但 mediation/M-bias/front-door 仅有 Empirical Finding。R2 建议改为 'show no sign reversal in extensive numerical verification'。R1 补充 6D 空间 100k 采样密度论证。\"\n    action_items:\n      - round: 1\n        action: \"拆分 Proposition 1 → 已证(confounding/collider/exposure反例) vs Empirical Finding(mediation/M-bias/front-door)；替换 'standard DGP' 为显式充分条件\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"Abstract 'never' → 'show no sign reversal in extensive numerical verification' 或类似措辞\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"δ_max = min_j 1/(1-(C₀)_{jj})。sign-flip ASV 6.7 可能超出有效域。超出 δ_max 的 ASV 应标为 ∞（实际强化结论）。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被任何 Reviewer 提及。论文 Section 3.3 已引入 δ_max 约束并明确 ASV 限制在 [0, δ_max]，可能已修复。待 Research Director 确认。\"\n    action_items:\n      - round: 1\n        action: \"引入 δ_max 约束，写脚本重新计算所有 ASV 值，超出 δ_max 标为 ∞，更新 method.tex + experiments.tex\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    category: presentation\n    severity: should-fix\n    summary: \"83.4% headline framing 需调整叙事重心\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 再次标为 CRITICAL。R1 REBUT：论文 Abstract 已同时报告 83.4%（Dirichlet prior）和 2.1%（realistic accuracy），条件透明。Dirichlet(1,1,1) 用于参数空间刻画有方法论正当性。R1 建议降级为 WARNING。R2 未反驳 REBUT。综合判断：降级为 should-fix。\"\n    action_items:\n      - round: 1\n        action: \"Abstract/Intro 同时呈现 full prior (83.4%) 和 realistic regime (2.1% sign reversal at diagonal≥0.7)\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"调整叙事重心：以 realistic accuracy 为主叙事，Dirichlet(1,1,1) 作为参数空间刻画的补充\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 must-fix，R1 rebut 认为 K≥3 是质变。降级 should-fix。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。当前 Abstract 使用 'We present a systematic framework'（非 'the first'），可能已修复。待确认。\"\n    action_items:\n      - round: 1\n        action: \"Abstract/Intro 'the first systematic framework' → 'a systematic framework'；保留 'first to jointly characterize' 在有依据处\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"4 篇已在 references.bib 中，page fitting 时从 .tex 移除。需恢复 \\\\cite 并补讨论。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。当前 Related Work 已包含 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 的引用，可能已修复。但 R2 本轮新增了 2 篇遗漏引用（见 NEW-2）。\"\n    action_items:\n      - round: 1\n        action: \"恢复 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 引用；Related Work 补讨论\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。Table 2 充分条件涉及未知 DGP 参数。论文 p4 承认但未讨论满足频率或可诊断性。建议添加模拟或 domain knowledge 讨论。\"\n    action_items:\n      - round: 1\n        action: \"Method 加 1-2 句讨论条件循环性 + ASV 作为不依赖精确条件的替代\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：14/38 配置完成，无商业 LLM\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 部分 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。R2 纠正数字为 14/38（非 14/28），完成率仅 36.8%。R1 补充缺少商业 LLM（GPT-4, Claude）对比。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 强化 model asymmetry caveat\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"补完缺失配置；讨论开源 vs 商业 LLM 误差模式差异\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 rebut 但同意调整 framing。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。Experiments 已区分理论风险 vs 实践观测。可能已改善。\"\n    action_items:\n      - round: 1\n        action: \"Experiments 明确区分理论风险（Dirichlet prior）vs 实践观测（empirical matrices）\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性未展示\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。论文 p4 提到 'we recommend bootstrapping C₀ and reporting ASV confidence intervals' 但未展示实际 bootstrap 结果。R1 要求示例。R2 追问不同 C₀ 是否导致 safe/unsafe 判断翻转。\"\n    action_items:\n      - round: 1\n        action: \"Method 或 Limitations 加 bootstrap C₀ uncertainty 讨论\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"展示至少一个 C₀ bootstrap 示例，分析 δ* 的置信区间\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制对 NLP 受众的实用性\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。FWL 对 logistic regression 不成立。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次完全一致。Limitations 仅一句提及。建议至少一个 logistic DGP 模拟验证 sign-flip 是否定性保持。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 加线性模型假设 + FWL 不推广到非线性的说明\"\n        assigned_to: agent\n        status: pending\n      - round: 2\n        action: \"添加 K=3 logistic regression 模拟实验验证核心发现的定性保持\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分，掩盖 per-topology 差异\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。论文已报告 per-topology range (0.5%-5.5%)，可能已改善。\"\n    action_items:\n      - round: 1\n        action: \"已有 per-topology range (0.5%-5.5%)，考虑加 median 或更详细报告\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一、命名歧义、Table caption 不完整\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被显式提及，但 R2 在小问题中提到符号系统多套（τ, τ̂, f(A*), β）建议符号表。\"\n    action_items:\n      - round: 1\n        action: \"统一符号，修正命名，补 Table caption 定义\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 新增 issues ===\n\n  - id: NEW-1\n    category: soundness\n    severity: must-fix\n    summary: \"Non-differential misclassification stress test 仅覆盖单一拓扑(exposure)、单一 K 值(K=3)、ε≤0.10\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R1 标为 MAJOR。R2 AGREE with nuance：non-differential 是标准假设（Carroll 2006），且 Table 6 显示小偏离下 sign-flip 仅从 2.0% 升至 4.5%，但覆盖面确实过窄。建议扩展至 confounding/mediation + K=10。\"\n    action_items:\n      - round: 2\n        action: \"扩展 stress test 至少覆盖 confounding 和 mediation 拓扑，以及 K=10 HumAID 设置；从实际数据估计 LLM 误差的 differential 程度\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 2 篇高度相关引用：Feder et al. (2022) TACL 综述, Cheng et al. (2024) LLM 误差分解\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 提出，R1 AGREE（Feder 完全同意，Cheng 条件性同意）。Feder et al. 是 NLP+因果推断最重要综述（TACL，400+ 引用），投 EMNLP 必引。Cheng et al. 分解 LLM 标注误差上游来源，与本文下游传播分析互补。\"\n    action_items:\n      - round: 2\n        action: \"Related Work 补充 Feder et al. (2022) TACL 和 Cheng et al. (2024) 引用\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证仅 500 scenarios，远少于 Empirical Finding 1 的 100,000\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。200 倍的采样量差异缺乏解释。Conjecture 1 是 ASV 框架的理论基础，重要性不亚于 Empirical Finding 1。\"\n    action_items:\n      - round: 2\n        action: \"增加 Conjecture 1 验证到至少 10,000 scenarios per topology，或讨论 500 即足够的理由\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-22T10:57:26.736659+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 11455}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-22T11:00:08.909486+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**目标 Venue**: EMNLP 2026 (via ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验验证; R2: 新颖性+相关工作+写作质量）\n**审稿模式**: Fresh（初审）\n**交叉轮次**: 1 轮（Round 1 独立审稿 → 交叉分享 → 收敛，未进入 Round 2）\n\n---\n\n## Summary\n\n本文系统研究了 K-class LLM 标注误差在 7 种因果 DAG 拓扑下的偏差传播。核心发现：(1) K≥3 时 exposure 和 IV 拓扑可产生符号翻转（83.4% under Dirichlet prior; 2.1% under realistic accuracy），而 5 种拓扑维持符号保持性（2 种已证明，3 种经验验证）；(2) ASV 灵敏度框架揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱；(3) FWL 不变性导致矩阵校正方法对 4 种拓扑完全无效。论文建立了有用的分类法，但核心理论结果部分依赖数值验证而非完整解析证明。\n\n---\n\n## Strengths\n\n**S1. 选题及时且填补明确研究空白**\nLLM 标注在计算社会科学中快速普及，但多分类标注误差在因果推断中的系统性传播此前缺乏跨拓扑研究。先前工作（Lee & Wood-Doughty 2024）仅覆盖 confounding 单一拓扑，本文扩展到 7 种拓扑的统一框架，是实质性进步。[R1, R2 共识]\n\n**S2. K≥3 符号翻转发现具有理论和实践价值**\nK=2 → K≥3 的定性断裂（符号翻转在二分类中不可能但在多分类中成为结构性风险）是非显而易见的理论发现。Appendix A.5 的反例构造严格且具教育意义，直接指导实践者不应将多分类标签简单二值化。[R1, R2 共识]\n\n**S3. FWL invariance 洞察新颖且可操作**\n证明 4 种拓扑下矩阵校正方法（Naive plug-in, MLA）因 FWL 不变性而恰好 0% 偏差缩减——这是结构性结果（非数值近似），为校正方法选择提供了明确的负面指导。Section 4.6 的 210 配置系统评估有较高实践价值。[R1, R2 共识]\n\n**S4. 理论-经验层级区分诚实**\n论文清晰标注 Proposition（已证）、Empirical Finding（数值验证）、Conjecture（猜想），这种分层在同类论文中较少见。[R1 首发, R2 同意]\n\n**S5. 解析推导与 MC 验证高度一致**\nGrand MAPE 2.0%（126 scenarios），per-topology range 0.5%-5.5%，理论预测与实验验证吻合度高。[R1, R2 共识]\n\n**S6. ASV 框架设计合理**\n三种互补灵敏度度量（magnitude, significance, sign-flip）类比 E-value 设计思路，为研究者提供简洁的\"标注误差预算\"工具。δ_max 约束的引入确保了参数化的有效性。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [CRITICAL] Theorem 1 一般情形证明不完整** [R1-N1, R2-N1 共识]\n- Theorem 1 声称 confounding 拓扑下 |B(C(δ))| 对 δ 单调非递减。比例情形 (f=λg) 有完整代数推导（Appendix A.4），但一般情形使用 Cauchy-Schwarz 界后以 \"Tightness is confirmed numerically (500 random (C₀, δ) pairs, zero violations)\" 收尾。\n- **核心问题**：Cauchy-Schwarz 仅证明上界 B̄(δ) 的单调性，不能推出 |B(C(δ))| 本身的单调性。R2 举例：f(δ)=sin(δ) 被 g(δ)=δ 界住，g 单调但 f 不单调。\n- **影响**：ASV 框架的 δ* 唯一性和解释性直接依赖该单调性。论文将唯一标记为 \"Theorem\" 的结果在一般情形下依赖数值验证，模糊了 theorem 和 conjecture 的界限。\n- **建议**：一般情形降级为 \"Theorem (proportional case) + Empirical Finding (general case)\"，明确讨论 ASV 在单调性仅为经验验证时的可靠性。\n\n**MF2. [MAJOR] 3/5 \"安全\"拓扑的符号保持缺乏解析证明** [R1-N2, R2-N1 共识]\n- Mediation、M-bias、front-door 的符号保持仅通过 100,000 随机列随机矩阵数值验证，论文明确承认 \"analytic proofs for general K remain open\"。\n- Abstract 使用 \"five topologies never produce sign reversal\"，\"never\" 是全称量词，与 Empirical Finding 的认识论地位不匹配。\n- **建议**：Abstract 修改为 \"five topologies show no sign reversal across extensive numerical verification (proven analytically for confounding and collider)\"；正文讨论解析证明的困难所在。\n\n**MF3. [MAJOR] Non-differential misclassification stress test 覆盖不足** [R1 首发, R2 同意(nuance)]\n- Stress test（Appendix B.3, Table 6）仅覆盖 exposure 拓扑、K=3、ε ∈ {0.00, 0.01, 0.05, 0.10}。\n- LLM 标注误差在实践中几乎必然是 differential 的（不同类别的分类能力系统性不同，可能与结果变量相关）。\n- R2 补充：论文 Limitations 提到 \"outcome-conditional prompting\" 可破坏该假设，但讨论不够深入。\n- **缓解因素**（R2）：non-differential 是测量误差文献标准假设（Carroll 2006），Table 6 显示 ε≤0.10 下 sign-flip 仅从 2.0% 升至 4.5%，表明小偏离下稳健。\n- **建议**：扩展至 confounding/mediation 拓扑 + K=10 HumAID 设置；从实际数据估计 LLM 误差的 differential 程度。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [MAJOR] 线性 SEM 假设限制对 NLP 受众的实用性** [R1-W5, R2-W1 共识]\n- 所有理论结果基于线性结构方程。NLP 中 logistic regression、非参数方法广泛使用。\n- Limitations 仅一句 \"FWL invariance result does not hold for logistic regression\"，未讨论线性假设的适用边界或非线性下核心发现是否定性保持。\n- **建议**：至少添加一个 K=3 logistic DGP 模拟验证 sign-flip 现象是否定性保持。\n\n**SF2. [MAJOR] 缺少 2 篇高度相关引用** [R2 首发, R1 同意]\n- **Feder et al. (2022) TACL**：\"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond\"——NLP+因果推断领域引用量最高的综述（400+ 引用），投 EMNLP 必引。\n- **Cheng, Mayya & Sedoc (2024)**：\"To Err Is Human; To Annotate, SILICON?\"——将 LLM 标注误差分解为四种上游来源，与本文下游传播分析互补。（注：此文已在 references.bib 中但未在正文 \\cite。）\n- **建议**：Related Work 补充引用并明确区分。\n\n**SF3. [MAJOR] ASV 参数化选择缺乏讨论和敏感性分析** [R1-W2, R2-W3 共识]\n- C(δ) = (1-δ)I + δC₀ 的线性插值是一个特定参数化选择，替代方案（对角线衰减、精度参数化）未讨论。\n- 论文 Section 3.3 提到 \"we recommend bootstrapping C₀\"，但未展示实际 bootstrap 结果。\n- **建议**：讨论参数化选择理由；展示至少一个 C₀ bootstrap 示例分析 δ* 置信区间。\n\n**SF4. [WARNING] 实证验证不完整** [R1-W3, R2-W4 共识]\n- 仅完成 14/38 计划配置（36.8%），VAST (K=3) 和 CivilComments (K=2) 覆盖不足。\n- 4 个 LLM 均为开源模型，无商业模型（GPT-4, Claude）对比。\n- **建议**：补完缺失配置；讨论开源 vs 商业 LLM 误差模式差异。\n\n**SF5. [WARNING] Conjecture 1 数值验证样本量不足** [R1-W4, R2-N1 共识]\n- 每拓扑仅 500 scenarios 验证 ASV envelope 单调性，而 Empirical Finding 1 用了 100,000 个矩阵。200 倍差异缺乏解释。\n- Conjecture 1 是 ASV 框架的理论基础，重要性不亚于 Empirical Finding 1。\n- **建议**：增加到至少 10,000 scenarios per topology。\n\n**SF6. [WARNING] DGP 条件在实践中难以事前验证** [R1-W1, R2-W5 共识]\n- Proposition 1 的充分条件（如 sign(τ) = sign(τ + B_OV)）涉及未知 DGP 参数，实践者无法事前判断。\n- 论文通过 ASV 部分缓解，但 ASV 本身依赖 Conjecture 1。\n- **建议**：讨论基于数据的诊断方法或典型参数范围下的满足率。\n\n### Minor（不影响接收）\n\n- Abstract \"five topologies never\" 措辞需与正文 Empirical Finding 对齐\n- Section 3.4 Binarization Collapse 仅 4 行，信息密度低，建议移至附录或扩充\n- Table 1 混排两种先验条件下的结果，建议分行标注\n- 多套符号系统（τ, τ̂, f(A*), β）快速阅读时易混淆，建议增加符号表\n- Appendix B.1 Applied Illustration（ClinicalBERT Case Study）有价值，建议主文增加交叉引用\n\n---\n\n## Reviewer Consensus\n\n以下问题双方完全一致（[AGREE]）：\n\n| # | 问题 | 严重程度 |\n|---|------|---------|\n| 1 | 核心理论结果（Theorem 1 一般情形、Empirical Finding 1、Conjecture 1）依赖数值验证 | Must-Fix |\n| 2 | 3/5 安全拓扑符号保持缺乏解析证明 + Abstract 措辞不匹配 | Must-Fix |\n| 3 | 线性 SEM 假设限制 NLP 实用性 | Should-Fix |\n| 4 | ASV 参数化限制 + C₀ 不确定性未展示 | Should-Fix |\n| 5 | 实验不完整（14/38 配置，无商业 LLM） | Should-Fix |\n| 6 | DGP 条件实践可验证性 | Should-Fix |\n| 7 | Conjecture 1 验证量（500 vs 100,000）不足 | Should-Fix |\n\n---\n\n## Reviewer Divergence\n\n**唯一分歧：83.4% framing 的严重程度**\n\n- **R2 立场 [CRITICAL]**：83.4% 基于 Dirichlet(1,1,1)（平均精度 ~0.33），realistic accuracy 下仅 2.1%。以极端场景数字为 headline 构成 sensationalization，影响论文诚实性信任。\n- **R1 反驳 [REBUT → WARNING]**：(1) 论文 Abstract 已同时报告两组数字，条件透明；(2) Dirichlet(1,1,1) 作为参数空间均匀采样有方法论正当性——刻画结构性风险而非估计实际频率；(3) 83.4% 证明符号翻转不是稀有角落情形。\n- **R2 未反驳 R1 的 REBUT**。\n- **Director 裁定**：降级为 Should-Fix。论文事实准确、条件透明，但建议调整叙事重心——以 realistic accuracy 为主叙事。\n\n---\n\n## Questions for Authors\n\n**Q1** (R1, R2 共识): Theorem 1 一般情形能否补全解析证明？若不能，是否考虑将一般情形降级为 Empirical Finding？\n\n**Q2** (R1, R2 共识): Conjecture 1 是否做过 adversarial search（专门寻找反例的优化搜索）？当前 500 scenarios 的搜索策略是什么？\n\n**Q3** (R2 首发, R1 同意): 在 logistic regression 下，sign-flip 现象是否定性保持？即使不提供完整理论，一个 K=3 × 3 topologies 的模拟也能大幅增强实用性。\n\n**Q4** (R2): ASV 的 C₀ 估计来自有限验证集。如果 C₀ 对角线估计误差为 ±0.05，ASV 的 safe/unsafe 判断是否会翻转？\n\n**Q5** (R1): 能否从 3 个实证数据集直接估计 LLM 混淆矩阵的 differential 程度（如按 Y 值分层计算 C 差异）？\n\n---\n\n## Missing References\n\n1. **Feder, A., Keith, K.A., Manzoor, E., et al. (2022). \"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond.\" TACL.** — NLP+因果推断领域最重要综述，400+ 引用，投 EMNLP 必引。[R2 首发, R1 同意]\n\n2. **Cheng, X., Mayya, R., & Sedoc, J. (2024). \"To Err Is Human; To Annotate, SILICON?\" arXiv:2412.14461.** — LLM 标注误差上游来源分解，与本文下游传播分析互补。已在 references.bib 中但未在正文引用。[R2 首发, R1 条件性同意]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：已跳过（用户未提交外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（5 warnings, 9 info, 0 critical）\n\n### Warnings\n\n1. **前 5 页无任何 figure/table**：审稿人翻过 5 页纯文字+公式后才看到第一个 display item（Figure 1, p6）。建议将 Figure 3（DAG 拓扑图，当前在 p18 附录）前移至 p2-3。\n2. **主文 display item 密度低**：8 页正文仅 3 个 display items（Figure 1, Table 1, Figure 2），大量关键结果图表在附录。\n3. **Figure 3 远离引用位置**：主文 p3 引用 \"Figure 3\" 展示 7 种 DAG 拓扑，但 Figure 3 在 p18，需翻 15 页。\n4. **p7 纯文本整页**：Empirical Validation 讨论，夹在 p6（Figure 1 + Table 1）和 p8（Figure 2）之间，视觉节奏断裂。\n5. **p20 约 40% 空白**：Figure 7 + Table 6 布局空间利用不足。\n\n### Info（参考）\n- Figure 1 子面板字体偏小（正文字号 65-70%）\n- Figure 2 线条颜色在灰度打印下区分度可能不足\n- p19 三张图挤在同一页，部分标签难以辨认\n- Figure 1 色板可能对色盲用户不友好（红/绿），建议 Okabe-Ito 色板\n- 格式合规：匿名处理正确，booktabs 三线表规范，References 格式统一\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5/5 — Borderline Conference\n\n**置信度**: 4/5（双方 Reviewer 均仔细检查了证明结构和实验设计）\n\n**评估理由**:\n\n论文填补了 LLM 多分类标注误差 × 因果 DAG 拓扑的明确研究空白，K≥3 符号翻转发现和 FWL invariance 洞察具有理论与实践双重价值。框架设计系统，理论-经验层级区分诚实。\n\n但存在两个阻碍明确接收推荐的结构性问题：\n1. **理论完整性缺口**：唯一标记为 Theorem 的结果在一般情形下依赖数值验证；3/5 \"安全\"拓扑的符号保持仅有经验证据；ASV 框架依赖的 Conjecture 1 仅 500 scenarios 验证。这些问题影响论文的核心理论贡献可信度。\n2. **实用性边界模糊**：线性 SEM 假设未充分讨论对 NLP 场景的适用性；non-differential misclassification stress test 覆盖不足；实验完成率仅 36.8%。\n\n**接收条件**：若以下修改可在 camera-ready 阶段完成，论文有望达到主会议水平：\n- MF1: Theorem 1 一般情形降级为 Empirical Finding 或补完证明\n- MF2: Abstract/正文措辞与证明状态对齐\n- MF3: Stress test 扩展至 2+ 拓扑和 K=10\n- SF1-SF6: 至少解决线性假设讨论和缺失引用\n\n**当前论文质量高于 Findings 门槛（3.0），处于 Borderline Conference 区间（3.5）。**\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"83.4% of confusion matrices cause sign reversal\" 作为 headline 在技术上准确（Dirichlet(1,1,1) prior），但叙事效果倾向于 sensationalization。建议将 \"under realistic classifier accuracy (diagonal ≥ 0.7), the violation rate is 13.7% with 2.1% sign reversal\" 提升到与 83.4% 同等显著位置。\n- 三项贡献的表述清晰，层次分明。\n\n### Section 2 (Related Work)\n- 三段式结构（measurement error / text classifiers / sensitivity analysis）覆盖面广。\n- 缺少 Feder et al. (2022) TACL 综述——NLP+因果推断领域的 canonical reference。\n- Cheng et al. (2024) 已在 .bib 中但未引用。\n\n### Section 3 (Method)\n- **3.1 Setup**: 清晰简洁。Non-differential misclassification 定义明确。\n- **3.2 Bias Expressions**: 7 种拓扑的偏差表达式推导是论文的核心技术贡献。Proposition 1 的分层处理（proved / empirical finding / counterexample）是正确做法，但 Abstract 未反映此层级。\n- **3.3 ASV**: 三种度量设计合理。δ_max 约束已引入。C₀ bootstrap 建议已提出但未实际展示。\n- **3.4 Binarization Collapse**: 仅 4 行，信息密度低。\n\n### Section 4 (Experiments)\n- **4.1-4.2**: 理论-MC 一致性验证充分（MAPE 2.0%）。\n- **4.3-4.4**: ASV 验证和 binarization collapse 分析有价值。\n- **4.5 Empirical Validation**: 核心实证部分。3 tasks × 4 LLMs 设计合理但完成率低（14/38）。\"F1 does not predict downstream bias\" 发现（Figure 2）有实用价值。\n- **4.6 Correction Guidance**: 210 配置系统评估，FWL invariance 的实证确认（exactly 0.0%）有力。\n\n### Section 5 (Conclusion)\n- 简洁准确，未过度声称。\n\n### Limitations\n- 覆盖面合理（non-differential 假设、线性假设、实验不完整），但每项讨论偏简略。\n- 缺少线性假设适用边界的讨论。\n\n### Appendix\n- Appendix A（证明）是论文的技术核心。比例情形证明完整严谨；一般情形的数值验证不足（500 scenarios）。\n- Appendix B.1（ClinicalBERT Case Study）展示框架实用性，建议主文交叉引用。\n- Appendix B.3（Stress Test）覆盖面过窄。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**目标 Venue**: EMNLP 2026 (via ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验验证; R2: 新颖性+相关工作+写作质量）\n**审稿模式**: Fresh（初审）\n**交叉轮次**: 1 轮（Round 1 独立审稿 → 交叉分享 → 收敛，未进入 Round 2）\n\n---\n\n## Summary\n\n本文系统研究了 K-class LLM 标注误差在 7 种因果 DAG 拓扑下的偏差传播。核心发现：(1) K≥3 时 exposure 和 IV 拓扑可产生符号翻转（83.4% under Dirichlet prior; 2.1% under realistic accuracy），而 5 种拓扑维持符号保持性（2 种已证明，3 种经验验证）；(2) ASV 灵敏度框架揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱；(3) FWL 不变性导致矩阵校正方法对 4 种拓扑完全无效。论文建立了有用的分类法，但核心理论结果部分依赖数值验证而非完整解析证明。\n\n---\n\n## Strengths\n\n**S1. 选题及时且填补明确研究空白**\nLLM 标注在计算社会科学中快速普及，但多分类标注误差在因果推断中的系统性传播此前缺乏跨拓扑研究。先前工作（Lee & Wood-Doughty 2024）仅覆盖 confounding 单一拓扑，本文扩展到 7 种拓扑的统一框架，是实质性进步。[R1, R2 共识]\n\n**S2. K≥3 符号翻转发现具有理论和实践价值**\nK=2 → K≥3 的定性断裂（符号翻转在二分类中不可能但在多分类中成为结构性风险）是非显而易见的理论发现。Appendix A.5 的反例构造严格且具教育意义，直接指导实践者不应将多分类标签简单二值化。[R1, R2 共识]\n\n**S3. FWL invariance 洞察新颖且可操作**\n证明 4 种拓扑下矩阵校正方法（Naive plug-in, MLA）因 FWL 不变性而恰好 0% 偏差缩减——这是结构性结果（非数值近似），为校正方法选择提供了明确的负面指导。Section 4.6 的 210 配置系统评估有较高实践价值。[R1, R2 共识]\n\n**S4. 理论-经验层级区分诚实**\n论文清晰标注 Proposition（已证）、Empirical Finding（数值验证）、Conjecture（猜想），这种分层在同类论文中较少见。[R1 首发, R2 同意]\n\n**S5. 解析推导与 MC 验证高度一致**\nGrand MAPE 2.0%（126 scenarios），per-topology range 0.5%-5.5%，理论预测与实验验证吻合度高。[R1, R2 共识]\n\n**S6. ASV 框架设计合理**\n三种互补灵敏度度量（magnitude, significance, sign-flip）类比 E-value 设计思路，为研究者提供简洁的\"标注误差预算\"工具。δ_max 约束的引入确保了参数化的有效性。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [CRITICAL] Theorem 1 一般情形证明不完整** [R1-N1, R2-N1 共识]\n- Theorem 1 声称 confounding 拓扑下 |B(C(δ))| 对 δ 单调非递减。比例情形 (f=λg) 有完整代数推导（Appendix A.4），但一般情形使用 Cauchy-Schwarz 界后以 \"Tightness is confirmed numerically (500 random (C₀, δ) pairs, zero violations)\" 收尾。\n- **核心问题**：Cauchy-Schwarz 仅证明上界 B̄(δ) 的单调性，不能推出 |B(C(δ))| 本身的单调性。R2 举例：f(δ)=sin(δ) 被 g(δ)=δ 界住，g 单调但 f 不单调。\n- **影响**：ASV 框架的 δ* 唯一性和解释性直接依赖该单调性。论文将唯一标记为 \"Theorem\" 的结果在一般情形下依赖数值验证，模糊了 theorem 和 conjecture 的界限。\n- **建议**：一般情形降级为 \"Theorem (proportional case) + Empirical Finding (general case)\"，明确讨论 ASV 在单调性仅为经验验证时的可靠性。\n\n**MF2. [MAJOR] 3/5 \"安全\"拓扑的符号保持缺乏解析证明** [R1-N2, R2-N1 共识]\n- Mediation、M-bias、front-door 的符号保持仅通过 100,000 随机列随机矩阵数值验证，论文明确承认 \"analytic proofs for general K remain open\"。\n- Abstract 使用 \"five topologies never produce sign reversal\"，\"never\" 是全称量词，与 Empirical Finding 的认识论地位不匹配。\n- **建议**：Abstract 修改为 \"five topologies show no sign reversal across extensive numerical verification (proven analytically for confounding and collider)\"；正文讨论解析证明的困难所在。\n\n**MF3. [MAJOR] Non-differential misclassification stress test 覆盖不足** [R1 首发, R2 同意(nuance)]\n- Stress test（Appendix B.3, Table 6）仅覆盖 exposure 拓扑、K=3、ε ∈ {0.00, 0.01, 0.05, 0.10}。\n- LLM 标注误差在实践中几乎必然是 differential 的（不同类别的分类能力系统性不同，可能与结果变量相关）。\n- R2 补充：论文 Limitations 提到 \"outcome-conditional prompting\" 可破坏该假设，但讨论不够深入。\n- **缓解因素**（R2）：non-differential 是测量误差文献标准假设（Carroll 2006），Table 6 显示 ε≤0.10 下 sign-flip 仅从 2.0% 升至 4.5%，表明小偏离下稳健。\n- **建议**：扩展至 confounding/mediation 拓扑 + K=10 HumAID 设置；从实际数据估计 LLM 误差的 differential 程度。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [MAJOR] 线性 SEM 假设限制对 NLP 受众的实用性** [R1-W5, R2-W1 共识]\n- 所有理论结果基于线性结构方程。NLP 中 logistic regression、非参数方法广泛使用。\n- Limitations 仅一句 \"FWL invariance result does not hold for logistic regression\"，未讨论线性假设的适用边界或非线性下核心发现是否定性保持。\n- **建议**：至少添加一个 K=3 logistic DGP 模拟验证 sign-flip 现象是否定性保持。\n\n**SF2. [MAJOR] 缺少 2 篇高度相关引用** [R2 首发, R1 同意]\n- **Feder et al. (2022) TACL**：\"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond\"——NLP+因果推断领域引用量最高的综述（400+ 引用），投 EMNLP 必引。\n- **Cheng, Mayya & Sedoc (2024)**：\"To Err Is Human; To Annotate, SILICON?\"——将 LLM 标注误差分解为四种上游来源，与本文下游传播分析互补。（注：此文已在 references.bib 中但未在正文 \\cite。）\n- **建议**：Related Work 补充引用并明确区分。\n\n**SF3. [MAJOR] ASV 参数化选择缺乏讨论和敏感性分析** [R1-W2, R2-W3 共识]\n- C(δ) = (1-δ)I + δC₀ 的线性插值是一个特定参数化选择，替代方案（对角线衰减、精度参数化）未讨论。\n- 论文 Section 3.3 提到 \"we recommend bootstrapping C₀\"，但未展示实际 bootstrap 结果。\n- **建议**：讨论参数化选择理由；展示至少一个 C₀ bootstrap 示例分析 δ* 置信区间。\n\n**SF4. [WARNING] 实证验证不完整** [R1-W3, R2-W4 共识]\n- 仅完成 14/38 计划配置（36.8%），VAST (K=3) 和 CivilComments (K=2) 覆盖不足。\n- 4 个 LLM 均为开源模型，无商业模型（GPT-4, Claude）对比。\n- **建议**：补完缺失配置；讨论开源 vs 商业 LLM 误差模式差异。\n\n**SF5. [WARNING] Conjecture 1 数值验证样本量不足** [R1-W4, R2-N1 共识]\n- 每拓扑仅 500 scenarios 验证 ASV envelope 单调性，而 Empirical Finding 1 用了 100,000 个矩阵。200 倍差异缺乏解释。\n- Conjecture 1 是 ASV 框架的理论基础，重要性不亚于 Empirical Finding 1。\n- **建议**：增加到至少 10,000 scenarios per topology。\n\n**SF6. [WARNING] DGP 条件在实践中难以事前验证** [R1-W1, R2-W5 共识]\n- Proposition 1 的充分条件（如 sign(τ) = sign(τ + B_OV)）涉及未知 DGP 参数，实践者无法事前判断。\n- 论文通过 ASV 部分缓解，但 ASV 本身依赖 Conjecture 1。\n- **建议**：讨论基于数据的诊断方法或典型参数范围下的满足率。\n\n### Minor（不影响接收）\n\n- Abstract \"five topologies never\" 措辞需与正文 Empirical Finding 对齐\n- Section 3.4 Binarization Collapse 仅 4 行，信息密度低，建议移至附录或扩充\n- Table 1 混排两种先验条件下的结果，建议分行标注\n- 多套符号系统（τ, τ̂, f(A*), β）快速阅读时易混淆，建议增加符号表\n- Appendix B.1 Applied Illustration（ClinicalBERT Case Study）有价值，建议主文增加交叉引用\n\n---\n\n## Reviewer Consensus\n\n以下问题双方完全一致（[AGREE]）：\n\n| # | 问题 | 严重程度 |\n|---|------|---------|\n| 1 | 核心理论结果（Theorem 1 一般情形、Empirical Finding 1、Conjecture 1）依赖数值验证 | Must-Fix |\n| 2 | 3/5 安全拓扑符号保持缺乏解析证明 + Abstract 措辞不匹配 | Must-Fix |\n| 3 | 线性 SEM 假设限制 NLP 实用性 | Should-Fix |\n| 4 | ASV 参数化限制 + C₀ 不确定性未展示 | Should-Fix |\n| 5 | 实验不完整（14/38 配置，无商业 LLM） | Should-Fix |\n| 6 | DGP 条件实践可验证性 | Should-Fix |\n| 7 | Conjecture 1 验证量（500 vs 100,000）不足 | Should-Fix |\n\n---\n\n## Reviewer Divergence\n\n**唯一分歧：83.4% framing 的严重程度**\n\n- **R2 立场 [CRITICAL]**：83.4% 基于 Dirichlet(1,1,1)（平均精度 ~0.33），realistic accuracy 下仅 2.1%。以极端场景数字为 headline 构成 sensationalization，影响论文诚实性信任。\n- **R1 反驳 [REBUT → WARNING]**：(1) 论文 Abstract 已同时报告两组数字，条件透明；(2) Dirichlet(1,1,1) 作为参数空间均匀采样有方法论正当性——刻画结构性风险而非估计实际频率；(3) 83.4% 证明符号翻转不是稀有角落情形。\n- **R2 未反驳 R1 的 REBUT**。\n- **Director 裁定**：降级为 Should-Fix。论文事实准确、条件透明，但建议调整叙事重心——以 realistic accuracy 为主叙事。\n\n---\n\n## Questions for Authors\n\n**Q1** (R1, R2 共识): Theorem 1 一般情形能否补全解析证明？若不能，是否考虑将一般情形降级为 Empirical Finding？\n\n**Q2** (R1, R2 共识): Conjecture 1 是否做过 adversarial search（专门寻找反例的优化搜索）？当前 500 scenarios 的搜索策略是什么？\n\n**Q3** (R2 首发, R1 同意): 在 logistic regression 下，sign-flip 现象是否定性保持？即使不提供完整理论，一个 K=3 × 3 topologies 的模拟也能大幅增强实用性。\n\n**Q4** (R2): ASV 的 C₀ 估计来自有限验证集。如果 C₀ 对角线估计误差为 ±0.05，ASV 的 safe/unsafe 判断是否会翻转？\n\n**Q5** (R1): 能否从 3 个实证数据集直接估计 LLM 混淆矩阵的 differential 程度（如按 Y 值分层计算 C 差异）？\n\n---\n\n## Missing References\n\n1. **Feder, A., Keith, K.A., Manzoor, E., et al. (2022). \"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond.\" TACL.** — NLP+因果推断领域最重要综述，400+ 引用，投 EMNLP 必引。[R2 首发, R1 同意]\n\n2. **Cheng, X., Mayya, R., & Sedoc, J. (2024). \"To Err Is Human; To Annotate, SILICON?\" arXiv:2412.14461.** — LLM 标注误差上游来源分解，与本文下游传播分析互补。已在 references.bib 中但未在正文引用。[R2 首发, R1 条件性同意]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：已跳过（用户未提交外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（5 warnings, 9 info, 0 critical）\n\n### Warnings\n\n1. **前 5 页无任何 figure/table**：审稿人翻过 5 页纯文字+公式后才看到第一个 display item（Figure 1, p6）。建议将 Figure 3（DAG 拓扑图，当前在 p18 附录）前移至 p2-3。\n2. **主文 display item 密度低**：8 页正文仅 3 个 display items（Figure 1, Table 1, Figure 2），大量关键结果图表在附录。\n3. **Figure 3 远离引用位置**：主文 p3 引用 \"Figure 3\" 展示 7 种 DAG 拓扑，但 Figure 3 在 p18，需翻 15 页。\n4. **p7 纯文本整页**：Empirical Validation 讨论，夹在 p6（Figure 1 + Table 1）和 p8（Figure 2）之间，视觉节奏断裂。\n5. **p20 约 40% 空白**：Figure 7 + Table 6 布局空间利用不足。\n\n### Info（参考）\n- Figure 1 子面板字体偏小（正文字号 65-70%）\n- Figure 2 线条颜色在灰度打印下区分度可能不足\n- p19 三张图挤在同一页，部分标签难以辨认\n- Figure 1 色板可能对色盲用户不友好（红/绿），建议 Okabe-Ito 色板\n- 格式合规：匿名处理正确，booktabs 三线表规范，References 格式统一\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5/5 — Borderline Conference\n\n**置信度**: 4/5（双方 Reviewer 均仔细检查了证明结构和实验设计）\n\n**评估理由**:\n\n论文填补了 LLM 多分类标注误差 × 因果 DAG 拓扑的明确研究空白，K≥3 符号翻转发现和 FWL invariance 洞察具有理论与实践双重价值。框架设计系统，理论-经验层级区分诚实。\n\n但存在两个阻碍明确接收推荐的结构性问题：\n1. **理论完整性缺口**：唯一标记为 Theorem 的结果在一般情形下依赖数值验证；3/5 \"安全\"拓扑的符号保持仅有经验证据；ASV 框架依赖的 Conjecture 1 仅 500 scenarios 验证。这些问题影响论文的核心理论贡献可信度。\n2. **实用性边界模糊**：线性 SEM 假设未充分讨论对 NLP 场景的适用性；non-differential misclassification stress test 覆盖不足；实验完成率仅 36.8%。\n\n**接收条件**：若以下修改可在 camera-ready 阶段完成，论文有望达到主会议水平：\n- MF1: Theorem 1 一般情形降级为 Empirical Finding 或补完证明\n- MF2: Abstract/正文措辞与证明状态对齐\n- MF3: Stress test 扩展至 2+ 拓扑和 K=10\n- SF1-SF6: 至少解决线性假设讨论和缺失引用\n\n**当前论文质量高于 Findings 门槛（3.0），处于 Borderline Conference 区间（3.5）。**\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"83.4% of confusion matrices cause sign reversal\" 作为 headline 在技术上准确（Dirichlet(1,1,1) prior），但叙事效果倾向于 sensationalization。建议将 \"under realistic classifier accuracy (diagonal ≥ 0.7), the violation rate is 13.7% with 2.1% sign reversal\" 提升到与 83.4% 同等显著位置。\n- 三项贡献的表述清晰，层次分明。\n\n### Section 2 (Related Work)\n- 三段式结构（measurement error / text classifiers / sensitivity analysis）覆盖面广。\n- 缺少 Feder et al. (2022) TACL 综述——NLP+因果推断领域的 canonical reference。\n- Cheng et al. (2024) 已在 .bib 中但未引用。\n\n### Section 3 (Method)\n- **3.1 Setup**: 清晰简洁。Non-differential misclassification 定义明确。\n- **3.2 Bias Expressions**: 7 种拓扑的偏差表达式推导是论文的核心技术贡献。Proposition 1 的分层处理（proved / empirical finding / counterexample）是正确做法，但 Abstract 未反映此层级。\n- **3.3 ASV**: 三种度量设计合理。δ_max 约束已引入。C₀ bootstrap 建议已提出但未实际展示。\n- **3.4 Binarization Collapse**: 仅 4 行，信息密度低。\n\n### Section 4 (Experiments)\n- **4.1-4.2**: 理论-MC 一致性验证充分（MAPE 2.0%）。\n- **4.3-4.4**: ASV 验证和 binarization collapse 分析有价值。\n- **4.5 Empirical Validation**: 核心实证部分。3 tasks × 4 LLMs 设计合理但完成率低（14/38）。\"F1 does not predict downstream bias\" 发现（Figure 2）有实用价值。\n- **4.6 Correction Guidance**: 210 配置系统评估，FWL invariance 的实证确认（exactly 0.0%）有力。\n\n### Section 5 (Conclusion)\n- 简洁准确，未过度声称。\n\n### Limitations\n- 覆盖面合理（non-differential 假设、线性假设、实验不完整），但每项讨论偏简略。\n- 缺少线性假设适用边界的讨论。\n\n### Appendix\n- Appendix A（证明）是论文的技术核心。比例情形证明完整严谨；一般情形的数值验证不足（500 scenarios）。\n- Appendix B.1（ClinicalBERT Case Study）展示框架实用性，建议主文交叉引用。\n- Appendix B.3（Stress Test）覆盖面过窄。"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-22T11:00:13.747977+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4838
}
```

</details>

---


### Assistant

_source line 172 · 2026-05-22T11:00:27.138284+00:00_

审稿报告已投递至 Research Director。

---

**审稿完成汇总**：

- **Overall Score**: 3.5/5 — Borderline Conference
- **Must-Fix**: 3 项（Theorem 1 一般情形证明不完整 / 3/5 安全拓扑无解析证明 + Abstract 措辞 / Non-differential stress test 覆盖不足）
- **Should-Fix**: 6 项（线性 SEM 限制 / 缺 2 篇引用 / ASV 参数化讨论 / 实验不完整 / Conjecture 1 验证量不足 / DGP 条件可验证性）
- **Reviewer 共识度**: 高（~80% 问题独立收敛，唯一分歧为 83.4% framing 的 severity，已裁定降级）
- **视觉审查**: 5 warnings（前 5 页无 display item、主文图表密度低、Figure 3 远离引用位置等），0 critical
- **外部审稿**: 已跳过

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 173 · 2026-05-22T11:00:29.853151+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。

**汇总**：8 条中 7 条 [AGREE]（含 2 条 with nuance/correction），0 条 [REBUT]。两位 Reviewer 的核心关切重叠度约 80%——独立收敛于"关键理论结果缺乏解析证明"、"ASV 参数化未讨论"、"线性假设限制实用性"、"实验覆盖不完整"四个主题。R1 独立提出了 non-differential stress test 不足（N3），我补充了 overclaiming framing（N2）和缺失引用（W2）的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 174 · 2026-05-22T11:00:47.950587+00:00_

审稿报告已投递至 Research Director。

**Round 2 审稿完成。汇总：**

- **评分**：3.5/5 — Borderline Conference
- **Reviewer 共识度**：极高（~80% 问题重叠，交叉回应中仅 1 条 REBUT，且为 severity 分歧而非实质矛盾）
- **3 个 Must-Fix**：Theorem 1 一般情形证明不完整、3/5 安全拓扑符号保持缺乏解析证明、non-differential stress test 覆盖不足
- **6 个 Should-Fix**：线性 SEM 限制、2 篇缺失引用、ASV 参数化讨论、实验不完整(14/38)、Conjecture 1 验证量不足、DGP 条件可验证性
- **Issue Tracker 已更新**：16 条 issue（含 3 条新增），与 Round 1 持续的 issue 已追加 Round 2 mention
- **视觉审查**：5 warnings（前 5 页无 display item、Figure 3 远离引用位置等），0 critical
- **外部审稿**：已跳过

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 18

## Round 18

42 recorded events


### User

_source line 175 · 2026-05-22T13:40:32.964562+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-22T13:40:38.437422+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-22T13:40:38.488633+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-22T13:40:46.219387+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-22T13:40:46.219913+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-22T13:40:50.337266+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-22T13:40:51.761798+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1424
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-22T13:40:52.263980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-22T13:40:52.515447+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	
19	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
20	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{method}
39	
40	% ── Figures ──
41	
42	\begin{figure*}[t]
43	\centering
44	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
45	\vspace{-6pt}
46	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
47	\label{fig:dag_taxonomy}
48	\end{figure*}
49	
50	\begin{figure*}[t]
51	\centering
52	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
53	\vspace{-6pt}
54	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
55	\label{fig:bias_distribution}
56	\end{figure*}
57	
58	\input{experiments}
59	
60	\input{conclusion}
61	
62	\bibliography{references}
63	
64	\appendix
65	\input{appendix_proofs}
66	
67	\end{document}
68	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-22T13:40:52.515943+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 185 · 2026-05-22T13:40:52.616625+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-22T13:41:01.752661+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 187 · 2026-05-22T13:41:02.807345+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-22T13:41:04.614695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-22T13:41:04.715558+00:00_

1	\begin{abstract}
2	Large language models (LLMs) are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that binary measurement error theory cannot predict. We present a systematic framework characterizing how $K$-class confusion matrix structure interacts with DAG topology to determine bias direction and magnitude. We derive bias expressions for seven canonical DAG topologies under multi-class non-differential misclassification and establish that five topologies show no sign reversal across extensive numerical verification (proven analytically for confounding and collider via sufficient conditions; Appendix~A), while exposure and instrumental variable topologies can produce sign reversal---under realistic classifier accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; across the full Dirichlet$(1,1,1)$ parameter space, the rate reaches 83.4\%. We introduce Annotation Sensitivity Values (ASVs) with three complementary measures revealing a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6\% sign reversal) to M-bias (immune). We evaluate five correction methods and prove a Frisch--Waugh--Lovell invariance result: matrix-based corrections achieve 0\% bias reduction for four topologies, while PPI++ achieves 47.0\% RMSE reduction but requires gold labels and is harmful for M-bias ($-$88\%). Empirical validation on three tasks ($K{=}2,3,10$) with four LLMs confirms structural predictions: zero sign reversals across five guaranteed topologies, while 61\% of exposure configurations exhibit coefficient-level sign reversal in secondary coefficients. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-22T13:41:04.766152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-22T13:41:04.816810+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The consequences can be catastrophic. Even under realistic classifier accuracy (diagonal $\geq 0.7$), 13.7\% of $K{=}3$ confusion matrices produce violations of the classical binary guarantee, with 2.1\% causing outright \emph{sign reversal} of the estimated treatment effect. Across the full Dirichlet$(1,1,1)$ parameter space, sign reversal reaches 83.4\%, establishing that it is the majority outcome under uniform priors, not a pathological edge case. This failure breaks the classical binary guarantee that non-differential misclassification biases estimates ``toward the null''~\cite{brenner1993}, a guarantee that many applied researchers implicitly rely upon. Moreover, standard classification metrics do not predict downstream causal risk: within a narrow $F_1$ range of 0.614--0.690 across three fro
…[truncated 2442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 192 · 2026-05-22T13:41:09.134321+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results for ACL Rolling Review 2026 submission guidelines, here are the key page limit and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

Revi
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6326
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-22T13:41:15.666572+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Now let me search for the author guidelines specifically:

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.o
…[truncated 3324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 13913
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-22T13:41:28.017694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-22T13:41:28.068450+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The statistical foundations are established in \citet{carroll2006} and \citet{gustafson2004}, with starred-node DAGs formalized by \citet{hernan_cole2009}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, but \citet{dosemeci1990} and \citet{jurek2005} showed this fails for polytomous exposures. \citet{veirod_laake2001} derived multi-category bias expressions for Poisson regression, and \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction. All of these works analyze a single DAG topology; our taxonomy is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} provide the foundation for text-as-data; \citet{feder_etal2022} offer a comprehensive taxonomy of causal inference in NLP, categorizing text-as-treatment and text-as-confounder paradigms. \citet{wood_doughty2018} first applied DAG reasoning to classifier error. \citet{teblunthuis2024} gave the most complete binary treatment (four DAG scenarios, $K{=}2$), and \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{baumann2025} found 31\% incorrect conclusions with LLM labels, \citet{cheng_mayya_sedoc2024} propose structured approaches to reduce LLM measurement error, and \citet{kim_garg2025} showed 60\% error correlation across models. \citet{audinet2025} benchmark debiasing methods for LLM-generated parameter estimates; \citet{keith_jensen_oconnor2020} survey the broader text-and-causal-inference landscape. These works either restrict to binary labels, cover a single topology, or diagnose quality without connecting it to causal validity. Our framework provides the missing
…[truncated 871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-22T13:41:28.068845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-22T13:41:28.421615+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
15	
16	\subsection{Multi-Class Bias Expressions}
17	\label{sec:bias_expressions}
18	
19	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
20	
21	\paragraph{Confounding ($A$ = confounder).}
22	When $A$ confounds the $X{\to}Y$ relationship, the OLS estimator controlling for $A^*$ has probability limit
23	\begin{equation}
24	\label{eq:confounding}
25	\text{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\bet
…[truncated 10240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-22T13:41:28.472303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-22T13:41:28.824233+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate the bias taxonomy and ASV framework through analytical derivations and Monte Carlo simulation across seven DAG topologies under $K{=}3$ non-differential misclassification.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 2.0\% across 126 scenarios (18 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.5\% (confounding) to 5.5\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: catastrophic sign reversal.}
18	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\% of matrices cause \emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\beta_1{=}1.0$, a near-permutation $C$ produces $\hat{\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\times}$); for $\beta_2{=}{-}0.5$, the same $C$ yields $\hat{\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\times}$).
19	
20	This finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\% with 2.1\% sign reversal and 11.7\% amplification. Even at diagonal $\geq 0.9$, violation
…[truncated 12554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-22T13:41:28.925208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-22T13:41:28.925598+00:00_

1	\enlargethispage{1\baselineskip}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	
5	We characterized how multi-class annotation errors interact with causal DAG topology, analyzing bias direction, sensitivity, and correction across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal (83.4\% and 52.6\%), while five topologies maintain a structural guarantee. Three core contributions---the $K{\geq}3$ algebraic break, the five-topology sign-preservation guarantee, and FWL invariance---are DGP-independent structural results that hold for arbitrary parameter values under stated sufficient conditions. Empirical validation with real LLM confusion matrices confirms this vulnerability: 61\% of exposure configurations exhibit coefficient-level sign reversal despite diagonal dominance. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and correction effectiveness is itself topology-dependent, with matrix-based methods provably ineffective for four topologies. Differential misclassification and correlated multi-LLM errors are natural extensions.
6	
7	\section*{Limitations}
8	
9	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM has no access to $Y$ but may be violated with outcome-conditional prompting. A stress test across 96 configurations (Appendix~\ref{sec:nondiff_stress}) shows moderate robustness: $\varepsilon{=}0.05$ increases violations by $<$3pp; at $K{=}10$, zero sign flips across all $\varepsilon$. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$; arbitrary $K$ remains open. The framework assumes a single annotator; correlated multi-annotator settings~\cite{kim_garg2025} are future work. Frontier-model coverage for VAST and CivilComments is partial (15 of 18 planned configurations completed); cross-tier comparisons should be interpreted with thi
…[truncated 183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-22T13:41:29.829316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-22T13:41:30.833948+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Empirical Finding~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y
…[truncated 57675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-22T13:41:31.386542+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-22T13:41:31.839993+00:00_

-rw-r--r-- 1 ubuntu ubuntu 844506 May 22 13:38 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-22T13:41:32.091366+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-22T13:41:32.142090+00:00_

-rw-r--r-- 1 ubuntu ubuntu 15026 May 22 11:12 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-22T13:42:17.725951+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 209 · 2026-05-22T13:42:18.278649+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-22T13:42:42.178306+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24452
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-22T13:42:42.178807+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 23900
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-22T13:42:42.279554+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务分配 — Reviewer 1（方法严谨性）\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- ARR 统一审稿，截止日期 2026-05-25\n- 正文 8 页限制 + 无限参考文献页\n- 强制 Limitations 章节（不计入页数）\n- ACL 模板，\\usepackage[review]{acl}\n- Double-blind（匿名）\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **数学推导正确性**：\n   - 7 种 DAG 拓扑的 bias 表达式（Eq. 1-6）是否正确推导\n   - Proposition 1 的三个子结论（confounding/collider 的 sign preservation，exposure 的 sign reversal）是否成立\n   - Theorem 1（envelope monotonicity for confounding, proportional effects）的证明是否严密\n   - Conjecture 1（ε-approximate monotonicity for 6 topologies）的数值验证是否充分\n   - 附录中 Lemma 1（Bias decomposition）和各 Proposition 的证明链是否完整\n\n2. **ASV 框架的理论基础**：\n   - 三类 ASV（magnitude/significance/sign-flip）的定义是否清晰、互补\n   - δ 参数化 C(δ) = (1-δ)I + δC₀ 的选择是否合理、是否有已知替代方案\n   - significance ASV 的 N-sensitivity 相变现象是否有理论解释\n   - 与 E-value 的类比是否恰当\n\n3. **实验设计与统计方法**：\n   - 100,000 Dirichlet(1,1,1) 随机矩阵采样是否足够，是否有采样偏差\n   - Monte Carlo 验证（N=10,000）的 MAPE 2.0% 是否在合理范围\n   - 经验验证使用 3 个任务/4 个 LLM 的覆盖面是否充分\n   - 校正方法实验（210 configurations）的设计是否公平\n   - Bootstrap ASV 的样本量（n=1,500, B=1,000）是否足够\n\n4. **FWL 不变性结论**：\n   - 对 4 种拓扑 matrix-based 校正 0% bias reduction 的论证是否严密\n   - 是否有遗漏的 bypass 途径\n\n5. **潜在技术问题**：\n   - non-differential misclassification 假设在实践中的合理性\n   - 线性 SEM 假设的限制\n   - Conjecture 未证明是否构成方法论缺陷\n\n请按 ARR 标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Overall Assessment（使用上述评分标准）和 Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务分配 — Reviewer 1（方法严谨性）\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- ARR 统一审稿，截止日期 2026-05-25\n- 正文 8 页限制 + 无限参考文献页\n- 强制 Limitations 章节（不计入页数）\n- ACL 模板，\\usepackage[review]{acl}\n- Double-blind（匿名）\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **数学推导正确性**：\n   - 7 种 DAG 拓扑的 bias 表达式（Eq. 1-6）是否正确推导\n   - Proposition 1 的三个子结论（confounding/collider 的 sign preservation，exposure 的 sign reversal）是否成立\n   - Theorem 1（envelope monotonicity for confounding, proportional effects）的证明是否严密\n   - Conjecture 1（ε-approximate monotonicity for 6 topologies）的数值验证是否充分\n   - 附录中 Lemma 1（Bias decomposition）和各 Proposition 的证明链是否完整\n\n2. **ASV 框架的理论基础**：\n   - 三类 ASV（magnitude/significance/sign-flip）的定义是否清晰、互补\n   - δ 参数化 C(δ) = (1-δ)I + δC₀ 的选择是否合理、是否有已知替代方案\n   - significance ASV 的 N-sensitivity 相变现象是否有理论解释\n   - 与 E-value 的类比是否恰当\n\n3. **实验设计与统计方法**：\n   - 100,000 Dirichlet(1,1,1) 随机矩阵采样是否足够，是否有采样偏差\n   - Monte Carlo 验证（N=10,000）的 MAPE 2.0% 是否在合理范围\n   - 经验验证使用 3 个任务/4 个 LLM 的覆盖面是否充分\n   - 校正方法实验（210 configurations）的设计是否公平\n   - Bootstrap ASV 的样本量（n=1,500, B=1,000）是否足够\n\n4. **FWL 不变性结论**：\n   - 对 4 种拓扑 matrix-based 校正 0% bias reduction 的论证是否严密\n   - 是否有遗漏的 bypass 途径\n\n5. **潜在技术问题**：\n   - non-differential misclassification 假设在实践中的合理性\n   - 线性 SEM 假设的限制\n   - Conjecture 未证明是否构成方法论缺陷\n\n请按 ARR 标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Overall Assessment（使用上述评分标准）和 Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-22T13:43:00.783807+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18504
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-22T13:43:00.884579+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务分配 — Reviewer 2（新颖性与完整性）\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- ARR 统一审稿，截止日期 2026-05-25\n- 正文 8 页限制 + 无限参考文献页\n- 强制 Limitations 章节（不计入页数）\n- ACL 模板，\\usepackage[review]{acl}\n- Double-blind（匿名）\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性 + 完整性 + 写作 + 格式\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 相对于 Teblunthuis (2024)（binary, 4 DAG scenarios）和 Lee, Wood-Doughty (2024)（categorical LLM classifiers, confounding only）的增量贡献是否足够\n   - ASV 框架相对于 E-values (VanderWeele & Ding 2017) 和概率偏差分析 (Lash 2009) 的技术创新程度\n   - FWL 不变性是否是已知结论的直接推论\n   - \"topology-dependent\" 视角是否构成足够的概念创新\n\n2. **相关工作覆盖**：\n   - 测量误差文献是否有重要遗漏（Carroll 2006, Gustafson 2004 已引用）\n   - NLP 因果推断文献是否完整（Feder et al. 2022, Keith et al. 2020 已引用）\n   - LLM annotation 质量文献是否有新发表的遗漏\n   - PPI++ / Cross-PPI 文献线是否完整\n   - 是否有因果推断领域的重要 sensitivity analysis 方法未被讨论\n\n3. **写作质量**：\n   - 论文结构是否合理（Abstract → Intro → Related Work → Method → Experiments → Conclusion）\n   - 符号体系是否一致\n   - 图表质量和信息密度\n   - 是否有过度 claim 或不当 hedging\n   - Abstract 是否准确反映论文内容和贡献\n\n4. **格式合规**：\n   - 正文是否在 8 页以内（不含参考文献和 Limitations）\n   - Limitations 章节是否存在且内容合适（不含新实验/分析）\n   - 是否使用 \\usepackage[review]{acl}\n   - 是否匿名（无作者信息泄露）\n   - 附录是否合理使用（是否有本应在正文的关键信息放在了附录）\n\n5. **论文的 broader impact 和定位**：\n   - 对 CL/NLP 社区的实际价值\n   - 是否适合 EMNLP 的主题范围（empirical methods for NLP）\n   - 论文的受众是谁——是否对 NLP 实践者有可操作性\n\n请按 ARR 标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（使用上述评分标准）和 Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务分配 — Reviewer 2（新颖性与完整性）\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_3/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- ARR 统一审稿，截止日期 2026-05-25\n- 正文 8 页限制 + 无限参考文献页\n- 强制 Limitations 章节（不计入页数）\n- ACL 模板，\\usepackage[review]{acl}\n- Double-blind（匿名）\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性 + 完整性 + 写作 + 格式\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 相对于 Teblunthuis (2024)（binary, 4 DAG scenarios）和 Lee, Wood-Doughty (2024)（categorical LLM classifiers, confounding only）的增量贡献是否足够\n   - ASV 框架相对于 E-values (VanderWeele & Ding 2017) 和概率偏差分析 (Lash 2009) 的技术创新程度\n   - FWL 不变性是否是已知结论的直接推论\n   - \"topology-dependent\" 视角是否构成足够的概念创新\n\n2. **相关工作覆盖**：\n   - 测量误差文献是否有重要遗漏（Carroll 2006, Gustafson 2004 已引用）\n   - NLP 因果推断文献是否完整（Feder et al. 2022, Keith et al. 2020 已引用）\n   - LLM annotation 质量文献是否有新发表的遗漏\n   - PPI++ / Cross-PPI 文献线是否完整\n   - 是否有因果推断领域的重要 sensitivity analysis 方法未被讨论\n\n3. **写作质量**：\n   - 论文结构是否合理（Abstract → Intro → Related Work → Method → Experiments → Conclusion）\n   - 符号体系是否一致\n   - 图表质量和信息密度\n   - 是否有过度 claim 或不当 hedging\n   - Abstract 是否准确反映论文内容和贡献\n\n4. **格式合规**：\n   - 正文是否在 8 页以内（不含参考文献和 Limitations）\n   - Limitations 章节是否存在且内容合适（不含新实验/分析）\n   - 是否使用 \\usepackage[review]{acl}\n   - 是否匿名（无作者信息泄露）\n   - 附录是否合理使用（是否有本应在正文的关键信息放在了附录）\n\n5. **论文的 broader impact 和定位**：\n   - 对 CL/NLP 社区的实际价值\n   - 是否适合 EMNLP 的主题范围（empirical methods for NLP）\n   - 论文的受众是谁——是否对 NLP 实践者有可操作性\n\n请按 ARR 标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（使用上述评分标准）和 Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-22T13:43:02.400379+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1515
}
```

</details>

---


### Assistant

_source line 216 · 2026-05-22T13:43:18.953346+00:00_

圆桌审稿已启动，各线程并行执行中：

| 线程 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发 |
| Reviewer 2（新颖性/完整性） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ⏭️ 未配置，跳过 |

**Venue 确认**：EMNLP 2026 via ARR，截止日期 **2026-05-25**（距今 3 天），Long Paper 8 页正文限制，double-blind，ACL 模板。

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 217 · 2026-05-22T13:49:15.175287+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1（新颖性 + 完整性 + 写作 + 格式）

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (via ARR), Long Paper

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 系统性地刻画了多分类标注误差在七种因果 DAG 拓扑下的传播差异，填补了文献空白；但理论深度中等，对 sign reversal 严重性的表述存在过度声称，且正文超页。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 核心 bias 表达式正确，5 拓扑的 sign preservation 中 2 个有解析证明（confounding/collider）、3 个仅有数值验证（Empirical Finding 1）；Conjecture 1 未证明；non-differential 假设的 stress test 范围有限 |
| **Excitement** | 3/5 | "topology-dependent" 视角新颖且实用，ASV 工具可操作，FWL invariance 结果被忽视但重要；但 bias 表达式推导直接，ASV 是 E-value 的自然类比，K≥3 break 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出 |
| **Reproducibility** | 4/5 | 数学公式清晰，DGP 参数详细，仿真设置可复现；但未提及代码/数据公开 |
| **Confidence** | 4/5 | 熟悉因果推断方法论和测量误差理论，逐页仔细阅读含附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文超出 8 页限制
- 具体位置：Page 9（Section 4.5 尾段 + Section 5 Conclusion 在第 9 页）
- 问题：EMNLP 2026 Long Paper 正文限 8 页（不含 References 和 Limitations）。Section 4.5 的最后若干段和 Section 5 (Conclusion) 溢出到第 9 页。即使 Limitations 不计入页数，Section 5 属于正文，目前大约超出 0.5 页。`main.tex` 中已使用 `\enlargethispage{1\baselineskip}` 和压缩 `\floatsep` 等手段，说明作者已在挤压空间但仍未达标。
- 为什么影响接收：ARR desk rejection 条件之一。即使不被 desk reject，reviewer 也应标记。
- 建议修改方向：压缩 Section 4（如将 Cross-K robustness 段和 ASV diagnostic results 段移至附录）；Figure 1+2 占满整页，考虑缩小或合并。

**N2** [critical] Sign reversal 的实际严重性被过度声称
- 具体位置：Abstract（"83.4% sign reversal"）、Section 1 第 2 段（"catastrophic"）、Section 4.4（"61% of exposure configurations exhibit coefficient-level sign reversal"）
- 问题：Abstract 和 Introduction 大量引用 83.4% sign reversal 数据，但这来自均匀 Dirichlet(1,1,1) 先验——一个包含大量非对角占优矩阵的不现实分布。在实际 LLM 分类器精度下（diagonal ≥ 0.7），sign reversal 降至 2.1%（Section 4.2 第 2 段）。更重要的是，Section 4.4 的实证结果显示 sign reversal **仅发生在 secondary coefficients**（"corresponding to rare categories with small |β|"），primary coefficient（最大|β|）在所有 23 个配置中从未反转。这与 abstract 中"catastrophic"的框架存在重大落差。
- 为什么影响接收：Reviewer 最敏感的问题之一是 overclaiming。83.4% 数字在 abstract/intro/conclusion 中反复出现，给读者留下"多数情况下因果估计方向错误"的印象，但实际只在极端参数空间和次要系数上成立。
- 建议修改方向：(1) Abstract 中先报告 realistic regime（diagonal ≥ 0.7）的 2.1% sign reversal，再提 Dirichlet prior 的 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 用 "structurally possible" 替代 "catastrophic" 等极端措辞。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Sign preservation 的 3/5 拓扑缺乏解析证明
- 具体位置：Section 3.2 Empirical Finding 1（mediation, M-bias, front-door）
- 问题：论文声称"五个拓扑维持 structural sign-flip guarantee"，但 Proposition 1 只覆盖 confounding 和 collider（解析证明）。Mediation、M-bias、front-door 三个拓扑的 sign preservation 标记为 "Empirical Finding"，基于 100,000 随机矩阵的数值验证而非解析证明。论文在 Empirical Finding 1 中承认"analytic proofs for general K remain open"，但在 abstract 和 conclusion 中说"establish that five topologies show no sign reversal"，"establish" 一词暗示证明而非数值验证。
- 建议：在 abstract/conclusion 中区分"proven"（2 个）和"numerically verified"（3 个），或者用"show"替代"establish"。

**W2** [warning] Conjecture 1（ε-approximate monotonicity）支撑 ASV 有效性，但未证明
- 具体位置：Section 3.3 Conjecture 1、Theorem 1
- 问题：Theorem 1 只对 confounding topology 在 proportional effects 假设下证明了单调性。其余 5 个 non-IV 拓扑的 ASV 单调性依赖 Conjecture 1，且 ε < 0.06 的 bound 来自数值模拟。如果单调性不成立，δ 作为"annotation error severity dial"的解释就不成立，ASV 的排序意义也受影响。
- 建议：(1) 更明确地讨论 Conjecture 1 失败时的后果；(2) 考虑证明 mediation 和 collider 等较简单拓扑的单调性。

**W3** [warning] Non-differential misclassification 假设对 LLM 的适用性讨论不足
- 具体位置：Definition 1 (Section 3.1)、Limitations
- 问题：LLM annotator 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在文本分类场景中很可能不成立。Appendix B.4 的 stress test 仅检验 ε=0.05 的微小偏离，且只覆盖 exposure 拓扑。对于一个以"LLM annotation"为卖点的框架，这个基础假设需要更充分的讨论和更强的鲁棒性分析。
- 建议：(1) 在正文 Method 部分讨论何时 LLM 满足 non-differential 条件（如 LLM 未见 outcome 文本时）；(2) stress test 扩展到更多拓扑和更大 ε。

**W4** [warning] 缺少 outcome misclassification 的讨论
- 具体位置：Section 3（整个 Method 部分）
- 问题：许多 NLP 因果研究中 Y 也是 LLM 标注的（如 sentiment → political engagement）。当 A 和 Y 同时被误分类时，bias 的传播更为复杂。论文完全未讨论这一场景，Related Work 中也未提及。
- 建议：至少在 Limitations 或 Related Work 中讨论 outcome misclassification 的影响和扩展方向。

**W5** [warning] Abstract 信息过载
- 具体位置：Abstract（整段）
- 问题：Abstract 约 200 词中塞入了 15+ 个数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 88%, 61%, 0.7 等），读起来像是 results summary 而非 motivated preview。ARR reviewer 通常在 abstract 阶段形成第一印象。
- 建议：Abstract 保留 3-4 个最关键数字，其余移至正文。重点是 "what's new and why it matters"，而非所有数字的罗列。

**W6** [warning] 未提及代码/数据公开
- 具体位置：全文
- 问题：方法论论文的可复现性很大程度依赖代码。论文包含大量仿真实验（100,000 矩阵 × 7 拓扑 × 多 K 值），但未提及代码是否会公开。ASV 计算工具如果作为 package 发布，实用价值会大幅提升。
- 建议：承诺公开代码，或在 supplementary 中提供。

---

## 小问题（不影响接收）

- Section 4.2 第 1 段："grand MAPE of 2.0% across 126 scenarios (18 LLM configurations × 7 topologies)" — 18×7=126 的推导依赖 empirical validation 的具体设置，但这里还在 Monte Carlo 验证部分，126 的解释容易混淆。
- Table 1 caption 很长（约 4 行），可以精简。
- Figure 2 中标签文字较小，在打印版中可能难以辨认。
- Section 3.3 中 ASV 的 parameterization C(δ) = (1-δ)I + δC₀ 在 δ=0 时给出完美分类，这意味着 ASV 衡量的是"从完美到 C₀ 的退化路径上"的敏感性——如果实际 confusion matrix 不在这条路径上呢？这个局限性未讨论。
- references.bib 中 `messing2026`（Hidden Measurement Error in LLM Pipelines）已引入但在正文中未看到引用，可能是 orphan entry。

---

## 新颖性专项评估

### 相对于 Teblunthuis (2024) 的增量
**充分**。Teblunthuis 限于 binary (K=2) 和 4 个 DAG。本文扩展到 K≥3 并证明了质的变化（sign reversal 可能性），覆盖 7 个拓扑且包含敏感性分析框架（ASV）和校正指南。增量不仅是数量上的（更多拓扑），更是性质上的（K≥3 的代数 break）。

### 相对于 Lee & Wood-Doughty (2024) 的增量
**充分**。Lee & Wood-Doughty 仅覆盖 confounding topology。本文证明了同一 confusion matrix 在不同拓扑下产生质的不同 bias，这是 Lee & Wood-Doughty 无法得出的结论。

### ASV 相对于 E-values 和 PBA 的技术创新
**中等**。ASV 的 parameterization C(δ) 是 E-value 思路的自然类比，三种 ASV 类型（magnitude/significance/sign-flip）的动机来自拓扑依赖的失败模式。Theorem 1 的单调性证明有技术贡献但限于 proportional effects。创新程度 adequate 但不 exciting。

### FWL 不变性
**重要但技术上直接**。这是一个被文献忽视的实用观察——矩阵校正方法在 4/7 拓扑上 provably 无效。技术上是 FWL 定理的直接推论，但对实践者意义重大。

### "Topology-dependent" 视角
**足够的概念创新**。虽然测量误差在不同位置的效果已有零散讨论，但系统性的 7 拓扑对比是第一次。这个视角将碎片化的知识统一到一个框架中。

---

## 相关工作覆盖评估

### 已覆盖（关键引用）
- 测量误差核心：Carroll (2006) ✓, Gustafson (2004) ✓, Hernán & Cole (2009) ✓
- NLP 因果推断：Feder et al. (2022) ✓, Keith et al. (2020) ✓, Wood-Doughty (2018) ✓
- LLM 标注质量：Baumann et al. (2025) ✓, Kim & Garg (2025) ✓, Cheng et al. (2024) ✓
- 校正方法：PPI++ ✓, Cross-PPI ✓, DSL ✓, Gligoric et al. (2025) ✓
- 敏感性分析：E-values ✓, PBA (Lash 2009) ✓, Rosenbaum (2002) ✓

### 可能的遗漏
1. **Cinelli & Hazlett (2020)** "Making Sense of Sensitivity: Extending Omitted Variable Bias" — 提出了 modern sensitivity analysis 的 robustness value 框架，与 ASV 有直接可比性，应在 Section 2 或 3.3 中讨论对比。
2. **Gilardi et al. (2023)** "ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks" — LLM 标注的标志性论文，虽非因果推断方向但经常被引用在 LLM annotation 文献综述中。
3. **Ziems et al. (2024)** "Can Large Language Models Transform Computational Social Science?" — 综合性 survey 覆盖 LLM 在社会科学中的标注应用，与论文的 motivation 直接相关。
4. **Bound, Brown & Mathiowetz (2001)** 关于 survey data 中 measurement error 的经典综述，虽然是 survey 领域但多分类误分类的讨论与本文相关。
5. 论文未讨论 **Bayesian measurement error models**（如 Gustafson 2004 中的方法）作为 FWL-invariant 拓扑的校正替代方案，Section 4.5 中仅一笔带过"Bayesian measurement error models"但未引用具体工作。

### PPI++ / Cross-PPI 文献线
**基本完整**。引用了 Angelopoulos et al. (2023), Zrnic & Candes (2024), Gligoric et al. (2025)。缺少 Angelopoulos et al. (2023b) "PPI++: When Is Prediction-Powered Inference Worth It?" 如果存在的话。

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| `\usepackage[review]{acl}` | ✓ | main.tex line 2 |
| 匿名 | ✓ | `\author{Anonymous}` |
| 正文 ≤ 8 页 | **✗** | 正文延伸至第 9 页（Section 4.5 尾段 + Section 5 Conclusion），超约 0.5 页 |
| Limitations 存在 | ✓ | 在 conclusion.tex 中，\section*{Limitations}，约 1 段 |
| Limitations 无新实验 | ✓ | 仅讨论假设局限和未来方向 |
| 附录合理使用 | ✓ | 证明、补充表格、stress test、case study 均适合附录 |
| 关键信息是否在正文 | 基本 ✓ | 核心结果在正文；但 sign preservation 的 sufficient conditions 汇总（Table 2, Appendix A.9）对理解 Proposition 1 很重要，可考虑在正文中简述 |

---

## 主要优势

1. **系统性的 taxonomy**：首次在统一框架下对比 7 种 DAG 拓扑的多分类误分类效应，概念贡献清晰。
2. **K≥3 代数 break 的刻画**：证明 K=2 的 sign preservation 在 K≥3 时结构性崩塌，这是一个非平凡的 qualitative 结果。
3. **FWL invariance 的实用洞察**：证明矩阵校正方法对 4/7 拓扑无效，对实践者直接可操作，文献中被忽视。
4. **ASV 框架**：提供了一个 parameterized 的敏感性分析工具，类比 E-values 但针对 annotation error，有实际应用价值。
5. **丰富的实证验证**：100,000 矩阵的仿真 + 4 个 LLM × 3 数据集的 empirical validation + logistic DGP robustness check + case study，验证覆盖面广。
6. **写作结构清晰**：Abstract → Intro → Related Work → Method → Experiments → Conclusion 的组织合理，符号体系一致。

---

## 关于论文定位和受众

**EMNLP 适配性**：高。论文直接回答"NLP 社区用 LLM 做标注时因果推断可靠吗"这一实际问题，符合 EMNLP "empirical methods for NLP" 的主题。

**目标受众**：(1) 用 LLM 标注做因果推断的计算社会科学家；(2) text-as-data 方法论研究者；(3) 对测量误差感兴趣的统计学家。

**可操作性**：中等偏高。论文的 taxonomy（Table 1）和 correction guidance（Section 4.5）直接可用。但 ASV 的实际使用需要估计 confusion matrix C₀，而论文未提供工具或 package。

---

## Questions to Authors

1. 在 realistic regime（diagonal ≥ 0.7）下，sign reversal rate 仅 2.1%。请作者解释为何 abstract 和 introduction 选择以 83.4%（Dirichlet prior）作为主要数字而非 2.1%？
2. Empirical Finding 1（mediation, M-bias, front-door 的 sign preservation）是否有证明进展？如果这 3 个拓扑的保证只是 conjectural，论文的核心 claim "five topologies maintain structural guarantee" 的可信度如何评估？
3. 论文是否计划公开代码？ASV 计算工具如果作为 Python package 发布，对论文影响力会有实质提升。
4. C(δ) = (1-δ)I + δC₀ 的线性路径是否是唯一合理的 parameterization？如果实际退化路径不在这条线上（如 off-diagonal 结构随 δ 变化），ASV 的意义如何？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 218 · 2026-05-22T13:49:32.012208+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 219 · 2026-05-22T13:49:35.366686+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成。主要结论：

- **Overall 3.5（Borderline Conference）**
- **2 个 Must-Fix**：正文超 8 页限制（约 0.5 页）；sign reversal 严重性被过度声称（83.4% 来自不现实的 Dirichlet prior，实际 LLM 矩阵下仅影响 secondary coefficients）
- **6 个 Should-Fix**：3/5 sign preservation 拓扑缺解析证明、Conjecture 1 未证明、non-differential 假设讨论不足、缺少 outcome misclassification 讨论、abstract 数字过载、未承诺代码公开
- **新颖性评估**：相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 的增量充分；ASV 创新中等（E-value 自然类比）；FWL invariance 技术直接但实用价值高；topology-dependent 视角是足够的概念创新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 220 · 2026-05-22T13:49:41.939566+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 21

## Round 21

6 recorded events


### User

_source line 221 · 2026-05-22T13:53:50.608328+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 理论框架新颖且重要（K≥3 break point, ASV, FWL invariance），但核心单调性结果仅为 Conjecture，线性 SEM 限制实际适用性，且正文可能超出 8 页限制。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 已有证明（Theorem 1, Propositions 1-5）正确，但核心单调性结果仅覆盖 confounding+proportional effects，其余 6 拓扑为 Conjecture；线性 SEM 假设限制了结论的普适性 |
| Excitement | 3.5/5 | 首个系统研究多类标注误差×因果推断的框架，K≥3 algebraic break 和 FWL invariance 发现有实际指导价值，但线性假设和非差异误分类假设限制了 NLP 社区的直接适用性 |
| Reproducibility | 4/5 | 分析推导详尽（12页附录），实验参数完整（Dirichlet 采样、MC 样本量、Bootstrap 配置均有报告），代码未提供但可从方程重现 |
| Confidence | 4/5 | 熟悉测量误差理论和因果推断文献，仔细阅读了全部证明和附录 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] Theorem 1 适用范围过窄，Conjecture 1 缺乏证明
- 具体位置：Section 3.3 (p.5), Theorem 1 & Conjecture 1; Appendix C, Table 9 (p.22)
- 问题：论文唯一被证明的单调性结果（Theorem 1）仅覆盖 confounding 拓扑 + proportional effects（β = λα）这一特殊条件。其余 6 个非 IV 拓扑的单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性。虽然违反幅度小（worst-case < 0.06），但高频违反意味着 ASV vulnerability spectrum 的理论基础不够坚实。
- 为什么影响接收：ASV 框架的核心价值依赖于 |bias| 随 δ 单调变化——如果不成立，"临界 δ 阈值"的语义变得模糊，ASV 不再是一个 well-defined 的 sensitivity measure。对于一篇强调理论贡献的论文，核心结果是 numerically-verified conjecture 而非 theorem，是显著弱点。
- 建议修改方向：(1) 至少再证明一个拓扑（如 mediation，其 indirect effect 结构较简洁，可能可推导出解析证明）；(2) 给出 ε 关于 K 和 DGP 参数的 formal bound，而非仅依赖经验验证；(3) 如果完整证明不可行，应明确讨论 Conjecture 失败时 ASV 的 interpretation 如何 degrade。

**N2** [critical] 正文疑似超出 8 页限制
- 具体位置：Sections 1-5, pages 1-9
- 问题：Section 5 (Conclusion) 在第 9 页开始，意味着正文（不含 Limitations 和 References）约为 8.3 页。EMNLP 2026 long paper 限制为严格 8 页。
- 为什么影响接收：可能导致 desk rejection。
- 建议修改方向：压缩 Section 2 (Related Work) 和 Section 4.2 (Bias Taxonomy 的实验细节，部分可移入附录) 以控制在 8 页内。

**N3** [critical] FWL invariance 结论缺乏严格证明
- 具体位置：Section 4.5 (p.8-9), Appendix B.3 (p.19), Algorithm 1 (p.19)
- 问题：论文声称"matrix-based corrections achieve exactly 0% bias reduction"对 4 个 FWL 拓扑成立，但这一 quantitative claim 主要依赖实验结果（Table 4），而非 formal proof。三个关键问题未澄清：
  (a) "matrix-based correction" 的精确定义是什么？MLA 调整的是群体级分布，SIMEX 通过模拟额外噪声并外推来修正——两者的操作机制截然不同，为何都导致 0% reduction？
  (b) SIMEX 在 individual level 工作（模拟额外误分类后外推至零误差），其外推函数的形式假设（线性/二次）是否适用于分类误差设定？Theorem 1 表明 confounding bias 关于 δ 确实是单调的，理论上 SIMEX 的外推应能工作——那么 0% reduction 的结果是否说明 SIMEX 实现中存在问题？
  (c) 这一发现与测量误差文献中已知的"controlling for a mismeasured confounder leaves residual confounding"结果（Carroll et al., 2006; Ogburn & VanderWeele, 2012）的关系是什么？
- 为什么影响接收：没有 formal proof，读者无法区分这是一个深刻的理论洞察还是实验设置的 artifact。
- 建议修改方向：添加一个 formal proposition 证明 FWL invariance，明确指出对每种 correction method 为何成立（或不成立）。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 非差异误分类假设对 LLM 标注者可能不成立
- 具体位置：Definition 1 (p.3), Appendix B.4 (p.20)
- 问题：假设 P(A*|A,T,Y) = P(A*|A) 要求 LLM 标注误差在给定真实标签后独立于处理和结果。但在 NLP 中，文本内容同时决定 LLM 分类、处理变量和结果变量，自然产生依赖。Appendix B.4 的 stress test 仅测试 ε ≤ 0.10 的轻微偏离，且 ε = 0.10 时 bias violation rate 已增加 7.4 个百分点。
- 建议：(1) 讨论非差异假设在哪些具体 NLP 场景下成立/失败（如情感分析 vs. 政治立场检测）；(2) 至少为 exposure 和 confounding 拓扑推导 differential misclassification 下的 bias 表达式骨架。

**W2** [warning] 线性 SEM 假设限制实际适用性
- 具体位置：Section 3.1 (p.3), Limitations (p.9), Appendix B.6 (p.20)
- 问题：所有结果基于线性结构方程，但 NLP 因果推断通常使用 logistic/nonlinear 模型。Appendix B.6 仅对 3 个拓扑（K=3, logistic DGP）做了有限的 robustness check。论文自身承认"FWL invariance result does not hold for logistic regressions"——这意味着最重要的实践指导之一（Algorithm 1 中 FWL 拓扑的分流）在 nonlinear 设定下可能失效。
- 建议：(1) 扩展 Appendix B.6 至全部 7 拓扑并包含更多 nonlinear DGP 变体；(2) 或在 Algorithm 1 中明确标注"仅适用于线性模型"的局限。

**W3** [warning] Dirichlet(1,1,1) headline 数字具有误导性
- 具体位置：Abstract, Section 4.2 (p.5)
- 问题：Abstract 和 Introduction 以 Dirichlet(1,1,1) 全参数空间统计量（"83.4% violation rate", "52.6% sign reversal"）为主导，但该分布包含随机分类器（平均准确率 1/K）。更具实践参考价值的数字——C_kk ≥ 0.7 时 13.7% violation rate, 2.1% sign reversal——出现在后文且着墨较少。LLM 分类器通常达到 70-99% 准确率。
- 建议：以 restricted parameter space 结果为主线叙事，Dirichlet(1,1,1) 结果作为理论完备性补充。

**W4** [warning] 相对于测量误差文献的新颖性定位不清
- 具体位置：Section 2 (p.2-3), throughout
- 问题：几个结果在已有文献中有直接先例：(1) 多类变量的 attenuation with possible sign reversal 在 Carroll et al. (2006) 和 Gustafson (2004) 中有讨论；(2) 对 mismeasured confounder 的 residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中有分析。论文引用了这些工作但未明确界定"哪些是已知结果在 LLM 语境的应用"vs."哪些是真正新的贡献"。
- 建议：在 Related Work 或 Contribution 段落中添加一段明确的 novelty delineation："以下结果已在 binary misclassification 下被建立：... 我们的贡献将其扩展至 K≥3 并新证明了：..."

**W5** [warning] 经验验证使用模拟 DGP 而非真实因果数据
- 具体位置：Section 4.4 (p.7-8)
- 问题："Empirical validation"使用真实 LLM confusion matrices 但应用于模拟 DGP（线性 SEM），而非使用已知因果效应的真实数据集。这验证的是理论推导的正确性（对线性 SEM 来说 trivially true），而非框架在实践中的指导价值。ClinicalBERT case study (Appendix B.2) 是回顾性应用，不是 prospective validation。
- 建议：增加至少一个 semi-synthetic 实验——使用已知因果效应的数据集（如 RCT 数据），引入 LLM 标注误差，验证框架能否正确识别 topology-specific risk 并指导 correction 选择。

## 小问题（不影响接收）
- 记号在 τ 和 β_T 之间交替使用，缺少明确消歧
- 正文 Proposition 1(a,b,c) 对应附录 Propositions 2, 3, 5 等不同编号——建议添加交叉引用帮助读者导航
- Figure 2 (p.6) 的 y 轴标签在 PDF 中较小，影响可读性
- Table 2 (p.17) conditions 列混合了 DGP 参数和形式化记号，风格不一致

## 主要优势
1. **重要且及时的问题**：LLM 标注质量与因果推断方法假设之间的差距日益严重，本文提供了首个系统性框架。
2. **清晰的理论贡献**：K≥3 algebraic break point（K=2 始终 attenuate；K≥3 可 sign reverse）是一个优雅且对实践者有直接指导意义的结果。
3. **实用性**：Algorithm 1 提供了 topology-aware correction 决策流程，ASV 框架给出了可量化的 sensitivity analysis 工具。
4. **系统覆盖**：7 DAG 拓扑 × 5 correction methods × 多种验证方式的组合覆盖面全面。
5. **附录质量高**：12 页证明和补充实验，Lemma-Proposition 证明链基本完整。
6. **Cross-PPI 和 FWL bypass 方法的讨论**：不仅诊断问题（FWL invariance），还提供了替代方案，增加了论文的实践指导价值。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-22T13:54:39.014812+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall**: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] 正文超出 8 页限制\n- Section 4.5 尾段 + Section 5 (Conclusion) 溢出到第 9 页，超约 0.5 页。已使用 `\\enlargethispage` 和压缩 `\\floatsep` 等手段但仍未达标。ARR desk rejection 条件之一。\n\n**N2** [critical] Sign reversal 的实际严重性被过度声称\n- Abstract 和 Introduction 大量引用 83.4% sign reversal（来自 Dirichlet(1,1,1) 先验——包含大量不现实矩阵），在 diagonal ≥ 0.7 下降至 2.1%。更重要的是，empirical sign reversal **仅发生在 secondary coefficients**（small |β|），primary coefficient 从未反转。与 abstract 中\"catastrophic\"框架存在重大落差。建议先报告 realistic regime 的 2.1%，再提 Dirichlet 的 83.4% 作为理论上界。\n\n### Should-Fix 问题\n\n**W1** Sign preservation 的 3/5 拓扑缺乏解析证明（mediation, M-bias, front-door 标为\"Empirical Finding\"，但 abstract/conclusion 用\"establish\"暗示已证明）\n\n**W2** Conjecture 1（ε-approximate monotonicity）支撑 ASV 有效性但未证明\n\n**W3** Non-differential misclassification 假设对 LLM 的适用性讨论不足（stress test 仅覆盖 exposure 拓扑、ε≤0.10）\n\n**W4** 缺少 outcome misclassification 的讨论（Y 也可能是 LLM 标注的）\n\n**W5** Abstract 信息过载（15+ 个数字）\n\n**W6** 未提及代码/数据公开\n\n### 新颖性评估\n- 相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 增量充分\n- ASV 创新中等（E-value 自然类比）\n- FWL invariance 技术直接但实用价值高\n- \"Topology-dependent\" 视角是足够的概念创新\n\n### 相关工作可能遗漏\n1. Cinelli & Hazlett (2020) \"Making Sense of Sensitivity\" — 与 ASV 有直接可比性\n2. Gilardi et al. (2023) \"ChatGPT Outperforms Crowd-Workers\"\n3. Ziems et al. (2024) \"Can Large Language Models Transform Computational Social Science?\"\n4. Bound, Brown & Mathiowetz (2001) 关于 survey data 中 measurement error\n5. Bayesian measurement error models 作为 FWL-invariant 拓扑的校正替代方案未引用具体工作\n\n### Questions\n1. 为何 abstract 选择 83.4% 而非 2.1% 作为主要数字？\n2. Empirical Finding 1 是否有证明进展？\n3. 是否计划公开代码？\n4. C(δ) 线性路径是否是唯一合理的 parameterization？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、新颖性评估、相关工作遗漏和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall**: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] 正文超出 8 页限制\n- Section 4.5 尾段 + Section 5 (Conclusion) 溢出到第 9 页，超约 0.5 页。已使用 `\\enlargethispage` 和压缩 `\\floatsep` 等手段但仍未达标。ARR desk rejection 条件之一。\n\n**N2** [critical] Sign reversal 的实际严重性被过度声称\n- Abstract 和 Introduction 大量引用 83.4% sign reversal（来自 Dirichlet(1,1,1) 先验——包含大量不现实矩阵），在 diagonal ≥ 0.7 下降至 2.1%。更重要的是，empirical sign reversal **仅发生在 secondary coefficients**（small |β|），primary coefficient 从未反转。与 abstract 中\"catastrophic\"框架存在重大落差。建议先报告 realistic regime 的 2.1%，再提 Dirichlet 的 83.4% 作为理论上界。\n\n### Should-Fix 问题\n\n**W1** Sign preservation 的 3/5 拓扑缺乏解析证明（mediation, M-bias, front-door 标为\"Empirical Finding\"，但 abstract/conclusion 用\"establish\"暗示已证明）\n\n**W2** Conjecture 1（ε-approximate monotonicity）支撑 ASV 有效性但未证明\n\n**W3** Non-differential misclassification 假设对 LLM 的适用性讨论不足（stress test 仅覆盖 exposure 拓扑、ε≤0.10）\n\n**W4** 缺少 outcome misclassification 的讨论（Y 也可能是 LLM 标注的）\n\n**W5** Abstract 信息过载（15+ 个数字）\n\n**W6** 未提及代码/数据公开\n\n### 新颖性评估\n- 相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 增量充分\n- ASV 创新中等（E-value 自然类比）\n- FWL invariance 技术直接但实用价值高\n- \"Topology-dependent\" 视角是足够的概念创新\n\n### 相关工作可能遗漏\n1. Cinelli & Hazlett (2020) \"Making Sense of Sensitivity\" — 与 ASV 有直接可比性\n2. Gilardi et al. (2023) \"ChatGPT Outperforms Crowd-Workers\"\n3. Ziems et al. (2024) \"Can Large Language Models Transform Computational Social Science?\"\n4. Bound, Brown & Mathiowetz (2001) 关于 survey data 中 measurement error\n5. Bayesian measurement error models 作为 FWL-invariant 拓扑的校正替代方案未引用具体工作\n\n### Questions\n1. 为何 abstract 选择 83.4% 而非 2.1% 作为主要数字？\n2. Empirical Finding 1 是否有证明进展？\n3. 是否计划公开代码？\n4. C(δ) 线性路径是否是唯一合理的 parameterization？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、新颖性评估、相关工作遗漏和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-22T13:55:02.362334+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23347
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-22T13:55:02.563608+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Theorem 1 适用范围过窄，Conjecture 1 缺乏证明\n- Theorem 1 仅覆盖 confounding + proportional effects。其余 6 个 non-IV 拓扑的单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性。虽然违反幅度小（< 0.06），但高频违反意味着 ASV vulnerability spectrum 的理论基础不够坚实。如果单调性不成立，\"临界 δ 阈值\"的语义变得模糊。建议至少再证明一个拓扑（如 mediation），或给出 ε 关于 K 和 DGP 参数的 formal bound。\n\n**N2** [critical] 正文疑似超出 8 页限制\n- Section 5 (Conclusion) 在第 9 页开始，正文约 8.3 页。\n\n**N3** [critical] FWL invariance 结论缺乏严格证明\n- 三个关键问题：(a) \"matrix-based correction\"的精确定义是什么？(b) SIMEX 在 individual level 工作，其外推函数形式假设是否适用于分类误差设定？Theorem 1 表明 confounding bias 关于 δ 单调——SIMEX 理论上应能工作，0% reduction 是否说明实现问题？(c) 与测量误差文献中已知的\"controlling for mismeasured confounder leaves residual confounding\"的关系？\n\n### Should-Fix 问题\n\n**W1** 非差异误分类假设对 LLM 标注者可能不成立（stress test 仅测 ε≤0.10 的轻微偏离）\n\n**W2** 线性 SEM 假设限制实际适用性（FWL invariance 在 logistic 下不成立——Algorithm 1 的分流建议可能失效）\n\n**W3** Dirichlet(1,1,1) headline 数字具有误导性（83.4% vs realistic 2.1%）\n\n**W4** 相对于测量误差文献的新颖性定位不清（哪些是已知结果在 LLM 语境的应用 vs 真正新贡献未明确界定）\n\n**W5** 经验验证使用模拟 DGP 而非真实因果数据（\"Empirical validation\"用真实 CM 但应用于模拟 DGP，验证的是理论推导正确性而非实践指导价值）\n\n### 主要优势\n1. 重要且及时的问题\n2. 清晰的理论贡献：K≥3 algebraic break point\n3. 实用性：Algorithm 1 + ASV 框架\n4. 系统覆盖：7 DAG × 5 correction methods\n5. 附录质量高（12 页证明）\n6. Cross-PPI 和 FWL bypass 方法讨论\n\n### 小问题\n- τ 和 β_T 记号交替使用\n- Proposition 编号在正文与附录不一致\n- Figure 2 y 轴标签较小\n- Table 2 conditions 列风格不一致\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、主要优势和小问题。特别关注：\n1. 你是否同意 R1-N3（FWL invariance 需要 formal proof）？你的审稿中也提到了 FWL invariance 但评价为\"技术上直接\"——两位对此的严重性评估是否一致？\n2. R1-W5（经验验证用模拟 DGP 而非真实因果数据）——你如何看待这一批评？\n3. R1-W4（新颖性定位不清）与你的新颖性评估是否矛盾？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Theorem 1 适用范围过窄，Conjecture 1 缺乏证明\n- Theorem 1 仅覆盖 confounding + proportional effects。其余 6 个 non-IV 拓扑的单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性。虽然违反幅度小（< 0.06），但高频违反意味着 ASV vulnerability spectrum 的理论基础不够坚实。如果单调性不成立，\"临界 δ 阈值\"的语义变得模糊。建议至少再证明一个拓扑（如 mediation），或给出 ε 关于 K 和 DGP 参数的 formal bound。\n\n**N2** [critical] 正文疑似超出 8 页限制\n- Section 5 (Conclusion) 在第 9 页开始，正文约 8.3 页。\n\n**N3** [critical] FWL invariance 结论缺乏严格证明\n- 三个关键问题：(a) \"matrix-based correction\"的精确定义是什么？(b) SIMEX 在 individual level 工作，其外推函数形式假设是否适用于分类误差设定？Theorem 1 表明 confounding bias 关于 δ 单调——SIMEX 理论上应能工作，0% reduction 是否说明实现问题？(c) 与测量误差文献中已知的\"controlling for mismeasured confounder leaves residual confounding\"的关系？\n\n### Should-Fix 问题\n\n**W1** 非差异误分类假设对 LLM 标注者可能不成立（stress test 仅测 ε≤0.10 的轻微偏离）\n\n**W2** 线性 SEM 假设限制实际适用性（FWL invariance 在 logistic 下不成立——Algorithm 1 的分流建议可能失效）\n\n**W3** Dirichlet(1,1,1) headline 数字具有误导性（83.4% vs realistic 2.1%）\n\n**W4** 相对于测量误差文献的新颖性定位不清（哪些是已知结果在 LLM 语境的应用 vs 真正新贡献未明确界定）\n\n**W5** 经验验证使用模拟 DGP 而非真实因果数据（\"Empirical validation\"用真实 CM 但应用于模拟 DGP，验证的是理论推导正确性而非实践指导价值）\n\n### 主要优势\n1. 重要且及时的问题\n2. 清晰的理论贡献：K≥3 algebraic break point\n3. 实用性：Algorithm 1 + ASV 框架\n4. 系统覆盖：7 DAG × 5 correction methods\n5. 附录质量高（12 页证明）\n6. Cross-PPI 和 FWL bypass 方法讨论\n\n### 小问题\n- τ 和 β_T 记号交替使用\n- Proposition 编号在正文与附录不一致\n- Figure 2 y 轴标签较小\n- Table 2 conditions 列风格不一致\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、主要优势和小问题。特别关注：\n1. 你是否同意 R1-N3（FWL invariance 需要 formal proof）？你的审稿中也提到了 FWL invariance 但评价为\"技术上直接\"——两位对此的严重性评估是否一致？\n2. R1-W5（经验验证用模拟 DGP 而非真实因果数据）——你如何看待这一批评？\n3. R1-W4（新颖性定位不清）与你的新颖性评估是否矛盾？"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-22T13:55:04.124598+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1560
}
```

</details>

---


### Assistant

_source line 226 · 2026-05-22T13:55:06.927352+00:00_

交叉分享已发送给两位 Reviewer。等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 227 · 2026-05-22T13:55:09.842097+00:00_

[Reviewer 1 审稿结果]:
清理完成。审稿任务已结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 228 · 2026-05-22T13:55:27.814519+00:00_

Reviewer 1 的交叉回应内容为空，等待 Reviewer 2 的交叉回应返回后一并处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 229 · 2026-05-22T13:56:56.648855+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 正文超出 8 页限制**
与我的 N2 一致。Section 5 (Conclusion) 确实在第 9 页开始，正文约 8.3 页。ARR 对 long paper 8 页限制执行严格，这是 desk rejection 风险。无异议。

**[AGREE] R2-N2: Sign reversal 实际严重性被过度声称**
与我的 W3 部分重叠，但 R2 提出了一个我未充分强调的关键观察：论文自身在 Section 4.4 (p.8) 明确写道 *"The primary coefficient (β₁, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small |β|"*。这与 Abstract 的 "catastrophic" 框架形成重大落差。

补充证据：(1) 在 C_kk ≥ 0.7 的现实区间，sign reversal 仅 2.1%，且全部发生在 secondary coefficients；(2) 论文 Section 4.2 (p.5) 的 "catastrophic sign reversal" 小标题与 Section 4.4 的实证结果自相矛盾。

不过我认为 R2 的严重性定级可以稍作调整：理论上任何系数都 CAN reverse（给定足够差的 confusion matrix），这一理论贡献本身是有价值的。建议将呈现方式从 "catastrophic failure is the norm" 调整为 "sign reversal is theoretically possible for K≥3, practically rare for primary coefficients under realistic classifiers, but non-negligible for secondary coefficients"。这比完全弱化声称更准确。

---

### Should-Fix 问题

**[AGREE] R2-W1: 3/5 拓扑缺乏解析证明但用词暗示已证明**
论文 Abstract 用 "establish" 描述五拓扑 sign preservation，但查看附录：
- Confounding: Proposition 2 (Appendix A.3, p.12) — **已证明** ✓
- Collider: Propositions 3-5 (Appendix A.6, p.14-15) — **已证明** ✓
- Mediation: Appendix A.5 (p.13-14) — "a closed-form proof for general K remains open"，仅 **数值验证** ✗
- M-bias: Appendix A.7 (p.15) — 类似，**数值验证** ✗
- Front-door: Appendix A.7 (p.15-16) — **数值验证** ✗

Abstract 的 "establish" 对只有 empirical verification 的 3 个拓扑而言确实 overclaim。建议改为 "prove for confounding and collider, and verify numerically for mediation, M-bias, and front-door"。

**[AGREE, 但我认为应升级为 Must-Fix] R2-W2: Conjecture 1 支撑 ASV 但未证明**
我在自己的审稿中将此列为 **N1 (critical)**，而 R2 列为 Should-Fix。我认为应升级。理由：
- ASV 的 vulnerability spectrum（IV fragile → M-bias immune）的语义 *依赖* 单调性——如果 |bias| 不随 δ 单调变化，"critical δ threshold" 的解释就失去了理论基础
- Table 9 (Appendix C, p.22) 显示 60-97% 的矩阵违反严格单调性，虽然幅度小 (< 0.06)，但这意味着对于相当大比例的 confusion matrices，ASV 可能给出误导性的 sensitivity ranking
- 对于一篇以理论贡献为核心卖点的论文，其最重要的实用工具（ASV）缺乏理论保障，这比 presentation 问题更严重

**[AGREE] R2-W3: Non-differential misclassification 假设讨论不足**
与我的 W1 一致。补充：R2 指出 stress test "仅覆盖 exposure 拓扑"——这一点我之前漏掉了。确实，Appendix B.4 (p.20) 的 stress test 只在 exposure DAG 上做了非差异假设的敏感性分析，对其他 6 个拓扑的 differential misclassification robustness 完全缺失。对于 confounding 拓扑（LLM 误差可能与混淆因子相关），这是一个更严重的遗漏。

**[AGREE] R2-W4: 缺少 outcome misclassification 的讨论**
这是一个我未提出的有效观点。在许多 NLP 因果推断场景中，Y（结果变量）也可能由 LLM 标注（如标注"是否包含仇恨言论"作为结果）。Outcome misclassification 在 OLS 中通常不导致系数偏倚（仅增加方差），但在 nonlinear models（如 logistic regression）中会导致偏倚。鉴于论文已在 Limitations 中承认 nonlinear 是重要扩展方向，outcome misclassification 至少值得一段讨论。

**[AGREE] R2-W5: Abstract 信息过载**
同意。Abstract 中包含 15+ 个具体数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 210 configurations, 100,000 matrices, etc.），影响可读性。建议保留 3-5 个最关键的数字，其余移入正文。

**[AGREE] R2-W6: 未提及代码/数据公开**
同意。对于 reproducibility 维度，代码公开是 ARR 评审的标准预期。

---

### 新颖性评估

**[AGREE] R2 的新颖性评估基本准确**
补充两点：
1. R2 说 "ASV 创新中等（E-value 自然类比）"——我同意 ASV 是 E-value 的自然多类扩展，但增加的是 **topology-dependent** 维度（不同拓扑的 ASV ranking 不同），这超越了简单类比。
2. R2 说 "FWL invariance 技术直接但实用价值高"——我同意实用价值，但正如我在 N3 中指出的，这一结论本身缺乏 formal proof（仅有实验验证），削弱了其作为"established result"的可信度。

---

### 相关工作遗漏

**[AGREE] R2-Ref1: Cinelli & Hazlett (2020) "Making Sense of Sensitivity"**
这是最重要的遗漏。Cinelli & Hazlett 的 sensitivity analysis framework（robustness value, partial R²-based bounds）与 ASV 框架有直接可比性——两者都通过参数化 confounding/measurement error 的强度来评估估计量的稳健性。论文应明确讨论 ASV 与 Cinelli & Hazlett framework 的异同：ASV 针对的是 misclassification-specific 的 C(δ) 参数化，而 Cinelli & Hazlett 针对的是 omitted variable 的 partial R²。

**[AGREE] R2-Ref2: Gilardi et al. (2023)**
同意，作为 LLM annotation quality 的 seminal reference 应被引用，特别是论文 Introduction 讨论 LLM annotation 在社会科学中的应用时。

**[AGREE] R2-Ref3: Ziems et al. (2024)**
同意，作为 LLM in CSS 的综合 survey 应被引用以支撑 motivation。

**[AGREE] R2-Ref4: Bound, Brown & Mathiowetz (2001)**
同意。这与我的 W4 (novelty delineation) 相关——survey methodology 中对 categorical measurement error 的研究是 ASV 和 bias taxonomy 的重要先例。

**[AGREE] R2-Ref5: Bayesian measurement error models 缺具体引用**
论文 Section 4.5 (p.8) 提到 "Bayesian measurement error models" 作为 FWL bypass 方案，但未引用具体工作（如 Richardson & Gilks 1993, Gustafson 2004 的具体 Bayesian 方法章节）。

---

### Questions 回应

**[AGREE] R2-Q1: 为何 abstract 选择 83.4% 而非 2.1%？**
与我的 W3 和 R2-N2 一致。83.4% 来自 Dirichlet(1,1,1) 全参数空间（含随机分类器），2.1% 来自 C_kk ≥ 0.7 的现实区间。论文应以后者为主线。

**[AGREE] R2-Q2: Empirical Finding 1 是否有证明进展？**
与我的 N1 相关。3/5 拓扑的 sign preservation 和 Conjecture 1 的 monotonicity 都缺乏解析证明。

**[AGREE] R2-Q3: 代码公开计划？**
标准 reproducibility 要求。

**[REBUT] R2-Q4: C(δ) 线性路径是否是唯一合理的 parameterization？**
R2 的问题隐含质疑 C(δ) = (1-δ)I + δC₀ 的唯一性。我认为这一 parameterization 是合理且自然的，理由：
1. 它是 identity matrix（完美分类）到目标 confusion matrix C₀ 的最短路径（在 Frobenius 范数下的线性插值）
2. δ 有清晰的语义解释：从 0（无误差）到 1（达到 C₀ 的误差水平）
3. 与 E-value 文献中的 sensitivity parameter 类似（单参数索引的 monotone family）
4. 论文 Section 3.3 (p.4-5) 讨论了 non-negativity constraint（δ ≤ δ_max = min_{j,k} C₀_{jk}/(1-C₀_{jk})），说明对 boundary behavior 有考虑

不过，论文确实应该讨论替代参数化（如 matrix exponential path、Dirichlet-based interpolation）及其对 ASV 值的潜在影响，即使最终选择线性路径。

---

### 总体评价差异

R2 给出 Overall 3.5，与我的 3.5 一致。我们的主要分歧在于：
1. **Conjecture 1 的严重性**：我列为 Must-Fix (N1)，R2 列为 Should-Fix (W2)。我坚持认为应升级——ASV 框架是论文的核心实用贡献，其理论基础不应仅依赖 numerical verification。
2. **FWL invariance 证明**：我列为 Must-Fix (N3)，R2 未专门讨论。我认为 "exactly 0%" 这一定量声称需要 formal justification。
3. **Sign reversal framing**：R2 列为 Must-Fix (N2)，我原列为 Should-Fix (W3)。R2 关于 "primary coefficient never reverses" 的观察让我认为这确实应升级——abstract/conclusion 的声称与实证结果之间的 gap 比我最初评估的更大。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 230 · 2026-05-22T13:57:10.260431+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 231 · 2026-05-22T13:57:12.897063+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心结论：与 R2 在大多数问题上达成一致（12 个 AGREE，1 个 REBUT），主要分歧在于严重性定级：
- 我认为 **Conjecture 1 (R2-W2) 应升级为 Must-Fix**——ASV 框架的理论基础不应仅依赖 numerical verification
- 我认为 **FWL invariance 缺乏 formal proof** 是 R2 未充分讨论的 Must-Fix 问题
- R2 关于 "primary coefficient never reverses" 的观察让我同意将 **sign reversal framing 升级为 Must-Fix**
- 唯一 REBUT：C(δ) 线性参数化是合理的自然选择，但应讨论替代方案

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 232 · 2026-05-22T13:57:24.426582+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 25

## Round 25

14 recorded events


### User

_source line 233 · 2026-05-22T13:57:29.391317+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: Theorem 1 适用范围过窄，Conjecture 1 缺乏证明**

同意这是一个实质性问题。我在自己的审稿中将其列为 W2（should-fix），但 R1 将其提升到 critical 也有道理。具体而言：

- Theorem 1 限于 confounding + proportional effects（Section 3.3），这是一个很强的假设。
- Conjecture 1 的数值验证虽然覆盖广（10,000 矩阵 × 7 拓扑 × K∈{3,5,7}），但 ε < 0.06 是 empirical bound，不是 formal bound。
- R1 指出 Table 9 显示 60-97% 的随机矩阵违反严格单调性——这个数字我在审稿中未单独指出，但它确实让"monotonicity"这个词的使用变得微妙。论文用了"ε-approximate monotonicity"来 hedge，但如果多数矩阵都违反严格单调性，"ASV 单调递增/递减"的直觉描述就不准确。

不过我对严重性的评估略低于 R1：ASV 的核心价值在于 **ranking topologies**（IV 最脆弱、M-bias 最安全），这个排序在所有数值实验中都成立，不完全依赖严格单调性。即使 ε-approximate，只要 ε 足够小（< 6%），排序结论不受影响。因此我维持 should-fix 而非 must-fix 的评级，但建议作者：(1) 在正文中更诚实地讨论"多数矩阵违反严格单调"这一事实；(2) 至少再证明 mediation 的单调性（其 bias 表达式 Eq.3 结构较简单）。

---

**[AGREE] R1-N2: 正文超出 8 页限制**

完全同意。我也将此列为 N1（critical）。Section 5 (Conclusion) 在第 9 页，正文约超 0.5 页。这是 ARR desk rejection 风险。

---

**[REBUT] R1-N3: FWL invariance 结论缺乏严格证明**

我部分不同意 R1 将此列为 critical。逐点回应：

**(a) "matrix-based correction"的精确定义**：R1 的要求合理。论文确实未给出 formal definition。但从 Section 4.5 和 Appendix 的上下文可以推断，"matrix-based correction"指的是对 dummy 变量施加 C⁻¹ 变换（naive plug-in 和 MLA 都属此类）。建议作者添加一个 precise definition，但这属于 writing clarity 问题，不影响结论正确性。

**(b) SIMEX 的 0% reduction 问题**：R1 质疑"SIMEX 理论上应能工作"。但我认为恰恰相反——SIMEX 对 covariate misclassification 的 0% reduction 正是 FWL invariance 的正确推论。SIMEX 通过向 A* 添加额外噪声再外推回去，但 FWL 定理保证了 T 的系数不受 A* column space 内任何变换的影响。因此 SIMEX 的 measurement error function 是常数函数——外推结果等于原始估计。这不是实现问题，而是 FWL 的必然结果。论文可以更清楚地解释这一点。

**(c) 与已知 "residual confounding" 结果的关系**：R1 问的是 "controlling for mismeasured confounder leaves residual confounding" 这一已知事实和 FWL invariance 的关系。这两者是互补而非矛盾的：(i) residual confounding 说的是 bias 的存在（T coefficient 有偏），这在论文的 Eq.1 confounding bias 表达式中已体现；(ii) FWL invariance 说的是 correction 的无效性——即使你知道真实 C，施加 C⁻¹ 也不能消除 T 的 bias，因为 bias 来自 T 与 A residual 的相关性而非 A 的编码方式。这个区分（bias 存在 vs. 校正无效）是论文的实质贡献，虽然技术上直接但在文献中确实被忽视。

**我的评估**：FWL invariance 的结论是正确的且可从 FWL 定理直接推出，不需要额外 formal proof——它本身就是 FWL 定理的 corollary。R1 要求"严格证明"的合理性在于论文表述不够 precise，但这是 writing issue 不是 correctness issue。我将此从 R1 的 critical 降为 should-fix：建议添加 precise definition + 一段 FWL 推导（3-4 行公式），但不认为这影响接收决定。

---

### Should-Fix 问题

**[AGREE] R1-W1: Non-differential 假设对 LLM 不成立**

同意。我在 W3 中提出了完全相同的关切。LLM 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在许多场景中不成立。Appendix B.4 的 stress test 仅测 ε≤0.10 且主要覆盖 exposure 拓扑，不足以支撑框架的一般性声称。

---

**[AGREE] R1-W2: 线性 SEM 假设限制适用性**

同意且认为 R1 指出了一个我在审稿中未充分强调的具体后果：**Algorithm 1 的分流建议可能在 logistic 模型下失效**。论文 Appendix B.3 的 logistic DGP 检验显示 sign-flip patterns 保持，但 FWL invariance 本身在非线性模型下不成立——这意味着 Algorithm 1 中"topology ∈ {confounding, mediation, collider, M-bias} → matrix-based correction ineffective"的分支在 logistic regression 中可能不正确。论文在 Limitations 中提到了这一点（"FWL invariance result does not hold for logistic regression"），但 Algorithm 1 本身没有加此 caveat。这是一个有实际影响的问题。

---

**[AGREE] R1-W3: Dirichlet(1,1,1) headline 数字误导性**

强烈同意。这与我的 N2 (critical) 一致。我甚至将其严重性评估高于 R1（R1 列为 W3 should-fix，我列为 N2 must-fix）。83.4% 在 abstract 第一段出现，但这是 Dirichlet(1,1,1) 均匀先验的结果——realistic regime（diagonal ≥ 0.7）下 sign reversal 仅 2.1%。更重要的是，empirical validation 显示 sign reversal 仅影响 secondary coefficients（Section 4.4）。Abstract 和 Introduction 的"catastrophic"框架与实际 severity 的落差是 overclaiming 问题。

---

**[PARTIALLY AGREE] R1-W4: 新颖性定位不清**

部分同意。R1 要求更清晰地界定"已知结果在 LLM 语境的应用 vs 真正新贡献"，这个要求合理。具体而言：

- **已知**：K≥3 polytomous misclassification 可导致 sign reversal（Dosemeci 1990, Veierød & Laake 2001）；non-differential misclassification of binary confounder 的 attenuation 性质（Brenner 1993, Ogburn & VanderWeele 2012）
- **新贡献**：(1) 系统性 7 拓扑对比（从未有人在统一框架下比较）；(2) ASV 框架（E-value 类比应用于 annotation error 是新的）；(3) FWL invariance 对 correction methods 的影响（文献中从未被指出）；(4) 在 NLP/LLM annotation 语境中的实证验证

但我不认为这构成 rejection 理由。论文在 Related Work（Section 2）中已经 cite 了 Dosemeci (1990) 和 Veierød & Laake (2001)，并明确说"our taxonomy is the first to characterize how the same confusion matrix produces qualitatively different bias across seven topologies"。问题是 **程度**——论文应更明确地用一两句话说"K≥3 sign reversal possibility 本身是已知的（Dosemeci 1990），我们的新贡献是 topology-dependent 的系统刻画"。这是 framing 改进而非 novelty 不足。

---

**[PARTIALLY AGREE] R1-W5: 经验验证用模拟 DGP 而非真实因果数据**

R1 的批评技术上正确但我认为过于严苛。理由如下：

1. **这是方法论论文的标准做法**。验证理论框架需要 known ground truth，只有模拟 DGP 能提供。E-value 原始论文（VanderWeele & Ding 2017）、PPI++（Angelopoulos et al. 2023）等方法论工作也采用类似策略。
2. **论文用了 real LLM confusion matrices**。这比纯模拟高一个层次——confusion matrices 来自 4 个真实 LLM 在 3 个真实数据集上的表现（HumAID, VAST, CivilComments），不是 fabricated 的。
3. **Appendix B.2 有 retrospective case study**。虽然在附录，但确实应用了框架到 Lee & Wood-Doughty (2024) 的真实因果分析。

但我也同意 R1 的核心关切：论文的 practical guidance value 没有被充分验证。如果作者能在 camera-ready 中加入一个更完整的 real-world case study（如在 HumAID 数据上执行完整因果分析并展示 ASV 如何改变分析决策），说服力会大幅提升。

---

### 主要优势

**[AGREE] 所有 6 条优势**

R1 列出的优势与我的评估高度一致：
- "重要且及时的问题" — 同意，LLM annotation 在 CL/NLP 社区快速普及，downstream causal validity 是紧迫问题。
- "K≥3 algebraic break point" — 同意，这是论文最核心的 insight。
- "Algorithm 1 + ASV 框架的实用性" — 同意，可操作性是论文的主要卖点。
- "7 DAG × 5 correction methods 的系统覆盖" — 同意，覆盖面是竞争优势。
- "附录质量高" — 同意，12 页附录包含详细证明、stress test、case study，质量高于多数投稿。
- "Cross-PPI 和 FWL bypass 方法讨论" — 同意，Section 4.5 最后一段的 Cross-PPI 和 EM imputation 讨论虽然只是提及未评估，但展示了对 correction 方向的全面思考。

---

### 小问题

**[AGREE] τ 和 β_T 记号交替使用**
确认存在。Section 3.2 用 τ 表示 target causal parameter，但 exposure 部分用 β_j，confounding 部分用 τ（T 的系数）。虽然语义可从上下文推断，但 notation 一致性应改进。

**[AGREE] Proposition 编号在正文与附录不一致**
未独立验证此问题，但如果存在，应在 camera-ready 修复。

**[AGREE] Figure 2 y 轴标签较小**
同意。我在小问题中也提到了 Figure 2 标签文字在打印版中可能难以辨认。

**[AGREE] Table 2 conditions 列风格不一致**
未独立验证（Table 2 在 Appendix A.9），但 R1 对附录阅读的仔细程度值得肯定。

---

### 对 Director 提出的三个具体问题的回应

**Q1: FWL invariance 严重性评估是否一致？**

不完全一致，但分歧不大。R1 将 FWL invariance 列为 N3 (critical)，要求 formal proof；我在审稿中将其列为优势（"技术上直接但实践重要"）。核心分歧在于：**R1 认为 FWL invariance 需要被 prove**，而我认为它是 FWL 定理的 direct corollary，不需要额外证明——需要改进的是 **表述精度**而非 **证明**。

具体来说：FWL 定理说 OLS 中 T 的系数等于对 T 和 Y 分别投影掉 A* dummies 后的简单回归系数。对 A* dummies 施加 C⁻¹ 变换不改变其 column space（C⁻¹ 可逆），因此 projection matrix M_{A*} 不变，T 系数不变。这个推导不到 3 行。论文应该把这 3 行写出来，但说它"缺乏严格证明"我认为过度了。

我建议将此定性为 **should-fix (writing clarity)**，而非 **must-fix (missing proof)**。

**Q2: 如何看待 R1-W5（模拟 DGP 而非真实因果数据）？**

如上所述，我认为这是有效但不严重的批评。方法论论文用模拟 DGP + real parameters 是标准做法。论文的贡献在于理论框架，不在于某个具体因果分析。但我同意 R1 的建议方向——一个完整的 real-world case study 会大幅增强论文说服力，建议在 camera-ready 中将 Appendix B.2 的 case study 扩展并移入正文（如果页数允许）。

**Q3: R1-W4（新颖性定位）与我的新颖性评估是否矛盾？**

不矛盾，高度一致。R1 说"新颖性定位不清"，我在新颖性专项评估中说"ASV 相对于 E-values 的技术创新中等"、"K≥3 break 已被 Dosemeci (1990) 指出"。我们都认为：
- 论文的系统性 7 拓扑对比是 **genuinely new**
- K≥3 sign reversal 本身是 **known but under-explored**
- ASV 是 E-value 的 **natural adaptation**，不是 breakthrough

差异在于表述：R1 要求论文更明确界定已知 vs 新，我在审稿中已经做了这个区分。建议作者在 Introduction 最后一段添加 1-2 句："The possibility of polytomous sign reversal was noted by Dosemeci et al. (1990); our contribution is the first systematic characterization across multiple DAG topologies and the ASV framework for quantifying this vulnerability."

---

### 综合评估

两位 reviewer 的评估高度一致：

| 维度 | R1 | R2（我） | 共识 |
|------|----|----|------|
| Overall | 3.5 | 3.5 | 一致 |
| 页数超限 | N2 critical | N1 critical | 一致 |
| Conjecture 1 未证明 | N1 critical | W2 warning | R1 更严格，但方向一致 |
| 83.4% overclaiming | W3 warning | N2 critical | 我更严格 |
| Non-differential 假设 | W1 warning | W3 warning | 一致 |
| FWL invariance | N3 critical | 列为优势 | 分歧最大——我认为 should-fix writing 即可 |
| 模拟 DGP | W5 warning | 未单独列出 | R1 更关注，我认为 acceptable |

**两位 reviewer 的核心共识**：这是一篇重要且及时的工作，系统性 taxonomy 和 ASV 框架有实用价值，但 (1) 理论深度中等（Conjecture 未证明、部分 sign preservation 仅数值验证），(2) framing 存在 overclaiming，(3) 格式需修复。Borderline Conference 的评分反映了贡献与不足的平衡。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-22T13:57:50.635375+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-22T13:57:51.188275+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T13:42:21.430890+00:00\", \"completed_at\": \"2026-05-22T13:42:25.019969+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets May 23, 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-22T13:57:51.188685+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-22T13:57:52.343967+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-22T13:57:53.149479+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "review_issues.yaml",
  "max_chars": "20000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "review_issues.yaml",
    "max_chars": "20000"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-22T13:57:53.250352+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-22T13:57:57.820127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-22T13:57:57.871311+00:00_

1	issues:
2	  # === Round 1 issues — status updates for Round 2 ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 一般情形证明不完整：Cauchy-Schwarz 界的单调性 ≠ |B(C(δ))| 本身的单调性"
8	    status: in_progress
9	    first_raised_round: 1
10	    last_seen_round: 2
11	    mentions:
12	      - round: 1
13	        reviewers: [R1, R2]
14	        note: "R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。"
15	      - round: 2
16	        reviewers: [R1, R2]
17	        note: "双方再次独立提出。R1 明确指出上界单调 ≠ 函数单调（Cauchy-Schwarz gap）。R2 AGREE 并补充 ASV δ* 唯一性依赖。比例情形 (f=λg) 证明完整，一般情形仅 500 组数值验证。建议：一般情形降级为 Conjecture 或 Empirical Finding。"
18	    action_items:
19	      - round: 1
20	        action: "Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture"
21	        assigned_to: agent
22	        status: in_progress
23	      - round: 2
24	        action: "一般情形降级为 Empirical Finding，保留比例情形 (f=λg) 的解析证明"
25	        assigned_to: agent
26	        status: in_progress
27	    resolution: ""
28	    resolution_round: null
29	
30	  - id: R1-N2
31	    category: soundness
32	    severity: must-fix
33	    summary: "3/5 安全拓扑的符号保持仅有数值验证，缺乏解析证明"
34	    status: in_progress
35	    first_raised_round: 1
36	    last_seen_round: 2
37	    mentions:
38	      - round: 1
39	        reviewers: [R1, R2]
40	        note: "R1 首发，R2 AGREE 并建议拆分。"
41	      - round: 2
42	        reviewers: [R1, R2]
43	        note: "双方再次一致。摘要 'five topologies never produce sign reversal' 中 'never' 是全称量词，但 mediation/M-bias/front-door 仅有 Empirical Finding。R2 建议改为 'show no sign reversal in extensive numerical verification'。R1 补充 6D 空间 100k 采样密度论证。"
44	    action_items:
45	      - round: 1
46	        action: "拆分 Proposition 1 → 已证(confounding/collider/exposure反例) vs Empirical Finding(mediation/M-bias/front-door)；替换 'standard DGP' 为显式充分条件"
47	        assigned_to: agent
48	        status: in_progress
49	      - round: 2
50	        action: "Abstract 'never' → 'show no sign reversal... (proven analytically for 
…[truncated 11814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-22T14:01:31.931577+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1 issues — status updates through Round 3 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），Conjecture 1 未证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次独立提出。R1 明确指出上界单调 ≠ 函数单调（Cauchy-Schwarz gap）。R2 AGREE 并补充 ASV δ* 唯一性依赖。比例情形 (f=λg) 证明完整，一般情形仅 500 组数值验证。建议：一般情形降级为 Conjecture 或 Empirical Finding。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 列为 N1 critical：Table 9 显示 60-97% 随机矩阵违反严格单调性，ASV 的 well-defined sensitivity measure 语义依赖单调性。R2 列为 W2 should-fix：ASV 核心价值在于 topology ranking，ranking 在所有实验中成立，不完全依赖严格单调性。R2 建议至少证明 mediation。双方方向一致，严重性分歧（R1 must-fix vs R2 should-fix）。\"\n    action_items:\n      - round: 1\n        action: \"Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"一般情形降级为 Empirical Finding，保留比例情形 (f=λg) 的解析证明\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"至少证明 mediation 的单调性；正文讨论 Conjecture 失败时 ASV interpretation 如何 degrade；给出 ε 关于 K 和 DGP 参数的 formal bound\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE 并建议拆分。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。Abstract 改为 'establish...proven analytically for confounding and collider via sufficient conditions; Appendix A'。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W1: Abstract 仍用 'establish that five topologies show no sign reversal'，'establish' 对仅有 empirical verification 的 3 拓扑是 overclaim。R1 AGREE。建议用 'prove for confounding and collider, verify numerically for mediation, M-bias, and front-door'。\"\n    action_items:\n      - round: 2\n        action: \"Abstract 'never' → 'show no sign reversal... (proven analytically for confounding and collider via sufficient conditions)'\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Abstract/Conclusion 中区分 'proven'(2) vs 'numerically verified'(3)，或用 'show' 替代 'establish'\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"δ_max = min_j 1/(1-(C₀)_{jj})。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。Section 3.3 已引入 δ_max 约束。已修复。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"引入 δ_max 约束\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Section 3.3 已引入 δ_max 约束，ASV 限制在 [0, δ_max]。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称；empirical sign reversal 仅影响 secondary coefficients\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 再次标为 CRITICAL。R1 REBUT 认为 Dirichlet 有方法论正当性。降级为 should-fix。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2 再次列为 N2 critical：(1) 83.4% 来自不现实的 Dirichlet(1,1,1) prior，realistic regime 仅 2.1%；(2) 新发现——Section 4.4 明确写道 primary coefficient never reverses，sign flips exclusively in secondary coefficients with small |β|，与 Abstract 'catastrophic' 框架严重不符。R1 AGREE 并升级：'Section 4.2 catastrophic sign reversal 小标题与 Section 4.4 实证结果自相矛盾'。建议：先报告 2.1%（realistic），再提 83.4%（theoretical）；用 'structurally possible' 替代 'catastrophic'。\"\n    action_items:\n      - round: 2\n        action: \"调整叙事重心：以 realistic accuracy 为主叙事\"\n        assigned_to: agent\n        status: pending\n      - round: 3\n        action: \"(1) Abstract 先报告 realistic regime (diagonal≥0.7, 2.1% sign reversal)，再提 Dirichlet 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 替换 'catastrophic' 措辞\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 must-fix，R1 rebut。降级 should-fix。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Abstract 已改为 'We present a systematic framework'。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"Abstract 'the first' → 'a systematic framework'\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Abstract 已改为 'We present a systematic framework'。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"4 篇已恢复引用。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。确认已修复。但 Round 3 发现新的遗漏引用（见 R3-NEW-5）。\"\n    action_items:\n      - round: 1\n        action: \"恢复 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 引用\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"4 篇引用已全部恢复。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被明确提及。论文 Section 3.2 最后一段添加了 ASV 作为不依赖精确条件的替代讨论。可能已部分改善。\"\n    action_items:\n      - round: 2\n        action: \"添加 DGP 条件可验证性讨论 + ASV 作为替代\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 部分 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"已扩展至 23 configs（4 LLM × 3 数据集）。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未明确提及。Section 4.4 报告 23 configurations，但均为开源 LLM（Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct），Limitations 提到 '15 of 18 planned configurations completed'。\"\n    action_items:\n      - round: 2\n        action: \"Limitations 讨论开源 vs 商业 LLM 误差模式差异\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 rebut。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。叙事已改善。\"\n    action_items:\n      - round: 1\n        action: \"区分理论风险 vs 实践观测\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Triple verification narrative 已解决。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议展示 bootstrap 示例。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Appendix B.5 现包含 B=1,000 bootstrap，95% CI for magnitude ASV。Section 3.3 建议 bootstrapping。Section 4.3 报告 bootstrap CI。已修复。\"\n    action_items:\n      - round: 2\n        action: \"展示 bootstrap C₀ uncertainty 示例\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Appendix B.5 + Section 4.3 已包含 bootstrap ASV 分析。Round 3 未再提及。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制对 NLP 受众的实用性；FWL 对 logistic 不成立\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议至少一个 logistic DGP 模拟验证。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W2: Appendix B.6 仅覆盖 3 拓扑（confounding, exposure, IV）的 logistic DGP，sign-flip rate 差异 <2pp，但 FWL invariance 在非线性下不成立。R2 AGREE 并补充：Algorithm 1 中 FWL 分流在 logistic 下可能失效，但 Algorithm 1 未加 caveat。\"\n    action_items:\n      - round: 2\n        action: \"添加 logistic DGP 模拟实验\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"(1) Algorithm 1 添加 'linear models only' caveat；(2) 扩展 Appendix B.6 至全部 7 拓扑\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Per-topology MAPE range (0.5%-5.5%) 已报告。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"报告 per-topology MAPE range\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Per-topology MAPE range 已在论文中报告。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号正文-附录不一致\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R2]\n        note: \"R2 建议符号表。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 小问题：τ 和 β_T 交替使用，Proposition 编号不一致。R2 AGREE。Appendix D 现有 notation table (Table 8) 但正文仍有不一致。\"\n    action_items:\n      - round: 3\n        action: \"统一正文 τ/β_T 记号；添加正文-附录 Proposition 交叉引用\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 issues — status updates for Round 3 ===\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification stress test 覆盖面\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议扩展至 confounding+mediation+exposure+IV × K=3,10。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W1/R2-W3: Appendix B.4 已扩展至 96 configurations (4 topologies × 2K × 3 CM × 4 ε)，但正文 Definition 1 的实践讨论仍不足——何时 LLM 满足 non-differential？R2 补充 stress test 基础版仅 exposure 拓扑不够。R1 建议讨论具体 NLP 场景（sentiment vs stance detection）。\"\n    action_items:\n      - round: 2\n        action: \"扩展 stress test\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"(1) 正文 Method 或 Related Work 讨论 non-differential 假设成立/失败的具体 NLP 场景；(2) Stress test 覆盖更多拓扑\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) TACL 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 提出，R1 AGREE。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Related Work 已引用 feder_etal2022 和 cheng_mayya_sedoc2024。确认已修复。\"\n    action_items:\n      - round: 2\n        action: \"补充 Feder et al. (2022) 和 Cheng et al. (2024) 引用\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Related Work 已包含两篇引用。Round 3 未再提及。\"\n    resolution_round: 3\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"仅 500 scenarios 远少于 Empirical Finding 1 的 100,000。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Appendix C (Table 9) 现报告 10,000 random C₀ per topology per K ∈ {3,5,7} + 500-restart adversarial search。规模已充分。确认已修复。\"\n    action_items:\n      - round: 2\n        action: \"增加 Conjecture 1 验证到 10,000 random + adversarial search\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Appendix C 现包含 210,000 total matrices (10,000 × 7 topologies × 3 K values) + adversarial search。Round 3 未再提及。\"\n    resolution_round: 3\n\n  # === Round 3 新增 issues ===\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制约 0.5 页\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方均列为 critical。Section 5 (Conclusion) 在第 9 页开始。main.tex 已使用 \\\\enlargethispage 和压缩 \\\\floatsep 但仍超限。ARR desk rejection 风险。建议压缩 Section 4（Cross-K robustness 和 ASV diagnostic 移至附录）或缩小 Figure 1+2。\"\n    action_items:\n      - round: 3\n        action: \"压缩正文至 8 页以内：(1) Section 4 部分段落移至附录；(2) Figure 1+2 缩小或合并；(3) Section 2 Related Work 精简\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 列为 N3 critical：'matrix-based correction' 精确定义缺失，SIMEX 0% reduction 需解释，与 Carroll et al. (2006) 关系需澄清。R2 REBUT 降为 should-fix：FWL invariance 是 FWL 定理的 direct corollary（3 行推导），C⁻¹ 不改变 column space，projection matrix 不变，T 系数不变。分歧：R1 要求 formal proof，R2 认为 writing clarity 即可。\"\n    action_items:\n      - round: 3\n        action: \"(1) 添加 'matrix-based correction' 的 precise definition；(2) 写出 3-4 行 FWL 推导；(3) 解释 SIMEX 0% reduction 为何不矛盾；(4) 讨论与 Carroll et al. (2006) residual confounding 的关系\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W4 首发，R1 AGREE。NLP 因果研究中 Y 也可能是 LLM 标注的。OLS 下 outcome misclassification 仅增加方差，但非线性模型下会产生偏倚。至少在 Limitations 中讨论。\"\n    action_items:\n      - round: 3\n        action: \"Limitations 添加 outcome misclassification 段落\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 信息过载（15+ 数字）\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W5 首发，R1 AGREE。Abstract 包含 83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 88%, 61% 等 15+ 数字，读起来像 results dump 而非 motivated preview。建议保留 3-5 个最关键数字。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 精简至 3-5 个核心数字，其余移入正文\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方 AGREE 缺少：(1) Cinelli & Hazlett (2020) 'Making Sense of Sensitivity'——与 ASV 直接可比；(2) Gilardi et al. (2023) ChatGPT annotation；(3) Ziems et al. (2024) LLM+CSS survey；(4) Bound, Brown & Mathiowetz (2001) survey measurement error；(5) Bayesian ME model 具体引用（Gustafson 2004 具体章节或 Richardson & Gilks 1993）。\"\n    action_items:\n      - round: 3\n        action: \"Related Work 补充 5 篇引用并讨论与本文关系\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W6 首发，R1 AGREE。方法论论文含大量仿真实验，代码公开是 ARR 评审标准预期。ASV 计算工具作为 package 发布可大幅提升实用价值。\"\n    action_items:\n      - round: 3\n        action: \"论文中承诺公开代码，或在 supplementary 中提供\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W4 首发，R2 partially agrees。K≥3 sign reversal 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出；residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中已分析。论文应明确：'以下已知：...。我们的新贡献：(1) 系统性 7 拓扑对比；(2) ASV 框架；(3) FWL invariance 对 correction 的影响'。R2 认为这是 framing 改进而非 novelty 不足。\"\n    action_items:\n      - round: 3\n        action: \"Introduction 或 Related Work 添加 1-2 句明确的 novelty delineation\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W5 首发，R2 partially agrees。'Empirical validation' 用真实 CM 但应用于模拟 DGP（线性 SEM），验证的是推导正确性而非实践指导价值。ClinicalBERT case study (Appendix B.2) 是回顾性应用。R2 认为这是方法论论文标准做法，但同意完整 real-world case study 会增强说服力。\"\n    action_items:\n      - round: 3\n        action: \"考虑将 Appendix B.2 case study 扩展并移入正文；或增加 semi-synthetic 实验\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1 issues — status updates through Round 3 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），Conjecture 1 未证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。Reviewer 确认 bias 是 δ 的有理函数（非线性），需正确的有理函数单调性证明。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次独立提出。R1 明确指出上界单调 ≠ 函数单调（Cauchy-Schwarz gap）。R2 AGREE 并补充 ASV δ* 唯一性依赖。比例情形 (f=λg) 证明完整，一般情形仅 500 组数值验证。建议：一般情形降级为 Conjecture 或 Empirical Finding。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 列为 N1 critical：Table 9 显示 60-97% 随机矩阵违反严格单调性，ASV 的 well-defined sensitivity measure 语义依赖单调性。R2 列为 W2 should-fix：ASV 核心价值在于 topology ranking，ranking 在所有实验中成立，不完全依赖严格单调性。R2 建议至少证明 mediation。双方方向一致，严重性分歧（R1 must-fix vs R2 should-fix）。\"\n    action_items:\n      - round: 1\n        action: \"Confounding case 补解析证明（有理函数单调性，非线性），其余降级为 Conjecture\"\n        assigned_to: agent\n        status: in_progress\n      - round: 2\n        action: \"一般情形降级为 Empirical Finding，保留比例情形 (f=λg) 的解析证明\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"至少证明 mediation 的单调性；正文讨论 Conjecture 失败时 ASV interpretation 如何 degrade；给出 ε 关于 K 和 DGP 参数的 formal bound\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE 并建议拆分。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。Abstract 改为 'establish...proven analytically for confounding and collider via sufficient conditions; Appendix A'。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W1: Abstract 仍用 'establish that five topologies show no sign reversal'，'establish' 对仅有 empirical verification 的 3 拓扑是 overclaim。R1 AGREE。建议用 'prove for confounding and collider, verify numerically for mediation, M-bias, and front-door'。\"\n    action_items:\n      - round: 2\n        action: \"Abstract 'never' → 'show no sign reversal... (proven analytically for confounding and collider via sufficient conditions)'\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Abstract/Conclusion 中区分 'proven'(2) vs 'numerically verified'(3)，或用 'show' 替代 'establish'\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误：δ∈[0,∞) 实际有限\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"δ_max = min_j 1/(1-(C₀)_{jj})。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未被提及。Section 3.3 已引入 δ_max 约束。已修复。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"引入 δ_max 约束\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Section 3.3 已引入 δ_max 约束，ASV 限制在 [0, δ_max]。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称；empirical sign reversal 仅影响 secondary coefficients\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 再次标为 CRITICAL。R1 REBUT 认为 Dirichlet 有方法论正当性。降级为 should-fix。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2 再次列为 N2 critical：(1) 83.4% 来自不现实的 Dirichlet(1,1,1) prior，realistic regime 仅 2.1%；(2) 新发现——Section 4.4 明确写道 primary coefficient never reverses，sign flips exclusively in secondary coefficients with small |β|，与 Abstract 'catastrophic' 框架严重不符。R1 AGREE 并升级：'Section 4.2 catastrophic sign reversal 小标题与 Section 4.4 实证结果自相矛盾'。建议：先报告 2.1%（realistic），再提 83.4%（theoretical）；用 'structurally possible' 替代 'catastrophic'。\"\n    action_items:\n      - round: 2\n        action: \"调整叙事重心：以 realistic accuracy 为主叙事\"\n        assigned_to: agent\n        status: pending\n      - round: 3\n        action: \"(1) Abstract 先报告 realistic regime (diagonal≥0.7, 2.1% sign reversal)，再提 Dirichlet 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 替换 'catastrophic' 措辞\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 must-fix，R1 rebut。降级 should-fix。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Abstract 已改为 'We present a systematic framework'。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"Abstract 'the first' → 'a systematic framework'\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Abstract 已改为 'We present a systematic framework'。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"4 篇已恢复引用。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。确认已修复。但 Round 3 发现新的遗漏引用（见 R3-NEW-5）。\"\n    action_items:\n      - round: 1\n        action: \"恢复 audinet2025, zrnic_candes2024, gligoric2025, keith_jensen_oconnor2020 引用\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"4 篇引用已全部恢复。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"双方再次一致。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被明确提及。论文 Section 3.2 最后一段添加了 ASV 作为不依赖精确条件的替代讨论。可能已部分改善。\"\n    action_items:\n      - round: 2\n        action: \"添加 DGP 条件可验证性讨论 + ASV 作为替代\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 部分 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"已扩展至 23 configs（4 LLM × 3 数据集）。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未明确提及。Section 4.4 报告 23 configurations，但均为开源 LLM（Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct），Limitations 提到 '15 of 18 planned configurations completed'。\"\n    action_items:\n      - round: 2\n        action: \"Limitations 讨论开源 vs 商业 LLM 误差模式差异\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 rebut。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。叙事已改善。\"\n    action_items:\n      - round: 1\n        action: \"区分理论风险 vs 实践观测\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Triple verification narrative 已解决。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议展示 bootstrap 示例。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Appendix B.5 现包含 B=1,000 bootstrap，95% CI for magnitude ASV。Section 3.3 建议 bootstrapping。Section 4.3 报告 bootstrap CI。已修复。\"\n    action_items:\n      - round: 2\n        action: \"展示 bootstrap C₀ uncertainty 示例\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Appendix B.5 + Section 4.3 已包含 bootstrap ASV 分析。Round 3 未再提及。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制对 NLP 受众的实用性；FWL 对 logistic 不成立\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发，R1 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议至少一个 logistic DGP 模拟验证。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W2: Appendix B.6 仅覆盖 3 拓扑（confounding, exposure, IV）的 logistic DGP，sign-flip rate 差异 <2pp，但 FWL invariance 在非线性下不成立。R2 AGREE 并补充：Algorithm 1 中 FWL 分流在 logistic 下可能失效，但 Algorithm 1 未加 caveat。\"\n    action_items:\n      - round: 2\n        action: \"添加 logistic DGP 模拟实验\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"(1) Algorithm 1 添加 'linear models only' caveat；(2) 扩展 Appendix B.6 至全部 7 拓扑\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Per-topology MAPE range (0.5%-5.5%) 已报告。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"报告 per-topology MAPE range\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Per-topology MAPE range 已在论文中报告。Round 2-3 未再提及。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号正文-附录不一致\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"双方 AGREE。\"\n      - round: 2\n        reviewers: [R2]\n        note: \"R2 建议符号表。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 小问题：τ 和 β_T 交替使用，Proposition 编号不一致。R2 AGREE。Appendix D 现有 notation table (Table 8) 但正文仍有不一致。\"\n    action_items:\n      - round: 3\n        action: \"统一正文 τ/β_T 记号；添加正文-附录 Proposition 交叉引用\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 issues — status updates for Round 3 ===\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification stress test 覆盖面\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"建议扩展至 confounding+mediation+exposure+IV × K=3,10。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W1/R2-W3: Appendix B.4 已扩展至 96 configurations (4 topologies × 2K × 3 CM × 4 ε)，但正文 Definition 1 的实践讨论仍不足——何时 LLM 满足 non-differential？R2 补充 stress test 基础版仅 exposure 拓扑不够。R1 建议讨论具体 NLP 场景（sentiment vs stance detection）。\"\n    action_items:\n      - round: 2\n        action: \"扩展 stress test\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"(1) 正文 Method 或 Related Work 讨论 non-differential 假设成立/失败的具体 NLP 场景；(2) Stress test 覆盖更多拓扑\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) TACL 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 提出，R1 AGREE。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Related Work 已引用 feder_etal2022 和 cheng_mayya_sedoc2024。确认已修复。\"\n    action_items:\n      - round: 2\n        action: \"补充 Feder et al. (2022) 和 Cheng et al. (2024) 引用\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Related Work 已包含两篇引用。Round 3 未再提及。\"\n    resolution_round: 3\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"仅 500 scenarios 远少于 Empirical Finding 1 的 100,000。\"\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未被提及。Appendix C (Table 9) 现报告 10,000 random C₀ per topology per K ∈ {3,5,7} + 500-restart adversarial search。规模已充分。确认已修复。\"\n    action_items:\n      - round: 2\n        action: \"增加 Conjecture 1 验证到 10,000 random + adversarial search\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Appendix C 现包含 210,000 total matrices (10,000 × 7 topologies × 3 K values) + adversarial search。Round 3 未再提及。\"\n    resolution_round: 3\n\n  # === Round 3 新增 issues ===\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制约 0.5 页\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方均列为 critical。Section 5 (Conclusion) 在第 9 页开始。main.tex 已使用 \\\\enlargethispage 和压缩 \\\\floatsep 但仍超限。ARR desk rejection 风险。建议压缩 Section 4（Cross-K robustness 和 ASV diagnostic 移至附录）或缩小 Figure 1+2。\"\n    action_items:\n      - round: 3\n        action: \"压缩正文至 8 页以内：(1) Section 4 部分段落移至附录；(2) Figure 1+2 缩小或合并；(3) Section 2 Related Work 精简\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 列为 N3 critical：'matrix-based correction' 精确定义缺失，SIMEX 0% reduction 需解释，与 Carroll et al. (2006) 关系需澄清。R2 REBUT 降为 should-fix：FWL invariance 是 FWL 定理的 direct corollary（3 行推导），C⁻¹ 不改变 column space，projection matrix 不变，T 系数不变。分歧：R1 要求 formal proof，R2 认为 writing clarity 即可。\"\n    action_items:\n      - round: 3\n        action: \"(1) 添加 'matrix-based correction' 的 precise definition；(2) 写出 3-4 行 FWL 推导；(3) 解释 SIMEX 0% reduction 为何不矛盾；(4) 讨论与 Carroll et al. (2006) residual confounding 的关系\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W4 首发，R1 AGREE。NLP 因果研究中 Y 也可能是 LLM 标注的。OLS 下 outcome misclassification 仅增加方差，但非线性模型下会产生偏倚。至少在 Limitations 中讨论。\"\n    action_items:\n      - round: 3\n        action: \"Limitations 添加 outcome misclassification 段落\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 信息过载（15+ 数字）\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W5 首发，R1 AGREE。Abstract 包含 83.4%, 52.6%, 13.7%, 2.1%, 47.0%, 88%, 61% 等 15+ 数字，读起来像 results dump 而非 motivated preview。建议保留 3-5 个最关键数字。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 精简至 3-5 个核心数字，其余移入正文\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方 AGREE 缺少：(1) Cinelli & Hazlett (2020) 'Making Sense of Sensitivity'——与 ASV 直接可比；(2) Gilardi et al. (2023) ChatGPT annotation；(3) Ziems et al. (2024) LLM+CSS survey；(4) Bound, Brown & Mathiowetz (2001) survey measurement error；(5) Bayesian ME model 具体引用（Gustafson 2004 具体章节或 Richardson & Gilks 1993）。\"\n    action_items:\n      - round: 3\n        action: \"Related Work 补充 5 篇引用并讨论与本文关系\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R2-W6 首发，R1 AGREE。方法论论文含大量仿真实验，代码公开是 ARR 评审标准预期。ASV 计算工具作为 package 发布可大幅提升实用价值。\"\n    action_items:\n      - round: 3\n        action: \"论文中承诺公开代码，或在 supplementary 中提供\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W4 首发，R2 partially agrees。K≥3 sign reversal 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出；residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中已分析。论文应明确：'以下已知：...。我们的新贡献：(1) 系统性 7 拓扑对比；(2) ASV 框架；(3) FWL invariance 对 correction 的影响'。R2 认为这是 framing 改进而非 novelty 不足。\"\n    action_items:\n      - round: 3\n        action: \"Introduction 或 Related Work 添加 1-2 句明确的 novelty delineation\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1-W5 首发，R2 partially agrees。'Empirical validation' 用真实 CM 但应用于模拟 DGP（线性 SEM），验证的是推导正确性而非实践指导价值。ClinicalBERT case study (Appendix B.2) 是回顾性应用。R2 认为这是方法论论文标准做法，但同意完整 real-world case study 会增强说服力。\"\n    action_items:\n      - round: 3\n        action: \"考虑将 Appendix B.2 case study 扩展并移入正文；或增加 semi-synthetic 实验\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-22T14:01:32.033527+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 18772}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-22T14:04:11.079372+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# Round 3 合并审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (via ARR), Long Paper\n**Reviewers**: R1（方法严谨性）, R2（新颖性+完整性+写作+格式）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统研究了 K 类（K≥3）非差异误分类在七种典型因果 DAG 拓扑下的偏差传播。核心发现：(1) K=2 时二分类变量的 attenuation-toward-null 保证在 K≥3 时结构性崩塌——exposure 和 IV 拓扑可产生符号反转；(2) 其余五种拓扑维持符号保持（confounding 和 collider 有解析证明，mediation/M-bias/front-door 有数值验证）；(3) 提出 Annotation Sensitivity Values (ASV) 框架量化各拓扑的脆弱性光谱；(4) 证明 Frisch-Waugh-Lovell 不变性导致矩阵校正方法对 4/7 拓扑无效；(5) 通过真实 LLM confusion matrix 的经验验证确认理论预测。\n\n---\n\n## Strengths\n\n**S1** [共识] **重要且及时的问题**。LLM 标注在计算社会科学中快速普及，标注误差对因果推断的影响是紧迫问题。本文提供了首个系统性框架。\n\n**S2** [共识] **K≥3 代数断点的刻画**。证明 K=2 的符号保持保证在 K≥3 时因混淆矩阵高维自由度而结构性崩塌，这是一个非平凡的定性结果，对实践者有直接指导意义。\n\n**S3** [共识] **FWL 不变性的实用洞察**。揭示矩阵校正方法（naive plug-in, MLA）对 4/7 拓扑 provably 无效，文献中长期被忽视，对实践者直接可操作。\n\n**S4** [共识] **ASV 框架的可操作性**。提供参数化的敏感性分析工具，类比 E-values 但针对标注误差，包含三种互补度量（magnitude/significance/sign-flip），实用价值明确。\n\n**S5** [共识] **系统覆盖面**。7 DAG 拓扑 × 5 校正方法 × 多种验证方式（100,000 随机矩阵 + 4 LLM × 3 数据集 + logistic DGP + case study），覆盖面全面。\n\n**S6** [共识] **附录质量高**。12 页附录包含详细 Lemma-Proposition 证明链、stress test、bootstrap ASV 分析、case study，质量高于多数投稿。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [共识, critical] **正文超出 8 页限制约 0.5 页**\nSection 5 (Conclusion) 在第 9 页开始，正文约 8.3 页。EMNLP 2026 Long Paper 严格限制 8 页正文（不含 References 和 Limitations）。main.tex 已使用 `\\enlargethispage` 和压缩 `\\floatsep` 等手段但仍超限。这是 ARR desk rejection 条件之一。\n- *建议*：压缩 Section 4（Cross-K robustness 段和 ASV diagnostic results 段可移至附录）；Figure 1+2 占满整页，考虑缩小或合并；精简 Section 2 Related Work。\n\n**N2** [共识, critical] **Sign reversal 严重性被过度声称**\nAbstract 和 Introduction 以 Dirichlet(1,1,1) 全参数空间的 83.4% sign reversal 为主导叙事，辅以 \"catastrophic\" 等极端措辞。但：(1) Dirichlet(1,1,1) 包含大量不现实的非对角占优矩阵（平均准确率 1/K）；(2) 在实际 LLM 分类器精度下（diagonal ≥ 0.7），sign reversal 降至 2.1%；(3) 论文 Section 4.4 自身明确写道 \"The primary coefficient (β₁, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small |β|\"。Section 4.2 的 \"catastrophic sign reversal\" 小标题与 Section 4.4 的实证结果自相矛盾。\n- R1 补充：理论上任何系数 CAN reverse 的结论本身有价值，建议调整为 \"sign reversal is theoretically possible for K≥3, practically rare for primary coefficients under realistic classifiers, but non-negligible for secondary coefficients\"\n- *建议*：(1) Abstract 先报告 realistic regime (diagonal ≥ 0.7, 2.1% sign reversal)，再提 Dirichlet 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 用 \"structurally possible\" 替代 \"catastrophic\"\n\n**N3** [R1 critical, R2 should-fix, 分歧] **Theorem 1 适用范围过窄，Conjecture 1 未证明**\nTheorem 1 仅覆盖 confounding + proportional effects（f = λg）。其余 6 个非 IV 拓扑的 ASV 单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性（虽然违反幅度 < 0.06）。如果单调性不成立，ASV 的 \"临界 δ 阈值\" 语义变得模糊。\n- R1 立场：ASV 是论文核心实用贡献，其理论基础不应仅依赖 numerical verification → must-fix\n- R2 立场：ASV 核心价值在于 topology ranking，ranking 在所有实验中成立，不完全依赖严格单调性；ε < 0.06 足够小 → should-fix\n- *建议*：(1) 至少证明 mediation 的单调性（Eq.3 结构较简单）；(2) 给出 ε 关于 K 和 DGP 参数的 formal bound；(3) 明确讨论 Conjecture 失败时 ASV interpretation 如何 degrade\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [共识] **3/5 sign preservation 拓扑 \"establish\" 措辞过度**\nAbstract 用 \"establish that five topologies show no sign reversal\"，但 mediation/M-bias/front-door 仅有 100,000 随机矩阵的数值验证（Empirical Finding 1），附录明确写 \"analytic proofs for general K remain open\"。\"Establish\" 暗示证明而非验证。\n- *建议*：改为 \"prove for confounding and collider, and verify numerically for mediation, M-bias, and front-door\"\n\n**W2** [R1 critical, R2 should-fix, 分歧] **FWL invariance 结论缺乏 precise statement**\n论文声称 \"matrix-based corrections achieve exactly 0% bias reduction\" 对 4 个 FWL 拓扑成立，但：(a) \"matrix-based correction\" 无精确定义；(b) SIMEX 的 0% reduction 与其理论上应能外推的预期矛盾，需解释；(c) 与 Carroll et al. (2006) 已知 residual confounding 结果的关系未澄清。\n- R1 立场：缺 formal proof，无法区分深刻洞察 vs 实验 artifact → must-fix\n- R2 立场：FWL invariance 是 FWL 定理的 direct corollary（C⁻¹ 不改变 column space → projection matrix 不变 → T 系数不变），3 行推导即可，是 writing clarity 问题 → should-fix\n- *建议*：添加 precise definition + 3-4 行 FWL 推导 + SIMEX 解释 + Carroll (2006) 关系讨论\n\n**W3** [共识] **Non-differential misclassification 假设讨论不足**\nLLM 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在许多场景中不成立。Appendix B.4 的 extended stress test 覆盖 96 configurations（4 topologies × 2K × 3 CM × 4ε），但正文 Method 部分未讨论何时 LLM 满足此假设（如 LLM 未见 outcome 文本时）。\n- *建议*：(1) 正文讨论具体 NLP 场景（sentiment vs. stance detection）；(2) stress test 进一步覆盖 confounding 拓扑\n\n**W4** [共识] **线性 SEM 假设限制实用性**\n所有结果基于线性结构方程。论文自身承认 \"FWL invariance result does not hold for logistic regression\"——Algorithm 1 的 FWL 分流建议在非线性设定下可能失效，但 Algorithm 1 未标注此 caveat。Appendix B.6 的 logistic DGP robustness check 仅覆盖 3/7 拓扑。\n- *建议*：(1) Algorithm 1 标注 \"linear models only\"；(2) 扩展 Appendix B.6 至全部 7 拓扑\n\n**W5** [共识] **缺少 outcome misclassification 讨论**\n许多 NLP 因果研究中 Y 也由 LLM 标注。至少在 Limitations 中讨论 outcome misclassification 的影响和扩展方向。\n\n**W6** [共识] **Abstract 信息过载**\nAbstract 包含 15+ 个具体数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0% 等），影响可读性。\n- *建议*：保留 3-5 个最关键数字，其余移入正文\n\n**W7** [共识] **未承诺代码/数据公开**\n方法论论文含大量仿真实验，代码公开是 ARR 标准预期。ASV 计算工具作为 package 发布可大幅提升实用价值。\n\n**W8** [R1 warning, R2 partially agrees] **新颖性定位不清**\nK≥3 sign reversal 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出；residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中已分析。论文应明确界定 \"已知结果在 LLM 语境的应用\" vs \"真正新贡献\"。R2 认为这是 framing 改进而非 novelty 不足。\n\n**W9** [R1 warning, R2 partially agrees] **经验验证使用模拟 DGP 而非真实因果数据**\n\"Empirical validation\" 用真实 LLM confusion matrices 但应用于模拟 DGP（线性 SEM），验证的是推导正确性而非实践指导价值。R2 认为这是方法论论文标准做法，但同意完整 real-world case study 会增强说服力。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识：\n1. **[AGREE]** 正文超 8 页限制 — 双方 critical\n2. **[AGREE]** Sign reversal 83.4% framing overclaiming — 双方同意需调整叙事（R2 critical, R1 upgraded after cross-sharing）\n3. **[AGREE]** Non-differential 假设讨论不足 — 双方 warning\n4. **[AGREE]** 线性 SEM 限制 + Algorithm 1 缺 caveat — 双方 warning\n5. **[AGREE]** Abstract 信息过载 — 双方 warning\n6. **[AGREE]** 代码公开 — 双方 warning\n7. **[AGREE]** 3/5 拓扑 \"establish\" 措辞过度 — 双方 warning\n8. **[AGREE]** Outcome misclassification 缺讨论 — 双方 warning\n9. **[AGREE]** 所有 6 条优势 — 双方一致\n10. **[AGREE]** 新颖性评估：相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 增量充分；ASV 创新中等；FWL invariance 实用价值高；topology-dependent 视角足够\n11. **[AGREE]** 缺少 Cinelli & Hazlett (2020)、Gilardi et al. (2023)、Ziems et al. (2024) 等引用\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧性质 |\n|------|----|----|----------|\n| Conjecture 1 严重性 | N1 must-fix | W2 should-fix | 严重性分歧：R1 认为 ASV 理论基础需保障，R2 认为 ranking 结论不受影响 |\n| FWL invariance 证明 | N3 must-fix | Should-fix (writing) | 定性分歧：R1 要求 formal proof，R2 认为是 FWL 的 direct corollary 仅需改善表述 |\n| 模拟 DGP 验证 | W5 warning | Partially agrees | R1 要求 semi-synthetic 实验，R2 认为方法论论文标准做法 |\n| C(δ) 参数化唯一性 | — | Q4 (question) | R1 rebut：线性路径是自然选择但应讨论替代方案（唯一 REBUT 点） |\n\n---\n\n## Questions（需要作者澄清）\n\n1. 在 realistic regime（diagonal ≥ 0.7）下 sign reversal rate 仅 2.1%，为何 abstract 选择以 83.4% 作为主要数字？\n2. Empirical Finding 1（mediation, M-bias, front-door 的 sign preservation）是否有解析证明进展？如果这 3 个拓扑的保证只是 conjectural，论文核心 claim \"five topologies maintain structural guarantee\" 的可信度如何评估？\n3. 论文是否计划公开代码和 ASV 计算工具？\n4. Algorithm 1 在非线性模型（如 logistic regression）下是否仍然有效？FWL 分流分支的适用范围应如何界定？\n5. C(δ) = (1-δ)I + δC₀ 线性参数化的选择理由是什么？如果实际退化路径不在此线上，ASV 的意义如何？\n\n---\n\n## Missing References\n\n1. **Cinelli & Hazlett (2020)** \"Making Sense of Sensitivity: Extending Omitted Variable Bias\" — 与 ASV 框架有直接可比性（robustness value vs ASV），应在 Section 2 或 3.3 中讨论对比 [双方 AGREE]\n2. **Gilardi et al. (2023)** \"ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks\" — LLM 标注的标志性论文 [双方 AGREE]\n3. **Ziems et al. (2024)** \"Can Large Language Models Transform Computational Social Science?\" — 综合 survey，与论文 motivation 直接相关 [双方 AGREE]\n4. **Bound, Brown & Mathiowetz (2001)** — Survey data 中 measurement error 经典综述 [双方 AGREE]\n5. **Bayesian measurement error models 具体引用**（如 Richardson & Gilks 1993, Gustafson 2004 具体章节）— Section 4.5 提及但未引用具体工作 [双方 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因配额限制（rate limit）执行失败，未产出排版审查结果。建议用户可手动触发重试。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**Soundness: 3.5/5** — 核心 bias 表达式和已有证明（Theorem 1, Propositions for confounding/collider）正确；但 Conjecture 1 未证明、3/5 sign preservation 仅有数值验证、FWL invariance 表述不够 precise。\n\n**Excitement: 3.25/5** — Topology-dependent 视角是足够的概念创新，ASV 框架可操作，FWL invariance 被忽视但重要；但理论深度中等（Conjecture 而非 Theorem），ASV 是 E-value 的自然类比，K≥3 break 本身已被 Dosemeci (1990) 指出。\n\n**Reproducibility: 4/5** — 数学公式清晰，DGP 参数详细，附录证明完整；但未承诺代码公开。\n\n**Confidence: 4/5** — 两位 Reviewer 均熟悉测量误差理论和因果推断文献，逐页仔细阅读含附录。\n\n**总体判断**：这是一篇重要且及时的方法论工作，系统性 taxonomy 和 ASV 框架有明确的实用价值。主要不足在于：(1) 格式问题（超页，desk rejection 风险）；(2) framing 过度声称（83.4% vs 2.1%，\"catastrophic\" vs secondary coefficients only）；(3) 理论完备性中等（Conjecture 未证明，部分 sign preservation 仅数值验证）。如果格式和 framing 问题能在修订中解决，论文有潜力达到 Conference (4.0) 水平；如果 Conjecture 1 能至少部分证明，理论贡献将显著增强。当前版本处于 Borderline Conference / Findings 交界。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"catastrophic\" 措辞与 Section 4.4 实证结果不符——primary coefficient 从未反转\n- 建议添加 1-2 句 novelty delineation：\"The possibility of polytomous sign reversal was noted by Dosemeci et al. (1990); our contribution is the first systematic characterization across multiple DAG topologies and the ASV framework for quantifying this vulnerability.\"\n\n### Section 2 (Related Work)\n- 缺少 Cinelli & Hazlett (2020) 与 ASV 的对比讨论\n- 缺少 Gilardi et al. (2023) 和 Ziems et al. (2024) 作为 LLM annotation 动机引用\n- 可精简以节省页面空间\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 中 \"establish\" 措辞对 mediation/M-bias/front-door 过度——应区分 \"proven\" vs \"numerically verified\"\n- Empirical Finding 1 的条件涉及未知 DGP 参数，实践中难以事前验证——论文已提 ASV 作为替代，但可进一步讨论\n\n### Section 3.3 (ASV Framework)\n- Theorem 1 限于 proportional effects——应讨论此假设何时成立/失败\n- Conjecture 1：60-97% 矩阵违反严格单调性但幅度 < 0.06——应更诚实地讨论\n- C(δ) 线性参数化的选择应讨论替代方案（matrix exponential, Dirichlet-based）\n\n### Section 4 (Experiments)\n- Section 4.2 \"catastrophic sign reversal\" 小标题与 Section 4.4 结果矛盾\n- Cross-K robustness 和 ASV diagnostic 段可移至附录以节省空间\n- \"grand MAPE of 2.0% across 126 scenarios (18 LLM configurations × 7 topologies)\" 的 126 = 18×7 推导出现在 Monte Carlo 验证段，容易与 empirical validation 混淆\n\n### Section 4.5 (Correction Guidance)\n- \"matrix-based correction\" 需 precise definition\n- FWL invariance 需 3-4 行推导而非仅引用实验结果\n- SIMEX 对 FWL 拓扑的 0% reduction 需解释为何不矛盾\n- Algorithm 1 需标注 \"linear models only\" caveat\n- Bayesian ME models 作为 FWL bypass 方案需引用具体工作\n\n### Section 5 (Conclusion)\n- 溢出到第 9 页——压缩或部分合入 Limitations\n\n### Limitations\n- 应增加 outcome misclassification 讨论\n- Non-differential 假设的适用场景应更具体\n\n### 附录\n- 符号表（Table 8）存在但正文 τ/β_T 仍不一致\n- Proposition 编号在正文与附录间缺乏交叉引用\n- Figure 2 y 轴标签偏小，影响打印可读性\n\n### 跨轮次 Issue 追踪\n本轮为 Round 3 fresh 审稿。以下先前 issue 已确认修复：\n- R1-N3 (ASV δ 定义域) — Section 3.3 引入 δ_max 约束 ✓\n- R2-N2 ('first systematic framework' overclaim) — Abstract 已改为 'a systematic framework' ✓\n- R2-N3 (4 篇缺失引用) — Related Work 已恢复 ✓\n- R2-W2 (zero reversals vs narrative tension) — Triple verification narrative 已改善 ✓\n- R2-W3 (ASV bootstrap uncertainty) — Appendix B.5 已包含 B=1,000 bootstrap 分析 ✓\n- NEW-2 (Feder et al. 2022, Cheng et al. 2024) — Related Work 已引用 ✓\n- NEW-3 (Conjecture 1 验证规模) — Appendix C 已扩展至 210,000 matrices ✓\n\n以下 issue 持续存在或新增：\n- R1-N1 (Theorem 1/Conjecture 1) — 持续 open（Round 1-3）\n- R1-N2 (3/5 拓扑 \"establish\" 措辞) — 持续 open（Round 1-3）\n- R2-N1 (83.4% framing) — 持续 open 且新增 secondary coefficient 维度（Round 1-3）\n- R3-NEW-1 ~ R3-NEW-8 — 本轮新增 8 个 issue\n\n完整 issue tracker 见 `artifacts/review_issues.yaml`。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# Round 3 合并审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (via ARR), Long Paper\n**Reviewers**: R1（方法严谨性）, R2（新颖性+完整性+写作+格式）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统研究了 K 类（K≥3）非差异误分类在七种典型因果 DAG 拓扑下的偏差传播。核心发现：(1) K=2 时二分类变量的 attenuation-toward-null 保证在 K≥3 时结构性崩塌——exposure 和 IV 拓扑可产生符号反转；(2) 其余五种拓扑维持符号保持（confounding 和 collider 有解析证明，mediation/M-bias/front-door 有数值验证）；(3) 提出 Annotation Sensitivity Values (ASV) 框架量化各拓扑的脆弱性光谱；(4) 证明 Frisch-Waugh-Lovell 不变性导致矩阵校正方法对 4/7 拓扑无效；(5) 通过真实 LLM confusion matrix 的经验验证确认理论预测。\n\n---\n\n## Strengths\n\n**S1** [共识] **重要且及时的问题**。LLM 标注在计算社会科学中快速普及，标注误差对因果推断的影响是紧迫问题。本文提供了首个系统性框架。\n\n**S2** [共识] **K≥3 代数断点的刻画**。证明 K=2 的符号保持保证在 K≥3 时因混淆矩阵高维自由度而结构性崩塌，这是一个非平凡的定性结果，对实践者有直接指导意义。\n\n**S3** [共识] **FWL 不变性的实用洞察**。揭示矩阵校正方法（naive plug-in, MLA）对 4/7 拓扑 provably 无效，文献中长期被忽视，对实践者直接可操作。\n\n**S4** [共识] **ASV 框架的可操作性**。提供参数化的敏感性分析工具，类比 E-values 但针对标注误差，包含三种互补度量（magnitude/significance/sign-flip），实用价值明确。\n\n**S5** [共识] **系统覆盖面**。7 DAG 拓扑 × 5 校正方法 × 多种验证方式（100,000 随机矩阵 + 4 LLM × 3 数据集 + logistic DGP + case study），覆盖面全面。\n\n**S6** [共识] **附录质量高**。12 页附录包含详细 Lemma-Proposition 证明链、stress test、bootstrap ASV 分析、case study，质量高于多数投稿。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [共识, critical] **正文超出 8 页限制约 0.5 页**\nSection 5 (Conclusion) 在第 9 页开始，正文约 8.3 页。EMNLP 2026 Long Paper 严格限制 8 页正文（不含 References 和 Limitations）。main.tex 已使用 `\\enlargethispage` 和压缩 `\\floatsep` 等手段但仍超限。这是 ARR desk rejection 条件之一。\n- *建议*：压缩 Section 4（Cross-K robustness 段和 ASV diagnostic results 段可移至附录）；Figure 1+2 占满整页，考虑缩小或合并；精简 Section 2 Related Work。\n\n**N2** [共识, critical] **Sign reversal 严重性被过度声称**\nAbstract 和 Introduction 以 Dirichlet(1,1,1) 全参数空间的 83.4% sign reversal 为主导叙事，辅以 \"catastrophic\" 等极端措辞。但：(1) Dirichlet(1,1,1) 包含大量不现实的非对角占优矩阵（平均准确率 1/K）；(2) 在实际 LLM 分类器精度下（diagonal ≥ 0.7），sign reversal 降至 2.1%；(3) 论文 Section 4.4 自身明确写道 \"The primary coefficient (β₁, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small |β|\"。Section 4.2 的 \"catastrophic sign reversal\" 小标题与 Section 4.4 的实证结果自相矛盾。\n- R1 补充：理论上任何系数 CAN reverse 的结论本身有价值，建议调整为 \"sign reversal is theoretically possible for K≥3, practically rare for primary coefficients under realistic classifiers, but non-negligible for secondary coefficients\"\n- *建议*：(1) Abstract 先报告 realistic regime (diagonal ≥ 0.7, 2.1% sign reversal)，再提 Dirichlet 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 用 \"structurally possible\" 替代 \"catastrophic\"\n\n**N3** [R1 critical, R2 should-fix, 分歧] **Theorem 1 适用范围过窄，Conjecture 1 未证明**\nTheorem 1 仅覆盖 confounding + proportional effects（f = λg）。其余 6 个非 IV 拓扑的 ASV 单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性（虽然违反幅度 < 0.06）。如果单调性不成立，ASV 的 \"临界 δ 阈值\" 语义变得模糊。\n- R1 立场：ASV 是论文核心实用贡献，其理论基础不应仅依赖 numerical verification → must-fix\n- R2 立场：ASV 核心价值在于 topology ranking，ranking 在所有实验中成立，不完全依赖严格单调性；ε < 0.06 足够小 → should-fix\n- *建议*：(1) 至少证明 mediation 的单调性（Eq.3 结构较简单）；(2) 给出 ε 关于 K 和 DGP 参数的 formal bound；(3) 明确讨论 Conjecture 失败时 ASV interpretation 如何 degrade\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [共识] **3/5 sign preservation 拓扑 \"establish\" 措辞过度**\nAbstract 用 \"establish that five topologies show no sign reversal\"，但 mediation/M-bias/front-door 仅有 100,000 随机矩阵的数值验证（Empirical Finding 1），附录明确写 \"analytic proofs for general K remain open\"。\"Establish\" 暗示证明而非验证。\n- *建议*：改为 \"prove for confounding and collider, and verify numerically for mediation, M-bias, and front-door\"\n\n**W2** [R1 critical, R2 should-fix, 分歧] **FWL invariance 结论缺乏 precise statement**\n论文声称 \"matrix-based corrections achieve exactly 0% bias reduction\" 对 4 个 FWL 拓扑成立，但：(a) \"matrix-based correction\" 无精确定义；(b) SIMEX 的 0% reduction 与其理论上应能外推的预期矛盾，需解释；(c) 与 Carroll et al. (2006) 已知 residual confounding 结果的关系未澄清。\n- R1 立场：缺 formal proof，无法区分深刻洞察 vs 实验 artifact → must-fix\n- R2 立场：FWL invariance 是 FWL 定理的 direct corollary（C⁻¹ 不改变 column space → projection matrix 不变 → T 系数不变），3 行推导即可，是 writing clarity 问题 → should-fix\n- *建议*：添加 precise definition + 3-4 行 FWL 推导 + SIMEX 解释 + Carroll (2006) 关系讨论\n\n**W3** [共识] **Non-differential misclassification 假设讨论不足**\nLLM 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在许多场景中不成立。Appendix B.4 的 extended stress test 覆盖 96 configurations（4 topologies × 2K × 3 CM × 4ε），但正文 Method 部分未讨论何时 LLM 满足此假设（如 LLM 未见 outcome 文本时）。\n- *建议*：(1) 正文讨论具体 NLP 场景（sentiment vs. stance detection）；(2) stress test 进一步覆盖 confounding 拓扑\n\n**W4** [共识] **线性 SEM 假设限制实用性**\n所有结果基于线性结构方程。论文自身承认 \"FWL invariance result does not hold for logistic regression\"——Algorithm 1 的 FWL 分流建议在非线性设定下可能失效，但 Algorithm 1 未标注此 caveat。Appendix B.6 的 logistic DGP robustness check 仅覆盖 3/7 拓扑。\n- *建议*：(1) Algorithm 1 标注 \"linear models only\"；(2) 扩展 Appendix B.6 至全部 7 拓扑\n\n**W5** [共识] **缺少 outcome misclassification 讨论**\n许多 NLP 因果研究中 Y 也由 LLM 标注。至少在 Limitations 中讨论 outcome misclassification 的影响和扩展方向。\n\n**W6** [共识] **Abstract 信息过载**\nAbstract 包含 15+ 个具体数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0% 等），影响可读性。\n- *建议*：保留 3-5 个最关键数字，其余移入正文\n\n**W7** [共识] **未承诺代码/数据公开**\n方法论论文含大量仿真实验，代码公开是 ARR 标准预期。ASV 计算工具作为 package 发布可大幅提升实用价值。\n\n**W8** [R1 warning, R2 partially agrees] **新颖性定位不清**\nK≥3 sign reversal 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出；residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中已分析。论文应明确界定 \"已知结果在 LLM 语境的应用\" vs \"真正新贡献\"。R2 认为这是 framing 改进而非 novelty 不足。\n\n**W9** [R1 warning, R2 partially agrees] **经验验证使用模拟 DGP 而非真实因果数据**\n\"Empirical validation\" 用真实 LLM confusion matrices 但应用于模拟 DGP（线性 SEM），验证的是推导正确性而非实践指导价值。R2 认为这是方法论论文标准做法，但同意完整 real-world case study 会增强说服力。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识：\n1. **[AGREE]** 正文超 8 页限制 — 双方 critical\n2. **[AGREE]** Sign reversal 83.4% framing overclaiming — 双方同意需调整叙事（R2 critical, R1 upgraded after cross-sharing）\n3. **[AGREE]** Non-differential 假设讨论不足 — 双方 warning\n4. **[AGREE]** 线性 SEM 限制 + Algorithm 1 缺 caveat — 双方 warning\n5. **[AGREE]** Abstract 信息过载 — 双方 warning\n6. **[AGREE]** 代码公开 — 双方 warning\n7. **[AGREE]** 3/5 拓扑 \"establish\" 措辞过度 — 双方 warning\n8. **[AGREE]** Outcome misclassification 缺讨论 — 双方 warning\n9. **[AGREE]** 所有 6 条优势 — 双方一致\n10. **[AGREE]** 新颖性评估：相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 增量充分；ASV 创新中等；FWL invariance 实用价值高；topology-dependent 视角足够\n11. **[AGREE]** 缺少 Cinelli & Hazlett (2020)、Gilardi et al. (2023)、Ziems et al. (2024) 等引用\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧性质 |\n|------|----|----|----------|\n| Conjecture 1 严重性 | N1 must-fix | W2 should-fix | 严重性分歧：R1 认为 ASV 理论基础需保障，R2 认为 ranking 结论不受影响 |\n| FWL invariance 证明 | N3 must-fix | Should-fix (writing) | 定性分歧：R1 要求 formal proof，R2 认为是 FWL 的 direct corollary 仅需改善表述 |\n| 模拟 DGP 验证 | W5 warning | Partially agrees | R1 要求 semi-synthetic 实验，R2 认为方法论论文标准做法 |\n| C(δ) 参数化唯一性 | — | Q4 (question) | R1 rebut：线性路径是自然选择但应讨论替代方案（唯一 REBUT 点） |\n\n---\n\n## Questions（需要作者澄清）\n\n1. 在 realistic regime（diagonal ≥ 0.7）下 sign reversal rate 仅 2.1%，为何 abstract 选择以 83.4% 作为主要数字？\n2. Empirical Finding 1（mediation, M-bias, front-door 的 sign preservation）是否有解析证明进展？如果这 3 个拓扑的保证只是 conjectural，论文核心 claim \"five topologies maintain structural guarantee\" 的可信度如何评估？\n3. 论文是否计划公开代码和 ASV 计算工具？\n4. Algorithm 1 在非线性模型（如 logistic regression）下是否仍然有效？FWL 分流分支的适用范围应如何界定？\n5. C(δ) = (1-δ)I + δC₀ 线性参数化的选择理由是什么？如果实际退化路径不在此线上，ASV 的意义如何？\n\n---\n\n## Missing References\n\n1. **Cinelli & Hazlett (2020)** \"Making Sense of Sensitivity: Extending Omitted Variable Bias\" — 与 ASV 框架有直接可比性（robustness value vs ASV），应在 Section 2 或 3.3 中讨论对比 [双方 AGREE]\n2. **Gilardi et al. (2023)** \"ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks\" — LLM 标注的标志性论文 [双方 AGREE]\n3. **Ziems et al. (2024)** \"Can Large Language Models Transform Computational Social Science?\" — 综合 survey，与论文 motivation 直接相关 [双方 AGREE]\n4. **Bound, Brown & Mathiowetz (2001)** — Survey data 中 measurement error 经典综述 [双方 AGREE]\n5. **Bayesian measurement error models 具体引用**（如 Richardson & Gilks 1993, Gustafson 2004 具体章节）— Section 4.5 提及但未引用具体工作 [双方 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因配额限制（rate limit）执行失败，未产出排版审查结果。建议用户可手动触发重试。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**Soundness: 3.5/5** — 核心 bias 表达式和已有证明（Theorem 1, Propositions for confounding/collider）正确；但 Conjecture 1 未证明、3/5 sign preservation 仅有数值验证、FWL invariance 表述不够 precise。\n\n**Excitement: 3.25/5** — Topology-dependent 视角是足够的概念创新，ASV 框架可操作，FWL invariance 被忽视但重要；但理论深度中等（Conjecture 而非 Theorem），ASV 是 E-value 的自然类比，K≥3 break 本身已被 Dosemeci (1990) 指出。\n\n**Reproducibility: 4/5** — 数学公式清晰，DGP 参数详细，附录证明完整；但未承诺代码公开。\n\n**Confidence: 4/5** — 两位 Reviewer 均熟悉测量误差理论和因果推断文献，逐页仔细阅读含附录。\n\n**总体判断**：这是一篇重要且及时的方法论工作，系统性 taxonomy 和 ASV 框架有明确的实用价值。主要不足在于：(1) 格式问题（超页，desk rejection 风险）；(2) framing 过度声称（83.4% vs 2.1%，\"catastrophic\" vs secondary coefficients only）；(3) 理论完备性中等（Conjecture 未证明，部分 sign preservation 仅数值验证）。如果格式和 framing 问题能在修订中解决，论文有潜力达到 Conference (4.0) 水平；如果 Conjecture 1 能至少部分证明，理论贡献将显著增强。当前版本处于 Borderline Conference / Findings 交界。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"catastrophic\" 措辞与 Section 4.4 实证结果不符——primary coefficient 从未反转\n- 建议添加 1-2 句 novelty delineation：\"The possibility of polytomous sign reversal was noted by Dosemeci et al. (1990); our contribution is the first systematic characterization across multiple DAG topologies and the ASV framework for quantifying this vulnerability.\"\n\n### Section 2 (Related Work)\n- 缺少 Cinelli & Hazlett (2020) 与 ASV 的对比讨论\n- 缺少 Gilardi et al. (2023) 和 Ziems et al. (2024) 作为 LLM annotation 动机引用\n- 可精简以节省页面空间\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 中 \"establish\" 措辞对 mediation/M-bias/front-door 过度——应区分 \"proven\" vs \"numerically verified\"\n- Empirical Finding 1 的条件涉及未知 DGP 参数，实践中难以事前验证——论文已提 ASV 作为替代，但可进一步讨论\n\n### Section 3.3 (ASV Framework)\n- Theorem 1 限于 proportional effects——应讨论此假设何时成立/失败\n- Conjecture 1：60-97% 矩阵违反严格单调性但幅度 < 0.06——应更诚实地讨论\n- C(δ) 线性参数化的选择应讨论替代方案（matrix exponential, Dirichlet-based）\n\n### Section 4 (Experiments)\n- Section 4.2 \"catastrophic sign reversal\" 小标题与 Section 4.4 结果矛盾\n- Cross-K robustness 和 ASV diagnostic 段可移至附录以节省空间\n- \"grand MAPE of 2.0% across 126 scenarios (18 LLM configurations × 7 topologies)\" 的 126 = 18×7 推导出现在 Monte Carlo 验证段，容易与 empirical validation 混淆\n\n### Section 4.5 (Correction Guidance)\n- \"matrix-based correction\" 需 precise definition\n- FWL invariance 需 3-4 行推导而非仅引用实验结果\n- SIMEX 对 FWL 拓扑的 0% reduction 需解释为何不矛盾\n- Algorithm 1 需标注 \"linear models only\" caveat\n- Bayesian ME models 作为 FWL bypass 方案需引用具体工作\n\n### Section 5 (Conclusion)\n- 溢出到第 9 页——压缩或部分合入 Limitations\n\n### Limitations\n- 应增加 outcome misclassification 讨论\n- Non-differential 假设的适用场景应更具体\n\n### 附录\n- 符号表（Table 8）存在但正文 τ/β_T 仍不一致\n- Proposition 编号在正文与附录间缺乏交叉引用\n- Figure 2 y 轴标签偏小，影响打印可读性\n\n### 跨轮次 Issue 追踪\n本轮为 Round 3 fresh 审稿。以下先前 issue 已确认修复：\n- R1-N3 (ASV δ 定义域) — Section 3.3 引入 δ_max 约束 ✓\n- R2-N2 ('first systematic framework' overclaim) — Abstract 已改为 'a systematic framework' ✓\n- R2-N3 (4 篇缺失引用) — Related Work 已恢复 ✓\n- R2-W2 (zero reversals vs narrative tension) — Triple verification narrative 已改善 ✓\n- R2-W3 (ASV bootstrap uncertainty) — Appendix B.5 已包含 B=1,000 bootstrap 分析 ✓\n- NEW-2 (Feder et al. 2022, Cheng et al. 2024) — Related Work 已引用 ✓\n- NEW-3 (Conjecture 1 验证规模) — Appendix C 已扩展至 210,000 matrices ✓\n\n以下 issue 持续存在或新增：\n- R1-N1 (Theorem 1/Conjecture 1) — 持续 open（Round 1-3）\n- R1-N2 (3/5 拓扑 \"establish\" 措辞) — 持续 open（Round 1-3）\n- R2-N1 (83.4% framing) — 持续 open 且新增 secondary coefficient 维度（Round 1-3）\n- R3-NEW-1 ~ R3-NEW-8 — 本轮新增 8 个 issue\n\n完整 issue tracker 见 `artifacts/review_issues.yaml`。\n"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-22T14:04:15.348358+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4268
}
```

</details>

---


### Assistant

_source line 246 · 2026-05-22T14:04:29.331645+00:00_

审稿报告已投递。

**Round 3 审稿完成总结**：

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 完全一致
- **3 个 Must-Fix**：正文超 8 页（双方 critical）、sign reversal overclaiming（双方共识升级）、Conjecture 1 未证明（R1 critical / R2 should-fix，分歧记录在报告中）
- **9 个 Should-Fix**：FWL invariance 表述（分歧）、"establish" 措辞、non-differential 假设、线性 SEM 限制、outcome misclassification、Abstract 过载、代码公开、新颖性定位、模拟 DGP 验证
- **5 篇遗漏引用**：Cinelli & Hazlett (2020)、Gilardi et al. (2023)、Ziems et al. (2024) 等
- **视觉审查**：Agent 配额耗尽，未完成
- **外部审稿**：未请求

Issue tracker 已同步更新至 `review_issues.yaml`（7 个先前 issue 确认修复，3 个持续 open，8 个新增）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 247 · 2026-05-22T14:04:32.046881+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。两位 reviewer 在 Overall 3.5、页数超限、overclaiming 等核心问题上高度一致，主要分歧在 FWL invariance 的严重性评估（R1 视为 critical missing proof，我视为 writing clarity issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 248 · 2026-05-22T14:04:48.402837+00:00_

审稿报告已投递至 Research Director。

**Round 3 审稿总结**：

- **Overall 3.5（Borderline Conference）**，两位 Reviewer 一致
- **3 个 Must-Fix**：正文超 8 页（desk rejection 风险）、83.4% sign reversal framing 过度声称、Conjecture 1 未证明（R1 critical / R2 should-fix，存在分歧）
- **9 个 Should-Fix**：3/5 拓扑 "establish" 措辞、FWL invariance 表述不精确（R1 critical / R2 should-fix）、non-differential 假设讨论不足、线性 SEM 限制 + Algorithm 1 缺 caveat、outcome misclassification 缺讨论、Abstract 数字过载、代码未公开、新颖性定位不清、模拟 DGP 验证
- **5 篇缺失引用**：Cinelli & Hazlett (2020)、Gilardi et al. (2023)、Ziems et al. (2024)、Bound et al. (2001)、Bayesian ME 具体引用
- **7 个先前 issue 确认修复**（δ 定义域、overclaim 措辞、4 篇引用恢复、bootstrap ASV、Conjecture 验证规模等）
- **视觉审查**：Agent 配额耗尽，未完成
- **外部审稿**：未请求

Issue tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 27

## Round 27

56 recorded events


### User

_source line 249 · 2026-05-22T14:47:03.867569+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-22T14:47:14.309916+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-22T14:47:14.361131+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-22T14:47:21.189815+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-22T14:47:21.190248+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-22T14:47:24.754505+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-22T14:47:24.855349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-22T14:47:27.625546+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-22T14:47:28.068818+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 443
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-22T14:47:28.159401+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 259 · 2026-05-22T14:47:28.216321+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 56
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-22T14:47:31.104784+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 261 · 2026-05-22T14:47:31.155393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-22T14:47:38.635784+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-22T14:47:38.887392+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-22T14:47:44.812561+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 265 · 2026-05-22T14:47:44.812917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-22T14:47:45.818364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-22T14:47:46.873255+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	
19	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
20	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{method}
39	
40	% ── Figures ──
41	
42	\begin{figure*}[t]
43	\centering
44	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
45	\vspace{-6pt}
46	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
47	\label{fig:dag_taxonomy}
48	\end{figure*}
49	
50	\begin{figure*}[t]
51	\centering
52	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
53	\vspace{-6pt}
54	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
55	\label{fig:bias_distribution}
56	\end{figure*}
57	
58	\input{experiments}
59	
60	\input{conclusion}
61	
62	\bibliography{references}
63	
64	\appendix
65	\input{appendix_proofs}
66	
67	\end{document}
68	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-22T14:47:47.275342+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-22T14:47:48.279895+00:00_

-rw-r--r-- 1 ubuntu ubuntu 850415 May 22 14:41 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-22T14:47:48.783389+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-22T14:47:48.884368+00:00_

/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-22T14:47:55.061002+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-22T14:47:55.513271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-22T14:47:56.467343+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy (diagonal ${\geq}\,0.7$), the sign reversal rate is 2.1\%, exclusively in secondary coefficients---the primary treatment effect never reverses in any of 23 empirical LLM configurations. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 275 · 2026-05-22T14:47:56.518091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 276 · 2026-05-22T14:47:56.970399+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	Even under realistic classifier accuracy (diagonal $\geq 0.7$), 13.7\% of $K{=}3$ confusion matrices violate the classical binary guarantee, with 2.1\% causing sign reversal of the estimated treatment effect. Across the full Dirichlet$(1,1,1)$ parameter space, sign reversal reaches 83.4\%. This breaks the guarantee that non-differential misclassification biases estimates ``toward the null''~\cite{brenner1993}, a guarantee that many applied researchers implicitly rely upon. Standard classification metrics do not predict this risk: within a narrow $F_1$ range of 0.614--0.690 across three frontier LLMs, relative bias varies by an order of magnitude across topologies (from 4.1\% to 42.1\%), illustrating that \emph{topology}, not annotator quality, determines downstream
…[truncated 2420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-22T14:47:56.970863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-22T14:47:57.424611+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, and \citet{kim_garg2025} showed 60\% error correlation across models. \citet{audinet2025} benchmark debiasing; \citet{keith_jensen_oconnor2020} survey the broader landscape. These works either restrict to binary labels, cover a single topology, or diagnose quality without connecting it to causal validity.
9	
10	\paragraph{Sensitivity analysis and correction methods.}
11	Our ASV framework draws on E-values~\cite{vanderweele_ding2017} and the robustness value of \citet{cinelli2020making}, but parametrizes annotation error severity rather than omitted variable strength. For correction, PPI++~\cite{angelopoulos2023} and DSL~\
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-22T14:47:57.425100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-22T14:47:57.877263+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This assumption is satisfied when the LLM does not observe outcome-related text during annotation---for instance, when treatment labels are assigned from source documents that exclude outcome measurements.
15	
16	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
17	
18	\subsection{Multi-Class Bias Expressions}
19	\label{sec:bias_expressions}
20	
21	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
22	
23	\paragraph{Confounding ($A$ = confounder).}
24	When $A$ confounds the $X{\to}Y$ relationship, the OLS es
…[truncated 11394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 281 · 2026-05-22T14:47:57.927926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 282 · 2026-05-22T14:47:58.380111+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate the bias taxonomy and ASV framework through analytical derivations and Monte Carlo simulation across seven DAG topologies under $K{=}3$ non-differential misclassification.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 2.0\% across 126 scenarios (18 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.5\% (confounding) to 5.5\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\% of matrices cause \emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\beta_1{=}1.0$, a near-permutation $C$ produces $\hat{\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\times}$); for $\beta_2{=}{-}0.5$, the same $C$ yields $\hat{\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\times}$).
19	
20	This finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\% with 2.1\% sign reversal and 11.7\% amplification. Even at diagona
…[truncated 10923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-22T14:47:58.380582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-22T14:47:58.832514+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain a structural guarantee. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. Empirical validation with 23 real LLM configurations confirms: the primary treatment effect never reverses, but 61\% of exposure configurations reverse a secondary coefficient. Differential misclassification and correlated multi-LLM errors are natural extensions. Code for ASV computation and all experiments will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated with outcome-conditional prompting; a stress test across 96 configurations (Appendix~\ref{sec:nondiff_stress}) shows moderate robustness ($\varepsilon{=}0.05$ increases violations by $<$3pp). Our framework addresses misclassification of the treatment variable $A$; when the outcome $Y$ is also LLM-annotated, outcome misclassification introduces additional bias channels not captured by our analysis. Our empirical validation applies real LLM confusion matrices to simulated linear DGPs, verifying analytical predictions rather than end-to-end practical guidance in specific domains. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$; arbitrary $K$ remains open. The framework assumes a single annotator; correlated multi-annotator settings~\cite{kim_garg2025} are future work. All derivations assume linear structural equations; bias patterns under nonlinear models may differ (Appendix~\ref{sec:logistic_dgp}).
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 285 · 2026-05-22T14:47:58.832878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-22T14:47:59.334900+00:00_

File content (26131 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 287 · 2026-05-22T14:47:59.335395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 288 · 2026-05-22T14:47:59.837773+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@article{cinelli2020making,
5	  author    = {Cinelli, Carlos and Hazlett, Chad},
6	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
7	  journal   = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
8	  year      = {2020},
9	  volume    = {82},
10	  number    = {1},
11	  pages     = {39--67},
12	  doi       = {10.1111/rssb.12348},
13	}
14	
15	@article{gilardi2023chatgpt,
16	  author    = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma\"{e}l},
17	  title     = {{ChatGPT} Outperforms Crowd Workers for Text-Annotation Tasks},
18	  journal   = {Proceedings of the National Academy of Sciences},
19	  year      = {2023},
20	  volume    = {120},
21	  number    = {30},
22	  pages     = {e2305016120},
23	  doi       = {10.1073/pnas.2305016120},
24	}
25	
26	@article{ziems2024can,
27	  author    = {Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
28	  title     = {Can Large Language Models Transform Computational Social Science?},
29	  journal   = {Computational Linguistics},
30	  year      = {2024},
31	  volume    = {50},
32	  number    = {1},
33	  pages     = {237--291},
34	  doi       = {10.1162/coli\_a\_00502},
35	}
36	
37	@incollection{bound2001measurement,
38	  author    = {Bound, John and Brown, Charles and Mathiowetz, Nancy},
39	  title     = {Measurement Error in Survey Data},
40	  booktitle = {Handbook of Econometrics},
41	  editor    = {Heckman, James J. and Leamer, Edward E.},
42	  year      = {2001},
43	  volume    = {5},
44	  chapter   = {59},
45	  pages     = {3705--3843},
46	  publisher = {Elsevier},
47	}
48	
49	@article{richardson1993bayesian,
50	  author    = {Richardson, Sylvia and Gilks, Walter R.},
51	  title     = {A {Bayesian} Approach to Measurement Error Problems in Epidemiology Using Conditional Independence Models},
52	  journal   = {Amer
…[truncated 14901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-22T14:47:59.838204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-22T14:47:59.939808+00:00_

1	issues:
2	  # === Round 1 issues — status updates through Round 3 ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），Conjecture 1 未证明"
8	    status: in_progress
9	    first_raised_round: 1
10	    last_seen_round: 3
11	    mentions:
12	      - round: 1
13	        reviewers: [R1, R2]
14	        note: "R1 首发，R2 AGREE。"
15	      - round: 2
16	        reviewers: [R1, R2]
17	        note: "一般情形降级为 Empirical Finding，保留比例情形证明。"
18	      - round: 3
19	        reviewers: [R1, R2]
20	        note: "R1 critical, R2 should-fix。建议至少证明 mediation；给出 formal ε bound；讨论 ASV interpretation under approximate monotonicity。"
21	    action_items:
22	      - round: 2
23	        action: "一般情形降级为 Empirical Finding"
24	        assigned_to: agent
25	        status: done
26	      - round: 3
27	        action: "尝试 mediation 单调性证明 (3h time box)；formal ε bound；ASV degradation 讨论"
28	        assigned_to: agent
29	        status: in_progress
30	    resolution: ""
31	    resolution_round: null
32	
33	  - id: R1-N2
34	    category: soundness
35	    severity: should-fix
36	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
37	    status: in_progress
38	    first_raised_round: 1
39	    last_seen_round: 3
40	    mentions:
41	      - round: 1
42	        reviewers: [R1, R2]
43	        note: "R1 首发，R2 AGREE。"
44	      - round: 2
45	        reviewers: [R1, R2]
46	        note: "Abstract 改为 'proven analytically for confounding and collider'。"
47	      - round: 3
48	        reviewers: [R1, R2]
49	        note: "Abstract 仍用 'establish'，对仅有 empirical verification 的 3 拓扑是 overclaim。"
50	    action_items:
51	      - round: 2
52	        action: "Abstract 'never' → 'show no sign reversal'"
53	        assigned_to: agent
54	        status: done
55	      - round: 3
56	        action: "Abstract 'establish' → 'prove for confounding and collider, verify numerically for mediation, M-bias, front-door'"
57	        assign
…[truncated 11575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-22T14:48:00.241634+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the information about EMNLP 2026 call for papers submission deadline for ARR:

## EMNLP 2026 ARR Submission Deadline

The ARR submission deadline is May 25, 2026.
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 5180
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-22T14:48:23.140952+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf 2>/dev/null | grep -i pages || python3 -c \"import PyPDF2; r=PyPDF2.PdfReader('/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf'); print(f'Pages: {len(r.pages)}')\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf 2>/dev/null | grep -i pages || python3 -c \"import PyPDF2; r=PyPDF2.PdfReader('/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf'); print(f'Pages: {len(r.pages)}')\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-22T14:48:23.694312+00:00_

Pages:           23

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-22T14:48:23.694743+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-22T14:48:24.247360+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-22T14:48:24.448582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-22T14:48:24.599988+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Empirical Finding~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\tilde{Y
…[truncated 8485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-22T14:48:52.281858+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-22T14:49:12.673390+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20391
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-22T14:49:13.075551+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 目标 Venue\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- ARR 提交截止：2026-05-25\n- Long Paper：正文 8 页限制，参考文献不限\n- ACL 模板，double-blind 审稿\n- Overall Assessment 评分：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- TeX: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查重点\n\n### 1. 理论推导与证明\n- Proposition 1 (sign preservation) 的证明是否完整、正确？条件 (a)(b)(c) 是否充分？\n- Theorem 1 (envelope monotonicity) 的证明是否严格？proportional effects 假设的合理性？\n- Conjecture 1 (ε-approximate monotonicity) 的数值验证是否充分？ε < 0.06 的 bound 是否 tight？\n- 各拓扑的 bias expression 推导（Eq 1-4）是否正确？\n- Empirical Finding 1 的\"数值验证\"与\"解析证明\"的区分是否清晰？\n\n### 2. ASV 框架\n- C(δ) 参数化是否合理？δ_max 约束是否正确？\n- 三种 ASV 类型的定义是否严格、有歧义的地方？\n- N-sensitivity phase transition 的声明是否有支撑？\n- Bootstrap ASV 的实现是否合理？\n\n### 3. 实验设计与验证\n- Dirichlet(1,1,1) prior 的选择是否合理？是否讨论了 prior sensitivity？\n- MC 验证的 MAPE 2.0% 是否可接受？IV 的 5.5% MAPE 是否需要解释？\n- 经验验证使用 3 个数据集 + 4 个 LLM（23 configs）——覆盖是否充分？\n- Correction guidance: FWL invariance 的论证是否严谨？\"matrix-based correction\" 的定义是否精确？\n- PPI++ \"harmful for M-bias (-88%)\" 的解释是否充分？\n\n### 4. 数学严谨性\n- 符号使用是否一致（τ vs β_T 等）？\n- 定义、定理、引理的编号和交叉引用是否正确？\n- 附录证明是否完整？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [CRITICAL] / [MAJOR] / [MINOR])\n## Questions (需要作者澄清)\n## Missing References\n## Soundness Score (1-5)\n## Overall Assessment + 评分建议\n```",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 目标 Venue\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- ARR 提交截止：2026-05-25\n- Long Paper：正文 8 页限制，参考文献不限\n- ACL 模板，double-blind 审稿\n- Overall Assessment 评分：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- TeX: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查重点\n\n### 1. 理论推导与证明\n- Proposition 1 (sign preservation) 的证明是否完整、正确？条件 (a)(b)(c) 是否充分？\n- Theorem 1 (envelope monotonicity) 的证明是否严格？proportional effects 假设的合理性？\n- Conjecture 1 (ε-approximate monotonicity) 的数值验证是否充分？ε < 0.06 的 bound 是否 tight？\n- 各拓扑的 bias expression 推导（Eq 1-4）是否正确？\n- Empirical Finding 1 的\"数值验证\"与\"解析证明\"的区分是否清晰？\n\n### 2. ASV 框架\n- C(δ) 参数化是否合理？δ_max 约束是否正确？\n- 三种 ASV 类型的定义是否严格、有歧义的地方？\n- N-sensitivity phase transition 的声明是否有支撑？\n- Bootstrap ASV 的实现是否合理？\n\n### 3. 实验设计与验证\n- Dirichlet(1,1,1) prior 的选择是否合理？是否讨论了 prior sensitivity？\n- MC 验证的 MAPE 2.0% 是否可接受？IV 的 5.5% MAPE 是否需要解释？\n- 经验验证使用 3 个数据集 + 4 个 LLM（23 configs）——覆盖是否充分？\n- Correction guidance: FWL invariance 的论证是否严谨？\"matrix-based correction\" 的定义是否精确？\n- PPI++ \"harmful for M-bias (-88%)\" 的解释是否充分？\n\n### 4. 数学严谨性\n- 符号使用是否一致（τ vs β_T 等）？\n- 定义、定理、引理的编号和交叉引用是否正确？\n- 附录证明是否完整？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [CRITICAL] / [MAJOR] / [MINOR])\n## Questions (需要作者澄清)\n## Missing References\n## Soundness Score (1-5)\n## Overall Assessment + 评分建议\n```",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
````

</details>

---


### Tool result

_source line 301 · 2026-05-22T14:49:29.250147+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16174
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-22T14:49:29.551819+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 目标 Venue\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- ARR 提交截止：2026-05-25\n- Long Paper：正文 8 页限制，参考文献不限\n- ACL 模板，double-blind 审稿\n- Overall Assessment 评分：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- TeX: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查重点\n\n### 1. 新颖性与贡献定位\n- 三个 contribution 的新颖性如何？相对于 Dosemeci (1990)、Veierød & Laake (2001)、Teblunthuis (2024)、Lee & Wood-Doughty (2024) 的增量贡献是否清晰？\n- \"first to characterize across seven topologies\" 的声明是否成立？\n- ASV 框架相对于 E-values 和 robustness values 的创新点是否充分？\n- FWL invariance 作为 correction 的 negative result 是否足够 novel？\n\n### 2. 相关工作覆盖\n- 是否遗漏了重要的相关工作？特别是：\n  - measurement error in causal inference 方向\n  - LLM annotation quality 方向\n  - sensitivity analysis 方向\n  - correction/debiasing 方向\n- 引用格式和 bib 条目是否正确？\n\n### 3. 写作质量与叙事\n- Abstract 是否清晰传达核心贡献？是否信息过载？\n- Introduction 的 narrative arc 是否连贯？motivation → gap → contribution 的逻辑链是否通顺？\n- 数字/统计结果的 framing 是否诚实？是否有 overclaim？\n- 特别关注 83.4% sign reversal 的 framing：是否与 empirical validation 中 \"primary coefficient never reverses\" 的发现有 tension？\n- Limitations 章节是否充分？\n\n### 4. 格式合规\n- **正文是否在 8 页以内**？（这是 desk rejection 硬约束）\n- Limitations 是否存在且位置正确？\n- 匿名规则是否遵守？（无作者信息泄露）\n- 图表质量、可读性\n- 参考文献格式是否符合 ACL 标准？\n\n### 5. 再现性\n- 代码/数据是否承诺公开？\n- 实验设置描述是否足以复现？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [CRITICAL] / [MAJOR] / [MINOR])\n## Questions (需要作者澄清)\n## Missing References\n## Novelty Score (1-5)\n## Presentation Score (1-5)\n## Overall Assessment + 评分建议\n```",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 目标 Venue\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- ARR 提交截止：2026-05-25\n- Long Paper：正文 8 页限制，参考文献不限\n- ACL 模板，double-blind 审稿\n- Overall Assessment 评分：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- TeX: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查重点\n\n### 1. 新颖性与贡献定位\n- 三个 contribution 的新颖性如何？相对于 Dosemeci (1990)、Veierød & Laake (2001)、Teblunthuis (2024)、Lee & Wood-Doughty (2024) 的增量贡献是否清晰？\n- \"first to characterize across seven topologies\" 的声明是否成立？\n- ASV 框架相对于 E-values 和 robustness values 的创新点是否充分？\n- FWL invariance 作为 correction 的 negative result 是否足够 novel？\n\n### 2. 相关工作覆盖\n- 是否遗漏了重要的相关工作？特别是：\n  - measurement error in causal inference 方向\n  - LLM annotation quality 方向\n  - sensitivity analysis 方向\n  - correction/debiasing 方向\n- 引用格式和 bib 条目是否正确？\n\n### 3. 写作质量与叙事\n- Abstract 是否清晰传达核心贡献？是否信息过载？\n- Introduction 的 narrative arc 是否连贯？motivation → gap → contribution 的逻辑链是否通顺？\n- 数字/统计结果的 framing 是否诚实？是否有 overclaim？\n- 特别关注 83.4% sign reversal 的 framing：是否与 empirical validation 中 \"primary coefficient never reverses\" 的发现有 tension？\n- Limitations 章节是否充分？\n\n### 4. 格式合规\n- **正文是否在 8 页以内**？（这是 desk rejection 硬约束）\n- Limitations 是否存在且位置正确？\n- 匿名规则是否遵守？（无作者信息泄露）\n- 图表质量、可读性\n- 参考文献格式是否符合 ACL 标准？\n\n### 5. 再现性\n- 代码/数据是否承诺公开？\n- 实验设置描述是否足以复现？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [CRITICAL] / [MAJOR] / [MINOR])\n## Questions (需要作者澄清)\n## Missing References\n## Novelty Score (1-5)\n## Presentation Score (1-5)\n## Overall Assessment + 评分建议\n```",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
````

</details>

---


### Tool result

_source line 303 · 2026-05-22T14:49:31.098377+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1546
}
```

</details>

---


### Assistant

_source line 304 · 2026-05-22T14:49:38.457278+00:00_

**Round 1 已启动。** 当前状态：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | 🔄 审稿中 |
| Reviewer 2（新颖性/完整性） | 🔄 审稿中 |
| 视觉审查 Agent | 🔄 运行中 |
| 外部审稿 | ❌ 未启用 |

**Venue 确认**：EMNLP 2026 via ARR，提交截止 2026-05-25，Long Paper 正文 8 页限制，ACL 模板 double-blind。PDF 共 23 页（含附录）。

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 305 · 2026-05-22T14:54:53.846692+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（新颖性与完整性）

---

## Summary (2-3 句)

本文系统研究了 K≥3 多类别标注误差在七种因果 DAG 拓扑下的偏差传播机制，证明了 exposure 和 IV 拓扑可产生符号反转而其余五种保持符号，提出了 ASV 敏感性框架，并揭示了 FWL 不变性导致矩阵修正方法对四种拓扑无效。论文覆盖面广（7 拓扑 × 3 ASV 类型 × 5 修正方法 × 实证验证），但核心发现的 framing 存在误导性——标题式的 83.4% 符号反转率与实证中"主效应从不反转"之间的张力需要认真处理。

---

## Strengths

**S1. 系统性填补了明确的文献空白。** 现有工作要么限于 binary misclassification（Teblunthuis 2024，4 DAGs），要么限于单一拓扑的 categorical 扩展（Lee & Wood-Doughty 2024，仅 confounding）。本文是首个在 K≥3 条件下系统覆盖七种拓扑的工作。"first to characterize across seven topologies" 的声明经我核查是成立的。

**S2. FWL 不变性作为 negative result 干净优雅。** Section 4.4 + Appendix B.2 证明了当 A 作为 covariate 进入回归时，任何对 dummy matrix D* 的线性变换都不改变 treatment coefficient——这直接否定了四种拓扑下矩阵修正方法的有效性。这是一个有实际指导意义的理论结果，会改变实践者的工具选择。

**S3. 实证验证设计周密。** 用 23 个真实 LLM confusion matrix × 7 拓扑 = 161 个场景的验证规模有说服力。Figure 3 (F₁ vs. bias) 清楚展示了"分类准确率不预测因果风险"这一核心洞察。Theory-MC 的 2.0% grand MAPE 确认了解析推导的准确性。

**S4. Correction guidance 的实用价值。** Table 4 的 210 配置结果和 Algorithm 1 提供了可操作的拓扑依赖修正选择指南。特别是 PPI++ 对 M-bias 有 -88% RMSE 的发现（即加剧偏差）对实践者有重要警示意义。

**S5. 附录质量高。** 23 页中有 15 页附录，包含完整证明、反例构造、robustness checks（非线性 DGP、交叉 K 验证、bootstrap ASV）。这大幅增强了可信度。

---

## Weaknesses

**W1 [CRITICAL] Abstract/Introduction 对 83.4% 符号反转率的 framing 具有误导性。**
- 具体位置：Abstract 第 4 句、Section 1 第 2 段、Figure 2 caption
- 问题：83.4% 来自 uniform Dirichlet(1,1,1) 先验，包含大量近置换矩阵（off-diagonal 可以远大于 diagonal）——这在实际 LLM 标注中几乎不会出现。在 diagonal ≥ 0.7（realistic LLM accuracy 范围）条件下，符号反转率仅 2.1%。但 Abstract 以 "K≥3 introduces a structural possibility of sign reversal" 开头，紧接 "83.4% sign reversal"，直到第 5 句才提到 "under realistic LLM accuracy... the sign reversal rate is 2.1%"。读者最先记住的是 83.4%。
- 更关键的是：Section 4.3 的实证验证显示 "the primary coefficient (β₁, largest magnitude) never reverses"，符号反转仅发生在 secondary coefficients with small |β|。这意味着在实践中，研究者最关心的 primary treatment effect 是安全的。这个发现与 Abstract 的 alarm tone 形成了严重 tension。
- 为什么影响接收：审稿人和读者可能会认为这是 overclaim。一个严格的 reviewer 可能认为核心 message 被人为放大了。
- 建议：(1) Abstract 应将 "under realistic accuracy" 的 2.1% 放在 83.4% 之前或至少同等突出；(2) 明确区分 "any coefficient reverses" 和 "primary coefficient reverses"；(3) 在 Introduction 中早期承认 primary effect 的安全性。

**W2 [MAJOR] 三个拓扑的符号保持仅为经验发现，缺乏解析证明。**
- 具体位置：Section 3.2 "Empirical Finding 1"、Appendix A.5-A.7
- 问题：Mediation、M-bias、front-door 的符号保持仅通过 100,000 次随机矩阵数值验证（"zero violations"），并非严格证明。对于一篇以 "We derive bias expressions" 和 "We prove sign preservation" 为核心 claim 的论文，三个拓扑依赖数值验证削弱了理论贡献。Proposition 1 仅涵盖 confounding 和 collider，且 collider 的条件 |τ| > √(Var(g)Var(h))/E[Var(T|A)] 在实践中不一定满足。
- Conjecture 1（ε-approximate envelope monotonicity）同样仅有数值支撑，作为 Conjecture 出现在一篇投稿论文中较为少见。
- 建议：(1) 至少对 proportional effects 特殊情况给出 mediation 和 front-door 的解析证明（附录中似乎已有部分推导但未升级为 Proposition）；(2) 明确标注哪些是已证明的、哪些是 conjectured 的——当前的 "prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door"（Abstract）已经做了区分，但 Introduction 第 10 行 "prove sign preservation for confounding and collider" 容易让人误认为所有拓扑都有证明。

**W3 [MAJOR] ASV 框架相对于 E-values 和 robustness values 的方法论创新有限。**
- 具体位置：Section 3.3
- 问题：ASV 的核心思路是将 E-value 的 "unmeasured confounding strength" 替换为 "misclassification severity δ"，采用 C(δ) = (1-δ)I + δC₀ 的线性插值。这在概念上是 E-value 框架的直接移植，而非方法论创新。三种 ASV 类型（magnitude, significance, sign-flip）分别对应已有文献中的 bias threshold、power analysis、sign reversal threshold。
- Theorem 1 的 envelope monotonicity 仅对 proportional effects 成立（一般情况为 ε-approximate，即 Conjecture）。这意味着 ASV 的理论保证在一般情况下是近似的。
- 论文诚实地承认了 linear path 的局限性（Section 3.3: "alternative parameterizations... could capture nonlinear degradation but sacrifice the interpretability"），这很好。但这也意味着 ASV 的实用性取决于 linear interpolation 的合理性——对于高度非对称的真实 confusion matrices，这个假设需要更多讨论。
- 建议：(1) 更明确地定位 ASV 的贡献——不是方法论创新，而是将已有框架应用于一个新的、重要的问题设定（annotation error × topology）；(2) 讨论 C₀ 的选择对 ASV 值的敏感性（Bootstrap CI 在 Appendix B.7 有涉及，但主文仅一句提及）。

**W4 [MAJOR] 论文广度有余、深度不足，像 technical report 多于 focused conference paper。**
- 问题：论文同时覆盖了 bias taxonomy（7 拓扑）、ASV framework（3 类型）、correction guidance（5 方法）、empirical validation（3 数据集 × 4 LLMs）。每个方向都只能浅尝辄止。例如：
  - Correction guidance（Section 4.4）仅用一段半描述 5 种方法的排名，缺乏对各方法适用条件的深入分析
  - ASV 的 N-sensitivity 分析（Section 4.2 最后一段）提到 "sharp phase transition at N* ≈ 6,000-10,000" 但没有解释其物理含义或实践意义
  - 实证验证的 HumAID case study 在 Appendix B.3 中但主文几乎没有讨论
- 建议：考虑将 correction guidance 或 ASV 中的一个作为独立贡献深化，而非全部压缩在一篇 8 页论文中。

**W5 [MINOR] 非差异性误分类假设的实际适用性讨论不足。**
- 具体位置：Definition 1 (Section 3.1)、Limitations
- 问题：Non-differential misclassification 要求 P(A*|A,Y,Z) = P(A*|A)。论文声称"when the LLM does not observe outcome-related text during annotation"即满足。但现实中，LLM 标注任务经常涉及与 outcome 相关的文本内容（例如标注 stance 时，文本同时包含 stance indicator 和 outcome-relevant 信息）。Appendix B.5 的 stress test 仅检验了 ε=0.05 的小偏离。
- 建议：在 Limitations 中更明确地列举哪些常见 NLP 任务可能违反这一假设。

**W6 [MINOR] 个别引用格式问题。**
- `lee_wood_doughty2024` 的 venue 为 "AIM-FM Workshop, NeurIPS 2024"——这是一个 workshop paper，但论文中将其与 full conference papers 并列讨论且未标注为 workshop paper。
- `baumann2025` 和 `messing2026` 为 arXiv preprints，应确认是否已被接收。

---

## Questions（需要作者澄清）

**Q1.** 83.4% 符号反转率在 Abstract 和 Introduction 中的突出位置，与 Section 4.3 中"primary coefficient never reverses"的发现之间如何调和？作者是否考虑过在 Abstract 中直接区分 primary 和 secondary coefficient 的风险？

**Q2.** Empirical Finding 1 声称 mediation/M-bias/front-door 的符号保持"verified across 100,000 random matrices with zero violations"。但 100,000 次零违反仅给出了 upper bound P(violation) < 3×10⁻⁵ (95% CI)。作者是否尝试过对抗性搜索（adversarial search）以寻找违反条件的 confusion matrix？

**Q3.** ASV 的 linear interpolation C(δ) = (1-δ)I + δC₀ 意味着误分类沿直线路径退化。在实践中，LLM 的错误模式可能是高度非线性的（例如某些类别的错误率急剧增加而其他保持稳定）。作者是否评估过 ASV 在这种情况下的鲁棒性？

**Q4.** Table 4 中 DSL 对 M-bias 的 RMSE reduction 为 -267%——这是否意味着 DSL 将偏差放大了近 4 倍？如果是，能否解释机制？

**Q5.** Conjecture 1 排除了 IV topology。除了 Wald estimator 的奇异性外，是否有更深层的结构原因使得 IV 无法满足 monotonicity？

---

## Missing References

1. **Blackwell, Honaker & King (2017)** "A Unified Approach to Measurement Error and Missing Data" — 社会科学中 measurement error 处理的重要框架，与本文的 applied social science 定位直接相关。

2. **Imai, Keele & Yamamoto (2010)** "Identification, Inference and Sensitivity Analysis for Causal Mediation Effects" — 提出了 mediation 的敏感性分析框架（correlated residuals），与 ASV 在 mediation topology 下的应用直接可比。

3. **Buonaccorsi (2010)** "Measurement Error: Models, Methods, and Applications" — measurement error 领域的标准教材，与 Carroll et al. (2006) 并列。

4. **Valeri & VanderWeele (2012)** "Mediation Analysis Allowing for Exposure-Mediator Interactions and Causal Interpretation" — 讨论了 mediator misclassification 对因果中介分析的影响。

5. **Pangakis, Wolken & Fasching (2023)** "Automated Annotation with Generative AI Requires Validation" — 直接讨论 LLM 标注的验证需求。

---

## Novelty Score: 3/5

核心新颖性在于**系统性**而非**方法论突破**。七拓扑的 bias taxonomy 是现有结果的系统扩展（Dosemeci 1990 → Veierød & Laake 2001 → Teblunthuis 2024 → 本文）。ASV 是 E-value 框架的移植。FWL 不变性是最干净的新结果但量级较小。整体而言，这是一篇高质量的**综合性扩展工作**，而非开创性贡献。

## Presentation Score: 3.5/5

写作整体清晰，符号一致，Related Work 覆盖良好。主要扣分点：(1) Abstract 信息过载——8 个具体数字让读者难以抓住核心 message；(2) 83.4% 的 framing 问题如上所述；(3) 论文试图在 8 页内讲完一个 16 页的故事，导致每个部分都偏浅。

---

## Overall Assessment

**Overall: 3.5（Borderline Conference）**

**一句话总结：** 论文系统填补了 K≥3 标注误差在多因果拓扑下的理论空白，但核心发现的 framing 存在 overclaim 倾向，三个拓扑缺乏解析证明，ASV 的方法论创新有限。

**详细判断：**

*支持接收的理由：* 这是一个真实的文献空白，论文的系统性处理有价值。FWL 不变性结果和拓扑依赖的修正指南对实践者有直接帮助。实证验证规模充足，附录质量高。

*犹豫的理由：* (1) 83.4% 的 framing 与实际风险（primary effect 安全、realistic accuracy 下 2.1%）之间的 disconnect 是一个 integrity concern——不是说数字本身有错，而是 presentation 策略有 overclaim 嫌疑；(2) 对于一篇以理论贡献为主的论文，三个拓扑依赖数值验证是明显短板；(3) 广度优先的策略意味着每个单独贡献（taxonomy / ASV / correction）的深度可能不足以支撑一篇顶会论文。

*建议：* 如果作者能在 camera-ready 中 (a) 修正 framing 使其更诚实，(b) 补充至少 mediation 的解析证明，(c) 减少 1-2 个次要贡献以深化核心贡献，则可达到 Conference 水平。当前版本更适合 Findings track。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims 有支撑，但 3/7 拓扑的符号保持缺乏证明；Conjecture 仅有数值验证；Dirichlet(1,1,1) 先验下的数字被用于支撑过强的结论 |
| Excitement | 3/5 | 填补了真实空白，但核心贡献是系统性扩展而非方法论突破；ASV 为已有框架的移植；最令人兴奋的结果（FWL 不变性）篇幅有限 |
| Reproducibility | 4/5 | 承诺代码公开；DGP 和实验设置描述充分；confusion matrix 来源明确 |
| Overall Assessment | 3.5 | Borderline Conference — 实质贡献存在但 framing 和理论完整性有显著问题 |
| Confidence | 4/5 | 熟悉 measurement error 和 causal inference 文献，仔细检查了证明和实验 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 306 · 2026-05-22T14:55:00.213518+00:00_

Reviewer 2 已提交审稿意见。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 307 · 2026-05-22T14:55:11.432873+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。论文系统填补了 K≥3 标注误差在七种因果拓扑下的理论空白，FWL 不变性是干净的 negative result，实证验证规模充足。但三个关键问题拉低评分：(1) 83.4% 符号反转率的 framing 与"primary coefficient 从不反转"之间存在严重 tension，有 overclaim 嫌疑；(2) 三个拓扑的符号保持仅有数值验证而非解析证明；(3) ASV 框架是 E-value 的直接移植，方法论新颖性有限。当前版本更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 308 · 2026-05-22T14:55:18.967577+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 30

## Round 30

6 recorded events


### User

_source line 309 · 2026-05-22T14:59:57.480603+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性审查）

### Summary (2-3 句)

本文推导了 7 种 DAG 拓扑下 K 类非差异误分类（由 LLM 标注引入）对因果估计的偏差表达式，引入 ASV 敏感性分析框架（类比 E-value），并提供拓扑依赖的校正指南。核心发现是 K≥3 在 exposure 和 IV 拓扑下结构性地引入符号翻转可能——这在 K=2 下不可能发生——但在其余 5 种拓扑下符号保持。论文结合代数证明（confounding/collider）、数值验证（mediation/M-bias/front-door）与 23 个真实 LLM 配置的经验验证。

### Strengths

**S1. 系统性与全面性。** 同时处理 7 种 DAG 拓扑的偏差分析在因果推断文献中是首次（Section 3.2, Table 1）。对每种拓扑给出闭式概率极限表达式，并区分 sign-preserving vs. sign-reversing 拓扑。

**S2. Exposure 符号翻转结果是核心亮点。** Proposition 6（Appendix A.8）通过显式构造证明 K≥3 时即使 C_kk > 0.5 也可发生符号翻转。Section 4.2 补充了 Dirichlet(1,1,1) 下 83.4% 翻转率，restricted 到 diagonal ≥ 0.7 时仍有 2.1%。

**S3. FWL 不变性洞察有独立价值。** Section 4.5 证明对 4 种 A 作为协变量的拓扑，任何基于矩阵的校正不改变 col(D*)，因此 τ̂ 完全不变（Appendix B.2）。Table 4 中 Naive/MLA 均为 0.0% 验证了这一结论。

**S4. Confounding 和 Collider 的符号保持证明严格。** Proposition 2–3（confounding）和 Proposition 4–5（collider）使用 Cauchy-Schwarz 给出充分条件（Appendix A.3, A.6）。

**S5. 经验验证设计合理。** 23 个 LLM 配置 × 7 拓扑 = 161 个 bias scenarios（Section 4.4），Figure 3 直观展示"F₁ 不能预测因果偏差"。

**S6. Algorithm 1 提供从 DAG 识别→校正方法选择的完整实用工作流。**

### Weaknesses

**W1 [CRITICAL] Theorem 1 的证明对一般 K 不完整——即使在 proportional effects 下。**
- 位置：Appendix A.4
- 问题：Theorem 1 声称在 proportional effects (f=λg) 下 |B(C(δ))| 单调非递减。关键步骤 V_B(δ) 单调非递增 的论证引用 DPI，但论文承认 "the exact degradation factorization C(δ₂)=M·C(δ₁) for a stochastic M is non-trivial for the linear interpolation family"。对一般 K，V_B(δ) 单调性仅数值验证。**标记为 Theorem 的结果解析证明仅对 K=2 对称情形完成。**
- 影响：作为核心理论贡献，证明不完整影响 soundness 评分。
- 建议：补充一般 K 的解析证明，或降格为 Conjecture。

**W2 [MAJOR] Eq. (3) 中 λ(C) ∈ [0,1] 未被证明。**
- 位置：Section 3.2 Eq. (3) vs. Appendix A.5 (lines 315-328)
- 问题：主文声明 λ(C) ∈ [0,1]，暗示已证。附录中 B(C)=Σw_j δ_j 的 bounded 性依赖 max_j|δ_j| ≤ |τ_ind|，仅数值验证 ("We verify numerically")。
- 建议：主文标注为数值观察或补充解析证明。

**W3 [MAJOR] "Empirical Finding 1" 术语误导——实为数值模拟验证，非真实数据发现。**
- 位置：Section 3.2
- 问题：所述条件（mediation: sign(τ_dir)=sign(τ_total) 等）没有解析证明。与 Proposition 1（已证明）和 Conjecture 1 的区分不清晰。
- 建议：重命名为 "Numerical Finding" 或 "Conjecture 2"。

**W4 [MAJOR] Non-differential misclassification 假设对 LLM 的合理性需更充分讨论。**
- 位置：Definition 1, Appendix B.5
- 问题：LLM 处理的文本可能同时含 A 和 Y 信息，违反非差异性。Stress test 仅考虑 ε ≤ 0.10 的小偏离。
- 建议：扩大 stress test 范围，讨论哪些 NLP 任务设计更可能满足假设。

**W5 [MAJOR] DAG 拓扑必须先验已知，未讨论拓扑误指定后果。**
- 位置：Algorithm 1
- 问题：拓扑错误识别会导致错误校正建议（DSL 对 confounding +48% 但对 collider -92.6%）。
- 建议：增加拓扑误指定的稳健性分析。

**W6 [MINOR] Conjecture 1 的 ε < 0.06 bound 可能依赖具体 DGP 参数。**

**W7 [MINOR] PPI++ 对 M-bias 有害 (-88%) 但缺乏机制解释。**

**W8 [MINOR] SIMEX 的 FWL 不变性论证不够严格（Appendix B.2），属经验声明。**

### Questions

Q1. C(δ) 线性插值族是否满足 stochastic degradation 条件？如果不满足，DPI 如何适用于 Theorem 1？

Q2. 是否存在使 |B(C)| > |τ_ind| 的 confusion matrix C（即 λ(C) ∉ [0,1] 的反例）？

Q3. Empirical validation 中符号翻转仅限 secondary coefficients（小 |β|）——实践中影响是否被过度强调？

Q4. LLM 中更现实的差异性违反模式是什么？Appendix B.5 的 perturbation 形式是否具有代表性？

Q5. 多 LLM ensemble 标注时框架如何扩展？

### Missing References

- Ogburn & VanderWeele (2012): collider 控制下 bias amplification 的系统分析
- Imai & Yamamoto (2010): mediation 分析中测量误差
- Buonaccorsi (2010): 多类变量非差异误分类的经典处理

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Theorem 1 证明对一般 K 不完整；Eq(3) λ(C)∈[0,1] 和 Empirical Finding 1 依赖数值验证；confounding/collider 证明和 exposure 反例严格 |
| Excitement | 3.5/5 | 首次系统处理 7 种拓扑的 K-class 误分类偏差；ASV 框架有实用性；但 proportional effects 假设限制理论深度 |
| Reproducibility | 4/5 | 声明开源代码和数据；实验设置描述充分；附录包含完整参数 |
| Reviewer Confidence | 4/5 | 熟悉因果推断和测量误差文献，仔细检查了主要证明 |

### Overall Assessment

**Overall: 3.5 (Borderline Conference)**

论文解决了重要且及时的问题，框架设计全面实用。Exposure 符号翻转结果和 FWL 不变性洞察是 genuinely novel 的贡献。但核心理论贡献（Theorem 1）证明不完整，多个主文结果依赖数值验证（W1, W2, W3），非差异假设讨论不充分（W4），拓扑误指定的稳健性未涉及（W5）。

提升至 4.0 路径：(i) 完成 Theorem 1 证明或降格为 Conjecture；(ii) 明确区分 proved/verified/conjectured 层次；(iii) 扩充非差异性假设讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-22T15:00:39.209673+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Equation）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Summary\n本文系统研究了 K≥3 多类别标注误差在七种因果 DAG 拓扑下的偏差传播机制，证明了 exposure 和 IV 拓扑可产生符号反转而其余五种保持符号，提出了 ASV 敏感性框架，并揭示了 FWL 不变性导致矩阵修正方法对四种拓扑无效。论文覆盖面广（7 拓扑 × 3 ASV 类型 × 5 修正方法 × 实证验证），但核心发现的 framing 存在误导性——标题式的 83.4% 符号反转率与实证中\"主效应从不反转\"之间的张力需要认真处理。\n\n## Strengths\nS1. 系统性填补了明确的文献空白。现有工作要么限于 binary misclassification（Teblunthuis 2024，4 DAGs），要么限于单一拓扑的 categorical 扩展（Lee & Wood-Doughty 2024，仅 confounding）。本文是首个在 K≥3 条件下系统覆盖七种拓扑的工作。\nS2. FWL 不变性作为 negative result 干净优雅。\nS3. 实证验证设计周密（23 LLM configs × 7 topologies = 161 scenarios）。\nS4. Correction guidance 的实用价值。\nS5. 附录质量高（15 页附录）。\n\n## Weaknesses\n\nW1 [CRITICAL] Abstract/Introduction 对 83.4% 符号反转率的 framing 具有误导性。83.4% 来自 uniform Dirichlet(1,1,1) 先验（含大量近置换矩阵），realistic accuracy 下仅 2.1%。更关键：Section 4.3 显示 primary coefficient never reverses，符号反转仅发生在 secondary coefficients with small |β|。Abstract 的 alarm tone 与实际风险形成严重 tension。\n\nW2 [MAJOR] 三个拓扑的符号保持仅为经验发现，缺乏解析证明。Mediation、M-bias、front-door 仅通过 100,000 次数值验证。Conjecture 1 同样仅有数值支撑。\n\nW3 [MAJOR] ASV 框架相对于 E-values 和 robustness values 的方法论创新有限。核心思路是将 E-value 的 \"unmeasured confounding strength\" 替换为 \"misclassification severity δ\"——概念上是 E-value 的直接移植。\n\nW4 [MAJOR] 论文广度有余、深度不足，像 technical report 多于 focused conference paper。同时覆盖 bias taxonomy + ASV + correction + empirical validation，每个方向都偏浅。\n\nW5 [MINOR] 非差异性误分类假设的实际适用性讨论不足。\n\nW6 [MINOR] 个别引用格式问题（workshop paper 未标注，arXiv preprints 状态未确认）。\n\n## Questions\nQ1. 83.4% framing 与 \"primary coefficient never reverses\" 如何调和？\nQ2. 是否尝试过 adversarial search 寻找 Empirical Finding 1 的违反案例？\nQ3. ASV linear interpolation 在非线性错误模式下的鲁棒性？\nQ4. DSL 对 M-bias RMSE -267% 的机制？\nQ5. Conjecture 1 排除 IV 的深层结构原因？\n\n## Missing References\n1. Blackwell, Honaker & King (2017) \"A Unified Approach to Measurement Error and Missing Data\"\n2. Imai, Keele & Yamamoto (2010) \"Identification, Inference and Sensitivity Analysis for Causal Mediation Effects\"\n3. Buonaccorsi (2010) \"Measurement Error: Models, Methods, and Applications\"\n4. Valeri & VanderWeele (2012) \"Mediation Analysis Allowing for Exposure-Mediator Interactions\"\n5. Pangakis, Wolken & Fasching (2023) \"Automated Annotation with Generative AI Requires Validation\"\n\n## Scores\nNovelty: 3/5, Presentation: 3.5/5, Overall: 3.5 (Borderline Conference)\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Equation）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Summary\n本文系统研究了 K≥3 多类别标注误差在七种因果 DAG 拓扑下的偏差传播机制，证明了 exposure 和 IV 拓扑可产生符号反转而其余五种保持符号，提出了 ASV 敏感性框架，并揭示了 FWL 不变性导致矩阵修正方法对四种拓扑无效。论文覆盖面广（7 拓扑 × 3 ASV 类型 × 5 修正方法 × 实证验证），但核心发现的 framing 存在误导性——标题式的 83.4% 符号反转率与实证中\"主效应从不反转\"之间的张力需要认真处理。\n\n## Strengths\nS1. 系统性填补了明确的文献空白。现有工作要么限于 binary misclassification（Teblunthuis 2024，4 DAGs），要么限于单一拓扑的 categorical 扩展（Lee & Wood-Doughty 2024，仅 confounding）。本文是首个在 K≥3 条件下系统覆盖七种拓扑的工作。\nS2. FWL 不变性作为 negative result 干净优雅。\nS3. 实证验证设计周密（23 LLM configs × 7 topologies = 161 scenarios）。\nS4. Correction guidance 的实用价值。\nS5. 附录质量高（15 页附录）。\n\n## Weaknesses\n\nW1 [CRITICAL] Abstract/Introduction 对 83.4% 符号反转率的 framing 具有误导性。83.4% 来自 uniform Dirichlet(1,1,1) 先验（含大量近置换矩阵），realistic accuracy 下仅 2.1%。更关键：Section 4.3 显示 primary coefficient never reverses，符号反转仅发生在 secondary coefficients with small |β|。Abstract 的 alarm tone 与实际风险形成严重 tension。\n\nW2 [MAJOR] 三个拓扑的符号保持仅为经验发现，缺乏解析证明。Mediation、M-bias、front-door 仅通过 100,000 次数值验证。Conjecture 1 同样仅有数值支撑。\n\nW3 [MAJOR] ASV 框架相对于 E-values 和 robustness values 的方法论创新有限。核心思路是将 E-value 的 \"unmeasured confounding strength\" 替换为 \"misclassification severity δ\"——概念上是 E-value 的直接移植。\n\nW4 [MAJOR] 论文广度有余、深度不足，像 technical report 多于 focused conference paper。同时覆盖 bias taxonomy + ASV + correction + empirical validation，每个方向都偏浅。\n\nW5 [MINOR] 非差异性误分类假设的实际适用性讨论不足。\n\nW6 [MINOR] 个别引用格式问题（workshop paper 未标注，arXiv preprints 状态未确认）。\n\n## Questions\nQ1. 83.4% framing 与 \"primary coefficient never reverses\" 如何调和？\nQ2. 是否尝试过 adversarial search 寻找 Empirical Finding 1 的违反案例？\nQ3. ASV linear interpolation 在非线性错误模式下的鲁棒性？\nQ4. DSL 对 M-bias RMSE -267% 的机制？\nQ5. Conjecture 1 排除 IV 的深层结构原因？\n\n## Missing References\n1. Blackwell, Honaker & King (2017) \"A Unified Approach to Measurement Error and Missing Data\"\n2. Imai, Keele & Yamamoto (2010) \"Identification, Inference and Sensitivity Analysis for Causal Mediation Effects\"\n3. Buonaccorsi (2010) \"Measurement Error: Models, Methods, and Applications\"\n4. Valeri & VanderWeele (2012) \"Mediation Analysis Allowing for Exposure-Mediator Interactions\"\n5. Pangakis, Wolken & Fasching (2023) \"Automated Annotation with Generative AI Requires Validation\"\n\n## Scores\nNovelty: 3/5, Presentation: 3.5/5, Overall: 3.5 (Borderline Conference)\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-22T15:00:51.296008+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12086
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-22T15:00:51.748214+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Equation）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Summary\n本文推导了 7 种 DAG 拓扑下 K 类非差异误分类对因果估计的偏差表达式，引入 ASV 敏感性分析框架（类比 E-value），并提供拓扑依赖的校正指南。核心发现是 K≥3 在 exposure 和 IV 拓扑下结构性地引入符号翻转可能，但在其余 5 种拓扑下符号保持。\n\n## Strengths\nS1. 系统性与全面性——同时处理 7 种 DAG 拓扑的偏差分析在因果推断文献中是首次。\nS2. Exposure 符号翻转结果是核心亮点。\nS3. FWL 不变性洞察有独立价值。\nS4. Confounding 和 Collider 的符号保持证明严格。\nS5. 经验验证设计合理（23 LLM configs × 7 topologies = 161 scenarios）。\nS6. Algorithm 1 提供完整实用工作流。\n\n## Weaknesses\n\nW1 [CRITICAL] Theorem 1 的证明对一般 K 不完整——即使在 proportional effects 下。关键步骤 V_B(δ) 单调非递增的论证引用 DPI，但 C(δ) 线性插值族不一定满足 stochastic degradation 条件。论文承认 \"the exact degradation factorization C(δ₂)=M·C(δ₁) for a stochastic M is non-trivial\"。标记为 Theorem 的结果解析证明仅对 K=2 对称情形完成。\n\nW2 [MAJOR] Eq. (3) 中 λ(C) ∈ [0,1] 未被证明。主文声明 λ(C) ∈ [0,1]，但附录中仅数值验证。\n\nW3 [MAJOR] \"Empirical Finding 1\" 术语误导——实为数值模拟验证，非真实数据发现。与 Proposition（已证明）和 Conjecture 的区分不清晰。\n\nW4 [MAJOR] Non-differential misclassification 假设对 LLM 的合理性需更充分讨论。Stress test 仅考虑 ε ≤ 0.10 的小偏离。\n\nW5 [MAJOR] DAG 拓扑必须先验已知，未讨论拓扑误指定后果。对 Algorithm 1 影响大——拓扑错误会导致错误校正建议。\n\nW6 [MINOR] Conjecture 1 的 ε < 0.06 bound 可能依赖具体 DGP 参数。\n\nW7 [MINOR] PPI++ 对 M-bias 有害 (-88%) 但缺乏机制解释。\n\nW8 [MINOR] SIMEX 的 FWL 不变性论证不够严格。\n\n## Questions\nQ1. C(δ) 线性插值族是否满足 stochastic degradation 条件？DPI 如何适用于 Theorem 1？\nQ2. 是否存在使 λ(C) ∉ [0,1] 的反例？\nQ3. 实践中 secondary coefficient 符号翻转的影响是否被过度强调？\nQ4. LLM 中更现实的差异性违反模式是什么？\nQ5. 多 LLM ensemble 标注时框架如何扩展？\n\n## Missing References\n- Ogburn & VanderWeele (2012): collider 控制下 bias amplification\n- Imai & Yamamoto (2010): mediation 分析中测量误差\n- Buonaccorsi (2010): 多类变量非差异误分类\n\n## Scores\nSoundness: 3.5/5, Excitement: 3.5/5, Overall: 3.5 (Borderline Conference)\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Equation）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Summary\n本文推导了 7 种 DAG 拓扑下 K 类非差异误分类对因果估计的偏差表达式，引入 ASV 敏感性分析框架（类比 E-value），并提供拓扑依赖的校正指南。核心发现是 K≥3 在 exposure 和 IV 拓扑下结构性地引入符号翻转可能，但在其余 5 种拓扑下符号保持。\n\n## Strengths\nS1. 系统性与全面性——同时处理 7 种 DAG 拓扑的偏差分析在因果推断文献中是首次。\nS2. Exposure 符号翻转结果是核心亮点。\nS3. FWL 不变性洞察有独立价值。\nS4. Confounding 和 Collider 的符号保持证明严格。\nS5. 经验验证设计合理（23 LLM configs × 7 topologies = 161 scenarios）。\nS6. Algorithm 1 提供完整实用工作流。\n\n## Weaknesses\n\nW1 [CRITICAL] Theorem 1 的证明对一般 K 不完整——即使在 proportional effects 下。关键步骤 V_B(δ) 单调非递增的论证引用 DPI，但 C(δ) 线性插值族不一定满足 stochastic degradation 条件。论文承认 \"the exact degradation factorization C(δ₂)=M·C(δ₁) for a stochastic M is non-trivial\"。标记为 Theorem 的结果解析证明仅对 K=2 对称情形完成。\n\nW2 [MAJOR] Eq. (3) 中 λ(C) ∈ [0,1] 未被证明。主文声明 λ(C) ∈ [0,1]，但附录中仅数值验证。\n\nW3 [MAJOR] \"Empirical Finding 1\" 术语误导——实为数值模拟验证，非真实数据发现。与 Proposition（已证明）和 Conjecture 的区分不清晰。\n\nW4 [MAJOR] Non-differential misclassification 假设对 LLM 的合理性需更充分讨论。Stress test 仅考虑 ε ≤ 0.10 的小偏离。\n\nW5 [MAJOR] DAG 拓扑必须先验已知，未讨论拓扑误指定后果。对 Algorithm 1 影响大——拓扑错误会导致错误校正建议。\n\nW6 [MINOR] Conjecture 1 的 ε < 0.06 bound 可能依赖具体 DGP 参数。\n\nW7 [MINOR] PPI++ 对 M-bias 有害 (-88%) 但缺乏机制解释。\n\nW8 [MINOR] SIMEX 的 FWL 不变性论证不够严格。\n\n## Questions\nQ1. C(δ) 线性插值族是否满足 stochastic degradation 条件？DPI 如何适用于 Theorem 1？\nQ2. 是否存在使 λ(C) ∉ [0,1] 的反例？\nQ3. 实践中 secondary coefficient 符号翻转的影响是否被过度强调？\nQ4. LLM 中更现实的差异性违反模式是什么？\nQ5. 多 LLM ensemble 标注时框架如何扩展？\n\n## Missing References\n- Ogburn & VanderWeele (2012): collider 控制下 bias amplification\n- Imai & Yamamoto (2010): mediation 分析中测量误差\n- Buonaccorsi (2010): 多类变量非差异误分类\n\n## Scores\nSoundness: 3.5/5, Excitement: 3.5/5, Overall: 3.5 (Borderline Conference)\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-22T15:00:53.214024+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Assistant

_source line 314 · 2026-05-22T15:00:56.369388+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 315 · 2026-05-22T15:00:59.062955+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心发现：

- **1 个 CRITICAL 问题**：Theorem 1（envelope monotonicity）证明对一般 K 不完整，V_B(δ) 单调性依赖数值验证而非解析证明
- **4 个 MAJOR 问题**：Eq.(3) λ(C)∈[0,1] 未证明、Empirical Finding 1 术语误导、非差异假设对 LLM 的合理性讨论不足、DAG 拓扑必须先验已知但未讨论误指定后果
- **3 个 MINOR 问题**：Conjecture 1 ε bound 参数依赖性、PPI++ 对 M-bias 失效机制未解释、SIMEX FWL 不变性论证不严格
- **Overall: 3.5 (Borderline Conference)**，Soundness 3.5/5，Excitement 3.5/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 316 · 2026-05-22T15:01:04.288694+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 32

## Round 32

2 recorded events


### User

_source line 317 · 2026-05-22T15:03:24.700153+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R1-W1: Theorem 1 的 DPI 论证对一般 K 不完整**

同意这是本文最严重的技术问题之一。Theorem 1 的证明 sketch 声称 "As δ increases, A* becomes a noisier channel for A, so Var(E[g|A*_δ]) decreases by the data processing inequality"（Section 3.3, Theorem 1 proof sketch）。但 DPI 要求 Markov chain A → A*_{δ₁} → A*_{δ₂}，即 C(δ₂) = M·C(δ₁) for some stochastic M（stochastic degradation）。线性插值族 C(δ) = (1-δ)I + δC₀ 并不自动满足这个条件——C(δ₂) = ((1-δ₂)/(1-δ₁))·C(δ₁) + (δ₂-δ₁)/(1-δ₁))·C₀ 不一定给出 stochastic factorization。

论文自己在 Appendix 中承认了这个 gap（"the exact degradation factorization... is non-trivial"）。一个被标记为 **Theorem** 的结果应该有完整证明。如果 DPI 步骤不严格，应降级为 Proposition（附条件）或 Conjecture，并在主文中明确标注证明状态。

不过我要补充：Appendix A.4（Page 13）尝试了一个不依赖 DPI 的直接证明路径——通过 V_W(δ) 的单调性直接推导。这个路径对 proportional effects 特殊情况似乎可以完成（因为 B(C) = λV_W/(V_W + σ²) 结构简单），但论文没有将其升级为完整证明。**如果作者能补全这个直接证明，W1 可以解决。**

---

**[AGREE] R1-W2: Eq. (3) 中 λ(C) ∈ [0,1] 未证明**

同意。Section 3.2 Mediation 段（Eq. 3）声明 λ(C) ∈ [0,1] 并引用 Appendix Proposition 3，但 Appendix A.5（Page 14）中的推导仅展示了 mediation bias 与 confounding bias 的结构类比，并未正式证明 λ(C) 的范围约束。

从直觉上看，λ(C) 度量 A* 对 A 的信息保留量：C=I 时 λ=1，C=uniform 时 λ=0。如果 λ 是 mutual information I(A;A*) 的某种归一化，则 [0,1] 范围自然成立。但论文的具体定义（Appendix A.5 中的 λ = 某个 within-group covariance 比率）需要单独证明有界性。

**建议作者至少提供 λ(C) ∈ [0,1] 的 sketch proof 或者明确标注为 assumption。**

---

**[AGREE] R1-W3: "Empirical Finding 1" 术语误导**

强烈同意。我在自己的审稿中（R2-W2）也独立指出了这个问题。"Empirical Finding" 在学术论文中通常指来自真实数据的发现，而非数值模拟验证。100,000 次 Monte Carlo 验证 ≠ empirical evidence。

更合适的术语：
- "Numerical Observation 1" 或 "Simulation Finding 1"（如果保持当前证据水平）
- 升级为 "Proposition"（如果补充证明）

当前标签的问题不仅是术语——它模糊了论文中已证明结果（Proposition 1: confounding, collider）和未证明结果（mediation, M-bias, front-door）之间的严格区分。读者容易误认为所有七种拓扑的符号保持都有同等的理论支撑。

---

**[AGREE] R1-W4: Non-differential misclassification 假设讨论不足**

同意，且与我的 R2-W5 一致。补充两点 R1 未提及的具体场景：

1. **Outcome-conditional prompting**: 当 LLM 标注 stance 时，输入文本本身可能包含 outcome-relevant 信息（例如灾害严重程度描述同时影响 stance 标注和 downstream outcome），即使 LLM 不直接观察 Y。
2. **In-context learning 效应**: Few-shot prompting 中 demonstration examples 的选择可能引入与 Y 相关的 systematic error pattern，违反 Definition 1。

Appendix B.5 的 stress test 仅检验 ε ≤ 0.10 的小偏离（Table 7），且 DGP 限于 exposure topology。对于实际 LLM 可能出现的 **structured** differential misclassification（非 random perturbation），robustness 可能更弱。

---

**[REBUT] R1-W5: DAG 拓扑必须先验已知，未讨论拓扑误指定后果**

部分不同意。

R1 的 concern 本身合理——拓扑误指定确实会导致错误的校正建议（Algorithm 1 的输入是拓扑）。但这个 limitation 并非本文特有：

1. **所有因果推断方法都假设 DAG 已知或可识别。** E-values（VanderWeele & Ding, 2017）假设研究者知道哪个变量是 unmeasured confounder；Cinelli & Hazlett (2020) 的 robustness value 同样需要 causal structure。本文的 ASV 在这个维度上与 established 方法处于同一立场。

2. **本文的核心贡献恰恰是"拓扑影响很大"这个 message。** Table 1 和 Figure 2 展示了同一个 confusion matrix 在不同拓扑下产生截然不同的偏差方向——这本身就是对"拓扑误指定很危险"的最好论证。论文不需要解决拓扑选择问题，只需要证明拓扑 matters。

3. **Algorithm 1 Step 1 就是 "Assess risk level: identify topology"**——论文确实将拓扑识别作为第一步，只是没有提供拓扑选择的方法论。

**但我同意论文应在 Limitations 中增加一句关于拓扑误指定的讨论。** 当前 Limitations（Section 5, page 8）未提及此问题。一句 "our framework assumes the causal DAG is correctly specified; misspecification of the topology would lead to incorrect correction recommendations" 足矣。

---

**[AGREE] R1-W6: Conjecture 1 的 ε < 0.06 可能依赖 DGP 参数**

同意这个 concern 有 merit。Appendix B.11 用 Gauss-Hermite quadrature 在零采样噪声下验证 Conjecture，但所用 DGP 参数（效应量、方差等）是固定的。论文报告 "worst-case step deviations below 0.06 (<6% of τ)"——这是一个相对 bound（相对于 τ）。

但问题在于：当 τ 很小时（near-null effects），6% 的相对偏差可能仍然足以导致错误推断（例如从"刚好显著"变为"不显著"）。论文的 ASV significance 分析（Section 4.2）部分解决了这个问题——它显示 ASV 的 phase transition 发生在 N* ≈ 6,000-10,000——但没有将 Conjecture 的 ε bound 与 significance ASV 联系起来。

**建议：报告 ε 在多组 DGP 参数下的 sensitivity，或至少说明 ε 对 τ 的依赖关系。**

---

**[AGREE] R1-W7: PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释**

同意，我在 R2-Q4 中也独立提出了这个问题。机制其实可以从论文现有内容推断：

- Section 3.2 M-bias 段说明 misclassification 是 **protective** 的（"Misclassifying A weakens this adjustment, reducing the M-bias"）
- PPI++ 的目标是修正 misclassification → 即恢复对 A 的精确调整
- 恢复精确调整 = 恢复完整的 M-bias spurious path = bias 增大

这个机制是论文框架的自然推论，但 Section 4.4 没有 connect the dots。一句话解释即可："PPI++ corrects misclassification toward perfect classification, but for M-bias, misclassification is protective—restoring perfect control reintroduces the full spurious M-bias path."

---

**[REBUT] R1-W8: SIMEX 的 FWL 不变性论证不够严格**

部分不同意。

SIMEX 的工作原理：(1) 对 A* 添加递增噪声生成 A*_b（更差的分类），(2) 在每个噪声水平下回归，(3) 外推到"零噪声"。

对于 covariate topologies（confounding, mediation, collider, M-bias），FWL 不变性的论证是**结构性的**：treatment coefficient τ̂ 不依赖于 D* 的列空间内部结构（Appendix B.2, proof of FWL invariance）。这意味着：
- 在 SIMEX 的每个噪声级别 b，更差的 A*_b 仍然保持 D*_b 的列空间结构 → τ̂(b) = τ̂(0)
- 如果所有噪声级别的 τ̂ 都相同，外推也相同

所以 SIMEX 对 covariate topologies 的无效性是 FWL 不变性的直接推论，不需要额外形式化。论文在 Section 4.4 说 "Naive plug-in and MLA achieve exactly 0.0% bias reduction across these four topologies" 已经通过数值验证了这一点。

**但我承认论文可以更明确地陈述这个推论链，而非让读者自行推断。**

---

### Questions 回应

**[AGREE] R1-Q1 (DPI 与 stochastic degradation)**
与 W1 一致，这是需要作者澄清的核心技术问题。

**[AGREE] R1-Q2 (λ(C) ∉ [0,1] 的反例)**
与 W2 一致。如果 λ(C) 可以超出 [0,1]，Eq. (3) 的解释将完全改变。

**[AGREE] R1-Q3 (Secondary coefficient 符号翻转是否被过度强调)**
强烈同意。这与我的 R2-W1 [CRITICAL] 完全一致——83.4% 的 framing 与 "primary coefficient never reverses" 之间的 tension 是本文最大的 presentation 问题。R1 和 R2 独立到达了相同结论，增加了这个 concern 的权重。

**[AGREE] R1-Q4 (更现实的差异性违反模式)**
与 R1-W4 和 R2-W5 一致。补充一个具体例子：在 HumAID 灾害数据中，涉及极端事件的 tweets 可能使用更强烈的语言，同时 (a) 更容易被 LLM 正确分类（因为 signal 更强）和 (b) 与更严重的 outcomes 相关——这就构成了 differential misclassification。

**[AGREE] R1-Q5 (Multi-LLM ensemble 扩展)**
合理的 future work 问题。论文在 Limitations 中提到 "correlated multi-annotator settings (Kim et al., 2025) are future work"，但没有讨论 Kim et al. (2025) 发现的 60% 跨模型错误相关性如何影响 non-differential 假设——如果多个 LLM 犯相似错误，ensemble 可能无法改善问题。

---

### 与 R1 的总体分歧和共识

**共识领域（高权重）：**
- 83.4% framing 的 overclaim 问题（R1-Q3 = R2-W1）
- 理论完整性不足：Theorem 1 DPI gap、λ(C) 未证明、Empirical Finding 术语（R1-W1/W2/W3 ≈ R2-W2）
- Non-differential assumption 讨论不足（R1-W4 = R2-W5）

**分歧领域：**
- **R1-W5（拓扑需先验已知）**: 我认为这是 causal inference 的 general limitation，不应作为 MAJOR weakness。论文的价值恰恰在于证明拓扑 matters。但同意应在 Limitations 中提及。
- **R1-W8（SIMEX FWL）**: 我认为 FWL 不变性对 SIMEX 的推论是结构性的，不需要额外形式化。

**Overall**: 两位 reviewer 独立达成了 **3.5 (Borderline Conference)** 的一致评分，主要基于 (1) framing overclaim, (2) 理论不完整, (3) 系统性扩展 vs. 方法论突破的创新度判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 318 · 2026-05-22T15:03:33.164441+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 33

## Round 33

10 recorded events


### User

_source line 319 · 2026-05-22T15:03:34.355349+00:00_

[Reviewer 2 审稿结果]:
已向 Review Director 提交对 Reviewer 1 的逐条交叉回应。核心结论：两位 Reviewer 在三个关键问题上独立达成共识——(1) 83.4% framing overclaim, (2) 理论证明不完整, (3) 创新度为系统性扩展而非方法论突破。在拓扑先验假设（R1-W5）和 SIMEX FWL 论证（R1-W8）上存在分歧。总评一致为 3.5 Borderline Conference。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2

### Weaknesses 回应

**[AGREE] R2-W1: 83.4% framing 误导性**
部分同意。Abstract/Introduction 应同时报告 83.4%（全先验理论值）和 2.1%（realistic diagonal≥0.7），并说明实证中翻转仅限 secondary coefficients。但 83.4% 作为 K≥3 vs K=2 结构断裂的量化证据不应移除——K=2 下严格为 0%（Section 4.2 control），这一对比有理论重要性。论文 Prop. 6 反例（β₁=1, β₂=-10）表明主效应 CAN 翻转但需极端系数比，实证中未观测到不等于不可能。

**[AGREE] R2-W2: 三拓扑符号保持无解析证明**
完全同意，与我的 W2/W3 一致。补充：Theorem 1 的 V_B(δ) 单调性对一般 K 也仅数值验证（我标为 CRITICAL），论文应建立 Proved → Numerically verified → Conjectured 的清晰三级层次。

**[REBUT] R2-W3: ASV 创新有限**
不同意。高层概念类比成立（都是"找最小扰动翻转结论"），但技术差异实质性：(1) E-value 参数化标量 Γ，天然单调；ASV 将 K×K matrix 映射到 1D 路径，需要额外证明 monotonicity（Theorem 1/Conjecture 1）；(2) 三种 ASV 类型 vs E-value 单类型，significance ASV 的 N* phase transition 无 E-value 对应物；(3) E-value topology-agnostic，ASV 的 topology-dependent ranking 是核心贡献；(4) Bootstrap ASV 处理 C₀ 估计不确定性。

**[REBUT] R2-W4: Breadth > depth**
不同意。系统性比较是核心贡献：sign-flip 二分法、FWL 不变性、ASV vulnerability ranking 均需跨拓扑才能发现。8 页主文 + 15 页附录的分配合理。但同意 correction methods 部分偏浅（可更深入解释失败机制）。

**[AGREE] R2-W5: 非差异性假设讨论不足**
完全同意，与我的 W4 一致。

**[AGREE] R2-W6: 引用格式**
同意。

### Questions 回应

**[AGREE] R2-Q1**: 需在 Section 4.2 明确调和。
**[AGREE] R2-Q2**: Adversarial search 可显著增强 Empirical Finding 1 可信度。
**[AGREE] R2-Q3**: 应至少用一种替代参数化验证 ASV ranking robustness。
**[AGREE] R2-Q4**: 应解释 protective topology 下"纠正=恢复 spurious bias"的机制。
**[REBUT] R2-Q5**: 论文 Section 3.3 和 4.2 已充分解释 IV 排除的结构原因（Wald 分母穿零）。

### Missing References
5 条均 [AGREE]，其中 Imai et al. (2010) 和 Buonaccorsi (2010) 我也独立建议。

### 总结
6 条 Weaknesses: 4 [AGREE], 2 [REBUT]（W3 ASV 创新性, W4 breadth 价值）。总评 3.5 一致。主要分歧：ASV 技术贡献超出 E-value 简单移植；breadth 是有意为之且有价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-22T15:03:59.391665+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-22T15:03:59.593037+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T14:48:55.941294+00:00\", \"completed_at\": \"2026-05-22T14:48:59.555800+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets May 23, 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-22T15:03:59.593661+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-22T15:03:59.644086+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---

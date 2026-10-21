# Director coordination — Part 2 of 14

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/46/46a4a073b0cc4314da71.json)

## Round 33

### Tool result

_source line 351 · 2026-05-17T13:53:16.160632+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-17T13:53:20.727764+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 353 · 2026-05-17T13:53:20.728241+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-17T13:53:25.746864+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,request_external_review,get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,request_external_review,get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-17T13:53:25.797393+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-17T13:53:32.022560+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-17T13:53:32.023001+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-17T13:53:37.383219+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-17T13:53:38.236927+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (50 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_048_cross_temp_transfer | Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters | — | — | — |\n\n## 待处理\n- multi_domain_t07（准备中）\n- review-exp-a-baseline-ensemble: 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异（准备中）\n- plan-004-prep: Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）（准备中）\n- plan-001-restore（准备中）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **exp_047_multi_domain_t07** (success): Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers ← 基于 exp_043_multi_domain_seeds\n- **multi-domain-seeds** (success): Domain independence: depth fingerprint 的 differential
…[truncated 841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-17T13:53:38.237290+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-17T13:53:38.790763+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-17T13:53:49.728727+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information related to EMNLP 2026, though the specific main conference call for papers wasn't directly returned. Here'
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 11491
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-17T13:53:49.729327+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml\", \"content\": \"# Literature Map for gen-depth-fingerprint\\n# 递归 LLM 生成链深度指纹识别\\n# Updated: 2026-05-15\\n# Categories: detection, model-collapse, data-quality, stylometry,\\n#             iterative-generation, watermarking, vocabulary-diversity,\\n#             membership-inference, ood-detection, survey\\n# Total: 39 papers\\n\\n##############################################################################\\n# 1. Perplexity-based / Zero-shot Detection\\n##############################################################################\\n\\n- id: detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Mitchell et al.\\\"\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  arxiv: \\\"2301.11305\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补\\\"\\n  key_finding: \\\"机器生成文本倾向于占据模型 log-probability 函数的负曲率区域\\\"\\n\\n- id: gltr\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: \\\"Gehrmann et al.\\\"\\n  year: 2019\\n  venue: \\\"ACL 2019\\\"\\n  arxiv: \\\"1906.04043\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化\\\"\\n  key_finding: \\\"使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%\\\"\\n\\n- id: dna_gpt\\n  title: \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\"\\n  authors: \\\"Yang et al.\\\"\\n  year: 2024\\n  venue: \\\"ICLR 2024\\\"\\n  arxiv: \\\"2305.17359\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析\\\"\\n  key_finding: \\\"截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测\\\"\\n\\n- id: binoculars\\n  tit
…[truncated 1705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10938
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-17T13:53:54.613714+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit template format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit template format requirements"
  }
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-17T13:53:55.817866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-17T13:53:55.818235+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{lineno}
11	\linenumbers
12	
13	\graphicspath{{../chart/}}
14	
15	\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\in Non-Paraphrastic LLM Text Chains}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{results}
28	
29	\input{discussion}
30	\input{conclusion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\appendix
37	
38	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
39	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
40	
41	\input{appendix_dataset_stats}
42	
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{End-to-End Depth Classification (QLoRA)}
56	\label{app:qlora}
57	\input{appendix_qlora}
58	
59	\section{Leave-One-Feature-Out Analysis}
60	\label{app:lofo}
61	\input{appendix_lofo}
62	
63	\section{Confusion Matrix}
64	\label{app:confusion}
65	\input{appendix_confusion_matrix}
66	
67	\section{Classifier Sensitivity}
68	\label{app:classifier}
69	\input{appendix_classifier}
70	
71	\section{Robustness to Text Perturbation}
72	\label{app:human-edit}
73	\input{appendix_human_edit}
74	
75	\section{Cross-Domain Generalization}
76	\label{app:domain}
77	\input{appendix_domain}
78	
79	\section{Error Analysis of B
…[truncated 51 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-17T13:54:00.736947+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit template format requirements"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026:

## Page Limits

ARR submissions are in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). The page limits are 8 for long papers and 4 for short papers, not including limitations and ethical considerations.

## Format Requirements

All long, 
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6123
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-17T13:54:05.213820+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"aclrollingreview.org\" ARR CFP 2026 long paper 8 pages anonymity supplementary material"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"aclrollingreview.org\" ARR CFP 2026 long paper 8 pages anonymity supplementary material"
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-17T13:54:05.665619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": "80",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "offset": "80",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-17T13:54:05.716206+00:00_

80	\label{app:error-analysis}
81	\input{appendix_error_analysis}
82	
83	\section{Downstream Utility}
84	\label{app:downstream}
85	\input{appendix_downstream}
86	
87	\end{document}
88	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-17T13:54:10.030684+00:00_

Web search results for query: ""aclrollingreview.org" ARR CFP 2026 long paper 8 pages anonymity supplementary material"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/cfp.md at master · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/master/cfp.md"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"LINGUIST List 36.2627 Confs: 19th Conference of the European Chapter of the Association for Computational Linguistics (Morocco)","url":"https://linguistlist.org/issues/36/2627/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the web search results for ARR (ACL Rolling Review) CFP 2026, here's the information about long papers, page limits, anonymity, and supplementary material:

## Long Paper Requirements

Long papers may consist of up to eight (8) pages of content, plus unlimited pages of references.

## Anonymity Policy

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities must be avoided.

## Supplementary Material

Anonymized versions of papers should be uploaded as supplementary material, particularly for papers that are concurrently submitted on related topics with overlapping author sets that need to discuss differences in the related work section.

Additiona
…[truncated 282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 4816
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-17T13:54:17.204340+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-17T13:54:17.656202+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-17T13:54:18.108195+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-17T13:54:18.259074+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-17T13:54:18.610873+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-17T13:54:18.661408+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_8.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-17T13:54:41.482755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-17T13:54:42.387020+00:00_

1	- id: "R1-W1"
2	  summary: "Baseline hyperparameter inconsistency"
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 8
8	  resolution: "method.tex unified to est200/md6. Verified R8."
9	  resolution_round: 8
10	
11	- id: "R1-W5"
12	  summary: "Downstream experiment too small"
13	  category: framing
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 8
18	  resolution: "TOST added. Contribution 3 restored with perplexity scope."
19	  resolution_round: 8
20	
21	- id: "R7-W1"
22	  summary: "gen-0 seed sharing inflating headline"
23	  category: experiment
24	  severity: warning
25	  status: resolved
26	  first_raised_round: 7
27	  last_seen_round: 9
28	  resolution: "Abstract reports both binary and 3-class. Verified R9."
29	  resolution_round: 9
30	
31	- id: "R7-W2"
32	  summary: "DDR mechanism overclaim"
33	  category: method
34	  severity: warning
35	  status: resolved
36	  first_raised_round: 7
37	  last_seen_round: 8
38	  resolution: "Changed to 'tendency of standard decoding'. Confirmed R8."
39	  resolution_round: 8
40	
41	- id: "R7-W3"
42	  summary: "Efficiency not quantified"
43	  category: experiment
44	  severity: warning
45	  status: resolved
46	  first_raised_round: 7
47	  last_seen_round: 8
48	  resolution: "Table 4 ms/text + memory. Confirmed R8."
49	  resolution_round: 8
50	
51	- id: "R7-W4"
52	  summary: "Method novelty divergence"
53	  category: framing
54	  severity: warning
55	  status: open
56	  first_raised_round: 7
57	  last_seen_round: 9
58	  mentions:
59	    - {round: 9, reviewers: "R1,R2", note: "Structural. R1 3.5, R2 3.0→3.5 if C3 fixed."}
60	  action_items:
61	    - {round: 7, action: "Rebuttal triple defense", assigned_to: "Director", status: "open"}
62	  resolution: ""
63	  resolution_round: null
64	
65	- id: "R7-W5"
66	  summary: "Instruct framing"
67	  category: framing
68	  severity: warning
69	  status: resolved
70	  first_rais
…[truncated 827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-17T13:54:42.487885+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
  "description": "Find project config files with external_review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
    "description": "Find project config files with external_review settings"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-17T13:54:42.640965+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-17T13:54:47.361147+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10",
  "description": "Search for external review config in project files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10",
    "description": "Search for external review config in project files"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-17T13:54:47.913676+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-17T13:54:53.893285+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/ -name \"config*.yaml\" -o -name \"config*.yml\" -o -name \"project*.yaml\" | grep -i \"gen-depth\\|config\" | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/ -name \"config*.yaml\" -o -name \"config*.yml\" -o -name \"project*.yaml\" | grep -i \"gen-depth\\|config\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-17T13:54:53.945971+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/svs_pipeline/config_proofwriter_full.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/svs_pipeline/config.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/svs_pipeline/config_logiqa.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/svs_pipeline/config_folio.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-17T13:55:01.775126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-17T13:55:01.876000+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	When LLM-generated text re-enters the web and seeds further generation, the resulting recursive chains exhibit progressively altered distributional properties, complicating provenance tracking and quality-aware data curation.
4	We ask whether this drift is structured enough to estimate how many generation steps a text has undergone, framing this as \emph{ordinal depth estimation} (classifying text as gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Studying eight base models from five families, we identify a \emph{differential depth response}: central-tendency features (mean entropy, lexical diversity) drift monotonically with generation depth, while shape features (entropy max, vocabulary tail slope) remain near-stationary.
6	This pattern is consistent with a location shift in the token-level negative log-likelihood (NLL) distribution that preserves distributional shape.
7	Exploiting this complementarity, a 7-feature ensemble achieves 3-class macro F1\,=\,0.809 on heterogeneous cross-model chains (binary F1\,=\,0.764) and F1\,=\,0.762 under leave-one-generator-out evaluation across eight generators (binary: 0.694), with competitive performance at substantially lower computational cost than multi-detector alternatives.
8	Despite this detectable drift, a TOST equivalence test confirms that depth-aware data selection yields training utility equivalent to random subsampling ($\pm$2\% margin, $p < 0.001$) within $\leq$4 generations, decoupling detectability from downstream perplexity degradation.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-17T13:55:01.926643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-17T13:55:01.977289+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-crawled pretraining corpora \cite{dolma,fineweb} increasingly contain LLM-generated text (estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}), and this proportion grows as generated text re-enters the web and seeds subsequent generation.
5	The result is recursive generation chains whose outputs progressively diverge from human-written text.
6	Understanding how distributional features evolve across generation depths is a prerequisite for characterizing this recursive contamination, yet existing methods \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions, conflating qualitatively different material: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	
8	We formulate \emph{ordinal depth estimation}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and refer to the overall framework as \emph{depth fingerprinting}.
9	No existing method addresses this task in non-paraphrastic continuation chains.
10	
11	The key finding is a \emph{differential depth response} (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) remain near-stationary.
12	This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution while preserving its shape: the softmax architecture and fixed sampling parameters constrain distributional shape under standard deco
…[truncated 2098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-17T13:55:07.157324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-17T13:55:07.358644+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
17	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	We use shared seeds across generators to ensure that cross-generator comparisons control for input content, isolating the effect of the generation model from sou
…[truncated 8902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-17T13:55:07.359079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-17T13:55:07.409760+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), the 3-class metric may carry upward bias from memorized gen-0 patterns; we therefore also report a leak-free binary metric (gen-1 vs.\ gen-2+): F1\,=\,0.694, CI [0.688, 0.700], which is unaffected by this sharing.
9	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B); the primary difficulty is distinguishing gen-1 from gen-2+ (Appendix~\ref{app:confusion}).
10	Larger generators show moderate degradation (Qwen3-8B: 0.692, Mistral-7B: 0.633) relative to the 0.694 average.
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.764 under 5-fold CV,\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists when text passes through heterogeneous generators.
14	Leave-one-family-out (LOFO) evaluation yields average binary F1\,=\,0.686 ($\Delta$\,=\,$-$0.8\,pp vs.\ LOGO), confirming transfer across architectural families under the strictest unseen-generator test.
15	Appendix~\ref{app:domain} further demonstrates that the signal generalizes across text domains (News, Academic, Code; binary F1 $>$ 0.73).
16	
17	\paragraph{Length confound control.}
18	Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770 unmatched; $\Delta$\,=\,$-$0.046); a random-subsample control at equal $N$ (F1\,=\,0.767) confirms the drop reflects deconfounding, not sample-size reduction.
19	Length accounts for $\approx$6\% of discriminative performance (Appendix~\ref{app:length}
…[truncated 7637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-17T13:55:13.330606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-17T13:55:13.833061+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why does shape remain approximately stationary?}
5	The softmax architecture and sampling hyperparameters that determine distributional shape are fixed across depths.
6	Recursive generation shifts context toward high-probability regions, reducing entropy mean, but does not alter the generation mechanism itself.
7	This account predicts approximate stationarity under standard decoding: sampling ablation confirms that shape measures remain stable when sampling noise is low ($t \in [0.5, 0.7]$, ${\leq}0.3$\,pp degradation), but stationarity weakens at $t = 1.0$ ($-6$\,pp; Appendix~\ref{app:sampling-sensitivity}), where sampling randomness begins to dominate the systematic location shift.
8	The phenomenon thus reflects a tendency of standard decoding rather than an architectural guarantee.
9	Entropy std ($|\rho| = 0.17$) is a borderline case: its moderate correlation places it between the clearly drifting central-tendency features ($|\rho| > 0.60$) and the near-stationary tail decay ($|\rho| = 0.04$), consistent with a feature that partially captures location-dependent variance.
10	
11	\paragraph{Prompt-type dependence.}
12	Continuation chains yield the strongest signal (F1\,=\,0.781 vs.\ 0.730 for elaboration), with cross-type transfer at 0.753 (Appendix~\ref{app:prompt-type}).
13	Semantic-preservation constraints attenuate drift, consistent with \citet{broken_telephone}: the more a task anchors the output distribution to the input, the less room recursive drift has to accumulate.
14	
15	\paragraph{Practical applicability.}
16	At the document level, gen-1 per-class F1\,=\,0.63 (37\% misclassification) is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\sqrt{n})$ and aggregate depth composition estimates become reliable.
17	Error analysis (Appendix~\ref{app:error-analysis}) confirms that misclassifications concentrate in shallow gen-2+ samples where dr
…[truncated 2388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-17T13:55:13.883593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-17T13:55:14.084666+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (3-class F1\,=\,0.809 on cross-model chains, 0.762 under LOGO).
5	Despite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\pm$2\%, $p < 0.001$) within chains of $\leq$4 generations as measured by perplexity, establishing that detectability and downstream harm are decoupled in this regime.
6	
7	Two boundaries define the scope of these results.
8	First, instruction tuning compresses the distributional variation that fingerprinting exploits; extending to aligned models requires disentangling format-induced and depth-induced drift.
9	Second, while the signal generalizes across generators up to 8B parameters, frontier-scale models (70B+) with higher fluency may further compress feature margins.
10	All code, data, and trained models will be released upon publication.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-17T13:55:14.084995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-17T13:55:14.135449+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
12	Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
13	Our contribution is not a new detection method but the task formulation (ordinal depth estimation, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance.
14	This is orthogonal to source attribution \cite{uchendu_attribution,munir_looking_glass}, which identifies \emph{which} model generated text; our LOGO evalua
…[truncated 2591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-17T13:55:19.456164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-17T13:55:19.707607+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 under a 7-generator split).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary e
…[truncated 1941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-17T13:55:19.758309+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-17T13:55:19.758784+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	
10	\paragraph{Licenses.}
11	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
12	Wikipedia seed passages are distributed under CC BY-SA 3.0.
13	
14	\paragraph{Compute budget.}
15	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
16	
17	\paragraph{Software.}
18	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-17T13:56:02.821014+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "**[Round 1 审稿任务 — Reviewer 1: 方法严谨性 + 实验设计]**\n\n## 论文信息\n- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 (ACL Rolling Review)\n- **格式**: ACL 模板 [review]，Long paper (≤8 页正文)，double-blind，Limitations section 必需\n\n## 你的审查侧重\n\n你负责评估**方法严谨性和实验设计**，重点关注：\n\n1. **实验设计合理性**\n   - 生成链构建是否控制了关键变量（seed 共享的泄漏风险、生成参数选择）\n   - LOGO/LOFO 评估协议是否真正测试泛化能力\n   - Binary F1（gen-1 vs gen-2+）vs 3-class F1 的区分是否合理\n   - gen-0 seed 共享导致的 train-test 重叠是否被充分处理\n\n2. **统计方法**\n   - Bootstrap CI、McNemar test、Bonferroni 校正的使用是否正确\n   - TOST equivalence test 的 margin 选择（±2%）是否合理\n   - 相关系数的计算（class-balanced subsampling）是否充分控制混淆\n\n3. **Baseline 比较公平性**\n   - 4 个 detection baseline 作为 ordinal predictor 的 repurposing 是否公平\n   - 统一 XGBoost 超参是否可能对某些方法不利\n   - 4-det ensemble vs 7-feature 的比较结论（\"competitive at lower cost\"）是否夸大\n\n4. **核心 claim 的证据支撑**\n   - DDR（differential depth response）是否有充分证据？location shift 解释是否overclaim？\n   - \"shape 保持 stationary\" 的 claim 是否有统计检验支撑？\n   - Downstream utility 实验（TOST）的规模和设计是否足以支撑 Contribution 3？\n   - Instruction tuning 失效是否是致命限制？\n\n5. **可复现性**\n   - 实验细节是否充分（超参、数据预处理、随机种子）\n   - 数据集规模（37K texts）是否足够\n   - 代码/数据是否承诺开源\n\n请按 ARR 标准输出完整审稿意见，包含：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Nice-to-Fix）、Questions to Authors、Overall Assessment（1-5 分制，参考 EMNLP 2026 评分标准：4=Conference, 3.5=Borderline Conference, 3=Findings）。",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "**[Round 1 审稿任务 — Reviewer 1: 方法严谨性 + 实验设计]**\n\n## 论文信息\n- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 (ACL Rolling Review)\n- **格式**: ACL 模板 [review]，Long paper (≤8 页正文)，double-blind，Limitations section 必需\n\n## 你的审查侧重\n\n你负责评估**方法严谨性和实验设计**，重点关注：\n\n1. **实验设计合理性**\n   - 生成链构建是否控制了关键变量（seed 共享的泄漏风险、生成参数选择）\n   - LOGO/LOFO 评估协议是否真正测试泛化能力\n   - Binary F1（gen-1 vs gen-2+）vs 3-class F1 的区分是否合理\n   - gen-0 seed 共享导致的 train-test 重叠是否被充分处理\n\n2. **统计方法**\n   - Bootstrap CI、McNemar test、Bonferroni 校正的使用是否正确\n   - TOST equivalence test 的 margin 选择（±2%）是否合理\n   - 相关系数的计算（class-balanced subsampling）是否充分控制混淆\n\n3. **Baseline 比较公平性**\n   - 4 个 detection baseline 作为 ordinal predictor 的 repurposing 是否公平\n   - 统一 XGBoost 超参是否可能对某些方法不利\n   - 4-det ensemble vs 7-feature 的比较结论（\"competitive at lower cost\"）是否夸大\n\n4. **核心 claim 的证据支撑**\n   - DDR（differential depth response）是否有充分证据？location shift 解释是否overclaim？\n   - \"shape 保持 stationary\" 的 claim 是否有统计检验支撑？\n   - Downstream utility 实验（TOST）的规模和设计是否足以支撑 Contribution 3？\n   - Instruction tuning 失效是否是致命限制？\n\n5. **可复现性**\n   - 实验细节是否充分（超参、数据预处理、随机种子）\n   - 数据集规模（37K texts）是否足够\n   - 代码/数据是否承诺开源\n\n请按 ARR 标准输出完整审稿意见，包含：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Nice-to-Fix）、Questions to Authors、Overall Assessment（1-5 分制，参考 EMNLP 2026 评分标准：4=Conference, 3.5=Borderline Conference, 3=Findings）。",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-17T13:56:18.744426+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15923
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-17T13:56:19.146799+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "**[Round 1 审稿任务 — Reviewer 2: 新颖性 + 完整性 + 写作质量]**\n\n## 论文信息\n- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 (ACL Rolling Review)\n- **格式**: ACL 模板 [review]，Long paper (≤8 页正文)，double-blind，Limitations section 必需\n\n## 你的审查侧重\n\n你负责评估**新颖性、完整性和写作质量**，重点关注：\n\n1. **新颖性和贡献度**\n   - \"Ordinal depth estimation\" 作为新任务是否有足够意义？是否只是 binary detection 的简单三分类扩展？\n   - DDR（differential depth response）是否是真正的新发现？还是已知现象（model collapse literature）的直接推论？\n   - 7-feature ensemble 方法本身的技术贡献有多大？（TTR/hapax ratio 是经典 stylometry 指标）\n   - 与 Broken Telephone (ICML 2024)、Markovian Chains 等 concurrent work 的差异化是否清晰？\n\n2. **Related Work 覆盖度**\n   - 引用是否充分覆盖：detection methods、model collapse、data quality、stylometry\n   - 是否遗漏重要的直接相关工作（特别是 2024-2026 年的新工作）\n   - Positioning 是否清晰——论文在现有工作格局中的位置\n\n3. **写作质量**\n   - 故事线是否连贯（Abstract → Intro → Method → Results → Discussion → Conclusion）\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段等）\n   - 专有名词是否有定义（DDR、depth fingerprinting、LOGO、LOFO 等首次出现时）\n   - 数字和 claim 是否前后一致（同一指标在不同 section 的引用是否匹配）\n\n4. **完整性**\n   - Contributions 列表中每项是否有对应的实验支撑\n   - 附录内容是否在正文中被恰当引用\n   - Limitations section 是否诚实、完整地讨论了核心局限\n   - 是否有重要实验/分析缺失（如：更多 generator、real-world data、paraphrase 攻击）\n\n5. **格式合规**\n   - 正文是否 ≤ 8 页\n   - 匿名化是否完整（无 self-citation 泄漏）\n   - 图表 caption 是否自包含\n   - 引用格式是否正确\n\n请按 ARR 标准输出完整审稿意见，包含：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Nice-to-Fix）、Questions to Authors、Missing References、Overall Assessment（1-5 分制，参考 EMNLP 2026 评分标准：4=Conference, 3.5=Borderline Conference, 3=Findings）。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "**[Round 1 审稿任务 — Reviewer 2: 新颖性 + 完整性 + 写作质量]**\n\n## 论文信息\n- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 (ACL Rolling Review)\n- **格式**: ACL 模板 [review]，Long paper (≤8 页正文)，double-blind，Limitations section 必需\n\n## 你的审查侧重\n\n你负责评估**新颖性、完整性和写作质量**，重点关注：\n\n1. **新颖性和贡献度**\n   - \"Ordinal depth estimation\" 作为新任务是否有足够意义？是否只是 binary detection 的简单三分类扩展？\n   - DDR（differential depth response）是否是真正的新发现？还是已知现象（model collapse literature）的直接推论？\n   - 7-feature ensemble 方法本身的技术贡献有多大？（TTR/hapax ratio 是经典 stylometry 指标）\n   - 与 Broken Telephone (ICML 2024)、Markovian Chains 等 concurrent work 的差异化是否清晰？\n\n2. **Related Work 覆盖度**\n   - 引用是否充分覆盖：detection methods、model collapse、data quality、stylometry\n   - 是否遗漏重要的直接相关工作（特别是 2024-2026 年的新工作）\n   - Positioning 是否清晰——论文在现有工作格局中的位置\n\n3. **写作质量**\n   - 故事线是否连贯（Abstract → Intro → Method → Results → Discussion → Conclusion）\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段等）\n   - 专有名词是否有定义（DDR、depth fingerprinting、LOGO、LOFO 等首次出现时）\n   - 数字和 claim 是否前后一致（同一指标在不同 section 的引用是否匹配）\n\n4. **完整性**\n   - Contributions 列表中每项是否有对应的实验支撑\n   - 附录内容是否在正文中被恰当引用\n   - Limitations section 是否诚实、完整地讨论了核心局限\n   - 是否有重要实验/分析缺失（如：更多 generator、real-world data、paraphrase 攻击）\n\n5. **格式合规**\n   - 正文是否 ≤ 8 页\n   - 匿名化是否完整（无 self-citation 泄漏）\n   - 图表 caption 是否自包含\n   - 引用格式是否正确\n\n请按 ARR 标准输出完整审稿意见，包含：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Nice-to-Fix）、Questions to Authors、Missing References、Overall Assessment（1-5 分制，参考 EMNLP 2026 评分标准：4=Conference, 3.5=Borderline Conference, 3=Findings）。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-17T13:56:20.563362+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1416
}
```

</details>

---


### Assistant

_source line 408 · 2026-05-17T13:56:26.373915+00:00_

Round 1 审稿任务已分配：

- **Reviewer 1**（方法严谨性 + 实验设计）→ 已触发
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）→ 已触发

等待两位 Reviewer 返回独立审稿意见后，进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 409 · 2026-05-17T14:05:52.219357+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

## Paper
**Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains**

---

## Summary

本文提出 ordinal generation depth estimation（序数生成深度估计）任务：给定一段文本，判断其经历了多少轮 LLM 续写（gen-0 = 人类原文, gen-1, gen-2+）。作者构建了 8 个 base model（来自 Pythia, OLMo, Qwen, Llama, Mistral 五个模型家族）的非改写式续写链（每链深度 4），基于约 1,000 条 Wikipedia 种子文本生成 ~37K 条样本。核心发现是 **differential depth response (DDR)**：reference-model 特征（entropy mean, NLL 相关统计量）随深度单调漂移，而 shape 特征（tail_decay, entropy_std）保持近平稳。基于 7 个手工特征的 XGBoost ensemble 在 LOGO (leave-one-generator-out) 评估下达到 3-class macro F1 = 0.809，binary F1 (gen-1 vs gen-2+) = 0.762。论文还通过 TOST equivalence test 论证 downstream utility（深度感知数据筛选 ≈ 随机子采样），并在附录中提供了大量消融实验。

---

## 总体评分

**Overall Assessment**: 3.0 / 5 (Findings)

**一句话总结**: 任务定义新颖、实证分析扎实，但方法对 instruction-tuned 模型完全失效且采样参数敏感性高，严重限制了实际影响力；部分核心 claim 的统计证据不足。

---

## 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 实验设计整体合理，但 gen-0 seed 共享造成 train-test 泄漏（inflates 3-class headline）、"location shift" claim 缺乏正式检验、TOST margin ±2% 无理论依据 |
| Excitement | 3.0 / 5 | 任务定义有趣且未被前人探索，但仅适用于 base model + 特定采样参数的续写链，实际部署场景极窄 |
| Reproducibility | 4.0 / 5 | 超参、软件版本、计算预算均有记录；承诺开源代码和数据；唯一扣分是某些关键实现细节（如 NLL 计算的 tokenization 对齐方式）未完全说明 |
| Confidence | 4 / 5 | 我仔细阅读了全文 17 页及所有附录，熟悉 AI-generated text detection 和分布漂移相关文献 |

---

## Must-Fix 问题（影响接收决定）

### N1 [critical] gen-0 seed 共享导致 LOGO 3-class 结果膨胀

- **具体位置**: §3.2 ("We use shared seeds across generators"), §4.1 Table 1
- **问题**: ~1,000 条 Wikipedia 种子文本作为 gen-0 被所有 8 个 generator 共享。在 LOGO 评估中，test set 中某 generator 的 gen-0 样本与 train set 中其他 generator 的 gen-0 样本是**完全相同的文本**。分类器可以通过记忆 gen-0 的具体文本内容（而非学习分布特征）来完美识别 gen-0 类，人为抬高 3-class 性能。
- **论文已知但处理不足**: 论文在 §3.2 承认了这一点，并额外报告了 binary F1 (gen-1 vs gen-2+, 排除 gen-0) = 0.684。然而论文的 headline 结果仍然是 3-class F1 = 0.809（Abstract, §4.1, Contribution 1），且 Confusion Matrix（Appendix G, Table 10）显示 gen-0 分类准确率 99.1%，远高于 gen-1 (56.9%) 和 gen-2+ (74.0%)，这与泄漏假说一致。
- **为什么影响接收**: 如果主要数字被泄漏 inflate，则 Contribution 1 的可信度大打折扣。审稿人和读者会质疑方法的真实区分力。
- **建议修改方向**: (1) 将 headline 结果改为 leak-free binary F1 或使用 generator-disjoint gen-0 seeds 重跑；(2) 设计一个消融实验：在 LOGO 中将 test generator 的 gen-0 替换为未在 train 中出现过的新 Wikipedia 种子，观察 gen-0 准确率是否显著下降；(3) 至少在正文中明确标注 3-class F1 的 gen-0 泄漏上限。

### N2 [critical] Instruction tuning 完全破坏 depth signal，但 framing 不匹配

- **具体位置**: §5 "Instruction tuning" 段, Conclusion §6 第 2 段
- **问题**: OLMo-2-7B-Instruct 的 LOGO F1 = 0.338 vs base 0.763（>55% 相对下降）；Qwen3-0.6B-Instruct F1 = 0.648。论文在 §8 (Limitations) 和 §6 中承认 "restriction to base models as the appropriate setting for isolating the phenomenon"，但 Abstract 和 Introduction 的 framing 均未限定 scope 为 base models only。
  - Abstract: "we ask whether this drift is structured enough to estimate how many generation steps a text has undergone"（暗示通用性）
  - Introduction: "provenance tracking and quality-aware data curation"（暗示实用性）
- **为什么影响接收**: 目前几乎所有被广泛使用的 LLM 都经过 instruction tuning / RLHF。一个仅适用于 base model 的方法，其 "provenance tracking" 和 "data curation" 动机在实际中不成立。这不是一个 edge case，而是方法的根本适用范围限制。
- **建议修改方向**: (1) 在 Abstract 和 Introduction 中明确限定 scope 为 base model continuation chains；(2) 讨论 instruction tuning 为何破坏 signal 的机制（alignment 改变了 token 分布的 entropy landscape？RLHF 的 KL regularization 限制了 depth-dependent drift？），这比单纯报告数字更有学术价值；(3) 探讨是否存在 feature 或方法变体在 instruction-tuned model 上仍有效。

### N3 [critical] 采样参数敏感性极高，但未在正文充分讨论

- **具体位置**: Appendix H (Table 12), §5 "Why does shape remain approximately stationary?"
- **问题**: 在 t=1.0, top-p=0.95 的采样条件下，"classification degrades to near chance"（Appendix H）。论文的所有主实验使用 t=0.7, nucleus p=0.7，这是一个相对受限的 low-temperature/low-diversity 设置。§5 讨论中说 "at t ≈ 1.0 (< 4 pp, where sampling randomness begins to dominate the systematic location shift)"，但这意味着**方法依赖于模型 output 的 high-probability regions 主导的生成方式**。
- **为什么影响接收**: 在实际场景中，不同用户/应用使用的采样参数各不相同。一个对采样参数如此敏感的方法，其 "depth fingerprinting" 的概念基础受到动摇——depth signal 可能只是 temperature 引起的 entropy 变化的间接产物，而非 recursive generation 的 intrinsic property。
- **建议修改方向**: (1) 在正文 (§4 或 §5) 中直接讨论采样参数敏感性（而非仅放在附录）；(2) 量化 depth signal 与 temperature 的交互效应：在不同 temperature 下是否仍然存在 monotonic drift，只是 magnitude 变小？还是 drift 方向反转？(3) 如果 depth signal 确实只在 low-temperature regime 存在，需要重新审视 DDR 的理论解释。

---

## Should-Fix 问题（影响评分但不一票否决）

### W1 [warning] "Location shift" claim 缺乏正式统计检验

- **具体位置**: §4.2, Abstract ("location shift in the token-level NLL distribution")
- **问题**: 论文声称 DDR "is consistent with a location shift in the token-level NLL distribution while preserving distributional shape"。但证据仅来自 (1) 单调相关性分析 (Spearman ρ)，和 (2) shape 特征 |ρ| < 0.10。这不构成对 "location shift" 的正式检验。"Location shift" 在统计学中有精确定义（分布族中仅 location parameter 变化），而论文没有：
  - 对 NLL 分布进行 Kolmogorov-Smirnov / Anderson-Darling test 检验同分布族假设
  - 量化 scale/shape parameter 在不同深度间是否真正不变（而非仅相关性弱）
  - 检验 shift 是否在所有 quantiles 上一致（不仅仅是 mean/min/max）
- **建议**: 降低 claim 强度（"consistent with" 改为 "suggestive of"），或补充 Q-Q plot + formal distributional tests 来支撑 claim。

### W2 [warning] TOST equivalence margin ±2% 的选择缺乏理论依据

- **具体位置**: §4.4 Downstream Utility, Table 18 (Appendix L)
- **问题**: TOST test 使用 ±2% relative margin 来论证 depth-stratified training ≈ random subsampling。但 ±2% 的选择没有理论或实证依据。在 NLU/language modeling 中，2% perplexity 差异在某些任务上可能微不足道，在另一些任务上可能 meaningful。论文也没有讨论 effect size 或 practical significance threshold 来自何处。
- **建议**: (1) 引用 NLP 文献中对 perplexity 差异的 practical significance 标准；(2) 报告多个 margin 下的 TOST 结果（如 ±1%, ±3%, ±5%），让读者判断 robustness；(3) 补充 Cohen's d 或其他 effect size 指标。

### W3 [warning] Baseline repurposing 可能不公平

- **具体位置**: §3.4 "Baselines", §4.3, Table 4
- **问题**: 4 个 detection baseline（Fast-DetectGPT, Binoculars, LD-Score, Avg-LogProb）被 repurposed 为 ordinal predictor——将其 score 作为 XGBoost 输入。这些方法设计初衷是 binary detection (human vs machine)，其 score 的 ordinal monotonicity 不是设计目标。统一使用 XGBoost (n_estimators=200, max_depth=6) 对所有方法可能不利于某些 baseline（例如 Binoculars 的 score 分布可能需要不同的 tree 深度）。
- **论文部分回应**: Table 4 脚注 5 提到 LOGO F1 "is stable across random seeds (sd < 0.001 over 5 seeds)"，Appendix D 展示了替代分类器（random forest, logistic regression）yielding comparable performance。但这只说明分类器选择 robust，没有说明超参对不同 baseline 的适配性。
- **建议**: (1) 对每个 baseline 做独立的超参搜索（至少 grid search max_depth 和 n_estimators），报告各自最佳结果；(2) 或者讨论为何统一超参是合理的（例如 score 分布的 smoothness 类似）。

### W4 [warning] gen-1/gen-2 边界区分力不足，但论文未充分讨论实际影响

- **具体位置**: Appendix G (Table 10), Appendix K (§K)
- **问题**: Confusion matrix 显示 gen-2+ 被误分为 gen-1 的比例为 18.93%，gen-1 被误分为 gen-2+ 的比例为 36.9%。Appendix K 进一步分析显示 gen-1→gen-2 boundary 的 error rate 为 48.42%。这意味着在实际应用中，对于 gen-1 和 gen-2 的区分接近随机猜测。
- **问题的核心**: 论文的 3-class 设计将 depth 2-4 合并为 gen-2+，但即使在这种 simplified 设定下，gen-1 vs gen-2+ 的区分仍然困难（binary F1 = 0.684/0.762 depending on gen-0 inclusion）。如果 depth fingerprinting 的核心价值在于细粒度深度估计，当前方法在最关键的边界上表现不佳。
- **建议**: 在 Discussion 中更坦诚地讨论 gen-1/gen-2 区分的实际难度和对应用的影响。

### W5 [warning] 数据多样性不足

- **具体位置**: §3.2, Appendix J (Table 16)
- **问题**: 主实验全部基于 English Wikipedia seeds。虽然 Appendix J 测试了 News, Academic, Code 三个域，但仅用 3 个 generator（Pythia-1B, Qwen3-1.7B, Mistral-7B）、200 seeds、depth 3。这是一个非常有限的 cross-domain 评估：
  - 仅 3/8 个 generator
  - 每 domain 仅 200 seeds
  - Academic domain 的 F1 = 0.628（显著低于 Wikipedia 0.762 的 binary F1）
  - 未测试更多真实场景域（如 social media, creative writing, dialogue）
- **建议**: 扩大 cross-domain 评估规模，或至少讨论 Wikipedia 作为唯一 seed source 的 selection bias。

---

## 小问题（不影响接收）

- **P1**: Table 1 caption 说 "Bootstrap 95% CIs, n = 1000"，但未说明 bootstrap 的具体抽样策略（case-level resample? stratified?）
- **P2**: §3.3 提到 "entropy" 作为 shorthand for token-level NLL，但 entropy 在信息论中有不同含义。建议统一使用 "per-token negative log-likelihood" 或明确定义 "entropy" 在本文中的操作定义
- **P3**: Figure 1 的 strip plot 中，hapax_ratio 的 violin 密度分布在高深度端几乎不可见，建议调整 y 轴或使用 box plot 补充
- **P4**: Appendix E (QLoRA) 达到 3-class F1 = 0.905，显著优于手工特征的 0.809，但正文几乎没有讨论这个结果对 "handcrafted features 是否是最佳方法选择" 的影响
- **P5**: 引用 `aaronson_watermark` (2022) 是一个 technical talk / blog post，非正式出版物，建议补充正式引用或注明性质

---

## Questions to Authors

1. **gen-0 泄漏量化**: 如果在 LOGO 中使用 generator-disjoint gen-0 seeds（每个 generator 使用不重叠的 Wikipedia 种子），3-class F1 会下降多少？这能直接量化 seed-sharing inflation 的程度。

2. **Temperature 交互效应**: 在 t=0.8 和 t=0.9 的中间设定下，DDR 的 monotonic drift 是否仍然成立？还是存在一个 sharp transition？如果有 transition，这对 "location shift" 的 intrinsic mechanism 解释意味着什么？

3. **Instruction tuning 的具体机制**: 你们认为 instruction tuning 破坏 depth signal 的机制是什么？是 alignment 训练改变了 base distribution 的 entropy landscape，还是 instruction following 引入了新的文本结构特征（如固定回答模板）导致 depth-independent 的 feature 变化？

4. **Downstream utility 的实际场景**: TOST test 仅在 fine-tuning perplexity 上测试。是否有更具说服力的 downstream 任务（如 text quality scoring, content moderation）能展示 depth-aware curation 的实际价值？

5. **QLoRA vs 手工特征**: 既然 QLoRA 的 3-class F1 (0.905) 显著高于手工特征 (0.809)，为什么论文不以 QLoRA 为主方法？"interpretability" 是否足以作为选择劣势方法的理由？

---

## 主要优势

1. **任务定义新颖**: Ordinal generation depth estimation 是一个未被前人探索的有意义的研究问题，将 binary AI detection 推进为 fine-grained depth estimation
2. **实证分析全面**: 17 页论文包含大量消融实验（LOFO, 混淆矩阵, 长度控制, 采样参数, 文本扰动, 跨域, QLoRA, 下游效用），远超一般论文的分析深度
3. **DDR 框架有洞察力**: Reference-model features drift / shape features stationary 的二分法提供了理解 recursive generation 的新视角，有启发性
4. **统计方法整体规范**: Bootstrap CI, McNemar test, Bonferroni correction, 类平衡子采样等使用得当
5. **诚实讨论局限**: Instruction tuning 限制、gen-0 泄漏、human editing 模拟等都有所讨论
6. **引用核查通过**: 56 条引用中 46 条在线验证通过，无伪造引用

---

## 最终判断

本文的任务定义和实证分析质量较高，值得发表。但三个 critical 问题（gen-0 泄漏导致 headline inflate, instruction tuning 完全失效与 framing 不匹配, 采样参数高度敏感）共同指向一个核心担忧：**方法的 actual discriminative power 和 practical applicability 被论文当前 framing 显著夸大了**。leak-free binary F1 = 0.684 对比 headline 3-class F1 = 0.809 的落差本身就说明了问题。如果作者能 (1) 用 leak-free metrics 重构 headline, (2) 在 framing 中明确限定 scope, (3) 正面讨论 temperature sensitivity 的理论含义，本文可以成为一篇坚实的 Findings 论文。当前状态建议 **Findings (3.0)**。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 410 · 2026-05-17T14:06:02.083565+00:00_

Reviewer 1 已提交审稿意见。等待 Reviewer 2 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 411 · 2026-05-17T14:06:07.327867+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.0 / 5 (Findings)** 评分。三个 critical 问题：

1. **gen-0 seed 共享导致 3-class headline inflate** — 相同 Wikipedia 种子在 LOGO 中 train/test 重叠，gen-0 准确率 99.1% 疑似记忆效应，leak-free binary F1 仅 0.684
2. **Instruction tuning 完全失效但 framing 未限定 scope** — OLMo-Instruct F1 从 0.763 降至 0.338，但 Abstract/Intro 暗示通用性
3. **采样参数敏感性极高** — t=1.0 时退化为随机水平，所有主实验仅在 t=0.7 下进行，且仅在附录讨论

另有 5 个 should-fix（"location shift" claim 缺正式检验、TOST margin 无依据、baseline repurposing 公平性、gen-1/gen-2 区分力不足、数据多样性有限）和 5 个小问题。论文的任务定义新颖、实证分析全面是主要优势，但核心 discriminative power 和 practical applicability 被当前 framing 显著夸大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-17T14:06:15.376618+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交意见后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 36

## Round 36

6 recorded events


### User

_source line 413 · 2026-05-17T14:08:03.280181+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见 — Round 1
## 论文：Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains

---

## Summary

本文提出 "depth fingerprinting" 任务，将 LLM 文本链中的生成深度估计从二分类（human vs. synthetic）扩展为三类序数分类（gen-0/gen-1/gen-2+）。作者在 5 个模型家族、8 个 base 模型（0.6B–8B）上构建非改写续写链，发现 "differential depth response"（DDR）：中心趋势特征（entropy mean、TTR、hapax ratio）随深度单调漂移，而形状特征（entropy sd、tail decay）保持近平稳。基于此，7 个手工特征 + XGBoost 在 LOGO 评估下达到 3-class macro F1 = 0.762，cross-model 链上达到 0.809。论文还展示了鲁棒性分析（长度、prompt 类型、扰动、跨域）和下游数据筛选实验。

---

## 总体评分

**Overall Assessment**: 3.0 / 5 (Findings)

**一句话总结**: 任务定义清晰、实验设计扎实，但 DDR 新颖性相对 model collapse 文献有限，"ordinal" framing 被三分类上限削弱，下游应用实验未能支撑核心动机。

---

## 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 评估方案设计周密（LOGO/LOFO/TOST），但部分 claim 被过度包装（见 N2、N3）；主要实验结论有充分支撑 |
| Excitement | 2.5/5 | 任务有趣但贡献增量有限：DDR 在 model collapse 理论下可预期；7 个经典 stylometry 特征 + XGBoost 技术贡献不大；下游实验为负面结果 |
| Reproducibility | 4/5 | 特征定义完整（§3.3），数据构建流程清晰（§3.2），超参数明确（§3.4），承诺释放代码和数据 |
| Reviewer Confidence | 4/5 | 熟悉 AI 文本检测、model collapse、stylometry 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DDR 相对 model collapse 文献的新颖性不足
- 具体位置：§4.2、Abstract ("The key finding is a differential depth response")
- 问题：DDR 的核心发现——递归生成导致分布收窄（词汇多样性下降、可预测性升高）——在 model collapse 文献中已有充分记录。Shumailov et al. (2024) 证明递归训练导致分布尾部丧失；Guo et al. (2024, Curious Decline) 直接量化了词汇多样性下降。本文将这一现象分解为 "location shift + shape preservation" 增加了颗粒度，但底层现象并非新发现。论文在 Discussion §5 段2 ("Relation to model collapse") 仅用两句带过这一关系，没有给出充分的区分论证。
- 为什么影响接收：如果核心 finding 是已知现象的再确认，论文的新颖性主张被实质性削弱。
- 建议修改方向：(1) 在 §2.2 和 §5 中系统对比 DDR 与 model collapse 的具体差异：model collapse 研究的是跨代训练后的分布退化，DDR 研究的是单次推理链中的分布漂移——需要论证为什么这一区别在理论和实践上重要。(2) 提供实验证据表明 DDR 不能由 model collapse 理论直接推导（例如 shape stationarity 在 model collapse 中是否也成立？）。

**N2** [critical] "Ordinal depth estimation" framing 与三分类实际能力不匹配
- 具体位置：Title、Abstract ("ordinal generation depth estimation")、§3.1 (depth ≥2 collapse)
- 问题：标题和摘要使用 "ordinal depth estimation" 暗示多级或连续估计能力，但实际只有三类（gen-0/gen-1/gen-2+）。Appendix D (5-class evaluation) 显示 F1 降至 ≤0.50，depth 2–4 mutually indistinguishable。Appendix G 的混淆矩阵进一步显示 gen-2+ 的主要错误是被判为 gen-1（86% 二分类错误为假阴性）。实质上这更接近 "binary detection with a gen-0/gen-1 boundary enhancement" 而非 ordinal estimation。
- 为什么影响接收：Framing 与实际能力之间的差距会被审稿人视为 overselling。如果只能区分三类且 gen-1/gen-2+ 边界很弱，"ordinal" 一词误导读者对方法能力的预期。
- 建议修改方向：(1) 标题和 Abstract 应更精确地描述为 "3-class depth classification" 或 "coarse ordinal depth estimation"。(2) §3.1 应在正文（不仅是附录）明确讨论三类上限的原因和影响。(3) 考虑在 Abstract 中直接说明 "depths beyond 2 are collapsed due to feature convergence"。

**N3** [critical] 下游应用实验 (§4.4 / Appendix L) 削弱而非支撑核心动机
- 具体位置：§4.4 "Downstream Utility"、Table 18 (Appendix L)、Introduction 第1段 "quality-aware data curation"
- 问题：Introduction 将 depth estimation 的动机之一定位为 "quality-aware data curation"（p1, "complicating provenance tracking and quality-aware data curation"）。但 §4.4 / Table 18 的实验结果显示：在等样本量下，random subsampling (ppl=2.367) 优于 depth-stratified selection (depth 0-1: ppl=2.387) 和 binary filtered (ppl=2.389)。论文诚实报告了这一结果，并得出 "knowing generation depth does not, by itself, make it more or less useful for training"（p17），但这直接矛盾了 Introduction 的 curation 动机。此外，实验仅用 3 seeds，作者自认 minimum achievable p-value = 0.125，统计功效严重不足。
- 为什么影响接收：一项核心动机（data curation）的实验不支持论文叙事。如果保留 curation 动机，需要更有力的实验支撑；如果结论是 depth 信息对 curation 没用，则需要调整 Introduction 的 framing。
- 建议修改方向：(1) 增加 seeds 数量（至少 10+）以获得充分统计功效。(2) 调整 Introduction 的动机叙述——将 data curation 降级为 "potential application" 而非核心动机，或探索更复杂的 depth-aware curation 策略（如非线性加权而非简单过滤）。(3) 如果维持当前实验规模，应在 §4.4 正文中明确标注 "underpowered" 而非仅在 Appendix L 中提及。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 生成器规模受限，缺乏 frontier 模型验证
- 具体位置：§3.2、Table 5 (Appendix A)、Limitations
- 问题：全部 8 个生成器均为 ≤8B 的 base pretrained 模型。无 instruction-tuned 模型（Limitations 中 §6 para 2 简短提及 instruction tuning 实验，但仅限于 OLMo 和 QLoRA fine-tuning），无 RLHF-aligned 模型，无 frontier 模型（GPT-4、Claude 等）。§8 (page 8) 提到 instruction-tuned models "show substantially weaker fingerprints"，这实际上是一个重要的负面发现，但在正文中被压缩到一句。
- 建议：在 Discussion 或 Limitations 中更突出地讨论 instruction tuning 对 depth signal 的削弱，及其对实际部署的影响。这是该方法最大的实际局限。

**W2** [warning] 与 Geng et al. (2026, Markovian Chains) 的差异化不够清晰
- 具体位置：§2.2、Discussion §5
- 问题：Geng et al. (2026) 研究 semantic-preservation 约束下的迭代生成，并发现 "attractor dynamics bounding distinguishable depth to approximately three classes"。这与本文的三类上限高度重合。论文在 §2.2 中仅用两句区分 ("We differ in studying non-paraphrastic continuation chains... and in focusing on estimating depth rather than characterizing convergence")。但如果两篇论文独立发现相似的三类边界，需要更深入的对比：(a) 两种链结构下三类边界是否由相同机制驱动？(b) 特征行为是否一致？
- 建议：增加一段专门与 Geng et al. (2026) 对比的讨论，从机制层面解释差异。

**W3** [warning] Cross-model 链的关键数据（F1=0.809）缺乏表格支撑
- 具体位置：Abstract ("3-class macro F1 = 0.809 on heterogeneous cross-model chains")、§4.1
- 问题：Abstract 引用的核心数字 F1 = 0.809（3-class, cross-model chains）在正文中只有文字叙述（§4.1 "Cross-model generalization" 段落），没有对应的正式表格。相比之下，LOGO 结果有 Table 1 详细报告。作为 Abstract 中最高的 F1 数字，这一结果应该有等价的表格展示。
- 建议：为 cross-model chain evaluation 增加独立表格，包含 per-class F1、macro-average、confidence intervals。

**W4** [warning] 参考模型依赖的局限讨论不足
- 具体位置：§3.3 (Reference-model features)、Table 2
- 问题：5/7 特征依赖参考模型（Pythia-410M）计算 NLL。Table 2 显示跨家族参考模型的 F1 spread 仅 0.013，表明不敏感——这是好消息。但以下问题未讨论：(a) 推理时需要运行参考模型，增加计算开销（至少 410M forward pass per text）；(b) 参考模型对非英语文本的适用性；(c) 当参考模型的训练分布与测试文本差异较大时（如代码、数学文本）是否退化。Appendix J 的跨域实验仅用 Wikipedia/News/Academic/Code 3 个生成器，且在 Academic 域 binary F1 降至 0.628。
- 建议：在 Limitations 中增加参考模型依赖性讨论。

**W5** [warning] Discussion (§5) 部分重复 Results
- 具体位置：§5 第1-3段
- 问题：§5 的前三段大量复述 §4 的发现（shape stationarity、sampling ablation、temperature sensitivity），缺乏超越结果本身的新解释。Discussion 应聚焦于 (a) 理论解释（为什么 shape preserves？与 decoding 机制的关系），(b) 与相关工作的深度对比，(c) 方法的根本局限和未来方向。
- 建议：精简 §5 对结果的复述，增加解释性内容。

---

## 小问题（不影响接收）

- **M1**: §3.3 对 "entropy" 使用了 "shorthand" 的脚注定义（"negative token-level log-likelihood under the reference model"）。这不是标准信息论中的 entropy。建议使用 "reference-model surprisal" 或 "negative log-likelihood (NLL)" 避免混淆。
- **M2**: Table 1 中 "Fam." 列的缩写（Pythia→Pythia, OLMo→OLMo 等）与 "Family" 在其他表格中不一致。应统一。
- **M3**: Appendix D (Finer-Grained Depth) 的 5-class F1 = 0.50 是重要的负面结果，但在正文中只有 Conclusion 末尾一句提及。考虑在 §4 或 §5 中更显著地讨论。
- **M4**: 引用验证显示 `detectgpt` (Mitchell et al., 2023) 和 `pythia` (Biderman et al., 2023) 在 OpenAlex 中未匹配。这可能是 API 问题而非引用错误，但建议检查这两条 bib entry 的元数据完整性。
- **M5**: §3.4 "We use the XGBoost classifier throughout." 一句过于简略。超参数 (n_estimators=200, max_depth, learning_rate) 应在正文方法部分给出，不仅在脚注中。

---

## Questions to Authors

1. **F1 = 0.809 的详细报告**：Abstract 中 cross-model chains 的 3-class macro F1 = 0.809 在正文中没有表格支撑。能否提供含 per-class metrics 和 CI 的完整表格？
2. **DDR vs. model collapse**：DDR 的 shape stationarity 是否在 model collapse 设置中（同一模型迭代训练于自身输出）也成立？如果是，DDR 就不是 depth-specific finding 而是更一般的递归生成性质。
3. **下游实验解读**：random subsampling 优于 depth-stratified selection 的结果如何与 curation 动机调和？是否尝试过更精细的 depth-aware 策略（如按深度加权而非简单过滤）？
4. **Instruction-tuned models**：§8 提到 instruction-tuned models 显示 "substantially weaker fingerprints"。能否量化 "substantially"？这是否意味着该方法在实际部署场景中（大部分 LLM 都是 instruction-tuned）的价值有限？
5. **Feature scalability**：如果未来模型进一步收窄 human-machine 分布差距，7 个手工特征是否还有区分力？是否考虑过 learned features（如 probing LLM hidden states）作为互补？

---

## Missing References

引用整体覆盖尚可（56 entries），但以下方向可考虑补充：
- **Iterative self-refinement 相关**：Madaan et al. (2023, Self-Refine) 等研究迭代 LLM 输出的工作，虽然场景不同但涉及多步生成。
- **Data provenance/attribution 方向**：如 Hammoudeh & Lowd (2024) 关于训练数据溯源的工作，与本文 provenance 动机相关。
- **Stylometric AI detection 方向**：Kumarage et al. (2023) 等使用 stylometric features 做 AI 检测的工作，与本文的 surface features 设计直接相关。

---

## 主要优势

1. **任务定义有价值**：将 AI 文本检测从二分类扩展到序数深度估计是一个自然且有意义的方向。即使当前实际只能区分三类，任务本身的提出为后续研究开辟了空间。
2. **实验设计严谨**：LOGO 交叉验证协议合理消除了 generator leakage；LOFO 分析增强了可解释性；多维鲁棒性测试（长度、prompt 类型、扰动、跨域）覆盖全面。
3. **统计方法得当**：TOST 等价性检验、bootstrap CI、Bonferroni 校正的使用体现了方法论素养。
4. **可复现性好**：特征定义完整可计算，数据构建流程清晰，承诺释放代码和数据。
5. **Limitations 讨论诚实**：直面 single-generator 限制、base-model 约束和两个 scope boundary。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-17T14:08:30.514221+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "**[Round 1 交叉分享 — 请逐条回应 Reviewer 2 的意见]**\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 `[AGREE]` 表示同意并说明理由，或用 `[REBUT]` 表示反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] DDR 相对 model collapse 文献的新颖性不足\n- DDR 的核心发现——递归生成导致分布收窄（词汇多样性下降、可预测性升高）——在 model collapse 文献中已有充分记录（Shumailov et al. 2024, Guo et al. 2024）。本文将这一现象分解为 \"location shift + shape preservation\" 增加了颗粒度，但底层现象并非新发现。§5 \"Relation to model collapse\" 仅两句带过。\n- 认为：如果核心 finding 是已知现象的再确认，论文新颖性主张被实质性削弱。\n\n**N2** [critical] \"Ordinal depth estimation\" framing 与三分类实际能力不匹配\n- 标题和 Abstract 暗示多级或连续估计能力，但只有三类（gen-0/gen-1/gen-2+）。5-class F1 ≤ 0.50。实质更接近 \"binary detection with gen-0/gen-1 boundary enhancement\"。\n- 认为：\"ordinal\" 一词误导对方法能力的预期。\n\n**N3** [critical] 下游应用实验削弱而非支撑核心动机\n- Introduction 将 depth estimation 动机定位为 \"quality-aware data curation\"，但 §4.4 实验显示 random subsampling 优于 depth-stratified selection。论文诚实报告但这矛盾了 Introduction 的 curation 动机。实验仅用 3 seeds，统计功效不足。\n- 认为：核心动机的实验不支持论文叙事。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** 生成器规模受限，缺乏 frontier 模型验证（全部 ≤8B base models）\n**W2** 与 Geng et al. (2026, Markovian Chains) 的差异化不够清晰（三类边界高度重合）\n**W3** Cross-model 链 F1=0.809 缺乏表格支撑（Abstract 引用的核心数字无正式表格）\n**W4** 参考模型依赖的局限讨论不足（推理开销、非英语、跨域退化）\n**W5** Discussion §5 部分重复 Results（前三段大量复述 §4 发现）\n\n---\n\n请对以上每条给出你的 [AGREE] 或 [REBUT] 回应。注意：你已经提出了自己的 N1（gen-0 泄漏）、N2（instruction tuning）、N3（采样敏感性）问题，现在需要独立评估 Reviewer 2 的观点是否成立。",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "**[Round 1 交叉分享 — 请逐条回应 Reviewer 2 的意见]**\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 `[AGREE]` 表示同意并说明理由，或用 `[REBUT]` 表示反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] DDR 相对 model collapse 文献的新颖性不足\n- DDR 的核心发现——递归生成导致分布收窄（词汇多样性下降、可预测性升高）——在 model collapse 文献中已有充分记录（Shumailov et al. 2024, Guo et al. 2024）。本文将这一现象分解为 \"location shift + shape preservation\" 增加了颗粒度，但底层现象并非新发现。§5 \"Relation to model collapse\" 仅两句带过。\n- 认为：如果核心 finding 是已知现象的再确认，论文新颖性主张被实质性削弱。\n\n**N2** [critical] \"Ordinal depth estimation\" framing 与三分类实际能力不匹配\n- 标题和 Abstract 暗示多级或连续估计能力，但只有三类（gen-0/gen-1/gen-2+）。5-class F1 ≤ 0.50。实质更接近 \"binary detection with gen-0/gen-1 boundary enhancement\"。\n- 认为：\"ordinal\" 一词误导对方法能力的预期。\n\n**N3** [critical] 下游应用实验削弱而非支撑核心动机\n- Introduction 将 depth estimation 动机定位为 \"quality-aware data curation\"，但 §4.4 实验显示 random subsampling 优于 depth-stratified selection。论文诚实报告但这矛盾了 Introduction 的 curation 动机。实验仅用 3 seeds，统计功效不足。\n- 认为：核心动机的实验不支持论文叙事。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** 生成器规模受限，缺乏 frontier 模型验证（全部 ≤8B base models）\n**W2** 与 Geng et al. (2026, Markovian Chains) 的差异化不够清晰（三类边界高度重合）\n**W3** Cross-model 链 F1=0.809 缺乏表格支撑（Abstract 引用的核心数字无正式表格）\n**W4** 参考模型依赖的局限讨论不足（推理开销、非英语、跨域退化）\n**W5** Discussion §5 部分重复 Results（前三段大量复述 §4 发现）\n\n---\n\n请对以上每条给出你的 [AGREE] 或 [REBUT] 回应。注意：你已经提出了自己的 N1（gen-0 泄漏）、N2（instruction tuning）、N3（采样敏感性）问题，现在需要独立评估 Reviewer 2 的观点是否成立。",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-17T14:08:48.227259+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17713
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-17T14:08:48.829205+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "**[Round 1 交叉分享 — 请逐条回应 Reviewer 1 的意见]**\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 `[AGREE]` 表示同意并说明理由，或用 `[REBUT]` 表示反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] gen-0 seed 共享导致 LOGO 3-class 结果膨胀\n- ~1,000 条 Wikipedia 种子文本作为 gen-0 被所有 8 个 generator 共享。LOGO 评估中 test set 的 gen-0 与 train set 的 gen-0 是完全相同文本。gen-0 准确率 99.1%（Table 10），远高于 gen-1 (56.9%) 和 gen-2+ (74.0%)。\n- 论文虽报告了 leak-free binary F1=0.694，但 headline 仍用 3-class F1=0.809。\n- 认为：headline 结果被泄漏 inflate，Contribution 1 可信度打折。\n\n**N2** [critical] Instruction tuning 完全破坏 depth signal，但 framing 不匹配\n- OLMo-Instruct F1=0.338 vs base 0.763。但 Abstract/Introduction 的 framing 未限定 scope 为 base models only，暗示通用性和实用性（\"provenance tracking\", \"data curation\"）。\n- 认为：一个仅适用于 base model 的方法，其 practical motivation 在实际中不成立。\n\n**N3** [critical] 采样参数敏感性极高\n- t=1.0 时退化为近随机水平。所有主实验仅在 t=0.7 下进行。\n- 认为：depth signal 可能只是 low-temperature entropy 变化的间接产物，非 recursive generation 的 intrinsic property。方法依赖于 high-probability regions 主导的生成。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** \"Location shift\" claim 缺乏正式统计检验（无 KS/AD test，无 Q-Q plot）\n**W2** TOST equivalence margin ±2% 的选择缺乏理论依据\n**W3** Baseline repurposing 可能不公平（统一 XGBoost 超参可能不利于某些 baseline）\n**W4** gen-1/gen-2 边界区分力不足但未充分讨论实际影响（error rate 48.42%）\n**W5** 数据多样性不足（Wikipedia only + limited cross-domain 评估）\n\n---\n\n请对以上每条给出你的 [AGREE] 或 [REBUT] 回应。注意：你已经提出了自己的 N1（DDR 新颖性）、N2（ordinal framing）、N3（downstream utility）问题，现在需要独立评估 Reviewer 1 的观点是否成立。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "**[Round 1 交叉分享 — 请逐条回应 Reviewer 1 的意见]**\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 `[AGREE]` 表示同意并说明理由，或用 `[REBUT]` 表示反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] gen-0 seed 共享导致 LOGO 3-class 结果膨胀\n- ~1,000 条 Wikipedia 种子文本作为 gen-0 被所有 8 个 generator 共享。LOGO 评估中 test set 的 gen-0 与 train set 的 gen-0 是完全相同文本。gen-0 准确率 99.1%（Table 10），远高于 gen-1 (56.9%) 和 gen-2+ (74.0%)。\n- 论文虽报告了 leak-free binary F1=0.694，但 headline 仍用 3-class F1=0.809。\n- 认为：headline 结果被泄漏 inflate，Contribution 1 可信度打折。\n\n**N2** [critical] Instruction tuning 完全破坏 depth signal，但 framing 不匹配\n- OLMo-Instruct F1=0.338 vs base 0.763。但 Abstract/Introduction 的 framing 未限定 scope 为 base models only，暗示通用性和实用性（\"provenance tracking\", \"data curation\"）。\n- 认为：一个仅适用于 base model 的方法，其 practical motivation 在实际中不成立。\n\n**N3** [critical] 采样参数敏感性极高\n- t=1.0 时退化为近随机水平。所有主实验仅在 t=0.7 下进行。\n- 认为：depth signal 可能只是 low-temperature entropy 变化的间接产物，非 recursive generation 的 intrinsic property。方法依赖于 high-probability regions 主导的生成。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** \"Location shift\" claim 缺乏正式统计检验（无 KS/AD test，无 Q-Q plot）\n**W2** TOST equivalence margin ±2% 的选择缺乏理论依据\n**W3** Baseline repurposing 可能不公平（统一 XGBoost 超参可能不利于某些 baseline）\n**W4** gen-1/gen-2 边界区分力不足但未充分讨论实际影响（error rate 48.42%）\n**W5** 数据多样性不足（Wikipedia only + limited cross-domain 评估）\n\n---\n\n请对以上每条给出你的 [AGREE] 或 [REBUT] 回应。注意：你已经提出了自己的 N1（DDR 新颖性）、N2（ordinal framing）、N3（downstream utility）问题，现在需要独立评估 Reviewer 1 的观点是否成立。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-17T14:08:50.186782+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1357
}
```

</details>

---


### Assistant

_source line 418 · 2026-05-17T14:08:54.322761+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 419 · 2026-05-17T14:08:56.920280+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0/5 (Findings)。三个 Must-Fix 问题：(1) DDR 相对 model collapse 文献新颖性不足；(2) "ordinal depth estimation" framing 与三分类实际能力不匹配；(3) 下游 curation 实验为负面结果，削弱核心动机。论文实验设计严谨、可复现性好，但技术贡献（7 个经典特征 + XGBoost）和核心发现的增量有限，适合 Findings 而非主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 420 · 2026-05-17T14:09:05.108945+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 421 · 2026-05-17T14:12:33.526725+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 逐条评估 Reviewer 1 意见

---

## Must-Fix 问题

### [AGREE] R1-N1: gen-0 seed 共享导致 LOGO 3-class 结果膨胀

同意这是一个有效的方法论问题，但需要修正 R1 的部分论述。

**同意的部分**：LOGO 中 gen-0 数据泄漏是事实。Table 10 (Appendix G) 的 gen-0 accuracy 99.1% vs. gen-1 56.9%、gen-2+ 74.0% 差距悬殊，3-class macro F1 确实被 gen-0 的近完美识别拉高。LOGO 3-class F1 = 0.762 不能作为方法在未见过 generator 上的可靠估计。

**需要修正的部分**：R1 说 "headline 仍用 3-class F1=0.809"，但 0.809 是 cross-model chains（5-fold CV）的结果而非 LOGO 结果。在 5-fold CV 中，gen-0 文本被随机分入 train/test，不存在 LOGO 那样的全量泄漏问题。因此 Abstract 的 headline 数字（0.809）可能不受此问题影响。不过论文确实应该在正文中更清晰地区分这两个评估设置的 gen-0 处理方式。

**补充论据**：论文在 §4.1 (page 5) 已明确承认此问题："the 3-class metric may carry upward bias from memorized gen-0 patterns; we therefore also report a leak-free binary metric (gen-1 vs. gen-2+): F1 = 0.694"。这说明作者意识到了泄漏，但处理方式（补充 binary 数字）不够充分。更好的做法是：(a) 在 LOGO 中为每个 held-out generator 重新采样独立的 gen-0 seeds；或 (b) 在 Abstract 中以 leak-free binary 或 cross-model 数字为主，降低 LOGO 3-class 的突出程度。

**与我的 N2 的关系**：此问题进一步支撑了我提出的 "ordinal framing 被三分类能力削弱" 的观点。如果 gen-0 识别依赖泄漏，那么方法的实际区分力更多体现在 gen-1 vs. gen-2+（F1=0.694），进一步缩小了 "ordinal estimation" 的实际意义。

---

### [AGREE] R1-N2: Instruction tuning 破坏 depth signal，framing 不匹配

同意，且这与我的 W1（generator 规模受限）高度相关。

**核心论据**：OLMo-Instruct LOGO F1 = 0.338 vs. base 0.763（§8, page 8），几乎退化到三分类随机水平（0.33）。论文在 Limitations 中解释为 "Length regulation and format constraints imposed by alignment alter the distributional variation"，但这一发现的实际影响被严重低估。

**Framing 问题确实存在**：Abstract 说 "Studying eight base models from five families"，确实提到了 "base models"，但 Introduction 的动机叙述（"provenance tracking and quality-aware data curation"，page 1）暗示了现实场景的适用性。在 2026 年，绝大多数部署的 LLM 都是 instruction-tuned/RLHF-aligned，web-crawled text 中来自 base model 的文本比例持续下降。一个仅在 base model 上有效的方法，其实用性 claim 需要更多论证。

**建议**：(a) Abstract 和 Introduction 的 scope 声明应从开头就限定为 base pretrained models；(b) 将 instruction tuning 的负面结果从 Limitations 的简短提及提升到 Discussion §5 中作为重要发现讨论；(c) 讨论 base model 在 pre-training data curation 场景中仍然相关的原因（如 Common Crawl 中的 model-generated text 可能来自 base model inference APIs）。

---

### [REBUT] R1-N3: 采样参数敏感性 — 部分反驳

R1 的敏感性担忧有效，但 "退化为近随机水平" 和 "非递归生成的 intrinsic property" 的结论过强。

**反驳"近随机水平"**：Table 12 (Appendix H, page 14) 显示 t=1.0 时 F1 下降约 8pp（从 0.762 降至约 0.68）。三分类随机水平为 0.33，0.68 仍远高于随机。R1 说 "退化为近随机水平" 与论文数据不符。退化是 significant 但非 catastrophic。

**反驳"非 intrinsic property"**：R1 认为 depth signal 只是 low-temperature entropy 变化的间接产物。但论文在 §5 (page 7) 和 Appendix H 的分析中提供了更 nuanced 的解释：temperature 影响的是 distributional drift 的积累速度，而非 drift 的存在与否。在 t=1.0 下，entropy-depth correlation 确实接近零（r ≈ −0.002），但这说明的是 entropy-based features 在高温下失效，不代表深度信号本身不存在。surface features（TTR、hapax ratio）在高温下可能仍保有信号（论文未单独报告，这是一个缺失）。

**同意的部分**：(a) 所有主实验在 t=0.7 单一设置下进行，确实限制了结论的 generalizability；(b) entropy-depth 相关性在 t=1.0 下的崩溃表明 5/7 features（reference-model 类）对采样温度高度敏感；(c) 论文应在 §4 正文（不仅在 Appendix H）中更突出地报告温度敏感性，并讨论在部署中如何处理未知温度的场景。

**建议**：R1 的担忧应促使作者 (a) 在 Appendix 中增加 t=1.0 下各特征子集的分解分析（surface vs. reference 特征哪个更 robust？），(b) 在 Discussion 中明确将 t ∈ [0.5, 0.9] 作为方法的有效工作范围。但将此升级为 "method is fundamentally flawed" 的 critical issue 证据不足。

---

## Should-Fix 问题

### [AGREE] R1-W1: "Location shift" claim 缺乏正式统计检验

同意。论文对 DDR 的 "location shift + shape preservation" claim 仅依赖 Spearman 相关系数和 Figure 1 的视觉展示。这对于一个 distributional 层面的 claim 是不够的。

具体建议：(a) 对不同深度的 NLL 分布进行两样本 KS 检验，检验 location shift 是否显著；(b) 用 Levene's test 或 Brown-Forsythe 检验 shape/variance stationarity；(c) Q-Q plot 可以直观展示分布形状的相似性。这些都是 standard 工具，添加成本低，但会大幅增强 DDR claim 的 rigor。

---

### [AGREE] R1-W2: TOST equivalence margin ±2% 缺乏理论依据

同意。TOST 检验中 equivalence margin 的选择直接影响结论的可信度。±2% 意味着如果 depth-stratified 与 random subsampling 的 perplexity 差距 < 2%，就被视为 "等价"。但论文未解释为什么 2% 是 "practically negligible" 的合理阈值。

对于语言模型 perplexity，2% 可能是一个 meaningful 差异（取决于绝对值和应用场景）。论文应参照目标任务的实际需求或领域惯例来选择 margin，并报告不同 margin（如 1%、3%、5%）下 TOST 结论的敏感性。

---

### [AGREE with nuance] R1-W3: Baseline repurposing 可能不公平

**部分同意，但 R1 的担忧可能被夸大**。论文在 §4.3 (page 6, Table 4) 中将 detection baselines（Avg-LogProb、FastDetectGPT、Binoculars、LD-Score）的原始 score 作为特征输入 XGBoost，使用统一的分类框架。这种做法在 feature-comparison 研究中是标准方法——固定 classifier，隔离 feature set 的贡献。

然而 R1 的合理担忧是：这些 baseline 原本是 binary detectors，直接输入 XGBoost 做 3-class ordinal 并不是它们的设计用途。更公平的对比应包括：(a) 为每个 baseline 独立调参（至少 grid search max_depth, n_estimators）；(b) 报告这些 baseline 在其原始 binary task 上的表现作为参照。

Appendix H (page 14) 部分缓解了这一担忧：logistic regression、random forest 等 alternative classifiers 也产生一致的排序，表明 discriminative power 主要来自 features 而非 classifier choice。但 R1 的建议仍有价值——独立调参可以消除这一疑虑。

---

### [AGREE] R1-W4: gen-1/gen-2 边界区分力不足

强烈同意，且这与我的 N2（ordinal framing）直接相关。

Table 10 (Appendix G, page 14) 显示 gen-2+ 被误判为 gen-1 的比例为 48.42%（R1 数字正确），几乎等于硬币翻转。Appendix K (page 16) 确认 gen-1/gen-2+ 边界是 "primary failure point"。这意味着方法的实际分辨力集中在 gen-0 vs. non-gen-0 这条线上，gen-1 和 gen-2+ 之间的区分非常弱。

论文声称 "ordinal depth estimation" 但最关键的序数边界（gen-1/gen-2+）错误率接近 50%。这不是一个小问题，而是对核心 claim 的实质性削弱。在 Discussion §5 或 Limitations 中需要更坦诚地讨论这一点，而非将其埋在 Appendix 中。

---

### [AGREE] R1-W5: 数据多样性不足

同意。主实验全部基于 Wikipedia seeds，Appendix J 的跨域评估仅覆盖 News、Academic、Code 三个域，各仅 200 seeds × 3 generators。Academic 域的 binary F1 降至 0.628 (page 16, Table 16)，显示域迁移存在显著退化。

对于一篇声称 provenance tracking 实用性的论文，仅靠 Wikipedia 数据不足以支撑通用性 claim。建议至少增加一个 real-world web crawl 数据的评估（如从 C4/OSCAR 采样种子文本）。

---

## 综合判断

R1 的三个 Must-Fix 中，N1（gen-0 泄漏）和 N2（instruction tuning）是有力的技术论点，我给予 AGREE。N3（温度敏感性）的担忧有效但结论过强，我给予 partial REBUT——方法在 t=0.7 下有效这一事实仍有实际意义，但确实需要更清晰的 scope 限定。

R1 的五个 Should-Fix 均有合理性，我对 W1-W5 全部给予 AGREE（W3 带 nuance）。

综合 R1 的意见后，我维持 Overall Assessment = 3.0 (Findings) 不变。R1 的 N1 进一步削弱了 LOGO 3-class 数字的可信度（但 cross-model 0.809 可能不受影响），N2 强化了 practical scope 的局限性。这些与我自己的 N2（ordinal framing）和 N3（downstream utility）形成互补，共同指向同一个核心结论：论文是一个执行良好的实证研究，但新颖性有限且实际影响力受 scope restrictions 约束，适合 Findings track。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 422 · 2026-05-17T14:12:39.160873+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 39

## Round 39

2 recorded events


### User

_source line 423 · 2026-05-17T14:12:42.900811+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。要点总结：

- **R1-N1 (gen-0 泄漏)**: AGREE — LOGO 中 gen-0 确实存在数据泄漏，但修正了 R1 的论述：Abstract headline 0.809 来自 cross-model 5-fold CV 而非 LOGO，可能不受此问题影响。
- **R1-N2 (instruction tuning)**: AGREE — F1=0.338 几乎等于随机，framing 确实与 base-model-only 现实不匹配。
- **R1-N3 (温度敏感性)**: REBUT (部分) — R1 "近随机水平" 的说法与数据不符（t=1.0 下 F1≈0.68，远高于 0.33 random），但敏感性担忧本身有效，需要更清晰的工作范围限定。
- **R1-W1~W5**: 全部 AGREE（W3 带 nuance）。

维持 Overall Assessment = 3.0 (Findings) 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 424 · 2026-05-17T14:12:50.267944+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 40

## Round 40

8 recorded events


### User

_source line 425 · 2026-05-17T14:12:51.774836+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 2 的审稿意见

---

## Must-Fix 逐条回应

### [AGREE] R2-N1: DDR 相对 model collapse 文献的新颖性不足

同意此观点，但需加注细微区分。

**同意的部分**: DDR 的核心现象（递归生成导致词汇多样性收缩、entropy 升高）在 model collapse 文献中确实已有记录。Shumailov et al. (2024) 的 "curse of recursion" 和 Guo et al. (2024) 的 "curious decline of linguistic diversity" 均描述了类似的分布收窄趋势。§5 "Relation to model collapse" 仅用两句话带过（"Our inference-chain drift occurs without parameter updates... Topic drift shows weak correlation with depth features (|ρ| < 0.29)"），对与 model collapse 文献的实质性差异化完全不够。论文的 Contribution 2（"We document differential depth response"）如果核心现象已知，贡献就从 "发现" 降级为 "再确认 + 更精细的分解"。

**补充的细微区分**: Model collapse 关注的是 **训练侧退化**（在合成数据上 retrain），而 DDR 关注的是 **推理侧统计指纹**（单次前向推理的 NLL 分布变化）。这个区分是有意义的，但论文完全没有强调这一点。此外，DDR 的 "location shift + shape preservation" 分解提供了比 model collapse 文献更细的颗粒度——但这是一个增量贡献，不是质变。

**建议**: §5 需要扩展为至少一个完整段落，正面对比 DDR 与 model collapse 的异同，明确论证 "推理侧 depth estimation" 为什么不能简单归约为 model collapse 的推论。如果不能做出有说服力的区分，应相应降低 Contribution 2 的 claim 力度。

---

### [AGREE] R2-N2: "Ordinal depth estimation" framing 与三分类实际能力不匹配

完全同意。

**证据**: §5 "Granularity and robustness" 明确承认 "5-class LOGO F1 drops to ≈0.50, with depths 2-4 mutually indistinguishable"。Appendix D Table 6 的 XGBoost 5-class macro F1 = 0.501，仅略高于 5-class 随机基线 (0.20)。即使 QLoRA 端到端学习也只达到 5-class F1 = 0.789（Appendix E Table 6），但论文的主方法（手工特征 + XGBoost）在 5-class 上几乎失效。

在实际操作中，论文的 3-class 设计将 depth 2/3/4 全部合并为 gen-2+。这意味着系统只能区分三个桶：人类原文 / 一次生成 / 多次生成。这更接近 "enhanced binary detection with a gen-0/gen-1 split" 而非真正的 ordinal estimation。"Ordinal" 一词在回归/分类文献中暗示对有序类别的 fine-grained 区分能力（论文自己在 §2.3 引用了 ordinal regression 文献 Gutiérrez et al. 2016, Cao et al. 2020），但当前方法达不到这个预期。

**与我自身 N1 的关联**: 即使在 3-class 中，gen-0 的 99.1% 准确率很可能受 seed 泄漏 inflate。因此实际有效区分力可能仅在 gen-1 vs gen-2+ 这条边界上，binary F1 = 0.684（leak-free）。这进一步支持 R2 的判断：方法的实际能力远低于 "ordinal" framing 的暗示。

---

### [AGREE] R2-N3: 下游应用实验削弱而非支撑核心动机

同意，且我认为问题比 R2 描述的更严重。

**证据**: Appendix L Table 18 的数据明确显示：
- All depths (n=12,299): PPL = 2.335 ± 0.000（最优）
- Size-matched random (n=3,951): PPL = 2.367 ± 0.000
- Depth 0-1 only (n=3,951): PPL = 2.367 ± 0.000（与 random **完全相同**）
- Binary-filtered (n=3,951): PPL = 2.389 ± 0.000
- Depth-1 only (n=797): PPL = 2.644 ± 0.000

这告诉我们两件事：(1) depth-stratified selection 在等量采样下 **等同于** random subsampling；(2) 使用所有数据（包括深层生成文本）反而给出最低 perplexity。这直接反驳了 Introduction 的 "quality-aware data curation" 动机：如果深层生成文本不仅无害反而有益（因为增加了数据量），那么 depth estimation 对 curation 的价值何在？

论文在 §6 将此框架为 "Detectable ≠ harmful"（Contribution 3），试图把负结果变成正面贡献。但这个 reframing 有逻辑问题：如果 depth 对下游无影响，那么 depth detection 本身的实用动机就被瓦解了——你检测到了一个不 matter 的属性。

**关于统计功效**: R2 提到 "仅用 3 seeds"。确认 Table 18 注释："mean ± std across 3 seeds"。3 个 random seeds 仅提供 2 个自由度的方差估计。虽然 n=3,951 样本的 TOST 在 ±2% margin 下达到 p < 0.001，但 fine-tuning 的随机性（初始化、batch 顺序）仅通过 3 次重复来估计，这确实不够 robust。至少需要 5-10 seeds 才能对 TOST 的结论有信心。

---

## Should-Fix 逐条回应

### [AGREE] R2-W1: 生成器规模受限，缺乏 frontier 模型验证

同意。所有 8 个 generator 均为 ≤8B base models（Pythia 410M-1B, OLMo 1B-2-1B, Qwen 0.6B-1.7B, Llama 3.2-3B, Mistral 7B）。这些模型的参数量和能力远低于实际广泛使用的 frontier models (GPT-4, Claude, Llama-70B+)。DDR 的 "location shift" 可能是小模型的 artifacts（小模型的 output distribution 更尖锐/受限，因此 recursive generation 的 drift 更明显），frontier models 可能不exhibit 同样的 monotonic drift。这与我自身 N2（instruction tuning 失效）和 N3（采样参数敏感性）形成一个 convergent concern：**论文展示的 DDR 可能是 small base model + low temperature 的特定现象，而非 LLM text generation 的通用属性**。

---

### [AGREE] R2-W2: 与 Geng et al. (2026, Markovian Chains) 的差异化不够清晰

部分同意。§2.2 用一句话做了区分："We differ in studying non-paraphrastic continuation chains... and in focusing on estimating depth rather than characterizing convergence." 但这不够。具体差异化缺失：
- Geng et al. 的 "三类边界" 与本文 3-class 设计（gen-0/gen-1/gen-2+）是否实质相同？如果是，则任务定义的独立性受质疑
- 两种方法在相同数据上的性能对比缺失
- "Non-paraphrastic vs paraphrastic" 的区别对 DDR 的影响没有实验验证

不过我未读过 Geng et al. 全文，无法判断 "三类边界高度重合" 的具体程度。建议作者在 revision 中补充正面对比。

---

### [AGREE] R2-W3: Cross-model 链 F1=0.809 缺乏表格支撑

部分同意。Abstract 使用 "heterogeneous cross-model chains (binary F1 = 0.764)" 的措辞存在歧义。实际上：
- 0.809 (3-class) 和 0.762 (binary) 来自 **Table 1 的 8-generator LOGO 评估**（单 generator 链 + cross-generator generalization test）
- 真正的 "cross-model chains"（每步随机选 generator）仅在 **脚注 5** 提及：binary F1 = 0.764 under 5-fold CV，无正式表格
- Abstract 的 "cross-model chains" 可能指 LOGO（which tests cross-model generalization），但也可能被误读为 mixed-generator chains

建议：(1) 为脚注 5 的 cross-model chain 实验补充正式表格；(2) 统一术语——Abstract 使用 "leave-one-generator-out evaluation across heterogeneous generators" 而非 "cross-model chains"。

---

### [AGREE] R2-W4: 参考模型依赖的局限讨论不足

同意。Table 2 仅测试了 3 个 reference models（Pythia-410M, OLMo-1B, Qwen3-0.6B），且全部来自与 generator 重叠的模型家族。以下问题未讨论：
- 推理开销：每个文本需要一次完整的 reference model forward pass（~410M parameters），在大规模 curation 场景下的 throughput 如何？
- 非英语语言：reference model 的 NLL 分布在非英语文本上是否仍然提供有效的 depth signal？
- 跨域退化：Appendix J 的 Academic domain F1 = 0.628 已经显示出显著退化，但论文未分析这是 reference model 还是 feature set 的问题

---

### [AGREE] R2-W5: Discussion §5 部分重复 Results

部分同意。§5 前三段（"Why does shape remain approximately stationary?"、"Prompt-type dependence"、"Practical applicability"）确实在 interpret 之前大量复述了 §4 的数字。例如 "Prompt-type dependence" 段几乎逐字复述了 Appendix C 的结果。但 "Relation to model collapse" 和 "The gen-1/gen-2 boundary" 段提供了新的解释性讨论。建议压缩前三段的数据复述，把空间留给更深入的理论讨论（如 DDR 与 model collapse 的正面对比，回应我们共同关注的 R2-N1）。

---

## 与我自身审稿意见的交叉对照

| R2 问题 | R1 相关问题 | 汇聚/分歧 |
|---------|-----------|----------|
| R2-N1 (DDR novelty) | R1-W1 (location shift claim 缺检验) | 汇聚：DDR 的 claim 基础均需加强 |
| R2-N2 (ordinal framing) | R1-N1 (gen-0 泄漏 inflate) | 汇聚：实际区分力远低于 framing |
| R2-N3 (downstream 矛盾) | R1-W2 (TOST margin 无依据) | 汇聚：Contribution 3 的证据链薄弱 |
| R2-W1 (scale 受限) | R1-N2 (instruction tuning) + R1-N3 (采样敏感) | 汇聚：方法可能仅是 small-base-model + low-temp 特定现象 |

**两位 Reviewer 的 critical concerns 高度一致**：论文的实际区分力和适用范围被当前 framing 显著夸大。R1 从 experimental confounds 角度（泄漏、采样敏感性），R2 从 novelty 和 framing 角度，得出了 convergent 的结论。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-17T14:13:13.411908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-17T14:13:13.412522+00:00_

1	- id: "R1-W1"
2	  summary: "Baseline hyperparameter inconsistency"
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 8
8	  resolution: "method.tex unified to est200/md6. Verified R8."
9	  resolution_round: 8
10	
11	- id: "R1-W5"
12	  summary: "Downstream experiment too small"
13	  category: framing
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 8
18	  resolution: "TOST added. Contribution 3 restored with perplexity scope."
19	  resolution_round: 8
20	
21	- id: "R7-W1"
22	  summary: "gen-0 seed sharing inflating headline"
23	  category: experiment
24	  severity: warning
25	  status: resolved
26	  first_raised_round: 7
27	  last_seen_round: 9
28	  resolution: "Abstract reports both binary and 3-class. Verified R9."
29	  resolution_round: 9
30	
31	- id: "R7-W2"
32	  summary: "DDR mechanism overclaim"
33	  category: method
34	  severity: warning
35	  status: resolved
36	  first_raised_round: 7
37	  last_seen_round: 8
38	  resolution: "Changed to 'tendency of standard decoding'. Confirmed R8."
39	  resolution_round: 8
40	
41	- id: "R7-W3"
42	  summary: "Efficiency not quantified"
43	  category: experiment
44	  severity: warning
45	  status: resolved
46	  first_raised_round: 7
47	  last_seen_round: 8
48	  resolution: "Table 4 ms/text + memory. Confirmed R8."
49	  resolution_round: 8
50	
51	- id: "R7-W4"
52	  summary: "Method novelty divergence"
53	  category: framing
54	  severity: warning
55	  status: open
56	  first_raised_round: 7
57	  last_seen_round: 9
58	  mentions:
59	    - {round: 9, reviewers: "R1,R2", note: "Structural. R1 3.5, R2 3.0→3.5 if C3 fixed."}
60	  action_items:
61	    - {round: 7, action: "Rebuttal triple defense", assigned_to: "Director", status: "open"}
62	  resolution: ""
63	  resolution_round: null
64	
65	- id: "R7-W5"
66	  summary: "Instruct framing"
67	  category: framing
68	  severity: warning
69	  status: resolved
70	  first_rais
…[truncated 4504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-17T14:14:29.106869+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"TOST added. Contribution 3 restored with perplexity scope.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Abstract reports both binary and 3-class.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-N1. Both reviewers agree reporting both numbers is insufficient; headline should use leak-free metric or disjoint seeds. gen-0 accuracy 99.1% vs gen-1 56.9% confirms inflation.\"}\n  action_items:\n    - {round: 10, action: \"Use leak-free binary F1 or generator-disjoint gen-0 seeds as headline; or run ablation with non-overlapping seeds\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Changed to 'tendency of standard decoding'. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Structural. R1 3.5, R2 3.0→3.5 if C3 fixed.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-R2-N1. DDR vs model collapse differentiation still insufficient. §5 'Relation to model collapse' only 2 sentences. Both agree: if DDR is known phenomenon re-confirmed, contribution claim weakened.\"}\n  action_items:\n    - {round: 7, action: \"Rebuttal triple defense\", assigned_to: \"Director\", status: \"open\"}\n    - {round: 10, action: \"Expand §5 model collapse discussion to full paragraph; argue why inference-side DDR != training-side collapse; provide experimental evidence (does shape stationarity hold under model collapse?)\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Instruct framing\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1\", note: \"Resolved: framing shifted to characterization.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-N2. Despite prior fix, Abstract/Intro still imply general applicability ('provenance tracking', 'quality-aware data curation') without explicit base-model scope limitation upfront.\"}\n  action_items:\n    - {round: 10, action: \"Abstract and Introduction first paragraph must explicitly limit scope to base pretrained models; move instruct finding from Limitations to Discussion as important negative result\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1\", note: \"Discussion error analysis added.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred. Error rate 48.42% at gen-1/gen-2 boundary still buried in Appendix. Both agree this undermines 'ordinal' framing and needs prominent discussion in main text.\"}\n  action_items:\n    - {round: 10, action: \"Discuss gen-1/gen-2+ boundary weakness prominently in §4 or §5, not just Appendix K\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added in Introduction. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M3\"\n  summary: \"NLL + topic drift spec\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Fixed. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-M4\"\n  summary: \"Missing references\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"All added. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R8-N1\"\n  summary: \"entropy_std grouping + Figure 1 caption\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Both metrics in Abstract. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-RV2\"\n  summary: \"LOFO delta error\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected to -0.8pp. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n    - {round: 9, action: \"Abstract: 'downstream harm' → 'downstream perplexity degradation'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Abstract L8 qualified. Introduction/Conclusion retain 'harm' with perplexity scope prefix. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises vs 3-class reality\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"5-class F1=0.50, gen-1/gen-2+ error rate 48%. Title/Abstract use 'ordinal' implying fine-grained estimation but actual ability is coarse 3-class with weak gen-1/gen-2+ boundary. Both reviewers agree this is overselling.\"}\n  action_items:\n    - {round: 10, action: \"Revise title/abstract to 'coarse ordinal' or '3-class depth classification'; state depth≥2 collapse reason in main text not just appendix\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation experiment contradicts core motivation\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Random subsampling = depth-stratified at equal N. Full dataset (incl. deep text) gives lowest ppl. Contradicts 'quality-aware data curation' motivation. Only 3 seeds = underpowered. Both agree Contribution 3 evidence chain is weak.\"}\n  action_items:\n    - {round: 10, action: \"Either increase seeds to 10+, or demote curation from core motivation to 'potential application'; adjust Intro framing accordingly\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"R1 flagged as critical (t=1.0 near-random), R2 partial rebut (F1≈0.68 not random but significant drop). Consensus: sensitivity is real, needs prominent discussion in main text and explicit working range [0.5,0.9].\"}\n  action_items:\n    - {round: 10, action: \"Move temperature sensitivity from Appendix H to §4 or §5; state explicit working range; add per-feature-group breakdown at t=1.0\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"Location shift claim lacks formal statistical testing\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both agree. Only evidence is Spearman ρ and visual. No KS/AD test for same-family hypothesis, no Levene's test for shape stationarity, no Q-Q plot.\"}\n  action_items:\n    - {round: 10, action: \"Add KS test + Levene's test + Q-Q plot to support location shift claim, or weaken claim to 'suggestive of'\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"TOST ±2% margin unjustified\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both agree. No theoretical basis for 2% threshold. Should report multiple margins and effect size.\"}\n  action_items:\n    - {round: 10, action: \"Report TOST at multiple margins (1%,3%,5%); add Cohen's d; cite literature for practical significance threshold\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W4\"\n  summary: \"Cross-model F1=0.809 lacks formal table\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Abstract headline number only in text/footnote, no proper table with per-class F1 and CIs.\"}\n  action_items:\n    - {round: 10, action: \"Add formal table for cross-model chain evaluation with per-class metrics and CIs\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Data diversity insufficient (Wikipedia-only seeds)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Main eval Wikipedia-only. Cross-domain (Appendix J) only 3 generators, 200 seeds. Academic F1=0.628 shows significant degradation.\"}\n  action_items:\n    - {round: 10, action: \"Expand cross-domain eval or discuss Wikipedia selection bias prominently\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"Geng et al. (2026) differentiation insufficient\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both find §2.2's 2-sentence differentiation insufficient. Three-class boundary coincidence with Markovian Chains needs mechanistic comparison.\"}\n  action_items:\n    - {round: 10, action: \"Add dedicated comparison paragraph in Related Work or Discussion\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === 历史 (R1-R6) ===\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Direction C. Persists as R7-W4.\"\n  resolution_round: 5\n\n- id: \"R5-TABLE1\"\n  summary: \"Table 1 only 6 generators\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"All 8.\"\n  resolution_round: 6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"TOST added. Contribution 3 restored with perplexity scope.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Abstract reports both binary and 3-class.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-N1. Both reviewers agree reporting both numbers is insufficient; headline should use leak-free metric or disjoint seeds. gen-0 accuracy 99.1% vs gen-1 56.9% confirms inflation.\"}\n  action_items:\n    - {round: 10, action: \"Use leak-free binary F1 or generator-disjoint gen-0 seeds as headline; or run ablation with non-overlapping seeds\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Changed to 'tendency of standard decoding'. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Structural. R1 3.5, R2 3.0→3.5 if C3 fixed.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-R2-N1. DDR vs model collapse differentiation still insufficient. §5 'Relation to model collapse' only 2 sentences. Both agree: if DDR is known phenomenon re-confirmed, contribution claim weakened.\"}\n  action_items:\n    - {round: 7, action: \"Rebuttal triple defense\", assigned_to: \"Director\", status: \"open\"}\n    - {round: 10, action: \"Expand §5 model collapse discussion to full paragraph; argue why inference-side DDR != training-side collapse; provide experimental evidence (does shape stationarity hold under model collapse?)\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Instruct framing\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1\", note: \"Resolved: framing shifted to characterization.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-N2. Despite prior fix, Abstract/Intro still imply general applicability ('provenance tracking', 'quality-aware data curation') without explicit base-model scope limitation upfront.\"}\n  action_items:\n    - {round: 10, action: \"Abstract and Introduction first paragraph must explicitly limit scope to base pretrained models; move instruct finding from Limitations to Discussion as important negative result\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 8, reviewers: \"R1\", note: \"Discussion error analysis added.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred. Error rate 48.42% at gen-1/gen-2 boundary still buried in Appendix. Both agree this undermines 'ordinal' framing and needs prominent discussion in main text.\"}\n  action_items:\n    - {round: 10, action: \"Discuss gen-1/gen-2+ boundary weakness prominently in §4 or §5, not just Appendix K\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added in Introduction. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M3\"\n  summary: \"NLL + topic drift spec\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Fixed. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-M4\"\n  summary: \"Missing references\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"All added. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R8-N1\"\n  summary: \"entropy_std grouping + Figure 1 caption\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Both metrics in Abstract. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-RV2\"\n  summary: \"LOFO delta error\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected to -0.8pp. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n    - {round: 9, action: \"Abstract: 'downstream harm' → 'downstream perplexity degradation'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Abstract L8 qualified. Introduction/Conclusion retain 'harm' with perplexity scope prefix. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises vs 3-class reality\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"5-class F1=0.50, gen-1/gen-2+ error rate 48%. Title/Abstract use 'ordinal' implying fine-grained estimation but actual ability is coarse 3-class with weak gen-1/gen-2+ boundary. Both reviewers agree this is overselling.\"}\n  action_items:\n    - {round: 10, action: \"Revise title/abstract to 'coarse ordinal' or '3-class depth classification'; state depth≥2 collapse reason in main text not just appendix\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation experiment contradicts core motivation\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Random subsampling = depth-stratified at equal N. Full dataset (incl. deep text) gives lowest ppl. Contradicts 'quality-aware data curation' motivation. Only 3 seeds = underpowered. Both agree Contribution 3 evidence chain is weak.\"}\n  action_items:\n    - {round: 10, action: \"Either increase seeds to 10+, or demote curation from core motivation to 'potential application'; adjust Intro framing accordingly\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"R1 flagged as critical (t=1.0 near-random), R2 partial rebut (F1≈0.68 not random but significant drop). Consensus: sensitivity is real, needs prominent discussion in main text and explicit working range [0.5,0.9].\"}\n  action_items:\n    - {round: 10, action: \"Move temperature sensitivity from Appendix H to §4 or §5; state explicit working range; add per-feature-group breakdown at t=1.0\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"Location shift claim lacks formal statistical testing\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both agree. Only evidence is Spearman ρ and visual. No KS/AD test for same-family hypothesis, no Levene's test for shape stationarity, no Q-Q plot.\"}\n  action_items:\n    - {round: 10, action: \"Add KS test + Levene's test + Q-Q plot to support location shift claim, or weaken claim to 'suggestive of'\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"TOST ±2% margin unjustified\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both agree. No theoretical basis for 2% threshold. Should report multiple margins and effect size.\"}\n  action_items:\n    - {round: 10, action: \"Report TOST at multiple margins (1%,3%,5%); add Cohen's d; cite literature for practical significance threshold\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W4\"\n  summary: \"Cross-model F1=0.809 lacks formal table\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Abstract headline number only in text/footnote, no proper table with per-class F1 and CIs.\"}\n  action_items:\n    - {round: 10, action: \"Add formal table for cross-model chain evaluation with per-class metrics and CIs\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Data diversity insufficient (Wikipedia-only seeds)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Main eval Wikipedia-only. Cross-domain (Appendix J) only 3 generators, 200 seeds. Academic F1=0.628 shows significant degradation.\"}\n  action_items:\n    - {round: 10, action: \"Expand cross-domain eval or discuss Wikipedia selection bias prominently\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"Geng et al. (2026) differentiation insufficient\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Both find §2.2's 2-sentence differentiation insufficient. Three-class boundary coincidence with Markovian Chains needs mechanistic comparison.\"}\n  action_items:\n    - {round: 10, action: \"Add dedicated comparison paragraph in Related Work or Discussion\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === 历史 (R1-R6) ===\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Direction C. Persists as R7-W4.\"\n  resolution_round: 5\n\n- id: \"R5-TABLE1\"\n  summary: \"Table 1 only 6 generators\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"All 8.\"\n  resolution_round: 6"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-17T14:14:29.214063+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 12785}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 107
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-17T14:16:27.544747+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 10 审稿报告 — Depth Fingerprinting\n\n**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n**目标 Venue**: EMNLP 2026 (ACL Rolling Review)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**轮次**: 1 轮（Step 2 交叉分享后达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n本文提出 ordinal generation depth estimation 任务，将 LLM 文本检测从二分类扩展为三类序数分类（gen-0/gen-1/gen-2+）。基于 8 个 base model（5 个家族，0.6B–8B）构建的非改写续写链（~37K 文本），作者发现 differential depth response (DDR)：中心趋势特征随深度单调漂移，形状特征保持近平稳。7 个手工特征 + XGBoost 在 LOGO 下达到 3-class macro F1=0.762（binary F1=0.694 leak-free）。下游实验通过 TOST 检验论证 depth-stratified selection 等价于 random subsampling。\n\n---\n\n## Strengths\n\n1. **任务定义有价值**: Ordinal depth estimation 是未被前人探索的自然研究方向，将 binary detection 推进为 fine-grained provenance characterization\n2. **实验设计严谨**: LOGO/LOFO 交叉验证、Bootstrap CI、McNemar test、Bonferroni 校正、类平衡子采样等方法论素养突出\n3. **分析深度极佳**: 17 页含 11 个附录，覆盖长度控制、prompt 类型、文本扰动、跨域、采样参数、QLoRA、下游效用等多维度消融\n4. **DDR 框架有启发性**: location shift + shape preservation 的二分法提供了理解递归生成的新视角\n5. **可复现性好**: 特征定义完整、超参明确、软件版本记录、承诺开源\n6. **Limitations 讨论诚实**: 直面 instruction tuning 限制、base-model 约束、temperature 依赖\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，Reviewer 共识）\n\n**[M1] gen-0 seed 共享导致 LOGO 3-class 结果膨胀** (R1-N1, R2 AGREE)\n- LOGO 中 test generator 的 gen-0 与 train generator 的 gen-0 是完全相同的 Wikipedia 文本。gen-0 准确率 99.1% vs gen-1 56.9%/gen-2+ 74.0%（Table 10）。3-class F1 被 gen-0 的近完美识别人为拉高。\n- 论文虽报告 leak-free binary F1=0.694，但 headline 仍突出 3-class metrics。\n- R2 修正：Abstract 的 0.809 来自 cross-model 5-fold CV（非 LOGO），可能不受此问题影响，但论文术语混淆了两个评估设置。\n- **要求**: 以 leak-free metric 为 headline，或用 generator-disjoint seeds 重跑并量化 inflation 程度。\n\n**[M2] Instruction tuning 完全破坏 signal，但 framing 未限定 scope** (R1-N2, R2 AGREE)\n- OLMo-Instruct LOGO F1=0.338（≈三分类随机）vs base 0.763。\n- Abstract/Introduction 使用 \"provenance tracking\"、\"quality-aware data curation\" 等暗示通用性的表述，未在开头限定为 base models only。\n- 2026 年绝大多数部署 LLM 均为 instruction-tuned，一个仅对 base model 有效的方法其 practical motivation 需要重新论证。\n- **要求**: Abstract/Intro 开头明确限定 scope；将 instruct 负面结果从 Limitations 提升到 Discussion 作为重要发现；论证 base model 场景的实际相关性。\n\n**[M3] DDR 相对 model collapse 文献新颖性论证不足** (R2-N1, R1 AGREE)\n- DDR 的核心现象（递归生成→词汇多样性下降→分布收窄）在 Shumailov et al. (2024), Guo et al. (2024) 中已有记录。\n- §5 \"Relation to model collapse\" 仅两句带过，未系统论证 inference-side DDR 与 training-side collapse 的实质差异。\n- R1 补充：DDR 的 \"location shift + shape preservation\" 分解是增量贡献，非质变。\n- **要求**: 扩展 §5 为完整对比段落；提供实验证据（如 shape stationarity 在 model collapse 设置中是否也成立？）\n\n**[M4] \"Ordinal depth estimation\" framing 与三分类实际能力不匹配** (R2-N2, R1 AGREE)\n- 5-class F1≤0.50，depth 2–4 mutually indistinguishable。gen-1/gen-2+ 边界 error rate 48.42%（接近随机）。\n- \"Ordinal\" 在统计文献中暗示 fine-grained ordered estimation，但实际只能区分三类，且最关键边界很弱。\n- 结合 M1，实际有效区分力可能仅在 gen-0 vs non-gen-0 这条线上。\n- **要求**: 标题/Abstract 精确描述为 \"coarse ordinal\" 或 \"3-class depth classification\"；在正文（非仅附录）讨论三类上限原因和 gen-1/gen-2+ 边界困难。\n\n**[M5] 下游 curation 实验削弱核心动机** (R2-N3, R1 AGREE)\n- Table 18: depth-stratified (ppl=2.387) = random subsampling (ppl=2.367)；full dataset (ppl=2.335) 最优。直接反驳 \"quality-aware data curation\" 动机。\n- 仅 3 seeds，统计功效严重不足（min achievable p=0.125 对部分比较）。\n- R1 补充：如果 depth 对下游无影响，depth detection 的实用动机被瓦解——检测了一个不 matter 的属性。\n- **要求**: 增加 seeds 至 10+ 以获得充分统计功效；或将 curation 从核心动机降级为 \"potential application\"；调整 Introduction framing。\n\n### Should-Fix（6 项）\n\n**[S1] Temperature 敏感性需正文讨论** (R1-N3, R2 partial REBUT)\n- t=1.0 下 F1 降约 8pp（0.762→~0.68），非 \"近随机\" 但退化显著。所有主实验仅 t=0.7。\n- R2 修正 R1 的过强表述，但两者同意：需明确工作范围 [0.5, 0.9]，并在正文讨论。\n- **要求**: 将 Appendix H 核心结论移入 §4 或 §5；增加 t=1.0 下 surface vs reference 特征分解分析。\n\n**[S2] \"Location shift\" claim 缺正式检验** (R1-W1, R2 AGREE)\n- 仅有 Spearman ρ 和 Figure 1 视觉证据，无 KS/AD test、Levene's test、Q-Q plot。\n- **要求**: 补充分布检验或降低 claim 强度（\"consistent with\"→\"suggestive of\"）。\n\n**[S3] TOST ±2% margin 无理论依据** (R1-W2, R2 AGREE)\n- 未解释为何 2% perplexity 差异是 \"practically negligible\"。\n- **要求**: 报告多 margin (1%/3%/5%) 结果 + Cohen's d。\n\n**[S4] Cross-model F1=0.809 缺正式表格** (R2-W3, R1 AGREE)\n- Abstract headline 数字仅在文字/脚注中出现，无 per-class metrics 和 CI 表格。\n- **要求**: 为 cross-model chain evaluation 添加正式表格。\n\n**[S5] 数据多样性不足** (R1-W5, R2 AGREE)\n- Wikipedia-only seeds。跨域仅 3 generators × 200 seeds，Academic F1=0.628 显示显著退化。\n- **要求**: 扩大跨域评估或在正文突出讨论 selection bias。\n\n**[S6] Geng et al. (2026) 差异化不够清晰** (R2-W2, R1 AGREE)\n- 两篇独立发现相似的三类边界，但 §2.2 仅两句区分。\n- **要求**: 增加专门对比段落，从机制层面解释差异。\n\n### Nice-to-Fix（5 项）\n\n- [P1] \"entropy\" 术语与信息论冲突，建议统一为 \"reference-model surprisal\" 或明确定义\n- [P2] Appendix E QLoRA F1=0.905 对主方法选择的 implication 未在正文讨论\n- [P3] Baseline repurposing 应独立调参（至少 grid search），或论证统一超参的合理性\n- [P4] Discussion §5 前三段复述 Results，应压缩并增加解释性内容\n- [P5] 参考模型依赖（推理开销、非英语适用性）应在 Limitations 增加讨论\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| gen-0 泄漏 inflate | Critical (N1) | AGREE | ✓ |\n| Instruction tuning + framing | Critical (N2) | AGREE | ✓ |\n| DDR novelty vs model collapse | AGREE | Critical (N1) | ✓ |\n| Ordinal framing overpromise | AGREE | Critical (N2) | ✓ |\n| Downstream contradicts motivation | AGREE | Critical (N3) | ✓ |\n| Temperature sensitivity | Critical (N3) | Partial REBUT | 部分共识 |\n| Location shift claim | Should-Fix (W1) | AGREE | ✓ |\n| TOST margin | Should-Fix (W2) | AGREE | ✓ |\n| Baseline fairness | Should-Fix (W3) | AGREE (nuance) | ✓ |\n| gen-1/gen-2 boundary | Should-Fix (W4) | AGREE | ✓ |\n| Data diversity | Should-Fix (W5) | AGREE | ✓ |\n\n---\n\n## Reviewer Divergence\n\n**唯一分歧: R1-N3 温度敏感性的严重程度**\n- R1 表述: \"t=1.0 时退化为近随机水平\"（升级为 critical）\n- R2 修正: \"t=1.0 下 F1≈0.68，远高于随机 0.33；退化 significant 但非 catastrophic\"（降为 should-fix）\n- **Director 判断**: R2 的修正有数据支撑（Appendix H Table 12），R1 \"近随机\" 的措辞不准确。但敏感性本身是真实问题，归入 Should-Fix [S1]。\n\n---\n\n## Questions to Authors\n\n1. 如果在 LOGO 中使用 generator-disjoint gen-0 seeds，3-class F1 下降多少？\n2. DDR 的 shape stationarity 在 model collapse 设置（retrain on own output）中是否也成立？\n3. t=0.8/0.9 中间温度下，surface features (TTR, hapax) 是否比 reference features 更 robust？\n4. Downstream utility：是否尝试过更精细的 depth-aware 策略（如按深度加权而非简单过滤）？\n5. QLoRA F1=0.905 vs 手工特征 0.809——为何不以 QLoRA 为主方法？\"Interpretability\" 是否足以作为理由？\n\n---\n\n## Missing References\n\n- Madaan et al. (2023, Self-Refine): 迭代 LLM 输出优化，涉及多步生成\n- Hammoudeh & Lowd (2024): 训练数据溯源，与 provenance 动机相关\n- Kumarage et al. (2023): Stylometric features 做 AI 检测，与 surface features 直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n项目未配置外部审稿，本轮无外部审稿结果。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 (Findings)**\n\n**置信度: 4 / 5** (两位 Reviewer 均熟悉相关文献，对论文进行了完整深入阅读)\n\n**核心判断**: 论文的任务定义新颖、实验设计严谨、分析覆盖全面，是一篇执行良好的实证研究。但五个 Must-Fix 问题共同指向一个核心结论：**论文的实际区分力（leak-free binary F1=0.694）和适用范围（base model + t≤0.9 + continuation chains）被当前 framing 显著夸大**。DDR 相对 model collapse 文献的增量有限，下游实验为负面结果，\"ordinal\" framing 与三分类实际能力不匹配。\n\n如果作者能 (1) 用 leak-free metrics 重构 headline，(2) 限定 scope 并调整 framing，(3) 正面论证 DDR vs model collapse 的差异，(4) 诚实面对 downstream negative result 的含义，本文可以成为一篇坚实的 **Findings** 论文。当前状态不足以支撑主会议录用。\n\n---\n\n## Detailed Comments (按章节)\n\n### Abstract\n- 0.809 (cross-model) 作为 headline 数字可能不受 gen-0 泄漏影响，但与 LOGO 0.762 的关系需澄清\n- \"complicating provenance tracking and quality-aware data curation\" 的 motivation claim 被 §4.4 实验反驳\n- 建议在 Abstract 中明确 \"base pretrained models\" scope\n\n### Introduction\n- §1 para 1 的 motivation（recursive contamination → quality degradation）被 downstream 实验否定\n- Contribution 3 (\"Detectable ≠ harmful\") 试图把负结果变成正面贡献，但逻辑上瓦解了 detection 的实用动机\n- 建议重新定位动机为 \"characterization/scientific understanding\" 而非 \"practical curation\"\n\n### Method\n- §3.2 gen-0 seed sharing 的 rationale 清晰，但对 leakage 后果的处理不够\n- §3.3 \"entropy\" shorthand 与信息论冲突，建议用 \"NLL\" 或 \"reference surprisal\"\n- §3.4 XGBoost 统一超参的合理性论证不充分\n\n### Results\n- Table 1 呈现清晰，但 gen-0 inflation 问题需要 footnote 或 caveat\n- §4.2 DDR claim 需要 formal distributional tests 支撑\n- §4.3 \"competitive at lower cost\" claim 对 4-det ensemble 的表述需要更精确（3-class 0.774 vs 0.795 = 2.1pp 差距）\n\n### Discussion\n- \"Relation to model collapse\" 段需大幅扩展\n- \"Practical applicability\" 段的 corpus-level flagging 论述有价值，建议突出\n- gen-1/gen-2+ boundary 分析应从 Appendix 移入正文\n\n### Limitations\n- 已相当全面和诚实\n- 建议增加：参考模型依赖、非英语泛化、computation overhead 量化",
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 10 审稿报告 — Depth Fingerprinting\n\n**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n**目标 Venue**: EMNLP 2026 (ACL Rolling Review)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n**轮次**: 1 轮（Step 2 交叉分享后达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n本文提出 ordinal generation depth estimation 任务，将 LLM 文本检测从二分类扩展为三类序数分类（gen-0/gen-1/gen-2+）。基于 8 个 base model（5 个家族，0.6B–8B）构建的非改写续写链（~37K 文本），作者发现 differential depth response (DDR)：中心趋势特征随深度单调漂移，形状特征保持近平稳。7 个手工特征 + XGBoost 在 LOGO 下达到 3-class macro F1=0.762（binary F1=0.694 leak-free）。下游实验通过 TOST 检验论证 depth-stratified selection 等价于 random subsampling。\n\n---\n\n## Strengths\n\n1. **任务定义有价值**: Ordinal depth estimation 是未被前人探索的自然研究方向，将 binary detection 推进为 fine-grained provenance characterization\n2. **实验设计严谨**: LOGO/LOFO 交叉验证、Bootstrap CI、McNemar test、Bonferroni 校正、类平衡子采样等方法论素养突出\n3. **分析深度极佳**: 17 页含 11 个附录，覆盖长度控制、prompt 类型、文本扰动、跨域、采样参数、QLoRA、下游效用等多维度消融\n4. **DDR 框架有启发性**: location shift + shape preservation 的二分法提供了理解递归生成的新视角\n5. **可复现性好**: 特征定义完整、超参明确、软件版本记录、承诺开源\n6. **Limitations 讨论诚实**: 直面 instruction tuning 限制、base-model 约束、temperature 依赖\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，Reviewer 共识）\n\n**[M1] gen-0 seed 共享导致 LOGO 3-class 结果膨胀** (R1-N1, R2 AGREE)\n- LOGO 中 test generator 的 gen-0 与 train generator 的 gen-0 是完全相同的 Wikipedia 文本。gen-0 准确率 99.1% vs gen-1 56.9%/gen-2+ 74.0%（Table 10）。3-class F1 被 gen-0 的近完美识别人为拉高。\n- 论文虽报告 leak-free binary F1=0.694，但 headline 仍突出 3-class metrics。\n- R2 修正：Abstract 的 0.809 来自 cross-model 5-fold CV（非 LOGO），可能不受此问题影响，但论文术语混淆了两个评估设置。\n- **要求**: 以 leak-free metric 为 headline，或用 generator-disjoint seeds 重跑并量化 inflation 程度。\n\n**[M2] Instruction tuning 完全破坏 signal，但 framing 未限定 scope** (R1-N2, R2 AGREE)\n- OLMo-Instruct LOGO F1=0.338（≈三分类随机）vs base 0.763。\n- Abstract/Introduction 使用 \"provenance tracking\"、\"quality-aware data curation\" 等暗示通用性的表述，未在开头限定为 base models only。\n- 2026 年绝大多数部署 LLM 均为 instruction-tuned，一个仅对 base model 有效的方法其 practical motivation 需要重新论证。\n- **要求**: Abstract/Intro 开头明确限定 scope；将 instruct 负面结果从 Limitations 提升到 Discussion 作为重要发现；论证 base model 场景的实际相关性。\n\n**[M3] DDR 相对 model collapse 文献新颖性论证不足** (R2-N1, R1 AGREE)\n- DDR 的核心现象（递归生成→词汇多样性下降→分布收窄）在 Shumailov et al. (2024), Guo et al. (2024) 中已有记录。\n- §5 \"Relation to model collapse\" 仅两句带过，未系统论证 inference-side DDR 与 training-side collapse 的实质差异。\n- R1 补充：DDR 的 \"location shift + shape preservation\" 分解是增量贡献，非质变。\n- **要求**: 扩展 §5 为完整对比段落；提供实验证据（如 shape stationarity 在 model collapse 设置中是否也成立？）\n\n**[M4] \"Ordinal depth estimation\" framing 与三分类实际能力不匹配** (R2-N2, R1 AGREE)\n- 5-class F1≤0.50，depth 2–4 mutually indistinguishable。gen-1/gen-2+ 边界 error rate 48.42%（接近随机）。\n- \"Ordinal\" 在统计文献中暗示 fine-grained ordered estimation，但实际只能区分三类，且最关键边界很弱。\n- 结合 M1，实际有效区分力可能仅在 gen-0 vs non-gen-0 这条线上。\n- **要求**: 标题/Abstract 精确描述为 \"coarse ordinal\" 或 \"3-class depth classification\"；在正文（非仅附录）讨论三类上限原因和 gen-1/gen-2+ 边界困难。\n\n**[M5] 下游 curation 实验削弱核心动机** (R2-N3, R1 AGREE)\n- Table 18: depth-stratified (ppl=2.387) = random subsampling (ppl=2.367)；full dataset (ppl=2.335) 最优。直接反驳 \"quality-aware data curation\" 动机。\n- 仅 3 seeds，统计功效严重不足（min achievable p=0.125 对部分比较）。\n- R1 补充：如果 depth 对下游无影响，depth detection 的实用动机被瓦解——检测了一个不 matter 的属性。\n- **要求**: 增加 seeds 至 10+ 以获得充分统计功效；或将 curation 从核心动机降级为 \"potential application\"；调整 Introduction framing。\n\n### Should-Fix（6 项）\n\n**[S1] Temperature 敏感性需正文讨论** (R1-N3, R2 partial REBUT)\n- t=1.0 下 F1 降约 8pp（0.762→~0.68），非 \"近随机\" 但退化显著。所有主实验仅 t=0.7。\n- R2 修正 R1 的过强表述，但两者同意：需明确工作范围 [0.5, 0.9]，并在正文讨论。\n- **要求**: 将 Appendix H 核心结论移入 §4 或 §5；增加 t=1.0 下 surface vs reference 特征分解分析。\n\n**[S2] \"Location shift\" claim 缺正式检验** (R1-W1, R2 AGREE)\n- 仅有 Spearman ρ 和 Figure 1 视觉证据，无 KS/AD test、Levene's test、Q-Q plot。\n- **要求**: 补充分布检验或降低 claim 强度（\"consistent with\"→\"suggestive of\"）。\n\n**[S3] TOST ±2% margin 无理论依据** (R1-W2, R2 AGREE)\n- 未解释为何 2% perplexity 差异是 \"practically negligible\"。\n- **要求**: 报告多 margin (1%/3%/5%) 结果 + Cohen's d。\n\n**[S4] Cross-model F1=0.809 缺正式表格** (R2-W3, R1 AGREE)\n- Abstract headline 数字仅在文字/脚注中出现，无 per-class metrics 和 CI 表格。\n- **要求**: 为 cross-model chain evaluation 添加正式表格。\n\n**[S5] 数据多样性不足** (R1-W5, R2 AGREE)\n- Wikipedia-only seeds。跨域仅 3 generators × 200 seeds，Academic F1=0.628 显示显著退化。\n- **要求**: 扩大跨域评估或在正文突出讨论 selection bias。\n\n**[S6] Geng et al. (2026) 差异化不够清晰** (R2-W2, R1 AGREE)\n- 两篇独立发现相似的三类边界，但 §2.2 仅两句区分。\n- **要求**: 增加专门对比段落，从机制层面解释差异。\n\n### Nice-to-Fix（5 项）\n\n- [P1] \"entropy\" 术语与信息论冲突，建议统一为 \"reference-model surprisal\" 或明确定义\n- [P2] Appendix E QLoRA F1=0.905 对主方法选择的 implication 未在正文讨论\n- [P3] Baseline repurposing 应独立调参（至少 grid search），或论证统一超参的合理性\n- [P4] Discussion §5 前三段复述 Results，应压缩并增加解释性内容\n- [P5] 参考模型依赖（推理开销、非英语适用性）应在 Limitations 增加讨论\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| gen-0 泄漏 inflate | Critical (N1) | AGREE | ✓ |\n| Instruction tuning + framing | Critical (N2) | AGREE | ✓ |\n| DDR novelty vs model collapse | AGREE | Critical (N1) | ✓ |\n| Ordinal framing overpromise | AGREE | Critical (N2) | ✓ |\n| Downstream contradicts motivation | AGREE | Critical (N3) | ✓ |\n| Temperature sensitivity | Critical (N3) | Partial REBUT | 部分共识 |\n| Location shift claim | Should-Fix (W1) | AGREE | ✓ |\n| TOST margin | Should-Fix (W2) | AGREE | ✓ |\n| Baseline fairness | Should-Fix (W3) | AGREE (nuance) | ✓ |\n| gen-1/gen-2 boundary | Should-Fix (W4) | AGREE | ✓ |\n| Data diversity | Should-Fix (W5) | AGREE | ✓ |\n\n---\n\n## Reviewer Divergence\n\n**唯一分歧: R1-N3 温度敏感性的严重程度**\n- R1 表述: \"t=1.0 时退化为近随机水平\"（升级为 critical）\n- R2 修正: \"t=1.0 下 F1≈0.68，远高于随机 0.33；退化 significant 但非 catastrophic\"（降为 should-fix）\n- **Director 判断**: R2 的修正有数据支撑（Appendix H Table 12），R1 \"近随机\" 的措辞不准确。但敏感性本身是真实问题，归入 Should-Fix [S1]。\n\n---\n\n## Questions to Authors\n\n1. 如果在 LOGO 中使用 generator-disjoint gen-0 seeds，3-class F1 下降多少？\n2. DDR 的 shape stationarity 在 model collapse 设置（retrain on own output）中是否也成立？\n3. t=0.8/0.9 中间温度下，surface features (TTR, hapax) 是否比 reference features 更 robust？\n4. Downstream utility：是否尝试过更精细的 depth-aware 策略（如按深度加权而非简单过滤）？\n5. QLoRA F1=0.905 vs 手工特征 0.809——为何不以 QLoRA 为主方法？\"Interpretability\" 是否足以作为理由？\n\n---\n\n## Missing References\n\n- Madaan et al. (2023, Self-Refine): 迭代 LLM 输出优化，涉及多步生成\n- Hammoudeh & Lowd (2024): 训练数据溯源，与 provenance 动机相关\n- Kumarage et al. (2023): Stylometric features 做 AI 检测，与 surface features 直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n项目未配置外部审稿，本轮无外部审稿结果。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 (Findings)**\n\n**置信度: 4 / 5** (两位 Reviewer 均熟悉相关文献，对论文进行了完整深入阅读)\n\n**核心判断**: 论文的任务定义新颖、实验设计严谨、分析覆盖全面，是一篇执行良好的实证研究。但五个 Must-Fix 问题共同指向一个核心结论：**论文的实际区分力（leak-free binary F1=0.694）和适用范围（base model + t≤0.9 + continuation chains）被当前 framing 显著夸大**。DDR 相对 model collapse 文献的增量有限，下游实验为负面结果，\"ordinal\" framing 与三分类实际能力不匹配。\n\n如果作者能 (1) 用 leak-free metrics 重构 headline，(2) 限定 scope 并调整 framing，(3) 正面论证 DDR vs model collapse 的差异，(4) 诚实面对 downstream negative result 的含义，本文可以成为一篇坚实的 **Findings** 论文。当前状态不足以支撑主会议录用。\n\n---\n\n## Detailed Comments (按章节)\n\n### Abstract\n- 0.809 (cross-model) 作为 headline 数字可能不受 gen-0 泄漏影响，但与 LOGO 0.762 的关系需澄清\n- \"complicating provenance tracking and quality-aware data curation\" 的 motivation claim 被 §4.4 实验反驳\n- 建议在 Abstract 中明确 \"base pretrained models\" scope\n\n### Introduction\n- §1 para 1 的 motivation（recursive contamination → quality degradation）被 downstream 实验否定\n- Contribution 3 (\"Detectable ≠ harmful\") 试图把负结果变成正面贡献，但逻辑上瓦解了 detection 的实用动机\n- 建议重新定位动机为 \"characterization/scientific understanding\" 而非 \"practical curation\"\n\n### Method\n- §3.2 gen-0 seed sharing 的 rationale 清晰，但对 leakage 后果的处理不够\n- §3.3 \"entropy\" shorthand 与信息论冲突，建议用 \"NLL\" 或 \"reference surprisal\"\n- §3.4 XGBoost 统一超参的合理性论证不充分\n\n### Results\n- Table 1 呈现清晰，但 gen-0 inflation 问题需要 footnote 或 caveat\n- §4.2 DDR claim 需要 formal distributional tests 支撑\n- §4.3 \"competitive at lower cost\" claim 对 4-det ensemble 的表述需要更精确（3-class 0.774 vs 0.795 = 2.1pp 差距）\n\n### Discussion\n- \"Relation to model collapse\" 段需大幅扩展\n- \"Practical applicability\" 段的 corpus-level flagging 论述有价值，建议突出\n- gen-1/gen-2+ boundary 分析应从 Appendix 移入正文\n\n### Limitations\n- 已相当全面和诚实\n- 建议增加：参考模型依赖、非英语泛化、computation overhead 量化",
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-17T14:16:31.260300+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3715
}
```

</details>

---


### Assistant

_source line 432 · 2026-05-17T14:16:40.018107+00:00_

审稿报告已投递。

---

**Round 10 审稿完成。**

两位 Reviewer 独立审稿 + 交叉分享后达成高度共识，1 轮即收敛。

**最终评分: 3.0 / 5 (Findings)**

5 个 Must-Fix 问题的核心结论：论文实际区分力（leak-free binary F1=0.694）和适用范围（base model + t≤0.9）被当前 framing 显著夸大。DDR 新颖性有限、"ordinal" 承诺超出三分类能力、下游实验为负面结果。修复 framing 和 scope 限定后，可作为坚实的 Findings 论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 433 · 2026-05-17T14:16:42.612181+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：我对 R2 的 3 个 Must-Fix 和 5 个 Should-Fix 全部给出 **[AGREE]**，无反驳。核心判断：

- **R2-N1 (DDR 新颖性)**: 同意。DDR 底层现象在 model collapse 文献已知，§5 的差异化不足。但补充了"训练侧退化 vs 推理侧指纹"的有意义区分。
- **R2-N2 (ordinal framing)**: 完全同意。5-class F1 ≈ 0.50 证明 "ordinal" 名不副实，实际是 enhanced binary detection。与我自身 N1（gen-0 泄漏）形成汇聚：leak-free binary F1 仅 0.684。
- **R2-N3 (downstream 矛盾)**: 同意且认为更严重。Table 18 显示 depth-stratified = random，使用全部数据反而最优，直接反驳 curation 动机。

两位 Reviewer 的 critical concerns 高度一致：方法的实际区分力和适用范围被当前 framing 显著夸大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 434 · 2026-05-17T14:16:56.708836+00:00_

审稿报告已提交给 Research Director。

**本轮审稿总结**：

- **评分**: 3.0 / 5 (Findings)，两位 Reviewer 一致
- **5 个 Must-Fix**: gen-0 泄漏 inflate headline、instruction tuning 破坏 signal 但 framing 未限定、DDR 新颖性论证不足、"ordinal" framing 与三分类能力不匹配、downstream 实验反驳 curation 动机
- **6 个 Should-Fix**: 温度敏感性需正文讨论、location shift 缺正式检验、TOST margin 无依据、cross-model F1 缺表格、数据多样性不足、Geng et al. 差异化不足
- **核心结论**: 论文执行质量高（实验设计严谨、分析全面），但实际区分力（leak-free binary F1=0.694）和适用范围（base model + t≤0.9）被当前 framing 显著夸大。修正 framing 后可成为坚实的 Findings 论文。

Issue tracker 已同步更新（10 个 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 42

## Round 42

36 recorded events


### User

_source line 435 · 2026-05-17T16:27:26.574913+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-17T16:27:33.090707+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-17T16:27:33.141830+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-17T16:27:36.403406+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 439 · 2026-05-17T16:27:36.453954+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-17T16:27:41.373755+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,update_review_issues,submit_review_report_to_research_director",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,update_review_issues,submit_review_report_to_research_director",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-17T16:27:41.424410+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-17T16:27:45.740548+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-17T16:27:45.791091+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-17T16:27:50.057733+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-17T16:27:50.610365+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (50 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_048_cross_temp_transfer | Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters | — | — | — |\n\n## 待处理\n- multi_domain_t07（准备中）\n- review-exp-a-baseline-ensemble: 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异（准备中）\n- plan-004-prep: Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）（准备中）\n- plan-001-restore（准备中）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **exp_047_multi_domain_t07** (success): Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers ← 基于 exp_043_multi_domain_seeds\n- **multi-domain-seeds** (success): Domain independence: depth fingerprint 的 differential
…[truncated 841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-17T16:27:51.062750+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-17T16:27:53.071846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-17T16:27:53.073046+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{lineno}
11	\linenumbers
12	
13	\graphicspath{{../chart/}}
14	
15	\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\in Non-Paraphrastic LLM Text Chains}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{results}
28	
29	\input{discussion}
30	\input{conclusion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\appendix
37	
38	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
39	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
40	
41	\input{appendix_dataset_stats}
42	
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{End-to-End Depth Classification (QLoRA)}
56	\label{app:qlora}
57	\input{appendix_qlora}
58	
59	\section{Leave-One-Feature-Out Analysis}
60	\label{app:lofo}
61	\input{appendix_lofo}
62	
63	\section{Confusion Matrix}
64	\label{app:confusion}
65	\input{appendix_confusion_matrix}
66	
67	\section{Classifier Sensitivity}
68	\label{app:classifier}
69	\input{appendix_classifier}
70	
71	\section{Robustness to Text Perturbation}
72	\label{app:human-edit}
73	\input{appendix_human_edit}
74	
75	\section{Cross-Domain Generalization}
76	\label{app:domain}
77	\input{appendix_domain}
78	
79	\section{Error Analysis of B
…[truncated 51 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-17T16:27:59.246343+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"}]

Based on the search results, here is information about the EMNLP 2026 Call for P
…[truncated 1804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 8183
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-17T16:28:04.745007+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline page limit format requirements",
  "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline page limit format requirements",
    "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-17T16:28:05.599102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": "80",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "offset": "80",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-17T16:28:05.699816+00:00_

80	\label{app:error-analysis}
81	\input{appendix_error_analysis}
82	
83	\section{Downstream Utility}
84	\label{app:downstream}
85	\input{appendix_downstream}
86	
87	\section{Cross-Model Chain Per-Class Detail}
88	\label{app:cross-model-detail}
89	\input{appendix_cross_model_detail}
90	
91	\section{Feature Distribution Analysis}
92	\label{app:feature-distributions}
93	\input{appendix_feature_distributions}
94	
95	\section{Cross-Temperature Transfer}
96	\label{app:cross-temp}
97	\input{appendix_cross_temp}
98	
99	\end{document}
100	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-17T16:28:22.226657+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline page limit format requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"Upcoming changes from April cycle - reviewing workload requirement","url":"http://aclrollingreview.org/reviewing-workload-requirement/"}]

Based on the search results, here's what I found regarding EMNLP 2026 ARR submission requirements:

## Submission Deadline

Papers must be submitted, at latest, by the ARR 2026 May cycle. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Format Requirements

The search results reference ARR's general format requirements. ARR has abandoned the MS Word Template for conference submissions, and submissions based on the Word template will be desk-rejected starting from March 2026. This indicates that papers must use a different format (typically LaTeX with the official ACL template).

## Length/Page Limit

Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected. However, the specific page limit numbers are not explicitly stated in t
…[truncated 588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 17481
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-17T16:28:26.592898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL rolling review 2026 CFP long paper page limit short paper format",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL rolling review 2026 CFP long paper page limit short paper format",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-17T16:28:27.245130+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-17T16:28:30.912876+00:00_

Web search results for query: "ACL rolling review 2026 CFP long paper page limit short paper format"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here is the information about ACL Rolling Review 2026 paper formats and page limits:

**Page Limits:**
- Short papers: 4 pag
…[truncated 687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 4319
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-17T16:28:30.931058+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml\", \"content\": \"# Literature Map for gen-depth-fingerprint\\n# 递归 LLM 生成链深度指纹识别\\n# Updated: 2026-05-15\\n# Categories: detection, model-collapse, data-quality, stylometry,\\n#             iterative-generation, watermarking, vocabulary-diversity,\\n#             membership-inference, ood-detection, survey\\n# Total: 39 papers\\n\\n##############################################################################\\n# 1. Perplexity-based / Zero-shot Detection\\n##############################################################################\\n\\n- id: detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Mitchell et al.\\\"\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  arxiv: \\\"2301.11305\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补\\\"\\n  key_finding: \\\"机器生成文本倾向于占据模型 log-probability 函数的负曲率区域\\\"\\n\\n- id: gltr\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: \\\"Gehrmann et al.\\\"\\n  year: 2019\\n  venue: \\\"ACL 2019\\\"\\n  arxiv: \\\"1906.04043\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化\\\"\\n  key_finding: \\\"使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%\\\"\\n\\n- id: dna_gpt\\n  title: \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\"\\n  authors: \\\"Yang et al.\\\"\\n  year: 2024\\n  venue: \\\"ICLR 2024\\\"\\n  arxiv: \\\"2305.17359\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析\\\"\\n  key_finding: \\\"截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测\\\"\\n\\n- id: binoculars\\n  tit
…[truncated 1705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3685
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-17T16:28:39.380386+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-17T16:28:40.384882+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml\", \"content\": \"_next_id: 21\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:15 UTC\\n  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class\\n    分类\\n  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost\\n    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 18:10 UTC\\n  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证\\n  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer\\n    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth\\n    信号超越 binary 分类的增量。\\n  related_experiments:\\n  - exp_id: mvp-001\\n    role: primary\\n    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 18:15 UTC\\n  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 \\\"independent signal\\\"\\n    调整为 \\\"complementary signal\\\"\\n  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio\\n    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从\\\"分布指纹独立于表面统计\\\"降为\\\"分布指纹提供互补信号\\\"，核心叙事转为\\n    vocabulary impoverishment as primary depth signal。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 \\\"Feature Complementarity\\n    & Dual Dynamics\\\"；H1/H2 从二选一转为共存\\n  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full\\n    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 \\\"independent signal\\\" 被否定，触发 Plan\\n    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing\\n    更丰富的科学贡献。\\n  related_experiments:\\n  - exp_id: p
…[truncated 1488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-17T16:28:40.785958+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-17T16:28:41.287971+00:00_

- id: "R1-W1"
  summary: "Baseline hyperparameter inconsistency"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 8
  resolution: "method.tex unified to est200/md6. Verified R8."
  resolution_round: 8

- id: "R1-W5"
  summary: "Downstream experiment too small"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 8
  resolution: "TOST added. Contribution 3 restored with perplexity scope."
  resolution_round: 8

- id: "R7-W1"
  summary: "gen-0 seed sharing inflating headline"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 7
  last_seen_round: 10
  mentions:
    - {round: 9, reviewers: "R1,R2", note: "Abstract reports both binary and 3-class."}
    - {round: 10, reviewers: "R1,R2", note: "Recurred as R10-N1."}
  action_items:
    - {round: 10, action: "Use leak-free binary F1 as headline", assigned_to: "Paper Agent", status: "done"}
  resolution: "Cross-model chains (clean 5-fold CV) as headline; binary F1 (leak-free) prominently reported; Table 1 per-class with CIs; Table 2 caption flags gen-0 bias."
  resolution_round: 10

- id: "R7-W2"
  summary: "DDR mechanism overclaim"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 7
  last_seen_round: 8
  resolution: "Changed to 'tendency of standard decoding'. Confirmed R8."
  resolution_round: 8

- id: "R7-W3"
  summary: "Efficiency not quantified"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 7
  last_seen_round: 8
  resolution: "Table 4 ms/text + memory. Confirmed R8."
  resolution_round: 8

- id: "R7-W4"
  summary: "Method novelty divergence"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 7
  last_seen_round: 10
  mentions:
    - {round: 9, reviewers: "R1,R2", note: "Structural."}
    - {round: 10, reviewers: "R1,R2", note: "DDR vs model collapse still insufficient."}
  action_
…[truncated 9877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-17T16:28:41.488786+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ 2>/dev/null | head -5",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ 2>/dev/null | head -5",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-17T16:28:41.639760+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_diagnose_qwen17b-sighup-root-cause_20260514T220218.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01KKBv8YYSr4BXnA8rMB6d8B","type":"tool_result","content":"1\t\"\"\"MCP Server — exposes SSH, W&B, and Registry tools via the Model Context Protocol.\n2\t\n3\tUsage:\n4\t    python -m core.mcp_server          # stdio transport (default, for Claude Code)\n5\t    python -m core.mcp_server --sse    # SSE transport (for remote clients)\n6\t\"\"\"\n7\t\n8\tfrom __future__ import annotations\n9\t\n10\timport json\n11\timport logging\n12\timport os\n13\tfrom dataclasses import asdict\n14\tfrom pathlib import Path\n15\tfrom typing import Any\n16\t\n17\tlogger = logging.getLogger(__name__)\n18\t\n19\tfrom mcp.server.fastmcp import FastMCP\n20\t\n21\tfrom core.tools import (\n22\t    artifacts as artifacts_mod,\n23\t    architecture as architecture_mod,\n24\t    clone_repo as clone_repo_mod,\n25\t    cron, feishu, feishu_group as feishu_group_mod,\n26\t    external_review as external_review_mod,\n27\t    file_parser as file_parser_mod,\n28\t    gpu_monitor as gpu_monitor_mod,\n29\t    image_tools as image_tools_mod,\n30\t    model_registry as model_registry_mod,\n31\t    oss_backup, pai_eas, s3_backup,\n32\t    project_config, registry, ssh, wandb_client, workspace,\n33\t    worker as worker_mod,\n34\t)\n35\t\n36\t# ---------------------------------------------------------------------------\n37\t# Server instance\n38\t# ---------------------------------------------------------------------------\n39\t\n40\tmcp = FastMCP(\n41\t    \"agent-ml-research\",\n42\t    instructions=\"ML research experiment management tools\",\n43\t)\n44\t\n45\t\n46\tdef _tool_result_to_str(result: ssh.ToolResult) -> str:\n47\t    \"\"\"Convert a ToolResult dataclass to a JSON string for MCP response.\"\"\"\n48\t    return json.dumps(asdict(result), ensure_ascii=False, default=str
…[truncated 6696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-17T16:28:46.004755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config in project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config in project config"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-17T16:28:46.055418+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-17T16:29:19.427949+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查**方法严谨性、实验设计、统计声明**。\n\n## 论文信息\n- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## Venue 格式要求\n- Long paper: 8 pages（不含 ethics/limitations/references）\n- ACL LaTeX 模板，`[review]` option\n- Double-blind 匿名审稿\n- 附录允许且参与审稿\n- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n1. **方法严谨性**：特征设计是否合理？分类器选择是否恰当？实验流程有无漏洞？\n2. **实验设计**：对照组设置、消融实验、跨域/跨温度泛化实验是否充分？样本量是否足够？\n3. **统计声明验证**：所有数值声明是否有充分证据支撑？置信区间/显著性检验是否正确使用？是否存在数据泄漏或不公平对比？\n4. **可复现性**：实验细节是否足以复现？超参选择是否说明？\n\n## 历史背景\n此论文已经过 10 轮内部审稿迭代。所有历史 issue（baseline 超参不一致、gen-0 seed 共享、DDR 机制过度声称、温度敏感性等）已标记为 resolved。你需要以全新视角审查当前版本，不要假设已修复的问题一定没问题——验证修复是否完整。\n\n请输出完整审稿报告，结构：Summary → Strengths → Weaknesses（Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查**方法严谨性、实验设计、统计声明**。\n\n## 论文信息\n- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## Venue 格式要求\n- Long paper: 8 pages（不含 ethics/limitations/references）\n- ACL LaTeX 模板，`[review]` option\n- Double-blind 匿名审稿\n- 附录允许且参与审稿\n- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n1. **方法严谨性**：特征设计是否合理？分类器选择是否恰当？实验流程有无漏洞？\n2. **实验设计**：对照组设置、消融实验、跨域/跨温度泛化实验是否充分？样本量是否足够？\n3. **统计声明验证**：所有数值声明是否有充分证据支撑？置信区间/显著性检验是否正确使用？是否存在数据泄漏或不公平对比？\n4. **可复现性**：实验细节是否足以复现？超参选择是否说明？\n\n## 历史背景\n此论文已经过 10 轮内部审稿迭代。所有历史 issue（baseline 超参不一致、gen-0 seed 共享、DDR 机制过度声称、温度敏感性等）已标记为 resolved。你需要以全新视角审查当前版本，不要假设已修复的问题一定没问题——验证修复是否完整。\n\n请输出完整审稿报告，结构：Summary → Strengths → Weaknesses（Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-17T16:29:31.026868+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11598
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-17T16:29:31.338132+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性、Related Work、写作质量**。\n\n## 论文信息\n- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## Venue 格式要求\n- Long paper: 8 pages（不含 ethics/limitations/references）\n- ACL LaTeX 模板，`[review]` option\n- Double-blind 匿名审稿\n- 附录允许且参与审稿\n- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n1. **新颖性**：问题定义是否新颖？方法是否有真正的创新？相比已有 AI-text detection 工作，增量贡献在哪里？是否存在 novelty overclaim？\n2. **完整性**：论文叙事是否完整？各 section 之间逻辑是否连贯？贡献声明是否都有实验支撑？附录内容是否在正文中被恰当引用？\n3. **Related Work**：引用是否充分覆盖直接相关方法、baseline 论文、评测 benchmark？是否遗漏重要工作？positioning 是否准确？\n4. **写作质量**：是否有 AI 写作痕迹（em-dash、-ing phrases、过度分段）？叙事是否像实验报告还是有说服力的故事？Abstract/Introduction 是否有吸引力？\n\n## 历史背景\n此论文已经过 10 轮内部审稿迭代。所有历史 issue 已标记为 resolved。你需要以全新视角审查当前版本——尤其注意：\n- method novelty 的 framing 是否已从 \"方法创新\" 调整为 \"实证/概念贡献\"\n- DDR (Differential Depth Response) 机制声称是否恰当\n- \"ordinal depth estimation\" 在标题中但实际只做 3-class，是否有 framing 问题\n- instruct model 范围限制是否明确\n\n请输出完整审稿报告，结构：Summary → Strengths → Weaknesses（Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性、Related Work、写作质量**。\n\n## 论文信息\n- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## Venue 格式要求\n- Long paper: 8 pages（不含 ethics/limitations/references）\n- ACL LaTeX 模板，`[review]` option\n- Double-blind 匿名审稿\n- 附录允许且参与审稿\n- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n1. **新颖性**：问题定义是否新颖？方法是否有真正的创新？相比已有 AI-text detection 工作，增量贡献在哪里？是否存在 novelty overclaim？\n2. **完整性**：论文叙事是否完整？各 section 之间逻辑是否连贯？贡献声明是否都有实验支撑？附录内容是否在正文中被恰当引用？\n3. **Related Work**：引用是否充分覆盖直接相关方法、baseline 论文、评测 benchmark？是否遗漏重要工作？positioning 是否准确？\n4. **写作质量**：是否有 AI 写作痕迹（em-dash、-ing phrases、过度分段）？叙事是否像实验报告还是有说服力的故事？Abstract/Introduction 是否有吸引力？\n\n## 历史背景\n此论文已经过 10 轮内部审稿迭代。所有历史 issue 已标记为 resolved。你需要以全新视角审查当前版本——尤其注意：\n- method novelty 的 framing 是否已从 \"方法创新\" 调整为 \"实证/概念贡献\"\n- DDR (Differential Depth Response) 机制声称是否恰当\n- \"ordinal depth estimation\" 在标题中但实际只做 3-class，是否有 framing 问题\n- instruct model 范围限制是否明确\n\n请输出完整审稿报告，结构：Summary → Strengths → Weaknesses（Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-17T16:29:32.646940+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1308
}
```

</details>

---


### Assistant

_source line 470 · 2026-05-17T16:29:37.506353+00:00_

Round 1 独立审稿任务已分配完毕。两位 Reviewer 已收到任务：

- **Reviewer 1** → 方法严谨性 + 实验设计 + 统计声明
- **Reviewer 2** → 新颖性 + 完整性 + Related Work + 写作质量

等待两位 Reviewer 返回审稿结果后，进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 471 · 2026-05-17T16:38:51.924959+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿报告

## 论文信息
- **标题**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
- **目标 venue**: EMNLP 2026 (ARR May 2026)
- **审查侧重**: 新颖性、完整性、Related Work、写作质量

---

## Summary

本文提出"ordinal generation depth estimation"任务，将传统的二分类 AI 文本检测（real vs. synthetic）扩展为三分类序数估计（gen-0 / gen-1 / gen-2+）。核心发现是 differential depth response (DDR)：在递归生成链中，central-tendency features（entropy mean、TTR、hapax ratio）随深度单调漂移，而 shape features（entropy max、tail decay）近似不变。基于此设计的 7-feature XGBoost 集成在 8 个 base model 生成器的 LOGO 评估中达到 3-class F1=0.762、binary F1=0.694。等价性检验表明 depth-aware data curation 在等样本量下与随机采样无显著差异。

---

## 主要优势

1. **任务定义新颖且有价值**。将 binary detection 扩展到 ordinal depth estimation 是一个清晰的、有实际动机的 problem formulation。与两篇 concurrent work（broken_telephone, markovian_chains）的定位区分准确且诚实（Section 2.2, lines 23-31 of related_work.tex）。

2. **实验全面且严谨**。论文包含 14 个附录，涵盖 classifier sensitivity、sampling sensitivity、cross-domain、cross-temperature、perturbation robustness、LOFO、QLoRA end-to-end、finer-grained 5-class 等全面消融。统计检验规范（bootstrap CI、McNemar、Bonferroni correction、TOST equivalence testing with margin sensitivity），远超大多数同类投稿。

3. **对局限性的诚实处理**。论文明确承认 base model only 限制、instruction tuning degradation（OLMo-Instruct LOGO F1=0.338）、temperature sensitivity、scale effect 等，并在 Limitations section 详细列出。这种诚实度值得肯定。

4. **DDR finding 本身有趣**。即使是描述性的，drifting vs. stationary features 的分离现象是一个有启发性的实证观察，且跨 3 个 reference model family 一致（Table 2, spread=0.013）。与 model collapse 文献的区分（Discussion, "Relation to model collapse" paragraph）是有见地的。

5. **写作质量整体较高**。Abstract 四要素完整，Introduction 叙事连贯（背景→缺口→洞察→方法→贡献），Related Work 分类清晰且有 positioning。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 标题中 "Ordinal" framing 与实际方法存在根本性矛盾

- 具体位置：Title, Section 3.1, Appendix H (classifier), Appendix C (finer-depth)
- 问题：标题声称 "Ordinal Generation Depth Estimation"，但论文自身证据表明 ordinal structure 在此任务中不提供任何增益。Appendix H 明确写道："CORAL ordinal regression, Frank-Hall reduction yield comparable F1 with overlapping CIs, confirming that 3-class granularity provides insufficient resolution for ranking-aware losses to improve over standard multiclass classification." 5-class 尝试 F1 仅 0.50（Appendix C）。这意味着论文做的实际上是一个 3-class multiclass classification，其中 ordinal 性质完全没有被利用。
- 为什么影响接收：标题和 framing 创造了"序数回归方法论贡献"的预期，但实际贡献是"3-class multiclass task formulation + empirical finding"。审稿人会质疑：如果 ordinal structure 没有帮助，为什么要在标题中突出它？这构成 framing overclaim。
- 建议修改方向：(a) 将标题改为更准确的描述，如 "Generation Depth Classification" 而非 "Ordinal...Estimation"；或 (b) 提供证据证明 ordinal structure 确实有帮助（例如在某些 sub-setting 下 ordinal methods 优于 multiclass），否则降低 ordinal 的 prominence。

**N2** [critical] Base model only 限制严重削弱实际影响力，论文 framing 未充分反映这一点

- 具体位置：Section 1 (Introduction, line 13), Discussion ("Instruction tuning" paragraph), Limitations (lines 1-9)
- 问题：论文限制在 base（pretrained）models，但现实世界几乎所有 LLM 生成文本来自 instruction-tuned/RLHF-aligned 模型。Instruction-tuned 模型的 depth signal 降至近随机（OLMo-Instruct F1=0.338, Qwen3-0.6B chat F1=0.667, length-matched 后 binary F1≈0.50）。论文将此框定为"deliberate design choice to isolate the phenomenon"，但这等于承认 DDR 在实际应用场景中可能不存在。
- 为什么影响接收：Introduction 开篇动机是"Web-crawled pretraining corpora increasingly contain LLM-generated text"和"provenance tracking and corpus-level quality assessment"。但如果方法仅适用于 base model 生成的文本（这在 web 上占极少数），则开篇动机与实际贡献之间存在严重脱节。Contribution 的 practical relevance 被大幅缩减为纯学术/分析性贡献。
- 建议修改方向：(a) 重新 frame Introduction 的动机——不是"解决 web contamination"，而是"理解 recursive generation 的分布特性"，定位为 analytical/scientific contribution 而非 applied tool；(b) 在 abstract 中明确 "base model" scope；(c) 减少 practical applicability 的暗示（如 "corpus-level flagging" 在 Discussion 中的表述）。

**N3** [critical] Gen-0 seed sharing 导致 3-class F1 可能系统性高估，而 Abstract 以此为主要指标

- 具体位置：Abstract (line 7), Section 3.2 (lines 27-30), Table 1 caption
- 问题：所有 generators 共享同一批 gen-0 seeds，因此在 LOGO 评估中，held-out generator 的 gen-0 测试样本在训练集中已出现（以相同文本作为其他 generators 的 gen-0）。论文承认"3-class metric may carry upward bias from memorized gen-0 patterns"，但 Abstract 仍以 3-class F1=0.809（cross-model）和 0.762（LOGO）为首要结果。leak-free binary F1 分别为 0.764 和 0.694，显著更低。
- 为什么影响接收：数据泄漏是实验方法论的根本问题。即使论文已报告 binary 指标，将 potentially-inflated 的 3-class F1 作为 Abstract 和 Introduction 的主打数字仍有误导性。审稿人会质疑实验设计的严谨性。
- 建议修改方向：(a) 在 Abstract 中以 binary F1 为主要指标，3-class 作为辅助；(b) 对 3-class 指标明确标注 caveat，或 (c) 修复数据泄漏（为每个 LOGO fold 使用独立的 gen-0 seeds），这是最干净的方案。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] DDR 的"机制解释"超越了实证证据

- 具体位置：Abstract (line 6), Introduction (line 12), Section 4.2, Discussion ("Why does shape remain approximately stationary?" paragraph)
- 问题：论文反复使用 "consistent with recursive generation inducing a location shift in the NLL distribution while preserving distributional shape" 的措辞。但这一"机制"仅基于 7 个手工特征的行为推断，而非对 NLL distribution 本身的直接分析（例如 KL divergence decomposition、distribution shape tests beyond KS）。Discussion 中的解释（"The softmax architecture and fixed sampling parameters determine distributional shape"）是直觉性的，缺乏理论或实验验证。
- 建议：(a) 弱化措辞——从 "consistent with" 到 "suggestive of" 或直接描述为 empirical pattern；(b) 或者增加直接的 NLL distribution shape analysis（如对 full NLL histogram 做 shape test，而非仅看 max/std 等 summary statistics）。

**W2** [warning] Multi-detector ensemble 在 Table 4 中优于所提方法，削弱了性能 claim

- 具体位置：Table 4 (baselines), Introduction (line 15)
- 问题：Introduction claim "outperforming all individual detection baselines by 6–11 pp"，但 Table 4 显示 4-detector + surface ensemble (3-cl F1=0.795, binary 0.708) 优于 7-feature (0.774, 0.705)。论文以计算效率为理由（9.7 vs 22.8 ms/text, 905 MB vs 2868 MB），但性能差距真实存在。
- 建议：Introduction 的 claim 应更精确——"outperforming all individual baselines" 是准确的，但不应给读者留下"最优方法"的印象。应在 Introduction 中提及 multi-detector ensemble 的 trade-off。

**W3** [warning] 6-gen / 5-gen / 8-gen 子集混用导致数字难以横向比较

- 具体位置：Table 1 (8-gen), Table 2 (5-gen), Table 3 (8-gen), Table 4 (8-gen), Appendix 各处（6-gen）
- 问题：主文使用 8-gen LOGO，cross-model chains 使用 5-gen subset（footnote in results.tex line 13），cross-reference 使用 5-gen，多个附录使用 6-gen（Llama/Mistral 后加入）。虽然 Appendix 开头有 note，但同一论文中如此多的 generator subset 变体使得数字之间的可比性很差。例如 Table 1 的 LOGO avg F1=0.762 vs Table 4 的 7-feature F1=0.774——同为 "8-gen pooled LOGO" 但数字不同，可能因 Table 4 使用了 34,131 subsample（footnote in appendix_dataset_stats）。
- 建议：(a) 在论文某处（可能是 Method 或 Appendix A 开头）提供一个清晰的 table 列出每个 experiment 使用的 generator subset 及 sample size；(b) 解释 Table 1 和 Table 4 中同一方法在 LOGO 下 F1 差异的来源。

**W4** [warning] Contribution 3（downstream utility）本质是 null result，framing 过于乐观

- 具体位置：Introduction contribution 3, Section 4.4, Appendix K
- 问题：TOST 等价检验表明 depth-aware curation 与 random subsampling 无差异。这是一个 null result。论文将其 frame 为 "decoupling detectability from downstream harm"，但同样可以读作 "depth fingerprinting has no practical utility for data curation"。进一步，实验仅在 perplexity 上评估、使用 $n$=3 seeds、且 data scale 极小（3,951 samples），使得"equivalence"的推广性存疑。
- 建议：(a) 更诚实地承认这是一个 null result with caveats（small scale, single metric, few seeds）；(b) 减少在 Abstract/Introduction 中的 prominence，或 (c) 补充更多 downstream task evaluation（例如 downstream task accuracy 而非仅 perplexity）。

**W5** [warning] Temperature t=1.0 时方法失效，但论文对此讨论不足

- 具体位置：Appendix H (sampling sensitivity), Discussion ("Temperature robustness"), Limitations
- 问题：t=1.0 时 entropy mean 的 Spearman ρ 从 -0.60 骤降到 -0.002，F1 下降 6pp。许多实际部署的 LLM 使用 t >= 1.0 或 variable temperature。论文声称 "applies reliably under standard decoding regimes" 但未定义 "standard"。cross-domain 实验甚至使用了 t=1.0 且效果更好，这与 Wikipedia 实验的结论矛盾。
- 建议：对 "standard decoding regime" 给出明确定义（如 t ∈ [0.5, 0.9]），并讨论当 temperature 未知时方法的适用性。

---

## 小问题（不影响接收）

1. **Table 1 vs Table 4 F1 不一致**：Table 1 average 3-cl F1 = 0.762, Table 4 中 7-feature = 0.774，同为 8-gen LOGO 但数字不同。虽然可能是 sample subset 差异（37,058 vs 34,131），但读者会困惑。需在 Table 4 caption 或正文中解释。

2. **entropy 术语使用**：method.tex footnote 1 解释 "entropy" 实为 token-level NLL，不是 Shannon entropy。这个区分重要但仅在 footnote 中出现一次。建议在首次使用时更明确或使用 "NLL" 代替 "entropy" 以避免混淆。

3. **Appendix confusion matrix (Table 5) 使用 6-gen** 但正文 Section 4.1 讨论的是 8-gen LOGO。Confusion matrix 应使用 8-gen 版本或明确标注。

4. **Cross-domain evaluation (Appendix I) 的 temperature 不一致**：使用 t=1.0 而非主实验的 t=0.7，使得 cross-domain 结果无法直接与主实验比较。虽然 supplementary evaluation at t=0.7 的结果在文中有报告，但混合 temperature 设置削弱了 generalization claim 的可信度。

5. **Writing: 少数 AI 写作痕迹**。Introduction line 6 有一处 long relative clause chain ("a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity")。Discussion section 过度使用 `\paragraph{}` 分段，7 个极短段落可合并为 3-4 个自然段。

6. **引用验证**：58 条引用全部有对应 bib entry（无 orphan/missing），48 条 OpenAlex 验证通过，6 条 not_found 系 API 覆盖问题（DetectGPT、XGBoost 等经典论文），4 条 minor mismatch（作者名格式），无虚假引用。引用覆盖度总体良好。

---

## Questions for Authors

Q1. 如果为每个 LOGO fold 使用独立的 gen-0 seeds（消除数据泄漏），3-class F1 会下降多少？这决定了 N3 的严重程度。

Q2. DDR 的 "location shift preserving shape" 解释是否可以用更直接的方式验证？例如对 full token-level NLL distribution 做 location-scale family 检验（如 Anderson-Darling after location-scale normalization），而非仅靠 7 个 summary statistics 推断。

Q3. 论文使用固定 prompt "Continue the following text"。如果每步使用 different random prompts（更接近现实场景），depth signal 是否 survive？Appendix F 的 cross-prompt-type 实验（LOPTO F1=0.753）部分回答了这个问题，但仅限于 Pythia-2.8B 单一生成器。

Q4. Contribution 3 的 TOST 仅使用 3 seeds、一个下游指标（perplexity）、小 scale data。作者是否有计划扩展这一评估？

---

## Missing References

论文引用覆盖总体良好，但以下方向可能存在遗漏：

1. **GPT-2 Output Dataset 和 OpenAI text classifier**（Solaiman et al., 2019 已引用，但 OpenAI 的后续 text classifier work 未讨论）。
2. **M4/SemEval 2024 shared task 的具体参赛方法**（仅引用 task overview paper，未讨论具体方案），特别是 multilingual/multi-model setting 的方法。
3. **Data provenance/lineage tracking** 更广泛的文献（如 data documentation, datasheets for datasets），与 Section 2.4 的 provenance 讨论相关。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0/5 | 实验设计总体严谨，统计检验规范；但 gen-0 seed sharing 泄漏问题（N3）、DDR 机制解释超越证据（W1）、downstream TOST 仅 3 seeds（W4）降低了 soundness。核心 claim 有足够支撑但存在可修复的方法论瑕疵。 |
| **Excitement** | 2.5/5 | 任务定义新颖，DDR finding 有趣；但 base-model-only 限制（N2）使得实际影响力大幅缩减，ordinal framing 名不副实（N1），一个贡献是 null result（W4）。在当前形态下，主要价值是学术分析而非 practical tool。 |
| **Reproducibility** | 4.5/5 | 详细的实验细节、明确的超参数、完整的软件版本、承诺代码释放。扣分点：部分附录使用不同 generator subset 但原因未完全解释。 |
| **Reviewer Confidence** | 4/5 | 我熟悉 AI text detection 和 NLP 实验方法论，仔细阅读了全文及所有附录。对 ordinal regression 的特定理论不及专家深入。 |

---

## Overall Assessment

**Overall**: 3.0 (Findings)

**Confidence**: 4/5

**一句话总结**: 任务定义新颖、实验全面、写作诚实，但 base-model-only 限制严重削弱实际影响力，ordinal framing 与实际方法矛盾，gen-0 数据泄漏和 downstream null result 进一步降低了贡献的 weight——作为 analytical study 适合 Findings 发表，作为 main conference paper 的 excitement 不足。

**详细理由**:

本文最大的贡献是 task formulation（ordinal depth estimation）和 empirical finding（DDR 中 drifting vs. stationary features 的分离）。这两者都是真实的学术贡献，且实验执行质量很高。

但三个根本性问题限制了论文的影响力：

(1) **Scope 太窄**。仅限 base model（0.6B-8B）生成的 continuation chains，instruction-tuned 模型近乎失效。这使得论文的 practical motivation（web contamination tracking、data provenance）与实际贡献之间存在显著 gap。

(2) **Framing 不匹配**。标题强调 "ordinal estimation"，但论文自证 ordinal structure 无增益（CORAL/Frank-Hall 无改善）。实际做的是 3-class multiclass classification，且 gen-2+ 是 catch-all class。DDR 被 branded 为一个 mechanism，但证据仅支持 empirical pattern。

(3) **Performance 并非 state-of-the-art**。Multi-detector ensemble 在 Table 4 中优于所提方法。一个 contribution（downstream utility）是 null result。

如果将论文 reframe 为 "an empirical study of distributional drift in recursive LLM generation chains"（去掉 ordinal overclaim、以 binary F1 为主指标、承认 base-model analytical scope），这是一个扎实的 Findings paper。在当前 framing 下偏向 borderline Findings。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 472 · 2026-05-17T16:38:58.865541+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 473 · 2026-05-17T16:39:02.011072+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

报告核心结论：**Overall 3.0 (Findings)**。三个 Must-Fix 问题：(1) "Ordinal" 标题与实际 3-class multiclass 矛盾，CORAL/Frank-Hall 无增益；(2) Base model only 限制使得 instruction-tuned 模型（实际应用场景）近乎失效（F1=0.338），与开篇 web contamination 动机脱节；(3) Gen-0 seed sharing 造成数据泄漏，3-class F1 可能系统性高估，但 Abstract 仍以此为主打数字。五个 Should-Fix 包括 DDR 机制解释超越证据、multi-detector ensemble 优于所提方法、6/5/8-gen 子集混用、downstream null result framing 过于乐观、temperature 敏感性讨论不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 474 · 2026-05-17T16:39:09.327072+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 45

## Round 45

6 recorded events


### User

_source line 475 · 2026-05-17T16:39:26.615453+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：Depth Fingerprinting

## Summary

本文提出 ordinal generation depth estimation（序数生成深度估计），将 AI 文本检测从二分类（human vs. machine）扩展为三分类（gen-0 / gen-1 / gen-2+）。作者使用来自 5 个家族的 8 个 base model 构建非释义递归生成链，提取 7 个手工特征（Pythia-410M 参考模型下的 NLL 统计量 + 表面词汇多样性指标），并发现 differential depth response (DDR) 模式：部分特征随深度单调漂移（entropy mean, TTR, hapax ratio），而形状特征保持近似平稳（entropy max, tail decay）。XGBoost 分类器在 LOGO（Leave-One-Generator-Out）评估下达到 3-class macro F1 = 0.762，cross-model chains 下达到 0.809。

---

## Strengths

**S1. 问题定义有价值且及时。** 随着递归生成文本（LLM 输出重新作为输入）在网络中日益增多，从 binary detection 扩展到 ordinal depth estimation 是自然且有意义的研究方向。

**S2. 评估协议严谨。** LOGO cross-validation 是测试跨生成器泛化的正确选择。论文还提供了 cross-model chains、length confound analysis（Appendix B）、temperature sensitivity（Appendix H）、perturbation robustness（Appendix I）、cross-domain（Appendix J）、LOFO（Appendix F）等大量消融和补充实验，覆盖面广。

**S3. 透明报告已知缺陷。** 论文明确承认 gen-0 seed 共享导致的潜在偏差（§4.1），并报告了 leak-free binary metric（gen-1 vs. gen-2+, F1 = 0.694）。Limitations 部分坦诚讨论了 base-model-only 的限制。

**S4. DDR 框架提供可解释洞察。** 将特征分解为 drifting（location shift）和 stationary（shape preservation）两类，提供了关于递归生成如何影响文本分布的清晰直觉。Spearman 相关性和 KS 检验为此提供了量化支撑（§4.2, Figure 2）。

**S5. 统计方法学规范。** Bonferroni 校正、percentile bootstrap CI、TOST 等价性检验、KS 检验等统计工具的使用总体得当。

**S6. 轻量级且可复现。** 仅需一个 410M 参考模型 + 7 个特征 + XGBoost，计算成本极低（1.48M 参数），这在该领域有实际价值。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Abstract framing 误导，headline metric 受 gen-0 数据泄漏膨胀**
- 具体位置：Abstract (p1), §4.1 (p5), §3.2 (p3)
- 问题：Gen-0 是共享的 Wikipedia 原文，在 LOGO 下，held-out generator 的 gen-0 文本与训练集中其他 generator 的 gen-0 文本完全相同，构成 gen-0 类的数据泄漏。3-class LOGO F1 = 0.762 因近乎完美的 gen-0 分类而膨胀。Leak-free binary metric（gen-1 vs. gen-2+）仅为 F1 = 0.694，低了 6.8 个点。更严重的是，Abstract 以"3-class macro F1 = 0.809 on heterogeneous cross-model chains"开头——这是使用标准 5-fold CV（generator 出现在训练和测试中）的更简单设定，而更有意义的 LOGO 结果（0.762）被置于次要位置，leak-free binary（0.694）完全未出现在 Abstract 中。
- 为什么影响接收：审稿人和读者会以 0.809 作为主要结果，高估方法实际能力。该任务真正的跨生成器、无泄漏性能是 0.694。这种 framing 方式在顶会审稿中会被视为 overclaiming。
- 建议：(a) Abstract 中必须报告 leak-free binary F1 = 0.694，明确标注 LOGO 为 primary metric；(b) 将 cross-model chains 的 0.809 标注为 secondary/optimistic metric；(c) 理想方案是为每个 generator 使用不同的 seed set，从根本上消除泄漏。

**N2** [critical] **仅限 base model，实际适用性严重受限**
- 具体位置：Limitations (p8), Discussion §5 (p7-8)
- 问题：全部 8 个 generator 均为 base（pretrained）model。Discussion 中提到的唯一 instruction-tuned 实验（OLMo-Instruct）LOGO F1 暴跌至 0.338。现实中，网络上 LLM 生成的文本绝大多数来自 instruction-tuned / RLHF / chat model。论文在 §1 中以网络文本污染和数据质量作为动机，但方法无法处理这一最主要的场景。
- 为什么影响接收：§1 的实际动机与 §4 的实验范围存在根本性断裂。如果方法在 instruction-tuned model 上失效，那么论文的实际贡献局限于对 base model 生成动力学的分析性理解，而非实用检测工具。审稿人会质疑 paper 声称的实际影响力。
- 建议：(a) 至少在主实验中加入 2-3 个 instruction-tuned model（如 Llama-3-chat, Mistral-Instruct）的完整评估；(b) 如果 instruction-tuned 结果确实差，需要诚实地将 contribution 重新框定为理论/分析性研究，而非实用检测方案。

**N3** [critical] **Gen-1 / gen-2+ 区分能力弱，削弱 ordinal estimation 核心声明**
- 具体位置：Appendix G confusion matrix (p15), §4.1 (p5), §5 (p7)
- 问题：混淆矩阵显示 35.5% 的 gen-2 样本和 37.8% 的 gen-3 样本被错分为 gen-1。§5 承认 binary depth-2 error rate 为 48%。这意味着方法无法可靠区分文本经过了一次还是多次递归生成——而这正是 ordinal depth estimation 相对于 binary detection 的核心价值。
- 为什么影响接收：论文的 central claim 是 ordinal depth estimation，但证据表明方法主要成功在于识别 gen-0（人类文本），这接近于传统 binary detection。"Ordinal" 能力在 gen-1 / gen-2+ 边界上近乎随机（48% error rate）。这使得论文标题中的 "Ordinal Generation Depth Estimation" 有 overclaim 之嫌。
- 建议：(a) 更显著地承认 ordinal estimation 目前主要在 coarse 层面有效（human vs. generated），gen-1/gen-2+ 区分是一个 open challenge；(b) 探索更丰富的特征集（n-gram patterns, positional features）或 fine-tuned classifier 来改善深度区分；(c) 调整论文 framing，将 gen-1/gen-2+ 区分定位为 preliminary finding 而非 solved problem。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **参考模型特征可能携带 generator-family 偏差**
- 具体位置：§3.3 (p4-5), Table 2 (p6)
- 问题：所有 reference-model features 在 Pythia-410M 下计算。对于 Pythia 家族的 generator（Pythia-1B, Pythia-2.8B），参考模型与 generator 架构相关且训练数据可能重叠，这可能产生系统性不同的特征分布。Table 2 展示了 3 个参考模型的交叉验证，但未分析 same-family vs. cross-family generator-reference pair 的差异。
- 建议：分别报告 same-family（Pythia ref + Pythia gen）和 cross-family（Pythia ref + non-Pythia gen）组合的 per-generator F1。

**W2** [warning] **Tail decay 特征的 rank 范围选择缺乏理论支撑**
- 具体位置：§3.3 (p5)
- 问题：Tail decay 对 vocabulary tokens 在 ranks 100-1000 范围内的 sorted log-probability 拟合线性回归。为什么是 100-1000？不同范围（如 50-500, 200-2000）可能产生不同特征特性。
- 建议：补充 rank 范围消融或提供理论动机。

**W3** [warning] **温度敏感性削弱泛化声明**
- 具体位置：Appendix H (p16), §5 (p7-8)
- 问题：主实验使用 t=0.7（低于标准 t=1.0）。在 t=1.0 下性能下降 ~6pp，t=1.6 下进一步恶化。论文承认高温度注入足够随机性以 flatten distributional drift。但 t=0.7 并非典型的 LLM 使用温度（很多应用用 t=0.8-1.0），主实验在 t=0.7 下可能过于乐观。
- 建议：以 t=1.0 作为主实验温度，或在正文（而非仅 Appendix）中明确讨论温度对结果的影响。

**W4** [warning] **Downstream utility 实验为负面结果，削弱实际动机**
- 具体位置：Appendix L (p19)
- 问题：TOST 等价性检验显示 depth-aware data curation 与 random subsampling 在 downstream fine-tuning perplexity 上统计等价（margin ±2%, p < 0.001）。这意味着知道生成深度对数据 curation 毫无帮助，削弱了 §1 和 §2.4 中的 data quality 动机。
- 建议：在正文 Discussion 中显式讨论这一负面结果及其 implication，而非仅放在 Appendix L。如果 depth 对 curation 无用，论文应更具体地发展 provenance tracking 的 use case。

**W5** [warning] **Cross-model chains 的评估设定不够严格**
- 具体位置：§4.1 (p5-6)
- 问题：Cross-model chains 设定中，每一步随机选择 generator，但评估使用 sample-level 5-fold CV。这意味着 generator-specific patterns 可以在训练中被学习并在测试中被利用。这解释了 0.809 vs LOGO 的 0.762 之间的差距。但更有意义的评估是在 cross-model chains 上使用 LOGO（hold out 某个 generator，该 generator 不出现在任何链的任何深度）。
- 建议：补充 cross-model chains + LOGO 的评估。

---

## Minor 问题

- §3.3 (p5): "Entropy" 在本文中指 token-level NLL（surprisal），脚注中有说明，但这一非标准用法可能造成混淆。建议在正文中一致使用 "surprisal" 或 "token-level NLL"。
- Figure 1 (p4): DDR panel（右侧）的 legend 较小，strip plot 中的颜色区分在黑白打印下可能不清晰。
- §4.2 (p6): 定义 "near-stationary" 为 |ρ| < 0.10 的阈值缺乏理论依据，略显随意。
- p12 Note: "appendix experiments use the original six-generator subset" 但主实验用 8 个 generator。部分 Appendix 用 6-gen LOGO，部分用 8-gen LOGO，交叉引用时容易混淆。应在 Appendix 开头统一说明。
- §4.1 (p5) 报告 "N = 37,058" 但 filtering criteria（移除 generation failures, exact duplicates, passages < 50 tokens）的具体数量仅在 Appendix A 的 Table 5 中。建议在正文中简要说明 filtering 的规模。

---

## Questions for Authors

1. OLMo-Instruct 之外，是否测试过其他 instruction-tuned model（如 Llama-3-chat, Mistral-Instruct）的完整链？如果多个 instruction-tuned model 均失效，这是系统性限制还是 OLMo-specific？
2. LOFO（Table 9）显示 entropy_max 贡献 -0.01pp，entropy_min 贡献 +0.01pp。实际上只有 5/7 个特征有意义贡献。是否考虑过更简洁的 feature set？
3. 在 cross-model chains 设定中，如果使用 LOGO（hold out 某个 generator 使其不出现在任何链的任何深度），F1 会如何变化？
4. 每篇文档的特征提取 wall-clock time 与 FastDetectGPT 等 neural baseline 的对比是多少？
5. 是否探索过同时使用多个参考模型的特征来改善 gen-1/gen-2+ 区分？

---

## Missing References

引用审计结果显示 58 条 bib 条目完整，无 orphan 或 missing 条目。48 条通过 OpenAlex 验证。以下几点值得注意：
- `detectgpt` (Mitchell et al., 2023) 和 `pythia` (Biderman et al., 2023) 在 OpenAlex 中未找到精确匹配，但为已知合法论文，bib 条目本身无问题。
- 建议补充：(a) 关于 training data contamination detection 的工作（beyond Min-K%）；(b) 关于 LLM output distribution 理论分析的工作，如 Braverman et al. (2020) 等信息论视角。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 (Acceptable) | 统计方法规范，LOGO 评估设计合理，但 gen-0 泄漏使 headline metric 不可靠；gen-1/gen-2+ 区分接近随机削弱核心 claim；base-model-only 限制与实际动机断裂 |
| **Excitement** | 2.5/5 (Borderline) | 问题定义有价值，DDR 分析有趣，但结果未能令人信服地证明 ordinal depth estimation 在实际场景中可行；instruction-tuned 失效是重大减分项 |
| **Reproducibility** | 4/5 | 超参完整（XGBoost n_estimators=200, max_depth=6, lr=0.1），特征计算过程清晰，承诺开源代码和数据。仅扣分：seed passage 的精确选择标准可以更明确 |
| **Confidence** | 4/5 | 仔细阅读全文含 12 个 Appendix，熟悉 AI text detection 和 NLP evaluation 方法论 |

## Overall Assessment

**Overall**: 3.0 — Findings

**一句话总结**：这是一个定义合理、统计工作扎实的分析性研究，DDR framework 提供了关于递归生成动力学的有价值洞察。但三个核心问题共同限制了其影响力：(1) gen-0 数据泄漏膨胀了 headline metric 且 abstract framing 过于乐观；(2) 仅限 base model 与论文声称的实际应用场景严重脱节（instruction-tuned F1 暴跌至 0.338）；(3) gen-1/gen-2+ 区分能力弱（48% error rate），使 "ordinal depth estimation" 的核心 claim 缺乏充分支撑。修复 abstract framing、增加 instruction-tuned 实验（即使结果不佳也需诚实报告）、并将 contribution 聚焦于分析性发现而非实用工具，可稳固达到 Findings 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-17T16:39:51.874802+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n## Must-Fix 问题\n\n**N1** [critical] Abstract framing 误导，headline metric 受 gen-0 数据泄漏膨���\n- Gen-0 是共享 Wikipedia 原文，LOGO 下 held-out generator �� gen-0 与训练集 gen-0 完全相同，构成泄漏。3-class LOGO F1=0.762 因近乎完美的 gen-0 分类而膨胀。Leak-free binary（gen-1 vs gen-2+）仅 0.694。Abstract 以 cross-model 0.809 开头，LOGO 0.762 次要，binary 0.694 完全未出现在 Abstract。\n\n**N2** [critical] 仅限 base model，实际适用性严重受限\n- 全部 8 个 generator 均为 base model。OLMo-Instruct LOGO F1=0.338。§1 以 web 文本污染为动机，但方法无法处理 instruction-tuned 场景。\n\n**N3** [critical] Gen-1/gen-2+ 区分能力弱，削弱 ordinal estimation 核心声明\n- 混淆矩阵 35.5% gen-2 / 37.8% gen-3 被错分为 gen-1。Binary depth-2 error rate 48%。方法主要成功在于识别 gen-0，接近传统 binary detection。\n\n## Should-Fix 问题\n\n**W1** 参考模型特征可能携带 generator-family 偏差（Pythia-410M ref + Pythia gen 的 same-family 效应未分析）\n**W2** Tail decay rank 范围 100-1000 缺乏理论支撑\n**W3** 温度敏感性：主实验 t=0.7 非典型，t=1.0 下降 6pp\n**W4** Downstream utility 为负面结果，削弱实际动机\n**W5** Cross-model chains 评估使用 sample-level CV 而非 LOGO，不够严格\n\n## Minor\n- \"Entropy\" 实为 token-level NLL，用词可能混淆\n- Figure 1 DDR panel legend 较小\n- |ρ|<0.10 \"near-stationary\" 阈值缺乏理论依据\n- 6-gen / 8-gen 附录交叉引用易混淆\n- Filtering 规模仅在 Appendix A 中\n\n## Overall: 3.0 (Findings)\n\n---\n\n请逐条回应每个问题。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n## Must-Fix 问题\n\n**N1** [critical] Abstract framing 误导，headline metric 受 gen-0 数据泄漏膨���\n- Gen-0 是共享 Wikipedia 原文，LOGO 下 held-out generator �� gen-0 与训练集 gen-0 完全相同，构成泄漏。3-class LOGO F1=0.762 因近乎完美的 gen-0 分类而膨胀。Leak-free binary（gen-1 vs gen-2+）仅 0.694。Abstract 以 cross-model 0.809 开头，LOGO 0.762 次要，binary 0.694 完全未出现在 Abstract。\n\n**N2** [critical] 仅限 base model，实际适用性严重受限\n- 全部 8 个 generator 均为 base model。OLMo-Instruct LOGO F1=0.338。§1 以 web 文本污染为动机，但方法无法处理 instruction-tuned 场景。\n\n**N3** [critical] Gen-1/gen-2+ 区分能力弱，削弱 ordinal estimation 核心声明\n- 混淆矩阵 35.5% gen-2 / 37.8% gen-3 被错分为 gen-1。Binary depth-2 error rate 48%。方法主要成功在于识别 gen-0，接近传统 binary detection。\n\n## Should-Fix 问题\n\n**W1** 参考模型特征可能携带 generator-family 偏差（Pythia-410M ref + Pythia gen 的 same-family 效应未分析）\n**W2** Tail decay rank 范围 100-1000 缺乏理论支撑\n**W3** 温度敏感性：主实验 t=0.7 非典型，t=1.0 下降 6pp\n**W4** Downstream utility 为负面结果，削弱实际动机\n**W5** Cross-model chains 评估使用 sample-level CV 而非 LOGO，不够严格\n\n## Minor\n- \"Entropy\" 实为 token-level NLL，用词可能混淆\n- Figure 1 DDR panel legend 较小\n- |ρ|<0.10 \"near-stationary\" 阈值缺乏理论依据\n- 6-gen / 8-gen 附录交叉引用易混淆\n- Filtering 规模仅在 Appendix A 中\n\n## Overall: 3.0 (Findings)\n\n---\n\n请逐条回应每个问题。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-17T16:40:10.133910+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18259
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-17T16:40:10.486737+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## Must-Fix 问题\n\n**N1** [critical] 标题中 \"Ordinal\" framing 与实际方法存在根本性矛盾\n- CORAL/Frank-Hall ordinal regression 无增益（Appendix H）。5-class F1 仅 0.50。实际是 3-class multiclass classification，ordinal 性质完全未被利用。标题创造了\"序数回归方法论贡献\"预期但实际未兑现。\n\n**N2** [critical] Base model only 限制严重削弱实际影响力\n- Instruction-tuned F1=0.338，现实 LLM 文本几乎都来自 instruct/RLHF 模型。Introduction 动机（web contamination）与实际贡献（base model 分析）脱节。\n\n**N3** [critical] Gen-0 seed sharing 导致 3-class F1 可能系统性高估\n- 所有 generators 共享同一批 gen-0 seeds。LOGO 中 held-out generator 的 gen-0 在训练集已出现。Abstract 仍以 potentially-inflated 的 3-class F1 为主打数字。\n\n## Should-Fix 问题\n\n**W1** DDR 的\"机制解释\"超越了实证证据（仅基于 7 个 summary statistics 推断 NLL distribution 性质）\n**W2** Multi-detector ensemble（Table 4: 3-cl 0.795, binary 0.708）优于 7-feature（0.774, 0.705），削弱性能 claim\n**W3** 6-gen/5-gen/8-gen 子集混用，数字难以横向比较（Table 1 LOGO 0.762 vs Table 4 7-feature 0.774 差异未解释）\n**W4** Contribution 3（downstream utility）本质是 null result，framing 过于乐观\n**W5** Temperature t=1.0 时方法失效讨论不足\n\n## Minor\n- Table 1 vs Table 4 F1 不一致\n- \"entropy\" 实为 NLL 用词混淆\n- Appendix confusion matrix 用 6-gen 而非 8-gen\n- Cross-domain t=1.0 vs 主实验 t=0.7 不一致\n- Discussion 过度使用 \\paragraph{} 分段（AI 写作痕迹）\n- 引用验证通过，建议补充 M4/SemEval 2024 参赛方法和 data provenance 文献\n\n## Overall: 3.0 (Findings)\n\n---\n\n请逐条回应每个问题。",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## Must-Fix 问题\n\n**N1** [critical] 标题中 \"Ordinal\" framing 与实际方法存在根本性矛盾\n- CORAL/Frank-Hall ordinal regression 无增益（Appendix H）。5-class F1 仅 0.50。实际是 3-class multiclass classification，ordinal 性质完全未被利用。标题创造了\"序数回归方法论贡献\"预期但实际未兑现。\n\n**N2** [critical] Base model only 限制严重削弱实际影响力\n- Instruction-tuned F1=0.338，现实 LLM 文本几乎都来自 instruct/RLHF 模型。Introduction 动机（web contamination）与实际贡献（base model 分析）脱节。\n\n**N3** [critical] Gen-0 seed sharing 导致 3-class F1 可能系统性高估\n- 所有 generators 共享同一批 gen-0 seeds。LOGO 中 held-out generator 的 gen-0 在训练集已出现。Abstract 仍以 potentially-inflated 的 3-class F1 为主打数字。\n\n## Should-Fix 问题\n\n**W1** DDR 的\"机制解释\"超越了实证证据（仅基于 7 个 summary statistics 推断 NLL distribution 性质）\n**W2** Multi-detector ensemble（Table 4: 3-cl 0.795, binary 0.708）优于 7-feature（0.774, 0.705），削弱性能 claim\n**W3** 6-gen/5-gen/8-gen 子集混用，数字难以横向比较（Table 1 LOGO 0.762 vs Table 4 7-feature 0.774 差异未解释）\n**W4** Contribution 3（downstream utility）本质是 null result，framing 过于乐观\n**W5** Temperature t=1.0 时方法失效讨论不足\n\n## Minor\n- Table 1 vs Table 4 F1 不一致\n- \"entropy\" 实为 NLL 用词混淆\n- Appendix confusion matrix 用 6-gen 而非 8-gen\n- Cross-domain t=1.0 vs 主实验 t=0.7 不一致\n- Discussion 过度使用 \\paragraph{} 分段（AI 写作痕迹）\n- 引用验证通过，建议补充 M4/SemEval 2024 参赛方法和 data provenance 文献\n\n## Overall: 3.0 (Findings)\n\n---\n\n请逐条回应每个问题。",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-17T16:40:11.852750+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1366
}
```

</details>

---


### Assistant

_source line 480 · 2026-05-17T16:40:14.929949+00:00_

交叉分享已分发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 481 · 2026-05-17T16:40:17.493609+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：作为 Reviewer 1（方法严谨性/实验设计/统计声明），我给出 **Overall 3.0 (Findings)** 评分。三个 Must-Fix 问题：

1. **Gen-0 数据泄漏 + Abstract framing 误导**：共享 Wikipedia seeds 在 LOGO 下构成 gen-0 泄漏，leak-free binary F1 仅 0.694，但 Abstract 以更乐观的 0.809 领衔
2. **仅限 base model**：instruction-tuned 模型 F1 暴跌至 0.338，与论文声称的实际应用场景严重脱节
3. **Gen-1/gen-2+ 区分近乎随机**（48% error rate），削弱 ordinal depth estimation 的核心声明

优点包括问题定义合理、评估协议严谨（LOGO + 大量 Appendix 消融）、统计方法规范、DDR 分析提供可解释洞察。引用完整（58 条，无遗漏）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 482 · 2026-05-17T16:40:22.444885+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 483 · 2026-05-17T16:42:02.814486+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 回应

**[AGREE] R1-N1: Gen-0 数据泄漏导致 3-class F1 膨胀**

同意。我在自己的审稿中独立提出了相同问题（我的 N3）。Appendix G confusion matrix 显示 gen-0 recall=99.4% vs gen-1=75.0%/gen-2+=73.7%，gen-0 的近完美分类可能部分来自 memorization。Abstract 以 3-class F1 为主打而非 leak-free binary F1=0.694 是 misleading。

**[AGREE] R1-N2: Base model only 限制**

完全同意（我的 N2）。补充：Limitations section 进一步报告 Qwen3-0.6B chat 的 length-matched 分析得到 |ρ|<0.02 和 binary F1≈0.5，说明 instruct model 下连基本 depth signal 都不存在。Introduction 的 web contamination 动机与 base-model-only scope 严重 mismatch。

**[REBUT] R1-N3: Gen-1/gen-2+ 区分能力弱**

R1 的事实准确（5-class gen-2/gen-3 错分率 36.5%/37.8%，binary depth-2 error rate 48%），但不应作为 critical issue：

(1) 论文完全透明——Section 4.1 报告 binary F1=0.694，Discussion 详细分析错误模式（86% false negatives，depth-2 error 48% vs depth-4 20%），与 DDR 预测一致。

(2) R1 说"方法主要成功在于识别 gen-0，接近传统 binary detection"不准确——binary metric 完全排除 gen-0，F1=0.705（Table 4）优于所有单一 baseline（0.539-0.675）。这是纯 depth discrimination。

(3) 两篇 concurrent work 独立收敛于"约三个可区分类"的相同结论 (Section 2.2, lines 28-31)，说明这是 recursive generation 的固有特性。Appendix C 的多 classifier 对比确认 bottleneck 在 feature separability。

建议降级为 Should-Fix。

---

## Should-Fix 回应

**[AGREE] R1-W1**: Reference model family 偏差。Table 1 中 Pythia generators 获最高 F1 可能与 same-family reference model (Pythia-410M) 有关。Table 2 的 cross-reference 实验无法隔离此效应。

**[AGREE] R1-W2**: Tail decay rank 100-1000 缺乏 justification。不过 LOFO (Appendix F) 显示 tail_decay ΔF1 仅 -0.33pp，影响有限。

**[AGREE] R1-W3**: 温度敏感性。补充：cross-domain 实验 (Appendix I) t=1.0 反而优于 t=0.7，与 Wikipedia 主实验方向相反，使"standard decoding regime"定义更模糊。

**[AGREE] R1-W4**: Downstream null result。n=3 seeds 不足以支撑任何强结论。

**[REBUT] R1-W5**: Cross-model chains 用 sample-level CV 有 structural reason——每条链 randomly 选择 generator，对此做 LOGO 在概念上 ill-defined（held-out generator 的文本在其他链中作为 input 出现）。Cross-model 结果的主要价值是证明 depth signal 在 generator heterogeneity 下 survives，泛化估计以 Table 1 的 8-gen LOGO 为准。

---

## Minor 回应

全部 [AGREE]——entropy 术语混淆、Figure 1 legend 小、|ρ|<0.10 阈值无理论依据、6-gen/8-gen 混淆、filtering 信息分散。均为有效的 minor issues。

---

## 与我审稿的对比

R1 与我在三个核心问题上高度一致（gen-0 泄漏、base-model 限制、downstream null result），为独立发现的共识。

我额外提出了 R1 未覆盖的两个问题：
- **标题 "Ordinal" framing 矛盾**（我的 N1）：CORAL/Frank-Hall ordinal methods 无改善，标题 overclaim
- **DDR 机制解释超越证据**（我的 W1）："location shift preserving shape" 仅基于 7 个 summary statistics 推断

主要分歧在 R1-N3（gen-1/gen-2+ 区分能力）：R1 视为 critical，我认为应为 Should-Fix——binary F1=0.694 是纯 depth discrimination 且 3-class ceiling 是有理论支撑的发现。

**Overall 评分一致：3.0 (Findings)**。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 484 · 2026-05-17T16:42:07.814363+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 485 · 2026-05-17T16:42:10.372717+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

与 Reviewer 1 的主要共识：gen-0 数据泄漏(N1)、base-model-only 限制(N2)、downstream null result(W4)。唯一分歧在 R1-N3（gen-1/gen-2+ 区分能力）——我认为应降级为 Should-Fix，因为 binary F1=0.694 是排除 gen-0 后的纯 depth discrimination，且 3-class ceiling 是 recursive generation 的固有特性而非方法缺陷。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 486 · 2026-05-17T16:42:15.580264+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 49

## Round 49

6 recorded events


### User

_source line 487 · 2026-05-17T16:43:57.709985+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE] R2-N1: "Ordinal" framing 与实际方法的矛盾

同意这是一个显著问题，但需补充两点细节：

1. **证据核实**：Reviewer 2 标注 "Appendix H" 有误——CORAL/Frank-Hall 对比实验在 **Appendix D** (p14)，Appendix H 是 Classifier Sensitivity。不过核心论点成立：Appendix D 明确报告 "ordinal-specific methods (CORAL, ordinal regression, Frank-Hall) reducers similarly fail to improve over multiclass XGBoost (§4), confirming that the bottleneck is feature separability across all granularities, not the modeling of label ordinality."（p14 原文）

2. **程度判断**：5-class LOGO Macro F1 ≈ 0.50（Table 6, p14），其中 gen-0 F1=0.921 但 gen-2/gen-3 F1 仅 0.268/0.259（Table 7, p14）。这说明序数性质不仅在方法论上未被利用，在特征层面也根本不支持 fine-grained ordinal estimation。标题中的 "Ordinal" 确实设定了 ordinal regression 方法论贡献的期待，但实际只是 3-class（近似 2-class）multiclass classification。

**与我的 N3 问题互补**：我指出的 gen-1/gen-2+ 区分弱（48% error rate at depth-2 boundary）正是此问题的另一面——如果连 3-class 的 gen-1/gen-2+ 边界都近乎随机，那么 "ordinal depth estimation" 的 framing 更成问题。

**建议**：标题修改为 "Depth Fingerprinting: Generation Depth Classification in Non-Paraphrastic LLM Text Chains" 或类似措辞，去掉 "Ordinal"，除非能证明序数结构对分类有实质帮助。

---

### [AGREE] R2-N2: Base model only 限制

完全同意。与我的 N2 判断一致。补充一个关键数据点：

论文在 Discussion §5 (p8) 明确说 "OLMo-2-1B-Instruct drops to LOGO F1 = 0.338"，而在 p9 进一步说 "instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base)"。但这只是 **单一 instruction-tuned 模型** 的数据点。没有 Llama-chat、Mistral-Instruct、Qwen-chat 的实验，无法判断这是 OLMo-specific 还是 systematic failure。

**进一步证据**：p9 承认 "extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven shaping)"，说明作者知道这不是简单的 domain shift 而是 fundamental limitation。这加剧了 Introduction 动机（web contamination, data quality）与实际贡献之间的 gap。

---

### [AGREE] R2-N3: Gen-0 seed sharing 导致 F1 高估

完全同意。与我的 N1 判断一致。

补充定量证据强化此论点：
- 3-class LOGO F1 = 0.762（Table 1, p6，含泄漏的 gen-0）
- Leak-free binary F1（gen-1 vs gen-2+）= 0.694（Table 1 note, p6）
- 差值 = 6.8pp，且 Appendix G confusion matrix (p15) 显示 gen-0 分类 F1 = 0.921（几乎完美），而 gen-1 F1 = 0.634，gen-2+ 更低

这意味着 3-class F1 中约 1/3 的"性能"来自 trivially 高的 gen-0 分类。Abstract 以 cross-model chains 的 0.809 领衔则更加乐观——该设定甚至未使用 LOGO。

**两个 Reviewer 的共识**：N2 和 N3 是两个独立的、各自足以降低一档评分的 critical issues，它们联合效应更强——method 在 base model + 无泄漏条件下的真实性能是 binary F1 = 0.694，与 abstract 的 0.809 相差 11.5pp。

---

## Should-Fix 问题

### [AGREE] R2-W1: DDR 机制解释超越实证

同意需要更审慎。论文在 §4.2 (p6) 声称 "a location shift in the NLL distribution while preserving its shape" 和 "the softmax architecture and fixed sampling parameters constrain distributional shape"。

但支撑这一机制解释的证据仅是：
- 4 个 drifting features 的 Spearman ρ（entropy mean ρ = −0.63, TTR ρ = −0.61 等）
- KS 统计量的量级对比（drifting ~0.5 vs stationary ~0.05）

这些是 **聚合统计量的相关性**，不是对完整 NLL 分布的直接分析。虽然方向合理，但 "location shift while preserving shape" 是一个关于完整分布的断言，仅靠 mean/std/max/min 四个 moment 无法严格证实。

**不过有一个缓和因素**：Appendix N (Feature Distribution Analysis, p19-20) 的 UMAP embedding 和 DDR trend lines 提供了一些额外的可视化支撑。但这仍是描述性的，不是机制性的。

**建议**：将 "consistent with" 改为断言性更弱的表述，或补充 token-level NLL 完整分布的直方图对比（gen-0 vs gen-1 vs gen-2+）来直接验证 location-shift-without-shape-change 的假说。

---

### [AGREE] R2-W2: Multi-detector ensemble 优于 7-feature，削弱性能 claim

同意，但需精确区分 3-class 和 binary：

Table 4 (p8, 6-gen pooled LOGO) 数据：
- 4-det + surface: **3-cl F1 = 0.795**, Bin F1 = 0.708
- 7-feature (ours): **3-cl F1 = 0.774**, Bin F1 = 0.705

3-class 差距 = 2.1pp（有实质差异），binary 差距 = 0.3pp（可忽略）。

论文在 p7 的表述是 "competitive performance at substantially lower computational cost than multi-detector alternatives"——这在 binary 上成立，但在 3-class 上 multi-detector 明确更好。Abstract 的 "competitive" 修饰语模糊了这一区分。

**进一步问题**：如果 multi-detector ensemble 在 3-class 上更强，而 3-class 正是论文标题所宣称的核心任务，那么方法的核心竞争力仅在于 cost-efficiency，而非 detection quality。这应更明确地表述。

---

### [AGREE] R2-W3: 6-gen/5-gen/8-gen 子集混用

完全同意。这是影响论文可读性的显著问题。

具体不一致列表：
| 表格/评估 | Generator 子集 | F1 |
|-----------|---------------|-----|
| Table 1 (主实验) | 8-gen LOGO | 0.762 |
| Table 2 (reference model) | 5-gen LOGO | — |
| Table 3 (ablation) | 6-gen, 10-fold CV | 0.773 |
| Table 4 (baselines) | 6-gen pooled LOGO | 0.774 |
| Appendix D (5-class) | 6-gen LOGO | ~0.50 |
| Appendix G (confusion) | 6-gen LOGO | — |

8-gen LOGO（0.762）比 6-gen LOGO（0.774）**低 1.2pp**，说明后加入的 Llama 和 Mistral 更难分类。但论文从未解释这一差异。读者无法在 Table 1 和 Table 4 之间做 apple-to-apple 比较，这是严重的可读性和可信度问题。

**建议**：所有主实验统一使用 8-gen LOGO。如果计算限制导致部分 Appendix 实验仍用 6-gen，应在 Appendix 开头用一段话说明并讨论 subset 选择的影响。

---

### [AGREE] R2-W4: Downstream utility 本质是 null result

同意。与我的 W4 判断一致。

Appendix L (p19) 的 TOST 结果说明 depth-aware curation 与 random subsampling 统计等价（±2% margin, p < 0.001）。论文将此 framed 为 Contribution 3 "depth composition per se does not determine training utility"，但这实质上是说**深度信息对 data curation 没用**。如果论文的一个核心动机是 data quality/provenance，那么发现深度对质量无影响实际上是 **against** 这个动机的。

论文应在 Discussion 中正面承认：depth fingerprinting 的价值在于 provenance tracking（知道文本经过了多少轮生成），而非 quality-based curation（用深度来筛选更好的训练数据）。

---

### [AGREE] R2-W5: Temperature t=1.0 讨论不足

同意，但需补充一个缓和因素。

论文主实验用 t=0.7，Appendix H 报告 t=1.0 时 ~6pp degradation。Reviewer 2 说 "方法失效"，我认为措辞偏强——6pp degradation 是 significant 但不是 collapse。

**但有一个加重因素**：Appendix O (p20) 的 cross-temperature transfer 分析显示，在 t=0.7 训练 / t=1.0 测试的 mismatched 条件下，Qwen3-1.7B 的 F1 从 matched 的 0.789 降至 0.418——这才是真正的 failure。其他 generator 的 mismatch degradation 也普遍存在。

论文正文（§5, p7-8）仅简要提到温度敏感性但未充分讨论其 implication。如果实际部署中无法预知 generator 的温度设定，方法的泛化能力会进一步受限。

---

## Minor 问题

### [AGREE] Table 1 vs Table 4 F1 不一致
同意。直接关联 W3，根本原因是 8-gen vs 6-gen 子集差异。

### [AGREE] "entropy" 实为 NLL 用词混淆
同意。我在自己的审稿中也独立标记了此问题（§3.3 footnote）。

### [AGREE] Appendix confusion matrix 用 6-gen 而非 8-gen
同意。Appendix G 应补充 8-gen 版本以与 Table 1 主实验对齐。

### [AGREE] Cross-domain t=1.0 vs 主实验 t=0.7 不一致
同意。Appendix J 的 cross-domain 实验使用 t=1.0（p18），而主实验用 t=0.7，这使得 cross-domain 结果不可直接与主实验比较。

### [AGREE] Discussion 过度使用 \paragraph{} 分段
同意。Discussion (§5, p7-8) 包含至少 7 个 \paragraph{} 标题（Prompt-type dependence, Practical applicability, The gen-1/gen-2+ boundary, Relation to model collapse, Model collapse, Granularity and robustness, Instruction tuning）。这种过度分段是典型的 AI 写作风格标志——真实的 Discussion 应以完整段落的叙事逻辑串联，而非碎片化的标题列表。

### [REBUT] 引用：建议补充 M4/SemEval 2024 参赛方法
部分反驳。**SemEval-2024 Task 8** 已被引用（`semeval2024_task8`, Related Work p2）。具体参赛方法（如 top-performing systems）的补充是 nice-to-have 但非必需——论文的 Related Work 已覆盖主要 detection 方法学分支。

Data provenance 文献的补充建议则合理——论文在 §2.4 讨论 Data Quality and Provenance 但引用主要集中在 data curation (DSIR, QuRating, CCNet) 和 watermarking，缺少 digital provenance tracking 领域的文献。

---

## 总体评估

两位 Reviewer 在三个核心问题上达成完全共识：
1. **Gen-0 数据泄漏 + Abstract framing** (R1-N1 = R2-N3)
2. **Base model only 限制** (R1-N2 = R2-N2)
3. **Ordinal estimation 能力弱 / framing 过度** (R1-N3 ≈ R2-N1)

这三个问题相互独立且各自成立，联合效应显著降低论文的 impact。

我维持 **Overall 3.0 (Findings)** 的评分。Reviewer 2 的审稿意见整体高质量，所有 Must-Fix 和 Should-Fix 均有实据支撑。唯一的 minor factual error 是 Appendix 编号引用（标为 Appendix H 实为 Appendix D）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-17T16:45:58.860891+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"TOST added. Contribution 3 restored with perplexity scope.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Abstract reports both binary and 3-class.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-N1.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers independently flagged. Abstract still leads with 3-class 0.809/0.762; leak-free binary 0.694 absent from Abstract. Gen-0 recall=99.4% vs gen-1=75.0%.\"}\n  action_items:\n    - {round: 10, action: \"Use leak-free binary F1 as headline\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Abstract must lead with leak-free binary F1=0.694 as primary metric; 3-class as secondary with explicit caveat\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"DDR 'location shift preserving shape' claim based only on 7 summary statistics, not direct NLL distribution analysis. Both agree evidence is suggestive but not mechanistic.\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Structural.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"DDR vs model collapse still insufficient.\"}\n  action_items:\n    - {round: 10, action: \"Expand §5 model collapse to full paragraph\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"discussion.tex: full paragraph on inference-chain vs training-loop, reversibility, shape stationarity evidence, pre-collapse regime framing.\"\n  resolution_round: 10\n\n- id: \"R7-W5\"\n  summary: \"Instruct framing\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Abstract/Intro still imply general applicability.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers flag as critical. Introduction web contamination motivation vs base-model-only scope is fundamental mismatch. OLMo-Instruct F1=0.338, Qwen3-0.6B-chat binary F1≈0.50. Only 1 instruct model tested.\"}\n  action_items:\n    - {round: 10, action: \"Explicit base-model scope in Intro; instruct in Discussion\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Reframe Introduction motivation from 'web contamination tool' to 'understanding recursive generation dynamics'; explicit base-model scope in Abstract\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Error rate 48% still buried in Appendix.\"}\n  action_items:\n    - {round: 10, action: \"Discuss prominently in §5\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Discussion has dedicated paragraph with 48% error rate, 86% false negative rate, mechanistic explanation, scale effect.\"\n  resolution_round: 10\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M3\"\n  summary: \"NLL + topic drift spec\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Fixed. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-M4\"\n  summary: \"Missing references\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"All added. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R8-N1\"\n  summary: \"entropy_std grouping + Figure 1 caption\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Recurred. Binary F1=0.694 still not in Abstract despite R10 fix claim.\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-RV2\"\n  summary: \"LOFO delta error\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected to -0.8pp. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n    - {round: 9, action: \"Abstract: 'downstream harm' → 'downstream perplexity degradation'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Abstract L8 qualified. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises vs 3-class reality\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"5-class F1=0.50, gen-1/gen-2+ error rate 48%.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers flag independently. CORAL/Frank-Hall ordinal methods provide zero improvement (Appendix D). Title 'Ordinal...Estimation' sets expectation of ordinal regression contribution but delivers 3-class multiclass. 5-class gen-2/gen-3 F1=0.268/0.259.\"}\n  action_items:\n    - {round: 10, action: \"Revise abstract to 'coarse ordinal'; state depth≥2 collapse reason in main text\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Remove 'Ordinal' from title or provide evidence that ordinal structure helps; current title: 'Generation Depth Classification' more accurate\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation experiment contradicts core motivation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Random subsampling = depth-stratified at equal N. Only 3 seeds.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers agree null result undermines data quality motivation. n=3 seeds insufficient. Paper frames as 'decoupling' but reads as 'no utility'.\"}\n  action_items:\n    - {round: 10, action: \"Demote curation from core motivation; adjust framing\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Acknowledge null result honestly in Discussion; reduce prominence in Abstract/Intro\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Sensitivity real, needs prominent discussion and explicit working range.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Cross-temperature transfer shows Qwen3-1.7B drops from 0.789 to 0.418 under mismatch. t=1.0 entropy_mean ρ collapses. Cross-domain at t=1.0 contradicts Wikipedia at t=0.7.\"}\n  action_items:\n    - {round: 10, action: \"Explicit working range [0.5,0.9]; ρ collapse mechanism\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Discuss cross-temperature transfer failure prominently in main text; acknowledge unknown-temperature deployment limitation\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"Location shift claim lacks formal statistical testing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"No KS/Levene test.\"}\n  action_items:\n    - {round: 10, action: \"Add KS + Levene tests\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"results.tex: KS tests with exact values (gen-1 vs gen-2+), Levene tests, CV shift comparison. All values verified against distributional_tests.json.\"\n  resolution_round: 10\n\n- id: \"R10-W3\"\n  summary: \"TOST ±2% margin unjustified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"No theoretical basis for 2%. Should report multiple margins.\"}\n  action_items:\n    - {round: 10, action: \"Multi-margin TOST + Cohen's d + Lakens citation\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"appendix_downstream.tex: Margin Sensitivity Analysis with ±1%/2%/3%/5% table, Cohen's d with n=3 caveat, Lakens (2017) citation.\"\n  resolution_round: 10\n\n- id: \"R10-W4\"\n  summary: \"Cross-model F1=0.809 lacks formal table\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"No proper table with per-class F1 and CIs.\"}\n  action_items:\n    - {round: 10, action: \"Add formal cross-model per-class table\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"results.tex Table 1: per-class P/R/F1 + 95% CI for gen-0/gen-1/gen-2+ (class-balanced 5-fold CV, N=2964). Caption notes 0.809 under natural distribution.\"\n  resolution_round: 10\n\n- id: \"R10-W5\"\n  summary: \"Data diversity insufficient (Wikipedia-only seeds)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Cross-domain only 3 generators, 200 seeds.\"}\n  action_items:\n    - {round: 10, action: \"Discuss Wikipedia selection bias prominently\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"results.tex: cross-domain numbers in main text (Wiki 0.789, Academic 0.628). Limitations L23-26: domain×temperature interaction, cross-domain variation discussed prominently.\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"Geng et al. (2026) differentiation insufficient\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Three-class boundary coincidence needs mechanistic comparison.\"}\n  action_items:\n    - {round: 10, action: \"Add dedicated comparison paragraph\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"related_work.tex: ~85-word mechanistic comparison — Markovian attractor dynamics vs empirical feature convergence, KS margin compression evidence, complementary frameworks (why vs what).\"\n  resolution_round: 10\n\n- id: \"R11-N1\"\n  summary: \"Title 'Ordinal' sets ordinal-regression expectation but method is standard multiclass\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"CORAL/Frank-Hall zero improvement (Appendix D). 5-class gen-2/gen-3 F1=0.268/0.259. Ordinal structure not exploited. Title misleads.\"}\n  action_items:\n    - {round: 11, action: \"Remove 'Ordinal' from title or justify with evidence of ordinal benefit\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Reference model family bias (same-family Pythia ref + Pythia gen)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Pythia generators get highest F1; may be due to Pythia-410M reference model. Table 2 cross-ref experiment cannot isolate this.\"}\n  action_items:\n    - {round: 11, action: \"Report same-family vs cross-family per-generator F1 breakdown\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Multi-detector ensemble outperforms 7-feature on 3-class (core task)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Table 4: 4-det+surface 3-cl F1=0.795 vs 7-feature 0.774 (2.1pp gap). Introduction claim 'competitive' is misleading for 3-class. Core competitiveness is cost-efficiency only.\"}\n  action_items:\n    - {round: 11, action: \"Clarify in Introduction that method trades 2pp 3-class F1 for 60% cost reduction; not claim parity\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"6-gen/5-gen/8-gen subset mixing impairs comparability\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Table 1 (8-gen 0.762) vs Table 4 (6-gen 0.774) not comparable. Llama/Mistral harder but difference unexplained. No master table of which experiment uses which subset.\"}\n  action_items:\n    - {round: 11, action: \"Add generator-subset summary table; explain 8-gen vs 6-gen F1 difference; unify main experiments to 8-gen where possible\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M1\"\n  summary: \"Discussion over-fragmented with \\\\paragraph{} (AI writing signature)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"7+ \\\\paragraph{} headers in Discussion. Should be consolidated into 3-4 natural paragraphs.\"}\n  action_items:\n    - {round: 11, action: \"Merge Discussion into coherent narrative paragraphs\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"'Entropy' misnomer (actually token-level NLL/surprisal)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Only footnote 1 clarifies. Both reviewers flag confusion risk.\"}\n  action_items:\n    - {round: 11, action: \"Use 'surprisal' or 'token-level NLL' consistently, or add prominent clarification beyond footnote\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"Tail decay rank range 100-1000 unjustified\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"No theoretical motivation. LOFO shows minimal impact (-0.33pp) so low priority.\"}\n  action_items:\n    - {round: 11, action: \"Add brief justification or range ablation\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === 历史 (R1-R6) ===\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Direction C. Persists as R7-W4.\"\n  resolution_round: 5\n\n- id: \"R5-TABLE1\"\n  summary: \"Table 1 only 6 generators\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"All 8.\"\n  resolution_round: 6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"TOST added. Contribution 3 restored with perplexity scope.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Abstract reports both binary and 3-class.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-N1.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers independently flagged. Abstract still leads with 3-class 0.809/0.762; leak-free binary 0.694 absent from Abstract. Gen-0 recall=99.4% vs gen-1=75.0%.\"}\n  action_items:\n    - {round: 10, action: \"Use leak-free binary F1 as headline\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Abstract must lead with leak-free binary F1=0.694 as primary metric; 3-class as secondary with explicit caveat\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"DDR 'location shift preserving shape' claim based only on 7 summary statistics, not direct NLL distribution analysis. Both agree evidence is suggestive but not mechanistic.\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Structural.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"DDR vs model collapse still insufficient.\"}\n  action_items:\n    - {round: 10, action: \"Expand §5 model collapse to full paragraph\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"discussion.tex: full paragraph on inference-chain vs training-loop, reversibility, shape stationarity evidence, pre-collapse regime framing.\"\n  resolution_round: 10\n\n- id: \"R7-W5\"\n  summary: \"Instruct framing\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Abstract/Intro still imply general applicability.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers flag as critical. Introduction web contamination motivation vs base-model-only scope is fundamental mismatch. OLMo-Instruct F1=0.338, Qwen3-0.6B-chat binary F1≈0.50. Only 1 instruct model tested.\"}\n  action_items:\n    - {round: 10, action: \"Explicit base-model scope in Intro; instruct in Discussion\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Reframe Introduction motivation from 'web contamination tool' to 'understanding recursive generation dynamics'; explicit base-model scope in Abstract\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Error rate 48% still buried in Appendix.\"}\n  action_items:\n    - {round: 10, action: \"Discuss prominently in §5\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Discussion has dedicated paragraph with 48% error rate, 86% false negative rate, mechanistic explanation, scale effect.\"\n  resolution_round: 10\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M3\"\n  summary: \"NLL + topic drift spec\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Fixed. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-M4\"\n  summary: \"Missing references\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"All added. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R8-N1\"\n  summary: \"entropy_std grouping + Figure 1 caption\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Recurred. Binary F1=0.694 still not in Abstract despite R10 fix claim.\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-RV2\"\n  summary: \"LOFO delta error\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected to -0.8pp. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  action_items:\n    - {round: 9, action: \"Abstract: 'downstream harm' → 'downstream perplexity degradation'\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"Abstract L8 qualified. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises vs 3-class reality\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"5-class F1=0.50, gen-1/gen-2+ error rate 48%.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers flag independently. CORAL/Frank-Hall ordinal methods provide zero improvement (Appendix D). Title 'Ordinal...Estimation' sets expectation of ordinal regression contribution but delivers 3-class multiclass. 5-class gen-2/gen-3 F1=0.268/0.259.\"}\n  action_items:\n    - {round: 10, action: \"Revise abstract to 'coarse ordinal'; state depth≥2 collapse reason in main text\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Remove 'Ordinal' from title or provide evidence that ordinal structure helps; current title: 'Generation Depth Classification' more accurate\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation experiment contradicts core motivation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Random subsampling = depth-stratified at equal N. Only 3 seeds.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers agree null result undermines data quality motivation. n=3 seeds insufficient. Paper frames as 'decoupling' but reads as 'no utility'.\"}\n  action_items:\n    - {round: 10, action: \"Demote curation from core motivation; adjust framing\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Acknowledge null result honestly in Discussion; reduce prominence in Abstract/Intro\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Sensitivity real, needs prominent discussion and explicit working range.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Cross-temperature transfer shows Qwen3-1.7B drops from 0.789 to 0.418 under mismatch. t=1.0 entropy_mean ρ collapses. Cross-domain at t=1.0 contradicts Wikipedia at t=0.7.\"}\n  action_items:\n    - {round: 10, action: \"Explicit working range [0.5,0.9]; ρ collapse mechanism\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Discuss cross-temperature transfer failure prominently in main text; acknowledge unknown-temperature deployment limitation\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"Location shift claim lacks formal statistical testing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"No KS/Levene test.\"}\n  action_items:\n    - {round: 10, action: \"Add KS + Levene tests\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"results.tex: KS tests with exact values (gen-1 vs gen-2+), Levene tests, CV shift comparison. All values verified against distributional_tests.json.\"\n  resolution_round: 10\n\n- id: \"R10-W3\"\n  summary: \"TOST ±2% margin unjustified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"No theoretical basis for 2%. Should report multiple margins.\"}\n  action_items:\n    - {round: 10, action: \"Multi-margin TOST + Cohen's d + Lakens citation\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"appendix_downstream.tex: Margin Sensitivity Analysis with ±1%/2%/3%/5% table, Cohen's d with n=3 caveat, Lakens (2017) citation.\"\n  resolution_round: 10\n\n- id: \"R10-W4\"\n  summary: \"Cross-model F1=0.809 lacks formal table\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"No proper table with per-class F1 and CIs.\"}\n  action_items:\n    - {round: 10, action: \"Add formal cross-model per-class table\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"results.tex Table 1: per-class P/R/F1 + 95% CI for gen-0/gen-1/gen-2+ (class-balanced 5-fold CV, N=2964). Caption notes 0.809 under natural distribution.\"\n  resolution_round: 10\n\n- id: \"R10-W5\"\n  summary: \"Data diversity insufficient (Wikipedia-only seeds)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Cross-domain only 3 generators, 200 seeds.\"}\n  action_items:\n    - {round: 10, action: \"Discuss Wikipedia selection bias prominently\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"results.tex: cross-domain numbers in main text (Wiki 0.789, Academic 0.628). Limitations L23-26: domain×temperature interaction, cross-domain variation discussed prominently.\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"Geng et al. (2026) differentiation insufficient\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Three-class boundary coincidence needs mechanistic comparison.\"}\n  action_items:\n    - {round: 10, action: \"Add dedicated comparison paragraph\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"related_work.tex: ~85-word mechanistic comparison — Markovian attractor dynamics vs empirical feature convergence, KS margin compression evidence, complementary frameworks (why vs what).\"\n  resolution_round: 10\n\n- id: \"R11-N1\"\n  summary: \"Title 'Ordinal' sets ordinal-regression expectation but method is standard multiclass\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"CORAL/Frank-Hall zero improvement (Appendix D). 5-class gen-2/gen-3 F1=0.268/0.259. Ordinal structure not exploited. Title misleads.\"}\n  action_items:\n    - {round: 11, action: \"Remove 'Ordinal' from title or justify with evidence of ordinal benefit\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Reference model family bias (same-family Pythia ref + Pythia gen)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Pythia generators get highest F1; may be due to Pythia-410M reference model. Table 2 cross-ref experiment cannot isolate this.\"}\n  action_items:\n    - {round: 11, action: \"Report same-family vs cross-family per-generator F1 breakdown\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Multi-detector ensemble outperforms 7-feature on 3-class (core task)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Table 4: 4-det+surface 3-cl F1=0.795 vs 7-feature 0.774 (2.1pp gap). Introduction claim 'competitive' is misleading for 3-class. Core competitiveness is cost-efficiency only.\"}\n  action_items:\n    - {round: 11, action: \"Clarify in Introduction that method trades 2pp 3-class F1 for 60% cost reduction; not claim parity\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"6-gen/5-gen/8-gen subset mixing impairs comparability\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Table 1 (8-gen 0.762) vs Table 4 (6-gen 0.774) not comparable. Llama/Mistral harder but difference unexplained. No master table of which experiment uses which subset.\"}\n  action_items:\n    - {round: 11, action: \"Add generator-subset summary table; explain 8-gen vs 6-gen F1 difference; unify main experiments to 8-gen where possible\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M1\"\n  summary: \"Discussion over-fragmented with \\\\paragraph{} (AI writing signature)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"7+ \\\\paragraph{} headers in Discussion. Should be consolidated into 3-4 natural paragraphs.\"}\n  action_items:\n    - {round: 11, action: \"Merge Discussion into coherent narrative paragraphs\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"'Entropy' misnomer (actually token-level NLL/surprisal)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Only footnote 1 clarifies. Both reviewers flag confusion risk.\"}\n  action_items:\n    - {round: 11, action: \"Use 'surprisal' or 'token-level NLL' consistently, or add prominent clarification beyond footnote\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"Tail decay rank range 100-1000 unjustified\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"No theoretical motivation. LOFO shows minimal impact (-0.33pp) so low priority.\"}\n  action_items:\n    - {round: 11, action: \"Add brief justification or range ablation\", assigned_to: \"Paper Agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === 历史 (R1-R6) ===\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Direction C. Persists as R7-W4.\"\n  resolution_round: 5\n\n- id: \"R5-TABLE1\"\n  summary: \"Table 1 only 6 generators\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"All 8.\"\n  resolution_round: 6"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-17T16:45:58.911903+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 17657}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-17T16:48:04.332465+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 11\n\n**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计声明; R2: 新颖性/完整性/Related Work/写作质量）\n**轮次**: Round 1（独立审稿 + 交叉分享，1 轮收敛）\n\n---\n\n## Summary\n\n本文提出 ordinal generation depth estimation 任务，将 AI 文本检测从二分类扩展为三分类（gen-0/gen-1/gen-2+）。核心发现是 differential depth response (DDR)：在递归生成链中，central-tendency features 随深度单调漂移，而 shape features 近似平稳。基于 7 个手工特征 + XGBoost 的分类器在 8 个 base model 生成器的 LOGO 评估下达到 3-class macro F1=0.762，leak-free binary F1=0.694。\n\n---\n\n## Strengths\n\n1. **任务定义新颖且及时**：从 binary detection 扩展到 ordinal depth estimation 是有价值的研究方向，与两篇 concurrent work 的定位区分准确。\n2. **评估协议严谨**：LOGO cross-validation + 14 个附录消融（cross-domain, cross-temperature, perturbation robustness, LOFO, QLoRA, 5-class 等），覆盖面远超同类投稿。\n3. **统计方法规范**：Bonferroni 校正、percentile bootstrap CI、TOST 等价性检验、KS 检验使用得当。\n4. **DDR 框架提供可解释洞察**：drifting vs. stationary 的分离是有启发性的实证观察。\n5. **透明诚实**：明确承认已知缺陷（gen-0 泄漏、base-model-only、instruction-tuning failure）。\n6. **轻量且可复现**：仅需 410M 参考模型 + 7 特征 + XGBoost（1.48M 参数），计算成本极低。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, consensus R1+R2] **Abstract framing 误导 + Gen-0 数据泄漏膨胀 headline metric**\n\n所有 generators 共享相同的 gen-0 Wikipedia seeds。在 LOGO 中，held-out generator 的 gen-0 测试样本与训练集 gen-0 完全相同，构成数据泄漏。Confusion matrix 显示 gen-0 recall=99.4%（几乎完美）vs gen-1=75.0%/gen-2+=73.7%。3-class LOGO F1=0.762 因 gen-0 的 trivially 高分类而膨胀。\n\n更严重的是，Abstract 以 cross-model chains 的 0.809 领衔（该设定甚至不使用 LOGO），LOGO 0.762 次要，而 leak-free binary F1=0.694（唯一不受泄漏影响的指标）完全未出现在 Abstract 中。真实的跨生成器无泄漏性能（0.694）与 Abstract 主打数字（0.809）相差 11.5pp。\n\n**Required action**: (a) Abstract 以 leak-free binary F1=0.694 为主指标；(b) 3-class F1 标注 gen-0 泄漏 caveat；(c) 理想方案：为每个 generator 使用独立 seed set 消除泄漏。\n\n---\n\n**MF2** [critical, consensus R1+R2] **仅限 base model，实际适用性与 Introduction 动机根本性脱节**\n\n全部 8 个 generator 为 base (pretrained) model。唯一的 instruction-tuned 实验：OLMo-Instruct LOGO F1=0.338，Qwen3-0.6B-chat length-matched binary F1≈0.50（近随机）。现实中网络 LLM 文本几乎全部来自 instruction-tuned/RLHF 模型。\n\nIntroduction 以 \"web-crawled pretraining corpora increasingly contain LLM-generated text\" 和 \"provenance tracking\" 为动机，但方法在实际应用场景中完全失效。且仅有单一 instruct model 数据点，无法判断这是系统性限制还是 model-specific。\n\n**Required action**: (a) Reframe Introduction 动机——从 \"解决 web contamination\" 转为 \"理解 recursive generation 分布特性\"，定位为 analytical/scientific contribution；(b) Abstract 明确 \"base model\" scope；(c) 减少 practical applicability 暗示。\n\n---\n\n**MF3** [critical, consensus R1+R2] **标题 \"Ordinal\" framing 与实际方法存在根本性矛盾**\n\n论文自身证据表明 ordinal structure 不提供任何增益：\n- Appendix D：CORAL ordinal regression, Frank-Hall reduction 均与 multiclass XGBoost 表现相当（overlapping CIs）\n- 5-class 尝试 F1 仅 0.50，gen-2/gen-3 F1=0.268/0.259\n- Gen-1/gen-2+ binary error rate 48%\n\n标题 \"Ordinal Generation Depth Estimation\" 创造了序数回归方法论贡献的预期，但实际是 3-class multiclass classification。序数性质在方法论和特征层面均未被有效利用。\n\n**Required action**: (a) 去掉标题中 \"Ordinal\"，改为 \"Generation Depth Classification\"；或 (b) 提供证据证明 ordinal structure 有帮助。\n\n---\n\n### Should-Fix（影响评分但非一票否决）\n\n**SF1** [warning, consensus] **DDR \"机制解释\" 超越实证证据**\n\n\"Location shift preserving distributional shape\" 的断言仅基于 7 个 summary statistics 的 Spearman ρ 和 KS 统计量，而非对完整 NLL 分布的直接分析。Discussion 中 \"softmax architecture constrains shape\" 是未经验证的直觉。\n\n→ 弱化措辞为 \"empirical pattern\" 而非 \"mechanism\"，或补充完整 NLL 分布直方图对比验证。\n\n**SF2** [warning, consensus] **Multi-detector ensemble 在 3-class（核心任务）上优于所提方法**\n\nTable 4：4-det+surface 3-cl F1=0.795 > 7-feature 0.774（2.1pp gap）。Introduction \"competitive performance\" 措辞模糊了这一事实。方法的核心竞争力仅在 cost-efficiency，而非 detection quality。\n\n→ Introduction 明确表述 cost-accuracy trade-off。\n\n**SF3** [warning, consensus] **6-gen/5-gen/8-gen 子集混用，数字难以横向比较**\n\nTable 1 (8-gen, F1=0.762) vs Table 4 (6-gen, F1=0.774)——同为 LOGO 但不可比。Llama/Mistral 更难分类导致 8-gen 下降 1.2pp，但从未解释。Appendix 大量使用 6-gen，无统一说明。\n\n→ 添加 generator-subset summary table；主实验统一 8-gen；解释差异来源。\n\n**SF4** [warning, consensus] **Downstream utility (Contribution 3) 本质是 null result**\n\nTOST 表明 depth-aware curation = random subsampling（±2% margin, p<0.001）。仅 n=3 seeds、单一 metric (perplexity)、小 scale (3,951 samples)。论文 frames 为 \"decoupling detectability from harm\"，但同样读作 \"depth info has no curation utility\"——与 data quality 动机矛盾。\n\n→ 在 Discussion 中诚实承认 null result；减少 Abstract/Introduction 中的 prominence。\n\n**SF5** [warning, consensus] **温度敏感性讨论不足**\n\nt=1.0 时 6pp degradation；cross-temperature transfer（t=0.7 训练 / t=1.0 测试）Qwen3-1.7B 从 0.789 骤降至 0.418。Cross-domain (t=1.0) 与 Wikipedia (t=0.7) 方向矛盾。论文对 unknown-temperature 部署场景的影响讨论不充分。\n\n→ 主文讨论 cross-temperature failure 及 unknown-temperature 限制。\n\n**SF6** [warning, consensus] **Reference model family bias 未分析**\n\nPythia-410M 作为 reference model，对 Pythia 家族 generators 可能产生 same-family 优势。Table 2 cross-reference 实验无法隔离此效应。\n\n→ 报告 same-family vs cross-family per-generator F1。\n\n---\n\n### Minor\n\n1. Discussion 过度使用 `\\paragraph{}`（7+ 标题），典型 AI 写作风格——应合并为 3-4 个自然段。\n2. \"Entropy\" 实为 token-level NLL/surprisal，仅 footnote 1 说明，易混淆——应在正文中更明确。\n3. Tail decay rank 范围 100-1000 缺乏理论支撑（LOFO 显示影响极小，低优先级）。\n4. Appendix G confusion matrix 使用 6-gen 而非 8-gen，与 Table 1 不对齐。\n5. |ρ| < 0.10 定义 \"near-stationary\" 阈值缺乏理论依据。\n6. Cross-domain 使用 t=1.0 而非主实验 t=0.7，结果不可直接比较。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全独立发现并达成 [AGREE]：\n- Gen-0 数据泄漏 + Abstract framing 误导 (MF1)\n- Base-model-only 与 Introduction 动机脱节 (MF2)\n- Ordinal framing overclaim (MF3)\n- DDR 机制解释超越证据 (SF1)\n- Multi-detector ensemble 更优 (SF2)\n- Generator subset 混用 (SF3)\n- Downstream null result (SF4)\n- Temperature sensitivity (SF5)\n- 全部 Minor issues\n\n## Reviewer Divergence\n\n**Gen-1/gen-2+ 区分能力弱的严重程度**：\n- R1 视为 Must-Fix (critical)——认为 48% error rate 使 \"ordinal depth estimation\" 名不副实，方法主要成功在于 gen-0 识别\n- R2 视为 Should-Fix (warning)——认为 binary F1=0.694 排除了 gen-0，是纯 depth discrimination 且优于所有单一 baseline；3-class ceiling 是 recursive generation 的固有特性（两篇 concurrent work 独立收敛于相同结论）\n\n**Director 裁决**：采纳 R2 的论证——binary F1=0.694 确实是排除 gen-0 后的真实 depth discrimination，且论文已透明报告此局限。但此问题与 MF3（Ordinal framing）互相加重：如果 gen-1/gen-2+ boundary 仅 52% 正确率，\"Ordinal Depth Estimation\" 的标题更难以自圆其说。因此将 gen-1/gen-2+ 区分弱作为 MF3 的 supporting evidence 而非独立 Must-Fix。\n\n---\n\n## Questions for Authors\n\n1. 如果为每个 LOGO fold 使用独立 gen-0 seeds（消除泄漏），3-class F1 下降多少？\n2. DDR 的 \"location shift preserving shape\" 能否用完整 NLL 分布的 location-scale family 检验直接验证？\n3. 是否测试过 Llama-3-chat / Mistral-Instruct 等其他 instruction-tuned 模型？OLMo-Instruct 的失败是系统性的还是 model-specific？\n4. Cross-model chains + LOGO（held-out generator 不出现在任何链的任何深度）的 F1？\n5. 多个参考模型特征的 concat/ensemble 能否改善 gen-1/gen-2+ 区分？\n\n---\n\n## Missing References\n\n引用总体充分（58 条，验证通过），以下可补充：\n1. M4/SemEval 2024 shared task 的 top-performing systems（具体方法，非仅 overview）\n2. Data provenance/lineage tracking 领域文献（与 §2.4 provenance 讨论相关）\n3. LLM output distribution 的信息论分析工作\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Confidence: 4/5**（两位 Reviewer 均仔细阅读全文 + 全部附录，熟悉 AI text detection 方法论）\n\n**评分理由**：\n\n本文最大的贡献是 task formulation（ordinal depth estimation）和 empirical finding（DDR drifting vs. stationary features 的分离）。实验执行质量高，统计方法规范，写作诚实。\n\n但三个根本性问题联合限制了 main conference 级别的影响力：\n\n1. **Scope 太窄**：仅限 base model（0.6B-8B）continuation chains，instruction-tuned 模型完全失效。Introduction 的 practical motivation 与实际贡献之间存在严重 gap。\n2. **Framing 不匹配**：标题强调 \"Ordinal Estimation\" 但 ordinal methods 无增益、gen-1/gen-2+ 边界 48% 错误率；Abstract 以泄漏膨胀的 0.809 领衔而非真实能力 0.694。\n3. **贡献增量有限**：方法不优于 multi-detector ensemble（3-class -2.1pp）；downstream utility 为 null result。核心竞争力仅在于 cost-efficiency（60% 成本减少）。\n\n如果重新 frame 为 \"an empirical study of distributional drift in recursive base-model generation chains\"，以 binary F1=0.694 为主指标，去掉 ordinal overclaim，诚实定位为 analytical contribution，这是一个扎实的 Findings paper。\n\n**EMNLP 2026 评分标准映射**：3.0 = Findings（可被 Findings 接收）。距 3.5 (Borderline Conference) 需解决 MF1-MF3 中至少两个（重新 frame + 消除泄漏）。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 以 3-class F1=0.809 (cross-model) 开头，这是最乐观的设定（非 LOGO、含 gen-0 泄漏）。应以 leak-free binary LOGO F1=0.694 为主。\n- \"Ordinal\" 在 Abstract 中设定了后文无法兑现的期待。\n- Contribution 3 (downstream) 可降低 prominence 或重新表述为 negative finding。\n\n### Introduction\n- Web contamination / data quality 动机与 base-model-only scope 脱节。应重新定位为 analytical/scientific contribution。\n- \"outperforming all individual detection baselines\" 准确但暗示整体最优——multi-det ensemble 在 3-class 上更强。\n\n### Related Work\n- 覆盖充分，positioning 准确。与 concurrent work 的区分诚实。\n- 可补充 data provenance 和 SemEval top systems。\n\n### Method\n- 特征设计合理但 standard（NLL statistics + lexical diversity）。\n- Tail decay rank 100-1000 未 justify。\n- \"Entropy\" misnomer 应在正文（非仅 footnote）中解决。\n\n### Results\n- LOGO 设计恰当，但 gen-0 泄漏问题需从根本上修复或在 framing 中充分承认。\n- DDR 分析有洞察价值，但机制解释应弱化为 empirical pattern。\n- Generator subset 不一致影响可读性和可比性。\n\n### Discussion\n- 过度碎片化（7+ \\paragraph{}）。\n- Instruction-tuning limitation 讨论充分但应反映在 Introduction 动机中。\n- Temperature robustness 的 cross-temperature transfer failure 应更显著讨论。\n\n### Limitations\n- 诚实且全面，值得肯定。",
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 11\n\n**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计声明; R2: 新颖性/完整性/Related Work/写作质量）\n**轮次**: Round 1（独立审稿 + 交叉分享，1 轮收敛）\n\n---\n\n## Summary\n\n本文提出 ordinal generation depth estimation 任务，将 AI 文本检测从二分类扩展为三分类（gen-0/gen-1/gen-2+）。核心发现是 differential depth response (DDR)：在递归生成链中，central-tendency features 随深度单调漂移，而 shape features 近似平稳。基于 7 个手工特征 + XGBoost 的分类器在 8 个 base model 生成器的 LOGO 评估下达到 3-class macro F1=0.762，leak-free binary F1=0.694。\n\n---\n\n## Strengths\n\n1. **任务定义新颖且及时**：从 binary detection 扩展到 ordinal depth estimation 是有价值的研究方向，与两篇 concurrent work 的定位区分准确。\n2. **评估协议严谨**：LOGO cross-validation + 14 个附录消融（cross-domain, cross-temperature, perturbation robustness, LOFO, QLoRA, 5-class 等），覆盖面远超同类投稿。\n3. **统计方法规范**：Bonferroni 校正、percentile bootstrap CI、TOST 等价性检验、KS 检验使用得当。\n4. **DDR 框架提供可解释洞察**：drifting vs. stationary 的分离是有启发性的实证观察。\n5. **透明诚实**：明确承认已知缺陷（gen-0 泄漏、base-model-only、instruction-tuning failure）。\n6. **轻量且可复现**：仅需 410M 参考模型 + 7 特征 + XGBoost（1.48M 参数），计算成本极低。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, consensus R1+R2] **Abstract framing 误导 + Gen-0 数据泄漏膨胀 headline metric**\n\n所有 generators 共享相同的 gen-0 Wikipedia seeds。在 LOGO 中，held-out generator 的 gen-0 测试样本与训练集 gen-0 完全相同，构成数据泄漏。Confusion matrix 显示 gen-0 recall=99.4%（几乎完美）vs gen-1=75.0%/gen-2+=73.7%。3-class LOGO F1=0.762 因 gen-0 的 trivially 高分类而膨胀。\n\n更严重的是，Abstract 以 cross-model chains 的 0.809 领衔（该设定甚至不使用 LOGO），LOGO 0.762 次要，而 leak-free binary F1=0.694（唯一不受泄漏影响的指标）完全未出现在 Abstract 中。真实的跨生成器无泄漏性能（0.694）与 Abstract 主打数字（0.809）相差 11.5pp。\n\n**Required action**: (a) Abstract 以 leak-free binary F1=0.694 为主指标；(b) 3-class F1 标注 gen-0 泄漏 caveat；(c) 理想方案：为每个 generator 使用独立 seed set 消除泄漏。\n\n---\n\n**MF2** [critical, consensus R1+R2] **仅限 base model，实际适用性与 Introduction 动机根本性脱节**\n\n全部 8 个 generator 为 base (pretrained) model。唯一的 instruction-tuned 实验：OLMo-Instruct LOGO F1=0.338，Qwen3-0.6B-chat length-matched binary F1≈0.50（近随机）。现实中网络 LLM 文本几乎全部来自 instruction-tuned/RLHF 模型。\n\nIntroduction 以 \"web-crawled pretraining corpora increasingly contain LLM-generated text\" 和 \"provenance tracking\" 为动机，但方法在实际应用场景中完全失效。且仅有单一 instruct model 数据点，无法判断这是系统性限制还是 model-specific。\n\n**Required action**: (a) Reframe Introduction 动机——从 \"解决 web contamination\" 转为 \"理解 recursive generation 分布特性\"，定位为 analytical/scientific contribution；(b) Abstract 明确 \"base model\" scope；(c) 减少 practical applicability 暗示。\n\n---\n\n**MF3** [critical, consensus R1+R2] **标题 \"Ordinal\" framing 与实际方法存在根本性矛盾**\n\n论文自身证据表明 ordinal structure 不提供任何增益：\n- Appendix D：CORAL ordinal regression, Frank-Hall reduction 均与 multiclass XGBoost 表现相当（overlapping CIs）\n- 5-class 尝试 F1 仅 0.50，gen-2/gen-3 F1=0.268/0.259\n- Gen-1/gen-2+ binary error rate 48%\n\n标题 \"Ordinal Generation Depth Estimation\" 创造了序数回归方法论贡献的预期，但实际是 3-class multiclass classification。序数性质在方法论和特征层面均未被有效利用。\n\n**Required action**: (a) 去掉标题中 \"Ordinal\"，改为 \"Generation Depth Classification\"；或 (b) 提供证据证明 ordinal structure 有帮助。\n\n---\n\n### Should-Fix（影响评分但非一票否决）\n\n**SF1** [warning, consensus] **DDR \"机制解释\" 超越实证证据**\n\n\"Location shift preserving distributional shape\" 的断言仅基于 7 个 summary statistics 的 Spearman ρ 和 KS 统计量，而非对完整 NLL 分布的直接分析。Discussion 中 \"softmax architecture constrains shape\" 是未经验证的直觉。\n\n→ 弱化措辞为 \"empirical pattern\" 而非 \"mechanism\"，或补充完整 NLL 分布直方图对比验证。\n\n**SF2** [warning, consensus] **Multi-detector ensemble 在 3-class（核心任务）上优于所提方法**\n\nTable 4：4-det+surface 3-cl F1=0.795 > 7-feature 0.774（2.1pp gap）。Introduction \"competitive performance\" 措辞模糊了这一事实。方法的核心竞争力仅在 cost-efficiency，而非 detection quality。\n\n→ Introduction 明确表述 cost-accuracy trade-off。\n\n**SF3** [warning, consensus] **6-gen/5-gen/8-gen 子集混用，数字难以横向比较**\n\nTable 1 (8-gen, F1=0.762) vs Table 4 (6-gen, F1=0.774)——同为 LOGO 但不可比。Llama/Mistral 更难分类导致 8-gen 下降 1.2pp，但从未解释。Appendix 大量使用 6-gen，无统一说明。\n\n→ 添加 generator-subset summary table；主实验统一 8-gen；解释差异来源。\n\n**SF4** [warning, consensus] **Downstream utility (Contribution 3) 本质是 null result**\n\nTOST 表明 depth-aware curation = random subsampling（±2% margin, p<0.001）。仅 n=3 seeds、单一 metric (perplexity)、小 scale (3,951 samples)。论文 frames 为 \"decoupling detectability from harm\"，但同样读作 \"depth info has no curation utility\"——与 data quality 动机矛盾。\n\n→ 在 Discussion 中诚实承认 null result；减少 Abstract/Introduction 中的 prominence。\n\n**SF5** [warning, consensus] **温度敏感性讨论不足**\n\nt=1.0 时 6pp degradation；cross-temperature transfer（t=0.7 训练 / t=1.0 测试）Qwen3-1.7B 从 0.789 骤降至 0.418。Cross-domain (t=1.0) 与 Wikipedia (t=0.7) 方向矛盾。论文对 unknown-temperature 部署场景的影响讨论不充分。\n\n→ 主文讨论 cross-temperature failure 及 unknown-temperature 限制。\n\n**SF6** [warning, consensus] **Reference model family bias 未分析**\n\nPythia-410M 作为 reference model，对 Pythia 家族 generators 可能产生 same-family 优势。Table 2 cross-reference 实验无法隔离此效应。\n\n→ 报告 same-family vs cross-family per-generator F1。\n\n---\n\n### Minor\n\n1. Discussion 过度使用 `\\paragraph{}`（7+ 标题），典型 AI 写作风格——应合并为 3-4 个自然段。\n2. \"Entropy\" 实为 token-level NLL/surprisal，仅 footnote 1 说明，易混淆——应在正文中更明确。\n3. Tail decay rank 范围 100-1000 缺乏理论支撑（LOFO 显示影响极小，低优先级）。\n4. Appendix G confusion matrix 使用 6-gen 而非 8-gen，与 Table 1 不对齐。\n5. |ρ| < 0.10 定义 \"near-stationary\" 阈值缺乏理论依据。\n6. Cross-domain 使用 t=1.0 而非主实验 t=0.7，结果不可直接比较。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全独立发现并达成 [AGREE]：\n- Gen-0 数据泄漏 + Abstract framing 误导 (MF1)\n- Base-model-only 与 Introduction 动机脱节 (MF2)\n- Ordinal framing overclaim (MF3)\n- DDR 机制解释超越证据 (SF1)\n- Multi-detector ensemble 更优 (SF2)\n- Generator subset 混用 (SF3)\n- Downstream null result (SF4)\n- Temperature sensitivity (SF5)\n- 全部 Minor issues\n\n## Reviewer Divergence\n\n**Gen-1/gen-2+ 区分能力弱的严重程度**：\n- R1 视为 Must-Fix (critical)——认为 48% error rate 使 \"ordinal depth estimation\" 名不副实，方法主要成功在于 gen-0 识别\n- R2 视为 Should-Fix (warning)——认为 binary F1=0.694 排除了 gen-0，是纯 depth discrimination 且优于所有单一 baseline；3-class ceiling 是 recursive generation 的固有特性（两篇 concurrent work 独立收敛于相同结论）\n\n**Director 裁决**：采纳 R2 的论证——binary F1=0.694 确实是排除 gen-0 后的真实 depth discrimination，且论文已透明报告此局限。但此问题与 MF3（Ordinal framing）互相加重：如果 gen-1/gen-2+ boundary 仅 52% 正确率，\"Ordinal Depth Estimation\" 的标题更难以自圆其说。因此将 gen-1/gen-2+ 区分弱作为 MF3 的 supporting evidence 而非独立 Must-Fix。\n\n---\n\n## Questions for Authors\n\n1. 如果为每个 LOGO fold 使用独立 gen-0 seeds（消除泄漏），3-class F1 下降多少？\n2. DDR 的 \"location shift preserving shape\" 能否用完整 NLL 分布的 location-scale family 检验直接验证？\n3. 是否测试过 Llama-3-chat / Mistral-Instruct 等其他 instruction-tuned 模型？OLMo-Instruct 的失败是系统性的还是 model-specific？\n4. Cross-model chains + LOGO（held-out generator 不出现在任何链的任何深度）的 F1？\n5. 多个参考模型特征的 concat/ensemble 能否改善 gen-1/gen-2+ 区分？\n\n---\n\n## Missing References\n\n引用总体充分（58 条，验证通过），以下可补充：\n1. M4/SemEval 2024 shared task 的 top-performing systems（具体方法，非仅 overview）\n2. Data provenance/lineage tracking 领域文献（与 §2.4 provenance 讨论相关）\n3. LLM output distribution 的信息论分析工作\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Confidence: 4/5**（两位 Reviewer 均仔细阅读全文 + 全部附录，熟悉 AI text detection 方法论）\n\n**评分理由**：\n\n本文最大的贡献是 task formulation（ordinal depth estimation）和 empirical finding（DDR drifting vs. stationary features 的分离）。实验执行质量高，统计方法规范，写作诚实。\n\n但三个根本性问题联合限制了 main conference 级别的影响力：\n\n1. **Scope 太窄**：仅限 base model（0.6B-8B）continuation chains，instruction-tuned 模型完全失效。Introduction 的 practical motivation 与实际贡献之间存在严重 gap。\n2. **Framing 不匹配**：标题强调 \"Ordinal Estimation\" 但 ordinal methods 无增益、gen-1/gen-2+ 边界 48% 错误率；Abstract 以泄漏膨胀的 0.809 领衔而非真实能力 0.694。\n3. **贡献增量有限**：方法不优于 multi-detector ensemble（3-class -2.1pp）；downstream utility 为 null result。核心竞争力仅在于 cost-efficiency（60% 成本减少）。\n\n如果重新 frame 为 \"an empirical study of distributional drift in recursive base-model generation chains\"，以 binary F1=0.694 为主指标，去掉 ordinal overclaim，诚实定位为 analytical contribution，这是一个扎实的 Findings paper。\n\n**EMNLP 2026 评分标准映射**：3.0 = Findings（可被 Findings 接收）。距 3.5 (Borderline Conference) 需解决 MF1-MF3 中至少两个（重新 frame + 消除泄漏）。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 以 3-class F1=0.809 (cross-model) 开头，这是最乐观的设定（非 LOGO、含 gen-0 泄漏）。应以 leak-free binary LOGO F1=0.694 为主。\n- \"Ordinal\" 在 Abstract 中设定了后文无法兑现的期待。\n- Contribution 3 (downstream) 可降低 prominence 或重新表述为 negative finding。\n\n### Introduction\n- Web contamination / data quality 动机与 base-model-only scope 脱节。应重新定位为 analytical/scientific contribution。\n- \"outperforming all individual detection baselines\" 准确但暗示整体最优——multi-det ensemble 在 3-class 上更强。\n\n### Related Work\n- 覆盖充分，positioning 准确。与 concurrent work 的区分诚实。\n- 可补充 data provenance 和 SemEval top systems。\n\n### Method\n- 特征设计合理但 standard（NLL statistics + lexical diversity）。\n- Tail decay rank 100-1000 未 justify。\n- \"Entropy\" misnomer 应在正文（非仅 footnote）中解决。\n\n### Results\n- LOGO 设计恰当，但 gen-0 泄漏问题需从根本上修复或在 framing 中充分承认。\n- DDR 分析有洞察价值，但机制解释应弱化为 empirical pattern。\n- Generator subset 不一致影响可读性和可比性。\n\n### Discussion\n- 过度碎片化（7+ \\paragraph{}）。\n- Instruction-tuning limitation 讨论充分但应反映在 Introduction 动机中。\n- Temperature robustness 的 cross-temperature transfer failure 应更显著讨论。\n\n### Limitations\n- 诚实且全面，值得肯定。",
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-17T16:48:08.097142+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3764
}
```

</details>

---


### Assistant

_source line 492 · 2026-05-17T16:48:16.964095+00:00_

审稿报告已投递至 Research Director。

---

**Round 11 审稿完成总结：**

- **评分**：3.0 (Findings)，两位 Reviewer ���立一致
- **3 个 Must-Fix**：(1) Gen-0 泄漏 + Abstract framing 误导；(2) Base-model-only 与实际动机脱节；(3) 标题 "Ordinal" overclaim
- **6 个 Should-Fix**：DDR 机制过度解释、multi-det ensemble 更优、generator subset 混用、downstream null result、温度敏感性、reference model family bias
- **收敛情况**：唯一分歧（gen-1/gen-2+ 区分严重程度）已裁决并入 MF3 作为 supporting evidence
- **Issue Tracker**：已同步更新，7 个 open issues 待 Research Director 处理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 50

## Round 50

2 recorded events


### User

_source line 493 · 2026-05-17T16:48:19.506241+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

逐条回应 Reviewer 2 全部 18 个问题的结果：**15 个 [AGREE]，1 个 [REBUT]**（SemEval 引用已存在），2 个 [AGREE] 带补充细节。

核心共识：两位 Reviewer 在三个 Must-Fix 上完全一致——gen-0 泄漏、base-model-only、ordinal framing 过度。我补充了 Reviewer 2 的一个 appendix 编号错误（标为 Appendix H 实为 Appendix D），并对温度敏感性（W5）补充了 cross-temperature transfer mismatch 的更严重证据（Qwen3-1.7B mismatch F1 从 0.789 降至 0.418）。维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 494 · 2026-05-17T16:48:31.075841+00:00_

审稿流程已完成。报告已投递至 Research Director。

**本轮审稿总结**：
- 两位 Reviewer 独立评分一致：**Overall 3.0 (Findings)**
- 3 个 Must-Fix 达成完全共识（gen-0 泄漏/framing、base-model-only 脱节、Ordinal 标题 overclaim）
- 6 个 Should-Fix 达成共识
- 唯一分歧（gen-1/gen-2+ 区分严重程度）已在报告中裁决并纳入 MF3 supporting evidence
- Issue Tracker 已同步更新（7 个新 open issues + 3 个历史 issue 重新打开）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 51

## Round 51

62 recorded events


### User

_source line 495 · 2026-05-17T17:15:12.511900+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026 cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-17T17:15:20.531374+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-17T17:15:20.582364+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-17T17:15:25.286716+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 499 · 2026-05-17T17:15:25.387497+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-17T17:15:29.703548+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,request_external_review,get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,request_external_review,get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-17T17:15:29.804318+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-17T17:15:33.967829+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-17T17:15:34.018314+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-17T17:15:37.895827+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-17T17:15:39.001928+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (50 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- multi_domain_t07（准备中）\n- review-exp-a-baseline-ensemble: 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异（准备中）\n- plan-004-prep: Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）（准备中）\n- plan-001-restore（准备中）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **exp_048_cross_temp_transfer** (success): Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters ← 基于 exp_047_multi_domain_t07\n- **exp_047_multi_domain_t07** (success): Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers ← 基于 exp_043_multi_domain_seeds\n- **multi-domain-seeds** (success): Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Aca
…[truncated 628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1106
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-17T17:15:39.303335+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-17T17:15:46.380310+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission guidelines author instructions"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authorship Changes Policy for ACL Venue Papers - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/Authorship_Changes_Policy_for_ACL_Venue_Papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Community announcement: Submission dates and process for EACL, NAACL and ACL","url":"https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, here is information about ACL Rolling Review (ARR) and ACL 2026 submission guidelines:

## Overview

ACL 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and area chairs, and then commit their reviewed article
…[truncated 1224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 7076
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-17T17:15:51.353399+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org cfp 2026 submission format page limit long paper short paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclrollingreview.org cfp 2026 submission format page limit long paper short paper"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-17T17:15:56.322763+00:00_

Web search results for query: "aclrollingreview.org cfp 2026 submission format page limit long paper short paper"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Submission Form Fields","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results from the ACL Rolling Review website, here is the submission format information for 2026:

## Page Limits

Long papers must follow a page limit of 8 pages, while short papers have a page limit of 4 pages, not including limitations and ethical considerations.

## Paper Types

All long, short, and theme papers must follow the ACL Author Guidelines.

## Submission Format Requirements

Submission is electronic, using the OpenReview.net platform. Paper submissions must use the official ACL style template.

## Additional Requirements

Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected. ACL requires all submissions to have a section titled "Limitations", which should be placed after the conclusion section and before references, and does not count towards th
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 4969
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-17T17:16:00.287690+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 \"May\" deadline submission date cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 \"May\" deadline submission date cycle"
  }
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-17T17:16:00.589004+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 commitment deadline ARR cycle"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-17T17:16:04.852735+00:00_

Web search results for query: "ACL Rolling Review 2026 "May" deadline submission date cycle"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here's information about the ACL Rolling Review 2026 May deadline:

The ACL Peer Review Committee recommended switching to 10-week cycles, with the new schedule starting in May 2025. This means that instead of 6 cycles a year there will generally be 5, and the cycles will always start on Mondays, developing a consistent schedule that clashes with weekends less.

However, the search results don't provide the specific submission deadline date for the May 2026 cycle itself. The official ACL Rolling Review websi
…[truncated 530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 4565
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-17T17:16:05.807687+00:00_

Web search results for query: "EMNLP 2026 commitment deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's the information about EMNLP 2026 commitment deadline related to the ARR cycle:

The EMNLP 2026 commitment deadline is August 2, 2026, and the ARR submission deadline for long and short papers is May 25, 2026.

Papers must be submitted, at latest, by the
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5218
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-17T17:16:10.726075+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main_conference_papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main_conference_papers"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-17T17:16:16.697986+00:00_

Web search results for query: "site:2026.emnlp.org calls main_conference_papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

I found the Call for Main Conference Papers for EMNLP 2026. Here's the key information:

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

**Key Details:**

- **Conference Location & Dates**: The conference will be held in Budapest, Hungary from October 24th to October 29th, 2026.

- **Submission Process**: Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

- **Scope**: Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

- **Special Theme**: The EMNLP 2026 special theme
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5971
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-17T17:16:20.461091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL 2026\" \"style files\" OR \"style template\" submission format anonymity requirements acl-org github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL 2026\" \"style files\" OR \"style template\" submission format anonymity requirements acl-org github"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-17T17:16:26.710649+00:00_

Web search results for query: ""ACL 2026" "style files" OR "style template" submission format anonymity requirements acl-org github"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"GitHub - acl-org/acl-style-files: Official style files for papers submitted to venues of the Association for Computational Linguistics · GitHub","url":"https://github.com/acl-org/acl-style-files"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on my search results, here's what I found regarding ACL 2026 style files, submission format, and anonymity requirements:

## Style Files and Submission Format

Authors may not modify these style files or use template designed for other conferences. Submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be rejected without review.

Style files are strongly recomme
…[truncated 1007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6249
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-17T17:16:40.215236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-17T17:16:40.767236+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{lineno}
11	\linenumbers
12	
13	\graphicspath{{../chart/}}
14	
15	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in LLM Text Chains}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{results}
28	
29	\input{discussion}
30	\input{conclusion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\appendix
37	
38	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
39	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
40	
41	\input{appendix_dataset_stats}
42	
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{End-to-End Depth Classification (QLoRA)}
56	\label{app:qlora}
57	\input{appendix_qlora}
58	
59	\section{Leave-One-Feature-Out Analysis}
60	\label{app:lofo}
61	\input{appendix_lofo}
62	
63	\section{Confusion Matrix}
64	\label{app:confusion}
65	\input{appendix_confusion_matrix}
66	
67	\section{Classifier Sensitivity}
68	\label{app:classifier}
69	\input{appendix_classifier}
70	
71	\section{Robustness to Text Perturbation}
72	\label{app:human-edit}
73	\input{appendix_human_edit}
74	
75	\section{Cross-Domain Generalization}
76	\label{app:domain}
77	\input{appendix_domain}
78	
79	\section{Error Analysis of Binary Classifica
…[truncated 542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-17T17:16:40.918070+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 521 · 2026-05-17T17:16:41.018933+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-17T17:16:46.235514+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-17T17:16:46.687377+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-17T17:16:46.737965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-17T17:16:47.090035+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	LLM-generated text increasingly re-enters the web and seeds subsequent generation, producing recursive chains whose outputs progressively diverge from human-written text.
4	We ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Studying eight base models from five families, we identify a \emph{differential depth response} (DDR): central-tendency features (mean entropy, lexical diversity) drift monotonically with generation depth, while shape features (entropy max, vocabulary tail slope) remain near-stationary.
6	This pattern is consistent with a location shift in the token-level negative log-likelihood (NLL) distribution that preserves distributional shape.
7	Exploiting this complementarity, a 7-feature ensemble achieves binary F1\,=\,0.764 on heterogeneous cross-model chains and 0.694 under leave-one-generator-out (LOGO) evaluation across eight generators (3-class macro F1\,=\,0.809 and 0.762, respectively), with competitive performance at substantially lower computational cost than multi-detector alternatives.
8	A TOST equivalence test further confirms that depth-aware data selection yields training utility equivalent to random subsampling ($\pm$2\% margin, $p < 0.001$) within $\leq$4 generations, indicating that the detected distributional shift does not translate to downstream perplexity degradation.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-17T17:16:47.090409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-17T17:16:47.140919+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-generated text increasingly re-enters the web and seeds subsequent generation \cite{dolma,fineweb}, with estimates suggesting that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}.
5	The result is recursive generation chains whose outputs progressively diverge from human-written text.
6	Understanding how distributional features evolve across recursive generation depths is a fundamental question for characterizing recursive generation dynamics, yet existing methods \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions, conflating qualitatively different material: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	
8	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and refer to the overall framework as \emph{depth fingerprinting}.
9	No existing method addresses this task in non-paraphrastic continuation chains.
10	
11	The key finding is a \emph{differential depth response} (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) remain near-stationary.
12	This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution while preserving its shape: the softmax architecture and fixed sampling parameters constrain distributional shape under standard decoding regimes, while each successive generation compr
…[truncated 2167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-17T17:16:53.313821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-17T17:16:53.515118+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig2_framework.pdf}
7	\caption{Overview of the depth fingerprinting framework. Given a text, reference-model features (entropy statistics under Pythia-410M) and surface features (lexical diversity) are extracted and fed to an XGBoost classifier trained under Leave-One-Generator-Out cross-validation. The feature set combines drifting indicators (entropy mean, TTR, hapax ratio) that capture the monotonic location shift with stationary indicators (entropy max, tail decay) that provide a stable baseline, exploiting their differential depth response for ordinal classification.}
8	\label{fig:framework}
9	\end{figure*}
10	
11	\subsection{Task Formulation}
12	\label{sec:task}
13	
14	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
15	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
16	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
17	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
18	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
19	
20	\subsection{Generation Chain Construction}
21	\label{sec:generation}
22	
23	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-
…[truncated 8238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-17T17:16:53.515660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-17T17:16:53.566394+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), the 3-class metric may carry upward bias from memorized gen-0 patterns; we therefore also report a leak-free binary metric (gen-1 vs.\ gen-2+): F1\,=\,0.694, CI [0.688, 0.700], which is unaffected by this sharing.
9	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B); the primary difficulty is distinguishing gen-1 from gen-2+ (Appendix~\ref{app:confusion}).
10	Larger generators show moderate degradation (Qwen3-8B: 0.692, Mistral-7B: 0.633) relative to the 0.694 average.
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield 3-class F1\,=\,0.809 and binary F1\,=\,0.764 under 5-fold CV,\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists when text passes through heterogeneous generators.
14	The higher cross-model performance relative to single-generator LOGO (3-class: 0.809 vs.\ 0.762) suggests that generator heterogeneity amplifies distributional shifts between depths, making each recursive step more distinct.
15	Under class balancing, macro F1 reaches 0.831 (per-class breakdown in Appendix~\ref{app:cross-model-detail}).
16	
17	Leave-one-family-out (LOFO) evaluation yields average binary F1\,=\,0.686, confirming transfer across architectural families.
18	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633), consistent with higher-capacity models compressing the feature ma
…[truncated 9144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-17T17:17:00.541657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-17T17:17:01.043782+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The near-stationarity of shape features across recursive depths is consistent with the softmax architecture and fixed sampling parameters constraining distributional shape: recursive generation shifts context toward high-probability regions without altering the generation mechanism itself.
5	One hypothesis is that standard decoding regimes inherently preserve the functional form of the NLL distribution while allowing its location to drift.
6	Sampling ablation supports this as a tendency rather than an architectural guarantee ($t \in [0.5, 0.7]$: ${\leq}0.3$\,pp degradation; $t = 1.0$: $-6$\,pp; Appendix~\ref{app:sampling-sensitivity}).
7	Prompt-type dependence further modulates the effect: semantic-preservation constraints attenuate drift (elaboration F1\,=\,0.730 vs.\ continuation 0.781; Appendix~\ref{app:prompt-type}), consistent with \citet{broken_telephone} showing that tasks anchoring the output distribution to the input leave less room for recursive drift to accumulate.
8	Cross-type transfer remains viable (F1\,=\,0.753).
9	
10	At the document level, gen-1 per-class F1\,=\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\sqrt{n})$.
11	The gen-1\,/\,gen-2+ boundary concentrates 86\% of binary errors as false negatives (gen-2+ predicted as gen-1), with depth-2 error rate at 48\% vs.\ 20\% for depth-4, consistent with DDR predictions that the first recursive step produces the smallest location shift; larger generators exacerbate this (Mistral-7B error rate 45\% vs.\ Pythia-1B 18\%; Appendix~\ref{app:error-analysis}).
12	Reference-model family bias is limited: Pythia generators show slightly higher F1 with the Pythia-410M reference, but cross-reference spread is only 0.013\,pp (Table~\ref{tab:cross-ref}).
13	Cross-temperature transfer presents a more significant limitation: classifiers trained at $t{=}0.7$ degrade substantially when tested at $t{=
…[truncated 1493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-17T17:17:01.044291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-17T17:17:01.496542+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and documented a differential depth response across eight base-model generators from five families: recursive generation is consistent with a systematic location shift in the token-level NLL distribution that preserves distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (binary F1\,=\,0.764 on cross-model chains, 0.694 under LOGO; 3-class: 0.809 and 0.762, respectively).
5	A TOST equivalence test confirms that depth-aware data curation yields training utility equivalent to random subsampling ($\pm$2\%, $p < 0.001$) within chains of $\leq$4 generations as measured by perplexity, indicating that detectability does not entail downstream perplexity degradation.
6	
7	Two boundaries define the scope: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.
8	All code, data, and trained models will be released upon publication.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-17T17:17:01.497010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-17T17:17:01.949036+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 under a 7-generator split).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary e
…[truncated 2124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-17T17:17:01.999607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-17T17:17:02.050236+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
12	Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
13	Our contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance.
14	This is orthogonal to source attribution \cite{uchendu_attribution,munir_looking_glass}, which identifies \emph{which} model generated text; our LOGO
…[truncated 4237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-17T17:17:07.678918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-17T17:17:08.180910+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	
10	\paragraph{Licenses.}
11	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
12	Wikipedia seed passages are distributed under CC BY-SA 3.0.
13	
14	\paragraph{Compute budget.}
15	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
16	
17	\paragraph{Software.}
18	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-17T17:17:08.281692+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-17T17:17:08.384031+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-17T17:17:13.455788+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-17T17:17:13.558995+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_2.md:177:项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），未请求。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/archive/feishu_group_oc_dbd68d7879a81efc0c108e9844b15d0b_director_20260515T135932_964533.jsonl:1932:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/worker_diagnose_qwen17b-sighup-root-cause_20260514T220218.jsonl:53:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/feishu_group_oc_999770e4e57bfc6eabd12fc1f64af1ef_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/chats/feishu_group_oc_999770e4e57bfc6eabd12fc1f64af1ef_director.jsonl:6:{"ts": "2026-05-15T11:51:25.901207+00:00", "role": "tool", "sess
…[truncated 9957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-17T17:17:58.984647+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/gen-depth-fingerprint/artifacts/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/gen-depth-fingerprint/artifacts/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-17T17:17:59.035254+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-17T17:18:03.553362+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/ -name \"*.md\" 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check review reports directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/ -name \"*.md\" 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check review reports directory"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-17T17:18:03.704435+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_reports/round_9.md
round_1.md
round_10.md
round_2.md
round_3.md
round_4.md
round_5.md
round_6.md
round_7.md
round_8.md
round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-17T17:18:27.104050+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 551 · 2026-05-17T17:18:27.154707+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-17T17:18:50.627907+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你负责**方法严谨性 + 实验设计 + 统计 claims**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references）\n- **模板**: ACL official style files（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录**: 允许，参与审稿\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## 论文概要\n\"Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\"——提出 generation depth classification（gen-0/gen-1/gen-2+），利用 differential depth response（DDR）中 drifting vs stationary features 的互补性，用 7-feature XGBoost ensemble 在 8 个 base model generator 上实现 3-class LOGO F1=0.762。\n\n## 你的审查重点\n\n请严格评估以下方面：\n\n1. **实验设计的严谨性**：\n   - LOGO 评估中 gen-0 seed sharing 是否引入系统性偏差？论文对此的处理是否充分？\n   - 8 个 generator 的选择是否有代表性？参数规模 0.6B-8B 是否覆盖足够？\n   - Cross-model chains 使用的是 5-generator subset 而非 full 8-generator，这个不一致是否有问题？\n   - Temperature 固定为 0.7 的合理性，以及 t=1.0 时 -6pp 退化的严重程度\n\n2. **统计 claims 的可靠性**：\n   - Bootstrap CI、McNemar test、TOST equivalence test 的使用是否正确？\n   - Bonferroni correction 的应用是否恰当？\n   - \"competitive performance\" 的 claim 是否被数据支持（Table 3 显示 7-feature 实际低于 4-detector ensemble）？\n   - Spearman correlation thresholds（|ρ|>0.60 为 \"substantial\"，<0.10 为 \"near-stationary\"）是否有标准支撑？\n\n3. **方法论缺陷**：\n   - Pythia-410M 同时作为 reference model 又与 2 个 generator 共享架构，是否存在信息泄露？\n   - XGBoost hyperparameters 固定不调参，是否公平？\n   - 7 个 features 的选择是否有 cherry-picking 嫌疑（entropy_min 贡献几乎为零但仍保留）？\n   - Downstream utility 实验（TOST）的结论是否被过度解读？\n\n4. **可复现性**：\n   - 实验细节是否足够复现？\n   - 数据集构建的随机性控制如何？\n\n请给出完整审稿意见，包含 Strengths、Weaknesses（逐条编号）、Questions、Minor Issues。",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你负责**方法严谨性 + 实验设计 + 统计 claims**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references）\n- **模板**: ACL official style files（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录**: 允许，参与审稿\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## 论文概要\n\"Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\"——提出 generation depth classification（gen-0/gen-1/gen-2+），利用 differential depth response（DDR）中 drifting vs stationary features 的互补性，用 7-feature XGBoost ensemble 在 8 个 base model generator 上实现 3-class LOGO F1=0.762。\n\n## 你的审查重点\n\n请严格评估以下方面：\n\n1. **实验设计的严谨性**：\n   - LOGO 评估中 gen-0 seed sharing 是否引入系统性偏差？论文对此的处理是否充分？\n   - 8 个 generator 的选择是否有代表性？参数规模 0.6B-8B 是否覆盖足够？\n   - Cross-model chains 使用的是 5-generator subset 而非 full 8-generator，这个不一致是否有问题？\n   - Temperature 固定为 0.7 的合理性，以及 t=1.0 时 -6pp 退化的严重程度\n\n2. **统计 claims 的可靠性**：\n   - Bootstrap CI、McNemar test、TOST equivalence test 的使用是否正确？\n   - Bonferroni correction 的应用是否恰当？\n   - \"competitive performance\" 的 claim 是否被数据支持（Table 3 显示 7-feature 实际低于 4-detector ensemble）？\n   - Spearman correlation thresholds（|ρ|>0.60 为 \"substantial\"，<0.10 为 \"near-stationary\"）是否有标准支撑？\n\n3. **方法论缺陷**：\n   - Pythia-410M 同时作为 reference model 又与 2 个 generator 共享架构，是否存在信息泄露？\n   - XGBoost hyperparameters 固定不调参，是否公平？\n   - 7 个 features 的选择是否有 cherry-picking 嫌疑（entropy_min 贡献几乎为零但仍保留）？\n   - Downstream utility 实验（TOST）的结论是否被过度解读？\n\n4. **可复现性**：\n   - 实验细节是否足够复现？\n   - 数据集构建的随机性控制如何？\n\n请给出完整审稿意见，包含 Strengths、Weaknesses（逐条编号）、Questions、Minor Issues。",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-17T17:19:06.500540+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15872
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-17T17:19:06.861805+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你负责**新颖性 + 完整性 + Related Work + 格式**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references）\n- **模板**: ACL official style files（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录**: 允许，参与审稿\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## 论文概要\n\"Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\"——提出 generation depth classification（gen-0/gen-1/gen-2+），利用 differential depth response（DDR）中 drifting vs stationary features 的互补性，用 7-feature XGBoost ensemble 在 8 个 base model generator 上实现 3-class LOGO F1=0.762。\n\n## 你的审查重点\n\n请严格评估以下方面：\n\n1. **新颖性评估**：\n   - \"Generation depth classification\" 作为 task formulation 的新颖性有多大？是否只是把 binary detection 分得更细？\n   - DDR（differential depth response）是一个 genuine insight 还是一个 trivial observation（递归生成当然会让 entropy 下降）？\n   - 7-feature ensemble 方法本身是否有技术新颖性？还是只是 feature engineering + XGBoost？\n   - 相比 Broken Telephone 和 Markovian Chains 两篇 concurrent work，本文的增量贡献是否足够？\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作？特别是：\n     - 多轮 LLM 生成的质量衰减研究\n     - Model collapse / self-consuming models 方向的最新进展\n     - 数据污染检测方法\n     - Ordinal classification 文献\n   - 与 concurrent works（Broken Telephone, Markovian Chains）的比较是否公平充分？\n   - 引用数量和覆盖度是否达到 EMNLP 水准？\n\n3. **论文完整性**：\n   - Abstract/Introduction 的 claims 是否都有实验支撑？\n   - 各章节逻辑是否连贯（story line 是否统一）？\n   - Contribution 列表是否准确反映实际贡献（有无 overclaim/underclaim）？\n   - Downstream utility（Contribution 3）的 narrative 定位是否合理——\"detectability does not entail downstream degradation\" 这个 claim 是否 well-motivated？\n   - Limitations 是否充分坦诚？\n\n4. **格式与写作**：\n   - 是否符合 ACL style 格式要求？\n   - 正文是否在 8 页内？\n   - 写作质量（AI 痕迹、dash 使用、-ing phrases、过度分段）\n   - 图表信息密度和清晰度\n   - 引用格式是否统一？\n\n请给出完整审稿意见，包含 Strengths、Weaknesses（逐条编号）、Questions、Minor Issues。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你负责**新颖性 + 完整性 + Related Work + 格式**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references）\n- **模板**: ACL official style files（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录**: 允许，参与审稿\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## 论文概要\n\"Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\"——提出 generation depth classification（gen-0/gen-1/gen-2+），利用 differential depth response（DDR）中 drifting vs stationary features 的互补性，用 7-feature XGBoost ensemble 在 8 个 base model generator 上实现 3-class LOGO F1=0.762。\n\n## 你的审查重点\n\n请严格评估以下方面：\n\n1. **新颖性评估**：\n   - \"Generation depth classification\" 作为 task formulation 的新颖性有多大？是否只是把 binary detection 分得更细？\n   - DDR（differential depth response）是一个 genuine insight 还是一个 trivial observation（递归生成当然会让 entropy 下降）？\n   - 7-feature ensemble 方法本身是否有技术新颖性？还是只是 feature engineering + XGBoost？\n   - 相比 Broken Telephone 和 Markovian Chains 两篇 concurrent work，本文的增量贡献是否足够？\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作？特别是：\n     - 多轮 LLM 生成的质量衰减研究\n     - Model collapse / self-consuming models 方向的最新进展\n     - 数据污染检测方法\n     - Ordinal classification 文献\n   - 与 concurrent works（Broken Telephone, Markovian Chains）的比较是否公平充分？\n   - 引用数量和覆盖度是否达到 EMNLP 水准？\n\n3. **论文完整性**：\n   - Abstract/Introduction 的 claims 是否都有实验支撑？\n   - 各章节逻辑是否连贯（story line 是否统一）？\n   - Contribution 列表是否准确反映实际贡献（有无 overclaim/underclaim）？\n   - Downstream utility（Contribution 3）的 narrative 定位是否合理——\"detectability does not entail downstream degradation\" 这个 claim 是否 well-motivated？\n   - Limitations 是否充分坦诚？\n\n4. **格式与写作**：\n   - 是否符合 ACL style 格式要求？\n   - 正文是否在 8 页内？\n   - 写作质量（AI 痕迹、dash 使用、-ing phrases、过度分段）\n   - 图表信息密度和清晰度\n   - 引用格式是否统一？\n\n请给出完整审稿意见，包含 Strengths、Weaknesses（逐条编号）、Questions、Minor Issues。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-17T17:19:08.223734+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 556 · 2026-05-17T17:19:13.283889+00:00_

Round 1 已分配给两位 Reviewer：
- **Reviewer 1** → 方法严谨性 + 实验设计 + 统计 claims
- **Reviewer 2** → 新颖性 + 完整性 + Related Work + 格式

等待两位 Reviewer 返回独立审稿意见后，进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 557 · 2026-05-17T17:23:19.657066+00:00_

[Reviewer 1 审稿意见]:

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)

**一句话总结**: 任务定义新颖、DDR 现象有趣且实验覆盖面广，但核心 claims 在统计解读上存在过度包装，且方法仅适用于 base model + 标准解码这一狭窄场景，实用价值受限。

---

## 官方维度打分（ACL ARR Review Form 2025）

| 维度 | 分数 | 理由摘��� |
|------|------|----------|
| Soundness | 3/5 | 核心实验设计基本合理，但 gen-0 seed sharing 引入系统偏差未充分解决；TOST 等价性测试解读有误导性；cross-model 评估用 5-gen 子集与主实验 8-gen 不一致 |
| Excitement | 3.5/5 | Generation depth classification 是一个有意义的新任务；DDR 分解（drifting vs stationary）是有洞察力的发现；但 base-model-only 限制大幅降低实际影响力 |
| Reproducibility | 4/5 | 实验细节充分（模型、超参数、decoding 参数、软件版本均报告），承诺代码开源；数据集构建流程清晰可复现 |
| Confidence | 4/5 | 仔细阅读了全文及所有附录，对统计方法和实验设计有充分把握 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] TOST 等价性测试解读具有误导性

- 具体位置：§4.4, Appendix §Downstream Utility, Abstract (第8行), Contribution #3
- 问题：论文声称 "depth-aware data selection yields training utility equivalent to random subsampling"（Abstract），但 Table 8 显示 random subsampling 实际 *优于* depth-aware curation（ppl 2.367 vs 2.387）。TOST 在 ±2% margin 下通过仅说明差异小于 2%，不等于两者"等价"——当一方一致性地更优时，"equivalence" 的 framing 会误导读者。更严重的是，TOST 仅用 n=3 seeds，pooled std < 0.001，导致 Cohen's d = 86-120（论文自己承认 "artificially inflating d"）。这意味着 TOST 的统计功效来自极低的方差而非真正的等价性证据。±2% margin 的选择也未从领域知识论证其合理性（为什么不是 ±1% 或 ±0.5%？Table 9 显示 ±1% 时等价性不成立）。
- 为什么影响接收：Contribution #3 的核心 claim 建立在这个统计推断上；如果 TOST 的解读被撤回，论文的三大贡献缩减为两个，且 downstream utility 部分变成一个 null result（depth-aware curation 没有任何优势）。
- 建议修改方向：(1) 将 claim 改为 "depth composition does not substantially degrade training utility" 而非 "equivalent"；(2) 明确报告 random 一致性优于 depth-aware 的事实；(3) 论证 ±2% margin 的合理性或改为报告最小等价 margin（Table 9 的 sensitivity analysis 应在正文而非仅附录中讨论）；(4) 承认 n=3 seeds 的 TOST 功效不足以支撑强等价性结论。

**N2** [critical] Gen-0 seed sharing 导致 3-class LOGO F1 系统性高估

- 具体位置：§3.2 (第27-29行), §4.1, Table 1, Appendix §Confusion Matrix
- 问题：所有 8 个 generator 共享相同的 ~1000 Wikipedia seeds 作为 gen-0。在 LOGO 中，held-out generator 的 gen-0 样本在训练集中出现（作为其他 generator 的 gen-0），构成直接的 train-test overlap。论文自己承认 "3-class metric may carry upward bias from memorized gen-0 patterns"。混淆矩阵证实 gen-0 recall = 99.4%，远高于 gen-1 (75%) 和 gen-2+ (73.7%)。论文提供了 binary metric (gen-1 vs gen-2+) 作为 "leak-free" 替代，但仍然以 3-class F1 = 0.762 作为 headline number（出现在 Abstract、Introduction、Conclusion 中），且 cross-model 评估 F1=0.809 同样包含 gen-0。
- 为什么影响接收：核心性能数字不可信。如果真正的 gen-0 泛化性能接近 gen-1 水平（~75% recall），3-class macro F1 会显著低于 0.762。审稿人无法判断 DDR 方法对从未见过的 gen-0 文本的泛化能力。
- 建议修改方向：(1) 正文的 primary metric 应改为 leak-free binary F1 = 0.694；(2) 或者将 gen-0 seeds 按 generator 分离（每个 generator 用不同的 seed subset），消除 overlap；(3) 如果保留 3-class 数字，应在 Abstract 中明确标注其上界性质。

**N3** [critical] 方法仅适用于 base model 且 temperature 鲁棒性不足，实用价值存疑

- 具体位置：§1 (第13行), §5 (Discussion), Limitations §
- 问题：论文限制于 base (pretrained) model 是一个"deliberate design choice"，但现实中 web 文本绝大多数来自 instruction-tuned/RLHF-aligned 模型。Instruct 模型 F1 从 0.763 暴降至 0.338 (OLMo) 和 0.667 (Qwen3 chat)。此外，cross-temperature transfer 显示在 t=0.7→t=1.0 时单个 generator 降至 F1=0.418。实际部署中 temperature 未知。这两个限制叠加意味着该方法在真实场景中几乎无法使用。
- 为什么影响接收：EMNLP 审稿人通常期待方法的实际应用前景。如果一个 detection 方法仅在实验室条件下工作（已知 base model、已知 temperature、已知 prompt type），其贡献更接近一个 empirical observation 而非一个 practical tool。论文的 framing 需要更明确地定位为 "phenomenon characterization" 而非 "detection method"。
- 建议修改方向：(1) 将论文 framing 从 "detection/classification system" 转向 "characterizing a fundamental property of recursive generation"；(2) 在 Abstract/Introduction 中前置这些限制条件，避免读者误解为通用检测方案；(3) 或者增加 mixed-temperature training 实验证明可以缓解 temperature 问题。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cross-model 评估与主实验 generator 集合不一致

- 具体位置：§4.1 脚注 (第13行), Table 1 vs cross-model results
- 问题：Cross-model chains 使用原始 5-generator subset (Pythia, OLMo, Qwen)，而主实验 LOGO 用 8 个 generator（加入 Llama-3.2-3B 和 Mistral-7B-v0.3）。Mistral-7B 的 LOGO binary F1 最低 (0.633)，比均值低 6pp。如果将 Mistral 和 Llama 加入 cross-model chains，F1=0.809 可能显著下降。论文以脚注形式轻描淡写这个不一致，但这使得主文中最高的 F1 数字（0.809）和 LOGO 结果无法直接比较。
- 建议：在 8-gen 集合上重跑 cross-model 评估，或将 5-gen cross-model 结果明确降格为 "pilot study"。

**W2** [warning] Spearman correlation 阈值缺乏标准引用

- 具体位置：§3.3 (第69行), §4.2, Introduction Contribution #2
- 问题：论文将 |ρ|>0.60 称为 "substantial monotonic drift"，|ρ|<0.10 称为 "near-stationary"。这些阈值未引用标准参考。Cohen (1988) 的 benchmarks (0.10/0.30/0.50 for small/medium/large) 是针对 Pearson r 的，且学术界对这些固定阈值有广泛批评。论文将这些阈值作为 DDR 定义的核心部分（Contribution #2 直接使用），需要更强的支撑。
- 建议：(1) 引用 Hinkle et al. (2003) 或 Akoglu (2018) 的 correlation interpretation guidelines；(2) 或者不依赖固定阈值，改为强调 drifting vs stationary 之间的 10× magnitude gap（这更有说服力）。

**W3** [warning] "Competitive performance" claim 与数据不完全吻合

- 具体位置：§4.3, Table 3, Abstract (第7行)
- 问题：Abstract 称 "competitive performance at substantially lower computational cost"。Table 3 显示 7-feature 3-class F1=0.774 vs 4-detector ensemble 0.785 (差 1.1pp) 和 4-det+surface 0.795 (差 2.1pp)。Binary F1 差距更小 (0.705 vs 0.708)。虽然 cost-performance tradeoff 论述合理（2.4× 推理时间），但 "competitive" 一词对 3-class 任务是可争议的——multi-detector ensembles 在同一评估协议下持续优于 7-feature。
- 建议：将 Abstract 的 claim 改为 "achieves comparable binary performance and moderately lower 3-class performance at 2.4× lower computational cost"，或只强调 binary F1 的 competitive 性。

**W4** [warning] Pythia-410M 作为 reference model 的公平性

- 具体位置：§3.3 (第47-48行), Table 4, Table 1
- 问题：Pythia-410M 与 Pythia-1B/2.8B 共享 GPT-NeoX 架构。虽然论文通过 cross-reference 实验（spread 0.013）论证 reference model 不影响结果，但这个实验只在 5-gen subset 上做。在 8-gen LOGO 中，Pythia generators 恰好达到最高 F1 (0.718-0.724)，而使用不同架构的 generators (Mistral, Llama) F1 较低。这可能反映 reference model familiarity 的残余效应，而非纯粹的 scale effect。
- 建议：在 8-gen 设置下验证 cross-reference robustness（当前 Table 4 仅报告 5-gen），或明确讨论 architecture overlap 与 per-generator F1 ranking 之间可能的混淆。

**W5** [warning] XGBoost 超参数固定可能偏向多特征方法

- 具体位置：§3.4 (第81行)
- 问题：所有方法使用 n_estimators=200, max_depth=6, lr=0.1。对于单特征 baseline（如 Avg-LogProb），200 棵深度为 6 的树可能过拟合一个一维输入；相反，7 个特征更能利用这个容量。论文的 classifier ablation (Appendix §Classifier) 证明信号在特征层面，但 XGBoost 配置对单特征方法可能不是最优的。
- 建议：为单特征 baseline 报告 tuned hyperparameter 的结果（至少 grid search max_depth 和 n_estimators），或用更简单的分类器（如 threshold-based）评估单特征方法。

---

## 小问题（不影响接收）

- Table 1 caption 较长且包含方法学解释，建议精简
- §4.1 "binary F1=0.694, CI [0.688, 0.700]" 的 CI 极窄（宽度 0.012），这在 N=37K 下是合理的，但应确认 bootstrap 是否在 LOGO fold 层面做的（否则会低估不确定性）
- entropy_min 保留 "for completeness" 的理由薄弱（Appendix LOFO 显示 Δ=+0.01pp，即删除略好），建议改为 "removing does not statistically improve performance" 而非 "retained for completeness"
- Bonferroni correction 的具体应用场景未列明——在哪些 pairwise comparisons 上做了 correction？涉及多少 comparisons？
- Figure 3 (fig3_baseline_comparison.png) 文件格式为 PNG 而非 PDF（见 results.tex 第110行），可能在打印时质量不足
- Cross-domain 实验使用 t=1.0 而主实验用 t=0.7，直接比较跨域数字与主实验数字时存在混淆

---

## 主要优势

1. **任务定义的新颖性**：Generation depth classification (gen-0/gen-1/gen-2+) 是一个有意义的新任务，超越了 binary detection，填补了文献空白。与 concurrent works (broken_telephone, markovian_chains) 的独立收敛增强了该方向的重要性。

2. **DDR 的科学洞察**：Differential Depth Response 的 drifting vs stationary 分解是一个优雅的发现，提供了对 recursive generation 机制的可解释理解。Location shift + shape preservation 的假说有理论吸引力且有实验支撑。

3. **实验覆盖面极广**：LOGO/LOFO/cross-model/cross-reference/cross-temperature/cross-domain/cross-prompt/perturbation robustness/length confound/classifier ablation/feature ablation/finer granularity/downstream utility——几乎涵盖了所有可能的审稿人质疑方向。

4. **自我批评的诚实度**：论文主动报告 gen-0 seed sharing 问题、t=1.0 退化、instruct model 失败等不利结果，Limitations section 全面且坦诚。

5. **计算效率优势**：单个 410M reference model (905MB) vs multi-detector ensemble 需 2 个模型 (2868MB)，2.4× 推理加速，在 binary F1 上几乎无损。

---

## Questions for Authors

Q1: LOGO 中 gen-0 seed sharing 导致的上界效应有多大？能否报告一个 gen-0 hold-out 实验（为 held-out generator 分配独立的 seeds）以量化真正的 gen-0 泛化能力？

Q2: TOST 的 ±2% margin 基于什么领域先验选择？在 NLP fine-tuning 中，0.02 ppl 差异（约 0.8% relative）是否真正"无意义"？

Q3: Cross-reference 实验（Table 4）仅在 5-gen subset 上报告。在 8-gen 设置下（特别是 Mistral-7B 和 Llama-3.2-3B）使用非 Pythia reference model 时，LOGO F1 是否变化？

Q4: 如果将 cross-model chains 扩展到 8 个 generator（包括 Mistral-7B），F1=0.809 是否仍然成立？

Q5: entropy_min 删除后性能微升 (+0.01pp)，保留它的真正科学理由是什么？如果是为了 NLL 分布的完整描述，为什么不包括其他统计量（如 skewness, kurtosis）？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 558 · 2026-05-17T17:23:27.384447+00:00_

Reviewer 1 已返回审稿意见（Overall: 3.5, Borderline Conference）。等待 Reviewer 2 完成审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 53

## Round 53

2 recorded events


### User

_source line 559 · 2026-05-17T17:23:29.962723+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **3.5/5 (Borderline Conference)** 的评分。三个 Must-Fix 问题分别是：(1) TOST 等价性测试的统计解读有误导性，n=3 seeds 不足以支撑强等价性结论；(2) Gen-0 seed sharing 导致 3-class headline number 系统性高估；(3) 方法仅适用于 base model + 标准 temperature 的狭窄场景，需要重新定位 framing。论文的核心优势在于任务新颖性、DDR 现象的科学洞察、以及异常全面的实验覆盖和诚实的自我批评。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 560 · 2026-05-17T17:23:37.406838+00:00_

Reviewer 1 已完成初审（3.5/5, Borderline Conference）。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 54

## Round 54

6 recorded events


### User

_source line 561 · 2026-05-17T17:26:18.888568+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains"
**审查侧重**: 新颖性 + 完整性 + Related Work + 格式

---

## 总体评分
**Overall**: 3 (Findings)
**一句话总结**: 扎实的实证工作，DDR 是一个有趣的经验性发现，但任务定义是 binary detection 的自然延伸而非范式突破，方法为标准 feature engineering + XGBoost，加之两篇 concurrent work 覆盖类似领域且 base-model-only 限制削弱实用性，整体贡献更适合 Findings 而非主会议。

## 官方维度打分（来自 ACL ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 核心 claim 有充分实验支撑（bootstrap CI、McNemar、TOST），统计方法论规范；但 downstream utility 实验仅 3 seeds/单模型，DDR "shape preservation" 表述与 Levene test 结果存在张力 |
| Excitement | 3/5 (Interesting) | DDR 的 drifting vs. stationary 分解是 nice observation，但 method 无算法创新，practical applicability 受限于 base models + 温度敏感性，concurrent works 覆盖相近 territory |
| Overall Assessment | 3 (Findings) | 适合 Findings 接收：贡献真实但增量有限，实用价值待验证 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Contribution 3（downstream utility）本质上是一个 null result，作为独立贡献过度包装

- 具体位置：Abstract L7-8, §4.4, §1 Contribution (3), Appendix K
- 问题：论文将"depth-aware data curation 与 random subsampling 等效（TOST ±2%, p < 0.001）"作为三大贡献之一。然而这本质上是一个 negative finding：检测到的 distributional shift 对 downstream training 没有实际影响。这意味着论文提出的 depth fingerprinting 的最直接应用场景（data curation）不成立。
  - 实验规模极小：仅 OLMo-2-0425-1B 一个模型，n=3,951 样本，3 seeds
  - Cohen's d 高达 86.0-119.7，论文自己承认这是 unreliable 的（Appendix K: "inflated effect sizes reflect low seed-level variance"）
  - 仅测 perplexity 一个下游指标，未测任何 downstream task（QA、summarization 等）
  - Abstract 的措辞 "confirming that the detected distributional shift does not translate to downstream perplexity degradation" 暗示这是一个有价值的发现，但实际上它削弱了整篇论文的实用动机
- 为什么影响接收：如果 depth 信号对 data curation 无用，论文需要更清晰地论证 depth classification 的实际应用场景。当前 framing 将 null result 包装为贡献，审稿人会质疑 practical impact。
- 建议修改方向：(a) 降级为 analysis finding 而非 main contribution；(b) 增加更多 downstream tasks 或至少坦诚讨论为何仅用 perplexity；(c) 在 Introduction/Discussion 中补充其他 practical use cases（如 provenance tracking、content moderation flagging）并给出具体场景论证。

**N2** [critical] 方法新颖性不足：7 个手工特征 + XGBoost 本质是标准 feature engineering

- 具体位置：§3.3, §3.4, Table 3 (ablation), Appendix E (LOFO)
- 问题：方法层面无算法创新。7 个特征中 5 个是 NLL 统计量（mean, std, max, min, tail slope），2 个是经典 stylometric measures（TTR, hapax ratio）。分类器是 off-the-shelf XGBoost。论文的贡献在于 DDR 这个 empirical observation，而非方法本身。
  - 论文自己在 Appendix D 承认 QLoRA fine-tuning 可达 F1=0.905 (vs. 7-feature 的 0.762 LOGO)，说明手工特征是 lossy summary
  - Appendix H 显示 CORAL/Frank-Hall 等 ordinal-specific methods "yield comparable performance"，说明 ordinal structure 也没有被有效利用
  - §2.1 的定位 "Our contribution is not a new detection method but the task formulation and the finding" 是诚实的，但这意味着方法章节的贡献接近零
- 为什么影响接收：EMNLP 主会议期望 methodological contribution 或 significant empirical insight。DDR observation 是 interesting 但 feature engineering pipeline 的技术门槛低，容易被 neural approaches 替代（论文自己的 QLoRA 实验已经证明这一点）。
- 建议修改方向：要么 (a) 将论文重新定位为 analysis paper（focus on DDR phenomenon 本身），弱化 method 贡献、强化对 DDR 的理论理解；要么 (b) 将 QLoRA 结果提升到主文，展示 end-to-end approach 也能 exploit DDR structure。

**N3** [critical] Instruction-tuned model 极弱表现严重削弱实用性

- 具体位置：§6 (Discussion L18), §Limitations L1-9
- 问题：OLMo-Instruct LOGO F1=0.338（接近 3-class random baseline 0.33），Qwen3-0.6B with chat template F1=0.667，length-matched 后 correlation 接近零。现实世界 LLM 生成文本几乎全部来自 instruction-tuned models。论文将此定位为 "deliberate design choice" 来隔离现象，但这意味着整个 framework 在实际部署场景中不可用。
- 为什么影响接收：审稿人会质疑：如果方法对实际场景（instruction-tuned models）不 work，仅在 base models 上验证 DDR 的科学价值是否足以支撑一篇完整论文？
- 建议修改方向：(a) 更深入分析 WHY instruction tuning destroys depth signal（length regulation? format constraints? RLHF shaping? 哪个因素主导？）；(b) 探索是否有 feature subset 在 instruct models 上保持 discriminative；(c) 在 Introduction 中更坦诚地定位为 "controlled study of the base model phenomenon" 而非暗示可部署。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] DDR "shape preservation" 表述与统计检验结果存在矛盾

- 具体位置：§4.2 paragraph "Distributional shift quantification" (L66-70)
- 问题：论文声称 recursive generation "preserving distributional shape"（Abstract L6, §1 L12, §4.2），但 Levene tests 对所有七个特征都拒绝了 equal variance 假设（p < 10^{-10}），包括 shape features。论文用 "coefficient of variation shift < 3% for entropy max vs. > 15% for hapax ratio" 来辩护 shape features 是 "approximately stationary"，但 "approximately" 的量化标准不清楚。
  - KS statistics 也显示 shape features 虽然小（0.043-0.052）但 statistically significant after Bonferroni
  - 更准确的表述应该是 "shape features drift much less than location features" 而非 "preserving shape"
- 建议：将 "preserving distributional shape" 改为 "approximately preserving shape" 或 "exhibiting substantially smaller drift in shape features"，并在 Discussion 中讨论这个 nuance。

**W2** [warning] Gen-0 seed sharing 导致 3-class LOGO metric 存在 upward bias，但 Abstract 中 3-class 数字排在 binary 之前

- 具体位置：Abstract L7, Table 1 caption, §4.1 L1-8
- 问题：论文正确识别了 gen-0 seed 在所有 generators 间共享导致 LOGO 评估中 gen-0 class 存在 train-test overlap，并报告了 leak-free binary metric。但 Abstract 的措辞 "binary F1=0.764 on heterogeneous cross-model chains and 0.694 under LOGO...3-class macro F1=0.809 and 0.762" 中 3-class 数字出现多次且排位靠前，给读者的第一印象是 headline number，而这个数字是 biased 的。
- 建议：Abstract 中将 binary LOGO F1 (0.694) 作为 primary metric 前置，3-class 数字作为辅助参考并加注 caveat。

**W3** [warning] Temperature sensitivity 比论文暗示的更严重

- 具体位置：§4.2 "Temperature robustness" paragraph, §6 (Discussion L13), Appendix P
- 问题：论文称 "operates reliably within t∈[0.5, 0.9]"，但：
  - t=1.0 时 entropy mean 相关性从 ρ=-0.60 骤降至 ρ=-0.002（本质上归零）
  - Cross-temperature transfer 更差：Qwen3-1.7B 从 0.789 降至 0.418（§6 L13）
  - 大量 real-world API 使用 t=1.0 甚至更高（如 creative writing、brainstorming）
  - "Standard decoding regimes" 的定义范围不够清晰
- 在 Limitations 中有提及，但 §4.2 的 "Temperature robustness" 段落标题给人一种鲁棒性良好的印象，实际上 t=1.0 是一个 hard failure mode。
- 建议：将 §4.2 该段标题改为 "Temperature sensitivity" 并在主文中更显著地讨论 t=1.0 failure。

**W4** [warning] Ordinal classification 文献引用和讨论不足

- 具体位置：§2.1 (L13), §3.4 "Classifier" paragraph
- 问题：论文将任务 framed 为 ordinal classification（§3.1: "We frame depth estimation as an ordinal classification task"），引用了 ordinal regression survey（Gutierrez et al.）和 CORAL，但：
  - 主文未讨论为何 ordinal structure 没有带来性能提升（CORAL "comparable performance" 仅在 Appendix H 一句话带过）
  - 缺少 ordinal classification 的其他重要方法（如 proportional odds model, ordinal SVM, unimodal regularization 等）
  - 如果 ordinal structure 不 help，这本身是一个值得讨论的 finding（可能说明 3-class 间距不均匀，或者 XGBoost 已经隐式地 captures ordinal structure）
- 建议：在主文中讨论 ordinal methods 为何未能改善性能，或者承认 ordinal framing 更多是概念性的而非方法性的。

**W5** [warning] 与 concurrent works 的实验性对比缺失

- 具体位置：§2.2, Table 4
- 问题：论文在 Related Work 中对 Broken Telephone 和 Markovian Chains 做了概念性区分（chain type, feature type, goal），但没有任何直接实验对比。例如：
  - 在 paraphrastic chains 上对比本文方法与 Broken Telephone 的 findings
  - 用 Markovian Chains 的 perplexity-based tracking 做 depth prediction baseline
  - 虽然 concurrent works 可能没有公开代码，但至少可以在 paraphrastic setting 下比较（论文 Appendix C 已有 paraphrastic chain 实验）
- 建议：如果时间允许，补充一个 paraphrastic chain comparison；否则至少讨论为何直接对比不可行。

---

## 小问题（不影响接收）

- §3.3 entropy_min 的 justification "we retain it for completeness of the NLL summary statistics (mean, std, max, min)" 不是一个好理由。如果它不贡献，要么 drop 它（变成 6-feature ensemble），要么提供更好的理由保留。
- Table 1 中 Pythia-1B 的 3-class F1 (0.806) 高于 Pythia-2.8B (0.798)，但 binary F1 排序相反（0.718 vs. 0.724）。这个交叉没有讨论。
- §3.2: "theoretical yield is 8 × ~1,000 × 5 ≈ 40,000 texts" — 8 generators × 1,000 seeds × 5 depths = 40,000 没错，但实际产出 37,058（7.4% attrition）。Generation failure 的具体原因和分布未报告。
- References 中部分 bib 条目缺少 pages/volume 信息（如 stamatatos_survey, koppel_authorship）。
- Figure 3 (baseline comparison) 图中标签较小，打印后可能难以辨认。
- §3.3 footnote 1: "We use 'entropy' as shorthand for token-level negative log-likelihood" — 这个 terminology abuse 可能困扰某些读者，建议在 §3.3 段落开头就说明，而不是用脚注。

---

## 主要优势

1. **实验设计严谨**：8 个 generator, 5 个 family, LOGO/LOFO 交叉验证, bootstrap CI, McNemar tests, Bonferroni correction, TOST equivalence testing — 统计方法论远超 average EMNLP 论文水准。
2. **DDR 分解是有价值的经验性发现**：drifting vs. stationary features 的区分提供了对 recursive generation dynamics 的结构化理解，这比单纯报告分类准确率更有 insight。
3. **诚实的 Limitations section**：覆盖 instruction tuning, scale, prompt type, temperature, domain, language，长度和深度都超出平均水平。
4. **Gen-0 leakage 的自我诊断和 mitigation**：主动识别 seed sharing 问题并报告 leak-free binary metric，这是良好的实验实践。
5. **Appendix 极为详尽**：15 个附录覆盖了 reviewer 可能提出的绝大多数 follow-up questions。
6. **写作质量高**：无明显 AI 写作痕迹（无 em-dash、无过度分段、无 -ing phrase 堆砌），语言简洁精确。
7. **格式合规**：ACL style with [review] option, 正文 8 页, anonymous, line numbers enabled, 无格式违规。

---

## 总结判断

这是一篇**扎实但增量有限**的实证论文。DDR 是一个 genuine empirical finding，实验设计和统计方法论严谨。主要问题在于：(1) 方法层面无创新（feature engineering + XGBoost），(2) 两篇 concurrent works 覆盖相似领域降低了 novelty premium，(3) base-model-only + temperature sensitivity 限制了 practical impact，(4) downstream utility 本质是 null result。建议以 Findings 接收，或者在 revision 中显著加强对 DDR phenomenon 本身的理论理解以提升到 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-17T17:26:50.038778+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和主要论点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**Overall**: 3 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] Contribution 3（downstream utility）本质上是一个 null result，作为独立贡献过度包装\n\n- 具体位置：Abstract L7-8, §4.4, §1 Contribution (3), Appendix K\n- 问题：论文将\"depth-aware data curation 与 random subsampling 等效（TOST ±2%, p < 0.001）\"作为三大贡献之一。然而这本质上是一个 negative finding：检测到的 distributional shift 对 downstream training 没有实际影响。这意味着论文提出的 depth fingerprinting 的最直接应用场景（data curation）不成立。\n  - 实验规模极小：仅 OLMo-2-0425-1B 一个模型，n=3,951 样本，3 seeds\n  - Cohen's d 高达 86.0-119.7，论文自己承认这是 unreliable 的\n  - 仅测 perplexity 一个下游指标，未测任何 downstream task\n  - Abstract 的措辞暗示这是一个有价值的发现，但实际上它削弱了整篇论文的实用动机\n- 建议：(a) 降级为 analysis finding 而非 main contribution；(b) 增加更多 downstream tasks 或坦诚讨论为何仅用 perplexity；(c) 补充其他 practical use cases。\n\n**N2** [critical] 方法新颖性不足：7 个手工特征 + XGBoost 本质是标准 feature engineering\n\n- 具体位置：§3.3, §3.4, Table 3 (ablation), Appendix E (LOFO)\n- 问题：方法层面无算法创新。7 个特征中 5 个是 NLL 统计量，2 个是经典 stylometric measures。分类器是 off-the-shelf XGBoost。论文的贡献在于 DDR 这个 empirical observation，而非方法本身。\n  - QLoRA fine-tuning 可达 F1=0.905 vs 7-feature 的 0.762 LOGO\n  - CORAL/Frank-Hall 等 ordinal methods \"yield comparable performance\"\n  - §2.1 承认 \"Our contribution is not a new detection method but the task formulation and the finding\"\n- 建议：(a) 重新定位为 analysis paper，弱化 method 贡献、强化 DDR 理论理解；或 (b) 将 QLoRA 提升到主文。\n\n**N3** [critical] Instruction-tuned model 极弱表现严重削弱实用性\n\n- 具体位置：§6 (Discussion L18), §Limitations L1-9\n- 问题：OLMo-Instruct LOGO F1=0.338（接近 random），现实世界文本几乎全部来自 instruction-tuned models。\n- 建议：(a) 更深入分析 WHY instruction tuning destroys depth signal；(b) 探索 feature subset 在 instruct models 上是否保持 discriminative；(c) 更坦诚地定位。\n\n### Should-Fix 问题\n\n**W1** [warning] DDR \"shape preservation\" 表述与 Levene test 结果矛盾\n- Levene tests 对所有七个特征（含 shape features）都拒绝了 equal variance。更准确应说 \"shape features drift much less\" 而非 \"preserving shape\"。\n\n**W2** [warning] Abstract 中 3-class 数字排在 binary 之前，但 3-class 存在 upward bias\n- 建议将 binary LOGO F1 (0.694) 前置为 primary metric。\n\n**W3** [warning] Temperature sensitivity 比论文暗示的更严重\n- t=1.0 时 entropy mean 相关性从 ρ=-0.60 骤降至 ρ=-0.002；cross-temp transfer Qwen 从 0.789 降至 0.418。\"Temperature robustness\" 段落标题给人错误印象。\n\n**W4** [warning] Ordinal classification 文献引用和讨论不足\n- 主文未讨论为何 ordinal structure 没有带来性能提升。\n\n**W5** [warning] 与 concurrent works 的实验性对比缺失\n- 没有与 Broken Telephone / Markovian Chains 的直接实验对比。\n\n### 主要优势\n1. 实验设计严谨（8 generator, LOGO/LOFO, bootstrap CI, McNemar, Bonferroni, TOST）\n2. DDR 分解是有价值的经验性发现\n3. 诚实的 Limitations section\n4. Gen-0 leakage 自我诊断\n5. Appendix 极为详尽\n6. 写作质量高，无 AI 痕迹\n7. 格式合规",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和主要论点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**Overall**: 3 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] Contribution 3（downstream utility）本质上是一个 null result，作为独立贡献过度包装\n\n- 具体位置：Abstract L7-8, §4.4, §1 Contribution (3), Appendix K\n- 问题：论文将\"depth-aware data curation 与 random subsampling 等效（TOST ±2%, p < 0.001）\"作为三大贡献之一。然而这本质上是一个 negative finding：检测到的 distributional shift 对 downstream training 没有实际影响。这意味着论文提出的 depth fingerprinting 的最直接应用场景（data curation）不成立。\n  - 实验规模极小：仅 OLMo-2-0425-1B 一个模型，n=3,951 样本，3 seeds\n  - Cohen's d 高达 86.0-119.7，论文自己承认这是 unreliable 的\n  - 仅测 perplexity 一个下游指标，未测任何 downstream task\n  - Abstract 的措辞暗示这是一个有价值的发现，但实际上它削弱了整篇论文的实用动机\n- 建议：(a) 降级为 analysis finding 而非 main contribution；(b) 增加更多 downstream tasks 或坦诚讨论为何仅用 perplexity；(c) 补充其他 practical use cases。\n\n**N2** [critical] 方法新颖性不足：7 个手工特征 + XGBoost 本质是标准 feature engineering\n\n- 具体位置：§3.3, §3.4, Table 3 (ablation), Appendix E (LOFO)\n- 问题：方法层面无算法创新。7 个特征中 5 个是 NLL 统计量，2 个是经典 stylometric measures。分类器是 off-the-shelf XGBoost。论文的贡献在于 DDR 这个 empirical observation，而非方法本身。\n  - QLoRA fine-tuning 可达 F1=0.905 vs 7-feature 的 0.762 LOGO\n  - CORAL/Frank-Hall 等 ordinal methods \"yield comparable performance\"\n  - §2.1 承认 \"Our contribution is not a new detection method but the task formulation and the finding\"\n- 建议：(a) 重新定位为 analysis paper，弱化 method 贡献、强化 DDR 理论理解；或 (b) 将 QLoRA 提升到主文。\n\n**N3** [critical] Instruction-tuned model 极弱表现严重削弱实用性\n\n- 具体位置：§6 (Discussion L18), §Limitations L1-9\n- 问题：OLMo-Instruct LOGO F1=0.338（接近 random），现实世界文本几乎全部来自 instruction-tuned models。\n- 建议：(a) 更深入分析 WHY instruction tuning destroys depth signal；(b) 探索 feature subset 在 instruct models 上是否保持 discriminative；(c) 更坦诚地定位。\n\n### Should-Fix 问题\n\n**W1** [warning] DDR \"shape preservation\" 表述与 Levene test 结果矛盾\n- Levene tests 对所有七个特征（含 shape features）都拒绝了 equal variance。更准确应说 \"shape features drift much less\" 而非 \"preserving shape\"。\n\n**W2** [warning] Abstract 中 3-class 数字排在 binary 之前，但 3-class 存在 upward bias\n- 建议将 binary LOGO F1 (0.694) 前置为 primary metric。\n\n**W3** [warning] Temperature sensitivity 比论文暗示的更严重\n- t=1.0 时 entropy mean 相关性从 ρ=-0.60 骤降至 ρ=-0.002；cross-temp transfer Qwen 从 0.789 降至 0.418。\"Temperature robustness\" 段落标题给人错误印象。\n\n**W4** [warning] Ordinal classification 文献引用和讨论不足\n- 主文未讨论为何 ordinal structure 没有带来性能提升。\n\n**W5** [warning] 与 concurrent works 的实验性对比缺失\n- 没有与 Broken Telephone / Markovian Chains 的直接实验对比。\n\n### 主要优势\n1. 实验设计严谨（8 generator, LOGO/LOFO, bootstrap CI, McNemar, Bonferroni, TOST）\n2. DDR 分解是有价值的经验性发现\n3. 诚实的 Limitations section\n4. Gen-0 leakage 自我诊断\n5. Appendix 极为详尽\n6. 写作质量高，无 AI 痕迹\n7. 格式合规",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-17T17:27:23.714479+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33675
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-17T17:27:23.938846+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和主要论点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] TOST 等价性测试解读具有误导性\n\n- Abstract 声称 \"depth-aware data selection yields training utility equivalent to random subsampling\"，但 Table 8 显示 random 实际优于 depth-aware（ppl 2.367 vs 2.387）。TOST 在 ±2% margin 下通过仅说明差异 <2%，不等于\"等价\"。\n- n=3 seeds，Cohen's d = 86-120（论文自己承认 \"artificially inflating d\"），TOST 功效来自极低方差而非真正等价。\n- ±2% margin 未从领域知识论证（Table 9 显示 ±1% 时不成立）。\n- 建议：(1) claim 改为 \"does not substantially degrade\" 而非 \"equivalent\"；(2) 明确报告 random 一致性优于 depth-aware；(3) 论证 ±2% margin 合理性；(4) 承认 n=3 功效不足。\n\n**N2** [critical] Gen-0 seed sharing 导致 3-class LOGO F1 系统性高估\n\n- 所有 8 个 generator 共享 ~1000 Wikipedia seeds 作为 gen-0。LOGO 中 held-out generator 的 gen-0 在训练集出现。\n- 混淆矩阵：gen-0 recall=99.4% vs gen-1 75% / gen-2+ 73.7%。\n- 论文仍以 3-class F1=0.762 作为 headline number（Abstract, Introduction, Conclusion），而非 leak-free binary F1=0.694。\n- 建议：(1) 正文 primary metric 改为 binary F1；(2) 或分离 gen-0 seeds per generator；(3) 如保留 3-class，标注上界性质。\n\n**N3** [critical] 方法仅适用于 base model + 标准 temperature，实用价值存疑\n\n- Instruct F1: OLMo 0.338, Qwen3 chat 0.667。\n- Cross-temperature: t=0.7→1.0 时 Qwen 从 0.789→0.418。\n- 两个限制叠加 = 真实场景无法使用。\n- 建议：(1) framing 从 \"detection system\" 转向 \"phenomenon characterization\"；(2) 前置限制条件；(3) 或增加 mixed-temperature training 实验。\n\n### Should-Fix 问题\n\n**W1** [warning] Cross-model 评估与主实验 generator 集合不一致\n- Cross-model chains 用 5-gen subset，主实验 LOGO 用 8-gen。Mistral LOGO binary F1 最低 (0.633)。F1=0.809 可能在 8-gen 下显著下降。\n\n**W2** [warning] Spearman correlation 阈值缺乏标准引用\n- |ρ|>0.60 为 \"substantial\"，<0.10 为 \"near-stationary\" 无标准参考。建议引用 Hinkle et al. 或强调 10× magnitude gap。\n\n**W3** [warning] \"Competitive performance\" claim 与数据不完全吻合\n- 7-feature 3-class F1=0.774 vs 4-det ensemble 0.785/4-det+surface 0.795。Multi-detector 在 3-class 上持续优于。\n\n**W4** [warning] Pythia-410M 与 Pythia generators 共享架构的公平性\n- Cross-reference 实验仅 5-gen subset。Pythia generators 恰好 F1 最高。\n\n**W5** [warning] XGBoost 超参数固定可能偏向多特征方法\n- 对单特征 baseline，200 棵 depth=6 的树可能过拟合。\n\n### 主要优势\n1. 任务定义新颖（gen depth classification 超越 binary detection）\n2. DDR 科学洞察优雅（drifting vs stationary 分解）\n3. 实验覆盖面极广（LOGO/LOFO/cross-model/cross-ref/cross-temp/cross-domain/cross-prompt/perturbation/length/classifier/feature ablation/finer granularity/downstream）\n4. 自我批评诚实\n5. 计算效率优势（单 410M model vs multi-detector 2.4× cost）\n\n### Questions for Authors\nQ1: 能否报告 gen-0 hold-out 实验量化真正的 gen-0 泛化？\nQ2: TOST ±2% margin 基于什么领域先验？\nQ3: 8-gen 设置下用非 Pythia reference model 时 LOGO F1 变化？\nQ4: Cross-model chains 扩展到 8 gen 后 F1=0.809 是否成立？\nQ5: entropy_min 保留的真正科学理由？",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和主要论点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] TOST 等价性测试解读具有误导性\n\n- Abstract 声称 \"depth-aware data selection yields training utility equivalent to random subsampling\"，但 Table 8 显示 random 实际优于 depth-aware（ppl 2.367 vs 2.387）。TOST 在 ±2% margin 下通过仅说明差异 <2%，不等于\"等价\"。\n- n=3 seeds，Cohen's d = 86-120（论文自己承认 \"artificially inflating d\"），TOST 功效来自极低方差而非真正等价。\n- ±2% margin 未从领域知识论证（Table 9 显示 ±1% 时不成立）。\n- 建议：(1) claim 改为 \"does not substantially degrade\" 而非 \"equivalent\"；(2) 明确报告 random 一致性优于 depth-aware；(3) 论证 ±2% margin 合理性；(4) 承认 n=3 功效不足。\n\n**N2** [critical] Gen-0 seed sharing 导致 3-class LOGO F1 系统性高估\n\n- 所有 8 个 generator 共享 ~1000 Wikipedia seeds 作为 gen-0。LOGO 中 held-out generator 的 gen-0 在训练集出现。\n- 混淆矩阵：gen-0 recall=99.4% vs gen-1 75% / gen-2+ 73.7%。\n- 论文仍以 3-class F1=0.762 作为 headline number（Abstract, Introduction, Conclusion），而非 leak-free binary F1=0.694。\n- 建议：(1) 正文 primary metric 改为 binary F1；(2) 或分离 gen-0 seeds per generator；(3) 如保留 3-class，标注上界性质。\n\n**N3** [critical] 方法仅适用于 base model + 标准 temperature，实用价值存疑\n\n- Instruct F1: OLMo 0.338, Qwen3 chat 0.667。\n- Cross-temperature: t=0.7→1.0 时 Qwen 从 0.789→0.418。\n- 两个限制叠加 = 真实场景无法使用。\n- 建议：(1) framing 从 \"detection system\" 转向 \"phenomenon characterization\"；(2) 前置限制条件；(3) 或增加 mixed-temperature training 实验。\n\n### Should-Fix 问题\n\n**W1** [warning] Cross-model 评估与主实验 generator 集合不一致\n- Cross-model chains 用 5-gen subset，主实验 LOGO 用 8-gen。Mistral LOGO binary F1 最低 (0.633)。F1=0.809 可能在 8-gen 下显著下降。\n\n**W2** [warning] Spearman correlation 阈值缺乏标准引用\n- |ρ|>0.60 为 \"substantial\"，<0.10 为 \"near-stationary\" 无标准参考。建议引用 Hinkle et al. 或强调 10× magnitude gap。\n\n**W3** [warning] \"Competitive performance\" claim 与数据不完全吻合\n- 7-feature 3-class F1=0.774 vs 4-det ensemble 0.785/4-det+surface 0.795。Multi-detector 在 3-class 上持续优于。\n\n**W4** [warning] Pythia-410M 与 Pythia generators 共享架构的公平性\n- Cross-reference 实验仅 5-gen subset。Pythia generators 恰好 F1 最高。\n\n**W5** [warning] XGBoost 超参数固定可能偏向多特征方法\n- 对单特征 baseline，200 棵 depth=6 的树可能过拟合。\n\n### 主要优势\n1. 任务定义新颖（gen depth classification 超越 binary detection）\n2. DDR 科学洞察优雅（drifting vs stationary 分解）\n3. 实验覆盖面极广（LOGO/LOFO/cross-model/cross-ref/cross-temp/cross-domain/cross-prompt/perturbation/length/classifier/feature ablation/finer granularity/downstream）\n4. 自我批评诚实\n5. 计算效率优势（单 410M model vs multi-detector 2.4× cost）\n\n### Questions for Authors\nQ1: 能否报告 gen-0 hold-out 实验量化真正的 gen-0 泛化？\nQ2: TOST ±2% margin 基于什么领域先验？\nQ3: 8-gen 设置下用非 Pythia reference model 时 LOGO F1 变化？\nQ4: Cross-model chains 扩展到 8 gen 后 F1=0.809 是否成立？\nQ5: entropy_min 保留的真正科学理由？",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-17T17:27:25.270652+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1331
}
```

</details>

---


### Assistant

_source line 566 · 2026-05-17T17:27:30.680602+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 55

## Round 55

2 recorded events


### User

_source line 567 · 2026-05-17T17:27:33.186015+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审查结果摘要**：

- **Overall: 3 (Findings)** | Soundness: 3/5 | Excitement: 3/5
- **3 个 Must-Fix 问题**：
  - N1: Downstream utility (Contribution 3) 是 null result 过度包装为独立贡献
  - N2: 方法无算法创新，7 手工特征 + XGBoost 是标准 feature engineering
  - N3: Instruction-tuned model 表现极弱（F1=0.338），严重限制实用性
- **5 个 Should-Fix 问题**：DDR "shape preservation" 措辞过强、gen-0 leakage 影响 headline metric、温度敏感性比标题暗示的更严重、ordinal classification 文献讨论不足、与 concurrent works 缺少实验性对比
- **主要优势**：实验设计严谨（LOGO/LOFO + 完整统计检验）、DDR 分解有价值、Limitations 坦诚详尽、写作质量高、格式合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 568 · 2026-05-17T17:27:38.944213+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 569 · 2026-05-17T17:28:37.780979+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 Round 1 意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1: Downstream utility 过度包装**
同意核心判断。我的 N1 从统计方法论角度独立发现了相同问题。Table 8 显示 random ppl=2.367 < depth-aware ppl=2.387；TOST 在 n=3 seeds 下的等价性结论不可靠。建议降级为 analysis finding。

**[REBUT] R2-N2: 方法新颖性不足**
部分反驳。(1) 论文在 §2.1 已明确自我定位为 "not a new detection method but the task formulation and the finding"；(2) 简单可解释方法支撑 DDR 分解是科学价值所在，QLoRA (F1=0.905) 无法提供这种 insight；(3) EMNLP 有录用 empirical finding + task formulation 论文的先例。但我同意论文在 "analysis paper" 与 "method paper" 之间定位模糊，应强化一边。

**[AGREE] R2-N3: Instruct model 失败**
完全同意。与我的 N3 相同关切。OLMo-Instruct F1=0.338 接近 random，且论文对 WHY 的分析不足。

---

### Should-Fix

**[AGREE] R2-W1**: Levene test 对 shape features 也拒绝 equal variance (§4.2 L70)，"preserve" 措辞过强。应改为量化表达（KS 10× gap）。

**[AGREE] R2-W2**: 与我 N2 相同。3-class F1 因 gen-0 leak 存在 upward bias。

**[AGREE] R2-W3**: 与我 N3 讨论重叠。"Temperature robustness" 标题需改为 "Temperature sensitivity"。

**[REBUT] R2-W4**: 部分反驳。论文在 §3.4、Appendix D、Appendix C 中讨论了 ordinal methods 且引用了 ordinal survey。但同意正文讨论应更集中。

**[REBUT] R2-W5**: 反驳。Concurrent works 研究不同 chain type（paraphrastic vs continuation），直接实验对比不可行。§2.2 的概念对比已足够。但同意 Appendix G 的 paraphrastic F1=0.671 可以在正文中与 concurrent work 做更明确的桥接。

---

### 总体评分差异

R2 给 3.0，我给 3.5。分歧在 N2（方法新颖性）。我认为 DDR finding + task formulation 对 EMNLP 有足够贡献；R2 更看重算法创新。若修复 N1/N3 + 明确 analysis paper 定位，论文可达 Findings 录用标准。Main conference 需 instruct model 方向突破。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 570 · 2026-05-17T17:28:43.461684+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 571 · 2026-05-17T17:28:45.991417+00:00_

[Reviewer 1 审稿结果]:
已提交交叉回应。总结：

- **N1 (TOST)**: 同意，与我的独立发现一致
- **N2 (方法新颖性)**: 部分反驳——DDR 的科学洞察 + task formulation 有价值，论文已自我定位为 empirical finding
- **N3 (instruct model)**: 完全同意
- **W1-W3**: 同意
- **W4-W5**: 部分反驳，论文已有相关讨论但可加强

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 572 · 2026-05-17T17:28:52.039865+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 58

## Round 58

12 recorded events


### User

_source line 573 · 2026-05-17T17:29:52.738907+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Round 1 意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: TOST 等价性测试解读具有误导性**

完全同意。我在自己的审稿中也将此标记为 N1 (critical)。补充以下证据：

1. Abstract L8 的措辞 "depth-aware data selection yields training utility equivalent to random subsampling" 使用了 "equivalent" 一词，但 Table 8 (Appendix K) 明确显示 random subsampling ppl=2.367 **一致优于** depth-aware 的 2.387。TOST 通过仅说明差异落在 ±2% margin 内，不支持 "equivalent" 的强表述。
2. Appendix K 中论文自己承认 Cohen's d = 86.0-119.7 是 "unreliable" 且 "artificially inflating"，这直接削弱了 TOST 的统计功效论证。仅 n=3 seeds 的实验不足以支撑任何因果性 claim。
3. Table 9 (TOST margin sensitivity) 显示 Full vs. Depth 0-1 在 ±2% margin 下不成立（需 ±3%），但 Contribution 3 (§1 L22) 的表述没有区分这两个 comparison。
4. 最重要的是：即使 TOST 成立，这是一个 **null result**——depth 信号对 data curation 无用。将其包装为 Contribution 3 过度抬高了一个 negative finding 的地位。

R1 的四条修改建议完全合理，我特别强调应将 Contribution 3 降级为 analysis finding 而非 main contribution。

---

**[AGREE] R1-N2: Gen-0 seed sharing 导致 3-class LOGO F1 系统性高估**

同意，我在 W2 中也提出了相同问题。R1 提供了更有力的定量证据：

- Appendix B 混淆矩阵 (Table 5): gen-0 recall = 99.4% vs. gen-1 = 75.0% vs. gen-2+ = 73.7%。gen-0 的近乎完美分类几乎必然来自 seed sharing 导致的 train-test overlap，而非 genuine generalization。
- 这意味着 3-class F1 = 0.762 中 gen-0 class 的贡献被 artificially inflated，真正有意义的 discriminative ability 体现在 gen-1 vs. gen-2+ 的 binary F1 = 0.694。
- 我同意 R1 的建议：primary metric 应改为 binary F1。Abstract 中 3-class 0.762/0.809 出现多次且排位靠前（Abstract L7, §1 L15, L21），给读者错误的 headline impression。

不过，我认为论文在 §4.1 L8 ("3-class metric may carry upward bias from memorized gen-0 patterns; we therefore also report a leak-free binary metric") 对问题有适当诊断，不是隐瞒，而是 **presentation emphasis** 问题。R1 建议 (2)（per-generator 分离 gen-0 seeds）是根本性修复，如果可行应优先采用。

---

**[AGREE] R1-N3: Base model + temperature 限制叠加，实用价值存疑**

完全同意。这也是我的 N3。R1 的 framing 比我更精确——两个限制的**叠加效应**是关键：

- 单独看：base-model-only 可以辩护为 "isolating the phenomenon"；temperature t∈[0.5, 0.9] 可以辩护为 "standard decoding regimes"
- 叠加看：现实世界文本 = instruct model + 未知 temperature → 方法在任何实际部署场景中都不可用

R1 建议 (1) 将 framing 从 "detection system" 转向 "phenomenon characterization" 是最合理的修复路径。这与我的 N2 建议一致——论文应将自己定位为 analysis paper（focus on DDR 现象本身的科学理解），而非声称提出一个可部署的 detection framework。

补充一点：§1 L12-13 已经有 "deliberate design choice" 的辩护，但 Abstract 和 Contribution 列表的措辞仍暗示这是一个 practical system（如 "competitive performance at substantially lower computational cost"），这种张力需要消除。

---

### Should-Fix 问题

**[AGREE] R1-W1: Cross-model 评估与主实验 generator 集合不一致**

同意这是一个 valid concern。§4.1 footnote 5 披露了 5-gen vs. 8-gen 差异，但 cross-model F1=0.809 在 §1 L15 和 Abstract L7 中作为 headline number 出现，读者很容易忽略脚注中的限定条件。Mistral-7B 是 LOGO binary F1 最低的 generator (0.633, Table 1)，如果加入 cross-model chains，F1=0.809 可能会下降。论文应在主文中明确标注这是 5-gen subset result，或者在 8-gen 设置下重跑 cross-model 实验。

---

**[REBUT] R1-W2: Spearman correlation 阈值缺乏标准引用**

部分不同意。R1 的建议（引用 Hinkle et al. 或类似标准）是合理的写作改进，但 DDR 的核心论证并不依赖于特定阈值的解读标准。

§4.2 的论证结构是：(1) drifting features |ρ| = 0.60-0.63；(2) shape features |ρ| < 0.10；(3) 两组之间存在 ~6-10× magnitude gap。这个 gap 本身才是 DDR 的核心证据，而非某个阈值是否达到 "substantial" 的标准。即使不用 "substantial" 这个标签，0.60 vs. 0.04 的差异也是 unambiguous。

此外，§4.2 还用 KS statistics 做了独立验证（drifting KS=0.517-0.537 vs. shape KS=0.043-0.052，~10× 差异），这提供了不依赖于 correlation interpretation 的第二条证据链。

建议：加标准引用是 easy fix，不反对，但这不构成 should-fix 级别问题。

---

**[AGREE] R1-W3: "Competitive performance" claim 与数据不完全吻合**

同意。Abstract L7 使用了 "with competitive performance at substantially lower computational cost" 的措辞。Table 4 显示 7-feature 在 3-class F1 上持续低于 multi-detector ensembles（0.774 vs. 0.785/0.795，gap = 1.1-2.1 pp）。虽然 binary F1 差异极小（0.705 vs. 0.700/0.708），但 "competitive" 一词 overstate 了 3-class 上的表现。

§4.3 L136 的主文措辞 ("moderately higher 3-class F1...with indistinguishable binary performance") 比 Abstract 更准确。建议 Abstract 改为 "at a fraction of the computational cost, with comparable binary but slightly lower 3-class performance" 或类似表述。

---

**[AGREE] R1-W4: Pythia-410M 与 Pythia generators 共享架构的公平性**

同意这是一个 valid concern，但影响程度有限。

- 支持 R1 的证据：Table 1 显示 Pythia generators (binary F1 0.718-0.724) 是表现最好的 generators，而 reference model 恰好也是 Pythia family。
- 缓解因素：Table 4 (cross-reference) 显示 OLMo reference 和 Qwen reference 的 LOGO F1 分别为 0.807 和 0.816（vs. Pythia-410M 的 0.803），spread 仅 0.013。这表明 reference family 不是 dominant factor。
- 但 R1 正确指出这是 5-gen subset 结果。在 full 8-gen 设置下（特别是包含 Llama 和 Mistral），cross-reference spread 可能更大。建议在 8-gen 设置下补充 cross-reference 实验。

---

**[AGREE] R1-W5: XGBoost 超参数固定可能偏向多特征方法**

同意这是一个 valid methodological concern。200 棵 depth=6 的树对单特征 input 可能过于复杂，导致过拟合并 artificially 降低 single-feature baseline 的表现。§3.4 声称 "identical hyperparameters across all methods in Table 4"，但 fair comparison 应考虑 model complexity 与 feature dimensionality 的匹配。

不过，影响程度可能有限：single-feature XGBoost 在 LOGO CV 下过拟合的空间受限于交叉验证本身的 regularization。建议至少报告一个 hyperparameter sweep 或 simpler model（如 logistic regression）作为 sanity check。

---

### Questions 回应

**Q1** (gen-0 hold-out 实验): 非常关键。如果 per-generator 分配独立的 gen-0 seeds，可以量化 gen-0 leakage 对 3-class metric 的真实影响。这是 N2 最直接的修复。

**Q2** (TOST ±2% margin): 同意这需要领域先验论证。现有 data selection 文献（DSIR, QuRating）中 2% perplexity 差异是否 practically meaningful 取决于具体应用，论文需要引用相关先例。

**Q3** (8-gen 非 Pythia reference): 同意需要补充。5-gen subset 的 cross-reference 结果不能直接外推到 8-gen。

**Q4** (8-gen cross-model chains): 同意需要验证。这是 W1 的核心问题。

**Q5** (entropy_min 保留理由): 这是我在 Minor Issues 中也提到的问题。"For completeness" 不是科学理由。要么 drop 要么提供更好的 justification。

---

### 总体评价对比

R1 给出 3.5 (Borderline Conference)，我给出 3 (Findings)。差异主要在于：

- **新颖性权重不同**: R1 在 Strengths 中承认 "任务定义新颖" 和 "DDR 科学洞察优雅"，给了更多 credit。我认为两篇 concurrent works (Broken Telephone, Markovian Chains) 显著降低了 novelty premium，且 feature engineering + XGBoost 的方法贡献接近零。
- **对 practical impact 的要求不同**: 我认为 base-model-only + temperature sensitivity + null downstream result 三重打击使得论文的实用叙事基本不成立，更适合作为 phenomenon characterization paper 以 Findings 发表。

R1 的审稿质量高，所有 N1-N3 和 W1-W5 的发现我基本认同（仅 W2 部分 rebut）。建议 Director 重点关注三个共识性 critical issues：(1) TOST 解读/Contribution 3 过度包装，(2) gen-0 leakage 的 presentation，(3) 实用性 framing 的调整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-17T17:30:17.641287+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 575 · 2026-05-17T17:30:17.691965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-17T17:30:23.162146+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 577 · 2026-05-17T17:30:23.212894+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-17T17:30:31.528771+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-17T17:30:31.680314+00:00_

- id: "R1-W1"
  summary: "Baseline hyperparameter inconsistency"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 8
  resolution: "method.tex unified to est200/md6. Verified R8."
  resolution_round: 8

- id: "R1-W5"
  summary: "Downstream experiment too small"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 8
  resolution: "TOST added. Contribution 3 restored with perplexity scope."
  resolution_round: 8

- id: "R7-W1"
  summary: "gen-0 seed sharing inflating headline"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 7
  last_seen_round: 11
  mentions:
    - {round: 9, reviewers: "R1,R2", note: "Abstract reports both binary and 3-class."}
    - {round: 10, reviewers: "R1,R2", note: "Recurred as R10-N1."}
    - {round: 11, reviewers: "R1,R2", note: "Both reviewers independently flagged. Abstract still leads with 3-class 0.809/0.762; leak-free binary 0.694 absent from Abstract. Gen-0 recall=99.4% vs gen-1=75.0%."}
  action_items:
    - {round: 10, action: "Use leak-free binary F1 as headline", assigned_to: "Paper Agent", status: "done"}
    - {round: 11, action: "Abstract leads with cross-model binary 0.764 + LOGO binary 0.694; 3-class as secondary with caveat; add gen-0 leakage note in Limitations", assigned_to: "Paper Agent", status: "in_progress"}
  resolution: ""
  resolution_round: null

- id: "R7-W2"
  summary: "DDR mechanism overclaim"
  category: method
  severity: warning
  status: in_progress
  first_raised_round: 7
  last_seen_round: 11
  mentions:
    - {round: 11, reviewers: "R1,R2", note: "DDR 'location shift preserving shape' claim based only on 7 summary statistics, not direct NLL distribution analysis. Both agree evidence is suggestive but not mechanistic."}
  action_items:
    - {round: 11, action: "Weaken to 'consistent with' / 'empirical pattern'; DDR primarily location shift with order-of-magnitude 
…[truncated 16784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-17T17:33:16.425626+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"TOST added. Contribution 3 restored with perplexity scope.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Abstract reports both binary and 3-class.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-N1.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers independently flag as critical. Abstract still leads with 3-class 0.809/0.762; leak-free binary 0.694 not primary. Gen-0 recall=99.4% vs gen-1=75.0%. R1 proposes per-generator seed separation as root fix.\"}\n  action_items:\n    - {round: 10, action: \"Use leak-free binary F1 as headline\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Abstract must lead with binary F1 (0.764 cross-model, 0.694 LOGO) as primary; 3-class as secondary with explicit upward-bias caveat; or separate gen-0 seeds per generator\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim — 'preserving shape' vs Levene test rejection\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Levene test rejects equal variance for ALL 7 features including shape features (p<10^-10). 'Preserving distributional shape' is too strong. R2 proposes 'shape features drift much less' or 'approximately preserving shape'. Coefficient of variation shift <3% vs >15% is the real evidence.\"}\n  action_items:\n    - {round: 11, action: \"Replace 'preserving shape' with 'approximately preserving shape' or quantitative formulation (10x magnitude gap); discuss Levene test tension explicitly\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Structural.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"DDR vs model collapse still insufficient.\"}\n  action_items:\n    - {round: 10, action: \"Expand §5 model collapse to full paragraph\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"discussion.tex: full paragraph on inference-chain vs training-loop, reversibility, shape stationarity evidence, pre-collapse regime framing.\"\n  resolution_round: 10\n\n- id: \"R7-W5\"\n  summary: \"Base-model-only scope vs Introduction web contamination motivation\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Abstract/Intro still imply general applicability.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers flag as critical (unanimous). OLMo-Instruct F1=0.338, cross-temp Qwen 0.789→0.418. Two limitations stack: base-model-only + temperature sensitivity = zero real-world applicability. Must reframe from 'detection system' to 'phenomenon characterization'.\"}\n  action_items:\n    - {round: 10, action: \"Explicit base-model scope in Intro; instruct in Discussion\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Reframe paper positioning: 'characterizing recursive generation distributional dynamics' not 'practical detection tool'; explicit scope in Abstract; remove 'competitive performance' language that implies deployment readiness\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  resolution: \"Discussion has dedicated paragraph with 48% error rate, 86% false negative rate, mechanistic explanation, scale effect.\"\n  resolution_round: 10\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M3\"\n  summary: \"NLL + topic drift spec\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Fixed. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-M4\"\n  summary: \"Missing references\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"All added. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R8-N1\"\n  summary: \"entropy_std grouping + Figure 1 caption\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1 as primary metric\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Recurred. Abstract still leads with 3-class numbers. Binary F1 0.694 (LOGO) / 0.764 (cross-model) must be primary.\"}\n  action_items:\n    - {round: 11, action: \"Restructure Abstract: lead with binary F1 as primary metric, 3-class as secondary with caveat\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-RV2\"\n  summary: \"LOFO delta error\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected to -0.8pp. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Abstract uses 'equivalent' but random consistently outperforms (ppl 2.367 vs 2.387). Must not use 'equivalent' without qualification. Demote to analysis finding.\"}\n  action_items:\n    - {round: 9, action: \"Abstract: 'downstream harm' → 'downstream perplexity degradation'\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Replace 'equivalent' with 'does not substantially degrade'; acknowledge random > depth-aware; demote from Contribution 3 to analysis finding in Discussion\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises vs 3-class reality\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"5-class F1=0.50, gen-1/gen-2+ error rate 48%.\"}\n    - {round: 11, reviewers: \"R2\", note: \"CORAL/Frank-Hall zero improvement (Appendix D). Ordinal framing in §3.1 not substantiated by method. R2-W4.\"}\n  action_items:\n    - {round: 10, action: \"Revise abstract to 'coarse ordinal'; state depth≥2 collapse reason in main text\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Title already changed to 'Depth Fingerprinting'; discuss in main text why ordinal methods don't help (gap compression beyond depth 2)\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation experiment is null result with flawed TOST methodology\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Random subsampling = depth-stratified at equal N. Only 3 seeds.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers flag unanimously as critical. Specific new criticisms: (1) TOST with n=3 seeds produces Cohen's d=86-120, paper self-acknowledges as 'artificially inflated'; (2) ±2% margin unjustified from domain knowledge (Table 9 shows ±1% fails); (3) random consistently outperforms depth-aware yet Abstract says 'equivalent'; (4) this is fundamentally a null result packaged as Contribution 3. Must demote.\"}\n  action_items:\n    - {round: 10, action: \"Demote curation from core motivation; adjust framing\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Demote from Contribution 3 to Discussion analysis; replace 'equivalent' with 'does not substantially degrade'; report random > depth-aware honestly; move TOST margin sensitivity (Table 9) to main text or explicitly caveat n=3 limitation\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Sensitivity real, needs prominent discussion and explicit working range.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Cross-temperature transfer: Qwen3-1.7B 0.789→0.418. t=1.0 entropy_mean ρ collapses to -0.002. Section title 'Temperature robustness' is misleading — should be 'Temperature sensitivity'. Many real-world APIs use t=1.0.\"}\n  action_items:\n    - {round: 10, action: \"Explicit working range [0.5,0.9]; ρ collapse mechanism\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Rename §4.2 paragraph from 'Temperature robustness' to 'Temperature sensitivity'; discuss cross-temp transfer failure prominently; state 'assumes known/matched temperature' as deployment requirement\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"Location shift claim lacks formal statistical testing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"results.tex: KS tests with exact values, Levene tests, CV shift comparison.\"\n  resolution_round: 10\n\n- id: \"R10-W3\"\n  summary: \"TOST ±2% margin unjustified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"appendix_downstream.tex: multi-margin table + Cohen's d + Lakens citation.\"\n  resolution_round: 10\n\n- id: \"R10-W4\"\n  summary: \"Cross-model F1=0.809 lacks formal table\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"results.tex Table 1: per-class P/R/F1 + 95% CI.\"\n  resolution_round: 10\n\n- id: \"R10-W5\"\n  summary: \"Data diversity insufficient (Wikipedia-only seeds)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Cross-domain numbers in main text; domain bias in Limitations.\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"Geng et al. (2026) differentiation insufficient\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"related_work.tex: mechanistic comparison paragraph.\"\n  resolution_round: 10\n\n- id: \"R11-N1\"\n  summary: \"Title 'Ordinal' sets ordinal-regression expectation but method is standard multiclass\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Current title uses 'Depth Fingerprinting' (already fixed from earlier). But body still frames as ordinal (§3.1) without ordinal method contribution. CORAL zero improvement.\"}\n  action_items:\n    - {round: 11, action: \"Keep current title; soften §3.1 ordinal framing to 'motivated by ordinal structure' rather than 'ordinal classification task'\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Reference model family bias (Pythia-410M ref + Pythia generators highest F1)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Pythia generators 0.718-0.724 highest in Table 1. Cross-reference experiment (Table 4) only on 5-gen subset, spread 0.013. Need 8-gen cross-reference or explicit discussion of architecture overlap.\"}\n  action_items:\n    - {round: 11, action: \"Discuss in §4.2 or Discussion: Pythia F1 advantage may partly reflect reference model familiarity; cross-ref spread (0.013) suggests limited effect but 8-gen verification ideal\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Multi-detector ensemble outperforms 7-feature on 3-class; 'competitive' overclaims\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Table 4: 4-det+surface 0.795 vs 7-feature 0.774 (2.1pp gap). Abstract 'competitive performance' overstates. Binary F1 difference negligible (0.705 vs 0.708). Must qualify.\"}\n  action_items:\n    - {round: 11, action: \"Abstract: replace 'competitive performance' with 'comparable binary performance at 2.4x lower cost, with moderate 3-class gap'\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"5-gen/6-gen/8-gen subset mixing impairs comparability\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Cross-model chains (5-gen) vs LOGO (8-gen) vs appendix (6-gen). No master explanation. F1=0.809 may not hold with 8-gen (Mistral LOGO F1=0.633).\"}\n  action_items:\n    - {round: 11, action: \"Add explicit paragraph/footnote explaining generator subsets and their historical rationale; flag cross-model 0.809 as 5-gen-only result prominently\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"XGBoost hyperparameters fixed may favor multi-feature over single-feature baselines\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1\", note: \"200 trees depth=6 for 1-dimensional input (single-score baselines) may overfit. LOGO CV limits overfitting but optimal config for 1-feature differs from 7-feature. R2 agrees impact likely limited but valid concern.\"}\n  action_items:\n    - {round: 11, action: \"Report tuned hyperparameter results for single-feature baselines (at minimum grid search max_depth), or add logistic regression sanity check\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"Ordinal classification literature discussion insufficient in main text\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R2\", note: \"§3.1 frames as ordinal task, cites CORAL/Gutierrez survey, but main text never discusses why ordinal methods don't help. This is itself an interesting finding (gap compression beyond depth 2). R1 partially rebuts (Appendix D exists) but agrees main text should discuss.\"}\n  action_items:\n    - {round: 11, action: \"Add 2-3 sentences in §4.2 or Discussion explaining why ordinal methods yield zero improvement (depth-class gaps non-uniform; XGBoost implicitly captures ordinal structure)\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M1\"\n  summary: \"Discussion over-fragmented with \\\\paragraph{} (AI writing signature)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"7+ paragraph headers in Discussion.\"}\n  action_items:\n    - {round: 11, action: \"Merge Discussion into 3-4 coherent paragraphs\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"'Entropy' misnomer (actually token-level NLL/surprisal)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Only footnote 1 clarifies. R2 says should be stated earlier/more prominently.\"}\n  action_items:\n    - {round: 11, action: \"Move clarification to §3.3 paragraph opening, not footnote\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"Tail decay rank range 100-1000 unjustified\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"No theoretical motivation.\"}\n  action_items:\n    - {round: 11, action: \"Add brief justification\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M4\"\n  summary: \"Appendix confusion matrix uses 6-gen not 8-gen\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Not aligned with Table 1 (8-gen).\"}\n  action_items:\n    - {round: 11, action: \"Add note in appendix\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M5\"\n  summary: \"|ρ| thresholds lack standard citation\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1\", note: \"R2 partially rebuts: 10x gap is self-evident. But standard citation (Hinkle/Akoglu) is easy fix.\"}\n  action_items:\n    - {round: 11, action: \"Add citation for correlation interpretation or emphasize magnitude gap rather than thresholds\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M6\"\n  summary: \"Cross-domain uses t=1.0 vs main experiment t=0.7\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1\", note: \"Results not directly comparable to main experiment.\"}\n  action_items:\n    - {round: 11, action: \"Add comparability caveat footnote\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M7\"\n  summary: \"Figure 3 uses PNG format instead of PDF\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1\", note: \"fig3_baseline_comparison.png may degrade at print resolution.\"}\n  action_items:\n    - {round: 11, action: \"Regenerate as PDF vector graphic\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M8\"\n  summary: \"entropy_min contributes zero yet retained 'for completeness'\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"LOFO Δ=+0.01pp (removing slightly improves). 'For completeness' is not a scientific justification. Either drop or provide better rationale.\"}\n  action_items:\n    - {round: 11, action: \"Reword justification: 'removing does not statistically improve performance (paired bootstrap p=0.89)' rather than 'for completeness'\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-CODE1\"\n  summary: \"eval_8gen_logo.py JSONL loading broken for Llama/Mistral\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"Reviewer\", note: \"load_data() tries to load nonexistent Llama/Mistral JSONL files. Reproducibility issue.\"}\n  action_items:\n    - {round: 11, action: \"Fix file path mapping in load_data()\", assigned_to: \"Main Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === 历史 (R1-R6) ===\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Direction C. Persists as R7-W4.\"\n  resolution_round: 5\n\n- id: \"R5-TABLE1\"\n  summary: \"Table 1 only 6 generators\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"All 8.\"\n  resolution_round: 6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "- id: \"R1-W1\"\n  summary: \"Baseline hyperparameter inconsistency\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"method.tex unified to est200/md6. Verified R8.\"\n  resolution_round: 8\n\n- id: \"R1-W5\"\n  summary: \"Downstream experiment too small\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 8\n  resolution: \"TOST added. Contribution 3 restored with perplexity scope.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"gen-0 seed sharing inflating headline\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Abstract reports both binary and 3-class.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"Recurred as R10-N1.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers independently flag as critical. Abstract still leads with 3-class 0.809/0.762; leak-free binary 0.694 not primary. Gen-0 recall=99.4% vs gen-1=75.0%. R1 proposes per-generator seed separation as root fix.\"}\n  action_items:\n    - {round: 10, action: \"Use leak-free binary F1 as headline\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Abstract must lead with binary F1 (0.764 cross-model, 0.694 LOGO) as primary; 3-class as secondary with explicit upward-bias caveat; or separate gen-0 seeds per generator\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"DDR mechanism overclaim — 'preserving shape' vs Levene test rejection\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Levene test rejects equal variance for ALL 7 features including shape features (p<10^-10). 'Preserving distributional shape' is too strong. R2 proposes 'shape features drift much less' or 'approximately preserving shape'. Coefficient of variation shift <3% vs >15% is the real evidence.\"}\n  action_items:\n    - {round: 11, action: \"Replace 'preserving shape' with 'approximately preserving shape' or quantitative formulation (10x magnitude gap); discuss Levene test tension explicitly\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Efficiency not quantified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 ms/text + memory. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Method novelty divergence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  mentions:\n    - {round: 9, reviewers: \"R1,R2\", note: \"Structural.\"}\n    - {round: 10, reviewers: \"R1,R2\", note: \"DDR vs model collapse still insufficient.\"}\n  action_items:\n    - {round: 10, action: \"Expand §5 model collapse to full paragraph\", assigned_to: \"Paper Agent\", status: \"done\"}\n  resolution: \"discussion.tex: full paragraph on inference-chain vs training-loop, reversibility, shape stationarity evidence, pre-collapse regime framing.\"\n  resolution_round: 10\n\n- id: \"R7-W5\"\n  summary: \"Base-model-only scope vs Introduction web contamination motivation\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Abstract/Intro still imply general applicability.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers flag as critical (unanimous). OLMo-Instruct F1=0.338, cross-temp Qwen 0.789→0.418. Two limitations stack: base-model-only + temperature sensitivity = zero real-world applicability. Must reframe from 'detection system' to 'phenomenon characterization'.\"}\n  action_items:\n    - {round: 10, action: \"Explicit base-model scope in Intro; instruct in Discussion\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Reframe paper positioning: 'characterizing recursive generation distributional dynamics' not 'practical detection tool'; explicit scope in Abstract; remove 'competitive performance' language that implies deployment readiness\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W6\"\n  summary: \"gen-1/gen-2+ boundary underdiscussed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 10\n  resolution: \"Discussion has dedicated paragraph with 48% error rate, 86% false negative rate, mechanistic explanation, scale effect.\"\n  resolution_round: 10\n\n- id: \"R7-W7\"\n  summary: \"Missing Ghostbuster baseline\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Skipped. Citations added.\"\n  resolution_round: 7\n\n- id: \"R7-M1\"\n  summary: \"'strong' → 'substantial'\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"All locations fixed. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M2\"\n  summary: \"Bib orphans\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"dolma/fineweb citations added. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R7-M3\"\n  summary: \"NLL + topic drift spec\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Fixed. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R7-M4\"\n  summary: \"Missing references\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"All added. Confirmed R8.\"\n  resolution_round: 8\n\n- id: \"R8-N1\"\n  summary: \"entropy_std grouping + Figure 1 caption\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-N2\"\n  summary: \"Abstract missing binary F1 as primary metric\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Recurred. Abstract still leads with 3-class numbers. Binary F1 0.694 (LOGO) / 0.764 (cross-model) must be primary.\"}\n  action_items:\n    - {round: 11, action: \"Restructure Abstract: lead with binary F1 as primary metric, 3-class as secondary with caveat\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-RV1\"\n  summary: \"Fabricated R²=0.082\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Replaced with verified ρ=-0.286. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R8-RV2\"\n  summary: \"LOFO delta error\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Corrected to -0.8pp. Verified R9.\"\n  resolution_round: 9\n\n- id: \"R9-N1\"\n  summary: \"Contribution 3 'harm' overclaim in Abstract\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Abstract uses 'equivalent' but random consistently outperforms (ppl 2.367 vs 2.387). Must not use 'equivalent' without qualification. Demote to analysis finding.\"}\n  action_items:\n    - {round: 9, action: \"Abstract: 'downstream harm' → 'downstream perplexity degradation'\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Replace 'equivalent' with 'does not substantially degrade'; acknowledge random > depth-aware; demote from Contribution 3 to analysis finding in Discussion\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-N2\"\n  summary: \"'Ordinal depth estimation' framing overpromises vs 3-class reality\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"5-class F1=0.50, gen-1/gen-2+ error rate 48%.\"}\n    - {round: 11, reviewers: \"R2\", note: \"CORAL/Frank-Hall zero improvement (Appendix D). Ordinal framing in §3.1 not substantiated by method. R2-W4.\"}\n  action_items:\n    - {round: 10, action: \"Revise abstract to 'coarse ordinal'; state depth≥2 collapse reason in main text\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Title already changed to 'Depth Fingerprinting'; discuss in main text why ordinal methods don't help (gap compression beyond depth 2)\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-N3\"\n  summary: \"Downstream curation experiment is null result with flawed TOST methodology\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Random subsampling = depth-stratified at equal N. Only 3 seeds.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Both reviewers flag unanimously as critical. Specific new criticisms: (1) TOST with n=3 seeds produces Cohen's d=86-120, paper self-acknowledges as 'artificially inflated'; (2) ±2% margin unjustified from domain knowledge (Table 9 shows ±1% fails); (3) random consistently outperforms depth-aware yet Abstract says 'equivalent'; (4) this is fundamentally a null result packaged as Contribution 3. Must demote.\"}\n  action_items:\n    - {round: 10, action: \"Demote curation from core motivation; adjust framing\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Demote from Contribution 3 to Discussion analysis; replace 'equivalent' with 'does not substantially degrade'; report random > depth-aware honestly; move TOST margin sensitivity (Table 9) to main text or explicitly caveat n=3 limitation\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Temperature sensitivity limits generalizability\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - {round: 10, reviewers: \"R1,R2\", note: \"Sensitivity real, needs prominent discussion and explicit working range.\"}\n    - {round: 11, reviewers: \"R1,R2\", note: \"Cross-temperature transfer: Qwen3-1.7B 0.789→0.418. t=1.0 entropy_mean ρ collapses to -0.002. Section title 'Temperature robustness' is misleading — should be 'Temperature sensitivity'. Many real-world APIs use t=1.0.\"}\n  action_items:\n    - {round: 10, action: \"Explicit working range [0.5,0.9]; ρ collapse mechanism\", assigned_to: \"Paper Agent\", status: \"done\"}\n    - {round: 11, action: \"Rename §4.2 paragraph from 'Temperature robustness' to 'Temperature sensitivity'; discuss cross-temp transfer failure prominently; state 'assumes known/matched temperature' as deployment requirement\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"Location shift claim lacks formal statistical testing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"results.tex: KS tests with exact values, Levene tests, CV shift comparison.\"\n  resolution_round: 10\n\n- id: \"R10-W3\"\n  summary: \"TOST ±2% margin unjustified\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"appendix_downstream.tex: multi-margin table + Cohen's d + Lakens citation.\"\n  resolution_round: 10\n\n- id: \"R10-W4\"\n  summary: \"Cross-model F1=0.809 lacks formal table\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"results.tex Table 1: per-class P/R/F1 + 95% CI.\"\n  resolution_round: 10\n\n- id: \"R10-W5\"\n  summary: \"Data diversity insufficient (Wikipedia-only seeds)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Cross-domain numbers in main text; domain bias in Limitations.\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"Geng et al. (2026) differentiation insufficient\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"related_work.tex: mechanistic comparison paragraph.\"\n  resolution_round: 10\n\n- id: \"R11-N1\"\n  summary: \"Title 'Ordinal' sets ordinal-regression expectation but method is standard multiclass\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Current title uses 'Depth Fingerprinting' (already fixed from earlier). But body still frames as ordinal (§3.1) without ordinal method contribution. CORAL zero improvement.\"}\n  action_items:\n    - {round: 11, action: \"Keep current title; soften §3.1 ordinal framing to 'motivated by ordinal structure' rather than 'ordinal classification task'\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Reference model family bias (Pythia-410M ref + Pythia generators highest F1)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Pythia generators 0.718-0.724 highest in Table 1. Cross-reference experiment (Table 4) only on 5-gen subset, spread 0.013. Need 8-gen cross-reference or explicit discussion of architecture overlap.\"}\n  action_items:\n    - {round: 11, action: \"Discuss in §4.2 or Discussion: Pythia F1 advantage may partly reflect reference model familiarity; cross-ref spread (0.013) suggests limited effect but 8-gen verification ideal\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Multi-detector ensemble outperforms 7-feature on 3-class; 'competitive' overclaims\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Table 4: 4-det+surface 0.795 vs 7-feature 0.774 (2.1pp gap). Abstract 'competitive performance' overstates. Binary F1 difference negligible (0.705 vs 0.708). Must qualify.\"}\n  action_items:\n    - {round: 11, action: \"Abstract: replace 'competitive performance' with 'comparable binary performance at 2.4x lower cost, with moderate 3-class gap'\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"5-gen/6-gen/8-gen subset mixing impairs comparability\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Cross-model chains (5-gen) vs LOGO (8-gen) vs appendix (6-gen). No master explanation. F1=0.809 may not hold with 8-gen (Mistral LOGO F1=0.633).\"}\n  action_items:\n    - {round: 11, action: \"Add explicit paragraph/footnote explaining generator subsets and their historical rationale; flag cross-model 0.809 as 5-gen-only result prominently\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"XGBoost hyperparameters fixed may favor multi-feature over single-feature baselines\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1\", note: \"200 trees depth=6 for 1-dimensional input (single-score baselines) may overfit. LOGO CV limits overfitting but optimal config for 1-feature differs from 7-feature. R2 agrees impact likely limited but valid concern.\"}\n  action_items:\n    - {round: 11, action: \"Report tuned hyperparameter results for single-feature baselines (at minimum grid search max_depth), or add logistic regression sanity check\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"Ordinal classification literature discussion insufficient in main text\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R2\", note: \"§3.1 frames as ordinal task, cites CORAL/Gutierrez survey, but main text never discusses why ordinal methods don't help. This is itself an interesting finding (gap compression beyond depth 2). R1 partially rebuts (Appendix D exists) but agrees main text should discuss.\"}\n  action_items:\n    - {round: 11, action: \"Add 2-3 sentences in §4.2 or Discussion explaining why ordinal methods yield zero improvement (depth-class gaps non-uniform; XGBoost implicitly captures ordinal structure)\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M1\"\n  summary: \"Discussion over-fragmented with \\\\paragraph{} (AI writing signature)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"7+ paragraph headers in Discussion.\"}\n  action_items:\n    - {round: 11, action: \"Merge Discussion into 3-4 coherent paragraphs\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"'Entropy' misnomer (actually token-level NLL/surprisal)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Only footnote 1 clarifies. R2 says should be stated earlier/more prominently.\"}\n  action_items:\n    - {round: 11, action: \"Move clarification to §3.3 paragraph opening, not footnote\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"Tail decay rank range 100-1000 unjustified\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"No theoretical motivation.\"}\n  action_items:\n    - {round: 11, action: \"Add brief justification\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M4\"\n  summary: \"Appendix confusion matrix uses 6-gen not 8-gen\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"Not aligned with Table 1 (8-gen).\"}\n  action_items:\n    - {round: 11, action: \"Add note in appendix\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M5\"\n  summary: \"|ρ| thresholds lack standard citation\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1\", note: \"R2 partially rebuts: 10x gap is self-evident. But standard citation (Hinkle/Akoglu) is easy fix.\"}\n  action_items:\n    - {round: 11, action: \"Add citation for correlation interpretation or emphasize magnitude gap rather than thresholds\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M6\"\n  summary: \"Cross-domain uses t=1.0 vs main experiment t=0.7\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1\", note: \"Results not directly comparable to main experiment.\"}\n  action_items:\n    - {round: 11, action: \"Add comparability caveat footnote\", assigned_to: \"Paper Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M7\"\n  summary: \"Figure 3 uses PNG format instead of PDF\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1\", note: \"fig3_baseline_comparison.png may degrade at print resolution.\"}\n  action_items:\n    - {round: 11, action: \"Regenerate as PDF vector graphic\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M8\"\n  summary: \"entropy_min contributes zero yet retained 'for completeness'\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"R1,R2\", note: \"LOFO Δ=+0.01pp (removing slightly improves). 'For completeness' is not a scientific justification. Either drop or provide better rationale.\"}\n  action_items:\n    - {round: 11, action: \"Reword justification: 'removing does not statistically improve performance (paired bootstrap p=0.89)' rather than 'for completeness'\", assigned_to: \"Paper Agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-CODE1\"\n  summary: \"eval_8gen_logo.py JSONL loading broken for Llama/Mistral\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - {round: 11, reviewers: \"Reviewer\", note: \"load_data() tries to load nonexistent Llama/Mistral JSONL files. Reproducibility issue.\"}\n  action_items:\n    - {round: 11, action: \"Fix file path mapping in load_data()\", assigned_to: \"Main Agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n# === 历史 (R1-R6) ===\n\n- id: \"R1-W2\"\n  summary: \"Generalization claim too strong\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Conservative framing.\"\n  resolution_round: 5\n\n- id: \"R1-W3\"\n  summary: \"Topic drift as confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Framed as mediator.\"\n  resolution_round: 5\n\n- id: \"R1-W4\"\n  summary: \"Missing multi-class refs\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Added.\"\n  resolution_round: 5\n\n- id: \"R1-W6\"\n  summary: \"Limited method novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  resolution: \"Direction C. Persists as R7-W4.\"\n  resolution_round: 5\n\n- id: \"R5-TABLE1\"\n  summary: \"Table 1 only 6 generators\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"All 8.\"\n  resolution_round: 6"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-17T17:33:16.578028+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 22583}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-17T17:35:19.371331+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 11 Consolidated Review Report\n\n**Paper**: \"Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\"\n**Target**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + Related Work)\n\n---\n\n## Summary\n\nThe paper formulates generation depth classification (gen-0/gen-1/gen-2+) as a new task beyond binary AI text detection, identifies a \"differential depth response\" (DDR) where central-tendency features drift monotonically with recursive generation depth while shape features remain near-stationary, and builds a 7-feature XGBoost ensemble achieving 3-class LOGO F1=0.762 across 8 base-model generators from 5 families. A TOST equivalence test suggests detected distributional shift does not translate to downstream perplexity degradation.\n\n---\n\n## Strengths\n\n1. **Novel and well-motivated task formulation**: Generation depth classification (gen-0/gen-1/gen-2+) fills a genuine gap between binary detection and source attribution. Independent convergence with two concurrent works (Broken Telephone, Markovian Chains) on ~3-class practical ceiling validates the research direction. [Unanimous]\n\n2. **DDR is a genuine scientific insight**: The drifting vs. stationary feature decomposition provides structured, interpretable understanding of recursive generation dynamics. The location-shift-preserving-shape hypothesis has theoretical elegance and empirical support (KS statistics show 10× magnitude gap). [Unanimous]\n\n3. **Exceptional experimental coverage**: LOGO/LOFO/cross-model/cross-reference/cross-temperature/cross-domain/cross-prompt/perturbation/length confound/classifier ablation/feature ablation/finer granularity/downstream utility — nearly every conceivable reviewer question is pre-addressed. Statistical methodology (bootstrap CI, McNemar, Bonferroni, TOST) exceeds average EMNLP standard. [Unanimous]\n\n4. **Honest self-criticism**: Paper proactively identifies gen-0 seed sharing bias, reports instruct model failure (F1=0.338), t=1.0 degradation, and provides leak-free binary metric. Limitations section is comprehensive and candid. [Unanimous]\n\n5. **Computational efficiency advantage**: Single 410M reference model (905 MB, 9.7 ms/text) vs. multi-detector ensembles (2 models, 2868 MB, 22.8 ms/text) with comparable binary F1. [Unanimous]\n\n6. **Writing quality and format compliance**: No AI writing artifacts (no em-dashes, no -ing phrase abuse, no excessive paragraphing). ACL style with [review] option, anonymous, line numbers, 8-page main text, Limitations section present. [R2 confirmed]\n\n---\n\n## Weaknesses\n\n### Must-Fix (影响接收决定)\n\n**MF1** [CONSENSUS — R1-N1 + R2-N1] **TOST equivalence test methodology flawed and Contribution 3 over-packaged**\n\nThe paper's third contribution claims \"depth-aware data selection yields training utility equivalent to random subsampling\" (Abstract L8). This is problematic on multiple levels:\n- Table 8 shows random subsampling **consistently outperforms** depth-aware (ppl 2.367 vs 2.387). Using \"equivalent\" is misleading when one method uniformly dominates.\n- TOST with n=3 seeds produces Cohen's d = 86–120, which the paper itself acknowledges as \"artificially inflated.\" Statistical power derives from extremely low seed-level variance, not genuine equivalence evidence.\n- The ±2% margin is not justified from domain knowledge. Table 9 shows equivalence fails at ±1% margin.\n- Fundamentally, this is a **null result**: the detected distributional shift has no practical downstream impact. Packaging this as a main contribution overstates its significance and paradoxically undermines the paper's data-curation motivation.\n\n**Required action**: (1) Demote from Contribution 3 to Discussion analysis finding; (2) Replace \"equivalent\" with \"does not substantially degrade\"; (3) Acknowledge random > depth-aware honestly; (4) Caveat n=3 limitation explicitly.\n\n---\n\n**MF2** [CONSENSUS — R1-N2 + R2-W2] **Gen-0 seed sharing inflates headline 3-class metric**\n\nAll 8 generators share identical ~1000 Wikipedia seeds as gen-0. In LOGO, held-out generator's gen-0 texts appear verbatim in training (via other generators' gen-0), creating direct train-test overlap. Evidence:\n- Confusion matrix: gen-0 recall = 99.4% vs. gen-1 = 75.0% vs. gen-2+ = 73.7%\n- 3-class macro F1 = 0.762 is upward-biased; the leak-free binary metric (gen-1 vs. gen-2+) = 0.694 is the trustworthy number\n- Despite paper correctly diagnosing this issue (§4.1 L8), Abstract/Introduction/Conclusion still lead with 3-class numbers (0.809, 0.762)\n\n**Required action**: (1) Abstract must lead with binary F1 (0.764 cross-model, 0.694 LOGO) as primary metric; (2) 3-class numbers demoted to secondary with explicit caveat; (3) Ideally: separate gen-0 seeds per generator to eliminate overlap entirely.\n\n---\n\n**MF3** [CONSENSUS — R1-N3 + R2-N3] **Base-model-only + temperature sensitivity = zero real-world applicability; framing mismatch**\n\nTwo independently devastating limitations stack:\n- **Instruct models**: OLMo-Instruct LOGO F1 = 0.338 (≈random baseline), Qwen3-0.6B-chat = 0.667. Real-world LLM text is overwhelmingly instruction-tuned.\n- **Temperature**: Cross-temperature transfer Qwen3-1.7B drops from 0.789 → 0.418. At t=1.0, entropy mean ρ collapses from -0.60 to -0.002. Many APIs default to t=1.0.\n- Combined: no real deployment scenario satisfies both base-model + known-temperature constraints.\n\nThe paper's Introduction motivates with web contamination (§1 L1-5) and §4.3 uses \"competitive performance at substantially lower computational cost\" — language implying deployment readiness. This creates a fundamental framing mismatch with the method's actual scope.\n\n**Required action**: (1) Reframe from \"detection/classification system\" to \"characterizing fundamental properties of recursive generation\"; (2) Remove deployment-implying language (\"competitive performance\"); (3) Explicit scope statement in Abstract (base models, standard decoding); (4) Deeper analysis of WHY instruction tuning destroys signal (which factor dominates: length regulation, format constraints, RLHF shaping?).\n\n---\n\n**MF4** [DIVERGENCE — R2-N2; R1 partial rebut] **Method novelty insufficient for main conference**\n\nR2 argues: 7 handcrafted features + off-the-shelf XGBoost constitutes zero algorithmic innovation. QLoRA (F1=0.905) demonstrates richer signal exists. CORAL/ordinal methods provide zero improvement. The paper's own §2.1 admission (\"not a new detection method\") confirms method contribution is negligible.\n\nR1 partially rebuts: (1) Paper is honestly self-positioned as task formulation + empirical finding; (2) Simple interpretable method enables DDR decomposition that neural approaches cannot; (3) EMNLP has precedent for empirical finding papers.\n\n**Director assessment**: The divergence is legitimate. If the paper clearly positions itself as an **analysis/phenomenon paper** (emphasizing DDR insight over classification pipeline), the contribution is appropriate for Findings. For main conference, methodological novelty or deeper theoretical understanding of DDR would be needed.\n\n---\n\n### Should-Fix (影响评分)\n\n**SF1** [CONSENSUS] **DDR \"shape preservation\" overstated**: Levene tests reject equal variance for ALL features including shape features (p < 10⁻¹⁰). \"Preserving distributional shape\" should be \"approximately preserving shape\" or quantified as \"order-of-magnitude smaller drift in shape features\" (CV shift <3% vs >15%).\n\n**SF2** [CONSENSUS] **Cross-model F1=0.809 uses 5-gen subset, not 8-gen**: Mistral-7B (LOGO binary F1=0.633, lowest) excluded from cross-model evaluation. The headline 0.809 may not hold with 8 generators. Must be prominently flagged as 5-gen result or re-run with full set.\n\n**SF3** [CONSENSUS] **\"Competitive performance\" claim**: Abstract overstates. 7-feature 3-cl F1=0.774 vs 4-det+surface 0.795 (2.1pp gap). Binary F1 difference negligible. Should say \"comparable binary performance at 2.4× lower cost.\"\n\n**SF4** [CONSENSUS] **Temperature section title misleading**: \"Temperature robustness\" paragraph actually documents a hard failure mode at t=1.0. Rename to \"Temperature sensitivity\" and discuss cross-temperature transfer failure prominently.\n\n**SF5** [CONSENSUS] **Pythia-410M reference model family bias**: Pythia generators achieve highest F1 (0.718-0.724) while reference model is Pythia family. Cross-reference spread (0.013) is on 5-gen subset only. Discuss architecture overlap in main text.\n\n**SF6** [R1 only, R2 agrees limited impact] **XGBoost hyperparameters fixed**: 200 trees depth=6 may be suboptimal for 1-dimensional single-score baselines. Report tuned results or simpler classifier sanity check.\n\n**SF7** [R2 only, R1 partial rebut] **Ordinal classification discussion insufficient**: §3.1 frames as ordinal task but main text never discusses why ordinal methods (CORAL, Frank-Hall) provide zero improvement. This is itself an interesting finding deserving explanation.\n\n---\n\n### Minor Issues\n\n- entropy_min retained \"for completeness\" (LOFO Δ=+0.01pp, i.e., removing slightly helps). Provide statistical justification or drop.\n- Figure 3 PNG format — regenerate as PDF for print quality\n- Appendix confusion matrix uses 6-gen, not aligned with Table 1 (8-gen)\n- Cross-domain evaluation uses t=1.0 while main experiment uses t=0.7 — add comparability note\n- \"Entropy\" misnomer (actually token-level NLL) clarified only in footnote — move to §3.3 opening\n- Tail decay rank range 100–1000 lacks theoretical motivation\n- Bonferroni correction application scope not fully specified (which comparisons, how many?)\n- Table 1 caption overly long with methodological explanation\n- Pythia-1B 3-class F1 > Pythia-2.8B but binary F1 reverses — undiscussed crossover\n- Generation failure rate (7.4% attrition from 40K to 37K) — causes not reported\n- Some bib entries missing pages/volume (stamatatos_survey, koppel_authorship)\n\n---\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| TOST misleading / Contribution 3 over-packaged | [AGREE] | [AGREE] | **Consensus** |\n| Gen-0 seed sharing inflates headline | [AGREE] | [AGREE] | **Consensus** |\n| Base-model + temperature = no real applicability | [AGREE] | [AGREE] | **Consensus** |\n| DDR \"shape preservation\" overstated | [AGREE] | [AGREE] | **Consensus** |\n| Cross-model 5-gen vs 8-gen inconsistency | [AGREE] | [AGREE] | **Consensus** |\n| \"Competitive performance\" overclaim | [AGREE] | [AGREE] | **Consensus** |\n| Temperature section title misleading | [AGREE] | [AGREE] | **Consensus** |\n| Spearman thresholds need citation | R1 raised | R2 [REBUT] (gap self-evident) | **Minor divergence** |\n| Method novelty insufficient | R1 [REBUT] partial | R2 [AGREE] critical | **Major divergence** |\n| Concurrent works need experimental comparison | R1 [REBUT] (infeasible) | R2 raised | **Minor divergence** |\n\n---\n\n## Reviewer Divergence\n\n**Novelty assessment** (the key divergence determining overall score):\n- **R1 (3.5)**: DDR as empirical finding + task formulation constitutes sufficient EMNLP contribution. Simple interpretable method is a feature, not a bug — enables the DDR decomposition insight.\n- **R2 (3.0)**: Two concurrent works (Broken Telephone, Markovian Chains) reduce novelty premium. Feature engineering + XGBoost has near-zero technical novelty. QLoRA already demonstrates superior performance. Better suited for Findings.\n\nBoth agree: if paper repositions clearly as **phenomenon characterization** (DDR analysis paper) rather than **method paper**, contribution level is appropriate for Findings acceptance.\n\n---\n\n## Questions for Authors\n\n1. Can you report a gen-0 hold-out experiment (per-generator independent seeds) to quantify true gen-0 generalization vs. seed memorization?\n2. What domain knowledge justifies the ±2% TOST margin? At what margin does equivalence first hold?\n3. Does cross-model F1=0.809 survive with 8 generators (including Mistral-7B)?\n4. In 8-gen setting, does a non-Pythia reference model (e.g., OLMo-2-1B) change the per-generator F1 ranking?\n5. Which factor dominates instruction-tuning's destruction of depth signal: length regulation, format constraints, or RLHF distribution shaping?\n6. Why do ordinal-specific methods (CORAL, Frank-Hall) provide zero improvement despite the task having ordinal structure?\n\n---\n\n## Missing References\n\n- Ordinal classification: proportional odds model, ordinal SVM, unimodal regularization (if framing as ordinal task, literature should be more comprehensive)\n- Multi-round LLM generation quality degradation studies beyond model collapse\n- Data contamination detection methods (overlap with provenance motivation)\n- R2 notes: concurrent works comparison could benefit from citing their specific experimental protocols\n\n---\n\n## External Review\n\n项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），未请求。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0–3.5 (Findings to Borderline Conference)**\n\n| Reviewer | Score | Rationale |\n|----------|-------|-----------|\n| R1 | 3.5 (Borderline Conference) | DDR insight + task novelty + exhaustive experiments sufficient for borderline acceptance |\n| R2 | 3.0 (Findings) | No method innovation + concurrent works + base-model-only = Findings-level |\n\n**Director's consolidated assessment: 3.0 (Findings)**\n\nRationale: The paper presents a genuine empirical finding (DDR) and a well-motivated task formulation. However, four factors push it below the main conference threshold:\n1. **Framing inconsistency**: Paper oscillates between \"practical detection system\" and \"phenomenon characterization\" without committing to either\n2. **Headline metrics inflated**: 3-class F1 biased by gen-0 leakage; Contribution 3 (TOST) is a null result over-packaged\n3. **Applicability gap**: Base-model-only + temperature sensitivity means the phenomenon, while interesting, cannot translate to any practical use case currently\n4. **Method contribution near zero**: Acknowledged by the paper itself (§2.1)\n\n**Recommendation**: Accept as **Findings** if MF1–MF3 are addressed (reframe positioning, fix headline metrics, demote TOST). For main conference, would need either (a) extension to instruction-tuned models or (b) deeper theoretical understanding of DDR mechanism.\n\n**Confidence**: 4/5 (both reviewers carefully evaluated all sections and appendices; statistical methodology scrutinized in detail)\n\n---\n\n## Detailed Comments by Section\n\n**Abstract**: Leads with biased 3-class numbers; uses \"equivalent\" for a null result; \"competitive performance\" overstates. Needs restructuring with binary F1 primary, scope qualification, honest downstream framing.\n\n**Introduction**: Web contamination motivation (§1 L1-5) creates expectation of practical tool, but scope is base-model laboratory study. Contribution 3 should be demoted. \"Competitive performance at substantially lower computational cost\" should be qualified.\n\n**Method (§3)**: Solid and clearly written. Minor issues: entropy misnomer (footnote insufficient), tail_decay range unjustified, entropy_min rationale weak, ordinal framing in §3.1 not substantiated by method.\n\n**Results (§4)**: Strong experimental design. Issues: §4.2 \"Temperature robustness\" title misleading; \"shape preservation\" language too strong given Levene results; 5-gen vs 8-gen subset mixing needs explicit explanation.\n\n**Discussion (§5)**: Over-fragmented with \\paragraph{} headers. Good content but needs consolidation into natural paragraphs. Cross-temperature transfer discussion should be more prominent.\n\n**Limitations**: Exceptionally thorough. Could add explicit statement that method is inapplicable in any real deployment scenario currently.\n\n**Related Work (§2)**: Well-structured with clear positioning. Ordinal classification discussion could be expanded. Concurrent works comparison is conceptual but adequate (direct experimental comparison infeasible due to different chain types).",
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 11 Consolidated Review Report\n\n**Paper**: \"Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\"\n**Target**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + Related Work)\n\n---\n\n## Summary\n\nThe paper formulates generation depth classification (gen-0/gen-1/gen-2+) as a new task beyond binary AI text detection, identifies a \"differential depth response\" (DDR) where central-tendency features drift monotonically with recursive generation depth while shape features remain near-stationary, and builds a 7-feature XGBoost ensemble achieving 3-class LOGO F1=0.762 across 8 base-model generators from 5 families. A TOST equivalence test suggests detected distributional shift does not translate to downstream perplexity degradation.\n\n---\n\n## Strengths\n\n1. **Novel and well-motivated task formulation**: Generation depth classification (gen-0/gen-1/gen-2+) fills a genuine gap between binary detection and source attribution. Independent convergence with two concurrent works (Broken Telephone, Markovian Chains) on ~3-class practical ceiling validates the research direction. [Unanimous]\n\n2. **DDR is a genuine scientific insight**: The drifting vs. stationary feature decomposition provides structured, interpretable understanding of recursive generation dynamics. The location-shift-preserving-shape hypothesis has theoretical elegance and empirical support (KS statistics show 10× magnitude gap). [Unanimous]\n\n3. **Exceptional experimental coverage**: LOGO/LOFO/cross-model/cross-reference/cross-temperature/cross-domain/cross-prompt/perturbation/length confound/classifier ablation/feature ablation/finer granularity/downstream utility — nearly every conceivable reviewer question is pre-addressed. Statistical methodology (bootstrap CI, McNemar, Bonferroni, TOST) exceeds average EMNLP standard. [Unanimous]\n\n4. **Honest self-criticism**: Paper proactively identifies gen-0 seed sharing bias, reports instruct model failure (F1=0.338), t=1.0 degradation, and provides leak-free binary metric. Limitations section is comprehensive and candid. [Unanimous]\n\n5. **Computational efficiency advantage**: Single 410M reference model (905 MB, 9.7 ms/text) vs. multi-detector ensembles (2 models, 2868 MB, 22.8 ms/text) with comparable binary F1. [Unanimous]\n\n6. **Writing quality and format compliance**: No AI writing artifacts (no em-dashes, no -ing phrase abuse, no excessive paragraphing). ACL style with [review] option, anonymous, line numbers, 8-page main text, Limitations section present. [R2 confirmed]\n\n---\n\n## Weaknesses\n\n### Must-Fix (影响接收决定)\n\n**MF1** [CONSENSUS — R1-N1 + R2-N1] **TOST equivalence test methodology flawed and Contribution 3 over-packaged**\n\nThe paper's third contribution claims \"depth-aware data selection yields training utility equivalent to random subsampling\" (Abstract L8). This is problematic on multiple levels:\n- Table 8 shows random subsampling **consistently outperforms** depth-aware (ppl 2.367 vs 2.387). Using \"equivalent\" is misleading when one method uniformly dominates.\n- TOST with n=3 seeds produces Cohen's d = 86–120, which the paper itself acknowledges as \"artificially inflated.\" Statistical power derives from extremely low seed-level variance, not genuine equivalence evidence.\n- The ±2% margin is not justified from domain knowledge. Table 9 shows equivalence fails at ±1% margin.\n- Fundamentally, this is a **null result**: the detected distributional shift has no practical downstream impact. Packaging this as a main contribution overstates its significance and paradoxically undermines the paper's data-curation motivation.\n\n**Required action**: (1) Demote from Contribution 3 to Discussion analysis finding; (2) Replace \"equivalent\" with \"does not substantially degrade\"; (3) Acknowledge random > depth-aware honestly; (4) Caveat n=3 limitation explicitly.\n\n---\n\n**MF2** [CONSENSUS — R1-N2 + R2-W2] **Gen-0 seed sharing inflates headline 3-class metric**\n\nAll 8 generators share identical ~1000 Wikipedia seeds as gen-0. In LOGO, held-out generator's gen-0 texts appear verbatim in training (via other generators' gen-0), creating direct train-test overlap. Evidence:\n- Confusion matrix: gen-0 recall = 99.4% vs. gen-1 = 75.0% vs. gen-2+ = 73.7%\n- 3-class macro F1 = 0.762 is upward-biased; the leak-free binary metric (gen-1 vs. gen-2+) = 0.694 is the trustworthy number\n- Despite paper correctly diagnosing this issue (§4.1 L8), Abstract/Introduction/Conclusion still lead with 3-class numbers (0.809, 0.762)\n\n**Required action**: (1) Abstract must lead with binary F1 (0.764 cross-model, 0.694 LOGO) as primary metric; (2) 3-class numbers demoted to secondary with explicit caveat; (3) Ideally: separate gen-0 seeds per generator to eliminate overlap entirely.\n\n---\n\n**MF3** [CONSENSUS — R1-N3 + R2-N3] **Base-model-only + temperature sensitivity = zero real-world applicability; framing mismatch**\n\nTwo independently devastating limitations stack:\n- **Instruct models**: OLMo-Instruct LOGO F1 = 0.338 (≈random baseline), Qwen3-0.6B-chat = 0.667. Real-world LLM text is overwhelmingly instruction-tuned.\n- **Temperature**: Cross-temperature transfer Qwen3-1.7B drops from 0.789 → 0.418. At t=1.0, entropy mean ρ collapses from -0.60 to -0.002. Many APIs default to t=1.0.\n- Combined: no real deployment scenario satisfies both base-model + known-temperature constraints.\n\nThe paper's Introduction motivates with web contamination (§1 L1-5) and §4.3 uses \"competitive performance at substantially lower computational cost\" — language implying deployment readiness. This creates a fundamental framing mismatch with the method's actual scope.\n\n**Required action**: (1) Reframe from \"detection/classification system\" to \"characterizing fundamental properties of recursive generation\"; (2) Remove deployment-implying language (\"competitive performance\"); (3) Explicit scope statement in Abstract (base models, standard decoding); (4) Deeper analysis of WHY instruction tuning destroys signal (which factor dominates: length regulation, format constraints, RLHF shaping?).\n\n---\n\n**MF4** [DIVERGENCE — R2-N2; R1 partial rebut] **Method novelty insufficient for main conference**\n\nR2 argues: 7 handcrafted features + off-the-shelf XGBoost constitutes zero algorithmic innovation. QLoRA (F1=0.905) demonstrates richer signal exists. CORAL/ordinal methods provide zero improvement. The paper's own §2.1 admission (\"not a new detection method\") confirms method contribution is negligible.\n\nR1 partially rebuts: (1) Paper is honestly self-positioned as task formulation + empirical finding; (2) Simple interpretable method enables DDR decomposition that neural approaches cannot; (3) EMNLP has precedent for empirical finding papers.\n\n**Director assessment**: The divergence is legitimate. If the paper clearly positions itself as an **analysis/phenomenon paper** (emphasizing DDR insight over classification pipeline), the contribution is appropriate for Findings. For main conference, methodological novelty or deeper theoretical understanding of DDR would be needed.\n\n---\n\n### Should-Fix (影响评分)\n\n**SF1** [CONSENSUS] **DDR \"shape preservation\" overstated**: Levene tests reject equal variance for ALL features including shape features (p < 10⁻¹⁰). \"Preserving distributional shape\" should be \"approximately preserving shape\" or quantified as \"order-of-magnitude smaller drift in shape features\" (CV shift <3% vs >15%).\n\n**SF2** [CONSENSUS] **Cross-model F1=0.809 uses 5-gen subset, not 8-gen**: Mistral-7B (LOGO binary F1=0.633, lowest) excluded from cross-model evaluation. The headline 0.809 may not hold with 8 generators. Must be prominently flagged as 5-gen result or re-run with full set.\n\n**SF3** [CONSENSUS] **\"Competitive performance\" claim**: Abstract overstates. 7-feature 3-cl F1=0.774 vs 4-det+surface 0.795 (2.1pp gap). Binary F1 difference negligible. Should say \"comparable binary performance at 2.4× lower cost.\"\n\n**SF4** [CONSENSUS] **Temperature section title misleading**: \"Temperature robustness\" paragraph actually documents a hard failure mode at t=1.0. Rename to \"Temperature sensitivity\" and discuss cross-temperature transfer failure prominently.\n\n**SF5** [CONSENSUS] **Pythia-410M reference model family bias**: Pythia generators achieve highest F1 (0.718-0.724) while reference model is Pythia family. Cross-reference spread (0.013) is on 5-gen subset only. Discuss architecture overlap in main text.\n\n**SF6** [R1 only, R2 agrees limited impact] **XGBoost hyperparameters fixed**: 200 trees depth=6 may be suboptimal for 1-dimensional single-score baselines. Report tuned results or simpler classifier sanity check.\n\n**SF7** [R2 only, R1 partial rebut] **Ordinal classification discussion insufficient**: §3.1 frames as ordinal task but main text never discusses why ordinal methods (CORAL, Frank-Hall) provide zero improvement. This is itself an interesting finding deserving explanation.\n\n---\n\n### Minor Issues\n\n- entropy_min retained \"for completeness\" (LOFO Δ=+0.01pp, i.e., removing slightly helps). Provide statistical justification or drop.\n- Figure 3 PNG format — regenerate as PDF for print quality\n- Appendix confusion matrix uses 6-gen, not aligned with Table 1 (8-gen)\n- Cross-domain evaluation uses t=1.0 while main experiment uses t=0.7 — add comparability note\n- \"Entropy\" misnomer (actually token-level NLL) clarified only in footnote — move to §3.3 opening\n- Tail decay rank range 100–1000 lacks theoretical motivation\n- Bonferroni correction application scope not fully specified (which comparisons, how many?)\n- Table 1 caption overly long with methodological explanation\n- Pythia-1B 3-class F1 > Pythia-2.8B but binary F1 reverses — undiscussed crossover\n- Generation failure rate (7.4% attrition from 40K to 37K) — causes not reported\n- Some bib entries missing pages/volume (stamatatos_survey, koppel_authorship)\n\n---\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| TOST misleading / Contribution 3 over-packaged | [AGREE] | [AGREE] | **Consensus** |\n| Gen-0 seed sharing inflates headline | [AGREE] | [AGREE] | **Consensus** |\n| Base-model + temperature = no real applicability | [AGREE] | [AGREE] | **Consensus** |\n| DDR \"shape preservation\" overstated | [AGREE] | [AGREE] | **Consensus** |\n| Cross-model 5-gen vs 8-gen inconsistency | [AGREE] | [AGREE] | **Consensus** |\n| \"Competitive performance\" overclaim | [AGREE] | [AGREE] | **Consensus** |\n| Temperature section title misleading | [AGREE] | [AGREE] | **Consensus** |\n| Spearman thresholds need citation | R1 raised | R2 [REBUT] (gap self-evident) | **Minor divergence** |\n| Method novelty insufficient | R1 [REBUT] partial | R2 [AGREE] critical | **Major divergence** |\n| Concurrent works need experimental comparison | R1 [REBUT] (infeasible) | R2 raised | **Minor divergence** |\n\n---\n\n## Reviewer Divergence\n\n**Novelty assessment** (the key divergence determining overall score):\n- **R1 (3.5)**: DDR as empirical finding + task formulation constitutes sufficient EMNLP contribution. Simple interpretable method is a feature, not a bug — enables the DDR decomposition insight.\n- **R2 (3.0)**: Two concurrent works (Broken Telephone, Markovian Chains) reduce novelty premium. Feature engineering + XGBoost has near-zero technical novelty. QLoRA already demonstrates superior performance. Better suited for Findings.\n\nBoth agree: if paper repositions clearly as **phenomenon characterization** (DDR analysis paper) rather than **method paper**, contribution level is appropriate for Findings acceptance.\n\n---\n\n## Questions for Authors\n\n1. Can you report a gen-0 hold-out experiment (per-generator independent seeds) to quantify true gen-0 generalization vs. seed memorization?\n2. What domain knowledge justifies the ±2% TOST margin? At what margin does equivalence first hold?\n3. Does cross-model F1=0.809 survive with 8 generators (including Mistral-7B)?\n4. In 8-gen setting, does a non-Pythia reference model (e.g., OLMo-2-1B) change the per-generator F1 ranking?\n5. Which factor dominates instruction-tuning's destruction of depth signal: length regulation, format constraints, or RLHF distribution shaping?\n6. Why do ordinal-specific methods (CORAL, Frank-Hall) provide zero improvement despite the task having ordinal structure?\n\n---\n\n## Missing References\n\n- Ordinal classification: proportional odds model, ordinal SVM, unimodal regularization (if framing as ordinal task, literature should be more comprehensive)\n- Multi-round LLM generation quality degradation studies beyond model collapse\n- Data contamination detection methods (overlap with provenance motivation)\n- R2 notes: concurrent works comparison could benefit from citing their specific experimental protocols\n\n---\n\n## External Review\n\n项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），未请求。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0–3.5 (Findings to Borderline Conference)**\n\n| Reviewer | Score | Rationale |\n|----------|-------|-----------|\n| R1 | 3.5 (Borderline Conference) | DDR insight + task novelty + exhaustive experiments sufficient for borderline acceptance |\n| R2 | 3.0 (Findings) | No method innovation + concurrent works + base-model-only = Findings-level |\n\n**Director's consolidated assessment: 3.0 (Findings)**\n\nRationale: The paper presents a genuine empirical finding (DDR) and a well-motivated task formulation. However, four factors push it below the main conference threshold:\n1. **Framing inconsistency**: Paper oscillates between \"practical detection system\" and \"phenomenon characterization\" without committing to either\n2. **Headline metrics inflated**: 3-class F1 biased by gen-0 leakage; Contribution 3 (TOST) is a null result over-packaged\n3. **Applicability gap**: Base-model-only + temperature sensitivity means the phenomenon, while interesting, cannot translate to any practical use case currently\n4. **Method contribution near zero**: Acknowledged by the paper itself (§2.1)\n\n**Recommendation**: Accept as **Findings** if MF1–MF3 are addressed (reframe positioning, fix headline metrics, demote TOST). For main conference, would need either (a) extension to instruction-tuned models or (b) deeper theoretical understanding of DDR mechanism.\n\n**Confidence**: 4/5 (both reviewers carefully evaluated all sections and appendices; statistical methodology scrutinized in detail)\n\n---\n\n## Detailed Comments by Section\n\n**Abstract**: Leads with biased 3-class numbers; uses \"equivalent\" for a null result; \"competitive performance\" overstates. Needs restructuring with binary F1 primary, scope qualification, honest downstream framing.\n\n**Introduction**: Web contamination motivation (§1 L1-5) creates expectation of practical tool, but scope is base-model laboratory study. Contribution 3 should be demoted. \"Competitive performance at substantially lower computational cost\" should be qualified.\n\n**Method (§3)**: Solid and clearly written. Minor issues: entropy misnomer (footnote insufficient), tail_decay range unjustified, entropy_min rationale weak, ordinal framing in §3.1 not substantiated by method.\n\n**Results (§4)**: Strong experimental design. Issues: §4.2 \"Temperature robustness\" title misleading; \"shape preservation\" language too strong given Levene results; 5-gen vs 8-gen subset mixing needs explicit explanation.\n\n**Discussion (§5)**: Over-fragmented with \\paragraph{} headers. Good content but needs consolidation into natural paragraphs. Cross-temperature transfer discussion should be more prominent.\n\n**Limitations**: Exceptionally thorough. Could add explicit statement that method is inapplicable in any real deployment scenario currently.\n\n**Related Work (§2)**: Well-structured with clear positioning. Ordinal classification discussion could be expanded. Concurrent works comparison is conceptual but adequate (direct experimental comparison infeasible due to different chain types).",
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-17T17:35:23.184646+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3813
}
```

</details>

---


### Assistant

_source line 584 · 2026-05-17T17:35:34.868645+00:00_

---

**审稿圆桌会议 Round 11 完成。**

汇总报告已投递至 Research Director。核心结论：

**评分：3.0 (Findings)**

4 个 Must-Fix 共识问题：
1. **TOST/Contribution 3**：null result 过度包装为主要贡献，统计方法论有缺陷
2. **Gen-0 seed sharing**：3-class headline metric 系统性高估，binary F1 应为 primary
3. **实用性 framing**：base-model + temperature 双重限制 = 无实际部署场景，需重定位为 phenomenon characterization
4. **方法新颖性**（分歧）：R1 认为 DDR insight 足够，R2 认为 feature engineering + XGBoost 无技术贡献

**建议路径**：修复 MF1-3（reframe positioning + fix metrics + demote TOST），以 Findings 接收。升级到主会议需要 instruct model 扩展或 DDR 理论深化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 585 · 2026-05-17T17:35:37.432453+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **N1-N3**: 三条 Must-Fix 全部 [AGREE]，与我的独立审稿发现高度一致
- **W1, W3-W5**: 四条 [AGREE]
- **W2** (Spearman 阈值): 唯一的 [REBUT]——DDR 核心论证依赖 6-10× magnitude gap 而非特定阈值标签，加标准引用是 easy fix 但非 should-fix 级别
- **整体评分差异**: R1 给 3.5 (Borderline Conference)，我给 3 (Findings)，主要分歧在于我对 concurrent works 降低的 novelty premium 和 method 层面零创新给了更多负面权重

三个共识性 critical issues 已明确标注供 Director 参考。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 586 · 2026-05-17T17:35:53.083961+00:00_

---

## 审稿完成

Round 11 圆桌审稿已结束，报告已投递至 Research Director。

**最终评分**: 3.0 (Findings)

**核心共识** (R1 + R2 unanimous):
1. TOST 等价性测试方法学有缺陷，Contribution 3 应降级为 analysis finding
2. Gen-0 seed sharing 导致 3-class headline metric 偏高，binary F1 应为 primary
3. Base-model-only + temperature sensitivity 叠加 = 无实际部署场景，需重新定位为 phenomenon characterization

**唯一分歧**: 方法新颖性（R1: DDR insight 够 borderline conference; R2: 零算法创新 + concurrent works → Findings only）

**建议**: 以 Findings 接收，前提是修复 framing（定位为 DDR 现象研究而非实用检测方案）、修正 headline metrics、诚实处理 downstream null result。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 60

## Round 60

62 recorded events


### User

_source line 587 · 2026-05-17T18:01:58.742086+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-17T18:02:04.604835+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-17T18:02:04.606123+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-17T18:02:09.021855+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,director_post_to_reviewer,WebSearch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,director_post_to_reviewer,WebSearch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-17T18:02:09.022302+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-17T18:02:11.792008+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,director_post_to_reviewer",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,director_post_to_reviewer",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-17T18:02:11.842512+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-17T18:02:15.154085+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-17T18:02:15.154416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-17T18:02:19.823282+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-17T18:02:21.128407+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (50 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- multi_domain_t07（准备中）\n- review-exp-a-baseline-ensemble: 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异（准备中）\n- plan-004-prep: Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）（准备中）\n- plan-001-restore（准备中）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **exp_048_cross_temp_transfer** (success): Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters ← 基于 exp_047_multi_domain_t07\n- **exp_047_multi_domain_t07** (success): Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers ← 基于 exp_043_multi_domain_seeds\n- **multi-domain-seeds** (success): Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Aca
…[truncated 628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-17T18:02:21.681154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-17T18:02:22.233810+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{lineno}
11	\linenumbers
12	
13	\graphicspath{{../chart/}}
14	
15	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in LLM Text Chains}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{results}
28	
29	\input{discussion}
30	\input{conclusion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\appendix
37	
38	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
39	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
40	
41	\input{appendix_dataset_stats}
42	
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{End-to-End Depth Classification (QLoRA)}
56	\label{app:qlora}
57	\input{appendix_qlora}
58	
59	\section{Leave-One-Feature-Out Analysis}
60	\label{app:lofo}
61	\input{appendix_lofo}
62	
63	\section{Confusion Matrix}
64	\label{app:confusion}
65	\input{appendix_confusion_matrix}
66	
67	\section{Classifier Sensitivity}
68	\label{app:classifier}
69	\input{appendix_classifier}
70	
71	\section{Robustness to Text Perturbation}
72	\label{app:human-edit}
73	\input{appendix_human_edit}
74	
75	\section{Cross-Domain Generalization}
76	\label{app:domain}
77	\input{appendix_domain}
78	
79	\section{Error Analysis of Binary Classifica
…[truncated 542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-17T18:02:22.936898+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-17T18:02:23.439247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-17T18:02:23.590621+00:00_

1	- id: "R1-W1"
2	  summary: "Baseline hyperparameter inconsistency"
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 8
8	  resolution: "method.tex unified to est200/md6. Verified R8."
9	  resolution_round: 8
10	
11	- id: "R1-W5"
12	  summary: "Downstream experiment too small"
13	  category: framing
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 8
18	  resolution: "TOST added. Contribution 3 restored with perplexity scope."
19	  resolution_round: 8
20	
21	- id: "R7-W1"
22	  summary: "gen-0 seed sharing inflating headline"
23	  category: experiment
24	  severity: critical
25	  status: in_progress
26	  first_raised_round: 7
27	  last_seen_round: 12
28	  mentions:
29	    - {round: 9, reviewers: "R1,R2", note: "Abstract reports both binary and 3-class."}
30	    - {round: 10, reviewers: "R1,R2", note: "Recurred as R10-N1."}
31	    - {round: 11, reviewers: "R1,R2", note: "Abstract still leads with 3-class."}
32	    - {round: 12, reviewers: "R1,R2", note: "Abstract now binary-first but Intro still 3-class-first. Both 0.809 and 0.762 have gen-0 sharing."}
33	  action_items:
34	    - {round: 10, action: "Use leak-free binary F1 as headline", assigned_to: "Paper Agent", status: "done"}
35	    - {round: 11, action: "Abstract lead with binary", assigned_to: "Paper Agent", status: "done"}
36	    - {round: 12, action: "Intro restructured to binary-first; all 0.809 refs tagged (five-generator subset); Conclusion adds gen-0 caveat", assigned_to: "Director", status: "done"}
37	  resolution: ""
38	  resolution_round: null
39	
40	- id: "R7-W2"
41	  summary: "DDR mechanism overclaim — 'preserving shape' vs Levene test rejection"
42	  category: method
43	  severity: warning
44	  status: in_progress
45	  first_raised_round: 7
46	  last_seen_round: 12
47	  mentions:
48	    - {round: 11, reviewers: "R1,R2", note: "Levene rejects for all 7 features. CV <3% vs >15%."}
49	    - {
…[truncated 20698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-17T18:02:28.713616+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"Call for Papers: NLP for Science Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/nlp-science"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"[Call for participation] Present your Findings of EMNLP paper at the NLP4MusA (NLP for Music and Audio) workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-present-your-findings-emnlp-paper-nlp4musa-nlp-music-and-audio-workshop"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"}]

Based on my search results, I found information about EMNLP 2026 calls for tutorials and workshops, but I did not find a dedicated main call f
…[truncated 1093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5776
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-17T18:02:38.024639+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limits author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limits author instructions"
  }
}
```

</details>

---


### Tool call

_source line 605 · 2026-05-17T18:02:39.085202+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline May 2026"
  }
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-17T18:02:39.838643+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-17T18:02:43.607271+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

Based on the search results, here is the key information about EMNLP 2026 ARR submission deadlines
…[truncated 794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 4522
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-17T18:02:45.112762+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limits author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, I found information about ACL Rolling Review 2026 submission guidelines. Here are the key details:

## Submission Guidelines

The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template. Starting in May 2025, all submitting authors have to also sign up as reviewers (dea
…[truncated 1237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 7088
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-17T18:02:45.113414+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml\", \"content\": \"_next_id: 21\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:15 UTC\\n  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class\\n    分类\\n  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost\\n    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 18:10 UTC\\n  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证\\n  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer\\n    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth\\n    信号超越 binary 分类的增量。\\n  related_experiments:\\n  - exp_id: mvp-001\\n    role: primary\\n    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 18:15 UTC\\n  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 \\\"independent signal\\\"\\n    调整为 \\\"complementary signal\\\"\\n  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio\\n    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从\\\"分布指纹独立于表面统计\\\"降为\\\"分布指纹提供互补信号\\\"，核心叙事转为\\n    vocabulary impoverishment as primary depth signal。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 \\\"Feature Complementarity\\n    & Dual Dynamics\\\"；H1/H2 从二选一转为共存\\n  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full\\n    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 \\\"independent signal\\\" 被否定，触发 Plan\\n    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing\\n    更丰富的科学贡献。\\n  related_experiments:\\n  - exp_id: p
…[truncated 1488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5274
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-17T18:02:51.386309+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers main conference long short paper page limits site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers main conference long short paper page limits site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-17T18:02:52.240072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 long paper 8 pages short paper 4 pages template overleaf site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 long paper 8 pages short paper 4 pages template overleaf site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-17T18:02:52.491619+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-17T18:02:54.952798+00:00_

Web search results for query: "EMNLP 2026 call for papers main conference long short paper page limits site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

Based on the search results from the EMNLP 2026 official website, here are the page limits for main conference papers:

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

This means the initial submission page limits are 8 pages for long papers and 4 pages for short papers, with one additional page allowed in the camera-ready (final) version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 3566
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-17T18:02:55.656810+00:00_

Web search results for query: "ACL Rolling Review 2026 long paper 8 pages short paper 4 pages template overleaf site:aclrollingreview.org"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Discontinuation of the MS Word Template – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/discontinuation-word-template"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results from aclrollingreview.org, here's the in
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 3416
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-17T18:02:55.707456+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3215
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-17T18:03:21.120640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-17T18:03:21.623209+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	LLM-generated text increasingly re-enters the web and seeds subsequent generation, producing recursive chains whose outputs progressively diverge from human-written text.
4	We ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Studying eight base models from five families, we identify a \emph{differential depth response} (DDR): central-tendency features (mean entropy, lexical diversity) drift monotonically with generation depth, while shape features (entropy max, vocabulary tail slope) remain near-stationary.
6	This pattern is consistent with a location shift in the token-level negative log-likelihood (NLL) distribution that approximately preserves distributional shape.
7	Exploiting this complementarity, a 7-feature ensemble achieves binary F1\,=\,0.764 on heterogeneous cross-model chains (3-class macro F1\,=\,0.809; five-generator subset) and binary F1\,=\,0.694 under eight-generator leave-one-generator-out (LOGO) evaluation, with comparable binary performance at 2.4$\times$ lower computational cost than multi-detector alternatives.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-17T18:03:21.673844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-17T18:03:21.674333+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-generated text increasingly re-enters the web and seeds subsequent generation \cite{dolma,fineweb}, with estimates suggesting that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}.
5	The result is recursive generation chains whose outputs progressively diverge from human-written text.
6	Understanding how distributional features evolve across recursive generation depths is a fundamental question for characterizing recursive generation dynamics, yet existing methods \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions, conflating qualitatively different material: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	
8	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and refer to the overall framework as \emph{depth fingerprinting}.
9	No existing method addresses this task in non-paraphrastic continuation chains.
10	
11	The key finding is a \emph{differential depth response} (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) remain near-stationary.
12	This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution while approximately preserving its shape: the softmax architecture and fixed sampling parameters constrain distributional shape under standard decoding regimes, while each successive ge
…[truncated 1907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-17T18:03:22.076332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-17T18:03:22.127144+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig2_framework.pdf}
7	\caption{Depth fingerprinting framework. (a)~Recursive generation chains are constructed by iteratively feeding text through a generator $G$. (b)~Seven features are extracted per text: five NLL statistics from a Pythia-410M reference model and two surface diversity measures. Horizontal bars show Spearman $\rho$ with generation depth, revealing differential depth response: drifting features ($|\rho| > 0.6$) capture the monotonic location shift, while stationary features ($|\rho| < 0.1$) provide a stable baseline. (c)~An XGBoost classifier trained under Leave-One-Generator-Out (LOGO) cross-validation predicts depth class (gen-0\,/\,gen-1\,/\,gen-2+).}
8	\label{fig:framework}
9	\end{figure*}
10	
11	\subsection{Task Formulation}
12	\label{sec:task}
13	
14	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
15	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
16	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
17	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
18	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
19	
20	\subsection{Generation Chain Construction}
21	\label{sec:generation}
22	
23	We construct generation chains using eight gen
…[truncated 8774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-17T18:03:30.312634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-17T18:03:30.814849+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), the 3-class metric may carry upward bias from memorized gen-0 patterns; we therefore also report a leak-free binary metric (gen-1 vs.\ gen-2+): F1\,=\,0.694, CI [0.688, 0.700], which is unaffected by this sharing.
9	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B); the primary difficulty is distinguishing gen-1 from gen-2+ (Appendix~\ref{app:confusion}).
10	Larger generators show moderate degradation (Qwen3-8B: 0.692, Mistral-7B: 0.633) relative to the 0.694 average.
11	The Pythia-1B/2.8B crossover between three-class and binary scores (0.806 vs.\ 0.798 and 0.718 vs.\ 0.724, respectively) reflects differences in gen-0 classification accuracy rather than in depth discrimination per se.
12	
13	\paragraph{Cross-model generalization.}
14	Cross-model chains (randomly selected generator per step) yield 3-class F1\,=\,0.809 and binary F1\,=\,0.764 under 5-fold CV,\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists when text passes through heterogeneous generators.
15	The higher cross-model performance relative to single-generator LOGO (3-class: 0.809 vs.\ 0.762) suggests that generator heterogeneity amplifies distributional shifts between depths, making each recursive step more distinct.
16	Under class balancing, macro F1 reaches 0.831 (per-class breakdown in Appendix~\ref{app:cross-model-detail}).
17	
18	Leave-one-family-out (LOFO) evaluation yields average binary F1\,=\,0.686, confirming transfer across architectural fa
…[truncated 9664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-17T18:03:30.815210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-17T18:03:31.116630+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The near-stationarity of shape features across recursive depths is consistent with the softmax architecture and fixed sampling parameters constraining distributional shape: recursive generation shifts context toward high-probability regions without altering the generation mechanism itself.
5	One hypothesis is that standard decoding regimes inherently preserve the functional form of the NLL distribution while allowing its location to drift.
6	Sampling ablation supports this as a tendency rather than an architectural guarantee ($t \in [0.5, 0.7]$: ${\leq}0.3$\,pp degradation; $t = 1.0$: $-6$\,pp; Appendix~\ref{app:sampling-sensitivity}).
7	Prompt-type dependence further modulates the effect: semantic-preservation constraints attenuate drift (elaboration F1\,=\,0.730 vs.\ continuation 0.781; Appendix~\ref{app:prompt-type}), consistent with \citet{broken_telephone} showing that tasks anchoring the output distribution to the input leave less room for recursive drift to accumulate.
8	Cross-type transfer remains viable (F1\,=\,0.753).
9	
10	At the document level, gen-1 per-class F1\,=\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\sqrt{n})$.
11	The gen-1\,/\,gen-2+ boundary concentrates 86\% of binary errors as false negatives (gen-2+ predicted as gen-1), with depth-2 error rate at 48\% vs.\ 20\% for depth-4, consistent with DDR predictions that the first recursive step produces the smallest location shift; larger generators exacerbate this (Mistral-7B error rate 45\% vs.\ Pythia-1B 18\%; Appendix~\ref{app:error-analysis}).
12	Reference-model family bias is limited: Pythia generators show slightly higher F1 with the Pythia-410M reference, but cross-reference spread is only 0.013\,pp (Table~\ref{tab:cross-ref}).
13	Cross-temperature transfer presents a more significant limitation: classifiers trained at $t{=}0.7$ degrade substantially when tested at $t{=
…[truncated 1748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-17T18:03:31.117001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-17T18:03:31.167470+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
12	Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
13	Our contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance.
14	This is orthogonal to source attribution \cite{uchendu_attribution,munir_looking_glass}, which identifies \emph{which} model generated text; our LOGO
…[truncated 4237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-17T18:03:36.466153+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-17T18:03:37.019019+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and documented a differential depth response across eight base-model generators from five families: recursive generation is consistent with a systematic location shift in the token-level NLL distribution that approximately preserves distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (binary F1\,=\,0.764 on cross-model chains, 0.694 under LOGO; 3-class: 0.809 and 0.762 on five- and eight-generator subsets, respectively, noting that 3-class metrics carry upward bias from shared gen-0 seeds).
5	Preliminary downstream evaluation suggests that this distributional shift does not substantially degrade training utility as measured by perplexity (\S\ref{sec:results-downstream}), though the evidence is limited (three seeds, single metric).
6	
7	Two boundaries define the scope: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.
8	All code, data, and trained models will be released upon publication.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-17T18:03:37.019378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-17T18:03:37.220353+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 under a 7-generator split).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary e
…[truncated 2124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-17T18:03:37.220728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-17T18:03:37.271202+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	
10	\paragraph{Licenses.}
11	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
12	Wikipedia seed passages are distributed under CC BY-SA 3.0.
13	
14	\paragraph{Compute budget.}
15	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
16	
17	\paragraph{Software.}
18	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-17T18:03:42.459666+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-17T18:03:43.012267+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml\", \"content\": \"# Literature Map for gen-depth-fingerprint\\n# 递归 LLM 生成链深度指纹识别\\n# Updated: 2026-05-15\\n# Categories: detection, model-collapse, data-quality, stylometry,\\n#             iterative-generation, watermarking, vocabulary-diversity,\\n#             membership-inference, ood-detection, survey\\n# Total: 39 papers\\n\\n##############################################################################\\n# 1. Perplexity-based / Zero-shot Detection\\n##############################################################################\\n\\n- id: detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Mitchell et al.\\\"\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  arxiv: \\\"2301.11305\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补\\\"\\n  key_finding: \\\"机器生成文本倾向于占据模型 log-probability 函数的负曲率区域\\\"\\n\\n- id: gltr\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: \\\"Gehrmann et al.\\\"\\n  year: 2019\\n  venue: \\\"ACL 2019\\\"\\n  arxiv: \\\"1906.04043\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化\\\"\\n  key_finding: \\\"使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%\\\"\\n\\n- id: dna_gpt\\n  title: \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\"\\n  authors: \\\"Yang et al.\\\"\\n  year: 2024\\n  venue: \\\"ICLR 2024\\\"\\n  arxiv: \\\"2305.17359\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析\\\"\\n  key_finding: \\\"截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测\\\"\\n\\n- id: binoculars\\n  tit
…[truncated 1705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-17T18:03:43.213519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-17T18:03:43.264152+00:00_

1	\begin{table}[t]
2	\centering
3	\footnotesize
4	\resizebox{\linewidth}{!}{%
5	\begin{tabular}{llccc}
6	\toprule
7	\textbf{Reference} & \textbf{Family} & \textbf{Params} & \textbf{LOGO F1} & \textbf{Ent.\ Drift} \\
8	\midrule
9	Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
10	OLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\
11	Qwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\
12	\bottomrule
13	\end{tabular}}
14	\caption{Cross-family reference model validation (5-gen LOGO subset). Drift direction is consistent (negative) across all three references; magnitude varies with capacity. Spread in LOGO F1 is 0.013.}
15	\label{tab:cross-ref}
16	\end{table}
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-17T18:03:43.264471+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-fingerprint/**/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-fingerprint/**/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-17T18:03:43.264659+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-17T18:03:48.888369+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-fingerprint/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-fingerprint/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-17T18:03:48.989391+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/review_context.yaml
/home/ubuntu/.age
…[truncated 3222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-17T18:03:54.865763+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-17T18:03:54.916388+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-17T18:04:44.757891+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）\n\n### 论文信息\n- **标题**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 via ARR May cycle（Findings track）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- Long paper ≤ 8 页正文（References/Limitations/Ethics/Appendix 不计入）\n- ACL 2023 LaTeX 模板，`[review]` 选项\n- Double-blind（匿名）\n- 行号必须开启\n- Responsible NLP Checklist\n\n### 你的审查侧重\n\n请重点审查以下方面：\n\n1. **实验设计**：\n   - gen-0 seed sharing 在 LOGO 评估中的数据泄露风险——论文是否充分处理和披露了这个问题？\n   - Leave-One-Generator-Out (LOGO) 和 Leave-One-Family-Out (LOFO) 的评估方案是否严谨？\n   - 8 个生成器的选择是否有代表性？规模范围（0.6B-8B）是否足够？\n   - 仅用 base model 而非 instruct model 的实验设计选择是否合理？\n\n2. **统计检验**：\n   - Bonferroni 校正的适用范围是否明确？\n   - Bootstrap CI、McNemar test、paired bootstrap 的使用是否恰当？\n   - DDR 的 Spearman ρ 阈值（|ρ|>0.60 vs <0.10）是否有统计依据？\n   - Levene test 结果（所有特征都 reject 等方差）与\"approximately preserves shape\"的 claim 是否矛盾？\n\n3. **Baseline 公平性**：\n   - 所有方法使用相同 XGBoost 配置——这对单特征 baseline 是否公平？\n   - 4-detector ensemble 的对比是否控制了计算成本？\n\n4. **Downstream utility**：\n   - n=3 seeds 的 TOST 分析统计功效如何？\n   - \"depth composition doesn't matter\" 的 null result 结论是否 justified？\n\n5. **可复现性**：\n   - 超参数、随机种子、数据处理流程是否完整披露？\n   - 37,058 texts 的数据集构建过程是否可复现？\n\n请按 ARR review form 结构输出：Summary → Strengths → Weaknesses（标注 severity: Must-Fix / Should-Fix / Minor）→ Questions → Overall Assessment。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）\n\n### 论文信息\n- **标题**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 via ARR May cycle（Findings track）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- Long paper ≤ 8 页正文（References/Limitations/Ethics/Appendix 不计入）\n- ACL 2023 LaTeX 模板，`[review]` 选项\n- Double-blind（匿名）\n- 行号必须开启\n- Responsible NLP Checklist\n\n### 你的审查侧重\n\n请重点审查以下方面：\n\n1. **实验设计**：\n   - gen-0 seed sharing 在 LOGO 评估中的数据泄露风险——论文是否充分处理和披露了这个问题？\n   - Leave-One-Generator-Out (LOGO) 和 Leave-One-Family-Out (LOFO) 的评估方案是否严谨？\n   - 8 个生成器的选择是否有代表性？规模范围（0.6B-8B）是否足够？\n   - 仅用 base model 而非 instruct model 的实验设计选择是否合理？\n\n2. **统计检验**：\n   - Bonferroni 校正的适用范围是否明确？\n   - Bootstrap CI、McNemar test、paired bootstrap 的使用是否恰当？\n   - DDR 的 Spearman ρ 阈值（|ρ|>0.60 vs <0.10）是否有统计依据？\n   - Levene test 结果（所有特征都 reject 等方差）与\"approximately preserves shape\"的 claim 是否矛盾？\n\n3. **Baseline 公平性**：\n   - 所有方法使用相同 XGBoost 配置——这对单特征 baseline 是否公平？\n   - 4-detector ensemble 的对比是否控制了计算成本？\n\n4. **Downstream utility**：\n   - n=3 seeds 的 TOST 分析统计功效如何？\n   - \"depth composition doesn't matter\" 的 null result 结论是否 justified？\n\n5. **可复现性**：\n   - 超参数、随机种子、数据处理流程是否完整披露？\n   - 37,058 texts 的数据集构建过程是否可复现？\n\n请按 ARR review form 结构输出：Summary → Strengths → Weaknesses（标注 severity: Must-Fix / Should-Fix / Minor）→ Questions → Overall Assessment。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-17T18:05:00.768507+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16010
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-17T18:05:01.170908+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 via ARR May cycle（Findings track）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- Long paper ≤ 8 页正文（References/Limitations/Ethics/Appendix 不计入）\n- ACL 2023 LaTeX 模板，`[review]` 选项\n- Double-blind（匿名）\n- 行号必须开启\n- Responsible NLP Checklist\n\n### 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与定位**：\n   - \"generation depth classification\" 作为新任务的贡献是否足够？\n   - DDR（differential depth response）是否构成真正的发现，还是已知现象的重新包装？\n   - 方法本身（7 个标准特征 + XGBoost）的技术新颖性如何？\n   - 论文定位为 \"phenomenon paper\"（实证贡献为主）是否 Findings-appropriate？\n   - 与 Geng et al. (broken_telephone) 和 Markovian chains 的区分是否清晰？\n\n2. **Related Work 覆盖度**：\n   - 引用是否充分覆盖：直接相关方法、baseline 论文、评测 benchmark、理论基础？\n   - 是否有重要遗漏的相关工作？特别关注 2025-2026 年的新工作\n   - 与 model collapse 文献的区分是否准确？\n\n3. **论文结构与叙事**：\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 的主线是否统一？\n   - \"twofold contributions\" 是否与正文内容一致？\n   - Downstream utility（§4.4）作为 null result 在论文中的定位是否合理？\n   - Limitations 是否全面、诚实？\n\n4. **写作质量**：\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、过渡词堆砌）？\n   - 专有名词是否首次出现时有定义？\n   - 代词/指示词的指代是否明确？\n   - 图表 caption 是否自包含？\n\n5. **格式合规**：\n   - 页数是否在 8 页限制内？\n   - 匿名化是否完整（无自引泄露）？\n   - bib 条目是否完整（作者、标题、venue、年份、pages）？\n   - 图表字体是否 ≥7pt？\n   - 图片格式（PDF vs PNG）？\n\n请按 ARR review form 结构输出：Summary → Strengths → Weaknesses（标注 severity: Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026 via ARR May cycle（Findings track）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求\n- Long paper ≤ 8 页正文（References/Limitations/Ethics/Appendix 不计入）\n- ACL 2023 LaTeX 模板，`[review]` 选项\n- Double-blind（匿名）\n- 行号必须开启\n- Responsible NLP Checklist\n\n### 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与定位**：\n   - \"generation depth classification\" 作为新任务的贡献是否足够？\n   - DDR（differential depth response）是否构成真正的发现，还是已知现象的重新包装？\n   - 方法本身（7 个标准特征 + XGBoost）的技术新颖性如何？\n   - 论文定位为 \"phenomenon paper\"（实证贡献为主）是否 Findings-appropriate？\n   - 与 Geng et al. (broken_telephone) 和 Markovian chains 的区分是否清晰？\n\n2. **Related Work 覆盖度**：\n   - 引用是否充分覆盖：直接相关方法、baseline 论文、评测 benchmark、理论基础？\n   - 是否有重要遗漏的相关工作？特别关注 2025-2026 年的新工作\n   - 与 model collapse 文献的区分是否准确？\n\n3. **论文结构与叙事**：\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 的主线是否统一？\n   - \"twofold contributions\" 是否与正文内容一致？\n   - Downstream utility（§4.4）作为 null result 在论文中的定位是否合理？\n   - Limitations 是否全面、诚实？\n\n4. **写作质量**：\n   - 是否存在 AI 写作痕迹（em-dash、-ing phrases、过度分段、过渡词堆砌）？\n   - 专有名词是否首次出现时有定义？\n   - 代词/指示词的指代是否明确？\n   - 图表 caption 是否自包含？\n\n5. **格式合规**：\n   - 页数是否在 8 页限制内？\n   - 匿名化是否完整（无自引泄露）？\n   - bib 条目是否完整（作者、标题、venue、年份、pages）？\n   - 图表字体是否 ≥7pt？\n   - 图片格式（PDF vs PNG）？\n\n请按 ARR review form 结构输出：Summary → Strengths → Weaknesses（标注 severity: Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-17T18:05:02.528472+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1357
}
```

</details>

---


### Assistant

_source line 648 · 2026-05-17T18:05:08.075929+00:00_

Round 1 已启动。两名 Reviewer 均已收到任务：

- **Reviewer 1**（方法严谨性 + 实验验证）：聚焦 gen-0 泄露、LOGO 评估方案、统计检验、baseline 公平性、downstream utility 的 n=3 问题
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：聚焦 novelty positioning、related work 覆盖度、叙事一致性、AI 写作痕迹、格式合规

等待两位 Reviewer 返回独立审稿意见后，将进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 649 · 2026-05-17T18:16:19.018984+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 1 审稿报告

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains
**Venue**: EMNLP 2026 via ARR (Findings track target)
**审查侧重**: 方法严谨性 + 实验验证

---

## Summary

本文提出 generation depth classification 任务：给定一段文本，判断其经历了多少轮 LLM 递归生成（d=0 人类原文, d=1 一次生成, d=2+ 多次递归）。作者构建了 8 个 base model（0.6B–8B, 5 个 family）的 37,058 条递归生成链数据集，提取 7 个基于 reference model NLL 的统计特征，用 XGBoost 分类器在 Leave-One-Generator-Out (LOGO) 评估下达到 3-class macro F1=0.762。核心分析发现是 Differential Depth Response (DDR)：递归生成使 NLL 分布发生 location shift（中心性/多样性特征单调漂移），但 distributional shape 近似保持（entropy max, tail decay 等近似平稳）。

---

## Strengths

**S1. 任务定义新颖且有意义。** 将 binary AI detection 扩展到 depth classification 是一个自然但此前未被系统研究的方向，对理解 web 上递归合成内容的"深度污染"具有现实意义（Section 1, §3.1）。

**S2. DDR 分析框架有洞察力。** 将 7 个特征分解为 drifting（|ρ|>0.60，单调漂移）和 stationary（|ρ|<0.10，近似平稳）两组，揭示了递归生成对 NLL 分布的结构化影响，超越了简单的 perplexity 阈值检测（Figure 2, §4.2）。

**S3. 评估方案全面。** LOGO 8-fold、LOFO 5-family、cross-model chains、cross-domain（Appendix J）、perturbation robustness（Appendix I）、length confound（Appendix B）、temperature sensitivity（Appendix H）、classifier ablation（Appendix K）、confusion matrix 分析（Appendix G）——覆盖面广。

**S4. 轻量高效。** 仅需单个 Pythia-410M reference model + 7 个手工特征，计算成本远低于 multi-detector ensemble（论文称 2.4× 差异），实用性强。

**S5. 引用完整无幽灵。** 58 条 bib 条目全部被引用，无 orphan/missing，在线验证 48/58 confirmed（其余为 OpenAlex 索引问题，非真实性问题）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] §3.2 温度参数存在内部矛盾——核心可复现性缺陷

- **具体位置**: §3.2 (page 4) vs. Limitations (page 9) vs. Appendix H/O (page 16, 20)
- **问题**: §3.2 明确写道 *"All generation uses temperature = 0, nucleus sampling with p = 0.9"*，但 Limitations 部分写 *"Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus p = 0.9)"*。Appendix O 进一步确认默认温度为 0.7（"remaining five generators retain t = 0.7"）。此外，temperature=0 本身是 greedy decoding，此时 nucleus sampling p=0.9 无实际效果，两者同时声明本身就矛盾。
- **为什么影响接收**: 解码参数是实验的最基础设定。如果复现者按 §3.2 使用 temperature=0（greedy），将得到与论文完全不同的数据和结果。这直接损害 reproducibility。
- **建议**: 确认实际使用的温度（根据上下文应为 0.7），修正 §3.2，并在 §3.2 中明确写出完整的采样配置（temperature, top-p, max length）。

**N2** [critical] Gen-0 seed sharing 导致主要指标被高估，报告框架需调整

- **具体位置**: §3.2 (page 3), Table 1 (page 6), Abstract (page 1)
- **问题**: 所有 8 个 generator 共享相同的 gen-0 seed（同一批 Wikipedia passages），在 LOGO 评估中，held-out generator 的 gen-0 文本与训练集中其他 generator 的 gen-0 文本完全相同。论文承认了这一点（"3-class F1 may carry upward bias from gen-0 seed sharing"）并补充了 binary F1（gen-1 vs. gen-2+）= 0.694。但 Abstract 和全文仍以 3-class F1=0.762 为主要指标。
- **为什么影响接收**: 审稿人和读者首先看到的是 Abstract 中的 F1=0.764（cross-model）和正文中的 0.762（LOGO），这些数字受 gen-0 泄露影响。泄露免疫的 binary F1=0.694 才是 LOGO 下的可信上界。
- **建议**: (a) 在 Abstract 中首先报告 leak-free binary F1；(b) 正文所有场景同时报告 leak-free metric 和 3-class metric（Table 1 已做到，但叙述重心需调整）；(c) 考虑对 gen-0 seed 做 per-fold split 以消除 LOGO 中的 gen-0 泄露。

**N3** [critical] 仅限 base model，对实际场景的适用性严重不足

- **具体位置**: §3.2 (page 3), Limitations (page 9)
- **问题**: 所有 8 个 generator 均为 base model（非 instruction-tuned）。Limitations 部分承认 instruction-tuned model 的 depth signal "substantially degrades"（OLMo-2-1B-Instruct: LOGO F1=0.338, Mistral-7B-Instruct: F1=0.667）。然而，现实中绝大部分 LLM 生成文本来自 instruct/chat model。
- **为什么影响接收**: 论文的核心 claim（"generation depth is detectable"）在最具实际意义的场景（instruct model）下大幅弱化。F1=0.338 意味着几乎不可用。如果论文定位为"基础研究发现"而非"实用检测方法"，则需要在 framing 中显著调整，目前 Introduction 和 Abstract 的 framing 暗示了实际应用价值（如 "data curation", "provenance"）。
- **建议**: (a) 在 Abstract/Introduction 中更明确地 scope 限定为 base model 设定下的分析性发现；(b) 至少增加 2-3 个 instruct model 作为探索性实验（即使结果不佳，也需在正文而非仅 Limitations 中讨论）；(c) 讨论为什么 instruction tuning 破坏了 depth signal（目前仅一句话带过）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] DDR 中 |ρ|>0.60 和 |ρ|<0.10 的阈值缺乏正式依据

- **具体位置**: §3.3 (page 5), §4.2 (page 6-7)
- **问题**: DDR 框架将特征分为 drifting（|ρ|>0.60）和 stationary（|ρ|<0.10），entropy_std 被标为 intermediate（|ρ|=0.17）。这些阈值是 post-hoc 选择以匹配观察到的行为，但论文将其表述为 "operative criteria"（page 5），暗示了某种规范性。没有解释为什么不是 0.50 或 0.70。
- **建议**: (a) 明确说明这是 empirical observation 而非预设标准；(b) 做一个 sensitivity analysis 展示不同阈值下的特征分组和分类性能变化。

**W2** [warning] Levene test 结果与 "approximately preserves shape" claim 存在张力

- **具体位置**: §4.2 (page 7)
- **问题**: Levene test 对所有 7 个特征都 reject 等方差假设（p < 10^{-10}），包括 shape features。但 Abstract 和 §3.3 claim shape features "approximately preserves distributional shape"。论文用 effect size（coefficient of variation shift <3% vs >15%）来辩护，这是合理的，但 framing 上存在问题——正式统计检验说"shape 确实变了"，文字叙述说"shape 近似不变"。
- **建议**: 使用更精确的表述，如 "features whose distributional spread changes minimally in relative terms" 而非 "preserves shape"。在 §4.2 中更显著地讨论 effect size vs. statistical significance 的区分。

**W3** [warning] Downstream utility 分析统计功效不足（n=3 seeds）

- **具体位置**: §4.4 (page 7-8), Appendix L (page 19)
- **问题**: Fine-tuning 实验仅用 3 个 random seeds，导致 Cohen's d 值不可靠（论文自己承认 "pooled standard deviation is extremely small (<0.001), artificially inflating d"）。TOST 在 ±2% margin 下拒绝了 full dataset vs. depth-filtered 的等价性，但论文结论 "depth composition doesn't matter" 主要基于 depth-0-1 vs. random subsample 的等价（同 sample count）。n=3 的 TOST 功效有限。
- **建议**: 至少增加到 n=5-10 seeds 以获得可信的 effect size 和功效分析，或明确标注为 preliminary/exploratory result。

**W4** [warning] 模型规模范围有限（0.6B–8B），缺少大模型

- **具体位置**: §3.2 (page 3), Limitations (page 9)
- **问题**: 8 个 generator 的参数量为 0.6B–8B。Limitations 承认 70B+ model "may further compress feature margins"。在当前 LLM 生态中（Llama-3-70B, Qwen-72B 等已广泛使用），不包含任何 >10B model 是一个显著缺口。论文的 scale effect 分析（page 9: "larger models show degradation, Mistral-7B: 0.653"）暗示 depth signal 可能随模型规模衰减。
- **建议**: 在 Limitations 中更明确讨论 scale trend 的外推风险。如果计算资源允许，至少增加一个 13B-70B 级别的探索性实验。

**W5** [warning] Cross-model 评估仅使用 5/8 generators

- **具体位置**: Table 1 footnote (page 6)
- **问题**: Cross-model chains 仅用原始 5 个 generator（Pythia, OLMo, Qwen），Llama 和 Mistral 是后来加入仅做 single-generator 评估。这意味着 cross-model F1=0.809 的泛化性声明基于更小的 generator pool。
- **建议**: 说明为什么 Llama/Mistral 不参与 cross-model evaluation。如果是实验时序原因，应在正文而非 footnote 中披露。

**W6** [warning] Baseline 对比中 multi-detector ensemble 的计算成本未量化

- **具体位置**: §3.4 (page 5), Table 4 (page 8)
- **问题**: 论文称 multi-detector ensemble 的计算成本是 7-feature ensemble 的 2.4×，但 Table 4 footnote 仅提到 "requires 410M reference model (960 MB); 4-det ensembles require two models (960 MB) totaling 1.4B parameters (2,865 MB)"。这是内存对比，不是 inference latency/FLOPs 对比。"2.4× computation" 的计算基础不明。
- **建议**: 提供 inference 时间的实际对比（per-text ms 或 throughput），或将 "2.4×" 改为更精确的内存/参数量对比。

---

## Minor 问题（不影响接收）

- **M1**: Table 5 (page 13) 的 "Attrition varies by generator due to differing generation failure rates" 未解释具体 attrition 率——Pythia-1B: 4,535 vs Qwen-0.6B: 4,536 差异极小，但 Mistral-7B-v0.3 仅 4,849，原因不明。
- **M2**: Figure 2 的 strip plot 有一些点的标签重叠（entropy_std），影响可读性。
- **M3**: §2.2 (page 2-3) Model Collapse and Iterative Generation 部分引用了 Geng et al. (2026) 的 Markovian chains 理论框架，但未充分区分该工作关注的 training-loop collapse 和本文关注的 inference-time chain，两者机制不同。
- **M4**: Appendix E (QLoRA end-to-end) 的超参数（LoRA rank 32, seed 32, yield 127）与主实验的 XGBoost 方案差异较大，作为 Appendix 可以接受，但应更明确说明这是 exploratory comparison。

---

## Questions for Authors

**Q1**: §3.2 的 temperature 究竟是 0 还是 0.7？如果是 0.7，那么在 greedy decoding 下的实验结果是否有对照？

**Q2**: 如果对 gen-0 做 per-generator unique seed（而非 shared seed），LOGO 3-class F1 预期会下降多少？是否做过这样的实验？

**Q3**: Instruction-tuned model 的 depth signal 衰减（F1=0.338），作者认为根本原因是什么？是 instruction tuning 改变了 NLL 分布的 convergence dynamics，还是 instruct model 的输出本身就更接近 human text？

**Q4**: DDR 的 drifting/stationary 分类在不同 generator family 之间是否一致？即，是否存在某个 family 中 entropy_mean 不再 drift 的情况？

**Q5**: 论文在 per-generator F1 上显示 Pythia generators 表现最好，而 larger models 表现更差。这是否意味着 depth fingerprinting 本质上依赖于 small model 的 generation quality gap？

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.0/5 | 核心方法合理，但温度矛盾（N1）是硬伤，gen-0 泄露使主指标不可信（N2），Levene test 与 claim 存在张力（W2），downstream analysis 欠功效（W3） |
| **Excitement** | 3.0/5 | 任务定义新颖（depth classification），DDR 分析有洞察力，但仅限 base model 的实用性限制了影响力（N3），0.694 binary F1 的实际效用有限 |
| **Reproducibility** | 2.5/5 | 温度参数矛盾直接损害复现（N1），数据构建流程清晰但关键采样参数不一致，代码/数据未公开（承诺 upon publication） |
| **Reviewer Confidence** | 4/5 | 仔细阅读全文含所有 20 页附录，交叉检查了统计声明和引用完整性 |

---

## Overall Assessment

**Overall**: **3.0** (Findings track 可接收)

**一句话总结**: 本文提出了一个新颖且有意义的任务（generation depth classification），DDR 分析提供了有价值的机制洞察，但三个 critical 问题——温度参数内部矛盾损害可复现性、gen-0 seed sharing 高估主指标、仅限 base model 的严重适用性限制——使其在当前状态下不适合主会议，但通过修正后适合 Findings track。

**接收条件**:
- **必须修正**: N1（温度矛盾）、N2（指标报告框架）
- **强烈建议**: N3（至少在正文讨论 instruct model 结果，而非仅放在 Limitations 一句话）
- **提升评分**: W1-W6 中任意 3 项的实质改进可将评分提至 3.5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 650 · 2026-05-17T18:16:26.121661+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成独立审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 62

## Round 62

2 recorded events


### User

_source line 651 · 2026-05-17T18:16:29.536854+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：我完成了 Round 1 全面审稿，给出 **Overall 3.0（Findings 可接收）**。标记了 3 个 Must-Fix 问题：

1. **N1 [critical]**: §3.2 写 temperature=0 但 Limitations 和 Appendix 均指向 0.7，核心可复现性缺陷
2. **N2 [critical]**: Gen-0 seed sharing 使 3-class LOGO F1=0.762 被高估，leak-free binary F1=0.694 应作为主指标
3. **N3 [critical]**: 仅 base model 实验，instruct model 下 F1 降至 0.338，实际适用性严重不足

另有 6 个 Should-Fix（DDR 阈值缺乏依据、Levene test 与 claim 矛盾、downstream n=3 欠功效、模型规模有限、cross-model 仅 5/8 generator、计算成本对比不精确）和 4 个 Minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 652 · 2026-05-17T18:16:35.233619+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 63

## Round 63

6 recorded events


### User

_source line 653 · 2026-05-17T18:20:30.602352+00:00_

[Reviewer 2 审稿意见]:
## Round 1 审稿报告 — Reviewer 2（新颖性 + 完整性 + 写作质量）

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains
**Venue**: EMNLP 2026 via ARR May cycle

---

## 总体评分
**Overall**: 2.5 / 5（Borderline Findings）
**一句话总结**: 任务定义新颖、实验设计严谨，但方法技术贡献低、仅适用于 base 模型严重限制实际价值、且正文超页数需修改后方可提交。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体合理：LOGO 评估、统计检验、length confound 控制均到位；但 gen-0 共享引入评估偏差（虽有 binary metric 缓解），DDR 机制解释停留在"consistent with"假设层面 |
| Excitement | 2.5/5 | Generation depth classification 作为新任务定义是有趣的贡献，DDR 现象有文档价值；但方法本身（7 个标准特征 + XGBoost）无技术新颖性，base-model-only 限制使实际应用场景极窄，downstream utility 为 null result |
| Reviewer Confidence | 4/5 | 对 AI text detection、distributional analysis、ordinal classification 文献较熟悉 |

---

## Summary

本文提出 generation depth classification（gen-0/gen-1/gen-2+），将传统二分类（human vs. synthetic）扩展为三类有序分类。核心发现是 differential depth response (DDR)：在 8 个 base model generator（5 个家族，0.6B–8B）上，central-tendency 特征（entropy mean、TTR、hapax ratio）随 depth 单调漂移，而 shape 特征（entropy max、tail decay）近似不变。7 特征 + XGBoost 在 8-generator LOGO 下取得 binary F1=0.694（gen-1 vs gen-2+），3-class F1=0.762。

论文实验全面，包括 cross-model chains、cross-family reference models、温度敏感性、length confound 控制、多种 prompt type、下游任务验证等。写作质量较好，limitation 部分诚实全面。

---

## 主要优势

**S1. 任务定义新颖且有研究意义**
Generation depth classification 是一个尚未被系统研究的问题。将 binary detection 扩展到 ordinal depth estimation 有助于理解递归生成的分布动态。与 broken_telephone（paraphrasing chains）和 markovian_chains（attractor dynamics）的区分清晰（§2.2, lines 23–31）：本文研究 non-paraphrastic continuation chains，使用 handcrafted features 而非 model-internal representations。

**S2. 实验设计严谨、消融分析充分**
LOGO cross-validation 是评估 cross-generator generalization 的正确选择。length confound control（§4.1）排除了长度假象。cross-reference model 实验（Table 2, spread=0.013）确认 DDR 非 reference-specific。温度敏感性分析（Appendix B）、prompt type generalization（Appendix C）、5-class fine-grained evaluation（Appendix D）等消融实验系统全面。统计检验规范：bootstrap CIs、McNemar tests、Bonferroni correction 均到位。

**S3. Null result 的诚实报告**
Downstream utility（§4.4）报告了一个 null result（depth composition 不影响训练质量），并用 TOST equivalence test 严格验证。这种科学诚实度在投稿论文中值得肯定。

**S4. Related Work 覆盖全面，定位清晰**
58 条引用覆盖了 detection methods、model collapse、stylometry、data quality 四个相关方向。与最直接相关的两篇 concurrent work（broken_telephone, markovian_chains）的三点区别表述清晰（§2.2, line 26）。对 model collapse 与 inference-chain drift 的区分准确（§5, line 17）。

**S5. 写作质量较高**
全文无 em-dash（仅注释中有），无 en-dash 滥用，-ing phrases 均为自然用法，AI 写作痕迹极少（仅 appendix 一处"Notably"）。专有名词首次出现均有定义。段落长度自然，过渡连贯。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文超页数限制
- 具体位置：PDF p8–p9
- 问题：EMNLP long paper 要求正文 ≤8 页（References/Limitations/Ethics/Appendix 不计入）。从 PDF 可见 Section 5 (Discussion) 横跨 p7 底部到 p9 顶部，Section 6 (Conclusion) 起始于 p9 约 1/6 处，Limitations 约在 p9 的 1/3 处开始。正文（Abstract 到 Conclusion）约溢出 1/3 页。
- 为什么影响接收：页数违规可能导致 desk reject。
- 建议修改方向：压缩 Discussion（当前约 1.5 页，内容可精简）或将部分 Results 数据移至附录。Table 4 (baselines) 可考虑与正文 baseline comparison 段落共同精简。

**N2** [critical] Abstract/Introduction 选择性报告性能数字
- 具体位置：Abstract lines 7; Introduction line 15
- 问题：Abstract 开头突出 cross-model chain 结果（binary F1=0.764, 3-class=0.809），但这使用的是 5-generator subset + 5-fold CV，而非更严格的 8-generator LOGO（binary=0.694, 3-class=0.762）。Table 1 caption 自己承认 "3-class F1 may carry upward bias from gen-0 seed sharing"。真正无偏的核心指标是 binary LOGO F1=0.694，但它在叙述中被边缘化。这给审稿人一个过于乐观的第一印象。
- 此外，Introduction 称 "outperforming all individual detection baselines by 6--11 pp"（line 15），但 Table 4 中 3-class 改进范围实际是 6.7 pp（vs Avg-LogProb）到 36.3 pp（vs Binoculars）。"6–11" 仅覆盖两个最强 baseline，忽略 LD-Score (+14.4 pp) 和 Binoculars (+36.3 pp)。
- 建议修改方向：Abstract 应以 8-gen LOGO binary F1 (0.694) 为主指标，cross-model 结果作为补充。"6–11 pp" 应改为 "6+ pp" 或报告完整范围。

**N3** [critical] Base-model-only 限制在 framing 中未充分体现
- 具体位置：Abstract（无提及）; Introduction line 13（一句话）; Limitations §全文
- 问题：论文仅在 base/pretrained 模型上有效。Instruction-tuned 模型性能骤降（OLMo-Instruct: 0.338 vs base 0.763; Qwen3-0.6B chat: 0.667 vs base 0.816, Limitations line 7）。由于现实中几乎所有 LLM 生成文本来自 instruction-tuned/RLHF 模型，这个限制从根本上约束了方法的实际应用场景。虽然 Limitations 部分详细讨论了这一点，但 Abstract 完全未提及，Introduction 仅用一句话带过（"we restrict to base models as a deliberate design choice"）。这导致论文 framing 与实际贡献范围不匹配。
- 为什么影响接收：审稿人读完 Abstract/Introduction 后会对方法的实际应用价值产生不切实际的预期。当 Limitations 部分揭示 instruct model 近乎失败时，会产生 "bait-and-switch" 的感觉。
- 建议修改方向：Abstract 应明确标注 "base (pretrained) models"；Introduction 的 contribution 列表中应包含这一 scope constraint。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] DDR 机制解释不充分
- 具体位置：§3.3 Feature Complementarity (line 72); §5 Discussion (lines 1–6)
- 问题：论文反复说 DDR "consistent with" NLL 分布的 location shift + shape preservation，但始终用 "consistent with" 而非 "caused by"。Discussion 第 5 行承认这是 "a tendency rather than an architectural guarantee"，t=1.0 时 shape preservation 破裂（-6pp）。然而论文 framing 中将 DDR 作为一个 "finding"（contribution 2），实际上更像是一个 empirical observation + post-hoc hypothesis。缺乏对 why shape should be preserved 的形式化分析（例如 softmax + temperature 如何约束 NLL 分布的高阶矩）。
- 建议：明确区分 "empirical observation" 与 "mechanistic explanation"，或补充简要的形式化分析支撑 shape-preservation 假设。

**W2** [warning] 方法技术新颖性极低
- 具体位置：§3 Method 全节
- 问题：7 个特征（5 个 NLL 统计量 + TTR + hapax ratio）均为标准的文本统计特征，分类器为 off-the-shelf XGBoost。论文自己在 §2.1 line 13 中说 "Our contribution is not a new detection method but the task formulation"。作为 Findings 论文可以接受（实证贡献为主），但审稿人仍需要评估方法层面是否有 non-trivial insight。DDR 中 drifting vs stationary 的分组本质上是对 Spearman |ρ| 的二值化（threshold 0.10 vs 0.60），缺乏理论依据。
- 建议：如果定位为 phenomenon paper，建议在 Introduction 中更显式地说明 "this is primarily an empirical contribution characterizing a previously undocumented phenomenon"。

**W3** [warning] Downstream utility 作为 null result 的定位问题
- 具体位置：§4.4 (results.tex lines 141–148)
- 问题：§4.4 在正文中占据宝贵空间（约 1/4 页），结论是 "depth composition per se does not determine training utility"——一个 null result。在正文已超页数的情况下，这部分内容的 cost-benefit 比不佳。如果 depth classification 最直接的应用场景（data curation）被证明无效，那么论文需要更清楚地说明 depth classification 的 concrete use case 是什么。
- 建议：考虑将 §4.4 完全移入附录，在 Discussion 中用 1-2 句话总结（目前 §6 Conclusion line 5 已有此总结）。正文空间用于压缩至 8 页。

**W4** [warning] Gen-0 seed sharing 引入的评估偏差虽有缓解但仍需更谨慎
- 具体位置：§3.2 lines 29-30; Table 1 caption
- 问题：LOGO 中 gen-0 样本在 held-out generator 的 chains 中与 training generators 的 chains 完全相同。虽然论文提供了 binary metric（排除 gen-0）作为 "leak-free" 指标，但 3-class F1 (0.762) 仍是论文的 headline metric 之一。Table 1 caption 说 "may carry upward bias" 但用词过于模糊——实际上，如果 classifier 记住了 gen-0 文本的特征分布，3-class F1 的 gen-0 recall 必然被高估。
- 建议：量化 gen-0 seed sharing 的影响（例如：在 training 中去除 held-out generator 的 gen-0 样本后重跑 LOGO，或报告 gen-1/gen-2+ 的 per-class F1 与 gen-0 对比）。

**W5** [warning] 部分附录使用 6-generator subset 与正文 8-generator 不一致
- 具体位置：main.tex line 38 (appendix note)
- 问题：附录开头注明 "Unless otherwise stated, appendix experiments use the original six-generator subset"，但正文用 8 generator。这意味着多个关键消融（classifier sensitivity Appendix G, sampling sensitivity, per-generator performance）的结果不能直接与正文主结果比较。Cross-reference table (Table 2) 也用 5-gen subset。这种不一致降低了实验的可比性。
- 建议：至少在核心消融（classifier sensitivity, cross-reference）上用 8-generator 重跑，或清楚解释为什么 subset 结果可以推广到 full set。

---

## 小问题（不影响接收）

- **M1**: Appendix D (appendix_finer_depth.tex line 46) 使用 "Notably"——minor AI writing marker，建议删除或改写。
- **M2**: Ethics Statement 中 GPU 型号为 "RTX 5090"（ethics.tex line 15）——如果 RTX 5090 尚未正式发布，可能引起审稿人疑问。请确认硬件信息准确。
- **M3**: `\documentclass[11pt]{article}` + `\usepackage[review]{acl}` 格式上可以工作，但标准写法是 `\documentclass[11pt,review]{acl}`。建议统一。
- **M4**: 引用验证中 6 条未被 OpenAlex 收录（DetectGPT, reliable_detection, detection_possibilities, aaronson_watermark, pythia, xgboost）——这些均为知名论文，应为 API 限制而非虚假引用。4 条 author name mismatch（self_consuming_mad, qwen3, gutierrez_ordinal_survey, llama3）为编码差异，不影响质量。
- **M5**: Table 4 中 "4-det. + surface" 和 "4-detector ens." 的 3-class F1（0.795, 0.785）均高于 7-feature（0.774）。虽然论文正确指出 binary 差距小（≤0.3pp）且 computational cost 更低，但 3-class 差距达 2.1pp。如果 3-class 是重要指标，应更坦率地讨论 ensemble baselines 的优势。

---

## Missing References

未发现重大遗漏。以下可选参考：
- "Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems" (2026, arxiv 2601.04170)——虽然是 multi-agent 场景，但 behavioral degradation across iterative interactions 的概念有相似之处，可在 Related Work 中提及以拓宽视角。
- "Visual Fingerprints for LLM Generation Comparison" (2026, arxiv 2605.06054)——LLM 输出的 visual fingerprint，与本文 "fingerprinting" 概念有命名相似性，可选择性引用。

---

## 对审稿侧重问题的回答

**1. 新颖性与定位**
- "generation depth classification" 作为新任务定义是论文最重要的贡献，对研究社区有价值。
- DDR 作为 empirical observation 有文档价值，但不构成 "discovery"——更像是对 recursive generation 分布动态的系统化量化。NLL mean 随 depth 漂移是直觉上可预期的；shape preservation 是一个有趣但未被证明的 observation。
- 方法本身（标准特征 + XGBoost）技术新颖性接近零。
- 定位为 "phenomenon paper" 是合理的策略，适合 Findings track，但前提是实证分析本身够深入——本文在这方面做得不错。
- 与 broken_telephone 和 markovian_chains 的区分清晰且充分（§2.2）。

**2. Related Work 覆盖度**
- 58 条引用覆盖了主要方向。未发现重大遗漏。
- 与 model collapse 文献的区分准确（inference chain vs training loop degradation）。
- 2025-2026 年的新工作（diveye, generator_barrier, feat_aug_transformer, chainwash, markovian_chains）已覆盖。

**3. 论文结构与叙事**
- 主线基本统一：problem → DDR observation → feature ensemble → evaluation。
- "twofold contributions" 与正文内容一致。
- Downstream utility null result（§4.4）在正文中的位置值得商榷（见 W3）。
- Limitations 部分全面诚实，是论文的亮点之一。

**4. 写作质量**
- AI 痕迹极少：无 em-dash 滥用（仅注释），无 en-dash 滥用，-ing phrases 自然，过渡词适度（仅一处 "Notably"）。
- 专有名词均有首次定义（DDR, generation depth, LOGO 等）。
- 代词指代清晰。
- 图表 caption 基本自包含（Figure 1 caption 较长但信息完整）。

**5. 格式合规**
- **页数**：正文超 8 页约 1/3 页 ❌
- **匿名化**：Anonymous author，未发现自引泄露 ✓
- **行号**：开启 ✓
- **Bib 完整性**：0 orphan, 0 missing, 大部分验证通过 ✓
- **图表字体**：Figure 1-3 字体 ≥7pt ✓
- **图片格式**：Figure 1-3 使用 PDF 格式 ✓（但 appendix violin plot 等未检查）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-17T18:20:58.252771+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条 Must-Fix / Should-Fix / Minor 问题：\n- **[AGREE]** 同意并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** 反驳并提供证据\n\n特别关注与你自身审稿意见的一致/冲突之处。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 — Overall: 2.5 / 5（Borderline Findings）\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reviewer Confidence | 4/5 |\n\n### Summary\n本文提出 generation depth classification（gen-0/gen-1/gen-2+），将传统二分类扩展为三类有序分类。核心发现是 DDR：central-tendency 特征随 depth 单调漂移，shape 特征近似不变。7 特征 + XGBoost 在 8-gen LOGO 下取得 binary F1=0.694，3-class F1=0.762。\n\n### Strengths\n- S1: 任务定义新颖，与 broken_telephone/markovian_chains 区分清晰\n- S2: 实验设计严谨、消融分析充分\n- S3: Null result 的诚实报告\n- S4: Related Work 覆盖全面\n- S5: 写作质量较高，AI 痕迹极少\n\n### Must-Fix\n**N1 [critical]** 正文超页数限制（约溢出 1/3 页），可能 desk reject\n**N2 [critical]** Abstract/Introduction 选择性报告——突出 cross-model 5-gen F1=0.764 而非 8-gen LOGO binary 0.694；\"6-11pp\" 改进范围仅覆盖两个最强 baseline\n**N3 [critical]** Base-model-only 限制在 framing 中未充分体现——Abstract 无提及，Introduction 仅一句话\n\n### Should-Fix\n**W1** DDR 机制解释不充分——始终 \"consistent with\" 而非 \"caused by\"，缺乏形式化分析\n**W2** 方法技术新颖性极低——7 个标准特征 + XGBoost，无 non-trivial insight\n**W3** Downstream utility null result 占正文 1/4 页空间，cost-benefit 不佳，建议移入附录\n**W4** Gen-0 seed sharing 偏差需量化\n**W5** 附录 6-gen subset 与正文 8-gen 不一致\n\n### Minor\nM1: Appendix D \"Notably\" AI marker\nM2: RTX 5090 硬件信息可能引起疑问\nM3: documentclass 写法建议统一\nM4: 6 条 bib 未被 OpenAlex 收录（API 限制）\nM5: 3-class F1 中 ensemble baselines 优势应更坦率讨论\n\n### Missing References\n无重大遗漏。可选：Agent Drift (2601.04170), Visual Fingerprints (2605.06054)\n\n---\n\n请逐条 [AGREE] 或 [REBUT]，重点关注 N1-N3 和 W1-W5。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条 Must-Fix / Should-Fix / Minor 问题：\n- **[AGREE]** 同意并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** 反驳并提供证据\n\n特别关注与你自身审稿意见的一致/冲突之处。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 — Overall: 2.5 / 5（Borderline Findings）\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reviewer Confidence | 4/5 |\n\n### Summary\n本文提出 generation depth classification（gen-0/gen-1/gen-2+），将传统二分类扩展为三类有序分类。核心发现是 DDR：central-tendency 特征随 depth 单调漂移，shape 特征近似不变。7 特征 + XGBoost 在 8-gen LOGO 下取得 binary F1=0.694，3-class F1=0.762。\n\n### Strengths\n- S1: 任务定义新颖，与 broken_telephone/markovian_chains 区分清晰\n- S2: 实验设计严谨、消融分析充分\n- S3: Null result 的诚实报告\n- S4: Related Work 覆盖全面\n- S5: 写作质量较高，AI 痕迹极少\n\n### Must-Fix\n**N1 [critical]** 正文超页数限制（约溢出 1/3 页），可能 desk reject\n**N2 [critical]** Abstract/Introduction 选择性报告——突出 cross-model 5-gen F1=0.764 而非 8-gen LOGO binary 0.694；\"6-11pp\" 改进范围仅覆盖两个最强 baseline\n**N3 [critical]** Base-model-only 限制在 framing 中未充分体现——Abstract 无提及，Introduction 仅一句话\n\n### Should-Fix\n**W1** DDR 机制解释不充分——始终 \"consistent with\" 而非 \"caused by\"，缺乏形式化分析\n**W2** 方法技术新颖性极低——7 个标准特征 + XGBoost，无 non-trivial insight\n**W3** Downstream utility null result 占正文 1/4 页空间，cost-benefit 不佳，建议移入附录\n**W4** Gen-0 seed sharing 偏差需量化\n**W5** 附录 6-gen subset 与正文 8-gen 不一致\n\n### Minor\nM1: Appendix D \"Notably\" AI marker\nM2: RTX 5090 硬件信息可能引起疑问\nM3: documentclass 写法建议统一\nM4: 6 条 bib 未被 OpenAlex 收录（API 限制）\nM5: 3-class F1 中 ensemble baselines 优势应更坦率讨论\n\n### Missing References\n无重大遗漏。可选：Agent Drift (2601.04170), Visual Fingerprints (2605.06054)\n\n---\n\n请逐条 [AGREE] 或 [REBUT]，重点关注 N1-N3 和 W1-W5。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-17T18:21:18.408669+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20155
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-17T18:21:19.011223+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条 Must-Fix / Should-Fix / Minor 问题：\n- **[AGREE]** 同意并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** 反驳并提供证据\n\n特别关注与你自身审稿意见的一致/冲突之处。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 — Overall: 3.0 (Findings track 可接收)\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.0/5 |\n| Excitement | 3.0/5 |\n| Reproducibility | 2.5/5 |\n| Reviewer Confidence | 4/5 |\n\n### Summary\n本文提出 generation depth classification 任务，构建了 8 个 base model 的 37,058 条递归生成链数据集，提取 7 个特征用 XGBoost 在 LOGO 下达到 3-class F1=0.762。核心发现是 DDR：递归生成使 NLL 分布发生 location shift 但 shape 近似保持。\n\n### Strengths\n- S1: 任务定义新颖\n- S2: DDR 分析框架有洞察力\n- S3: 评估方案全面\n- S4: 轻量高效（单 Pythia-410M reference）\n- S5: 引用完整无幽灵（58 条全部被引用）\n\n### Must-Fix\n**N1 [critical]** §3.2 温度参数内部矛盾——§3.2 写 temperature=0 但 Limitations/Appendix 指向 0.7，核心可复现性缺陷\n**N2 [critical]** Gen-0 seed sharing 高估主指标——3-class F1=0.762 受泄露影响，leak-free binary 0.694 应为主指标\n**N3 [critical]** 仅 base model，instruct model 下 F1=0.338，实际适用性严重不足\n\n### Should-Fix\n**W1** DDR 阈值 |ρ|>0.60 / <0.10 缺乏正式依据\n**W2** Levene test 全 reject 与 \"approximately preserves shape\" claim 张力\n**W3** Downstream n=3 seeds 功效不足\n**W4** 模型规模有限（0.6B-8B），无 >10B model\n**W5** Cross-model 仅 5/8 generators\n**W6** Multi-detector ensemble 计算成本 \"2.4×\" 基础不明\n\n### Minor\nM1: Mistral-7B attrition 原因不明\nM2: Figure 2 strip plot 标签重叠\nM3: §2.2 Geng et al. 区分不够充分\nM4: Appendix E QLoRA 超参差异大\n\n### Questions\nQ1: §3.2 temperature 究竟是 0 还是 0.7？\nQ2: Per-generator unique seed 实验？\nQ3: Instruct model depth signal 衰减根本原因？\nQ4: DDR drifting/stationary 在不同 family 间是否一致？\nQ5: Depth fingerprinting 是否本质上依赖 small model generation quality gap？\n\n---\n\n请逐条 [AGREE] 或 [REBUT]，重点关注 N1-N3 和 W1-W6。",
  "project": "gen-depth-fingerprint",
  "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条 Must-Fix / Should-Fix / Minor 问题：\n- **[AGREE]** 同意并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** 反驳并提供证据\n\n特别关注与你自身审稿意见的一致/冲突之处。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 — Overall: 3.0 (Findings track 可接收)\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.0/5 |\n| Excitement | 3.0/5 |\n| Reproducibility | 2.5/5 |\n| Reviewer Confidence | 4/5 |\n\n### Summary\n本文提出 generation depth classification 任务，构建了 8 个 base model 的 37,058 条递归生成链数据集，提取 7 个特征用 XGBoost 在 LOGO 下达到 3-class F1=0.762。核心发现是 DDR：递归生成使 NLL 分布发生 location shift 但 shape 近似保持。\n\n### Strengths\n- S1: 任务定义新颖\n- S2: DDR 分析框架有洞察力\n- S3: 评估方案全面\n- S4: 轻量高效（单 Pythia-410M reference）\n- S5: 引用完整无幽灵（58 条全部被引用）\n\n### Must-Fix\n**N1 [critical]** §3.2 温度参数内部矛盾——§3.2 写 temperature=0 但 Limitations/Appendix 指向 0.7，核心可复现性缺陷\n**N2 [critical]** Gen-0 seed sharing 高估主指标——3-class F1=0.762 受泄露影响，leak-free binary 0.694 应为主指标\n**N3 [critical]** 仅 base model，instruct model 下 F1=0.338，实际适用性严重不足\n\n### Should-Fix\n**W1** DDR 阈值 |ρ|>0.60 / <0.10 缺乏正式依据\n**W2** Levene test 全 reject 与 \"approximately preserves shape\" claim 张力\n**W3** Downstream n=3 seeds 功效不足\n**W4** 模型规模有限（0.6B-8B），无 >10B model\n**W5** Cross-model 仅 5/8 generators\n**W6** Multi-detector ensemble 计算成本 \"2.4×\" 基础不明\n\n### Minor\nM1: Mistral-7B attrition 原因不明\nM2: Figure 2 strip plot 标签重叠\nM3: §2.2 Geng et al. 区分不够充分\nM4: Appendix E QLoRA 超参差异大\n\n### Questions\nQ1: §3.2 temperature 究竟是 0 还是 0.7？\nQ2: Per-generator unique seed 实验？\nQ3: Instruct model depth signal 衰减根本原因？\nQ4: DDR drifting/stationary 在不同 family 间是否一致？\nQ5: Depth fingerprinting 是否本质上依赖 small model generation quality gap？\n\n---\n\n请逐条 [AGREE] 或 [REBUT]，重点关注 N1-N3 和 W1-W6。",
    "project": "gen-depth-fingerprint",
    "chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "director_session_key": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-17T18:21:20.372441+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 658 · 2026-05-17T18:21:23.114076+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 659 · 2026-05-17T18:21:25.668766+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿报告已提交给 Review Director。

核心结论：**Overall 2.5（Borderline Findings）**。

三个 Must-Fix 问题：
1. 正文超 8 页限制约 1/3 页（可能 desk reject）
2. Abstract/Introduction 选择性报告 5-generator cross-model 数字而非更严格的 8-gen LOGO 结果
3. Base-model-only 限制在 framing 中未充分体现（instruct 模型近乎失败但 Abstract 未提及）

五个 Should-Fix 问题：DDR 机制解释不足、方法技术新颖性低、downstream null result 占正文空间、gen-0 seed sharing 偏差量化不够、附录与正文 generator 数量不一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 660 · 2026-05-17T18:21:32.840956+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 65

## Round 65

2 recorded events


### User

_source line 661 · 2026-05-17T18:23:50.975068+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条评议

---

### Must-Fix 逐条回应

**[AGREE] R2-N1: 正文超页数限制（约溢出 1/3 页）**

我在自己的审查中未显式标注此问题，但核实后确认：§1–§6 Conclusion 结束于 page 9 约 1/3 处（Limitations 从 page 9 约 2/3 处开始，不计入页数限制），正文确实约溢出 1/3 页。ARR Long paper ≤ 8 页正文是硬约束，溢出有 desk reject 风险。这与我提出的 W3（downstream utility 占空间）相关——将 §4.4 的 null result 移入附录是最直接的压缩方案，同时也回应了 R2-W3。

**[AGREE] R2-N2: Abstract/Introduction 选择性报告**

与我的 N2（gen-0 seed sharing 高估主指标）高度一致。补充两个具体证据：

1. Abstract 突出 "binary F1 = 0.764 on heterogeneous cross-model chains (3-class: 0.809; five-generator subset)"，但 8-gen LOGO 的 leak-free binary F1 = 0.694 才是更严格的泛化指标，降了 7pp。
2. "6–11 pp" 改进范围（page 1）仅对比单特征 baseline（Table 4: FastDetectGPT 0.411, Binoculars 0.625, LD-Score 0.635, Avg-LogProb 0.60）。4-det+surface ensemble 实际上在 3-class F1（0.768 vs. 0.762）和 binary F1（0.698 vs. 0.694）上均优于 7-feature method，但正文描述为 "comparable"（page 8）。这是选择性 framing。

R2 的判断正确：报告策略需要调整，应以 8-gen LOGO binary F1 = 0.694 为 primary metric，并坦率承认 4-det ensemble 在数值上小幅领先。

**[AGREE] R2-N3: Base-model-only 限制在 framing 中未充分体现**

与我的 N3 完全一致。Abstract 完全未提及 base-model 限制。Introduction（page 1）仅在末尾有一句 "We restrict to base (pretrained) models as a deliberate design choice; since instruction-tuning introduces confounds..."。Limitations（page 9）报告了 instruct model 的严重降级（OLMo-2-Instruct: F1=0.338），但这条关键信息被埋在正文最后。

对于一篇 Findings paper，至少应在 Abstract 中用一句话 scope 限定（如 "among base language models"），并在 Introduction 的 Contributions 列表中标注此约束。

---

### Should-Fix 逐条回应

**[REBUT] R2-W1: DDR 机制解释不充分——"consistent with" 而非 "caused by"**

R2 认为 DDR 分析始终用 hedging 语言（"consistent with"）而缺乏形式化解释，构成方法缺陷。我部分不同意。

理由：本文是实证研究（empirical study），而非理论工作。使用 "consistent with" 恰恰是科学上恰当的表述——论文观察到 NLL 分布的 location shift 与 shape preservation 模式，并利用这一模式构建分类器，但论文没有声称发现了因果机制。这与同类实证检测工作（如 Binoculars (Hans et al., 2024) 使用 cross-perplexity ratio 时也未给出形式化因果解释）的写作规范一致。

但我同意一个 weaker version：§5 Discussion（page 8）提出 "standard decoding regimes indirectly preserve the functional form of the NLL distribution" 时，如果能用简短的 information-theoretic argument 或至少一个 toy experiment 来支撑这个 hypothesis，会增加说服力。作为 Should-Fix 而非 Must-Fix 是合理的。

**[AGREE] R2-W2: 方法技术新颖性极低**

7 个标准统计特征（entropy mean/std/max/min, tail slope, TTR, hapax ratio）+ 现成 XGBoost（§3.3, §3.4），确实无 non-trivial 算法贡献。论文的核心新颖性在于 task formulation 和 DDR empirical finding，而非 method。

但我认为 R2 对此的权重可能偏高——对于 Findings track，task definition + empirical insight 的新颖性是可接受的，不要求方法本身突破。我的 Excitement 评分（3.0）高于 R2（2.5）正是因为我认为 task novelty 部分补偿了 method simplicity。

**[AGREE] R2-W3: Downstream utility null result 占正文空间过多**

§4.4（page 7–8）占约 1/4 页，在 8 页限制下确实昂贵。结合 R2-N1 的超页问题，将 §4.4 核心结论压缩为 1–2 句话留在正文，详细 TOST 分析移入附录，是最直接的 compression 方案。这同时缓解我提出的 W3（n=3 统计功效不足）——附录中可以更充分讨论功效限制，不占正文宝贵空间。

**[AGREE] R2-W4: Gen-0 seed sharing 偏差需量化**

与我的 N2 一致。论文目前仅定性承认偏差（Table 1 footnote: "3-class F1 may carry upward bias"），但未量化：如果 gen-0 分类准确率从实际的 ~95%（从 per-class confusion matrix, Appendix G 可推算）降至 ~70%（无泄露的预期水平），3-class F1 将下降多少？Table 7（page 14, Appendix D）中 5-class LOGO 的 gen-0 per-class F1 = 0.921 异常高，进一步支持 gen-0 泄露的怀疑。

具体建议：通过 bootstrap 模拟或 ablation（对 gen-0 samples 做 per-fold unique seed split）量化偏差幅度。

**[AGREE] R2-W5: 附录 6-gen subset 与正文 8-gen 不一致**

Table 1 footnote（page 6）披露 cross-model chains 仅用 5 个原始 generator（Pythia, OLMo, Qwen），Llama/Mistral 后加入仅做 single-generator 评估。Appendix D（5-class, Table 6）使用 6 generators（排除两个并未说明是哪两个）。Appendix K（classifier comparison, Table 11）也用 6 generators。这些 subset 变化分散在 footnote 中，读者很难追踪哪些结论基于哪些 generator pool。

建议：在 §3.2 或 §3.4 用一个清晰的表格或段落统一说明各评估方案使用的 generator subset 及理由。

---

### Minor 逐条回应

**[AGREE] R2-M1**: Appendix D "Notably" 是典型 AI 写作标记，应删除。与论文整体较好的去 AI 风格不一致。

**[AGREE] R2-M2**: RTX 5090 是 2025 年初发布的消费级 GPU。在 double-blind 审稿下不会造成身份泄露问题，但可能引发计算环境可复现性疑问（不是所有审稿人都有该硬件）。建议改为通用描述或补充在其他 GPU 上的兼容性说明。

**[AGREE] R2-M3**: documentclass 格式应统一，确保与 ARR 要求一致。

**[AGREE] R2-M4**: 6 条 bib 未被 OpenAlex 收录是 API 覆盖限制，非论文问题。我的引用验证同样确认这一点（6 条 not_found 均为知名论文：DetectGPT, Pythia, XGBoost 等）。

**[AGREE] R2-M5**: Table 4 显示 4-det+surface（3-class F1=0.768, binary F1=0.698）在两个指标上均略高于 7-feature（0.762, 0.694）。论文仅强调计算效率优势（"2.4× computation"），但对数值上被 ensemble baseline 超越这一事实的坦率度不够。正文应明确承认 "the ensemble achieves marginally higher F1 at substantially higher computational cost"。

---

### 对 R2 Missing References 的回应

R2 建议可选引用 Agent Drift (2601.04170) 和 Visual Fingerprints (2605.06054)。这两篇与本文有一定相关性（都涉及 LLM 输出的特征分析），但非 must-cite。如果正文空间充裕（解决 N1 后），可在 Related Work §2.1 补充。

---

### R1 vs R2 评分差异分析

| 维度 | R1 | R2 | 差异原因 |
|------|----|----|---------|
| Soundness | 3.0 | 3.5 | R2 未发现温度矛盾（我的 N1），该问题直接损害 soundness |
| Excitement | 3.0 | 2.5 | R2 更重技术方法新颖性（W2），我认为 task definition novelty 部分补偿 |
| Overall | 3.0 | 2.5 | 差异主要来自 excitement 权重 |

**关键分歧**：R2 的 Soundness 3.5 可能偏高——**温度参数矛盾**（§3.2 写 temperature=0，Limitations 写 temperature=0.7，Appendix H/O 确认默认 0.7）是一个 R2 未捕获的 critical reproducibility issue，应将 Soundness 下调至至少 3.0。

**共识区域**：两位 reviewer 在 N2（选择性报告/gen-0 偏差）、N3（base-model-only 限制未充分声明）上高度一致，这两个问题是决定论文能否接收的核心。

**建议 Overall**：维持我的 3.0（Findings track 可接收），但条件是 N1（温度矛盾）和 N2（指标报告）必须修正。如果作者能同时回应 R2-N1（页数）和补充 instruct model 实验讨论，可考虑 3.5。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 662 · 2026-05-17T18:23:55.401882+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 66

## Round 66

2 recorded events


### User

_source line 663 · 2026-05-17T18:24:00.478538+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

要点总结：
- 对 R2 的 3 个 Must-Fix 全部 **[AGREE]**（页数溢出、选择性报告、base-model 限制）
- 对 R2 的 5 个 Should-Fix 中 4 个 **[AGREE]**（W2-W5），仅对 W1（DDR 机制解释不充分）部分 **[REBUT]**——hedging 语言在实证研究中是科学恰当的
- 指出 R2 遗漏了一个 critical issue：**温度参数矛盾**（§3.2 vs Limitations），这使得 R2 的 Soundness 3.5 评分偏高
- 维持 Overall 3.0（Findings track），两位 reviewer 在核心问题上形成共识

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 664 · 2026-05-17T18:24:05.128266+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 67

## Round 67

10 recorded events


### User

_source line 665 · 2026-05-17T18:24:28.866541+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R1-N1: §3.2 温度参数内部矛盾（"temperature=0"）**

R1 称 §3.2 写 "temperature=0"，但这与源文不符。§3.2 (method.tex line 32) 原文为：

> "All generation uses temperature τ=0.7, nucleus sampling with p=0.9, and maximum length of 256 new tokens."

τ=0.7 表述明确，与 Limitations（line 28: "default analysis uses fixed decoding parameters (temperature 0.7, nucleus p=0.9)"）和 Appendix B sampling ablation（Table: Default config Temp=0.7, Top-p=0.90）完全一致。**不存在内部矛盾。** R1 可能将 LaTeX 渲染中的 `$\tau{=}0.7$` 误读为 "0"（τ 与 0 在某些字体下形似），或将 temperature 与其他参数混淆。这不构成可复现性缺陷。

---

**[AGREE] R1-N2: Gen-0 seed sharing 高估主指标**

完全同意。我在独立审稿中也将此列为 Should-Fix (W4)。Table 1 caption 自己承认 "3-class F1 may carry upward bias from gen-0 seed sharing across generators"。Binary F1=0.694（排除 gen-0，无泄露）应作为主指标。

补充一点 R1 未提及的：论文未量化 gen-0 sharing 的实际影响幅度。建议作者在 LOGO 训练集中去除 held-out generator 的 gen-0 样本后重跑，直接量化 3-class metric 的 inflation magnitude。

---

**[AGREE] R1-N3: 仅 base model，instruct model 下 F1=0.338**

完全同意。我在独立审稿中将此列为 N3 (critical)，措辞几乎相同。核心问题不仅是性能下降本身，而是 Abstract 完全未提及 "base model" 限定词，Introduction 仅用一句话带过（line 13），导致 framing 与实际贡献范围不匹配。

Limitations §提供了部分解释（"length regulation, format constraints, safety-driven distribution shaping"），但这是 symptom description 而非 root cause analysis。R1 的 Q3 问得好——instruct 模型 depth signal 衰减的根本机制未被分析。

---

### Should-Fix

**[AGREE] R1-W1: DDR 阈值 |ρ|>0.60 / <0.10 缺乏正式依据**

同意阈值本身是 post-hoc 的。我在独立审稿中（W2）也指出 "DDR 中 drifting vs stationary 的分组本质上是对 Spearman |ρ| 的二值化，缺乏理论依据"。

不过，这个 concern 的严重性需要 nuance：7 个特征的 |ρ| 自然形成两个明确的 cluster（0.60–0.63 vs <0.10），中间只有 entropy_std（|ρ|=0.17）作为 intermediate。6 倍 magnitude gap 使得具体阈值选择对结论影响不大——无论阈值定在 0.30 还是 0.50，分组结果不变。论文应补充 sensitivity analysis 说明这一点，而非让阈值看起来是任意选择。

---

**[AGREE] R1-W2: Levene test 全 reject 与 "approximately preserves shape" 张力**

同意存在 framing 张力。论文在 §4.2 (results.tex line 72) 部分回应了这个问题：

> "coefficient of variation shift <3% for entropy max vs. >15% for hapax ratio"

即 shape 特征的 variance 变化在量级上远小于 drifting 特征。Levene test 全 reject 是因为 N=37,058 时统计功效极高，微小的 variance 差异也能达到显著。这是大样本下 significance vs. effect size 的经典问题。

建议作者明确使用 effect size measure（如 η² 或 variance ratio）替代单纯的 p-value 报告，以更准确地描述 "approximately stationary"。当前的 "all $p < 10^{-10}$" 与 "approximately preserves shape" 确实给人矛盾印象。

---

**[AGREE] R1-W3: Downstream n=3 seeds 功效不足**

同意。3 seeds 下 Cohen's $d$ 值膨胀至 86–120（appendix_downstream.tex line 69-70），论文自己也承认 "artificially inflating d"。TOST 框架在一定程度上缓解了这个问题（用预设 relative margin 而非 effect size），但 n=3 的统计功效仍然很弱。我在独立审稿中将整个 downstream section 定位为空间效率问题（W3），建议移至附录。

---

**[AGREE] R1-W4: 模型规模有限（0.6B-8B），无 >10B model**

同意。论文自身发现了 scale effect（Table 1: Mistral-7B binary F1=0.633，Qwen3-8B=0.692，均低于均值 0.694），且 Limitations line 13 承认 "Frontier models (70B+) remain untested"。这意味着论文的发现在更大模型上可能不成立。不过对于 Findings 定位的 phenomenon paper，我认为这是一个 acknowledged limitation 而非 fatal flaw。

---

**[AGREE] R1-W5: Cross-model 仅 5/8 generators**

同意。我在独立审稿中也将此列为 W5。Table 2 (cross-reference model validation) 和 cross-model chain evaluation 均使用 5-generator subset（Pythia, OLMo, Qwen），排除了后加入的 Llama 和 Mistral。论文在 §4.1 footnote 中解释了原因（"Cross-model chains use the original five-generator subset; Llama and Mistral were added later for single-generator evaluation"），但这仍削弱了 cross-model 结果的普适性。

---

**[REBUT] R1-W6: Multi-detector ensemble "2.4×" 基础不明**

Table 4 (baselines, results.tex) 最后一列明确给出了 ms/text：7-feature = 9.7 ms/text，4-det + surface = 22.8 ms/text。22.8 / 9.7 = 2.35 ≈ 2.4×。同一 caption 还给出了 memory 对比：7-feature 需要一个 410M reference model (905 MB)，4-det ensembles 需要两个模型共 1.4B 参数 (2,868 MB)，memory ratio = 3.2×。

这些数据在论文中有明确记录。R1 可能忽略了 Table 4 的 ms/text 列和 caption 的 memory 信息。

---

### Minor

**[REBUT] R1-M1: Mistral-7B attrition 原因不明**

如果 R1 指的是样本 attrition：Appendix A (appendix_dataset_stats.tex) 显示 Mistral-7B 有 4,849 samples，是所有 8 个 generator 中**最多**的（vs Pythia-1B: 4,555，Qwen3-0.6B: 4,538）。Mistral 的 chain break rate 实际上最低，不存在 attrition 问题。

如果 R1 指的是性能衰减（F1=0.633，最低）：Discussion line 11 和 Limitations line 12 将此归因于 scale effect（"larger generators exacerbate this"），与 Qwen3-8B (0.692) 的类似趋势一致。不过同意这可以更具体——7B Mistral 与 8B Qwen3 的 F1 差距（0.633 vs 0.692）可能还涉及 model family 差异（不同 pretraining data distribution），不仅仅是 scale。

---

**[未独立验证] R1-M2: Figure 2 strip plot 标签重叠**

我的视觉审查未聚焦于此。需要查看 PDF 原图确认。

---

**[REBUT] R1-M3: §2.2 Geng et al. 区分不够充分**

不同意。§2.2 (related_work.tex lines 23-31) 提供了三点明确区分：(i) non-paraphrastic continuation chains vs paraphrasing/translation chains；(ii) handcrafted features vs model-internal representations，enabling DDR decomposition；(iii) estimating depth vs characterizing convergence dynamics。

更重要的是，lines 28-31 进一步解释了两篇工作为何独立收敛到约三类的相同 ceiling，并从互补角度分析了各自的贡献（markovian_chains: why convergence occurs via attractor dynamics; 本文: what converges vs what remains stable via DDR decomposition）。

这是 Related Work 中最强的段落之一。对于一个有 two concurrent works 的 §2.2 来说，覆盖度是充分的。

---

**[AGREE] R1-M4: Appendix E QLoRA 超参差异大**

部分同意。QLoRA 使用 Qwen3-0.6B-Base（0.6B 参数），而主实验 reference model 是 Pythia-410M，两者在架构和规模上不同。不过 appendix_qlora.tex line 29-30 报告了 hyperparameter robustness check（LoRA rank 16 vs 32, different seed），3-class F1 稳定在 0.905±0.004（ΔF1 < 1pp）。QLoRA 的目的是证明 "deeper signal exists beyond handcrafted features"，而非作为一个 production method，这个定位是合理的。

---

### Questions

**Q1**: 温度是 0.7。见上方 N1 rebuttal。

**Q2**: Per-generator unique seed 实验——论文未做。这是一个有价值的建议，可以彻底消除 gen-0 sharing 问题。但这需要对每个 generator 单独采样不同的 Wikipedia seed，可能引入 content variation 作为混淆因素。Tradeoff 需要权衡。

**Q3**: Instruct model depth signal 衰减根因——论文给出了 symptom description（length regulation, format constraints, safety-driven shaping, Limitations lines 7-9），但确实缺乏 mechanistic analysis。例如：instruct tuning 是通过压缩 NLL 分布的 variance 来消除 depth signal 的（使所有 depth 的特征值趋同），还是通过引入 structured formatting patterns 遮盖了 DDR？这两种机制的区分对 future work 有指导意义。

**Q4**: DDR 在不同 family 间的一致性——Figure 1 (fig1_differential_response.pdf, per-generator strip plot) 展示了 per-generator variation。§4.2 和 Table 2 的 cross-family reference 实验（spread=0.013）确认了 DDR 的 cross-family consistency。但 R1 的问题可能更深：drifting/stationary 的分组是否在每个 family 内部都成立？论文未明确报告 per-family Spearman ρ。

**Q5**: Depth fingerprinting 是否本质依赖 small model quality gap——Table 1 中 scale effect（larger models → lower F1）和 Discussion line 18（instruction-tuned models F1=0.338）确实暗示：当 model 生成质量越接近 human text，depth signal 越弱。这是否意味着 DDR 只是 "model quality detection" 的一个 proxy？这是一个深层次的概念问题，如果答案是 "yes"，则 DDR 的独立贡献会大打折扣。

---

### 与我独立审稿的一致/冲突总结

| R1 问题 | R2 独立审稿 | 一致性 |
|---------|------------|--------|
| N1 温度矛盾 | 未发现此问题 | **冲突**：R1 可能误读源文 |
| N2 Gen-0 sharing | W4 (Should-Fix) | **一致**：都认为需修改，R1 定为 critical 更严 |
| N3 Base-model only | N3 (Must-Fix) | **完全一致** |
| W1 DDR 阈值 | W2 (部分) | **一致** |
| W2 Levene tension | 未独立提出 | **R1 新发现**：有效观察 |
| W3 Downstream n=3 | W3 (positioning) | **一致方向不同**：R1 关注统计功效，我关注空间效率 |
| W6 2.4× basis | 未提出 | **冲突**：Table 4 有明确数据 |
| M3 Geng et al. | S1 中肯定覆盖充分 | **冲突**：我认为区分充分 |

**R2 独立发现但 R1 未提出的问题：**
- N1 正文超页数限制（~1/3 页）——这是格式硬约束
- N2 Abstract/Introduction 选择性报告性能数字（cross-model vs LOGO 优先级）
- "6-11 pp" 改进范围不准确（实际 6-36 pp）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-17T18:25:00.109074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "offset": "30",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
    "offset": "30",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-17T18:25:00.159676+00:00_

30	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
31	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
32	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
33	The theoretical yield is $8 \times {\sim}1{,}000 \times 5 = 39{,}815$ texts; after removing 2{,}746 chain breaks (empty or degenerate outputs at intermediate depths that prevented deeper generation) and 11 passages too short for feature extraction, 37{,}058 texts remain (Appendix~\ref{app:dataset-stats}).
34	For classification, depths 2--4 are collapsed into the $2{+}$ class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-17T18:25:31.084701+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-17T18:25:31.135366+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

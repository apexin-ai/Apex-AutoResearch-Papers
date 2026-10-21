# Director coordination — Part 5 of 5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Structured JSON](../../../sessions/5a/5a5f768420cdca035482.json)

## Round 113

### Tool result

_source line 1458 · 2026-05-25T21:29:39.028982+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (269 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无 — 4 GPU 全部空闲）\n\n## D&R 阈值扫描结果（完整）\n| 阈值 | 数据保留 | holdout_ppl | owt_ppl | wiki_ppl | seeds |\n|------|---------|-------------|---------|----------|-------|\n| q>0.3 | 31.5% | 17.25 | — | — | 3 (prior) |\n| q>0.5 | 41.4% | 17.291 | 18.02 | 15.06 | 1 (ckpt-5500) |\n| q>0.7 | 50.0% | 17.32 | 18.04 | 15.11 | 3 |\n| Uniform | 100% | 17.694 | — | — | baseline |\n| Adaptive b* | 100% | 17.674 | — | — | baseline |\n\n## 近期结论\n- **q07 三 seed 完成** (success): holdout=17.32±0.00, owt=18.04±0.01, wiki=15.11±0.01 — 方差极小\n- **q05 ckpt-5500** (success): holdout=17.291, owt=18.02, wiki=15.06（final model 因 optimizer corruption 废弃）\n- **所有 D&R 阈值均显著优于 Uniform (17.694) 和 Adaptive b* (17.674)**\n\n## 趋势\n成功 175 / 负向 14 / 失败 42 / 共 254\n\n## 下一步\n- Paper Agent 可用完整 D&R 数据更新论文\n- 4 GPU 空闲待命\n\n## 资源状态\nwestd-41312: cuda:0/1/2/3 全部空闲\n\n## 告警\n- detector_modernbert: 已被终止 — unknown\n- diagnostic_contamination100: 已被终止 — unknown\n- adaptive_v2_seed42: 已被终止 — unknown\n- adaptive_v2_seed123: 已被终止 — unknown\n- adaptive_v2_seed456: 已被终止 — unknown\n- grid_b_low_seed42: 训练失败 — unknown\n- tau_0.6_seed42: 已被终止 — unknown\n- bs8_seed42: 训练失败 — unknown\n- bs8_nmin2_seed42: 训练失败 — unknown\n- contamination_60_
…[truncated 1820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 753
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-25T21:29:39.129824+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-25T21:29:39.230606+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

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
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-25T21:29:39.281310+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:16:30.826651+00:00\", \"completed_at\": \"2026-05-25T21:19:03.302021+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（纯文本：Title + Abstract + Introduction 开头）。Figure 1 出现在 page 2 顶部，仍在前 2 页内，审稿人锚定效应尚可，但若能将 Figure 1 或一个精简版概念图提至首页底部效果更佳\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 三子图(a)(b)(c)的 legend 文字和 axis label 字号偏小（约正文 55-60%），尤其 subplot (a) 的 legend 与数据线有轻微视觉拥挤。建议放大 legend 字号至正文 70%+ 或移至图外\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 2（架构概览图）仅占单栏宽度。作为传达核心方法的概览图，建议改用 figure*（全宽）以提升可读性和视觉冲击力\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗，格式规范。Figure 3 双子图 axis label 字号偏小但可读\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 最优结果加粗标注，精度统一（小数点后 3 位）。Figure 4 清晰可读，caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figures 5 & 6 并排布局合理。Figure 5 legend 文字偏小（4 条 legend 项），建议适当放大。Figure 6 有 error bars + shaded region，统计信息呈现好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"本页 display items 密度最高（Table 3 + Table 4 + Figure 7），视觉上略拥挤但内容关联紧密，可接受。Figure 7 bar chart 使用颜色+斜线纹理区分类别，色盲友好性好\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 8 stacked bar chart 使用 5+ 种颜色类别，部分相邻色段（如浅蓝与浅绿）在灰度打印下可能难以区分。建议增加纹理填充或减少颜色类别数\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 5（决策摘要表）使用颜色背景行高亮不同条件，视觉效果好。主文正好 8 页（§1-§7），符合 EMNLP 2026 的 8 页限制\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 节简洁（3 个要点：Scope / Detector coverage / Evaluation scope），符合 EMNLP 要求。References 格式统一，无 [?] 未解析引用\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Algorithm 1 伪代码框排版整齐。Figure 9 轨迹图清晰。Tables 6-8 密度高但作为 Appendix 可接受\"}, {\"severity\": \"info\", \"d
…[truncated 303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-25T21:30:45.170166+00:00_

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

_source line 1463 · 2026-05-25T21:30:45.573043+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1464 · 2026-05-25T21:30:45.824158+00:00_

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

_source line 1465 · 2026-05-25T21:30:45.874752+00:00_

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

_source line 1466 · 2026-05-25T21:31:19.765060+00:00_

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

_source line 1467 · 2026-05-25T21:31:20.167394+00:00_

1	issues:
2	# === Round 10 issues (all resolved, retained for history) ===
3	- id: "R10-C1"
4	  summary: "Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 10
9	  last_seen_round: 10
10	  mentions:
11	    - round: 10
12	      reviewers: [1, 2]
13	      note: "Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。"
14	  resolution: "tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。"
15	  resolution_round: 10
16	
17	- id: "R10-C2"
18	  summary: "多重比较未校正，p=0.025 Bonferroni 校正后不显著"
19	  category: experiment
20	  severity: critical
21	  status: resolved
22	  first_raised_round: 10
23	  last_seen_round: 10
24	  mentions:
25	    - round: 10
26	      reviewers: [1, 2]
27	      note: "6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。"
28	  resolution: "BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。"
29	  resolution_round: 10
30	
31	- id: "R10-C3"
32	  summary: "方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配"
33	  category: framing
34	  severity: critical
35	  status: resolved
36	  first_raised_round: 10
37	  last_seen_round: 10
38	  mentions:
39	    - round: 10
40	      reviewers: [1, 2]
41	      note: "w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。"
42	  resolution: "§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。"
43	  resolution_round: 10
44	
45	- id: "R10-C4"
46	  summary: "Downstream task 零改善削弱实际意义"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 10
51	  last_seen_round: 10
52	  mentions:
53	    - round: 10
54	      reviewers: [1, 2]
55	      note: "Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。"
56	  resolution: "Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limit
…[truncated 19415 chars]

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

_source line 1468 · 2026-05-25T21:31:20.318383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "150"
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
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1469 · 2026-05-25T21:31:20.369050+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\graphicspath{{../../artifacts/figures/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{algorithm}
15	\usepackage{algorithmic}
16	\usepackage{booktabs}
17	\usepackage{multirow}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	\setlength{\textfloatsep}{6pt plus 2pt minus 2pt}
30	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
31	\setlength{\abovecaptionskip}{4pt plus 1pt minus 1pt}
32	\setlength{\belowcaptionskip}{0pt}
33	\title{When Does Detect-and-Reweight Work for Synthetic Contamination?}
34	
35	\author{Anonymous}
36	
37	\begin{document}
38	\maketitle
39	
40	\begin{abstract}
41	\input{sections/abstract}
42	\end{abstract}
43	
44	\section{Introduction}
45	\label{sec:intro}
46	\input{sections/introduction}
47	
48	\section{Related Work}
49	\label{sec:related}
50	\input{sections/related_work}
51	
52	\section{Method}
53	\label{sec:method}
54	\input{sections/method}
55	
56	\section{Experimental Setup}
57	\label{sec:experiments}
58	\input{sections/experiments}
59	
60	\section{Results}
61	\label{sec:results}
62	\input{sections/results}
63	
64	\section{Discussion}
65	\label{sec:discussion}
66	\input{sections/discussion}
67	
68	\section{Conclusion}
69	\label{sec:conclusion}
70	\input{sections/conclusion}
71	
72	\section*{Limitations}
73	\label{sec:limitations}
74	\input{sections/limitations}
75	
76	\bibliography{references}
77	
78	\appendix
79	\input{sections/appendix}
80	
81	\end{document}
82	

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

_source line 1470 · 2026-05-25T21:31:29.897635+00:00_

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

_source line 1471 · 2026-05-25T21:31:30.350032+00:00_

1	As synthetic text pervades web corpora, detect-and-reweight methods that downweight likely-synthetic samples during training have emerged to prevent model collapse, yet when they actually help remains unclear.
2	We investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.
3	First, detect-and-remove (D\&R) outperforms all reweighting methods in our setting; epoch-matched controls attribute over 95\% of the advantage to multi-epoch exposure on filtered data, identifying the mechanism behind D\&R's effectiveness.
4	Second, the detector must provide both sufficient discrimination \emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.
5	Third, minimum intervention, applying the smallest reweighting exponent that meets a quality floor, outperforms unconstrained weight maximization.
6	As an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\bstar$ that improves over uniform training at contamination ratios $\rho \geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.
7	These findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established\footnote{Code and data are available at \url{https://anonymous.4open.science/r/provenance_weight_training-F72D/}.}.
8	

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

_source line 1472 · 2026-05-25T21:31:30.450812+00:00_

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

_source line 1473 · 2026-05-25T21:31:30.953401+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\setlength{\tabcolsep}{3pt}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
9	\midrule
10	Uniform                & 17.694 & 17.686 & 17.702 & 17.697 $\pm$ .008 \\
11	Adaptive $\bstar$ (ours) & \textbf{17.680} & \textbf{17.666} & \textbf{17.677} & \textbf{17.674} $\pm$ .006 \\
12	ESS-only               & 17.730 & 17.720 & 17.760 & 17.737 $\pm$ .021 \\
13	Random $\mathcal{U}(0,2)$ & 17.830 & 17.800 & 17.777 & 17.802 $\pm$ .027 \\
14	Permuted $q$-scores  & 17.919 & --     & --     & 17.919 \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Main comparison: held-out PPL ($\downarrow$) at $\rho{=}0.4$, 1 content epoch.
18	Adaptive and Uniform: 5-seed means (seeds 42, 123, 456, 789, 234); ESS-only and Random: 3-seed means (seeds 42, 123, 456); Permuted: single seed (42).
19	Adaptive uses $\tau{=}0.7$, $\nmin{=}2$.
20	Permuted randomly shuffles $q$-scores across samples, destroying provenance signal while preserving weight non-uniformity ($\Delta{=}{+}0.225$).}
21	\label{tab:main}
22	\end{table}
23	
24	\subsection{Main Results}
25	\label{sec:main-results}
26	
27	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
28	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
29	
30	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
31	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
32	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{dray
…[truncated 13772 chars]

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

_source line 1474 · 2026-05-25T21:31:30.953807+00:00_

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

_source line 1475 · 2026-05-25T21:31:31.004421+00:00_

1	\paragraph{D\&R as the strongest strategy.}
2	D\&R outperforms all reweighting methods by $0.35$--$0.42$ PPL (Table~\ref{tab:epoch_match}), but epoch-matched controls attribute ${>}$95\% of this advantage to multi-epoch exposure on filtered data rather than superior per-token learning.
3	This benefit was invisible in \citet{drayson2025detection}, where from-scratch pretraining rarely completes one epoch; in continued pretraining, it becomes the dominant factor.
4	
5	\paragraph{When uniform beats reweighting.}
6	Table~\ref{tab:decision} summarizes three prerequisites for effective soft reweighting: (i)~sufficient detector discrimination \emph{and} calibration (AUC\,$\geq$\,0.9, ECE\,$\leq$\,0.05; \S\ref{sec:robustness}); (ii)~contamination $\rho \geq 0.4$, below which the method degrades ($+$0.046 at $\rho{=}0.2$; Appendix~\ref{app:rho02}) with a sharp transition in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}); (iii)~generator--trainee mismatch (at 1.7B the benefit diminishes to $\Delta{=}{-}0.013$ with OOD mixed).
7	When any condition is violated, uniform is the safer default.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\setlength{\tabcolsep}{3pt}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}lcll@{}}
15	\toprule
16	\textbf{Condition} & \textbf{Observed?} & \textbf{Evidence} & \textbf{$\Delta$ PPL} \\
17	\midrule
18	Detector AUC $\geq 0.9$ & Yes & N-gram (0.73) degrades & $+$0.129 \\
19	Detector ECE $\leq 0.05$ & Yes & GPT-2 (0.131) degrades & $+$0.098 \\
20	Contamination $\rho \geq 0.4$ & Yes & $\rho{=}0.2$ degrades & $+$0.046 \\
21	Generator $\neq$ trainee & Tentative & 1.7B: $\Delta{=}{-}0.013$, OOD mixed & -- \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Decision summary for practitioners.
25	$\Delta$ values are relative to uniform (positive = worse).
26	When any observed condition is violated, uniform is the safer default.}
27	\label{tab:decision}
28	\end{table}
29	
30	\paragraph{Effect size and downstream impact.}
31
…[truncated 1062 chars]

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

_source line 1476 · 2026-05-25T21:31:57.996878+00:00_

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


### Tool call

_source line 1477 · 2026-05-25T21:31:57.997409+00:00_

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

_source line 1478 · 2026-05-25T21:31:58.048014+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (i)~D\&R is the strongest method in our setting, with multi-epoch exposure on filtered data accounting for ${>}$95\% of its advantage over reweighting; (ii)~detector calibration alongside discrimination, as high-AUC detectors with poor calibration degrade PPL below uniform; and (iii)~minimum intervention over unconstrained maximization, supported by the ESS-only ablation and the fixed-$b$ grid curve (Figure~\ref{fig:grid_b_trend}).
2	A dual-constrained adaptive $\bstar$ implementing these principles improves over uniform training at $\rho \geq 0.4$ without per-model tuning (Table~\ref{tab:decision}), though without measurable downstream gains at 0.6B scale.
3	Whether these conditions hold at full pretraining scale ($>$100B tokens), where contamination ratios are lower but corpora are harder to curate, is the central open question; a second priority is extending the detector--calibration axis to neural classifiers whose ECE profiles differ qualitatively from the TF-IDF family tested here.
4	

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


### Tool result

_source line 1479 · 2026-05-25T21:31:58.048420+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	\begin{figure*}[t]
6	\centering
7	\includegraphics[width=\textwidth]{fig1_overview}
8	\caption{Three effectiveness conditions for detect-and-reweight.
9	\textbf{(a)}~D\&R achieves the best raw PPL; epoch-matched controls reveal that multi-epoch exposure on filtered data accounts for the bulk of the advantage (\S\ref{sec:results}).
10	\textbf{(b)}~Only detectors with both high AUC \emph{and} low ECE fall in the effective zone; comparable AUC with poor calibration degrades PPL below uniform.
11	\textbf{(c)}~Adaptive $\bstar{\approx}0.9$ operates near the grid-search optimum, while ESS-only $b{\approx}3.5$ falls in the degradation zone.}
12	\label{fig:overview}
13	\end{figure*}
14	
15	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
16	What mechanism drives D\&R's strong performance, and how does it compare to soft reweighting under controlled conditions?
17	What detector properties are necessary for effective reweighting?
18	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
19	
20	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 5 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
21	To ground the analysis of exponent selection, we impleme
…[truncated 1838 chars]

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

_source line 1480 · 2026-05-25T21:36:35.031049+00:00_

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

_source line 1481 · 2026-05-25T21:36:39.984281+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora, though accumulating real data avoids divergence~\citep{kazdan2025collapse} and even minimal curation suffices~\citep{amin2025escaping}.
6	Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
7	
8	\paragraph{Detection, Filtering, and Data Reweighting.}
9	Continuous-score detectors---probability curvature~\citep{mitchell2023detectgpt}, cross-perplexity ratios~\citep{hans2024binoculars}, low-probability token statistics~\citep{shi2024minkprob}---enable document-level weighting~\citep{wu2025survey}.
10	Data composition is optimized via perplexity filtering~\citep{wenzek2020ccnet}, domain-level importance sampling~\citep{xie2023doremi,xie2023dsir,grangier2025crisp,ye2025mixing}, instance-level strategies~\citep{bengio2009curriculum,mindermann2022prioritized,sow2025dynamic,engstrom2024dsdm}, and deduplication~\citep{abbas2023semdedup}; see \citet{albalak2024survey}.
11	None targets synthetic provenance; moreover, classifier-based quality scores may capture stylistic similarity rather than intrinsic quality~\citep{naitsaada2025illusion}.
12	Most directly related, \citet{drayson2025detection} propose $w_j = (1{-
…[truncated 2560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 4953
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-25T21:36:40.135366+00:00_

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

_source line 1483 · 2026-05-25T21:36:40.135715+00:00_

1	\begin{itemize}[nosep,leftmargin=*]
2	\item \textbf{Scope.}
3	All experiments use Qwen3 (0.6B and 1.7B) under self-contamination with 132--200M tokens of continued pretraining.
4	Generalization to other architectures, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination, where generator-corpus distribution mismatch may reduce detector accuracy, remains untested.
5	
6	\item \textbf{Detector coverage.}
7	Only three detectors from two families (discriminative TF-IDF+LR and generative perplexity scorers) were evaluated; fine-tuned neural classifiers (e.g., ModernBERT) and zero-shot methods (e.g., DetectGPT, Binoculars) remain untested, so the AUC/ECE thresholds reported here may shift with broader detector coverage.
8	
9	\item \textbf{Evaluation scope.}
10	Our primary metric is held-out perplexity; downstream accuracy is unchanged across conditions (Appendix~\ref{app:downstream}), so the practical benefit at 0.6B scale is limited to distributional quality rather than task performance.
11	\end{itemize}
12	

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

_source line 1484 · 2026-05-25T21:44:26.797511+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11+ recurring issues (updated with Round 14 fresh review) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。双方 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"论文已升至 5 seeds + BH correction。统计检验力问题部分缓解但 Cohen's d=3.83 被 deterministic data ordering 人为放大。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"N=5 seeds 和 BH correction 已到位。原始 N=3 问题已解决。但衍生出 R14-N1（ρ=0.6 p_BH=0.064 overclaim）。\"\n  resolution: \"主实验升至 5 seeds + BH correction。原始统计检验力问题已解决。\"\n  resolution_round: 14\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.63，Wang (2026) 理论保证不直接转移到 proxy\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 标为 critical。圆桌共识：should-fix（修改 'guarantees' 措辞即可）。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。§6 已有 'Limitations of α_eff as a proxy' 段落（Pearson r≈0.79, ~63% variance, Spearman ρ_s ≥ 0.86），部分改善。但 §3 'motivated by convergence theory' 仍暗示理论保证。\"\n  action_items:\n    - round: 13\n      action: \"将 §3 中 'guarantees a convergence-rate lower bound' 改为 'targets/approximates'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.023 PPL, 0.13% relative），practitioner framing 自相矛盾\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=128 幂律外推被一致认为不可靠。'practical' 表述仍残留。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2+W5 独立提出。核心矛盾仍在。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N3 + R1-N1 再次确认。Abstract 'improves over uniform training' 未限定 metric，读者理解为含下游。实际 downstream 0.5414 vs 0.5415。Conclusion 写了 'without measurable downstream gains' 但 Abstract 未提及。此外 Δ=-0.023 缺 baseline contextualization（无与其他 data curation 方法的量级对比）。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 限定 'improves held-out PPL' + 注明无下游改善。补充 Δ=-0.023 在 continued pretraining 文献中的量级对照。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"标题通用性远超实验 scope：仅 self-contamination + continued pretraining + 0.6B\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Cross-model transfer single seed + mixed + 无 PPL 比较。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 must-fix。建议标题加限定如 '...in Continued Pretraining'。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N2 + R1 AGREE。标题未改。'When Does D&R Work for Synthetic Contamination?' 暗示系统性评估，但实验仅覆盖 self-contamination/0.6B+1.7B/continued pretraining/单一数据源/1 个有效 detector。§6 自述 epoch confound 在 from-scratch 下不适用，但标题未反映。跨 4 轮持续存在。\"\n  action_items:\n    - round: 14\n      action: \"修改标题增加限定词，如 '...in Controlled Continued Pretraining' 或 '...under Self-Contamination at Sub-Billion Scale'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§3 压缩后仍给人独立方法贡献印象。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3 新颖性低。R1 REBUT。圆桌共识：中偏低，不影响评分。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W2 指出 'three effectiveness conditions' framing 仍过度概括。Introduction 已改用 'illustrative application' 和 'three findings'（改善），但 Abstract/Conclusion/Figure 1 仍用 'conditions'（不一致）。'Conditions' 暗示充分必要性，evidence 仅支持 empirical observations。\"\n  action_items:\n    - round: 14\n      action: \"统一使用 'three empirical findings' 或 'three observed requirements'，避免 'conditions' 暗示充分必要性。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作和 detection benchmarks\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议。\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 新增：RAID benchmark (Dugan et al. 2024)、M4 shared task (Wang et al. 2024)。R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"RAID 和 M4 仍缺失。R2-W3 再次提出，R1 AGREE。MATES (Yu et al. 2024) 和 Aioli (Balachandran et al. 2024) 也建议纳入（如涉及 data selection/mixing）。\"\n  action_items:\n    - round: 14\n      action: \"补充 RAID (Dugan et al. 2024) 和 M4 (Wang et al. 2024)。考虑 MATES 和 Aioli。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏 uniform+multi-epoch baseline\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Epoch confound 适用范围需限定为 multi-epoch exposure 场景。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2：缺 uniform × 3.2 epochs baseline。R2 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍缺失。R1-W2 再次提出（缺 uniform × 3.2 epochs），R2 AGREE 且认为计算成本低但对分析完整性至关重要。无法区分纯重复训练 vs 选择性重复高质量数据的贡献。\"\n  action_items:\n    - round: 14\n      action: \"增加 uniform+multi-epoch baseline（全数据 ~3.2 epochs），完善 epoch confound 分析。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 可读性和 display item 分布问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"ρ 符号冲突、Figure 1 黑白不可辨。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"视觉审查发现 page 6 含 4 个 display items 密度过高。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 reviewers 未独立提出。视觉审查（Round 14）发现 Figure 8 灰度打印问题（warning）、多处 axis label 字号偏小（info）。整体有所改善。\"\n  action_items:\n    - round: 14\n      action: \"Figure 8 增加纹理填充。考虑放大 Figure 1/3/10 axis label 字号至正文 70%+。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 issues (updated with Round 14) ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"LaTeX wc 确认 225 words。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 ~155 words，合规。\"\n  resolution: \"Abstract 已压缩至 ~155 words，符合 ≤200 words 限制。\"\n  resolution_round: 13\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§7 Conclusion 溢出至第 9 页。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 §1-§7 在 page 8 内。合规。\"\n  resolution: \"正文已压缩至 8 页内。\"\n  resolution_round: 13\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个），不足以支撑 AUC/ECE threshold 的通用性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"仅 TF-IDF+LR / GPT-2 / N-gram。3 个数据点不足建立因果关系。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 + R1 AGREE。缺少 neural detectors。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2-W4 再次确认。Table 5 将 AUC≥0.9/ECE≤0.05 作为 binary threshold 但仅 3 个数据点。AUC=0.88/ECE=0.04 区间无 empirical support。Limitations 已承认，但 Table 5 'for practitioners' 定位与 evidence 有张力。\"\n  action_items:\n    - round: 14\n      action: \"扩展 detector coverage（至少 1 个 neural detector），或将 threshold 标注为 'observed in our 3 detectors, not general guidance'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size scaling 趋势基于 3 个数据点，power law fitting 不可靠\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=4/8/16 仅 3 点，外推到 B=128 不可靠。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"未再单独提及，可能已部分改善。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。§5.3 现报告 monotonic trend 和 amplification factor（1.0×/2.3×/3.0×），未见 power law fitting 外推。可能已改善。\"\n  action_items:\n    - round: 12\n      action: \"确认是否已删除 power law fitting，保留 monotonic trend 描述。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"建议将 Spearman 改为 ρ_s。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未提及。§6 Discussion 使用 'Spearman ρ_s ≥ 0.86'，表明已部分修正。需验证全文一致性。\"\n  action_items:\n    - round: 12\n      action: \"全文 Spearman ρ → ρ_s\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 13 issues (updated with Round 14) ===\n\n- id: \"R13-W1\"\n  summary: \"B=4 micro-batch 上 dual constraint 统计可靠性不足，主实验在次优设定运行\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE。B=4 MAE=0.114，advantage 最小（1.0×）。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q3 + R1 AGREE。Modern pretraining micro-batch B=32-128。B=16 仍远低于实际设定。论文应讨论 B=64/128 预期行为和 per-batch α_eff 估计稳定性。\"\n  action_items:\n    - round: 14\n      action: \"讨论 B=64/128 时的预期行为（external extrapolation）。可选：补充 B=32 实验。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Grid-best b=0.3 vs adaptive b*≈0.9 偏差：α_eff 负偏差导致过度干预\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"因果链：α_eff 负偏差 → quality floor 过早绑定 → b_τ 推高 → b*≈0.9 远高于 grid-best b=0.3。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q1 间接涉及：当 D&R 总优于 adaptive 时，adaptive 的 use case 不清楚。Grid-best b=0.3 vs adaptive b*≈0.9 的 gap 仍未解释。\"\n  action_items:\n    - round: 13\n      action: \"补充 per-batch b* 分布（median, percentiles）。分析 α_eff 负偏差对 b* 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"1.7B 规模效应递减 43% 且 scaling trend 未正式讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE。Δ=-0.013 at 1.7B + OOD mixed。Practitioner 关注 7B-70B 规模可能完全失效。§5.2 仅一段描述，缺 formal scaling analysis。Table 5 'for practitioners' 无 scale caveat。\"\n  action_items:\n    - round: 14\n      action: \"正式讨论 scaling trend 和 implications。在 Table 5 或 Conclusion 加 scale caveat。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W4\"\n  summary: \"ρ≥0.4 实用门槛偏高，实际适用场景极窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2-W7。方法仅在多条件同时成立下有效。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"两位 reviewer 均确认。ρ≥0.4 + calibrated detector + self-contamination + continued pretraining + 0.6B 的交集极窄。'Decision summary for practitioners' 在如此受限范围下可能给读者不准确信号。\"\n  action_items:\n    - round: 14\n      action: \"在 Table 5 或 Conclusion 明确标注完整的适用范围限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"§6 Discussion 第一段与 §5.1 epoch confound 内容重复\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W1 + R1 AGREE。§6 开头仍重述 'D&R outperforms...0.35--0.42 PPL... >95% multi-epoch...'，与 §5.1 高度重合。8 页限制下应精简。\"\n  action_items:\n    - round: 14\n      action: \"精简 §6 第一段为一句概括 + §5.1 交叉引用。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Cohen's d 被 deterministic data ordering 人为放大，效应量不确定性未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"d=3.83 但 σ=0.006 因 data ordering 固定。如果 data shuffle seed 也随机化 paired SD 大概率升高。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。可能因论文未报告 Cohen's d 而不再适用，需确认。\"\n  action_items:\n    - round: 13\n      action: \"报告 Cohen's d + CI，讨论 deterministic data ordering 对 paired SD 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"PPL 改善与模型质量（下游任务能力）之间的关系未讨论\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"在 continued pretraining 中多大 PPL 改善才对应有意义的 capability 提升？\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。§6 Effect size 段引用 Tay et al. 2023 和 Ye et al. 2025 讨论 PPL-accuracy 非线性关系，部分改善。\"\n  action_items:\n    - round: 13\n      action: \"在 Discussion 中简要讨论 PPL-capability 关系。\"\n      assigned_to: director\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m4\"\n  summary: \"Permuted q-scores ablation 仅 1 seed\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Table 1 确认仅 seed-42 有 Permuted 结果。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未独立提出。Table 1 仍显示 Permuted 仅 seed 42（'17.919, --, --'）。\"\n  action_items:\n    - round: 13\n      action: \"补充 permuted q-scores 多 seed 或标注 single-seed 限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 14 新发现 ===\n\n- id: \"R14-N1\"\n  summary: \"Abstract 中 'ρ ≥ 0.4, reaching conventional significance' 对 ρ=0.6 构成 overclaim（p_BH=0.064）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。§5.2 报告 ρ=0.6 p_BH=0.064 > α=0.05。仅 ρ=0.4 p_BH=0.011 达标。Abstract 'at ρ ≥ 0.4, reaching conventional significance' 暗示两个 level 均显著，构成事实性错误。\"\n  action_items:\n    - round: 14\n      action: \"修改 Abstract：改为 'at ρ=0.4 (p_BH=0.011)' 或注明 ρ=0.6 仅 marginal significance。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M1\"\n  summary: \"Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。Caption: '5-seed means (seeds 42, 123, 456, 789, 234)' 但表格仅 3 列。Seeds 789/234 不可见，可能引发选择性报告疑虑。\"\n  action_items:\n    - round: 14\n      action: \"Caption 注明 'full 5-seed results in Appendix X' 或增加 seed 列。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M2\"\n  summary: \"§5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。ρ=0.6 paired t 在正文和附录之间数值不一致。损害 reproducibility。\"\n  action_items:\n    - round: 14\n      action: \"核实并统一 t 值。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M3\"\n  summary: \"'Three effectiveness conditions' vs 'three findings' 术语全文不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。Abstract/Figure 1/Conclusion 使用 'conditions'，Introduction 使用 'findings'。应统一。\"\n  action_items:\n    - round: 14\n      action: \"全文统一术语（建议用 'findings' 或 'observed requirements'）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M4\"\n  summary: \"Appendix P Table 16 seed 456 缺 OOD 评估\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。数据完整性问题。\"\n  action_items:\n    - round: 14\n      action: \"补充 seed 456 OOD 评估或解释缺失原因。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M5\"\n  summary: \"Sliding-window evaluation 未说明 window size 和 stride\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。Reproducibility 要求所有 evaluation hyperparameters 明确。\"\n  action_items:\n    - round: 14\n      action: \"在 §4 或 Appendix 注明 window size 和 stride。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Temperature scaling T=0.204 需要 labeled data，限制实际部署性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q2 + R1 AGREE。Detector calibration 依赖 10K labeled validation split。Web-scale pretraining 中 ground-truth synthetic labels 不可用。限制 Table 5 decision framework 的 deployability。\"\n  action_items:\n    - round: 14\n      action: \"在 Discussion 讨论 unsupervised calibration alternatives。或在 Limitations 加此限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
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
    "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11+ recurring issues (updated with Round 14 fresh review) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。双方 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"论文已升至 5 seeds + BH correction。统计检验力问题部分缓解但 Cohen's d=3.83 被 deterministic data ordering 人为放大。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"N=5 seeds 和 BH correction 已到位。原始 N=3 问题已解决。但衍生出 R14-N1（ρ=0.6 p_BH=0.064 overclaim）。\"\n  resolution: \"主实验升至 5 seeds + BH correction。原始统计检验力问题已解决。\"\n  resolution_round: 14\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.63，Wang (2026) 理论保证不直接转移到 proxy\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 标为 critical。圆桌共识：should-fix（修改 'guarantees' 措辞即可）。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。§6 已有 'Limitations of α_eff as a proxy' 段落（Pearson r≈0.79, ~63% variance, Spearman ρ_s ≥ 0.86），部分改善。但 §3 'motivated by convergence theory' 仍暗示理论保证。\"\n  action_items:\n    - round: 13\n      action: \"将 §3 中 'guarantees a convergence-rate lower bound' 改为 'targets/approximates'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.023 PPL, 0.13% relative），practitioner framing 自相矛盾\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=128 幂律外推被一致认为不可靠。'practical' 表述仍残留。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2+W5 独立提出。核心矛盾仍在。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N3 + R1-N1 再次确认。Abstract 'improves over uniform training' 未限定 metric，读者理解为含下游。实际 downstream 0.5414 vs 0.5415。Conclusion 写了 'without measurable downstream gains' 但 Abstract 未提及。此外 Δ=-0.023 缺 baseline contextualization（无与其他 data curation 方法的量级对比）。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 限定 'improves held-out PPL' + 注明无下游改善。补充 Δ=-0.023 在 continued pretraining 文献中的量级对照。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"标题通用性远超实验 scope：仅 self-contamination + continued pretraining + 0.6B\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Cross-model transfer single seed + mixed + 无 PPL 比较。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 must-fix。建议标题加限定如 '...in Continued Pretraining'。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N2 + R1 AGREE。标题未改。'When Does D&R Work for Synthetic Contamination?' 暗示系统性评估，但实验仅覆盖 self-contamination/0.6B+1.7B/continued pretraining/单一数据源/1 个有效 detector。§6 自述 epoch confound 在 from-scratch 下不适用，但标题未反映。跨 4 轮持续存在。\"\n  action_items:\n    - round: 14\n      action: \"修改标题增加限定词，如 '...in Controlled Continued Pretraining' 或 '...under Self-Contamination at Sub-Billion Scale'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§3 压缩后仍给人独立方法贡献印象。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3 新颖性低。R1 REBUT。圆桌共识：中偏低，不影响评分。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W2 指出 'three effectiveness conditions' framing 仍过度概括。Introduction 已改用 'illustrative application' 和 'three findings'（改善），但 Abstract/Conclusion/Figure 1 仍用 'conditions'（不一致）。'Conditions' 暗示充分必要性，evidence 仅支持 empirical observations。\"\n  action_items:\n    - round: 14\n      action: \"统一使用 'three empirical findings' 或 'three observed requirements'，避免 'conditions' 暗示充分必要性。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作和 detection benchmarks\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议。\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 新增：RAID benchmark (Dugan et al. 2024)、M4 shared task (Wang et al. 2024)。R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"RAID 和 M4 仍缺失。R2-W3 再次提出，R1 AGREE。MATES (Yu et al. 2024) 和 Aioli (Balachandran et al. 2024) 也建议纳入（如涉及 data selection/mixing）。\"\n  action_items:\n    - round: 14\n      action: \"补充 RAID (Dugan et al. 2024) 和 M4 (Wang et al. 2024)。考虑 MATES 和 Aioli。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏 uniform+multi-epoch baseline\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Epoch confound 适用范围需限定为 multi-epoch exposure 场景。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2：缺 uniform × 3.2 epochs baseline。R2 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍缺失。R1-W2 再次提出（缺 uniform × 3.2 epochs），R2 AGREE 且认为计算成本低但对分析完整性至关重要。无法区分纯重复训练 vs 选择性重复高质量数据的贡献。\"\n  action_items:\n    - round: 14\n      action: \"增加 uniform+multi-epoch baseline（全数据 ~3.2 epochs），完善 epoch confound 分析。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 可读性和 display item 分布问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"ρ 符号冲突、Figure 1 黑白不可辨。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"视觉审查发现 page 6 含 4 个 display items 密度过高。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 reviewers 未独立提出。视觉审查（Round 14）发现 Figure 8 灰度打印问题（warning）、多处 axis label 字号偏小（info）。整体有所改善。\"\n  action_items:\n    - round: 14\n      action: \"Figure 8 增加纹理填充。考虑放大 Figure 1/3/10 axis label 字号至正文 70%+。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 issues (updated with Round 14) ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"LaTeX wc 确认 225 words。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 ~155 words，合规。\"\n  resolution: \"Abstract 已压缩至 ~155 words，符合 ≤200 words 限制。\"\n  resolution_round: 13\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§7 Conclusion 溢出至第 9 页。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 §1-§7 在 page 8 内。合规。\"\n  resolution: \"正文已压缩至 8 页内。\"\n  resolution_round: 13\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个），不足以支撑 AUC/ECE threshold 的通用性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"仅 TF-IDF+LR / GPT-2 / N-gram。3 个数据点不足建立因果关系。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 + R1 AGREE。缺少 neural detectors。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2-W4 再次确认。Table 5 将 AUC≥0.9/ECE≤0.05 作为 binary threshold 但仅 3 个数据点。AUC=0.88/ECE=0.04 区间无 empirical support。Limitations 已承认，但 Table 5 'for practitioners' 定位与 evidence 有张力。\"\n  action_items:\n    - round: 14\n      action: \"扩展 detector coverage（至少 1 个 neural detector），或将 threshold 标注为 'observed in our 3 detectors, not general guidance'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size scaling 趋势基于 3 个数据点，power law fitting 不可靠\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=4/8/16 仅 3 点，外推到 B=128 不可靠。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"未再单独提及，可能已部分改善。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。§5.3 现报告 monotonic trend 和 amplification factor（1.0×/2.3×/3.0×），未见 power law fitting 外推。可能已改善。\"\n  action_items:\n    - round: 12\n      action: \"确认是否已删除 power law fitting，保留 monotonic trend 描述。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"建议将 Spearman 改为 ρ_s。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未提及。§6 Discussion 使用 'Spearman ρ_s ≥ 0.86'，表明已部分修正。需验证全文一致性。\"\n  action_items:\n    - round: 12\n      action: \"全文 Spearman ρ → ρ_s\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 13 issues (updated with Round 14) ===\n\n- id: \"R13-W1\"\n  summary: \"B=4 micro-batch 上 dual constraint 统计可靠性不足，主实验在次优设定运行\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE。B=4 MAE=0.114，advantage 最小（1.0×）。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q3 + R1 AGREE。Modern pretraining micro-batch B=32-128。B=16 仍远低于实际设定。论文应讨论 B=64/128 预期行为和 per-batch α_eff 估计稳定性。\"\n  action_items:\n    - round: 14\n      action: \"讨论 B=64/128 时的预期行为（external extrapolation）。可选：补充 B=32 实验。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Grid-best b=0.3 vs adaptive b*≈0.9 偏差：α_eff 负偏差导致过度干预\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"因果链：α_eff 负偏差 → quality floor 过早绑定 → b_τ 推高 → b*≈0.9 远高于 grid-best b=0.3。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q1 间接涉及：当 D&R 总优于 adaptive 时，adaptive 的 use case 不清楚。Grid-best b=0.3 vs adaptive b*≈0.9 的 gap 仍未解释。\"\n  action_items:\n    - round: 13\n      action: \"补充 per-batch b* 分布（median, percentiles）。分析 α_eff 负偏差对 b* 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"1.7B 规模效应递减 43% 且 scaling trend 未正式讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE。Δ=-0.013 at 1.7B + OOD mixed。Practitioner 关注 7B-70B 规模可能完全失效。§5.2 仅一段描述，缺 formal scaling analysis。Table 5 'for practitioners' 无 scale caveat。\"\n  action_items:\n    - round: 14\n      action: \"正式讨论 scaling trend 和 implications。在 Table 5 或 Conclusion 加 scale caveat。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W4\"\n  summary: \"ρ≥0.4 实用门槛偏高，实际适用场景极窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2-W7。方法仅在多条件同时成立下有效。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"两位 reviewer 均确认。ρ≥0.4 + calibrated detector + self-contamination + continued pretraining + 0.6B 的交集极窄。'Decision summary for practitioners' 在如此受限范围下可能给读者不准确信号。\"\n  action_items:\n    - round: 14\n      action: \"在 Table 5 或 Conclusion 明确标注完整的适用范围限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"§6 Discussion 第一段与 §5.1 epoch confound 内容重复\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W1 + R1 AGREE。§6 开头仍重述 'D&R outperforms...0.35--0.42 PPL... >95% multi-epoch...'，与 §5.1 高度重合。8 页限制下应精简。\"\n  action_items:\n    - round: 14\n      action: \"精简 §6 第一段为一句概括 + §5.1 交叉引用。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Cohen's d 被 deterministic data ordering 人为放大，效应量不确定性未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"d=3.83 但 σ=0.006 因 data ordering 固定。如果 data shuffle seed 也随机化 paired SD 大概率升高。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。可能因论文未报告 Cohen's d 而不再适用，需确认。\"\n  action_items:\n    - round: 13\n      action: \"报告 Cohen's d + CI，讨论 deterministic data ordering 对 paired SD 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"PPL 改善与模型质量（下游任务能力）之间的关系未讨论\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"在 continued pretraining 中多大 PPL 改善才对应有意义的 capability 提升？\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。§6 Effect size 段引用 Tay et al. 2023 和 Ye et al. 2025 讨论 PPL-accuracy 非线性关系，部分改善。\"\n  action_items:\n    - round: 13\n      action: \"在 Discussion 中简要讨论 PPL-capability 关系。\"\n      assigned_to: director\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m4\"\n  summary: \"Permuted q-scores ablation 仅 1 seed\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Table 1 确认仅 seed-42 有 Permuted 结果。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未独立提出。Table 1 仍显示 Permuted 仅 seed 42（'17.919, --, --'）。\"\n  action_items:\n    - round: 13\n      action: \"补充 permuted q-scores 多 seed 或标注 single-seed 限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 14 新发现 ===\n\n- id: \"R14-N1\"\n  summary: \"Abstract 中 'ρ ≥ 0.4, reaching conventional significance' 对 ρ=0.6 构成 overclaim（p_BH=0.064）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。§5.2 报告 ρ=0.6 p_BH=0.064 > α=0.05。仅 ρ=0.4 p_BH=0.011 达标。Abstract 'at ρ ≥ 0.4, reaching conventional significance' 暗示两个 level 均显著，构成事实性错误。\"\n  action_items:\n    - round: 14\n      action: \"修改 Abstract：改为 'at ρ=0.4 (p_BH=0.011)' 或注明 ρ=0.6 仅 marginal significance。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M1\"\n  summary: \"Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。Caption: '5-seed means (seeds 42, 123, 456, 789, 234)' 但表格仅 3 列。Seeds 789/234 不可见，可能引发选择性报告疑虑。\"\n  action_items:\n    - round: 14\n      action: \"Caption 注明 'full 5-seed results in Appendix X' 或增加 seed 列。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M2\"\n  summary: \"§5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。ρ=0.6 paired t 在正文和附录之间数值不一致。损害 reproducibility。\"\n  action_items:\n    - round: 14\n      action: \"核实并统一 t 值。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M3\"\n  summary: \"'Three effectiveness conditions' vs 'three findings' 术语全文不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。Abstract/Figure 1/Conclusion 使用 'conditions'，Introduction 使用 'findings'。应统一。\"\n  action_items:\n    - round: 14\n      action: \"全文统一术语（建议用 'findings' 或 'observed requirements'）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M4\"\n  summary: \"Appendix P Table 16 seed 456 缺 OOD 评估\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。数据完整性问题。\"\n  action_items:\n    - round: 14\n      action: \"补充 seed 456 OOD 评估或解释缺失原因。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M5\"\n  summary: \"Sliding-window evaluation 未说明 window size 和 stride\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。Reproducibility 要求所有 evaluation hyperparameters 明确。\"\n  action_items:\n    - round: 14\n      action: \"在 §4 或 Appendix 注明 window size 和 stride。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Temperature scaling T=0.204 需要 labeled data，限制实际部署性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q2 + R1 AGREE。Detector calibration 依赖 10K labeled validation split。Web-scale pretraining 中 ground-truth synthetic labels 不可用。限制 Table 5 decision framework 的 deployability。\"\n  action_items:\n    - round: 14\n      action: \"在 Discussion 讨论 unsupervised calibration alternatives。或在 Limitations 加此限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-25T21:44:26.900076+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 24243}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1486 · 2026-05-25T21:47:20.323190+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 14 审稿报告 — Provenance Weight Training\n\n**论文标题**: When Does Detect-and-Reweight Work for Synthetic Contamination?\n**投稿目标**: EMNLP 2026 (via ARR), Long Paper\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）\n**交叉回应**: 1 轮, 100% 共识（全部 [AGREE], 0 [REBUT]）\n\n---\n\n## Summary\n\n本文通过受控 continued-pretraining 实验（Qwen3-0.6B, 132M FineWeb tokens, 5 seeds）研究 detect-and-reweight 方法在合成数据污染场景下的有效性条件。核心贡献是 epoch-matched mechanism analysis：D&R 方法 >95% 的优势来自 filtered data 的 multi-epoch exposure 而非 per-token 学习质量差异。论文还提出 dual-constrained adaptive exponent b*，无需 per-model grid search 即可改善 held-out perplexity（Δ=-0.023 at ρ=0.4）。实验覆盖 ρ ∈ {0.2, 0.3, 0.4, 0.6}、0.6B/1.7B scale、3 种 detector。\n\n---\n\n## Strengths\n\n**S1. Epoch-matched mechanism analysis 是真正的学术贡献。**\n通过将 D&R 的 raw PPL 优势（Δ=-0.424）与 epoch-matched control（Δ=0.017）对比，清晰分解了 multi-epoch exposure vs per-token quality 的贡献比。这一发现解释了为什么 D&R 在 continued pretraining（多 epoch）下远优于 from-scratch pretraining（通常 <1 epoch）。[R1+R2 AGREE]\n\n**S2. 消融层次设计严谨。**\nAdaptive < Uniform < ESS-only < Random < Permuted 的递进消融有效隔离了 (1) detector signal vs noise, (2) minimum intervention vs unconstrained maximization, (3) provenance signal vs weight non-uniformity 三个维度。Permuted q-scores ablation 特别巧妙——破坏样本级信息但保留权重分布形状，Δ=+0.225 的强降级清晰证明 provenance signal 是 load-bearing。[R1+R2 AGREE]\n\n**S3. 5-seed 实验 + BH 多重比较校正。**\n主实验 5 seeds + Bonferroni-Holm 校正（ρ=0.4: p_BH=0.011），cross-seed variance 极小（σ=0.006）。统计实践规范。[R1+R2 AGREE]\n\n**S4. Calibration vs discrimination 的经验性分离。**\nTF-IDF+LR (AUC=0.94, ECE=0.048) vs GPT-2 (AUC=0.91, ECE=0.131) 对比在 comparable AUC 下隔离了 calibration 效应，揭示 high-AUC but poorly-calibrated detector 反而有害（Δ=+0.098）。[R1+R2 AGREE]\n\n**S5. Scope limitation 声明诚实。**\nIntroduction（\"with extensions to ρ ∈ {0.2, 0.6} and 1.7B parameters (§limitations discusses scope)\"）、Abstract 最后一句（\"These findings apply within our self-contamination setup at 0.6B scale\"）、Limitations 节（3 点覆盖 scope/detector/evaluation）均显式声明限制。[R2 AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**N1. Abstract 中 \"ρ ≥ 0.4, reaching conventional significance\" 对 ρ=0.6 构成 overclaim。** [R2 发现, R1 AGREE; 新发现]\n\nAbstract: \"improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction\"。\n事实核查：§5.2 报告 ρ=0.6 的 p_BH=0.064（> α=0.05），未达传统显著性水平。仅 ρ=0.4 的 p_BH=0.011 达标。\"ρ ≥ 0.4\" 暗示两个 contamination level 均显著——这是事实性错误。\n\n> 建议：修改为 \"at ρ=0.4 (p_BH=0.011)\" 或注明 ρ=0.6 仅 marginal significance (p_BH=0.064)。\n\n**N2. 标题 scope 远超实验覆盖面。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C4]\n\n\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示系统性评估，但实验仅覆盖：\n- Self-contamination（非 cross-model contamination）\n- 0.6B + 1.7B（非 full pretraining scale）\n- Continued pretraining（非 from-scratch——且 §6 自述 epoch confound 在 from-scratch 下不适用）\n- 单一数据源 FineWeb\n- 主要依赖 TF-IDF+LR 1 个有效 detector（GPT-2 和 N-gram 均为 negative results）\n\n此问题自 Round 11 起连续 4 轮被提出。\n\n> 建议：标题加限定词，如 \"...in Controlled Continued Pretraining\" 或 \"...under Self-Contamination at Sub-Billion Scale\"。\n\n**N3. 下游任务零改善但 Abstract 未提及。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C3]\n\nAbstract \"improves over uniform training\" 未限定 metric。读者自然理解为包含下游任务质量。实际上 downstream accuracy 完全相同（0.5414 vs 0.5415, §5.2）。Conclusion 写了 \"without measurable downstream gains at 0.6B scale\"，但 Abstract 省略这一关键信息，构成 Abstract-正文 framing 不一致。\n\n> 建议：Abstract 明确限定 \"improves held-out perplexity\" 并注明无下游改善。\n\n### Should-Fix (Warning)\n\n**W1. \"Three effectiveness conditions\" framing 过度概括。** [R2 发现, R1 AGREE]\n\nAbstract/Figure 1/Conclusion 使用 \"conditions\"，暗示充分必要条件。但 evidence 仅支持在特定受控设定下的 empirical observations：(a) 3 个 detector 不足以确立 AUC/ECE boundary；(b) 仅 self-contamination；(c) conditions 可能 scale-dependent。Introduction 使用 \"three findings\"，自身术语已不一致。\n\n> 建议：统一使用 \"three empirical findings\" 或 \"three observed requirements\"。\n\n**W2. Δ=-0.023 PPL 缺乏 baseline contextualization。** [R2 发现, R1 AGREE; 关联 R11-C3]\n\n论文未在 continued pretraining 文献中定位 0.023 PPL（0.13% relative）的量级含义。缺少：(a) 同等 compute 下 learning rate schedule 的 PPL delta；(b) 其他 data curation 方法（DSIR, DsDm, DoReMi）在类似 scale 的 PPL improvement；(c) 增加 1% training data 的边际改善。没有对照，读者无法判断 0.023 是 meaningful 还是 noise-level。\n\n**W3. Related Work 遗漏 detection benchmarks。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-W3]\n\n缺少：RAID (Dugan et al., 2024) — AI-generated text detection benchmark；M4 (Wang et al., 2024) — 多语言 machine-generated text detection。§2 讨论了 detection 方法（DetectGPT, Binoculars, Min-k Prob）但未引用评估这些方法的标准 benchmark。自 Round 13 起被要求补充，仍缺失。\n\n**W4. Table 5 decision framework 基于 3 个 detector，实用性受限。** [R2 发现, R1 AGREE; 跨轮次 recurring R12-W1]\n\nTable 5 将 AUC ≥ 0.9 和 ECE ≤ 0.05 作为 binary threshold，但仅 3 个 detector 数据点（TF-IDF+LR, GPT-2, N-gram），缺少 neural detectors（RoBERTa/DeBERTa/DetectGPT/Binoculars/RADAR）。AUC=0.88, ECE=0.04 区间无 empirical support。Limitations 已承认此限制，但 Table 5 \"for practitioners\" 定位与有限 evidence 之间存在张力。\n\n**W5. §6 Discussion 第一段与 §5.1 高度重复。** [R2 发现, R1 AGREE; 跨轮次 recurring R13-m1]\n\n§6 开头重述 \"D&R outperforms all reweighting methods by 0.35--0.42 PPL... epoch-matched controls attribute >95%...\"，与 §5.1 高度重合。8 页限制下应精简。\n\n**W6. 缺 uniform × 3.2 epochs baseline，epoch confound 分析不完整。** [R1 发现, R2 AGREE; 跨轮次 recurring R11-W4]\n\n缺关键对照实验：对全部数据（含 synthetic）跑 ~3.2 epochs 的 PPL。无此 baseline 无法区分\"纯重复训练的 benefit\"vs\"选择性重复高质量数据的 benefit\"。计算成本低（~1 次额外训练），对 epoch-matched analysis 的完整性至关重要。\n\n**W7. 1.7B 规模效应递减 43%，scaling trend 未正式讨论。** [R1 发现, R2 AGREE; 跨轮次 recurring R13-W3]\n\n0.6B→1.7B Δ 从 -0.023 缩至 -0.013（43% 递减），OOD 方向不一致。如果 trend 成立，7B-70B scale 方法可能完全失效，削弱 Table 5 \"for practitioners\" 适用性。§5.2 仅一段描述，未正式 scaling analysis 或外推讨论。\n\n**W8. ρ≥0.4 实用门槛偏高，实际适用场景极窄。** [R2 发现, R1 AGREE; 跨轮次 recurring R13-W4]\n\n方法仅在 ρ≥0.4 + well-calibrated detector + self-contamination + continued pretraining + 0.6B 下有效。多条件交集的实际场景极窄，\"decision summary for practitioners\" 可能给读者不准确的 generalizability 信号。\n\n**W9. Temperature scaling T=0.204 依赖 labeled data，限制 deployability。** [R2 发现, R1 AGREE; 新发现]\n\nDetector calibration（§4, Appendix L）依赖 10K labeled validation split。Web-scale pretraining 中 ground-truth synthetic labels 通常不可用。论文未讨论 unsupervised calibration alternatives，限制了 Table 5 decision framework 的实际部署性。\n\n### Minor Issues\n\n**M1. Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列。** [R2 发现, R1 AGREE]\nCaption: \"5-seed means (seeds 42, 123, 456, 789, 234)\" 但表格列仅 Seed 42/123/456 + Mean。Seeds 789/234 个体结果不可见，可能引发选择性报告疑虑。\n\n**M2. §5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）。** [R2 发现, R1 AGREE]\nρ=0.6 的 paired t 在正文和附录间数值不一致。损害 reproducibility 和信任度。\n\n**M3. \"Three effectiveness conditions\" vs \"three findings\" 术语全文不一致。** [R2 发现, R1 AGREE]\nAbstract/Figure 1/Conclusion 使用 \"conditions\"，Introduction 使用 \"findings\"。\n\n**M4. Appendix P Table 16 seed 456 缺 OOD 评估。** [R2 发现, R1 AGREE]\n数据完整性问题。\n\n**M5. Sliding-window evaluation 未说明 window size 和 stride。** [R2 发现, R1 AGREE]\nReproducibility 要求所有 evaluation hyperparameters 明确。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在所有问题上达成完全共识（100% [AGREE], 0% [REBUT]）。交叉验证关系：\n- R2-N3 ≈ R1-N1（effect size vs framing 矛盾）\n- R2-N2 ≈ R1-W4+W5（scope 限制）\n- R2-W4 ≈ R1-W4（detector threshold 通用性）\n- R2-Q3 ≈ R1-M1（batch size 限制）\n\nR2 额外发现 R1 遗漏的：N1（p_BH=0.064 overclaim），W3（missing references），M2（t 值不一致）。\n\n---\n\n## Reviewer Divergence\n\n无。本轮所有问题均 [AGREE]。\n\n---\n\n## Questions\n\n**Q1. Adaptive reweighting 的实际 use case。** [R2 提出, R1 AGREE]\nD&R (q>0.3) PPL 17.250 大幅优于 adaptive (17.674)。如果 D&R 在所有设定下都优于 adaptive reweighting，后者的 use case 是什么？论文隐含论证 adaptive 不需要 grid search，但 D&R 同样只需一个 threshold 而非 grid search。除非存在 D&R 不适用的场景（如 corpus 过小无法承受数据丢弃），论文未讨论此情形。\n\n**Q2. Temperature scaling T=0.204 在无标注数据下的替代方案。** [R2 提出, R1 AGREE]\nDetector calibration 依赖 labeled validation split（10K documents）。Web-scale pretraining 中 ground-truth synthetic labels 不可用。是否存在 unsupervised calibration 方案？\n\n**Q3. B=4 micro-batch size 的代表性。** [R2 提出, R1 AGREE; 跨轮次 recurring R13-W1]\nModern pretraining micro-batch size 通常 B=32-128。§5.3 显示 B=4→16 效果提升（1.0× → 3.0× amplification），但 B=16 仍远低于实际设定。论文应讨论 (a) B=64/128 预期行为；(b) 大 batch 下 per-batch α_eff 估计是否更稳定。\n\n---\n\n## Missing References\n\n1. **RAID** (Dugan et al., 2024) — AI-generated text detection benchmark，与论文 detector evaluation 直接相关\n2. **M4** (Wang et al., 2024) — 多语言 machine-generated text detection shared task\n3. **MATES** (Yu et al., 2024) — 如涉及 training-time data selection\n4. **Aioli** (Balachandran et al., 2024) — 如涉及 data mixing\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求 (not_requested)\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成 (2026-05-25 21:16–21:19, ~2.5 min)\n**统计**: 0 critical, 1 warning, 12 info\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Page 8 | Figure 8 stacked bar chart 5+ 颜色类别，灰度打印下部分相邻色段难以区分。建议增加纹理填充 |\n| ℹ️ info | Page 1 | 首页无 display item，Figure 1 在 page 2 顶部 |\n| ℹ️ info | Page 2 | Figure 1 legend 字号偏小（约正文 55-60%），subplot (a) legend 与数据线轻微视觉拥挤 |\n| ℹ️ info | Page 3 | Figure 2（架构概览图）仅单栏宽度，建议改用 figure*（全宽）|\n| ℹ️ info | Page 7 | Display item 密度最高（Table 3 + Table 4 + Figure 7），略拥挤但内容关联紧密 |\n| ℹ️ info | Page 8 | Table 5 颜色背景行高亮效果好。主文正好 8 页，符合 EMNLP 2026 限制 ✓ |\n| ℹ️ info | Page 9 | Limitations 简洁（3 点），合规 ✓。References 格式统一，无 [?] ✓ |\n| ℹ️ info | Page 12 | Figure 10 axis label 字号偏小（~55%），建议放大 |\n| ℹ️ info | Page 15 | 含 AI Assistants 声明，合规 ✓ |\n\n---\n\n## Overall Assessment\n\n| 维度 | 评分 | 说明 |\n|------|------|------|\n| **Overall** | **3.0 — Findings** | 分析贡献（epoch-matched mechanism）有学术价值，但 framing 系统性超出 evidence，实际效果量级不足以支撑 practitioner 定位 |\n| **Soundness** | **3.5** | 实验设计严谨（5 seeds, BH correction, 层次消融），但 scope 限制（self-contamination, 0.6B, B=4, 3 detectors）+ p-value overclaim 削弱可信度 |\n| **Excitement** | **2.5** | Epoch-matched analysis 有新意，但 Δ=-0.023 PPL (0.13%) 无下游改善，practical impact 有限 |\n| **Confidence** | **4 — High** | 两位 Reviewer 独立得出一致评分，交叉回应 100% 共识 |\n\n**核心判断**: 论文的学术贡献在于 epoch-matched mechanism analysis——解释 D&R 为何在 continued pretraining 中有效（multi-epoch exposure 而非 per-token quality）。这一发现值得发表。但当前存在三层 framing 偏差：\n\n1. **Abstract 事实性错误**：ρ=0.6 p_BH=0.064 未达显著性，Abstract overclaims\n2. **标题-实验 scope gap**：标题暗示通用性，实验仅覆盖极窄场景（self-contamination + continued pretraining + 0.6B + 1 个有效 detector）\n3. **Practitioner framing 与 evidence 矛盾**：Δ=-0.023 PPL 无下游改善、1.7B 递减 43%、ρ<0.4 失效，综合来看 practical impact 有限，但 Table 5 和多处措辞维持 practitioner-oriented 定位\n\n**建议接收路径**: 修正 Abstract overclaim + 标题 scope 限定 + 重新定位为 analysis paper with negative practical result at current scales → Findings 发表。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"three findings\"（line 23）与 Abstract/Conclusion 的 \"three conditions\" 不一致（M3）\n- Scope 声明（line 20）合理，但标题仍未反映限制（N2）\n- \"illustrative application\" 表述改善了方法定位（对比 Round 10 的 §3 ~1.5 页），但 Figure 1 caption 仍用 \"Three effectiveness conditions\"\n\n### §2 Related Work\n- 缺少 RAID 和 M4 detection benchmarks（W3）\n- 现有 coverage 对 data curation 和 theoretical foundations 较为全面\n- Drayson et al. 对比清晰（3 点差异），但应注意 ModernBERT-150M 未在本文测试（与 W4 相关）\n\n### §3 Method\n- 方法新颖性有限（w=(1-q)^b 来自 Drayson, dual constraint + bisection 是标准方法），但论文已改善定位为 \"illustrative application\"\n- \"motivated by convergence theory (Wang 2026)\" 仍暗示理论保证，而 α_eff proxy R²≈0.63 (~37% unexplained variance) 意味理论前提不完全满足。§6 已讨论此限制，但 §3 的措辞应对齐\n\n### §4 Experimental Setup\n- Sliding-window evaluation 缺 window size 和 stride 参数（M5）\n- Temperature scaling T=0.204 依赖 labeled data 未讨论可行性（W9/Q2）\n- Self-contamination 设定在 Introduction 中已有预告，合理\n\n### §5 Results\n- §5.1: 消融严谨，5-seed 统计可靠。但 Table 1 显示 3 seeds 而 caption 说 5-seed mean（M1）——seeds 789/234 个体值不可见\n- §5.1: Permuted q-scores 仅 seed-42 (17.919, --, --)。作为关键 ablation 控制组，单 seed 可靠性有限\n- §5.2 Robustness: ρ=0.6 p_BH=0.064 在正文中正确报告为 \"directionally outperforms\"，但 Abstract overclaims（N1）\n- §5.2 Scale: 1.7B Δ=-0.013 + OOD mixed 仅一段，未正式 scaling analysis（W7）\n- §5.2: t=-9.95 vs Appendix I t=-15.4 数值不一致（M2）\n- §5.3 Batch-size: B=4/8/16 monotonic trend 清晰，amplification 报告改善（对比 Round 12 的 power law fitting 问题）。但 B=16 仍远低于实际设定（Q3）\n\n### §6 Discussion\n- 第一段与 §5.1 高度重复（W5）。建议一句概括 + §5.1 交叉引用\n- \"When uniform beats reweighting\" 段 + Table 5: \"conditions\" 表述仍过强（W1），且 3 detector 支撑不足（W4）\n- \"Effect size and downstream impact\" 段诚实，引用 Tay et al. 和 Ye et al.，但缺 baseline contextualization（W2）\n- \"Limitations of α_eff as a proxy\" 段坦诚且必要，Pearson r≈0.79, Spearman ρ_s≥0.86\n\n### §7 Conclusion\n- \"without measurable downstream gains at 0.6B scale\" 比 Abstract 诚实——但这恰恰暴露 Abstract 的 framing gap（N3）\n- \"three effectiveness conditions\" 仍 over-claims（W1）\n\n### Limitations\n- 三点覆盖 scope/detector/evaluation，简洁合规\n- 与 EMNLP 2026 要求一致\n\n### Appendix\n- Table 16 seed 456 缺 OOD 评估（M4）\n- 整体 appendix 内容丰富\n\n---\n\n**审稿圆桌**: R1 × R2, 1 轮初审 + 1 轮交叉回应, 100% 共识收敛\n**Issue Tracker**: 已同步更新至 review_issues.yaml（Round 14）",
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
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
    "report": "# Round 14 审稿报告 — Provenance Weight Training\n\n**论文标题**: When Does Detect-and-Reweight Work for Synthetic Contamination?\n**投稿目标**: EMNLP 2026 (via ARR), Long Paper\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）\n**交叉回应**: 1 轮, 100% 共识（全部 [AGREE], 0 [REBUT]）\n\n---\n\n## Summary\n\n本文通过受控 continued-pretraining 实验（Qwen3-0.6B, 132M FineWeb tokens, 5 seeds）研究 detect-and-reweight 方法在合成数据污染场景下的有效性条件。核心贡献是 epoch-matched mechanism analysis：D&R 方法 >95% 的优势来自 filtered data 的 multi-epoch exposure 而非 per-token 学习质量差异。论文还提出 dual-constrained adaptive exponent b*，无需 per-model grid search 即可改善 held-out perplexity（Δ=-0.023 at ρ=0.4）。实验覆盖 ρ ∈ {0.2, 0.3, 0.4, 0.6}、0.6B/1.7B scale、3 种 detector。\n\n---\n\n## Strengths\n\n**S1. Epoch-matched mechanism analysis 是真正的学术贡献。**\n通过将 D&R 的 raw PPL 优势（Δ=-0.424）与 epoch-matched control（Δ=0.017）对比，清晰分解了 multi-epoch exposure vs per-token quality 的贡献比。这一发现解释了为什么 D&R 在 continued pretraining（多 epoch）下远优于 from-scratch pretraining（通常 <1 epoch）。[R1+R2 AGREE]\n\n**S2. 消融层次设计严谨。**\nAdaptive < Uniform < ESS-only < Random < Permuted 的递进消融有效隔离了 (1) detector signal vs noise, (2) minimum intervention vs unconstrained maximization, (3) provenance signal vs weight non-uniformity 三个维度。Permuted q-scores ablation 特别巧妙——破坏样本级信息但保留权重分布形状，Δ=+0.225 的强降级清晰证明 provenance signal 是 load-bearing。[R1+R2 AGREE]\n\n**S3. 5-seed 实验 + BH 多重比较校正。**\n主实验 5 seeds + Bonferroni-Holm 校正（ρ=0.4: p_BH=0.011），cross-seed variance 极小（σ=0.006）。统计实践规范。[R1+R2 AGREE]\n\n**S4. Calibration vs discrimination 的经验性分离。**\nTF-IDF+LR (AUC=0.94, ECE=0.048) vs GPT-2 (AUC=0.91, ECE=0.131) 对比在 comparable AUC 下隔离了 calibration 效应，揭示 high-AUC but poorly-calibrated detector 反而有害（Δ=+0.098）。[R1+R2 AGREE]\n\n**S5. Scope limitation 声明诚实。**\nIntroduction（\"with extensions to ρ ∈ {0.2, 0.6} and 1.7B parameters (§limitations discusses scope)\"）、Abstract 最后一句（\"These findings apply within our self-contamination setup at 0.6B scale\"）、Limitations 节（3 点覆盖 scope/detector/evaluation）均显式声明限制。[R2 AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**N1. Abstract 中 \"ρ ≥ 0.4, reaching conventional significance\" 对 ρ=0.6 构成 overclaim。** [R2 发现, R1 AGREE; 新发现]\n\nAbstract: \"improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction\"。\n事实核查：§5.2 报告 ρ=0.6 的 p_BH=0.064（> α=0.05），未达传统显著性水平。仅 ρ=0.4 的 p_BH=0.011 达标。\"ρ ≥ 0.4\" 暗示两个 contamination level 均显著——这是事实性错误。\n\n> 建议：修改为 \"at ρ=0.4 (p_BH=0.011)\" 或注明 ρ=0.6 仅 marginal significance (p_BH=0.064)。\n\n**N2. 标题 scope 远超实验覆盖面。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C4]\n\n\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示系统性评估，但实验仅覆盖：\n- Self-contamination（非 cross-model contamination）\n- 0.6B + 1.7B（非 full pretraining scale）\n- Continued pretraining（非 from-scratch——且 §6 自述 epoch confound 在 from-scratch 下不适用）\n- 单一数据源 FineWeb\n- 主要依赖 TF-IDF+LR 1 个有效 detector（GPT-2 和 N-gram 均为 negative results）\n\n此问题自 Round 11 起连续 4 轮被提出。\n\n> 建议：标题加限定词，如 \"...in Controlled Continued Pretraining\" 或 \"...under Self-Contamination at Sub-Billion Scale\"。\n\n**N3. 下游任务零改善但 Abstract 未提及。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C3]\n\nAbstract \"improves over uniform training\" 未限定 metric。读者自然理解为包含下游任务质量。实际上 downstream accuracy 完全相同（0.5414 vs 0.5415, §5.2）。Conclusion 写了 \"without measurable downstream gains at 0.6B scale\"，但 Abstract 省略这一关键信息，构成 Abstract-正文 framing 不一致。\n\n> 建议：Abstract 明确限定 \"improves held-out perplexity\" 并注明无下游改善。\n\n### Should-Fix (Warning)\n\n**W1. \"Three effectiveness conditions\" framing 过度概括。** [R2 发现, R1 AGREE]\n\nAbstract/Figure 1/Conclusion 使用 \"conditions\"，暗示充分必要条件。但 evidence 仅支持在特定受控设定下的 empirical observations：(a) 3 个 detector 不足以确立 AUC/ECE boundary；(b) 仅 self-contamination；(c) conditions 可能 scale-dependent。Introduction 使用 \"three findings\"，自身术语已不一致。\n\n> 建议：统一使用 \"three empirical findings\" 或 \"three observed requirements\"。\n\n**W2. Δ=-0.023 PPL 缺乏 baseline contextualization。** [R2 发现, R1 AGREE; 关联 R11-C3]\n\n论文未在 continued pretraining 文献中定位 0.023 PPL（0.13% relative）的量级含义。缺少：(a) 同等 compute 下 learning rate schedule 的 PPL delta；(b) 其他 data curation 方法（DSIR, DsDm, DoReMi）在类似 scale 的 PPL improvement；(c) 增加 1% training data 的边际改善。没有对照，读者无法判断 0.023 是 meaningful 还是 noise-level。\n\n**W3. Related Work 遗漏 detection benchmarks。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-W3]\n\n缺少：RAID (Dugan et al., 2024) — AI-generated text detection benchmark；M4 (Wang et al., 2024) — 多语言 machine-generated text detection。§2 讨论了 detection 方法（DetectGPT, Binoculars, Min-k Prob）但未引用评估这些方法的标准 benchmark。自 Round 13 起被要求补充，仍缺失。\n\n**W4. Table 5 decision framework 基于 3 个 detector，实用性受限。** [R2 发现, R1 AGREE; 跨轮次 recurring R12-W1]\n\nTable 5 将 AUC ≥ 0.9 和 ECE ≤ 0.05 作为 binary threshold，但仅 3 个 detector 数据点（TF-IDF+LR, GPT-2, N-gram），缺少 neural detectors（RoBERTa/DeBERTa/DetectGPT/Binoculars/RADAR）。AUC=0.88, ECE=0.04 区间无 empirical support。Limitations 已承认此限制，但 Table 5 \"for practitioners\" 定位与有限 evidence 之间存在张力。\n\n**W5. §6 Discussion 第一段与 §5.1 高度重复。** [R2 发现, R1 AGREE; 跨轮次 recurring R13-m1]\n\n§6 开头重述 \"D&R outperforms all reweighting methods by 0.35--0.42 PPL... epoch-matched controls attribute >95%...\"，与 §5.1 高度重合。8 页限制下应精简。\n\n**W6. 缺 uniform × 3.2 epochs baseline，epoch confound 分析不完整。** [R1 发现, R2 AGREE; 跨轮次 recurring R11-W4]\n\n缺关键对照实验：对全部数据（含 synthetic）跑 ~3.2 epochs 的 PPL。无此 baseline 无法区分\"纯重复训练的 benefit\"vs\"选择性重复高质量数据的 benefit\"。计算成本低（~1 次额外训练），对 epoch-matched analysis 的完整性至关重要。\n\n**W7. 1.7B 规模效应递减 43%，scaling trend 未正式讨论。** [R1 发现, R2 AGREE; 跨轮次 recurring R13-W3]\n\n0.6B→1.7B Δ 从 -0.023 缩至 -0.013（43% 递减），OOD 方向不一致。如果 trend 成立，7B-70B scale 方法可能完全失效，削弱 Table 5 \"for practitioners\" 适用性。§5.2 仅一段描述，未正式 scaling analysis 或外推讨论。\n\n**W8. ρ≥0.4 实用门槛偏高，实际适用场景极窄。** [R2 发现, R1 AGREE; 跨轮次 recurring R13-W4]\n\n方法仅在 ρ≥0.4 + well-calibrated detector + self-contamination + continued pretraining + 0.6B 下有效。多条件交集的实际场景极窄，\"decision summary for practitioners\" 可能给读者不准确的 generalizability 信号。\n\n**W9. Temperature scaling T=0.204 依赖 labeled data，限制 deployability。** [R2 发现, R1 AGREE; 新发现]\n\nDetector calibration（§4, Appendix L）依赖 10K labeled validation split。Web-scale pretraining 中 ground-truth synthetic labels 通常不可用。论文未讨论 unsupervised calibration alternatives，限制了 Table 5 decision framework 的实际部署性。\n\n### Minor Issues\n\n**M1. Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列。** [R2 发现, R1 AGREE]\nCaption: \"5-seed means (seeds 42, 123, 456, 789, 234)\" 但表格列仅 Seed 42/123/456 + Mean。Seeds 789/234 个体结果不可见，可能引发选择性报告疑虑。\n\n**M2. §5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）。** [R2 发现, R1 AGREE]\nρ=0.6 的 paired t 在正文和附录间数值不一致。损害 reproducibility 和信任度。\n\n**M3. \"Three effectiveness conditions\" vs \"three findings\" 术语全文不一致。** [R2 发现, R1 AGREE]\nAbstract/Figure 1/Conclusion 使用 \"conditions\"，Introduction 使用 \"findings\"。\n\n**M4. Appendix P Table 16 seed 456 缺 OOD 评估。** [R2 发现, R1 AGREE]\n数据完整性问题。\n\n**M5. Sliding-window evaluation 未说明 window size 和 stride。** [R2 发现, R1 AGREE]\nReproducibility 要求所有 evaluation hyperparameters 明确。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在所有问题上达成完全共识（100% [AGREE], 0% [REBUT]）。交叉验证关系：\n- R2-N3 ≈ R1-N1（effect size vs framing 矛盾）\n- R2-N2 ≈ R1-W4+W5（scope 限制）\n- R2-W4 ≈ R1-W4（detector threshold 通用性）\n- R2-Q3 ≈ R1-M1（batch size 限制）\n\nR2 额外发现 R1 遗漏的：N1（p_BH=0.064 overclaim），W3（missing references），M2（t 值不一致）。\n\n---\n\n## Reviewer Divergence\n\n无。本轮所有问题均 [AGREE]。\n\n---\n\n## Questions\n\n**Q1. Adaptive reweighting 的实际 use case。** [R2 提出, R1 AGREE]\nD&R (q>0.3) PPL 17.250 大幅优于 adaptive (17.674)。如果 D&R 在所有设定下都优于 adaptive reweighting，后者的 use case 是什么？论文隐含论证 adaptive 不需要 grid search，但 D&R 同样只需一个 threshold 而非 grid search。除非存在 D&R 不适用的场景（如 corpus 过小无法承受数据丢弃），论文未讨论此情形。\n\n**Q2. Temperature scaling T=0.204 在无标注数据下的替代方案。** [R2 提出, R1 AGREE]\nDetector calibration 依赖 labeled validation split（10K documents）。Web-scale pretraining 中 ground-truth synthetic labels 不可用。是否存在 unsupervised calibration 方案？\n\n**Q3. B=4 micro-batch size 的代表性。** [R2 提出, R1 AGREE; 跨轮次 recurring R13-W1]\nModern pretraining micro-batch size 通常 B=32-128。§5.3 显示 B=4→16 效果提升（1.0× → 3.0× amplification），但 B=16 仍远低于实际设定。论文应讨论 (a) B=64/128 预期行为；(b) 大 batch 下 per-batch α_eff 估计是否更稳定。\n\n---\n\n## Missing References\n\n1. **RAID** (Dugan et al., 2024) — AI-generated text detection benchmark，与论文 detector evaluation 直接相关\n2. **M4** (Wang et al., 2024) — 多语言 machine-generated text detection shared task\n3. **MATES** (Yu et al., 2024) — 如涉及 training-time data selection\n4. **Aioli** (Balachandran et al., 2024) — 如涉及 data mixing\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求 (not_requested)\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成 (2026-05-25 21:16–21:19, ~2.5 min)\n**统计**: 0 critical, 1 warning, 12 info\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Page 8 | Figure 8 stacked bar chart 5+ 颜色类别，灰度打印下部分相邻色段难以区分。建议增加纹理填充 |\n| ℹ️ info | Page 1 | 首页无 display item，Figure 1 在 page 2 顶部 |\n| ℹ️ info | Page 2 | Figure 1 legend 字号偏小（约正文 55-60%），subplot (a) legend 与数据线轻微视觉拥挤 |\n| ℹ️ info | Page 3 | Figure 2（架构概览图）仅单栏宽度，建议改用 figure*（全宽）|\n| ℹ️ info | Page 7 | Display item 密度最高（Table 3 + Table 4 + Figure 7），略拥挤但内容关联紧密 |\n| ℹ️ info | Page 8 | Table 5 颜色背景行高亮效果好。主文正好 8 页，符合 EMNLP 2026 限制 ✓ |\n| ℹ️ info | Page 9 | Limitations 简洁（3 点），合规 ✓。References 格式统一，无 [?] ✓ |\n| ℹ️ info | Page 12 | Figure 10 axis label 字号偏小（~55%），建议放大 |\n| ℹ️ info | Page 15 | 含 AI Assistants 声明，合规 ✓ |\n\n---\n\n## Overall Assessment\n\n| 维度 | 评分 | 说明 |\n|------|------|------|\n| **Overall** | **3.0 — Findings** | 分析贡献（epoch-matched mechanism）有学术价值，但 framing 系统性超出 evidence，实际效果量级不足以支撑 practitioner 定位 |\n| **Soundness** | **3.5** | 实验设计严谨（5 seeds, BH correction, 层次消融），但 scope 限制（self-contamination, 0.6B, B=4, 3 detectors）+ p-value overclaim 削弱可信度 |\n| **Excitement** | **2.5** | Epoch-matched analysis 有新意，但 Δ=-0.023 PPL (0.13%) 无下游改善，practical impact 有限 |\n| **Confidence** | **4 — High** | 两位 Reviewer 独立得出一致评分，交叉回应 100% 共识 |\n\n**核心判断**: 论文的学术贡献在于 epoch-matched mechanism analysis——解释 D&R 为何在 continued pretraining 中有效（multi-epoch exposure 而非 per-token quality）。这一发现值得发表。但当前存在三层 framing 偏差：\n\n1. **Abstract 事实性错误**：ρ=0.6 p_BH=0.064 未达显著性，Abstract overclaims\n2. **标题-实验 scope gap**：标题暗示通用性，实验仅覆盖极窄场景（self-contamination + continued pretraining + 0.6B + 1 个有效 detector）\n3. **Practitioner framing 与 evidence 矛盾**：Δ=-0.023 PPL 无下游改善、1.7B 递减 43%、ρ<0.4 失效，综合来看 practical impact 有限，但 Table 5 和多处措辞维持 practitioner-oriented 定位\n\n**建议接收路径**: 修正 Abstract overclaim + 标题 scope 限定 + 重新定位为 analysis paper with negative practical result at current scales → Findings 发表。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"three findings\"（line 23）与 Abstract/Conclusion 的 \"three conditions\" 不一致（M3）\n- Scope 声明（line 20）合理，但标题仍未反映限制（N2）\n- \"illustrative application\" 表述改善了方法定位（对比 Round 10 的 §3 ~1.5 页），但 Figure 1 caption 仍用 \"Three effectiveness conditions\"\n\n### §2 Related Work\n- 缺少 RAID 和 M4 detection benchmarks（W3）\n- 现有 coverage 对 data curation 和 theoretical foundations 较为全面\n- Drayson et al. 对比清晰（3 点差异），但应注意 ModernBERT-150M 未在本文测试（与 W4 相关）\n\n### §3 Method\n- 方法新颖性有限（w=(1-q)^b 来自 Drayson, dual constraint + bisection 是标准方法），但论文已改善定位为 \"illustrative application\"\n- \"motivated by convergence theory (Wang 2026)\" 仍暗示理论保证，而 α_eff proxy R²≈0.63 (~37% unexplained variance) 意味理论前提不完全满足。§6 已讨论此限制，但 §3 的措辞应对齐\n\n### §4 Experimental Setup\n- Sliding-window evaluation 缺 window size 和 stride 参数（M5）\n- Temperature scaling T=0.204 依赖 labeled data 未讨论可行性（W9/Q2）\n- Self-contamination 设定在 Introduction 中已有预告，合理\n\n### §5 Results\n- §5.1: 消融严谨，5-seed 统计可靠。但 Table 1 显示 3 seeds 而 caption 说 5-seed mean（M1）——seeds 789/234 个体值不可见\n- §5.1: Permuted q-scores 仅 seed-42 (17.919, --, --)。作为关键 ablation 控制组，单 seed 可靠性有限\n- §5.2 Robustness: ρ=0.6 p_BH=0.064 在正文中正确报告为 \"directionally outperforms\"，但 Abstract overclaims（N1）\n- §5.2 Scale: 1.7B Δ=-0.013 + OOD mixed 仅一段，未正式 scaling analysis（W7）\n- §5.2: t=-9.95 vs Appendix I t=-15.4 数值不一致（M2）\n- §5.3 Batch-size: B=4/8/16 monotonic trend 清晰，amplification 报告改善（对比 Round 12 的 power law fitting 问题）。但 B=16 仍远低于实际设定（Q3）\n\n### §6 Discussion\n- 第一段与 §5.1 高度重复（W5）。建议一句概括 + §5.1 交叉引用\n- \"When uniform beats reweighting\" 段 + Table 5: \"conditions\" 表述仍过强（W1），且 3 detector 支撑不足（W4）\n- \"Effect size and downstream impact\" 段诚实，引用 Tay et al. 和 Ye et al.，但缺 baseline contextualization（W2）\n- \"Limitations of α_eff as a proxy\" 段坦诚且必要，Pearson r≈0.79, Spearman ρ_s≥0.86\n\n### §7 Conclusion\n- \"without measurable downstream gains at 0.6B scale\" 比 Abstract 诚实——但这恰恰暴露 Abstract 的 framing gap（N3）\n- \"three effectiveness conditions\" 仍 over-claims（W1）\n\n### Limitations\n- 三点覆盖 scope/detector/evaluation，简洁合规\n- 与 EMNLP 2026 要求一致\n\n### Appendix\n- Table 16 seed 456 缺 OOD 评估（M4）\n- 整体 appendix 内容丰富\n\n---\n\n**审稿圆桌**: R1 × R2, 1 轮初审 + 1 轮交叉回应, 100% 共识收敛\n**Issue Tracker**: 已同步更新至 review_issues.yaml（Round 14）",
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1487 · 2026-05-25T21:47:24.137999+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3814
}
```

</details>

---


### Assistant

_source line 1488 · 2026-05-25T21:47:39.239322+00:00_

**Round 14 审稿报告已投递。**

两位 Reviewer 100% 共识收敛（全部 [AGREE]），评分一致：

| 维度 | 评分 |
|------|------|
| Overall | **3.0 — Findings** |
| Soundness | 3.5 |
| Excitement | 2.5 |
| Confidence | 4 (High) |

**3 个 Must-Fix**:
1. Abstract "ρ ≥ 0.4, reaching conventional significance" overclaim — ρ=0.6 p_BH=0.064 未达显著性
2. 标题 scope 远超实验覆盖面（self-contamination + 0.6B + continued pretraining only）— 跨 4 轮未修
3. 下游零改善未在 Abstract 提及

**9 个 Should-Fix**, **5 个 Minor**, **3 个 Questions**。

核心判断：epoch-matched mechanism analysis 是真正的学术贡献，值得 Findings 发表。但 framing 存在系统性偏差——标题/Abstract/Table 5 的 practitioner 定位与 Δ=-0.023 PPL 无下游改善、1.7B 递减 43%、ρ<0.4 失效的 evidence 矛盾。

Issue Tracker 已同步更新（24 个 issue，含 7 个 Round 14 新发现）。报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 114

## Round 114

6 recorded events


### User

_source line 1489 · 2026-05-25T21:47:40.488661+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

所有 R2 的 Must-Fix（N1-N3）、Should-Fix（W1-W5）、小问题（M1-M5）和 Questions（Q1-Q3）均标记为 **[AGREE]**。关键发现：

- R2-N1（ρ≥0.4 的 p_BH=0.064 overclaim）是我遗漏的事实性错误，具有独立价值
- 两位 Reviewer 在 Overall 3.0、Soundness 3.5、Excitement 2.5 上完全一致
- 核心共识：epoch-matched mechanism analysis 有贡献，但 framing 超出 evidence 范围，实际效果不足以支撑 practitioner-oriented 定位

---

[Reviewer 2 审稿意见]:
# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

**[AGREE] R1-N1: Effect size 与 practitioner framing 之间的根本矛盾**

同意。这与我的 N3（Abstract 未提及无下游提升）和 W5（效应量论证不足）一致。Δ=-0.023 PPL（0.13% relative）在 §6 被承认为 "modest"，但 Table 5 标题仍为 "Decision summary for practitioners"，且 Abstract 中 "improves over uniform training" 未限定为 PPL-only。论文内部存在定位矛盾：一方面诚实承认影响有限（§6 "does not transfer to downstream accuracy"），另一方面仍以 practitioner guidance 包装结论。

补充发现：§7 Conclusion 最后一句提到 "whether these conditions hold at full pretraining scale (>100B tokens)...is the central open question"，但如果 0.6B→1.7B 效应已减半（§5.2, Δ=-0.013），且 1.7B OOD 方向不一致（OWT Δ=-0.008, Wiki Δ=+0.013），那么 full-scale 的前景进一步存疑。R1 建议重新定位为 mechanism analysis 是合理的——论文最有价值的贡献（D&R epoch-matching decomposition、calibration 发现）本质上是分析性的，不需要 practitioner framing 来体现价值。

**[AGREE] R1-N2: Cohen's d = 3.83 被 deterministic data ordering 系统性放大**

同意，这是一个重要的方法论问题。Appendix Q 明确承认 "seeds affect only parameter initialization, not data order (the dataloader is deterministic), so the primary stochastic axis is initialization noise at 0.6B scale"。这意味着 SD_Δ=0.006 仅反映初始化噪声的极小方差，而非方法在不同数据采样条件下的稳健性。

Cohen's d=3.83 和 power>0.99 的呈现方式在 §5.1 中给读者留下了"效果极其稳健"的印象，但实际上只是说"在固定数据顺序下，不同初始化产生的结果非常一致"——这是一个远弱于"方法在不同条件下稳健有效"的声明。论文在 Appendix Q 的透明度值得肯定（"the low dispersion is a property of the experimental setting rather than a method artifact"），但这个关键 caveat 应出现在 §5.1 主文而非仅在 appendix 中。

补充：uniform baseline 也有类似的低方差（σ=0.008），说明窄方差确实是实验设定的属性。但这恰恰意味着 paired t-test 的高显著性并不能推广到更广泛的 data conditions。

---

## Should-Fix 问题

**[AGREE] R1-W1: 缺少 uniform × multi-epoch baseline**

同意。论文的 epoch-matched D&R controls（Table 3）回答了"D&R 在等 epoch 条件下是否优于 adaptive"（answer: gap 仅 0.017），但未回答 R1 提出的更基本问题：**在包含合成数据的全部语料上做 3.2 epochs 的 uniform 训练，PPL 会如何？** 这个 baseline 可以区分两个假说：(a) D&R 的优势来自 filtering quality（去除坏数据）vs (b) 单纯来自 repetition（多看数据本身就有帮助，即使包含合成数据）。如果 uniform × 3.2 epochs 也大幅改善 PPL，那 D&R 的 "filtering" 叙事需要修正。

这个 baseline 的计算成本很低（一次训练），应该被包含。

**[AGREE] R1-W2: α_eff proxy 的 37% 未解释方差——但建议更具体**

同意 R1 的核心关切。§6 "Limitations of α_eff as a proxy" 段定性地承认了 "some batches satisfying α_eff ≥ τ may have true fractions below τ"，但未给出具体的 violation 频率。Appendix J Table 12 报告了 Pearson r≈0.79（连续 formulation）和 consistent negative bias ≈-0.03，但 violation rate（α_eff ≥ 0.7 且 true real fraction < 0.7 的 batch 比例）是一个可以直接从现有数据计算的量，缺失是一个遗漏。

不过我要补充一点 nuance：negative bias（α_eff 低估 true fraction）意味着方法偏向 conservative intervention（多干预而非少干预），这在 safety 角度是可取的——但也解释了 W3 中 b*≈0.9 系统高于 grid-optimal b=0.3 的问题。两个 weakness 是 mechanistically linked。

**[REBUT] R1-W3: Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差——部分反驳**

R1 的观察（b*≈0.9 > grid-optimal b=0.3）是准确的，但 "违背 minimum intervention 原则" 的结论需要 nuance：

1. **比较框架不对等**：Grid-optimal b=0.3 是对所有 batch 施加固定 b 的全局最优值（Table 8, Appendix C），而 adaptive b* 是逐 batch 计算的。Mean b*≈0.9 ≠ "每个 batch 都用 0.9"。Figure 10（Appendix B, b* trajectory）显示 b* 在 0 到 ~5 之间大幅波动，包括 5.8% 的 clean batches（b*=0）。Per-batch 的 b* 分布均值为 0.9，但这不能简单类比为固定 b=0.9（fixed b=1.0 的 PPL=17.692 ≈ uniform，见 §5.1）。

2. **PPL gap 的归因**：0.054 的 gap（adaptive 17.674 vs grid 17.620）部分来自 α_eff 的 negative bias 导致的 over-intervention，但也部分来自 grid-search 的 post-hoc oracle advantage（grid-best 是从 9 个候选中选出的最优值，具有 overfitting 风险；其 cross-seed SD=0.035 是 adaptive 的 ~6×，见 §5.1）。

3. **但 R1 的核心 concern 成立**：α_eff 的 systematic negative bias（-0.03, Table 12）确实会系统性地推高 b*，这是 adaptive 方法的一个结构性缺陷。论文未讨论 bias correction 的可能性（如用 calibrated offset 调整 α_eff），这是一个改进方向。

综合判断：R1 的观察有价值，但 "违背 minimum intervention 原则" 的表述过强。更准确的说法是 "α_eff 的 systematic underestimation 导致 adaptive 方法未能完全实现 minimum intervention，有改进空间"。

**[AGREE] R1-W4: 3 个 detector 不足以支撑 AUC/ECE threshold 通用性**

完全同意，这与我的 W4 一致。3 个 detectors（AUC 分别为 0.73/0.91/0.94）的采样密度不足以确定 AUC≥0.9 的阈值——AUC=0.85 或 0.88 的 detector 表现如何完全未知。ECE 方面同理：0.048 和 0.131 之间的巨大空白使得 ECE≤0.05 的 threshold 更像是一个 coincidental observation 而非 validated boundary。

**[AGREE] R1-W5: Scale 效应递减 43%，practitioner 适用性存疑**

同意。0.6B→1.7B 效应减半（Δ: -0.023 → -0.013），且 1.7B 的 OOD 结果方向不一致（§5.2: OWT -0.008, Wiki +0.013）。论文的解释（"larger models being more robust to self-generated contamination"）合理但也暗示了方法的结构性局限：如果效果依赖于 generator-trainee distribution mismatch，而 self-contamination 中 mismatch 随模型增大而缩小，那么方法在最常见的 self-contamination 场景下可能 inherently limited。

---

## 小问题

**[AGREE] R1-M1: B=4 主实验低估方法潜力**

同意。§5.3 的 batch-size amplification（B=4→16, Δ 从 -0.023 到 -0.068）暗示 B=4 不是方法的最佳展示。但论文选择 B=4 作为主实验有合理理由（"reflecting memory constraints typical of continued pretraining setups"），且 B=8/16 结果已在 §5.3 补充。这是 framing issue 而非 experimental flaw。

**[AGREE] R1-M2: Paired t-test 正态性假设 n=5 下无法验证**

同意，但这是 small-sample 研究的通用局限。论文提供了 directional consistency（所有 5 个 seed 都改善）作为补充证据，部分弥补了参数检验假设无法验证的问题。建议补充 non-parametric test（如 Wilcoxon signed-rank）作为 robustness check。

**[REBUT] R1-M3: Abstract word count 接近 200-word 限制**

不同意这是一个问题。我实际计数约 171 words，距离 200-word 限制还有约 29 words 的余量（~15%）。"接近限制" 不构成 weakness。

---

## Questions 回应

**Q1: 是否有不同 data permutation 下的实验？**
论文中没有。这与 N2 直接相关——如果增加 data ordering randomization 作为额外 stochastic axis，当前的高 Cohen's d 很可能显著下降。这是一个合理的 revision requirement。

**Q2: Uniform × multi-epoch baseline 的预期结果？**
同意 R1 的预期——这个 baseline 对区分 repetition vs filtering 至关重要。如果 uniform × 3.2 epochs 也大幅改善（例如达到 17.3-17.5 range），那 D&R 的 filtering 叙事需要大幅弱化；如果 uniform × 3.2 epochs 反而因为合成数据的 multi-epoch 放大而 degradation，则强化 filtering 的价值。两种结果都有信息量。

**Q3: α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例？**
同意这应该被报告。从现有数据（Appendix J, Table 12: MAE=0.114, bias=-0.03 at B=4）可以粗略推断 violation rate 不会太高（因为 negative bias 意味着 α_eff 倾向于低估，所以 α_eff ≥ τ 的 batch 通常 true fraction 也 ≥ τ），但精确数字应从数据中直接计算。

**Q4: Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？**
这是一个有建设性的建议。如果用 empirical bias correction（加回 +0.03 offset）调整 α_eff，b_τ 会降低（更少干预），可能使 mean b* 从 0.9 下降到更接近 grid-optimal 的 0.3-0.5 range。论文未探索这个方向，是一个合理的 revision suggestion。

**Q5: 1.7B 实验选择 τ=0.8 而非 0.7 的理由？**
论文在 §5.2 报告 1.7B 使用 τ=0.8 但未解释选择理由。考虑到 0.6B 的主结果推荐 τ=0.7（§5.3 Table 6 明确显示 τ=0.7 在 holdout 和 OOD 上均优于 τ=0.8），1.7B 却用 τ=0.8 缺乏 justification。如果 1.7B 用 τ=0.7 结果可能不同，这是一个 confound——无法确定 1.7B 效应减弱是因为 scale 还是因为 suboptimal τ。这是一个值得指出的实验设计问题。

---

## 综合评估

R1 的审稿意见在方法论层面质量很高，多数 concerns 与我的独立评估一致。两份审稿的核心共识：

1. **论文最大价值在分析贡献**（D&R epoch-matching、calibration finding），而非 adaptive method 本身
2. **Effect size 过小且无下游影响**，practitioner framing 不恰当
3. **实验 scope 过窄**，不足以支撑标题和 "conditions" 的一般性 claim
4. **统计显著性的呈现方式**需要更多 caveats

我维持 **Overall 3.0 (Findings)** 的评分。论文在其 scope 内 soundness 达标，但需要：(a) 重新定位为 mechanism analysis；(b) 修正 abstract 中的统计 overclaim；(c) 补充 uniform × multi-epoch baseline。

---

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。核心结论：

- R1 的 10 条意见中，**8 条 AGREE**（N1, N2, W1, W2, W4, W5, M1, M2），**1 条 partial REBUT**（W3: adaptive b* vs grid-optimal 的比较框架不对等），**1 条 full REBUT**（M3: abstract word count 实际约 171 words，距限制有余量）
- 两份审稿的核心共识：论文应重新定位为 mechanism analysis，修正统计 overclaim，补充 uniform × multi-epoch baseline
- 维持 Overall 3.0 (Findings) 评分

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

_source line 1490 · 2026-05-25T21:52:19.129517+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11+ recurring issues (updated with Round 14 fresh review) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。双方 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"论文已升至 5 seeds + BH correction。统计检验力问题部分缓解但 Cohen's d=3.83 被 deterministic data ordering 人为放大。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"N=5 seeds 和 BH correction 已到位。原始 N=3 问题已解决。衍生出 R14-N1（ρ=0.6 p_BH=0.064 overclaim）。R2 交叉回应补充：Cohen's d caveat 应在 §5.1 主文而非仅 Appendix Q；建议补充 Wilcoxon signed-rank 作为 robustness check。\"\n  resolution: \"主实验升至 5 seeds + BH correction。原始统计检验力问题已解决。\"\n  resolution_round: 14\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.63，Wang (2026) 理论保证不直接转移到 proxy\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 标为 critical。圆桌共识：should-fix（修改 'guarantees' 措辞即可）。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2 补充：negative bias ≈-0.03 意味 α_eff 偏向 conservative intervention（多干预），在 safety 角度可取但解释了 b*≈0.9 系统偏高的问题。应报告 violation rate（α_eff ≥ τ 且 true fraction < τ 的 batch 比例），可从现有数据直接计算。\"\n  action_items:\n    - round: 14\n      action: \"将 §3 中 'guarantees' 改为 'targets/approximates'。报告 violation rate。考虑 bias correction（+0.03 offset）对 b* 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.023 PPL, 0.13% relative），practitioner framing 自相矛盾\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=128 幂律外推被一致认为不可靠。'practical' 表述仍残留。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2+W5 独立提出。核心矛盾仍在。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N3 + R1-N1 再次确认。R2 交叉回应补充：论文内部存在定位矛盾——§6 诚实承认影响有限('does not transfer to downstream accuracy')但 Table 5 仍以 'for practitioners' 包装。R2 建议：论文最有价值的贡献（D&R epoch-matching、calibration）本质是分析性的，不需要 practitioner framing 来体现价值。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 限定 'improves held-out PPL' + 注明无下游改善。重新定位为 mechanism analysis paper。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"标题通用性远超实验 scope：仅 self-contamination + continued pretraining + 0.6B\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Cross-model transfer single seed + mixed + 无 PPL 比较。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 must-fix。建议标题加限定如 '...in Continued Pretraining'。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N2 + R1 AGREE。跨 4 轮持续存在。标题未改。\"\n  action_items:\n    - round: 14\n      action: \"修改标题增加限定词。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§3 压缩后仍给人独立方法贡献印象。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"圆桌共识：中偏低，不影响评分。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W2 指出 'three effectiveness conditions' framing 仍过度概括。Introduction 已改用 'illustrative application' 和 'three findings'（改善），但 Abstract/Conclusion/Figure 1 仍用 'conditions'（不一致）。\"\n  action_items:\n    - round: 14\n      action: \"统一使用 'three empirical findings' 或 'three observed requirements'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作和 detection benchmarks\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议。\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 新增：RAID benchmark (Dugan et al. 2024)、M4 shared task (Wang et al. 2024)。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"RAID 和 M4 仍缺失。\"\n  action_items:\n    - round: 14\n      action: \"补充 RAID 和 M4。考虑 MATES 和 Aioli。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏 uniform+multi-epoch baseline\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Epoch confound 适用范围需限定为 multi-epoch exposure 场景。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2：缺 uniform × 3.2 epochs baseline。R2 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍缺失。R2 交叉回应进一步论证：此 baseline 可区分两个假说——(a) filtering quality vs (b) 单纯 repetition。如果 uniform × 3.2 epochs 也大幅改善 PPL，D&R 的 'filtering' 叙事需修正。计算成本低（~1 次训练）。\"\n  action_items:\n    - round: 14\n      action: \"增加 uniform+multi-epoch baseline（全数据 ~3.2 epochs）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 可读性和 display item 分布问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"ρ 符号冲突、Figure 1 黑白不可辨。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"视觉审查发现 page 6 密度过高。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 reviewers 未独立提出。视觉审查发现 Figure 8 灰度问题（warning）。\"\n  action_items:\n    - round: 14\n      action: \"Figure 8 增加纹理填充。放大 axis label 字号。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 issues (updated with Round 14) ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"LaTeX wc 确认 225 words。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 ~155 words，合规。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2 在交叉回应中 REBUT R1 的 'abstract 接近限制' concern：实际约 171 words，距 200 限制有 ~15% 余量。合规。\"\n  resolution: \"Abstract 已压缩至合规范围。\"\n  resolution_round: 13\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§7 Conclusion 溢出至第 9 页。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 §1-§7 在 page 8 内。合规。\"\n  resolution: \"正文已压缩至 8 页内。\"\n  resolution_round: 13\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个），不足以支撑 AUC/ECE threshold 的通用性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"仅 TF-IDF+LR / GPT-2 / N-gram。3 个数据点不足建立因果关系。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"缺少 neural detectors。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2-W4 再次确认。AUC=0.88/ECE=0.04 区间无 empirical support。\"\n  action_items:\n    - round: 14\n      action: \"扩展 detector coverage 或标注 threshold 为 observational。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size scaling 趋势基于 3 个数据点，power law fitting 不可靠\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=4/8/16 仅 3 点，外推到 B=128 不可靠。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"未再单独提及。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。§5.3 现报告 monotonic trend 和 amplification factor，未见 power law 外推。可能已改善。\"\n  action_items:\n    - round: 12\n      action: \"确认是否已删除 power law fitting。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"建议将 Spearman 改为 ρ_s。\"\n    - round: 14\n      reviewers: []\n      note: \"§6 使用 'Spearman ρ_s ≥ 0.86'，部分修正。需验证全文一致性。\"\n  action_items:\n    - round: 12\n      action: \"全文 Spearman ρ → ρ_s\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 13 issues (updated with Round 14) ===\n\n- id: \"R13-W1\"\n  summary: \"B=4 micro-batch 上 dual constraint 统计可靠性不足，主实验在次优设定运行\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"B=4 MAE=0.114，advantage 最小（1.0×）。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q3 + R1 AGREE。R2 交叉回应补充：B=4 选择有合理理由（memory constraints），且 B=8/16 结果已在 §5.3 补充，是 framing issue 而非 experimental flaw。但仍应讨论 B=64/128 预期行为。\"\n  action_items:\n    - round: 14\n      action: \"讨论 B=64/128 预期行为。可选：补 B=32 实验。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Grid-best b=0.3 vs adaptive b*≈0.9 偏差：α_eff 负偏差导致过度干预\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"因果链：α_eff 负偏差 → quality floor 过早绑定 → b_τ 推高 → b*≈0.9 远高于 grid-best b=0.3。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 AGREE，R2 partial REBUT。R2 论证：(1) 比较框架不对等——grid b=0.3 是全局固定值而 mean b*≈0.9 含 per-batch 波动（0~5 range, 5.8% clean batches b*=0）；(2) gap 部分来自 grid-search 的 post-hoc oracle advantage（cross-seed SD=0.035 是 adaptive 6×）；(3) 但核心 concern 成立——α_eff negative bias -0.03 确实系统推高 b*，是结构性缺陷。圆桌共识：观察有效，但'违背 minimum intervention'措辞过强，更准确为'未能完全实现 minimum intervention，有改进空间'。\"\n  action_items:\n    - round: 14\n      action: \"补充 per-batch b* 分布。探索 bias correction（+0.03 offset）对 b* 和 PPL 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"1.7B 规模效应递减 43% 且 scaling trend 未正式讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE。R2 交叉回应补充：论文解释('larger models more robust to self-generated contamination')合理但暗示方法的结构性局限——效果依赖 generator-trainee mismatch，而 self-contamination 中 mismatch 随模型增大缩小，方法 inherently limited。§7 最后一句'whether these conditions hold at full scale...is the central open question'——但 0.6B→1.7B 已减半，full-scale 前景更存疑。\"\n  action_items:\n    - round: 14\n      action: \"正式讨论 scaling trend。在 Table 5/Conclusion 加 scale caveat。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W4\"\n  summary: \"ρ≥0.4 实用门槛偏高，实际适用场景极窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"方法仅在多条件同时成立下有效。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"两位 reviewer 均确认。\"\n  action_items:\n    - round: 14\n      action: \"在 Table 5 或 Conclusion 明确标注适用范围限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"§6 Discussion 第一段与 §5.1 epoch confound 内容重复\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍存在。建议精简。\"\n  action_items:\n    - round: 14\n      action: \"精简 §6 第一段为概括 + §5.1 交叉引用。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Cohen's d 被 deterministic data ordering 人为放大，效应量不确定性未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"d=3.83 但 σ=0.006 因 data ordering 固定。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2 AGREE。R2 补充：Appendix Q 透明度好（承认'low dispersion is a property of the experimental setting'），但 caveat 应在 §5.1 主文而非仅 appendix。Uniform baseline 也有类似低方差（σ=0.008），确认窄方差是实验设定属性。Paired t-test 高显著性不能推广到更广 data conditions。\"\n  action_items:\n    - round: 14\n      action: \"将 Appendix Q 的 Cohen's d caveat 移至/复制到 §5.1 主文。补充 Wilcoxon signed-rank test。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"PPL 改善与模型质量（下游任务能力）之间的关系未讨论\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"在 continued pretraining 中多大 PPL 改善才对应有意义的 capability 提升？\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未独立提出。§6 引用 Tay et al. 和 Ye et al. 讨论 PPL-accuracy 非线性关系，部分改善。\"\n  action_items:\n    - round: 13\n      action: \"在 Discussion 简要讨论 PPL-capability 关系。\"\n      assigned_to: director\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m4\"\n  summary: \"Permuted q-scores ablation 仅 1 seed\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Table 1 确认仅 seed-42。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未独立提出。Table 1 仍显示 Permuted 仅 seed 42。\"\n  action_items:\n    - round: 13\n      action: \"补充 permuted 多 seed 或标注限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 14 新发现 ===\n\n- id: \"R14-N1\"\n  summary: \"Abstract 中 'ρ ≥ 0.4, reaching conventional significance' 对 ρ=0.6 构成 overclaim（p_BH=0.064）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。§5.2 ρ=0.6 p_BH=0.064 > α=0.05。仅 ρ=0.4 p_BH=0.011 达标。\"\n  action_items:\n    - round: 14\n      action: \"修改 Abstract：改为 'at ρ=0.4' 或注明 ρ=0.6 仅 marginal。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Temperature scaling T=0.204 需要 labeled data，限制实际部署性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q2 + R1 AGREE。Detector calibration 依赖 10K labeled validation split。\"\n  action_items:\n    - round: 14\n      action: \"在 Discussion 讨论 unsupervised calibration alternatives 或在 Limitations 加此限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W2\"\n  summary: \"1.7B 实验选择 τ=0.8 而非推荐的 τ=0.7，构成 confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2 在交叉回应中新发现（Q5）。§5.2 报告 1.7B 使用 τ=0.8 但未解释理由。0.6B 主结果推荐 τ=0.7（§5.3 明确显示 τ=0.7 在 holdout 和 OOD 上均优）。1.7B 用 τ=0.8 导致无法区分效应减弱是因为 scale 还是因为 suboptimal τ。\"\n  action_items:\n    - round: 14\n      action: \"解释 1.7B 选择 τ=0.8 的理由，或补充 1.7B + τ=0.7 实验。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M1\"\n  summary: \"Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Seeds 789/234 不可见，可能引发选择性报告疑虑。\"\n  action_items:\n    - round: 14\n      action: \"Caption 注明 full results in Appendix 或增加 seed 列。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M2\"\n  summary: \"§5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。损害 reproducibility。\"\n  action_items:\n    - round: 14\n      action: \"核实并统一 t 值。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M3\"\n  summary: \"'Three effectiveness conditions' vs 'three findings' 术语全文不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Abstract/Figure 1/Conclusion 使用 'conditions'，Introduction 使用 'findings'。\"\n  action_items:\n    - round: 14\n      action: \"全文统一术语。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M4\"\n  summary: \"Appendix P Table 16 seed 456 缺 OOD 评估\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"数据完整性问题。\"\n  action_items:\n    - round: 14\n      action: \"补充或解释缺失原因。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M5\"\n  summary: \"Sliding-window evaluation 未说明 window size 和 stride\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Reproducibility 要求。\"\n  action_items:\n    - round: 14\n      action: \"在 §4 或 Appendix 注明。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
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
    "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11+ recurring issues (updated with Round 14 fresh review) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 12 fresh review 再次独立发现。双方 AGREE。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"论文已升至 5 seeds + BH correction。统计检验力问题部分缓解但 Cohen's d=3.83 被 deterministic data ordering 人为放大。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"N=5 seeds 和 BH correction 已到位。原始 N=3 问题已解决。衍生出 R14-N1（ρ=0.6 p_BH=0.064 overclaim）。R2 交叉回应补充：Cohen's d caveat 应在 §5.1 主文而非仅 Appendix Q；建议补充 Wilcoxon signed-rank 作为 robustness check。\"\n  resolution: \"主实验升至 5 seeds + BH correction。原始统计检验力问题已解决。\"\n  resolution_round: 14\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.63，Wang (2026) 理论保证不直接转移到 proxy\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"r(α_eff, mean_q)=0.80 被识别为 proxy-to-proxy 循环论证。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 标为 critical。圆桌共识：should-fix（修改 'guarantees' 措辞即可）。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2 补充：negative bias ≈-0.03 意味 α_eff 偏向 conservative intervention（多干预），在 safety 角度可取但解释了 b*≈0.9 系统偏高的问题。应报告 violation rate（α_eff ≥ τ 且 true fraction < τ 的 batch 比例），可从现有数据直接计算。\"\n  action_items:\n    - round: 14\n      action: \"将 §3 中 'guarantees' 改为 'targets/approximates'。报告 violation rate。考虑 bias correction（+0.03 offset）对 b* 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.023 PPL, 0.13% relative），practitioner framing 自相矛盾\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4 全部 |Δ| ≤ 0.01。Abstract 'yielding a practical adaptive method' 构成 overclaim。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=128 幂律外推被一致认为不可靠。'practical' 表述仍残留。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W2+W5 独立提出。核心矛盾仍在。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N3 + R1-N1 再次确认。R2 交叉回应补充：论文内部存在定位矛盾——§6 诚实承认影响有限('does not transfer to downstream accuracy')但 Table 5 仍以 'for practitioners' 包装。R2 建议：论文最有价值的贡献（D&R epoch-matching、calibration）本质是分析性的，不需要 practitioner framing 来体现价值。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 限定 'improves held-out PPL' + 注明无下游改善。重新定位为 mechanism analysis paper。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"标题通用性远超实验 scope：仅 self-contamination + continued pretraining + 0.6B\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Cross-model transfer single seed + mixed + 无 PPL 比较。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 must-fix。建议标题加限定如 '...in Continued Pretraining'。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N2 + R1 AGREE。跨 4 轮持续存在。标题未改。\"\n  action_items:\n    - round: 14\n      action: \"修改标题增加限定词。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§3 压缩后仍给人独立方法贡献印象。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"圆桌共识：中偏低，不影响评分。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W2 指出 'three effectiveness conditions' framing 仍过度概括。Introduction 已改用 'illustrative application' 和 'three findings'（改善），但 Abstract/Conclusion/Figure 1 仍用 'conditions'（不一致）。\"\n  action_items:\n    - round: 14\n      action: \"统一使用 'three empirical findings' 或 'three observed requirements'。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作和 detection benchmarks\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失 4 篇参考文献。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Round 11 缺失的 4 篇已补充。Round 12 新增建议。\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 新增：RAID benchmark (Dugan et al. 2024)、M4 shared task (Wang et al. 2024)。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"RAID 和 M4 仍缺失。\"\n  action_items:\n    - round: 14\n      action: \"补充 RAID 和 M4。考虑 MATES 和 Aioli。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏 uniform+multi-epoch baseline\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"需讨论 prior work 是否控制了 epoch。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"Epoch confound 适用范围需限定为 multi-epoch exposure 场景。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2：缺 uniform × 3.2 epochs baseline。R2 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍缺失。R2 交叉回应进一步论证：此 baseline 可区分两个假说——(a) filtering quality vs (b) 单纯 repetition。如果 uniform × 3.2 epochs 也大幅改善 PPL，D&R 的 'filtering' 叙事需修正。计算成本低（~1 次训练）。\"\n  action_items:\n    - round: 14\n      action: \"增加 uniform+multi-epoch baseline（全数据 ~3.2 epochs）。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 可读性和 display item 分布问题\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"ρ 符号冲突、Figure 1 黑白不可辨。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"视觉审查发现 page 6 密度过高。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 reviewers 未独立提出。视觉审查发现 Figure 8 灰度问题（warning）。\"\n  action_items:\n    - round: 14\n      action: \"Figure 8 增加纹理填充。放大 axis label 字号。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 12 issues (updated with Round 14) ===\n\n- id: \"R12-C1\"\n  summary: \"Abstract 超过 200 words 限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"LaTeX wc 确认 225 words。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 ~155 words，合规。\"\n    - round: 14\n      reviewers: [2]\n      note: \"R2 在交叉回应中 REBUT R1 的 'abstract 接近限制' concern：实际约 171 words，距 200 限制有 ~15% 余量。合规。\"\n  resolution: \"Abstract 已压缩至合规范围。\"\n  resolution_round: 13\n\n- id: \"R12-C2\"\n  summary: \"正文超出 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"§7 Conclusion 溢出至第 9 页。\"\n    - round: 13\n      reviewers: [2]\n      note: \"Round 13 确认 §1-§7 在 page 8 内。合规。\"\n  resolution: \"正文已压缩至 8 页内。\"\n  resolution_round: 13\n\n- id: \"R12-W1\"\n  summary: \"Detector 测试范围不足（仅 3 个），不足以支撑 AUC/ECE threshold 的通用性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"仅 TF-IDF+LR / GPT-2 / N-gram。3 个数据点不足建立因果关系。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"缺少 neural detectors。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2-W4 再次确认。AUC=0.88/ECE=0.04 区间无 empirical support。\"\n  action_items:\n    - round: 14\n      action: \"扩展 detector coverage 或标注 threshold 为 observational。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"Batch-size scaling 趋势基于 3 个数据点，power law fitting 不可靠\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"B=4/8/16 仅 3 点，外推到 B=128 不可靠。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"未再单独提及。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未作为独立问题提出。§5.3 现报告 monotonic trend 和 amplification factor，未见 power law 外推。可能已改善。\"\n  action_items:\n    - round: 12\n      action: \"确认是否已删除 power law fitting。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-m1\"\n  summary: \"ρ 符号冲突：同时表示 contamination ratio 和 Spearman 相关系数\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"建议将 Spearman 改为 ρ_s。\"\n    - round: 14\n      reviewers: []\n      note: \"§6 使用 'Spearman ρ_s ≥ 0.86'，部分修正。需验证全文一致性。\"\n  action_items:\n    - round: 12\n      action: \"全文 Spearman ρ → ρ_s\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 13 issues (updated with Round 14) ===\n\n- id: \"R13-W1\"\n  summary: \"B=4 micro-batch 上 dual constraint 统计可靠性不足，主实验在次优设定运行\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"B=4 MAE=0.114，advantage 最小（1.0×）。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q3 + R1 AGREE。R2 交叉回应补充：B=4 选择有合理理由（memory constraints），且 B=8/16 结果已在 §5.3 补充，是 framing issue 而非 experimental flaw。但仍应讨论 B=64/128 预期行为。\"\n  action_items:\n    - round: 14\n      action: \"讨论 B=64/128 预期行为。可选：补 B=32 实验。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Grid-best b=0.3 vs adaptive b*≈0.9 偏差：α_eff 负偏差导致过度干预\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"因果链：α_eff 负偏差 → quality floor 过早绑定 → b_τ 推高 → b*≈0.9 远高于 grid-best b=0.3。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 AGREE，R2 partial REBUT。R2 论证：(1) 比较框架不对等——grid b=0.3 是全局固定值而 mean b*≈0.9 含 per-batch 波动（0~5 range, 5.8% clean batches b*=0）；(2) gap 部分来自 grid-search 的 post-hoc oracle advantage（cross-seed SD=0.035 是 adaptive 6×）；(3) 但核心 concern 成立——α_eff negative bias -0.03 确实系统推高 b*，是结构性缺陷。圆桌共识：观察有效，但'违背 minimum intervention'措辞过强，更准确为'未能完全实现 minimum intervention，有改进空间'。\"\n  action_items:\n    - round: 14\n      action: \"补充 per-batch b* 分布。探索 bias correction（+0.03 offset）对 b* 和 PPL 的影响。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"1.7B 规模效应递减 43% 且 scaling trend 未正式讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"0.6B→1.7B Δ 从 −0.023 缩至 −0.013（43% 递减），OOD 方向不一致。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE。R2 交叉回应补充：论文解释('larger models more robust to self-generated contamination')合理但暗示方法的结构性局限——效果依赖 generator-trainee mismatch，而 self-contamination 中 mismatch 随模型增大缩小，方法 inherently limited。§7 最后一句'whether these conditions hold at full scale...is the central open question'——但 0.6B→1.7B 已减半，full-scale 前景更存疑。\"\n  action_items:\n    - round: 14\n      action: \"正式讨论 scaling trend。在 Table 5/Conclusion 加 scale caveat。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W4\"\n  summary: \"ρ≥0.4 实用门槛偏高，实际适用场景极窄\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"方法仅在多条件同时成立下有效。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"两位 reviewer 均确认。\"\n  action_items:\n    - round: 14\n      action: \"在 Table 5 或 Conclusion 明确标注适用范围限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"§6 Discussion 第一段与 §5.1 epoch confound 内容重复\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"仍存在。建议精简。\"\n  action_items:\n    - round: 14\n      action: \"精简 §6 第一段为概括 + §5.1 交叉引用。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Cohen's d 被 deterministic data ordering 人为放大，效应量不确定性未讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"d=3.83 但 σ=0.006 因 data ordering 固定。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2 AGREE。R2 补充：Appendix Q 透明度好（承认'low dispersion is a property of the experimental setting'），但 caveat 应在 §5.1 主文而非仅 appendix。Uniform baseline 也有类似低方差（σ=0.008），确认窄方差是实验设定属性。Paired t-test 高显著性不能推广到更广 data conditions。\"\n  action_items:\n    - round: 14\n      action: \"将 Appendix Q 的 Cohen's d caveat 移至/复制到 §5.1 主文。补充 Wilcoxon signed-rank test。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"PPL 改善与模型质量（下游任务能力）之间的关系未讨论\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"在 continued pretraining 中多大 PPL 改善才对应有意义的 capability 提升？\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未独立提出。§6 引用 Tay et al. 和 Ye et al. 讨论 PPL-accuracy 非线性关系，部分改善。\"\n  action_items:\n    - round: 13\n      action: \"在 Discussion 简要讨论 PPL-capability 关系。\"\n      assigned_to: director\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m4\"\n  summary: \"Permuted q-scores ablation 仅 1 seed\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Table 1 确认仅 seed-42。\"\n    - round: 14\n      reviewers: []\n      note: \"Round 14 未独立提出。Table 1 仍显示 Permuted 仅 seed 42。\"\n  action_items:\n    - round: 13\n      action: \"补充 permuted 多 seed 或标注限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 14 新发现 ===\n\n- id: \"R14-N1\"\n  summary: \"Abstract 中 'ρ ≥ 0.4, reaching conventional significance' 对 ρ=0.6 构成 overclaim（p_BH=0.064）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。§5.2 ρ=0.6 p_BH=0.064 > α=0.05。仅 ρ=0.4 p_BH=0.011 达标。\"\n  action_items:\n    - round: 14\n      action: \"修改 Abstract：改为 'at ρ=0.4' 或注明 ρ=0.6 仅 marginal。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Temperature scaling T=0.204 需要 labeled data，限制实际部署性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-Q2 + R1 AGREE。Detector calibration 依赖 10K labeled validation split。\"\n  action_items:\n    - round: 14\n      action: \"在 Discussion 讨论 unsupervised calibration alternatives 或在 Limitations 加此限制。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-W2\"\n  summary: \"1.7B 实验选择 τ=0.8 而非推荐的 τ=0.7，构成 confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2 在交叉回应中新发现（Q5）。§5.2 报告 1.7B 使用 τ=0.8 但未解释理由。0.6B 主结果推荐 τ=0.7（§5.3 明确显示 τ=0.7 在 holdout 和 OOD 上均优）。1.7B 用 τ=0.8 导致无法区分效应减弱是因为 scale 还是因为 suboptimal τ。\"\n  action_items:\n    - round: 14\n      action: \"解释 1.7B 选择 τ=0.8 的理由，或补充 1.7B + τ=0.7 实验。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M1\"\n  summary: \"Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Seeds 789/234 不可见，可能引发选择性报告疑虑。\"\n  action_items:\n    - round: 14\n      action: \"Caption 注明 full results in Appendix 或增加 seed 列。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M2\"\n  summary: \"§5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现，R1 AGREE。损害 reproducibility。\"\n  action_items:\n    - round: 14\n      action: \"核实并统一 t 值。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M3\"\n  summary: \"'Three effectiveness conditions' vs 'three findings' 术语全文不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Abstract/Figure 1/Conclusion 使用 'conditions'，Introduction 使用 'findings'。\"\n  action_items:\n    - round: 14\n      action: \"全文统一术语。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M4\"\n  summary: \"Appendix P Table 16 seed 456 缺 OOD 评估\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"数据完整性问题。\"\n  action_items:\n    - round: 14\n      action: \"补充或解释缺失原因。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M5\"\n  summary: \"Sliding-window evaluation 未说明 window size 和 stride\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Reproducibility 要求。\"\n  action_items:\n    - round: 14\n      action: \"在 §4 或 Appendix 注明。\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1491 · 2026-05-25T21:52:19.282169+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 23732}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-25T21:55:23.447517+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 14 审稿报告 — Provenance Weight Training (FINAL)\n\n**论文标题**: When Does Detect-and-Reweight Work for Synthetic Contamination?\n**投稿目标**: EMNLP 2026 (via ARR), Long Paper\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）\n**交叉回应**: 1 轮。R1→R2: 全部 AGREE。R2→R1: 8 AGREE, 1 partial REBUT (W3), 1 full REBUT (M3)。\n\n---\n\n## Summary\n\n本文通过受控 continued-pretraining 实验（Qwen3-0.6B, 132M FineWeb tokens, 5 seeds）研究 detect-and-reweight 方法在合成数据污染场景下的有效性条件。核心贡献是 epoch-matched mechanism analysis：D&R 方法 >95% 的优势来自 filtered data 的 multi-epoch exposure 而非 per-token 学习质量差异。论文还提出 dual-constrained adaptive exponent b*，无需 per-model grid search 即可改善 held-out perplexity（Δ=-0.023 at ρ=0.4）。实验覆盖 ρ ∈ {0.2, 0.3, 0.4, 0.6}、0.6B/1.7B scale、3 种 detector。\n\n---\n\n## Strengths\n\n**S1. Epoch-matched mechanism analysis 是真正的学术贡献。**\n通过将 D&R 的 raw PPL 优势（Δ=-0.424）与 epoch-matched control（Δ=0.017）对比，清晰分解了 multi-epoch exposure vs per-token quality 的贡献比。这一发现解释了为什么 D&R 在 continued pretraining（多 epoch）下远优于 from-scratch pretraining（通常 <1 epoch）。[R1+R2 AGREE]\n\n**S2. 消融层次设计严谨。**\nAdaptive < Uniform < ESS-only < Random < Permuted 的递进消融有效隔离了 (1) detector signal vs noise, (2) minimum intervention vs unconstrained maximization, (3) provenance signal vs weight non-uniformity 三个维度。Permuted q-scores ablation 特别巧妙——破坏样本级信息但保留权重分布形状，Δ=+0.225 的强降级清晰证明 provenance signal 是 load-bearing。[R1+R2 AGREE]\n\n**S3. 5-seed 实验 + BH 多重比较校正。**\n主实验 5 seeds + Bonferroni-Holm 校正（ρ=0.4: p_BH=0.011），cross-seed variance 极小（σ=0.006）。统计实践规范。[R1+R2 AGREE]\n\n**S4. Calibration vs discrimination 的经验性分离。**\nTF-IDF+LR (AUC=0.94, ECE=0.048) vs GPT-2 (AUC=0.91, ECE=0.131) 对比在 comparable AUC 下隔离了 calibration 效应，揭示 high-AUC but poorly-calibrated detector 反而有害（Δ=+0.098）。[R1+R2 AGREE]\n\n**S5. Scope limitation 声明诚实。**\nIntroduction、Abstract 最后一句、Limitations 节均显式声明限制。Appendix Q 对 deterministic data ordering 对方差的影响也做了透明披露。[R1+R2 AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**N1. Abstract 中 \"ρ ≥ 0.4, reaching conventional significance\" 对 ρ=0.6 构成 overclaim。** [R2 发现, R1 AGREE; 新发现]\n\nAbstract: \"improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction\"。\n事实核查：§5.2 报告 ρ=0.6 的 p_BH=0.064（> α=0.05），未达传统显著性。仅 ρ=0.4 的 p_BH=0.011 达标。\"ρ ≥ 0.4\" 暗示两个 contamination level 均显著——这是事实性错误。\n\n> 建议：修改为 \"at ρ=0.4 (p_BH=0.011)\" 或注明 ρ=0.6 仅 marginal significance (p_BH=0.064)。\n\n**N2. 标题 scope 远超实验覆盖面。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C4，连续 4 轮]\n\n\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示系统性评估，但实验仅覆盖：self-contamination only、0.6B+1.7B、continued pretraining（§6 自述 epoch confound 在 from-scratch 下不适用）、单一数据源 FineWeb、1 个有效 detector。\n\n> 建议：标题加限定词，如 \"...in Controlled Continued Pretraining\"。\n\n**N3. 下游任务零改善但 Abstract 未提及。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C3]\n\nAbstract \"improves over uniform training\" 未限定 metric。Downstream accuracy 完全相同（0.5414 vs 0.5415）。Conclusion 写了 \"without measurable downstream gains\" 但 Abstract 省略。R2 在交叉回应中进一步指出：论文内部存在定位矛盾——§6 诚实承认影响有限，但 Table 5 仍以 \"for practitioners\" 包装。论文最有价值的贡献（D&R epoch-matching、calibration finding）本质是分析性的，不需要 practitioner framing 来体现价值。\n\n> 建议：Abstract 明确限定 \"improves held-out perplexity\"，注明无下游改善。重新定位为 mechanism analysis。\n\n**N4. Cohen's d=3.83 被 deterministic data ordering 系统性放大，关键 caveat 仅在 Appendix。** [R1 发现, R2 AGREE]\n\nAppendix Q 承认 \"seeds affect only parameter initialization, not data order\"，SD_Δ=0.006 仅反映初始化噪声。Cohen's d=3.83 和 power>0.99 给读者留下 \"效果极其稳健\" 的印象，实际上只说明 \"固定数据顺序下不同初始化产生一致结果\"——远弱于 \"方法在不同条件下稳健有效\"。Uniform baseline 也有类似低方差（σ=0.008），确认窄方差是实验设定属性而非方法特性。此 caveat 应在 §5.1 主文而非仅 appendix 中。\n\n> 建议：在 §5.1 加入 Cohen's d 的 deterministic ordering caveat。补充 Wilcoxon signed-rank test 作为 robustness check。\n\n### Should-Fix (Warning)\n\n**W1. \"Three effectiveness conditions\" framing 过度概括。** [R2 发现, R1 AGREE]\n\nAbstract/Figure 1/Conclusion 使用 \"conditions\" 暗示充分必要条件，但 evidence 仅支持 empirical observations。Introduction 使用 \"three findings\"，术语自身不一致。\n\n> 建议：统一使用 \"three empirical findings\" 或 \"three observed requirements\"。\n\n**W2. Δ=-0.023 PPL 缺乏 baseline contextualization。** [R2 发现, R1 AGREE]\n\n论文未在 continued pretraining 文献中定位 0.023 PPL（0.13% relative）的量级含义。缺少与其他 data curation 方法（DSIR, DsDm, DoReMi）的量级对比。\n\n**W3. Related Work 遗漏 detection benchmarks。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-W3]\n\n缺 RAID (Dugan et al., 2024)、M4 (Wang et al., 2024)。自 Round 13 起被要求补充，仍缺失。\n\n**W4. Table 5 decision framework 基于 3 个 detector，实用性受限。** [R1+R2 AGREE; 跨轮次 recurring R12-W1]\n\nAUC ≥ 0.9 / ECE ≤ 0.05 threshold 仅 3 个数据点，缺少 neural detectors。AUC=0.88, ECE=0.04 区间无 empirical support。\n\n**W5. §6 Discussion 第一段与 §5.1 高度重复。** [R2 发现, R1 AGREE; recurring R13-m1]\n\n§6 开头重述 epoch-matched analysis 全部内容，8 页限制下应精简。\n\n**W6. 缺 uniform × 3.2 epochs baseline，epoch confound 分析不完整。** [R1 发现, R2 AGREE; 跨轮次 recurring R11-W4]\n\nR2 在交叉回应中进一步论证：此 baseline 可区分两个假说——(a) D&R 优势来自 filtering quality（去除坏数据）vs (b) 单纯来自 repetition（多看数据本身有帮助即使含 synthetic）。如果 uniform × 3.2 epochs 也大幅改善 PPL，D&R 的 \"filtering\" 叙事需修正。计算成本低。\n\n**W7. 1.7B 规模效应递减 43%，scaling trend 未正式讨论。** [R1 发现, R2 AGREE; recurring R13-W3]\n\nR2 补充：论文解释（\"larger models more robust to self-generated contamination\"）合理但暗示结构性局限——效果依赖 generator-trainee mismatch，而 self-contamination 中 mismatch 随模型增大缩小，方法 inherently limited。\n\n**W8. ρ≥0.4 实用门槛偏高，实际适用场景极窄。** [R2 发现, R1 AGREE; recurring R13-W4]\n\n多条件交集极窄。\"Decision summary for practitioners\" 可能给读者不准确的 generalizability 信号。\n\n**W9. Temperature scaling T=0.204 依赖 labeled data，限制 deployability。** [R2 发现, R1 AGREE]\n\nDetector calibration 依赖 10K labeled validation split。Web-scale pretraining 中 ground-truth synthetic labels 不可用。\n\n**W10. 1.7B 实验选择 τ=0.8 而非推荐的 τ=0.7，构成 confound。** [R2 交叉回应新发现]\n\n§5.2 报告 1.7B 使用 τ=0.8 但未解释选择理由。0.6B 主结果推荐 τ=0.7（§5.3 Table 6 明确显示 τ=0.7 在 holdout 和 OOD 上均优于 τ=0.8）。1.7B 用 τ=0.8 导致无法区分效应减弱是因为 scale 还是因为 suboptimal τ——这是一个实验设计 confound。\n\n> 建议：解释 τ=0.8 选择理由，或补充 1.7B + τ=0.7 实验。\n\n### Minor Issues\n\n**M1. Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列。** [R2 发现, R1 AGREE]\nSeeds 789/234 个体结果不可见，可能引发选择性报告疑虑。\n\n**M2. §5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）。** [R2 发现, R1 AGREE]\n\n**M3. \"Three effectiveness conditions\" vs \"three findings\" 术语全文不一致。** [R2 发现, R1 AGREE]\n\n**M4. Appendix P Table 16 seed 456 缺 OOD 评估。** [R2 发现, R1 AGREE]\n\n**M5. Sliding-window evaluation 未说明 window size 和 stride。** [R2 发现, R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在核心判断上完全一致：\n\n1. **论文应定位为 mechanism analysis paper**，而非 practitioner-oriented method paper\n2. **Abstract overclaim** 必须修正（p-value + downstream null）\n3. **标题需限定 scope**（连续 4 轮 recurring）\n4. **Epoch-matched analysis 是论文的核心价值**\n5. **Overall 3.0 (Findings)**, Soundness 3.5, Excitement 2.5——两人独立得出完全相同评分\n\n交叉验证关系：\n- R2-N3 ≈ R1-N1（effect size vs framing 矛盾）\n- R2-N2 ≈ R1-W4+W5（scope 限制）\n- R2-W4 ≈ R1-W4（detector threshold 通用性）\n- R2-Q3 ≈ R1-M1（batch size 限制）\n\nR2 额外贡献：N1（p_BH=0.064 overclaim，R1 遗漏）、W3（missing references）、M2（t 值不一致）、W10/Q5（1.7B τ=0.8 confound）。\n\n---\n\n## Reviewer Divergence\n\n两处分歧，均为 minor：\n\n**1. R1-W3: Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差** — R2 partial REBUT\n\n- R1 原始主张：\"违背 minimum intervention 原则\"\n- R2 反驳要点：(a) 比较框架不对等——grid b=0.3 是全局固定值而 mean b*≈0.9 含 per-batch 波动（0~5 range, Figure 10, 5.8% clean batches b*=0）；(b) gap 部分来自 grid-search 的 post-hoc oracle advantage（cross-seed SD=0.035 = adaptive 的 6×）；(c) 但核心 concern 成立——α_eff negative bias ≈-0.03 确实系统推高 b*，是结构性缺陷\n- **圆桌裁定**：观察有效，措辞调整。采纳 R2 更精确的表述：**\"α_eff 的 systematic underestimation 导致 adaptive 方法未能完全实现 minimum intervention，有改进空间（如 bias correction）\"**。不影响评分。\n\n**2. R1-M3: Abstract word count 接近 200-word 限制** — R2 full REBUT\n\n- R1 原始主张：abstract 接近 200-word 限制\n- R2 反驳：实际约 171 words，距限制有 ~15% 余量（~29 words），不构成 weakness\n- **圆桌裁定**：采纳 R2 的事实更正。Abstract word count 合规，不列入报告 weaknesses。\n\n---\n\n## Questions\n\n**Q1. Adaptive reweighting 的实际 use case。** [R2 提出, R1 AGREE]\nD&R (q>0.3) PPL 17.250 大幅优于 adaptive (17.674)。如果 D&R 在所有设定下都优于 adaptive，后者的 use case 是什么？\n\n**Q2. Temperature scaling T=0.204 在无标注数据下的替代方案。** [R2 提出, R1 AGREE]\n\n**Q3. B=4 micro-batch size 的代表性。** [R2 提出, R1 AGREE; recurring R13-W1]\nModern pretraining B=32-128。§5.3 B=4→16 amplification 3.0× 但 B=16 仍远低于实际。\n\n**Q4. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例。** [R1 提出, R2 AGREE]\n可从现有数据（Appendix J, Table 12: MAE=0.114, bias=-0.03）直接计算。\n\n**Q5. 1.7B 实验选择 τ=0.8 而非 τ=0.7 的理由。** [R2 交叉回应新发现]\n0.6B 推荐 τ=0.7（holdout+OOD 均优），1.7B 却用 τ=0.8，创造 confound。\n\n**Q6. Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？** [R1 提出, R2 AGREE]\n用 +0.03 offset 调整 α_eff → b_τ 降低 → mean b* 可能从 0.9 降至更接近 grid-optimal 的 0.3-0.5 range。建设性改进方向。\n\n---\n\n## Missing References\n\n1. **RAID** (Dugan et al., 2024) — AI-generated text detection benchmark\n2. **M4** (Wang et al., 2024) — 多语言 machine-generated text detection\n3. **MATES** (Yu et al., 2024) — training-time data selection（如相关）\n4. **Aioli** (Balachandran et al., 2024) — data mixing（如相关）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求 (not_requested)\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成 (2026-05-25 21:16–21:19, ~2.5 min)\n**统计**: 0 critical, 1 warning, 12 info\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Page 8 | Figure 8 stacked bar chart 5+ 颜色类别，灰度打印下相邻色段难以区分。建议增加纹理填充 |\n| ℹ️ info | Page 1 | 首页无 display item，Figure 1 在 page 2 顶部 |\n| ℹ️ info | Page 2 | Figure 1 legend 字号偏小（约正文 55-60%）|\n| ℹ️ info | Page 3 | Figure 2 仅单栏，建议 figure*（全宽）|\n| ℹ️ info | Page 7 | Display item 密度最高（Table 3+4 + Figure 7），略拥挤 |\n| ℹ️ info | Page 8 | 主文正好 8 页，符合 EMNLP 2026 限制 ✓ |\n| ℹ️ info | Page 9 | Limitations 简洁合规 ✓。References 无 [?] ✓ |\n| ℹ️ info | Page 12 | Figure 10 axis label 字号偏小 |\n| ℹ️ info | Page 15 | AI Assistants 声明 ✓ |\n\n---\n\n## Overall Assessment\n\n| 维度 | 评分 | 说明 |\n|------|------|------|\n| **Overall** | **3.0 — Findings** | 分析贡献（epoch-matched mechanism）有学术价值，但 framing 系统性超出 evidence，实际效果量级不足以支撑 practitioner 定位 |\n| **Soundness** | **3.5** | 实验设计严谨（5 seeds, BH correction, 层次消融），但 scope 限制 + p-value overclaim + τ=0.8 confound 削弱可信度 |\n| **Excitement** | **2.5** | Epoch-matched analysis 有新意，但 Δ=-0.023 PPL (0.13%) 无下游改善，practical impact 有限 |\n| **Confidence** | **4 — High** | 两位 Reviewer 独立得出一致评分，交叉回应近完全共识（仅 1 个 minor framing 分歧 + 1 个事实更正）|\n\n**核心判断**: 论文的学术贡献在于 epoch-matched mechanism analysis——解释 D&R 为何在 continued pretraining 中有效。这一发现值得发表。但存在三层 framing 偏差：\n\n1. **Abstract 事实性错误**：ρ=0.6 p_BH=0.064 未达显著性，Abstract overclaims\n2. **标题-实验 scope gap**：标题暗示通用性，实验仅覆盖极窄场景\n3. **Practitioner framing 与 evidence 矛盾**：Δ=-0.023 PPL 无下游改善、1.7B 递减 43%（且存在 τ=0.8 confound）、ρ<0.4 失效\n\n此外，两个缺失的实验 baseline 影响分析完整性：uniform × 3.2 epochs（区分 filtering vs repetition）和 1.7B + τ=0.7（区分 scale vs hyperparameter effect）。\n\n**建议接收路径**: 修正 Abstract overclaim + 标题 scope 限定 + 重新定位为 mechanism analysis + 补充 uniform × multi-epoch baseline → Findings 发表。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"three findings\"（正确）与 Abstract/Conclusion 的 \"three conditions\"（过强）不一致\n- Scope 声明合理，但标题未反映限制\n- \"illustrative application\" 定位改善了方法预期\n\n### §2 Related Work\n- 缺 RAID 和 M4 detection benchmarks\n- Drayson et al. 对比清晰（3 点差异），但 ModernBERT-150M 未测试\n\n### §3 Method\n- 方法新颖性有限但论文已改善定位\n- \"motivated by convergence theory (Wang 2026)\" 仍暗示理论保证，而 α_eff proxy R²≈0.63 + negative bias -0.03 意味理论前提不完全满足\n\n### §4 Experimental Setup\n- Sliding-window evaluation 缺 window size 参数\n- Temperature scaling 依赖 labeled data 未讨论\n- 1.7B 选择 τ=0.8 而非 τ=0.7 缺乏 justification，构成 confound\n\n### §5 Results\n- §5.1: 消融严谨。Table 1 显示 3 seeds 而 caption 说 5-seed mean。Permuted 仅 seed-42\n- §5.2: ρ=0.6 p_BH=0.064 正文正确报告为 directional，但 Abstract overclaims\n- §5.2: 1.7B Δ=-0.013 仅一段，未正式 scaling analysis。τ=0.8 confound 未讨论\n- §5.2: t=-9.95 vs Appendix I t=-15.4 不一致\n- §5.3: B=4/8/16 monotonic trend 清晰。B=16 仍远低于实际\n- Cohen's d=3.83 的 deterministic ordering caveat 应从 Appendix Q 提升到 §5.1 主文。建议补充 Wilcoxon signed-rank test\n\n### §6 Discussion\n- 第一段与 §5.1 重复，应精简\n- Table 5 + \"conditions\" 仍过强\n- Effect size 段诚实但缺 baseline contextualization\n- α_eff limitations 段坦诚且必要。R2 补充：negative bias → conservative intervention → 解释 b*≈0.9 偏高。可探索 bias correction (+0.03) 改进\n\n### §7 Conclusion\n- \"without measurable downstream gains\" 比 Abstract 诚实，恰恰暴露 Abstract framing gap\n\n### Limitations\n- 三点合规\n\n### Appendix\n- Table 16 seed 456 缺 OOD\n- Appendix Q 对 deterministic ordering 的透明度好，但 caveat 应在主文\n\n---\n\n**审稿圆桌**: R1 × R2, 1 轮初审 + 1 轮交叉回应, 近完全共识（1 minor framing 分歧 + 1 事实更正）\n**Issue Tracker**: 已同步更新至 review_issues.yaml（Round 14, 含 R14-W2 τ=0.8 confound）",
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3",
  "force_resubmit": "True"
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
    "report": "# Round 14 审稿报告 — Provenance Weight Training (FINAL)\n\n**论文标题**: When Does Detect-and-Reweight Work for Synthetic Contamination?\n**投稿目标**: EMNLP 2026 (via ARR), Long Paper\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）\n**交叉回应**: 1 轮。R1→R2: 全部 AGREE。R2→R1: 8 AGREE, 1 partial REBUT (W3), 1 full REBUT (M3)。\n\n---\n\n## Summary\n\n本文通过受控 continued-pretraining 实验（Qwen3-0.6B, 132M FineWeb tokens, 5 seeds）研究 detect-and-reweight 方法在合成数据污染场景下的有效性条件。核心贡献是 epoch-matched mechanism analysis：D&R 方法 >95% 的优势来自 filtered data 的 multi-epoch exposure 而非 per-token 学习质量差异。论文还提出 dual-constrained adaptive exponent b*，无需 per-model grid search 即可改善 held-out perplexity（Δ=-0.023 at ρ=0.4）。实验覆盖 ρ ∈ {0.2, 0.3, 0.4, 0.6}、0.6B/1.7B scale、3 种 detector。\n\n---\n\n## Strengths\n\n**S1. Epoch-matched mechanism analysis 是真正的学术贡献。**\n通过将 D&R 的 raw PPL 优势（Δ=-0.424）与 epoch-matched control（Δ=0.017）对比，清晰分解了 multi-epoch exposure vs per-token quality 的贡献比。这一发现解释了为什么 D&R 在 continued pretraining（多 epoch）下远优于 from-scratch pretraining（通常 <1 epoch）。[R1+R2 AGREE]\n\n**S2. 消融层次设计严谨。**\nAdaptive < Uniform < ESS-only < Random < Permuted 的递进消融有效隔离了 (1) detector signal vs noise, (2) minimum intervention vs unconstrained maximization, (3) provenance signal vs weight non-uniformity 三个维度。Permuted q-scores ablation 特别巧妙——破坏样本级信息但保留权重分布形状，Δ=+0.225 的强降级清晰证明 provenance signal 是 load-bearing。[R1+R2 AGREE]\n\n**S3. 5-seed 实验 + BH 多重比较校正。**\n主实验 5 seeds + Bonferroni-Holm 校正（ρ=0.4: p_BH=0.011），cross-seed variance 极小（σ=0.006）。统计实践规范。[R1+R2 AGREE]\n\n**S4. Calibration vs discrimination 的经验性分离。**\nTF-IDF+LR (AUC=0.94, ECE=0.048) vs GPT-2 (AUC=0.91, ECE=0.131) 对比在 comparable AUC 下隔离了 calibration 效应，揭示 high-AUC but poorly-calibrated detector 反而有害（Δ=+0.098）。[R1+R2 AGREE]\n\n**S5. Scope limitation 声明诚实。**\nIntroduction、Abstract 最后一句、Limitations 节均显式声明限制。Appendix Q 对 deterministic data ordering 对方差的影响也做了透明披露。[R1+R2 AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**N1. Abstract 中 \"ρ ≥ 0.4, reaching conventional significance\" 对 ρ=0.6 构成 overclaim。** [R2 发现, R1 AGREE; 新发现]\n\nAbstract: \"improves over uniform training at contamination ratios ρ ≥ 0.4, reaching conventional significance after multiple-comparison correction\"。\n事实核查：§5.2 报告 ρ=0.6 的 p_BH=0.064（> α=0.05），未达传统显著性。仅 ρ=0.4 的 p_BH=0.011 达标。\"ρ ≥ 0.4\" 暗示两个 contamination level 均显著——这是事实性错误。\n\n> 建议：修改为 \"at ρ=0.4 (p_BH=0.011)\" 或注明 ρ=0.6 仅 marginal significance (p_BH=0.064)。\n\n**N2. 标题 scope 远超实验覆盖面。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C4，连续 4 轮]\n\n\"When Does Detect-and-Reweight Work for Synthetic Contamination?\" 暗示系统性评估，但实验仅覆盖：self-contamination only、0.6B+1.7B、continued pretraining（§6 自述 epoch confound 在 from-scratch 下不适用）、单一数据源 FineWeb、1 个有效 detector。\n\n> 建议：标题加限定词，如 \"...in Controlled Continued Pretraining\"。\n\n**N3. 下游任务零改善但 Abstract 未提及。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-C3]\n\nAbstract \"improves over uniform training\" 未限定 metric。Downstream accuracy 完全相同（0.5414 vs 0.5415）。Conclusion 写了 \"without measurable downstream gains\" 但 Abstract 省略。R2 在交叉回应中进一步指出：论文内部存在定位矛盾——§6 诚实承认影响有限，但 Table 5 仍以 \"for practitioners\" 包装。论文最有价值的贡献（D&R epoch-matching、calibration finding）本质是分析性的，不需要 practitioner framing 来体现价值。\n\n> 建议：Abstract 明确限定 \"improves held-out perplexity\"，注明无下游改善。重新定位为 mechanism analysis。\n\n**N4. Cohen's d=3.83 被 deterministic data ordering 系统性放大，关键 caveat 仅在 Appendix。** [R1 发现, R2 AGREE]\n\nAppendix Q 承认 \"seeds affect only parameter initialization, not data order\"，SD_Δ=0.006 仅反映初始化噪声。Cohen's d=3.83 和 power>0.99 给读者留下 \"效果极其稳健\" 的印象，实际上只说明 \"固定数据顺序下不同初始化产生一致结果\"——远弱于 \"方法在不同条件下稳健有效\"。Uniform baseline 也有类似低方差（σ=0.008），确认窄方差是实验设定属性而非方法特性。此 caveat 应在 §5.1 主文而非仅 appendix 中。\n\n> 建议：在 §5.1 加入 Cohen's d 的 deterministic ordering caveat。补充 Wilcoxon signed-rank test 作为 robustness check。\n\n### Should-Fix (Warning)\n\n**W1. \"Three effectiveness conditions\" framing 过度概括。** [R2 发现, R1 AGREE]\n\nAbstract/Figure 1/Conclusion 使用 \"conditions\" 暗示充分必要条件，但 evidence 仅支持 empirical observations。Introduction 使用 \"three findings\"，术语自身不一致。\n\n> 建议：统一使用 \"three empirical findings\" 或 \"three observed requirements\"。\n\n**W2. Δ=-0.023 PPL 缺乏 baseline contextualization。** [R2 发现, R1 AGREE]\n\n论文未在 continued pretraining 文献中定位 0.023 PPL（0.13% relative）的量级含义。缺少与其他 data curation 方法（DSIR, DsDm, DoReMi）的量级对比。\n\n**W3. Related Work 遗漏 detection benchmarks。** [R2 发现, R1 AGREE; 跨轮次 recurring R11-W3]\n\n缺 RAID (Dugan et al., 2024)、M4 (Wang et al., 2024)。自 Round 13 起被要求补充，仍缺失。\n\n**W4. Table 5 decision framework 基于 3 个 detector，实用性受限。** [R1+R2 AGREE; 跨轮次 recurring R12-W1]\n\nAUC ≥ 0.9 / ECE ≤ 0.05 threshold 仅 3 个数据点，缺少 neural detectors。AUC=0.88, ECE=0.04 区间无 empirical support。\n\n**W5. §6 Discussion 第一段与 §5.1 高度重复。** [R2 发现, R1 AGREE; recurring R13-m1]\n\n§6 开头重述 epoch-matched analysis 全部内容，8 页限制下应精简。\n\n**W6. 缺 uniform × 3.2 epochs baseline，epoch confound 分析不完整。** [R1 发现, R2 AGREE; 跨轮次 recurring R11-W4]\n\nR2 在交叉回应中进一步论证：此 baseline 可区分两个假说——(a) D&R 优势来自 filtering quality（去除坏数据）vs (b) 单纯来自 repetition（多看数据本身有帮助即使含 synthetic）。如果 uniform × 3.2 epochs 也大幅改善 PPL，D&R 的 \"filtering\" 叙事需修正。计算成本低。\n\n**W7. 1.7B 规模效应递减 43%，scaling trend 未正式讨论。** [R1 发现, R2 AGREE; recurring R13-W3]\n\nR2 补充：论文解释（\"larger models more robust to self-generated contamination\"）合理但暗示结构性局限——效果依赖 generator-trainee mismatch，而 self-contamination 中 mismatch 随模型增大缩小，方法 inherently limited。\n\n**W8. ρ≥0.4 实用门槛偏高，实际适用场景极窄。** [R2 发现, R1 AGREE; recurring R13-W4]\n\n多条件交集极窄。\"Decision summary for practitioners\" 可能给读者不准确的 generalizability 信号。\n\n**W9. Temperature scaling T=0.204 依赖 labeled data，限制 deployability。** [R2 发现, R1 AGREE]\n\nDetector calibration 依赖 10K labeled validation split。Web-scale pretraining 中 ground-truth synthetic labels 不可用。\n\n**W10. 1.7B 实验选择 τ=0.8 而非推荐的 τ=0.7，构成 confound。** [R2 交叉回应新发现]\n\n§5.2 报告 1.7B 使用 τ=0.8 但未解释选择理由。0.6B 主结果推荐 τ=0.7（§5.3 Table 6 明确显示 τ=0.7 在 holdout 和 OOD 上均优于 τ=0.8）。1.7B 用 τ=0.8 导致无法区分效应减弱是因为 scale 还是因为 suboptimal τ——这是一个实验设计 confound。\n\n> 建议：解释 τ=0.8 选择理由，或补充 1.7B + τ=0.7 实验。\n\n### Minor Issues\n\n**M1. Table 1 caption 声明 5-seed mean 但仅展示 3 个 seed 列。** [R2 发现, R1 AGREE]\nSeeds 789/234 个体结果不可见，可能引发选择性报告疑虑。\n\n**M2. §5.2 与 Appendix I 的 t 值不一致（t=-9.95 vs t=-15.4）。** [R2 发现, R1 AGREE]\n\n**M3. \"Three effectiveness conditions\" vs \"three findings\" 术语全文不一致。** [R2 发现, R1 AGREE]\n\n**M4. Appendix P Table 16 seed 456 缺 OOD 评估。** [R2 发现, R1 AGREE]\n\n**M5. Sliding-window evaluation 未说明 window size 和 stride。** [R2 发现, R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在核心判断上完全一致：\n\n1. **论文应定位为 mechanism analysis paper**，而非 practitioner-oriented method paper\n2. **Abstract overclaim** 必须修正（p-value + downstream null）\n3. **标题需限定 scope**（连续 4 轮 recurring）\n4. **Epoch-matched analysis 是论文的核心价值**\n5. **Overall 3.0 (Findings)**, Soundness 3.5, Excitement 2.5——两人独立得出完全相同评分\n\n交叉验证关系：\n- R2-N3 ≈ R1-N1（effect size vs framing 矛盾）\n- R2-N2 ≈ R1-W4+W5（scope 限制）\n- R2-W4 ≈ R1-W4（detector threshold 通用性）\n- R2-Q3 ≈ R1-M1（batch size 限制）\n\nR2 额外贡献：N1（p_BH=0.064 overclaim，R1 遗漏）、W3（missing references）、M2（t 值不一致）、W10/Q5（1.7B τ=0.8 confound）。\n\n---\n\n## Reviewer Divergence\n\n两处分歧，均为 minor：\n\n**1. R1-W3: Adaptive b*≈0.9 vs grid-optimal b=0.3 的系统偏差** — R2 partial REBUT\n\n- R1 原始主张：\"违背 minimum intervention 原则\"\n- R2 反驳要点：(a) 比较框架不对等——grid b=0.3 是全局固定值而 mean b*≈0.9 含 per-batch 波动（0~5 range, Figure 10, 5.8% clean batches b*=0）；(b) gap 部分来自 grid-search 的 post-hoc oracle advantage（cross-seed SD=0.035 = adaptive 的 6×）；(c) 但核心 concern 成立——α_eff negative bias ≈-0.03 确实系统推高 b*，是结构性缺陷\n- **圆桌裁定**：观察有效，措辞调整。采纳 R2 更精确的表述：**\"α_eff 的 systematic underestimation 导致 adaptive 方法未能完全实现 minimum intervention，有改进空间（如 bias correction）\"**。不影响评分。\n\n**2. R1-M3: Abstract word count 接近 200-word 限制** — R2 full REBUT\n\n- R1 原始主张：abstract 接近 200-word 限制\n- R2 反驳：实际约 171 words，距限制有 ~15% 余量（~29 words），不构成 weakness\n- **圆桌裁定**：采纳 R2 的事实更正。Abstract word count 合规，不列入报告 weaknesses。\n\n---\n\n## Questions\n\n**Q1. Adaptive reweighting 的实际 use case。** [R2 提出, R1 AGREE]\nD&R (q>0.3) PPL 17.250 大幅优于 adaptive (17.674)。如果 D&R 在所有设定下都优于 adaptive，后者的 use case 是什么？\n\n**Q2. Temperature scaling T=0.204 在无标注数据下的替代方案。** [R2 提出, R1 AGREE]\n\n**Q3. B=4 micro-batch size 的代表性。** [R2 提出, R1 AGREE; recurring R13-W1]\nModern pretraining B=32-128。§5.3 B=4→16 amplification 3.0× 但 B=16 仍远低于实际。\n\n**Q4. α_eff ≥ τ 但 true fraction < τ 的 violation batch 比例。** [R1 提出, R2 AGREE]\n可从现有数据（Appendix J, Table 12: MAE=0.114, bias=-0.03）直接计算。\n\n**Q5. 1.7B 实验选择 τ=0.8 而非 τ=0.7 的理由。** [R2 交叉回应新发现]\n0.6B 推荐 τ=0.7（holdout+OOD 均优），1.7B 却用 τ=0.8，创造 confound。\n\n**Q6. Calibration-corrected α_eff 能否缩小 b* vs grid-optimal 的 gap？** [R1 提出, R2 AGREE]\n用 +0.03 offset 调整 α_eff → b_τ 降低 → mean b* 可能从 0.9 降至更接近 grid-optimal 的 0.3-0.5 range。建设性改进方向。\n\n---\n\n## Missing References\n\n1. **RAID** (Dugan et al., 2024) — AI-generated text detection benchmark\n2. **M4** (Wang et al., 2024) — 多语言 machine-generated text detection\n3. **MATES** (Yu et al., 2024) — training-time data selection（如相关）\n4. **Aioli** (Balachandran et al., 2024) — data mixing（如相关）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求 (not_requested)\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成 (2026-05-25 21:16–21:19, ~2.5 min)\n**统计**: 0 critical, 1 warning, 12 info\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Page 8 | Figure 8 stacked bar chart 5+ 颜色类别，灰度打印下相邻色段难以区分。建议增加纹理填充 |\n| ℹ️ info | Page 1 | 首页无 display item，Figure 1 在 page 2 顶部 |\n| ℹ️ info | Page 2 | Figure 1 legend 字号偏小（约正文 55-60%）|\n| ℹ️ info | Page 3 | Figure 2 仅单栏，建议 figure*（全宽）|\n| ℹ️ info | Page 7 | Display item 密度最高（Table 3+4 + Figure 7），略拥挤 |\n| ℹ️ info | Page 8 | 主文正好 8 页，符合 EMNLP 2026 限制 ✓ |\n| ℹ️ info | Page 9 | Limitations 简洁合规 ✓。References 无 [?] ✓ |\n| ℹ️ info | Page 12 | Figure 10 axis label 字号偏小 |\n| ℹ️ info | Page 15 | AI Assistants 声明 ✓ |\n\n---\n\n## Overall Assessment\n\n| 维度 | 评分 | 说明 |\n|------|------|------|\n| **Overall** | **3.0 — Findings** | 分析贡献（epoch-matched mechanism）有学术价值，但 framing 系统性超出 evidence，实际效果量级不足以支撑 practitioner 定位 |\n| **Soundness** | **3.5** | 实验设计严谨（5 seeds, BH correction, 层次消融），但 scope 限制 + p-value overclaim + τ=0.8 confound 削弱可信度 |\n| **Excitement** | **2.5** | Epoch-matched analysis 有新意，但 Δ=-0.023 PPL (0.13%) 无下游改善，practical impact 有限 |\n| **Confidence** | **4 — High** | 两位 Reviewer 独立得出一致评分，交叉回应近完全共识（仅 1 个 minor framing 分歧 + 1 个事实更正）|\n\n**核心判断**: 论文的学术贡献在于 epoch-matched mechanism analysis——解释 D&R 为何在 continued pretraining 中有效。这一发现值得发表。但存在三层 framing 偏差：\n\n1. **Abstract 事实性错误**：ρ=0.6 p_BH=0.064 未达显著性，Abstract overclaims\n2. **标题-实验 scope gap**：标题暗示通用性，实验仅覆盖极窄场景\n3. **Practitioner framing 与 evidence 矛盾**：Δ=-0.023 PPL 无下游改善、1.7B 递减 43%（且存在 τ=0.8 confound）、ρ<0.4 失效\n\n此外，两个缺失的实验 baseline 影响分析完整性：uniform × 3.2 epochs（区分 filtering vs repetition）和 1.7B + τ=0.7（区分 scale vs hyperparameter effect）。\n\n**建议接收路径**: 修正 Abstract overclaim + 标题 scope 限定 + 重新定位为 mechanism analysis + 补充 uniform × multi-epoch baseline → Findings 发表。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"three findings\"（正确）与 Abstract/Conclusion 的 \"three conditions\"（过强）不一致\n- Scope 声明合理，但标题未反映限制\n- \"illustrative application\" 定位改善了方法预期\n\n### §2 Related Work\n- 缺 RAID 和 M4 detection benchmarks\n- Drayson et al. 对比清晰（3 点差异），但 ModernBERT-150M 未测试\n\n### §3 Method\n- 方法新颖性有限但论文已改善定位\n- \"motivated by convergence theory (Wang 2026)\" 仍暗示理论保证，而 α_eff proxy R²≈0.63 + negative bias -0.03 意味理论前提不完全满足\n\n### §4 Experimental Setup\n- Sliding-window evaluation 缺 window size 参数\n- Temperature scaling 依赖 labeled data 未讨论\n- 1.7B 选择 τ=0.8 而非 τ=0.7 缺乏 justification，构成 confound\n\n### §5 Results\n- §5.1: 消融严谨。Table 1 显示 3 seeds 而 caption 说 5-seed mean。Permuted 仅 seed-42\n- §5.2: ρ=0.6 p_BH=0.064 正文正确报告为 directional，但 Abstract overclaims\n- §5.2: 1.7B Δ=-0.013 仅一段，未正式 scaling analysis。τ=0.8 confound 未讨论\n- §5.2: t=-9.95 vs Appendix I t=-15.4 不一致\n- §5.3: B=4/8/16 monotonic trend 清晰。B=16 仍远低于实际\n- Cohen's d=3.83 的 deterministic ordering caveat 应从 Appendix Q 提升到 §5.1 主文。建议补充 Wilcoxon signed-rank test\n\n### §6 Discussion\n- 第一段与 §5.1 重复，应精简\n- Table 5 + \"conditions\" 仍过强\n- Effect size 段诚实但缺 baseline contextualization\n- α_eff limitations 段坦诚且必要。R2 补充：negative bias → conservative intervention → 解释 b*≈0.9 偏高。可探索 bias correction (+0.03) 改进\n\n### §7 Conclusion\n- \"without measurable downstream gains\" 比 Abstract 诚实，恰恰暴露 Abstract framing gap\n\n### Limitations\n- 三点合规\n\n### Appendix\n- Table 16 seed 456 缺 OOD\n- Appendix Q 对 deterministic ordering 的透明度好，但 caveat 应在主文\n\n---\n\n**审稿圆桌**: R1 × R2, 1 轮初审 + 1 轮交叉回应, 近完全共识（1 minor framing 分歧 + 1 事实更正）\n**Issue Tracker**: 已同步更新至 review_issues.yaml（Round 14, 含 R14-W2 τ=0.8 confound）",
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-25T21:55:27.413038+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3965
}
```

</details>

---


### Assistant

_source line 1494 · 2026-05-25T21:55:37.077716+00:00_

Round 14 审稿完成。报告已更新并投递至 Research Director。

**最终裁定：Overall 3.0 — Findings**

关键更新（相比初版报告）：
- **新增 N4**：Cohen's d=3.83 被 deterministic data ordering 放大，caveat 仅在 Appendix Q
- **新增 W10**：1.7B 用 τ=0.8 而非推荐的 τ=0.7，构成 scale vs hyperparameter confound（R2 交叉回应新发现）
- **Divergence 节**：记录了 R2 对 W3（b* vs grid-optimal 比较框架）的 partial REBUT 和对 M3（abstract word count）的 full REBUT
- **新增 Q4-Q6**：violation rate、τ=0.8 理由、bias correction 可能性
- Issue tracker 同步更新（含 R14-W2 新条目）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---

# Reviewer 1 coordination — Part 1 of 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/d2/d2b424f30b3535d8857b.json)

## Round 1

## Round 1

56 recorded events


### User

_source line 1 · 2026-05-18T06:22:27.419946+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）
**截止日期**: 2026-05-25 (ARR May cycle)
**格式要求**: ACL 模板 `[review]`，长文 ≤8 页正文 + unlimited references，Limitations section 不计页数，double-blind
**论文路径**: `projects/provenance_weight_training/paper/main.tex`（sections/ 子目录含各章节）

### 你的审查侧重：方法严谨性 + 实验设计

请从以下维度深入审查：

1. **方法正确性**
   - 双约束框架（α_eff ≥ τ, ESS ≥ n_min）的数学推导是否严谨
   - Proposition 1 (monotonicity) 的证明是否完整/正确
   - "minimum intervention principle" 的形式化是否站得住脚
   - bisection 算法的正确性和收敛保证

2. **实验设计**
   - Baseline 选择是否充分公平（Uniform / Grid-b / ESS-only / Random / Golden Ratio / Detect & Remove）
   - 自污染设计（用 Qwen3-0.6B 生成 synthetic → 同架构训练）的合理性和局限
   - 评估指标（仅 held-out PPL + 附录 downstream）是否充分
   - 单一模型（0.6B）、单一数据源（FineWeb）、单一 detector（TF-IDF+LR）的外部效度

3. **统计检验**
   - 3-seed 比较的统计功效是否足够（特别是 p=0.30 "indistinguishable" 这一 claim）
   - bootstrap p-value 的使用是否恰当
   - effect size（~0.04 PPL）是否足以支撑论文 claims

4. **消融完整性**
   - τ sweep、n_min sweep、batch size sweep 是否覆盖关键范围
   - ρ=0.2 失效、ρ>0.6 未测试的 implications
   - 缺失的消融（如不同 detector 的影响、不同数据规模）

5. **历史 Issue 检查**
   - RR-W1: 此前论文错误声称 "from random initialization"，应为 "continued pretraining"——检查是否已修正
   - RR-W2: 此前论文错误声称 "balanced real/synthetic test set"，实际为 human-only——检查是否已修正

请输出完整结构化审稿报告：Summary → Strengths → Weaknesses（逐条编号，标 [Must-Fix] / [Should-Fix] / [Minor]）→ Questions → Missing References → Score (1-5) + Confidence (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-18T06:22:35.361323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-18T06:22:35.462556+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-18T06:22:37.524182+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-18T06:22:37.574820+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-18T06:22:39.759486+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-18T06:22:39.845160+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 85
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-18T06:22:41.405282+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-18T06:22:41.940235+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 534
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-18T06:22:45.556055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-18T06:22:45.620243+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 64
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-18T06:22:59.175926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-18T06:22:59.176387+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\bibliography{references}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-18T06:22:59.226943+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-18T06:22:59.227375+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-18T06:23:04.148032+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-18T06:23:04.651074+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-18T06:23:04.701891+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-18T06:23:12.726046+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, I found comprehensive information about ACL Rolling Review 2026 reviewer guidelines, review form, and criteria. Here's what I found:

## Reviewer Guidelines

Each submission receives at least three reviews, and the reviewer's main tasks are checking
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8024
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-18T06:23:16.941952+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-18T06:23:17.395009+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-18T06:23:18.750090+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all fields, scoring scales (1-5 or whatever scale is used), and descriptions for each criterion. I need the exact scoring dimensions and their definitions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all fields, scoring scales (1-5 or whatever scale is used), and descriptions for each criterion. I need the exact scoring dimensions and their definitions."
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-18T06:23:25.276147+00:00_

# ACL Rolling Review Form - Complete Structure

## Primary Review Dimensions

**1. Reviewer Confidence (1-5 scale)**
- 5: Positive evaluation correct; careful reading and familiar with related work
- 4: Quite sure; important points checked carefully
- 3: Pretty sure; general area knowledge but didn't check details thoroughly
- 2: Can defend evaluation; fairly likely missed some details or novelty
- 1: Outside expertise area or paper very difficult to understand

**2. Soundness (1-5 scale with half-points)**
- 5: Most thorough study of its type
- 4: Sufficient support for claims; extra experiments optional
- 3: Adequate support for main claims; minor points need detail
- 2: Main claims lack support; major technical/methodological problems
- 1: Insufficiently thorough or not relevant to computational linguistics

**3. Excitement (1-5 scale with half-points)**
Measures subjective perception of transformational value, community impact, or personal relevance. Ranges from "Highly Exciting" (5) to "Not Exciting" (1).

**4. Overall Assessment (1-5 scale with half-points)**
Recommendation levels span from "Consider for Award" (5) through "Conference" (4), "Findings" (3), various resubmission options, to "Do not resubmit" (1).

## Supporting Sections

- **Limitations and Societal Impact evaluation**
- **Ethical concerns assessment**
- **Reproducibility rating (1-5)**
- **Datasets value (1-5)**
- **Software value (1-5)**
- **Author identity knowledge (1-5)**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6526
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-18T06:23:28.990967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-18T06:23:29.495550+00:00_

1	Web corpora now contain an estimated 20--60\% machine-generated text, and training on such contaminated data risks model collapse.
2	Detect-and-reweight methods suppress likely-synthetic samples via $w(x) = (1-q(x))^b$, but the exponent $b$ critically determines outcomes and requires per-model grid search (typically multiple complete training runs) to tune.
3	
4	We propose a dual-constrained adaptive exponent $b^*$ derived per-batch from detector scores alone: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling).
5	This minimum intervention principle applies only as much downweighting as needed, with zero validation cost.
6	
7	On Qwen3-0.6B continued pretraining (132M FineWeb tokens, 40\% synthetic contamination), adaptive $b^*$ is statistically indistinguishable from the grid-searched optimum (3-seed means: PPL 17.651 vs.\ 17.620, $p{=}0.30$).
8	A complete ablation confirms that both detector signal and minimum intervention are necessary: random reweighting degrades performance (17.803), ESS-only maximum intervention provides no improvement (17.737 vs.\ uniform 17.694), and only the dual-constrained method improves.
9	The advantage extends to $\rho{=}0.6$ (3-seed $\Delta{=}{-}0.028$, $p{<}0.01$), where the ESS-only/uniform gap collapses but adaptive reweighting maintains its improvement through the quality constraint alone.
10	Hard filtering achieves lower absolute PPL (17.290) but requires a calibrated detection threshold that reweighting avoids.
11	The quality threshold $\tau$ is robust across $[0.5, 0.8]$, and a lightweight TF-IDF + logistic regression detector (AUC = 0.939, calibrated ECE = 0.048) suffices, suggesting that score calibration may matter as much as raw classification accuracy.
12	
13	Principled per-batch exponent derivation eliminates grid search while retaining the effectiveness of detect-and-reweight pretraining
…[truncated 5 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-18T06:23:29.495947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-18T06:23:30.451213+00:00_

1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation (\emph{model collapse}), and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.
6	
7	A natural response is \emph{detect-and-reweight}: suppress likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a classifier's synthetic probability estimate.
8	However, the exponent $b$ critically determines outcomes and requires per-model validation-set grid search~\citep{drayson2025detection}; alternative approaches require the exact contamination ratio~\citep{he2025golden} or a well-calibrated detection threshold for hard filtering~\citep{feng2025beyond}.
9	
10	Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
11	We formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\aeff(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $\nmin$.
12	The quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effec
…[truncated 3098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-18T06:23:30.451591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-18T06:23:30.954083+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
6	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
7	
8	\paragraph{Detection and Filtering of Machine-Generated Text.}
9	Given the severity of contamination, a natural response is to detect and remove synthetic content.
10	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
11	Both produce continuous confidence scores suitable as input to downstream weighting, including ours.
12	On the mitigation side, \citet{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
13	\citet{guo2025escaping} similarly rely on verification-based selection.
14	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
15	
16	Most directly related to our work, \citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic 
…[truncated 3369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-18T06:23:30.954447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-18T06:23:31.412577+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	At $b = 0$, $\alpha_{\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\alpha_{\mathrm{ef
…[truncated 8268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-18T06:23:31.412952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-18T06:23:31.864440+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at ratio $\rho = 0.4$ via uniform random mixing.
4	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.939, calibrated ECE\,=\,0.048 after temperature scaling with $T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	
11	\paragraph{Training.}
12	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
13	All main comparisons use three random seeds (42, 123, 456).
14	
15	\paragraph{Evaluation.}
16	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
17	All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.
18	
19	\paragraph{Methods.}
20	We compare five approaches:
21	\begin{itemize}[nosep,leftmargin=*]
22	  \item \textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).
23	  \item \textbf{Grid-$b$}: fixed $b \in \{0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$, best select
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-18T06:23:31.864925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-18T06:23:32.366945+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ is statistically indistinguishable from grid-best: 3-seed means 17.651 vs.\ 17.620 for grid $b{=}0.3$ (gap 0.031, bootstrap $p{=}0.30$).
8	The grid sweep requires nine complete training runs to identify the optimum~\citep{drayson2025detection}; the adaptive method requires one, with lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
9	Using the mean of per-batch $\bstar$ ($\bar{b}^*{=}1.19$) as a fixed exponent yields PPL 17.693, comparable to uniform (17.694); per-batch adaptation is essential.
10	
11	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
12	Random weights $\mathcal{U}(0,2)$ (mean 17.803) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
13	ESS-only (mean $17.737 {\pm} 0.021$) uses $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
14	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves over uniform (paired gap $0.086$, $p{<}0.01$, $N{=}3$).
15	Figure~\ref{fig:grid_b_trend} contextualizes this: the grid curve has a broad plateau at $b \in [0.1, 0.5]$ (PPL 17.620--17.655), and adaptive $\bstar$ (mean 17.651) falls within it; ESS-only $\bstar$ (mean 3.5--5.9) lies in the degradation zone beyond the plateau.
16	
17	Golden Ratio~\citep{he202
…[truncated 6805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-18T06:23:32.367294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-18T06:23:32.819206+00:00_

1	\paragraph{Why minimum intervention works.}
2	The central finding is that restraint in downweighting outperforms aggressiveness.
3	ESS-only reweighting (PPL 17.737) performs worse than uniform (17.694), while the dual-constrained adaptive $\bstar$ achieves 17.651 by selecting the \emph{smallest} $b$ that meets the quality floor.
4	The binding statistics (\S\ref{sec:regime}) explain why: in the 38.2\% of batches where $\aeff$ determines $\bstar$, the selected exponent is 4.9$\times$ lower than the ESS-only upper bound, preventing unnecessary suppression of borderline samples ($q \approx 0.4$--$0.6$) that carry useful training signal.
5	This behavior is robust across contamination levels ($\aeff$-binding rate: 38.2\% at $\rho{=}0.4$, 33.4\% at $\rho{=}0.6$) and seeds (CV ${<}2\%$).
6	
7	\paragraph{Where the advantage manifests.}
8	The advantage appears entirely at evaluation (PPL 17.65 vs.\ 17.69 on human-authored text); unweighted training loss curves overlap (${\sim}1.4\%$ difference), consistent with reshaping the effective distribution without changing the optimization trajectory.
9	
10	\paragraph{Why not a fixed $b$?}
11	Training with the aggregate mean $\bstar \approx 1.4$ as a fixed exponent yields PPL 17.693, no better than uniform (17.694), because the average masks extreme per-batch heterogeneity (std $\approx$ 1.9, range $[0, 20]$): it over-penalizes the 55\% of batches needing mild correction ($\bstar < 1$) and under-penalizes the 3.6\% requiring aggressive intervention ($\bstar > 5$).
12	The grid-searched optimum ($b{=}0.3$ at $\rho{=}0.4$, $b{=}0.5$ at $\rho{=}0.6$) varies with contamination level, requiring per-setting retuning that the adaptive method eliminates.
13	
14	\paragraph{$\tau$ as a practical dial.}
15	$\tau \in [0.5, 0.8]$ all outperform uniform (Table~\ref{tab:tau}), with asymmetric sensitivity: under-cleaning is mild, while over-cleaning ($\tau > 0.8$) sharply degrades as $\bstar$ inflates.
16	This reinforces the minimum intervention int
…[truncated 762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-18T06:23:32.819717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-18T06:23:33.321584+00:00_

1	We introduced Minimum Intervention Reweighting, a dual-constraint framework that derives per-batch exponents $\bstar$ without validation data by finding the smallest $b$ satisfying $\aeff(b) \geq \tau$ subject to $\mathrm{ESS}(b) \geq \nmin$.
2	
3	At 0.6B scale with 40\% contamination, adaptive $\bstar$ is statistically indistinguishable from grid-best (3-seed means 17.651 vs.\ 17.620, $p{=}0.30$) while eliminating grid search entirely.
4	At $\rho{=}0.4$, the ablation Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random confirms that both detector signal and minimum intervention are necessary.
5	Hard filtering achieves lower absolute PPL (17.290) but requires threshold calibration that reweighting avoids.
6	At $\rho{=}0.6$, adaptive $\bstar$ remains significantly better than uniform (3-seed $\Delta{=}{-}0.028$, $p{<}0.01$); the ESS-only/uniform gap collapses at this level, isolating $\aeff$ as the key driver of the advantage.
7	A lightweight TF-IDF + LR detector (AUC\,=\,0.939, ECE\,=\,0.048) suffices throughout.
8	
9	Future work: scaling to 3B+ models, multi-detector comparison to test the calibration hypothesis, and evaluation on naturally contaminated corpora.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-18T06:23:33.322031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-18T06:23:33.773476+00:00_

1	\paragraph{Scale and cross-model transfer.}
2	All main experiments use Qwen3-0.6B with batch size 4.
3	Cross-model transfer (Llama-3.2-3B, single seed): adaptive training achieves PPL and HellaSwag parity with uniform (within 0.5\,pp).
4	MMLU shows a $+$1.6\,pp advantage for adaptive, though this observation requires multi-seed replication.
5	Overall, the dual-constrained method transfers to a different architecture without degradation, but we cannot claim improvement from a single seed.
6	Batch-level statistics at larger batch sizes and scale-dependent threshold tuning remain important directions for future work.
7	
8	\paragraph{Contamination range.}
9	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative), indicating an effective range of $\rho \geq 0.4$ with $\tau{=}0.8$.
10	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
11	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
12	
13	\paragraph{Detector coverage.}
14	We evaluate one detector family (TF-IDF + logistic regression).
15	Whether score calibration matters as much as raw discrimination for reweighting remains a hypothesis; a systematic ablation across detector architectures and quality levels is needed to test it.
16	
17	\paragraph{Threshold.}
18	$\tau$ is an empirical hyperparameter.
19	The convergence theory of \citet{wang2026survive} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
20	
21	\paragraph{Evaluation.}
22	Main results report held-out perplexity.
23	Downstream benchmarks (Appendix~\ref{app:downstream}) show no significant difference between adaptive and uniform at 0.6B; systematic downstream evaluation across seeds and larger scales would strengthen the practical case.
24
…[truncated 415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-18T06:23:33.774002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-18T06:23:33.824795+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
5	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
6	Then
7	\begin{equation*}
8	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
9	\end{equation*}
10	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
11	Taking the derivative with respect to $b$:
12	\begin{align*}
13	  \frac{d\pi_i}{db}
14	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right)
15	  = \pi_i \!\left(\ln(1{-}q_i) - \sum_j \pi_j \ln(1{-}q_j)\right).
16	\end{align*}
17	Substituting,
18	\begin{align*}
19	  \frac{d\alpha_{\mathrm{eff}}}{db}
20	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
21	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
22	\end{align*}
23	For any detector with better-than-random discrimination, real samples ($r_i = 1$) have $q_i \leq 0.5$ on average, and thus higher $\ln(1{-}q_i)$ than synthetic samples.
24	The weighted covariance $\mathrm{Cov}_{\pi}(r_i, \ln(1{-}q_i))$ is therefore non-negative, establishing that $\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$.
25	\end{proof}
26	
27	\section{Grid Search Details}
28	\label{app:grid}
29	
30	Table~\ref{tab:grid_full} reports held-out PPL for all grid-$b$ values at $\rho = 0.4$ (seed\,42).
31	
32	\begin{table}[h]
33	\centering
34	\small
35	\begin{tabular}{@{}cc@{}}
36	\toprule
37	$b$ & PPL $\downarrow$ \\
38	\midrule
39	0.1 & 17.657 \\
40	0.2 & 17.640 \\
41	0.3 & \textbf{17.640} \\
42	0.5 & 17.651 \\
43	1.0 & 17.692 \\
44	1.5 & 17.718 \\
45	2.0 & 17.741 \\
46	3.0 & 17.774 \\
47	5.0 & 17.818 \\
48	\bottomrule
49	\end{tabular}
50	\caption{Full grid search results ($\rho{=}0.4$, seed\,42).
51	$b \in [0.1, 0.5]$ forms a broad plateau (three-seed mean for $b{=}0.1$: $17.655 \pm 0.009$); $b{=}0.3$ is the post-hoc best.}
52	\label{tab:grid_full}
53	\end{table}
54	
55	\section{Quality Threshold Sweep}
56	\label{app:tau_s
…[truncated 5469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-18T06:23:39.698054+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-18T06:23:40.100219+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-18T06:23:42.119048+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: (1) the scoring scales with exact descriptions for each level of Soundness, Excitement, and Overall Assessment, (2) what reviewers should evaluate, (3) any specific criteria or dimensions. I need the exact scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: (1) the scoring scales with exact descriptions for each level of Soundness, Excitement, and Overall Assessment, (2) what reviewers should evaluate, (3) any specific criteria or dimensions. I need the exact scoring rubric."
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-18T06:23:46.818516+00:00_

# ARR Reviewer Guidelines: Scoring Rubric

Based on the provided documentation, **the guidelines do not contain explicit numerical scoring scales** with detailed descriptions for each Soundness, Excitement, or Overall Assessment level.

## What the Guidelines Specify

The document mentions that "Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation" but provides only conceptual guidance rather than a scored rubric:

**Soundness:** "The soundness scores must be justified by the text of the review." Low scores require substantive justification rooted in identified technical flaws.

**Excitement:** Described as "orthogonal to the assessment of soundness" and reflecting personal interest rather than objective merit.

**Overall Assessment:** Characterized as "a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

## What Reviewers Should Evaluate

Key evaluation dimensions include:
- Technical soundness and methodological validity
- Clarity and specificity of contributions
- Appropriate scope relative to claims
- Reproducibility and statistical rigor
- Professional tone and constructive feedback

## Additional Resources

The guidelines reference an "[ARR review form](https://aclrollingreview.org/reviewform)" post "describing the ARR review form in detail," which likely contains the actual numerical scale definitions, but that document isn't included in your provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4699
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-18T06:23:49.647232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-18T06:23:50.049114+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@article{drayson2025detection,
5	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
6	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
7	  journal={arXiv preprint arXiv:2502.15654},
8	  year={2025}
9	}
10	
11	@article{he2025golden,
12	  title={Golden Ratio Weighting Prevents Model Collapse},
13	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
14	  journal={arXiv preprint arXiv:2502.18049},
15	  year={2025}
16	}
17	
18	@article{wang2026survive,
19	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
20	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
21	  journal={arXiv preprint arXiv:2602.16065},
22	  year={2026}
23	}
24	
25	@article{shumailov2024model,
26	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
27	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
28	  journal={Nature},
29	  volume={631},
30	  pages={755--759},
31	  year={2024}
32	}
33	
34	@inproceedings{dohmatob2025strong,
35	  title={Strong Model Collapse},
36	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
37	  booktitle={ICLR},
38	  year={2025}
39	}
40	
41	@article{vehtari2024psis,
42	  title={Pareto Smoothed Importance Sampling},
43	  author={Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, Jonah},
44	  journal={JMLR},
45	  year={2024}
46	}
47	
48	@inproceedings{sow2025dynamic,
49	  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
50	  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans-Arno and Liang, Yingbin},
51	  booktitle={ICLR},
52	  year={2025}
53	
…[truncated 4590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-18T06:23:51.354310+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the EXACT scoring scales with numerical values and their descriptions for: (1) Soundness scale, (2) Excitement scale, (3) Overall Assessment scale, (4) Confidence scale, (5) Reproducibility scale, and any other scored dimensions. I need every number and its exact text description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the EXACT scoring scales with numerical values and their descriptions for: (1) Soundness scale, (2) Excitement scale, (3) Overall Assessment scale, (4) Confidence scale, (5) Reproducibility scale, and any other scored dimensions. I need every number and its exact text description."
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-18T06:23:59.133613+00:00_

# ACL Rolling Review Scoring Scales

## 1. Soundness Scale
- 5 = "Excellent: This study is one of the most thorough I have seen"
- 4.5 = (no description provided)
- 4 = "Strong: This study provides sufficient support for all of its claims"
- 3.5 = (no description provided)
- 3 = "Acceptable: This study provides sufficient support for its main claims"
- 2.5 = (no description provided)
- 2 = "Poor: Some of the main claims are not sufficiently supported"
- 1.5 = (no description provided)
- 1 = "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 2. Excitement Scale
- 5 = "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- 4.5 = (no description provided)
- 4 = "Exciting: I would mention this paper to others and/or make an effort to attend"
- 3.5 = (no description provided)
- 3 = "Interesting: I might mention some points of this paper to others and/or attend"
- 2.5 = (no description provided)
- 2 = "Potentially Interesting: this paper does not resonate with me"
- 1.5 = (no description provided)
- 1 = "Not Exciting: this paper does not resonate with me"

## 3. Overall Assessment Scale
- 5 = "Consider for Award"
- 4.5 = "Borderline Award"
- 4 = "Conference: I think this paper could be accepted"
- 3.5 = "Borderline Conference"
- 3 = "Findings: I think this paper could be accepted to the Findings of the ACL"
- 2.5 = "Borderline Findings"
- 2 = "Resubmit next cycle: substantial revisions can be completed by the next ARR cycle"
- 1.5 = "Resubmit after next cycle: substantial revisions cannot be completed by next cycle"
- 1 = "Do not resubmit"

## 4. Reviewer Confidence Scale
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure. It's unlikely, though conceivable, that I missed something"
- 3 = "Pretty sure, but there's a chance I missed something"
- 2 = "Willing to defend my evaluation, but fairly likely that I missed some details"
- 1 = "Not my area, or paper is very hard to understand"

## 5.
…[truncated 1369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7779
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-18T06:24:12.680029+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-18T06:24:28.196988+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 23, \"total_citations\": 45, \"unique_cited_keys\": 23, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 18, \"online_not_found\": 2, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"drayson2025detection\", \"type\": \"article\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.15654\"}, {\"key\": \"he2025golden\", \"type\": \"article\", \"title\": \"Golden Ratio Weighting Prevents Model Collapse\", \"authors\": \"He, Hengzhi and Xu, Shirong and Cheng, Guang\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.18049\"}, {\"key\": \"wang2026survive\", \"type\": \"article\", \"title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive T...\", \"authors\": \"Wang, Kevin and Niu, Hongqian and Li, Didong\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.16065\"}, {\"key\": \"shumailov2024model\", \"type\": \"article\", \"title\": \"AI Models Collapse When Trained on Recursively Generated Data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2025strong\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"ICLR\"}, {\"key\": \"vehtari2024psis\", \"type\": \"article\", \"title\": \"Pareto Smoothed Importance Sampling\", \"authors\": \"Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, J...\", \"year\": \"2024\", \"venue
…[truncated 17168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 15516
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-18T06:27:32.280203+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**审查侧重**: 方法严谨性 + 实验设计\n**评分标准**: ACL Rolling Review (ARR) 官方 review form\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**Confidence**: 4 / 5\n**一句话总结**: 方法直觉清晰、框架简洁，但核心 claim 的统计支撑存在方法论缺陷（用 failure-to-reject 代替 equivalence test），实验规模和 detector 覆盖不足以支撑论文的一般性主张。\n\n---\n\n## ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5 / 5 | Proposition 1 证明存在 gap（$r_i$ 是估计量非 ground truth，与理论动机脱节）；\"indistinguishable\" claim 的统计方法不当（§详见 N1）；effect size 极小（0.24%）且 downstream 无显著差异 |\n| Excitement | 3.0 / 5 | 问题重要且实际（web 数据污染加剧），minimum intervention 直觉好，但实验未能在下游任务或更大规模上展示实际价值 |\n| Reproducibility | 4 / 5 | 算法伪代码清晰、超参设置完整、3-seed 报告；但代码未提供 |\n| Datasets | 1 / 5 | 无新数据集 |\n| Software | 1 / 5 | 无代码发布 |\n\n---\n\n## Summary\n\n本文提出一种双约束自适应指数选择框架用于 detect-and-reweight 预训练：给定 per-sample 检测器分数 $q(x)$，对每个 batch 求解满足 $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$（质量下界）且 $\\mathrm{ESS}(b) \\geq n_{\\min}$（稳定性上界）的最小 $b$，称为 \"minimum intervention principle\"。在 Qwen3-0.6B continued pretraining（132M tokens FineWeb，40% 合成污染）上，方法与 grid-searched best 统计不可区分（PPL 17.651 vs 17.620，$p=0.30$），消融证实 detector 信号和 minimum intervention 都是必要的。\n\n## Strengths\n\n**S1.** 问题定义清晰且实际。Web 数据中合成内容比例持续增长，需要无需验证集和已知污染比例的自适应方法。论文清楚地将此问题形式化为受约束优化。\n\n**S2.** 双约束框架设计简洁。$\\alpha_{\\mathrm{eff}}$ 和 ESS 的对立单调性自然地定义了 feasible region，bisection 求解高效（$\\sim$44 FLOPs per batch）。\"最小干预\"直觉合理：borderline samples 仍有训练价值，过度下权适得其反。\n\n**S3.** 消融设计有层次。Random → ESS-only → Uniform → Adaptive 的四级层次有效分离了 detector 信号和 minimum intervention 两个因素。固定 $\\bar{b}^*$ 实验（PPL 17.693 ≈ uniform）进一步证明 per-batch adaptation 的必要性。\n\n**S4.** 超参敏感性分析全面。$\\tau$ sweep（0.50–0.95）、$n_{\\min}$ sweep、batch size sweep ($B \\in \\{4,8,16\\}$) 均有覆盖，$\\tau \\in [0.5, 0.8]$ 的宽 safe range 是实用性的重要证据。\n\n**S5.** Related Work 定位准确。与 Drayson et al. (2025) 的三点差异（per-model grid search → per-batch adaptive, SIR resampling → loss reweighting, strong detector → lightweight detector）表述清楚，positioning 不过度。\n\n**S6.** 历史问题已修正。此前版本错误声称 \"from random initialization\"（现为 \"continued pretraining from pretrained weights\"，Section 4）和 \"balanced real/synthetic test set\"（现为 \"containing only human-authored text\"，Section 4）。两个问题均已正确修正。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **\"Statistically indistinguishable\" claim 使用了错误的统计范式**\n- 具体位置：Abstract, Section 5.1, Section 6 (Conclusion)\n- 问题：论文核心 claim 是 adaptive $b^*$ \"statistically indistinguishable from grid-searched optimum\"，依据是 bootstrap $p = 0.30$。但 $p = 0.30$ 仅表示 **未能拒绝**差异为零的零假设，不等于证明等价。在 N=3（3 seeds）的极小样本下，统计功效（power）极低——即使真实差异为 0.5 PPL，也很可能得到 $p > 0.05$。要正式声称\"不可区分\"，需要 equivalence test（如 TOST, Two One-Sided Tests），预设实际等价边界 $\\delta$，并证明差异落在 $[-\\delta, +\\delta]$ 内。当前表述将 absence of evidence 当作 evidence of absence，这是统计推断的基本错误。\n- 为什么影响接收：这是论文第一贡献的核心支撑。如果 \"indistinguishable\" claim 不成立，论文的核心价值主张需要重新表述。\n- 建议修改方向：(1) 执行 TOST 等价检验，明确 $\\delta$（如 0.1 PPL）；(2) 若功效不足，将 claim 降级为 \"adaptive $b^*$ achieves comparable PPL to grid-best, with the gap not reaching significance at N=3\"；(3) 增加 seeds 数量至少到 5-10 以提高统计功效。\n\n**N2** [critical] **$\\alpha_{\\mathrm{eff}}$ 的理论动机与实际计算之间存在逻辑断层**\n- 具体位置：Section 3.2 (Eq. 2), Proposition 1 proof (Appendix A)\n- 问题：$\\alpha_{\\mathrm{eff}}$ 使用 $r_i = \\mathbf{1}[q_i \\leq 0.5]$ 作为样本是否为真实数据的 indicator。但理论动机来自 Wang et al. (2026)，其收敛速率定理基于 **真实的** real-data fraction $\\alpha$，不是检测器估计的 $\\hat{\\alpha}$。这个 gap 意味着：当检测器不完美时（AUC = 0.939，46.3% 样本在不确定区间 $[0.2, 0.8]$），$\\alpha_{\\mathrm{eff}}$ 可能系统性偏离真实 $\\alpha$，$\\tau$ 的保证不再成立。Proposition 1 的证明也依赖 $r_i$ 与 $\\ln(1-q_i)$ 的正协方差，但 $r_i$ 本身就是 $q_i$ 的阈值函数——两者不是独立信号，covariance 的正性是 tautological（高 $q$ 导致 $r_i = 0$，低 $q$ 导致 $r_i = 1$ 且高 $\\ln(1-q_i)$）。这意味着 $\\alpha_{\\mathrm{eff}}$ 增加并非因为\"权重转移到真实样本\"，而仅仅因为\"权重转移到检测器认为是真实的样本\"。\n- 为什么影响接收：Proposition 1 是方法框架的数学基础。如果 $\\alpha_{\\mathrm{eff}}$ 不是 true $\\alpha$ 的良好代理，quality constraint 的理论根基不稳。\n- 建议修改方向：(1) 明确讨论 $\\alpha_{\\mathrm{eff}}$ 是 estimated effective real proportion，不是 true real proportion；(2) 在已知 ground truth 的合成实验中，报告 $\\alpha_{\\mathrm{eff}}$ vs true $\\alpha$ 的 correlation；(3) 分析检测器精度如何影响 $\\alpha_{\\mathrm{eff}}$ 的保证。\n\n**N3** [critical] **实验外部效度严重不足**\n- 具体位置：Section 4 (Experimental Setup), Section 8 (Limitations)\n- 问题：全部主实验在单一设定下完成：\n  - **单一模型规模**：0.6B。Limitations 提到 Llama-3.2-3B 迁移实验（单 seed）显示 PPL 和 HellaSwag 与 uniform 持平，MMLU +1.6pp 但需要 multi-seed。这不构成 scaling 证据。\n  - **单一数据源**：FineWeb。真实 web 数据的领域分布、噪声模式可能截然不同。\n  - **单一 detector**：TF-IDF + LR。论文声称 \"score calibration may matter as much as raw classification accuracy\"（Abstract, Section 4），但未用任何其他检测器验证。这个 claim 完全无实验支撑。\n  - **自污染设计**：用 Qwen3-0.6B 生成合成数据，再用同架构训练。真实场景中生成器通常是更大/不同模型（GPT-4, Claude 等），检测难度和分布特征完全不同。\n  - **$\\rho = 0.2$ 失效**：Limitations 报告 $\\rho = 0.2$ 方法反而伤害 PPL（+0.046），但无深入分析。$\\rho > 0.6$ 未测试。\n- 为什么影响接收：论文 framing 为 general-purpose contamination-aware pretraining method，但实验证据只覆盖一个极窄的 setting。EMNLP/ARR 审稿人会要求至少 2 个模型规模 + 2 个 detector 的交叉验证。\n- 建议修改方向：(1) 至少增加一个 neural detector（如 ModernBERT）的对比实验，直接验证 calibration hypothesis；(2) 增加至少一个 1B+ 规模的 3-seed 实验；(3) 分析 $\\rho = 0.2$ 失效的原因（可能是 $\\tau = 0.8$ 在低污染时已是 over-constraint）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Downstream benchmarks 未能展示实际价值**\n- 具体位置：Appendix E (Table 8)\n- 问题：5 个 downstream benchmarks（ARC-Challenge, ARC-Easy, HellaSwag, PIQA, WinoGrande）全部在标准误差内，且 4/5 个 adaptive 略微 **低于** uniform。论文说 \"preserves downstream performance\"，但审稿人会问：如果 PPL 改善不能转化为任何可测量的下游改善，这个方法的实际价值是什么？\n- 建议：(1) 增加更多种类的 benchmarks（如 MMLU, GSM8K），尤其是对数据质量敏感的任务；(2) 在更大模型上验证 PPL 改善是否放大为下游差异；(3) 至少用多 seed 做下游评估。\n\n**W2** [warning] **Proposition 1 声称 strictly increasing 但证明只建立 non-decreasing**\n- 具体位置：Section 3.2, Proposition 1 statement vs proof\n- 问题：命题声称 \"$\\alpha_{\\mathrm{eff}}(b)$ is strictly increasing in $b$\"。证明得到 $d\\alpha_{\\mathrm{eff}}/db = \\mathrm{Cov}_\\pi(r_i, \\ln(1-q_i))$，然后说 \"this covariance is non-negative\"。Non-negative 只能推出 non-decreasing，不是 strictly increasing。命题前提 \"containing both real and synthetic samples with distinct $q$-values\" 旨在排除退化情况，但证明中没有严格论证在此前提下 covariance 严格为正。需要论证 $r_i$ 和 $\\ln(1-q_i)$ 不是 $\\pi$-a.s. 常数。\n- 建议：严格化证明，或将命题降级为 non-decreasing，并注明在 non-degenerate 条件下严格成立。\n\n**W3** [warning] **ESS monotonicity 未证明**\n- 具体位置：Section 3.2, line 57\n- 问题：\"$\\mathrm{ESS}(b)$ is monotonically decreasing in $b$: larger exponents concentrate the weight distribution, a standard property of exponential tilting (Kimura et al., 2024).\"。但 Kimura et al. (2024) 是一篇 importance weighting 综述，不一定包含这个具体结论。ESS 的 monotonicity 对 bisection 算法的正确性至关重要——如果 ESS 非单调，$b_{\\mathrm{ESS}}$ 可能不唯一，bisection 会失败。这个性质应该被正式证明或给出精确引用。\n- 建议：在 Appendix 中加入 ESS 单调性的简短证明，至少对 $(1-q)^b$ 形式的 weights。\n\n**W4** [warning] **Grid-$b$ baseline 存在 post-hoc oracle 问题但论文未充分讨论**\n- 具体位置：Section 4 (Methods), Table 1 caption\n- 问题：Grid-$b$ 的 best 是 post-hoc 在测试集上选择的（\"best selected post-hoc by held-out PPL\"），这给了 grid search 一个 oracle 优势。论文确实在 Table 1 caption 中标注了 $^\\ddagger$Post-hoc oracle，但核心 claim \"indistinguishable from grid-searched optimum\" 是拿 adaptive 和 post-hoc oracle 比。在实践中，grid search 需要一个独立的 validation set 来选择 $b$，选出的 $b$ 在 test set 上通常略差于 post-hoc best。因此，adaptive 方法在公平比较中可能实际上优于真正的 grid search（用 val set 选 $b$，在 test set 上评估）。\n- 建议：增加一个 split-validation grid search baseline（用 val set 选 $b$，用 test set 评估），以提供更公平的比较。\n\n**W5** [warning] **Detect & Remove 和 Golden Ratio 仅单 seed**\n- 具体位置：Table 1\n- 问题：两个重要 baseline 只报告了 seed 42 的结果。Detect & Remove（17.290）显著优于所有 reweighting 方法，但没有多 seed 验证。在论文的核心叙事中，Detect & Remove 的优势被归因于 \"distribution match\"，但如果这个结果在多 seed 下不稳定，论文的 framing 需要调整。\n- 建议：至少用 3 seeds 复现 Detect & Remove 和 Golden Ratio。\n\n**W6** [warning] **效应量在实际意义上是否足够大？**\n- 具体位置：Section 5.4, Limitations (Effect size)\n- 问题：主要改善 0.043 PPL（0.24% relative）。论文自己也承认 \"modest in absolute terms\"。在 0.6B 模型上，这个改善完全不可能在任何下游任务上被观测到（Appendix E 已证实）。论文的实际贡献缩小为：消除 grid search，同时不伤害性能。但这个 framing 与论文标题和 Abstract 的主张（\"contamination-aware pretraining\"）有 mismatch——读者预期一个能显著改善训练质量的方法，而不仅仅是一个省去 grid search 的方法。\n- 建议：调整 framing，将核心卖点从 \"improved pretraining\" 转为 \"matching grid-search at zero validation cost\"。这更诚实，且仍有实际价值。\n\n---\n\n## Questions for Authors\n\n**Q1.** $\\alpha_{\\mathrm{eff}}$ 使用阈值 $q_i \\leq 0.5$ 判断真实/合成（Section 3.2, Eq. 2），这与 hard filtering 的 $q > 0.5$ 阈值相同。如果将 $r_i$ 改为 soft indicator $r_i = 1 - q_i$，性能如何变化？这会消除 0.5 阈值的硬依赖。\n\n**Q2.** $\\rho = 0.2$ 时方法反而伤害 PPL（+0.046，Limitations），但 $\\tau = 0.8$ 在低污染下可能要求过高的 $b$。是否测试过 $\\tau = 0.5$ 或 $\\tau = 0.6$ 在 $\\rho = 0.2$ 时的表现？\n\n**Q3.** Section 5.4 提到 \"unweighted training loss curves overlap (~1.4% difference)\"。如果训练 loss 几乎不变，PPL 改善从何而来？是否因为 evaluation set 是 human-only 而 training 的 reweighting 恰好对 human-like 分布做了隐式 importance weighting？如果 evaluation set 包含合成样本，PPL 差异是否消失？\n\n**Q4.** 论文使用 micro-batch size $B = 4$（Section 4），这意味着 ESS 的取值范围是 $[1, 4]$，$n_{\\min} = 2$ 将 ESS 下界设在总样本的 50%。在如此小的 batch 上，$\\alpha_{\\mathrm{eff}}$ 和 ESS 的估计方差必然很大。是否分析过 per-batch $b^*$ 的噪声对训练稳定性的影响？\n\n**Q5.** 论文声称 \"score calibration may matter as much as raw classification accuracy\"（Abstract），但只使用了一个 detector。要支撑这个 claim，至少需要一个 high-AUC 但 poorly-calibrated detector 和一个 lower-AUC 但 well-calibrated detector 的对比。是否有计划做这个实验？\n\n---\n\n## Missing References / 引用问题\n\n1. **`guo2025escaping`**（Guo et al., 2025）在线验证未找到匹配。bib 条目缺少 arXiv ID，venue 仅写 \"arXiv preprint\"，无法确认真实性。需要补充完整信息或确认这篇论文确实存在。\n\n2. **`vehtari2024psis`** 年份不一致：bib 写 2024，但 PSIS 原始版本为 2015（arXiv:1507.02646），JMLR 正式发表版可能为 2024。建议核实并使用正式发表年份。\n\n3. **Temperature scaling** 用于检测器校准（Section 4, \"calibrated ECE = 0.048 after temperature scaling with $T = 0.204$\"），但未引用 Guo et al. (2017) \"On Calibration of Modern Neural Networks\" 等温度校准的基础文献。\n\n4. **缺少 data contamination 检测的近期重要工作**：如 Hans et al. (2024) \"Spotting LLMs with Binoculars\" 等基于 likelihood ratio 的检测方法，可作为 detector 替代方案讨论。\n\n5. **缺少 equivalence testing / TOST 方法引用**：如果论文要声称 \"indistinguishable\"，应引用统计等价性检验文献（Schuirmann 1987, Lakens 2017）。\n\n---\n\n## Score Summary\n\n| 维度 | 分数 |\n|------|------|\n| **Soundness** | 2.5 / 5 |\n| **Excitement** | 3.0 / 5 |\n| **Overall** | 3.0 / 5 (Findings) |\n| **Confidence** | 4 / 5 |\n| **Reproducibility** | 4 / 5 |\n\n---\n\n## 审稿人总结\n\n本文提出了一个简洁、直觉合理的框架，用于在无需验证集的条件下选择 detect-and-reweight 预训练的下权指数。方法设计思路清晰，消融结构合理。但三个 critical 问题制约了当前版本的接收：(1) \"indistinguishable\" 的核心 claim 基于错误的统计推断范式，(2) $\\alpha_{\\mathrm{eff}}$ 的理论动机与实际计算之间存在未讨论的逻辑 gap，(3) 实验仅覆盖单一模型/detector/数据源，外部效度不足以支撑 general-purpose method 的定位。建议将 (1) 的 claim 降级、(2) 加入讨论、(3) 至少增加一个 detector 和一个更大模型的多 seed 实验后重新提交。如果仅修正 (1)(2) 的表述但不扩展实验，可考虑 Findings 接收。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**审查侧重**: 方法严谨性 + 实验设计\n**评分标准**: ACL Rolling Review (ARR) 官方 review form\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**Confidence**: 4 / 5\n**一句话总结**: 方法直觉清晰、框架简洁，但核心 claim 的统计支撑存在方法论缺陷（用 failure-to-reject 代替 equivalence test），实验规模和 detector 覆盖不足以支撑论文的一般性主张。\n\n---\n\n## ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5 / 5 | Proposition 1 证明存在 gap（$r_i$ 是估计量非 ground truth，与理论动机脱节）；\"indistinguishable\" claim 的统计方法不当（§详见 N1）；effect size 极小（0.24%）且 downstream 无显著差异 |\n| Excitement | 3.0 / 5 | 问题重要且实际（web 数据污染加剧），minimum intervention 直觉好，但实验未能在下游任务或更大规模上展示实际价值 |\n| Reproducibility | 4 / 5 | 算法伪代码清晰、超参设置完整、3-seed 报告；但代码未提供 |\n| Datasets | 1 / 5 | 无新数据集 |\n| Software | 1 / 5 | 无代码发布 |\n\n---\n\n## Summary\n\n本文提出一种双约束自适应指数选择框架用于 detect-and-reweight 预训练：给定 per-sample 检测器分数 $q(x)$，对每个 batch 求解满足 $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$（质量下界）且 $\\mathrm{ESS}(b) \\geq n_{\\min}$（稳定性上界）的最小 $b$，称为 \"minimum intervention principle\"。在 Qwen3-0.6B continued pretraining（132M tokens FineWeb，40% 合成污染）上，方法与 grid-searched best 统计不可区分（PPL 17.651 vs 17.620，$p=0.30$），消融证实 detector 信号和 minimum intervention 都是必要的。\n\n## Strengths\n\n**S1.** 问题定义清晰且实际。Web 数据中合成内容比例持续增长，需要无需验证集和已知污染比例的自适应方法。论文清楚地将此问题形式化为受约束优化。\n\n**S2.** 双约束框架设计简洁。$\\alpha_{\\mathrm{eff}}$ 和 ESS 的对立单调性自然地定义了 feasible region，bisection 求解高效（$\\sim$44 FLOPs per batch）。\"最小干预\"直觉合理：borderline samples 仍有训练价值，过度下权适得其反。\n\n**S3.** 消融设计有层次。Random → ESS-only → Uniform → Adaptive 的四级层次有效分离了 detector 信号和 minimum intervention 两个因素。固定 $\\bar{b}^*$ 实验（PPL 17.693 ≈ uniform）进一步证明 per-batch adaptation 的必要性。\n\n**S4.** 超参敏感性分析全面。$\\tau$ sweep（0.50–0.95）、$n_{\\min}$ sweep、batch size sweep ($B \\in \\{4,8,16\\}$) 均有覆盖，$\\tau \\in [0.5, 0.8]$ 的宽 safe range 是实用性的重要证据。\n\n**S5.** Related Work 定位准确。与 Drayson et al. (2025) 的三点差异（per-model grid search → per-batch adaptive, SIR resampling → loss reweighting, strong detector → lightweight detector）表述清楚，positioning 不过度。\n\n**S6.** 历史问题已修正。此前版本错误声称 \"from random initialization\"（现为 \"continued pretraining from pretrained weights\"，Section 4）和 \"balanced real/synthetic test set\"（现为 \"containing only human-authored text\"，Section 4）。两个问题均已正确修正。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **\"Statistically indistinguishable\" claim 使用了错误的统计范式**\n- 具体位置：Abstract, Section 5.1, Section 6 (Conclusion)\n- 问题：论文核心 claim 是 adaptive $b^*$ \"statistically indistinguishable from grid-searched optimum\"，依据是 bootstrap $p = 0.30$。但 $p = 0.30$ 仅表示 **未能拒绝**差异为零的零假设，不等于证明等价。在 N=3（3 seeds）的极小样本下，统计功效（power）极低——即使真实差异为 0.5 PPL，也很可能得到 $p > 0.05$。要正式声称\"不可区分\"，需要 equivalence test（如 TOST, Two One-Sided Tests），预设实际等价边界 $\\delta$，并证明差异落在 $[-\\delta, +\\delta]$ 内。当前表述将 absence of evidence 当作 evidence of absence，这是统计推断的基本错误。\n- 为什么影响接收：这是论文第一贡献的核心支撑。如果 \"indistinguishable\" claim 不成立，论文的核心价值主张需要重新表述。\n- 建议修改方向：(1) 执行 TOST 等价检验，明确 $\\delta$（如 0.1 PPL）；(2) 若功效不足，将 claim 降级为 \"adaptive $b^*$ achieves comparable PPL to grid-best, with the gap not reaching significance at N=3\"；(3) 增加 seeds 数量至少到 5-10 以提高统计功效。\n\n**N2** [critical] **$\\alpha_{\\mathrm{eff}}$ 的理论动机与实际计算之间存在逻辑断层**\n- 具体位置：Section 3.2 (Eq. 2), Proposition 1 proof (Appendix A)\n- 问题：$\\alpha_{\\mathrm{eff}}$ 使用 $r_i = \\mathbf{1}[q_i \\leq 0.5]$ 作为样本是否为真实数据的 indicator。但理论动机来自 Wang et al. (2026)，其收敛速率定理基于 **真实的** real-data fraction $\\alpha$，不是检测器估计的 $\\hat{\\alpha}$。这个 gap 意味着：当检测器不完美时（AUC = 0.939，46.3% 样本在不确定区间 $[0.2, 0.8]$），$\\alpha_{\\mathrm{eff}}$ 可能系统性偏离真实 $\\alpha$，$\\tau$ 的保证不再成立。Proposition 1 的证明也依赖 $r_i$ 与 $\\ln(1-q_i)$ 的正协方差，但 $r_i$ 本身就是 $q_i$ 的阈值函数——两者不是独立信号，covariance 的正性是 tautological（高 $q$ 导致 $r_i = 0$，低 $q$ 导致 $r_i = 1$ 且高 $\\ln(1-q_i)$）。这意味着 $\\alpha_{\\mathrm{eff}}$ 增加并非因为\"权重转移到真实样本\"，而仅仅因为\"权重转移到检测器认为是真实的样本\"。\n- 为什么影响接收：Proposition 1 是方法框架的数学基础。如果 $\\alpha_{\\mathrm{eff}}$ 不是 true $\\alpha$ 的良好代理，quality constraint 的理论根基不稳。\n- 建议修改方向：(1) 明确讨论 $\\alpha_{\\mathrm{eff}}$ 是 estimated effective real proportion，不是 true real proportion；(2) 在已知 ground truth 的合成实验中，报告 $\\alpha_{\\mathrm{eff}}$ vs true $\\alpha$ 的 correlation；(3) 分析检测器精度如何影响 $\\alpha_{\\mathrm{eff}}$ 的保证。\n\n**N3** [critical] **实验外部效度严重不足**\n- 具体位置：Section 4 (Experimental Setup), Section 8 (Limitations)\n- 问题：全部主实验在单一设定下完成：\n  - **单一模型规模**：0.6B。Limitations 提到 Llama-3.2-3B 迁移实验（单 seed）显示 PPL 和 HellaSwag 与 uniform 持平，MMLU +1.6pp 但需要 multi-seed。这不构成 scaling 证据。\n  - **单一数据源**：FineWeb。真实 web 数据的领域分布、噪声模式可能截然不同。\n  - **单一 detector**：TF-IDF + LR。论文声称 \"score calibration may matter as much as raw classification accuracy\"（Abstract, Section 4），但未用任何其他检测器验证。这个 claim 完全无实验支撑。\n  - **自污染设计**：用 Qwen3-0.6B 生成合成数据，再用同架构训练。真实场景中生成器通常是更大/不同模型（GPT-4, Claude 等），检测难度和分布特征完全不同。\n  - **$\\rho = 0.2$ 失效**：Limitations 报告 $\\rho = 0.2$ 方法反而伤害 PPL（+0.046），但无深入分析。$\\rho > 0.6$ 未测试。\n- 为什么影响接收：论文 framing 为 general-purpose contamination-aware pretraining method，但实验证据只覆盖一个极窄的 setting。EMNLP/ARR 审稿人会要求至少 2 个模型规模 + 2 个 detector 的交叉验证。\n- 建议修改方向：(1) 至少增加一个 neural detector（如 ModernBERT）的对比实验，直接验证 calibration hypothesis；(2) 增加至少一个 1B+ 规模的 3-seed 实验；(3) 分析 $\\rho = 0.2$ 失效的原因（可能是 $\\tau = 0.8$ 在低污染时已是 over-constraint）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Downstream benchmarks 未能展示实际价值**\n- 具体位置：Appendix E (Table 8)\n- 问题：5 个 downstream benchmarks（ARC-Challenge, ARC-Easy, HellaSwag, PIQA, WinoGrande）全部在标准误差内，且 4/5 个 adaptive 略微 **低于** uniform。论文说 \"preserves downstream performance\"，但审稿人会问：如果 PPL 改善不能转化为任何可测量的下游改善，这个方法的实际价值是什么？\n- 建议：(1) 增加更多种类的 benchmarks（如 MMLU, GSM8K），尤其是对数据质量敏感的任务；(2) 在更大模型上验证 PPL 改善是否放大为下游差异；(3) 至少用多 seed 做下游评估。\n\n**W2** [warning] **Proposition 1 声称 strictly increasing 但证明只建立 non-decreasing**\n- 具体位置：Section 3.2, Proposition 1 statement vs proof\n- 问题：命题声称 \"$\\alpha_{\\mathrm{eff}}(b)$ is strictly increasing in $b$\"。证明得到 $d\\alpha_{\\mathrm{eff}}/db = \\mathrm{Cov}_\\pi(r_i, \\ln(1-q_i))$，然后说 \"this covariance is non-negative\"。Non-negative 只能推出 non-decreasing，不是 strictly increasing。命题前提 \"containing both real and synthetic samples with distinct $q$-values\" 旨在排除退化情况，但证明中没有严格论证在此前提下 covariance 严格为正。需要论证 $r_i$ 和 $\\ln(1-q_i)$ 不是 $\\pi$-a.s. 常数。\n- 建议：严格化证明，或将命题降级为 non-decreasing，并注明在 non-degenerate 条件下严格成立。\n\n**W3** [warning] **ESS monotonicity 未证明**\n- 具体位置：Section 3.2, line 57\n- 问题：\"$\\mathrm{ESS}(b)$ is monotonically decreasing in $b$: larger exponents concentrate the weight distribution, a standard property of exponential tilting (Kimura et al., 2024).\"。但 Kimura et al. (2024) 是一篇 importance weighting 综述，不一定包含这个具体结论。ESS 的 monotonicity 对 bisection 算法的正确性至关重要——如果 ESS 非单调，$b_{\\mathrm{ESS}}$ 可能不唯一，bisection 会失败。这个性质应该被正式证明或给出精确引用。\n- 建议：在 Appendix 中加入 ESS 单调性的简短证明，至少对 $(1-q)^b$ 形式的 weights。\n\n**W4** [warning] **Grid-$b$ baseline 存在 post-hoc oracle 问题但论文未充分讨论**\n- 具体位置：Section 4 (Methods), Table 1 caption\n- 问题：Grid-$b$ 的 best 是 post-hoc 在测试集上选择的（\"best selected post-hoc by held-out PPL\"），这给了 grid search 一个 oracle 优势。论文确实在 Table 1 caption 中标注了 $^\\ddagger$Post-hoc oracle，但核心 claim \"indistinguishable from grid-searched optimum\" 是拿 adaptive 和 post-hoc oracle 比。在实践中，grid search 需要一个独立的 validation set 来选择 $b$，选出的 $b$ 在 test set 上通常略差于 post-hoc best。因此，adaptive 方法在公平比较中可能实际上优于真正的 grid search（用 val set 选 $b$，在 test set 上评估）。\n- 建议：增加一个 split-validation grid search baseline（用 val set 选 $b$，用 test set 评估），以提供更公平的比较。\n\n**W5** [warning] **Detect & Remove 和 Golden Ratio 仅单 seed**\n- 具体位置：Table 1\n- 问题：两个重要 baseline 只报告了 seed 42 的结果。Detect & Remove（17.290）显著优于所有 reweighting 方法，但没有多 seed 验证。在论文的核心叙事中，Detect & Remove 的优势被归因于 \"distribution match\"，但如果这个结果在多 seed 下不稳定，论文的 framing 需要调整。\n- 建议：至少用 3 seeds 复现 Detect & Remove 和 Golden Ratio。\n\n**W6** [warning] **效应量在实际意义上是否足够大？**\n- 具体位置：Section 5.4, Limitations (Effect size)\n- 问题：主要改善 0.043 PPL（0.24% relative）。论文自己也承认 \"modest in absolute terms\"。在 0.6B 模型上，这个改善完全不可能在任何下游任务上被观测到（Appendix E 已证实）。论文的实际贡献缩小为：消除 grid search，同时不伤害性能。但这个 framing 与论文标题和 Abstract 的主张（\"contamination-aware pretraining\"）有 mismatch——读者预期一个能显著改善训练质量的方法，而不仅仅是一个省去 grid search 的方法。\n- 建议：调整 framing，将核心卖点从 \"improved pretraining\" 转为 \"matching grid-search at zero validation cost\"。这更诚实，且仍有实际价值。\n\n---\n\n## Questions for Authors\n\n**Q1.** $\\alpha_{\\mathrm{eff}}$ 使用阈值 $q_i \\leq 0.5$ 判断真实/合成（Section 3.2, Eq. 2），这与 hard filtering 的 $q > 0.5$ 阈值相同。如果将 $r_i$ 改为 soft indicator $r_i = 1 - q_i$，性能如何变化？这会消除 0.5 阈值的硬依赖。\n\n**Q2.** $\\rho = 0.2$ 时方法反而伤害 PPL（+0.046，Limitations），但 $\\tau = 0.8$ 在低污染下可能要求过高的 $b$。是否测试过 $\\tau = 0.5$ 或 $\\tau = 0.6$ 在 $\\rho = 0.2$ 时的表现？\n\n**Q3.** Section 5.4 提到 \"unweighted training loss curves overlap (~1.4% difference)\"。如果训练 loss 几乎不变，PPL 改善从何而来？是否因为 evaluation set 是 human-only 而 training 的 reweighting 恰好对 human-like 分布做了隐式 importance weighting？如果 evaluation set 包含合成样本，PPL 差异是否消失？\n\n**Q4.** 论文使用 micro-batch size $B = 4$（Section 4），这意味着 ESS 的取值范围是 $[1, 4]$，$n_{\\min} = 2$ 将 ESS 下界设在总样本的 50%。在如此小的 batch 上，$\\alpha_{\\mathrm{eff}}$ 和 ESS 的估计方差必然很大。是否分析过 per-batch $b^*$ 的噪声对训练稳定性的影响？\n\n**Q5.** 论文声称 \"score calibration may matter as much as raw classification accuracy\"（Abstract），但只使用了一个 detector。要支撑这个 claim，至少需要一个 high-AUC 但 poorly-calibrated detector 和一个 lower-AUC 但 well-calibrated detector 的对比。是否有计划做这个实验？\n\n---\n\n## Missing References / 引用问题\n\n1. **`guo2025escaping`**（Guo et al., 2025）在线验证未找到匹配。bib 条目缺少 arXiv ID，venue 仅写 \"arXiv preprint\"，无法确认真实性。需要补充完整信息或确认这篇论文确实存在。\n\n2. **`vehtari2024psis`** 年份不一致：bib 写 2024，但 PSIS 原始版本为 2015（arXiv:1507.02646），JMLR 正式发表版可能为 2024。建议核实并使用正式发表年份。\n\n3. **Temperature scaling** 用于检测器校准（Section 4, \"calibrated ECE = 0.048 after temperature scaling with $T = 0.204$\"），但未引用 Guo et al. (2017) \"On Calibration of Modern Neural Networks\" 等温度校准的基础文献。\n\n4. **缺少 data contamination 检测的近期重要工作**：如 Hans et al. (2024) \"Spotting LLMs with Binoculars\" 等基于 likelihood ratio 的检测方法，可作为 detector 替代方案讨论。\n\n5. **缺少 equivalence testing / TOST 方法引用**：如果论文要声称 \"indistinguishable\"，应引用统计等价性检验文献（Schuirmann 1987, Lakens 2017）。\n\n---\n\n## Score Summary\n\n| 维度 | 分数 |\n|------|------|\n| **Soundness** | 2.5 / 5 |\n| **Excitement** | 3.0 / 5 |\n| **Overall** | 3.0 / 5 (Findings) |\n| **Confidence** | 4 / 5 |\n| **Reproducibility** | 4 / 5 |\n\n---\n\n## 审稿人总结\n\n本文提出了一个简洁、直觉合理的框架，用于在无需验证集的条件下选择 detect-and-reweight 预训练的下权指数。方法设计思路清晰，消融结构合理。但三个 critical 问题制约了当前版本的接收：(1) \"indistinguishable\" 的核心 claim 基于错误的统计推断范式，(2) $\\alpha_{\\mathrm{eff}}$ 的理论动机与实际计算之间存在未讨论的逻辑 gap，(3) 实验仅覆盖单一模型/detector/数据源，外部效度不足以支撑 general-purpose method 的定位。建议将 (1) 的 claim 降级、(2) 加入讨论、(3) 至少增加一个 detector 和一个更大模型的多 seed 实验后重新提交。如果仅修正 (1)(2) 的表述但不扩展实验，可考虑 Findings 接收。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-18T06:27:36.398424+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4118
}
```

</details>

---


### Assistant

_source line 56 · 2026-05-18T06:27:44.351869+00:00_

Round 1 审稿报告已提交给 Review Director。

核心发现：
- **3 个 Must-Fix**："indistinguishable" claim 基于错误的统计范式（failure-to-reject ≠ equivalence）；$\alpha_{\mathrm{eff}}$ 理论动机与实际计算之间的逻辑断层；实验外部效度严重不足（单一模型/detector/数据源）
- **6 个 Should-Fix**：downstream 无改善、Proposition 1 证明 gap、ESS 单调性未证明、grid-$b$ 的 post-hoc oracle 问题、重要 baseline 仅单 seed、效应量过小与 framing 不匹配
- **Overall 3.0 / 5**（Findings 水平），Soundness 2.5，Excitement 3.0
- 历史问题 RR-W1 和 RR-W2 均已修正

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 57 · 2026-05-18T06:31:28.211713+00:00_

[Round 1 审稿请求]:
## Round 1 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — Round 1 审稿报告

**Overall**: 3.0/5 (Findings)
**Soundness**: 3.0/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

**一句话总结**: 方法 formulation 干净、ablation 诚实，但实验规模（仅 0.6B/132M tokens）和效果量（~0.04 PPL）不足以支撑 EMNLP 长文；hard filtering 以显著优势碾压所有 reweighting 方法，削弱了实际动机。

### Must-Fix 问题

**N1** [critical] 实验规模不足以支撑长文贡献声明
- 全部主实验仅在 Qwen3-0.6B（单一模型规模）上进行，数据量 132M tokens。cross-model 实验（Llama-3.2-3B）仅 single seed。对于 EMNLP 长文，至少需要两个不同规模的模型 + 多 seed 复现。Drayson et al. (2025) 在 160M/360M/1.7B 三个规模上实验，本文声称改进了 Drayson 的方法却在实验覆盖上远不如它。

**N2** [critical] Hard filtering 碾压所有 reweighting 方法，削弱核心动机
- Detect & Remove（PPL 17.290）比 Adaptive（17.651）低 0.36 PPL。Appendix 显示即使 suboptimal threshold（$q > 0.3$: 17.253）也全面优于所有 reweighting。threshold 从 0.3 到 0.5 仅差 0.037 PPL，远小于 filtering vs. reweighting 的 0.36 差距——threshold 选择对 filtering 的敏感度远低于论文暗示的程度。

**N3** [critical] 效果量极小，downstream 无改善
- Adaptive vs. Uniform 的 PPL 改善仅 0.043（0.24% relative）。Appendix Table 5 显示所有 downstream benchmarks adaptive 均不优于 uniform（4/5 benchmarks 轻微 degradation）。

### Should-Fix 问题

**W1** [warning] 新颖性相对 Drayson et al. 的增量有限
- 核心公式直接来自 Drayson et al.。增量是选 $b$ 的方法。ESS 作为 IS 诊断是标准做法，"minimum intervention"本质是选 feasible region 最小值，数学上 trivial。

**W2** [warning] 仅模拟污染，无真实 web 数据验证
- synthetic contamination 通过自生成注入，是最容易检测的场景。

**W3** [warning] $\tau$ 实际需要根据 $\rho$ 调整，削弱"zero validation cost"声明
- optimal $\tau$ 从 0.8（$\rho=0.4$）变为 0.7（$\rho=0.6$），$\rho=0.2$ 时方法退化。Discussion 建议 "$\tau \approx 1 - \rho/2$" 但 $\rho$ 被假定未知。

**W4** [warning] 引用密度不足
- 仅 23 篇引用，EMNLP 长文通常 40-60+。缺失 curriculum learning, focal loss, DRO, watermarking, 更多检测器, DataComp 等。

**W5** [warning] Golden Ratio 和 Detect & Remove 仅 single seed

### Minor 问题

**M1** "five approaches" 实际列出 6 个方法。
**M2** Grid 值列表不一致（正文 7 个 vs Appendix 9 个）。
**M3** vehtari2024psis 年份可能有误，guo2025escaping 缺 arXiv ID。
**M4** AI 写作痕迹检查通过。
**M5** Hybrid 方法 $\rho=0.6$ 行数据可比性说明不清。

### Missing References
Bengio et al. (2009) Curriculum Learning, Kumar et al. (2010) Self-Paced Learning, Lin et al. (2017) Focal Loss, Sagawa et al. (2020) Group DRO, Kirchenbauer et al. (2023) Watermarking, Bao et al. (2024) Fast-DetectGPT, Hans et al. (2024) Binoculars, Gadre et al. (2024) DataComp-LM, Abbas et al. (2023) Semdedup, Tirumala et al. (2024) D4.

---

请对以上每条意见逐一给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-18T06:33:27.137153+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 实验规模不足以支撑长文贡献声明**\n\n同意。我在自己的 N3 中提出了高度一致的问题。补充两点：\n1. Drayson et al. (2025) 在 160M/360M/1.7B 三个规模上做了系统实验（Related Work, Section 2 对此有明确讨论），本文声称改进其方法却实验覆盖远不如它，这个对比会让审稿人印象很差。\n2. Limitations section 的 Llama-3.2-3B 单 seed 结果（\"PPL and HellaSwag parity with uniform, MMLU +1.6pp\"）实际上**更不利**——PPL parity 意味着方法在 3B 上没有改善，且单 seed 不能下结论。这比没有 3B 实验更糟，因为它暗示方法可能不 scale。\n\n**[AGREE with nuance] R2-N2: Hard filtering 碾压所有 reweighting 方法，削弱核心动机**\n\n基本同意 R2 的观察（0.36 PPL 差距确实显著），但认为 R2 对 threshold 敏感度的分析有遗漏：\n- R2 说 \"threshold 从 0.3 到 0.5 仅差 0.037 PPL，远小于 filtering vs. reweighting 的 0.36 差距\"。这是正确的，但**方向信息**是关键：0.3 比 0.5 更好（17.253 vs 17.290），但论文指出\"no principled way to choose the direction without validation data\"（Section 5.1）。在实践中，用错方向（选 0.7 而非 0.3）的 cost 可能远大于 0.037。论文没有测试更极端的阈值（如 0.1 或 0.9），所以 threshold robustness 的 full picture 缺失。\n- 然而，即使考虑此点，R2 的核心论点成立：Detect & Remove 在论文自己的实验中全面优于 reweighting，论文对此的解释（\"requires calibrated detection threshold\"）不够有力。如果 threshold 在 [0.3, 0.7] 全面优于 reweighting，那 \"threshold-free\" 的优势就不够 compelling。\n- 论文的 Discussion（Section 6）确实诚实地将 D&R、Hybrid、Adaptive 放在 spectrum 上，但 Introduction 和 Abstract 的 framing 没有充分反映 D&R 的优势。\n\n**[AGREE] R2-N3: 效果量极小，downstream 无改善**\n\n完全同意。我在 W1 和 W6 中详细讨论了这个问题。特别强调 Appendix Table 5 的 downstream 结果：4/5 benchmarks adaptive 略低于 uniform（ARC-Challenge -0.005, ARC-Easy -0.007, HellaSwag -0.005, WinoGrande -0.008），虽然在标准误差内，但方向一致性 suggests 即使有统计显著的 PPL 改善，它也不反映真正的训练质量提升——更可能是对 human-only evaluation set 的隐式 distribution matching（我的 Q3 直接问了这个问题）。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: 新颖性相对 Drayson et al. 的增量有限**\n\n不完全同意 R2 将贡献定性为 \"mathematically trivial\"。\n1. **ESS-only 失败的反直觉性**：如果 \"minimum intervention 本质是选 feasible region 最小值\" 是 trivial，那为什么直觉上合理的 \"选最大值\"（ESS-only）反而比 uniform 更差？Table 1 显示 ESS-only (17.737) 比 uniform (17.694) 差 0.043，和 adaptive 的改善幅度几乎对称。这说明 exponent 选择的方向（最小 vs 最大）有实质性影响，不是 trivial 的 design choice。\n2. **Regime analysis 提供了非平凡洞察**：Section 5.4 报告 $\\alpha_{\\mathrm{eff}}$-binding batches 中 dual-constrained $b^*$ 仅为 ESS-only 的 ~20%（median 0.80 vs 3.59），4.9× 的 over-intervention ratio 量化了 ESS-only 的失败原因。这种失败模式分析不是从 formulation 就能预见的。\n3. **但我同意数学深度确实有限**：Proposition 1 的证明是 straightforward 的 covariance 计算，bisection 是标准数值方法。novelty 更多在 problem formulation 和 empirical insight 层面，不在数学工具层面。\n\n综合判断：novelty 属于 \"useful engineering insight backed by careful ablation\"，足以支撑 Findings，但确实不够 exciting 支撑主会议长文。\n\n**[AGREE] R2-W2: 仅模拟污染，无真实 web 数据验证**\n\n同意。我在 N3 中也指出了这一点。自污染（用 Qwen3-0.6B 生成再用同架构训练）是最容易检测的场景——generator 和 trainee 共享分布，TF-IDF+LR 就能达到 AUC 0.939。真实场景中生成器通常是 GPT-4/Claude 等更大/不同模型，检测难度和分布特征完全不同。\n\n**[AGREE with nuance] R2-W3: $\\tau$ 需要根据 $\\rho$ 调整，削弱 \"zero validation cost\"**\n\n基本同意这个逻辑矛盾，但论文有部分 defense：\n- Section 5.3 的 $\\tau$ sweep 显示 $\\tau \\in [0.5, 0.8]$ 全部优于 uniform（Table 3），safe range 跨 0.3。这意味着默认 $\\tau = 0.8$ 不是唯一可行值，即使不调整也有效。\n- 但 R2 指出的矛盾是成立的：Discussion 建议 $\\tau \\approx 1 - \\rho/2$ 作为 heuristic，但 $\\rho$ 被假定未知（Section 3.1 的核心假设）。如果需要估计 $\\rho$ 来设 $\\tau$，那就引入了额外的依赖。论文应该明确说明 $\\tau = 0.8$ 作为 fixed default 在 $\\rho \\in [0.4, 0.6]$ 足够好，而不是暗示可以根据 $\\rho$ 微调。\n- $\\rho = 0.2$ 的失效（Limitations: +0.046 PPL）更严重：它表明方法有一个下界有效范围，但这个下界在实践中可能覆盖大部分真实场景（当前 web 污染估计 20-60%，Section 1）。\n\n**[AGREE] R2-W4: 引用密度不足**\n\n同意。23 篇引用对 EMNLP 长文偏少。R2 列出的缺失引用大部分确实相关：\n- **高度相关（应引用）**：Sagawa et al. (2020) Group DRO（和 DoReMi 关联密切）、Hans et al. (2024) Binoculars（检测器替代方案）、Gadre et al. (2024) DataComp-LM（数据质量基准）、Bao et al. (2024) Fast-DetectGPT\n- **相关但非必需**：Bengio et al. (2009) Curriculum Learning、Kumar et al. (2010) Self-Paced Learning（方法论关联较弱——这些是 difficulty-based ordering，不是 provenance-based reweighting）；Lin et al. (2017) Focal Loss（loss reweighting 的一般性引用，可以放但不是 gap）\n- **我额外建议**：温度校准文献 Guo et al. (2017) \"On Calibration of Modern Neural Networks\"（论文用了 temperature scaling 但未引用）\n\n**[AGREE] R2-W5: Golden Ratio 和 Detect & Remove 仅 single seed**\n\n同意，与我的 W5 一致。\n\n---\n\n### Minor 问题\n\n**[AGREE] R2-M1: \"five approaches\" 实际列出 6 个方法**\n\n确认。Section 4 Methods 段落说 \"We compare five approaches:\" 但列表包含 Uniform, Grid-$b$, ESS-only, Golden Ratio, Adaptive, Detect & Remove = 6 个。简单计数错误。\n\n**[AGREE] R2-M2: Grid 值列表不一致**\n\n确认。Section 4 列出 7 个值 $\\{0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$，但 Table 1 caption 说 \"nine candidates\"，Appendix Table 2 列出 9 个值（多了 0.1 和 0.2）。正文描述和附录数据不一致。\n\n**[AGREE] R2-M3: 引用格式问题**\n\n与我的 Missing References 发现一致。`vehtari2024psis` 年份可能是 JMLR 正式发表年份（2024）但原始版本 2015，需核实。`guo2025escaping` 在线验证完全找不到匹配，存在 phantom reference 风险。\n\n**[AGREE] R2-M4: AI 写作痕迹检查通过**\n\n同意。论文写作风格自然，未发现典型 AI 写作标志（过度 em-dash、-ing 结尾、过度分段等）。\n\n**[AGREE] R2-M5: Hybrid $\\rho=0.6$ 数据可比性说明不清**\n\n同意。Appendix Table 4 的脚注（\"$^*$Hybrid at $\\rho=0.6$ filters high-confidence synthetic ($q>0.95$), reducing effective $\\rho$ to $\\approx$0.4\"）说明这行数据与同列 $\\rho=0.6$ baselines 不直接可比，但这个说明容易被忽略。应该在正文中更明确地讨论。\n\n---\n\n### Missing References\n\nR2 列出的引用中，我同意以下为实质性遗漏：\n- Hans et al. (2024) Binoculars — 直接相关的检测器方法\n- Bao et al. (2024) Fast-DetectGPT — DetectGPT 的改进，论文已引 DetectGPT 但缺后续\n- Sagawa et al. (2020) Group DRO — DoReMi 的理论基础，论文引了 DoReMi 但缺其上游\n- Gadre et al. (2024) DataComp-LM — 数据选择/质量的重要基准\n\n以下为 nice-to-have 但非 gap：\n- Bengio et al. (2009) / Kumar et al. (2010) — difficulty-based，与 provenance-based 机制不同\n- Kirchenbauer et al. (2023) Watermarking — 提供 ground-truth provenance 但方法逻辑不同\n- Abbas et al. (2023) Semdedup / Tirumala et al. (2024) D4 — deduplication，不是 provenance reweighting\n\n---\n\n### 总结：两位 Reviewer 的共识与分歧\n\n**高度共识区域**（两位 Reviewer 独立指出）：\n1. 实验规模不足（单一模型/detector/数据源）— 两位均列为 critical\n2. 效果量小且 downstream 无改善 — 两位均列为 critical/warning\n3. Detect & Remove 优势明显 — R2 更强调，R1 同意\n4. Golden Ratio / D&R 单 seed 不足 — 两位一致\n5. 引用问题（guo2025escaping 可疑、vehtari 年份）— 两位一致\n\n**R1 独有的关注点**：\n- \"Indistinguishable\" claim 的统计范式错误（N1）— R2 未提及但这是核心方法论问题\n- $\\alpha_{\\mathrm{eff}}$ 理论动机与实际计算的逻辑断层（N2）— R2 未涉及\n- Proposition 1 严格递增 vs 非递减的证明 gap（W2）\n- ESS 单调性未证明（W3）\n\n**R2 独有但有效的关注点**：\n- Threshold 敏感度分析（N2 中的定量论证）— R1 关注但 R2 分析更锐利\n- 引用密度和缺失引用的系统性列举（W4）— R2 更全面\n- $\\tau$ 与 $\\rho$ 的依赖矛盾 \"zero validation cost\" claim（W3）— R1 在 Q2 问了但 R2 直接指出矛盾\n\n**分歧区域**：\n- **Novelty 判断**：R2 认为数学上 trivial，R1 认为 ESS-only 失败的反直觉性和 regime analysis 有非平凡价值。R1 倾向 Findings 可接收，R2 也给了 3.0 但 excitement 更低（2.5 vs 3.0）。\n\n**综合建议**：当前版本适合 Findings，不适合主会议。修改后重投需要至少解决实验规模和统计 claim 两个核心问题。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 实验规模不足以支撑长文贡献声明**\n\n同意。我在自己的 N3 中提出了高度一致的问题。补充两点：\n1. Drayson et al. (2025) 在 160M/360M/1.7B 三个规模上做了系统实验（Related Work, Section 2 对此有明确讨论），本文声称改进其方法却实验覆盖远不如它，这个对比会让审稿人印象很差。\n2. Limitations section 的 Llama-3.2-3B 单 seed 结果（\"PPL and HellaSwag parity with uniform, MMLU +1.6pp\"）实际上**更不利**——PPL parity 意味着方法在 3B 上没有改善，且单 seed 不能下结论。这比没有 3B 实验更糟，因为它暗示方法可能不 scale。\n\n**[AGREE with nuance] R2-N2: Hard filtering 碾压所有 reweighting 方法，削弱核心动机**\n\n基本同意 R2 的观察（0.36 PPL 差距确实显著），但认为 R2 对 threshold 敏感度的分析有遗漏：\n- R2 说 \"threshold 从 0.3 到 0.5 仅差 0.037 PPL，远小于 filtering vs. reweighting 的 0.36 差距\"。这是正确的，但**方向信息**是关键：0.3 比 0.5 更好（17.253 vs 17.290），但论文指出\"no principled way to choose the direction without validation data\"（Section 5.1）。在实践中，用错方向（选 0.7 而非 0.3）的 cost 可能远大于 0.037。论文没有测试更极端的阈值（如 0.1 或 0.9），所以 threshold robustness 的 full picture 缺失。\n- 然而，即使考虑此点，R2 的核心论点成立：Detect & Remove 在论文自己的实验中全面优于 reweighting，论文对此的解释（\"requires calibrated detection threshold\"）不够有力。如果 threshold 在 [0.3, 0.7] 全面优于 reweighting，那 \"threshold-free\" 的优势就不够 compelling。\n- 论文的 Discussion（Section 6）确实诚实地将 D&R、Hybrid、Adaptive 放在 spectrum 上，但 Introduction 和 Abstract 的 framing 没有充分反映 D&R 的优势。\n\n**[AGREE] R2-N3: 效果量极小，downstream 无改善**\n\n完全同意。我在 W1 和 W6 中详细讨论了这个问题。特别强调 Appendix Table 5 的 downstream 结果：4/5 benchmarks adaptive 略低于 uniform（ARC-Challenge -0.005, ARC-Easy -0.007, HellaSwag -0.005, WinoGrande -0.008），虽然在标准误差内，但方向一致性 suggests 即使有统计显著的 PPL 改善，它也不反映真正的训练质量提升——更可能是对 human-only evaluation set 的隐式 distribution matching（我的 Q3 直接问了这个问题）。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: 新颖性相对 Drayson et al. 的增量有限**\n\n不完全同意 R2 将贡献定性为 \"mathematically trivial\"。\n1. **ESS-only 失败的反直觉性**：如果 \"minimum intervention 本质是选 feasible region 最小值\" 是 trivial，那为什么直觉上合理的 \"选最大值\"（ESS-only）反而比 uniform 更差？Table 1 显示 ESS-only (17.737) 比 uniform (17.694) 差 0.043，和 adaptive 的改善幅度几乎对称。这说明 exponent 选择的方向（最小 vs 最大）有实质性影响，不是 trivial 的 design choice。\n2. **Regime analysis 提供了非平凡洞察**：Section 5.4 报告 $\\alpha_{\\mathrm{eff}}$-binding batches 中 dual-constrained $b^*$ 仅为 ESS-only 的 ~20%（median 0.80 vs 3.59），4.9× 的 over-intervention ratio 量化了 ESS-only 的失败原因。这种失败模式分析不是从 formulation 就能预见的。\n3. **但我同意数学深度确实有限**：Proposition 1 的证明是 straightforward 的 covariance 计算，bisection 是标准数值方法。novelty 更多在 problem formulation 和 empirical insight 层面，不在数学工具层面。\n\n综合判断：novelty 属于 \"useful engineering insight backed by careful ablation\"，足以支撑 Findings，但确实不够 exciting 支撑主会议长文。\n\n**[AGREE] R2-W2: 仅模拟污染，无真实 web 数据验证**\n\n同意。我在 N3 中也指出了这一点。自污染（用 Qwen3-0.6B 生成再用同架构训练）是最容易检测的场景——generator 和 trainee 共享分布，TF-IDF+LR 就能达到 AUC 0.939。真实场景中生成器通常是 GPT-4/Claude 等更大/不同模型，检测难度和分布特征完全不同。\n\n**[AGREE with nuance] R2-W3: $\\tau$ 需要根据 $\\rho$ 调整，削弱 \"zero validation cost\"**\n\n基本同意这个逻辑矛盾，但论文有部分 defense：\n- Section 5.3 的 $\\tau$ sweep 显示 $\\tau \\in [0.5, 0.8]$ 全部优于 uniform（Table 3），safe range 跨 0.3。这意味着默认 $\\tau = 0.8$ 不是唯一可行值，即使不调整也有效。\n- 但 R2 指出的矛盾是成立的：Discussion 建议 $\\tau \\approx 1 - \\rho/2$ 作为 heuristic，但 $\\rho$ 被假定未知（Section 3.1 的核心假设）。如果需要估计 $\\rho$ 来设 $\\tau$，那就引入了额外的依赖。论文应该明确说明 $\\tau = 0.8$ 作为 fixed default 在 $\\rho \\in [0.4, 0.6]$ 足够好，而不是暗示可以根据 $\\rho$ 微调。\n- $\\rho = 0.2$ 的失效（Limitations: +0.046 PPL）更严重：它表明方法有一个下界有效范围，但这个下界在实践中可能覆盖大部分真实场景（当前 web 污染估计 20-60%，Section 1）。\n\n**[AGREE] R2-W4: 引用密度不足**\n\n同意。23 篇引用对 EMNLP 长文偏少。R2 列出的缺失引用大部分确实相关：\n- **高度相关（应引用）**：Sagawa et al. (2020) Group DRO（和 DoReMi 关联密切）、Hans et al. (2024) Binoculars（检测器替代方案）、Gadre et al. (2024) DataComp-LM（数据质量基准）、Bao et al. (2024) Fast-DetectGPT\n- **相关但非必需**：Bengio et al. (2009) Curriculum Learning、Kumar et al. (2010) Self-Paced Learning（方法论关联较弱——这些是 difficulty-based ordering，不是 provenance-based reweighting）；Lin et al. (2017) Focal Loss（loss reweighting 的一般性引用，可以放但不是 gap）\n- **我额外建议**：温度校准文献 Guo et al. (2017) \"On Calibration of Modern Neural Networks\"（论文用了 temperature scaling 但未引用）\n\n**[AGREE] R2-W5: Golden Ratio 和 Detect & Remove 仅 single seed**\n\n同意，与我的 W5 一致。\n\n---\n\n### Minor 问题\n\n**[AGREE] R2-M1: \"five approaches\" 实际列出 6 个方法**\n\n确认。Section 4 Methods 段落说 \"We compare five approaches:\" 但列表包含 Uniform, Grid-$b$, ESS-only, Golden Ratio, Adaptive, Detect & Remove = 6 个。简单计数错误。\n\n**[AGREE] R2-M2: Grid 值列表不一致**\n\n确认。Section 4 列出 7 个值 $\\{0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$，但 Table 1 caption 说 \"nine candidates\"，Appendix Table 2 列出 9 个值（多了 0.1 和 0.2）。正文描述和附录数据不一致。\n\n**[AGREE] R2-M3: 引用格式问题**\n\n与我的 Missing References 发现一致。`vehtari2024psis` 年份可能是 JMLR 正式发表年份（2024）但原始版本 2015，需核实。`guo2025escaping` 在线验证完全找不到匹配，存在 phantom reference 风险。\n\n**[AGREE] R2-M4: AI 写作痕迹检查通过**\n\n同意。论文写作风格自然，未发现典型 AI 写作标志（过度 em-dash、-ing 结尾、过度分段等）。\n\n**[AGREE] R2-M5: Hybrid $\\rho=0.6$ 数据可比性说明不清**\n\n同意。Appendix Table 4 的脚注（\"$^*$Hybrid at $\\rho=0.6$ filters high-confidence synthetic ($q>0.95$), reducing effective $\\rho$ to $\\approx$0.4\"）说明这行数据与同列 $\\rho=0.6$ baselines 不直接可比，但这个说明容易被忽略。应该在正文中更明确地讨论。\n\n---\n\n### Missing References\n\nR2 列出的引用中，我同意以下为实质性遗漏：\n- Hans et al. (2024) Binoculars — 直接相关的检测器方法\n- Bao et al. (2024) Fast-DetectGPT — DetectGPT 的改进，论文已引 DetectGPT 但缺后续\n- Sagawa et al. (2020) Group DRO — DoReMi 的理论基础，论文引了 DoReMi 但缺其上游\n- Gadre et al. (2024) DataComp-LM — 数据选择/质量的重要基准\n\n以下为 nice-to-have 但非 gap：\n- Bengio et al. (2009) / Kumar et al. (2010) — difficulty-based，与 provenance-based 机制不同\n- Kirchenbauer et al. (2023) Watermarking — 提供 ground-truth provenance 但方法逻辑不同\n- Abbas et al. (2023) Semdedup / Tirumala et al. (2024) D4 — deduplication，不是 provenance reweighting\n\n---\n\n### 总结：两位 Reviewer 的共识与分歧\n\n**高度共识区域**（两位 Reviewer 独立指出）：\n1. 实验规模不足（单一模型/detector/数据源）— 两位均列为 critical\n2. 效果量小且 downstream 无改善 — 两位均列为 critical/warning\n3. Detect & Remove 优势明显 — R2 更强调，R1 同意\n4. Golden Ratio / D&R 单 seed 不足 — 两位一致\n5. 引用问题（guo2025escaping 可疑、vehtari 年份）— 两位一致\n\n**R1 独有的关注点**：\n- \"Indistinguishable\" claim 的统计范式错误（N1）— R2 未提及但这是核心方法论问题\n- $\\alpha_{\\mathrm{eff}}$ 理论动机与实际计算的逻辑断层（N2）— R2 未涉及\n- Proposition 1 严格递增 vs 非递减的证明 gap（W2）\n- ESS 单调性未证明（W3）\n\n**R2 独有但有效的关注点**：\n- Threshold 敏感度分析（N2 中的定量论证）— R1 关注但 R2 分析更锐利\n- 引用密度和缺失引用的系统性列举（W4）— R2 更全面\n- $\\tau$ 与 $\\rho$ 的依赖矛盾 \"zero validation cost\" claim（W3）— R1 在 Q2 问了但 R2 直接指出矛盾\n\n**分歧区域**：\n- **Novelty 判断**：R2 认为数学上 trivial，R1 认为 ESS-only 失败的反直觉性和 regime analysis 有非平凡价值。R1 倾向 Findings 可接收，R2 也给了 3.0 但 excitement 更低（2.5 vs 3.0）。\n\n**综合建议**：当前版本适合 Findings，不适合主会议。修改后重投需要至少解决实验规模和统计 claim 两个核心问题。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-18T06:33:31.155154+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Assistant

_source line 60 · 2026-05-18T06:33:44.328467+00:00_

交叉回应已提交给 Review Director。

对 R2 的 10 条意见（3 Must-Fix + 5 Should-Fix + 5 Minor），我的判断：
- **8 条 AGREE**（N1, N3, W2, W4, W5, M1-M5）
- **1 条 AGREE with nuance**（N2: 同意 filtering 优势明显，但补充了 threshold 方向不可知的 defense；W3: 同意 $\tau$-$\rho$ 矛盾，但指出 safe range 较宽）
- **1 条 REBUT**（W1: 不同意 novelty "trivial" 判断——ESS-only 失败是反直觉的，regime analysis 提供了非平凡洞察，但同意数学深度有限）

两位 Reviewer 在实验规模不足、效果量小、D&R 优势、引用问题上高度共识。R1 额外关注了统计推断范式错误和 $\alpha_{\mathrm{eff}}$ 理论 gap，R2 在 threshold 敏感度和引用密度上分析更深入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

52 recorded events


### User

_source line 61 · 2026-05-19T04:31:23.320716+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计/统计）

### 论文信息
- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`（sections 目录下 10 个 .tex 文件）
- **目标 venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL 模板 (`\usepackage[review]{acl}`)，长文正文 ≤ 8 页 + unlimited references，double-blind，Limitations section 必须（不计页数）

### 你的审查侧重

**A. 方法严谨性（重点）**
1. Dual-constraint framework (α_eff ≥ τ, ESS ≥ n_min) 的理论基础是否solid？
   - Proposition 1 (α_eff 单调性) 的证明是否完整、条件是否充分？
   - ESS 单调性证明（Appendix）是否严格？
   - α_eff 作为 true real fraction 的 proxy，其理论依据和实证验证（Appendix α_eff validation）是否充分？
   - Wang 2026 的收敛理论要求已知 α，但本文的 τ 是经验超参——这个理论断联是否被充分讨论？
2. "Minimum intervention principle" 是否有理论保证（为何选最小 b 而非其他 b）？
3. 超参数 τ=0.8 和 n_min=2 的选择是否有足够依据？声称"principled defaults"是否过强？
4. Bisection 算法在 b_max=20 下是否可能遗漏非单调区间？

**B. 实验设计与统计**
1. N=3 seeds 下的统计推断是否充分？95% CI [-0.039, 0.101] 是否支持所做的 claims？
2. Grid-b post-hoc oracle selection (best b=0.3 on test set) vs adaptive 的比较是否公平？
3. D&R epoch-matched 控制实验（Table 2）是否充分解决 multi-epoch confound？
4. 1.7B scale 验证仅单 seed，Δ=-0.01——是否支持"transfers without degradation"的 claim？
5. 下游 benchmark 4/5 略差——PPL 改善是否可能是 distribution matching artifact？
6. 自污染设定（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）的外部有效性？
7. ρ=0.2 时方法失效（+0.046 PPL）——"effective range ρ≥0.4"的限制是否被充分讨论？

**C. 可复现性**
1. 检测器训练细节（TF-IDF feature 设置、LR 超参、calibration 流程）是否足以复现？
2. 训练配置（lr schedule, warmup, gradient accumulation 等）是否完整？

请输出完整审稿报告，包含 Summary, Strengths, Weaknesses (分 Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-19T04:31:32.744894+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-19T04:31:32.745329+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-19T04:31:36.785809+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/provenance_weight_training/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/provenance_weight_training/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-19T04:31:36.786255+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-19T04:31:39.197164+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/provenance_weight_training/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/provenance_weight_training/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-19T04:31:39.247709+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-19T04:31:44.485801+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper tex files",
  "prompt": "Find all .tex and .bib files related to the paper \"Minimum Intervention Reweighting\" in the provenance_weight_training project. The paper is supposed to be at projects/provenance_weight_training/docs/paper/main.tex with sections in a sections directory. Search broadly - try multiple paths including /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/ and any other plausible locations. Report all found file paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find paper tex files",
    "prompt": "Find all .tex and .bib files related to the paper \"Minimum Intervention Reweighting\" in the provenance_weight_training project. The paper is supposed to be at projects/provenance_weight_training/docs/paper/main.tex with sections in a sections directory. Search broadly - try multiple paths including /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/ and any other plausible locations. Report all found file paths."
  }
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-19T04:31:46.144066+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-19T04:31:46.397324+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T102146/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T102146/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T102146/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work_963aec.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method_76a694.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments_1613c9.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results_819b43.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method_3f5a58.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments_86dfd1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/pap
…[truncated 3337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-19T04:31:46.449054+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-19T04:31:46.449451+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-19T04:31:48.357817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-19T04:31:48.408493+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\bibliography{references}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-19T04:31:56.339031+00:00_

Excellent! This confirms this is the correct paper. Now let me compile the complete list of all .tex and .bib files found:

## Summary of Found Files

### Main Paper Files
**Primary location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/`

**Main document:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`

**Section files (in sections/ subdirectory):**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex`

**Top-level section files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/introduction.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/related_work.tex`
- `/home/ubuntu/.agent-ml-resea
…[truncated 1557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 11853
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-19T04:31:59.601001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-19T04:31:59.651873+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\bibliography{references}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-19T04:32:02.565093+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-19T04:32:02.615709+00:00_

1	Web corpora now contain an estimated 20--60\% machine-generated text, and training on such contaminated data risks model collapse.
2	Detect-and-reweight methods suppress likely-synthetic samples via $w(x) = (1-q(x))^b$, but the exponent $b$ critically determines outcomes and requires per-model grid search (typically multiple complete training runs) to tune.
3	
4	We propose a dual-constrained adaptive exponent $b^*$ derived per-batch from detector scores alone: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling).
5	This minimum intervention principle applies only as much downweighting as needed, with zero validation cost.
6	
7	On Qwen3-0.6B continued pretraining (132M FineWeb tokens, 40\% synthetic contamination), adaptive $b^*$ achieves PPL competitive with the grid-searched optimum (3-seed means: 17.651 vs.\ 17.620, 95\% CI of gap $[-0.039, 0.101]$) while reducing the search cost from nine training runs to one.
8	A complete ablation confirms that both detector signal and minimum intervention are necessary: random reweighting degrades performance (17.803), ESS-only maximum intervention provides no improvement (17.737 vs.\ uniform 17.694), and only the dual-constrained method improves.
9	The advantage extends to $\rho{=}0.6$ (3-seed $\Delta{=}{-}0.027$, $p{<}0.01$) and transfers to 1.7B parameters without degradation ($\Delta{=}{-}0.01$).
10	An epoch-matched control (3 seeds) shows that hard filtering (Detect \& Remove) achieves equivalent PPL to adaptive $b^*$ when content epochs are equalized ($\Delta{=}0.006$, within seed variance); D\&R's apparent advantage at full training length is entirely attributable to multi-epoch exposure on the filtered subset.
11	The quality threshold $\tau$ is robust across $[0.5, 0.8]$, and detector type matters more than AUC: a discriminative detector (TF-IDF+LR, AUC\,=\,0.94) produces consistent gai
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-19T04:32:03.017732+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-19T04:32:03.470326+00:00_

1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation (\emph{model collapse}), and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.
6	
7	A natural response is \emph{detect-and-reweight}: suppress likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a classifier's synthetic probability estimate.
8	However, the exponent $b$ critically determines outcomes and requires per-model validation-set grid search~\citep{drayson2025detection}; alternative approaches require the exact contamination ratio~\citep{he2025golden} or a well-calibrated detection threshold for hard filtering~\citep{feng2025beyond}.
9	
10	Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
11	We formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\aeff(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $\nmin$.
12	The quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effec
…[truncated 3151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-19T04:32:03.521061+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-19T04:32:03.973523+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
6	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
7	
8	\paragraph{Detection and Filtering of Machine-Generated Text.}
9	Given the severity of contamination, a natural response is to detect and remove synthetic content.
10	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens.
11	All produce continuous confidence scores suitable as input to downstream weighting, including ours.
12	\citet{kirchenbauer2023watermark} propose watermarking as a complementary provenance mechanism.
13	On the mitigation side, \citet{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
14	Hard filter
…[truncated 4428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-19T04:32:03.974158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-19T04:32:04.427348+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	The indicator $r_i = \mathbf{1}[q_i \leq 0.5]$ is a proxy for true provenance: $\alpha_{\mathrm{eff}}$ tracks the detector's estimate of the real fraction, not
…[truncated 9052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-19T04:32:04.427722+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-19T04:32:05.381621+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.939, calibrated ECE\,=\,0.048 after temperature scaling with $T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.913) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
14	All main comparisons use three random seeds (42, 123, 456).
15	
16	\paragraph{Evaluation.}
17	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M toke
…[truncated 1412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-19T04:32:05.432381+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-19T04:32:05.834369+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves PPL competitive with grid-best: 3-seed means 17.651 vs.\ 17.620 for grid $b{=}0.3$ (gap 0.031, 95\% CI $[-0.039, 0.101]$).
8	With only $N{=}3$ seeds, this interval is too wide for formal equivalence testing; we refrain from claiming statistical indistinguishability and instead emphasize the practical value: the adaptive method requires one training run instead of nine~\citep{drayson2025detection}, with lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
9	Using the mean of per-batch $\bstar$ ($\bar{b}^*{=}1.19$) as a fixed exponent yields PPL 17.693, comparable to uniform (17.694); per-batch adaptation is essential.
10	
11	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
12	Random weights $\mathcal{U}(0,2)$ (mean 17.803) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
13	ESS-only (mean $17.737 {\pm} 0.021$) uses $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
14	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves over uniform (paired gap $0.086$, $p{<}0.01$, $N{=}3$).
15	Figure~\ref{fig:grid_b_trend} contextualizes this: the grid curve has a broad plateau at $b \in [0.1, 0.5]$ (PPL 17.620--17.655), and adaptive $\bstar$ (mean 17.651) f
…[truncated 8264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-19T04:32:05.834832+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-19T04:32:06.302365+00:00_

1	\paragraph{Why minimum intervention works.}
2	Restraint in downweighting outperforms aggressiveness.
3	In the 38.2\% of batches where $\aeff$ determines $\bstar$, the selected exponent is 4.9$\times$ lower than the ESS-only upper bound (\S\ref{sec:regime}), preventing unnecessary suppression of borderline samples ($q \approx 0.4$--$0.6$); this rate is robust across contamination levels (33.4\% at $\rho{=}0.6$) and seeds (CV ${<}2\%$).
4	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.70$ with a conservative bias of $-0.03$ (Appendix~\ref{app:alpha_validation}).
5	
6	\paragraph{Where the advantage manifests.}
7	The advantage appears entirely at evaluation (PPL 17.65 vs.\ 17.69); training loss curves overlap (${\sim}1.4\%$ difference), consistent with reshaping the effective distribution.
8	Downstream benchmarks show 4 of 5 tasks with small negative $\Delta$ ($p \approx 0.19$, Appendix~\ref{app:downstream}); the aggregate mean $\bstar \approx 1.4$ as a fixed exponent yields PPL no better than uniform (17.693 vs.\ 17.694), confirming that per-batch adaptation is essential.
9	
10	\paragraph{$\tau$ as a practical dial.}
11	$\tau \in [0.5, 0.8]$ all outperform uniform (Table~\ref{tab:tau}); sensitivity is asymmetric (over-cleaning degrades sharply, under-cleaning is mild), and $\tau \in [0.7, 0.8]$ is robust across $\rho \in \{0.4, 0.6\}$ (Appendix~\ref{app:tau_rho}).
12	
13	\paragraph{Detector signal semantics.}
14	The method requires a discriminative detector: both generative alternatives (GPT-2 PPL at AUC\,=\,0.91, $\Delta{=}{+}0.10$; N-gram PPL at AUC\,=\,0.73, $\Delta{=}{+}0.13$) reverse the advantage despite GPT-2's high AUC, because they conflate predictability with synthetic origin and assign high $q$-scores to fluent human text.
15	TF-IDF+LR (AUC\,=\,0.94, ECE\,=\,0.048) succeeds because its features target provenance rather than fluency.
16	
17	\paragraph{Filtering vs.\ reweighting.}
18	The 3-seed epoch-matched experiment (\S
…[truncated 761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 467
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-19T04:32:06.326049+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-19T04:32:06.778812+00:00_

1	We introduced Minimum Intervention Reweighting, a dual-constraint framework that derives per-batch $\bstar$ from detector scores alone ($\aeff(b) \geq \tau$, $\mathrm{ESS}(b) \geq \nmin$), reducing grid search from nine runs to one while achieving comparable PPL (3-seed gap 95\% CI $[-0.039, 0.101]$).
2	The ablation confirms both detector signal and minimum intervention are necessary ($\rho{=}0.4$); the advantage persists at $\rho{=}0.6$ ($\Delta{=}{-}0.027$, $p{<}0.01$).
3	A 3-seed epoch-matched control shows D\&R's apparent advantage is entirely due to multi-epoch exposure ($\Delta{=}0.006$); the method transfers to 1.7B without degradation ($\Delta{=}{-}0.01$).
4	Future work: multi-seed scale confirmation, discriminative detector characterization across architectures, and naturally contaminated corpora.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-19T04:32:06.779253+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-19T04:32:07.231382+00:00_

1	\paragraph{Scale and cross-model transfer.}
2	All main experiments use Qwen3-0.6B with batch size 4.
3	A 1.7B verification (Qwen3-1.7B, $\rho{=}0.4$) under matched conditions shows $\Delta{=}{-}0.01$ (adaptive 13.26 vs.\ uniform 13.26), confirming that the method transfers without degradation but does not demonstrate a clear advantage at this scale; multi-seed replication is needed.
4	Cross-model transfer (Llama-3.2-3B, single seed) shows parity with uniform on PPL and HellaSwag, with a $+$1.6\,pp MMLU advantage that requires replication.
5	
6	\paragraph{Contamination range.}
7	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative), indicating an effective range of $\rho \geq 0.4$ with $\tau{=}0.8$.
8	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
9	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
10	
11	\paragraph{Detector coverage.}
12	Three detectors have been tested: TF-IDF+LR (discriminative, AUC\,=\,0.94) succeeds, while GPT-2 perplexity (generative, AUC\,=\,0.91) and N-gram perplexity (generative, AUC\,=\,0.73) both fail.
13	The pattern suggests discriminative signal is necessary, but three detectors from two families cannot distinguish a type effect from a calibration effect; testing additional discriminative detectors at varying AUC levels would isolate the mechanism.
14	
15	\paragraph{Threshold.}
16	$\tau$ is an empirical hyperparameter.
17	The convergence theory of \citet{wang2026survive} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
18	
19	\paragraph{Evaluation.}
20	Main results report held-out perplexity.
21	Downstream benchmarks (Appendix~\ref{app:downstream}) show 4 of 5 tasks with small negative $\Delta$ (uniform slightly 
…[truncated 863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-19T04:32:07.231879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-19T04:32:07.736691+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
5	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
6	Then
7	\begin{equation*}
8	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
9	\end{equation*}
10	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
11	Taking the derivative with respect to $b$:
12	\begin{align*}
13	  \frac{d\pi_i}{db}
14	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right)
15	  = \pi_i \!\left(\ln(1{-}q_i) - \sum_j \pi_j \ln(1{-}q_j)\right).
16	\end{align*}
17	Substituting,
18	\begin{align*}
19	  \frac{d\alpha_{\mathrm{eff}}}{db}
20	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
21	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
22	\end{align*}
23	For any detector with better-than-random discrimination, real samples ($r_i = 1$) have $q_i \leq 0.5$ on average, and thus higher $\ln(1{-}q_i)$ than synthetic samples.
24	The weighted covariance $\mathrm{Cov}_{\pi}(r_i, \ln(1{-}q_i))$ is therefore non-negative, establishing that $\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$.
25	\end{proof}
26	
27	\begin{proposition}[ESS monotonicity]
28	\label{prop:ess_mono}
29	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
30	\end{proposition}
31	
32	\begin{proof}
33	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
34	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
35	Differentiating $H$ with respect to $b$:
36	\begin{equation*}
37	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
38	\end{equation*}
39	This equals $2\,\mathrm{Var}_{\pi^2}[\ln(1{-}q)]$ under the $\pi^2$-weighted measure.
40	Since variance is non-negative and strictly positive when not all $\ln(1{-}q_i)$ coincide (i.e., when at least two $q$
…[truncated 12675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-19T04:32:07.737212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-19T04:32:08.692180+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@article{drayson2025detection,
5	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
6	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
7	  journal={arXiv preprint arXiv:2502.15654},
8	  year={2025}
9	}
10	
11	@article{he2025golden,
12	  title={Golden Ratio Weighting Prevents Model Collapse},
13	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
14	  journal={arXiv preprint arXiv:2502.18049},
15	  year={2025}
16	}
17	
18	@article{wang2026survive,
19	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
20	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
21	  journal={arXiv preprint arXiv:2602.16065},
22	  year={2026}
23	}
24	
25	@article{shumailov2024model,
26	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
27	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
28	  journal={Nature},
29	  volume={631},
30	  pages={755--759},
31	  year={2024}
32	}
33	
34	@inproceedings{dohmatob2025strong,
35	  title={Strong Model Collapse},
36	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
37	  booktitle={ICLR},
38	  year={2025}
39	}
40	
41	@article{vehtari2024psis,
42	  title={Pareto Smoothed Importance Sampling},
43	  author={Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, Jonah},
44	  journal={JMLR},
45	  year={2024}
46	}
47	
48	@inproceedings{sow2025dynamic,
49	  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
50	  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans-Arno and Liang, Yingbin},
51	  booktitle={ICLR},
52	  year={2025}
53	
…[truncated 9235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-19T04:32:08.692542+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 101 · 2026-05-19T04:32:09.144826+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 102 · 2026-05-19T04:32:18.380988+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the web search results, here's what I found about ACL Rolling Review 2026 reviewer guidelines:

## Reviewer Guidelines and Responsibilities

ARR developed detailed guidelines and suggestions for each step of the reviewing process, including a list of common problems in both reviews and NLP papers to watch out for.

## Review Form and Criteria

Some sections of these guidelines now have codes for (meta-)review issues (I1-I12) that can be reported by the authors during the response period. This suggests the review form includes specific issue codes that reviewers can use.

## Reviewer Incentives and Awards

Starting from May 2025, ACL introduced awards policy for reviewers & chairs, where area chairs or senior area chairs may nominate great reviewers. Nominees will receive more recognition during ACL conferences through public lists on conference websites, special 
…[truncated 710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9688
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-19T04:32:48.098962+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 39, \"total_citations\": 63, \"unique_cited_keys\": 39, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 29, \"online_not_found\": 5, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"drayson2025detection\", \"type\": \"article\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.15654\"}, {\"key\": \"he2025golden\", \"type\": \"article\", \"title\": \"Golden Ratio Weighting Prevents Model Collapse\", \"authors\": \"He, Hengzhi and Xu, Shirong and Cheng, Guang\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.18049\"}, {\"key\": \"wang2026survive\", \"type\": \"article\", \"title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive T...\", \"authors\": \"Wang, Kevin and Niu, Hongqian and Li, Didong\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.16065\"}, {\"key\": \"shumailov2024model\", \"type\": \"article\", \"title\": \"AI Models Collapse When Trained on Recursively Generated Data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2025strong\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"ICLR\"}, {\"key\": \"vehtari2024psis\", \"type\": \"article\", \"title\": \"Pareto Smoothed Importance Sampling\", \"authors\": \"Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, J...\", \"year\": \"2024\", \"venue
…[truncated 28599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 38954
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-19T04:32:54.682840+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete ACL ARR review form criteria/dimensions with their scoring scales. I need the exact dimensions reviewers are asked to score on (e.g., soundness, excitement, clarity, etc.), the scale for each dimension (e.g., 1-5), and any description of what each score level means. Also extract any guidance on what makes a good vs bad review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete ACL ARR review form criteria/dimensions with their scoring scales. I need the exact dimensions reviewers are asked to score on (e.g., soundness, excitement, clarity, etc.), the scale for each dimension (e.g., 1-5), and any description of what each score level means. Also extract any guidance on what makes a good vs bad review."
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-19T04:33:01.056278+00:00_

# ARR Review Form Criteria and Guidance

## Scoring Dimensions

Based on the guidelines, starting February 2025, ARR reviewers provide **three scores**:

1. **Soundness** - Technical quality and validity
2. **Excitement** - Personal interest/engagement with the work
3. **Overall Recommendation** - Composite assessment for venue suitability

The document does not specify numeric scales for these dimensions.

## Key Guidance on Scoring

**Soundness scores must align with review text.** The guidelines state: "If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

**Excitement is separate from soundness.** Work can be technically sound but personally uninteresting, and vice versa. Authors may find sound but unexciting contributions valuable due to impact potential.

**Overall assessment reflects multiple factors:** "soundness, excitement, and also other factors like novelty and impact."

## What Makes Strong Reviews

✓ **Specific, actionable feedback** - Name particular missing references, explain *how* formulations are problematic
✓ **Professional, neutral tone** - Treat authors as colleagues; avoid sarcasm
✓ **Awareness of common biases** - Avoid assumptions that surprising results, simple methods, or non-English work indicate weakness
✓ **Engagement with author responses** - Acknowledge rebuttals and adjust scores when concerns are addressed

## What to Avoid

✗ Vague criticisms ("unclear," "missing details")
✗ Requesting unnecessary experiments beyond core claims
✗ Assuming author identity affects judgment
✗ Using generative AI to draft reviews

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6373
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-19T04:33:04.421072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 soundness excitement overall score scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 soundness excitement overall score scale 1-5"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-19T04:33:11.687930+00:00_

Web search results for query: "ACL ARR review form 2025 2026 soundness excitement overall score scale 1-5"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Statistics","url":"https://stats.aclrollingreview.org/"}]

Based on the search results, I found detailed information about the ACL ARR review form for 2025-2026:

## Three Core Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness score assesses whether the paper is sufficiently sound and thorough. The scale includes: 5 = Excellent: "This study is one of the most thorough I have seen, given its type"; 4 = Strong: "This study provides sufficient support for all of its claims"; and 3 = Acceptable: "This study provides sufficient support for its main claims."

## Excitement Score

The excitement scale includes: 5 = Highly Exciting: "I would recommend this paper to others and/or attend its presentation in a conference"; and 4 = Exciting: "I would mention this paper to others and/or make an effort to attend its presentation in a conference." Excitement is subjective, and does not necessarily 
…[truncated 604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7266
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-19T04:33:15.301778+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scales (1-5 etc), and the exact meaning of each score level. I need every field in the review form including: soundness, excitement, overall assessment, confidence, and any other fields. Give me the exact text for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scales (1-5 etc), and the exact meaning of each score level. I need every field in the review form including: soundness, excitement, overall assessment, confidence, and any other fields. Give me the exact text for each score level."
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-19T04:33:21.927251+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others and/or attend."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment
- **5**: "Consider for Award" (top 2.5% papers)
- **4.5**: "Borderline Award"
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: substantial revisions needed."
- **1.5**: "Resubmit after next cycle: substantial revisions cannot be completed by next cycle."
- **1**: "Do not resubmit: paper must be fully redone."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6625
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-19T04:36:53.809939+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**Venue**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法直觉合理、实验设计有亮点（epoch-matched control），但核心 claim 的统计支撑不足，理论基础与经验选择之间存在未弥合的断联，且效果量极小、外部有效性受限。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主要 claim 有实验支撑但统计力度不足（N=3, wide CI）；理论与经验超参之间的断联被承认但未解决；Proposition 1 证明正确但表述误导 |\n| Excitement | 3/5 (Interesting) | 问题实际且相关，minimum intervention 视角有新意，但效果量过小（0.043 PPL）、适用范围窄（ρ≥0.4、仅 discriminative detectors），实际影响力有限 |\n| Confidence | 4/5 | 仔细阅读了全文、附录和证明，熟悉 importance weighting 和 LLM pretraining 文献 |\n\n---\n\n## Summary\n\n本文提出了一个双约束框架，从 batch 级别的检测器分数自动导出 reweighting exponent b*：通过 α_eff(b) ≥ τ（质量下限）和 ESS(b) ≥ n_min（稳定上限）两个约束的交集，选取满足条件的最小 b，称为 \"minimum intervention principle\"。在 Qwen3-0.6B 的 continued pretraining 上（132M FineWeb tokens, 40% 合成污染），adaptive b* 的 PPL 接近 grid search 最优值（17.651 vs 17.620），且 ablation 表明 detector signal 和 minimum intervention 缺一不可。Epoch-matched 实验显示 D&R 的表面优势完全来自 multi-epoch exposure。\n\n---\n\n## 主要优势\n\n1. **Epoch-matched control 实验设计精巧**（Table 2, Section 5.1）。通过控制 content epochs，将 D&R 的表面 PPL 优势（0.360）分解为 multi-epoch effect vs. filtering effect，结论清晰（Δ=0.006 within seed variance）。这一分析对领域有独立价值，即使方法本身不被采纳。\n\n2. **Ablation 层次清晰**（Table 1）。Random < ESS-only < Uniform < Adaptive 的层级在 ρ=0.4 和 ρ=0.6 两个水平上一致复现，令人信服地分离了 detector signal 和 minimum intervention 两个要素的贡献。\n\n3. **Detector signal type 发现有启发性**（Section 5.2, Table 7, Appendix D）。Discriminative vs. generative detector 的对比揭示了 AUC 并非唯一决定因素，generative detectors 因混淆 fluency 与 synthetic origin 而反转优势。这一发现有实用意义。\n\n4. **写作质量高**。论文结构清楚，叙事主线统一，Limitations section 坦诚地讨论了多数弱点。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心 claim 的统计支撑不足：N=3 下的推断力度**\n- 具体位置：Section 5.1, Table 1, Abstract\n- 问题：Adaptive vs Grid-best 的 95% CI 为 [-0.039, 0.101]，跨越零且包含 adaptive 更差的区间。论文诚实地承认 \"too wide for formal equivalence testing\"（Section 5.1 第2段），但 Abstract 仍称 \"achieves PPL competitive with the grid-searched optimum\"。在 paired comparison 中 N=3 的 statistical power 极低（对于 0.03 量级的 effect size，power 远低于 0.5）。Adaptive vs Uniform 的 Δ=0.043 虽 p<0.003，但绝对量级在 22.97→17.65 的 5.3-point drop 背景下极小（0.24% relative）。\n- 为什么影响接收：如果核心 claim（\"matches grid-searched optimum\"）在统计上无法确立，论文的主要贡献就从 \"achieves comparable quality\" 降级为 \"saves compute but quality unknown\"。\n- 建议修改方向：(a) 增加到 N≥5 seeds 以缩窄 CI；(b) 如果 seed 数无法增加，调整 claim 措辞，将 \"competitive\" 改为更谨慎的表述，明确说明 CI 包含 degradation；(c) 考虑 TOST equivalence test 并报告 smallest meaningful difference。\n\n**N2** [critical] **理论基础与经验超参之间的断联**\n- 具体位置：Section 3.2 (第66-67行), Section 3.5 (第127行), Limitations (第17行)\n- 问题：α_eff ≥ τ 的理论 motivation 来自 Wang 2026 的收敛理论（\"convergence rate improves with the effective real-data fraction\"），但 Wang 2026 假设已知精确污染比例 α，而本文的 τ 是一个需要在 [0.5, 0.95] 范围内搜索的经验超参。Section 3.5 称 \"principled defaults\"，但 τ=0.8 的选择完全基于 seed 42 的 sweep（Table 3）。这构成一个理论断联：\n  (a) 方法声称的理论 grounding 仅限于 \"α_eff 越大收敛越快\" 这一定性 insight，不提供 τ 的定量推导；\n  (b) \"principled defaults\" 这一措辞暗示比实际更强的理论保证。\n  (c) τ 的最优值随 ρ 变化（ρ=0.4 时 0.8，ρ=0.6 时 0.7，Figure 4），意味着 τ 本身也需要某种 per-setting tuning，削弱了 \"zero validation cost\" 的 claim。\n- 为什么影响接收：如果 τ 需要调优，方法的核心卖点（免去 grid search）就被削弱——从 9 次训练减少到 1 次，但代价是一个难以事先确定的超参。\n- 建议修改方向：(a) 将 \"principled defaults\" 改为 \"empirically robust defaults\"；(b) 承认 τ 的选择本质上替代了对 b 的搜索，并定量比较两者的搜索空间大小和敏感度；(c) 或者推导 τ 与 ρ 的理论关系（即使是近似的）。\n\n**N3** [critical] **1.7B 结果不支持 \"transfers without degradation\" 的 claim**\n- 具体位置：Section 5.2 (第94行), Abstract (第9行), Conclusion (第3行)\n- 问题：1.7B 验证仅单 seed，Δ=-0.01（adaptive 13.26 vs uniform 13.26），这个差异在报告精度内几乎为零。\"Transfers without degradation\" 是一个关于方法鲁棒性的正面 claim，但单 seed、Δ≈0 的结果同样支持 \"no effect at this scale\" 的解释。Abstract 称 \"transfers to 1.7B parameters without degradation\"，Conclusion 同样使用，但 Limitations 更谨慎地说 \"confirms generalization but not advantage amplification\"。\n- 为什么影响接收：Scale transfer 是 NLP 社区高度关注的问题。单 seed、无统计显著性的结果不应在 Abstract/Conclusion 中被表述为正面发现。\n- 建议修改方向：Abstract/Conclusion 中加入 \"single-seed\" qualifier，或增加 multi-seed 1.7B 验证。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **自污染设定的外部有效性**\n- 具体位置：Section 4 (第1-3行)\n- 问题：Qwen3-0.6B 生成 + Qwen3-0.6B 训练的自污染设定是一个特殊场景。现实中 web 污染来自多种不同（通常更强的）模型。当污染源与训练模型不同时：(a) 检测器的 AUC 可能变化；(b) 合成文本的 distribution 与模型自身输出不同，α_eff proxy 的有效性未验证。Limitations 中提到 Llama-3.2-3B 的 cross-model transfer 但数据仅在 Limitations 文本中（未见 table）。\n- 建议：增加至少一个 cross-generator 实验（如用 GPT-4/Llama 生成的合成数据），或将 Llama-3.2-3B 结果移入 appendix 并给出完整 table。\n\n**W2** [warning] **Downstream benchmarks 4/5 略差，distribution matching artifact 风险**\n- 具体位置：Appendix F (Table 6), Discussion (第7-8行)\n- 问题：5 个 downstream benchmarks 中 4 个 adaptive 略差于 uniform（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA +0.001。单 seed 下无法做统计检验，但方向性一致地偏负值。Discussion 承认 \"may partly reflect distribution matching\"，但 Abstract 和 Conclusion 完全未提及这一重要 caveat。\n- 为什么重要：PPL 改善可能仅反映 training distribution 向 human-only evaluation set 偏移（因 reweighting 提升了 real-data 权重），而非真正的模型能力提升。如果 downstream 任务系统性地更差，这是 distribution matching artifact 的证据。\n- 建议：在 Abstract 或 Conclusion 中加入一句 downstream caveat；增加 multi-seed downstream 评估。\n\n**W3** [warning] **ρ=0.2 失效的讨论不充分**\n- 具体位置：Limitations (第7行)\n- 问题：ρ=0.2 时 adaptive 比 uniform 差 +0.046 PPL（0.26% relative），方法失效。Limitations 用一行带过（\"effective range ρ≥0.4\"），但：\n  (a) 主文完全不提 ρ=0.2；\n  (b) 失效的机制未解释（ρ=0.2 时 α_eff(0) ≈ 0.8 已满足 τ=0.8，大部分 batch 直接 b*=0，那为什么 PPL 反而更差？是否因少数 contaminated batch 的过度干预？）；\n  (c) 实际 web 污染比例的分布未讨论——如果真实 ρ 可能低于 0.4，方法的适用性受限。\n- 建议：在 Section 5 或 Discussion 中分析 ρ=0.2 失效的机制；讨论何时应当使用 vs 不使用该方法。\n\n**W4** [warning] **Micro-batch 级别 b* 决策的合理性**\n- 具体位置：Section 3.3 (第86行), Section 3.5 (第138行)\n- 问题：b* 在 micro-batch（B=4）级别计算。B=4 时 α_eff 仅有 5 个离散值 {0, 0.25, 0.5, 0.75, 1.0}（Appendix E），MAE=0.114，这意味着 α_eff 对 true real fraction 的估计精度很粗糙。方法论上，为什么不在 effective batch（B=16, gradient accumulation 后）级别计算 b*？Section 3.5 警告 \"setting [n_min] relative to the effective batch silently forces b*=0\"，但这只是 n_min 设置的问题，不是不能在更大 batch 上计算。\n- 建议：解释 micro-batch vs effective-batch 的设计选择；报告在 B=16 上计算 b* 的对比实验。\n\n**W5** [warning] **Proposition 1 证明表述的误导性**\n- 具体位置：Section 3.2 Proof sketch (第52-57行), Appendix A (第1-25行)\n- 问题：Proof sketch 称 \"for any detector with better-than-random discrimination, real samples (r_i=1) have q_i ≤ 0.5 and thus higher ln(1-q_i)\"。但 r_i 的定义是 r_i = 1[q_i ≤ 0.5]（Section 3.2 第23行），所以 r_i=1 ⟹ q_i ≤ 0.5 是定义上的恒等式，不依赖于检测器质量。α_eff 的单调性对任意 q-score 分布成立，是一个关于 weighted proportion 的代数性质，不是关于检测质量的声明。\"Better-than-random discrimination\" 条件实际上是 α_eff 作为真实 real fraction proxy 有效性的前提（Appendix E 验证的内容），不是单调性成立的前提。这一混淆让读者误以为单调性依赖于检测器质量。\n- 建议：在 proof sketch 中明确 r_i = 1[q_i ≤ 0.5] 的定义蕴含了 Cov ≥ 0；将检测器质量条件移至 α_eff proxy 有效性的讨论中。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 脚注 $^\\S$ 说 D&R 用 q>0.3，但正文说 \"best threshold (q>0.3)\" 是 post-hoc 选出的（Section 5.1 第20行）。应标注为 oracle。\n- **M2**: Golden Ratio baseline 仅单 seed（Table 1 脚注 $^\\dagger$），与 3-seed 方法不对称。\n- **M3**: Appendix Table 4 (D&R threshold) 中 Retained% 和 Epochs 部分行是近似值（用 ~），部分是精确值，不一致。\n- **M4**: Llama-3.2-3B cross-model transfer 结果出现在 Limitations 文本中但无 table/appendix，无法 verify。\n- **M5**: References: `lin2017focal` venue 写 \"ICCV\" 但 Focal Loss 发表于 ICCV 2017 作为 article，bib 中 type 为 article 但 venue 为 ICCV，建议改为 inproceedings。`vehtari2024psis` year 与 OpenAlex 不一致（bib=2024 vs API=2015, JMLR 正式发表可能更晚）。\n- **M6**: 检测器训练细节不足（TF-IDF n-gram range、max features、LR regularization/solver 未报告），影响可复现性。Section 4 \"Detector\" 段仅给出 AUC 和 ECE，无法复现检测器本身。\n- **M7**: 无代码/数据公开承诺。\n\n---\n\n## Questions to Authors\n\n1. ρ=0.2 时 τ=0.8 使得大部分 batch 的 α_eff(0) ≈ 0.8（因污染比例低），此时 adaptive 方法大多返回 b*=0，理论上应退化为 uniform。为什么 PPL 反而比 uniform 差 +0.046？是否因为少数 contaminated batch 的 b* 过大导致了 negative transfer？能否提供 ρ=0.2 时的 b* 分布和 constraint regime 分解？\n\n2. 为什么选择在 micro-batch（B=4）而非 effective batch（B=16）级别计算 b*？是否有在更大 batch 上的 ablation？\n\n3. τ 的最优值随 ρ 变化（0.8 → 0.7）。如果预先不知道 ρ，如何确定 τ？是否可以从 batch-level 的 α_eff(0) 分布反推 ρ 的估计，再自适应选择 τ？\n\n4. Cross-model transfer (Llama-3.2-3B) 的完整结果（PPL、downstream、per-task breakdown）能否补充到 appendix？\n\n5. Hybrid method（Table 4, q>0.95 filtering + adaptive）显示 PPL 17.514，显著优于 pure adaptive 17.653，但仅在 appendix 提及。为什么不将 hybrid 作为推荐方法？\n\n---\n\n## Missing References\n\n- **Gururangan et al. (2020)** \"Don't Stop Pretraining: Adapt Pretraining Language Models to Domains and Tasks\" — continued pretraining 的经典工作，直接相关但未引用。\n- **Wettig et al. (2023)** \"Should You Mask 15% in Masked Language Modeling?\" — 关于 pretraining masking ratio 如何影响质量的分析，与本文的 intervention intensity 问题类似。\n- 缺少对 **PANDA** (Li et al. 2024, \"Purifying Large Language Models by Ensembling a Small Language Model\") 或类似 purification/decontamination 方法的讨论。\n\n---\n\n## Reproducibility Assessment\n\n**中等偏低**。训练配置（lr, schedule, optimizer, precision, batch size）基本完整。但以下细节缺失：\n- 检测器：TF-IDF feature 设置（n-gram range, max_features, sublinear_tf 等）、LR 超参（C, solver, max_iter）、calibration validation set 大小\n- 评估：sliding-window PPL 的实现细节（是否用 strided、overlap 处理）\n- 代码/数据未公开\n- Contamination injection：synthetic continuation 的 prompt format、decoding parameters（temperature, top-p 等）\n\n---\n\n## Overall Assessment\n\n本文解决了一个实际且重要的问题（如何在不知道污染比例的情况下选择 reweighting exponent），提出的双约束框架在概念上简洁优雅。Epoch-matched control 是实验设计上的亮点，对领域有独立贡献。\n\n然而，三个核心问题限制了论文的 acceptance case：\n1. **统计力度不足**：N=3 seeds 下核心 claim 的 CI 过宽，效果量极小（0.043 PPL, 0.24%）；\n2. **理论-经验断联**：\"principled\" 和 \"theoretical grounding\" 的措辞超出了实际的理论保证；\n3. **外部有效性受限**：仅验证 self-contamination + discriminative detector + ρ≥0.4 的组合，real-world applicability 未建立。\n\n如果增加 seeds、调整 claims 措辞、补充 cross-generator 实验，这将是一篇适合 Findings 的贡献。当前版本介于 Findings borderline 和 Findings 之间。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**Venue**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法直觉合理、实验设计有亮点（epoch-matched control），但核心 claim 的统计支撑不足，理论基础与经验选择之间存在未弥合的断联，且效果量极小、外部有效性受限。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主要 claim 有实验支撑但统计力度不足（N=3, wide CI）；理论与经验超参之间的断联被承认但未解决；Proposition 1 证明正确但表述误导 |\n| Excitement | 3/5 (Interesting) | 问题实际且相关，minimum intervention 视角有新意，但效果量过小（0.043 PPL）、适用范围窄（ρ≥0.4、仅 discriminative detectors），实际影响力有限 |\n| Confidence | 4/5 | 仔细阅读了全文、附录和证明，熟悉 importance weighting 和 LLM pretraining 文献 |\n\n---\n\n## Summary\n\n本文提出了一个双约束框架，从 batch 级别的检测器分数自动导出 reweighting exponent b*：通过 α_eff(b) ≥ τ（质量下限）和 ESS(b) ≥ n_min（稳定上限）两个约束的交集，选取满足条件的最小 b，称为 \"minimum intervention principle\"。在 Qwen3-0.6B 的 continued pretraining 上（132M FineWeb tokens, 40% 合成污染），adaptive b* 的 PPL 接近 grid search 最优值（17.651 vs 17.620），且 ablation 表明 detector signal 和 minimum intervention 缺一不可。Epoch-matched 实验显示 D&R 的表面优势完全来自 multi-epoch exposure。\n\n---\n\n## 主要优势\n\n1. **Epoch-matched control 实验设计精巧**（Table 2, Section 5.1）。通过控制 content epochs，将 D&R 的表面 PPL 优势（0.360）分解为 multi-epoch effect vs. filtering effect，结论清晰（Δ=0.006 within seed variance）。这一分析对领域有独立价值，即使方法本身不被采纳。\n\n2. **Ablation 层次清晰**（Table 1）。Random < ESS-only < Uniform < Adaptive 的层级在 ρ=0.4 和 ρ=0.6 两个水平上一致复现，令人信服地分离了 detector signal 和 minimum intervention 两个要素的贡献。\n\n3. **Detector signal type 发现有启发性**（Section 5.2, Table 7, Appendix D）。Discriminative vs. generative detector 的对比揭示了 AUC 并非唯一决定因素，generative detectors 因混淆 fluency 与 synthetic origin 而反转优势。这一发现有实用意义。\n\n4. **写作质量高**。论文结构清楚，叙事主线统一，Limitations section 坦诚地讨论了多数弱点。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心 claim 的统计支撑不足：N=3 下的推断力度**\n- 具体位置：Section 5.1, Table 1, Abstract\n- 问题：Adaptive vs Grid-best 的 95% CI 为 [-0.039, 0.101]，跨越零且包含 adaptive 更差的区间。论文诚实地承认 \"too wide for formal equivalence testing\"（Section 5.1 第2段），但 Abstract 仍称 \"achieves PPL competitive with the grid-searched optimum\"。在 paired comparison 中 N=3 的 statistical power 极低（对于 0.03 量级的 effect size，power 远低于 0.5）。Adaptive vs Uniform 的 Δ=0.043 虽 p<0.003，但绝对量级在 22.97→17.65 的 5.3-point drop 背景下极小（0.24% relative）。\n- 为什么影响接收：如果核心 claim（\"matches grid-searched optimum\"）在统计上无法确立，论文的主要贡献就从 \"achieves comparable quality\" 降级为 \"saves compute but quality unknown\"。\n- 建议修改方向：(a) 增加到 N≥5 seeds 以缩窄 CI；(b) 如果 seed 数无法增加，调整 claim 措辞，将 \"competitive\" 改为更谨慎的表述，明确说明 CI 包含 degradation；(c) 考虑 TOST equivalence test 并报告 smallest meaningful difference。\n\n**N2** [critical] **理论基础与经验超参之间的断联**\n- 具体位置：Section 3.2 (第66-67行), Section 3.5 (第127行), Limitations (第17行)\n- 问题：α_eff ≥ τ 的理论 motivation 来自 Wang 2026 的收敛理论（\"convergence rate improves with the effective real-data fraction\"），但 Wang 2026 假设已知精确污染比例 α，而本文的 τ 是一个需要在 [0.5, 0.95] 范围内搜索的经验超参。Section 3.5 称 \"principled defaults\"，但 τ=0.8 的选择完全基于 seed 42 的 sweep（Table 3）。这构成一个理论断联：\n  (a) 方法声称的理论 grounding 仅限于 \"α_eff 越大收敛越快\" 这一定性 insight，不提供 τ 的定量推导；\n  (b) \"principled defaults\" 这一措辞暗示比实际更强的理论保证。\n  (c) τ 的最优值随 ρ 变化（ρ=0.4 时 0.8，ρ=0.6 时 0.7，Figure 4），意味着 τ 本身也需要某种 per-setting tuning，削弱了 \"zero validation cost\" 的 claim。\n- 为什么影响接收：如果 τ 需要调优，方法的核心卖点（免去 grid search）就被削弱——从 9 次训练减少到 1 次，但代价是一个难以事先确定的超参。\n- 建议修改方向：(a) 将 \"principled defaults\" 改为 \"empirically robust defaults\"；(b) 承认 τ 的选择本质上替代了对 b 的搜索，并定量比较两者的搜索空间大小和敏感度；(c) 或者推导 τ 与 ρ 的理论关系（即使是近似的）。\n\n**N3** [critical] **1.7B 结果不支持 \"transfers without degradation\" 的 claim**\n- 具体位置：Section 5.2 (第94行), Abstract (第9行), Conclusion (第3行)\n- 问题：1.7B 验证仅单 seed，Δ=-0.01（adaptive 13.26 vs uniform 13.26），这个差异在报告精度内几乎为零。\"Transfers without degradation\" 是一个关于方法鲁棒性的正面 claim，但单 seed、Δ≈0 的结果同样支持 \"no effect at this scale\" 的解释。Abstract 称 \"transfers to 1.7B parameters without degradation\"，Conclusion 同样使用，但 Limitations 更谨慎地说 \"confirms generalization but not advantage amplification\"。\n- 为什么影响接收：Scale transfer 是 NLP 社区高度关注的问题。单 seed、无统计显著性的结果不应在 Abstract/Conclusion 中被表述为正面发现。\n- 建议修改方向：Abstract/Conclusion 中加入 \"single-seed\" qualifier，或增加 multi-seed 1.7B 验证。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **自污染设定的外部有效性**\n- 具体位置：Section 4 (第1-3行)\n- 问题：Qwen3-0.6B 生成 + Qwen3-0.6B 训练的自污染设定是一个特殊场景。现实中 web 污染来自多种不同（通常更强的）模型。当污染源与训练模型不同时：(a) 检测器的 AUC 可能变化；(b) 合成文本的 distribution 与模型自身输出不同，α_eff proxy 的有效性未验证。Limitations 中提到 Llama-3.2-3B 的 cross-model transfer 但数据仅在 Limitations 文本中（未见 table）。\n- 建议：增加至少一个 cross-generator 实验（如用 GPT-4/Llama 生成的合成数据），或将 Llama-3.2-3B 结果移入 appendix 并给出完整 table。\n\n**W2** [warning] **Downstream benchmarks 4/5 略差，distribution matching artifact 风险**\n- 具体位置：Appendix F (Table 6), Discussion (第7-8行)\n- 问题：5 个 downstream benchmarks 中 4 个 adaptive 略差于 uniform（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA +0.001。单 seed 下无法做统计检验，但方向性一致地偏负值。Discussion 承认 \"may partly reflect distribution matching\"，但 Abstract 和 Conclusion 完全未提及这一重要 caveat。\n- 为什么重要：PPL 改善可能仅反映 training distribution 向 human-only evaluation set 偏移（因 reweighting 提升了 real-data 权重），而非真正的模型能力提升。如果 downstream 任务系统性地更差，这是 distribution matching artifact 的证据。\n- 建议：在 Abstract 或 Conclusion 中加入一句 downstream caveat；增加 multi-seed downstream 评估。\n\n**W3** [warning] **ρ=0.2 失效的讨论不充分**\n- 具体位置：Limitations (第7行)\n- 问题：ρ=0.2 时 adaptive 比 uniform 差 +0.046 PPL（0.26% relative），方法失效。Limitations 用一行带过（\"effective range ρ≥0.4\"），但：\n  (a) 主文完全不提 ρ=0.2；\n  (b) 失效的机制未解释（ρ=0.2 时 α_eff(0) ≈ 0.8 已满足 τ=0.8，大部分 batch 直接 b*=0，那为什么 PPL 反而更差？是否因少数 contaminated batch 的过度干预？）；\n  (c) 实际 web 污染比例的分布未讨论——如果真实 ρ 可能低于 0.4，方法的适用性受限。\n- 建议：在 Section 5 或 Discussion 中分析 ρ=0.2 失效的机制；讨论何时应当使用 vs 不使用该方法。\n\n**W4** [warning] **Micro-batch 级别 b* 决策的合理性**\n- 具体位置：Section 3.3 (第86行), Section 3.5 (第138行)\n- 问题：b* 在 micro-batch（B=4）级别计算。B=4 时 α_eff 仅有 5 个离散值 {0, 0.25, 0.5, 0.75, 1.0}（Appendix E），MAE=0.114，这意味着 α_eff 对 true real fraction 的估计精度很粗糙。方法论上，为什么不在 effective batch（B=16, gradient accumulation 后）级别计算 b*？Section 3.5 警告 \"setting [n_min] relative to the effective batch silently forces b*=0\"，但这只是 n_min 设置的问题，不是不能在更大 batch 上计算。\n- 建议：解释 micro-batch vs effective-batch 的设计选择；报告在 B=16 上计算 b* 的对比实验。\n\n**W5** [warning] **Proposition 1 证明表述的误导性**\n- 具体位置：Section 3.2 Proof sketch (第52-57行), Appendix A (第1-25行)\n- 问题：Proof sketch 称 \"for any detector with better-than-random discrimination, real samples (r_i=1) have q_i ≤ 0.5 and thus higher ln(1-q_i)\"。但 r_i 的定义是 r_i = 1[q_i ≤ 0.5]（Section 3.2 第23行），所以 r_i=1 ⟹ q_i ≤ 0.5 是定义上的恒等式，不依赖于检测器质量。α_eff 的单调性对任意 q-score 分布成立，是一个关于 weighted proportion 的代数性质，不是关于检测质量的声明。\"Better-than-random discrimination\" 条件实际上是 α_eff 作为真实 real fraction proxy 有效性的前提（Appendix E 验证的内容），不是单调性成立的前提。这一混淆让读者误以为单调性依赖于检测器质量。\n- 建议：在 proof sketch 中明确 r_i = 1[q_i ≤ 0.5] 的定义蕴含了 Cov ≥ 0；将检测器质量条件移至 α_eff proxy 有效性的讨论中。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 脚注 $^\\S$ 说 D&R 用 q>0.3，但正文说 \"best threshold (q>0.3)\" 是 post-hoc 选出的（Section 5.1 第20行）。应标注为 oracle。\n- **M2**: Golden Ratio baseline 仅单 seed（Table 1 脚注 $^\\dagger$），与 3-seed 方法不对称。\n- **M3**: Appendix Table 4 (D&R threshold) 中 Retained% 和 Epochs 部分行是近似值（用 ~），部分是精确值，不一致。\n- **M4**: Llama-3.2-3B cross-model transfer 结果出现在 Limitations 文本中但无 table/appendix，无法 verify。\n- **M5**: References: `lin2017focal` venue 写 \"ICCV\" 但 Focal Loss 发表于 ICCV 2017 作为 article，bib 中 type 为 article 但 venue 为 ICCV，建议改为 inproceedings。`vehtari2024psis` year 与 OpenAlex 不一致（bib=2024 vs API=2015, JMLR 正式发表可能更晚）。\n- **M6**: 检测器训练细节不足（TF-IDF n-gram range、max features、LR regularization/solver 未报告），影响可复现性。Section 4 \"Detector\" 段仅给出 AUC 和 ECE，无法复现检测器本身。\n- **M7**: 无代码/数据公开承诺。\n\n---\n\n## Questions to Authors\n\n1. ρ=0.2 时 τ=0.8 使得大部分 batch 的 α_eff(0) ≈ 0.8（因污染比例低），此时 adaptive 方法大多返回 b*=0，理论上应退化为 uniform。为什么 PPL 反而比 uniform 差 +0.046？是否因为少数 contaminated batch 的 b* 过大导致了 negative transfer？能否提供 ρ=0.2 时的 b* 分布和 constraint regime 分解？\n\n2. 为什么选择在 micro-batch（B=4）而非 effective batch（B=16）级别计算 b*？是否有在更大 batch 上的 ablation？\n\n3. τ 的最优值随 ρ 变化（0.8 → 0.7）。如果预先不知道 ρ，如何确定 τ？是否可以从 batch-level 的 α_eff(0) 分布反推 ρ 的估计，再自适应选择 τ？\n\n4. Cross-model transfer (Llama-3.2-3B) 的完整结果（PPL、downstream、per-task breakdown）能否补充到 appendix？\n\n5. Hybrid method（Table 4, q>0.95 filtering + adaptive）显示 PPL 17.514，显著优于 pure adaptive 17.653，但仅在 appendix 提及。为什么不将 hybrid 作为推荐方法？\n\n---\n\n## Missing References\n\n- **Gururangan et al. (2020)** \"Don't Stop Pretraining: Adapt Pretraining Language Models to Domains and Tasks\" — continued pretraining 的经典工作，直接相关但未引用。\n- **Wettig et al. (2023)** \"Should You Mask 15% in Masked Language Modeling?\" — 关于 pretraining masking ratio 如何影响质量的分析，与本文的 intervention intensity 问题类似。\n- 缺少对 **PANDA** (Li et al. 2024, \"Purifying Large Language Models by Ensembling a Small Language Model\") 或类似 purification/decontamination 方法的讨论。\n\n---\n\n## Reproducibility Assessment\n\n**中等偏低**。训练配置（lr, schedule, optimizer, precision, batch size）基本完整。但以下细节缺失：\n- 检测器：TF-IDF feature 设置（n-gram range, max_features, sublinear_tf 等）、LR 超参（C, solver, max_iter）、calibration validation set 大小\n- 评估：sliding-window PPL 的实现细节（是否用 strided、overlap 处理）\n- 代码/数据未公开\n- Contamination injection：synthetic continuation 的 prompt format、decoding parameters（temperature, top-p 等）\n\n---\n\n## Overall Assessment\n\n本文解决了一个实际且重要的问题（如何在不知道污染比例的情况下选择 reweighting exponent），提出的双约束框架在概念上简洁优雅。Epoch-matched control 是实验设计上的亮点，对领域有独立贡献。\n\n然而，三个核心问题限制了论文的 acceptance case：\n1. **统计力度不足**：N=3 seeds 下核心 claim 的 CI 过宽，效果量极小（0.043 PPL, 0.24%）；\n2. **理论-经验断联**：\"principled\" 和 \"theoretical grounding\" 的措辞超出了实际的理论保证；\n3. **外部有效性受限**：仅验证 self-contamination + discriminative detector + ρ≥0.4 的组合，real-world applicability 未建立。\n\n如果增加 seeds、调整 claims 措辞、补充 cross-generator 实验，这将是一篇适合 Findings 的贡献。当前版本介于 Findings borderline 和 Findings 之间。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-19T04:36:57.834824+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4024
}
```

</details>

---


### Assistant

_source line 112 · 2026-05-19T04:37:07.612003+00:00_

审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**，Soundness 3/5，Excitement 3/5。

三个 Must-Fix 问题：
1. **统计支撑不足** — N=3 的 95% CI [-0.039, 0.101] 包含 degradation，无法确立 "competitive with grid-best" 的 claim
2. **理论-经验断联** — τ=0.8 是经验选择但被包装为 "principled default"；τ 最优值随 ρ 变化，削弱 "zero validation cost" 卖点
3. **1.7B 单 seed 结果不支持 "transfers without degradation"** — Δ=-0.01 同样可解读为 "no effect"

主要优势：epoch-matched control 实验设计精巧，ablation 层级清晰，detector type finding 有启发性。

如需要我对特定问题深入分析或进入交叉评审阶段，随时通知。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 113 · 2026-05-19T04:39:21.058555+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉评审：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每个 Must-Fix、Should-Fix 和关键判断，用 **[AGREE]** 或 **[REBUT]** 标注你的立场，并说明理由。如果你 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。

---

以下是 Reviewer 2 的完整审稿报告：

### Overall: 2.5/5（Findings/borderline reject）
Soundness 3.0/5, Excitement 2.0/5, Reproducibility 4.0/5, Confidence 4/5

### Must-Fix 问题

**R2-N1** [critical] 新颖性不足以支撑 EMNLP Main Conference
- 核心加权公式 w=(1-q)^b 完全来自 Drayson 2025
- Dual constraint 的两个组件（α_eff 加权平均 + ESS Kish 1965）均为标准工具
- "Minimum intervention principle" 是标准约束优化的 rebranding
- 增量贡献可概括为：对已有公式的自动超参数选择程序
- EMNLP Main 要求 "transformational value" 或显著方法论创新

**R2-N2** [critical] 实验规模与论文动机严重不匹配
- 论文动机聚焦 web-scale（数十B tokens），但主要实验仅 0.6B + 132M tokens
- 1.7B 单 seed，Δ=-0.01 无改善
- Llama-3.2-3B 仅在 Limitations 一笔带过
- EMNLP 2024-2025 data curation 论文通常至少 1B+ scale 有 3-seed 结果

**R2-N3** [critical] 效果量极小，且 downstream 无改善
- PPL 改善 0.043（0.24% relative）
- Downstream 4/5 任务 Adaptive 略差于 Uniform
- Grid-best CI [-0.039, 0.101] 包含零
- 如果改善本身不重要，省去 grid search 的价值也大打折扣

### Should-Fix 问题

**R2-W1** 人造 contamination 不代表真实场景（自污染 + 已知 ρ 均匀混入 vs 真实 multi-source unknown）
**R2-W2** Abstract 超长（~291 words > 250 建议上限），数据堆砌而非叙事
**R2-W3** 引用偏少（~39 条），遗漏 DCLM、QuRating、OLMo、LESS、Tale of Tails、Gerstgrasser 2024
**R2-W4** Discussion 过于单薄（仅 20 行，基本是 Results 重述）
**R2-W5** "Minimum Intervention Principle" framing 过度，标准约束优化不应命名为 "principle"
**R2-W6** ECE 缩写未定义

### 关键判断
- Reviewer 2 认为 Excitement 仅 2.0/5，核心理由是 "对已有公式的自动调参，novelty 更接近 Findings 水平"
- Reviewer 2 认为 epoch-matched control 和 detector signal type 发现有价值，但不足以弥补 novelty 不足

---

请对以上所有 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，重点关注你与 Reviewer 2 在 novelty 评估和 excitement 分数上是否一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-19T04:41:13.861410+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 交叉评审回应 Reviewer 2\n\n---\n\n### Must-Fix 逐条回应\n\n**[REBUT] R2-N1: 新颖性不足以支撑 EMNLP Main Conference**\n\nR2 将本文贡献简化为\"对已有公式的自动超参数选择程序\"，我认为这一概括过于粗暴，遗漏了三个有独立价值的贡献：\n\n1. **Dual-constraint formulation 不是 trivial 的组合**。α_eff 和 ESS 虽然分别是标准工具，但将两者的 opposing monotonicity 形式化为 feasible region [b_τ, b_ESS]，并利用 minimum vs maximum 的选择产生可测量的性能差异（Section 5.1 Table 1: Adaptive 17.651 vs ESS-only 17.737，paired gap 0.086, p<0.01），这一设计选择并非显而易见。R2 说\"标准约束优化的 rebranding\"，但 ESS-only ablation 的失败恰恰证明约束的选取和优化方向（min vs max）是方法成功的关键。\n\n2. **Epoch-matched control 的实验设计**（Table 2）解决了领域中 D&R vs reweighting 对比的一个系统性 confound，这一分析方法论贡献独立于方法本身。\n\n3. **Detector signal type 发现**（Appendix D, Table 7）揭示 AUC 不是决定因素（GPT-2 AUC=0.91 失败，TF-IDF AUC=0.94 成功），这对后续工作的 detector 选择有实用指导意义。\n\n但我同意 R2 的结论方向：**这些贡献更适合 Findings 而非 Main**。我给 Overall 3.0（Findings），R2 给 2.5（Borderline Findings），分歧在半档。核心方法确实是对已有 weighting scheme 的 hyperparameter automation，Excitement 不足以支撑 Main 是合理判断。\n\n我不同意的是 Excitement 2.0 的评分。Epoch-matched analysis 和 detector-type finding 对领域的实际指导价值使本文值得 \"Interesting\"（3.0），而非 \"Potentially Interesting\"（2.0）。\n\n---\n\n**[AGREE] R2-N2: 实验规模与论文动机严重不匹配**\n\n完全同意。论文 Introduction 以 \"web corpora now contain an estimated 20-60% machine-generated text\"（Section 1, 第1行）开篇，framing 是 web-scale 问题，但实验仅 0.6B model + 132M tokens，与 web-scale pretraining（通常 1T+ tokens）相差 4 个数量级。\n\n我在自己的审稿中将此归入 N3（1.7B 单 seed 不充分），但 R2 更准确地指出了 framing-experiment gap 这一更根本的问题。补充论据：\n\n- EMNLP/ACL 近期的 data curation 论文如 DataComp-LM（Gadre et al. 2024, 引用于本文）在 billions of tokens 上验证。DoReMi（Xie et al. 2023）同样在 GPT-scale 上验证。\n- 本文的 \"continued pretraining\" 设定（从 pretrained checkpoint 开始）部分缓解了这一问题，但 Introduction 的 framing 并未限定为 continued pretraining。\n\n建议：调整 Introduction framing 使之与实验规模匹配（聚焦 continued pretraining 场景），或增加更大规模实验。\n\n---\n\n**[AGREE] R2-N3: 效果量极小，且 downstream 无改善**\n\n同意，这是我自己 N1 和 W2 的核心关注。补充两点 R2 未提及的论据：\n\n1. **效果量的 contextual significance**：PPL 从 pretrained 22.970 降到 17.65 的 5.3-point drop 是 continued pretraining 的主效应；reweighting 的 0.043 改善仅占此 drop 的 0.8%。在如此窄的 residual margin 中，seed variance（±0.007 to ±0.033）与 method difference（0.031 to 0.043）同量级，方法效果很难与噪声分离。\n\n2. **\"省去 grid search\" 的价值依赖于效果量**。R2 正确指出：如果改善本身不重要，省去 grid search 的 compute saving 也不重要。9 次 0.6B + 132M tokens 的训练总共约 1.2B tokens 的计算量，在现代标准下是 trivial 的开销。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: 人造 contamination 不代表真实场景**\n\n同意，与我的 W1 一致。补充：自污染设定（generator = trainee）使得检测器的 task 特别难（AUC 仅 0.939 而非 Drayson 2025 的 0.986），但也特别不现实——真实 web 污染来自多种 generators，distribution 更异质。方法在异质污染下的行为完全未知。\n\n---\n\n**[REBUT] R2-W2: Abstract 超长（~291 words > 250 建议上限），数据堆砌**\n\n部分同意长度问题，但 REBUT \"数据堆砌\"的判断。\n\nACL ARR 对 Abstract 长度无硬性上限（ARR CfP 未指定 word count）。实测 Abstract 约 280 words，略超惯例但不构成格式违规。\n\n关于\"数据堆砌\"：Abstract 中的数字（3-seed means, 95% CI, Δ values, p-values）服务于 claim 的 quantitative substantiation，在 empirical NLP 论文中是标准做法。我的审稿关注点相反——Abstract 中的 claim 措辞可能比数字支撑的更强（如 \"competitive with grid-searched optimum\" 在 CI 包含零时）。问题不在数字多，而在 claim 与数字的对齐。\n\n建议保留关键数字但精简叙事，目标 230-250 words。\n\n---\n\n**[AGREE] R2-W3: 引用偏少（~39 条），遗漏重要工作**\n\n同意。39 条引用对 EMNLP long paper 偏少（同类论文通常 50-70 条）。R2 提到的遗漏中：\n\n- **Gerstgrasser et al. (2024)** \"Is Model Collapse Inevitable?\" — 直接挑战 Shumailov 2024 的 inevitability claim，是 model collapse 讨论中不可忽略的反面视角。\n- **DCLM (Li et al. 2024)** — 大规模 data curation 的直接 comparable，应在 Related Work \"Data Mixing\" 段讨论。\n- **Tale of Tails (Ionescu et al. 2024)** — 关于 importance weighting 中的 heavy-tail 问题，与 ESS 约束的理论基础直接相关。\n\n我自己指出的遗漏（Gururangan 2020, Wettig 2023）加上 R2 的列表，说明 Related Work 的 coverage 确实不足。\n\n---\n\n**[AGREE] R2-W4: Discussion 过于单薄**\n\n同意。Discussion（Section 6）约 20 行，5 个 paragraph，内容基本是 Results 的重新组织（\"why minimum intervention works\" 重述 Section 5.3 的 regime analysis，\"where advantage manifests\" 重述 Section 5.1 的 PPL vs training loss 观察）。缺少的内容包括：\n\n- 方法在什么条件下预期失败（beyond ρ=0.2 的简单 mention）\n- 与 importance weighting 理论（Vehtari 2024 PSIS, Pareto-k diagnostic）的深入连接\n- 对 \"soft vs hard filtering\" 更广泛的理论讨论（信息论视角：reweighting 保留了多少信息？）\n- 实际部署建议（何时用 adaptive，何时用 D&R，何时不需要干预）\n\n---\n\n**[REBUT] R2-W5: \"Minimum Intervention Principle\" framing 过度**\n\n部分同意措辞可更审慎，但 REBUT \"不应命名为 principle\"的判断。\n\n\"Principle\" 在优化文献中常用于命名设计偏好（如 \"principle of maximum entropy\", \"minimum description length principle\", \"parsimony principle\"），并不要求形式化定理。本文的 minimum intervention 选择（选 b_τ 而非 b_ESS 或中间值）是一个有实验支撑的设计决策：ESS-only（maximum intervention）在 Table 1 中显著更差（17.737 vs 17.651），Section 5.3 量化了 4.9× 过度干预。\n\n问题在于 Introduction 第17行的措辞 \"embodying a minimum intervention principle\" 可能暗示理论最优性，而实际上只有经验优势。建议将 \"principle\" 保留但加 qualifier：如 \"an empirically motivated minimum intervention principle\"。\n\n---\n\n**[AGREE] R2-W6: ECE 缩写未定义**\n\n确认。ECE (Expected Calibration Error) 首次出现在 Section 3.2 第32行（\"calibrated ECE=0.048\"）和 Section 4 第7行（\"calibrated ECE=0.048 after temperature scaling\"），均未展开定义。应在首次使用时写全称。\n\n---\n\n### 对 Reviewer 2 关键判断的评估\n\n**Excitement 2.0 vs 我的 3.0**：\n\nR2 的核心理由是 \"对已有公式的自动调参，novelty 更接近 Findings\"。我同意 novelty assessment（Findings 级别），但认为 Excitement 评分应考虑论文的 \"useful insights\" 维度，而非仅看 method novelty：\n\n- Epoch-matched control 的实验方法论有示范价值（Section 5.1, Table 2）\n- Detector signal type 的发现（discriminative vs generative, Appendix D）对后续工作有直接指导\n- τ robustness 分析（Table 3, Figure 4）为实际使用提供了可操作的 guidance\n\nARR guidelines 明确指出 Excitement \"does not necessarily follow what is popular in the field\"。这些实验 insights 即使方法 novelty 有限，也值得 3.0（\"might mention some points to others\"）。2.0 过低。\n\n**Overall 2.5 vs 我的 3.0**：\n\nR2 给 2.5（Borderline Findings），我给 3.0（Findings）。分歧来源是对 epoch-matched control 和 detector-type finding 的权重。我认为这两个分析贡献足以将论文推至 Findings 水平，即使核心方法 novelty 有限。但如果 N2（scale mismatch）不被修复，我也会考虑降至 2.5。\n\n---\n\n### 总结\n\n| R2 编号 | 我的立场 | 核心理由 |\n|---------|---------|---------|\n| R2-N1 | REBUT（部分） | Novelty 确实 incremental（同意 Findings 级别），但 R2 过度简化了贡献，忽略了 ablation 证据和实验 insights |\n| R2-N2 | AGREE | Scale mismatch 是真实问题，framing 与实验不匹配 |\n| R2-N3 | AGREE | 效果量过小且 downstream 无改善，与我的 N1/W2 一致 |\n| R2-W1 | AGREE | 与我的 W1 一致 |\n| R2-W2 | REBUT（部分） | 长度略超但无硬性违规；数字服务于 claim 而非堆砌 |\n| R2-W3 | AGREE | 引用确实偏少，遗漏多篇重要工作 |\n| R2-W4 | AGREE | Discussion 单薄，缺少深入分析 |\n| R2-W5 | REBUT（部分） | \"Principle\" 措辞在优化文献中有先例，但应加 qualifier |\n| R2-W6 | AGREE | ECE 未定义，应修复 |\n| Excitement | REBUT | 2.0 过低，实验 insights 值得 3.0 |\n| Overall | 半同意 | 3.0 vs 2.5 分歧在半档，如果 scale 不修复可降至 2.5 |",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 交叉评审回应 Reviewer 2\n\n---\n\n### Must-Fix 逐条回应\n\n**[REBUT] R2-N1: 新颖性不足以支撑 EMNLP Main Conference**\n\nR2 将本文贡献简化为\"对已有公式的自动超参数选择程序\"，我认为这一概括过于粗暴，遗漏了三个有独立价值的贡献：\n\n1. **Dual-constraint formulation 不是 trivial 的组合**。α_eff 和 ESS 虽然分别是标准工具，但将两者的 opposing monotonicity 形式化为 feasible region [b_τ, b_ESS]，并利用 minimum vs maximum 的选择产生可测量的性能差异（Section 5.1 Table 1: Adaptive 17.651 vs ESS-only 17.737，paired gap 0.086, p<0.01），这一设计选择并非显而易见。R2 说\"标准约束优化的 rebranding\"，但 ESS-only ablation 的失败恰恰证明约束的选取和优化方向（min vs max）是方法成功的关键。\n\n2. **Epoch-matched control 的实验设计**（Table 2）解决了领域中 D&R vs reweighting 对比的一个系统性 confound，这一分析方法论贡献独立于方法本身。\n\n3. **Detector signal type 发现**（Appendix D, Table 7）揭示 AUC 不是决定因素（GPT-2 AUC=0.91 失败，TF-IDF AUC=0.94 成功），这对后续工作的 detector 选择有实用指导意义。\n\n但我同意 R2 的结论方向：**这些贡献更适合 Findings 而非 Main**。我给 Overall 3.0（Findings），R2 给 2.5（Borderline Findings），分歧在半档。核心方法确实是对已有 weighting scheme 的 hyperparameter automation，Excitement 不足以支撑 Main 是合理判断。\n\n我不同意的是 Excitement 2.0 的评分。Epoch-matched analysis 和 detector-type finding 对领域的实际指导价值使本文值得 \"Interesting\"（3.0），而非 \"Potentially Interesting\"（2.0）。\n\n---\n\n**[AGREE] R2-N2: 实验规模与论文动机严重不匹配**\n\n完全同意。论文 Introduction 以 \"web corpora now contain an estimated 20-60% machine-generated text\"（Section 1, 第1行）开篇，framing 是 web-scale 问题，但实验仅 0.6B model + 132M tokens，与 web-scale pretraining（通常 1T+ tokens）相差 4 个数量级。\n\n我在自己的审稿中将此归入 N3（1.7B 单 seed 不充分），但 R2 更准确地指出了 framing-experiment gap 这一更根本的问题。补充论据：\n\n- EMNLP/ACL 近期的 data curation 论文如 DataComp-LM（Gadre et al. 2024, 引用于本文）在 billions of tokens 上验证。DoReMi（Xie et al. 2023）同样在 GPT-scale 上验证。\n- 本文的 \"continued pretraining\" 设定（从 pretrained checkpoint 开始）部分缓解了这一问题，但 Introduction 的 framing 并未限定为 continued pretraining。\n\n建议：调整 Introduction framing 使之与实验规模匹配（聚焦 continued pretraining 场景），或增加更大规模实验。\n\n---\n\n**[AGREE] R2-N3: 效果量极小，且 downstream 无改善**\n\n同意，这是我自己 N1 和 W2 的核心关注。补充两点 R2 未提及的论据：\n\n1. **效果量的 contextual significance**：PPL 从 pretrained 22.970 降到 17.65 的 5.3-point drop 是 continued pretraining 的主效应；reweighting 的 0.043 改善仅占此 drop 的 0.8%。在如此窄的 residual margin 中，seed variance（±0.007 to ±0.033）与 method difference（0.031 to 0.043）同量级，方法效果很难与噪声分离。\n\n2. **\"省去 grid search\" 的价值依赖于效果量**。R2 正确指出：如果改善本身不重要，省去 grid search 的 compute saving 也不重要。9 次 0.6B + 132M tokens 的训练总共约 1.2B tokens 的计算量，在现代标准下是 trivial 的开销。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: 人造 contamination 不代表真实场景**\n\n同意，与我的 W1 一致。补充：自污染设定（generator = trainee）使得检测器的 task 特别难（AUC 仅 0.939 而非 Drayson 2025 的 0.986），但也特别不现实——真实 web 污染来自多种 generators，distribution 更异质。方法在异质污染下的行为完全未知。\n\n---\n\n**[REBUT] R2-W2: Abstract 超长（~291 words > 250 建议上限），数据堆砌**\n\n部分同意长度问题，但 REBUT \"数据堆砌\"的判断。\n\nACL ARR 对 Abstract 长度无硬性上限（ARR CfP 未指定 word count）。实测 Abstract 约 280 words，略超惯例但不构成格式违规。\n\n关于\"数据堆砌\"：Abstract 中的数字（3-seed means, 95% CI, Δ values, p-values）服务于 claim 的 quantitative substantiation，在 empirical NLP 论文中是标准做法。我的审稿关注点相反——Abstract 中的 claim 措辞可能比数字支撑的更强（如 \"competitive with grid-searched optimum\" 在 CI 包含零时）。问题不在数字多，而在 claim 与数字的对齐。\n\n建议保留关键数字但精简叙事，目标 230-250 words。\n\n---\n\n**[AGREE] R2-W3: 引用偏少（~39 条），遗漏重要工作**\n\n同意。39 条引用对 EMNLP long paper 偏少（同类论文通常 50-70 条）。R2 提到的遗漏中：\n\n- **Gerstgrasser et al. (2024)** \"Is Model Collapse Inevitable?\" — 直接挑战 Shumailov 2024 的 inevitability claim，是 model collapse 讨论中不可忽略的反面视角。\n- **DCLM (Li et al. 2024)** — 大规模 data curation 的直接 comparable，应在 Related Work \"Data Mixing\" 段讨论。\n- **Tale of Tails (Ionescu et al. 2024)** — 关于 importance weighting 中的 heavy-tail 问题，与 ESS 约束的理论基础直接相关。\n\n我自己指出的遗漏（Gururangan 2020, Wettig 2023）加上 R2 的列表，说明 Related Work 的 coverage 确实不足。\n\n---\n\n**[AGREE] R2-W4: Discussion 过于单薄**\n\n同意。Discussion（Section 6）约 20 行，5 个 paragraph，内容基本是 Results 的重新组织（\"why minimum intervention works\" 重述 Section 5.3 的 regime analysis，\"where advantage manifests\" 重述 Section 5.1 的 PPL vs training loss 观察）。缺少的内容包括：\n\n- 方法在什么条件下预期失败（beyond ρ=0.2 的简单 mention）\n- 与 importance weighting 理论（Vehtari 2024 PSIS, Pareto-k diagnostic）的深入连接\n- 对 \"soft vs hard filtering\" 更广泛的理论讨论（信息论视角：reweighting 保留了多少信息？）\n- 实际部署建议（何时用 adaptive，何时用 D&R，何时不需要干预）\n\n---\n\n**[REBUT] R2-W5: \"Minimum Intervention Principle\" framing 过度**\n\n部分同意措辞可更审慎，但 REBUT \"不应命名为 principle\"的判断。\n\n\"Principle\" 在优化文献中常用于命名设计偏好（如 \"principle of maximum entropy\", \"minimum description length principle\", \"parsimony principle\"），并不要求形式化定理。本文的 minimum intervention 选择（选 b_τ 而非 b_ESS 或中间值）是一个有实验支撑的设计决策：ESS-only（maximum intervention）在 Table 1 中显著更差（17.737 vs 17.651），Section 5.3 量化了 4.9× 过度干预。\n\n问题在于 Introduction 第17行的措辞 \"embodying a minimum intervention principle\" 可能暗示理论最优性，而实际上只有经验优势。建议将 \"principle\" 保留但加 qualifier：如 \"an empirically motivated minimum intervention principle\"。\n\n---\n\n**[AGREE] R2-W6: ECE 缩写未定义**\n\n确认。ECE (Expected Calibration Error) 首次出现在 Section 3.2 第32行（\"calibrated ECE=0.048\"）和 Section 4 第7行（\"calibrated ECE=0.048 after temperature scaling\"），均未展开定义。应在首次使用时写全称。\n\n---\n\n### 对 Reviewer 2 关键判断的评估\n\n**Excitement 2.0 vs 我的 3.0**：\n\nR2 的核心理由是 \"对已有公式的自动调参，novelty 更接近 Findings\"。我同意 novelty assessment（Findings 级别），但认为 Excitement 评分应考虑论文的 \"useful insights\" 维度，而非仅看 method novelty：\n\n- Epoch-matched control 的实验方法论有示范价值（Section 5.1, Table 2）\n- Detector signal type 的发现（discriminative vs generative, Appendix D）对后续工作有直接指导\n- τ robustness 分析（Table 3, Figure 4）为实际使用提供了可操作的 guidance\n\nARR guidelines 明确指出 Excitement \"does not necessarily follow what is popular in the field\"。这些实验 insights 即使方法 novelty 有限，也值得 3.0（\"might mention some points to others\"）。2.0 过低。\n\n**Overall 2.5 vs 我的 3.0**：\n\nR2 给 2.5（Borderline Findings），我给 3.0（Findings）。分歧来源是对 epoch-matched control 和 detector-type finding 的权重。我认为这两个分析贡献足以将论文推至 Findings 水平，即使核心方法 novelty 有限。但如果 N2（scale mismatch）不被修复，我也会考虑降至 2.5。\n\n---\n\n### 总结\n\n| R2 编号 | 我的立场 | 核心理由 |\n|---------|---------|---------|\n| R2-N1 | REBUT（部分） | Novelty 确实 incremental（同意 Findings 级别），但 R2 过度简化了贡献，忽略了 ablation 证据和实验 insights |\n| R2-N2 | AGREE | Scale mismatch 是真实问题，framing 与实验不匹配 |\n| R2-N3 | AGREE | 效果量过小且 downstream 无改善，与我的 N1/W2 一致 |\n| R2-W1 | AGREE | 与我的 W1 一致 |\n| R2-W2 | REBUT（部分） | 长度略超但无硬性违规；数字服务于 claim 而非堆砌 |\n| R2-W3 | AGREE | 引用确实偏少，遗漏多篇重要工作 |\n| R2-W4 | AGREE | Discussion 单薄，缺少深入分析 |\n| R2-W5 | REBUT（部分） | \"Principle\" 措辞在优化文献中有先例，但应加 qualifier |\n| R2-W6 | AGREE | ECE 未定义，应修复 |\n| Excitement | REBUT | 2.0 过低，实验 insights 值得 3.0 |\n| Overall | 半同意 | 3.0 vs 2.5 分歧在半档，如果 scale 不修复可降至 2.5 |",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-19T04:41:17.775233+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3913
}
```

</details>

---


### Assistant

_source line 116 · 2026-05-19T04:41:23.740192+00:00_

交叉评审已提交。

核心立场：与 R2 在 scale mismatch (N2)、effect size (N3)、引用不足 (W3)、Discussion 薄弱 (W4) 上一致；在 novelty 评估 (N1) 和 Excitement 评分上有分歧——R2 将贡献简化为"自动调参"过于粗暴，epoch-matched control 和 detector-type finding 有独立价值，Excitement 应为 3.0 而非 2.0。Overall 分歧半档（我 3.0 Findings vs R2 2.5 Borderline Findings）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

44 recorded events


### User

_source line 117 · 2026-05-19T05:51:36.295254+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的侧重**: 方法严谨性 + 实验设计 + 统计推断

### Venue 信息
- **目标会议**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle 提交）
- **截止日期**: 2026-05-25
- **正文页数**: 8 页（参考文献不限）
- **模板**: ACL 官方 style files，双栏格式
- **匿名规则**: Double-blind
- **必需**: Limitations section + Responsible NLP Research Checklist

### 论文信息
- **标题**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
- **论文路径**: `projects/provenance_weight_training/docs/paper/main.tex`
  - Sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, checklist.tex, appendix.tex
  - 引用: `docs/paper/references.bib`

### 审查重点（你的职责）

1. **方法严谨性**:
   - Dual-constraint framework（α_eff ≥ τ, ESS ≥ n_min）的数学推导是否正确、完备？
   - Proposition 1（α_eff 单调性）的证明是否严密？proof sketch 是否充分？
   - ESS 单调性（Proposition 2）是否正确？
   - "Minimum intervention" 语义是否有理论支撑，还是仅仅是设计选择？
   - α_eff 作为 true real fraction 的 proxy 是否可靠？r_i = 1[q_i ≤ 0.5] 这个 indicator 的合理性？
   - 超参数 τ=0.8 和 n_min=⌊B/2⌋ 的选择是否有充分依据？

2. **实验设计**:
   - 自污染设计（Qwen3-0.6B 生成 + 同模型训练）的合理性和局限性
   - 132M tokens 的数据规模是否足以支撑结论？
   - Batch size 4（micro-batch）下计算 α_eff 的统计可靠性（只有 5 个离散值）
   - Grid search baseline（9 个 b 值，post-hoc 最优选择）是否公平？
   - Epoch-matched control 的实验设计是否正确？是否真的消除了 multi-epoch confound？
   - 3 seeds 的统计检验力是否充足？95% CI [-0.039, 0.101] 包含正值的含义

3. **统计推断**:
   - "competitive with grid-best" 的 claim 是否被数据支撑？（CI 包含 degradation）
   - p < 0.01（N=3）的可信度
   - 效应量（0.043 PPL at ρ=0.4）的实际意义
   - 1.7B 结果（Δ=-0.01，2 seeds）能否支撑 "transfers without degradation" 的 claim？

请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-19T05:51:42.453982+00:00_

called Skill

<details open><summary>🔧 Tool call — Skill</summary>

```json
{
  "skill": "review-reviewer-session-start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-19T05:51:42.454328+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Skill",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-19T05:51:47.826172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-19T05:51:49.332793+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1506
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-19T05:51:49.383423+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-19T05:51:49.435108+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-19T05:51:53.262969+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 125 · 2026-05-19T05:51:55.173961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-19T05:51:56.137647+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\input{sections/checklist}
74	
75	\bibliography{references}
76	
77	\appendix
78	\input{sections/appendix}
79	
80	\end{document}
81	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 127 · 2026-05-19T05:51:56.138189+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-19T05:51:56.232072+00:00_

1	Web corpora now contain an estimated 20--60\% machine-generated text, and training on such contaminated data risks model collapse.
2	Detect-and-reweight methods suppress likely-synthetic samples via $w(x) = (1-q(x))^b$, but the exponent $b$ critically determines outcomes and requires per-model grid search (typically multiple complete training runs) to tune.
3	
4	We propose a dual-constrained adaptive exponent $b^*$ derived per-batch from detector scores alone: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling).
5	This minimum intervention strategy applies only as much downweighting as needed, with zero validation cost.
6	
7	On Qwen3-0.6B continued pretraining (132M FineWeb tokens, 40\% synthetic contamination), the gap between adaptive and grid-best (0.031 PPL) falls within grid-search's own cross-seed variance ($\pm$0.033), eliminating the need for exhaustive search (nine runs to one; 95\% CI of gap $[-0.039, 0.101]$, which includes possible degradation).
8	The advantage extends to $\rho{=}0.6$ ($\Delta{=}{-}0.028$, $p{<}0.01$, $N{=}3$) and transfers to 1.7B without degradation ($\Delta{=}{-}0.01$).
9	An epoch-matched control ($N{=}3$) shows D\&R's full-length advantage is entirely attributable to multi-epoch exposure ($\Delta{=}0.006$ at equal epochs).
10	Detector type matters more than AUC: a discriminative detector (TF-IDF+LR, AUC\,=\,0.94) produces consistent gains, while two generative perplexity detectors (AUC up to 0.91) both reverse the advantage.
11	
12	Soft provenance-based reweighting matches hard filtering at equal data exposure, eliminating both grid search and the multi-epoch training that drives D\&R's apparent advantage.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 93
}
```

</details>

---


### Tool call

_source line 129 · 2026-05-19T05:51:56.232509+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-19T05:51:56.308479+00:00_

1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation (\emph{model collapse}), and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware training a practical necessity, particularly for continued pretraining on potentially contaminated data.
6	
7	A natural response is \emph{detect-and-reweight}: suppress likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a classifier's synthetic probability estimate.
8	However, the exponent $b$ critically determines outcomes and requires per-model validation-set grid search~\citep{drayson2025detection}; alternative approaches require the exact contamination ratio~\citep{he2025golden} or a well-calibrated detection threshold for hard filtering~\citep{feng2025beyond}.
9	
10	Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
11	We formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\aeff(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $\nmin$.
12	The quality constraint has theoretical grounding
…[truncated 3291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 75
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-19T05:51:59.975558+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Here are the key findings about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Recommendation Scoring Scale

5 = Consider for Award: reviewers think the paper could be considered for an outstanding paper award at 
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6712
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-19T05:52:06.102449+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any specific criteria or guidelines for each score level. Include soundness, excitement, overall recommendation, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any specific criteria or guidelines for each score level. Include soundness, excitement, overall recommendation, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-19T05:52:08.011195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-19T05:52:08.463533+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	The indicator $r_i = \mathbf{1}[q_i \leq 0.5]$ is a proxy for true provenance: $\alpha_{\mathrm{eff}}$ tracks the detector's estimate of the real fraction, not
…[truncated 9713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 135 · 2026-05-19T05:52:08.464012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-19T05:52:08.715266+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.939, calibrated ECE\,=\,0.048 after temperature scaling with $T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.913) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
14	All main comparisons use three random seeds (42, 123, 456).
15	
16	\paragraph{Evaluation.}
17	We 
…[truncated 1508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 137 · 2026-05-19T05:52:08.766091+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 138 · 2026-05-19T05:52:08.816942+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves PPL competitive with grid-best: 3-seed means 17.651 vs.\ 17.620 for grid $b{=}0.3$ (gap 0.031, 95\% CI $[-0.039, 0.101]$).
8	With only $N{=}3$ seeds, this interval is too wide for formal equivalence testing; we refrain from claiming statistical indistinguishability and instead emphasize the practical value: the adaptive method requires one training run instead of nine~\citep{drayson2025detection}, with lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
9	Using the mean of per-batch $\bstar$ ($\bar{b}^*{=}1.19$) as a fixed exponent yields PPL 17.693, comparable to uniform (17.694); per-batch adaptation is essential.
10	
11	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
12	Random weights $\mathcal{U}(0,2)$ (mean 17.803) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
13	ESS-only (mean $17.737 {\pm} 0.017$) uses $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
14	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves over uniform (paired gap $0.043$, $p{<}0.01$, $N{=}3$).
15	Figure~\ref{fig:grid_b_trend} contextualizes this: the grid curve has a broad plateau at $b \in [0.1, 0.5]$ (PPL 17.620--17.655), and adaptive $\bstar$ (mean 17.651) f
…[truncated 8578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-19T05:52:14.288461+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but conceivable errors
- **3**: Pretty sure, though details may be missed
- **2**: Willing to defend evaluation, but details possibly overlooked
- **1**: Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Strong with sufficient support; minor experiments optional
- **3**: Acceptable with support for main claims; minor details may need strengthening
- **2**: Poor; main claims lack sufficient support with major technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: Highly Exciting; would recommend broadly
- **4**: Exciting; would mention to others
- **3**: Interesting; might mention selectively
- **2**: Potentially Interesting; may resonate with some community members
- **1**: Not Exciting; lacks relevance to computational linguistics

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings track acceptance
- **2.5**: Borderline Findings
- **2**: Substantial revisions needed for next cycle
- **1.5**: Major revisions needed for following cycle
- **1**: Do not resubmit; lacks relevance

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations possible
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Very difficult; unavailable data or insufficient details
- **1**: Irreproducible regardless of effort

## 6. 
…[truncated 679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8186
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-19T05:52:21.319765+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-19T05:52:21.671418+00:00_

1	\paragraph{Why minimum intervention works.}
2	In the 38.2\% of batches where $\aeff$ determines $\bstar$, the selected exponent is 4.9$\times$ lower than the ESS-only upper bound (\S\ref{sec:regime}); this rate is robust across contamination levels (33.4\% at $\rho{=}0.6$) and seeds (CV ${<}2\%$).
3	The aggregate mean $\bstar \approx 1.4$ as a fixed exponent yields PPL no better than uniform (17.693 vs.\ 17.694), confirming per-batch adaptation is essential.
4	
5	\paragraph{Failure modes.}
6	At $\rho{=}0.2$, the method degrades ($+$0.046 PPL): detector mean $q{=}0.393$ indicates poor discrimination, yet $\aeff$-binding in ${\sim}$60\% of batches causes active but misdirected reweighting (Appendix~\ref{app:rho02}).
7	Both generative detectors (GPT-2 PPL AUC\,=\,0.91, $\Delta{=}{+}0.10$; N-gram PPL AUC\,=\,0.73, $\Delta{=}{+}0.13$) fail via the same mechanism: conflating predictability with synthetic origin.
8	The method requires discriminative signal targeting provenance rather than fluency.
9	
10	\paragraph{Soft vs.\ hard filtering.}
11	At equal content epochs, D\&R ($17.657 \pm 0.006$) and adaptive $\bstar$ ($17.651 \pm 0.007$) are equivalent ($\Delta{=}0.006$, $N{=}3$).
12	D\&R's best full-length PPL (17.250 at $q{>}0.3$) requires ${\sim}$3.2$\times$ effective compute and a calibrated threshold; the raw U-shaped curve is entirely a multi-epoch artifact (Figure~\ref{fig:dr_dual_curve}).
13	A hybrid ($q{>}0.95$ removal + adaptive, PPL\,=\,17.514) further improves but assigns $w{=}0$, conflicting with minimum intervention; its advantage likely also reflects multi-epoch exposure.
14	
15	\paragraph{$\tau$ and deployment.}
16	$\tau \in [0.5, 0.8]$ all outperform uniform; $\tau \in [0.7, 0.8]$ is robust across $\rho \in \{0.4, 0.6\}$ (Appendix~\ref{app:tau_rho}).
17	$\tau$ remains empirical; theoretical derivation is open (\S\ref{sec:limitations}).
18	Defaults: discriminative detector with AUC ${\geq}$ 0.94, $\tau{=}0.8$, $\nmin{=}\lfloor B/2 \rfloor$.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-19T05:52:21.671939+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-19T05:52:22.174010+00:00_

1	We introduced Minimum Intervention Reweighting, a dual-constraint framework that derives per-batch $\bstar$ from detector scores alone ($\aeff(b) \geq \tau$, $\mathrm{ESS}(b) \geq \nmin$), reducing grid search from nine runs to one; the adaptive-to-grid gap (0.031 PPL) falls within grid-search's own cross-seed variance ($\pm$0.033, 95\% CI $[-0.039, 0.101]$).
2	The ablation confirms both detector signal and minimum intervention are necessary ($\rho{=}0.4$); a 3-seed epoch-matched control shows D\&R's apparent advantage is entirely due to multi-epoch exposure ($\Delta{=}0.006$).
3	Empirically, the advantage diminishes at higher contamination ($\rho{=}0.6$: $\Delta{=}{-}0.028$) and is negligible at 1.7B scale ($\Delta{=}{-}0.01$), suggesting the method's primary value lies in the 0.6B continued pretraining regime tested here.
4	Future work: multi-seed scale confirmation, discriminative detector characterization across architectures, and naturally contaminated corpora.
5	Code and data will be released upon acceptance.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-19T05:52:22.174375+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-19T05:52:22.676826+00:00_

1	\paragraph{Scale and cross-model transfer.}
2	All main experiments use Qwen3-0.6B with batch size 4 on 132--200M tokens, comparable to domain-adaptive continued pretraining but far below full pretraining scale; validation at ${>}$100B tokens remains an important direction.
3	A 1.7B verification (Qwen3-1.7B, $\rho{=}0.4$) under matched conditions shows $\Delta{=}{-}0.01$ (adaptive 13.26 vs.\ uniform 13.26), confirming that the method transfers without degradation but does not demonstrate a clear advantage at this scale; multi-seed replication is needed.
4	Cross-model transfer (Llama-3.2-3B, single seed) shows parity with uniform on PPL and HellaSwag, with a $+$1.6\,pp MMLU advantage that requires replication.
5	
6	\paragraph{Contamination range.}
7	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative), indicating an effective range of $\rho \geq 0.4$ with $\tau{=}0.8$.
8	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
9	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
10	
11	\paragraph{Detector coverage.}
12	Three detectors have been tested: TF-IDF+LR (discriminative, AUC\,=\,0.94) succeeds, while GPT-2 perplexity (generative, AUC\,=\,0.91) and N-gram perplexity (generative, AUC\,=\,0.73) both fail.
13	The pattern suggests discriminative signal is necessary, but three detectors from two families cannot distinguish a type effect from a calibration effect; testing additional discriminative detectors at varying AUC levels would isolate the mechanism.
14	
15	\paragraph{Threshold.}
16	$\tau$ is an empirical hyperparameter.
17	The convergence theory of \citet{wang2026survive} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
18	
19	\paragraph{Evalua
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-19T05:52:22.677317+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-19T05:52:23.179634+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
7	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
8	
9	\paragraph{Detection and Filtering of Machine-Generated Text.}
10	Given the severity of contamination, a natural response is to detect and remove synthetic content.
11	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens.
12	All produce continuous confidence scores suitable as input to downstream weighting, including ours.
13	\citet{kirchenbauer2023watermark} propose watermarkin
…[truncated 5042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-19T05:52:23.180084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-19T05:52:23.230967+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
5	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
6	Then
7	\begin{equation*}
8	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
9	\end{equation*}
10	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
11	Taking the derivative with respect to $b$:
12	\begin{align*}
13	  \frac{d\pi_i}{db}
14	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right)
15	  = \pi_i \!\left(\ln(1{-}q_i) - \sum_j \pi_j \ln(1{-}q_j)\right).
16	\end{align*}
17	Substituting,
18	\begin{align*}
19	  \frac{d\alpha_{\mathrm{eff}}}{db}
20	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
21	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
22	\end{align*}
23	For any detector with better-than-random discrimination, real samples ($r_i = 1$) have $q_i \leq 0.5$ on average, and thus higher $\ln(1{-}q_i)$ than synthetic samples.
24	The weighted covariance $\mathrm{Cov}_{\pi}(r_i, \ln(1{-}q_i))$ is therefore non-negative, establishing that $\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$.
25	\end{proof}
26	
27	\begin{proposition}[ESS monotonicity]
28	\label{prop:ess_mono}
29	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
30	\end{proposition}
31	
32	\begin{proof}
33	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
34	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
35	Differentiating $H$ with respect to $b$:
36	\begin{equation*}
37	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
38	\end{equation*}
39	This equals $2\,\mathrm{Var}_{\pi^2}[\ln(1{-}q)]$ under the $\pi^2$-weighted measure.
40	Since variance is non-negative and strictly positive when not all $\ln(1{-}q_i)$ coincide (i.e., when at least two $q$
…[truncated 16281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-19T05:52:28.879645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "offset": "344"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
    "offset": "344"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-19T05:52:29.834354+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (344). The file has 344 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-19T05:52:29.834829+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-19T05:52:30.387496+00:00_

1	% Responsible NLP Research Checklist
2	% https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A. For Every Submission}
7	
8	\begin{itemize}[nosep,leftmargin=*]
9	\item[\checkmark] \textbf{A1.} Did you describe the limitations of your work?
10	\textit{Yes, \S\ref{sec:limitations} discusses scale, contamination range, detector coverage, threshold, evaluation, and effect size limitations.}
11	
12	\item[\checkmark] \textbf{A2.} Did you discuss any potential risks of your work?
13	\textit{Yes. The method assumes a pre-trained detector is available; deploying it with a poorly calibrated detector could degrade training quality (discussed in \S\ref{sec:limitations}, Detector coverage). The method does not generate new content or enable harmful uses beyond standard language model pretraining.}
14	\end{itemize}
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\checkmark] \textbf{B1.} Did you cite the creators of artifacts you used?
20	\textit{Yes. FineWeb~\citep{penedo2024fineweb}, Qwen3~\citep{yang2025qwen3}, and all baseline methods are cited in \S\ref{sec:experiments} and \S\ref{sec:related}.}
21	
22	\item[\checkmark] \textbf{B2.} Did you discuss the license or terms for use and/or distribution of any artifacts?
23	\textit{FineWeb is released under Apache-2.0; Qwen3 under Apache-2.0. Our code and data will be released upon acceptance.}
24	
25	\item[\checkmark] \textbf{B3.} Did you discuss if your use of existing artifacts was consistent with their intended use?
26	\textit{Yes. FineWeb is intended for language model training; we use it as a pretraining corpus. Qwen3 is used for both continued pretraining and synthetic data generation, consistent with its general-purpose design.}
27	
28	\item[\checkmark] \textbf{B4.} Did you discuss the steps taken to check whether the data contains information that names or uniquely identifies individ
…[truncated 3080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-19T05:52:32.897555+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL fields, especially: 1) The exact scoring scales for soundness, excitement, and overall assessment with all intermediate values. 2) Any specific criteria mentioned for each dimension. 3) Any required free-text fields. 4) The reproducibility checklist criteria. 5) Any guidance on what constitutes different score levels."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL fields, especially: 1) The exact scoring scales for soundness, excitement, and overall assessment with all intermediate values. 2) Any specific criteria mentioned for each dimension. 3) Any required free-text fields. 4) The reproducibility checklist criteria. 5) Any guidance on what constitutes different score levels."
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-19T05:52:37.916299+00:00_

# ACL Rolling Review Form - Complete Structure

## Required Free-Text Fields

1. **Paper Summary** - Description of paper topic
2. **Summary of Strengths** - Reasons for publication
3. **Summary of Weaknesses** - Numbered concerns
4. **Comments/Suggestions/Typos** - Author improvement suggestions
5. **Best Paper Justification** - Required if award consideration
6. **Limitations and Societal Impact** - Discussion of harms and benefits
7. **Ethical Concerns** - Assessment against ACL code of ethics
8. **Knowledge of Author Identity** - Optional conjecture field

## Scoring Scales

### Reviewer Confidence
Scale 1-5: "Not my area" (1) through "Positive that my evaluation is correct" (5)

### Soundness
Scale 1-5 with half-point increments (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
- Ranges from "Major Issues" to "Excellent: This study is one of the most thorough"

### Excitement
Scale 1-5 with half-point increments
- Ranges from "Not Exciting" to "Highly Exciting: I would recommend this paper to others"

### Overall Assessment
Scale 1-5 with half-point increments
- Ranges from "Do not resubmit" (1) to "Consider for Award" (5)
- Distinguishes Conference vs. Findings track recommendations

### Reproducibility
Scale 1-5: "Would not be able to reproduce" (1) to "Could easily reproduce" (5)

### Datasets & Software Value
Scale 1-5: "No usable [datasets/software]" (1) to "Enabling" (5)

### Author Identity Knowledge
Scale 1-5: "No educated guess" (1) to "Violation of blind submission rules" (5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5018
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-19T05:54:06.965502+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-19T05:54:51.166556+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 45, \"total_citations\": 72, \"unique_cited_keys\": 45, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 34, \"online_not_found\": 6, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"drayson2025detection\", \"type\": \"article\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.15654\"}, {\"key\": \"he2025golden\", \"type\": \"article\", \"title\": \"Golden Ratio Weighting Prevents Model Collapse\", \"authors\": \"He, Hengzhi and Xu, Shirong and Cheng, Guang\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.18049\"}, {\"key\": \"wang2026survive\", \"type\": \"article\", \"title\": \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive T...\", \"authors\": \"Wang, Kevin and Niu, Hongqian and Li, Didong\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.16065\"}, {\"key\": \"shumailov2024model\", \"type\": \"article\", \"title\": \"AI Models Collapse When Trained on Recursively Generated Data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2025strong\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"ICLR\"}, {\"key\": \"vehtari2024psis\", \"type\": \"article\", \"title\": \"Pareto Smoothed Importance Sampling\", \"authors\": \"Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, J...\", \"year\": \"2024\", \"venue
…[truncated 33358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 44201
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-19T05:57:24.822162+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n### Paper Summary\n\n本文提出 Minimum Intervention Reweighting (MIR)，一种用于污染感知预训练的自适应指数选择方法。给定 detect-and-reweight 框架 w(x) = (1-q(x))^b，作者提出 per-batch 双约束优化：找最小的 b 使得 weighted effective real proportion α_eff(b) ≥ τ（质量下限），同时保持 ESS(b) ≥ n_min（稳定性上限）。在 Qwen3-0.6B 上的 132M token 续训实验中，自适应方法与 grid search 最优值竞争（gap 0.031 PPL），同时将搜索成本从 9 次训练降至 1 次。论文还发现 D&R 相对于 reweighting 的优势完全来自多 epoch 暴露，以及判别式检测器（而非生成式）是 reweighting 有效性的必要条件。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 框架设计清晰、epoch-matched 发现有价值，但效应量极小且未能转移到下游任务或更大规模，核心统计推断力不足以支撑主要 claims。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 数学推导基本正确，但实验证据与 claims 之间存在系统性落差：CI 包含降级、下游评估为负、1.7B 仅 2 seeds |\n| Excitement | 2.5 / 5 | 问题重要且 framing 清楚，但 0.043 PPL 的效应量（0.24% 相对改善）在实际应用中意义有限，且方法在 ρ=0.2 失败、ρ=0.6 减弱、1.7B 消失 |\n| Reproducibility | 4.0 / 5 | 算法、超参、训练配置描述充分；代码承诺发布但尚未提供 |\n| Reviewer Confidence | 4 / 5 | 熟悉 importance weighting、LM pretraining 和统计推断 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 效应量极小，下游任务不支持 PPL 改善的实际意义\n\n- 具体位置：Table 1 (main results), Table 8 (downstream, Appendix D)\n- 问题：核心 PPL 改善为 0.043（17.694 → 17.651，0.24% 相对），发生在已被续训吸收 5.2 PPL 的\"残差\"区间内。更关键的是，Table 8 的下游评估显示 5 个 benchmark 中 4 个为负 Δ（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA 微正（+0.001）。sign-test p ≈ 0.19，suggestive but not significant。\n- 为什么影响接收：如果 PPL 改善无法转化为任何可测量的下游增益，那么方法的实际价值存疑。论文 §Limitations 承认\"the PPL improvement may partly reflect distribution matching (training data closer to the human-only evaluation set) rather than a generalizable quality gain\"，但这一关键限制被藏在 Limitations 而非 Results 或 Abstract 中。Abstract 和 Introduction 的 framing 给出了比实际证据更强的印象。\n- 建议修改方向：(1) 在 Results 正文中报告下游结果（而非仅 Appendix），并诚实讨论 PPL-downstream 脱节；(2) 多 seed 下游评估以判断趋势是否稳定；(3) 考虑在 Abstract 中明确 PPL 改善的局限性。\n\n**N2** [critical] 1.7B \"transfers without degradation\" 的 claim 缺乏统计支撑\n\n- 具体位置：§5.2 (Scale and detector signal), §Conclusion, §Limitations\n- 问题：1.7B 结果基于 2 seeds（13.25, 13.27），uniform baseline 仅 1 seed（13.26）。Δ = -0.01 在任何标准下都无法区分 noise 和 signal。2 个数据点无法计算有意义的 CI 或 p-value。论文 Conclusion 称\"the advantage observed at 0.6B does not amplify\"，但实际上连\"advantage 是否存在\"都无法判断。\n- 为什么影响接收：这是三个 Contribution 的实验基础之一。如果 1.7B 结果不可靠，method 的 scale transfer claim 就悬空了。\n- 建议修改方向：(1) 至少 3 seeds for both adaptive 和 uniform at 1.7B；(2) 或明确降级 claim 为 \"preliminary evidence\"，不在 Abstract/Conclusion 中作为 contribution。\n\n**N3** [critical] \"competitive with grid-best\" 的 framing 与 CI 不一致\n\n- 具体位置：Abstract, §5.1, §Conclusion\n- 问题：95% CI of gap 为 [-0.039, 0.101]。这意味着自适应方法可能比 grid-best 差 0.101 PPL，而 grid-best 自身的 cross-seed 标准差为 ±0.033。Abstract 称 \"the gap (0.031 PPL) falls within grid-search's own cross-seed variance (±0.033)\"，但这种比较混淆了两个不同的统计量：gap 的 CI 是 paired variability 的函数，cross-seed variance 是 marginal variability。CI 包含 0 本身不构成等价性证据——N=3 下 CI 过宽是 power 不足的结果，不是等价性的证明。\n- 论文 §5.1 确实写了 \"we refrain from claiming statistical indistinguishability\"，但 Abstract 和 Conclusion 的措辞隐含了等价性 claim。\n- 为什么影响接收：核心 claim 的统计逻辑不成立。\n- 建议修改方向：(1) Abstract 中明确 CI 包含降级的可能性；(2) 增加 seeds 以缩窄 CI；(3) 若无法增加 seeds，将 claim 明确为\"point estimate competitive, but wide CI prevents formal equivalence\"。\n\n**N4** [critical] Batch size B=4 下 α_eff 仅有 5 个离散值，bisection 搜索的意义存疑\n\n- 具体位置：§3.3 (Algorithm), §3.4 (Hyperparameters), Appendix F (α_eff Proxy Validation)\n- 问题：B=4 时，α_eff(0) 取值仅有 {0, 0.25, 0.5, 0.75, 1.0}。r_i ∈ {0,1} 的 4 个值之和除以 4，最多 5 种可能。这意味着 bisection 搜索 b_τ 使得 α_eff(b) = τ = 0.8 时，α_eff 作为 b 的函数是一个最多有 4 个跳跃点的阶梯函数。整个\"连续优化\"框架在 B=4 下退化为一个极粗粒度的离散选择。\n- Appendix Table 5 报告 Pearson r ≈ 0.70, MAE = 0.114。r=0.70 意味着 51% 的方差未被解释；MAE=0.114 意味着平均 11.4% 的估计误差。这对于一个声称提供\"quality floor\"的指标来说是相当粗糙的。\n- 论文辩称 \"PPL differs by <0.01 across B ∈ {4, 8, 16}\"，但这些实验的细节（多少 seeds？哪些 B 值实际测试了？）不够清楚。\n- 为什么影响接收：方法的核心机制——per-batch α_eff-driven b* selection——在实际使用的 batch size 下几乎丧失了设计中的连续性和精度。如果 B=4 和 B=16 的 PPL 差异 <0.01，且 B=4 下 α_eff 如此粗糙，那是否说明 per-batch adaptation 的价值主要不在于 α_eff 的精确值，而在于其他因素？这需要更深入的分析。\n- 建议修改方向：(1) 在方法 section 中明确讨论 B=4 下的离散化问题及其对 bisection 的影响；(2) 提供 B=8 和 B=16 的多 seed 结果以验证 robustness claim；(3) 分析 α_eff-binding 在不同 B 下的频率和 b* 分布变化。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 自污染设计（self-contamination）的生态效度有限\n\n- 具体位置：§4 (Experimental Setup), §Limitations\n- 问题：用 Qwen3-0.6B 生成合成数据再训练同模型，是一种特殊的自污染场景。真实 web 污染来自多种不同模型、不同大小、非均匀混合。论文的 cross-model 结果（Llama-3.2-3B generator, Appendix H）是单 seed 且结果 mixed（MMLU +1.57pp, HellaSwag -0.60pp），无法支撑泛化性。\n- 建议：(1) 至少测试一个\"强生成器 + 弱训练模型\"场景（如 GPT-4 生成 → 0.6B 训练）；(2) 或明确将 self-contamination 标注为主要假设限制。\n\n**W2** [warning] 132M tokens 的规模太小，结论的可迁移性未知\n\n- 具体位置：§4, §Limitations\n- 问题：132M tokens 对应 domain-adaptive continued pretraining，但论文动机和 introduction 讨论的是 web-scale 污染场景。方法在 1.7B 上已无 measurable advantage (Δ=-0.01)。论文 Conclusion 诚实地承认\"the method's primary value lies in the 0.6B continued pretraining regime tested here\"，但 Introduction 和 Abstract 的 framing 没有反映这一限制。\n- 建议：Introduction 中明确方法的目标场景是 continued pretraining（而非 from-scratch pretraining），并在 Abstract 中限定 scope。\n\n**W3** [warning] Epoch-matched 对比存在潜在混淆变量\n\n- 具体位置：§5.1 (Hard filtering and the epoch confound), Table 2\n- 问题：D&R epoch-matched 运行 2,533 步（vs. adaptive 6,103 步），以匹配约 1.0 content epoch。但两个实验的 cosine learning rate schedule 总长度不同（2,533 vs. 6,103 步），这意味着 warmup 比例和 decay 曲线不同。D&R epoch-matched 可能因为更短的 schedule 导致 under-optimization（更少的 gradient updates），也可能因为更快的 decay 受益。这个混淆变量未被讨论。\n- 更严格的设计是：两个方法使用相同总步数但不同 data pipeline（adaptive 看所有数据一次，D&R 过滤后用剩余数据填充到相同步数但不重复）。\n- 为什么重要：Contribution 2 的核心 claim——\"D&R's reported advantage over reweighting is entirely a multi-epoch artifact\"——依赖于这个 epoch-matched 设计的正确性。\n- 建议：(1) 讨论 LR schedule 差异对结果的潜在影响；(2) 或提供控制实验（相同步数 + 不同 data pipeline）。\n\n**W4** [warning] Grid search baseline 的公平性需要讨论\n\n- 具体位置：§4 (Methods), §5.1\n- 问题：Grid-$b$ 从 9 个值中 post-hoc 选最优，是一个 oracle baseline。实际使用中 grid search 需要 validation set 选择，且容易 overfit to validation distribution。论文正确标注了 \"post-hoc oracle\"，但比较的 fairness 需要更显式的讨论：\n  - 如果 grid search 用 validation set 选择（而非 post-hoc on test set），其 PPL 会更差\n  - 因此 adaptive 相对于\"实际可用的 grid search\"可能有更大优势\n- 这其实对论文有利，但目前的呈现方式没有充分利用这一点。\n- 建议：明确讨论 post-hoc vs. validation-based grid search 的区别，可能增加一个 validation-based grid search 结果作为更公平的 baseline。\n\n**W5** [warning] p < 0.01 (N=3) 的可信度和解释\n\n- 具体位置：§5.1, §5.2\n- 问题：N=3 的 paired t-test 只有 2 个自由度。p < 0.01 在数学上是可能的（paired differences 的 t 值足够大），但正态性假设在 N=3 下无法验证。论文使用 p-value 时应附带这一 caveat。此外，p < 0.01 at ρ=0.6 的报告方式给人以\"高度显著\"的印象，但在 N=3 下任何 p-value 都应持保留态度。\n- 建议：(1) 报告 exact paired differences 而非仅 p-value；(2) 注明 N=3 下 t-test p-value 应谨慎解读；(3) 考虑非参数检验（如 sign test）作为 robustness check。\n\n**W6** [warning] \"Minimum intervention\" 缺乏理论最优性证明\n\n- 具体位置：§3.2, §6 (Discussion)\n- 问题：选择 b* = b_τ（最小 b）而非 b_ESS（最大 b）或其他中间值，论文称之为 \"minimum intervention strategy\"，理由是\"borderline samples still carry useful training signal\"。这是一个合理的设计直觉，但不是定理。论文引用 wang2026survive 提供 α_eff ≥ τ 的动机，但 wang2026survive 假设已知 α，且未证明\"最小 b\"是最优的。\n- Empirically, ESS-only (maximum b) 确实更差，但这只排除了一个极端，不证明 minimum 是最优——例如 b* = (b_τ + b_ESS)/2 可能更好，论文没有测试。\n- 建议：(1) 测试 feasible region 中的其他选择策略（如 midpoint, geometric mean）；(2) 或明确标注 minimum intervention 是一个 heuristic，不是 optimal。\n\n---\n\n## 小问题（不影响接收）\n\n- §5.1: \"3-seed means: 17.651 vs. 17.620 for grid b=0.3 (gap 0.031, 95% CI [−0.039, 0.101])\"——应说明 CI 计算方法（paired t-based? bootstrap?）\n- Table 1: D&R full (q>0.5) 标注为 seed 42 only，但 D&R (q>0.3) 标注为 3 seeds；不同 D&R threshold 的 seed 数量不一致，增加了比较的复杂性\n- §3.4: \"We leave fine-grained ratio characterization (e.g., 0.4 vs. 0.6) to future work\"——考虑到 n_min 是核心超参之一，这一留白略显不足\n- Appendix Table 5: \"Spearman r=0.699\" 在正文 §3.3 中被引用为 \"sufficient variance within micro-batches\"，但 0.699 是否\"sufficient\"是主观判断\n- Abstract 中 \"eliminating the need for exhaustive search (nine runs to one; 95% CI of gap [−0.039, 0.101], which includes possible degradation)\" 这句话的后半部分削弱了前半部分的 claim，导致 Abstract 内部信息传达矛盾\n- §5.2 报告 ρ=0.6 时 Grid b=0.3 仅 seed 42 (17.634)，adaptive 三 seed mean 17.736——gap 扩大到 0.102。如果 grid 也是 3-seed 结果，gap 可能不同，这个比较不公平\n- Checklist E1 \"AI assistants were used for code development and manuscript drafting\" 可以更具体（哪些 AI、用于哪些部分）\n\n---\n\n## 主要优势\n\n1. **问题定义清晰，框架设计优雅**：将 b 的选择形式化为双约束优化，两个约束具有自然的对立单调性，这是一个比 grid search 更优雅的解决方案框架。\n2. **Epoch-matched 发现有独立价值**：证明 D&R 的优势来自多 epoch 暴露（而非 filtering 本身）是一个有意义的负面结果，对 community 有参考价值（§5.1, Table 2, Figure in Appendix）。\n3. **检测器类型发现是 novel 的**：discriminative vs. generative 检测器的差异（Table 9, §5.2）提供了关于 reweighting 何时有效的实践指导，这个发现比主方法本身可能更有影响。\n4. **诚实的 Limitations**：§Limitations 相当全面，覆盖了 scale, ρ range, detector coverage, τ, evaluation, effect size 等方面。许多问题在 Limitations 中已被承认。\n5. **写作质量较高**：论文结构清晰，Related Work 做了有效的 positioning（特别是与 Drayson et al. 2025 的三点区别），Algorithm 1 描述明确。\n\n---\n\n## 总结建议\n\n本文提出了一个设计清晰的框架，但实验证据系统性地弱于 claims。核心困境：方法在唯一充分测试的 setting（0.6B, ρ=0.4, 132M tokens）中效应量极小（0.24%），且无法转化为下游增益；在其他 settings（ρ=0.2, 1.7B, cross-model）中要么失败要么不可判断。建议增加实验规模（更多 seeds、更大模型、下游评估）后重投，或重新 framing 为一个聚焦于 epoch-matched 和 detector-type 发现的分析性贡献。\n",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n### Paper Summary\n\n本文提出 Minimum Intervention Reweighting (MIR)，一种用于污染感知预训练的自适应指数选择方法。给定 detect-and-reweight 框架 w(x) = (1-q(x))^b，作者提出 per-batch 双约束优化：找最小的 b 使得 weighted effective real proportion α_eff(b) ≥ τ（质量下限），同时保持 ESS(b) ≥ n_min（稳定性上限）。在 Qwen3-0.6B 上的 132M token 续训实验中，自适应方法与 grid search 最优值竞争（gap 0.031 PPL），同时将搜索成本从 9 次训练降至 1 次。论文还发现 D&R 相对于 reweighting 的优势完全来自多 epoch 暴露，以及判别式检测器（而非生成式）是 reweighting 有效性的必要条件。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 框架设计清晰、epoch-matched 发现有价值，但效应量极小且未能转移到下游任务或更大规模，核心统计推断力不足以支撑主要 claims。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 数学推导基本正确，但实验证据与 claims 之间存在系统性落差：CI 包含降级、下游评估为负、1.7B 仅 2 seeds |\n| Excitement | 2.5 / 5 | 问题重要且 framing 清楚，但 0.043 PPL 的效应量（0.24% 相对改善）在实际应用中意义有限，且方法在 ρ=0.2 失败、ρ=0.6 减弱、1.7B 消失 |\n| Reproducibility | 4.0 / 5 | 算法、超参、训练配置描述充分；代码承诺发布但尚未提供 |\n| Reviewer Confidence | 4 / 5 | 熟悉 importance weighting、LM pretraining 和统计推断 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 效应量极小，下游任务不支持 PPL 改善的实际意义\n\n- 具体位置：Table 1 (main results), Table 8 (downstream, Appendix D)\n- 问题：核心 PPL 改善为 0.043（17.694 → 17.651，0.24% 相对），发生在已被续训吸收 5.2 PPL 的\"残差\"区间内。更关键的是，Table 8 的下游评估显示 5 个 benchmark 中 4 个为负 Δ（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA 微正（+0.001）。sign-test p ≈ 0.19，suggestive but not significant。\n- 为什么影响接收：如果 PPL 改善无法转化为任何可测量的下游增益，那么方法的实际价值存疑。论文 §Limitations 承认\"the PPL improvement may partly reflect distribution matching (training data closer to the human-only evaluation set) rather than a generalizable quality gain\"，但这一关键限制被藏在 Limitations 而非 Results 或 Abstract 中。Abstract 和 Introduction 的 framing 给出了比实际证据更强的印象。\n- 建议修改方向：(1) 在 Results 正文中报告下游结果（而非仅 Appendix），并诚实讨论 PPL-downstream 脱节；(2) 多 seed 下游评估以判断趋势是否稳定；(3) 考虑在 Abstract 中明确 PPL 改善的局限性。\n\n**N2** [critical] 1.7B \"transfers without degradation\" 的 claim 缺乏统计支撑\n\n- 具体位置：§5.2 (Scale and detector signal), §Conclusion, §Limitations\n- 问题：1.7B 结果基于 2 seeds（13.25, 13.27），uniform baseline 仅 1 seed（13.26）。Δ = -0.01 在任何标准下都无法区分 noise 和 signal。2 个数据点无法计算有意义的 CI 或 p-value。论文 Conclusion 称\"the advantage observed at 0.6B does not amplify\"，但实际上连\"advantage 是否存在\"都无法判断。\n- 为什么影响接收：这是三个 Contribution 的实验基础之一。如果 1.7B 结果不可靠，method 的 scale transfer claim 就悬空了。\n- 建议修改方向：(1) 至少 3 seeds for both adaptive 和 uniform at 1.7B；(2) 或明确降级 claim 为 \"preliminary evidence\"，不在 Abstract/Conclusion 中作为 contribution。\n\n**N3** [critical] \"competitive with grid-best\" 的 framing 与 CI 不一致\n\n- 具体位置：Abstract, §5.1, §Conclusion\n- 问题：95% CI of gap 为 [-0.039, 0.101]。这意味着自适应方法可能比 grid-best 差 0.101 PPL，而 grid-best 自身的 cross-seed 标准差为 ±0.033。Abstract 称 \"the gap (0.031 PPL) falls within grid-search's own cross-seed variance (±0.033)\"，但这种比较混淆了两个不同的统计量：gap 的 CI 是 paired variability 的函数，cross-seed variance 是 marginal variability。CI 包含 0 本身不构成等价性证据——N=3 下 CI 过宽是 power 不足的结果，不是等价性的证明。\n- 论文 §5.1 确实写了 \"we refrain from claiming statistical indistinguishability\"，但 Abstract 和 Conclusion 的措辞隐含了等价性 claim。\n- 为什么影响接收：核心 claim 的统计逻辑不成立。\n- 建议修改方向：(1) Abstract 中明确 CI 包含降级的可能性；(2) 增加 seeds 以缩窄 CI；(3) 若无法增加 seeds，将 claim 明确为\"point estimate competitive, but wide CI prevents formal equivalence\"。\n\n**N4** [critical] Batch size B=4 下 α_eff 仅有 5 个离散值，bisection 搜索的意义存疑\n\n- 具体位置：§3.3 (Algorithm), §3.4 (Hyperparameters), Appendix F (α_eff Proxy Validation)\n- 问题：B=4 时，α_eff(0) 取值仅有 {0, 0.25, 0.5, 0.75, 1.0}。r_i ∈ {0,1} 的 4 个值之和除以 4，最多 5 种可能。这意味着 bisection 搜索 b_τ 使得 α_eff(b) = τ = 0.8 时，α_eff 作为 b 的函数是一个最多有 4 个跳跃点的阶梯函数。整个\"连续优化\"框架在 B=4 下退化为一个极粗粒度的离散选择。\n- Appendix Table 5 报告 Pearson r ≈ 0.70, MAE = 0.114。r=0.70 意味着 51% 的方差未被解释；MAE=0.114 意味着平均 11.4% 的估计误差。这对于一个声称提供\"quality floor\"的指标来说是相当粗糙的。\n- 论文辩称 \"PPL differs by <0.01 across B ∈ {4, 8, 16}\"，但这些实验的细节（多少 seeds？哪些 B 值实际测试了？）不够清楚。\n- 为什么影响接收：方法的核心机制——per-batch α_eff-driven b* selection——在实际使用的 batch size 下几乎丧失了设计中的连续性和精度。如果 B=4 和 B=16 的 PPL 差异 <0.01，且 B=4 下 α_eff 如此粗糙，那是否说明 per-batch adaptation 的价值主要不在于 α_eff 的精确值，而在于其他因素？这需要更深入的分析。\n- 建议修改方向：(1) 在方法 section 中明确讨论 B=4 下的离散化问题及其对 bisection 的影响；(2) 提供 B=8 和 B=16 的多 seed 结果以验证 robustness claim；(3) 分析 α_eff-binding 在不同 B 下的频率和 b* 分布变化。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 自污染设计（self-contamination）的生态效度有限\n\n- 具体位置：§4 (Experimental Setup), §Limitations\n- 问题：用 Qwen3-0.6B 生成合成数据再训练同模型，是一种特殊的自污染场景。真实 web 污染来自多种不同模型、不同大小、非均匀混合。论文的 cross-model 结果（Llama-3.2-3B generator, Appendix H）是单 seed 且结果 mixed（MMLU +1.57pp, HellaSwag -0.60pp），无法支撑泛化性。\n- 建议：(1) 至少测试一个\"强生成器 + 弱训练模型\"场景（如 GPT-4 生成 → 0.6B 训练）；(2) 或明确将 self-contamination 标注为主要假设限制。\n\n**W2** [warning] 132M tokens 的规模太小，结论的可迁移性未知\n\n- 具体位置：§4, §Limitations\n- 问题：132M tokens 对应 domain-adaptive continued pretraining，但论文动机和 introduction 讨论的是 web-scale 污染场景。方法在 1.7B 上已无 measurable advantage (Δ=-0.01)。论文 Conclusion 诚实地承认\"the method's primary value lies in the 0.6B continued pretraining regime tested here\"，但 Introduction 和 Abstract 的 framing 没有反映这一限制。\n- 建议：Introduction 中明确方法的目标场景是 continued pretraining（而非 from-scratch pretraining），并在 Abstract 中限定 scope。\n\n**W3** [warning] Epoch-matched 对比存在潜在混淆变量\n\n- 具体位置：§5.1 (Hard filtering and the epoch confound), Table 2\n- 问题：D&R epoch-matched 运行 2,533 步（vs. adaptive 6,103 步），以匹配约 1.0 content epoch。但两个实验的 cosine learning rate schedule 总长度不同（2,533 vs. 6,103 步），这意味着 warmup 比例和 decay 曲线不同。D&R epoch-matched 可能因为更短的 schedule 导致 under-optimization（更少的 gradient updates），也可能因为更快的 decay 受益。这个混淆变量未被讨论。\n- 更严格的设计是：两个方法使用相同总步数但不同 data pipeline（adaptive 看所有数据一次，D&R 过滤后用剩余数据填充到相同步数但不重复）。\n- 为什么重要：Contribution 2 的核心 claim——\"D&R's reported advantage over reweighting is entirely a multi-epoch artifact\"——依赖于这个 epoch-matched 设计的正确性。\n- 建议：(1) 讨论 LR schedule 差异对结果的潜在影响；(2) 或提供控制实验（相同步数 + 不同 data pipeline）。\n\n**W4** [warning] Grid search baseline 的公平性需要讨论\n\n- 具体位置：§4 (Methods), §5.1\n- 问题：Grid-$b$ 从 9 个值中 post-hoc 选最优，是一个 oracle baseline。实际使用中 grid search 需要 validation set 选择，且容易 overfit to validation distribution。论文正确标注了 \"post-hoc oracle\"，但比较的 fairness 需要更显式的讨论：\n  - 如果 grid search 用 validation set 选择（而非 post-hoc on test set），其 PPL 会更差\n  - 因此 adaptive 相对于\"实际可用的 grid search\"可能有更大优势\n- 这其实对论文有利，但目前的呈现方式没有充分利用这一点。\n- 建议：明确讨论 post-hoc vs. validation-based grid search 的区别，可能增加一个 validation-based grid search 结果作为更公平的 baseline。\n\n**W5** [warning] p < 0.01 (N=3) 的可信度和解释\n\n- 具体位置：§5.1, §5.2\n- 问题：N=3 的 paired t-test 只有 2 个自由度。p < 0.01 在数学上是可能的（paired differences 的 t 值足够大），但正态性假设在 N=3 下无法验证。论文使用 p-value 时应附带这一 caveat。此外，p < 0.01 at ρ=0.6 的报告方式给人以\"高度显著\"的印象，但在 N=3 下任何 p-value 都应持保留态度。\n- 建议：(1) 报告 exact paired differences 而非仅 p-value；(2) 注明 N=3 下 t-test p-value 应谨慎解读；(3) 考虑非参数检验（如 sign test）作为 robustness check。\n\n**W6** [warning] \"Minimum intervention\" 缺乏理论最优性证明\n\n- 具体位置：§3.2, §6 (Discussion)\n- 问题：选择 b* = b_τ（最小 b）而非 b_ESS（最大 b）或其他中间值，论文称之为 \"minimum intervention strategy\"，理由是\"borderline samples still carry useful training signal\"。这是一个合理的设计直觉，但不是定理。论文引用 wang2026survive 提供 α_eff ≥ τ 的动机，但 wang2026survive 假设已知 α，且未证明\"最小 b\"是最优的。\n- Empirically, ESS-only (maximum b) 确实更差，但这只排除了一个极端，不证明 minimum 是最优——例如 b* = (b_τ + b_ESS)/2 可能更好，论文没有测试。\n- 建议：(1) 测试 feasible region 中的其他选择策略（如 midpoint, geometric mean）；(2) 或明确标注 minimum intervention 是一个 heuristic，不是 optimal。\n\n---\n\n## 小问题（不影响接收）\n\n- §5.1: \"3-seed means: 17.651 vs. 17.620 for grid b=0.3 (gap 0.031, 95% CI [−0.039, 0.101])\"——应说明 CI 计算方法（paired t-based? bootstrap?）\n- Table 1: D&R full (q>0.5) 标注为 seed 42 only，但 D&R (q>0.3) 标注为 3 seeds；不同 D&R threshold 的 seed 数量不一致，增加了比较的复杂性\n- §3.4: \"We leave fine-grained ratio characterization (e.g., 0.4 vs. 0.6) to future work\"——考虑到 n_min 是核心超参之一，这一留白略显不足\n- Appendix Table 5: \"Spearman r=0.699\" 在正文 §3.3 中被引用为 \"sufficient variance within micro-batches\"，但 0.699 是否\"sufficient\"是主观判断\n- Abstract 中 \"eliminating the need for exhaustive search (nine runs to one; 95% CI of gap [−0.039, 0.101], which includes possible degradation)\" 这句话的后半部分削弱了前半部分的 claim，导致 Abstract 内部信息传达矛盾\n- §5.2 报告 ρ=0.6 时 Grid b=0.3 仅 seed 42 (17.634)，adaptive 三 seed mean 17.736——gap 扩大到 0.102。如果 grid 也是 3-seed 结果，gap 可能不同，这个比较不公平\n- Checklist E1 \"AI assistants were used for code development and manuscript drafting\" 可以更具体（哪些 AI、用于哪些部分）\n\n---\n\n## 主要优势\n\n1. **问题定义清晰，框架设计优雅**：将 b 的选择形式化为双约束优化，两个约束具有自然的对立单调性，这是一个比 grid search 更优雅的解决方案框架。\n2. **Epoch-matched 发现有独立价值**：证明 D&R 的优势来自多 epoch 暴露（而非 filtering 本身）是一个有意义的负面结果，对 community 有参考价值（§5.1, Table 2, Figure in Appendix）。\n3. **检测器类型发现是 novel 的**：discriminative vs. generative 检测器的差异（Table 9, §5.2）提供了关于 reweighting 何时有效的实践指导，这个发现比主方法本身可能更有影响。\n4. **诚实的 Limitations**：§Limitations 相当全面，覆盖了 scale, ρ range, detector coverage, τ, evaluation, effect size 等方面。许多问题在 Limitations 中已被承认。\n5. **写作质量较高**：论文结构清晰，Related Work 做了有效的 positioning（特别是与 Drayson et al. 2025 的三点区别），Algorithm 1 描述明确。\n\n---\n\n## 总结建议\n\n本文提出了一个设计清晰的框架，但实验证据系统性地弱于 claims。核心困境：方法在唯一充分测试的 setting（0.6B, ρ=0.4, 132M tokens）中效应量极小（0.24%），且无法转化为下游增益；在其他 settings（ρ=0.2, 1.7B, cross-model）中要么失败要么不可判断。建议增加实验规模（更多 seeds、更大模型、下游评估）后重投，或重新 framing 为一个聚焦于 epoch-matched 和 detector-type 发现的分析性贡献。\n",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-19T05:57:28.885510+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4063
}
```

</details>

---


### Assistant

_source line 160 · 2026-05-19T05:57:38.725205+00:00_

审稿意见已提交给 Review Director。

审稿核心判断：**Borderline Findings (2.5/5)**。

主要问题集中在四个 critical issues：
1. 效应量仅 0.043 PPL (0.24%)，下游 5 个 benchmark 中 4 个为负，PPL 改善可能是 distribution matching artifact
2. 1.7B "transfers without degradation" 仅 2 seeds，无法支撑 claim
3. "competitive with grid-best" 的 CI [-0.039, 0.101] 包含实质性降级，统计逻辑不成立
4. B=4 下 α_eff 仅 5 个离散值，核心机制的连续优化退化为粗粒度离散选择

主要优势在于框架设计优雅、epoch-matched 发现和 detector type 发现具有独立价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 161 · 2026-05-19T05:58:10.176981+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — Round 1 审稿意见

**Overall**: 3/5 (Findings)

### Must-Fix 问题

**N1** [critical] 与 Drayson et al. (2025) 的区分度不足以支撑 Main Conference 新颖性
- 论文使用与 Drayson et al. 完全相同的公式 w=(1-q)^b。全部创新在于 b 的选择方式。
- (i) per-batch vs fixed b：engineering improvement
- (ii) loss reweighting vs SIR resampling：实现层面差异
- (iii) lightweight detector suffices：实验发现而非方法贡献
- α_eff 约束来自 Wang et al. (2026) 的直接应用；ESS 约束是 IS 标准做法
- "Minimum intervention" 本质是在两个单调函数上做 bisection 取下界
- 建议重新 frame：将 D&R epoch confound 和 detector type 发现提升为主要贡献

**N2** [critical] 效果量极小，实际意义不明
- ρ=0.4: Δ=-0.043, 95% CI 包含退化
- ρ=0.6: Δ=-0.028
- 1.7B: Δ=-0.01 (negligible)
- Downstream: 4/5 benchmarks uniform 略优
- PPL 改进可能仅反映 distribution matching

**N3** [critical] 自污染实验设计严重限制泛化性
- Qwen3-0.6B 既是 generator 又是 trainee（self-contamination），检测最容易的场景
- Limitations 未讨论 self-contamination 限制
- Cross-generator 结果 (Llama-3.2-3B) mixed 且无 PPL 对比

### Should-Fix 问题

**W1** "D&R" 缩写在 Abstract/Introduction 中未定义
**W2** "robust defaults" 声明验证不足（τ safe range 基于单 seed, ρ=0.6 optimal shift 到 τ=0.7）
**W3** Grid search 在 ρ=0.6 为单 seed，Adaptive-vs-Grid gap (0.106) 不可靠
**W4** 缺少重要近期相关工作（Kang et al. EMNLP 2025, Zhang et al. 2025 ForTIFAI, Yi et al. 2025）
**W5** Downstream 评估不充分（5 benchmarks, single seed, 4/5 negative）
**W6** Micro-batch B=4 下 α_eff 仅 5 个离散值，bisection 退化为离散 lookup

### 主要优势
1. 诚实透明的 Limitations
2. D&R epoch confound 发现有独立社区价值
3. Detector type 发现有实用指导意义
4. 叙事完整性好
5. 写作干净无 AI 痕迹
6. 格式完全合规

---

请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-19T06:00:30.538117+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 与 Drayson et al. (2025) 的区分度不足**\n\n同意核心判断。论文采用完全相同的权重公式 w=(1-q)^b（§3.1, Eq.1），方法创新集中在 b 的选择方式上：(i) per-batch bisection 是工程层面的改进而非概念突破；(ii) α_eff ≥ τ 约束是 wang2026survive 收敛率结论的直接操作化（§3.2 line 66 明确承认 \"convergence under contaminated training improves with the effective real-data fraction\"）；(iii) ESS 约束是 importance sampling 领域的标准做法（§3.2 引用 kish1965survey, owen2013mc）。\n\n但我要补充：R2 的 reframing 建议（将 D&R epoch confound 和 detector type 发现提升为主要贡献）是建设性的，也与我的审稿意见一致。这两个发现的独立价值高于方法本身：\n\n- Epoch confound 发现（Table 2, §5.1）：D&R 全长 17.290 vs. epoch-matched 17.657，Δ=0.367 完全来自多 epoch——这对 community 有纠偏价值\n- Detector type 发现（Table 9, Appendix G）：GPT-2 PPL (AUC=0.91) 反而使 adaptive 退化 (+0.10)，证明 AUC 不是决定因素——这是一个 non-trivial 的实践指导\n\n如果论文重新定位为 \"analysis-driven contribution with a methodological tool\"，novelty 问题可能缓解。但当前 framing 将 dual-constraint framework 作为 Contribution 1（§1, contribution list），抬高了 novelty 预期。\n\n---\n\n**[AGREE] R2-N2: 效果量极小，实际意义不明**\n\n完全同意。这与我的 N1 判断一致。补充几个 R2 未展开的点：\n\n1. **PPL-downstream 脱节的严重性**：不仅是 4/5 benchmark 为负 Δ，而且方向一致（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA +0.001 例外（Table 8, Appendix D）。sign-test p ≈ 0.19 虽不显著，但一致的负方向 suggestive，论文将此归为 \"within standard error\" 有回避之嫌。\n\n2. **效应量的 context**：0.043 PPL 改善发生在 22.970 → 17.694 的 5.276 PPL 下降之后（Table 1），占总改善的 0.8%。方法在\"残差\"区间操作，实际效果被大幅稀释。\n\n3. **Conclusion 的自我矛盾**：§Conclusion 称 \"the method's primary value lies in the 0.6B continued pretraining regime tested here\"——如果连作者都承认 value 仅限于一个特定 regime，这对 general contribution claim 是致命的。\n\n---\n\n**[AGREE] R2-N3: 自污染实验设计限制泛化性**\n\n同意，且 R2 指出的 \"Limitations 未讨论 self-contamination\" 这一点是准确的。我核查了 §Limitations 的六个段落（Scale, Contamination range, Detector coverage, Threshold, Evaluation, Effect size），没有一个段落将 self-contamination 作为独立限制讨论。§Limitations 的 \"Scale and cross-model transfer\" 段落提到了 Llama-3.2-3B cross-model 结果，但这是关于 cross-model transfer 的，不是关于 self-contamination 设计本身的局限性。\n\n补充我的分析：\n\n- 论文 §4 声称 self-contamination \"creates a challenging detection scenario where generator and trainee share the same distribution\"，但这实际上是一个 **可控的** 场景——TF-IDF+LR 在此 setting 下达到 AUC=0.94（§4 detector paragraph），说明 self-contamination 并非特别困难\n- 真实 web 污染的关键挑战——**多源异构**（不同模型、不同 prompt 策略、不同时间段生成）、**非均匀混合**（特定 domain/topic 污染更重）——在 uniform random mixing 设计中完全缺失\n- Cross-generator 结果（Appendix H, Table 10）不仅 single seed 且 mixed results，还缺少 PPL 对比（\"Perplexity comparison omitted due to inconsistent evaluation configurations; checkpoints were not retained for re-evaluation\"），这是一个严重的实验管理疏忽\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"D&R\" 缩写未定义**\n\n确认。Abstract line 9 使用 \"D&R's full-length advantage\" 时无前置定义。Introduction contribution list（§1 line 30）同样直接使用 \"D&R's reported advantage\"。§4 的 Methods 部分（experiments.tex line 30）定义了 \"Detect & Remove\"，但这在 Abstract/Introduction 之后。对于 double-blind review，审稿人可能不熟悉这个缩写。\n\n---\n\n**[AGREE] R2-W2: \"robust defaults\" 验证不足**\n\n同意。τ sweep（Table 3, Appendix B）仅基于 seed 42, ρ=0.4。当 ρ 变化时，optimal τ 从 0.8 移动到 0.7（Figure 3, §5.2 line 90: \"A τ sweep at this level finds τ=0.7 optimal\"）。论文声称 \"τ ∈ [0.7, 0.8] performs well across tested ρ\"，但这仅基于两个 ρ 值（0.4, 0.6）且 τ=0.7 的数据仅来自 ρ=0.6 的实验。\n\n\"empirically robust defaults that transfer without per-model tuning\"（§5.4 最后一句）这个 claim 对于仅在一个模型（Qwen3-0.6B）的两个 ρ 值上验证的超参来说过强。\n\n---\n\n**[AGREE] R2-W3: Grid search 在 ρ=0.6 为单 seed**\n\n同意。Table 6（Appendix E）的 Grid (b=0.3) 在 ρ=0.6 标注为 \"seed 42 only\"。Adaptive 3-seed mean 17.736 vs. Grid 单 seed 17.634，gap 0.102 不具可比性。如果 Grid 在 ρ=0.6 也有 3-seed variance（如 ρ=0.4 的 ±0.033），真实 gap 可能显著缩窄或扩大。这使得 §5.2 中关于 \"Adaptive-vs-Grid gap widens from 0.013 at ρ=0.4 to 0.106 at ρ=0.6\" 的叙述不可靠。\n\n---\n\n**[AGREE with caveat] R2-W4: 缺少重要近期相关工作**\n\n原则上同意相关工作应完整覆盖。但我无法独立验证 R2 提到的三篇论文（Kang et al. EMNLP 2025, Zhang et al. 2025 ForTIFAI, Yi et al. 2025）的存在和相关性。如果这些论文确实存在且直接相关，应被引用。\n\n从论文当前引用来看（45 篇，覆盖 contamination、detection、data mixing、instance selection、theory 五个方向），引用密度合理。但如果 R2 提到的工作涉及 contamination-aware training 的替代方法，缺失会影响 positioning 的完整性。建议 R2 提供具体论文信息以便作者核实。\n\n---\n\n**[AGREE] R2-W5: Downstream 评估不充分**\n\n同意，与我的 N1 判断一致。5 benchmarks、single seed、4/5 negative Δ。论文将下游结果放在 Appendix 而非正文，且 framing 为 \"preserves downstream performance\"（Table 8 caption: \"adaptive reweighting preserves downstream performance\"）而非\"downstream results are inconclusive or mildly negative\"，这是对证据的 over-positive interpretation。\n\n---\n\n**[AGREE] R2-W6: B=4 下 α_eff 仅 5 个离散值**\n\n同意，与我的 N4 判断一致。补充：论文 §3.3 line 119-120 写道 \"we compute b* at the micro-batch level (B=4) rather than the effective batch (B=16 after gradient accumulation) because q-score statistics exhibit sufficient variance within micro-batches: Spearman r=0.699\"。但 Spearman r=0.699 是 α_eff(0) 与 true real fraction 的 rank correlation，不是 α_eff(b*) 与最优 b 之间的相关性。这两个量之间存在概念跳跃，论文未能 bridge。\n\n此外，当 α_eff(0) = 0.5 且 τ = 0.8 时，bisection 需要找 b 使得 α_eff 从 0.5 跳到 ≥ 0.8。但在 B=4 的阶梯函数上，这个 \"跳跃\" 发生在某个特定 b 值处，bisection 的精度（ε=0.01）远超函数本身的分辨率。这不影响正确性，但暴露了方法描述与实际操作之间的失配。\n\n---\n\n### 总体评价\n\nR2 的审稿意见整体准确，与我的独立评估高度一致。主要分歧在于定位：\n\n- R2 给了 3.0/5 (Findings)，我给了 2.5/5 (Borderline Findings)。差异主要来自我对效应量的权重更大——我认为 0.043 PPL 无下游转化是一个比 novelty 问题更根本的缺陷。即使 reframing 后 novelty 足够 Findings，效应量问题仍然存在。\n- 两位 reviewer 在以下问题上完全一致：(1) 效应量过小；(2) 1.7B 证据不足；(3) 自污染设计限制泛化；(4) B=4 离散化问题；(5) 下游评估不充分。这种独立一致性增强了这些问题的权重。\n",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 与 Drayson et al. (2025) 的区分度不足**\n\n同意核心判断。论文采用完全相同的权重公式 w=(1-q)^b（§3.1, Eq.1），方法创新集中在 b 的选择方式上：(i) per-batch bisection 是工程层面的改进而非概念突破；(ii) α_eff ≥ τ 约束是 wang2026survive 收敛率结论的直接操作化（§3.2 line 66 明确承认 \"convergence under contaminated training improves with the effective real-data fraction\"）；(iii) ESS 约束是 importance sampling 领域的标准做法（§3.2 引用 kish1965survey, owen2013mc）。\n\n但我要补充：R2 的 reframing 建议（将 D&R epoch confound 和 detector type 发现提升为主要贡献）是建设性的，也与我的审稿意见一致。这两个发现的独立价值高于方法本身：\n\n- Epoch confound 发现（Table 2, §5.1）：D&R 全长 17.290 vs. epoch-matched 17.657，Δ=0.367 完全来自多 epoch——这对 community 有纠偏价值\n- Detector type 发现（Table 9, Appendix G）：GPT-2 PPL (AUC=0.91) 反而使 adaptive 退化 (+0.10)，证明 AUC 不是决定因素——这是一个 non-trivial 的实践指导\n\n如果论文重新定位为 \"analysis-driven contribution with a methodological tool\"，novelty 问题可能缓解。但当前 framing 将 dual-constraint framework 作为 Contribution 1（§1, contribution list），抬高了 novelty 预期。\n\n---\n\n**[AGREE] R2-N2: 效果量极小，实际意义不明**\n\n完全同意。这与我的 N1 判断一致。补充几个 R2 未展开的点：\n\n1. **PPL-downstream 脱节的严重性**：不仅是 4/5 benchmark 为负 Δ，而且方向一致（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），仅 PIQA +0.001 例外（Table 8, Appendix D）。sign-test p ≈ 0.19 虽不显著，但一致的负方向 suggestive，论文将此归为 \"within standard error\" 有回避之嫌。\n\n2. **效应量的 context**：0.043 PPL 改善发生在 22.970 → 17.694 的 5.276 PPL 下降之后（Table 1），占总改善的 0.8%。方法在\"残差\"区间操作，实际效果被大幅稀释。\n\n3. **Conclusion 的自我矛盾**：§Conclusion 称 \"the method's primary value lies in the 0.6B continued pretraining regime tested here\"——如果连作者都承认 value 仅限于一个特定 regime，这对 general contribution claim 是致命的。\n\n---\n\n**[AGREE] R2-N3: 自污染实验设计限制泛化性**\n\n同意，且 R2 指出的 \"Limitations 未讨论 self-contamination\" 这一点是准确的。我核查了 §Limitations 的六个段落（Scale, Contamination range, Detector coverage, Threshold, Evaluation, Effect size），没有一个段落将 self-contamination 作为独立限制讨论。§Limitations 的 \"Scale and cross-model transfer\" 段落提到了 Llama-3.2-3B cross-model 结果，但这是关于 cross-model transfer 的，不是关于 self-contamination 设计本身的局限性。\n\n补充我的分析：\n\n- 论文 §4 声称 self-contamination \"creates a challenging detection scenario where generator and trainee share the same distribution\"，但这实际上是一个 **可控的** 场景——TF-IDF+LR 在此 setting 下达到 AUC=0.94（§4 detector paragraph），说明 self-contamination 并非特别困难\n- 真实 web 污染的关键挑战——**多源异构**（不同模型、不同 prompt 策略、不同时间段生成）、**非均匀混合**（特定 domain/topic 污染更重）——在 uniform random mixing 设计中完全缺失\n- Cross-generator 结果（Appendix H, Table 10）不仅 single seed 且 mixed results，还缺少 PPL 对比（\"Perplexity comparison omitted due to inconsistent evaluation configurations; checkpoints were not retained for re-evaluation\"），这是一个严重的实验管理疏忽\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"D&R\" 缩写未定义**\n\n确认。Abstract line 9 使用 \"D&R's full-length advantage\" 时无前置定义。Introduction contribution list（§1 line 30）同样直接使用 \"D&R's reported advantage\"。§4 的 Methods 部分（experiments.tex line 30）定义了 \"Detect & Remove\"，但这在 Abstract/Introduction 之后。对于 double-blind review，审稿人可能不熟悉这个缩写。\n\n---\n\n**[AGREE] R2-W2: \"robust defaults\" 验证不足**\n\n同意。τ sweep（Table 3, Appendix B）仅基于 seed 42, ρ=0.4。当 ρ 变化时，optimal τ 从 0.8 移动到 0.7（Figure 3, §5.2 line 90: \"A τ sweep at this level finds τ=0.7 optimal\"）。论文声称 \"τ ∈ [0.7, 0.8] performs well across tested ρ\"，但这仅基于两个 ρ 值（0.4, 0.6）且 τ=0.7 的数据仅来自 ρ=0.6 的实验。\n\n\"empirically robust defaults that transfer without per-model tuning\"（§5.4 最后一句）这个 claim 对于仅在一个模型（Qwen3-0.6B）的两个 ρ 值上验证的超参来说过强。\n\n---\n\n**[AGREE] R2-W3: Grid search 在 ρ=0.6 为单 seed**\n\n同意。Table 6（Appendix E）的 Grid (b=0.3) 在 ρ=0.6 标注为 \"seed 42 only\"。Adaptive 3-seed mean 17.736 vs. Grid 单 seed 17.634，gap 0.102 不具可比性。如果 Grid 在 ρ=0.6 也有 3-seed variance（如 ρ=0.4 的 ±0.033），真实 gap 可能显著缩窄或扩大。这使得 §5.2 中关于 \"Adaptive-vs-Grid gap widens from 0.013 at ρ=0.4 to 0.106 at ρ=0.6\" 的叙述不可靠。\n\n---\n\n**[AGREE with caveat] R2-W4: 缺少重要近期相关工作**\n\n原则上同意相关工作应完整覆盖。但我无法独立验证 R2 提到的三篇论文（Kang et al. EMNLP 2025, Zhang et al. 2025 ForTIFAI, Yi et al. 2025）的存在和相关性。如果这些论文确实存在且直接相关，应被引用。\n\n从论文当前引用来看（45 篇，覆盖 contamination、detection、data mixing、instance selection、theory 五个方向），引用密度合理。但如果 R2 提到的工作涉及 contamination-aware training 的替代方法，缺失会影响 positioning 的完整性。建议 R2 提供具体论文信息以便作者核实。\n\n---\n\n**[AGREE] R2-W5: Downstream 评估不充分**\n\n同意，与我的 N1 判断一致。5 benchmarks、single seed、4/5 negative Δ。论文将下游结果放在 Appendix 而非正文，且 framing 为 \"preserves downstream performance\"（Table 8 caption: \"adaptive reweighting preserves downstream performance\"）而非\"downstream results are inconclusive or mildly negative\"，这是对证据的 over-positive interpretation。\n\n---\n\n**[AGREE] R2-W6: B=4 下 α_eff 仅 5 个离散值**\n\n同意，与我的 N4 判断一致。补充：论文 §3.3 line 119-120 写道 \"we compute b* at the micro-batch level (B=4) rather than the effective batch (B=16 after gradient accumulation) because q-score statistics exhibit sufficient variance within micro-batches: Spearman r=0.699\"。但 Spearman r=0.699 是 α_eff(0) 与 true real fraction 的 rank correlation，不是 α_eff(b*) 与最优 b 之间的相关性。这两个量之间存在概念跳跃，论文未能 bridge。\n\n此外，当 α_eff(0) = 0.5 且 τ = 0.8 时，bisection 需要找 b 使得 α_eff 从 0.5 跳到 ≥ 0.8。但在 B=4 的阶梯函数上，这个 \"跳跃\" 发生在某个特定 b 值处，bisection 的精度（ε=0.01）远超函数本身的分辨率。这不影响正确性，但暴露了方法描述与实际操作之间的失配。\n\n---\n\n### 总体评价\n\nR2 的审稿意见整体准确，与我的独立评估高度一致。主要分歧在于定位：\n\n- R2 给了 3.0/5 (Findings)，我给了 2.5/5 (Borderline Findings)。差异主要来自我对效应量的权重更大——我认为 0.043 PPL 无下游转化是一个比 novelty 问题更根本的缺陷。即使 reframing 后 novelty 足够 Findings，效应量问题仍然存在。\n- 两位 reviewer 在以下问题上完全一致：(1) 效应量过小；(2) 1.7B 证据不足；(3) 自污染设计限制泛化；(4) B=4 离散化问题；(5) 下游评估不充分。这种独立一致性增强了这些问题的权重。\n",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-19T06:00:34.853393+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4315
}
```

</details>

---


### Assistant

_source line 164 · 2026-05-19T06:00:39.764176+00:00_

交叉回应已提交。对 R2 的 9 个问题全部标注 [AGREE]（W4 附带 caveat），核心一致点：效应量过小、1.7B 证据不足、自污染限制、B=4 离散化、下游评估不充分。主要分歧在 Overall 评分（我 2.5 vs R2 3.0），因为我对效应量无下游转化的权重更大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

42 recorded events


### User

_source line 165 · 2026-05-19T07:13:11.578921+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计分析**。

## Venue 信息
- 目标：EMNLP 2026（ARR May 2025 cycle，Findings track）
- Deadline：2026-05-25
- 页数限制：正文 8 页（不含 Limitations/Ethics/References）
- 模板：ACL style，`[review]` 模式
- 匿名：Double-blind

## 论文路径
- 主文件：`projects/provenance_weight_training/docs/paper/main.tex`
- 各 section 在 `docs/paper/sections/` 下：abstract.tex, introduction.tex, method.tex, experiments.tex, results.tex, discussion.tex, conclusion.tex, related_work.tex, limitations.tex, appendix.tex, checklist.tex
- 参考文献：`docs/paper/references.bib`

## 论文摘要
标题：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in LM Pretraining

核心内容：提出 dual-constrained adaptive exponent b* 用于 detect-and-reweight 方法中的权重指数选择。公式 w=(1-q)^b，q 为检测器合成概率。两个约束：α_eff(b)≥τ（quality floor）和 ESS(b)≥n_min（stability ceiling）。在 Qwen3-0.6B 上做 continued pretraining（132M FineWeb tokens，40% 合成污染，3 seeds）。三个主要发现：(1) D&R 优势是 multi-epoch artifact；(2) dual-constrained adaptive b* 改善 uniform（Δ=-0.043, p<0.003）；(3) 检测器信号类型（discriminative vs generative）比 AUC 更重要。

## 你的审查侧重

请重点审查以下方面：

1. **方法的数学严谨性**
   - dual-constraint 框架的理论基础是否扎实？
   - Proposition 1（α_eff 单调性）和 Proposition 2（ESS 单调性）的证明是否正确？
   - α_eff 作为真实数据比例的 proxy 的可靠性（Pearson r≈0.70, MAE=0.114）
   - b* 选择算法在 B=4（仅 5 个离散值）下的合理性

2. **实验设计的科学性**
   - 控制变量是否充分（3 seeds, contamination levels, model sizes）？
   - Epoch-matched comparison 的设计是否有混淆因素？
   - Grid search baseline 是 post-hoc oracle 的公平性
   - 统计检验在 N=3（2 df）下的可靠性
   - p < 0.003/0.01 在 N=3 下的可信度

3. **消融实验的完整性**
   - Adaptive vs ESS-only vs Uniform vs Random 的消融层次
   - τ 和 n_min 的 sensitivity analysis
   - 检测器类型实验的充分性（3 detectors from 2 families）

4. **可复现性**
   - 实验细节是否足以复现？
   - 代码/数据发布承诺

请输出完整审稿意见，包括：Summary, Strengths, Weaknesses（逐条编号 R1-W1, R1-W2...），Questions, Missing References, 以及按 1-5 分制的各维度评分（Soundness, Substance, Novelty, Clarity, Reproducibility, Overall）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-19T07:13:20.831436+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-19T07:13:20.831915+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-19T07:13:26.503901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-19T07:13:27.007440+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{hyperref}
20	
21	\newtheorem{proposition}{Proposition}
22	\newtheorem{definition}{Definition}
23	
24	\newcommand{\bstar}{b^*}
25	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
26	\newcommand{\nmin}{n_{\min}}
27	\newcommand{\btau}{b_{\tau}}
28	\newcommand{\bess}{b_{\mathrm{ESS}}}
29	
30	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in LM Pretraining}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	\input{sections/abstract}
39	\end{abstract}
40	
41	\section{Introduction}
42	\label{sec:intro}
43	\input{sections/introduction}
44	
45	\section{Related Work}
46	\label{sec:related}
47	\input{sections/related_work}
48	
49	\section{Method}
50	\label{sec:method}
51	\input{sections/method}
52	
53	\section{Experimental Setup}
54	\label{sec:experiments}
55	\input{sections/experiments}
56	
57	\section{Results}
58	\label{sec:results}
59	\input{sections/results}
60	
61	\section{Discussion}
62	\label{sec:discussion}
63	\input{sections/discussion}
64	
65	\section{Conclusion}
66	\label{sec:conclusion}
67	\input{sections/conclusion}
68	
69	\section*{Limitations}
70	\label{sec:limitations}
71	\input{sections/limitations}
72	
73	\input{sections/checklist}
74	
75	\bibliography{references}
76	
77	\appendix
78	\input{sections/appendix}
79	
80	\end{document}
81	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-19T07:13:27.007915+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-19T07:13:27.509784+00:00_

1	Detect-and-reweight methods suppress likely-synthetic samples during pretraining via $w(x) = (1-q(x))^b$, where $q(x)$ is a detector's synthetic probability.
2	Two questions are open: does hard filtering (Detect and Remove, D\&R) outperform soft reweighting, and how should $b$ be set without per-model grid search?
3	
4	We address both through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, 40\% synthetic contamination, 3 seeds).
5	First, D\&R's reported advantage is entirely a multi-epoch artifact: at equal content epochs, reweighting and D\&R differ by only 0.006 PPL ($N{=}3$).
6	Second, a dual-constrained adaptive exponent $b^*$ that selects the minimum $b$ satisfying a quality floor ($\alpha_{\mathrm{eff}}(b) \geq \tau$) and stability ceiling ($\mathrm{ESS}(b) \geq n_{\min}$) consistently improves over uniform weighting ($\Delta{=}{-}0.043$, $p{<}0.003$) and over maximizing $b$ to the ESS limit; adaptive $b^*$ performs comparably to grid-best in our experiments ($N{=}3$, 95\% CI of the gap includes possible degradation up to 0.10 PPL).
7	Third, detector signal type matters more than discrimination accuracy: two generative detectors (AUC up to 0.91) both reverse the advantage that a discriminative classifier (AUC\,=\,0.94) provides.
8	
9	The method fails at low contamination ($\rho{=}0.2$), establishing a clear applicability boundary.
10	These findings inform practical choices for contamination-aware continued pretraining.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-19T07:13:27.510256+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-19T07:13:28.012099+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, fundamental questions remain.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	How should $b$ be chosen, given that \citet{drayson2025detection} find optimal values vary from $b{=}10$ (GPT-2 124M) to $b{=}1$ (SmolLM 1.7B), requiring costly grid search?
8	What detector properties are necessary for effective reweighting?
9	
10	We address these through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters.
11	This scope, continued pretraining on moderate-scale corpora with known contamination~\citep{gururangan2020dont}, does not address from-scratch pretraining at web scale.
12	We formulate adaptive exponent selection as a dual-constrained problem: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to Kish's effective sample size $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
13	
14	Our contributions:
15	\begin{itemize}[nosep,leftmargin=*]
16	\item \textbf{Epoch confound in D\&R comparisons.}
17	D\&R at its post-hoc best threshold achieves PPL 17.250 at full training length.
18	Epoch-matched controls ($N{=}3$) that equalize cont
…[truncated 1437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-19T07:13:28.012592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-19T07:13:28.464644+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	The indicator $r_i = \mathbf{1}[q_i \leq 0.5]$ is a proxy for true provenance: $\alpha_{\mathrm{eff}}$ tracks the detector's estimate of the real fraction, not
…[truncated 9233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-19T07:13:28.515321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-19T07:13:29.418368+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.939, calibrated ECE\,=\,0.048 after temperature scaling with $T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.913) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
14	All main comparisons use three random seeds (42, 123, 456)
…[truncated 1547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-19T07:13:29.418810+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-19T07:13:29.921150+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.651, compared to 17.620 for grid $b{=}0.3$ (gap 0.031, 95\% CI $[-0.039, 0.101]$, which includes possible degradation).
8	With only $N{=}3$ seeds (2 degrees of freedom), normality of paired differences cannot be verified; we report exact per-seed gaps: 0.010, 0.064, 0.020.
9	The practical value is reducing search cost from nine full training runs to one~\citep{drayson2025detection}, with lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
10	The grid-best $b{=}0.3$ is a post-hoc oracle selected after observing all nine candidates; in practice, validation-based selection from the same grid would yield worse results due to the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}).
11	Using the mean of per-batch $\bstar$ ($\bar{b}^*{=}1.19$) as a fixed exponent yields PPL 17.693, comparable to uniform (17.694); per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (mean 17.803) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
15	ESS-only (mean $17.737 {\pm} 0.007$) uses $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
16	Only the dual-constrained adaptive method, which l
…[truncated 8746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-19T07:13:29.921527+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-19T07:13:30.373227+00:00_

1	\paragraph{Why minimum intervention works.}
2	The $\aeff$ quality constraint prevents 4.9$\times$ over-aggressive downweighting in 38.2\% of batches (\S\ref{sec:regime}), robust across contamination levels (33.4\% at $\rho{=}0.6$) and seeds (CV ${<}2\%$).
3	Using the aggregate mean $\bstar \approx 1.4$ as a fixed exponent yields PPL comparable to uniform (17.693 vs.\ 17.694), confirming per-batch adaptation is essential.
4	
5	\paragraph{Failure modes and applicability boundary.}
6	At $\rho{=}0.2$, the method degrades by $+$0.046 PPL (Appendix~\ref{app:rho02}): the detector's mean $q$-score drops to 0.393, yet $\aeff$-binding rises to 60.1\%, so the method actively intervenes on unreliable signal.
7	The same failure appears with generative detectors (GPT-2 PPL: $\Delta{=}{+}0.10$; N-gram PPL: $\Delta{=}{+}0.13$), which conflate predictability with provenance; when $q$-scores do not separate real from synthetic, the framework amplifies detector error.
8	Discriminative signal is required, and the effective range with $\tau{=}0.8$ is $\rho \geq 0.4$.
9	
10	\paragraph{PPL vs.\ downstream divergence.}
11	Downstream benchmarks at 0.6B show 4 of 5 tasks with small negative $\Delta$ ($p{\approx}0.19$, $N{=}5$, single seed); cross-model evaluation (Llama-3.2-3B, single seed) is similarly mixed (Appendix~\ref{app:downstream},~\ref{app:cross_model}).
12	The PPL gain may reflect distribution matching rather than generalizable quality improvement.
13	
14	\paragraph{Soft vs.\ hard filtering.}
15	At equal content epochs, D\&R ($17.657 \pm 0.006$) and adaptive $\bstar$ ($17.651 \pm 0.007$) are equivalent ($\Delta{=}0.006$, $N{=}3$); D\&R's full-length advantage (17.250 at $q{>}0.3$) requires ${\sim}$3.2$\times$ effective compute, and its U-shaped threshold curve is entirely a multi-epoch artifact (Figure~\ref{fig:dr_dual_curve}).
16	
17	\paragraph{$\tau$ and deployment.}
18	$\tau{=}0.8$ is validated at $\rho{=}0.4$ (single-seed sweep) and $\rho{=}0.6$ ($\tau{=}0.7$ is optimal ther
…[truncated 238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-19T07:13:30.474064+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-19T07:13:30.876576+00:00_

1	Our empirical analysis of contamination-aware reweighting in continued pretraining yields three findings.
2	First, D\&R's reported advantage over soft reweighting is entirely attributable to multi-epoch exposure; at equal content epochs ($N{=}3$), the two approaches differ by $\Delta{=}0.006$ PPL (Table~\ref{tab:epoch_match}).
3	Second, dual-constrained exponent selection with minimum intervention outperforms both uniform weighting and the ESS-only alternative ($\rho \in \{0.4, 0.6\}$), with the quality constraint preventing 4.9$\times$ over-aggressive downweighting; the adaptive-to-grid gap (0.031 PPL, 95\% CI $[-0.039, 0.101]$) falls within grid-search's cross-seed variance, reducing search from nine runs to one.
4	Third, detector signal type (discriminative vs.\ generative), not AUC, determines effectiveness.
5	The method fails at $\rho{=}0.2$, and at 1.7B we find no evidence of improvement or degradation ($\Delta{=}{-}0.01$, 2 seeds), suggesting its value lies in moderate-scale continued pretraining.
6	Future work: multi-seed scale experiments, discriminative detector characterization, and evaluation on naturally contaminated corpora. Code and data will be released upon acceptance.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-19T07:13:30.877066+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-19T07:13:31.330174+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\
…[truncated 5528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-19T07:13:31.330539+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-19T07:13:31.832591+00:00_

1	\paragraph{Self-contamination.}
2	All main experiments use self-contamination (generator = trainee), which does not represent realistic web contamination from multiple models and sources.
3	The resulting AUC of 0.94 reflects that self-generated text is relatively easy to detect; real multi-source contamination may yield lower detection accuracy, shifting the operating regime.
4	Cross-model results (Llama-3.2-3B generator, Appendix~\ref{app:cross_model}) are single-seed and lack PPL evaluation, providing insufficient evidence for generalization beyond self-contamination.
5	
6	\paragraph{Scale.}
7	All main experiments use Qwen3-0.6B with batch size 4 on 132--200M tokens, comparable to domain-adaptive continued pretraining but far below full pretraining scale; validation at ${>}$100B tokens remains an important direction.
8	Preliminary evidence at 1.7B (Qwen3-1.7B, $\rho{=}0.4$, 2 seeds) shows $\Delta{=}{-}0.01$ (adaptive 13.26 vs.\ uniform 13.26); with only 2 seeds, this is insufficient for statistical conclusions about scale transfer.
9	
10	\paragraph{Contamination range.}
11	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative), indicating an effective range of $\rho \geq 0.4$ with $\tau{=}0.8$.
12	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
13	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
14	
15	\paragraph{Detector coverage.}
16	Three detectors have been tested: TF-IDF+LR (discriminative, AUC\,=\,0.94) succeeds, while GPT-2 perplexity (generative, AUC\,=\,0.91) and N-gram perplexity (generative, AUC\,=\,0.73) both fail.
17	The pattern suggests discriminative signal is necessary, but three detectors from two families cannot distinguish a type effect from a calibration effect; testing additional discriminative detectors at varying 
…[truncated 1534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-19T07:13:31.833039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-19T07:13:32.285247+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right)
20	  = \pi_i \!\left(\ln(1{-}q_i) - \sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	By construction, real samples ($r_i = 1$) have $q_i \leq 0.5$ and thus higher $\ln(1{-}q_i)$ than synthetic samples ($r_i = 0$, $q_i > 0.5$).
29	The weighted covariance $\mathrm{Cov}_{\pi}(r_i, \ln(1{-}q_i))$ is therefore non-negative, establishing that $\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$.
30	\end{proof}
31	
32	\begin{proposition}[ESS monotonicity]
33	\label{prop:ess_mono}
34	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
35	\end{proposition}
36	
37	\begin{proof}
38	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
39	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
40	Differentiating $H$ with respect to $b$:
41	\begin{equation*}
42	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \math
…[truncated 16519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-19T07:13:32.285868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-19T07:13:33.239616+00:00_

1	% Responsible NLP Research Checklist
2	% https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A. For Every Submission}
7	
8	\begin{itemize}[nosep,leftmargin=*]
9	\item[\checkmark] \textbf{A1.} Did you describe the limitations of your work?
10	\textit{Yes, \S\ref{sec:limitations} discusses scale, contamination range, detector coverage, threshold, evaluation, and effect size limitations.}
11	
12	\item[\checkmark] \textbf{A2.} Did you discuss any potential risks of your work?
13	\textit{Yes. The method assumes a pre-trained detector is available; deploying it with a poorly calibrated detector could degrade training quality (discussed in \S\ref{sec:limitations}, Detector coverage). The method does not generate new content or enable harmful uses beyond standard language model pretraining.}
14	\end{itemize}
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\checkmark] \textbf{B1.} Did you cite the creators of artifacts you used?
20	\textit{Yes. FineWeb~\citep{penedo2024fineweb}, Qwen3~\citep{yang2025qwen3}, and all baseline methods are cited in \S\ref{sec:experiments} and \S\ref{sec:related}.}
21	
22	\item[\checkmark] \textbf{B2.} Did you discuss the license or terms for use and/or distribution of any artifacts?
23	\textit{FineWeb is released under Apache-2.0; Qwen3 under Apache-2.0. Our code and data will be released upon acceptance.}
24	
25	\item[\checkmark] \textbf{B3.} Did you discuss if your use of existing artifacts was consistent with their intended use?
26	\textit{Yes. FineWeb is intended for language model training; we use it as a pretraining corpus. Qwen3 is used for both continued pretraining and synthetic data generation, consistent with its general-purpose design.}
27	
28	\item[\checkmark] \textbf{B4.} Did you discuss the steps taken to check whether the data contains information that names or uniquely identifies individ
…[truncated 3080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-19T07:13:33.240000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-19T07:13:33.240334+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@inproceedings{kang2025demystifying,
5	  title={Demystifying Synthetic Data in {LLM} Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls},
6	  author={Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Chen, Hongliang and Zhu, Yiming and Chen, Zijian and Liu, Mohan and Liu, Jingcheng and Liu, Haoran and Han, Song},
7	  booktitle={EMNLP},
8	  year={2025}
9	}
10	
11	@article{zibakhsh2025fortifai,
12	  title={{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse},
13	  author={Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koushanfar, Farinaz},
14	  journal={arXiv preprint arXiv:2509.08972},
15	  year={2025}
16	}
17	
18	@article{yi2025escaping,
19	  title={Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
20	  author={Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
21	  journal={arXiv preprint arXiv:2510.16657},
22	  year={2025}
23	}
24	
25	@article{drayson2025detection,
26	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
27	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
28	  journal={arXiv preprint arXiv:2502.15654},
29	  year={2025}
30	}
31	
32	@article{he2025golden,
33	  title={Golden Ratio Weighting Prevents Model Collapse},
34	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
35	  journal={arXiv preprint arXiv:2502.18049},
36	  year={2025}
37	}
38	
39	@article{wang2026survive,
40	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
41	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
42	  journal={arXiv preprint arXiv:2602.16065},
43	  year={2026}
44	}
45	
46	@article{shumailov2024model,
47	  title={{AI} 
…[truncated 12117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-19T07:13:33.391232+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-19T07:13:41.215293+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

I found relevant information about ACL ARR reviewer guidelines for 2025-2026. Here's what the search results show:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. 

The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scoring

The ARR 
…[truncated 1020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7824
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-19T07:13:47.268046+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, score ranges, and descriptions for each dimension. I need the exact scoring scale for soundness, excitement, overall recommendation, and any other scored dimensions. Include the exact numeric scale and what each score level means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, score ranges, and descriptions for each dimension. I need the exact scoring scale for soundness, excitement, overall recommendation, and any other scored dimensions. Include the exact numeric scale and what each score level means."
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-19T07:13:52.939135+00:00_

# ARR Review Form Scoring Dimensions

Based on the ARR Reviewer Guidelines, the document explicitly mentions three scoring dimensions but does not provide the complete numeric scales or detailed level descriptions:

## Documented Scoring Dimensions

**1. Soundness**
The guidelines state reviewers provide "soundness" scores that "must be justified by the text of the review." However, the specific numeric range and level definitions are not included in this document.

**2. Excitement**
Described as a "separate _excitement_ score, which is orthogonal to the assessment of the soundness of the paper." The guidelines note this reflects "personal taste" and doesn't require explicit justification. The numeric scale is not detailed here.

**3. Overall Assessment/Recommendation**
Characterized as "an explicit recommendation for the outcome of this paper, if it were committed to an \*ACL venue." The guidelines explain it's "a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact," but specific score levels aren't enumerated.

## Key Limitation

The document states: "Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation." However, the actual numeric scales (e.g., 1-5, 1-10) and what each level represents are not included in these guidelines. For complete scoring specifications, you would need to consult the actual ARR review form itself or related documentation referenced in the guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5671
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-19T07:13:56.753206+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement score scale 1-5 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement score scale 1-5 2025"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-19T07:14:03.328072+00:00_

Web search results for query: "ACL ARR review form soundness excitement score scale 1-5 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about the ACL ARR (ACL Rolling Review) review form for soundness and excitement scores:

## Scoring Overview

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score Scale (1-5)

The soundness score evaluates whether the paper is technically sound. The scale includes:
- 5 = Excellent: This study is one of the most thorough I have seen, given its type.
- 4 = Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.
- 3 = Acceptable: This study provides sufficient support for its main claims.

The soundness scores must be justified by 
…[truncated 756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6574
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-19T07:14:07.594654+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact numeric scales, and the description for each score level. I need soundness (1-5), excitement (1-5), overall recommendation, confidence, and any other scored fields with their complete scale definitions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact numeric scales, and the description for each score level. I need soundness (1-5), excitement (1-5), overall recommendation, confidence, and any other scored fields with their complete scale definitions."
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-19T07:14:12.985520+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence (1-5)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness (1-5)
- **5**: "This study is one of the most thorough I have seen, given its type."
- **4**: "This study provides sufficient support for all of its claims."
- **3**: "This study provides sufficient support for its main claims."
- **2**: "Some of the main claims are not sufficiently supported."
- **1**: "This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5)
- **5**: "I would recommend this paper to others and/or attend its presentation."
- **4**: "I would mention this paper to others and/or make an effort to attend."
- **3**: "I might mention some points of this paper to others."
- **2**: "This paper does not resonate with me, but it might with others."
- **1**: "Does not resonate with me, and I don't think it would with others."

## Overall Assessment (1-5)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5390
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-19T07:14:19.446704+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-19T07:15:18.728294+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 48, \"total_citations\": 78, \"unique_cited_keys\": 48, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 35, \"online_not_found\": 6, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"kang2025demystifying\", \"type\": \"inproceedings\", \"title\": \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\", \"authors\": \"Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Ch...\", \"year\": \"2025\", \"venue\": \"EMNLP\"}, {\"key\": \"zibakhsh2025fortifai\", \"type\": \"article\", \"title\": \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\", \"authors\": \"Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koush...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.08972\"}, {\"key\": \"yi2025escaping\", \"type\": \"article\", \"title\": \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\", \"authors\": \"Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.16657\"}, {\"key\": \"drayson2025detection\", \"type\": \"article\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.15654\"}, {\"key\": \"he2025golden\", \"type\": \"article\", \"title\": \"Golden Ratio Weighting Prevents Model Collapse\", \"authors\": \"He, Hengzhi and Xu, Shirong and Cheng, Guang\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.18049\"}, {\"key\": \"wang2026survive\", \"type\": \"article\", \"title\": \"Can Generative Artificial Int
…[truncated 36275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 59281
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-19T07:18:38.479016+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）\n\n### 总体评分\n**Overall**: 3/5 (Findings acceptance)\n**一句话总结**: 论文提出了一个数学上清晰的 dual-constraint 框架，epoch confound 发现有价值，但效果量极小（0.24% relative PPL），统计检验在 N=3 下勉强可信，自污染实验设置的外部效度存疑，且下游任务未见改善。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claim 在特定实验条件下有支撑，但 N=3 统计功效不足、B=4 离散化严重、自污染设置限制了结论的一般性 |\n| Excitement | 3/5 | Epoch confound 发现有洞察力；但 adaptive method 实际效果极小，1.7B 无效，下游无改善 |\n| Overall | 3/5 | 分析工作扎实，诚实报告了失败模式，适合 Findings track；但 claim 范围与证据强度不匹配 |\n| Confidence | 4/5 | 仔细检查了数学证明和实验设计，熟悉相关文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**R1-W1** [critical] N=3 下的统计可靠性问题\n- 具体位置：Section 5.1, Table 1, 以及全文所有 p-value 报告\n- 问题：论文核心 claim 依赖 paired t-test with N=3 (2 df)。报告 p<0.003（Section 5.1: Adaptive vs Uniform）。按 per-seed gaps 0.044, 0.047, 0.040 计算，t(2)≈20.8，p 确实可达 0.002 左右，但这完全是因为 cross-seed variance 极低（σ=0.005 for Uniform, σ=0.007 for Adaptive）。问题在于：(a) 2 df 下无法验证正态性假设（论文自己在 Section 5.1 第8行承认 \"normality of paired differences cannot be verified\"）；(b) 三个 seed (42, 123, 456) 是否产生了足够的训练动态多样性？在 B=4 micro-batch、同一模型架构、同一数据上，seed 间差异可能系统性偏小；(c) 0.043 PPL 的效果量在 17.694 baseline 下仅为 0.24% relative improvement，远小于 pretrained→continued pretraining 的 5.2 PPL 下降。\n- 为什么影响接收：统计证据是论文方法有效性的唯一支撑。如果审稿人认为 N=3 的 t-test 不可靠，则核心 contribution 2 和 contribution 3 均缺乏可信的定量支持。\n- 建议修改方向：(1) 增加至少 5-8 seeds 以获得合理的 df；(2) 使用 permutation test 或 bootstrap CI 替代 parametric t-test；(3) 报告 effect size（Cohen's d）以补充 p-value。\n\n**R1-W2** [critical] B=4 micro-batch 使 dual-constraint 框架退化为粗糙离散查表\n- 具体位置：Section 3.3（Algorithm 1）, Appendix E（Table 9）\n- 问题：论文用连续数学描述了一个优雅的 dual-constraint 优化问题（Eq. 4: bisection on α_eff and ESS），但实际运行在 B=4 上，α_eff 仅取 {0, 0.25, 0.5, 0.75, 1.0} 五个离散值。bisection 本质上在搜索一个阶梯函数的跳变点，不是连续优化。以 τ=0.8 为例：仅当 batch 中 4 个样本全部满足 q_i ≤ 0.5 时 α_eff(0)=1.0≥0.8（clean batch，~2%）；3/4 满足时 α_eff(0)=0.75<0.8，需要通过增大 b 将 α_eff 推到 0.8，这相当于一个固定的离散决策规则。Section 3.3 最后一段承认 \"PPL differs by <0.01 across B∈{4,8,16}\"，说明 B=4 的离散化并未造成 PPL 损失，但这恰恰削弱了 continuous dual-constraint 框架的必要性论证。\n- 为什么影响接收：方法论文的数学框架与实际实现之间存在显著落差。审稿人可能质疑：如果 B=4 下的离散规则已经足够好，那么 bisection 算法和 monotonicity proofs 的贡献是什么？\n- 建议修改方向：(1) 在 B=16 或 B=32 上展示 dual-constraint 的连续特性确实优于简单的离散规则（如 if α_eff(0)<τ then b=fixed_value）；(2) 明确论文的 contribution 是框架本身（可迁移到大 batch）还是在 B=4 下的具体效果。\n\n**R1-W3** [critical] 自污染实验设计的外部效度严重不足\n- 具体位置：Section 4（Experimental Setup），Limitations 第1段\n- 问题：generator = trainee（Qwen3-0.6B 生成合成数据用于 Qwen3-0.6B continued pretraining）。自污染使检测变得人为简单（TF-IDF+LR 即可达 AUC=0.94），且生成数据的分布与训练数据高度相似。真实 web 污染来自多种模型（GPT-4, Claude, Gemini 等）、多种提示策略、多种文本类型。论文的跨模型实验（Appendix G, Table 10: Llama-3.2-3B as generator）仅为 single-seed、无 PPL 评估（\"Perplexity comparison omitted due to inconsistent evaluation configurations; checkpoints were not retained for re-evaluation\"），不足以论证泛化。\n- 为什么影响接收：如果方法仅在自污染条件下有效，其实际应用价值存疑。Self-contamination 是最容易处理的污染形式；web-scale 场景下 AUC 可能大幅下降，进入论文自己定义的\"failure mode\"区间。\n- 建议修改方向：(1) 至少补充 1-2 个 cross-model 污染条件下的完整实验（含多 seed PPL）；(2) 如无法补充，需要在 Abstract 和 Introduction 中将 scope 限定为 self-contamination continued pretraining，而非泛称 \"contamination-aware continued pretraining\"。\n\n**R1-W4** [critical] 下游任务无改善，PPL 增益可能只是分布匹配\n- 具体位置：Appendix D（Table 8），Discussion 第3段\n- 问题：Table 8 显示 Adaptive 在 5 个下游任务中有 4 个比 Uniform 差（ARC-C: -0.005, ARC-E: -0.007, HellaSwag: -0.005, WinoGrande: -0.008），仅 PIQA 微好（+0.001）。虽在标准误内，但方向一致性 (4/5 negative) 令人担忧。Discussion 第3段承认 \"The PPL gain may reflect distribution matching rather than generalizable quality improvement\"。如果 PPL 改善仅因为 reweighting 使训练分布更接近 human-only evaluation set（本身就是 FineWeb 子集），这不代表模型质量的真实提升。\n- 为什么影响接收：论文的核心 metric（PPL improvement）可能不反映真实效用。4/5 下游任务下降虽不显著，但系统性方向一致，削弱了 \"practical tool\" 的定位。\n- 建议修改方向：(1) 在多 seed 下做下游评估（目前仅 seed 42）；(2) 在非 FineWeb 来源的 held-out set 上评估 PPL；(3) 如果确认是分布匹配效应，需要在 Abstract/Conclusion 中明确这一限制。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**R1-W5** [warning] Epoch-matched 对比存在 learning rate schedule 混淆\n- 具体位置：Table 2 footnote，Section 5.1 最后一段\n- 问题：Epoch-matched D&R 训练 2,533 步但使用为 6,103 步设计的 cosine schedule。论文认为 \"this confound, if anything, favors D&R (warmer LR)\"。但这是一个未控制的混淆因素。\n- 建议：补充一组 schedule-matched 对比。\n\n**R1-W6** [warning] τ 选择本身需要调参，\"zero validation cost\" claim 过强\n- 具体位置：Section 3.4, Section 5.4 (Table 6)\n- 问题：τ=0.8 是通过 single-seed sweep 选出的，且最优 τ 在 ρ=0.6 下移至 0.7。论文声称方法 \"eliminates grid search (nine runs to one)\"，但 τ sweep 本身是另一种 grid search（6 个值）。\n- 建议：弱化 \"zero validation cost\" 的措辞。\n\n**R1-W7** [warning] \"Detector signal type > AUC\" 的结论基于过少样本\n- 具体位置：Section 5.2 最后一段，Appendix F（Table 7）\n- 问题：3 个检测器（1 discriminative, 2 generative）不足以分离 type effect 和 calibration effect。\n- 建议：增加检测器数量或弱化 claim 措辞。\n\n**R1-W8** [warning] 1.7B 结果削弱贡献的实用性\n- 具体位置：Section 5.2 第1段\n- 问题：Qwen3-1.7B 上 Δ=-0.01，仅 2 seeds，方法在稍大模型上已无可见效果。\n- 建议：在 Discussion 和 Conclusion 中更明确地界定有效范围。\n\n---\n\n### 小问题\n- Section 3.3: 连续数学描述与 B=4 离散实现的 tension 需更早提及\n- Table 1: Golden Ratio 和 D&R 部分仅 seed 42，可比性受限\n- Appendix G: \"checkpoints were not retained\" 降低可复现性\n- references.bib: vehtari2024psis 年份标注 2024，OpenAlex 匹配到 2015\n\n### Questions\nQ1. 在 B=4 下，能否展示简单离散规则与 dual-constraint bisection 的 PPL 差异？\nQ2. 在 effective batch (B=16) 上计算 α_eff 和 ESS 会如何？\nQ3. 0.043 PPL improvement 在实际应用中对应什么级别的下游影响？\nQ4. wang2026survive 的 convergence guarantee 在 proxy quality r≈0.70 下有多少可用 slack？\n\n### 主要优势\n1. Epoch confound 发现具有独立价值（Section 5.1, Table 2, Figure 3）\n2. 数学框架清晰完整，Proposition 1/2 证明正确\n3. 诚实的效果报告（失败模式、95% CI 包含 degradation、下游略差）\n4. 消融层次完整且跨 ρ 一致\n5. Related Work 组织良好，positioning 清晰",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）\n\n### 总体评分\n**Overall**: 3/5 (Findings acceptance)\n**一句话总结**: 论文提出了一个数学上清晰的 dual-constraint 框架，epoch confound 发现有价值，但效果量极小（0.24% relative PPL），统计检验在 N=3 下勉强可信，自污染实验设置的外部效度存疑，且下游任务未见改善。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claim 在特定实验条件下有支撑，但 N=3 统计功效不足、B=4 离散化严重、自污染设置限制了结论的一般性 |\n| Excitement | 3/5 | Epoch confound 发现有洞察力；但 adaptive method 实际效果极小，1.7B 无效，下游无改善 |\n| Overall | 3/5 | 分析工作扎实，诚实报告了失败模式，适合 Findings track；但 claim 范围与证据强度不匹配 |\n| Confidence | 4/5 | 仔细检查了数学证明和实验设计，熟悉相关文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**R1-W1** [critical] N=3 下的统计可靠性问题\n- 具体位置：Section 5.1, Table 1, 以及全文所有 p-value 报告\n- 问题：论文核心 claim 依赖 paired t-test with N=3 (2 df)。报告 p<0.003（Section 5.1: Adaptive vs Uniform）。按 per-seed gaps 0.044, 0.047, 0.040 计算，t(2)≈20.8，p 确实可达 0.002 左右，但这完全是因为 cross-seed variance 极低（σ=0.005 for Uniform, σ=0.007 for Adaptive）。问题在于：(a) 2 df 下无法验证正态性假设（论文自己在 Section 5.1 第8行承认 \"normality of paired differences cannot be verified\"）；(b) 三个 seed (42, 123, 456) 是否产生了足够的训练动态多样性？在 B=4 micro-batch、同一模型架构、同一数据上，seed 间差异可能系统性偏小；(c) 0.043 PPL 的效果量在 17.694 baseline 下仅为 0.24% relative improvement，远小于 pretrained→continued pretraining 的 5.2 PPL 下降。\n- 为什么影响接收：统计证据是论文方法有效性的唯一支撑。如果审稿人认为 N=3 的 t-test 不可靠，则核心 contribution 2 和 contribution 3 均缺乏可信的定量支持。\n- 建议修改方向：(1) 增加至少 5-8 seeds 以获得合理的 df；(2) 使用 permutation test 或 bootstrap CI 替代 parametric t-test；(3) 报告 effect size（Cohen's d）以补充 p-value。\n\n**R1-W2** [critical] B=4 micro-batch 使 dual-constraint 框架退化为粗糙离散查表\n- 具体位置：Section 3.3（Algorithm 1）, Appendix E（Table 9）\n- 问题：论文用连续数学描述了一个优雅的 dual-constraint 优化问题（Eq. 4: bisection on α_eff and ESS），但实际运行在 B=4 上，α_eff 仅取 {0, 0.25, 0.5, 0.75, 1.0} 五个离散值。bisection 本质上在搜索一个阶梯函数的跳变点，不是连续优化。以 τ=0.8 为例：仅当 batch 中 4 个样本全部满足 q_i ≤ 0.5 时 α_eff(0)=1.0≥0.8（clean batch，~2%）；3/4 满足时 α_eff(0)=0.75<0.8，需要通过增大 b 将 α_eff 推到 0.8，这相当于一个固定的离散决策规则。Section 3.3 最后一段承认 \"PPL differs by <0.01 across B∈{4,8,16}\"，说明 B=4 的离散化并未造成 PPL 损失，但这恰恰削弱了 continuous dual-constraint 框架的必要性论证。\n- 为什么影响接收：方法论文的数学框架与实际实现之间存在显著落差。审稿人可能质疑：如果 B=4 下的离散规则已经足够好，那么 bisection 算法和 monotonicity proofs 的贡献是什么？\n- 建议修改方向：(1) 在 B=16 或 B=32 上展示 dual-constraint 的连续特性确实优于简单的离散规则（如 if α_eff(0)<τ then b=fixed_value）；(2) 明确论文的 contribution 是框架本身（可迁移到大 batch）还是在 B=4 下的具体效果。\n\n**R1-W3** [critical] 自污染实验设计的外部效度严重不足\n- 具体位置：Section 4（Experimental Setup），Limitations 第1段\n- 问题：generator = trainee（Qwen3-0.6B 生成合成数据用于 Qwen3-0.6B continued pretraining）。自污染使检测变得人为简单（TF-IDF+LR 即可达 AUC=0.94），且生成数据的分布与训练数据高度相似。真实 web 污染来自多种模型（GPT-4, Claude, Gemini 等）、多种提示策略、多种文本类型。论文的跨模型实验（Appendix G, Table 10: Llama-3.2-3B as generator）仅为 single-seed、无 PPL 评估（\"Perplexity comparison omitted due to inconsistent evaluation configurations; checkpoints were not retained for re-evaluation\"），不足以论证泛化。\n- 为什么影响接收：如果方法仅在自污染条件下有效，其实际应用价值存疑。Self-contamination 是最容易处理的污染形式；web-scale 场景下 AUC 可能大幅下降，进入论文自己定义的\"failure mode\"区间。\n- 建议修改方向：(1) 至少补充 1-2 个 cross-model 污染条件下的完整实验（含多 seed PPL）；(2) 如无法补充，需要在 Abstract 和 Introduction 中将 scope 限定为 self-contamination continued pretraining，而非泛称 \"contamination-aware continued pretraining\"。\n\n**R1-W4** [critical] 下游任务无改善，PPL 增益可能只是分布匹配\n- 具体位置：Appendix D（Table 8），Discussion 第3段\n- 问题：Table 8 显示 Adaptive 在 5 个下游任务中有 4 个比 Uniform 差（ARC-C: -0.005, ARC-E: -0.007, HellaSwag: -0.005, WinoGrande: -0.008），仅 PIQA 微好（+0.001）。虽在标准误内，但方向一致性 (4/5 negative) 令人担忧。Discussion 第3段承认 \"The PPL gain may reflect distribution matching rather than generalizable quality improvement\"。如果 PPL 改善仅因为 reweighting 使训练分布更接近 human-only evaluation set（本身就是 FineWeb 子集），这不代表模型质量的真实提升。\n- 为什么影响接收：论文的核心 metric（PPL improvement）可能不反映真实效用。4/5 下游任务下降虽不显著，但系统性方向一致，削弱了 \"practical tool\" 的定位。\n- 建议修改方向：(1) 在多 seed 下做下游评估（目前仅 seed 42）；(2) 在非 FineWeb 来源的 held-out set 上评估 PPL；(3) 如果确认是分布匹配效应，需要在 Abstract/Conclusion 中明确这一限制。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**R1-W5** [warning] Epoch-matched 对比存在 learning rate schedule 混淆\n- 具体位置：Table 2 footnote，Section 5.1 最后一段\n- 问题：Epoch-matched D&R 训练 2,533 步但使用为 6,103 步设计的 cosine schedule。论文认为 \"this confound, if anything, favors D&R (warmer LR)\"。但这是一个未控制的混淆因素。\n- 建议：补充一组 schedule-matched 对比。\n\n**R1-W6** [warning] τ 选择本身需要调参，\"zero validation cost\" claim 过强\n- 具体位置：Section 3.4, Section 5.4 (Table 6)\n- 问题：τ=0.8 是通过 single-seed sweep 选出的，且最优 τ 在 ρ=0.6 下移至 0.7。论文声称方法 \"eliminates grid search (nine runs to one)\"，但 τ sweep 本身是另一种 grid search（6 个值）。\n- 建议：弱化 \"zero validation cost\" 的措辞。\n\n**R1-W7** [warning] \"Detector signal type > AUC\" 的结论基于过少样本\n- 具体位置：Section 5.2 最后一段，Appendix F（Table 7）\n- 问题：3 个检测器（1 discriminative, 2 generative）不足以分离 type effect 和 calibration effect。\n- 建议：增加检测器数量或弱化 claim 措辞。\n\n**R1-W8** [warning] 1.7B 结果削弱贡献的实用性\n- 具体位置：Section 5.2 第1段\n- 问题：Qwen3-1.7B 上 Δ=-0.01，仅 2 seeds，方法在稍大模型上已无可见效果。\n- 建议：在 Discussion 和 Conclusion 中更明确地界定有效范围。\n\n---\n\n### 小问题\n- Section 3.3: 连续数学描述与 B=4 离散实现的 tension 需更早提及\n- Table 1: Golden Ratio 和 D&R 部分仅 seed 42，可比性受限\n- Appendix G: \"checkpoints were not retained\" 降低可复现性\n- references.bib: vehtari2024psis 年份标注 2024，OpenAlex 匹配到 2015\n\n### Questions\nQ1. 在 B=4 下，能否展示简单离散规则与 dual-constraint bisection 的 PPL 差异？\nQ2. 在 effective batch (B=16) 上计算 α_eff 和 ESS 会如何？\nQ3. 0.043 PPL improvement 在实际应用中对应什么级别的下游影响？\nQ4. wang2026survive 的 convergence guarantee 在 proxy quality r≈0.70 下有多少可用 slack？\n\n### 主要优势\n1. Epoch confound 发现具有独立价值（Section 5.1, Table 2, Figure 3）\n2. 数学框架清晰完整，Proposition 1/2 证明正确\n3. 诚实的效果报告（失败模式、95% CI 包含 degradation、下游略差）\n4. 消融层次完整且跨 ρ 一致\n5. Related Work 组织良好，positioning 清晰",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-19T07:18:42.394033+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Assistant

_source line 206 · 2026-05-19T07:18:47.757516+00:00_

审稿意见已提交给 Review Director。

总结：本文的 epoch confound 发现和数学框架是优势，但有四个 critical 问题需要解决：(1) N=3 统计功效不足；(2) B=4 使连续框架退化为离散查表；(3) 自污染实验设置限制外部效度；(4) 下游任务无改善，PPL 增益可能仅反映分布匹配。整体评价 3/5，适合 Findings track，但需要补充实验证据或调整 claim 范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 207 · 2026-05-19T07:19:31.442960+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Weakness。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿意见：

**Overall**: 3.0/5 (Findings)

**Strengths**:
S1. Epoch confound 分析是最强贡献（Table 2 + Figure 3）
S2. 诚实且全面的 Limitations section
S3. 消融设计合理（Adaptive < Uniform < ESS-only < Random）
S4. Related Work 覆盖全面（48 条引用）
S5. 写作质量较好，无 AI 痕迹

**Must-Fix**:

R2-W1 [critical]: Effect size 极其微弱，1.7B 无改善，实用价值成疑
- 0.6B, ρ=0.4: Δ=-0.043 PPL (0.24% relative)
- 0.6B, ρ=0.6: Δ=-0.028 PPL
- 1.7B: Δ=-0.01, 仅 2 seeds, "no evidence of either improvement or degradation"
- Downstream: 5 个 task 中 4 个 adaptive 略差于 uniform
- 95% CI of adaptive-vs-grid gap [-0.039, 0.101] 包含 0.10 PPL 退化
- 建议重新 frame 为 empirical findings 为主要贡献

R2-W2 [critical]: Self-contamination 设计严重限制 generalizability
- generator = trainee（Qwen3-0.6B）
- Self-generated text 对同架构 detector 最容易检测
- Cross-model (Appendix F, Llama-3.2-3B) single-seed, 无 PPL
- Real web contamination 是 multi-source, domain-skewed

**Should-Fix**:

R2-W3 [warning]: Micro-batch B=4 使 α_eff 退化为 5-point 离散函数
- α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}
- Bisection 实质上在做离散搜索
- Dual-constraint 框架在 B=4 下是否 overkill？

R2-W4 [warning]: τ=0.8 通过 single-seed sweep 选出，"no grid search" claim 过强
- τ sweep 本身是另一种 grid search（6 values）
- τ=0.8 在 ρ=0.4 最优，ρ=0.6 下 τ=0.7 最优
- 建议弱化为 "reduces b grid search to a τ sensitivity check"

R2-W5 [warning]: "Detector signal type > AUC" 证据不足
- 仅 3 detectors (1 discriminative, 2 generative), all seed 42
- 无法区分 type effect 和 calibration effect

R2-W6 [warning]: Downstream evaluation 过于薄弱
- 5 benchmarks, single seed, 4/5 tasks adaptive 略差
- Table 11 caption "preserves downstream performance" 与数据不符

**Minor**:
R2-M1: Abstract 数字过多
R2-M2: "Content epochs" 未正式定义
R2-M3: Grid results at ρ=0.6 single seed 标注不够显眼
R2-M4: GPU 类型未在正文中指定
R2-M5: vehtari2024psis 年份待核实

---

请对每条 R2-W1 到 R2-W6 以及 R2-M1 到 R2-M5 逐条给出 [AGREE] 或 [REBUT]，并说明理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-19T07:21:00.338585+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n### 总结\n与 R2 的 11 条意见中，**[AGREE] 10 条**，**[REBUT] 1 条**（R2-W6 caption 措辞问题，仅为部分反驳）。两位 reviewer 核心关切高度一致。\n\n### Must-Fix\n\n**[AGREE] R2-W1**: Effect size 递减趋势（0.6B→1.7B）比单个数字更说明问题。95% CI 包含 0.10 degradation 而 Abstract/Intro 未充分反映。同意 reframe 为 empirical findings paper。\n\n**[AGREE] R2-W2**: 与 R1-W3 一致。补充：Appendix G 原文 \"checkpoints were not retained for re-evaluation\"，cross-model 实验存在实验管理缺失。\n\n### Should-Fix\n\n**[AGREE] R2-W3**: 与 R1-W2 一致。补充 α_eff 分布具体数据（Appendix E）：τ=0.8 下 clean batch 仅 3%，实际上是 binary decision 而非连续优化。但论文已 acknowledge 且 B∈{4,8,16} 差异<0.01。\n\n**[AGREE] R2-W4**: R2 建议措辞 \"reduces b grid search to a τ sensitivity check\" 比我的建议更精确。τ 最优值随 ρ 变化（0.4→0.8, 0.6→0.7），不是 universal default。\n\n**[AGREE] R2-W5**: 补充标注 Table 7 仅 seed 42。论文给出了合理 mechanism hypothesis（generative detectors 对 fluent human text 产生 false positives），但需要 controlled experiment 验证。\n\n**[REBUT] R2-W6**: Table 8 caption \"preserves downstream performance\" 在统计学意义上成立（所有 |Δ| < typical SE）。但同意 R2 的实质关切：4/5 negative 的方向一致性需多 seed 评估 resolve。\n\n### Minor\n[AGREE] R2-M1, M2, M3, M5。[REBUT] R2-M4（GPU 信息在 Checklist C1 中已报告，但同意放入正文更好）。\n\n### 两位 Reviewer 的共识\n核心问题三条：(1) effect size 过小且随规模递减；(2) self-contamination 外部效度不足；(3) 统计证据在 N=3 下薄弱。Epoch confound 发现是论文最强的独立贡献。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n### 总结\n与 R2 的 11 条意见中，**[AGREE] 10 条**，**[REBUT] 1 条**（R2-W6 caption 措辞问题，仅为部分反驳）。两位 reviewer 核心关切高度一致。\n\n### Must-Fix\n\n**[AGREE] R2-W1**: Effect size 递减趋势（0.6B→1.7B）比单个数字更说明问题。95% CI 包含 0.10 degradation 而 Abstract/Intro 未充分反映。同意 reframe 为 empirical findings paper。\n\n**[AGREE] R2-W2**: 与 R1-W3 一致。补充：Appendix G 原文 \"checkpoints were not retained for re-evaluation\"，cross-model 实验存在实验管理缺失。\n\n### Should-Fix\n\n**[AGREE] R2-W3**: 与 R1-W2 一致。补充 α_eff 分布具体数据（Appendix E）：τ=0.8 下 clean batch 仅 3%，实际上是 binary decision 而非连续优化。但论文已 acknowledge 且 B∈{4,8,16} 差异<0.01。\n\n**[AGREE] R2-W4**: R2 建议措辞 \"reduces b grid search to a τ sensitivity check\" 比我的建议更精确。τ 最优值随 ρ 变化（0.4→0.8, 0.6→0.7），不是 universal default。\n\n**[AGREE] R2-W5**: 补充标注 Table 7 仅 seed 42。论文给出了合理 mechanism hypothesis（generative detectors 对 fluent human text 产生 false positives），但需要 controlled experiment 验证。\n\n**[REBUT] R2-W6**: Table 8 caption \"preserves downstream performance\" 在统计学意义上成立（所有 |Δ| < typical SE）。但同意 R2 的实质关切：4/5 negative 的方向一致性需多 seed 评估 resolve。\n\n### Minor\n[AGREE] R2-M1, M2, M3, M5。[REBUT] R2-M4（GPU 信息在 Checklist C1 中已报告，但同意放入正文更好）。\n\n### 两位 Reviewer 的共识\n核心问题三条：(1) effect size 过小且随规模递减；(2) self-contamination 外部效度不足；(3) 统计证据在 N=3 下薄弱。Epoch confound 发现是论文最强的独立贡献。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-19T07:21:05.407506+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5068
}
```

</details>

---


### Assistant

_source line 210 · 2026-05-19T07:21:09.579083+00:00_

交叉回应已提交。与 R2 的 11 条意见中同意 10 条，仅对 R2-W6（caption 措辞）部分反驳。两位 reviewer 的核心共识：effect size 过小、self-contamination 外部效度不足、N=3 统计薄弱。Epoch confound 是最强独立贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

78 recorded events


### User

_source line 211 · 2026-05-19T14:03:34.791359+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查方法严谨性、实验设计和统计有效性。

## Venue 信息
- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR)
- **截止日期**：2026-05-25
- **格式**：Long paper，正文 ≤8 页，参考文献不限页数
- **模板**：ACL style（\usepackage[review]{acl}）
- **匿名规则**：Double-blind
- **Limitations section**：必须，不计入页数
- **ARR Overall Assessment 评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf`
- Sections 在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex, checklist.tex

## 你的审查侧重

### 1. 数学公式与理论正确性
- Dual-constraint framework（Eq. 1-4）的数学严谨性
- Proposition 1（α_eff 单调性）和 Proposition 2（ESS 单调性）的证明正确性
- b* 求解算法（Algorithm 1）的正确性和完备性
- 是否有隐含假设未说明

### 2. 实验设计有效性
- 自污染（self-contamination）设计的合理性和局限性
- Epoch-matched 对照实验的设计是否公平（注意：D&R 和 adaptive 使用不同的 cosine schedule 步数）
- 基线选择是否充分（Uniform, Grid-b, ESS-only, Random, Golden Ratio, D&R）
- 评估指标的适当性（held-out PPL 作为主要指标）

### 3. 统计有效性
- N=3 seeds 的统计检验力是否足够支撑论文声明
- 95% CI [-0.039, 0.101] 包含了性能退化的可能——论文如何处理这一事实
- 1.7B 结果只有 2 seeds，是否足以得出"无效果"的结论
- 效应量（Δ=-0.043 PPL）的实际意义
- 单 seed 结果（Golden Ratio, Grid at ρ=0.6）的可靠性

### 4. 可复现性
- 超参数报告是否完整（lr, optimizer, schedule, batch size, seq len, precision）
- 数据集构建过程是否可复现（FineWeb subset selection, synthetic generation）
- 代码可用性声明

### 5. 消融实验
- τ sweep 和 n_min sweep 是否充分
- Batch size sensitivity（B∈{4,8,16}）的验证
- 不同 ρ 值下方法行为的系统性分析

请严格、客观地评审，按以下格式输出：
1. Summary（2-3句）
2. Strengths（逐条）
3. Weaknesses（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）
4. Questions（需要作者回答的问题）
5. Missing References（遗漏的重要引用）
6. Overall Assessment（评分 + 置信度 + 简要理由）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-19T14:03:41.220830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-19T14:03:42.024234+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-19T14:03:42.024617+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-19T14:03:42.075042+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-19T14:03:46.396549+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-19T14:03:47.852168+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-19T14:03:48.153631+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-19T14:03:56.504909+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

The ACL Rolling Review asks reviewers to follow a workflow of: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. Additionally, reviewers should state in the review if they did not check some major parts, such as proofs, as this information is helpful for the AC to tell what aspects of the pape
…[truncated 943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10108
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-19T14:03:58.517024+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 623.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 766.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 688.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 643.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 728.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 707.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 630.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 666.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 683.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weig
…[truncated 333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10664
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-19T14:03:58.517514+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 10363
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-19T14:04:08.522296+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidance for each dimension. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidance for each dimension. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-19T14:04:09.327461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-19T14:04:09.730033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-19T14:04:11.642039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-19T14:04:11.642479+00:00_

Image file is empty: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 227 · 2026-05-19T14:04:12.147050+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-19T14:04:12.398924+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3071
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-19T14:04:12.399362+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-19T14:04:12.904595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3174
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-19T14:04:17.042397+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely but conceivable to miss important details
- **3**: Pretty sure; good general knowledge but didn't carefully verify details
- **2**: Willing to defend evaluation; fairly likely to have missed elements
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: Excellent; "one of the most thorough I have seen"
- **4**: Strong; sufficient support with optional minor additions
- **3**: Acceptable; supports main claims with minor gaps
- **2**: Poor; major technical/methodological problems
- **1**: Major Issues; "not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
Guidance: Subjective assessment of transformational potential, community impact, or personal relevance
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Exciting; worth mentioning to colleagues
- **3**: Interesting; might attend presentation if available
- **2**: Potentially Interesting; may resonate with others
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: Mostly reproducible; minor variations possible
- **3**: Some difficulty; underspecified parameters
- **2**: "Hard pressed to reproduce"; unavailable data
- **1**: "Would not be able to reproduce the results"

## 6. **Datasets Value**
Scale: 1-5
- **5**: Enabling; affects research direction choices
- **4**: Useful; recommended for ongoing work
- **3**: Po
…[truncated 646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8520
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-19T14:04:21.610076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-19T14:04:21.962021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-19T14:04:22.668056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-19T14:04:23.673037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-19T14:04:24.025971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-19T14:04:24.534031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-19T14:04:25.037198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-19T14:04:25.038310+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3428
}
```

</details>

---


### Tool result

_source line 240 · 2026-05-19T14:04:26.801704+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4839
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-19T14:04:28.717509+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6049
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-19T14:04:29.673620+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6000
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-19T14:04:30.226831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6200
}
```

</details>

---


### Tool result

_source line 244 · 2026-05-19T14:04:30.329843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5795
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-19T14:04:30.481738+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5444
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-19T14:04:37.474299+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "11-16",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "11-16",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-19T14:04:38.227345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-19T14:04:38.277923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-19T14:04:41.690540+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 703.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 631.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 462.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 562.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 656.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 138.4}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 200, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4216
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-19T14:04:41.691177+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	The indicator $r_i = \mathbf{1}[q_i \leq 0.5]$ is a proxy for true provenance: $\alpha_{\mathrm{eff}}$ tracks the detector's estimate of the real fraction, not the
…[truncated 9446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3463
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-19T14:04:41.691466+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision on a single NVIDIA RTX PRO 6000 (96\,GB).
14	All main comparisons
…[truncated 1585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3413
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-19T14:04:41.842123+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-19T14:04:41.893220+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 (pretrained checkpoint) to the 17.3--17.8 range; the initial 5.2-point drop absorbs the bulk of easy gains, and reweighting method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.651, compared to 17.620 for grid $b{=}0.3$ (gap 0.031, 95\% CI $[-0.039, 0.101]$, which includes possible degradation).
8	With only $N{=}3$ seeds, normality cannot be verified; we report exact per-seed gaps (0.013, 0.064, 0.017) and note lower cross-seed variance ($\pm$0.007 vs.\ $\pm$0.033).
9	The practical value is reducing $b$ grid search from nine full training runs to one~\citep{drayson2025detection}, saving ${\sim}$16 GPU-hours at 0.6B scale.
10	The grid-best $b{=}0.3$ is a post-hoc oracle selected after observing all nine candidates; in practice, validation-based selection from the same grid would yield worse results due to the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}).
11	At the grid point nearest mean per-batch $\bstar$ ($b{=}1.0$, seed\,42), PPL is 17.692, indistinguishable from uniform (17.694); per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (mean 17.802) perform worse than uniform (17.694): the detector's $q$-scores carry genuine provenance information, and uninformed reweighting increases gradient variance without corrective signal.
15	ESS-only (mean $17.738 {\pm} 0.022$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it provides no improvement over uniform.
16	Only the dual-constrained adaptive 
…[truncated 9723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-19T14:04:48.976421+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-19T14:04:49.278024+00:00_

1	\paragraph{Why minimum intervention works.}
2	The $\aeff$ constraint prevents 4.9$\times$ over-aggressive downweighting in 38.2\% of batches (\S\ref{sec:regime}), with consistent behavior across $\rho$ and seeds (CV ${<}2\%$).
3	A fixed exponent at the aggregate mean $\bstar$ ($b{=}1.0$) yields PPL 17.692, indistinguishable from uniform (17.694): per-batch adaptation is essential, and the minimum intervention principle (adaptive, 17.651) outperforms maximum intervention (ESS-only, 17.738).
4	
5	\paragraph{Failure modes and applicability boundary.}
6	At $\rho{=}0.2$, the method degrades by $+$0.046 PPL (Appendix~\ref{app:rho02}): the detector's mean $q$-score drops to 0.393, yet $\aeff$-binding rises to 60.1\%, so the method actively intervenes on unreliable signal.
7	The same pattern appears with generative detectors (GPT-2 PPL: $\Delta{=}{+}0.10$; N-gram PPL: $\Delta{=}{+}0.13$), which conflate predictability with provenance.
8	Both failure modes share a common root cause: when $q$-scores do not separate real from synthetic, the framework amplifies detector error rather than correcting for contamination.
9	The effective range with $\tau{=}0.8$ requires discriminative signal and $\rho \geq 0.4$.
10	
11	\paragraph{Distribution matching, not quality gain.}
12	The in-distribution PPL improvement reverses out-of-distribution ($+$0.06 OpenWebText, $+$0.14 Wikipedia; seed 42, other-seed checkpoints not retained), consistent with distribution matching rather than general improvement.
13	This pattern likely affects all contamination-aware reweighting that upweights human-authored samples~\citep{drayson2025detection}: in-distribution PPL may be an inadequate metric for evaluating contamination mitigation, since any method that shifts the training distribution toward the evaluation distribution will show gains regardless of genuine quality improvement.
14	Given this caveat, the concrete benefit of adaptive $\bstar$ is operational: reducing grid search from nine runs to one 
…[truncated 814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-19T14:04:49.429014+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-19T14:04:50.633530+00:00_

1	\paragraph{Self-contamination.}
2	All main experiments use self-contamination (generator = trainee), which does not represent realistic web contamination from multiple models and sources.
3	The resulting AUC of 0.94 reflects that self-generated text is relatively easy to detect; real multi-source contamination may yield lower detection accuracy, shifting the operating regime.
4	Cross-model results (Llama-3.2-3B generator, Appendix~\ref{app:cross_model}) are single-seed and lack PPL evaluation, and provide insufficient evidence for generalization beyond self-contamination.
5	
6	\paragraph{Scale.}
7	All main experiments use Qwen3-0.6B with batch size 4 on 132--200M tokens, comparable to domain-adaptive continued pretraining but far below full pretraining scale; validation at ${>}$100B tokens remains an important direction.
8	Preliminary evidence at 1.7B (Qwen3-1.7B, $\rho{=}0.4$, 2 seeds) shows $\Delta{=}{-}0.01$ (adaptive 13.26 vs.\ uniform 13.26); with only 2 seeds, this is insufficient for statistical conclusions about scale transfer.
9	A preliminary test with Llama-3.2-3B as trainee (single seed, $\rho{=}0.4$) showed degradation ($\Delta{=}{+}0.20$); the method has been validated only on the Qwen3 family.
10	Architecture transfer, which may involve tokenizer-dependent $q$-score calibration differences, remains an open question.
11	
12	\paragraph{Contamination range.}
13	The method improves over uniform at $\rho \in \{0.4, 0.6\}$ but not at $\rho{=}0.2$ ($+$0.046 PPL, 0.26\% relative); the effective range is $\rho \geq 0.4$ with $\tau{=}0.8$.
14	Behavior at $\rho > 0.8$ is untested; extreme contamination may violate the assumption that sufficient real samples exist per batch for meaningful $\aeff$ estimation.
15	Real web-scale contamination is domain-skewed, which may alter within-batch $\aeff$ distributions.
16	
17	\paragraph{Detector coverage.}
18	Three detectors have been tested: TF-IDF+LR (discriminative, AUC\,=\,0.94) succeeds, while GPT-2 perplexity (genera
…[truncated 1943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1204
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-19T14:04:50.684174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-19T14:04:51.286753+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
20	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	Since $r_i = \mathbf{1}[q_i \leq 0.5]$, the indicator $r_i$ and $\ln(1{-}q_i)$ are positively associated by construction, so the covariance is non-negative.
29	\end{proof}
30	
31	\begin{proposition}[ESS monotonicity]
32	\label{prop:ess_mono}
33	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
34	\end{proposition}
35	
36	\begin{proof}
37	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
38	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
39	Differentiating $H$ with respect to $b$:
40	\begin{equation*}
41	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
42	\end{equation*}
43	This equals $2\,\mathrm{Var}_{\pi^2}[\ln(1{-}q)]$ under the $\pi^2$-weighted measur
…[truncated 16791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-19T14:04:51.337314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 261 · 2026-05-19T14:04:52.340966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-19T14:04:53.145667+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1808
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-19T14:04:54.049472+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1708
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-19T14:05:00.222029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-19T14:05:01.333046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-19T14:05:02.237641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 267 · 2026-05-19T14:05:02.538961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-19T14:05:03.988356+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 269 · 2026-05-19T14:05:03.988780+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-19T14:05:03.989048+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-19T14:05:04.244123+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, detect-and-reweight methods that downweight likely-synthetic samples via $w(x) = (1-q(x))^b$ have gained traction.
2	Two questions remain open: does hard filtering outperform soft reweighting, and how should the exponent $b$ be set without per-model grid search?
3	
4	Through controlled experiments (Qwen3-0.6B continued pretraining, 132M FineWeb tokens, 40\% contamination, 3 seeds), we identify two confounds in current evaluation practice.
5	Detect and Remove (D\&R) owes its reported advantage entirely to multi-epoch exposure: at matched content epochs, D\&R and reweighting differ by only 0.006 perplexity ($N{=}3$).
6	In-distribution perplexity gains from adaptive reweighting do not transfer out-of-distribution (OpenWebText $+$0.06, Wikipedia $+$0.14), consistent with distribution matching rather than general quality improvement.
7	A dual-constrained adaptive $b^*$, selecting the minimum exponent that satisfies a quality floor while preserving gradient stability, matches grid-search performance without per-model tuning (gap 0.031, within seed variance $\pm$0.033); detector signal type appears to matter more than discrimination accuracy (3 detectors, single seed).
8	The method fails at $\rho{=}0.2$ and shows no effect at 1.7B; with $N{=}3$, we report effect sizes and directional consistency rather than formal significance.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 255
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-19T14:05:04.244743+00:00_

1	This analysis identifies two evaluation confounds in contamination-aware reweighting (epoch exposure and distribution matching) and characterizes when adaptive $\bstar$ is effective ($\rho \geq 0.4$ with a discriminative detector).
2	The most broadly relevant finding is that in-distribution PPL improvement does not transfer out-of-distribution: contamination-aware reweighting may function as distribution correction rather than quality improvement, a distinction that affects how such methods should be evaluated.
3	The adaptive framework's practical contribution is replacing per-model $b$ grid search with a single default $\tau$, though the effect size is modest ($\Delta{=}{-}0.043$ at $\rho{=}0.4$) and absent at 1.7B ($\Delta{=}{-}0.01$, 2 seeds).
4	Future work should establish evaluation protocols that distinguish genuine quality gains from distribution-shift artifacts, and test whether adaptive reweighting transfers beyond continued pretraining to web-scale settings.
5	Code and data will be released upon acceptance.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 255
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-19T14:05:04.245126+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, fundamental questions remain.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	How should $b$ be chosen, given that \citet{drayson2025detection} find optimal values ranging from $b{=}10$ (GPT-2 124M) to $b{=}1$ (SmolLM 1.7B), requiring costly per-model grid search?
8	What detector properties are necessary for effective reweighting?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters.\footnote{Our scope is continued pretraining on moderate-scale corpora with known contamination~\citep{gururangan2020dont}; generalization to from-scratch pretraining at web scale is untested.}
11	For the exponent selection problem, we derive $b$ per-batch from a dual-constrained formulation: find the minimum $b$ such that the weighted effective real proportion $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to Kish's effective sample size $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
12	
13	Our analysis identifies two evaluation confounds and characterizes adaptive reweighting:
14	\begin{itemize}[nosep,leftmargin=*]
15	\item \textbf{Epoch confound.}
16	D\&R's PPL a
…[truncated 1087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 256
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-19T14:05:04.259157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1720
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-19T14:05:04.260143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4038
}
```

</details>

---


### Tool result

_source line 276 · 2026-05-19T14:05:06.977737+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5644
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-19T14:05:07.531385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5293
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-19T14:05:16.677201+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-19T14:05:17.225279+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-19T14:05:53.293042+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 48, \"total_citations\": 79, \"unique_cited_keys\": 48, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 35, \"online_not_found\": 6, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"kang2025demystifying\", \"type\": \"inproceedings\", \"title\": \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\", \"authors\": \"Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Ch...\", \"year\": \"2025\", \"venue\": \"EMNLP\"}, {\"key\": \"zibakhsh2025fortifai\", \"type\": \"article\", \"title\": \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\", \"authors\": \"Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koush...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.08972\"}, {\"key\": \"yi2025escaping\", \"type\": \"article\", \"title\": \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\", \"authors\": \"Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.16657\"}, {\"key\": \"drayson2025detection\", \"type\": \"article\", \"title\": \"Machine-Generated Text Detection Prevents Language Model Collapse\", \"authors\": \"Drayson, George and Yilmaz, Emine and Lampos, Vasileios\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.15654\"}, {\"key\": \"he2025golden\", \"type\": \"article\", \"title\": \"Golden Ratio Weighting Prevents Model Collapse\", \"authors\": \"He, Hengzhi and Xu, Shirong and Cheng, Guang\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.18049\"}, {\"key\": \"wang2026survive\", \"type\": \"article\", \"title\": \"Can Generative Artificial Int
…[truncated 36389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 36615
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-19T14:05:53.293534+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\
…[truncated 5527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 36068
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-19T14:09:59.853831+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见 — Round 1 (Fresh Review)\n\n**侧重**：方法严谨性、实验设计、统计有效性\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 论文在方法学上的分析贡献（epoch confound 识别、distribution matching 洞察）有价值，但自适应方法的实际收益微弱（Δ=-0.043 PPL）、OOD 评估反转、1.7B 无效果、self-contamination 设计限制了泛化性，整体达到 Findings 水平。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 数学证明正确，实验设计周全（epoch-matched control 设计良好），但 N=3 统计效力有限，多项关键结论依赖 single-seed |\n| Excitement | 2.5/5 | Epoch confound 分析对领域有启示，但自适应方法实际收益微弱且适用范围窄（ρ≥0.4, 仅 Qwen3, 仅 in-distribution） |\n| Reproducibility | 4/5 | 训练细节完整（lr, optimizer, schedule, batch size, seq len, precision, hardware），代码承诺发布 |\n| Reviewer Confidence | 4/5 | 仔细阅读全文及附录，熟悉相关工作 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 下的统计声明与 95% CI 包含退化的矛盾\n\n- 具体位置：Section 5.1, Table 2, Abstract\n- 问题：论文声称 adaptive b* \"matches grid-search performance\"，但 adaptive vs. grid-best 的 95% CI 为 [-0.039, 0.101]（Section 5.1），意味着 adaptive 可能比 grid-best 差 0.101 PPL。Abstract 中 \"gap 0.031, within seed variance ±0.033\" 模糊了这一事实。对 adaptive vs. uniform（paired Δ: -0.041, -0.043, -0.045, SD=0.002），论文自述 \"N=3 precludes formal significance testing\"，但实际上 paired t-test 会高度显著（t≈-37, df=2）——论文本可做此检验而非回避。\n- 为什么影响接收：核心 claim 需统计支撑。呈现方式在 under-claiming（可做的 paired test 未做）和 over-claiming（CI 包含退化但声称 \"matches\"）之间不一致。\n- 建议：(1) 执行 paired t-test 报告 p-value；(2) 将 \"matches grid-search\" 改为更审慎的措辞。\n\n**N2** [critical] Self-contamination 设计严重限制外部效度\n\n- 具体位置：Section 4, Limitations §Self-contamination\n- 问题：generator=trainee（Qwen3-0.6B），检测较易（AUC=0.94），与真实 web-scale 多源污染差异极大。唯一 cross-model 结果（Appendix M）是 single-seed 无 PPL 评估；Llama-3.2-3B 作为 trainee 直接退化（Δ=+0.20）。\n- 为什么影响接收：方法仅在 Qwen3 self-contamination 下有效，Llama 退化是不泛化的直接证据。\n- 建议：补充 Llama 3-seed PPL 评估，或在标题/abstract 中明确限定 scope。\n\n**N3** [critical] OOD 评估反转 + 下游任务无收益 = 实际价值存疑\n\n- 具体位置：Section 5.2, Appendix G, Discussion\n- 问题：OpenWebText +0.06, Wikipedia +0.14（PPL 反升），downstream 4/5 tasks slightly negative。论文自承 \"distribution matching, not quality gain\"。OOD 评估仅基于 seed 42（\"checkpoints for other seeds not retained\"）——最重要的评估方向证据最弱。\n- 为什么影响接收：若 PPL 改善仅是 distribution matching，方法实际价值仅限于节省约 16 GPU-hours grid search。\n- 建议：补充 3-seed OOD 评估和 multi-seed downstream 评估。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] D&R epoch-matched 对照的 LR schedule confound — Table 1 中 epoch-matched D&R 用 6,103-step cosine schedule 但仅训练 2,533 步，LR 未充分衰减。论文声称 \"favors D&R\" 但未验证。建议补充 matched schedule 对照。\n\n**W2** [warning] 1.7B 实验严重不足 — 仅 2 seeds, 无 grid-best 对比, Δ=-0.01。建议补充至 3 seeds 或降级为 preliminary observation。\n\n**W3** [warning] τ=0.8 default 泛化性证据不足 — τ sweep 仅 single-seed ρ=0.4；ρ=0.6 下 optimal 偏移至 τ=0.7。建议 multi-seed multi-ρ 验证。\n\n**W4** [warning] α_eff proxy 在 B=4 下仅 5 个离散值 — Pearson r=0.706 仅解释约 50% 方差，b* 决策全依赖此 proxy。建议讨论 proxy error sensitivity。\n\n**W5** [warning] Grid-best 对比 fairness — 论文 argue 实际 grid search 表现更差（\"noisy PPL plateau\"），但未实现 realistic validation-based grid search 来量化。建议补充。\n\n---\n\n## 小问题\n\n- Proposition 2 证明中 \"2 Var_{π²}[ln(1-q)]\" 表述不精确，实为 π-measure 下的 covariance。\n- Eq. 4 的 inf + s.t. 混合形式不标准，建议用 piecewise 显式写出冲突解决。\n- ρ 的 token-level vs. document-level 区分（脚注 1）应更早说明。\n- Fig. 1 \"degradation zone\" (b≥2) 定义模糊：grid b=2.0 PPL (17.741) 仍优于 ESS-only (17.738)。\n\n---\n\n## Questions for Authors\n\n1. Adaptive vs. uniform paired SD=0.002，为何不做 paired t-test？\n2. OOD 评估为何仅 seed 42？为何未保留其他 checkpoint？\n3. Domain-heterogeneous contamination（某些 domain ρ=0.6, 某些 ρ=0.1）下方法行为如何？\n4. Llama 退化归因于 detector 还是架构？是否为 Llama 重训了 detector？\n5. Fig. 1 degradation zone 定义是否准确？\n\n---\n\n## Missing References\n\n- Katharopoulos & Fleuret (2018) \"Not All Samples Are Created Equal: Deep Learning with Importance Sampling\"\n- Ren et al. (2018) \"Learning to Reweight Examples for Robust Deep Learning\"\n\n---\n\n## 主要优势\n\n- Epoch confound 分析：Table 1 设计简洁有力，揭示 D&R 优势完全来自 multi-epoch exposure\n- 罕见的诚实自我批评：主动披露所有负面结果，不 overclaim\n- 数学框架清晰：dual-constraint formulation 优雅，Propositions 证明简洁正确\n- 系统消融实验：τ/n_min/batch size/regime/detector comparison 全面\n- 格式合规：正文 8 页，Limitations 完整，checklist 详尽，双盲合规",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见 — Round 1 (Fresh Review)\n\n**侧重**：方法严谨性、实验设计、统计有效性\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 论文在方法学上的分析贡献（epoch confound 识别、distribution matching 洞察）有价值，但自适应方法的实际收益微弱（Δ=-0.043 PPL）、OOD 评估反转、1.7B 无效果、self-contamination 设计限制了泛化性，整体达到 Findings 水平。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 数学证明正确，实验设计周全（epoch-matched control 设计良好），但 N=3 统计效力有限，多项关键结论依赖 single-seed |\n| Excitement | 2.5/5 | Epoch confound 分析对领域有启示，但自适应方法实际收益微弱且适用范围窄（ρ≥0.4, 仅 Qwen3, 仅 in-distribution） |\n| Reproducibility | 4/5 | 训练细节完整（lr, optimizer, schedule, batch size, seq len, precision, hardware），代码承诺发布 |\n| Reviewer Confidence | 4/5 | 仔细阅读全文及附录，熟悉相关工作 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 下的统计声明与 95% CI 包含退化的矛盾\n\n- 具体位置：Section 5.1, Table 2, Abstract\n- 问题：论文声称 adaptive b* \"matches grid-search performance\"，但 adaptive vs. grid-best 的 95% CI 为 [-0.039, 0.101]（Section 5.1），意味着 adaptive 可能比 grid-best 差 0.101 PPL。Abstract 中 \"gap 0.031, within seed variance ±0.033\" 模糊了这一事实。对 adaptive vs. uniform（paired Δ: -0.041, -0.043, -0.045, SD=0.002），论文自述 \"N=3 precludes formal significance testing\"，但实际上 paired t-test 会高度显著（t≈-37, df=2）——论文本可做此检验而非回避。\n- 为什么影响接收：核心 claim 需统计支撑。呈现方式在 under-claiming（可做的 paired test 未做）和 over-claiming（CI 包含退化但声称 \"matches\"）之间不一致。\n- 建议：(1) 执行 paired t-test 报告 p-value；(2) 将 \"matches grid-search\" 改为更审慎的措辞。\n\n**N2** [critical] Self-contamination 设计严重限制外部效度\n\n- 具体位置：Section 4, Limitations §Self-contamination\n- 问题：generator=trainee（Qwen3-0.6B），检测较易（AUC=0.94），与真实 web-scale 多源污染差异极大。唯一 cross-model 结果（Appendix M）是 single-seed 无 PPL 评估；Llama-3.2-3B 作为 trainee 直接退化（Δ=+0.20）。\n- 为什么影响接收：方法仅在 Qwen3 self-contamination 下有效，Llama 退化是不泛化的直接证据。\n- 建议：补充 Llama 3-seed PPL 评估，或在标题/abstract 中明确限定 scope。\n\n**N3** [critical] OOD 评估反转 + 下游任务无收益 = 实际价值存疑\n\n- 具体位置：Section 5.2, Appendix G, Discussion\n- 问题：OpenWebText +0.06, Wikipedia +0.14（PPL 反升），downstream 4/5 tasks slightly negative。论文自承 \"distribution matching, not quality gain\"。OOD 评估仅基于 seed 42（\"checkpoints for other seeds not retained\"）——最重要的评估方向证据最弱。\n- 为什么影响接收：若 PPL 改善仅是 distribution matching，方法实际价值仅限于节省约 16 GPU-hours grid search。\n- 建议：补充 3-seed OOD 评估和 multi-seed downstream 评估。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] D&R epoch-matched 对照的 LR schedule confound — Table 1 中 epoch-matched D&R 用 6,103-step cosine schedule 但仅训练 2,533 步，LR 未充分衰减。论文声称 \"favors D&R\" 但未验证。建议补充 matched schedule 对照。\n\n**W2** [warning] 1.7B 实验严重不足 — 仅 2 seeds, 无 grid-best 对比, Δ=-0.01。建议补充至 3 seeds 或降级为 preliminary observation。\n\n**W3** [warning] τ=0.8 default 泛化性证据不足 — τ sweep 仅 single-seed ρ=0.4；ρ=0.6 下 optimal 偏移至 τ=0.7。建议 multi-seed multi-ρ 验证。\n\n**W4** [warning] α_eff proxy 在 B=4 下仅 5 个离散值 — Pearson r=0.706 仅解释约 50% 方差，b* 决策全依赖此 proxy。建议讨论 proxy error sensitivity。\n\n**W5** [warning] Grid-best 对比 fairness — 论文 argue 实际 grid search 表现更差（\"noisy PPL plateau\"），但未实现 realistic validation-based grid search 来量化。建议补充。\n\n---\n\n## 小问题\n\n- Proposition 2 证明中 \"2 Var_{π²}[ln(1-q)]\" 表述不精确，实为 π-measure 下的 covariance。\n- Eq. 4 的 inf + s.t. 混合形式不标准，建议用 piecewise 显式写出冲突解决。\n- ρ 的 token-level vs. document-level 区分（脚注 1）应更早说明。\n- Fig. 1 \"degradation zone\" (b≥2) 定义模糊：grid b=2.0 PPL (17.741) 仍优于 ESS-only (17.738)。\n\n---\n\n## Questions for Authors\n\n1. Adaptive vs. uniform paired SD=0.002，为何不做 paired t-test？\n2. OOD 评估为何仅 seed 42？为何未保留其他 checkpoint？\n3. Domain-heterogeneous contamination（某些 domain ρ=0.6, 某些 ρ=0.1）下方法行为如何？\n4. Llama 退化归因于 detector 还是架构？是否为 Llama 重训了 detector？\n5. Fig. 1 degradation zone 定义是否准确？\n\n---\n\n## Missing References\n\n- Katharopoulos & Fleuret (2018) \"Not All Samples Are Created Equal: Deep Learning with Importance Sampling\"\n- Ren et al. (2018) \"Learning to Reweight Examples for Robust Deep Learning\"\n\n---\n\n## 主要优势\n\n- Epoch confound 分析：Table 1 设计简洁有力，揭示 D&R 优势完全来自 multi-epoch exposure\n- 罕见的诚实自我批评：主动披露所有负面结果，不 overclaim\n- 数学框架清晰：dual-constraint formulation 优雅，Propositions 证明简洁正确\n- 系统消融实验：τ/n_min/batch size/regime/detector comparison 全面\n- 格式合规：正文 8 页，Limitations 完整，checklist 详尽，双盲合规",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-19T14:10:03.770541+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-19T14:10:07.901281+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-19T14:10:07.951843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-19T14:10:11.816654+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-19T14:10:11.869081+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 52
}
```

</details>

---


### Assistant

_source line 288 · 2026-05-19T14:10:22.310016+00:00_

审稿完成。

**总结**：论文评为 **3.0 (Findings)**。主要贡献是识别 D&R 的 epoch confound 和 distribution matching 现象，这两个分析发现有独立价值。自适应 b* 方法数学上优雅但实际收益微弱（Δ=-0.043 PPL, OOD 反转, 1.7B 无效果），且仅在 Qwen3 self-contamination 设定下验证。3 个 Must-Fix 问题：(1) 统计声明不一致（可做的 paired test 未做，CI 包含退化但声称 "matches"）；(2) self-contamination + Llama 退化限制泛化性；(3) OOD/downstream 无收益且仅 single-seed 评估。论文最值得称道的是诚实的自我批评——几乎所有弱点都被主动披露。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 289 · 2026-05-19T14:10:48.430076+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿报告

**Overall**: 2.5 — Borderline Findings
**Confidence**: 4/5

### Strengths
S1. Epoch confound 实验揭示是最有价值贡献（Table 1, Figure 4, Table 6）
S2. 异常诚实的自我评估（Abstract 直接陈述 method fails at ρ=0.2, no effect at 1.7B）
S3. Dual-constraint 框架设计原则清晰（Propositions 1-2, Algorithm 1）
S4. 相关工作覆盖系统全面（5 层次结构）
S5. Ablation 设计完整（Table 2, 5+2 methods）

### Weaknesses
W1 [Must-Fix] 实验规模过窄，无法支撑论文核心 claim。全部主实验基于单一模型族（Qwen3-0.6B）、单一数据集（FineWeb 132M）、3 个 seed。1.7B 仅 2 seeds 且无效果，Llama-3.2-3B 单 seed 退化（Δ=+0.20）。标题 "When Does Detect-and-Reweight Work?" 的普适性问题无法被回答。建议至少 (a) 1.7B 补 3-seed，或 (b) 第二模型族验证，或 (c) title/claim 限定 scope。

W2 [Must-Fix] In-distribution PPL 改善量级极小且不迁移，实际价值存疑。Δ=-0.043 at 0.6B, OOD 反转（OpenWebText +0.06, Wikipedia +0.14），downstream 4/5 tasks 略降，论文自承 "in-distribution PPL may be an inadequate metric"。建议 (a) 多 seed OOD 评估，(b) 多 seed downstream，(c) 或重新定位为 analysis paper。

W3 [Must-Fix] Self-contamination 实验设计的外部效度不足。Generator=trainee 使检测人为降低难度（AUC=0.94）。Cross-model（Appendix M）仅 single seed 无 PPL。建议至少一个多模型混合污染实验。

W4 [Should-Fix] Adaptive b* 相对于 Grid-best 无显著优势。Gap=0.031, 95% CI [-0.039, 0.101] 包含退化。建议修改 abstract "matches" 为 "approaches"。

W5 [Should-Fix] Micro-batch B=4 导致 α_eff 仅 5 离散值，与连续优化框架叙事矛盾。建议更早更显著说明离散化现实。

W6 [Should-Fix] τ=0.8 推荐缺乏充分验证。τ sweep 基于 single seed ρ=0.4；ρ=0.6 最优偏移至 0.7。建议 multi-seed sweep。

W7 [Should-Fix] 遗漏 Chen et al. (2024) "Take the Bull by the Horns" — instance-level reweighting for continual pretraining。

W8 [Minor] 部分引用年份不一致（vehtari2024psis, alemohammad2024mad）。
W9 [Minor] Figure 1 较小，b* 区域标注难辨。
W10 [Minor] Checklist E1 AI 辅助声明过于模糊。

### Questions
Q1. Grid b=0.3 的 3-seed 实验是否为 post-hoc selection 后才跑的？3-seed mean 是否被高估？
Q2. OOD 评估仅 seed 42，为何不保留其他 checkpoints？
Q3. "Detector signal type > accuracy" 结论是否可替代解释为 score distribution shape 而非 discriminative vs. generative？
Q4. 1.7B 无效是否意味着更大模型对合成数据更鲁棒，reweighting 本身不必要？
Q5. 如果 PPL 改善是 distribution matching 且 downstream 无改善，adaptive b* 的实际 use case 是什么？

### Missing References
1. Chen et al. (2024) "Take the Bull by the Horns" (arXiv:2402.14270)
2. 可能相关：arXiv:2505.03617 importance weighting in deep learning

---

请逐条回应每个 Weakness（W1-W10）和 Question（Q1-Q5），以及 Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-19T14:12:49.943462+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 实验规模过窄** — 与我的 N2 一致。补充：Llama-3.2-3B 退化 Δ=+0.20（Limitations §Scale）不仅是 \"未验证\"，而是方法在第二模型族上失败的直接证据。\n\n**[AGREE] R2-W2: PPL 改善极小且不迁移** — 与我的 N3 一致。OOD 评估仅 seed 42，最重要的负面发现证据最弱。建议重定位为 analysis paper。\n\n**[AGREE] R2-W3: Self-contamination 外部效度** — 与我的 N2 一致。补充：Discussion §Failure modes 承认 \"requires discriminative signal and ρ ≥ 0.4\"，这两个条件在 web-scale 同时满足需要 argue。\n\n**[AGREE] R2-W4: Adaptive vs. Grid-best 无显著优势** — 同意 CI 问题。但补充：adaptive vs. uniform 的 paired Δ SD=0.002，paired t-test t≈-37 极度显著。问题不是 \"是否优于 uniform\" 而是 \"是否 match grid-best\"——论文应区分两个 claim 的证据强度。\n\n**[REBUT] R2-W5: B=4 离散化** — 论文 Section 3.3 第 73-75 行已明确说明离散性，Appendix I 验证 B∈{4,8,16} PPL 差异 <0.01。Framework 数学对任意 B 成立。建议从 Should-Fix 降为 Minor。\n\n**[AGREE] R2-W6: τ=0.8 验证不足** — 与我的 W3 一致。ρ=0.6 下 optimal 已偏移至 0.7。\n\n**[REBUT] R2-W7: 遗漏 Chen et al. (2024)** — 该工作是 influence function-based domain adaptation，非 provenance-based reweighting。Related Work 已覆盖同类方法 LESS（Section 2 第 37 行），并在第 38 行明确区分了动机差异。建议降为 Minor。\n\n**[AGREE] R2-W8: 引用年份不一致** — 确认 vehtari2024psis 年份应为 2015，需修正。\n\n**[AGREE] R2-W9: Figure 1 标注难辨** — 同意。\n\n**[REBUT] R2-W10: Checklist E1 AI 辅助声明** — 论文声明 \"AI assistants were used for code development and manuscript drafting. All scientific claims verified by authors\"（Page 10），满足 ARR 2026 transparency 要求。不构成 weakness。\n\n### Questions 回应\n\n**[AGREE] R2-Q1** — Grid b=0.3 的 full grid 仅在 seed 42 跑（Appendix B Table 3），存在 selection bias。但 b∈[0.1,0.5] 的 broad plateau 使实际偏差可能很小。\n\n**[AGREE] R2-Q2** — 同我的 N3。\n\n**[AGREE] R2-Q3** — 替代解释更精确。论文 Appendix J 描述的实际机制是 score distribution shape（false positive 位置），非类型标签本身。论文 framing 应修正。\n\n**[AGREE] R2-Q4** — 合理假设。与 Drayson et al. 发现 1.7B 最优 b=1 一致。论文应在 Discussion 中讨论 \"reweighting 边际价值随规模递减\" 的可能性。\n\n**[AGREE] R2-Q5** — 当前 use case（节省 ~16 GPU-hours at 0.6B）结合 OOD 反转 + downstream 无收益 + 1.7B 无效果，价值微弱。重定位为 analysis paper 更 coherent。\n\n### Missing References 回应\n\n**[REBUT]** Chen et al. (2024) — 引用有参考价值但非必要，已有同类覆盖。\n**[REBUT]** arXiv:2505.03617 — 论文已引 Kimura & Hino (2024) 覆盖 importance weighting。\n\n### 评分分歧说明\n\nR2 给 2.5（Borderline Findings），我给 3.0（Findings）。分歧在于：我认为 epoch confound 分析（Table 1, Figure 4）作为独立 analytical contribution 足以支撑 Findings——揭示 D&R 优势完全归因于 multi-epoch exposure 对领域内方法评估有实质性指导意义。R2 可能过多 weight 了 method contribution 不足，未充分 credit analysis contribution。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 实验规模过窄** — 与我的 N2 一致。补充：Llama-3.2-3B 退化 Δ=+0.20（Limitations §Scale）不仅是 \"未验证\"，而是方法在第二模型族上失败的直接证据。\n\n**[AGREE] R2-W2: PPL 改善极小且不迁移** — 与我的 N3 一致。OOD 评估仅 seed 42，最重要的负面发现证据最弱。建议重定位为 analysis paper。\n\n**[AGREE] R2-W3: Self-contamination 外部效度** — 与我的 N2 一致。补充：Discussion §Failure modes 承认 \"requires discriminative signal and ρ ≥ 0.4\"，这两个条件在 web-scale 同时满足需要 argue。\n\n**[AGREE] R2-W4: Adaptive vs. Grid-best 无显著优势** — 同意 CI 问题。但补充：adaptive vs. uniform 的 paired Δ SD=0.002，paired t-test t≈-37 极度显著。问题不是 \"是否优于 uniform\" 而是 \"是否 match grid-best\"——论文应区分两个 claim 的证据强度。\n\n**[REBUT] R2-W5: B=4 离散化** — 论文 Section 3.3 第 73-75 行已明确说明离散性，Appendix I 验证 B∈{4,8,16} PPL 差异 <0.01。Framework 数学对任意 B 成立。建议从 Should-Fix 降为 Minor。\n\n**[AGREE] R2-W6: τ=0.8 验证不足** — 与我的 W3 一致。ρ=0.6 下 optimal 已偏移至 0.7。\n\n**[REBUT] R2-W7: 遗漏 Chen et al. (2024)** — 该工作是 influence function-based domain adaptation，非 provenance-based reweighting。Related Work 已覆盖同类方法 LESS（Section 2 第 37 行），并在第 38 行明确区分了动机差异。建议降为 Minor。\n\n**[AGREE] R2-W8: 引用年份不一致** — 确认 vehtari2024psis 年份应为 2015，需修正。\n\n**[AGREE] R2-W9: Figure 1 标注难辨** — 同意。\n\n**[REBUT] R2-W10: Checklist E1 AI 辅助声明** — 论文声明 \"AI assistants were used for code development and manuscript drafting. All scientific claims verified by authors\"（Page 10），满足 ARR 2026 transparency 要求。不构成 weakness。\n\n### Questions 回应\n\n**[AGREE] R2-Q1** — Grid b=0.3 的 full grid 仅在 seed 42 跑（Appendix B Table 3），存在 selection bias。但 b∈[0.1,0.5] 的 broad plateau 使实际偏差可能很小。\n\n**[AGREE] R2-Q2** — 同我的 N3。\n\n**[AGREE] R2-Q3** — 替代解释更精确。论文 Appendix J 描述的实际机制是 score distribution shape（false positive 位置），非类型标签本身。论文 framing 应修正。\n\n**[AGREE] R2-Q4** — 合理假设。与 Drayson et al. 发现 1.7B 最优 b=1 一致。论文应在 Discussion 中讨论 \"reweighting 边际价值随规模递减\" 的可能性。\n\n**[AGREE] R2-Q5** — 当前 use case（节省 ~16 GPU-hours at 0.6B）结合 OOD 反转 + downstream 无收益 + 1.7B 无效果，价值微弱。重定位为 analysis paper 更 coherent。\n\n### Missing References 回应\n\n**[REBUT]** Chen et al. (2024) — 引用有参考价值但非必要，已有同类覆盖。\n**[REBUT]** arXiv:2505.03617 — 论文已引 Kimura & Hino (2024) 覆盖 importance weighting。\n\n### 评分分歧说明\n\nR2 给 2.5（Borderline Findings），我给 3.0（Findings）。分歧在于：我认为 epoch confound 分析（Table 1, Figure 4）作为独立 analytical contribution 足以支撑 Findings——揭示 D&R 优势完全归因于 multi-epoch exposure 对领域内方法评估有实质性指导意义。R2 可能过多 weight 了 method contribution 不足，未充分 credit analysis contribution。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-19T14:12:53.505877+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3562
}
```

</details>

---


### Assistant

_source line 292 · 2026-05-19T14:12:58.835369+00:00_

已完成对 Reviewer 2 全部 10 条 Weakness 和 5 个 Question 的逐条回应，并发送给 Review Director。

总结：与 R2 在 7/10 Weaknesses 上一致（W1-W4, W6, W8-W9），对 W5（离散化严重性）、W7（遗漏引用）、W10（checklist 声明）持反驳意见。5 个 Questions 全部认同合理性。评分分歧（R2: 2.5 vs. 我: 3.0）源于对 epoch confound 分析作为独立 analytical contribution 的权重不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

58 recorded events


### User

_source line 293 · 2026-05-20T03:10:10.481805+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计**。

## 论文信息
- 标题: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf`
- 目标 venue: EMNLP 2026 (via ARR)
- 投稿类别: Findings
- 截止日期: 2026-05-25

## Venue 要求 (EMNLP 2026 ARR)
- Long paper: **正文 8 页限制**，参考文献无限制
- Limitations section 必选（不计入页数限制）
- Ethics statement 可选（不计入页数限制）
- Responsible NLP Research Checklist 必选
- **Double-blind**: 不得出现作者姓名、机构、非匿名链接
- Overall Assessment 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重

### 1. 方法正确性
- Dual-constraint framework (α_eff + ESS) 的理论基础是否合理
- Proposition 1 和 Proposition 2 的证明是否正确
- Per-batch adaptive b* 算法是否正确实现
- B=4 micro-batch 下 α_eff 仅 5 个离散值，continuous framing 是否成立

### 2. 统计声明
- N=3 seeds 下的效果声明是否适当 (Δ=-0.020 PPL)
- "directional consistency" framing 是否 overstate 证据
- 1.7B 结果 (2 seeds, Δ=-0.01) 的 "preliminary" 标签是否足够
- Epoch-matched comparison 的统计支持度

### 3. 实验设计
- Self-contamination 设计的 external validity
- Detector 选择 (TF-IDF+LR, AUC=0.94) 的合理性
- 消融实验完整性 (Grid, ESS-only, Random, Golden Ratio, D&R)
- ρ=0.2 failure 和 ρ=0.6 extension 的覆盖是否足够
- Generative detector reversal (GPT-2, N-gram) 的分析深度
- OOD evaluation 和 downstream evaluation 的充分性

### 4. 可复现性
- 实验细节是否足以复现（超参数、训练配置、评估协议）
- 代码/数据承诺是否明确

请按以下格式输出审稿报告：

```
## Summary (2-3 句)

## Strengths (逐条)

## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])

## Questions (需要作者澄清的)

## Missing References

## Scores
- Soundness: X/5
- Substance: X/5
- Reproducibility: X/5
- Overall Assessment: X (使用 EMNLP 2026 评分标准)
- Confidence: X/5
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-20T03:10:16.663070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-20T03:10:16.715073+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-20T03:10:18.982467+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-20T03:10:19.134301+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-20T03:10:21.203122+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/*review*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-20T03:10:21.253780+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-20T03:10:27.526124+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-20T03:10:27.526541+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-20T03:10:32.713628+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-20T03:10:35.172768+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-20T03:10:35.801297+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-20T03:10:41.292022+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Review Form Criteria

The review form distinguishes between diffe
…[truncated 1114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8578
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-20T03:10:43.402207+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 575.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weig
…[truncated 333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8229
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-20T03:11:25.823248+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 51, \"total_citations\": 80, \"unique_cited_keys\": 51, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 38, \"online_not_found\": 6, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"katharopoulos2018not\", \"type\": \"inproceedings\", \"title\": \"Not All Samples Are Created Equal: Deep Learning with Importance Sampling\", \"authors\": \"\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"ren2018learning\", \"type\": \"inproceedings\", \"title\": \"Learning to Reweight Examples for Robust Deep Learning\", \"authors\": \"Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"chen2024bull\", \"type\": \"article\", \"title\": \"Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves LLM Generalization\", \"authors\": \"Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.14270\"}, {\"key\": \"kang2025demystifying\", \"type\": \"inproceedings\", \"title\": \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\", \"authors\": \"Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Ch...\", \"year\": \"2025\", \"venue\": \"EMNLP\"}, {\"key\": \"zibakhsh2025fortifai\", \"type\": \"article\", \"title\": \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\", \"authors\": \"Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koush...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.08972\"}, {\"key\": \"yi2025escaping\", \"type\": \"article\", \"title\
…[truncated 38435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 50021
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-20T03:11:34.709825+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other criteria."
  }
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-20T03:11:37.034182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-20T03:11:37.639159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-20T03:11:38.881772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-20T03:11:38.882407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 313 · 2026-05-20T03:11:39.199669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-20T03:11:39.252624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2218
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-20T03:11:40.210638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2571
}
```

</details>

---


### Tool result

_source line 316 · 2026-05-20T03:11:41.119768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2237
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-20T03:11:41.221803+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2339
}
```

</details>

---


### Tool result

_source line 318 · 2026-05-20T03:11:41.273332+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2073
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-20T03:11:43.281541+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Review Dimensions

**1. Reviewer Confidence**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

**2. Soundness**
Evaluates scientific rigor and methodological validity. Scale ranges from 5 (Excellent) to 1 (Major Issues), with half-point increments available (4.5, 3.5, 2.5, 1.5).
- 5: "one of the most thorough I have seen, given its type"
- 4: "provides sufficient support for all of its claims"
- 3: "provides sufficient support for its main claims"
- 2: "main claims are not sufficiently supported"
- 1: "not yet sufficiently thorough to warrant publication"

**3. Excitement**
Subjective assessment of innovation and potential impact. Scale 5 (Highly Exciting) to 1 (Not Exciting).
- 5: "I would recommend this paper to others"
- 4: "I would mention this paper to others"
- 3: "I might mention some points"
- 2: "does not resonate with me, but it might with others"
- 1: "does not resonate with me"

**4. Overall Assessment**
Primary recommendation scale with seven tiers:
- 5: "Consider for Award" (top 2.5%)
- 4.5: "Borderline Award"
- 4: "Conference acceptance"
- 3.5: "Borderline Conference"
- 3: "Findings acceptance"
- 2.5: "Borderline Findings"
- 2: "Resubmit next cycle"
- 1.5: "Resubmit after next cycle"
- 1: "Do not resubmit"

## Secondary Evaluation Criteria

**5. Reproducibility**
- 5: "easily reproduce the results"
- 4: "mostly reproduce the results"
- 3: "reproduce with some difficulty"
- 2: "hard pressed to reproduce"
- 1: "would not be able to reproduce"

**6. Datasets (if applicable)**
- 5: "Enabling" impact on research decisions
- 4: "Useful" for ongoing work
- 3: "Potentially useful"
- 2: "Docume
…[truncated 433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8571
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-20T03:11:48.463696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 321 · 2026-05-20T03:11:48.966233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 322 · 2026-05-20T03:11:49.422011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 323 · 2026-05-20T03:11:49.422503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 324 · 2026-05-20T03:11:49.927167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 325 · 2026-05-20T03:11:49.927593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-20T03:11:50.379255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-20T03:11:50.480808+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-20T03:11:51.033955+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1106
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-20T03:11:51.338116+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-20T03:11:57.735716+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-20T03:11:59.398305+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 364.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 421.3}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 360.5}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1662
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-20T03:12:02.263479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 333 · 2026-05-20T03:12:02.715467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 334 · 2026-05-20T03:12:03.572137+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-20T03:12:03.573994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-20T03:12:03.574399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-20T03:12:04.029171+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-20T03:12:04.029631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-20T03:12:04.482178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 340 · 2026-05-20T03:12:04.936563+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 341 · 2026-05-20T03:12:04.937005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 342 · 2026-05-20T03:12:05.694056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1211
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-20T03:12:05.697017+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 760
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-20T03:16:25.641448+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告（方法严谨性 + 实验设计）\n\n### Summary (2-3 句)\n\n本文研究 continued LM pretraining 中 detect-and-reweight (D&R) 范式的有效性。核心发现有二：(1) D&R 报告的 PPL 优势主要来自 multi-epoch exposure 而非 distribution matching（epoch confound）；(2) 提出基于 α_eff + ESS 双约束的 adaptive reweighting 框架，避免 per-model grid search。在 Qwen3-0.6B 上 3 seeds 实验显示 Δ≈−0.020 PPL 的一致性改进，但改进幅度小且缺乏统计显著性检验；1.7B 规模实验（2 seeds）效果几乎消失。\n\n---\n\n### Strengths\n\n**S1. Epoch confound 的识别具有方法论价值。** 通过 epoch-matched control（Table 1），论文清晰展示 D&R 的 PPL 优势从 0.384 缩减至 Δ≈0.017，揭示了一个容易被忽视的实验设计陷阱。\n\n**S2. Dual-constraint 框架理论动机清晰。** α_eff（quality floor）+ ESS（stability ceiling）来源于重要性采样理论（Kish, 1965; Owen, 2013），Proposition 1-2 的单调性证明简洁正确（Appendix A）。将 grid search 降为单超参数 τ 的设计在工程上有实际价值。\n\n**S3. 消融实验覆盖全面。** 6 种方法对比（Uniform, Grid, ESS-only, Golden Ratio, Adaptive b*, D&R），加上 Appendix B 的完整 grid search 结果和 Appendix F 的 D&R threshold sensitivity（Table 6），充分展示了方法空间。\n\n**S4. Detector type 分析揭示了非直觉发现。** §5.3 和 Table 10 显示 generative detectors（GPT-2 perplexity, N-gram）尽管 AUC 可比甚至更高，却反转了 reweighting 的方向——detector signal type 比 discrimination accuracy 更重要。\n\n**S5. 诚实的 limitations 讨论。** 对 self-contamination 局限性、N=3 统计限制、ρ=0.2 失败模式、1.7B 初步性质均做了坦诚讨论。\n\n---\n\n### Weaknesses\n\n#### Must-Fix\n\n**N1** [critical] **Epoch confound——论文最重要的发现——仅基于单 seed（seed 42）**\n- 具体位置：Table 1（page 7），脚注 \"†Seed 42 only\"\n- 问题：Table 1 中 \"D&R full\" 和 \"D&R epoch-matched\" 两行均为 seed 42 单次实验。论文的核心 claim——\"gap shrinks from 0.384 to Δ≈0.017\"——完全依赖于该单 seed。仅 Adaptive b* 行使用了 3 seeds。由于 epoch-matched D&R 与 Adaptive b* 在 cosine schedule、LR curve 起点等训练动态上存在差异，单 seed 无法排除 seed-specific confound。\n- 为什么影响接收：这是论文的主要贡献之一。如果 epoch confound 在其他 seeds 上不成立或幅度不同，核心叙事将被削弱。\n- 建议修改方向：补充 seed 123 和 seed 456 的 epoch-matched comparison，或至少在 Limitations 中明确标注这是单 seed 的初步证据。\n\n**N2** [critical] **N=3 seeds + Δ=−0.020 PPL + 无正式统计检验 = 核心效果声明证据不足**\n- 具体位置：Table 2（page 7），Limitations §L（page 9）\n- 问题：Adaptive b* 的核心改进 Δ≈−0.020（mean PPL 17.674 vs. Uniform 17.694）来自 3 seeds。论文使用 \"directional consistency\" 替代统计检验。Table 2 注释 \"²\" 标注 seed 42 的 Adaptive b* 结果为 17.634，与其他 seed 存在约 0.04 的差异，暗示 seed 42 可能是 outlier。\n- 为什么影响接收：\"directional consistency\" framing 在 N=3 下可能 overstate 证据。Findings 级别论文仍需对核心定量 claim 提供最低限度的统计支撑。\n- 建议：(a) 报告 paired differences 及其标准差；(b) 执行 paired t-test 或 bootstrap CI；(c) 如果不显著，调整 claim 措辞强度。\n\n**N3** [critical] **B=4 micro-batch 下 α_eff 仅 5 个离散值，continuous framework 的实际意义存疑**\n- 具体位置：§3.3（page 4）\n- 问题：Proposition 1-2 建立在 α_eff 和 ESS 关于 b 的连续单调性基础上，但实际 b∈{0,1,2,3,4}，α_eff 只有 5 个取值。dual-constraint 中的 bisection 搜索退化为 brute-force 枚举。Appendix I（Table 9）报告 α_eff(0) 与真实 batch-level real fraction 的 MAE=0.114（约 11% 平均绝对误差）。\n- 为什么影响接收：理论和实践的 gap 未被充分弥合。在 B=4 下，\"adaptive\" 本质上是在 5 个固定权重配置中选择。\n- 建议：(a) 讨论 B=4 下离散化的理论影响；(b) 补充 B=8 或 B=16 的实验；(c) 或将 framing 调整为 discrete selection problem。\n\n#### Should-Fix\n\n**W1** [warning] **1.7B 规模结果（Δ≈−0.01, 2 seeds）实际上是负面证据，但论文措辞模糊**\n- 具体位置：§5.2（page 7）\n- 问题：1.7B 实验仅 2 seeds，Δ≈−0.01 在实验噪声范围内。论文称 \"insufficient for statistical conclusions about scale transfer\"，但这实际上是方法可能无效的信号。Downstream evaluation 也显示 \"no meaningful downstream impact\"。\n- 建议：更明确地定位为\"目前无证据表明方法在更大规模有效\"。\n\n**W2** [warning] **Self-contamination 设计的 external validity 严重受限**\n- 具体位置：§4，Limitations §Self-contamination，Appendix M\n- 问题：所有主实验使用 self-contamination（generator = trainee），AUC=0.94。Appendix M 的 cross-model transfer 实验是单 seed 且未报告 PPL comparison。真实 web 场景的 contamination 来自多源，AUC 可能远低于 0.94。\n- 建议：补充至少一个 cross-model contamination 完整实验，或在 title/abstract 中限定为 self-contamination。\n\n**W3** [warning] **ρ=0.2 失败模式未充分探索**\n- 具体位置：§5.4 / Appendix H\n- 问题：ρ=0.2 时方法退化 +0.046 PPL，但未探索是否可通过调整 τ 或 detector threshold 应对，也未提供诊断方法判断何时 reweighting 有益。\n\n**W4** [warning] **Detector calibration 敏感性未分析**\n- 具体位置：§4，Appendix K\n- 问题：方法依赖 post-hoc temperature scaling（T=0.204, ECE=0.05），但未分析 calibration 质量对最终 PPL 的影响。\n\n#### Minor\n\n- **M1**: Figure 1 y 轴压缩（~17.2-17.8），视觉放大差异。建议在 caption 提示。\n- **M2**: Table 2 中 seed 42 使用 checkpoint-resumed model（Appendix N），与其他 seed 训练条件不完全一致，应更显著标注。\n- **M3**: Appendix I Table 9 的 α_eff negative bias（−0.029 to −0.031）说明系统性低估真实 real fraction，值得正文简要提及。\n\n---\n\n### Questions\n\n**Q1**: Table 1 的 epoch confound 分析能否扩展到 3 seeds？\n\n**Q2**: Adaptive b* vs. Uniform 的 paired differences（per-seed Δ）及标准差是多少？能否提供 paired t-test 或 bootstrap 95% CI？\n\n**Q3**: 在 ρ 未知的实际场景中，如何判断 contamination level 是否足以使 reweighting 有效？\n\n**Q4**: 1.7B 实验中 Δ≈−0.01 是否与 B=4 离散化有关？在 1.7B 中尝试过更大的 B 吗？\n\n**Q5**: Generative detector reversal（Table 10）是否可能是 calibration artifact？\n\n---\n\n### Missing References\n\n无明显缺失。51 条引用覆盖了 model collapse、data selection、importance weighting、synthetic text detection 等主要领域。引用验证：38 条 OpenAlex verified，6 条 not found 均为已知经典作品（Kish 1965, Owen 2013, Radford 2019 等），无伪造嫌疑。\n\n---\n\n### Scores\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 理论框架合理但 B=4 离散化使 continuous framing 与实际不符；epoch confound 核心发现仅基于单 seed；N=3 无统计检验 |\n| Excitement | 3/5 | epoch confound 有用但改进幅度小（Δ=−0.020），1.7B 无效果，self-contamination 限制影响 |\n| Reproducibility | 4/5 | 超参数和训练配置详尽，承诺 code/data release，扣分因 cross-model experiment 缺完整 evaluation |\n| Overall Assessment | **3** (Findings) | 两个有价值的贡献（epoch confound + adaptive framework），但核心证据链有缺陷。适合 Findings 但需补强统计证据。 |\n| Confidence | 4/5 | 仔细阅读全文含全部 appendix，对统计和重要性采样有足够背景判断 |",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告（方法严谨性 + 实验设计）\n\n### Summary (2-3 句)\n\n本文研究 continued LM pretraining 中 detect-and-reweight (D&R) 范式的有效性。核心发现有二：(1) D&R 报告的 PPL 优势主要来自 multi-epoch exposure 而非 distribution matching（epoch confound）；(2) 提出基于 α_eff + ESS 双约束的 adaptive reweighting 框架，避免 per-model grid search。在 Qwen3-0.6B 上 3 seeds 实验显示 Δ≈−0.020 PPL 的一致性改进，但改进幅度小且缺乏统计显著性检验；1.7B 规模实验（2 seeds）效果几乎消失。\n\n---\n\n### Strengths\n\n**S1. Epoch confound 的识别具有方法论价值。** 通过 epoch-matched control（Table 1），论文清晰展示 D&R 的 PPL 优势从 0.384 缩减至 Δ≈0.017，揭示了一个容易被忽视的实验设计陷阱。\n\n**S2. Dual-constraint 框架理论动机清晰。** α_eff（quality floor）+ ESS（stability ceiling）来源于重要性采样理论（Kish, 1965; Owen, 2013），Proposition 1-2 的单调性证明简洁正确（Appendix A）。将 grid search 降为单超参数 τ 的设计在工程上有实际价值。\n\n**S3. 消融实验覆盖全面。** 6 种方法对比（Uniform, Grid, ESS-only, Golden Ratio, Adaptive b*, D&R），加上 Appendix B 的完整 grid search 结果和 Appendix F 的 D&R threshold sensitivity（Table 6），充分展示了方法空间。\n\n**S4. Detector type 分析揭示了非直觉发现。** §5.3 和 Table 10 显示 generative detectors（GPT-2 perplexity, N-gram）尽管 AUC 可比甚至更高，却反转了 reweighting 的方向——detector signal type 比 discrimination accuracy 更重要。\n\n**S5. 诚实的 limitations 讨论。** 对 self-contamination 局限性、N=3 统计限制、ρ=0.2 失败模式、1.7B 初步性质均做了坦诚讨论。\n\n---\n\n### Weaknesses\n\n#### Must-Fix\n\n**N1** [critical] **Epoch confound——论文最重要的发现——仅基于单 seed（seed 42）**\n- 具体位置：Table 1（page 7），脚注 \"†Seed 42 only\"\n- 问题：Table 1 中 \"D&R full\" 和 \"D&R epoch-matched\" 两行均为 seed 42 单次实验。论文的核心 claim——\"gap shrinks from 0.384 to Δ≈0.017\"——完全依赖于该单 seed。仅 Adaptive b* 行使用了 3 seeds。由于 epoch-matched D&R 与 Adaptive b* 在 cosine schedule、LR curve 起点等训练动态上存在差异，单 seed 无法排除 seed-specific confound。\n- 为什么影响接收：这是论文的主要贡献之一。如果 epoch confound 在其他 seeds 上不成立或幅度不同，核心叙事将被削弱。\n- 建议修改方向：补充 seed 123 和 seed 456 的 epoch-matched comparison，或至少在 Limitations 中明确标注这是单 seed 的初步证据。\n\n**N2** [critical] **N=3 seeds + Δ=−0.020 PPL + 无正式统计检验 = 核心效果声明证据不足**\n- 具体位置：Table 2（page 7），Limitations §L（page 9）\n- 问题：Adaptive b* 的核心改进 Δ≈−0.020（mean PPL 17.674 vs. Uniform 17.694）来自 3 seeds。论文使用 \"directional consistency\" 替代统计检验。Table 2 注释 \"²\" 标注 seed 42 的 Adaptive b* 结果为 17.634，与其他 seed 存在约 0.04 的差异，暗示 seed 42 可能是 outlier。\n- 为什么影响接收：\"directional consistency\" framing 在 N=3 下可能 overstate 证据。Findings 级别论文仍需对核心定量 claim 提供最低限度的统计支撑。\n- 建议：(a) 报告 paired differences 及其标准差；(b) 执行 paired t-test 或 bootstrap CI；(c) 如果不显著，调整 claim 措辞强度。\n\n**N3** [critical] **B=4 micro-batch 下 α_eff 仅 5 个离散值，continuous framework 的实际意义存疑**\n- 具体位置：§3.3（page 4）\n- 问题：Proposition 1-2 建立在 α_eff 和 ESS 关于 b 的连续单调性基础上，但实际 b∈{0,1,2,3,4}，α_eff 只有 5 个取值。dual-constraint 中的 bisection 搜索退化为 brute-force 枚举。Appendix I（Table 9）报告 α_eff(0) 与真实 batch-level real fraction 的 MAE=0.114（约 11% 平均绝对误差）。\n- 为什么影响接收：理论和实践的 gap 未被充分弥合。在 B=4 下，\"adaptive\" 本质上是在 5 个固定权重配置中选择。\n- 建议：(a) 讨论 B=4 下离散化的理论影响；(b) 补充 B=8 或 B=16 的实验；(c) 或将 framing 调整为 discrete selection problem。\n\n#### Should-Fix\n\n**W1** [warning] **1.7B 规模结果（Δ≈−0.01, 2 seeds）实际上是负面证据，但论文措辞模糊**\n- 具体位置：§5.2（page 7）\n- 问题：1.7B 实验仅 2 seeds，Δ≈−0.01 在实验噪声范围内。论文称 \"insufficient for statistical conclusions about scale transfer\"，但这实际上是方法可能无效的信号。Downstream evaluation 也显示 \"no meaningful downstream impact\"。\n- 建议：更明确地定位为\"目前无证据表明方法在更大规模有效\"。\n\n**W2** [warning] **Self-contamination 设计的 external validity 严重受限**\n- 具体位置：§4，Limitations §Self-contamination，Appendix M\n- 问题：所有主实验使用 self-contamination（generator = trainee），AUC=0.94。Appendix M 的 cross-model transfer 实验是单 seed 且未报告 PPL comparison。真实 web 场景的 contamination 来自多源，AUC 可能远低于 0.94。\n- 建议：补充至少一个 cross-model contamination 完整实验，或在 title/abstract 中限定为 self-contamination。\n\n**W3** [warning] **ρ=0.2 失败模式未充分探索**\n- 具体位置：§5.4 / Appendix H\n- 问题：ρ=0.2 时方法退化 +0.046 PPL，但未探索是否可通过调整 τ 或 detector threshold 应对，也未提供诊断方法判断何时 reweighting 有益。\n\n**W4** [warning] **Detector calibration 敏感性未分析**\n- 具体位置：§4，Appendix K\n- 问题：方法依赖 post-hoc temperature scaling（T=0.204, ECE=0.05），但未分析 calibration 质量对最终 PPL 的影响。\n\n#### Minor\n\n- **M1**: Figure 1 y 轴压缩（~17.2-17.8），视觉放大差异。建议在 caption 提示。\n- **M2**: Table 2 中 seed 42 使用 checkpoint-resumed model（Appendix N），与其他 seed 训练条件不完全一致，应更显著标注。\n- **M3**: Appendix I Table 9 的 α_eff negative bias（−0.029 to −0.031）说明系统性低估真实 real fraction，值得正文简要提及。\n\n---\n\n### Questions\n\n**Q1**: Table 1 的 epoch confound 分析能否扩展到 3 seeds？\n\n**Q2**: Adaptive b* vs. Uniform 的 paired differences（per-seed Δ）及标准差是多少？能否提供 paired t-test 或 bootstrap 95% CI？\n\n**Q3**: 在 ρ 未知的实际场景中，如何判断 contamination level 是否足以使 reweighting 有效？\n\n**Q4**: 1.7B 实验中 Δ≈−0.01 是否与 B=4 离散化有关？在 1.7B 中尝试过更大的 B 吗？\n\n**Q5**: Generative detector reversal（Table 10）是否可能是 calibration artifact？\n\n---\n\n### Missing References\n\n无明显缺失。51 条引用覆盖了 model collapse、data selection、importance weighting、synthetic text detection 等主要领域。引用验证：38 条 OpenAlex verified，6 条 not found 均为已知经典作品（Kish 1965, Owen 2013, Radford 2019 等），无伪造嫌疑。\n\n---\n\n### Scores\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 理论框架合理但 B=4 离散化使 continuous framing 与实际不符；epoch confound 核心发现仅基于单 seed；N=3 无统计检验 |\n| Excitement | 3/5 | epoch confound 有用但改进幅度小（Δ=−0.020），1.7B 无效果，self-contamination 限制影响 |\n| Reproducibility | 4/5 | 超参数和训练配置详尽，承诺 code/data release，扣分因 cross-model experiment 缺完整 evaluation |\n| Overall Assessment | **3** (Findings) | 两个有价值的贡献（epoch confound + adaptive framework），但核心证据链有缺陷。适合 Findings 但需补强统计证据。 |\n| Confidence | 4/5 | 仔细阅读全文含全部 appendix，对统计和重要性采样有足够背景判断 |",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-20T03:16:30.163914+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4522
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-20T03:16:35.095031+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-20T03:16:35.145666+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-20T03:16:39.011366+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-20T03:16:39.011817+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 350 · 2026-05-20T03:16:45.547353+00:00_

审稿完成。报告已提交至 Review Director，Overall Assessment 给出 **3 (Findings)**。

核心判断：论文有两个有价值的贡献（epoch confound 识别 + adaptive reweighting framework），但三个 critical 问题需要解决——epoch confound 核心发现仅基于单 seed、N=3 无统计检验的效果声明、B=4 离散化与 continuous framing 的 gap。补强这些证据后评分可能提升。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 351 · 2026-05-20T03:17:56.043280+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿报告

**审查侧重**: 新颖性 + 完整性 + 呈现质量

### Summary
本文研究 detect-and-reweight (D&R) 范式在污染语料续训中的有效性。核心发现是 D&R 的 PPL 优势主要来自 multi-epoch exposure（epoch confound），epoch-matched 对照组将差距从 0.384 压缩至 Δ≈0.017。论文提出 adaptive b* 框架（dual constraint: quality floor τ + stability ceiling n_min），在 Qwen3-0.6B / 132M FineWeb tokens / 40% 自污染设定下实现 Δ≈-0.020 的一致但微小的改进。

### Strengths
S1. Epoch confound 发现是真正有价值的方法论贡献。
S2. Dual-constraint 理论框架有扎实的统计基础。
S3. 在测试范围内的消融非常充分。
S4. Limitations 诚实且全面。
S5. 可复现性好。

### Weaknesses (Must-Fix)

**N1 [critical] Title 和 Abstract 对实验范围严重 overpromise。**
Title "When Does Detect-and-Reweight Work?" 构建了全面回答的预期，实际仅覆盖一个模型族 (Qwen3-0.6B)、一种污染类型 (self-contamination)、一个数据集 (FineWeb 132M)、一个主要污染比 (ρ=0.4)。论文自身证据直接否定了 title 的隐含承诺：ρ=0.2 失效，1.7B 无效果。建议收窄为 "Epoch Confounds in Detect-and-Reweight: A Case Study in Continued LM Pretraining"。

**N2 [critical] "No evidence of distribution matching" 的证据强度不足。**
结论基于 OOD improvements 与 ID improvements 比较，但 (a) 只有 3 seeds，SE 大幅重叠；(b) OOD 与 ID 的 Δ 差异仅约 0.01 PPL，在噪声范围内；(c) 论文声称 absence of evidence 而非 evidence of absence，需要远高于当前 sample size 的统计功效。

### Weaknesses (Should-Fix)

**W1 [warning] Self-contamination 设定的外部效度严重不足。**
Appendix M cross-model transfer 显示 "inconsistent quality differences"，实际否定了方法在非 self-contamination 场景的有效性，但被放在附录中轻描淡写。

**W2 [warning] "Eliminates grid search" 表述有误导性。**
τ=0.7 本身通过 3-seed validation 选出。实际上是将搜索空间从 (b) 变为 (τ, n_min)——"reduces sensitivity" 而非 "eliminates search"。

**W3 [warning] 实际收益极其微小，且无 downstream 表现提升。**
Adaptive b* 仅 Δ≈-0.020 PPL。Table 7 下游 benchmark 显示 "no meaningful downstream impact"。需更充分论证 PPL gain 的实际价值。

**W4 [warning] 1.7B 实验结果被边缘化处理。**
1.7B 无效果 (13.26 vs 13.26)，对于 title 问 "when does it work" 的论文，这是核心发现，不应藏在附录中。方法有效条件极为狭窄 (0.6B, self-contamination, ρ≥0.4)。

**W5 [warning] 缺少对 epoch confound 的机制解释。**
论文只证明了 epoch confound 存在，没有解释为什么 multi-epoch exposure 能产生优势。是 unique token coverage？Learning dynamics？Curriculum effect？

### Minor
M1. Figure 1 缺少 confidence band。
M2. Abstract 精度层级不一致。
M3. vehtari2024psis 年份标注。
M4. Appendix M checkpoints "not retained" 暗示实验流程质量控制问题。

### Questions
Q1. Epoch confound 的机制是什么？
Q2. 能否量化 batch-level α_eff estimation 对 ρ 的最低要求？
Q3. Cross-model transfer 的 "inconsistent quality differences" 是否意味着框架绑定于 self-contamination？
Q4. PPL gain 但无 downstream gain 如何理解？
Q5. 检测器 AUC 的最低有效阈值是多少？

### Missing References
1. Ibrahim et al. (2024) "Simple and Scalable Strategies to Continually Pre-train Large Language Models" (NAACL 2024)
2. Gupta et al. (2023) "Continual Pre-Training of Large Language Models: How to (re)warm your model?"
3. Maini et al. (2024) "Rephrasing the Web" — synthetic data 在 pretraining 中的系统性使用

### Scores
Soundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5, Clarity 3.5/5, Novelty 3/5, Completeness 2.5/5
**Overall: 3.0 (Findings)**, Confidence 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-20T03:19:49.060056+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: Title 和 Abstract overpromise**\n同意。Title \"When Does Detect-and-Reweight Work?\" 暗示全面回答，但实际仅覆盖 Qwen3-0.6B / self-contamination / FineWeb 132M / ρ=0.4。论文自身证据直接限制了适用范围：ρ=0.2 退化（Appendix H），1.7B 无效果（§5.2），cross-model 结果 inconsistent（Appendix M）。epoch confound 发现具有一定普遍性，但 adaptive reweighting 的有效性 claim 需收窄。\n\n**[AGREE] R2-N2: \"No evidence of distribution matching\" 证据强度不足**\n同意，与我的 N2 呼应。N=3 且 SE 重叠条件下，null result 的统计功效极低。§5.2 的 \"providing no evidence of distribution matching\" 措辞偏强，应改为更审慎表述。\n\n### Should-Fix\n\n**[AGREE] R2-W1: Self-contamination 外部效度不足**\n完全同意，与我的 W2 一致。Appendix M 连 PPL 对比都省略了，实验体系事实上仅支撑 self-contamination。\n\n**[AGREE] R2-W2: \"Eliminates grid search\" 表述有误导性**\n同意。τ=0.7 通过 3-seed validation 在 5 个候选值中选出（§3.4），加上 n_min 设计选择，实际是从 grid over b 替换为 (τ, n_min) 的 joint space。\"Reduces sensitivity\" 比 \"eliminates search\" 更准确。\n\n**[REBUT] R2-W3: 实际收益极其微小，且无 downstream 表现提升**\n部分反驳。事实陈述正确，但论文主要贡献是 (1) 识别 epoch confound，(2) 在控制 confound 后表征 reweighting 真实效果。\"效果微小\" 本身就是核心发现——D&R 在控制 epoch confound 后的真实贡献远小于文献暗示。微小收益不应视为方法失败，而是对领域的重要 calibration。但论文应更显式地阐述这一 calibration 意义。\n\n**[AGREE] R2-W4: 1.7B 结果被边缘化处理**\n同意，与我的 W1 一致。对 \"when does it work\" 的论文，1.7B null result 和 ρ=0.2 failure 是回答该问题的关键证据，不应边缘化。\n\n**[AGREE] R2-W5: 缺少对 epoch confound 的机制解释**\n同意，这是我审稿时未充分关注的有价值视角。可能的假说包括：(a) filtering 减少 unique token coverage 导致重复训练；(b) 高权重 clean samples 的 curriculum effect；(c) cosine schedule 在不同 step 数下的 learning dynamics 差异。即使无确定性解释，讨论这些假说也会增强分析深度。\n\n### Minor\n\n[AGREE] R2-M1: Figure 1 缺 confidence band。\n[AGREE] R2-M2: Abstract 精度不一致。\n[REBUT] R2-M3: vehtari2024psis 的 JMLR 正式发表确实是 2024 年（Volume 25），preprint 始于 2015，bib 标注 2024 合理。\n[AGREE] R2-M4: Appendix M checkpoints \"not retained\" 暗示实验流程问题，结果不可重复验证。\n\n### Questions 回应\n\nR2-Q1: 同 W5，需补充机制讨论。\nR2-Q2: 与我的 W3 呼应，ρ 下界对实际部署重要。\nR2-Q3: 基于 Appendix M 有限证据倾向同意担忧，但证据不足得确定性结论。\nR2-Q4: PPL 改进可能仅反映 in-distribution LM 微小提升，不足以传导到 downstream accuracy。\nR2-Q5: Table 10 的差异更多来自 detector type 而非 AUC 水平，需同一 type 内变化 AUC 来回答。\n\n### Missing References\n\n[AGREE] 三篇均直接相关：Ibrahim et al. (2024) 是 continued pretraining 重要基线；Gupta et al. (2023) re-warming 与 epoch confound 机制相关；Maini et al. (2024) 是 web contamination motivation 的重要背景。\n\n### 综合评估\n\nR2 与我的审稿在主要问题上高度一致（epoch confound 单 seed、统计检验缺失、self-contamination 局限、1.7B 边缘化）。R2 额外指出的 title overpromise（N1）、grid search 误导（W2）和机制解释缺失（W5）是有价值的补充。我对 W3 有部分不同意见——认为微小收益本身是论文的 finding 而非缺陷。\n\n总体评分维持 **Overall 3.0 (Findings)**，与 R2 一致。论文适合 Findings 但需显著补强统计证据和调整 framing。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: Title 和 Abstract overpromise**\n同意。Title \"When Does Detect-and-Reweight Work?\" 暗示全面回答，但实际仅覆盖 Qwen3-0.6B / self-contamination / FineWeb 132M / ρ=0.4。论文自身证据直接限制了适用范围：ρ=0.2 退化（Appendix H），1.7B 无效果（§5.2），cross-model 结果 inconsistent（Appendix M）。epoch confound 发现具有一定普遍性，但 adaptive reweighting 的有效性 claim 需收窄。\n\n**[AGREE] R2-N2: \"No evidence of distribution matching\" 证据强度不足**\n同意，与我的 N2 呼应。N=3 且 SE 重叠条件下，null result 的统计功效极低。§5.2 的 \"providing no evidence of distribution matching\" 措辞偏强，应改为更审慎表述。\n\n### Should-Fix\n\n**[AGREE] R2-W1: Self-contamination 外部效度不足**\n完全同意，与我的 W2 一致。Appendix M 连 PPL 对比都省略了，实验体系事实上仅支撑 self-contamination。\n\n**[AGREE] R2-W2: \"Eliminates grid search\" 表述有误导性**\n同意。τ=0.7 通过 3-seed validation 在 5 个候选值中选出（§3.4），加上 n_min 设计选择，实际是从 grid over b 替换为 (τ, n_min) 的 joint space。\"Reduces sensitivity\" 比 \"eliminates search\" 更准确。\n\n**[REBUT] R2-W3: 实际收益极其微小，且无 downstream 表现提升**\n部分反驳。事实陈述正确，但论文主要贡献是 (1) 识别 epoch confound，(2) 在控制 confound 后表征 reweighting 真实效果。\"效果微小\" 本身就是核心发现——D&R 在控制 epoch confound 后的真实贡献远小于文献暗示。微小收益不应视为方法失败，而是对领域的重要 calibration。但论文应更显式地阐述这一 calibration 意义。\n\n**[AGREE] R2-W4: 1.7B 结果被边缘化处理**\n同意，与我的 W1 一致。对 \"when does it work\" 的论文，1.7B null result 和 ρ=0.2 failure 是回答该问题的关键证据，不应边缘化。\n\n**[AGREE] R2-W5: 缺少对 epoch confound 的机制解释**\n同意，这是我审稿时未充分关注的有价值视角。可能的假说包括：(a) filtering 减少 unique token coverage 导致重复训练；(b) 高权重 clean samples 的 curriculum effect；(c) cosine schedule 在不同 step 数下的 learning dynamics 差异。即使无确定性解释，讨论这些假说也会增强分析深度。\n\n### Minor\n\n[AGREE] R2-M1: Figure 1 缺 confidence band。\n[AGREE] R2-M2: Abstract 精度不一致。\n[REBUT] R2-M3: vehtari2024psis 的 JMLR 正式发表确实是 2024 年（Volume 25），preprint 始于 2015，bib 标注 2024 合理。\n[AGREE] R2-M4: Appendix M checkpoints \"not retained\" 暗示实验流程问题，结果不可重复验证。\n\n### Questions 回应\n\nR2-Q1: 同 W5，需补充机制讨论。\nR2-Q2: 与我的 W3 呼应，ρ 下界对实际部署重要。\nR2-Q3: 基于 Appendix M 有限证据倾向同意担忧，但证据不足得确定性结论。\nR2-Q4: PPL 改进可能仅反映 in-distribution LM 微小提升，不足以传导到 downstream accuracy。\nR2-Q5: Table 10 的差异更多来自 detector type 而非 AUC 水平，需同一 type 内变化 AUC 来回答。\n\n### Missing References\n\n[AGREE] 三篇均直接相关：Ibrahim et al. (2024) 是 continued pretraining 重要基线；Gupta et al. (2023) re-warming 与 epoch confound 机制相关；Maini et al. (2024) 是 web contamination motivation 的重要背景。\n\n### 综合评估\n\nR2 与我的审稿在主要问题上高度一致（epoch confound 单 seed、统计检验缺失、self-contamination 局限、1.7B 边缘化）。R2 额外指出的 title overpromise（N1）、grid search 误导（W2）和机制解释缺失（W5）是有价值的补充。我对 W3 有部分不同意见——认为微小收益本身是论文的 finding 而非缺陷。\n\n总体评分维持 **Overall 3.0 (Findings)**，与 R2 一致。论文适合 Findings 但需显著补强统计证据和调整 framing。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-20T03:19:53.338673+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4278
}
```

</details>

---


### Assistant

_source line 354 · 2026-05-20T03:19:59.247171+00:00_

交叉回应已提交。

总结：R2 的 11 个 Weakness/Question 中，我 **AGREE 9 条，REBUT 2 条**（W3 部分反驳——微小收益本身是 finding 而非缺陷；M3 反驳——vehtari2024psis 标注 2024 正式发表年份合理）。两位 reviewer 在核心问题上高度一致，评分均为 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

54 recorded events


### User

_source line 355 · 2026-05-21T11:27:44.831935+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**。

## 审稿目标
- 目标 venue: EMNLP 2026（ARR May 2026 cycle，截止 2026-05-25）
- 格式要求: ACL 两栏模板，long paper 正文 8 页限制，参考文献不限，double-blind 匿名
- 必须包含: Limitations 章节 + Responsible NLP Research Checklist

## 论文信息
- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
- 标题: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"

## 你的审查侧重

### 1. 方法严谨性
- Dual-constraint 框架（α_eff quality floor + ESS stability ceiling）的理论动机是否充分？Proposition 1-2 的证明是否正确？
- 每 batch 自适应 b* 的 bisection 算法在 B=4 这样极小的 batch size 下，α_eff 只有 5 个离散值 {0, 0.25, 0.5, 0.75, 1.0}，这是否严重削弱了方法的理论优雅性？
- "minimum intervention" 设计选择（取满足 quality floor 的最小 b）是否有充分的理论或实证支撑？
- 对 wang2026survive 收敛理论的引用是否恰当——该理论假设已知 contamination proportion α，而本文不要求此假设

### 2. 实验设计
- Epoch confound 分析：epoch-matched comparison 的实验设计是否公平？D&R 在 2,533 steps 用相同 cosine schedule（6,103 steps 设计的）是否引入了 LR schedule confound？
- 统计检验：N=3 的 paired t-test 是否足够？p=0.025 在 df=2 下的可靠性？
- Self-contamination 设计（generator = trainee）的生态效度：这是否过于简化了真实场景？
- Detector 选择：为什么用 AUC=0.94 的 TF-IDF+LR 而非更强的 neural detector？是否 cherry-pick 了最有利的 detector？
- 3 detectors 的对比能否可靠地分离 calibration vs discrimination 效应？
- ρ=0.2 失败、1.7B 效果减弱——这是否限制了方法的实用范围？
- Grid search 只在 seed 42 做了完整 9 点扫描，其他 seed 只测了部分 b 值——是否对 grid-best baseline 不公平？

### 3. 效果大小
- Δ=-0.020 PPL（约 0.11% 相对改进）在实践中是否有意义？
- 下游任务完全没有改善（|Δ|≤0.01），这是否削弱了论文的实用价值主张？

请按以下结构输出审稿意见：
1. Summary（2-3句）
2. Strengths（逐条）
3. Weaknesses（逐条，标注严重程度：critical/major/minor）
4. Questions for Authors
5. Missing References（如有）
6. Overall Assessment（评分 + 置信度）

评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-21T11:27:53.187309+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-21T11:27:53.237890+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-21T11:27:56.498482+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-21T11:27:57.201219+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-21T11:28:03.552947+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also
…[truncated 1248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7054
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-21T11:28:05.984347+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 571.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weig
…[truncated 333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8783
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-21T11:28:10.854868+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement, Reproducibility, and any other dimensions with their full scoring rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement, Reproducibility, and any other dimensions with their full scoring rubrics."
  }
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-21T11:28:11.808989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-21T11:28:12.162365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-21T11:28:12.800593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 991
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-21T11:28:12.801037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 367 · 2026-05-21T11:28:13.120650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-21T11:28:13.627101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-21T11:28:13.828933+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1666
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-21T11:28:15.455714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2654
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-21T11:28:16.885760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3765
}
```

</details>

---


### Tool result

_source line 372 · 2026-05-21T11:28:17.336665+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3709
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-21T11:28:19.262696+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award"
- **4**: "Conference acceptance"
- **3**: "Findings of the ACL"
- **2**: "Resubmit next cycle"
- **1.5**: "Resubmit after next cycle"
- **1**: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: 
…[truncated 536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8407
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-21T11:28:23.740057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-21T11:28:24.646025+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-21T11:28:24.746785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-21T11:28:25.149445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-21T11:28:26.254631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1507
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-21T11:28:26.255048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-21T11:28:27.466360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2316
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-21T11:28:27.717430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-21T11:28:28.073154+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-21T11:28:29.281768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3026
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-21T11:28:29.937184+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2219
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-21T11:28:31.751576+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 354.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 439.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 394.2}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3678
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-21T11:28:36.778749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 387 · 2026-05-21T11:28:37.231861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-21T11:28:37.986927+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1208
}
```

</details>

---


### Tool call

_source line 389 · 2026-05-21T11:28:38.138631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-21T11:28:38.139079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-21T11:28:39.095110+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1863
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-21T11:28:39.095525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-21T11:28:39.247809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-21T11:28:39.348650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-21T11:28:39.550413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-21T11:28:40.259085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1163
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-21T11:28:40.261030+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-21T11:30:28.774997+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool call

_source line 399 · 2026-05-21T11:30:30.481212+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, including all review criteria, what reviewers should focus on, scoring rubrics, and any specific instructions about how to evaluate soundness, novelty, significance, and experimental rigor. Include any guidance about what constitutes critical vs minor issues."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, including all review criteria, what reviewers should focus on, scoring rubrics, and any specific instructions about how to evaluate soundness, novelty, significance, and experimental rigor. Include any guidance about what constitutes critical vs minor issues."
  }
}
```

</details>

---


### Tool result

_source line 400 · 2026-05-21T11:31:40.822373+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 51, \"total_citations\": 79, \"unique_cited_keys\": 51, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 38, \"online_not_found\": 6, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"katharopoulos2018not\", \"type\": \"inproceedings\", \"title\": \"Not All Samples Are Created Equal: Deep Learning with Importance Sampling\", \"authors\": \"\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"ren2018learning\", \"type\": \"inproceedings\", \"title\": \"Learning to Reweight Examples for Robust Deep Learning\", \"authors\": \"Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"chen2024bull\", \"type\": \"article\", \"title\": \"Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves LLM Generalization\", \"authors\": \"Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.14270\"}, {\"key\": \"kang2025demystifying\", \"type\": \"inproceedings\", \"title\": \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\", \"authors\": \"Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Ch...\", \"year\": \"2025\", \"venue\": \"EMNLP\"}, {\"key\": \"zibakhsh2025fortifai\", \"type\": \"article\", \"title\": \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\", \"authors\": \"Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koush...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.08972\"}, {\"key\": \"yi2025escaping\", \"type\": \"article\", \"title\
…[truncated 38332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 72047
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-21T11:31:53.233085+00:00_

# ARR Reviewer Guidelines: Complete Summary

## Core Review Tasks

Reviewers must complete four main tasks:

1. **Allocate time** for reviewing and discussion phases
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write substantive reviews** addressing methodology and contributions
4. **Engage in post-response discussion** and update assessments

## Key Review Criteria

### Soundness Assessment
The guidelines emphasize that "soundness scores must be justified by the text of the review." Low scores require explicit evidence of technical flaws. Reviewers should verify:

- Technical correctness of methodology
- Validity of proofs and formal statements
- Reproducibility details and data availability
- Statistical significance of results
- Appropriate scope of claims

### Novelty and Contribution
Rather than demanding SOTA results, reviewers should evaluate whether papers advance knowledge. The guidelines specifically warn against dismissing work because:

- Results seem "obvious in retrospect"
- Methods are "too simple"
- Work focuses on non-English languages
- Papers are reproductions or analyses

### Excitement vs. Soundness
These are explicitly separated. Papers can be technically sound without being personally interesting to the reviewer—this distinction matters for differentiated scoring.

## Critical vs. Minor Issues

**Critical flaws (potential desk rejection):**
- Anonymity violations
- Hallucinated references
- Style/length violations
- Missing Limitations section
- Egregious responsible NLP checklist violations
- Ethics concerns requiring additional review

**Common problematic criticisms** (flagged as potentially biased):
- Lack of SOTA performance
- Negative results
- Simple methodologies
- Niche topics
- Language-specific focus

## Review Quality Standards

### Tone and Professionalism
Reviewers must maintain "professional and neutral" communication. The guidelines note that "sarcastic or insulting reviews" undermine peer review's 
…[truncated 2171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 82751
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-21T11:34:39.814537+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n### 论文\n\"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n\n---\n\n## 1. Summary\n\n本文研究 Detect-and-Reweight (D&R) 范式在含合成文本污染的 continued LM pretraining 中何时有效。核心发现有二：(1) D&R 的 PPL 优势中 96% 归因于 epoch confound（多轮数据重复曝光），epoch-matched 后优势从 0.384 缩至 0.017；(2) 提出 dual-constraint 自适应 reweighting 框架（α_eff quality floor + ESS stability ceiling），在 Qwen3-0.6B / 132M token / 40% self-contamination 设定下取得 Δ=−0.020 PPL 改进（~0.11%），但下游任务无可测量改善。\n\n## 2. Strengths\n\n**S1. Epoch confound 分析有实质贡献。** Table 1 的 epoch-matched 实验将 0.384 PPL gap 分解为 epoch 效应（96%）和真实 filtering 效应（4%），对社区理解 D&R 的实际机制有意义。\n\n**S2. 框架形式化清晰。** Dual-constraint 的数学表述简洁（§3.2），Proposition 1–2 证明正确（Appendix A），三种 regime 划分直观。\n\n**S3. 消融实验覆盖面广。** Grid search 全空间、threshold 敏感性、contamination level、scale、constraint regime 分解、detector 家族均有系统消融。\n\n**S4. 诚实的 limitations。** §8 明确承认 self-contamination 局限、单模型规模、缺乏下游改善。\n\n**S5. 引用质量好。** 51 条引用无伪造、无遗漏。\n\n## 3. Weaknesses\n\n### Must-Fix (Critical)\n\n**W1 [critical] 效果大小不足以支撑方法论贡献。**\n- 位置：Table 2, §5.1, §H\n- Adaptive b* 的 PPL 改进 Δ=−0.020（0.11%），接近 noise margin（std ±0.006–0.007）。下游任务 |Δ|≤0.01（§H: \"no meaningful downstream impact\"）。Abstract 用 \"consistent improvements\" 描述这一结果过于乐观。论文在 analysis paper 和 method paper 之间定位模糊，后者的 evidence 不足。\n- 建议：重新定位为分析论文，或补充更大规模实验。\n\n**W2 [critical] B=4 下 dual-constraint 框架实质退化。**\n- 位置：§3.3, Algorithm 1, Figure 2\n- α_eff 仅有 5 个离散值，α_eff-binding regime 占比极低（~0.2%）。Quality floor 约束几乎不生效，方法实际退化为 \"ESS-only + clean batch 不干预\"。ESS-only vs. Adaptive 的差距更可能归因于 ESS-only 在 clean batch 上的崩溃（§5.1），而非 α_eff floor 的贡献。\n- 建议：在 B≥16 下验证，或明确承认小 batch 下退化。\n\n**W3 [critical] Epoch-matched 比较的 LR schedule confound。**\n- 位置：Table 1 脚注\n- D&R epoch-matched 在 2,533/6,103 步时 LR 仍处 cosine 中段（~64% 峰值），非训练终态。论文以 \"if anything, favors D&R\" 打发，但 warmer LR 影响方向不确定。Epoch confound 是论文最强贡献，但其 epoch-matched 比较引入新 confound 削弱了可靠性。\n- 建议：补充为 2,533 步独立设计 cosine schedule 的对照。\n\n### Should-Fix (Major)\n\n**W4 [major] N=3 统计功效不足。** df=2 下 p=0.025 可靠性有限。Δ=−0.020 的微小效应需更多 seeds 或 bootstrap CI。\n\n**W5 [major] Self-contamination 生态效度受限。** Generator=trainee 使 AUC=0.94 人为偏高。Appendix N 的 cross-model 实验（单 seed、无 PPL）不足以证明泛化。标题问 \"When Does D&R Work\" 但仅在最有利场景下回答。\n\n**W6 [major] Grid search baseline 公平性。** 完整 9 点 grid 仅在 seed 42 做，最优 b=0.3 是 seed 42 特定的，可能对 grid-best baseline 不公平。\n\n**W7 [major] ρ=0.2 失败 + 1.7B 效果减弱限制实用范围。** 方法仅在高污染率 + 小模型 + 高 AUC detector 交集下有效。\n\n**W8 [major] Wang et al. (2026) 理论假设不匹配。** 该理论假设已知 α，本文用 α_eff（r=0.70, bias≈−0.03）近似，理论保证不能直接迁移。\n\n### Minor\n\n**W9 [minor]** \"Minimum intervention\" 缺乏与其他 b 选择策略的消融对比。\n\n**W10 [minor]** §3.3 constraint regime 占比数字与 Figure 2 视觉不完全一致。\n\n**W11 [minor]** Figure 1 的 shaded region 边界与文字描述不一致。\n\n## 4. Questions for Authors\n\nQ1. B≥16 下 α_eff-binding regime 占比？dual-constraint 两个约束是否都有实质作用？\nQ2. 为 D&R epoch-matched 独立设计 2,533 步 cosine schedule 后，Δ=0.017 是否改变？\nQ3. Detector AUC 与方法有效性的定量关系？\nQ4. Seed 123/456 各自的 grid-best b 是多少？\nQ5. 是否尝试过 fine-tuned BERT-based detector 来更充分分离 calibration 和 discrimination？\n\n## 5. Missing References\n\n无关键遗漏。\n\n## 6. Overall Assessment\n\n**Overall: 2.5 (Borderline Findings)**\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/5 | Epoch confound 分析合理但有 LR confound；dual-constraint 在 B=4 下退化；理论引用条件不完全匹配 |\n| Excitement | 2/5 | Epoch confound 有价值但效果大小（0.11% PPL, 0 downstream）限制影响力 |\n| Reproducibility | 4/5 | 细节详尽，承诺 release |\n| Confidence | 4/5 | 仔细检查了方法、证明、实验和统计 |\n\n**一句话总结：** Epoch confound 分析有价值，但 adaptive method 效果微弱（0.11% PPL, 下游为零），B=4 下框架退化、LR confound 未解决、N=3 功效不足共同削弱说服力。建议重新定位为分析论文或补充更大规模实验。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n### 论文\n\"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n\n---\n\n## 1. Summary\n\n本文研究 Detect-and-Reweight (D&R) 范式在含合成文本污染的 continued LM pretraining 中何时有效。核心发现有二：(1) D&R 的 PPL 优势中 96% 归因于 epoch confound（多轮数据重复曝光），epoch-matched 后优势从 0.384 缩至 0.017；(2) 提出 dual-constraint 自适应 reweighting 框架（α_eff quality floor + ESS stability ceiling），在 Qwen3-0.6B / 132M token / 40% self-contamination 设定下取得 Δ=−0.020 PPL 改进（~0.11%），但下游任务无可测量改善。\n\n## 2. Strengths\n\n**S1. Epoch confound 分析有实质贡献。** Table 1 的 epoch-matched 实验将 0.384 PPL gap 分解为 epoch 效应（96%）和真实 filtering 效应（4%），对社区理解 D&R 的实际机制有意义。\n\n**S2. 框架形式化清晰。** Dual-constraint 的数学表述简洁（§3.2），Proposition 1–2 证明正确（Appendix A），三种 regime 划分直观。\n\n**S3. 消融实验覆盖面广。** Grid search 全空间、threshold 敏感性、contamination level、scale、constraint regime 分解、detector 家族均有系统消融。\n\n**S4. 诚实的 limitations。** §8 明确承认 self-contamination 局限、单模型规模、缺乏下游改善。\n\n**S5. 引用质量好。** 51 条引用无伪造、无遗漏。\n\n## 3. Weaknesses\n\n### Must-Fix (Critical)\n\n**W1 [critical] 效果大小不足以支撑方法论贡献。**\n- 位置：Table 2, §5.1, §H\n- Adaptive b* 的 PPL 改进 Δ=−0.020（0.11%），接近 noise margin（std ±0.006–0.007）。下游任务 |Δ|≤0.01（§H: \"no meaningful downstream impact\"）。Abstract 用 \"consistent improvements\" 描述这一结果过于乐观。论文在 analysis paper 和 method paper 之间定位模糊，后者的 evidence 不足。\n- 建议：重新定位为分析论文，或补充更大规模实验。\n\n**W2 [critical] B=4 下 dual-constraint 框架实质退化。**\n- 位置：§3.3, Algorithm 1, Figure 2\n- α_eff 仅有 5 个离散值，α_eff-binding regime 占比极低（~0.2%）。Quality floor 约束几乎不生效，方法实际退化为 \"ESS-only + clean batch 不干预\"。ESS-only vs. Adaptive 的差距更可能归因于 ESS-only 在 clean batch 上的崩溃（§5.1），而非 α_eff floor 的贡献。\n- 建议：在 B≥16 下验证，或明确承认小 batch 下退化。\n\n**W3 [critical] Epoch-matched 比较的 LR schedule confound。**\n- 位置：Table 1 脚注\n- D&R epoch-matched 在 2,533/6,103 步时 LR 仍处 cosine 中段（~64% 峰值），非训练终态。论文以 \"if anything, favors D&R\" 打发，但 warmer LR 影响方向不确定。Epoch confound 是论文最强贡献，但其 epoch-matched 比较引入新 confound 削弱了可靠性。\n- 建议：补充为 2,533 步独立设计 cosine schedule 的对照。\n\n### Should-Fix (Major)\n\n**W4 [major] N=3 统计功效不足。** df=2 下 p=0.025 可靠性有限。Δ=−0.020 的微小效应需更多 seeds 或 bootstrap CI。\n\n**W5 [major] Self-contamination 生态效度受限。** Generator=trainee 使 AUC=0.94 人为偏高。Appendix N 的 cross-model 实验（单 seed、无 PPL）不足以证明泛化。标题问 \"When Does D&R Work\" 但仅在最有利场景下回答。\n\n**W6 [major] Grid search baseline 公平性。** 完整 9 点 grid 仅在 seed 42 做，最优 b=0.3 是 seed 42 特定的，可能对 grid-best baseline 不公平。\n\n**W7 [major] ρ=0.2 失败 + 1.7B 效果减弱限制实用范围。** 方法仅在高污染率 + 小模型 + 高 AUC detector 交集下有效。\n\n**W8 [major] Wang et al. (2026) 理论假设不匹配。** 该理论假设已知 α，本文用 α_eff（r=0.70, bias≈−0.03）近似，理论保证不能直接迁移。\n\n### Minor\n\n**W9 [minor]** \"Minimum intervention\" 缺乏与其他 b 选择策略的消融对比。\n\n**W10 [minor]** §3.3 constraint regime 占比数字与 Figure 2 视觉不完全一致。\n\n**W11 [minor]** Figure 1 的 shaded region 边界与文字描述不一致。\n\n## 4. Questions for Authors\n\nQ1. B≥16 下 α_eff-binding regime 占比？dual-constraint 两个约束是否都有实质作用？\nQ2. 为 D&R epoch-matched 独立设计 2,533 步 cosine schedule 后，Δ=0.017 是否改变？\nQ3. Detector AUC 与方法有效性的定量关系？\nQ4. Seed 123/456 各自的 grid-best b 是多少？\nQ5. 是否尝试过 fine-tuned BERT-based detector 来更充分分离 calibration 和 discrimination？\n\n## 5. Missing References\n\n无关键遗漏。\n\n## 6. Overall Assessment\n\n**Overall: 2.5 (Borderline Findings)**\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/5 | Epoch confound 分析合理但有 LR confound；dual-constraint 在 B=4 下退化；理论引用条件不完全匹配 |\n| Excitement | 2/5 | Epoch confound 有价值但效果大小（0.11% PPL, 0 downstream）限制影响力 |\n| Reproducibility | 4/5 | 细节详尽，承诺 release |\n| Confidence | 4/5 | 仔细检查了方法、证明、实验和统计 |\n\n**一句话总结：** Epoch confound 分析有价值，但 adaptive method 效果微弱（0.11% PPL, 下游为零），B=4 下框架退化、LR confound 未解决、N=3 功效不足共同削弱说服力。建议重新定位为分析论文或补充更大规模实验。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-21T11:34:43.428786+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-21T11:34:47.942908+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-21T11:34:47.993505+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-21T11:34:51.605235+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-21T11:34:51.655968+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 408 · 2026-05-21T11:34:58.142975+00:00_

审稿完成。评分 **Overall 2.5 (Borderline Findings)**，已提交 Director。

核心判断：Epoch confound 分析是有价值的贡献（将 D&R 的 96% PPL 优势归因于多轮曝光），但 adaptive reweighting 方法的效果过小（0.11% PPL、下游为零），加上 B=4 下框架退化为近似 single-constraint、epoch-matched 比较引入 LR confound、N=3 统计功效不足，整体说服力不够。建议作者将论文重新定位为分析论文，或补充更大规模实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 409 · 2026-05-21T11:35:49.863648+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每一条 Weakness/Strength/Question，标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

### 1. Summary
本文研究 D&R 方法在含合成数据污染的 continued LM pretraining 中的有效性。三个贡献：(1) 识别 epoch confound——D&R 优势主要来自多 epoch 曝光而非 reweighting 本身；(2) 基于 quality floor + stability ceiling 的自适应 b* 框架；(3) 分析 detector 的校准与区分度要求。实验基于 Qwen3-0.6B，132M FineWeb tokens，40% 自生成污染，3 seeds。

### 2. Strengths
**S1.** Epoch-matched 对比设计严谨。Table 1 显示 D&R 的 PPL 优势从 0.384 缩小到 Δ=0.017，揭示了 prior work 中被忽视的混淆变量。
**S2.** 双约束框架概念清晰。Quality floor (α_eff ≥ τ) + stability ceiling (ESS ≥ n_min) 分解合理，Algorithm 1 简洁可复现。
**S3.** Detector 对比分析（Table 10, Appendix K）有实用价值——TF-IDF+LR 同时满足 calibration + discrimination，而 GPT-2 和 N-gram 各缺一个。
**S4.** Appendix 全面（Grid Search 全表、constraint regime 分解、rank preservation、cross-model transfer 等），可复现性好。
**S5.** α_eff 作为 real fraction proxy 验证充分（Table 9, Pearson r ≈ 0.70, bias ≈ −0.03）。

### 3. Weaknesses
**N1 [critical] 新颖性不足以支撑 main conference。**
- Epoch confound 是 ablation-level 发现，缺机制解释（为什么多 epoch 能替代 reweighting？）
- Adaptive b* 基于成熟统计工具（ESS, calibration）的 straightforward 组合，搜索 5 个离散 b 值
- Detector requirements（需要 calibration + discrimination）接近 expected
- 三个贡献叠加仍偏 incremental

**N2 [critical] 实验规模严重不足。**
- Qwen3-0.6B, batch size 4, 132M tokens
- 1.7B 实验仍然很小；Llama-3.2-3B cross-model transfer 结果 mixed/negative
- τ=0.7 是否 scale-invariant 无证据
- 在当前 LLM 研究中难以令人信服

**W1 [major] Epoch-matched 设计存在步数/LR confound。**
**W2 [major] Self-contamination 设置局限性未充分讨论。**
**W3 [major] Abstract/Introduction 中 overclaim。**
**W4 [minor] Related Work 遗漏 Mindermann et al. (2022) "Prioritized Training"。**
**W5 [minor] 术语不统一。**

### 4. Questions
Q1. Epoch confound 的机制是什么？多 epoch 曝光为什么能替代 reweighting？
Q2. Batch size 增大到 64/256 时框架行为如何变化？
Q3. Table 5 显示高污染下 hard filtering 仍优于 soft reweighting？
Q4. τ=0.7 对不同 ρ 是否稳定？
Q5. Llama cross-model transfer 失败是否说明需要 per-model tuning？

### 5. Overall Assessment
**Overall: 3.0 (Findings)** | Soundness 3.5 | Excitement 2.5 | Reproducibility 4 | Confidence 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-21T11:37:40.486004+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2\n\n### Strengths 回应\n\n[AGREE] R2-S1 (Epoch-matched 设计): 同意，也是我的 S1。但需注意 my W3 指出的 LR schedule confound。\n\n[AGREE] R2-S2 (框架清晰): 同意数学表述清晰，但 my W2 [critical] 指出 B=4 下 α_eff-binding 仅 ~0.2%（Figure 2），框架实质退化。\n\n[AGREE] R2-S3 (Detector 分析): 同意。Table 10 对从业者有参考价值。\n\n[AGREE] R2-S4 (Appendix 全面): 同意（my S3）。\n\n[AGREE] R2-S5 (α_eff proxy): 部分同意。r=0.70 只解释 ~49% 方差，不足以继承 Wang et al. 理论保证（my W8）。\n\n### Weaknesses 回应\n\n[AGREE] R2-N1 (新颖性不足): 基本同意，是我给 Excitement 2/5 的核心原因。Epoch confound 有纠偏价值但缺机制解释；adaptive b* 在 B=4 下等价于 5-value lookup table；三个贡献叠加仍 incremental。\n\n[AGREE] R2-N2 (规模不足): 强烈同意。1.7B OOD gains 消失（Δ→−0.008, §5.5），Appendix N Llama 实验省略 PPL 是 negative signal。标题暗示一般性结论但 evidence 仅来自 0.6B。\n\n[AGREE] R2-W1 (LR confound): 与 my W3 一致。但我升级为 critical（R2 标 major），因为 epoch confound 分析是论文最强贡献，其核心实验有 confound 动摇 foundation。\n\n[AGREE] R2-W2 (Self-contamination 局限): 与 my W5 一致。§8 有声明但不免除对 claim 可信度的影响。\n\n[AGREE] R2-W3 (Overclaim): 同意。Abstract \"consistent improvements\" 对 0.11% PPL 是 overclaim；§7 \"zero-tuning baseline that improves\" 技术正确但 framing misleading。\n\n[AGREE] R2-W4 (Missing Mindermann 2022): 同意。Prioritized Training 与 provenance-based reweighting 形成有意义对比。\n\n[AGREE] R2-W5 (术语不统一): Minor 级别合理。\n\n### Questions 回应\n\n[AGREE] R2-Q1: 关键问题。可能的机制是 multi-epoch 等效于反复看 clean data（implicit data augmentation），论文未探讨。\n\n[AGREE] R2-Q2: 与 my Q1 一致。验证 dual-constraint 是否 practically useful 的关键实验。\n\n[REBUT] R2-Q3: Table 5 的 D&R 数字是 ~2.4 epochs 的结果。Epoch-matched 后 D&R (17.657) vs. Adaptive (17.674) 差距仅 0.017，在 noise margin 内。R2 可能基于未 epoch-match 的原始数字。\n\n[AGREE] R2-Q4: Figure 3 / Table 6 部分回答，但 ρ=0.2 下方法完全失败（§5.5），核心问题是 detector quality 而非 τ 本身。\n\n[AGREE] R2-Q5: 如果需要 per-model tuning，\"zero-tuning baseline\" 定位站不住脚。\n\n### Overall Assessment 比较\n\nR2: 3.0 (Findings) vs. 我: 2.5 (Borderline Findings)。差异 0.5 分。\n\nR2 偏宽松的原因：(1) Soundness 3.5 偏高——LR confound 应为 critical（非 major），B=4 退化是 soundness 问题；(2) Excitement 2.5 与 R2 自己 N1/N2 的判断有内在张力。\n\n**我维持 2.5。** 建议 AC 关注：(1) 论文定位（analysis vs. method paper）；(2) 0.11% PPL 无下游效果是否足以支撑接收。",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2\n\n### Strengths 回应\n\n[AGREE] R2-S1 (Epoch-matched 设计): 同意，也是我的 S1。但需注意 my W3 指出的 LR schedule confound。\n\n[AGREE] R2-S2 (框架清晰): 同意数学表述清晰，但 my W2 [critical] 指出 B=4 下 α_eff-binding 仅 ~0.2%（Figure 2），框架实质退化。\n\n[AGREE] R2-S3 (Detector 分析): 同意。Table 10 对从业者有参考价值。\n\n[AGREE] R2-S4 (Appendix 全面): 同意（my S3）。\n\n[AGREE] R2-S5 (α_eff proxy): 部分同意。r=0.70 只解释 ~49% 方差，不足以继承 Wang et al. 理论保证（my W8）。\n\n### Weaknesses 回应\n\n[AGREE] R2-N1 (新颖性不足): 基本同意，是我给 Excitement 2/5 的核心原因。Epoch confound 有纠偏价值但缺机制解释；adaptive b* 在 B=4 下等价于 5-value lookup table；三个贡献叠加仍 incremental。\n\n[AGREE] R2-N2 (规模不足): 强烈同意。1.7B OOD gains 消失（Δ→−0.008, §5.5），Appendix N Llama 实验省略 PPL 是 negative signal。标题暗示一般性结论但 evidence 仅来自 0.6B。\n\n[AGREE] R2-W1 (LR confound): 与 my W3 一致。但我升级为 critical（R2 标 major），因为 epoch confound 分析是论文最强贡献，其核心实验有 confound 动摇 foundation。\n\n[AGREE] R2-W2 (Self-contamination 局限): 与 my W5 一致。§8 有声明但不免除对 claim 可信度的影响。\n\n[AGREE] R2-W3 (Overclaim): 同意。Abstract \"consistent improvements\" 对 0.11% PPL 是 overclaim；§7 \"zero-tuning baseline that improves\" 技术正确但 framing misleading。\n\n[AGREE] R2-W4 (Missing Mindermann 2022): 同意。Prioritized Training 与 provenance-based reweighting 形成有意义对比。\n\n[AGREE] R2-W5 (术语不统一): Minor 级别合理。\n\n### Questions 回应\n\n[AGREE] R2-Q1: 关键问题。可能的机制是 multi-epoch 等效于反复看 clean data（implicit data augmentation），论文未探讨。\n\n[AGREE] R2-Q2: 与 my Q1 一致。验证 dual-constraint 是否 practically useful 的关键实验。\n\n[REBUT] R2-Q3: Table 5 的 D&R 数字是 ~2.4 epochs 的结果。Epoch-matched 后 D&R (17.657) vs. Adaptive (17.674) 差距仅 0.017，在 noise margin 内。R2 可能基于未 epoch-match 的原始数字。\n\n[AGREE] R2-Q4: Figure 3 / Table 6 部分回答，但 ρ=0.2 下方法完全失败（§5.5），核心问题是 detector quality 而非 τ 本身。\n\n[AGREE] R2-Q5: 如果需要 per-model tuning，\"zero-tuning baseline\" 定位站不住脚。\n\n### Overall Assessment 比较\n\nR2: 3.0 (Findings) vs. 我: 2.5 (Borderline Findings)。差异 0.5 分。\n\nR2 偏宽松的原因：(1) Soundness 3.5 偏高——LR confound 应为 critical（非 major），B=4 退化是 soundness 问题；(2) Excitement 2.5 与 R2 自己 N1/N2 的判断有内在张力。\n\n**我维持 2.5。** 建议 AC 关注：(1) 论文定位（analysis vs. method paper）；(2) 0.11% PPL 无下游效果是否足以支撑接收。",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-21T11:37:44.200959+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-21T11:37:50.946333+00:00_

交叉回应已提交。

与 R2 在 11 条意见中达成 10 项 [AGREE]，仅在 R2-Q3（高污染下 hard filtering 是否优于 soft reweighting）上 [REBUT]——因为 R2 可能基于未 epoch-match 的数字，epoch-matched 后差距仅 0.017，在 noise margin 内。

核心分歧在最终评分：R2 给 3.0 (Findings)，我维持 2.5 (Borderline Findings)。主要原因是我将 LR confound 升级为 critical（epoch confound 分析是论文最强贡献，其核心实验有 confound 直接动摇 foundation），且认为 R2 的 Soundness 3.5 与 Excitement 2.5 偏高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

56 recorded events


### User

_source line 413 · 2026-05-21T14:02:54.833229+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。

## Venue 信息
- **目标**：EMNLP 2026 via ARR May 2026
- **截止日期**：2026-05-25
- **格式**：ACL 模板，正文 8 页限制（参考文献不限），double-blind
- **匿名规则**：严格 double-blind，禁止透露作者身份

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf`

## 审查侧重

### 1. 数学推导与理论基础
- Proposition 1 (α_eff 单调性) 和 Proposition 2 (ESS 单调性) 的证明是否严谨
- 双约束框架 (Eq. 4) 的三种 regime 划分是否完备且互斥
- α_eff 作为真实 real fraction 的代理指标，Pearson r≈0.70 是否足够支撑整个方法的理论动机
- b* 的 bisection 求解在 B=4 离散情况下的行为是否被充分讨论

### 2. 实验设计与对照
- 3 seeds (N=3) 的统计检验力是否足够支撑所有声称（尤其是 p=0.025 的结果）
- Epoch confound 分析：epoch-matched 对照是否完全消除了混淆因素（LR schedule 是否也是混淆？）
- Grid-b 作为 post-hoc oracle 的公平性讨论
- 自我污染设定（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）是否过度简化
- Detector 选择：只有 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram PPL），是否充分
- ρ=0.2 失败和 1.7B 效果减弱的分析是否充分

### 3. 统计严谨性
- 主要声称 Δ=-0.020 (p=0.025) 在 N=3 下的可信度
- 多重比较校正是否需要
- Effect size vs. practical significance：0.020 PPL 差异的实际意义
- 从 seed 42 到 from-scratch seeds 的 resume artifact 问题是否彻底解决

### 4. 可复现性
- 代码和数据承诺 upon acceptance，但当前是否提供足够细节
- 超参数设置是否完整
- 实验细节是否足够复现

请提供完整审稿报告，格式为：Summary → Strengths → Weaknesses → Questions → Minor Issues。Weaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-21T14:03:05.507652+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-21T14:03:05.558268+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-21T14:03:08.645221+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-21T14:03:09.540266+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-21T14:03:15.807041+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and related policies:

## Reviewer Guidelines

The recommended workflow is to read the paper and get a first impression, then search for relate
…[truncated 1294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7161
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-21T14:03:22.570230+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weig
…[truncated 333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 13029
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-21T14:03:27.424732+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
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

_source line 421 · 2026-05-21T14:03:27.476015+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-21T14:03:32.097831+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need every field a reviewer must fill out, including Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, etc. List the exact scale descriptions for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need every field a reviewer must fill out, including Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, etc. List the exact scale descriptions for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 423 · 2026-05-21T14:03:32.652143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 424 · 2026-05-21T14:03:33.505597+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-21T14:03:33.506088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-21T14:03:34.111308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-21T14:03:34.512914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-21T14:03:35.173096+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1667
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-21T14:03:35.173425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-21T14:03:36.132283+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2020
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-21T14:03:37.086628+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2573
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-21T14:03:37.741785+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2568
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-21T14:03:41.663705+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Review Fields

**1. Paper Summary**
Open-ended narrative describing the paper's topic and clarifying any misunderstandings.

**2. Summary of Strengths**
Open-ended explanation of reasons for publication, including methodology novelty, empirical results, or theoretical contributions.

**3. Summary of Weaknesses**
Numbered concerns about correctness, limited impact, clarity, or other publication barriers.

**4. Comments/Suggestions/Typos**
Open-ended improvement suggestions beyond main concerns.

## Quantitative Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- "5 = Positive that my evaluation is correct"
- 4 = Quite sure with unlikely missed details
- 3 = Pretty sure but possible gaps in review depth
- 2 = Willing to defend but likely missed some details
- "1 = Not my area, or paper is very hard to understand"

**Soundness** (1-5 with half-point increments)
- "5 = Excellent: This study is one of the most thorough"
- 4 = Strong with sufficient support
- 3 = Acceptable with minor gaps
- 2 = Poor with unsupported main claims
- "1 = Major Issues: not yet sufficiently thorough"

**Excitement** (1-5 with half-point increments)
- "5 = Highly Exciting: I would recommend this paper"
- 4 = Exciting; willing to mention to others
- 3 = Interesting; might mention selectively
- 2 = Potentially Interesting but lacking personal resonance
- 1 = Not Exciting; limited community relevance

**Overall Assessment** (1-5 scale with qualitative labels)
- 5 = Consider for Award (top 2.5%)
- 4.5 = Borderline Award
- 4 = Conference acceptance
- 3.5 = Borderline Conference
- 3 = Findings track acceptance
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

**Best Paper Justification**
Required only if overall assessment is "Consider for Award" or "Borderline Award."

## Additional Assessment Areas

**Reproducibility** (1-5 scale)
- "5 = They could easily reproduce
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9565
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-21T14:03:48.085991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 435 · 2026-05-21T14:03:48.641350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 436 · 2026-05-21T14:03:49.094718+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 437 · 2026-05-21T14:03:49.095144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 438 · 2026-05-21T14:03:49.553144+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-21T14:03:49.553788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-21T14:03:50.902950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-21T14:03:51.207805+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2112
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-21T14:03:51.815017+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
  "project": "provenance_weight_training",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf",
    "project": "provenance_weight_training",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-21T14:03:52.269873+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2716
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-21T14:03:53.553876+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2650
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-21T14:03:54.659588+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 378.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 391.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.7}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 150.9}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2844
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-21T14:04:00.983125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-21T14:04:01.536879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-21T14:04:02.092442+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-21T14:04:02.092864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-21T14:04:02.896618+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-21T14:04:02.898364+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-21T14:04:02.948934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-21T14:04:03.400981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 454 · 2026-05-21T14:04:03.653698+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-21T14:04:03.654132+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-21T14:04:04.409638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-21T14:04:04.460762+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-21T14:05:43.781028+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-21T14:05:45.588128+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines. I need: what reviewers should evaluate, how to assess soundness, what constitutes a good review, scoring guidance, and any specific instructions about statistical rigor, reproducibility, or experimental design evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines. I need: what reviewers should evaluate, how to assess soundness, what constitutes a good review, scoring guidance, and any specific instructions about statistical rigor, reproducibility, or experimental design evaluation."
  }
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-21T14:11:30.357953+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 52, \"total_citations\": 79, \"unique_cited_keys\": 52, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 37, \"online_not_found\": 8, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"katharopoulos2018not\", \"type\": \"inproceedings\", \"title\": \"Not All Samples Are Created Equal: Deep Learning with Importance Sampling\", \"authors\": \"\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"ren2018learning\", \"type\": \"inproceedings\", \"title\": \"Learning to Reweight Examples for Robust Deep Learning\", \"authors\": \"Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel\", \"year\": \"2018\", \"venue\": \"International Conference on Machine Learning\"}, {\"key\": \"chen2024bull\", \"type\": \"article\", \"title\": \"Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves LLM Generalization\", \"authors\": \"Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.14270\"}, {\"key\": \"kang2025demystifying\", \"type\": \"inproceedings\", \"title\": \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\", \"authors\": \"Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Ch...\", \"year\": \"2025\", \"venue\": \"EMNLP\"}, {\"key\": \"zibakhsh2025fortifai\", \"type\": \"article\", \"title\": \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\", \"authors\": \"Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koush...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.08972\"}, {\"key\": \"yi2025escaping\", \"type\": \"article\", \"title\
…[truncated 39116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 346576
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-21T14:11:40.845033+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Framework

Reviewers assess papers across three dimensions:

**Soundness**: Technical correctness and methodological rigor. "Soundness scores must be justified by the text of the review." Low scores require explicit justification; if you identify no major faults, reconsider your assessment.

**Excitement**: Personal interest level, orthogonal to soundness. Reflects subjective taste without requiring detailed reasoning.

**Overall Recommendation**: Composite judgment balancing soundness, novelty, and potential impact for venue placement (main conference vs. findings track).

## Key Evaluation Principles

**Read strategically**: First, skim to understand research questions and methodology *before* examining results. This prevents hindsight bias. Then conduct in-depth technical evaluation.

**Be specific**: Replace vague criticism ("not clear") with concrete observations ("Y and Z missing from X description"). Reference specific sections or line numbers where actionable.

**Distinguish weaknesses from limitations**: Papers acknowledging constraints shouldn't be penalized for those known limitations unless they fundamentally invalidate claims.

## Common Problematic Review Patterns

Reviewers should avoid:
- Dismissing findings as "obvious" or "not surprising" without evidence the community already knows them
- Rejecting work for lacking SOTA results when other contributions suffice
- Criticizing negative results when documenting what doesn't work serves the field
- Demanding extra experiments beyond what supports stated claims
- Penalizing methodological choices differing from reviewer preferences

## Reproducibility & Experimental Rigor

Assess whether papers provide:
- Sufficient implementation details for reproduction
- Clear hyperparameter selection methodology
- Data availability plans (public release, reviewer access, or justified withholding)
- Appropriate statistical significance reporting (confidence interv
…[truncated 1140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 355256
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-21T14:15:10.832499+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## 总体评分\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n**一句话总结**: 论文发现了有价值的 epoch confound 和 calibration 必要性，但核心自适应方法在 N=3 下统计支撑不足、无下游任务改善、且主文与 checklist 存在 p 值矛盾。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 理论框架合理，但核心实验声称受限于 N=3 统计功效不足、p 值自相矛盾、实际效应量微小（Δ=-0.020, 0.11%），且 epoch+LR 完全控制后 D&R 反而退化 |\n| Excitement | 3/5 | Epoch confound 发现对社区有实用价值，calibration 要求是可操作的 insight；但自适应方法本身效果微弱且缺乏下游验证 |\n| Reproducibility | 3.5/5 | 超参数、算法伪代码、训练配置较完整；代码承诺 upon acceptance 但未提供匿名仓库 |\n| Reviewer Confidence | 4/5 | 本人熟悉重要性采样、LM 预训练、数据质量方法 |\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight (D&R) 范式在含合成污染的 continued LM pretraining 中何时有效。使用 Qwen3-0.6B 在 132M FineWeb token（ρ=0.4 合成比例）上进行实验，3 个 seed，得出三个发现：(1) D&R 的 PPL 优势 >95% 归因于多 epoch 暴露（epoch confound），而非过滤质量；(2) 有效重加权同时需要检测器的高区分度（AUC）和良好校准（低 ECE）；(3) 提出双约束自适应框架（α_eff 质量下限 + ESS 稳定性上限）在最小干预下维持训练质量，声称 Δ=-0.020 PPL 改善（p=0.025）。\n\n---\n\n## 主要优势\n\n**S1. Epoch confound 发现具有独立贡献价值。** Table 1 (§5.1) 的 epoch-matched 对照实验表明 D&R full 的 PPL 优势从 Δ=-2.4 缩小到 Δ=+0.017（几乎消失），揭示了此前文献未充分讨论的混淆因素。这一发现对所有使用 D&R 的后续工作具有直接指导意义。\n\n**S2. Calibration 必要性是可操作的实践指导。** Table 10 (Appendix K) 展示了 TF-IDF+LR（AUC=0.94, ECE=0.048）有效而 N-gram PPL（AUC=0.939, better ECE=0.069）无法补偿 insufficient AUC (0.73) 的结果。\"区分度+校准缺一不可\"这一结论具有实用性。\n\n**S3. 理论框架设计合理。** 双约束公式化（Eq. 4）将 convergence guarantee（Wang et al., 2026）和 importance sampling stability（Kish, 1965）统一在同一框架内。Proposition 1（α_eff 单调性）和 Proposition 2（ESS 单调性）的证明思路清晰，利用协方差符号论证。\n\n**S4. 对自身局限性诚实处理。** 论文主动报告了 ρ=0.2 退化、1.7B 效果减弱、checkpoint resume artifact（Appendix O），并提供了 from-scratch seed 分析。这种透明度在实证研究中值得肯定。\n\n**S5. 附录分析全面。** 15 个附录覆盖 grid search、阈值敏感性、batch-adaptive 变体、constraint regime 分解、proxy 验证、cross-model transfer 等，展现了充分的实验探索。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 的统计功效根本不足以支撑核心声称\n- **具体位置**: §5.1, Abstract, §7\n- **问题**: \n  (a) 核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感——一个异常 seed 即可驱动整个结果。论文未报告所有比较的逐 seed PPL 值，无法判断改善是否跨 seed 一致。\n  (b) 以 df=2 获得 p=0.025（双尾），t 统计量需 ≈6.2，意味着三个 seed 的差异异常一致。对于随机性极高的 LM 训练过程，这种一致性本身就应引起怀疑而非增加信心。\n  (c) 论文测试了 6 种方法 × 2 个 ρ 值 × 3 个评估域 × 2 个模型大小，未做任何多重比较校正（Bonferroni、FDR 等）。在如此多的比较中，找到 p<0.05 的概率本身就很高。\n  (d) Appendix O 揭示 seed 42 使用了 checkpoint-resumed 训练，resume artifact 膨胀了表观效应。From-scratch seeds 的效果更弱。\n- **为什么影响接收**: 论文的第三个核心发现（自适应方法有效）完全依赖这一统计检验。如果 p 值不可靠，该发现无法成立。\n- **建议修改方向**: 增加到 ≥5 seeds（理想 10 seeds），报告逐 seed 结果及 bootstrap confidence intervals，对所有声称的比较做 FDR 校正。\n\n**N2** [critical] 实际显著性存疑：Δ=-0.020 PPL 无下游任务改善\n- **具体位置**: §5.1 (主要 PPL 声称), Table 7 (Appendix H, 下游基准)\n- **问题**:\n  (a) Δ=-0.020 在 base PPL ≈17.7 上仅为 0.11% 的相对改善，处于大多数实际应用的噪声范围内。\n  (b) Table 7 明确表明下游任务性能\"all differences within standard error (±0.01)\"，三 seed 均值完全相同（0.5414）。PPL 微小改善未转化为任何可测量的任务性能提升。\n  (c) 论文以 PPL 为主要指标却未充分论证为什么 0.020 的 PPL 差异具有实践价值。如果方法无法改善任何下游任务，其实际动机何在？\n- **为什么影响接收**: 方法论文的核心价值在于实用性。无下游改善意味着该方法的实际贡献有限。\n- **建议修改方向**: (1) 明确讨论 PPL vs 下游的 gap 及其对方法定位的影响；(2) 考虑在更大污染比例或更大模型上测试是否存在 PPL→下游的 transfer；(3) 或重新定位论文为分析性贡献而非方法贡献。\n\n**N3** [critical] 主文与 Checklist 的 p 值矛盾\n- **具体位置**: §5.1 报告 p=0.025；Responsible NLP Research Checklist §C3 报告 p=0.0425（同一比较：adaptive vs. uniform at ρ=0.4）\n- **问题**: 对于核心声称存在两个不同的 p 值。在一篇统计显著性已处于边缘的论文中，这一矛盾严重损害了对统计分析的信心。无论哪个值正确，另一处都是错误的——这意味着至少有一处计算或转录存在问题。\n- **为什么影响接收**: 如果真实 p=0.0425 而非 0.025，结论的可信度进一步下降。核心声称的 p 值不应自相矛盾。\n- **建议修改方向**: 核实并统一，报告准确的检验统计量（t 值、df、exact p）以及检验类型（单尾/双尾）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 自我污染设定是不切实际的简化检测场景\n- **具体位置**: §4 (Training Data), §7 (Limitations 简要提及)\n- **问题**: Qwen3-0.6B 生成 + Qwen3-0.6B 训练（§4）创造了最有利的检测环境——生成器和训练目标共享完全相同的架构和分词器。真实世界的 web 污染包含来自 GPT-4、Claude、Gemini、各种开源模型的异构合成文本，检测难度远高于此。\n  Table 11 (Appendix N) 的 cross-model transfer（Llama-3.2-3B 生成）仅为\"preliminary single-seed\"，且结果\"mixed\"——HellaSWag 轻微退化。这不足以支撑方法的通用性。\n- **建议**: 增加 ≥2 种跨模型污染实验（不同架构、不同规模的生成器）；或在 Limitations 中更显著地限定结论范围为 self-contamination。\n\n**W2** [warning] 完全控制混淆因素后 D&R 过滤本身有害\n- **具体位置**: §5.1, Table 1\n- **问题**: Table 1 显示 epoch-matched + LR-matched 对照下，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。这意味着过滤机制本身在剥离 multi-epoch 和 LR schedule 交互效应后是有害的。自适应方法的改善可能完全来自 LR schedule 交互作用，而非智能重加权。论文将此描述为\"warm LR from multi-epoch exposure\"但未直面其对方法核心动机的冲击——如果重加权机制本身不起正面作用，双约束框架的意义需要重新审视。\n- **建议**: 需要一个控制实验，在保持 LR schedule 一致的条件下（如相同步数、相同 LR schedule 但不同 b*）测试自适应方法是否仍有优势。\n\n**W3** [warning] 检测器覆盖面窄：仅 3 个检测器来自 2 个家族\n- **具体位置**: §5.2, Appendix K, Table 10\n- **问题**: 仅测试了 TF-IDF+LR（判别式）、GPT-2 PPL（生成式）、N-gram PPL（统计式）。缺少：fine-tuned 神经分类器（RoBERTa/DeBERTa-based）、DetectGPT/Fast-DetectGPT（论文在 Related Work 中引用但未评估）、watermark-based 方法、Binoculars 等。\"区分度+校准缺一不可\"的结论可能是检测器家族特异性的。\n- **建议**: 至少补充一个 fine-tuned 神经检测器的实验，以验证 calibration 发现的通用性。\n\n**W4** [warning] α_eff 作为真实人类比例代理：r=0.70 仅解释 49% 方差\n- **具体位置**: §3.2, Table 9 (Appendix J)\n- **问题**: Pearson r≈0.70 意味着 r²=0.49，超过一半的真实人类比例方差未被 α_eff 捕获。Table 9 还显示在 batch size=1 时 r=-0.16，需要 batch size ≥4 才达到 0.70。方法的理论动机——α_eff 追踪污染程度——仅获得中等程度的经验支撑。论文未讨论 51% 未解释方差的来源及其对方法可靠性的影响。\n- **建议**: 分析残差来源（是检测器噪声还是 α_eff 公式的系统偏差？），讨论对方法鲁棒性的影响。\n\n**W5** [warning] ρ=0.2 失败和 1.7B 效果减弱分析不充分\n- **具体位置**: §5.2 (boundary conditions), Appendix M (low contamination)\n- **问题**: \n  (a) ρ=0.2 退化 +0.040 PPL，归因于\"q-scores 模糊化\"，但未给出该污染水平下检测器的具体 AUC/ECE，也未测试不同 τ 是否能挽救。Appendix M 提供了些分析但仍是 seed 42 only。\n  (b) 1.7B 效果不显著（Δ=+0.013），论文解释为\"大模型对 0.6B 生成文本更鲁棒\"。但这也意味着方法在最需要的场景（大模型 at scale）可能无用。这两个边界条件的分析对方法的适用范围界定至关重要。\n- **建议**: (1) 报告 ρ=0.2 下检测器指标；(2) 测试 1.7B 模型受 1.7B 生成文本污染的场景；(3) 明确标定方法的适用条件。\n\n**W6** [warning] B=4 离散空间上的 bisection 与连续理论的脱节\n- **具体位置**: §3.3, Algorithm 1\n- **问题**: Micro-batch B=4 时，α_eff 实际只取 5 个离散值（§3.3 明确说明：\"α_eff takes only five discrete values {0, 0.25, 0.5, 0.75, 1.0}\"）。Bisection 算法是连续优化工具，但搜索空间实际上只有 5 个点。Propositions 1-2 的连续单调性保证与离散实现之间的 gap 未被讨论。\n- **建议**: (1) 讨论离散化对理论保证的影响；(2) 说明为何不直接枚举 5 个值而使用 bisection；(3) 考虑测试更大 batch size 下连续近似是否改善。\n\n---\n\n## 小问题（不影响接收）\n\n- **Figure 2 (p.8)**: 仅展示 seed 42 的 PPL 曲线。添加其他 seed 的曲线（或置信带）会更有说服力。\n- **Appendix O (Checkpoint Resume Artifact)**: 此发现对主文 seed 42 结果的解读有直接影响，建议在主文 §5.1 中简要提及而非仅放附录。\n- **Vehtari et al. 引用**: bib 标注 2024 年（JMLR 发表年），但该工作原始 arXiv 版本为 2015 年。建议注明。\n- **匿名仓库**: 论文承诺 code/data upon acceptance 但未提供匿名代码仓库，限制了审稿期间的复现性评估。\n- **Table 2 (p.7)**: Held-out perplexity 的 \"per-seed results rounded to three decimal places\" 对于 Δ=0.020 级别的效应量，3 位小数的 rounding 可能引入 artifacts——建议报告更多有效数字。\n\n---\n\n## Questions for Authors\n\n**Q1.** §5.1 报告 p=0.025，§C3 报告 p=0.0425，请澄清哪个值正确？请同时报告完整的检验信息（t 值、df、检验类型单尾/双尾）。\n\n**Q2.** 三个 from-scratch seeds 在 adaptive vs. uniform (ρ=0.4) 下各自的 PPL 值是多少？改善是三个 seed 一致的还是主要由某个 seed 驱动？\n\n**Q3.** Table 7 显示下游任务性能完全无差异（均值 0.5414）。在无下游改善的情况下，该方法的实际应用动机是什么？\n\n**Q4.** §5.1/Table 1: epoch-matched + LR-matched 对照下 D&R 劣于 uniform (Δ=+0.72)。如何调和这一发现与\"重加权机制独立于 epoch 效应有贡献\"的声称？\n\n**Q5.** 是否考虑过异构合成源（如混合 GPT-4 + Llama + Qwen 生成的文本）的实验，以测试 calibration 发现的通用性？\n\n**Q6.** α_eff 与真实人类比例仅 r=0.70。剩余 51% 方差中，有多少来自检测器噪声 vs. α_eff 公式的系统偏差？这对方法在不同检测器/数据分布下的可迁移性有何影响？\n",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## 总体评分\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n**一句话总结**: 论文发现了有价值的 epoch confound 和 calibration 必要性，但核心自适应方法在 N=3 下统计支撑不足、无下游任务改善、且主文与 checklist 存在 p 值矛盾。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 理论框架合理，但核心实验声称受限于 N=3 统计功效不足、p 值自相矛盾、实际效应量微小（Δ=-0.020, 0.11%），且 epoch+LR 完全控制后 D&R 反而退化 |\n| Excitement | 3/5 | Epoch confound 发现对社区有实用价值，calibration 要求是可操作的 insight；但自适应方法本身效果微弱且缺乏下游验证 |\n| Reproducibility | 3.5/5 | 超参数、算法伪代码、训练配置较完整；代码承诺 upon acceptance 但未提供匿名仓库 |\n| Reviewer Confidence | 4/5 | 本人熟悉重要性采样、LM 预训练、数据质量方法 |\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight (D&R) 范式在含合成污染的 continued LM pretraining 中何时有效。使用 Qwen3-0.6B 在 132M FineWeb token（ρ=0.4 合成比例）上进行实验，3 个 seed，得出三个发现：(1) D&R 的 PPL 优势 >95% 归因于多 epoch 暴露（epoch confound），而非过滤质量；(2) 有效重加权同时需要检测器的高区分度（AUC）和良好校准（低 ECE）；(3) 提出双约束自适应框架（α_eff 质量下限 + ESS 稳定性上限）在最小干预下维持训练质量，声称 Δ=-0.020 PPL 改善（p=0.025）。\n\n---\n\n## 主要优势\n\n**S1. Epoch confound 发现具有独立贡献价值。** Table 1 (§5.1) 的 epoch-matched 对照实验表明 D&R full 的 PPL 优势从 Δ=-2.4 缩小到 Δ=+0.017（几乎消失），揭示了此前文献未充分讨论的混淆因素。这一发现对所有使用 D&R 的后续工作具有直接指导意义。\n\n**S2. Calibration 必要性是可操作的实践指导。** Table 10 (Appendix K) 展示了 TF-IDF+LR（AUC=0.94, ECE=0.048）有效而 N-gram PPL（AUC=0.939, better ECE=0.069）无法补偿 insufficient AUC (0.73) 的结果。\"区分度+校准缺一不可\"这一结论具有实用性。\n\n**S3. 理论框架设计合理。** 双约束公式化（Eq. 4）将 convergence guarantee（Wang et al., 2026）和 importance sampling stability（Kish, 1965）统一在同一框架内。Proposition 1（α_eff 单调性）和 Proposition 2（ESS 单调性）的证明思路清晰，利用协方差符号论证。\n\n**S4. 对自身局限性诚实处理。** 论文主动报告了 ρ=0.2 退化、1.7B 效果减弱、checkpoint resume artifact（Appendix O），并提供了 from-scratch seed 分析。这种透明度在实证研究中值得肯定。\n\n**S5. 附录分析全面。** 15 个附录覆盖 grid search、阈值敏感性、batch-adaptive 变体、constraint regime 分解、proxy 验证、cross-model transfer 等，展现了充分的实验探索。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] N=3 seeds 的统计功效根本不足以支撑核心声称\n- **具体位置**: §5.1, Abstract, §7\n- **问题**: \n  (a) 核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感——一个异常 seed 即可驱动整个结果。论文未报告所有比较的逐 seed PPL 值，无法判断改善是否跨 seed 一致。\n  (b) 以 df=2 获得 p=0.025（双尾），t 统计量需 ≈6.2，意味着三个 seed 的差异异常一致。对于随机性极高的 LM 训练过程，这种一致性本身就应引起怀疑而非增加信心。\n  (c) 论文测试了 6 种方法 × 2 个 ρ 值 × 3 个评估域 × 2 个模型大小，未做任何多重比较校正（Bonferroni、FDR 等）。在如此多的比较中，找到 p<0.05 的概率本身就很高。\n  (d) Appendix O 揭示 seed 42 使用了 checkpoint-resumed 训练，resume artifact 膨胀了表观效应。From-scratch seeds 的效果更弱。\n- **为什么影响接收**: 论文的第三个核心发现（自适应方法有效）完全依赖这一统计检验。如果 p 值不可靠，该发现无法成立。\n- **建议修改方向**: 增加到 ≥5 seeds（理想 10 seeds），报告逐 seed 结果及 bootstrap confidence intervals，对所有声称的比较做 FDR 校正。\n\n**N2** [critical] 实际显著性存疑：Δ=-0.020 PPL 无下游任务改善\n- **具体位置**: §5.1 (主要 PPL 声称), Table 7 (Appendix H, 下游基准)\n- **问题**:\n  (a) Δ=-0.020 在 base PPL ≈17.7 上仅为 0.11% 的相对改善，处于大多数实际应用的噪声范围内。\n  (b) Table 7 明确表明下游任务性能\"all differences within standard error (±0.01)\"，三 seed 均值完全相同（0.5414）。PPL 微小改善未转化为任何可测量的任务性能提升。\n  (c) 论文以 PPL 为主要指标却未充分论证为什么 0.020 的 PPL 差异具有实践价值。如果方法无法改善任何下游任务，其实际动机何在？\n- **为什么影响接收**: 方法论文的核心价值在于实用性。无下游改善意味着该方法的实际贡献有限。\n- **建议修改方向**: (1) 明确讨论 PPL vs 下游的 gap 及其对方法定位的影响；(2) 考虑在更大污染比例或更大模型上测试是否存在 PPL→下游的 transfer；(3) 或重新定位论文为分析性贡献而非方法贡献。\n\n**N3** [critical] 主文与 Checklist 的 p 值矛盾\n- **具体位置**: §5.1 报告 p=0.025；Responsible NLP Research Checklist §C3 报告 p=0.0425（同一比较：adaptive vs. uniform at ρ=0.4）\n- **问题**: 对于核心声称存在两个不同的 p 值。在一篇统计显著性已处于边缘的论文中，这一矛盾严重损害了对统计分析的信心。无论哪个值正确，另一处都是错误的——这意味着至少有一处计算或转录存在问题。\n- **为什么影响接收**: 如果真实 p=0.0425 而非 0.025，结论的可信度进一步下降。核心声称的 p 值不应自相矛盾。\n- **建议修改方向**: 核实并统一，报告准确的检验统计量（t 值、df、exact p）以及检验类型（单尾/双尾）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 自我污染设定是不切实际的简化检测场景\n- **具体位置**: §4 (Training Data), §7 (Limitations 简要提及)\n- **问题**: Qwen3-0.6B 生成 + Qwen3-0.6B 训练（§4）创造了最有利的检测环境——生成器和训练目标共享完全相同的架构和分词器。真实世界的 web 污染包含来自 GPT-4、Claude、Gemini、各种开源模型的异构合成文本，检测难度远高于此。\n  Table 11 (Appendix N) 的 cross-model transfer（Llama-3.2-3B 生成）仅为\"preliminary single-seed\"，且结果\"mixed\"——HellaSWag 轻微退化。这不足以支撑方法的通用性。\n- **建议**: 增加 ≥2 种跨模型污染实验（不同架构、不同规模的生成器）；或在 Limitations 中更显著地限定结论范围为 self-contamination。\n\n**W2** [warning] 完全控制混淆因素后 D&R 过滤本身有害\n- **具体位置**: §5.1, Table 1\n- **问题**: Table 1 显示 epoch-matched + LR-matched 对照下，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。这意味着过滤机制本身在剥离 multi-epoch 和 LR schedule 交互效应后是有害的。自适应方法的改善可能完全来自 LR schedule 交互作用，而非智能重加权。论文将此描述为\"warm LR from multi-epoch exposure\"但未直面其对方法核心动机的冲击——如果重加权机制本身不起正面作用，双约束框架的意义需要重新审视。\n- **建议**: 需要一个控制实验，在保持 LR schedule 一致的条件下（如相同步数、相同 LR schedule 但不同 b*）测试自适应方法是否仍有优势。\n\n**W3** [warning] 检测器覆盖面窄：仅 3 个检测器来自 2 个家族\n- **具体位置**: §5.2, Appendix K, Table 10\n- **问题**: 仅测试了 TF-IDF+LR（判别式）、GPT-2 PPL（生成式）、N-gram PPL（统计式）。缺少：fine-tuned 神经分类器（RoBERTa/DeBERTa-based）、DetectGPT/Fast-DetectGPT（论文在 Related Work 中引用但未评估）、watermark-based 方法、Binoculars 等。\"区分度+校准缺一不可\"的结论可能是检测器家族特异性的。\n- **建议**: 至少补充一个 fine-tuned 神经检测器的实验，以验证 calibration 发现的通用性。\n\n**W4** [warning] α_eff 作为真实人类比例代理：r=0.70 仅解释 49% 方差\n- **具体位置**: §3.2, Table 9 (Appendix J)\n- **问题**: Pearson r≈0.70 意味着 r²=0.49，超过一半的真实人类比例方差未被 α_eff 捕获。Table 9 还显示在 batch size=1 时 r=-0.16，需要 batch size ≥4 才达到 0.70。方法的理论动机——α_eff 追踪污染程度——仅获得中等程度的经验支撑。论文未讨论 51% 未解释方差的来源及其对方法可靠性的影响。\n- **建议**: 分析残差来源（是检测器噪声还是 α_eff 公式的系统偏差？），讨论对方法鲁棒性的影响。\n\n**W5** [warning] ρ=0.2 失败和 1.7B 效果减弱分析不充分\n- **具体位置**: §5.2 (boundary conditions), Appendix M (low contamination)\n- **问题**: \n  (a) ρ=0.2 退化 +0.040 PPL，归因于\"q-scores 模糊化\"，但未给出该污染水平下检测器的具体 AUC/ECE，也未测试不同 τ 是否能挽救。Appendix M 提供了些分析但仍是 seed 42 only。\n  (b) 1.7B 效果不显著（Δ=+0.013），论文解释为\"大模型对 0.6B 生成文本更鲁棒\"。但这也意味着方法在最需要的场景（大模型 at scale）可能无用。这两个边界条件的分析对方法的适用范围界定至关重要。\n- **建议**: (1) 报告 ρ=0.2 下检测器指标；(2) 测试 1.7B 模型受 1.7B 生成文本污染的场景；(3) 明确标定方法的适用条件。\n\n**W6** [warning] B=4 离散空间上的 bisection 与连续理论的脱节\n- **具体位置**: §3.3, Algorithm 1\n- **问题**: Micro-batch B=4 时，α_eff 实际只取 5 个离散值（§3.3 明确说明：\"α_eff takes only five discrete values {0, 0.25, 0.5, 0.75, 1.0}\"）。Bisection 算法是连续优化工具，但搜索空间实际上只有 5 个点。Propositions 1-2 的连续单调性保证与离散实现之间的 gap 未被讨论。\n- **建议**: (1) 讨论离散化对理论保证的影响；(2) 说明为何不直接枚举 5 个值而使用 bisection；(3) 考虑测试更大 batch size 下连续近似是否改善。\n\n---\n\n## 小问题（不影响接收）\n\n- **Figure 2 (p.8)**: 仅展示 seed 42 的 PPL 曲线。添加其他 seed 的曲线（或置信带）会更有说服力。\n- **Appendix O (Checkpoint Resume Artifact)**: 此发现对主文 seed 42 结果的解读有直接影响，建议在主文 §5.1 中简要提及而非仅放附录。\n- **Vehtari et al. 引用**: bib 标注 2024 年（JMLR 发表年），但该工作原始 arXiv 版本为 2015 年。建议注明。\n- **匿名仓库**: 论文承诺 code/data upon acceptance 但未提供匿名代码仓库，限制了审稿期间的复现性评估。\n- **Table 2 (p.7)**: Held-out perplexity 的 \"per-seed results rounded to three decimal places\" 对于 Δ=0.020 级别的效应量，3 位小数的 rounding 可能引入 artifacts——建议报告更多有效数字。\n\n---\n\n## Questions for Authors\n\n**Q1.** §5.1 报告 p=0.025，§C3 报告 p=0.0425，请澄清哪个值正确？请同时报告完整的检验信息（t 值、df、检验类型单尾/双尾）。\n\n**Q2.** 三个 from-scratch seeds 在 adaptive vs. uniform (ρ=0.4) 下各自的 PPL 值是多少？改善是三个 seed 一致的还是主要由某个 seed 驱动？\n\n**Q3.** Table 7 显示下游任务性能完全无差异（均值 0.5414）。在无下游改善的情况下，该方法的实际应用动机是什么？\n\n**Q4.** §5.1/Table 1: epoch-matched + LR-matched 对照下 D&R 劣于 uniform (Δ=+0.72)。如何调和这一发现与\"重加权机制独立于 epoch 效应有贡献\"的声称？\n\n**Q5.** 是否考虑过异构合成源（如混合 GPT-4 + Llama + Qwen 生成的文本）的实验，以测试 calibration 发现的通用性？\n\n**Q6.** α_eff 与真实人类比例仅 r=0.70。剩余 51% 方差中，有多少来自检测器噪声 vs. α_eff 公式的系统偏差？这对方法在不同检测器/数据分布下的可迁移性有何影响？\n",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-21T14:15:14.604268+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3771
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-21T14:15:27.611945+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-21T14:15:27.712687+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-21T14:15:31.729167+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-21T14:15:31.729547+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 468 · 2026-05-21T14:15:39.869234+00:00_

审稿完成。核心判断：

- **Overall 3.0（Findings）**：epoch confound 和 calibration 必要性两个发现有独立价值，但自适应方法本身受限于 N=3 统计功效不足、p 值矛盾（主文 0.025 vs checklist 0.0425）、无下游改善（Table 7 均值完全相同）、以及完全控制混淆后 D&R 反而退化（Δ=+0.72）。
- **3 个 Must-Fix**：统计功效、实际显著性、p 值矛盾
- **6 个 Should-Fix**：自我污染过简、epoch+LR 控制后 D&R 有害、检测器覆盖窄、α_eff 代理质量中等、边界条件分析不足、离散空间与连续理论脱节

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 469 · 2026-05-21T14:15:57.256211+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

### 总体评分
**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）

**一句话总结**: 论文在实验控制上做得扎实（epoch confound 的发现有价值），但核心方法论贡献（adaptive b*）相对于 Drayson et al. (2025) 是增量式改进，效果规模小（Δ=-0.020 PPL），且适用范围受限（ρ=0.2 失败、1.7B 减弱），不足以支撑主会议接收。

### Must-Fix 问题

**N1** [critical] 相对于 Drayson et al. (2025) 的新颖性不足
- 论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b。核心区别仅在于 b 的选择方式——Drayson 用 validation-set grid search，本文用双约束自适应选择。但这本质上是一个超参数自动调节方案，而非方法论层面的根本创新。双约束中的 ESS 约束是重要性采样文献中的标准工具（Kish 1965, Owen 2013），α_eff 质量下限是直觉性阈值。将两个标准工具组合为一个自适应选择器，技术深度有限。

**N2** [critical] 效果规模极小，实用价值论证不足
- 核心效果数字是 Δ=−0.020 PPL（约 0.11%）。ρ=0.2 时方法失败（+0.040 退化），1.7B 时效果减弱，下游任务评估差异在标准误差范围内。如果 PPL 微小改进不转化为下游能力提升，整个 reweighting 工作的价值存疑。

**N3** [critical] Discussion 部分过于单薄（Section 6，约 11 行）
- 对于一篇声称揭示三项发现的分析型论文，Discussion 仅含两小段远远不够。

### Should-Fix 问题

**W1** [warning] 实验场景过窄——仅 self-contamination，单一数据域。Cross-model transfer (Appendix N) 仅单 seed 且 "mixed results"。

**W2** [warning] "Minimum intervention" 概念缺乏充分动机。未解释为什么过度降权有害。

**W3** [warning] Conclusion 过于简短（~8 行），缺乏前瞻性讨论。

**W4** [warning] 论文在 "分析论文" 与 "方法论文" 之间定位模糊，双重定位削弱了两个维度的说服力。

**W5** [warning] 下游任务评估不足——PPL 改进无法转化为下游任务改进，但该负面结果仅放在附录未在正文讨论。

### 格式合规性
全部通过：正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确。

---

请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-21T14:17:35.143403+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 相对于 Drayson et al. (2025) 的新颖性不足**\n\n同意核心判断。论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b（§3.1, Eq. 1），差异仅在于 b 的选取从 validation-set grid search 变为双约束自适应。ESS 约束确实是重要性采样文献的标准工具（Kish, 1965; Owen, 2013），α_eff 质量下限本质上是一个阈值化的加权比例统计量。将两个标准工具组合为一个 per-batch 选择器，技术深度有限。\n\n补充一点：论文的更大价值在于分析性发现（epoch confound 揭示、calibration 必要性），而非 adaptive b* 方法本身。但论文的叙事结构将 adaptive b* 作为三大发现之一并在 Abstract/Introduction 中突出（§1: \"a dual-constrained adaptive b* that eliminates per-model grid search\"），这一定位放大了 R2 指出的新颖性不足问题。如果论文重新定位为分析贡献为主、方法为辅，这一问题可以缓解。\n\n**[AGREE] R2-N2: 效果规模极小，实用价值论证不足**\n\n完全同意，且补充我自己的发现作为强化证据：\n(a) Table 7 (Appendix H) 下游任务 3-seed 均值完全相同（0.5414），所有差异在 ±0.01 标准误差范围内。PPL 微小改善（0.11%）不转化为任何可测量的能力提升。\n(b) 论文主文与 Checklist 存在 p 值矛盾——§5.1 报告 p=0.025，§C3 报告 p=0.0425（我在自己的审稿 N3 中指出）。即使取较小的 p 值，N=3 的统计功效也根本不足。\n(c) ρ=0.2 退化 +0.040（§5.2）和 1.7B 效果不显著 Δ=+0.013（§5.2）进一步限制了适用范围。方法在低污染和大模型两个最实际的场景都失效，严重削弱实用价值。\n\n**[AGREE] R2-N3: Discussion 部分过于单薄**\n\n同意。Section 6 仅包含两个小节（\"Why minimum intervention works\" 和 \"Practical guidance\"），合计约 15 行。对于一篇声称揭示三项发现的分析型论文，这远远不够。缺失的讨论包括：\n- Epoch confound 发现对现有 D&R 文献的系统性影响（哪些先前工作的结论需要重新审视？）\n- 方法适用边界的系统讨论（何时用 / 何时不用 / 何时该选择其他方案）\n- α_eff proxy 仅 r=0.70 的局限性及其对方法可靠性的影响（Table 9, Appendix J）\n- 与 domain-level mixing 方法（DoReMi, Aioli 等，§2 Related Work 中已引用）的概念对比\n\n不过我认为这是 should-fix 级别而非 must-fix，因为 Discussion 的厚度是写作问题，不影响技术正确性。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 实验场景过窄**\n\n同意，且与我自己的 W1 一致。Self-contamination（Qwen3-0.6B 生成 + Qwen3-0.6B 训练，§4）是最简单的检测场景。Appendix N (Table 11) 的 cross-model transfer 仅单 seed、混合结果（HellaSWag 退化），不足以支撑通用性声称。\n\n**[REBUT] R2-W2: \"Minimum intervention\" 概念缺乏充分动机**\n\n部分不同意。论文实际上提供了两层动机：\n\n(a) **理论层面**: §3.2 明确解释 ESS 稳定性约束防止梯度退化——\"Overly concentrated weights yield high-variance gradients; η_min prevents the batch from degenerating into a single effective sample.\" 这是重要性采样中 well-established 的 ESS 下界动机。\n\n(b) **经验层面**: Figure 2 (p.8) 展示了 b* 过大时 PPL 进入 \"degradation zone\"（b > ~1.5 时 PPL 开始快速上升）。§5.3 的超参数敏感性分析显示 τ=0.7 优于 τ=0.8（更激进的下权），且 τ > 0.8 导致 b* 快速增长（mean b* = 3.08 at τ=0.9）和 PPL 退化。§6 还通过 Random reweighting 对照（PPL 17,861）确认 detector signal 是 \"load-bearing\" 的，即仅有正确方向的适度干预才有效。\n\nR2 的合理之处在于：论文确实没有从信息论或优化理论角度给出 *为什么恰好最小干预是最优的* 的深层解释，现有动机更多是经验观察。但说\"未解释为什么过度降权有害\"并不准确——ESS 退化和 Figure 2 的 degradation zone 已经回答了这个问题。\n\n**[AGREE] R2-W3: Conclusion 过于简短**\n\n同意。§7 约 8-10 行，仅为三个发现的复述加 code/data 承诺，缺乏前瞻性讨论（如：对 recursive training 的长期影响、与 data provenance 标注标准化的关系、方法扩展到 instruction tuning 场景的可能性等）。不过这在严重程度上低于 Discussion 单薄（N3），属于写作层面的改善空间。\n\n**[AGREE] R2-W4: \"分析论文\" 与 \"方法论文\" 定位模糊**\n\n同意，且这是论文结构性问题的根源。具体证据：\n\n- **标题和研究问题（§1）** 框定为分析：\"When Does Detect-and-Reweight Work?\" → 期望是系统性分析\n- **Abstract 和 Contribution** 同时强调方法贡献：\"a dual-constrained adaptive b* that eliminates per-model grid search\" → 期望是方法创新\n- **实验评估** 以 PPL/下游比较为主（§5, Table 2），这是方法论文的评估模式\n\n双重定位的问题正如 R2 所说，两个维度都被削弱：\n- 作为分析论文：epoch confound 和 calibration 发现有价值，但正文空间被方法描述（§3 约 2.5 页）占据，分析深度不足（Discussion 仅 15 行）\n- 作为方法论文：效果仅 Δ=-0.020 PPL、无下游改善、适用范围受限\n\n建议作者明确选择分析性定位，将 adaptive b* 降格为分析发现的自然延伸而非独立贡献。\n\n**[AGREE] R2-W5: 下游任务评估不足**\n\n同意。Table 7 (Appendix H) 的负面结果——PPL 改善完全不转化为下游任务改善——是论文实用价值评估中最重要的数据之一，但仅放在附录中。主文 §5 和 §6 均未讨论这一结果。对于声称 \"practical adaptive method\" 的论文，将核心实用性的负面证据隐藏在附录中是一个叙事诚信问题。\n\n补充：即便 0.6B 模型可能因 benchmark saturation/floor effects 难以体现差异，论文也应在主文中讨论这一可能性并论证为什么 PPL 仍然是有意义的评估指标。\n\n---\n\n### 总结\n\n与 R2 的 8 条意见中，我对 7 条 [AGREE]（N1, N2, N3, W1, W3, W4, W5），对 1 条 [REBUT]（W2: minimum intervention 动机）。\n\n两位 Reviewer 的核心关切高度一致：N=3 统计功效不足、效果规模微小且无下游改善、适用范围受限。我与 R2 的主要分歧在于：R2 更强调新颖性不足（N1），而我更强调统计严谨性（N=3、p 值矛盾）。两个视角互补——即使方法足够新颖，统计支撑也不足；即使统计上 solid，新颖性也有限。\n\nOverall 评分我维持 **3.0 (Findings)**，与 R2 一致。Epoch confound 发现和 calibration 必要性是 Findings 级别的贡献；adaptive b* 方法在当前证据下不支持主会议接收。\n",
  "reviewer_id": "1",
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 相对于 Drayson et al. (2025) 的新颖性不足**\n\n同意核心判断。论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b（§3.1, Eq. 1），差异仅在于 b 的选取从 validation-set grid search 变为双约束自适应。ESS 约束确实是重要性采样文献的标准工具（Kish, 1965; Owen, 2013），α_eff 质量下限本质上是一个阈值化的加权比例统计量。将两个标准工具组合为一个 per-batch 选择器，技术深度有限。\n\n补充一点：论文的更大价值在于分析性发现（epoch confound 揭示、calibration 必要性），而非 adaptive b* 方法本身。但论文的叙事结构将 adaptive b* 作为三大发现之一并在 Abstract/Introduction 中突出（§1: \"a dual-constrained adaptive b* that eliminates per-model grid search\"），这一定位放大了 R2 指出的新颖性不足问题。如果论文重新定位为分析贡献为主、方法为辅，这一问题可以缓解。\n\n**[AGREE] R2-N2: 效果规模极小，实用价值论证不足**\n\n完全同意，且补充我自己的发现作为强化证据：\n(a) Table 7 (Appendix H) 下游任务 3-seed 均值完全相同（0.5414），所有差异在 ±0.01 标准误差范围内。PPL 微小改善（0.11%）不转化为任何可测量的能力提升。\n(b) 论文主文与 Checklist 存在 p 值矛盾——§5.1 报告 p=0.025，§C3 报告 p=0.0425（我在自己的审稿 N3 中指出）。即使取较小的 p 值，N=3 的统计功效也根本不足。\n(c) ρ=0.2 退化 +0.040（§5.2）和 1.7B 效果不显著 Δ=+0.013（§5.2）进一步限制了适用范围。方法在低污染和大模型两个最实际的场景都失效，严重削弱实用价值。\n\n**[AGREE] R2-N3: Discussion 部分过于单薄**\n\n同意。Section 6 仅包含两个小节（\"Why minimum intervention works\" 和 \"Practical guidance\"），合计约 15 行。对于一篇声称揭示三项发现的分析型论文，这远远不够。缺失的讨论包括：\n- Epoch confound 发现对现有 D&R 文献的系统性影响（哪些先前工作的结论需要重新审视？）\n- 方法适用边界的系统讨论（何时用 / 何时不用 / 何时该选择其他方案）\n- α_eff proxy 仅 r=0.70 的局限性及其对方法可靠性的影响（Table 9, Appendix J）\n- 与 domain-level mixing 方法（DoReMi, Aioli 等，§2 Related Work 中已引用）的概念对比\n\n不过我认为这是 should-fix 级别而非 must-fix，因为 Discussion 的厚度是写作问题，不影响技术正确性。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 实验场景过窄**\n\n同意，且与我自己的 W1 一致。Self-contamination（Qwen3-0.6B 生成 + Qwen3-0.6B 训练，§4）是最简单的检测场景。Appendix N (Table 11) 的 cross-model transfer 仅单 seed、混合结果（HellaSWag 退化），不足以支撑通用性声称。\n\n**[REBUT] R2-W2: \"Minimum intervention\" 概念缺乏充分动机**\n\n部分不同意。论文实际上提供了两层动机：\n\n(a) **理论层面**: §3.2 明确解释 ESS 稳定性约束防止梯度退化——\"Overly concentrated weights yield high-variance gradients; η_min prevents the batch from degenerating into a single effective sample.\" 这是重要性采样中 well-established 的 ESS 下界动机。\n\n(b) **经验层面**: Figure 2 (p.8) 展示了 b* 过大时 PPL 进入 \"degradation zone\"（b > ~1.5 时 PPL 开始快速上升）。§5.3 的超参数敏感性分析显示 τ=0.7 优于 τ=0.8（更激进的下权），且 τ > 0.8 导致 b* 快速增长（mean b* = 3.08 at τ=0.9）和 PPL 退化。§6 还通过 Random reweighting 对照（PPL 17,861）确认 detector signal 是 \"load-bearing\" 的，即仅有正确方向的适度干预才有效。\n\nR2 的合理之处在于：论文确实没有从信息论或优化理论角度给出 *为什么恰好最小干预是最优的* 的深层解释，现有动机更多是经验观察。但说\"未解释为什么过度降权有害\"并不准确——ESS 退化和 Figure 2 的 degradation zone 已经回答了这个问题。\n\n**[AGREE] R2-W3: Conclusion 过于简短**\n\n同意。§7 约 8-10 行，仅为三个发现的复述加 code/data 承诺，缺乏前瞻性讨论（如：对 recursive training 的长期影响、与 data provenance 标注标准化的关系、方法扩展到 instruction tuning 场景的可能性等）。不过这在严重程度上低于 Discussion 单薄（N3），属于写作层面的改善空间。\n\n**[AGREE] R2-W4: \"分析论文\" 与 \"方法论文\" 定位模糊**\n\n同意，且这是论文结构性问题的根源。具体证据：\n\n- **标题和研究问题（§1）** 框定为分析：\"When Does Detect-and-Reweight Work?\" → 期望是系统性分析\n- **Abstract 和 Contribution** 同时强调方法贡献：\"a dual-constrained adaptive b* that eliminates per-model grid search\" → 期望是方法创新\n- **实验评估** 以 PPL/下游比较为主（§5, Table 2），这是方法论文的评估模式\n\n双重定位的问题正如 R2 所说，两个维度都被削弱：\n- 作为分析论文：epoch confound 和 calibration 发现有价值，但正文空间被方法描述（§3 约 2.5 页）占据，分析深度不足（Discussion 仅 15 行）\n- 作为方法论文：效果仅 Δ=-0.020 PPL、无下游改善、适用范围受限\n\n建议作者明确选择分析性定位，将 adaptive b* 降格为分析发现的自然延伸而非独立贡献。\n\n**[AGREE] R2-W5: 下游任务评估不足**\n\n同意。Table 7 (Appendix H) 的负面结果——PPL 改善完全不转化为下游任务改善——是论文实用价值评估中最重要的数据之一，但仅放在附录中。主文 §5 和 §6 均未讨论这一结果。对于声称 \"practical adaptive method\" 的论文，将核心实用性的负面证据隐藏在附录中是一个叙事诚信问题。\n\n补充：即便 0.6B 模型可能因 benchmark saturation/floor effects 难以体现差异，论文也应在主文中讨论这一可能性并论证为什么 PPL 仍然是有意义的评估指标。\n\n---\n\n### 总结\n\n与 R2 的 8 条意见中，我对 7 条 [AGREE]（N1, N2, N3, W1, W3, W4, W5），对 1 条 [REBUT]（W2: minimum intervention 动机）。\n\n两位 Reviewer 的核心关切高度一致：N=3 统计功效不足、效果规模微小且无下游改善、适用范围受限。我与 R2 的主要分歧在于：R2 更强调新颖性不足（N1），而我更强调统计严谨性（N=3、p 值矛盾）。两个视角互补——即使方法足够新颖，统计支撑也不足；即使统计上 solid，新颖性也有限。\n\nOverall 评分我维持 **3.0 (Findings)**，与 R2 一致。Epoch confound 发现和 calibration 必要性是 Findings 级别的贡献；adaptive b* 方法在当前证据下不支持主会议接收。\n",
    "reviewer_id": "1",
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-21T14:17:38.704884+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3561
}
```

</details>

---


### Assistant

_source line 472 · 2026-05-21T14:17:44.215924+00:00_

交叉回应已提交。对 R2 的 8 条意见中 7 条 [AGREE]、1 条 [REBUT]（W2: minimum intervention 动机——论文通过 ESS 退化论证和 Figure 2 degradation zone 提供了合理解释）。两位 Reviewer 核心关切一致：N=3 统计功效不足、效果微小无下游改善、适用范围受限。Overall 维持 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

58 recorded events


### User

_source line 473 · 2026-05-22T16:54:58.681975+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性、实验设计和统计分析**。

## Venue 信息
- **目标**: EMNLP 2026 Long Paper (ARR)
- **Deadline**: 2026-05-25
- **格式**: ACL template, double-blind, 正文 ≤ 8 页, 参考文献无限制
- **匿名**: double-blind（无匿名期要求）
- **附录**: 允许但 reviewer 不必阅读；关键内容必须在正文
- **Limitations**: 必须有，不计入页数
- **Responsible NLP Checklist**: 应在 OpenReview 表单填写，不在论文 PDF 中

## 论文路径
- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`
- Sections: `projects/provenance_weight_training/docs/paper/sections/` 下各 .tex 文件
- PDF: `projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf`

## 你的审查侧重

### 1. 方法严谨性
- Dual-constraint framework (α_eff ≥ τ, ESS ≥ n_min) 的数学框架是否合理？Proposition 1-2 的证明是否正确？
- b* 的 bisection 求解是否有收敛保证？离散 B=4 下 α_eff 仅 5 个离散值，连续性声明是否站得住？
- α_eff 作为 true real fraction 的 proxy (r=0.70) 是否足够支撑方法的理论动机？
- Minimum intervention 原则的合理性——为什么最小 b 比最大 b 更好？是否有理论支持？

### 2. 实验设计
- 132M tokens, Qwen3-0.6B continued pretraining, 3 seeds——规模是否足以支撑 claims？
- Self-contamination 设定（generator = trainee）的生态效度
- Baselines 是否充分？缺少哪些重要 baseline？
- Epoch-matched comparison 的实验设计是否严密？LR schedule confound 是否完全排除？
- ρ=0.2 失败、1.7B 效果减弱——boundary conditions 的刻画是否充分？

### 3. 统计分析
- N=3 seeds, df=2: paired t-test 的可靠性？多重比较校正？
- seed 42 checkpoint resume artifact (Appendix O)——是否影响主表结果的可信度？
- Cross-seed variance 报告是否充分？bootstrap CI？
- 下游任务零改善——负面结果的讨论是否充分？

### 4. 格式合规
- 正文是否超过 8 页？
- 关键证据是否都在正文而非附录？

请按 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses (逐条，标注 severity: critical/major/minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-22T16:55:06.932139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-22T16:55:06.936034+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_reviewer_1_a7140515.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-22T16:55:08.894025+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-22T16:55:08.944643+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-22T16:55:10.702178+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-22T16:55:10.802939+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-22T16:55:16.380039+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-22T16:55:16.533130+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-22T16:55:20.600010+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 483 · 2026-05-22T16:55:22.556059+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
  "pages": "1-8",
  "project": "provenance_weight_training",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
    "pages": "1-8",
    "project": "provenance_weight_training",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-22T16:55:27.531226+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key ACL ARR reviewer guidelines and scoring criteria for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Area Chair Recommendations
The ARR metareview score options are: 5 = Consider for Award (top 2.5% papers); 2 = Resubmit next cycle; 1.5 = Resubmit after next cycle; 1 = Do not resubmit.

## Additional Requirements
All reviewers
…[truncated 385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6931
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-22T16:55:28.635289+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.1}], \"total_pages\": 16, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_
…[truncated 86 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6079
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-22T16:55:34.909140+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, review form dimensions, score scales (1-5), and what each score means for: soundness, excitement, overall assessment, confidence, reproducibility. Include any guidance on how to evaluate methodology, experiments, and statistical analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, review form dimensions, score scales (1-5), and what each score means for: soundness, excitement, overall assessment, confidence, reproducibility. Include any guidance on how to evaluate methodology, experiments, and statistical analysis."
  }
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-22T16:55:35.262051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-22T16:55:36.267063+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-22T16:55:36.367890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-22T16:55:36.770017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-22T16:55:37.425951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-22T16:55:37.426927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-22T16:55:37.583919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 813
}
```

</details>

---


### Tool result

_source line 494 · 2026-05-22T16:55:38.136517+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 709
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-22T16:55:40.745655+00:00_

# ARR Reviewer Scoring Criteria

## Primary Scoring Dimensions

Based on the guidelines, ARR reviewers provide **three main scores** (as of February 2025):

### 1. **Soundness**
The guidelines state that "The _soundness_ scores must be justified by the text of the review." Low soundness ratings require explicit justification identifying specific technical flaws. Reviewers must ensure scoring aligns with their review content.

### 2. **Excitement**
Described as a separate, subjective dimension capturing personal interest independent of methodological rigor. The guidelines clarify this is "orthogonal to the assessment of the soundness of the paper" and reflects individual taste rather than objective quality.

### 3. **Overall Assessment**
A composite recommendation score reflecting "soundness, excitement, and also other factors like novelty and impact." Papers recommended for publication must demonstrate sufficient soundness and reproducibility, though reviewers may endorse work lacking personal excitement if it offers significant impact to target communities.

## Additional Evaluation Dimensions

**Confidence**: Reviewers indicate confidence levels in their assessments, with guidance that lower confidence should be justified.

**Reproducibility**: Assessed separately, requiring justification for low scores. Reviewers evaluate whether sufficient implementation details, hyperparameters, code availability, and methodological transparency exist to enable replication.

## Scoring Guidance

The guidelines emphasize that scores must genuinely reflect review content—unexplained low scores on any dimension suggest unconscious bias rather than substantive critique. Reviewers should distinguish between technical soundness and subjective appeal when assigning scores.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5836
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-22T16:55:46.832925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-22T16:55:47.637021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-22T16:55:48.092745+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1259
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-22T16:55:48.093375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-22T16:55:48.898741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-22T16:55:48.949999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-22T16:55:50.056638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1963
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-22T16:55:50.057955+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-22T16:55:50.158696+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
  "pages": "9-16",
  "project": "provenance_weight_training",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf",
    "pages": "9-16",
    "project": "provenance_weight_training",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-22T16:55:51.067082+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.0}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 395.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 387.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 430.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 196.7}], \"total_pages\": 16, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/prov
…[truncated 100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-22T16:55:56.638675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-22T16:55:57.140678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-22T16:55:57.555041+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 916
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-22T16:55:57.555439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-22T16:55:58.229049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-22T16:55:58.288655+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1147
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-22T16:55:59.506462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1951
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-22T16:55:59.508903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1279
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-22T16:56:04.633159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-22T16:56:04.986066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-22T16:56:05.689844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-22T16:56:05.898194+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1265
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-22T16:56:05.950009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-22T16:56:07.464813+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2478
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-22T16:56:08.173471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2223
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-22T16:56:08.530598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2840
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-22T17:01:24.559008+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the exact scoring scales for ARR review form: soundness (1-5 scale description for each value), excitement (1-5), overall assessment, confidence, and any other required dimensions. What does each number mean?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the exact scoring scales for ARR review form: soundness (1-5 scale description for each value), excitement (1-5), overall assessment, confidence, and any other required dimensions. What does each number mean?"
  }
}
```

</details>

---

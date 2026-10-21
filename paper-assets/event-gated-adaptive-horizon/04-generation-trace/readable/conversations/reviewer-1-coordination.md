# Reviewer 1 coordination

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 471
- **Recorded user turns:** 14
- **Tool calls:** 222
- **Original source:** `logs/chats/feishu_group_oc_dd4a07a509df7e5f9a31d65f776059bc_reviewer_1.jsonl`
- **Structured JSON:** [`40195f1d416b75be1929.json`](../../sessions/40/40195f1d416b75be1929.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-15T12:29:34.795907+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 & 实验设计**

### 投稿信息
- **Venue**: CoRL 2026 Main Conference
- **Deadline**: 2026-05-29 (abstract: 2026-05-26)
- **格式要求**: 8页正文, PMLR模板 (`\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section
- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）

### 论文概述
标题："Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"

这是一篇诊断性论文，通过 factorial ablation 在 Walker Walk (DMC) 上分析为什么 dt-conditioning 在 DreamerV3 的 imagination-based actor-critic 中失败（尽管在 TAWM/TD-MPC2 的 MPC 框架中成功）。核心发现：trained dt-embedding 导致 RSSM reward head 产生 2.78× 的跨时间尺度预测偏差，critic 将其内化为过度估值（CIVO）。

### 你需要重点审查
1. **因果推断有效性**：factorial design 是否真的能支撑"trained dt-embedding is the causal factor"的强因果声明？有无混淆因素？
2. **统计检验力**：大多数配置仅 2-3 seeds。对于声称的"4/4 separating power"和"88.9% accuracy"，这个样本量是否足够支撑结论？是否需要置信区间或统计检验？
3. **NVE 阈值 1.5×**：该阈值是 empirically determined 还是 data-driven overfitting？是否 post-hoc 选择？
4. **单环境局限**：所有实验仅在 Walker Walk 上进行。因果声明能否推广？
5. **实验设计逻辑**：factorial grid 的设计是否有遗漏的关键对比组？例如 trained embedding + subsample OFF + H=8 是否测试过？
6. **105K 训练步数**：baseline 跑到 505K 而 treatment 只跑到 105K，这是否公平？

请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T12:29:41.895624+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T12:29:41.946263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T12:29:45.622490+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T12:29:45.823790+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/event-gated-adaptive-horizon/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/event-gated-adaptive-horizon/docs/paper/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T12:29:45.925939+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T12:29:53.249345+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"}]

Based on the search results, I found information about CoRL 2026, though specific detailed reviewer guidelines and review form criteria for CoRL 2026 were not fully available in the search results. However, I did find some relevant information:

## CoRL 2026 Reviewer Information

CoRL 2026 aims to have at least two reviewers per paper.

The search results included guidelines from CoRL 2023 which provide insight into the review criteria structure. The review criteria assess relevance by asking whether the paper addresses a problem in robot learning, applies or improves a learning-based method or learned model, evaluates the method in simulation, on real robots, or both, and whether the CoRL audience will be interested in reading the paper.

Additionally, CoRL papers are required to include a limitations section, with reviewers instructed to treat honestly reported limitations kindly and with high appre
…[truncated 739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7626
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T12:29:57.331119+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 \"instruction for reviews\" review form scoring criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 \"instruction for reviews\" review form scoring criteria"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T12:29:57.834742+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T12:29:59.199140+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 1364
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T12:29:59.409347+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/ -name \"*.tex\" 2>/dev/null | head -20",
  "description": "Find all .tex files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/ -name \"*.tex\" 2>/dev/null | head -20",
    "description": "Find all .tex files in paper directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T12:29:59.663995+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 254
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T12:30:09.178681+00:00_

Web search results for query: "CoRL 2024 "instruction for reviews" review form scoring criteria"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Instructions for Reviewers","url":"https://corl2022.org/instructions-for-reviewers/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"Instructions for Authors – Initial Submission","url":"https://corl2022.org/instructions-for-authors/"},{"title":"Frequently Asked Questions","url":"https://corl2022.org/frequently-asked-questions/"},{"title":"CoRL.2024 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/CoRL.2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"}]

I found the CoRL 2024 Instructions for Reviews page. Let me search for more specific information about the review form scoring criteria.

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"CORLcleared Vendor Scoring Process – CORL_Portal","url":"https://corl-portal.zendesk.com/hc/en-us/articles/14440881933339-C
…[truncated 3597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 11847
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T12:30:13.244280+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
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

_source line 15 · 2026-05-15T12:30:13.297135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T12:30:18.493445+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and numerical rating scales used for CoRL paper reviews. Include all rating categories (e.g., overall recommendation, confidence, soundness, novelty, clarity, etc.) with their full scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and numerical rating scales used for CoRL paper reviews. Include all rating categories (e.g., overall recommendation, confidence, soundness, novelty, clarity, etc.) with their full scale descriptions."
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T12:30:19.512659+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T12:30:19.820856+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 308
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T12:30:19.821335+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T12:30:20.123384+00:00_

1	\begin{abstract}
2	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify trained temporal embedding as the causal factor and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. A normalized value-to-eval ratio threshold of $1.5\times$ achieves 4/4 separating power within the factorial grid (88.9\% accuracy across all configurations, with one false negative under $\Delta t{=}1$-only imagination). The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T12:30:20.276593+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T12:30:20.279344+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T12:30:22.701648+00:00_

# CoRL 2024 Review Criteria - Summary

Based on the provided content, the document does **not** contain a complete review form with specific scoring dimensions or numerical rating scales.

## What is Actually Specified:

The document outlines only **general review criteria** for regular papers:

**Evaluation Focus:**
- "Significance and novelty of the results, either theoretical or empirical"
- Degree of objective establishment and potential for scientific/technological impact
- Relevance to robotic learning

**Scope Requirements:**
Papers must demonstrate robot learning relevance through either:
1. Intent: "Explicitly address a learning question for physical robots" OR
2. Outcome: "Test the proposed learning solution on physical robots"

## Missing Information:

The document does not provide:
- Numerical rating scales (e.g., 1-5, 1-10)
- Specific scoring dimensions (soundness, clarity, significance, etc.)
- Reviewer recommendation categories
- Confidence scales
- Detailed rubrics for each dimension

To access the complete review form with numerical ratings and detailed scoring categories, you would need to consult CoRL's actual review submission system or contact the organizing committee directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4208
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T12:30:27.598397+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, numerical rating scales, and all scoring categories with their descriptions. I need the full reviewer scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, numerical rating scales, and all scoring categories with their descriptions. I need the full reviewer scoring rubric."
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T12:30:28.106794+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T12:30:28.564391+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T12:30:28.615266+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T12:30:28.967300+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T12:30:28.967900+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T12:30:29.069115+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T12:30:33.203217+00:00_

# CoRL 2023 Review Criteria

Based on the provided guidelines, the review form evaluates submissions across six dimensions:

1. **Originality**: Novel problems/methods, combinations of existing techniques, clear differentiation from prior work, and adequate citations.

2. **Quality**: Technical soundness, well-supported claims through theory or experiments, appropriate methodology, completeness, and balanced author assessment of strengths/weaknesses.

3. **Clarity**: Clear writing, good organization, informative presentation, and sufficient detail "for an expert reader to reproduce its results."

4. **Significance**: Important results, likelihood of adoption by researchers/practitioners, advancement beyond prior approaches, and unique theoretical or experimental contributions.

5. **Relevance**: Addresses robot learning problems, applies learning-based methods, evaluation in simulation or real robots, and appeal to the CoRL audience.

6. **Limitations**: Papers must include limitations sections; "honestly reported limitations" should be treated respectfully, while unreported flaws should significantly impact scoring.

## Notable Absence

The provided document does not specify numerical rating scales or specific scoring categories (e.g., 1-5, 1-10 scales). It emphasizes qualitative evaluation principles rather than quantitative rubrics. The guidelines focus on evaluation dimensions and philosophical approaches to reviewing rather than detailed numerical scoring frameworks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5604
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T12:30:43.159195+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T12:30:43.765303+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T12:30:43.765698+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T12:30:44.373629+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T12:30:44.374345+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL OpenReview review form \"overall score\" rating scale 1-10 soundness significance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL OpenReview review form \"overall score\" rating scale 1-10 soundness significance"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T12:30:51.440631+00:00_

Web search results for query: "CoRL OpenReview review form "overall score" rating scale 1-10 soundness significance"

Links: [{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"Paper Ranking Methodology","url":"https://openreview-copilot.eamag.me/ranking"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Reviewer Guidelines","url":"https://neurips.cc/Conferences/2022/ReviewerGuidelines"},{"title":"Why are the \"rating\" and \"confidence\" fields in my PC Console wrong? | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions/why-are-the-rating-and-confidence-fields-in-my-pc-console-wrong"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"2023 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2023/ReviewerGuidelines"}]

Based on the search results, I found information about CoRL's review form. The CoRL review form asks for an evaluation of originality, quality, clarity, significance, relevance and limitations of the work. However, the search results don't contain specific details about the exact rating scale (1-10) for the "overall score" field or how soundness and significance are specifically scaled.

The search results show that CoRL's review form includes an evaluation of quality, asking "Is the submission technically sound?", and the guidelines mention significance as one of the evaluation criteria, but the exact numerical rating scale and definitions for these scores are 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7066
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T12:30:56.271151+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
  "prompt": "Extract the complete default review form including all rating dimensions, their numerical scales, and the description of each score level (e.g., what does 1 mean, what does 10 mean for overall score). I need the full rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
    "prompt": "Extract the complete default review form including all rating dimensions, their numerical scales, and the description of each score level (e.g., what does 1 mean, what does 10 mean for overall score). I need the full rubric."
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T12:30:59.952256+00:00_

# Default Review Form - Complete Rubric

The OpenReview default review form contains four dimensions:

## 1. **Title**
A brief summary (max 500 characters) of the review's focus.

## 2. **Review**
Detailed evaluation up to 20,000 characters covering "quality, clarity, originality and significance" with pros/cons listed. Supports Markdown and LaTeX formatting.

## 3. **Rating Scale** (10-point)
- **10:** "Top 5% of accepted papers, seminal paper"
- **9:** "Top 15% of accepted papers, strong accept"
- **8:** "Top 50% of accepted papers, clear accept"
- **7:** "Good paper, accept"
- **6:** "Marginally above acceptance threshold"
- **5:** "Marginally below acceptance threshold"
- **4:** "Ok but not good enough - rejection"
- **3:** "Clear rejection"
- **2:** "Strong rejection"
- **1:** "Trivial or wrong"

## 4. **Confidence Scale** (5-level)
- **5:** Absolutely certain; very familiar with relevant literature
- **4:** Confident but not absolutely certain about correctness
- **3:** Fairly confident in the evaluation
- **2:** Willing to defend, but may have missed central paper content
- **1:** Educated guess only

Both API V2 and V1 JSON formats are available for implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3681
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T12:31:09.527059+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/ -name \"*.bib\" 2>/dev/null",
  "description": "Find bibliography files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/ -name \"*.bib\" 2>/dev/null",
    "description": "Find bibliography files"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T12:31:09.627751+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T12:31:12.109114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T12:31:12.160435+00:00_

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
…[truncated 22609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T12:34:03.077122+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**审查侧重**: 方法严谨性 & 实验设计\n\n---\n\n## 总体评分\n\n**Overall**: 4/10 (Ok but not good enough — rejection)\n**Confidence**: 4/5 (Confident but not absolutely certain)\n\n**一句话总结**: 有趣的诊断视角和清晰的 CIVO 机制描述，但 2-3 seeds 的统计基础无法支撑论文的强因果声明，单环境局限严重削弱泛化性，且对 CoRL 的 robotics relevance 不足。\n\n---\n\n## 官方维度打分（基于 CoRL review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | CIVO 机制是新的观察，但本质是\"model error + bootstrapping = value overestimation\"的已知问题在新 setting 下的实例化 |\n| Quality | 2/5 | Factorial design 结构良好但统计检验力极弱（2-3 seeds），NVE 阈值 post-hoc，因果声明过强 |\n| Clarity | 4/5 | 写作清晰，结构良好，Figure/Table 信息量充足 |\n| Significance | 2/5 | 单环境 + 单架构的 negative result，对社区的指导价值有限 |\n| Relevance | 1/5 | 无任何机器人实验或机器人问题讨论，DMC Walker Walk 不满足 CoRL 对 robot learning relevance 的要求 |\n| Limitations | 4/5 | 诚实地报告了单环境和单架构的局限，但未充分讨论统计检验力不足的问题 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 统计检验力严重不足，无法支撑因果声明\n\n- 具体位置：Section 4.3 (\"2--3 seeds\"), Section 5.2 (\"4/4 separating power\"), Abstract (\"88.9% accuracy\")\n- 问题：核心因果声明\"trained dt-embedding is the causal factor\"依赖于 factorial grid 内 2 trained seeds vs 2 untrained seeds 的比较。\"4/4 separating power\"即 n=2 per group 的完美分离——即使在随机零假设下（每个 seed 独立 50% 概率超阈值），P(4/4) = 1/16 ≈ 6.25%，这离统计显著性（p<0.05 需考虑多重比较修正）甚远。更重要的是，deep RL 中 2-3 seeds 的高方差已被 Henderson et al. (2018) 和 Colas et al. (2018)（后者在论文 bib 中但未被正文引用）反复证明不足以得出可靠结论。论文引用 Agarwal et al. (2021) 来辩护报告 per-seed trajectories，但该文的核心论点恰恰是需要 **更多** seeds 并使用 IQM 等稳健统计量，而非在更少 seeds 上报告个体轨迹。\n- 为什么影响接收：一篇诊断性论文的核心价值在于其结论的可靠性。当样本量无法排除随机效应时，\"causal factor\" 这一强声明不成立。\n- 建议修改方向：(1) 至少增加到 5-10 seeds per configuration；(2) 使用 bootstrap CI 或 permutation test 报告置信区间；(3) 将语言从\"causal factor\"弱化为\"associated factor\"或\"candidate mechanism\"。\n\n**N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择，\"88.9% accuracy\"是训练准确率\n\n- 具体位置：Section 4.4 (Eq. 1), Section 5.2, Abstract\n- 问题：NVE > 1.5× 阈值在论文中未说明选择依据。查看数据分布：trained seeds 的 NVE 值为 {4.12, 2.05, 4.12, 1.57, 3.78}，untrained/none seeds 为 {0.30, 1.14, 0.59, 0.58, 0.80}。两组之间有明显间隙，[1.2, 2.0] 范围内任何阈值都能达到类似分类效果。这强烈暗示阈值是在观察数据后选定的。在此基础上报告的 \"88.9% accuracy\" 是在训练集上的准确率，没有任何 held-out 验证或 cross-validation，因此不具有泛化意义。\n- 为什么影响接收：将 post-hoc 选择的指标阈值包装为具有诊断价值的 \"separating power\" 是方法论上的严重问题，可能误导后续研究者将其作为通用诊断工具使用。\n- 建议修改方向：(1) 明确说明阈值选择过程（是 pre-registered 还是 data-driven）；(2) 在独立环境/配置上验证该阈值；(3) 或去除定量声明，改为定性描述\"trained embedding 配置的 NVE 系统性高于 untrained 配置\"。\n\n**N3** [critical] CoRL Relevance 严重不足\n\n- 具体位置：全文；Section 4.5 (Environment: Walker Walk DMC, proprioceptive)\n- 问题：CoRL 明确要求论文\"explicitly address a learning question for physical robots\"或\"test the proposed learning solution on physical robots\"。本文仅在 DMC Walker Walk（一个 low-dimensional locomotion simulation）上用 proprioceptive observations 做实验。全文未讨论任何 robotics application，未测试任何 robotics benchmark（如 RoboSuite, ManiSkill, IsaacGym），未讨论 CIVO 对 real-robot deployment 的影响。DreamerV3 虽然可用于 robotics，但本文的分析完全局限在 control suite simulation 层面。\n- 为什么影响接收：这是 CoRL 的基本投稿要求，不满足 relevance 门槛可能导致 desk reject。\n- 建议修改方向：(1) 至少在一个 robotics-relevant benchmark 上复现核心发现；(2) 增加 Discussion section 讨论 CIVO 对 real-world robot learning 的具体影响（如 sim-to-real transfer 中的 temporal abstraction）。\n\n**N4** [critical] 单环境局限使因果声明不可泛化\n\n- 具体位置：Section 4.5, Conclusion (Limitations paragraph)\n- 问题：所有实验仅在 Walker Walk 上进行。这是 DMC 中最简单的连续控制任务之一（24-dim observation, 6-dim action）。CIVO 的发生可能高度依赖于：(a) 动力学的低维度和可预测性——更复杂任务中 RSSM 的 reward gap 模式可能不同；(b) reward 的密度和 scale——sparse reward 任务中 value overestimation 的表现可能不同；(c) observation modality——visual observations 会引入额外的 representation bottleneck。在一个环境上做的诊断无法支撑 Section 6 中关于\"structural incompatibility between flat temporal conditioning and imagination-based actor-critic training\"的泛化性声明。\n- 为什么影响接收：诊断性论文的价值取决于发现的普遍性。单环境发现可能只是 task-specific artifact。\n- 建议修改方向：至少增加 2-3 个不同复杂度的 DMC 任务（如 Cheetah Run, Quadruped Walk, Humanoid Walk），验证 CIVO 在不同动力学复杂度下是否稳定出现。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Factorial design 存在混淆变量\n\n- 具体位置：Table 1 (Section 4.3)\n- 问题：Factorial grid 的关键比较存在混淆。核心的 \"trained vs untrained\" 比较：008d (trained + Sub ON + H=8) vs 008a (untrained + Sub OFF + H=15)——这同时改变了三个因素（embedding type, subsampling, horizon）。唯一干净的比较是 008d vs 008f，但 008f 是 embedding **完全移除**（none），而非 untrained。因此实际上没有一组配置同时保持 subsampling 和 horizon 不变，仅改变 trained → untrained embedding。论文声称 008a/008c 是 untrained 控制组，但它们与 008d 在 subsampling 上不同（OFF vs ON），引入了混淆。\n- 建议：补充 untrained + Sub ON + H=8 + dt=2 配置，形成与 008d 的干净对比。\n\n**W2** [warning] 105K vs 505K 训练步数不对等\n\n- 具体位置：Section 4.5 (\"Treatment configurations run for 105K steps\")\n- 问题：Baseline 运行到 505K 展示了完整的收敛行为（peak 970.4），但所有 treatment 仅运行到 105K。对于一篇诊断 \"collapse\" 动态的论文，这创造了不对称的观察窗口：(a) Self-correcting seed 009b（267.9 @105K）可能在更长训练后恢复；(b) \"healthy\" 的 untrained configs 可能在后期发展出其他 pathology；(c) Oscillatory pattern (009e) 的长期命运未知。论文在 Section 4.5 辩护说 \"105K is sufficient to observe both collapse onset and diagnostic markers\"，但这是循环论证——你不知道 105K 之后会发生什么，因为你没观察。\n- 建议：至少将关键配置（008d 三个 seeds + 008f + 008e_v3 两个 seeds）延长到 300-500K，与 baseline 对等。\n\n**W3** [warning] 对 Pathway B 的解释不充分\n\n- 具体位置：Section 5.6, Section 6.5\n- 问题：008e_v3 seed 2 的 non-CIVO collapse (Pathway B) 是论文最有趣的发现之一，但解释极其薄弱。论文仅描述了现象（entropy 增加、eval 下降、value 稳定），然后含糊地归因于 \"representation space\" 影响。没有提供任何机制性解释：trained embedding 如何在 dt=1 imagination 下导致 actor destabilization？为什么 entropy 增加而非减少？这个 Pathway B 是否可能只是普通的 training instability，与 dt-embedding 无关？Baseline seed 2 (009a) 的稳定性不能排除这一可能，因为增加任何额外 module（包括 subsampling data augmentation）都可能引入 instability。\n- 建议：(1) 提供 Pathway B 的具体机制假说并设计实验验证；(2) 或诚实地承认 Pathway B 的 causation 未建立，仅为观察。\n\n**W4** [warning] RSSM fidelity analysis 的解释可能有误\n\n- 具体位置：Table 4 (Section 5.6), Section 6.1\n- 问题：Table 4 中 008d (trained embedding) 的 reward MAE at dt=1 是 0.0568，at dt=2 是 0.1579（gap 2.78×）。论文将此解释为 \"reward head systematically overpredicts rewards at dt=2\"。但 MAE 只衡量误差大小，不区分 over- 和 under-prediction。高 MAE 可能是正向偏差、负向偏差、或高方差的结果。论文需要证明偏差方向是系统性正向的（即 reward over-prediction 而非 under-prediction），才能支撑 CIVO 的 \"overestimation\" 机制。\n- 建议：报告 reward prediction bias（signed error）而非仅 MAE，以验证方向性假设。\n\n**W5** [warning] 格式不符合 CoRL 2026 要求\n\n- 具体位置：main.tex line 1\n- 问题：论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}`，而 CoRL 2026 要求 PMLR 模板（`\\usepackage[final]{corl_2026}`）。当前格式虽然视觉上接近双栏，但不符合官方提交要求，可能导致 desk reject。\n- 建议：切换到 CoRL 2026 官方 PMLR 模板。\n\n---\n\n## 小问题（不影响接收）\n\n- **bib 质量问题**：`splates2025` 条目 author 为 \"SPlaTES, authors\"（占位符），`nie2025sdar` 和多个条目使用 \"et, al\" 代替完整作者列表——BibTeX 中 \"et al.\" 应写完整作者或正确截断。\n- **hafner2023dreamerv3** 标注 year=2025 (Nature 发表年) 但 cite key 用 2023——可能造成混淆。\n- **Missing citation**: `colas2018seeds` 在 bib 中存在但正文未引用，该文恰恰是关于 seed 数量对 deep RL 结论可靠性影响的直接相关工作，应当引用并讨论。\n- Abstract 中 \"88.9% accuracy\" 放在如此显眼位置有误导性（如 N2 所述）。\n- Section 6.4 对 \"dt-embedding dilemma\" 的讨论倾向于将 negative result 包装为 fundamental insight，但在单环境 + 低 seed 数下，这个 \"dilemma\" 可能只是实验设计的 artifact。\n\n---\n\n## 主要优势\n\n- **清晰的问题定义**：将 \"为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败\" 作为核心问题，切入点明确且有实际意义。\n- **结构化的实验设计**：Factorial ablation 的框架设计本身是好的方法论选择，配置间的对比逻辑清晰。\n- **机制描述细致**：CIVO 的四阶段反馈回路（Section 6.1）描述得清楚且有说服力，三种 post-CIVO 结果的刻画也很有信息量。\n- **诚实的 Limitations**：论文承认了单环境和单架构的局限，且 Finding F6 的 partial falsification 展示了良好的科学态度。\n- **写作质量高**：论文组织良好，Figure/Table 信息密度高，notation 一致。\n\n---\n\n## 总结判断\n\n本文提出了一个有趣的诊断视角（CIVO），但在当前形态下存在多个根本性问题：(1) 2-3 seeds 的统计基础无法支撑强因果声明；(2) NVE 阈值为 post-hoc 选择且无独立验证；(3) 单环境实验严重限制泛化性；(4) 对 CoRL 的 robotics relevance 要求未满足。建议作者大幅增加实验规模（更多 seeds、更多环境），弱化因果语言，并在修改后投稿到更 general 的 RL venue（如 ICML/NeurIPS 的 workshop 或 RLC）。\n\n**建议决定**: Reject (4/10)",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**审查侧重**: 方法严谨性 & 实验设计\n\n---\n\n## 总体评分\n\n**Overall**: 4/10 (Ok but not good enough — rejection)\n**Confidence**: 4/5 (Confident but not absolutely certain)\n\n**一句话总结**: 有趣的诊断视角和清晰的 CIVO 机制描述，但 2-3 seeds 的统计基础无法支撑论文的强因果声明，单环境局限严重削弱泛化性，且对 CoRL 的 robotics relevance 不足。\n\n---\n\n## 官方维度打分（基于 CoRL review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | CIVO 机制是新的观察，但本质是\"model error + bootstrapping = value overestimation\"的已知问题在新 setting 下的实例化 |\n| Quality | 2/5 | Factorial design 结构良好但统计检验力极弱（2-3 seeds），NVE 阈值 post-hoc，因果声明过强 |\n| Clarity | 4/5 | 写作清晰，结构良好，Figure/Table 信息量充足 |\n| Significance | 2/5 | 单环境 + 单架构的 negative result，对社区的指导价值有限 |\n| Relevance | 1/5 | 无任何机器人实验或机器人问题讨论，DMC Walker Walk 不满足 CoRL 对 robot learning relevance 的要求 |\n| Limitations | 4/5 | 诚实地报告了单环境和单架构的局限，但未充分讨论统计检验力不足的问题 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 统计检验力严重不足，无法支撑因果声明\n\n- 具体位置：Section 4.3 (\"2--3 seeds\"), Section 5.2 (\"4/4 separating power\"), Abstract (\"88.9% accuracy\")\n- 问题：核心因果声明\"trained dt-embedding is the causal factor\"依赖于 factorial grid 内 2 trained seeds vs 2 untrained seeds 的比较。\"4/4 separating power\"即 n=2 per group 的完美分离——即使在随机零假设下（每个 seed 独立 50% 概率超阈值），P(4/4) = 1/16 ≈ 6.25%，这离统计显著性（p<0.05 需考虑多重比较修正）甚远。更重要的是，deep RL 中 2-3 seeds 的高方差已被 Henderson et al. (2018) 和 Colas et al. (2018)（后者在论文 bib 中但未被正文引用）反复证明不足以得出可靠结论。论文引用 Agarwal et al. (2021) 来辩护报告 per-seed trajectories，但该文的核心论点恰恰是需要 **更多** seeds 并使用 IQM 等稳健统计量，而非在更少 seeds 上报告个体轨迹。\n- 为什么影响接收：一篇诊断性论文的核心价值在于其结论的可靠性。当样本量无法排除随机效应时，\"causal factor\" 这一强声明不成立。\n- 建议修改方向：(1) 至少增加到 5-10 seeds per configuration；(2) 使用 bootstrap CI 或 permutation test 报告置信区间；(3) 将语言从\"causal factor\"弱化为\"associated factor\"或\"candidate mechanism\"。\n\n**N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择，\"88.9% accuracy\"是训练准确率\n\n- 具体位置：Section 4.4 (Eq. 1), Section 5.2, Abstract\n- 问题：NVE > 1.5× 阈值在论文中未说明选择依据。查看数据分布：trained seeds 的 NVE 值为 {4.12, 2.05, 4.12, 1.57, 3.78}，untrained/none seeds 为 {0.30, 1.14, 0.59, 0.58, 0.80}。两组之间有明显间隙，[1.2, 2.0] 范围内任何阈值都能达到类似分类效果。这强烈暗示阈值是在观察数据后选定的。在此基础上报告的 \"88.9% accuracy\" 是在训练集上的准确率，没有任何 held-out 验证或 cross-validation，因此不具有泛化意义。\n- 为什么影响接收：将 post-hoc 选择的指标阈值包装为具有诊断价值的 \"separating power\" 是方法论上的严重问题，可能误导后续研究者将其作为通用诊断工具使用。\n- 建议修改方向：(1) 明确说明阈值选择过程（是 pre-registered 还是 data-driven）；(2) 在独立环境/配置上验证该阈值；(3) 或去除定量声明，改为定性描述\"trained embedding 配置的 NVE 系统性高于 untrained 配置\"。\n\n**N3** [critical] CoRL Relevance 严重不足\n\n- 具体位置：全文；Section 4.5 (Environment: Walker Walk DMC, proprioceptive)\n- 问题：CoRL 明确要求论文\"explicitly address a learning question for physical robots\"或\"test the proposed learning solution on physical robots\"。本文仅在 DMC Walker Walk（一个 low-dimensional locomotion simulation）上用 proprioceptive observations 做实验。全文未讨论任何 robotics application，未测试任何 robotics benchmark（如 RoboSuite, ManiSkill, IsaacGym），未讨论 CIVO 对 real-robot deployment 的影响。DreamerV3 虽然可用于 robotics，但本文的分析完全局限在 control suite simulation 层面。\n- 为什么影响接收：这是 CoRL 的基本投稿要求，不满足 relevance 门槛可能导致 desk reject。\n- 建议修改方向：(1) 至少在一个 robotics-relevant benchmark 上复现核心发现；(2) 增加 Discussion section 讨论 CIVO 对 real-world robot learning 的具体影响（如 sim-to-real transfer 中的 temporal abstraction）。\n\n**N4** [critical] 单环境局限使因果声明不可泛化\n\n- 具体位置：Section 4.5, Conclusion (Limitations paragraph)\n- 问题：所有实验仅在 Walker Walk 上进行。这是 DMC 中最简单的连续控制任务之一（24-dim observation, 6-dim action）。CIVO 的发生可能高度依赖于：(a) 动力学的低维度和可预测性——更复杂任务中 RSSM 的 reward gap 模式可能不同；(b) reward 的密度和 scale——sparse reward 任务中 value overestimation 的表现可能不同；(c) observation modality——visual observations 会引入额外的 representation bottleneck。在一个环境上做的诊断无法支撑 Section 6 中关于\"structural incompatibility between flat temporal conditioning and imagination-based actor-critic training\"的泛化性声明。\n- 为什么影响接收：诊断性论文的价值取决于发现的普遍性。单环境发现可能只是 task-specific artifact。\n- 建议修改方向：至少增加 2-3 个不同复杂度的 DMC 任务（如 Cheetah Run, Quadruped Walk, Humanoid Walk），验证 CIVO 在不同动力学复杂度下是否稳定出现。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Factorial design 存在混淆变量\n\n- 具体位置：Table 1 (Section 4.3)\n- 问题：Factorial grid 的关键比较存在混淆。核心的 \"trained vs untrained\" 比较：008d (trained + Sub ON + H=8) vs 008a (untrained + Sub OFF + H=15)——这同时改变了三个因素（embedding type, subsampling, horizon）。唯一干净的比较是 008d vs 008f，但 008f 是 embedding **完全移除**（none），而非 untrained。因此实际上没有一组配置同时保持 subsampling 和 horizon 不变，仅改变 trained → untrained embedding。论文声称 008a/008c 是 untrained 控制组，但它们与 008d 在 subsampling 上不同（OFF vs ON），引入了混淆。\n- 建议：补充 untrained + Sub ON + H=8 + dt=2 配置，形成与 008d 的干净对比。\n\n**W2** [warning] 105K vs 505K 训练步数不对等\n\n- 具体位置：Section 4.5 (\"Treatment configurations run for 105K steps\")\n- 问题：Baseline 运行到 505K 展示了完整的收敛行为（peak 970.4），但所有 treatment 仅运行到 105K。对于一篇诊断 \"collapse\" 动态的论文，这创造了不对称的观察窗口：(a) Self-correcting seed 009b（267.9 @105K）可能在更长训练后恢复；(b) \"healthy\" 的 untrained configs 可能在后期发展出其他 pathology；(c) Oscillatory pattern (009e) 的长期命运未知。论文在 Section 4.5 辩护说 \"105K is sufficient to observe both collapse onset and diagnostic markers\"，但这是循环论证——你不知道 105K 之后会发生什么，因为你没观察。\n- 建议：至少将关键配置（008d 三个 seeds + 008f + 008e_v3 两个 seeds）延长到 300-500K，与 baseline 对等。\n\n**W3** [warning] 对 Pathway B 的解释不充分\n\n- 具体位置：Section 5.6, Section 6.5\n- 问题：008e_v3 seed 2 的 non-CIVO collapse (Pathway B) 是论文最有趣的发现之一，但解释极其薄弱。论文仅描述了现象（entropy 增加、eval 下降、value 稳定），然后含糊地归因于 \"representation space\" 影响。没有提供任何机制性解释：trained embedding 如何在 dt=1 imagination 下导致 actor destabilization？为什么 entropy 增加而非减少？这个 Pathway B 是否可能只是普通的 training instability，与 dt-embedding 无关？Baseline seed 2 (009a) 的稳定性不能排除这一可能，因为增加任何额外 module（包括 subsampling data augmentation）都可能引入 instability。\n- 建议：(1) 提供 Pathway B 的具体机制假说并设计实验验证；(2) 或诚实地承认 Pathway B 的 causation 未建立，仅为观察。\n\n**W4** [warning] RSSM fidelity analysis 的解释可能有误\n\n- 具体位置：Table 4 (Section 5.6), Section 6.1\n- 问题：Table 4 中 008d (trained embedding) 的 reward MAE at dt=1 是 0.0568，at dt=2 是 0.1579（gap 2.78×）。论文将此解释为 \"reward head systematically overpredicts rewards at dt=2\"。但 MAE 只衡量误差大小，不区分 over- 和 under-prediction。高 MAE 可能是正向偏差、负向偏差、或高方差的结果。论文需要证明偏差方向是系统性正向的（即 reward over-prediction 而非 under-prediction），才能支撑 CIVO 的 \"overestimation\" 机制。\n- 建议：报告 reward prediction bias（signed error）而非仅 MAE，以验证方向性假设。\n\n**W5** [warning] 格式不符合 CoRL 2026 要求\n\n- 具体位置：main.tex line 1\n- 问题：论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}`，而 CoRL 2026 要求 PMLR 模板（`\\usepackage[final]{corl_2026}`）。当前格式虽然视觉上接近双栏，但不符合官方提交要求，可能导致 desk reject。\n- 建议：切换到 CoRL 2026 官方 PMLR 模板。\n\n---\n\n## 小问题（不影响接收）\n\n- **bib 质量问题**：`splates2025` 条目 author 为 \"SPlaTES, authors\"（占位符），`nie2025sdar` 和多个条目使用 \"et, al\" 代替完整作者列表——BibTeX 中 \"et al.\" 应写完整作者或正确截断。\n- **hafner2023dreamerv3** 标注 year=2025 (Nature 发表年) 但 cite key 用 2023——可能造成混淆。\n- **Missing citation**: `colas2018seeds` 在 bib 中存在但正文未引用，该文恰恰是关于 seed 数量对 deep RL 结论可靠性影响的直接相关工作，应当引用并讨论。\n- Abstract 中 \"88.9% accuracy\" 放在如此显眼位置有误导性（如 N2 所述）。\n- Section 6.4 对 \"dt-embedding dilemma\" 的讨论倾向于将 negative result 包装为 fundamental insight，但在单环境 + 低 seed 数下，这个 \"dilemma\" 可能只是实验设计的 artifact。\n\n---\n\n## 主要优势\n\n- **清晰的问题定义**：将 \"为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败\" 作为核心问题，切入点明确且有实际意义。\n- **结构化的实验设计**：Factorial ablation 的框架设计本身是好的方法论选择，配置间的对比逻辑清晰。\n- **机制描述细致**：CIVO 的四阶段反馈回路（Section 6.1）描述得清楚且有说服力，三种 post-CIVO 结果的刻画也很有信息量。\n- **诚实的 Limitations**：论文承认了单环境和单架构的局限，且 Finding F6 的 partial falsification 展示了良好的科学态度。\n- **写作质量高**：论文组织良好，Figure/Table 信息密度高，notation 一致。\n\n---\n\n## 总结判断\n\n本文提出了一个有趣的诊断视角（CIVO），但在当前形态下存在多个根本性问题：(1) 2-3 seeds 的统计基础无法支撑强因果声明；(2) NVE 阈值为 post-hoc 选择且无独立验证；(3) 单环境实验严重限制泛化性；(4) 对 CoRL 的 robotics relevance 要求未满足。建议作者大幅增加实验规模（更多 seeds、更多环境），弱化因果语言，并在修改后投稿到更 general 的 RL venue（如 ICML/NeurIPS 的 workshop 或 RLC）。\n\n**建议决定**: Reject (4/10)",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T12:34:08.020623+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4943
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-15T12:34:17.761260+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 47 · 2026-05-15T12:36:36.974599+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 和 Reviewer 3 的意见

以下是 Reviewer 2 和 Reviewer 3 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 的审稿意见（侧重：新颖性 & 贡献度 & Venue Fit & Related Work）

**Overall: 4/10 (Reject)**

### Must-Fix:
- **N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性。全文无 robotics 实验/讨论，仅 DMC Walker Walk proprioceptive。
- **N2** [critical] 单环境实验无法支撑因果 claim 的泛化性。全部 findings F1-F6 仅来自 Walker Walk。"structural incompatibility" 结论的泛化性完全未经验证。
- **N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution。Section 6.6 的三个 future directions 全部 "leave to future work"。

### Should-Fix:
- **W1** 与 TAWM 的对比仅基于 architectural reasoning，缺乏实证验证（未实际运行 TAWM）。
- **W2** NVE threshold 1.5× 的选取缺乏 principled justification（post-hoc fitting to 9 configs）。
- **W3** CIVO 与已知 value overestimation 的区分不够清晰——可能只是 "compounding model error in MBRL" 的特定实例化。
- **W4** Related Work 遗漏：Becker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024) 在 .bib 中但未引用；DreamerV4 讨论不足；48 个 orphan bib entries。

---

## Reviewer 3 的审稿意见（侧重：格式合规 & 写作质量）

**Overall: 4/10 (Borderline Reject)**

### Must-Fix:
- **N1** [critical] 未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险。使用 `\documentclass{article}` + 自定义 geometry。
- **N2** [critical] CoRL scope 适配性严重不足——无物理机器人实验或讨论。
- **N3** [critical] 页数合规性无法验证——换到 PMLR 模板后正文极有可能超过 8 页。

### Should-Fix:
- **W1** Limitations 作为段落嵌入 Conclusion 而非独立 Section。
- **W2** Abstract 过长且过于技术化，缺乏 robotics motivation。
- **W3** Bibliography 严重冗余：77 条 bib entry 中仅 29 条被引用，多个占位符 author。
- **W4** 参考文献格式可能不符合 PMLR 惯例（使用 plainnat）。
- **W5** fig4_mechanism_diagram.pdf 存在但未被论文引用。

---

请逐条给出你的 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T12:38:16.698021+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 交叉回应 Reviewer 2 & Reviewer 3\n\n---\n\n# 回应 Reviewer 2\n\n## Must-Fix\n\n**[AGREE] R2-N1: Venue Fit 严重不足**\n完全同意。这与我的 N3 一致。CoRL 明确要求论文 \"explicitly address a learning question for physical robots\" 或 \"test the proposed learning solution on physical robots\"。全文无任何 robotics 实验、robotics benchmark（RoboSuite/ManiSkill/IsaacGym 等）、或对 real-robot deployment 的实质性讨论。Section 6.7 提到 \"extending this diagnostic framework to... continuous-control benchmarks\" 作为 future work，进一步说明当前版本不满足 CoRL 的 scope 要求。三位 reviewer 在此问题上完全一致，这应当是接收决定的核心考量。\n\n**[AGREE] R2-N2: 单环境无法支撑因果泛化性**\n完全同意。这与我的 N4 一致。补充一点定量论据：Walker Walk 是 DMC 中最简单的 locomotion 任务之一（24-dim obs, 6-dim action），其 RSSM 容易达到高 fidelity（baseline reward MAE 仅 0.0102，Table 4）。在更复杂任务中，RSSM 的 baseline reward prediction 本身就更差，trained embedding 带来的 differential gap 可能被整体预测噪声淹没——即 CIVO 的 2.78× reward gap 可能是 Walker Walk 特有的现象。Section 6.7 的 \"structural incompatibility\" 声明在没有多环境验证的情况下是不负责任的泛化。\n\n**[AGREE with nuance] R2-N3: 贡献度不足——纯诊断负面结果缺乏 actionable solution**\n基本同意，但有一定保留。诊断性论文（negative results / diagnostic analysis）在学术上有独立价值——Engstrom et al. (2020) 和 Andrychowicz et al. (2021) 都是纯诊断工作且获高引。问题不在于 \"没有 solution\" 本身，而在于：(1) 诊断的统计基础不够扎实（2-3 seeds，如我的 N1）；(2) 诊断的泛化范围不够广（单环境）；(3) Section 6.6 提出的三个 future direction（hierarchical abstraction、embedding regularization、transformer extension）都是 one-sentence speculation，未提供任何初步验证。如果诊断本身足够 robust 且 generalizable，缺少 solution 不应成为 reject 的理由；但在当前形态下，诊断的可靠性本身就存疑，叠加缺少 solution 使贡献确实不足。\n\n## Should-Fix\n\n**[AGREE] R2-W1: 与 TAWM 的对比缺乏实证**\n同意。Section 6.3 关于 \"MPC re-plans from real states\" vs \"imagination-based bootstrapping\" 的分析是合理的架构推理，但未用实验验证。具体来说：(1) 论文未实际运行 TAWM 或 TD-MPC2 + dt-conditioning 来确认它们确实不产生 CIVO；(2) 未验证在 DreamerV3 中添加 \"re-plan from real states\" 的机制（如缩短 rollout + 更频繁 re-grounding）是否能缓解 CIVO。这两个实验中任一个都会大幅强化论文的核心论点。仅靠 architectural reasoning 无法排除 TAWM 的成功可能源于其他差异（如 planning horizon 长度、采样策略、value function 的不同角色等）。\n\n**[AGREE] R2-W2: NVE threshold 1.5× post-hoc**\n完全同意，这与我的 N2 一致。不再赘述。\n\n**[REBUT with partial agreement] R2-W3: CIVO 可能只是 \"compounding model error in MBRL\" 的实例化**\n部分反驳。R2 说得对，CIVO 的上层逻辑（model error → value overestimation → policy exploitation）确实是 MBRL 中已知的 failure mode（MBPO [Janner et al. 2019], MOPO [Yu et al. 2020]）。但论文在 Section 6.1 提供了一个有价值的细化：CIVO 的触发机制是 *learned input feature* (dt-embedding) 与 reward head 的 co-adaptation 导致的 *asymmetric* fidelity（Table 4, 2.78× gap），而非简单的 compounding error 或 rollout 长度问题。untrained embedding 消除 CIVO（Section 5.3）而 compounding error 不会因 embedding 训练方式改变，这一对比提供了超越 \"compounding error\" 泛化解释的机制特异性。当然，这个 specific mechanism 是否稳健成立仍受限于统计检验力不足（N1），但 R2 将 CIVO 完全等同于已知 failure mode 过于简化。\n\n**[AGREE] R2-W4: Related Work 遗漏 + orphan bib entries**\n同意。我验证了 references.bib：`beckerehmck2023multitimestep`（multi-timestep models for MBRL）、`park2021sar`（time discretization-invariant action repetition）、`wang2024seac`（elastic time steps）均在 bib 中但未在正文中引用。这三篇都与 variable temporal resolution in RL 直接相关，遗漏引用是 scholarship 缺陷。此外，`colas2018seeds` 也在 bib 中但未引用，而该文恰好是关于 seed 数量对 deep RL 结论可靠性影响的关键参考——如我在 N1 中指出的。77 条 bib entries 中大量未引用的 orphan entries 反映了论文的粗糙程度。\n\n---\n\n# 回应 Reviewer 3\n\n## Must-Fix\n\n**[AGREE] R3-N1: 未使用 CoRL 2026 官方 PMLR 模板**\n完全同意。这与我的 W5 一致。main.tex line 1 使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + 自定义 `\\usepackage[margin=0.75in]{geometry}`（line 12），完全不符合 CoRL 2026 要求的 PMLR 模板。这不仅是格式问题——PMLR 模板的 margin、字号、行距与当前 setup 不同，切换后的页面利用率和排版效果会有显著变化。\n\n**[AGREE] R3-N2: CoRL scope 适配性**\n同意，与 R2-N1 和我的 N3 一致。三位 reviewer 共识。\n\n**[AGREE] R3-N3: 换模板后可能超页**\n同意这是合理担忧。当前用 0.75in margin + 10pt article class 的双栏排版比 PMLR 模板更紧凑。粗略估计：PMLR corl_2026 模板通常有更宽的 margin 和更大的行距。当前论文 7 个 section + 6 个 figure + 4 个 table 的内容量，切换到 PMLR 后正文很可能超过 8 页。作者需要压缩内容——可能需要删减 Section 6 (Analysis & Discussion) 中的部分展开论述，或将某些 table/figure 移入 appendix。\n\n## Should-Fix\n\n**[REBUT] R3-W1: Limitations 应为独立 Section**\n部分反驳。查看 conclusion.tex，Limitations 确实是 `\\paragraph{Limitations.}` 嵌入 Conclusion section。但 CoRL 的要求是 \"papers must include a limitations section\"——这里的 \"section\" 未必指 LaTeX 的 `\\section{}`。查看 CoRL 2023 reviewer guidelines 的原文，是要求 \"honestly reported limitations\" 并给予正面评价。当前实现是一个清晰标注的段落，内容实质到位（承认了单环境和单架构的局限）。我认为 R3 对此的 severity 有些夸大——这是一个 minor formatting preference，而非 must-fix。不过为保险起见，改为 `\\subsection{Limitations}` 或独立 `\\section{Limitations}` 确实更安全。\n\n**[AGREE with partial caveat] R3-W2: Abstract 过长且缺乏 robotics motivation**\n同意 \"缺乏 robotics motivation\" 的部分——对 CoRL 投稿，abstract 应在首句建立 robotics 相关性。但 \"过长且过于技术化\" 我认为对于诊断性论文是可接受的风格选择。Abstract 中的具体数字（2.78×, 4/4, 88.9%）使其 self-contained 且可检索。真正的问题不是技术密度，而是缺少 \"这对 robot learning 意味着什么\" 的一句话。\n\n**[AGREE] R3-W3: Bibliography 严重冗余**\n完全同意。如我在小问题中指出，77 条 bib entries 中大量 orphan（R2-W4 也提到此问题）。`splates2025` 的 author 是 \"SPlaTES, authors\"（明显的占位符），`nie2025sdar` 使用 \"et, al\" 代替完整作者列表。这些不仅是冗余问题，更反映了论文准备的粗糙度。\n\n**[AGREE] R3-W4: 参考文献格式可能不符 PMLR**\n同意。main.tex line 58 使用 `\\bibliographystyle{plainnat}`，而 PMLR 模板通常自带 bibliography style（如 `\\bibliographystyle{pmlr-style}` 或 `abbrvnat`）。切换模板后需要同步更换 bibliography style，否则格式不一致。\n\n**[AGREE] R3-W5: fig4_mechanism_diagram.pdf 未被引用**\n同意。我检查了全部 .tex 文件：正文引用了 fig1 (learning curves), fig2 (NVE trajectory), fig3 (factorial grid), fig5 (dt amplification), fig6 (multiple pathways)——唯独跳过了 fig4。`\\graphicspath` 指向 `../../artifacts/`，如果该目录下确实存在 `figures/paper/fig4_mechanism_diagram.pdf`，这是一个遗漏（mechanism diagram 对于解释 CIVO 的四阶段反馈回路可能很有价值）。如果是 intentionally excluded，至少不应留在目录中。\n\n---\n\n## 综合评估\n\n三位 reviewer 在三个核心问题上达成完全共识：\n1. **CoRL venue fit 不足**（R1-N3, R2-N1, R3-N2）\n2. **单环境局限**（R1-N4, R2-N2）\n3. **格式不合规**（R1-W5, R3-N1）\n\n我与 R2 的主要分歧在 W3：R2 认为 CIVO 完全是已知问题的 repackaging，我认为 trained vs untrained embedding 的对比提供了一定的机制特异性（虽然 statistical power 不足削弱了这一贡献）。\n\n我的独有关注点（未被 R2/R3 充分覆盖）是 **统计检验力**（N1）和 **NVE 阈值的 post-hoc 性质**（N2）——这些是方法严谨性层面的根本问题，即使解决了 venue fit 和格式问题，论文的结论可靠性仍然存疑。\n\n**维持评分: 4/10 (Reject)**",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 交叉回应 Reviewer 2 & Reviewer 3\n\n---\n\n# 回应 Reviewer 2\n\n## Must-Fix\n\n**[AGREE] R2-N1: Venue Fit 严重不足**\n完全同意。这与我的 N3 一致。CoRL 明确要求论文 \"explicitly address a learning question for physical robots\" 或 \"test the proposed learning solution on physical robots\"。全文无任何 robotics 实验、robotics benchmark（RoboSuite/ManiSkill/IsaacGym 等）、或对 real-robot deployment 的实质性讨论。Section 6.7 提到 \"extending this diagnostic framework to... continuous-control benchmarks\" 作为 future work，进一步说明当前版本不满足 CoRL 的 scope 要求。三位 reviewer 在此问题上完全一致，这应当是接收决定的核心考量。\n\n**[AGREE] R2-N2: 单环境无法支撑因果泛化性**\n完全同意。这与我的 N4 一致。补充一点定量论据：Walker Walk 是 DMC 中最简单的 locomotion 任务之一（24-dim obs, 6-dim action），其 RSSM 容易达到高 fidelity（baseline reward MAE 仅 0.0102，Table 4）。在更复杂任务中，RSSM 的 baseline reward prediction 本身就更差，trained embedding 带来的 differential gap 可能被整体预测噪声淹没——即 CIVO 的 2.78× reward gap 可能是 Walker Walk 特有的现象。Section 6.7 的 \"structural incompatibility\" 声明在没有多环境验证的情况下是不负责任的泛化。\n\n**[AGREE with nuance] R2-N3: 贡献度不足——纯诊断负面结果缺乏 actionable solution**\n基本同意，但有一定保留。诊断性论文（negative results / diagnostic analysis）在学术上有独立价值——Engstrom et al. (2020) 和 Andrychowicz et al. (2021) 都是纯诊断工作且获高引。问题不在于 \"没有 solution\" 本身，而在于：(1) 诊断的统计基础不够扎实（2-3 seeds，如我的 N1）；(2) 诊断的泛化范围不够广（单环境）；(3) Section 6.6 提出的三个 future direction（hierarchical abstraction、embedding regularization、transformer extension）都是 one-sentence speculation，未提供任何初步验证。如果诊断本身足够 robust 且 generalizable，缺少 solution 不应成为 reject 的理由；但在当前形态下，诊断的可靠性本身就存疑，叠加缺少 solution 使贡献确实不足。\n\n## Should-Fix\n\n**[AGREE] R2-W1: 与 TAWM 的对比缺乏实证**\n同意。Section 6.3 关于 \"MPC re-plans from real states\" vs \"imagination-based bootstrapping\" 的分析是合理的架构推理，但未用实验验证。具体来说：(1) 论文未实际运行 TAWM 或 TD-MPC2 + dt-conditioning 来确认它们确实不产生 CIVO；(2) 未验证在 DreamerV3 中添加 \"re-plan from real states\" 的机制（如缩短 rollout + 更频繁 re-grounding）是否能缓解 CIVO。这两个实验中任一个都会大幅强化论文的核心论点。仅靠 architectural reasoning 无法排除 TAWM 的成功可能源于其他差异（如 planning horizon 长度、采样策略、value function 的不同角色等）。\n\n**[AGREE] R2-W2: NVE threshold 1.5× post-hoc**\n完全同意，这与我的 N2 一致。不再赘述。\n\n**[REBUT with partial agreement] R2-W3: CIVO 可能只是 \"compounding model error in MBRL\" 的实例化**\n部分反驳。R2 说得对，CIVO 的上层逻辑（model error → value overestimation → policy exploitation）确实是 MBRL 中已知的 failure mode（MBPO [Janner et al. 2019], MOPO [Yu et al. 2020]）。但论文在 Section 6.1 提供了一个有价值的细化：CIVO 的触发机制是 *learned input feature* (dt-embedding) 与 reward head 的 co-adaptation 导致的 *asymmetric* fidelity（Table 4, 2.78× gap），而非简单的 compounding error 或 rollout 长度问题。untrained embedding 消除 CIVO（Section 5.3）而 compounding error 不会因 embedding 训练方式改变，这一对比提供了超越 \"compounding error\" 泛化解释的机制特异性。当然，这个 specific mechanism 是否稳健成立仍受限于统计检验力不足（N1），但 R2 将 CIVO 完全等同于已知 failure mode 过于简化。\n\n**[AGREE] R2-W4: Related Work 遗漏 + orphan bib entries**\n同意。我验证了 references.bib：`beckerehmck2023multitimestep`（multi-timestep models for MBRL）、`park2021sar`（time discretization-invariant action repetition）、`wang2024seac`（elastic time steps）均在 bib 中但未在正文中引用。这三篇都与 variable temporal resolution in RL 直接相关，遗漏引用是 scholarship 缺陷。此外，`colas2018seeds` 也在 bib 中但未引用，而该文恰好是关于 seed 数量对 deep RL 结论可靠性影响的关键参考——如我在 N1 中指出的。77 条 bib entries 中大量未引用的 orphan entries 反映了论文的粗糙程度。\n\n---\n\n# 回应 Reviewer 3\n\n## Must-Fix\n\n**[AGREE] R3-N1: 未使用 CoRL 2026 官方 PMLR 模板**\n完全同意。这与我的 W5 一致。main.tex line 1 使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + 自定义 `\\usepackage[margin=0.75in]{geometry}`（line 12），完全不符合 CoRL 2026 要求的 PMLR 模板。这不仅是格式问题——PMLR 模板的 margin、字号、行距与当前 setup 不同，切换后的页面利用率和排版效果会有显著变化。\n\n**[AGREE] R3-N2: CoRL scope 适配性**\n同意，与 R2-N1 和我的 N3 一致。三位 reviewer 共识。\n\n**[AGREE] R3-N3: 换模板后可能超页**\n同意这是合理担忧。当前用 0.75in margin + 10pt article class 的双栏排版比 PMLR 模板更紧凑。粗略估计：PMLR corl_2026 模板通常有更宽的 margin 和更大的行距。当前论文 7 个 section + 6 个 figure + 4 个 table 的内容量，切换到 PMLR 后正文很可能超过 8 页。作者需要压缩内容——可能需要删减 Section 6 (Analysis & Discussion) 中的部分展开论述，或将某些 table/figure 移入 appendix。\n\n## Should-Fix\n\n**[REBUT] R3-W1: Limitations 应为独立 Section**\n部分反驳。查看 conclusion.tex，Limitations 确实是 `\\paragraph{Limitations.}` 嵌入 Conclusion section。但 CoRL 的要求是 \"papers must include a limitations section\"——这里的 \"section\" 未必指 LaTeX 的 `\\section{}`。查看 CoRL 2023 reviewer guidelines 的原文，是要求 \"honestly reported limitations\" 并给予正面评价。当前实现是一个清晰标注的段落，内容实质到位（承认了单环境和单架构的局限）。我认为 R3 对此的 severity 有些夸大——这是一个 minor formatting preference，而非 must-fix。不过为保险起见，改为 `\\subsection{Limitations}` 或独立 `\\section{Limitations}` 确实更安全。\n\n**[AGREE with partial caveat] R3-W2: Abstract 过长且缺乏 robotics motivation**\n同意 \"缺乏 robotics motivation\" 的部分——对 CoRL 投稿，abstract 应在首句建立 robotics 相关性。但 \"过长且过于技术化\" 我认为对于诊断性论文是可接受的风格选择。Abstract 中的具体数字（2.78×, 4/4, 88.9%）使其 self-contained 且可检索。真正的问题不是技术密度，而是缺少 \"这对 robot learning 意味着什么\" 的一句话。\n\n**[AGREE] R3-W3: Bibliography 严重冗余**\n完全同意。如我在小问题中指出，77 条 bib entries 中大量 orphan（R2-W4 也提到此问题）。`splates2025` 的 author 是 \"SPlaTES, authors\"（明显的占位符），`nie2025sdar` 使用 \"et, al\" 代替完整作者列表。这些不仅是冗余问题，更反映了论文准备的粗糙度。\n\n**[AGREE] R3-W4: 参考文献格式可能不符 PMLR**\n同意。main.tex line 58 使用 `\\bibliographystyle{plainnat}`，而 PMLR 模板通常自带 bibliography style（如 `\\bibliographystyle{pmlr-style}` 或 `abbrvnat`）。切换模板后需要同步更换 bibliography style，否则格式不一致。\n\n**[AGREE] R3-W5: fig4_mechanism_diagram.pdf 未被引用**\n同意。我检查了全部 .tex 文件：正文引用了 fig1 (learning curves), fig2 (NVE trajectory), fig3 (factorial grid), fig5 (dt amplification), fig6 (multiple pathways)——唯独跳过了 fig4。`\\graphicspath` 指向 `../../artifacts/`，如果该目录下确实存在 `figures/paper/fig4_mechanism_diagram.pdf`，这是一个遗漏（mechanism diagram 对于解释 CIVO 的四阶段反馈回路可能很有价值）。如果是 intentionally excluded，至少不应留在目录中。\n\n---\n\n## 综合评估\n\n三位 reviewer 在三个核心问题上达成完全共识：\n1. **CoRL venue fit 不足**（R1-N3, R2-N1, R3-N2）\n2. **单环境局限**（R1-N4, R2-N2）\n3. **格式不合规**（R1-W5, R3-N1）\n\n我与 R2 的主要分歧在 W3：R2 认为 CIVO 完全是已知问题的 repackaging，我认为 trained vs untrained embedding 的对比提供了一定的机制特异性（虽然 statistical power 不足削弱了这一贡献）。\n\n我的独有关注点（未被 R2/R3 充分覆盖）是 **统计检验力**（N1）和 **NVE 阈值的 post-hoc 性质**（N2）——这些是方法严谨性层面的根本问题，即使解决了 venue fit 和格式问题，论文的结论可靠性仍然存疑。\n\n**维持评分: 4/10 (Reject)**",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T12:38:21.894282+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5196
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-15T12:38:28.734598+00:00_

交叉回应已提交。对 R2 和 R3 的每条 Must-Fix/Should-Fix 逐条给出了 [AGREE] 或 [REBUT]，并标注了与我自己审稿意见的交叉关系。三位 reviewer 在 venue fit、单环境局限、格式合规三个核心问题上完全一致。我与 R2 唯一的实质分歧是 W3（CIVO 的新颖性），我认为 trained vs untrained embedding 对比提供了一定的机制特异性，不应完全归为已知 failure mode 的 repackaging。维持 4/10 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 3

118 recorded events

### User

_source line 51 · 2026-05-24T07:01:08.191611+00:00_

[Round 3 审稿请求]:
## Round 3 修订评估任务 — Reviewer 1（方法严谨性 + 实验充分性）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf`
**目标 Venue**: CoRL 2026 Main Conference
**Deadline**: 2026-05-29
**页数限制**: 8 页正文（References/Appendix 不计）
**模板**: PMLR (`\usepackage{corl_2026}`)
**匿名规则**: Double-blind
**审查侧重**: 方法严谨性、实验设计充分性、统计论证

### 你的核心任务

这是 Round 3 继续审稿。论文在 Round 1 后进行了大幅修改。你需要**逐条检查以下 open/in_progress issue**，标注 `[RESOLVED]` 或 `[STILL_OPEN]` + 理由：

---

### 必须逐条检查的 Issue（方法/实验类）

**1. R1-N1 [critical, in_progress]: 统计检验力不足**
- Round 1 问题：2-3 seeds 无法支撑 causal 声明
- 已知修改：seeds 增至 4，语言从 "causal factor" 改为 "strongest predictor"，IQM + bootstrap CI 已添加
- **检查要点**：4 seeds 是否足够？因果语言是否已充分弱化？IQM/CI 报告是否到位？论文现称 26/29 accuracy (AUROC=0.953, LOEO)——这些数字的统计意义如何？

**2. R1-N4 [critical, in_progress]: 单环境局限**
- Round 1 问题：仅 Walker Walk，无法泛化
- 已知修改：扩展到 Walker Walk + Cheetah Run + 3 个 ManiSkill 任务（PickCube、StackCube、PegInsertionSide），Table cross_domain 已添加
- **检查要点**：5 环境覆盖度是否足够？ManiSkill 结果（非 CIVO）对论文论点是积极还是消极贡献？跨环境结论的措辞是否准确？

**3. R1-W1 [warning, in_progress]: Factorial design 混淆变量**
- Round 1 问题：secondary comparisons 同时改变多个因素
- 已知修改：论文应已标注 primary vs secondary comparisons
- **检查要点**：是否在文中显式区分了 primary（008d vs 008f）和 secondary comparisons？2×2 factorial grid 是否完整？

**4. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 训练步数不对等**
- Round 1 问题：treatment 仅 105K，baseline 505K，可能是速度差
- 已知修改：baseline 4 seeds 到 505K，treatment extension exp_045 延长到 300K
- **检查要点**：论文中是否讨论了步数不对等问题？是否有 treatment 长跑数据？结论是否仍然站得住脚？

**5. R1-W3 [warning, open]: Pathway B 解释不充分**
- Round 1 问题：仅 1 seed 证据
- 已知修改：语言弱化为 "preliminary evidence"，现有 2 seeds
- **检查要点**：2 seeds 是否改善了可信度？声明力度是否与证据匹配？

**6. R2-W1 [warning, open]: TAWM 对比无实证**
- Round 1 问题：仅 architectural reasoning
- **检查要点**：论文是否改进了 TAWM 对比的论证？是否引用了 TAWM 原文数据？是否在 Limitations 中承认了这一局限？

**7. R1-W4 [warning, resolved in R1]: RSSM signed reward error**
- 已标记 resolved，验证 signed error 分析是否在论文中体现。

---

### 额外审查要点（不限于上述 issue）

- 四级干预层级（gradient/output/representation/architecture）的实验设计是否严谨？结论是否过度泛化？
- Dual-critic convergence 分析（ρ > 0.999）的方法论是否正确？
- Online CIVO detector 的评估（TPR=5/5, FPR=2/9）是否有足够样本量？
- 修改是否引入了新的方法论问题？

### 输出格式

1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由
2. 列出新发现的问题（如有）
3. 给出方法严谨性评分（1-10）和简要总评

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T07:01:28.839451+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-24T07:01:28.891212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T07:01:54.030287+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-24T07:01:55.138460+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
  "pages": "1-8",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
    "pages": "1-8",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-24T07:01:55.741018+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
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

_source line 57 · 2026-05-24T07:01:59.759073+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found information about CoRL 2026, though the specific detailed reviewer guidelines and review form criteria for CoRL 2026 were not fully available in the search results. However, I can share what was found:

**CoRL 2026 Reviewer Requirements:**

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

**Related CoRL Evaluation Criteria:**

While the detailed 2026 review form wasn't in the search results, I found that CoRL 2024 evaluated submissions based on "the significance and novelty of the results, either theoretical or empirical." Additionally, submissions should focus on a core robotics problem and authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

For the complete and most up-to-date CoRL 2026 reviewer guidelines and review 
…[truncated 261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5728
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-24T07:02:00.666812+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 320.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 393.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 317.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 317.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 296.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 338.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 299.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 337.5}], \"total_pages\": 33, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated
…[truncated 95 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5528
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-24T07:02:00.667356+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4926
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-24T07:02:13.041597+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and reviewer guidelines for CoRL. List all evaluation dimensions with their scales and descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and reviewer guidelines for CoRL. List all evaluation dimensions with their scales and descriptions."
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-24T07:02:13.847306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-24T07:02:13.897982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-24T07:02:14.303703+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-24T07:02:14.657478+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 759
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T07:02:17.351119+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided content, here's what the instructions specify:

## Review Evaluation Criteria

The document outlines **one primary evaluation dimension** for regular papers:

**Significance and Impact**: Papers are assessed on "the significance and novelty of the results, either theoretical or empirical" with consideration for "objective establishment" and "potential for scientific and technological impact."

## Scope Requirements

Submissions must demonstrate relevance to robot learning through either:
- **Intent**: Explicitly addressing a learning question for physical robots, OR
- **Outcome**: Testing the proposed learning solution on physical robots

## Desk Rejection Grounds

Papers may be rejected at desk review stage for:
1. Formatting violations
2. Anonymity breaches
3. Scope misalignment (lacking robotics or learning components)

## Reviewer Qualifications

The guidelines specify that reviewers should possess:
- Expertise in robotics, robot learning, and machine learning
- Ideally "a minimum of 3 first author publications in major robotics conferences" such as CoRL, RSS, ICRA, IROS, and related venues
- Publications in core ML venues like NeurIPS, ICML, and similar conferences

**Note**: The provided content does not include detailed scoring scales, numbered rating systems, or a formal review form structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4309
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T07:02:22.269660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T07:02:22.824259+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-24T07:02:22.976250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-24T07:02:23.279091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-24T07:02:23.736441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 760
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-24T07:02:23.838979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 559
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-24T07:02:23.839713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-24T07:02:24.199235+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 359
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-24T07:02:27.665090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-24T07:02:28.068214+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-24T07:02:28.219060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-24T07:02:28.574037+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-24T07:02:33.547736+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
  "pages": "9-20",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
    "pages": "9-20",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-24T07:02:34.652611+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 307.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 332.3}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 328.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 231.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 396.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 372.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 297.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 209.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_r
…[truncated 1018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1104
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-24T07:02:37.322171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-24T07:02:37.774054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-24T07:02:38.581164+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1258
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-24T07:02:38.583666+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-24T07:02:38.584133+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-24T07:02:38.985739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-24T07:02:39.138721+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-24T07:02:39.695812+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 710
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-24T07:02:43.074912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-24T07:02:43.530602+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-24T07:02:43.531196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-24T07:02:44.488076+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-24T07:02:44.488641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-24T07:02:44.815969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-24T07:02:44.886233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 397
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-24T07:02:45.508334+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 692
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-24T07:02:49.871101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-24T07:02:50.482361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-24T07:02:51.034337+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1163
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-24T07:02:51.045416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-24T07:02:51.427385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-24T07:02:51.429632+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 947
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-24T07:02:52.077444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1032
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-24T07:02:52.346232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 918
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-24T07:02:56.061197+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
  "pages": "21-33",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
    "pages": "21-33",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-24T07:02:57.143589+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p21.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 265.8}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p22.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 265.6}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p23.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 373.2}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p24.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 285.1}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p25.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 305.2}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p26.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 146.1}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p27.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 356.9}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p28.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 285.5}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review
…[truncated 1246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1082
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-24T07:03:02.878451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-24T07:03:03.331606+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-24T07:03:03.534050+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-24T07:03:04.138511+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-24T07:03:04.189628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-24T07:03:04.492209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-24T07:03:04.596485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-24T07:03:04.949722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-24T07:03:10.169018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-24T07:03:10.573579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-24T07:03:10.574099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-24T07:03:11.530562+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-24T07:03:11.631475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-24T07:03:12.034457+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-24T07:03:12.086236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p28.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-24T07:03:12.489597+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-24T07:03:25.010221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-24T07:03:25.451927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-24T07:03:26.313404+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1303
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-24T07:03:26.316100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p31.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-24T07:03:26.881128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1429
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-24T07:03:26.881570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p32.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-24T07:03:27.121964+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-24T07:03:27.174416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p33.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-24T07:03:27.413225+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 238
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-24T07:03:27.814174+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 932
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-24T07:03:43.000848+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read key LaTeX sections",
  "prompt": "Read the following files completely and report back the full content of each:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex\n\nReport the full text content. Do not summarize - I need the exact wording.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read key LaTeX sections",
    "prompt": "Read the following files completely and report back the full content of each:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex\n\nReport the full text content. Do not summarize - I need the exact wording.",
    "subagent_type": "Explore"
  }
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-24T07:03:44.407310+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer form scoring dimensions rating scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer form scoring dimensions rating scale"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-24T07:03:44.608485+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-24T07:03:45.010543+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\times$ reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\% sensitivity.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-24T07:03:45.011105+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-24T07:03:45.412942+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-24T07:03:45.493886+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-24T07:03:45.594547+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-24T07:03:45.599335+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-24T07:03:45.700309+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-24T07:03:48.962350+00:00_

Web search results for query: "CoRL 2026 reviewer form scoring dimensions rating scale"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"ICLR 2026 Scores Released: Reviewers Call It \"Crazy\", DeepMind Researchers Show Comeback from Desperate Situation","url":"https://eu.36kr.com/en/p/3551362253731718"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"Reviewer agreement trends from four years of electronic submissions of conference abstract","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1473196/"}]

I found general information about CoRL 2026 in the search results, including instructions for authors and information about the conference. However, the search results do not contain specific information about the reviewer form scoring dimensions or the rating scale used for CoRL 2026 reviews.

The search results show information about CoRL 2023 reviewer guidelines and CoRL 2026 general conference information, but they don't include the specific scoring dimensions or rating scale details from the reviewer form itself. To find this information, you would likely need to:

1. Access the CoRL 2026 OpenReview page directly and look for reviewer guidelines
2. Contact the CoRL 2026 conference organizers
3. Check if there's a specific reviewer handbook or documentation available to regist
…[truncated 234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 4555
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-24T07:05:10.047464+00:00_

Here is the full content of each file:

## 1. abstract_body.tex

```tex
World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\times$ reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\% sensitivity.
```

## 2. methodology.tex

```tex
\section{Experimental Setup}
\label{sec:methodology}

\subsection{Base Architecture}
\label{sec:base_arch}

All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.

\subsection{Variable-Rate Imagination Mechanism}
\label{sec:variable_rate}

We introduce three orthogonal architectural modifications that enable variabl
…[truncated 21333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 87046
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-24T07:05:16.255498+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract all review scoring dimensions, rating scales, and evaluation criteria for CoRL reviews. Include specific numeric scales, dimension names, and descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract all review scoring dimensions, rating scales, and evaluation criteria for CoRL reviews. Include specific numeric scales, dimension names, and descriptions."
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-24T07:05:17.109982+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference",
  "prompt": "Extract reviewer guidelines, review form dimensions, scoring criteria, and rating scales for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference",
    "prompt": "Extract reviewer guidelines, review form dimensions, scoring criteria, and rating scales for CoRL 2026."
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-24T07:05:20.474846+00:00_

# CoRL 2026 Conference Review Information

I cannot extract the requested information about reviewer guidelines, review form dimensions, scoring criteria, and rating scales for CoRL 2026 based on the content provided.

**Why:** The webpage content you shared contains only OpenReview's site navigation, footer, and general platform information. It does not include:

- Reviewer guidelines
- Review form specifications
- Scoring criteria details
- Rating scale information

**To find this information**, you would need to:

1. Navigate directly to the CoRL 2026 conference venue page on OpenReview
2. Look for sections labeled "Reviewer Instructions," "Review Guidelines," or "Submission/Review Information"
3. Check the conference's official website or Call for Papers announcement

If you can provide the actual CoRL 2026 conference page content, I'd be happy to extract the specific review guidelines and scoring criteria you're seeking.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3364
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-24T07:05:21.077394+00:00_

# CoRL 2023 Review Scoring Dimensions

Based on the provided guidelines, CoRL 2023 specifies **six primary evaluation dimensions** for reviewer assessments:

1. **Originality** - Evaluates novelty of problems/methods and how clearly the work differentiates from prior contributions

2. **Quality** - Assesses technical soundness, evidence supporting claims, methodological appropriateness, and author honesty about strengths/weaknesses

3. **Clarity** - Examines writing quality, organization, and informativeness for reproducibility by expert readers

4. **Significance** - Determines importance of results and potential impact on researchers and practitioners

5. **Relevance** - Judges alignment with robot learning focus and whether "the CoRL audience be interested in reading this paper"

6. **Limitations** - Reviews how honestly authors report constraints, with appreciation for transparent limitation sections

## Notable Guidance

The document emphasizes that papers need not meet strict policies (mandatory code/data release, real robot evaluation, or state-of-the-art performance) to warrant acceptance. Rather, reviewers should evaluate whether work advances knowledge through "novel perspectives, insights, and sufficient knowledge advancement."

**No specific numeric rating scales are provided** in these guidelines—only the six qualitative dimensions for assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4821
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-24T07:05:24.741126+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 2025 OpenReview review form rating scale overall recommendation soundness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 2025 OpenReview review form rating scale overall recommendation soundness"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-24T07:05:41.366953+00:00_

Web search results for query: "CoRL 2024 2025 OpenReview review form rating scale overall recommendation soundness"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"Can Small and Reasoning Large Language Models Score Journal Articles for Research Quality and Do Averaging and Few-shot Help?","url":"https://arxiv.org/pdf/2510.22389"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"Best Reviewers Award for 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11955497/"}]

I found the OpenReview pages for CoRL 2024 and 2025, but the search results don't contain detailed information about the review form rating scales. Let me search more specifically for the review form details.

Links: [{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"Paper Ranking Methodology","url":"https://openreview-copilot.eamag.me/ranking"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"OpenReviewer: A Specialized Lar
…[truncated 5950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 16625
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-24T07:05:47.764022+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract all review form dimensions, rating scales (numeric), evaluation criteria, scoring rubrics, and overall recommendation scale. Include every numbered scale option."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract all review form dimensions, rating scales (numeric), evaluation criteria, scoring rubrics, and overall recommendation scale. Include every numbered scale option."
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-24T07:05:50.875432+00:00_

# CoRL 2024 Review Criteria Analysis

Based on the provided content, **no specific review form dimensions, numeric rating scales, or scoring rubrics are detailed** in this instruction document.

## What IS Specified:

**Review Evaluation Criteria (Qualitative):**
- Significance and novelty of results (theoretical or empirical)
- Objective establishment of results
- Potential for "scientific and technological impact"
- Relevance to robotic learning

**Desk Rejection Categories:**
The document outlines three grounds for desk rejection rather than a scoring system:
- Formatting violations
- Anonymity breaches
- Scope misalignment with robot learning

## What Is NOT Provided:

- Numeric rating scales (e.g., 1-5, 1-10)
- Specific scoring rubrics with point distributions
- Overall recommendation scale options
- Quantified evaluation dimensions
- Weighted scoring criteria

The document emphasizes qualitative judgment criteria focused on significance, novelty, and impact rather than providing a formal numeric assessment framework typical of peer review forms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3111
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-24T07:05:55.621081+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=pREGFBBhKG",
  "prompt": "Extract all review form dimensions, rating scales, and scoring criteria used in this CoRL review. Include the specific rating questions and their scale options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=pREGFBBhKG",
    "prompt": "Extract all review form dimensions, rating scales, and scoring criteria used in this CoRL review. Include the specific rating questions and their scale options."
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-24T07:05:57.673118+00:00_

I cannot extract review form dimensions, rating scales, or scoring criteria from the provided content because the page displays an error message indicating that a specific note (pREGFBBhKG) was not found on OpenReview.

The webpage content only shows the error message and navigation elements—it does not contain any actual review form information, rating scales, or CoRL review criteria. To access this information, you would need to navigate to a functioning page containing the actual review form or venue details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 2052
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-24T07:06:04.256238+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net CoRL 2024 \"overall score\" OR \"overall rating\" OR \"recommendation\" review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net CoRL 2024 \"overall score\" OR \"overall rating\" OR \"recommendation\" review"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-24T07:06:08.680949+00:00_

Web search results for query: "site:openreview.net CoRL 2024 "overall score" OR "overall rating" OR "recommendation" review"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 Workshop Assembly | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FAssembly"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 Workshop XE | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FXE"},{"title":"CoRL 2024 Workshop SAFE-ROL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FSAFE-ROL"},{"title":"CoRL 2024 Workshop LEAP | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FLEAP"},{"title":"CoRL 2024 Workshop | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 Workshop CoRoboLearn | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FCoRoboLearn"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"}]

I've performed the web search for CoRL 2024 reviews on OpenReview. The search returned the main OpenReview pages for CoRL 2024, including the conference submissions page. The results show that there are submitted papers published on September 5, 2024, with various modification dates through November 2024.

The search found the OpenReview submission listings for CoRL 2024 Conference, which contains papers with their peer review information, though the specific review details with overall scores and recommendations are not disp
…[truncated 343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 4424
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-24T07:06:23.331660+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference",
  "prompt": "Find paper IDs or links to individual paper pages for CoRL 2024 accepted papers. I need to see a review form with rating scales. List a few paper URLs/forum IDs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference",
    "prompt": "Find paper IDs or links to individual paper pages for CoRL 2024 accepted papers. I need to see a review form with rating scales. List a few paper URLs/forum IDs."
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-24T07:06:28.960776+00:00_

# CoRL 2024 Paper Submissions

Based on the webpage content, here are several paper URLs/forum IDs from the CoRL 2024 Conference:

1. **Body Transformer: Leveraging Robot Embodiment for Policy Learning**
   - Forum ID: `Oce2215aJE`
   - URL: `/forum?id=Oce2215aJE`

2. **Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation**
   - Forum ID: `FO6tePGRZj`
   - URL: `/forum?id=FO6tePGRZj`

3. **OpenVLA: An Open-Source Vision-Language-Action Model**
   - Forum ID: `ZMnD6QZAE6`
   - URL: `/forum?id=ZMnD6QZAE6`

4. **Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation**
   - Forum ID: `AuJnXGq3AL`
   - URL: `/forum?id=AuJnXGq3AL`

**Regarding review forms:** The provided content does not display rating scales or peer review information. The webpage only shows accepted papers with publication dates and author information. To access review details, you would need to visit individual paper forum pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5629
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-24T07:06:32.976950+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=Oce2215aJE",
  "prompt": "Extract the review form dimensions and rating scales used. Look for fields like \"Overall Score\", \"Soundness\", \"Presentation\", \"Contribution\", \"Confidence\" and their numeric scales. List each dimension with its scale and the reviewer's rating."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=Oce2215aJE",
    "prompt": "Extract the review form dimensions and rating scales used. Look for fields like \"Overall Score\", \"Soundness\", \"Presentation\", \"Contribution\", \"Confidence\" and their numeric scales. List each dimension with its scale and the reviewer's rating."
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-24T07:06:35.435626+00:00_

# Review Form Information Not Available

The provided webpage content does not contain review form dimensions, rating scales, or reviewer ratings. The page displays metadata about the "Body Transformer" paper published at CoRL 2024, including authors, abstract, and resource links, but does not include the actual peer review information.

To find review details, you would need to access the full review section of the OpenReview page, which would typically show fields like Overall Score, Soundness, Presentation, Contribution, and Confidence along with their respective rating scales and individual reviewer assessments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 2458
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-24T07:06:43.427216+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2021.corl.org/reviewer-information/instructions-for-reviewers",
  "prompt": "Extract ALL review form dimensions, rating scales (numeric), and scoring rubrics. Include every dimension name, its scale (e.g., 1-5, 1-10), and what each number means. I need the complete review form specification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2021.corl.org/reviewer-information/instructions-for-reviewers",
    "prompt": "Extract ALL review form dimensions, rating scales (numeric), and scoring rubrics. Include every dimension name, its scale (e.g., 1-5, 1-10), and what each number means. I need the complete review form specification."
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-24T07:06:46.327250+00:00_

# Review Form Specification Not Provided

The webpage content shared contains only **timeline and procedural instructions** for CoRL 2021 reviewers. It does not include the actual review form dimensions, rating scales, or scoring rubrics.

The document specifies reviewer responsibilities and deadlines (e.g., "1-23 Jul - Review period") but does not detail:

- Specific evaluation criteria or dimensions
- Numeric rating scales (1-5, 1-10, etc.)
- Definitions for each score point
- Rubric descriptions

To obtain the complete review form specification, you would need to access the actual review interface on OpenReview or contact the conference organizers at the provided email: **info@robot-learning.org**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 2900
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-24T07:11:51.208333+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Round 3 审稿报告 — Reviewer 1（方法严谨性 + 实验充分性）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026\n\n---\n\n## 总体评分\n\n**方法严谨性**: 7/10\n**一句话总结**: 论文在 Round 1 后有实质性改进——统计语言适度弱化、LOEO 交叉验证增加了可信度、五环境扩展提供了 discriminative validity——但 CIVO 仅在 2 个运动任务中复现、训练步数不对等未显式讨论、TAWM 对比仍无实证，这些残留问题将方法严谨性限制在\"solid but not exceptional\"层面。\n\n## 官方维度打分（基于 CoRL review form: Originality / Quality / Clarity / Significance / Relevance / Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/5 | 首个系统性诊断 DreamerV3 变速想象失败模式的工作；CIVO 现象的识别和四级干预层级分析均为新贡献 |\n| Quality | 3/5 | Factorial design 严谨、LOEO 验证有力，但 CIVO 仅在 2/5 环境复现、per-intervention 样本量小（2-7 seeds）、detector 仅 5 个正例 |\n| Clarity | 4/5 | 写作清晰、F1-F7 结构化叙事好；primary/secondary comparison 标注明确；33 页 appendix 非常详尽 |\n| Significance | 3/5 | 对想象式 RL 社区有价值的 negative result，但 locomotion-specific 的结论限制了 impact |\n| Relevance | 4/5 | 直接关联 robot control 中的 world-model RL；temporal abstraction 是 CoRL 核心话题 |\n| Limitations | 4/5 | Limitations section 诚实全面（承认 4 seeds 局限、architecture 局限、reward scale 局限），ManiSkill non-CIVO 结果如实报告 |\n\n---\n\n## 逐条 Issue 检查\n\n### 1. R1-N1 [critical, in_progress]: 统计检验力不足\n**[RESOLVED]**\n\n改进清单：\n- Seeds 从 2-3 增至 4（关键配置），Section 4.2 报告 IQM 175.2, mean 170.6, n=4（citing Agarwal et al. 2021）\n- 因果语言全面弱化：Abstract 和 Conclusion 统一使用 \"strongest predictor\" 而非 \"causal factor\"\n- NVE 阈值验证：26/29 accuracy, AUROC=0.953 (in-sample), LOEO cross-validated mean AUROC=0.981（Appendix Table B.4）\n- Bootstrap CI：ROC 曲线配 95% bootstrap CI (10,000 resamples)（Appendix Figure 3）\n- Limitations 显式承认：\"Statistical power with 4 seeds per configuration is limited; the NVE threshold (LOEO AUROC=0.981) may require recalibration for different reward scales\"\n\n**残留小问题**: Abstract 仍用 \"isolate\" 一词（\"Factorial diagnostics...isolate trained temporal embedding\"），该词携带近因果含义。建议改为 \"identify...as the strongest predictor\" 以保持全文一致。但这不影响接收决定。\n\n---\n\n### 2. R1-N4 [critical, in_progress]: 单环境局限\n**[RESOLVED]，附重要说明**\n\n改进：\n- 从 1 环境扩展到 5 环境：Walker Walk（primary factorial）、Cheetah Run（severity probe, NVE 8-70×）、PickCube-v1、StackCube-v1、PegInsertionSide-v1\n- ManiSkill 结果诚实报告为 non-CIVO：frozen control 匹配 trained spikes（StackCube frozen 4.30× vs trained 5.05×），PegInsertion seed-dependent ordering\n- Cross-domain Table 1 + Appendix Table 4 提供完整跨环境数据\n\n**重要说明**: CIVO 被证实为 locomotion-specific（仅 Walker Walk + Cheetah Run），ManiSkill 3 个任务均未展现 dt-embedding-dependent CIVO。论文诚实地陈述了这一点（Section 4.3: \"CIVO is locomotion-specific in DreamerV3\"），且 ManiSkill 结果提供了重要的 discriminative validity（NVE 诊断能正确区分 CIVO 与环境特异性 transient）。\n\n标题使用 \"Can Fail\" 的措辞是恰当的。但论文应更突出讨论**为什么**运动任务触发 CIVO 而操作任务不触发——当前解释仅在 Appendix D.3 中简要提及 \"representational capacity already partially consumed when CIVO injects\"，不够深入。\n\n---\n\n### 3. R1-W1 [warning, in_progress]: Factorial design 混淆变量\n**[RESOLVED]**\n\n- Section 4.2 明确标注 primary comparison（008d vs 008f，仅 embedding 因素不同）vs secondary comparisons（008a/008c 同时改变 subsample 和 horizon）\n- 2×2 factorial grid 隐式完整：{trained, no-emb} × {sub-ON, sub-OFF} = {008d(CIVO), 008a(healthy), 008f(healthy), 001(healthy)}，仅 (trained, sub-ON) 单元触发 CIVO\n- 论文正确推断 \"jointly sufficient in tested configurations\"\n\n---\n\n### 4. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 训练步数不对等\n**[STILL_OPEN]**\n\n**已改善之处**:\n- Table 1 报告 baseline 在 105K 时的 eval（915.7），与 treatment 在相同训练步数比较——这确保了 matched-timestep comparison\n- 1/4 Walker seeds 展示 self-correction（29.3% of baseline by 105K）\n\n**仍然存在的问题**:\n1. 论文**未显式讨论**步数不对等问题。Section 3.8 仅说 \"treatments run for 105K steps, sufficient to observe collapse onset\"，但未论证**为什么** 105K 足够——尤其当 1/4 seeds 展示 self-correction trajectory 时\n2. Director 提到的 exp_045 延长到 300K 的 treatment 数据**未在正文中呈现**或讨论。如果存在这样的数据，应至少在 Appendix 中报告 treatment 长跑结果\n3. Cheetah Run frozen (046) 运行到 215K，PickCube 到 200K——说明作者有能力运行更长实验。为什么 Walker 的 treatment 不延长？\n4. Figure 5 (Appendix C.2) 显示 performance 随 dt 单调下降，但 x 轴止于 105K。如果 self-correction 在更长时间窗口内更普遍，则 \"all variable-rate configurations degrade\" (F1) 可能过强\n\n**建议**: 在 Discussion 或 Appendix 中增加一段明确说明：(a) comparison 在 matched 105K 步数进行；(b) 已知 1/4 seeds self-correct 但 3/4 不在 105K 内恢复；(c) 如有 exp_045 长跑数据，报告之。\n\n---\n\n### 5. R1-W3 [warning, open]: Pathway B 解释不充分\n**[RESOLVED]**\n\n- 证据从 1 seed 增至 2 seeds\n- Section 4.6 措辞为 \"preliminary Pathway B (entropy increase, nve = 3.78×; 2 seeds only, requires confirmation)\"\n- \"requires confirmation\" 的声明力度与 2 seeds 的证据量匹配\n- Appendix D.6 提供了 Pathway B 的 entropy dynamics 对比（Figure 10）\n\n---\n\n### 6. R2-W1 [warning, open]: TAWM 对比无实证\n**[STILL_OPEN]**\n\n- 论文的 MPC vs imagination-based 论证仍为纯架构/理论分析：Section 5 (\"The feedback architecture—MPC re-planning versus imagination-based bootstrapping—is the structural factor\") 和 Conclusion 重复此 claim\n- **无实证数据**对比 TAWM、TD-MPC2 或其他 MPC 方法在相同环境下的表现\n- Limitations 承认 \"whether CIVO manifests in other imagination-based architectures (e.g., IRIS or latent-space planners beyond TD-MPC2) remains open\"，但这仅覆盖了其他 imagination-based 方法，未覆盖 MPC 方法的实证\n- Related Work (Section 2) 引用了 TD-MPC2 [11] 和 MBPO [27]，但仅做 architectural reasoning\n\n**严谨性影响**: \"feedback architecture as the structural factor\" 这一核心论断无实验支撑。论文声称 MPC re-planning 避免了 CIVO 是基于推理而非数据。这是一个合理的假说，但不应作为 \"the structural factor\" 呈现。\n\n**建议**: (a) 弱化措辞为 \"hypothesized structural factor\" 或 \"we conjecture that feedback architecture is the key differentiator\"；或 (b) 在 at least 1 MPC baseline (e.g., vanilla TD-MPC2 with dt-conditioning) 上验证无 CIVO。\n\n---\n\n### 7. R1-W4 [warning, resolved in R1]: RSSM signed reward error\n**[RESOLVED]**\n\n- Appendix D.1 / Table 15 提供完整的 signed reward error 分析\n- 结论：trained-embedding model 在 dt=2 时**低估**奖励（mean signed error = -0.150, 仅 8% 样本过预测），排除了 observation-level reward overprediction 作为 CIVO 机制\n- 方法学正确：在 posterior-conditioned RSSM predictions 上计算，isolate 了 reward head 的 prediction bias\n\n---\n\n## 新发现的问题\n\n### N-new-1 [warning]: Online CIVO Detector 评估样本量不足\n- **位置**: Section 4.7, Appendix F\n- **问题**: Detector 在 n=14 runs 上评估，仅 5 个正例（TPR=5/5）。任何单个漏检就会将 TPR 降至 80%。FPR=2/9 (22%) 意味着近 1/4 的非 CIVO 配置被误报。论文称 \"achieves 100% sensitivity\" 在 n=5 的基础上统计意义有限\n- **与 NVE 分类的区别**: NVE 阈值分类用了 n=29 configs（AUROC=0.953），这是合理的。但 online detector 的 streaming 评估仅 14 runs，应与 NVE 静态分类的统计效力区分讨论\n- **建议**: 承认 detector 评估的 small-sample limitation，或在更多配置上运行 retrospective 验证\n\n### N-new-2 [minor]: IQM 报告不完整\n- **位置**: Section 4.2\n- **问题**: 仅对一个配置报告 IQM (175.2, n=4)。既然 cite Agarwal et al. 2021 作为统计最佳实践，其他关键 comparison（如 008f control, frozen variants, Cheetah runs）也应报告 IQM + stratified bootstrap CI\n- **影响**: 不影响接收决定，但如果声称遵循 Agarwal et al. best practices，应更一致地应用\n\n### N-new-3 [minor]: Dual-critic convergence 的因果推理存在跳跃\n- **位置**: Section 4.8\n- **问题**: 论文从 ρ > 0.999 推导出 \"rendering Double Q pessimism ineffective\"。逻辑链是：identical training data → critic convergence → no pessimism gap → min operation ineffective。但 ρ > 0.999 是在 converged critics 上测量的——early training 时 critics 可能有差异。论文在 Appendix G 分析了 recovery mechanism（\"min operation reduces both peak CIVO severity\"），说明 min 操作确实在某些 seed 有效（3/4 wide dual-critic CIVO prevention）。这与 \"pessimism ineffective\" 的叙事有张力\n- **论文部分地址了这个问题**: Appendix G.3 区分了 recovery（min-dominated）和 prevention（min + capacity synergy），并承认 \"the mechanism for this synergy is an open question\"。但主文 Section 4.8 的 framing 过于简化\n- **建议**: 在主文中 nuance：ρ > 0.999 convergence 是 asymptotic 结果；early training 时的 brief divergence 可能足以让 min operation 发挥作用，这解释了 wide dual-critic 的部分成功\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n无新增 critical 问题。Round 1 的两个 critical issues (N1, N4) 均已实质性解决。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**S1**: 训练步数不对等未显式讨论（R1-W2, [STILL_OPEN]）——论文应在正文中明确说明 matched-timestep comparison 和 self-correction 现象\n\n**S2**: TAWM/MPC 对比仍无实证（R2-W1, [STILL_OPEN]）——\"the structural factor\" 措辞应弱化或增加实验验证\n\n**S3**: Online detector 评估的 small-sample limitation 应被承认（N-new-1）\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 中 \"isolate\" 应改为 \"identify...as\" 以与全文 \"strongest predictor\" 措辞一致\n- IQM 报告应更一致地应用于多个关键配置（N-new-2）\n- Dual-critic convergence 的主文叙事应增加 nuance 关于 early-training divergence（N-new-3）\n\n---\n\n## 主要优势\n\n1. **Factorial design 系统且严谨**: 43 配置 × 4 seeds × 5 环境的设计空间覆盖广泛；primary/secondary comparison 标注清晰\n2. **LOEO 交叉验证显著增强统计可信度**: AUROC=0.953 (in-sample), 0.981 (LOEO) 在 29 配置上表现出色\n3. **四级干预层级分析**（gradient/output/repr/arch）提供了系统性的 negative result，对社区有长期价值\n4. **ManiSkill non-CIVO 结果增加了 discriminative validity**: NVE 诊断能正确区分 dt-embedding-dependent CIVO 与环境特异性 transient\n5. **Dual-critic convergence (ρ > 0.999)** 是关于 imagination-based training 的有价值的 structural insight\n6. **Limitations section 诚实全面**: 主动承认 4-seed 局限、architecture 局限、ManiSkill locomotion-specificity\n\n---\n\n## Issue 状态汇总\n\n| Issue | 状态 | 理由 |\n|-------|------|------|\n| R1-N1 统计检验力 | [RESOLVED] | 4 seeds, \"strongest predictor\" 语言, LOEO AUROC=0.981, IQM 报告 |\n| R1-N4 单环境 | [RESOLVED] | 5 环境, CIVO locomotion-specificity 诚实报告, discriminative validity |\n| R1-W1 Factorial 混淆 | [RESOLVED] | Primary vs secondary 明确标注, 2×2 grid 完整 |\n| R1-W2 步数不对等 | [STILL_OPEN] | Matched-timestep 比较存在但未显式讨论; 缺少 treatment 长跑数据 |\n| R1-W3 Pathway B | [RESOLVED] | 2 seeds + \"preliminary/requires confirmation\" 措辞 |\n| R2-W1 TAWM 对比 | [STILL_OPEN] | 仍为纯 architectural reasoning, \"structural factor\" 措辞过强 |\n| R1-W4 Signed error | [RESOLVED] | Appendix D.1 / Table 15 完整呈现 |\n\n**5/7 issues resolved, 2/7 still open (均为 warning 级别，非 critical)**\n\n---\n\n## 方法严谨性总评\n\n**评分: 7/10**\n\n论文在 Round 1 后取得了显著进步。核心 factorial design 严谨，LOEO 交叉验证有效提升了统计论证质量，五环境扩展提供了正面和反面证据。两个残留 warning 级问题（步数不对等讨论不足 + TAWM 对比缺实证）不构成 fatal flaw，但将方法论评分限制在 7 而非 8。\n\n作为 diagnostic/negative-result paper，这是一个 solid 的工作——它不需要解决 CIVO，只需正确识别和表征它。论文在这方面做得好。主要限制是 CIVO 的 locomotion-specificity 收窄了 impact，以及 \"structural factor\" 论断缺乏跨架构实验验证。\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Round 3 审稿报告 — Reviewer 1（方法严谨性 + 实验充分性）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026\n\n---\n\n## 总体评分\n\n**方法严谨性**: 7/10\n**一句话总结**: 论文在 Round 1 后有实质性改进——统计语言适度弱化、LOEO 交叉验证增加了可信度、五环境扩展提供了 discriminative validity——但 CIVO 仅在 2 个运动任务中复现、训练步数不对等未显式讨论、TAWM 对比仍无实证，这些残留问题将方法严谨性限制在\"solid but not exceptional\"层面。\n\n## 官方维度打分（基于 CoRL review form: Originality / Quality / Clarity / Significance / Relevance / Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/5 | 首个系统性诊断 DreamerV3 变速想象失败模式的工作；CIVO 现象的识别和四级干预层级分析均为新贡献 |\n| Quality | 3/5 | Factorial design 严谨、LOEO 验证有力，但 CIVO 仅在 2/5 环境复现、per-intervention 样本量小（2-7 seeds）、detector 仅 5 个正例 |\n| Clarity | 4/5 | 写作清晰、F1-F7 结构化叙事好；primary/secondary comparison 标注明确；33 页 appendix 非常详尽 |\n| Significance | 3/5 | 对想象式 RL 社区有价值的 negative result，但 locomotion-specific 的结论限制了 impact |\n| Relevance | 4/5 | 直接关联 robot control 中的 world-model RL；temporal abstraction 是 CoRL 核心话题 |\n| Limitations | 4/5 | Limitations section 诚实全面（承认 4 seeds 局限、architecture 局限、reward scale 局限），ManiSkill non-CIVO 结果如实报告 |\n\n---\n\n## 逐条 Issue 检查\n\n### 1. R1-N1 [critical, in_progress]: 统计检验力不足\n**[RESOLVED]**\n\n改进清单：\n- Seeds 从 2-3 增至 4（关键配置），Section 4.2 报告 IQM 175.2, mean 170.6, n=4（citing Agarwal et al. 2021）\n- 因果语言全面弱化：Abstract 和 Conclusion 统一使用 \"strongest predictor\" 而非 \"causal factor\"\n- NVE 阈值验证：26/29 accuracy, AUROC=0.953 (in-sample), LOEO cross-validated mean AUROC=0.981（Appendix Table B.4）\n- Bootstrap CI：ROC 曲线配 95% bootstrap CI (10,000 resamples)（Appendix Figure 3）\n- Limitations 显式承认：\"Statistical power with 4 seeds per configuration is limited; the NVE threshold (LOEO AUROC=0.981) may require recalibration for different reward scales\"\n\n**残留小问题**: Abstract 仍用 \"isolate\" 一词（\"Factorial diagnostics...isolate trained temporal embedding\"），该词携带近因果含义。建议改为 \"identify...as the strongest predictor\" 以保持全文一致。但这不影响接收决定。\n\n---\n\n### 2. R1-N4 [critical, in_progress]: 单环境局限\n**[RESOLVED]，附重要说明**\n\n改进：\n- 从 1 环境扩展到 5 环境：Walker Walk（primary factorial）、Cheetah Run（severity probe, NVE 8-70×）、PickCube-v1、StackCube-v1、PegInsertionSide-v1\n- ManiSkill 结果诚实报告为 non-CIVO：frozen control 匹配 trained spikes（StackCube frozen 4.30× vs trained 5.05×），PegInsertion seed-dependent ordering\n- Cross-domain Table 1 + Appendix Table 4 提供完整跨环境数据\n\n**重要说明**: CIVO 被证实为 locomotion-specific（仅 Walker Walk + Cheetah Run），ManiSkill 3 个任务均未展现 dt-embedding-dependent CIVO。论文诚实地陈述了这一点（Section 4.3: \"CIVO is locomotion-specific in DreamerV3\"），且 ManiSkill 结果提供了重要的 discriminative validity（NVE 诊断能正确区分 CIVO 与环境特异性 transient）。\n\n标题使用 \"Can Fail\" 的措辞是恰当的。但论文应更突出讨论**为什么**运动任务触发 CIVO 而操作任务不触发——当前解释仅在 Appendix D.3 中简要提及 \"representational capacity already partially consumed when CIVO injects\"，不够深入。\n\n---\n\n### 3. R1-W1 [warning, in_progress]: Factorial design 混淆变量\n**[RESOLVED]**\n\n- Section 4.2 明确标注 primary comparison（008d vs 008f，仅 embedding 因素不同）vs secondary comparisons（008a/008c 同时改变 subsample 和 horizon）\n- 2×2 factorial grid 隐式完整：{trained, no-emb} × {sub-ON, sub-OFF} = {008d(CIVO), 008a(healthy), 008f(healthy), 001(healthy)}，仅 (trained, sub-ON) 单元触发 CIVO\n- 论文正确推断 \"jointly sufficient in tested configurations\"\n\n---\n\n### 4. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 训练步数不对等\n**[STILL_OPEN]**\n\n**已改善之处**:\n- Table 1 报告 baseline 在 105K 时的 eval（915.7），与 treatment 在相同训练步数比较——这确保了 matched-timestep comparison\n- 1/4 Walker seeds 展示 self-correction（29.3% of baseline by 105K）\n\n**仍然存在的问题**:\n1. 论文**未显式讨论**步数不对等问题。Section 3.8 仅说 \"treatments run for 105K steps, sufficient to observe collapse onset\"，但未论证**为什么** 105K 足够——尤其当 1/4 seeds 展示 self-correction trajectory 时\n2. Director 提到的 exp_045 延长到 300K 的 treatment 数据**未在正文中呈现**或讨论。如果存在这样的数据，应至少在 Appendix 中报告 treatment 长跑结果\n3. Cheetah Run frozen (046) 运行到 215K，PickCube 到 200K——说明作者有能力运行更长实验。为什么 Walker 的 treatment 不延长？\n4. Figure 5 (Appendix C.2) 显示 performance 随 dt 单调下降，但 x 轴止于 105K。如果 self-correction 在更长时间窗口内更普遍，则 \"all variable-rate configurations degrade\" (F1) 可能过强\n\n**建议**: 在 Discussion 或 Appendix 中增加一段明确说明：(a) comparison 在 matched 105K 步数进行；(b) 已知 1/4 seeds self-correct 但 3/4 不在 105K 内恢复；(c) 如有 exp_045 长跑数据，报告之。\n\n---\n\n### 5. R1-W3 [warning, open]: Pathway B 解释不充分\n**[RESOLVED]**\n\n- 证据从 1 seed 增至 2 seeds\n- Section 4.6 措辞为 \"preliminary Pathway B (entropy increase, nve = 3.78×; 2 seeds only, requires confirmation)\"\n- \"requires confirmation\" 的声明力度与 2 seeds 的证据量匹配\n- Appendix D.6 提供了 Pathway B 的 entropy dynamics 对比（Figure 10）\n\n---\n\n### 6. R2-W1 [warning, open]: TAWM 对比无实证\n**[STILL_OPEN]**\n\n- 论文的 MPC vs imagination-based 论证仍为纯架构/理论分析：Section 5 (\"The feedback architecture—MPC re-planning versus imagination-based bootstrapping—is the structural factor\") 和 Conclusion 重复此 claim\n- **无实证数据**对比 TAWM、TD-MPC2 或其他 MPC 方法在相同环境下的表现\n- Limitations 承认 \"whether CIVO manifests in other imagination-based architectures (e.g., IRIS or latent-space planners beyond TD-MPC2) remains open\"，但这仅覆盖了其他 imagination-based 方法，未覆盖 MPC 方法的实证\n- Related Work (Section 2) 引用了 TD-MPC2 [11] 和 MBPO [27]，但仅做 architectural reasoning\n\n**严谨性影响**: \"feedback architecture as the structural factor\" 这一核心论断无实验支撑。论文声称 MPC re-planning 避免了 CIVO 是基于推理而非数据。这是一个合理的假说，但不应作为 \"the structural factor\" 呈现。\n\n**建议**: (a) 弱化措辞为 \"hypothesized structural factor\" 或 \"we conjecture that feedback architecture is the key differentiator\"；或 (b) 在 at least 1 MPC baseline (e.g., vanilla TD-MPC2 with dt-conditioning) 上验证无 CIVO。\n\n---\n\n### 7. R1-W4 [warning, resolved in R1]: RSSM signed reward error\n**[RESOLVED]**\n\n- Appendix D.1 / Table 15 提供完整的 signed reward error 分析\n- 结论：trained-embedding model 在 dt=2 时**低估**奖励（mean signed error = -0.150, 仅 8% 样本过预测），排除了 observation-level reward overprediction 作为 CIVO 机制\n- 方法学正确：在 posterior-conditioned RSSM predictions 上计算，isolate 了 reward head 的 prediction bias\n\n---\n\n## 新发现的问题\n\n### N-new-1 [warning]: Online CIVO Detector 评估样本量不足\n- **位置**: Section 4.7, Appendix F\n- **问题**: Detector 在 n=14 runs 上评估，仅 5 个正例（TPR=5/5）。任何单个漏检就会将 TPR 降至 80%。FPR=2/9 (22%) 意味着近 1/4 的非 CIVO 配置被误报。论文称 \"achieves 100% sensitivity\" 在 n=5 的基础上统计意义有限\n- **与 NVE 分类的区别**: NVE 阈值分类用了 n=29 configs（AUROC=0.953），这是合理的。但 online detector 的 streaming 评估仅 14 runs，应与 NVE 静态分类的统计效力区分讨论\n- **建议**: 承认 detector 评估的 small-sample limitation，或在更多配置上运行 retrospective 验证\n\n### N-new-2 [minor]: IQM 报告不完整\n- **位置**: Section 4.2\n- **问题**: 仅对一个配置报告 IQM (175.2, n=4)。既然 cite Agarwal et al. 2021 作为统计最佳实践，其他关键 comparison（如 008f control, frozen variants, Cheetah runs）也应报告 IQM + stratified bootstrap CI\n- **影响**: 不影响接收决定，但如果声称遵循 Agarwal et al. best practices，应更一致地应用\n\n### N-new-3 [minor]: Dual-critic convergence 的因果推理存在跳跃\n- **位置**: Section 4.8\n- **问题**: 论文从 ρ > 0.999 推导出 \"rendering Double Q pessimism ineffective\"。逻辑链是：identical training data → critic convergence → no pessimism gap → min operation ineffective。但 ρ > 0.999 是在 converged critics 上测量的——early training 时 critics 可能有差异。论文在 Appendix G 分析了 recovery mechanism（\"min operation reduces both peak CIVO severity\"），说明 min 操作确实在某些 seed 有效（3/4 wide dual-critic CIVO prevention）。这与 \"pessimism ineffective\" 的叙事有张力\n- **论文部分地址了这个问题**: Appendix G.3 区分了 recovery（min-dominated）和 prevention（min + capacity synergy），并承认 \"the mechanism for this synergy is an open question\"。但主文 Section 4.8 的 framing 过于简化\n- **建议**: 在主文中 nuance：ρ > 0.999 convergence 是 asymptotic 结果；early training 时的 brief divergence 可能足以让 min operation 发挥作用，这解释了 wide dual-critic 的部分成功\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n无新增 critical 问题。Round 1 的两个 critical issues (N1, N4) 均已实质性解决。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**S1**: 训练步数不对等未显式讨论（R1-W2, [STILL_OPEN]）——论文应在正文中明确说明 matched-timestep comparison 和 self-correction 现象\n\n**S2**: TAWM/MPC 对比仍无实证（R2-W1, [STILL_OPEN]）——\"the structural factor\" 措辞应弱化或增加实验验证\n\n**S3**: Online detector 评估的 small-sample limitation 应被承认（N-new-1）\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 中 \"isolate\" 应改为 \"identify...as\" 以与全文 \"strongest predictor\" 措辞一致\n- IQM 报告应更一致地应用于多个关键配置（N-new-2）\n- Dual-critic convergence 的主文叙事应增加 nuance 关于 early-training divergence（N-new-3）\n\n---\n\n## 主要优势\n\n1. **Factorial design 系统且严谨**: 43 配置 × 4 seeds × 5 环境的设计空间覆盖广泛；primary/secondary comparison 标注清晰\n2. **LOEO 交叉验证显著增强统计可信度**: AUROC=0.953 (in-sample), 0.981 (LOEO) 在 29 配置上表现出色\n3. **四级干预层级分析**（gradient/output/repr/arch）提供了系统性的 negative result，对社区有长期价值\n4. **ManiSkill non-CIVO 结果增加了 discriminative validity**: NVE 诊断能正确区分 dt-embedding-dependent CIVO 与环境特异性 transient\n5. **Dual-critic convergence (ρ > 0.999)** 是关于 imagination-based training 的有价值的 structural insight\n6. **Limitations section 诚实全面**: 主动承认 4-seed 局限、architecture 局限、ManiSkill locomotion-specificity\n\n---\n\n## Issue 状态汇总\n\n| Issue | 状态 | 理由 |\n|-------|------|------|\n| R1-N1 统计检验力 | [RESOLVED] | 4 seeds, \"strongest predictor\" 语言, LOEO AUROC=0.981, IQM 报告 |\n| R1-N4 单环境 | [RESOLVED] | 5 环境, CIVO locomotion-specificity 诚实报告, discriminative validity |\n| R1-W1 Factorial 混淆 | [RESOLVED] | Primary vs secondary 明确标注, 2×2 grid 完整 |\n| R1-W2 步数不对等 | [STILL_OPEN] | Matched-timestep 比较存在但未显式讨论; 缺少 treatment 长跑数据 |\n| R1-W3 Pathway B | [RESOLVED] | 2 seeds + \"preliminary/requires confirmation\" 措辞 |\n| R2-W1 TAWM 对比 | [STILL_OPEN] | 仍为纯 architectural reasoning, \"structural factor\" 措辞过强 |\n| R1-W4 Signed error | [RESOLVED] | Appendix D.1 / Table 15 完整呈现 |\n\n**5/7 issues resolved, 2/7 still open (均为 warning 级别，非 critical)**\n\n---\n\n## 方法严谨性总评\n\n**评分: 7/10**\n\n论文在 Round 1 后取得了显著进步。核心 factorial design 严谨，LOEO 交叉验证有效提升了统计论证质量，五环境扩展提供了正面和反面证据。两个残留 warning 级问题（步数不对等讨论不足 + TAWM 对比缺实证）不构成 fatal flaw，但将方法论评分限制在 7 而非 8。\n\n作为 diagnostic/negative-result paper，这是一个 solid 的工作——它不需要解决 CIVO，只需正确识别和表征它。论文在这方面做得好。主要限制是 CIVO 的 locomotion-specificity 收窄了 impact，以及 \"structural factor\" 论断缺乏跨架构实验验证。\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-24T07:11:55.075838+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3867
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-24T07:11:58.498901+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
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

_source line 165 · 2026-05-24T07:11:58.549774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-24T07:12:02.416785+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-24T07:12:02.467482+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 168 · 2026-05-24T07:12:11.665308+00:00_

Round 3 审稿报告已提交给 Review Director。

核心结论：**7/10 方法严谨性**，5/7 issues resolved，2 个 warning 级问题仍 open：

1. **R1-W2 步数不对等** — 105K vs 505K 的 matched-timestep comparison 存在但未显式讨论，缺少 treatment 长跑数据
2. **R2-W1 TAWM 对比** — "feedback architecture as the structural factor" 仍无实证，仅 architectural reasoning

两个 Round 1 critical issues（统计检验力 N1、单环境 N4）均已实质性解决。新发现 3 个额外问题（online detector 小样本、IQM 报告不完整、dual-critic convergence 叙事过简），均为 warning 或 minor 级别。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 4

4 recorded events

### User

_source line 169 · 2026-05-24T07:12:56.116851+00:00_

[Round 3 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的意见

以下是 Reviewer 2（Venue Fit / 贡献度 / 写作质量）的完整审稿意见。请对每个要点标注 `[AGREE]`（同意并说明理由）或 `[REBUT]`（反驳并引用论文具体 Section/Table/Figure 作为证据）。

---

**Reviewer 2 完整审稿意见：**

### 1. R1-N3 [STILL_OPEN]: CoRL venue fit 不足
R2 认为改善明显但有结构性问题：
- ManiSkill 结果**反向证明** CIVO 与 robotics manipulation 无关（所有 3 个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO）
- Robotics framing 是 "bookend" 式的（集中在 Intro 前两句和 Discussion 一段，中间 4 页纯 RL 分析）
- CoRL CFP 要求 "focus on core robotics problems"，CIVO 是通用 RL 问题
- Desk reject 风险降低但未消除
- **评分：Venue Fit 5/10**

### 2. R2-N3 [STILL_OPEN]: 纯诊断缺乏 actionable solution
R2 认为有改善但贡献模式偏弱：
- Table 2 核心结论仍是 "No level reliably eliminates CIVO across environments"
- 最有效 "solution" 是 embedding removed (100%) = 不使用该功能
- Frozen embedding 71% prevention rate 但 eval 仍差
- Wide dual critic 75% Walker 但 Cheetah 0/1
- 对 CoRL deployment-oriented 社区价值有限
- **评分：贡献度 6/10**

### 3. R2-W3 [RESOLVED]: CIVO 与 compounding error 区分
R2 认为 Related Work 提供了清晰的经验性区分，数据支撑充分。

### 4. R2-W4/R3-W3 [PARTIALLY RESOLVED]: Related Work/Bib
R2 发现 Becker-Ehmck 2023 仍未引用。其他 3 篇（Park, Wang, Colas）已引用。Bib 从 77 条清理至 44 条。

### 5. R3-W2 [RESOLVED]: Abstract 过长缺 robotics
R2 确认约 150 词，robotics motivation 到位，88.9% accuracy 已替换。

### 6-7. R3-N1, R3-N3 [RESOLVED]: 模板和页数。

### R2 额外发现：
- **E1** [minor]: Abstract 统计数据过密（6+ 数字指标）
- **E2** [minor]: Section 标题 F1-F7 与标准编号混用
- **E3** [minor]: Limitations 作为 Conclusion paragraph 是否满足 CoRL 要求
- **N1** [warning]: ManiSkill 实验的 baseline eval 值缺失
- **N2** [warning]: Cheetah Run baseline 同样缺失
- **N3** [minor]: Table 2 中 1-seed 条目（TCN σ=0.1, σ=1.0）统计无意义

### R2 总评：
- Venue Fit 5/10, 贡献度 6/10, 写作质量 7/10
- 论文更适合 ICML/NeurIPS
- 核心矛盾：CIVO 是 locomotion-specific negative result，robotics framing 装饰性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-24T07:14:49.020110+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n## 1. R1-N3 [STILL_OPEN]: CoRL venue fit 不足\n\n**[REBUT] R2-Issue-N3**\n\nR2 的核心论点是 ManiSkill non-CIVO 结果反向证明 CIVO 与 robotics 无关。这一推理有逻辑跳跃：\n\n1. **Locomotion IS a core robotics problem.** Walker Walk 和 Cheetah Run 是标准的连续控制 benchmark，直接对应双足/四足机器人控制。CIVO 在运动任务中 100% 复现（6/6 seeds across 2 environments）对 robotics locomotion 社区有直接实践警示价值。\n\n2. **Temporal abstraction 是 CoRL 核心议题。** Variable-rate planning 对 real-robot deployment 至关重要（不同关节/层级需要不同控制频率）。论文诊断的是：为什么这一在 MPC 中有效的技术在 imagination-based actor-critic 中失败——这对准备在 DreamerV3 类系统中部署 temporal abstraction 的 robotics 团队有直接意义。\n\n3. **ManiSkill non-CIVO 不削弱而是增强论文价值。** 它提供了 discriminative validity——告诉读者 CIVO 在何时不需要担心。一个只报告 \"everywhere fails\" 的论文反而更可疑。\n\n4. **\"Bookend\" framing 的批评有一定道理**，但 Section 5 Discussion 的机制分析（MPC re-planning vs imagination bootstrapping, Section 5 paragraphs 1-3）和 online detector（Section 4.7）都是面向 deployment 的贡献，不仅仅是开头结尾提及 robotics。\n\n**但我部分同意 R2**: 论文中间确实有 ~3 页（Sections 4.2-4.5 的 factorial ablation 细节）是纯 RL 方法论分析，缺少 robotics grounding。如果作者能在 Section 4.3 的 ManiSkill 讨论中增加一段关于为什么 locomotion dynamics（contact-rich, periodic gait patterns）特别容易触发 CIVO 的机制讨论，venue fit 会更强。\n\n**我的评分**: Venue Fit 6.5/10（比 R2 的 5/10 高，但承认存在改善空间）。\n\n---\n\n## 2. R2-N3 [STILL_OPEN]: 纯诊断缺乏 actionable solution\n\n**[AGREE] R2-Issue-N3，但程度不同**\n\nR2 的观察在事实层面正确：Table 2 (Section 4.6) 核心结论确实是 \"No level reliably eliminates CIVO across environments\"，最有效方案是 embedding removed (100%) = 不用该功能。\n\n但我认为 R2 低估了三个 actionable 贡献：\n\n1. **NVE online detector**（Section 4.7, Algorithm 1 in Appendix F）是可直接部署的工具——TPR=5/5, FPR=2/9，虽然样本量小（我在 N-new-1 中已指出），但提供了实时监控 CIVO onset 的方法。\n\n2. **Min + increased capacity 实现 recovery**（Section 4.8, Appendix G）：wide dual-critic 在 Walker 上 3/4 prevention rate，narrow dual-critic 即使不 prevent 也能 recover（16-19× recovery ratio）。这是具体的架构建议，不只是 \"don't use it\"。\n\n3. **Frozen embedding 作为安全替代**（Table 1: 5/7 prevention rate, 71%）：虽然 eval 较差，但对需要 temporal conditioning 又不想触发 CIVO 的场景提供了中间方案。\n\n**综合看**: R2 说论文更适合 ICML/NeurIPS，这个建议有道理——diagnostic negative result 在方法论 venue 的 impact 更直接。但 CoRL 也接受 methodology 贡献，前提是 robotics relevance 清晰。问题不在于论文没有 actionable solution，而在于 actionable solution（NVE detector, min+capacity）的统计支撑较弱（小样本），且最强方案（wide dual-critic）不跨环境泛化（Cheetah 0/1）。\n\n**我的评分**: 贡献度 6.5/10（与 R2 的 6/10 接近）。\n\n---\n\n## 3. R2-W3 [RESOLVED]: CIVO 与 compounding error 区分\n\n**[AGREE] R2-W3**\n\n同意 R2 的 RESOLVED 判定。Section 2 (Related Work) 清晰区分了 CIVO 和 standard compounding error。Appendix D.1 的 signed reward error 分析（Table 15）提供了经验性证据：trained-embedding model 在 dt=2 时低估奖励（mean signed error = -0.150），排除了 observation-level overprediction。CIVO 的机制（value function internalization of reward prediction gap → positive feedback loop）与 compounding error（累积 model error）在 pathway 上有本质区别。\n\n---\n\n## 4. R2-W4/R3-W3 [PARTIALLY RESOLVED]: Becker-Ehmck 2023 缺失\n\n**[AGREE] R2-W4**\n\n如果 Becker-Ehmck 2023 确实涉及 temporal abstraction in model-based RL（如 \"Temporal Difference Learning for Model Predictive Control\" 或类似工作），且与论文的 variable-rate imagination mechanism 直接相关，则应被引用。Bib 从 77 条清理至 44 条是正确方向，但清理过程不应遗漏直接相关的工作。\n\n我无法独立验证该引用的具体内容，但 R2 连续两轮指出同一遗漏，说明这不是边缘情况。建议作者补充。\n\n---\n\n## 5. R3-W2 [RESOLVED]: Abstract\n\n**[AGREE] R2-R3-W2**\n\n确认 Abstract 约 150 词，包含 robotics motivation。\n\n---\n\n## 6-7. R3-N1, R3-N3: 模板和页数\n\n**[AGREE]**\n\n已确认使用 `\\usepackage{corl_2026}` 模板，8 页正文。\n\n---\n\n## 对 R2 额外发现的回应\n\n### E1 [minor]: Abstract 统计数据过密\n\n**[AGREE] R2-E1**\n\nAbstract 包含至少 6 个数值指标：14-19%, 26/29, AUROC=0.953, 2.78×, ρ > 0.999, 100%。对于 ~150 词的 abstract，数字密度确实过高，影响可读性。建议保留 2-3 个最关键的数字（如 AUROC=0.953 和 \"all variable-rate configurations degrade\"），其余移至正文。但这是写作偏好问题，不影响接收决定。\n\n### E2 [minor]: F1-F7 与标准编号混用\n\n**[REBUT] R2-E2**\n\nSection 编号为 4.1-4.8，F1-F7 是 findings 的逻辑编号。这在 findings-based diagnostic paper 中是合理的组织方式——类似于 empirical study 按 research question (RQ1-RQn) 组织 results section。Section 4.1 标题为 \"F1: All Variable-Rate Configurations Degrade\"，读者可以通过 section 编号 (4.1) 导航，也可以通过 finding 编号 (F1) 追踪论证链。两套编号不冲突。\n\n### E3 [minor]: Limitations 作为 Conclusion paragraph\n\n**[AGREE] R2-E3**\n\n从 LaTeX 源码确认：Limitations 是 Section 6 (Conclusion) 内的 `\\paragraph{Limitations.}`，而非独立 section。CoRL 2024/2025 的 submission guidelines 是否要求 standalone Limitations section 需要核实。如果 CoRL CFP 要求独立 Limitations section，当前格式不合规。即使不硬性要求，独立 section 也是更安全的选择。\n\n### N1 [warning]: ManiSkill baseline eval 缺失\n\n**[AGREE] R2-N1**\n\nTable 1 的 ManiSkill 条目（PickCube 019b, StackCube 049, PegInsertion 050）缺少对应的 vanilla DreamerV3 baseline 评分。虽然脚注 c 提到 \"NVE normalized against exp_019a_v2 (vanilla DreamerV3 on PickCube-v1)\"，但 019a_v2 的 eval 值未出现在 Table 1 中。读者无法直接判断 ManiSkill 上 treatment 的 degradation 程度。Cheetah Run baseline（010b 对应的 untreated baseline）同理。\n\n这是我在 Round 3 审查中未单独提出但确实存在的问题。Table 1 应补充 ManiSkill 和 Cheetah 的 baseline 行。\n\n### N2 [warning]: Cheetah Run baseline 缺失\n\n**[AGREE] R2-N2**\n\n同上。Table 1 仅包含 Cheetah treated (010b) 和 frozen (046)，无 untreated baseline 行。Table 3 (Appendix) 可能有，但主表应自足。\n\n### N3 [minor]: 1-seed 条目统计无意义\n\n**[AGREE] R2-N3**\n\nTable 2 中 TCN σ=0.1（1 seed, 1/1, 100%）和 TCN σ=1.0（1 seed, 1/1, 100%）的 prevention rate 在统计上无意义。我在 Round 3 审查中未专门提出此点，但 R2 的观察正确。这些条目要么应标注 \"n=1, exploratory\"，要么从 Table 2 移至 Appendix。Table 2 中保留 n≥2 的条目并注明 \"*single-seed pilot, not statistically interpretable*\" 是最低要求。\n\n---\n\n## 对 R2 总评的回应\n\n**Venue Fit 5/10**: 我给 6.5/10。R2 的 \"CIVO 与 robotics manipulation 无关\" 论点过强——locomotion 是 core robotics，temporal abstraction 直接关联 deployment。但 \"bookend\" framing 批评有效。\n\n**贡献度 6/10**: 我给 6.5/10。基本同意。NVE detector 和 min+capacity finding 提供了部分 actionable value，但整体贡献确实偏 diagnostic。\n\n**写作质量 7/10**: 同意。论文结构清晰但 abstract 数字过密、baseline 行缺失。\n\n**\"论文更适合 ICML/NeurIPS\"**: 这是一个合理但非决定性的观点。CoRL 历史上接受过 methodology-focused RL 论文（如 world model analysis、sim-to-real failure mode 研究）。关键在于作者是否能在 rebuttal 中加强 robotics grounding——如果能增加 1-2 段关于 locomotion-specific CIVO 的 robotics 机制讨论（为什么 gait patterns + contact dynamics 使 RSSM reward head 特别脆弱），venue fit 可以从 borderline 提升到 acceptable。\n\n**\"核心矛盾：CIVO 是 locomotion-specific negative result，robotics framing 装饰性\"**: 部分同意 framing 可以更深入，但 \"装饰性\" 一词过强。论文的核心发现（imagination-based bootstrapping vs MPC re-planning 的结构性差异）对 robotics deployment 决策有直接指导意义。\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n## 1. R1-N3 [STILL_OPEN]: CoRL venue fit 不足\n\n**[REBUT] R2-Issue-N3**\n\nR2 的核心论点是 ManiSkill non-CIVO 结果反向证明 CIVO 与 robotics 无关。这一推理有逻辑跳跃：\n\n1. **Locomotion IS a core robotics problem.** Walker Walk 和 Cheetah Run 是标准的连续控制 benchmark，直接对应双足/四足机器人控制。CIVO 在运动任务中 100% 复现（6/6 seeds across 2 environments）对 robotics locomotion 社区有直接实践警示价值。\n\n2. **Temporal abstraction 是 CoRL 核心议题。** Variable-rate planning 对 real-robot deployment 至关重要（不同关节/层级需要不同控制频率）。论文诊断的是：为什么这一在 MPC 中有效的技术在 imagination-based actor-critic 中失败——这对准备在 DreamerV3 类系统中部署 temporal abstraction 的 robotics 团队有直接意义。\n\n3. **ManiSkill non-CIVO 不削弱而是增强论文价值。** 它提供了 discriminative validity——告诉读者 CIVO 在何时不需要担心。一个只报告 \"everywhere fails\" 的论文反而更可疑。\n\n4. **\"Bookend\" framing 的批评有一定道理**，但 Section 5 Discussion 的机制分析（MPC re-planning vs imagination bootstrapping, Section 5 paragraphs 1-3）和 online detector（Section 4.7）都是面向 deployment 的贡献，不仅仅是开头结尾提及 robotics。\n\n**但我部分同意 R2**: 论文中间确实有 ~3 页（Sections 4.2-4.5 的 factorial ablation 细节）是纯 RL 方法论分析，缺少 robotics grounding。如果作者能在 Section 4.3 的 ManiSkill 讨论中增加一段关于为什么 locomotion dynamics（contact-rich, periodic gait patterns）特别容易触发 CIVO 的机制讨论，venue fit 会更强。\n\n**我的评分**: Venue Fit 6.5/10（比 R2 的 5/10 高，但承认存在改善空间）。\n\n---\n\n## 2. R2-N3 [STILL_OPEN]: 纯诊断缺乏 actionable solution\n\n**[AGREE] R2-Issue-N3，但程度不同**\n\nR2 的观察在事实层面正确：Table 2 (Section 4.6) 核心结论确实是 \"No level reliably eliminates CIVO across environments\"，最有效方案是 embedding removed (100%) = 不用该功能。\n\n但我认为 R2 低估了三个 actionable 贡献：\n\n1. **NVE online detector**（Section 4.7, Algorithm 1 in Appendix F）是可直接部署的工具——TPR=5/5, FPR=2/9，虽然样本量小（我在 N-new-1 中已指出），但提供了实时监控 CIVO onset 的方法。\n\n2. **Min + increased capacity 实现 recovery**（Section 4.8, Appendix G）：wide dual-critic 在 Walker 上 3/4 prevention rate，narrow dual-critic 即使不 prevent 也能 recover（16-19× recovery ratio）。这是具体的架构建议，不只是 \"don't use it\"。\n\n3. **Frozen embedding 作为安全替代**（Table 1: 5/7 prevention rate, 71%）：虽然 eval 较差，但对需要 temporal conditioning 又不想触发 CIVO 的场景提供了中间方案。\n\n**综合看**: R2 说论文更适合 ICML/NeurIPS，这个建议有道理——diagnostic negative result 在方法论 venue 的 impact 更直接。但 CoRL 也接受 methodology 贡献，前提是 robotics relevance 清晰。问题不在于论文没有 actionable solution，而在于 actionable solution（NVE detector, min+capacity）的统计支撑较弱（小样本），且最强方案（wide dual-critic）不跨环境泛化（Cheetah 0/1）。\n\n**我的评分**: 贡献度 6.5/10（与 R2 的 6/10 接近）。\n\n---\n\n## 3. R2-W3 [RESOLVED]: CIVO 与 compounding error 区分\n\n**[AGREE] R2-W3**\n\n同意 R2 的 RESOLVED 判定。Section 2 (Related Work) 清晰区分了 CIVO 和 standard compounding error。Appendix D.1 的 signed reward error 分析（Table 15）提供了经验性证据：trained-embedding model 在 dt=2 时低估奖励（mean signed error = -0.150），排除了 observation-level overprediction。CIVO 的机制（value function internalization of reward prediction gap → positive feedback loop）与 compounding error（累积 model error）在 pathway 上有本质区别。\n\n---\n\n## 4. R2-W4/R3-W3 [PARTIALLY RESOLVED]: Becker-Ehmck 2023 缺失\n\n**[AGREE] R2-W4**\n\n如果 Becker-Ehmck 2023 确实涉及 temporal abstraction in model-based RL（如 \"Temporal Difference Learning for Model Predictive Control\" 或类似工作），且与论文的 variable-rate imagination mechanism 直接相关，则应被引用。Bib 从 77 条清理至 44 条是正确方向，但清理过程不应遗漏直接相关的工作。\n\n我无法独立验证该引用的具体内容，但 R2 连续两轮指出同一遗漏，说明这不是边缘情况。建议作者补充。\n\n---\n\n## 5. R3-W2 [RESOLVED]: Abstract\n\n**[AGREE] R2-R3-W2**\n\n确认 Abstract 约 150 词，包含 robotics motivation。\n\n---\n\n## 6-7. R3-N1, R3-N3: 模板和页数\n\n**[AGREE]**\n\n已确认使用 `\\usepackage{corl_2026}` 模板，8 页正文。\n\n---\n\n## 对 R2 额外发现的回应\n\n### E1 [minor]: Abstract 统计数据过密\n\n**[AGREE] R2-E1**\n\nAbstract 包含至少 6 个数值指标：14-19%, 26/29, AUROC=0.953, 2.78×, ρ > 0.999, 100%。对于 ~150 词的 abstract，数字密度确实过高，影响可读性。建议保留 2-3 个最关键的数字（如 AUROC=0.953 和 \"all variable-rate configurations degrade\"），其余移至正文。但这是写作偏好问题，不影响接收决定。\n\n### E2 [minor]: F1-F7 与标准编号混用\n\n**[REBUT] R2-E2**\n\nSection 编号为 4.1-4.8，F1-F7 是 findings 的逻辑编号。这在 findings-based diagnostic paper 中是合理的组织方式——类似于 empirical study 按 research question (RQ1-RQn) 组织 results section。Section 4.1 标题为 \"F1: All Variable-Rate Configurations Degrade\"，读者可以通过 section 编号 (4.1) 导航，也可以通过 finding 编号 (F1) 追踪论证链。两套编号不冲突。\n\n### E3 [minor]: Limitations 作为 Conclusion paragraph\n\n**[AGREE] R2-E3**\n\n从 LaTeX 源码确认：Limitations 是 Section 6 (Conclusion) 内的 `\\paragraph{Limitations.}`，而非独立 section。CoRL 2024/2025 的 submission guidelines 是否要求 standalone Limitations section 需要核实。如果 CoRL CFP 要求独立 Limitations section，当前格式不合规。即使不硬性要求，独立 section 也是更安全的选择。\n\n### N1 [warning]: ManiSkill baseline eval 缺失\n\n**[AGREE] R2-N1**\n\nTable 1 的 ManiSkill 条目（PickCube 019b, StackCube 049, PegInsertion 050）缺少对应的 vanilla DreamerV3 baseline 评分。虽然脚注 c 提到 \"NVE normalized against exp_019a_v2 (vanilla DreamerV3 on PickCube-v1)\"，但 019a_v2 的 eval 值未出现在 Table 1 中。读者无法直接判断 ManiSkill 上 treatment 的 degradation 程度。Cheetah Run baseline（010b 对应的 untreated baseline）同理。\n\n这是我在 Round 3 审查中未单独提出但确实存在的问题。Table 1 应补充 ManiSkill 和 Cheetah 的 baseline 行。\n\n### N2 [warning]: Cheetah Run baseline 缺失\n\n**[AGREE] R2-N2**\n\n同上。Table 1 仅包含 Cheetah treated (010b) 和 frozen (046)，无 untreated baseline 行。Table 3 (Appendix) 可能有，但主表应自足。\n\n### N3 [minor]: 1-seed 条目统计无意义\n\n**[AGREE] R2-N3**\n\nTable 2 中 TCN σ=0.1（1 seed, 1/1, 100%）和 TCN σ=1.0（1 seed, 1/1, 100%）的 prevention rate 在统计上无意义。我在 Round 3 审查中未专门提出此点，但 R2 的观察正确。这些条目要么应标注 \"n=1, exploratory\"，要么从 Table 2 移至 Appendix。Table 2 中保留 n≥2 的条目并注明 \"*single-seed pilot, not statistically interpretable*\" 是最低要求。\n\n---\n\n## 对 R2 总评的回应\n\n**Venue Fit 5/10**: 我给 6.5/10。R2 的 \"CIVO 与 robotics manipulation 无关\" 论点过强——locomotion 是 core robotics，temporal abstraction 直接关联 deployment。但 \"bookend\" framing 批评有效。\n\n**贡献度 6/10**: 我给 6.5/10。基本同意。NVE detector 和 min+capacity finding 提供了部分 actionable value，但整体贡献确实偏 diagnostic。\n\n**写作质量 7/10**: 同意。论文结构清晰但 abstract 数字过密、baseline 行缺失。\n\n**\"论文更适合 ICML/NeurIPS\"**: 这是一个合理但非决定性的观点。CoRL 历史上接受过 methodology-focused RL 论文（如 world model analysis、sim-to-real failure mode 研究）。关键在于作者是否能在 rebuttal 中加强 robotics grounding——如果能增加 1-2 段关于 locomotion-specific CIVO 的 robotics 机制讨论（为什么 gait patterns + contact dynamics 使 RSSM reward head 特别脆弱），venue fit 可以从 borderline 提升到 acceptable。\n\n**\"核心矛盾：CIVO 是 locomotion-specific negative result，robotics framing 装饰性\"**: 部分同意 framing 可以更深入，但 \"装饰性\" 一词过强。论文的核心发现（imagination-based bootstrapping vs MPC re-planning 的结构性差异）对 robotics deployment 决策有直接指导意义。\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-24T07:14:53.093181+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4073
}
```

</details>

---

### Assistant

_source line 172 · 2026-05-24T07:15:03.179630+00:00_

交叉回应已提交。总结：

- **7 个 R2 要点中 AGREE 5 个，REBUT 2 个**
- REBUT 的两个点：(1) CoRL venue fit — R2 低估了 locomotion 作为 core robotics 的相关性，以及 ManiSkill non-CIVO 结果的 discriminative validity 价值；(2) F1-F7 编号方式 — findings-based structure 在 diagnostic paper 中合理
- AGREE 的重点：贡献度偏 diagnostic（6.5/10）、Becker-Ehmck 引用缺失、ManiSkill/Cheetah baseline eval 在 Table 1 中缺失、1-seed 条目统计无意义、abstract 数字过密
- 与 R2 最大分歧在 venue fit 评分（我给 6.5 vs R2 的 5）和 "装饰性 framing" 的判断

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 5

44 recorded events

### User

_source line 173 · 2026-05-24T09:27:14.661460+00:00_

[Round 4 审稿请求]:
## Round 4 修订评估任务 — Reviewer 1（方法严谨性 + 残留问题验证）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`
**目标 Venue**: ⚠️ ICML 2026（从 CoRL 2026 转投）
**Deadline**: 2026-01-28（已过期；可能处于 rebuttal 阶段或准备下一轮投稿）
**页数限制**: 8 页正文 + unlimited appendix/references
**模板**: 应使用 ICML 2026 官方样式（当前仍为 corl_2026，需核实）
**匿名规则**: Double-blind
**审查侧重**: 方法严谨性、Round 3 残留问题验证

### 背景

Venue 从 CoRL 2026 改为 ICML 2026。Round 3 评分 Weak Reject (5/10)，主因是 CoRL venue fit 和 actionable contribution 问题。转投 ICML 后需重新评估。

### 必须逐条检查的 Issue（Round 3 open/in_progress）

**1. R1-W2 / REV-2 [warning, in_progress]: 105K vs 505K 步数不对等**
- Round 3 问题：未显式讨论步数不对等，exp_045 长跑数据未呈现
- **已知修改**：Discussion 新增 "Training horizon" 段落，提及 "Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset"
- **检查要点**：这段讨论是否充分回应了问题？302K 单 seed 数据是否在 Appendix 呈现？"sufficient to observe collapse onset" 的论证是否有力？1/4 self-correction 现象是否被合理讨论？

**2. R2-W1 [warning, in_progress]: TAWM 对比无实证，"structural factor" 过强**
- Round 3 问题：Abstract/Conclusion 称 "the structural factor" 但无 MPC 实验
- **已知修改**：Abstract 改为 "a hypothesized structural factor"；Conclusion 改为 "hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work."
- **检查要点**：措辞是否已充分弱化？全文是否一致使用 "hypothesized"？是否还有其他位置仍用 "the structural factor"？

**3. R3-N-new-1 [warning, open]: Online detector 样本量不足**
- Round 3 问题：n=14, 5 正例, TPR=5/5 统计意义有限，不应作为独立 contribution
- **已知修改**：Contribution 4 改为 "Preliminary diagnostic"，报告 95% CI [47.8%, 100%]；Section 4.7 加 "requires larger-sample validation before deployment"
- **检查要点**：降级是否充分？论文是否还在其他地方过度宣传 detector？

**4. R3-N-new-2 [info, open]: Dual-critic convergence 叙事过简**
- Round 3 问题：ρ>0.999 与 wide dual-critic 3/4 prevention 成功有张力
- **已知修改**：Section 4.8 加 "the min operation in wide dual-critic may instead regularize through gradient diversity"
- **检查要点**："gradient diversity" 解释是否有支撑（Appendix 是否提供了证据）？是否解决了叙事张力？

**5. R3-N-new-3 [warning, open]: Baseline eval 值缺失**
- Round 3 问题：Table 1 中 ManiSkill/Cheetah 缺少 baseline
- **已知修改**：Table 1 脚注加 "Baselines: Walker 915.7 (row 001); Cheetah ~320; PickCube via exp_019a_v2; StackCube/PegInsertion not separately measured."
- **检查要点**：脚注中的部分 baseline 是否足够？"not separately measured" 是否可接受？

**6. 统计数据更新**：26/29 → 27/30, AUROC 0.953 → 0.957, 6/6 → 7/7 seeds
- **检查要点**：新增数据是否一致反映在全文中？数字是否前后一致？

### 额外要求
- 检查论文是否引入了新的方法论问题
- 评估 4 seeds 在 ICML 标准下是否足够
- 给出方法严谨性评分（1-10）

### 输出格式
1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由
2. 列出新发现的问题（如有）
3. 方法严谨性评分（1-10）+ 简要总评

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-24T09:27:25.209073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ICML 2026 reviewer guidelines review form scoring dimensions rating scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ICML 2026 reviewer guidelines review form scoring dimensions rating scale"
  }
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-24T09:27:27.067016+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-24T09:27:27.067484+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-24T09:27:30.481384+00:00_

Web search results for query: "ICML 2026 reviewer guidelines review form scoring dimensions rating scale"

Links: [{"title":"ICML 2026 Reviewer Instructions","url":"https://icml.cc/Conferences/2026/ReviewerInstructions"},{"title":"ICML 2026 Area Chair Instructions","url":"https://icml.cc/Conferences/2026/AreaChairInstructions"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"Introducing ICML 2026 policy for self-ranking in reviews – ICML Blog","url":"https://blog.icml.cc/2026/01/12/introducing-icml-2026-policy-for-self-ranking-in-reviews/"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"ICML 2025 Reviewer Instructions","url":"https://icml.cc/Conferences/2025/ReviewerInstructions"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"}]

Based on the search results, I found information about ICML 2026 reviewer guidelines. Here's what I discovered:

## Review Form

The review form for ICML 2026 is new and has specific items that reviewers are required to complete.

## Scoring Dimensions and Rating Scale

While the search results reference questions about paper originality and technical soundness, they don't provide a complete breakdown of all scoring dimensions or the specific numerical rating scale used for ICML 2026. 

The results indicate that reviewers rate the paper on a scale to indicate the soundness of the technical claims, experimental and research methodology, and whether the central claims are adequately supported with evidence.

Additionally, recommendations and meta-reviews should be informed by the review content, as opposed to just relying on average (or other aggregate) numerical scores.

For more detailed information about the specific rating scales and all scoring dimensions, you would need to consult the full ICML 2026 Reviewer Instructions page directly at https://icml.cc/Conferences/202
…[truncated 200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5272
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-24T09:27:39.387070+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://icml.cc/Conferences/2026/ReviewerInstructions",
  "prompt": "Extract ALL review form dimensions, rating scales (with numeric values and their meanings), evaluation criteria, and scoring rubrics. I need the complete review form specification including overall score scale, soundness, significance, novelty, clarity, reproducibility, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://icml.cc/Conferences/2026/ReviewerInstructions",
    "prompt": "Extract ALL review form dimensions, rating scales (with numeric values and their meanings), evaluation criteria, and scoring rubrics. I need the complete review form specification including overall score scale, soundness, significance, novelty, clarity, reproducibility, etc."
  }
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-24T09:27:41.764854+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-24T09:27:42.269052+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 27/30, AUROC${=}0.957$, LOEO cross-validated). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-24T09:27:42.269518+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-24T09:27:42.321017+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-24T09:27:46.942551+00:00_

# ICML 2026 Review Form Dimensions and Rating Scales

## Main Track Review Form

### Rating Scales (All use 4-point scale unless noted):

**Soundness**
- 4: excellent
- 3: good
- 2: fair
- 1: poor

**Presentation**
- 4: excellent
- 3: good
- 2: fair
- 1: poor

**Significance**
- 4: excellent
- 3: good
- 2: fair
- 1: poor

**Originality**
- 4: excellent
- 3: good
- 2: fair
- 1: poor

**Overall Recommendation** (6-point scale):
- 6: "Strong Accept: Technically flawless paper with exceptional impact"
- 5: "Accept: Technically solid paper, with high impact"
- 4: Weak accept
- 3: Weak reject
- 2: Reject
- 1: Strong Reject

**Confidence** (5-point scale):
- 5: absolutely certain
- 4: confident but not certain
- 3: fairly confident
- 2: willing to defend but uncertain
- 1: educated guess

### Evaluation Dimensions:
- Soundness (technical correctness, proof validity, experimental design)
- Presentation (clarity, structure, contextualization)
- Significance (importance, impact potential, practical utility)
- Originality (novel insights, new methods/tasks/theory, creative combinations)

### Additional Form Items:
- Summary
- Strengths and Weaknesses
- Key Questions for Authors
- Limitations assessment
- Ethical Concerns flags
- LLM Policy compliance affirmation
- Code of Conduct acknowledgment
- Final Justification (post-rebuttal)

## Position Paper Track Review Form

**Support** (4-point): "how well it supports its position with clear reasoning"

**Significance** (4-point): "position is important, in terms of scope, impact, timeliness"

**Discussion Potential** (4-point): "potential to inspire constructive discussion"

**Argument Clarity** (4-point): "clarity of presentation (including writing style)"

**Related Work** (4-point): "discussion of literature and events relevant"

**Overall Rating** (6-point scale): Same as Main Track

**Confidence** (5-point scale): Same as Main Track

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7555
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-24T09:27:57.357344+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-24T09:27:57.408510+00:00_

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
…[truncated 12044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-24T09:28:10.978345+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-24T09:28:11.028986+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-24T09:28:11.130006+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-24T09:28:11.231005+00:00_

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
…[truncated 5036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-24T09:28:17.309019+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-24T09:28:17.763447+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-24T09:28:18.068332+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "structural factor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "structural factor",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-24T09:28:18.119040+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex:1:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex:4:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-24T09:28:22.142919+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "structural factor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "context": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "structural factor",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "context": "0"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-24T09:28:22.193574+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex:1:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex:4:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-24T09:28:31.629280+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "extended.training|302K|self-recovery|170K additional",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "extended.training|302K|self-recovery|170K additional",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-24T09:28:32.131950+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-8-Monitor via NVE diagnostic ($\geq 1.5\times$, AUROC${=}0.957$; Table~\ref{tab:nve_loeo}). Freezing the $\dt$-embedding converts CIVO onset (7/7 trained locomotion, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\times$) causes irrecoverable damage (Appendix~\ref{sec:appendix_analysis}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-9-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-10-\paragraph{Training horizon.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:11:Our primary analysis uses 105K steps, sufficient to observe CIVO onset (45K--65K) and classify trajectories. Extended training (${\sim}$302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset---at substantial computational cost that the frozen $\dt$-embedding diagnostic eliminates entirely (Appendix~\ref{sec:extended_training}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-12-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-13-\paragraph{Implications for robot learning.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex-14-No $\dt$-embedding-dependent CIVO was observed in manipulation (Table~\ref{tab:cross_domain}). Both domains use dense shaped rewards, so reward sparsity cannot explain the boundary. Possible mediators include action-space periodicity, observation structure, and continuous versu
…[truncated 2888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-24T09:28:32.584408+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gradient diversity|gradient.divers",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gradient diversity|gradient.divers",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-24T09:28:32.636054+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-163-\label{sec:arch_results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-164-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-165-\paragraph{Critic convergence in pure imagination.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:166:Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}). Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix~\ref{sec:dual_critic_appendix}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-167-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-168-\paragraph{$2{\times}2$ factorial: recovery vs.\ prevention.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-169-Min drives recovery: narrow dual-critic (${\sim}1.2$M) recovers fully (${\sim}16$--$19\times$ recovery ratio) despite $2\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\nve \leq 1.4\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-24T09:28:36.953845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": "640",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "offset": "640",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-24T09:28:37.004538+00:00_

640	\bottomrule
641	\end{tabular}
642	\end{table}
643	
644	\subsection{Extended Training Dynamics}\label{sec:extended_training}
645	
646	One Walker seed (s3, exp\_045) was extended from 112K to approximately 302K steps to investigate long-horizon CIVO dynamics. After onset (NVE peak $4.91\times$ at 132K steps), the system exhibited complete self-recovery: NVE declined to $0.05\times$ and evaluation performance recovered to 867.6 (94.7\% of baseline). This recovery required approximately 170K additional training steps beyond onset. The trajectory shows a single onset--recovery cycle with no recurrence, suggesting that the CIVO feedback loop can break spontaneously given sufficient training---though at substantial computational cost that the frozen $\dt$-embedding diagnostic eliminates entirely.
647	
648	\subsection{Why MPC Is Immune}
649	\label{sec:mpc_immune}
650	
651	\citet{nhu2025tawm} show that $\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\dt > 1$ is amplified through the closed actor-critic loop.
652	
653	\subsection{The \texorpdfstring{$\dt$}{dt}-Embedding Dilemma}
654	\label{sec:embedding_dilemma}
655	
656	The factorial results reveal a fundamental tension: removing the $\dt$-embedding (008f) eliminates CIVO but at a $13\times$ cost to reward prediction quality ($0.7469$ vs.\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\dt{=}1$ while retaining the trained embedding (008e\_v3) avoids collapse in 2 of 4 seeds (50\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\times$) and Pathw
…[truncated 1546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-24T09:28:43.443621+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gradient diversity|dual_critic_appendix|dual.critic.appendix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gradient diversity|dual_critic_appendix|dual.critic.appendix",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "5"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-24T09:28:43.545367+00:00_

859-\subsection{Detector Limitations}
860-
861-[Omitted long context line]
862-
863-\section{Dual-Critic Mechanism Ablation}
864:\label{sec:dual_critic_appendix}
865-
866-\subsection{\texorpdfstring{$2{\times}2$}{2x2} Factorial Design}
867-
868-We ablate the critic architecture in a $2{\times}2$ factorial: \{single, dual\} $\times$ \{narrow (${\sim}1.2$M), wide (${\sim}2.4$M)\} parameters. Table~\ref{tab:dual_critic_full} reports all configurations.
869-

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-24T09:28:48.113082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": "863",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "offset": "863",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-24T09:28:48.214152+00:00_

863	\section{Dual-Critic Mechanism Ablation}
864	\label{sec:dual_critic_appendix}
865	
866	\subsection{\texorpdfstring{$2{\times}2$}{2x2} Factorial Design}
867	
868	We ablate the critic architecture in a $2{\times}2$ factorial: \{single, dual\} $\times$ \{narrow (${\sim}1.2$M), wide (${\sim}2.4$M)\} parameters. Table~\ref{tab:dual_critic_full} reports all configurations.
869	
870	\begin{table}[ht]
871	\centering
872	\caption{Dual-critic $2{\times}2$ factorial results. Walker Walk unless noted.}
873	\label{tab:dual_critic_full}
874	\footnotesize
875	\setlength{\tabcolsep}{3pt}
876	\begin{tabular}{llcccl}
877	\toprule
878	\textbf{Exp} & \textbf{Config} & \textbf{Params} & \textbf{NVE} & \textbf{Eval} & \textbf{Outcome} \\
879	\midrule
880	008d & Single narrow & 1.2M & 4.12$\times$ & 82.8 & Collapse \\
881	033 & Wide single & 2.4M & 4.75$\times$ & 407.9 & CIVO $\to$ self-repair \\
882	035 s0 & Narrow dual (min) & 1.2M & 2.75$\times$ & 697.8 & CIVO $\to$ recovery \\
883	039 s1 & Narrow dual (min) & 1.2M & 2.19$\times$ & 592.7 & CIVO $\to$ recovery \\
884	032 s0 & Wide dual (min) & 2.4M & $\leq$1.1$\times$ & 739.7 & CIVO prevented \\
885	032b s1 & Wide dual (min) & 2.4M & 1.4$\times$ & 551.8 & CIVO prevented \\
886	038 s2 & Wide dual (min) & 2.4M & $\leq$0.3$\times$ & 120.9$^*$ & Non-CIVO collapse \\
887	\midrule
888	\multicolumn{6}{l}{\textit{Cross-environment}} \\
889	034 & Cheetah dual & 2.4M & 1.75$\times$ & 97.5 & Partial recovery (31\%) \\
890	037 & Cheetah wide single & 2.4M & 3.60$\times$ & 146.1 & CIVO $\to$ self-repair \\
891	036 & PickCube dual & 2.4M & 2.3$\times$ & 27.7 & Transient CIVO \\
892	\bottomrule
893	\end{tabular}
894	\vspace{1pt}
895	{\raggedright\footnotesize $^*$CIVO prevented (NVE $\leq 0.3\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\par}
896	\end{table}
897	
898	\subsection{Critic Convergence (\texorpdfstring{$v_1 \approx v_2$}{v1 ≈ v2})}
899
…[truncated 2596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-24T09:29:54.348011+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "4 seeds|four seeds|Key configurations use",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "4 seeds|four seeds|Key configurations use",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-24T09:29:54.803034+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex:10:Statistical power with 4 seeds per configuration is limited \citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.988$) may require recalibration for different reward scales.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:656:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:723:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:90:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:103:Exp\_008e\_v3 restricts imagination to $\dt{=}1$ while retaining the trained embedding. Two of four seeds collapse (50\%): Pathway~A (CIVO, $\nve = 4.02\times$) and preliminary Pathway~B (entropy \emph{increase}, $\nve = 3.78\times$; 2 seeds only, requires confirmation; see Figure~\ref{fig:multiple_pathways} in Appendix~\ref{sec:pathways}). Pathway~B produces one of three non-CIVO false positives ($n{=}30$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-24T09:29:55.506162+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "seed.4|seed.5|five Walker|five seeds",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "seed.4|seed.5|five Walker|five seeds",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-24T09:29:55.708024+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:244:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:614:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:77:\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\ref{tab:complete_results}) exceeds the $1.5\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:81:The trained $\dt$-embedding precedes CIVO in all five Walker Walk seeds (peak NVE $1.53$--$4.72\times$), universally degrading performance to below 30\% of baseline (IQM $175.2$, $n{=}5$; \citealt{agarwal2021precipice}). Combined with Cheetah Run (\S\ref{sec:f6}), CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 6/7 suffering sustained policy collapse, 1/7 self-correcting (Appendix~\ref{sec:seed_divergence}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-24T09:30:18.089044+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\bisolate\\b|causal chain|causal factor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\bisolate\\b|causal chain|causal factor",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-24T09:30:18.140114+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:12:We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:244:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:549:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex:11:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:4:We organize results around seven findings (F1--F7) that establish a causal chain from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-24T09:30:25.494337+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Becker|becker|ehmck",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Becker|becker|ehmck",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-24T09:30:25.595280+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-24T09:33:25.762243+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Round 4 审稿报告 — Reviewer 1（方法严谨性 + 残留问题验证）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL\"\n**目标 Venue**: ICML 2026（从 CoRL 转投）\n\n---\n\n## 总体评分\n\n**方法严谨性**: 7.5/10（Round 3 为 7/10，提升 0.5 分）\n**ICML Overall Recommendation**: 4/6 (Weak Accept)\n**一句话总结**: Round 3 两个 open warning 均已实质性解决（步数不对等增加讨论+302K 延长数据，\"structural factor\" 弱化为 \"hypothesized\"），但数据更新引入了 seed 数量不一致问题（Methodology 说 4 seeds 而 Results 报告 5 seeds），模板仍为 CoRL 格式，需要在投稿前紧急修复。\n\n## ICML 2026 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/4 (Good) | Factorial design 严谨，LOEO AUROC=0.988 有力，但 seed 数量前后不一致削弱可信度 |\n| Presentation | 3/4 (Good) | F1-F7 结构清晰，但存在数字不一致、模板错误 |\n| Significance | 3/4 (Good) | 对 imagination-based RL 社区有直接价值；转投 ICML 消除了 venue fit 问题 |\n| Originality | 3/4 (Good) | 首个系统诊断 CIVO 的工作；四级干预层级和 dual-critic convergence 发现均为新贡献 |\n\n---\n\n## 逐条 Issue 检查\n\n### 1. R1-W2 [warning, in_progress]: 105K vs 505K 步数不对等\n**[RESOLVED]**\n\n**修改内容确认**:\n- Discussion Section 5 新增 \"Training horizon\" 段落（analysis.tex line 10-11）\n- 正文明确说明：\"Our primary analysis uses 105K steps, sufficient to observe CIVO onset (45K--65K) and classify trajectories\"\n- 报告 302K 延长实验结果：\"Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset\"\n- Appendix D.4 \"Extended Training Dynamics\" 提供完整细节：exp_045 seed s3，NVE peak 4.91× at 132K → 自恢复至 NVE 0.05×，eval 867.6（94.7% of baseline），需约 170K 额外步数\n- 论文将此与 frozen embedding 对比：\"at substantial computational cost that the frozen dt-embedding diagnostic eliminates entirely\"\n\n**评估**: 这是一个充分的回应。论文现在：(a) 明确论证 105K 足以观察 onset（45K-65K window）；(b) 提供 1 seed 的 302K 长跑证据显示自恢复可能但代价高昂；(c) 将此纳入 Discussion 而非隐藏在 Appendix。单 seed 长跑的统计效力有限，但对诊断论文而言足够——论文不声称自恢复率，只是展示其存在性。\n\n---\n\n### 2. R2-W1 [warning, in_progress]: TAWM 对比无实证，\"structural factor\" 过强\n**[RESOLVED]**\n\n**修改内容确认**:\n- Abstract: \"a hypothesized structural factor\" ✓（此前为 \"the structural factor\"）\n- Conclusion: \"hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work.\" ✓\n- Grep 确认全文仅 Abstract 和 Conclusion 使用 \"structural factor\"，均已加 \"hypothesized\" ✓\n\n**全文一致性检查**:\n- Introduction Contribution 2: 使用 \"Architectural boundary\" 而非 \"structural factor\"，表述为事实观察（\"dt-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping\"）——这是基于 TAWM 论文和本文实验的事实描述，不是假说，措辞合理\n- Discussion paragraph 1: \"MPC re-planning prevents accumulation\"——呼应 Appendix D.5 的理论分析\n- 无其他位置仍使用 \"the structural factor\"\n\n**评估**: 措辞充分弱化且全文一致。\"hypothesized\" + \"remains future work\" 的组合恰当地将其定位为需要验证的假说。\n\n---\n\n### 3. R3-N-new-1 [warning, open]: Online detector 样本量不足\n**[RESOLVED]**\n\n**修改内容确认**:\n- Introduction Contribution 4: 降级为 \"Preliminary diagnostic\"，不再作为独立 contribution 宣传 ✓\n- 报告 95% Clopper-Pearson CI [47.8%, 100%]（n=5/5）——CI 下界 47.8% 诚实地展示了 small-sample 的不确定性 ✓\n- Section 4.7 末尾：\"The detector requires larger-sample validation before deployment as a practical diagnostic tool.\" ✓\n\n**全文其他位置检查**:\n- Discussion \"Practitioner guidelines\" (analysis.tex line 7-8): \"Monitor via NVE diagnostic (≥ 1.5×, AUROC=0.957)\"——引用的是 NVE 阈值分类器（n=30, AUROC=0.957），不是 online detector（n=14），两者区分清晰 ✓\n- Abstract: 已删除 \"100% sensitivity\" 的表述 ✓\n\n**评估**: 降级充分。\"Preliminary diagnostic\" + Clopper-Pearson CI + \"requires larger-sample validation\" 的组合正确定位了这一贡献的成熟度。\n\n---\n\n### 4. R3-N-new-3 [info, open]: Dual-critic convergence 叙事过简\n**[PARTIALLY RESOLVED]**\n\n**修改内容确认**:\n- Section 4.8 (results.tex line 166): \"Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix G).\"\n- Appendix G.3 (appendix.tex line 910): \"The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\"\n\n**问题**:\n- Section 4.8 说 \"gradient diversity\"，但 Appendix G.3 描述的机制是 \"increased capacity + early-training divergence + overestimation feedback constraint\"。两处的解释不一致\n- \"gradient diversity\" 未被定义或测量——既无 gradient 方差/cosine similarity 的数据，也无理论论证\n- Appendix G.3 的 \"briefly diverge\" 假说更具体也更诚实（承认为 open question），是更好的解释\n\n**评估**: 核心叙事张力（ρ>0.999 yet min+capacity works）在 Appendix G.3 通过 \"open question + early-training divergence hypothesis\" 被合理地框定了。但主文 Section 4.8 的 \"gradient diversity\" 措辞过于具体且无支撑。建议 Section 4.8 改为与 Appendix G.3 一致的措辞，如 \"may instead function through a capacity-dependent mechanism during early training (Appendix G)\"。\n\n这是一个 minor 措辞问题，不影响接收决定。\n\n---\n\n### 5. R3-N-new-2 [warning, open]: Baseline eval 值缺失\n**[PARTIALLY RESOLVED]**\n\n**修改内容确认**:\n- Table 1 脚注（results.tex line 47）: \"Baselines: Walker 915.7 (row 001); Cheetah ~320; PickCube via exp_019a_v2; StackCube/PegInsertion not separately measured.\"\n\n**评估**:\n- Walker: 已在 Table 1 row 001 显示 (915.7 @105K) ✓\n- Cheetah: \"~320\" 为近似值——对于评估 CIVO 严重度（010b eval 51.7 = ~16% of ~320）足够，但精确值更好\n- PickCube: \"via exp_019a_v2\" 但未给出 eval 值——读者仍无法判断 019b (26.64) 的 degradation 比例\n- StackCube/PegInsertion: \"not separately measured\" 仍然是一个gap\n\n**对论文论点的影响**: 有限。ManiSkill 环境的论点是 CIVO 不存在（frozen controls match trained），不需要 baseline 来判断 CIVO 是否发生。但如果要讨论 dt-conditioning 对 manipulation 任务的总体影响（即使不是 CIVO），baseline 值是必要的。\n\n---\n\n### 6. 统计数据更新 (26/29→27/30, AUROC 0.953→0.957, 6/6→7/7)\n**[STILL_OPEN] — 发现多处不一致**\n\n**数字更新一致性检查**:\n\n| 指标 | 位置 | 值 | 一致？ |\n|------|------|-----|--------|\n| 分类 accuracy | Abstract | 27/30 | ✓ |\n| 分类 accuracy | Introduction | 27/30 | ✓ |\n| 分类 accuracy | Section 4.2 | 27/30 | ✓ |\n| AUROC (in-sample) | Abstract | 0.957 | ✓ |\n| AUROC (in-sample) | Introduction | 0.957 | ✓ |\n| AUROC (in-sample) | Section 3.4 | 0.957 | ✓ |\n| AUROC (in-sample) | Discussion | 0.957 | ✓ |\n| AUROC (in-sample) | Conclusion | 0.957 | ✓ |\n| AUROC (LOEO) | Section 3.4 | 0.988 | ✓ |\n| AUROC (LOEO) | Limitations | 0.988 | ✓ |\n| CIVO seeds | Introduction C1 | 7/7 | ✓ |\n| CIVO seeds | Discussion | 7/7 | ✓ |\n\n**⚠️ 不一致之处**:\n\n**N-R4-1 [warning]: Seed 数量不一致**\n- **Methodology Section 3.3** (methodology.tex line 32): \"Key configurations use **4** seeds\"\n- **Results Section 4.2** (results.tex line 81): \"all **five** Walker Walk seeds (peak NVE 1.53--4.72×)...IQM 175.2, **n=5**\"\n- **Conclusion Limitations** (conclusion.tex line 10): \"Statistical power with **4** seeds per configuration is limited\"\n- **结论**: Methodology 和 Limitations 说 4 seeds，Results 说 5 seeds。如果确实增加了第 5 个 Walker seed，Methodology 和 Limitations 的 \"4 seeds\" 必须同步更新\n\n**N-R4-2 [minor]: Figure 2 caption 未更新**\n- **Figure 2 caption** (results.tex line 77): \"n=**3** seeds plotted; seed~**4** data in Table\"\n- 如果有 5 个 Walker seeds，caption 应提及 seed 4 和 seed 5 的数据去向\n\n**N-R4-3 [info]: IQM 值未变**\n- IQM 从 175.2 (n=4) → 175.2 (n=5)：添加第 5 个 seed 后 IQM 保持完全相同在统计上不常见（though possible）。如果 IQM 确实没变，应该无问题。但建议作者 double-check 计算。\n\n**N-R4-4 [minor]: Introduction \"isolate\" 未更新**\n- Abstract 已改为 \"identify\"，但 Introduction line 6 仍使用 \"we **isolate** the combination of a trained dt-embedding\"\n- Introduction Contribution 1 (line 11): \"**isolate** trained dt-embedding + multi-rate exposure as jointly sufficient\"\n- Results Section 4 intro (line 4): \"establish a **causal chain**\"——虽然指的是 findings 的逻辑链，但 \"causal chain\" 措辞与全文弱化因果声明的方向不一致\n\n---\n\n## 新发现的问题\n\n### N-R4-5 [critical]: 模板未更新\n- **位置**: main.tex line 5\n- **问题**: `\\usepackage{corl_2026}` — 论文仍使用 CoRL 2026 模板，但目标 venue 已改为 ICML 2026\n- **影响**: ICML 2026 使用自己的样式文件。提交 CoRL 格式的论文将导致**格式违规**，可能 desk reject\n- **必须修改**: 替换为 ICML 2026 官方样式（`icml2026.sty`），同时检查页数、列宽、字体大小等是否合规\n\n### N-R4-6 [minor]: Becker-Ehmck 2023 仍未引用\n- Reviewer 2 在 Round 2 和 Round 3 均指出此遗漏，Round 4 仍未修复\n- Grep 确认全文和 references 中均无 \"Becker\" 或 \"ehmck\" 匹配\n\n### N-R4-7 [info]: ICML Limitations 格式\n- 当前 Limitations 为 Conclusion Section 内的 `\\paragraph{}`\n- ICML 2026 reviewer form 包含 \"Limitations assessment\" 维度。虽然不硬性要求独立 section，但建议将 Limitations 独立为 section 以提升可见性\n\n---\n\n## ICML Venue Fit 评估\n\n转投 ICML 后，venue fit 问题**基本消除**：\n\n1. **ICML 核心受众**: RL methodology/analysis 论文是 ICML 的核心内容。CIVO 作为 imagination-based RL 的失败模式诊断，直接面向 ICML 的 world-model RL 读者群\n2. **不再需要 robotics framing**: CoRL 审稿时 robotics relevance 是主要弱点。ICML 评价维度（Soundness, Significance, Originality, Presentation）全部与本文匹配\n3. **Negative result 接受度**: ICML 历史上接受 diagnostic/negative result 论文（如 Henderson et al. 2018 \"Deep RL That Matters\"），本文的系统性 factorial 分析符合这一传统\n4. **4-5 seeds 在 ICML 的充分性**: ICML RL 论文通常使用 3-10 seeds。本文的 5 seeds (Walker) + 2 seeds (Cheetah) + LOEO AUROC=0.988 满足 ICML 最低标准。Agarwal et al. 2021 IQM 报告是加分项\n\n**评分: Venue Fit 8.5/10（vs Round 3 CoRL 的 6.5/10）**\n\n---\n\n## Issue 状态汇总\n\n| Issue | Round 3 状态 | Round 4 状态 | 说明 |\n|-------|-------------|-------------|------|\n| R1-W2 步数不对等 | STILL_OPEN | **[RESOLVED]** | Discussion 新段 + Appendix D.4 302K 延长数据 |\n| R2-W1 TAWM 对比 | STILL_OPEN | **[RESOLVED]** | \"hypothesized structural factor\" 全文一致 |\n| N-new-1 Detector 样本量 | open | **[RESOLVED]** | 降级 \"Preliminary\" + CI + \"requires validation\" |\n| N-new-3 Dual-critic 叙事 | open | **[PARTIALLY]** | Appendix 承认 open question，但主文 \"gradient diversity\" 措辞无支撑 |\n| N-new-2 Baseline 缺失 | open | **[PARTIALLY]** | 脚注增加部分 baseline，2 个 ManiSkill 仍 \"not measured\" |\n| 统计数据一致性 | — | **[STILL_OPEN]** | Seed 数量不一致（4 vs 5）、Figure caption 未更新 |\n| 模板 | — | **[NEW, critical]** | 仍为 corl_2026，需改 ICML 2026 |\n| Becker-Ehmck 引用 | R2 flagged ×2 | **[STILL_OPEN]** | 第三轮仍未引用 |\n\n**Round 3 的 2 个 STILL_OPEN warning 全部 RESOLVED。**\n**新增 1 个 critical（模板）+ 1 个 warning（seed 数量不一致）+ 若干 minor。**\n\n---\n\n## 方法严谨性总评\n\n**评分: 7.5/10（ICML 标准）**\n\n相较 Round 3 (7/10) 提升了 0.5 分，原因：\n- 步数不对等问题通过 Discussion 段落 + 302K 延长数据实质性解决\n- TAWM 措辞通过 \"hypothesized\" 一词和 future work 声明恰当弱化\n- Detector 降级为 preliminary 诚实反映了统计效力限制\n\n未达 8/10 的原因：\n- **Seed 数量前后不一致**（4 vs 5）是一个 credibility 问题——reviewer 会质疑数据管理是否可靠\n- **模板未更新**是 desk reject 风险\n- **\"gradient diversity\" 无支撑**虽然是 minor，但反映了在添加解释时未配套实证的习惯\n\n**ICML 推荐**: Weak Accept (4/6)。核心方法论和实验设计 sound，CIVO 发现对社区有价值，转投 ICML 消除了 venue fit 障碍。修复 seed 不一致和模板问题后可达 Accept (5/6)。\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Round 4 审稿报告 — Reviewer 1（方法严谨性 + 残留问题验证）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL\"\n**目标 Venue**: ICML 2026（从 CoRL 转投）\n\n---\n\n## 总体评分\n\n**方法严谨性**: 7.5/10（Round 3 为 7/10，提升 0.5 分）\n**ICML Overall Recommendation**: 4/6 (Weak Accept)\n**一句话总结**: Round 3 两个 open warning 均已实质性解决（步数不对等增加讨论+302K 延长数据，\"structural factor\" 弱化为 \"hypothesized\"），但数据更新引入了 seed 数量不一致问题（Methodology 说 4 seeds 而 Results 报告 5 seeds），模板仍为 CoRL 格式，需要在投稿前紧急修复。\n\n## ICML 2026 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/4 (Good) | Factorial design 严谨，LOEO AUROC=0.988 有力，但 seed 数量前后不一致削弱可信度 |\n| Presentation | 3/4 (Good) | F1-F7 结构清晰，但存在数字不一致、模板错误 |\n| Significance | 3/4 (Good) | 对 imagination-based RL 社区有直接价值；转投 ICML 消除了 venue fit 问题 |\n| Originality | 3/4 (Good) | 首个系统诊断 CIVO 的工作；四级干预层级和 dual-critic convergence 发现均为新贡献 |\n\n---\n\n## 逐条 Issue 检查\n\n### 1. R1-W2 [warning, in_progress]: 105K vs 505K 步数不对等\n**[RESOLVED]**\n\n**修改内容确认**:\n- Discussion Section 5 新增 \"Training horizon\" 段落（analysis.tex line 10-11）\n- 正文明确说明：\"Our primary analysis uses 105K steps, sufficient to observe CIVO onset (45K--65K) and classify trajectories\"\n- 报告 302K 延长实验结果：\"Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset\"\n- Appendix D.4 \"Extended Training Dynamics\" 提供完整细节：exp_045 seed s3，NVE peak 4.91× at 132K → 自恢复至 NVE 0.05×，eval 867.6（94.7% of baseline），需约 170K 额外步数\n- 论文将此与 frozen embedding 对比：\"at substantial computational cost that the frozen dt-embedding diagnostic eliminates entirely\"\n\n**评估**: 这是一个充分的回应。论文现在：(a) 明确论证 105K 足以观察 onset（45K-65K window）；(b) 提供 1 seed 的 302K 长跑证据显示自恢复可能但代价高昂；(c) 将此纳入 Discussion 而非隐藏在 Appendix。单 seed 长跑的统计效力有限，但对诊断论文而言足够——论文不声称自恢复率，只是展示其存在性。\n\n---\n\n### 2. R2-W1 [warning, in_progress]: TAWM 对比无实证，\"structural factor\" 过强\n**[RESOLVED]**\n\n**修改内容确认**:\n- Abstract: \"a hypothesized structural factor\" ✓（此前为 \"the structural factor\"）\n- Conclusion: \"hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work.\" ✓\n- Grep 确认全文仅 Abstract 和 Conclusion 使用 \"structural factor\"，均已加 \"hypothesized\" ✓\n\n**全文一致性检查**:\n- Introduction Contribution 2: 使用 \"Architectural boundary\" 而非 \"structural factor\"，表述为事实观察（\"dt-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping\"）——这是基于 TAWM 论文和本文实验的事实描述，不是假说，措辞合理\n- Discussion paragraph 1: \"MPC re-planning prevents accumulation\"——呼应 Appendix D.5 的理论分析\n- 无其他位置仍使用 \"the structural factor\"\n\n**评估**: 措辞充分弱化且全文一致。\"hypothesized\" + \"remains future work\" 的组合恰当地将其定位为需要验证的假说。\n\n---\n\n### 3. R3-N-new-1 [warning, open]: Online detector 样本量不足\n**[RESOLVED]**\n\n**修改内容确认**:\n- Introduction Contribution 4: 降级为 \"Preliminary diagnostic\"，不再作为独立 contribution 宣传 ✓\n- 报告 95% Clopper-Pearson CI [47.8%, 100%]（n=5/5）——CI 下界 47.8% 诚实地展示了 small-sample 的不确定性 ✓\n- Section 4.7 末尾：\"The detector requires larger-sample validation before deployment as a practical diagnostic tool.\" ✓\n\n**全文其他位置检查**:\n- Discussion \"Practitioner guidelines\" (analysis.tex line 7-8): \"Monitor via NVE diagnostic (≥ 1.5×, AUROC=0.957)\"——引用的是 NVE 阈值分类器（n=30, AUROC=0.957），不是 online detector（n=14），两者区分清晰 ✓\n- Abstract: 已删除 \"100% sensitivity\" 的表述 ✓\n\n**评估**: 降级充分。\"Preliminary diagnostic\" + Clopper-Pearson CI + \"requires larger-sample validation\" 的组合正确定位了这一贡献的成熟度。\n\n---\n\n### 4. R3-N-new-3 [info, open]: Dual-critic convergence 叙事过简\n**[PARTIALLY RESOLVED]**\n\n**修改内容确认**:\n- Section 4.8 (results.tex line 166): \"Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix G).\"\n- Appendix G.3 (appendix.tex line 910): \"The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\"\n\n**问题**:\n- Section 4.8 说 \"gradient diversity\"，但 Appendix G.3 描述的机制是 \"increased capacity + early-training divergence + overestimation feedback constraint\"。两处的解释不一致\n- \"gradient diversity\" 未被定义或测量——既无 gradient 方差/cosine similarity 的数据，也无理论论证\n- Appendix G.3 的 \"briefly diverge\" 假说更具体也更诚实（承认为 open question），是更好的解释\n\n**评估**: 核心叙事张力（ρ>0.999 yet min+capacity works）在 Appendix G.3 通过 \"open question + early-training divergence hypothesis\" 被合理地框定了。但主文 Section 4.8 的 \"gradient diversity\" 措辞过于具体且无支撑。建议 Section 4.8 改为与 Appendix G.3 一致的措辞，如 \"may instead function through a capacity-dependent mechanism during early training (Appendix G)\"。\n\n这是一个 minor 措辞问题，不影响接收决定。\n\n---\n\n### 5. R3-N-new-2 [warning, open]: Baseline eval 值缺失\n**[PARTIALLY RESOLVED]**\n\n**修改内容确认**:\n- Table 1 脚注（results.tex line 47）: \"Baselines: Walker 915.7 (row 001); Cheetah ~320; PickCube via exp_019a_v2; StackCube/PegInsertion not separately measured.\"\n\n**评估**:\n- Walker: 已在 Table 1 row 001 显示 (915.7 @105K) ✓\n- Cheetah: \"~320\" 为近似值——对于评估 CIVO 严重度（010b eval 51.7 = ~16% of ~320）足够，但精确值更好\n- PickCube: \"via exp_019a_v2\" 但未给出 eval 值——读者仍无法判断 019b (26.64) 的 degradation 比例\n- StackCube/PegInsertion: \"not separately measured\" 仍然是一个gap\n\n**对论文论点的影响**: 有限。ManiSkill 环境的论点是 CIVO 不存在（frozen controls match trained），不需要 baseline 来判断 CIVO 是否发生。但如果要讨论 dt-conditioning 对 manipulation 任务的总体影响（即使不是 CIVO），baseline 值是必要的。\n\n---\n\n### 6. 统计数据更新 (26/29→27/30, AUROC 0.953→0.957, 6/6→7/7)\n**[STILL_OPEN] — 发现多处不一致**\n\n**数字更新一致性检查**:\n\n| 指标 | 位置 | 值 | 一致？ |\n|------|------|-----|--------|\n| 分类 accuracy | Abstract | 27/30 | ✓ |\n| 分类 accuracy | Introduction | 27/30 | ✓ |\n| 分类 accuracy | Section 4.2 | 27/30 | ✓ |\n| AUROC (in-sample) | Abstract | 0.957 | ✓ |\n| AUROC (in-sample) | Introduction | 0.957 | ✓ |\n| AUROC (in-sample) | Section 3.4 | 0.957 | ✓ |\n| AUROC (in-sample) | Discussion | 0.957 | ✓ |\n| AUROC (in-sample) | Conclusion | 0.957 | ✓ |\n| AUROC (LOEO) | Section 3.4 | 0.988 | ✓ |\n| AUROC (LOEO) | Limitations | 0.988 | ✓ |\n| CIVO seeds | Introduction C1 | 7/7 | ✓ |\n| CIVO seeds | Discussion | 7/7 | ✓ |\n\n**⚠️ 不一致之处**:\n\n**N-R4-1 [warning]: Seed 数量不一致**\n- **Methodology Section 3.3** (methodology.tex line 32): \"Key configurations use **4** seeds\"\n- **Results Section 4.2** (results.tex line 81): \"all **five** Walker Walk seeds (peak NVE 1.53--4.72×)...IQM 175.2, **n=5**\"\n- **Conclusion Limitations** (conclusion.tex line 10): \"Statistical power with **4** seeds per configuration is limited\"\n- **结论**: Methodology 和 Limitations 说 4 seeds，Results 说 5 seeds。如果确实增加了第 5 个 Walker seed，Methodology 和 Limitations 的 \"4 seeds\" 必须同步更新\n\n**N-R4-2 [minor]: Figure 2 caption 未更新**\n- **Figure 2 caption** (results.tex line 77): \"n=**3** seeds plotted; seed~**4** data in Table\"\n- 如果有 5 个 Walker seeds，caption 应提及 seed 4 和 seed 5 的数据去向\n\n**N-R4-3 [info]: IQM 值未变**\n- IQM 从 175.2 (n=4) → 175.2 (n=5)：添加第 5 个 seed 后 IQM 保持完全相同在统计上不常见（though possible）。如果 IQM 确实没变，应该无问题。但建议作者 double-check 计算。\n\n**N-R4-4 [minor]: Introduction \"isolate\" 未更新**\n- Abstract 已改为 \"identify\"，但 Introduction line 6 仍使用 \"we **isolate** the combination of a trained dt-embedding\"\n- Introduction Contribution 1 (line 11): \"**isolate** trained dt-embedding + multi-rate exposure as jointly sufficient\"\n- Results Section 4 intro (line 4): \"establish a **causal chain**\"——虽然指的是 findings 的逻辑链，但 \"causal chain\" 措辞与全文弱化因果声明的方向不一致\n\n---\n\n## 新发现的问题\n\n### N-R4-5 [critical]: 模板未更新\n- **位置**: main.tex line 5\n- **问题**: `\\usepackage{corl_2026}` — 论文仍使用 CoRL 2026 模板，但目标 venue 已改为 ICML 2026\n- **影响**: ICML 2026 使用自己的样式文件。提交 CoRL 格式的论文将导致**格式违规**，可能 desk reject\n- **必须修改**: 替换为 ICML 2026 官方样式（`icml2026.sty`），同时检查页数、列宽、字体大小等是否合规\n\n### N-R4-6 [minor]: Becker-Ehmck 2023 仍未引用\n- Reviewer 2 在 Round 2 和 Round 3 均指出此遗漏，Round 4 仍未修复\n- Grep 确认全文和 references 中均无 \"Becker\" 或 \"ehmck\" 匹配\n\n### N-R4-7 [info]: ICML Limitations 格式\n- 当前 Limitations 为 Conclusion Section 内的 `\\paragraph{}`\n- ICML 2026 reviewer form 包含 \"Limitations assessment\" 维度。虽然不硬性要求独立 section，但建议将 Limitations 独立为 section 以提升可见性\n\n---\n\n## ICML Venue Fit 评估\n\n转投 ICML 后，venue fit 问题**基本消除**：\n\n1. **ICML 核心受众**: RL methodology/analysis 论文是 ICML 的核心内容。CIVO 作为 imagination-based RL 的失败模式诊断，直接面向 ICML 的 world-model RL 读者群\n2. **不再需要 robotics framing**: CoRL 审稿时 robotics relevance 是主要弱点。ICML 评价维度（Soundness, Significance, Originality, Presentation）全部与本文匹配\n3. **Negative result 接受度**: ICML 历史上接受 diagnostic/negative result 论文（如 Henderson et al. 2018 \"Deep RL That Matters\"），本文的系统性 factorial 分析符合这一传统\n4. **4-5 seeds 在 ICML 的充分性**: ICML RL 论文通常使用 3-10 seeds。本文的 5 seeds (Walker) + 2 seeds (Cheetah) + LOEO AUROC=0.988 满足 ICML 最低标准。Agarwal et al. 2021 IQM 报告是加分项\n\n**评分: Venue Fit 8.5/10（vs Round 3 CoRL 的 6.5/10）**\n\n---\n\n## Issue 状态汇总\n\n| Issue | Round 3 状态 | Round 4 状态 | 说明 |\n|-------|-------------|-------------|------|\n| R1-W2 步数不对等 | STILL_OPEN | **[RESOLVED]** | Discussion 新段 + Appendix D.4 302K 延长数据 |\n| R2-W1 TAWM 对比 | STILL_OPEN | **[RESOLVED]** | \"hypothesized structural factor\" 全文一致 |\n| N-new-1 Detector 样本量 | open | **[RESOLVED]** | 降级 \"Preliminary\" + CI + \"requires validation\" |\n| N-new-3 Dual-critic 叙事 | open | **[PARTIALLY]** | Appendix 承认 open question，但主文 \"gradient diversity\" 措辞无支撑 |\n| N-new-2 Baseline 缺失 | open | **[PARTIALLY]** | 脚注增加部分 baseline，2 个 ManiSkill 仍 \"not measured\" |\n| 统计数据一致性 | — | **[STILL_OPEN]** | Seed 数量不一致（4 vs 5）、Figure caption 未更新 |\n| 模板 | — | **[NEW, critical]** | 仍为 corl_2026，需改 ICML 2026 |\n| Becker-Ehmck 引用 | R2 flagged ×2 | **[STILL_OPEN]** | 第三轮仍未引用 |\n\n**Round 3 的 2 个 STILL_OPEN warning 全部 RESOLVED。**\n**新增 1 个 critical（模板）+ 1 个 warning（seed 数量不一致）+ 若干 minor。**\n\n---\n\n## 方法严谨性总评\n\n**评分: 7.5/10（ICML 标准）**\n\n相较 Round 3 (7/10) 提升了 0.5 分，原因：\n- 步数不对等问题通过 Discussion 段落 + 302K 延长数据实质性解决\n- TAWM 措辞通过 \"hypothesized\" 一词和 future work 声明恰当弱化\n- Detector 降级为 preliminary 诚实反映了统计效力限制\n\n未达 8/10 的原因：\n- **Seed 数量前后不一致**（4 vs 5）是一个 credibility 问题——reviewer 会质疑数据管理是否可靠\n- **模板未更新**是 desk reject 风险\n- **\"gradient diversity\" 无支撑**虽然是 minor，但反映了在添加解释时未配套实证的习惯\n\n**ICML 推荐**: Weak Accept (4/6)。核心方法论和实验设计 sound，CIVO 发现对社区有价值，转投 ICML 消除了 venue fit 障碍。修复 seed 不一致和模板问题后可达 Accept (5/6)。\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-24T09:33:29.881156+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4118
}
```

</details>

---

### Assistant

_source line 216 · 2026-05-24T09:33:36.380787+00:00_

审稿报告已提交。

核心结论：Round 3 的两个 open warning（步数不对等 + TAWM 措辞）均已 RESOLVED，但数据更新引入了新的不一致问题——Methodology/Limitations 说 "4 seeds" 而 Results 报告 5 Walker seeds，且模板仍为 `corl_2026` 未更新为 ICML 格式。方法严谨性从 7/10 提升至 7.5/10，ICML 推荐 Weak Accept (4/6)，修复 seed 不一致和模板后可达 Accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 6

4 recorded events

### User

_source line 217 · 2026-05-24T09:35:06.650643+00:00_

[Round 4 审稿请求]:
## Step 2 交叉分享 — Reviewer 2 的 Round 4 完整审稿意见

请逐条回应，标注 [AGREE] 或 [REBUT]（附理由）。

---

### Reviewer 2 核心发现：

**1. [CRITICAL] 模板仍为 `corl_2026`**
PDF 页脚明确显示 CoRL。目标 venue 已改为 ICML 2026，以当前状态提交会被 desk reject。

**2. [CRITICAL] 缺少 ICML 必需的 Impact Statement**
ICML 2026 要求 Broader Impact / Ethics Statement，当前论文中没有。

**3. Venue fit 大幅改善**
从 CoRL 的 5/10 提升到 ICML 的 8/10。Diagnostic/negative-result 论文在 ICML 有先例（Henderson et al. 2018 等）。

**4. Round 3 具体审稿意见均已回应**
"structural factor" 弱化、detector 降级、training horizon 数据、baseline 值补充——均已处理。

**5. Overall: Weak Accept (4/6)**
Soundness 和 Originality 为 Good，Significance 偏 Fair。

---

### 你的交叉任务：

请特别关注以下问题，看你是否同意 R2 的判断：

1. **Impact Statement 缺失是否为 critical**？你的审稿中未提及此问题——是你判断不需要，还是遗漏了？
2. **R2 给 Significance 为 Fair**——你给了 3/4 (Good)。你是否仍维持你的评分？理由？
3. **Venue fit 8/10 vs 你的 8.5/10**——差异可忽略，但请确认你是否同意 R2 的 ICML fit 评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-24T09:36:02.519901+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 Round 4 意见的交叉回应\n\n---\n\n## 1. [CRITICAL] 模板仍为 `corl_2026`\n\n**[AGREE] R2**\n\n我在 Round 4 审稿中同样将此标记为 N-R4-5 [critical]。main.tex line 5 确认 `\\usepackage{corl_2026}`。这是 desk reject 风险，无争议。\n\n---\n\n## 2. [CRITICAL] 缺少 ICML 必需的 Impact Statement\n\n**[AGREE] R2 — 这是我的遗漏，不是判断不需要。**\n\n我在 Round 4 审稿中未提及 Impact Statement / Broader Impact 缺失，这是审查疏忽。ICML 2026 Reviewer Instructions 明确包含 \"Limitations assessment\" 和 \"Ethical Concerns\" 作为 review form 维度。虽然 ICML 2025/2026 对 Broader Impact 的要求不如 NeurIPS 那样硬性（NeurIPS 曾要求独立 Broader Impact section），但缺少任何形式的 ethical/societal impact 讨论确实是一个合规风险。\n\n具体来说：\n- 论文当前的 Limitations 段落（Conclusion 内的 `\\paragraph{}`）讨论了技术局限（seeds、architecture、reward scales），但**未涉及 broader impact**\n- 对于一篇诊断 RL failure mode 的论文，broader impact 可以自然地讨论：(a) 该发现对安全部署 world-model RL 的意义；(b) 负面结果公开发表对社区的价值；(c) 不存在明显的负面社会影响\n- 这段内容简短（3-5 句）但必须存在\n\n**结论**: R2 正确识别了这一遗漏。我将其严重度评估为 **warning 而非 critical**——因为 ICML 对此的执行力度不如模板格式那样严格（不会自动 desk reject），但缺失确实会被 reviewer 在 form 中标记。\n\n---\n\n## 3. Venue fit 大幅改善\n\n**[AGREE] R2**\n\n我给 8.5/10，R2 给 8/10，差异可忽略。我同意 R2 的核心判断：ICML 是显著更好的 venue。Diagnostic/negative-result 论文在 ICML 有明确先例。0.5 分的差异来自我对 factorial design 在 ICML methodology track 中价值的略高估计，不影响结论。\n\n**确认 ICML fit**: 同意 R2 的 8/10 评估。\n\n---\n\n## 4. Round 3 审稿意见回应\n\n**[AGREE] R2**\n\n与我的 Round 4 逐条检查结果一致：\n- \"structural factor\" → \"hypothesized structural factor\": [RESOLVED] ✓\n- Detector 降级 \"Preliminary diagnostic\" + CI: [RESOLVED] ✓\n- Training horizon 302K 数据: [RESOLVED] ✓\n- Baseline 值脚注: [PARTIALLY RESOLVED] ✓\n\n---\n\n## 5. Overall Weak Accept (4/6)\n\n**[AGREE] R2**\n\n我同样给出 Weak Accept (4/6)。\n\n---\n\n## 交叉任务专项回应\n\n### Q1: Impact Statement 缺失是否为 critical？\n\n如上所述，**这是我的遗漏**。我将其评估为 **high warning 而非 critical**：\n- Critical = desk reject 风险。ICML 对 Impact Statement 的缺失不会自动 desk reject（不同于模板格式违规）\n- 但 reviewer form 有 \"Ethical Concerns\" 和 \"Limitations\" 字段。完全缺失 broader impact 讨论会导致 reviewer 在这些字段给出负面标记\n- 修复成本极低（3-5 句话），应该立即添加\n\n### Q2: Significance — Fair vs Good？\n\n**我维持 Good (3/4)，但承认这是 borderline。**\n\n理由：\n1. **CIVO 作为 failure mode 的发现价值**: 任何计划在 DreamerV3 或类似架构中使用 temporal abstraction 的研究者都需要知道这个结果。这不是一个小众问题——temporal abstraction 在 world-model RL 中是活跃的研究方向（TAWM, Director 等近期工作）\n2. **Dual-critic convergence (ρ>0.999) 的 insight**: 这个发现超越了 CIVO 本身——它揭示了 pure-imagination training 中 Double Q pessimism 失效的结构性原因。这对任何在 imagination-based training 中使用 dual critic 的研究有广泛意义\n3. **四级干预层级的系统性 negative result**: 不仅展示了 \"什么不 work\"，更展示了 \"为什么不 work\"（gradient pathway redundancy, representation-level coupling）\n\nR2 给 Fair 的逻辑可能是：CIVO 是 locomotion-specific（2 环境），且无 actionable solution。这些都是合理的限制。但对 ICML 受众而言，systematic diagnostic methodology + structural insight 的组合达到了 Good 的门槛。\n\n**如果 R2 的 Fair 是基于 \"impact 局限于 DreamerV3 一个架构\"**，我部分同意——论文未验证其他 imagination-based 架构。但 DreamerV3 是该领域最广泛使用的 baseline，其失败模式分析本身有足够的 significance。\n\n**最终判断**: 维持 Good (3/4)，但认可 R2 的 Fair (2/4) 也是合理的。这属于 reviewer 间正常的评分分歧。\n\n### Q3: Venue fit 8/10 vs 8.5/10\n\n**接受 R2 的 8/10**。0.5 分差异无实质意义，我不坚持 8.5。两位 reviewer 一致认为 ICML 是合适的 venue。\n\n---\n\n## 两位 Reviewer 的共识与分歧总结\n\n| 维度 | R1 | R2 | 共识？ |\n|------|----|----|--------|\n| Overall | Weak Accept (4/6) | Weak Accept (4/6) | ✅ 完全一致 |\n| Soundness | Good (3/4) | Good (3/4) | ✅ 完全一致 |\n| Originality | Good (3/4) | Good (3/4) | ✅ 完全一致 |\n| Significance | **Good (3/4)** | **Fair (2/4)** | ⚠️ 分歧（见上） |\n| Presentation | Good (3/4) | Good (3/4) | ✅ 完全一致 |\n| 模板问题 | Critical | Critical | ✅ 完全一致 |\n| Impact Statement | 遗漏（现补 warning） | Critical | ⚠️ 严重度分歧 |\n| Venue fit (ICML) | 8.5→8/10 | 8/10 | ✅ 一致 |\n\n**共识**: 论文在方法论上 sound，转投 ICML 后 venue fit 合理，需修复模板 + Impact Statement + seed 数量不一致后可达 Accept。\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 Round 4 意见的交叉回应\n\n---\n\n## 1. [CRITICAL] 模板仍为 `corl_2026`\n\n**[AGREE] R2**\n\n我在 Round 4 审稿中同样将此标记为 N-R4-5 [critical]。main.tex line 5 确认 `\\usepackage{corl_2026}`。这是 desk reject 风险，无争议。\n\n---\n\n## 2. [CRITICAL] 缺少 ICML 必需的 Impact Statement\n\n**[AGREE] R2 — 这是我的遗漏，不是判断不需要。**\n\n我在 Round 4 审稿中未提及 Impact Statement / Broader Impact 缺失，这是审查疏忽。ICML 2026 Reviewer Instructions 明确包含 \"Limitations assessment\" 和 \"Ethical Concerns\" 作为 review form 维度。虽然 ICML 2025/2026 对 Broader Impact 的要求不如 NeurIPS 那样硬性（NeurIPS 曾要求独立 Broader Impact section），但缺少任何形式的 ethical/societal impact 讨论确实是一个合规风险。\n\n具体来说：\n- 论文当前的 Limitations 段落（Conclusion 内的 `\\paragraph{}`）讨论了技术局限（seeds、architecture、reward scales），但**未涉及 broader impact**\n- 对于一篇诊断 RL failure mode 的论文，broader impact 可以自然地讨论：(a) 该发现对安全部署 world-model RL 的意义；(b) 负面结果公开发表对社区的价值；(c) 不存在明显的负面社会影响\n- 这段内容简短（3-5 句）但必须存在\n\n**结论**: R2 正确识别了这一遗漏。我将其严重度评估为 **warning 而非 critical**——因为 ICML 对此的执行力度不如模板格式那样严格（不会自动 desk reject），但缺失确实会被 reviewer 在 form 中标记。\n\n---\n\n## 3. Venue fit 大幅改善\n\n**[AGREE] R2**\n\n我给 8.5/10，R2 给 8/10，差异可忽略。我同意 R2 的核心判断：ICML 是显著更好的 venue。Diagnostic/negative-result 论文在 ICML 有明确先例。0.5 分的差异来自我对 factorial design 在 ICML methodology track 中价值的略高估计，不影响结论。\n\n**确认 ICML fit**: 同意 R2 的 8/10 评估。\n\n---\n\n## 4. Round 3 审稿意见回应\n\n**[AGREE] R2**\n\n与我的 Round 4 逐条检查结果一致：\n- \"structural factor\" → \"hypothesized structural factor\": [RESOLVED] ✓\n- Detector 降级 \"Preliminary diagnostic\" + CI: [RESOLVED] ✓\n- Training horizon 302K 数据: [RESOLVED] ✓\n- Baseline 值脚注: [PARTIALLY RESOLVED] ✓\n\n---\n\n## 5. Overall Weak Accept (4/6)\n\n**[AGREE] R2**\n\n我同样给出 Weak Accept (4/6)。\n\n---\n\n## 交叉任务专项回应\n\n### Q1: Impact Statement 缺失是否为 critical？\n\n如上所述，**这是我的遗漏**。我将其评估为 **high warning 而非 critical**：\n- Critical = desk reject 风险。ICML 对 Impact Statement 的缺失不会自动 desk reject（不同于模板格式违规）\n- 但 reviewer form 有 \"Ethical Concerns\" 和 \"Limitations\" 字段。完全缺失 broader impact 讨论会导致 reviewer 在这些字段给出负面标记\n- 修复成本极低（3-5 句话），应该立即添加\n\n### Q2: Significance — Fair vs Good？\n\n**我维持 Good (3/4)，但承认这是 borderline。**\n\n理由：\n1. **CIVO 作为 failure mode 的发现价值**: 任何计划在 DreamerV3 或类似架构中使用 temporal abstraction 的研究者都需要知道这个结果。这不是一个小众问题——temporal abstraction 在 world-model RL 中是活跃的研究方向（TAWM, Director 等近期工作）\n2. **Dual-critic convergence (ρ>0.999) 的 insight**: 这个发现超越了 CIVO 本身——它揭示了 pure-imagination training 中 Double Q pessimism 失效的结构性原因。这对任何在 imagination-based training 中使用 dual critic 的研究有广泛意义\n3. **四级干预层级的系统性 negative result**: 不仅展示了 \"什么不 work\"，更展示了 \"为什么不 work\"（gradient pathway redundancy, representation-level coupling）\n\nR2 给 Fair 的逻辑可能是：CIVO 是 locomotion-specific（2 环境），且无 actionable solution。这些都是合理的限制。但对 ICML 受众而言，systematic diagnostic methodology + structural insight 的组合达到了 Good 的门槛。\n\n**如果 R2 的 Fair 是基于 \"impact 局限于 DreamerV3 一个架构\"**，我部分同意——论文未验证其他 imagination-based 架构。但 DreamerV3 是该领域最广泛使用的 baseline，其失败模式分析本身有足够的 significance。\n\n**最终判断**: 维持 Good (3/4)，但认可 R2 的 Fair (2/4) 也是合理的。这属于 reviewer 间正常的评分分歧。\n\n### Q3: Venue fit 8/10 vs 8.5/10\n\n**接受 R2 的 8/10**。0.5 分差异无实质意义，我不坚持 8.5。两位 reviewer 一致认为 ICML 是合适的 venue。\n\n---\n\n## 两位 Reviewer 的共识与分歧总结\n\n| 维度 | R1 | R2 | 共识？ |\n|------|----|----|--------|\n| Overall | Weak Accept (4/6) | Weak Accept (4/6) | ✅ 完全一致 |\n| Soundness | Good (3/4) | Good (3/4) | ✅ 完全一致 |\n| Originality | Good (3/4) | Good (3/4) | ✅ 完全一致 |\n| Significance | **Good (3/4)** | **Fair (2/4)** | ⚠️ 分歧（见上） |\n| Presentation | Good (3/4) | Good (3/4) | ✅ 完全一致 |\n| 模板问题 | Critical | Critical | ✅ 完全一致 |\n| Impact Statement | 遗漏（现补 warning） | Critical | ⚠️ 严重度分歧 |\n| Venue fit (ICML) | 8.5→8/10 | 8/10 | ✅ 一致 |\n\n**共识**: 论文在方法论上 sound，转投 ICML 后 venue fit 合理，需修复模板 + Impact Statement + seed 数量不一致后可达 Accept。\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-24T09:36:06.386497+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3866
}
```

</details>

---

### Assistant

_source line 220 · 2026-05-24T09:36:12.006098+00:00_

审稿报告已提交。两位 Reviewer 在 Overall (Weak Accept 4/6)、Soundness、Originality、Presentation 上完全一致。唯一实质分歧是 Significance（我给 Good，R2 给 Fair）——我维持 Good 但承认 borderline，主要基于 dual-critic convergence insight 和 systematic negative result 的 ICML 社区价值。我补充承认了 Impact Statement 遗漏是审查疏忽。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 7

56 recorded events

### User

_source line 221 · 2026-05-24T15:03:04.183113+00:00_

[Round 5 审稿请求]:
## Round 5 继续审稿 — Reviewer 1（方法严谨性 + 数据完整性验证）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: ICML 2026
**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf`
**Venue 要求**: 正文 8 页 + 无限 references/impact statement/appendix，double-blind，icml2026.sty 模板
**上轮评分**: Round 4 Weak Accept (6/10)

### 你的侧重
方法严谨性 + 数据完整性验证。本轮重点是**逐条验证 Round 4 的 8 个 open/in_progress issues 是否已修复**，并检查修改是否引入新问题。

### Round 4 Open/In-Progress Issues（逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由）

**CRITICAL (3)**:
1. **N-R4-1** 模板仍为 corl_2026 → 需切换 icml2026.sty | status: in_progress
2. **N-R4-2** 缺少 ICML Impact Statement → 需在 References 前添加 | status: in_progress
3. **N-R4-3** IQM 计算错误：results.tex 报告 IQM=175.2 (n=4 值)，n=5 正确值应为 148.8 | status: in_progress

**WARNING (4)**:
4. **R3-N-new-2** "gradient diversity" 术语无支撑证据 → results.tex:166 应弱化措辞 | status: in_progress | [复发×2轮]
5. **R3-N-new-3** ManiSkill/Cheetah baseline eval 值在 Table 1 中缺失 | status: in_progress | [复发×2轮]
6. **N-R4-4** Seed 数量叙述全文不一致（methodology 说4，results 说5，Figure 2 caption 漏 seed 5） | status: in_progress
7. **R2-N3** 纯诊断负面结果缺乏 actionable solution（ICML 下降级为 warning）| status: in_progress

**INFO (1)**:
8. **N-R4-5** "causal chain" 措辞 → 建议改为 "trace a pathway" | status: in_progress

### 额外检查
- 验证 Walker 5 seeds 的 IQM 计算是否正确（从 appendix 获取 5 个 eval 值，计算 25% trim IQM）
- 检查全文因果语言一致性（strongest predictor / hypothesized structural factor）
- 检查 LOEO AUROC 值（正文 vs appendix 一致性）
- 检查 Table 1 数值与 appendix 完整结果表的一致性
- 检查是否有新引入的问题

### 评分维度
Soundness (1-4), Presentation (1-4), Contribution (1-4), Overall (1-6), Confidence (1-5)
对每个 RESOLVED issue 给出验证依据（具体文件:行号）；对 STILL_OPEN 给出具体位置和原因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-24T15:03:27.839681+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf",
  "pages": "1-8",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf",
    "pages": "1-8",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-24T15:03:28.846891+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 433.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 530.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 481.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 457.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 453.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 494.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 468.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 461.9}], \"total_pages\": 24, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated
…[truncated 95 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1007
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-24T15:03:29.098266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-24T15:03:29.249357+00:00_

1	\documentclass{article}
2	
3	% xcolor with table option must be loaded before icml2026.sty (which loads xcolor internally)
4	\PassOptionsToPackage{table}{xcolor}
5	
6	\usepackage{hyperref}
7	\newcommand{\theHalgorithm}{\arabic{algorithm}}
8	\usepackage{icml2026}
9	
10	\usepackage[utf8]{inputenc}
11	\usepackage[T1]{fontenc}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{graphicx}
16	\graphicspath{{../../artifacts/}}
17	\usepackage{colortbl}
18	\usepackage{caption}
19	\usepackage{subcaption}
20	\usepackage{array}
21	\usepackage{enumitem}
22	\usepackage{wrapfig}
23	\usepackage{algorithm}
24	\usepackage{algorithmic}
25	
26	% Custom commands
27	\newcommand{\dt}{\mathrm{dt}}
28	\newcommand{\nve}{\mathrm{nve}}
29	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
30	\newcommand{\sgseval}{448.3}
31	\newcommand{\sgsnve}{1.66}
32	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
33	\newcommand{\ie}{\textit{i.e.}}
34	\newcommand{\eg}{\textit{e.g.}}
35	\newcommand{\cf}{\textit{cf.}}
36	\newcommand{\etal}{\textit{et al.}}
37	
38	\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}
39	
40	\begin{document}
41	
42	\twocolumn[
43	  \icmltitle{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\
44	  A Diagnostic Analysis of Variable-Rate DreamerV3}
45	
46	  \begin{icmlauthorlist}
47	    \icmlauthor{Anonymous Authors}{anon}
48	  \end{icmlauthorlist}
49	
50	  \icmlaffiliation{anon}{Anonymous Institution}
51	
52	  \icmlkeywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
53	
54	  \vskip 0.3in
55	]
56	
57	\printAffiliationsAndNotice{}
58	
59	\begin{abstract}
60	\input{sections/abstract_body}
61	\end{abstract}
62	
63	% --- INTRODUCTION ---
64	\input{sections/introduction}
65	
66	% --- RELATED WORK ---
67	\input{sections/related_work}
68	
69	% --- METHODOLOGY ---
70	
…[truncated 199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-24T15:03:39.289814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "offset": "78",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "offset": "78",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-24T15:03:39.742026+00:00_

78	% --- CONCLUSION ---
79	\input{sections/conclusion}
80	
81	\bibliographystyle{icml2026}
82	\bibliography{references}
83	
84	% --- APPENDIX ---
85	\appendix
86	\input{sections/appendix}
87	
88	\end{document}
89	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-24T15:03:39.742463+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-24T15:03:40.144424+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 27/30, AUROC${=}0.957$, LOEO cross-validated). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-24T15:03:40.195116+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-24T15:03:40.245890+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We identify trained $\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (27/30, AUROC${=}0.957$; LOEO cross-validated). No tested intervention reliably eliminates CIVO; in pure imagination, dual critics converge ($\rho > 0.999$), rendering Double Q pessimism ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work.
5	
6	\paragraph{Limitations.}
7	Our analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but does not test pixel-based observations, Atari benchmarks, or real-robot deployments where sensor noise and actuation latency introduce additional confounds.
8	All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.
9	We characterize CIVO under fixed-$\dt$ subsampling; learned temporal gates warrant separate study.
10	Statistical power is limited (4--5 seeds per configuration) \citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.988$) may require recalibration for different reward scales.
11	Code: upon acceptance.
12	\label{sec:limitations}
13	
14	\section*{Broader Impact Statement}
15	
16	This work contributes a diagnostic framework for identifying a failure mode in model-based reinforcement learning. By characterizing Conditioning-Induced Value Overestimation (CIVO), we aim to help practitioners detect and mitigate training instabilities in world-model-based agents before deployment. The frozen embedding diagnostic provides a low-cost preliminary check that could reduce wasted computation on silently failing training runs.
17	
18	We note several limitations regarding broader impact. First, our NVE-based detector is a proof-of-concept w
…[truncated 459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-24T15:03:50.344278+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-24T15:03:50.445497+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that trace a predictive pathway from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
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
33	049 & StackCube-v1 & trn 
…[truncated 12108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-24T15:04:06.355731+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool call

_source line 235 · 2026-05-24T15:04:06.356316+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-24T15:04:06.457191+00:00_

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
…[truncated 5133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-24T15:04:06.458158+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-24T15:04:37.454635+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf",
  "pages": "9-12",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf",
    "pages": "9-12",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-24T15:04:38.962362+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 464.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 498.9}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 492.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 436.3}], \"total_pages\": 24, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1507
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-24T15:04:39.063185+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Becker|becker|ehmck",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Becker|becker|ehmck",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-24T15:04:39.164052+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-24T15:04:43.635016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-24T15:04:44.137197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-24T15:04:44.340027+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-24T15:04:44.894194+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-24T15:04:48.459968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool call

_source line 247 · 2026-05-24T15:04:48.811861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-24T15:04:49.013799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-24T15:04:49.566754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-24T15:04:55.588677+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf",
  "pages": "18-20",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf",
    "pages": "18-20",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-24T15:04:55.890180+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p18.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 333.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p19.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 406.6}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p20.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 159.9}], \"total_pages\": 24, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-24T15:05:00.208491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-24T15:05:00.763298+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---

### Tool call

_source line 254 · 2026-05-24T15:05:00.763797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-24T15:05:01.169895+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-24T15:05:26.270937+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "IQM|148\\\\.8|interquartile mean",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "IQM|148\\\\.8|interquartile mean",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-24T15:05:26.321794+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-80-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-81-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:82:The trained $\dt$-embedding precedes CIVO in all five Walker Walk seeds (peak NVE $1.53$--$4.72\times$), universally degrading performance to below 30\% of baseline (IQM $148.8$, $n{=}5$; \citealt{agarwal2021precipice}). Combined with Cheetah Run (\S\ref{sec:f6}), CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 6/7 suffering sustained policy collapse, 1/7 self-correcting (Appendix~\ref{sec:seed_divergence}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-83-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-84-%% ============================================================

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 258 · 2026-05-24T15:05:32.748192+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "008d.*seed|008d.*s[0-9]|exp_059|seed.5|five.*seed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "1",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "008d.*seed|008d.*s[0-9]|exp_059|seed.5|five.*seed",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "1",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-24T15:05:32.798834+00:00_

5-
6:Table~\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7-
--
25-\rowcolor{gray!15}
26:008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\heartsuit$ & 4.12$\times$ & Full collapse \\
27-\rowcolor{gray!15}
--
29-\rowcolor{gray!15}
30:008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31-\rowcolor{gray!15}
32:008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33-\rowcolor{gray!15}
--
244-
245:[Omitted long matching line]
246-
--
268-
269:[Omitted long matching line]
270-
--
387-\paragraph{Evidence A: exposure is necessary (exp\_008a).}
388:[Omitted long matching line]
389-
--
438-
439:Neither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\nve < 0.93\times$ (\S\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\nve = 4.12\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\ 009c: 148.3) but neither exhibits $\nve > 1.5\times$; low evaluation alone does not indicate CIVO.
440-
--

[Showing results with pagination = limit: 30]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 260 · 2026-05-24T15:05:42.568891+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "009b|008d.*s0|008d.*s2|Factorial.*s[02]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "1",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "009b|008d.*s0|008d.*s2|Factorial.*s[02]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "1",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-24T15:05:42.619648+00:00_

5-
6:Table~\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7-
--
27-\rowcolor{gray!15}
28:009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29-\rowcolor{gray!15}
--
120-
121:[Omitted long matching line]
122-
--
140-008e\_v3\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\
141:009b         & 1.62 & transient CIVO & $-$ & $+$ \\
142-001          & 1.00 & non-CIVO       & $-$ & $-$ \\
--
223-\begin{enumerate}[nosep,leftmargin=*]
224:\item \textbf{Maximum recall.} The $1.5\times$ threshold achieves 100\% recall, detecting all five CIVO cases including the transient case (009b, $\nve = 1.62\times$). Raising the threshold to $1.7\times$ loses 009b, dropping recall to 80.0\%.
225-\item \textbf{Best F1.} At $1.5\times$, F1 = 90.9\%, the highest among all tested thresholds for B2. The single false positive (008e\_v3\_s2) is mechanistically identifiable as IRD rather than CIVO.
--

[Showing results with pagination = limit: 20]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-24T15:05:47.842850+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "059|exp_059|Factorial.*s0|008d_s0|4\\.72",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "1",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "059|exp_059|Factorial.*s0|008d_s0|4\\.72",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "1",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-24T15:05:47.943909+00:00_

33-\rowcolor{gray!15}
34:059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\times$ & Collapse$^\dagger$ \\
35-008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
--
89-$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
90:$^\dagger$ NVE self-corrected ($4.72\times$ $\to$ $1.22\times$) but policy did not recover (eval 10.5\% of baseline).\\
91-$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
--
108-\midrule
109:Locomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\times$) \\
110-Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\times$) \\
--
124-
125:Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eleven factorial experiments (including four 008e\_v3 seeds and exp\_059). Experiments are sorted by descending NVE. Experiment 008e\_v3\_s2 exhibits elevated NVE ($3.78\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\_v3\_s3 exhibits CIVO with NVE $4.02\times$ despite $\Delta t{=}1$ imagination.
126-
--
136-006          & 4.83 & sustained CIVO & $+$ & $+$ \\
137:059          & 4.72 & self-correcting CIVO & $-$ & $+$ \\
138-008d         & 4.12 & sustained CIVO & $+$ & $+$ \\
--

[Showing results with pagination = limit: 20]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-24T15:06:45.578686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-24T15:06:45.579115+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_1_3ba83a7f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 266 · 2026-05-24T15:06:46.131092+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 267 · 2026-05-24T15:06:46.181688+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_1_3ba83a7f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 268 · 2026-05-24T15:06:53.261664+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf",
  "pages": "1",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf",
    "pages": "1",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 269 · 2026-05-24T15:06:53.412866+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 433.0}], \"total_pages\": 24, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 270 · 2026-05-24T15:06:58.786706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 271 · 2026-05-24T15:06:59.339908+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 272 · 2026-05-24T15:09:13.401563+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Round 5 审稿报告 — Reviewer 1（方法严谨性 + 数据完整性验证）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL\"\n**目标 Venue**: ICML 2026\n**上轮评分**: Weak Accept (4/6)\n\n---\n\n## 总体评分\n\n**Soundness**: 3/4 (Good)\n**Presentation**: 3/4 (Good)\n**Significance**: 3/4 (Good)\n**Originality**: 3/4 (Good)\n**Overall Recommendation**: 5/6 (Accept)\n**Confidence**: 4/5 (Confident but not certain)\n\n**一句话总结**: Round 4 的 3 个 critical issues 全部修复（模板切换 ICML、Impact Statement 添加、IQM 计算更正），4 个 warning 中 3 个 RESOLVED / 1 个 PARTIALLY RESOLVED。论文现已达到 ICML 投稿标准，从 Weak Accept 升至 Accept。\n\n---\n\n## 逐条 Issue 验证\n\n### CRITICAL Issues (3/3 RESOLVED)\n\n---\n\n#### 1. N-R4-1 [CRITICAL]: 模板仍为 corl_2026\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `main.tex:8`: `\\usepackage{icml2026}` ✓\n- `main.tex:38`: `\\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}` ✓\n- `main.tex:81`: `\\bibliographystyle{icml2026}` ✓\n- PDF page 1 页脚: \"Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.\" ✓\n- 双栏排版、`\\icmltitle`/`\\icmlauthor` 格式正确 ✓\n- Anonymous: \"Anonymous Authors¹\" ✓\n\n**小瑕疵**: PDF page 1 脚注显示 \"AUTHORERR: Missing \\icmlcorrespondingauthor\"。这是 ICML 模板在匿名模式下的已知行为（不需要指定 corresponding author），但提交时应确认 camera-ready 阶段能正确渲染。不影响 review。\n\n---\n\n#### 2. N-R4-2 [CRITICAL]: 缺少 ICML Impact Statement\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `conclusion.tex:14`: `\\section*{Broader Impact Statement}` ✓\n- 内容覆盖两个维度：\n  - **正面影响** (line 16): \"help practitioners detect and mitigate training instabilities...reduce wasted computation on silently failing training runs\"\n  - **风险与局限** (line 18): NVE detector 的 small-sample limitation（\"premature reliance on it could lead to unnecessary interventions\"）、simulation-only 实验无 real-world safety risk\n- 篇幅合理（2 段，~100 词）✓\n- 位置正确：在 Conclusion/Limitations 之后、Bibliography 之前 ✓\n\n---\n\n#### 3. N-R4-3 [CRITICAL]: IQM 计算错误（175.2 → 148.8）\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `results.tex:82`: \"IQM $148.8$, $n{=}5$\" ✓\n\n**IQM 独立验证**（从 Appendix Table 3 提取 5 个 Walker Walk trained-embedding seeds 的 eval@final）:\n\n| Seed | Exp | Eval@final | NVE |\n|------|-----|-----------|-----|\n| s1 | 008d | 82.8 @55K | 4.12× |\n| s2 | 009b | 267.9 @105K | 1.62× |\n| s3 | 008d_s3 | 268 @105K | 1.53× |\n| s4 | 008d_s4 | 63.6 @105K | 4.62× |\n| s5 | 059 | 95.8 @105K | 4.72× |\n\n排序: [63.6, 82.8, 95.8, 267.9, 268]\n\nIQM (25% trimmed mean, k=floor(0.25×5)=1, 去掉两端各 1 个值):\n= (82.8 + 95.8 + 267.9) / 3 = 446.5 / 3 = **148.83 ≈ 148.8** ✓\n\n**Peak NVE range**: 1.53--4.72× ✓（最小 008d_s3=1.53×，最大 059=4.72×）\n\n**旧值回溯验证**: n=4 时排序 [63.6, 82.8, 267.9, 268]，IQM = (82.8+267.9)/2 = 175.35 ≈ 175.2 ✓（Round 4 正确指出了不一致）\n\n---\n\n### WARNING Issues (3/4 RESOLVED, 1 PARTIALLY)\n\n---\n\n#### 4. R3-N-new-2 [WARNING, 复发×2轮]: \"gradient diversity\" 术语无支撑\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `results.tex:167`（Round 4）: ~~\"may instead regularize through gradient diversity\"~~\n- `results.tex:167`（Round 5）: \"may provide regularization through mechanisms that remain to be characterized (Appendix G)\" ✓\n\n新措辞完全移除了无支撑的 \"gradient diversity\" 术语，改为承认机制未知。Appendix G.3 的 \"open question + early-training divergence hypothesis\" 与主文措辞一致。\n\n---\n\n#### 5. R3-N-new-3 [WARNING, 复发×2轮]: ManiSkill/Cheetah baseline eval 值缺失\n**[PARTIALLY RESOLVED]** ⚠️\n\n**验证依据**:\n- `results.tex:47`: \"Baselines: Walker 915.7 (row 001); Cheetah ${\\sim}409$ (5-seed mean at 105K); PickCube via exp\\_019a\\_v2; StackCube/PegInsertion not separately measured.\"\n\n**改善**: Cheetah baseline 从 \"~320\" 更新为 \"~409 (5-seed mean at 105K)\"——更精确且说明了来源\n\n**残留问题**:\n- PickCube: \"via exp_019a_v2\" 仍未给出具体 eval 值\n- StackCube/PegInsertion: \"not separately measured\" 仍然缺失\n\n**影响评估**: 对论文核心论点影响极小。ManiSkill 环境的论点是 CIVO 不存在（frozen controls match trained），baseline 值对此判断不必要。但如果读者想知道 dt-conditioning 对 manipulation 任务的 overall degradation 程度，这些信息是缺失的。\n\n**降级为 info**: 鉴于已经复发 3 轮且对核心论点无影响，建议不再追踪此 issue 作为 action item。\n\n---\n\n#### 6. N-R4-4 [WARNING]: Seed 数量叙述全文不一致\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `methodology.tex:32`: \"Key configurations use 4--5 seeds (Walker Walk uses 5 seeds to strengthen statistical power; other environments use 2--4 seeds)\" ✓\n- `conclusion.tex:10`: \"Statistical power is limited (4--5 seeds per configuration)\" ✓\n- `results.tex:78` (Figure 2 caption): \"seeds~4 and~5 data in Table~\\ref{tab:complete_results}\" ✓\n- `results.tex:82`: \"all five Walker Walk seeds...IQM $148.8$, $n{=}5$\" ✓\n\n全文 seed 数量叙述现在一致：Walker 5 seeds，其他环境 2-4 seeds，统称 \"4-5 seeds per configuration\"。\n\n---\n\n#### 7. R2-N3 [WARNING→info]: 纯诊断缺乏 actionable solution\n**[RESOLVED — 在 ICML 语境下不再构成独立问题]** ✅\n\n论文作为 ICML diagnostic/negative-result paper，其 contribution 模式是合理的：\n- Failure mode identification + characterization（而非 solution）\n- Frozen embedding 作为 practical workaround（71% prevention rate）\n- Wide dual-critic 作为 architectural mitigation（3/4 Walker）\n- NVE detector 作为 preliminary monitoring tool\n\nICML 历史上接受此类 diagnostic 贡献（Henderson et al. 2018; Engstrom et al. 2019 等）。不再单独追踪。\n\n---\n\n### INFO Issues (1/1 RESOLVED)\n\n---\n\n#### 8. N-R4-5 [INFO]: \"causal chain\" 措辞\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `results.tex:4`（Round 4）: ~~\"establish a causal chain\"~~\n- `results.tex:4`（Round 5）: \"trace a predictive pathway from trained temporal conditioning to pathological value dynamics\" ✓\n\n措辞恰当：\"predictive pathway\" 传达了 findings 之间的逻辑关联，同时避免了因果声明。\n\n---\n\n## 额外检查\n\n### 全文因果语言一致性\n\n| 位置 | 措辞 | 评估 |\n|------|------|------|\n| Abstract | \"identify...as the strongest predictor\" | ✓ 合理 |\n| Abstract | \"a hypothesized structural factor\" | ✓ 适当弱化 |\n| Introduction line 6 | \"we isolate the combination...as the strongest predictor\" | ⚠️ \"isolate\" 仍在，但用于描述 factorial design 的方法论操作（设计就是为了 isolate variables），在此语境下可接受 |\n| Introduction C1 | \"We identify CIVO...and isolate trained dt-embedding\" | ⚠️ 同上，方法论语言 |\n| Results line 4 | \"trace a predictive pathway\" | ✓ 已修正 |\n| Results line 74 | \"The factorial design isolates trained dt-embedding as the strongest predictor\" | ✓ 方法论语言 |\n| Conclusion | \"hypothesized structural factor\" | ✓ |\n\n**评估**: \"isolate\" 在 Introduction 和 Results 中作为 factorial analysis 的方法论术语使用是合理的——factorial design 的目的就是 isolate variables。与 \"causal factor\" 或 \"causal chain\" 不同，\"isolate\" 不做因果声明。全文因果语言总体一致。\n\n### LOEO AUROC 一致性\n\n| 位置 | 值 | 一致？ |\n|------|-----|--------|\n| methodology.tex:38 | 0.988 | ✓ |\n| conclusion.tex:10 | 0.988 | ✓ |\n\n### 27/30 和 AUROC=0.957 一致性\n\n| 位置 | 27/30 | 0.957 | ✓ |\n|------|-------|-------|---|\n| Abstract | ✓ | ✓ | ✓ |\n| Introduction | ✓ | ✓ | ✓ |\n| Methodology 3.4 | ✓ | ✓ | ✓ |\n| Results 4.2 | ✓ | ✓ | ✓ |\n| Discussion | — | ✓ | ✓ |\n| Conclusion | ✓ | ✓ | ✓ |\n\n全文数字一致。\n\n### Table 1 与 Appendix 完整结果表一致性\n\n| 条目 | Table 1 | Appendix Table 3 | 一致？ |\n|------|---------|------------------|--------|\n| 001 baseline | 915.7 @105K | 915.7 @105K | ✓ |\n| 008d | 82.8 @55K, 4.12× | 82.8 @55K♥, 4.12× | ✓ |\n| 008f | 503.0, 0.97× | 503.0, 0.97× | ✓ |\n| 010b Cheetah | 51.7, 8.27× | 51.7, 8.27× | ✓ |\n| 059 (new s5) | — (not in Table 1) | 95.8, 4.72× | ✓ (Table 1 只含 key configs) |\n\n### 是否引入新问题？\n\n**N-R5-1 [info]: Becker-Ehmck 2023 仍未引用**\n- Grep 确认全文无 \"Becker\" 或 \"ehmck\" 匹配\n- R2 在 Round 2, 3, 4 均指出此遗漏\n- 如果 Becker-Ehmck 2023 确实是 temporal abstraction in model-based RL 的直接相关工作，四轮不修复可能引起 reviewer/AC 注意\n- 但这是 R2 的 concern，我无法独立判断该引用的相关性等级\n\n**N-R5-2 [info]: PDF 脚注 \"AUTHORERR\"**\n- Page 1 脚注显示 \"AUTHORERR: Missing \\icmlcorrespondingauthor\"\n- 这是 icml2026.sty 匿名模式的已知行为，不影响 review\n- Camera-ready 阶段需添加 `\\icmlcorrespondingauthor{}` 修复\n\n**无新的 critical 或 warning 问题**。\n\n---\n\n## Issue 状态汇总\n\n| # | Issue | Round 4 状态 | Round 5 状态 | 验证文件:行号 |\n|---|-------|-------------|-------------|-------------|\n| 1 | 模板 corl→icml | CRITICAL | **[RESOLVED]** | main.tex:8, PDF footer |\n| 2 | Impact Statement | CRITICAL | **[RESOLVED]** | conclusion.tex:14-18 |\n| 3 | IQM 175.2→148.8 | CRITICAL | **[RESOLVED]** | results.tex:82, 独立计算验证 |\n| 4 | \"gradient diversity\" | WARNING ×2 | **[RESOLVED]** | results.tex:167 |\n| 5 | Baseline vals | WARNING ×2 | **[PARTIAL→info]** | results.tex:47 |\n| 6 | Seed 数量不一致 | WARNING | **[RESOLVED]** | methodology.tex:32, conclusion.tex:10, results.tex:78 |\n| 7 | Actionable solution | WARNING | **[RESOLVED]** | ICML 语境下合理 |\n| 8 | \"causal chain\" | INFO | **[RESOLVED]** | results.tex:4 |\n\n**7/8 RESOLVED, 1 降级为 info (baseline vals)**\n**0 个新 critical/warning**\n\n---\n\n## 方法严谨性总评\n\n**评分: 8/10（ICML 标准，Round 4 为 7.5/10）**\n\n提升 0.5 分原因:\n- IQM 计算已更正并通过独立验证（148.8, n=5）\n- Seed 数量叙述全文一致（4-5 seeds）\n- \"gradient diversity\" 无支撑术语已移除\n- 因果语言一致性达到可接受水平\n\n未达 9/10 原因:\n- 仍为 4-5 seeds（ICML 标准下 adequate 但非 strong；elite RL 论文用 10+ seeds）\n- 2 个运动环境的 CIVO 验证覆盖度有限（though honestly reported）\n- TAWM/MPC 对比仍为 hypothetical（though appropriately framed）\n\n---\n\n## ICML Overall Recommendation: Accept (5/6)\n\n**升级理由**（从 Round 4 Weak Accept 4/6 → Accept 5/6）：\n\n1. **所有 critical issues 已修复**: 模板、Impact Statement、IQM 计算三个 blocking 问题全部解决\n2. **数据完整性验证通过**: IQM 148.8 经独立计算确认正确；27/30, AUROC=0.957, LOEO=0.988 全文一致\n3. **方法论措辞到位**: \"strongest predictor\"（非 causal factor）、\"hypothesized structural factor\"（非 the structural factor）、\"trace a predictive pathway\"（非 causal chain）、\"mechanisms that remain to be characterized\"（非 gradient diversity）\n4. **ICML venue fit 良好**: Diagnostic negative-result paper with systematic factorial design, well-suited for ICML methodology track\n5. **残留 issues 均为 info 级**: ManiSkill baseline 未测量、Becker-Ehmck 未引用——均不影响接收决定\n\n**Confidence 4/5**: 我对方法论评估有高度信心（factorial design, IQM, AUROC 均已独立验证），但对 CIVO 的 broader significance（是否足够 important for ICML accept threshold）略有不确定。\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Round 5 审稿报告 — Reviewer 1（方法严谨性 + 数据完整性验证）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL\"\n**目标 Venue**: ICML 2026\n**上轮评分**: Weak Accept (4/6)\n\n---\n\n## 总体评分\n\n**Soundness**: 3/4 (Good)\n**Presentation**: 3/4 (Good)\n**Significance**: 3/4 (Good)\n**Originality**: 3/4 (Good)\n**Overall Recommendation**: 5/6 (Accept)\n**Confidence**: 4/5 (Confident but not certain)\n\n**一句话总结**: Round 4 的 3 个 critical issues 全部修复（模板切换 ICML、Impact Statement 添加、IQM 计算更正），4 个 warning 中 3 个 RESOLVED / 1 个 PARTIALLY RESOLVED。论文现已达到 ICML 投稿标准，从 Weak Accept 升至 Accept。\n\n---\n\n## 逐条 Issue 验证\n\n### CRITICAL Issues (3/3 RESOLVED)\n\n---\n\n#### 1. N-R4-1 [CRITICAL]: 模板仍为 corl_2026\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `main.tex:8`: `\\usepackage{icml2026}` ✓\n- `main.tex:38`: `\\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}` ✓\n- `main.tex:81`: `\\bibliographystyle{icml2026}` ✓\n- PDF page 1 页脚: \"Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.\" ✓\n- 双栏排版、`\\icmltitle`/`\\icmlauthor` 格式正确 ✓\n- Anonymous: \"Anonymous Authors¹\" ✓\n\n**小瑕疵**: PDF page 1 脚注显示 \"AUTHORERR: Missing \\icmlcorrespondingauthor\"。这是 ICML 模板在匿名模式下的已知行为（不需要指定 corresponding author），但提交时应确认 camera-ready 阶段能正确渲染。不影响 review。\n\n---\n\n#### 2. N-R4-2 [CRITICAL]: 缺少 ICML Impact Statement\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `conclusion.tex:14`: `\\section*{Broader Impact Statement}` ✓\n- 内容覆盖两个维度：\n  - **正面影响** (line 16): \"help practitioners detect and mitigate training instabilities...reduce wasted computation on silently failing training runs\"\n  - **风险与局限** (line 18): NVE detector 的 small-sample limitation（\"premature reliance on it could lead to unnecessary interventions\"）、simulation-only 实验无 real-world safety risk\n- 篇幅合理（2 段，~100 词）✓\n- 位置正确：在 Conclusion/Limitations 之后、Bibliography 之前 ✓\n\n---\n\n#### 3. N-R4-3 [CRITICAL]: IQM 计算错误（175.2 → 148.8）\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `results.tex:82`: \"IQM $148.8$, $n{=}5$\" ✓\n\n**IQM 独立验证**（从 Appendix Table 3 提取 5 个 Walker Walk trained-embedding seeds 的 eval@final）:\n\n| Seed | Exp | Eval@final | NVE |\n|------|-----|-----------|-----|\n| s1 | 008d | 82.8 @55K | 4.12× |\n| s2 | 009b | 267.9 @105K | 1.62× |\n| s3 | 008d_s3 | 268 @105K | 1.53× |\n| s4 | 008d_s4 | 63.6 @105K | 4.62× |\n| s5 | 059 | 95.8 @105K | 4.72× |\n\n排序: [63.6, 82.8, 95.8, 267.9, 268]\n\nIQM (25% trimmed mean, k=floor(0.25×5)=1, 去掉两端各 1 个值):\n= (82.8 + 95.8 + 267.9) / 3 = 446.5 / 3 = **148.83 ≈ 148.8** ✓\n\n**Peak NVE range**: 1.53--4.72× ✓（最小 008d_s3=1.53×，最大 059=4.72×）\n\n**旧值回溯验证**: n=4 时排序 [63.6, 82.8, 267.9, 268]，IQM = (82.8+267.9)/2 = 175.35 ≈ 175.2 ✓（Round 4 正确指出了不一致）\n\n---\n\n### WARNING Issues (3/4 RESOLVED, 1 PARTIALLY)\n\n---\n\n#### 4. R3-N-new-2 [WARNING, 复发×2轮]: \"gradient diversity\" 术语无支撑\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `results.tex:167`（Round 4）: ~~\"may instead regularize through gradient diversity\"~~\n- `results.tex:167`（Round 5）: \"may provide regularization through mechanisms that remain to be characterized (Appendix G)\" ✓\n\n新措辞完全移除了无支撑的 \"gradient diversity\" 术语，改为承认机制未知。Appendix G.3 的 \"open question + early-training divergence hypothesis\" 与主文措辞一致。\n\n---\n\n#### 5. R3-N-new-3 [WARNING, 复发×2轮]: ManiSkill/Cheetah baseline eval 值缺失\n**[PARTIALLY RESOLVED]** ⚠️\n\n**验证依据**:\n- `results.tex:47`: \"Baselines: Walker 915.7 (row 001); Cheetah ${\\sim}409$ (5-seed mean at 105K); PickCube via exp\\_019a\\_v2; StackCube/PegInsertion not separately measured.\"\n\n**改善**: Cheetah baseline 从 \"~320\" 更新为 \"~409 (5-seed mean at 105K)\"——更精确且说明了来源\n\n**残留问题**:\n- PickCube: \"via exp_019a_v2\" 仍未给出具体 eval 值\n- StackCube/PegInsertion: \"not separately measured\" 仍然缺失\n\n**影响评估**: 对论文核心论点影响极小。ManiSkill 环境的论点是 CIVO 不存在（frozen controls match trained），baseline 值对此判断不必要。但如果读者想知道 dt-conditioning 对 manipulation 任务的 overall degradation 程度，这些信息是缺失的。\n\n**降级为 info**: 鉴于已经复发 3 轮且对核心论点无影响，建议不再追踪此 issue 作为 action item。\n\n---\n\n#### 6. N-R4-4 [WARNING]: Seed 数量叙述全文不一致\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `methodology.tex:32`: \"Key configurations use 4--5 seeds (Walker Walk uses 5 seeds to strengthen statistical power; other environments use 2--4 seeds)\" ✓\n- `conclusion.tex:10`: \"Statistical power is limited (4--5 seeds per configuration)\" ✓\n- `results.tex:78` (Figure 2 caption): \"seeds~4 and~5 data in Table~\\ref{tab:complete_results}\" ✓\n- `results.tex:82`: \"all five Walker Walk seeds...IQM $148.8$, $n{=}5$\" ✓\n\n全文 seed 数量叙述现在一致：Walker 5 seeds，其他环境 2-4 seeds，统称 \"4-5 seeds per configuration\"。\n\n---\n\n#### 7. R2-N3 [WARNING→info]: 纯诊断缺乏 actionable solution\n**[RESOLVED — 在 ICML 语境下不再构成独立问题]** ✅\n\n论文作为 ICML diagnostic/negative-result paper，其 contribution 模式是合理的：\n- Failure mode identification + characterization（而非 solution）\n- Frozen embedding 作为 practical workaround（71% prevention rate）\n- Wide dual-critic 作为 architectural mitigation（3/4 Walker）\n- NVE detector 作为 preliminary monitoring tool\n\nICML 历史上接受此类 diagnostic 贡献（Henderson et al. 2018; Engstrom et al. 2019 等）。不再单独追踪。\n\n---\n\n### INFO Issues (1/1 RESOLVED)\n\n---\n\n#### 8. N-R4-5 [INFO]: \"causal chain\" 措辞\n**[RESOLVED]** ✅\n\n**验证依据**:\n- `results.tex:4`（Round 4）: ~~\"establish a causal chain\"~~\n- `results.tex:4`（Round 5）: \"trace a predictive pathway from trained temporal conditioning to pathological value dynamics\" ✓\n\n措辞恰当：\"predictive pathway\" 传达了 findings 之间的逻辑关联，同时避免了因果声明。\n\n---\n\n## 额外检查\n\n### 全文因果语言一致性\n\n| 位置 | 措辞 | 评估 |\n|------|------|------|\n| Abstract | \"identify...as the strongest predictor\" | ✓ 合理 |\n| Abstract | \"a hypothesized structural factor\" | ✓ 适当弱化 |\n| Introduction line 6 | \"we isolate the combination...as the strongest predictor\" | ⚠️ \"isolate\" 仍在，但用于描述 factorial design 的方法论操作（设计就是为了 isolate variables），在此语境下可接受 |\n| Introduction C1 | \"We identify CIVO...and isolate trained dt-embedding\" | ⚠️ 同上，方法论语言 |\n| Results line 4 | \"trace a predictive pathway\" | ✓ 已修正 |\n| Results line 74 | \"The factorial design isolates trained dt-embedding as the strongest predictor\" | ✓ 方法论语言 |\n| Conclusion | \"hypothesized structural factor\" | ✓ |\n\n**评估**: \"isolate\" 在 Introduction 和 Results 中作为 factorial analysis 的方法论术语使用是合理的——factorial design 的目的就是 isolate variables。与 \"causal factor\" 或 \"causal chain\" 不同，\"isolate\" 不做因果声明。全文因果语言总体一致。\n\n### LOEO AUROC 一致性\n\n| 位置 | 值 | 一致？ |\n|------|-----|--------|\n| methodology.tex:38 | 0.988 | ✓ |\n| conclusion.tex:10 | 0.988 | ✓ |\n\n### 27/30 和 AUROC=0.957 一致性\n\n| 位置 | 27/30 | 0.957 | ✓ |\n|------|-------|-------|---|\n| Abstract | ✓ | ✓ | ✓ |\n| Introduction | ✓ | ✓ | ✓ |\n| Methodology 3.4 | ✓ | ✓ | ✓ |\n| Results 4.2 | ✓ | ✓ | ✓ |\n| Discussion | — | ✓ | ✓ |\n| Conclusion | ✓ | ✓ | ✓ |\n\n全文数字一致。\n\n### Table 1 与 Appendix 完整结果表一致性\n\n| 条目 | Table 1 | Appendix Table 3 | 一致？ |\n|------|---------|------------------|--------|\n| 001 baseline | 915.7 @105K | 915.7 @105K | ✓ |\n| 008d | 82.8 @55K, 4.12× | 82.8 @55K♥, 4.12× | ✓ |\n| 008f | 503.0, 0.97× | 503.0, 0.97× | ✓ |\n| 010b Cheetah | 51.7, 8.27× | 51.7, 8.27× | ✓ |\n| 059 (new s5) | — (not in Table 1) | 95.8, 4.72× | ✓ (Table 1 只含 key configs) |\n\n### 是否引入新问题？\n\n**N-R5-1 [info]: Becker-Ehmck 2023 仍未引用**\n- Grep 确认全文无 \"Becker\" 或 \"ehmck\" 匹配\n- R2 在 Round 2, 3, 4 均指出此遗漏\n- 如果 Becker-Ehmck 2023 确实是 temporal abstraction in model-based RL 的直接相关工作，四轮不修复可能引起 reviewer/AC 注意\n- 但这是 R2 的 concern，我无法独立判断该引用的相关性等级\n\n**N-R5-2 [info]: PDF 脚注 \"AUTHORERR\"**\n- Page 1 脚注显示 \"AUTHORERR: Missing \\icmlcorrespondingauthor\"\n- 这是 icml2026.sty 匿名模式的已知行为，不影响 review\n- Camera-ready 阶段需添加 `\\icmlcorrespondingauthor{}` 修复\n\n**无新的 critical 或 warning 问题**。\n\n---\n\n## Issue 状态汇总\n\n| # | Issue | Round 4 状态 | Round 5 状态 | 验证文件:行号 |\n|---|-------|-------------|-------------|-------------|\n| 1 | 模板 corl→icml | CRITICAL | **[RESOLVED]** | main.tex:8, PDF footer |\n| 2 | Impact Statement | CRITICAL | **[RESOLVED]** | conclusion.tex:14-18 |\n| 3 | IQM 175.2→148.8 | CRITICAL | **[RESOLVED]** | results.tex:82, 独立计算验证 |\n| 4 | \"gradient diversity\" | WARNING ×2 | **[RESOLVED]** | results.tex:167 |\n| 5 | Baseline vals | WARNING ×2 | **[PARTIAL→info]** | results.tex:47 |\n| 6 | Seed 数量不一致 | WARNING | **[RESOLVED]** | methodology.tex:32, conclusion.tex:10, results.tex:78 |\n| 7 | Actionable solution | WARNING | **[RESOLVED]** | ICML 语境下合理 |\n| 8 | \"causal chain\" | INFO | **[RESOLVED]** | results.tex:4 |\n\n**7/8 RESOLVED, 1 降级为 info (baseline vals)**\n**0 个新 critical/warning**\n\n---\n\n## 方法严谨性总评\n\n**评分: 8/10（ICML 标准，Round 4 为 7.5/10）**\n\n提升 0.5 分原因:\n- IQM 计算已更正并通过独立验证（148.8, n=5）\n- Seed 数量叙述全文一致（4-5 seeds）\n- \"gradient diversity\" 无支撑术语已移除\n- 因果语言一致性达到可接受水平\n\n未达 9/10 原因:\n- 仍为 4-5 seeds（ICML 标准下 adequate 但非 strong；elite RL 论文用 10+ seeds）\n- 2 个运动环境的 CIVO 验证覆盖度有限（though honestly reported）\n- TAWM/MPC 对比仍为 hypothetical（though appropriately framed）\n\n---\n\n## ICML Overall Recommendation: Accept (5/6)\n\n**升级理由**（从 Round 4 Weak Accept 4/6 → Accept 5/6）：\n\n1. **所有 critical issues 已修复**: 模板、Impact Statement、IQM 计算三个 blocking 问题全部解决\n2. **数据完整性验证通过**: IQM 148.8 经独立计算确认正确；27/30, AUROC=0.957, LOEO=0.988 全文一致\n3. **方法论措辞到位**: \"strongest predictor\"（非 causal factor）、\"hypothesized structural factor\"（非 the structural factor）、\"trace a predictive pathway\"（非 causal chain）、\"mechanisms that remain to be characterized\"（非 gradient diversity）\n4. **ICML venue fit 良好**: Diagnostic negative-result paper with systematic factorial design, well-suited for ICML methodology track\n5. **残留 issues 均为 info 级**: ManiSkill baseline 未测量、Becker-Ehmck 未引用——均不影响接收决定\n\n**Confidence 4/5**: 我对方法论评估有高度信心（factorial design, IQM, AUROC 均已独立验证），但对 CIVO 的 broader significance（是否足够 important for ICML accept threshold）略有不确定。\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 273 · 2026-05-24T15:09:17.319137+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-24T15:09:31.737365+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-24T15:09:31.838232+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 276 · 2026-05-24T15:09:36.447696+00:00_

Round 5 审稿报告已提交。核心结论：Round 4 的 3 个 critical issues 全部修复（模板/Impact Statement/IQM），IQM=148.8 经独立计算验证正确，整体评分从 Weak Accept (4/6) 升至 Accept (5/6)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 8

3 recorded events

### User

_source line 277 · 2026-05-24T15:10:12.644267+00:00_

[Round 5 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每个关键判断标注 [AGREE] 或 [REBUT] 并给出理由。

**特别关注**：
1. R2 维持 **Weak Accept (4/6)**，你升至 **Accept (5/6)**——请直接回应分歧
2. R2 Contribution 2/4 (Fair) vs 你的 Significance 3/4 (Good)——R2 认为 scope (DreamerV3 + locomotion) 和 actionability ("不用 trained embedding") 限制了 significance，你是否同意？
3. R2 发现 AUTHORERR 并标为 warning——你标为 info (已知行为)，哪个更准确？
4. R2 将 baseline vals 降级为 minor（理由：negative result 不需要 baseline 来判断）——你同意吗？
5. R2 对 Impact Statement 给出了正面评价（"既不是 boilerplate 也不过度渲染"）——你是否同意这个质量评估？

---

以下是 Reviewer 2 的完整审稿意见：

**Overall**: Weak Accept (4/6)
**Soundness**: 3/4, **Presentation**: 3/4, **Contribution**: 2/4, **Originality**: 3/4
**Confidence**: 4/5

**Issue 验证结果**（与你完全一致）:
- 3/3 CRITICAL: 全部 RESOLVED
- gradient diversity: RESOLVED ✓
- Seed 数量: RESOLVED ✓
- Baseline vals: PARTIALLY RESOLVED → 降级为 minor
- "causal chain": RESOLVED ✓
- Actionable solution: ACKNOWLEDGED non-blocking for ICML

**新发现**:
- N-R5-1 [warning]: PDF page 1 显示 "AUTHORERR: Missing \icmlcorrespondingauthor"——R2 认为是可见格式错误，建议立即修复
- N-R5-2 [minor]: Introduction "isolate" vs Abstract "identify" 不完全一致——R2 认为是 stylistic preference，不影响评分

**Contribution 2/4 的理由**:
- CIVO 现象新颖但 scope 限于 DreamerV3 locomotion
- Architectural boundary (MPC vs imagination) 仅为假说
- 四级干预层级有方法论示范价值
- 核心 takeaway 仍是"不要用 trained embedding"
- 与 Henderson et al. 2018 相比，本文 scope 窄

**写作质量评估**:
- Abstract 数字密度从 6+ 降至 ~4，改善明显
- 因果语言一致性达标
- Impact Statement 质量合理
- Robotics framing 在 ICML 中作为 motivation 合理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 278 · 2026-05-24T15:11:09.133690+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 Round 5 意见的交叉回应\n\n---\n\n## 核心分歧：Accept (5/6) vs Weak Accept (4/6)\n\n**我维持 Accept (5/6)，但承认 R2 的 Weak Accept (4/6) 是合理的 reviewer 间分歧。**\n\n分歧的根源在于 Contribution/Significance 维度（我 3/4 Good，R2 2/4 Fair）。其他三个维度（Soundness 3/4, Presentation 3/4, Originality 3/4）完全一致。以下逐条回应。\n\n---\n\n## 1. Contribution/Significance 分歧：Good (3/4) vs Fair (2/4)\n\n**[REBUT] R2 的 Fair 评分，维持 Good，但承认处于 Good 下沿。**\n\nR2 的三个论据和我的回应：\n\n**R2 论据 A: \"scope 限于 DreamerV3 locomotion\"**\n\n事实层面正确。但 significance 不应仅按现象的覆盖范围衡量，还应考虑：\n- DreamerV3 是当前 imagination-based RL 最广泛使用的 baseline。在这个特定架构上发现的 failure mode 对所有使用或 extend DreamerV3 的团队有直接实践价值\n- 论文的 structural insight——pure-imagination training 导致 dual critics converge (ρ>0.999)——是 architecture-general 的。无论 CIVO 是否在其他架构复现，这一发现对所有 imagination-based 方法中使用 dual critic 的研究有意义\n- Locomotion-specific 的发现并非局限——locomotion 是 robotics RL 的 core application（Boston Dynamics, legged robots, ANYmal 等大量 CoRL/RSS 工作）\n\n**R2 论据 B: \"核心 takeaway 是不要用 trained embedding\"**\n\n这是对论文贡献的简化。论文的核心 takeaway 是：\n1. **为什么**它失败（RSSM reward prediction gap → critic internalization → positive feedback loop）——这是 mechanistic understanding，不只是 \"don't do X\"\n2. **为什么**标准修复不 work（gradient pathway redundancy, dual critic convergence in imagination）——这告诉社区哪些方向不值得尝试\n3. **什么条件下**它失败（trained + exposed = jointly sufficient; frozen 或 removed = safe）——这给出了 precise boundary conditions\n\n这三层 insight 的组合超越了 \"don't use trained embedding\" 的简单建议。\n\n**R2 论据 C: \"与 Henderson et al. 2018 相比 scope 窄\"**\n\nHenderson et al. 2018 覆盖了整个 deep RL reproducibility landscape（多环境 × 多算法 × 多 hyperparameter）。本文确实 scope 更窄。但 Henderson 是 AAAI 2018（1500+ citations），以 ICML accept threshold 而非 landmark paper threshold 衡量，本文的 systematic factorial design + mechanistic analysis 达到 Good。\n\n**总结**: R2 的 Fair 强调了 scope 限制，我的 Good 强调了 mechanistic depth。两者都有道理。我认为 3/4 是更准确的评估，因为 ICML 读者从这篇论文获得的不仅是 \"avoid X\" 而是 \"understand why X fails and why Y can't fix it\"——这是方法论贡献，不仅仅是 empirical observation。\n\n---\n\n## 2. AUTHORERR：warning vs info\n\n**[AGREE] R2 的 warning 评级更准确。**\n\n我将其标为 info 是基于 \"这是 icml2026.sty 匿名模式的已知行为\"。但 R2 的观点更实际：无论原因如何，PDF 中可见的 \"AUTHORERR\" 文字是一个格式瑕疵，reviewer/AC 看到后可能产生 \"论文准备不充分\" 的印象。\n\n修复方法简单（添加 `\\icmlcorrespondingauthor{}` 或在匿名模式下 suppress 该 warning），应该立即修复。R2 的 warning 级别比我的 info 更合适。\n\n---\n\n## 3. Baseline vals 降级为 minor\n\n**[AGREE] R2**\n\n我在 Round 5 已将此降级为 info 并建议不再追踪。R2 独立得出同样结论。理由一致：negative result 论文中，ManiSkill 部分的论点是 \"CIVO 不存在\"（frozen matches trained），不需要 baseline eval 来判断。\n\n---\n\n## 4. Impact Statement 质量\n\n**[AGREE] R2**\n\nR2 评价 \"既不是 boilerplate 也不过度渲染\"——同意。具体来说：\n- 正面：它具体讨论了 NVE detector 的过早依赖风险和 simulation-only 的局限性（conclusion.tex:18），这些是论文特有的 concern，不是 generic 的 \"AI could be misused\"\n- 非 boilerplate：它没有使用 \"this work has no negative societal impact\" 的空话\n- 合理长度（~100 词）：不占过多版面\n\n---\n\n## 5. Introduction \"isolate\" vs Abstract \"identify\"\n\n**[AGREE] R2 — stylistic preference, non-blocking**\n\n两位 reviewer 一致认为这不影响评分。\"isolate\" 在 factorial design 语境下是合理的方法论术语。\n\n---\n\n## 两位 Reviewer 最终评分对比\n\n| 维度 | R1 | R2 | 差异 |\n|------|----|----|------|\n| Overall | **Accept (5/6)** | **Weak Accept (4/6)** | ±1 |\n| Soundness | 3/4 | 3/4 | — |\n| Presentation | 3/4 | 3/4 | — |\n| Contribution | **3/4** | **2/4** | ±1 |\n| Originality | 3/4 | 3/4 | — |\n| Confidence | 4/5 | 4/5 | — |\n\n**分歧集中在 Contribution 一个维度**，导致 Overall 差 1 档。这是典型的 reviewer 间正常分歧范围。\n\n**给 AC 的建议**: 两位 reviewer 在 Soundness、Originality、Presentation 上完全一致（均 Good）。分歧仅在 Contribution/Significance——这取决于 AC 对 \"DreamerV3 locomotion-specific diagnostic\" 的 impact 判断。论文的 methodological rigor 不是争议点。\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 Round 5 意见的交叉回应\n\n---\n\n## 核心分歧：Accept (5/6) vs Weak Accept (4/6)\n\n**我维持 Accept (5/6)，但承认 R2 的 Weak Accept (4/6) 是合理的 reviewer 间分歧。**\n\n分歧的根源在于 Contribution/Significance 维度（我 3/4 Good，R2 2/4 Fair）。其他三个维度（Soundness 3/4, Presentation 3/4, Originality 3/4）完全一致。以下逐条回应。\n\n---\n\n## 1. Contribution/Significance 分歧：Good (3/4) vs Fair (2/4)\n\n**[REBUT] R2 的 Fair 评分，维持 Good，但承认处于 Good 下沿。**\n\nR2 的三个论据和我的回应：\n\n**R2 论据 A: \"scope 限于 DreamerV3 locomotion\"**\n\n事实层面正确。但 significance 不应仅按现象的覆盖范围衡量，还应考虑：\n- DreamerV3 是当前 imagination-based RL 最广泛使用的 baseline。在这个特定架构上发现的 failure mode 对所有使用或 extend DreamerV3 的团队有直接实践价值\n- 论文的 structural insight——pure-imagination training 导致 dual critics converge (ρ>0.999)——是 architecture-general 的。无论 CIVO 是否在其他架构复现，这一发现对所有 imagination-based 方法中使用 dual critic 的研究有意义\n- Locomotion-specific 的发现并非局限——locomotion 是 robotics RL 的 core application（Boston Dynamics, legged robots, ANYmal 等大量 CoRL/RSS 工作）\n\n**R2 论据 B: \"核心 takeaway 是不要用 trained embedding\"**\n\n这是对论文贡献的简化。论文的核心 takeaway 是：\n1. **为什么**它失败（RSSM reward prediction gap → critic internalization → positive feedback loop）——这是 mechanistic understanding，不只是 \"don't do X\"\n2. **为什么**标准修复不 work（gradient pathway redundancy, dual critic convergence in imagination）——这告诉社区哪些方向不值得尝试\n3. **什么条件下**它失败（trained + exposed = jointly sufficient; frozen 或 removed = safe）——这给出了 precise boundary conditions\n\n这三层 insight 的组合超越了 \"don't use trained embedding\" 的简单建议。\n\n**R2 论据 C: \"与 Henderson et al. 2018 相比 scope 窄\"**\n\nHenderson et al. 2018 覆盖了整个 deep RL reproducibility landscape（多环境 × 多算法 × 多 hyperparameter）。本文确实 scope 更窄。但 Henderson 是 AAAI 2018（1500+ citations），以 ICML accept threshold 而非 landmark paper threshold 衡量，本文的 systematic factorial design + mechanistic analysis 达到 Good。\n\n**总结**: R2 的 Fair 强调了 scope 限制，我的 Good 强调了 mechanistic depth。两者都有道理。我认为 3/4 是更准确的评估，因为 ICML 读者从这篇论文获得的不仅是 \"avoid X\" 而是 \"understand why X fails and why Y can't fix it\"——这是方法论贡献，不仅仅是 empirical observation。\n\n---\n\n## 2. AUTHORERR：warning vs info\n\n**[AGREE] R2 的 warning 评级更准确。**\n\n我将其标为 info 是基于 \"这是 icml2026.sty 匿名模式的已知行为\"。但 R2 的观点更实际：无论原因如何，PDF 中可见的 \"AUTHORERR\" 文字是一个格式瑕疵，reviewer/AC 看到后可能产生 \"论文准备不充分\" 的印象。\n\n修复方法简单（添加 `\\icmlcorrespondingauthor{}` 或在匿名模式下 suppress 该 warning），应该立即修复。R2 的 warning 级别比我的 info 更合适。\n\n---\n\n## 3. Baseline vals 降级为 minor\n\n**[AGREE] R2**\n\n我在 Round 5 已将此降级为 info 并建议不再追踪。R2 独立得出同样结论。理由一致：negative result 论文中，ManiSkill 部分的论点是 \"CIVO 不存在\"（frozen matches trained），不需要 baseline eval 来判断。\n\n---\n\n## 4. Impact Statement 质量\n\n**[AGREE] R2**\n\nR2 评价 \"既不是 boilerplate 也不过度渲染\"——同意。具体来说：\n- 正面：它具体讨论了 NVE detector 的过早依赖风险和 simulation-only 的局限性（conclusion.tex:18），这些是论文特有的 concern，不是 generic 的 \"AI could be misused\"\n- 非 boilerplate：它没有使用 \"this work has no negative societal impact\" 的空话\n- 合理长度（~100 词）：不占过多版面\n\n---\n\n## 5. Introduction \"isolate\" vs Abstract \"identify\"\n\n**[AGREE] R2 — stylistic preference, non-blocking**\n\n两位 reviewer 一致认为这不影响评分。\"isolate\" 在 factorial design 语境下是合理的方法论术语。\n\n---\n\n## 两位 Reviewer 最终评分对比\n\n| 维度 | R1 | R2 | 差异 |\n|------|----|----|------|\n| Overall | **Accept (5/6)** | **Weak Accept (4/6)** | ±1 |\n| Soundness | 3/4 | 3/4 | — |\n| Presentation | 3/4 | 3/4 | — |\n| Contribution | **3/4** | **2/4** | ±1 |\n| Originality | 3/4 | 3/4 | — |\n| Confidence | 4/5 | 4/5 | — |\n\n**分歧集中在 Contribution 一个维度**，导致 Overall 差 1 档。这是典型的 reviewer 间正常分歧范围。\n\n**给 AC 的建议**: 两位 reviewer 在 Soundness、Originality、Presentation 上完全一致（均 Good）。分歧仅在 Contribution/Significance——这取决于 AC 对 \"DreamerV3 locomotion-specific diagnostic\" 的 impact 判断。论文的 methodological rigor 不是争议点。\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 279 · 2026-05-24T15:11:12.849033+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3715
}
```

</details>

---

## Round 9

26 recorded events

### User

_source line 280 · 2026-05-28T00:34:45.185677+00:00_

[Round 6 审稿请求]:
## Round 6 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验完整性 + CoRL venue 适配性**

### Venue 信息
- **目标 venue**: CoRL 2026 (Conference on Robot Learning)
- **截止日期**: 2026-05-29 23:59 UTC
- **页数限制**: 正文 8 页，参考文献和附录不限
- **模板**: PMLR（Proceedings of Machine Learning Research）
- **匿名规则**: Double-blind
- **核心要求**: 论文必须聚焦于机器人学习的核心问题（"focus on core robotics problems"）
- **必须包含**: Limitations section

### 论文文件
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/submitted.pdf`
- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`

### 审稿模式：继续审稿（Round 6）
这是第 6 轮审稿。上轮（Round 5）在 ICML 2026 venue 下评分为 Borderline Accept (7/10)。**本轮 venue 变回 CoRL 2026**，这是关键变化。

### ⚠️ 需重点关注的问题

**CRITICAL — CoRL Venue 适配性（REOPENED）**:
Round 3（上次 CoRL 审稿）评分 Weak Reject (5/10)，核心障碍就是 venue fit。当时的解决方案是"改投 ICML"，但现在又回到 CoRL。你必须重新评估：
- CoRL CFP 明确要求 "focus on core robotics problems"
- CIVO 现象仅在 DMC locomotion 中出现
- ManiSkill 实验（3 个 manipulation 环境）结果为阴性——CIVO 未出现
- 论文如何论证这一 locomotion-specific 的 failure mode 对机器人学习社区的价值？
- 是否有足够的 framing 将 diagnostic 发现与 robot learning 实践联系起来？

**CRITICAL — 模板合规性**:
main.tex 第 8 行仍使用 `\usepackage{icml2026}`，包括 `\icmltitlerunning`、`\icmlkeywords`、`\icmlauthorlist` 等 ICML 专用命令。**请检查提交的 PDF 实际使用的模板**——可能 PDF 已切换但 LaTeX 源码未同步，也可能两者都错。

**上轮遗留 in_progress 问题**:
1. **N-R5-1 (AUTHORERR)**: icml2026.sty 报错，已添加 `\icmlcorrespondingauthor`。现在如果切回 CoRL 模板，此问题可能消失或变化——检查 PDF 是否有编译警告。
2. **N-R5-2 (显示密度/6页)**: 8 页正文对 CoRL 是合规的（CoRL 允许 8 页），但检查排版密度是否合理。
3. **N-R5-3 (色盲友好)**: 检查 Figure 2 和其他图表是否添加了非颜色区分机制。

### 你的评分维度
1. 方法论严谨性（实验设计、统计检验、因果/预测声明的措辞）
2. 实验完整性（消融充分性、seed 数量、跨环境验证）
3. CoRL venue 适配性（对机器人学习社区的价值和相关性）
4. 模板与格式合规性

请按 ICML/CoRL 标准给出：Overall Score (1-6), Significance, Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 281 · 2026-05-28T00:35:00.490446+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/submitted.pdf",
  "pages": "1-2",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/submitted.pdf",
    "pages": "1-2",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 282 · 2026-05-28T00:35:00.942687+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 424.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 418.7}], \"total_pages\": 31, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 283 · 2026-05-28T00:35:01.143803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "90"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "90"
  }
}
```

</details>

---

### Tool result

_source line 284 · 2026-05-28T00:35:01.546161+00:00_

1	\documentclass{article}
2	
3	% xcolor with table option must be loaded before icml2026.sty (which loads xcolor internally)
4	\PassOptionsToPackage{table}{xcolor}
5	
6	\usepackage{hyperref}
7	\newcommand{\theHalgorithm}{\arabic{algorithm}}
8	\usepackage{icml2026}
9	
10	\usepackage[utf8]{inputenc}
11	\usepackage[T1]{fontenc}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{graphicx}
16	\graphicspath{{../../artifacts/}}
17	\usepackage{colortbl}
18	\usepackage{caption}
19	\usepackage{subcaption}
20	\usepackage{array}
21	\usepackage{enumitem}
22	\usepackage{wrapfig}
23	\usepackage{algorithm}
24	\usepackage{algorithmic}
25	
26	% Custom commands
27	\newcommand{\dt}{\mathrm{dt}}
28	\newcommand{\nve}{\mathrm{nve}}
29	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
30	\newcommand{\sgseval}{448.3}
31	\newcommand{\sgsnve}{1.66}
32	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
33	\usepackage{pifont}
34	\newcommand{\cmark}{\ding{51}}
35	\newcommand{\xmark}{\ding{55}}
36	\newcommand{\ie}{\textit{i.e.}}
37	\newcommand{\eg}{\textit{e.g.}}
38	\newcommand{\cf}{\textit{cf.}}
39	\newcommand{\etal}{\textit{et al.}}
40	
41	\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}
42	
43	\begin{document}
44	
45	\twocolumn[
46	  \icmltitle{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\
47	  A Diagnostic Analysis of Variable-Rate DreamerV3}
48	
49	  \begin{icmlauthorlist}
50	    \icmlauthor{Anonymous Authors}{anon}
51	  \end{icmlauthorlist}
52	
53	  \icmlaffiliation{anon}{Anonymous Institution}
54	
55	  \icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}
56	
57	  \icmlkeywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
58	
59	  \vskip 0.3in
60	]
61	
62	\printAffiliationsAndNotice{}
63	
64	\begin{abstract}
65	\input{sections/abstract_body}
66	\end{abstract}

…[truncated 457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 285 · 2026-05-28T00:35:07.025637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 286 · 2026-05-28T00:35:08.537295+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1511
}
```

</details>

---

### Tool call

_source line 287 · 2026-05-28T00:35:30.527869+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 288 · 2026-05-28T00:35:30.729120+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; $n{=}36$, AUROC${=}1.000$, F1${=}1.000$). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, so Double Q pessimism is ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 289 · 2026-05-28T00:35:30.779948+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 290 · 2026-05-28T00:35:30.830854+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	World-model reinforcement learning enables sample-efficient learning directly on physical hardware \citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\dt$ mismatches between simulation and hardware. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\% of baseline). Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables environment-dependent pathologies---a $1.63\times$ reward prediction gap in Walker Walk, or dynamics-model prior drift without measurable reward bias in Cheetah Run---which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\geq 2.0\times$ achieves perfect classification ($n{=}36$; AUROC${=}1.000$, F1${=}1.000$; Appendix~\ref{sec:appendix_sensitivity}).
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/paper/fig4_mechanism_diagram.pdf}
10	\caption{CIVO mechanism. The trained $\dt$-embedding enables asymmetric reward prediction fidelity, initiati
…[truncated 2071 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 291 · 2026-05-28T00:35:40.838050+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 292 · 2026-05-28T00:35:40.889014+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that trace a predictive pathway from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
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
24	008f & No dt\_emb (s0) & --- & ON & 8 & 139.5 @105K$^f$ & 1.69$\times$$^f$ & Healthy$^f$ \\
25	--- s1 & No dt\_emb (s1) & --- & ON & 8 & 468.8 @105K & 0.88$\times$ & Healthy \\
26	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
27	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
28	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
29	\midrule
30	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
31	\rowcolor{gray!15}
32	010b & Cheetah Run (s1) & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
33	\rowcolor{gray
…[truncated 16702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 293 · 2026-05-28T00:35:58.381524+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-28T00:35:58.382062+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-28T00:35:58.432796+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{CIVO mechanism.}
5	The RSSM fidelity gap under trained conditioning is environment-dependent (Table~\ref{tab:rssm_fidelity}): Walker Walk develops a $1.63\times$ reward prediction gap (MAE $0.053 \to 0.087$ at $\dt{=}2$) while observation reconstruction improves ($1.35\times$ vs.\ baseline $2.04\times$), but Cheetah Run shows \emph{no} reward gap ($1.00\times$, MAE ${\approx}0.141$ at both scales) despite exhibiting CIVO at comparable or higher severity ($8.27\times$ NVE). This dissociation indicates that reward fidelity degradation is one environment-dependent transmission pathway---operative in Walker---but not a necessary condition; in Cheetah, the trained $\dt$-embedding induces value overestimation through an alternative pathway, possibly via dynamics-model prior drift, without measurable single-step reward bias. The mechanism is analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. Gradient magnitude $\neq$ causal importance: the reward head (38--49\% of $\nabla_\theta e_{\dt}$) fails when blocked alone; the observation decoder (16--22\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge ($\rho > 0.999$; \S\ref{sec:arch_results}), a structural consequence of shared-feature imagination where both value heads train on identical model-generated rollouts (any system with this architecture will exhibit the same convergence, regardless of the specific world model)---so standard overestimation corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\ref{sec:mpc_immune}). On Walker, time-series analysis across 12 dense checkpoints resolves a three-stage causal chain ($n{=}2$; Appendix~\ref{sec:timeseries_fidelity}): reward fidelity degradation (SS ratio $>1.1\times$ at 20K) precedes value overestimat
…[truncated 6975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool result

_source line 296 · 2026-05-28T00:35:58.433347+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We identify trained $\dt$-embedding with multi-rate data exposure as the strongest predictor of CIVO in DreamerV3 (36/36, AUROC${=}1.000$, F1${=}1.000$). No tested intervention reliably eliminates CIVO across environments (seven interventions across four levels; pathway redundancy shifts co-adaptation to unblocked channels); in pure imagination, dual critics converge ($\rho > 0.999$), so Double Q pessimism is ineffective. The feedback architecture---MPC re-planning versus imagination-based bootstrapping---is the hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work.
5	
6	\paragraph{Limitations.}
7	Our analysis covers proprioceptive locomotion (DMC) and simulated manipulation (ManiSkill) but not pixel-based observations, Atari, or real-robot deployments. All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures \citep{micheli2023iris} or under learned temporal gates remains open. Statistical power is limited (4--5 seeds) \citep{colas2018seeds}; the NVE threshold may require recalibration for different reward scales. Code: upon acceptance.
8	\label{sec:limitations}
9	
10	\section*{Broader Impact Statement}
11	
12	Silent training failures in variable-rate world-model RL pose safety risks for robotic deployment. Two safeguards address this: the NVE diagnostic ($\geq 2.0\times$, AUROC${=}1.000$, $n{=}36$) detects CIVO during training, and the frozen-embedding check eliminates it (0/16 controls). Both are specific to DreamerV3's RSSM; all experiments use simulated environments without real-robot deployment.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 297 · 2026-05-28T00:36:55.072809+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LOEO|leave.one.*out|cross.valid",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LOEO|leave.one.*out|cross.valid",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 298 · 2026-05-28T00:36:56.478624+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-292-\item \textbf{Perfect classification.} The $2.0\times$ threshold achieves 100\% accuracy on both the $n{=}11$ factorial set and the comprehensive $n{=}36$ evaluation (AUROC${=}1.000$, F1${=}1.000$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-293-\item \textbf{Clean separation.} The lowest CIVO-positive NVE ($2.09\times$) clears the threshold by $0.09\times$; the highest non-CIVO transient ($1.88\times$, frozen-embedding exp\_057) sits $0.12\times$ below. All non-CIVO NVE transients (frozen embeddings, endpoint dips) remain below $2.0\times$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:294:\item \textbf{Robustness.} The $2.0\times$ threshold achieves perfect classification across the extended $n{=}36$ evaluation and LOEO cross-validation (Table~\ref{tab:nve_loeo}), with zero false positives across all folds.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-295-\end{enumerate}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-296-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-356-\label{sec:nve_loeo}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-357-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:358:To assess whether $\theta{=}2.0\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}15$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all exper
…[truncated 2481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 1405
}
```

</details>

---

### Tool call

_source line 299 · 2026-05-28T00:36:57.583585+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cross_env_civo|cross.env.civo|causal_ablation|cosine_similarity|cosine_temporal|timeseries_fidelity|entropy_not_diagnostic",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "2",
  "head_limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cross_env_civo|cross.env.civo|causal_ablation|cosine_similarity|cosine_temporal|timeseries_fidelity|entropy_not_diagnostic",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "2",
    "head_limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 300 · 2026-05-28T00:36:57.634312+00:00_

149-\centering
150-\caption{Cross-environment CIVO comparison. \textbf{Trigger}: trained dt\_emb + subsample ON + $H{=}8$; \textbf{Control}: dt\_embed\_dim$=$0 (no dt\_emb) + subsample ON + $H{=}8$. NVE Peak reports the maximum Normalized Value Excess across all seeds. CIVO is flagged when any seed exceeds NVE $\geq 2.0\times$. Per-row seed lists in footnotes; sample std throughout.}
151:\label{tab:cross_env_civo}
152-\begin{tabular}{llccc}
153-\toprule
--
181-\end{table}
182-
183:[Omitted long matching line]
184-
185-\section{NVE Threshold Sensitivity Analysis}
--
420-
421-\paragraph{Controlled three-way causal ablation.}
422:[Omitted long matching line]
423-
424-\paragraph{Cross-environment frozen verification.}
--
428-\centering
429-\caption{Three-way causal ablation (Walker Walk, seed${=}1$). Only the $\dt$-embedding treatment varies; all other configuration is identical. Trained embedding triggers CIVO; frozen and removed do not.}
430:\label{tab:causal_ablation}
431-\footnotesize
432-\begin{tabular}{llccl}
--
854-\label{sec:cosine_evolution}
855-
856:[Omitted long matching line]
857-
858-\begin{figure}[h]
859-\centering
860:\includegraphics[width=0.85\columnwidth]{figures/dt_embedding_cosine_similarity.png}
861:[Omitted long matching line]
862:\label{fig:cosine_similarity}
863-\end{figure}
864-
865-\subsection{\texorpdfstring{$\dt$}{dt}-Embedding Differentiation Precedes Value Divergence}
866:\label{sec:cosine_temporal}
867-
868-The preceding analysis established that trained $\dt$-embeddings learn near-antipodal representations. Here we resolve the \emph{temporal dynamics} of this differentiation across 11 experiments (${\sim}$47 checkpoints), testing whether embedding differentiation is a consequence or precursor of CIVO.
--

[Showing results with pagination = limit: 40]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 301 · 2026-05-28T00:37:09.185321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": "148",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "offset": "148",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 302 · 2026-05-28T00:37:09.186003+00:00_

148	\begin{table}[h]
149	\centering
150	\caption{Cross-environment CIVO comparison. \textbf{Trigger}: trained dt\_emb + subsample ON + $H{=}8$; \textbf{Control}: dt\_embed\_dim$=$0 (no dt\_emb) + subsample ON + $H{=}8$. NVE Peak reports the maximum Normalized Value Excess across all seeds. CIVO is flagged when any seed exceeds NVE $\geq 2.0\times$. Per-row seed lists in footnotes; sample std throughout.}
151	\label{tab:cross_env_civo}
152	\begin{tabular}{llccc}
153	\toprule
154	Environment & Configuration & Eval Return & NVE Peak & CIVO \\
155	\midrule
156	\multirow{3}{*}{Walker Walk}
157	 & Baseline ($\Delta t{=}1$) & $787.7 \pm 230.8$$^a$ & --- & --- \\
158	 & Trigger (trained dt\_emb) & $146.9 \pm 112.3$$^b$ & $4.72\times$ & \cmark~(2/3) \\
159	 & Control (no dt\_emb) & $302.4 \pm 134.8$$^c$ & $1.69\times$$^*$ & \xmark~(0/4) \\
160	\midrule
161	\multirow{3}{*}{Cheetah Run}
162	 & Baseline ($\Delta t{=}1$) & $446.1 \pm 2.9$$^d$ & --- & --- \\
163	 & Trigger (trained dt\_emb) & $77.6 \pm 36.6$$^e$ & $8.27\times$ & \cmark~(3/4) \\
164	 & Control (no dt\_emb) & $100.6 \pm 34.9$$^f$ & $0.20\times$ & \xmark~(0/4) \\
165	\midrule
166	\multirow{3}{*}{Cartpole Swingup}
167	 & Baseline ($\Delta t{=}1$) & $673.3 \pm 142.0$ & --- & --- \\
168	 & Trigger (trained dt\_emb) & $236.3 \pm 29.7$ & $0.06\times$ & \xmark~(0/3) \\
169	 & Control (no dt\_emb) & $244.8 \pm 12.7$ & ${\leq}0.1\times$ & \xmark~(0/3) \\
170	\bottomrule
171	\end{tabular}
172	\vspace{1pt}
173	{\raggedright\footnotesize
174	$^a$\,$N{=}4$: exp\_001 s1 (915.7), s2 (443.5), s3 (869.0), s4 (922.8); s3/s4 from cross-environment evaluation runs.
175	$^b$\,Eval: $N{=}5$ at 105K (009b, 008d\_s3, 008d\_s4, 059, 068). CIVO evaluated on $N{=}3$ seeds with full NVE pipeline (008d s0, 009e s1, 009b s2); 2/3 exceed $2.0\times$.
176	$^c$\,$N{=}4$: 008f s0 (139.5), s1 (468.8), s4 (289.3), 009c s3 (311.9).
177	$^d$\,$N{=}2$: exp\_077 s0 (448.1), exp\_083 s1 (444.0); consistent with Table~\ref{tab:complete_results}.
178	$^e$\,
…[truncated 3412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 303 · 2026-05-28T00:38:59.044713+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Round 6 审稿报告 — Reviewer 1（方法严谨性 + 实验完整性 + CoRL Venue 适配性）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL\"\n**目标 Venue**: CoRL 2026（从 ICML 转回）\n**上轮评分**: ICML Accept (5/6)\n\n---\n\n## 总体评分\n\n**Overall Score**: 4/6 (Weak Accept)\n**Significance**: 3/4 (Good)\n**Confidence**: 4/5\n\n**一句话总结**: 论文方法论和实验质量有显著提升（NVE 2.0× 完美分类 + Fisher exact test + 6 环境 + Cheetah 机制 dissociation），但（1）模板第三次错误——仍为 `icml2026` 而非 CoRL PMLR，（2）CoRL venue fit 有实质改善但仍为 borderline——CIVO 仅在 multi-joint DMC locomotion 中出现，核心内容仍为 RL 方法论分析。\n\n---\n\n## CRITICAL Issues\n\n### C1: 模板仍为 ICML 2026（第三次模板错误）\n\n**严重度**: CRITICAL — desk reject 风险\n\n**证据**:\n- `main.tex:8`: `\\usepackage{icml2026}` — 应为 CoRL PMLR 模板\n- `main.tex:41`: `\\icmltitlerunning{...}` — ICML 专用命令\n- `main.tex:46-51`: `\\icmltitle`, `\\icmlauthor`, `\\icmlaffiliation` — ICML 专用\n- `main.tex:86`: `\\bibliographystyle{icml2026}`\n- PDF page 1 页脚: \"Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.\"\n\n这是第三次模板错误（R3 CoRL→R4 切换 ICML✓→R6 回 CoRL 未切回）。CoRL 2026 要求 PMLR 模板（`\\usepackage{corl_2026}`）。当前 PDF 在 CoRL 系统中会被立即识别为错误 venue 的提交。\n\n### C2: CoRL Venue 适配性（重新评估）\n\n**评分: 6.5/10（R3 为 5/10，有实质改善但仍 borderline）**\n\n**改善之处**:\n\n1. **Cartpole 负控制**（6th environment，Appendix Table cross_env_civo）：单关节 vs 多关节的对比建立了精确的 scope boundary（\"multi-joint locomotion\" specificity）。这是方法论上的显著进步——从 \"locomotion-specific\" 细化为 \"multi-joint locomotion-specific\"，且提供了 mechanistic hypothesis（periodic gait dynamics vs contact-gated transitions）\n\n2. **\"Transferable diagnostic protocol\" 段落**（Discussion line 13-14）：四级干预层级被框定为可复用的诊断框架，适用于 \"goal-conditioned imagination, language-conditioned world models, or skill embeddings\"。这直接面向 CoRL 社区——这些都是 robot learning 的活跃方向\n\n3. **\"Scope precision through negative controls\" 段落**（Discussion line 22-25）：明确讨论了为什么 manipulation 不触发 CIVO（periodic vs contact-gated dynamics），将 scope 分析从纯 empirical observation 提升为 hypothesis-driven analysis\n\n4. **Fisher exact test**（5/7 vs 0/16, p<0.001）：正式的统计检验强化了因果论证\n\n5. **Broader Impact Statement** 直接连接 robot deployment safety\n\n**仍然存在的 venue fit 限制**:\n\n1. **核心内容仍为 RL 方法论分析**：Sections 4.1-4.8（占正文 ~4 页）是纯 RL factorial ablation + intervention hierarchy。Robotics grounding 集中在 Introduction 开头、Discussion 尾部和 Broader Impact——结构上仍有 \"bookend\" 特征\n\n2. **无 real-robot 验证或 robot-specific 环境**：DMC Walker/Cheetah/Cartpole 是 generic control tasks，ManiSkill 是 sim-only。CoRL 社区更看重 real-robot relevance\n\n3. **CIVO 仅影响 multi-joint DMC locomotion**（5/7 seeds），不影响 manipulation（3 tasks × multiple seeds = all negative）。对 CoRL 核心受众（大量是 manipulation 研究者）的直接价值有限\n\n4. **\"Transferable diagnostic protocol\" 是 forward-looking**：论文声称四级 hierarchy 可用于 goal-conditioning 等，但未验证。这是 speculation，不是 demonstrated contribution\n\n**与 R3 对比**：\n- R3 (5/10): 1 环境 + 无 robotics grounding + \"bookend\" framing\n- R6 (6.5/10): 6 环境 + scope precision analysis + transferable protocol framing + Fisher test + mechanism nuance\n\n改善幅度约 1.5 分。论文现在处于 CoRL 的 borderline 区域——有足够的 robotics motivation 不被 desk reject，但核心贡献的 robotics specificity 仍弱于 CoRL typical acceptance。\n\n---\n\n## 方法论严谨性评估（显著提升）\n\n### 统计论证\n\n**NVE 2.0× 完美分类 (n=36, AUROC=1.000, F1=1.000)**:\n\n- 阈值从 1.5× 提升到 2.0×，实现了完美分类\n- Clean separation margin: 最低 CIVO+ NVE (2.09×) 与最高 non-CIVO NVE (1.88×) 之间有 0.21× gap\n- **LOEO 交叉验证**: 在 Appendix B.5 中确认——Walker/Cheetah/PickCube 三折 LOEO 全部 100% accuracy ✓\n- **LOCO 交叉验证**: 36/36 = 100%，zero FP across all folds ✓\n- 阈值不是 data-snooping 的结果——0.21× 的 separation gap 和多种交叉验证方式支持其泛化性\n\n**Fisher exact test (5/7 vs 0/16, p<0.001)**:\n\n正式的统计检验替代了之前的描述性比较。这是 Round 6 最重要的方法论改进之一。\n\n**Temporal ordering (n=2, r=0.81, p=0.002)**:\n\n12 dense checkpoints 的时间序列分析为 \"fidelity → value → entropy\" 因果链提供了定量证据。n=2 仍然很小，但 ~10K step onset-to-onset lag 在两个 seeds 间 consistent（10K vs 9K）。p=0.002 统计显著（though interpretation at n=2 should be cautious）。\n\n### Cheetah 机制 Dissociation\n\n这是本轮最有价值的新发现。Walker 有 1.63× reward prediction gap，Cheetah 有 NO reward gap (1.00×) yet comparable CIVO severity (8.27×)。这意味着：\n\n1. CIVO 有至少两种传播途径（reward fidelity vs dynamics-model prior drift）\n2. 之前的 \"2.78× reward prediction gap\" 叙事被修正为 environment-specific\n3. 机制理解更深入但也更复杂——论文诚实地承认 Cheetah pathway 仍 open\n\n### F6 重写（Pathway B 移除）\n\n**重大变更**：Round 3-5 报告 \"Two of four seeds collapse (50%): Pathway A (CIVO) and Pathway B (entropy increase)\"。Round 6 报告 \"none exhibits CIVO onset (peak NVE ≤0.8×)\"。\n\n这是一个 180° 的结果翻转。可能原因：\n- 008f 脚注提到 \"corrected-code rerun\"——可能发现了 code bug\n- Seed numbering changed (s0,s1,s2,s5 vs 原来的 s0-s3)\n- NVE 阈值改变（2.0× vs 1.5×）不解释 NVE 值的变化（4.02× → ≤0.8×）\n\n**方法论影响**：\n- 如果是 code correction，论文应说明修改了什么、为什么之前的结果不可靠\n- 完全移除 Pathway B 而不解释为什么之前报告了它，会降低可信度\n- 正面来看：0/4 CIVO in dt=1 imagination 是一个更 clean 的结论（\"multi-step imagination is necessary for CIVO\"），逻辑上更有力\n\n**建议**：在 Appendix 增加一段解释 F6 results 的变化原因。\n\n### 新增实验的充分性\n\n| 新增内容 | 评估 |\n|---------|------|\n| Cartpole (0/3, 3 seeds) | ✓ 好的负控制，确立 multi-joint boundary |\n| Cheetah s0 (exp_078) | ✓ 增加 Cheetah seeds 强化跨环境验证 |\n| 008f s0 corrected rerun | ⚠️ \"corrected-code\" 需要更多解释 |\n| Temporal ordering (n=2) | ✓ 有意义但 sample 小 |\n| Cosine similarity analysis | ✓ Embedding representation analysis 增加 mechanistic depth |\n| Fisher exact test | ✓ 正式统计检验 |\n\n---\n\n## 上轮遗留问题\n\n### N-R5-1 (AUTHORERR)\n**[RESOLVED but superseded]**: `main.tex:55` 添加了 `\\icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}`。但由于模板应切回 CoRL，此修复将被替换。\n\n### N-R5-2 (显示密度)\n**[RESOLVED]**: 论文为 31 页 PDF（8 页正文 + refs + 22 页 appendix），正文密度合理。CoRL 允许 8 页正文，排版无问题。\n\n### N-R5-3 (色盲友好)\n**[CANNOT VERIFY from LaTeX]**: Figure 2 caption 描述 red/blue 颜色编码，未提及 linestyle/marker 区分。建议检查。\n\n---\n\n## 新发现的问题\n\n### N-R6-1 [warning]: F6 结果完全翻转未解释\n- **位置**: results.tex:113-114\n- **问题**: 从 \"2/4 collapse (Pathway A + Pathway B)\" 变为 \"0/4 CIVO onset (NVE ≤0.8×)\"，文中未解释变化原因\n- **影响**: 降低修订过程的透明度。如果这是 code correction，应该说明\n- **建议**: 在 Appendix 增加 1 段说明 F6 修订历史\n\n### N-R6-2 [warning]: \"corrected-code rerun\" 缺乏细节\n- **位置**: results.tex:50 (Table 1 脚注 f)\n- **问题**: 008f s0 标注 \"corrected-code rerun\" 但未说明修正了什么\n- **影响**: Reviewer 会质疑：修正了什么 bug？是否影响其他实验？\n- **建议**: 在 Appendix 简述 code correction 的内容和影响范围\n\n### N-R6-3 [info]: Table 1 中 \"--- s1\" 行的 Exp 编号空白\n- **位置**: results.tex:25\n- **问题**: 008f s1 的 Exp 列显示 \"--- s1\" 而非正式实验编号，格式不一致\n\n---\n\n## ICML 维度打分（CoRL 无标准化维度，沿用 ICML 量表）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/4 (Good) | Factorial design 严谨, LOEO+LOCO 验证, Fisher exact test, temporal ordering analysis; Cheetah dissociation 增加 depth |\n| Presentation | 3/4 (Good) | F1-F7 结构清晰, Discussion 大幅扩展且有机制深度; 但 F6 翻转未解释, \"corrected-code\" 未说明 |\n| Significance | 3/4 (Good, CoRL-adjusted) | Diagnostic protocol 有方法论示范价值; multi-joint specificity + mechanism nuance; 但 CoRL 实践价值仍弱于 methodology 价值 |\n| Originality | 3/4 (Good) | Cheetah dissociation 是重要新发现; embedding cosine analysis 增加 representational insight; 四级 hierarchy 仍有新意 |\n\n---\n\n## 方法严谨性评分: 8.5/10（Round 5 为 8/10）\n\n提升 0.5 分原因:\n- NVE 2.0× 完美分类 + LOEO/LOCO 双重交叉验证\n- Fisher exact test (p<0.001) 正式化因果论证\n- Cheetah dissociation 深化机制理解\n- Temporal ordering analysis (虽然 n=2)\n- Cartpole 负控制精确化 scope boundary\n\n未达 9/10 原因:\n- F6 结果翻转未解释\n- \"corrected-code rerun\" 细节缺失\n- Temporal ordering n=2 仍然很小\n- Cheetah pathway 仍为 open question\n\n---\n\n## Overall: Weak Accept (4/6)\n\n**降级理由**（从 ICML Accept 5/6 → CoRL Weak Accept 4/6）：\n- 完全因为 venue 变化。论文方法论质量从 Round 5 到 Round 6 **提升了**，但 CoRL venue fit (6.5/10) 弱于 ICML venue fit (8.5/10)。\n- 如果论文修复模板 + 在正文中增加 1 段 robotics-specific mechanism analysis（为什么 multi-joint 周期性步态使 RSSM 对 temporal conditioning 特别脆弱），可升至 Accept (5/6)。\n\n**阻塞项**:\n1. **模板必须立即切回 CoRL PMLR**——否则 desk reject\n2. **F6 结果翻转需要至少一句话解释**——否则 reviewer 质疑数据可靠性\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Round 6 审稿报告 — Reviewer 1（方法严谨性 + 实验完整性 + CoRL Venue 适配性）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL\"\n**目标 Venue**: CoRL 2026（从 ICML 转回）\n**上轮评分**: ICML Accept (5/6)\n\n---\n\n## 总体评分\n\n**Overall Score**: 4/6 (Weak Accept)\n**Significance**: 3/4 (Good)\n**Confidence**: 4/5\n\n**一句话总结**: 论文方法论和实验质量有显著提升（NVE 2.0× 完美分类 + Fisher exact test + 6 环境 + Cheetah 机制 dissociation），但（1）模板第三次错误——仍为 `icml2026` 而非 CoRL PMLR，（2）CoRL venue fit 有实质改善但仍为 borderline——CIVO 仅在 multi-joint DMC locomotion 中出现，核心内容仍为 RL 方法论分析。\n\n---\n\n## CRITICAL Issues\n\n### C1: 模板仍为 ICML 2026（第三次模板错误）\n\n**严重度**: CRITICAL — desk reject 风险\n\n**证据**:\n- `main.tex:8`: `\\usepackage{icml2026}` — 应为 CoRL PMLR 模板\n- `main.tex:41`: `\\icmltitlerunning{...}` — ICML 专用命令\n- `main.tex:46-51`: `\\icmltitle`, `\\icmlauthor`, `\\icmlaffiliation` — ICML 专用\n- `main.tex:86`: `\\bibliographystyle{icml2026}`\n- PDF page 1 页脚: \"Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.\"\n\n这是第三次模板错误（R3 CoRL→R4 切换 ICML✓→R6 回 CoRL 未切回）。CoRL 2026 要求 PMLR 模板（`\\usepackage{corl_2026}`）。当前 PDF 在 CoRL 系统中会被立即识别为错误 venue 的提交。\n\n### C2: CoRL Venue 适配性（重新评估）\n\n**评分: 6.5/10（R3 为 5/10，有实质改善但仍 borderline）**\n\n**改善之处**:\n\n1. **Cartpole 负控制**（6th environment，Appendix Table cross_env_civo）：单关节 vs 多关节的对比建立了精确的 scope boundary（\"multi-joint locomotion\" specificity）。这是方法论上的显著进步——从 \"locomotion-specific\" 细化为 \"multi-joint locomotion-specific\"，且提供了 mechanistic hypothesis（periodic gait dynamics vs contact-gated transitions）\n\n2. **\"Transferable diagnostic protocol\" 段落**（Discussion line 13-14）：四级干预层级被框定为可复用的诊断框架，适用于 \"goal-conditioned imagination, language-conditioned world models, or skill embeddings\"。这直接面向 CoRL 社区——这些都是 robot learning 的活跃方向\n\n3. **\"Scope precision through negative controls\" 段落**（Discussion line 22-25）：明确讨论了为什么 manipulation 不触发 CIVO（periodic vs contact-gated dynamics），将 scope 分析从纯 empirical observation 提升为 hypothesis-driven analysis\n\n4. **Fisher exact test**（5/7 vs 0/16, p<0.001）：正式的统计检验强化了因果论证\n\n5. **Broader Impact Statement** 直接连接 robot deployment safety\n\n**仍然存在的 venue fit 限制**:\n\n1. **核心内容仍为 RL 方法论分析**：Sections 4.1-4.8（占正文 ~4 页）是纯 RL factorial ablation + intervention hierarchy。Robotics grounding 集中在 Introduction 开头、Discussion 尾部和 Broader Impact——结构上仍有 \"bookend\" 特征\n\n2. **无 real-robot 验证或 robot-specific 环境**：DMC Walker/Cheetah/Cartpole 是 generic control tasks，ManiSkill 是 sim-only。CoRL 社区更看重 real-robot relevance\n\n3. **CIVO 仅影响 multi-joint DMC locomotion**（5/7 seeds），不影响 manipulation（3 tasks × multiple seeds = all negative）。对 CoRL 核心受众（大量是 manipulation 研究者）的直接价值有限\n\n4. **\"Transferable diagnostic protocol\" 是 forward-looking**：论文声称四级 hierarchy 可用于 goal-conditioning 等，但未验证。这是 speculation，不是 demonstrated contribution\n\n**与 R3 对比**：\n- R3 (5/10): 1 环境 + 无 robotics grounding + \"bookend\" framing\n- R6 (6.5/10): 6 环境 + scope precision analysis + transferable protocol framing + Fisher test + mechanism nuance\n\n改善幅度约 1.5 分。论文现在处于 CoRL 的 borderline 区域——有足够的 robotics motivation 不被 desk reject，但核心贡献的 robotics specificity 仍弱于 CoRL typical acceptance。\n\n---\n\n## 方法论严谨性评估（显著提升）\n\n### 统计论证\n\n**NVE 2.0× 完美分类 (n=36, AUROC=1.000, F1=1.000)**:\n\n- 阈值从 1.5× 提升到 2.0×，实现了完美分类\n- Clean separation margin: 最低 CIVO+ NVE (2.09×) 与最高 non-CIVO NVE (1.88×) 之间有 0.21× gap\n- **LOEO 交叉验证**: 在 Appendix B.5 中确认——Walker/Cheetah/PickCube 三折 LOEO 全部 100% accuracy ✓\n- **LOCO 交叉验证**: 36/36 = 100%，zero FP across all folds ✓\n- 阈值不是 data-snooping 的结果——0.21× 的 separation gap 和多种交叉验证方式支持其泛化性\n\n**Fisher exact test (5/7 vs 0/16, p<0.001)**:\n\n正式的统计检验替代了之前的描述性比较。这是 Round 6 最重要的方法论改进之一。\n\n**Temporal ordering (n=2, r=0.81, p=0.002)**:\n\n12 dense checkpoints 的时间序列分析为 \"fidelity → value → entropy\" 因果链提供了定量证据。n=2 仍然很小，但 ~10K step onset-to-onset lag 在两个 seeds 间 consistent（10K vs 9K）。p=0.002 统计显著（though interpretation at n=2 should be cautious）。\n\n### Cheetah 机制 Dissociation\n\n这是本轮最有价值的新发现。Walker 有 1.63× reward prediction gap，Cheetah 有 NO reward gap (1.00×) yet comparable CIVO severity (8.27×)。这意味着：\n\n1. CIVO 有至少两种传播途径（reward fidelity vs dynamics-model prior drift）\n2. 之前的 \"2.78× reward prediction gap\" 叙事被修正为 environment-specific\n3. 机制理解更深入但也更复杂——论文诚实地承认 Cheetah pathway 仍 open\n\n### F6 重写（Pathway B 移除）\n\n**重大变更**：Round 3-5 报告 \"Two of four seeds collapse (50%): Pathway A (CIVO) and Pathway B (entropy increase)\"。Round 6 报告 \"none exhibits CIVO onset (peak NVE ≤0.8×)\"。\n\n这是一个 180° 的结果翻转。可能原因：\n- 008f 脚注提到 \"corrected-code rerun\"——可能发现了 code bug\n- Seed numbering changed (s0,s1,s2,s5 vs 原来的 s0-s3)\n- NVE 阈值改变（2.0× vs 1.5×）不解释 NVE 值的变化（4.02× → ≤0.8×）\n\n**方法论影响**：\n- 如果是 code correction，论文应说明修改了什么、为什么之前的结果不可靠\n- 完全移除 Pathway B 而不解释为什么之前报告了它，会降低可信度\n- 正面来看：0/4 CIVO in dt=1 imagination 是一个更 clean 的结论（\"multi-step imagination is necessary for CIVO\"），逻辑上更有力\n\n**建议**：在 Appendix 增加一段解释 F6 results 的变化原因。\n\n### 新增实验的充分性\n\n| 新增内容 | 评估 |\n|---------|------|\n| Cartpole (0/3, 3 seeds) | ✓ 好的负控制，确立 multi-joint boundary |\n| Cheetah s0 (exp_078) | ✓ 增加 Cheetah seeds 强化跨环境验证 |\n| 008f s0 corrected rerun | ⚠️ \"corrected-code\" 需要更多解释 |\n| Temporal ordering (n=2) | ✓ 有意义但 sample 小 |\n| Cosine similarity analysis | ✓ Embedding representation analysis 增加 mechanistic depth |\n| Fisher exact test | ✓ 正式统计检验 |\n\n---\n\n## 上轮遗留问题\n\n### N-R5-1 (AUTHORERR)\n**[RESOLVED but superseded]**: `main.tex:55` 添加了 `\\icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}`。但由于模板应切回 CoRL，此修复将被替换。\n\n### N-R5-2 (显示密度)\n**[RESOLVED]**: 论文为 31 页 PDF（8 页正文 + refs + 22 页 appendix），正文密度合理。CoRL 允许 8 页正文，排版无问题。\n\n### N-R5-3 (色盲友好)\n**[CANNOT VERIFY from LaTeX]**: Figure 2 caption 描述 red/blue 颜色编码，未提及 linestyle/marker 区分。建议检查。\n\n---\n\n## 新发现的问题\n\n### N-R6-1 [warning]: F6 结果完全翻转未解释\n- **位置**: results.tex:113-114\n- **问题**: 从 \"2/4 collapse (Pathway A + Pathway B)\" 变为 \"0/4 CIVO onset (NVE ≤0.8×)\"，文中未解释变化原因\n- **影响**: 降低修订过程的透明度。如果这是 code correction，应该说明\n- **建议**: 在 Appendix 增加 1 段说明 F6 修订历史\n\n### N-R6-2 [warning]: \"corrected-code rerun\" 缺乏细节\n- **位置**: results.tex:50 (Table 1 脚注 f)\n- **问题**: 008f s0 标注 \"corrected-code rerun\" 但未说明修正了什么\n- **影响**: Reviewer 会质疑：修正了什么 bug？是否影响其他实验？\n- **建议**: 在 Appendix 简述 code correction 的内容和影响范围\n\n### N-R6-3 [info]: Table 1 中 \"--- s1\" 行的 Exp 编号空白\n- **位置**: results.tex:25\n- **问题**: 008f s1 的 Exp 列显示 \"--- s1\" 而非正式实验编号，格式不一致\n\n---\n\n## ICML 维度打分（CoRL 无标准化维度，沿用 ICML 量表）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/4 (Good) | Factorial design 严谨, LOEO+LOCO 验证, Fisher exact test, temporal ordering analysis; Cheetah dissociation 增加 depth |\n| Presentation | 3/4 (Good) | F1-F7 结构清晰, Discussion 大幅扩展且有机制深度; 但 F6 翻转未解释, \"corrected-code\" 未说明 |\n| Significance | 3/4 (Good, CoRL-adjusted) | Diagnostic protocol 有方法论示范价值; multi-joint specificity + mechanism nuance; 但 CoRL 实践价值仍弱于 methodology 价值 |\n| Originality | 3/4 (Good) | Cheetah dissociation 是重要新发现; embedding cosine analysis 增加 representational insight; 四级 hierarchy 仍有新意 |\n\n---\n\n## 方法严谨性评分: 8.5/10（Round 5 为 8/10）\n\n提升 0.5 分原因:\n- NVE 2.0× 完美分类 + LOEO/LOCO 双重交叉验证\n- Fisher exact test (p<0.001) 正式化因果论证\n- Cheetah dissociation 深化机制理解\n- Temporal ordering analysis (虽然 n=2)\n- Cartpole 负控制精确化 scope boundary\n\n未达 9/10 原因:\n- F6 结果翻转未解释\n- \"corrected-code rerun\" 细节缺失\n- Temporal ordering n=2 仍然很小\n- Cheetah pathway 仍为 open question\n\n---\n\n## Overall: Weak Accept (4/6)\n\n**降级理由**（从 ICML Accept 5/6 → CoRL Weak Accept 4/6）：\n- 完全因为 venue 变化。论文方法论质量从 Round 5 到 Round 6 **提升了**，但 CoRL venue fit (6.5/10) 弱于 ICML venue fit (8.5/10)。\n- 如果论文修复模板 + 在正文中增加 1 段 robotics-specific mechanism analysis（为什么 multi-joint 周期性步态使 RSSM 对 temporal conditioning 特别脆弱），可升至 Accept (5/6)。\n\n**阻塞项**:\n1. **模板必须立即切回 CoRL PMLR**——否则 desk reject\n2. **F6 结果翻转需要至少一句话解释**——否则 reviewer 质疑数据可靠性\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 304 · 2026-05-28T00:39:03.119180+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4074
}
```

</details>

---

### Assistant

_source line 305 · 2026-05-28T00:41:05.708780+00:00_

Round 6 审稿已提交，等待 Review Director 的下一步指示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 10

22 recorded events

### User

_source line 306 · 2026-05-28T00:41:26.441750+00:00_

[Round 6 审稿请求]:
## Round 6 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

**Reviewer 2 Overall Score**: 3/6 (Weak Reject)
**Reviewer 2 核心立场**: "这是一篇好论文放在了错误的 venue"

### CRITICAL Issues

**C1: 模板仍为 ICML 2026**
R2 与你一致：main.tex 仍使用 icml2026.sty，PDF 页脚显示 ICML，desk reject 风险。

**C2: 页数合规性风险**
R2 指出：Round 6 新增大量内容（Figure 1 机制图、Mechanism evidence 段落、Discussion 5 个新段落、Table 1/2 扩展），在 CoRL 单栏格式下几乎确定超过 8 页正文。

### CoRL Venue 适配性

**R2 评分: 5.5/10（你给 6.5/10）**

R2 认为 venue fit 有微幅提升但核心矛盾未解：
1. CIVO 仍是 locomotion-specific，不出现在 manipulation 中——论文自己的数据证明了这一点
2. "Transferable diagnostic protocol" 仍是理论性的，未在 goal-conditioned/language-conditioned 场景验证
3. 无 real-robot 实验，连 sim-to-real 讨论都很有限
4. CoRL 历史上接受的 diagnostic papers 通常有 real-robot 实验
5. Actionable takeaway 仍是 "不要用 trained dt-embedding"

R2 明确建议：考虑 ICML 2026 下一 cycle 或 NeurIPS 2026 作为更合适的 venue。

### 新颖性（R2: 7/10）
- 双通路分析、temporal ordering、完美分类器有价值
- 但方法论是已有技术组合，CIVO 泛化性未知

### 新发现问题

**N-R6-1 [warning]**: F6 seed 集合变更（s1-s4 → s0,s1,s2,s5），从 "2/4 collapse" 到 "0/4 CIVO onset"，未说明原因。R2 指出 NVE threshold 变化不能解释这个翻转（原值 4.02× 和 3.78× 远超 2.0×）。

**N-R6-2 [warning]**: AUROC 从 0.957 (n=30) 到 1.000 (n=36) 的跳跃需要透明度——新增 6 个 data points 是什么？threshold 从 1.5× 到 2.0× 是 data-driven optimization 还是有 principled reason？是否 retrospective fitting？

**N-R6-3 [minor]**: DreamSmooth/NoisyNet/PETS/STEVE 引用被移除。

### R2 写作质量评分: 7.5/10
Discussion 大幅改善，Figure 1 机制图优秀，但 Abstract 仍偏数字密集，F6 seed 变更未解释。

### R2 维度评分
| 维度 | R2 评分 |
|------|---------|
| Soundness | 3/4 |
| Presentation | 3/4 |
| Significance (CoRL) | 2/4 (Fair) |
| Originality | 3/4 |

---

请对以上意见逐条回应，特别关注：
1. CoRL venue fit 评分差异（你 6.5 vs R2 5.5）——你认为 R2 的评估是否过于严格？
2. 页数合规性风险——你是否同意切换模板后可能超页？
3. F6 结果翻转——你们都提出了这个问题，但具体关注点是否一致？
4. AUROC 跳跃的透明度问题——你是否同意 R2 关于 retrospective fitting 的担忧？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 307 · 2026-05-28T00:41:35.144552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 308 · 2026-05-28T00:41:36.199069+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around seven findings (F1--F7) that trace a predictive pathway from trained temporal conditioning to pathological value dynamics. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$, \S\ref{sec:metrics}).
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
24	008f & No dt\_emb (s0) & --- & ON & 8 & 139.5 @105K$^f$ & 1.69$\times$$^f$ & Healthy$^f$ \\
25	--- s1 & No dt\_emb (s1) & --- & ON & 8 & 468.8 @105K & 0.88$\times$ & Healthy \\
26	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
27	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
28	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
29	\midrule
30	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
31	\rowcolor{gray!15}
32	010b & Cheetah Run (s1) & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
33	\rowcolor{gray
…[truncated 3291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---

### Tool call

_source line 309 · 2026-05-28T00:41:36.199516+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 310 · 2026-05-28T00:41:36.500802+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; $n{=}36$, AUROC${=}1.000$, F1${=}1.000$). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, so Double Q pessimism is ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 311 · 2026-05-28T00:41:36.551579+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
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

_source line 312 · 2026-05-28T00:41:36.602276+00:00_

1	\documentclass{article}
2	
3	% xcolor with table option must be loaded before icml2026.sty (which loads xcolor internally)
4	\PassOptionsToPackage{table}{xcolor}
5	
6	\usepackage{hyperref}
7	\newcommand{\theHalgorithm}{\arabic{algorithm}}
8	\usepackage{icml2026}
9	
10	\usepackage[utf8]{inputenc}
11	\usepackage[T1]{fontenc}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{graphicx}
16	\graphicspath{{../../artifacts/}}
17	\usepackage{colortbl}
18	\usepackage{caption}
19	\usepackage{subcaption}
20	\usepackage{array}
21	\usepackage{enumitem}
22	\usepackage{wrapfig}
23	\usepackage{algorithm}
24	\usepackage{algorithmic}
25	
26	% Custom commands
27	\newcommand{\dt}{\mathrm{dt}}
28	\newcommand{\nve}{\mathrm{nve}}
29	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
30	\newcommand{\sgseval}{448.3}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 313 · 2026-05-28T00:41:40.220044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "80",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "80",
    "limit": "120"
  }
}
```

</details>

---

### Tool result

_source line 314 · 2026-05-28T00:41:40.622345+00:00_

80	\centering
81	\includegraphics[width=0.65\columnwidth]{figures/fig1_nve_trajectory.pdf}
82	\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seeds~4 and~5 data in Table~\ref{tab:complete_results}) exceeds the $2.0\times$ diagnostic threshold in 3/5 seeds (peak NVE; sustained onset in 2/3 full-pipeline seeds, Table~\ref{tab:cross_env_civo}); dashed line shows $1.5\times$ reference; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
83	\label{fig:nve_trajectory}
84	\end{figure}
85	
86	The trained $\dt$-embedding triggers CIVO onset (NVE $\geq 2.0\times$) in 3 of 5 Walker Walk seeds, and universally degrades performance across all five to below 30\% of baseline (peak NVE $1.53$--$4.72\times$; IQM $148.8$, $n{=}5$; \citealt{agarwal2021precipice}). Including replications and Cheetah Run (\S\ref{sec:f6}), CIVO onset occurs in 5 of 7 tested multi-joint locomotion runs (71\%, two environments). Of the 5 onset runs, 3 exhibit sustained collapse, one self-corrects, and one shows NVE self-correction without policy recovery (Appendix~\ref{sec:seed_divergence}).
87	
88	\paragraph{Mechanism evidence.}
89	On Walker Walk, the RSSM reward head develops a $1.63\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning (reward MAE $0.053 \to 0.087$; Table~\ref{tab:rssm_fidelity}), while observation reconstruction improves (gap $1.35\times$ vs.\ baseline $2.04\times$). However, Cheetah Run exhibits no reward gap ($1.00\times$) despite comparable CIVO severity ($8.27\times$ NVE); reward fidelity degradation is thus one transmission pathway but not a necessary condition. Direct value calibration confirms the critic internalizes this bias: the CIVO model's mean $V(s)/\text{MC-return}$ ratio reaches $7.80\times$ (median $3.40\time
…[truncated 11424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 315 · 2026-05-28T00:41:40.873761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 316 · 2026-05-28T00:41:40.975023+00:00_

1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 45 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks self-correcting NVE without policy recovery.}
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
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\heartsuit$ & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29	\rowcolor{gray!15}
30	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31	\rowcolor{gray!15}
32	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33	\rowcolor{gray!15}
34	059 & Factorial (s
…[truncated 2113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 317 · 2026-05-28T00:41:44.841002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": "60",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "offset": "60",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 318 · 2026-05-28T00:41:44.891808+00:00_

60	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
61	\rowcolor{gray!15}
62	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
63	\rowcolor{gray!15}
64	010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\times$ & Full collapse \\
65	\rowcolor{gray!15}
66	021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Transient CIVO (self-corr.) \\
67	024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
68	024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
69	092 s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & $<$1.0$\times$$^n$ & Healthy \\
70	093 s2 & Cheetah Run & --- & ON & 8 & 151.2 @105K & $<$1.0$\times$$^n$ & Healthy \\
71	008a\_ch s0 & Cheetah Run$^k$ & exp$^a$ & OFF & 15 & 366.2 @105K & 0.45$\times$ & Healthy \\
72	008a\_ch s1 & Cheetah Run$^k$ & exp$^a$ & OFF & 15 & 281.2 @105K & 0.58$\times$ & Healthy \\
73	077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\times$ & Healthy \\
74	083 & Cheetah baseline (s1) & --- & --- & 15 & 444.0 @105K & 1.00$\times$ & Healthy \\
75	\rowcolor{gray!15}
76	078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\times$ & Onset (self-corr.) \\
77	\rowcolor{gray!15}
78	097 s3 & Cheetah trigger (s3) & trn & ON & 8 & 61.7 @105K & ${\geq}2.0\times$$^o$ & Onset (self-corr.) \\
79	\rowcolor{gray!15}
80	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
81	054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\times$$^h$ & Env.\ transient (ctrl) \\
82	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^f$ & Env.\ transient \\
83	052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\times$$^f$ & Env.\ transient \\
84	051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\times$$^f$ & Env.\ transient (ctrl) \\
85	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^g$ & Env.\ dynamics \\
86	053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 
…[truncated 6041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 319 · 2026-05-28T00:41:49.460410+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LOEO|leave-one|retrospective|threshold.*2\\.0|threshold.*1\\.5|separation gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LOEO|leave-one|retrospective|threshold.*2\\.0|threshold.*1\\.5|separation gap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 320 · 2026-05-28T00:41:50.364839+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-30-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-31-\paragraph{Normalized value-to-eval ratio ($\nve$).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-33-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex-34-\subsection{Selective Gradient Stopping}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-291-\begin{enumerate}[nosep,leftmargin=*]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-292-\item \textbf{Perfect classification.} The $2.0\times$ threshold achieves 100\% accuracy on both the $n{=}11$ factorial set and the comprehensive $n{=}36$ evaluation (AUROC${=}1.000$, F1${=}1.000$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:293:\item \textbf{Clean separation.} The lowest CIVO-positive NVE ($2.09\times$) clears the threshold by $0.09\times$; the highest non-CIVO transient ($1.88\times$, frozen-embedding exp\_057) sits $0.12\times$ below. All non-CIVO NVE transients (frozen embeddings, endpoint dips) remain below $2.0\times$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:294:\item \textbf{Robustness.} The $2.0\times$ threshold achieves perfect classification across the extended $n{=}36$ evaluation and LOEO cross-validation (Table~\ref{tab:nve_loeo}), with zero false positives across all 
…[truncated 12873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 904
}
```

</details>

---

### Tool call

_source line 321 · 2026-05-28T00:41:50.819189+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "008e_v3|F6.*seed|s1.*s4|s0.*s1.*s2.*s5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "008e_v3|F6.*seed|s1.*s4|s0.*s1.*s2.*s5",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 322 · 2026-05-28T00:41:50.869893+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-172-\vspace{1pt}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-173-{\raggedright\footnotesize
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:174:$^a$\,$N{=}4$: exp\_001 s1 (915.7), s2 (443.5), s3 (869.0), s4 (922.8); s3/s4 from cross-environment evaluation runs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-175-$^b$\,Eval: $N{=}5$ at 105K (009b, 008d\_s3, 008d\_s4, 059, 068). CIVO evaluated on $N{=}3$ seeds with full NVE pipeline (008d s0, 009e s1, 009b s2); 2/3 exceed $2.0\times$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:176:$^c$\,$N{=}4$: 008f s0 (139.5), s1 (468.8), s4 (289.3), 009c s3 (311.9).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-177-$^d$\,$N{=}2$: exp\_077 s0 (448.1), exp\_083 s1 (444.0); consistent with Table~\ref{tab:complete_results}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-178-$^e$\,$N{=}3$: exp\_010b s1 (51.7), exp\_078 s0 (119.5), exp\_097 s3 (61.7). exp\_010b s0 (eval${=}0.8$, NVE${=}108.5\times$) excluded as outlier.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-112-
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-113-\paragraph{F6: $\dt{=}1$ imagination eliminates CIVO.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:114:[Omitted long matching line]
/home/ubuntu/.agent-ml-res
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 323 · 2026-05-28T00:42:24.597853+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 324 · 2026-05-28T00:42:24.598320+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 325 · 2026-05-28T00:43:55.396101+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 交叉回应 — Reviewer 1 逐条回应 Reviewer 2\n\n---\n\n### CRITICAL Issues\n\n**[AGREE] C1: 模板仍为 ICML 2026**\n完全同意。我在 R6 独立审查中已将此列为 CRITICAL（N1）。`main.tex:8` 仍为 `\\usepackage{icml2026}`，PDF 页脚显示 ICML branding。Desk reject 风险确实存在。两位 reviewer 一致认定此问题，优先级最高。\n\n**[AGREE] C2: 页数合规性风险**\n同意这是一个实质性风险。R6 新增内容量大：Figure 1 机制图（Introduction）、Mechanism evidence + Temporal ordering 段落（Section 4.2）、Discussion 从 2 段扩展至 7 段（含 \"Causal role of embedding training\"、\"Intervention resistance reveals pathway redundancy\"、\"Transferable diagnostic protocol\"、\"Scope precision through negative controls\" 等）、Table 1/2 均有扩展。CoRL PMLR 单栏格式下每页容纳文字量远少于 ICML 双栏，正文超 8 页几乎确定。我在 R6 审查中未单独列出此项，承认这是一个疏漏——R2 的判断正确。\n\n---\n\n### CoRL Venue 适配性\n\n**[REBUT] R2 评分 5.5/10 — 我认为偏低，但承认分歧合理**\n\nR2 的五点论据逐条回应：\n\n1. **\"CIVO 仍是 locomotion-specific\"** — 事实正确，但论文自身对此有清晰界定。Section 5 \"Scope precision through negative controls\" 段落明确说 \"multi-joint locomotion reliably triggers it (5/7 seeds); single-joint dynamics (Cartpole, 0/3) and manipulation (three ManiSkill tasks, 0/3) do not\"。这种精确划界本身是科学贡献——知道一个 failure mode 的边界与知道它存在同等重要。论文没有过度泛化 claim。\n\n2. **\"Transferable diagnostic protocol 仍是理论性的\"** — 同意这是局限。但 Section 5 将其定位为 \"reusable diagnostic protocol\" 而非 verified solution，措辞审慎。对于 diagnostic paper 而言，提出 protocol 框架并在一个架构上验证是合理的第一步。\n\n3. **\"无 real-robot 实验\"** — 事实正确。但 Section 6 Limitations 已明确承认 \"not pixel-based observations, Atari, or real-robot deployments\"。CoRL 历史上确实偏好 real-robot，但也接受过纯仿真的 diagnostic/analysis 论文（如 world-model failure analysis 类工作）。\n\n4. **\"CoRL 历史上接受的 diagnostic papers 通常有 real-robot\"** — 这个 claim 需要 R2 提供具体引证。据我所知 CoRL 也接受过纯 simulation 的分析性论文，尤其是当 failure mode 对 deployment safety 有直接影响时。\n\n5. **\"Actionable takeaway 仍是不要用 trained dt-embedding\"** — 部分同意。但 R6 的 takeaway 比 R3 丰富得多：NVE 在线诊断（AUROC=1.000）、frozen embedding 修复（0/16 controls）、四级 intervention hierarchy 作为诊断框架、MPC vs imagination 的架构边界。不只是 \"别用 X\"。\n\n**我的评估**：R6 相比 R3 有实质性改进（6 environments → Fisher exact test → Cartpole negative control → temporal ordering），但核心矛盾（locomotion-specific + 无 real-robot）确实制约 CoRL fit。我维持 6.5/10，但理解 R2 的 5.5 立场。如果取中间值 6.0，我不会反对。\n\nR2 建议 ICML/NeurIPS 作为更合适 venue——我不反对这个判断，但认为这超出 reviewer 职责范围。我们的工作是评估论文是否达到 CoRL 接收标准，而非推荐替代 venue。\n\n---\n\n### 新颖性\n\n**[AGREE] R2: 7/10**\n基本同意。双通路分析（Walker reward gap vs Cheetah non-reward pathway）、temporal ordering（r=0.81, p=0.002）、NVE 完美分类器确实有价值。方法论确实是已有技术的组合（factorial design + gradient stopping + dual-critic），但组合的系统性和发现的深度超出简单拼凑。7/10 是合理评分。\n\n---\n\n### 新发现问题\n\n**[AGREE] N-R6-1: F6 seed 集合变更**\n完全同意。我在 R6 审查中将此列为 W1（Should-Fix）。我和 R2 的关注点一致：\n\n- 种子集从 s1-s4 变为 s0, s1, s2, s5\n- 结果从 \"2/4 collapse\" 完全翻转为 \"0/4 CIVO onset\"\n- NVE threshold 变化（1.5× → 2.0×）**不能**解释此翻转——R5 报告的 NVE 值（4.02× 和 3.78×）远超 2.0×\n\nR2 正确指出这一点。关键问题：这是实验重跑（corrected code？不同 version？）还是种子替换？Complete results table（Appendix Table 3）列出 008e_v3 为实验名称，暗示是 v3 版本——那 v1/v2 的结果去哪了？论文需要透明说明版本变更原因。\n\n补充一点 R2 未提及的：008f 脚注 $^f$ 说 \"Corrected-code rerun\"，008e_v3 的 \"v3\" 命名暗示类似情况，但正文中没有对 008e_v3 做同样的 corrected-code 声明。如果确实是代码修正后重跑，应该：(a) 明确说明修正了什么，(b) 解释为什么之前的代码有问题，(c) 报告旧结果作为参照。\n\n**[AGREE] N-R6-2: AUROC 跳跃的透明度**\n同意需要更多透明度，但程度上与 R2 有细微分歧。\n\n**同意部分**：\n- n=30→36 新增 6 个 data points 的身份应该明确列出\n- threshold 从 1.5× 到 2.0× 的选择依据应更清晰\n\n**部分缓解因素（R2 未充分考虑）**：\n- Appendix B.5 ROC 图标题已承认 \"Threshold calibrated and validated post-hoc\"（appendix.tex:307）——这不是隐瞒 retrospective fitting\n- LOEO 跨环境交叉验证（Walker/Cheetah/PickCube 三折，全部完美分类）在一定程度上缓解了 overfitting 担忧\n- LOCO 36/36 = 100% 进一步验证稳健性\n- 分离间隙有明确数值：最低 CIVO-positive NVE = 2.09×，最高 non-CIVO transient = 1.88×（frozen exp_057），间隔 0.21×（appendix.tex:293）\n\n**仍然成立的担忧**：0.21× 的分离间隙在绝对值上很窄。如果未来出现 NVE 在 1.9×-2.1× 之间的 borderline case，完美分类可能不成立。论文应该讨论这个 margin 的稳健性，而不仅是报告完美结果。\n\n关于 \"retrospective fitting\"：这在诊断阈值研究中是标准做法（先收集数据再确定最优阈值），但需要 out-of-sample 验证。论文提供了 LOEO 和 LOCO，这比很多同类工作做得好。我认为 R2 的担忧合理但不构成 critical issue——是 warning 级别。\n\n**[AGREE] N-R6-3: 引用移除**\n同意应记录。DreamSmooth/NoisyNet/PETS/STEVE 的移除可能是精简 Related Work 的结果，但如果这些工作与论文主题直接相关，移除需要理由。这是 minor issue。\n\n---\n\n### 写作质量\n\n**[AGREE] R2: 7.5/10**\n同意。Discussion 确实大幅改善（从 2 段到 7 段，每段有独立论点和证据）。Figure 1 机制图对理解 CIVO 有实质帮助。Abstract 数字密度问题我在 R6 中未单独标记——R2 的观察有道理，n=36/AUROC=1.000/F1=1.000 集中在一句话内确实偏密。\n\n---\n\n### R2 维度评分回应\n\n| 维度 | R2 | R1 | R1 回应 |\n|------|----|----|---------|\n| Soundness | 3/4 | — | 同意。核心方法论可靠，但 F6 翻转、n=2 temporal ordering、0.21× 分离间隙限制了满分 |\n| Presentation | 3/4 | — | 同意。R6 大幅改善但模板错误和页数风险拉低分数 |\n| Significance (CoRL) | 2/4 | — | 偏低。我给 2.5/4。locomotion-specific 确实限制 CoRL significance，但 \"when does temporal conditioning fail in imagination-based RL\" 对 world-model RL deployment 有直接意义。Frozen embedding fix + NVE diagnostic 是可操作的 |\n| Originality | 3/4 | — | 同意。CIVO 的识别和系统性诊断是原创贡献，但方法工具箱是已有技术 |\n\n---\n\n### Director 提出的四个焦点问题\n\n**Q1: CoRL venue fit 评分差异（6.5 vs 5.5）**\n分歧来源：我更重视 R6 的增量改进（6 environments、Fisher exact、Cartpole negative control、four-level protocol），R2 更重视核心结构性缺陷（locomotion-only、no real-robot）。两种视角都有道理。我认为 6.0 是公平的共识点——论文在 CoRL 的接收线上，但不舒适。\n\n**Q2: 页数合规性风险**\n同意。R6 在 ICML 双栏下已经内容饱满，切换到 CoRL 单栏后超页几乎确定。这需要大幅削减正文或将更多内容移入 appendix。Discussion 的 7 段尤其是瘦身目标。\n\n**Q3: F6 结果翻转**\n两位 reviewer 的关注点高度一致：种子集变更 + 结果翻转 + 缺乏解释。我补充了 \"v3\" 版本命名暗示代码修正但未明确声明的问题。这应升级为 **Must-Fix**——不是因为结果本身有问题，而是因为不透明的数据变更严重损害可信度。\n\n**Q4: AUROC 跳跃的 retrospective fitting**\nR2 的担忧合理但我认为论文已提供部分缓解（post-hoc 声明 + LOEO + LOCO）。需要补充的是：(a) 明确列出新增 6 个 data points，(b) 讨论 0.21× 分离间隙的稳健性。我将此定级为 **Should-Fix** 而非 Critical。\n\n---\n\n### 总体判断\n\nR2 给 3/6 (Weak Reject)，核心理由是 venue mismatch。我给 4/6 (Weak Accept)，因为论文的技术质量在 R6 有实质提升。\n\n分歧的本质：**我们对论文质量的评估接近，对 venue fit 的权重不同。** 如果 venue fit 在评分中占 40%+ 权重，R2 的 3/6 合理；如果占 20-30%，我的 4/6 更合理。CoRL 评审实践中，venue fit 是 AC 决策的重要因素但通常不是 reviewer 降分的主要依据——reviewer 更多评估 soundness 和 significance。\n\n**共识点**：模板必须修复（desk reject 风险）、F6 变更必须透明化、页数需要控制。这三个是 camera-ready 之前的硬性要求。",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 交叉回应 — Reviewer 1 逐条回应 Reviewer 2\n\n---\n\n### CRITICAL Issues\n\n**[AGREE] C1: 模板仍为 ICML 2026**\n完全同意。我在 R6 独立审查中已将此列为 CRITICAL（N1）。`main.tex:8` 仍为 `\\usepackage{icml2026}`，PDF 页脚显示 ICML branding。Desk reject 风险确实存在。两位 reviewer 一致认定此问题，优先级最高。\n\n**[AGREE] C2: 页数合规性风险**\n同意这是一个实质性风险。R6 新增内容量大：Figure 1 机制图（Introduction）、Mechanism evidence + Temporal ordering 段落（Section 4.2）、Discussion 从 2 段扩展至 7 段（含 \"Causal role of embedding training\"、\"Intervention resistance reveals pathway redundancy\"、\"Transferable diagnostic protocol\"、\"Scope precision through negative controls\" 等）、Table 1/2 均有扩展。CoRL PMLR 单栏格式下每页容纳文字量远少于 ICML 双栏，正文超 8 页几乎确定。我在 R6 审查中未单独列出此项，承认这是一个疏漏——R2 的判断正确。\n\n---\n\n### CoRL Venue 适配性\n\n**[REBUT] R2 评分 5.5/10 — 我认为偏低，但承认分歧合理**\n\nR2 的五点论据逐条回应：\n\n1. **\"CIVO 仍是 locomotion-specific\"** — 事实正确，但论文自身对此有清晰界定。Section 5 \"Scope precision through negative controls\" 段落明确说 \"multi-joint locomotion reliably triggers it (5/7 seeds); single-joint dynamics (Cartpole, 0/3) and manipulation (three ManiSkill tasks, 0/3) do not\"。这种精确划界本身是科学贡献——知道一个 failure mode 的边界与知道它存在同等重要。论文没有过度泛化 claim。\n\n2. **\"Transferable diagnostic protocol 仍是理论性的\"** — 同意这是局限。但 Section 5 将其定位为 \"reusable diagnostic protocol\" 而非 verified solution，措辞审慎。对于 diagnostic paper 而言，提出 protocol 框架并在一个架构上验证是合理的第一步。\n\n3. **\"无 real-robot 实验\"** — 事实正确。但 Section 6 Limitations 已明确承认 \"not pixel-based observations, Atari, or real-robot deployments\"。CoRL 历史上确实偏好 real-robot，但也接受过纯仿真的 diagnostic/analysis 论文（如 world-model failure analysis 类工作）。\n\n4. **\"CoRL 历史上接受的 diagnostic papers 通常有 real-robot\"** — 这个 claim 需要 R2 提供具体引证。据我所知 CoRL 也接受过纯 simulation 的分析性论文，尤其是当 failure mode 对 deployment safety 有直接影响时。\n\n5. **\"Actionable takeaway 仍是不要用 trained dt-embedding\"** — 部分同意。但 R6 的 takeaway 比 R3 丰富得多：NVE 在线诊断（AUROC=1.000）、frozen embedding 修复（0/16 controls）、四级 intervention hierarchy 作为诊断框架、MPC vs imagination 的架构边界。不只是 \"别用 X\"。\n\n**我的评估**：R6 相比 R3 有实质性改进（6 environments → Fisher exact test → Cartpole negative control → temporal ordering），但核心矛盾（locomotion-specific + 无 real-robot）确实制约 CoRL fit。我维持 6.5/10，但理解 R2 的 5.5 立场。如果取中间值 6.0，我不会反对。\n\nR2 建议 ICML/NeurIPS 作为更合适 venue——我不反对这个判断，但认为这超出 reviewer 职责范围。我们的工作是评估论文是否达到 CoRL 接收标准，而非推荐替代 venue。\n\n---\n\n### 新颖性\n\n**[AGREE] R2: 7/10**\n基本同意。双通路分析（Walker reward gap vs Cheetah non-reward pathway）、temporal ordering（r=0.81, p=0.002）、NVE 完美分类器确实有价值。方法论确实是已有技术的组合（factorial design + gradient stopping + dual-critic），但组合的系统性和发现的深度超出简单拼凑。7/10 是合理评分。\n\n---\n\n### 新发现问题\n\n**[AGREE] N-R6-1: F6 seed 集合变更**\n完全同意。我在 R6 审查中将此列为 W1（Should-Fix）。我和 R2 的关注点一致：\n\n- 种子集从 s1-s4 变为 s0, s1, s2, s5\n- 结果从 \"2/4 collapse\" 完全翻转为 \"0/4 CIVO onset\"\n- NVE threshold 变化（1.5× → 2.0×）**不能**解释此翻转——R5 报告的 NVE 值（4.02× 和 3.78×）远超 2.0×\n\nR2 正确指出这一点。关键问题：这是实验重跑（corrected code？不同 version？）还是种子替换？Complete results table（Appendix Table 3）列出 008e_v3 为实验名称，暗示是 v3 版本——那 v1/v2 的结果去哪了？论文需要透明说明版本变更原因。\n\n补充一点 R2 未提及的：008f 脚注 $^f$ 说 \"Corrected-code rerun\"，008e_v3 的 \"v3\" 命名暗示类似情况，但正文中没有对 008e_v3 做同样的 corrected-code 声明。如果确实是代码修正后重跑，应该：(a) 明确说明修正了什么，(b) 解释为什么之前的代码有问题，(c) 报告旧结果作为参照。\n\n**[AGREE] N-R6-2: AUROC 跳跃的透明度**\n同意需要更多透明度，但程度上与 R2 有细微分歧。\n\n**同意部分**：\n- n=30→36 新增 6 个 data points 的身份应该明确列出\n- threshold 从 1.5× 到 2.0× 的选择依据应更清晰\n\n**部分缓解因素（R2 未充分考虑）**：\n- Appendix B.5 ROC 图标题已承认 \"Threshold calibrated and validated post-hoc\"（appendix.tex:307）——这不是隐瞒 retrospective fitting\n- LOEO 跨环境交叉验证（Walker/Cheetah/PickCube 三折，全部完美分类）在一定程度上缓解了 overfitting 担忧\n- LOCO 36/36 = 100% 进一步验证稳健性\n- 分离间隙有明确数值：最低 CIVO-positive NVE = 2.09×，最高 non-CIVO transient = 1.88×（frozen exp_057），间隔 0.21×（appendix.tex:293）\n\n**仍然成立的担忧**：0.21× 的分离间隙在绝对值上很窄。如果未来出现 NVE 在 1.9×-2.1× 之间的 borderline case，完美分类可能不成立。论文应该讨论这个 margin 的稳健性，而不仅是报告完美结果。\n\n关于 \"retrospective fitting\"：这在诊断阈值研究中是标准做法（先收集数据再确定最优阈值），但需要 out-of-sample 验证。论文提供了 LOEO 和 LOCO，这比很多同类工作做得好。我认为 R2 的担忧合理但不构成 critical issue——是 warning 级别。\n\n**[AGREE] N-R6-3: 引用移除**\n同意应记录。DreamSmooth/NoisyNet/PETS/STEVE 的移除可能是精简 Related Work 的结果，但如果这些工作与论文主题直接相关，移除需要理由。这是 minor issue。\n\n---\n\n### 写作质量\n\n**[AGREE] R2: 7.5/10**\n同意。Discussion 确实大幅改善（从 2 段到 7 段，每段有独立论点和证据）。Figure 1 机制图对理解 CIVO 有实质帮助。Abstract 数字密度问题我在 R6 中未单独标记——R2 的观察有道理，n=36/AUROC=1.000/F1=1.000 集中在一句话内确实偏密。\n\n---\n\n### R2 维度评分回应\n\n| 维度 | R2 | R1 | R1 回应 |\n|------|----|----|---------|\n| Soundness | 3/4 | — | 同意。核心方法论可靠，但 F6 翻转、n=2 temporal ordering、0.21× 分离间隙限制了满分 |\n| Presentation | 3/4 | — | 同意。R6 大幅改善但模板错误和页数风险拉低分数 |\n| Significance (CoRL) | 2/4 | — | 偏低。我给 2.5/4。locomotion-specific 确实限制 CoRL significance，但 \"when does temporal conditioning fail in imagination-based RL\" 对 world-model RL deployment 有直接意义。Frozen embedding fix + NVE diagnostic 是可操作的 |\n| Originality | 3/4 | — | 同意。CIVO 的识别和系统性诊断是原创贡献，但方法工具箱是已有技术 |\n\n---\n\n### Director 提出的四个焦点问题\n\n**Q1: CoRL venue fit 评分差异（6.5 vs 5.5）**\n分歧来源：我更重视 R6 的增量改进（6 environments、Fisher exact、Cartpole negative control、four-level protocol），R2 更重视核心结构性缺陷（locomotion-only、no real-robot）。两种视角都有道理。我认为 6.0 是公平的共识点——论文在 CoRL 的接收线上，但不舒适。\n\n**Q2: 页数合规性风险**\n同意。R6 在 ICML 双栏下已经内容饱满，切换到 CoRL 单栏后超页几乎确定。这需要大幅削减正文或将更多内容移入 appendix。Discussion 的 7 段尤其是瘦身目标。\n\n**Q3: F6 结果翻转**\n两位 reviewer 的关注点高度一致：种子集变更 + 结果翻转 + 缺乏解释。我补充了 \"v3\" 版本命名暗示代码修正但未明确声明的问题。这应升级为 **Must-Fix**——不是因为结果本身有问题，而是因为不透明的数据变更严重损害可信度。\n\n**Q4: AUROC 跳跃的 retrospective fitting**\nR2 的担忧合理但我认为论文已提供部分缓解（post-hoc 声明 + LOEO + LOCO）。需要补充的是：(a) 明确列出新增 6 个 data points，(b) 讨论 0.21× 分离间隙的稳健性。我将此定级为 **Should-Fix** 而非 Critical。\n\n---\n\n### 总体判断\n\nR2 给 3/6 (Weak Reject)，核心理由是 venue mismatch。我给 4/6 (Weak Accept)，因为论文的技术质量在 R6 有实质提升。\n\n分歧的本质：**我们对论文质量的评估接近，对 venue fit 的权重不同。** 如果 venue fit 在评分中占 40%+ 权重，R2 的 3/6 合理；如果占 20-30%，我的 4/6 更合理。CoRL 评审实践中，venue fit 是 AC 决策的重要因素但通常不是 reviewer 降分的主要依据——reviewer 更多评估 soundness 和 significance。\n\n**共识点**：模板必须修复（desk reject 风险）、F6 变更必须透明化、页数需要控制。这三个是 camera-ready 之前的硬性要求。",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 326 · 2026-05-28T00:43:59.564605+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4168
}
```

</details>

---

### Assistant

_source line 327 · 2026-05-28T00:44:06.584122+00:00_

交叉回应已提交。核心立场：与 R2 在 C1（模板）、C2（页数）、N-R6-1（F6翻转）上完全一致；在 venue fit 评分上维持 6.5 vs R2 的 5.5（分歧来自对增量改进的权重不同）；AUROC retrospective fitting 同意需要更多透明度但认为 LOEO/LOCO 已部分缓解。建议 F6 变更升级为 Must-Fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 11

14 recorded events

### User

_source line 328 · 2026-05-28T00:50:09.632247+00:00_

[Round 6 审稿请求]:
【交叉分享准备 — 请重新提供 Round 6 审稿要点】

由于 Director 会话上下文压缩，你之前提交的 Round 6 审稿原文已丢失。为执行 Step 2 交叉分享（将你的审稿转发给 Reviewer 2），需要你重新提供一份完整的审稿要点摘要。

**背景**: 这是 Round 6 继续审稿（修订评估）。Round 5 评分 Borderline Accept (7/10)。Round 5 遗留的 3 个 open/in_progress issues：
1. N-R5-1: PDF 显示 AUTHORERR（info）
2. N-R5-2: 正文仅 6 页，display item 密度偏低（warning）
3. N-R5-3: Figure 4 红绿色块对色盲不友好（info）

**你的审查侧重（与之前相同）**: 方法严谨性 + 数据完整性。

**请提供**:
1. 对上述 3 个 open issues 的修复状态评估（RESOLVED / PARTIALLY RESOLVED / NOT FIXED）
2. 本轮发现的任何新问题（如有）
3. 维度评分（Soundness / Presentation / Originality / Significance，各 X/4）
4. 整体评分（X/6 + 文字标签）

**论文文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/submitted.pdf`
**Venue**: ICML 2026（icml2026.sty, double-blind, 正文最多 8 页 + 无限 appendix + references 不计页数）

请以结构化格式输出，不需要重新做完整审稿——只需基于你的审查侧重，快速检查上述 issues 并报告要点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 329 · 2026-05-28T00:50:43.123762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 330 · 2026-05-28T00:50:43.174549+00:00_

1	\documentclass{article}
2	
3	% xcolor with table option must be loaded before icml2026.sty (which loads xcolor internally)
4	\PassOptionsToPackage{table}{xcolor}
5	
6	\usepackage{hyperref}
7	\newcommand{\theHalgorithm}{\arabic{algorithm}}
8	\usepackage{icml2026}
9	
10	\usepackage[utf8]{inputenc}
11	\usepackage[T1]{fontenc}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{graphicx}
16	\graphicspath{{../../artifacts/}}
17	\usepackage{colortbl}
18	\usepackage{caption}
19	\usepackage{subcaption}
20	\usepackage{array}
21	\usepackage{enumitem}
22	\usepackage{wrapfig}
23	\usepackage{algorithm}
24	\usepackage{algorithmic}
25	
26	% Custom commands
27	\newcommand{\dt}{\mathrm{dt}}
28	\newcommand{\nve}{\mathrm{nve}}
29	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
30	\newcommand{\sgseval}{448.3}
31	\newcommand{\sgsnve}{1.66}
32	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
33	\usepackage{pifont}
34	\newcommand{\cmark}{\ding{51}}
35	\newcommand{\xmark}{\ding{55}}
36	\newcommand{\ie}{\textit{i.e.}}
37	\newcommand{\eg}{\textit{e.g.}}
38	\newcommand{\cf}{\textit{cf.}}
39	\newcommand{\etal}{\textit{et al.}}
40	
41	\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}
42	
43	\begin{document}
44	
45	\twocolumn[
46	  \icmltitle{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\
47	  A Diagnostic Analysis of Variable-Rate DreamerV3}
48	
49	  \begin{icmlauthorlist}
50	    \icmlauthor{Anonymous Authors}{anon}
51	  \end{icmlauthorlist}
52	
53	  \icmlaffiliation{anon}{Anonymous Institution}
54	
55	  \icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}
56	
57	  \icmlkeywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
58	
59	  \vskip 0.3in
60	]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 331 · 2026-05-28T00:50:44.078566+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "AUTHORERR|authorerr|\\\\author",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
  "output_mode": "content",
  "-C": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "AUTHORERR|authorerr|\\\\author",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
    "output_mode": "content",
    "-C": "1"
  }
}
```

</details>

---

### Tool result

_source line 332 · 2026-05-28T00:50:44.129199+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 333 · 2026-05-28T00:50:49.201031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon && find docs/paper -name \"*.tex\" -exec grep -l \"fig4\\|figure.*4\\|fig_4\" {} \\;",
  "description": "Find which tex file references Figure 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon && find docs/paper -name \"*.tex\" -exec grep -l \"fig4\\|figure.*4\\|fig_4\" {} \\;",
    "description": "Find which tex file references Figure 4"
  }
}
```

</details>

---

### Tool result

_source line 334 · 2026-05-28T00:50:49.452381+00:00_

docs/paper/sections/introduction.tex
docs/paper/sections/appendix.tex
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_1_3ba83a7f

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 335 · 2026-05-28T00:50:54.220553+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fig4_mechanism|fig_4|label\\{fig:.*4\\}|Figure.*4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fig4_mechanism|fig_4|label\\{fig:.*4\\}|Figure.*4",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 336 · 2026-05-28T00:50:54.271238+00:00_

9:\includegraphics[width=\textwidth]{figures/paper/fig4_mechanism_diagram.pdf}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 337 · 2026-05-28T00:50:59.054633+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon && wc -l docs/paper/sections/results.tex docs/paper/sections/methodology.tex docs/paper/sections/introduction.tex docs/paper/sections/analysis.tex docs/paper/sections/conclusion.tex docs/paper/sections/abstract_body.tex",
  "description": "Count lines in main body tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon && wc -l docs/paper/sections/results.tex docs/paper/sections/methodology.tex docs/paper/sections/introduction.tex docs/paper/sections/analysis.tex docs/paper/sections/conclusion.tex docs/paper/sections/abstract_body.tex",
    "description": "Count lines in main body tex files"
  }
}
```

</details>

---

### Tool result

_source line 338 · 2026-05-28T00:50:59.245031+00:00_

  197 docs/paper/sections/results.tex
   52 docs/paper/sections/methodology.tex
   22 docs/paper/sections/introduction.tex
   25 docs/paper/sections/analysis.tex
   12 docs/paper/sections/conclusion.tex
    1 docs/paper/sections/abstract_body.tex
  309 total
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_1_3ba83a7f

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 190
}
```

</details>

---

### Tool call

_source line 339 · 2026-05-28T00:51:53.694058+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 审稿要点摘要（Reviewer 1 — 方法严谨性 + 数据完整性）\n\n**Venue**: ICML 2026 | **模板**: icml2026.sty ✓ | **R5 评分**: Borderline Accept (7/10)\n\n---\n\n### 1. R5 遗留 Issues 修复状态\n\n| Issue | 状态 | 说明 |\n|-------|------|------|\n| N-R5-1: AUTHORERR | **RESOLVED** | main.tex 使用 `\\icmlauthor{Anonymous Authors}{anon}` + `\\icmlaffiliation{anon}{Anonymous Institution}`，无 AUTHORERR 残留。双盲合规。 |\n| N-R5-2: 正文仅 6 页，display item 密度偏低 | **RESOLVED** | R6 大幅扩充内容：新增 Figure 1 机制图（Introduction）、Mechanism evidence + Temporal ordering 段落（Section 4.2）、Discussion 从 2 段扩展至 7 段、Table 1/2 均有数据扩充。正文内容密度大幅提升。 |\n| N-R5-3: Figure 4 红绿色块对色盲不友好 | **NOT VERIFIED** | Figure 4（现为 fig4_mechanism_diagram.pdf，位于 Introduction）已从统计色块图改为机制概念图。原 R5 中的色盲问题图可能已被替换或移入 appendix，需 PDF 渲染确认。降级为 info，不影响评分。 |\n\n---\n\n### 2. 本轮新发现问题\n\n**N-R6-1 [warning — Should-Fix]: F6 结果完全翻转，未解释**\n- 位置：Section 4.4 (F6), Table 3 (Appendix)\n- R5 F6 报告 \"2/4 seeds collapse (Pathway A + B)\"，种子集 s1-s4\n- R6 F6 报告 \"0/4 CIVO onset (NVE ≤0.8×)\"，种子集 s0, s1, s2, s5，实验编号 008e_v3\n- NVE 阈值变化（1.5×→2.0×）无法解释此翻转——R5 报告的 NVE 值（4.02×, 3.78×）远超 2.0×\n- \"v3\" 命名暗示代码修正重跑，但正文未声明（对比 008f 有 \"corrected-code rerun\" 脚注）\n- **影响**：数据变更不透明，损害可重复性声称\n\n**N-R6-2 [warning — Should-Fix]: NVE 完美分类的透明度**\n- 位置：Section 4.2, Appendix B.5\n- AUROC 从 0.957 (n=30) 跳升至 1.000 (n=36)，threshold 从 1.5× 升至 2.0×\n- 新增 6 个 data points 的身份未在正文明确列出\n- 分离间隙仅 0.21×（最低 CIVO-positive 2.09× vs 最高 non-CIVO 1.88×）\n- **缓解因素**：ROC 图标题承认 \"Threshold calibrated and validated post-hoc\"；LOEO 三折交叉验证均完美分类；LOCO 36/36=100%\n- **仍需补充**：明确列出新增 data points 来源 + 讨论 0.21× margin 的稳健性\n\n**N-R6-3 [info]: \"Corrected-code rerun\" 缺乏细节**\n- 位置：Table 1 脚注 $^f$（008f）\n- 仅声明 \"corrected-code rerun\" 但未说明修正了什么代码错误\n- 作为论文的核心 factorial 对照实验之一，代码修正应有更多透明度\n\n---\n\n### 3. 主要优势（R6 相比 R5 的实质改进）\n\n- **统计严谨性提升**：Fisher exact test (5/7 vs 0/16, p<0.001)、NVE 完美分类 (36/36)、Clopper-Pearson CI\n- **Cheetah 机制解离**：Walker 1.63× reward gap vs Cheetah 1.00× (无 reward gap) 却有 8.27× NVE——证明 CIVO 有多条传播通路\n- **Temporal ordering (n=2)**：fidelity gap 先于 value overestimation ~10K steps (r=0.81, p=0.002)\n- **Cartpole 负对照**：single-joint 0/3 CIVO，精确划定触发边界\n- **Discussion 质量飞跃**：从 2 段泛论变为 7 段系统性分析（causal role、pathway redundancy、transferable protocol、scope precision）\n- **Dual-critic 收敛发现**：ρ>0.999 证明 Double Q pessimism 在 pure imagination 中结构性失效\n\n---\n\n### 4. 维度评分\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| **Soundness** | 3.5/4 | 核心 claim 有充分实验支撑（36/36 分类、Fisher exact、LOEO/LOCO）。扣分：F6 结果翻转未解释、temporal ordering 仅 n=2、分离间隙窄 |\n| **Presentation** | 3/4 | Discussion 大幅改善、Figure 1 机制图优秀。扣分：F6 数据变更不透明、\"corrected-code rerun\" 缺细节、Abstract 数字偏密 |\n| **Originality** | 3/4 | CIVO 的识别 + 双通路分析 + dual-critic 收敛发现是原创。方法工具箱（factorial + SGS + dual-critic）是已有技术组合 |\n| **Significance** | 3/4 | 对 world-model RL temporal conditioning 社区有明确贡献。Frozen embedding fix + NVE diagnostic 可直接使用。受限于 locomotion-specific |\n\n---\n\n### 5. 整体评分\n\n**5/6 — Weak Accept**\n\nR5 给 Borderline Accept (7/10, 映射约 4.5/6)。R6 在统计严谨性、机制分析深度、cross-environment 验证上有实质性改进，足以上调半级。主要保留意见：F6 数据变更透明度 + NVE 分离间隙讨论不足。如果这两个 Should-Fix 在 camera-ready 中解决，我对接收没有异议。\n\n**一句话总结**：R6 将一个有趣但证据不足的诊断观察升级为一个统计严谨的 failure mode 表征，method rigor 从 R5 的 8/10 提升至 8.5/10，主要残留问题是数据变更透明度而非方法论缺陷。",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 审稿要点摘要（Reviewer 1 — 方法严谨性 + 数据完整性）\n\n**Venue**: ICML 2026 | **模板**: icml2026.sty ✓ | **R5 评分**: Borderline Accept (7/10)\n\n---\n\n### 1. R5 遗留 Issues 修复状态\n\n| Issue | 状态 | 说明 |\n|-------|------|------|\n| N-R5-1: AUTHORERR | **RESOLVED** | main.tex 使用 `\\icmlauthor{Anonymous Authors}{anon}` + `\\icmlaffiliation{anon}{Anonymous Institution}`，无 AUTHORERR 残留。双盲合规。 |\n| N-R5-2: 正文仅 6 页，display item 密度偏低 | **RESOLVED** | R6 大幅扩充内容：新增 Figure 1 机制图（Introduction）、Mechanism evidence + Temporal ordering 段落（Section 4.2）、Discussion 从 2 段扩展至 7 段、Table 1/2 均有数据扩充。正文内容密度大幅提升。 |\n| N-R5-3: Figure 4 红绿色块对色盲不友好 | **NOT VERIFIED** | Figure 4（现为 fig4_mechanism_diagram.pdf，位于 Introduction）已从统计色块图改为机制概念图。原 R5 中的色盲问题图可能已被替换或移入 appendix，需 PDF 渲染确认。降级为 info，不影响评分。 |\n\n---\n\n### 2. 本轮新发现问题\n\n**N-R6-1 [warning — Should-Fix]: F6 结果完全翻转，未解释**\n- 位置：Section 4.4 (F6), Table 3 (Appendix)\n- R5 F6 报告 \"2/4 seeds collapse (Pathway A + B)\"，种子集 s1-s4\n- R6 F6 报告 \"0/4 CIVO onset (NVE ≤0.8×)\"，种子集 s0, s1, s2, s5，实验编号 008e_v3\n- NVE 阈值变化（1.5×→2.0×）无法解释此翻转——R5 报告的 NVE 值（4.02×, 3.78×）远超 2.0×\n- \"v3\" 命名暗示代码修正重跑，但正文未声明（对比 008f 有 \"corrected-code rerun\" 脚注）\n- **影响**：数据变更不透明，损害可重复性声称\n\n**N-R6-2 [warning — Should-Fix]: NVE 完美分类的透明度**\n- 位置：Section 4.2, Appendix B.5\n- AUROC 从 0.957 (n=30) 跳升至 1.000 (n=36)，threshold 从 1.5× 升至 2.0×\n- 新增 6 个 data points 的身份未在正文明确列出\n- 分离间隙仅 0.21×（最低 CIVO-positive 2.09× vs 最高 non-CIVO 1.88×）\n- **缓解因素**：ROC 图标题承认 \"Threshold calibrated and validated post-hoc\"；LOEO 三折交叉验证均完美分类；LOCO 36/36=100%\n- **仍需补充**：明确列出新增 data points 来源 + 讨论 0.21× margin 的稳健性\n\n**N-R6-3 [info]: \"Corrected-code rerun\" 缺乏细节**\n- 位置：Table 1 脚注 $^f$（008f）\n- 仅声明 \"corrected-code rerun\" 但未说明修正了什么代码错误\n- 作为论文的核心 factorial 对照实验之一，代码修正应有更多透明度\n\n---\n\n### 3. 主要优势（R6 相比 R5 的实质改进）\n\n- **统计严谨性提升**：Fisher exact test (5/7 vs 0/16, p<0.001)、NVE 完美分类 (36/36)、Clopper-Pearson CI\n- **Cheetah 机制解离**：Walker 1.63× reward gap vs Cheetah 1.00× (无 reward gap) 却有 8.27× NVE——证明 CIVO 有多条传播通路\n- **Temporal ordering (n=2)**：fidelity gap 先于 value overestimation ~10K steps (r=0.81, p=0.002)\n- **Cartpole 负对照**：single-joint 0/3 CIVO，精确划定触发边界\n- **Discussion 质量飞跃**：从 2 段泛论变为 7 段系统性分析（causal role、pathway redundancy、transferable protocol、scope precision）\n- **Dual-critic 收敛发现**：ρ>0.999 证明 Double Q pessimism 在 pure imagination 中结构性失效\n\n---\n\n### 4. 维度评分\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| **Soundness** | 3.5/4 | 核心 claim 有充分实验支撑（36/36 分类、Fisher exact、LOEO/LOCO）。扣分：F6 结果翻转未解释、temporal ordering 仅 n=2、分离间隙窄 |\n| **Presentation** | 3/4 | Discussion 大幅改善、Figure 1 机制图优秀。扣分：F6 数据变更不透明、\"corrected-code rerun\" 缺细节、Abstract 数字偏密 |\n| **Originality** | 3/4 | CIVO 的识别 + 双通路分析 + dual-critic 收敛发现是原创。方法工具箱（factorial + SGS + dual-critic）是已有技术组合 |\n| **Significance** | 3/4 | 对 world-model RL temporal conditioning 社区有明确贡献。Frozen embedding fix + NVE diagnostic 可直接使用。受限于 locomotion-specific |\n\n---\n\n### 5. 整体评分\n\n**5/6 — Weak Accept**\n\nR5 给 Borderline Accept (7/10, 映射约 4.5/6)。R6 在统计严谨性、机制分析深度、cross-environment 验证上有实质性改进，足以上调半级。主要保留意见：F6 数据变更透明度 + NVE 分离间隙讨论不足。如果这两个 Should-Fix 在 camera-ready 中解决，我对接收没有异议。\n\n**一句话总结**：R6 将一个有趣但证据不足的诊断观察升级为一个统计严谨的 failure mode 表征，method rigor 从 R5 的 8/10 提升至 8.5/10，主要残留问题是数据变更透明度而非方法论缺陷。",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 340 · 2026-05-28T00:51:57.611997+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---

### Assistant

_source line 341 · 2026-05-28T00:52:02.447343+00:00_

已提交 Round 6 审稿要点摘要。包含：3 个 R5 遗留 issue 状态（2 RESOLVED, 1 NOT VERIFIED）、3 个新发现问题（F6 结果翻转、AUROC 透明度、corrected-code 细节）、四维度评分（Soundness 3.5/4, Presentation 3/4, Originality 3/4, Significance 3/4）、整体 5/6 Weak Accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 12

4 recorded events

### User

_source line 342 · 2026-05-28T01:01:01.013799+00:00_

[Round 6 审稿请求]:
【Step 2 交叉分享 — Reviewer 2 的 Round 6 审稿意见】

以下是 Reviewer 2 的完整 Round 6 审稿意见（ICML 2026 标准）。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

**重点关注**：
1. R2 Soundness 3/4 vs 你的 3.5/4 —— 差异是否有实质依据？
2. R2 Overall 4/6 vs 你的 5/6 —— 核心分歧在哪？
3. F6 透明度问题是否升级为 Must-Fix？

---

## Reviewer 2 审稿意见原文

### R5 遗留 Issues 修复状态

- N-R5-1 AUTHORERR: **RESOLVED**。PDF page 1 脚注正确，`\icmlcorrespondingauthor` 已添加。
- N-R5-2 正文 6 页: **RESOLVED**。扩展至 8 页，6 display items / 8 页正文。Discussion 新增 5 段。
- N-R5-3 色盲: **PARTIALLY RESOLVED**。线型冗余改善但红/绿未完全消除。

### 新发现

**N-R6-1 [warning] F6 结果 180° 翻转未解释**
- R5 F6 报告 "2/4 collapse (50%)"（seeds s1-s4），R6 变为 "0/4 CIVO onset"（seeds s0,s1,s2,s5）
- Seed 集合更换（s3,s4 消失，s0,s5 出现）且结论从 "dt=1 无法完全阻止 CIVO" 翻转为 "dt=1 消除 CIVO"
- 论文未解释这一变化。两个结论互斥，需要透明交代。

**N-R6-2 [warning] "corrected-code rerun" 透明度不足**
- 008f 标注 corrected-code rerun 但未说明 bug 内容、影响范围、修正前后结果差异
- 直接影响 Table 2 "Removed: 6/6 (100%)" 的可信度

**N-R6-3 [info] AUROC 演进缺乏透明度**
- NVE threshold 1.5× → 2.0×，n=30 → 36，AUROC 0.957 → 1.000
- LOEO 交叉验证部分缓解，但 reviewer 会追问

**N-R6-4 [info] Table 1 "--- s1" 格式**

### 维度评分

| 维度 | 评分 |
|------|------|
| Soundness | 3/4 |
| Presentation | 3/4 |
| Originality | 3/4 |
| Significance (ICML) | 3/4 |

### Overall: 4/6 (Weak Accept)
未升 5/6 原因：F6 + seed 更换 + corrected-code 三重透明度问题叠加。ICML venue fit: 8.5/10。

---

请逐条回应 R2 的发现和评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 343 · 2026-05-28T01:01:51.535780+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 交叉回应 — Reviewer 1 逐条回应 Reviewer 2（ICML 2026）\n\n---\n\n### R5 遗留 Issues\n\n**[AGREE] N-R5-1 AUTHORERR: RESOLVED**\n一致。我已独立确认 main.tex:49-55 使用 `\\icmlauthor{Anonymous Authors}{anon}` + `\\icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}`，无 AUTHORERR。\n\n**[AGREE] N-R5-2 正文 6 页: RESOLVED**\n一致。R6 内容量大幅提升，display items 密度合理。\n\n**[AGREE] N-R5-3 色盲: PARTIALLY RESOLVED**\n接受 R2 的判断。我标注为 NOT VERIFIED（未渲染 PDF 确认），R2 给出了更精确的评估。Info 级别，不影响评分。\n\n---\n\n### 新发现\n\n**[AGREE] N-R6-1: F6 结果 180° 翻转未解释**\n完全同意，我在独立审查中将此列为 W1（Should-Fix）。两位 reviewer 的关注点高度一致：\n\n- 种子集变更（s3,s4 消失，s0,s5 出现）未交代\n- 结论互斥：R5 \"dt=1 无法完全阻止 CIVO\" vs R6 \"dt=1 消除 CIVO\"\n- 实验编号从 008e 变为 008e_v3，暗示代码修正重跑，但正文未声明\n\n补充一点：008e_v3 的 \"v3\" 与 008f 的 \"corrected-code rerun\" 脚注形成对比——后者至少承认了代码修正，前者完全静默。**我同意将此升级为 Must-Fix**——两个互斥结论之间的数据变更不透明，这不是措辞问题而是科学诚信的基本要求。\n\n**[AGREE] N-R6-2: \"corrected-code rerun\" 透明度不足**\n同意。我在独立审查中将此列为 N-R6-3（info 级别），但 R2 的分析说服我应提高严重性。R2 正确指出这直接影响 Table 2 \"Removed: 6/6 (100%)\" 的可信度——如果 008f 是修正后重跑，那修正前结果是什么？修正前 008f 是否也是 healthy？如果是，6/6 统计不变；如果不是，则修正前数据被 cherry-pick 式替换。\n\n论文 Table 3 脚注 $^l$ 提供了部分信息：\"pre-correction data (eval 503.0, NVE 0.97×) superseded\"——修正前 NVE=0.97× 仍低于 2.0× threshold，仍分类为 non-CIVO。因此 6/6 统计事实上不受影响。但这个信息埋在 appendix 脚注中，正文应直接交代。升级为 **warning** 合理。\n\n**[AGREE] N-R6-3: AUROC 演进缺乏透明度**\n同意。我在独立审查中也标注此问题。LOEO/LOCO 交叉验证是有效缓解，但新增 6 个 data points 的来源应明确列出。ROC 图标题已承认 \"post-hoc\"（Appendix B.5），这是诚实的，但正文应更显式地讨论。Info 级别合理。\n\n**[AGREE] N-R6-4: Table 1 \"--- s1\" 格式**\n同意。Minor formatting issue。\n\n---\n\n### 维度评分差异分析\n\n**Soundness: R2 3/4 vs R1 3.5/4**\n\n差距 0.5 分。R2 扣分理由：F6 翻转 + seed 更换 + corrected-code 三重透明度叠加。我扣分理由：F6 翻转 + temporal ordering n=2 + 分离间隙 0.21×。\n\n评估后我认为分歧不具实质性——我们识别的核心问题相同（F6 透明度），只是权重略不同。R2 更重视 corrected-code 对 Table 2 统计的影响，我更重视 statistical margin 的脆弱性。两种视角互补。\n\n**我愿意调整至 3.25/4**，承认 corrected-code 透明度问题的权重应略高于我初始评估。\n\n**Significance: R2 3/4 vs R1 3/4**\n一致，无分歧。\n\n**Presentation / Originality: 均 3/4**\n一致，无分歧。\n\n---\n\n### Overall: R2 4/6 vs R1 5/6 — 核心分歧\n\nR2 未升 5/6 的理由：\"F6 + seed 更换 + corrected-code 三重透明度问题叠加\"。\n\n我给 5/6 的理由：R6 在统计严谨性（Fisher exact、AUROC=1.000、LOEO/LOCO）、机制分析（Cheetah 解离、temporal ordering）、experimental scope（6 environments、Cartpole 负对照）上均有实质改进，这些改进的科学价值超过透明度缺陷的扣分。\n\n**反思后的判断**：R2 的 \"三重叠加\" 论点有说服力。单看任何一个透明度问题都是 warning 级别，但三个同时存在（F6 结论翻转 + corrected-code 未说明 + AUROC 数据变更）构成了一个 pattern——即作者在数据/代码变更时未充分交代。这个 pattern 是否足以从 5 降至 4，取决于是否认为这反映了系统性的 reporting 问题还是孤立的疏忽。\n\n**我调整为 4.5/6**——承认透明度问题比我初始评估更严重（三重叠加 > 单一 warning），但仍认为技术贡献足以支撑 weak accept 区间的上端。如果 F6 透明度在 camera-ready 中解决（升级为 Must-Fix 后这是预期的），我的评分回到 5/6。\n\n---\n\n### Director 三个焦点问题\n\n**Q1: Soundness 3/4 vs 3.5/4**\n分歧不具实质性。调整至 3.25/4 作为共识点。核心问题一致：透明度缺陷，非方法论缺陷。\n\n**Q2: Overall 4/6 vs 5/6**\n核心分歧在于透明度问题的权重。R2 将三重叠加视为系统性 reporting 问题（足以阻止升级），我初始将其视为孤立疏忽（不阻止升级）。反思后调整至 4.5/6。\n\n**Q3: F6 升级为 Must-Fix？**\n**同意升级**。理由充分：两个互斥结论（\"无法阻止\" vs \"消除\"）之间的数据变更未交代，这是科学报告的基本要求。建议 camera-ready 中至少需要：(a) 说明 008e→008e_v3 的代码变更内容，(b) 报告旧结果作为参照，(c) 解释种子集变更原因。\n\n---\n\n### 最终评分（调整后）\n\n| 维度 | R1 调整后 | R2 | 共识区间 |\n|------|-----------|-----|----------|\n| Soundness | 3.25/4 | 3/4 | 3-3.25 |\n| Presentation | 3/4 | 3/4 | 3 |\n| Originality | 3/4 | 3/4 | 3 |\n| Significance | 3/4 | 3/4 | 3 |\n| **Overall** | **4.5/6** | **4/6** | **4-4.5 (Weak Accept)** |\n\n两位 reviewer 共识：Weak Accept 区间，条件是 F6 透明度问题在 camera-ready 中解决。ICML venue fit 无争议（8.5/10）。",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 交叉回应 — Reviewer 1 逐条回应 Reviewer 2（ICML 2026）\n\n---\n\n### R5 遗留 Issues\n\n**[AGREE] N-R5-1 AUTHORERR: RESOLVED**\n一致。我已独立确认 main.tex:49-55 使用 `\\icmlauthor{Anonymous Authors}{anon}` + `\\icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}`，无 AUTHORERR。\n\n**[AGREE] N-R5-2 正文 6 页: RESOLVED**\n一致。R6 内容量大幅提升，display items 密度合理。\n\n**[AGREE] N-R5-3 色盲: PARTIALLY RESOLVED**\n接受 R2 的判断。我标注为 NOT VERIFIED（未渲染 PDF 确认），R2 给出了更精确的评估。Info 级别，不影响评分。\n\n---\n\n### 新发现\n\n**[AGREE] N-R6-1: F6 结果 180° 翻转未解释**\n完全同意，我在独立审查中将此列为 W1（Should-Fix）。两位 reviewer 的关注点高度一致：\n\n- 种子集变更（s3,s4 消失，s0,s5 出现）未交代\n- 结论互斥：R5 \"dt=1 无法完全阻止 CIVO\" vs R6 \"dt=1 消除 CIVO\"\n- 实验编号从 008e 变为 008e_v3，暗示代码修正重跑，但正文未声明\n\n补充一点：008e_v3 的 \"v3\" 与 008f 的 \"corrected-code rerun\" 脚注形成对比——后者至少承认了代码修正，前者完全静默。**我同意将此升级为 Must-Fix**——两个互斥结论之间的数据变更不透明，这不是措辞问题而是科学诚信的基本要求。\n\n**[AGREE] N-R6-2: \"corrected-code rerun\" 透明度不足**\n同意。我在独立审查中将此列为 N-R6-3（info 级别），但 R2 的分析说服我应提高严重性。R2 正确指出这直接影响 Table 2 \"Removed: 6/6 (100%)\" 的可信度——如果 008f 是修正后重跑，那修正前结果是什么？修正前 008f 是否也是 healthy？如果是，6/6 统计不变；如果不是，则修正前数据被 cherry-pick 式替换。\n\n论文 Table 3 脚注 $^l$ 提供了部分信息：\"pre-correction data (eval 503.0, NVE 0.97×) superseded\"——修正前 NVE=0.97× 仍低于 2.0× threshold，仍分类为 non-CIVO。因此 6/6 统计事实上不受影响。但这个信息埋在 appendix 脚注中，正文应直接交代。升级为 **warning** 合理。\n\n**[AGREE] N-R6-3: AUROC 演进缺乏透明度**\n同意。我在独立审查中也标注此问题。LOEO/LOCO 交叉验证是有效缓解，但新增 6 个 data points 的来源应明确列出。ROC 图标题已承认 \"post-hoc\"（Appendix B.5），这是诚实的，但正文应更显式地讨论。Info 级别合理。\n\n**[AGREE] N-R6-4: Table 1 \"--- s1\" 格式**\n同意。Minor formatting issue。\n\n---\n\n### 维度评分差异分析\n\n**Soundness: R2 3/4 vs R1 3.5/4**\n\n差距 0.5 分。R2 扣分理由：F6 翻转 + seed 更换 + corrected-code 三重透明度叠加。我扣分理由：F6 翻转 + temporal ordering n=2 + 分离间隙 0.21×。\n\n评估后我认为分歧不具实质性——我们识别的核心问题相同（F6 透明度），只是权重略不同。R2 更重视 corrected-code 对 Table 2 统计的影响，我更重视 statistical margin 的脆弱性。两种视角互补。\n\n**我愿意调整至 3.25/4**，承认 corrected-code 透明度问题的权重应略高于我初始评估。\n\n**Significance: R2 3/4 vs R1 3/4**\n一致，无分歧。\n\n**Presentation / Originality: 均 3/4**\n一致，无分歧。\n\n---\n\n### Overall: R2 4/6 vs R1 5/6 — 核心分歧\n\nR2 未升 5/6 的理由：\"F6 + seed 更换 + corrected-code 三重透明度问题叠加\"。\n\n我给 5/6 的理由：R6 在统计严谨性（Fisher exact、AUROC=1.000、LOEO/LOCO）、机制分析（Cheetah 解离、temporal ordering）、experimental scope（6 environments、Cartpole 负对照）上均有实质改进，这些改进的科学价值超过透明度缺陷的扣分。\n\n**反思后的判断**：R2 的 \"三重叠加\" 论点有说服力。单看任何一个透明度问题都是 warning 级别，但三个同时存在（F6 结论翻转 + corrected-code 未说明 + AUROC 数据变更）构成了一个 pattern——即作者在数据/代码变更时未充分交代。这个 pattern 是否足以从 5 降至 4，取决于是否认为这反映了系统性的 reporting 问题还是孤立的疏忽。\n\n**我调整为 4.5/6**——承认透明度问题比我初始评估更严重（三重叠加 > 单一 warning），但仍认为技术贡献足以支撑 weak accept 区间的上端。如果 F6 透明度在 camera-ready 中解决（升级为 Must-Fix 后这是预期的），我的评分回到 5/6。\n\n---\n\n### Director 三个焦点问题\n\n**Q1: Soundness 3/4 vs 3.5/4**\n分歧不具实质性。调整至 3.25/4 作为共识点。核心问题一致：透明度缺陷，非方法论缺陷。\n\n**Q2: Overall 4/6 vs 5/6**\n核心分歧在于透明度问题的权重。R2 将三重叠加视为系统性 reporting 问题（足以阻止升级），我初始将其视为孤立疏忽（不阻止升级）。反思后调整至 4.5/6。\n\n**Q3: F6 升级为 Must-Fix？**\n**同意升级**。理由充分：两个互斥结论（\"无法阻止\" vs \"消除\"）之间的数据变更未交代，这是科学报告的基本要求。建议 camera-ready 中至少需要：(a) 说明 008e→008e_v3 的代码变更内容，(b) 报告旧结果作为参照，(c) 解释种子集变更原因。\n\n---\n\n### 最终评分（调整后）\n\n| 维度 | R1 调整后 | R2 | 共识区间 |\n|------|-----------|-----|----------|\n| Soundness | 3.25/4 | 3/4 | 3-3.25 |\n| Presentation | 3/4 | 3/4 | 3 |\n| Originality | 3/4 | 3/4 | 3 |\n| Significance | 3/4 | 3/4 | 3 |\n| **Overall** | **4.5/6** | **4/6** | **4-4.5 (Weak Accept)** |\n\n两位 reviewer 共识：Weak Accept 区间，条件是 F6 透明度问题在 camera-ready 中解决。ICML venue fit 无争议（8.5/10）。",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 344 · 2026-05-28T01:01:55.555767+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4019
}
```

</details>

---

### Assistant

_source line 345 · 2026-05-28T01:02:00.673184+00:00_

交叉回应已提交。核心结论：

- **Soundness** 调整至 3.25/4（向 R2 靠拢，承认 corrected-code 透明度权重应更高）
- **Overall** 调整至 4.5/6（从 5 降半级，认可 R2 "三重透明度叠加" 论点）
- **F6 升级为 Must-Fix**——两位 reviewer 一致同意
- 两位 reviewer 共识区间：Weak Accept (4-4.5/6)，条件是 F6 透明度问题在 camera-ready 解决

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 13

122 recorded events

### User

_source line 346 · 2026-05-28T02:01:44.997497+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查本论文的 **方法严谨性 + 实验设计 + 数据透明度**。

## 论文信息
- **标题**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
- **论文路径**: projects/event-gated-adaptive-horizon/docs/paper/main.tex
- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf
- **目标 venue**: CoRL 2026 (10th Conference on Robot Learning)
- **截止日期**: 2026-05-28

## CoRL 2026 格式要求（实时搜索确认）
- **页数限制**: 8 页正文内容 + 无限引用页（camera-ready 9 页）
- **模板**: CoRL PMLR 模板 (corl_2026.sty)
- **审稿制度**: Double-blind（匿名）
- **必须包含**: Limitations section（计入 8 页限制）
- **核心要求**: 论文必须聚焦核心机器人问题，展示对机器人领域的相关性
- **附录**: 可选，通过 OpenReview 提交补充材料

## 你的审查侧重

1. **方法论严谨性**:
   - CIVO (conditioning-induced value overestimation) 的定义和诊断指标 (NVE) 是否严谨
   - NVE 阈值 2.0× 的选择是否有充分的统计验证（AUROC, LOEO, LOCO）
   - Factorial design 是否正确隔离了因果因素
   - 因果/预测性声明的措辞是否与实验证据强度匹配

2. **实验设计与统计**:
   - 4-5 seeds 的统计效力是否足够支撑声明
   - n=36 分类实验的样本构成是否合理（CIVO-positive vs non-CIVO 比例）
   - 干预实验（SGS, TCN, RAVE, dual-critic）的对照是否充分
   - IQM + bootstrap CI 的使用是否正确

3. **数据透明度**:
   - Table 1 中的脚注 f ("corrected-code rerun") 是否有充分解释
   - 008e_v3 seed 集合变更和结果翻转是否透明记录
   - 是否存在 cherry-picking 或 post-hoc 选择性报告的风险
   - Appendix 中数据与正文叙述是否一致

请提供完整的结构化审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → 评分建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 347 · 2026-05-28T02:01:54.274015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 348 · 2026-05-28T02:01:54.324787+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_1_3ba83a7f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 349 · 2026-05-28T02:01:54.425616+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
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

_source line 350 · 2026-05-28T02:01:54.528040+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 351 · 2026-05-28T02:01:59.349242+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 352 · 2026-05-28T02:01:59.702989+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 review form scoring dimensions robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 review form scoring dimensions robot learning"
  }
}
```

</details>

---

### Tool call

_source line 353 · 2026-05-28T02:02:00.758872+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
  "project": "event-gated-adaptive-horizon",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
    "project": "event-gated-adaptive-horizon",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 354 · 2026-05-28T02:02:05.789904+00:00_

Web search results for query: "CoRL 2026 review form scoring dimensions robot learning"

Links: [{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"Instruments for Measuring Psychological Dimensions in Human-Robot Interaction: Systematic Review of Psychometric Properties","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11187516/"},{"title":"Back to Reality for Imitation Learning","url":"https://arxiv.org/pdf/2111.12867"}]

Based on the search results, I found information about CoRL 2026 but not specific details about the review form scoring dimensions. Here's what I found:

CoRL 2026 is a premier annual event dedicated to the intersection of robotics, machine learning, and control, scheduled for November 10–12, 2026, in Austin, Texas.

The aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning, and it is a selective, single-track international conference addressing theory and practice of machine learning for robots.

Regarding the review process, the conference aims to have at least two reviewers per paper.

However, the search results did not contain specific information about the review form's scoring dimensions. To find the detailed scoring criteria, you may want to check the official OpenReview platform at https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference or contact the conference organizers directly, as specific review rubrics are often p
…[truncated 141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6086
}
```

</details>

---

### Tool result

_source line 355 · 2026-05-28T02:02:07.249886+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on my search results, I found information related to CoRL 2026 submission requirements and review criteria, though the specific detailed reviewer guidelines form was not fully available in the search results. Here's what I found:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal. Additionally, every author with 3 or more submissions must agree to serve as a reviewer.

## Review Criteria

While I couldn't find the complete 2026 reviewer guidelines form specifically, based on the 2024 CoRL review criteria: Submissions will be evaluated based on the significance and novelty of the results, either theoretical or empirical.

For more detailed and current information about the CoRL 2026 specific reviewer guidelines and review form criteria, I recommend visiting the official CoRL 2026 website directly at corl.org or checking
…[truncated 208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7900
}
```

</details>

---

### Tool result

_source line 356 · 2026-05-28T02:02:08.907061+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 315.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 290.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 340.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 318.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 362.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 269.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 389.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 266.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8148
}
```

</details>

---

### Tool call

_source line 357 · 2026-05-28T02:02:15.718312+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form dimensions, scoring criteria, rating scales, and specific instructions for reviewers. Include all scoring dimensions (e.g., soundness, novelty, clarity, significance, etc.) and their definitions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form dimensions, scoring criteria, rating scales, and specific instructions for reviewers. Include all scoring dimensions (e.g., soundness, novelty, clarity, significance, etc.) and their definitions."
  }
}
```

</details>

---

### Tool call

_source line 358 · 2026-05-28T02:02:16.724585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 359 · 2026-05-28T02:02:17.232641+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---

### Tool call

_source line 360 · 2026-05-28T02:02:17.233204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 361 · 2026-05-28T02:02:17.584887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 362 · 2026-05-28T02:02:18.543175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---

### Tool result

_source line 363 · 2026-05-28T02:02:18.546786+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---

### Tool call

_source line 364 · 2026-05-28T02:02:18.547294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 365 · 2026-05-28T02:02:18.848505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 366 · 2026-05-28T02:02:18.953254+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---

### Tool result

_source line 367 · 2026-05-28T02:02:19.357211+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---

### Tool result

_source line 368 · 2026-05-28T02:02:20.110207+00:00_

# CoRL 2024 Review Criteria Analysis

Based on the provided webpage content, the document does **not contain a complete review form** with detailed scoring dimensions, rating scales, or specific numerical criteria.

## What Is Included

The page outlines only **high-level evaluation principles**:

**Review Criteria for Regular Papers:**
- Papers are judged on "significance and novelty of the results, either theoretical or empirical"
- Assessment considers "the degree to which they have been objectively established and/or their potential for scientific and technological impact"
- Relevance to robotic learning is required
- Both experimental and theoretical results are welcomed

## What Is Missing

The document does not provide:
- Specific scoring dimensions (e.g., soundness, novelty, clarity, significance)
- Numerical rating scales (e.g., 1-5 or 1-10 scales)
- Detailed rubrics for each dimension
- Specific review form templates or instructions
- Guidance on weighting different evaluation criteria

## Additional Context

The page includes desk rejection criteria focused on formatting, anonymity, and scope relevance, but these are distinct from the actual review scoring mechanism that would appear on reviewer evaluation forms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4391
}
```

</details>

---

### Tool call

_source line 369 · 2026-05-28T02:02:24.831264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 370 · 2026-05-28T02:02:25.284849+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 371 · 2026-05-28T02:02:25.310162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 372 · 2026-05-28T02:02:25.782030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 373 · 2026-05-28T02:02:26.383211+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1073
}
```

</details>

---

### Tool call

_source line 374 · 2026-05-28T02:02:26.394277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 375 · 2026-05-28T02:02:26.896335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 376 · 2026-05-28T02:02:26.954294+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1172
}
```

</details>

---

### Tool result

_source line 377 · 2026-05-28T02:02:28.033773+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1639
}
```

</details>

---

### Tool result

_source line 378 · 2026-05-28T02:02:29.314726+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2418
}
```

</details>

---

### Tool call

_source line 379 · 2026-05-28T02:02:36.144859+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
  "project": "event-gated-adaptive-horizon",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
    "project": "event-gated-adaptive-horizon",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 380 · 2026-05-28T02:02:36.650719+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2024 OpenReview review form soundness significance clarity rating scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2024 OpenReview review form soundness significance clarity rating scale"
  }
}
```

</details>

---

### Tool result

_source line 381 · 2026-05-28T02:02:38.313332+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 362.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 314.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 336.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 360.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 390.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 262.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 283.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p18.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 354.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review
…[truncated 566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2168
}
```

</details>

---

### Tool result

_source line 382 · 2026-05-28T02:02:44.407285+00:00_

Web search results for query: "CoRL 2025 2024 OpenReview review form soundness significance clarity rating scale"

Links: [{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"2025 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2025/ReviewerGuidelines"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found some information about CoRL review processes. Here's what I discovered:

For CoRL 2024, submissions were evaluated based on the significance and novelty of the results, either theoretical or empirical.

For context on how robotics and machine learning conferences structure their review forms, CoRL 2023's review form evaluated originality, quality, clarity, significance, relevance and limitations of work.

However, the search results did not provide specific details about the exact rating scales used for soundness, significance, and clarity in the CoRL 2025 or 2024 OpenReview forms. The OpenReview pages for CoRL 2025 and 2024 (shown in the search results) appear to have minimal publicly visible content in the excerpts returned.

To get the detailed rating scale information you're looking for, you would likely need to visit the OpenReview pages directly:
- CoRL 2025: https://openreview.net/group?id=robot-learning.org/CoRL/2025
- CoRL 2
…[truncated 282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7756
}
```

</details>

---

### Tool call

_source line 383 · 2026-05-28T02:02:50.250270+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form with all scoring dimensions, rating scales (1-10 or 1-5), definitions for each score level, and any specific instructions. Include soundness, novelty/excitement, clarity, significance, relevance, and any other review criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form with all scoring dimensions, rating scales (1-10 or 1-5), definitions for each score level, and any specific instructions. Include soundness, novelty/excitement, clarity, significance, relevance, and any other review criteria."
  }
}
```

</details>

---

### Tool call

_source line 384 · 2026-05-28T02:02:50.908915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool call

_source line 385 · 2026-05-28T02:02:51.366017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 386 · 2026-05-28T02:02:52.234398+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1325
}
```

</details>

---

### Tool call

_source line 387 · 2026-05-28T02:02:52.234894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 388 · 2026-05-28T02:02:52.742297+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1376
}
```

</details>

---

### Tool call

_source line 389 · 2026-05-28T02:02:52.742791+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 390 · 2026-05-28T02:02:52.998067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 763
}
```

</details>

---

### Tool call

_source line 391 · 2026-05-28T02:02:52.998528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool result

_source line 392 · 2026-05-28T02:02:53.204812+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 462
}
```

</details>

---

### Tool result

_source line 393 · 2026-05-28T02:02:53.988958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 990
}
```

</details>

---

### Tool result

_source line 394 · 2026-05-28T02:02:55.311148+00:00_

# CoRL 2023 Review Form Analysis

Based on the provided content, the document **does not include the complete review form with specific scoring scales or numerical ratings** (such as 1-10 or 1-5 scales).

## Available Review Criteria

The guidelines specify six evaluation dimensions:

1. **Originality**: "Are the problems or methods new? Is the work a novel combination of well-known techniques?"

2. **Quality**: Focuses on technical soundness and whether "claims well supported (e.g., by theoretical analysis or experimental results)"

3. **Clarity**: Assesses if the submission is "clearly written" and "well organized"

4. **Significance**: Evaluates whether "results important" and if the work "advances the state of the art in a demonstrable way"

5. **Relevance**: Determines if the paper addresses "robot learning" and whether "the CoRL audience be interested in reading this paper"

6. **Limitations**: Requires authors to include a limitations section; reviewers should "treat the honestly reported limitations kindly"

## Missing Information

The document does not specify:
- Numerical rating scales for any dimension
- Score level definitions (e.g., what constitutes 7/10 vs. 8/10)
- Overall acceptance recommendation scale
- Weighted scoring methodology

The actual review form interface appears to be on the OpenReview platform, which isn't detailed in this content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5060
}
```

</details>

---

### Tool call

_source line 395 · 2026-05-28T02:03:00.539975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 396 · 2026-05-28T02:03:00.995765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 397 · 2026-05-28T02:03:00.996620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 398 · 2026-05-28T02:03:01.502552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---

### Tool call

_source line 399 · 2026-05-28T02:03:01.503071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 400 · 2026-05-28T02:03:01.956695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 401 · 2026-05-28T02:03:02.007418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool result

_source line 402 · 2026-05-28T02:03:02.562765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---

### Tool call

_source line 403 · 2026-05-28T02:03:02.563353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---

### Tool result

_source line 404 · 2026-05-28T02:03:02.969272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---

### Tool call

_source line 405 · 2026-05-28T02:03:10.157602+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
  "project": "event-gated-adaptive-horizon",
  "pages": "21-30",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
    "project": "event-gated-adaptive-horizon",
    "pages": "21-30",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 406 · 2026-05-28T02:03:10.816207+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 2025 OpenReview review form \"overall recommendation\" \"1\" \"2\" \"3\" \"4\" \"5\" \"6\" \"7\" \"8\" \"9\" \"10\" rating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 2025 OpenReview review form \"overall recommendation\" \"1\" \"2\" \"3\" \"4\" \"5\" \"6\" \"7\" \"8\" \"9\" \"10\" rating"
  }
}
```

</details>

---

### Tool result

_source line 407 · 2026-05-28T02:03:11.674276+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p21.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 367.1}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p22.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 316.2}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p23.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 346.0}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p24.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 281.5}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p25.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 289.1}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p26.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 288.6}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p27.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 374.2}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p28.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 346.8}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review
…[truncated 566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1516
}
```

</details>

---

### Tool result

_source line 408 · 2026-05-28T02:03:32.114531+00:00_

Web search results for query: "CoRL 2024 2025 OpenReview review form "overall recommendation" "1" "2" "3" "4" "5" "6" "7" "8" "9" "10" rating"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical Scientific Paper Reviews","url":"https://arxiv.org/html/2412.11948v3"},{"title":"2024 | OpenReview","url":"https://openreview.net/group?id=corl.org%2F2024"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"Can Small and Reasoning Large Language Models Score Journal Articles for Research Quality and Do Averaging and Few-shot Help?","url":"https://arxiv.org/pdf/2510.22389"},{"title":"Best Reviewers Award for 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11955497/"}]

The search results show general OpenReview pages for CoRL 2024 and 2025, but don't contain the specific review form rating scale details. Let me try a more specific search focused on the review template.

Links: [{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Default Meta Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-form
…[truncated 6332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 21298
}
```

</details>

---

### Tool call

_source line 409 · 2026-05-28T02:03:43.119790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---

### Tool call

_source line 410 · 2026-05-28T02:03:43.421495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---

### Tool result

_source line 411 · 2026-05-28T02:03:43.876580+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---

### Tool result

_source line 412 · 2026-05-28T02:03:43.881347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---

### Tool call

_source line 413 · 2026-05-28T02:03:43.881739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---

### Tool result

_source line 414 · 2026-05-28T02:03:44.837525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 415 · 2026-05-28T02:03:44.888342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---

### Tool call

_source line 416 · 2026-05-28T02:03:45.091267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---

### Tool result

_source line 417 · 2026-05-28T02:03:45.295080+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---

### Tool result

_source line 418 · 2026-05-28T02:03:45.648034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---

### Tool call

_source line 419 · 2026-05-28T02:03:50.469095+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
  "project": "event-gated-adaptive-horizon",
  "pages": "31-40",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
    "project": "event-gated-adaptive-horizon",
    "pages": "31-40",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 420 · 2026-05-28T02:03:51.374496+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 31, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p31.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 308.7}, {\"page\": 32, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p32.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 383.6}, {\"page\": 33, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p33.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 272.8}, {\"page\": 34, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p34.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 319.6}, {\"page\": 35, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p35.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 373.8}, {\"page\": 36, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p36.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 44.0}, {\"page\": 37, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p37.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 407.5}, {\"page\": 38, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p38.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 273.0}, {\"page\": 39, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_
…[truncated 565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 905
}
```

</details>

---

### Tool call

_source line 421 · 2026-05-28T02:03:54.873617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---

### Tool call

_source line 422 · 2026-05-28T02:03:55.380953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---

### Tool result

_source line 423 · 2026-05-28T02:03:56.274758+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1401
}
```

</details>

---

### Tool result

_source line 424 · 2026-05-28T02:03:56.280621+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 899
}
```

</details>

---

### Tool call

_source line 425 · 2026-05-28T02:03:56.285344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p28.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---

### Tool call

_source line 426 · 2026-05-28T02:03:56.838742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---

### Tool result

_source line 427 · 2026-05-28T02:03:57.192935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool result

_source line 428 · 2026-05-28T02:03:57.194738+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---

### Tool call

_source line 429 · 2026-05-28T02:03:57.395775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---

### Tool result

_source line 430 · 2026-05-28T02:03:57.801089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---

### Tool call

_source line 431 · 2026-05-28T02:04:03.177393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p31.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---

### Tool call

_source line 432 · 2026-05-28T02:04:03.530190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p32.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---

### Tool result

_source line 433 · 2026-05-28T02:04:03.986996+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---

### Tool result

_source line 434 · 2026-05-28T02:04:03.990347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 460
}
```

</details>

---

### Tool call

_source line 435 · 2026-05-28T02:04:03.990783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p33.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---

### Tool result

_source line 436 · 2026-05-28T02:04:04.897889+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool call

_source line 437 · 2026-05-28T02:04:04.948607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p34.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p34.png"
  }
}
```

</details>

---

### Tool call

_source line 438 · 2026-05-28T02:04:05.151924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p35.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p35.png"
  }
}
```

</details>

---

### Tool result

_source line 439 · 2026-05-28T02:04:05.610793+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 662
}
```

</details>

---

### Tool result

_source line 440 · 2026-05-28T02:04:05.814400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 662
}
```

</details>

---

### Tool call

_source line 441 · 2026-05-28T02:04:11.094197+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
  "project": "event-gated-adaptive-horizon",
  "pages": "41-45",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
    "project": "event-gated-adaptive-horizon",
    "pages": "41-45",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 442 · 2026-05-28T02:04:11.548021+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 41, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p41.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 254.6}, {\"page\": 42, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p42.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 260.9}, {\"page\": 43, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p43.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 245.3}, {\"page\": 44, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p44.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 200.9}, {\"page\": 45, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p45.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 168.5}], \"total_pages\": 45, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 443 · 2026-05-28T02:04:11.548369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p37.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p37.png"
  }
}
```

</details>

---

### Tool result

_source line 444 · 2026-05-28T02:04:12.604237+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---

### Tool call

_source line 445 · 2026-05-28T02:04:12.755317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p38.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p38.png"
  }
}
```

</details>

---

### Tool call

_source line 446 · 2026-05-28T02:04:13.118453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p39.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p39.png"
  }
}
```

</details>

---

### Tool result

_source line 447 · 2026-05-28T02:04:13.482571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 727
}
```

</details>

---

### Tool call

_source line 448 · 2026-05-28T02:04:13.487222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p40.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p40.png"
  }
}
```

</details>

---

### Tool result

_source line 449 · 2026-05-28T02:04:14.145582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1027
}
```

</details>

---

### Tool result

_source line 450 · 2026-05-28T02:04:14.607702+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1120
}
```

</details>

---

### Tool call

_source line 451 · 2026-05-28T02:04:18.632023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p41.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p41.png"
  }
}
```

</details>

---

### Tool result

_source line 452 · 2026-05-28T02:04:19.087458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 453 · 2026-05-28T02:04:19.088002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p42.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p42.png"
  }
}
```

</details>

---

### Tool result

_source line 454 · 2026-05-28T02:04:19.994435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---

### Tool call

_source line 455 · 2026-05-28T02:04:20.044971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p43.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p43.png"
  }
}
```

</details>

---

### Tool result

_source line 456 · 2026-05-28T02:04:20.503132+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---

### Tool call

_source line 457 · 2026-05-28T02:04:20.503680+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p44.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p44.png"
  }
}
```

</details>

---

### Tool call

_source line 458 · 2026-05-28T02:04:20.959452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p45.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p45.png"
  }
}
```

</details>

---

### Tool result

_source line 459 · 2026-05-28T02:04:21.161778+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---

### Tool result

_source line 460 · 2026-05-28T02:04:21.717816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---

### Tool call

_source line 461 · 2026-05-28T02:08:25.287355+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 数据透明度\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 venue**: CoRL 2026\n\n---\n\n## 总体评分\n\n**Overall**: 6/10 — Marginally above acceptance threshold\n\n**一句话总结**: 一篇实验透明度极高的诊断分析论文，系统性地识别了变速率 DreamerV3 中的 CIVO 失败模式，但统计效力有限、因果机制声明超出了实验证据强度，且对 CoRL 的机器人学习核心议题的直接关联性不足。\n\n---\n\n## 官方维度打分（基于 CoRL review form：Originality / Quality / Clarity / Significance / Relevance / Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 7/10 | CIVO 现象和 NVE 诊断指标是新颖的；四层干预层级和 factorial design 对失败模式的系统分析在 MBRL 文献中少见 |\n| Quality (Soundness) | 5/10 | Factorial 设计合理但统计效力偏低（4-5 seeds）；n=36 上 AUROC=1.000 缺乏 bootstrap CI；部分因果声明超出观测证据 |\n| Clarity | 8/10 | 论文组织清晰，Figure 1 的 CIVO 机制图和 Figure 2 的 learning curves 信息量大，Appendix 结构系统 |\n| Significance | 5/10 | 诊断发现对 MBRL 研究者有价值，但仅验证于 DreamerV3 + 2 个 DMC 环境，泛化性未知；无 positive solution |\n| Relevance | 5/10 | 论文讨论了 temporal abstraction 在 robot control 中的重要性，但所有实验仅在 DMC 仿真中进行，无真实机器人任务或高维控制任务验证 |\n| Limitations | 8/10 | Limitations section 诚实全面（Section 6）；code correction 历史完整记录（Appendix I, Table 32）；承认了统计效力和环境多样性局限 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] AUROC = 1.000 on n=36 缺乏不确定性量化，完美分类声明过强\n\n- 具体位置：Section 4.7 (p.9), Appendix B (Table B1, p.16; Figure 5, p.16)\n- 问题：论文在 n=36 配置上报告 NVE 阈值 τ=2.0× 的分类 AUROC=1.000，但未提供 bootstrap confidence interval。在 n=36 的样本上，单个误分类即会使 AUROC 降至约 0.97。论文虽然执行了 LOEO（Table 11, p.17）和 LOCO（Appendix B.7）验证，但 LOEO 仅涵盖 3 个环境（Walker Walk, Cheetah Run, Cartpole Swingup），每个 fold 的留出集极小。\"Perfect separation\" 的声明在如此小的样本上可能是假象——CIVO 是否在更多样的环境中仍保持清晰的二模态分布尚未验证。\n- 为什么影响接收：NVE 诊断器是论文的核心 practical contribution 之一（Algorithm 1, Appendix F）。如果阈值的泛化性不确定，practitioner guidelines（Section 5, p.10, line ~40）的可靠性存疑。\n- 建议修改方向：(1) 报告 AUROC 的 bootstrap 95% CI（如 [0.94, 1.00]）；(2) 在至少 1-2 个额外 DMC 环境（如 Hopper, Quadruped）上验证阈值的外部有效性；(3) 弱化 \"perfect classification\" 的措辞为 \"perfect classification within the tested environments\"。\n\n**N2** [critical] 因果机制声明（CIVO feedback loop）超出观测证据强度\n\n- 具体位置：Figure 1 (p.2), Section D.1 (p.21), Section 5 Discussion (p.9-10)\n- 问题：论文提出了一个四步反馈环机制（trained dt-embedding → biased RSSM predictions → overestimated critic → policy exploitation → biased training data, Figure 1 Pathway A）。但实验证据是 observational ablation——证明了某些因素是 CIVO 发生的必要条件，而非直接证明了因果链中每个环节。具体地：\n  - **Step 1→2**（embedding 导致 RSSM 偏差）：gradient decomposition（Appendix D.2, p.24, Figure 11）提供了 partial evidence，但 gradient magnitude ≠ causal effect\n  - **Step 2→3**（biased prediction → value overestimation）：critic value vs. prediction analysis（Figure 10, p.23）显示相关性，但未排除其他混淆因素（如 optimizer dynamics、exploration artifacts）\n  - **Step 3→4**（value overestimation → exploitative policy）：没有直接的 policy behavior 分析或 trajectory-level evidence\n  - **Step 4→1**（biased data → further embedding bias）：完全是推断，无直接实验支持\n- 为什么影响接收：因果机制的准确性决定了干预建议（四层层级）的理论基础是否可靠。如果机制是错的（例如 CIVO 实际由 optimizer landscape 问题驱动），干预建议可能 mislead 后续研究者。\n- 建议修改方向：(1) 将 \"CIVO mechanism\" 改为 \"proposed CIVO mechanism\" 或 \"hypothesized feedback loop\"；(2) 在 Figure 1 caption 中明确标注哪些环节有直接证据、哪些是推测；(3) 在 Discussion 中添加 alternative explanations 段落（如 optimization landscape hypothesis）。\n\n**N3** [critical] 统计效力不足以支撑部分关键声明\n\n- 具体位置：Section 4 全文, Table 1 (p.5), Table 2 (p.8)\n- 问题：\n  - **4-5 seeds 的 IQM**: IQM with 4 seeds 实际上是中间 2 个值的均值，with 5 seeds 是中间 3 个值的均值。这使得每个配置的效果估计噪声极大。论文在 Section 4.1-4.6 中基于 IQM 差异做出了多处定量声明（如 \"prediction gap 0.161\", \"AUROC=1.000\"），但未报告多数声明的 effect size confidence intervals。\n  - **Seed-level claims**: 论文在多处做出 seed-level 的叙述性声明（如 \"seed 3 shows early collapse\", Figure 3, p.6; \"5 stable-onset, 1 self-correction\", p.6）。单个 seed 的行为在 RL 中高度随机，这些 seed-level observations 不构成统计证据。\n  - **n=36 分类中的 class balance**: 论文未明确报告 CIVO-positive vs non-CIVO 的类别比例。如果类别严重不平衡（如 30:6），AUROC=1.000 的意义会大幅降低。\n- 为什么影响接收：统计效力不足直接影响 claims 的可信度。在 4-5 seeds 上的 \"trend\" 可能在更多 seeds 下消失或反转。\n- 建议修改方向：(1) 报告 n=36 中 CIVO-positive 与 non-CIVO 的精确数量；(2) 对主要声明（如 Table 2 中的干预效果比较）提供 bootstrap CI；(3) 在 limitations 中更明确地讨论 4-5 seeds 的 power analysis 限制；(4) 对 seed-level claims 添加 \"anecdotal\" 限定词。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] NVE 阈值 2.0× 的选取存在潜在循环性\n\n- 具体位置：Section 3.4 (p.4), Appendix B (p.16), Figure 5 ROC curve\n- 问题：τ=2.0 的阈值是从同一数据集上通过观察 CIVO-positive 与 non-CIVO 配置的 NVE 分布选出的，然后在同一数据集上通过 LOEO/LOCO 验证。虽然 LOEO/LOCO 是 internal cross-validation 的标准做法，但 threshold selection 和 validation 共享同一组环境（3 个环境）。这不是严格意义上的 external validation——阈值在一个新颖的、从未见过的环境类别上是否仍有效完全未知。\n- 建议：(1) 在 Appendix B 中更明确地承认阈值选取的循环性风险；(2) 讨论在什么条件下阈值可能失效（如高维观测空间、稀疏奖励环境）。\n\n**W2** [warning] Factorial design 未完全隔离 embedding 架构与训练信号的效果\n\n- 具体位置：Table 14 (p.40), Table 15 (p.40), Section 4.1-4.2\n- 问题：论文的 factorial design 将 \"trained dt-embedding\" 视为单一因子，但它实际同时引入了两个变化：(1) 网络架构变化（额外的 embedding 层）和 (2) 训练信号变化（dt 值作为输入）。虽然 Table 13 (p.40) 包含了 \"frozen dt-embedding\" 条件（冻结 embedding 权重），能部分分离这两个因素，但 frozen embedding 的初始化方式可能影响结论——随机初始化的 frozen embedding 与 pretrained frozen embedding 行为可能不同。\n- 建议：明确报告 frozen embedding 的初始化策略；讨论 embedding 架构 vs. 训练信号这两个 confound 的分离程度。\n\n**W3** [warning] 环境多样性不足，robotics relevance 偏弱\n\n- 具体位置：Section 3.8 (p.4-5), Table 1 (p.5), Section 6 Limitations (p.11)\n- 问题：所有主要实验仅在 Walker Walk 和 Cheetah Run 两个 DMC 环境中进行，Cartpole Swingup 仅用于 cross-validation。对于 CoRL：\n  - 无接触丰富 (contact-rich) 的操作任务\n  - 无高维观测（如 pixel input）——虽然论文声称 DreamerV3 从 pixel 训练，但环境本身是低维 locomotion\n  - 无 sim-to-real 或真实机器人实验\n  - \"2 environments + 1 cross-validation\" 的泛化性声明在机器人学习领域偏弱\n- 建议：(1) 至少在 1-2 个操作任务（如 DMC manipulation 或 Meta-World）上验证 CIVO 是否存在；(2) 在 Discussion 中更具体地讨论 CIVO 对真实机器人部署的潜在影响。\n\n**W4** [warning] Table 1 脚注 f (\"corrected-code rerun\") 的影响范围需更清晰呈现\n\n- 具体位置：Table 1 (p.5) footnote f, Appendix I (p.35), Table 32 (p.45)\n- 问题：论文在 Appendix I 和 Table 32 中详细记录了代码修正历史——这种透明度值得赞赏，在 ML 论文中罕见。但以下问题需要更清晰的回答：\n  - (a) 代码修正影响了多少个配置的 CIVO 分类标签？Table 32 显示了个别配置的前后对比，但没有汇总统计。\n  - (b) 修正前后 NVE 阈值 2.0× 的 AUROC 是否变化？如果修正前 AUROC < 1.000 而修正后 = 1.000，这暗示阈值可能是在修正后的数据上 optimized 的。\n  - (c) 是否还有其他未发现的 bugs 可能影响结论？论文未讨论代码审查或 testing 的覆盖范围。\n- 建议：(1) 在 Appendix I 中添加一个汇总段落，明确说明修正影响了多少配置、多少个分类标签改变；(2) 报告修正前的 AUROC 以供对比。\n\n**W5** [warning] 干预实验（SGS, TCN, RAVE, dual-critic）的 \"pathway redundancy\" 声明缺乏统计检验\n\n- 具体位置：Section 4.4-4.6 (p.7-8), Table 2 (p.8), Section 5 第 6-7 段 (p.10)\n- 问题：论文核心发现之一是 \"intervention resistance reveals pathway redundancy\"（p.10, line ~30）——即 CIVO 通过多条梯度通路运作，因此单一干预无法完全消除。但这一声明基于 4 种干预各自在 4-5 seeds 上的效果比较，没有正式的统计检验（如 paired test 或 ANOVA）来验证干预间的差异是否显著。Table 2 中的 \"Prev. Rate\" 列给出了 prevention 比例，但这些比例基于极小样本（如 \"2 of 4 Walker seeds\" → 50%），置信区间极宽。\n- 建议：(1) 为 Table 2 中的关键对比提供 Fisher exact test 或 bootstrap comparison p-values；(2) 明确承认 sample size 限制下 \"redundancy\" 声明的置信程度。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 3.4 中 NVE 的数学定义公式应在正文中给出完整形式（目前定义分散在 p.4 的文字描述中），便于快速查阅。\n- **M2**: Figure 3 (p.6) 的 NVE trajectory 图中，6 条 seed 曲线的颜色区分度不足，尤其是 seed 2/4/5 在灰度打印下难以辨别。\n- **M3**: Table 1 (p.5) 信息密度极高（43 行），建议在正文中添加 summary statistics（如 CIVO-positive 比例、各环境分布）以帮助读者快速把握全局。\n- **M4**: Section 3.5 \"Selective Gradient Stopping\" 和 Section 3.6 \"Forward-Pass Interventions\" 的描述可以更紧凑——当前正文中的干预方法描述占了约 1 页，但每个干预的关键信息（what/why/how）可以用更少篇幅表达。\n- **M5**: Appendix D.2 的 gradient decomposition 分析（Figure 11, p.24）使用了 `e_obs` 的 gradient contribution percentage，但未解释为什么选择这个特定层来分解而非其他层。\n\n---\n\n## 主要优势\n\n1. **异常优秀的数据透明度**：完整的 per-seed 结果（Table 3, p.37-38）、code correction 历史（Appendix I, Table 32）、版本控制记录——这是我在 MBRL 论文中见过的最透明的实验报告之一。Appendix 长达 35 页，几乎每个声明都有 backing data。\n2. **系统性的实验设计**：Factorial design（Table 14）、四层干预层级（gradient → representation → architecture → full）、三种 cross-validation（LOEO, LOCO, standard）构成了一个连贯的证据链。\n3. **实用的诊断工具**：Algorithm 1（Online CIVO Detector, Appendix F）是一个可直接部署的在线监控工具，NVE 的计算仅需标准的 critic value 和 evaluation return，不增加额外计算开销。\n4. **Practitioner guidelines**（Section 5, p.10）提供了具体可操作的建议（如 \"Monitor NVE ≥ 2.0×\", \"Freezing dt-embedding eliminates CIVO 0/16 frozen\"）。\n5. **诚实的 negative result framing**：论文坦承四种干预均无法在所有环境中完全消除 CIVO，这种诚实比过度声称 solution 更有价值。\n\n---\n\n## 对 Review Director 的补充说明\n\n- 论文的核心 claim 结构是合理的，CIVO 作为一种 failure mode 确实存在且在 tested environments 中可复现。主要的 methodological 担忧集中在统计效力和因果声明的强度上，而非结果的真实性。\n- 对于 CoRL venue 的适配性：这是一篇高质量的 diagnostic/negative-result 论文，但 robotics relevance 是最大的弱点。所有实验在 DMC locomotion 上进行，无 manipulation、无 real-robot、无 high-dimensional tasks。如果 CoRL AC 重视 robotics grounding，这可能是一个显著减分项。\n- 如果作者能在 rebuttal 中补充 (1) AUROC 的 bootstrap CI，(2) 1-2 个额外环境的验证，(3) 弱化因果机制措辞，该论文可以达到 7/10 的水平。\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 数据透明度\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 venue**: CoRL 2026\n\n---\n\n## 总体评分\n\n**Overall**: 6/10 — Marginally above acceptance threshold\n\n**一句话总结**: 一篇实验透明度极高的诊断分析论文，系统性地识别了变速率 DreamerV3 中的 CIVO 失败模式，但统计效力有限、因果机制声明超出了实验证据强度，且对 CoRL 的机器人学习核心议题的直接关联性不足。\n\n---\n\n## 官方维度打分（基于 CoRL review form：Originality / Quality / Clarity / Significance / Relevance / Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 7/10 | CIVO 现象和 NVE 诊断指标是新颖的；四层干预层级和 factorial design 对失败模式的系统分析在 MBRL 文献中少见 |\n| Quality (Soundness) | 5/10 | Factorial 设计合理但统计效力偏低（4-5 seeds）；n=36 上 AUROC=1.000 缺乏 bootstrap CI；部分因果声明超出观测证据 |\n| Clarity | 8/10 | 论文组织清晰，Figure 1 的 CIVO 机制图和 Figure 2 的 learning curves 信息量大，Appendix 结构系统 |\n| Significance | 5/10 | 诊断发现对 MBRL 研究者有价值，但仅验证于 DreamerV3 + 2 个 DMC 环境，泛化性未知；无 positive solution |\n| Relevance | 5/10 | 论文讨论了 temporal abstraction 在 robot control 中的重要性，但所有实验仅在 DMC 仿真中进行，无真实机器人任务或高维控制任务验证 |\n| Limitations | 8/10 | Limitations section 诚实全面（Section 6）；code correction 历史完整记录（Appendix I, Table 32）；承认了统计效力和环境多样性局限 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] AUROC = 1.000 on n=36 缺乏不确定性量化，完美分类声明过强\n\n- 具体位置：Section 4.7 (p.9), Appendix B (Table B1, p.16; Figure 5, p.16)\n- 问题：论文在 n=36 配置上报告 NVE 阈值 τ=2.0× 的分类 AUROC=1.000，但未提供 bootstrap confidence interval。在 n=36 的样本上，单个误分类即会使 AUROC 降至约 0.97。论文虽然执行了 LOEO（Table 11, p.17）和 LOCO（Appendix B.7）验证，但 LOEO 仅涵盖 3 个环境（Walker Walk, Cheetah Run, Cartpole Swingup），每个 fold 的留出集极小。\"Perfect separation\" 的声明在如此小的样本上可能是假象——CIVO 是否在更多样的环境中仍保持清晰的二模态分布尚未验证。\n- 为什么影响接收：NVE 诊断器是论文的核心 practical contribution 之一（Algorithm 1, Appendix F）。如果阈值的泛化性不确定，practitioner guidelines（Section 5, p.10, line ~40）的可靠性存疑。\n- 建议修改方向：(1) 报告 AUROC 的 bootstrap 95% CI（如 [0.94, 1.00]）；(2) 在至少 1-2 个额外 DMC 环境（如 Hopper, Quadruped）上验证阈值的外部有效性；(3) 弱化 \"perfect classification\" 的措辞为 \"perfect classification within the tested environments\"。\n\n**N2** [critical] 因果机制声明（CIVO feedback loop）超出观测证据强度\n\n- 具体位置：Figure 1 (p.2), Section D.1 (p.21), Section 5 Discussion (p.9-10)\n- 问题：论文提出了一个四步反馈环机制（trained dt-embedding → biased RSSM predictions → overestimated critic → policy exploitation → biased training data, Figure 1 Pathway A）。但实验证据是 observational ablation——证明了某些因素是 CIVO 发生的必要条件，而非直接证明了因果链中每个环节。具体地：\n  - **Step 1→2**（embedding 导致 RSSM 偏差）：gradient decomposition（Appendix D.2, p.24, Figure 11）提供了 partial evidence，但 gradient magnitude ≠ causal effect\n  - **Step 2→3**（biased prediction → value overestimation）：critic value vs. prediction analysis（Figure 10, p.23）显示相关性，但未排除其他混淆因素（如 optimizer dynamics、exploration artifacts）\n  - **Step 3→4**（value overestimation → exploitative policy）：没有直接的 policy behavior 分析或 trajectory-level evidence\n  - **Step 4→1**（biased data → further embedding bias）：完全是推断，无直接实验支持\n- 为什么影响接收：因果机制的准确性决定了干预建议（四层层级）的理论基础是否可靠。如果机制是错的（例如 CIVO 实际由 optimizer landscape 问题驱动），干预建议可能 mislead 后续研究者。\n- 建议修改方向：(1) 将 \"CIVO mechanism\" 改为 \"proposed CIVO mechanism\" 或 \"hypothesized feedback loop\"；(2) 在 Figure 1 caption 中明确标注哪些环节有直接证据、哪些是推测；(3) 在 Discussion 中添加 alternative explanations 段落（如 optimization landscape hypothesis）。\n\n**N3** [critical] 统计效力不足以支撑部分关键声明\n\n- 具体位置：Section 4 全文, Table 1 (p.5), Table 2 (p.8)\n- 问题：\n  - **4-5 seeds 的 IQM**: IQM with 4 seeds 实际上是中间 2 个值的均值，with 5 seeds 是中间 3 个值的均值。这使得每个配置的效果估计噪声极大。论文在 Section 4.1-4.6 中基于 IQM 差异做出了多处定量声明（如 \"prediction gap 0.161\", \"AUROC=1.000\"），但未报告多数声明的 effect size confidence intervals。\n  - **Seed-level claims**: 论文在多处做出 seed-level 的叙述性声明（如 \"seed 3 shows early collapse\", Figure 3, p.6; \"5 stable-onset, 1 self-correction\", p.6）。单个 seed 的行为在 RL 中高度随机，这些 seed-level observations 不构成统计证据。\n  - **n=36 分类中的 class balance**: 论文未明确报告 CIVO-positive vs non-CIVO 的类别比例。如果类别严重不平衡（如 30:6），AUROC=1.000 的意义会大幅降低。\n- 为什么影响接收：统计效力不足直接影响 claims 的可信度。在 4-5 seeds 上的 \"trend\" 可能在更多 seeds 下消失或反转。\n- 建议修改方向：(1) 报告 n=36 中 CIVO-positive 与 non-CIVO 的精确数量；(2) 对主要声明（如 Table 2 中的干预效果比较）提供 bootstrap CI；(3) 在 limitations 中更明确地讨论 4-5 seeds 的 power analysis 限制；(4) 对 seed-level claims 添加 \"anecdotal\" 限定词。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] NVE 阈值 2.0× 的选取存在潜在循环性\n\n- 具体位置：Section 3.4 (p.4), Appendix B (p.16), Figure 5 ROC curve\n- 问题：τ=2.0 的阈值是从同一数据集上通过观察 CIVO-positive 与 non-CIVO 配置的 NVE 分布选出的，然后在同一数据集上通过 LOEO/LOCO 验证。虽然 LOEO/LOCO 是 internal cross-validation 的标准做法，但 threshold selection 和 validation 共享同一组环境（3 个环境）。这不是严格意义上的 external validation——阈值在一个新颖的、从未见过的环境类别上是否仍有效完全未知。\n- 建议：(1) 在 Appendix B 中更明确地承认阈值选取的循环性风险；(2) 讨论在什么条件下阈值可能失效（如高维观测空间、稀疏奖励环境）。\n\n**W2** [warning] Factorial design 未完全隔离 embedding 架构与训练信号的效果\n\n- 具体位置：Table 14 (p.40), Table 15 (p.40), Section 4.1-4.2\n- 问题：论文的 factorial design 将 \"trained dt-embedding\" 视为单一因子，但它实际同时引入了两个变化：(1) 网络架构变化（额外的 embedding 层）和 (2) 训练信号变化（dt 值作为输入）。虽然 Table 13 (p.40) 包含了 \"frozen dt-embedding\" 条件（冻结 embedding 权重），能部分分离这两个因素，但 frozen embedding 的初始化方式可能影响结论——随机初始化的 frozen embedding 与 pretrained frozen embedding 行为可能不同。\n- 建议：明确报告 frozen embedding 的初始化策略；讨论 embedding 架构 vs. 训练信号这两个 confound 的分离程度。\n\n**W3** [warning] 环境多样性不足，robotics relevance 偏弱\n\n- 具体位置：Section 3.8 (p.4-5), Table 1 (p.5), Section 6 Limitations (p.11)\n- 问题：所有主要实验仅在 Walker Walk 和 Cheetah Run 两个 DMC 环境中进行，Cartpole Swingup 仅用于 cross-validation。对于 CoRL：\n  - 无接触丰富 (contact-rich) 的操作任务\n  - 无高维观测（如 pixel input）——虽然论文声称 DreamerV3 从 pixel 训练，但环境本身是低维 locomotion\n  - 无 sim-to-real 或真实机器人实验\n  - \"2 environments + 1 cross-validation\" 的泛化性声明在机器人学习领域偏弱\n- 建议：(1) 至少在 1-2 个操作任务（如 DMC manipulation 或 Meta-World）上验证 CIVO 是否存在；(2) 在 Discussion 中更具体地讨论 CIVO 对真实机器人部署的潜在影响。\n\n**W4** [warning] Table 1 脚注 f (\"corrected-code rerun\") 的影响范围需更清晰呈现\n\n- 具体位置：Table 1 (p.5) footnote f, Appendix I (p.35), Table 32 (p.45)\n- 问题：论文在 Appendix I 和 Table 32 中详细记录了代码修正历史——这种透明度值得赞赏，在 ML 论文中罕见。但以下问题需要更清晰的回答：\n  - (a) 代码修正影响了多少个配置的 CIVO 分类标签？Table 32 显示了个别配置的前后对比，但没有汇总统计。\n  - (b) 修正前后 NVE 阈值 2.0× 的 AUROC 是否变化？如果修正前 AUROC < 1.000 而修正后 = 1.000，这暗示阈值可能是在修正后的数据上 optimized 的。\n  - (c) 是否还有其他未发现的 bugs 可能影响结论？论文未讨论代码审查或 testing 的覆盖范围。\n- 建议：(1) 在 Appendix I 中添加一个汇总段落，明确说明修正影响了多少配置、多少个分类标签改变；(2) 报告修正前的 AUROC 以供对比。\n\n**W5** [warning] 干预实验（SGS, TCN, RAVE, dual-critic）的 \"pathway redundancy\" 声明缺乏统计检验\n\n- 具体位置：Section 4.4-4.6 (p.7-8), Table 2 (p.8), Section 5 第 6-7 段 (p.10)\n- 问题：论文核心发现之一是 \"intervention resistance reveals pathway redundancy\"（p.10, line ~30）——即 CIVO 通过多条梯度通路运作，因此单一干预无法完全消除。但这一声明基于 4 种干预各自在 4-5 seeds 上的效果比较，没有正式的统计检验（如 paired test 或 ANOVA）来验证干预间的差异是否显著。Table 2 中的 \"Prev. Rate\" 列给出了 prevention 比例，但这些比例基于极小样本（如 \"2 of 4 Walker seeds\" → 50%），置信区间极宽。\n- 建议：(1) 为 Table 2 中的关键对比提供 Fisher exact test 或 bootstrap comparison p-values；(2) 明确承认 sample size 限制下 \"redundancy\" 声明的置信程度。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 3.4 中 NVE 的数学定义公式应在正文中给出完整形式（目前定义分散在 p.4 的文字描述中），便于快速查阅。\n- **M2**: Figure 3 (p.6) 的 NVE trajectory 图中，6 条 seed 曲线的颜色区分度不足，尤其是 seed 2/4/5 在灰度打印下难以辨别。\n- **M3**: Table 1 (p.5) 信息密度极高（43 行），建议在正文中添加 summary statistics（如 CIVO-positive 比例、各环境分布）以帮助读者快速把握全局。\n- **M4**: Section 3.5 \"Selective Gradient Stopping\" 和 Section 3.6 \"Forward-Pass Interventions\" 的描述可以更紧凑——当前正文中的干预方法描述占了约 1 页，但每个干预的关键信息（what/why/how）可以用更少篇幅表达。\n- **M5**: Appendix D.2 的 gradient decomposition 分析（Figure 11, p.24）使用了 `e_obs` 的 gradient contribution percentage，但未解释为什么选择这个特定层来分解而非其他层。\n\n---\n\n## 主要优势\n\n1. **异常优秀的数据透明度**：完整的 per-seed 结果（Table 3, p.37-38）、code correction 历史（Appendix I, Table 32）、版本控制记录——这是我在 MBRL 论文中见过的最透明的实验报告之一。Appendix 长达 35 页，几乎每个声明都有 backing data。\n2. **系统性的实验设计**：Factorial design（Table 14）、四层干预层级（gradient → representation → architecture → full）、三种 cross-validation（LOEO, LOCO, standard）构成了一个连贯的证据链。\n3. **实用的诊断工具**：Algorithm 1（Online CIVO Detector, Appendix F）是一个可直接部署的在线监控工具，NVE 的计算仅需标准的 critic value 和 evaluation return，不增加额外计算开销。\n4. **Practitioner guidelines**（Section 5, p.10）提供了具体可操作的建议（如 \"Monitor NVE ≥ 2.0×\", \"Freezing dt-embedding eliminates CIVO 0/16 frozen\"）。\n5. **诚实的 negative result framing**：论文坦承四种干预均无法在所有环境中完全消除 CIVO，这种诚实比过度声称 solution 更有价值。\n\n---\n\n## 对 Review Director 的补充说明\n\n- 论文的核心 claim 结构是合理的，CIVO 作为一种 failure mode 确实存在且在 tested environments 中可复现。主要的 methodological 担忧集中在统计效力和因果声明的强度上，而非结果的真实性。\n- 对于 CoRL venue 的适配性：这是一篇高质量的 diagnostic/negative-result 论文，但 robotics relevance 是最大的弱点。所有实验在 DMC locomotion 上进行，无 manipulation、无 real-robot、无 high-dimensional tasks。如果 CoRL AC 重视 robotics grounding，这可能是一个显著减分项。\n- 如果作者能在 rebuttal 中补充 (1) AUROC 的 bootstrap CI，(2) 1-2 个额外环境的验证，(3) 弱化因果机制措辞，该论文可以达到 7/10 的水平。\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 462 · 2026-05-28T02:08:29.579317+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4291
}
```

</details>

---

### Tool call

_source line 463 · 2026-05-28T02:08:35.353591+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
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

_source line 464 · 2026-05-28T02:08:35.404319+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 465 · 2026-05-28T02:08:39.881448+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 466 · 2026-05-28T02:08:39.932509+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---

### Assistant

_source line 467 · 2026-05-28T02:08:50.576111+00:00_

审稿完成。已向 Review Director 提交完整结构化意见，核心发现：

**评分 6/10**（marginally above threshold）

**三个 Must-Fix**：
1. AUROC=1.000 on n=36 缺乏 bootstrap CI，完美分类声明在小样本上过强
2. CIVO feedback loop 的因果机制声明超出观测 ablation 证据能支撑的强度
3. 4-5 seeds 的统计效力不足以支撑多处定量声明和 seed-level 叙述

**五个 Should-Fix**：NVE 阈值选取循环性、factorial 未完全分离 embedding 架构与训练信号、环境多样性不足（仅 2 DMC 环境，CoRL relevance 偏弱）、corrected-code rerun 影响范围需汇总、pathway redundancy 声明缺乏统计检验

**主要优势**：数据透明度异常出色（35 页 Appendix，per-seed 结果，code correction 历史完整记录），实验设计系统性强（factorial + 四层干预 + 三种 cross-validation），NVE 诊断工具具有实用价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

## Round 14

4 recorded events

### User

_source line 468 · 2026-05-28T02:09:36.702858+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿意见（完整原文）

**Overall**: 3/10 — Reject (存在两个独立的 desk-reject 级别问题)

## 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3/5 | CIVO 作为新命名的 failure mode 有一定新颖性，但与已知 value overestimation / compounding model error 的边界模糊 |
| Quality | 4/5 | 实验设计严谨（43 配置 ×5 seeds），四级干预层级方法论扎实 |
| Clarity | 4/5 | 写作清晰，结构合理；但正文信息密度过高导致超页 |
| Significance | 2/5 | 纯诊断论文且结论为"无已测试干预有效"——对 CoRL 社区缺乏实际指导价值 |
| Relevance | 1/5 | CIVO 是通用 MBRL 问题，非机器人特有；无真实机器人实验 |
| Limitations | 4/5 | Limitations section 存在且诚实 |

## Must-Fix 问题

**N1** [critical] 正文严重超页——约 10.5 页 vs 8 页限制
- CoRL 2026 明确规定正文（含 Limitations section）限 8 页，仅 references 和 appendix 不计入。实际正文内容横跨约 10.5 页，超限约 2.5 页。可直接触发 desk rejection。
- 建议：压缩 Discussion（~1.5 页）和 Setup（~1.5 页），将细节移至 Appendix。

**N2** [critical] Venue Fit 不足——核心贡献是通用 RL 诊断，非 robotics-specific
- CoRL 2026 CFP 明确要求 "Submissions must focus on a core robotics problem"。CIVO 是任何使用 imagination + temporal conditioning 的 MBRL 系统的通用问题，非机器人特有。
- 使用的环境（DMC Walker Walk, Cheetah Run, ManiSkill）虽是 robotics 常用 benchmark，但论文没有展示任何 robotics-specific 的 insight。
- 建议投 ICML/NeurIPS/ICLR RL track。

**N3** [critical] 纯诊断 + 负面结论缺乏 actionable contribution
- 核心结论是四级干预均无法可靠消除 CIVO。Negative result papers 在 robotics venues 的接受门槛极高。
- "冻结 dt-embedding" 等于放弃了 temporal abstraction 的全部价值——不是真正的解决方案。

## Should-Fix 问题

**W1** [warning] CIVO 与已知 value overestimation 文献的区分不够锐利
- 与 Janner et al. 讨论的 MBRL compounding model error 高度相似。Section 5 line 540 称 CIVO 是 "structural vulnerability, not regularization deficiency" 但无形式化理论分析证明。

**W2** [warning] 环境覆盖范围有限
- 主文仅 Walker Walk 和 Cheetah Run 两个 DMC 环境。缺少导航、长 horizon planning、contact-rich manipulation。

**W3** [warning] 诊断协议的通用性未经验证
- 四级层级仅在 DreamerV3 上验证，未在 TD-MPC2、Director 等其他架构上测试。

## 缺失引用
- FiGAR (Sharma et al., 2017)
- DAC (Zhang & Whiteson, 2019)
- SPiRL/SPIRAL (Pertsch et al., 2020)
- 近期 real-robot temporal abstraction 工作

---

请对以上每个 N1-N3 和 W1-W3 给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 469 · 2026-05-28T02:12:11.618799+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n## Must-Fix 问题回应\n\n### [AGREE] R2-N1: 正文严重超页——约 10.5 页 vs 8 页限制\n\n同意此问题严重且可能触发 desk rejection。\n\n我在审阅 PDF 时确认：正文内容延续至少至 page 10（含 Discussion 的编号段落 29-40，包括 \"Causal role of embedding training\"、\"Intervention resistance reveals pathway redundancy\"、\"Transferable diagnostic protocol\"、\"Practitioner guidelines\" 等实质性讨论），References 最早从 page 11 开始。即便保守估计，正文也至少 10 页，超限 2 页。\n\n补充观察：Table 1（p.5）单独占据近一整页（43 行配置表），这是超页的主要原因之一。建议将完整 Table 1 移至 Appendix，正文保留 summary statistics（如 CIVO-positive 比例、各环境配置数、class balance）和代表性子集。Discussion section（p.9-10）的 10 个编号发现也过于冗长，可压缩为 3-4 个核心发现 + Appendix 扩展。\n\n**结论**：这是一个硬性格式违规，必须在提交前修复，否则 AC 可直接 desk reject。\n\n---\n\n### [REBUT] R2-N2: Venue Fit 不足——核心贡献是通用 RL 诊断，非 robotics-specific\n\n**部分反驳，不构成 desk-reject。**\n\nR2 的论点是 CIVO 是通用 MBRL 问题而非 robotics-specific。这一判断有道理但过于绝对，理由如下：\n\n1. **Temporal abstraction 是 robot learning 的核心议题**：CoRL 历年接收了大量关于 hierarchical RL、options framework、skill discovery 的论文，这些本质上都是 \"通用 RL\" 技术在 robotics context 中的研究。CIVO 诊断的对象——variable-rate world models for temporal abstraction——直接对应真实机器人控制中的 multi-rate decision making 需求（如操作任务中 grasp planning vs. finger control 的不同时间尺度）。\n\n2. **DreamerV3 是 robotics 社区广泛采用的 MBRL baseline**：Hafner et al. (2023) 本身就在 CoRL 前身会议和 robotics benchmarks 上验证。识别其在 temporal abstraction 配置下的系统性失败模式对 robotics practitioners 有直接防护价值。\n\n3. **论文的 Practitioner Guidelines（Section 5, p.10）是 robotics-actionable 的**：如 \"Monitor NVE ≥ 2.0×\"、\"Freezing dt-embedding eliminates CIVO 0/16 frozen\" 可直接应用于机器人部署前的安全检查流程。\n\n**但 R2 指出了真实弱点**：实验仅使用 DMC locomotion 环境（Walker Walk, Cheetah Run, Cartpole Swingup），无 contact-rich manipulation、无 real-robot、无 high-dimensional observation。我在自己的审稿中也将此列为 W3（Should-Fix）。如果论文能补充 1-2 个 ManiSkill 或 Robomimic 环境的验证，venue fit 的争议可大幅缓解。\n\n**我的判断**：Relevance 偏弱（我给了 5/10），但不构成 desk-reject。CoRL CFP 的 \"focus on a core robotics problem\" 要求有解释空间——temporal abstraction failure mode diagnostics 可以合理归入 \"safe deployment of learned robot policies\" 主题。\n\n---\n\n### [REBUT] R2-N3: 纯诊断 + 负面结论缺乏 actionable contribution\n\n**不同意 \"纯负面结论\" 的定性。**\n\nR2 将论文总结为 \"四级干预均无法可靠消除 CIVO\"，但这忽略了论文中明确给出的 actionable contributions：\n\n1. **Freezing dt-embedding 完全消除 CIVO**（Table 1, p.5：0/16 frozen 配置产生 CIVO；Table 13, p.40 三路 ablation 确认）。R2 称 \"冻结等于放弃 temporal abstraction 全部价值\"——但这并非准确描述。frozen embedding 仍然 *提供* temporal abstraction（模型仍按 variable rate 运行），只是不再 *学习* dt-conditioned dynamics。论文 Section 4.2（p.7）和 Appendix C.1（p.18）的 cross-environment frozen validation 表明 frozen embedding 在 Walker Walk + Cheetah Run + Cartpole Swingup 上均维持合理性能（Table 5, p.38），并非 \"无价值\" 的退化方案。\n\n2. **NVE 在线诊断器（Algorithm 1, Appendix F, p.33）是零额外计算开销的监控工具**。对部署在真实机器人上的 MBRL 系统，能在运行时检测 value overestimation 爆发并触发安全回退，这本身就是有实际价值的 contribution。\n\n3. **四层干预层级虽未完全解决问题，但提供了 graduated mitigation 策略**。Section 4.4（SGS 在 Cheetah 上 prevent rate 4/4）、Section 4.5（TCN 在 50% 配置上有效）——这些 partial successes 对 practitioners 意味着可以根据环境特性选择合适的干预组合。\n\n4. **Table 28（p.43）的 prevention rate 数据**和 **Section 5 的 Practitioner guidelines** 提供了具体可操作的部署建议，包括 NVE 监控阈值、环境风险评估、干预选择决策树。\n\n**我的判断**：论文的 contribution 是 \"diagnostic + partial mitigation + deployment guidelines\"，而非 \"purely negative\"。Negative result papers 确实在 CoRL 接受门槛较高，但本文提供的诊断工具和实用指南超出了典型 negative result 的价值。这一点 R2 评估过于严苛。\n\n---\n\n## Should-Fix 问题回应\n\n### [AGREE] R2-W1: CIVO 与已知 value overestimation 文献的区分不够锐利\n\n同意。这与我在 N2 中提出的 \"因果机制声明超出观测证据\" 问题高度相关。\n\n论文 Section 5（p.10, line ~540）声称 CIVO 是 \"structural vulnerability, not regularization deficiency\"，但缺乏形式化理论分析。具体而言：\n\n- Janner et al. (2019) 的 compounding model error 框架已经描述了 MBRL 中 rollout horizon 增长导致 value overestimation 的一般机制\n- 论文需要更精确地阐明 CIVO 的 **独特机制**（dt-conditioning 导致的 selective bias，而非 uniform compounding error）与传统 value overestimation 的数学区别\n- Appendix D.2（p.24）的 gradient decomposition 提供了一些 evidence，但未上升为形式化 theorem 或 proposition\n\n建议：在 Section 2 或 Section 5 中添加一个明确的 \"CIVO vs. standard value overestimation\" 对比段落，从 prediction bias 的 **条件性**（conditioned on dt）vs. **均匀性**（uniform across timesteps）角度建立区分。\n\n---\n\n### [AGREE] R2-W2: 环境覆盖范围有限\n\n完全同意，与我 W3 的关切一致。仅 2 个主要 DMC 环境 + 1 个 cross-validation 环境，对于支撑 \"general diagnostic protocol\" 的声明明显不足。\n\n---\n\n### [AGREE] R2-W3: 诊断协议的通用性未经验证\n\n同意。NVE 诊断和四层干预层级仅在 DreamerV3 上验证。TD-MPC2（Hansen et al., 2024）、IRIS（Micheli et al., 2023）、Director（Hafner et al., 2022）等其他使用 temporal conditioning 的 MBRL 架构是否也会出现 CIVO 完全未知。论文 Limitations section 承认了这一点，但 generalizability 的缺失确实削弱了 \"transferable diagnostic protocol\"（Section 5, p.10）的声明强度。\n\n---\n\n### 关于缺失引用\n\n[AGREE] FiGAR（Sharma et al., 2017）和 DAC（Zhang & Whiteson, 2019）是 temporal abstraction / action repeat 的直接前驱工作，论文的 Related Work 中确实应讨论。SPiRL/SPIRAL（Pertsch et al., 2020）和近期 real-robot temporal abstraction 工作的引用也会加强 robotics relevance 的论证。\n\n---\n\n## 总结性评估\n\n| R2 问题 | 我的判断 | 理由 |\n|---------|---------|------|\n| N1 超页 | **AGREE** | PDF 确认正文至少 10 页，硬性违规 |\n| N2 Venue Fit | **REBUT** (部分) | Relevance 偏弱但不构成 desk-reject；temporal abstraction 是 robotics core topic |\n| N3 纯负面结论 | **REBUT** | 论文提供 frozen embedding solution + NVE 诊断器 + practitioner guidelines，非纯 negative |\n| W1 CIVO 区分 | **AGREE** | 需要更锐利的形式化区分 |\n| W2 环境覆盖 | **AGREE** | 与我 W3 一致 |\n| W3 通用性 | **AGREE** | 仅 DreamerV3，generalizability 未知 |\n| 缺失引用 | **AGREE** | FiGAR, DAC, SPiRL 应被讨论 |\n\n**关于 R2 的 Overall 3/10 评分**：我认为过于严苛。N1（超页）是可修复的格式问题而非实质性学术缺陷。N2 和 N3 的严重程度被高估——论文确实有 actionable contributions，venue fit 有争议但不至于 desk-reject。我维持自己的 6/10 评分（marginally above threshold），但如果超页问题不修复，实际上可能在 desk-reject 阶段被拦截而无法进入实质审稿。\n",
  "reviewer_id": "1",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n## Must-Fix 问题回应\n\n### [AGREE] R2-N1: 正文严重超页——约 10.5 页 vs 8 页限制\n\n同意此问题严重且可能触发 desk rejection。\n\n我在审阅 PDF 时确认：正文内容延续至少至 page 10（含 Discussion 的编号段落 29-40，包括 \"Causal role of embedding training\"、\"Intervention resistance reveals pathway redundancy\"、\"Transferable diagnostic protocol\"、\"Practitioner guidelines\" 等实质性讨论），References 最早从 page 11 开始。即便保守估计，正文也至少 10 页，超限 2 页。\n\n补充观察：Table 1（p.5）单独占据近一整页（43 行配置表），这是超页的主要原因之一。建议将完整 Table 1 移至 Appendix，正文保留 summary statistics（如 CIVO-positive 比例、各环境配置数、class balance）和代表性子集。Discussion section（p.9-10）的 10 个编号发现也过于冗长，可压缩为 3-4 个核心发现 + Appendix 扩展。\n\n**结论**：这是一个硬性格式违规，必须在提交前修复，否则 AC 可直接 desk reject。\n\n---\n\n### [REBUT] R2-N2: Venue Fit 不足——核心贡献是通用 RL 诊断，非 robotics-specific\n\n**部分反驳，不构成 desk-reject。**\n\nR2 的论点是 CIVO 是通用 MBRL 问题而非 robotics-specific。这一判断有道理但过于绝对，理由如下：\n\n1. **Temporal abstraction 是 robot learning 的核心议题**：CoRL 历年接收了大量关于 hierarchical RL、options framework、skill discovery 的论文，这些本质上都是 \"通用 RL\" 技术在 robotics context 中的研究。CIVO 诊断的对象——variable-rate world models for temporal abstraction——直接对应真实机器人控制中的 multi-rate decision making 需求（如操作任务中 grasp planning vs. finger control 的不同时间尺度）。\n\n2. **DreamerV3 是 robotics 社区广泛采用的 MBRL baseline**：Hafner et al. (2023) 本身就在 CoRL 前身会议和 robotics benchmarks 上验证。识别其在 temporal abstraction 配置下的系统性失败模式对 robotics practitioners 有直接防护价值。\n\n3. **论文的 Practitioner Guidelines（Section 5, p.10）是 robotics-actionable 的**：如 \"Monitor NVE ≥ 2.0×\"、\"Freezing dt-embedding eliminates CIVO 0/16 frozen\" 可直接应用于机器人部署前的安全检查流程。\n\n**但 R2 指出了真实弱点**：实验仅使用 DMC locomotion 环境（Walker Walk, Cheetah Run, Cartpole Swingup），无 contact-rich manipulation、无 real-robot、无 high-dimensional observation。我在自己的审稿中也将此列为 W3（Should-Fix）。如果论文能补充 1-2 个 ManiSkill 或 Robomimic 环境的验证，venue fit 的争议可大幅缓解。\n\n**我的判断**：Relevance 偏弱（我给了 5/10），但不构成 desk-reject。CoRL CFP 的 \"focus on a core robotics problem\" 要求有解释空间——temporal abstraction failure mode diagnostics 可以合理归入 \"safe deployment of learned robot policies\" 主题。\n\n---\n\n### [REBUT] R2-N3: 纯诊断 + 负面结论缺乏 actionable contribution\n\n**不同意 \"纯负面结论\" 的定性。**\n\nR2 将论文总结为 \"四级干预均无法可靠消除 CIVO\"，但这忽略了论文中明确给出的 actionable contributions：\n\n1. **Freezing dt-embedding 完全消除 CIVO**（Table 1, p.5：0/16 frozen 配置产生 CIVO；Table 13, p.40 三路 ablation 确认）。R2 称 \"冻结等于放弃 temporal abstraction 全部价值\"——但这并非准确描述。frozen embedding 仍然 *提供* temporal abstraction（模型仍按 variable rate 运行），只是不再 *学习* dt-conditioned dynamics。论文 Section 4.2（p.7）和 Appendix C.1（p.18）的 cross-environment frozen validation 表明 frozen embedding 在 Walker Walk + Cheetah Run + Cartpole Swingup 上均维持合理性能（Table 5, p.38），并非 \"无价值\" 的退化方案。\n\n2. **NVE 在线诊断器（Algorithm 1, Appendix F, p.33）是零额外计算开销的监控工具**。对部署在真实机器人上的 MBRL 系统，能在运行时检测 value overestimation 爆发并触发安全回退，这本身就是有实际价值的 contribution。\n\n3. **四层干预层级虽未完全解决问题，但提供了 graduated mitigation 策略**。Section 4.4（SGS 在 Cheetah 上 prevent rate 4/4）、Section 4.5（TCN 在 50% 配置上有效）——这些 partial successes 对 practitioners 意味着可以根据环境特性选择合适的干预组合。\n\n4. **Table 28（p.43）的 prevention rate 数据**和 **Section 5 的 Practitioner guidelines** 提供了具体可操作的部署建议，包括 NVE 监控阈值、环境风险评估、干预选择决策树。\n\n**我的判断**：论文的 contribution 是 \"diagnostic + partial mitigation + deployment guidelines\"，而非 \"purely negative\"。Negative result papers 确实在 CoRL 接受门槛较高，但本文提供的诊断工具和实用指南超出了典型 negative result 的价值。这一点 R2 评估过于严苛。\n\n---\n\n## Should-Fix 问题回应\n\n### [AGREE] R2-W1: CIVO 与已知 value overestimation 文献的区分不够锐利\n\n同意。这与我在 N2 中提出的 \"因果机制声明超出观测证据\" 问题高度相关。\n\n论文 Section 5（p.10, line ~540）声称 CIVO 是 \"structural vulnerability, not regularization deficiency\"，但缺乏形式化理论分析。具体而言：\n\n- Janner et al. (2019) 的 compounding model error 框架已经描述了 MBRL 中 rollout horizon 增长导致 value overestimation 的一般机制\n- 论文需要更精确地阐明 CIVO 的 **独特机制**（dt-conditioning 导致的 selective bias，而非 uniform compounding error）与传统 value overestimation 的数学区别\n- Appendix D.2（p.24）的 gradient decomposition 提供了一些 evidence，但未上升为形式化 theorem 或 proposition\n\n建议：在 Section 2 或 Section 5 中添加一个明确的 \"CIVO vs. standard value overestimation\" 对比段落，从 prediction bias 的 **条件性**（conditioned on dt）vs. **均匀性**（uniform across timesteps）角度建立区分。\n\n---\n\n### [AGREE] R2-W2: 环境覆盖范围有限\n\n完全同意，与我 W3 的关切一致。仅 2 个主要 DMC 环境 + 1 个 cross-validation 环境，对于支撑 \"general diagnostic protocol\" 的声明明显不足。\n\n---\n\n### [AGREE] R2-W3: 诊断协议的通用性未经验证\n\n同意。NVE 诊断和四层干预层级仅在 DreamerV3 上验证。TD-MPC2（Hansen et al., 2024）、IRIS（Micheli et al., 2023）、Director（Hafner et al., 2022）等其他使用 temporal conditioning 的 MBRL 架构是否也会出现 CIVO 完全未知。论文 Limitations section 承认了这一点，但 generalizability 的缺失确实削弱了 \"transferable diagnostic protocol\"（Section 5, p.10）的声明强度。\n\n---\n\n### 关于缺失引用\n\n[AGREE] FiGAR（Sharma et al., 2017）和 DAC（Zhang & Whiteson, 2019）是 temporal abstraction / action repeat 的直接前驱工作，论文的 Related Work 中确实应讨论。SPiRL/SPIRAL（Pertsch et al., 2020）和近期 real-robot temporal abstraction 工作的引用也会加强 robotics relevance 的论证。\n\n---\n\n## 总结性评估\n\n| R2 问题 | 我的判断 | 理由 |\n|---------|---------|------|\n| N1 超页 | **AGREE** | PDF 确认正文至少 10 页，硬性违规 |\n| N2 Venue Fit | **REBUT** (部分) | Relevance 偏弱但不构成 desk-reject；temporal abstraction 是 robotics core topic |\n| N3 纯负面结论 | **REBUT** | 论文提供 frozen embedding solution + NVE 诊断器 + practitioner guidelines，非纯 negative |\n| W1 CIVO 区分 | **AGREE** | 需要更锐利的形式化区分 |\n| W2 环境覆盖 | **AGREE** | 与我 W3 一致 |\n| W3 通用性 | **AGREE** | 仅 DreamerV3，generalizability 未知 |\n| 缺失引用 | **AGREE** | FiGAR, DAC, SPiRL 应被讨论 |\n\n**关于 R2 的 Overall 3/10 评分**：我认为过于严苛。N1（超页）是可修复的格式问题而非实质性学术缺陷。N2 和 N3 的严重程度被高估——论文确实有 actionable contributions，venue fit 有争议但不至于 desk-reject。我维持自己的 6/10 评分（marginally above threshold），但如果超页问题不修复，实际上可能在 desk-reject 阶段被拦截而无法进入实质审稿。\n",
    "reviewer_id": "1",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 470 · 2026-05-28T02:12:15.935669+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4316
}
```

</details>

---

### Assistant

_source line 471 · 2026-05-28T02:12:21.644599+00:00_

交叉回应已提交。总结：

- **AGREE**：R2-N1（超页，硬性违规）、R2-W1（CIVO 区分不锐利）、R2-W2（环境覆盖不足）、R2-W3（通用性未验证）、缺失引用
- **REBUT**：R2-N2（venue fit 偏弱但不构成 desk-reject，temporal abstraction 是 robotics core topic）、R2-N3（论文非纯负面——提供 frozen embedding 方案 + NVE 诊断器 + practitioner guidelines）
- **关于 R2 的 3/10 评分**：认为过于严苛。超页是可修复的格式问题；venue fit 和 negative result 的严重程度被高估。维持我的 6/10 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_1"
}
```

</details>

---

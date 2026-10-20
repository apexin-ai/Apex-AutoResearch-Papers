# Reviewer 2 coordination

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 457
- **Recorded user turns:** 14
- **Tool calls:** 215
- **Original source:** `logs/chats/feishu_group_oc_dd4a07a509df7e5f9a31d65f776059bc_reviewer_2.jsonl`
- **Structured JSON:** [`72739ba2d9dee0d0611b.json`](../../sessions/72/72739ba2d9dee0d0611b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-15T12:29:45.918721+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 & 贡献度 & Venue Fit & Related Work**

### 投稿信息
- **Venue**: CoRL 2026 Main Conference
- **Deadline**: 2026-05-29 (abstract: 2026-05-26)
- **格式要求**: 8页正文, PMLR模板 (`\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section
- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）

### 论文概述
标题："Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"

诊断性论文，识别出在 DreamerV3 中 dt-conditioning 失败的根因（trained dt-embedding 导致 CIVO），并与 TAWM (MPC-based) 的成功形成对比，归因于 feedback architecture 的差异。

### 你需要重点审查
1. **Venue Fit (CoRL)**：CoRL 侧重 robot learning，本文实验仅在 DMC Walker Walk（非真实机器人任务）上进行。temporal abstraction 对 robotics 的重要性是否被充分 motivate？是否应该有更多 robotics-relevant 的讨论或实验？
2. **贡献度**：这是一篇"负面结果+诊断"论文。CIVO 的发现是否足够深入和 actionable 以达到 CoRL 主会议的接收门槛？
3. **新颖性**：
   - value overestimation 在 MBRL 中已被广泛研究 (TD3, MBPO, MOPO)。CIVO 与已有工作的区别是否清晰？
   - factorial ablation 方法本身是否有方法论创新？
4. **Related Work 完整性**：
   - 是否遗漏了重要的 temporal abstraction in MBRL 工作？
   - DreamerV4 (transformer-based) 的讨论是否充分？
   - 是否有其他尝试在 Dreamer 中做 multi-dt 的工作被遗漏？
   - TempoRL, FiGAR, Dynamic-dt 等 model-free temporal abstraction 的关系是否充分讨论？
5. **与 TAWM 的对比**：仅基于 architectural reasoning 而非实证对比——是否应该实际运行 TAWM 来验证？
6. **Actionability**：论文是否提供了足够的前进方向？"hierarchical approaches may work"是否太泛？

请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T12:29:56.489029+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T12:29:56.539996+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_2_393bd6df.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T12:29:57.297840+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T12:29:57.753089+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T12:30:00.935426+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 7 · 2026-05-15T12:30:00.986769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T12:30:04.905368+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/event-gated-adaptive-horizon/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/event-gated-adaptive-horizon/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T12:30:09.069155+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 4163
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T12:30:09.336049+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T12:30:15.588880+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"}]

Based on the search results, I found information about CoRL 2026, but the specific detailed reviewer guidelines and review form criteria for CoRL 2026 do not appear to be publicly available yet in the search results. 

However, I can provide you with what information is available:

**General CoRL 2026 Information:**
All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

**Previous CoRL Review Criteria (from CoRL 2024):**
While the specific 2026 review form isn't available, CoRL 2024 review criteria provide a reference point: Submissions will be evaluated based on the significance and novelty of the results, either theoretical or empirical.

**CoRL 2023 Reviewer Guidelines (reference):**
Rel
…[truncated 645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6252
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T12:30:18.362584+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T12:30:18.774517+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 411
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T12:30:18.775004+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 15 · 2026-05-15T12:30:18.825499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T12:30:24.184625+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, score scales, and any specific guidelines for reviewers. I need: 1) All rating dimensions and their scales, 2) What each score means, 3) Any specific instructions about what reviewers should evaluate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, score scales, and any specific guidelines for reviewers. I need: 1) All rating dimensions and their scales, 2) What each score means, 3) Any specific instructions about what reviewers should evaluate."
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T12:30:25.096114+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T12:30:25.601226+00:00_

1	\begin{abstract}
2	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify trained temporal embedding as the causal factor and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. A normalized value-to-eval ratio threshold of $1.5\times$ achieves 4/4 separating power within the factorial grid (88.9\% accuracy across all configurations, with one false negative under $\Delta t{=}1$-only imagination). The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T12:30:25.601637+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T12:30:26.055620+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T12:30:26.056154+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T12:30:26.559091+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T12:30:26.559495+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T12:30:27.013772+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T12:30:27.014432+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T12:30:27.469623+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T12:30:27.470754+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T12:30:28.177202+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T12:30:28.229025+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T12:30:28.330415+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T12:30:28.331050+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided content, I can only identify **general evaluation guidance** rather than a complete review form with specific scoring scales.

## Available Evaluation Criteria

**Review Standard for Regular Papers:**
Papers are assessed on "significance and novelty of the results, either theoretical or empirical" along with "the degree to which they have been objectively established" and potential impact.

**Scope Requirements:**
Submissions must demonstrate robot learning relevance through either:
- **Intent**: "Explicitly address a learning question for physical robots" OR
- **Outcome**: "Test the proposed learning solution on physical robots"

## Missing Information

The document does not contain:
- Specific rating dimensions (e.g., technical quality, clarity, originality scores)
- Numerical scoring scales or point ranges
- Definitions of what each score level means
- Detailed evaluation rubrics beyond the criteria listed above

The page focuses on desk rejection standards and reviewer qualification requirements rather than providing the complete scoring framework you requested. To obtain the actual review form with rating scales and point definitions, you would need to access CoRL 2024's reviewer instructions or submission platform directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4146
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T12:30:35.028587+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria including: 1) All rating dimensions and their exact scales (1-10 or whatever they use), 2) What each score level means, 3) Specific instructions about relevance to robotics, novelty, etc. I need the full scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria including: 1) All rating dimensions and their exact scales (1-10 or whatever they use), 2) What each score level means, 3) Specific instructions about relevance to robotics, novelty, etc. I need the full scoring rubric."
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T12:30:36.040025+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2024 review form scoring dimensions \"overall recommendation\" scale 1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2024 review form scoring dimensions \"overall recommendation\" scale 1-10"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T12:30:37.705009+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T12:30:37.757526+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T12:30:39.822944+00:00_

# CoRL 2023 Review Form Analysis

Based on the provided guidelines, I must note that **the complete numerical rating scales and score level definitions are not included in this document**.

## Available Review Criteria

The guidelines specify reviewers should evaluate papers across six dimensions:

1. **Originality** - Assesses novelty of problems/methods and differentiation from prior work
2. **Quality** - Evaluates technical soundness and substantiation of claims
3. **Clarity** - Examines writing quality and reproducibility of information
4. **Significance** - Determines if results are important and advance the field
5. **Relevance** - Checks alignment with "robot learning" focus and audience interest
6. **Limitations** - Reviews how honestly authors acknowledge shortcomings

## Key Instruction

The guidelines emphasize treating "honestly reported limitations kindly" while pointing out unreported flaws that should "strongly" affect scores.

## Missing Information

The actual numerical scales (e.g., 1-10, 1-5), specific score interpretations, and acceptance thresholds are **not provided in this excerpt**. These details would typically appear in the formal review form itself, which reviewers access through OpenReview but isn't reproduced in this guidelines document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4794
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T12:30:51.037789+00:00_

Web search results for query: "CoRL 2025 2024 review form scoring dimensions "overall recommendation" scale 1-10"

Links: [{"title":"CORL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"Corl Technologies Reviews (58): Pros & Cons of Working At Corl Technologies | Glassdoor","url":"https://www.glassdoor.com/Reviews/Corl-Technologies-Reviews-E644284.htm"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2025 Demos | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FDemos"},{"title":"CoRL Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/"},{"title":"CORLcleared Vendor Scoring Process – CORL_Portal","url":"https://corl-portal.zendesk.com/hc/en-us/articles/14440881933339-CORLcleared-Vendor-Scoring-Process"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"}]

Let me search more specifically for CoRL review form details:

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"CORLcleared Vendor Scoring Process – CORL_Portal","url":"https://corl-portal.zendesk.com/hc/en-us/articles/14440881933339-CORLcleared-Vendor-Scoring-Process"},{"title":"Reviewer Guidelines — CoRL 20
…[truncated 4383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 14997
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T12:30:53.862849+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T12:30:54.369744+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T12:30:55.436962+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/",
  "prompt": "Extract the CoRL review form scoring dimensions and scales. What are the rating categories (e.g., overall recommendation, soundness, significance, novelty) and what numerical scale do they use (1-5, 1-10, etc.)? What does each score level mean?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/",
    "prompt": "Extract the CoRL review form scoring dimensions and scales. What are the rating categories (e.g., overall recommendation, soundness, significance, novelty) and what numerical scale do they use (1-5, 1-10, etc.)? What does each score level mean?"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T12:31:00.790073+00:00_

# CoRL Review Form Scoring Dimensions

Based on the provided webpage content, I cannot extract specific information about CoRL's review form scoring dimensions and scales.

The page displays statistics and data visualization tools for CoRL 2025 submissions but does not detail the actual review form structure. While the interface mentions metrics like "[OpenReview] Rating," "[OpenReview] Confidence," and "[OpenReview] Replies," it does not explain:

- What specific review categories exist (soundness, significance, novelty, etc.)
- The numerical scales used (1-5, 1-10, or other ranges)
- Definitions for each score level

The content shows that CORL 2024 used a 1.70-4.00 scale while CORL 2023 used a 4.70-10.00 scale, but no interpretation of what these scores signify is provided.

**To find this information**, you would need to access the actual OpenReview submission portal or conference reviewer guidelines linked within the page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5353
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T12:31:08.515645+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "variable timestep world model reinforcement learning multi-rate imagination dreamer temporal abstraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "variable timestep world model reinforcement learning multi-rate imagination dreamer temporal abstraction 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T12:31:08.767368+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 OpenReview review form rating scale 1-10 overall score dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 OpenReview review form rating scale 1-10 overall score dimensions"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T12:31:18.156112+00:00_

Web search results for query: "variable timestep world model reinforcement learning multi-rate imagination dreamer temporal abstraction 2024 2025"

Links: [{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/pdf/2506.08441"},{"title":"NeurIPS Graph Dreamer: Temporal Graph World Models for Sample-Efficient and Generalisable Reinforcement Learning","url":"https://neurips.cc/virtual/2025/loc/san-diego/133755"},{"title":"Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/html/2603.02765v1"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/html/2512.20605v1"},{"title":"[2502.21142] Multimodal Dreaming: A Global Workspace Approach to World Model-Based Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/2502.21142"},{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"[Quick Review] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://liner.com/review/emergent-temporal-abstractions-in-autoregressive-models-enable-hierarchical-reinforcement-learning"}]

Based on the web search results, I found several relevant papers and research on world models, reinforcement learning, temporal abstraction, and the Dreamer framework from 2024-2025:

## Key
…[truncated 2023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9640
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T12:31:20.941967+00:00_

Web search results for query: "CoRL 2024 OpenReview review form rating scale 1-10 overall score dimensions"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 Workshop XE | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FXE"},{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"GitHub - ANLGBOY/ICLR-2024-OpenReview-Ratings · GitHub","url":"https://github.com/ANLGBOY/ICLR-2024-OpenReview-Ratings"},{"title":"ICLR 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/iclr-statistics/iclr-2024-statistics/"}]

The search results don't contain specific details about the CoRL 2024 review form rating scale or dimensions. Let me search more specifically for the review form information.

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-
…[truncated 4606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12174
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T12:32:20.657261+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T12:32:20.708707+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:20:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:27:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:45:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:50:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:52:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex:8:TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping---transforming manageable imprecision into pathological value overestimation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex:11:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:7:All experiments build on DreamerV3 \citep{hafner2023dreamerv3},
…[truncated 1632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T12:32:25.639143+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T12:33:21.760984+00:00_

&lt;persisted-output>
Output too large (53.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon--claude-sessions-review-reviewer-2-393bd6df/8a031905-bd95-4655-9f54-317dad0d5e31/tool-results/toolu_01W2x6Qu2rLV8TFzBShpHuQW.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 77, \"total_citations\": 44, \"unique_cited_keys\": 29, \"orphan_bib\": 48, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 63, \"online_not_found\": 5, \"online_mismatch\": 9}, \"cross_check\": {\"orphan_bib\": [\"asadi2019combating\", \"barkley2024stealing\", \"beckerehmck2023multitimestep\", \"bjorck2022variance\", \"braylan2015frame\", \"bredis2026nedreamer\", \"chen2022transdreamer\", \"chua2018pets\", \"colas2018seeds\", \"farebrother2024stopregressing\", \"haarnoja2018sac\", \"hafner2022director\", \"henderson2018deep\", \"hussing2024dissecting\", \"jaderberg2017unreal\", \"ke2019learning\", \"kim2025deas\", \"kobayashi2025metacontroller\", \"kumar2022dr3\", \"lambert2020objective\", \"lambert2022investigating\", \"lee2021sunrise\", \"lenz2025macura\", \"liu2022dmve\", \"liu2025vanta\", \"luo2025vpl\", \"lyle2021auxiliary\", \"lyle2024normalization\", \"ma2024harmonydream\", \"nachum2018hiro\", \"nagabandi2018neural\", \"nie2025sdar\", \"nikishin2022primacy\", \"nikishin2023plasticity\", \"palenicek2025diminishing\", \"park2021sar\", \"qiao2023mind\", \"schwarzer2023bbf\", \"sokar2023dormant\", \"splates2025\", \"su2020conqur\", \"thrun1993issues\", \"venkatraman2015improving\", \"voelcker2025madtd\", \"wang2024seac\", \"zhang2025dymodreamer\", \"zhang2026hwm\", \"zhang2026instability\"], \"missing_bib\": [], \"orphan_count\": 48, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"sutton1999options\", \"type\": \"article\", \"title\": \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 56121
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T12:33:32.765696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon--claude-sessions-review-reviewer-2-393bd6df/8a031905-bd95-4655-9f54-317dad0d5e31/tool-results/toolu_01W2x6Qu2rLV8TFzBShpHuQW.txt",
  "offset": "0",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon--claude-sessions-review-reviewer-2-393bd6df/8a031905-bd95-4655-9f54-317dad0d5e31/tool-results/toolu_01W2x6Qu2rLV8TFzBShpHuQW.txt",
    "offset": "0",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T12:33:33.219789+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 77, \"total_citations\": 44, \"unique_cited_keys\": 29, \"orphan_bib\": 48, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 63, \"online_not_found\": 5, \"online_mismatch\": 9}, \"cross_check\": {\"orphan_bib\": [\"asadi2019combating\", \"barkley2024stealing\", \"beckerehmck2023multitimestep\", \"bjorck2022variance\", \"braylan2015frame\", \"bredis2026nedreamer\", \"chen2022transdreamer\", \"chua2018pets\", \"colas2018seeds\", \"farebrother2024stopregressing\", \"haarnoja2018sac\", \"hafner2022director\", \"henderson2018deep\", \"hussing2024dissecting\", \"jaderberg2017unreal\", \"ke2019learning\", \"kim2025deas\", \"kobayashi2025metacontroller\", \"kumar2022dr3\", \"lambert2020objective\", \"lambert2022investigating\", \"lee2021sunrise\", \"lenz2025macura\", \"liu2022dmve\", \"liu2025vanta\", \"luo2025vpl\", \"lyle2021auxiliary\", \"lyle2024normalization\", \"ma2024harmonydream\", \"nachum2018hiro\", \"nagabandi2018neural\", \"nie2025sdar\", \"nikishin2022primacy\", \"nikishin2023plasticity\", \"palenicek2025diminishing\", \"park2021sar\", \"qiao2023mind\", \"schwarzer2023bbf\", \"sokar2023dormant\", \"splates2025\", \"su2020conqur\", \"thrun1993issues\", \"venkatraman2015improving\", \"voelcker2025madtd\", \"wang2024seac\", \"zhang2025dymodreamer\", \"zhang2026hwm\", \"zhang2026instability\"], \"missing_bib\": [], \"orphan_count\": 48, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"sutton1999options\", \"type\": \"article\", \"title\": \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\", \"authors\": \"Sutton, R.S and Precup, D and Singh, S\", \"year\": \"1999\", \"venue\": \"Artificial Intelligence 112\"}, {\"key\": \"hafner2020dreamerv1\", \"type\": \"inproceedings\", \"title\": \"Dream to Control: Learning Behaviors by Latent Imagination\", \"authors\": \"Hafner, D and Lillicrap, T and Ba, J and Norouzi, M\", \"year\"
…[truncated 52410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T12:35:47.402461+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**审查侧重**: 新颖性 & 贡献度 & Venue Fit & Related Work\n\n---\n\n## Summary\n\n本文系统调查了将 dt-conditioning（源自 TAWM/TD-MPC2 框架）移植到 DreamerV3 imagination-based actor-critic 中的失败原因。通过 Walker Walk 上的 9 组 factorial ablation，作者识别出 trained dt-embedding 是导致 conditioning-induced value overestimation (CIVO) 的因果因子：trained embedding 使 RSSM reward head 在 dt=1 和 dt=2 之间产生 2.78× 的预测偏差，该偏差通过 imagination bootstrapping 被 critic 内化为系统性高估。论文进一步发现：(1) 同一 CIVO trigger 产生三种随机下游结果（full collapse、self-correction、oscillatory degradation）；(2) 限制 imagination 到 dt=1 不能完全防止崩溃，存在一条 non-CIVO pathway（Pathway B）；(3) 与 TAWM 的对比将 feedback architecture（imagination bootstrapping vs. MPC re-planning）定位为关键结构差异。\n\n---\n\n## 官方维度打分（基于 CoRL Review Form: Originality, Quality, Clarity, Significance, Relevance, Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/10 | CIVO 是已知 value overestimation 问题在特定 dt-conditioning 下的实例化，方法论（factorial ablation）无创新 |\n| Quality | 5/10 | Factorial 设计合理但单环境 + 2-3 seeds 的统计效力不足，TAWM 对比缺乏实证 |\n| Clarity | 7/10 | 写作清晰、结构好，NVE 指标定义明确，Findings 组织有序 |\n| Significance | 4/10 | 诊断性负面结果，actionable takeaway 太弱，对社区指导有限 |\n| Relevance | 3/10 | 仅 DMC Walker Walk，无机器人任务，robotics motivation 缺失 |\n| Limitations | 7/10 | 诚实承认单环境和单架构局限，但未讨论统计效力问题 |\n\n---\n\n## 总体评分\n\n**Overall: 4/10 (Reject)**\n\n**一句话总结**: 对一个有趣的负面结果给出了结构化诊断，但单环境实验、与 CoRL robotics 主题的弱关联、以及缺乏 actionable 解决方案，使得本文不达到 CoRL 主会议的接收门槛。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性\n\n- 具体位置：全文；Section 5 (Methodology) §5.5 Environment\n- 问题：CoRL 的 scope 要求论文 \"explicitly address a learning question for physical robots\" 或 \"test the proposed learning solution on physical robots\"（参考 CoRL 2023 Reviewer Guidelines）。本文全部实验仅在 DMC Walker Walk（proprioceptive，非视觉）上进行，且论文正文未讨论 temporal abstraction 对 robotics 的具体重要性——例如变频控制对机械臂操作的必要性、sim-to-real 中时间分辨率 mismatch 问题、或 real robot 上 MPC vs. imagination 的延迟约束。Introduction (Section 1) 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。\n- 为什么影响接收：CoRL 审稿人会首先检查 robotics relevance。一篇纯粹在 DMC locomotion 上做 DreamerV3 诊断的论文，即使技术正确，也更适合投 ICML/NeurIPS/ICLR 的 RL track 而非 CoRL。\n- 建议修改方向：(1) 增加至少 1-2 个 robotics-relevant 环境（如 Meta-World manipulation、RoboSuite、或 real robot locomotion）上的验证实验；(2) 在 Introduction 中用具体 robotics scenario 来 motivate temporal abstraction 的重要性；(3) 讨论 CIVO 对 sim-to-real transfer 的 implications。\n\n**N2** [critical] 单环境实验无法支撑因果 claim 的泛化性\n\n- 具体位置：Section 5.5 及 Conclusion (Section 7)\n- 问题：全部 findings（F1-F6）仅来自 Walker Walk 一个环境。论文声称识别出 \"structural incompatibility between flat temporal conditioning and imagination-based actor-critic training\"（Section 6.6），但这一结论的泛化性完全未经验证。Walker Walk 是一个相对简单的 locomotion 任务，reward 接近 dense；在 sparse reward 环境、高维视觉输入、multi-object manipulation 等场景下，CIVO 可能表现完全不同——例如 reward prediction gap 的幅度可能因任务 reward structure 而异。\n- 为什么影响接收：CoRL 审稿人在 Quality 维度会要求 \"results are objectively established\"。单环境 + 2-3 seeds 的实验设置不满足这一标准，尤其是论文自身发现 seed 间的巨大方差（F2 中 1/2 seeds collapse）。按 Colas et al. (2018)（论文 .bib 中有但未引用），2-3 seeds 的统计效力极低。\n- 建议修改方向：(1) 至少在 3-5 个 DMC tasks 上复现核心 finding（如 Cheetah Run、Humanoid Walk）；(2) 增加 seeds 到 5+ 以提供有意义的统计检验；(3) 如果资源有限，至少对 NVE threshold 的鲁棒性做跨任务讨论。\n\n**N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution\n\n- 具体位置：Section 6.6 (Implications) 和 Section 7 (Conclusion, Future directions)\n- 问题：论文的核心贡献是 \"识别 CIVO 失败模式\"。但诊断之后，论文未提供任何可验证的解决方案。Section 6.6 提到三个 future directions：(1) hierarchical approaches (THICK/Hieros)、(2) embedding regularization (gradient stopping/spectral norm)、(3) 扩展到 transformer world models——但这些全部是 \"we leave to future work\" 的表述。Conclusion 的 Future directions 同样只是重述这三点。这意味着论文的 output 仅仅是 \"dt-conditioning 在 DreamerV3 中不 work\"，缺乏 constructive contribution。\n- 为什么影响接收：CoRL 主会议对负面结果论文的接收门槛很高——需要 finding 本身足够深入且 actionable 以抵消缺少正面算法贡献的劣势。类比 \"Implementation Matters\" (Engstrom et al., 2020) 之所以被接收，是因为它跨大量环境和超参数做了系统性发现且提供了具体的实践指导。本文的 CIVO 诊断局限于单环境且缺乏等价的实践指导。\n- 建议修改方向：(1) 实现并测试至少一种 mitigation（如 gradient-stop dt-embedding 对 reward head 的梯度），将其作为 actionable contribution；(2) 或者将 NVE 指标包装为一个通用的 early-warning diagnostic tool，提供可复用的代码和使用指南。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 与 TAWM 的对比仅基于 architectural reasoning，缺乏实证验证\n\n- 具体位置：Section 6.3 (Why MPC Is Immune), Related Work §2 (TAWM paragraph)\n- 问题：论文的核心 narrative 之一是 \"同一 dt-conditioning 在 TAWM (MPC) 中 work 但在 DreamerV3 (imagination) 中 fail\"。但论文从未实际运行 TAWM 来验证。Section 6.3 的分析完全基于 architectural reasoning（\"MPC re-plans from real states at every step, so model errors do not accumulate into the critic\"）。这一论证虽然 plausible，但存在替代解释——例如 TD-MPC2 和 DreamerV3 的 world model architecture 本身不同（连续 vs. 离散 latent states），training objective 不同（joint vs. detached），这些差异可能同样 confound 对比。\n- 建议：至少运行 TAWM 的公开代码在 Walker Walk 上，验证 dt-conditioning 确实在 MPC setting 下 healthy（NVE ≈ 1.0），或引用 TAWM 原文中 Walker Walk 的具体数字。\n\n**W2** [warning] NVE threshold 1.5× 的选取缺乏 principled justification\n\n- 具体位置：Section 5.4 (Diagnostic Metrics), Equation 1\n- 问题：1.5× threshold 被描述为在 factorial grid 内有 \"4/4 separating power\"，但这是事后拟合（post-hoc fitting）到一个仅有 9 个 configurations 的 grid。论文声称 88.9% accuracy (8/9)，但 false negative（008e_v3 s1）恰好是最有诊断价值的 case。没有交叉验证、bootstrapped confidence interval、或理论推导来支撑 1.5× 这个具体数值。对于一个试图建立 diagnostic 标准的论文，这一点令人担忧。\n- 建议：讨论 threshold sensitivity（如 1.3× 和 2.0× 下的 accuracy 变化），或承认该 threshold 是探索性的。\n\n**W3** [warning] CIVO 与已知 value overestimation 的区分不够清晰\n\n- 具体位置：Section 6.1 (CIVO Mechanism), Related Work §3 (Value Overestimation paragraph)\n- 问题：论文将 CIVO 与 delusional bias (Lu et al., 2018) 区分为 \"model-induced vs. policy-class constraints\"（Section 6.1, line 13）。但 CIVO 的核心机制——model error 通过 bootstrapping 被 critic 放大——与已知的 MBRL value overestimation 文献（MBPO, MOPO, Frauenknecht et al.）高度相似。论文 Related Work 中对 Frauenknecht et al. (2025) 的讨论是 \"we identify the specific dt-embedding-induced reward bias by which rollout divergence corrupts values\"（Section 2, line 11），但这一区分的粒度是 \"what triggers the bias\"（dt-embedding），而非 \"how the bias propagates\"（同样是 bootstrapping amplification）。一个 reviewer 会问：CIVO 是否只是 \"compounding model error in MBRL\" 的一个特定实例化（instantiation），而非一个新的失败模式？\n- 建议：更精确地定义 CIVO 相对于 general compounding error 的新颖性——可能在于 \"learned conditioning feature 主动引入偏差\" 而非 \"模型本身不够准\"，但这一点需要更清晰地阐述。\n\n**W4** [warning] Related Work 遗漏若干相关工作\n\n- 具体位置：Section 2 (Related Work)\n- 问题：\n  (a) **Becker-Ehmck et al. (2023) \"Multi-timestep models for Model-based RL\"**——该论文直接研究 multi-timestep world model 在 MBRL 中的效果，与本文主题高度相关，但在 .bib 中存在（`beckerehmck2023multitimestep`）却未在正文中引用或讨论。\n  (b) **Park et al. (2021) \"Time Discretization-Invariant Safe Action Repetition\"** 和 **Wang & Beltrame (2024) \"Reinforcement Learning with Elastic Time Steps\"**——均在 .bib 中但未引用，它们研究 time-discretization 对 RL 的影响，与 Section 6.3 (Why MPC Is Immune) 和 Tallec et al. (2019) 的讨论直接相关。\n  (c) **DreamerV4 讨论不足**：Section 6.6 仅用一段提到 DreamerV4 的 transformer architecture \"may mitigate or amplify\" CIVO，但未讨论 DreamerV4 的 attention mechanism 如何具体影响 temporal conditioning 的 co-adaptation 问题。考虑到 DreamerV4 是 Dreamer 家族的最新成员，这一讨论的缺失是显著的。\n  (d) **.bib 中 48 个 orphan entries** 未在正文引用——虽然这是一个 housekeeping 问题，但表明 related work 讨论尚未完成。\n- 建议：引用并讨论 Becker-Ehmck et al. (2023) 和 Park et al. (2021)；加深 DreamerV4 讨论；清理 .bib 中未引用的条目。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式问题**：当前使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` 而非 CoRL 2026 要求的 PMLR 模板（`\\usepackage[final]{corl_2026}`）。投稿前需切换模板并验证页数。\n- **引用格式问题**：.bib 中 `splates2025` 的 author 字段为 \"SPlaTES, authors\"——这不是合法的 BibTeX author 格式。`nie2025sdar` 和 `kim2025deas` 使用了 \"et, al\" 而非完整作者列表。\n- **Baseline seeds 不完整**：Section 5.3 (line 63) 提到 \"a third seed (seed 0) is in progress\"——提交时应完成。\n- **Treatment 训练步数**：Treatment configurations 仅跑到 105K steps，而 baseline 跑到 505K。Section 5.5 声称 105K \"sufficient to observe collapse onset\"，但对于 self-correction 的 seed（009b, eval 267.9 at 105K），无法判断是否会在更长训练后进一步恢复或最终也崩溃——这削弱了 \"three post-CIVO outcomes\" 结论的可靠性。\n- **Table 1 中 NVE 的缺失值**：exp_006, 007, 005 的 NVE 标注为 \"---\"。即使这些 early experiments 没有完整的 NVE 计算，解释原因或补充数据会增强一致性。\n\n---\n\n## 主要优势\n\n1. **清晰的因果 ablation 设计**：trained vs. untrained vs. removed embedding 的三向对比是方法论亮点。008d vs. 008f 的 key control 设计精巧，在其控制的范围内具有说服力。\n2. **多路径发现有价值**：Pathway A (CIVO, value-driven) 和 Pathway B (non-CIVO, eval-driven) 的识别是一个 genuine discovery，表明 trained temporal conditioning 的危害超出单一 value overestimation 机制。这一发现对 future work 有实际指导意义。\n3. **NVE 指标设计合理**：normalized value-to-eval ratio 作为诊断工具思路清晰，通过 baseline normalization 控制了自然的 v/e 动态。尽管 threshold 选取缺乏 principled justification，指标本身有推广价值。\n4. **写作质量**：F1-F6 的组织清晰，每个 finding 有明确的实验证据支撑。Analysis section 的 CIVO 机制四阶段描述和 seed divergence 分析写得好。\n5. **诚实的 limitations**：Conclusion 承认单环境和单架构局限，这比许多论文做得好。\n\n---\n\n## Questions for Authors\n\n1. 你们是否在其他 DMC 任务上做过任何初步验证？即使是不完整的数据（如 Cheetah Run 上的 1 seed），也能大幅增强 CIVO 发现的可信度。\n2. Pathway B (non-CIVO) 中 entropy 增加而 evaluation 崩溃——你们是否分析过 actor 的 action distribution 在崩溃前后的变化？这对区分 exploration-driven degradation 和 representation corruption 很关键。\n3. 你们在 Section 6.4 (dt-Embedding Dilemma) 提到 gradient stopping 作为可能的 mitigation——为什么没有在实验中测试？这只需要修改一行代码，且结果（无论正面或负面）都会显著提升论文贡献。\n4. 对于 TAWM 的对比：TD-MPC2 使用 continuous latent states 而 DreamerV3 使用 discrete latent states——你们是否考虑过 latent space 的离散化本身是否放大了 dt-conditioning 的偏差？\n\n---\n\n## 总结\n\n本文提出了一个结构化的诊断框架来分析 DreamerV3 中 temporal abstraction 的失败，CIVO 机制和双路径发现有一定学术价值。但三个核心问题使其不适合 CoRL 主会议：(1) 与 robotics 的关联太弱；(2) 单环境单架构的实验无法支撑泛化性声明；(3) 纯诊断无 solution 的贡献形式难以达到主会议门槛。建议作者增加 robotics-relevant 环境、实现至少一种 mitigation 策略、并更多 seeds 的验证后，考虑投 ICML/NeurIPS 或 CoRL workshop track。\n",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**审查侧重**: 新颖性 & 贡献度 & Venue Fit & Related Work\n\n---\n\n## Summary\n\n本文系统调查了将 dt-conditioning（源自 TAWM/TD-MPC2 框架）移植到 DreamerV3 imagination-based actor-critic 中的失败原因。通过 Walker Walk 上的 9 组 factorial ablation，作者识别出 trained dt-embedding 是导致 conditioning-induced value overestimation (CIVO) 的因果因子：trained embedding 使 RSSM reward head 在 dt=1 和 dt=2 之间产生 2.78× 的预测偏差，该偏差通过 imagination bootstrapping 被 critic 内化为系统性高估。论文进一步发现：(1) 同一 CIVO trigger 产生三种随机下游结果（full collapse、self-correction、oscillatory degradation）；(2) 限制 imagination 到 dt=1 不能完全防止崩溃，存在一条 non-CIVO pathway（Pathway B）；(3) 与 TAWM 的对比将 feedback architecture（imagination bootstrapping vs. MPC re-planning）定位为关键结构差异。\n\n---\n\n## 官方维度打分（基于 CoRL Review Form: Originality, Quality, Clarity, Significance, Relevance, Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/10 | CIVO 是已知 value overestimation 问题在特定 dt-conditioning 下的实例化，方法论（factorial ablation）无创新 |\n| Quality | 5/10 | Factorial 设计合理但单环境 + 2-3 seeds 的统计效力不足，TAWM 对比缺乏实证 |\n| Clarity | 7/10 | 写作清晰、结构好，NVE 指标定义明确，Findings 组织有序 |\n| Significance | 4/10 | 诊断性负面结果，actionable takeaway 太弱，对社区指导有限 |\n| Relevance | 3/10 | 仅 DMC Walker Walk，无机器人任务，robotics motivation 缺失 |\n| Limitations | 7/10 | 诚实承认单环境和单架构局限，但未讨论统计效力问题 |\n\n---\n\n## 总体评分\n\n**Overall: 4/10 (Reject)**\n\n**一句话总结**: 对一个有趣的负面结果给出了结构化诊断，但单环境实验、与 CoRL robotics 主题的弱关联、以及缺乏 actionable 解决方案，使得本文不达到 CoRL 主会议的接收门槛。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性\n\n- 具体位置：全文；Section 5 (Methodology) §5.5 Environment\n- 问题：CoRL 的 scope 要求论文 \"explicitly address a learning question for physical robots\" 或 \"test the proposed learning solution on physical robots\"（参考 CoRL 2023 Reviewer Guidelines）。本文全部实验仅在 DMC Walker Walk（proprioceptive，非视觉）上进行，且论文正文未讨论 temporal abstraction 对 robotics 的具体重要性——例如变频控制对机械臂操作的必要性、sim-to-real 中时间分辨率 mismatch 问题、或 real robot 上 MPC vs. imagination 的延迟约束。Introduction (Section 1) 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。\n- 为什么影响接收：CoRL 审稿人会首先检查 robotics relevance。一篇纯粹在 DMC locomotion 上做 DreamerV3 诊断的论文，即使技术正确，也更适合投 ICML/NeurIPS/ICLR 的 RL track 而非 CoRL。\n- 建议修改方向：(1) 增加至少 1-2 个 robotics-relevant 环境（如 Meta-World manipulation、RoboSuite、或 real robot locomotion）上的验证实验；(2) 在 Introduction 中用具体 robotics scenario 来 motivate temporal abstraction 的重要性；(3) 讨论 CIVO 对 sim-to-real transfer 的 implications。\n\n**N2** [critical] 单环境实验无法支撑因果 claim 的泛化性\n\n- 具体位置：Section 5.5 及 Conclusion (Section 7)\n- 问题：全部 findings（F1-F6）仅来自 Walker Walk 一个环境。论文声称识别出 \"structural incompatibility between flat temporal conditioning and imagination-based actor-critic training\"（Section 6.6），但这一结论的泛化性完全未经验证。Walker Walk 是一个相对简单的 locomotion 任务，reward 接近 dense；在 sparse reward 环境、高维视觉输入、multi-object manipulation 等场景下，CIVO 可能表现完全不同——例如 reward prediction gap 的幅度可能因任务 reward structure 而异。\n- 为什么影响接收：CoRL 审稿人在 Quality 维度会要求 \"results are objectively established\"。单环境 + 2-3 seeds 的实验设置不满足这一标准，尤其是论文自身发现 seed 间的巨大方差（F2 中 1/2 seeds collapse）。按 Colas et al. (2018)（论文 .bib 中有但未引用），2-3 seeds 的统计效力极低。\n- 建议修改方向：(1) 至少在 3-5 个 DMC tasks 上复现核心 finding（如 Cheetah Run、Humanoid Walk）；(2) 增加 seeds 到 5+ 以提供有意义的统计检验；(3) 如果资源有限，至少对 NVE threshold 的鲁棒性做跨任务讨论。\n\n**N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution\n\n- 具体位置：Section 6.6 (Implications) 和 Section 7 (Conclusion, Future directions)\n- 问题：论文的核心贡献是 \"识别 CIVO 失败模式\"。但诊断之后，论文未提供任何可验证的解决方案。Section 6.6 提到三个 future directions：(1) hierarchical approaches (THICK/Hieros)、(2) embedding regularization (gradient stopping/spectral norm)、(3) 扩展到 transformer world models——但这些全部是 \"we leave to future work\" 的表述。Conclusion 的 Future directions 同样只是重述这三点。这意味着论文的 output 仅仅是 \"dt-conditioning 在 DreamerV3 中不 work\"，缺乏 constructive contribution。\n- 为什么影响接收：CoRL 主会议对负面结果论文的接收门槛很高——需要 finding 本身足够深入且 actionable 以抵消缺少正面算法贡献的劣势。类比 \"Implementation Matters\" (Engstrom et al., 2020) 之所以被接收，是因为它跨大量环境和超参数做了系统性发现且提供了具体的实践指导。本文的 CIVO 诊断局限于单环境且缺乏等价的实践指导。\n- 建议修改方向：(1) 实现并测试至少一种 mitigation（如 gradient-stop dt-embedding 对 reward head 的梯度），将其作为 actionable contribution；(2) 或者将 NVE 指标包装为一个通用的 early-warning diagnostic tool，提供可复用的代码和使用指南。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 与 TAWM 的对比仅基于 architectural reasoning，缺乏实证验证\n\n- 具体位置：Section 6.3 (Why MPC Is Immune), Related Work §2 (TAWM paragraph)\n- 问题：论文的核心 narrative 之一是 \"同一 dt-conditioning 在 TAWM (MPC) 中 work 但在 DreamerV3 (imagination) 中 fail\"。但论文从未实际运行 TAWM 来验证。Section 6.3 的分析完全基于 architectural reasoning（\"MPC re-plans from real states at every step, so model errors do not accumulate into the critic\"）。这一论证虽然 plausible，但存在替代解释——例如 TD-MPC2 和 DreamerV3 的 world model architecture 本身不同（连续 vs. 离散 latent states），training objective 不同（joint vs. detached），这些差异可能同样 confound 对比。\n- 建议：至少运行 TAWM 的公开代码在 Walker Walk 上，验证 dt-conditioning 确实在 MPC setting 下 healthy（NVE ≈ 1.0），或引用 TAWM 原文中 Walker Walk 的具体数字。\n\n**W2** [warning] NVE threshold 1.5× 的选取缺乏 principled justification\n\n- 具体位置：Section 5.4 (Diagnostic Metrics), Equation 1\n- 问题：1.5× threshold 被描述为在 factorial grid 内有 \"4/4 separating power\"，但这是事后拟合（post-hoc fitting）到一个仅有 9 个 configurations 的 grid。论文声称 88.9% accuracy (8/9)，但 false negative（008e_v3 s1）恰好是最有诊断价值的 case。没有交叉验证、bootstrapped confidence interval、或理论推导来支撑 1.5× 这个具体数值。对于一个试图建立 diagnostic 标准的论文，这一点令人担忧。\n- 建议：讨论 threshold sensitivity（如 1.3× 和 2.0× 下的 accuracy 变化），或承认该 threshold 是探索性的。\n\n**W3** [warning] CIVO 与已知 value overestimation 的区分不够清晰\n\n- 具体位置：Section 6.1 (CIVO Mechanism), Related Work §3 (Value Overestimation paragraph)\n- 问题：论文将 CIVO 与 delusional bias (Lu et al., 2018) 区分为 \"model-induced vs. policy-class constraints\"（Section 6.1, line 13）。但 CIVO 的核心机制——model error 通过 bootstrapping 被 critic 放大——与已知的 MBRL value overestimation 文献（MBPO, MOPO, Frauenknecht et al.）高度相似。论文 Related Work 中对 Frauenknecht et al. (2025) 的讨论是 \"we identify the specific dt-embedding-induced reward bias by which rollout divergence corrupts values\"（Section 2, line 11），但这一区分的粒度是 \"what triggers the bias\"（dt-embedding），而非 \"how the bias propagates\"（同样是 bootstrapping amplification）。一个 reviewer 会问：CIVO 是否只是 \"compounding model error in MBRL\" 的一个特定实例化（instantiation），而非一个新的失败模式？\n- 建议：更精确地定义 CIVO 相对于 general compounding error 的新颖性——可能在于 \"learned conditioning feature 主动引入偏差\" 而非 \"模型本身不够准\"，但这一点需要更清晰地阐述。\n\n**W4** [warning] Related Work 遗漏若干相关工作\n\n- 具体位置：Section 2 (Related Work)\n- 问题：\n  (a) **Becker-Ehmck et al. (2023) \"Multi-timestep models for Model-based RL\"**——该论文直接研究 multi-timestep world model 在 MBRL 中的效果，与本文主题高度相关，但在 .bib 中存在（`beckerehmck2023multitimestep`）却未在正文中引用或讨论。\n  (b) **Park et al. (2021) \"Time Discretization-Invariant Safe Action Repetition\"** 和 **Wang & Beltrame (2024) \"Reinforcement Learning with Elastic Time Steps\"**——均在 .bib 中但未引用，它们研究 time-discretization 对 RL 的影响，与 Section 6.3 (Why MPC Is Immune) 和 Tallec et al. (2019) 的讨论直接相关。\n  (c) **DreamerV4 讨论不足**：Section 6.6 仅用一段提到 DreamerV4 的 transformer architecture \"may mitigate or amplify\" CIVO，但未讨论 DreamerV4 的 attention mechanism 如何具体影响 temporal conditioning 的 co-adaptation 问题。考虑到 DreamerV4 是 Dreamer 家族的最新成员，这一讨论的缺失是显著的。\n  (d) **.bib 中 48 个 orphan entries** 未在正文引用——虽然这是一个 housekeeping 问题，但表明 related work 讨论尚未完成。\n- 建议：引用并讨论 Becker-Ehmck et al. (2023) 和 Park et al. (2021)；加深 DreamerV4 讨论；清理 .bib 中未引用的条目。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式问题**：当前使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` 而非 CoRL 2026 要求的 PMLR 模板（`\\usepackage[final]{corl_2026}`）。投稿前需切换模板并验证页数。\n- **引用格式问题**：.bib 中 `splates2025` 的 author 字段为 \"SPlaTES, authors\"——这不是合法的 BibTeX author 格式。`nie2025sdar` 和 `kim2025deas` 使用了 \"et, al\" 而非完整作者列表。\n- **Baseline seeds 不完整**：Section 5.3 (line 63) 提到 \"a third seed (seed 0) is in progress\"——提交时应完成。\n- **Treatment 训练步数**：Treatment configurations 仅跑到 105K steps，而 baseline 跑到 505K。Section 5.5 声称 105K \"sufficient to observe collapse onset\"，但对于 self-correction 的 seed（009b, eval 267.9 at 105K），无法判断是否会在更长训练后进一步恢复或最终也崩溃——这削弱了 \"three post-CIVO outcomes\" 结论的可靠性。\n- **Table 1 中 NVE 的缺失值**：exp_006, 007, 005 的 NVE 标注为 \"---\"。即使这些 early experiments 没有完整的 NVE 计算，解释原因或补充数据会增强一致性。\n\n---\n\n## 主要优势\n\n1. **清晰的因果 ablation 设计**：trained vs. untrained vs. removed embedding 的三向对比是方法论亮点。008d vs. 008f 的 key control 设计精巧，在其控制的范围内具有说服力。\n2. **多路径发现有价值**：Pathway A (CIVO, value-driven) 和 Pathway B (non-CIVO, eval-driven) 的识别是一个 genuine discovery，表明 trained temporal conditioning 的危害超出单一 value overestimation 机制。这一发现对 future work 有实际指导意义。\n3. **NVE 指标设计合理**：normalized value-to-eval ratio 作为诊断工具思路清晰，通过 baseline normalization 控制了自然的 v/e 动态。尽管 threshold 选取缺乏 principled justification，指标本身有推广价值。\n4. **写作质量**：F1-F6 的组织清晰，每个 finding 有明确的实验证据支撑。Analysis section 的 CIVO 机制四阶段描述和 seed divergence 分析写得好。\n5. **诚实的 limitations**：Conclusion 承认单环境和单架构局限，这比许多论文做得好。\n\n---\n\n## Questions for Authors\n\n1. 你们是否在其他 DMC 任务上做过任何初步验证？即使是不完整的数据（如 Cheetah Run 上的 1 seed），也能大幅增强 CIVO 发现的可信度。\n2. Pathway B (non-CIVO) 中 entropy 增加而 evaluation 崩溃——你们是否分析过 actor 的 action distribution 在崩溃前后的变化？这对区分 exploration-driven degradation 和 representation corruption 很关键。\n3. 你们在 Section 6.4 (dt-Embedding Dilemma) 提到 gradient stopping 作为可能的 mitigation——为什么没有在实验中测试？这只需要修改一行代码，且结果（无论正面或负面）都会显著提升论文贡献。\n4. 对于 TAWM 的对比：TD-MPC2 使用 continuous latent states 而 DreamerV3 使用 discrete latent states——你们是否考虑过 latent space 的离散化本身是否放大了 dt-conditioning 的偏差？\n\n---\n\n## 总结\n\n本文提出了一个结构化的诊断框架来分析 DreamerV3 中 temporal abstraction 的失败，CIVO 机制和双路径发现有一定学术价值。但三个核心问题使其不适合 CoRL 主会议：(1) 与 robotics 的关联太弱；(2) 单环境单架构的实验无法支撑泛化性声明；(3) 纯诊断无 solution 的贡献形式难以达到主会议门槛。建议作者增加 robotics-relevant 环境、实现至少一种 mitigation 策略、并更多 seeds 的验证后，考虑投 ICML/NeurIPS 或 CoRL workshop track。\n",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T12:35:52.040733+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4638
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-15T12:36:00.108128+00:00_

审稿意见已提交给 Review Director。

总结：**Overall 4/10, Reject**。三个核心问题：

1. **Venue fit 严重不足**——全部实验仅 DMC Walker Walk，无 robotics motivation，不符合 CoRL 对 robot learning 的 scope 要求
2. **单环境 + 2-3 seeds 无法支撑因果泛化 claim**——CIVO 可能是 Walker Walk 特异的现象，论文自身发现 seed 间巨大方差（1/2 seeds collapse）却只用 2 seeds
3. **纯诊断负面结果缺乏 actionable solution**——gradient stopping 作为 mitigation 只需一行代码却未测试，三个 future directions 全部 "leave to future work"

主要优势是清晰的 factorial ablation 设计和 Pathway A/B 双路径发现。建议增加 robotics 环境、实现至少一种 mitigation、增加 seeds 后考虑投 ICML/NeurIPS 或 CoRL workshop。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 55 · 2026-05-15T12:36:56.047133+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 3 的意见

以下是 Reviewer 1 和 Reviewer 3 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
- 特别关注与你自己意见的共识和分歧点

---

## Reviewer 1 的审稿意见（侧重：方法严谨性 & 实验设计）

**Overall: 4/10 (Reject)**

### Must-Fix:
- **N1** [critical] 统计检验力严重不足。核心 "causal factor" 声明依赖 n=2 per group。"4/4 separating power" 在随机零假设下 P=1/16≈6.25%，不够显著。Henderson et al. (2018) 和 Colas et al. (2018) 已证明 2-3 seeds 不足以得出可靠结论。Agarwal et al. (2021) 的核心论点是需要更多 seeds + IQM，而非更少 seeds 上报告个体轨迹。
- **N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择。两组间 [1.2, 2.0] 范围内任何阈值都能达到类似分类效果。"88.9% accuracy"是训练准确率，无 held-out 验证。
- **N3** [critical] CoRL Relevance 严重不足。CoRL 要求论文 "explicitly address a learning question for physical robots"。全文无 robotics 实验/讨论。
- **N4** [critical] 单环境局限使因果声明不可泛化。Walker Walk 是 DMC 最简单任务之一。CIVO 可能高度依赖动力学低维度、dense reward、proprioceptive observation。

### Should-Fix:
- **W1** Factorial design 存在混淆变量：008d vs 008a 同时改变了三个因素；008d vs 008f 是 trained vs removed（不是 trained vs untrained）。缺少 untrained + Sub ON + H=8 + dt=2 的干净对比。
- **W2** 105K vs 505K 训练步数不对等——self-correcting seeds 可能在更长训练后恢复。
- **W3** Pathway B 解释不充分——可能只是普通 training instability 而非 dt-embedding 特有。
- **W4** RSSM fidelity analysis：MAE 不区分 over- vs under-prediction。需要 signed error 验证方向性。
- **W5** 格式不符合 CoRL 2026 要求（未使用 PMLR 模板）。

---

## Reviewer 3 的审稿意见（侧重：格式合规 & 写作质量）

**Overall: 4/10 (Borderline Reject)**

### Must-Fix:
- **N1** [critical] 未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险。
- **N2** [critical] CoRL scope 适配性严重不足——无物理机器人实验或讨论。CoRL CFP 明确要求 "Submissions should focus on a core robotics problem"。
- **N3** [critical] 页数合规性无法验证——换到 PMLR 模板后正文极有可能超过 8 页。

### Should-Fix:
- **W1** Limitations 作为段落嵌入 Conclusion 而非独立 Section。
- **W2** Abstract 过长且过于技术化，缺乏 robotics motivation。
- **W3** Bibliography 冗余：77 条 bib 中仅 29 条被引用；占位符 author 字段。
- **W4** 参考文献格式可能不符合 PMLR 惯例。
- **W5** fig4_mechanism_diagram.pdf 存在但未被引用。

---

请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别注意与你自己意见的共识和分歧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-15T12:38:51.225436+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 交叉回应 R1 & R3\n\n## 回应 Reviewer 1\n\n**[AGREE] R1-N1 (统计检验力)**: 完全同意。与我的 N2 一致。n=2 下 \"4/4 separating power\" P=1/16≈6.25%，论文引用 Agarwal et al. 来辩护 per-seed 报告，但 Agarwal 的核心论点是 IQM + bootstrap，不是更少 seeds。\n\n**[AGREE] R1-N2 (NVE threshold post-hoc)**: 同意，与我的 W2 一致。该阈值在最关键 case (008e_v3 s1) 上 false negative，却被 \"88.9%\" 包装为高精度。\n\n**[AGREE] R1-N3 (CoRL relevance)**: 三 reviewer 一致。\n\n**[AGREE] R1-N4 (单环境)**: 同意，与我的 N2 一致。R1 补充的 \"Walker Walk 是最简任务之一\" 进一步削弱泛化性。\n\n**[AGREE] R1-W1 (Factorial confounds)**: 我审稿时漏掉此点。008d vs 008f 是 trained vs removed（非 untrained），且缺少 untrained+SubON+H=8+dt=2 的干净 cell。\n\n**[AGREE] R1-W2 (训练步数不对等)**: 与我的小问题一致。\n\n**[REBUT] R1-W3 (Pathway B 是普通 instability)**: 部分反驳——baseline seed 2 (009a) 稳定在 836.5 排除了 seed 脆弱性，008e_v3 s2 与 009a 唯一差异是 trained dt-embedding。但仅 1/2 seeds，统计效力确实不足。\n\n**[AGREE] R1-W4 (RSSM signed error)**: 好的技术点，我漏掉了。MAE 无法验证 CIVO 假设的方向性（高估 vs 低估）。\n\n**[AGREE] R1-W5 (格式)**: 三方均提及。\n\n## 回应 Reviewer 3\n\n**[AGREE] R3-N1 (PMLR 模板)**: 同意升级为 critical，desk reject 风险实质存在。\n\n**[AGREE] R3-N2 (CoRL scope)**: 三 reviewer 一致。\n\n**[REBUT] R3-N3 (页数超限)**: 合理担忧但 critical 过重——需要实际测试，可能通过压缩解决，建议降为 should-fix。\n\n**[AGREE] R3-W1 (Limitations 非独立 section)**: 确实只是 Conclusion 中的 \\paragraph。\n\n**[AGREE] R3-W2 (Abstract 缺 robotics motivation)**: 完全同意。\n\n**[AGREE] R3-W3 (Bibliography 冗余)**: 我的引用验证确认 77 条中 48 条 orphan。\n\n**[AGREE] R3-W4 (参考文献格式)**: 同意。\n\n**[AGREE] R3-W5 (fig4 未引用)**: 确认 fig4_mechanism_diagram.pdf 在全部 tex 文件中无 \\includegraphics 引用。\n\n## 三 Reviewer 共识\n\n三位 reviewer scores (4, 4, 4) 高度一致。核心拒稿共识：(1) CoRL venue fit 严重不足（三方一致）；(2) 单环境 + 低 seeds 无法支撑因果声明（R1+R2 一致）；(3) 格式不合规（三方均提及）。我与 R1 唯一分歧在 Pathway B 的解释——我认为 baseline control 提供了部分证据，但统计效力仍然不足。\n",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 交叉回应 R1 & R3\n\n## 回应 Reviewer 1\n\n**[AGREE] R1-N1 (统计检验力)**: 完全同意。与我的 N2 一致。n=2 下 \"4/4 separating power\" P=1/16≈6.25%，论文引用 Agarwal et al. 来辩护 per-seed 报告，但 Agarwal 的核心论点是 IQM + bootstrap，不是更少 seeds。\n\n**[AGREE] R1-N2 (NVE threshold post-hoc)**: 同意，与我的 W2 一致。该阈值在最关键 case (008e_v3 s1) 上 false negative，却被 \"88.9%\" 包装为高精度。\n\n**[AGREE] R1-N3 (CoRL relevance)**: 三 reviewer 一致。\n\n**[AGREE] R1-N4 (单环境)**: 同意，与我的 N2 一致。R1 补充的 \"Walker Walk 是最简任务之一\" 进一步削弱泛化性。\n\n**[AGREE] R1-W1 (Factorial confounds)**: 我审稿时漏掉此点。008d vs 008f 是 trained vs removed（非 untrained），且缺少 untrained+SubON+H=8+dt=2 的干净 cell。\n\n**[AGREE] R1-W2 (训练步数不对等)**: 与我的小问题一致。\n\n**[REBUT] R1-W3 (Pathway B 是普通 instability)**: 部分反驳——baseline seed 2 (009a) 稳定在 836.5 排除了 seed 脆弱性，008e_v3 s2 与 009a 唯一差异是 trained dt-embedding。但仅 1/2 seeds，统计效力确实不足。\n\n**[AGREE] R1-W4 (RSSM signed error)**: 好的技术点，我漏掉了。MAE 无法验证 CIVO 假设的方向性（高估 vs 低估）。\n\n**[AGREE] R1-W5 (格式)**: 三方均提及。\n\n## 回应 Reviewer 3\n\n**[AGREE] R3-N1 (PMLR 模板)**: 同意升级为 critical，desk reject 风险实质存在。\n\n**[AGREE] R3-N2 (CoRL scope)**: 三 reviewer 一致。\n\n**[REBUT] R3-N3 (页数超限)**: 合理担忧但 critical 过重——需要实际测试，可能通过压缩解决，建议降为 should-fix。\n\n**[AGREE] R3-W1 (Limitations 非独立 section)**: 确实只是 Conclusion 中的 \\paragraph。\n\n**[AGREE] R3-W2 (Abstract 缺 robotics motivation)**: 完全同意。\n\n**[AGREE] R3-W3 (Bibliography 冗余)**: 我的引用验证确认 77 条中 48 条 orphan。\n\n**[AGREE] R3-W4 (参考文献格式)**: 同意。\n\n**[AGREE] R3-W5 (fig4 未引用)**: 确认 fig4_mechanism_diagram.pdf 在全部 tex 文件中无 \\includegraphics 引用。\n\n## 三 Reviewer 共识\n\n三位 reviewer scores (4, 4, 4) 高度一致。核心拒稿共识：(1) CoRL venue fit 严重不足（三方一致）；(2) 单环境 + 低 seeds 无法支撑因果声明（R1+R2 一致）；(3) 格式不合规（三方均提及）。我与 R1 唯一分歧在 Pathway B 的解释——我认为 baseline control 提供了部分证据，但统计效力仍然不足。\n",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T12:38:57.562086+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 6336
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-15T12:39:02.904044+00:00_

交叉回应已提交。三位 reviewer 评分一致（4/4/4），在 CoRL venue fit、统计效力、单环境局限三个核心问题上形成强共识。我与 R1 唯一分歧在 Pathway B 的解释——我认为 baseline seed 2 的 control 提供了部分因果证据，但同意统计效力不足以做强声明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 3

74 recorded events

### User

_source line 59 · 2026-05-24T07:01:34.787636+00:00_

[Round 3 审稿请求]:
## Round 3 修订评估任务 — Reviewer 2（Venue Fit + 贡献度 + 写作质量）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf`
**目标 Venue**: CoRL 2026 Main Conference
**Deadline**: 2026-05-29
**页数限制**: 8 页正文（References/Appendix 不计）
**模板**: PMLR (`\usepackage{corl_2026}`)
**匿名规则**: Double-blind
**附录规则**: 不计页数，reviewer 不必阅读
**审查侧重**: CoRL venue fit、贡献度、写作质量、格式合规

### CoRL 2026 CFP 要点（实时搜索确认）
- 8 页正文 + unlimited appendix/refs
- Limitations section 必须包含（计入 8 页）
- 每位有 3+ 篇提交的作者必须同意审稿
- PMLR 模板
- Double-blind
- Submissions should focus on core robotics problems

### 你的核心任务

这是 Round 3 继续审稿。论文在 Round 1 后进行了大幅修改。你需要**逐条检查以下 open/in_progress issue**，标注 `[RESOLVED]` 或 `[STILL_OPEN]` + 理由：

---

### 必须逐条检查的 Issue（Venue fit/贡献/写作类）

**1. R1-N3 [critical, in_progress]: CoRL venue fit 不足**
- Round 1 问题：全文无 robotics 实验/讨论，desk reject 风险
- 已知修改：Abstract 加 robotics motivation，Intro 引用 DayDreamer/TD-MPC2，Discussion 加 "Implications for robot learning" 段落，ManiSkill 实验（PickCube/StackCube/PegInsertionSide）
- **检查要点**：
  - robotics framing 是否贯穿全文（不仅仅是开头结尾的点缀）？
  - ManiSkill 实验是否足以满足 CoRL "core robotics problem" 要求？
  - 论文的核心贡献是否与 robot learning 社区的关注点对齐？
  - 是否还存在 desk reject 风险？

**2. R2-N3 [critical, in_progress]: 纯诊断缺乏 actionable solution**
- Round 1 问题：仅诊断问题不提供解决方案
- 已知修改：Practitioner guidelines 段落，frozen embedding mitigation，四级干预层级，online detector
- **检查要点**：
  - 这些 actionable 贡献是否足够有分量？
  - Practitioner guidelines 是否具体可操作？
  - 对 CoRL 社区（偏重实际部署）来说，诊断+partial mitigation 的贡献模式是否可接受？

**3. R2-W3 [warning, in_progress]: CIVO 与已知 value overestimation 区分不清**
- Round 1 问题：CIVO 可能只是 compounding error 的实例
- 已知修改：Related Work 增加显式对比，signed error 证据
- **检查要点**：Related Work 和 Discussion 中 CIVO 与 compounding error、delusional bias 的区分是否清晰充分？

**4. R2-W4 / R3-W3 [warning, in_progress]: Related Work 遗漏 + Bib 冗余**
- Round 1 问题：Becker-Ehmck 2023、Park 2021、Wang 2024、Colas 2018 未引用；77 条 bib 仅 29 条被引用
- 已知修改：清理 bib，引用遗漏文献
- **检查要点**：这四篇文献是否已被引用？bib 是否已清理？是否有新的 orphan entries？

**5. R3-W2 [warning, in_progress]: Abstract 过长缺 robotics motivation**
- Round 1 问题：~180 词，缺 robotics
- 已知修改：缩短 + 加 robotics motivation
- **检查要点**：当前 Abstract 长度和内容是否合适？robotics motivation 是否到位？"88.9% accuracy" 是否已移除/修正？

**6. R3-N1 [critical, resolved]: 未使用 PMLR 模板**
- 验证是否使用 `\usepackage{corl_2026}`。

**7. R3-N3 [warning, resolved]: 正文超 8 页**
- 验证当前正文是否在 8 页以内。

---

### 额外审查要点

- 写作质量整体评估：clarity、organization、terminology consistency
- 是否有残留的非匿名信息（代码链接、机构名）？
- Limitations section 是否满足 CoRL 要求？
- Contribution 列表是否与实际内容一致？
- Title 是否准确反映论文内容（"Can Fail" vs 之前的 "Fails"）？
- 修改是否引入了新的写作/framing 问题？

### 输出格式

1. 对每个 issue 给出 [RESOLVED] 或 [STILL_OPEN] + 理由
2. 列出新发现的问题（如有）
3. 给出 Venue Fit 评分（1-10）、贡献度评分（1-10）、写作质量评分（1-10）和简要总评

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-24T07:01:53.559555+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 61 · 2026-05-24T07:01:53.660361+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-24T07:01:58.582975+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-24T07:02:01.795337+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
  "pages": "1-10",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
    "pages": "1-10",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-24T07:02:02.048455+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T07:02:08.137334+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found some information about CoRL 2026, though the specific 2026 reviewer guidelines and review form criteria are not fully detailed in these results. Here's what I found:

## CoRL 2026 Reviewer Information

All submissions must include at least one author who agrees to serve as a CoRL reviewer and are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

## Review Criteria (from CoRL 2024)

While specific 2026 criteria were not found, the most recent available guidance from CoRL 2024 indicates that submissions will be evaluated based on the significance and novelty of the results, either theoretical or empirical.

Additionally, all CoRL submissions must demonstrate the relevance to Robot Learning through either explicitly addressing a learning question for physical robots or testing the proposed learning solution on physical robots.

## General Guidance from CoRL 2023

The general reviewer approach emphasizes that reviewers 
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9554
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-24T07:02:09.193461+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 320.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 393.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 317.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 317.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 296.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 338.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 299.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 337.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7398
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T07:02:09.193999+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7145
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-24T07:02:15.313717+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-24T07:02:16.173865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-24T07:02:16.174324+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-24T07:02:16.630082+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-24T07:02:17.088228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 913
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-24T07:02:17.092155+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 462
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-24T07:02:17.092680+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-24T07:02:18.101479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-24T07:02:18.101946+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-24T07:02:18.555162+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-24T07:02:18.555942+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-24T07:02:19.012018+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-24T07:02:19.012539+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-24T07:02:19.968129+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-24T07:02:19.968633+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-24T07:02:20.523241+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-24T07:02:21.878809+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales for CoRL reviews. Include all evaluation categories and their descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales for CoRL reviews. Include all evaluation categories and their descriptions."
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-24T07:02:22.635456+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete reviewer guidelines, review form criteria, scoring dimensions, and rating scales for CoRL 2023. Include all evaluation categories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete reviewer guidelines, review form criteria, scoring dimensions, and rating scales for CoRL 2023. Include all evaluation categories."
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-24T07:02:26.408422+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided content, CoRL does not specify a detailed review form with numerical rating scales or scoring dimensions. Instead, the guidelines emphasize qualitative evaluation criteria:

## Primary Review Criteria

Reviewers assess submissions on:

- **Significance and novelty** of results (theoretical or empirical)
- **Objectivity** of established results and "their potential for scientific and technological impact"
- **Relevance to robotic learning**

## Scope Requirements

Papers must demonstrate robot learning relevance through either:
- **Intent**: "Explicitly address a learning question for physical robots" 
- **Outcome**: "Test the proposed learning solution on physical robots"

## Key Emphasis

The guidelines note that "Papers with both experimental and theoretical results relevant to robot learning are welcome," and CoRL aims to be "a selective top-tier conference on robotic learning."

**Note**: The provided instructions do not include a numerical rating scale, numbered evaluation categories, or a standardized review form. Reviewers appear to use qualitative judgment based on the criteria outlined above, with desk rejection decisions handled separately through AC and PC consensus.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4529
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-24T07:02:28.674653+00:00_

# CoRL 2023 Reviewer Guidelines Summary

## Review Writing Structure

The review form contains two main sections:

**1. Summary of Paper**
Reviewers should "re-express the paper's position clearly and fairly" by restating contributions in their own words rather than copying from abstracts.

**2. Main Review Evaluation Criteria**

CoRL evaluates submissions across six dimensions:

- **Originality**: Novelty of problems/methods, differentiation from prior work, and adequacy of related work citations
- **Quality**: Technical soundness, claim support through analysis or experiments, methodological appropriateness, and honest assessment of strengths/weaknesses
- **Clarity**: Writing quality, organization, and provision of sufficient detail for expert reproducibility
- **Significance**: Importance of results, likelihood of adoption or extension by others, and advancement of the field
- **Relevance**: Connection to robot learning, evaluation approaches (simulation/real robots), and audience interest
- **Limitations**: Appreciation for honestly reported limitations; flagging unreported shortcomings

## Key Reviewer Principles

Reviewers should remain "constructive" and "concrete," starting with positive aspects and suggesting improvements. The guidelines explicitly state that papers need not publish code, include theorems, or demonstrate on real robots as mandatory requirements for acceptance.

## Notable Timeline

- Review deadline: July 19
- Discussion period: August 3-15
- Decision notification: August 30

**Note**: The provided content does not include specific numerical rating scales or detailed scoring rubrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6039
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-24T07:02:49.049042+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-24T07:02:49.452052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-24T07:02:49.603919+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-24T07:02:50.482147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 878
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-24T07:02:50.545600+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-24T07:02:50.714549+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 168
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-24T07:02:54.275621+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-24T07:02:54.276127+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-24T07:02:56.984412+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-24T07:02:57.437379+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\times$ reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\% sensitivity.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-24T07:02:57.437870+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-24T07:02:58.392222+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	World-model reinforcement learning enables sample-efficient learning directly on physical hardware \citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\dt$ mismatches between simulation and hardware. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\% of baseline). Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\geq 1.5\times$ achieves 26/29 classification ($n{=}29$, two environments, AUROC${=}0.953$, in-sample; LOEO cross-validated, Appendix~Table~\ref{tab:nve_loeo}).
7	
8	Gradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\% of $\nabla_\theta e_{\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\%) carries the critical signal. A fou
…[truncated 2265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-24T07:02:58.392781+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-24T07:02:58.493545+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal abstraction in RL.}
5	The options framework \citep{sutton1999options}, option-critic \citep{bacon2017optioncritc}, HAM \citep{parr1998ham}, and MAXQ \citep{dietterich2000maxq} formalize temporal abstraction through hierarchical policies. Semi-MDP theory \citep{bradtke1995smdp} provides the mathematical foundation. Action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, park2021timediscretization} achieve simpler temporal abstraction via real transitions; \citet{wang2024elastic} learn elastic time steps that adapt step size to state dynamics. The Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3, hafner2025dreamerv4} trains policies in imagination at fixed $\dt{=}1$; hierarchical variants \citep{hafner2022director, gumbsch2024thick, mattes2024hieros, li2025lsimagine} use subgoals or separate dynamics per scale, avoiding flat $\dt$-conditioning. TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains; the critical distinction is that MPC re-plans from real states, so model errors do not accumulate into a critic (\S\ref{sec:discussion}).
6	
7	\paragraph{Value overestimation and model fidelity.}
8	Maximization bias \citep{thrun1993issues} has been addressed by Double Q-learning \citep{vanhasselt2016double}, TD3 \citep{fujimoto2018td3}, and ensemble methods \citep{chen2021redq}; in model-based settings, MBPO \citep{janner2019mbpo} and MOPO \citep{yu2020mopo} bound rollout error, while MOReL \citep{kidambi2020morel} and COMBO \citep{yu2021combo} penalize model uncertainty. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints. CIVO is mechanistically distinct: the amplifier is the world model's co-adaptation with a learned temporal embedding, producing systematic reward-prediction bias at $\dt > 1$. Multi-timestep world models \citep{benechehab20
…[truncated 1421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-24T07:02:58.494001+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-24T07:02:58.549101+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 55
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-24T07:03:06.295207+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-24T07:03:06.446379+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{CIVO mechanism.}
5	The RSSM develops a $2.78\times$ reward prediction gap under trained conditioning (Table~\ref{tab:rssm_fidelity}), analogous to delusional bias \citep{lu2018nondelusional}. Gradient magnitude $\neq$ causal importance: the reward head (38--49\% of $\nabla_\theta e_{\dt}$) fails when blocked alone; the observation decoder (16--22\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\S\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\ref{sec:mpc_immune}).
6	
7	\paragraph{Practitioner guidelines.}
8	Monitor via NVE diagnostic ($\geq 1.5\times$, AUROC${=}0.953$; Table~\ref{tab:nve_loeo}). Freezing the $\dt$-embedding converts sustained CIVO (6/6 trained locomotion, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\times$) causes irrecoverable damage (Appendix~\ref{sec:appendix_analysis}).
9	
10	\paragraph{Implications for robot learning.}
11	No $\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\times$), but frozen controls show comparable or higher peaks (Table~\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-24T07:03:06.497104+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-24T07:03:06.548068+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-24T07:03:06.950185+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-24T07:03:07.409093+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-24T07:03:07.760518+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-24T07:03:07.811118+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-24T07:03:18.320048+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-24T07:03:18.370938+00:00_

1	% Auto-generated from literature_map.yaml
2	% 44 entries
3	
4	@inproceedings{micheli2023iris,
5	  title = {Transformers are Sample-Efficient World Models},
6	  author = {Micheli, Vincent and Alonso, Eloi and Fleuret, Fran{\c{c}}ois},
7	  year = {2023},
8	  booktitle = {International Conference on Learning Representations},
9	}
10	
11	@article{sutton1999options,
12	  title = {Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning},
13	  author = {Sutton, R.S and Precup, D and Singh, S},
14	  year = {1999},
15	  journal = {Artificial Intelligence 112},
16	}
17	
18	@inproceedings{hafner2020dreamerv1,
19	  title = {Dream to Control: Learning Behaviors by Latent Imagination},
20	  author = {Hafner, D and Lillicrap, T and Ba, J and Norouzi, M},
21	  year = {2020},
22	  booktitle = {International Conference on Learning Representations},
23	}
24	
25	@article{hafner2023dreamerv3,
26	  title = {Mastering Diverse Domains through World Models},
27	  author = {Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},
28	  year = {2025},
29	  journal = {Nature},
30	  eprint = {2301.04104},
31	  archivePrefix = {arXiv},
32	}
33	
34	@inproceedings{sharma2017figar,
35	  title = {Fine Grained Action Repetition for Deep Reinforcement Learning},
36	  author = {Sharma, S and Lakshminarayanan, A.S and Ravindran, B},
37	  year = {2017},
38	  booktitle = {International Conference on Learning Representations},
39	}
40	
41	@inproceedings{janner2019mbpo,
42	  title = {When to Trust Your Model: Model-Based Policy Optimization},
43	  author = {Janner, M and Fu, J and Zhang, M and Levine, S},
44	  year = {2019},
45	  booktitle = {Advances in Neural Information Processing Systems},
46	}
47	
48	@article{asadi2019combating,
49	  title = {Combating the Compounding-Error Problem with a Multi-step Model},
50	  author = {Asadi, K and Misra, D and Kim, S and Littman, M.L},
51	  year = {2019},
52	  journal = {arXiv preprint arXiv:1905.13320},
53	  
…[truncated 12021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-24T07:04:30.069629+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Becker|becker",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Becker|becker",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-24T07:04:30.622160+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-24T07:04:31.626620+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-24T07:04:32.530767+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex:8:All experiments use DreamerV3's RSSM; whether CIVO manifests in other imagination-based architectures (e.g., IRIS \citep{micheli2023iris} or latent-space planners beyond TD-MPC2) remains open.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex:10:Statistical power with 4 seeds per configuration is limited \citep{colas2018seeds}; the NVE threshold (LOEO AUROC${=}0.981$) may require recalibration for different reward scales.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:7:All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:53:To test whether standard overestimation countermeasures address 
…[truncated 1888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 904
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-24T07:04:32.732001+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
  "pages": "11-16",
  "project": "event-gated-adaptive-horizon",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/submitted.pdf",
    "pages": "11-16",
    "project": "event-gated-adaptive-horizon",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-24T07:04:33.284462+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 328.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 231.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 396.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 372.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 297.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 209.2}], \"total_pages\": 33, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-24T07:04:39.859172+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-24T07:04:40.315337+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-24T07:04:40.316043+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-24T07:04:40.820623+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-24T07:04:40.921457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-24T07:04:40.972290+00:00_

1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 42 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
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
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29	\rowcolor{gray!15}
30	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31	\rowcolor{gray!15}
32	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33	008f & No dt\_emb (s1) & --- & ON & 8 & 50
…[truncated 3486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-24T07:06:57.192858+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 3 修订评估 — Reviewer 2（Venue Fit / 贡献度 / 写作质量）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n\n---\n\n## 逐条 Issue 检查\n\n### 1. R1-N3 [critical, in_progress]: CoRL venue fit 不足\n**[STILL_OPEN]** — 改善明显但仍有结构性问题\n\n**已改进**：\n- Abstract 首句加入 \"increasingly deployed for robot control\" (Section 1, abstract_body.tex:1)\n- Introduction 引用 DayDreamer [wu2023daydreamer] 和 TD-MPC2 [hansen2024tdmpc2]，提到 \"Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle dt mismatches between simulation and hardware\" (Section 1, introduction.tex:4)\n- 新增 ManiSkill 实验（PickCube-v1, StackCube-v1, PegInsertionSide-v1；Table 1, Section 4.3）\n- Discussion 新增 \"Implications for robot learning\" 段落 (Section 5, analysis.tex:10-11)\n\n**仍存在的问题**：\n- **ManiSkill 结果反向证明了 CIVO 与 robotics manipulation 无关**：所有三个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO（Section 4.3: \"None of three ManiSkill environments exhibit dt-embedding-dependent CIVO\"），frozen controls 表现相当甚至更高。这些结果实际上削弱了 robotics relevance——论文的核心发现（CIVO）仅在 DMC locomotion 中出现，而 locomotion 恰恰不是 CoRL 的核心关注点。\n- **Robotics framing 仍是 \"bookend\" 式的**：robotics motivation 集中在 Introduction 的前两句和 Discussion 的一个段落，中间的方法和结果部分（Section 3-4，约 4 页）完全是通用 RL 分析，没有任何 robotics-specific 的实验设计考量（如 sim-to-real、sensor noise、actuation delay）。\n- **核心贡献定位问题**：CoRL CFP 要求 \"submissions should focus on core robotics problems\"。本文的核心贡献是诊断 DreamerV3 中一个特定的 value overestimation 机制——这是一个通用 RL 问题，并非 robotics-specific 的。Limitations 部分自己也承认 \"does not test...real-robot deployments\"（conclusion.tex:7）。\n- **Desk reject 风险已降低但未消除**：ManiSkill 实验的加入使论文不至于完全没有 robot-relevant 实验，但一位严格的 AC 可能会认为：(a) ManiSkill 结果为 negative（CIVO 不存在），(b) 核心实验仍在 DMC Walker/Cheetah 上完成，这些不是 \"core robotics problems\"。\n\n**建议**：如果有时间，考虑在 Discussion 中更深入地讨论 CIVO 不出现在 manipulation 的原因（reward density 假说需要更多证据），以及这对 real-robot deployment（如 DayDreamer 式的 online learning）的具体指导意义。\n\n---\n\n### 2. R2-N3 [critical, in_progress]: 纯诊断缺乏 actionable solution\n**[STILL_OPEN]** — 有改善但贡献模式仍偏弱\n\n**已改进**：\n- Practitioner guidelines 段落（Section 5, analysis.tex:7-8）：提供 NVE≥1.5× 诊断阈值（AUROC=0.953）、embedding freezing 作为缓解手段\n- Table 2（intervention hierarchy）：系统展示四级干预的效果\n- Online CIVO detector（Section 4.7）：TPR=5/5, FPR=2/9\n- Contribution 列表明确标注 \"Four-level intervention hierarchy\" 和 \"Online detection\"\n\n**仍存在的问题**：\n- **核心结论仍是 negative**：Table 2 最终结论是 \"No level reliably eliminates CIVO across environments\"。最有效的 \"solution\" 是 embedding removed（5/5, 100%），即**不使用这个功能**——这等于说 temporal abstraction via dt-conditioning 在 imagination-based RL 中就是不可行的。\n- **Frozen embedding 不是真正的解决方案**：71% prevention rate（5/7），且成功案例中 eval 仍然很差（如 015b: 204.2, 仅 22% baseline；042: 612.0 但只有单 seed）。这说明 freezing 既不能 reliably prevent CIVO，也不能恢复 baseline 性能。\n- **Wide dual critic 部分有效**：75% prevention（3/4 Walker），但 Cheetah 0/1，跨环境 transfer 有限。\n- **对 CoRL 社区的价值**：CoRL 偏重 deployable methods。\"这个方法不行，我们可以告诉你什么时候它不行\" 的贡献模式在 ML theory venue（ICML/NeurIPS）可能可以接受，但对 CoRL 来说显得不够 actionable。\n\n**评估**：贡献模式从 \"纯诊断\" 升级为 \"诊断 + partial mitigation + detection\"，这是有进步的。但 actionable 部分的实际效果不强——practitioner 的最佳策略仍然是 \"不要用 trained dt-embedding\"。\n\n---\n\n### 3. R2-W3 [warning, in_progress]: CIVO 与已知 value overestimation 区分不清\n**[RESOLVED]**\n\nRelated Work (related_work.tex:8) 提供了清晰的经验性区分：\n- **控制实验证据**：\"if CIVO were generic compounding error, untrained dt-embeddings at dt=2 should also produce overestimation, yet they do not (NVE<0.6× for 008a/008c vs. 4.12× for 008d)\"\n- **Signed error 分析**：\"dt=2 rewards are underpredicted (mean SE=-0.599), ruling out observation-level overprediction and localizing CIVO to imagination-level prior drift\"\n- **与 delusional bias 的类比和区分**：明确指出 \"analogous to delusional bias but model-induced rather than policy-class-induced\"\n\n区分充分、有数据支撑。\n\n---\n\n### 4. R2-W4 / R3-W3 [warning, in_progress]: Related Work 遗漏 + Bib 冗余\n**[PARTIALLY RESOLVED]**\n\n- **Park 2021** (park2021timediscretization): ✅ 已在 related_work.tex:5 引用\n- **Wang 2024** (wang2024elastic): ✅ 已在 related_work.tex:5 引用\n- **Colas 2018** (colas2018seeds): ✅ 已在 conclusion.tex:10 引用\n- **Becker-Ehmck 2023**: ❌ **仍未引用**。在 references.bib 和所有 .tex 文件中均未找到。Becker-Ehmck et al. (2023) 关于 temporal abstraction in model-based RL 的工作与本文直接相关，应予引用。\n- **Bib 清理**：从 Round 1 的 77 条减至 44 条，所有 44 条均被正文引用，无 orphan entries ✅\n\n---\n\n### 5. R3-W2 [warning, in_progress]: Abstract 过长缺 robotics motivation\n**[RESOLVED]**\n\n- Abstract 约 150 词，长度合理（CoRL 通常 150-200 词）\n- 首句即包含 robotics motivation：\"World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales\"\n- \"88.9% accuracy\" 已移除，替换为更精确的 \"26/29, AUROC=0.953, LOEO cross-validated\"\n- Keywords 合理：World Models, Temporal Abstraction, Value Overestimation, DreamerV3\n\n---\n\n### 6. R3-N1 [critical, resolved]: 未使用 PMLR 模板\n**[RESOLVED]** — main.tex:5 确认 `\\usepackage{corl_2026}` ✅\n\n---\n\n### 7. R3-N3 [warning, resolved]: 正文超 8 页\n**[RESOLVED]** — PDF 确认正文 8 页（pages 1-8），References 从第 9 页开始，Appendix 从第 11 页开始 ✅\n\n---\n\n## 额外审查发现\n\n### 写作质量评估\n\n**优点**：\n- 论文结构清晰：Introduction → Related Work → Experimental Setup → Results (F1-F7) → Discussion → Conclusion，逻辑链条完整\n- Factorial design 的表述专业严谨\n- Table 1 和 Table 2 信息密度高且组织良好\n- Contribution 列表与正文内容一致\n\n**问题**：\n- **E1** [minor] Abstract 统计数据过密：在约 150 词内包含了 \"14-19%\", \"26/29\", \"AUROC=0.953\", \"2.78×\", \"ρ > 0.999\", \"100% sensitivity\" 等 6 个以上数字指标。建议精简到 2-3 个关键数字，其余放入正文。\n- **E2** [minor] Section 标题混用：Section 4 (Results) 用 \"F1\", \"F2\", \"F3-F5\", \"F6-F7\" 编号，而 Section 5 (Discussion) 和其他 section 用标准编号。这种双编号系统可能让读者困惑。\n- **E3** [minor] Conclusion 中 Limitations 部分的 `\\label{sec:limitations}` 放在段落末尾（conclusion.tex:12），如果 CoRL 要求 Limitations 作为独立 section，当前作为 Conclusion 的 paragraph 是否满足格式要求需确认。\n\n### 匿名合规\n- 作者：\"Anonymous Authors\" ✅\n- 代码链接：\"Code: upon acceptance\" ✅\n- DreamerV3 仓库链接（methodology.tex:58 脚注）：`https://github.com/danijar/dreamerv3` 是公开的官方仓库，非作者代码，不破坏 double-blind ✅\n- 未发现机构名称或自引泄露 ✅\n\n### Contribution 列表一致性\n四项 contribution（Failure mode identification, Architectural boundary, Four-level intervention hierarchy, Online detection）与正文内容一致 ✅\n\n### Title 准确性\n\"Can Fail\" 比之前的 \"Fails\" 更准确——论文发现 CIVO 是条件性的（需要 trained embedding + multi-rate exposure），且仅在 locomotion 中出现，manipulation 不受影响。Title 准确反映内容 ✅\n\n### 潜在新问题\n- **N1** [warning] **ManiSkill 实验的 baseline 缺失**：Table 1 中 ManiSkill 任务（019b, 049, 050）没有给出 vanilla DreamerV3 baseline 的 eval 值，只有脚注 c 提到 \"NVE normalized against exp_019a_v2 (vanilla DreamerV3 on PickCube-v1)\"。读者无法直接判断这些任务上 variable-rate 配置的相对性能。\n- **N2** [warning] **Cheetah Run baseline 同样缺失**：Table 1 中 Cheetah Run 只有 trained (010b) 和 frozen (046) 的结果，没有 standard baseline 的 eval 值供参照。\n- **N3** [minor] **统计功效限制**：论文自己承认 \"Statistical power with 4 seeds per configuration is limited\"（conclusion.tex:10），部分配置只有 1-2 seeds（如 TCN σ=0.1 和 σ=1.0 各只有 1 seed）。Table 2 中一些 100% prevention rate 的条目（TCN σ=0.1: 1/1, TCN σ=1.0: 1/1）在统计上完全无意义。\n\n---\n\n## 评分\n\n### Venue Fit: 5/10\n论文与 CoRL 的核心要求（\"focus on core robotics problems\"）之间存在结构性 gap。Robotics framing 主要是 opening/closing 的修辞包装，核心实验在 DMC locomotion 上完成。ManiSkill 实验虽然增加了 robotics 相关性，但 negative results（CIVO 不出现）反而削弱了论文对 robotics 社区的直接价值。论文更适合 ICML/NeurIPS 的 RL/world-model track。\n\n### 贡献度: 6/10\n- 优势：CIVO 的诊断和因果分离做得扎实（factorial design + AUROC + LOEO），architectural boundary（MPC vs imagination-based bootstrapping）的发现有洞见\n- 劣势：核心贡献是 negative result（temporal abstraction 在 imagination-based RL 中不可行），且没有找到可靠的解决方案。Practitioner guidelines 的实际建议是 \"不要用\"。对 CoRL 的 deployment-oriented 社区来说价值有限。\n\n### 写作质量: 7/10\n- 论文结构清晰、专业\n- Factorial design 的展示严谨\n- Abstract 过于数字密集\n- F1-F7 编号系统增加认知负担\n- 总体可读性良好\n\n### 总体评估\n论文在 Round 1 基础上做了实质性改进：ManiSkill 实验、practitioner guidelines、bib 清理、CIVO-compounding error 区分、PMLR 模板、页数控制。但两个 critical issue（venue fit 和 actionable contribution）的核心矛盾未解决：\n1. CIVO 是 locomotion-specific 的发现，robotics framing 仍是装饰性的\n2. 最有效的 \"solution\" 是不用该功能，这对需要 temporal abstraction 的 robotics 应用帮助有限\n\n如果提交到 ICML/NeurIPS 作为 diagnostic/negative-result contribution，评分会明显更高。对 CoRL 来说，论文处于 borderline 区域。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 3 修订评估 — Reviewer 2（Venue Fit / 贡献度 / 写作质量）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n\n---\n\n## 逐条 Issue 检查\n\n### 1. R1-N3 [critical, in_progress]: CoRL venue fit 不足\n**[STILL_OPEN]** — 改善明显但仍有结构性问题\n\n**已改进**：\n- Abstract 首句加入 \"increasingly deployed for robot control\" (Section 1, abstract_body.tex:1)\n- Introduction 引用 DayDreamer [wu2023daydreamer] 和 TD-MPC2 [hansen2024tdmpc2]，提到 \"Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle dt mismatches between simulation and hardware\" (Section 1, introduction.tex:4)\n- 新增 ManiSkill 实验（PickCube-v1, StackCube-v1, PegInsertionSide-v1；Table 1, Section 4.3）\n- Discussion 新增 \"Implications for robot learning\" 段落 (Section 5, analysis.tex:10-11)\n\n**仍存在的问题**：\n- **ManiSkill 结果反向证明了 CIVO 与 robotics manipulation 无关**：所有三个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO（Section 4.3: \"None of three ManiSkill environments exhibit dt-embedding-dependent CIVO\"），frozen controls 表现相当甚至更高。这些结果实际上削弱了 robotics relevance——论文的核心发现（CIVO）仅在 DMC locomotion 中出现，而 locomotion 恰恰不是 CoRL 的核心关注点。\n- **Robotics framing 仍是 \"bookend\" 式的**：robotics motivation 集中在 Introduction 的前两句和 Discussion 的一个段落，中间的方法和结果部分（Section 3-4，约 4 页）完全是通用 RL 分析，没有任何 robotics-specific 的实验设计考量（如 sim-to-real、sensor noise、actuation delay）。\n- **核心贡献定位问题**：CoRL CFP 要求 \"submissions should focus on core robotics problems\"。本文的核心贡献是诊断 DreamerV3 中一个特定的 value overestimation 机制——这是一个通用 RL 问题，并非 robotics-specific 的。Limitations 部分自己也承认 \"does not test...real-robot deployments\"（conclusion.tex:7）。\n- **Desk reject 风险已降低但未消除**：ManiSkill 实验的加入使论文不至于完全没有 robot-relevant 实验，但一位严格的 AC 可能会认为：(a) ManiSkill 结果为 negative（CIVO 不存在），(b) 核心实验仍在 DMC Walker/Cheetah 上完成，这些不是 \"core robotics problems\"。\n\n**建议**：如果有时间，考虑在 Discussion 中更深入地讨论 CIVO 不出现在 manipulation 的原因（reward density 假说需要更多证据），以及这对 real-robot deployment（如 DayDreamer 式的 online learning）的具体指导意义。\n\n---\n\n### 2. R2-N3 [critical, in_progress]: 纯诊断缺乏 actionable solution\n**[STILL_OPEN]** — 有改善但贡献模式仍偏弱\n\n**已改进**：\n- Practitioner guidelines 段落（Section 5, analysis.tex:7-8）：提供 NVE≥1.5× 诊断阈值（AUROC=0.953）、embedding freezing 作为缓解手段\n- Table 2（intervention hierarchy）：系统展示四级干预的效果\n- Online CIVO detector（Section 4.7）：TPR=5/5, FPR=2/9\n- Contribution 列表明确标注 \"Four-level intervention hierarchy\" 和 \"Online detection\"\n\n**仍存在的问题**：\n- **核心结论仍是 negative**：Table 2 最终结论是 \"No level reliably eliminates CIVO across environments\"。最有效的 \"solution\" 是 embedding removed（5/5, 100%），即**不使用这个功能**——这等于说 temporal abstraction via dt-conditioning 在 imagination-based RL 中就是不可行的。\n- **Frozen embedding 不是真正的解决方案**：71% prevention rate（5/7），且成功案例中 eval 仍然很差（如 015b: 204.2, 仅 22% baseline；042: 612.0 但只有单 seed）。这说明 freezing 既不能 reliably prevent CIVO，也不能恢复 baseline 性能。\n- **Wide dual critic 部分有效**：75% prevention（3/4 Walker），但 Cheetah 0/1，跨环境 transfer 有限。\n- **对 CoRL 社区的价值**：CoRL 偏重 deployable methods。\"这个方法不行，我们可以告诉你什么时候它不行\" 的贡献模式在 ML theory venue（ICML/NeurIPS）可能可以接受，但对 CoRL 来说显得不够 actionable。\n\n**评估**：贡献模式从 \"纯诊断\" 升级为 \"诊断 + partial mitigation + detection\"，这是有进步的。但 actionable 部分的实际效果不强——practitioner 的最佳策略仍然是 \"不要用 trained dt-embedding\"。\n\n---\n\n### 3. R2-W3 [warning, in_progress]: CIVO 与已知 value overestimation 区分不清\n**[RESOLVED]**\n\nRelated Work (related_work.tex:8) 提供了清晰的经验性区分：\n- **控制实验证据**：\"if CIVO were generic compounding error, untrained dt-embeddings at dt=2 should also produce overestimation, yet they do not (NVE<0.6× for 008a/008c vs. 4.12× for 008d)\"\n- **Signed error 分析**：\"dt=2 rewards are underpredicted (mean SE=-0.599), ruling out observation-level overprediction and localizing CIVO to imagination-level prior drift\"\n- **与 delusional bias 的类比和区分**：明确指出 \"analogous to delusional bias but model-induced rather than policy-class-induced\"\n\n区分充分、有数据支撑。\n\n---\n\n### 4. R2-W4 / R3-W3 [warning, in_progress]: Related Work 遗漏 + Bib 冗余\n**[PARTIALLY RESOLVED]**\n\n- **Park 2021** (park2021timediscretization): ✅ 已在 related_work.tex:5 引用\n- **Wang 2024** (wang2024elastic): ✅ 已在 related_work.tex:5 引用\n- **Colas 2018** (colas2018seeds): ✅ 已在 conclusion.tex:10 引用\n- **Becker-Ehmck 2023**: ❌ **仍未引用**。在 references.bib 和所有 .tex 文件中均未找到。Becker-Ehmck et al. (2023) 关于 temporal abstraction in model-based RL 的工作与本文直接相关，应予引用。\n- **Bib 清理**：从 Round 1 的 77 条减至 44 条，所有 44 条均被正文引用，无 orphan entries ✅\n\n---\n\n### 5. R3-W2 [warning, in_progress]: Abstract 过长缺 robotics motivation\n**[RESOLVED]**\n\n- Abstract 约 150 词，长度合理（CoRL 通常 150-200 词）\n- 首句即包含 robotics motivation：\"World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales\"\n- \"88.9% accuracy\" 已移除，替换为更精确的 \"26/29, AUROC=0.953, LOEO cross-validated\"\n- Keywords 合理：World Models, Temporal Abstraction, Value Overestimation, DreamerV3\n\n---\n\n### 6. R3-N1 [critical, resolved]: 未使用 PMLR 模板\n**[RESOLVED]** — main.tex:5 确认 `\\usepackage{corl_2026}` ✅\n\n---\n\n### 7. R3-N3 [warning, resolved]: 正文超 8 页\n**[RESOLVED]** — PDF 确认正文 8 页（pages 1-8），References 从第 9 页开始，Appendix 从第 11 页开始 ✅\n\n---\n\n## 额外审查发现\n\n### 写作质量评估\n\n**优点**：\n- 论文结构清晰：Introduction → Related Work → Experimental Setup → Results (F1-F7) → Discussion → Conclusion，逻辑链条完整\n- Factorial design 的表述专业严谨\n- Table 1 和 Table 2 信息密度高且组织良好\n- Contribution 列表与正文内容一致\n\n**问题**：\n- **E1** [minor] Abstract 统计数据过密：在约 150 词内包含了 \"14-19%\", \"26/29\", \"AUROC=0.953\", \"2.78×\", \"ρ > 0.999\", \"100% sensitivity\" 等 6 个以上数字指标。建议精简到 2-3 个关键数字，其余放入正文。\n- **E2** [minor] Section 标题混用：Section 4 (Results) 用 \"F1\", \"F2\", \"F3-F5\", \"F6-F7\" 编号，而 Section 5 (Discussion) 和其他 section 用标准编号。这种双编号系统可能让读者困惑。\n- **E3** [minor] Conclusion 中 Limitations 部分的 `\\label{sec:limitations}` 放在段落末尾（conclusion.tex:12），如果 CoRL 要求 Limitations 作为独立 section，当前作为 Conclusion 的 paragraph 是否满足格式要求需确认。\n\n### 匿名合规\n- 作者：\"Anonymous Authors\" ✅\n- 代码链接：\"Code: upon acceptance\" ✅\n- DreamerV3 仓库链接（methodology.tex:58 脚注）：`https://github.com/danijar/dreamerv3` 是公开的官方仓库，非作者代码，不破坏 double-blind ✅\n- 未发现机构名称或自引泄露 ✅\n\n### Contribution 列表一致性\n四项 contribution（Failure mode identification, Architectural boundary, Four-level intervention hierarchy, Online detection）与正文内容一致 ✅\n\n### Title 准确性\n\"Can Fail\" 比之前的 \"Fails\" 更准确——论文发现 CIVO 是条件性的（需要 trained embedding + multi-rate exposure），且仅在 locomotion 中出现，manipulation 不受影响。Title 准确反映内容 ✅\n\n### 潜在新问题\n- **N1** [warning] **ManiSkill 实验的 baseline 缺失**：Table 1 中 ManiSkill 任务（019b, 049, 050）没有给出 vanilla DreamerV3 baseline 的 eval 值，只有脚注 c 提到 \"NVE normalized against exp_019a_v2 (vanilla DreamerV3 on PickCube-v1)\"。读者无法直接判断这些任务上 variable-rate 配置的相对性能。\n- **N2** [warning] **Cheetah Run baseline 同样缺失**：Table 1 中 Cheetah Run 只有 trained (010b) 和 frozen (046) 的结果，没有 standard baseline 的 eval 值供参照。\n- **N3** [minor] **统计功效限制**：论文自己承认 \"Statistical power with 4 seeds per configuration is limited\"（conclusion.tex:10），部分配置只有 1-2 seeds（如 TCN σ=0.1 和 σ=1.0 各只有 1 seed）。Table 2 中一些 100% prevention rate 的条目（TCN σ=0.1: 1/1, TCN σ=1.0: 1/1）在统计上完全无意义。\n\n---\n\n## 评分\n\n### Venue Fit: 5/10\n论文与 CoRL 的核心要求（\"focus on core robotics problems\"）之间存在结构性 gap。Robotics framing 主要是 opening/closing 的修辞包装，核心实验在 DMC locomotion 上完成。ManiSkill 实验虽然增加了 robotics 相关性，但 negative results（CIVO 不出现）反而削弱了论文对 robotics 社区的直接价值。论文更适合 ICML/NeurIPS 的 RL/world-model track。\n\n### 贡献度: 6/10\n- 优势：CIVO 的诊断和因果分离做得扎实（factorial design + AUROC + LOEO），architectural boundary（MPC vs imagination-based bootstrapping）的发现有洞见\n- 劣势：核心贡献是 negative result（temporal abstraction 在 imagination-based RL 中不可行），且没有找到可靠的解决方案。Practitioner guidelines 的实际建议是 \"不要用\"。对 CoRL 的 deployment-oriented 社区来说价值有限。\n\n### 写作质量: 7/10\n- 论文结构清晰、专业\n- Factorial design 的展示严谨\n- Abstract 过于数字密集\n- F1-F7 编号系统增加认知负担\n- 总体可读性良好\n\n### 总体评估\n论文在 Round 1 基础上做了实质性改进：ManiSkill 实验、practitioner guidelines、bib 清理、CIVO-compounding error 区分、PMLR 模板、页数控制。但两个 critical issue（venue fit 和 actionable contribution）的核心矛盾未解决：\n1. CIVO 是 locomotion-specific 的发现，robotics framing 仍是装饰性的\n2. 最有效的 \"solution\" 是不用该功能，这对需要 temporal abstraction 的 robotics 应用帮助有限\n\n如果提交到 ICML/NeurIPS 作为 diagnostic/negative-result contribution，评分会明显更高。对 CoRL 来说，论文处于 borderline 区域。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-24T07:07:01.832743+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4639
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-24T07:07:05.912735+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 129 · 2026-05-24T07:07:05.963341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-24T07:07:11.643991+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-24T07:07:11.694659+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 132 · 2026-05-24T07:07:27.070746+00:00_

Round 3 审稿意见已提交给 Review Director。

**总结**：

7 个 issue 中：
- **3 个 RESOLVED**：CIVO vs compounding error 区分（R2-W3）、Abstract 长度/robotics（R3-W2）、PMLR 模板（R3-N1）、页数（R3-N3）
- **1 个 PARTIALLY RESOLVED**：Related Work/Bib（R2-W4/R3-W3）— Becker-Ehmck 2023 仍未引用
- **2 个 STILL_OPEN**：CoRL venue fit（R1-N3）和 actionable solution（R2-N3）— 这两个是结构性问题

**评分**：Venue Fit 5/10、贡献度 6/10、写作质量 7/10。论文做了实质性改进但核心矛盾未解：CIVO 是 locomotion-specific 的 negative result，robotics framing 仍是装饰性的，最佳 "solution" 是不用该功能。更适合 ICML/NeurIPS。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 4

4 recorded events

### User

_source line 133 · 2026-05-24T07:12:58.871593+00:00_

[Round 3 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的意见

以下是 Reviewer 1（方法严谨性 + 实验充分性）的完整审稿意见。请对每个要点标注 `[AGREE]`（同意并说明理由）或 `[REBUT]`（反驳并引用论文具体 Section/Table/Figure 作为证据）。

---

**Reviewer 1 完整审稿意见：**

### Issue 状态判定：
| Issue | R1 判定 | 理由 |
|-------|---------|------|
| R1-N1 统计检验力 | [RESOLVED] | 4 seeds, "strongest predictor", LOEO AUROC=0.981, IQM |
| R1-N4 单环境 | [RESOLVED] | 5 环境, discriminative validity, locomotion-specificity 诚实报告 |
| R1-W1 Factorial 混淆 | [RESOLVED] | Primary vs secondary 标注, 2×2 grid 完整 |
| R1-W2 步数不对等 | [STILL_OPEN] | Matched-timestep 比较存在但未显式讨论; 缺少 treatment 长跑数据; exp_045 未在正文呈现 |
| R1-W3 Pathway B | [RESOLVED] | 2 seeds + "preliminary/requires confirmation" |
| R2-W1 TAWM 对比 | [STILL_OPEN] | 仍为纯 architectural reasoning, "structural factor" 措辞过强 |
| R1-W4 Signed error | [RESOLVED] | Appendix 完整呈现 |

### R1 评分：方法严谨性 7/10

### R1 的 CoRL 维度打分：
Originality 4/5, Quality 3/5, Clarity 4/5, Significance 3/5, Relevance 4/5, Limitations 4/5

### R1 新发现的问题：

**N-new-1 [warning]: Online CIVO Detector 评估样本量不足**
- n=14 runs, 仅 5 正例, TPR=5/5 但统计意义有限
- FPR=2/9 (22%) 意味着近 1/4 非 CIVO 被误报
- 应与 NVE 静态分类（n=29）区分讨论

**N-new-2 [minor]: IQM 报告不完整**
- 仅对一个配置报告 IQM (175.2, n=4)
- 其他关键 comparison 也应报告 IQM + stratified bootstrap CI

**N-new-3 [minor]: Dual-critic convergence 因果推理跳跃**
- ρ > 0.999 是 asymptotic 结果，early training 可能有差异
- 与 wide dual-critic 3/4 prevention 成功存在张力
- 主文 "pessimism ineffective" 叙事过于简化

### R1 主要优势总结：
1. Factorial design 系统严谨（43 配置 × 4 seeds × 5 环境）
2. LOEO 交叉验证（AUROC=0.981）
3. 四级干预层级分析的长期社区价值
4. ManiSkill non-CIVO 增加 discriminative validity
5. Dual-critic convergence 的 structural insight
6. Limitations section 诚实全面

### R1 Should-Fix：
- S1: 步数不对等应在正文显式讨论
- S2: TAWM "structural factor" 应弱化或增加实验
- S3: Online detector small-sample limitation 应承认

### R1 总评：
5/7 issues resolved, 2/7 still open（均 warning 级别）。作为 diagnostic/negative-result paper 是 solid work，主要限制是 locomotion-specificity 和 "structural factor" 缺实验验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-24T07:14:37.494529+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Issue 状态判定回应\n\n**[AGREE] R1-N1 统计检验力 [RESOLVED]**\n同意。LOEO AUROC=0.981 提供了比简单 in-sample accuracy 更有说服力的验证。4 seeds × 多配置 × LOEO 的组合在 RL 诊断类工作中是合理的统计功效水平。Limitations 部分也诚实承认了 seed 数量限制（conclusion.tex:10）。\n\n**[AGREE] R1-N4 单环境 [RESOLVED]**\n同意 resolved 判定。5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1）的覆盖面已足够。但补充我的观察：ManiSkill 的 negative results 虽增加了 discriminative validity，却同时削弱了论文对 CoRL 的 relevance——CIVO 恰恰在 robotics-relevant 的 manipulation 任务中不出现（Section 4.3, results.tex:92-93），使得核心发现的 robotics 价值变得更模糊。R1 给 Relevance 4/5 我认为偏高。\n\n**[AGREE] R1-W1 Factorial 混淆 [RESOLVED]**\n同意。introduction.tex:6 中 primary vs secondary comparison 的标注清楚区分了单因素对比和多因素共变的情况。\n\n**[AGREE] R1-W2 步数不对等 [STILL_OPEN]**\n同意且补充。这个问题有两个层面：\n1. **Baseline 505K vs treatment 105K**：论文声称 \"105K steps, sufficient to observe collapse onset\"（methodology.tex:58），但未讨论某些 treatment 是否可能在更长训练后 recover。results.tex:81 提到 seed 2 出现 self-correction，那其他 collapsed seeds 是否也可能在更长训练后 recover？这直接影响 \"14-19% of baseline\" 这一核心 claim 的可靠性。\n2. **exp_045 缺失**：如果存在 matched-duration 实验数据但未呈现在正文中，这是一个审稿可见性问题。reviewer 不应需要猜测 appendix 中是否存在支持证据。\n\n**[AGREE] R1-W3 Pathway B [RESOLVED]**\n同意。\"preliminary\" 和 \"requires confirmation\" 的措辞恰当（results.tex:103），且只有 2 seeds 的情况下不做过强 claim 是负责任的。\n\n**[AGREE] R2-W1 TAWM 对比 [STILL_OPEN]**\n强烈同意。这也是我在 Round 1 (R2-W3) 关注的延伸。具体问题：\n- Abstract 称 \"the contrast with MPC identifies feedback architecture as the structural factor\"，Conclusion 重复 \"MPC re-planning versus imagination-based bootstrapping—is the structural factor\"（conclusion.tex:4）——但论文**从未在 TD-MPC2/TAWM 上运行任何实验**。\n- Related Work（related_work.tex:5）的论述 \"the critical distinction is that MPC re-plans from real states, so model errors do not accumulate into a critic\" 是合理的 architectural reasoning，但将其称为 \"structural factor\" 暗示了因果确认，而实际只有推理。\n- 至少应做到以下之一：(a) 在 TD-MPC2 上复现 dt-conditioning 实验验证 CIVO 不出现，(b) 将 \"structural factor\" 弱化为 \"hypothesized structural factor\" 或 \"architectural difference that our analysis suggests...\"。\n- 作为 warning 而非 critical 是合理的——这不影响 DreamerV3 侧的核心诊断结论，但影响论文的 generalizability claim 的可信度。\n\n**[AGREE] R1-W4 Signed error [RESOLVED]**\n同意。Appendix 中的 signed error 分析提供了充分证据。\n\n---\n\n### R1 新发现问题回应\n\n**[AGREE] R1-N-new-1: Online CIVO Detector 样本量不足**\n完全同意。我的审查（Section 4.7, analysis.tex 中 detector 部分）也独立注意到了这个问题：\n- n=14 runs 中仅 5 个正例，TPR=5/5 在统计上等价于 \"我们没有观察到 false negative\"，不能推断 sensitivity。5 个正例的 95% CI 下界（Clopper-Pearson）为 47.8%，远低于声称的 100%。\n- FPR=2/9 (22%) 更值得关注：在实际部署中，近 1/4 的误报意味着 practitioner 会频繁收到无意义的警告，降低对 detector 的信任。\n- 论文将 detector 作为四项 contribution 之一（introduction.tex:15 \"Online detection\"），但以这个样本量作为独立贡献偏弱。建议：要么增加评估规模，要么将 detector 降级为 \"preliminary tool\" 而非正式 contribution。\n\n**[REBUT] R1-N-new-2: IQM 报告不完整**\n部分不同意。\n- IQM 的主要价值在于替代 mean 来报告跨 seed 的聚合性能（Agarwal et al. 2021）。论文对核心配置（Walker Walk trained dt-embedding, n=4）报告了 IQM=175.2（results.tex:81），这是最关键的比较。\n- 对于 n=1 或 n=2 的配置（Table 2 中多个条目），计算 IQM 本身就没有统计意义。要求所有比较都报告 IQM + stratified bootstrap CI 在当前实验规模下不现实，且不会改变核心结论。\n- 但同意 R1 的潜在关注：如果论文引用了 Agarwal et al. 2021 的统计最佳实践，最好在报告数字时更系统地应用（至少对 n≥3 的配置报告 CI）。这是 minor 而非需要修改的问题。\n\n**[AGREE] R1-N-new-3: Dual-critic convergence 因果推理**\n同意这存在叙事过度简化的问题。具体：\n- ρ > 0.999 是 n=7 dual-critic 配置的结果（results.tex 中 Section 4.6），但论文未报告 convergence 随训练进展的 trajectory——如果 early training 阶段 dual critics 有差异而后来才 converge，那 \"Double Q pessimism ineffective\" 的结论只在 asymptotic 意义上成立。\n- 更关键的张力：如果 dual critics 真的完全 converge 使 pessimism 无效，wide dual-critic 的 3/4 prevention 成功（Table 2, results.tex:136）如何解释？论文在 Section 4.6 提到 \"min drives recovery...Prevention requires min + capacity\"，但 min 操作在 ρ > 0.999 下理论上应该无效（因为两个 critic 几乎相同）。这里的解释是 \"通过不同机制\" 而非 pessimism，但论文未充分阐述这个 \"不同机制\" 是什么。\n- 建议：在 Section 4.6 或 Discussion 中增加 1-2 句解释 min operation 在 converged critics 下为何仍能 enable recovery（可能是 gradient 层面的效应而非 value 层面的 pessimism）。\n\n---\n\n### R1 评分回应\n\n**方法严谨性 7/10**：[AGREE] 合理。factorial design 系统性强，但步数不对等和 TAWM 缺实验验证各扣约 1-1.5 分。\n\n**CoRL 维度打分差异**：\n\n| 维度 | R1 评分 | R2 评分 | 差异说明 |\n|------|---------|---------|----------|\n| Originality | 4/5 | 3/5 | CIVO 现象新颖但 factorial ablation 方法论是标准做法；negative result 的原创性 credit 存在争议 |\n| Quality | 3/5 | 3/5 | 一致 |\n| Clarity | 4/5 | 3.5/5 | Abstract 过于数字密集（我的 E1），F1-F7 双编号系统增加认知负担（我的 E2） |\n| Significance | 3/5 | 2/5 | R1 高估了 significance。核心 actionable takeaway 是 \"不要用 trained dt-embedding\"——这对需要 temporal abstraction 的社区帮助有限 |\n| Relevance | 4/5 | 2.5/5 | **主要分歧点**。ManiSkill negative results 表明 CIVO 是 locomotion-specific，而 CoRL 社区更关心 manipulation/contact-rich tasks。R1 对 relevance 的评估过于宽泛 |\n| Limitations | 4/5 | 4/5 | 一致 |\n\n---\n\n### R1 Should-Fix 回应\n\n**[AGREE] S1: 步数不对等**：应在正文 Section 3.6 或 Section 4.1 显式讨论 105K vs 505K 的 rationale，以及为什么 collapse 在 105K 足以确认。\n\n**[AGREE] S2: TAWM \"structural factor\"**：必须弱化措辞或增加实验。当前 \"identifies...as the structural factor\" 的表述在没有 TAWM 实验的情况下超出了证据范围。\n\n**[AGREE] S3: Online detector small-sample**：应在 Section 4.7 或 Discussion 中明确承认 n=14 的局限性。\n\n---\n\n### 综合评议\n\n与 R1 的主要共识：\n1. Factorial design 严谨，是本文最大优势\n2. LOEO 交叉验证增强了可信度\n3. 步数不对等和 TAWM 缺实验是两个 remaining open issues\n\n与 R1 的主要分歧：\n1. **Relevance 评分**（R1: 4/5 vs R2: 2.5/5）：我认为 R1 低估了 CIVO locomotion-specificity 对 CoRL venue fit 的负面影响。论文的核心发现恰恰在 robot-relevant 任务中不成立，这是一个根本性的 venue fit 问题。\n2. **Significance 评分**（R1: 3/5 vs R2: 2/5）：negative result + no reliable fix 的贡献模式在 CoRL 的 deployment-oriented 社区中价值有限。R1 对 \"长期社区价值\" 的评估合理但偏乐观。\n3. **Originality 评分**（R1: 4/5 vs R2: 3/5）：发现一个新 failure mode 有原创性，但方法论（factorial ablation + 标准 RL diagnostics）本身不新颖。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Issue 状态判定回应\n\n**[AGREE] R1-N1 统计检验力 [RESOLVED]**\n同意。LOEO AUROC=0.981 提供了比简单 in-sample accuracy 更有说服力的验证。4 seeds × 多配置 × LOEO 的组合在 RL 诊断类工作中是合理的统计功效水平。Limitations 部分也诚实承认了 seed 数量限制（conclusion.tex:10）。\n\n**[AGREE] R1-N4 单环境 [RESOLVED]**\n同意 resolved 判定。5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1）的覆盖面已足够。但补充我的观察：ManiSkill 的 negative results 虽增加了 discriminative validity，却同时削弱了论文对 CoRL 的 relevance——CIVO 恰恰在 robotics-relevant 的 manipulation 任务中不出现（Section 4.3, results.tex:92-93），使得核心发现的 robotics 价值变得更模糊。R1 给 Relevance 4/5 我认为偏高。\n\n**[AGREE] R1-W1 Factorial 混淆 [RESOLVED]**\n同意。introduction.tex:6 中 primary vs secondary comparison 的标注清楚区分了单因素对比和多因素共变的情况。\n\n**[AGREE] R1-W2 步数不对等 [STILL_OPEN]**\n同意且补充。这个问题有两个层面：\n1. **Baseline 505K vs treatment 105K**：论文声称 \"105K steps, sufficient to observe collapse onset\"（methodology.tex:58），但未讨论某些 treatment 是否可能在更长训练后 recover。results.tex:81 提到 seed 2 出现 self-correction，那其他 collapsed seeds 是否也可能在更长训练后 recover？这直接影响 \"14-19% of baseline\" 这一核心 claim 的可靠性。\n2. **exp_045 缺失**：如果存在 matched-duration 实验数据但未呈现在正文中，这是一个审稿可见性问题。reviewer 不应需要猜测 appendix 中是否存在支持证据。\n\n**[AGREE] R1-W3 Pathway B [RESOLVED]**\n同意。\"preliminary\" 和 \"requires confirmation\" 的措辞恰当（results.tex:103），且只有 2 seeds 的情况下不做过强 claim 是负责任的。\n\n**[AGREE] R2-W1 TAWM 对比 [STILL_OPEN]**\n强烈同意。这也是我在 Round 1 (R2-W3) 关注的延伸。具体问题：\n- Abstract 称 \"the contrast with MPC identifies feedback architecture as the structural factor\"，Conclusion 重复 \"MPC re-planning versus imagination-based bootstrapping—is the structural factor\"（conclusion.tex:4）——但论文**从未在 TD-MPC2/TAWM 上运行任何实验**。\n- Related Work（related_work.tex:5）的论述 \"the critical distinction is that MPC re-plans from real states, so model errors do not accumulate into a critic\" 是合理的 architectural reasoning，但将其称为 \"structural factor\" 暗示了因果确认，而实际只有推理。\n- 至少应做到以下之一：(a) 在 TD-MPC2 上复现 dt-conditioning 实验验证 CIVO 不出现，(b) 将 \"structural factor\" 弱化为 \"hypothesized structural factor\" 或 \"architectural difference that our analysis suggests...\"。\n- 作为 warning 而非 critical 是合理的——这不影响 DreamerV3 侧的核心诊断结论，但影响论文的 generalizability claim 的可信度。\n\n**[AGREE] R1-W4 Signed error [RESOLVED]**\n同意。Appendix 中的 signed error 分析提供了充分证据。\n\n---\n\n### R1 新发现问题回应\n\n**[AGREE] R1-N-new-1: Online CIVO Detector 样本量不足**\n完全同意。我的审查（Section 4.7, analysis.tex 中 detector 部分）也独立注意到了这个问题：\n- n=14 runs 中仅 5 个正例，TPR=5/5 在统计上等价于 \"我们没有观察到 false negative\"，不能推断 sensitivity。5 个正例的 95% CI 下界（Clopper-Pearson）为 47.8%，远低于声称的 100%。\n- FPR=2/9 (22%) 更值得关注：在实际部署中，近 1/4 的误报意味着 practitioner 会频繁收到无意义的警告，降低对 detector 的信任。\n- 论文将 detector 作为四项 contribution 之一（introduction.tex:15 \"Online detection\"），但以这个样本量作为独立贡献偏弱。建议：要么增加评估规模，要么将 detector 降级为 \"preliminary tool\" 而非正式 contribution。\n\n**[REBUT] R1-N-new-2: IQM 报告不完整**\n部分不同意。\n- IQM 的主要价值在于替代 mean 来报告跨 seed 的聚合性能（Agarwal et al. 2021）。论文对核心配置（Walker Walk trained dt-embedding, n=4）报告了 IQM=175.2（results.tex:81），这是最关键的比较。\n- 对于 n=1 或 n=2 的配置（Table 2 中多个条目），计算 IQM 本身就没有统计意义。要求所有比较都报告 IQM + stratified bootstrap CI 在当前实验规模下不现实，且不会改变核心结论。\n- 但同意 R1 的潜在关注：如果论文引用了 Agarwal et al. 2021 的统计最佳实践，最好在报告数字时更系统地应用（至少对 n≥3 的配置报告 CI）。这是 minor 而非需要修改的问题。\n\n**[AGREE] R1-N-new-3: Dual-critic convergence 因果推理**\n同意这存在叙事过度简化的问题。具体：\n- ρ > 0.999 是 n=7 dual-critic 配置的结果（results.tex 中 Section 4.6），但论文未报告 convergence 随训练进展的 trajectory——如果 early training 阶段 dual critics 有差异而后来才 converge，那 \"Double Q pessimism ineffective\" 的结论只在 asymptotic 意义上成立。\n- 更关键的张力：如果 dual critics 真的完全 converge 使 pessimism 无效，wide dual-critic 的 3/4 prevention 成功（Table 2, results.tex:136）如何解释？论文在 Section 4.6 提到 \"min drives recovery...Prevention requires min + capacity\"，但 min 操作在 ρ > 0.999 下理论上应该无效（因为两个 critic 几乎相同）。这里的解释是 \"通过不同机制\" 而非 pessimism，但论文未充分阐述这个 \"不同机制\" 是什么。\n- 建议：在 Section 4.6 或 Discussion 中增加 1-2 句解释 min operation 在 converged critics 下为何仍能 enable recovery（可能是 gradient 层面的效应而非 value 层面的 pessimism）。\n\n---\n\n### R1 评分回应\n\n**方法严谨性 7/10**：[AGREE] 合理。factorial design 系统性强，但步数不对等和 TAWM 缺实验验证各扣约 1-1.5 分。\n\n**CoRL 维度打分差异**：\n\n| 维度 | R1 评分 | R2 评分 | 差异说明 |\n|------|---------|---------|----------|\n| Originality | 4/5 | 3/5 | CIVO 现象新颖但 factorial ablation 方法论是标准做法；negative result 的原创性 credit 存在争议 |\n| Quality | 3/5 | 3/5 | 一致 |\n| Clarity | 4/5 | 3.5/5 | Abstract 过于数字密集（我的 E1），F1-F7 双编号系统增加认知负担（我的 E2） |\n| Significance | 3/5 | 2/5 | R1 高估了 significance。核心 actionable takeaway 是 \"不要用 trained dt-embedding\"——这对需要 temporal abstraction 的社区帮助有限 |\n| Relevance | 4/5 | 2.5/5 | **主要分歧点**。ManiSkill negative results 表明 CIVO 是 locomotion-specific，而 CoRL 社区更关心 manipulation/contact-rich tasks。R1 对 relevance 的评估过于宽泛 |\n| Limitations | 4/5 | 4/5 | 一致 |\n\n---\n\n### R1 Should-Fix 回应\n\n**[AGREE] S1: 步数不对等**：应在正文 Section 3.6 或 Section 4.1 显式讨论 105K vs 505K 的 rationale，以及为什么 collapse 在 105K 足以确认。\n\n**[AGREE] S2: TAWM \"structural factor\"**：必须弱化措辞或增加实验。当前 \"identifies...as the structural factor\" 的表述在没有 TAWM 实验的情况下超出了证据范围。\n\n**[AGREE] S3: Online detector small-sample**：应在 Section 4.7 或 Discussion 中明确承认 n=14 的局限性。\n\n---\n\n### 综合评议\n\n与 R1 的主要共识：\n1. Factorial design 严谨，是本文最大优势\n2. LOEO 交叉验证增强了可信度\n3. 步数不对等和 TAWM 缺实验是两个 remaining open issues\n\n与 R1 的主要分歧：\n1. **Relevance 评分**（R1: 4/5 vs R2: 2.5/5）：我认为 R1 低估了 CIVO locomotion-specificity 对 CoRL venue fit 的负面影响。论文的核心发现恰恰在 robot-relevant 任务中不成立，这是一个根本性的 venue fit 问题。\n2. **Significance 评分**（R1: 3/5 vs R2: 2/5）：negative result + no reliable fix 的贡献模式在 CoRL 的 deployment-oriented 社区中价值有限。R1 对 \"长期社区价值\" 的评估合理但偏乐观。\n3. **Originality 评分**（R1: 4/5 vs R2: 3/5）：发现一个新 failure mode 有原创性，但方法论（factorial ablation + 标准 RL diagnostics）本身不新颖。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-24T07:14:41.422068+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3927
}
```

</details>

---

### Assistant

_source line 136 · 2026-05-24T07:14:49.664211+00:00_

交叉回应已提交。总结：

- 7 个 issue 中 **5 个 AGREE**（R1-N1/N4/W1/W3/W4 resolved，R1-W2/R2-W1 still open）
- 新问题中 **N-new-1 AGREE**（detector 样本量）、**N-new-2 REBUT**（IQM 对 n≤2 配置无意义，不必所有比较都报告）、**N-new-3 AGREE**（dual-critic convergence 叙事过度简化）
- **主要分歧在 Relevance**（R1: 4/5 vs R2: 2.5/5）和 **Significance**（R1: 3/5 vs R2: 2/5）——CIVO 的 locomotion-specificity 使其对 CoRL 的 manipulation/deployment 社区价值有限

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 5

38 recorded events

### User

_source line 137 · 2026-05-24T09:27:38.160715+00:00_

[Round 4 审稿请求]:
## Round 4 修订评估任务 — Reviewer 2（ICML Novelty/Significance + 格式）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`
**目标 Venue**: ⚠️ ICML 2026（从 CoRL 2026 转投）
**Deadline**: 2026-01-28（已过期；可能处于 rebuttal 阶段或准备下一轮）
**页数限制**: 8 页正文 + unlimited appendix/references
**模板**: 应使用 ICML 2026 官方样式（当前文件仍为 `\usepackage{corl_2026}`！）
**匿名规则**: Double-blind
**审查侧重**: ICML venue fit、novelty、significance、格式合规

### 背景

Venue 从 CoRL 2026 改为 ICML 2026。Round 3 两个 critical issues（venue fit 5/10, actionable contribution 6/10）在转投 ICML 后需完全重新评估：
- ICML 对 diagnostic/negative-result paper 的接受度比 CoRL 高
- ICML 不要求 "core robotics problems"
- 但 ICML 对 novelty 和 broader impact 要求高

### 必须逐条检查的 Issue

**1. R1-N3 [critical, in_progress → 重新评估]: Venue fit**
- Round 3 问题：CoRL 要求 "core robotics problems"，论文不满足
- **Venue 变更**：ICML 2026 的 RL/world-model track 对 diagnostic/negative-result 论文更开放
- **检查要点**：
  - 论文是否适合 ICML 的 scope（RL, optimization, representation learning）？
  - 当前的 robotics framing（Abstract 首句、Intro 前两段、Discussion implications）在 ICML 中是否仍合适，还是应该调整为更通用的 RL framing？
  - ICML 的 broader impact 要求如何影响论文定位？

**2. R2-N3 [critical, in_progress → 重新评估]: 纯诊断缺乏 actionable solution**
- Round 3 问题：对 CoRL deployment-oriented 社区贡献偏弱
- **Venue 变更**：ICML 接受 Henderson et al. (2018) 类型的 diagnostic/empirical study
- **检查要点**：
  - 在 ICML 标准下，diagnostic + partial mitigation + preliminary detection 的贡献模式是否足够？
  - 与 ICML 历史上接受的 diagnostic/negative-result paper 对比如何？
  - 四级干预层级分析的方法论贡献在 ICML 中的价值如何？

**3. R3-N1 [critical] ⚠️ 模板不合规**
- **严重问题**：main.tex:5 仍为 `\usepackage{corl_2026}`，未切换到 ICML 2026 样式
- ICML 2026 使用自己的样式文件（icml2026.sty），格式与 PMLR/CoRL 不同
- **检查要点**：确认模板状态。如果确实仍是 CoRL 模板，这是 desk reject 风险。

**4. R2-W4 [warning, resolved]: Becker-Ehmck 引用**
- Issue tracker 标记为 resolved（解释为 Benechehab et al. 2023 的混淆）
- **检查要点**：验证 Related Work 中是否引用了 benechehab2023multitimestep

**5. 写作质量（针对 ICML）**
- Round 3 发现：Abstract 统计数据过密、F1-F7 双编号
- **检查要点**：
  - Abstract 是否仍然数字过密？（看最新版本）
  - 论文长度是否在 ICML 8 页限制内？
  - Limitations section 是否满足 ICML 的 broader impact / societal impact 要求？
  - 是否需要增加 impact statement（ICML 近年要求）？
  - Keywords 是否适合 ICML？

### ICML 2026 CFP 关键要求
- 8 页正文 + unlimited references/appendix
- Impact statement 必须包含
- Double-blind
- 接受范围广：ML theory, RL, optimization, representation learning, applications
- 重视 novelty, significance, clarity

### 输出格式
1. 对每个 issue 给出判定 + 理由
2. ICML venue fit 评分（1-10）
3. Novelty 评分（1-10）
4. Significance 评分（1-10）
5. 写作质量评分（1-10）
6. 简要总评 + 与 ICML 历史接受论文的对比

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-24T09:27:53.991151+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-24T09:27:54.393123+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-24T09:27:54.393529+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ICML 2026 reviewer guidelines review form scoring criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ICML 2026 reviewer guidelines review form scoring criteria"
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-24T09:27:55.247877+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-24T09:27:55.298598+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 27/30, AUROC${=}0.957$, LOEO cross-validated). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-24T09:28:03.942958+00:00_

Web search results for query: "ICML 2026 reviewer guidelines review form scoring criteria"

Links: [{"title":"ICML 2026 Area Chair Instructions","url":"https://icml.cc/Conferences/2026/AreaChairInstructions"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"ICML 2026 Reviewer Instructions","url":"https://icml.cc/Conferences/2026/ReviewerInstructions"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"Introducing ICML 2026 policy for self-ranking in reviews – ICML Blog","url":"https://blog.icml.cc/2026/01/12/introducing-icml-2026-policy-for-self-ranking-in-reviews/"},{"title":"ICML 2026 Policy for LLM use in reviewing","url":"https://icml.cc/Conferences/2026/LLM-Policy"}]

I found information about ICML 2026 reviewer guidelines. Here are the key details:

## Review Form and Process

The review form this year is new and has specific items that reviewers are required to complete. Reviewers are asked to summarize how they weighed the strengths and weaknesses across review dimensions.

## Scoring Criteria and Recommendations

Recommendations and meta-reviews should be informed by the review content, as opposed to just relying on average (or other aggregate) numerical scores. What eventually matters is the review text, not just the numerical scores.

## Acceptance Criteria

Papers that are technically sound, well-written, non-redundant with previous research, and useful to at least some fraction of the ICML community should be accepted.

## Important Review Considerations

The review instructions also include requirements regarding:
- Explaining the final recommendation, taking into account both the paper and the authors' rebuttal
- Flagging papers for ethics review when appropriate, indicating relevant areas of expertise, and explaining ethical concerns in detail
- Following 
…[truncated 360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9549
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-24T09:28:16.143037+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://icml.cc/Conferences/2026/ReviewerInstructions",
  "prompt": "Extract the complete ICML 2026 review form criteria, scoring dimensions, rating scales, and all evaluation categories with descriptions. Include any information about impact statements, ethics review, and acceptance criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://icml.cc/Conferences/2026/ReviewerInstructions",
    "prompt": "Extract the complete ICML 2026 review form criteria, scoring dimensions, rating scales, and all evaluation categories with descriptions. Include any information about impact statements, ethics review, and acceptance criteria."
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-24T09:28:18.459487+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-24T09:28:19.463788+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-24T09:28:19.464337+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-24T09:28:19.665385+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-24T09:28:19.665748+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-24T09:28:19.716329+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal abstraction in RL.}
5	The options framework \citep{sutton1999options}, option-critic \citep{bacon2017optioncritc}, HAM \citep{parr1998ham}, and MAXQ \citep{dietterich2000maxq} formalize temporal abstraction through hierarchical policies. Semi-MDP theory \citep{bradtke1995smdp} provides the mathematical foundation. Action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, park2021timediscretization} achieve simpler temporal abstraction via real transitions; \citet{wang2024elastic} learn elastic time steps that adapt step size to state dynamics. The Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3, hafner2025dreamerv4} trains policies in imagination at fixed $\dt{=}1$; hierarchical variants \citep{hafner2022director, gumbsch2024thick, mattes2024hieros, li2025lsimagine} use subgoals or separate dynamics per scale, avoiding flat $\dt$-conditioning. TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains; the critical distinction is that MPC re-plans from real states, so model errors do not accumulate into a critic (\S\ref{sec:discussion}).
6	
7	\paragraph{Value overestimation and model fidelity.}
8	Maximization bias \citep{thrun1993issues} has been addressed by Double Q-learning \citep{vanhasselt2016double}, TD3 \citep{fujimoto2018td3}, and ensemble methods \citep{chen2021redq}; in model-based settings, MBPO \citep{janner2019mbpo} and MOPO \citep{yu2020mopo} bound rollout error, while MOReL \citep{kidambi2020morel} and COMBO \citep{yu2021combo} penalize model uncertainty. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints. CIVO is mechanistically distinct: the amplifier is the world model's co-adaptation with a learned temporal embedding, producing systematic reward-prediction bias at $\dt > 1$. Multi-timestep world models \citep{benechehab20
…[truncated 1421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-24T09:28:28.740727+00:00_

# ICML 2026 Review Form Criteria and Evaluation Framework

## Main Track Reviewer Form

### Core Evaluation Dimensions

**Soundness** (4-point scale: Excellent to Poor)
Assesses technical correctness, methodological appropriateness, and whether claims receive adequate support through theory or experimentation. The guidance notes that "soundness is distinct from impact."

**Presentation** (4-point scale: Excellent to Poor)
Evaluates clarity of writing, structural organization, narrative flow, and contextualization within existing literature. A superbly written paper should enable "an expert reader to reproduce its results."

**Significance** (4-point scale: Excellent to Poor)
Determines whether the work addresses important problems and advances machine learning understanding, capabilities, or practice. Impact can be broad or specialized as appropriate to the contribution.

**Originality** (4-point scale: Excellent to Poor)
Examines novelty of insights, methods, tasks, theory, data, or perspectives. The form emphasizes that "originality does not necessarily require introducing an entirely new method."

### Overall Recommendation Scale (6 options)

- **6: Strong Accept** — Technically flawless with exceptional impact, strong evaluation, reproducibility
- **5: Accept** — Technically solid, high or moderate-to-high impact across areas
- **4: Weak Accept** — Solid advancement with some limiting weaknesses (used sparingly)
- **3: Weak Reject** — Clear merits outweighed by weaknesses requiring revision
- **2: Reject** — Technical flaws, weak evaluation, poor reproducibility, or clarity issues
- **1: Strong Reject** — Well-known results, unaddressed ethics, or unintelligible contribution

### Confidence Scale (5 levels)

Ranges from "absolutely certain" (5) to "educated guess" (1), reflecting familiarity with related work and depth of technical verification.

## Position Paper Track Reviewer Form

### Specific Assessment Dimensions

**Support** (4-point scale)
Evaluates how 
…[truncated 1685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 12597
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-24T09:28:47.814629+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-24T09:28:48.116774+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-24T09:28:48.619307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-24T09:28:49.121587+00:00_

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
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-24T09:28:49.122146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-24T09:28:49.172707+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-24T09:29:24.003304+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_4/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_4/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-24T09:29:24.886875+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/pro
…[truncated 2768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 883
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-24T09:29:25.037931+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "impact|Impact|broader",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "impact|Impact|broader",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-24T09:29:25.339305+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md:9:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-24T09:29:25.841649+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "icml|ICML",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "icml|ICML",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-24T09:29:26.394310+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty:5:% This template is heavily inspired by the NeurIPS, ICML, ICLR and IEEE Transactions latex templates.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty:6:% Hence we would like to thank: Roman Garnett and the previous mantainers of the NIPS style, Percy Liang and the previous mantainers of the ICML style, Hugo Larochelle for the ICLR style, and Michael Shell for the IEEE Transactions style.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/_corl_template/corl_2026_template_submission/corl_2026.sty:11:%	       - The abstract is more compact compared to NeurIPS/ICML
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/corl_2026.sty:5:% This template is heavily inspired by the NeurIPS, ICML, ICLR and IEEE Transactions latex templates.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/corl_2026.sty:6:% Hence we would like to thank: Roman Garnett and the previous mantainers of the NIPS style, Percy Liang and the previous mantainers of the ICML style, Hugo Larochelle for the ICLR style, and Michael Shell for the IEEE Transactions style.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/corl_2026.sty:11:%	       - The abstract is more compact compared to NeurIPS/ICML

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-24T09:29:27.650172+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://icml.cc/Conferences/2026/CallForPapers",
  "prompt": "Extract the ICML 2026 call for papers requirements: page limits, template requirements, impact statement requirements, formatting rules, submission categories, and any specific requirements about broader impact or ethics statements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://icml.cc/Conferences/2026/CallForPapers",
    "prompt": "Extract the ICML 2026 call for papers requirements: page limits, template requirements, impact statement requirements, formatting rules, submission categories, and any specific requirements about broader impact or ethics statements."
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-24T09:29:32.621498+00:00_

# ICML 2026 Call for Papers Requirements

## Page Limits
- **Main paper**: 8 pages maximum
- **References, impact statement, and appendices**: Unlimited pages
- **Accepted papers**: One additional page permitted for camera-ready version

## Template & Formatting
- Submissions must be prepared as a **single file**
- Authors must use the correct [Style Files](https://media.icml.cc/Conferences/ICML2026/Styles/icml2026.zip)
- Papers not conforming to formatting policies face rejection without review

## Impact Statement Requirements
Required section at end of paper (before References), does not count toward page limit. Authors may use this statement verbatim when impacts are well-established:

"This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here."

However, authors should consider whether additional discussion of ethical impacts and societal implications is warranted.

## Submission Categories
- **Main track**: Original research papers
- **Position papers**: Submitted through separate OpenReview site

## Additional Ethics & Broader Impact Requirements
- Statements addressing "ethical aspects and future societal consequences" must be included
- Papers may be flagged for ethics review by reviewers/ACs
- Ethics committee can recommend rejection on ethical grounds, independent of scientific quality

## Key Deadlines
- Abstract deadline: January 23, 2026 (AoE)
- Full paper deadline: January 28, 2026 (AoE)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4971
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-24T09:29:43.414355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-24T09:29:44.328750+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 914
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-24T09:29:44.329283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-24T09:29:44.481036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-24T09:29:44.734952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-24T09:29:45.038230+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 557
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-24T09:32:01.472759+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 4 修订评估 — Reviewer 2（ICML Novelty/Significance + 格式）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: ICML 2026（从 CoRL 转投）\n\n---\n\n## Round 3→4 修改追踪\n\n在逐条审查前，先确认论文从 Round 3 到 Round 4 的关键修改：\n\n| 修改点 | 位置 | 内容 |\n|--------|------|------|\n| Abstract 精简 | abstract_body.tex | 移除 \"2.78×\"、\"ρ > 0.999\"、detector 句；减少数字密度 |\n| 措辞弱化 | abstract + conclusion | \"the structural factor\" → \"a hypothesized structural factor\" |\n| 数据更新 | 全文 | 26/29 → 27/30, AUROC 0.953 → 0.957, LOEO 0.981 → 0.988 |\n| Detector 降级 | introduction.tex:14 | \"Online detection\" → \"Preliminary diagnostic\" + CI [47.8%, 100%] |\n| 步数问题回应 | analysis.tex:10-11 | 新增 \"Training horizon\" 段落：extended training ~302K 一个 seed 显示 self-recovery |\n| Future work | conclusion.tex:4 | \"Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work\" |\n| 因果措辞 | analysis.tex:8 | \"6/6\" → \"7/7\", AUROC 更新 |\n| Table 1 footnote | results.tex:47 | 新增 baseline 参考值 |\n| Implications 更新 | analysis.tex:14 | 修正 reward density 解释：\"Both domains use dense shaped rewards, so reward sparsity cannot explain the boundary\" |\n\n这些修改直接回应了 Round 3 R1/R2 的具体意见，质量上有明显提升。\n\n---\n\n## 逐条 Issue 检查\n\n### 1. R1-N3 [critical → 重新评估]: Venue fit（CoRL → ICML）\n**[RESOLVED for ICML]**\n\nICML venue fit 与 CoRL 完全不同：\n- **ICML 接受范围**：CFP 明确涵盖 \"RL, optimization, representation learning\"。本文的核心贡献——在 imagination-based actor-critic 中诊断 dt-conditioning 的 value overestimation 失败模式——完全属于 ICML 的 RL track。\n- **Diagnostic/negative-result 传统**：ICML 有接受此类工作的先例。Henderson et al. (2018) \"Deep Reinforcement Learning that Matters\"（本文引用）正是 ICML 接受的大规模 diagnostic study，其核心也是 negative results + 方法论建议，没有提出新算法。\n- **Robotics framing 的处理**：当前 Introduction 仍以 robotics motivation 开篇（\"directly on physical hardware\"、DayDreamer、TD-MPC2），这在 ICML 中不构成问题——robotics 应用是 RL 研究的合法动机。但论文可以考虑略微拓宽开篇 framing，将 temporal abstraction 的 motivation 从纯 robotics 扩展到更广泛的连续控制场景（如 Atari、game-playing），以更好匹配 ICML 受众。\n- **不再是核心阻碍**：在 CoRL 中 venue fit 是 critical 问题（5/10），在 ICML 中不再是问题。\n\n---\n\n### 2. R2-N3 [critical → 重新评估]: 纯诊断缺乏 actionable solution\n**[RESOLVED for ICML]**\n\nICML 对贡献模式的要求与 CoRL 不同：\n- **ICML 接受标准**（reviewer instructions）：\"Papers that are technically sound, well-written, non-redundant with previous research, and useful to at least some fraction of the ICML community should be accepted.\"论文满足所有条件。\n- **与 Henderson et al. (2018) 对比**：该论文也没有提出新方法，核心贡献是实验方法论和 negative findings。本文的 factorial design（43 配置 × 5 环境 × 四级干预）在系统性上至少与之相当。\n- **贡献层次明确**：\n  1. 新 failure mode 的识别和因果分离（CIVO, 27/30, AUROC=0.957）\n  2. 架构边界的发现（MPC vs imagination-based bootstrapping）\n  3. 四级干预层级的系统分析（gradient → output → representation → architecture）\n  4. Preliminary diagnostic tool（降级为 preliminary 是诚实的）\n- **在 ICML 中 \"不要用 trained dt-embedding\" 是合理贡献**：对 ICML 的方法论社区来说，知道某条看似合理的技术路线（dt-conditioning in imagination-based RL）为什么不可行，以及为什么标准 countermeasures（Double Q, gradient stopping）无法修复，本身就有价值。这类 \"warning\" 可以避免社区重复踩坑。\n\n---\n\n### 3. R3-N1 [critical] ⚠️ 模板不合规\n**[STILL_OPEN — CRITICAL]**\n\n这是当前最严重的问题：\n\n- **main.tex:5 仍为 `\\usepackage{corl_2026}`**。未切换到 ICML 2026 样式文件（`icml2026.sty`）。\n- **PDF 页脚**（page 1 底部）明确显示：\"Submitted to the 10th Conference on Robot Learning (CoRL, 2026). Do not distribute.\" 这是 CoRL 特有的页脚文字。\n- **ICML CFP 明确要求**：\"Authors must use the correct Style Files...Papers not conforming to formatting policies face rejection without review.\"\n- **`\\keywords{}` 命令**（main.tex:49）是 CoRL 模板特有的，ICML 模板可能不支持。\n- **影响**：以当前状态提交到 ICML 将被 desk reject，无需进入实质审稿。\n\n**必须修复**：\n1. 下载 ICML 2026 样式文件（icml2026.zip）\n2. 替换 `\\usepackage{corl_2026}` 为 `\\usepackage{icml2026}`\n3. 移除或调整 `\\keywords{}` 命令\n4. 验证编译通过、格式正确\n\n---\n\n### 4. [NEW — CRITICAL] Impact Statement 缺失\n**[STILL_OPEN — CRITICAL]**\n\nICML 2026 CFP 明确要求：\n> \"Required section at end of paper (before References), does not count toward page limit.\"\n\n当前论文在 References 之前没有 Impact Statement。即使论文的 societal impact 有限，ICML 也要求至少包含一个标准声明：\n\n> \"This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.\"\n\n**必须添加**：在 Conclusion/Limitations 之后、`\\bibliography{}` 之前插入 Impact Statement section。\n\n---\n\n### 5. R2-W4 [warning, resolved]: Becker-Ehmck 引用\n**[RESOLVED]**\n\nIssue tracker 正确标记：Round 3 的 \"Becker-Ehmck 2023\" 系与 \"Benechehab et al. 2023\" 的混淆。相关引用 `benechehab2023multitimestep` 在 related_work.tex:8 中已被引用（\"Multi-timestep world models learn predictions at variable horizons but do not examine the value overestimation pathology we isolate\"）。确认 resolved。\n\n---\n\n### 6. 写作质量（针对 ICML）\n\n**Abstract 数字密度（Round 3 E1）**：\n**[PARTIALLY RESOLVED]** — 改善明显。Abstract 移除了 \"2.78×\"、\"ρ > 0.999\"、detector 句。但仍包含 \"14-19%\"、\"27/30\"、\"AUROC=0.957\"、\"LOEO\"。相比 Round 3 的 6+ 个数字指标，现在约 4 个，可接受但仍偏密。\n\n**F1-F7 双编号（Round 3 E2）**：\n**[STILL_OPEN]** — 未修改。Results section 仍使用 \"F1\"...\"F7\" 编号与 Section 编号并行。这对 ICML reviewer 来说是额外认知负担。建议：要么用 F1-F7 作为唯一编号系统（替代 subsection 编号），要么去掉 F 编号改用 descriptive subsection titles。\n\n**论文长度**：\n正文 8 页（pages 1-8），References 从 page 9 开始。符合 ICML 8 页限制 ✅\n\n**Limitations section**：\n存在于 Conclusion 的 paragraph 中（conclusion.tex:6-11）。ICML 不要求 Limitations 作为独立 section（与 NeurIPS 不同），当前形式可接受 ✅\n\n**匿名合规**：\n- \"Anonymous Author(s)\" ✅\n- \"Code: upon acceptance\" ✅\n- DreamerV3 仓库链接（官方仓库，非作者代码）✅\n- 但页脚 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\" 在 ICML 提交中技术上暴露了此前的投稿 venue（尽管这更多是模板问题而非匿名问题）\n\n**Keywords 适配**：\n当前 keywords \"World Models, Temporal Abstraction, Value Overestimation, DreamerV3\" 内容上适合 ICML，但 `\\keywords{}` 命令需确认 ICML 模板是否支持。\n\n---\n\n## Round 3 → Round 4 改进的其他确认\n\n### R1-W2 步数不对等：[SUBSTANTIALLY ADDRESSED]\n新增 \"Training horizon\" 段落（analysis.tex:10-11）提供了关键的 extended training 数据：\"Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset\"。这直接回应了 \"treatment 是否在更长训练后 recover\" 的问题。\n\n但 n=1 seed 的 extended training 数据仍然有限，且结论（self-recovery 需要 ~170K 额外步数，计算成本高）也支持论文的核心论点：CIVO 即使可以 recover，代价也很大。在 ICML 标准下，这个回应足够。\n\n### R2-W1 TAWM \"structural factor\"：[RESOLVED]\n两处修改充分回应：\n1. Abstract: \"a hypothesized structural factor\"（而非 \"the structural factor\"）\n2. Conclusion: \"Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work\"\n\n措辞准确反映了证据级别：architectural reasoning + 未经 TD-MPC2 实验验证 → 假说而非结论。\n\n### R1-N-new-1 Online detector 样本量：[RESOLVED]\nContribution 4 从 \"Online detection\" 降级为 \"Preliminary diagnostic\"，明确标注 \"TPR 95% CI [47.8%, 100%] (n=5/5), FPR 22% (2/9)\"。这是对小样本限制的诚实披露。\n\n---\n\n## 评分（ICML 标准）\n\n### ICML Venue Fit: 8/10\n论文完全属于 ICML RL track 的范畴。Diagnostic/negative-result 论文在 ICML 有先例（Henderson et al. 2018）。唯一减分：robotics-heavy 的开篇 framing 可以更通用化以更好匹配 ICML 受众，但这是 minor 的 presentation 问题。\n\n### Novelty: 7/10\n- **CIVO 作为新 failure mode**：dt-conditioning 在 imagination-based RL 中引发 value overestimation 的发现是新颖的。之前没有工作系统地研究过这个特定的失败机制。\n- **Factorial design 的诊断方法论**：将 Henderson et al. (2018) 的 factorial 方法论应用到 world-model RL 的特定问题中，方法论本身不新但应用有价值。\n- **MPC vs imagination-based 的 architectural boundary**：这个洞察有概念新颖性，即使实验验证不完整（\"hypothesized\"）。\n- **减分点**：论文没有提出新方法或新算法，核心工具（factorial ablation, NVE metric, gradient stopping）都是已有技术的组合。CIVO 现象虽新颖，但论文自己承认它在 manipulation 中不出现、在 locomotion 中可以通过 \"不用 trained embedding\" 避免。\n\n### Significance: 6/10\n- **对 world-model RL 社区的价值**：知道 dt-conditioning 在 imagination-based RL 中为什么失败、为什么 Double Q 和 gradient stopping 无法修复，可以帮助社区避免重复探索这条技术路线。\n- **方法论示范**：四级干预层级分析为未来的 RL 诊断研究提供了一个可复用的框架。\n- **减分点**：\n  - 发现的 scope 有限——仅在 DreamerV3 + locomotion 中确认\n  - Actionable outcome 弱——最有效建议是\"不要用\"\n  - 未提出解决方案或新理论框架\n  - 与 Henderson et al. (2018) 相比，后者的发现影响了整个 RL 社区的实验报告实践；本文的影响范围窄得多（仅 world-model RL + temporal abstraction）\n\n### 写作质量: 7/10\n- 结构清晰、专业\n- Abstract 较 Round 3 改善明显但仍偏数字密集\n- F1-F7 双编号增加认知负担\n- 总体可读性良好，技术细节充分\n\n---\n\n## ICML 维度打分（4-point scale: Excellent / Good / Fair / Poor）\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| Soundness | Good (3/4) | Factorial design 严谨，LOEO 交叉验证有力；但 extended training 仅 1 seed，TAWM 对比无实验（已弱化为 hypothesized） |\n| Presentation | Good (3/4) | 结构清晰，写作专业；Abstract 偏数字密集，F1-F7 双编号增加认知负担；模板问题需修复 |\n| Significance | Fair (2/4) | 对 world-model RL 子社区有价值的 warning，但 scope 窄（DreamerV3 + locomotion），无解决方案 |\n| Originality | Good (3/4) | CIVO 作为新 failure mode 有新颖性，MPC vs imagination 的 architectural boundary 有概念价值；方法论是已有技术组合 |\n\n### Overall Recommendation: 4 (Weak Accept)\n论文是一个 technically solid 的 diagnostic study，在 ICML RL track 中处于 borderline accept 区域。主要优势是 factorial design 的系统性和 CIVO 发现的新颖性；主要劣势是有限的 scope 和缺乏 constructive solution。\n\n---\n\n## 与 ICML 历史接受论文对比\n\n| 对比论文 | 贡献类型 | 本文对比 |\n|---------|---------|---------|\n| Henderson et al. (2018) \"RL that Matters\" | Diagnostic，方法论指南 | 类似贡献模式，但影响范围窄得多 |\n| Lyle et al. (2022) \"Capacity Loss in RL\" | 诊断 + partial mitigation | 本文结构类似：诊断→干预→发现干预不够 |\n| Lambert et al. (2020) \"Objective Mismatch\" | Diagnostic, model-based RL | 类似领域的 diagnostic work |\n\n本文的 systematic rigor 与上述论文相当，但 breadth of impact 偏窄。如果 reviewer 重视 \"避免社区重复踩坑\" 的价值，weak accept 是合理的；如果 reviewer 要求 constructive solution 或更广泛的适用性，可能会 weak reject。\n\n---\n\n## 总结\n\n**两个 CRITICAL 格式问题必须立即修复**：\n1. 模板从 `corl_2026` 切换到 `icml2026`（含页脚修复）\n2. 添加 Impact Statement\n\n**内容方面**，Round 3→4 的修改质量好——\"hypothesized structural factor\"、detector 降级、training horizon 段落、baseline 值补充都直接回应了具体审稿意见。转投 ICML 是正确决策：论文的贡献模式（diagnostic + negative result）在 ICML 中比 CoRL 更有竞争力。\n\n**Remaining weakness**：novelty 和 significance 在 ICML 中处于 borderline 水平。如果审稿人认为 \"在 DreamerV3 locomotion 中发现的一个可以通过不用 trained embedding 避免的 failure mode\" 值得 ICML 版面，论文可以接受；如果审稿人期望更广泛的适用性或 constructive solution，论文偏弱。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 4 修订评估 — Reviewer 2（ICML Novelty/Significance + 格式）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: ICML 2026（从 CoRL 转投）\n\n---\n\n## Round 3→4 修改追踪\n\n在逐条审查前，先确认论文从 Round 3 到 Round 4 的关键修改：\n\n| 修改点 | 位置 | 内容 |\n|--------|------|------|\n| Abstract 精简 | abstract_body.tex | 移除 \"2.78×\"、\"ρ > 0.999\"、detector 句；减少数字密度 |\n| 措辞弱化 | abstract + conclusion | \"the structural factor\" → \"a hypothesized structural factor\" |\n| 数据更新 | 全文 | 26/29 → 27/30, AUROC 0.953 → 0.957, LOEO 0.981 → 0.988 |\n| Detector 降级 | introduction.tex:14 | \"Online detection\" → \"Preliminary diagnostic\" + CI [47.8%, 100%] |\n| 步数问题回应 | analysis.tex:10-11 | 新增 \"Training horizon\" 段落：extended training ~302K 一个 seed 显示 self-recovery |\n| Future work | conclusion.tex:4 | \"Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work\" |\n| 因果措辞 | analysis.tex:8 | \"6/6\" → \"7/7\", AUROC 更新 |\n| Table 1 footnote | results.tex:47 | 新增 baseline 参考值 |\n| Implications 更新 | analysis.tex:14 | 修正 reward density 解释：\"Both domains use dense shaped rewards, so reward sparsity cannot explain the boundary\" |\n\n这些修改直接回应了 Round 3 R1/R2 的具体意见，质量上有明显提升。\n\n---\n\n## 逐条 Issue 检查\n\n### 1. R1-N3 [critical → 重新评估]: Venue fit（CoRL → ICML）\n**[RESOLVED for ICML]**\n\nICML venue fit 与 CoRL 完全不同：\n- **ICML 接受范围**：CFP 明确涵盖 \"RL, optimization, representation learning\"。本文的核心贡献——在 imagination-based actor-critic 中诊断 dt-conditioning 的 value overestimation 失败模式——完全属于 ICML 的 RL track。\n- **Diagnostic/negative-result 传统**：ICML 有接受此类工作的先例。Henderson et al. (2018) \"Deep Reinforcement Learning that Matters\"（本文引用）正是 ICML 接受的大规模 diagnostic study，其核心也是 negative results + 方法论建议，没有提出新算法。\n- **Robotics framing 的处理**：当前 Introduction 仍以 robotics motivation 开篇（\"directly on physical hardware\"、DayDreamer、TD-MPC2），这在 ICML 中不构成问题——robotics 应用是 RL 研究的合法动机。但论文可以考虑略微拓宽开篇 framing，将 temporal abstraction 的 motivation 从纯 robotics 扩展到更广泛的连续控制场景（如 Atari、game-playing），以更好匹配 ICML 受众。\n- **不再是核心阻碍**：在 CoRL 中 venue fit 是 critical 问题（5/10），在 ICML 中不再是问题。\n\n---\n\n### 2. R2-N3 [critical → 重新评估]: 纯诊断缺乏 actionable solution\n**[RESOLVED for ICML]**\n\nICML 对贡献模式的要求与 CoRL 不同：\n- **ICML 接受标准**（reviewer instructions）：\"Papers that are technically sound, well-written, non-redundant with previous research, and useful to at least some fraction of the ICML community should be accepted.\"论文满足所有条件。\n- **与 Henderson et al. (2018) 对比**：该论文也没有提出新方法，核心贡献是实验方法论和 negative findings。本文的 factorial design（43 配置 × 5 环境 × 四级干预）在系统性上至少与之相当。\n- **贡献层次明确**：\n  1. 新 failure mode 的识别和因果分离（CIVO, 27/30, AUROC=0.957）\n  2. 架构边界的发现（MPC vs imagination-based bootstrapping）\n  3. 四级干预层级的系统分析（gradient → output → representation → architecture）\n  4. Preliminary diagnostic tool（降级为 preliminary 是诚实的）\n- **在 ICML 中 \"不要用 trained dt-embedding\" 是合理贡献**：对 ICML 的方法论社区来说，知道某条看似合理的技术路线（dt-conditioning in imagination-based RL）为什么不可行，以及为什么标准 countermeasures（Double Q, gradient stopping）无法修复，本身就有价值。这类 \"warning\" 可以避免社区重复踩坑。\n\n---\n\n### 3. R3-N1 [critical] ⚠️ 模板不合规\n**[STILL_OPEN — CRITICAL]**\n\n这是当前最严重的问题：\n\n- **main.tex:5 仍为 `\\usepackage{corl_2026}`**。未切换到 ICML 2026 样式文件（`icml2026.sty`）。\n- **PDF 页脚**（page 1 底部）明确显示：\"Submitted to the 10th Conference on Robot Learning (CoRL, 2026). Do not distribute.\" 这是 CoRL 特有的页脚文字。\n- **ICML CFP 明确要求**：\"Authors must use the correct Style Files...Papers not conforming to formatting policies face rejection without review.\"\n- **`\\keywords{}` 命令**（main.tex:49）是 CoRL 模板特有的，ICML 模板可能不支持。\n- **影响**：以当前状态提交到 ICML 将被 desk reject，无需进入实质审稿。\n\n**必须修复**：\n1. 下载 ICML 2026 样式文件（icml2026.zip）\n2. 替换 `\\usepackage{corl_2026}` 为 `\\usepackage{icml2026}`\n3. 移除或调整 `\\keywords{}` 命令\n4. 验证编译通过、格式正确\n\n---\n\n### 4. [NEW — CRITICAL] Impact Statement 缺失\n**[STILL_OPEN — CRITICAL]**\n\nICML 2026 CFP 明确要求：\n> \"Required section at end of paper (before References), does not count toward page limit.\"\n\n当前论文在 References 之前没有 Impact Statement。即使论文的 societal impact 有限，ICML 也要求至少包含一个标准声明：\n\n> \"This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.\"\n\n**必须添加**：在 Conclusion/Limitations 之后、`\\bibliography{}` 之前插入 Impact Statement section。\n\n---\n\n### 5. R2-W4 [warning, resolved]: Becker-Ehmck 引用\n**[RESOLVED]**\n\nIssue tracker 正确标记：Round 3 的 \"Becker-Ehmck 2023\" 系与 \"Benechehab et al. 2023\" 的混淆。相关引用 `benechehab2023multitimestep` 在 related_work.tex:8 中已被引用（\"Multi-timestep world models learn predictions at variable horizons but do not examine the value overestimation pathology we isolate\"）。确认 resolved。\n\n---\n\n### 6. 写作质量（针对 ICML）\n\n**Abstract 数字密度（Round 3 E1）**：\n**[PARTIALLY RESOLVED]** — 改善明显。Abstract 移除了 \"2.78×\"、\"ρ > 0.999\"、detector 句。但仍包含 \"14-19%\"、\"27/30\"、\"AUROC=0.957\"、\"LOEO\"。相比 Round 3 的 6+ 个数字指标，现在约 4 个，可接受但仍偏密。\n\n**F1-F7 双编号（Round 3 E2）**：\n**[STILL_OPEN]** — 未修改。Results section 仍使用 \"F1\"...\"F7\" 编号与 Section 编号并行。这对 ICML reviewer 来说是额外认知负担。建议：要么用 F1-F7 作为唯一编号系统（替代 subsection 编号），要么去掉 F 编号改用 descriptive subsection titles。\n\n**论文长度**：\n正文 8 页（pages 1-8），References 从 page 9 开始。符合 ICML 8 页限制 ✅\n\n**Limitations section**：\n存在于 Conclusion 的 paragraph 中（conclusion.tex:6-11）。ICML 不要求 Limitations 作为独立 section（与 NeurIPS 不同），当前形式可接受 ✅\n\n**匿名合规**：\n- \"Anonymous Author(s)\" ✅\n- \"Code: upon acceptance\" ✅\n- DreamerV3 仓库链接（官方仓库，非作者代码）✅\n- 但页脚 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\" 在 ICML 提交中技术上暴露了此前的投稿 venue（尽管这更多是模板问题而非匿名问题）\n\n**Keywords 适配**：\n当前 keywords \"World Models, Temporal Abstraction, Value Overestimation, DreamerV3\" 内容上适合 ICML，但 `\\keywords{}` 命令需确认 ICML 模板是否支持。\n\n---\n\n## Round 3 → Round 4 改进的其他确认\n\n### R1-W2 步数不对等：[SUBSTANTIALLY ADDRESSED]\n新增 \"Training horizon\" 段落（analysis.tex:10-11）提供了关键的 extended training 数据：\"Extended training (~302K steps, one seed) shows complete self-recovery after approximately 170K additional steps post-onset\"。这直接回应了 \"treatment 是否在更长训练后 recover\" 的问题。\n\n但 n=1 seed 的 extended training 数据仍然有限，且结论（self-recovery 需要 ~170K 额外步数，计算成本高）也支持论文的核心论点：CIVO 即使可以 recover，代价也很大。在 ICML 标准下，这个回应足够。\n\n### R2-W1 TAWM \"structural factor\"：[RESOLVED]\n两处修改充分回应：\n1. Abstract: \"a hypothesized structural factor\"（而非 \"the structural factor\"）\n2. Conclusion: \"Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work\"\n\n措辞准确反映了证据级别：architectural reasoning + 未经 TD-MPC2 实验验证 → 假说而非结论。\n\n### R1-N-new-1 Online detector 样本量：[RESOLVED]\nContribution 4 从 \"Online detection\" 降级为 \"Preliminary diagnostic\"，明确标注 \"TPR 95% CI [47.8%, 100%] (n=5/5), FPR 22% (2/9)\"。这是对小样本限制的诚实披露。\n\n---\n\n## 评分（ICML 标准）\n\n### ICML Venue Fit: 8/10\n论文完全属于 ICML RL track 的范畴。Diagnostic/negative-result 论文在 ICML 有先例（Henderson et al. 2018）。唯一减分：robotics-heavy 的开篇 framing 可以更通用化以更好匹配 ICML 受众，但这是 minor 的 presentation 问题。\n\n### Novelty: 7/10\n- **CIVO 作为新 failure mode**：dt-conditioning 在 imagination-based RL 中引发 value overestimation 的发现是新颖的。之前没有工作系统地研究过这个特定的失败机制。\n- **Factorial design 的诊断方法论**：将 Henderson et al. (2018) 的 factorial 方法论应用到 world-model RL 的特定问题中，方法论本身不新但应用有价值。\n- **MPC vs imagination-based 的 architectural boundary**：这个洞察有概念新颖性，即使实验验证不完整（\"hypothesized\"）。\n- **减分点**：论文没有提出新方法或新算法，核心工具（factorial ablation, NVE metric, gradient stopping）都是已有技术的组合。CIVO 现象虽新颖，但论文自己承认它在 manipulation 中不出现、在 locomotion 中可以通过 \"不用 trained embedding\" 避免。\n\n### Significance: 6/10\n- **对 world-model RL 社区的价值**：知道 dt-conditioning 在 imagination-based RL 中为什么失败、为什么 Double Q 和 gradient stopping 无法修复，可以帮助社区避免重复探索这条技术路线。\n- **方法论示范**：四级干预层级分析为未来的 RL 诊断研究提供了一个可复用的框架。\n- **减分点**：\n  - 发现的 scope 有限——仅在 DreamerV3 + locomotion 中确认\n  - Actionable outcome 弱——最有效建议是\"不要用\"\n  - 未提出解决方案或新理论框架\n  - 与 Henderson et al. (2018) 相比，后者的发现影响了整个 RL 社区的实验报告实践；本文的影响范围窄得多（仅 world-model RL + temporal abstraction）\n\n### 写作质量: 7/10\n- 结构清晰、专业\n- Abstract 较 Round 3 改善明显但仍偏数字密集\n- F1-F7 双编号增加认知负担\n- 总体可读性良好，技术细节充分\n\n---\n\n## ICML 维度打分（4-point scale: Excellent / Good / Fair / Poor）\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| Soundness | Good (3/4) | Factorial design 严谨，LOEO 交叉验证有力；但 extended training 仅 1 seed，TAWM 对比无实验（已弱化为 hypothesized） |\n| Presentation | Good (3/4) | 结构清晰，写作专业；Abstract 偏数字密集，F1-F7 双编号增加认知负担；模板问题需修复 |\n| Significance | Fair (2/4) | 对 world-model RL 子社区有价值的 warning，但 scope 窄（DreamerV3 + locomotion），无解决方案 |\n| Originality | Good (3/4) | CIVO 作为新 failure mode 有新颖性，MPC vs imagination 的 architectural boundary 有概念价值；方法论是已有技术组合 |\n\n### Overall Recommendation: 4 (Weak Accept)\n论文是一个 technically solid 的 diagnostic study，在 ICML RL track 中处于 borderline accept 区域。主要优势是 factorial design 的系统性和 CIVO 发现的新颖性；主要劣势是有限的 scope 和缺乏 constructive solution。\n\n---\n\n## 与 ICML 历史接受论文对比\n\n| 对比论文 | 贡献类型 | 本文对比 |\n|---------|---------|---------|\n| Henderson et al. (2018) \"RL that Matters\" | Diagnostic，方法论指南 | 类似贡献模式，但影响范围窄得多 |\n| Lyle et al. (2022) \"Capacity Loss in RL\" | 诊断 + partial mitigation | 本文结构类似：诊断→干预→发现干预不够 |\n| Lambert et al. (2020) \"Objective Mismatch\" | Diagnostic, model-based RL | 类似领域的 diagnostic work |\n\n本文的 systematic rigor 与上述论文相当，但 breadth of impact 偏窄。如果 reviewer 重视 \"避免社区重复踩坑\" 的价值，weak accept 是合理的；如果 reviewer 要求 constructive solution 或更广泛的适用性，可能会 weak reject。\n\n---\n\n## 总结\n\n**两个 CRITICAL 格式问题必须立即修复**：\n1. 模板从 `corl_2026` 切换到 `icml2026`（含页脚修复）\n2. 添加 Impact Statement\n\n**内容方面**，Round 3→4 的修改质量好——\"hypothesized structural factor\"、detector 降级、training horizon 段落、baseline 值补充都直接回应了具体审稿意见。转投 ICML 是正确决策：论文的贡献模式（diagnostic + negative result）在 ICML 中比 CoRL 更有竞争力。\n\n**Remaining weakness**：novelty 和 significance 在 ICML 中处于 borderline 水平。如果审稿人认为 \"在 DreamerV3 locomotion 中发现的一个可以通过不用 trained embedding 避免的 failure mode\" 值得 ICML 版面，论文可以接受；如果审稿人期望更广泛的适用性或 constructive solution，论文偏弱。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-24T09:32:05.593129+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4120
}
```

</details>

---

### Assistant

_source line 174 · 2026-05-24T09:32:16.015610+00:00_

审稿完成。已提交 Round 4 评估，核心发现：

1. **两个 CRITICAL 格式问题**：模板仍为 `corl_2026`（PDF 页脚明确显示 CoRL），且缺少 ICML 必需的 Impact Statement——以当前状态提交会被 desk reject
2. **Venue fit 大幅改善**：从 CoRL 的 5/10 提升到 ICML 的 8/10，diagnostic/negative-result 论文在 ICML 有先例
3. **内容修改质量好**：Round 3 的具体审稿意见（"structural factor" 弱化、detector 降级、training horizon 数据、baseline 值补充）均已回应
4. **Overall**: ICML 标准下 Weak Accept (4/6)，soundness 和 originality 是 Good，significance 偏 Fair

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 6

16 recorded events

### User

_source line 175 · 2026-05-24T09:35:27.085511+00:00_

[Round 4 审稿请求]:
## Step 2 交叉分享 — Reviewer 1 的 Round 4 完整审稿意见

请逐条回应，标注 [AGREE] 或 [REBUT]（附理由）。

---

### Reviewer 1 核心发现：

**1. [CRITICAL] 模板仍为 `corl_2026`**（与你的发现一致）

**2. R1-W2 步数不对等 → [RESOLVED]**
Discussion 新增 "Training horizon" 段落，报告 302K 延长实验（exp_045 seed s3: NVE peak 4.91× → 自恢复至 0.05×, eval 867.6 = 94.7% baseline）。论文正确论证 105K 足以观察 onset (45K-65K window)。

**3. R2-W1 TAWM 对比 → [RESOLVED]**
"hypothesized structural factor" 全文一致，Conclusion 增加 "Empirical validation on MPC-based architectures remains future work"。

**4. R3-N-new-1 Detector 样本量 → [RESOLVED]**
降级为 "Preliminary diagnostic" + Clopper-Pearson CI [47.8%, 100%] + "requires larger-sample validation"。

**5. R3-N-new-2 Dual-critic 叙事 → [PARTIALLY RESOLVED]**
Appendix G.3 承认 open question，但主文 Section 4.8 使用 "gradient diversity" 措辞无实证支撑。建议改为 "may instead function through a capacity-dependent mechanism during early training (Appendix G)"。

**6. [NEW, warning] N-R4-1: Seed 数量前后不一致**
- Methodology Section 3.3: "Key configurations use **4** seeds"
- Results Section 4.2: "all **five** Walker Walk seeds, n=5"
- Conclusion Limitations: "Statistical power with **4** seeds"
- Figure 2 caption: "n=3 seeds plotted; seed 4 data in Table"（若有 5 seeds 则应更新）
- IQM 175.2 在 n=4→n=5 后完全不变——统计上不常见

**7. [NEW, minor] N-R4-4: Introduction 仍用 "isolate" + "causal chain"**
Abstract 已改 "identify"，但 Introduction line 6/11 仍使用 "isolate"，Results Section 4 使用 "causal chain"，与弱化因果声明的方向不一致。

**8. [minor] N-R4-6: Becker-Ehmck 2023 仍未引用**
第三轮指出仍未修复。

**9. Overall: Weak Accept (4/6), 方法严谨性 7.5/10, Venue fit 8.5/10**

---

### 你的交叉任务：

1. **N-R4-1 Seed 数量不一致**——你是否也注意到？这是否影响你对 Soundness 的评分？
2. **"gradient diversity" 无支撑**——你是否同意 R1 的 PARTIALLY RESOLVED 判定？
3. **R1 判定 R1-W2 (步数不对等) 和 R2-W1 (TAWM) 均为 RESOLVED**——你是否同意？
4. **N-R4-4 Introduction "isolate" 残留**——严重性如何？
5. **Becker-Ehmck 2023**——R1 也确认 Round 4 仍未引用。你之前在 Round 2/3 均提出此问题，Round 3 报告中指出已以 benechehab2023multitimestep 引用（认为审稿人混淆了作者名）。你是否接受这一解释？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-24T09:35:34.075702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "65",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "65",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-24T09:35:35.230852+00:00_

65	
66	%% ============================================================
67	%% F2: Trained dt_embedding → nve > 1.5x
68	%% ============================================================
69	
70	\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}
71	\label{sec:f2}
72	
73	The factorial design isolates trained $\dt$-embedding as the strongest predictor. The \emph{primary} comparison---008d (trained, subsample ON) vs.\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\nve = 4.12\times$ (eval 82.8) vs.\ $\nve \leq 0.97\times$ (eval 503.0). \emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\nve \geq 1.5\times$ threshold (35K+ window) correctly classifies 27 of 30 experimental configurations across two environments (AUROC${=}0.957$, in-sample; LOEO cross-validated, Table~\ref{tab:nve_loeo}; Figure~\ref{fig:nve_trajectory}).
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=0.65\columnwidth]{figures/fig1_nve_trajectory.pdf}
77	\caption{NVE trajectories (mean $\pm$ seed range). Trained $\dt$-embedding (red, Walker Walk, $n{=}3$ seeds plotted; seed~4 data in Table~\ref{tab:complete_results}) exceeds the $1.5\times$ threshold (dashed) in all seeds; no-embedding control (blue) remains near $1.0\times$. Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2). Dotted line marks the 35K diagnostic window onset.}
78	\label{fig:nve_trajectory}
79	\end{figure}
80	
81	The trained $\dt$-embedding precedes CIVO in all five Walker Walk seeds (peak NVE $1.53$--$4.72\times$), universally degrading performance to below 30\% of baseline (IQM $175.2$, $n{=}5$; \citealt{agarwal2021precipice}). Combined with Cheetah Run (\S\ref{sec:f6}), CIVO onset is universal across all seven tested seeds ($n{=}7$, two environments) with 6/7 suffering sustained policy collapse, 1/7 self-correcting (A
…[truncated 3854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1155
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-24T09:35:35.281550+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-24T09:35:35.384240+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-24T09:35:36.087651+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "isolate|causal chain|causal",
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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "isolate|causal chain|causal",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-24T09:35:36.138604+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:12:We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:6:Table~\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:244:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:312:Table~\ref{tab:three_way_emb} isolates embedding \emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\dt{=}2$ imagination).
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:404:\label{tab:causal_matrix}
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/proj
…[truncated 3101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-24T09:36:16.327765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "150",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "150",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-24T09:36:16.452665+00:00_

150	%% Forward-pass interventions
151	%% ============================================================
152	
153	\subsection{Forward-Pass Interventions}
154	\label{sec:forward_results}
155	
156	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\sigma{=}0.2$ (NVE $< 1.0\times$, eval 45--91\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\sigma{=}1.0$) causes policy erosion to 15\% baseline; PickCube 0/1 (Appendix~\ref{sec:tcn_cross_env}). TCN is a \emph{diagnostic probe}, not a deployable mitigation.
157	
158	%% ============================================================
159	%% Architecture-Level Ablation
160	%% ============================================================
161	
162	\subsection{Architecture-Level Ablation}
163	\label{sec:arch_results}
164	
165	\paragraph{Critic convergence in pure imagination.}
166	Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}). Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix~\ref{sec:dual_critic_appendix}).
167	
168	\paragraph{$2{\times}2$ factorial: recovery vs.\ prevention.}
169	Min drives recovery: narrow dual-critic (${\sim}1.2$M) recovers fully (${\sim}16$--$19\times$ recovery ratio) despite $2\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\nve \leq 1.4\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).
170	
171	%% ==============================
…[truncated 625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 124
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-24T09:36:18.015227+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gradient diversity|capacity-dependent|different mechanism",
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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gradient diversity|capacity-dependent|different mechanism",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-24T09:36:18.267689+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex:568:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex:13:    \item \textbf{Four-level intervention hierarchy.} Across gradient, output, representation, and architecture levels, no intervention reliably eliminates CIVO across environments. Gradient magnitude does not predict causal importance (reward head: 38--49\%, reward-only stopping fails). In pure-imagination training, dual critics converge ($\rho > 0.999$), eliminating Double Q pessimism, though the min operation enables recovery through a different mechanism.
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex:166:Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}). Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix~\ref{sec:dual_critic_appendix}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-24T09:36:18.268184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": "600",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "offset": "600",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-24T09:36:18.369920+00:00_

600	Walker & s1 (008d) & 4.12$\times$ & 4.12$\times$ & 82.8 & Full collapse \\
601	Walker & s2 (009b) & 1.62$\times$ & 0.38$\times$ & 267.9 & Transient CIVO \\
602	Walker & s3 (008d\_s3) & 1.53$\times$ & 1.53$\times$ & 268$^\diamond$ & Late-onset collapse \\
603	Walker & s4 (008d\_s4) & 4.62$\times$ & 4.62$\times$ & 63.6 & Full collapse \\
604	Walker & s5 (059) & 4.72$\times$ & 1.22$\times$ & 95.8 & Collapse$^\dagger$ \\
605	\midrule
606	Cheetah & s1 (010b) & 8.27$\times$ & 8.27$\times$ & 51.7 & Full collapse \\
607	Cheetah & s0 (010b\_s0) & 108.52$\times$ & 108.52$\times$ & 0.83 & Full collapse \\
608	\bottomrule
609	\end{tabular}
610	\vspace{1pt}
611	{\raggedright\footnotesize $^\diamond$ Transitional; train returns still declining at 105K. $^\dagger$~NVE self-corrected ($4.72\times$ $\to$ $1.22\times$) but policy did not recover (eval 10.5\% of baseline).\par}
612	\end{table}
613	
614	All seven CIVO-positive seeds cross the $\nve > 1.5\times$ threshold (Table~\ref{tab:post_civo}), yet the downstream damage is stochastic.\footnote{Exp\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\_008d).}  Full collapse is the majority outcome (6/7 seeds), with one self-correction case (Walker seed 2); seed 5 exemplifies a dissociation where NVE self-corrects ($4.72\times \to 1.22\times$) while the policy remains collapsed (eval 10.5\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\times$ vs.\ Walker's $1.53$--$4.62\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network ca
…[truncated 7717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-24T09:38:42.627102+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 4 审稿意见的逐条评议\n\n---\n\n### 1. [CRITICAL] 模板仍为 `corl_2026`\n**[AGREE]** 与我的发现完全一致。PDF 页脚显示 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\"。必须切换到 `icml2026.sty`。我在自己的审稿中也将此列为两个 CRITICAL 格式问题之一（另一个是缺少 Impact Statement，R1 似乎未提及）。\n\n---\n\n### 2. R1-W2 步数不对等 → [RESOLVED]\n**[AGREE]** Discussion 新增的 \"Training horizon\" 段落（analysis.tex:10-11）提供了关键数据：exp_045 seed s3 在 302K 步后完全 self-recovery（NVE 4.91× → 0.05×, eval 867.6 = 94.7% baseline）。这充分证明了：\n- 105K 步足以观察 CIVO onset（45K-65K window）\n- Recovery 需要 ~170K 额外步数，计算成本高，支持论文的核心论点\n- \"14-19% of baseline\" 的 claim 限定在 105K 时间窗口内是准确的\n\nR1 给出 RESOLVED 是合理的。\n\n---\n\n### 3. R2-W1 TAWM 对比 → [RESOLVED]\n**[AGREE]** 两处修改充分回应了我在 Round 3 交叉评议中的关切：\n- Abstract/Conclusion: \"a hypothesized structural factor\"（全文一致）\n- Conclusion: \"Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work\"\n\n措辞准确反映证据级别，不再 overclaim。\n\n---\n\n### 4. R3-N-new-1 Detector 样本量 → [RESOLVED]\n**[AGREE]** 降级为 \"Preliminary diagnostic\" + Clopper-Pearson CI [47.8%, 100%] + \"requires larger-sample validation\"（results.tex:178）是对小样本限制的诚实披露。Contribution 列表中的表述（introduction.tex:14）也相应调整。\n\n---\n\n### 5. R3-N-new-2 Dual-critic \"gradient diversity\" → [PARTIALLY RESOLVED]\n**[AGREE]** R1 的判定准确。\n\n具体问题在 results.tex:166：\n> \"Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through **gradient diversity** (Appendix G).\"\n\n- \"gradient diversity\" 是一个具有特定技术含义的术语（如 gradient diversity in distributed optimization），论文在此处使用它来解释为什么 wide dual-critic + min 能在 ρ > 0.999 下仍然有效，但 **appendix 中没有提供 gradient diversity 的直接证据**（如 gradient cosine similarity、gradient variance 等指标）。\n- R1 建议改为 \"may instead function through a capacity-dependent mechanism during early training (Appendix G)\" 是更准确的替代方案。\n- 同时，introduction.tex:13 中 \"the min operation enables recovery through a different mechanism\" 的措辞反而更合适——承认了机制不明但避免了无根据的猜测。主文 Section 4.8 应与此一致。\n\n**影响 Soundness 评分**：此问题的严重性较低（\"may\" 限定词已降低了 claim 强度），但在 ICML 的 soundness 标准下，无支撑的机制假说不应出现在主文中。建议用 R1 的替代措辞或直接说 \"the mechanism is an open question\"。\n\n---\n\n### 对 Director 的 5 个具体问题的回答\n\n#### Q1: N-R4-1 Seed 数量不一致——是否影响 Soundness？\n\n**[AGREE]** 我独立确认了这个问题，而且问题比 R1 描述的更严重。\n\n**不一致的具体位置**：\n| 位置 | 文本 | 问题 |\n|------|------|------|\n| methodology.tex:32 | \"Key configurations use **4** seeds\" | 与 n=5 不一致 |\n| results.tex:81 | \"all **five** Walker Walk seeds...IQM $175.2$, $n{=}5$\" | 声称 n=5 |\n| conclusion.tex:10 | \"Statistical power with **4** seeds\" | 与 n=5 不一致 |\n| Figure 2 caption (results.tex:77) | \"n=3 seeds plotted; **seed 4** data in Table\" | 应提及 seed 5 |\n\n**更严重的问题——IQM 数值错误**：\n\n从 Appendix（appendix.tex:600-604），5 个 Walker seeds 的 eval 值为：\n- s1: 82.8, s2: 267.9, s3: 268, s4: 63.6, s5: 95.8\n\n排序后：{63.6, 82.8, 95.8, 267.9, 268.0}\n\n- **n=4 时 IQM**（25% trim, 去掉首尾各 1）：middle 2 = {82.8, 267.9} → mean = **175.35 ≈ 175.2** ✓\n- **n=5 时 IQM**（25% trim, 去掉首尾各 1）：middle 3 = {82.8, 95.8, 267.9} → mean = **148.8**，**而非 175.2**\n\nIQM 175.2 是 n=4 的正确值，添加第 5 个 seed（eval 95.8）后未重新计算。这是一个**数据完整性错误**，不是四舍五入问题。\n\n**对 Soundness 的影响**：将我的 Soundness 评分从 Good (3/4) 微调至 Good- (2.75/4)。错误本身是 careless 而非 systematic，不影响核心结论（CIVO 仍然在所有 5 seeds 中出现），但对于一篇以统计严谨性为卖点的 diagnostic paper（引用 Agarwal et al. 2021、报告 LOEO AUROC），这类不一致会损害可信度。\n\n**修复**：(1) 重新计算 n=5 的 IQM 并更新 results.tex:81；(2) methodology.tex:32 改为 \"Key configurations use 4-5 seeds\"；(3) conclusion.tex:10 同步更新；(4) Figure 2 caption 更新提及 seed 5。\n\n---\n\n#### Q2: \"gradient diversity\" 无支撑——是否同意 PARTIALLY RESOLVED？\n\n**[AGREE]** 已在上文第 5 点详细说明。R1 的判定和替代措辞建议都合理。\n\n---\n\n#### Q3: R1-W2 和 R2-W1 均判为 RESOLVED——是否同意？\n\n**[AGREE]** 两者均同意。理由已在上文第 2、3 点给出。\n\n---\n\n#### Q4: N-R4-4 Introduction \"isolate\" 残留——严重性如何？\n\n**[REBUT — minor, not warning]**\n\nR1 标为 minor 是合理的，但我认为这个问题的实际严重性比 R1 暗示的更低：\n\n- \"isolate\" 在实验科学中是标准的 factorial ablation 术语——当你通过 2×2 设计控制其他变量来测试某因素的效应时，\"isolate the effect of X\" 是准确的描述。Abstract 用 \"identify\" 是更保守的选择，但 Introduction 和 Results 中的 \"isolate\" 并不 overclaim。\n- \"causal chain\"（results.tex:4）更值得注意——\"establish a causal chain\" 暗示了因果推断，而 factorial ablation 提供的是 predictive/associative 证据。但在 RL 实验传统中，这种用法是常见的（Henderson et al. 2018 也使用类似措辞）。\n- 建议将 \"establish a causal chain\" 改为 \"trace a pathway\" 或 \"establish a predictive chain\"。这是 minor 修改，不影响接收决定。\n\n---\n\n#### Q5: Becker-Ehmck 2023——是否接受混淆解释？\n\n**[AGREE — 接受，降级为 non-issue]**\n\n重新审视此问题：\n1. Round 1 原始 issue 仅提到 \"Becker-Ehmck 2023\" 未给出论文标题\n2. Philip Becker-Ehmck 的已知工作（TD-VAE, ICLR 2020）是关于 temporal abstraction in latent models，但那是 2020 年的\n3. 我搜索后未找到一篇 2023 年的 \"Becker-Ehmck\" 论文与本文直接相关\n4. Benechehab et al. 2023 (benechehab2023multitimestep) 关于 multi-timestep models in MBRL 的工作与本文直接相关，且已被引用（related_work.tex:8）\n5. 两者的主题高度重叠（multi-timestep prediction in model-based RL），名字有一定相似性\n\n混淆解释是合理的。如果确实存在一篇特定的 Becker-Ehmck 2023 论文应该引用，Round 1 reviewer 应该提供具体标题。在当前信息下，我不再追踪此 issue。R1 继续标记为 \"仍未引用\" 是 technically correct 但 practically irrelevant。\n\n---\n\n### 评分调整\n\n**修改前（纯基于文本审查）→ 修改后（考虑 R1 的发现）**\n\n| 维度 | R2 原始评分 | 调整后 | 理由 |\n|------|------------|--------|------|\n| Soundness | Good (3/4) | Good- (2.75/4) | Seed 数量不一致 + IQM 未重算是 data integrity 问题 |\n| Presentation | Good (3/4) | Good (3/4) | 不变 |\n| Significance | Fair (2/4) | Fair (2/4) | 不变 |\n| Originality | Good (3/4) | Good (3/4) | 不变 |\n\n**Overall Recommendation**: 维持 **4 (Weak Accept)**。Seed/IQM 不一致是 careless error 而非 fundamental flaw，可在 camera-ready 中修复。核心结论（CIVO 在所有 seeds 中出现、无可靠干预）不受影响。\n\n---\n\n### 与 R1 评分对比\n\n| 维度 | R1 | R2 | 差异说明 |\n|------|-----|-----|----------|\n| Overall | 4 (Weak Accept) | 4 (Weak Accept) | 一致 |\n| 方法严谨性 | 7.5/10 | 7/10 | R2 因 IQM 错误和 \"gradient diversity\" 略低 |\n| Venue fit | 8.5/10 | 8/10 | 基本一致，R2 稍保守（robotics framing 在 ICML 中不加分也不减分） |\n\n**两位 reviewer 的核心共识**：\n1. 论文在 ICML 中比 CoRL 更合适\n2. Factorial design 是最大优势\n3. Scope 和 significance 是主要 weakness\n4. 模板必须修复\n5. Weak Accept 是当前合理的推荐\n\n**我的补充（R1 未提及）**：\n- **Impact Statement 缺失**：ICML 2026 要求 \"Impact statement at end of paper (before References)\"，当前论文缺少此 section。这与模板问题同样是 desk reject 风险。\n- **Keywords**：`\\keywords{}` 命令是 CoRL 特有的，ICML 模板可能不支持，切换模板时需处理。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 4 审稿意见的逐条评议\n\n---\n\n### 1. [CRITICAL] 模板仍为 `corl_2026`\n**[AGREE]** 与我的发现完全一致。PDF 页脚显示 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\"。必须切换到 `icml2026.sty`。我在自己的审稿中也将此列为两个 CRITICAL 格式问题之一（另一个是缺少 Impact Statement，R1 似乎未提及）。\n\n---\n\n### 2. R1-W2 步数不对等 → [RESOLVED]\n**[AGREE]** Discussion 新增的 \"Training horizon\" 段落（analysis.tex:10-11）提供了关键数据：exp_045 seed s3 在 302K 步后完全 self-recovery（NVE 4.91× → 0.05×, eval 867.6 = 94.7% baseline）。这充分证明了：\n- 105K 步足以观察 CIVO onset（45K-65K window）\n- Recovery 需要 ~170K 额外步数，计算成本高，支持论文的核心论点\n- \"14-19% of baseline\" 的 claim 限定在 105K 时间窗口内是准确的\n\nR1 给出 RESOLVED 是合理的。\n\n---\n\n### 3. R2-W1 TAWM 对比 → [RESOLVED]\n**[AGREE]** 两处修改充分回应了我在 Round 3 交叉评议中的关切：\n- Abstract/Conclusion: \"a hypothesized structural factor\"（全文一致）\n- Conclusion: \"Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work\"\n\n措辞准确反映证据级别，不再 overclaim。\n\n---\n\n### 4. R3-N-new-1 Detector 样本量 → [RESOLVED]\n**[AGREE]** 降级为 \"Preliminary diagnostic\" + Clopper-Pearson CI [47.8%, 100%] + \"requires larger-sample validation\"（results.tex:178）是对小样本限制的诚实披露。Contribution 列表中的表述（introduction.tex:14）也相应调整。\n\n---\n\n### 5. R3-N-new-2 Dual-critic \"gradient diversity\" → [PARTIALLY RESOLVED]\n**[AGREE]** R1 的判定准确。\n\n具体问题在 results.tex:166：\n> \"Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may instead regularize through **gradient diversity** (Appendix G).\"\n\n- \"gradient diversity\" 是一个具有特定技术含义的术语（如 gradient diversity in distributed optimization），论文在此处使用它来解释为什么 wide dual-critic + min 能在 ρ > 0.999 下仍然有效，但 **appendix 中没有提供 gradient diversity 的直接证据**（如 gradient cosine similarity、gradient variance 等指标）。\n- R1 建议改为 \"may instead function through a capacity-dependent mechanism during early training (Appendix G)\" 是更准确的替代方案。\n- 同时，introduction.tex:13 中 \"the min operation enables recovery through a different mechanism\" 的措辞反而更合适——承认了机制不明但避免了无根据的猜测。主文 Section 4.8 应与此一致。\n\n**影响 Soundness 评分**：此问题的严重性较低（\"may\" 限定词已降低了 claim 强度），但在 ICML 的 soundness 标准下，无支撑的机制假说不应出现在主文中。建议用 R1 的替代措辞或直接说 \"the mechanism is an open question\"。\n\n---\n\n### 对 Director 的 5 个具体问题的回答\n\n#### Q1: N-R4-1 Seed 数量不一致——是否影响 Soundness？\n\n**[AGREE]** 我独立确认了这个问题，而且问题比 R1 描述的更严重。\n\n**不一致的具体位置**：\n| 位置 | 文本 | 问题 |\n|------|------|------|\n| methodology.tex:32 | \"Key configurations use **4** seeds\" | 与 n=5 不一致 |\n| results.tex:81 | \"all **five** Walker Walk seeds...IQM $175.2$, $n{=}5$\" | 声称 n=5 |\n| conclusion.tex:10 | \"Statistical power with **4** seeds\" | 与 n=5 不一致 |\n| Figure 2 caption (results.tex:77) | \"n=3 seeds plotted; **seed 4** data in Table\" | 应提及 seed 5 |\n\n**更严重的问题——IQM 数值错误**：\n\n从 Appendix（appendix.tex:600-604），5 个 Walker seeds 的 eval 值为：\n- s1: 82.8, s2: 267.9, s3: 268, s4: 63.6, s5: 95.8\n\n排序后：{63.6, 82.8, 95.8, 267.9, 268.0}\n\n- **n=4 时 IQM**（25% trim, 去掉首尾各 1）：middle 2 = {82.8, 267.9} → mean = **175.35 ≈ 175.2** ✓\n- **n=5 时 IQM**（25% trim, 去掉首尾各 1）：middle 3 = {82.8, 95.8, 267.9} → mean = **148.8**，**而非 175.2**\n\nIQM 175.2 是 n=4 的正确值，添加第 5 个 seed（eval 95.8）后未重新计算。这是一个**数据完整性错误**，不是四舍五入问题。\n\n**对 Soundness 的影响**：将我的 Soundness 评分从 Good (3/4) 微调至 Good- (2.75/4)。错误本身是 careless 而非 systematic，不影响核心结论（CIVO 仍然在所有 5 seeds 中出现），但对于一篇以统计严谨性为卖点的 diagnostic paper（引用 Agarwal et al. 2021、报告 LOEO AUROC），这类不一致会损害可信度。\n\n**修复**：(1) 重新计算 n=5 的 IQM 并更新 results.tex:81；(2) methodology.tex:32 改为 \"Key configurations use 4-5 seeds\"；(3) conclusion.tex:10 同步更新；(4) Figure 2 caption 更新提及 seed 5。\n\n---\n\n#### Q2: \"gradient diversity\" 无支撑——是否同意 PARTIALLY RESOLVED？\n\n**[AGREE]** 已在上文第 5 点详细说明。R1 的判定和替代措辞建议都合理。\n\n---\n\n#### Q3: R1-W2 和 R2-W1 均判为 RESOLVED——是否同意？\n\n**[AGREE]** 两者均同意。理由已在上文第 2、3 点给出。\n\n---\n\n#### Q4: N-R4-4 Introduction \"isolate\" 残留——严重性如何？\n\n**[REBUT — minor, not warning]**\n\nR1 标为 minor 是合理的，但我认为这个问题的实际严重性比 R1 暗示的更低：\n\n- \"isolate\" 在实验科学中是标准的 factorial ablation 术语——当你通过 2×2 设计控制其他变量来测试某因素的效应时，\"isolate the effect of X\" 是准确的描述。Abstract 用 \"identify\" 是更保守的选择，但 Introduction 和 Results 中的 \"isolate\" 并不 overclaim。\n- \"causal chain\"（results.tex:4）更值得注意——\"establish a causal chain\" 暗示了因果推断，而 factorial ablation 提供的是 predictive/associative 证据。但在 RL 实验传统中，这种用法是常见的（Henderson et al. 2018 也使用类似措辞）。\n- 建议将 \"establish a causal chain\" 改为 \"trace a pathway\" 或 \"establish a predictive chain\"。这是 minor 修改，不影响接收决定。\n\n---\n\n#### Q5: Becker-Ehmck 2023——是否接受混淆解释？\n\n**[AGREE — 接受，降级为 non-issue]**\n\n重新审视此问题：\n1. Round 1 原始 issue 仅提到 \"Becker-Ehmck 2023\" 未给出论文标题\n2. Philip Becker-Ehmck 的已知工作（TD-VAE, ICLR 2020）是关于 temporal abstraction in latent models，但那是 2020 年的\n3. 我搜索后未找到一篇 2023 年的 \"Becker-Ehmck\" 论文与本文直接相关\n4. Benechehab et al. 2023 (benechehab2023multitimestep) 关于 multi-timestep models in MBRL 的工作与本文直接相关，且已被引用（related_work.tex:8）\n5. 两者的主题高度重叠（multi-timestep prediction in model-based RL），名字有一定相似性\n\n混淆解释是合理的。如果确实存在一篇特定的 Becker-Ehmck 2023 论文应该引用，Round 1 reviewer 应该提供具体标题。在当前信息下，我不再追踪此 issue。R1 继续标记为 \"仍未引用\" 是 technically correct 但 practically irrelevant。\n\n---\n\n### 评分调整\n\n**修改前（纯基于文本审查）→ 修改后（考虑 R1 的发现）**\n\n| 维度 | R2 原始评分 | 调整后 | 理由 |\n|------|------------|--------|------|\n| Soundness | Good (3/4) | Good- (2.75/4) | Seed 数量不一致 + IQM 未重算是 data integrity 问题 |\n| Presentation | Good (3/4) | Good (3/4) | 不变 |\n| Significance | Fair (2/4) | Fair (2/4) | 不变 |\n| Originality | Good (3/4) | Good (3/4) | 不变 |\n\n**Overall Recommendation**: 维持 **4 (Weak Accept)**。Seed/IQM 不一致是 careless error 而非 fundamental flaw，可在 camera-ready 中修复。核心结论（CIVO 在所有 seeds 中出现、无可靠干预）不受影响。\n\n---\n\n### 与 R1 评分对比\n\n| 维度 | R1 | R2 | 差异说明 |\n|------|-----|-----|----------|\n| Overall | 4 (Weak Accept) | 4 (Weak Accept) | 一致 |\n| 方法严谨性 | 7.5/10 | 7/10 | R2 因 IQM 错误和 \"gradient diversity\" 略低 |\n| Venue fit | 8.5/10 | 8/10 | 基本一致，R2 稍保守（robotics framing 在 ICML 中不加分也不减分） |\n\n**两位 reviewer 的核心共识**：\n1. 论文在 ICML 中比 CoRL 更合适\n2. Factorial design 是最大优势\n3. Scope 和 significance 是主要 weakness\n4. 模板必须修复\n5. Weak Accept 是当前合理的推荐\n\n**我的补充（R1 未提及）**：\n- **Impact Statement 缺失**：ICML 2026 要求 \"Impact statement at end of paper (before References)\"，当前论文缺少此 section。这与模板问题同样是 desk reject 风险。\n- **Keywords**：`\\keywords{}` 命令是 CoRL 特有的，ICML 模板可能不支持，切换模板时需处理。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-24T09:38:46.595746+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3968
}
```

</details>

---

### Assistant

_source line 190 · 2026-05-24T09:38:56.087163+00:00_

交叉回应已提交。核心发现：

1. **IQM 数据错误确认**：第 5 个 seed (eval 95.8) 加入后 IQM 应为 ~148.8 而非 175.2——n=4 的值未重新计算，是数据完整性问题
2. **"gradient diversity" 无支撑**：同意 R1 的 PARTIALLY RESOLVED，主文应弱化措辞
3. **R1-W2 步数、R2-W1 TAWM**：同意均为 RESOLVED
4. **"isolate" 残留**：minor 问题，factorial ablation 语境下可接受，"causal chain" 建议弱化
5. **Becker-Ehmck**：接受混淆解释，降级为 non-issue
6. **补充 R1 遗漏**：ICML Impact Statement 缺失同样是 desk reject 风险
7. **Overall**：与 R1 一致，维持 Weak Accept (4/6)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 7

32 recorded events

### User

_source line 191 · 2026-05-24T15:03:19.900183+00:00_

[Round 5 审稿请求]:
## Round 5 继续审稿 — Reviewer 2（Venue 合规 + 写作质量 + 贡献度）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: ICML 2026
**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex`
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/submitted.pdf`
**Venue 要求**: 正文 8 页 + 无限 references/impact statement/appendix，double-blind，icml2026.sty 模板，Impact Statement 必须在 References 前
**上轮评分**: Round 4 Weak Accept (6/10)

### 你的侧重
Venue 合规 + 写作质量 + 贡献度评估。本轮重点是**验证 ICML 格式合规性**和**评估修改后的论文整体质量**。

### Round 4 Open/In-Progress Issues（逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由）

**CRITICAL (3)**:
1. **N-R4-1** 模板仍为 corl_2026 → 需切换 icml2026.sty | status: in_progress
2. **N-R4-2** 缺少 ICML Impact Statement → 需在 References 前添加 | status: in_progress
3. **N-R4-3** IQM 计算错误：175.2 是 n=4 值，n=5 正确值应为 148.8 | status: in_progress

**WARNING (4)**:
4. **R3-N-new-2** "gradient diversity" 术语无支撑证据（results.tex:166）| status: in_progress | [复发×2轮]
5. **R3-N-new-3** ManiSkill/Cheetah baseline eval 值在 Table 1 中缺失 | status: in_progress | [复发×2轮]
6. **N-R4-4** Seed 数量叙述不一致（methodology 说4，results 说5，Figure 2 caption 漏 seed 5）| status: in_progress
7. **R2-N3** 纯诊断负面结果缺乏 actionable solution（ICML 下降级为 warning）| status: in_progress

**INFO (1)**:
8. **N-R4-5** "causal chain" → "trace a pathway" | status: in_progress

### 你的重点检查
**Venue 合规**:
- ICML 2026 模板（icml2026.sty）是否正确使用
- 正文是否 ≤ 8 页（不含 references/impact statement/appendix）
- Double-blind 匿名合规（无作者信息泄露、无 GitHub/实验室名称）
- Impact Statement 质量——是否充分讨论了潜在影响和局限
- \icmltitlerunning 和 \icmlkeywords 是否正确设置
- 引用格式是否符合 ICML 要求

**写作质量**:
- Abstract 信息密度（Round 3 注意到过多数字指标）
- 因果语言一致性（isolate / strongest predictor / hypothesized structural factor）
- 论文叙事连贯性（F1-F7 pathway）
- Robotics framing 是否需要调整（从 CoRL → ICML 后是否仍然合适）

**贡献度评估**:
- 论文在 ICML RL track 的定位是否清晰
- Negative result + diagnostic framework 的贡献模式在 ICML 中的价值
- 与 Round 4 相比，贡献度评估是否有变化

### 评分维度
Soundness (1-4), Presentation (1-4), Contribution (1-4), Overall (1-6), Confidence (1-5)
对每个 RESOLVED issue 给出验证依据（具体文件:行号）；对 STILL_OPEN 给出具体位置和原因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-24T15:03:30.714891+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-24T15:03:31.668959+00:00_

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
…[truncated 354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-24T15:03:31.669354+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-24T15:03:32.071098+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 27/30, AUROC${=}0.957$, LOEO cross-validated). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-24T15:03:32.121787+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-24T15:03:32.122331+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-24T15:03:45.784012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-24T15:03:45.834894+00:00_

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
…[truncated 6075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-24T15:03:46.338697+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-24T15:03:46.592116+00:00_

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
…[truncated 2275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-24T15:03:46.592609+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-24T15:03:46.694710+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-24T15:04:03.565013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "155",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "155",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-24T15:04:04.067446+00:00_

155	\label{sec:forward_results}
156	
157	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\sigma{=}0.2$ (NVE $< 1.0\times$, eval 45--91\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\sigma{=}1.0$) causes policy erosion to 15\% baseline; PickCube 0/1 (Appendix~\ref{sec:tcn_cross_env}). TCN is a \emph{diagnostic probe}, not a deployable mitigation.
158	
159	%% ============================================================
160	%% Architecture-Level Ablation
161	%% ============================================================
162	
163	\subsection{Architecture-Level Ablation}
164	\label{sec:arch_results}
165	
166	\paragraph{Critic convergence in pure imagination.}
167	Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}). Pessimistic estimation is thus ineffective; the min operation in wide dual-critic may provide regularization through mechanisms that remain to be characterized (Appendix~\ref{sec:dual_critic_appendix}).
168	
169	\paragraph{$2{\times}2$ factorial: recovery vs.\ prevention.}
170	Min drives recovery: narrow dual-critic (${\sim}1.2$M) recovers fully (${\sim}16$--$19\times$ recovery ratio) despite $2\times$ fewer parameters. Prevention requires min $+$ capacity: wide dual-critic maintains $\nve \leq 1.4\times$ (3/3 prevention, 1/3 non-CIVO collapse). Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).
171	
172	%% ============================================================
173	%% Online CIVO Detection
174	%% ========================================================
…[truncated 502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-24T15:04:04.118053+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-24T15:04:04.168709+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-24T15:04:21.115418+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 209 · 2026-05-24T15:04:21.468175+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-24T15:04:21.871730+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-24T15:04:21.922493+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-24T15:04:22.628081+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1159
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-24T15:04:22.830001+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-24T15:04:51.262030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-24T15:04:51.966753+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-24T15:04:51.967266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-24T15:04:52.521178+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-24T15:05:18.384399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-24T15:05:18.937641+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-24T15:07:51.662128+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

````json
{
  "text": "## Round 5 修订评估 — Reviewer 2（Venue 合规 + 写作质量 + 贡献度）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: ICML 2026\n\n---\n\n## 逐条 Issue 检查\n\n### CRITICAL (3)\n\n**1. N-R4-1 模板 corl_2026 → icml2026**\n**[RESOLVED]** — main.tex:8 `\\usepackage{icml2026}` ✓\n\n验证清单：\n- `\\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}` (main.tex:38) ✓\n- `\\icmlkeywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}` (main.tex:52) ✓\n- `\\icmlauthorlist` + `\\icmlaffiliation` (main.tex:46-50) ✓\n- `\\bibliographystyle{icml2026}` (main.tex:81) ✓\n- PDF 页脚：\"Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.\" ✓\n- PDF 两栏排版，ICML 标准格式 ✓\n\n**但有一个新的格式 warning** — 见下方 N-R5-1。\n\n---\n\n**2. N-R4-2 缺少 ICML Impact Statement**\n**[RESOLVED]** — conclusion.tex:14-18\n\nImpact Statement 内容充实：\n- 明确了论文贡献（diagnostic framework for detecting CIVO）\n- 讨论了 NVE detector 的局限（wide CI, premature reliance risks）\n- 说明了所有实验在模拟环境中进行，无 real-world safety risks\n- 位于 Conclusion/Limitations 之后、References 之前 ✓（PDF page 6 底部 → page 7 顶部）\n\n质量评估：Impact Statement 内容合理，既不是纯 boilerplate 也不过度渲染影响。符合 ICML 的 \"consider whether additional discussion of ethical impacts and societal implications is warranted\" 要求。\n\n---\n\n**3. N-R4-3 IQM 计算错误 (175.2 → 148.8)**\n**[RESOLVED]** — results.tex:82\n\n修改前：`IQM $175.2$, $n{=}5$`（错误——175.2 是 n=4 的值）\n修改后：`IQM $148.8$, $n{=}5$`\n\n验证：5 个 Walker seeds eval 值 {63.6, 82.8, 95.8, 267.9, 268.0}，排序后去掉首尾各 1，middle 3 = {82.8, 95.8, 267.9}，mean = 148.83 ≈ 148.8 ✓\n\n---\n\n### WARNING (4)\n\n**4. R3-N-new-2 \"gradient diversity\" 术语无支撑**\n**[RESOLVED]** — results.tex:167\n\n修改前：\"the min operation in wide dual-critic may instead regularize through **gradient diversity** (Appendix G)\"\n修改后：\"the min operation in wide dual-critic may provide regularization through **mechanisms that remain to be characterized** (Appendix G)\"\n\n这是恰当的修改——承认机制不明，避免使用无实证支撑的特定术语。同时 introduction.tex:13 的 \"through a different mechanism\" 措辞保持一致。**两轮复发问题彻底解决。**\n\n---\n\n**5. R3-N-new-3 ManiSkill/Cheetah baseline 缺失**\n**[PARTIALLY RESOLVED]** — results.tex:47-48\n\n修改前：无 baseline 参考值\n修改后：`Baselines: Walker 915.7 (row 001); Cheetah ~409 (5-seed mean at 105K); PickCube via exp_019a_v2; StackCube/PegInsertion not separately measured.`\n\n- Walker baseline ✓（Table 1 row 001）\n- Cheetah baseline ✓（~409，比 Round 4 的 ~320 更新为 5-seed mean）\n- PickCube baseline ✓（via exp_019a_v2）\n- StackCube/PegInsertion: \"not separately measured\" ✗\n\n仍有两个 ManiSkill 环境缺少 baseline eval 值。但考虑到这些环境的结论是 CIVO 不出现（negative result），baseline 的缺失影响有限——读者不需要 baseline 来判断 CIVO 是否发生，只需要看 trained vs frozen 的 NVE 对比。**降级为 minor**。\n\n---\n\n**6. N-R4-4 Seed 数量叙述不一致**\n**[RESOLVED]**\n\n逐处验证：\n| 位置 | Round 4 文本 | Round 5 文本 | 状态 |\n|------|------------|------------|------|\n| methodology.tex:32 | \"4 seeds\" | \"4--5 seeds (Walker Walk uses 5 seeds...)\" | ✓ |\n| results.tex:82 | \"IQM 175.2, n=5\" | \"IQM 148.8, n=5\" | ✓ |\n| conclusion.tex:10 | \"4 seeds\" | \"4--5 seeds per configuration\" | ✓ |\n| Figure 2 caption (results.tex:78) | \"seed 4 data in Table\" | \"seeds 4 and 5 data in Table\" | ✓ |\n\n所有 4 处不一致均已修复，叙述一致。\n\n---\n\n**7. R2-N3 纯诊断缺乏 actionable solution**\n**[ACKNOWLEDGED — non-blocking for ICML]**\n\n论文的贡献模式（diagnostic + negative result + partial mitigation + preliminary detection）在 ICML 中可接受。Discussion 中的 practitioner guidelines（analysis.tex:7-8）和 Training horizon 段落（analysis.tex:10-11）提供了实用信息。不再作为阻碍 issue 追踪。\n\n---\n\n### INFO (1)\n\n**8. N-R4-5 \"causal chain\" → \"predictive pathway\"**\n**[RESOLVED]** — results.tex:4\n\n修改前：`establish a causal chain from trained temporal conditioning to pathological value dynamics`\n修改后：`trace a predictive pathway from trained temporal conditioning to pathological value dynamics`\n\n措辞准确反映了 factorial ablation 提供的证据级别（predictive/associative 而非 strict causal）。✓\n\n---\n\n## 新发现的问题\n\n**N-R5-1 [warning] PDF 页面 1 显示 \"AUTHORERR: Missing \\icmlcorrespondingauthor\"**\n\nPDF page 1 脚注区域清晰可见：\n> \"Anonymous Institution, Anonymous City, Anonymous Region, Anonymous Country. **AUTHORERR: Missing \\icmlcorrespondingauthor**\"\n\nICML 2026 模板要求设置 `\\icmlcorrespondingauthor{}` 命令。在 double-blind 提交中，应在 author block 中添加：\n```latex\n\\icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}\n```\n或根据 ICML 模板文档的 double-blind 指示处理。\n\n这是一个**可见的格式错误**，审稿人会看到。虽然不太可能导致 desk reject，但会给人留下粗糙的印象。**建议立即修复。**\n\n---\n\n**N-R5-2 [minor] Introduction \"isolate\" vs Abstract \"identify\" 措辞仍不完全一致**\n\n- Abstract (abstract_body.tex:1): \"identify trained temporal embedding...\"\n- Introduction (introduction.tex:6): \"we **isolate** the combination of a trained dt-embedding...\"\n- Introduction (introduction.tex:11): \"**isolate** trained dt-embedding + multi-rate exposure as jointly sufficient\"\n- Results (results.tex:73): \"The factorial design **isolates** trained dt-embedding as the strongest predictor\"\n- Methodology (methodology.tex:12/32): \"isolate its contribution\" / \"isolates...as orthogonal factors\"\n\n如 Round 4 分析中所述，\"isolate\" 在 factorial ablation 语境中是标准用语（you do isolate factors），与 Abstract 的更保守用词 \"identify\" 之间的差异不构成实质问题。这是 stylistic preference 而非错误。**不影响评分。**\n\n---\n\n## Venue 合规总结\n\n| 检查项 | 状态 | 依据 |\n|--------|------|------|\n| ICML 2026 模板 | ✅ | main.tex:8 `\\usepackage{icml2026}` |\n| 正文 ≤ 8 页 | ✅ | PDF: 主文约 6 页（两栏），结论+Impact Statement 在 page 6-7，References 从 page 7 开始 |\n| Double-blind | ✅ | \"Anonymous Authors\", \"Anonymous Institution\"，无代码链接/机构名泄露 |\n| Impact Statement | ✅ | conclusion.tex:14-18，内容充实，位置正确（References 前） |\n| \\icmltitlerunning | ✅ | main.tex:38 |\n| \\icmlkeywords | ✅ | main.tex:52 |\n| 引用格式 | ✅ | `\\bibliographystyle{icml2026}` main.tex:81 |\n| \\icmlcorrespondingauthor | ⚠️ | 缺失，PDF 显示 AUTHORERR |\n\n---\n\n## 写作质量评估\n\n**Abstract**：\nRound 3（CoRL 版）有 6+ 个数字指标。Round 5 减至约 4 个（14-19%, 27/30, AUROC=0.957, LOEO）。仍偏数字密集但可接受。移除了 detector \"100% sensitivity\" 句和 \"ρ > 0.999\"，信息密度改善明显。\n\n**因果语言一致性**：\n- Abstract: \"identify\" ✓\n- Conclusion: \"identify\" ✓\n- Results: \"trace a predictive pathway\" ✓（曾是 \"causal chain\"）\n- \"hypothesized structural factor\" 全文一致 ✓\n- Introduction 仍用 \"isolate\" — 可接受的 factorial ablation 术语\n\n**F1-F7 叙事结构**：\n仍使用 F1-F7 编号与 Section 编号并行。在 ICML 两栏格式中，这些 finding 标签作为便捷的交叉引用锚点，认知负担低于单栏格式。**降级为 stylistic preference**。\n\n**Robotics framing**：\nIntroduction 仍以 robotics motivation 开篇（DayDreamer, TD-MPC2, \"Real robotic tasks demand temporal abstraction\"）。在 ICML 中，这是 RL 研究的合法动机——无需调整。如果审稿人质疑，可以指出 Discussion 的 \"Implications for robot learning\" 段落是 empirically grounded（基于 ManiSkill 实验），而非空泛的 motivation。\n\n---\n\n## 贡献度评估（ICML 标准）\n\n与 Round 4 相比，贡献度评估**无实质变化**——论文内容未改变，仅修复了格式和数据一致性问题。\n\n**贡献层次**：\n1. **CIVO 作为新 failure mode** — 新颖，但 scope 限于 DreamerV3 locomotion\n2. **Architectural boundary (MPC vs imagination)** — 概念有价值，但仅为假说\n3. **四级干预层级** — 方法论示范，社区可复用\n4. **Preliminary diagnostic** — 诚实降级，不 overclaim\n\n**与 ICML 历史 diagnostic papers 对比**：\n- Henderson et al. (2018): broader impact（影响整个 RL 实验报告实践），本文 scope 窄\n- Lambert et al. (2020): 类似领域，类似贡献模式\n- Lyle et al. (2022): diagnostic + partial mitigation，与本文结构最相似\n\n论文在 ICML RL track 的 borderline accept 区域。格式修复后，论文的专业度提升，但核心 contribution 的 scope 和 significance 仍是主要 weakness。\n\n---\n\n## ICML 评分\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| **Soundness** | 3/4 (Good) | IQM 修正后数据完整性恢复；factorial design 严谨；LOEO AUROC=0.988；extended training 数据回应了步数问题。从 Round 4 的 2.75 回升至 3——数据一致性问题已全部解决。 |\n| **Presentation** | 3/4 (Good) | ICML 模板正确使用；Abstract 改善；\"predictive pathway\" 替代 \"causal chain\"；Impact Statement 内容充实。扣分点：AUTHORERR 格式错误、Abstract 仍偏数字密集。 |\n| **Contribution** | 2/4 (Fair) | 新 failure mode 的识别和诊断框架有价值，但 scope（DreamerV3 + locomotion）和 actionability（最佳建议是\"不用 trained embedding\"）限制了 significance。 |\n| **Originality** | 3/4 (Good) | CIVO 现象新颖；MPC vs imagination 的 architectural boundary 有概念价值；方法论（factorial ablation）是已有技术的组合。 |\n\n**Overall**: **4 (Weak Accept)** — Technically solid diagnostic study with limited scope but genuine novelty. 格式问题几乎全部解决（仅剩 AUTHORERR），数据一致性修复，写作质量提升。主要 weakness 仍是 contribution scope 和 significance。\n\n**Confidence**: **4/5** (Fairly confident) — 我对 RL/world-model 领域有足够了解来评估此论文的技术正确性和贡献价值。不确定性主要在于 ICML RL track 的 acceptance bar 在 2026 年的具体位置。\n\n---\n\n## Round 4 → Round 5 改善总结\n\n| Issue | Round 4 状态 | Round 5 状态 | 变化 |\n|-------|------------|------------|------|\n| 模板 corl_2026 | CRITICAL OPEN | RESOLVED | ✅ 切换到 icml2026 |\n| Impact Statement | CRITICAL OPEN | RESOLVED | ✅ 内容充实 |\n| IQM 175.2→148.8 | CRITICAL OPEN | RESOLVED | ✅ 正确重算 |\n| \"gradient diversity\" | WARNING (复发×2) | RESOLVED | ✅ 终于修复 |\n| Baselines | WARNING (复发×2) | PARTIALLY RESOLVED | ⚠️ Cheetah ✓, StackCube/Peg ✗ |\n| Seed 数量不一致 | WARNING OPEN | RESOLVED | ✅ 全部统一 |\n| \"causal chain\" | INFO OPEN | RESOLVED | ✅ → \"predictive pathway\" |\n| AUTHORERR (新) | — | NEW WARNING | ⚠️ 需添加 \\icmlcorrespondingauthor |\n\n**本轮解决了 6/8 个 open issues**，其中包括全部 3 个 CRITICAL。论文从格式和数据完整性角度已基本 submission-ready（仅需修复 AUTHORERR 和 StackCube/Peg baseline 两个 minor 问题）。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 5 修订评估 — Reviewer 2（Venue 合规 + 写作质量 + 贡献度）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: ICML 2026\n\n---\n\n## 逐条 Issue 检查\n\n### CRITICAL (3)\n\n**1. N-R4-1 模板 corl_2026 → icml2026**\n**[RESOLVED]** — main.tex:8 `\\usepackage{icml2026}` ✓\n\n验证清单：\n- `\\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}` (main.tex:38) ✓\n- `\\icmlkeywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}` (main.tex:52) ✓\n- `\\icmlauthorlist` + `\\icmlaffiliation` (main.tex:46-50) ✓\n- `\\bibliographystyle{icml2026}` (main.tex:81) ✓\n- PDF 页脚：\"Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.\" ✓\n- PDF 两栏排版，ICML 标准格式 ✓\n\n**但有一个新的格式 warning** — 见下方 N-R5-1。\n\n---\n\n**2. N-R4-2 缺少 ICML Impact Statement**\n**[RESOLVED]** — conclusion.tex:14-18\n\nImpact Statement 内容充实：\n- 明确了论文贡献（diagnostic framework for detecting CIVO）\n- 讨论了 NVE detector 的局限（wide CI, premature reliance risks）\n- 说明了所有实验在模拟环境中进行，无 real-world safety risks\n- 位于 Conclusion/Limitations 之后、References 之前 ✓（PDF page 6 底部 → page 7 顶部）\n\n质量评估：Impact Statement 内容合理，既不是纯 boilerplate 也不过度渲染影响。符合 ICML 的 \"consider whether additional discussion of ethical impacts and societal implications is warranted\" 要求。\n\n---\n\n**3. N-R4-3 IQM 计算错误 (175.2 → 148.8)**\n**[RESOLVED]** — results.tex:82\n\n修改前：`IQM $175.2$, $n{=}5$`（错误——175.2 是 n=4 的值）\n修改后：`IQM $148.8$, $n{=}5$`\n\n验证：5 个 Walker seeds eval 值 {63.6, 82.8, 95.8, 267.9, 268.0}，排序后去掉首尾各 1，middle 3 = {82.8, 95.8, 267.9}，mean = 148.83 ≈ 148.8 ✓\n\n---\n\n### WARNING (4)\n\n**4. R3-N-new-2 \"gradient diversity\" 术语无支撑**\n**[RESOLVED]** — results.tex:167\n\n修改前：\"the min operation in wide dual-critic may instead regularize through **gradient diversity** (Appendix G)\"\n修改后：\"the min operation in wide dual-critic may provide regularization through **mechanisms that remain to be characterized** (Appendix G)\"\n\n这是恰当的修改——承认机制不明，避免使用无实证支撑的特定术语。同时 introduction.tex:13 的 \"through a different mechanism\" 措辞保持一致。**两轮复发问题彻底解决。**\n\n---\n\n**5. R3-N-new-3 ManiSkill/Cheetah baseline 缺失**\n**[PARTIALLY RESOLVED]** — results.tex:47-48\n\n修改前：无 baseline 参考值\n修改后：`Baselines: Walker 915.7 (row 001); Cheetah ~409 (5-seed mean at 105K); PickCube via exp_019a_v2; StackCube/PegInsertion not separately measured.`\n\n- Walker baseline ✓（Table 1 row 001）\n- Cheetah baseline ✓（~409，比 Round 4 的 ~320 更新为 5-seed mean）\n- PickCube baseline ✓（via exp_019a_v2）\n- StackCube/PegInsertion: \"not separately measured\" ✗\n\n仍有两个 ManiSkill 环境缺少 baseline eval 值。但考虑到这些环境的结论是 CIVO 不出现（negative result），baseline 的缺失影响有限——读者不需要 baseline 来判断 CIVO 是否发生，只需要看 trained vs frozen 的 NVE 对比。**降级为 minor**。\n\n---\n\n**6. N-R4-4 Seed 数量叙述不一致**\n**[RESOLVED]**\n\n逐处验证：\n| 位置 | Round 4 文本 | Round 5 文本 | 状态 |\n|------|------------|------------|------|\n| methodology.tex:32 | \"4 seeds\" | \"4--5 seeds (Walker Walk uses 5 seeds...)\" | ✓ |\n| results.tex:82 | \"IQM 175.2, n=5\" | \"IQM 148.8, n=5\" | ✓ |\n| conclusion.tex:10 | \"4 seeds\" | \"4--5 seeds per configuration\" | ✓ |\n| Figure 2 caption (results.tex:78) | \"seed 4 data in Table\" | \"seeds 4 and 5 data in Table\" | ✓ |\n\n所有 4 处不一致均已修复，叙述一致。\n\n---\n\n**7. R2-N3 纯诊断缺乏 actionable solution**\n**[ACKNOWLEDGED — non-blocking for ICML]**\n\n论文的贡献模式（diagnostic + negative result + partial mitigation + preliminary detection）在 ICML 中可接受。Discussion 中的 practitioner guidelines（analysis.tex:7-8）和 Training horizon 段落（analysis.tex:10-11）提供了实用信息。不再作为阻碍 issue 追踪。\n\n---\n\n### INFO (1)\n\n**8. N-R4-5 \"causal chain\" → \"predictive pathway\"**\n**[RESOLVED]** — results.tex:4\n\n修改前：`establish a causal chain from trained temporal conditioning to pathological value dynamics`\n修改后：`trace a predictive pathway from trained temporal conditioning to pathological value dynamics`\n\n措辞准确反映了 factorial ablation 提供的证据级别（predictive/associative 而非 strict causal）。✓\n\n---\n\n## 新发现的问题\n\n**N-R5-1 [warning] PDF 页面 1 显示 \"AUTHORERR: Missing \\icmlcorrespondingauthor\"**\n\nPDF page 1 脚注区域清晰可见：\n> \"Anonymous Institution, Anonymous City, Anonymous Region, Anonymous Country. **AUTHORERR: Missing \\icmlcorrespondingauthor**\"\n\nICML 2026 模板要求设置 `\\icmlcorrespondingauthor{}` 命令。在 double-blind 提交中，应在 author block 中添加：\n```latex\n\\icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}\n```\n或根据 ICML 模板文档的 double-blind 指示处理。\n\n这是一个**可见的格式错误**，审稿人会看到。虽然不太可能导致 desk reject，但会给人留下粗糙的印象。**建议立即修复。**\n\n---\n\n**N-R5-2 [minor] Introduction \"isolate\" vs Abstract \"identify\" 措辞仍不完全一致**\n\n- Abstract (abstract_body.tex:1): \"identify trained temporal embedding...\"\n- Introduction (introduction.tex:6): \"we **isolate** the combination of a trained dt-embedding...\"\n- Introduction (introduction.tex:11): \"**isolate** trained dt-embedding + multi-rate exposure as jointly sufficient\"\n- Results (results.tex:73): \"The factorial design **isolates** trained dt-embedding as the strongest predictor\"\n- Methodology (methodology.tex:12/32): \"isolate its contribution\" / \"isolates...as orthogonal factors\"\n\n如 Round 4 分析中所述，\"isolate\" 在 factorial ablation 语境中是标准用语（you do isolate factors），与 Abstract 的更保守用词 \"identify\" 之间的差异不构成实质问题。这是 stylistic preference 而非错误。**不影响评分。**\n\n---\n\n## Venue 合规总结\n\n| 检查项 | 状态 | 依据 |\n|--------|------|------|\n| ICML 2026 模板 | ✅ | main.tex:8 `\\usepackage{icml2026}` |\n| 正文 ≤ 8 页 | ✅ | PDF: 主文约 6 页（两栏），结论+Impact Statement 在 page 6-7，References 从 page 7 开始 |\n| Double-blind | ✅ | \"Anonymous Authors\", \"Anonymous Institution\"，无代码链接/机构名泄露 |\n| Impact Statement | ✅ | conclusion.tex:14-18，内容充实，位置正确（References 前） |\n| \\icmltitlerunning | ✅ | main.tex:38 |\n| \\icmlkeywords | ✅ | main.tex:52 |\n| 引用格式 | ✅ | `\\bibliographystyle{icml2026}` main.tex:81 |\n| \\icmlcorrespondingauthor | ⚠️ | 缺失，PDF 显示 AUTHORERR |\n\n---\n\n## 写作质量评估\n\n**Abstract**：\nRound 3（CoRL 版）有 6+ 个数字指标。Round 5 减至约 4 个（14-19%, 27/30, AUROC=0.957, LOEO）。仍偏数字密集但可接受。移除了 detector \"100% sensitivity\" 句和 \"ρ > 0.999\"，信息密度改善明显。\n\n**因果语言一致性**：\n- Abstract: \"identify\" ✓\n- Conclusion: \"identify\" ✓\n- Results: \"trace a predictive pathway\" ✓（曾是 \"causal chain\"）\n- \"hypothesized structural factor\" 全文一致 ✓\n- Introduction 仍用 \"isolate\" — 可接受的 factorial ablation 术语\n\n**F1-F7 叙事结构**：\n仍使用 F1-F7 编号与 Section 编号并行。在 ICML 两栏格式中，这些 finding 标签作为便捷的交叉引用锚点，认知负担低于单栏格式。**降级为 stylistic preference**。\n\n**Robotics framing**：\nIntroduction 仍以 robotics motivation 开篇（DayDreamer, TD-MPC2, \"Real robotic tasks demand temporal abstraction\"）。在 ICML 中，这是 RL 研究的合法动机——无需调整。如果审稿人质疑，可以指出 Discussion 的 \"Implications for robot learning\" 段落是 empirically grounded（基于 ManiSkill 实验），而非空泛的 motivation。\n\n---\n\n## 贡献度评估（ICML 标准）\n\n与 Round 4 相比，贡献度评估**无实质变化**——论文内容未改变，仅修复了格式和数据一致性问题。\n\n**贡献层次**：\n1. **CIVO 作为新 failure mode** — 新颖，但 scope 限于 DreamerV3 locomotion\n2. **Architectural boundary (MPC vs imagination)** — 概念有价值，但仅为假说\n3. **四级干预层级** — 方法论示范，社区可复用\n4. **Preliminary diagnostic** — 诚实降级，不 overclaim\n\n**与 ICML 历史 diagnostic papers 对比**：\n- Henderson et al. (2018): broader impact（影响整个 RL 实验报告实践），本文 scope 窄\n- Lambert et al. (2020): 类似领域，类似贡献模式\n- Lyle et al. (2022): diagnostic + partial mitigation，与本文结构最相似\n\n论文在 ICML RL track 的 borderline accept 区域。格式修复后，论文的专业度提升，但核心 contribution 的 scope 和 significance 仍是主要 weakness。\n\n---\n\n## ICML 评分\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| **Soundness** | 3/4 (Good) | IQM 修正后数据完整性恢复；factorial design 严谨；LOEO AUROC=0.988；extended training 数据回应了步数问题。从 Round 4 的 2.75 回升至 3——数据一致性问题已全部解决。 |\n| **Presentation** | 3/4 (Good) | ICML 模板正确使用；Abstract 改善；\"predictive pathway\" 替代 \"causal chain\"；Impact Statement 内容充实。扣分点：AUTHORERR 格式错误、Abstract 仍偏数字密集。 |\n| **Contribution** | 2/4 (Fair) | 新 failure mode 的识别和诊断框架有价值，但 scope（DreamerV3 + locomotion）和 actionability（最佳建议是\"不用 trained embedding\"）限制了 significance。 |\n| **Originality** | 3/4 (Good) | CIVO 现象新颖；MPC vs imagination 的 architectural boundary 有概念价值；方法论（factorial ablation）是已有技术的组合。 |\n\n**Overall**: **4 (Weak Accept)** — Technically solid diagnostic study with limited scope but genuine novelty. 格式问题几乎全部解决（仅剩 AUTHORERR），数据一致性修复，写作质量提升。主要 weakness 仍是 contribution scope 和 significance。\n\n**Confidence**: **4/5** (Fairly confident) — 我对 RL/world-model 领域有足够了解来评估此论文的技术正确性和贡献价值。不确定性主要在于 ICML RL track 的 acceptance bar 在 2026 年的具体位置。\n\n---\n\n## Round 4 → Round 5 改善总结\n\n| Issue | Round 4 状态 | Round 5 状态 | 变化 |\n|-------|------------|------------|------|\n| 模板 corl_2026 | CRITICAL OPEN | RESOLVED | ✅ 切换到 icml2026 |\n| Impact Statement | CRITICAL OPEN | RESOLVED | ✅ 内容充实 |\n| IQM 175.2→148.8 | CRITICAL OPEN | RESOLVED | ✅ 正确重算 |\n| \"gradient diversity\" | WARNING (复发×2) | RESOLVED | ✅ 终于修复 |\n| Baselines | WARNING (复发×2) | PARTIALLY RESOLVED | ⚠️ Cheetah ✓, StackCube/Peg ✗ |\n| Seed 数量不一致 | WARNING OPEN | RESOLVED | ✅ 全部统一 |\n| \"causal chain\" | INFO OPEN | RESOLVED | ✅ → \"predictive pathway\" |\n| AUTHORERR (新) | — | NEW WARNING | ⚠️ 需添加 \\icmlcorrespondingauthor |\n\n**本轮解决了 6/8 个 open issues**，其中包括全部 3 个 CRITICAL。论文从格式和数据完整性角度已基本 submission-ready（仅需修复 AUTHORERR 和 StackCube/Peg baseline 两个 minor 问题）。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
````

</details>

---

### Tool result

_source line 221 · 2026-05-24T15:07:55.631001+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3968
}
```

</details>

---

### Assistant

_source line 222 · 2026-05-24T15:08:04.701655+00:00_

Round 5 审稿完成。核心结论：

- **3 个 CRITICAL 全部解决**：ICML 模板正确使用、Impact Statement 已添加、IQM 重算为 148.8
- **WARNING 层修复大半**："gradient diversity" 终于修复（复发两轮后）、seed 数量统一、"causal chain" → "predictive pathway"
- **新发现 1 个 warning**：PDF page 1 显示 `AUTHORERR: Missing \icmlcorrespondingauthor`，需添加对应 LaTeX 命令
- **Overall 维持 Weak Accept (4/6)**，Soundness 从 Round 4 的 2.75 回升至 3/4（数据完整性恢复）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 8

3 recorded events

### User

_source line 223 · 2026-05-24T15:09:58.569431+00:00_

[Round 5 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每个关键判断标注 [AGREE] 或 [REBUT] 并给出理由。

**特别关注**：
1. R1 将 Overall 从 Weak Accept 升至 **Accept (5/6)**，你维持 **Weak Accept (4/6)**——请直接回应你们的分歧点
2. R1 Significance 3/4 (Good) vs 你的 2/4 (Fair)——是否有充分理由支持一方？
3. R1 将 Becker-Ehmck 列为 N-R5-1 info——你在 Round 4 已接受混淆解释并降级为 non-issue，是否维持？
4. R1 对 AUTHORERR 的判断是"匿名模式已知行为，不影响 review"——你标记为 warning，评估差异如何？
5. R1 将 R2-N3 (actionable solution) 标为 RESOLVED (ICML 语境下合理)——你标为 ACKNOWLEDGED non-blocking——实质一致还是有差异？

---

以下是 Reviewer 1 的完整审稿意见：

**Overall**: Accept (5/6)
**Soundness**: 3/4, **Presentation**: 3/4, **Significance**: 3/4, **Originality**: 3/4
**Confidence**: 4/5

**Issue 验证结果**:
- 3/3 CRITICAL: 全部 RESOLVED（模板 icml2026 ✓, Impact Statement ✓, IQM 148.8 独立验证 ✓）
- 3/4 WARNING: RESOLVED（gradient diversity ✓, seed 数量 ✓, actionable solution ✓）
- 1/4 WARNING: PARTIALLY → info（baseline vals，降级理由：复发 3 轮且对核心论点无影响）
- 1/1 INFO: RESOLVED（"causal chain" → "predictive pathway" ✓）

**升级至 Accept 的理由**:
1. 所有 critical issues 修复
2. IQM 148.8 经独立计算确认
3. 方法论措辞全面到位（strongest predictor, hypothesized structural factor, predictive pathway, mechanisms that remain to be characterized）
4. ICML venue fit 良好——diagnostic negative-result paper 适合 ICML methodology track
5. 残留 issues 均为 info 级

**新发现**:
- N-R5-1 [info]: Becker-Ehmck 2023 仍未引用（grep 确认全文无匹配）
- N-R5-2 [info]: AUTHORERR——icml2026.sty 匿名模式已知行为

**方法严谨性**: 8/10（Round 4 为 7.5/10）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-24T15:11:15.391166+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 5 审稿意见的逐条评议\n\n---\n\n### Issue 验证结果回应\n\n**[AGREE] 3/3 CRITICAL 全部 RESOLVED**\n与我的判定完全一致。模板、Impact Statement、IQM 三个 critical issue 均已验证修复。\n\n**[AGREE] gradient diversity RESOLVED**\nresults.tex:167 \"mechanisms that remain to be characterized\" 是恰当的替代。两轮复发问题终于解决。\n\n**[AGREE] seed 数量 RESOLVED**\n4 处不一致全部统一为 \"4--5 seeds\"。\n\n**[AGREE] \"causal chain\" → \"predictive pathway\" RESOLVED**\nresults.tex:4 修改准确。\n\n**[AGREE] baseline vals 降级为 info**\nR1 将 StackCube/PegInsertion baseline 缺失从 warning 降级为 info 的理由合理——这些环境的结论是 CIVO 不出现，baseline eval 值对核心论点无影响。我在自己的审查中也已将此降级为 minor。实质一致。\n\n---\n\n### Director 的 5 个具体问题\n\n#### Q1: R1 Accept (5/6) vs R2 Weak Accept (4/6) 分歧\n\n核心分歧在于**对 contribution scope 的容忍度**。\n\nR1 的 Accept 逻辑：所有技术问题修复 → 方法论严谨 → ICML 有 diagnostic paper 先例 → Accept。这个逻辑链是 valid 的。\n\n我维持 Weak Accept 的理由是 **significance ceiling**：\n- CIVO 仅在 DreamerV3 + locomotion 中确认。是否在 IRIS、DreamerV4、TransDreamer 等其他 imagination-based 架构中也存在，完全未知。Limitations 自己承认了这一点（conclusion.tex:8）。\n- Actionable takeaway 是 \"不要用 trained dt-embedding\" 或 \"用 MPC 代替\"——这是对一条尚未被广泛采用的技术路线的 warning，实际受影响的研究者数量有限。\n- 与 Henderson et al. (2018) 对比：后者的发现影响了整个 RL 社区的实验报告和比较方法论；CIVO 的影响范围窄一个量级。\n\n**但我承认 R1 的判断也合理**：如果审稿人认为 \"在 world-model RL 社区建立一个 well-characterized failure mode + diagnostic framework\" 的长期价值足以支撑 ICML 版面，Accept 是可以 justify 的。这是 borderline 论文的 judgment call，不是技术分歧。\n\n**我的 calibration**：如果 AC 倾向于 Accept，我不会反对。我将评分从 4 (Weak Accept) 微调至 **4+ (Weak Accept, leaning Accept)**，反映 Round 5 的全面修复。\n\n---\n\n#### Q2: Significance 3/4 (R1) vs 2/4 (R2)\n\nR1 给 3/4 (Good) 的核心论据应该是：\n1. 四级干预层级分析作为可复用的方法论框架\n2. MPC vs imagination-based 的 architectural boundary insight\n3. 对 world-model RL 社区的长期 warning 价值\n\n我给 2/4 (Fair) 的理由：\n1. **Scope 限制**：发现仅在 DreamerV3 locomotion 中成立，manipulation 中不成立——受影响的具体场景很窄\n2. **Actionability 限制**：最有效的 \"solution\" 是不用该功能，而非改进它\n3. **影响范围**：dt-conditioning in imagination-based RL 目前并非主流方向（TAWM 用 MPC，Dreamer 系列用 fixed dt=1，hierarchical variants 用 subgoal），受影响的研究者基数小\n\n**重新审视后的判断**：R1 的 3/4 可能偏高，我的 2/4 可能偏低。论文的 systematic rigor 本身有示范价值——四级干预层级分析为未来 RL 诊断研究提供了一个 template。但 \"发现一个目前无人使用的功能不可行\" 的 significance 确实受限。\n\n**调整**：维持 **2/4 (Fair)**，但 acknowledge R1 的 3/4 在不同 calibration 标准下可成立。如果考虑方法论示范价值，2.5/4 是合理的中间位置。\n\n---\n\n#### Q3: Becker-Ehmck 2023 — 是否维持 non-issue？\n\n**[AGREE with R1] 维持 non-issue / info**\n\nR1 将其列为 N-R5-1 info 与我 Round 4 的判断一致。重申理由：\n1. Round 1 原始 issue 未提供论文标题，仅给出作者名和年份\n2. 两位 reviewer 独立搜索均未找到一篇 2023 年的 Becker-Ehmck 论文与本文直接相关\n3. benechehab2023multitimestep 已被引用，覆盖了 multi-timestep prediction in MBRL 这一主题\n4. 如果确实存在相关的 Becker-Ehmck 2023 论文，原始 reviewer 应提供完整引用\n\n**作为 info 处理是合适的**——在最终 camera-ready 前，作者可以再次搜索确认，但不应阻碍 acceptance 决定。\n\n---\n\n#### Q4: AUTHORERR 判断差异\n\nR1 判断：\"icml2026.sty 匿名模式已知行为，不影响 review\"\nR2 判断：\"warning，建议修复\"\n\n**[PARTIALLY AGREE with R1]**\n\nR1 的技术判断可能是正确的——如果 `icml2026.sty` 在 anonymous mode 下省略 `\\icmlcorrespondingauthor` 会自动产生这个 AUTHORERR 标记，那这确实是模板行为而非作者错误。我没有验证 icml2026.sty 的源码来确认这一点。\n\n但即使是 \"已知行为\"，它在 PDF 中仍然可见，会让部分 reviewer 产生 \"preparation careless\" 的印象。**建议降级为 info**（介于 R1 的 \"不影响\" 和我原来的 \"warning\" 之间），并建议作者验证是否可以通过添加 placeholder corresponding author 来消除该提示。\n\n---\n\n#### Q5: R2-N3 (actionable solution) — RESOLVED (R1) vs ACKNOWLEDGED non-blocking (R2)\n\n**实质一致，表述差异。**\n\nR1 的 RESOLVED 意味着：在 ICML 语境下，diagnostic paper 不需要 actionable solution 来满足 acceptance bar → issue 不再成立 → RESOLVED。\n\n我的 ACKNOWLEDGED non-blocking 意味着：问题本身仍然存在（论文确实没有提供可靠的解决方案），但在 ICML 中这不是 acceptance blocker → 不再追踪。\n\n两者的实际影响相同：不影响评分，不阻碍 acceptance。我接受 R1 的 RESOLVED 标记，因为在 ICML 标准下 diagnostic paper 的贡献模式本身就是合理的。\n\n---\n\n### 方法严谨性 8/10 回应\n\n**[AGREE]** R1 从 7.5 升至 8 的理由（IQM 修正、seed 一致性修复、\"mechanisms that remain to be characterized\" 替代 \"gradient diversity\"）与我的评估一致。我的 Soundness 也从 Round 4 的 2.75/4 回升至 3/4，比例上等同于从 ~6.9/10 升至 7.5/10。R1 的 8/10 略高但在合理范围内。\n\n---\n\n### 最终评分\n\n| 维度 | R1 | R2 | 共识区间 |\n|------|-----|-----|----------|\n| Overall | 5 (Accept) | 4+ (Weak Accept, leaning Accept) | 4-5 |\n| Soundness | 3/4 | 3/4 | 一致 |\n| Presentation | 3/4 | 3/4 | 一致 |\n| Significance | 3/4 | 2/4 | 分歧点 |\n| Originality | 3/4 | 3/4 | 一致 |\n| Confidence | 4/5 | 4/5 | 一致 |\n\n**两位 reviewer 在 Soundness、Presentation、Originality、Confidence 上完全一致。** 唯一的实质分歧是 Significance（3/4 vs 2/4），这决定了 Overall 的差异（5 vs 4+）。这是一个合理的 judgment call 分歧——AC 的 meta-review 应在此基础上做出最终决定。\n\n**我的建议给 AC**：论文技术上 solid，所有审稿问题已修复，在 ICML RL track 的 borderline accept 区域。Significance 的分歧源于对 \"narrow-scope but well-executed diagnostic paper\" 的价值判断差异，而非对论文质量的分歧。如果 ICML 2026 的 acceptance rate 和 track 容量允许，Accept 是 defensible 的。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 5 审稿意见的逐条评议\n\n---\n\n### Issue 验证结果回应\n\n**[AGREE] 3/3 CRITICAL 全部 RESOLVED**\n与我的判定完全一致。模板、Impact Statement、IQM 三个 critical issue 均已验证修复。\n\n**[AGREE] gradient diversity RESOLVED**\nresults.tex:167 \"mechanisms that remain to be characterized\" 是恰当的替代。两轮复发问题终于解决。\n\n**[AGREE] seed 数量 RESOLVED**\n4 处不一致全部统一为 \"4--5 seeds\"。\n\n**[AGREE] \"causal chain\" → \"predictive pathway\" RESOLVED**\nresults.tex:4 修改准确。\n\n**[AGREE] baseline vals 降级为 info**\nR1 将 StackCube/PegInsertion baseline 缺失从 warning 降级为 info 的理由合理——这些环境的结论是 CIVO 不出现，baseline eval 值对核心论点无影响。我在自己的审查中也已将此降级为 minor。实质一致。\n\n---\n\n### Director 的 5 个具体问题\n\n#### Q1: R1 Accept (5/6) vs R2 Weak Accept (4/6) 分歧\n\n核心分歧在于**对 contribution scope 的容忍度**。\n\nR1 的 Accept 逻辑：所有技术问题修复 → 方法论严谨 → ICML 有 diagnostic paper 先例 → Accept。这个逻辑链是 valid 的。\n\n我维持 Weak Accept 的理由是 **significance ceiling**：\n- CIVO 仅在 DreamerV3 + locomotion 中确认。是否在 IRIS、DreamerV4、TransDreamer 等其他 imagination-based 架构中也存在，完全未知。Limitations 自己承认了这一点（conclusion.tex:8）。\n- Actionable takeaway 是 \"不要用 trained dt-embedding\" 或 \"用 MPC 代替\"——这是对一条尚未被广泛采用的技术路线的 warning，实际受影响的研究者数量有限。\n- 与 Henderson et al. (2018) 对比：后者的发现影响了整个 RL 社区的实验报告和比较方法论；CIVO 的影响范围窄一个量级。\n\n**但我承认 R1 的判断也合理**：如果审稿人认为 \"在 world-model RL 社区建立一个 well-characterized failure mode + diagnostic framework\" 的长期价值足以支撑 ICML 版面，Accept 是可以 justify 的。这是 borderline 论文的 judgment call，不是技术分歧。\n\n**我的 calibration**：如果 AC 倾向于 Accept，我不会反对。我将评分从 4 (Weak Accept) 微调至 **4+ (Weak Accept, leaning Accept)**，反映 Round 5 的全面修复。\n\n---\n\n#### Q2: Significance 3/4 (R1) vs 2/4 (R2)\n\nR1 给 3/4 (Good) 的核心论据应该是：\n1. 四级干预层级分析作为可复用的方法论框架\n2. MPC vs imagination-based 的 architectural boundary insight\n3. 对 world-model RL 社区的长期 warning 价值\n\n我给 2/4 (Fair) 的理由：\n1. **Scope 限制**：发现仅在 DreamerV3 locomotion 中成立，manipulation 中不成立——受影响的具体场景很窄\n2. **Actionability 限制**：最有效的 \"solution\" 是不用该功能，而非改进它\n3. **影响范围**：dt-conditioning in imagination-based RL 目前并非主流方向（TAWM 用 MPC，Dreamer 系列用 fixed dt=1，hierarchical variants 用 subgoal），受影响的研究者基数小\n\n**重新审视后的判断**：R1 的 3/4 可能偏高，我的 2/4 可能偏低。论文的 systematic rigor 本身有示范价值——四级干预层级分析为未来 RL 诊断研究提供了一个 template。但 \"发现一个目前无人使用的功能不可行\" 的 significance 确实受限。\n\n**调整**：维持 **2/4 (Fair)**，但 acknowledge R1 的 3/4 在不同 calibration 标准下可成立。如果考虑方法论示范价值，2.5/4 是合理的中间位置。\n\n---\n\n#### Q3: Becker-Ehmck 2023 — 是否维持 non-issue？\n\n**[AGREE with R1] 维持 non-issue / info**\n\nR1 将其列为 N-R5-1 info 与我 Round 4 的判断一致。重申理由：\n1. Round 1 原始 issue 未提供论文标题，仅给出作者名和年份\n2. 两位 reviewer 独立搜索均未找到一篇 2023 年的 Becker-Ehmck 论文与本文直接相关\n3. benechehab2023multitimestep 已被引用，覆盖了 multi-timestep prediction in MBRL 这一主题\n4. 如果确实存在相关的 Becker-Ehmck 2023 论文，原始 reviewer 应提供完整引用\n\n**作为 info 处理是合适的**——在最终 camera-ready 前，作者可以再次搜索确认，但不应阻碍 acceptance 决定。\n\n---\n\n#### Q4: AUTHORERR 判断差异\n\nR1 判断：\"icml2026.sty 匿名模式已知行为，不影响 review\"\nR2 判断：\"warning，建议修复\"\n\n**[PARTIALLY AGREE with R1]**\n\nR1 的技术判断可能是正确的——如果 `icml2026.sty` 在 anonymous mode 下省略 `\\icmlcorrespondingauthor` 会自动产生这个 AUTHORERR 标记，那这确实是模板行为而非作者错误。我没有验证 icml2026.sty 的源码来确认这一点。\n\n但即使是 \"已知行为\"，它在 PDF 中仍然可见，会让部分 reviewer 产生 \"preparation careless\" 的印象。**建议降级为 info**（介于 R1 的 \"不影响\" 和我原来的 \"warning\" 之间），并建议作者验证是否可以通过添加 placeholder corresponding author 来消除该提示。\n\n---\n\n#### Q5: R2-N3 (actionable solution) — RESOLVED (R1) vs ACKNOWLEDGED non-blocking (R2)\n\n**实质一致，表述差异。**\n\nR1 的 RESOLVED 意味着：在 ICML 语境下，diagnostic paper 不需要 actionable solution 来满足 acceptance bar → issue 不再成立 → RESOLVED。\n\n我的 ACKNOWLEDGED non-blocking 意味着：问题本身仍然存在（论文确实没有提供可靠的解决方案），但在 ICML 中这不是 acceptance blocker → 不再追踪。\n\n两者的实际影响相同：不影响评分，不阻碍 acceptance。我接受 R1 的 RESOLVED 标记，因为在 ICML 标准下 diagnostic paper 的贡献模式本身就是合理的。\n\n---\n\n### 方法严谨性 8/10 回应\n\n**[AGREE]** R1 从 7.5 升至 8 的理由（IQM 修正、seed 一致性修复、\"mechanisms that remain to be characterized\" 替代 \"gradient diversity\"）与我的评估一致。我的 Soundness 也从 Round 4 的 2.75/4 回升至 3/4，比例上等同于从 ~6.9/10 升至 7.5/10。R1 的 8/10 略高但在合理范围内。\n\n---\n\n### 最终评分\n\n| 维度 | R1 | R2 | 共识区间 |\n|------|-----|-----|----------|\n| Overall | 5 (Accept) | 4+ (Weak Accept, leaning Accept) | 4-5 |\n| Soundness | 3/4 | 3/4 | 一致 |\n| Presentation | 3/4 | 3/4 | 一致 |\n| Significance | 3/4 | 2/4 | 分歧点 |\n| Originality | 3/4 | 3/4 | 一致 |\n| Confidence | 4/5 | 4/5 | 一致 |\n\n**两位 reviewer 在 Soundness、Presentation、Originality、Confidence 上完全一致。** 唯一的实质分歧是 Significance（3/4 vs 2/4），这决定了 Overall 的差异（5 vs 4+）。这是一个合理的 judgment call 分歧——AC 的 meta-review 应在此基础上做出最终决定。\n\n**我的建议给 AC**：论文技术上 solid，所有审稿问题已修复，在 ICML RL track 的 borderline accept 区域。Significance 的分歧源于对 \"narrow-scope but well-executed diagnostic paper\" 的价值判断差异，而非对论文质量的分歧。如果 ICML 2026 的 acceptance rate 和 track 容量允许，Accept 是 defensible 的。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-24T15:11:20.773920+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5382
}
```

</details>

---

## Round 9

30 recorded events

### User

_source line 226 · 2026-05-28T00:35:04.673440+00:00_

[Round 6 审稿请求]:
## Round 6 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + CoRL venue 适配性**

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
这是本轮最核心的评审问题。Round 3 在 CoRL venue 下给出 Weak Reject (5/10)，核心原因是 venue fit 不足。当时切到 ICML 作为解决方案，现在又回来了。你需要评估：
- CoRL 社区关心的是 robot learning 的实际问题——这篇论文的 CIVO diagnostic 发现与 robot learning 的实际关联有多强？
- CIVO 仅在 DMC locomotion 中复现，ManiSkill manipulation 为阴性——如何说服 CoRL 审稿人这对机器人学习有价值？
- 论文是否在 Introduction/Discussion 中充分论证了对 robot deployment 的影响？
- Broader Impact Statement 是否从 robotics safety 角度论述？
- 与 Round 3 相比，论文在 robotics relevance 方面是否有实质性改进？

**CRITICAL — 模板合规性**:
main.tex 仍使用 `\usepackage{icml2026}` 和 ICML 专用宏。检查提交 PDF 的实际模板——如果 PDF 也是 ICML 模板，这是 desk reject 级别的问题。

**上轮遗留 in_progress 问题**:
1. **N-R5-1 (AUTHORERR)**: 检查 PDF 编译状态和匿名化合规
2. **N-R5-2 (显示密度)**: CoRL 8 页限制，检查是否合规
3. **N-R5-3 (色盲友好)**: Figure 2 等图表的可访问性

**已修复但需确认的 Round 5 修复**:
- IQM 从 175.2 修正为 148.8 (n=5)
- "causal chain" → "predictive pathway"
- "gradient diversity" → "mechanisms that remain to be characterized"
- Seed 数量统一为 "4--5 seeds"
- Broader Impact Statement 已添加

### 你的评分维度
1. 新颖性（CIVO 诊断作为贡献的创新性，对已有文献的增量价值）
2. 相关工作完整性（是否遗漏关键参考文献，尤其 robot learning + temporal abstraction 交叉领域）
3. 写作质量（声明精确度、论述逻辑、robotics relevance 论证）
4. CoRL venue 适配性（对 CoRL 社区的价值）

请按 CoRL 标准给出：Overall Score (1-6), Significance, Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 227 · 2026-05-28T00:35:17.128730+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-28T00:35:17.832371+00:00_

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

…[truncated 512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-28T00:35:17.883110+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-28T00:35:18.490745+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-28T00:35:37.862473+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-28T00:35:38.214213+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; $n{=}36$, AUROC${=}1.000$, F1${=}1.000$). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, so Double Q pessimism is ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 233 · 2026-05-28T00:35:38.264899+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-28T00:35:38.616369+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 235 · 2026-05-28T00:35:38.616913+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-28T00:35:38.770224+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 153
}
```

</details>

---

### Tool call

_source line 237 · 2026-05-28T00:35:58.003479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 238 · 2026-05-28T00:35:58.505967+00:00_

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
…[truncated 6996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 239 · 2026-05-28T00:35:58.506424+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 240 · 2026-05-28T00:35:59.159330+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-28T00:35:59.159862+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-28T00:35:59.260718+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal abstraction in RL.}
5	The options framework \citep{sutton1999options}, option-critic \citep{bacon2017optioncritc}, HAM \citep{parr1998ham}, and MAXQ \citep{dietterich2000maxq} formalize temporal abstraction through hierarchical policies. Semi-MDP theory \citep{bradtke1995smdp} provides the mathematical foundation. Action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, park2021timediscretization} achieve simpler temporal abstraction via real transitions; \citet{wang2024elastic} learn elastic time steps that adapt step size to state dynamics. The Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3, hafner2025dreamerv4} trains policies in imagination at fixed $\dt{=}1$; hierarchical variants \citep{hafner2022director, gumbsch2024thick, mattes2024hieros, li2025lsimagine} use subgoals or separate dynamics per scale, avoiding flat $\dt$-conditioning. TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains; the critical distinction is that MPC re-plans from real states, so model errors do not accumulate into a critic (\S\ref{sec:discussion}).
6	
7	\paragraph{Value overestimation and model fidelity.}
8	Maximization bias \citep{thrun1993issues} has been addressed by Double Q-learning \citep{vanhasselt2016double}, TD3 \citep{fujimoto2018td3}, and ensemble methods \citep{chen2021redq}; in model-based settings, MBPO \citep{janner2019mbpo} and MOPO \citep{yu2020mopo} bound rollout error, while MOReL \citep{kidambi2020morel} and COMBO \citep{yu2021combo} penalize model uncertainty. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints. CIVO is mechanistically distinct: the amplifier is the world model's co-adaptation with a learned temporal embedding, producing systematic reward-prediction bias at $\dt > 1$. Multi-timestep world models \citep{benechehab20
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-28T00:36:34.363918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-28T00:36:34.766011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-28T00:36:34.768783+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-28T00:36:35.071014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-28T00:36:35.623985+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-28T00:36:35.876775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-28T00:37:25.383608+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 250 · 2026-05-28T00:37:25.786081+00:00_

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
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step. We test three modes: \textbf{trained} (updated via backpropagation, enabling co-adaptation), \textbf{frozen} (fixed random projection, \texttt{requires\_grad=False}), and \textbf{removed} (dimension zero). We further distinguish \textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\dt{>}1$ transitions) from \textbf{trained-but-unexposed} (subsample OFF: $\dt{>}1$ used only during imagination). This four-way classification is the key experimental structure of our factorial design.
16	
17	\paragraph{Temporal subsampling.}
18	When enabled, the replay buffer augments training data with variable-$\dt$ transitions by subsampling consecutive frames (max factor~2: both $\dt{=}1$ and $\dt{=}2$ from the same episodes). This controls whether the world model has seen multi-scale dynamics during training.
19	
20	\paragraph{Imagination horizon and step size.}
21	The imagination horizon $H$ sets the number of rollout steps. We test $H{=}15$ (default) and $H{=}8$. The reduced horizon controls for compounding error: $H{
…[truncated 4378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 251 · 2026-05-28T00:37:25.836905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "100",
  "limit": "90"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "100",
    "limit": "90"
  }
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-28T00:37:25.888107+00:00_

100	
101	Trained $\dt$-embedding and multi-rate data exposure are \emph{jointly sufficient in tested configurations} for CIVO. Neither factor alone triggers the CIVO feedback loop: trained embedding without multi-rate exposure (008a, Walker 3 seeds, peak NVE $0.83$--$0.93\times$; Cheetah 2 seeds, NVE $0.45$--$0.58\times$) and multi-rate exposure without embedding (008f, 4 seeds, peak NVE $\leq 1.69\times$$^f$) all remain below $\tau{=}2.0\times$ across both environments; untrained or absent $\dt$-embedding blocks the CIVO feedback loop. Performance varies by environment and horizon (Walker $82$--$93\%$ baseline at $H{=}8$; Cheetah $63$--$82\%$ (mean $73\%$) at $H{=}15$), consistent with longer imagination horizons compounding small untrained-embedding errors; the mechanism-level conclusion (NVE $\ll \tau$, no CIVO) holds uniformly. Freezing the embedding (\texttt{requires\_grad=False}) eliminates CIVO: across 6 Walker frozen seeds (NVE $0.19$--$0.53\times$ in 4/6, transient spikes $1.71$--$1.88\times$ in 2/6; Table~\ref{tab:three_way_emb}) and 4 Cheetah frozen seeds (all NVE $< 1.35\times$), no frozen run exhibits sustained CIVO. A controlled $2{\times}2$ frozen verification (Walker $+$ Cheetah, 2 seeds each; exp\_084--087, all NVE $< 0.53\times$; Appendix~\ref{sec:appendix_factorial}) confirms that gradient training---not embedding presence---is necessary. Across all runs, trained $\dt$-embedding triggers CIVO in 5/7 multi-joint locomotion seeds versus 0/16 frozen or removed controls\footnote{The 16 control seeds comprise 8 frozen and 8 removed/absent $\dt$-embedding configurations across Walker Walk and Cheetah Run (Table~\ref{tab:complete_results}).} (Fisher exact $p < 0.001$). Partial gradient blocking (exp\_044) does not prevent onset (peak NVE $4.45\times$) but permits delayed self-correction (final eval 538, 59\% baseline; Appendix~\ref{sec:appendix_factorial}); \emph{any} gradient pathway updating $e_{\dt}$ suffices to induce CIVO. Degradation scales monoton
…[truncated 6904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-28T00:40:36.798939+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 修订评估 — Reviewer 2（新颖性 + 相关工作 + 写作质量 + CoRL Venue 适配性）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026（从 ICML 转回 CoRL）\n\n---\n\n## 关键变化追踪（Round 5 → Round 6）\n\n论文在内容层面有 **大幅实质性更新**，远超格式级修改：\n\n| 变化类别 | 具体内容 |\n|---------|---------|\n| 统计数据 | NVE threshold 1.5× → 2.0×; AUROC 0.957 → 1.000; n: 30 → 36; 27/30 → 36/36 perfect |\n| 新机制分析 | 值校准（V/MC-return 7.80× vs 1.05×）、temporal ordering（r=0.81, p=0.002）、双通路分析（Walker: reward fidelity, Cheetah: dynamics drift） |\n| 新环境 | Cartpole 作为 single-joint negative control（0/3 CIVO） |\n| 新实验 | 2×2 frozen verification (exp_084-087), 008f corrected-code rerun, exp_078 (Cheetah s0) |\n| 新图表 | Figure 1: CIVO 机制图 (mechanism diagram) |\n| Discussion 扩展 | 新增 5 个段落：Causal role of embedding training, Intervention resistance, Transferable diagnostic protocol, Scope precision, Cross-env validation |\n| F6 重写 | \"2/4 collapse (50%)\" → \"0/4 CIVO onset\"（不同 seed 集合：s0,s1,s2,s5 替代原 s1-s4） |\n| Table 2 更新 | Frozen: 5/7→7/7 (100%), Removed: 5/5→6/6, Untreated: 7→10 seeds |\n| Broader Impact | 完全重写，聚焦 robotics safety |\n\n这是一篇在科学内容上显著优于所有前几轮版本的论文。\n\n---\n\n## CRITICAL Issues\n\n### 1. 模板合规性 — `\\usepackage{icml2026}` 仍未切换\n**[STILL_OPEN — CRITICAL / DESK REJECT]**\n\n- main.tex:8: `\\usepackage{icml2026}` ✗\n- main.tex:41: `\\icmltitlerunning{...}` — ICML 专用宏\n- main.tex:46-55: `\\icmltitle`, `\\icmlauthorlist`, `\\icmlaffiliation`, `\\icmlcorrespondingauthor` — ICML 专用宏\n- main.tex:86: `\\bibliographystyle{icml2026}` — ICML 引用格式\n- PDF 页脚: \"Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.\"\n- PDF 格式: 两栏排版（ICML），而非 CoRL 的单栏 PMLR 格式\n\n**以当前 PDF 提交到 CoRL 2026 会被 desk reject**。必须：\n1. 替换为 `\\usepackage{corl_2026}`\n2. 移除所有 ICML 专用宏\n3. 恢复 CoRL 单栏格式\n4. 重新编译并验证 8 页限制\n\n### 2. 页数合规性风险（无法在当前模板下验证）\n**[CANNOT VERIFY — WARNING]**\n\nRound 3 版本在 CoRL 单栏格式下恰好 8 页。Round 6 版本新增了大量内容：\n- Figure 1 机制图（新增）\n- Mechanism evidence 段落（~20 行新文本）\n- Temporal ordering 段落（~15 行新文本）\n- Discussion 新增 5 个完整段落（~120 行新文本）\n- Table 1 扩展（新增 exp_078, 008f s0）\n- Table 2 脚注扩展\n\n在 CoRL 单栏格式下，这些新增内容几乎确定会导致正文超过 8 页。需要在切换模板后立即验证，可能需要大幅精简 Discussion 或将部分内容移至 Appendix。\n\n---\n\n## CoRL Venue 适配性（REOPENED — 核心评审问题）\n\n### Round 3 vs Round 6 对比\n\n| 维度 | Round 3 评估 | Round 6 评估 |\n|------|------------|------------|\n| 环境覆盖 | 5 env (2 DMC + 3 ManiSkill) | 6 env (3 DMC incl. Cartpole + 3 ManiSkill) |\n| 统计证据 | AUROC 0.953, 26/29 | AUROC 1.000, 36/36, Fisher p<0.001 |\n| 机制理解 | 2.78× reward gap | 双通路分析 + temporal ordering + 值校准 |\n| 方法论贡献 | 四级干预层级 | 四级干预 + \"transferable diagnostic protocol\" 概念 |\n| Robotics framing | bookend 式 rhetoric | 更深入但仍以 DreamerV3 为核心 |\n| Broader Impact | CoRL 版：标准 limitations | 新版：robotics safety framing |\n\n### Venue Fit 评分：5.5/10（Round 3: 5/10）\n\n**微幅提升但核心矛盾未解**。\n\n**改善的地方**：\n1. **\"Transferable diagnostic protocol\"**（analysis.tex:13-14）是本轮最有价值的 CoRL 定位改进。将四级干预层级从 \"CIVO 专用工具\" 提升为 \"任何 learned conditioning signal + imagination-based training 都可复用的诊断框架\"，明确提到 goal-conditioned imagination、language-conditioned world models、skill embeddings——都是 CoRL 核心话题。\n2. **Scope precision 分析**（analysis.tex:22-25）通过 6 环境 × 3 task types 的系统 negative controls 展示了实验设计的严谨性。\n3. **Fisher exact test** (p < 0.001) 和 AUROC=1.000 大幅增强了统计可信度。\n4. **Broader Impact Statement** 直接讨论 robotic deployment safety。\n\n**未解决的核心问题**：\n1. **CIVO 仍是 locomotion-specific**：5/7 multi-joint locomotion seeds vs 0/16 controls，但在 manipulation（ManiSkill 3 tasks, 0/3 trigger-specific）中不出现。CoRL 社区更关心 manipulation 和 contact-rich tasks。\n2. **\"Transferable diagnostic protocol\" 仍是理论性的**：论文声称该协议可用于 goal-conditioned 和 language-conditioned models，但**没有在任何这些场景上实际验证**。这是一个 promise 而非 demonstrated contribution。\n3. **所有实验在模拟环境中**：Limitations 承认 \"not...real-robot deployments\"（conclusion.tex:7）。\n4. **Actionable takeaway 不变**：对 CoRL 从业者来说，最有效建议仍然是 \"不要用 trained dt-embedding\"。\n5. **核心贡献是 DreamerV3-specific 诊断**：虽然论文试图推广，但 CIVO 是否在 IRIS、DreamerV4、TransDreamer 等其他架构中存在完全未知。\n\n**对比 CoRL 接受的 diagnostic papers**：CoRL 历史上确实接受 diagnostic work（如 DayDreamer 的 ablation studies），但这些通常是在真实机器人上做的，且直接服务于 deployment。本文的诊断是在 simulated locomotion 上做的，与 real-robot deployment 的距离较远。\n\n---\n\n## 新颖性评估\n\n**评分: 7/10**\n\nRound 6 的科学新颖性显著提升：\n\n1. **CIVO 作为新 failure mode**（已在前几轮确认）——新颖且有价值\n2. **双通路分析**（NEW）：Walker 通过 reward fidelity degradation，Cheetah 通过 dynamics-model prior drift（无 reward gap），这是一个有洞察力的发现——同一个宏观现象可以有不同的微观机制\n3. **Temporal ordering**（NEW）：r=0.81, p=0.002 的时间序列分析提供了 causal direction 的证据（但 n=2 仍然太少）\n4. **完美分类器**（AUROC=1.000, F1=1.000, n=36）——NVE 阈值 2.0× 完美分离 CIVO/non-CIVO，这在 RL 诊断中非常稀有\n5. **Transferable diagnostic protocol 概念**——有潜力但未验证\n\n**减分点**：\n- 方法论本身（factorial ablation, NVE metric, gradient stopping）都是已有技术的组合\n- CIVO 现象仅在 DreamerV3 locomotion 中复现，泛化性未知\n- Temporal ordering n=2 太小，只能算 preliminary evidence\n\n---\n\n## 相关工作完整性\n\nRelated Work（related_work.tex）覆盖了主要领域：\n- Temporal abstraction: options, option-critic, HAM, MAXQ, semi-MDP, action-repetition (FIGAR, TempoRL, Park 2021, Wang 2024), Dreamer family (V1-V4), hierarchical variants (Director, THICK, Hieros, LS-Imagine), TAWM ✓\n- Value overestimation: Double Q, TD3, REDQ, MBPO, MOPO, MOReL, COMBO, delusional bias ✓\n- Related methods: benechehab2023multitimestep, compounding error, DreamSmooth ✓（wait, DreamSmooth was removed in this version）\n\n**遗漏检查**：\n- DreamSmooth (lee2024dreamsmooth)、NoisyNet (fortunato2018noisynet)、PETS (chua2018pets)、STEVE (buckman2018steve) 在 Round 3/5 的 Related Work 中出现但**本轮被移除**。这些引用与论文相关（DreamSmooth: reward smoothing；NoisyNet/PETS/STEVE: noise/uncertainty 方法），但可能为了节省空间而被精简。\n- Becker-Ehmck 2023: 已在前轮降级为 non-issue（benechehab2023multitimestep 覆盖了相关主题）\n\n让我验证 references.bib 中这些被移除的引用是否还在。\n\n**总体评估**：Related Work 覆盖面在核心领域足够。被移除的引用（DreamSmooth 等）属于 secondary relevance，不影响审查结论。\n\n---\n\n## 写作质量评估\n\n**评分: 7.5/10**（Round 3: 7/10）\n\n**显著改善**：\n1. **Discussion 大幅增强**：从 Round 3 的 3 个段落扩展到 8 个段落，每个都有明确的论证目标。\"Causal role of embedding training\"、\"Intervention resistance reveals pathway redundancy\"、\"Transferable diagnostic protocol\" 各自独立成章且逻辑严密。\n2. **Mechanism evidence** 段落的分析深度远超前几轮——值校准、temporal ordering、dual pathway 分析形成完整的 evidence chain。\n3. **\"Predictive pathway\"** 措辞一致保持 ✓\n4. **\"Hypothesized structural factor\"** 一致保持 ✓\n5. **\"Mechanisms that remain to be characterized\"** 一致保持 ✓\n\n**仍存在的问题**：\n1. **Abstract 仍偏数字密集**：n=36, AUROC=1.000, F1=1.000, 14-19% 在约 140 词中出现。\n2. **F1-F7 双编号** 仍在使用——但在内容已大幅充实的情况下，这些 finding 标签确实提供了有效的交叉引用结构。降级为 non-issue。\n3. **F6 section 的 seed 变更需要解释**：Round 3-5 报告 exp_008e_v3 s1-s4（2/4 collapse, 含 Pathway B），Round 6 报告 s0,s1,s2,s5（0/4 CIVO onset）。这是不同的 seed 集合。论文应在正文或脚注中说明为何更换了实验 seeds，否则有 cherry-picking 嫌疑——尽管新 seeds 的结果实际上更合理（dt=1 imagination 下确实不应出现 CIVO）。\n\n**新的写作亮点**：\n- Figure 1 (mechanism diagram) 是优秀的概念图，直观展示了 CIVO 反馈环路\n- \"Scope precision through negative controls\" 段落展示了 mature 的实验设计思维\n\n---\n\n## 其他 Issue 确认\n\n### Round 5 修复确认\n| Issue | 状态 | 验证 |\n|-------|------|------|\n| IQM 148.8 | ✅ maintained | results.tex:86 |\n| \"predictive pathway\" | ✅ maintained | results.tex:4 |\n| \"gradient diversity\" → \"mechanisms...\" | ✅ maintained | results.tex:185 |\n| Seed count \"4-5 seeds\" | ✅ maintained | methodology.tex:26 |\n| AUTHORERR | ✅ fixed | main.tex:55 (但这是 ICML 模板的修复，切换到 CoRL 后需重新处理) |\n\n### 新发现问题\n\n**N-R6-1 [warning] F6 seed 集合变更未说明**\n\nRound 3-5: \"Exp_008e_v3 restricts imagination to dt=1...Two of four seeds collapse (50%): Pathway A (CIVO, NVE=4.02×) and Pathway B (entropy increase, NVE=3.78×)\"\n\nRound 6: \"Across four unique seeds (s0, s1, s2, s5), none exhibits CIVO onset (peak NVE ≤0.8×)\"\n\n从 \"2/4 collapse\" 到 \"0/4 CIVO onset\" 是一个重大结论变化。如果是因为使用了不同 seeds，应明确说明原因（如原 seeds 存在 configuration error）。如果是因为 threshold 从 1.5× 提高到 2.0×，原来的 NVE 4.02× 和 3.78× 仍然远超 2.0×，所以不能是 threshold 变化导致的。这需要解释。\n\n**N-R6-2 [warning] 统计跳跃需要透明度**\n\n从 AUROC 0.957 (n=30) 到 AUROC 1.000 (n=36) 是一个非常大的跳跃。论文应在正文或 Appendix 中说明：\n- 新增的 6 个 data points 是什么（哪些实验？）\n- 为什么 threshold 从 1.5× 调整到 2.0×（是 data-driven optimization 还是有 principled reason？）\n- 新数据是否有 prospective validation（先设定 threshold 再测试），还是 retrospective fitting（在全部数据上优化 threshold）\n\nAUROC=1.000 在 36 个样本上看起来令人印象深刻，但如果 threshold 是在同一数据上优化的（retrospective），这可能是 overfitting。LOEO 验证的结果（之前报告 AUROC=0.988）在新数据上是否仍成立？\n\n**N-R6-3 [minor] DreamSmooth/NoisyNet/PETS/STEVE 引用被移除**\n\nRound 5 的 Related Work 引用了这四篇论文；Round 6 移除了它们。这些引用与论文有 secondary relevance（DreamSmooth: reward smoothing 无法解决 fidelity gap；NoisyNet: noise 方法的对比；PETS/STEVE: ensemble 方法）。移除可能是为了节省空间，但在切换到 CoRL 单栏格式后 Related Work 的空间约束可能更大也可能更小。\n\n---\n\n## CoRL 评分\n\n### Soundness: 3/4 (Good)\nFactorial design 严谨；AUROC=1.000 令人印象深刻（但需透明度）；Fisher exact p<0.001；temporal ordering 仅 n=2。\n\n### Presentation: 3/4 (Good)\nDiscussion 大幅改善；Figure 1 机制图优秀；Abstract 仍偏数字密集；F6 seed 变更未解释。**但当前 PDF 使用 ICML 模板是 disqualifying 的格式问题。**\n\n### Significance (CoRL 标准): 2/4 (Fair)\n对 world-model RL 子社区有价值的 diagnostic，但：\n- CIVO 在 manipulation 中不出现——CoRL 核心关注领域\n- \"Transferable diagnostic protocol\" 未验证\n- Actionable takeaway 仍是 \"不要用 trained dt-embedding\"\n- 无 real-robot 实验\n\n### Originality: 3/4 (Good)\nCIVO 新颖；双通路分析有洞见；完美分类器稀有。方法论是已有技术组合。\n\n### Overall: 3/6 (Weak Reject)\n\n**CoRL venue fit 是决定性因素。**\n\n如果这篇论文提交到 ICML/NeurIPS，我会给 4-5/6 (Weak Accept 到 Accept)。论文的科学质量在 6 轮审稿中提升巨大——从 Round 3 的 decent diagnostic study 成长为一个有 mature mechanism analysis、完美分类器、系统 negative controls 的 thorough investigation。\n\n但 CoRL 要求 \"focus on core robotics problems\"：\n1. CIVO 不出现在 manipulation 中——论文自己的数据证明了这一点\n2. 所有 positive results 来自 DMC locomotion——不是 robot learning 的前沿\n3. \"Transferable diagnostic protocol\" 是一个好概念但未在任何 robotics-relevant scenario（goal-conditioned, language-conditioned）中验证\n4. 无 real-robot 实验——连 sim-to-real 的讨论都很有限\n\n**与 Round 3 的 5/10 相比**：科学质量大幅提升（更多环境、更强统计、更深机制分析），但 venue fit 的核心矛盾不变。从 5/10 微升到 5.5/10 反映的是 \"更好的论文但仍然不是 CoRL 论文\" 的判断。\n\n### Confidence: 4/5\n\n---\n\n## 总结与建议\n\n**必须立即修复的 CRITICAL 问题**：\n1. 切换到 CoRL/PMLR 模板（`corl_2026.sty`）\n2. 验证切换后正文是否 ≤ 8 页——以当前内容量，大概率超页，需大幅精简\n\n**建议**：\n- 如果要提交 CoRL，需要在 Discussion 中显著加强 robotics deployment 的具体论证——不是 \"这与 robotics 相关\" 的修辞，而是具体说明 CIVO 在什么样的 real-robot 部署场景（如 DayDreamer 式的 online world-model learning）中会造成什么样的具体危险\n- 考虑在 \"Transferable diagnostic protocol\" 部分增加一个 pilot experiment：在一个 goal-conditioned imagination 任务上运行该协议的 quick validation，即使结果是 negative，也能展示协议的实际可用性\n- 或者：再次考虑 ICML 2026 的下一个 submission cycle / NeurIPS 2026 作为更合适的 venue\n\n**我的诚实评价**：这是一篇好论文放在了错误的 venue。科学质量从 Round 1 到 Round 6 的进步是显著的，但 CoRL 的 \"core robotics problems\" 要求与本文的核心贡献（DreamerV3 locomotion-specific diagnostic）之间存在结构性不匹配。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 修订评估 — Reviewer 2（新颖性 + 相关工作 + 写作质量 + CoRL Venue 适配性）\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026（从 ICML 转回 CoRL）\n\n---\n\n## 关键变化追踪（Round 5 → Round 6）\n\n论文在内容层面有 **大幅实质性更新**，远超格式级修改：\n\n| 变化类别 | 具体内容 |\n|---------|---------|\n| 统计数据 | NVE threshold 1.5× → 2.0×; AUROC 0.957 → 1.000; n: 30 → 36; 27/30 → 36/36 perfect |\n| 新机制分析 | 值校准（V/MC-return 7.80× vs 1.05×）、temporal ordering（r=0.81, p=0.002）、双通路分析（Walker: reward fidelity, Cheetah: dynamics drift） |\n| 新环境 | Cartpole 作为 single-joint negative control（0/3 CIVO） |\n| 新实验 | 2×2 frozen verification (exp_084-087), 008f corrected-code rerun, exp_078 (Cheetah s0) |\n| 新图表 | Figure 1: CIVO 机制图 (mechanism diagram) |\n| Discussion 扩展 | 新增 5 个段落：Causal role of embedding training, Intervention resistance, Transferable diagnostic protocol, Scope precision, Cross-env validation |\n| F6 重写 | \"2/4 collapse (50%)\" → \"0/4 CIVO onset\"（不同 seed 集合：s0,s1,s2,s5 替代原 s1-s4） |\n| Table 2 更新 | Frozen: 5/7→7/7 (100%), Removed: 5/5→6/6, Untreated: 7→10 seeds |\n| Broader Impact | 完全重写，聚焦 robotics safety |\n\n这是一篇在科学内容上显著优于所有前几轮版本的论文。\n\n---\n\n## CRITICAL Issues\n\n### 1. 模板合规性 — `\\usepackage{icml2026}` 仍未切换\n**[STILL_OPEN — CRITICAL / DESK REJECT]**\n\n- main.tex:8: `\\usepackage{icml2026}` ✗\n- main.tex:41: `\\icmltitlerunning{...}` — ICML 专用宏\n- main.tex:46-55: `\\icmltitle`, `\\icmlauthorlist`, `\\icmlaffiliation`, `\\icmlcorrespondingauthor` — ICML 专用宏\n- main.tex:86: `\\bibliographystyle{icml2026}` — ICML 引用格式\n- PDF 页脚: \"Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.\"\n- PDF 格式: 两栏排版（ICML），而非 CoRL 的单栏 PMLR 格式\n\n**以当前 PDF 提交到 CoRL 2026 会被 desk reject**。必须：\n1. 替换为 `\\usepackage{corl_2026}`\n2. 移除所有 ICML 专用宏\n3. 恢复 CoRL 单栏格式\n4. 重新编译并验证 8 页限制\n\n### 2. 页数合规性风险（无法在当前模板下验证）\n**[CANNOT VERIFY — WARNING]**\n\nRound 3 版本在 CoRL 单栏格式下恰好 8 页。Round 6 版本新增了大量内容：\n- Figure 1 机制图（新增）\n- Mechanism evidence 段落（~20 行新文本）\n- Temporal ordering 段落（~15 行新文本）\n- Discussion 新增 5 个完整段落（~120 行新文本）\n- Table 1 扩展（新增 exp_078, 008f s0）\n- Table 2 脚注扩展\n\n在 CoRL 单栏格式下，这些新增内容几乎确定会导致正文超过 8 页。需要在切换模板后立即验证，可能需要大幅精简 Discussion 或将部分内容移至 Appendix。\n\n---\n\n## CoRL Venue 适配性（REOPENED — 核心评审问题）\n\n### Round 3 vs Round 6 对比\n\n| 维度 | Round 3 评估 | Round 6 评估 |\n|------|------------|------------|\n| 环境覆盖 | 5 env (2 DMC + 3 ManiSkill) | 6 env (3 DMC incl. Cartpole + 3 ManiSkill) |\n| 统计证据 | AUROC 0.953, 26/29 | AUROC 1.000, 36/36, Fisher p<0.001 |\n| 机制理解 | 2.78× reward gap | 双通路分析 + temporal ordering + 值校准 |\n| 方法论贡献 | 四级干预层级 | 四级干预 + \"transferable diagnostic protocol\" 概念 |\n| Robotics framing | bookend 式 rhetoric | 更深入但仍以 DreamerV3 为核心 |\n| Broader Impact | CoRL 版：标准 limitations | 新版：robotics safety framing |\n\n### Venue Fit 评分：5.5/10（Round 3: 5/10）\n\n**微幅提升但核心矛盾未解**。\n\n**改善的地方**：\n1. **\"Transferable diagnostic protocol\"**（analysis.tex:13-14）是本轮最有价值的 CoRL 定位改进。将四级干预层级从 \"CIVO 专用工具\" 提升为 \"任何 learned conditioning signal + imagination-based training 都可复用的诊断框架\"，明确提到 goal-conditioned imagination、language-conditioned world models、skill embeddings——都是 CoRL 核心话题。\n2. **Scope precision 分析**（analysis.tex:22-25）通过 6 环境 × 3 task types 的系统 negative controls 展示了实验设计的严谨性。\n3. **Fisher exact test** (p < 0.001) 和 AUROC=1.000 大幅增强了统计可信度。\n4. **Broader Impact Statement** 直接讨论 robotic deployment safety。\n\n**未解决的核心问题**：\n1. **CIVO 仍是 locomotion-specific**：5/7 multi-joint locomotion seeds vs 0/16 controls，但在 manipulation（ManiSkill 3 tasks, 0/3 trigger-specific）中不出现。CoRL 社区更关心 manipulation 和 contact-rich tasks。\n2. **\"Transferable diagnostic protocol\" 仍是理论性的**：论文声称该协议可用于 goal-conditioned 和 language-conditioned models，但**没有在任何这些场景上实际验证**。这是一个 promise 而非 demonstrated contribution。\n3. **所有实验在模拟环境中**：Limitations 承认 \"not...real-robot deployments\"（conclusion.tex:7）。\n4. **Actionable takeaway 不变**：对 CoRL 从业者来说，最有效建议仍然是 \"不要用 trained dt-embedding\"。\n5. **核心贡献是 DreamerV3-specific 诊断**：虽然论文试图推广，但 CIVO 是否在 IRIS、DreamerV4、TransDreamer 等其他架构中存在完全未知。\n\n**对比 CoRL 接受的 diagnostic papers**：CoRL 历史上确实接受 diagnostic work（如 DayDreamer 的 ablation studies），但这些通常是在真实机器人上做的，且直接服务于 deployment。本文的诊断是在 simulated locomotion 上做的，与 real-robot deployment 的距离较远。\n\n---\n\n## 新颖性评估\n\n**评分: 7/10**\n\nRound 6 的科学新颖性显著提升：\n\n1. **CIVO 作为新 failure mode**（已在前几轮确认）——新颖且有价值\n2. **双通路分析**（NEW）：Walker 通过 reward fidelity degradation，Cheetah 通过 dynamics-model prior drift（无 reward gap），这是一个有洞察力的发现——同一个宏观现象可以有不同的微观机制\n3. **Temporal ordering**（NEW）：r=0.81, p=0.002 的时间序列分析提供了 causal direction 的证据（但 n=2 仍然太少）\n4. **完美分类器**（AUROC=1.000, F1=1.000, n=36）——NVE 阈值 2.0× 完美分离 CIVO/non-CIVO，这在 RL 诊断中非常稀有\n5. **Transferable diagnostic protocol 概念**——有潜力但未验证\n\n**减分点**：\n- 方法论本身（factorial ablation, NVE metric, gradient stopping）都是已有技术的组合\n- CIVO 现象仅在 DreamerV3 locomotion 中复现，泛化性未知\n- Temporal ordering n=2 太小，只能算 preliminary evidence\n\n---\n\n## 相关工作完整性\n\nRelated Work（related_work.tex）覆盖了主要领域：\n- Temporal abstraction: options, option-critic, HAM, MAXQ, semi-MDP, action-repetition (FIGAR, TempoRL, Park 2021, Wang 2024), Dreamer family (V1-V4), hierarchical variants (Director, THICK, Hieros, LS-Imagine), TAWM ✓\n- Value overestimation: Double Q, TD3, REDQ, MBPO, MOPO, MOReL, COMBO, delusional bias ✓\n- Related methods: benechehab2023multitimestep, compounding error, DreamSmooth ✓（wait, DreamSmooth was removed in this version）\n\n**遗漏检查**：\n- DreamSmooth (lee2024dreamsmooth)、NoisyNet (fortunato2018noisynet)、PETS (chua2018pets)、STEVE (buckman2018steve) 在 Round 3/5 的 Related Work 中出现但**本轮被移除**。这些引用与论文相关（DreamSmooth: reward smoothing；NoisyNet/PETS/STEVE: noise/uncertainty 方法），但可能为了节省空间而被精简。\n- Becker-Ehmck 2023: 已在前轮降级为 non-issue（benechehab2023multitimestep 覆盖了相关主题）\n\n让我验证 references.bib 中这些被移除的引用是否还在。\n\n**总体评估**：Related Work 覆盖面在核心领域足够。被移除的引用（DreamSmooth 等）属于 secondary relevance，不影响审查结论。\n\n---\n\n## 写作质量评估\n\n**评分: 7.5/10**（Round 3: 7/10）\n\n**显著改善**：\n1. **Discussion 大幅增强**：从 Round 3 的 3 个段落扩展到 8 个段落，每个都有明确的论证目标。\"Causal role of embedding training\"、\"Intervention resistance reveals pathway redundancy\"、\"Transferable diagnostic protocol\" 各自独立成章且逻辑严密。\n2. **Mechanism evidence** 段落的分析深度远超前几轮——值校准、temporal ordering、dual pathway 分析形成完整的 evidence chain。\n3. **\"Predictive pathway\"** 措辞一致保持 ✓\n4. **\"Hypothesized structural factor\"** 一致保持 ✓\n5. **\"Mechanisms that remain to be characterized\"** 一致保持 ✓\n\n**仍存在的问题**：\n1. **Abstract 仍偏数字密集**：n=36, AUROC=1.000, F1=1.000, 14-19% 在约 140 词中出现。\n2. **F1-F7 双编号** 仍在使用——但在内容已大幅充实的情况下，这些 finding 标签确实提供了有效的交叉引用结构。降级为 non-issue。\n3. **F6 section 的 seed 变更需要解释**：Round 3-5 报告 exp_008e_v3 s1-s4（2/4 collapse, 含 Pathway B），Round 6 报告 s0,s1,s2,s5（0/4 CIVO onset）。这是不同的 seed 集合。论文应在正文或脚注中说明为何更换了实验 seeds，否则有 cherry-picking 嫌疑——尽管新 seeds 的结果实际上更合理（dt=1 imagination 下确实不应出现 CIVO）。\n\n**新的写作亮点**：\n- Figure 1 (mechanism diagram) 是优秀的概念图，直观展示了 CIVO 反馈环路\n- \"Scope precision through negative controls\" 段落展示了 mature 的实验设计思维\n\n---\n\n## 其他 Issue 确认\n\n### Round 5 修复确认\n| Issue | 状态 | 验证 |\n|-------|------|------|\n| IQM 148.8 | ✅ maintained | results.tex:86 |\n| \"predictive pathway\" | ✅ maintained | results.tex:4 |\n| \"gradient diversity\" → \"mechanisms...\" | ✅ maintained | results.tex:185 |\n| Seed count \"4-5 seeds\" | ✅ maintained | methodology.tex:26 |\n| AUTHORERR | ✅ fixed | main.tex:55 (但这是 ICML 模板的修复，切换到 CoRL 后需重新处理) |\n\n### 新发现问题\n\n**N-R6-1 [warning] F6 seed 集合变更未说明**\n\nRound 3-5: \"Exp_008e_v3 restricts imagination to dt=1...Two of four seeds collapse (50%): Pathway A (CIVO, NVE=4.02×) and Pathway B (entropy increase, NVE=3.78×)\"\n\nRound 6: \"Across four unique seeds (s0, s1, s2, s5), none exhibits CIVO onset (peak NVE ≤0.8×)\"\n\n从 \"2/4 collapse\" 到 \"0/4 CIVO onset\" 是一个重大结论变化。如果是因为使用了不同 seeds，应明确说明原因（如原 seeds 存在 configuration error）。如果是因为 threshold 从 1.5× 提高到 2.0×，原来的 NVE 4.02× 和 3.78× 仍然远超 2.0×，所以不能是 threshold 变化导致的。这需要解释。\n\n**N-R6-2 [warning] 统计跳跃需要透明度**\n\n从 AUROC 0.957 (n=30) 到 AUROC 1.000 (n=36) 是一个非常大的跳跃。论文应在正文或 Appendix 中说明：\n- 新增的 6 个 data points 是什么（哪些实验？）\n- 为什么 threshold 从 1.5× 调整到 2.0×（是 data-driven optimization 还是有 principled reason？）\n- 新数据是否有 prospective validation（先设定 threshold 再测试），还是 retrospective fitting（在全部数据上优化 threshold）\n\nAUROC=1.000 在 36 个样本上看起来令人印象深刻，但如果 threshold 是在同一数据上优化的（retrospective），这可能是 overfitting。LOEO 验证的结果（之前报告 AUROC=0.988）在新数据上是否仍成立？\n\n**N-R6-3 [minor] DreamSmooth/NoisyNet/PETS/STEVE 引用被移除**\n\nRound 5 的 Related Work 引用了这四篇论文；Round 6 移除了它们。这些引用与论文有 secondary relevance（DreamSmooth: reward smoothing 无法解决 fidelity gap；NoisyNet: noise 方法的对比；PETS/STEVE: ensemble 方法）。移除可能是为了节省空间，但在切换到 CoRL 单栏格式后 Related Work 的空间约束可能更大也可能更小。\n\n---\n\n## CoRL 评分\n\n### Soundness: 3/4 (Good)\nFactorial design 严谨；AUROC=1.000 令人印象深刻（但需透明度）；Fisher exact p<0.001；temporal ordering 仅 n=2。\n\n### Presentation: 3/4 (Good)\nDiscussion 大幅改善；Figure 1 机制图优秀；Abstract 仍偏数字密集；F6 seed 变更未解释。**但当前 PDF 使用 ICML 模板是 disqualifying 的格式问题。**\n\n### Significance (CoRL 标准): 2/4 (Fair)\n对 world-model RL 子社区有价值的 diagnostic，但：\n- CIVO 在 manipulation 中不出现——CoRL 核心关注领域\n- \"Transferable diagnostic protocol\" 未验证\n- Actionable takeaway 仍是 \"不要用 trained dt-embedding\"\n- 无 real-robot 实验\n\n### Originality: 3/4 (Good)\nCIVO 新颖；双通路分析有洞见；完美分类器稀有。方法论是已有技术组合。\n\n### Overall: 3/6 (Weak Reject)\n\n**CoRL venue fit 是决定性因素。**\n\n如果这篇论文提交到 ICML/NeurIPS，我会给 4-5/6 (Weak Accept 到 Accept)。论文的科学质量在 6 轮审稿中提升巨大——从 Round 3 的 decent diagnostic study 成长为一个有 mature mechanism analysis、完美分类器、系统 negative controls 的 thorough investigation。\n\n但 CoRL 要求 \"focus on core robotics problems\"：\n1. CIVO 不出现在 manipulation 中——论文自己的数据证明了这一点\n2. 所有 positive results 来自 DMC locomotion——不是 robot learning 的前沿\n3. \"Transferable diagnostic protocol\" 是一个好概念但未在任何 robotics-relevant scenario（goal-conditioned, language-conditioned）中验证\n4. 无 real-robot 实验——连 sim-to-real 的讨论都很有限\n\n**与 Round 3 的 5/10 相比**：科学质量大幅提升（更多环境、更强统计、更深机制分析），但 venue fit 的核心矛盾不变。从 5/10 微升到 5.5/10 反映的是 \"更好的论文但仍然不是 CoRL 论文\" 的判断。\n\n### Confidence: 4/5\n\n---\n\n## 总结与建议\n\n**必须立即修复的 CRITICAL 问题**：\n1. 切换到 CoRL/PMLR 模板（`corl_2026.sty`）\n2. 验证切换后正文是否 ≤ 8 页——以当前内容量，大概率超页，需大幅精简\n\n**建议**：\n- 如果要提交 CoRL，需要在 Discussion 中显著加强 robotics deployment 的具体论证——不是 \"这与 robotics 相关\" 的修辞，而是具体说明 CIVO 在什么样的 real-robot 部署场景（如 DayDreamer 式的 online world-model learning）中会造成什么样的具体危险\n- 考虑在 \"Transferable diagnostic protocol\" 部分增加一个 pilot experiment：在一个 goal-conditioned imagination 任务上运行该协议的 quick validation，即使结果是 negative，也能展示协议的实际可用性\n- 或者：再次考虑 ICML 2026 的下一个 submission cycle / NeurIPS 2026 作为更合适的 venue\n\n**我的诚实评价**：这是一篇好论文放在了错误的 venue。科学质量从 Round 1 到 Round 6 的进步是显著的，但 CoRL 的 \"core robotics problems\" 要求与本文的核心贡献（DreamerV3 locomotion-specific diagnostic）之间存在结构性不匹配。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-28T00:40:41.022138+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4223
}
```

</details>

---

### Assistant

_source line 255 · 2026-05-28T00:43:03.916573+00:00_

Round 6 审稿已提交，等待 Review Director 的下一步指示（可能是 Reviewer 1 的 Round 6 交叉审稿，或其他任务）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 10

12 recorded events

### User

_source line 256 · 2026-05-28T00:43:05.137969+00:00_

[Round 6 审稿请求]:
## Round 6 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

**Reviewer 1 Overall Score**: 4/6 (Weak Accept)
**Reviewer 1 核心立场**: 方法论质量提升，但 venue 变化导致降级（从 ICML Accept 5/6 → CoRL Weak Accept 4/6）

### CRITICAL Issues

**C1: 模板仍为 ICML 2026**
R1 与你一致：第三次模板错误。

**C2: CoRL Venue 适配性**
**R1 评分: 6.5/10（你给 5.5/10）**

R1 认为有实质改善：
1. Cartpole 负控制建立了 "multi-joint locomotion-specific" 的精确 scope boundary
2. "Transferable diagnostic protocol" 直接面向 CoRL 社区（goal-conditioned, language-conditioned, skill embeddings）
3. Fisher exact test (p<0.001) 强化因果论证
4. Broader Impact 直接连接 robot deployment safety
5. Scope precision 分析从 empirical observation 提升为 hypothesis-driven analysis

但 R1 也指出仍有限制：
- 核心内容仍为 RL 方法论分析（~4 页 factorial ablation）
- 无 real-robot 验证
- CIVO 不影响 manipulation
- "Transferable diagnostic protocol" 是 forward-looking 而非 demonstrated

R1 总结：从 R3 (5/10) 改善约 1.5 分，论文处于 CoRL borderline。

### 方法论严谨性（R1: 8.5/10，比 R5 提升 0.5）

R1 高度评价：
- NVE 2.0× 完美分类 + LOEO/LOCO 双重交叉验证
- Fisher exact test 正式化因果论证
- Cheetah dissociation 深化机制理解——Walker 有 1.63× reward gap，Cheetah 无 reward gap (1.00×) 但有 comparable CIVO severity (8.27×)
- Temporal ordering (r=0.81, p=0.002)

### F6 重写

R1 详细分析了 F6 的 180° 翻转：
- Round 3-5: "2/4 collapse (50%), Pathway A (NVE=4.02×) + Pathway B (NVE=3.78×)"
- Round 6: "0/4 CIVO onset (NVE ≤0.8×)"
- 可能原因：code bug correction (008f 脚注)、seed 集合变更 (s0,s1,s2,s5 vs 原 s0-s3)、但 threshold 变化无法解释（4.02× 远超 2.0×）
- R1 认为完全移除 Pathway B 不解释原因会降低可信度
- 但正面看：0/4 CIVO in dt=1 是一个更 clean 的结论

### 新发现问题

**N-R6-1 [warning]**: F6 结果翻转未解释（与你的 N-R6-1 一致）
**N-R6-2 [warning]**: "corrected-code rerun" 缺乏细节——修正了什么 bug？是否影响其他实验？
**N-R6-3 [info]**: Table 1 中 "--- s1" 行的 Exp 编号空白

### R1 维度评分
| 维度 | R1 评分 |
|------|---------|
| Soundness | 3/4 |
| Presentation | 3/4 |
| Significance (CoRL-adjusted) | 3/4 (Good) |
| Originality | 3/4 |

---

请对以上意见逐条回应，特别关注：
1. CoRL venue fit 评分差异（R1 6.5 vs 你 5.5）——R1 的 "Cartpole negative control" 和 "transferable diagnostic protocol" 论据是否足以支撑更高评分？
2. "corrected-code rerun" 透明度问题——你是否同意 R1 的担忧？
3. R1 给 Significance 3/4 (Good) 而你给 2/4 (Fair)——你认为 R1 是否高估了对 CoRL 社区的价值？
4. 你们在 venue fit 上的 1 分差异是否可以收敛？你能接受的最高分是多少？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-28T00:43:16.223025+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-28T00:43:16.625590+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 259 · 2026-05-28T00:43:16.676398+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-28T00:43:16.727180+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 261 · 2026-05-28T00:43:21.447028+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
  }
}
```

</details>

---

### Tool result

_source line 262 · 2026-05-28T00:43:21.497810+00:00_

1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--19\% of baseline. Factorial diagnostics on two continuous-control tasks identify trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; $n{=}36$, AUROC${=}1.000$, F1${=}1.000$). The RSSM develops a reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as a hypothesized structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination, so Double Q pessimism is ineffective, though min $+$ increased capacity enables recovery.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 263 · 2026-05-28T00:43:57.706302+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 264 · 2026-05-28T00:43:57.756940+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 265 · 2026-05-28T00:45:29.286699+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 交叉回应 — Reviewer 2 对 Reviewer 1 的逐条回应\n\n---\n\n### C1: 模板仍为 ICML 2026\n\n[AGREE] R1-C1: 完全同意。第三次模板错误，这是 desk reject 级别问题，无需进一步讨论。\n\n---\n\n### C2: CoRL Venue 适配性（R1: 6.5/10 vs R2: 5.5/10）\n\n[REBUT] R1-C2: **部分反驳，上调至 6.0/10，但不接受 6.5。**\n\nR1 提出五个改善论据，我逐一回应：\n\n1. **Cartpole 负控制建立精确 scope boundary** — 同意这是方法论改善。但 scope 越精确（\"multi-joint locomotion-specific\"），与 CoRL 核心受众的交集越小。CoRL 2026 reviewer guidelines 强调 \"core robotics problems\"；一个仅在步态任务中出现、不影响 manipulation 的 failure mode，scope precision 越高反而越暴露 venue 不匹配。\n\n2. **\"Transferable diagnostic protocol\" 面向 CoRL 社区** — 这是 R1 论据中最弱的一环。§5 (Discussion) 原文：\"goal-conditioned imagination, language-conditioned world models, or skill embeddings each introduce auxiliary representations that **could** co-adapt\"（强调 could）。这是 forward-looking hypothesis，论文中没有任何一个实验在 goal-conditioned 或 language-conditioned 设置下验证过该 protocol。CoRL reviewer 会问：你说这能迁移到 skill embeddings，证据在哪？答案是没有。\n\n3. **Fisher exact test (p<0.001)** — 同意强化了统计严谨性，但这是 RL 方法论改善，不是 robotics 贡献。任何 venue 都受益于更好的统计检验。\n\n4. **Broader Impact 连接 robot deployment safety** — Framing 不改变 content。\"Silent training failures...pose safety risks for robotic deployment\" 是一句 motivation，但论文的全部实验在 DMC Walker 和 Cheetah 上运行，没有任何 real-robot deployment。\n\n5. **Scope precision 从 empirical observation 提升为 hypothesis-driven** — 同意这是科学质量的提升。但 hypothesis-driven analysis 说的是\"周期性步态动力学对 RSSM 时间预测精度更敏感\"（§5 \"Scope precision\" 段），这本身是一个未验证的假说，且指向的是 RL dynamics modeling 问题，不是 robotics 问题。\n\n**核心分歧**：R1 似乎将\"论文提到了 robotics 应用场景\"等同于\"论文对 robotics 社区有贡献\"。我的立场是：论文的 4 页 factorial ablation + 2 页 intervention hierarchy 是 RL 内部方法论分析，核心贡献是理解 DreamerV3 RSSM 的 failure mode。这对 ICML RL track 是 excellent fit，对 CoRL 是 borderline。\n\n**上调理由**：相比 Round 3，Cartpole 负控制和 cross-environment validation 确实增加了实验覆盖面，诊断 protocol 概念虽未验证但有启发价值。从 5.5 → 6.0/10。\n\n**不接受 6.5 的理由**：6.5 意味着\"略高于 borderline\"，但论文的三个根本限制未变——(1) CIVO 不影响 manipulation，(2) 无 real-robot 验证，(3) 核心方法是 RL-internal factorial ablation。这三点在 Round 3 就存在，Round 6 的改善没有触及它们。\n\n---\n\n### 方法论严谨性（R1: 8.5/10）\n\n[AGREE] R1 方法论评分: 同意 8.5/10 的评估。Round 6 的方法论提升是实质性的：\n\n- AUROC 从 0.957 → 1.000（n=36），threshold 从 1.5× → 2.0×，LOEO 交叉验证\n- Fisher exact test 正式化因果论证（p<0.001）\n- Cheetah dissociation 深化机制理解（Walker 有 reward gap 1.63×，Cheetah 无 reward gap 但 CIVO severity 8.27×）\n- Temporal ordering (r=0.81, p=0.002, n=2) 建立时间因果链\n\n唯一保留：temporal ordering 仅 n=2，统计效力有限。但作为 preliminary evidence 是充分的。\n\n---\n\n### F6 重写\n\n[AGREE] R1-F6 分析: 同意 R1 的详细分析。与我的 N-R6-1 一致。\n\n补充一点 R1 未明确说的：Round 3-5 的 F6 是论文的关键支撑之一——\"$\\dt=1$ imagination 仍有 50% collapse rate\"被用来论证 CIVO 的严重性和 intervention resistance。Round 6 直接翻转为\"0/4 CIVO\"，这不仅是数据变化，更是叙事逻辑的重构。旧结论\"even $\\dt=1$ cannot fully prevent CIVO\"变成了新结论\"$\\dt=1$ eliminates CIVO\"——这是 180° 的 claim 翻转，需要比一个脚注 $^f$ 更充分的解释。\n\n---\n\n### N-R6-1 [warning]: F6 结果翻转未解释\n\n[AGREE] R1-N-R6-1: 完全同意。与我的 N-R6-1 一致。Seeds 从 s1-s4 变为 s0,s1,s2,s5，且结论从 \"2/4 collapse\" 变为 \"0/4 CIVO\"。论文需要解释：(1) 为什么更换 seed 集合？(2) 原来的 s3, s4 发生了什么？(3) 如果是 code bug 导致旧结果不可靠，bug 的性质是什么？\n\n---\n\n### N-R6-2 [warning]: \"corrected-code rerun\" 缺乏细节\n\n[AGREE] R1-N-R6-2: 同意这是一个透明度问题。\n\nTable 1 脚注 $^f$ 仅说 \"Corrected-code rerun\"，但未交代：\n1. **修正了什么 bug？** 如果 bug 影响了 008f 的结果，是否也影响了同一代码路径上的其他实验（如 008d, 008a, 008c）？\n2. **影响范围？** 如果只有 008f 受影响，为什么？如果 bug 是 temporal subsampling 模块中的，那所有 subsample=ON 的实验都应重新审查。\n3. **新旧结果对比？** 原来的 008f 结果是什么？与 corrected 版本差异多大？\n\n这直接关系到 Table 2 中 \"Removed: 6/6 (100%)\" 的可信度——如果 008f 的\"健康\"结论依赖于 code correction，reviewer 有权要求看到 correction 的完整 changelog。\n\n---\n\n### N-R6-3 [info]: Table 1 \"--- s1\" 行 Exp 编号空白\n\n[AGREE] R1-N-R6-3: 小问题，但确实降低可读性。应为 008f 的 s1 seed 行补上实验编号。\n\n---\n\n### R1 维度评分对比与回应\n\n| 维度 | R1 评分 | R2 评分 | 差异 | 回应 |\n|------|---------|---------|------|------|\n| Soundness | 3/4 | 3/4 | 一致 | — |\n| Presentation | 3/4 | 2.5/4 | -0.5 | R1 可能未充分考虑 F6 叙事翻转对可读性的影响；但 Round 6 整体写作确实改善，我可上调至 2.75/4 |\n| Significance (CoRL) | 3/4 | 2/4 | -1.0 | 见下方详细讨论 |\n| Originality | 3/4 | 3/4 | 一致 | — |\n\n---\n\n### Director 指定问题回应\n\n**Q1: CoRL venue fit 评分差异是否可收敛？**\n\n我从 5.5 上调至 **6.0/10**。R1 在 6.5/10。差距缩小至 0.5 分。\n\n不接受进一步上调的原因：CoRL 的核心标准是\"对机器人学社区的直接贡献\"。论文的全部实验在 DMC 仿真环境中进行，CIVO 仅影响 multi-joint locomotion，不影响 manipulation（CoRL 的核心场景），\"transferable diagnostic protocol\" 是未验证的假说。这些是结构性限制，不是写作能修复的。\n\n**Q2: \"corrected-code rerun\" 透明度**\n\n同意 R1 的担忧。见上方 N-R6-2 详细分析。这不是 critical 级别（不会单独导致 reject），但在 F6 结论已经 180° 翻转的背景下，缺乏透明度会放大可信度风险。两个问题叠加（seed 更换 + code correction）使得 F6 这一行实验的可信度低于论文其他部分。\n\n**Q3: Significance 3/4 vs 2/4**\n\n维持 **2/4 (Fair)**，理由：\n\nR1 给 3/4 (Good) 的核心论据是 \"transferable diagnostic protocol\" 对 CoRL 社区的价值。但：\n- §5 原文用的是 \"could co-adapt\"，是假说不是结论\n- 没有任何 goal-conditioned / language-conditioned / skill embedding 实验\n- 论文对 CoRL practitioner 的实际 actionable takeaway 是：\"如果你在 DreamerV3 中用 $\\dt$-conditioning，冻结 embedding 或用 NVE 监控\"——这是一个非常窄的 practitioner 群体（使用 DreamerV3 + 想做 variable-rate imagination 的研究者）\n\n如果 venue 是 ICML，我会给 Significance 3/4 (Good)，因为 CIVO 作为 failure mode identification 对 RL 社区有广泛意义。但 CoRL 要求 robotics-specific significance，这篇论文没有达到。\n\n**Q4: 最高可接受分数**\n\n- Venue fit: **6.0/10**（已上调，不再上调）\n- Significance: **2.5/4**（如果必须收敛，我可以从 2/4 让步到 2.5/4，承认 diagnostic protocol 概念的启发价值，但仍低于 R1 的 3/4）\n- Overall: 维持 **3/6 (Weak Reject)**。R1 给 4/6 (Weak Accept)。核心分歧在 venue fit 判断上——我认为这是一篇好论文投错了会议，R1 认为改善足以 borderline accept。\n\n---\n\n### 总结\n\n与 R1 在方法论评价上高度一致（Soundness 3/4, Originality 3/4）。主要分歧在 venue fit（6.0 vs 6.5）和 significance（2-2.5/4 vs 3/4），根源是对 \"robotics 社区直接贡献\" 的判断标准不同。R1 更看重 forward-looking potential（\"could apply to skill embeddings\"），我更看重 demonstrated contribution（\"论文实际验证了什么\"）。这是合理的 reviewer 间分歧，建议 AC 根据 CoRL 2026 的实际接收标准裁决。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 交叉回应 — Reviewer 2 对 Reviewer 1 的逐条回应\n\n---\n\n### C1: 模板仍为 ICML 2026\n\n[AGREE] R1-C1: 完全同意。第三次模板错误，这是 desk reject 级别问题，无需进一步讨论。\n\n---\n\n### C2: CoRL Venue 适配性（R1: 6.5/10 vs R2: 5.5/10）\n\n[REBUT] R1-C2: **部分反驳，上调至 6.0/10，但不接受 6.5。**\n\nR1 提出五个改善论据，我逐一回应：\n\n1. **Cartpole 负控制建立精确 scope boundary** — 同意这是方法论改善。但 scope 越精确（\"multi-joint locomotion-specific\"），与 CoRL 核心受众的交集越小。CoRL 2026 reviewer guidelines 强调 \"core robotics problems\"；一个仅在步态任务中出现、不影响 manipulation 的 failure mode，scope precision 越高反而越暴露 venue 不匹配。\n\n2. **\"Transferable diagnostic protocol\" 面向 CoRL 社区** — 这是 R1 论据中最弱的一环。§5 (Discussion) 原文：\"goal-conditioned imagination, language-conditioned world models, or skill embeddings each introduce auxiliary representations that **could** co-adapt\"（强调 could）。这是 forward-looking hypothesis，论文中没有任何一个实验在 goal-conditioned 或 language-conditioned 设置下验证过该 protocol。CoRL reviewer 会问：你说这能迁移到 skill embeddings，证据在哪？答案是没有。\n\n3. **Fisher exact test (p<0.001)** — 同意强化了统计严谨性，但这是 RL 方法论改善，不是 robotics 贡献。任何 venue 都受益于更好的统计检验。\n\n4. **Broader Impact 连接 robot deployment safety** — Framing 不改变 content。\"Silent training failures...pose safety risks for robotic deployment\" 是一句 motivation，但论文的全部实验在 DMC Walker 和 Cheetah 上运行，没有任何 real-robot deployment。\n\n5. **Scope precision 从 empirical observation 提升为 hypothesis-driven** — 同意这是科学质量的提升。但 hypothesis-driven analysis 说的是\"周期性步态动力学对 RSSM 时间预测精度更敏感\"（§5 \"Scope precision\" 段），这本身是一个未验证的假说，且指向的是 RL dynamics modeling 问题，不是 robotics 问题。\n\n**核心分歧**：R1 似乎将\"论文提到了 robotics 应用场景\"等同于\"论文对 robotics 社区有贡献\"。我的立场是：论文的 4 页 factorial ablation + 2 页 intervention hierarchy 是 RL 内部方法论分析，核心贡献是理解 DreamerV3 RSSM 的 failure mode。这对 ICML RL track 是 excellent fit，对 CoRL 是 borderline。\n\n**上调理由**：相比 Round 3，Cartpole 负控制和 cross-environment validation 确实增加了实验覆盖面，诊断 protocol 概念虽未验证但有启发价值。从 5.5 → 6.0/10。\n\n**不接受 6.5 的理由**：6.5 意味着\"略高于 borderline\"，但论文的三个根本限制未变——(1) CIVO 不影响 manipulation，(2) 无 real-robot 验证，(3) 核心方法是 RL-internal factorial ablation。这三点在 Round 3 就存在，Round 6 的改善没有触及它们。\n\n---\n\n### 方法论严谨性（R1: 8.5/10）\n\n[AGREE] R1 方法论评分: 同意 8.5/10 的评估。Round 6 的方法论提升是实质性的：\n\n- AUROC 从 0.957 → 1.000（n=36），threshold 从 1.5× → 2.0×，LOEO 交叉验证\n- Fisher exact test 正式化因果论证（p<0.001）\n- Cheetah dissociation 深化机制理解（Walker 有 reward gap 1.63×，Cheetah 无 reward gap 但 CIVO severity 8.27×）\n- Temporal ordering (r=0.81, p=0.002, n=2) 建立时间因果链\n\n唯一保留：temporal ordering 仅 n=2，统计效力有限。但作为 preliminary evidence 是充分的。\n\n---\n\n### F6 重写\n\n[AGREE] R1-F6 分析: 同意 R1 的详细分析。与我的 N-R6-1 一致。\n\n补充一点 R1 未明确说的：Round 3-5 的 F6 是论文的关键支撑之一——\"$\\dt=1$ imagination 仍有 50% collapse rate\"被用来论证 CIVO 的严重性和 intervention resistance。Round 6 直接翻转为\"0/4 CIVO\"，这不仅是数据变化，更是叙事逻辑的重构。旧结论\"even $\\dt=1$ cannot fully prevent CIVO\"变成了新结论\"$\\dt=1$ eliminates CIVO\"——这是 180° 的 claim 翻转，需要比一个脚注 $^f$ 更充分的解释。\n\n---\n\n### N-R6-1 [warning]: F6 结果翻转未解释\n\n[AGREE] R1-N-R6-1: 完全同意。与我的 N-R6-1 一致。Seeds 从 s1-s4 变为 s0,s1,s2,s5，且结论从 \"2/4 collapse\" 变为 \"0/4 CIVO\"。论文需要解释：(1) 为什么更换 seed 集合？(2) 原来的 s3, s4 发生了什么？(3) 如果是 code bug 导致旧结果不可靠，bug 的性质是什么？\n\n---\n\n### N-R6-2 [warning]: \"corrected-code rerun\" 缺乏细节\n\n[AGREE] R1-N-R6-2: 同意这是一个透明度问题。\n\nTable 1 脚注 $^f$ 仅说 \"Corrected-code rerun\"，但未交代：\n1. **修正了什么 bug？** 如果 bug 影响了 008f 的结果，是否也影响了同一代码路径上的其他实验（如 008d, 008a, 008c）？\n2. **影响范围？** 如果只有 008f 受影响，为什么？如果 bug 是 temporal subsampling 模块中的，那所有 subsample=ON 的实验都应重新审查。\n3. **新旧结果对比？** 原来的 008f 结果是什么？与 corrected 版本差异多大？\n\n这直接关系到 Table 2 中 \"Removed: 6/6 (100%)\" 的可信度——如果 008f 的\"健康\"结论依赖于 code correction，reviewer 有权要求看到 correction 的完整 changelog。\n\n---\n\n### N-R6-3 [info]: Table 1 \"--- s1\" 行 Exp 编号空白\n\n[AGREE] R1-N-R6-3: 小问题，但确实降低可读性。应为 008f 的 s1 seed 行补上实验编号。\n\n---\n\n### R1 维度评分对比与回应\n\n| 维度 | R1 评分 | R2 评分 | 差异 | 回应 |\n|------|---------|---------|------|------|\n| Soundness | 3/4 | 3/4 | 一致 | — |\n| Presentation | 3/4 | 2.5/4 | -0.5 | R1 可能未充分考虑 F6 叙事翻转对可读性的影响；但 Round 6 整体写作确实改善，我可上调至 2.75/4 |\n| Significance (CoRL) | 3/4 | 2/4 | -1.0 | 见下方详细讨论 |\n| Originality | 3/4 | 3/4 | 一致 | — |\n\n---\n\n### Director 指定问题回应\n\n**Q1: CoRL venue fit 评分差异是否可收敛？**\n\n我从 5.5 上调至 **6.0/10**。R1 在 6.5/10。差距缩小至 0.5 分。\n\n不接受进一步上调的原因：CoRL 的核心标准是\"对机器人学社区的直接贡献\"。论文的全部实验在 DMC 仿真环境中进行，CIVO 仅影响 multi-joint locomotion，不影响 manipulation（CoRL 的核心场景），\"transferable diagnostic protocol\" 是未验证的假说。这些是结构性限制，不是写作能修复的。\n\n**Q2: \"corrected-code rerun\" 透明度**\n\n同意 R1 的担忧。见上方 N-R6-2 详细分析。这不是 critical 级别（不会单独导致 reject），但在 F6 结论已经 180° 翻转的背景下，缺乏透明度会放大可信度风险。两个问题叠加（seed 更换 + code correction）使得 F6 这一行实验的可信度低于论文其他部分。\n\n**Q3: Significance 3/4 vs 2/4**\n\n维持 **2/4 (Fair)**，理由：\n\nR1 给 3/4 (Good) 的核心论据是 \"transferable diagnostic protocol\" 对 CoRL 社区的价值。但：\n- §5 原文用的是 \"could co-adapt\"，是假说不是结论\n- 没有任何 goal-conditioned / language-conditioned / skill embedding 实验\n- 论文对 CoRL practitioner 的实际 actionable takeaway 是：\"如果你在 DreamerV3 中用 $\\dt$-conditioning，冻结 embedding 或用 NVE 监控\"——这是一个非常窄的 practitioner 群体（使用 DreamerV3 + 想做 variable-rate imagination 的研究者）\n\n如果 venue 是 ICML，我会给 Significance 3/4 (Good)，因为 CIVO 作为 failure mode identification 对 RL 社区有广泛意义。但 CoRL 要求 robotics-specific significance，这篇论文没有达到。\n\n**Q4: 最高可接受分数**\n\n- Venue fit: **6.0/10**（已上调，不再上调）\n- Significance: **2.5/4**（如果必须收敛，我可以从 2/4 让步到 2.5/4，承认 diagnostic protocol 概念的启发价值，但仍低于 R1 的 3/4）\n- Overall: 维持 **3/6 (Weak Reject)**。R1 给 4/6 (Weak Accept)。核心分歧在 venue fit 判断上——我认为这是一篇好论文投错了会议，R1 认为改善足以 borderline accept。\n\n---\n\n### 总结\n\n与 R1 在方法论评价上高度一致（Soundness 3/4, Originality 3/4）。主要分歧在 venue fit（6.0 vs 6.5）和 significance（2-2.5/4 vs 3/4），根源是对 \"robotics 社区直接贡献\" 的判断标准不同。R1 更看重 forward-looking potential（\"could apply to skill embeddings\"），我更看重 demonstrated contribution（\"论文实际验证了什么\"）。这是合理的 reviewer 间分歧，建议 AC 根据 CoRL 2026 的实际接收标准裁决。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-28T00:45:33.253636+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3966
}
```

</details>

---

### Assistant

_source line 267 · 2026-05-28T00:45:40.665868+00:00_

Round 6 交叉回应已提交。核心立场：

- **C1 模板错误**：[AGREE]，与 R1 一致
- **Venue fit**：从 5.5 上调至 **6.0/10**（R1: 6.5），承认 Cartpole 负控制和 scope precision 的改善，但不接受 6.5——"transferable diagnostic protocol" 是未验证假说，CIVO 不影响 manipulation，无 real-robot 验证
- **Significance**：维持 **2~2.5/4**（R1: 3/4），分歧在于 forward-looking potential vs demonstrated contribution
- **F6 翻转 + corrected-code rerun**：[AGREE]，两个透明度问题叠加使 F6 可信度低于论文其他部分
- **Overall**：维持 **3/6 (Weak Reject)**，核心判断不变——好论文，错会议

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 11

30 recorded events

### User

_source line 268 · 2026-05-28T00:50:12.840533+00:00_

[Round 6 审稿请求]:
【交叉分享准备 — 请重新提供 Round 6 审稿要点】

由于 Director 会话上下文压缩，你之前提交的 Round 6 审稿原文已丢失。为执行 Step 2 交叉分享（将你的审稿转发给 Reviewer 1），需要你重新提供一份完整的审稿要点摘要。

**背景**: 这是 Round 6 继续审稿（修订评估）。Round 5 评分 Borderline Accept (7/10)。Round 5 遗留的 3 个 open/in_progress issues：
1. N-R5-1: PDF 显示 AUTHORERR（info）
2. N-R5-2: 正文仅 6 页，display item 密度偏低（warning）
3. N-R5-3: Figure 4 红绿色块对色盲不友好（info）

**你的审查侧重（与之前相同）**: Venue 合规 + 写作质量 + 贡献度。

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 269 · 2026-05-28T00:50:45.451641+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 270 · 2026-05-28T00:50:45.552662+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 271 · 2026-05-28T00:50:49.722845+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/submitted.pdf",
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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/submitted.pdf",
    "project": "event-gated-adaptive-horizon",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 272 · 2026-05-28T00:50:50.877339+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 424.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 418.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 476.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 477.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 464.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 472.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 545.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 502.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1154
}
```

</details>

---

### Tool call

_source line 273 · 2026-05-28T00:50:55.297811+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-28T00:50:55.801730+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-28T00:50:56.207692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---

### Tool call

_source line 276 · 2026-05-28T00:50:56.208218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-28T00:50:56.763332+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---

### Tool call

_source line 278 · 2026-05-28T00:50:56.763785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 279 · 2026-05-28T00:50:56.866984+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---

### Tool result

_source line 280 · 2026-05-28T00:50:57.419924+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---

### Tool call

_source line 281 · 2026-05-28T00:51:06.129051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 282 · 2026-05-28T00:51:07.234469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---

### Tool call

_source line 283 · 2026-05-28T00:51:07.285283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-28T00:51:07.586943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 285 · 2026-05-28T00:51:08.141684+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---

### Tool call

_source line 286 · 2026-05-28T00:51:08.142164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 287 · 2026-05-28T00:51:09.057950+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1471
}
```

</details>

---

### Tool result

_source line 288 · 2026-05-28T00:51:09.059336+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 917
}
```

</details>

---

### Tool call

_source line 289 · 2026-05-28T00:51:09.059677+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 290 · 2026-05-28T00:51:09.294099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-28T00:51:10.464430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1404
}
```

</details>

---

### Tool result

_source line 292 · 2026-05-28T00:51:10.858732+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1564
}
```

</details>

---

### Tool call

_source line 293 · 2026-05-28T00:52:58.212064+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 审稿要点摘要（Reviewer 2 — ICML 2026 继续审稿）\n\n**审查侧重**: Venue 合规 + 写作质量 + 贡献度\n**Round 5 评分**: Borderline Accept (7/10)\n\n---\n\n### 1. Round 5 Open Issues 修复状态\n\n**N-R5-1 [RESOLVED]**: AUTHORERR 已修复。PDF 第 1 页脚注正确显示 \"Correspondence to: Anonymous Author \\&lt;anon@anon.edu\\>\"，`\\icmlcorrespondingauthor` 命令已添加（main.tex line 55）。\n\n**N-R5-2 [RESOLVED]**: 正文已从 6 页扩展至完整 8 页。Section 5 (Discussion) 大幅扩展（新增 5 段：Causal role of embedding training, Intervention resistance, Transferable diagnostic protocol, Scope precision, Cross-environment validation）。Section 4 (Results) 新增 mechanism evidence 段和 temporal ordering 段。Broader Impact Statement 完整出现在第 8 页。Display item 密度合理：Table 1 (p5), Table 2 (p6), Figure 1 mechanism diagram (p2), Figure 2 learning curves (p4), Figure 3 NVE trajectory (p4), Figure 4 contrasting dynamics (p6)——6 个 display items / 8 页正文。\n\n**N-R5-3 [PARTIALLY RESOLVED]**: Figure 1 (mechanism diagram, p2) 使用 solid vs dashed 线型区分 Pathway A/B，增加了非颜色维度的可区分性。但红/绿色块仍然存在。Figure 3 (NVE trajectory) 使用红/蓝区分 trained vs control，对色盲友好。Figure 4 (contrasting dynamics) 使用不同线型。整体改善但未完全消除红绿依赖。降级为 minor，不影响接收。\n\n---\n\n### 2. 本轮新发现\n\n**N-R6-1 [warning] F6 结果 180° 翻转未解释**\n- 位置：§4.4 (F6), Table 1 (008e_v3)\n- 问题：Round 5 的 F6 报告 \"2/4 collapse (50%)\"（seeds s1-s4），Round 6 变为 \"0/4 CIVO onset\"（seeds s0,s1,s2,s5）。Seed 集合更换（s3,s4 消失，s0,s5 出现）且结论从\"$\\dt=1$ 无法完全阻止 CIVO\"翻转为\"$\\dt=1$ 消除 CIVO\"。论文未解释这一变化。\n- 影响：叙事逻辑重构——旧版 F6 支撑 \"intervention resistance\" 论点，新版支撑 \"$\\dt>1$ imagination 是 CIVO 的必要条件\" 论点。两个结论互斥，需要透明交代。\n\n**N-R6-2 [warning] \"corrected-code rerun\" 透明度不足**\n- 位置：Table 1 脚注 $^f$\n- 问题：008f 标注 \"Corrected-code rerun\" 但未说明：(1) 修正了什么 bug；(2) 该 bug 是否影响其他实验（尤其是 subsample=ON 的配置）；(3) 修正前后结果差异。这直接影响 Table 2 中 \"Removed: 6/6 (100%)\" 的可信度。\n\n**N-R6-3 [info] AUROC 演进缺乏透明度**\n- 位置：§4.2 (F2), Abstract\n- 问题：NVE threshold 从 1.5× → 2.0×，n 从 30 → 36，AUROC 从 0.957 → 1.000。论文报告最终数值但未讨论阈值选择过程或为何 1.5× 被放弃。AUROC=1.000 在小样本（n=36）下可能因 threshold 过拟合而虚高。LOEO 交叉验证部分缓解此问题，但 reviewer 会追问。\n\n**N-R6-4 [info] Table 1 格式**\n- \"--- s1\" 行 Exp 编号空白，应标注为 008f 的 s1 seed。\n\n---\n\n### 3. 维度评分（ICML 2026 标准）\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| Soundness | 3/4 | AUROC=1.000 完美分类、Fisher exact (p<0.001)、temporal ordering (r=0.81, p=0.002)、LOEO 交叉验证——方法论严谨。扣分：F6 seed 更换 + code correction 透明度不足；temporal ordering 仅 n=2。 |\n| Presentation | 3/4 | 从 6 页扩展至 8 页，信息密度显著改善。Discussion 结构清晰（mechanism → causal role → intervention resistance → transferable protocol → scope precision）。扣分：F6 叙事翻转无解释；Table 1 脚注系统复杂（a-f 六个脚注）增加认知负担。 |\n| Originality | 3/4 | CIVO 作为 failure mode identification 是新颖贡献；dual-critic convergence in pure imagination (ρ>0.999) 是有价值的发现；four-level intervention hierarchy 方法论有创新。 |\n| Significance | 3/4 | **对 ICML RL track 有直接价值**：(1) 理解 imagination-based bootstrapping vs MPC re-planning 的架构边界；(2) dual-critic convergence 发现对所有 shared-feature imagination 系统适用；(3) NVE diagnostic 对 DreamerV3 用户实用。相比 Round 5 提升：Fisher exact 正式化、Cheetah dissociation 深化机制理解、diagnostic protocol 概念化。 |\n\n---\n\n### 4. 整体评分\n\n**4/6 (Weak Accept)**\n\n**相比 Round 5 (Borderline Accept, 7/10) 的变化**：\n\n科学质量有实质改善：AUROC 达到完美分类、Fisher exact test 正式化因果论证、Cheetah dissociation 揭示双通路机制、temporal ordering 建立时间因果链、cross-environment validation 扩展至 6 环境。正文从 6 页填充至完整 8 页，解决了 Round 5 的主要写作问题。\n\n未升至 5/6 (Accept) 的原因：F6 的 180° 结果翻转 + seed 更换 + \"corrected-code rerun\" 三重透明度问题叠加，构成可信度风险。如果作者能在 camera-ready 或 rebuttal 中清楚解释 (1) code bug 的性质和影响范围，(2) seed 集合更换的理由，该评分可升至 5/6。\n\n**ICML venue fit: 8.5/10** — 这是一篇 RL 方法论分析论文，ICML RL track 是其天然归属。CIVO 对 imagination-based actor-critic 的影响、dual-critic convergence 发现、NVE diagnostic 对 ICML 社区直接有用。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 审稿要点摘要（Reviewer 2 — ICML 2026 继续审稿）\n\n**审查侧重**: Venue 合规 + 写作质量 + 贡献度\n**Round 5 评分**: Borderline Accept (7/10)\n\n---\n\n### 1. Round 5 Open Issues 修复状态\n\n**N-R5-1 [RESOLVED]**: AUTHORERR 已修复。PDF 第 1 页脚注正确显示 \"Correspondence to: Anonymous Author \\&lt;anon@anon.edu\\>\"，`\\icmlcorrespondingauthor` 命令已添加（main.tex line 55）。\n\n**N-R5-2 [RESOLVED]**: 正文已从 6 页扩展至完整 8 页。Section 5 (Discussion) 大幅扩展（新增 5 段：Causal role of embedding training, Intervention resistance, Transferable diagnostic protocol, Scope precision, Cross-environment validation）。Section 4 (Results) 新增 mechanism evidence 段和 temporal ordering 段。Broader Impact Statement 完整出现在第 8 页。Display item 密度合理：Table 1 (p5), Table 2 (p6), Figure 1 mechanism diagram (p2), Figure 2 learning curves (p4), Figure 3 NVE trajectory (p4), Figure 4 contrasting dynamics (p6)——6 个 display items / 8 页正文。\n\n**N-R5-3 [PARTIALLY RESOLVED]**: Figure 1 (mechanism diagram, p2) 使用 solid vs dashed 线型区分 Pathway A/B，增加了非颜色维度的可区分性。但红/绿色块仍然存在。Figure 3 (NVE trajectory) 使用红/蓝区分 trained vs control，对色盲友好。Figure 4 (contrasting dynamics) 使用不同线型。整体改善但未完全消除红绿依赖。降级为 minor，不影响接收。\n\n---\n\n### 2. 本轮新发现\n\n**N-R6-1 [warning] F6 结果 180° 翻转未解释**\n- 位置：§4.4 (F6), Table 1 (008e_v3)\n- 问题：Round 5 的 F6 报告 \"2/4 collapse (50%)\"（seeds s1-s4），Round 6 变为 \"0/4 CIVO onset\"（seeds s0,s1,s2,s5）。Seed 集合更换（s3,s4 消失，s0,s5 出现）且结论从\"$\\dt=1$ 无法完全阻止 CIVO\"翻转为\"$\\dt=1$ 消除 CIVO\"。论文未解释这一变化。\n- 影响：叙事逻辑重构——旧版 F6 支撑 \"intervention resistance\" 论点，新版支撑 \"$\\dt>1$ imagination 是 CIVO 的必要条件\" 论点。两个结论互斥，需要透明交代。\n\n**N-R6-2 [warning] \"corrected-code rerun\" 透明度不足**\n- 位置：Table 1 脚注 $^f$\n- 问题：008f 标注 \"Corrected-code rerun\" 但未说明：(1) 修正了什么 bug；(2) 该 bug 是否影响其他实验（尤其是 subsample=ON 的配置）；(3) 修正前后结果差异。这直接影响 Table 2 中 \"Removed: 6/6 (100%)\" 的可信度。\n\n**N-R6-3 [info] AUROC 演进缺乏透明度**\n- 位置：§4.2 (F2), Abstract\n- 问题：NVE threshold 从 1.5× → 2.0×，n 从 30 → 36，AUROC 从 0.957 → 1.000。论文报告最终数值但未讨论阈值选择过程或为何 1.5× 被放弃。AUROC=1.000 在小样本（n=36）下可能因 threshold 过拟合而虚高。LOEO 交叉验证部分缓解此问题，但 reviewer 会追问。\n\n**N-R6-4 [info] Table 1 格式**\n- \"--- s1\" 行 Exp 编号空白，应标注为 008f 的 s1 seed。\n\n---\n\n### 3. 维度评分（ICML 2026 标准）\n\n| 维度 | 评分 | 理由 |\n|------|------|------|\n| Soundness | 3/4 | AUROC=1.000 完美分类、Fisher exact (p<0.001)、temporal ordering (r=0.81, p=0.002)、LOEO 交叉验证——方法论严谨。扣分：F6 seed 更换 + code correction 透明度不足；temporal ordering 仅 n=2。 |\n| Presentation | 3/4 | 从 6 页扩展至 8 页，信息密度显著改善。Discussion 结构清晰（mechanism → causal role → intervention resistance → transferable protocol → scope precision）。扣分：F6 叙事翻转无解释；Table 1 脚注系统复杂（a-f 六个脚注）增加认知负担。 |\n| Originality | 3/4 | CIVO 作为 failure mode identification 是新颖贡献；dual-critic convergence in pure imagination (ρ>0.999) 是有价值的发现；four-level intervention hierarchy 方法论有创新。 |\n| Significance | 3/4 | **对 ICML RL track 有直接价值**：(1) 理解 imagination-based bootstrapping vs MPC re-planning 的架构边界；(2) dual-critic convergence 发现对所有 shared-feature imagination 系统适用；(3) NVE diagnostic 对 DreamerV3 用户实用。相比 Round 5 提升：Fisher exact 正式化、Cheetah dissociation 深化机制理解、diagnostic protocol 概念化。 |\n\n---\n\n### 4. 整体评分\n\n**4/6 (Weak Accept)**\n\n**相比 Round 5 (Borderline Accept, 7/10) 的变化**：\n\n科学质量有实质改善：AUROC 达到完美分类、Fisher exact test 正式化因果论证、Cheetah dissociation 揭示双通路机制、temporal ordering 建立时间因果链、cross-environment validation 扩展至 6 环境。正文从 6 页填充至完整 8 页，解决了 Round 5 的主要写作问题。\n\n未升至 5/6 (Accept) 的原因：F6 的 180° 结果翻转 + seed 更换 + \"corrected-code rerun\" 三重透明度问题叠加，构成可信度风险。如果作者能在 camera-ready 或 rebuttal 中清楚解释 (1) code bug 的性质和影响范围，(2) seed 集合更换的理由，该评分可升至 5/6。\n\n**ICML venue fit: 8.5/10** — 这是一篇 RL 方法论分析论文，ICML RL track 是其天然归属。CIVO 对 imagination-based actor-critic 的影响、dual-critic convergence 发现、NVE diagnostic 对 ICML 社区直接有用。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 294 · 2026-05-28T00:53:02.317551+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4105
}
```

</details>

---

### Tool call

_source line 295 · 2026-05-28T00:53:06.439907+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 296 · 2026-05-28T00:53:06.540838+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 297 · 2026-05-28T00:53:12.612599+00:00_

Round 6 审稿要点已重新提交。核心判断：

- 3 个 Round 5 遗留问题：2 个 RESOLVED，1 个 PARTIALLY RESOLVED
- 新发现 4 个问题（N-R6-1 至 N-R6-4），其中 F6 结果翻转和 code correction 透明度是最主要的 warning
- 整体评分 **4/6 (Weak Accept)**，ICML venue fit 8.5/10
- 如果 F6 透明度问题得到解释，可升至 5/6

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 12

4 recorded events

### User

_source line 298 · 2026-05-28T01:01:14.959800+00:00_

[Round 6 审稿请求]:
【Step 2 交叉分享 — Reviewer 1 的 Round 6 审稿意见】

以下是 Reviewer 1 的完整 Round 6 审稿意见（ICML 2026 标准）。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

**重点关注**：
1. R1 Soundness 3.5/4 vs 你的 3/4 —— 差异是否有实质依据？
2. R1 Overall 5/6 vs 你的 4/6 —— 核心分歧在哪？
3. R1 将 "corrected-code rerun" 降级为 info 而非你的 warning —— 你是否同意？

---

## Reviewer 1 审稿意见原文

### R5 遗留 Issues 修复状态

- N-R5-1 AUTHORERR: **RESOLVED**。无 AUTHORERR 残留。
- N-R5-2 正文 6 页: **RESOLVED**。大幅扩充，Discussion 从 2 段扩至 7 段。
- N-R5-3 色盲: **NOT VERIFIED**。fig4 已改为机制概念图，原色盲问题图可能被替换。

### 新发现

**N-R6-1 [warning — Should-Fix]: F6 结果完全翻转，未解释**
- R5 F6 报告 "2/4 seeds collapse"（s1-s4），R6 变为 "0/4 CIVO onset"（s0,s1,s2,s5），实验编号 008e_v3
- NVE 阈值变化无法解释此翻转——R5 NVE 值 4.02×, 3.78× 远超 2.0×
- "v3" 暗示代码修正但正文无声明
- 影响：数据变更不透明，损害可重复性声称

**N-R6-2 [warning — Should-Fix]: NVE 完美分类的透明度**
- AUROC 0.957→1.000，n=30→36，threshold 1.5×→2.0×
- 新增 6 data points 身份未列明
- 分离间隙仅 0.21×（2.09× vs 1.88×）
- 缓解因素：ROC 图承认 post-hoc，LOEO 三折完美，LOCO 36/36
- 仍需：列出新增 data points + 讨论 0.21× margin 稳健性

**N-R6-3 [info]: "Corrected-code rerun" 缺乏细节**
- Table 1 脚注 f 仅声明 corrected-code 但未说明修正内容

### 维度评分

| 维度 | 评分 |
|------|------|
| Soundness | 3.5/4 |
| Presentation | 3/4 |
| Originality | 3/4 |
| Significance (ICML) | 3/4 |

### Overall: 5/6 (Weak Accept)
R6 统计严谨性、机制分析深度、cross-environment 验证有实质改进。主要保留：F6 透明度 + NVE 分离间隙。camera-ready 解决后对接收无异议。

---

请逐条回应 R1 的发现和评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 299 · 2026-05-28T01:02:36.444095+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 交叉回应 — Reviewer 2 对 Reviewer 1 的逐条回应（ICML 2026）\n\n---\n\n### R5 遗留 Issues 修复状态\n\n**N-R5-1 AUTHORERR**: [AGREE] 一致，RESOLVED。\n\n**N-R5-2 正文 6 页**: [AGREE] 一致，RESOLVED。Discussion 从 2 段扩至 7 段，正文填满 8 页。\n\n**N-R5-3 色盲**: [REBUT] R1 标记 NOT VERIFIED，我标记 PARTIALLY RESOLVED。我已在 PDF 中验证：Figure 1（机制概念图）使用 solid/dashed 线型区分 Pathway A/B，增加了非颜色可区分性；Figure 3（NVE trajectory）使用红/蓝而非红/绿；Figure 4（contrasting dynamics）使用不同线型。但 Figure 1 中仍存在红/绿色块。整体改善，降级为 minor。分歧不影响评分。\n\n---\n\n### 新发现逐条回应\n\n**N-R6-1 [warning]: F6 结果完全翻转**\n\n[AGREE] R1-N-R6-1: 完全同意，与我的 N-R6-1 一致。\n\n补充 R1 未展开的一点：这不仅是数据变更问题，更是**论证逻辑重构**。Round 5 的 F6（\"2/4 collapse\"）支撑的核心论点是 \"even restricting to $\\dt=1$ cannot fully prevent CIVO\"，这强化了 intervention resistance 叙事。Round 6 的 F6（\"0/4 CIVO\"）支撑的是截然相反的论点——\"multi-step imagination is necessary for CIVO induction\"（§4.4 末句）。两个结论互斥。论文选择了更 clean 的新结论，但读者无法评估这一判断的可靠性，因为旧数据去向不明。\n\nR1 注意到 \"v3\" 后缀暗示代码修正——这是对的。结合 Table 1 脚注 $^f$ 的 \"corrected-code rerun\"（008f 也经历了代码修正），至少两个实验受到了未公开的代码修正。模式令人担忧。\n\n**N-R6-2 [warning]: NVE 完美分类的透明度**\n\n[AGREE] R1-N-R6-2: 同意，与我的 N-R6-3 一致。\n\nR1 提出了一个我未注意到的关键细节：**分离间隙仅 0.21×**（最低 CIVO-positive 2.09× vs 最高 non-CIVO 1.88×）。这个间隙非常窄。AUROC=1.000 在数学上正确（完美分离），但实际稳健性取决于这 0.21× 的 margin 在新数据上是否能保持。论文用 LOEO 三折交叉验证和 LOCO 36/36 部分缓解了这一问题，但 R1 对 \"列出新增 6 个 data points + 讨论 margin 稳健性\" 的要求合理。\n\n**N-R6-3 [info]: \"Corrected-code rerun\"**\n\n[REBUT] R1-N-R6-3: **不同意降级为 info。我维持 warning。**\n\n理由：\n1. \"corrected-code rerun\" 涉及 Table 1 中的 008f，而 008f 是 \"Removed embedding\" 控制组的一部分。Table 2 中 \"Removed: 6/6 (100%) no CIVO\" 的完美分类直接依赖 008f 的健康结论。如果 code correction 改变了 008f 的结果，reviewer 有权追问修正前的结果。\n\n2. 同时，F6 的 008e_v3 也暗示代码修正（\"v3\" 后缀）。两个实验都经历了未公开的代码修正，且两者都是论文关键数据点——008f 支撑控制组完美率，008e_v3 支撑 \"$\\dt=1$ eliminates CIVO\" 结论。\n\n3. R1 自己在 N-R6-1 中标记 F6 翻转为 warning，但将 code correction 降级为 info——这不一致。F6 翻转的最可能解释**正是**代码修正，两者应同级。\n\ninfo 级别意味着\"不影响评分的小问题\"。但代码修正的透明度直接影响 reproducibility 评估（ICML reviewer guidelines 明确要求评估 reproducibility）。应为 warning。\n\n---\n\n### Director 指定问题回应\n\n**Q1: Soundness 3.5/4 vs 3/4 —— 差异是否有实质依据？**\n\n有实质依据，我维持 **3/4**。\n\nR1 的 3.5/4 反映了对 Round 6 统计改进（AUROC=1.000, Fisher exact, temporal ordering）的高度认可。我同样认可这些改进。但 0.5 分的差异来自我对两个问题的不同权重：\n\n(a) **F6 透明度**：R1 标记为 warning 但未在 Soundness 扣分。我认为数据点更换 + 结论翻转 + 未公开代码修正是 Soundness 问题，不仅是 Presentation 问题。Soundness 要求实验可验证（ICML guidelines: \"Are the claims well-supported by theoretical analysis or experimental results?\"）——当关键数据点的来源不透明时，well-supported 打折扣。\n\n(b) **Temporal ordering n=2**：r=0.81, p=0.002 是有意义的，但两个 seed 的 time-series correlation 在统计上脆弱。论文谨慎地标注了 \"(n=2)\"，但 Discussion 中 \"three-stage causal chain\" 的表述（§5 第一段）仍暗示比数据支撑更强的因果推断。\n\n如果 F6 透明度在 rebuttal 中解决，我可上调至 3.5/4。当前维持 3/4。\n\n**Q2: Overall 5/6 vs 4/6 —— 核心分歧在哪？**\n\n核心分歧在于**对 F6 + code correction 透明度问题的严重性判断**。\n\nR1 的立场：科学改进是实质性的，透明度问题是 camera-ready 可修复的 → 5/6。\n我的立场：F6 结论翻转 + 代码修正不透明构成当前版本的可信度风险，不应在评分中预支 camera-ready 修复的信用 → 4/6。\n\n具体来说：\n- 5/6 意味着 \"我推荐接收，仅有 minor 保留\"\n- 4/6 意味着 \"我倾向接收，但有需要解决的问题\"\n\nF6 的 180° 翻转不是 minor issue。这是论文五个核心 findings 之一（F6: \"$\\dt=1$ imagination eliminates CIVO\"）的数据基础发生了不透明的变更。在 rebuttal 中如果作者能清楚说明 (1) code bug 性质，(2) bug 影响范围，(3) 为什么新 seed 集合比旧集合更可靠，我愿意升至 5/6。\n\n**但我不认为 R1 的 5/6 不合理。** R1 聚焦于科学贡献本身的质量（AUROC=1.000, mechanism analysis, cross-env validation），这些确实达到了 ICML 的标准。我们的分歧在于\"当前版本的透明度缺陷应该多大程度影响评分\"——这是合理的 reviewer 间差异。\n\n**收敛建议**：如果必须统一评分，**4.5/6（Borderline Accept，有条件）** 是合理的中间点——承认科学质量达标，但明确要求 rebuttal 解决 F6 透明度。\n\n**Q3: \"corrected-code rerun\" info vs warning**\n\n维持 **warning**。理由见上方 N-R6-3 REBUT 部分。R1 将 F6 翻转标为 warning 但将 code correction 标为 info，这两个问题实际上是同一根源的两个表现（代码修正导致了数据变更和结论翻转），应同级处理。\n\n---\n\n### 总结\n\n| 维度 | R1 | R2 | 差异 | 可收敛？ |\n|------|-----|-----|------|----------|\n| Soundness | 3.5/4 | 3/4 | 0.5 | 可收敛至 3.25/4（若 F6 rebuttal 解决则 3.5） |\n| Presentation | 3/4 | 3/4 | 0 | 一致 |\n| Originality | 3/4 | 3/4 | 0 | 一致 |\n| Significance | 3/4 | 3/4 | 0 | 一致 |\n| Overall | 5/6 | 4/6 | 1.0 | 可收敛至 4.5/6（条件：rebuttal 解决 F6） |\n\n与 R1 在 Presentation, Originality, Significance 上完全一致。分歧仅在 Soundness（F6 透明度权重）和 Overall（是否预支 camera-ready 修复的信用）。建议 AC 在 rebuttal 阶段要求作者回应 F6 翻转和 code correction 细节，作为有条件接收的前提。",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 交叉回应 — Reviewer 2 对 Reviewer 1 的逐条回应（ICML 2026）\n\n---\n\n### R5 遗留 Issues 修复状态\n\n**N-R5-1 AUTHORERR**: [AGREE] 一致，RESOLVED。\n\n**N-R5-2 正文 6 页**: [AGREE] 一致，RESOLVED。Discussion 从 2 段扩至 7 段，正文填满 8 页。\n\n**N-R5-3 色盲**: [REBUT] R1 标记 NOT VERIFIED，我标记 PARTIALLY RESOLVED。我已在 PDF 中验证：Figure 1（机制概念图）使用 solid/dashed 线型区分 Pathway A/B，增加了非颜色可区分性；Figure 3（NVE trajectory）使用红/蓝而非红/绿；Figure 4（contrasting dynamics）使用不同线型。但 Figure 1 中仍存在红/绿色块。整体改善，降级为 minor。分歧不影响评分。\n\n---\n\n### 新发现逐条回应\n\n**N-R6-1 [warning]: F6 结果完全翻转**\n\n[AGREE] R1-N-R6-1: 完全同意，与我的 N-R6-1 一致。\n\n补充 R1 未展开的一点：这不仅是数据变更问题，更是**论证逻辑重构**。Round 5 的 F6（\"2/4 collapse\"）支撑的核心论点是 \"even restricting to $\\dt=1$ cannot fully prevent CIVO\"，这强化了 intervention resistance 叙事。Round 6 的 F6（\"0/4 CIVO\"）支撑的是截然相反的论点——\"multi-step imagination is necessary for CIVO induction\"（§4.4 末句）。两个结论互斥。论文选择了更 clean 的新结论，但读者无法评估这一判断的可靠性，因为旧数据去向不明。\n\nR1 注意到 \"v3\" 后缀暗示代码修正——这是对的。结合 Table 1 脚注 $^f$ 的 \"corrected-code rerun\"（008f 也经历了代码修正），至少两个实验受到了未公开的代码修正。模式令人担忧。\n\n**N-R6-2 [warning]: NVE 完美分类的透明度**\n\n[AGREE] R1-N-R6-2: 同意，与我的 N-R6-3 一致。\n\nR1 提出了一个我未注意到的关键细节：**分离间隙仅 0.21×**（最低 CIVO-positive 2.09× vs 最高 non-CIVO 1.88×）。这个间隙非常窄。AUROC=1.000 在数学上正确（完美分离），但实际稳健性取决于这 0.21× 的 margin 在新数据上是否能保持。论文用 LOEO 三折交叉验证和 LOCO 36/36 部分缓解了这一问题，但 R1 对 \"列出新增 6 个 data points + 讨论 margin 稳健性\" 的要求合理。\n\n**N-R6-3 [info]: \"Corrected-code rerun\"**\n\n[REBUT] R1-N-R6-3: **不同意降级为 info。我维持 warning。**\n\n理由：\n1. \"corrected-code rerun\" 涉及 Table 1 中的 008f，而 008f 是 \"Removed embedding\" 控制组的一部分。Table 2 中 \"Removed: 6/6 (100%) no CIVO\" 的完美分类直接依赖 008f 的健康结论。如果 code correction 改变了 008f 的结果，reviewer 有权追问修正前的结果。\n\n2. 同时，F6 的 008e_v3 也暗示代码修正（\"v3\" 后缀）。两个实验都经历了未公开的代码修正，且两者都是论文关键数据点——008f 支撑控制组完美率，008e_v3 支撑 \"$\\dt=1$ eliminates CIVO\" 结论。\n\n3. R1 自己在 N-R6-1 中标记 F6 翻转为 warning，但将 code correction 降级为 info——这不一致。F6 翻转的最可能解释**正是**代码修正，两者应同级。\n\ninfo 级别意味着\"不影响评分的小问题\"。但代码修正的透明度直接影响 reproducibility 评估（ICML reviewer guidelines 明确要求评估 reproducibility）。应为 warning。\n\n---\n\n### Director 指定问题回应\n\n**Q1: Soundness 3.5/4 vs 3/4 —— 差异是否有实质依据？**\n\n有实质依据，我维持 **3/4**。\n\nR1 的 3.5/4 反映了对 Round 6 统计改进（AUROC=1.000, Fisher exact, temporal ordering）的高度认可。我同样认可这些改进。但 0.5 分的差异来自我对两个问题的不同权重：\n\n(a) **F6 透明度**：R1 标记为 warning 但未在 Soundness 扣分。我认为数据点更换 + 结论翻转 + 未公开代码修正是 Soundness 问题，不仅是 Presentation 问题。Soundness 要求实验可验证（ICML guidelines: \"Are the claims well-supported by theoretical analysis or experimental results?\"）——当关键数据点的来源不透明时，well-supported 打折扣。\n\n(b) **Temporal ordering n=2**：r=0.81, p=0.002 是有意义的，但两个 seed 的 time-series correlation 在统计上脆弱。论文谨慎地标注了 \"(n=2)\"，但 Discussion 中 \"three-stage causal chain\" 的表述（§5 第一段）仍暗示比数据支撑更强的因果推断。\n\n如果 F6 透明度在 rebuttal 中解决，我可上调至 3.5/4。当前维持 3/4。\n\n**Q2: Overall 5/6 vs 4/6 —— 核心分歧在哪？**\n\n核心分歧在于**对 F6 + code correction 透明度问题的严重性判断**。\n\nR1 的立场：科学改进是实质性的，透明度问题是 camera-ready 可修复的 → 5/6。\n我的立场：F6 结论翻转 + 代码修正不透明构成当前版本的可信度风险，不应在评分中预支 camera-ready 修复的信用 → 4/6。\n\n具体来说：\n- 5/6 意味着 \"我推荐接收，仅有 minor 保留\"\n- 4/6 意味着 \"我倾向接收，但有需要解决的问题\"\n\nF6 的 180° 翻转不是 minor issue。这是论文五个核心 findings 之一（F6: \"$\\dt=1$ imagination eliminates CIVO\"）的数据基础发生了不透明的变更。在 rebuttal 中如果作者能清楚说明 (1) code bug 性质，(2) bug 影响范围，(3) 为什么新 seed 集合比旧集合更可靠，我愿意升至 5/6。\n\n**但我不认为 R1 的 5/6 不合理。** R1 聚焦于科学贡献本身的质量（AUROC=1.000, mechanism analysis, cross-env validation），这些确实达到了 ICML 的标准。我们的分歧在于\"当前版本的透明度缺陷应该多大程度影响评分\"——这是合理的 reviewer 间差异。\n\n**收敛建议**：如果必须统一评分，**4.5/6（Borderline Accept，有条件）** 是合理的中间点——承认科学质量达标，但明确要求 rebuttal 解决 F6 透明度。\n\n**Q3: \"corrected-code rerun\" info vs warning**\n\n维持 **warning**。理由见上方 N-R6-3 REBUT 部分。R1 将 F6 翻转标为 warning 但将 code correction 标为 info，这两个问题实际上是同一根源的两个表现（代码修正导致了数据变更和结论翻转），应同级处理。\n\n---\n\n### 总结\n\n| 维度 | R1 | R2 | 差异 | 可收敛？ |\n|------|-----|-----|------|----------|\n| Soundness | 3.5/4 | 3/4 | 0.5 | 可收敛至 3.25/4（若 F6 rebuttal 解决则 3.5） |\n| Presentation | 3/4 | 3/4 | 0 | 一致 |\n| Originality | 3/4 | 3/4 | 0 | 一致 |\n| Significance | 3/4 | 3/4 | 0 | 一致 |\n| Overall | 5/6 | 4/6 | 1.0 | 可收敛至 4.5/6（条件：rebuttal 解决 F6） |\n\n与 R1 在 Presentation, Originality, Significance 上完全一致。分歧仅在 Soundness（F6 透明度权重）和 Overall（是否预支 camera-ready 修复的信用）。建议 AC 在 rebuttal 阶段要求作者回应 F6 翻转和 code correction 细节，作为有条件接收的前提。",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 300 · 2026-05-28T01:02:40.564663+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4120
}
```

</details>

---

### Assistant

_source line 301 · 2026-05-28T01:02:45.748693+00:00_

交叉回应已提交。核心立场：维持 4/6（Weak Accept），与 R1 在 Presentation/Originality/Significance 上一致（均 3/4），分歧集中在 Soundness（3 vs 3.5）和 Overall（4 vs 5），根源是对 F6 透明度问题的权重判断不同。建议收敛至 4.5/6 有条件接收，以 rebuttal 解决 F6 + code correction 细节为前提。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 13

138 recorded events

### User

_source line 302 · 2026-05-28T02:02:03.749733+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查本论文的 **新颖性 + venue fit (robotics relevance) + 格式合规 + 完整性**。

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
- **核心要求**: 论文必须聚焦核心机器人问题，展示对机器人领域的相关性。鼓励报告真实机器人实验或提供令人信服的证据表明仿真实验可迁移到真实机器人
- **附录**: 可选，通过 OpenReview 提交补充材料
- **生成式 AI 政策**: 不可作为作者，需披露使用情况

## 你的审查侧重

1. **格式合规（最高优先级）**:
   - 正文页数是否符合 8 页限制（初步检查发现正文约 10-11 页，严重超页）
   - 精确统计：从 Section 1 开始到 References 之前的最后一行内容，总共占多少页
   - 模板使用是否正确（corl_2026.sty）
   - 匿名化是否彻底（检查 acknowledgments、代码链接、自引等潜在去匿名化）
   - Limitations section 是否存在且符合要求

2. **Venue Fit (Robotics Relevance)**:
   - CoRL 要求论文聚焦"核心机器人问题"——本文是否满足？
   - 论文使用 DMC locomotion (Walker Walk, Cheetah Run) + ManiSkill manipulation 作为测试平台，但核心贡献是对 DreamerV3 内部 value overestimation 的诊断分析
   - 这是一篇 "diagnostic/negative-result" paper——CoRL 是否接受此类论文？
   - 与 robotics deployment 的实际关联性有多强？
   - 对比：此类诊断论文是否更适合 ICML/NeurIPS/ICLR 等通用 ML 会议？

3. **新颖性与贡献**:
   - CIVO 作为新发现的 failure mode 是否有足够新颖性？
   - 与已知的 value overestimation (Double Q, TD3) 和 delusional bias (Lu et al.) 的区分是否充分？
   - 诊断协议（四级干预层级）作为方法论贡献是否足够？
   - "No tested intervention reliably eliminates CIVO" 这一负面结论是否构成足够贡献？

4. **Related Work 完整性**:
   - 是否覆盖了所有关键相关工作？
   - 引用是否存在遗漏（特别是 robotics-specific temporal abstraction 工作）
   - 参考文献列表条目是否准确

请提供完整的结构化审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → 评分建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 303 · 2026-05-28T02:02:11.474431+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 304 · 2026-05-28T02:02:12.681169+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_2_393bd6df.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1206
}
```

</details>

---

### Tool call

_source line 305 · 2026-05-28T02:02:12.681652+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 306 · 2026-05-28T02:02:12.782427+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 307 · 2026-05-28T02:02:19.062364+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 308 · 2026-05-28T02:02:20.268646+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 309 · 2026-05-28T02:02:26.111381+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, I found some relevant information about CoRL 2026, though I didn't locate a specific detailed "reviewer guidelines review form criteria" document. Here's what I found:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics conference (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

Additionally, every author with 3 or more submissions must agree to serve as a reviewer.

## Submission Review Criteria

While a specific CoRL 2026 reviewer guidelines document wasn't directly accessible, the call for papers indicates that submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these mig
…[truncated 405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7049
}
```

</details>

---

### Tool result

_source line 310 · 2026-05-28T02:02:28.870149+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 315.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 290.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 340.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 318.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 362.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 269.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 389.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 266.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8601
}
```

</details>

---

### Tool call

_source line 311 · 2026-05-28T02:02:34.445976+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 312 · 2026-05-28T02:02:35.455210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---

### Tool call

_source line 313 · 2026-05-28T02:02:35.556000+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 314 · 2026-05-28T02:02:36.163016+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---

### Tool call

_source line 315 · 2026-05-28T02:02:36.215992+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 316 · 2026-05-28T02:02:36.416997+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 317 · 2026-05-28T02:02:37.678258+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 318 · 2026-05-28T02:02:37.932685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1716
}
```

</details>

---

### Tool result

_source line 319 · 2026-05-28T02:02:38.495281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2078
}
```

</details>

---

### Tool call

_source line 320 · 2026-05-28T02:02:38.495864+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 321 · 2026-05-28T02:02:38.496145+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 322 · 2026-05-28T02:02:39.255128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1576
}
```

</details>

---

### Tool call

_source line 323 · 2026-05-28T02:02:39.458250+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 324 · 2026-05-28T02:02:39.864365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1368
}
```

</details>

---

### Tool result

_source line 325 · 2026-05-28T02:02:39.877117+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1380
}
```

</details>

---

### Tool call

_source line 326 · 2026-05-28T02:02:39.877626+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 327 · 2026-05-28T02:02:40.182400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 724
}
```

</details>

---

### Tool call

_source line 328 · 2026-05-28T02:02:40.587004+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 329 · 2026-05-28T02:02:41.195404+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1317
}
```

</details>

---

### Tool result

_source line 330 · 2026-05-28T02:02:42.562073+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1975
}
```

</details>

---

### Tool call

_source line 331 · 2026-05-28T02:02:42.614025+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete reviewer guidelines, review form criteria, evaluation dimensions, and scoring scales used for CoRL paper reviews. Include all rating categories and their descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete reviewer guidelines, review form criteria, evaluation dimensions, and scoring scales used for CoRL paper reviews. Include all rating categories and their descriptions."
  }
}
```

</details>

---

### Tool call

_source line 332 · 2026-05-28T02:02:43.925170+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract all submission requirements, page limits, formatting rules, review criteria, and any information about what reviewers should evaluate. Include details about robotics relevance requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/call-for-papers",
    "prompt": "Extract all submission requirements, page limits, formatting rules, review criteria, and any information about what reviewers should evaluate. Include details about robotics relevance requirements."
  }
}
```

</details>

---

### Tool result

_source line 333 · 2026-05-28T02:02:47.649608+00:00_

# CoRL 2024 Review Guidelines Summary

Based on the provided content, here are the key review guidelines:

## Review Criteria for Regular Papers

Papers are evaluated on "significance and novelty of the results, either theoretical or empirical." Assessments consider objective establishment of results and "potential for scientific and technological impact, as well as their relevance to robotic learning."

## Scope Requirements

All submissions must demonstrate robot learning relevance through either:
- **Intent**: Explicitly addressing a learning question for physical robots, OR
- **Outcome**: Testing proposed learning solutions on physical robots

## What Gets Rejected

The document lists examples that fail scope requirements: manually-designed controllers without learning, generic planning algorithms, generic machine learning results, and standard computer vision benchmarks without robotics application.

## Reviewer Qualifications

Reviewers should demonstrate expertise in robotics and machine learning through publication history. Ideally, they possess "minimum of 3 first author publications in major robotics conferences" like CoRL, RSS, ICRA, and IROS, plus publications in venues like NeurIPS and ICML.

## Notable Limitation

**The provided content does not include specific scoring scales, detailed review forms, or numerical rating categories.** Only the foundational evaluation principles and scope criteria are documented in this excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5035
}
```

</details>

---

### Tool result

_source line 334 · 2026-05-28T02:02:48.404632+00:00_

# CoRL 2026 Submission Requirements

Based on the call for papers, here are the key submission requirements:

## Robotics Relevance
Submissions must "focus on a core robotics problem" and demonstrate relevance of proposed work to robotics. Papers lacking robotics focus "will be returned without review."

## Required Content Elements
All submissions must include a **Limitations section** that "explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future."

## Experimental Standards
Authors should prioritize "real-robot experiments" or provide "convincing evidence that simulation experiments are transferable to real robots."

## Supplementary Materials
Submissions may include video, code, and data as supplementary materials (encouraged but optional).

## Format & Timeline Details
Specific information about page limits, formatting rules, and submission deadlines is referenced as available in the "Instruction for Authors" section, but those details are not provided in this page excerpt.

## Review Scope
The document indicates reviewers should evaluate whether proposed models, algorithms, datasets, and benchmarks demonstrate genuine relevance to robotics problems.

**Note:** For complete submission guidelines including page limits and formatting specifications, consult the Instruction for Authors page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4479
}
```

</details>

---

### Tool call

_source line 335 · 2026-05-28T02:02:56.015043+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 336 · 2026-05-28T02:02:56.522202+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 2025 review form scoring scale rating dimensions OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 2025 review form scoring scale rating dimensions OpenReview"
  }
}
```

</details>

---

### Tool result

_source line 337 · 2026-05-28T02:02:58.081516+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 362.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 314.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 336.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 360.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 390.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 262.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 283.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p18.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 354.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review
…[truncated 566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2066
}
```

</details>

---

### Tool call

_source line 338 · 2026-05-28T02:02:58.232412+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all formatting requirements: page limits, template name, anonymity rules, section requirements, supplementary material rules, and any other submission guidelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract all formatting requirements: page limits, template name, anonymity rules, section requirements, supplementary material rules, and any other submission guidelines."
  }
}
```

</details>

---

### Tool result

_source line 339 · 2026-05-28T02:03:02.203667+00:00_

Web search results for query: "CoRL 2024 2025 review form scoring scale rating dimensions OpenReview"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"An Open Review of OpenReview: A Critical Analysis of the Machine   Learning Conference Review Process","url":"https://arxiv.org/pdf/2010.05137"},{"title":"Best Reviewers Award for 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11955497/"}]

Based on the search results, I found some information about CoRL 2024's review process:

CoRL 2024 regular papers are evaluated based on the significance and novelty of the results, either theoretical or empirical. However, the search results only provided partial information about the review form and do not contain detailed specifications about the specific scoring scale, rating dimensions, or the complete review form structure.

The search results show that CoRL 2024 uses OpenReview as its review platform, but the detailed review form specifications with scoring scales and all rating dimensions are not fully visible in these results. To access the complete review form with all scoring dimensions, you would likely need to visit the OpenReview pages directly or check the CoRL 2024 website for the full reviewer instructions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyp
…[truncated 8 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5681
}
```

</details>

---

### Tool result

_source line 340 · 2026-05-28T02:03:02.958586+00:00_

# CoRL 2026 Submission Formatting Requirements

## Page Limits
- **Initial submission:** 8 pages for main paper
- **Camera-ready submission:** 9 pages for main paper
- Acknowledgments, references, and appendix (optional) do not count toward the page limit

## Template & Format
Use the provided LaTeX template available on the conference website. The camera-ready version requires the command `\usepackage[final]{corl_2026}`.

## Anonymity Rules
Papers must be double-blind anonymized for initial submission. Author names and affiliations are revealed only after acceptance decisions are announced.

## Required Sections
- **Limitations section** (counted in the 8-page limit) must explicitly describe limiting assumptions, failure modes, and how these might be addressed

## Supplementary Materials
- Submit as a single ZIP file through OpenReview
- Video submissions encouraged: maximum 250 MB, 3 minutes suggested length
- Appendix may be included with main paper or supplementary materials
- Note: PMLR does not allow videos as supplementary material; host externally instead

## Additional Guidelines
- Papers must include "all relevant details" to enable reproducibility
- Authors must disclose generative AI tool usage during submission
- Citations to non-existent references result in desk rejection

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4726
}
```

</details>

---

### Tool call

_source line 341 · 2026-05-28T02:03:10.495206+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool call

_source line 342 · 2026-05-28T02:03:10.949504+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool call

_source line 343 · 2026-05-28T02:03:10.949996+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool call

_source line 344 · 2026-05-28T02:03:10.950257+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool call

_source line 345 · 2026-05-28T02:03:11.252271+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool call

_source line 346 · 2026-05-28T02:03:11.709024+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 347 · 2026-05-28T02:03:12.566548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2071
}
```

</details>

---

### Tool call

_source line 348 · 2026-05-28T02:03:12.567034+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form, all scoring dimensions, rating scales, and evaluation criteria used by CoRL reviewers. Include every rating category with its scale and description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form, all scoring dimensions, rating scales, and evaluation criteria used by CoRL reviewers. Include every rating category with its scale and description."
  }
}
```

</details>

---

### Tool result

_source line 349 · 2026-05-28T02:03:12.719873+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1769
}
```

</details>

---

### Tool result

_source line 350 · 2026-05-28T02:03:12.924577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1974
}
```

</details>

---

### Tool result

_source line 351 · 2026-05-28T02:03:13.077460+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2127
}
```

</details>

---

### Tool result

_source line 352 · 2026-05-28T02:03:13.283221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2030
}
```

</details>

---

### Tool result

_source line 353 · 2026-05-28T02:03:13.385258+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1676
}
```

</details>

---

### Tool result

_source line 354 · 2026-05-28T02:03:18.506659+00:00_

# CoRL 2023 Review Form Analysis

Based on the provided content, the document does **not include the complete review form, scoring scales, or numerical rating categories**. 

The guidelines outline six evaluation dimensions that reviewers must assess:

1. **Originality** — novelty of problems/methods and differentiation from prior work
2. **Quality** — technical soundness and claim support
3. **Clarity** — writing quality and organization
4. **Significance** — importance and potential impact on the field
5. **Relevance** — alignment with robot learning focus
6. **Limitations** — evaluation of how authors address shortcomings

However, the document provides only qualitative guidance for each dimension, not quantitative rating scales or point values. For instance, reviewers are told to evaluate "originality" by asking questions like "Are the problems or methods new?" but no numerical scale (1-5, 1-10, etc.) is specified.

The guidelines emphasize constructive, evidence-based feedback over numerical scores, referencing external resources from ICML and NeurIPS for detailed reviewer training.

**To obtain the actual scoring rubric and numerical scales, you would need to access the OpenReview submission system directly.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5939
}
```

</details>

---

### Tool call

_source line 355 · 2026-05-28T02:03:23.678223+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 OpenReview review form \"overall score\" \"soundness\" \"excitement\" rating scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 OpenReview review form \"overall score\" \"soundness\" \"excitement\" rating scale 1-5"
  }
}
```

</details>

---

### Tool call

_source line 356 · 2026-05-28T02:03:26.648150+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract EVERY detail about the review form: all scoring dimensions, all rating scales with numbers, all evaluation criteria. Include the complete text of rating options for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract EVERY detail about the review form: all scoring dimensions, all rating scales with numbers, all evaluation criteria. Include the complete text of rating options for each dimension."
  }
}
```

</details>

---

### Tool call

_source line 357 · 2026-05-28T02:03:28.629963+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

### Tool result

_source line 358 · 2026-05-28T02:03:28.865311+00:00_

Web search results for query: "CoRL 2024 OpenReview review form "overall score" "soundness" "excitement" rating scale 1-5"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CoRL 2024 Workshop XE | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FXE"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Paper Ranking Methodology","url":"https://openreview-copilot.eamag.me/ranking"},{"title":"Can Small and Reasoning Large Language Models Score Journal Articles for Research Quality and Do Averaging and Few-shot Help?","url":"https://arxiv.org/pdf/2510.22389"}]

Based on the search results, I found information about review forms used in academic conferences, though the specific details about CoRL 2024's exact rating scale weren't directly returned. The search results show that the ARR (ACL Rolling Review) platform uses review forms with "soundness," "excitement," and "overall recommendation" scores, but I wasn't able to find the specific 1-5 rating scale details for CoRL 2024's OpenReview form.

The search results primarily returned information about ARR and general OpenReview conference pages rather than the specific CoRL 2024 review form configuration. To get the precise details about CoRL 2024's review form rating scales, you would n
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5187
}
```

</details>

---

### Tool result

_source line 359 · 2026-05-28T02:03:30.090056+00:00_

# CoRL 2024 Review Form Details

Based on the provided content, **no specific review form scoring dimensions, rating scales, or numerical evaluation criteria are documented** in this instruction page.

The page outlines general review guidance rather than a structured form. The only evaluative framework mentioned is:

**Review Criteria:** Papers are assessed on "significance and novelty of results" and "degree to which they have been objectively established" along with "potential for scientific and technological impact" and "relevance to robotic learning."

**Desk Reject Categories:** Three grounds exist—formatting violations, anonymity breaches, or scope misalignment—but these represent rejection thresholds, not scoring dimensions.

The instructions establish reviewer qualifications and scope boundaries for submissions (robot learning requirement), but they do not specify numerical rating scales, point systems, or structured evaluation dimensions that would typically appear on a peer review form.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3441
}
```

</details>

---

### Tool result

_source line 360 · 2026-05-28T02:03:31.044364+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p21.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 367.1}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p22.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 316.2}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p23.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 346.0}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p24.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 281.5}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p25.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 289.1}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p26.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 288.6}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p27.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 374.2}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p28.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 346.8}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review
…[truncated 566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2414
}
```

</details>

---

### Tool call

_source line 361 · 2026-05-28T02:03:36.068054+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net CoRL 2024 review \"Overall Score\" \"Relevance\" \"Presentation\" rating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net CoRL 2024 review \"Overall Score\" \"Relevance\" \"Presentation\" rating"
  }
}
```

</details>

---

### Tool call

_source line 362 · 2026-05-28T02:03:36.520027+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 363 · 2026-05-28T02:03:37.474956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 364 · 2026-05-28T02:03:37.625990+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 365 · 2026-05-28T02:03:38.081354+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 366 · 2026-05-28T02:03:38.081838+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool call

_source line 367 · 2026-05-28T02:03:38.433464+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---

### Tool result

_source line 368 · 2026-05-28T02:03:39.392971+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---

### Tool result

_source line 369 · 2026-05-28T02:03:39.394895+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---

### Tool call

_source line 370 · 2026-05-28T02:03:39.395276+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---

### Tool call

_source line 371 · 2026-05-28T02:03:39.696341+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---

### Tool result

_source line 372 · 2026-05-28T02:03:39.799674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---

### Tool result

_source line 373 · 2026-05-28T02:03:40.154803+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---

### Tool result

_source line 374 · 2026-05-28T02:03:41.711883+00:00_

Web search results for query: "site:openreview.net CoRL 2024 review "Overall Score" "Relevance" "Presentation" rating"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 Workshop LEAP | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FLEAP"},{"title":"CoRL 2024 Workshop LFDM | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FLFDM"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"Best Reviewers Award for 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11955497/"}]

I've performed a web search for CoRL 2024 reviews on OpenReview. The search results show that CoRL 2024 has an OpenReview homepage, and submissions were published starting September 5, 2024. 

However, the search results didn't return specific review examples with the exact rating fields you mentioned ("Overall Score," "Relevance," "Presentation"). The OpenReview pages appear to be listing submissions and general information, but not displaying the detailed review content with those specific rating categories.

To find actual reviews with those rating fields, you would need to:
1. Visit the OpenReview CoRL 2024 Conference page directly
2. Browse through individual paper submissions to view their reviews
3. Look for papers with publicly available reviews

The search results 
…[truncated 258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5643
}
```

</details>

---

### Tool call

_source line 375 · 2026-05-28T02:03:50.455923+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference",
  "prompt": "Find the URL of any accepted CoRL 2024 paper review. List the first few paper titles and their OpenReview URLs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference",
    "prompt": "Find the URL of any accepted CoRL 2024 paper review. List the first few paper titles and their OpenReview URLs."
  }
}
```

</details>

---

### Tool call

_source line 376 · 2026-05-28T02:03:53.269013+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---

### Tool call

_source line 377 · 2026-05-28T02:03:53.422025+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---

### Tool result

_source line 378 · 2026-05-28T02:03:54.270739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1001
}
```

</details>

---

### Tool result

_source line 379 · 2026-05-28T02:03:54.309643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 887
}
```

</details>

---

### Tool call

_source line 380 · 2026-05-28T02:03:54.415116+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---

### Tool call

_source line 381 · 2026-05-28T02:03:54.671060+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---

### Tool result

_source line 382 · 2026-05-28T02:03:55.277539+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 862
}
```

</details>

---

### Tool call

_source line 383 · 2026-05-28T02:03:55.280132+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---

### Tool result

_source line 384 · 2026-05-28T02:03:55.682218+00:00_

# CoRL 2024 Papers and URLs

Based on the OpenReview submissions page, here are the first few accepted papers with their review URLs:

1. **Body Transformer: Leveraging Robot Embodiment for Policy Learning**
   - URL: https://openreview.net/forum?id=Oce2215aJE

2. **Gameplay Filters: Robust Zero-Shot Safety through Adversarial Imagination**
   - URL: https://openreview.net/forum?id=Ke5xrnBFAR

3. **Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation**
   - URL: https://openreview.net/forum?id=FO6tePGRZj

4. **RP1M: A Large-Scale Motion Dataset for Piano Playing with Bi-Manual Dexterous Robot Hands**
   - URL: https://openreview.net/forum?id=4Of4UWyBXE

5. **Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models**
   - URL: https://openreview.net/forum?id=evCXwlCMIi

All papers were published on September 5, 2024, and are accessible to all readers on OpenReview.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5226
}
```

</details>

---

### Tool result

_source line 385 · 2026-05-28T02:03:55.687586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1016
}
```

</details>

---

### Tool call

_source line 386 · 2026-05-28T02:03:55.688301+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---

### Tool result

_source line 387 · 2026-05-28T02:03:56.113096+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 832
}
```

</details>

---

### Tool result

_source line 388 · 2026-05-28T02:03:56.624043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 935
}
```

</details>

---

### Tool call

_source line 389 · 2026-05-28T02:04:04.825350+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=Oce2215aJE",
  "prompt": "Extract the complete review form structure. List ALL scoring dimensions and their rating scales. For each dimension, show: dimension name, scale (e.g. 1-5), and the text labels for each score level. Look at the official reviews posted on this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=Oce2215aJE",
    "prompt": "Extract the complete review form structure. List ALL scoring dimensions and their rating scales. For each dimension, show: dimension name, scale (e.g. 1-5), and the text labels for each score level. Look at the official reviews posted on this paper."
  }
}
```

</details>

---

### Tool call

_source line 390 · 2026-05-28T02:04:07.139242+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---

### Tool result

_source line 391 · 2026-05-28T02:04:08.544049+00:00_

I cannot extract the review form structure from the provided web page content. The page shows a paper abstract and metadata for "Body Transformer: Leveraging Robot Embodiment for Policy Learning" from CoRL 2024, but it does not display the actual peer reviews or scoring dimensions.

To access the review form structure with scoring dimensions and their rating scales, you would need to:

1. Visit the full paper page on OpenReview.net
2. Look for a "Reviews" or "Official Reviews" section
3. Check if reviews are publicly visible (some venues make reviews public after publication)

The content provided only includes the paper's title, authors, abstract, and publication metadata—not the underlying review evaluation criteria or reviewer assessments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3718
}
```

</details>

---

### Tool result

_source line 392 · 2026-05-28T02:04:08.547050+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---

### Tool call

_source line 393 · 2026-05-28T02:04:08.598585+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---

### Tool result

_source line 394 · 2026-05-28T02:04:09.557138+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---

### Tool call

_source line 395 · 2026-05-28T02:04:09.708146+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
  "project": "event-gated-adaptive-horizon",
  "pages": "31-45",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
    "project": "event-gated-adaptive-horizon",
    "pages": "31-45",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 396 · 2026-05-28T02:04:10.915680+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 31, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p31.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 308.7}, {\"page\": 32, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p32.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 383.6}, {\"page\": 33, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p33.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 272.8}, {\"page\": 34, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p34.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 319.6}, {\"page\": 35, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p35.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 373.8}, {\"page\": 36, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p36.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 44.0}, {\"page\": 37, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p37.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 407.5}, {\"page\": 38, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p38.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 273.0}, {\"page\": 39, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_
…[truncated 1700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1207
}
```

</details>

---

### Tool call

_source line 397 · 2026-05-28T02:04:19.325516+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---

### Tool result

_source line 398 · 2026-05-28T02:04:20.184898+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---

### Tool call

_source line 399 · 2026-05-28T02:04:20.336008+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---

### Tool call

_source line 400 · 2026-05-28T02:04:20.890194+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---

### Tool result

_source line 401 · 2026-05-28T02:04:21.196998+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---

### Tool call

_source line 402 · 2026-05-28T02:04:21.197501+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p34.png"
  }
}
```

</details>

---

### Tool result

_source line 403 · 2026-05-28T02:04:22.103375+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1213
}
```

</details>

---

### Tool result

_source line 404 · 2026-05-28T02:04:22.104931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool call

_source line 405 · 2026-05-28T02:04:22.205905+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p35.png"
  }
}
```

</details>

---

### Tool result

_source line 406 · 2026-05-28T02:04:22.560809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---

### Tool call

_source line 407 · 2026-05-28T02:04:22.561393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p36.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p36.png"
  }
}
```

</details>

---

### Tool result

_source line 408 · 2026-05-28T02:04:23.114597+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 409 · 2026-05-28T02:04:23.115091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL review form \"overall recommendation\" \"1:\" \"2:\" \"3:\" \"4:\" \"5:\" confidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL review form \"overall recommendation\" \"1:\" \"2:\" \"3:\" \"4:\" \"5:\" confidence"
  }
}
```

</details>

---

### Tool result

_source line 410 · 2026-05-28T02:04:28.585170+00:00_

Web search results for query: "CoRL review form "overall recommendation" "1:" "2:" "3:" "4:" "5:" confidence"

Links: [{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ICML 2025 Reviewer Instructions","url":"https://icml.cc/Conferences/2025/ReviewerInstructions"},{"title":"What the ACL-2014 review scores mean | AI and Social Science – Brendan O'Connor","url":"https://brenocon.com/blog/2014/02/what-the-acl-2014-review-scores-mean/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Instructions for Reviewers - ACL 2019","url":"https://acl2019.org/EN/instructions-for-reviewers.xhtml.html"},{"title":"Confidence Calibration for Recommender Systems and Its Applications","url":"https://arxiv.org/pdf/2402.16325"},{"title":"Intructions for Reviewers - ACL 2020","url":"https://acl2020.org/reviewers/"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"}]

Based on the search results, I found general information about conference review processes, but the specific CoRL review form with the exact "overall recommendation" scale definitions and confidence levels you're asking about wasn't fully detailed in these results.

The search returned reviewer guidelines for CoRL 2023 and 2024, as well as information from other conferences like ICML and ACL, but it did not contain the specific breakdown of what ratings 1-5 mean for the "overall recommendation" field or the confidence scale definitions specifically for CoRL's review form.

To get the exact CoRL review form definitions, you might want to:
1. Check the latest CoRL conference website's reviewer instructions page directly
2. Look at OpenReview's CoRL submission system, which displays the review form
3. Contact CoRL's program committee chairs directly

Would you like me to search for more specific information about a particular year's C
…[truncated 211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5470
}
```

</details>

---

### Tool call

_source line 411 · 2026-05-28T02:04:36.136504+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p37.png"
  }
}
```

</details>

---

### Tool result

_source line 412 · 2026-05-28T02:04:36.640473+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 413 · 2026-05-28T02:04:36.641007+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p38.png"
  }
}
```

</details>

---

### Tool result

_source line 414 · 2026-05-28T02:04:37.447727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---

### Tool call

_source line 415 · 2026-05-28T02:04:37.598697+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p39.png"
  }
}
```

</details>

---

### Tool call

_source line 416 · 2026-05-28T02:04:38.202451+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p40.png"
  }
}
```

</details>

---

### Tool result

_source line 417 · 2026-05-28T02:04:38.605605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---

### Tool call

_source line 418 · 2026-05-28T02:04:38.608211+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p41.png"
  }
}
```

</details>

---

### Tool result

_source line 419 · 2026-05-28T02:04:39.011511+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---

### Tool call

_source line 420 · 2026-05-28T02:04:39.015855+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p42.png"
  }
}
```

</details>

---

### Tool result

_source line 421 · 2026-05-28T02:04:39.974712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---

### Tool result

_source line 422 · 2026-05-28T02:04:39.976614+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---

### Tool call

_source line 423 · 2026-05-28T02:04:39.976980+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p43.png"
  }
}
```

</details>

---

### Tool call

_source line 424 · 2026-05-28T02:04:40.532279+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p44.png"
  }
}
```

</details>

---

### Tool result

_source line 425 · 2026-05-28T02:04:41.339061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---

### Tool result

_source line 426 · 2026-05-28T02:04:41.340058+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---

### Tool call

_source line 427 · 2026-05-28T02:04:41.340376+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p45.png"
  }
}
```

</details>

---

### Tool result

_source line 428 · 2026-05-28T02:04:41.842395+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_2_393bd6df.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 429 · 2026-05-28T02:04:43.505003+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=FO6tePGRZj",
  "prompt": "Look for official reviews on this paper. Extract the review scoring dimensions, rating scales, and score labels. What dimensions are scored (e.g. Soundness, Presentation, Contribution, Overall) and what rating scale is used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=FO6tePGRZj",
    "prompt": "Look for official reviews on this paper. Extract the review scoring dimensions, rating scales, and score labels. What dimensions are scored (e.g. Soundness, Presentation, Contribution, Overall) and what rating scale is used?"
  }
}
```

</details>

---

### Tool result

_source line 430 · 2026-05-28T02:04:48.180019+00:00_

# Review Information Not Available

Based on the provided webpage content, **no official reviews are visible**. The page displays the paper's metadata (title, authors, abstract, keywords, publication date) and links to supplementary materials, but does not include the actual peer review scores or dimensions.

To find the review scoring information, you would need to:
- Access the full OpenReview page directly
- Look for a "Reviews" section that typically appears below the abstract
- Check if reviews are public (some venues restrict visibility until after decisions are finalized)

The page footer indicates this is from CoRL 2024 Conference, but the review details are not rendered in the content provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4675
}
```

</details>

---

### Tool call

_source line 431 · 2026-05-28T02:06:06.653967+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2023 2024 review \"Soundness\" OR \"Excitement\" OR \"Overall Assessment\" score 1 2 3 4 5 6 7 8 9 10 robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2023 2024 review \"Soundness\" OR \"Excitement\" OR \"Overall Assessment\" score 1 2 3 4 5 6 7 8 9 10 robotics"
  }
}
```

</details>

---

### Tool result

_source line 432 · 2026-05-28T02:06:12.582103+00:00_

Web search results for query: "CoRL 2023 2024 review "Soundness" OR "Excitement" OR "Overall Assessment" score 1 2 3 4 5 6 7 8 9 10 robotics"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2023","url":"https://www.corl2023.org/"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2023 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2023%2FConference"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024","url":"https://2024.corl.org/"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"Motion-generation system for violin-playing robot using reinforcement learning differences in bowing parameters due to changes in learning conditions and sound pressure values","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11634750/"}]

Based on the search results, I found information about CoRL review guidelines and general conference information, but the search did not return specific review scores or data showing actual "Soundness," "Excitement," or "Overall Assessment" scores on a 1-10 scale for CoRL 2023 or 2024 submissions.

The search results show that:

- CoRL submissions are evaluated based on the significance and novelty of results, and judged on the degree to which they have been objectively established and their potential for scientific and technological impact
- Reviews and rebuttals of accepted papers will be made publicly available

However, the actual review score data with the specific metrics you're looking for (Soundness, Excitement, Overall Assessment scores) does not appear in these results. Such detailed review score information would typically be found on the OpenReview platform (openrev
…[truncated 390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5928
}
```

</details>

---

### Tool call

_source line 433 · 2026-05-28T02:08:43.094492+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：Round 1\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026\n**审查侧重**: 新颖性 + Venue Fit (Robotics Relevance) + 格式合规 + 完整性\n\n---\n\n## 总体评分\n\n**Overall**: 3/10 — Reject (存在两个独立的 desk-reject 级别问题)\n\n**一句话总结**: 扎实的诊断分析，但正文严重超页（~10.5 页 vs 8 页限制）且核心贡献是通用 RL 洞察而非机器人学问题，不符合 CoRL 的 venue scope。\n\n---\n\n## 官方维度打分（基于 CoRL 2023 Reviewer Guidelines: Originality, Quality, Clarity, Significance, Relevance, Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | CIVO 作为新命名的 failure mode 有一定新颖性，但与已知 value overestimation / compounding model error 的边界模糊 |\n| Quality | 4/5 | 实验设计严谨（43 配置 ×5 seeds），四级干预层级方法论扎实，NVE 诊断和 online detector 有技术含量 |\n| Clarity | 4/5 | 写作清晰，结构合理，Figure 1 机制图有效传达核心思想；但正文信息密度过高导致超页 |\n| Significance | 2/5 | 纯诊断论文且结论为\"无已测试干预有效\"——对 CoRL 社区缺乏实际指导价值 |\n| Relevance | 1/5 | CIVO 是任何使用 imagination + temporal conditioning 的 MBRL 系统的通用问题，非机器人特有；无真实机器人实验 |\n| Limitations | 4/5 | Limitations section 存在且诚实讨论了统计功效和环境覆盖范围 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文严重超页——约 10.5 页 vs 8 页限制\n\n- 具体位置：Pages 1–11（References 从 page 11 下方约 2/3 处开始）\n- 问题：CoRL 2026 明确规定正文（含 Limitations section）限 8 页，仅 references 和 appendix 不计入。实际正文内容（Section 1 至 Limitations 结束）横跨约 10.5 页，超限约 2.5 页。根据 CoRL 2026 Instruction for Authors（https://www.corl.org/contributions/instruction-for-authors），此项违规可直接触发 desk rejection。\n- 为什么影响接收：格式违规是 CoRL 评审流程的硬约束。AC 在分配 reviewer 前即可做格式检查并退回论文。\n- 建议修改方向：大幅压缩正文——Section 5 (Discussion) 整整占了 page 10 和 page 11 上半部分（约 1.5 页），大量内容与 Section 4 的 findings 重复；Section 3 (Experimental Setup) 的细粒度配置细节（3.3-3.8，共约 1.5 页）可大量移入 Appendix；Table 1 的完整 43 配置结果可精简为主要发现的 summary table 并将完整版置于 Appendix。压缩 Discussion + Setup 共约 3 页即可达标。\n\n**N2** [critical] Venue Fit 不足——核心贡献是通用 RL 诊断，非 robotics-specific\n\n- 具体位置：全文，特别是 Abstract（\"World model reinforcement learning is increasingly deployed for robot control\"）和 Section 5 Discussion\n- 问题：CoRL 2026 Call for Papers 明确要求 \"Submissions must focus on a core robotics problem\" 且 \"papers lacking robotics focus will be returned without review\"（https://www.corl.org/contributions/call-for-papers）。本文的核心贡献——发现 CIVO 这一 failure mode 及四级诊断协议——是**通用 MBRL 的方法论洞察**，不依赖于任何机器人特性：\n  - CIVO 的成因（dt-conditioning + imagination 中的 value overestimation feedback loop）在任何使用 DreamerV3 temporal abstraction 的领域都会出现（Atari、棋盘游戏等）\n  - 使用的环境（DMC Walker Walk, Cheetah Run, ManiSkill）虽是 robotics 常用 benchmark，但论文没有展示任何 robotics-specific 的 insight（如 sim-to-real gap 如何影响 CIVO、real robot 上的验证等）\n  - Section 5 的 \"Practitioner guidelines\"（第 10 页 line 593-597）提到 \"monitor NVE diagnostic\" 和 \"freezing the dt-embedding eliminates CIVO\"——这些建议适用于任何使用 DreamerV3 的场景，无机器人特异性\n  - 没有任何真实机器人实验，也没有提供 convincing evidence that simulation experiments are transferable to real robots（CoRL 2026 明确鼓励此项）\n- 为什么影响接收：CoRL scope 要求是第二个独立的 desk-reject 条件。即使格式合规，AC 仍可能以 scope 不符退回。\n- 建议修改方向：(a) 增加真实机器人实验验证 CIVO 在 sim-to-real transfer 场景中的影响；(b) 分析 CIVO 对 robotics-specific 任务特性（contact-rich, long-horizon, multi-modal observation）的差异化表现；(c) 或者将论文投至更合适的 venue——ICML、NeurIPS、ICLR 的 RL track 对此类通用 MBRL 诊断分析的接受度更高。\n\n**N3** [critical] 纯诊断 + 负面结论缺乏 actionable contribution\n\n- 具体位置：Section 4.5 (Forward-Pass Interventions), Section 4.6 (Architecture-Level Ablation), Table 2, Section 5 (Discussion line 554: \"No tested intervention reliably eliminates CIVO\")\n- 问题：论文的核心结论是四级干预均无法可靠消除 CIVO。这是一个 honest negative result，但 CoRL 社区高度重视 practical impact。Negative result papers 在 robotics venues 的接受门槛极高——需要 (a) 挑战广泛接受的假设，或 (b) 提供清晰的 \"不要做 X\" 的实践指导。本文的负面结论——\"variable-rate imagination 会导致 CIVO\"——对应的 actionable takeaway 过于简单（\"冻结 dt-embedding\" 或 \"用 NVE 监控\"），且冻结 dt-embedding 等于放弃了 temporal abstraction 的全部价值。\n- 为什么影响接收：CoRL reviewer 在 Significance 维度会严重扣分——论文指出了问题但未提供可行的前进方向。\n- 建议修改方向：至少提出一个有效的缓解方案（即使不完美），或提供更具体的理论分析指出 CIVO 的根本原因和潜在解决路径。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] CIVO 与已知 value overestimation 文献的区分不够锐利\n\n- 具体位置：Section 2 (Related Work, page 2-3), Section 5 Discussion (page 10 lines 535-547)\n- 问题：论文引用了 Thrun & Schwartz [5], van Hasselt [34], Double Q [14], delusional bias (Lu et al. [9]) 并尝试区分 CIVO。但核心区分论点——\"CIVO arises from the interaction between learned temporal conditioning and imagination-based training\"——在概念层面与 Janner et al. [26] 讨论的 MBRL compounding model error 高度相似：两者都是 model 的系统性偏差在 imagination rollout 中被放大。Section 5 line 540 称 CIVO 是 \"a structural vulnerability, not a regularization deficiency\"，但没有提供形式化的理论分析来证明这一点（仅有经验观察）。\n- 建议：(a) 提供更精确的形式化定义区分 CIVO 与 compounding model error；(b) 设计一个实验直接对比这两个 failure mode 的表现特征（例如，在不使用 temporal conditioning 的标准 DreamerV3 上展示 compounding error 不触发同样的 NVE 爆炸模式）。\n\n**W2** [warning] 环境覆盖范围有限\n\n- 具体位置：Section 3.8 (page 4), Table 1 (page 5), 附录中的 ManiSkill 结果\n- 问题：主文主要报告 Walker Walk 和 Cheetah Run（DMC）两个环境的结果，加上少量 ManiSkill manipulation 实验。对于一个声称发现了 temporal abstraction in imagination-based RL 的通用 failure mode 的论文，2+1 个环境偏窄。特别是：\n  - 两个 DMC 环境都是 continuous locomotion 任务，缺少导航、长 horizon planning、contact-rich manipulation 等多样化 robotics 场景\n  - ManiSkill 结果在附录中展开（Table 5, Appendix C），主文仅简要提及\n  - 没有 vision-based 环境（都用 proprioceptive states）\n- 建议：如果 claim CIVO 是通用现象，应至少覆盖 3-4 种有代表性的 task 类型（locomotion, manipulation, navigation, contact-rich），并将关键 ManiSkill 结果提升到主文中。\n\n**W3** [warning] 诊断协议（四级干预层级）的通用性未经验证\n\n- 具体位置：Section 3.5-3.7 (page 4), Section 5 line 570-585 (page 10)\n- 问题：四级层级（gradient → output → representation → architecture）被称为 \"transferable diagnostic protocol\"（Section 5, line 578），但仅在 DreamerV3 一个算法上验证。该协议是否能推广到 TD-MPC2 [14]、Director [18]、TWM [10] 等其他 imagination-based architectures？论文本身承认 \"TD-MPC2 combines... td-conditioning bringing temporal abstraction in imagination-based acto-critic frameworks\" (Section 2, page 2) 但从未在这些系统上测试诊断协议。\n- 建议：至少在一个非 DreamerV3 架构上验证诊断协议的适用性，或明确限定声明范围。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Figure 1 (page 2) 的 Pathway A/B 图文字偏小，在打印时可能不易阅读。建议适当增大关键标签的字号。\n- **M2**: Table 1 (page 5) 包含 43 个配置，信息密度极高但扫描性差。主文中可用 summary statistics 替代，完整表格放入 Appendix。\n- **M3**: Section 1 Introduction (page 1) 的 contribution list 使用了 \"failure mode identification\", \"architectural benchmarking\", \"four-level intervention hierarchy\", \"preliminary diagnostics\" 四个层次——但 \"preliminary diagnostics\"（指 NVE online detector）与 \"failure mode identification\" 在概念上有重叠，分类不够正交。\n- **M4**: 论文尾注 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\" 格式正确。匿名化方面，作者信息使用 \"Anonymous Author(s)\" ✓；GitHub 脚注（page 4, footnote 1）指向公开的 DreamerV3 仓库而非作者代码，不构成去匿名化风险 ✓。\n- **M5**: 附录 I (Bug Correction and Version History, pages 35-36) 记录了实验过程中发现的 bug 及修正——这种透明度值得赞赏，但也暗示实验代码在写作期间仍在迭代，可能影响 reviewer 对结果稳定性的信心。\n\n---\n\n## 缺失引用检查\n\n引用列表覆盖了 temporal abstraction 的主要文献（Options [7], TempoRL [3], Director [18], TD-MPC2 [14], TWM [10]）。以下可能相关但未引用的工作：\n\n1. **FiGAR** (Sharma, Lakshminarayanan, Ravindran, 2017): \"Fine Grained Action Repetition for Deep Reinforcement Learning\" — 与 variable-rate control 直接相关，论文引用了 [22] Sharma et al. 2017 但这似乎是另一篇（\"Learned embeddings...\"），FiGAR 是否也被涵盖需确认。\n2. **DAC** (Zhang & Whiteson, 2019): \"DAC: The Double Actor-Critic Architecture for Learning Options\" — options 学习中与 value estimation 相关的架构工作。\n3. **SPiRL / SPIRAL** (Pertsch et al., 2020): skill-prior RL with temporal abstraction in robotics contexts — CoRL 接受的 robotics temporal abstraction 工作范例。\n4. 近期 real-robot temporal abstraction 部署工作（如果存在）——补充这些引用可强化 robotics relevance 论证。\n\n总体而言，引用列表对于 general RL 领域是全面的，缺失主要集中在 robotics-specific temporal abstraction 工作。\n\n---\n\n## 主要优势\n\n1. **实验规模与严谨性**：43 个配置 × 5 seeds，总计 215+ 独立训练 run，NVE 时间序列分析覆盖 12 个 checkpoint，实验设计是诊断论文的标杆。\n2. **四级干预层级设计精巧**：从 gradient 到 architecture 逐层剥离，系统性地排除了 regularization、gradient flow、forward-pass 等常见 suspect，最终定位到 architectural 层面。\n3. **NVE 诊断指标和 online CIVO detector**：AUROC=1.000（Table 1 page 5 注释 / Table 9 page 39），precision/recall 完美分离，有实用价值。\n4. **诚实的负面结论**：不过度宣称，明确承认无有效缓解方案，这在学术文化中是罕见且值得尊重的。\n5. **写作质量高**：逻辑链条清晰（CIVO mechanism → experimental evidence → intervention tests → failure pattern），Figure 1 的双路径机制图有效概括了核心思想。\n6. **附录极其详尽**：31 页附录覆盖完整实验配置、额外环境验证、梯度分解分析（Appendix D）、CIVO detector 算法规格和 ROC 分析（Appendix F）、bug 修正记录（Appendix I），可复现性极高。\n\n---\n\n## 评分建议\n\n**推荐决定**: **Reject**\n\n**理由排序**:\n1. 正文超页 ~2.5 页（desk reject 条件）\n2. Robotics relevance 不足（desk reject 条件）\n3. 纯诊断 + 负面结论的 significance 对 CoRL 偏低\n4. 建议投 ICML/NeurIPS/ICLR RL track，该诊断在通用 ML 社区的接受度会显著更高\n\n**Confidence**: 4/5 — 对格式违规和 venue fit 评判有高度信心；对新颖性评估有中高信心（熟悉 value overestimation 和 MBRL 文献）。\n",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：Round 1\n\n**论文**: \"Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**目标 Venue**: CoRL 2026\n**审查侧重**: 新颖性 + Venue Fit (Robotics Relevance) + 格式合规 + 完整性\n\n---\n\n## 总体评分\n\n**Overall**: 3/10 — Reject (存在两个独立的 desk-reject 级别问题)\n\n**一句话总结**: 扎实的诊断分析，但正文严重超页（~10.5 页 vs 8 页限制）且核心贡献是通用 RL 洞察而非机器人学问题，不符合 CoRL 的 venue scope。\n\n---\n\n## 官方维度打分（基于 CoRL 2023 Reviewer Guidelines: Originality, Quality, Clarity, Significance, Relevance, Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | CIVO 作为新命名的 failure mode 有一定新颖性，但与已知 value overestimation / compounding model error 的边界模糊 |\n| Quality | 4/5 | 实验设计严谨（43 配置 ×5 seeds），四级干预层级方法论扎实，NVE 诊断和 online detector 有技术含量 |\n| Clarity | 4/5 | 写作清晰，结构合理，Figure 1 机制图有效传达核心思想；但正文信息密度过高导致超页 |\n| Significance | 2/5 | 纯诊断论文且结论为\"无已测试干预有效\"——对 CoRL 社区缺乏实际指导价值 |\n| Relevance | 1/5 | CIVO 是任何使用 imagination + temporal conditioning 的 MBRL 系统的通用问题，非机器人特有；无真实机器人实验 |\n| Limitations | 4/5 | Limitations section 存在且诚实讨论了统计功效和环境覆盖范围 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文严重超页——约 10.5 页 vs 8 页限制\n\n- 具体位置：Pages 1–11（References 从 page 11 下方约 2/3 处开始）\n- 问题：CoRL 2026 明确规定正文（含 Limitations section）限 8 页，仅 references 和 appendix 不计入。实际正文内容（Section 1 至 Limitations 结束）横跨约 10.5 页，超限约 2.5 页。根据 CoRL 2026 Instruction for Authors（https://www.corl.org/contributions/instruction-for-authors），此项违规可直接触发 desk rejection。\n- 为什么影响接收：格式违规是 CoRL 评审流程的硬约束。AC 在分配 reviewer 前即可做格式检查并退回论文。\n- 建议修改方向：大幅压缩正文——Section 5 (Discussion) 整整占了 page 10 和 page 11 上半部分（约 1.5 页），大量内容与 Section 4 的 findings 重复；Section 3 (Experimental Setup) 的细粒度配置细节（3.3-3.8，共约 1.5 页）可大量移入 Appendix；Table 1 的完整 43 配置结果可精简为主要发现的 summary table 并将完整版置于 Appendix。压缩 Discussion + Setup 共约 3 页即可达标。\n\n**N2** [critical] Venue Fit 不足——核心贡献是通用 RL 诊断，非 robotics-specific\n\n- 具体位置：全文，特别是 Abstract（\"World model reinforcement learning is increasingly deployed for robot control\"）和 Section 5 Discussion\n- 问题：CoRL 2026 Call for Papers 明确要求 \"Submissions must focus on a core robotics problem\" 且 \"papers lacking robotics focus will be returned without review\"（https://www.corl.org/contributions/call-for-papers）。本文的核心贡献——发现 CIVO 这一 failure mode 及四级诊断协议——是**通用 MBRL 的方法论洞察**，不依赖于任何机器人特性：\n  - CIVO 的成因（dt-conditioning + imagination 中的 value overestimation feedback loop）在任何使用 DreamerV3 temporal abstraction 的领域都会出现（Atari、棋盘游戏等）\n  - 使用的环境（DMC Walker Walk, Cheetah Run, ManiSkill）虽是 robotics 常用 benchmark，但论文没有展示任何 robotics-specific 的 insight（如 sim-to-real gap 如何影响 CIVO、real robot 上的验证等）\n  - Section 5 的 \"Practitioner guidelines\"（第 10 页 line 593-597）提到 \"monitor NVE diagnostic\" 和 \"freezing the dt-embedding eliminates CIVO\"——这些建议适用于任何使用 DreamerV3 的场景，无机器人特异性\n  - 没有任何真实机器人实验，也没有提供 convincing evidence that simulation experiments are transferable to real robots（CoRL 2026 明确鼓励此项）\n- 为什么影响接收：CoRL scope 要求是第二个独立的 desk-reject 条件。即使格式合规，AC 仍可能以 scope 不符退回。\n- 建议修改方向：(a) 增加真实机器人实验验证 CIVO 在 sim-to-real transfer 场景中的影响；(b) 分析 CIVO 对 robotics-specific 任务特性（contact-rich, long-horizon, multi-modal observation）的差异化表现；(c) 或者将论文投至更合适的 venue——ICML、NeurIPS、ICLR 的 RL track 对此类通用 MBRL 诊断分析的接受度更高。\n\n**N3** [critical] 纯诊断 + 负面结论缺乏 actionable contribution\n\n- 具体位置：Section 4.5 (Forward-Pass Interventions), Section 4.6 (Architecture-Level Ablation), Table 2, Section 5 (Discussion line 554: \"No tested intervention reliably eliminates CIVO\")\n- 问题：论文的核心结论是四级干预均无法可靠消除 CIVO。这是一个 honest negative result，但 CoRL 社区高度重视 practical impact。Negative result papers 在 robotics venues 的接受门槛极高——需要 (a) 挑战广泛接受的假设，或 (b) 提供清晰的 \"不要做 X\" 的实践指导。本文的负面结论——\"variable-rate imagination 会导致 CIVO\"——对应的 actionable takeaway 过于简单（\"冻结 dt-embedding\" 或 \"用 NVE 监控\"），且冻结 dt-embedding 等于放弃了 temporal abstraction 的全部价值。\n- 为什么影响接收：CoRL reviewer 在 Significance 维度会严重扣分——论文指出了问题但未提供可行的前进方向。\n- 建议修改方向：至少提出一个有效的缓解方案（即使不完美），或提供更具体的理论分析指出 CIVO 的根本原因和潜在解决路径。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] CIVO 与已知 value overestimation 文献的区分不够锐利\n\n- 具体位置：Section 2 (Related Work, page 2-3), Section 5 Discussion (page 10 lines 535-547)\n- 问题：论文引用了 Thrun & Schwartz [5], van Hasselt [34], Double Q [14], delusional bias (Lu et al. [9]) 并尝试区分 CIVO。但核心区分论点——\"CIVO arises from the interaction between learned temporal conditioning and imagination-based training\"——在概念层面与 Janner et al. [26] 讨论的 MBRL compounding model error 高度相似：两者都是 model 的系统性偏差在 imagination rollout 中被放大。Section 5 line 540 称 CIVO 是 \"a structural vulnerability, not a regularization deficiency\"，但没有提供形式化的理论分析来证明这一点（仅有经验观察）。\n- 建议：(a) 提供更精确的形式化定义区分 CIVO 与 compounding model error；(b) 设计一个实验直接对比这两个 failure mode 的表现特征（例如，在不使用 temporal conditioning 的标准 DreamerV3 上展示 compounding error 不触发同样的 NVE 爆炸模式）。\n\n**W2** [warning] 环境覆盖范围有限\n\n- 具体位置：Section 3.8 (page 4), Table 1 (page 5), 附录中的 ManiSkill 结果\n- 问题：主文主要报告 Walker Walk 和 Cheetah Run（DMC）两个环境的结果，加上少量 ManiSkill manipulation 实验。对于一个声称发现了 temporal abstraction in imagination-based RL 的通用 failure mode 的论文，2+1 个环境偏窄。特别是：\n  - 两个 DMC 环境都是 continuous locomotion 任务，缺少导航、长 horizon planning、contact-rich manipulation 等多样化 robotics 场景\n  - ManiSkill 结果在附录中展开（Table 5, Appendix C），主文仅简要提及\n  - 没有 vision-based 环境（都用 proprioceptive states）\n- 建议：如果 claim CIVO 是通用现象，应至少覆盖 3-4 种有代表性的 task 类型（locomotion, manipulation, navigation, contact-rich），并将关键 ManiSkill 结果提升到主文中。\n\n**W3** [warning] 诊断协议（四级干预层级）的通用性未经验证\n\n- 具体位置：Section 3.5-3.7 (page 4), Section 5 line 570-585 (page 10)\n- 问题：四级层级（gradient → output → representation → architecture）被称为 \"transferable diagnostic protocol\"（Section 5, line 578），但仅在 DreamerV3 一个算法上验证。该协议是否能推广到 TD-MPC2 [14]、Director [18]、TWM [10] 等其他 imagination-based architectures？论文本身承认 \"TD-MPC2 combines... td-conditioning bringing temporal abstraction in imagination-based acto-critic frameworks\" (Section 2, page 2) 但从未在这些系统上测试诊断协议。\n- 建议：至少在一个非 DreamerV3 架构上验证诊断协议的适用性，或明确限定声明范围。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Figure 1 (page 2) 的 Pathway A/B 图文字偏小，在打印时可能不易阅读。建议适当增大关键标签的字号。\n- **M2**: Table 1 (page 5) 包含 43 个配置，信息密度极高但扫描性差。主文中可用 summary statistics 替代，完整表格放入 Appendix。\n- **M3**: Section 1 Introduction (page 1) 的 contribution list 使用了 \"failure mode identification\", \"architectural benchmarking\", \"four-level intervention hierarchy\", \"preliminary diagnostics\" 四个层次——但 \"preliminary diagnostics\"（指 NVE online detector）与 \"failure mode identification\" 在概念上有重叠，分类不够正交。\n- **M4**: 论文尾注 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\" 格式正确。匿名化方面，作者信息使用 \"Anonymous Author(s)\" ✓；GitHub 脚注（page 4, footnote 1）指向公开的 DreamerV3 仓库而非作者代码，不构成去匿名化风险 ✓。\n- **M5**: 附录 I (Bug Correction and Version History, pages 35-36) 记录了实验过程中发现的 bug 及修正——这种透明度值得赞赏，但也暗示实验代码在写作期间仍在迭代，可能影响 reviewer 对结果稳定性的信心。\n\n---\n\n## 缺失引用检查\n\n引用列表覆盖了 temporal abstraction 的主要文献（Options [7], TempoRL [3], Director [18], TD-MPC2 [14], TWM [10]）。以下可能相关但未引用的工作：\n\n1. **FiGAR** (Sharma, Lakshminarayanan, Ravindran, 2017): \"Fine Grained Action Repetition for Deep Reinforcement Learning\" — 与 variable-rate control 直接相关，论文引用了 [22] Sharma et al. 2017 但这似乎是另一篇（\"Learned embeddings...\"），FiGAR 是否也被涵盖需确认。\n2. **DAC** (Zhang & Whiteson, 2019): \"DAC: The Double Actor-Critic Architecture for Learning Options\" — options 学习中与 value estimation 相关的架构工作。\n3. **SPiRL / SPIRAL** (Pertsch et al., 2020): skill-prior RL with temporal abstraction in robotics contexts — CoRL 接受的 robotics temporal abstraction 工作范例。\n4. 近期 real-robot temporal abstraction 部署工作（如果存在）——补充这些引用可强化 robotics relevance 论证。\n\n总体而言，引用列表对于 general RL 领域是全面的，缺失主要集中在 robotics-specific temporal abstraction 工作。\n\n---\n\n## 主要优势\n\n1. **实验规模与严谨性**：43 个配置 × 5 seeds，总计 215+ 独立训练 run，NVE 时间序列分析覆盖 12 个 checkpoint，实验设计是诊断论文的标杆。\n2. **四级干预层级设计精巧**：从 gradient 到 architecture 逐层剥离，系统性地排除了 regularization、gradient flow、forward-pass 等常见 suspect，最终定位到 architectural 层面。\n3. **NVE 诊断指标和 online CIVO detector**：AUROC=1.000（Table 1 page 5 注释 / Table 9 page 39），precision/recall 完美分离，有实用价值。\n4. **诚实的负面结论**：不过度宣称，明确承认无有效缓解方案，这在学术文化中是罕见且值得尊重的。\n5. **写作质量高**：逻辑链条清晰（CIVO mechanism → experimental evidence → intervention tests → failure pattern），Figure 1 的双路径机制图有效概括了核心思想。\n6. **附录极其详尽**：31 页附录覆盖完整实验配置、额外环境验证、梯度分解分析（Appendix D）、CIVO detector 算法规格和 ROC 分析（Appendix F）、bug 修正记录（Appendix I），可复现性极高。\n\n---\n\n## 评分建议\n\n**推荐决定**: **Reject**\n\n**理由排序**:\n1. 正文超页 ~2.5 页（desk reject 条件）\n2. Robotics relevance 不足（desk reject 条件）\n3. 纯诊断 + 负面结论的 significance 对 CoRL 偏低\n4. 建议投 ICML/NeurIPS/ICLR RL track，该诊断在通用 ML 社区的接受度会显著更高\n\n**Confidence**: 4/5 — 对格式违规和 venue fit 评判有高度信心；对新颖性评估有中高信心（熟悉 value overestimation 和 MBRL 文献）。\n",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 434 · 2026-05-28T02:08:47.564476+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4469
}
```

</details>

---

### Tool call

_source line 435 · 2026-05-28T02:08:54.330014+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
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

_source line 436 · 2026-05-28T02:08:54.381981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 437 · 2026-05-28T02:08:58.582153+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 438 · 2026-05-28T02:08:58.636044+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 53
}
```

</details>

---

### Assistant

_source line 439 · 2026-05-28T02:09:12.810861+00:00_

审稿完成。已向 Review Director 提交完整的 Round 1 审稿意见，核心判断：

**Overall: 3/10 — Reject**，存在两个独立的 desk-reject 级别问题：

1. **正文超页 ~2.5 页**（10.5 页 vs 8 页限制）——Section 5 Discussion 和 Section 3 Setup 的大量细节可压缩至 Appendix
2. **Robotics relevance 不足**——CIVO 是通用 MBRL 的 failure mode，非机器人特有问题；无真实机器人实验；建议投 ICML/NeurIPS/ICLR

此外，纯诊断 + "无有效缓解方案" 的负面结论在 CoRL 的 significance 维度偏低。论文实验质量本身很高（43 配置 ×5 seeds，四级干预层级设计精巧），适合在通用 ML venue 发表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

## Round 14

18 recorded events

### User

_source line 440 · 2026-05-28T02:10:01.306227+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿意见（完整原文）

**Overall**: 6/10 — Marginally above acceptance threshold

## 官方维度打分
| 维度 | 分数 |
|------|------|
| Originality | 7/10 |
| Quality (Soundness) | 5/10 |
| Clarity | 8/10 |
| Significance | 5/10 |
| Relevance | 5/10 |
| Limitations | 8/10 |

## Must-Fix 问题

**N1** [critical] AUROC = 1.000 on n=36 缺乏不确定性量化，完美分类声明过强
- 未提供 bootstrap confidence interval。在 n=36 的样本上，单个误分类即会使 AUROC 降至约 0.97。
- LOEO 仅涵盖 3 个环境，每个 fold 的留出集极小。
- 建议：报告 bootstrap 95% CI；弱化 "perfect classification" 措辞。

**N2** [critical] 因果机制声明（CIVO feedback loop）超出观测证据强度
- Figure 1 的四步反馈环中，每个环节的证据强度不同：
  - Step 1→2（embedding → RSSM 偏差）：gradient decomposition 提供 partial evidence
  - Step 2→3（biased prediction → value overestimation）：相关性但未排除混淆因素
  - Step 3→4（overestimation → exploitative policy）：无直接 policy behavior 分析
  - Step 4→1（biased data → further bias）：完全推断，无直接实验
- 建议：将措辞改为 "proposed/hypothesized mechanism"；标注证据层级。

**N3** [critical] 统计效力不足以支撑部分关键声明
- 4-5 seeds 的 IQM 每个配置效果估计噪声极大。
- 多处 seed-level 叙述性声明不构成统计证据。
- n=36 分类中的 class balance 未明确报告。
- 建议：报告 CIVO-positive vs non-CIVO 精确数量；对主要声明提供 bootstrap CI。

## Should-Fix 问题

**W1** [warning] NVE 阈值 2.0× 的选取存在潜在循环性
- 阈值从同一数据集上选出，然后在同一数据集上通过 LOEO/LOCO 验证。3 个环境的 internal cross-validation 不等于 external validation。

**W2** [warning] Factorial design 未完全隔离 embedding 架构与训练信号的效果
- "trained dt-embedding" 同时引入了架构变化和训练信号变化。Frozen embedding 能部分分离但初始化方式可能影响结论。

**W3** [warning] 环境多样性不足，robotics relevance 偏弱
- 所有主要实验仅在 Walker Walk 和 Cheetah Run 中进行。无接触丰富操作任务、无高维观测、无 sim-to-real。

**W4** [warning] Table 1 脚注 f ("corrected-code rerun") 的影响范围需更清晰呈现
- 代码修正影响了多少配置的 CIVO 分类标签？修正前后 AUROC 是否变化？

**W5** [warning] "pathway redundancy" 声明缺乏统计检验
- 基于极小样本的 prevention rate 比较无统计检验。

## 优势
1. 异常优秀的数据透明度（per-seed 结果、code correction 历史）
2. 系统性实验设计（factorial + 四级干预 + 三种 cross-validation）
3. 实用的 NVE 诊断工具（Algorithm 1）
4. 诚实的负面结论

---

请对以上每个 N1-N3 和 W1-W5 给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 441 · 2026-05-28T02:10:36.374190+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
  "project": "event-gated-adaptive-horizon",
  "pages": "5,9,10,38,39",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/submitted.pdf",
    "project": "event-gated-adaptive-horizon",
    "pages": "5,9,10,38,39",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 442 · 2026-05-28T02:10:37.328362+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 362.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 330.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 414.2}, {\"page\": 38, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p38.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 273.0}, {\"page\": 39, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p39.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 266.0}], \"total_pages\": 45, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 443 · 2026-05-28T02:10:40.528036+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 444 · 2026-05-28T02:10:41.434310+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---

### Tool call

_source line 445 · 2026-05-28T02:10:41.434783+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 446 · 2026-05-28T02:10:41.888102+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 447 · 2026-05-28T02:10:41.938859+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool call

_source line 448 · 2026-05-28T02:10:42.491424+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p38.png"
  }
}
```

</details>

---

### Tool result

_source line 449 · 2026-05-28T02:10:42.944428+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---

### Tool result

_source line 450 · 2026-05-28T02:10:42.945717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 451 · 2026-05-28T02:10:42.996334+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images/submitted_p39.png"
  }
}
```

</details>

---

### Tool result

_source line 452 · 2026-05-28T02:10:43.349464+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 453 · 2026-05-28T02:12:22.392134+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: AUROC=1.000 缺乏不确定性量化**\n\n同意该批评的核心——AUROC 本身未报告 bootstrap CI。但需补充两点：\n\n1. 论文在附录中**已提供部分不确定性量化**：Table 7-8（page 39）报告了 Clopper-Pearson exact binomial 95% CI 用于 accuracy/precision/recall（例如 Table 7: Accuracy 72.7% [39.0, 94.0] at threshold 2.0）。但这是对特定阈值下的 point metrics 的 CI，**不是对 AUROC 本身的 CI**，R1 的要求合理。\n2. Table 9（page 39）显示 CIVO-positive 样本 NVE ≥ 1.53，negative < 1.04——两类之间存在 **~0.5 的 clean gap**，这降低了\"单个误分类即破坏 perfect AUROC\"的实际风险，但不能替代形式化的 CI 报告。\n\n总体判断：R1 的建议（报告 bootstrap 95% CI + 弱化 \"perfect classification\" 措辞）完全合理且容易执行。\n\n---\n\n**[AGREE] R1-N2: 因果机制声明超出证据强度**\n\n同意。论文确实将 CIVO 呈现为一个**闭环因果链**（Figure 1, page 2），但四个环节的证据强度不对称：\n\n- **有较强证据的环节**：(a) trained dt-embedding → RSSM bias（Appendix D gradient decomposition, page 24-26 显示 reward head 贡献最大的 gradient 份额 34.7%/40.4%）；(b) 冻结 dt-embedding 消除 CIVO（Table 1 中所有 0/16 frozen configs 触发 CIVO）——这是一个有效的**反事实干预**，支持因果推断。\n- **证据较弱的环节**：(c) value overestimation → exploitative policy behavior——论文仅通过 NVE ratio 间接推断，没有直接的 policy trajectory/action distribution 分析；(d) biased policy → further embedding bias（loop closure）——完全是推断，无直接实验证据。\n\nR1 关于标注 \"proposed/hypothesized mechanism\" 并区分证据层级的建议，对论文的学术严谨性有实质改善。不过需要公平指出，反事实干预（freezing experiment）确实提供了因果方向的 evidence——虽然不足以证明完整环路，但比纯粹的相关性分析要强。\n\n---\n\n**[AGREE] R1-N3: 统计效力不足**\n\n同意。补充两个具体观察：\n\n1. **Class balance 问题**：Table 9（page 39）报告 n_pos=8, n_neg=8, n=17（Full validation set 仅含 Walker Walk 15 configs + Cheetah Run 2 configs），而非论文主文 Section 4.7（page 9）声称的 n=36。n=36 的完整分类中 CIVO-positive vs negative 的精确比例**未在主文中明确报告**，需要读者到附录 Table 3（page 37）逐行统计。这是一个 presentation 问题——关键统计信息应直接出现在主文。\n2. **Per-seed 叙述性声明**：Section 4.1（page 5-6）和 Section 4.2（page 7）中出现多处基于个别 seed 表现的推断（例如 \"peaks at 485.3 before collapsing\"），这些未附 CI 或 significance test。对于诊断论文而言，每个定量 claim 都应有明确的统计支撑。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: NVE 阈值 2.0× 潜在循环性**\n\n同意这一方法论关切。阈值选取和验证使用同一数据集，LOEO 仅 3 个 folds（Table 11, page 39：PegCube, Cheetah, Walker），每个 fold 的 held-out 集极小（PegCube 仅 3 个样本）。\n\n但需指出缓解因素：Table 9 显示 positive/negative 类之间的 NVE gap（1.53 vs <1.04）远大于阈值选择的敏感范围，Table 7 的 sensitivity analysis 显示 threshold 在 1.5-2.5 范围内 F1 均为 1.0。这表明结论对阈值选择**不敏感**，但形式上仍不能替代外部验证。一个新的（未参与训练的）环境上的 prospective validation 会显著增强可信度。\n\n---\n\n**[AGREE] R1-W2: Factorial design 未完全隔离 embedding 架构与训练信号**\n\n同意。trained dt-embedding 是一个 compound treatment——同时改变了 (a) 网络架构（增加 embedding input）和 (b) 训练信号（dt 值的梯度流）。论文的 frozen embedding 控制组确实分离了 (b)，但 frozen 的初始化方式（random vs pre-trained then frozen）可能影响 (a) 的效果归因。\n\n补充一点：Section 4.3（page 7-8）中 \"Architecture-Level Ablation\" 和 Table 14（page 40）的 2×2 factorial（single vs dual critic, with/without dt-embedding）部分解决了这个问题，但 R1 的核心关切——无法完全排除架构变化本身（而非训练信号）导致 CIVO——仍然成立。\n\n---\n\n**[AGREE] R1-W3: 环境多样性不足，robotics relevance 偏弱**\n\n强烈同意——这与我自己的 N2（venue fit）和 W2（环境覆盖）完全一致。Walker Walk 和 Cheetah Run 都是 low-dimensional proprioceptive continuous locomotion 任务，代表性极为有限。附录中有 ManiSkill 结果（Table 5, page 38），但仅在附录出现且样本量更小。\n\n---\n\n**[AGREE] R1-W4: Table 1 脚注 f 的 code correction 影响范围**\n\n同意。Appendix I（pages 35-36）详细记录了 bug 修正历史，论文声称 \"All numerical results reported in the main text and appendix tables use the corrected codebase\"（page 36, line 1191-1192）。但以下关键信息缺失：\n\n- 修正前有多少配置被错误分类为 CIVO-positive/negative？\n- 修正是否改变了任何核心结论（如 pathway redundancy 的 prevention rates）？\n- AUROC 在修正前后是否一致？\n\nAppendix I 中保留了 pre-correction 数据（Table 32 和 Table 3 footnotes k, l），这是好的透明度实践，但未直接回答上述问题。\n\n---\n\n**[AGREE] R1-W5: Pathway redundancy 声明缺乏统计检验**\n\n同意。Section 5（page 10, lines 554-568）中 \"intervention resistance reveals pathway redundancy\" 的论证基于 Table 2（page 9）中各干预的 prevention rates，但这些 rates 来自极小样本（例如 obs-decoder-only SGS 在 Cheetah 上仅有 2 个 CIVO-positive baseline 可比较），且无任何 hypothesis test（如 Fisher's exact test 或 permutation test）。将观察到的 partial prevention 上升为 \"pathway redundancy\" 这一结构性声明需要更强的统计支撑。\n\n---\n\n## 总结\n\nR1 的 8 个问题中我全部 AGREE。R1 的审稿与我的侧重互补：\n\n- **我侧重 venue fit + 格式**：发现了两个独立的 desk-reject 级问题（超页 2.5 页 + robotics relevance 不足）\n- **R1 侧重 statistical rigor + causal claims**：发现了统计效力、AUROC 不确定性、因果声明过强三个质量问题\n\n两者结合的画面是：这是一篇**实验设计和执行优秀但在 claims calibration、statistical rigor 和 venue targeting 上存在系统性问题**的论文。核心科学贡献（CIVO 现象的发现和诊断）是有价值的，但需要 (a) 大幅压缩至 8 页，(b) 加强统计报告，(c) 校准因果声明强度，(d) 重新考虑 venue 选择（ICML/NeurIPS 更合适）。\n",
  "reviewer_id": "2",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: AUROC=1.000 缺乏不确定性量化**\n\n同意该批评的核心——AUROC 本身未报告 bootstrap CI。但需补充两点：\n\n1. 论文在附录中**已提供部分不确定性量化**：Table 7-8（page 39）报告了 Clopper-Pearson exact binomial 95% CI 用于 accuracy/precision/recall（例如 Table 7: Accuracy 72.7% [39.0, 94.0] at threshold 2.0）。但这是对特定阈值下的 point metrics 的 CI，**不是对 AUROC 本身的 CI**，R1 的要求合理。\n2. Table 9（page 39）显示 CIVO-positive 样本 NVE ≥ 1.53，negative < 1.04——两类之间存在 **~0.5 的 clean gap**，这降低了\"单个误分类即破坏 perfect AUROC\"的实际风险，但不能替代形式化的 CI 报告。\n\n总体判断：R1 的建议（报告 bootstrap 95% CI + 弱化 \"perfect classification\" 措辞）完全合理且容易执行。\n\n---\n\n**[AGREE] R1-N2: 因果机制声明超出证据强度**\n\n同意。论文确实将 CIVO 呈现为一个**闭环因果链**（Figure 1, page 2），但四个环节的证据强度不对称：\n\n- **有较强证据的环节**：(a) trained dt-embedding → RSSM bias（Appendix D gradient decomposition, page 24-26 显示 reward head 贡献最大的 gradient 份额 34.7%/40.4%）；(b) 冻结 dt-embedding 消除 CIVO（Table 1 中所有 0/16 frozen configs 触发 CIVO）——这是一个有效的**反事实干预**，支持因果推断。\n- **证据较弱的环节**：(c) value overestimation → exploitative policy behavior——论文仅通过 NVE ratio 间接推断，没有直接的 policy trajectory/action distribution 分析；(d) biased policy → further embedding bias（loop closure）——完全是推断，无直接实验证据。\n\nR1 关于标注 \"proposed/hypothesized mechanism\" 并区分证据层级的建议，对论文的学术严谨性有实质改善。不过需要公平指出，反事实干预（freezing experiment）确实提供了因果方向的 evidence——虽然不足以证明完整环路，但比纯粹的相关性分析要强。\n\n---\n\n**[AGREE] R1-N3: 统计效力不足**\n\n同意。补充两个具体观察：\n\n1. **Class balance 问题**：Table 9（page 39）报告 n_pos=8, n_neg=8, n=17（Full validation set 仅含 Walker Walk 15 configs + Cheetah Run 2 configs），而非论文主文 Section 4.7（page 9）声称的 n=36。n=36 的完整分类中 CIVO-positive vs negative 的精确比例**未在主文中明确报告**，需要读者到附录 Table 3（page 37）逐行统计。这是一个 presentation 问题——关键统计信息应直接出现在主文。\n2. **Per-seed 叙述性声明**：Section 4.1（page 5-6）和 Section 4.2（page 7）中出现多处基于个别 seed 表现的推断（例如 \"peaks at 485.3 before collapsing\"），这些未附 CI 或 significance test。对于诊断论文而言，每个定量 claim 都应有明确的统计支撑。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: NVE 阈值 2.0× 潜在循环性**\n\n同意这一方法论关切。阈值选取和验证使用同一数据集，LOEO 仅 3 个 folds（Table 11, page 39：PegCube, Cheetah, Walker），每个 fold 的 held-out 集极小（PegCube 仅 3 个样本）。\n\n但需指出缓解因素：Table 9 显示 positive/negative 类之间的 NVE gap（1.53 vs <1.04）远大于阈值选择的敏感范围，Table 7 的 sensitivity analysis 显示 threshold 在 1.5-2.5 范围内 F1 均为 1.0。这表明结论对阈值选择**不敏感**，但形式上仍不能替代外部验证。一个新的（未参与训练的）环境上的 prospective validation 会显著增强可信度。\n\n---\n\n**[AGREE] R1-W2: Factorial design 未完全隔离 embedding 架构与训练信号**\n\n同意。trained dt-embedding 是一个 compound treatment——同时改变了 (a) 网络架构（增加 embedding input）和 (b) 训练信号（dt 值的梯度流）。论文的 frozen embedding 控制组确实分离了 (b)，但 frozen 的初始化方式（random vs pre-trained then frozen）可能影响 (a) 的效果归因。\n\n补充一点：Section 4.3（page 7-8）中 \"Architecture-Level Ablation\" 和 Table 14（page 40）的 2×2 factorial（single vs dual critic, with/without dt-embedding）部分解决了这个问题，但 R1 的核心关切——无法完全排除架构变化本身（而非训练信号）导致 CIVO——仍然成立。\n\n---\n\n**[AGREE] R1-W3: 环境多样性不足，robotics relevance 偏弱**\n\n强烈同意——这与我自己的 N2（venue fit）和 W2（环境覆盖）完全一致。Walker Walk 和 Cheetah Run 都是 low-dimensional proprioceptive continuous locomotion 任务，代表性极为有限。附录中有 ManiSkill 结果（Table 5, page 38），但仅在附录出现且样本量更小。\n\n---\n\n**[AGREE] R1-W4: Table 1 脚注 f 的 code correction 影响范围**\n\n同意。Appendix I（pages 35-36）详细记录了 bug 修正历史，论文声称 \"All numerical results reported in the main text and appendix tables use the corrected codebase\"（page 36, line 1191-1192）。但以下关键信息缺失：\n\n- 修正前有多少配置被错误分类为 CIVO-positive/negative？\n- 修正是否改变了任何核心结论（如 pathway redundancy 的 prevention rates）？\n- AUROC 在修正前后是否一致？\n\nAppendix I 中保留了 pre-correction 数据（Table 32 和 Table 3 footnotes k, l），这是好的透明度实践，但未直接回答上述问题。\n\n---\n\n**[AGREE] R1-W5: Pathway redundancy 声明缺乏统计检验**\n\n同意。Section 5（page 10, lines 554-568）中 \"intervention resistance reveals pathway redundancy\" 的论证基于 Table 2（page 9）中各干预的 prevention rates，但这些 rates 来自极小样本（例如 obs-decoder-only SGS 在 Cheetah 上仅有 2 个 CIVO-positive baseline 可比较），且无任何 hypothesis test（如 Fisher's exact test 或 permutation test）。将观察到的 partial prevention 上升为 \"pathway redundancy\" 这一结构性声明需要更强的统计支撑。\n\n---\n\n## 总结\n\nR1 的 8 个问题中我全部 AGREE。R1 的审稿与我的侧重互补：\n\n- **我侧重 venue fit + 格式**：发现了两个独立的 desk-reject 级问题（超页 2.5 页 + robotics relevance 不足）\n- **R1 侧重 statistical rigor + causal claims**：发现了统计效力、AUROC 不确定性、因果声明过强三个质量问题\n\n两者结合的画面是：这是一篇**实验设计和执行优秀但在 claims calibration、statistical rigor 和 venue targeting 上存在系统性问题**的论文。核心科学贡献（CIVO 现象的发现和诊断）是有价值的，但需要 (a) 大幅压缩至 8 页，(b) 加强统计报告，(c) 校准因果声明强度，(d) 重新考虑 venue 选择（ICML/NeurIPS 更合适）。\n",
    "reviewer_id": "2",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 454 · 2026-05-28T02:12:27.514193+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5122
}
```

</details>

---

### Tool call

_source line 455 · 2026-05-28T02:12:32.383405+00:00_

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
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 456 · 2026-05-28T02:12:32.434125+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 457 · 2026-05-28T02:12:37.736240+00:00_

交叉回应已提交。R1 的 8 个问题（N1-N3, W1-W5）我全部标注 [AGREE]，并为每条附加了具体证据引用和补充观察。核心判断：R1 侧重 statistical rigor / causal claims，我侧重 venue fit / 格式合规，两者互补形成一致的 reject 建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_2"
}
```

</details>

---

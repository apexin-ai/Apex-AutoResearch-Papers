# paper writing introduction reframe

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_writing_introduction_reframe_20260522T052341.jsonl`
- **Structured JSON:** [`50fd368a9fa044975f91.json`](../../sessions/50/50fd368a9fa044975f91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Assistant

_source line 1 · 2026-05-22T05:23:51.778386+00:00_

You've hit your limit · resets 5pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T05:24:01.088011+00:00_

You've hit your limit · resets May 24, 1am (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341"
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T05:27:42.853569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T05:27:42.854326+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T05:27:42.854568+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/ 2>/dev/null",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/ 2>/dev/null",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T05:27:42.854722+00:00_

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
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T05:27:42.854849+00:00_

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
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T05:27:42.855009+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	\looseness=-1 Deploying a pretrained Vision-Language-Action model (VLA) on a new task typically requires fine-tuning on task-specific demonstrations, yet collecting such data is expensive and the resulting checkpoint may not generalize further.
5	An alternative is to keep the VLA frozen and attach a lightweight post-hoc correction module trained on task-specific VLA rollout data, improving action quality at inference time without modifying the base model.
6	Flow-matching VLAs~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are natural candidates: each forward pass produces a stochastic action sample, so drawing multiple samples opens the door to selection and correction without changing model weights.
7	The question is not only how to use these samples but \emph{when} to invest the additional compute: most control steps are easy and do not benefit from multi-sample correction, while a minority of hard steps account for the majority of task failures.
8	
9	\looseness=-1 Recent robustness evaluations~\cite{fei2025liberoplus} show that state-of-the-art VLAs lose over 65 percentage points under common deployment perturbations, making inference-time correction practically relevant.
10	Training-time methods~\cite{srpo2025,robustvla2025,digflow2025,liu2026ttvla} improve the base policy through robustness-aware objectives or test-time RL, but require retraining and remain bounded by the training distribution.
11	Inference-time methods leave the policy frozen: ReconVLA~\cite{chen2026reconvla} provides uncertainty quantification but does not learn corrective residuals; A2C2~\cite{a2c2_2025} trains a per-step correction head on action chunks but applies correction unconditionally without adaptive compute allocation; VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization at 2.41\,s per control step.
12	Despite growing interest, no prior work addresses a core efficiency question: how to determine per-step whether t
…[truncated 3116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T05:27:42.855166+00:00_

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
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T05:27:42.855346+00:00_

1	Frozen Vision-Language-Action (VLA) models can be improved at inference time without modifying weights, but existing approaches either apply correction unconditionally or require prohibitive compute.
2	We propose ACR-VLA, a lightweight adaptive correction pipeline for frozen flow-matching VLAs. At each control step, the pipeline draws $K{=}2$ action samples in a single batched forward pass and uses their pairwise $L_2$ distance ($\rho{=}0.9979$ vs.\ $K{=}10$ sample variance) as a per-step uncertainty gate. Low-uncertainty steps output the argmin-to-centroid sample directly; high-uncertainty steps apply bounded residual correction via a Correction Residual Module (CRM). The pipeline uses at most two VLA forward passes---performance gains come from learned correction, not additional sampling.
3	We validate ACR-VLA across three flow-matching VLAs (SmolVLA 0.4B, $\pi_{0.5}$ 3.6B, OpenVLA-OFT 7B) on four LIBERO benchmark suites. On SmolVLA, ACR-VLA achieves $18.3$\% on LIBERO-Object ($+$7.3\,pp vs.\ VLA-only) and $35.0$\% on LIBERO-Spatial ($+$5.6\,pp), matching fixed-$K{=}10$ unconditional correction with 80\% fewer forward passes. Systematic analysis reveals that learned correction is the active mechanism (55--78\% of the gain), while multi-sampling provides enabling centering---random selection alone fails to improve over VLA-only on either benchmark.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T05:27:42.855509+00:00_

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
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T05:27:42.855648+00:00_

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
15	\newcommand{\placeholder}[1]{---}
16	
17	\graphicspath{{figures/}}
18	
19	\title{ACR-VLA: Adaptive Conformal Refinement\\for Frozen Flow-Matching VLAs}
20	
21	\author{
22	  Anonymous
23	}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\keywords{Vision-Language-Action Models, Inference-Time Refinement, Robotic Manipulation}
34	
35	\input{introduction}
36	\input{related_work}
37	\input{method}
38	\input{experiments}
39	\input{discussion}
40	
41	\bibliography{references}
42	
43	\clearpage
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T05:27:42.855774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T05:27:42.855937+00:00_

1	
2	\section{Method}
3	\label{sec:method}
4	
5	\begin{figure}[t]
6	  \centering
7	  \includegraphics[width=\linewidth]{fig1_pipeline.pdf}
8	  \caption{Adaptive sample-select-correct pipeline. $K{=}2$ action samples are drawn from the frozen VLA; the argmin-to-centroid sample is selected, and a lightweight CRM applies bounded correction ($\|\boldsymbol{\delta}\|_2 \leq \varepsilon$) only when the pairwise $L_2$ distance exceeds the uncertainty threshold $\tau$.}
9	  \label{fig:pipeline}
10	\end{figure}
11	
12	\looseness=-1 Our method adaptively allocates inference-time compute for a frozen flow-matching VLA (Figure~\ref{fig:pipeline}). At each control step, a $K{=}2$ uncertainty probe determines whether the VLA is confident or uncertain; confident steps output the argmin-to-centroid sample directly, while uncertain steps apply a learned residual correction to the same sample via a lightweight module. The base VLA is never retrained.
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
24	We draw $K$ action chunks from $\
…[truncated 3076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T05:27:42.856132+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"^(@|\\\\\\\\label)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib | grep -iE \"openvla|kim|oft\" 2>/dev/null | head -5",
  "description": "Check for OpenVLA citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"^(@|\\\\\\\\label)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib | grep -iE \"openvla|kim|oft\" 2>/dev/null | head -5",
    "description": "Check for OpenVLA citations"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T05:27:42.856340+00:00_

@misc{kim2024openvla,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T05:27:42.856476+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "openvla|oft",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Grep",
  "tool_args": {
    "pattern": "openvla|oft",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T05:27:42.856592+00:00_

79:@misc{kim2024openvla,
80:    title={OpenVLA: An Open-Source Vision-Language-Action Model},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T05:27:42.856703+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{sec:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T05:27:42.856833+00:00_

docs/paper/related_work.tex:1:\section{Related Work}\label{sec:related_work}
docs/paper/experiments.tex:3:\label{sec:experiments}
docs/paper/experiments.tex:8:\label{sec:exp_setup}
docs/paper/experiments.tex:22:\label{sec:adaptive_k}
docs/paper/experiments.tex:64:\label{sec:main_results}
docs/paper/experiments.tex:102:\label{sec:magnitude_results}
docs/paper/experiments.tex:103:\label{sec:failure_modes}
docs/paper/method.tex:3:\label{sec:method}
docs/paper/method.tex:15:\label{sec:problem_setup}
docs/paper/method.tex:22:\label{sec:selection}
docs/paper/method.tex:32:\label{sec:crm}
docs/paper/method.tex:62:\label{sec:magnitude}
docs/paper/method.tex:67:\label{sec:adaptive_k_method}
docs/paper/review_template/corl_2026_template_submission/example.tex:73:\label{sec:citations}
docs/paper/review_template/corl_2026_template_submission/example.tex:82:\label{sec:result}
docs/paper/review_template/corl_2026_template_submission/example.tex:112:\label{sec:conclusion}
docs/paper/camera_ready_template/corl_2026_template_cameraready/example.tex:73:\label{sec:citations}
docs/paper/camera_ready_template/corl_2026_template_cameraready/example.tex:82:\label{sec:result}
docs/paper/camera_ready_template/corl_2026_template_cameraready/example.tex:112:\label{sec:conclusion}
docs/paper/appendix.tex:5:\label{sec:decomposition_appendix}
docs/paper/appendix.tex:15:\label{sec:magnitude_appendix}
docs/paper/appendix.tex:25:\label{sec:k_scaling}
docs/paper/appendix.tex:64:\label{sec:spatial_adaptive}
docs/paper/appendix.tex:93:\label{sec:applicability}
docs/paper/appendix.tex:112:\label{sec:per_task}
docs/paper/appendix.tex:151:\label{sec:latency}
docs/paper/appendix.tex:180:\label{sec:cross_vla}
docs/paper/introduction.tex:2:\label{sec:intro}
docs/paper/discussion.tex:5:\label{sec:conclusion}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T05:27:42.857000+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\n\\looseness=-1 Deploying a pretrained Vision-Language-Action (VLA) model on a new task usually requires fine-tuning on task demonstrations, yet collecting that data is expensive and the resulting checkpoint may not transfer further. A more attractive route keeps the VLA frozen and improves action quality at inference time. Flow-matching VLAs~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} fit this setting because each forward pass produces a stochastic action sample, so drawing multiple samples opens a path to selection and correction without retraining~\\cite{snell2024scaling}. The naive instantiation draws $K{=}10$ samples per control step and either averages them or applies an unconditional correction, but most control steps are easy and the extra forward passes are wasted compute. The question we ask is whether the same gain is reachable with adaptive, per-step allocation.\n\n\\looseness=-1 Recent work touches parts of this question without answering it. A2C2~\\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and inherits the temporal staleness of fixed chunks. ReconVLA~\\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\\cite{liu2026scvla} uses reinforcement learning on the base policy and therefore does not stay weight-frozen. VLA-Pilot~\\cite{li2025vlapilot} performs evolutionary search at $2.41$\\,s per control step, which rules out closed-loop deployment. None of these address the core efficiency question: can a frozen VLA decide \\emph{per step} whether it needs additional sampling and correction at all?\n\n\\looseness=-1 We propose \\textbf{ACR-VLA}, an adaptive inference-time pipeline for frozen flow-matching VLAs. ACR-VLA draws only $K{=}2$ samples in a single batched forward pass and uses their pairwise $L_2$ distance as a per-step uncertainty estimate. This minimal probe is well-calibrated: Spearman $\\rho{=}0.9979$ against the $K{=}10$ sample variance computed offline, whereas three alternatives (flow-matching velocity divergence, CRM correction magnitude at $K{=}1$ and at $K{=}2$) all yield $\\rho \\leq 0.15$. When the probe falls below threshold, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds threshold, a lightweight Correction Residual Module (CRM, ${\\sim}$327K parameters, $<\\!1\\%$ of the SmolVLA backbone) applies a bounded residual to the same sample. The pipeline uses at most two VLA forward passes per step, and batched $K{=}2$ inference matches single-sample latency (${\\sim}253$\\,ms).\n\n\\looseness=-1 On SmolVLA, ACR-VLA reaches $18.3 \\pm 2.1$\\% on LIBERO-Object ($+$7.3\\,pp over the $11.0 \\pm 1.3$\\% VLA-only baseline, 8 seeds) and $35.0 \\pm 1.0$\\% on LIBERO-Spatial ($+$5.6\\,pp over $29.4 \\pm 1.5$\\%, 5 seeds). The adaptive pipeline reaches the same task success as the fixed-$K{=}10$ unconditional pipeline while issuing 80\\% fewer VLA forward passes. We then apply the identical recipe, with only the per-task CRM retrained, to two larger flow-matching VLAs ($\\pi_{0.5}$~\\cite{black2024pi0} at $3.6$B and OpenVLA-OFT~\\cite{kim2024openvla} at $7$B) across all four LIBERO suites~\\cite{liu2023libero} (Object, Spatial, Goal, Long). The pipeline is VLA-agnostic by design: the $K{=}2$ probe, argmin selection, and bounded CRM correction do not depend on backbone scale or task family.\n\n\\looseness=-1 An ablation isolates where the gain comes from. Learned correction contributes $55$\\% of the gain at $K{=}5$ and $78$\\% at $K{=}10$, while random sample selection on its own fails to improve over the VLA-only baseline on either benchmark. Multi-sampling supplies a centered starting point and the uncertainty gate, but the active mechanism is the residual. This finding shaped the adaptive design: scaling samples beyond $K{=}2$ buys little once the correction is in place, so the budget is better spent on the residual than on extra sampling.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{ACR-VLA pipeline} (Section~\\ref{sec:method}): an adaptive $K{=}2$ uncertainty-gated CRM correction pipeline for frozen flow-matching VLAs. ACR-VLA reaches $18.3$\\% on LIBERO-Object and $35.0$\\% on LIBERO-Spatial ($+$7.3 / $+$5.6\\,pp over VLA-only) and matches the $K{=}10$ unconditional pipeline with 80\\% fewer forward passes.\n  \\item \\textbf{Cross-VLA validation} (Section~\\ref{sec:main_results}): the same recipe is evaluated on three flow-matching VLAs spanning $0.4$B to $7$B parameters and on all four LIBERO suites, providing evidence that the design is VLA-agnostic.\n  \\item \\textbf{Component analysis} (Section~\\ref{sec:main_results}): learned correction is the active mechanism (55--78\\% of the gain), multi-sampling provides centering, and random selection alone fails to improve. This analysis motivated the adaptive gate.\n  \\item \\textbf{Applicability boundaries} (Section~\\ref{sec:failure_modes}): stochastic VLA diversity is a prerequisite (tokenized VLAs are near-deterministic and lie outside scope), and the CRM requires task-specific calibration rather than a single global checkpoint.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\n\\looseness=-1 Deploying a pretrained Vision-Language-Action (VLA) model on a new task usually requires fine-tuning on task demonstrations, yet collecting that data is expensive and the resulting checkpoint may not transfer further. A more attractive route keeps the VLA frozen and improves action quality at inference time. Flow-matching VLAs~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} fit this setting because each forward pass produces a stochastic action sample, so drawing multiple samples opens a path to selection and correction without retraining~\\cite{snell2024scaling}. The naive instantiation draws $K{=}10$ samples per control step and either averages them or applies an unconditional correction, but most control steps are easy and the extra forward passes are wasted compute. The question we ask is whether the same gain is reachable with adaptive, per-step allocation.\n\n\\looseness=-1 Recent work touches parts of this question without answering it. A2C2~\\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and inherits the temporal staleness of fixed chunks. ReconVLA~\\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\\cite{liu2026scvla} uses reinforcement learning on the base policy and therefore does not stay weight-frozen. VLA-Pilot~\\cite{li2025vlapilot} performs evolutionary search at $2.41$\\,s per control step, which rules out closed-loop deployment. None of these address the core efficiency question: can a frozen VLA decide \\emph{per step} whether it needs additional sampling and correction at all?\n\n\\looseness=-1 We propose \\textbf{ACR-VLA}, an adaptive inference-time pipeline for frozen flow-matching VLAs. ACR-VLA draws only $K{=}2$ samples in a single batched forward pass and uses their pairwise $L_2$ distance as a per-step uncertainty estimate. This minimal probe is well-calibrated: Spearman $\\rho{=}0.9979$ against the $K{=}10$ sample variance computed offline, whereas three alternatives (flow-matching velocity divergence, CRM correction magnitude at $K{=}1$ and at $K{=}2$) all yield $\\rho \\leq 0.15$. When the probe falls below threshold, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds threshold, a lightweight Correction Residual Module (CRM, ${\\sim}$327K parameters, $<\\!1\\%$ of the SmolVLA backbone) applies a bounded residual to the same sample. The pipeline uses at most two VLA forward passes per step, and batched $K{=}2$ inference matches single-sample latency (${\\sim}253$\\,ms).\n\n\\looseness=-1 On SmolVLA, ACR-VLA reaches $18.3 \\pm 2.1$\\% on LIBERO-Object ($+$7.3\\,pp over the $11.0 \\pm 1.3$\\% VLA-only baseline, 8 seeds) and $35.0 \\pm 1.0$\\% on LIBERO-Spatial ($+$5.6\\,pp over $29.4 \\pm 1.5$\\%, 5 seeds). The adaptive pipeline reaches the same task success as the fixed-$K{=}10$ unconditional pipeline while issuing 80\\% fewer VLA forward passes. We then apply the identical recipe, with only the per-task CRM retrained, to two larger flow-matching VLAs ($\\pi_{0.5}$~\\cite{black2024pi0} at $3.6$B and OpenVLA-OFT~\\cite{kim2024openvla} at $7$B) across all four LIBERO suites~\\cite{liu2023libero} (Object, Spatial, Goal, Long). The pipeline is VLA-agnostic by design: the $K{=}2$ probe, argmin selection, and bounded CRM correction do not depend on backbone scale or task family.\n\n\\looseness=-1 An ablation isolates where the gain comes from. Learned correction contributes $55$\\% of the gain at $K{=}5$ and $78$\\% at $K{=}10$, while random sample selection on its own fails to improve over the VLA-only baseline on either benchmark. Multi-sampling supplies a centered starting point and the uncertainty gate, but the active mechanism is the residual. This finding shaped the adaptive design: scaling samples beyond $K{=}2$ buys little once the correction is in place, so the budget is better spent on the residual than on extra sampling.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{ACR-VLA pipeline} (Section~\\ref{sec:method}): an adaptive $K{=}2$ uncertainty-gated CRM correction pipeline for frozen flow-matching VLAs. ACR-VLA reaches $18.3$\\% on LIBERO-Object and $35.0$\\% on LIBERO-Spatial ($+$7.3 / $+$5.6\\,pp over VLA-only) and matches the $K{=}10$ unconditional pipeline with 80\\% fewer forward passes.\n  \\item \\textbf{Cross-VLA validation} (Section~\\ref{sec:main_results}): the same recipe is evaluated on three flow-matching VLAs spanning $0.4$B to $7$B parameters and on all four LIBERO suites, providing evidence that the design is VLA-agnostic.\n  \\item \\textbf{Component analysis} (Section~\\ref{sec:main_results}): learned correction is the active mechanism (55--78\\% of the gain), multi-sampling provides centering, and random selection alone fails to improve. This analysis motivated the adaptive gate.\n  \\item \\textbf{Applicability boundaries} (Section~\\ref{sec:failure_modes}): stochastic VLA diversity is a prerequisite (tokenized VLAs are near-deterministic and lie outside scope), and the CRM requires task-specific calibration rather than a single global checkpoint.\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T05:27:42.857236+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T05:27:42.857389+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tail -30",
  "description": "Compile paper to check for errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tail -30",
    "description": "Compile paper to check for errors"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T05:27:42.857526+00:00_

ures/fig3_kvalue.pdf>] [13 <./figures/fig4_diversity.pdf>]

LaTeX Warning: `h' float specifier changed to `ht'.

[14]) [15] (./main.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/ms
bm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (15 pages, 544338 bytes).
Transcript writ
…[truncated 16 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T05:27:42.857680+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"Introduction|Related Work|page \\[\" main.log | head -10",
  "description": "Find page breaks for intro"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"Introduction|Related Work|page \\[\" main.log | head -10",
    "description": "Find page breaks for intro"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T05:27:42.857794+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T05:27:42.857911+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w introduction.tex && grep -cE \"—|–\" introduction.tex",
  "description": "Count words and check for em/en dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w introduction.tex && grep -cE \"—|–\" introduction.tex",
    "description": "Count words and check for em/en dashes"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T05:27:42.858031+00:00_

675 introduction.tex
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T05:27:42.858193+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"ing,|novel|groundbreak|significantly|leverage|utilize|delve|myriad|plethora|paradigm shift\" introduction.tex",
  "description": "Check for forbidden patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"ing,|novel|groundbreak|significantly|leverage|utilize|delve|myriad|plethora|paradigm shift\" introduction.tex",
    "description": "Check for forbidden patterns"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T05:27:42.858361+00:00_

18:  \item \textbf{Component analysis} (Section~\ref{sec:main_results}): learned correction is the active mechanism (55--78\% of the gain), multi-sampling provides centering, and random selection alone fails to improve. This analysis motivated the adaptive gate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T05:27:42.858511+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "old_string": "learned correction is the active mechanism (55--78\\% of the gain), multi-sampling provides centering, and random selection alone fails to improve.",
  "new_string": "learned correction is the active mechanism (55--78\\% of the gain), multi-sampling provides a centered initial sample, and random selection alone fails to improve over VLA-only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
    "old_string": "learned correction is the active mechanism (55--78\\% of the gain), multi-sampling provides centering, and random selection alone fails to improve.",
    "new_string": "learned correction is the active mechanism (55--78\\% of the gain), multi-sampling provides a centered initial sample, and random selection alone fails to improve over VLA-only."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T05:27:42.858662+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T05:27:42.858777+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tail -5",
  "description": "Recompile to verify"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tail -5",
    "description": "Recompile to verify"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T05:27:42.858888+00:00_

sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (15 pages, 544349 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T05:27:42.858998+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -f 1 -l 2 main.pdf - | head -80",
  "description": "Check rendered page 1-2 content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -f 1 -l 2 main.pdf - | head -80",
    "description": "Check rendered page 1-2 content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T05:27:42.859138+00:00_

ACR-VLA: Adaptive Conformal Refinement
for Frozen Flow-Matching VLAs
Anonymous Author(s)
Affiliation
Address
email

Abstract: Frozen Vision-Language-Action (VLA) models can be improved at inference time without modifying weights, but existing approaches either apply correction unconditionally or require prohibitive compute. We propose ACR-VLA, a
lightweight adaptive correction pipeline for frozen flow-matching VLAs. At each
control step, the pipeline draws K=2 action samples in a single batched forward
pass and uses their pairwise L2 distance (ρ=0.9979 vs. K=10 sample variance) as
a per-step uncertainty gate. Low-uncertainty steps output the argmin-to-centroid
sample directly; high-uncertainty steps apply bounded residual correction via a
Correction Residual Module (CRM). The pipeline uses at most two VLA forward passes—performance gains come from learned correction, not additional
sampling. We validate ACR-VLA across three flow-matching VLAs (SmolVLA
0.4B, π0.5 3.6B, OpenVLA-OFT 7B) on four LIBERO benchmark suites. On
SmolVLA, ACR-VLA achieves 18.3% on LIBERO-Object (+7.3 pp vs. VLAonly) and 35.0% on LIBERO-Spatial (+5.6 pp), matching fixed-K=10 unconditional correction with 80% fewer forward passes. Systematic analysis reveals that
learned correction is the active mechanism (55–78% of the gain), while multisampling provides enabling centering—random selection alone fails to improve
over VLA-only on either benchmark.

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

Keywords: Vision-Language-Action Models, Inference-Time Refinement,
Robotic Manipulation

19
20

21

22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37

1

Introduction

Deploying a pretrained Vision-Language-Action (VLA) model on a new task usually requires
fine-tuning on task demonstrations, yet collecting that data is expensive and the resulting checkpoint
may not transfer further. A more attractive route keeps the VLA frozen and improves action quality
at inference time. Flow-matching VLAs [1, 2, 3] fit t
…[truncated 754 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T05:27:42.859294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -f 2 -l 3 main.pdf - | head -80",
  "description": "Check where intro ends"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -f 2 -l 3 main.pdf - | head -80",
    "description": "Check where intro ends"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T05:27:42.859458+00:00_

38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55

We propose ACR-VLA, an adaptive inference-time pipeline for frozen flow-matching VLAs. ACRVLA draws only K=2 samples in a single batched forward pass and uses their pairwise L2 distance
as a per-step uncertainty estimate. This minimal probe is well-calibrated: Spearman ρ=0.9979
against the K=10 sample variance computed offline, whereas three alternatives (flow-matching
velocity divergence, CRM correction magnitude at K=1 and at K=2) all yield ρ ≤ 0.15. When
the probe falls below threshold, the pipeline outputs the argmin-to-centroid sample directly; when
it exceeds threshold, a lightweight Correction Residual Module (CRM, ∼327K parameters, < 1%
of the SmolVLA backbone) applies a bounded residual to the same sample. The pipeline uses at
most two VLA forward passes per step, and batched K=2 inference matches single-sample latency
(∼253 ms).
On SmolVLA, ACR-VLA reaches 18.3 ± 2.1% on LIBERO-Object (+7.3 pp over the 11.0 ± 1.3%
VLA-only baseline, 8 seeds) and 35.0 ± 1.0% on LIBERO-Spatial (+5.6 pp over 29.4 ± 1.5%,
5 seeds). The adaptive pipeline reaches the same task success as the fixed-K=10 unconditional
pipeline while issuing 80% fewer VLA forward passes. We then apply the identical recipe,
with only the per-task CRM retrained, to two larger flow-matching VLAs (π0.5 [1] at 3.6B and
OpenVLA-OFT [14] at 7B) across all four LIBERO suites [30] (Object, Spatial, Goal, Long).
The pipeline is VLA-agnostic by design: the K=2 probe, argmin selection, and bounded CRM
correction do not depend on backbone scale or task family.

61

An ablation isolates where the gain comes from. Learned correction contributes 55% of the gain
at K=5 and 78% at K=10, while random sample selection on its own fails to improve over the
VLA-only baseline on either benchmark. Multi-sampling supplies a centered starting point and the
uncertainty gate, but the active mechanism is the residual. This finding shaped the adaptive design:
scaling samples
…[truncated 1209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-22T05:27:42.859650+00:00_

Introduction rewritten at `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex`.

**Structure**: Problem (frozen VLA + wasted K=10 compute) → Gap (A2C2/ReconVLA/SC-VLA/VLA-Pilot none ask the per-step question) → ACR-VLA pipeline (K=2 + ρ=0.9979 probe + argmin + CRM, ≤2 forwards) → SmolVLA headline results + cross-VLA recipe applied to π₀.₅/OpenVLA-OFT × 4 LIBERO suites → Analysis as supporting evidence (correction 55–78%, random selection fails) → 4 contributions.

**Verified**: 675 words, ~1.1 pages (ends mid-page 2 before §Related Work), zero em/en-dashes, no forbidden vocabulary (novel/significantly/leverage/utilize/etc.), compiles cleanly. Cross-VLA and 4-suite phrased descriptively without `\placeholder`. All references use the cite keys you listed plus `kim2024openvla` for OpenVLA-OFT.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_reframe_20260522T052341"
}
```

</details>

---

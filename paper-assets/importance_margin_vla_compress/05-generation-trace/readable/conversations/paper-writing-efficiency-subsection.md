# paper writing efficiency subsection

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_writing_efficiency_subsection_20260525T192453.jsonl`
- **Structured JSON:** [`2bcdaf210e3888e5f7fa.json`](../../sessions/2b/2bcdaf210e3888e5f7fa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-25T19:27:42.281465+00:00_

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
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T19:27:42.282320+00:00_

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
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T19:27:42.282641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T19:27:42.283072+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on the LIBERO benchmark~\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.
8	
9	Four models are evaluated in closed-loop robotic control: $\pi_{0.5}$~\cite{black2025pi05} (4B parameters, linear projection with $\times\!\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\cite{lewis2020bart}, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$ folding, 128 tokens, CV$\,{=}\,$0.314). Two additional models are analyzed via offline metrics only: $\pi_{0}$~\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\,{=}\,$0.038) and OFT~\cite{kim2025openoft} (7B, three-layer MLP, 512 tokens, CV$\,{=}\,$0.219). All six architectures contribute to the CV diagnostic (Section~\ref{sec:cv_sensitivity}). Table~\ref{tab:model_properties} summarizes model properties and connector details.
10	
11	We follow the pruning protocol of Section~\ref{sec:pruning_protocol} at retention ratios $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, reporting mean success rate (SR) over 500 episodes with Wilson 95\% confidence intervals.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	The pruning response depends on token independence imposed by the connector and task complexity (Figure~\ref{fig:teaser}). Token-independent connectors degrade gracefully; token-entanglin
…[truncated 17279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T19:27:42.283409+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\placeholder|\\\\newcommand.*placeholder",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\placeholder|\\\\newcommand.*placeholder",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T19:27:42.283609+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T19:27:42.283843+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T19:27:42.284049+00:00_

docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/background.tex
docs/paper/results_v2.tex
docs/paper/experimental_setup.tex
docs/paper/analysis.tex
docs/paper/results.tex
docs/paper/discussion.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T19:27:42.284291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T19:27:42.284522+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	
13	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
14	
15	\begin{document}
16	\maketitle
17	
18	\input{abstract}
19	
20	\keywords{vision-language-action models, token pruning, robot learning}
21	
22	\input{introduction}
23	
24	\input{related_work}
25	
26	\input{method}
27	
28	\input{experiments}
29	
30	\input{conclusion}
31	
32	\bibliography{references}
33	
34	\input{appendix}
35	
36	\end{document}
37	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T19:27:42.284784+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "xcolor|\\\\textcolor",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Grep",
  "tool_args": {
    "pattern": "xcolor|\\\\textcolor",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T19:27:42.284979+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T19:27:42.285189+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "corl_2026.sty",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Glob",
  "tool_args": {
    "pattern": "corl_2026.sty",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T19:27:42.285390+00:00_

docs/paper/corl_2026.sty

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T19:27:42.285576+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "xcolor|color",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.sty",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Grep",
  "tool_args": {
    "pattern": "xcolor|color",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.sty",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T19:27:42.285771+00:00_

74:\RequirePackage{color}
101:  \definecolor{mydarkblue}{rgb}{0,0.08,0.45}
109:    colorlinks=true,
110:    linkcolor=mydarkblue,
111:    citecolor=mydarkblue,
112:    filecolor=mydarkblue,
113:    urlcolor=mydarkblue,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T19:27:42.286148+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
  "old_string": "\\usepackage{subcaption}\n\n\\title",
  "new_string": "\\usepackage{subcaption}\n\n\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
    "old_string": "\\usepackage{subcaption}\n\n\\title",
    "new_string": "\\usepackage{subcaption}\n\n\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\title"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T19:27:42.286409+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T19:27:42.286641+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "\\end{table}\n\n\\paragraph{Limitations.}",
  "new_string": "\\end{table}\n\n\\subsection{Computational Efficiency}\n\\label{sec:efficiency}\n\nToken pruning shortens the LLM's input sequence and reduces computation in both attention and feedforward layers. Self-attention FLOPs scale quadratically with sequence length: removing $(1{-}k) \\cdot N$ vision tokens from a total sequence of $L = N + L_\\text{other}$ tokens reduces attention cost to a fraction\n\\begin{equation}\n\\rho_\\text{attn} = \\left(\\frac{L - (1{-}k) \\cdot N}{L}\\right)^{\\!2},\n\\label{eq:flops_ratio}\n\\end{equation}\nwhile FFN costs decrease linearly by $(1{-}k) \\cdot N / L$. The practical impact scales with the vision-to-total token ratio. For $\\pi_{0.5}$, vision tokens dominate the input ($N{=}768$ of $L{\\approx}900$): at $k{=}0.9$, removing 77 tokens cuts attention FLOPs by ${\\sim}$16\\% and FFN cost by ${\\sim}$9\\%; at $k{=}0.5$, removing 384 tokens yields ${\\sim}$67\\% attention and ${\\sim}$43\\% FFN savings. These reductions apply at operating points where L2 scoring preserves ${\\geq}$95\\% SR (Table~\\ref{tab:main_results}). X-VLA's compact 50-token representation limits absolute savings regardless of pruning ratio. For SmolVLA, VTR at $M{=}16$ achieves 87.5\\% vision token compression with ${\\leq}$1.1\\,pp SR loss (Section~\\ref{sec:vtr_recovery}), the largest practical reduction in our study.\n\nPreliminary single-GPU measurements indicate \\placeholder{XX\\,ms} per-step latency for $\\pi_{0.5}$ at full token count, reduced to \\placeholder{YY\\,ms} at $k{=}0.9$ (\\placeholder{ZZ\\%} wall-clock speedup). Full latency profiling across architectures is in progress.\n\n\\paragraph{Limitations.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "old_string": "\\end{table}\n\n\\paragraph{Limitations.}",
    "new_string": "\\end{table}\n\n\\subsection{Computational Efficiency}\n\\label{sec:efficiency}\n\nToken pruning shortens the LLM's input sequence and reduces computation in both attention and feedforward layers. Self-attention FLOPs scale quadratically with sequence length: removing $(1{-}k) \\cdot N$ vision tokens from a total sequence of $L = N + L_\\text{other}$ tokens reduces attention cost to a fraction\n\\begin{equation}\n\\rho_\\text{attn} = \\left(\\frac{L - (1{-}k) \\cdot N}{L}\\right)^{\\!2},\n\\label{eq:flops_ratio}\n\\end{equation}\nwhile FFN costs decrease linearly by $(1{-}k) \\cdot N / L$. The practical impact scales with the vision-to-total token ratio. For $\\pi_{0.5}$, vision tokens dominate the input ($N{=}768$ of $L{\\approx}900$): at $k{=}0.9$, removing 77 tokens cuts attention FLOPs by ${\\sim}$16\\% and FFN cost by ${\\sim}$9\\%; at $k{=}0.5$, removing 384 tokens yields ${\\sim}$67\\% attention and ${\\sim}$43\\% FFN savings. These reductions apply at operating points where L2 scoring preserves ${\\geq}$95\\% SR (Table~\\ref{tab:main_results}). X-VLA's compact 50-token representation limits absolute savings regardless of pruning ratio. For SmolVLA, VTR at $M{=}16$ achieves 87.5\\% vision token compression with ${\\leq}$1.1\\,pp SR loss (Section~\\ref{sec:vtr_recovery}), the largest practical reduction in our study.\n\nPreliminary single-GPU measurements indicate \\placeholder{XX\\,ms} per-step latency for $\\pi_{0.5}$ at full token count, reduced to \\placeholder{YY\\,ms} at $k{=}0.9$ (\\placeholder{ZZ\\%} wall-clock speedup). Full latency profiling across architectures is in progress.\n\n\\paragraph{Limitations.}"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T19:27:42.286984+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T19:27:42.287227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "offset": "153",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "offset": "153",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T19:27:42.287471+00:00_

153	\bottomrule
154	\end{tabular}
155	\end{table}
156	
157	\subsection{Computational Efficiency}
158	\label{sec:efficiency}
159	
160	Token pruning shortens the LLM's input sequence and reduces computation in both attention and feedforward layers. Self-attention FLOPs scale quadratically with sequence length: removing $(1{-}k) \cdot N$ vision tokens from a total sequence of $L = N + L_\text{other}$ tokens reduces attention cost to a fraction
161	\begin{equation}
162	\rho_\text{attn} = \left(\frac{L - (1{-}k) \cdot N}{L}\right)^{\!2},
163	\label{eq:flops_ratio}
164	\end{equation}
165	while FFN costs decrease linearly by $(1{-}k) \cdot N / L$. The practical impact scales with the vision-to-total token ratio. For $\pi_{0.5}$, vision tokens dominate the input ($N{=}768$ of $L{\approx}900$): at $k{=}0.9$, removing 77 tokens cuts attention FLOPs by ${\sim}$16\% and FFN cost by ${\sim}$9\%; at $k{=}0.5$, removing 384 tokens yields ${\sim}$67\% attention and ${\sim}$43\% FFN savings. These reductions apply at operating points where L2 scoring preserves ${\geq}$95\% SR (Table~\ref{tab:main_results}). X-VLA's compact 50-token representation limits absolute savings regardless of pruning ratio. For SmolVLA, VTR at $M{=}16$ achieves 87.5\% vision token compression with ${\leq}$1.1\,pp SR loss (Section~\ref{sec:vtr_recovery}), the largest practical reduction in our study.
166	
167	Preliminary single-GPU measurements indicate \placeholder{XX\,ms} per-step latency for $\pi_{0.5}$ at full token count, reduced to \placeholder{YY\,ms} at $k{=}0.9$ (\placeholder{ZZ\%} wall-clock speedup). Full latency profiling across architectures is in progress.
168	
169	\paragraph{Limitations.}
170	All evaluations use LIBERO simulation; we provide no sim-to-real evidence. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing causal isolation. The CV--SR correlation relies on four closed-loop models, too few for a general law. VTR is validated on SmolVLA only. M
…[truncated 208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-25T19:27:42.287782+00:00_

Inserted. Two changes made:

1. **`main.tex`**: Added `\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}` in the preamble (uses the `color` package already loaded by `corl_2026.sty`).

2. **`experiments.tex`** (lines 157-167): New `\subsection{Computational Efficiency}` with:
   - **Paragraph 1** (~150 words): Quadratic attention FLOPs formula (Eq. \ref{eq:flops_ratio}), concrete numbers for π₀.₅ (16% attention savings at k=0.9, 67% at k=0.5), notes that X-VLA's 50 tokens limit gains, and SmolVLA VTR at M=16 gives the largest practical compression (87.5%).
   - **Paragraph 2** (~30 words): Three `\placeholder{}` markers for wall-clock latency measurements (baseline, k=0.9, speedup %).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_efficiency_subsection_20260525T192453"
}
```

</details>

---

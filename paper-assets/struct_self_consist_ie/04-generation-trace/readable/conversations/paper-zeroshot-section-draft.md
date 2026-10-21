# paper zeroshot section draft

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_zeroshot-section-draft_20260519T170646.jsonl`
- **Structured JSON:** [`453086e0fe411f3c4210.json`](../../sessions/45/453086e0fe411f3c4210.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-19T17:11:09.068071+00:00_

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
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T17:11:09.068919+00:00_

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
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T17:11:09.069188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md",
    "limit": "120"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T17:11:09.069481+00:00_

1	# Paper Framing — struct_self_consist_ie
2	
3	> Updated 2026-05-19 — D157+D160 TRIPLE CONTRIBUTION + SCALE UPGRADE. Title: "Strong Predictors, Weak Selectors: Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition". Entity construction θ=2/N (+1.02pp SciERC, +1.40pp FewNERD, multi-seed N=8 mean). **72B zero-shot confirms gap is fundamental**: LP ρ=-0.002 (CoNLL) / 0.081 (SciERC); LP-weighted construction +1.53pp (SciERC ZS); θ=2/N fails in zero-shot (-0.52pp SciERC, -0.92pp CoNLL). Gating bootstrap CI: τ=0.3 stable in [0.2,0.4]. D162: Decomposition formula deleted (R²=-8.53). Scale: 7B→14B→32B→72B Qwen2.5 + 8B cross-family (Qwen3+LLaMA). 14B/32B training in progress.
4	
5	## Target Venue
6	- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)
7	- Deadline: ARR May cycle, 2026-05-25
8	
9	## Core Claims (D157 updated — TRIPLE CONTRIBUTION: QE + diagnostic + prescriptive)
10	
11	### Claim 1 (PRIMARY — Dual Contribution: QE Framework + Selection Diagnostic)
12	**Positive contribution (A)**: Confidence signals reliably predict structured IE output quality at the population level (AUROC up to 0.82, ρ up to 0.45), enabling practical QE/selective prediction.
13	**Diagnostic contribution (B)** (D154 revised): Selection viability depends on LP signal quality and dataset characteristics, not degeneracy alone:
14	- **Degeneracy as headroom predictor**: High degeneracy eliminates selection headroom (CoNLL 47.4% degen → 0 net gain). Within fixed dataset-model settings, degeneracy causally modulates LP effectiveness (SciERC epoch ablation: −1.18/+0.74/+0.99pp at 3/5/10 epochs; per-entity-type within Few-NERD ρ=−0.881). But across datasets, degeneracy alone does NOT predict LP selection direction (23-point cross-configuration ρ=0.052, p=0.81).
15	- **LP-quality alignment as primary predictor**: LP must track entity-level F1 within instances. Few-NERD within-instance ρ(LP,F1) ≈ 0.5-0.66 → LP selection +1.36pp (p<0.05). SciERC ρ(LP,F1) ≈ 0.
…[truncated 15539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T17:11:09.069657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T17:11:09.069788+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T17:11:09.069933+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T17:11:09.070053+00:00_

docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T17:11:09.070203+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T17:11:09.070338+00:00_

docs/paper/sections/checklist.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/introduction.tex
docs/paper/sections/abstract.tex
docs/paper/sections/limitations.tex
docs/paper/sections/discussion.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/experiments.tex
docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T17:11:09.070467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T17:11:09.070603+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Diagnosing and Addressing Self-Consistency for Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\section*{Responsible NLP Research Checklist}
47	\input{sections/checklist}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T17:11:09.070736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T17:11:09.070995+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\topr
…[truncated 18335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T17:11:09.071173+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T17:11:09.071319+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Three factors qualitatively constrain selection: instance degeneracy (17.8--67.9\%) compresses the candidate space, limited oracle headroom bounds achievable gains, and LP compression (within-instance $\rho$ 0.043--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}), but $\varepsilon{=}0.05$ is post-hoc ($p_{\text{adj}}{=}0.14$ after joint correction; Appendix~\ref{app:epsilon_robustness}), so this is exploratory evidence.
6	Temperature disentangles degeneracy from alignment: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve (median $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}); the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms (Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}); our negative results are specific to fine-tuned models with constrained decoding (Appendix~\ref{app:when_selection_works}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T17:11:09.071612+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -d /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if paper/sections directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -d /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check if paper/sections directory exists"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T17:11:09.071774+00:00_

DIR_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T17:11:09.071907+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections",
  "description": "Create paper/sections directory for draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections",
    "description": "Create paper/sections directory for draft"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T17:11:09.072029+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T17:11:09.072189+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
  "content": "%% Draft: Zero-shot / Scaling paragraph for \\S5.5 (Scaling Behavior)\n%% Exp ID: exp_qwen25_72b_zeroshot (all 72B ZS numbers)\n%% Status: Draft for Paper Agent integration. Replaces current \\S5.5 content.\n%% Pending: 7B/14B/32B FT results for full scaling curve; 72B FT for regime disentanglement.\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTo test whether the correlation-selection gap is specific to fine-tuned models, we evaluate Qwen2.5-72B-Instruct (AWQ 4-bit) in a zero-shot setting across all three primary datasets ($N{=}8$, $T{=}1.0$, no task-specific training).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B: QE correlations and entity construction ($N{=}8$, $T{=}1.0$). Degen.\\ = instance degeneracy (\\%). Constr.\\ = LP-weighted entity construction $\\Delta$F1 vs.\\ greedy (pp). $^\\dagger$Majority voting (uniform weights).}\n\\label{tab:zs_72b}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccccr@{}}\n\\toprule\nDataset & Regime & Greedy & Degen. & LP $\\rho$ & SJ $\\rho$ & VC $\\rho$ & Constr. \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 17.8\\% & .205 & .360 & .379 & $+$1.02 \\\\\n       & 72B ZS & .399 & 21.0\\% & .081 & .217 & .277 & $+$1.53 \\\\\n\\midrule\nFew-NERD & 8B FT & .748 & 13.0\\% & .220 & .380 & --- & $+$1.40 \\\\\n         & 72B ZS & .628 & 46.2\\% & .119 & .345 & .416 & $-$0.20 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & 61.7\\% & .302 & .436 & .424 & $-$0.39 \\\\\n       & 72B ZS & .712 & 67.7\\% & $-$.002 & .304 & .297 & $-$0.37 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{LP requires fine-tuning calibration.}\nTable~\\ref{tab:zs_72b} compares QE correlations between regimes.\nLP $\\rho$ drops to near zero in the zero-shot setting: from $0.205$ to $0.081$ on SciERC, $0.220$ to $0.119$ on Few-NERD, and $0.302$ to $-0.002$ on CoNLL.\nFine-tuning calibrates the model's token-level confidence to task-specific quality gradients; without this calibration, LP provides little discriminative signal for candidate quality.\n\n\\paragraph{Structural signals generalize beyond fine-tuning.}\nVC and SJ retain moderate correlations in the zero-shot regime (VC $\\rho{=}0.277$--$0.416$, SJ $\\rho{=}0.217$--$0.345$), despite the absence of task-specific training.\nThese signals measure inter-sample agreement, a property of output consistency that does not require the model's confidence to be calibrated to a particular task.\nThe divergence between LP and structural signals under zero-shot conditions reflects the correlation-selection gap from a complementary angle: structural signals capture consistency as a task-agnostic distributional property, while LP depends on fine-tuning to align confidence with performance.\n\n\\paragraph{Degeneracy gates construction effectiveness.}\nEntity construction (\\S\\ref{sec:prescriptive}) with LP-weighting yields $+1.53$\\,pp on SciERC ($p{=}0.008$, 95\\% CI [$+0.25$, $+2.82$]\\,pp), where zero-shot degeneracy is lowest (21.0\\%).\nMajority voting also improves SciERC by $+1.39$\\,pp; the marginal contribution of LP-weighting over uniform voting is $+0.14$\\,pp.\nOn Few-NERD (46.2\\% degeneracy, $-0.20$\\,pp) and CoNLL (67.7\\%, $-0.37$\\,pp), construction provides no benefit.\nThis monotonic relationship between degeneracy and construction gain is consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: construction recovers value only when candidate diversity is sufficient for recall-driven aggregation.\n\n\\paragraph{The gap is not a fine-tuning artifact.}\nZero-shot LP $\\rho$ approaches zero on all three datasets, and LP selection fails on SciERC ($-0.1$\\,pp) and CoNLL ($-0.4$\\,pp).\nThe same structural factors identified in \\S\\ref{sec:selection_gap} operate here: weak LP-quality alignment and instance degeneracy compress the effective candidate space.\nThat the gap persists at $9{\\times}$ the parameter count, in a zero-shot regime without LoRA fine-tuning, and across three datasets with varying difficulty is consistent with the gap being a structural property of self-consistency applied to structured IE rather than an artifact of a specific training configuration.\n\n%% Placeholder: scaling curve figure\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve (4B/8B/14B/32B/72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% TODO: 7B/14B/32B fine-tuned results to complete the scaling curve.\n%% TODO: 72B fine-tuned results to disentangle scale effect from training regime effect.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
    "content": "%% Draft: Zero-shot / Scaling paragraph for \\S5.5 (Scaling Behavior)\n%% Exp ID: exp_qwen25_72b_zeroshot (all 72B ZS numbers)\n%% Status: Draft for Paper Agent integration. Replaces current \\S5.5 content.\n%% Pending: 7B/14B/32B FT results for full scaling curve; 72B FT for regime disentanglement.\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTo test whether the correlation-selection gap is specific to fine-tuned models, we evaluate Qwen2.5-72B-Instruct (AWQ 4-bit) in a zero-shot setting across all three primary datasets ($N{=}8$, $T{=}1.0$, no task-specific training).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B: QE correlations and entity construction ($N{=}8$, $T{=}1.0$). Degen.\\ = instance degeneracy (\\%). Constr.\\ = LP-weighted entity construction $\\Delta$F1 vs.\\ greedy (pp). $^\\dagger$Majority voting (uniform weights).}\n\\label{tab:zs_72b}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccccr@{}}\n\\toprule\nDataset & Regime & Greedy & Degen. & LP $\\rho$ & SJ $\\rho$ & VC $\\rho$ & Constr. \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 17.8\\% & .205 & .360 & .379 & $+$1.02 \\\\\n       & 72B ZS & .399 & 21.0\\% & .081 & .217 & .277 & $+$1.53 \\\\\n\\midrule\nFew-NERD & 8B FT & .748 & 13.0\\% & .220 & .380 & --- & $+$1.40 \\\\\n         & 72B ZS & .628 & 46.2\\% & .119 & .345 & .416 & $-$0.20 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & 61.7\\% & .302 & .436 & .424 & $-$0.39 \\\\\n       & 72B ZS & .712 & 67.7\\% & $-$.002 & .304 & .297 & $-$0.37 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{LP requires fine-tuning calibration.}\nTable~\\ref{tab:zs_72b} compares QE correlations between regimes.\nLP $\\rho$ drops to near zero in the zero-shot setting: from $0.205$ to $0.081$ on SciERC, $0.220$ to $0.119$ on Few-NERD, and $0.302$ to $-0.002$ on CoNLL.\nFine-tuning calibrates the model's token-level confidence to task-specific quality gradients; without this calibration, LP provides little discriminative signal for candidate quality.\n\n\\paragraph{Structural signals generalize beyond fine-tuning.}\nVC and SJ retain moderate correlations in the zero-shot regime (VC $\\rho{=}0.277$--$0.416$, SJ $\\rho{=}0.217$--$0.345$), despite the absence of task-specific training.\nThese signals measure inter-sample agreement, a property of output consistency that does not require the model's confidence to be calibrated to a particular task.\nThe divergence between LP and structural signals under zero-shot conditions reflects the correlation-selection gap from a complementary angle: structural signals capture consistency as a task-agnostic distributional property, while LP depends on fine-tuning to align confidence with performance.\n\n\\paragraph{Degeneracy gates construction effectiveness.}\nEntity construction (\\S\\ref{sec:prescriptive}) with LP-weighting yields $+1.53$\\,pp on SciERC ($p{=}0.008$, 95\\% CI [$+0.25$, $+2.82$]\\,pp), where zero-shot degeneracy is lowest (21.0\\%).\nMajority voting also improves SciERC by $+1.39$\\,pp; the marginal contribution of LP-weighting over uniform voting is $+0.14$\\,pp.\nOn Few-NERD (46.2\\% degeneracy, $-0.20$\\,pp) and CoNLL (67.7\\%, $-0.37$\\,pp), construction provides no benefit.\nThis monotonic relationship between degeneracy and construction gain is consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: construction recovers value only when candidate diversity is sufficient for recall-driven aggregation.\n\n\\paragraph{The gap is not a fine-tuning artifact.}\nZero-shot LP $\\rho$ approaches zero on all three datasets, and LP selection fails on SciERC ($-0.1$\\,pp) and CoNLL ($-0.4$\\,pp).\nThe same structural factors identified in \\S\\ref{sec:selection_gap} operate here: weak LP-quality alignment and instance degeneracy compress the effective candidate space.\nThat the gap persists at $9{\\times}$ the parameter count, in a zero-shot regime without LoRA fine-tuning, and across three datasets with varying difficulty is consistent with the gap being a structural property of self-consistency applied to structured IE rather than an artifact of a specific training configuration.\n\n%% Placeholder: scaling curve figure\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve (4B/8B/14B/32B/72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% TODO: 7B/14B/32B fine-tuned results to complete the scaling curve.\n%% TODO: 72B fine-tuned results to disentangle scale effect from training regime effect.\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T17:11:09.072399+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T17:11:09.072563+00:00_

草稿已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex`。

**段落摘要**: 72B zero-shot 下 LP ρ 趋近零（三数据集均<0.12），而结构信号 VC/SJ 仍保持中等相关（0.22-0.42），表明 LP 依赖 fine-tuning 校准。Construction 效果与 degeneracy 单调相关（SciERC 21% degen → +1.53pp, p=0.008；majority vote 也 +1.39pp）。结论：gap 与 self-consistency 在结构化 IE 中的内在属性一致，非 LoRA-specific artifact。

**注意事项**:
- Few-NERD 8B FT 的 VC ρ 缺失（标记为 `---`），需 Paper Agent 补全
- LP selection 数字仅引用 SciERC/CoNLL（FewNERD ZS LP selection 精确值未在 registry 中）
- 7B/14B/32B 占位已预留

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_zeroshot-section-draft_20260519T170646"
}
```

</details>

---

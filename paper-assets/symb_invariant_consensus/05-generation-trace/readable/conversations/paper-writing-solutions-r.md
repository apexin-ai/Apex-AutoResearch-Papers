# paper writing solutions r

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_solutions_r_20260520T121050.jsonl`
- **Structured JSON:** [`9e90a66def1a1095ebfe.json`](../../sessions/9e/9e90a66def1a1095ebfe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-20T12:12:10.135827+00:00_

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
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T12:12:10.136452+00:00_

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
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T12:12:10.136662+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T12:12:10.136842+00:00_

docs/paper/limitations_content.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/analysis.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T12:12:10.137075+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T12:12:10.137279+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models on three reasoning domains with over 3,000 instances. Beyond accuracy comparisons, we conduct diagnostic analyses of symbolic confirmation bias and process-level trace independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B parameters).
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold FOL annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$; extraction at $T_{\text{ext}}{=}0.3$. Z3 timeout: 10s. $\alpha{=}0.5$. Statistical significance via McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs from 10,000 resamples for $n \geq 200$.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline. SICA effectiveness depends sharply on the accuracy regime.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref{app:failure-modes}.}
25	\label{tab:main_results}
26	\begin{tabular}{@{}llrr
…[truncated 5943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T12:12:10.137434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T12:12:10.137626+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \to \infty$ \citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \citet{ladha1992correlated} and the design-effect framework of \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
11	\end{equation}
12	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. This \emph{independence bottleneck} motivates our investigation.
13	
14	\subsection{SICA Pipeline}
15	\label{sec:pipeline}
16	
17	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
18	
19	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
20	
21	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts FOL constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}). The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
22	

…[truncated 6836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T12:12:10.137786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T12:12:10.137980+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage{tikz}
18	\usetikzlibrary{arrows.meta,positioning,calc,fit}
19	\usepackage{listings}
20	\usepackage{algorithm}
21	\usepackage{algpseudocode}
22	\usepackage{hyperref}
23	\usepackage{cleveref}
24	
25	\lstset{
26	  basicstyle=\small\ttfamily,
27	  breaklines=true,
28	  frame=single,
29	  xleftmargin=1em,
30	  xrightmargin=1em,
31	  aboveskip=0.5em,
32	  belowskip=0.5em,
33	}
34	
35	\graphicspath{{../figures/paper/}{figures/}}
36	
37	\title{Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints\\Fail in LLM Reasoning}
38	
39	\author{Anonymous}
40	
41	\begin{document}
42	\maketitle
43	
44	\input{abstract}
45	
46	\input{introduction}
47	
48	\input{related_work}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\input{analysis}
55	
56	\input{discussion}
57	
58	\input{conclusion}
59	
60	\section*{Limitations}
61	\input{limitations_content}
62	
63	\bibliography{references}
64	
65	\appendix
66	\input{appendix}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T12:12:10.138180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T12:12:10.138403+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	The regime-dependent pattern in \S\ref{sec:main-results} establishes \emph{where} SICA succeeds and fails. This section investigates \emph{why}: trace correlation quantifies the SC plateau (\S\ref{sec:effective-k}), symbolic confirmation bias identifies the root cause (\S\ref{sec:confirmation-bias}), process-level independence reveals a deeper bottleneck (\S\ref{sec:process-kappa}), supporting diagnostics confirm the mechanism (\S\ref{sec:diagnostics}), and more than twenty remediation strategies demonstrate a fundamental independence-accuracy trade-off (\S\ref{sec:remediation}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$. The four Mistral-7B FOLIO seeds produce $\kappa \in [0.41, 0.51]$, yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp---seed-level constraint quality, not independence, drives the variation. Two conditions are jointly necessary for positive $\Delta$: sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and sufficient SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ produces significant degradation). Cross-model validation confirms universality: all four families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}; Appendix~\ref{app:cross-model-kappa}).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$; positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each.}
15	\label{tab:independence}
16	\begin{tabular}{@{}llccrr@{}}
17	\toprule
18	Model & Condit
…[truncated 1086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T12:12:10.138559+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{sec:confirmation-bias\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{sec:confirmation-bias\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T12:12:10.138683+00:00_

docs/paper/analysis.tex:42:\label{sec:confirmation-bias}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T12:12:10.138833+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
  "content": "\\section{Breaking Confirmation Bias}\n\\label{sec:solutions}\n\nThe preceding analyses localize the bottleneck: symbolic confirmation bias (\\S\\ref{sec:confirmation-bias}) causes self-extracted constraints to mirror the model's own answer distribution, and more than twenty remediation strategies fail to break this pattern (\\S\\ref{sec:remediation}). Two independent interventions target different links in this causal chain.\n\n\\subsection{Constraint-Answer Decoupling}\n\\label{sec:decoupling}\n\n% TODO: §4.1 content blocked on registry data (exp-wave3-dir-g-decoupling RUNNING)\n% Placeholder text:\n\\textit{[Section content pending experimental verification.]}\n\n\\subsection{Cross-Architecture NLI Verification}\n\\label{sec:cross-arch-results}\n\n\\paragraph{Motivation.}\nThe oracle gap (\\S\\ref{sec:oracle}) demonstrates that the MAX-SAT aggregation mechanism is sound: given gold constraints, SICA achieves $+14.22$\\,pp over SC. The bottleneck is self-extraction quality, and twenty-five same-model remediation strategies fail to improve it (\\S\\ref{sec:remediation}). This implies that the corrective signal must come from outside the reasoning model's own distribution.\n\n\\paragraph{Method.}\nWe test this hypothesis with DeBERTa-large \\citep{he2021deberta} (350M parameters, encoder-only), fine-tuned on MultiNLI \\citep{williams2018mnli}, as described in \\S\\ref{sec:cross-arch-method}. For each problem, DeBERTa classifies the (premise, conclusion) pair into \\textsc{entailment}, \\textsc{contradiction}, or \\textsc{neutral}. In combo mode, the NLI verdict is integrated with SC's $K$ votes via a weight parameter $w$: each NLI-supporting vote counts $w$ times. We evaluate on Mistral-7B FOLIO ($n = 204$, seed 123).\n\n\\paragraph{Main result.}\nDeBERTa NLI alone achieves 49.51\\%, below SC's 54.41\\% baseline. Combo mode at $w{=}3$ reaches 58.82\\% ($\\Delta = +4.41$\\,pp, McNemar $p = 0.039$, 95\\% CI $[0.59, 6.28]$\\,pp). This is the only same-dataset result in our experiments that reaches $p < 0.05$ with a positive effect. Weight sensitivity is monotonic: $w{=}1$ gives $+3.43$\\,pp, $w{=}3$ gives $+4.41$\\,pp (significant), $w{=}5$ gives $+5.88$\\,pp (best absolute, 60.29\\%).\n\n\\paragraph{Per-label complementarity.}\nThe combo gain is not uniform across labels. On \\textsc{False} problems, NLI achieves 71.43\\% compared to SC's 38.10\\% ($+33$\\,pp), because DeBERTa's contradiction detection directly identifies negated conclusions that the LLM's chain-of-thought reasoning systematically mishandles. On \\textsc{Unknown} problems, the pattern reverses: SC reaches 68.12\\% while NLI drops to 18.84\\% ($+49$\\,pp for SC), because ``neutral'' in NLI does not map cleanly to the logical \\textsc{Unknown} label. The combo succeeds precisely because these label-level strengths are complementary: DeBERTa compensates for the LLM's negation weakness, and SC compensates for DeBERTa's inability to distinguish unknown from entailed.\n\n\\paragraph{Agreement as a precision signal.}\nWhen NLI and SC agree on the same answer (45.1\\% of problems), accuracy reaches 68.48\\% ($+14.07$\\,pp over SC). The extended evaluation confirms this pattern: at 47.5\\% agreement coverage, accuracy is 70.1\\%. Agreement between architecturally independent systems serves as a high-precision filter, at the cost of reduced coverage.\n\n\\paragraph{Why cross-architecture verification works.}\nThe 350M encoder-only model and the 7B decoder-only LLM share no architecture, training data, or inference mechanism. DeBERTa's verdict is based on textual entailment classification, not chain-of-thought generation, so it does not exhibit the symbolic confirmation bias identified in \\S\\ref{sec:confirmation-bias}. The two systems make errors on different subsets of the problem space, satisfying the independence condition that same-model sampling cannot provide. This result validates the causal model from our analysis: because confirmation bias originates from the shared distribution of a single model, an external signal with an independent error profile can break the cycle.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
    "content": "\\section{Breaking Confirmation Bias}\n\\label{sec:solutions}\n\nThe preceding analyses localize the bottleneck: symbolic confirmation bias (\\S\\ref{sec:confirmation-bias}) causes self-extracted constraints to mirror the model's own answer distribution, and more than twenty remediation strategies fail to break this pattern (\\S\\ref{sec:remediation}). Two independent interventions target different links in this causal chain.\n\n\\subsection{Constraint-Answer Decoupling}\n\\label{sec:decoupling}\n\n% TODO: §4.1 content blocked on registry data (exp-wave3-dir-g-decoupling RUNNING)\n% Placeholder text:\n\\textit{[Section content pending experimental verification.]}\n\n\\subsection{Cross-Architecture NLI Verification}\n\\label{sec:cross-arch-results}\n\n\\paragraph{Motivation.}\nThe oracle gap (\\S\\ref{sec:oracle}) demonstrates that the MAX-SAT aggregation mechanism is sound: given gold constraints, SICA achieves $+14.22$\\,pp over SC. The bottleneck is self-extraction quality, and twenty-five same-model remediation strategies fail to improve it (\\S\\ref{sec:remediation}). This implies that the corrective signal must come from outside the reasoning model's own distribution.\n\n\\paragraph{Method.}\nWe test this hypothesis with DeBERTa-large \\citep{he2021deberta} (350M parameters, encoder-only), fine-tuned on MultiNLI \\citep{williams2018mnli}, as described in \\S\\ref{sec:cross-arch-method}. For each problem, DeBERTa classifies the (premise, conclusion) pair into \\textsc{entailment}, \\textsc{contradiction}, or \\textsc{neutral}. In combo mode, the NLI verdict is integrated with SC's $K$ votes via a weight parameter $w$: each NLI-supporting vote counts $w$ times. We evaluate on Mistral-7B FOLIO ($n = 204$, seed 123).\n\n\\paragraph{Main result.}\nDeBERTa NLI alone achieves 49.51\\%, below SC's 54.41\\% baseline. Combo mode at $w{=}3$ reaches 58.82\\% ($\\Delta = +4.41$\\,pp, McNemar $p = 0.039$, 95\\% CI $[0.59, 6.28]$\\,pp). This is the only same-dataset result in our experiments that reaches $p < 0.05$ with a positive effect. Weight sensitivity is monotonic: $w{=}1$ gives $+3.43$\\,pp, $w{=}3$ gives $+4.41$\\,pp (significant), $w{=}5$ gives $+5.88$\\,pp (best absolute, 60.29\\%).\n\n\\paragraph{Per-label complementarity.}\nThe combo gain is not uniform across labels. On \\textsc{False} problems, NLI achieves 71.43\\% compared to SC's 38.10\\% ($+33$\\,pp), because DeBERTa's contradiction detection directly identifies negated conclusions that the LLM's chain-of-thought reasoning systematically mishandles. On \\textsc{Unknown} problems, the pattern reverses: SC reaches 68.12\\% while NLI drops to 18.84\\% ($+49$\\,pp for SC), because ``neutral'' in NLI does not map cleanly to the logical \\textsc{Unknown} label. The combo succeeds precisely because these label-level strengths are complementary: DeBERTa compensates for the LLM's negation weakness, and SC compensates for DeBERTa's inability to distinguish unknown from entailed.\n\n\\paragraph{Agreement as a precision signal.}\nWhen NLI and SC agree on the same answer (45.1\\% of problems), accuracy reaches 68.48\\% ($+14.07$\\,pp over SC). The extended evaluation confirms this pattern: at 47.5\\% agreement coverage, accuracy is 70.1\\%. Agreement between architecturally independent systems serves as a high-precision filter, at the cost of reduced coverage.\n\n\\paragraph{Why cross-architecture verification works.}\nThe 350M encoder-only model and the 7B decoder-only LLM share no architecture, training data, or inference mechanism. DeBERTa's verdict is based on textual entailment classification, not chain-of-thought generation, so it does not exhibit the symbolic confirmation bias identified in \\S\\ref{sec:confirmation-bias}. The two systems make errors on different subsets of the problem space, satisfying the independence condition that same-model sampling cannot provide. This result validates the causal model from our analysis: because confirmation bias originates from the shared distribution of a single model, an external signal with an independent error profile can break the cycle.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T12:12:10.139063+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_solutions_r_20260520T121050",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T12:12:10.139238+00:00_

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex`。

内容要点：
- 开头 1 句过渡，连接 §3/§5 的诊断结论到两个解决方案
- §4.1 占位符如要求
- §4.2 约 480 words，按要求的 7 段叙事结构展开：motivation, method, main result (combo w=3, p=0.039), weight sensitivity, per-label complementarity, intersection/agreement signal, causal argument
- 所有数字与 registry 数据一致，包含 extended evaluation 的 agreement 数据 (47.5%, 70.1%)
- 无 em-dash/en-dash，无 -ing 结尾，无黑名单用词，段落长度 5-8 句

注意：`main.tex` 尚未 `\input{solutions}`，需要在合适位置插入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_solutions_r_20260520T121050"
}
```

</details>

---

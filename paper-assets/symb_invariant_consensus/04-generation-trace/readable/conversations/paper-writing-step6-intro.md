# paper writing step6 intro

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_paper_writing_step6_intro_20260523T025141.jsonl`
- **Structured JSON:** [`183fa2295bc9eb15c7eb.json`](../../sessions/18/183fa2295bc9eb15c7eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-23T02:53:39.059381+00:00_

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
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T02:53:39.059995+00:00_

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
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T02:53:39.060211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T02:53:39.060417+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\text{eff}}$ as an ordinal diagnostic of vote diversity ($K
…[truncated 6808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T02:53:39.060571+00:00_

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
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T02:53:39.060745+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{SICA Pipeline}
5	\label{sec:pipeline}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\kappa$ \citep{fleiss1971kappa}), effective sample size reduces to
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa]
11	\end{equation}
12	(following \citet{ladha1992correlated}), motivating constraint-based aggregation.
13	
14	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
15	
16	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
17	
18	\looseness=-1
19	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
20	
21	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
22	\begin{equation}
23	\label{eq:maxsat}
24	\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
25	\end{equation}
26	Z3 \citep{demoura2008z3} solves this with a 10-second timeout. Answer assertion constra
…[truncated 3367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T02:53:39.060929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T02:53:39.061118+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. A shuffle control reveals this bias is \emph{structural}: randomizing constraint--answer associations while preserving per-trace counts yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($p > 0.7$), indicating that BR reflects the trace-count distribution rather than extraction-specific error. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting. This vacuity is $\alpha$-insensitive: agreement $\geq$99\% across $\alpha \in \{0.1, \ldots, 0.9\}$ (Table~\ref{tab:alpha-ablation}).
8	
9	\looseness=-1 This pattern generalizes: $4.97\times$ (Mistral), $3.85\times$ (Qwen-14B), $2.88\times$ (LLaMA), all $> 1.0$ with 95\% bootstrap CIs (Table~\ref{tab:cross-model-bias}). Cross-model extraction confirms universality across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb}). BR $> 1$ further holds across all eight cells of a $2{\times}2$ generator${\times}$extractor matrix on FOLIO and ProofWriter (range $1.94$--$2.70$; Appendix~\ref{app:2x2}). Constraints use trace-specific variables (56.4\% zero cross-answer overlap), collapsing aggregation to majority voting.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3pt}
15	\caption{Symbolic confirmation bias across nine models on FOLIO ($n = 204$). BR: mean per-problem bias ratio. $n_\
…[truncated 6169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T02:53:39.061352+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\\label{sec:introduction}\n\n\\looseness=-1\nCan a provably sound formal solver improve LLM reasoning if the constraints it operates on are self-extracted from the model's own traces? We show that the answer is no: Z3 validates 99\\% of self-extracted constraints, yet MAX-SAT produces answers identical to majority voting on 94.4\\% of problems. The formal verification layer is vacuous, not because the solver fails, but because extraction inherits the model's distributional bias. This finding challenges a natural extension of Self-Consistency (SC) \\citep{wang2023sc}, which samples $K$ chain-of-thought traces and selects the majority answer. SC's gains plateau and decline for strong models \\citep{loo2025reevaluating}; the gap between its theoretical promise (independent voters converge to truth \\citep{condorcet1785, ladha1992correlated}) and practice points to correlated errors that majority voting cannot correct.\n\n\\looseness=-1\nWe study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}). Across six models (7B--32B), three reasoning domains, and over 3{,}000 condition-evaluations with multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\\ref{tab:main_results}). Four conditions are confirmed equivalent within $\\pm$2\\,pp; ten remain underpowered for effects below ${\\sim}$2\\,pp.\n\n\\looseness=-1\nThe failure traces to \\emph{symbolic confirmation bias}: on problems where the model errs, 83.3\\% of self-extracted constraints support the incorrect majority answer (bias ratio $1.66$--$4.97\\times$ across nine models from 7B to frontier; \\S\\ref{sec:confirmation-bias}). A shuffle control confirms this bias is structural, proportional to the trace-count distribution rather than extraction-specific error ($p > 0.7$). Prior work shows LLMs cannot self-correct without external feedback \\citep{huang2024selfcorrect}; we demonstrate that this limitation extends to formal self-verification: even with a provably correct solver, self-extracted constraints carry no information beyond majority voting.\n\n\\looseness=-1\nTwenty-seven training-free remediation strategies produce neutral-to-negative results (\\S\\ref{sec:remediation}), revealing a fundamental independence-accuracy trade-off. Cross-architecture verification provides preliminary evidence of escaping the bottleneck: a structurally independent NLI verifier yields $+6.67$\\,pp on the weakest generator ($p < 0.001$); domain-adapted verification extends gains to generators with SC up to 72\\% with monotonically decreasing benefit (\\S\\ref{sec:cross-arch}). Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions (\\S\\ref{sec:diagnostic-framework}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction: symbolic confirmation bias (BR $1.66$--$4.97\\times$ across nine models) renders MAX-SAT equivalent to majority voting on 94.4\\% of problems. A shuffle control and 27 failed remediation strategies confirm the bias is structural (\\S\\ref{sec:confirmation-bias}, \\S\\ref{sec:remediation}).\n\n\\item \\textbf{Diagnostic framework.} Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions, providing practitioners with a priori prediction of symbolic aggregation viability from a $K{=}12$ pilot run (\\S\\ref{sec:diagnostic-framework}).\n\n\\item \\textbf{Cross-architecture escape.} Preliminary evidence that structurally independent NLI verification escapes the bottleneck ($+6.67$\\,pp on the weakest generator, $p < 0.001$), with gain decreasing monotonically as generator accuracy increases (\\S\\ref{sec:cross-arch}).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tikzpicture}[\n    node distance=0.3cm and 0.1cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,\n                text width=1.2cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract logical\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}\n\\label{fig:pipeline}\n\\end{figure}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\\label{sec:introduction}\n\n\\looseness=-1\nCan a provably sound formal solver improve LLM reasoning if the constraints it operates on are self-extracted from the model's own traces? We show that the answer is no: Z3 validates 99\\% of self-extracted constraints, yet MAX-SAT produces answers identical to majority voting on 94.4\\% of problems. The formal verification layer is vacuous, not because the solver fails, but because extraction inherits the model's distributional bias. This finding challenges a natural extension of Self-Consistency (SC) \\citep{wang2023sc}, which samples $K$ chain-of-thought traces and selects the majority answer. SC's gains plateau and decline for strong models \\citep{loo2025reevaluating}; the gap between its theoretical promise (independent voters converge to truth \\citep{condorcet1785, ladha1992correlated}) and practice points to correlated errors that majority voting cannot correct.\n\n\\looseness=-1\nWe study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}). Across six models (7B--32B), three reasoning domains, and over 3{,}000 condition-evaluations with multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\\ref{tab:main_results}). Four conditions are confirmed equivalent within $\\pm$2\\,pp; ten remain underpowered for effects below ${\\sim}$2\\,pp.\n\n\\looseness=-1\nThe failure traces to \\emph{symbolic confirmation bias}: on problems where the model errs, 83.3\\% of self-extracted constraints support the incorrect majority answer (bias ratio $1.66$--$4.97\\times$ across nine models from 7B to frontier; \\S\\ref{sec:confirmation-bias}). A shuffle control confirms this bias is structural, proportional to the trace-count distribution rather than extraction-specific error ($p > 0.7$). Prior work shows LLMs cannot self-correct without external feedback \\citep{huang2024selfcorrect}; we demonstrate that this limitation extends to formal self-verification: even with a provably correct solver, self-extracted constraints carry no information beyond majority voting.\n\n\\looseness=-1\nTwenty-seven training-free remediation strategies produce neutral-to-negative results (\\S\\ref{sec:remediation}), revealing a fundamental independence-accuracy trade-off. Cross-architecture verification provides preliminary evidence of escaping the bottleneck: a structurally independent NLI verifier yields $+6.67$\\,pp on the weakest generator ($p < 0.001$); domain-adapted verification extends gains to generators with SC up to 72\\% with monotonically decreasing benefit (\\S\\ref{sec:cross-arch}). Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions (\\S\\ref{sec:diagnostic-framework}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction: symbolic confirmation bias (BR $1.66$--$4.97\\times$ across nine models) renders MAX-SAT equivalent to majority voting on 94.4\\% of problems. A shuffle control and 27 failed remediation strategies confirm the bias is structural (\\S\\ref{sec:confirmation-bias}, \\S\\ref{sec:remediation}).\n\n\\item \\textbf{Diagnostic framework.} Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions, providing practitioners with a priori prediction of symbolic aggregation viability from a $K{=}12$ pilot run (\\S\\ref{sec:diagnostic-framework}).\n\n\\item \\textbf{Cross-architecture escape.} Preliminary evidence that structurally independent NLI verification escapes the bottleneck ($+6.67$\\,pp on the weakest generator, $p < 0.001$), with gain decreasing monotonically as generator accuracy increases (\\S\\ref{sec:cross-arch}).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tikzpicture}[\n    node distance=0.3cm and 0.1cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,\n                text width=1.2cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract logical\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}\n\\label{fig:pipeline}\n\\end{figure}\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T02:53:39.061620+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T02:53:39.061759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T02:53:39.061942+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Can a provably sound formal solver improve LLM reasoning if the constraints it operates on are self-extracted from the model's own traces? We show that the answer is no: Z3 validates 99\% of self-extracted constraints, yet MAX-SAT produces answers identical to majority voting on 94.4\% of problems. The formal verification layer is vacuous, not because the solver fails, but because extraction inherits the model's distributional bias. This finding challenges a natural extension of Self-Consistency (SC) \citep{wang2023sc}, which samples $K$ chain-of-thought traces and selects the majority answer. SC's gains plateau and decline for strong models \citep{loo2025reevaluating}; the gap between its theoretical promise (independent voters converge to truth \citep{condorcet1785, ladha1992correlated}) and practice points to correlated errors that majority voting cannot correct.
5	
6	\looseness=-1
7	We study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). Across six models (7B--32B), three reasoning domains, and over 3{,}000 condition-evaluations with multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). Four conditions are confirmed equivalent within $\pm$2\,pp; ten remain underpowered for effects below ${\sim}$2\,pp.
8	
9	\looseness=-1
10	The failure traces to \emph{symbolic confirmation bias}: on problems where the model errs, 83.3\% of self-extracted constraints support the incorrect majority answer (bias ratio $1.66$--$4.97\times$ across nine models from 7B to frontier; \S\ref{sec:confirmation-bias}). A shuffle control confirms this bias is structural, proportional to the trace-count distribution rather than extraction-specific error ($p > 0.7$). Prior work shows LLMs c
…[truncated 3845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_step6_intro_20260523T025141",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T02:53:39.062147+00:00_

Written and verified. Changes from the original:

- **Opening**: Z3 paradox hook leads (replaces generic test-time scaling opener); SC/CJT context compressed to 2 sentences
- **Removed**: Long CJT paragraph (old lines 14-20), verbose oracle/independence-accuracy details, C3 "Process-level independence analysis"
- **Added**: Power caveat (line 7: "Four conditions confirmed equivalent; ten underpowered")
- **Softened**: Cross-architecture uses "preliminary evidence", "on the weakest generator" (line 13)
- **Contributions**: 3 items, each ~3 lines (down from 3 items at 5-8 lines each)
- **Figure 1**: TikZ block preserved exactly
- **Style**: No em-dashes, no AI clichés, `\looseness=-1` on all body paragraphs, BR range `1.66--4.97×`
- 77 lines → 61 lines; body text from ~4 dense paragraphs + verbose contributions to 4 tight paragraphs + concise contributions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_step6_intro_20260523T025141"
}
```

</details>

---

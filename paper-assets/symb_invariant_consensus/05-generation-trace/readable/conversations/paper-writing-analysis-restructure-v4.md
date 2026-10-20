# paper writing analysis restructure v4

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_analysis_restructure_v4_20260523T043430.jsonl`
- **Structured JSON:** [`54e87505195690cccc29.json`](../../sessions/54/54e87505195690cccc29.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-23T04:40:32.904090+00:00_

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
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T04:40:32.904693+00:00_

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
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T04:40:32.904955+00:00_

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
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T04:40:32.905232+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting. This vacuity is $\alpha$-insensitive: agreement $\geq$99\% across $\alpha \in \{0.1, \ldots, 0.9\}$ (Table~\ref{tab:alpha-ablation}).
8	The following result formalizes this degeneration.
9	
10	\medskip\noindent
11	\textbf{Proposition 1} \textit{(Symbolic Confirmation Bias is Structural).}\;%
12	Let $t_1, \ldots, t_K \overset{\mathrm{i.i.d.}}{\sim} P_M(\cdot \mid q)$ be reasoning traces from model $M$ on question $q$.
13	Assume:
14	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=2.5em,nosep]
15	\item Answers are trace-determined: $a_i = h(t_i)$.
16	\item Constraints are trace-determined: $c_i = f(t_i)$.
17	\end{enumerate}
18	Let $\hat{a} = \mathrm{mode}(a_1, \ldots, a_K)$, $n_a = |\{i : a_i = a\}|$, and $Y$ the ground truth. Then:
19	\begin{enumerate}[label=\textit{(\roman*)},leftmargin=1.8em,itemsep=2pt,topsep=3pt]
20	\item \textit{Voting degeneration.}\;
21	Under source attribution (Eq.~\ref{eq:score}), the constraint score reduces to the majority-vote count: $\operatorname{score}(a) = n_a$.
22	When $|\{a : n_a > 0\}| \geq 2$, the bias ratio satisfies $\mathrm{BR} \triangleq n_{\hat{a}} \big/ \max_{a' \neq \hat{a}} n_{a'} \geq 1$.
23	
24	\item \textit{Information ceiling.}\;
25	$I(C_{1:K};\, Y) \leq I(T_{1:K};\, Y)$ and $I(C_{1:K
…[truncated 12544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T04:40:32.905574+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
  "old_string": "(Table~\\ref{tab:alpha-ablation}).\nThe following result formalizes this degeneration.\n\n\\medskip\\noindent\n\\textbf{Proposition 1} \\textit{(Symbolic Confirmation Bias is Structural).}\\;%\nLet $t_1, \\ldots, t_K \\overset{\\mathrm{i.i.d.}}{\\sim} P_M(\\cdot \\mid q)$ be reasoning traces from model $M$ on question $q$.\nAssume:\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=2.5em,nosep]\n\\item Answers are trace-determined: $a_i = h(t_i)$.\n\\item Constraints are trace-determined: $c_i = f(t_i)$.\n\\end{enumerate}\nLet $\\hat{a} = \\mathrm{mode}(a_1, \\ldots, a_K)$, $n_a = |\\{i : a_i = a\\}|$, and $Y$ the ground truth. Then:\n\\begin{enumerate}[label=\\textit{(\\roman*)},leftmargin=1.8em,itemsep=2pt,topsep=3pt]\n\\item \\textit{Voting degeneration.}\\;\nUnder source attribution (Eq.~\\ref{eq:score}), the constraint score reduces to the majority-vote count: $\\operatorname{score}(a) = n_a$.\nWhen $|\\{a : n_a > 0\\}| \\geq 2$, the bias ratio satisfies $\\mathrm{BR} \\triangleq n_{\\hat{a}} \\big/ \\max_{a' \\neq \\hat{a}} n_{a'} \\geq 1$.\n\n\\item \\textit{Information ceiling.}\\;\n$I(C_{1:K};\\, Y) \\leq I(T_{1:K};\\, Y)$ and $I(C_{1:K};\\, Y \\mid A_{1:K}) \\leq I(T_{1:K};\\, Y \\mid A_{1:K})$:\nself-extracted constraints cannot carry more information about $Y$ than the source traces, even beyond what the answers already encode.\n\\end{enumerate}\n\\noindent\nBoth bounds hold for \\emph{any} model $M$, task $q$, and extraction function $f$.\n\n\\medskip\n\\textit{Proof.}\\;%\n\\textit{(i)}\\; By definition, $\\operatorname{score}(a) = \\sum_{i=1}^K \\mathbf{1}[a_i = a] = n_a$, maximized at $\\hat{a}$, so $\\mathrm{BR} \\geq 1$.\n\\textit{(ii)}\\; $c_i = f(t_i)$ makes $C_{1:K}$ a deterministic function of $T_{1:K}$, so $Y \\mathop{\\text{---}} T_{1:K} \\mathop{\\text{---}} C_{1:K}$ forms a Markov chain and the data processing inequality gives $I(C_{1:K}; Y) \\leq I(T_{1:K}; Y)$.\nThe conditional bound follows identically: $c_i = f(t_i)$ holds unconditionally, so the Markov property and DPI apply within each stratum $\\{A_{1:K} = \\mathbf{a}\\}$.\\hfill$\\square$\n\n\\medskip\\noindent\nEach constraint is a downstream product of a trace that simultaneously determines an answer; constraint-based aggregation therefore cannot escape the distributional bias of the answer vote.\nNeither bound depends on model capability, task difficulty, or extraction quality. The bias is a structural artifact of the self-extraction pipeline.\n\n\\medskip\\noindent\n\\textbf{Remark.}\\;%\nPart~\\textit{(i)} relies on source attribution (Eq.~\\ref{eq:score}), the mechanism used by SICA.\nUnder \\emph{semantic} evaluation (checking whether $c_i$ is logically consistent with answer $a$ directly), $\\mathrm{BR} \\geq 1$ additionally requires \\emph{answer alignment}: $P(c_i \\text{ supports } a_i) \\geq P(c_i \\text{ supports } a')$ for $a' \\neq a_i$.\nThis property is structurally motivated (the reasoning chain producing $a_i$ generates intermediate steps aligned with $a_i$) and is empirically validated across all nine model--task conditions ($\\mathrm{BR} \\in [1.66,\\, 4.97]$; Table~\\ref{tab:frontier-scb}), but is not a mathematical necessity of self-extraction alone; it could fail if $f$ systematically extracted premises that contradict their source trace's conclusion.\nUnder the degeneration condition (Eq.~\\ref{eq:degenerate}), full SICA scoring with weights $w_c$ and penalty $\\alpha$ reduces to trace counting, and the count-ratio BR in Part~\\textit{(i)} specializes to the general definition (Eq.~\\ref{eq:mirage}).\nThis condition holds on 94.4\\% of problems (Table~\\ref{tab:ablation}), so the proposition's conclusions extend to the complete scoring function in practice.\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}[\n  node distance=0.8cm,\n  nd/.style={rectangle, rounded corners=2pt, draw=black!50,\n             fill=gray!6, minimum height=5.5mm, minimum width=8mm,\n             font=\\small},\n  bn/.style={nd, fill=red!10, draw=red!50, line width=0.7pt},\n  ex/.style={nd, draw=gray!50, densely dashed, fill=white},\n  >=Stealth,\n  base/.style={->, semithick, black!50},\n  leak/.style={->, line width=0.85pt, red!50},\n  sub/.style={font=\\scriptsize, text=gray!55},\n]\n\\node[nd]             (M) {$M$};\n\\node[nd, right=of M] (T) {$T$};\n\\node[bn, right=of T] (A) {$A$};\n\\node[nd, right=of A] (C) {$C$};\n\\node[nd, right=of C] (S) {$S$};\n\\node[ex, above=0.65cm of A] (Y) {$Y$};\n\n\\node[sub, below=0.5mm of M] {Model};\n\\node[sub, below=0.5mm of T] {Trace};\n\\node[sub, below=0.5mm of A] {Answer};\n\\node[sub, below=0.5mm of C] {Constr.};\n\\node[sub, below=0.5mm of S] {SICA};\n\\node[sub, above=0.5mm of Y] {Truth};\n\n\\draw[base] (M) -- (T);\n\\draw[leak] (T) -- (A);\n\\draw[leak] (A) -- (C);\n\\draw[base] (C) -- (S);\n\\draw[base, bend right=22] (T) to (C);\n\n\\draw[densely dashed, gray!30, shorten >=1pt, shorten <=1pt] (Y) -- (A);\n\n\\node[font=\\tiny, text=red!45, fill=white, inner sep=0.5pt]\n  at ($(A)!0.5!(C) + (0, 0.27)$) {\\textit{bottleneck}};\n\n\\node[draw=gray!30, rounded corners=1.5pt, fill=white,\n      inner sep=2.5pt, font=\\scriptsize, text=gray!50,\n      right=0.2cm of Y]\n  {$C \\!\\perp\\! Y \\mid A$};\n\\end{tikzpicture}\n\\caption{Causal DAG of the self-extraction pipeline. All information about ground truth $Y$ reaching constraints $C$ is mediated by answer $A$ ($C \\perp Y \\mid A$; Proposition~1, Part~\\textit{ii}), making self-verification inherently answer-biased.}\n\\label{fig:causal-dag}\n\\end{figure}\n\n\\looseness=-1 Empirically, confirmation bias extends beyond incorrect instances.",
  "new_string": "(Table~\\ref{tab:alpha-ablation}).\n\n\\looseness=-1 Empirically, confirmation bias extends beyond incorrect instances."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
    "old_string": "(Table~\\ref{tab:alpha-ablation}).\nThe following result formalizes this degeneration.\n\n\\medskip\\noindent\n\\textbf{Proposition 1} \\textit{(Symbolic Confirmation Bias is Structural).}\\;%\nLet $t_1, \\ldots, t_K \\overset{\\mathrm{i.i.d.}}{\\sim} P_M(\\cdot \\mid q)$ be reasoning traces from model $M$ on question $q$.\nAssume:\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=2.5em,nosep]\n\\item Answers are trace-determined: $a_i = h(t_i)$.\n\\item Constraints are trace-determined: $c_i = f(t_i)$.\n\\end{enumerate}\nLet $\\hat{a} = \\mathrm{mode}(a_1, \\ldots, a_K)$, $n_a = |\\{i : a_i = a\\}|$, and $Y$ the ground truth. Then:\n\\begin{enumerate}[label=\\textit{(\\roman*)},leftmargin=1.8em,itemsep=2pt,topsep=3pt]\n\\item \\textit{Voting degeneration.}\\;\nUnder source attribution (Eq.~\\ref{eq:score}), the constraint score reduces to the majority-vote count: $\\operatorname{score}(a) = n_a$.\nWhen $|\\{a : n_a > 0\\}| \\geq 2$, the bias ratio satisfies $\\mathrm{BR} \\triangleq n_{\\hat{a}} \\big/ \\max_{a' \\neq \\hat{a}} n_{a'} \\geq 1$.\n\n\\item \\textit{Information ceiling.}\\;\n$I(C_{1:K};\\, Y) \\leq I(T_{1:K};\\, Y)$ and $I(C_{1:K};\\, Y \\mid A_{1:K}) \\leq I(T_{1:K};\\, Y \\mid A_{1:K})$:\nself-extracted constraints cannot carry more information about $Y$ than the source traces, even beyond what the answers already encode.\n\\end{enumerate}\n\\noindent\nBoth bounds hold for \\emph{any} model $M$, task $q$, and extraction function $f$.\n\n\\medskip\n\\textit{Proof.}\\;%\n\\textit{(i)}\\; By definition, $\\operatorname{score}(a) = \\sum_{i=1}^K \\mathbf{1}[a_i = a] = n_a$, maximized at $\\hat{a}$, so $\\mathrm{BR} \\geq 1$.\n\\textit{(ii)}\\; $c_i = f(t_i)$ makes $C_{1:K}$ a deterministic function of $T_{1:K}$, so $Y \\mathop{\\text{---}} T_{1:K} \\mathop{\\text{---}} C_{1:K}$ forms a Markov chain and the data processing inequality gives $I(C_{1:K}; Y) \\leq I(T_{1:K}; Y)$.\nThe conditional bound follows identically: $c_i = f(t_i)$ holds unconditionally, so the Markov property and DPI apply within each stratum $\\{A_{1:K} = \\mathbf{a}\\}$.\\hfill$\\square$\n\n\\medskip\\noindent\nEach constraint is a downstream product of a trace that simultaneously determines an answer; constraint-based aggregation therefore cannot escape the distributional bias of the answer vote.\nNeither bound depends on model capability, task difficulty, or extraction quality. The bias is a structural artifact of the self-extraction pipeline.\n\n\\medskip\\noindent\n\\textbf{Remark.}\\;%\nPart~\\textit{(i)} relies on source attribution (Eq.~\\ref{eq:score}), the mechanism used by SICA.\nUnder \\emph{semantic} evaluation (checking whether $c_i$ is logically consistent with answer $a$ directly), $\\mathrm{BR} \\geq 1$ additionally requires \\emph{answer alignment}: $P(c_i \\text{ supports } a_i) \\geq P(c_i \\text{ supports } a')$ for $a' \\neq a_i$.\nThis property is structurally motivated (the reasoning chain producing $a_i$ generates intermediate steps aligned with $a_i$) and is empirically validated across all nine model--task conditions ($\\mathrm{BR} \\in [1.66,\\, 4.97]$; Table~\\ref{tab:frontier-scb}), but is not a mathematical necessity of self-extraction alone; it could fail if $f$ systematically extracted premises that contradict their source trace's conclusion.\nUnder the degeneration condition (Eq.~\\ref{eq:degenerate}), full SICA scoring with weights $w_c$ and penalty $\\alpha$ reduces to trace counting, and the count-ratio BR in Part~\\textit{(i)} specializes to the general definition (Eq.~\\ref{eq:mirage}).\nThis condition holds on 94.4\\% of problems (Table~\\ref{tab:ablation}), so the proposition's conclusions extend to the complete scoring function in practice.\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}[\n  node distance=0.8cm,\n  nd/.style={rectangle, rounded corners=2pt, draw=black!50,\n             fill=gray!6, minimum height=5.5mm, minimum width=8mm,\n             font=\\small},\n  bn/.style={nd, fill=red!10, draw=red!50, line width=0.7pt},\n  ex/.style={nd, draw=gray!50, densely dashed, fill=white},\n  >=Stealth,\n  base/.style={->, semithick, black!50},\n  leak/.style={->, line width=0.85pt, red!50},\n  sub/.style={font=\\scriptsize, text=gray!55},\n]\n\\node[nd]             (M) {$M$};\n\\node[nd, right=of M] (T) {$T$};\n\\node[bn, right=of T] (A) {$A$};\n\\node[nd, right=of A] (C) {$C$};\n\\node[nd, right=of C] (S) {$S$};\n\\node[ex, above=0.65cm of A] (Y) {$Y$};\n\n\\node[sub, below=0.5mm of M] {Model};\n\\node[sub, below=0.5mm of T] {Trace};\n\\node[sub, below=0.5mm of A] {Answer};\n\\node[sub, below=0.5mm of C] {Constr.};\n\\node[sub, below=0.5mm of S] {SICA};\n\\node[sub, above=0.5mm of Y] {Truth};\n\n\\draw[base] (M) -- (T);\n\\draw[leak] (T) -- (A);\n\\draw[leak] (A) -- (C);\n\\draw[base] (C) -- (S);\n\\draw[base, bend right=22] (T) to (C);\n\n\\draw[densely dashed, gray!30, shorten >=1pt, shorten <=1pt] (Y) -- (A);\n\n\\node[font=\\tiny, text=red!45, fill=white, inner sep=0.5pt]\n  at ($(A)!0.5!(C) + (0, 0.27)$) {\\textit{bottleneck}};\n\n\\node[draw=gray!30, rounded corners=1.5pt, fill=white,\n      inner sep=2.5pt, font=\\scriptsize, text=gray!50,\n      right=0.2cm of Y]\n  {$C \\!\\perp\\! Y \\mid A$};\n\\end{tikzpicture}\n\\caption{Causal DAG of the self-extraction pipeline. All information about ground truth $Y$ reaching constraints $C$ is mediated by answer $A$ ($C \\perp Y \\mid A$; Proposition~1, Part~\\textit{ii}), making self-verification inherently answer-biased.}\n\\label{fig:causal-dag}\n\\end{figure}\n\n\\looseness=-1 Empirically, confirmation bias extends beyond incorrect instances.",
    "new_string": "(Table~\\ref{tab:alpha-ablation}).\n\n\\looseness=-1 Empirically, confirmation bias extends beyond incorrect instances."
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T04:40:32.905941+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T04:40:32.906165+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
  "old_string": "Appendix~\\ref{app:cil}).\n\n\\subsection{Why Remediation Fails}",
  "new_string": "Appendix~\\ref{app:cil}).\n\n\\looseness=-1 These patterns---universal BR $> 1$, structural equivalence to trace-count distributions, and process-level correlation exceeding answer-level agreement---follow from a structural property of self-extraction pipelines.\n\n\\medskip\\noindent\n\\textbf{Proposition 1} \\textit{(Symbolic Confirmation Bias is Structural).}\\;%\nLet $t_1, \\ldots, t_K \\overset{\\mathrm{i.i.d.}}{\\sim} P_M(\\cdot \\mid q)$ be reasoning traces from model $M$ on question $q$.\nAssume:\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=2.5em,nosep]\n\\item Answers are trace-determined: $a_i = h(t_i)$.\n\\item Constraints are trace-determined: $c_i = f(t_i)$.\n\\end{enumerate}\nLet $\\hat{a} = \\mathrm{mode}(a_1, \\ldots, a_K)$, $n_a = |\\{i : a_i = a\\}|$, and $Y$ the ground truth. Then:\n\\begin{enumerate}[label=\\textit{(\\roman*)},leftmargin=1.8em,itemsep=2pt,topsep=3pt]\n\\item \\textit{Voting degeneration.}\\;\nUnder source attribution (Eq.~\\ref{eq:score}), the constraint score reduces to the majority-vote count: $\\operatorname{score}(a) = n_a$.\nWhen $|\\{a : n_a > 0\\}| \\geq 2$, the bias ratio satisfies $\\mathrm{BR} \\triangleq n_{\\hat{a}} \\big/ \\max_{a' \\neq \\hat{a}} n_{a'} \\geq 1$.\n\n\\item \\textit{Information ceiling.}\\;\n$I(C_{1:K};\\, Y) \\leq I(T_{1:K};\\, Y)$ and $I(C_{1:K};\\, Y \\mid A_{1:K}) \\leq I(T_{1:K};\\, Y \\mid A_{1:K})$:\nself-extracted constraints cannot carry more information about $Y$ than the source traces, even beyond what the answers already encode.\n\\end{enumerate}\n\\noindent\nBoth bounds hold for \\emph{any} model $M$, task $q$, and extraction function $f$.\n\n\\medskip\n\\textit{Proof.}\\;%\n\\textit{(i)}\\; By definition, $\\operatorname{score}(a) = \\sum_{i=1}^K \\mathbf{1}[a_i = a] = n_a$, maximized at $\\hat{a}$, so $\\mathrm{BR} \\geq 1$.\n\\textit{(ii)}\\; $c_i = f(t_i)$ makes $C_{1:K}$ a deterministic function of $T_{1:K}$, so $Y \\mathop{\\text{---}} T_{1:K} \\mathop{\\text{---}} C_{1:K}$ forms a Markov chain and the data processing inequality gives $I(C_{1:K}; Y) \\leq I(T_{1:K}; Y)$.\nThe conditional bound follows identically: $c_i = f(t_i)$ holds unconditionally, so the Markov property and DPI apply within each stratum $\\{A_{1:K} = \\mathbf{a}\\}$.\\hfill$\\square$\n\n\\medskip\\noindent\nEach constraint is a downstream product of a trace that simultaneously determines an answer; constraint-based aggregation therefore cannot escape the distributional bias of the answer vote.\nNeither bound depends on model capability, task difficulty, or extraction quality. The bias is a structural artifact of the self-extraction pipeline.\n\n\\medskip\\noindent\n\\textbf{Remark.}\\;%\nPart~\\textit{(i)} relies on source attribution (Eq.~\\ref{eq:score}), the mechanism used by SICA.\nUnder \\emph{semantic} evaluation (checking whether $c_i$ is logically consistent with answer $a$ directly), $\\mathrm{BR} \\geq 1$ additionally requires \\emph{answer alignment}: $P(c_i \\text{ supports } a_i) \\geq P(c_i \\text{ supports } a')$ for $a' \\neq a_i$.\nThis property is structurally motivated (the reasoning chain producing $a_i$ generates intermediate steps aligned with $a_i$) and is empirically validated across all nine model--task conditions ($\\mathrm{BR} \\in [1.66,\\, 4.97]$; Table~\\ref{tab:frontier-scb}), but is not a mathematical necessity of self-extraction alone; it could fail if $f$ systematically extracted premises that contradict their source trace's conclusion.\n\nUnder SICA's source attribution (Eq.~\\ref{eq:score}), Proposition~1\\textit{(i)} implies $\\mathrm{BR} \\geq 1$ deterministically for every problem; the empirical BR (Eq.~\\ref{eq:mirage}), which evaluates semantic support across incorrect problems, consistently exceeds this structural bound ($1.66\\times$--$4.97\\times$; Table~\\ref{tab:frontier-scb}).\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}[\n  node distance=0.8cm,\n  nd/.style={rectangle, rounded corners=2pt, draw=black!50,\n             fill=gray!6, minimum height=5.5mm, minimum width=8mm,\n             font=\\small},\n  bn/.style={nd, fill=red!10, draw=red!50, line width=0.7pt},\n  ex/.style={nd, draw=gray!50, densely dashed, fill=white},\n  >=Stealth,\n  base/.style={->, semithick, black!50},\n  leak/.style={->, line width=0.85pt, red!50},\n  sub/.style={font=\\scriptsize, text=gray!55},\n]\n\\node[nd]             (M) {$M$};\n\\node[nd, right=of M] (T) {$T$};\n\\node[bn, right=of T] (A) {$A$};\n\\node[nd, right=of A] (C) {$C$};\n\\node[nd, right=of C] (S) {$S$};\n\\node[ex, above=0.65cm of A] (Y) {$Y$};\n\n\\node[sub, below=0.5mm of M] {Model};\n\\node[sub, below=0.5mm of T] {Trace};\n\\node[sub, below=0.5mm of A] {Answer};\n\\node[sub, below=0.5mm of C] {Constr.};\n\\node[sub, below=0.5mm of S] {SICA};\n\\node[sub, above=0.5mm of Y] {Truth};\n\n\\draw[base] (M) -- (T);\n\\draw[leak] (T) -- (A);\n\\draw[leak] (A) -- (C);\n\\draw[base] (C) -- (S);\n\\draw[base, bend right=22] (T) to (C);\n\n\\draw[densely dashed, gray!30, shorten >=1pt, shorten <=1pt] (Y) -- (A);\n\n\\node[font=\\tiny, text=red!45, fill=white, inner sep=0.5pt]\n  at ($(A)!0.5!(C) + (0, 0.27)$) {\\textit{bottleneck}};\n\n\\node[draw=gray!30, rounded corners=1.5pt, fill=white,\n      inner sep=2.5pt, font=\\scriptsize, text=gray!50,\n      right=0.2cm of Y]\n  {$C \\!\\perp\\! Y \\mid A$};\n\\end{tikzpicture}\n\\caption{Causal DAG of the self-extraction pipeline. All information about ground truth $Y$ reaching constraints $C$ is mediated by answer $A$; Proposition~1\\textit{(ii)} formalizes this as an information ceiling via the data processing inequality.}\n\\label{fig:causal-dag}\n\\end{figure}\n\n\\looseness=-1 Since the bias holds for any model, task, and extraction function $f$, training-free remediation strategies face a structural limitation: methods that preserve extraction accuracy necessarily inherit the model's distributional prior.\n\n\\subsection{Why Remediation Fails}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
    "old_string": "Appendix~\\ref{app:cil}).\n\n\\subsection{Why Remediation Fails}",
    "new_string": "Appendix~\\ref{app:cil}).\n\n\\looseness=-1 These patterns---universal BR $> 1$, structural equivalence to trace-count distributions, and process-level correlation exceeding answer-level agreement---follow from a structural property of self-extraction pipelines.\n\n\\medskip\\noindent\n\\textbf{Proposition 1} \\textit{(Symbolic Confirmation Bias is Structural).}\\;%\nLet $t_1, \\ldots, t_K \\overset{\\mathrm{i.i.d.}}{\\sim} P_M(\\cdot \\mid q)$ be reasoning traces from model $M$ on question $q$.\nAssume:\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=2.5em,nosep]\n\\item Answers are trace-determined: $a_i = h(t_i)$.\n\\item Constraints are trace-determined: $c_i = f(t_i)$.\n\\end{enumerate}\nLet $\\hat{a} = \\mathrm{mode}(a_1, \\ldots, a_K)$, $n_a = |\\{i : a_i = a\\}|$, and $Y$ the ground truth. Then:\n\\begin{enumerate}[label=\\textit{(\\roman*)},leftmargin=1.8em,itemsep=2pt,topsep=3pt]\n\\item \\textit{Voting degeneration.}\\;\nUnder source attribution (Eq.~\\ref{eq:score}), the constraint score reduces to the majority-vote count: $\\operatorname{score}(a) = n_a$.\nWhen $|\\{a : n_a > 0\\}| \\geq 2$, the bias ratio satisfies $\\mathrm{BR} \\triangleq n_{\\hat{a}} \\big/ \\max_{a' \\neq \\hat{a}} n_{a'} \\geq 1$.\n\n\\item \\textit{Information ceiling.}\\;\n$I(C_{1:K};\\, Y) \\leq I(T_{1:K};\\, Y)$ and $I(C_{1:K};\\, Y \\mid A_{1:K}) \\leq I(T_{1:K};\\, Y \\mid A_{1:K})$:\nself-extracted constraints cannot carry more information about $Y$ than the source traces, even beyond what the answers already encode.\n\\end{enumerate}\n\\noindent\nBoth bounds hold for \\emph{any} model $M$, task $q$, and extraction function $f$.\n\n\\medskip\n\\textit{Proof.}\\;%\n\\textit{(i)}\\; By definition, $\\operatorname{score}(a) = \\sum_{i=1}^K \\mathbf{1}[a_i = a] = n_a$, maximized at $\\hat{a}$, so $\\mathrm{BR} \\geq 1$.\n\\textit{(ii)}\\; $c_i = f(t_i)$ makes $C_{1:K}$ a deterministic function of $T_{1:K}$, so $Y \\mathop{\\text{---}} T_{1:K} \\mathop{\\text{---}} C_{1:K}$ forms a Markov chain and the data processing inequality gives $I(C_{1:K}; Y) \\leq I(T_{1:K}; Y)$.\nThe conditional bound follows identically: $c_i = f(t_i)$ holds unconditionally, so the Markov property and DPI apply within each stratum $\\{A_{1:K} = \\mathbf{a}\\}$.\\hfill$\\square$\n\n\\medskip\\noindent\nEach constraint is a downstream product of a trace that simultaneously determines an answer; constraint-based aggregation therefore cannot escape the distributional bias of the answer vote.\nNeither bound depends on model capability, task difficulty, or extraction quality. The bias is a structural artifact of the self-extraction pipeline.\n\n\\medskip\\noindent\n\\textbf{Remark.}\\;%\nPart~\\textit{(i)} relies on source attribution (Eq.~\\ref{eq:score}), the mechanism used by SICA.\nUnder \\emph{semantic} evaluation (checking whether $c_i$ is logically consistent with answer $a$ directly), $\\mathrm{BR} \\geq 1$ additionally requires \\emph{answer alignment}: $P(c_i \\text{ supports } a_i) \\geq P(c_i \\text{ supports } a')$ for $a' \\neq a_i$.\nThis property is structurally motivated (the reasoning chain producing $a_i$ generates intermediate steps aligned with $a_i$) and is empirically validated across all nine model--task conditions ($\\mathrm{BR} \\in [1.66,\\, 4.97]$; Table~\\ref{tab:frontier-scb}), but is not a mathematical necessity of self-extraction alone; it could fail if $f$ systematically extracted premises that contradict their source trace's conclusion.\n\nUnder SICA's source attribution (Eq.~\\ref{eq:score}), Proposition~1\\textit{(i)} implies $\\mathrm{BR} \\geq 1$ deterministically for every problem; the empirical BR (Eq.~\\ref{eq:mirage}), which evaluates semantic support across incorrect problems, consistently exceeds this structural bound ($1.66\\times$--$4.97\\times$; Table~\\ref{tab:frontier-scb}).\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}[\n  node distance=0.8cm,\n  nd/.style={rectangle, rounded corners=2pt, draw=black!50,\n             fill=gray!6, minimum height=5.5mm, minimum width=8mm,\n             font=\\small},\n  bn/.style={nd, fill=red!10, draw=red!50, line width=0.7pt},\n  ex/.style={nd, draw=gray!50, densely dashed, fill=white},\n  >=Stealth,\n  base/.style={->, semithick, black!50},\n  leak/.style={->, line width=0.85pt, red!50},\n  sub/.style={font=\\scriptsize, text=gray!55},\n]\n\\node[nd]             (M) {$M$};\n\\node[nd, right=of M] (T) {$T$};\n\\node[bn, right=of T] (A) {$A$};\n\\node[nd, right=of A] (C) {$C$};\n\\node[nd, right=of C] (S) {$S$};\n\\node[ex, above=0.65cm of A] (Y) {$Y$};\n\n\\node[sub, below=0.5mm of M] {Model};\n\\node[sub, below=0.5mm of T] {Trace};\n\\node[sub, below=0.5mm of A] {Answer};\n\\node[sub, below=0.5mm of C] {Constr.};\n\\node[sub, below=0.5mm of S] {SICA};\n\\node[sub, above=0.5mm of Y] {Truth};\n\n\\draw[base] (M) -- (T);\n\\draw[leak] (T) -- (A);\n\\draw[leak] (A) -- (C);\n\\draw[base] (C) -- (S);\n\\draw[base, bend right=22] (T) to (C);\n\n\\draw[densely dashed, gray!30, shorten >=1pt, shorten <=1pt] (Y) -- (A);\n\n\\node[font=\\tiny, text=red!45, fill=white, inner sep=0.5pt]\n  at ($(A)!0.5!(C) + (0, 0.27)$) {\\textit{bottleneck}};\n\n\\node[draw=gray!30, rounded corners=1.5pt, fill=white,\n      inner sep=2.5pt, font=\\scriptsize, text=gray!50,\n      right=0.2cm of Y]\n  {$C \\!\\perp\\! Y \\mid A$};\n\\end{tikzpicture}\n\\caption{Causal DAG of the self-extraction pipeline. All information about ground truth $Y$ reaching constraints $C$ is mediated by answer $A$; Proposition~1\\textit{(ii)} formalizes this as an information ceiling via the data processing inequality.}\n\\label{fig:causal-dag}\n\\end{figure}\n\n\\looseness=-1 Since the bias holds for any model, task, and extraction function $f$, training-free remediation strategies face a structural limitation: methods that preserve extraction accuracy necessarily inherit the model's distributional prior.\n\n\\subsection{Why Remediation Fails}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T04:40:32.906445+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T04:40:32.906624+00:00_

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
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T04:40:32.906852+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting. This vacuity is $\alpha$-insensitive: agreement $\geq$99\% across $\alpha \in \{0.1, \ldots, 0.9\}$ (Table~\ref{tab:alpha-ablation}).
8	
9	\looseness=-1 Empirically, confirmation bias extends beyond incorrect instances. On problems where SC selects the correct answer, constraints still disproportionately support the majority ($\text{BR}_\text{correct}$ $1.29$--$3.64\times$ across all six tested conditions, with 5/6 showing $\text{BR}_\text{correct} \geq \text{BR}_\text{wrong}$), confirming that self-extracted constraints track distributional frequency rather than logical validity. A shuffle control further confirms the structural nature of this bias: randomizing constraint--answer associations while preserving per-trace counts yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($p > 0.7$), indicating that BR reflects the trace-count distribution rather than extraction-specific error.
10	
11	\looseness=-1 The pattern generalizes: $4.97\times$ (Mistral), $3.85\times$ (Qwen-14B), $2.88\times$ (LLaMA), all $> 1.0$ with 95\% bootstrap CIs (Table~\ref{tab:cross-model-bias}). Cross-model extraction confirms universality across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb}). BR $> 1$ further hold
…[truncated 12931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-23T04:40:32.907108+00:00_

验证通过，所有 6 项检查：

1. **§5.1 结构正确**：SCB 经验段 (L7) → BR_correct+shuffle (L9) → Cross-model (L11) → Table (L13-35) → Leakage (L37) → Process similarity (L39-40) → 过渡句 (L42) → Proposition (L44-79) → BR 桥接 (L81) → DAG (L83-129) → §5.2 桥接 (L131) → §5.2 (L133)
2. **Proposition 数学内容完整**：statement、proof、summary、remark 全部保留
3. **旧 bridge 句已删除**：`Under the degeneration condition...` 和 `This condition holds on 94.4%...` 均不存在
4. **新内容正确**：过渡句 (L42)、BR 桥接句 (L81)、新 caption (L127)、§5.2 桥接句 (L131)
5. **§5.2 (L133-150) 和 §5.3 (L152-158) 未修改**
6. **无 Unicode em-dash**：全文仅使用 `---`（LaTeX 三连字符）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_analysis_restructure_v4_20260523T043430"
}
```

</details>

---

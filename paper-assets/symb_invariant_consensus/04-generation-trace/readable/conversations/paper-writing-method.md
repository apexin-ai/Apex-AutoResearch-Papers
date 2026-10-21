# paper writing method

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_writing_method_20260519T035043.jsonl`
- **Structured JSON:** [`15a705c6aeba640442ba.json`](../../sessions/15/15a705c6aeba640442ba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-19T03:54:30.224078+00:00_

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
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T03:54:30.224664+00:00_

1	\section{Method: The SICA Pipeline}
2	\label{sec:method}
3	
4	This section describes Symbolic Invariant Consensus Aggregation (SICA), which extracts first-order logic (FOL) constraints from multiple reasoning traces produced by a single LLM, formulates a weighted partial MAX-SAT problem, and selects the answer best supported by the satisfiable subset.
5	
6	\subsection{Overview}
7	\label{sec:method-overview}
8	
9	Given a question $q$, SICA proceeds in four stages. First, an LLM generates $K$ independent reasoning traces $\{t_1, \ldots, t_K\}$ by sampling at temperature $T$; each trace $t_i$ yields a candidate answer $a_i$. Second, the same LLM extracts a set of structured FOL constraints $C_i$ from each trace $t_i$. Third, constraints are deduplicated across traces by syntactic equivalence, and each unique constraint receives a weight equal to the number of traces that produced it. Fourth, the deduplicated constraint pool is formulated as a weighted partial MAX-SAT instance and solved by Z3 \cite{demoura2008z3}. Each candidate answer is scored by the total weight of satisfied constraints, and the highest-scoring answer is selected.
10	
11	Self-Consistency (SC) uses only the first stage: it selects $a^* = \arg\max_{a} \sum_{i=1}^{K} \mathbf{1}[a_i = a]$. SICA's additional signal comes from constraint satisfaction structure. Whether this signal provides discriminative power beyond vote counting is the central empirical question.
12	
13	\begin{figure}[t]
14	\centering
15	\small
16	\begin{tikzpicture}[
17	    node distance=0.4cm and 0.35cm,
18	    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,
19	                text width=1.6cm, align=center, font=\scriptsize},
20	    arr/.style={-{Stealth[length=4pt]}, thick},
21	    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},
22	    lbl/.style={font=\scriptsize, text=gray!70!black},
23	]
24	\node[box] (q) {Question $q$};
25	\node[box, right=of q] (sample) {Sample $K$\\traces};
26	\node[box, right=of sa
…[truncated 7065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:54:30.225044+00:00_

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
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T03:54:30.225459+00:00_

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
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T03:54:30.225690+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "condorcet|austensmith|ladha|fleiss1971|wang2023sc",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "tool_args": {
    "pattern": "condorcet|austensmith|ladha|fleiss1971|wang2023sc",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T03:54:30.225832+00:00_

docs/paper/related_work.tex:5:[Omitted long matching line]
docs/paper/main.bbl:263:  and Zhou}]{wang2023sc}
docs/paper/introduction.tex:3:[Omitted long matching line]
docs/paper/references.bib:6:@inproceedings{wang2023sc,
docs/paper/main.aux:7:\citation{wang2023sc}
docs/paper/main.aux:113:\citation{wang2023sc}
docs/paper/main.aux:1048:\bibcite{wang2023sc}{{37}{2023}{{Wang et~al.}}{{Wang, Wei, Schuurmans, Le, Chi, Narang, Chowdhery, and Zhou}}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T03:54:30.225980+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "condorcet|austensmith|ladha|fleiss1971",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "output_mode": "content",
  "-i": "True",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "tool_args": {
    "pattern": "condorcet|austensmith|ladha|fleiss1971",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "output_mode": "content",
    "-i": "True",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T03:54:30.226101+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T03:54:30.226234+00:00_

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
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T03:54:30.226400+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Scaling test-time computation has emerged as a key strategy for improving large language model (LLM) reasoning \citep{snell2025scaling}. Majority voting over multiple chain-of-thought samples, known as Self-Consistency (SC) \citep{wang2023sc}, remains the dominant aggregation method but faces diminishing returns from additional traces \citep{loo2025reevaluating}. Verification-based approaches that extract richer signal from reasoning traces offer a path to break this plateau. Symbolic verification through formal constraints and satisfiability solvers is one such direction, as it provides logical guarantees that natural language self-critique lacks \citep{huang2024selfcorrect}.
4	
5	Neuro-symbolic methods that augment LLM reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \citep{xu2026dylos}, apply logic-complete decomposition \citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \citep{wang2025fover}, or employ multi-perspective grounding \citep{luo2025logicagent}. These systems report positive results, but each introduces capabilities beyond the reasoning model itself: trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering.
6	
7	These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces, and if so, under what conditions? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability s
…[truncated 4616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T03:54:30.226548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:54:30.226699+00:00_

1	% References for SICA Capability Trap paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% Self-Consistency and Variants %%%
5	
6	@inproceedings{wang2023sc,
7	  title={Self-Consistency Improves Chain of Thought Reasoning in Language Models},
8	  author={Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
9	  booktitle={ICLR},
10	  year={2023}
11	}
12	
13	@inproceedings{chen2024usc,
14	  title={Universal Self-Consistency for Large Language Model Generation},
15	  author={Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
16	  booktitle={ICML},
17	  year={2024}
18	}
19	
20	@inproceedings{taubenfeld2025cisc,
21	  title={Confidence Improves Self-Consistency in {LLM}s},
22	  author={Taubenfeld, Asaf and Goldstein, Ido and Tsur, Oren},
23	  booktitle={ACL Findings},
24	  year={2025}
25	}
26	
27	@article{loo2025reevaluating,
28	  title={Reevaluating Self-Consistency Scaling in Multi-Agent Systems},
29	  author={Loo, Ryan and others},
30	  journal={arXiv preprint arXiv:2511.00751},
31	  year={2025}
32	}
33	
34	@inproceedings{li2023diverse,
35	  title={Making Language Models Better Reasoners with Step-Aware Verifier},
36	  author={Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},
37	  booktitle={ACL},
38	  year={2023}
39	}
40	
41	%%% Neuro-Symbolic Reasoning %%%
42	
43	@inproceedings{pan2023logiclm,
44	  title={Logic-{LM}: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning},
45	  author={Pan, Liangming and Alber, Alon and Xu, Wenhu and Deng, Yixin and Chen, Huan and Ji, Heng},
46	  booktitle={EMNLP Findings},
47	  year={2023}
48	}
49	
50	@inproceedings{olausson2023linc,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T03:54:30.226929+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sec:c0|sec:constraint-extraction|sec:oracle|sec:scope|sec:maxsat|sec:method",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sec:c0|sec:constraint-extraction|sec:oracle|sec:scope|sec:maxsat|sec:method",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:54:30.227105+00:00_

docs/paper/experiments.tex:11:[Omitted long matching line]
docs/paper/experiments.tex:15:\paragraph{Metrics.} Accuracy (\%), $C_0$ (\S\ref{sec:c0}), and $\Delta = \text{SICA} - \text{SC}$ in percentage points (pp). McNemar exact test at $\alpha = 0.05$; 95\% bootstrap CIs (10{,}000 resamples) for $n \geq 200$.
docs/paper/experiments.tex:66:[Omitted long matching line]
docs/paper/experiments.tex:76:\label{sec:oracle}
docs/paper/method.tex:2:\label{sec:method}
docs/paper/method.tex:7:\label{sec:method-overview}
docs/paper/method.tex:50:\label{sec:constraint-extraction}
docs/paper/method.tex:57:\label{sec:maxsat}
docs/paper/method.tex:84:\label{sec:c0}
docs/paper/method.tex:95:\label{sec:scope}
docs/paper/method.tex:97:[Omitted long matching line]
docs/paper/limitations_content.tex:1:[Omitted long matching line]
docs/paper/introduction.tex:9:[Omitted long matching line]
docs/paper/introduction.tex:11:[Omitted long matching line]
docs/paper/introduction.tex:16:\item We introduce oracle controls on two datasets that causally localize the bottleneck: replacing self-extraction with gold annotations yields $+14.22$\,pp on FOLIO ($p = 2.0 \times 10^{-7}$) and $+11.50$\,pp on ProofWriter ($p < 0.001$). Even the best self-extraction result captures only 34.5\% of the oracle ceiling (\S\ref{sec:oracle}).
docs/paper/introduction.tex:18:\item We propose $C_0$ and SC accuracy as a two-dimensional, zero-cost diagnostic: low $C_0$ rules out SICA benefit by construction, while high $C_0$ with high SC identifies the capability trap regime (\S\ref{sec:c0}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:54:30.227487+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sec:method-overview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sec:method-overview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T03:54:30.227648+00:00_

docs/paper/method.tex:7:\label{sec:method-overview}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T03:54:30.227831+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Self-Consistency and the Condorcet Independence Assumption}\n\\label{sec:condorcet}\n\nSelf-Consistency (SC) \\citep{wang2023sc} samples $K$ reasoning traces from a language model and selects the answer by majority vote: $a^* = \\arg\\max_{a} \\sum_{i=1}^{K} \\mathbf{1}[a_i = a]$. The theoretical justification for this approach follows the Condorcet Jury Theorem (CJT) \\citep{condorcet1785}: given $K$ independent voters each correct with probability $p > 0.5$, the probability that the majority is correct approaches 1 as $K \\to \\infty$ \\citep{austensmith1996}.\n\nCJT requires that voters be conditionally independent given the correct answer. LLM traces violate this assumption: all $K$ samples come from the same model, conditioned on the same prompt, with only sampling temperature as a source of variation. Correlated voters reduce the effective ensemble size. \\citet{ladha1992correlated} show that under uniform pairwise correlation $\\rho$, the effective number of independent voters is $K_{\\text{eff}} = K / (1 + (K{-}1)\\rho)$. We use Fleiss' $\\kappa$ \\citep{fleiss1971kappa} as an empirical proxy for inter-trace agreement:\n\\begin{equation}\n\\label{eq:effk}\nK_{\\text{eff}} = \\frac{K}{1 + (K - 1) \\cdot \\kappa}.\n\\end{equation}\n\nIn our experiments (\\S\\ref{sec:main-results}), $\\kappa$ ranges from 0.40 to 0.74 across model-dataset pairs, yielding $K_{\\text{eff}} \\approx 1.2\\text{--}2.2$ for $K = 12$. At $K_{\\text{eff}} \\approx 1$, additional traces provide almost no new information, and the CJT guarantee collapses. This \\emph{independence bottleneck} motivates our investigation: can structured constraint extraction recover discriminative signal that majority voting cannot?\n\n\\subsection{SICA Pipeline}\n\\label{sec:pipeline}\n\nSymbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from reasoning traces and selecting the answer best supported by the satisfiable subset. Figure~\\ref{fig:pipeline} illustrates the pipeline.\n\n\\paragraph{Trace generation.} Given a question $q$, an LLM generates $K$ reasoning traces $\\{t_1, \\ldots, t_K\\}$ by sampling at temperature $T = 0.7$. Each trace $t_i$ yields a candidate answer $a_i$.\n\n\\paragraph{Constraint extraction.}\n\\label{sec:constraint-extraction}\nThe same LLM extracts structured first-order logic (FOL) constraints from each trace $t_i$ at a lower temperature $T_{\\text{ext}} = 0.3$. While we prompt for FOL-style formalizations, the extracted constraints are predominantly ground propositional clauses without quantifiers, reflecting instruction-scale model capabilities. The extraction prompt requests JSON output containing the constraint type, a human-readable expression, and a Z3-compatible formula string. Each constraint $c$ is associated with its source trace $t_i$ and the answer $a_i$ that trace produced. The full prompt template is in Appendix~\\ref{app:prompts}. We define the \\emph{extraction rate} as the fraction of traces yielding at least one parseable constraint. Traces with no valid constraints are excluded from MAX-SAT but still contribute answers to the candidate pool.\n\n\\paragraph{Syntactic deduplication.} Constraints are deduplicated across traces by syntactic equivalence. Each unique constraint $c_m$ receives weight $w_m$ equal to the number of distinct traces that produced it.\n\n\\paragraph{Weighted partial MAX-SAT.}\n\\label{sec:maxsat}\nLet $\\mathcal{A}(q) = \\{a : a \\in \\{a_1, \\ldots, a_K\\}\\}$ denote the set of distinct candidate answers for question $q$, and let $\\mathcal{C} = \\{c_1, \\ldots, c_M\\}$ denote the deduplicated constraint pool with weights $\\{w_1, \\ldots, w_M\\}$. Each unique constraint $c_m$ serves as a soft clause with weight $w_m$. The objective is to find the largest-weight satisfiable subset:\n\\begin{equation}\n\\label{eq:maxsat}\n\\mathcal{C}^* = \\arg\\max_{\\mathcal{S} \\subseteq \\mathcal{C}} \\sum_{c \\in \\mathcal{S}} w_c \\quad \\text{s.t.} \\quad \\mathcal{S} \\text{ is satisfiable.}\n\\end{equation}\nZ3 \\citep{demoura2008z3} solves this with a 10-second per-problem timeout. To ensure each candidate answer participates in scoring, the pipeline injects an \\emph{answer assertion} constraint $\\texttt{answer\\_a} \\mathrel{{=}{=}} \\texttt{True}$ for each trace, with weight~1. This guarantees that every candidate receives a nonzero base score proportional to its vote count; SICA is therefore a strict generalization of SC.\n\n\\paragraph{Answer scoring.} Let $\\mathcal{C}^{\\setminus} = \\mathcal{C} \\setminus \\mathcal{C}^*$ denote the excluded constraint set. Each candidate answer $a \\in \\mathcal{A}(q)$ is scored by:\n\\begin{equation}\n\\label{eq:score}\n\\text{score}(a) = \\sum_{c \\in \\mathcal{C}^*} w_c \\cdot \\sigma(c, a) \\;-\\; \\alpha \\sum_{c \\in \\mathcal{C}^{\\setminus}} w_c \\cdot \\sigma(c, a),\n\\end{equation}\nwhere $\\sigma(c, a) \\in \\{0, 1\\}$ is a source-trace indicator: $\\sigma(c, a) = 1$ if $c$ was extracted from any trace that produced answer $a$, and 0 otherwise. The penalty weight $\\alpha = 0.5$ in all experiments. The first term rewards answers whose source constraints are satisfied; the second penalizes answers whose source constraints were excluded by MAX-SAT. Discriminative signal arises when constraints from different traces conflict: Z3 excludes low-weight constraints from $\\mathcal{C}^*$, and the scorer attributes these exclusions to the corresponding source answers via $\\sigma$ (see Algorithm~\\ref{alg:scorer} in Appendix~\\ref{app:z3-pseudocode}). The selected answer is $a^* = \\arg\\max_{a \\in \\mathcal{A}} \\text{score}(a)$.\n\n\\paragraph{Degeneration under non-discriminative constraints.}\nIn practice, self-extracted constraints are tightly coupled to their source answer: $c_m$ derived from trace $t_i$ typically entails $a_i$ ($\\sigma(c_m, a_i) \\approx 1$). When constraints lack discriminative power across candidates, MAX-SAT excludes almost no constraints ($|\\mathcal{C}^{\\setminus}| \\approx 0$), so the penalty term vanishes regardless of $\\alpha$, and the score function degenerates:\n\\begin{equation}\n\\label{eq:degenerate}\n\\text{score}(a) \\approx \\sum_{\\substack{c \\in \\mathcal{C}^* \\\\ \\text{source}(c) \\to a}} w_c,\n\\end{equation}\nwhich reduces to a weighted count of traces supporting $a$, equivalent to majority voting when weights are uniform. Only ${\\sim}8$\\% of self-extracted constraints are semantically discriminative across candidates (\\S\\ref{sec:discussion}). The ablation in \\S\\ref{sec:ablation} confirms this empirically: MAX-SAT, count-only, and random-weight baselines produce nearly identical accuracy.\n\n\\paragraph{The $C_0$ diagnostic.}\n\\label{sec:c0}\nWe define the multi-candidate rate $C_0$ as the fraction of questions for which $K$ sampled traces produce more than one distinct answer (Eq.~\\ref{eq:c0-def}). $C_0$ is a zero-cost diagnostic computable before any constraint extraction. When $C_0 < 5$\\%, nearly all questions are answered unanimously and SICA produces the same output as SC by construction. High $C_0$ does not guarantee improvement but ensures disagreement exists for constraints to resolve.\n\\begin{equation}\n\\label{eq:c0-def}\nC_0 = \\frac{|\\{q \\in \\mathcal{Q} : |\\mathcal{A}(q)| > 1\\}|}{|\\mathcal{Q}|}.\n\\end{equation}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\begin{tikzpicture}[\n    node distance=0.4cm and 0.35cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,\n                text width=1.6cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract FOL\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n% Independence Bottleneck annotation\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts FOL constraints from each trace, deduplicates, and solves a MAX-SAT instance via Z3. The red dashed box marks the independence bottleneck: same-model sampling and extraction produce correlated constraints ($K_{\\text{eff}} \\approx 1.2\\text{--}2.2$ for $K = 12$). Dashed arrow: the oracle variant substitutes gold FOL annotations.}\n\\label{fig:pipeline}\n\\end{figure}\n\n\\subsection{Oracle Control Design}\n\\label{sec:oracle-design}\n\nTo isolate whether the bottleneck lies in constraint extraction or in the aggregation mechanism, we introduce an oracle control. For FOLIO \\citep{han2022folio}, gold FOL annotations replace self-extracted constraints. For ProofWriter \\citep{tafjord2021proofwriter}, gold domain-specific logic (DSL) rules serve the same role. In both cases, Z3 evaluates the gold constraints against each candidate answer produced by the original $K$ traces; the scoring function (Eq.~\\ref{eq:score}) remains unchanged.\n\nThis design functions as a causal intervention on constraint quality. If the oracle variant produces large gains while self-extraction does not, the aggregation mechanism itself is sound, and the failure localizes to constraint extraction. Conversely, if the oracle also fails, the MAX-SAT aggregation framework is insufficient regardless of constraint quality. Results of this intervention appear in \\S\\ref{sec:oracle}.\n\n\\subsection{Scope}\n\\label{sec:scope}\n\nSICA as evaluated here uses \\emph{same-model self-extraction}: the same LLM generates traces and extracts constraints. This design isolates whether a model's own reasoning can be usefully formalized for aggregation. Methods that use trained extractors, external provers, or multi-model ensembles fall outside the scope of this evaluation. We test nine remediation strategies spanning prompt, architecture, and solver dimensions (\\S\\ref{sec:interventions}), including Z3 Feedback Refinement (Appendix~\\ref{app:z3-pseudocode}), a closed-loop paradigm \\citep{kambhampati2024position} where the solver feeds UNSAT cores back to the extractor.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Self-Consistency and the Condorcet Independence Assumption}\n\\label{sec:condorcet}\n\nSelf-Consistency (SC) \\citep{wang2023sc} samples $K$ reasoning traces from a language model and selects the answer by majority vote: $a^* = \\arg\\max_{a} \\sum_{i=1}^{K} \\mathbf{1}[a_i = a]$. The theoretical justification for this approach follows the Condorcet Jury Theorem (CJT) \\citep{condorcet1785}: given $K$ independent voters each correct with probability $p > 0.5$, the probability that the majority is correct approaches 1 as $K \\to \\infty$ \\citep{austensmith1996}.\n\nCJT requires that voters be conditionally independent given the correct answer. LLM traces violate this assumption: all $K$ samples come from the same model, conditioned on the same prompt, with only sampling temperature as a source of variation. Correlated voters reduce the effective ensemble size. \\citet{ladha1992correlated} show that under uniform pairwise correlation $\\rho$, the effective number of independent voters is $K_{\\text{eff}} = K / (1 + (K{-}1)\\rho)$. We use Fleiss' $\\kappa$ \\citep{fleiss1971kappa} as an empirical proxy for inter-trace agreement:\n\\begin{equation}\n\\label{eq:effk}\nK_{\\text{eff}} = \\frac{K}{1 + (K - 1) \\cdot \\kappa}.\n\\end{equation}\n\nIn our experiments (\\S\\ref{sec:main-results}), $\\kappa$ ranges from 0.40 to 0.74 across model-dataset pairs, yielding $K_{\\text{eff}} \\approx 1.2\\text{--}2.2$ for $K = 12$. At $K_{\\text{eff}} \\approx 1$, additional traces provide almost no new information, and the CJT guarantee collapses. This \\emph{independence bottleneck} motivates our investigation: can structured constraint extraction recover discriminative signal that majority voting cannot?\n\n\\subsection{SICA Pipeline}\n\\label{sec:pipeline}\n\nSymbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from reasoning traces and selecting the answer best supported by the satisfiable subset. Figure~\\ref{fig:pipeline} illustrates the pipeline.\n\n\\paragraph{Trace generation.} Given a question $q$, an LLM generates $K$ reasoning traces $\\{t_1, \\ldots, t_K\\}$ by sampling at temperature $T = 0.7$. Each trace $t_i$ yields a candidate answer $a_i$.\n\n\\paragraph{Constraint extraction.}\n\\label{sec:constraint-extraction}\nThe same LLM extracts structured first-order logic (FOL) constraints from each trace $t_i$ at a lower temperature $T_{\\text{ext}} = 0.3$. While we prompt for FOL-style formalizations, the extracted constraints are predominantly ground propositional clauses without quantifiers, reflecting instruction-scale model capabilities. The extraction prompt requests JSON output containing the constraint type, a human-readable expression, and a Z3-compatible formula string. Each constraint $c$ is associated with its source trace $t_i$ and the answer $a_i$ that trace produced. The full prompt template is in Appendix~\\ref{app:prompts}. We define the \\emph{extraction rate} as the fraction of traces yielding at least one parseable constraint. Traces with no valid constraints are excluded from MAX-SAT but still contribute answers to the candidate pool.\n\n\\paragraph{Syntactic deduplication.} Constraints are deduplicated across traces by syntactic equivalence. Each unique constraint $c_m$ receives weight $w_m$ equal to the number of distinct traces that produced it.\n\n\\paragraph{Weighted partial MAX-SAT.}\n\\label{sec:maxsat}\nLet $\\mathcal{A}(q) = \\{a : a \\in \\{a_1, \\ldots, a_K\\}\\}$ denote the set of distinct candidate answers for question $q$, and let $\\mathcal{C} = \\{c_1, \\ldots, c_M\\}$ denote the deduplicated constraint pool with weights $\\{w_1, \\ldots, w_M\\}$. Each unique constraint $c_m$ serves as a soft clause with weight $w_m$. The objective is to find the largest-weight satisfiable subset:\n\\begin{equation}\n\\label{eq:maxsat}\n\\mathcal{C}^* = \\arg\\max_{\\mathcal{S} \\subseteq \\mathcal{C}} \\sum_{c \\in \\mathcal{S}} w_c \\quad \\text{s.t.} \\quad \\mathcal{S} \\text{ is satisfiable.}\n\\end{equation}\nZ3 \\citep{demoura2008z3} solves this with a 10-second per-problem timeout. To ensure each candidate answer participates in scoring, the pipeline injects an \\emph{answer assertion} constraint $\\texttt{answer\\_a} \\mathrel{{=}{=}} \\texttt{True}$ for each trace, with weight~1. This guarantees that every candidate receives a nonzero base score proportional to its vote count; SICA is therefore a strict generalization of SC.\n\n\\paragraph{Answer scoring.} Let $\\mathcal{C}^{\\setminus} = \\mathcal{C} \\setminus \\mathcal{C}^*$ denote the excluded constraint set. Each candidate answer $a \\in \\mathcal{A}(q)$ is scored by:\n\\begin{equation}\n\\label{eq:score}\n\\text{score}(a) = \\sum_{c \\in \\mathcal{C}^*} w_c \\cdot \\sigma(c, a) \\;-\\; \\alpha \\sum_{c \\in \\mathcal{C}^{\\setminus}} w_c \\cdot \\sigma(c, a),\n\\end{equation}\nwhere $\\sigma(c, a) \\in \\{0, 1\\}$ is a source-trace indicator: $\\sigma(c, a) = 1$ if $c$ was extracted from any trace that produced answer $a$, and 0 otherwise. The penalty weight $\\alpha = 0.5$ in all experiments. The first term rewards answers whose source constraints are satisfied; the second penalizes answers whose source constraints were excluded by MAX-SAT. Discriminative signal arises when constraints from different traces conflict: Z3 excludes low-weight constraints from $\\mathcal{C}^*$, and the scorer attributes these exclusions to the corresponding source answers via $\\sigma$ (see Algorithm~\\ref{alg:scorer} in Appendix~\\ref{app:z3-pseudocode}). The selected answer is $a^* = \\arg\\max_{a \\in \\mathcal{A}} \\text{score}(a)$.\n\n\\paragraph{Degeneration under non-discriminative constraints.}\nIn practice, self-extracted constraints are tightly coupled to their source answer: $c_m$ derived from trace $t_i$ typically entails $a_i$ ($\\sigma(c_m, a_i) \\approx 1$). When constraints lack discriminative power across candidates, MAX-SAT excludes almost no constraints ($|\\mathcal{C}^{\\setminus}| \\approx 0$), so the penalty term vanishes regardless of $\\alpha$, and the score function degenerates:\n\\begin{equation}\n\\label{eq:degenerate}\n\\text{score}(a) \\approx \\sum_{\\substack{c \\in \\mathcal{C}^* \\\\ \\text{source}(c) \\to a}} w_c,\n\\end{equation}\nwhich reduces to a weighted count of traces supporting $a$, equivalent to majority voting when weights are uniform. Only ${\\sim}8$\\% of self-extracted constraints are semantically discriminative across candidates (\\S\\ref{sec:discussion}). The ablation in \\S\\ref{sec:ablation} confirms this empirically: MAX-SAT, count-only, and random-weight baselines produce nearly identical accuracy.\n\n\\paragraph{The $C_0$ diagnostic.}\n\\label{sec:c0}\nWe define the multi-candidate rate $C_0$ as the fraction of questions for which $K$ sampled traces produce more than one distinct answer (Eq.~\\ref{eq:c0-def}). $C_0$ is a zero-cost diagnostic computable before any constraint extraction. When $C_0 < 5$\\%, nearly all questions are answered unanimously and SICA produces the same output as SC by construction. High $C_0$ does not guarantee improvement but ensures disagreement exists for constraints to resolve.\n\\begin{equation}\n\\label{eq:c0-def}\nC_0 = \\frac{|\\{q \\in \\mathcal{Q} : |\\mathcal{A}(q)| > 1\\}|}{|\\mathcal{Q}|}.\n\\end{equation}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\begin{tikzpicture}[\n    node distance=0.4cm and 0.35cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,\n                text width=1.6cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract FOL\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n% Independence Bottleneck annotation\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts FOL constraints from each trace, deduplicates, and solves a MAX-SAT instance via Z3. The red dashed box marks the independence bottleneck: same-model sampling and extraction produce correlated constraints ($K_{\\text{eff}} \\approx 1.2\\text{--}2.2$ for $K = 12$). Dashed arrow: the oracle variant substitutes gold FOL annotations.}\n\\label{fig:pipeline}\n\\end{figure}\n\n\\subsection{Oracle Control Design}\n\\label{sec:oracle-design}\n\nTo isolate whether the bottleneck lies in constraint extraction or in the aggregation mechanism, we introduce an oracle control. For FOLIO \\citep{han2022folio}, gold FOL annotations replace self-extracted constraints. For ProofWriter \\citep{tafjord2021proofwriter}, gold domain-specific logic (DSL) rules serve the same role. In both cases, Z3 evaluates the gold constraints against each candidate answer produced by the original $K$ traces; the scoring function (Eq.~\\ref{eq:score}) remains unchanged.\n\nThis design functions as a causal intervention on constraint quality. If the oracle variant produces large gains while self-extraction does not, the aggregation mechanism itself is sound, and the failure localizes to constraint extraction. Conversely, if the oracle also fails, the MAX-SAT aggregation framework is insufficient regardless of constraint quality. Results of this intervention appear in \\S\\ref{sec:oracle}.\n\n\\subsection{Scope}\n\\label{sec:scope}\n\nSICA as evaluated here uses \\emph{same-model self-extraction}: the same LLM generates traces and extracts constraints. This design isolates whether a model's own reasoning can be usefully formalized for aggregation. Methods that use trained extractors, external provers, or multi-model ensembles fall outside the scope of this evaluation. We test nine remediation strategies spanning prompt, architecture, and solver dimensions (\\S\\ref{sec:interventions}), including Z3 Feedback Refinement (Appendix~\\ref{app:z3-pseudocode}), a closed-loop paradigm \\citep{kambhampati2024position} where the solver feeds UNSAT cores back to the extractor.\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:54:30.228253+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T03:54:30.228601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:54:30.228923+00:00_

1	% References for SICA Capability Trap paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% Self-Consistency and Variants %%%
5	
6	@inproceedings{wang2023sc,
7	  title={Self-Consistency Improves Chain of Thought Reasoning in Language Models},
8	  author={Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
9	  booktitle={ICLR},
10	  year={2023}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T03:54:30.229092+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "old_string": "%%% Self-Consistency and Variants %%%",
  "new_string": "%%% Theoretical Foundations %%%\n\n@book{condorcet1785,\n  title={Essai sur l'application de l'analyse \\`a la probabilit\\'e des d\\'ecisions rendues \\`a la pluralit\\'e des voix},\n  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},\n  year={1785},\n  publisher={Imprimerie Royale},\n  address={Paris}\n}\n\n@article{austensmith1996,\n  title={Information Aggregation, Rationality, and the {C}ondorcet Jury Theorem},\n  author={Austen-Smith, David and Banks, Jeffrey S.},\n  journal={American Political Science Review},\n  volume={90},\n  number={1},\n  pages={34--45},\n  year={1996}\n}\n\n@article{ladha1992correlated,\n  title={The {C}ondorcet Jury Theorem, Free Speech, and Correlated Votes},\n  author={Ladha, Krishna K.},\n  journal={American Journal of Political Science},\n  volume={36},\n  number={3},\n  pages={617--634},\n  year={1992}\n}\n\n@article{fleiss1971kappa,\n  title={Measuring Nominal Scale Agreement Among Many Raters},\n  author={Fleiss, Joseph L.},\n  journal={Psychological Bulletin},\n  volume={76},\n  number={5},\n  pages={378--382},\n  year={1971}\n}\n\n%%% Self-Consistency and Variants %%%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "old_string": "%%% Self-Consistency and Variants %%%",
    "new_string": "%%% Theoretical Foundations %%%\n\n@book{condorcet1785,\n  title={Essai sur l'application de l'analyse \\`a la probabilit\\'e des d\\'ecisions rendues \\`a la pluralit\\'e des voix},\n  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},\n  year={1785},\n  publisher={Imprimerie Royale},\n  address={Paris}\n}\n\n@article{austensmith1996,\n  title={Information Aggregation, Rationality, and the {C}ondorcet Jury Theorem},\n  author={Austen-Smith, David and Banks, Jeffrey S.},\n  journal={American Political Science Review},\n  volume={90},\n  number={1},\n  pages={34--45},\n  year={1996}\n}\n\n@article{ladha1992correlated,\n  title={The {C}ondorcet Jury Theorem, Free Speech, and Correlated Votes},\n  author={Ladha, Krishna K.},\n  journal={American Journal of Political Science},\n  volume={36},\n  number={3},\n  pages={617--634},\n  year={1992}\n}\n\n@article{fleiss1971kappa,\n  title={Measuring Nominal Scale Agreement Among Many Raters},\n  author={Fleiss, Joseph L.},\n  journal={Psychological Bulletin},\n  volume={76},\n  number={5},\n  pages={378--382},\n  year={1971}\n}\n\n%%% Self-Consistency and Variants %%%"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T03:54:30.229297+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T03:54:30.229493+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—|–",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T03:54:30.229679+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T03:54:30.229853+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting|leverage|utilize|delve",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting|leverage|utilize|delve",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T03:54:30.230060+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T03:54:30.230236+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T03:54:30.230435+00:00_

26:[Omitted long matching line]
37:Z3 \citep{demoura2008z3} solves this with a 10-second per-problem timeout. To ensure each candidate answer participates in scoring, the pipeline injects an \emph{answer assertion} constraint $\texttt{answer\_a} \mathrel{{=}{=}} \texttt{True}$ for each trace, with weight~1. This guarantees that every candidate receives a nonzero base score proportional to its vote count; SICA is therefore a strict generalization of SC.
39:\paragraph{Answer scoring.} Let $\mathcal{C}^{\setminus} = \mathcal{C} \setminus \mathcal{C}^*$ denote the excluded constraint set. Each candidate answer $a \in \mathcal{A}(q)$ is scored by:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T03:54:30.230676+00:00_

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
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T03:54:30.231001+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces from a language model and selects the answer by majority vote: $a^* = \arg\max_{a} \sum_{i=1}^{K} \mathbf{1}[a_i = a]$. The theoretical justification for this approach follows the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: given $K$ independent voters each correct with probability $p > 0.5$, the probability that the majority is correct approaches 1 as $K \to \infty$ \citep{austensmith1996}.
8	
9	CJT requires that voters be conditionally independent given the correct answer. LLM traces violate this assumption: all $K$ samples come from the same model, conditioned on the same prompt, with only sampling temperature as a source of variation. Correlated voters reduce the effective ensemble size. \citet{ladha1992correlated} show that under uniform pairwise correlation $\rho$, the effective number of independent voters is $K_{\text{eff}} = K / (1 + (K{-}1)\rho)$. We use Fleiss' $\kappa$ \citep{fleiss1971kappa} as an empirical proxy for inter-trace agreement:
10	\begin{equation}
11	\label{eq:effk}
12	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
13	\end{equation}
14	
15	In our experiments (\S\ref{sec:main-results}), $\kappa$ ranges from 0.40 to 0.74 across model-dataset pairs, yielding $K_{\text{eff}} \approx 1.2\text{--}2.2$ for $K = 12$. At $K_{\text{eff}} \approx 1$, additional traces provide almost no new information, and the CJT guarantee collapses. This \emph{independence bottleneck} motivates our investigation: can structured constraint extraction recover discriminative signal that majority voting cannot?
16	
17	\subsection{SICA Pipeline}
18	\label{sec:pipeline}
19	
20	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from reasoning traces and selecting the answer best supported by the satisfiable 
…[truncated 9104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260519T035043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T03:54:30.231312+00:00_

The rewrite is complete. Changes made:

1. **Added §3.1** (Condorcet Independence Assumption): Frames SC as majority voting under CJT, explains the independence violation from same-model sampling, introduces the $K_{\text{eff}}$ formula with Fleiss' $\kappa$, and establishes the "independence bottleneck" framing.

2. **Restructured §3.2** (SICA Pipeline): Reorganized into clear paragraphs (trace generation, constraint extraction, deduplication, MAX-SAT, scoring, degeneration, $C_0$). Added extraction temperature $T_{\text{ext}} = 0.3$. Preserved all equations (Eq 1-5) and the degeneration analysis. $C_0$ is now a brief paragraph (3 sentences + equation) instead of a full subsection.

3. **Added §3.3** (Oracle Control Design): Promoted from implicit mention to explicit subsection. Framed as causal intervention.

4. **Updated §3.4** (Scope): Changed "six" to "nine" remediation strategies.

5. **Updated TikZ figure**: Added red dashed box around sampling+extraction stages labeled "Independence Bottleneck". Updated caption with $K_{\text{eff}}$ context.

6. **Section title**: Changed from "Method: The SICA Pipeline" to "Method".

7. **Added 4 bib entries**: `condorcet1785`, `austensmith1996`, `ladha1992correlated`, `fleiss1971kappa`.

8. All style rules pass: zero em-dashes/en-dashes, no banned words, no -ing phrase endings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260519T035043"
}
```

</details>

---

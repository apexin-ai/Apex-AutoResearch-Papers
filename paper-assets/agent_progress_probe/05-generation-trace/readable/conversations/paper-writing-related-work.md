# paper writing related work

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260514T223003.jsonl`
- **Structured JSON:** [`77e37a8af6fbb101b172.json`](../../sessions/77/77e37a8af6fbb101b172.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-14T22:32:19.024520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T22:32:19.025105+00:00_

1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T22:32:19.025291+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T22:32:19.025431+00:00_

docs/paper/_acl_template/acl_lualatex.tex
docs/paper/_acl_template/acl_latex.tex
docs/paper/main.tex
docs/paper/sections/abstract.tex
docs/paper/sections/related_work.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/experiments.tex
docs/paper/sections/analysis.tex
docs/paper/sections/appendix.tex
docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T22:32:19.025600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T22:32:19.025808+00:00_

1	% Related Work: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)
2	\section{Related Work}
3	\label{sec:related_work}
4	
5	\subsection{LLM Agent Monitoring and Evaluation}
6	
7	As LLM agents tackle increasingly complex tasks \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands,zhou2024webarena,wang2024mint}, understanding and monitoring their failure modes has become critical.
8	Taxonomic studies reveal that agent failures are often systematic: \citet{cemri2025multiagentfail} identify 14 failure modes in multi-agent systems, including step repetition as a concrete symptom, while \citet{zhu2025agentfail} show that cascading failures---where a single root cause propagates across subsequent decisions---dominate long-horizon tasks.
9	\citet{orlanski2026slopcodebench} provide the most direct evidence of agent degradation, documenting structural erosion in 77\% of coding agent trajectories with no agent fully solving any benchmark task end-to-end.
10	
11	Existing monitoring approaches span several paradigms.
12	\emph{Self-reflection} methods \citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent to diagnose its own failures, but \citet{huang2024selfcorrect} and \citet{kamoi2024selfcorrection} demonstrate that LLMs cannot reliably self-correct without external feedback, motivating external monitoring.
13	\citet{george2025cycledetection} propose unsupervised cycle detection combining call-stack analysis with embedding similarity, while \citet{pipis2025reasoningloop} analyze why reasoning models loop, using $n$-gram repetition as a detection heuristic.
14	On the external monitoring front, \citet{chen2025monitoring} show that sequence-level context is necessary---single-step analysis misses sequentially contextual harm---and \citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, with weak models reliably monitoring stronger agents.
15	
16	Our work differs from all of the above in its
…[truncated 5545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T22:32:19.025959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T22:32:19.026119+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.
5	As these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.
6	\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 90\% and quality drops of 80\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.
7	Crucially, the dominant failure pattern is not simple repetition but what we term \emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.
8	This ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.
9	We observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \citep{yang2024sweagent} and OpenHands \citep{wang2025openhands}---on SWE-bench tasks \citep{jimenez2024swebench}, 28.5\% and 6.6\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.
10	
11	Existing approaches address aspects of this problem but fall short in three ways.
12	First, \emph{repetition detectors} such as cycle detection \citep{george2025cycledetection} and SpecRA \citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss s
…[truncated 6412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T22:32:19.026262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T22:32:19.026443+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We frame stagnation detection as window-level binary classification over agent trajectories.
5	Silver labels are generated via weak supervision from three labeling functions, then used to train and evaluate three detection approaches: structural features, a neural embedding probe, and an LLM-as-judge baseline.
6	Figure~\ref{fig:pipeline} provides a system overview.
7	
8	\begin{figure*}[t]
9	\centering
10	\includegraphics[width=\textwidth]{../../figures/paper/fig_pipeline.pdf}
11	\caption{System overview. (Left) Agent trajectories are segmented into overlapping windows of $k{=}5$ steps. (Center) Three labeling functions vote on each window; majority vote produces silver labels with confidence 1--3. (Right) Three detection approaches compared: structural features (30-dim), NL embedding probe (GRU), and LLM-as-judge (eval only, not trained on silver labels).}
12	\label{fig:pipeline}
13	\end{figure*}
14	
15	%-------------------------------------------------------------------
16	\subsection{Problem Formulation}
17	\label{sec:problem}
18	
19	Given an agent trajectory $T = (a_1, a_2, \ldots, a_n)$ where each $a_t$ is an action (e.g., a shell command, file edit, or API call), we partition it into overlapping sliding windows $w_i = (a_i, \ldots, a_{i+k-1})$ with window size $k{=}5$ and stride 1.
20	The task is to assign each window a binary label $y_i \in \{0, 1\}$, where 0 denotes \emph{stagnation} (the agent is stuck or unproductive) and 1 denotes \emph{progress} (the agent is making meaningful headway toward the task goal).
21	
22	The window formulation offers two advantages over alternatives.
23	Compared to step-level scoring, windows capture short-range temporal patterns---such as a sequence of repeated failed attempts---that individual actions cannot express.
24	Compared to trajectory-level labeling, windows provide the granularity needed to pinpoint \emph{when} stagnation begins and ends within a single task attempt, enabli
…[truncated 9550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T22:32:19.026584+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T22:32:19.026819+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.
5	All reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\S\ref{sec:method}).
6	
7	\paragraph{Circular evaluation caveat.}
8	Structural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.
9	Consequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.
10	The cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\S\ref{sec:cmd_rep_ablation}).
11	A human-annotated gold set provides the definitive non-circular evaluation (\S\ref{sec:gold_set}).
12	
13	%-------------------------------------------------------------------
14	\subsection{Experimental Setup}
15	\label{sec:setup}
16	
17	\paragraph{Datasets.}
18	We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.
19	\textbf{SWE-Agent} trajectories from SWE-bench \citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\%.
20	\textbf{OpenHands} (OH) trajectories \citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\%.
21	Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).
22	Unless stated otherwise, evaluation uses the conf${\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\begin{tabu
…[truncated 13667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T22:32:19.026997+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T22:32:19.027160+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Circular Evaluation and Its Implications}
5	\label{sec:circular}
6	
7	The structural RF's 0.9951 macro-F1 (\S\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.
8	The 30 structural features include repetition ratios and file operation counts---the same signals $\lambda_1$ and $\lambda_2$ consume to produce silver labels.
9	This score therefore represents an upper bound on LF reverse-engineering fidelity.
10	
11	Two evaluation settings break this circularity.
12	First, cross-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.9674 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\_rep fires on 92.3\% vs.\ 65.6\% of windows).
13	The model cannot memorize LF outputs when tested on a different agent's distribution.
14	Second, a human-annotated gold set (\S\ref{sec:gold_set}) will provide definitive non-circular ground truth.
15	Until then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.
16	
17	\subsection{Why Temporal Label Models Fail}
18	\label{sec:why_tlm_fail}
19	
20	Despite clear temporal structure in LF activations (\S\ref{sec:lf_temporal}), no temporal label model improves downstream detection over majority vote (\S\ref{sec:temporal_label_models}).
21	The root cause is low label conflict in the 3-LF regime: conf${\geq}$2 windows dominate the training set, leaving few ambiguous labels for temporal models to correct.
22	
23	TWV targets only conf${=}1$ windows, flipping 14.1\% of their labels.
24	These flips introduce noise rather than corrections---downstream probe F1 drops by 2.57\,pp relative to MV-trained.
25	HMM overpredicts stagnation (29,176 vs.\ 25,633 progress windows), producing a distorted label distribution that degrades the probe to 0.6564.
26	Lag-HMM, despite explicitly modeling per-LF temporal offsets, tracks MV within 0.1\,pp---
…[truncated 2925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T22:32:19.027429+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Process Reward Models.}\nProcess reward models (PRMs) assign step-level quality scores to guide agent behavior during inference or training.\n\\citet{xi2025agentprm} introduce AgentPRM, training TD/GAE-based step-level rewards that evaluate both long-term promise and immediate progress in agent trajectories, requiring outcome labels and an RL pipeline.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs outperform general-purpose ones, while \\citet{wang2026planrewardbench} reveal that all reward model categories---generative, discriminative, and LLM-as-judge---degrade on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques, and \\citet{qiu2026dataprm} introduce environment-aware probing for data analysis agents to detect silent errors.\nOur work differs in operating at window level rather than step level, requiring no outcome labels or reward annotations at inference time---labeling functions use only observable structural signals---and targeting real-time monitoring ($<$5\\,ms per window) rather than training signal generation.\n\n\\paragraph{Agent Self-Reflection and Verification.}\nSelf-reflection methods prompt agents to diagnose and correct their own failures.\n\\citet{shinn2023reflexion} introduce verbal self-reflection loops, \\citet{yao2023tot} propose tree-structured deliberation, and \\citet{zhou2024lats} combine Monte Carlo tree search with LLM self-evaluation for language agents.\nHowever, \\citet{huang2024selfcorrect} demonstrate that LLMs cannot reliably self-correct reasoning without external feedback, and \\citet{kamoi2024selfcorrection} confirm that self-correction attempts frequently degrade initial answers.\nThese methods address what to \\emph{do} when an agent is stuck, relying on the stuck model's own judgment for both detection and correction.\nWe address the prior question---\\emph{when} is the agent stuck---using external structural signals rather than self-evaluation.\nOur LLM-as-judge baseline (\\S\\ref{sec:main_results}) illustrates the ceiling of model-based assessment for this detection task.\n\n\\paragraph{Weak Supervision for Sequential Data.}\nData programming \\citep{ratner2016dataprogramming} enables rapid dataset creation through user-defined labeling functions (LFs), with Snorkel \\citep{ratner2017snorkel} operationalizing this into a dependency-aware end-to-end system.\n\\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods, and \\citet{zhang2021wrench} benchmark 22 weak supervision datasets, all assuming i.i.d.\\ samples.\nExtensions to sequential data relax this assumption: \\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised NER, improving over i.i.d.\\ label models by incorporating span-level linking rules; \\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities; and \\citet{dawid1979em} provide the foundational EM framework for aggregating noisy annotators, later extended with HMM structure for sequential settings.\nWe apply data programming to agent trajectories, a novel domain where LFs exhibit systematic temporal dynamics distinct from token-level NER.\nUnlike \\citeauthor{safranchik2020linkedhmm}'s positive NER results, we find that temporal label models (HMM, lag-HMM, TWV) do not improve over majority vote in our low-conflict 3-LF regime (\\S\\ref{sec:temporal_label_models})---a negative result that constrains when sequential extensions to weak supervision add value.\n\n\\paragraph{Agent Monitoring and Degradation.}\nRecent work documents the prevalence and impact of agent failures at scale.\n\\citet{orlanski2026slopcodebench} provide direct evidence of coding agent degradation on SlopCodeBench, recording verbosity increases and quality drops across long-horizon trajectories with no agent fully solving any benchmark task.\n\\citet{chen2025monitoring} establish that sequence-level context is necessary for effective agent monitoring, as single-step analysis misses failures that emerge only across action sequences.\n\\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, showing weak models can reliably oversee stronger agents---a finding that motivates lightweight monitoring approaches over scaling up monitor size.\n\\citet{cemri2025multiagentfail} identify 14 systematic failure modes in multi-agent systems including step repetition as a concrete symptom, and \\citet{zhu2025agentfail} show that cascading failures---where single root causes propagate across subsequent decisions---dominate long-horizon tasks.\nThese works document and motivate the monitoring problem; we complement them with a systematic comparative study across signal types (structural, neural, LLM-based), demonstrating that lightweight structural features suffice for detection and transfer across agent architectures without requiring another LLM or GPU.\n\n\\paragraph{Cycle and Anomaly Detection.}\nCycle detection targets structural repetition in agent behavior.\n\\citet{george2025cycledetection} combine call-stack analysis (CDCS) with embedding similarity (CDSA) to detect action-level cycles in agents, and \\citet{pipis2025reasoningloop} analyze reasoning loops in language models using speculative decoding and $n$-gram repetition heuristics.\n\\citet{liu2026trajad} take a broader view with TrajAD, training a fine-grained verifier through synthetic perturbations to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation; they show that general-purpose LLMs perform poorly at zero-shot trajectory verification, motivating specialized approaches.\nCycle detectors are effective for exact or near-exact repetition but by design cannot capture semantically diverse stagnation, where agents vary surface commands while remaining functionally stuck.\nOur window-level approach with structural features captures both repetitive and non-repetitive stagnation patterns.\nWe formulate stagnation as prevalent binary classification over sliding windows rather than rare-event anomaly detection (\\S\\ref{sec:setup}), and our error analysis (\\S\\ref{sec:error_analysis}) confirms that the dominant missed-stagnation category involves diverse-but-ineffective behavior---the pattern category that repetition-based detectors would also miss.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Process Reward Models.}\nProcess reward models (PRMs) assign step-level quality scores to guide agent behavior during inference or training.\n\\citet{xi2025agentprm} introduce AgentPRM, training TD/GAE-based step-level rewards that evaluate both long-term promise and immediate progress in agent trajectories, requiring outcome labels and an RL pipeline.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs outperform general-purpose ones, while \\citet{wang2026planrewardbench} reveal that all reward model categories---generative, discriminative, and LLM-as-judge---degrade on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques, and \\citet{qiu2026dataprm} introduce environment-aware probing for data analysis agents to detect silent errors.\nOur work differs in operating at window level rather than step level, requiring no outcome labels or reward annotations at inference time---labeling functions use only observable structural signals---and targeting real-time monitoring ($<$5\\,ms per window) rather than training signal generation.\n\n\\paragraph{Agent Self-Reflection and Verification.}\nSelf-reflection methods prompt agents to diagnose and correct their own failures.\n\\citet{shinn2023reflexion} introduce verbal self-reflection loops, \\citet{yao2023tot} propose tree-structured deliberation, and \\citet{zhou2024lats} combine Monte Carlo tree search with LLM self-evaluation for language agents.\nHowever, \\citet{huang2024selfcorrect} demonstrate that LLMs cannot reliably self-correct reasoning without external feedback, and \\citet{kamoi2024selfcorrection} confirm that self-correction attempts frequently degrade initial answers.\nThese methods address what to \\emph{do} when an agent is stuck, relying on the stuck model's own judgment for both detection and correction.\nWe address the prior question---\\emph{when} is the agent stuck---using external structural signals rather than self-evaluation.\nOur LLM-as-judge baseline (\\S\\ref{sec:main_results}) illustrates the ceiling of model-based assessment for this detection task.\n\n\\paragraph{Weak Supervision for Sequential Data.}\nData programming \\citep{ratner2016dataprogramming} enables rapid dataset creation through user-defined labeling functions (LFs), with Snorkel \\citep{ratner2017snorkel} operationalizing this into a dependency-aware end-to-end system.\n\\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods, and \\citet{zhang2021wrench} benchmark 22 weak supervision datasets, all assuming i.i.d.\\ samples.\nExtensions to sequential data relax this assumption: \\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised NER, improving over i.i.d.\\ label models by incorporating span-level linking rules; \\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities; and \\citet{dawid1979em} provide the foundational EM framework for aggregating noisy annotators, later extended with HMM structure for sequential settings.\nWe apply data programming to agent trajectories, a novel domain where LFs exhibit systematic temporal dynamics distinct from token-level NER.\nUnlike \\citeauthor{safranchik2020linkedhmm}'s positive NER results, we find that temporal label models (HMM, lag-HMM, TWV) do not improve over majority vote in our low-conflict 3-LF regime (\\S\\ref{sec:temporal_label_models})---a negative result that constrains when sequential extensions to weak supervision add value.\n\n\\paragraph{Agent Monitoring and Degradation.}\nRecent work documents the prevalence and impact of agent failures at scale.\n\\citet{orlanski2026slopcodebench} provide direct evidence of coding agent degradation on SlopCodeBench, recording verbosity increases and quality drops across long-horizon trajectories with no agent fully solving any benchmark task.\n\\citet{chen2025monitoring} establish that sequence-level context is necessary for effective agent monitoring, as single-step analysis misses failures that emerge only across action sequences.\n\\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, showing weak models can reliably oversee stronger agents---a finding that motivates lightweight monitoring approaches over scaling up monitor size.\n\\citet{cemri2025multiagentfail} identify 14 systematic failure modes in multi-agent systems including step repetition as a concrete symptom, and \\citet{zhu2025agentfail} show that cascading failures---where single root causes propagate across subsequent decisions---dominate long-horizon tasks.\nThese works document and motivate the monitoring problem; we complement them with a systematic comparative study across signal types (structural, neural, LLM-based), demonstrating that lightweight structural features suffice for detection and transfer across agent architectures without requiring another LLM or GPU.\n\n\\paragraph{Cycle and Anomaly Detection.}\nCycle detection targets structural repetition in agent behavior.\n\\citet{george2025cycledetection} combine call-stack analysis (CDCS) with embedding similarity (CDSA) to detect action-level cycles in agents, and \\citet{pipis2025reasoningloop} analyze reasoning loops in language models using speculative decoding and $n$-gram repetition heuristics.\n\\citet{liu2026trajad} take a broader view with TrajAD, training a fine-grained verifier through synthetic perturbations to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation; they show that general-purpose LLMs perform poorly at zero-shot trajectory verification, motivating specialized approaches.\nCycle detectors are effective for exact or near-exact repetition but by design cannot capture semantically diverse stagnation, where agents vary surface commands while remaining functionally stuck.\nOur window-level approach with structural features captures both repetitive and non-repetitive stagnation patterns.\nWe formulate stagnation as prevalent binary classification over sliding windows rather than rare-event anomaly detection (\\S\\ref{sec:setup}), and our error analysis (\\S\\ref{sec:error_analysis}) confirms that the dominant missed-stagnation category involves diverse-but-ineffective behavior---the pattern category that repetition-based detectors would also miss.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T22:32:19.027717+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260514T223003",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-14T22:32:19.027894+00:00_

Related Work 已写入。5 个 paragraph-level subsection，~700 words，所有 citation key 均来自已验证列表，无 "significantly"，无价值判断，数字通过 section 引用回指而非重复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260514T223003"
}
```

</details>

---

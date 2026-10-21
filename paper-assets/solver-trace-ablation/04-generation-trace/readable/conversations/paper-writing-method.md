# paper writing method

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_writing_method_20260514T191123.jsonl`
- **Structured JSON:** [`b49eb490db2fcc5882f2.json`](../../sessions/b4/b49eb490db2fcc5882f2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-14T19:15:14.420340+00:00_

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
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T19:15:14.420967+00:00_

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
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T19:15:14.421155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T19:15:14.421467+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA-derived ISR across three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}), as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}), and as a cross-logic diagnostic protocol (\S\ref{sec:crosslogic}). We then synthesize the observed hacking strategies into a taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Model and Training.}
10	We use Qwen3-4B as the base model, trained with GRPO~\cite{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 steps where noted. All experiments use three random seeds (42, 43, 44) to assess cross-seed stability, with seeds controlling model initialization and training stochasticity. Training data is a fixed 500-example subset of FOLIO~\cite{folio} (\texttt{train\_500\_seed42.jsonl}), a corpus of human-annotated first-order logic problems, held constant across all seeds and conditions.
11	
12	\paragraph{Solvers and Logic Types.}
13	For first-order logic (FOL), we use Prover9 as the automated theorem prover. For Prolog experiments, we use SWI-Prolog 8.4.2. The execution reward $r_{\text{exec}} \in \{0, 1\}$ is binary: 1 if the solver returns a proof, 0 otherwise.
14	
15	\paragraph{Evaluation.}
16	We evaluate on a held-out set of 100 FOLIO examples using greedy decoding. All ISR values reported in cross-run comparisons are computed by \texttt{eval\_sta.py}, which applies the full STA protocol uniformly. We report: prove rate (PR), proved-only ISR (ISR*, computed over proved samples only), hacking mode percentages (H7, H1), genuine rate, and mean component count where relevant. All tabulated ISR values are proved-only unless otherwise noted.
17	
18	\paragraph{Reward Formulations.}
19	We compare six conditions:
20	\begin{itemize}[nosep,leftmargin=*]
21	  \item \textbf{Exec-only}: $r = r_{\text{exec}}$ (baseline)
22	  \item \textbf{ISR $\beta$}: $r = r_{\text{exec}
…[truncated 16379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T19:15:14.421674+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T19:15:14.421833+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T19:15:14.421965+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "writing_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "writing_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T19:15:14.422277+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: main\\n  template: acl2023/\\n  template_note: \\\"ARR May 25 cycle. ACL Rolling Review format (acl2023.sty).\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >\\n    ISR (Intensional Structural Reward), derived via Solver Trace Ablation,\\n    serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers\\n    but fails as a training signal due to meta-level Goodhart's Law — the diagnostic\\n    metric becomes gamed when optimized, with apparent improvements explained by\\n    premise minimization artifacts.\\n  created_at: 2026-05-14T18:00:00Z\\n  updated_at: 2026-05-14T19:05:00Z\\n  update_note: \\\"Director approved with 5 corrections applied: taxonomy 6→7, Claim 3 Prolog STA 3/3 gaming complete, conclusion limitations updated, tab5/fig4 expanded, registry_refs added.\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    core_bullets:\\n      - \\\"Problem: GRPO formalizers achieve high prove rates but produce structurally degenerate outputs; no diagnostic exists\\\"\\n      - \\\"Method: STA derives ISR via leave-one-out component necessity testing on solver inputs\\\"\\n      - \\\"Claim 1: ISR detects hacking invisible to prove_rate (0.64→0.13→0.003 collapse over 100→500→1000 steps)\\\"\\n      - \\\"Claim 2: ISR-as-reward exhibits meta-level Goodhart — β=0.1 induces ISR-specific gaming (H7=64.5% vs 0% random), premise-matched 1.06x; β=0.3 PR collapses (18% vs 48% random)\\\"\\n      - \\\"Claim 3: ISR diagnostic transfers to Prolog (cross-logic generality)\\\"\\n      - \\\"Taxonomy: 7 distinct hacking modes identified across conditions (including query-as-fact gaming discovered in Prolog STA)\\\"\\n    dependencies: [experiments, method, discussion]\\n    tables: []\\n    figures: []\\n    registry_r
…[truncated 17631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T19:15:14.422443+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T19:15:14.422777+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (7 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 se
…[truncated 20933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T19:15:14.422943+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T19:15:14.423073+00:00_

paper/method.tex
paper/discussion.tex
paper/introduction.tex
paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T19:15:14.423213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T19:15:14.423476+00:00_

1	% Method section — solver-trace-ablation
2	% Requires: algorithm, algorithmic, amsmath, enumitem packages
3	
4	\section{Method}
5	\label{sec:method}
6	
7	\subsection{Task Formulation}
8	\label{sec:task}
9	
10	Given natural language premises $P_1, \ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \{c_1, \ldots, c_n\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.
11	An external solver $S$ determines whether $F$ constitutes a valid proof:
12	$S(F) \in \{\textit{proved}, \textit{failed}\}$.
13	We experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs.
14	
15	\subsection{GRPO Training}
16	\label{sec:grpo}
17	
18	We train formalizers with Group Relative Policy Optimization \citep[GRPO;][]{deepseekmath}.
19	For each training prompt, the policy samples $K{=}8$ rollouts.
20	Each rollout receives a binary \emph{execution reward}:
21	\begin{equation}
22	  r_{\text{exec}}(x) = \mathbf{1}\bigl[S(F_x) = \textit{proved}\bigr]
23	  \label{eq:rexec}
24	\end{equation}
25	where $F_x$ is the formalization produced by rollout $x$.
26	Advantages are computed group-relative: $A_i = (r_i - \bar{r}) / \sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.
27	
28	This setup optimizes \emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \emph{structural quality} of proved outputs.
29	A formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.
30	
31	\subsection{Solver Trace Ablation}
32	\label{sec:sta}
33	
34	To diagnose structural quality, we propose \emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each
…[truncated 7183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T19:15:14.423653+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T19:15:14.423875+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Neurosymbolic approaches that combine large language models with external solvers have shown promising results on logical reasoning tasks~\citep{satlm, logic-lm, linc}.
9	Recent work applies reinforcement learning---specifically Group Relative Policy Optimization~\citep[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by automated theorem provers~\citep{mellgren-prolog-grpo, logic-rl}.
10	The standard reward signal in these systems is binary: 1 if the solver proves the formalization, 0 otherwise.
11	This execution reward drives rapid improvement in prove rate but provides no gradient on structural quality.
12	A formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.
13	
14	The absence of structural diagnostics leaves a critical blind spot.
15	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.
16	Without a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from those that exploit solver mechanics.
17	This gap is particularly consequential in RL settings, where the optimizer will find and exploit any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-
…[truncated 6272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T19:15:14.424161+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
  "content": "% Method section — solver-trace-ablation\n% Requires: algorithm, algorithmic, amsmath, enumitem packages\n\n\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Overview of Solver Trace Ablation (STA). (a) Formalization pipeline: NL input is formalized into logical representation and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations to compute ISR. (c) ISR as diagnostic vs.\\ ISR as reward: when the diagnostic becomes the optimization target, meta-level Goodhart's Law emerges.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task: NL to Formal Logic}\n\\label{sec:task}\n\nGiven natural language premises $P_1, \\ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \\{c_1, \\ldots, c_n\\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.\nAn external solver $S$ determines whether $F$ constitutes a valid proof:\n$S(F) \\in \\{\\textit{proved}, \\textit{failed}\\}$.\nWe experiment with two solver backends: Prover9 for first-order logic~\\citep{proofwriter} and SWI-Prolog for Prolog programs (\\autoref{fig:sta-overview}a).\n\n\\subsection{GRPO Training}\n\\label{sec:grpo}\n\nWe train formalizers with Group Relative Policy Optimization \\citep[GRPO;][]{deepseekmath}.\nFor each training prompt, the policy samples $K{=}8$ rollouts.\nEach rollout receives a binary \\emph{execution reward}:\n\\begin{equation}\n  r_{\\text{exec}}(x) = \\mathbf{1}\\bigl[S(F_x) = \\textit{proved}\\bigr]\n  \\label{eq:rexec}\n\\end{equation}\nwhere $F_x$ is the formalization produced by rollout $x$.\nAdvantages are computed group-relative: $A_i = (r_i - \\bar{r}) / \\sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.\n\nThis setup optimizes \\emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \\emph{structural quality} of proved outputs.\nA formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nTo diagnose structural quality, we propose \\emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each component of a proved formalization is individually necessary for proof success (\\autoref{fig:sta-overview}b).\n\n\\paragraph{Protocol.}\nGiven a proved formalization $x$ with $n$ components $\\{c_1, \\ldots, c_n\\}$, STA constructs $n$ ablated variants $x \\setminus \\{c_i\\}$, each with one component removed, and re-runs the solver on each.\nA component $c_i$ is \\emph{necessary} if its removal causes proof failure: $S(x \\setminus \\{c_i\\}) = \\textit{failed}$.\nWhat constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.\n\n\\paragraph{Intensional Structural Reward.}\nWe define ISR as the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\mathbf{1}\\bigl[S(x \\setminus \\{c_i\\}) = \\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR $\\in [0, 1]$ and is defined only for proved formalizations ($r_{\\text{exec}}(x) = 1$).\nISR $= 1$ indicates a maximally tight formalization where every component is individually necessary; ISR $= 0$ indicates complete redundancy.\nThe protocol is solver-agnostic: it applies to any solver that accepts component-level input manipulation, requiring $n{+}1$ solver calls per sample (one initial verification plus $n$ ablations).\n\nAlgorithm~\\ref{alg:sta} gives the full procedure.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE ISR score $\\in [0,1]$ or $\\bot$ (undefined)\n\\IF{$S(x) \\neq \\textit{proved}$}\n  \\RETURN $\\bot$\n\\ENDIF\n\\STATE $n_{\\text{nec}} \\gets 0$\n\\FOR{$i = 1$ \\TO $n$}\n  \\STATE $x' \\gets x \\setminus \\{c_i\\}$\n  \\IF{$S(x') = \\textit{failed}$}\n    \\STATE $n_{\\text{nec}} \\gets n_{\\text{nec}} + 1$\n  \\ENDIF\n\\ENDFOR\n\\RETURN $n_{\\text{nec}} \\mathbin{/} n$\n\\end{algorithmic}\n\\end{algorithm}\n\nSTA draws on the same intuition as mutation testing in software engineering \\citep{demillo1978, jia-harman-survey}: systematically perturbing a program to assess whether each element contributes to the overall result.\nThe key difference is that STA operates on solver \\emph{inputs} (formalizations) rather than program code, and targets component necessity rather than test adequacy.\n\n\\paragraph{ISR limitations.}\nISR measures syntactic component necessity, not semantic faithfulness to the natural language input.\nIt is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each component carries a larger share of the proof burden under LOO ablation.\nWe control for this confound in our analysis (\\S\\ref{sec:goodhart}).\n\n\\subsection{ISR as Reward Signal}\n\\label{sec:rewards}\n\nHaving defined ISR as a diagnostic, we investigate whether it can serve as a training signal (\\autoref{fig:sta-overview}c).\nWe study six reward conditions across two formulations.\nFor all RL conditions, bonuses apply only to proved samples; unproved samples receive $r = 0$.\n\n\\paragraph{Exec-only (baseline).}\n$r = r_{\\text{exec}}$.\nBinary solver verification with no structural component.\n\n\\paragraph{Additive ISR.}\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR}(x)), \\quad \\beta \\in \\{0.1, 0.3\\}\n  \\label{eq:additive-isr}\n\\end{equation}\nISR provides a bonus proportional to structural tightness, gated on proof success.\nThe multiplicative gating ensures that unproved samples never receive an ISR bonus.\n\n\\paragraph{Additive Random (control).}\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u), \\quad u \\sim \\mathcal{U}(0,1), \\quad \\beta \\in \\{0.1, 0.3\\}\n  \\label{eq:additive-random}\n\\end{equation}\nReplacing ISR with uniform noise isolates the causal effect of ISR-specific structural signal from general reward-shaping effects (variance injection, magnitude scaling).\n\n\\paragraph{SFT baseline.}\nSupervised fine-tuning on gold formalizations with no reinforcement learning, confirming whether observed hacking behaviors are RL-reward-specific or artifacts of general fine-tuning.\n\nEach RL condition is trained across three random seeds (42, 43, 44).\nSeeds control model initialization and training stochasticity; all seeds share identical training data (\\S\\ref{sec:setup}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy-method}\n\nAnalysis of trained models across reward conditions, seeds, and logic types reveals seven distinct reward hacking modes (full quantitative analysis in \\S\\ref{sec:taxonomy}):\n\n\\begin{enumerate}[leftmargin=*, itemsep=2pt]\n\\item \\textbf{Conclusion Embedding (H1).}\nThe conclusion appears verbatim as one of multiple premises; the solver succeeds trivially regardless of the other premises.\n\n\\item \\textbf{Conclusion Duplication (H7).}\nThe formalization collapses to a single premise identical to the conclusion.\nLOO ablation marks this sole component as necessary, yielding ISR$=$1 by construction.\n\n\\item \\textbf{Tautological Collapse.}\nTwo-component formalizations where the premise and query are identical.\n\n\\item \\textbf{Repetition Collapse.}\nIdentical premises or clauses repeated until the token limit.\nRemoving any single copy leaves the others intact, yielding ISR $\\approx 0$.\n\n\\item \\textbf{Complexity-without-utility.}\nExcessive syntactically complex but semantically vacuous components, none individually necessary.\n\n\\item \\textbf{Contradiction Explosion.}\nUnbounded component count growth over training, with the excess premises trivially entailing any conclusion.\n\n\\item \\textbf{Query-as-fact Gaming.}\nThe model converts the natural language conclusion into an atom and includes it as both a fact and the query.\nThis mode bypasses text-match classifiers designed for H1/H7.\n\\end{enumerate}\n\nModes are identified by a two-stage classification procedure.\nFirst, strict normalized text matching detects H1 and H7 by comparing each premise against the query.\nSecond, functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA catches modes that evade text matching---particularly query-as-fact gaming, where the gaming mechanism produces surface-level novelty invisible to exact-match classifiers.\nSamples not assigned to any hacking mode are classified as \\emph{genuine}.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
    "content": "% Method section — solver-trace-ablation\n% Requires: algorithm, algorithmic, amsmath, enumitem packages\n\n\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Overview of Solver Trace Ablation (STA). (a) Formalization pipeline: NL input is formalized into logical representation and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations to compute ISR. (c) ISR as diagnostic vs.\\ ISR as reward: when the diagnostic becomes the optimization target, meta-level Goodhart's Law emerges.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task: NL to Formal Logic}\n\\label{sec:task}\n\nGiven natural language premises $P_1, \\ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \\{c_1, \\ldots, c_n\\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.\nAn external solver $S$ determines whether $F$ constitutes a valid proof:\n$S(F) \\in \\{\\textit{proved}, \\textit{failed}\\}$.\nWe experiment with two solver backends: Prover9 for first-order logic~\\citep{proofwriter} and SWI-Prolog for Prolog programs (\\autoref{fig:sta-overview}a).\n\n\\subsection{GRPO Training}\n\\label{sec:grpo}\n\nWe train formalizers with Group Relative Policy Optimization \\citep[GRPO;][]{deepseekmath}.\nFor each training prompt, the policy samples $K{=}8$ rollouts.\nEach rollout receives a binary \\emph{execution reward}:\n\\begin{equation}\n  r_{\\text{exec}}(x) = \\mathbf{1}\\bigl[S(F_x) = \\textit{proved}\\bigr]\n  \\label{eq:rexec}\n\\end{equation}\nwhere $F_x$ is the formalization produced by rollout $x$.\nAdvantages are computed group-relative: $A_i = (r_i - \\bar{r}) / \\sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped surrogate objective with KL regularization.\n\nThis setup optimizes \\emph{prove rate}---the fraction of rollouts yielding a proved formalization---but provides no signal about the \\emph{structural quality} of proved outputs.\nA formalization that embeds the conclusion among its premises, producing a trivially provable tautology, receives the same reward as a faithful multi-step derivation.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nTo diagnose structural quality, we propose \\emph{Solver Trace Ablation} (STA), a leave-one-out protocol that tests whether each component of a proved formalization is individually necessary for proof success (\\autoref{fig:sta-overview}b).\n\n\\paragraph{Protocol.}\nGiven a proved formalization $x$ with $n$ components $\\{c_1, \\ldots, c_n\\}$, STA constructs $n$ ablated variants $x \\setminus \\{c_i\\}$, each with one component removed, and re-runs the solver on each.\nA component $c_i$ is \\emph{necessary} if its removal causes proof failure: $S(x \\setminus \\{c_i\\}) = \\textit{failed}$.\nWhat constitutes a component depends on the logic type: individual premises in FOL, individual clauses or ground facts in Prolog.\n\n\\paragraph{Intensional Structural Reward.}\nWe define ISR as the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\mathbf{1}\\bigl[S(x \\setminus \\{c_i\\}) = \\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR $\\in [0, 1]$ and is defined only for proved formalizations ($r_{\\text{exec}}(x) = 1$).\nISR $= 1$ indicates a maximally tight formalization where every component is individually necessary; ISR $= 0$ indicates complete redundancy.\nThe protocol is solver-agnostic: it applies to any solver that accepts component-level input manipulation, requiring $n{+}1$ solver calls per sample (one initial verification plus $n$ ablations).\n\nAlgorithm~\\ref{alg:sta} gives the full procedure.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE ISR score $\\in [0,1]$ or $\\bot$ (undefined)\n\\IF{$S(x) \\neq \\textit{proved}$}\n  \\RETURN $\\bot$\n\\ENDIF\n\\STATE $n_{\\text{nec}} \\gets 0$\n\\FOR{$i = 1$ \\TO $n$}\n  \\STATE $x' \\gets x \\setminus \\{c_i\\}$\n  \\IF{$S(x') = \\textit{failed}$}\n    \\STATE $n_{\\text{nec}} \\gets n_{\\text{nec}} + 1$\n  \\ENDIF\n\\ENDFOR\n\\RETURN $n_{\\text{nec}} \\mathbin{/} n$\n\\end{algorithmic}\n\\end{algorithm}\n\nSTA draws on the same intuition as mutation testing in software engineering \\citep{demillo1978, jia-harman-survey}: systematically perturbing a program to assess whether each element contributes to the overall result.\nThe key difference is that STA operates on solver \\emph{inputs} (formalizations) rather than program code, and targets component necessity rather than test adequacy.\n\n\\paragraph{ISR limitations.}\nISR measures syntactic component necessity, not semantic faithfulness to the natural language input.\nIt is also subject to a component-count confound: formalizations with fewer components yield mechanically higher ISR, since each component carries a larger share of the proof burden under LOO ablation.\nWe control for this confound in our analysis (\\S\\ref{sec:goodhart}).\n\n\\subsection{ISR as Reward Signal}\n\\label{sec:rewards}\n\nHaving defined ISR as a diagnostic, we investigate whether it can serve as a training signal (\\autoref{fig:sta-overview}c).\nWe study six reward conditions across two formulations.\nFor all RL conditions, bonuses apply only to proved samples; unproved samples receive $r = 0$.\n\n\\paragraph{Exec-only (baseline).}\n$r = r_{\\text{exec}}$.\nBinary solver verification with no structural component.\n\n\\paragraph{Additive ISR.}\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR}(x)), \\quad \\beta \\in \\{0.1, 0.3\\}\n  \\label{eq:additive-isr}\n\\end{equation}\nISR provides a bonus proportional to structural tightness, gated on proof success.\nThe multiplicative gating ensures that unproved samples never receive an ISR bonus.\n\n\\paragraph{Additive Random (control).}\n\\begin{equation}\n  r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot u), \\quad u \\sim \\mathcal{U}(0,1), \\quad \\beta \\in \\{0.1, 0.3\\}\n  \\label{eq:additive-random}\n\\end{equation}\nReplacing ISR with uniform noise isolates the causal effect of ISR-specific structural signal from general reward-shaping effects (variance injection, magnitude scaling).\n\n\\paragraph{SFT baseline.}\nSupervised fine-tuning on gold formalizations with no reinforcement learning, confirming whether observed hacking behaviors are RL-reward-specific or artifacts of general fine-tuning.\n\nEach RL condition is trained across three random seeds (42, 43, 44).\nSeeds control model initialization and training stochasticity; all seeds share identical training data (\\S\\ref{sec:setup}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy-method}\n\nAnalysis of trained models across reward conditions, seeds, and logic types reveals seven distinct reward hacking modes (full quantitative analysis in \\S\\ref{sec:taxonomy}):\n\n\\begin{enumerate}[leftmargin=*, itemsep=2pt]\n\\item \\textbf{Conclusion Embedding (H1).}\nThe conclusion appears verbatim as one of multiple premises; the solver succeeds trivially regardless of the other premises.\n\n\\item \\textbf{Conclusion Duplication (H7).}\nThe formalization collapses to a single premise identical to the conclusion.\nLOO ablation marks this sole component as necessary, yielding ISR$=$1 by construction.\n\n\\item \\textbf{Tautological Collapse.}\nTwo-component formalizations where the premise and query are identical.\n\n\\item \\textbf{Repetition Collapse.}\nIdentical premises or clauses repeated until the token limit.\nRemoving any single copy leaves the others intact, yielding ISR $\\approx 0$.\n\n\\item \\textbf{Complexity-without-utility.}\nExcessive syntactically complex but semantically vacuous components, none individually necessary.\n\n\\item \\textbf{Contradiction Explosion.}\nUnbounded component count growth over training, with the excess premises trivially entailing any conclusion.\n\n\\item \\textbf{Query-as-fact Gaming.}\nThe model converts the natural language conclusion into an atom and includes it as both a fact and the query.\nThis mode bypasses text-match classifiers designed for H1/H7.\n\\end{enumerate}\n\nModes are identified by a two-stage classification procedure.\nFirst, strict normalized text matching detects H1 and H7 by comparing each premise against the query.\nSecond, functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA catches modes that evade text matching---particularly query-as-fact gaming, where the gaming mechanism produces surface-level novelty invisible to exact-match classifiers.\nSamples not assigned to any hacking mode are classified as \\emph{genuine}.\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T19:15:14.424508+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T19:15:14.424677+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T19:15:14.424890+00:00_

1	% Method section — solver-trace-ablation
2	% Requires: algorithm, algorithmic, amsmath, enumitem packages
3	
4	\section{Method}
5	\label{sec:method}
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig1_sta_overview.pdf}
10	\caption{Overview of Solver Trace Ablation (STA). (a) Formalization pipeline: NL input is formalized into logical representation and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations to compute ISR. (c) ISR as diagnostic vs.\ ISR as reward: when the diagnostic becomes the optimization target, meta-level Goodhart's Law emerges.}
11	\label{fig:sta-overview}
12	\end{figure*}
13	
14	\subsection{Task: NL to Formal Logic}
15	\label{sec:task}
16	
17	Given natural language premises $P_1, \ldots, P_k$ and a conclusion $C$, the task is to produce a formal logic program $F = \{c_1, \ldots, c_n\}$, where each component $c_i$ is a premise encoding (in FOL) or a clause/fact (in Prolog), with one distinguished component encoding the query derived from $C$.
18	An external solver $S$ determines whether $F$ constitutes a valid proof:
19	$S(F) \in \{\textit{proved}, \textit{failed}\}$.
20	We experiment with two solver backends: Prover9 for first-order logic~\citep{proofwriter} and SWI-Prolog for Prolog programs (\autoref{fig:sta-overview}a).
21	
22	\subsection{GRPO Training}
23	\label{sec:grpo}
24	
25	We train formalizers with Group Relative Policy Optimization \citep[GRPO;][]{deepseekmath}.
26	For each training prompt, the policy samples $K{=}8$ rollouts.
27	Each rollout receives a binary \emph{execution reward}:
28	\begin{equation}
29	  r_{\text{exec}}(x) = \mathbf{1}\bigl[S(F_x) = \textit{proved}\bigr]
30	  \label{eq:rexec}
31	\end{equation}
32	where $F_x$ is the formalization produced by rollout $x$.
33	Advantages are computed group-relative: $A_i = (r_i - \bar{r}) / \sigma_r$ within each prompt's rollout group, and the policy update maximizes expected advantage under a clipped s
…[truncated 7183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T19:15:14.425089+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
  "old_string": "We experiment with two solver backends: Prover9 for first-order logic~\\citep{proofwriter} and SWI-Prolog for Prolog programs (\\autoref{fig:sta-overview}a).",
  "new_string": "We experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs (\\autoref{fig:sta-overview}a)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
    "old_string": "We experiment with two solver backends: Prover9 for first-order logic~\\citep{proofwriter} and SWI-Prolog for Prolog programs (\\autoref{fig:sta-overview}a).",
    "new_string": "We experiment with two solver backends: Prover9 for first-order logic and SWI-Prolog for Prolog programs (\\autoref{fig:sta-overview}a)."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T19:15:14.425256+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T191123",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T19:15:14.425449+00:00_

Method section written to `paper/method.tex`. Changes from the previous draft:

- **Added Figure 1** (`fig:sta-overview`) — the 3-panel STA overview figure, placed at the top of the section
- **Added `\autoref` references** to Figure 1 panels (a), (b), (c) in the Task, STA, and Reward Signal subsections
- **Dropped convex formulations** — experiments.tex only uses 6 conditions (exec-only, ISR×2β, random×2β, SFT); convex was not part of the main experimental matrix
- **Trimmed taxonomy section** — removed quantitative results (percentages, seed-specific data) that belong in §4; kept definitional descriptions only, with a forward reference to `\S\ref{sec:taxonomy}`
- **Added explicit equation labels** for the random control reward (`eq:additive-random`)
- **Fixed label collision** — taxonomy label changed to `sec:taxonomy-method` to avoid colliding with `sec:taxonomy` in experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260514T191123"
}
```

</details>

---

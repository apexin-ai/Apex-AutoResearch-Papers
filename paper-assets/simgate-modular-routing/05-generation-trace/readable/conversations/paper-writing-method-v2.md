# paper writing method v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_writing_method_v2_20260514T092526.jsonl`
- **Structured JSON:** [`7458976060e69bc7e18c.json`](../../sessions/74/7458976060e69bc7e18c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-14T09:27:00.902747+00:00_

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
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T09:27:00.903390+00:00_

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
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T09:27:00.903685+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T09:27:00.903899+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T09:27:00.904164+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*paper*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*paper*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T09:27:00.904367+00:00_

artifacts/_project/report/paper_data_tables.md
artifacts/_project/paper/paper_outline.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T09:27:00.904545+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T09:27:00.904715+00:00_

artifacts/dream_reports/dream_20260513T153257/best/paper.tex
artifacts/dream_reports/dream_20260513T153257/median/paper.tex
artifacts/dream_reports/dream_20260513T153257/worst/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T09:27:00.904881+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*experiment*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*experiment*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T09:27:00.905079+00:00_

artifacts/_project/paper/experiment_tables.md
artifacts/_project/report/experiment_tables.md
artifacts/_project/paper/experiments_draft_dd9866.md
artifacts/_project/paper/experiments_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T09:27:00.905249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_draft.md"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T09:27:00.905495+00:00_

1	# Experiments — Draft v1
2	
3	\section{Experiments}
4	
5	\subsection{Setup}
6	\label{sec:exp-setup}
7	
8	We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.
9	
10	\subsection{Death Avoidance Decomposition}
11	\label{sec:death-decomp}
12	
13	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{no\_death}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.
14	
15	This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), as shown in Figure~\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episodes compared to 16.3\% for deterministic computation---a 2.6$\times$ ratio that drives the bulk of the observed score difference.
16	
17	The episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \texttt
…[truncated 6755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T09:27:00.905718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T09:27:00.905980+00:00_

1	# EMNLP 2026 Short Paper Outline
2	
3	## Title Candidates
4	
5	1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**
6	2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**
7	3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**
8	
9	Recommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)
10	
11	---
12	
13	## Abstract Skeleton (~150 words)
14	
15	Key points to cover:
16	
17	- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?
18	- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.
19	- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.
20	- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).
21	- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.
22	
23	---
24	
25	## Section Structure
26	
27	### 1. Introduction (0.8 pages)
28	
29	**Key points:**
30	- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the r
…[truncated 8551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T09:27:00.906258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiment_tables.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiment_tables.md"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T09:27:00.906514+00:00_

1	# Experiment Tables for EMNLP 2026 Short Paper
2	
3	> **Status**: Preliminary (pre-analysis: prescreening 5 ep/task + MVP 20 ep/task, N=249 episodes).
4	> Plan-001b full data collection in progress; numbers will be updated upon completion.
5	
6	---
7	
8	## Table 1: Death Decomposition Analysis (plan-012)
9	
10	Core result: deterministic simulation advantage is almost entirely explained by death avoidance.
11	
12	| Metric | Episode-weighted | Task-weighted† |
13	|--------|:---------------:|:-------------:|
14	| Δ_full (det − internal) | **+38.33** | **+41.48** |
15	| Δ_nd (non-death episodes only) | +0.48 | +0.91 |
16	| DAF (death avoidance fraction) | 98.8% | 93.9% |
17	| DAF 95% CI (bootstrap) | [93.9%, 104.5%] | [84.6%, 99.8%] |
18	| Pearson *r* (Δ_death_rate vs Δ_full) | 0.986 | — |
19	| *p*-value | <0.0001 | — |
20	| Δ_penalty_removed | +0.98 | — |
21	| Internal death rate | 49.0% | — |
22	| Deterministic death rate | 11.7% | — |
23	| Tasks / Episodes | 30 / 249 | 30 / 249 |
24	
25	**Data source**: `results/death_decomposition_report.json` (plan-012, 2026-05-14).
26	Episode-weighted = aggregate means across all episodes; Task-weighted† = mean of per-task metrics (from registry, pending re-verification).
27	
28	### Signal Source Decomposition (episode-level)
29	
30	| Signal Source | Count | % of Episodes |
31	|--------------|:-----:|:------------:|
32	| death_asymmetry | 93 | 37.3% |
33	| tied_alive (no-preference) | 117 | 47.0% |
34	| both_dead (no-preference) | 29 | 11.6% |
35	| score_comparison | 10 | 4.0% |
36	
37	**Interpretation**: 93/102 det-preferred labels (91.2%) come from death asymmetry; only 9 (8.8%) from genuine score differences.
38	
39	---
40	
41	## Table 2: Keyword Routing Baseline (plan-011)
42	
43	All keyword heuristics degenerate — none provides meaningful routing signal.
44	
45	| Version | Keywords | N | Match Rate | Routing Acc.† | Effective Behavior |
46	|---------|:--------:|:---:|:----------:|:------------:|-------------------|
47	| v1 
…[truncated 3864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T09:27:00.906856+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md",
  "content": "# Method Section — Draft v2 (A-Source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Method}\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 98.2\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n\nFor each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.\n\nEach episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. We evaluate on ScienceWorld \\cite{scienceworld-2022}, which spans 30 task types covering physical and chemical reasoning with a $-100$ penalty upon agent death. After prescreening (5 episodes per type for signal estimation), we perform targeted full collection on 11 task types, yielding 245 episode pairs (20--40 per type).\n\n\\subsection{Death-Aware Labeling}\n\\label{sec:labeling}\n\nEach counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:\n\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ the surviving strategy is preferred.\n    \\item \\textbf{Both dead}: $d^{\\text{int}} = d^{\\text{det}} = 1$ $\\rightarrow$ \\texttt{no\\_preference}.\n    \\item \\textbf{Score comparison}: both survive and $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ the higher-scoring strategy is preferred.\n    \\item \\textbf{Tied alive}: both survive and $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n\\end{enumerate}\n\nAcross 245 episodes, this yields 86 (35.1\\%) \\texttt{det\\_preferred}, 9 (3.7\\%) \\texttt{internal\\_preferred}, and 150 (61.2\\%) \\texttt{no\\_preference}. The near-absence of \\texttt{internal\\_preferred} labels combined with the dominance of \\texttt{no\\_preference} indicates that the deterministic strategy's advantage is concentrated in death avoidance rather than superior task performance when both agents survive.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{no\\_death}}}{\\Delta_{\\text{full}}}\n\\end{equation}\nwhere $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{no\\_death}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\\Delta_{\\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\\Delta_{\\text{full}}| > 0$.\n\nOn 245 episodes across 11 task types: $\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{no\\_death}} = +2.84$, yielding DAF $= 90.41\\%$. The cross-task consistency is strong: the Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$) across 11 task types, indicating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.\n\n\\subsection{Rule-Based Baseline}\n\\label{sec:rule}\n\nAs a simple routing heuristic, we test keyword-based rules that route to deterministic computation when the action contains science-related verbs. We evaluate three keyword lists of decreasing breadth:\n\n\\begin{itemize}\n    \\item \\textbf{v1} (20 generic verbs including \\emph{connect}, \\emph{move}): matches 85.8\\% of actions, degenerating to always-deterministic.\n    \\item \\textbf{v2} (17 science-specific verbs: \\emph{heat}, \\emph{boil}, \\emph{melt}, \\emph{freeze}, \\ldots): matches 4.9\\%, degenerating to always-internal.\n    \\item \\textbf{v3} (12 state-change verbs): matches 2.8\\%, degenerating to always-internal.\n\\end{itemize}\n\nThe structural cause is that ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms. No keyword granularity bridges the gap between near-total and negligible match rates, precluding meaningful routing discrimination. This structural failure motivates observation-based approaches that use environment observations and agent state as routing features rather than action keywords.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md",
    "content": "# Method Section — Draft v2 (A-Source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Method}\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 98.2\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n\nFor each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.\n\nEach episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. We evaluate on ScienceWorld \\cite{scienceworld-2022}, which spans 30 task types covering physical and chemical reasoning with a $-100$ penalty upon agent death. After prescreening (5 episodes per type for signal estimation), we perform targeted full collection on 11 task types, yielding 245 episode pairs (20--40 per type).\n\n\\subsection{Death-Aware Labeling}\n\\label{sec:labeling}\n\nEach counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:\n\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ the surviving strategy is preferred.\n    \\item \\textbf{Both dead}: $d^{\\text{int}} = d^{\\text{det}} = 1$ $\\rightarrow$ \\texttt{no\\_preference}.\n    \\item \\textbf{Score comparison}: both survive and $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ the higher-scoring strategy is preferred.\n    \\item \\textbf{Tied alive}: both survive and $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n\\end{enumerate}\n\nAcross 245 episodes, this yields 86 (35.1\\%) \\texttt{det\\_preferred}, 9 (3.7\\%) \\texttt{internal\\_preferred}, and 150 (61.2\\%) \\texttt{no\\_preference}. The near-absence of \\texttt{internal\\_preferred} labels combined with the dominance of \\texttt{no\\_preference} indicates that the deterministic strategy's advantage is concentrated in death avoidance rather than superior task performance when both agents survive.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{no\\_death}}}{\\Delta_{\\text{full}}}\n\\end{equation}\nwhere $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{no\\_death}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\\Delta_{\\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\\Delta_{\\text{full}}| > 0$.\n\nOn 245 episodes across 11 task types: $\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{no\\_death}} = +2.84$, yielding DAF $= 90.41\\%$. The cross-task consistency is strong: the Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$) across 11 task types, indicating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.\n\n\\subsection{Rule-Based Baseline}\n\\label{sec:rule}\n\nAs a simple routing heuristic, we test keyword-based rules that route to deterministic computation when the action contains science-related verbs. We evaluate three keyword lists of decreasing breadth:\n\n\\begin{itemize}\n    \\item \\textbf{v1} (20 generic verbs including \\emph{connect}, \\emph{move}): matches 85.8\\% of actions, degenerating to always-deterministic.\n    \\item \\textbf{v2} (17 science-specific verbs: \\emph{heat}, \\emph{boil}, \\emph{melt}, \\emph{freeze}, \\ldots): matches 4.9\\%, degenerating to always-internal.\n    \\item \\textbf{v3} (12 state-change verbs): matches 2.8\\%, degenerating to always-internal.\n\\end{itemize}\n\nThe structural cause is that ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms. No keyword granularity bridges the gap between near-total and negligible match rates, precluding meaningful routing discrimination. This structural failure motivates observation-based approaches that use environment observations and agent state as routing features rather than action keywords.\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T09:27:00.907189+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T09:27:00.907348+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T09:27:00.907475+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T09:27:00.907600+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "method_v2_draft",
  "type": "paper",
  "description": "Method section v2 draft (LaTeX) for EMNLP 2026 short paper. 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor, Rule-Based Baseline. ~700 words, A-source data (plan-012-full, 11 tasks / 245 episodes).",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md",
  "tags": "['paper', 'method', 'latex', 'v2', 'a-source']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "method_v2_draft",
    "type": "paper",
    "description": "Method section v2 draft (LaTeX) for EMNLP 2026 short paper. 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor, Rule-Based Baseline. ~700 words, A-source data (plan-012-full, 11 tasks / 245 episodes).",
    "project": "simgate-modular-routing",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md",
    "tags": "['paper', 'method', 'latex', 'v2', 'a-source']"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T09:27:00.907743+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_875550\", \"name\": \"method_v2_draft\", \"type\": \"paper\", \"description\": \"Method section v2 draft (LaTeX) for EMNLP 2026 short paper. 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor, Rule-Based Baseline. ~700 words, A-source data (plan-012-full, 11 tasks / 245 episodes).\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft_875550.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T09:26:50.786906+00:00\", \"tags\": [\"paper\", \"method\", \"latex\", \"v2\", \"a-source\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_v2_20260514T092526",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T09:27:00.907914+00:00_

Method section v2 写入 `artifacts/_project/paper/method_v2_draft.md` 并已注册。

结构概要：
- **§3.1 Counterfactual Episode Collection** — 解释 per-step oracle 退化（98.2% tie rate）→ episode-level counterfactual 方案；pure-internal (ReAct) vs pure-deterministic；operational definition of deterministic computation；245 episodes / 11 task types
- **§3.2 Death-Aware Labeling** — 四个 mutually exclusive cases（death asymmetry / both dead / score comparison / tied alive）；label 分布 86/9/150
- **§3.3 Death Avoidance Factor** — DAF 公式、boundary case（Δ_full=0 → undefined）；Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%；Pearson r=0.9698
- **§3.4 Rule-Based Baseline** — 三个 keyword list (v1: 85.8%, v2: 4.9%, v3: 2.8%) 全部退化；以 observation-based approaches 收尾

所有数值均来自 A-source（plan-012-full, 11 tasks / 245 episodes）。Labels 与 experiments_draft.md 中的 `\ref{sec:collection}`, `\ref{sec:daf}`, `\ref{sec:rule}` 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_v2_20260514T092526"
}
```

</details>

---

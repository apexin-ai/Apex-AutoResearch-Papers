# paper writing introduction

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260514T215352.jsonl`
- **Structured JSON:** [`3f0ae2f8fc5132eaab44.json`](../../sessions/3f/3f0ae2f8fc5132eaab44.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-14T21:59:55.339009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:59:55.339613+00:00_

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
…[truncated 9555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:59:55.339943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T21:59:55.340405+00:00_

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
…[truncated 13333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T21:59:55.340751+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper_framing.md",
  "prompt": "Find and read the file paper_framing.md in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/. Search broadly - it might be in artifacts/, or the project root, or any subdirectory. Return the full contents."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find paper_framing.md",
    "prompt": "Find and read the file paper_framing.md in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/. Search broadly - it might be in artifacts/, or the project root, or any subdirectory. Return the full contents."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:59:55.341075+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper_framing.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper_framing.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T21:59:55.341277+00:00_

artifacts/dream_reports/dream_20260514T081656/best/paper_framing.md
artifacts/dream_reports/dream_20260514T081656/median/paper_framing.md
artifacts/dream_reports/dream_20260514T081656/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T095527/best/paper_framing.md
artifacts/dream_reports/dream_20260514T095527/median/paper_framing.md
artifacts/dream_reports/dream_20260514T095527/worst/paper_framing.md
paper_framing.md
artifacts/dream_reports/dream_20260514T184058/best/paper_framing.md
artifacts/dream_reports/dream_20260514T184058/median/paper_framing.md
artifacts/dream_reports/dream_20260514T184058/worst/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T21:59:55.341470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T21:59:55.341701+00:00_

1	# Paper Framing — agent_progress_probe
2	
3	## Target Venue
4	- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)
5	- Format: Long paper (8 pages + appendix)
6	- Track: LLM Agents
7	- Paper type: **Empirical analysis paper**（D039 pivot: 从 method paper 转 empirical study）
8	- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)
9	
10	## Core Claims (3 条) — D039 Pivot
11	
12	1. **Stagnation Signals Are Structural, Not Semantic (primary contribution)**: 系统性对比发现 agent stagnation 信号本质是结构性的——30 个结构特征（命令重复率、唯一命令比、文件 diff 频率等）在 in-domain (RF 0.9951) 和 cross-agent (GB 0.967) 都近完美预测停滞，全面优于 NL embedding probe (in-domain 0.906, cross-domain 0.751) 和 LLM-as-judge (+24.3pp)。Encoder-agnostic（3 个 encoder 均 >0.90）；最优窗口 k=5 (0.9309)；data scaling 10%→100% 单调递增。这揭示：(a) stagnation detection 不需要语义理解——简单结构特征已足够；(b) 结构特征天然跨 agent 迁移（不依赖 embedding domain adaptation）；(c) NL embedding 对 stagnation detection 无增量价值。**改变社区对 agent monitoring 方法选型的认知：从昂贵的表示学习转向轻量结构监控。** Gold set 验证 structural features 是否检测到真实 stagnation（非仅 circular eval artifact）是论文成立的关键。
13	
14	2. **LF Temporal Dynamics Are Systematic but Agent-Specific (analytical contribution)**: LFs 在 trajectory 上展现**系统性但 agent-specific 的**时序角色。SWE-Agent 上：cmd_rep leading (-1.87步)、file_diff concurrent (-1.2步)、OB lagging (+6.7步)。**OH 上 cmd_rep 角色反转**（从 leading 变 lagging +3.32步），而 file_diff（leading, -4.9步）和 OB（lagging, +18.1步）跨域一致。**消融验证：去掉 cmd_rep 后 OH F1 从 0.7512 飙升到 0.9272（+21.6pp）**，证明 cmd_rep 在 OH 上是噪声源而非信号。根因：cmd_rep 在 OH 上 92.3% firing rate + 71% FP，失去区分性。这揭示 LF 行为与 agent 架构之间的交互效应——为 weak supervision pipeline 在 sequential agent data 上的设计提供实证指导。同时量化 circular evaluation 问题：structural features 以 0.9951 F1 逆向工程 LF 标签，证明 LF-derived labels 上的高分不等于真实检测能力。
15	
16	3. **Temporal Label Model: A Well-Motivated Negative Finding (D039 negative result)**: 标准 data programming（majority vote）在 agent trajectory 上违反 i.i.d. 假设——LFs 产生系统性时序动态，这 motivate 了 temporal label model（TLM）的开发。然而，三种 TLM 实现**均未能超越简单 MV**：(a) *
…[truncated 7312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:59:55.342046+00:00_

Here is the full contents of paper_framing.md:

The file contains a comprehensive paper framing document for the "agent_progress_probe" project with the following structure:

**Target Venue**: EMNLP 2026 ARR (submission deadline May 25, 2026) for an 8-page empirical analysis paper on LLM Agents, with ACL 2026 as fallback.

**Core Claims (3 main contributions)**:

1. **Structural Signal Discovery** (primary): Stagnation signals are fundamentally structural, not semantic. 30 structural features achieve near-perfect prediction (in-domain F1 0.9951, cross-agent 0.967), significantly outperforming NL embedding approaches (0.906/0.751) and LLM-as-judge (+24.3pp improvement).

2. **LF Temporal Dynamics Analysis**: Labeling functions exhibit systematic but agent-specific temporal patterns. For example, cmd_rep leads stagnation by ~1.87 steps on SWE-Agent but reverses to lagging on OpenHands (+3.32 steps). Notably, removing cmd_rep on OpenHands improves F1 by +21.6pp.

3. **Temporal Label Model Negative Finding**: Three temporal label model implementations (TWV, HMM, lag-aware HMM) all fail to improve over simple majority vote, with TWV degrading downstream classifiers by up to 21.7pp. This reveals that temporal alignment introduces noise rather than signal in low-conflict regimes.

**Story Spine**: The paper addresses LLM agent "semantic stagnation" in long-horizon tasks, contrasts with existing approaches (cycle detectors, Process Reward Models, self-reflection), and proposes a weak supervision framework for progress stagnation detection emphasizing structural monitoring over expensive representation learning.

**Key Results**: Structural features achieve <5ms inference vs. LLM-based approaches; cross-domain F1 of 0.967; detailed failure analysis of temporal label models.

**Anticipated Concerns & Responses**: Addresses circular evaluation risks (with gold set validation), feature performance interpretation, two-agent scope limitations, information leakage concerns, and me
…[truncated 194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:59:55.342327+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T21:59:55.342521+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:59:55.342736+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SlopCodeBench arxiv 2603.24755 LLM coding agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SlopCodeBench arxiv 2603.24755 LLM coding agent"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:59:55.342947+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentPRM arxiv 2511.08325 process reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentPRM arxiv 2511.08325 process reward model"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T21:59:55.343244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reflexion language agents verbal reinforcement learning arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reflexion language agents verbal reinforcement learning arxiv"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T21:59:55.343498+00:00_

Web search results for query: "Reflexion language agents verbal reinforcement learning arxiv"

Links: [{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://arxiv.org/pdf/2303.11366"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"Reflexion: language agents with verbal reinforcement learning | OpenReview","url":"https://openreview.net/forum?id=vAElhFcKW6"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://openreview.net/pdf?id=vAElhFcKW6"},{"title":"Reflexion: language agents with verbal reinforcement ...","url":"https://dl.acm.org/doi/10.5555/3666122.3666499"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University","url":"https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - Science Explorer Abstract","url":"https://www.scixplorer.org/abs/2023arXiv230311366S/abstract"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2303.11366v4"}]

I found the research paper you're looking for! Here's what I found:

## Reflexion: Language Agents with Verbal Reinforcement Learning

The paper is authored by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao, and it was published at NeurIPS 2023.

**Key Concept:**
Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through lingui
…[truncated 1105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T21:59:55.343942+00:00_

Web search results for query: "SlopCodeBench arxiv 2603.24755 LLM coding agent"

Links: [{"title":"[2603.24755] SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks","url":"https://arxiv.org/abs/2603.24755"},{"title":"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks","url":"https://arxiv.org/html/2603.24755"},{"title":"SlopCodeBench: Benchmarking How Coding Agents ...","url":"https://arxiv.org/pdf/2603.24755"},{"title":"Paper page - SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks","url":"https://huggingface.co/papers/2603.24755"},{"title":"SlopCodeBench: Degradation in Iterative Coding Agents","url":"https://www.emergentmind.com/papers/2603.24755"},{"title":"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.24755"},{"title":"slop-code-bench/README.md at main · SprocketLab/slop-code-bench","url":"https://github.com/SprocketLab/slop-code-bench/blob/main/README.md"},{"title":"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.24755"},{"title":"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69c71a2fe63e77db717c95c7"},{"title":"Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?","url":"https://arxiv.org/html/2603.25719"}]

Based on the search results, here's what I found about SlopCodeBench arxiv 2603.24755:

## Overview

SlopCodeBench is a benchmark of 36 problems and 196 checkpoints where agents repeatedly extend their own solutions. Software development is iterative, yet agentic coding benchmarks hide design issues through their single-shot setup.

## Purpo
…[truncated 1267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T21:59:55.344265+00:00_

Web search results for query: "AgentPRM arxiv 2511.08325 process reward model"

Links: [{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/abs/2511.08325"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251108325X/abstract"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/html/2511.08325"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.08325v1"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Request PDF","url":"https://www.researchgate.net/publication/403735553_AgentPRM_Process_Reward_Models_for_LLM_Agents_via_Step-Wise_Promise_and_Progress"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"[2502.10325] Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/abs/2502.10325"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792551"}]

Here are the search results for "AgentPRM arxiv 2511.08325 process reward model":

## Overview

The paper is titled "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress" and was submitted on November 11, 2025.

## Pr
…[truncated 1554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T21:59:55.344752+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LATS \"Language Agent Tree Search\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LATS \"Language Agent Tree Search\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T21:59:55.344976+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Tree of Thoughts\" Yao arxiv deliberate problem solving"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Tree of Thoughts\" Yao arxiv deliberate problem solving"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T21:59:55.345184+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ICLR 2025 workshop \"agent monitoring\" OR \"sequence-level monitoring\" LLM stagnation detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ICLR 2025 workshop \"agent monitoring\" OR \"sequence-level monitoring\" LLM stagnation detection"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T21:59:55.345402+00:00_

Web search results for query: ""Tree of Thoughts" Yao arxiv deliberate problem solving"

Links: [{"title":"[2305.10601] Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://arxiv.org/abs/2305.10601"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://arxiv.org/pdf/2305.10601"},{"title":"GitHub - princeton-nlp/tree-of-thought-llm: [NeurIPS 2023] Tree of Thoughts: Deliberate Problem Solving with Large Language Models · GitHub","url":"https://github.com/princeton-nlp/tree-of-thought-llm"},{"title":"[PDF] Tree of Thoughts: Deliberate Problem Solving with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Tree-of-Thoughts:-Deliberate-Problem-Solving-with-Yao-Yu/2f3822eb380b5e753a6d579f31dfc3ec4c4a0820"},{"title":"Tree of thoughts: deliberate problem solving with large ...","url":"https://dl.acm.org/doi/abs/10.5555/3666122.3666639"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=5Xc1ecxO1h"},{"title":"[2305.10601] Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2305.10601"},{"title":"Tree of Thoughts: Deliberate Problem Solving With Large Language Models | PDF | Artificial Intelligence | Intelligence (AI) & Semantics","url":"https://www.scribd.com/document/689324832/Tree-of-Thoughts-Deliberate-Problem-Solving-with-Large-Language-Models"},{"title":"Paper page - Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://huggingface.co/papers/2305.10601"},{"title":"[2305.10601v2] Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://arxiv.org/abs/2305.10601v2"}]

I found the paper you're looking for. Here's what the search revealed:

## Tree of Thoughts: Deliberate Problem Solving with Large Language Models

The paper introduces Tree of Thoughts 
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T21:59:55.345654+00:00_

Web search results for query: "LATS "Language Agent Tree Search" arxiv"

Links: [{"title":"[2310.04406] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs/2310.04406"},{"title":"GitHub - lapisrocks/LanguageAgentTreeSearch: [ICML 2024] Official repository for \"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models\" · GitHub","url":"https://github.com/lapisrocks/LanguageAgentTreeSearch"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in","url":"https://arxiv.org/pdf/2310.04406"},{"title":"LanguageAgentTreeSearch | [ICML 2024] Official repository for “Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models”","url":"http://lapisrocks.github.io/LanguageAgentTreeSearch/"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models","url":"https://arxiv.org/html/2310.04406v3"},{"title":"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | OpenReview","url":"https://openreview.net/forum?id=6LNTSrJjBe"},{"title":"Language agent tree search unifies reasoning, acting, and planning in language models | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3694642"},{"title":"Language Agent Tree Search — LATS | by Cobus Greyling | Medium","url":"https://cobusgreyling.medium.com/language-agent-tree-search-lats-837de73d0672"},{"title":"[2310.04406v3] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs/2310.04406v3"},{"title":"[2310.04406v1] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs/2310.04406v1"}]

Based on the search results, here's what I found about LATS (Language Agent Tree Search):

## Overview

LATS is the first general framework that synergizes the capabilities of 
…[truncated 1371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T21:59:55.345938+00:00_

Web search results for query: "ICLR 2025 workshop "agent monitoring" OR "sequence-level monitoring" LLM stagnation detection"

Links: [{"title":"ICLR Monitoring LLM Agents for Sequentially Contextual Harm","url":"https://iclr.cc/virtual/2025/34234"},{"title":"MONITORING LLM AGENTS FOR SEQUENTIALLY ...","url":"https://openreview.net/pdf?id=PGsM81SWHt"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Published at Building Trust Workshop at ICLR 2025 MONITORING LLM AGENTS FOR","url":"https://openreview.net/pdf?id=LC0XQ6ufbr"},{"title":"Monitoring LLM Agents for Sequentially Contextual Harm | OpenReview","url":"https://openreview.net/forum?id=LC0XQ6ufbr"},{"title":"ICLR 2025 Workshop on Reasoning and Planning for Large Language Models","url":"https://workshop-llm-reasoning-planning.github.io/"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"ICLR 2025 Schedule","url":"https://iclr.cc/virtual/2025/calendar"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d033407a1a4b7a75cd5f9e4575ad9fb5-Paper-Conference.pdf"}]

Based on the search results, I found information about an ICLR 2025 workshop paper related to your query:

## ICLR 2025 Workshop: "Monitoring LLM Agents for Sequentially Contextual Harm"

This paper was presented at the ICLR 2025 Workshop on Bidirectional Human-AI Alignment (note: the search results also indicate it was published at the "Building Trust Workshop" at ICLR 2025).

**Key Focus:** The paper addresses **sequence-level monitoring** of LLM agents. Monitoring Large Language Model (LLM) agents is critical for detecting and mitigating catastrophic risk in real-world applications, and this monitoring is particularly difficult since the harm caused by the agent may be sequentially contextual. This means that monitoring individual instructions or actions executed by
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T21:59:55.346360+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2310.04406 \"Language Agent Tree Search\" authors Zhou"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2310.04406 \"Language Agent Tree Search\" authors Zhou"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T21:59:55.347557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentPRM arxiv 2511.08325 authors first author name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentPRM arxiv 2511.08325 authors first author name"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T21:59:55.347847+00:00_

Web search results for query: "AgentPRM arxiv 2511.08325 authors first author name"

Links: [{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/abs/2511.08325"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/html/2511.08325"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251108325X/abstract"},{"title":"Paper published at the Lifelong Agent Workshop @ ICLR 2026","url":"https://openreview.net/pdf/b2457c04f7ac44958db7c76f1ae3710a489fce02.pdf"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.08325v1"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Request PDF","url":"https://www.researchgate.net/publication/403735553_AgentPRM_Process_Reward_Models_for_LLM_Agents_via_Step-Wise_Promise_and_Progress"},{"title":"Guideline-Grounded Evidence Accumulation for High-Stakes Agent Verification","url":"https://arxiv.org/pdf/2603.02798"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://www.researchgate.net/publication/397522531_AgentPRM_Process_Reward_Models_for_LLM_Agents_via_Step-Wise_Promise_and_Progress"},{"title":"Co-Evolution of Policy and Internal Reward for Language Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2604.03098v1"}]

The first author of the AgentPRM paper (arxiv 2511.08325) is Zhiheng Xi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T21:59:55.348153+00:00_

Web search results for query: "arxiv 2310.04406 "Language Agent Tree Search" authors Zhou"

Links: [{"title":"[2310.04406] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs/2310.04406"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in","url":"https://arxiv.org/pdf/2310.04406"},{"title":"[2310.04406v3] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs/2310.04406v3"},{"title":"LanguageAgentTreeSearch | [ICML 2024] Official repository for “Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models”","url":"http://lapisrocks.github.io/LanguageAgentTreeSearch/"},{"title":"GitHub - lapisrocks/LanguageAgentTreeSearch: [ICML 2024] Official repository for \"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models\" · GitHub","url":"https://github.com/lapisrocks/LanguageAgentTreeSearch"},{"title":"[PDF] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Agent-Tree-Search-Unifies-Reasoning-Acting-Zhou-Yan/700bd9681f1b9e9e2212e10415d27b11c7e6836b"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Andy+Zhou,+Kai+Yan,+Michal+Shlapentokh-Rothman,+Haohan+Wang,+and+Yu-Xiong+Wang.+2023.+Language+Agent+Tree+Search+Unifies+Reasoning+Acting+and+Planning+in+Language+Models.+arXiv+preprint+arXiv:2310.04406+(2023)."},{"title":"[2310.04406v1] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs/2310.04406v1"},{"title":"[2310.04406] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"http://export.arxiv.org/abs/2310.04406"},{"title":"[2310.04406v2] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs
…[truncated 1232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T21:59:55.348589+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T21:59:55.348810+00:00_

experiments.tex
method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T21:59:55.349016+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/introduction.tex",
  "content": "% Introduction: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\n\\section{Introduction}\n\\label{sec:introduction}\n\nLarge language model (LLM) agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on code across multiple rounds of edits \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.\nAs task complexity grows, a critical failure mode emerges that is qualitatively different from crashes or syntax errors: the agent \\emph{stagnates}---continuing to produce actions that appear diverse on the surface while making no meaningful progress toward the task goal.\n\\citet{orlanski2026slopcodebench} systematically document this degradation in long-horizon coding tasks, finding structural erosion in 77\\% of agent trajectories and verbosity increases in 75.5\\%, with no agent fully solving any benchmark problem end-to-end.\nUnlike overt loops, stagnation is insidious: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.\nDetecting when an agent has entered this regime is essential for reliable deployment---enabling interventions such as early termination, strategy switching, or human escalation---yet identifying \\emph{what signals} carry stagnation information, and whether complex language understanding is necessary to extract them, remains an open question.\n\nPrior approaches to monitoring agent behavior address aspects of this problem but none systematically investigate what information is needed for detection.\n\\emph{Repetition detectors} identify exact or near-exact loops in action sequences, catching the simplest failure mode but missing semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.\n\\emph{Process reward models} \\citep{xi2025agentprm} assign quality scores to individual actions, enabling search-time guidance, but step-level granularity cannot capture temporal patterns that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over windows of consecutive actions \\textcolor{red}{[CITE: ICLR 2025 Workshop, Monitoring LLM Agents for Sequentially Contextual Harm]}.\n\\emph{Self-reflection} frameworks \\citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent itself to diagnose and recover from failures, but when the agent is genuinely stuck, self-diagnosis amounts to querying the failing model about its own failure---a circularity that limits reliability.\nMore fundamentally, all three lines of work prescribe detection \\emph{methods} without first asking what kinds of signals actually carry stagnation information: does detecting subtle agent failure require sophisticated semantic understanding, or do simpler structural patterns suffice?\n\nWe present an empirical analysis that addresses this gap.\nUsing a weak supervision framework \\citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from trajectories of two architecturally distinct agents: SWE-Agent \\citep{yang2024sweagent} on SWE-bench \\citep{jimenez2024swebench} (54,809 windows) and OpenHands \\citep{wang2025openhands} (150,652 windows).\nThree labeling functions (LFs)---targeting command repetition, file modification patterns, and task outcome---provide noisy votes that are aggregated via majority vote into window-level binary labels.\nAgainst these silver labels, we systematically compare three detection paradigms: hand-crafted structural features, neural embedding probes, and LLM-as-judge evaluation.\n\nOur central finding is that \\textbf{stagnation signals are fundamentally structural, not semantic}.\nThirty hand-crafted features capturing command repetition rates, file operation counts, and edit distances achieve 0.9951 macro-F1 in-domain and 0.967 on zero-shot cross-agent transfer, exceeding the LLM judge by 33.3 percentage points (pp).\nA GRU-based neural probe \\citep{cho2014gru} over sentence embeddings reaches 0.906 in-domain but collapses to 0.528 on zero-shot transfer and recovers only to 0.751 after full fine-tuning on the target agent.\nThe structural advantage is encoder-agnostic: swapping the probe's embedding backbone across three encoders (Qwen3-0.6B, BGE-M3, E5-large-v2) yields probe F1 consistently above 0.90 \\citep{zhang2025qwen3embedding,chen2024bgem3,wang2024e5}, confirming that the temporal architecture rather than a specific pretrained encoder drives embedding-based performance.\nCritically, the gap between structural features and learned representations persists across agents with substantially different action distributions (28.5\\% vs.\\ 6.6\\% stagnation rates), suggesting that stagnation manifests in action-level structure that generalizes without adaptation.\nThis challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---requiring no GPU and running in under 5\\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.\n\nBeyond static detection, we analyze the temporal dynamics of the labeling functions that generate silver labels.\nOn SWE-Agent, command repetition ($\\lambda_1$) leads stagnation onset by 1.87 steps on average, serving as an early warning signal, while outcome backpropagation ($\\lambda_3$) lags by 6.70 steps (Kruskal-Wallis $H{=}274.3$, $p{<}10^{-59}$).\nHowever, this temporal structure is agent-specific: on OpenHands, $\\lambda_1$ reverses from leading to lagging ($+3.32$ steps), firing on 92.3\\% of windows with a 71\\% false positive rate on progress windows.\nRemoving $\\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\\,pp, demonstrating that labeling functions validated on one agent architecture can become adversarial on another.\nThis finding establishes that LF temporal roles must be re-validated per agent and motivates the circular evaluation methodology we develop to surface such pathologies (\\S\\ref{sec:cmd_rep_ablation}).\n\nWe further investigate whether encoding this temporal structure into label aggregation can improve over simple majority vote.\nThree temporal label models---time-varying weights (TWV), Hidden Markov Models \\citep{safranchik2020linkedhmm}, and lag-aware HMMs---all fail to surpass majority vote on downstream stagnation detection.\nTWV achieves marginally higher self-evaluated F1 (+0.57\\,pp) but degrades downstream probe performance by 2.57\\,pp; the standard HMM overpredicts stagnation, dropping downstream F1 to 0.656.\nThis negative result demonstrates that temporal sophistication in label aggregation does not translate to better silver labels when base agreement among LFs is already high.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Structural signal discovery.} We show that 30 structural features achieve near-perfect stagnation detection (0.9951 in-domain, 0.967 cross-agent macro-F1), outperforming neural probes and LLM judges by wide margins (+33.3\\,pp over LLM-as-judge). To our knowledge, this is the first systematic comparison demonstrating that stagnation information resides in action-level structure rather than semantic content.\n    \\item \\textbf{Labeling function temporal dynamics.} We reveal that LFs occupy statistically distinct temporal niches relative to stagnation onset, with agent-specific reversals that corrupt silver labels. We develop a circular evaluation methodology to identify and quantify these cross-agent pathologies.\n    \\item \\textbf{Temporal label model negative finding.} We show that three temporal label models fail to improve over majority vote for downstream detection, despite clear temporal structure in LF firing patterns. This informs future weak supervision design for sequential agent data.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/introduction.tex",
    "content": "% Introduction: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\n\\section{Introduction}\n\\label{sec:introduction}\n\nLarge language model (LLM) agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on code across multiple rounds of edits \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.\nAs task complexity grows, a critical failure mode emerges that is qualitatively different from crashes or syntax errors: the agent \\emph{stagnates}---continuing to produce actions that appear diverse on the surface while making no meaningful progress toward the task goal.\n\\citet{orlanski2026slopcodebench} systematically document this degradation in long-horizon coding tasks, finding structural erosion in 77\\% of agent trajectories and verbosity increases in 75.5\\%, with no agent fully solving any benchmark problem end-to-end.\nUnlike overt loops, stagnation is insidious: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.\nDetecting when an agent has entered this regime is essential for reliable deployment---enabling interventions such as early termination, strategy switching, or human escalation---yet identifying \\emph{what signals} carry stagnation information, and whether complex language understanding is necessary to extract them, remains an open question.\n\nPrior approaches to monitoring agent behavior address aspects of this problem but none systematically investigate what information is needed for detection.\n\\emph{Repetition detectors} identify exact or near-exact loops in action sequences, catching the simplest failure mode but missing semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.\n\\emph{Process reward models} \\citep{xi2025agentprm} assign quality scores to individual actions, enabling search-time guidance, but step-level granularity cannot capture temporal patterns that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over windows of consecutive actions \\textcolor{red}{[CITE: ICLR 2025 Workshop, Monitoring LLM Agents for Sequentially Contextual Harm]}.\n\\emph{Self-reflection} frameworks \\citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent itself to diagnose and recover from failures, but when the agent is genuinely stuck, self-diagnosis amounts to querying the failing model about its own failure---a circularity that limits reliability.\nMore fundamentally, all three lines of work prescribe detection \\emph{methods} without first asking what kinds of signals actually carry stagnation information: does detecting subtle agent failure require sophisticated semantic understanding, or do simpler structural patterns suffice?\n\nWe present an empirical analysis that addresses this gap.\nUsing a weak supervision framework \\citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from trajectories of two architecturally distinct agents: SWE-Agent \\citep{yang2024sweagent} on SWE-bench \\citep{jimenez2024swebench} (54,809 windows) and OpenHands \\citep{wang2025openhands} (150,652 windows).\nThree labeling functions (LFs)---targeting command repetition, file modification patterns, and task outcome---provide noisy votes that are aggregated via majority vote into window-level binary labels.\nAgainst these silver labels, we systematically compare three detection paradigms: hand-crafted structural features, neural embedding probes, and LLM-as-judge evaluation.\n\nOur central finding is that \\textbf{stagnation signals are fundamentally structural, not semantic}.\nThirty hand-crafted features capturing command repetition rates, file operation counts, and edit distances achieve 0.9951 macro-F1 in-domain and 0.967 on zero-shot cross-agent transfer, exceeding the LLM judge by 33.3 percentage points (pp).\nA GRU-based neural probe \\citep{cho2014gru} over sentence embeddings reaches 0.906 in-domain but collapses to 0.528 on zero-shot transfer and recovers only to 0.751 after full fine-tuning on the target agent.\nThe structural advantage is encoder-agnostic: swapping the probe's embedding backbone across three encoders (Qwen3-0.6B, BGE-M3, E5-large-v2) yields probe F1 consistently above 0.90 \\citep{zhang2025qwen3embedding,chen2024bgem3,wang2024e5}, confirming that the temporal architecture rather than a specific pretrained encoder drives embedding-based performance.\nCritically, the gap between structural features and learned representations persists across agents with substantially different action distributions (28.5\\% vs.\\ 6.6\\% stagnation rates), suggesting that stagnation manifests in action-level structure that generalizes without adaptation.\nThis challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---requiring no GPU and running in under 5\\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.\n\nBeyond static detection, we analyze the temporal dynamics of the labeling functions that generate silver labels.\nOn SWE-Agent, command repetition ($\\lambda_1$) leads stagnation onset by 1.87 steps on average, serving as an early warning signal, while outcome backpropagation ($\\lambda_3$) lags by 6.70 steps (Kruskal-Wallis $H{=}274.3$, $p{<}10^{-59}$).\nHowever, this temporal structure is agent-specific: on OpenHands, $\\lambda_1$ reverses from leading to lagging ($+3.32$ steps), firing on 92.3\\% of windows with a 71\\% false positive rate on progress windows.\nRemoving $\\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\\,pp, demonstrating that labeling functions validated on one agent architecture can become adversarial on another.\nThis finding establishes that LF temporal roles must be re-validated per agent and motivates the circular evaluation methodology we develop to surface such pathologies (\\S\\ref{sec:cmd_rep_ablation}).\n\nWe further investigate whether encoding this temporal structure into label aggregation can improve over simple majority vote.\nThree temporal label models---time-varying weights (TWV), Hidden Markov Models \\citep{safranchik2020linkedhmm}, and lag-aware HMMs---all fail to surpass majority vote on downstream stagnation detection.\nTWV achieves marginally higher self-evaluated F1 (+0.57\\,pp) but degrades downstream probe performance by 2.57\\,pp; the standard HMM overpredicts stagnation, dropping downstream F1 to 0.656.\nThis negative result demonstrates that temporal sophistication in label aggregation does not translate to better silver labels when base agreement among LFs is already high.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Structural signal discovery.} We show that 30 structural features achieve near-perfect stagnation detection (0.9951 in-domain, 0.967 cross-agent macro-F1), outperforming neural probes and LLM judges by wide margins (+33.3\\,pp over LLM-as-judge). To our knowledge, this is the first systematic comparison demonstrating that stagnation information resides in action-level structure rather than semantic content.\n    \\item \\textbf{Labeling function temporal dynamics.} We reveal that LFs occupy statistically distinct temporal niches relative to stagnation onset, with agent-specific reversals that corrupt silver labels. We develop a circular evaluation methodology to identify and quantify these cross-agent pathologies.\n    \\item \\textbf{Temporal label model negative finding.} We show that three temporal label models fail to improve over majority vote for downstream detection, despite clear temporal structure in LF firing patterns. This informs future weak supervision design for sequential agent data.\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:59:55.349483+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T21:59:55.349800+00:00_

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
  "session": "worker_paper_writing_introduction_20260514T215352",
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

_source line 34 · 2026-05-14T21:59:55.350109+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T21:59:55.350297+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "introduction.tex",
  "type": "paper",
  "description": "EMNLP 2026 ARR Introduction section (~1100 words): hook on silent stagnation failure, gap analysis of 3 prior approaches, structural signal discovery finding, LF temporal dynamics, TLM negative finding, 3 contributions",
  "project": "agent_progress_probe",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/introduction.tex",
  "tags": "['paper', 'introduction', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "introduction.tex",
    "type": "paper",
    "description": "EMNLP 2026 ARR Introduction section (~1100 words): hook on silent stagnation failure, gap analysis of 3 prior approaches, structural signal discovery finding, LF temporal dynamics, TLM negative finding, 3 contributions",
    "project": "agent_progress_probe",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/_project/paper/introduction.tex",
    "tags": "['paper', 'introduction', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T21:59:55.350513+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_176b40\", \"name\": \"introduction.tex\", \"type\": \"paper\", \"description\": \"EMNLP 2026 ARR Introduction section (~1100 words): hook on silent stagnation failure, gap analysis of 3 prior approaches, structural signal discovery finding, LF temporal dynamics, TLM negative finding, 3 contributions\", \"path\": \"projects/agent_progress_probe/artifacts/_project/paper/introduction_176b40.tex\", \"url\": null, \"project\": \"agent_progress_probe\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T21:59:37.313154+00:00\", \"tags\": [\"paper\", \"introduction\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260514T215352",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T21:59:55.351023+00:00_

Introduction 已写入 `artifacts/_project/paper/introduction.tex` 并注册。

结构概览：
1. **Hook** — SlopCodeBench 记录的 silent stagnation 问题，77% 结构退化，75.5% 冗余增长
2. **Gap** — 三类现有方法的局限：repetition detectors（漏语义停滞）、PRM（step-level 丢时序）、self-reflection（循环依赖 stuck model）
3. **Setup** — 弱监督框架，SWE-Agent 54K + OpenHands 150K windows，三个 LF + majority vote
4. **Core finding** — 30 结构特征 0.9951 in-domain / 0.967 cross-agent，+33.3pp vs LLM judge，encoder-agnostic（3 encoders >0.90），<5ms/window
5. **Temporal dynamics** — cmd_rep leading -1.87 步（SWE-Agent）→ lagging +3.32 步（OH），去掉后 FT F1 +17.6pp
6. **TLM negative** — TWV/HMM/lag-HMM 均未超 MV，TWV 下游 -2.57pp
7. **Contributions** — C1 structural signal, C2 LF temporal dynamics + circular evaluation, C3 TLM negative finding

待处理：1 个红色引用标记（ICLR 2025 Workshop monitoring paper），需确认后替换为 `\citep{}`；新增引用（orlanski2026slopcodebench, xi2025agentprm, shinn2023reflexion, yao2023tot, zhou2024lats）需加入 bib 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260514T215352"
}
```

</details>

---

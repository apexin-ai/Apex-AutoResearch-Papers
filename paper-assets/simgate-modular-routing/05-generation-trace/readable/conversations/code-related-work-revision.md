# code related work revision

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_code_related-work-revision_20260514T010609.jsonl`
- **Structured JSON:** [`1a39283d6fd01fc8b3c2.json`](../../sessions/1a/1a39283d6fd01fc8b3c2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-14T01:08:02.938747+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_related-work-revision_20260514T010609",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T01:08:02.939161+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_related-work-revision_20260514T010609",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T01:08:02.939341+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_related-work-revision_20260514T010609",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T01:08:02.939664+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml\", \"content\": \"# Literature Map — simgate-modular-routing\\n# Last updated: 2026-05-14\\n# Scan scope: 2025-2026 incremental scan + existing references from paper_framing.md\\n\\n# ============================================================\\n# CATEGORY: Direct Competitors (novelty threat)\\n# ============================================================\\ndirect_competitors: []\\n# None found. No 2025-2026 paper claims death/safety avoidance\\n# as the dominant routing signal in LLM agent systems.\\n\\n# ============================================================\\n# CATEGORY: ScienceWorld Agent Baselines (must-cite)\\n# ============================================================\\nscienceworld_baselines:\\n  - id: cogrouter-2026\\n    title: \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv:2602.12662, Feb 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      SOTA on ScienceWorld (82.3% with Qwen2.5-7B). Routes between cognitive\\n      depth levels (instinct to strategic planning) via CoPO, not between\\n      internal vs deterministic computation. Does not analyze WHAT drives\\n      routing signal. Cite as SOTA baseline and adaptive computation related work.\\n    our_differentiation: >\\n      CogRouter optimizes HOW MUCH to think; we analyze WHAT routing learns\\n      (death avoidance = 99%). Different routing dimensions (depth vs modality).\\n\\n  - id: itp-2026\\n    title: \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv:2601.08955, Jan 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Extends POIMDP with world model lookahead on ScienceWorld/ALFWorld/
…[truncated 11514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_related-work-revision_20260514T010609",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T01:08:02.939847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/related_work_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_related-work-revision_20260514T010609",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/related_work_draft.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T01:08:02.940060+00:00_

1	# Related Work — Draft v1
2	
3	\section{Related Work}
4	
5	\paragraph{Tool-Use Learning.}
6	A line of work teaches LLMs when and how to invoke external tools.
7	Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering, while ART \cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.
8	More recently, ReTool \cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.
9	Our work differs along three axes: (1) we generate routing labels via \emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL-based signals; (2) we frame routing as \emph{catastrophic failure prevention} rather than general tool selection; and (3) we train an explicit lightweight router decoupled from the backbone LLM, enabling diagnostic analysis of what the routing signal encodes.
10	
11	\paragraph{Adaptive Computation.}
12	Several recent methods adapt reasoning effort per step.
13	CogRouter \cite{cogrouter-2026} achieves 82.3\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\%.
14	Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.
15	These methods route \emph{how much} to reason; we route \emph{which modality} to use (internal LLM reasoning vs.\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\sim}99\%$ of the learned routing signal.
16	
17	\paragraph{World Model Routing.}
18	ITP \cite{itp-2026} augments agents with LLM-based world model lookahead, ad
…[truncated 993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_related-work-revision_20260514T010609",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T01:08:02.940380+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/related_work_draft.md",
  "content": "# Related Work — Draft v2\n&lt;!-- ReAct citation moved to Introduction to free space (short paper ~400 word budget) -->\n\n\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering, ART \\cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \\cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.\nReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.\nConcurrently, MTRouter \\cite{mtrouter-2026} routes between different LLMs on ScienceWorld for cost-quality tradeoff; unlike our work, it selects \\emph{which model} to call rather than \\emph{which reasoning modality} to use, and does not analyze routing signal composition.\nOur routing labels come from \\emph{episode-level counterfactual analysis}---complete trajectories under competing strategies---and frame routing as catastrophic failure prevention rather than tool selection or cost optimization.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\\sim}99\\%$ of the learned routing signal.\n\n\\paragraph{World Model Routing and Environment Simulation.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nEnvSimBench \\cite{envsimbench-2025} diagnoses a related limitation: LLMs exhibit a ``state-change cliff,'' failing catastrophically when multiple state variables require simultaneous updates.\nOur deterministic computation modality sidesteps this cliff by providing \\emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance.\n\n\\paragraph{Agent Failure Analysis.}\n\\citet{llm-agentic-failures-2025} qualitatively identify four failure archetypes in agentic LLM scenarios; our counterfactual methodology complements this by quantitatively isolating the dominant failure mechanism---death avoidance accounts for ${\\sim}99\\%$ of the routing signal on ScienceWorld.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_related-work-revision_20260514T010609",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/related_work_draft.md",
    "content": "# Related Work — Draft v2\n&lt;!-- ReAct citation moved to Introduction to free space (short paper ~400 word budget) -->\n\n\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering, ART \\cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \\cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.\nReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.\nConcurrently, MTRouter \\cite{mtrouter-2026} routes between different LLMs on ScienceWorld for cost-quality tradeoff; unlike our work, it selects \\emph{which model} to call rather than \\emph{which reasoning modality} to use, and does not analyze routing signal composition.\nOur routing labels come from \\emph{episode-level counterfactual analysis}---complete trajectories under competing strategies---and frame routing as catastrophic failure prevention rather than tool selection or cost optimization.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\\sim}99\\%$ of the learned routing signal.\n\n\\paragraph{World Model Routing and Environment Simulation.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nEnvSimBench \\cite{envsimbench-2025} diagnoses a related limitation: LLMs exhibit a ``state-change cliff,'' failing catastrophically when multiple state variables require simultaneous updates.\nOur deterministic computation modality sidesteps this cliff by providing \\emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance.\n\n\\paragraph{Agent Failure Analysis.}\n\\citet{llm-agentic-failures-2025} qualitatively identify four failure archetypes in agentic LLM scenarios; our counterfactual methodology complements this by quantitatively isolating the dominant failure mechanism---death avoidance accounts for ${\\sim}99\\%$ of the routing signal on ScienceWorld.\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T01:08:02.940615+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/related_work_draft.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_related-work-revision_20260514T010609",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-14T01:08:02.940784+00:00_

修订完成。变更摘要：

**1. MTRouter** — Tool-Use Learning 段末尾新增 1 句，区分"选模型 vs 选推理模态"，强调我们分析 signal composition 而非优化 cost。同时精简了原 "Our work differs" 句，去掉三轴罗列改为更紧凑的表述。

**2. EnvSimBench** — World Model Routing 段（已更名为 "World Model Routing and Environment Simulation"）新增 1 句，引入 state-change cliff，形成因果链：EnvSimBench 诊断 WHERE LLMs fail → 我们的 deterministic modality sidesteps this cliff → counterfactual 揭示这只 matters for death avoidance。

**3. LLM Agentic Failures** — 新增 Agent Failure Analysis 段，1 句话：他们定性分类 4 种 failure archetypes，我们定量隔离 dominant failure mechanism (death = 99%)。

**空间管理** — 移除 Agent Frameworks 段（ReAct 引用标注移至 Introduction），全文约 340 words，控制在 400 以内。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_related-work-revision_20260514T010609"
}
```

</details>

---

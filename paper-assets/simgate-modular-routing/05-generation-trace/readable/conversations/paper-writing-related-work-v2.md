# paper writing related work v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_writing_related_work_v2_20260514T112612.jsonl`
- **Structured JSON:** [`1a345c29fbbd3bbbbcab.json`](../../sessions/1a/1a345c29fbbd3bbbbcab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-14T11:27:55.700966+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T11:27:55.701415+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T11:27:55.701672+00:00_

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
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
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

_source line 4 · 2026-05-14T11:27:55.702118+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml\", \"content\": \"# Literature Map — simgate-modular-routing\\n# Last updated: 2026-05-14\\n# Scan scope: 2025-2026 incremental scan + existing references from paper_framing.md\\n\\n# ============================================================\\n# CATEGORY: Direct Competitors (novelty threat)\\n# ============================================================\\ndirect_competitors: []\\n# None found. No 2025-2026 paper claims death/safety avoidance\\n# as the dominant routing signal in LLM agent systems.\\n\\n# ============================================================\\n# CATEGORY: ScienceWorld Agent Baselines (must-cite)\\n# ============================================================\\nscienceworld_baselines:\\n  - id: cogrouter-2026\\n    title: \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv:2602.12662, Feb 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      SOTA on ScienceWorld (82.3% with Qwen2.5-7B). Routes between cognitive\\n      depth levels (instinct to strategic planning) via CoPO, not between\\n      internal vs deterministic computation. Does not analyze WHAT drives\\n      routing signal. Cite as SOTA baseline and adaptive computation related work.\\n    our_differentiation: >\\n      CogRouter optimizes HOW MUCH to think; we analyze WHAT routing learns\\n      (death avoidance = 99%). Different routing dimensions (depth vs modality).\\n\\n  - id: itp-2026\\n    title: \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv:2601.08955, Jan 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Extends POIMDP with world model lookahead on ScienceWorld/ALFWorld/
…[truncated 11514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T11:27:55.702457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_draft.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T11:27:55.702706+00:00_

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
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T11:27:55.702942+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T11:27:55.703300+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (11 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd
…[truncated 11976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T11:27:55.703568+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "write_paper_section",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "write_paper_section",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T11:27:55.703746+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T11:27:55.703932+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+write_paper_section",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+write_paper_section",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T11:27:55.704128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T11:27:55.704311+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T11:27:55.704485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T11:27:55.704658+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "write_paper_section",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "glob": "*.py",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Grep",
  "tool_args": {
    "pattern": "write_paper_section",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
    "glob": "*.py",
    "head_limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T11:27:55.704822+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T11:27:55.705033+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "write_paper_section",
  "path": "/home/ubuntu/agent-ml-research",
  "glob": "*.py",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Grep",
  "tool_args": {
    "pattern": "write_paper_section",
    "path": "/home/ubuntu/agent-ml-research",
    "glob": "*.py",
    "head_limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T11:27:55.705236+00:00_

Found 10 files limit: 10
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/core/tool_registry.py
/home/ubuntu/agent-ml-research/core/tools/architecture.py
/home/ubuntu/agent-ml-research/tests/test_section_writing.py
/home/ubuntu/agent-ml-research/tests/test_patch_mode.py
/home/ubuntu/agent-ml-research/tests/test_provenance.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_full_draft_e2e.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_patch_e2e.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_reframe_e2e.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_tools.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T11:27:55.705434+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def write_paper_section|\"write_paper_section\"",
  "path": "/home/ubuntu/agent-ml-research/core/tools/architecture.py",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def write_paper_section|\"write_paper_section\"",
    "path": "/home/ubuntu/agent-ml-research/core/tools/architecture.py",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T11:27:55.705623+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T11:27:55.705810+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "write_paper_section",
  "path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "output_mode": "content",
  "-C": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Grep",
  "tool_args": {
    "pattern": "write_paper_section",
    "path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
    "output_mode": "content",
    "-C": "5"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T11:27:55.706046+00:00_

2082-# ---------------------------------------------------------------------------
2083-# Paper provenance tools
2084-# ---------------------------------------------------------------------------
2085-
2086-@mcp.tool()
2087:def write_paper_section(
2088-    project: str,
2089-    section: str,
2090-    content: str,
2091-    claims: list[dict] | None = None,
2092-    table_cells: list[dict] | None = None,
--
2100-        content: LaTeX content.
2101-        claims: List of {text, type, evidence[], decisions[]} for provenance.
2102-        table_cells: List of {table_id, row, col, value, source{exp_id, metric}}.
2103-        figures: List of {figure_id, caption, type, source, output_path}.
2104-    """
2105:    from core.tools.provenance import write_paper_section as _wps
2106-    result = _wps(project, section, content, claims=claims,
2107-                  table_cells=table_cells, figures=figures)
2108-    return _tool_result_to_str(result)
2109-
2110-
--
2776-    """Write a project file (unified entry point, strict whitelist).
2777-
2778-    Writable: memory.md, writing_plan.yaml, paper_framing.md. Other files
2779-    have dedicated tools: ROADMAP.md → update_roadmap, ideas.md →
2780-    append_idea/move_idea, decisions.yaml → log_decision, report.md →
2781:    auto-generated, paper sections → write_paper_section / edit_paper_section.
2782-
2783-    Args:
2784-        project: Project name.
2785-        content: Full file content.
2786-        file: File name to write.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T11:27:55.706285+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__write_paper_section",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__write_paper_section",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T11:27:55.706474+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T11:27:55.706743+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2.md",
  "content": "\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering;\nART \\cite{art-2023} delegates tool selection to LLM reasoning chains;\nChameleon \\cite{chameleon-2024} composes diverse modules under LLM-as-planner orchestration;\nand ReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation for mathematical reasoning.\nThese methods learn \\emph{which tool} to use or \\emph{whether} to use one, but do not analyze what signal drives the learned routing policy.\nWe differ in three ways: (1)~we generate labels via \\emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL signals; (2)~we frame routing as catastrophic-failure prevention rather than general tool selection; and (3)~by training an explicit lightweight router decoupled from the backbone, we can diagnose \\emph{what} the routing signal encodes, revealing that ${\\sim}90\\%$ is death avoidance.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves state-of-the-art on ScienceWorld (82.3\\%) by routing among cognitive depth levels via Cooperative Policy Optimization.\nARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort, reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation).\nMore importantly, none quantify the composition of their routing signal.\nOur counterfactual decomposition reveals that death avoidance accounts for ${\\sim}90\\%$ of the performance gap---the contribution is this empirical finding and the diagnostic methodology, not the router architecture itself.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nOur deterministic computation modality provides \\emph{exact} state transitions, and episode-level counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance: non-death performance is near-equivalent across modalities ($\\Delta_\\text{nd}$ accounts for only 9.6\\% of the full gap).\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents, including our internal-reasoning baseline.\nScienceWorld \\cite{scienceworld-2022} provides the evaluation environment: 30 science task types requiring multi-step reasoning over rule-governed state transitions with catastrophic failure penalties.\nMTRouter \\cite{mtrouter-2026} routes between different LLMs on ScienceWorld for cost optimization, but targets model-level selection rather than reasoning-modality selection.\nOur work complements these efforts by asking a different question: not \\emph{how} to build a better agent framework, but \\emph{what} a learned router actually captures.\nThe answer---that routing signal is dominated by catastrophic-failure prevention---suggests that future agent designs should prioritize safety-aware computation allocation over general-purpose reasoning enhancement.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2.md",
    "content": "\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering;\nART \\cite{art-2023} delegates tool selection to LLM reasoning chains;\nChameleon \\cite{chameleon-2024} composes diverse modules under LLM-as-planner orchestration;\nand ReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation for mathematical reasoning.\nThese methods learn \\emph{which tool} to use or \\emph{whether} to use one, but do not analyze what signal drives the learned routing policy.\nWe differ in three ways: (1)~we generate labels via \\emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL signals; (2)~we frame routing as catastrophic-failure prevention rather than general tool selection; and (3)~by training an explicit lightweight router decoupled from the backbone, we can diagnose \\emph{what} the routing signal encodes, revealing that ${\\sim}90\\%$ is death avoidance.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves state-of-the-art on ScienceWorld (82.3\\%) by routing among cognitive depth levels via Cooperative Policy Optimization.\nARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort, reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation).\nMore importantly, none quantify the composition of their routing signal.\nOur counterfactual decomposition reveals that death avoidance accounts for ${\\sim}90\\%$ of the performance gap---the contribution is this empirical finding and the diagnostic methodology, not the router architecture itself.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nOur deterministic computation modality provides \\emph{exact} state transitions, and episode-level counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance: non-death performance is near-equivalent across modalities ($\\Delta_\\text{nd}$ accounts for only 9.6\\% of the full gap).\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents, including our internal-reasoning baseline.\nScienceWorld \\cite{scienceworld-2022} provides the evaluation environment: 30 science task types requiring multi-step reasoning over rule-governed state transitions with catastrophic failure penalties.\nMTRouter \\cite{mtrouter-2026} routes between different LLMs on ScienceWorld for cost optimization, but targets model-level selection rather than reasoning-modality selection.\nOur work complements these efforts by asking a different question: not \\emph{how} to build a better agent framework, but \\emph{what} a learned router actually captures.\nThe answer---that routing signal is dominated by catastrophic-failure prevention---suggests that future agent designs should prioritize safety-aware computation allocation over general-purpose reasoning enhancement.\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T11:27:55.707040+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T11:27:55.707244+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "related_work_v2",
  "type": "paper",
  "description": "Related Work v2: fixed DAF 99→90%, expanded Agent Frameworks (ScienceWorld, MTRouter), strengthened differentiation per paragraph",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2.md",
  "tags": "['paper', 'related-work', 'v2']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "related_work_v2",
    "type": "paper",
    "description": "Related Work v2: fixed DAF 99→90%, expanded Agent Frameworks (ScienceWorld, MTRouter), strengthened differentiation per paragraph",
    "project": "simgate-modular-routing",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2.md",
    "tags": "['paper', 'related-work', 'v2']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T11:27:55.707456+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_7196ef\", \"name\": \"related_work_v2\", \"type\": \"paper\", \"description\": \"Related Work v2: fixed DAF 99→90%, expanded Agent Frameworks (ScienceWorld, MTRouter), strengthened differentiation per paragraph\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2_7196ef.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T11:27:46.313955+00:00\", \"tags\": [\"paper\", \"related-work\", \"v2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_v2_20260514T112612",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-14T11:27:55.707732+00:00_

v2 已保存并注册 (`art_20260514_7196ef`)。

**变更摘要：**

| 修改项 | 具体变更 |
|--------|---------|
| 数字修正 | `~99%` → `~90%`（出现在 Adaptive Computation 和 Tool-Use Learning 段） |
| Agent Frameworks 扩展 | 加入 `\cite{scienceworld-2022}`（Wang et al. 2022）和 `\cite{mtrouter-2026}`，段落从2句扩到5句 |
| 差异化增强 | Tool-Use：加"none analyze what signal drives routing"；Adaptive Comp：加"none quantify the composition of their routing signal" + "contribution is finding + methodology, not architecture"；World Model：加 `Δ_nd` 9.6% 数据；Agent Frameworks：结尾提出 safety-aware computation allocation 方向性结论 |
| 新引用 | `mtrouter-2026`、`scienceworld-2022`（均在 literature_map.yaml 中） |
| 篇幅 | ~430 words，符合 400-500 目标 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_v2_20260514T112612"
}
```

</details>

---

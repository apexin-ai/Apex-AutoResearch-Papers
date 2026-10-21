# paper writing related work v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_writing_related_work_v2_20260514T112612.log`
- **Structured JSON:** [`05d557201cd8ba1e135c.json`](../../sessions/05/05d557201cd8ba1e135c.json)

## Before a recorded user message

42 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "831c85f4-97d7-442e-b4a2-4d18060c5816",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779303600,
    "rateLimitType": "seven_day",
    "utilization": 0.34,
    "isUsingOverage": false
  },
  "uuid": "8552b848-9c05-4c9f-9526-03309e7102cc",
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current draft and the literature map in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "036f2097-96db-4ff1-b205-73a03a5df2d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V27VCvutfu8NSwruzDNJoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11528,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11528
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ERPoR71kY9nb3tXMZdjzBJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "414bb657-d6e0-4176-b2dd-5713dda0b7c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V27VCvutfu8NSwruzDNJoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11528,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11528
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T11:26:28.072Z_

<details><summary>↩ Tool result · `toolu_01ERPoR71kY9nb3tXMZdjzBJ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "d2500fed-20aa-400c-b89a-f2f952057e60",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the current draft and the literature map in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "d9fd660e-4a4c-4022-8fa3-b41e78e3c506",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ki7hvghagkTHnM2K74BMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1327,
      "cache_read_input_tokens": 23369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1327
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FZw2sWcJVFt2Tkf4rNHp3J`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "c5490154-5e6f-4147-8041-d631c10e5a2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ki7hvghagkTHnM2K74BMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1327,
      "cache_read_input_tokens": 23369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1327
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T11:26:31.616Z_

<details><summary>↩ Tool result · `toolu_01FZw2sWcJVFt2Tkf4rNHp3J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml\", \"content\": \"# Literature Map — simgate-modular-routing\\n# Last updated: 2026-05-14\\n# Scan scope: 2025-2026 incremental scan + existing references from paper_framing.md\\n\\n# ============================================================\\n# CATEGORY: Direct Competitors (novelty threat)\\n# ============================================================\\ndirect_competitors: []\\n# None found. No 2025-2026 paper claims death/safety avoidance\\n# as the dominant routing signal in LLM agent systems.\\n\\n# ============================================================\\n# CATEGORY: ScienceWorld Agent Baselines (must-cite)\\n# ============================================================\\nscienceworld_baselines:\\n  - id: cogrouter-2026\\n    title: \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv:2602.12662, Feb 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      SOTA on ScienceWorld (82.3% with Qwen2.5-7B). Routes between cognitive\\n      depth levels (instinct to strategic planning) via CoPO, not between\\n      internal vs deterministic computation. Does not analyze WHAT drives\\n      routing signal. Cite as SOTA baseline and adaptive computation related work.\\n    our_differentiation: >\\n      CogRouter optimizes HOW MUCH to think; we analyze WHAT routing learns\\n      (death avoidance = 99%). Different routing dimensions (depth vs modality).\\n\\n  - id: itp-2026\\n    title: \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv:2601.08955, Jan 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Extends POIMDP with world model lookahead on ScienceWorld/ALFWorld/WebShop.\\n      Adaptive lookahead horizon based on task progress. Uses approximate LLM\\n      world model, not deterministic simulator.\\n    our_differentiation: >\\n      ITP routes lookahead depth using world model; we route modality (internal\\n      vs deterministic) and discover death avoidance dominates. ITP world\\n      model is approximate; our deterministic computation is exact.\\n\\n  - id: mtrouter-2026\\n    title: \\\"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv:2604.23530, ACL 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Multi-turn routing between different LLMs on ScienceWorld (53.8 avg score,\\n      -58.7% cost vs GPT-5). Routes between model APIs for cost optimization.\\n    our_differentiation: >\\n      MTRouter routes between different LLMs (cost-quality tradeoff); we route\\n      between reasoning modalities (internal vs deterministic). Different routing\\n      targets, different findings. We analyze routing signal composition;\\n      they optimize cost.\\n\\n# ============================================================\\n# CATEGORY: Tool-Use Routing & Learning (positioning)\\n# ============================================================\\ntool_use_routing:\\n  - id: retool-2026\\n    title: \\\"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"arXiv:2504.11536, ICLR 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      RL framework to learn when to invoke code interpreter for math reasoning.\\n      Implicit routing entangled with backbone LLM. AIME2024 67.0% (Qwen2.5-32B).\\n    our_differentiation: >\\n      ReTool implicit routing via RL in math domain. SimGate explicit modular\\n      router with counterfactual labels in interactive environment. We analyze\\n      routing signal composition; they optimize tool usage strategy.\\n\\n  - id: toolformer-2024\\n    title: \\\"Toolformer: Language Models Can Teach Themselves to Use Tools\\\"\\n    authors: \\\"Schick et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    relation: background\\n    relevance: medium\\n    summary: Self-supervised tool-use learning via API call insertion.\\n    our_differentiation: >\\n      Hindsight labels from environment forking, not self-supervised. Safety-aware\\n      framing, not general tool selection.\\n\\n  - id: art-2023\\n    title: \\\"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\\\"\\n    authors: \\\"Paranjape et al.\\\"\\n    venue: \\\"2023\\\"\\n    relation: background\\n    relevance: medium\\n    summary: Automated tool selection via LLM reasoning chains.\\n    our_differentiation: Dedicated lightweight router, not LLM-as-router.\\n\\n  - id: chameleon-2024\\n    title: \\\"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"2024\\\"\\n    relation: background\\n    relevance: medium\\n    summary: LLM-as-planner routing to diverse tools.\\n    our_differentiation: >\\n      Single modality (deterministic computation), explicit small router, counterfactual\\n      methodology to understand routing signal composition.\\n\\n  - id: toolkengpt-2024\\n    title: \\\"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\\\"\\n    authors: \\\"Hao et al.\\\"\\n    venue: \\\"2024\\\"\\n    relation: background\\n    relevance: low\\n    summary: Token-level tool triggers via special embeddings.\\n    our_differentiation: Step-level routing with counterfactual episode labels.\\n\\n# ============================================================\\n# CATEGORY: Adaptive Computation & Reasoning Depth\\n# ============================================================\\nadaptive_computation:\\n  - id: ares-2026\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv:2603.07915, Mar 2026\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      Lightweight router predicts per-step reasoning effort (low/medium/high).\\n      Trained via trajectory filtering + effort annotation + SFT. Reduces tokens\\n      by 52.7%. Evaluated on TAU-Bench, WebArena, BrowseComp-Plus.\\n    our_differentiation: >\\n      Similar router architecture pattern (lightweight SFT router), but routes\\n      reasoning effort, not modality. We contribute the empirical finding about\\n      death avoidance dominance, not the router design.\\n\\n  - id: dynathink-2025\\n    title: \\\"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\\\"\\n    venue: \\\"arXiv:2506.00320, May 2025\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      Integrates world model simulation into agent reasoning loop. Uses critique\\n      generation for world model training. 32B Dyna-Think matches 685B R1 with\\n      2x fewer tokens.\\n    our_differentiation: >\\n      Dyna-Think synthesizes reasoning and simulation; we analyze the signal\\n      composition of routing between them and find death avoidance dominates.\\n\\n  - id: mixture-of-recursions-2025\\n    title: \\\"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\\\"\\n    authors: \\\"Bae et al.\\\"\\n    venue: \\\"arXiv:2507.10524, NeurIPS 2025\\\"\\n    relation: background\\n    relevance: low\\n    summary: Architecture-level adaptive depth routing via lightweight routers.\\n    our_differentiation: Architecture-level, not agent-level routing.\\n\\n# ============================================================\\n# CATEGORY: Agent Safety & Failure Analysis\\n# ============================================================\\nagent_safety:\\n  - id: toolsafety-2025\\n    title: \\\"ToolSafety: A Comprehensive Dataset for Enhancing Safety in LLM-Based Agent Tool Invocations\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      5668 direct harm + 4311 indirect harm + 4311 multi-step samples for tool\\n      invocation safety. Covers multi-step interaction vulnerabilities.\\n    our_differentiation: >\\n      ToolSafety addresses adversarial/misuse safety of tool calls. We study\\n      safety as catastrophic task failure (death) and its role as routing signal.\\n      Different safety definitions.\\n\\n  - id: openagentsafety-2026\\n    title: \\\"OpenAgentSafety: A Comprehensive Benchmark\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    relation: background\\n    relevance: low\\n    summary: >\\n      Agent safety benchmark. Finds individually safe steps compounding into\\n      unsafe outcomes over multi-turn interactions.\\n\\n  - id: llm-agentic-failures-2025\\n    title: \\\"How Do LLMs Fail In Agentic Scenarios? A Qualitative Analysis\\\"\\n    venue: \\\"arXiv:2512.07497, Dec 2025\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      Identifies 4 failure archetypes: premature action, over-helpfulness,\\n      distractor pollution, fragile execution. Qualitative analysis on 900 traces.\\n    our_differentiation: >\\n      They categorize failure types qualitatively; we quantify the dominant\\n      failure mechanism (death) and its contribution to routing signal (99%).\\n\\n  - id: envsimbench-2025\\n    title: \\\"EnvSimBench: State Prediction for LLM Environment Simulation\\\"\\n    venue: \\\"2025\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Discovers state-change cliff: LLMs fail catastrophically when multiple\\n      state variables require simultaneous updates. Directly explains WHY\\n      deterministic computation helps on rule-governed environments.\\n    our_differentiation: >\\n      EnvSimBench diagnoses WHERE LLMs fail (multi-variable state transitions);\\n      we quantify the CONSEQUENCE (death avoidance = 99% of routing signal).\\n      Highly complementary: their finding explains the mechanism behind ours.\\n\\n# ============================================================\\n# CATEGORY: Trajectory-Level Methods\\n# ============================================================\\ntrajectory_methods:\\n  - id: tsr-2026\\n    title: \\\"TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents\\\"\\n    authors: \\\"IBM Research\\\"\\n    venue: \\\"arXiv:2602.11767, ICLR 2026\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      Tree-search trajectory optimization for multi-turn RL training. Branching\\n      at high-uncertainty steps. Up to 15% absolute gains.\\n    our_differentiation: >\\n      TSR uses tree search for training optimization; our counterfactual analysis\\n      runs complete episodes under pure strategies for diagnostic purposes.\\n\\n  - id: routerr1-2025\\n    title: \\\"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    relation: background\\n    relevance: low\\n    summary: RL-based multi-LLM routing with reasoning traces.\\n\\n# ============================================================\\n# CATEGORY: Other Referenced Works\\n# ============================================================\\nother_references:\\n  - id: react-2023\\n    title: \\\"ReAct: Synergizing Reasoning and Acting in Language Models\\\"\\n    relation: background\\n    relevance: medium\\n\\n  - id: dagger-2011\\n    title: \\\"A Reduction of Imitation Learning to No-Regret Online Learning (DAgger)\\\"\\n    authors: \\\"Ross et al.\\\"\\n    relation: background\\n    relevance: medium\\n    summary: Distribution shift in imitation learning. Cited for DAgger gap discussion.\\n\\n  - id: scienceworld-2022\\n    title: \\\"ScienceWorld: Is your Agent Smarter than a 5th Grader?\\\"\\n    venue: \\\"EMNLP 2022\\\"\\n    relation: background\\n    relevance: high\\n    summary: The benchmark environment used in our experiments.\\n\\n# ============================================================\\n# SCAN SUMMARY (2026-05-14)\\n# ============================================================\\nscan_metadata:\\n  date: \\\"2026-05-14\\\"\\n  keywords_searched:\\n    - \\\"LLM agent safety + routing / mode switching\\\"\\n    - \\\"death avoidance + language model agent\\\"\\n    - \\\"counterfactual evaluation + interactive environment\\\"\\n    - \\\"ScienceWorld + agent (2025-2026)\\\"\\n    - \\\"modular reasoning + agent safety\\\"\\n    - \\\"CogRouter ScienceWorld\\\"\\n    - \\\"tool use routing learning LLM\\\"\\n    - \\\"deterministic simulation LLM agent catastrophic failure\\\"\\n    - \\\"ITP world model routing ScienceWorld\\\"\\n    - \\\"ReTool code interpreter routing\\\"\\n    - \\\"ARES adaptive reasoning\\\"\\n    - \\\"MTRouter multi-turn routing ScienceWorld\\\"\\n    - \\\"EnvSimBench state prediction\\\"\\n    - \\\"fork-based trajectory evaluation\\\"\\n    - \\\"episode-level evaluation sparse reward\\\"\\n    - \\\"Mixture-of-Depths adaptive computation\\\"\\n    - \\\"Dyna-Think world model\\\"\\n    - \\\"safety-aware tool selection catastrophic action\\\"\\n  new_papers_found: 12\\n  direct_competitors_found: 0\\n  novelty_threat: none\\n\", \"total_chars\": 12269, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "52951795-ad8a-4062-bb03-75d3c10fdf38",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map — simgate-modular-routing\\\\n# Last updated: 2026-05-14\\\\n# Scan scope: 2025-2026 incremental scan + existing references from paper_framing.md\\\\n\\\\n# ============================================================\\\\n# CATEGORY: Direct Competitors (novelty threat)\\\\n# ============================================================\\\\ndirect_competitors: []\\\\n# None found. No 2025-2026 paper claims death/safety avoidance\\\\n# as the dominant routing signal in LLM agent systems.\\\\n\\\\n# ============================================================\\\\n# CATEGORY: ScienceWorld Agent Baselines (must-cite)\\\\n# ============================================================\\\\nscienceworld_baselines:\\\\n  - id: cogrouter-2026\\\\n    title: \\\\\\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2602.12662, Feb 2026\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: high\\\\n    summary: >\\\\n      SOTA on ScienceWorld (82.3% with Qwen2.5-7B). Routes between cognitive\\\\n      depth levels (instinct to strategic planning) via CoPO, not between\\\\n      internal vs deterministic computation. Does not analyze WHAT drives\\\\n      routing signal. Cite as SOTA baseline and adaptive computation related work.\\\\n    our_differentiation: >\\\\n      CogRouter optimizes HOW MUCH to think; we analyze WHAT routing learns\\\\n      (death avoidance = 99%). Different routing dimensions (depth vs modality).\\\\n\\\\n  - id: itp-2026\\\\n    title: \\\\\\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2601.08955, Jan 2026\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: high\\\\n    summary: >\\\\n      Extends POIMDP with world model lookahead on ScienceWorld/ALFWorld/WebShop.\\\\n      Adaptive lookahead horizon based on task progress. Uses approximate LLM\\\\n      world model, not deterministic simulator.\\\\n    our_differentiation: >\\\\n      ITP routes lookahead depth using world model; we route modality (internal\\\\n      vs deterministic) and discover death avoidance dominates. ITP world\\\\n      model is approximate; our deterministic computation is exact.\\\\n\\\\n  - id: mtrouter-2026\\\\n    title: \\\\\\\"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2604.23530, ACL 2026\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: high\\\\n    summary: >\\\\n      Multi-turn routing between different LLMs on ScienceWorld (53.8 avg score,\\\\n      -58.7% cost vs GPT-5). Routes between model APIs for cost optimization.\\\\n    our_differentiation: >\\\\n      MTRouter routes between different LLMs (cost-quality tradeoff); we route\\\\n      between reasoning modalities (internal vs deterministic). Different routing\\\\n      targets, different findings. We analyze routing signal composition;\\\\n      they optimize cost.\\\\n\\\\n# ============================================================\\\\n# CATEGORY: Tool-Use Routing & Learning (positioning)\\\\n# ============================================================\\\\ntool_use_routing:\\\\n  - id: retool-2026\\\\n    title: \\\\\\\"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Feng et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2504.11536, ICLR 2026\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: high\\\\n    summary: >\\\\n      RL framework to learn when to invoke code interpreter for math reasoning.\\\\n      Implicit routing entangled with backbone LLM. AIME2024 67.0% (Qwen2.5-32B).\\\\n    our_differentiation: >\\\\n      ReTool implicit routing via RL in math domain. SimGate explicit modular\\\\n      router with counterfactual labels in interactive environment. We analyze\\\\n      routing signal composition; they optimize tool usage strategy.\\\\n\\\\n  - id: toolformer-2024\\\\n    title: \\\\\\\"Toolformer: Language Models Can Teach Themselves to Use Tools\\\\\\\"\\\\n    authors: \\\\\\\"Schick et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    relation: background\\\\n    relevance: medium\\\\n    summary: Self-supervised tool-use learning via API call insertion.\\\\n    our_differentiation: >\\\\n      Hindsight labels from environment forking, not self-supervised. Safety-aware\\\\n      framing, not general tool selection.\\\\n\\\\n  - id: art-2023\\\\n    title: \\\\\\\"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Paranjape et al.\\\\\\\"\\\\n    venue: \\\\\\\"2023\\\\\\\"\\\\n    relation: background\\\\n    relevance: medium\\\\n    summary: Automated tool selection via LLM reasoning chains.\\\\n    our_differentiation: Dedicated lightweight router, not LLM-as-router.\\\\n\\\\n  - id: chameleon-2024\\\\n    title: \\\\\\\"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Lu et al.\\\\\\\"\\\\n    venue: \\\\\\\"2024\\\\\\\"\\\\n    relation: background\\\\n    relevance: medium\\\\n    summary: LLM-as-planner routing to diverse tools.\\\\n    our_differentiation: >\\\\n      Single modality (deterministic computation), explicit small router, counterfactual\\\\n      methodology to understand routing signal composition.\\\\n\\\\n  - id: toolkengpt-2024\\\\n    title: \\\\\\\"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\\\\\\\"\\\\n    authors: \\\\\\\"Hao et al.\\\\\\\"\\\\n    venue: \\\\\\\"2024\\\\\\\"\\\\n    relation: background\\\\n    relevance: low\\\\n    summary: Token-level tool triggers via special embeddings.\\\\n    our_differentiation: Step-level routing with counterfactual episode labels.\\\\n\\\\n# ============================================================\\\\n# CATEGORY: Adaptive Computation & Reasoning Depth\\\\n# ============================================================\\\\nadaptive_computation:\\\\n  - id: ares-2026\\\\n    title: \\\\\\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2603.07915, Mar 2026\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: medium\\\\n    summary: >\\\\n      Lightweight router predicts per-step reasoning effort (low/medium/high).\\\\n      Trained via trajectory filtering + effort annotation + SFT. Reduces tokens\\\\n      by 52.7%. Evaluated on TAU-Bench, WebArena, BrowseComp-Plus.\\\\n    our_differentiation: >\\\\n      Similar router architecture pattern (lightweight SFT router), but routes\\\\n      reasoning effort, not modality. We contribute the empirical finding about\\\\n      death avoidance dominance, not the router design.\\\\n\\\\n  - id: dynathink-2025\\\\n    title: \\\\\\\"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2506.00320, May 2025\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: medium\\\\n    summary: >\\\\n      Integrates world model simulation into agent reasoning loop. Uses critique\\\\n      generation for world model training. 32B Dyna-Think matches 685B R1 with\\\\n      2x fewer tokens.\\\\n    our_differentiation: >\\\\n      Dyna-Think synthesizes reasoning and simulation; we analyze the signal\\\\n      composition of routing between them and find death avoidance dominates.\\\\n\\\\n  - id: mixture-of-recursions-2025\\\\n    title: \\\\\\\"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\\\\\\\"\\\\n    authors: \\\\\\\"Bae et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2507.10524, NeurIPS 2025\\\\\\\"\\\\n    relation: background\\\\n    relevance: low\\\\n    summary: Architecture-level adaptive depth routing via lightweight routers.\\\\n    our_differentiation: Architecture-level, not agent-level routing.\\\\n\\\\n# ============================================================\\\\n# CATEGORY: Agent Safety & Failure Analysis\\\\n# ============================================================\\\\nagent_safety:\\\\n  - id: toolsafety-2025\\\\n    title: \\\\\\\"ToolSafety: A Comprehensive Dataset for Enhancing Safety in LLM-Based Agent Tool Invocations\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: medium\\\\n    summary: >\\\\n      5668 direct harm + 4311 indirect harm + 4311 multi-step samples for tool\\\\n      invocation safety. Covers multi-step interaction vulnerabilities.\\\\n    our_differentiation: >\\\\n      ToolSafety addresses adversarial/misuse safety of tool calls. We study\\\\n      safety as catastrophic task failure (death) and its role as routing signal.\\\\n      Different safety definitions.\\\\n\\\\n  - id: openagentsafety-2026\\\\n    title: \\\\\\\"OpenAgentSafety: A Comprehensive Benchmark\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    relation: background\\\\n    relevance: low\\\\n    summary: >\\\\n      Agent safety benchmark. Finds individually safe steps compounding into\\\\n      unsafe outcomes over multi-turn interactions.\\\\n\\\\n  - id: llm-agentic-failures-2025\\\\n    title: \\\\\\\"How Do LLMs Fail In Agentic Scenarios? A Qualitative Analysis\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2512.07497, Dec 2025\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: medium\\\\n    summary: >\\\\n      Identifies 4 failure archetypes: premature action, over-helpfulness,\\\\n      distractor pollution, fragile execution. Qualitative analysis on 900 traces.\\\\n    our_differentiation: >\\\\n      They categorize failure types qualitatively; we quantify the dominant\\\\n      failure mechanism (death) and its contribution to routing signal (99%).\\\\n\\\\n  - id: envsimbench-2025\\\\n    title: \\\\\\\"EnvSimBench: State Prediction for LLM Environment Simulation\\\\\\\"\\\\n    venue: \\\\\\\"2025\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: high\\\\n    summary: >\\\\n      Discovers state-change cliff: LLMs fail catastrophically when multiple\\\\n      state variables require simultaneous updates. Directly explains WHY\\\\n      deterministic computation helps on rule-governed environments.\\\\n    our_differentiation: >\\\\n      EnvSimBench diagnoses WHERE LLMs fail (multi-variable state transitions);\\\\n      we quantify the CONSEQUENCE (death avoidance = 99% of routing signal).\\\\n      Highly complementary: their finding explains the mechanism behind ours.\\\\n\\\\n# ============================================================\\\\n# CATEGORY: Trajectory-Level Methods\\\\n# ============================================================\\\\ntrajectory_methods:\\\\n  - id: tsr-2026\\\\n    title: \\\\\\\"TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"IBM Research\\\\\\\"\\\\n    venue: \\\\\\\"arXiv:2602.11767, ICLR 2026\\\\\\\"\\\\n    relation: complementary\\\\n    relevance: medium\\\\n    summary: >\\\\n      Tree-search trajectory optimization for multi-turn RL training. Branching\\\\n      at high-uncertainty steps. Up to 15% absolute gains.\\\\n    our_differentiation: >\\\\n      TSR uses tree search for training optimization; our counterfactual analysis\\\\n      runs complete episodes under pure strategies for diagnostic purposes.\\\\n\\\\n  - id: routerr1-2025\\\\n    title: \\\\\\\"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    relation: background\\\\n    relevance: low\\\\n    summary: RL-based multi-LLM routing with reasoning traces.\\\\n\\\\n# ============================================================\\\\n# CATEGORY: Other Referenced Works\\\\n# ============================================================\\\\nother_references:\\\\n  - id: react-2023\\\\n    title: \\\\\\\"ReAct: Synergizing Reasoning and Acting in Language Models\\\\\\\"\\\\n    relation: background\\\\n    relevance: medium\\\\n\\\\n  - id: dagger-2011\\\\n    title: \\\\\\\"A Reduction of Imitation Learning to No-Regret Online Learning (DAgger)\\\\\\\"\\\\n    authors: \\\\\\\"Ross et al.\\\\\\\"\\\\n    relation: background\\\\n    relevance: medium\\\\n    summary: Distribution shift in imitation learning. Cited for DAgger gap discussion.\\\\n\\\\n  - id: scienceworld-2022\\\\n    title: \\\\\\\"ScienceWorld: Is your Agent Smarter than a 5th Grader?\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2022\\\\\\\"\\\\n    relation: background\\\\n    relevance: high\\\\n    summary: The benchmark environment used in our experiments.\\\\n\\\\n# ============================================================\\\\n# SCAN SUMMARY (2026-05-14)\\\\n# ============================================================\\\\nscan_metadata:\\\\n  date: \\\\\\\"2026-05-14\\\\\\\"\\\\n  keywords_searched:\\\\n    - \\\\\\\"LLM agent safety + routing / mode switching\\\\\\\"\\\\n    - \\\\\\\"death avoidance + language model agent\\\\\\\"\\\\n    - \\\\\\\"counterfactual evaluation + interactive environment\\\\\\\"\\\\n    - \\\\\\\"ScienceWorld + agent (2025-2026)\\\\\\\"\\\\n    - \\\\\\\"modular reasoning + agent safety\\\\\\\"\\\\n    - \\\\\\\"CogRouter ScienceWorld\\\\\\\"\\\\n    - \\\\\\\"tool use routing learning LLM\\\\\\\"\\\\n    - \\\\\\\"deterministic simulation LLM agent catastrophic failure\\\\\\\"\\\\n    - \\\\\\\"ITP world model routing ScienceWorld\\\\\\\"\\\\n    - \\\\\\\"ReTool code interpreter routing\\\\\\\"\\\\n    - \\\\\\\"ARES adaptive reasoning\\\\\\\"\\\\n    - \\\\\\\"MTRouter multi-turn routing ScienceWorld\\\\\\\"\\\\n    - \\\\\\\"EnvSimBench state prediction\\\\\\\"\\\\n    - \\\\\\\"fork-based trajectory evaluation\\\\\\\"\\\\n    - \\\\\\\"episode-level evaluation sparse reward\\\\\\\"\\\\n    - \\\\\\\"Mixture-of-Depths adaptive computation\\\\\\\"\\\\n    - \\\\\\\"Dyna-Think world model\\\\\\\"\\\\n    - \\\\\\\"safety-aware tool selection catastrophic action\\\\\\\"\\\\n  new_papers_found: 12\\\\n  direct_competitors_found: 0\\\\n  novelty_threat: none\\\\n\\\", \\\"total_chars\\\": 12269, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml\", \"content\": \"# Literature Map — simgate-modular-routing\\n# Last updated: 2026-05-14\\n# Scan scope: 2025-2026 incremental scan + existing references from paper_framing.md\\n\\n# ============================================================\\n# CATEGORY: Direct Competitors (novelty threat)\\n# ============================================================\\ndirect_competitors: []\\n# None found. No 2025-2026 paper claims death/safety avoidance\\n# as the dominant routing signal in LLM agent systems.\\n\\n# ============================================================\\n# CATEGORY: ScienceWorld Agent Baselines (must-cite)\\n# ============================================================\\nscienceworld_baselines:\\n  - id: cogrouter-2026\\n    title: \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv:2602.12662, Feb 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      SOTA on ScienceWorld (82.3% with Qwen2.5-7B). Routes between cognitive\\n      depth levels (instinct to strategic planning) via CoPO, not between\\n      internal vs deterministic computation. Does not analyze WHAT drives\\n      routing signal. Cite as SOTA baseline and adaptive computation related work.\\n    our_differentiation: >\\n      CogRouter optimizes HOW MUCH to think; we analyze WHAT routing learns\\n      (death avoidance = 99%). Different routing dimensions (depth vs modality).\\n\\n  - id: itp-2026\\n    title: \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv:2601.08955, Jan 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Extends POIMDP with world model lookahead on ScienceWorld/ALFWorld/WebShop.\\n      Adaptive lookahead horizon based on task progress. Uses approximate LLM\\n      world model, not deterministic simulator.\\n    our_differentiation: >\\n      ITP routes lookahead depth using world model; we route modality (internal\\n      vs deterministic) and discover death avoidance dominates. ITP world\\n      model is approximate; our deterministic computation is exact.\\n\\n  - id: mtrouter-2026\\n    title: \\\"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv:2604.23530, ACL 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Multi-turn routing between different LLMs on ScienceWorld (53.8 avg score,\\n      -58.7% cost vs GPT-5). Routes between model APIs for cost optimization.\\n    our_differentiation: >\\n      MTRouter routes between different LLMs (cost-quality tradeoff); we route\\n      between reasoning modalities (internal vs deterministic). Different routing\\n      targets, different findings. We analyze routing signal composition;\\n      they optimize cost.\\n\\n# ============================================================\\n# CATEGORY: Tool-Use Routing & Learning (positioning)\\n# ============================================================\\ntool_use_routing:\\n  - id: retool-2026\\n    title: \\\"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"arXiv:2504.11536, ICLR 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      RL framework to learn when to invoke code interpreter for math reasoning.\\n      Implicit routing entangled with backbone LLM. AIME2024 67.0% (Qwen2.5-32B).\\n    our_differentiation: >\\n      ReTool implicit routing via RL in math domain. SimGate explicit modular\\n      router with counterfactual labels in interactive environment. We analyze\\n      routing signal composition; they optimize tool usage strategy.\\n\\n  - id: toolformer-2024\\n    title: \\\"Toolformer: Language Models Can Teach Themselves to Use Tools\\\"\\n    authors: \\\"Schick et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    relation: background\\n    relevance: medium\\n    summary: Self-supervised tool-use learning via API call insertion.\\n    our_differentiation: >\\n      Hindsight labels from environment forking, not self-supervised. Safety-aware\\n      framing, not general tool selection.\\n\\n  - id: art-2023\\n    title: \\\"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\\\"\\n    authors: \\\"Paranjape et al.\\\"\\n    venue: \\\"2023\\\"\\n    relation: background\\n    relevance: medium\\n    summary: Automated tool selection via LLM reasoning chains.\\n    our_differentiation: Dedicated lightweight router, not LLM-as-router.\\n\\n  - id: chameleon-2024\\n    title: \\\"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"2024\\\"\\n    relation: background\\n    relevance: medium\\n    summary: LLM-as-planner routing to diverse tools.\\n    our_differentiation: >\\n      Single modality (deterministic computation), explicit small router, counterfactual\\n      methodology to understand routing signal composition.\\n\\n  - id: toolkengpt-2024\\n    title: \\\"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\\\"\\n    authors: \\\"Hao et al.\\\"\\n    venue: \\\"2024\\\"\\n    relation: background\\n    relevance: low\\n    summary: Token-level tool triggers via special embeddings.\\n    our_differentiation: Step-level routing with counterfactual episode labels.\\n\\n# ============================================================\\n# CATEGORY: Adaptive Computation & Reasoning Depth\\n# ============================================================\\nadaptive_computation:\\n  - id: ares-2026\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv:2603.07915, Mar 2026\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      Lightweight router predicts per-step reasoning effort (low/medium/high).\\n      Trained via trajectory filtering + effort annotation + SFT. Reduces tokens\\n      by 52.7%. Evaluated on TAU-Bench, WebArena, BrowseComp-Plus.\\n    our_differentiation: >\\n      Similar router architecture pattern (lightweight SFT router), but routes\\n      reasoning effort, not modality. We contribute the empirical finding about\\n      death avoidance dominance, not the router design.\\n\\n  - id: dynathink-2025\\n    title: \\\"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\\\"\\n    venue: \\\"arXiv:2506.00320, May 2025\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      Integrates world model simulation into agent reasoning loop. Uses critique\\n      generation for world model training. 32B Dyna-Think matches 685B R1 with\\n      2x fewer tokens.\\n    our_differentiation: >\\n      Dyna-Think synthesizes reasoning and simulation; we analyze the signal\\n      composition of routing between them and find death avoidance dominates.\\n\\n  - id: mixture-of-recursions-2025\\n    title: \\\"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\\\"\\n    authors: \\\"Bae et al.\\\"\\n    venue: \\\"arXiv:2507.10524, NeurIPS 2025\\\"\\n    relation: background\\n    relevance: low\\n    summary: Architecture-level adaptive depth routing via lightweight routers.\\n    our_differentiation: Architecture-level, not agent-level routing.\\n\\n# ============================================================\\n# CATEGORY: Agent Safety & Failure Analysis\\n# ============================================================\\nagent_safety:\\n  - id: toolsafety-2025\\n    title: \\\"ToolSafety: A Comprehensive Dataset for Enhancing Safety in LLM-Based Agent Tool Invocations\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      5668 direct harm + 4311 indirect harm + 4311 multi-step samples for tool\\n      invocation safety. Covers multi-step interaction vulnerabilities.\\n    our_differentiation: >\\n      ToolSafety addresses adversarial/misuse safety of tool calls. We study\\n      safety as catastrophic task failure (death) and its role as routing signal.\\n      Different safety definitions.\\n\\n  - id: openagentsafety-2026\\n    title: \\\"OpenAgentSafety: A Comprehensive Benchmark\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    relation: background\\n    relevance: low\\n    summary: >\\n      Agent safety benchmark. Finds individually safe steps compounding into\\n      unsafe outcomes over multi-turn interactions.\\n\\n  - id: llm-agentic-failures-2025\\n    title: \\\"How Do LLMs Fail In Agentic Scenarios? A Qualitative Analysis\\\"\\n    venue: \\\"arXiv:2512.07497, Dec 2025\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      Identifies 4 failure archetypes: premature action, over-helpfulness,\\n      distractor pollution, fragile execution. Qualitative analysis on 900 traces.\\n    our_differentiation: >\\n      They categorize failure types qualitatively; we quantify the dominant\\n      failure mechanism (death) and its contribution to routing signal (99%).\\n\\n  - id: envsimbench-2025\\n    title: \\\"EnvSimBench: State Prediction for LLM Environment Simulation\\\"\\n    venue: \\\"2025\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Discovers state-change cliff: LLMs fail catastrophically when multiple\\n      state variables require simultaneous updates. Directly explains WHY\\n      deterministic computation helps on rule-governed environments.\\n    our_differentiation: >\\n      EnvSimBench diagnoses WHERE LLMs fail (multi-variable state transitions);\\n      we quantify the CONSEQUENCE (death avoidance = 99% of routing signal).\\n      Highly complementary: their finding explains the mechanism behind ours.\\n\\n# ============================================================\\n# CATEGORY: Trajectory-Level Methods\\n# ============================================================\\ntrajectory_methods:\\n  - id: tsr-2026\\n    title: \\\"TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents\\\"\\n    authors: \\\"IBM Research\\\"\\n    venue: \\\"arXiv:2602.11767, ICLR 2026\\\"\\n    relation: complementary\\n    relevance: medium\\n    summary: >\\n      Tree-search trajectory optimization for multi-turn RL training. Branching\\n      at high-uncertainty steps. Up to 15% absolute gains.\\n    our_differentiation: >\\n      TSR uses tree search for training optimization; our counterfactual analysis\\n      runs complete episodes under pure strategies for diagnostic purposes.\\n\\n  - id: routerr1-2025\\n    title: \\\"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    relation: background\\n    relevance: low\\n    summary: RL-based multi-LLM routing with reasoning traces.\\n\\n# ============================================================\\n# CATEGORY: Other Referenced Works\\n# ============================================================\\nother_references:\\n  - id: react-2023\\n    title: \\\"ReAct: Synergizing Reasoning and Acting in Language Models\\\"\\n    relation: background\\n    relevance: medium\\n\\n  - id: dagger-2011\\n    title: \\\"A Reduction of Imitation Learning to No-Regret Online Learning (DAgger)\\\"\\n    authors: \\\"Ross et al.\\\"\\n    relation: background\\n    relevance: medium\\n    summary: Distribution shift in imitation learning. Cited for DAgger gap discussion.\\n\\n  - id: scienceworld-2022\\n    title: \\\"ScienceWorld: Is your Agent Smarter than a 5th Grader?\\\"\\n    venue: \\\"EMNLP 2022\\\"\\n    relation: background\\n    relevance: high\\n    summary: The benchmark environment used in our experiments.\\n\\n# ============================================================\\n# SCAN SUMMARY (2026-05-14)\\n# ============================================================\\nscan_metadata:\\n  date: \\\"2026-05-14\\\"\\n  keywords_searched:\\n    - \\\"LLM agent safety + routing / mode switching\\\"\\n    - \\\"death avoidance + language model agent\\\"\\n    - \\\"counterfactual evaluation + interactive environment\\\"\\n    - \\\"ScienceWorld + agent (2025-2026)\\\"\\n    - \\\"modular reasoning + agent safety\\\"\\n    - \\\"CogRouter ScienceWorld\\\"\\n    - \\\"tool use routing learning LLM\\\"\\n    - \\\"deterministic simulation LLM agent catastrophic failure\\\"\\n    - \\\"ITP world model routing ScienceWorld\\\"\\n    - \\\"ReTool code interpreter routing\\\"\\n    - \\\"ARES adaptive reasoning\\\"\\n    - \\\"MTRouter multi-turn routing ScienceWorld\\\"\\n    - \\\"EnvSimBench state prediction\\\"\\n    - \\\"fork-based trajectory evaluation\\\"\\n    - \\\"episode-level evaluation sparse reward\\\"\\n    - \\\"Mixture-of-Depths adaptive computation\\\"\\n    - \\\"Dyna-Think world model\\\"\\n    - \\\"safety-aware tool selection catastrophic action\\\"\\n  new_papers_found: 12\\n  direct_competitors_found: 0\\n  novelty_threat: none\\n\", \"total_chars\": 12269, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01W5zzarKTWporrPD4KUsQiQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "dc5ae51d-b17f-4204-9bb5-bceac56ffe3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ki7hvghagkTHnM2K74BMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1327,
      "cache_read_input_tokens": 23369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1327
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T11:26:32.993Z_

<details><summary>↩ Tool result · `toolu_01W5zzarKTWporrPD4KUsQiQ`</summary>

```text
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
18	ITP \cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.
19	Dyna-Think \cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.
20	Both route to \emph{approximate} world models that inherit LLM hallucination failures.
21	Our deterministic computation modality provides \emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance---non-death performance is near-equivalent between modalities.
22	
23	\paragraph{Agent Frameworks.}
24	ReAct \cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents including our internal-reasoning baseline.
25	Our work complements ReAct by analyzing \emph{when} reasoning should yield to deterministic computation and finding that the answer is concentrated in catastrophic failure scenarios.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "775657e5-4c64-44cb-9d2d-d420ef115668",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_draft.md",
      "content": "# Related Work — Draft v1\n\n\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering, while ART \\cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \\cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.\nMore recently, ReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.\nOur work differs along three axes: (1) we generate routing labels via \\emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL-based signals; (2) we frame routing as \\emph{catastrophic failure prevention} rather than general tool selection; and (3) we train an explicit lightweight router decoupled from the backbone LLM, enabling diagnostic analysis of what the routing signal encodes.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\\sim}99\\%$ of the learned routing signal.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nOur deterministic computation modality provides \\emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance---non-death performance is near-equivalent between modalities.\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents including our internal-reasoning baseline.\nOur work complements ReAct by analyzing \\emph{when} reasoning should yield to deterministic computation and finding that the answer is concentrated in catastrophic failure scenarios.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016VYAFsHdqUb84HisTnFUmN`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "a94fd835-8d0e-46cf-85e6-381b2cbe3752",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ki7hvghagkTHnM2K74BMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1327,
      "cache_read_input_tokens": 23369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1327
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T11:26:33.359Z_

<details><summary>↩ Tool result · `toolu_016VYAFsHdqUb84HisTnFUmN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (11 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\\n\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\n\\n**D013 note**: C1 no longer claims \\\"selective > unconditional.\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\n\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\n\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\n\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\"we built a better tool selector\\\" papers.\\n\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\n\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\n\\n- **Headline result template**: \\\"Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\"\\n\\n## Paper Structure (4-page short paper)\\n\\n| Section | Pages | Content |\\n|---------|-------|---------|\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\n| References | ~0.5 | Not counted in 4-page limit |\\n\\n## Anticipated Reviewer Concerns & Mitigations\\n\\n1. **\\\"Novelty is incremental — just SFT a small model to classify\\\"**\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\n\\n2. **\\\"Only one benchmark (ScienceWorld)\\\"**\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\n\\n3. **\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\"**\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\n\\n4. **\\\"Death avoidance is trivial — just always use deterministic\\\"**\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\n\\n5. **\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\"**\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\n\\n6. **\\\"ScienceWorld's -100 penalty inflates gains\\\"** (Dream all 3 tiers)\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\n\\n7. **\\\"Missing tool-use literature — this is just Toolformer\\\"** (Dream all 3 tiers, CRITICAL)\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\n\\n8. **\\\"Rule-based routing baseline missing\\\"** (Dream median + worst)\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\"structural failure analysis\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\n\\n## Venue Fit Risks\\n\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\n- Short paper format matches focused contribution scope\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\"Scope & Future Work\\\" paragraph\\n- Risk: \\\"Death avoidance is the only signal\\\" may seem like a limited finding — mitigate by framing as \\\"this IS the insight\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\"structural failure analysis\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\n\\n## Key Differences from IDEA_BRIEF\\n\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\n2. **Framing shifted**: From \\\"general routing to deterministic computation\\\" to \\\"safety-aware routing\\\" based on MVP death avoidance finding.\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\n4. **\\\"ANY form\\\" softened**: Per Human Review Note #4, \\\"across multiple forms\\\" instead of \\\"ANY form\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\n\\n## Robustness Check (30-task prescreening, appendix only)\\n\\nA broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.\\n\\n## 数据源权威声明\\n\\n- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用\\n- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix\\n- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）\\n- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）\\n\", \"total_chars\": 13390, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "4caa8edb-2bf8-4c57-bf61-abb9777266f5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — simgate-modular-routing\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026 (11 days remaining)\\\\n\\\\n## Core Insight\\\\n\\\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\\\n\\\\n## Core Claims (2 claims for short paper)\\\\n\\\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\\\\n\\\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\\\n\\\\n**D013 note**: C1 no longer claims \\\\\\\"selective > unconditional.\\\\\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\\\n\\\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\\\n\\\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\\\n\\\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\\\\\"we built a better tool selector\\\\\\\" papers.\\\\n\\\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\\\n\\\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\\\n\\\\n- **Headline result template**: \\\\\\\"Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\\\\\"\\\\n\\\\n## Paper Structure (4-page short paper)\\\\n\\\\n| Section | Pages | Content |\\\\n|---------|-------|---------|\\\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\\\n| References | ~0.5 | Not counted in 4-page limit |\\\\n\\\\n## Anticipated Reviewer Concerns & Mitigations\\\\n\\\\n1. **\\\\\\\"Novelty is incremental — just SFT a small model to classify\\\\\\\"**\\\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\\\n\\\\n2. **\\\\\\\"Only one benchmark (ScienceWorld)\\\\\\\"**\\\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\\\n\\\\n3. **\\\\\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\\\\\"**\\\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\\\n\\\\n4. **\\\\\\\"Death avoidance is trivial — just always use deterministic\\\\\\\"**\\\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\\\n\\\\n5. **\\\\\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\\\\\"**\\\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\\\n\\\\n6. **\\\\\\\"ScienceWorld's -100 penalty inflates gains\\\\\\\"** (Dream all 3 tiers)\\\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\\\n\\\\n7. **\\\\\\\"Missing tool-use literature — this is just Toolformer\\\\\\\"** (Dream all 3 tiers, CRITICAL)\\\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\\\n\\\\n8. **\\\\\\\"Rule-based routing baseline missing\\\\\\\"** (Dream median + worst)\\\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\\\\\"structural failure analysis\\\\\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\\\n- Short paper format matches focused contribution scope\\\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\\\\\"Scope & Future Work\\\\\\\" paragraph\\\\n- Risk: \\\\\\\"Death avoidance is the only signal\\\\\\\" may seem like a limited finding — mitigate by framing as \\\\\\\"this IS the insight\\\\\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\\\\\"structural failure analysis\\\\\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\\\n\\\\n## Key Differences from IDEA_BRIEF\\\\n\\\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\\\n2. **Framing shifted**: From \\\\\\\"general routing to deterministic computation\\\\\\\" to \\\\\\\"safety-aware routing\\\\\\\" based on MVP death avoidance finding.\\\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\\\n4. **\\\\\\\"ANY form\\\\\\\" softened**: Per Human Review Note #4, \\\\\\\"across multiple forms\\\\\\\" instead of \\\\\\\"ANY form\\\\\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\\\n\\\\n## Robustness Check (30-task prescreening, appendix only)\\\\n\\\\nA broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.\\\\n\\\\n## 数据源权威声明\\\\n\\\\n- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用\\\\n- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix\\\\n- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）\\\\n- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）\\\\n\\\", \\\"total_chars\\\": 13390, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (11 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\\n\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\n\\n**D013 note**: C1 no longer claims \\\"selective > unconditional.\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\n\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\n\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\n\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\"we built a better tool selector\\\" papers.\\n\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\n\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\n\\n- **Headline result template**: \\\"Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\"\\n\\n## Paper Structure (4-page short paper)\\n\\n| Section | Pages | Content |\\n|---------|-------|---------|\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\n| References | ~0.5 | Not counted in 4-page limit |\\n\\n## Anticipated Reviewer Concerns & Mitigations\\n\\n1. **\\\"Novelty is incremental — just SFT a small model to classify\\\"**\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\n\\n2. **\\\"Only one benchmark (ScienceWorld)\\\"**\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\n\\n3. **\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\"**\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\n\\n4. **\\\"Death avoidance is trivial — just always use deterministic\\\"**\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\n\\n5. **\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\"**\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\n\\n6. **\\\"ScienceWorld's -100 penalty inflates gains\\\"** (Dream all 3 tiers)\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\n\\n7. **\\\"Missing tool-use literature — this is just Toolformer\\\"** (Dream all 3 tiers, CRITICAL)\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\n\\n8. **\\\"Rule-based routing baseline missing\\\"** (Dream median + worst)\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\"structural failure analysis\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\n\\n## Venue Fit Risks\\n\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\n- Short paper format matches focused contribution scope\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\"Scope & Future Work\\\" paragraph\\n- Risk: \\\"Death avoidance is the only signal\\\" may seem like a limited finding — mitigate by framing as \\\"this IS the insight\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\"structural failure analysis\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\n\\n## Key Differences from IDEA_BRIEF\\n\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\n2. **Framing shifted**: From \\\"general routing to deterministic computation\\\" to \\\"safety-aware routing\\\" based on MVP death avoidance finding.\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\n4. **\\\"ANY form\\\" softened**: Per Human Review Note #4, \\\"across multiple forms\\\" instead of \\\"ANY form\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\n\\n## Robustness Check (30-task prescreening, appendix only)\\n\\nA broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.\\n\\n## 数据源权威声明\\n\\n- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用\\n- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix\\n- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）\\n- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）\\n\", \"total_chars\": 13390, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also look for the `write_paper_section` tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "905a4ba4-9d12-4181-9d88-9c5a009eb1bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgA5GU91TEFNbK9ebt61PU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9125,
      "cache_read_input_tokens": 24696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9125
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 15_

Let me load the `write_paper_section` tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "3ea63870-84fe-48c6-bea7-6b8734ba1400",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgA5GU91TEFNbK9ebt61PU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9125,
      "cache_read_input_tokens": 24696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9125
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01N2s5bxtr9Wb26Dmj8as6d7`</summary>

```json
{
  "query": "write_paper_section",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "afab98b2-656c-4f26-ab04-038acf18ff4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgA5GU91TEFNbK9ebt61PU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9125,
      "cache_read_input_tokens": 24696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9125
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T11:26:37.338Z_

<details><summary>↩ Tool result · `toolu_01N2s5bxtr9Wb26Dmj8as6d7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "6a04327e-8fc1-4b17-97de-2f1443620857",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "write_paper_section",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
The `write_paper_section` tool wasn't found directly. Let me search more specifically for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "93700fb5-4e0c-488f-af1b-e11ccd49dac0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TwcPYK9HLSFr3Tchgg8Yxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 405,
      "cache_read_input_tokens": 33821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 405
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TKHV6usX16vZasPLtYBB7N`</summary>

```json
{
  "query": "+write_paper_section",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "bef63352-4089-46d4-9931-a65f45b30b04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TwcPYK9HLSFr3Tchgg8Yxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 405,
      "cache_read_input_tokens": 33821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 405
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T11:26:40.368Z_

<details><summary>↩ Tool result · `toolu_01TKHV6usX16vZasPLtYBB7N`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "8e3bf4da-6aee-4822-ab02-91dda847aec8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "+write_paper_section",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
It seems `write_paper_section` isn't a separate tool but is referenced in the `save_project_file` description. Let me search the MCP tools more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "a9dcf348-a513-4eeb-94c0-a71a66ea4ce3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6gFo3sTn913zVDqQQx3PP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 34226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 392
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KweJ86TLaxeQc51ey6VkpN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "a9609ab5-2bb9-408d-a145-7c9cbdbc275f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6gFo3sTn913zVDqQQx3PP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 34226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 392
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T11:26:43.915Z_

<details><summary>↩ Tool result · `toolu_01KweJ86TLaxeQc51ey6VkpN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "8d7efcea-f61a-49ed-8661-9dda4987402f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_012GYKmL5PWWbayX1TQheHbq`</summary>

```json
{
  "pattern": "write_paper_section",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "glob": "*.py",
  "head_limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "baf07649-0ff6-41b3-9f87-1b6266b42bef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6gFo3sTn913zVDqQQx3PP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 34226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 392
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T11:26:45.388Z_

<details><summary>↩ Tool result · `toolu_012GYKmL5PWWbayX1TQheHbq`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "3d45eda1-a334-407d-9018-63222594f6bf",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [],
    "numFiles": 0
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the write_paper_section tool in the MCP tools list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "de90b050-07f3-492c-97a2-c6f20b30ac65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012oD6VyxhdtLoTLe3a91S6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 34618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_018CmeXbp5Ms3udrPU5UuCaP`</summary>

```json
{
  "pattern": "write_paper_section",
  "path": "/home/ubuntu/agent-ml-research",
  "glob": "*.py",
  "head_limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "d10a4123-ce1e-43a3-a06f-08a6fa3340ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012oD6VyxhdtLoTLe3a91S6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 34618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T11:26:52.129Z_

<details><summary>↩ Tool result · `toolu_018CmeXbp5Ms3udrPU5UuCaP`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "8fd9b306-c1b9-45e6-b8f0-9e7998311684",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "/home/ubuntu/agent-ml-research/core/mcp_server.py",
      "/home/ubuntu/agent-ml-research/core/tool_registry.py",
      "/home/ubuntu/agent-ml-research/core/tools/architecture.py",
      "/home/ubuntu/agent-ml-research/tests/test_section_writing.py",
      "/home/ubuntu/agent-ml-research/tests/test_patch_mode.py",
      "/home/ubuntu/agent-ml-research/tests/test_provenance.py",
      "/home/ubuntu/agent-ml-research/tests/test_paper_agent_full_draft_e2e.py",
      "/home/ubuntu/agent-ml-research/tests/test_paper_agent_patch_e2e.py",
      "/home/ubuntu/agent-ml-research/tests/test_paper_agent_reframe_e2e.py",
      "/home/ubuntu/agent-ml-research/tests/test_paper_agent_tools.py"
    ],
    "numFiles": 10,
    "appliedLimit": 10
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_01C5qkDfsPqFLa6KmHZ1n53s`</summary>

```json
{
  "pattern": "def write_paper_section|\"write_paper_section\"",
  "path": "/home/ubuntu/agent-ml-research/core/tools/architecture.py",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "5022c9b7-c705-48eb-a237-b11629c54ca6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LariWzY3sXPaW8SBwC9SF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 35438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T11:26:55.252Z_

<details><summary>↩ Tool result · `toolu_01C5qkDfsPqFLa6KmHZ1n53s`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "bbc60664-357d-429f-90ea-2ae9bc7d5aee",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01L9qHq6GqkdVQwm5wWK5Rgx`</summary>

```json
{
  "pattern": "write_paper_section",
  "path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "output_mode": "content",
  "-C": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "eadc7913-486c-4e5d-9169-18e000e2507d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011U8aYcpiX5kcXhnHxELcZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 151,
      "cache_read_input_tokens": 35840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 151
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T11:26:58.295Z_

<details><summary>↩ Tool result · `toolu_01L9qHq6GqkdVQwm5wWK5Rgx`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "be650c64-3a01-4e3a-b555-a0fd2bd50d6a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "2082-# ---------------------------------------------------------------------------\n2083-# Paper provenance tools\n2084-# ---------------------------------------------------------------------------\n2085-\n2086-@mcp.tool()\n2087:def write_paper_section(\n2088-    project: str,\n2089-    section: str,\n2090-    content: str,\n2091-    claims: list[dict] | None = None,\n2092-    table_cells: list[dict] | None = None,\n--\n2100-        content: LaTeX content.\n2101-        claims: List of {text, type, evidence[], decisions[]} for provenance.\n2102-        table_cells: List of {table_id, row, col, value, source{exp_id, metric}}.\n2103-        figures: List of {figure_id, caption, type, source, output_path}.\n2104-    \"\"\"\n2105:    from core.tools.provenance import write_paper_section as _wps\n2106-    result = _wps(project, section, content, claims=claims,\n2107-                  table_cells=table_cells, figures=figures)\n2108-    return _tool_result_to_str(result)\n2109-\n2110-\n--\n2776-    \"\"\"Write a project file (unified entry point, strict whitelist).\n2777-\n2778-    Writable: memory.md, writing_plan.yaml, paper_framing.md. Other files\n2779-    have dedicated tools: ROADMAP.md → update_roadmap, ideas.md →\n2780-    append_idea/move_idea, decisions.yaml → log_decision, report.md →\n2781:    auto-generated, paper sections → write_paper_section / edit_paper_section.\n2782-\n2783-    Args:\n2784-        project: Project name.\n2785-        content: Full file content.\n2786-        file: File name to write.",
    "numLines": 35
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QktTd4eNF8MWp2WjLNwQaT`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__write_paper_section",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "2fddc359-e486-4f45-ba4f-94fafb73be8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkrgzdPc9or8t7nqmYasUh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 35991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 600
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T11:27:01.178Z_

<details><summary>↩ Tool result · `toolu_01QktTd4eNF8MWp2WjLNwQaT`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "6977fba2-aa2c-4810-a200-13ebd01fdd22",
  "tool_use_result": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__write_paper_section",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
The tool exists in the MCP server but isn't in the deferred tools list. Let me check if it's directly available or if I need to use another approach. Let me try calling it directly.

Actually, looking at the deferred tools list again:
- mcp__agent-ml-research__append_idea
- mcp__agent-ml-research__read_project_file
- mcp__agent-ml-research__read_registry
- mcp__agent-ml-research__register_artifact
- mcp__agent-ml-research__save_project_file


- mcp__agent-ml-research__update_registry

The `write_paper_section` tool isn't available even though the `save_project_file` description mentions it should be used for paper sections. Since those tools aren't exposed, I'll write the file directly to the artifacts path and then register it with `register_artifact`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "5537172d-a6fe-4c67-ba44-c3002d1b2ca1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01373cZZKZ9co9RysNMRvHN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 105,
      "cache_read_input_tokens": 36591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 105
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 36_

The `write_paper_section` tool isn't available in my current tool set. I'll write the file directly and register it.

Now let me draft the v2. Key changes based on the inputs:
1. `~99%` → `~90%`
2. Expand Agent Frameworks with ScienceWorld (Wang et al. 2022 — confirmed in literature_map)
3. Strengthen differentiation in each paragraph
4. Add MTRouter (in literature_map, not cited in v1) — relevant ScienceWorld baseline

From the literature map, available cite keys: `toolformer-2024`, `art-2023`, `chameleon-2024`, `retool-2026`, `cogrouter-2026`, `ares-2026`, `mixture-of-recursions-2025`, `itp-2026`, `dynathink-2025`, `react-2023`, `scienceworld-2022`, `mtrouter-2026`. All confirmed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "dacb6807-2863-4406-984f-3c9cefacf393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01373cZZKZ9co9RysNMRvHN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 105,
      "cache_read_input_tokens": 36591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 105
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Write · `toolu_01BC957k5SULALaAZMvkMdjD`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "567ef3b1-3344-4e7f-bd4c-f050bb08174b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01373cZZKZ9co9RysNMRvHN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 105,
      "cache_read_input_tokens": 36591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 105
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T11:27:42.135Z_

<details><summary>↩ Tool result · `toolu_01BC957k5SULALaAZMvkMdjD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "ba07b3b7-3765-4016-be7b-5c10f74b61b3",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2.md",
    "content": "\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering;\nART \\cite{art-2023} delegates tool selection to LLM reasoning chains;\nChameleon \\cite{chameleon-2024} composes diverse modules under LLM-as-planner orchestration;\nand ReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation for mathematical reasoning.\nThese methods learn \\emph{which tool} to use or \\emph{whether} to use one, but do not analyze what signal drives the learned routing policy.\nWe differ in three ways: (1)~we generate labels via \\emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL signals; (2)~we frame routing as catastrophic-failure prevention rather than general tool selection; and (3)~by training an explicit lightweight router decoupled from the backbone, we can diagnose \\emph{what} the routing signal encodes, revealing that ${\\sim}90\\%$ is death avoidance.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves state-of-the-art on ScienceWorld (82.3\\%) by routing among cognitive depth levels via Cooperative Policy Optimization.\nARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort, reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation).\nMore importantly, none quantify the composition of their routing signal.\nOur counterfactual decomposition reveals that death avoidance accounts for ${\\sim}90\\%$ of the performance gap---the contribution is this empirical finding and the diagnostic methodology, not the router architecture itself.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nOur deterministic computation modality provides \\emph{exact} state transitions, and episode-level counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance: non-death performance is near-equivalent across modalities ($\\Delta_\\text{nd}$ accounts for only 9.6\\% of the full gap).\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents, including our internal-reasoning baseline.\nScienceWorld \\cite{scienceworld-2022} provides the evaluation environment: 30 science task types requiring multi-step reasoning over rule-governed state transitions with catastrophic failure penalties.\nMTRouter \\cite{mtrouter-2026} routes between different LLMs on ScienceWorld for cost optimization, but targets model-level selection rather than reasoning-modality selection.\nOur work complements these efforts by asking a different question: not \\emph{how} to build a better agent framework, but \\emph{what} a learned router actually captures.\nThe answer---that routing signal is dominated by catastrophic-failure prevention---suggests that future agent designs should prioritize safety-aware computation allocation over general-purpose reasoning enhancement.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Ev5howYxhSCYKyGNgQXcXL`</summary>

```json
{
  "name": "related_work_v2",
  "type": "paper",
  "description": "Related Work v2: fixed DAF 99→90%, expanded Agent Frameworks (ScienceWorld, MTRouter), strengthened differentiation per paragraph",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2.md",
  "tags": [
    "paper",
    "related-work",
    "v2"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "88ab8aa8-d7eb-45dc-a9b7-664f05128c76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JasAFhmCWVJ3XN9t5J64QZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1626,
      "cache_read_input_tokens": 36696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1626
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T11:27:46.384Z_

<details><summary>↩ Tool result · `toolu_01Ev5howYxhSCYKyGNgQXcXL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_7196ef\", \"name\": \"related_work_v2\", \"type\": \"paper\", \"description\": \"Related Work v2: fixed DAF 99→90%, expanded Agent Frameworks (ScienceWorld, MTRouter), strengthened differentiation per paragraph\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2_7196ef.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T11:27:46.313955+00:00\", \"tags\": [\"paper\", \"related-work\", \"v2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "a7bfa95f-49f9-4335-bfdb-18f6f6c984be",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_7196ef\\\", \\\"name\\\": \\\"related_work_v2\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Related Work v2: fixed DAF 99→90%, expanded Agent Frameworks (ScienceWorld, MTRouter), strengthened differentiation per paragraph\\\", \\\"path\\\": \\\"projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2_7196ef.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"simgate-modular-routing\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T11:27:46.313955+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"related-work\\\", \\\"v2\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_7196ef\", \"name\": \"related_work_v2\", \"type\": \"paper\", \"description\": \"Related Work v2: fixed DAF 99→90%, expanded Agent Frameworks (ScienceWorld, MTRouter), strengthened differentiation per paragraph\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/related_work_v2_7196ef.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T11:27:46.313955+00:00\", \"tags\": [\"paper\", \"related-work\", \"v2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "uuid": "99d070f1-02e1-459f-94bd-8c7ffa2638ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cs5PcT25D5gM3yxYmsbWWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 526,
      "cache_read_input_tokens": 38322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 526
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 42_

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
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 91378,
  "duration_api_ms": 91468,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "10b9a82b-ef43-4703-ba08-b3f567742d96",
  "total_cost_usd": 0.4502392499999999,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 27007,
    "cache_read_input_tokens": 381449,
    "output_tokens": 3567,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27007,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 316,
        "cache_read_input_tokens": 38322,
        "cache_creation_input_tokens": 526,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 526
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1346,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001441,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 3567,
      "cacheReadInputTokens": 381449,
      "cacheCreationInputTokens": 27007,
      "webSearchRequests": 0,
      "costUSD": 0.4487982499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1eee1cb0-8967-40b3-a620-e63f7610b8b5"
}
```

</details>

---

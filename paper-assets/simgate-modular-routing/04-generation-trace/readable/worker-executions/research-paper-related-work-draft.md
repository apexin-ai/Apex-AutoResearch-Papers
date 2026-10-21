# research paper related work draft

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_research_paper-related-work-draft_20260514T010203.log`
- **Structured JSON:** [`8635a4a29eb8bd204765.json`](../../sessions/86/8635a4a29eb8bd204765.json)

## Before a recorded user message

27 recorded events

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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
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
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "a4f25e3b-9acf-418c-9500-0fc71be96977",
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
    "status": "allowed",
    "resetsAt": 1778721000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0fd58c4e-001b-461c-9fc1-cd634ebc2cef",
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359"
}
```

---

### Assistant

_source line 4_

我先读取文献地图和论文 framing。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "5796488b-2ca9-48de-b57d-8986c654e9c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SapmmAfVbSf8qpTo5H26mq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11436,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11436
      },
      "output_tokens": 3,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Tj5VEQbGBB2DbheisZiiJG`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "f1f419ff-b9a0-48e4-a614-fd6042b2c700",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SapmmAfVbSf8qpTo5H26mq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11436,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11436
      },
      "output_tokens": 3,
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

_source line 6 · 2026-05-14T01:02:14.811Z_

<details><summary>↩ Tool result · `toolu_01Tj5VEQbGBB2DbheisZiiJG`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "9557fe5d-0cf8-4f09-a398-3a2f8866c9f7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JfVFajzmtF5ZCRVdmGecDv`</summary>

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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "6a283924-635e-43b4-8197-dd09a4df51f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiEEqDPPYGW3NYKyA5RnFg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 23277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 452
      },
      "output_tokens": 73,
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

_source line 8 · 2026-05-14T01:02:17.905Z_

<details><summary>↩ Tool result · `toolu_01JfVFajzmtF5ZCRVdmGecDv`</summary>

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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "8c73f219-c78b-4000-851d-62edb025898b",
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DLqTnU57h3Wbp8jPWHTP46`</summary>

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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "2b83fd0f-1329-499c-acd5-b1cfb7c6a435",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiEEqDPPYGW3NYKyA5RnFg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 23277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 452
      },
      "output_tokens": 73,
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

_source line 10 · 2026-05-14T01:02:18.264Z_

<details><summary>↩ Tool result · `toolu_01DLqTnU57h3Wbp8jPWHTP46`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (12 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~99% of routing signal** on ScienceWorld (Δ_full=+36.9, Δ_no_death=+0.3, r=0.986 p<0.0001). Non-death performance is approximately equal between modalities. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (+30-60pp), with **death avoidance as the dominant mechanism** (~99% of the performance gap, measured by Δ decomposition). Episode-level label distribution: ~40% det-preferred, ~1% internal-preferred, ~59% no-preference. Non-death score deltas are small and inconsistent (range: -6.8 to +4.2, most near 0). The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance. Evidence: 24+ task types consistently show death-dominated signal; correlation between death rate differential and Δ(D-I) is r=0.986 (p<0.0001).\\n\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\n\\n**D013 note**: C1 no longer claims \\\"selective > unconditional.\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\n\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\n\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\n\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~99% of routing signal — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\"we built a better tool selector\\\" papers.\\n\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\n\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~99% of routing signal is death avoidance — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance is approximately equal between modalities. A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\n\\n- **Headline result template**: \\\"Episode-level counterfactual analysis across [N] ScienceWorld task types reveals that death avoidance accounts for [99]% of routing signal between internal LLM reasoning and deterministic computation, with non-death score deltas averaging [+0.3]pp (not significant). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\"\\n\\n## Paper Structure (4-page short paper)\\n\\n| Section | Pages | Content |\\n|---------|-------|---------|\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\n| References | ~0.5 | Not counted in 4-page limit |\\n\\n## Anticipated Reviewer Concerns & Mitigations\\n\\n1. **\\\"Novelty is incremental — just SFT a small model to classify\\\"**\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\n\\n2. **\\\"Only one benchmark (ScienceWorld)\\\"**\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\n\\n3. **\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\"**\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\n\\n4. **\\\"Death avoidance is trivial — just always use deterministic\\\"**\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~99%), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\n\\n5. **\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\"**\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\n\\n6. **\\\"ScienceWorld's -100 penalty inflates gains\\\"** (Dream all 3 tiers)\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\n\\n7. **\\\"Missing tool-use literature — this is just Toolformer\\\"** (Dream all 3 tiers, CRITICAL)\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\n\\n8. **\\\"Rule-based routing baseline missing\\\"** (Dream median + worst)\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\"structural failure analysis\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\n\\n## Venue Fit Risks\\n\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\n- Short paper format matches focused contribution scope\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\"Scope & Future Work\\\" paragraph\\n- Risk: \\\"Death avoidance is the only signal\\\" may seem like a limited finding — mitigate by framing as \\\"this IS the insight\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\"structural failure analysis\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\n\\n## Key Differences from IDEA_BRIEF\\n\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\n2. **Framing shifted**: From \\\"general routing to deterministic computation\\\" to \\\"safety-aware routing\\\" based on MVP death avoidance finding.\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\n4. **\\\"ANY form\\\" softened**: Per Human Review Note #4, \\\"across multiple forms\\\" instead of \\\"ANY form\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\n\", \"total_chars\": 12184, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "8a46376a-2787-4366-b013-5982a92bb326",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — simgate-modular-routing\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026 (12 days remaining)\\\\n\\\\n## Core Insight\\\\n\\\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~99% of routing signal** on ScienceWorld (Δ_full=+36.9, Δ_no_death=+0.3, r=0.986 p<0.0001). Non-death performance is approximately equal between modalities. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\\\n\\\\n## Core Claims (2 claims for short paper)\\\\n\\\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (+30-60pp), with **death avoidance as the dominant mechanism** (~99% of the performance gap, measured by Δ decomposition). Episode-level label distribution: ~40% det-preferred, ~1% internal-preferred, ~59% no-preference. Non-death score deltas are small and inconsistent (range: -6.8 to +4.2, most near 0). The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance. Evidence: 24+ task types consistently show death-dominated signal; correlation between death rate differential and Δ(D-I) is r=0.986 (p<0.0001).\\\\n\\\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\\\n\\\\n**D013 note**: C1 no longer claims \\\\\\\"selective > unconditional.\\\\\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\\\n\\\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\\\n\\\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\\\n\\\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~99% of routing signal — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\\\\\"we built a better tool selector\\\\\\\" papers.\\\\n\\\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\\\n\\\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~99% of routing signal is death avoidance — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance is approximately equal between modalities. A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\\\n\\\\n- **Headline result template**: \\\\\\\"Episode-level counterfactual analysis across [N] ScienceWorld task types reveals that death avoidance accounts for [99]% of routing signal between internal LLM reasoning and deterministic computation, with non-death score deltas averaging [+0.3]pp (not significant). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\\\\\"\\\\n\\\\n## Paper Structure (4-page short paper)\\\\n\\\\n| Section | Pages | Content |\\\\n|---------|-------|---------|\\\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\\\n| References | ~0.5 | Not counted in 4-page limit |\\\\n\\\\n## Anticipated Reviewer Concerns & Mitigations\\\\n\\\\n1. **\\\\\\\"Novelty is incremental — just SFT a small model to classify\\\\\\\"**\\\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\\\n\\\\n2. **\\\\\\\"Only one benchmark (ScienceWorld)\\\\\\\"**\\\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\\\n\\\\n3. **\\\\\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\\\\\"**\\\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\\\n\\\\n4. **\\\\\\\"Death avoidance is trivial — just always use deterministic\\\\\\\"**\\\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~99%), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\\\n\\\\n5. **\\\\\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\\\\\"**\\\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\\\n\\\\n6. **\\\\\\\"ScienceWorld's -100 penalty inflates gains\\\\\\\"** (Dream all 3 tiers)\\\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\\\n\\\\n7. **\\\\\\\"Missing tool-use literature — this is just Toolformer\\\\\\\"** (Dream all 3 tiers, CRITICAL)\\\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\\\n\\\\n8. **\\\\\\\"Rule-based routing baseline missing\\\\\\\"** (Dream median + worst)\\\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\\\\\"structural failure analysis\\\\\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\\\n- Short paper format matches focused contribution scope\\\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\\\\\"Scope & Future Work\\\\\\\" paragraph\\\\n- Risk: \\\\\\\"Death avoidance is the only signal\\\\\\\" may seem like a limited finding — mitigate by framing as \\\\\\\"this IS the insight\\\\\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\\\\\"structural failure analysis\\\\\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\\\n\\\\n## Key Differences from IDEA_BRIEF\\\\n\\\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\\\n2. **Framing shifted**: From \\\\\\\"general routing to deterministic computation\\\\\\\" to \\\\\\\"safety-aware routing\\\\\\\" based on MVP death avoidance finding.\\\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\\\n4. **\\\\\\\"ANY form\\\\\\\" softened**: Per Human Review Note #4, \\\\\\\"across multiple forms\\\\\\\" instead of \\\\\\\"ANY form\\\\\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\\\n\\\", \\\"total_chars\\\": 12184, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (12 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~99% of routing signal** on ScienceWorld (Δ_full=+36.9, Δ_no_death=+0.3, r=0.986 p<0.0001). Non-death performance is approximately equal between modalities. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (+30-60pp), with **death avoidance as the dominant mechanism** (~99% of the performance gap, measured by Δ decomposition). Episode-level label distribution: ~40% det-preferred, ~1% internal-preferred, ~59% no-preference. Non-death score deltas are small and inconsistent (range: -6.8 to +4.2, most near 0). The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance. Evidence: 24+ task types consistently show death-dominated signal; correlation between death rate differential and Δ(D-I) is r=0.986 (p<0.0001).\\n\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. The resulting labels train a lightweight router (Qwen3-1.7B) that serves as a **diagnostic probe** for LLM failure modes. [Hypothesis, pending plan-005]: the router may learn within-task-type early warning signals of catastrophic failure from early observations, beyond simple task-type classification.\\n\\n**D013 note**: C1 no longer claims \\\"selective > unconditional.\\\" Router training (plan-002/003) proceeds — if router ≈ always-det, that IS the finding; comparison with rule-based baseline (plan-011) quantifies whether learned routing adds value over keyword heuristics.\\n\\n## Positioning vs Tool-Use Literature (Dream-driven addition)\\n\\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\\n\\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (98% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~99% of routing signal — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Diagnostic framework — counterfactual analysis + router as probe reveals systematic LLM failure modes across task categories. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \\\"we built a better tool selector\\\" papers.\\n\\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\\n\\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (98% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~99% of routing signal is death avoidance — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance is approximately equal between modalities. A router trained on these labels becomes a diagnostic probe for LLM failure modes, but (per D013) is structurally limited to task-level risk classification under episode-level labels.\\n\\n- **Headline result template**: \\\"Episode-level counterfactual analysis across [N] ScienceWorld task types reveals that death avoidance accounts for [99]% of routing signal between internal LLM reasoning and deterministic computation, with non-death score deltas averaging [+0.3]pp (not significant). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\\\"\\n\\n## Paper Structure (4-page short paper)\\n\\n| Section | Pages | Content |\\n|---------|-------|---------|\\n| Abstract | 0.2 | Counterfactual analysis framing, death avoidance finding, headline numbers |\\n| Introduction | 0.8 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (empirical finding + methodology) |\\n| Method | 1.0 | Episode-level counterfactual labeling (why per-step fails: 98% ties → episode-level solution); router training as downstream application; death decomposition analysis framework |\\n| Experiments | 1.5 | Death avoidance decomposition (core) + router vs baselines (always-det, rule-based, learned) + routing pattern analysis figure |\\n| Conclusion | 0.3 | Summary + limitations (episode-level granularity, single benchmark) + future (step-level labeling, MATH) |\\n| References | ~0.5 | Not counted in 4-page limit |\\n\\n## Anticipated Reviewer Concerns & Mitigations\\n\\n1. **\\\"Novelty is incremental — just SFT a small model to classify\\\"**\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\n\\n2. **\\\"Only one benchmark (ScienceWorld)\\\"**\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\n\\n3. **\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\"**\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\n\\n4. **\\\"Death avoidance is trivial — just always use deterministic\\\"**\\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~99%), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\\n\\n5. **\\\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\\\"**\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\\n\\n6. **\\\"ScienceWorld's -100 penalty inflates gains\\\"** (Dream all 3 tiers)\\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\\n\\n7. **\\\"Missing tool-use literature — this is just Toolformer\\\"** (Dream all 3 tiers, CRITICAL)\\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router).\\n\\n8. **\\\"Rule-based routing baseline missing\\\"** (Dream median + worst)\\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \\\"structural failure analysis\\\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\\n\\n## Venue Fit Risks\\n\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\n- Short paper format matches focused contribution scope\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\"Scope & Future Work\\\" paragraph\\n- Risk: \\\"Death avoidance is the only signal\\\" may seem like a limited finding — mitigate by framing as \\\"this IS the insight\\\" (most routing literature assumes diverse routing benefits; we show it's dominated by one mechanism) + diagnostic methodology has value beyond ScienceWorld\\n- Risk: Router ≈ always-det ≈ rule-based keyword heuristic → novelty concern. **D014 update: keyword routing structurally fails on ScienceWorld** — v1 (generic verbs) ≈ always-det (85.8%), v2 (science keywords) ≈ always-internal (4.9%). ScienceWorld actions use generic interaction verbs (connect/move/pick up), not science-specific keywords, so no keyword list provides meaningful routing. This is a POSITIVE finding: positions keyword routing as \\\"structural failure analysis\\\" in the paper, strengthens case for learned routing or observation-based approaches.\\n\\n## Key Differences from IDEA_BRIEF\\n\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\n2. **Framing shifted**: From \\\"general routing to deterministic computation\\\" to \\\"safety-aware routing\\\" based on MVP death avoidance finding.\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\n4. **\\\"ANY form\\\" softened**: Per Human Review Note #4, \\\"across multiple forms\\\" instead of \\\"ANY form\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\n\", \"total_chars\": 12184, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the literature map and paper framing. Let me draft the Related Work section based on:

1. **Tool-use learning**: Toolformer, ART, Chameleon — differentiation: counterfactual trajectory labeling + safety-aware framing
2. **Adaptive computation**: CogRouter, ARES, Mixture-of-Depths — we route modality not cognitive depth
3. **World model routing**: ITP-R, Dyna-Think — we use exact deterministic computation not approximate world models
4. **Agent frameworks**: ReAct — general reference


5. **Recent work**: ReTool and MTRouter also fit into the tool-use and routing categories

I need to reconcile the citation IDs from the literature map with what's in the paper framing — there's a discrepancy between "Mixture-of-Depths" and "mixture-of-recursions-2025" that I should resolve before drafting.

Now I'm organizing the Related Work into thematic sections: tool-use learning where I'll highlight our episode-level counterfactual labeling and safety-aware approach, adaptive computation methods that handle modality routing differently than depth-based approaches, and world model routing techniques.

I'm also mapping the literature entries to LaTeX-friendly citation keys so I can properly reference them throughout the paper, aiming for around 300-400 words total for this section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "10014c3e-4cfd-4972-8704-dc3359838e77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBzGHKzpKGL4yNdgWMc3hL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 23729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7623
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

_source line 12_

Now let me load the artifact registration tool, then write the draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "e9d389d8-88f0-4bea-adbd-4b4ee74900ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBzGHKzpKGL4yNdgWMc3hL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 23729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7623
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

_source line 13_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FNBzXU4Snt7PwMCHi69mzf`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "4e8ecfdf-e5f0-49d4-9a2b-8ea329ba3c11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBzGHKzpKGL4yNdgWMc3hL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 23729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7623
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

_source line 14 · 2026-05-14T01:02:37.448Z_

<details><summary>↩ Tool result · `toolu_01FNBzXU4Snt7PwMCHi69mzf`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "9c79fbbb-77f1-48f1-959f-0310f2f37815",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qy8tTZPsz2xjvU6SE1bN2w`</summary>

```json
{
  "query": "register artifact",
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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "0524e679-5d1e-4fed-ba8a-b337910f4d42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBzGHKzpKGL4yNdgWMc3hL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7623,
      "cache_read_input_tokens": 23729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7623
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

_source line 16 · 2026-05-14T01:02:37.905Z_

<details><summary>↩ Tool result · `toolu_01Qy8tTZPsz2xjvU6SE1bN2w`</summary>

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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "81fdccbd-fbcf-499a-8cec-e735beee9230",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
There's no `register_artifact` tool available as a deferred tool. Let me search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "d831c9ee-c70d-4858-9f39-e16b9e2c4e99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCpjDGFfQkgCZ1Eaxzegn4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 31352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1036
      },
      "output_tokens": 19,
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

_source line 18_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014H5AWQGyE9NkfsnMvfeKT2`</summary>

```json
{
  "query": "register artifact save project",
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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "0ad6aedb-0a5c-41bf-b1db-aecfe737a974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCpjDGFfQkgCZ1Eaxzegn4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 31352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1036
      },
      "output_tokens": 19,
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

_source line 19 · 2026-05-14T01:02:41.613Z_

<details><summary>↩ Tool result · `toolu_014H5AWQGyE9NkfsnMvfeKT2`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "EnterWorktree"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "75ed5ab7-95fd-403b-9a25-189da96e05ed",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file",
      "EnterWorktree",
      "TodoWrite",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "register artifact save project",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
There's no `register_artifact` tool available. Let me check if there's a different tool name for registering artifacts.

Let me just write the draft to the specified path and note that `register_artifact` isn't available. I'll write the file and let the user know.

Now let me draft the Related Work section. I need to cover 4 directions with ~300-400 words, using only papers from the literature map.

**Tool-Use Learning**: toolformer-2024, art-2023, chameleon-2024, retool-2026
**Adaptive Computation**: cogrouter-2026, ares-2026, mixture-of-recursions-2025


**World Model Routing**: itp-2026, dynathink-2025
**Agent Frameworks**: react-2023

Let me write this up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "0741f04a-0868-4052-9da1-e43951c6a58f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YS1w2iDBqyE8EzYgA7rf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 32388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4052
      },
      "output_tokens": 18,
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

_source line 21_

`register_artifact` 不在可用工具列表中，我先写草稿文件，注册步骤后续处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "663a100d-6bb9-4c6e-8e6a-d9c68f98f09d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YS1w2iDBqyE8EzYgA7rf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 32388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4052
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01U2FNv2k3RAKzCKJhjuyW77`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "d47ceb8c-4e9b-49df-85ac-f08bca841714",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YS1w2iDBqyE8EzYgA7rf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 32388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4052
      },
      "output_tokens": 18,
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

_source line 23 · 2026-05-14T01:02:53.599Z_

<details><summary>↩ Tool result · `toolu_01U2FNv2k3RAKzCKJhjuyW77`</summary>

```text
_project
death_aware_labeling.py
diagnosis_mvp-p1-gpu1-v2.md
dream_reports
literature_survey_death_avoidance.md
manifest.yaml
phase1_progress_report.md
plan_001b_revised_proposal.md
plan_001b_task_selection.md
prescreening_final_summary.json
router_sft_train.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "8ce9ccd7-f171-404f-ab39-fb9efcfcd4df",
  "tool_use_result": {
    "stdout": "_project\ndeath_aware_labeling.py\ndiagnosis_mvp-p1-gpu1-v2.md\ndream_reports\nliterature_survey_death_avoidance.md\nmanifest.yaml\nphase1_progress_report.md\nplan_001b_revised_proposal.md\nplan_001b_task_selection.md\nprescreening_final_summary.json\nrouter_sft_train.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Write · `toolu_01CDxYs5GqBgBDn8xTMADpVg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/related_work_draft.md",
  "content": "# Related Work — Draft v1\n\n\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering, while ART \\cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \\cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.\nMore recently, ReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.\nOur work differs along three axes: (1) we generate routing labels via \\emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL-based signals; (2) we frame routing as \\emph{catastrophic failure prevention} rather than general tool selection; and (3) we train an explicit lightweight router decoupled from the backbone LLM, enabling diagnostic analysis of what the routing signal encodes.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\\sim}99\\%$ of the learned routing signal.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nOur deterministic computation modality provides \\emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance---non-death performance is near-equivalent between modalities.\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents including our internal-reasoning baseline.\nOur work complements ReAct by analyzing \\emph{when} reasoning should yield to deterministic computation and finding that the answer is concentrated in catastrophic failure scenarios.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "0db480db-f69a-49dc-a0b3-b72b5f041def",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnDSjhQpxV5JL6HjFVrFU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 36440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 556
      },
      "output_tokens": 53,
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

_source line 25 · 2026-05-14T01:03:16.101Z_

<details><summary>↩ Tool result · `toolu_01CDxYs5GqBgBDn8xTMADpVg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/related_work_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "e0e3cadf-f2b6-4c50-9ef4-2181ac9b047b",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/related_work_draft.md",
    "content": "# Related Work — Draft v1\n\n\\section{Related Work}\n\n\\paragraph{Tool-Use Learning.}\nA line of work teaches LLMs when and how to invoke external tools.\nToolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering, while ART \\cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \\cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.\nMore recently, ReTool \\cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.\nOur work differs along three axes: (1) we generate routing labels via \\emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL-based signals; (2) we frame routing as \\emph{catastrophic failure prevention} rather than general tool selection; and (3) we train an explicit lightweight router decoupled from the backbone LLM, enabling diagnostic analysis of what the routing signal encodes.\n\n\\paragraph{Adaptive Computation.}\nSeveral recent methods adapt reasoning effort per step.\nCogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \\cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\\%.\nMixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.\nThese methods route \\emph{how much} to reason; we route \\emph{which modality} to use (internal LLM reasoning vs.\\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\\sim}99\\%$ of the learned routing signal.\n\n\\paragraph{World Model Routing.}\nITP \\cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.\nDyna-Think \\cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.\nBoth route to \\emph{approximate} world models that inherit LLM hallucination failures.\nOur deterministic computation modality provides \\emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance---non-death performance is near-equivalent between modalities.\n\n\\paragraph{Agent Frameworks.}\nReAct \\cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents including our internal-reasoning baseline.\nOur work complements ReAct by analyzing \\emph{when} reasoning should yield to deterministic computation and finding that the answer is concentrated in catastrophic failure scenarios.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 26_

草稿已写入 `artifacts/related_work_draft.md`（约 370 words）。

结构覆盖了 4 个方向：
- **Tool-Use Learning**: Toolformer / ART / Chameleon / ReTool — 区分点：episode-level counterfactual labeling + safety-aware framing + explicit decoupled router
- **Adaptive Computation**: CogRouter / ARES / Mixture-of-Recursions — 区分点：route modality (internal vs deterministic) 而非 cognitive depth/effort
- **World Model Routing**: ITP / Dyna-Think — 区分点：exact deterministic computation vs approximate world models，exactness 的价值集中在 death avoidance
- **Agent Frameworks**: ReAct — 作为 internal-reasoning baseline 的基础框架

所有引用均来自 `literature_map.yaml`，无编造。`register_artifact` 工具不可用，需要你手动注册或告诉我替代方式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "uuid": "706de2d1-ae6f-4cf6-8b9f-6d9b8add5812",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZyxCRsZ74qZwZRmQZVc9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 883,
      "cache_read_input_tokens": 36996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 883
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

_source line 27_

草稿已写入 `artifacts/related_work_draft.md`（约 370 words）。

结构覆盖了 4 个方向：
- **Tool-Use Learning**: Toolformer / ART / Chameleon / ReTool — 区分点：episode-level counterfactual labeling + safety-aware framing + explicit decoupled router
- **Adaptive Computation**: CogRouter / ARES / Mixture-of-Recursions — 区分点：route modality (internal vs deterministic) 而非 cognitive depth/effort
- **World Model Routing**: ITP / Dyna-Think — 区分点：exact deterministic computation vs approximate world models，exactness 的价值集中在 death avoidance
- **Agent Frameworks**: ReAct — 作为 internal-reasoning baseline 的基础框架

所有引用均来自 `literature_map.yaml`，无编造。`register_artifact` 工具不可用，需要你手动注册或告诉我替代方式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 76598,
  "duration_api_ms": 77300,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "82c411d2-6630-4f2f-b48c-9e2994b03359",
  "total_cost_usd": 0.328143,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 26038,
    "cache_read_input_tokens": 196023,
    "output_tokens": 2637,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26038,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 262,
        "cache_read_input_tokens": 36996,
        "cache_creation_input_tokens": 883,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 883
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1294,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001394,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 2637,
      "cacheReadInputTokens": 196023,
      "cacheCreationInputTokens": 26038,
      "webSearchRequests": 0,
      "costUSD": 0.326749,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d0d368e3-6e84-4004-9958-debb5bed6000"
}
```

</details>

---

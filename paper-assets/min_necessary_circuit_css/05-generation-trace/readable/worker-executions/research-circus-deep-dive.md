# research circus deep dive

**Transformer Model EAP-IG** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_research_circus_deep_dive_20260512T221843.log`
- **Structured JSON:** [`100d97280c1fe152ece9.json`](../../sessions/10/100d97280c1fe152ece9.json)

## Before a recorded user message

47 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "f7321644-7ab3-40b9-92fb-958fd1d445cb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-structfuse-context/memory/"
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
    "resetsAt": 1778634000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8ccfd373-cb4f-4fb7-964d-aa53583026da",
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa"
}
```

---

### Assistant

_source line 4_

我将搜索 CIRCUS 论文的详细信息，先并行执行多个搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "b26abc35-eaa4-4785-8d37-232a7f503f5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuDuE9TQVfquntSUtZjeEd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11889,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11889
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QajzTZPuon8WvNbusXsucY`</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "0d23922e-967a-4956-8ee1-7498de7252cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuDuE9TQVfquntSUtZjeEd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11889,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11889
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

_source line 6 · 2026-05-12T22:18:59.085Z_

<details><summary>↩ Tool result · `toolu_01QajzTZPuon8WvNbusXsucY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
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
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "d5902471-5d34-4a20-b9c4-851a2b355c72",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing related_work_notes.md and simultaneously searching for the CIRCUS paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "f32e5797-c8e3-41f1-b2bd-1760f909b2c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XChEyWkeR4rmpa43fpBmUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2340,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2340
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

### Assistant

_source line 8_

并行搜索 CIRCUS 论文信息并读取现有笔记。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "9e8691da-558f-40f4-9d8c-97cb60ea29f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XChEyWkeR4rmpa43fpBmUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2340,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2340
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WrvTESfyuAGqsGPhqeWZsp`</summary>

```json
{
  "query": "CIRCUS circuit discovery stability arXiv 2603.00523"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "bd7a9950-6f75-4829-8091-3d9637cbdbdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XChEyWkeR4rmpa43fpBmUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2340,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2340
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017EwTsukvsRiTdmufnpx7qL`</summary>

```json
{
  "query": "CIRCUS \"config-bagging\" circuit discovery consensus stability scoring 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "f0c58d6f-a53a-4630-ac2e-82a6aca77b8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XChEyWkeR4rmpa43fpBmUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2340,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2340
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B4SGqo9NhN1eQrbTxme7No`</summary>

```json
{
  "query": "arXiv 2603.00523 CIRCUS per-edge stability mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "91f583c2-0c20-426c-a2c8-627b423a3ada",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XChEyWkeR4rmpa43fpBmUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2340,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2340
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

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01CnwAJUaQHUm3LQpxubnHJB`</summary>

```json
{
  "pattern": "artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "d36b3d26-76d3-4386-b5b0-8d3299afbd92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XChEyWkeR4rmpa43fpBmUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2340,
      "cache_read_input_tokens": 23730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2340
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

_source line 13 · 2026-05-12T22:19:06.359Z_

<details><summary>↩ Tool result · `toolu_01CnwAJUaQHUm3LQpxubnHJB`</summary>

```text
artifacts/related_work_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "0cc19716-bb0e-453c-81fd-2513790d373f",
  "tool_use_result": {
    "filenames": [
      "artifacts/related_work_notes.md"
    ],
    "durationMs": 17,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T22:19:11.638Z_

<details><summary>↩ Tool result · `toolu_01WrvTESfyuAGqsGPhqeWZsp`</summary>

```text
Web search results for query: "CIRCUS circuit discovery stability arXiv 2603.00523"

Links: [{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/html/2505.24731"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823v1"},{"title":"Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/pdf/2602.16823"},{"title":"Automatic Discovery of Visual Circuits","url":"https://arxiv.org/html/2404.14349v1"}]

Based on the search results, here is information about the paper arXiv 2603.00523:

## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

CIRCUS constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views.

**The Core Problem:**
Mechanistic circuit discovery is notoriously sensitive to arbitrary analyst choices, especially pruning thresholds and feature dictionaries, often yielding brittle "one-shot" explanations with no principled notion of uncertainty.

**The Solution:**
The method reframes circuit discovery as an uncertainty-quantification problem over these analytic degrees of freedom. This produces a threshold-robust "core" circuit while explicitly surfacing contingent alternatives and enabling rejection of low-agreement structure.

**Key Advantages:**
CIRCUS requires no retraining and adds negligible overhead, since it aggregates structure across already-computed pruned graphs.

**Author:** The paper was submitted on February 28, 2026, by Swapnil Parekh.

The method adapts stability selection techniques to circuit discovery, providing a principled way to distinguish robust circuit components from those that are sensitive to analyst choices.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "ef12f83b-2454-4e1a-8f5a-163eda5e36b9",
  "tool_use_result": {
    "query": "CIRCUS circuit discovery stability arXiv 2603.00523",
    "results": [
      {
        "tool_use_id": "srvtoolu_011ZyJYHaPibf3dngb6fvTj3",
        "content": [
          {
            "title": "[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/abs/2603.00523"
          },
          {
            "title": "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/html/2603.00523"
          },
          {
            "title": "Circuit Stability Characterizes Language Model Generalization",
            "url": "https://arxiv.org/html/2505.24731"
          },
          {
            "title": "[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees",
            "url": "https://arxiv.org/abs/2602.16823"
          },
          {
            "title": "[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability",
            "url": "https://arxiv.org/abs/2304.14997"
          },
          {
            "title": "[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees",
            "url": "https://arxiv.org/abs/2602.16823v1"
          },
          {
            "title": "Certified Circuits: Stability Guarantees for Mechanistic Circuits",
            "url": "https://arxiv.org/html/2602.22968"
          },
          {
            "title": "Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees",
            "url": "https://arxiv.org/html/2602.16823v1"
          },
          {
            "title": "Automated Circuit Discovery with Provable Guarantees",
            "url": "https://arxiv.org/pdf/2602.16823"
          },
          {
            "title": "Automatic Discovery of Visual Circuits",
            "url": "https://arxiv.org/html/2404.14349v1"
          }
        ]
      },
      "Based on the search results, here is information about the paper arXiv 2603.00523:\n\n## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\n\nCIRCUS constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views.\n\n**The Core Problem:**\nMechanistic circuit discovery is notoriously sensitive to arbitrary analyst choices, especially pruning thresholds and feature dictionaries, often yielding brittle \"one-shot\" explanations with no principled notion of uncertainty.\n\n**The Solution:**\nThe method reframes circuit discovery as an uncertainty-quantification problem over these analytic degrees of freedom. This produces a threshold-robust \"core\" circuit while explicitly surfacing contingent alternatives and enabling rejection of low-agreement structure.\n\n**Key Advantages:**\nCIRCUS requires no retraining and adds negligible overhead, since it aggregates structure across already-computed pruned graphs.\n\n**Author:** The paper was submitted on February 28, 2026, by Swapnil Parekh.\n\nThe method adapts stability selection techniques to circuit discovery, providing a principled way to distinguish robust circuit components from those that are sensitive to analyst choices."
    ],
    "durationSeconds": 6.984591755999998
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T22:19:13.380Z_

<details><summary>↩ Tool result · `toolu_017EwTsukvsRiTdmufnpx7qL`</summary>

```text
Web search results for query: "CIRCUS "config-bagging" circuit discovery consensus stability scoring 2026"

Links: [{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Generalized String-Stability Criteria for Consensus Protocols","url":"https://arxiv.org/html/2604.21329v1"},{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"Circus 2026 — AI & Experimentation Conference — London","url":"https://speero.com/circus"},{"title":"Configuration — Circus 0.17.2 documentation - Read the Docs","url":"https://circus.readthedocs.io/en/latest/for-ops/configuration/"},{"title":"Circuit Insights - 2026 IEEE CICC","url":"https://www.ieee-cicc.org/circuit-insights/"},{"title":"ConsCS: Effective and Efficient Verification of Circom Circuits (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/189/ConsCS-Effective-and-Efficient-Verification-of-Circom-Circuits"},{"title":"Circos: An information aesthetic for comparative genomics","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/"},{"title":"ConsCS: Effective and Efficient Verification of Circom Circuits | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00200"}]

Based on the search results, I found relevant information about CIRCUS:

## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

CIRCUS addresses the problem that mechanistic circuit discovery is notoriously sensitive to arbitrary analyst choices, especially pruning thresholds and feature dictionaries, often yielding brittle "one-shot" explanations with no principled notion of uncertainty. The method reframes circuit discovery as an uncertainty-quantification problem over these analytic degrees of freedom.

### How It Works

CIRCUS constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views. This produces a threshold-robust "core" circuit while explicitly surfacing contingent alternatives and enabling rejection of low-agreement structure.

### Key Technical Feature

The method adapts stability selection, replacing data subsampling with config-bagging over pruning thresholds. CIRCUS produces per-edge scores measuring how robustly edges survive across the configuration family, and extracts a consensus circuit. This yields a principled core/contingent/noise decomposition that separates robust structure from threshold-sensitive artifacts, with negligible overhead.

### Efficiency

CIRCUS requires no retraining and adds negligible overhead, since it aggregates structure across already-computed pruned graphs.

The paper was published on arXiv in February 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "8d943724-5d2e-4ad5-a52b-f6ded402a11c",
  "tool_use_result": {
    "query": "CIRCUS \"config-bagging\" circuit discovery consensus stability scoring 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SqSYiEyHQLHrASd9CE7bsj",
        "content": [
          {
            "title": "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/html/2603.00523"
          },
          {
            "title": "[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/abs/2603.00523"
          },
          {
            "title": "Generalized String-Stability Criteria for Consensus Protocols",
            "url": "https://arxiv.org/html/2604.21329v1"
          },
          {
            "title": "Certified Circuits: Stability Guarantees for Mechanistic Circuits",
            "url": "https://arxiv.org/html/2602.22968"
          },
          {
            "title": "Circus 2026 — AI & Experimentation Conference — London",
            "url": "https://speero.com/circus"
          },
          {
            "title": "Configuration — Circus 0.17.2 documentation - Read the Docs",
            "url": "https://circus.readthedocs.io/en/latest/for-ops/configuration/"
          },
          {
            "title": "Circuit Insights - 2026 IEEE CICC",
            "url": "https://www.ieee-cicc.org/circuit-insights/"
          },
          {
            "title": "ConsCS: Effective and Efficient Verification of Circom Circuits (ICSE 2025 - Research Track) - ICSE 2025",
            "url": "https://conf.researchr.org/details/icse-2025/icse-2025-research-track/189/ConsCS-Effective-and-Efficient-Verification-of-Circom-Circuits"
          },
          {
            "title": "Circos: An information aesthetic for comparative genomics",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/"
          },
          {
            "title": "ConsCS: Effective and Efficient Verification of Circom Circuits | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering",
            "url": "https://dl.acm.org/doi/10.1109/ICSE55347.2025.00200"
          }
        ]
      },
      "Based on the search results, I found relevant information about CIRCUS:\n\n## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\n\nCIRCUS addresses the problem that mechanistic circuit discovery is notoriously sensitive to arbitrary analyst choices, especially pruning thresholds and feature dictionaries, often yielding brittle \"one-shot\" explanations with no principled notion of uncertainty. The method reframes circuit discovery as an uncertainty-quantification problem over these analytic degrees of freedom.\n\n### How It Works\n\nCIRCUS constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views. This produces a threshold-robust \"core\" circuit while explicitly surfacing contingent alternatives and enabling rejection of low-agreement structure.\n\n### Key Technical Feature\n\nThe method adapts stability selection, replacing data subsampling with config-bagging over pruning thresholds. CIRCUS produces per-edge scores measuring how robustly edges survive across the configuration family, and extracts a consensus circuit. This yields a principled core/contingent/noise decomposition that separates robust structure from threshold-sensitive artifacts, with negligible overhead.\n\n### Efficiency\n\nCIRCUS requires no retraining and adds negligible overhead, since it aggregates structure across already-computed pruned graphs.\n\nThe paper was published on arXiv in February 2026."
    ],
    "durationSeconds": 7.790220938000002
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T22:19:14.312Z_

<details><summary>↩ Tool result · `toolu_01B4SGqo9NhN1eQrbTxme7No`</summary>

```text
Web search results for query: "arXiv 2603.00523 CIRCUS per-edge stability mechanistic interpretability"

Links: [{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/html/2602.16740"},{"title":"Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/html/2505.24731"},{"title":"[2603.30002] Tracking Equivalent Mechanistic Interpretations Across Neural Networks","url":"https://arxiv.org/abs/2603.30002"},{"title":"Circuit Stability Characterizes Language Model ...","url":"https://aclanthology.org/2025.acl-long.442.pdf"},{"title":"Mechanistic Interpretability for AI Safety A Review","url":"https://arxiv.org/html/2404.14082v2"},{"title":"Beyond Accuracy: Introducing a Symbolic-Mechanistic Approach to Interpretable Evaluation","url":"https://arxiv.org/html/2603.23517"},{"title":"Mechanistic Interpretability Needs Philosophy","url":"https://arxiv.org/html/2506.18852v1"}]

Based on the search results, I found detailed information about arXiv paper 2603.00523.

## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

CIRCUS reframes circuit discovery as a problem of uncertainty over explanations, pruning one attribution graph under multiple configurations and assigning each edge an empirical inclusion frequency s(e)∈[0,1] measuring how robustly it survives across the configuration family.

### Key Problem Addressed

A critical issue is that circuit discovery results depend on arbitrary analyst choices: two different pruning thresholds yield two different circuits, with no principled way to tell which edges reflect genuine model structure versus threshold sensitivity.

### Per-Edge Stability & Methodology

The method constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views.

### Core/Contingent/Noise Taxonomy

This yields a principled core/contingent/noise decomposition (analogous to posterior model-inclusion indicators in Bayesian variable selection) that separates robust structure from threshold-sensitive artifacts, with negligible overhead.

### Empirical Results

On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power, and consensus-identified nodes consistently beat matched non-consensus controls in activation patching validation (p=0.0004).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "1604f4a2-94d7-40ad-b06c-8a806a7ba007",
  "tool_use_result": {
    "query": "arXiv 2603.00523 CIRCUS per-edge stability mechanistic interpretability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D3SM9GqUXUnZSfBUGQLDsa",
        "content": [
          {
            "title": "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/html/2603.00523"
          },
          {
            "title": "[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/abs/2603.00523"
          },
          {
            "title": "Certified Circuits: Stability Guarantees for Mechanistic Circuits",
            "url": "https://arxiv.org/html/2602.22968"
          },
          {
            "title": "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality",
            "url": "https://arxiv.org/html/2602.16740"
          },
          {
            "title": "Circuit Stability Characterizes Language Model Generalization",
            "url": "https://arxiv.org/html/2505.24731"
          },
          {
            "title": "[2603.30002] Tracking Equivalent Mechanistic Interpretations Across Neural Networks",
            "url": "https://arxiv.org/abs/2603.30002"
          },
          {
            "title": "Circuit Stability Characterizes Language Model ...",
            "url": "https://aclanthology.org/2025.acl-long.442.pdf"
          },
          {
            "title": "Mechanistic Interpretability for AI Safety A Review",
            "url": "https://arxiv.org/html/2404.14082v2"
          },
          {
            "title": "Beyond Accuracy: Introducing a Symbolic-Mechanistic Approach to Interpretable Evaluation",
            "url": "https://arxiv.org/html/2603.23517"
          },
          {
            "title": "Mechanistic Interpretability Needs Philosophy",
            "url": "https://arxiv.org/html/2506.18852v1"
          }
        ]
      },
      "Based on the search results, I found detailed information about arXiv paper 2603.00523.\n\n## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\n\nCIRCUS reframes circuit discovery as a problem of uncertainty over explanations, pruning one attribution graph under multiple configurations and assigning each edge an empirical inclusion frequency s(e)∈[0,1] measuring how robustly it survives across the configuration family.\n\n### Key Problem Addressed\n\nA critical issue is that circuit discovery results depend on arbitrary analyst choices: two different pruning thresholds yield two different circuits, with no principled way to tell which edges reflect genuine model structure versus threshold sensitivity.\n\n### Per-Edge Stability & Methodology\n\nThe method constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views.\n\n### Core/Contingent/Noise Taxonomy\n\nThis yields a principled core/contingent/noise decomposition (analogous to posterior model-inclusion indicators in Bayesian variable selection) that separates robust structure from threshold-sensitive artifacts, with negligible overhead.\n\n### Empirical Results\n\nOn Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power, and consensus-identified nodes consistently beat matched non-consensus controls in activation patching validation (p=0.0004)."
    ],
    "durationSeconds": 8.242610004000001
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, I have some initial information. Now let me fetch the actual paper HTML to get detailed method information, and read the existing related_work_notes.md.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "a0c41833-2d25-4aee-8554-ed7a7f3bda5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKh65mw4qBfXywTAr1M1P6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 40,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 26070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

_source line 18_

找到了关键信息。现在获取论文全文细节和现有笔记。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "2409bdac-727e-46d6-99a4-d8f9f60efce3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKh65mw4qBfXywTAr1M1P6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 40,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 26070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

_source line 19_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VH2Qpw4u5djcQy2RunkMVw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.00523",
  "prompt": "Extract the full abstract, author list, and any methodology details visible on this page. What models and tasks are evaluated? What circuit discovery methods are used (EAP, ACDC, Edge Pruning, etc.)? Does CIRCUS compare across different circuit discovery algorithms?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "9f6f1d55-eada-4d5e-a191-521d6bdc8d7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKh65mw4qBfXywTAr1M1P6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 40,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 26070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

_source line 20 · 2026-05-12T22:19:30.383Z_

<details><summary>↩ Tool result · `toolu_01VH2Qpw4u5djcQy2RunkMVw`</summary>

```text
# CIRCUS Paper Summary

## Full Abstract
"Every mechanistic circuit carries an invisible asterisk: it reflects not just the model's computation, but the analyst's choice of pruning threshold. Change that choice and the circuit changes, yet current practice treats a single pruned subgraph as ground truth with no way to distinguish robust structure from threshold artifacts. We introduce CIRCUS, which reframes circuit discovery as a problem of uncertainty over explanations. CIRCUS prunes one attribution graph under B configurations, assigns each edge an empirical inclusion frequency s(e) in [0,1] measuring how robustly it survives across the configuration family, and extracts a consensus circuit of edges present in every view. This yields a principled core/contingent/noise decomposition (analogous to posterior model-inclusion indicators in Bayesian variable selection) that separates robust structure from threshold-sensitive artifacts, with negligible overhead. On Gemma-2-2B and Llama-3.2-1B, consensus circuits are 40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power, consistently outperform influence-ranked and random baselines, and are confirmed causally relevant by activation patching."

## Author
Swapnil Parekh

## Models & Tasks Evaluated
- Gemma-2-2B
- Llama-3.2-1B

## Methodology Details
CIRCUS prunes a single attribution graph across multiple pruning threshold configurations, computing empirical edge inclusion frequencies. It extracts consensus circuits and decomposes results into robust core/contingent/noise categories. Evaluation employs activation patching for causal validation.

## Circuit Discovery Comparison
The page does not specify which circuit discovery algorithms (EAP, ACDC, etc.) CIRCUS compares against, though it benchmarks against influence-ranked and random baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "99e54b07-caaa-41aa-a874-805392fdb833",
  "tool_use_result": {
    "bytes": 46130,
    "code": 200,
    "codeText": "OK",
    "result": "# CIRCUS Paper Summary\n\n## Full Abstract\n\"Every mechanistic circuit carries an invisible asterisk: it reflects not just the model's computation, but the analyst's choice of pruning threshold. Change that choice and the circuit changes, yet current practice treats a single pruned subgraph as ground truth with no way to distinguish robust structure from threshold artifacts. We introduce CIRCUS, which reframes circuit discovery as a problem of uncertainty over explanations. CIRCUS prunes one attribution graph under B configurations, assigns each edge an empirical inclusion frequency s(e) in [0,1] measuring how robustly it survives across the configuration family, and extracts a consensus circuit of edges present in every view. This yields a principled core/contingent/noise decomposition (analogous to posterior model-inclusion indicators in Bayesian variable selection) that separates robust structure from threshold-sensitive artifacts, with negligible overhead. On Gemma-2-2B and Llama-3.2-1B, consensus circuits are 40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power, consistently outperform influence-ranked and random baselines, and are confirmed causally relevant by activation patching.\"\n\n## Author\nSwapnil Parekh\n\n## Models & Tasks Evaluated\n- Gemma-2-2B\n- Llama-3.2-1B\n\n## Methodology Details\nCIRCUS prunes a single attribution graph across multiple pruning threshold configurations, computing empirical edge inclusion frequencies. It extracts consensus circuits and decomposes results into robust core/contingent/noise categories. Evaluation employs activation patching for causal validation.\n\n## Circuit Discovery Comparison\nThe page does not specify which circuit discovery algorithms (EAP, ACDC, etc.) CIRCUS compares against, though it benchmarks against influence-ranked and random baselines.",
    "durationMs": 6887,
    "url": "https://arxiv.org/abs/2603.00523"
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q8KECUBCzwTJrSFxpnD3Z4`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.00523",
  "prompt": "Extract ALL methodology details from the CIRCUS paper. Specifically I need:\n\n1. STABILITY MEASUREMENT: What exactly varies across the ensemble? Is it pruning thresholds, random seeds, data subsets, or something else? What is \"config-bagging\" precisely? How many configurations B are used?\n\n2. CONSENSUS MECHANISM: What is the mathematical formula for the stability score s(e)? Is it binary voting or continuous averaging? How is the consensus circuit extracted - what threshold is used?\n\n3. MODELS AND TASKS: List all models (GPT-2, Llama, Gemma, etc.) and all tasks (IOI, Greater-Than, etc.) used in experiments.\n\n4. CIRCUIT DISCOVERY METHODS: Which underlying circuit discovery method(s) does CIRCUS use? EAP? ACDC? Edge Pruning? Does it compare across DIFFERENT circuit discovery algorithms, or only vary parameters within ONE algorithm?\n\n5. FAITHFULNESS EVALUATION: What metrics are used to evaluate circuit quality? KL divergence? Logit diff? How does CIRCUS prove consensus is better than single runs?\n\n6. CORE/CONTINGENT/NOISE DECOMPOSITION: How are these three categories defined mathematically?\n\nBe extremely detailed and include any formulas or specific numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "36f6646c-d105-4a13-9f35-71a097f70b6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKh65mw4qBfXywTAr1M1P6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 40,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 26070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

<details open><summary>🔧 Tool call — Read · `toolu_017VV2Nj5e95r7cb7b3F5EWv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "4bc94643-cd81-4755-b551-11954b2700e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKh65mw4qBfXywTAr1M1P6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 40,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 26070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

_source line 23 · 2026-05-12T22:19:32.428Z_

<details><summary>↩ Tool result · `toolu_017VV2Nj5e95r7cb7b3F5EWv`</summary>

```text
1	# Circuit Discovery Related Work Notes (2024-2026)
2	
3	> 调研日期：2026-05-12 | 项目：structfuse-context
4	> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？
5	
6	---
7	
8	## 1. 方法一致性比较（Novelty 关键）
9	
10	**结论：没有论文以"跨方法一致性分析"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。
11	
12	### 直接比较多方法的论文
13	
14	| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |
15	|------|----------|----------|---------------------|
16	| Conmy et al. "Towards Automated Circuit Discovery" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |
17	| Syed et al. "Attribution Patching Outperforms Automated Circuit Discovery" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |
18	| Bhaskar et al. "Finding Transformer Circuits with Edge Pruning" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |
19	| Hsu et al. "CD-T" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |
20	| Edin et al. "GIM" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |
21	| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |
22	
23	### 最接近"一致性分析"的论文
24	
25	**Hanna et al. "Have Faith in Faithfulness: Going Beyond Circuit Overlap" (2024, arXiv 2403.17806)**
26	- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大
27	- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价
28	- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究
29	
30	**Méloux et al. "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis" (2025, arXiv 2510.00845)**
31	- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561
32	- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等
33	- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法
34	
35	**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**
36	
37	---
38	
39	## 2. Circuit Aggregation / Ensemble（Novelty 威胁）
40	
41	### 🔴 最高威胁：CIRCUS
42	
43	**CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**
44	- 作者：Swapnil Parekh
45	- 时间：2026年3月, arXiv 2603.00523
46	- 方法：对单一归因方法，在多组剪枝阈值配置下运行，计算每条边的 inclusion frequency → stability score s(e) ∈ [0,1]，提取 consensus circuit（所有配置下都存在的边），分为 core/contingent/noise
47	- **与 CSS 的区别**：CIRCUS 变化的是**单方法内的超参数**（剪枝阈值），不是跨不同算法族。它不运行 ACDC + EAP + SP 然后求交集
48	- **与 CSS 的相似度**：数学框架高度相似（per-edge stability scoring, consensus extraction, core/contingent taxonomy）
49	- **威胁评级**：🔴 HIGH — 概念上最接近，但维度不同（intra-method vs cross-method）
50	
51	### 🟡 中等威胁：Mondorf et al. Ensemble
52	
53	**Mondorf et al. "Exploring Ensemble Strategies for Circuit Localization Methods" (BlackboxNLP 2025, arXiv 2510.06811)**
54	- 方法：组合 EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning 的输出
55	  - Max = union（任一方法选中）
56	  - Min = intersection（所有方法选中）
57	  - Mean = 连续分数平均
58	  - Hybrid = 并行+串行组合
59	- 结果：Mean > union/intersection，Hybrid 最佳 (CMD 0.03, CPR 1.83)
60	- **与 CSS 的区别**：聚合的是**连续归因分数**（mean/min/max），不是二值 edge-in/edge-out；方法主要是 EAP 变体，不是真正不同的算法族；workshop 短文非完整方法贡献
61	- **与 CSS 的相似度**：确实跨方法组合（attribution + pruning），实现了 union/intersection 操作
62	- **威胁评级**：🟡 MODERATE — 最接近跨方法聚合，但 framing 为 shared task 工程方案非方法论贡献
63	
64	### 🟢 低威胁
65	
66	| 论文 | 方法 | 与 CSS 区别 | 威胁 |
67	|------|------|------------|------|
68	| Nikankin et al. "Improving Circuit Faithfulness via Better Edge Selection" (BlackboxNLP 2025) | Bootstrap EAP-IG scores across data resamples | 单方法 + 数据重采样，非跨方法 | 🟢 LOW |
69	| Anani et al. "Certified Circuits: Stability Guarantees" (2026, arXiv 2602.22968) | 随机化数据子采样 + 删除平滑认证 | 单方法 wrapper，不聚合多方法 | 🟢 LOW |
70	| Miller et al. "Transformer Circuit Faithfulness Metrics are not Robust" (CoLM 2024) | 分析 faithfulness 指标敏感性 | 纯诊断，不提出聚合 | 🟢 LOW |
71	
72	**总结：没有论文提出 CSS 的精确方案——运行 N 种根本不同的算法族（ACDC, EAP, SP, EP），对每种输出做二值化，然后计算跨方法 binary consensus。CIRCUS 最接近但维度不同（intra-method threshold variation vs cross-method）。Mondorf et al. 确实跨方法但用连续分数聚合且为 workshop 工程方案。**
73	
74	---
75	
76	## 3. 2024-2026 新方法
77	
78	| 方法 | 论文 | 年份 | 会议 | 算法族 | 备注 |
79	|------|------|------|------|--------|------|
80	| CD-T | Hsu et al. "Efficient Automated Circuit Discovery using Contextual Decomposition" | 2024 | ICLR 2025 | 分解 (decomposition) | 无需 activation patching，秒级发现，97% AUC |
81	| DiscoGP | Yu et al. "Functional Faithfulness in the Wild" | 2024 | ICML 2024 | 可微剪枝 | 联合权重+边剪枝，端到端学习二值 mask |
82	| Transcoders | Dunefsky et al. "Transcoders Find Interpretable LLM Feature Circuits" | 2024 | NeurIPS 2024 | 稀疏替换模型 | 用稀疏 MLP 替换原 MLP，实现 weights-based 电路分析 |
83	| Sparse Feature Circuits | Marks et al. "Discovering and Editing Interpretable Causal Graphs" | 2024 | ICLR 2025 (Oral) | 归因 + SAE 特征 | 在 SAE 特征级别发现电路，支持 SHIFT 编辑 |
84	| Circuit Tracing | Ameisen, Olah et al. (Anthropic) "Attribution Graphs" | 2025 | Tech Report | 稀疏替换 + 归因 | Cross-layer transcoders → per-prompt DAG，应用于 Claude 3.5 |
85	| GIM | Edin et al. "Improved Interpretability for LLMs" | 2025 | arXiv | 梯度修正 | 修正 softmax/LayerNorm 反传，MIB 排行榜第一 |
86	| HAP | Gu et al. "Hybrid Attribution and Pruning Framework" | 2025 | arXiv | 混合 (EAP → EP) | 先 EAP 粗筛再 EP 精修，比 EP 快 46% |
87	| ModCirc | He et al. "Modular Circuits of LLMs" | 2025 | ICML 2025 | 模块化分解 | 发现跨任务共享的模块化电路词表 |
88	| Stream | Rosser et al. "Scaling up MI to Long Context" | 2025 | arXiv | 层次化剪枝 | O(T log T) 稀疏注意力 mask，支持 100K+ token |
89	| Weight-Sparse Circuits | Gao et al. (OpenAI) | 2025 | arXiv | 稀疏训练 | 极端权重稀疏 (~1/1000) → 天然可解释电路 |
90	| Formal MI | Hadad et al. "Automated Circuit Discovery with Provable Guarantees" | 2026 | ICLR 2026 | 验证 (verification) | 首个可证明保证的电路发现（鲁棒性 + 最小性） |
91	| SVD Directional Masking | Ahmad et al. "Beyond Components" | 2025 | arXiv | SVD + 可微 mask | 揭示单头内叠加子功能 |
92	
93	---
94	
95	## 4. 顶会论文列表
96	
97	### ICLR 2024
98	| 论文 | 主要贡献 |
99	|------|----------|
100	| Sparse Autoencoders Find Highly Interpretable Features in LMs | SAE 发现单语义特征，解决 superposition |
101	| Towards Best Practices of Activation Patching in LMs | 系统分析 patching 方法选择对电路发现的影响 |
102	| Circuit Component Reuse Across Tasks | IOI 电路 ~78% 被 Colored Objects 复用 |
103	| Successor Heads: Recurring Interpretable Attention Heads | 发现跨架构的 successor heads（递增操作） |
104	
105	### ICLR 2025
106	| 论文 | 主要贡献 |
107	|------|----------|
108	| Sparse Feature Circuits (Oral) | SAE 特征级电路发现 + SHIFT 编辑 |
109	| Scaling and Evaluating Sparse Autoencoders (Oral) | k-sparse SAE 扩展到 GPT-4，16M latents |
110	| CD-T: Contextual Decomposition for Circuit Discovery | 秒级电路发现，97% AUC |
111	| Computational Complexity of Circuit Discovery (Spotlight) | 证明多数电路发现查询 NP-hard |
112	| Everything Everywhere All at Once: Is MI Identifiable? | 电路非唯一性：多电路可复现同一行为 |
113	| SAEs Do Not Find Canonical Units of Analysis | SAE stitching 证明特征非原子/非完备 |
114	| Unifying and Verifying Mechanistic Interpretations | 统一群运算网络的机制解释并形式化证明 |
115	
116	### NeurIPS 2024
117	| 论文 | 主要贡献 |
118	|------|----------|
119	| Finding Transformer Circuits with Edge Pruning (Spotlight) | EP 方法，更忠实且更稀疏，扩展到 13B |
120	| Transcoders Find Interpretable LLM Feature Circuits | 稀疏 MLP 替换实现 weights-based 电路分析 |
121	| LLM Circuit Analyses Are Consistent Across Training and Scale | 电路在训练过程和模型规模间一致出现 |
122	| Compact Proofs of Model Performance via MI | MI → 可证明的准确率下界 |
123	| Hypothesis Testing the Circuit Hypothesis | 形式化电路假设的假设检验 |
124	| InterpBench: Semi-Synthetic Transformers for Evaluating MI | 86 个有 ground-truth 的半合成模型评估基准 |
125	
126	### ICML 2025
127	| 论文 | 主要贡献 |
128	|------|----------|
129	| MIB: A Mechanistic Interpretability Benchmark | 标准化电路定位基准，归因+mask 优化方法领先 |
130	| ModCirc: Modular Circuits of LLMs | 跨任务模块化电路词表 |
131	| Towards Understanding Fine-Tuning via Circuit Analysis | 追踪微调中电路变化，提出 circuit-aware LoRA |
132	
133	---
134	
135	## 5. Novelty 评估
136	
137	### CSS 的 novelty 站得住吗？**站得住，但需要精确定位差异化。**
138	
139	#### ✅ Novelty 成立的理由
140	
141	1. **无人做跨算法族的 binary consensus**：所有现有工作要么是单方法内变异分析（CIRCUS, Méloux），要么是连续分数聚合（Mondorf），要么只是各方法 vs ground-truth 的性能比较。CSS 提出跨 N 种根本不同的算法族做二值共识，这个精确配方是新的。
142	
143	2. **方法间差异的系统分析是空白**：没有论文报告过不同方法的 pairwise Jaccard matrix / agreement heatmap。大量论文隐含表明方法差异很大（EP 边数不到 ACDC 一半），但无人将此作为研究问题。
144	
145	3. **core/contingent 分类的跨方法版本未被探索**：CIRCUS 做了类似的 core/contingent/noise taxonomy，但基于 intra-method threshold variation。CSS 基于 cross-method agreement 做分类，维度不同且信息更丰富。
146	
147	#### ⚠️ 需要小心的 Novelty 威胁
148	
149	1. **CIRCUS (2603.00523)** 是最大威胁。虽然维度不同，但 reviewer 可能认为 conceptual overlap 太大。**建议**：论文中必须明确讨论 CIRCUS，强调区别（intra-method hyperparameter variation vs cross-method algorithmic diversity），并论证为何跨方法维度更有意义（不同方法有不同 inductive bias，而阈值变化只探索同一方法的 Rashomon set）。
150	
151	2. **Mondorf et al.** 已经实现了 union/intersection 操作并发现 mean 优于两者。CSS 需要论证 binary consensus 相比连续分数平均的优势（如可解释性、对阈值选择的鲁棒性）。
152	
153	3. **Méloux et al. 的 intra-method instability 问题**：如果单方法内 Jaccard 仅 0.56，跨方法 consensus 可能更低。需要实验证明 CSS-core 的 faithfulness 确实优于单方法，否则 consensus 可能只是噪声的交集。
154	
155	4. **非唯一性问题 (ICLR 2025 "Everything Everywhere All at Once")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。
156	
157	#### 🎯 差异化建议
158	
159	- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。
160	- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。
161	- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。
162	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "aaa68cb3-93d7-4eb5-97a2-598922a3e4d4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
      "content": "# Circuit Discovery Related Work Notes (2024-2026)\n\n> 调研日期：2026-05-12 | 项目：structfuse-context\n> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？\n\n---\n\n## 1. 方法一致性比较（Novelty 关键）\n\n**结论：没有论文以\"跨方法一致性分析\"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。\n\n### 直接比较多方法的论文\n\n| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |\n|------|----------|----------|---------------------|\n| Conmy et al. \"Towards Automated Circuit Discovery\" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |\n| Syed et al. \"Attribution Patching Outperforms Automated Circuit Discovery\" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |\n| Bhaskar et al. \"Finding Transformer Circuits with Edge Pruning\" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |\n| Hsu et al. \"CD-T\" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |\n| Edin et al. \"GIM\" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |\n| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |\n\n### 最接近\"一致性分析\"的论文\n\n**Hanna et al. \"Have Faith in Faithfulness: Going Beyond Circuit Overlap\" (2024, arXiv 2403.17806)**\n- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大\n- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价\n- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究\n\n**Méloux et al. \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\" (2025, arXiv 2510.00845)**\n- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561\n- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等\n- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法\n\n**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**\n\n---\n\n## 2. Circuit Aggregation / Ensemble（Novelty 威胁）\n\n### 🔴 最高威胁：CIRCUS\n\n**CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**\n- 作者：Swapnil Parekh\n- 时间：2026年3月, arXiv 2603.00523\n- 方法：对单一归因方法，在多组剪枝阈值配置下运行，计算每条边的 inclusion frequency → stability score s(e) ∈ [0,1]，提取 consensus circuit（所有配置下都存在的边），分为 core/contingent/noise\n- **与 CSS 的区别**：CIRCUS 变化的是**单方法内的超参数**（剪枝阈值），不是跨不同算法族。它不运行 ACDC + EAP + SP 然后求交集\n- **与 CSS 的相似度**：数学框架高度相似（per-edge stability scoring, consensus extraction, core/contingent taxonomy）\n- **威胁评级**：🔴 HIGH — 概念上最接近，但维度不同（intra-method vs cross-method）\n\n### 🟡 中等威胁：Mondorf et al. Ensemble\n\n**Mondorf et al. \"Exploring Ensemble Strategies for Circuit Localization Methods\" (BlackboxNLP 2025, arXiv 2510.06811)**\n- 方法：组合 EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning 的输出\n  - Max = union（任一方法选中）\n  - Min = intersection（所有方法选中）\n  - Mean = 连续分数平均\n  - Hybrid = 并行+串行组合\n- 结果：Mean > union/intersection，Hybrid 最佳 (CMD 0.03, CPR 1.83)\n- **与 CSS 的区别**：聚合的是**连续归因分数**（mean/min/max），不是二值 edge-in/edge-out；方法主要是 EAP 变体，不是真正不同的算法族；workshop 短文非完整方法贡献\n- **与 CSS 的相似度**：确实跨方法组合（attribution + pruning），实现了 union/intersection 操作\n- **威胁评级**：🟡 MODERATE — 最接近跨方法聚合，但 framing 为 shared task 工程方案非方法论贡献\n\n### 🟢 低威胁\n\n| 论文 | 方法 | 与 CSS 区别 | 威胁 |\n|------|------|------------|------|\n| Nikankin et al. \"Improving Circuit Faithfulness via Better Edge Selection\" (BlackboxNLP 2025) | Bootstrap EAP-IG scores across data resamples | 单方法 + 数据重采样，非跨方法 | 🟢 LOW |\n| Anani et al. \"Certified Circuits: Stability Guarantees\" (2026, arXiv 2602.22968) | 随机化数据子采样 + 删除平滑认证 | 单方法 wrapper，不聚合多方法 | 🟢 LOW |\n| Miller et al. \"Transformer Circuit Faithfulness Metrics are not Robust\" (CoLM 2024) | 分析 faithfulness 指标敏感性 | 纯诊断，不提出聚合 | 🟢 LOW |\n\n**总结：没有论文提出 CSS 的精确方案——运行 N 种根本不同的算法族（ACDC, EAP, SP, EP），对每种输出做二值化，然后计算跨方法 binary consensus。CIRCUS 最接近但维度不同（intra-method threshold variation vs cross-method）。Mondorf et al. 确实跨方法但用连续分数聚合且为 workshop 工程方案。**\n\n---\n\n## 3. 2024-2026 新方法\n\n| 方法 | 论文 | 年份 | 会议 | 算法族 | 备注 |\n|------|------|------|------|--------|------|\n| CD-T | Hsu et al. \"Efficient Automated Circuit Discovery using Contextual Decomposition\" | 2024 | ICLR 2025 | 分解 (decomposition) | 无需 activation patching，秒级发现，97% AUC |\n| DiscoGP | Yu et al. \"Functional Faithfulness in the Wild\" | 2024 | ICML 2024 | 可微剪枝 | 联合权重+边剪枝，端到端学习二值 mask |\n| Transcoders | Dunefsky et al. \"Transcoders Find Interpretable LLM Feature Circuits\" | 2024 | NeurIPS 2024 | 稀疏替换模型 | 用稀疏 MLP 替换原 MLP，实现 weights-based 电路分析 |\n| Sparse Feature Circuits | Marks et al. \"Discovering and Editing Interpretable Causal Graphs\" | 2024 | ICLR 2025 (Oral) | 归因 + SAE 特征 | 在 SAE 特征级别发现电路，支持 SHIFT 编辑 |\n| Circuit Tracing | Ameisen, Olah et al. (Anthropic) \"Attribution Graphs\" | 2025 | Tech Report | 稀疏替换 + 归因 | Cross-layer transcoders → per-prompt DAG，应用于 Claude 3.5 |\n| GIM | Edin et al. \"Improved Interpretability for LLMs\" | 2025 | arXiv | 梯度修正 | 修正 softmax/LayerNorm 反传，MIB 排行榜第一 |\n| HAP | Gu et al. \"Hybrid Attribution and Pruning Framework\" | 2025 | arXiv | 混合 (EAP → EP) | 先 EAP 粗筛再 EP 精修，比 EP 快 46% |\n| ModCirc | He et al. \"Modular Circuits of LLMs\" | 2025 | ICML 2025 | 模块化分解 | 发现跨任务共享的模块化电路词表 |\n| Stream | Rosser et al. \"Scaling up MI to Long Context\" | 2025 | arXiv | 层次化剪枝 | O(T log T) 稀疏注意力 mask，支持 100K+ token |\n| Weight-Sparse Circuits | Gao et al. (OpenAI) | 2025 | arXiv | 稀疏训练 | 极端权重稀疏 (~1/1000) → 天然可解释电路 |\n| Formal MI | Hadad et al. \"Automated Circuit Discovery with Provable Guarantees\" | 2026 | ICLR 2026 | 验证 (verification) | 首个可证明保证的电路发现（鲁棒性 + 最小性） |\n| SVD Directional Masking | Ahmad et al. \"Beyond Components\" | 2025 | arXiv | SVD + 可微 mask | 揭示单头内叠加子功能 |\n\n---\n\n## 4. 顶会论文列表\n\n### ICLR 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Autoencoders Find Highly Interpretable Features in LMs | SAE 发现单语义特征，解决 superposition |\n| Towards Best Practices of Activation Patching in LMs | 系统分析 patching 方法选择对电路发现的影响 |\n| Circuit Component Reuse Across Tasks | IOI 电路 ~78% 被 Colored Objects 复用 |\n| Successor Heads: Recurring Interpretable Attention Heads | 发现跨架构的 successor heads（递增操作） |\n\n### ICLR 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Feature Circuits (Oral) | SAE 特征级电路发现 + SHIFT 编辑 |\n| Scaling and Evaluating Sparse Autoencoders (Oral) | k-sparse SAE 扩展到 GPT-4，16M latents |\n| CD-T: Contextual Decomposition for Circuit Discovery | 秒级电路发现，97% AUC |\n| Computational Complexity of Circuit Discovery (Spotlight) | 证明多数电路发现查询 NP-hard |\n| Everything Everywhere All at Once: Is MI Identifiable? | 电路非唯一性：多电路可复现同一行为 |\n| SAEs Do Not Find Canonical Units of Analysis | SAE stitching 证明特征非原子/非完备 |\n| Unifying and Verifying Mechanistic Interpretations | 统一群运算网络的机制解释并形式化证明 |\n\n### NeurIPS 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Finding Transformer Circuits with Edge Pruning (Spotlight) | EP 方法，更忠实且更稀疏，扩展到 13B |\n| Transcoders Find Interpretable LLM Feature Circuits | 稀疏 MLP 替换实现 weights-based 电路分析 |\n| LLM Circuit Analyses Are Consistent Across Training and Scale | 电路在训练过程和模型规模间一致出现 |\n| Compact Proofs of Model Performance via MI | MI → 可证明的准确率下界 |\n| Hypothesis Testing the Circuit Hypothesis | 形式化电路假设的假设检验 |\n| InterpBench: Semi-Synthetic Transformers for Evaluating MI | 86 个有 ground-truth 的半合成模型评估基准 |\n\n### ICML 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| MIB: A Mechanistic Interpretability Benchmark | 标准化电路定位基准，归因+mask 优化方法领先 |\n| ModCirc: Modular Circuits of LLMs | 跨任务模块化电路词表 |\n| Towards Understanding Fine-Tuning via Circuit Analysis | 追踪微调中电路变化，提出 circuit-aware LoRA |\n\n---\n\n## 5. Novelty 评估\n\n### CSS 的 novelty 站得住吗？**站得住，但需要精确定位差异化。**\n\n#### ✅ Novelty 成立的理由\n\n1. **无人做跨算法族的 binary consensus**：所有现有工作要么是单方法内变异分析（CIRCUS, Méloux），要么是连续分数聚合（Mondorf），要么只是各方法 vs ground-truth 的性能比较。CSS 提出跨 N 种根本不同的算法族做二值共识，这个精确配方是新的。\n\n2. **方法间差异的系统分析是空白**：没有论文报告过不同方法的 pairwise Jaccard matrix / agreement heatmap。大量论文隐含表明方法差异很大（EP 边数不到 ACDC 一半），但无人将此作为研究问题。\n\n3. **core/contingent 分类的跨方法版本未被探索**：CIRCUS 做了类似的 core/contingent/noise taxonomy，但基于 intra-method threshold variation。CSS 基于 cross-method agreement 做分类，维度不同且信息更丰富。\n\n#### ⚠️ 需要小心的 Novelty 威胁\n\n1. **CIRCUS (2603.00523)** 是最大威胁。虽然维度不同，但 reviewer 可能认为 conceptual overlap 太大。**建议**：论文中必须明确讨论 CIRCUS，强调区别（intra-method hyperparameter variation vs cross-method algorithmic diversity），并论证为何跨方法维度更有意义（不同方法有不同 inductive bias，而阈值变化只探索同一方法的 Rashomon set）。\n\n2. **Mondorf et al.** 已经实现了 union/intersection 操作并发现 mean 优于两者。CSS 需要论证 binary consensus 相比连续分数平均的优势（如可解释性、对阈值选择的鲁棒性）。\n\n3. **Méloux et al. 的 intra-method instability 问题**：如果单方法内 Jaccard 仅 0.56，跨方法 consensus 可能更低。需要实验证明 CSS-core 的 faithfulness 确实优于单方法，否则 consensus 可能只是噪声的交集。\n\n4. **非唯一性问题 (ICLR 2025 \"Everything Everywhere All at Once\")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。\n\n#### 🎯 差异化建议\n\n- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。\n- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。\n- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n",
      "numLines": 162,
      "startLine": 1,
      "totalLines": 162
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T22:19:51.209Z_

<details><summary>↩ Tool result · `toolu_01Q8KECUBCzwTJrSFxpnD3Z4`</summary>

````text
# CIRCUS Methodology: Comprehensive Extraction

## 1. STABILITY MEASUREMENT

**What Varies:** "Config-bagging" varies **pruning thresholds** (node and edge cumulative-influence cutoffs), not random seeds or data subsets. The method applies B different threshold configurations to a **single attribution graph** without retraining.

**Config-Bagging Definition:** A deterministic design set of pruning configurations {πb} where each πb specifies node and edge thresholds. The paper uses B=25 (5×5 grid) for stability analysis and B=9 non-nested configurations for main evaluation. B=3 is used in some nested-config experiments.

**Critical Design Principle—Non-Nesting:** Configurations must cross thresholds in **opposite directions** to avoid degeneracy. Nested configs (where E(1)⊆E(2)⊆...⊆E(B)) cause consensus to equal the tightest single view. Non-nested examples: "(0.6,0.99)" retains few nodes but many edges; "(0.9,0.95)" does the opposite.

## 2. CONSENSUS MECHANISM

**Stability Score Formula:**
```
s(e) = (1/B) × Σ[b=1 to B] 𝟙[e ∈ E(b)]
```

This is **binary voting with continuous averaging**: each edge receives a frequency s(e)∈[0,1] representing the proportion of the B views in which it appears.

**Consensus Circuit Extraction:**
```
Cτ = {e : s(e) ≥ τ}
```

The paper primarily reports **strict consensus** with τ=1 (edges present in **every view**), though τ<1 permits exploratory larger sets.

**Threshold Rationale:** τ=1 yields an "all-views circuit"; the paper notes this is the "data-driven operating point" because C₁ remains within ~2% influence-retained (IR) of best single configs.

## 3. MODELS AND TASKS

**Models:**
- Gemma-2-2B
- Llama-3.2-1B

**Tasks/Behaviors:**
- Short factoid completions: capitals, arithmetic, trivia
- Paper explicitly states: "Prompts are short factoid completions (capitals, arithmetic, trivia); generalization to more complex behaviors (reasoning, in-context learning) remains open."

**Dataset Scale:**
- Gemma: 50 prompts
- Llama: 20 prompts

## 4. CIRCUIT DISCOVERY METHODS

**Single Underlying Method:** CIRCUS wraps **attribution graphs** produced by "cross-layer transcoders" (CLT replacement models), specifically implementations from Ameisen et al. (2025) and Hanna et al. (2025).

**No Algorithm Comparison:** The paper does **not** compare across different circuit discovery algorithms (EAP, ACDC, etc.). It varies **parameters within one pipeline**: pruning thresholds on a fixed attribution graph.

**Attribution Graph Properties:** Nodes are "learned features (produced by cross-layer transcoders, CLTs) and weighted edges represent direct causal effects between features" with weights W ∈ ℝ|E|.

## 5. FAITHFULNESS EVALUATION

**Metrics Used:**

1. **Influence Retained (IR):**
```
IR(S) = Φ(S) / Φ(E)
```
where Φ(S) = Σ|we| (sum of absolute edge weights). IR∈[0,1] measures "fraction of total attributed influence passes through S."

2. **KL Divergence (per-logit):**
```
DKL(pE || pS)
```
where pS(ℓ) = fraction of subgraph influence per output logit ℓ, pE(ℓ) = same for full graph. Consensus achieves "0.0010±0.0008 vs. 0.40±1.74 for union-pruned" (20 prompts, 17/20 wins).

3. **Activation Patching (Causal Validation):**
- Patches C₁ node activations from source prompt (different answer) to target
- Measures "recovery" = logit shift toward source answer
- Results: consensus 19.4 vs. random 6.8 vs. matched controls 1.6 (p=0.0004, Wilcoxon signed-rank)
- Consensus achieves "57% of oracle (34.2 recovery)" vs. "20% for random"

4. **Win-Rate Comparison:**
- Against union-pruned baseline: 47/50 prompts (Gemma), 19/20 (Llama) with B=9
- Against random baseline: 37/50 (Gemma), 20/20 (Llama)

**Comparative Claims:** Consensus achieves "~40× smaller than the union of all configurations while retaining comparable influence-flow explanatory power."

## 6. CORE/CONTINGENT/NOISE DECOMPOSITION

**Mathematical Definition:**

- **Core:** s(e)=1 (present in every view) → forms C₁
- **Contingent:** 0.5 ≤ s(e) < 1 (in at least half of views) → alternative pathways worth reporting
- **Noise:** s(e) < 0.5 (in fewer than half of views) → flagged for rejection/abstention

**Conceptual Role:** Paper states this "analogous to posterior model-inclusion indicators in Bayesian variable selection" enabling "the analyst to abstain from reporting unstable edges."

**Empirical Results:** On one nested B=3 experiment: "2.5% stability=1 (625 edges); 73% stability<0.5" and "6.2k contingent edges carrying 45% of total influence."

---

## Key Overhead
The full pipeline (attribution + B prunes + consensus + IR) adds **5.5% computational overhead** beyond a single attribution run (0.19s beyond baseline, consensus build <1ms).
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "af3663b2-a22b-434f-b98b-937962f1b07e",
  "tool_use_result": {
    "bytes": 142842,
    "code": 200,
    "codeText": "OK",
    "result": "# CIRCUS Methodology: Comprehensive Extraction\n\n## 1. STABILITY MEASUREMENT\n\n**What Varies:** \"Config-bagging\" varies **pruning thresholds** (node and edge cumulative-influence cutoffs), not random seeds or data subsets. The method applies B different threshold configurations to a **single attribution graph** without retraining.\n\n**Config-Bagging Definition:** A deterministic design set of pruning configurations {πb} where each πb specifies node and edge thresholds. The paper uses B=25 (5×5 grid) for stability analysis and B=9 non-nested configurations for main evaluation. B=3 is used in some nested-config experiments.\n\n**Critical Design Principle—Non-Nesting:** Configurations must cross thresholds in **opposite directions** to avoid degeneracy. Nested configs (where E(1)⊆E(2)⊆...⊆E(B)) cause consensus to equal the tightest single view. Non-nested examples: \"(0.6,0.99)\" retains few nodes but many edges; \"(0.9,0.95)\" does the opposite.\n\n## 2. CONSENSUS MECHANISM\n\n**Stability Score Formula:**\n```\ns(e) = (1/B) × Σ[b=1 to B] 𝟙[e ∈ E(b)]\n```\n\nThis is **binary voting with continuous averaging**: each edge receives a frequency s(e)∈[0,1] representing the proportion of the B views in which it appears.\n\n**Consensus Circuit Extraction:**\n```\nCτ = {e : s(e) ≥ τ}\n```\n\nThe paper primarily reports **strict consensus** with τ=1 (edges present in **every view**), though τ<1 permits exploratory larger sets.\n\n**Threshold Rationale:** τ=1 yields an \"all-views circuit\"; the paper notes this is the \"data-driven operating point\" because C₁ remains within ~2% influence-retained (IR) of best single configs.\n\n## 3. MODELS AND TASKS\n\n**Models:**\n- Gemma-2-2B\n- Llama-3.2-1B\n\n**Tasks/Behaviors:**\n- Short factoid completions: capitals, arithmetic, trivia\n- Paper explicitly states: \"Prompts are short factoid completions (capitals, arithmetic, trivia); generalization to more complex behaviors (reasoning, in-context learning) remains open.\"\n\n**Dataset Scale:**\n- Gemma: 50 prompts\n- Llama: 20 prompts\n\n## 4. CIRCUIT DISCOVERY METHODS\n\n**Single Underlying Method:** CIRCUS wraps **attribution graphs** produced by \"cross-layer transcoders\" (CLT replacement models), specifically implementations from Ameisen et al. (2025) and Hanna et al. (2025).\n\n**No Algorithm Comparison:** The paper does **not** compare across different circuit discovery algorithms (EAP, ACDC, etc.). It varies **parameters within one pipeline**: pruning thresholds on a fixed attribution graph.\n\n**Attribution Graph Properties:** Nodes are \"learned features (produced by cross-layer transcoders, CLTs) and weighted edges represent direct causal effects between features\" with weights W ∈ ℝ|E|.\n\n## 5. FAITHFULNESS EVALUATION\n\n**Metrics Used:**\n\n1. **Influence Retained (IR):**\n```\nIR(S) = Φ(S) / Φ(E)\n```\nwhere Φ(S) = Σ|we| (sum of absolute edge weights). IR∈[0,1] measures \"fraction of total attributed influence passes through S.\"\n\n2. **KL Divergence (per-logit):**\n```\nDKL(pE || pS)\n```\nwhere pS(ℓ) = fraction of subgraph influence per output logit ℓ, pE(ℓ) = same for full graph. Consensus achieves \"0.0010±0.0008 vs. 0.40±1.74 for union-pruned\" (20 prompts, 17/20 wins).\n\n3. **Activation Patching (Causal Validation):**\n- Patches C₁ node activations from source prompt (different answer) to target\n- Measures \"recovery\" = logit shift toward source answer\n- Results: consensus 19.4 vs. random 6.8 vs. matched controls 1.6 (p=0.0004, Wilcoxon signed-rank)\n- Consensus achieves \"57% of oracle (34.2 recovery)\" vs. \"20% for random\"\n\n4. **Win-Rate Comparison:**\n- Against union-pruned baseline: 47/50 prompts (Gemma), 19/20 (Llama) with B=9\n- Against random baseline: 37/50 (Gemma), 20/20 (Llama)\n\n**Comparative Claims:** Consensus achieves \"~40× smaller than the union of all configurations while retaining comparable influence-flow explanatory power.\"\n\n## 6. CORE/CONTINGENT/NOISE DECOMPOSITION\n\n**Mathematical Definition:**\n\n- **Core:** s(e)=1 (present in every view) → forms C₁\n- **Contingent:** 0.5 ≤ s(e) < 1 (in at least half of views) → alternative pathways worth reporting\n- **Noise:** s(e) < 0.5 (in fewer than half of views) → flagged for rejection/abstention\n\n**Conceptual Role:** Paper states this \"analogous to posterior model-inclusion indicators in Bayesian variable selection\" enabling \"the analyst to abstain from reporting unstable edges.\"\n\n**Empirical Results:** On one nested B=3 experiment: \"2.5% stability=1 (625 edges); 73% stability<0.5\" and \"6.2k contingent edges carrying 45% of total influence.\"\n\n---\n\n## Key Overhead\nThe full pipeline (attribution + B prunes + consensus + IR) adds **5.5% computational overhead** beyond a single attribution run (0.19s beyond baseline, consensus build <1ms).",
    "durationMs": 20198,
    "url": "https://arxiv.org/html/2603.00523"
  }
}
````

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
I now have very detailed information about CIRCUS. Let me also search for the GitHub repository and any additional details about whether CIRCUS has been applied to different circuit discovery algorithms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "a687959b-910b-4982-97b4-33de01676afa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGcZ3zGxDpTgxZ8PSqvxH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5132,
      "cache_creation_input_tokens": 2701,
      "cache_read_input_tokens": 28782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2701
      },
      "output_tokens": 9,
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

_source line 26_

已获取论文全文关键细节。再搜索 GitHub 仓库和后续引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "1536d8b1-7ae6-4807-b292-13b68cc1bb81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGcZ3zGxDpTgxZ8PSqvxH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5132,
      "cache_creation_input_tokens": 2701,
      "cache_read_input_tokens": 28782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2701
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KvzfbrhYhJL1UXKNYAAJHS`</summary>

```json
{
  "query": "CIRCUS \"Swapnil Parekh\" circuit consensus github code repository 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "d8fe5019-b470-4d80-a33e-135a9bcba317",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGcZ3zGxDpTgxZ8PSqvxH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5132,
      "cache_creation_input_tokens": 2701,
      "cache_read_input_tokens": 28782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2701
      },
      "output_tokens": 9,
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FMEg9VeqgwkQoeNshoGMeg`</summary>

```json
{
  "query": "\"2603.00523\" citing papers OR follow-up stability ensemble circuit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "125c6e57-4902-4560-8304-5bbe4d4925c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGcZ3zGxDpTgxZ8PSqvxH3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5132,
      "cache_creation_input_tokens": 2701,
      "cache_read_input_tokens": 28782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2701
      },
      "output_tokens": 9,
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

_source line 29 · 2026-05-12T22:20:02.389Z_

<details><summary>↩ Tool result · `toolu_01KvzfbrhYhJL1UXKNYAAJHS`</summary>

```text
Web search results for query: "CIRCUS "Swapnil Parekh" circuit consensus github code repository 2026"

Links: [{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Swapnil Parekh – AI","url":"https://swapnilparekh.github.io/"},{"title":"Swapnil Srivastava — Full Stack Engineer","url":"https://swapnilsparsh.github.io/"},{"title":"swapnilsparsh (Swapnil Srivastava) · GitHub","url":"https://github.com/swapnilsparsh"},{"title":"Swapnil Parekh - Intuit | LinkedIn","url":"https://www.linkedin.com/in/swapnil-parekh/"},{"title":"swapagarwal (Swapnil Agarwal) · GitHub","url":"https://github.com/swapagarwal"},{"title":"Swapnil Joshi & Manasi Parekh Ke Saath Movie Talk, Bharela Ringan Batata Nu Shaak Aur Fajeto! - YouTube","url":"https://www.youtube.com/watch?v=ONhbc_6ayV4"},{"title":"circuit-simulator · GitHub Topics · GitHub","url":"https://github.com/topics/circuit-simulator"},{"title":"GitHub - midas-research/data-free-uats","url":"https://github.com/midas-research/data-free-uats"},{"title":"Swapnil Mishra","url":"https://s-mishra.github.io/"}]

Based on the search results, I found information about the CIRCUS research:

CIRCUS is a paper titled "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles" by Swapnil Parekh, which was submitted on February 28, 2026.

The method constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score, and extracts a strict-consensus circuit consisting only of edges that appear in all views, producing a threshold-robust "core" circuit while explicitly surfacing contingent alternatives.

On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power.

The paper is available on arXiv (arxiv.org/abs/2603.00523). However, the search results did not return a specific GitHub code repository link for this project. You may want to check the arXiv paper page directly or look for the authors' GitHub profiles for the code repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "c74eb613-b0bc-482d-99ce-68f0d12ec256",
  "tool_use_result": {
    "query": "CIRCUS \"Swapnil Parekh\" circuit consensus github code repository 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Rc2TtfkT1o3dq9YccWkQ5z",
        "content": [
          {
            "title": "[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/abs/2603.00523"
          },
          {
            "title": "Swapnil Parekh – AI",
            "url": "https://swapnilparekh.github.io/"
          },
          {
            "title": "Swapnil Srivastava — Full Stack Engineer",
            "url": "https://swapnilsparsh.github.io/"
          },
          {
            "title": "swapnilsparsh (Swapnil Srivastava) · GitHub",
            "url": "https://github.com/swapnilsparsh"
          },
          {
            "title": "Swapnil Parekh - Intuit | LinkedIn",
            "url": "https://www.linkedin.com/in/swapnil-parekh/"
          },
          {
            "title": "swapagarwal (Swapnil Agarwal) · GitHub",
            "url": "https://github.com/swapagarwal"
          },
          {
            "title": "Swapnil Joshi & Manasi Parekh Ke Saath Movie Talk, Bharela Ringan Batata Nu Shaak Aur Fajeto! - YouTube",
            "url": "https://www.youtube.com/watch?v=ONhbc_6ayV4"
          },
          {
            "title": "circuit-simulator · GitHub Topics · GitHub",
            "url": "https://github.com/topics/circuit-simulator"
          },
          {
            "title": "GitHub - midas-research/data-free-uats",
            "url": "https://github.com/midas-research/data-free-uats"
          },
          {
            "title": "Swapnil Mishra",
            "url": "https://s-mishra.github.io/"
          }
        ]
      },
      "Based on the search results, I found information about the CIRCUS research:\n\nCIRCUS is a paper titled \"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\" by Swapnil Parekh, which was submitted on February 28, 2026.\n\nThe method constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score, and extracts a strict-consensus circuit consisting only of edges that appear in all views, producing a threshold-robust \"core\" circuit while explicitly surfacing contingent alternatives.\n\nOn Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power.\n\nThe paper is available on arXiv (arxiv.org/abs/2603.00523). However, the search results did not return a specific GitHub code repository link for this project. You may want to check the arXiv paper page directly or look for the authors' GitHub profiles for the code repository."
    ],
    "durationSeconds": 6.0935492789999985
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T22:20:02.892Z_

<details><summary>↩ Tool result · `toolu_01FMEg9VeqgwkQoeNshoGMeg`</summary>

```text
Web search results for query: ""2603.00523" citing papers OR follow-up stability ensemble circuit"

Links: [{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"Stability-Weighted Ensemble Feature Importance for Financial Applications by Hamid R. Arian, Seyed Alireza Mousavizade, Luis A. Seco :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4905824"},{"title":"ELAVL1 primarily couples mRNA stability with the 3 - UTRs ...","url":"https://www.cell.com/cell-reports/pdf/S2211-1247(21)00523-4.pdf"},{"title":"3600 Market Street, 6th Floor Philadelphia, PA 19104-2688 U.S.","url":"https://www.siam.org/media/kuib0myo/ds25_abstracts.pdf"},{"title":"i POWER SYSTEM DYNAMICS AND STABILITY Peter W. Sauer and M. A. Pai","url":"https://courses.physics.illinois.edu/ece576/sp2018/Sauer%20and%20Pai%20book%20-%20Jan%202007.pdf"},{"title":"Chapter 6 Stability and nonlinear dynamics in thyristor and diode circuits","url":"https://iandobson.ece.iastate.edu/PAPERS/dobsonPEchapter01.pdf"},{"title":"Top arXiv papers","url":"https://scirate.com/?archive=quant-ph&date=2026-03-03&page=22&range=1"},{"title":"Definition and Classification of Power System Stability","url":"https://home.engineering.iastate.edu/~jdm/ee554/TermsDefinitions2004.pdf"},{"title":"Power System Stability and Control - Prabha Kundur ( ...","url":"https://dl.poweren.ir/downloads/PowerEn/Book/2019/Jun/Power%20System%20Stability%20and%20Control%20-%20Prabha%20Kundur%20(PowerEn.ir).pdf"}]

Based on the search results, I found the paper you're looking for:

The paper with ID 2603.00523 is titled "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles" by Swapnil Parekh, submitted on February 28, 2026.

**Overview of the paper:**

The paper addresses how mechanistic circuit discovery is sensitive to arbitrary analyst choices like pruning thresholds and feature dictionaries, and reframes circuit discovery as an uncertainty-quantification problem over these analytic degrees of freedom.

**The CIRCUS method:**

CIRCUS constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views. This produces a threshold-robust "core" circuit while explicitly surfacing contingent alternatives and enabling rejection of low-agreement structure, and requires no retraining with negligible overhead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "2e7e1f4f-18e0-4800-a546-e8b2c8e1b841",
  "tool_use_result": {
    "query": "\"2603.00523\" citing papers OR follow-up stability ensemble circuit",
    "results": [
      {
        "tool_use_id": "srvtoolu_011evGrTUtekEqm8ki7L2p7b",
        "content": [
          {
            "title": "[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/abs/2603.00523"
          },
          {
            "title": "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles",
            "url": "https://arxiv.org/html/2603.00523"
          },
          {
            "title": "Stability-Weighted Ensemble Feature Importance for Financial Applications by Hamid R. Arian, Seyed Alireza Mousavizade, Luis A. Seco :: SSRN",
            "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4905824"
          },
          {
            "title": "ELAVL1 primarily couples mRNA stability with the 3 - UTRs ...",
            "url": "https://www.cell.com/cell-reports/pdf/S2211-1247(21)00523-4.pdf"
          },
          {
            "title": "3600 Market Street, 6th Floor Philadelphia, PA 19104-2688 U.S.",
            "url": "https://www.siam.org/media/kuib0myo/ds25_abstracts.pdf"
          },
          {
            "title": "i POWER SYSTEM DYNAMICS AND STABILITY Peter W. Sauer and M. A. Pai",
            "url": "https://courses.physics.illinois.edu/ece576/sp2018/Sauer%20and%20Pai%20book%20-%20Jan%202007.pdf"
          },
          {
            "title": "Chapter 6 Stability and nonlinear dynamics in thyristor and diode circuits",
            "url": "https://iandobson.ece.iastate.edu/PAPERS/dobsonPEchapter01.pdf"
          },
          {
            "title": "Top arXiv papers",
            "url": "https://scirate.com/?archive=quant-ph&date=2026-03-03&page=22&range=1"
          },
          {
            "title": "Definition and Classification of Power System Stability",
            "url": "https://home.engineering.iastate.edu/~jdm/ee554/TermsDefinitions2004.pdf"
          },
          {
            "title": "Power System Stability and Control - Prabha Kundur ( ...",
            "url": "https://dl.poweren.ir/downloads/PowerEn/Book/2019/Jun/Power%20System%20Stability%20and%20Control%20-%20Prabha%20Kundur%20(PowerEn.ir).pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper with ID 2603.00523 is titled \"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\" by Swapnil Parekh, submitted on February 28, 2026.\n\n**Overview of the paper:**\n\nThe paper addresses how mechanistic circuit discovery is sensitive to arbitrary analyst choices like pruning thresholds and feature dictionaries, and reframes circuit discovery as an uncertainty-quantification problem over these analytic degrees of freedom.\n\n**The CIRCUS method:**\n\nCIRCUS constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views. This produces a threshold-robust \"core\" circuit while explicitly surfacing contingent alternatives and enabling rejection of low-agreement structure, and requires no retraining with negligible overhead."
    ],
    "durationSeconds": 6.040928541999994
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the author's personal page for any code/GitHub link, and look for more details about the cross-layer transcoders used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "d44561c2-dffb-45f9-a3f9-2a2ce48d2911",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Xyk5d5k4bh7USL96RtyPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6904,
      "cache_read_input_tokens": 31483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6904
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

_source line 32_

没有找到公开的 GitHub 仓库。让我检查作者主页看是否有代码链接，并补充搜索 CIRCUS 使用的具体 attribution 方法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "0694150c-f5e9-4864-afda-e0099ace23c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Xyk5d5k4bh7USL96RtyPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6904,
      "cache_read_input_tokens": 31483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6904
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

_source line 33_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011DHh2zaQtKigzzLvjthhVW`</summary>

```json
{
  "url": "https://swapnilparekh.github.io/",
  "prompt": "Look for any GitHub links, code repositories, or project pages related to CIRCUS or circuit discovery. Also note the author's affiliation and other publications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "75925f2d-12f3-46e7-a531-8457843234ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Xyk5d5k4bh7USL96RtyPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6904,
      "cache_read_input_tokens": 31483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6904
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

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AZnNRiBVEppDA9kkURTxFp`</summary>

```json
{
  "query": "CIRCUS circuit discovery \"cross-layer transcoders\" OR \"attribution graph\" EAP ACDC \"single method\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "8e643242-5e34-423c-8a83-ca877e23e54f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Xyk5d5k4bh7USL96RtyPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6904,
      "cache_read_input_tokens": 31483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6904
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

_source line 35 · 2026-05-12T22:20:17.027Z_

<details><summary>↩ Tool result · `toolu_011DHh2zaQtKigzzLvjthhVW`</summary>

```text
# Response: GitHub Links and CIRCUS-Related Content

Based on the web page content provided, I found **no references to CIRCUS or circuit discovery projects**, and **no GitHub repository links** are displayed on this portfolio page.

## What I Found:

**GitHub Profile Link:**
The page includes a GitHub icon link at the bottom (to https://github.com/SwapnilDreams100), but no specific repositories or projects are listed.

**Author Information:**
Swapnil Parekh identifies as an "AI Scientist" specializing in mechanistic interpretability, adversarial robustness, and agentic systems. His most relevant publication for circuit-related work appears to be:

- "The Parliament in the Model: How Neural Circuits Reach Consensus" (April 2024), which discusses how "specific computational subgraphs, attention heads, MLP layers, residual stream connections" operate within language models.

**Affiliation:**
No institutional affiliation is mentioned on this page.

## Conclusion:

To locate CIRCUS-related code or circuit discovery projects, you would need to visit his GitHub profile directly or contact the author, as this portfolio page doesn't enumerate specific repositories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "4a20ec3f-8ad2-49e0-89ca-2d7b18235b76",
  "tool_use_result": {
    "bytes": 13418,
    "code": 200,
    "codeText": "OK",
    "result": "# Response: GitHub Links and CIRCUS-Related Content\n\nBased on the web page content provided, I found **no references to CIRCUS or circuit discovery projects**, and **no GitHub repository links** are displayed on this portfolio page.\n\n## What I Found:\n\n**GitHub Profile Link:**\nThe page includes a GitHub icon link at the bottom (to https://github.com/SwapnilDreams100), but no specific repositories or projects are listed.\n\n**Author Information:**\nSwapnil Parekh identifies as an \"AI Scientist\" specializing in mechanistic interpretability, adversarial robustness, and agentic systems. His most relevant publication for circuit-related work appears to be:\n\n- \"The Parliament in the Model: How Neural Circuits Reach Consensus\" (April 2024), which discusses how \"specific computational subgraphs, attention heads, MLP layers, residual stream connections\" operate within language models.\n\n**Affiliation:**\nNo institutional affiliation is mentioned on this page.\n\n## Conclusion:\n\nTo locate CIRCUS-related code or circuit discovery projects, you would need to visit his GitHub profile directly or contact the author, as this portfolio page doesn't enumerate specific repositories.",
    "durationMs": 7831,
    "url": "https://swapnilparekh.github.io/"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T22:20:26.712Z_

<details><summary>↩ Tool result · `toolu_01AZnNRiBVEppDA9kkURTxFp`</summary>

```text
Web search results for query: "CIRCUS circuit discovery "cross-layer transcoders" OR "attribution graph" EAP ACDC "single method" 2026"

Links: [{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://www.arxiv.org/pdf/2510.03282"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://aclanthology.org/2024.blackboxnlp-1.25.pdf"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"Sparse Crosscoders for Cross-Layer Features and Model Diffing","url":"https://transformer-circuits.pub/2024/crosscoders/index.html"},{"title":"Cross-Layer Transcoders (CLTs)","url":"https://www.emergentmind.com/topics/cross-layer-transcoders-clts"},{"title":"Circuit Tracing with the Qwen3 Cross-Layer Transcoders — BluelightAI","url":"https://www.bluelightai.com/blog/circuit-tracing-with-qwen3/"},{"title":"Circuit Tracing: A Step Closer to Understanding Large Language Models | Towards Data Science","url":"https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/"}]

Based on the web search results, I found relevant information about the topics you searched for. Here's what I found:

## Circuit Discovery Methods

EAP outperforms all previous methods for circuit discovery, since it is competitive with ACDC on recovering circuits while significantly reducing the computational demand. ACDC recursively applies activation patching—replacing activations with those from "corrupted" examples—removing edges that do not degrade task metric performance.

## Cross-Layer Transcoders and Attribution Graphs

Cross-layer transcoders (CLT) enable each feature to read from the residual stream at one layer and contribute to the outputs of all subsequent MLP layers of the original model, which greatly simplifies the resulting circuits. Attribution graphs support understanding simple behaviors of an 18-layer language model.

The CLT-based approach to circuit discovery uses objects known as attribution graphs, which link together groups of CLT features into a network whose edges represent causal influences of one feature on another.

## Recent Applications (2026)

On GPT-2, CLTs achieve explained variance ≈0.8, replacement score ≈0.8, and attribution graph completeness ≈0.95 under standard prompts. Activation caching and distributed sharding enable end-to-end pipelines at trillion-token scales and with models exceeding 1B parameters.

The search results show active ongoing research in circuit discovery combining these methods for improved mechanistic interpretability of language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "57b81fe7-903a-476d-9735-efa7e2066fb0",
  "tool_use_result": {
    "query": "CIRCUS circuit discovery \"cross-layer transcoders\" OR \"attribution graph\" EAP ACDC \"single method\" 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uwz5kjQDexRMF5xheugFFJ",
        "content": [
          {
            "title": "Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed",
            "url": "https://openreview.net/pdf?id=tiLbFR4bJW"
          },
          {
            "title": "Automatic Circuit Discovery",
            "url": "https://sidn.baulab.info/autocircuits/"
          },
          {
            "title": "Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework",
            "url": "https://www.arxiv.org/pdf/2510.03282"
          },
          {
            "title": "Circuit Tracing: Revealing Computational Graphs in Language Models",
            "url": "https://transformer-circuits.pub/2025/attribution-graphs/methods.html"
          },
          {
            "title": "Attribution Patching Outperforms Automated Circuit Discovery",
            "url": "https://aclanthology.org/2024.blackboxnlp-1.25.pdf"
          },
          {
            "title": "Transcoders find interpretable LLM feature circuits",
            "url": "https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"
          },
          {
            "title": "Sparse Crosscoders for Cross-Layer Features and Model Diffing",
            "url": "https://transformer-circuits.pub/2024/crosscoders/index.html"
          },
          {
            "title": "Cross-Layer Transcoders (CLTs)",
            "url": "https://www.emergentmind.com/topics/cross-layer-transcoders-clts"
          },
          {
            "title": "Circuit Tracing with the Qwen3 Cross-Layer Transcoders — BluelightAI",
            "url": "https://www.bluelightai.com/blog/circuit-tracing-with-qwen3/"
          },
          {
            "title": "Circuit Tracing: A Step Closer to Understanding Large Language Models | Towards Data Science",
            "url": "https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/"
          }
        ]
      },
      "Based on the web search results, I found relevant information about the topics you searched for. Here's what I found:\n\n## Circuit Discovery Methods\n\nEAP outperforms all previous methods for circuit discovery, since it is competitive with ACDC on recovering circuits while significantly reducing the computational demand. ACDC recursively applies activation patching—replacing activations with those from \"corrupted\" examples—removing edges that do not degrade task metric performance.\n\n## Cross-Layer Transcoders and Attribution Graphs\n\nCross-layer transcoders (CLT) enable each feature to read from the residual stream at one layer and contribute to the outputs of all subsequent MLP layers of the original model, which greatly simplifies the resulting circuits. Attribution graphs support understanding simple behaviors of an 18-layer language model.\n\nThe CLT-based approach to circuit discovery uses objects known as attribution graphs, which link together groups of CLT features into a network whose edges represent causal influences of one feature on another.\n\n## Recent Applications (2026)\n\nOn GPT-2, CLTs achieve explained variance ≈0.8, replacement score ≈0.8, and attribution graph completeness ≈0.95 under standard prompts. Activation caching and distributed sharding enable end-to-end pipelines at trillion-token scales and with models exceeding 1B parameters.\n\nThe search results show active ongoing research in circuit discovery combining these methods for improved mechanistic interpretability of language models."
    ],
    "durationSeconds": 16.772239812
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive information about CIRCUS. Let me compile everything and write the updated related_work_notes.md. Key findings:

**Q1: What does CIRCUS vary to test stability?**
- Varies pruning thresholds (node and edge cumulative-influence cutoffs), NOT random seeds or data subsets
- Config-bagging: deterministic design set of pruning configurations {πb}, each specifying node and edge thresholds
- B=25 (5×5 grid) for stability analysis, B=9 non-nested configurations for main evaluation, B=3 for some nested experiments


- Configurations must be non-nested, crossing thresholds in opposite directions to ensure diversity

**Q2: Consensus mechanism**
- Stability score measures the fraction of configurations that retain each edge, with strict consensus (τ=1) being the primary threshold
- Edges are classified into core (retained across all configs), contingent (retained in some), and noise (rarely retained) based on their stability scores
- Models tested include Gemma-2 across various tasks like factoid completions and arithmetic, with Llama-3.2-1B on a smaller prompt set

**Q4: Faithfulness evaluation**
- The consensus approach dramatically outperforms union-pruned circuits on KL divergence and activation patching metrics, with strong win rates across both model families
- CIRCUS doesn't actually compare across different circuit discovery algorithms—that's not what this method does

**Q5: Cross-method comparison - THE KEY QUESTION**
- CIRCUS works exclusively with attribution graphs derived from cross-layer transcoders, only varying the pruning thresholds applied to that single pipeline
- This focused approach on a single underlying method is what sets CIRCUS apart

Now I'm updating the artifacts/related_work_notes.md file to add the deep CIRCUS analysis section...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "21f01145-a0e0-4e13-8669-c0449459dc11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcbbHK5eEsYj5toamCgmYf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 38387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1420
      },
      "output_tokens": 9,
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

_source line 38_

信息充分。现在生成 CIRCUS 深度分析并追加到笔记。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "811afc04-286b-40cc-bb45-c745b1673e0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcbbHK5eEsYj5toamCgmYf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 38387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1420
      },
      "output_tokens": 9,
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01PjcHBDsegRaF6z3yDDaVwe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "offset": 155
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "9c731522-47a9-4514-a6fc-6551ade21557",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcbbHK5eEsYj5toamCgmYf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 38387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1420
      },
      "output_tokens": 9,
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

_source line 40 · 2026-05-12T22:20:48.747Z_

<details><summary>↩ Tool result · `toolu_01PjcHBDsegRaF6z3yDDaVwe`</summary>

```text
155	4. **非唯一性问题 (ICLR 2025 "Everything Everywhere All at Once")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。
156	
157	#### 🎯 差异化建议
158	
159	- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。
160	- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。
161	- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。
162	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "bd30e0d0-551b-4ba6-a040-c5f002ef7561",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
      "content": "4. **非唯一性问题 (ICLR 2025 \"Everything Everywhere All at Once\")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。\n\n#### 🎯 差异化建议\n\n- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。\n- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。\n- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n",
      "numLines": 8,
      "startLine": 155,
      "totalLines": 162
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_018rkgyGoM4oA3jDR5YmjK3K`</summary>

````json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "old_string": "- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。",
  "new_string": "- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n\n---\n\n## 1b. CIRCUS 深度分析\n\n> 论文：CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles (arXiv 2603.00523, 2026.02.28)\n> 作者：Swapnil Parekh\n> 代码：未公开（GitHub: SwapnilDreams100，未找到 CIRCUS 仓库）\n\n### 方法细节\n\n**Stability 测量机制：变化剪枝阈值，不变种子/数据。**\n\nCIRCUS 对**单一 attribution graph**（由 cross-layer transcoders 生成的归因图）施加 B 组不同的剪枝配置 {π₁, ..., πB}，每组配置指定不同的 node threshold 和 edge threshold（cumulative-influence cutoffs）。**不涉及**随机种子变化或数据子集变化。\n\n**Config-bagging 参数：**\n- B=25（5×5 grid）用于 stability 分析\n- B=9（non-nested configurations）用于主实验评估\n- B=3 用于嵌套配置消融实验\n- **关键设计约束——non-nesting**：配置必须在不同维度上交叉变化（如 (0.6, 0.99) 保留少 node 多 edge，(0.9, 0.95) 相反），避免 E(1)⊆E(2)⊆...⊆E(B) 导致 consensus 退化为最严格单配置\n\n**Consensus 公式：**\n\nstability score（per-edge inclusion frequency）：\n```\ns(e) = (1/B) × Σ_{b=1}^{B} 𝟙[e ∈ E(b)]\n```\n\nconsensus circuit 提取：\n```\nC_τ = {e : s(e) ≥ τ}\n```\n\n主实验使用 **strict consensus τ=1**（边必须在所有配置中存在）。τ<1 可用于探索性分析。\n\n**Core/Contingent/Noise 分类：**\n| 类别 | 定义 | 含义 |\n|------|------|------|\n| Core | s(e) = 1 | 所有配置都保留，鲁棒结构 |\n| Contingent | 0.5 ≤ s(e) < 1 | 多数配置保留，替代路径 |\n| Noise | s(e) < 0.5 | 少数配置保留，阈值敏感伪影 |\n\n类比 Bayesian variable selection 中的 posterior model-inclusion indicators。\n\n### 实验设置\n\n**模型：**\n- Gemma-2-2B\n- Llama-3.2-1B\n\n**任务：**\n- Short factoid completions：capitals, arithmetic, trivia\n- 数据规模：50 prompts (Gemma), 20 prompts (Llama)\n- 论文明确承认局限：\"generalization to more complex behaviors (reasoning, in-context learning) remains open\"\n\n**使用的 circuit discovery 方法：仅一种。**\n- 底层方法：cross-layer transcoders (CLTs) 生成的 attribution graphs（引用 Ameisen et al. 2025, Hanna et al. 2025）\n- 节点 = learned features（CLT 特征），边 = features 间的直接因果效应，权重 W ∈ ℝ^{|E|}\n- **不使用** EAP, ACDC, Edge Pruning 或其他传统 circuit discovery 方法\n- **不跨方法比较**\n\n### Faithfulness 评估\n\n**Metrics：**\n\n1. **Influence Retained (IR)**：IR(S) = Φ(S)/Φ(E)，其中 Φ(S) = Σ|w_e| 为子图绝对边权之和。衡量通过子图 S 的总归因影响比例。\n\n2. **KL Divergence（per-logit）**：D_KL(p_E || p_S)，consensus 达到 0.0010±0.0008 vs union-pruned 0.40±1.74（20 prompts, 17/20 wins）。\n\n3. **Activation Patching（因果验证）**：\n   - Patch C₁ 节点激活从 source prompt → target prompt\n   - Recovery: consensus 19.4 vs random 6.8 vs matched controls 1.6\n   - p=0.0004 (Wilcoxon signed-rank)\n   - Consensus = oracle 的 57%，random = 20%\n\n4. **Win-rate**：\n   - vs union-pruned: 47/50 (Gemma), 19/20 (Llama) with B=9\n   - vs random: 37/50 (Gemma), 20/20 (Llama)\n\n**关键结论：** strict consensus circuit ~40× smaller than union，但保持 comparable influence-flow 解释力。overhead 仅 5.5%（<1ms consensus 构建）。\n\n### 跨方法比较\n\n**CIRCUS 没有做跨方法比较。** 这是确认的事实：\n- 仅使用 CLT attribution graphs 一种 pipeline\n- 变化的是该 pipeline 内的剪枝阈值配置\n- 不涉及 EAP, ACDC, Edge Pruning, SP 等任何其他 circuit discovery 算法\n- **这是 CSS 的核心差异点**\n\n### CSS vs CIRCUS 精确差异表\n\n| 维度 | CIRCUS | CSS (ours) |\n|------|--------|-----------|\n| **变化什么** | 单方法内的剪枝阈值 (node/edge cutoffs) | 算法族 (gradient/mask/causal 等不同范式) |\n| **底层方法数** | 1 种 (CLT attribution graphs) | K=3+ 种根本不同的算法 (如 EAP, ACDC, EP) |\n| **稳定性来源** | Intra-method: 阈值鲁棒性 (Rashomon set) | Cross-method: 算法族间一致性 (不同 inductive bias) |\n| **聚合方式** | 连续 stability score s(e)∈[0,1] + strict consensus τ=1 | 二值投票 (K 方法中 ≥ threshold 方法包含 edge) |\n| **输入** | 单次 attribution run 的一张归因图 | 每种方法独立运行产出的 K 张电路图 |\n| **计算开销** | 极低 (5.5% overhead, 不需重新计算归因) | 需要运行 K 种不同算法 (各自完整 pipeline) |\n| **模型规模** | Gemma-2-2B, Llama-3.2-1B | 待定 |\n| **任务类型** | Short factoid completions | 待定 |\n| **core claim** | 阈值变化下的鲁棒核心 vs 阈值敏感伪影 | 跨算法族共识比单方法更鲁棒、更可信 |\n| **方法间差异分析** | ❌ 不分析 | ✅ Pairwise Jaccard matrix / agreement heatmap |\n| **taxonomy 基础** | 同方法不同参数的 inclusion frequency | 不同方法的 agreement count |\n\n### 关键论点：为何 cross-method > intra-method\n\n1. **不同 inductive bias**：EAP 基于梯度归因，ACDC 基于 activation patching（因果干预），EP 基于可微剪枝。它们从根本不同的角度逼近\"重要边\"。阈值变化只探索同一视角的灵敏度。\n2. **信息正交性**：跨方法共识的边同时被梯度信号、因果干预和优化剪枝确认，信息量远大于同方法不同阈值。\n3. **实用价值**：如果研究者只有一种方法，CIRCUS 有用；如果研究者想知道\"哪些结构是方法无关的\"，CSS 回答的是不同的问题。\n4. **Méloux et al. 的启示**：单方法内 Jaccard 仅 0.561，说明 intra-method 变异已经很大。跨方法共识可能提供更稳定的 core（或发现更大的分歧——这本身也是重要发现）。"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "7efc159f-bce4-4bec-8cbb-6f632dddaa39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dTp5T5KfT1pbPVybWCXUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 39807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1020
      },
      "output_tokens": 59,
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

_source line 42 · 2026-05-12T22:21:44.731Z_

<details><summary>↩ Tool result · `toolu_018rkgyGoM4oA3jDR5YmjK3K`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "b39a116c-28ad-4ca1-8d62-0d7de8ba3402",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
    "oldString": "- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。",
    "newString": "- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n\n---\n\n## 1b. CIRCUS 深度分析\n\n> 论文：CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles (arXiv 2603.00523, 2026.02.28)\n> 作者：Swapnil Parekh\n> 代码：未公开（GitHub: SwapnilDreams100，未找到 CIRCUS 仓库）\n\n### 方法细节\n\n**Stability 测量机制：变化剪枝阈值，不变种子/数据。**\n\nCIRCUS 对**单一 attribution graph**（由 cross-layer transcoders 生成的归因图）施加 B 组不同的剪枝配置 {π₁, ..., πB}，每组配置指定不同的 node threshold 和 edge threshold（cumulative-influence cutoffs）。**不涉及**随机种子变化或数据子集变化。\n\n**Config-bagging 参数：**\n- B=25（5×5 grid）用于 stability 分析\n- B=9（non-nested configurations）用于主实验评估\n- B=3 用于嵌套配置消融实验\n- **关键设计约束——non-nesting**：配置必须在不同维度上交叉变化（如 (0.6, 0.99) 保留少 node 多 edge，(0.9, 0.95) 相反），避免 E(1)⊆E(2)⊆...⊆E(B) 导致 consensus 退化为最严格单配置\n\n**Consensus 公式：**\n\nstability score（per-edge inclusion frequency）：\n```\ns(e) = (1/B) × Σ_{b=1}^{B} 𝟙[e ∈ E(b)]\n```\n\nconsensus circuit 提取：\n```\nC_τ = {e : s(e) ≥ τ}\n```\n\n主实验使用 **strict consensus τ=1**（边必须在所有配置中存在）。τ<1 可用于探索性分析。\n\n**Core/Contingent/Noise 分类：**\n| 类别 | 定义 | 含义 |\n|------|------|------|\n| Core | s(e) = 1 | 所有配置都保留，鲁棒结构 |\n| Contingent | 0.5 ≤ s(e) < 1 | 多数配置保留，替代路径 |\n| Noise | s(e) < 0.5 | 少数配置保留，阈值敏感伪影 |\n\n类比 Bayesian variable selection 中的 posterior model-inclusion indicators。\n\n### 实验设置\n\n**模型：**\n- Gemma-2-2B\n- Llama-3.2-1B\n\n**任务：**\n- Short factoid completions：capitals, arithmetic, trivia\n- 数据规模：50 prompts (Gemma), 20 prompts (Llama)\n- 论文明确承认局限：\"generalization to more complex behaviors (reasoning, in-context learning) remains open\"\n\n**使用的 circuit discovery 方法：仅一种。**\n- 底层方法：cross-layer transcoders (CLTs) 生成的 attribution graphs（引用 Ameisen et al. 2025, Hanna et al. 2025）\n- 节点 = learned features（CLT 特征），边 = features 间的直接因果效应，权重 W ∈ ℝ^{|E|}\n- **不使用** EAP, ACDC, Edge Pruning 或其他传统 circuit discovery 方法\n- **不跨方法比较**\n\n### Faithfulness 评估\n\n**Metrics：**\n\n1. **Influence Retained (IR)**：IR(S) = Φ(S)/Φ(E)，其中 Φ(S) = Σ|w_e| 为子图绝对边权之和。衡量通过子图 S 的总归因影响比例。\n\n2. **KL Divergence（per-logit）**：D_KL(p_E || p_S)，consensus 达到 0.0010±0.0008 vs union-pruned 0.40±1.74（20 prompts, 17/20 wins）。\n\n3. **Activation Patching（因果验证）**：\n   - Patch C₁ 节点激活从 source prompt → target prompt\n   - Recovery: consensus 19.4 vs random 6.8 vs matched controls 1.6\n   - p=0.0004 (Wilcoxon signed-rank)\n   - Consensus = oracle 的 57%，random = 20%\n\n4. **Win-rate**：\n   - vs union-pruned: 47/50 (Gemma), 19/20 (Llama) with B=9\n   - vs random: 37/50 (Gemma), 20/20 (Llama)\n\n**关键结论：** strict consensus circuit ~40× smaller than union，但保持 comparable influence-flow 解释力。overhead 仅 5.5%（<1ms consensus 构建）。\n\n### 跨方法比较\n\n**CIRCUS 没有做跨方法比较。** 这是确认的事实：\n- 仅使用 CLT attribution graphs 一种 pipeline\n- 变化的是该 pipeline 内的剪枝阈值配置\n- 不涉及 EAP, ACDC, Edge Pruning, SP 等任何其他 circuit discovery 算法\n- **这是 CSS 的核心差异点**\n\n### CSS vs CIRCUS 精确差异表\n\n| 维度 | CIRCUS | CSS (ours) |\n|------|--------|-----------|\n| **变化什么** | 单方法内的剪枝阈值 (node/edge cutoffs) | 算法族 (gradient/mask/causal 等不同范式) |\n| **底层方法数** | 1 种 (CLT attribution graphs) | K=3+ 种根本不同的算法 (如 EAP, ACDC, EP) |\n| **稳定性来源** | Intra-method: 阈值鲁棒性 (Rashomon set) | Cross-method: 算法族间一致性 (不同 inductive bias) |\n| **聚合方式** | 连续 stability score s(e)∈[0,1] + strict consensus τ=1 | 二值投票 (K 方法中 ≥ threshold 方法包含 edge) |\n| **输入** | 单次 attribution run 的一张归因图 | 每种方法独立运行产出的 K 张电路图 |\n| **计算开销** | 极低 (5.5% overhead, 不需重新计算归因) | 需要运行 K 种不同算法 (各自完整 pipeline) |\n| **模型规模** | Gemma-2-2B, Llama-3.2-1B | 待定 |\n| **任务类型** | Short factoid completions | 待定 |\n| **core claim** | 阈值变化下的鲁棒核心 vs 阈值敏感伪影 | 跨算法族共识比单方法更鲁棒、更可信 |\n| **方法间差异分析** | ❌ 不分析 | ✅ Pairwise Jaccard matrix / agreement heatmap |\n| **taxonomy 基础** | 同方法不同参数的 inclusion frequency | 不同方法的 agreement count |\n\n### 关键论点：为何 cross-method > intra-method\n\n1. **不同 inductive bias**：EAP 基于梯度归因，ACDC 基于 activation patching（因果干预），EP 基于可微剪枝。它们从根本不同的角度逼近\"重要边\"。阈值变化只探索同一视角的灵敏度。\n2. **信息正交性**：跨方法共识的边同时被梯度信号、因果干预和优化剪枝确认，信息量远大于同方法不同阈值。\n3. **实用价值**：如果研究者只有一种方法，CIRCUS 有用；如果研究者想知道\"哪些结构是方法无关的\"，CSS 回答的是不同的问题。\n4. **Méloux et al. 的启示**：单方法内 Jaccard 仅 0.561，说明 intra-method 变异已经很大。跨方法共识可能提供更稳定的 core（或发现更大的分歧——这本身也是重要发现）。",
    "originalFile": "# Circuit Discovery Related Work Notes (2024-2026)\n\n> 调研日期：2026-05-12 | 项目：structfuse-context\n> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？\n\n---\n\n## 1. 方法一致性比较（Novelty 关键）\n\n**结论：没有论文以\"跨方法一致性分析\"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。\n\n### 直接比较多方法的论文\n\n| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |\n|------|----------|----------|---------------------|\n| Conmy et al. \"Towards Automated Circuit Discovery\" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |\n| Syed et al. \"Attribution Patching Outperforms Automated Circuit Discovery\" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |\n| Bhaskar et al. \"Finding Transformer Circuits with Edge Pruning\" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |\n| Hsu et al. \"CD-T\" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |\n| Edin et al. \"GIM\" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |\n| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |\n\n### 最接近\"一致性分析\"的论文\n\n**Hanna et al. \"Have Faith in Faithfulness: Going Beyond Circuit Overlap\" (2024, arXiv 2403.17806)**\n- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大\n- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价\n- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究\n\n**Méloux et al. \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\" (2025, arXiv 2510.00845)**\n- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561\n- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等\n- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法\n\n**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**\n\n---\n\n## 2. Circuit Aggregation / Ensemble（Novelty 威胁）\n\n### 🔴 最高威胁：CIRCUS\n\n**CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**\n- 作者：Swapnil Parekh\n- 时间：2026年3月, arXiv 2603.00523\n- 方法：对单一归因方法，在多组剪枝阈值配置下运行，计算每条边的 inclusion frequency → stability score s(e) ∈ [0,1]，提取 consensus circuit（所有配置下都存在的边），分为 core/contingent/noise\n- **与 CSS 的区别**：CIRCUS 变化的是**单方法内的超参数**（剪枝阈值），不是跨不同算法族。它不运行 ACDC + EAP + SP 然后求交集\n- **与 CSS 的相似度**：数学框架高度相似（per-edge stability scoring, consensus extraction, core/contingent taxonomy）\n- **威胁评级**：🔴 HIGH — 概念上最接近，但维度不同（intra-method vs cross-method）\n\n### 🟡 中等威胁：Mondorf et al. Ensemble\n\n**Mondorf et al. \"Exploring Ensemble Strategies for Circuit Localization Methods\" (BlackboxNLP 2025, arXiv 2510.06811)**\n- 方法：组合 EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning 的输出\n  - Max = union（任一方法选中）\n  - Min = intersection（所有方法选中）\n  - Mean = 连续分数平均\n  - Hybrid = 并行+串行组合\n- 结果：Mean > union/intersection，Hybrid 最佳 (CMD 0.03, CPR 1.83)\n- **与 CSS 的区别**：聚合的是**连续归因分数**（mean/min/max），不是二值 edge-in/edge-out；方法主要是 EAP 变体，不是真正不同的算法族；workshop 短文非完整方法贡献\n- **与 CSS 的相似度**：确实跨方法组合（attribution + pruning），实现了 union/intersection 操作\n- **威胁评级**：🟡 MODERATE — 最接近跨方法聚合，但 framing 为 shared task 工程方案非方法论贡献\n\n### 🟢 低威胁\n\n| 论文 | 方法 | 与 CSS 区别 | 威胁 |\n|------|------|------------|------|\n| Nikankin et al. \"Improving Circuit Faithfulness via Better Edge Selection\" (BlackboxNLP 2025) | Bootstrap EAP-IG scores across data resamples | 单方法 + 数据重采样，非跨方法 | 🟢 LOW |\n| Anani et al. \"Certified Circuits: Stability Guarantees\" (2026, arXiv 2602.22968) | 随机化数据子采样 + 删除平滑认证 | 单方法 wrapper，不聚合多方法 | 🟢 LOW |\n| Miller et al. \"Transformer Circuit Faithfulness Metrics are not Robust\" (CoLM 2024) | 分析 faithfulness 指标敏感性 | 纯诊断，不提出聚合 | 🟢 LOW |\n\n**总结：没有论文提出 CSS 的精确方案——运行 N 种根本不同的算法族（ACDC, EAP, SP, EP），对每种输出做二值化，然后计算跨方法 binary consensus。CIRCUS 最接近但维度不同（intra-method threshold variation vs cross-method）。Mondorf et al. 确实跨方法但用连续分数聚合且为 workshop 工程方案。**\n\n---\n\n## 3. 2024-2026 新方法\n\n| 方法 | 论文 | 年份 | 会议 | 算法族 | 备注 |\n|------|------|------|------|--------|------|\n| CD-T | Hsu et al. \"Efficient Automated Circuit Discovery using Contextual Decomposition\" | 2024 | ICLR 2025 | 分解 (decomposition) | 无需 activation patching，秒级发现，97% AUC |\n| DiscoGP | Yu et al. \"Functional Faithfulness in the Wild\" | 2024 | ICML 2024 | 可微剪枝 | 联合权重+边剪枝，端到端学习二值 mask |\n| Transcoders | Dunefsky et al. \"Transcoders Find Interpretable LLM Feature Circuits\" | 2024 | NeurIPS 2024 | 稀疏替换模型 | 用稀疏 MLP 替换原 MLP，实现 weights-based 电路分析 |\n| Sparse Feature Circuits | Marks et al. \"Discovering and Editing Interpretable Causal Graphs\" | 2024 | ICLR 2025 (Oral) | 归因 + SAE 特征 | 在 SAE 特征级别发现电路，支持 SHIFT 编辑 |\n| Circuit Tracing | Ameisen, Olah et al. (Anthropic) \"Attribution Graphs\" | 2025 | Tech Report | 稀疏替换 + 归因 | Cross-layer transcoders → per-prompt DAG，应用于 Claude 3.5 |\n| GIM | Edin et al. \"Improved Interpretability for LLMs\" | 2025 | arXiv | 梯度修正 | 修正 softmax/LayerNorm 反传，MIB 排行榜第一 |\n| HAP | Gu et al. \"Hybrid Attribution and Pruning Framework\" | 2025 | arXiv | 混合 (EAP → EP) | 先 EAP 粗筛再 EP 精修，比 EP 快 46% |\n| ModCirc | He et al. \"Modular Circuits of LLMs\" | 2025 | ICML 2025 | 模块化分解 | 发现跨任务共享的模块化电路词表 |\n| Stream | Rosser et al. \"Scaling up MI to Long Context\" | 2025 | arXiv | 层次化剪枝 | O(T log T) 稀疏注意力 mask，支持 100K+ token |\n| Weight-Sparse Circuits | Gao et al. (OpenAI) | 2025 | arXiv | 稀疏训练 | 极端权重稀疏 (~1/1000) → 天然可解释电路 |\n| Formal MI | Hadad et al. \"Automated Circuit Discovery with Provable Guarantees\" | 2026 | ICLR 2026 | 验证 (verification) | 首个可证明保证的电路发现（鲁棒性 + 最小性） |\n| SVD Directional Masking | Ahmad et al. \"Beyond Components\" | 2025 | arXiv | SVD + 可微 mask | 揭示单头内叠加子功能 |\n\n---\n\n## 4. 顶会论文列表\n\n### ICLR 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Autoencoders Find Highly Interpretable Features in LMs | SAE 发现单语义特征，解决 superposition |\n| Towards Best Practices of Activation Patching in LMs | 系统分析 patching 方法选择对电路发现的影响 |\n| Circuit Component Reuse Across Tasks | IOI 电路 ~78% 被 Colored Objects 复用 |\n| Successor Heads: Recurring Interpretable Attention Heads | 发现跨架构的 successor heads（递增操作） |\n\n### ICLR 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Feature Circuits (Oral) | SAE 特征级电路发现 + SHIFT 编辑 |\n| Scaling and Evaluating Sparse Autoencoders (Oral) | k-sparse SAE 扩展到 GPT-4，16M latents |\n| CD-T: Contextual Decomposition for Circuit Discovery | 秒级电路发现，97% AUC |\n| Computational Complexity of Circuit Discovery (Spotlight) | 证明多数电路发现查询 NP-hard |\n| Everything Everywhere All at Once: Is MI Identifiable? | 电路非唯一性：多电路可复现同一行为 |\n| SAEs Do Not Find Canonical Units of Analysis | SAE stitching 证明特征非原子/非完备 |\n| Unifying and Verifying Mechanistic Interpretations | 统一群运算网络的机制解释并形式化证明 |\n\n### NeurIPS 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Finding Transformer Circuits with Edge Pruning (Spotlight) | EP 方法，更忠实且更稀疏，扩展到 13B |\n| Transcoders Find Interpretable LLM Feature Circuits | 稀疏 MLP 替换实现 weights-based 电路分析 |\n| LLM Circuit Analyses Are Consistent Across Training and Scale | 电路在训练过程和模型规模间一致出现 |\n| Compact Proofs of Model Performance via MI | MI → 可证明的准确率下界 |\n| Hypothesis Testing the Circuit Hypothesis | 形式化电路假设的假设检验 |\n| InterpBench: Semi-Synthetic Transformers for Evaluating MI | 86 个有 ground-truth 的半合成模型评估基准 |\n\n### ICML 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| MIB: A Mechanistic Interpretability Benchmark | 标准化电路定位基准，归因+mask 优化方法领先 |\n| ModCirc: Modular Circuits of LLMs | 跨任务模块化电路词表 |\n| Towards Understanding Fine-Tuning via Circuit Analysis | 追踪微调中电路变化，提出 circuit-aware LoRA |\n\n---\n\n## 5. Novelty 评估\n\n### CSS 的 novelty 站得住吗？**站得住，但需要精确定位差异化。**\n\n#### ✅ Novelty 成立的理由\n\n1. **无人做跨算法族的 binary consensus**：所有现有工作要么是单方法内变异分析（CIRCUS, Méloux），要么是连续分数聚合（Mondorf），要么只是各方法 vs ground-truth 的性能比较。CSS 提出跨 N 种根本不同的算法族做二值共识，这个精确配方是新的。\n\n2. **方法间差异的系统分析是空白**：没有论文报告过不同方法的 pairwise Jaccard matrix / agreement heatmap。大量论文隐含表明方法差异很大（EP 边数不到 ACDC 一半），但无人将此作为研究问题。\n\n3. **core/contingent 分类的跨方法版本未被探索**：CIRCUS 做了类似的 core/contingent/noise taxonomy，但基于 intra-method threshold variation。CSS 基于 cross-method agreement 做分类，维度不同且信息更丰富。\n\n#### ⚠️ 需要小心的 Novelty 威胁\n\n1. **CIRCUS (2603.00523)** 是最大威胁。虽然维度不同，但 reviewer 可能认为 conceptual overlap 太大。**建议**：论文中必须明确讨论 CIRCUS，强调区别（intra-method hyperparameter variation vs cross-method algorithmic diversity），并论证为何跨方法维度更有意义（不同方法有不同 inductive bias，而阈值变化只探索同一方法的 Rashomon set）。\n\n2. **Mondorf et al.** 已经实现了 union/intersection 操作并发现 mean 优于两者。CSS 需要论证 binary consensus 相比连续分数平均的优势（如可解释性、对阈值选择的鲁棒性）。\n\n3. **Méloux et al. 的 intra-method instability 问题**：如果单方法内 Jaccard 仅 0.56，跨方法 consensus 可能更低。需要实验证明 CSS-core 的 faithfulness 确实优于单方法，否则 consensus 可能只是噪声的交集。\n\n4. **非唯一性问题 (ICLR 2025 \"Everything Everywhere All at Once\")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。\n\n#### 🎯 差异化建议\n\n- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。\n- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。\n- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n",
    "structuredPatch": [
      {
        "oldStart": 159,
        "oldLines": 3,
        "newStart": 159,
        "newLines": 114,
        "lines": [
          " - **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。",
          " - **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。",
          " - **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。",
          "+",
          "+---",
          "+",
          "+## 1b. CIRCUS 深度分析",
          "+",
          "+> 论文：CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles (arXiv 2603.00523, 2026.02.28)",
          "+> 作者：Swapnil Parekh",
          "+> 代码：未公开（GitHub: SwapnilDreams100，未找到 CIRCUS 仓库）",
          "+",
          "+### 方法细节",
          "+",
          "+**Stability 测量机制：变化剪枝阈值，不变种子/数据。**",
          "+",
          "+CIRCUS 对**单一 attribution graph**（由 cross-layer transcoders 生成的归因图）施加 B 组不同的剪枝配置 {π₁, ..., πB}，每组配置指定不同的 node threshold 和 edge threshold（cumulative-influence cutoffs）。**不涉及**随机种子变化或数据子集变化。",
          "+",
          "+**Config-bagging 参数：**",
          "+- B=25（5×5 grid）用于 stability 分析",
          "+- B=9（non-nested configurations）用于主实验评估",
          "+- B=3 用于嵌套配置消融实验",
          "+- **关键设计约束——non-nesting**：配置必须在不同维度上交叉变化（如 (0.6, 0.99) 保留少 node 多 edge，(0.9, 0.95) 相反），避免 E(1)⊆E(2)⊆...⊆E(B) 导致 consensus 退化为最严格单配置",
          "+",
          "+**Consensus 公式：**",
          "+",
          "+stability score（per-edge inclusion frequency）：",
          "+```",
          "+s(e) = (1/B) × Σ_{b=1}^{B} 𝟙[e ∈ E(b)]",
          "+```",
          "+",
          "+consensus circuit 提取：",
          "+```",
          "+C_τ = {e : s(e) ≥ τ}",
          "+```",
          "+",
          "+主实验使用 **strict consensus τ=1**（边必须在所有配置中存在）。τ<1 可用于探索性分析。",
          "+",
          "+**Core/Contingent/Noise 分类：**",
          "+| 类别 | 定义 | 含义 |",
          "+|------|------|------|",
          "+| Core | s(e) = 1 | 所有配置都保留，鲁棒结构 |",
          "+| Contingent | 0.5 ≤ s(e) < 1 | 多数配置保留，替代路径 |",
          "+| Noise | s(e) < 0.5 | 少数配置保留，阈值敏感伪影 |",
          "+",
          "+类比 Bayesian variable selection 中的 posterior model-inclusion indicators。",
          "+",
          "+### 实验设置",
          "+",
          "+**模型：**",
          "+- Gemma-2-2B",
          "+- Llama-3.2-1B",
          "+",
          "+**任务：**",
          "+- Short factoid completions：capitals, arithmetic, trivia",
          "+- 数据规模：50 prompts (Gemma), 20 prompts (Llama)",
          "+- 论文明确承认局限：\"generalization to more complex behaviors (reasoning, in-context learning) remains open\"",
          "+",
          "+**使用的 circuit discovery 方法：仅一种。**",
          "+- 底层方法：cross-layer transcoders (CLTs) 生成的 attribution graphs（引用 Ameisen et al. 2025, Hanna et al. 2025）",
          "+- 节点 = learned features（CLT 特征），边 = features 间的直接因果效应，权重 W ∈ ℝ^{|E|}",
          "+- **不使用** EAP, ACDC, Edge Pruning 或其他传统 circuit discovery 方法",
          "+- **不跨方法比较**",
          "+",
          "+### Faithfulness 评估",
          "+",
          "+**Metrics：**",
          "+",
          "+1. **Influence Retained (IR)**：IR(S) = Φ(S)/Φ(E)，其中 Φ(S) = Σ|w_e| 为子图绝对边权之和。衡量通过子图 S 的总归因影响比例。",
          "+",
          "+2. **KL Divergence（per-logit）**：D_KL(p_E || p_S)，consensus 达到 0.0010±0.0008 vs union-pruned 0.40±1.74（20 prompts, 17/20 wins）。",
          "+",
          "+3. **Activation Patching（因果验证）**：",
          "+   - Patch C₁ 节点激活从 source prompt → target prompt",
          "+   - Recovery: consensus 19.4 vs random 6.8 vs matched controls 1.6",
          "+   - p=0.0004 (Wilcoxon signed-rank)",
          "+   - Consensus = oracle 的 57%，random = 20%",
          "+",
          "+4. **Win-rate**：",
          "+   - vs union-pruned: 47/50 (Gemma), 19/20 (Llama) with B=9",
          "+   - vs random: 37/50 (Gemma), 20/20 (Llama)",
          "+",
          "+**关键结论：** strict consensus circuit ~40× smaller than union，但保持 comparable influence-flow 解释力。overhead 仅 5.5%（<1ms consensus 构建）。",
          "+",
          "+### 跨方法比较",
          "+",
          "+**CIRCUS 没有做跨方法比较。** 这是确认的事实：",
          "+- 仅使用 CLT attribution graphs 一种 pipeline",
          "+- 变化的是该 pipeline 内的剪枝阈值配置",
          "+- 不涉及 EAP, ACDC, Edge Pruning, SP 等任何其他 circuit discovery 算法",
          "+- **这是 CSS 的核心差异点**",
          "+",
          "+### CSS vs CIRCUS 精确差异表",
          "+",
          "+| 维度 | CIRCUS | CSS (ours) |",
          "+|------|--------|-----------|",
          "+| **变化什么** | 单方法内的剪枝阈值 (node/edge cutoffs) | 算法族 (gradient/mask/causal 等不同范式) |",
          "+| **底层方法数** | 1 种 (CLT attribution graphs) | K=3+ 种根本不同的算法 (如 EAP, ACDC, EP) |",
          "+| **稳定性来源** | Intra-method: 阈值鲁棒性 (Rashomon set) | Cross-method: 算法族间一致性 (不同 inductive bias) |",
          "+| **聚合方式** | 连续 stability score s(e)∈[0,1] + strict consensus τ=1 | 二值投票 (K 方法中 ≥ threshold 方法包含 edge) |",
          "+| **输入** | 单次 attribution run 的一张归因图 | 每种方法独立运行产出的 K 张电路图 |",
          "+| **计算开销** | 极低 (5.5% overhead, 不需重新计算归因) | 需要运行 K 种不同算法 (各自完整 pipeline) |",
          "+| **模型规模** | Gemma-2-2B, Llama-3.2-1B | 待定 |",
          "+| **任务类型** | Short factoid completions | 待定 |",
          "+| **core claim** | 阈值变化下的鲁棒核心 vs 阈值敏感伪影 | 跨算法族共识比单方法更鲁棒、更可信 |",
          "+| **方法间差异分析** | ❌ 不分析 | ✅ Pairwise Jaccard matrix / agreement heatmap |",
          "+| **taxonomy 基础** | 同方法不同参数的 inclusion frequency | 不同方法的 agreement count |",
          "+",
          "+### 关键论点：为何 cross-method > intra-method",
          "+",
          "+1. **不同 inductive bias**：EAP 基于梯度归因，ACDC 基于 activation patching（因果干预），EP 基于可微剪枝。它们从根本不同的角度逼近\"重要边\"。阈值变化只探索同一视角的灵敏度。",
          "+2. **信息正交性**：跨方法共识的边同时被梯度信号、因果干预和优化剪枝确认，信息量远大于同方法不同阈值。",
          "+3. **实用价值**：如果研究者只有一种方法，CIRCUS 有用；如果研究者想知道\"哪些结构是方法无关的\"，CSS 回答的是不同的问题。",
          "+4. **Méloux et al. 的启示**：单方法内 Jaccard 仅 0.561，说明 intra-method 变异已经很大。跨方法共识可能提供更稳定的 core（或发现更大的分歧——这本身也是重要发现）。"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 43_

注册更新后的 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "10eb72a6-f8cd-4965-ab88-0150d1dbeecb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDrM7jWSZuw1Sw1u4u5eKa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2621,
      "cache_read_input_tokens": 40827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2621
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

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_019CLgUqXRA6dSQ3X2gGYjK1`</summary>

```json
{
  "name": "related_work_notes_v2",
  "type": "report",
  "description": "Related work notes with CIRCUS deep analysis (Section 1b) - detailed method comparison, stability scoring mechanism, cross-method gap confirmation",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "tags": [
    "literature",
    "CIRCUS",
    "novelty",
    "related-work"
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
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "a14b60d0-faca-4b3a-9f6c-34831abf3537",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDrM7jWSZuw1Sw1u4u5eKa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2621,
      "cache_read_input_tokens": 40827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2621
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

### Tool result

_source line 45 · 2026-05-12T22:21:54.604Z_

<details><summary>↩ Tool result · `toolu_019CLgUqXRA6dSQ3X2gGYjK1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_114feb\", \"name\": \"related_work_notes_v2\", \"type\": \"report\", \"description\": \"Related work notes with CIRCUS deep analysis (Section 1b) - detailed method comparison, stability scoring mechanism, cross-method gap confirmation\", \"path\": \"projects/structfuse-context/artifacts/_project/report/related_work_notes_114feb.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:21:54.490118+00:00\", \"tags\": [\"literature\", \"CIRCUS\", \"novelty\", \"related-work\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "81e86133-c5f9-40d6-995b-0a4f032f6d90",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260512_114feb\\\", \\\"name\\\": \\\"related_work_notes_v2\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Related work notes with CIRCUS deep analysis (Section 1b) - detailed method comparison, stability scoring mechanism, cross-method gap confirmation\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/report/related_work_notes_114feb.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-12T22:21:54.490118+00:00\\\", \\\"tags\\\": [\\\"literature\\\", \\\"CIRCUS\\\", \\\"novelty\\\", \\\"related-work\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_114feb\", \"name\": \"related_work_notes_v2\", \"type\": \"report\", \"description\": \"Related work notes with CIRCUS deep analysis (Section 1b) - detailed method comparison, stability scoring mechanism, cross-method gap confirmation\", \"path\": \"projects/structfuse-context/artifacts/_project/report/related_work_notes_114feb.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:21:54.490118+00:00\", \"tags\": [\"literature\", \"CIRCUS\", \"novelty\", \"related-work\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

## Q5 结论（最关键）：CIRCUS **没有**做跨方法比较

CIRCUS 只使用一种底层方法（CLT attribution graphs），变化的是剪枝阈值配置，不涉及 EAP/ACDC/EP 等不同 circuit discovery 算法。这确认了 CSS 的核心差异点。

## CSS vs CIRCUS 精确差异

| 维度 | CIRCUS | CSS (ours) |
|------|--------|-----------|
| 变化什么 | 单方法内剪枝阈值 | 不同算法族 (gradient/mask/causal) |
| 方法数 | 1 种 (CLT attribution) | K=3+ 种根本不同算法 |
| 稳定性来源 | Intra-method 阈值鲁棒性 | Cross-method 算法间一致性 |
| 聚合方式 | 连续 s(e)∈[0,1] + strict τ=1 | 二值投票 ≥ threshold |
| 计算开销 | 极低 (5.5%) | 需运行 K 种完整 pipeline |
| 跨方法分析 | 不做 | Pairwise Jaccard / agreement matrix |

**核心论点**：CIRCUS 回答"这条边对阈值选择鲁棒吗？"，CSS 回答"这条边是算法无关的吗？"。不同算法有不同 inductive bias（梯度 vs 因果干预 vs 可微剪枝），跨方法共识的信息正交性远高于阈值变化。

## 其他要点

- **模型/任务**：Gemma-2-2B + Llama-3.2-1B，仅 short factoid completions（capitals, arithmetic, trivia），50/20 prompts
- **Consensus 公式**：s(e) = (1/B)Σ𝟙[e∈E(b)]，B=9 主实验，strict consensus τ=1
- **Faithfulness**：IR + KL divergence + activation patching (p=0.0004)，consensus ~40× smaller than union 但保持解释力
- **GitHub 仓库**：未公开

已追加到 `artifacts/related_work_notes.md` Section 1b。

Sources:
- [CIRCUS paper (arXiv)](https://arxiv.org/abs/2603.00523)
- [CIRCUS HTML full text](https://arxiv.org/html/2603.00523)
- [Swapnil Parekh's page](https://swapnilparekh.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "uuid": "67d6f345-b6c6-435c-8938-cbcc1d8606cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNZrufxZhQWQNJZEuJiYG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 43448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 627
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

_source line 47_

## Q5 结论（最关键）：CIRCUS **没有**做跨方法比较

CIRCUS 只使用一种底层方法（CLT attribution graphs），变化的是剪枝阈值配置，不涉及 EAP/ACDC/EP 等不同 circuit discovery 算法。这确认了 CSS 的核心差异点。

## CSS vs CIRCUS 精确差异

| 维度 | CIRCUS | CSS (ours) |
|------|--------|-----------|
| 变化什么 | 单方法内剪枝阈值 | 不同算法族 (gradient/mask/causal) |
| 方法数 | 1 种 (CLT attribution) | K=3+ 种根本不同算法 |
| 稳定性来源 | Intra-method 阈值鲁棒性 | Cross-method 算法间一致性 |
| 聚合方式 | 连续 s(e)∈[0,1] + strict τ=1 | 二值投票 ≥ threshold |
| 计算开销 | 极低 (5.5%) | 需运行 K 种完整 pipeline |
| 跨方法分析 | 不做 | Pairwise Jaccard / agreement matrix |

**核心论点**：CIRCUS 回答"这条边对阈值选择鲁棒吗？"，CSS 回答"这条边是算法无关的吗？"。不同算法有不同 inductive bias（梯度 vs 因果干预 vs 可微剪枝），跨方法共识的信息正交性远高于阈值变化。

## 其他要点

- **模型/任务**：Gemma-2-2B + Llama-3.2-1B，仅 short factoid completions（capitals, arithmetic, trivia），50/20 prompts
- **Consensus 公式**：s(e) = (1/B)Σ𝟙[e∈E(b)]，B=9 主实验，strict consensus τ=1
- **Faithfulness**：IR + KL divergence + activation patching (p=0.0004)，consensus ~40× smaller than union 但保持解释力
- **GitHub 仓库**：未公开

已追加到 `artifacts/related_work_notes.md` Section 1b。

Sources:
- [CIRCUS paper (arXiv)](https://arxiv.org/abs/2603.00523)
- [CIRCUS HTML full text](https://arxiv.org/html/2603.00523)
- [Swapnil Parekh's page](https://swapnilparekh.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 203478,
  "duration_api_ms": 240887,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "a8be2c55-52ff-463d-876f-8fe34afc24fa",
  "total_cost_usd": 0.6952200000000001,
  "usage": {
    "input_tokens": 5182,
    "cache_creation_input_tokens": 32234,
    "cache_read_input_tokens": 284375,
    "output_tokens": 5782,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32234,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 722,
        "cache_read_input_tokens": 43448,
        "cache_creation_input_tokens": 627,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 627
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 97375,
      "outputTokens": 4747,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 6,
      "costUSD": 0.18111,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5182,
      "outputTokens": 5782,
      "cacheReadInputTokens": 284375,
      "cacheCreationInputTokens": 32234,
      "webSearchRequests": 0,
      "costUSD": 0.5141100000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b81b141c-6e46-494b-bb3c-077067499bfc"
}
```

</details>

---

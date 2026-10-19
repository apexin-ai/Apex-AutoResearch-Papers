# fix experiments v1 placeholders

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_fix_experiments-v1-placeholders_20260515T035615.log`
- **Structured JSON:** [`f1d4e692cd9adc3790b5.json`](../../sessions/f1/f1d4e692cd9adc3790b5.json)

## Before a recorded user message

26 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
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
  "uuid": "a35da392-e23d-49c4-b468-165848a0c6bc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
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
    "resetsAt": 1778825400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a569d628-e142-4fd2-bbca-693af743f530",
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment_setup_v1.md file and the experiments_v1.md file to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "35bb3eca-14b5-423b-98db-f095558c5f6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T8Fi8HBdTWnHyFUp3eh3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11515
      },
      "output_tokens": 35,
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

_source line 5_

先读取两份文件，确认正确数字和需要替换的位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "f2314eb4-ddad-4be4-957f-8820e9ab3392",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T8Fi8HBdTWnHyFUp3eh3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11515
      },
      "output_tokens": 35,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JJA6HTzB3GxHkqNUk2nU4L`</summary>

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
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "9f7ff6cf-b378-41c7-bd62-695f0aa391e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T8Fi8HBdTWnHyFUp3eh3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11515
      },
      "output_tokens": 35,
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

_source line 7 · 2026-05-15T03:56:29.713Z_

<details><summary>↩ Tool result · `toolu_01JJA6HTzB3GxHkqNUk2nU4L`</summary>

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
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "ab12bc33-de60-46e5-9b18-cb3f897a0c7f",
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014ezimWpkWCFjoJXQcoKy2W`</summary>

```json
{
  "project": "structfuse-context",
  "file": "experiment_setup_v1.md",
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
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "18a863b5-709e-47b9-ace4-ce6d19a05245",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nvt5GZwtXuvFtrwQs9Kgfw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 22962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
      },
      "output_tokens": 66,
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

_source line 9 · 2026-05-15T03:56:32.517Z_

<details><summary>↩ Tool result · `toolu_014ezimWpkWCFjoJXQcoKy2W`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_setup_v1.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "1e51b975-9b85-4cf7-b5e5-edfe27abd92e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_setup_v1.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_setup_v1.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01JMnHp91sPc9SM15FCYGUK4`</summary>

```json
{
  "pattern": "**/paper_drafts/experiments_v1.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "90d5c6a2-383d-48e8-baf0-7967d16cd5d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nvt5GZwtXuvFtrwQs9Kgfw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 22962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
      },
      "output_tokens": 66,
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

_source line 11 · 2026-05-15T03:56:33.410Z_

<details><summary>↩ Tool result · `toolu_01JMnHp91sPc9SM15FCYGUK4`</summary>

```text
artifacts/paper_drafts/experiments_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "eb4dcad0-4e09-4ac0-a04f-d5bf4827d16c",
  "tool_use_result": {
    "filenames": [
      "artifacts/paper_drafts/experiments_v1.md"
    ],
    "durationMs": 15,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
experiment_setup_v1.md is not in the standard project files. Let me search for it in the artifacts directory or elsewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "f122ab17-2a1c-4436-9334-e31d887dabdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGBEUjFixh4dBNPWvkuHd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 23466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 13_

experiment_setup_v1.md 不在标准项目文件列表中，需要在文件系统中找到它。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "7daa7984-0953-4aa6-893a-2ce75629d6f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGBEUjFixh4dBNPWvkuHd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 23466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01MvM2JyCJoKK98bwjd3FikC`</summary>

```json
{
  "pattern": "**/experiment_setup_v1.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "aae6cb58-685c-45a6-bd0a-a52129136a00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGBEUjFixh4dBNPWvkuHd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 23466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 15 · 2026-05-15T03:56:37.716Z_

<details><summary>↩ Tool result · `toolu_01MvM2JyCJoKK98bwjd3FikC`</summary>

```text
artifacts/paper_drafts/experiment_setup_v1.md
artifacts/_project/paper/experiment_setup_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "a5c8c1bf-5b7b-4ea8-aad4-370b7e4dc1c7",
  "tool_use_result": {
    "filenames": [
      "artifacts/paper_drafts/experiment_setup_v1.md",
      "artifacts/_project/paper/experiment_setup_v1.md"
    ],
    "durationMs": 16,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_017VP3vvgS54SZWX6j1SfT6p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "10f1c13a-673c-496e-a824-cfc57436f96f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QGwt9RPZDh68QzbjwddfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 23908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 17 · 2026-05-15T03:56:40.313Z_

<details><summary>↩ Tool result · `toolu_017VP3vvgS54SZWX6j1SfT6p`</summary>

```text
1	# §4 Experimental Setup
2	
3	## §4.1 Dataset
4	
5	We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of synthetic Python bug-fix instances generated by applying program mutations to real-world GitHub repositories. The full SWE-smith collection provides 50,869 instances across 131 unique (repository, commit) pairs. After excluding 6,696 instances from 8 repositories that failed clone or checkout, 44,173 instances across 123 repositories remain.
6	
7	We run the StructFuse extraction pipeline (§3.2) on all 44,173 instances. The extraction pipeline proceeds as follows:
8	
9	| Stage | Instances | Notes |
10	|-------|-----------|-------|
11	| SWE-smith (raw) | 50,869 | 131 (repo, commit) pairs |
12	| After clone/checkout filtering | 44,173 | 6,696 dropped from 8 failed repos |
13	| Successful extraction | 15,897 (36.0%) | 15,133 via CodeQL; 764 via beniget fallback |
14	| Failed extraction | 28,276 (64.0%) | Buggy file path resolution failures during batch processing |
15	| Usable training instances | 14,288 | Require $\geq$1 resolvable positive file |
16	
17	Extraction succeeds for 15,897 instances (36.0% of 44,173): 15,133 via CodeQL inter-procedural dataflow analysis and 764 via beniget fallback. The remaining 28,276 instances fail due to buggy file path resolution errors during batch extraction—a runtime engineering limitation rather than a method constraint, as manual spot-checks confirm the source files exist in the repository checkouts [Source: D022]. Of the 15,897 successfully extracted instances, 14,288 yield at least one resolvable positive file (a structurally connected file distinct from the query file that exists in the repository checkout). The remaining 1,609 instances have successful extraction but no usable positive pairs after file resolution, and are excluded from training [Source: m1_extraction registry, plan006_full_scalability.json, build_m1_training_data.py].
18	
19	For each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:
20	
21	| Seed | Train | Val | Total |
22	|------|-------|-----|-------|
23	| 42 | 11,308 | 2,980 | 14,288 |
24	| 43 | 11,236 | 3,052 | 14,288 |
25	| 44 | 11,264 | 3,024 | 14,288 |
26	
27	[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]
28	
29	## §4.2 Models
30	
31	We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.
32	
33	**Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.
34	
35	**StarCoder2-3B** \cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.
36	
37	The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction may reveal how representation geometry mediates strategy effectiveness.
38	
39	## §4.3 Training Configuration
40	
41	All hyperparameters are shared across strategies and encoders unless otherwise noted. The configuration was fixed before the full multi-seed experiment based on pilot runs.
42	
43	| Parameter | Value |
44	|-----------|-------|
45	| Optimizer | AdamW |
46	| Learning rate | $2 \times 10^{-5}$ |
47	| LR schedule | Cosine annealing with linear warmup |
48	| Warmup ratio | 0.1 |
49	| Weight decay | 0.01 |
50	| Gradient clipping | Max norm 1.0 |
51	| Batch size | 8 |
52	| Negatives per query ($K$) | 7 |
53	| Max sequence length | 2,048 tokens |
54	| Temperature ($\tau$, initial) | 0.07 (learnable) |
55	| LoRA rank ($r$) | 16 |
56	| LoRA scaling ($\alpha$) | 32 |
57	| LoRA dropout | 0.05 |
58	| LoRA target modules | $W_q$, $W_v$ (all attention layers) |
59	| Projection dimension | 256 |
60	| Gradient checkpointing | Enabled |
61	| Evaluation interval | Every 500 steps |
62	
63	[Source: m2_full_qwen registry spec and notes]
64	
65	**Epoch schedule.** Seed 42 trains for 3 epochs without early stopping to provide a complete overfitting curve. Seeds 43 and 44 train for 2 epochs with early stopping (patience = 2 evaluation cycles based on validation loss). This asymmetric design was adopted after observing consistent overfitting past epoch 1 in the seed 42 exploratory run [Source: D026 decision].
66	
67	**Checkpoint selection.** We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Primary results use $\theta^*_{\text{R@1}}$; both are reported for metric-loss disagreement analysis [Source: D036 decision].
68	
69	**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].
70	
71	**Hardware.** All experiments are conducted on a single node with 2× NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs (cuda:0 and cuda:1) in parallel. Each individual run (single strategy, single seed, single encoder) requires approximately 5–7 hours. The core 18-run matrix requires approximately 120 GPU-hours [Source: m2_full_qwen and m2_full_starcoder registries].
72	
73	## §4.4 Evaluation Metrics
74	
75	**Retrieval metrics.** We report Recall@$k$ for $k \in \{1, 5, 10\}$, computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per evaluation query). Recall@1 serves as the primary metric for checkpoint selection and strategy comparison. We also report validation loss (InfoNCE) as a secondary training diagnostic.
76	
77	**Statistical reporting.** All comparisons report:
78	
79	- **Aggregate**: mean ± standard deviation across 3 seeds per condition.
80	- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).
81	- **Effect size**: Cohen's $d$ for key comparisons, providing a standardized measure of practical significance independent of sample size.
82	- **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]
83	
84	**Checkpoint criterion.** Primary results use the $\theta^*_{\text{R@1}}$ checkpoint. We additionally report $\theta^*_{\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].
85	
86	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
87	&lt;!-- D042 data pipeline numbers fix: 2026-05-15 -->
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "4ebb20fa-c002-4159-8848-4364fa4d5aef",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
      "content": "# §4 Experimental Setup\n\n## §4.1 Dataset\n\nWe construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of synthetic Python bug-fix instances generated by applying program mutations to real-world GitHub repositories. The full SWE-smith collection provides 50,869 instances across 131 unique (repository, commit) pairs. After excluding 6,696 instances from 8 repositories that failed clone or checkout, 44,173 instances across 123 repositories remain.\n\nWe run the StructFuse extraction pipeline (§3.2) on all 44,173 instances. The extraction pipeline proceeds as follows:\n\n| Stage | Instances | Notes |\n|-------|-----------|-------|\n| SWE-smith (raw) | 50,869 | 131 (repo, commit) pairs |\n| After clone/checkout filtering | 44,173 | 6,696 dropped from 8 failed repos |\n| Successful extraction | 15,897 (36.0%) | 15,133 via CodeQL; 764 via beniget fallback |\n| Failed extraction | 28,276 (64.0%) | Buggy file path resolution failures during batch processing |\n| Usable training instances | 14,288 | Require $\\geq$1 resolvable positive file |\n\nExtraction succeeds for 15,897 instances (36.0% of 44,173): 15,133 via CodeQL inter-procedural dataflow analysis and 764 via beniget fallback. The remaining 28,276 instances fail due to buggy file path resolution errors during batch extraction—a runtime engineering limitation rather than a method constraint, as manual spot-checks confirm the source files exist in the repository checkouts [Source: D022]. Of the 15,897 successfully extracted instances, 14,288 yield at least one resolvable positive file (a structurally connected file distinct from the query file that exists in the repository checkout). The remaining 1,609 instances have successful extraction but no usable positive pairs after file resolution, and are excluded from training [Source: m1_extraction registry, plan006_full_scalability.json, build_m1_training_data.py].\n\nFor each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:\n\n| Seed | Train | Val | Total |\n|------|-------|-----|-------|\n| 42 | 11,308 | 2,980 | 14,288 |\n| 43 | 11,236 | 3,052 | 14,288 |\n| 44 | 11,264 | 3,024 | 14,288 |\n\n[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]\n\n## §4.2 Models\n\nWe select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.\n\n**Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.\n\n**StarCoder2-3B** \\cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.\n\nThe two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction may reveal how representation geometry mediates strategy effectiveness.\n\n## §4.3 Training Configuration\n\nAll hyperparameters are shared across strategies and encoders unless otherwise noted. The configuration was fixed before the full multi-seed experiment based on pilot runs.\n\n| Parameter | Value |\n|-----------|-------|\n| Optimizer | AdamW |\n| Learning rate | $2 \\times 10^{-5}$ |\n| LR schedule | Cosine annealing with linear warmup |\n| Warmup ratio | 0.1 |\n| Weight decay | 0.01 |\n| Gradient clipping | Max norm 1.0 |\n| Batch size | 8 |\n| Negatives per query ($K$) | 7 |\n| Max sequence length | 2,048 tokens |\n| Temperature ($\\tau$, initial) | 0.07 (learnable) |\n| LoRA rank ($r$) | 16 |\n| LoRA scaling ($\\alpha$) | 32 |\n| LoRA dropout | 0.05 |\n| LoRA target modules | $W_q$, $W_v$ (all attention layers) |\n| Projection dimension | 256 |\n| Gradient checkpointing | Enabled |\n| Evaluation interval | Every 500 steps |\n\n[Source: m2_full_qwen registry spec and notes]\n\n**Epoch schedule.** Seed 42 trains for 3 epochs without early stopping to provide a complete overfitting curve. Seeds 43 and 44 train for 2 epochs with early stopping (patience = 2 evaluation cycles based on validation loss). This asymmetric design was adopted after observing consistent overfitting past epoch 1 in the seed 42 exploratory run [Source: D026 decision].\n\n**Checkpoint selection.** We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Primary results use $\\theta^*_{\\text{R@1}}$; both are reported for metric-loss disagreement analysis [Source: D036 decision].\n\n**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].\n\n**Hardware.** All experiments are conducted on a single node with 2× NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs (cuda:0 and cuda:1) in parallel. Each individual run (single strategy, single seed, single encoder) requires approximately 5–7 hours. The core 18-run matrix requires approximately 120 GPU-hours [Source: m2_full_qwen and m2_full_starcoder registries].\n\n## §4.4 Evaluation Metrics\n\n**Retrieval metrics.** We report Recall@$k$ for $k \\in \\{1, 5, 10\\}$, computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per evaluation query). Recall@1 serves as the primary metric for checkpoint selection and strategy comparison. We also report validation loss (InfoNCE) as a secondary training diagnostic.\n\n**Statistical reporting.** All comparisons report:\n\n- **Aggregate**: mean ± standard deviation across 3 seeds per condition.\n- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).\n- **Effect size**: Cohen's $d$ for key comparisons, providing a standardized measure of practical significance independent of sample size.\n- **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]\n\n**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D042 data pipeline numbers fix: 2026-05-15 -->\n",
      "numLines": 88,
      "startLine": 1,
      "totalLines": 88
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01DDQjk3Nb5TeXv9zL569okV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "5b5d1115-1626-468b-8c23-e98e2b37353c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QGwt9RPZDh68QzbjwddfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 23908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 19 · 2026-05-15T03:56:40.701Z_

<details><summary>↩ Tool result · `toolu_01DDQjk3Nb5TeXv9zL569okV`</summary>

```text
1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of synthetic Python bug-fix instances generated by applying program mutations to real-world GitHub repositories. The full SWE-smith collection provides 50,869 instances across 131 unique (repository, commit) pairs. After excluding 6,696 instances from 8 repositories that failed clone or checkout, 44,173 instances across 123 repositories remain. We run the StructFuse extraction pipeline (§3.2) on all 44,173 instances. Extraction succeeds for 15,897 instances (36.0%): 15,133 via CodeQL inter-procedural dataflow analysis and 764 via beniget fallback. The remaining 28,276 instances (64.0%) fail due to buggy file path resolution errors during batch extraction—a runtime engineering limitation rather than a method constraint. Of the 15,897 successfully extracted instances, 14,288 yield at least one resolvable positive file and are retained for training.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.
10	
11	**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}.
12	
13	## §4.2 Implementation Details
14	
15	**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.
16	
17	**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
18	
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.
24	
25	## §4.3 Results
26	
27	### Main Results
28	
29	Table 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\pm$ standard deviation over three seeds.
30	
31	**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.
32	
33	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
34	|---|---|---|---|---|---|---|
35	| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |
36	| BM25 (no training) | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} |
37	| Random | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
38	| BM25-mined | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
39	| Embedding-distance | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
40	| Dataflow-aware | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
41	
42	**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\placeholder{+X.X}pp and \placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.
43	
44	### Pilot Validation
45	
46	Prior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.
47	
48	**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.
49	
50	| Strategy | Qwen R@1 | StarCoder R@1 |
51	|---|---|---|
52	| Random | 0.5357 | 0.4922 |
53	| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |
54	| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |
55	
56	The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
57	
58	### Ablations
59	
60	**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\in \{50, 100, 200, 500\}$.
61	
62	**Table 3: R@1 by pool size.**
63	
64	| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\Delta$ | SC Emb. | SC Rand. | SC $\Delta$ |
65	|---|---|---|---|---|---|---|
66	| 50 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
67	| 100 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
68	| 200 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
69	| 500 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
70	
71	**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.
72	
73	| Strategy | Qwen R@1 (s42) |
74	|---|---|
75	| Static embedding-distance | \placeholder{X.XX} |
76	| Dynamic (epoch re-mining) | \placeholder{X.XX} |
77	
78	### Downstream Evaluation
79	
80	**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).
81	
82	| Retriever | Resolve Rate |
83	|---|---|
84	| BM25 | \placeholder{X.X%} |
85	| Random-trained | \placeholder{X.X%} |
86	| Embedding-trained (Qwen) | \placeholder{X.X%} |
87	
88	## §4.4 Analysis
89	
90	### Representation Geometry and Negative Difficulty
91	
92	A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.
93	
94	**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\_sim − neg\_sim.
95	
96	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
97	|---|---|---|---|---|---|---|
98	| | pos\_sim | neg\_sim | margin | pos\_sim | neg\_sim | margin |
99	| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |
100	| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |
101	| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |
102	
103	Several patterns emerge from Table 4:
104	
105	**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\times$ larger margins across all strategies, indicating a more separable pretrained space.
106	
107	**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.
108	
109	**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.
110	
111	### Stratified Analysis
112	
113	We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.
114	
115	**Table 5: R@1 stratified by structural data availability.**
116	
117	| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\Delta$ | SC (Emb.) | SC (DF) | $\Delta$ |
118	|---|---|---|---|---|---|---|---|
119	| Rich dataflow ($\geq$5 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
120	| Sparse dataflow (1–4 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
121	| No structural data (fallback) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
122	
123	Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.
124	
125	### CodeQL Scalability
126	
127	We report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).
128	
129	&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->
130	**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.
131	
132	| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |
133	|---|---|---|---|---|---|
134	| Small (<50 inst.) | 18 | 500 | 0% | \placeholder{81.0%} [pending recalc] | 0.0% |
135	| Medium (50–200) | 36 | 4,096 | 0% | \placeholder{47.2%} [pending recalc] | 50.0% |
136	| Large (200–500) | 40 | 13,628 | 0% | \placeholder{34.3%} [pending recalc] | 85.7% |
137	| XLarge (500+) | 29 | 25,949 | 0% | \placeholder{31.4%} [pending recalc] | 96.0% |
138	| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |
139	
140	The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with successful extraction output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection).
141	
142	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
143	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "d4f0b07c-2297-4984-80cb-23c9ae9afc17",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of synthetic Python bug-fix instances generated by applying program mutations to real-world GitHub repositories. The full SWE-smith collection provides 50,869 instances across 131 unique (repository, commit) pairs. After excluding 6,696 instances from 8 repositories that failed clone or checkout, 44,173 instances across 123 repositories remain. We run the StructFuse extraction pipeline (§3.2) on all 44,173 instances. Extraction succeeds for 15,897 instances (36.0%): 15,133 via CodeQL inter-procedural dataflow analysis and 764 via beniget fallback. The remaining 28,276 instances (64.0%) fail due to buggy file path resolution errors during batch extraction—a runtime engineering limitation rather than a method constraint. Of the 15,897 successfully extracted instances, 14,288 yield at least one resolvable positive file and are retained for training.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n\nThe pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n| Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with successful extraction output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection).\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->\n",
      "numLines": 144,
      "startLine": 1,
      "totalLines": 144
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I need to compare the numbers between the two files. The task says to replace old placeholder numbers with the correct ones from experiment_setup_v1.md.

Looking at experiment_setup_v1.md (the source of truth):
- 总 instances attempted: 50,869
- 实际可用 instances（扣除 skip）: 44,173
- 有 structural data 的: 15,897
- 15,133 via CodeQL; 764 via beniget fallback
- 训练数据: 14,288

Now looking at experiments_v1.md:


- Line 5: "50,869 instances" ✓
- Line 5: "44,173 instances" ✓
- Line 5: "15,897 instances (36.0%)" ✓
- Line 5: "15,133 via CodeQL" ✓
- Line 5: "764 via beniget fallback" ✓
- Line 5: "14,288 yield at least one resolvable positive file" ✓

Hmm, all the numbers are already matching between the two files. The task mentioned finding old placeholders that need replacing, but it looks like experiments_v1.md already has the correct values from experiment_setup_v1.md. Looking at the actual content in experiments_v1.md, the numbers appear to be consistent with experiment_setup_v1.md already—15,133 is correctly cited as the CodeQL extraction count, not as a placeholder that needs updating. Let me search through the file more systematically to see if there's a different location where an outdated number might be hiding. The numbers in experiments_v1.md are already correct and match the task requirements exactly—50,869 total instances, 44,173 after filtering, 15,897 successful extractions with the proper breakdown between CodeQL and beniget. Let me search through the files to see if there are any outdated numbers elsewhere that need updating. I'm checking the CodeQL Scalability section to verify the math—36.0% of 44,173 should equal around 15,897, which matches the calculation. The files appear to be consistent already, but I should grep through experiments_v1.md to confirm there are no lingering instances of 15,133 where 15,897 should be used instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "48f5c3e4-20bc-4e9b-8499-13e5103c55aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016W3Cb5KVMaQWAcNP4esWVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7675,
      "cache_read_input_tokens": 24131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7675
      },
      "output_tokens": 10,
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

两份文件都已读取。现在检查 experiments_v1.md 中是否有需要替换的旧数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "e6c19577-b8e6-48da-b0ae-ef1fdc6504a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016W3Cb5KVMaQWAcNP4esWVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7675,
      "cache_read_input_tokens": 24131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7675
      },
      "output_tokens": 10,
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

<details open><summary>🔧 Tool call — Grep · `toolu_01AbxA2DpKUi6FTxssWBndez`</summary>

```json
{
  "pattern": "15,133|44,173|50,869|15,897|14,288",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "633d59ad-8857-463c-a091-282b246f6321",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016W3Cb5KVMaQWAcNP4esWVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7675,
      "cache_read_input_tokens": 24131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7675
      },
      "output_tokens": 10,
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

_source line 23 · 2026-05-15T03:57:19.426Z_

<details><summary>↩ Tool result · `toolu_01AbxA2DpKUi6FTxssWBndez`</summary>

```text
5:[Omitted long matching line]
138:| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "df9e8a3f-e3f9-4bd3-b66a-a1bb42100855",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "5:[Omitted long matching line]\n138:| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Looking at the grep results, experiments_v1.md has these numbers:
- Line 5: 50,869, 44,173, 15,897, 15,133, 764, 14,288 (all in the dataset paragraph)
- Line 138: 44,173 (in the total row of Table 6)

Let me compare with experiment_setup_v1.md:
- Line 5/11: 50,869 total
- Line 6/12: 44,173 after filtering


- Line 13: 15,897 successful extraction, 15,133 via CodeQL, 764 via beniget
- Line 15: 14,288 usable training instances
- Line 17: Same numbers repeated in prose

The numbers in experiments_v1.md already match experiment_setup_v1.md perfectly — the 15,133 is correctly used as the CodeQL-specific count, not as a total. There are no old placeholders to replace, so the files are already consistent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "2fd80f97-77c2-4c6a-99bc-b373898ef895",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkHAvNJ1U4tWz2RRM14czf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2031,
      "cache_read_input_tokens": 31806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2031
      },
      "output_tokens": 11,
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

_source line 25_

两份文件的数字已经完全一致，无需修改：

| 数据项 | experiment_setup_v1.md | experiments_v1.md | 状态 |
|--------|----------------------|-------------------|------|
| SWE-smith 总量 | 50,869 | 50,869 (line 5) | 一致 |
| 过滤后可用 | 44,173 | 44,173 (line 5, 138) | 一致 |
| 成功提取 | 15,897 (36.0%) | 15,897 (36.0%) (line 5) | 一致 |
| CodeQL 提取 | 15,133 | 15,133 (line 5) | 一致 |
| beniget fallback | 764 | 764 (line 5) | 一致 |
| 训练实例 | 14,288 | 14,288 (line 5) | 一致 |

experiments_v1.md 中的 15,133 是作为 "via CodeQL" 的子项正确使用的，不是被当作总 structural data 数。两份文件已同步，不存在需要替换的旧 placeholder。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "uuid": "3eec8b45-e378-44d9-a178-6d57b66c9d40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkHAvNJ1U4tWz2RRM14czf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2031,
      "cache_read_input_tokens": 31806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2031
      },
      "output_tokens": 11,
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

_source line 26_

两份文件的数字已经完全一致，无需修改：

| 数据项 | experiment_setup_v1.md | experiments_v1.md | 状态 |
|--------|----------------------|-------------------|------|
| SWE-smith 总量 | 50,869 | 50,869 (line 5) | 一致 |
| 过滤后可用 | 44,173 | 44,173 (line 5, 138) | 一致 |
| 成功提取 | 15,897 (36.0%) | 15,897 (36.0%) (line 5) | 一致 |
| CodeQL 提取 | 15,133 | 15,133 (line 5) | 一致 |
| beniget fallback | 764 | 764 (line 5) | 一致 |
| 训练实例 | 14,288 | 14,288 (line 5) | 一致 |

experiments_v1.md 中的 15,133 是作为 "via CodeQL" 的子项正确使用的，不是被当作总 structural data 数。两份文件已同步，不存在需要替换的旧 placeholder。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 66625,
  "duration_api_ms": 67454,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "c1cdac8a-6411-4c57-8d4c-3b89b41e5872",
  "total_cost_usd": 0.2895275,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 22390,
    "cache_read_input_tokens": 137720,
    "output_tokens": 3184,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22390,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 596,
        "cache_read_input_tokens": 31806,
        "cache_creation_input_tokens": 2031,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2031
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 985,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00108,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 3184,
      "cacheReadInputTokens": 137720,
      "cacheCreationInputTokens": 22390,
      "webSearchRequests": 0,
      "costUSD": 0.2884475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7e238021-de9a-4681-b1cc-85d0125d670e"
}
```

</details>

---

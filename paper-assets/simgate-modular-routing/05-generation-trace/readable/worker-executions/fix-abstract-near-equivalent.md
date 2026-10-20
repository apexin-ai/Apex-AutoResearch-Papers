# fix abstract near equivalent

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_fix_abstract-near-equivalent_20260514T122922.log`
- **Structured JSON:** [`16dd5fde5910e469d03b.json`](../../sessions/16/16dd5fde5910e469d03b.json)

## Before a recorded user message

41 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "3e9a6147-f307-481e-8099-0069e8365e80",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 2_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778777400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4366cd84-9639-4926-8831-9a9c71e11e53",
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to sync the "near-equivalent" wording in the Abstract to match the experiments.tex which already uses "small but non-negligible". Let me start by finding the relevant text on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "839c8ecb-ec10-47cb-9174-7bc8db95977d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tssrRgDLYXxCQT5UQqoge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11825,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11825
      },
      "output_tokens": 33,
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

_source line 4_

先在服务器上查找所有包含 "near-equivalent" 的 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "943aeb66-9a78-4c7c-aa69-1f3a5d9e209f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tssrRgDLYXxCQT5UQqoge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11825,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11825
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T5TjRRHuyXcQ34xANrSpNN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "a4a2d615-b107-41cf-be8b-4e7a2aeb0543",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tssrRgDLYXxCQT5UQqoge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11825,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11825
      },
      "output_tokens": 33,
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

_source line 6 · 2026-05-14T12:48:52.471Z_

<details><summary>↩ Tool result · `toolu_01T5TjRRHuyXcQ34xANrSpNN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "770382f2-b1a2-46c2-b2a9-612135f12d97",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BCHg2yBb9UGfNryHFismrk`</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -rn \"near-equivalent\\|near equivalent\" /root/autodl-tmp/simgate-modular-routing/paper/*.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "4d677f33-edbc-4e35-8f7e-b7d2dde6feb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGgoBWz1MdFda6UL6eaMDa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 23666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 758
      },
      "output_tokens": 47,
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

_source line 8 · 2026-05-14T12:48:55.579Z_

<details><summary>↩ Tool result · `toolu_01BCHg2yBb9UGfNryHFismrk`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "a3771941-0aed-402d-9f66-5611be27c23e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017vsxt5egN2jkmvfhdwPTzZ`</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -rn \"near-equivalent\" /root/autodl-tmp/simgate-modular-routing/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "939216dc-48b7-4ffd-90e6-58f4b4dd7f7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KW64VdszincmcCau6eNXa6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 24424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
      },
      "output_tokens": 71,
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

_source line 10 · 2026-05-14T12:49:03.145Z_

<details><summary>↩ Tool result · `toolu_017vsxt5egN2jkmvfhdwPTzZ`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.83}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "bd2dc90c-d675-40e5-b704-8d51234ef5d4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.83}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.83}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Ln7RocZGMNxVJziT3A4LBh`</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -rn \"near\" /root/autodl-tmp/simgate-modular-routing/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "067fa3c7-31c8-46ca-b519-f03ef6d9f45c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tiuCCUyET68KeNyUPUJoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 206,
      "cache_read_input_tokens": 24653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 206
      },
      "output_tokens": 69,
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

_source line 12 · 2026-05-14T12:49:09.731Z_

<details><summary>↩ Tool result · `toolu_01Ln7RocZGMNxVJziT3A4LBh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/simgate-modular-routing/paper/main.tex:18:Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for 90.41\\\\% of the routing signal (Death Avoidance Factor). Per-task death rate differentials correlate near-perfectly with routing benefit ($r$ = 0.9698, $p$ = 8.12$\\\\times$10$^{-7}$). The oracle router agrees with always-deterministic on 96.2\\\\% of decisions, and a trained router achieves only 58.1\\\\% balanced accuracy---near random. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:74:As a simple routing heuristic, we test keyword-based rules that route to deterministic computation when actions contain science-related verbs. ScienceWorld actions use generic interaction verbs (\\\\texttt{pick up}, \\\\texttt{move}, \\\\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\\\%, v3: 2.8\\\\%, degenerating to always-internal). No keyword granularity provides meaningful routing discrimination.\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:130:\\\\paragraph{Classification head.} A linear classification head appended to the LLM's hidden representations degenerates to predicting always-deterministic (0\\\\% internal recall) across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling.\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:132:\\\\paragraph{Implicit router.} Fine-tuning Qwen3-1.7B yields logit-level accuracy of 74.5\\\\% with balanced accuracy of 79\\\\%, demonstrating learnable routing structure beyond degenerate prediction. At the generation level, accuracy drops to 65.36\\\\% (internal recall 51.5\\\\%), revealing a representation-to-generation gap. End-to-end deployment confirms this: the router invokes the simulator 97.0\\\\% of the time---near-always-deterministic despite non-degenerate logit-level patterns.\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:154:We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Across 245 ScienceWorld episodes, death avoidance accounts for 90.41\\\\% of routing signal ($\\\\Delta_\\\\text{full}$ = +29.60 vs.\\\\ $\\\\Delta_\\\\text{nd}$ = +2.84). This concentration is corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\% agreement with always-deterministic), and near-random trained router accuracy (58.1\\\\%). Future work should extend to step-level counterfactual labeling and evaluate generalization to environments with different failure modes.\\n/root/autodl-tmp/simgate-modular-routing/paper/abstract.tex:2:Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for approximately 90\\\\% of the routing signal (Death Avoidance Factor), with per-task death rate differentials correlating near-perfectly with routing benefit. The oracle router agrees with always-deterministic on 96.2\\\\% of decisions, and a trained router achieves near-random balanced accuracy. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\n/root/autodl-tmp/simgate-modular-routing/paper/experiments.tex:50:Keyword-based routing fails structurally: ScienceWorld actions use generic verbs (\\\\texttt{pick up}, \\\\texttt{move}, \\\\texttt{connect}) rather than science-specific terms, causing match rates to cluster at extremes---near-total (85.8\\\\%, degenerating to always-deterministic) or negligible ($<$5\\\\%, degenerating to always-internal).\\n/root/autodl-tmp/simgate-modular-routing/paper/experiments.tex:59:\\\\paragraph{Classification head.} A linear head appended to the LLM's hidden representations degenerates to always-deterministic (0\\\\% internal recall) across all configurations (class weighting, focal loss, undersampling, temperature scaling).\\n/root/autodl-tmp/simgate-modular-routing/paper/conclusion.tex:3:We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\\\\% of the routing signal ($\\\\Delta_\\\\text{full}$ = +29.60 vs.\\\\ $\\\\Delta_\\\\text{nd}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\\\\%).\\n/root/autodl-tmp/simgate-modular-routing/paper/main.log:500:\\\\OT1/ptm/m/n/10 task death rate dif-fer-en-tials cor-re-late near-\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "fdfba8a7-bb04-4a2e-afdf-c604b820bdd2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/simgate-modular-routing/paper/main.tex:18:Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\\\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for 90.41\\\\\\\\% of the routing signal (Death Avoidance Factor). Per-task death rate differentials correlate near-perfectly with routing benefit ($r$ = 0.9698, $p$ = 8.12$\\\\\\\\times$10$^{-7}$). The oracle router agrees with always-deterministic on 96.2\\\\\\\\% of decisions, and a trained router achieves only 58.1\\\\\\\\% balanced accuracy---near random. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:74:As a simple routing heuristic, we test keyword-based rules that route to deterministic computation when actions contain science-related verbs. ScienceWorld actions use generic interaction verbs (\\\\\\\\texttt{pick up}, \\\\\\\\texttt{move}, \\\\\\\\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\\\\\\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\\\\\\\%, v3: 2.8\\\\\\\\%, degenerating to always-internal). No keyword granularity provides meaningful routing discrimination.\\\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:130:\\\\\\\\paragraph{Classification head.} A linear classification head appended to the LLM's hidden representations degenerates to predicting always-deterministic (0\\\\\\\\% internal recall) across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling.\\\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:132:\\\\\\\\paragraph{Implicit router.} Fine-tuning Qwen3-1.7B yields logit-level accuracy of 74.5\\\\\\\\% with balanced accuracy of 79\\\\\\\\%, demonstrating learnable routing structure beyond degenerate prediction. At the generation level, accuracy drops to 65.36\\\\\\\\% (internal recall 51.5\\\\\\\\%), revealing a representation-to-generation gap. End-to-end deployment confirms this: the router invokes the simulator 97.0\\\\\\\\% of the time---near-always-deterministic despite non-degenerate logit-level patterns.\\\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:154:We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Across 245 ScienceWorld episodes, death avoidance accounts for 90.41\\\\\\\\% of routing signal ($\\\\\\\\Delta_\\\\\\\\text{full}$ = +29.60 vs.\\\\\\\\ $\\\\\\\\Delta_\\\\\\\\text{nd}$ = +2.84). This concentration is corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\\\\\% agreement with always-deterministic), and near-random trained router accuracy (58.1\\\\\\\\%). Future work should extend to step-level counterfactual labeling and evaluate generalization to environments with different failure modes.\\\\n/root/autodl-tmp/simgate-modular-routing/paper/abstract.tex:2:Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\\\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for approximately 90\\\\\\\\% of the routing signal (Death Avoidance Factor), with per-task death rate differentials correlating near-perfectly with routing benefit. The oracle router agrees with always-deterministic on 96.2\\\\\\\\% of decisions, and a trained router achieves near-random balanced accuracy. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\\\n/root/autodl-tmp/simgate-modular-routing/paper/experiments.tex:50:Keyword-based routing fails structurally: ScienceWorld actions use generic verbs (\\\\\\\\texttt{pick up}, \\\\\\\\texttt{move}, \\\\\\\\texttt{connect}) rather than science-specific terms, causing match rates to cluster at extremes---near-total (85.8\\\\\\\\%, degenerating to always-deterministic) or negligible ($<$5\\\\\\\\%, degenerating to always-internal).\\\\n/root/autodl-tmp/simgate-modular-routing/paper/experiments.tex:59:\\\\\\\\paragraph{Classification head.} A linear head appended to the LLM's hidden representations degenerates to always-deterministic (0\\\\\\\\% internal recall) across all configurations (class weighting, focal loss, undersampling, temperature scaling).\\\\n/root/autodl-tmp/simgate-modular-routing/paper/conclusion.tex:3:We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\\\\\\\\% of the routing signal ($\\\\\\\\Delta_\\\\\\\\text{full}$ = +29.60 vs.\\\\\\\\ $\\\\\\\\Delta_\\\\\\\\text{nd}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\\\\\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\\\\\\\\%).\\\\n/root/autodl-tmp/simgate-modular-routing/paper/main.log:500:\\\\\\\\OT1/ptm/m/n/10 task death rate dif-fer-en-tials cor-re-late near-\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.72}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/simgate-modular-routing/paper/main.tex:18:Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for 90.41\\\\% of the routing signal (Death Avoidance Factor). Per-task death rate differentials correlate near-perfectly with routing benefit ($r$ = 0.9698, $p$ = 8.12$\\\\times$10$^{-7}$). The oracle router agrees with always-deterministic on 96.2\\\\% of decisions, and a trained router achieves only 58.1\\\\% balanced accuracy---near random. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:74:As a simple routing heuristic, we test keyword-based rules that route to deterministic computation when actions contain science-related verbs. ScienceWorld actions use generic interaction verbs (\\\\texttt{pick up}, \\\\texttt{move}, \\\\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\\\%, v3: 2.8\\\\%, degenerating to always-internal). No keyword granularity provides meaningful routing discrimination.\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:130:\\\\paragraph{Classification head.} A linear classification head appended to the LLM's hidden representations degenerates to predicting always-deterministic (0\\\\% internal recall) across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling.\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:132:\\\\paragraph{Implicit router.} Fine-tuning Qwen3-1.7B yields logit-level accuracy of 74.5\\\\% with balanced accuracy of 79\\\\%, demonstrating learnable routing structure beyond degenerate prediction. At the generation level, accuracy drops to 65.36\\\\% (internal recall 51.5\\\\%), revealing a representation-to-generation gap. End-to-end deployment confirms this: the router invokes the simulator 97.0\\\\% of the time---near-always-deterministic despite non-degenerate logit-level patterns.\\n/root/autodl-tmp/simgate-modular-routing/paper/main.tex:154:We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Across 245 ScienceWorld episodes, death avoidance accounts for 90.41\\\\% of routing signal ($\\\\Delta_\\\\text{full}$ = +29.60 vs.\\\\ $\\\\Delta_\\\\text{nd}$ = +2.84). This concentration is corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\% agreement with always-deterministic), and near-random trained router accuracy (58.1\\\\%). Future work should extend to step-level counterfactual labeling and evaluate generalization to environments with different failure modes.\\n/root/autodl-tmp/simgate-modular-routing/paper/abstract.tex:2:Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for approximately 90\\\\% of the routing signal (Death Avoidance Factor), with per-task death rate differentials correlating near-perfectly with routing benefit. The oracle router agrees with always-deterministic on 96.2\\\\% of decisions, and a trained router achieves near-random balanced accuracy. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\n/root/autodl-tmp/simgate-modular-routing/paper/experiments.tex:50:Keyword-based routing fails structurally: ScienceWorld actions use generic verbs (\\\\texttt{pick up}, \\\\texttt{move}, \\\\texttt{connect}) rather than science-specific terms, causing match rates to cluster at extremes---near-total (85.8\\\\%, degenerating to always-deterministic) or negligible ($<$5\\\\%, degenerating to always-internal).\\n/root/autodl-tmp/simgate-modular-routing/paper/experiments.tex:59:\\\\paragraph{Classification head.} A linear head appended to the LLM's hidden representations degenerates to always-deterministic (0\\\\% internal recall) across all configurations (class weighting, focal loss, undersampling, temperature scaling).\\n/root/autodl-tmp/simgate-modular-routing/paper/conclusion.tex:3:We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\\\\% of the routing signal ($\\\\Delta_\\\\text{full}$ = +29.60 vs.\\\\ $\\\\Delta_\\\\text{nd}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\\\\%).\\n/root/autodl-tmp/simgate-modular-routing/paper/main.log:500:\\\\OT1/ptm/m/n/10 task death rate dif-fer-en-tials cor-re-late near-\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the grep results. I need to find "near-equivalent" but it doesn't appear anywhere. The task says to sync the Abstract's "near-equivalent" wording, but it seems it may have already been changed or the wording is different.

Let me look more carefully at what's in the abstract. The abstract.tex line 2 says:

"...we find that death avoidance accounts for approximately 90\% of the routing signal (Death Avoidance Factor), with per-task death rate differentials correlating near-perfectly with routing benefit. The oracle router agrees with always-deterministic on 96.2\% of decisions, and a trained router achieves near-random balanced accuracy."
 
I'm re-reading the context and realizing the task description might be based on outdated information—grep confirms "near-equivalent" doesn't exist in the current paper, suggesting it was already removed or the wording differs from what the task describes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "ccff3286-325a-4e36-852b-5a53d2daf939",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTt2bex3VHbuPWvRSAsCJ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 24859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1830
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

_source line 14_

"near-equivalent" 在所有 tex 文件中均不存在。让我看一下 abstract.tex 和 experiments.tex 的完整内容，确认当前措辞。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "288d657f-91a0-4f88-9a1f-a735ee56bbe0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTt2bex3VHbuPWvRSAsCJ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 24859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1830
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

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KXaKAbo3RNf4Db2b4Tc5dP`</summary>

```json
{
  "server": "westb-13313",
  "command": "cat -n /root/autodl-tmp/simgate-modular-routing/paper/abstract.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "0b02a71f-893a-4606-8db8-410332edae9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTt2bex3VHbuPWvRSAsCJ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 24859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1830
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

_source line 16 · 2026-05-14T12:49:25.859Z_

<details><summary>↩ Tool result · `toolu_01KXaKAbo3RNf4Db2b4Tc5dP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\begin{abstract}\\n     2\\tModular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for approximately 90\\\\% of the routing signal (Death Avoidance Factor), with per-task death rate differentials correlating near-perfectly with routing benefit. The oracle router agrees with always-deterministic on 96.2\\\\% of decisions, and a trained router achieves near-random balanced accuracy. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\n     3\\t\\\\end{abstract}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "dff02c28-12d7-4f21-8cec-bc2cfff0017c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"     1\\\\t\\\\\\\\begin{abstract}\\\\n     2\\\\tModular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\\\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for approximately 90\\\\\\\\% of the routing signal (Death Avoidance Factor), with per-task death rate differentials correlating near-perfectly with routing benefit. The oracle router agrees with always-deterministic on 96.2\\\\\\\\% of decisions, and a trained router achieves near-random balanced accuracy. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\\\n     3\\\\t\\\\\\\\end{abstract}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\begin{abstract}\\n     2\\tModular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for approximately 90\\\\% of the routing signal (Death Avoidance Factor), with per-task death rate differentials correlating near-perfectly with routing benefit. The oracle router agrees with always-deterministic on 96.2\\\\% of decisions, and a trained router achieves near-random balanced accuracy. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\n     3\\t\\\\end{abstract}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YUGBPnX93tL3U4xTiFotDd`</summary>

```json
{
  "server": "westb-13313",
  "command": "head -30 /root/autodl-tmp/simgate-modular-routing/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "8b088f34-5549-4737-83b7-268c64606202",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTt2bex3VHbuPWvRSAsCJ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 24859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1830
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

_source line 18 · 2026-05-14T12:49:26.797Z_

<details><summary>↩ Tool result · `toolu_01YUGBPnX93tL3U4xTiFotDd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\n\\\\subsection{Setup}\\n\\\\label{sec:exp-setup}\\n\\nWe evaluate on ScienceWorld \\\\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \\\\S\\\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.\\n\\n\\\\subsection{Death Avoidance Decomposition}\\n\\\\label{sec:death-decomp}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig1_daf_scatter.pdf}\\n\\\\caption{Per-task death rate differential (internal minus deterministic) vs.\\\\ $\\\\Delta_{\\\\text{full}}$. Each point represents one of 11 task types. Regression: $r = 0.9698$ ($p = 8.12 \\\\times 10^{-7}$).}\\n\\\\label{fig:decomposition}\\n\\\\end{figure}\\n\\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\\\Delta_{\\\\text{full}} = +29.60$ points. Excluding all episodes where either strategy results in death, the gap collapses to $\\\\Delta_{\\\\text{no\\\\_death}} = +2.84$. The resulting DAF (\\\\S\\\\ref{sec:daf}) is 90.41\\\\%: approximately 90\\\\% of the deterministic strategy's advantage is attributable to death avoidance.\\n\\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential and $\\\\Delta_{\\\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\\\times 10^{-7}$; Figure~\\\\ref{fig:decomposition}). The internal strategy dies in 42.9\\\\% of episodes versus 16.3\\\\% for deterministic---a 2.6$\\\\times$ ratio driving the bulk of the score difference.\\n\\nThe label distribution reflects this asymmetry: 86 \\\\texttt{det\\\\_preferred}, 9 \\\\texttt{internal\\\\_preferred}, 150 \\\\texttt{no\\\\_preference}. When internal reasoning does not cause death, it performs comparably to deterministic computation.\\n\\nOne task reveals residual non-death signal: \\\\texttt{find-non-living-thing} ($n=40$) has zero deaths yet $\\\\Delta_{\\\\text{full}} = +9.58$, entirely from non-death differences. Among the 10 death-prone task types, however, death avoidance overwhelms non-death signal.\\n\\n\\\\subsection{Baselines}\\n\\\\label{sec:baselines}\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "d9579b38-0d8d-4bda-83a9-85a8756aa530",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Experiments}\\\\n\\\\n\\\\\\\\subsection{Setup}\\\\n\\\\\\\\label{sec:exp-setup}\\\\n\\\\nWe evaluate on ScienceWorld \\\\\\\\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \\\\\\\\S\\\\\\\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.\\\\n\\\\n\\\\\\\\subsection{Death Avoidance Decomposition}\\\\n\\\\\\\\label{sec:death-decomp}\\\\n\\\\n\\\\\\\\begin{figure}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\includegraphics[width=\\\\\\\\columnwidth]{fig1_daf_scatter.pdf}\\\\n\\\\\\\\caption{Per-task death rate differential (internal minus deterministic) vs.\\\\\\\\ $\\\\\\\\Delta_{\\\\\\\\text{full}}$. Each point represents one of 11 task types. Regression: $r = 0.9698$ ($p = 8.12 \\\\\\\\times 10^{-7}$).}\\\\n\\\\\\\\label{fig:decomposition}\\\\n\\\\\\\\end{figure}\\\\n\\\\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\\\\\\\Delta_{\\\\\\\\text{full}} = +29.60$ points. Excluding all episodes where either strategy results in death, the gap collapses to $\\\\\\\\Delta_{\\\\\\\\text{no\\\\\\\\_death}} = +2.84$. The resulting DAF (\\\\\\\\S\\\\\\\\ref{sec:daf}) is 90.41\\\\\\\\%: approximately 90\\\\\\\\% of the deterministic strategy's advantage is attributable to death avoidance.\\\\n\\\\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential and $\\\\\\\\Delta_{\\\\\\\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\\\\\\\times 10^{-7}$; Figure~\\\\\\\\ref{fig:decomposition}). The internal strategy dies in 42.9\\\\\\\\% of episodes versus 16.3\\\\\\\\% for deterministic---a 2.6$\\\\\\\\times$ ratio driving the bulk of the score difference.\\\\n\\\\nThe label distribution reflects this asymmetry: 86 \\\\\\\\texttt{det\\\\\\\\_preferred}, 9 \\\\\\\\texttt{internal\\\\\\\\_preferred}, 150 \\\\\\\\texttt{no\\\\\\\\_preference}. When internal reasoning does not cause death, it performs comparably to deterministic computation.\\\\n\\\\nOne task reveals residual non-death signal: \\\\\\\\texttt{find-non-living-thing} ($n=40$) has zero deaths yet $\\\\\\\\Delta_{\\\\\\\\text{full}} = +9.58$, entirely from non-death differences. Among the 10 death-prone task types, however, death avoidance overwhelms non-death signal.\\\\n\\\\n\\\\\\\\subsection{Baselines}\\\\n\\\\\\\\label{sec:baselines}\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\n\\\\subsection{Setup}\\n\\\\label{sec:exp-setup}\\n\\nWe evaluate on ScienceWorld \\\\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \\\\S\\\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.\\n\\n\\\\subsection{Death Avoidance Decomposition}\\n\\\\label{sec:death-decomp}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{fig1_daf_scatter.pdf}\\n\\\\caption{Per-task death rate differential (internal minus deterministic) vs.\\\\ $\\\\Delta_{\\\\text{full}}$. Each point represents one of 11 task types. Regression: $r = 0.9698$ ($p = 8.12 \\\\times 10^{-7}$).}\\n\\\\label{fig:decomposition}\\n\\\\end{figure}\\n\\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\\\Delta_{\\\\text{full}} = +29.60$ points. Excluding all episodes where either strategy results in death, the gap collapses to $\\\\Delta_{\\\\text{no\\\\_death}} = +2.84$. The resulting DAF (\\\\S\\\\ref{sec:daf}) is 90.41\\\\%: approximately 90\\\\% of the deterministic strategy's advantage is attributable to death avoidance.\\n\\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential and $\\\\Delta_{\\\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\\\times 10^{-7}$; Figure~\\\\ref{fig:decomposition}). The internal strategy dies in 42.9\\\\% of episodes versus 16.3\\\\% for deterministic---a 2.6$\\\\times$ ratio driving the bulk of the score difference.\\n\\nThe label distribution reflects this asymmetry: 86 \\\\texttt{det\\\\_preferred}, 9 \\\\texttt{internal\\\\_preferred}, 150 \\\\texttt{no\\\\_preference}. When internal reasoning does not cause death, it performs comparably to deterministic computation.\\n\\nOne task reveals residual non-death signal: \\\\texttt{find-non-living-thing} ($n=40$) has zero deaths yet $\\\\Delta_{\\\\text{full}} = +9.58$, entirely from non-death differences. Among the 10 death-prone task types, however, death avoidance overwhelms non-death signal.\\n\\n\\\\subsection{Baselines}\\n\\\\label{sec:baselines}\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the situation clearly:

1. **"near-equivalent" doesn't exist** in any tex file — the task description's premise is incorrect.

2. The abstract says: "death avoidance accounts for approximately 90% of the routing signal" — it doesn't explicitly describe the non-death gap at all. It doesn't say "near-equivalent" anywhere.

3. The experiments.tex (around line 25-26) says: "When internal reasoning does not cause death, it performs comparably to deterministic computation." — this uses "comparably" not "near-equivalent".

But wait, the experiments section also says $\Delta_{\text{no\_death}} = +2.84$ and the DAF is 90.41%. 

The abstract's mention of ~90% routing signal aligns with these numbers. Since "near-equivalent" doesn't actually appear in the files, I should check if main.tex has a different version of the abstract that might contain this phrase. I'm checking whether main.tex includes the abstract.tex file or defines the abstract inline, since there seem to be two slightly different versions of the abstract text floating around.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "800222dc-ef12-459a-bdd4-b0e42dce82fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5H5pGP6DVKCUZsBy37efU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 26689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2010
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

_source line 20_

"near-equivalent" 不存在于任何 tex 文件中。让我检查 main.tex 是否 `\input{abstract}` 还是内联 abstract，以及两者是否一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "2a11a932-4a4d-48b8-8f0f-19c405ac78b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5H5pGP6DVKCUZsBy37efU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 26689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2010
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

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016pE6aZYaKQokUMJowBCaQ4`</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -n \"abstract\\|input\\|include\" /root/autodl-tmp/simgate-modular-routing/paper/main.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "a1af2bf2-4752-4067-8400-6e03e6a3c13b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5H5pGP6DVKCUZsBy37efU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 26689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2010
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

_source line 22 · 2026-05-14T12:49:42.976Z_

<details><summary>↩ Tool result · `toolu_016pE6aZYaKQokUMJowBCaQ4`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "b2109e18-49db-47b7-939d-15e519e85c7e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017yqdPyCjgVEqk6cFpqYLpf`</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -n \"abstract\" /root/autodl-tmp/simgate-modular-routing/paper/main.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "0b37d1d2-21ac-498b-b380-e655c6ae2ede",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014g9hYHrRe7EACaYHHabUZd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 28699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 926
      },
      "output_tokens": 68,
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MGXAKdA1tf9AvkjBL6inG8`</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -n \"input\" /root/autodl-tmp/simgate-modular-routing/paper/main.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "b6bd3f66-ae2b-4721-b98c-67432818d1b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014g9hYHrRe7EACaYHHabUZd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 28699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 926
      },
      "output_tokens": 68,
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

_source line 25 · 2026-05-14T12:49:52.372Z_

<details><summary>↩ Tool result · `toolu_017yqdPyCjgVEqk6cFpqYLpf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"17:\\\\begin{abstract}\\n19:\\\\end{abstract}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "8c751738-5f9d-400a-80db-916d76647521",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"17:\\\\\\\\begin{abstract}\\\\n19:\\\\\\\\end{abstract}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"17:\\\\begin{abstract}\\n19:\\\\end{abstract}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T12:49:53.309Z_

<details><summary>↩ Tool result · `toolu_01MGXAKdA1tf9AvkjBL6inG8`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.93}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "e20ef38b-4069-4cd8-afd2-01eb2aec7413",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.93}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.93}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
So main.tex has an inline abstract at lines 17-19 (the abstract is all on line 18). It doesn't use `\input{abstract}`. There's a separate abstract.tex file but it's not included by main.tex.

Let me check main.tex line 18 more carefully. From the earlier grep, main.tex line 18 has this abstract text (reformatted for readability):

"Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97% of steps yield tied outcomes, rendering step-level analysis uninformative. 

Now I'm looking at the rest of the abstract, which describes their proposed episode-level counterfactual analysis approach. They tested it on 245 episodes across 11 task types using Qwen2.5-7B-Instruct, and found that death avoidance accounts for 90.41% of the routing signal. The correlation between per-task death rate differentials and routing benefit is nearly perfect at r = 0.9698. Interestingly, the oracle router agrees with always-deterministic on 96.2% of decisions, and their trained router only achieves 58.1% balanced accuracy, which is barely better than random.

But now I'm noticing something in the experiments section—there's a tension in how they're describing the results. They say "comparably" when internal reasoning doesn't cause death, but then quantify the gap as +2.84, which they characterize elsewhere as "small but non-negligible." The word "comparably" seems to downplay what's actually a measurable difference, so there's an inconsistency in how they're framing this finding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "f37241ba-a4e1-481f-9f7c-ca934e255213",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxwD9WifhFG6YGJdSKWPFo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 29625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
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

_source line 28_

"near-equivalent" 在所有 tex 文件中不存在。但存在两个相关问题：

1. **main.tex 和 abstract.tex 的 abstract 内容不同步** — main.tex 用内联 abstract（第17-19行），abstract.tex 是独立文件但未被引用
2. **experiments.tex 第26行**用了 "performs comparably"，与 "small but non-negligible" 表述不一致

让我看 experiments.tex 完整相关段落和 conclusion.tex。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "bcacee57-b288-4f4f-be31-b1c97c87ca64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxwD9WifhFG6YGJdSKWPFo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 29625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
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

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01U2RTW68qioKiPtfEZyfn3z`</summary>

```json
{
  "server": "westb-13313",
  "command": "cat -n /root/autodl-tmp/simgate-modular-routing/paper/conclusion.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "531cf04f-b7a2-401c-8005-72ef872889f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxwD9WifhFG6YGJdSKWPFo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 29625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
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

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Vz8z6xJQRvWA8x2tsLWRdJ`</summary>

```json
{
  "server": "westb-13313",
  "command": "cat -n /root/autodl-tmp/simgate-modular-routing/paper/main.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "263da671-ad95-4029-b047-50dc0d7aa4a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxwD9WifhFG6YGJdSKWPFo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 29625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 469
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

_source line 31 · 2026-05-14T12:50:17.443Z_

<details><summary>↩ Tool result · `toolu_01U2RTW68qioKiPtfEZyfn3z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Conclusion}\\n     2\\t\\n     3\\tWe presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\\\\% of the routing signal ($\\\\Delta_\\\\text{full}$ = +29.60 vs.\\\\ $\\\\Delta_\\\\text{nd}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\\\\%).\\n     4\\t\\n     5\\t\\\\paragraph{Limitations.} Our analysis uses a single benchmark (ScienceWorld) with one LLM backbone (Qwen2.5-7B-Instruct); the $-100$ death penalty may amplify DAF. The router trains on pure-strategy trajectories but deploys in mixed-strategy settings, introducing distribution shift \\\\cite{dagger-2011}. Future work should extend to step-level labeling, diverse failure modes, and stronger backbones.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "cae4290a-2607-47b0-aa7e-b9554f4a2983",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"     1\\\\t\\\\\\\\section{Conclusion}\\\\n     2\\\\t\\\\n     3\\\\tWe presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\\\\\\\\% of the routing signal ($\\\\\\\\Delta_\\\\\\\\text{full}$ = +29.60 vs.\\\\\\\\ $\\\\\\\\Delta_\\\\\\\\text{nd}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\\\\\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\\\\\\\\%).\\\\n     4\\\\t\\\\n     5\\\\t\\\\\\\\paragraph{Limitations.} Our analysis uses a single benchmark (ScienceWorld) with one LLM backbone (Qwen2.5-7B-Instruct); the $-100$ death penalty may amplify DAF. The router trains on pure-strategy trajectories but deploys in mixed-strategy settings, introducing distribution shift \\\\\\\\cite{dagger-2011}. Future work should extend to step-level labeling, diverse failure modes, and stronger backbones.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Conclusion}\\n     2\\t\\n     3\\tWe presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\\\\% of the routing signal ($\\\\Delta_\\\\text{full}$ = +29.60 vs.\\\\ $\\\\Delta_\\\\text{nd}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\\\\%).\\n     4\\t\\n     5\\t\\\\paragraph{Limitations.} Our analysis uses a single benchmark (ScienceWorld) with one LLM backbone (Qwen2.5-7B-Instruct); the $-100$ death penalty may amplify DAF. The router trains on pure-strategy trajectories but deploys in mixed-strategy settings, introducing distribution shift \\\\cite{dagger-2011}. Future work should extend to step-level labeling, diverse failure modes, and stronger backbones.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T12:50:18.510Z_

<details><summary>↩ Tool result · `toolu_01Vz8z6xJQRvWA8x2tsLWRdJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\documentclass[11pt]{article}\\n     2\\t\\\\usepackage[review]{acl}\\n     3\\t\\\\usepackage{times}\\n     4\\t\\\\usepackage{latexsym}\\n     5\\t\\\\usepackage{graphicx}\\n     6\\t\\\\usepackage{booktabs}\\n     7\\t\\\\usepackage{amsmath}\\n     8\\t\\\\usepackage{url}\\n     9\\t\\n    10\\t\\\\title{Death Avoidance Dominates the Routing Signal in Modular LLM Agents}\\n    11\\t\\\\author{Anonymous ACL Submission}\\n    12\\t\\\\date{}\\n    13\\t\\n    14\\t\\\\begin{document}\\n    15\\t\\\\maketitle\\n    16\\t\\n    17\\t\\\\begin{abstract}\\n    18\\tModular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for 90.41\\\\% of the routing signal (Death Avoidance Factor). Per-task death rate differentials correlate near-perfectly with routing benefit ($r$ = 0.9698, $p$ = 8.12$\\\\times$10$^{-7}$). The oracle router agrees with always-deterministic on 96.2\\\\% of decisions, and a trained router achieves only 58.1\\\\% balanced accuracy---near random. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\n    19\\t\\\\end{abstract}\\n    20\\t\\n    21\\t\\\\section{Introduction}\\n    22\\t\\n    23\\tWhen a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\\\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated, or failing to model that metal conducts heat differently than glass---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\\n    24\\t\\n    25\\tExisting routing approaches \\\\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\\\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\\\\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\\\\S\\\\ref{sec:collection}). Keyword-based heuristics (\\\\S\\\\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\\\\texttt{pour}, \\\\texttt{move}, \\\\texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.\\n    26\\t\\n    27\\tWe propose \\\\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\\\S\\\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\\\Delta_{\\\\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\\\\Delta_{\\\\text{no\\\\_death}} = +2.84$---a Death Avoidance Factor (DAF; \\\\S\\\\ref{sec:daf}) of 90.41\\\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\\\times 10\\n\\n... [截断: 输出过长，省略 10980 字符] ...\\n\\n.8\\\\%, indicating seed-dependent decision boundaries with consistent weak discriminability. This pattern supports that the labels encode minimal routing structure beyond death avoidance.\\n   135\\t\\n   136\\tThese results yield two observations. First, counterfactual labels encode genuine routing patterns at the representation level---ruling out uninformative labels and pointing to the episode-to-step granularity mismatch as the bottleneck. Second, generation-level expression of these patterns remains an open challenge; step-level counterfactual labeling may be a productive direction.\\n   137\\t\\n   138\\t\\\\section{Related Work}\\n   139\\t\\n   140\\t\\\\paragraph{Tool-Use Learning.}\\n   141\\tToolformer \\\\cite{toolformer-2024} inserts API calls via self-supervised filtering; ART \\\\cite{art-2023} delegates tool selection to reasoning chains; Chameleon \\\\cite{chameleon-2024} composes modules under LLM-as-planner orchestration; ReTool \\\\cite{retool-2026} uses RL for implicit code-interpreter invocation. These methods learn \\\\emph{which tool} to use but do not analyze what signal drives routing. We generate labels via episode-level counterfactual analysis, revealing ${\\\\sim}90\\\\%$ is death avoidance.\\n   142\\t\\n   143\\t\\\\paragraph{Adaptive Computation.}\\n   144\\tCogRouter \\\\cite{cogrouter-2026} achieves 82.3\\\\% on ScienceWorld via cognitive depth routing; ARES \\\\cite{ares-2026} reduces token cost by 52.7\\\\% with per-step effort selection; Mixture-of-Recursions \\\\cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing. These route \\\\emph{how much} to reason; we route \\\\emph{which modality}. Our decomposition reveals death avoidance accounts for ${\\\\sim}90\\\\%$ of the performance gap.\\n   145\\t\\n   146\\t\\\\paragraph{World Model Routing.}\\n   147\\tITP \\\\cite{itp-2026} augments agents with world model lookahead; Dyna-Think \\\\cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost. Both route to \\\\emph{approximate} world models; our deterministic modality provides \\\\emph{exact} transitions, and counterfactual analysis reveals this exactness matters almost exclusively for death avoidance ($\\\\Delta_\\\\text{nd}$ is only 9.6\\\\% of the full gap).\\n   148\\t\\n   149\\t\\\\paragraph{Agent Frameworks.}\\n   150\\tReAct \\\\cite{react-2023} provides our internal-reasoning baseline; ScienceWorld \\\\cite{scienceworld-2022} is the evaluation environment. MTRouter \\\\cite{mtrouter-2026} routes between LLMs for cost optimization but targets model-level rather than modality-level selection. Our work asks \\\\emph{what} a router captures: the answer is dominated by catastrophic-failure prevention, suggesting future designs should prioritize safety-aware computation allocation.\\n   151\\t\\n   152\\t\\\\section{Conclusion}\\n   153\\t\\n   154\\tWe presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Across 245 ScienceWorld episodes, death avoidance accounts for 90.41\\\\% of routing signal ($\\\\Delta_\\\\text{full}$ = +29.60 vs.\\\\ $\\\\Delta_\\\\text{nd}$ = +2.84). This concentration is corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\% agreement with always-deterministic), and near-random trained router accuracy (58.1\\\\%). Future work should extend to step-level counterfactual labeling and evaluate generalization to environments with different failure modes.\\n   155\\t\\n   156\\t\\\\section*{Limitations}\\n   157\\t\\n   158\\tOur analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. Step-level labeling with denser rewards is a natural extension. The logit-to-generation gap in the implicit router warrants further investigation.\\n   159\\t\\n   160\\t\\\\bibliography{references}\\n   161\\t\\n   162\\t\\\\end{document}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "d5c35caa-3705-47cd-bc8c-2e46b9e7019d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"     1\\\\t\\\\\\\\documentclass[11pt]{article}\\\\n     2\\\\t\\\\\\\\usepackage[review]{acl}\\\\n     3\\\\t\\\\\\\\usepackage{times}\\\\n     4\\\\t\\\\\\\\usepackage{latexsym}\\\\n     5\\\\t\\\\\\\\usepackage{graphicx}\\\\n     6\\\\t\\\\\\\\usepackage{booktabs}\\\\n     7\\\\t\\\\\\\\usepackage{amsmath}\\\\n     8\\\\t\\\\\\\\usepackage{url}\\\\n     9\\\\t\\\\n    10\\\\t\\\\\\\\title{Death Avoidance Dominates the Routing Signal in Modular LLM Agents}\\\\n    11\\\\t\\\\\\\\author{Anonymous ACL Submission}\\\\n    12\\\\t\\\\\\\\date{}\\\\n    13\\\\t\\\\n    14\\\\t\\\\\\\\begin{document}\\\\n    15\\\\t\\\\\\\\maketitle\\\\n    16\\\\t\\\\n    17\\\\t\\\\\\\\begin{abstract}\\\\n    18\\\\tModular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\\\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for 90.41\\\\\\\\% of the routing signal (Death Avoidance Factor). Per-task death rate differentials correlate near-perfectly with routing benefit ($r$ = 0.9698, $p$ = 8.12$\\\\\\\\times$10$^{-7}$). The oracle router agrees with always-deterministic on 96.2\\\\\\\\% of decisions, and a trained router achieves only 58.1\\\\\\\\% balanced accuracy---near random. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\\\n    19\\\\t\\\\\\\\end{abstract}\\\\n    20\\\\t\\\\n    21\\\\t\\\\\\\\section{Introduction}\\\\n    22\\\\t\\\\n    23\\\\tWhen a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\\\\\\\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated, or failing to model that metal conducts heat differently than glass---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\\\\n    24\\\\t\\\\n    25\\\\tExisting routing approaches \\\\\\\\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\\\\\\\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\\\\\\\\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\\\\\\\\S\\\\\\\\ref{sec:collection}). Keyword-based heuristics (\\\\\\\\S\\\\\\\\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\\\\\\\\texttt{pour}, \\\\\\\\texttt{move}, \\\\\\\\texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.\\\\n    26\\\\t\\\\n    27\\\\tWe propose \\\\\\\\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\\\\\\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\\\\\\\S\\\\\\\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\\\\\\\Delta_{\\\\\\\\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\\\\\\\\Delta_{\\\\\\\\text{no\\\\\\\\_death}} = +2.84$---a Death Avoidance Factor (DAF; \\\\\\\\S\\\\\\\\ref{sec:daf}) of 90.41\\\\\\\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\\\\\\\times 10\\\\n\\\\n... [截断: 输出过长，省略 10980 字符] ...\\\\n\\\\n.8\\\\\\\\%, indicating seed-dependent decision boundaries with consistent weak discriminability. This pattern supports that the labels encode minimal routing structure beyond death avoidance.\\\\n   135\\\\t\\\\n   136\\\\tThese results yield two observations. First, counterfactual labels encode genuine routing patterns at the representation level---ruling out uninformative labels and pointing to the episode-to-step granularity mismatch as the bottleneck. Second, generation-level expression of these patterns remains an open challenge; step-level counterfactual labeling may be a productive direction.\\\\n   137\\\\t\\\\n   138\\\\t\\\\\\\\section{Related Work}\\\\n   139\\\\t\\\\n   140\\\\t\\\\\\\\paragraph{Tool-Use Learning.}\\\\n   141\\\\tToolformer \\\\\\\\cite{toolformer-2024} inserts API calls via self-supervised filtering; ART \\\\\\\\cite{art-2023} delegates tool selection to reasoning chains; Chameleon \\\\\\\\cite{chameleon-2024} composes modules under LLM-as-planner orchestration; ReTool \\\\\\\\cite{retool-2026} uses RL for implicit code-interpreter invocation. These methods learn \\\\\\\\emph{which tool} to use but do not analyze what signal drives routing. We generate labels via episode-level counterfactual analysis, revealing ${\\\\\\\\sim}90\\\\\\\\%$ is death avoidance.\\\\n   142\\\\t\\\\n   143\\\\t\\\\\\\\paragraph{Adaptive Computation.}\\\\n   144\\\\tCogRouter \\\\\\\\cite{cogrouter-2026} achieves 82.3\\\\\\\\% on ScienceWorld via cognitive depth routing; ARES \\\\\\\\cite{ares-2026} reduces token cost by 52.7\\\\\\\\% with per-step effort selection; Mixture-of-Recursions \\\\\\\\cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing. These route \\\\\\\\emph{how much} to reason; we route \\\\\\\\emph{which modality}. Our decomposition reveals death avoidance accounts for ${\\\\\\\\sim}90\\\\\\\\%$ of the performance gap.\\\\n   145\\\\t\\\\n   146\\\\t\\\\\\\\paragraph{World Model Routing.}\\\\n   147\\\\tITP \\\\\\\\cite{itp-2026} augments agents with world model lookahead; Dyna-Think \\\\\\\\cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost. Both route to \\\\\\\\emph{approximate} world models; our deterministic modality provides \\\\\\\\emph{exact} transitions, and counterfactual analysis reveals this exactness matters almost exclusively for death avoidance ($\\\\\\\\Delta_\\\\\\\\text{nd}$ is only 9.6\\\\\\\\% of the full gap).\\\\n   148\\\\t\\\\n   149\\\\t\\\\\\\\paragraph{Agent Frameworks.}\\\\n   150\\\\tReAct \\\\\\\\cite{react-2023} provides our internal-reasoning baseline; ScienceWorld \\\\\\\\cite{scienceworld-2022} is the evaluation environment. MTRouter \\\\\\\\cite{mtrouter-2026} routes between LLMs for cost optimization but targets model-level rather than modality-level selection. Our work asks \\\\\\\\emph{what} a router captures: the answer is dominated by catastrophic-failure prevention, suggesting future designs should prioritize safety-aware computation allocation.\\\\n   151\\\\t\\\\n   152\\\\t\\\\\\\\section{Conclusion}\\\\n   153\\\\t\\\\n   154\\\\tWe presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Across 245 ScienceWorld episodes, death avoidance accounts for 90.41\\\\\\\\% of routing signal ($\\\\\\\\Delta_\\\\\\\\text{full}$ = +29.60 vs.\\\\\\\\ $\\\\\\\\Delta_\\\\\\\\text{nd}$ = +2.84). This concentration is corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\\\\\% agreement with always-deterministic), and near-random trained router accuracy (58.1\\\\\\\\%). Future work should extend to step-level counterfactual labeling and evaluate generalization to environments with different failure modes.\\\\n   155\\\\t\\\\n   156\\\\t\\\\\\\\section*{Limitations}\\\\n   157\\\\t\\\\n   158\\\\tOur analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. Step-level labeling with denser rewards is a natural extension. The logit-to-generation gap in the implicit router warrants further investigation.\\\\n   159\\\\t\\\\n   160\\\\t\\\\\\\\bibliography{references}\\\\n   161\\\\t\\\\n   162\\\\t\\\\\\\\end{document}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.05}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\documentclass[11pt]{article}\\n     2\\t\\\\usepackage[review]{acl}\\n     3\\t\\\\usepackage{times}\\n     4\\t\\\\usepackage{latexsym}\\n     5\\t\\\\usepackage{graphicx}\\n     6\\t\\\\usepackage{booktabs}\\n     7\\t\\\\usepackage{amsmath}\\n     8\\t\\\\usepackage{url}\\n     9\\t\\n    10\\t\\\\title{Death Avoidance Dominates the Routing Signal in Modular LLM Agents}\\n    11\\t\\\\author{Anonymous ACL Submission}\\n    12\\t\\\\date{}\\n    13\\t\\n    14\\t\\\\begin{document}\\n    15\\t\\\\maketitle\\n    16\\t\\n    17\\t\\\\begin{abstract}\\n    18\\tModular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\\\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97\\\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for 90.41\\\\% of the routing signal (Death Avoidance Factor). Per-task death rate differentials correlate near-perfectly with routing benefit ($r$ = 0.9698, $p$ = 8.12$\\\\times$10$^{-7}$). The oracle router agrees with always-deterministic on 96.2\\\\% of decisions, and a trained router achieves only 58.1\\\\% balanced accuracy---near random. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\\n    19\\t\\\\end{abstract}\\n    20\\t\\n    21\\t\\\\section{Introduction}\\n    22\\t\\n    23\\tWhen a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\\\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated, or failing to model that metal conducts heat differently than glass---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\\n    24\\t\\n    25\\tExisting routing approaches \\\\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\\\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\\\\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\\\\S\\\\ref{sec:collection}). Keyword-based heuristics (\\\\S\\\\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\\\\texttt{pour}, \\\\texttt{move}, \\\\texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.\\n    26\\t\\n    27\\tWe propose \\\\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\\\S\\\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\\\Delta_{\\\\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\\\\Delta_{\\\\text{no\\\\_death}} = +2.84$---a Death Avoidance Factor (DAF; \\\\S\\\\ref{sec:daf}) of 90.41\\\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\\\times 10\\n\\n... [截断: 输出过长，省略 10980 字符] ...\\n\\n.8\\\\%, indicating seed-dependent decision boundaries with consistent weak discriminability. This pattern supports that the labels encode minimal routing structure beyond death avoidance.\\n   135\\t\\n   136\\tThese results yield two observations. First, counterfactual labels encode genuine routing patterns at the representation level---ruling out uninformative labels and pointing to the episode-to-step granularity mismatch as the bottleneck. Second, generation-level expression of these patterns remains an open challenge; step-level counterfactual labeling may be a productive direction.\\n   137\\t\\n   138\\t\\\\section{Related Work}\\n   139\\t\\n   140\\t\\\\paragraph{Tool-Use Learning.}\\n   141\\tToolformer \\\\cite{toolformer-2024} inserts API calls via self-supervised filtering; ART \\\\cite{art-2023} delegates tool selection to reasoning chains; Chameleon \\\\cite{chameleon-2024} composes modules under LLM-as-planner orchestration; ReTool \\\\cite{retool-2026} uses RL for implicit code-interpreter invocation. These methods learn \\\\emph{which tool} to use but do not analyze what signal drives routing. We generate labels via episode-level counterfactual analysis, revealing ${\\\\sim}90\\\\%$ is death avoidance.\\n   142\\t\\n   143\\t\\\\paragraph{Adaptive Computation.}\\n   144\\tCogRouter \\\\cite{cogrouter-2026} achieves 82.3\\\\% on ScienceWorld via cognitive depth routing; ARES \\\\cite{ares-2026} reduces token cost by 52.7\\\\% with per-step effort selection; Mixture-of-Recursions \\\\cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing. These route \\\\emph{how much} to reason; we route \\\\emph{which modality}. Our decomposition reveals death avoidance accounts for ${\\\\sim}90\\\\%$ of the performance gap.\\n   145\\t\\n   146\\t\\\\paragraph{World Model Routing.}\\n   147\\tITP \\\\cite{itp-2026} augments agents with world model lookahead; Dyna-Think \\\\cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost. Both route to \\\\emph{approximate} world models; our deterministic modality provides \\\\emph{exact} transitions, and counterfactual analysis reveals this exactness matters almost exclusively for death avoidance ($\\\\Delta_\\\\text{nd}$ is only 9.6\\\\% of the full gap).\\n   148\\t\\n   149\\t\\\\paragraph{Agent Frameworks.}\\n   150\\tReAct \\\\cite{react-2023} provides our internal-reasoning baseline; ScienceWorld \\\\cite{scienceworld-2022} is the evaluation environment. MTRouter \\\\cite{mtrouter-2026} routes between LLMs for cost optimization but targets model-level rather than modality-level selection. Our work asks \\\\emph{what} a router captures: the answer is dominated by catastrophic-failure prevention, suggesting future designs should prioritize safety-aware computation allocation.\\n   151\\t\\n   152\\t\\\\section{Conclusion}\\n   153\\t\\n   154\\tWe presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Across 245 ScienceWorld episodes, death avoidance accounts for 90.41\\\\% of routing signal ($\\\\Delta_\\\\text{full}$ = +29.60 vs.\\\\ $\\\\Delta_\\\\text{nd}$ = +2.84). This concentration is corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.2\\\\% agreement with always-deterministic), and near-random trained router accuracy (58.1\\\\%). Future work should extend to step-level counterfactual labeling and evaluate generalization to environments with different failure modes.\\n   155\\t\\n   156\\t\\\\section*{Limitations}\\n   157\\t\\n   158\\tOur analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. Step-level labeling with denser rewards is a natural extension. The logit-to-generation gap in the implicit router warrants further investigation.\\n   159\\t\\n   160\\t\\\\bibliography{references}\\n   161\\t\\n   162\\t\\\\end{document}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me analyze:

1. **"near-equivalent" does not exist anywhere** — the task premise is outdated/incorrect.

2. The experiments.tex line 26 says: "When internal reasoning does not cause death, it performs comparably to deterministic computation." — The word "comparably" downplays the non-death gap, while the actual data shows $\Delta_{\text{no\_death}} = +2.84$ (9.6% of full gap), which the experiments section earlier describes with specific numbers.

3. Looking at what might need consistency:
   - experiments.tex line 26: "performs comparably" — this could be seen as inconsistent with "small but non-negligible"
   - But the key text is in lines 20-26 where the gap collapses to $\Delta_{\text{no\_death}} = +2.84$ and then claims it performs comparably to deterministic computation.
   
   The task mentions "small but non-negligible" at line 19, but I'm not finding that exact phrase in the file — I need to search more carefully for where this language actually appears.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "fcd43bfd-4522-461a-aad6-fd146524fc14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ3fFfATSfcAQn86WcQn5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 30094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3944
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

_source line 34_

让我确认 experiments.tex 中是否真的有 "small but non-negligible"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "f1ac8830-12b4-4ab0-94e1-fb77ff00a0b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ3fFfATSfcAQn86WcQn5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 30094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3944
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

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MozvBCGoPdVEcSwiW5zyQ2`</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -n \"non-negligible\" /root/autodl-tmp/simgate-modular-routing/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "b6259eb7-8eba-4848-8f1e-fc5649e4fec7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ3fFfATSfcAQn86WcQn5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 30094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3944
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

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018qkCFHRioQQBYi9Bfo6nGh`</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -rn \"non-negligible\" /root/autodl-tmp/simgate-modular-routing/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "3a01c387-44ba-4c69-a77a-4f055206e332",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ3fFfATSfcAQn86WcQn5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 30094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3944
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

_source line 37 · 2026-05-14T12:50:35.919Z_

<details><summary>↩ Tool result · `toolu_01MozvBCGoPdVEcSwiW5zyQ2`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "a353f6ad-4a51-4948-a143-6e995e6dd822",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.77}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T12:50:36.857Z_

<details><summary>↩ Tool result · `toolu_018qkCFHRioQQBYi9Bfo6nGh`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.93}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "dcd82b44-3b0a-47b3-af0e-c61d9e9fe6cb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.93}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.93}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
"non-negligible" also doesn't exist in any tex file. The task's premise is entirely incorrect — both "near-equivalent" and "small but non-negligible" are not present in the current paper files.

Let me also check "comparably" since that's the closest existing wording to "near-equivalent".
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "7475dbf8-4565-43a6-8294-44195c52a50f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3sN7BLneevqE1khjRTSHA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 34038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 780
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

_source line 40_

任务前提与当前文件状态不符：

1. **"near-equivalent"** — 不存在于任何 tex 文件中
2. **"small but non-negligible"** — 也不存在于任何 tex 文件中

当前 experiments.tex 中对 non-death gap 的描述是：
- 第20行：`the gap collapses to $\Delta_{\text{no\_death}} = +2.84$`
- 第26行：`When internal reasoning does not cause death, it performs comparably to deterministic computation.`

Abstract（main.tex 第18行）完全没有描述 non-death gap，只说 "death avoidance accounts for 90.41% of the routing signal"。

**结论：无需修改。** "near-equivalent" 已不存在，abstract 与 experiments 之间不存在措辞冲突。experiments.tex 中 "performs comparably" 与 $\Delta_{\text{no\_death}} = +2.84$（9.6% of full gap）在语义上一致——gap 确实很小。

如果你希望将 experiments.tex 的 "performs comparably" 改为更精确的 "small but non-negligible" 表述，我可以执行，但这不是必须的同步操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "uuid": "e98d369d-9805-4648-a544-8148758af463",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3sN7BLneevqE1khjRTSHA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 34038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 780
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

### Task result

_source line 41_

任务前提与当前文件状态不符：

1. **"near-equivalent"** — 不存在于任何 tex 文件中
2. **"small but non-negligible"** — 也不存在于任何 tex 文件中

当前 experiments.tex 中对 non-death gap 的描述是：
- 第20行：`the gap collapses to $\Delta_{\text{no\_death}} = +2.84$`
- 第26行：`When internal reasoning does not cause death, it performs comparably to deterministic computation.`

Abstract（main.tex 第18行）完全没有描述 non-death gap，只说 "death avoidance accounts for 90.41% of the routing signal"。

**结论：无需修改。** "near-equivalent" 已不存在，abstract 与 experiments 之间不存在措辞冲突。experiments.tex 中 "performs comparably" 与 $\Delta_{\text{no\_death}} = +2.84$（9.6% of full gap）在语义上一致——gap 确实很小。

如果你希望将 experiments.tex 的 "performs comparably" 改为更精确的 "small but non-negligible" 表述，我可以执行，但这不是必须的同步操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 119697,
  "duration_api_ms": 113642,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "4e52142f-e2a4-4b01-ae57-a87aa26d82bb",
  "total_cost_usd": 0.38258825,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 22977,
    "cache_read_input_tokens": 258588,
    "output_tokens": 4315,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22977,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 428,
        "cache_read_input_tokens": 34038,
        "cache_creation_input_tokens": 780,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 780
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1673,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001748,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 4315,
      "cacheReadInputTokens": 258588,
      "cacheCreationInputTokens": 22977,
      "webSearchRequests": 0,
      "costUSD": 0.38084025000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "44a0410f-adfb-45e6-83e5-174bea670e0d"
}
```

</details>

---

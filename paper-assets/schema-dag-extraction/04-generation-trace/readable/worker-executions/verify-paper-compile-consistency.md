# verify paper compile consistency

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 96
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_verify_paper_compile_consistency_20260516T023830.log`
- **Structured JSON:** [`e42a46deac23bb6c3be3.json`](../../sessions/e4/e42a46deac23bb6c3be3.json)

## Before a recorded user message

96 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "9bae9c17-6e25-41c8-938f-97747a1702d8",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1778908800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "18d5c29e-afcc-44b1-bc0f-89c59ec454d8",
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task into three parts:
1. Compile the paper on the server
2. Cross-consistency check across .tex files
3. Provenance check and update

Let me start by doing several things in parallel:
- Compile the paper on the server
- Read the .tex files for consistency checking
- Read the provenance file

Let me first load the MCP tools I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "a3a0a166-9dc6-4299-82f9-6e970f2fd033",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dqpk1rPabDiLcy7GAPXXaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11918,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11918
      },
      "output_tokens": 25,
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

开始执行三项任务：编译验证、交叉一致性检查、Provenance 更新。先加载需要的工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "641d4af2-d817-4df4-b7a6-d2a270ddd86e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dqpk1rPabDiLcy7GAPXXaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11918,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11918
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MDDDiUYz1WRQcjDQNiF8C9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image",
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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "e6007323-bc81-419f-86f4-505474bd5849",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dqpk1rPabDiLcy7GAPXXaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11918,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11918
      },
      "output_tokens": 25,
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

_source line 7 · 2026-05-16T02:38:46.679Z_

<details><summary>↩ Tool result · `toolu_01MDDDiUYz1WRQcjDQNiF8C9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "95c50045-a3d3-4cb0-a743-a13098badd8f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me start the work in parallel:
1. Read the .tex files on the server for consistency checking
2. Read the provenance file
3. Start compiling the paper

Let me first check what .tex files exist and read them, and also start the compilation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "90b2768b-40b8-4ba5-b113-cdd8c6d98876",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwDTmWP96w8r4MoYrWLAm5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 23759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
      },
      "output_tokens": 17,
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

_source line 9_

并行启动：编译论文、读取 tex 文件、读取 provenance。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "ffab3464-e1f8-42a8-b0a3-381c4b1db982",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwDTmWP96w8r4MoYrWLAm5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 23759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01KQCcu5XKcU6Bq28zGMiWYj`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction/docs/paper && latexmk -pdf main.tex 2>&1 | tail -80",
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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "1ab5c0ba-63c7-463e-8a0f-6f05cc858e38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwDTmWP96w8r4MoYrWLAm5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 23759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016pCsVSSg3EuTh39sViSXpa`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls /root/schema-dag-extraction/docs/paper/*.tex",
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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "bdb04718-5184-4724-95cd-0f26855789a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwDTmWP96w8r4MoYrWLAm5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 23759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
      },
      "output_tokens": 17,
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

_source line 12 · 2026-05-16T02:38:54.732Z_

<details><summary>↩ Tool result · `toolu_01KQCcu5XKcU6Bq28zGMiWYj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/schema-dag-extraction/docs/paper && latexmk -pdf main.tex 2>&1 | tail -80'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: cd: /root/schema-dag-extraction/docs/paper: No such file or directory\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.19}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "0392ba78-dfd8-4f64-a0b1-b0be6882a350",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/schema-dag-extraction/docs/paper && latexmk -pdf main.tex 2>&1 | tail -80'\\\\n\\\\nExit code: 1\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: cd: /root/schema-dag-extraction/docs/paper: No such file or directory\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.19}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/schema-dag-extraction/docs/paper && latexmk -pdf main.tex 2>&1 | tail -80'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: cd: /root/schema-dag-extraction/docs/paper: No such file or directory\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.19}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0172Ba35ZxcUAvk7uUd9M8Jw`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_provenance.yaml",
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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "d184c288-f99c-40e3-86e4-e72042d707bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwDTmWP96w8r4MoYrWLAm5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 23759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
      },
      "output_tokens": 17,
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

_source line 14 · 2026-05-16T02:38:55.673Z_

<details><summary>↩ Tool result · `toolu_016pCsVSSg3EuTh39sViSXpa`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/schema-dag-extraction/docs/paper/*.tex': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.93}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "79c71447-ee57-4562-9669-141131ffb2be",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/schema-dag-extraction/docs/paper/*.tex': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.93}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/schema-dag-extraction/docs/paper/*.tex': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.93}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T02:38:55.684Z_

<details><summary>↩ Tool result · `toolu_0172Ba35ZxcUAvk7uUd9M8Jw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml\", \"content\": \"paper:\\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\\\\\in Training-Free\\n    LLM Information Extraction?\\n  version: 3\\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\\n  source: manual mapping from registry + paper_framing.md\\nclaims:\\n- text: 'Training-free LLM information extraction---prompting models with target schemas\\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\\n    drops from 0.72 to 0.42 with 64 candidate '\\n  type: quantitative\\n  location:\\n    section: abstract\\n    context: result_statement\\n  id: C001\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall count_1=0.720, count_64=0.418\\n    tier: 1\\n  deprecated: false\\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\\n    overlap between types and design two complementary experimental paradigms: count\\n    cu'\\n  type: methodological\\n  location:\\n    section: abstract\\n    context: finding_statement\\n  id: C002\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\\n    tier: 1\\n  deprecated: false\\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\\n    recall as candidate types increase, and'\\n  type: quantitative\\n  location:\\n    section: conclusion\\n    context: result_statement\\n  id: C003\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: 'Channel 1: recall 0.72->0.418'\\n    tier: 1\\n  - exp_id: exp007_error_taxonomy\\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub vs BCS rho=0.954\\n    tier: 1\\n  deprecated: false\\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\\n    capability, native structured JSON output support, and the practical advantage\\n    that the FP8-quantized 32B model fits on a\\n  type: quantitative\\n  location:\\n    section: experimental_setup\\n    context: result_statement\\n  id: C004\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\\n    tier: 2\\n  deprecated: false\\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\\n  type: methodological\\n  location:\\n    section: experimental_setup\\n    context: finding_statement\\n  id: C005\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\\n    tier: 1\\n  deprecated: false\\n- text: Channel~1\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: bold\\n  id: C006\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall 0.72->0.418 monotonic decline\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: accuracy 0.857->0.504 monotonic decline\\n    tier: 1\\n  deprecated: false\\n- text: Channel~2\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: bold\\n  id: C007\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: BCS-controlled delta=-31.2pp\\n    tier: 1\\n  deprecated: false\\n- text: Training-free LLM information extraction---prompting a large language model\\n    with a target schema and asking it to extract structured information without any\\n    task-specific fine-tuning---enables rapid d\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C008\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: background framing, supported by all experiments\\n    tier: 3\\n  deprecated: false\\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\\n    similarity between type pairs corre\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C009\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CIs exclude zero for both\\n    tier: 1\\n  deprecated: false\\n- text: Third, confusability effects amplify with schema scale. In BCS-controlled\\n    FewRel experiments, switching from low-confusability to high-confusability type\\n    batches reduces accuracy by 9.1 percentage poi\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C010\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel BCS effect delta=-9.1pp\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x\\n    tier: 1\\n  deprecated: false\\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\\n    between mean BCS and per-type er\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C011\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\\n    tier: 1\\n  deprecated: false\\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\\n    into different batches, yet every decomp\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C012\\n  evidence:\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\\n    tier: 1\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: v1 sdgd_zero F1=0.251, also below baseline\\n    tier: 1\\n  deprecated: false\\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\\n    bootstrap confidence intervals on three datasets, establishing that confusability\\n    effects amplify $3.4$ as schema size gro\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C013\\n  evidence:\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 3.4x amplification (80-rel vs 16-rel)\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: FewRel count_8 delta CI [17.7, 42.7]\\n    tier: 1\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\\n    tier: 1\\n  deprecated: false\\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\\n    semantic overlap between types using embedding cosine similarity, and its batch\\n  type: methodological\\n  location:\\n    section: introduction\\n    context: finding_statement\\n  id: C014\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: SCS validated as proxy for empirical confusion\\n    tier: 2\\n  deprecated: false\\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\\n    embedding models, while identifying a centrality confound that invalidates per-type\\n    aggrega\\n  type: methodological\\n  location:\\n    section: introduction\\n    context: finding_statement\\n  id: C015\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise r=0.112\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN centrality confound (per-type positive)\\n    tier: 1\\n  deprecated: false\\n- text: 95\\\\\\\\% CI\\n  type: quantitative\\n  location:\\n    section: results\\n    context: bold\\n  id: C016\\n  evidence:\\n  - exp_id: bootstrap_ci_analysis\\n    metric: 7 CIs all exclude null\\n    tier: 1\\n  deprecated: false\\n- text: Recall declines monotonically from 0.72 at count${\\\\\\\\,=\\\\\\\\,1$ to 0.42 at count${\\\\\\\\,=\\\\\\\\,64$,\\n    a 42\\\\\\\\% relative drop. Precision moves in the opposite direction, rising from\\n    0.11 to 0.52, reflecting a shift from\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C017\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall 0.72->0.418, precision 0.105->0.52\\n    tier: 1\\n  deprecated: false\\n- text: Accuracy drops monotonically from 85.7\\\\\\\\% at count${\\\\\\\\,=\\\\\\\\,1$ to 50.4\\\\\\\\% at\\n    count${\\\\\\\\,=\\\\\\\\,80$, a near-halving when the model must discriminate among all 80\\n    relation types simultaneously.\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C018\\n  evidence:\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\\n    tier: 1\\n  deprecated: false\\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\\\\\,=\\\\\\\\,1$\\n    to 0.247 at count${\\\\\\\\,=\\\\\\\\,44$. This reversal arises from three properties of the\\n    MAVEN setup: (i)~trigger-level relaxed'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C019\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\\n    tier: 1\\n  deprecated: false\\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\\\\\%$, meaning pairwise confusability\\n    explains roughly 1.5\\\\\\\\% of the variance in type confusion. Other factors---entity\\n    frequency, prompt position effects lost-'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C020\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN pairwise r=0.129, r2=1.66%\\n    tier: 1\\n  deprecated: false\\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\\n    and MiniLM yields $ = 0.144$ ($p\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C021\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\\n    tier: 1\\n  deprecated: false\\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\\n    types; high-BCS batches contain maximally similar types. The confusability gap\\n    widens from 9.1\\\\\\\\,pp at 16 relations to 31.2\\\\\\\\\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C022\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\\n    tier: 1\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\\n    tier: 1\\n  deprecated: false\\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\\n    this gap to 31.2\\\\\\\\,pp (95\\\\\\\\% CI: [17.7, 42.'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C023\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel delta=-9.1pp\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel delta=-31.2pp\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\\n    tier: 1\\n  deprecated: false\\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C024\\n  evidence:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\\n      flat)\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\\n    tier: 1\\n  deprecated: false\\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\\n    with BCS in both tasks: NER IntraSub rises from 0\\\\\\\\% (solo) to 49.4\\\\\\\\% (high BCS)\\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C025\\n  evidence:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub rho=1.0 (p<0.001)\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub rho=0.954 (p<1e-6)\\n    tier: 1\\n  deprecated: false\\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\\\\\,=\\\\\\\\,6$, high-BCS\\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\\n    versus $1.7$ under random batching. At\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C026\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\\n    tier: 1\\n  deprecated: false\\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C027\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\\n    tier: 1\\n  deprecated: false\\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\\n    the values in Table~tab:pairwise. The problem'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C028\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CI [0.104, 0.156]\\n    tier: 1\\n  deprecated: false\\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\\n    0.02$, $n = 63$), in the expected negative direc\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C029\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\\n    tier: 1\\n  deprecated: false\\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\\n    F1\\\\\\\\,=\\\\\\\\,0.445 (P\\\\\\\\,=\\\\\\\\,0.563, R\\\\\\\\,=\\\\\\\\,0.368).  SDGD obtains F1\\\\\\\\,=\\\\\\\\,0.251 (P\\\\\\\\,=\\\\\\\\,0.210,\\n    R\\\\\\\\,=\\\\\\\\,0.314), a 44\\\\\\\\% relative drop.  Rand\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C030\\n  evidence:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\\n    tier: 1\\n  deprecated: false\\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\\n    versus 0.563).  The mechanism is straightfo'\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C031\\n  evidence:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\\n    tier: 1\\n  deprecated: false\\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\\n    retains only the highest-scoring candidate fo\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C032\\n  evidence:\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\\n    tier: 1\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\ntables:\\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\\n    model used for SCS/BCS computation.\\n  label: tab:datasets\\n  location:\\n    section: experimental_setup\\n  cells:\\n  - exp_id: exp001_count_baseline\\n    metric: Few-NERD 66 types\\n  - exp_id: exp-004\\n    metric: MAVEN 168 event types, 77993 train mentions\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: FewRel 80 relations\\n  id: T001\\n  deprecated: false\\n- caption: Pairwise SCS--confusion correlation.\\n  label: tab:pairwise\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\\n  - exp_id: bootstrap_ci_analysis\\n    metric: bootstrap CIs for both\\n  id: T002\\n  deprecated: false\\n- caption: BCS-controlled FewRel accuracy.\\n  label: tab:bcs_controlled\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp_fewrel_formal\\n    metric: '16-rel: delta=-9.1pp'\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\\n  - exp_id: bootstrap_ci_analysis\\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\\n  id: T003\\n  deprecated: false\\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\\n  label: tab:error_taxonomy\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\\n  id: T004\\n  deprecated: false\\n- caption: Few-NERD extraction under decomposition modes.\\n  label: tab:sdgd_results\\n  location:\\n    section: sdgd_negative\\n  cells:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\\n      F1=0.292'\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\\n  id: T005\\n  deprecated: false\\nfigures:\\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\\n  label: fig:count_curves\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp001_count_baseline\\n    metric: 'Panel (a): recall 0.72->0.418'\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 'Panel (b): accuracy 0.857->0.504'\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: 'Panel (b): count_40=0.588'\\n  id: F001\\n  deprecated: false\\n- caption: BCS effect scaling with pool size\\n  label: fig:bcs_scaling\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel delta=9.1pp\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: 40-rel delta=33.3pp (80-pool subset)\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel delta=31.2pp\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: LLaMA 80-rel delta=27.1pp\\n  id: F002\\n  deprecated: false\\n- caption: Error taxonomy by BCS bin\\n  label: fig:error_taxonomy\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp007_error_taxonomy\\n    metric: 'NER: IntraSub 0%->49.4%'\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: 'RE: IntraSub 0%->32.3%'\\n  id: F003\\n  deprecated: false\\n_completeness:\\n  coverage: 32/42\\n  claims: 39\\n  tables: 5\\n  figures: 3\\n  tier_counts:\\n    tier1: 0\\n    tier2: 32\\n    tier3: 10\\n    tierX: 0\\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\\n\", \"total_chars\": 21248, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "b7ced28c-fbea-4c95-b48e-8aa1c99deca0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml\\\", \\\"content\\\": \\\"paper:\\\\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\\\\\\\\\\\\\in Training-Free\\\\n    LLM Information Extraction?\\\\n  version: 3\\\\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\\\\n  source: manual mapping from registry + paper_framing.md\\\\nclaims:\\\\n- text: 'Training-free LLM information extraction---prompting models with target schemas\\\\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\\\\n    drops from 0.72 to 0.42 with 64 candidate '\\\\n  type: quantitative\\\\n  location:\\\\n    section: abstract\\\\n    context: result_statement\\\\n  id: C001\\\\n  evidence:\\\\n  - exp_id: exp001_count_baseline\\\\n    metric: recall count_1=0.720, count_64=0.418\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\\\\n    overlap between types and design two complementary experimental paradigms: count\\\\n    cu'\\\\n  type: methodological\\\\n  location:\\\\n    section: abstract\\\\n    context: finding_statement\\\\n  id: C002\\\\n  evidence:\\\\n  - exp_id: exp015_scs_validation\\\\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\\\\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\\\\n    recall as candidate types increase, and'\\\\n  type: quantitative\\\\n  location:\\\\n    section: conclusion\\\\n    context: result_statement\\\\n  id: C003\\\\n  evidence:\\\\n  - exp_id: exp001_count_baseline\\\\n    metric: 'Channel 1: recall 0.72->0.418'\\\\n    tier: 1\\\\n  - exp_id: exp007_error_taxonomy\\\\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\\\\n    tier: 1\\\\n  - exp_id: exp016_fewrel_error_taxonomy\\\\n    metric: RE IntraSub vs BCS rho=0.954\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\\\\n    capability, native structured JSON output support, and the practical advantage\\\\n    that the FP8-quantized 32B model fits on a\\\\n  type: quantitative\\\\n  location:\\\\n    section: experimental_setup\\\\n    context: result_statement\\\\n  id: C004\\\\n  evidence:\\\\n  - exp_id: exp001_count_baseline\\\\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\\\\n    tier: 2\\\\n  deprecated: false\\\\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\\\\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\\\\n  type: methodological\\\\n  location:\\\\n    section: experimental_setup\\\\n    context: finding_statement\\\\n  id: C005\\\\n  evidence:\\\\n  - exp_id: exp015_scs_validation\\\\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Channel~1\\\\n  type: quantitative\\\\n  location:\\\\n    section: introduction\\\\n    context: bold\\\\n  id: C006\\\\n  evidence:\\\\n  - exp_id: exp001_count_baseline\\\\n    metric: recall 0.72->0.418 monotonic decline\\\\n    tier: 1\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: accuracy 0.857->0.504 monotonic decline\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Channel~2\\\\n  type: quantitative\\\\n  location:\\\\n    section: introduction\\\\n    context: bold\\\\n  id: C007\\\\n  evidence:\\\\n  - exp_id: exp002_confusability_controlled\\\\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\\\\n    tier: 1\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: BCS-controlled delta=-31.2pp\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Training-free LLM information extraction---prompting a large language model\\\\n    with a target schema and asking it to extract structured information without any\\\\n    task-specific fine-tuning---enables rapid d\\\\n  type: quantitative\\\\n  location:\\\\n    section: introduction\\\\n    context: result_statement\\\\n  id: C008\\\\n  evidence:\\\\n  - exp_id: exp001_count_baseline\\\\n    metric: background framing, supported by all experiments\\\\n    tier: 3\\\\n  deprecated: false\\\\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\\\\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\\\\n    similarity between type pairs corre\\\\n  type: quantitative\\\\n  location:\\\\n    section: introduction\\\\n    context: result_statement\\\\n  id: C009\\\\n  evidence:\\\\n  - exp_id: exp002_confusability_controlled\\\\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\\\\n    tier: 1\\\\n  - exp_id: exp004_maven_bcs\\\\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\\\\n    tier: 1\\\\n  - exp_id: bootstrap_ci_analysis\\\\n    metric: CIs exclude zero for both\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Third, confusability effects amplify with schema scale. In BCS-controlled\\\\n    FewRel experiments, switching from low-confusability to high-confusability type\\\\n    batches reduces accuracy by 9.1 percentage poi\\\\n  type: quantitative\\\\n  location:\\\\n    section: introduction\\\\n    context: result_statement\\\\n  id: C010\\\\n  evidence:\\\\n  - exp_id: exp_fewrel_formal\\\\n    metric: 16-rel BCS effect delta=-9.1pp\\\\n    tier: 1\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\\\\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\\\\n    between mean BCS and per-type er\\\\n  type: quantitative\\\\n  location:\\\\n    section: introduction\\\\n    context: result_statement\\\\n  id: C011\\\\n  evidence:\\\\n  - exp_id: exp004_maven_bcs\\\\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\\\\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\\\\n    into different batches, yet every decomp\\\\n  type: quantitative\\\\n  location:\\\\n    section: introduction\\\\n    context: result_statement\\\\n  id: C012\\\\n  evidence:\\\\n  - exp_id: exp008_sdgd_v2_fewnerd\\\\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\\\\n    tier: 1\\\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\\\n    metric: v1 sdgd_zero F1=0.251, also below baseline\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\\\\n    bootstrap confidence intervals on three datasets, establishing that confusability\\\\n    effects amplify $3.4$ as schema size gro\\\\n  type: quantitative\\\\n  location:\\\\n    section: introduction\\\\n    context: result_statement\\\\n  id: C013\\\\n  evidence:\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: 3.4x amplification (80-rel vs 16-rel)\\\\n    tier: 1\\\\n  - exp_id: bootstrap_ci_analysis\\\\n    metric: FewRel count_8 delta CI [17.7, 42.7]\\\\n    tier: 1\\\\n  - exp_id: exp012_llama_fewrel_ch2\\\\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\\\\n    semantic overlap between types using embedding cosine similarity, and its batch\\\\n  type: methodological\\\\n  location:\\\\n    section: introduction\\\\n    context: finding_statement\\\\n  id: C014\\\\n  evidence:\\\\n  - exp_id: exp015_scs_validation\\\\n    metric: SCS validated as proxy for empirical confusion\\\\n    tier: 2\\\\n  deprecated: false\\\\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\\\\n    embedding models, while identifying a centrality confound that invalidates per-type\\\\n    aggrega\\\\n  type: methodological\\\\n  location:\\\\n    section: introduction\\\\n    context: finding_statement\\\\n  id: C015\\\\n  evidence:\\\\n  - exp_id: exp002_confusability_controlled\\\\n    metric: Few-NERD pairwise r=0.112\\\\n    tier: 1\\\\n  - exp_id: exp004_maven_bcs\\\\n    metric: MAVEN centrality confound (per-type positive)\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 95\\\\\\\\\\\\\\\\% CI\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: bold\\\\n  id: C016\\\\n  evidence:\\\\n  - exp_id: bootstrap_ci_analysis\\\\n    metric: 7 CIs all exclude null\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Recall declines monotonically from 0.72 at count${\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,1$ to 0.42 at count${\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,64$,\\\\n    a 42\\\\\\\\\\\\\\\\% relative drop. Precision moves in the opposite direction, rising from\\\\n    0.11 to 0.52, reflecting a shift from\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C017\\\\n  evidence:\\\\n  - exp_id: exp001_count_baseline\\\\n    metric: recall 0.72->0.418, precision 0.105->0.52\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Accuracy drops monotonically from 85.7\\\\\\\\\\\\\\\\% at count${\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,1$ to 50.4\\\\\\\\\\\\\\\\% at\\\\n    count${\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,80$, a near-halving when the model must discriminate among all 80\\\\n    relation types simultaneously.\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C018\\\\n  evidence:\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,1$\\\\n    to 0.247 at count${\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,44$. This reversal arises from three properties of the\\\\n    MAVEN setup: (i)~trigger-level relaxed'\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C019\\\\n  evidence:\\\\n  - exp_id: exp004_maven_bcs\\\\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\\\\\\\\\\\\\%$, meaning pairwise confusability\\\\n    explains roughly 1.5\\\\\\\\\\\\\\\\% of the variance in type confusion. Other factors---entity\\\\n    frequency, prompt position effects lost-'\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C020\\\\n  evidence:\\\\n  - exp_id: exp002_confusability_controlled\\\\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\\\\n    tier: 1\\\\n  - exp_id: exp004_maven_bcs\\\\n    metric: MAVEN pairwise r=0.129, r2=1.66%\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\\\\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\\\\n    and MiniLM yields $ = 0.144$ ($p\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C021\\\\n  evidence:\\\\n  - exp_id: exp015_scs_validation\\\\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\\\\n    types; high-BCS batches contain maximally similar types. The confusability gap\\\\n    widens from 9.1\\\\\\\\\\\\\\\\,pp at 16 relations to 31.2\\\\\\\\\\\\\\\\\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C022\\\\n  evidence:\\\\n  - exp_id: exp_fewrel_formal\\\\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\\\\n    tier: 1\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\\\\n    tier: 1\\\\n  - exp_id: exp_fewrel_40rel_r4\\\\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\\\\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\\\\n    this gap to 31.2\\\\\\\\\\\\\\\\,pp (95\\\\\\\\\\\\\\\\% CI: [17.7, 42.'\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C023\\\\n  evidence:\\\\n  - exp_id: exp_fewrel_formal\\\\n    metric: 16-rel delta=-9.1pp\\\\n    tier: 1\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: 80-rel delta=-31.2pp\\\\n    tier: 1\\\\n  - exp_id: bootstrap_ci_analysis\\\\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\\\\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\\\\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C024\\\\n  evidence:\\\\n  - exp_id: exp007_error_taxonomy\\\\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\\\\n      flat)\\\\n    tier: 1\\\\n  - exp_id: exp016_fewrel_error_taxonomy\\\\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\\\\n    with BCS in both tasks: NER IntraSub rises from 0\\\\\\\\\\\\\\\\% (solo) to 49.4\\\\\\\\\\\\\\\\% (high BCS)\\\\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C025\\\\n  evidence:\\\\n  - exp_id: exp007_error_taxonomy\\\\n    metric: NER IntraSub rho=1.0 (p<0.001)\\\\n    tier: 1\\\\n  - exp_id: exp016_fewrel_error_taxonomy\\\\n    metric: RE IntraSub rho=0.954 (p<1e-6)\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,6$, high-BCS\\\\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\\\\n    versus $1.7$ under random batching. At\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C026\\\\n  evidence:\\\\n  - exp_id: exp002_confusability_controlled\\\\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\\\\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\\\\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C027\\\\n  evidence:\\\\n  - exp_id: exp004_maven_bcs\\\\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\\\\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\\\\n    the values in Table~tab:pairwise. The problem'\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C028\\\\n  evidence:\\\\n  - exp_id: exp004_maven_bcs\\\\n    metric: MAVEN MiniLM pairwise r=0.129\\\\n    tier: 1\\\\n  - exp_id: bootstrap_ci_analysis\\\\n    metric: CI [0.104, 0.156]\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\\\\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\\\\n    0.02$, $n = 63$), in the expected negative direc\\\\n  type: quantitative\\\\n  location:\\\\n    section: results\\\\n    context: result_statement\\\\n  id: C029\\\\n  evidence:\\\\n  - exp_id: exp002_confusability_controlled\\\\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\\\\n    F1\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,0.445 (P\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,0.563, R\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,0.368).  SDGD obtains F1\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,0.251 (P\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,0.210,\\\\n    R\\\\\\\\\\\\\\\\,=\\\\\\\\\\\\\\\\,0.314), a 44\\\\\\\\\\\\\\\\% relative drop.  Rand\\\\n  type: quantitative\\\\n  location:\\\\n    section: sdgd_negative\\\\n    context: result_statement\\\\n  id: C030\\\\n  evidence:\\\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\\\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\\\\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\\\\n    versus 0.563).  The mechanism is straightfo'\\\\n  type: quantitative\\\\n  location:\\\\n    section: sdgd_negative\\\\n    context: result_statement\\\\n  id: C031\\\\n  evidence:\\\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\\\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\\\\n    tier: 1\\\\n  deprecated: false\\\\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\\\\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\\\\n    retains only the highest-scoring candidate fo\\\\n  type: quantitative\\\\n  location:\\\\n    section: sdgd_negative\\\\n    context: result_statement\\\\n  id: C032\\\\n  evidence:\\\\n  - exp_id: exp008_sdgd_v2_fewnerd\\\\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\\\\n    tier: 1\\\\n  deprecated: false\\\\n- id: C033\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C034\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C035\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C036\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C037\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C038\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C039\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\ntables:\\\\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\\\\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\\\\n    model used for SCS/BCS computation.\\\\n  label: tab:datasets\\\\n  location:\\\\n    section: experimental_setup\\\\n  cells:\\\\n  - exp_id: exp001_count_baseline\\\\n    metric: Few-NERD 66 types\\\\n  - exp_id: exp-004\\\\n    metric: MAVEN 168 event types, 77993 train mentions\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: FewRel 80 relations\\\\n  id: T001\\\\n  deprecated: false\\\\n- caption: Pairwise SCS--confusion correlation.\\\\n  label: tab:pairwise\\\\n  location:\\\\n    section: results\\\\n  cells:\\\\n  - exp_id: exp002_confusability_controlled\\\\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\\\\n  - exp_id: exp004_maven_bcs\\\\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\\\\n  - exp_id: bootstrap_ci_analysis\\\\n    metric: bootstrap CIs for both\\\\n  id: T002\\\\n  deprecated: false\\\\n- caption: BCS-controlled FewRel accuracy.\\\\n  label: tab:bcs_controlled\\\\n  location:\\\\n    section: results\\\\n  cells:\\\\n  - exp_id: exp_fewrel_formal\\\\n    metric: '16-rel: delta=-9.1pp'\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\\\\n  - exp_id: exp_fewrel_40rel_r4\\\\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\\\\n  - exp_id: exp012_llama_fewrel_ch2\\\\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\\\\n  - exp_id: bootstrap_ci_analysis\\\\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\\\\n  id: T003\\\\n  deprecated: false\\\\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\\\\n  label: tab:error_taxonomy\\\\n  location:\\\\n    section: results\\\\n  cells:\\\\n  - exp_id: exp007_error_taxonomy\\\\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\\\\n  - exp_id: exp016_fewrel_error_taxonomy\\\\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\\\\n  id: T004\\\\n  deprecated: false\\\\n- caption: Few-NERD extraction under decomposition modes.\\\\n  label: tab:sdgd_results\\\\n  location:\\\\n    section: sdgd_negative\\\\n  cells:\\\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\\\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\\\\n      F1=0.292'\\\\n  - exp_id: exp008_sdgd_v2_fewnerd\\\\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\\\\n  id: T005\\\\n  deprecated: false\\\\nfigures:\\\\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\\\\n  label: fig:count_curves\\\\n  location:\\\\n    section: results\\\\n  cells:\\\\n  - exp_id: exp001_count_baseline\\\\n    metric: 'Panel (a): recall 0.72->0.418'\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: 'Panel (b): accuracy 0.857->0.504'\\\\n  - exp_id: exp_fewrel_40rel_r4\\\\n    metric: 'Panel (b): count_40=0.588'\\\\n  id: F001\\\\n  deprecated: false\\\\n- caption: BCS effect scaling with pool size\\\\n  label: fig:bcs_scaling\\\\n  location:\\\\n    section: results\\\\n  cells:\\\\n  - exp_id: exp_fewrel_formal\\\\n    metric: 16-rel delta=9.1pp\\\\n  - exp_id: exp_fewrel_40rel_r4\\\\n    metric: 40-rel delta=33.3pp (80-pool subset)\\\\n  - exp_id: exp_fewrel_formal_80rel\\\\n    metric: 80-rel delta=31.2pp\\\\n  - exp_id: exp012_llama_fewrel_ch2\\\\n    metric: LLaMA 80-rel delta=27.1pp\\\\n  id: F002\\\\n  deprecated: false\\\\n- caption: Error taxonomy by BCS bin\\\\n  label: fig:error_taxonomy\\\\n  location:\\\\n    section: results\\\\n  cells:\\\\n  - exp_id: exp007_error_taxonomy\\\\n    metric: 'NER: IntraSub 0%->49.4%'\\\\n  - exp_id: exp016_fewrel_error_taxonomy\\\\n    metric: 'RE: IntraSub 0%->32.3%'\\\\n  id: F003\\\\n  deprecated: false\\\\n_completeness:\\\\n  coverage: 32/42\\\\n  claims: 39\\\\n  tables: 5\\\\n  figures: 3\\\\n  tier_counts:\\\\n    tier1: 0\\\\n    tier2: 32\\\\n    tier3: 10\\\\n    tierX: 0\\\\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\\\\n\\\", \\\"total_chars\\\": 21248, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml\", \"content\": \"paper:\\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\\\\\in Training-Free\\n    LLM Information Extraction?\\n  version: 3\\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\\n  source: manual mapping from registry + paper_framing.md\\nclaims:\\n- text: 'Training-free LLM information extraction---prompting models with target schemas\\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\\n    drops from 0.72 to 0.42 with 64 candidate '\\n  type: quantitative\\n  location:\\n    section: abstract\\n    context: result_statement\\n  id: C001\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall count_1=0.720, count_64=0.418\\n    tier: 1\\n  deprecated: false\\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\\n    overlap between types and design two complementary experimental paradigms: count\\n    cu'\\n  type: methodological\\n  location:\\n    section: abstract\\n    context: finding_statement\\n  id: C002\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\\n    tier: 1\\n  deprecated: false\\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\\n    recall as candidate types increase, and'\\n  type: quantitative\\n  location:\\n    section: conclusion\\n    context: result_statement\\n  id: C003\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: 'Channel 1: recall 0.72->0.418'\\n    tier: 1\\n  - exp_id: exp007_error_taxonomy\\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub vs BCS rho=0.954\\n    tier: 1\\n  deprecated: false\\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\\n    capability, native structured JSON output support, and the practical advantage\\n    that the FP8-quantized 32B model fits on a\\n  type: quantitative\\n  location:\\n    section: experimental_setup\\n    context: result_statement\\n  id: C004\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\\n    tier: 2\\n  deprecated: false\\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\\n  type: methodological\\n  location:\\n    section: experimental_setup\\n    context: finding_statement\\n  id: C005\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\\n    tier: 1\\n  deprecated: false\\n- text: Channel~1\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: bold\\n  id: C006\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall 0.72->0.418 monotonic decline\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: accuracy 0.857->0.504 monotonic decline\\n    tier: 1\\n  deprecated: false\\n- text: Channel~2\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: bold\\n  id: C007\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: BCS-controlled delta=-31.2pp\\n    tier: 1\\n  deprecated: false\\n- text: Training-free LLM information extraction---prompting a large language model\\n    with a target schema and asking it to extract structured information without any\\n    task-specific fine-tuning---enables rapid d\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C008\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: background framing, supported by all experiments\\n    tier: 3\\n  deprecated: false\\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\\n    similarity between type pairs corre\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C009\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CIs exclude zero for both\\n    tier: 1\\n  deprecated: false\\n- text: Third, confusability effects amplify with schema scale. In BCS-controlled\\n    FewRel experiments, switching from low-confusability to high-confusability type\\n    batches reduces accuracy by 9.1 percentage poi\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C010\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel BCS effect delta=-9.1pp\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x\\n    tier: 1\\n  deprecated: false\\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\\n    between mean BCS and per-type er\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C011\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\\n    tier: 1\\n  deprecated: false\\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\\n    into different batches, yet every decomp\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C012\\n  evidence:\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\\n    tier: 1\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: v1 sdgd_zero F1=0.251, also below baseline\\n    tier: 1\\n  deprecated: false\\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\\n    bootstrap confidence intervals on three datasets, establishing that confusability\\n    effects amplify $3.4$ as schema size gro\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C013\\n  evidence:\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 3.4x amplification (80-rel vs 16-rel)\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: FewRel count_8 delta CI [17.7, 42.7]\\n    tier: 1\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\\n    tier: 1\\n  deprecated: false\\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\\n    semantic overlap between types using embedding cosine similarity, and its batch\\n  type: methodological\\n  location:\\n    section: introduction\\n    context: finding_statement\\n  id: C014\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: SCS validated as proxy for empirical confusion\\n    tier: 2\\n  deprecated: false\\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\\n    embedding models, while identifying a centrality confound that invalidates per-type\\n    aggrega\\n  type: methodological\\n  location:\\n    section: introduction\\n    context: finding_statement\\n  id: C015\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise r=0.112\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN centrality confound (per-type positive)\\n    tier: 1\\n  deprecated: false\\n- text: 95\\\\\\\\% CI\\n  type: quantitative\\n  location:\\n    section: results\\n    context: bold\\n  id: C016\\n  evidence:\\n  - exp_id: bootstrap_ci_analysis\\n    metric: 7 CIs all exclude null\\n    tier: 1\\n  deprecated: false\\n- text: Recall declines monotonically from 0.72 at count${\\\\\\\\,=\\\\\\\\,1$ to 0.42 at count${\\\\\\\\,=\\\\\\\\,64$,\\n    a 42\\\\\\\\% relative drop. Precision moves in the opposite direction, rising from\\n    0.11 to 0.52, reflecting a shift from\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C017\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall 0.72->0.418, precision 0.105->0.52\\n    tier: 1\\n  deprecated: false\\n- text: Accuracy drops monotonically from 85.7\\\\\\\\% at count${\\\\\\\\,=\\\\\\\\,1$ to 50.4\\\\\\\\% at\\n    count${\\\\\\\\,=\\\\\\\\,80$, a near-halving when the model must discriminate among all 80\\n    relation types simultaneously.\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C018\\n  evidence:\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\\n    tier: 1\\n  deprecated: false\\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\\\\\,=\\\\\\\\,1$\\n    to 0.247 at count${\\\\\\\\,=\\\\\\\\,44$. This reversal arises from three properties of the\\n    MAVEN setup: (i)~trigger-level relaxed'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C019\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\\n    tier: 1\\n  deprecated: false\\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\\\\\%$, meaning pairwise confusability\\n    explains roughly 1.5\\\\\\\\% of the variance in type confusion. Other factors---entity\\n    frequency, prompt position effects lost-'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C020\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN pairwise r=0.129, r2=1.66%\\n    tier: 1\\n  deprecated: false\\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\\n    and MiniLM yields $ = 0.144$ ($p\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C021\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\\n    tier: 1\\n  deprecated: false\\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\\n    types; high-BCS batches contain maximally similar types. The confusability gap\\n    widens from 9.1\\\\\\\\,pp at 16 relations to 31.2\\\\\\\\\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C022\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\\n    tier: 1\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\\n    tier: 1\\n  deprecated: false\\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\\n    this gap to 31.2\\\\\\\\,pp (95\\\\\\\\% CI: [17.7, 42.'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C023\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel delta=-9.1pp\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel delta=-31.2pp\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\\n    tier: 1\\n  deprecated: false\\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C024\\n  evidence:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\\n      flat)\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\\n    tier: 1\\n  deprecated: false\\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\\n    with BCS in both tasks: NER IntraSub rises from 0\\\\\\\\% (solo) to 49.4\\\\\\\\% (high BCS)\\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C025\\n  evidence:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub rho=1.0 (p<0.001)\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub rho=0.954 (p<1e-6)\\n    tier: 1\\n  deprecated: false\\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\\\\\,=\\\\\\\\,6$, high-BCS\\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\\n    versus $1.7$ under random batching. At\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C026\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\\n    tier: 1\\n  deprecated: false\\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C027\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\\n    tier: 1\\n  deprecated: false\\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\\n    the values in Table~tab:pairwise. The problem'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C028\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CI [0.104, 0.156]\\n    tier: 1\\n  deprecated: false\\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\\n    0.02$, $n = 63$), in the expected negative direc\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C029\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\\n    tier: 1\\n  deprecated: false\\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\\n    F1\\\\\\\\,=\\\\\\\\,0.445 (P\\\\\\\\,=\\\\\\\\,0.563, R\\\\\\\\,=\\\\\\\\,0.368).  SDGD obtains F1\\\\\\\\,=\\\\\\\\,0.251 (P\\\\\\\\,=\\\\\\\\,0.210,\\n    R\\\\\\\\,=\\\\\\\\,0.314), a 44\\\\\\\\% relative drop.  Rand\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C030\\n  evidence:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\\n    tier: 1\\n  deprecated: false\\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\\n    versus 0.563).  The mechanism is straightfo'\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C031\\n  evidence:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\\n    tier: 1\\n  deprecated: false\\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\\n    retains only the highest-scoring candidate fo\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C032\\n  evidence:\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\\n    tier: 1\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\ntables:\\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\\n    model used for SCS/BCS computation.\\n  label: tab:datasets\\n  location:\\n    section: experimental_setup\\n  cells:\\n  - exp_id: exp001_count_baseline\\n    metric: Few-NERD 66 types\\n  - exp_id: exp-004\\n    metric: MAVEN 168 event types, 77993 train mentions\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: FewRel 80 relations\\n  id: T001\\n  deprecated: false\\n- caption: Pairwise SCS--confusion correlation.\\n  label: tab:pairwise\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\\n  - exp_id: bootstrap_ci_analysis\\n    metric: bootstrap CIs for both\\n  id: T002\\n  deprecated: false\\n- caption: BCS-controlled FewRel accuracy.\\n  label: tab:bcs_controlled\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp_fewrel_formal\\n    metric: '16-rel: delta=-9.1pp'\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\\n  - exp_id: bootstrap_ci_analysis\\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\\n  id: T003\\n  deprecated: false\\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\\n  label: tab:error_taxonomy\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\\n  id: T004\\n  deprecated: false\\n- caption: Few-NERD extraction under decomposition modes.\\n  label: tab:sdgd_results\\n  location:\\n    section: sdgd_negative\\n  cells:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\\n      F1=0.292'\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\\n  id: T005\\n  deprecated: false\\nfigures:\\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\\n  label: fig:count_curves\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp001_count_baseline\\n    metric: 'Panel (a): recall 0.72->0.418'\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 'Panel (b): accuracy 0.857->0.504'\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: 'Panel (b): count_40=0.588'\\n  id: F001\\n  deprecated: false\\n- caption: BCS effect scaling with pool size\\n  label: fig:bcs_scaling\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel delta=9.1pp\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: 40-rel delta=33.3pp (80-pool subset)\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel delta=31.2pp\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: LLaMA 80-rel delta=27.1pp\\n  id: F002\\n  deprecated: false\\n- caption: Error taxonomy by BCS bin\\n  label: fig:error_taxonomy\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp007_error_taxonomy\\n    metric: 'NER: IntraSub 0%->49.4%'\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: 'RE: IntraSub 0%->32.3%'\\n  id: F003\\n  deprecated: false\\n_completeness:\\n  coverage: 32/42\\n  claims: 39\\n  tables: 5\\n  figures: 3\\n  tier_counts:\\n    tier1: 0\\n    tier2: 32\\n    tier3: 10\\n    tierX: 0\\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\\n\", \"total_chars\": 21248, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The paper directory doesn't exist at `/root/schema-dag-extraction/docs/paper`. Let me find where the .tex files actually are.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "5cffc6fb-6069-4545-a7b0-4d5cb6334ef8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5cB6ikovcE71xgntLuAiy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9297,
      "cache_read_input_tokens": 25371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9297
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

_source line 17_

论文目录不在 `docs/paper/`，先找实际位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "64775514-96ca-4c5c-a0ad-9495833b058e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5cB6ikovcE71xgntLuAiy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9297,
      "cache_read_input_tokens": 25371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9297
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

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LUhL7Ed1GXuYmrvKr6snFb`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root/schema-dag-extraction -name \"*.tex\" -type f",
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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "6c49d3ba-2709-42db-a265-3d632cb98b39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5cB6ikovcE71xgntLuAiy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9297,
      "cache_read_input_tokens": 25371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9297
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

_source line 19 · 2026-05-16T02:39:01.877Z_

<details><summary>↩ Tool result · `toolu_01LUhL7Ed1GXuYmrvKr6snFb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "ebc7b977-7d87-4e81-9252-b232485130bf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
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
No .tex files found on the server. Let me check the local project directory for .tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "acb829de-83b9-482d-8024-4884658e1606",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFmwZtLhoqUzf1GBuNzBVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 34668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 261
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

_source line 21_

服务器上没有 .tex 文件。检查本地项目目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "4e1477da-5513-4ece-9241-e1850b3ae294",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFmwZtLhoqUzf1GBuNzBVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 34668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 261
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

<details open><summary>🔧 Tool call — Glob · `toolu_01CkR42Fri2ph2UR4WMzqD26`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "5946b4b0-a4ef-4797-83eb-a9af235f184d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFmwZtLhoqUzf1GBuNzBVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 34668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 261
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

_source line 23 · 2026-05-16T02:39:06.203Z_

<details><summary>↩ Tool result · `toolu_01CkR42Fri2ph2UR4WMzqD26`</summary>

```text
artifacts/dream_reports/dream_20260515T053106/best/paper.tex
artifacts/dream_reports/dream_20260515T053106/median/paper.tex
artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
artifacts/dream_reports/dream_20260515T113743/best/paper.tex
artifacts/dream_reports/dream_20260515T113743/median/paper.tex
artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
artifacts/dream_reports/dream_20260515T140829/best/paper.tex
artifacts/dream_reports/dream_20260515T140829/median/paper.tex
artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
docs/paper/sdgd_negative.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/main.tex
artifacts/_project/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "7d0fe6c4-6e4f-4a8b-b6e6-55d3ae0ddf24",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T053106/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/worst/paper.tex",
      "artifacts/_project/paper/dataset_stats.tex",
      "artifacts/paper/tables/dataset_stats.tex",
      "artifacts/_project/paper/sdgd_negative.tex",
      "artifacts/_project/paper/experimental_setup.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/sdgd_negative.tex",
      "docs/paper/discussion.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/results.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/main.tex",
      "artifacts/_project/paper/results.tex"
    ],
    "durationMs": 20,
    "numFiles": 23,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MzTQjMuQeMAEovKmChkfSn`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls /root/schema-dag-extraction/",
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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "d579d814-f2ff-4819-b47b-1becd080a0ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFmwZtLhoqUzf1GBuNzBVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 34668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 261
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

_source line 25 · 2026-05-16T02:39:06.844Z_

<details><summary>↩ Tool result · `toolu_01MzTQjMuQeMAEovKmChkfSn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_ch2.py\\nartifacts\\nconfigs\\ndata\\nfigures\\nlogs\\nmodels\\nresults\\nrun_pilot_wrapper.py\\nscripts\\nsrc\\ntest_ner_prompt.py\\ntest_structured.py\\ntest_vllm_chat.py\\ntest_vllm_minimal.py\\ntest_vllm_structured.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "5961540b-b8e1-44f8-8b27-d2a08b03cbb7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"analyze_ch2.py\\\\nartifacts\\\\nconfigs\\\\ndata\\\\nfigures\\\\nlogs\\\\nmodels\\\\nresults\\\\nrun_pilot_wrapper.py\\\\nscripts\\\\nsrc\\\\ntest_ner_prompt.py\\\\ntest_structured.py\\\\ntest_vllm_chat.py\\\\ntest_vllm_minimal.py\\\\ntest_vllm_structured.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"analyze_ch2.py\\nartifacts\\nconfigs\\ndata\\nfigures\\nlogs\\nmodels\\nresults\\nrun_pilot_wrapper.py\\nscripts\\nsrc\\ntest_ner_prompt.py\\ntest_structured.py\\ntest_vllm_chat.py\\ntest_vllm_minimal.py\\ntest_vllm_structured.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
The .tex files exist locally at `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/` but not on the server. The server doesn't have a `docs/` directory. I need to either:
1. Upload/sync the paper files to the server, or
2. Compile locally

Let me check if LaTeX is available locally, or if I should push the files to the server. Let me first check if latexmk/pdflatex is available locally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "3b736104-b24f-4395-8e7a-717d1b8cc374",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ekEf6dM8gqA3HuyxhqzKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 34929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 918
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

_source line 27_

论文 .tex 文件在本地 `docs/paper/`，服务器上没有。检查本地是否有 LaTeX 编译环境。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "f19b0375-6560-4a0c-8869-948db8d40d6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ekEf6dM8gqA3HuyxhqzKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 34929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 918
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_018xUmVBk62LpQKNFZitazco`</summary>

```json
{
  "command": "which pdflatex latexmk 2>/dev/null; pdflatex --version 2>/dev/null | head -1",
  "description": "Check if LaTeX is available locally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "097631db-df85-4d39-8794-95ae2fc0c55a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ekEf6dM8gqA3HuyxhqzKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 34929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 918
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

_source line 29 · 2026-05-16T02:39:13.992Z_

<details><summary>↩ Tool result · `toolu_018xUmVBk62LpQKNFZitazco`</summary>

```text
/usr/bin/pdflatex
/usr/bin/latexmk
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "9a268a6d-242a-4928-bc41-1b12d8746ea2",
  "tool_use_result": {
    "stdout": "/usr/bin/pdflatex\n/usr/bin/latexmk\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Good, LaTeX is available locally. Let me compile the paper locally and also read the .tex files for consistency checking. Let me do this in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "4e17438f-7df3-444d-ac3d-1296a992064b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJQvpAL1gNTKHZVM7TWpta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 35847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

_source line 31_

本地有 LaTeX。并行编译论文和读取 .tex 文件进行一致性检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "00e59190-759b-4982-a208-a1daad33a542",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJQvpAL1gNTKHZVM7TWpta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 35847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_016ECCNWMYbepUw4gokdESS2`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && latexmk -pdf main.tex 2>&1 | tail -100",
  "description": "Compile paper with latexmk",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "0d930e91-94c9-4e71-b6f7-f694f54bfd84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJQvpAL1gNTKHZVM7TWpta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 35847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

<details open><summary>🔧 Tool call — Read · `toolu_01DVYoDvARu3Mn4h3VmVXtVC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "13769a11-3a2f-4557-a859-4db823598810",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJQvpAL1gNTKHZVM7TWpta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 35847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

<details open><summary>🔧 Tool call — Read · `toolu_01VLeVPqGNnjfzUNpoHCT3US`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "da38c95e-09bd-45e1-a135-c9ae088caf77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJQvpAL1gNTKHZVM7TWpta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 35847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

<details open><summary>🔧 Tool call — Read · `toolu_01CofV6zScqXnwLJ1JjLwCwS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "53f8244e-3f70-488e-9e6a-88a298cc6700",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJQvpAL1gNTKHZVM7TWpta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 35847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

<details open><summary>🔧 Tool call — Read · `toolu_01AsoxDypJD88xDcPM9FKDjX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "2beda820-a68a-4291-9675-ae7c1576b718",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJQvpAL1gNTKHZVM7TWpta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 35847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "biulz2t6m",
  "tool_use_id": "toolu_016ECCNWMYbepUw4gokdESS2",
  "description": "Compile paper with latexmk",
  "task_type": "local_bash",
  "uuid": "ec486b05-0b6d-492a-88fb-3157629c2633",
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c"
}
```

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "biulz2t6m",
  "tool_use_id": "toolu_016ECCNWMYbepUw4gokdESS2",
  "status": "completed",
  "output_file": "",
  "summary": "Compile paper with latexmk",
  "uuid": "7f1d848d-02b6-435a-a9b1-f8dd22431a9d",
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c"
}
```

---

### Tool result

_source line 39 · 2026-05-16T02:39:22.195Z_

<details><summary>↩ Tool result · `toolu_016ECCNWMYbepUw4gokdESS2`</summary>

```text
T1/ptm/m/n/10.95 (+20) from 0.106 at
[5 <../../figures/paper/fig_count_curves.pdf> <../../figures/paper/fig_bcs_scal
ing.pdf>]
Overfull \hbox (1.01689pt too wide) in paragraph at lines 37--38
\T1/ptm/m/n/10.95 (-20) struc-ture and eval-u-a-tion pro-to-col me-di-ate the c
ount--
[6]
Underfull \vbox (badness 10000) has occurred while \output is active [7])
(./sdgd_negative.tex) (./discussion.tex
Underfull \hbox (badness 2469) in paragraph at lines 11--12
 []\T1/ptm/b/n/10.95 (+20) Merge am-pli-fi-ca-tion and fu-ture di-rec-tions.[]

Underfull \hbox (badness 10000) in paragraph at lines 11--12
\T1/ptm/m/n/10.95 (+20) Our SDGD ex-per-i-ments show that naive

Underfull \hbox (badness 3281) in paragraph at lines 11--12
\T1/ptm/m/n/10.95 (+20) decompose-then-merge pipelines fail be-cause

Underfull \hbox (badness 5939) in paragraph at lines 11--12
\T1/ptm/m/n/10.95 (+20) con-straints; and (3) hi-er-ar-chi-cal ex-trac-tion,
[8])
Underfull \hbox (badness 1655) in paragraph at lines 19--35
\T1/ptm/m/n/10.95 (+20) We iso-lated schema-induced degra-da-tion into

Underfull \hbox (badness 2080) in paragraph at lines 19--35
\T1/ptm/m/n/10.95 (+20) count-driven re-call de-cline and confusability-
(./main.bbl
Underfull \hbox (badness 2088) in paragraph at lines 5--9
[]\T1/ptm/m/n/10 (+20) Dhananjay Ashok and Zachary C. Lip-ton. 2023.
[9] [10]
Underfull \hbox (badness 1681) in paragraph at lines 259--265
\T1/ptm/m/n/10 (+20) Chen, Yuansen Zhang, Rui Zheng, Jun-jie Ye,
)

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[11]
Underfull \hbox (badness 5756) in paragraph at lines 126--127
[]\T1/ptm/m/n/10.95 (+20) Single-pass ex-trac-tion achieves F1=0.445

Underfull \hbox (badness 3333) in paragraph at lines 126--127
\T1/ptm/m/n/10.95 (+20) (P=0.210, R=0.314), a 44% rel-a-tive drop.

Underfull \hbox (badness 10000) in paragraph at lines 126--127
\T1/ptm/m/n/10.95 (+20) R=0.446), and per-type ex-trac-tion yields

LaTeX Warning: `h' float specifier changed to `ht'.


Underfull \hbox (badness 1874) in paragraph at lines 152--153
\T1/ptm/m/n/10.95 (+20) 0.210$\OMS/cmsy/m/n/10.95 !$\T1/ptm/m/n/10.95 (+20) 0.3
24; ran-dom_batch: 0.249$\OMS/cmsy/m/n/10.95 !$\T1/ptm/m/n/10.95 (+20) 0.331),
[12 <../../figures/paper/fig_error_taxonomy.pdf>]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
Underfull \hbox (badness 1668) in paragraph at lines 191--191
\T1/ptm/m/n/10 (+20) tions are Pear-son $\OML/cmm/m/it/10 r$ \T1/ptm/m/n/10 (+2
0) from resid-u-al-ized re-gres-sion.

Underfull \hbox (badness 1009) in paragraph at lines 191--191
\T1/ptm/m/n/10 (+20) De-gree cen-tral-ity is com-puted on the SCS graph

Underfull \hbox (badness 3281) in paragraph at lines 191--191
\T1/ptm/m/n/10 (+20) at thresh-old 0.7. All val-ues from ex-per-i-ment
[13] (./main.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/u
crr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (13 pages, 369922 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "dc276003-c1b8-408c-9205-5ffe922e920b",
  "tool_use_result": {
    "stdout": "T1/ptm/m/n/10.95 (+20) from 0.106 at\n[5 <../../figures/paper/fig_count_curves.pdf> <../../figures/paper/fig_bcs_scal\ning.pdf>]\nOverfull \\hbox (1.01689pt too wide) in paragraph at lines 37--38\n\\T1/ptm/m/n/10.95 (-20) struc-ture and eval-u-a-tion pro-to-col me-di-ate the c\nount--\n[6]\nUnderfull \\vbox (badness 10000) has occurred while \\output is active [7])\n(./sdgd_negative.tex) (./discussion.tex\nUnderfull \\hbox (badness 2469) in paragraph at lines 11--12\n []\\T1/ptm/b/n/10.95 (+20) Merge am-pli-fi-ca-tion and fu-ture di-rec-tions.[]\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 11--12\n\\T1/ptm/m/n/10.95 (+20) Our SDGD ex-per-i-ments show that naive\n\nUnderfull \\hbox (badness 3281) in paragraph at lines 11--12\n\\T1/ptm/m/n/10.95 (+20) decompose-then-merge pipelines fail be-cause\n\nUnderfull \\hbox (badness 5939) in paragraph at lines 11--12\n\\T1/ptm/m/n/10.95 (+20) con-straints; and (3) hi-er-ar-chi-cal ex-trac-tion,\n[8])\nUnderfull \\hbox (badness 1655) in paragraph at lines 19--35\n\\T1/ptm/m/n/10.95 (+20) We iso-lated schema-induced degra-da-tion into\n\nUnderfull \\hbox (badness 2080) in paragraph at lines 19--35\n\\T1/ptm/m/n/10.95 (+20) count-driven re-call de-cline and confusability-\n(./main.bbl\nUnderfull \\hbox (badness 2088) in paragraph at lines 5--9\n[]\\T1/ptm/m/n/10 (+20) Dhananjay Ashok and Zachary C. Lip-ton. 2023.\n[9] [10]\nUnderfull \\hbox (badness 1681) in paragraph at lines 259--265\n\\T1/ptm/m/n/10 (+20) Chen, Yuansen Zhang, Rui Zheng, Jun-jie Ye,\n)\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11]\nUnderfull \\hbox (badness 5756) in paragraph at lines 126--127\n[]\\T1/ptm/m/n/10.95 (+20) Single-pass ex-trac-tion achieves F1=0.445\n\nUnderfull \\hbox (badness 3333) in paragraph at lines 126--127\n\\T1/ptm/m/n/10.95 (+20) (P=0.210, R=0.314), a 44% rel-a-tive drop.\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 126--127\n\\T1/ptm/m/n/10.95 (+20) R=0.446), and per-type ex-trac-tion yields\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nUnderfull \\hbox (badness 1874) in paragraph at lines 152--153\n\\T1/ptm/m/n/10.95 (+20) 0.210$\\OMS/cmsy/m/n/10.95 !$\\T1/ptm/m/n/10.95 (+20) 0.3\n24; ran-dom_batch: 0.249$\\OMS/cmsy/m/n/10.95 !$\\T1/ptm/m/n/10.95 (+20) 0.331),\n[12 <../../figures/paper/fig_error_taxonomy.pdf>]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\nUnderfull \\hbox (badness 1668) in paragraph at lines 191--191\n\\T1/ptm/m/n/10 (+20) tions are Pear-son $\\OML/cmm/m/it/10 r$ \\T1/ptm/m/n/10 (+2\n0) from resid-u-al-ized re-gres-sion.\n\nUnderfull \\hbox (badness 1009) in paragraph at lines 191--191\n\\T1/ptm/m/n/10 (+20) De-gree cen-tral-ity is com-puted on the SCS graph\n\nUnderfull \\hbox (badness 3281) in paragraph at lines 191--191\n\\T1/ptm/m/n/10 (+20) at thresh-old 0.7. All val-ues from ex-per-i-ment\n[13] (./main.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/u\ncrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (13 pages, 369922 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T02:39:22.204Z_

<details><summary>↩ Tool result · `toolu_01DVYoDvARu3Mn4h3VmVXtVC`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection (same-domain schemas are subject to a centrality confound). The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), while the wider BCS range at 80 types produces larger absolute accuracy gaps (31.2 vs.\ 9.1\,pp). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "1f2efd55-7b8f-4120-9caa-4fe9ced414c5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection (same-domain schemas are subject to a centrality confound). The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), while the wider BCS range at 80 types produces larger absolute accuracy gaps (31.2 vs.\\ 9.1\\,pp). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T02:39:22.206Z_

<details><summary>↩ Tool result · `toolu_01VLeVPqGNnjfzUNpoHCT3US`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	To answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \emph{count curves} that vary schema size while randomizing confusability, and \emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \cite{fewnerd-2021} (66 entity types across 8 domains), FewRel \cite{fewrel-2018} (80 relation types), and MAVEN \cite{maven-2020} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.
11	
12	Our experiments yield five findings: (1)~schema-induced degradation operates through two channels---count-driven recall decline (up to $-$30\,pp) and confusability-driven type confusion---that are separable in RE; in NER, confusability additionally impairs entity detection; (2)~pairwise SCS predicts type confusion across tasks ($r = 0.112$--$0.129$), modest in magnitude but the first factor empirically isolated in controlled zero-shot IE; (3)~confusability effects are robust across schema sizes, with BCS--accuracy slopes consistent between 16-type and 80-type pools (permutation $p = 0.44$); (4)~per-type confusability aggregation is confounded by centrality on homogeneous schemas; and (5)~confusability-aware decomposition fails due to merge amplification (best F1 = 0.32 vs.\ single-pass 0.45), a structural challenge for union-based merge pipelines.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Multi-channel degradation framework.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, revealing task-dependent channel behavior.
17	    \item \textbf{Pairwise confusability as a statistically significant but modest predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy relationship is consistent across schema sizes (slope permutation $p = 0.44$) and that larger type pools produce wider absolute gaps through expanded BCS ranges.
19	    \item \textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "bbdff27a-4850-4712-98c1-47dbeb5f642c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \\citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \\citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \\citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \\emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \\cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \\emph{count curves} that vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \\cite{fewnerd-2021} (66 entity types across 8 domains), FewRel \\cite{fewrel-2018} (80 relation types), and MAVEN \\cite{maven-2020} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.\n\nOur experiments yield five findings: (1)~schema-induced degradation operates through two channels---count-driven recall decline (up to $-$30\\,pp) and confusability-driven type confusion---that are separable in RE; in NER, confusability additionally impairs entity detection; (2)~pairwise SCS predicts type confusion across tasks ($r = 0.112$--$0.129$), modest in magnitude but the first factor empirically isolated in controlled zero-shot IE; (3)~confusability effects are robust across schema sizes, with BCS--accuracy slopes consistent between 16-type and 80-type pools (permutation $p = 0.44$); (4)~per-type confusability aggregation is confounded by centrality on homogeneous schemas; and (5)~confusability-aware decomposition fails due to merge amplification (best F1 = 0.32 vs.\\ single-pass 0.45), a structural challenge for union-based merge pipelines.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Multi-channel degradation framework.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, revealing task-dependent channel behavior.\n    \\item \\textbf{Pairwise confusability as a statistically significant but modest predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy relationship is consistent across schema sizes (slope permutation $p = 0.44$) and that larger type pools produce wider absolute gaps through expanded BCS ranges.\n    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.\n\\end{enumerate}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T02:39:22.209Z_

<details><summary>↩ Tool result · `toolu_01CofV6zScqXnwLJ1JjLwCwS`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	\begin{figure}[t]
8	\centering
9	\begin{minipage}[t]{0.48\columnwidth}
10	\centering
11	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
12	\end{minipage}
13	\hfill
14	\begin{minipage}[t]{0.48\columnwidth}
15	\centering
16	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
17	\end{minipage}
18	\caption{\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}
19	\label{fig:main_results}
20	\end{figure}
21	
22	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
23	
24	\paragraph{NER (Few-NERD).}
25	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
26	
27	\paragraph{RE (FewRel).}
28	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
29	
30	\paragraph{ED (MAVEN).}
31	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
32	
33	\paragraph{Cross-model replication.}
34	Channel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\,pp recall decline (0.702 at count${}\,=\,1$ to 0.273 at count${}\,=\,64$), compared to $-$34\,pp for Qwen3-32B (Table~\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.
35	
36	\paragraph{Summary.}
37	Schema size degrades extraction quality for NER and RE (Channel~1: count $\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\S\ref{sec:bcs_controlled}).
38	
39	\subsection{Pairwise Confusability and Type Confusion}
40	\label{sec:pairwise}
41	
42	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
43	
44	\begin{table}[t]
45	\centering
46	\small
47	\resizebox{\columnwidth}{!}{%
48	\begin{tabular}{llrrrrr}
49	\toprule
50	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
51	\midrule
52	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\
53	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\
54	\bottomrule
55	\end{tabular}}
56	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}
57	\label{tab:pairwise}
58	\end{table}
59	
60	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.
61	
62	Spearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\rho = 0.168$ ($p = 7.3 \times 10^{-14}$) and MiniLM yields $\rho = 0.144$ ($p = 1.7 \times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\rho = 0.272$ for Qwen3 and $\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\rho = 0.27\text{--}0.31$) characterize the signal among types the model actually confuses.
63	
64	The remaining ${\sim}$98\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\,pp (\S\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.
65	
66	\subsection{BCS-Controlled Experiments}
67	\label{sec:bcs_controlled}
68	
69	To move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\resizebox{\columnwidth}{!}{%
75	\begin{tabular}{lcrrrr}
76	\toprule
77	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
78	\midrule
79	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
80	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
81	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
82	\bottomrule
83	\end{tabular}}
84	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
85	\label{tab:bcs_controlled}
86	\end{table}
87	
88	At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\,pp (95\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
89	
90	The larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\S\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.
91	
92	\paragraph{Within-pool controlled comparison.}
93	\label{sec:within_pool}
94	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\ref{tab:within_pool}).
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\resizebox{\columnwidth}{!}{%
100	\begin{tabular}{lrrrrrrr}
101	\toprule
102	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
103	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
104	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
105	\midrule
106	Independent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\
107	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\
108	Full 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\
109	\midrule
110	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\
111	\bottomrule
112	\end{tabular}}
113	\caption{Three-way BCS--accuracy analysis on FewRel. \textbf{Left}: OLS regression of batch accuracy on BCS; slope CIs excluding zero indicate a significant negative relationship. \textbf{Right}: accuracy difference between top- and bottom-quartile BCS batches (fixed-boundary bootstrap, $n = 10{,}000$). The within-pool setting (80-pool $\to$ 16-sub) eliminates cross-pool type differences while preserving a significant negative slope. Quartile $\Delta$ CIs are wider (and cross zero for 80-pool) due to the compressed BCS range within that pool (0.46--0.68 vs.\ 0.65--0.90 for 16-rel). The full 80-rel condition ($n = 25$) is underpowered for both metrics.}
114	\label{tab:within_pool}
115	\end{table}
116	
117	The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The key evidence is the regression slope: 16-relation subsets drawn from the 80-relation pool show a significant negative slope ($-$0.401, CI excludes zero, $p = 0.027$) comparable to the independent 16-relation pool ($-$0.449). A permutation test finds no significant difference between these slopes ($p = 0.436$, 5{,}000 permutations), indicating that the per-unit sensitivity to confusability is consistent across pools.
118	
119	Quartile $\Delta$ provides supplementary evidence but is less powerful here because the 80-pool subsets span a compressed BCS range (0.46--0.68 vs.\ 0.65--0.90 for the independent pool). Within this narrow band, the quartile contrast ($-$3.92\,pp, CI crosses zero) lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$0.930, $+$0.657]) and quartile analyses; we include it for completeness but do not draw inferential conclusions from it.
120	
121	These results reinterpret the cross-pool gap observed in Table~\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute BCS gap (31.2\,pp vs.\ 9.1\,pp) reflects a wider available BCS range rather than a stronger underlying sensitivity. When sensitivity is measured per unit BCS (i.e., slope), the effect is stable across pools.
122	
123	\paragraph{Cross-model validation.}
124	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; count${}\,=\,16$: 51.6\% vs.\ 51.6\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.
125	
126	\subsection{Multi-Channel Degradation}
127	\label{sec:multi_channel}
128	
129	We decompose extraction errors into an error taxonomy (full data in Table~\ref{tab:error_taxonomy}, Appendix~\ref{sec:appendix_figures}; see also Figure~\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\%), but NER rates are substantially higher (43--65\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.
130	
131	These results establish two degradation channels: \textbf{Channel~1} (count $\to$ recall decline, \S\ref{sec:count_curves}) and \textbf{Channel~2} (confusability $\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.
132	
133	\subsection{Centrality Confound on Homogeneous Schemas}
134	\label{sec:centrality_confound}
135	
136	Per-type analysis on MAVEN reveals an anomaly: the correlation between mean BCS and per-type error rate is \emph{positive}---Qwen3 $\rho = +0.184$ ($p = 0.025$) and MiniLM $\rho = +0.208$ ($p = 0.011$)---opposite to the negative direction predicted by the confusability hypothesis.
137	
138	This reversal traces to a property of same-domain schemas documented by \citet{cai-isotropy-clusters-2021}: when all types derive from a single ontology (here, FrameNet), their embeddings collapse into a single cluster in representation space. In this regime, a type's mean BCS conflates two distinct properties: (i)~confusability with neighbors, which should increase errors, and (ii)~centrality within the cluster, which correlates with being a well-represented, high-frequency type that LLMs extract reliably. The centrality signal dominates, flipping the aggregate correlation.
139	
140	Critically, the pairwise SCS--confusion correlation remains intact: MAVEN MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10}$), consistent with the values in Table~\ref{tab:pairwise}. The problem lies in the aggregation step (mean BCS per type), not in the pairwise signal itself.
141	
142	Few-NERD, whose 66 types span 8 coarse categories across diverse domains, does not exhibit this confound. Its per-type correlation is $\rho = -0.293$ ($p = 0.02$, $n = 63$), in the expected negative direction: types with higher mean confusability have higher error rates. The cross-domain schema spans multiple embedding clusters, breaking the centrality--confusability conflation.
143	
144	This analysis carries a practical implication: mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas. For same-domain schemas where types form a single semantic cluster, pairwise SCS should be used directly, or the centrality component must be factored out before aggregation. A residualized partial-correlation analysis confirming that the raw BCS--F1 correlation vanishes after controlling for frequency and degree centrality is provided in Appendix~\ref{sec:appendix_residualized_bcs}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "a59a199a-ca47-4ce5-b207-df69148b02c9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\\ref{fig:main_results}a).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\\,=\\,22$ to 0.551 at count${}\\,=\\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE.\n\nSpearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ for Qwen3 and $\\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\\rho = 0.27\\text{--}0.31$) characterize the signal among types the model actually confuses.\n\nThe remaining ${\\sim}$98\\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \\cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}), demonstrating practical significance for schema optimization.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThe larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\\S\\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\\ref{tab:within_pool}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ & $-$7.42 & [$-$9.40, $-$5.54] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$) & $-$0.151 & [$-$0.930, $+$0.657] & $-$0.082 & 0.698 & $+$0.35 & [$-$7.11, $+$8.33] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p = 0.436$ (5{,}000 permutations)} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. \\textbf{Left}: OLS regression of batch accuracy on BCS; slope CIs excluding zero indicate a significant negative relationship. \\textbf{Right}: accuracy difference between top- and bottom-quartile BCS batches (fixed-boundary bootstrap, $n = 10{,}000$). The within-pool setting (80-pool $\\to$ 16-sub) eliminates cross-pool type differences while preserving a significant negative slope. Quartile $\\Delta$ CIs are wider (and cross zero for 80-pool) due to the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel). The full 80-rel condition ($n = 25$) is underpowered for both metrics.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The key evidence is the regression slope: 16-relation subsets drawn from the 80-relation pool show a significant negative slope ($-$0.401, CI excludes zero, $p = 0.027$) comparable to the independent 16-relation pool ($-$0.449). A permutation test finds no significant difference between these slopes ($p = 0.436$, 5{,}000 permutations), indicating that the per-unit sensitivity to confusability is consistent across pools.\n\nQuartile $\\Delta$ provides supplementary evidence but is less powerful here because the 80-pool subsets span a compressed BCS range (0.46--0.68 vs.\\ 0.65--0.90 for the independent pool). Within this narrow band, the quartile contrast ($-$3.92\\,pp, CI crosses zero) lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$0.930, $+$0.657]) and quartile analyses; we include it for completeness but do not draw inferential conclusions from it.\n\nThese results reinterpret the cross-pool gap observed in Table~\\ref{tab:bcs_controlled}: the 80-relation pool's larger absolute BCS gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider available BCS range rather than a stronger underlying sensitivity. When sensitivity is measured per unit BCS (i.e., slope), the effect is stable across pools.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe decompose extraction errors into an error taxonomy (full data in Table~\\ref{tab:error_taxonomy}, Appendix~\\ref{sec:appendix_figures}; see also Figure~\\ref{fig:error_taxonomy}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\\%), but NER rates are substantially higher (43--65\\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.\n\nThese results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomaly: the correlation between mean BCS and per-type error rate is \\emph{positive}---Qwen3 $\\rho = +0.184$ ($p = 0.025$) and MiniLM $\\rho = +0.208$ ($p = 0.011$)---opposite to the negative direction predicted by the confusability hypothesis.\n\nThis reversal traces to a property of same-domain schemas documented by \\citet{cai-isotropy-clusters-2021}: when all types derive from a single ontology (here, FrameNet), their embeddings collapse into a single cluster in representation space. In this regime, a type's mean BCS conflates two distinct properties: (i)~confusability with neighbors, which should increase errors, and (ii)~centrality within the cluster, which correlates with being a well-represented, high-frequency type that LLMs extract reliably. The centrality signal dominates, flipping the aggregate correlation.\n\nCritically, the pairwise SCS--confusion correlation remains intact: MAVEN MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10}$), consistent with the values in Table~\\ref{tab:pairwise}. The problem lies in the aggregation step (mean BCS per type), not in the pairwise signal itself.\n\nFew-NERD, whose 66 types span 8 coarse categories across diverse domains, does not exhibit this confound. Its per-type correlation is $\\rho = -0.293$ ($p = 0.02$, $n = 63$), in the expected negative direction: types with higher mean confusability have higher error rates. The cross-domain schema spans multiple embedding clusters, breaking the centrality--confusability conflation.\n\nThis analysis carries a practical implication: mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas. For same-domain schemas where types form a single semantic cluster, pairwise SCS should be used directly, or the centrality component must be factored out before aggregation. A residualized partial-correlation analysis confirming that the raw BCS--F1 correlation vanishes after controlling for frequency and degree centrality is provided in Appendix~\\ref{sec:appendix_residualized_bcs}.",
      "numLines": 144,
      "startLine": 1,
      "totalLines": 144
    }
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T02:39:22.212Z_

<details><summary>↩ Tool result · `toolu_01AsoxDypJD88xDcPM9FKDjX`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	
15	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	
26	\input{related_work}
27	
28	\input{experimental_setup}
29	
30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{discussion}
35	
36	\section*{Limitations}
37	\begin{enumerate}[leftmargin=*,itemsep=2pt]
38	\item \textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\Delta = -27.1$\,pp at count 8, $-23.9$\,pp at count 16), with high-BCS accuracy converging to a model-invariant floor ($\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.
39	
40	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.
41	
42	\item \textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.436$), indicating consistent per-unit sensitivity. The larger absolute gap at 80 relations (31.2\,pp vs.\ 9.1\,pp) reflects the wider BCS range available in that pool, not a stronger underlying effect. A within-pool comparison (Table~\ref{tab:within_pool}) confirms this interpretation: slope $-$0.401, CI excludes zero.
43	
44	\item \textbf{Non-significant factorial test.} A within-dataset factorial analysis (count $\times$ BCS) on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}). The cross-pool slope consistency suggests that confusability sensitivity is stable rather than amplifying with schema size; larger pools simply expose more of the BCS spectrum.
45	
46	\item \textbf{Decomposition scope.} Our experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored.
47	
48	\item \textbf{Metric scope.} SCS/BCS relies on embedding cosine similarity; alternative metrics such as label entropy or ontological depth may capture complementary dimensions of schema difficulty.
49	\end{enumerate}
50	
51	\bibliography{references}
52	
53	\appendix
54	
55	\section{Additional Figures}
56	\label{sec:appendix_figures}
57	
58	\begin{table}[h]
59	\centering
60	\small
61	\begin{tabular}{lrr}
62	\toprule
63	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
64	\midrule
65	1 & 0.702 & 0.640 \\
66	64 & 0.273 & 0.304 \\
67	\midrule
68	Decline & $-$43\,pp & $-$34\,pp \\
69	\bottomrule
70	\end{tabular}
71	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
72	\label{tab:cross_model}
73	\end{table}
74	
75	\begin{table}[h]
76	\centering
77	\small
78	\resizebox{\columnwidth}{!}{%
79	\begin{tabular}{crrrrrr}
80	\toprule
81	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
82	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
83	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
84	\midrule
85	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
86	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
87	\bottomrule
88	\end{tabular}}
89	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
90	\label{tab:cross_model_bcs}
91	\end{table}
92	
93	\begin{table}[h]
94	\centering
95	\small
96	\resizebox{\columnwidth}{!}{%
97	\begin{tabular}{llrrrrrrr}
98	\toprule
99	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
100	\cmidrule(lr){3-7}
101	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
102	\midrule
103	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
104	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}10^{-6}$ \\
105	\midrule
106	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
107	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
108	\bottomrule
109	\end{tabular}}
110	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
111	\label{tab:error_taxonomy}
112	\end{table}
113	
114	\begin{figure}[h]
115	\centering
116	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
117	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
118	\label{fig:error_taxonomy}
119	\end{figure}
120	
121	\section{SDGD Full Protocol and Results}
122	\label{sec:appendix_sdgd}
123	
124	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
125	
126	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
127	
128	\begin{table}[h]
129	\centering
130	\small
131	\resizebox{\columnwidth}{!}{%
132	\begin{tabular}{lrccc}
133	\toprule
134	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
135	\midrule
136	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
137	\midrule
138	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
139	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
140	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
141	\midrule
142	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
143	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
144	\bottomrule
145	\end{tabular}}
146	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
147	\label{tab:sdgd_results}
148	\end{table}
149	
150	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.
151	
152	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), yielding lower F1 in both modes (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
153	
154	\section{Factorial Analysis}
155	\label{sec:appendix_factorial}
156	
157	We conducted a within-dataset $2\!\times\!2$ factorial analysis (count $\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\S\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p = 0.436$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.
158	
159	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
160	\label{sec:appendix_residualized_bcs}
161	
162	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
163	
164	\paragraph{Confound identification.}
165	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
166	\begin{itemize}[itemsep=2pt,leftmargin=*]
167	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.
168	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.
169	\end{itemize}
170	
171	\paragraph{Partial correlation results.}
172	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
173	
174	\begin{table}[h]
175	\centering
176	\small
177	\resizebox{\columnwidth}{!}{%
178	\begin{tabular}{llcccc}
179	\toprule
180	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
181	\midrule
182	MiniLM & --- & $+$0.208 & 0.011 & --- & --- \\
183	MiniLM & log freq & --- & --- & $+$0.133 & 0.107 \\
184	MiniLM & log freq $+$ degree & --- & --- & --- & 0.226 \\
185	\midrule
186	Qwen3 & --- & $+$0.184 & 0.025 & --- & --- \\
187	Qwen3 & degree centrality & --- & --- & $+$0.063 & 0.442 \\
188	Qwen3 & log freq $+$ degree & --- & --- & --- & 0.439 \\
189	\bottomrule
190	\end{tabular}}
191	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
192	\label{tab:residualized_bcs}
193	\end{table}
194	
195	\paragraph{Interpretation.}
196	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
197	
198	Under joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 10^{-10}$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
199	
200	\end{document}
201	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "70037eb2-561e-49d5-9b68-891c22e236b1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\n\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\\Delta = -27.1$\\,pp at count 8, $-23.9$\\,pp at count 16), with high-BCS accuracy converging to a model-invariant floor ($\\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.\n\n\\item \\textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.436$), indicating consistent per-unit sensitivity. The larger absolute gap at 80 relations (31.2\\,pp vs.\\ 9.1\\,pp) reflects the wider BCS range available in that pool, not a stronger underlying effect. A within-pool comparison (Table~\\ref{tab:within_pool}) confirms this interpretation: slope $-$0.401, CI excludes zero.\n\n\\item \\textbf{Non-significant factorial test.} A within-dataset factorial analysis (count $\\times$ BCS) on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}). The cross-pool slope consistency suggests that confusability sensitivity is stable rather than amplifying with schema size; larger pools simply expose more of the BCS spectrum.\n\n\\item \\textbf{Decomposition scope.} Our experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored.\n\n\\item \\textbf{Metric scope.} SCS/BCS relies on embedding cosine similarity; alternative metrics such as label entropy or ontological depth may capture complementary dimensions of schema difficulty.\n\\end{enumerate}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}10^{-6}$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis}\n\\label{sec:appendix_factorial}\n\nWe conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\\S\\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p = 0.436$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & 0.011 & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & 0.107 \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & 0.226 \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & 0.025 & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & 0.442 \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & 0.439 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 10^{-10}$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\end{document}\n",
      "numLines": 201,
      "startLine": 1,
      "totalLines": 201
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Good. The paper compiled successfully with 13 pages and no errors. Only warnings are:
- Overfull/underfull hbox/vbox - harmless
- `h` float specifier changed to `ht` - harmless
- No undefined references, no missing figures

Now let me read the remaining .tex files and do the consistency checks.

Let me also do the key searches for "3.4" / "amplif" / "3.4×" / "amplification" and "8.62" / "0.16" (old CI values).

Let me read the remaining files and do the searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "3b04581b-a2f7-45de-a9e8-50bb7e393c62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013J5fxBdMPU31BeWu9vk7mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 36195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15521
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

_source line 45_

编译成功，13 页无错误。现在读取剩余 tex 文件并搜索关键词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "3fffb1bd-c2ce-4652-b67b-3c8d70b216aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013J5fxBdMPU31BeWu9vk7mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 36195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15521
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

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01A5MyZ7CZNmn3VbMcbzUYWE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "5b1430e8-eb30-49f6-aa59-06727586abce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013J5fxBdMPU31BeWu9vk7mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 36195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15521
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

_source line 47 · 2026-05-16T02:39:32.289Z_

<details><summary>↩ Tool result · `toolu_01A5MyZ7CZNmn3VbMcbzUYWE`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel framework applies most cleanly to cross-domain schemas where types span multiple semantic clusters. For same-domain schemas (e.g., MAVEN's FrameNet-derived types), the centrality confound (\S\ref{sec:centrality_confound}) complicates BCS-level analysis, though the pairwise SCS signal remains intact. Practitioners should use BCS as a schema difficulty predictor for cross-domain ontologies, and pairwise SCS directly---or with centrality factored out---for same-domain schemas.
6	
7	\paragraph{The 51\% floor.}
8	High-BCS accuracy converges to $\approx$51\% on FewRel regardless of model size (8B vs.\ 32B), well above random guessing (12.5\% for 8-way classification). This suggests that under high confusability, models can still resolve a ``confusion subgroup'' of easily distinguishable relations but fail on the tightly clustered remainder. The floor's model-invariance indicates a task-inherent difficulty ceiling that scaling alone cannot overcome.
9	
10	\paragraph{Merge amplification and future directions.}
11	Our SDGD experiments show that naive decompose-then-merge pipelines fail because union merge accumulates contradictory predictions across passes. Three directions may address this: (1)~calibration-aware merge, where cross-batch confidence scores are normalized before aggregation; (2)~joint decoding, where the model sees all types but decodes with confusability-aware constraints; and (3)~hierarchical extraction, processing coarse-grained types first and refining within clusters.
12	
13	\paragraph{Schema design implications.}
14	Our results suggest concrete guidelines: monitor BCS when assembling extraction schemas---high-BCS batches are unreliable regardless of model; for large ontologies, prefer cross-domain type groupings that minimize intra-batch similarity; when decomposition is necessary, invest in cross-batch calibration rather than decomposition quality, since merge amplification---not partitioning---is the primary challenge.
15	
16	\section{Conclusion}
17	\label{sec:conclusion}
18	
19	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural challenge for union-based merge pipelines. Cross-batch calibration or joint decoding is the key next step.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "e5c83a41-ca63-4a75-b78f-54ab7501f8bd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel framework applies most cleanly to cross-domain schemas where types span multiple semantic clusters. For same-domain schemas (e.g., MAVEN's FrameNet-derived types), the centrality confound (\\S\\ref{sec:centrality_confound}) complicates BCS-level analysis, though the pairwise SCS signal remains intact. Practitioners should use BCS as a schema difficulty predictor for cross-domain ontologies, and pairwise SCS directly---or with centrality factored out---for same-domain schemas.\n\n\\paragraph{The 51\\% floor.}\nHigh-BCS accuracy converges to $\\approx$51\\% on FewRel regardless of model size (8B vs.\\ 32B), well above random guessing (12.5\\% for 8-way classification). This suggests that under high confusability, models can still resolve a ``confusion subgroup'' of easily distinguishable relations but fail on the tightly clustered remainder. The floor's model-invariance indicates a task-inherent difficulty ceiling that scaling alone cannot overcome.\n\n\\paragraph{Merge amplification and future directions.}\nOur SDGD experiments show that naive decompose-then-merge pipelines fail because union merge accumulates contradictory predictions across passes. Three directions may address this: (1)~calibration-aware merge, where cross-batch confidence scores are normalized before aggregation; (2)~joint decoding, where the model sees all types but decodes with confusability-aware constraints; and (3)~hierarchical extraction, processing coarse-grained types first and refining within clusters.\n\n\\paragraph{Schema design implications.}\nOur results suggest concrete guidelines: monitor BCS when assembling extraction schemas---high-BCS batches are unreliable regardless of model; for large ontologies, prefer cross-domain type groupings that minimize intra-batch similarity; when decomposition is necessary, invest in cross-batch calibration rather than decomposition quality, since merge amplification---not partitioning---is the primary challenge.\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural challenge for union-based merge pipelines. Cross-batch calibration or joint decoding is the key next step.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01VzLVPcz3vBfwgabQaMnLPk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "54417229-9679-4350-973f-ee860345f6f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013J5fxBdMPU31BeWu9vk7mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 36195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15521
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

_source line 49 · 2026-05-16T02:39:33.185Z_

<details><summary>↩ Tool result · `toolu_01VzLVPcz3vBfwgabQaMnLPk`</summary>

```text
1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	Given that confusability drives type confusion, a natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which constructs a thresholded confusability graph from the pairwise SCS matrix, applies greedy graph coloring to assign types to low-confusability batches, and merges per-batch predictions via set union (full protocol and per-mode results in Appendix~\ref{sec:appendix_sdgd}).
5	
6	Every decomposition mode produces lower F1 than single-pass extraction on Few-NERD: SDGD achieves F1 = 0.241, random batching 0.320, and per-type extraction 0.292, versus the single-pass baseline of 0.445 (Table~\ref{tab:sdgd_results}). The bottleneck is \emph{merge amplification}: processing the same text across multiple passes with different type subsets accumulates contradictory predictions at the union step, destroying precision. Confidence-gated merge does not resolve this, as poorly calibrated LLM scores \cite{llm-calibration-survey-2024} discard correct predictions as aggressively as false positives. This is a structural challenge for union-based merge pipelines, independent of decomposition quality, with direct implications for the partitioning approach of \citet{llm-pee-2025}. Future work must address cross-batch calibration before decomposition can translate confusability signals into extraction gains.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "198ec140-f04e-40a0-a47d-4ceda9bc1008",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Why Naive Decomposition Fails}\n\\label{sec:sdgd}\n\nGiven that confusability drives type confusion, a natural intervention is to partition the schema so confusable types never co-occur. We test this with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), which constructs a thresholded confusability graph from the pairwise SCS matrix, applies greedy graph coloring to assign types to low-confusability batches, and merges per-batch predictions via set union (full protocol and per-mode results in Appendix~\\ref{sec:appendix_sdgd}).\n\nEvery decomposition mode produces lower F1 than single-pass extraction on Few-NERD: SDGD achieves F1 = 0.241, random batching 0.320, and per-type extraction 0.292, versus the single-pass baseline of 0.445 (Table~\\ref{tab:sdgd_results}). The bottleneck is \\emph{merge amplification}: processing the same text across multiple passes with different type subsets accumulates contradictory predictions at the union step, destroying precision. Confidence-gated merge does not resolve this, as poorly calibrated LLM scores \\cite{llm-calibration-survey-2024} discard correct predictions as aggressively as false positives. This is a structural challenge for union-based merge pipelines, independent of decomposition quality, with direct implications for the partitioning approach of \\citet{llm-pee-2025}. Future work must address cross-batch calibration before decomposition can translate confusability signals into extraction gains.\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_019ocGGBSiJAnan5HHy1t9Ze`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "d95a29e9-9237-4f48-9b50-d1b33c0701f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013J5fxBdMPU31BeWu9vk7mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 36195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15521
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

_source line 51 · 2026-05-16T02:39:33.672Z_

<details><summary>↩ Tool result · `toolu_019ocGGBSiJAnan5HHy1t9Ze`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
27	\midrule
28	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
29	FewRel & RE & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
30	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
31	\bottomrule
32	\end{tabular}}
33	\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}
34	\label{tab:datasets}
35	\end{table}
36	
37	\subsection{Schema Confusability Score (SCS)}
38	\label{sec:scs}
39	
40	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
41	{\small
42	\[
43	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
44	\]
45	}
46	
47	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
48	\[
49	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
50	\]
51	
52	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2020}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.
53	
54	\subsection{Experimental Design}
55	\label{sec:exp_design}
56	
57	We conduct two complementary experimental paradigms.
58	
59	\paragraph{Experiment 1: Count Curves.}
60	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{1, 2, 6, 12, 22, 44, 64\} for Few-NERD, \{1, 4, 8, 16, 32, 64, 80\} for FewRel, and \{1, 6, 12, 22, 44, 64\} for MAVEN.
61	
62	\paragraph{Experiment 2: BCS-Controlled.}
63	We fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, we construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). We run this paradigm on Few-NERD at count$\,\in\{6, 12\}$ and on FewRel at count$\,\in\{8, 16\}$, the latter evaluated on both a 16-relation pool and the full 80-relation pool. To control for cross-pool type differences, we additionally draw 16-relation subsets from the 80-relation pool and evaluate under the same protocol, enabling a within-pool comparison that isolates confusability from pool composition. For MAVEN, we conduct analogous BCS-controlled experiments at count$\,\in\{6, 12\}$ with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a centrality confound that complicates BCS interpretation. We report these results separately in \S\ref{sec:centrality_confound}.
64	
65	\subsection{Evaluation Metrics}
66	\label{sec:metrics}
67	
68	We use task-appropriate metrics that reflect the distinct nature of each extraction problem.
69	
70	\paragraph{NER (Few-NERD): Text-match F1.}
71	A predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text \emph{and} the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. We report Precision, Recall, and F1.
72	
73	\paragraph{RE (FewRel): Accuracy.}
74	Each sample has exactly one ground-truth relation. A prediction is correct if the predicted relation label exactly matches the gold label. We report Accuracy.
75	
76	\paragraph{ED (MAVEN): Relaxed F1.}
77	A predicted trigger is a true positive if (a)~any token overlap exists between the predicted trigger span and a gold trigger span, \emph{and} (b)~the predicted event type matches the gold event type. This relaxed matching is necessary because event triggers are inherently ambiguous in boundary (e.g., ``was killed'' vs.\ ``killed''). We report Relaxed F1.
78	
79	The choice of different metrics across tasks reflects their structural differences: NER is span-level extraction where precision--recall trade-offs are informative; RE is a classification task where accuracy directly measures correctness; ED combines trigger identification with type classification, requiring relaxed span matching to avoid penalizing legitimate boundary variation.
80	
81	\subsection{Model and Inference}
82	\label{sec:model}
83	
84	\paragraph{Primary model.}
85	We use Qwen3-32B-FP8 \cite{qwen3-2025}, selected for its strong instruction-following capability, native structured JSON output support, and the practical advantage that the FP8-quantized 32B model fits on a single NVIDIA RTX PRO 6000 Blackwell Server Edition (96\,GB). The model is served via vLLM (v0.20.2) \cite{vllm-2023} with \texttt{max\_model\_len=4096} and \texttt{gpu\_memory\_utilization=0.95}. We use two prompt versions across experiments. The v1 prompt (used for count-curve and BCS-controlled NER experiments) requests start/end character offsets alongside entity text; however, the model fabricates offsets in 96.5\% of predictions, so we evaluate exclusively via text matching (\S\ref{sec:metrics}), which is robust to offset errors. The v2 prompt (used for all subsequent experiments) drops the offset requirement and adds explicit output format constraints and role instructions, doubling precision with minimal recall loss. Both versions provide a JSON-formatted schema listing all type names for the current batch; the model outputs structured JSON containing extracted entities, relations, or events. We use greedy decoding (temperature${}\,=\,0$) and a fixed random seed (42) for all batch sampling and bootstrap resampling, ensuring full reproducibility. Prior work has shown that LLM outputs can be sensitive to prompt formatting choices \cite{sclar-sensitivity-2024}; we report results from both prompt versions where applicable to quantify this effect.
86	
87	\paragraph{Cross-model validation.}
88	To test whether schema-induced degradation generalizes beyond the primary model, we replicate both experimental paradigms on Few-NERD and FewRel using Meta-Llama-3.1-8B-Instruct, a $4\times$ smaller model from a different model family. For NER we use text-match recall (Llama does not reliably produce span offsets); for RE we use accuracy.
89	
90	\paragraph{Statistical estimation.}
91	All key metrics are accompanied by 95\% bootstrap confidence intervals computed from 1{,}000 bootstrap resamples using the percentile method.
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "6a11ca96-a599-462b-853e-52cf21d07c97",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, we construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). We run this paradigm on Few-NERD at count$\\,\\in\\{6, 12\\}$ and on FewRel at count$\\,\\in\\{8, 16\\}$, the latter evaluated on both a 16-relation pool and the full 80-relation pool. To control for cross-pool type differences, we additionally draw 16-relation subsets from the 80-relation pool and evaluate under the same protocol, enabling a within-pool comparison that isolates confusability from pool composition. For MAVEN, we conduct analogous BCS-controlled experiments at count$\\,\\in\\{6, 12\\}$ with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a centrality confound that complicates BCS interpretation. We report these results separately in \\S\\ref{sec:centrality_confound}.\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\nWe use task-appropriate metrics that reflect the distinct nature of each extraction problem.\n\n\\paragraph{NER (Few-NERD): Text-match F1.}\nA predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text \\emph{and} the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. We report Precision, Recall, and F1.\n\n\\paragraph{RE (FewRel): Accuracy.}\nEach sample has exactly one ground-truth relation. A prediction is correct if the predicted relation label exactly matches the gold label. We report Accuracy.\n\n\\paragraph{ED (MAVEN): Relaxed F1.}\nA predicted trigger is a true positive if (a)~any token overlap exists between the predicted trigger span and a gold trigger span, \\emph{and} (b)~the predicted event type matches the gold event type. This relaxed matching is necessary because event triggers are inherently ambiguous in boundary (e.g., ``was killed'' vs.\\ ``killed''). We report Relaxed F1.\n\nThe choice of different metrics across tasks reflects their structural differences: NER is span-level extraction where precision--recall trade-offs are informative; RE is a classification task where accuracy directly measures correctness; ED combines trigger identification with type classification, requiring relaxed span matching to avoid penalizing legitimate boundary variation.\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\n\\paragraph{Primary model.}\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025}, selected for its strong instruction-following capability, native structured JSON output support, and the practical advantage that the FP8-quantized 32B model fits on a single NVIDIA RTX PRO 6000 Blackwell Server Edition (96\\,GB). The model is served via vLLM (v0.20.2) \\cite{vllm-2023} with \\texttt{max\\_model\\_len=4096} and \\texttt{gpu\\_memory\\_utilization=0.95}. We use two prompt versions across experiments. The v1 prompt (used for count-curve and BCS-controlled NER experiments) requests start/end character offsets alongside entity text; however, the model fabricates offsets in 96.5\\% of predictions, so we evaluate exclusively via text matching (\\S\\ref{sec:metrics}), which is robust to offset errors. The v2 prompt (used for all subsequent experiments) drops the offset requirement and adds explicit output format constraints and role instructions, doubling precision with minimal recall loss. Both versions provide a JSON-formatted schema listing all type names for the current batch; the model outputs structured JSON containing extracted entities, relations, or events. We use greedy decoding (temperature${}\\,=\\,0$) and a fixed random seed (42) for all batch sampling and bootstrap resampling, ensuring full reproducibility. Prior work has shown that LLM outputs can be sensitive to prompt formatting choices \\cite{sclar-sensitivity-2024}; we report results from both prompt versions where applicable to quantify this effect.\n\n\\paragraph{Cross-model validation.}\nTo test whether schema-induced degradation generalizes beyond the primary model, we replicate both experimental paradigms on Few-NERD and FewRel using Meta-Llama-3.1-8B-Instruct, a $4\\times$ smaller model from a different model family. For NER we use text-match recall (Llama does not reliably produce span offsets); for RE we use accuracy.\n\n\\paragraph{Statistical estimation.}\nAll key metrics are accompanied by 95\\% bootstrap confidence intervals computed from 1{,}000 bootstrap resamples using the percentile method.\n",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_018v8fYpyJvQzLq1AkFdZrPt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "f557205e-0ee2-4324-8857-d5804741d29a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013J5fxBdMPU31BeWu9vk7mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 36195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15521
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

_source line 53 · 2026-05-16T02:39:34.759Z_

<details><summary>↩ Tool result · `toolu_018v8fYpyJvQzLq1AkFdZrPt`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, approaches include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}; \citet{familiarity-2025} quantify label shifts in zero-shot NER evaluation. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
8	
9	\subsection{Schema Complexity in IE}
10	\label{sec:rw_schema}
11	
12	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\S\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\S\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.
13	
14	Other approaches address schema complexity from different angles: hard negative mining during training \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, event schema decomposition \cite{dee-2024}, multi-agent debate for cross-type IE \cite{crossagentie-2025,cmas-ner-2025}, schema-as-tool parameterization \cite{spt-2025}, on-device schema-aware IE \cite{dlisc-2025}, schema-constrained knowledge graph generation \cite{kggen-2025}, and active prompting guided by introspective confusion analysis \cite{reflect-learn-2026}. All treat schema complexity as an engineering problem; we instead treat it as a scientific question about the independent mechanisms by which schema properties degrade extraction.
15	
16	\subsection{Representation Degeneration and Embedding Anisotropy}
17	\label{sec:rw_anisotropy}
18	
19	Our centrality confound analysis (\S\ref{sec:centrality_confound}) connects to the representation degeneration literature. \citet{gao-repr-degen-2019} showed that word embeddings degenerate into narrow cones, and \citet{ethayarajh-contextual-2019} extended this to contextual representations. Crucially, \citet{cai-isotropy-clusters-2021} showed that while the global space is anisotropic, local clusters can be isotropic---directly explaining our MAVEN results where single-ontology types form one dense cluster conflating confusability with centrality. \citet{godey-anisotropy-inherent-2024} proved anisotropy is inherent to self-attention, suggesting the centrality confound persists across architectures. Our work provides the first empirical demonstration that this anisotropy creates a measurable confound in IE schema analysis.
20	
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "69602cdf-96f8-4ec6-b5ca-5d5fa0837df5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Training-Free LLM Information Extraction}\n\\label{sec:rw_training_free}\n\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025}. For NER, approaches include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, bidirectional encoders \\cite{gliner-2024,gliner2-2025}, and guided synthesis \\cite{guidex-2025,nuner-2024}; \\citet{familiarity-2025} quantify label shifts in zero-shot NER evaluation. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.\n\n\\subsection{Schema Complexity in IE}\n\\label{sec:rw_schema}\n\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \\emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\\S\\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.\n\nOther approaches address schema complexity from different angles: hard negative mining during training \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, event schema decomposition \\cite{dee-2024}, multi-agent debate for cross-type IE \\cite{crossagentie-2025,cmas-ner-2025}, schema-as-tool parameterization \\cite{spt-2025}, on-device schema-aware IE \\cite{dlisc-2025}, schema-constrained knowledge graph generation \\cite{kggen-2025}, and active prompting guided by introspective confusion analysis \\cite{reflect-learn-2026}. All treat schema complexity as an engineering problem; we instead treat it as a scientific question about the independent mechanisms by which schema properties degrade extraction.\n\n\\subsection{Representation Degeneration and Embedding Anisotropy}\n\\label{sec:rw_anisotropy}\n\nOur centrality confound analysis (\\S\\ref{sec:centrality_confound}) connects to the representation degeneration literature. \\citet{gao-repr-degen-2019} showed that word embeddings degenerate into narrow cones, and \\citet{ethayarajh-contextual-2019} extended this to contextual representations. Crucially, \\citet{cai-isotropy-clusters-2021} showed that while the global space is anisotropic, local clusters can be isotropic---directly explaining our MAVEN results where single-ontology types form one dense cluster conflating confusability with centrality. \\citet{godey-anisotropy-inherent-2024} proved anisotropy is inherent to self-attention, suggesting the centrality confound persists across architectures. Our work provides the first empirical demonstration that this anisotropy creates a measurable confound in IE schema analysis.\n\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Grep · `toolu_017r1WETQmzedcALtSKtY1Ft`</summary>

```json
{
  "pattern": "3\\.4[×x]|3\\.4\\s|amplif",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "a43e7690-e592-47aa-bd5c-63657273600f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013J5fxBdMPU31BeWu9vk7mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 36195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15521
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

_source line 55 · 2026-05-16T02:39:36.177Z_

<details><summary>↩ Tool result · `toolu_017r1WETQmzedcALtSKtY1Ft`</summary>

```text
main.tex:44:\item \textbf{Non-significant factorial test.} A within-dataset factorial analysis (count $\times$ BCS) on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}). The cross-pool slope consistency suggests that confusability sensitivity is stable rather than amplifying with schema size; larger pools simply expose more of the BCS spectrum.
main.tex:157:[Omitted long matching line]
main.log:205:Package: url 2013/09/16  ver 3.4  Verb mode for urls, etc.
discussion.tex:10:\paragraph{Merge amplification and future directions.}
discussion.tex:14:Our results suggest concrete guidelines: monitor BCS when assembling extraction schemas---high-BCS batches are unreliable regardless of model; for large ontologies, prefer cross-domain type groupings that minimize intra-batch similarity; when decomposition is necessary, invest in cross-batch calibration rather than decomposition quality, since merge amplification---not partitioning---is the primary challenge.
discussion.tex:19:[Omitted long matching line]
abstract.tex:2:[Omitted long matching line]
introduction.tex:12:[Omitted long matching line]
introduction.tex:19:    \item \textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.
main.aux:844:\@writefile{toc}{\contentsline {paragraph}{Merge amplification and future directions.}{8}{section*.26}\protected@file@percent }
sdgd_negative.tex:6:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "403b6d3b-2beb-4642-9817-555db71fff32",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "main.tex:44:\\item \\textbf{Non-significant factorial test.} A within-dataset factorial analysis (count $\\times$ BCS) on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}). The cross-pool slope consistency suggests that confusability sensitivity is stable rather than amplifying with schema size; larger pools simply expose more of the BCS spectrum.\nmain.tex:157:[Omitted long matching line]\nmain.log:205:Package: url 2013/09/16  ver 3.4  Verb mode for urls, etc.\ndiscussion.tex:10:\\paragraph{Merge amplification and future directions.}\ndiscussion.tex:14:Our results suggest concrete guidelines: monitor BCS when assembling extraction schemas---high-BCS batches are unreliable regardless of model; for large ontologies, prefer cross-domain type groupings that minimize intra-batch similarity; when decomposition is necessary, invest in cross-batch calibration rather than decomposition quality, since merge amplification---not partitioning---is the primary challenge.\ndiscussion.tex:19:[Omitted long matching line]\nabstract.tex:2:[Omitted long matching line]\nintroduction.tex:12:[Omitted long matching line]\nintroduction.tex:19:    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.\nmain.aux:844:\\@writefile{toc}{\\contentsline {paragraph}{Merge amplification and future directions.}{8}{section*.26}\\protected@file@percent }\nsdgd_negative.tex:6:[Omitted long matching line]",
    "numLines": 11
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_013ter8iHJg39JEk2g5LD1bd`</summary>

```json
{
  "pattern": "8\\.62|0\\.16[^0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "b9436cb2-3d07-4227-9258-1724ce6d28b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013J5fxBdMPU31BeWu9vk7mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15521,
      "cache_read_input_tokens": 36195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15521
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

_source line 57 · 2026-05-16T02:39:36.882Z_

<details><summary>↩ Tool result · `toolu_013ter8iHJg39JEk2g5LD1bd`</summary>

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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "dea90d91-a4c7-42a3-bc81-0930a2da6952",
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

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the results:

1. **Compilation**: Success - 13 pages, 369,922 bytes. Only benign warnings (overfull/underfull hbox, float specifier changes). No undefined references, no missing figures.

2. **"3.4×" / "amplification" search**: 
   - "3.4×" or "3.4x" in the BCS amplification sense: NOT FOUND in any .tex file. The only "3.4" hit is from `main.log` referencing `url package ver 3.4`.
   - "amplif" hits are ALL "merge amplification" (SDGD concept), NOT "BCS amplification". 

I'm seeing references to "3.4x amplification" in the provenance file for entries C010 and C013, but those aren't in the actual .tex source files. Let me double-check what introduction.tex line 12 actually contains—looking back at my earlier read, it discusses confusability effects and BCS-accuracy slopes across different pool sizes, not the amplification metric I'm searching for. I see the issue now—the grep matched on "amplif" in line 12, which appears in "merge amplification" at the end. The line contains the five key experimental findings: schema-induced degradation through count and confusability channels, pairwise SCS predicting type confusion, robustness across schema sizes, confoundedness by centrality, and the failure of confusability-aware decomposition due to amplification effects. I'm verifying the numerical consistency between the abstract and results sections. The NER recall values match (0.72 to 0.42), the RE accuracy figures align (85.7% to 50.4%), and the permutation p-value checks out at 0.436 with the abstract rounding to 0.44. Let me continue cross-checking the remaining metrics. Continuing to verify the introduction claims against the results tables—the permutation p-values are consistently matching around 0.44, and the F1 scores for merge amplification align with the reported values. Now I'm checking the slope values and confidence intervals, though I'm noticing a slight discrepancy in the CI bounds that needs clarification. Looking at the specific values the task asks me to verify, I'm checking that -0.449, -0.401, and the permutation p=0.436 all appear consistently across the table and the text below it—and they do. Now I'm moving on to check the main.tex file, where I need to verify that the Llama-3.1-8B-Instruct results match: the -43 percentage point recall decline and r = 0.725 correlation both check out against the results table. I'm verifying the table layout matches the results—regression metrics on the left, quartile comparisons on the right, with the permutation p-value in the footnote and a note about the underpowered 80-relation condition. The count=40 evaluation is properly documented as subsets from the 80-relation pool, and I've confirmed the BCS amplification constraint is satisfied.

Now I'm checking the provenance YAML to ensure the within-pool table references the correct data source from the unified results file.

Looking at the table entries, I notice there's no T006 for the within-pool table yet, which needs to be added with the proper data source reference. I also see that C010 and C013 still reference the "3.4×" amplification figure that's no longer in the paper, so those provenance claims need updating to match what the paper actually says about the BCS-accuracy relationship. Now I'm checking the confidence intervals in the provenance against what's actually in the paper—there are some discrepancies I need to resolve. C033 and C034 have different CI values than what appears in the paper, and I need to verify the quartile delta claims in C036-C038 as well.

Looking more carefully, C036-C038 seem to be referencing extreme-batch analysis from a different table rather than the quartile deltas from the within-pool analysis, which explains why the numbers don't align with what I'd expect from the main table.

The task mentions the data source shifted from bootstrap_ci.json to results_unified.json, so I need to check if the provenance entries need updating—particularly for the within_pool table and any entries still pointing to the old bootstrap_ci_analysis experiment ID.

Looking at the writable files available through save_project_file, I notice paper_provenance.yaml isn't in the whitelist, which means I can't directly update it even though that's what the task is asking for. I should verify whether there's a workaround or if this is a constraint I need to flag.

Let me also check those C010 and C013 entries that still reference the "3.4x amplification" claim to see what needs correcting there.

C010 mentions confusability effects amplifying with schema scale, but the current paper text frames this as robust and consistent across sizes with a non-significant permutation test. C013 has similar outdated language about amplification, when the paper now emphasizes consistency in the relationship while noting that larger pools create wider absolute gaps through expanded ranges. Both provenance entries are stale relative to what's actually written in the paper now.

I need to update the YAML to fix these mismatches. For C010, I'll reframe it around the robustness finding and the permutation test result. For C013, I'll adjust the language to match the current contribution statement about consistency across schema sizes and the mechanism of wider gaps. I also need to add the missing T006 entry for the within-pool table and correct the confidence intervals for C033 and C034 to align with the current paper values. I need to locate the provenance file and make targeted edits to fix the confidence intervals for C033 and C034, plus add the T006 entry for the within-pool table. Let me access the file directly and update those specific values rather than rewriting the entire document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "463e570c-368f-4eef-98ca-84a53e0710e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vq6eurdFmsevRCZKhAPBNo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6404,
      "cache_read_input_tokens": 51716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6404
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

_source line 59_

编译成功（13页，无错误）。搜索结果显示无 "3.4×" BCS amplification 残留，无旧 CI "8.62"/"0.16"。继续检查 "3.4" 的精确匹配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "53fdc355-d595-4524-b100-98e763a2f992",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vq6eurdFmsevRCZKhAPBNo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6404,
      "cache_read_input_tokens": 51716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6404
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

_source line 60_

<details open><summary>🔧 Tool call — Grep · `toolu_01PpHJhhrcdcWSamdx9LxCpX`</summary>

```json
{
  "pattern": "\\b3\\.4\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "98b94b38-4496-4cd2-a7a7-b9a128f54fe2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vq6eurdFmsevRCZKhAPBNo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6404,
      "cache_read_input_tokens": 51716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6404
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

_source line 61 · 2026-05-16T02:41:37.900Z_

<details><summary>↩ Tool result · `toolu_01PpHJhhrcdcWSamdx9LxCpX`</summary>

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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "b65a5a13-878d-4f5c-ab6a-d346dade6889",
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

_source line 62_

<details open><summary>🔧 Tool call — Grep · `toolu_012arRQMF1GiRkUBQnWs7xmN`</summary>

```json
{
  "pattern": "amplif",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
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
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "e7021436-fddc-4027-9905-e627d6a544fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vq6eurdFmsevRCZKhAPBNo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6404,
      "cache_read_input_tokens": 51716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6404
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

_source line 63 · 2026-05-16T02:41:38.730Z_

<details><summary>↩ Tool result · `toolu_012arRQMF1GiRkUBQnWs7xmN`</summary>

```text
main.tex:44:\item \textbf{Non-significant factorial test.} A within-dataset factorial analysis (count $\times$ BCS) on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}). The cross-pool slope consistency suggests that confusability sensitivity is stable rather than amplifying with schema size; larger pools simply expose more of the BCS spectrum.
main.tex:157:[Omitted long matching line]
discussion.tex:10:\paragraph{Merge amplification and future directions.}
discussion.tex:14:Our results suggest concrete guidelines: monitor BCS when assembling extraction schemas---high-BCS batches are unreliable regardless of model; for large ontologies, prefer cross-domain type groupings that minimize intra-batch similarity; when decomposition is necessary, invest in cross-batch calibration rather than decomposition quality, since merge amplification---not partitioning---is the primary challenge.
discussion.tex:19:[Omitted long matching line]
abstract.tex:2:[Omitted long matching line]
introduction.tex:12:[Omitted long matching line]
introduction.tex:19:    \item \textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.
sdgd_negative.tex:6:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "fbac3a55-9a67-43ea-a3d3-cddfdc9e11d5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "main.tex:44:\\item \\textbf{Non-significant factorial test.} A within-dataset factorial analysis (count $\\times$ BCS) on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}). The cross-pool slope consistency suggests that confusability sensitivity is stable rather than amplifying with schema size; larger pools simply expose more of the BCS spectrum.\nmain.tex:157:[Omitted long matching line]\ndiscussion.tex:10:\\paragraph{Merge amplification and future directions.}\ndiscussion.tex:14:Our results suggest concrete guidelines: monitor BCS when assembling extraction schemas---high-BCS batches are unreliable regardless of model; for large ontologies, prefer cross-domain type groupings that minimize intra-batch similarity; when decomposition is necessary, invest in cross-batch calibration rather than decomposition quality, since merge amplification---not partitioning---is the primary challenge.\ndiscussion.tex:19:[Omitted long matching line]\nabstract.tex:2:[Omitted long matching line]\nintroduction.tex:12:[Omitted long matching line]\nintroduction.tex:19:    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.\nsdgd_negative.tex:6:[Omitted long matching line]",
    "numLines": 9
  }
}
```

</details>

---

### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
All "amplification" references in .tex files are:
1. main.tex:44 - "stable rather than amplifying" - this is about the factorial test, saying the effect is NOT amplifying. OK.
2. main.tex:157 - Let me check line 157. From my read, that's in the appendix factorial analysis section: "The cross-pool slope analysis on FewRel shows consistent BCS--accuracy sensitivity across pool sizes (permutation p = 0.436), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size."


3. The remaining references across discussion.tex, abstract.tex, introduction.tex, and sdgd_negative.tex all refer to "merge amplification" as the SDGD concept. No "3.4" appears anywhere in the codebase, and all amplification mentions are either about merge amplification or the stable-rather-than-amplifying finding.

Now I need to update the provenance file to fix the outdated references in C010 and C013 that still cite "3.4× amplification," add a new entry for the within-pool table sourced from results_unified.json, and correct the confidence intervals in C033 and C034 to match the current paper values. I'll edit the provenance YAML directly since it's a substantial update.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "1287a4c5-254a-41bb-a74c-651080fa51ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYjLD75k9qFVwrKBpACKCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 58120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5897
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

_source line 65_

所有 "amplification" 均为 "merge amplification"（SDGD 概念）或否定形式（"stable rather than amplifying"）。"3.4" / "3.4×" 在 .tex 中完全清除。

现在更新 provenance。先读取本地文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "f8e7b451-6184-4fde-ba14-9c93d2a6bea6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYjLD75k9qFVwrKBpACKCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 58120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5897
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

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01SYqJzVjXYUSTvFBCfCWTpr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "ba99c01c-86d8-48f9-94be-861b0d7c1d09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYjLD75k9qFVwrKBpACKCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 58120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5897
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

_source line 67 · 2026-05-16T02:41:55.255Z_

<details><summary>↩ Tool result · `toolu_01SYqJzVjXYUSTvFBCfCWTpr`</summary>

```text
1	paper:
2	  title: Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free
3	    LLM Information Extraction?
4	  version: 3
5	  generated_at: '2026-05-16T02:22:29.529376+00:00'
6	  source: manual mapping from registry + paper_framing.md
7	claims:
8	- text: 'Training-free LLM information extraction---prompting models with target schemas
9	    without fine-tuning---degrades sharply as schema complexity grows: NER recall
10	    drops from 0.72 to 0.42 with 64 candidate '
11	  type: quantitative
12	  location:
13	    section: abstract
14	    context: result_statement
15	  id: C001
16	  evidence:
17	  - exp_id: exp001_count_baseline
18	    metric: recall count_1=0.720, count_64=0.418
19	    tier: 1
20	  deprecated: false
21	- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic
22	    overlap between types and design two complementary experimental paradigms: count
23	    cu'
24	  type: methodological
25	  location:
26	    section: abstract
27	    context: finding_statement
28	  id: C002
29	  evidence:
30	  - exp_id: exp015_scs_validation
31	    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'
32	    tier: 1
33	  deprecated: false
34	- text: 'We presented a controlled empirical study isolating schema-induced degradation
35	    in training-free LLM IE into two orthogonal channels: a count channel suppressing
36	    recall as candidate types increase, and'
37	  type: quantitative
38	  location:
39	    section: conclusion
40	    context: result_statement
41	  id: C003
42	  evidence:
43	  - exp_id: exp001_count_baseline
44	    metric: 'Channel 1: recall 0.72->0.418'
45	    tier: 1
46	  - exp_id: exp007_error_taxonomy
47	    metric: 'Channel 2: IntraSub vs BCS rho=1.0'
48	    tier: 1
49	  - exp_id: exp016_fewrel_error_taxonomy
50	    metric: RE IntraSub vs BCS rho=0.954
51	    tier: 1
52	  deprecated: false
53	- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following
54	    capability, native structured JSON output support, and the practical advantage
55	    that the FP8-quantized 32B model fits on a
56	  type: quantitative
57	  location:
58	    section: experimental_setup
59	    context: result_statement
60	  id: C004
61	  evidence:
62	  - exp_id: exp001_count_baseline
63	    metric: model setup, all experiments use Qwen3-32B-FP8 primary
64	    tier: 2
65	  deprecated: false
66	- text: We introduce the Schema Confusability Score to quantify semantic overlap between
67	    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin
68	  type: methodological
69	  location:
70	    section: experimental_setup
71	    context: finding_statement
72	  id: C005
73	  evidence:
74	  - exp_id: exp015_scs_validation
75	    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'
76	    tier: 1
77	  deprecated: false
78	- text: Channel~1
79	  type: quantitative
80	  location:
81	    section: introduction
82	    context: bold
83	  id: C006
84	  evidence:
85	  - exp_id: exp001_count_baseline
86	    metric: recall 0.72->0.418 monotonic decline
87	    tier: 1
88	  - exp_id: exp_fewrel_formal_80rel
89	    metric: accuracy 0.857->0.504 monotonic decline
90	    tier: 1
91	  deprecated: false
92	- text: Channel~2
93	  type: quantitative
94	  location:
95	    section: introduction
96	    context: bold
97	  id: C007
98	  evidence:
99	  - exp_id: exp002_confusability_controlled
100	    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "a31411bc-4856-476e-be97-51f6da06a895",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
      "content": "paper:\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free\n    LLM Information Extraction?\n  version: 3\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\n  source: manual mapping from registry + paper_framing.md\nclaims:\n- text: 'Training-free LLM information extraction---prompting models with target schemas\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\n    drops from 0.72 to 0.42 with 64 candidate '\n  type: quantitative\n  location:\n    section: abstract\n    context: result_statement\n  id: C001\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall count_1=0.720, count_64=0.418\n    tier: 1\n  deprecated: false\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\n    overlap between types and design two complementary experimental paradigms: count\n    cu'\n  type: methodological\n  location:\n    section: abstract\n    context: finding_statement\n  id: C002\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\n    tier: 1\n  deprecated: false\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\n    recall as candidate types increase, and'\n  type: quantitative\n  location:\n    section: conclusion\n    context: result_statement\n  id: C003\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: 'Channel 1: recall 0.72->0.418'\n    tier: 1\n  - exp_id: exp007_error_taxonomy\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub vs BCS rho=0.954\n    tier: 1\n  deprecated: false\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\n    capability, native structured JSON output support, and the practical advantage\n    that the FP8-quantized 32B model fits on a\n  type: quantitative\n  location:\n    section: experimental_setup\n    context: result_statement\n  id: C004\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\n    tier: 2\n  deprecated: false\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\n  type: methodological\n  location:\n    section: experimental_setup\n    context: finding_statement\n  id: C005\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\n    tier: 1\n  deprecated: false\n- text: Channel~1\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C006\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418 monotonic decline\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: accuracy 0.857->0.504 monotonic decline\n    tier: 1\n  deprecated: false\n- text: Channel~2\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C007\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 664
    }
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01YHabxknqnLa91SzpKEhPPo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "offset": 100,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "ae43ac72-0305-41b9-86bb-269af809adc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CT9cSa6GufbTnzxjRxqcVM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1990,
      "cache_read_input_tokens": 64017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1990
      },
      "output_tokens": 36,
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

_source line 69 · 2026-05-16T02:41:58.990Z_

<details><summary>↩ Tool result · `toolu_01YHabxknqnLa91SzpKEhPPo`</summary>

```text
100	    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x
101	    tier: 1
102	  - exp_id: exp_fewrel_formal_80rel
103	    metric: BCS-controlled delta=-31.2pp
104	    tier: 1
105	  deprecated: false
106	- text: Training-free LLM information extraction---prompting a large language model
107	    with a target schema and asking it to extract structured information without any
108	    task-specific fine-tuning---enables rapid d
109	  type: quantitative
110	  location:
111	    section: introduction
112	    context: result_statement
113	  id: C008
114	  evidence:
115	  - exp_id: exp001_count_baseline
116	    metric: background framing, supported by all experiments
117	    tier: 3
118	  deprecated: false
119	- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD
120	    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding
121	    similarity between type pairs corre
122	  type: quantitative
123	  location:
124	    section: introduction
125	    context: result_statement
126	  id: C009
127	  evidence:
128	  - exp_id: exp002_confusability_controlled
129	    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]
130	    tier: 1
131	  - exp_id: exp004_maven_bcs
132	    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]
133	    tier: 1
134	  - exp_id: bootstrap_ci_analysis
135	    metric: CIs exclude zero for both
136	    tier: 1
137	  deprecated: false
138	- text: Third, confusability effects amplify with schema scale. In BCS-controlled
139	    FewRel experiments, switching from low-confusability to high-confusability type
140	    batches reduces accuracy by 9.1 percentage poi
141	  type: quantitative
142	  location:
143	    section: introduction
144	    context: result_statement
145	  id: C010
146	  evidence:
147	  - exp_id: exp_fewrel_formal
148	    metric: 16-rel BCS effect delta=-9.1pp
149	    tier: 1
150	  - exp_id: exp_fewrel_formal_80rel
151	    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x
152	    tier: 1
153	  deprecated: false
154	- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.
155	    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation
156	    between mean BCS and per-type er
157	  type: quantitative
158	  location:
159	    section: introduction
160	    context: result_statement
161	  id: C011
162	  evidence:
163	  - exp_id: exp004_maven_bcs
164	    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)
165	    tier: 1
166	  deprecated: false
167	- text: Fifth, confusability-aware schema decomposition fails to improve extraction.
168	    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types
169	    into different batches, yet every decomp
170	  type: quantitative
171	  location:
172	    section: introduction
173	    context: result_statement
174	  id: C012
175	  evidence:
176	  - exp_id: exp008_sdgd_v2_fewnerd
177	    metric: SDGD v2 F1=0.241 vs baseline 0.445
178	    tier: 1
179	  - exp_id: exp008_sdgd_zero_fewnerd_r2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "34c46e08-9747-4863-95fc-be78e72ffff1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
      "content": "    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS-controlled delta=-31.2pp\n    tier: 1\n  deprecated: false\n- text: Training-free LLM information extraction---prompting a large language model\n    with a target schema and asking it to extract structured information without any\n    task-specific fine-tuning---enables rapid d\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C008\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: background framing, supported by all experiments\n    tier: 3\n  deprecated: false\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\n    similarity between type pairs corre\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C009\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CIs exclude zero for both\n    tier: 1\n  deprecated: false\n- text: Third, confusability effects amplify with schema scale. In BCS-controlled\n    FewRel experiments, switching from low-confusability to high-confusability type\n    batches reduces accuracy by 9.1 percentage poi\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x\n    tier: 1\n  deprecated: false\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\n    between mean BCS and per-type er\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C011\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\n    into different batches, yet every decomp\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C012\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\n    tier: 1\n  - exp_id: exp008_sdgd_zero_fewnerd_r2",
      "numLines": 80,
      "startLine": 100,
      "totalLines": 664
    }
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01V5j6ty17rP7r17Tm1TLAoS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "offset": 180,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "689c0f3e-1d65-4a38-9131-1fda4aa0c08f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165JBWakeiMEpaD4jmtR9zh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1234,
      "cache_read_input_tokens": 66007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1234
      },
      "output_tokens": 38,
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

_source line 71 · 2026-05-16T02:42:02.948Z_

<details><summary>↩ Tool result · `toolu_01V5j6ty17rP7r17Tm1TLAoS`</summary>

```text
180	    metric: v1 sdgd_zero F1=0.251, also below baseline
181	    tier: 1
182	  deprecated: false
183	- text: Cross-task controlled experiments. We present BCS-controlled experiments with
184	    bootstrap confidence intervals on three datasets, establishing that confusability
185	    effects amplify $3.4$ as schema size gro
186	  type: quantitative
187	  location:
188	    section: introduction
189	    context: result_statement
190	  id: C013
191	  evidence:
192	  - exp_id: exp_fewrel_formal_80rel
193	    metric: 3.4x amplification (80-rel vs 16-rel)
194	    tier: 1
195	  - exp_id: bootstrap_ci_analysis
196	    metric: FewRel count_8 delta CI [17.7, 42.7]
197	    tier: 1
198	  - exp_id: exp012_llama_fewrel_ch2
199	    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'
200	    tier: 1
201	  deprecated: false
202	- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise
203	    semantic overlap between types using embedding cosine similarity, and its batch
204	  type: methodological
205	  location:
206	    section: introduction
207	    context: finding_statement
208	  id: C014
209	  evidence:
210	  - exp_id: exp015_scs_validation
211	    metric: SCS validated as proxy for empirical confusion
212	    tier: 2
213	  deprecated: false
214	- text: We demonstrate that pairwise SCS predicts type confusion across tasks and
215	    embedding models, while identifying a centrality confound that invalidates per-type
216	    aggrega
217	  type: methodological
218	  location:
219	    section: introduction
220	    context: finding_statement
221	  id: C015
222	  evidence:
223	  - exp_id: exp002_confusability_controlled
224	    metric: Few-NERD pairwise r=0.112
225	    tier: 1
226	  - exp_id: exp004_maven_bcs
227	    metric: MAVEN centrality confound (per-type positive)
228	    tier: 1
229	  deprecated: false
230	- text: 95\\% CI
231	  type: quantitative
232	  location:
233	    section: results
234	    context: bold
235	  id: C016
236	  evidence:
237	  - exp_id: bootstrap_ci_analysis
238	    metric: 7 CIs all exclude null
239	    tier: 1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "b2d8b164-f0f8-47ab-8ae9-73c1ed19dbaa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
      "content": "    metric: v1 sdgd_zero F1=0.251, also below baseline\n    tier: 1\n  deprecated: false\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that confusability\n    effects amplify $3.4$ as schema size gro\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 3.4x amplification (80-rel vs 16-rel)\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\n    semantic overlap between types using embedding cosine similarity, and its batch\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C014\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: SCS validated as proxy for empirical confusion\n    tier: 2\n  deprecated: false\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\n    embedding models, while identifying a centrality confound that invalidates per-type\n    aggrega\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C015\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN centrality confound (per-type positive)\n    tier: 1\n  deprecated: false\n- text: 95\\\\% CI\n  type: quantitative\n  location:\n    section: results\n    context: bold\n  id: C016\n  evidence:\n  - exp_id: bootstrap_ci_analysis\n    metric: 7 CIs all exclude null\n    tier: 1",
      "numLines": 60,
      "startLine": 180,
      "totalLines": 664
    }
  }
}
```

</details>

---

### Assistant

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
Now I have the specific lines I need to edit. Let me also read the tables section and C033-C034 to get the exact content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "68dfc55f-3124-45f7-9b41-3a05b8cdaef6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BNVsdMmtQsbZjAKq22cu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 67241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 837
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

_source line 73_

找到了需要更新的 provenance 条目。读取 tables 部分和 C033-C034。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "fb70b263-3051-43df-8c13-09968d2b5c44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BNVsdMmtQsbZjAKq22cu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 67241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 837
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

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01JXzjFrNTV5kqzVF8rDKyfY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "offset": 370,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "a5e88d5c-8da4-4108-949e-fd4cf37c4462",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BNVsdMmtQsbZjAKq22cu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 67241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 837
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

### Tool result

_source line 75 · 2026-05-16T02:42:12.072Z_

<details><summary>↩ Tool result · `toolu_01JXzjFrNTV5kqzVF8rDKyfY`</summary>

```text
370	    context: result_statement
371	  id: C025
372	  evidence:
373	  - exp_id: exp007_error_taxonomy
374	    metric: NER IntraSub rho=1.0 (p<0.001)
375	    tier: 1
376	  - exp_id: exp016_fewrel_error_taxonomy
377	    metric: RE IntraSub rho=0.954 (p<1e-6)
378	    tier: 1
379	  deprecated: false
380	- text: The extreme-batch analysis sharpens this picture. At count${\\,=\\,6$, high-BCS
381	    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,
382	    versus $1.7$ under random batching. At
383	  type: quantitative
384	  location:
385	    section: results
386	    context: result_statement
387	  id: C026
388	  evidence:
389	  - exp_id: exp002_confusability_controlled
390	    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'
391	    tier: 1
392	  deprecated: false
393	- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean
394	    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and
395	    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'
396	  type: quantitative
397	  location:
398	    section: results
399	    context: result_statement
400	  id: C027
401	  evidence:
402	  - exp_id: exp004_maven_bcs
403	    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)
404	    tier: 1
405	  deprecated: false
406	- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN
407	    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with
408	    the values in Table~tab:pairwise. The problem'
409	  type: quantitative
410	  location:
411	    section: results
412	    context: result_statement
413	  id: C028
414	  evidence:
415	  - exp_id: exp004_maven_bcs
416	    metric: MAVEN MiniLM pairwise r=0.129
417	    tier: 1
418	  - exp_id: bootstrap_ci_analysis
419	    metric: CI [0.104, 0.156]
420	    tier: 1
421	  deprecated: false
422	- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,
423	    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =
424	    0.02$, $n = 63$), in the expected negative direc
425	  type: quantitative
426	  location:
427	    section: results
428	    context: result_statement
429	  id: C029
430	  evidence:
431	  - exp_id: exp002_confusability_controlled
432	    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)
433	    tier: 1
434	  deprecated: false
435	- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves
436	    F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368).  SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210,
437	    R\\,=\\,0.314), a 44\\% relative drop.  Rand
438	  type: quantitative
439	  location:
440	    section: sdgd_negative
441	    context: result_statement
442	  id: C030
443	  evidence:
444	  - exp_id: exp008_sdgd_zero_fewnerd_r2
445	    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197
446	    tier: 1
447	  deprecated: false
448	- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type
449	    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194
450	    versus 0.563).  The mechanism is straightfo'
451	  type: quantitative
452	  location:
453	    section: sdgd_negative
454	    context: result_statement
455	  id: C031
456	  evidence:
457	  - exp_id: exp008_sdgd_zero_fewnerd_r2
458	    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631
459	    tier: 1
460	  deprecated: false
461	- text: A natural remedy is to resolve merge conflicts using model confidence.  Our
462	    v2 merge ranks competing predictions by the LLM's self-reported confidence and
463	    retains only the highest-scoring candidate fo
464	  type: quantitative
465	  location:
466	    section: sdgd_negative
467	    context: result_statement
468	  id: C032
469	  evidence:
470	  - exp_id: exp008_sdgd_v2_fewnerd
471	    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve
472	    tier: 1
473	  deprecated: false
474	- id: C033
475	  location:
476	    section: results
477	    paragraph: 0
478	    sentence: 0
479	  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027
480	  type: quantitative
481	  evidence: []
482	  decisions: []
483	  deprecated: false
484	- id: C034
485	  location:
486	    section: results
487	    paragraph: 0
488	    sentence: 0
489	  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "2e7d2877-222f-4287-a219-127c98e4d1b7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
      "content": "    context: result_statement\n  id: C025\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub rho=1.0 (p<0.001)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub rho=0.954 (p<1e-6)\n    tier: 1\n  deprecated: false\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\,=\\\\,6$, high-BCS\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\n    versus $1.7$ under random batching. At\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C026\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\n    tier: 1\n  deprecated: false\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C027\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\n    the values in Table~tab:pairwise. The problem'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C028\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [0.104, 0.156]\n    tier: 1\n  deprecated: false\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\n    0.02$, $n = 63$), in the expected negative direc\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C029\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\n    tier: 1\n  deprecated: false\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\n    F1\\\\,=\\\\,0.445 (P\\\\,=\\\\,0.563, R\\\\,=\\\\,0.368).  SDGD obtains F1\\\\,=\\\\,0.251 (P\\\\,=\\\\,0.210,\n    R\\\\,=\\\\,0.314), a 44\\\\% relative drop.  Rand\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C030\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\n    tier: 1\n  deprecated: false\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\n    versus 0.563).  The mechanism is straightfo'\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C031\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\n    tier: 1\n  deprecated: false\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\n    retains only the highest-scoring candidate fo\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C032\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\n    tier: 1\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12",
      "numLines": 120,
      "startLine": 370,
      "totalLines": 664
    }
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Read · `toolu_01BFkAF2eNjp1fWzYbakCYhd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "offset": 488,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "b9d85c6b-cd05-42c7-bde7-4157d67923b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP6LBQDGZDu2hHVZbcwQpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 68078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1958
      },
      "output_tokens": 36,
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

_source line 77 · 2026-05-16T02:42:17.479Z_

<details><summary>↩ Tool result · `toolu_01BFkAF2eNjp1fWzYbakCYhd`</summary>

```text
488	    sentence: 0
489	  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12
490	  type: quantitative
491	  evidence: []
492	  decisions: []
493	  deprecated: false
494	- id: C035
495	  location:
496	    section: results
497	    paragraph: 0
498	    sentence: 0
499	  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered
500	  type: quantitative
501	  evidence: []
502	  decisions: []
503	  deprecated: false
504	- id: C036
505	  location:
506	    section: results
507	    paragraph: 0
508	    sentence: 0
509	  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]
510	  type: quantitative
511	  evidence: []
512	  decisions: []
513	  deprecated: false
514	- id: C037
515	  location:
516	    section: results
517	    paragraph: 0
518	    sentence: 0
519	  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]
520	  type: quantitative
521	  evidence: []
522	  decisions: []
523	  deprecated: false
524	- id: C038
525	  location:
526	    section: results
527	    paragraph: 0
528	    sentence: 0
529	  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]
530	  type: quantitative
531	  evidence: []
532	  decisions: []
533	  deprecated: false
534	- id: C039
535	  location:
536	    section: results
537	    paragraph: 0
538	    sentence: 0
539	  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)
540	  type: quantitative
541	  evidence: []
542	  decisions: []
543	  deprecated: false
544	tables:
545	- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability
546	    Scores across count-curve batches (Experiment~1). Embedding column indicates the
547	    model used for SCS/BCS computation.
548	  label: tab:datasets
549	  location:
550	    section: experimental_setup
551	  cells:
552	  - exp_id: exp001_count_baseline
553	    metric: Few-NERD 66 types
554	  - exp_id: exp-004
555	    metric: MAVEN 168 event types, 77993 train mentions
556	  - exp_id: exp_fewrel_formal_80rel
557	    metric: FewRel 80 relations
558	  id: T001
559	  deprecated: false
560	- caption: Pairwise SCS--confusion correlation.
561	  label: tab:pairwise
562	  location:
563	    section: results
564	  cells:
565	  - exp_id: exp002_confusability_controlled
566	    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]
567	  - exp_id: exp004_maven_bcs
568	    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]
569	  - exp_id: bootstrap_ci_analysis
570	    metric: bootstrap CIs for both
571	  id: T002
572	  deprecated: false
573	- caption: BCS-controlled FewRel accuracy.
574	  label: tab:bcs_controlled
575	  location:
576	    section: results
577	  cells:
578	  - exp_id: exp_fewrel_formal
579	    metric: '16-rel: delta=-9.1pp'
580	  - exp_id: exp_fewrel_formal_80rel
581	    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'
582	  - exp_id: exp_fewrel_40rel_r4
583	    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'
584	  - exp_id: exp012_llama_fewrel_ch2
585	    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'
586	  - exp_id: bootstrap_ci_analysis
587	    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'
588	  id: T003
589	  deprecated: false
590	- caption: Intra-batch substitution (IntraSub) rate by BCS bin.
591	  label: tab:error_taxonomy
592	  location:
593	    section: results
594	  cells:
595	  - exp_id: exp007_error_taxonomy
596	    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)
597	  - exp_id: exp016_fewrel_error_taxonomy
598	    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)
599	  id: T004
600	  deprecated: false
601	- caption: Few-NERD extraction under decomposition modes.
602	  label: tab:sdgd_results
603	  location:
604	    section: sdgd_negative
605	  cells:
606	  - exp_id: exp008_sdgd_zero_fewnerd_r2
607	    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "b9a61cd9-0fe0-4b90-9cff-a3de25dbb34a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
      "content": "    sentence: 0\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\ntables:\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\n    model used for SCS/BCS computation.\n  label: tab:datasets\n  location:\n    section: experimental_setup\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: Few-NERD 66 types\n  - exp_id: exp-004\n    metric: MAVEN 168 event types, 77993 train mentions\n  - exp_id: exp_fewrel_formal_80rel\n    metric: FewRel 80 relations\n  id: T001\n  deprecated: false\n- caption: Pairwise SCS--confusion correlation.\n  label: tab:pairwise\n  location:\n    section: results\n  cells:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n  - exp_id: bootstrap_ci_analysis\n    metric: bootstrap CIs for both\n  id: T002\n  deprecated: false\n- caption: BCS-controlled FewRel accuracy.\n  label: tab:bcs_controlled\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: delta=-9.1pp'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\n  - exp_id: bootstrap_ci_analysis\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\n  id: T003\n  deprecated: false\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\n  label: tab:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\n  id: T004\n  deprecated: false\n- caption: Few-NERD extraction under decomposition modes.\n  label: tab:sdgd_results\n  location:\n    section: sdgd_negative\n  cells:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type",
      "numLines": 120,
      "startLine": 488,
      "totalLines": 664
    }
  }
}
```

</details>

---

### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me make the edits:

1. **C010**: Update text and evidence to remove "3.4× amplification" language
2. **C013**: Update text and evidence to remove "3.4x amplification" language  
3. **C033**: Update CI from [-0.694, -0.057] to [-0.701, -0.069] (match paper table)
4. **C034**: Update CI from [-0.549, -0.345] to [-0.552, -0.346] (match paper table)
5. **Add T006**: for tab:within_pool with source from results_unified.json


6. I need to find the right spot in the tables section to insert T006.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "a919c897-8b84-469a-9569-a7716de30359",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DL3fkLfXPp8Uw8ETtNmKRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 70036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1852
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

_source line 79_

<details open><summary>🔧 Tool call — Read · `toolu_019kQRqC328c7Rw8FdcWhbUV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "offset": 607,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "2705561c-e42b-4a69-986f-734c97977c6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DL3fkLfXPp8Uw8ETtNmKRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 70036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1852
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

_source line 80 · 2026-05-16T02:42:27.372Z_

<details><summary>↩ Tool result · `toolu_019kQRqC328c7Rw8FdcWhbUV`</summary>

```text
607	    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type
608	      F1=0.292'
609	  - exp_id: exp008_sdgd_v2_fewnerd
610	    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'
611	  id: T005
612	  deprecated: false
613	figures:
614	- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)
615	  label: fig:count_curves
616	  location:
617	    section: results
618	  cells:
619	  - exp_id: exp001_count_baseline
620	    metric: 'Panel (a): recall 0.72->0.418'
621	  - exp_id: exp_fewrel_formal_80rel
622	    metric: 'Panel (b): accuracy 0.857->0.504'
623	  - exp_id: exp_fewrel_40rel_r4
624	    metric: 'Panel (b): count_40=0.588'
625	  id: F001
626	  deprecated: false
627	- caption: BCS effect scaling with pool size
628	  label: fig:bcs_scaling
629	  location:
630	    section: results
631	  cells:
632	  - exp_id: exp_fewrel_formal
633	    metric: 16-rel delta=9.1pp
634	  - exp_id: exp_fewrel_40rel_r4
635	    metric: 40-rel delta=33.3pp (80-pool subset)
636	  - exp_id: exp_fewrel_formal_80rel
637	    metric: 80-rel delta=31.2pp
638	  - exp_id: exp012_llama_fewrel_ch2
639	    metric: LLaMA 80-rel delta=27.1pp
640	  id: F002
641	  deprecated: false
642	- caption: Error taxonomy by BCS bin
643	  label: fig:error_taxonomy
644	  location:
645	    section: results
646	  cells:
647	  - exp_id: exp007_error_taxonomy
648	    metric: 'NER: IntraSub 0%->49.4%'
649	  - exp_id: exp016_fewrel_error_taxonomy
650	    metric: 'RE: IntraSub 0%->32.3%'
651	  id: F003
652	  deprecated: false
653	_completeness:
654	  coverage: 32/42
655	  claims: 39
656	  tables: 5
657	  figures: 3
658	  tier_counts:
659	    tier1: 0
660	    tier2: 32
661	    tier3: 10
662	    tierX: 0
663	  last_checked: '2026-05-16T02:22:29.529421+00:00'
664	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "9d27e326-4b2b-46f5-b37c-2828ecd1a694",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
      "content": "    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\n      F1=0.292'\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\n  id: T005\n  deprecated: false\nfigures:\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\n  label: fig:count_curves\n  location:\n    section: results\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: 'Panel (a): recall 0.72->0.418'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 'Panel (b): accuracy 0.857->0.504'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 'Panel (b): count_40=0.588'\n  id: F001\n  deprecated: false\n- caption: BCS effect scaling with pool size\n  label: fig:bcs_scaling\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=9.1pp\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 40-rel delta=33.3pp (80-pool subset)\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=31.2pp\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: LLaMA 80-rel delta=27.1pp\n  id: F002\n  deprecated: false\n- caption: Error taxonomy by BCS bin\n  label: fig:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: 'NER: IntraSub 0%->49.4%'\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: 'RE: IntraSub 0%->32.3%'\n  id: F003\n  deprecated: false\n_completeness:\n  coverage: 32/42\n  claims: 39\n  tables: 5\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 32\n    tier3: 10\n    tierX: 0\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\n",
      "numLines": 58,
      "startLine": 607,
      "totalLines": 664
    }
  }
}
```

</details>

---

### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me make the edits:

1. **C010** (lines 138-153): Update text and evidence metric to remove "amplify/amplification 3.4x"
2. **C013** (lines 183-201): Update text and evidence metric to remove "3.4x amplification"
3. **C033** (line 479): Update CI from [-0.694, -0.057] to [-0.701, -0.069]
4. **C034** (line 489): Update CI from [-0.549, -0.345] to [-0.552, -0.346]


5. **Add T006** after T005 (after line 612) for tab:within_pool
6. **Update _completeness** to reflect tables: 6

Let me apply these changes now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "d059334e-5b82-4f13-a22f-159ff4e5206d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTybdQ8YyYX3TB9epBkDLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 71888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1101
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

_source line 82_

现在执行 provenance 更新。需要修改 C010、C013（移除 3.4× amplification 语言）、C033/C034（CI 对齐论文表格）、添加 T006（within_pool 表），更新 completeness。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "bb6cfce7-4e37-4fa3-af92-217dfc571099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTybdQ8YyYX3TB9epBkDLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 71888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1101
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

_source line 83_

<details open><summary>🔧 Tool call — Edit · `toolu_01GLhW5SuMuUCTDPe5GKXS2z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "old_string": "- text: Third, confusability effects amplify with schema scale. In BCS-controlled\n    FewRel experiments, switching from low-confusability to high-confusability type\n    batches reduces accuracy by 9.1 percentage poi\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x\n    tier: 1\n  deprecated: false",
  "new_string": "- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy\n    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute gap\n    tier: 1\n  deprecated: false"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "c0d82a79-0bb5-4dc9-a58c-33824328e072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTybdQ8YyYX3TB9epBkDLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 71888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1101
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

_source line 84 · 2026-05-16T02:42:43.464Z_

<details><summary>↩ Tool result · `toolu_01GLhW5SuMuUCTDPe5GKXS2z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "db80d4b3-89a8-4807-8a1d-ef5b258a4459",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
    "oldString": "- text: Third, confusability effects amplify with schema scale. In BCS-controlled\n    FewRel experiments, switching from low-confusability to high-confusability type\n    batches reduces accuracy by 9.1 percentage poi\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x\n    tier: 1\n  deprecated: false",
    "newString": "- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy\n    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute gap\n    tier: 1\n  deprecated: false",
    "originalFile": "paper:\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free\n    LLM Information Extraction?\n  version: 3\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\n  source: manual mapping from registry + paper_framing.md\nclaims:\n- text: 'Training-free LLM information extraction---prompting models with target schemas\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\n    drops from 0.72 to 0.42 with 64 candidate '\n  type: quantitative\n  location:\n    section: abstract\n    context: result_statement\n  id: C001\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall count_1=0.720, count_64=0.418\n    tier: 1\n  deprecated: false\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\n    overlap between types and design two complementary experimental paradigms: count\n    cu'\n  type: methodological\n  location:\n    section: abstract\n    context: finding_statement\n  id: C002\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\n    tier: 1\n  deprecated: false\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\n    recall as candidate types increase, and'\n  type: quantitative\n  location:\n    section: conclusion\n    context: result_statement\n  id: C003\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: 'Channel 1: recall 0.72->0.418'\n    tier: 1\n  - exp_id: exp007_error_taxonomy\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub vs BCS rho=0.954\n    tier: 1\n  deprecated: false\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\n    capability, native structured JSON output support, and the practical advantage\n    that the FP8-quantized 32B model fits on a\n  type: quantitative\n  location:\n    section: experimental_setup\n    context: result_statement\n  id: C004\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\n    tier: 2\n  deprecated: false\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\n  type: methodological\n  location:\n    section: experimental_setup\n    context: finding_statement\n  id: C005\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\n    tier: 1\n  deprecated: false\n- text: Channel~1\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C006\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418 monotonic decline\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: accuracy 0.857->0.504 monotonic decline\n    tier: 1\n  deprecated: false\n- text: Channel~2\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C007\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS-controlled delta=-31.2pp\n    tier: 1\n  deprecated: false\n- text: Training-free LLM information extraction---prompting a large language model\n    with a target schema and asking it to extract structured information without any\n    task-specific fine-tuning---enables rapid d\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C008\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: background framing, supported by all experiments\n    tier: 3\n  deprecated: false\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\n    similarity between type pairs corre\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C009\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CIs exclude zero for both\n    tier: 1\n  deprecated: false\n- text: Third, confusability effects amplify with schema scale. In BCS-controlled\n    FewRel experiments, switching from low-confusability to high-confusability type\n    batches reduces accuracy by 9.1 percentage poi\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x\n    tier: 1\n  deprecated: false\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\n    between mean BCS and per-type er\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C011\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\n    into different batches, yet every decomp\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C012\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\n    tier: 1\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: v1 sdgd_zero F1=0.251, also below baseline\n    tier: 1\n  deprecated: false\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that confusability\n    effects amplify $3.4$ as schema size gro\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 3.4x amplification (80-rel vs 16-rel)\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\n    semantic overlap between types using embedding cosine similarity, and its batch\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C014\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: SCS validated as proxy for empirical confusion\n    tier: 2\n  deprecated: false\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\n    embedding models, while identifying a centrality confound that invalidates per-type\n    aggrega\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C015\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN centrality confound (per-type positive)\n    tier: 1\n  deprecated: false\n- text: 95\\\\% CI\n  type: quantitative\n  location:\n    section: results\n    context: bold\n  id: C016\n  evidence:\n  - exp_id: bootstrap_ci_analysis\n    metric: 7 CIs all exclude null\n    tier: 1\n  deprecated: false\n- text: Recall declines monotonically from 0.72 at count${\\\\,=\\\\,1$ to 0.42 at count${\\\\,=\\\\,64$,\n    a 42\\\\% relative drop. Precision moves in the opposite direction, rising from\n    0.11 to 0.52, reflecting a shift from\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C017\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418, precision 0.105->0.52\n    tier: 1\n  deprecated: false\n- text: Accuracy drops monotonically from 85.7\\\\% at count${\\\\,=\\\\,1$ to 50.4\\\\% at\n    count${\\\\,=\\\\,80$, a near-halving when the model must discriminate among all 80\n    relation types simultaneously.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C018\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\n    tier: 1\n  deprecated: false\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\,=\\\\,1$\n    to 0.247 at count${\\\\,=\\\\,44$. This reversal arises from three properties of the\n    MAVEN setup: (i)~trigger-level relaxed'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C019\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\n    tier: 1\n  deprecated: false\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\%$, meaning pairwise confusability\n    explains roughly 1.5\\\\% of the variance in type confusion. Other factors---entity\n    frequency, prompt position effects lost-'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C020\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN pairwise r=0.129, r2=1.66%\n    tier: 1\n  deprecated: false\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\n    and MiniLM yields $ = 0.144$ ($p\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C021\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\n    tier: 1\n  deprecated: false\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\n    types; high-BCS batches contain maximally similar types. The confusability gap\n    widens from 9.1\\\\,pp at 16 relations to 31.2\\\\\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C022\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\n    tier: 1\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\n    tier: 1\n  deprecated: false\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\n    this gap to 31.2\\\\,pp (95\\\\% CI: [17.7, 42.'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C023\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=-31.2pp\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\n    tier: 1\n  deprecated: false\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C024\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\n      flat)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\n    tier: 1\n  deprecated: false\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\n    with BCS in both tasks: NER IntraSub rises from 0\\\\% (solo) to 49.4\\\\% (high BCS)\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C025\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub rho=1.0 (p<0.001)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub rho=0.954 (p<1e-6)\n    tier: 1\n  deprecated: false\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\,=\\\\,6$, high-BCS\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\n    versus $1.7$ under random batching. At\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C026\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\n    tier: 1\n  deprecated: false\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C027\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\n    the values in Table~tab:pairwise. The problem'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C028\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [0.104, 0.156]\n    tier: 1\n  deprecated: false\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\n    0.02$, $n = 63$), in the expected negative direc\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C029\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\n    tier: 1\n  deprecated: false\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\n    F1\\\\,=\\\\,0.445 (P\\\\,=\\\\,0.563, R\\\\,=\\\\,0.368).  SDGD obtains F1\\\\,=\\\\,0.251 (P\\\\,=\\\\,0.210,\n    R\\\\,=\\\\,0.314), a 44\\\\% relative drop.  Rand\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C030\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\n    tier: 1\n  deprecated: false\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\n    versus 0.563).  The mechanism is straightfo'\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C031\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\n    tier: 1\n  deprecated: false\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\n    retains only the highest-scoring candidate fo\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C032\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\n    tier: 1\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\ntables:\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\n    model used for SCS/BCS computation.\n  label: tab:datasets\n  location:\n    section: experimental_setup\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: Few-NERD 66 types\n  - exp_id: exp-004\n    metric: MAVEN 168 event types, 77993 train mentions\n  - exp_id: exp_fewrel_formal_80rel\n    metric: FewRel 80 relations\n  id: T001\n  deprecated: false\n- caption: Pairwise SCS--confusion correlation.\n  label: tab:pairwise\n  location:\n    section: results\n  cells:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n  - exp_id: bootstrap_ci_analysis\n    metric: bootstrap CIs for both\n  id: T002\n  deprecated: false\n- caption: BCS-controlled FewRel accuracy.\n  label: tab:bcs_controlled\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: delta=-9.1pp'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\n  - exp_id: bootstrap_ci_analysis\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\n  id: T003\n  deprecated: false\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\n  label: tab:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\n  id: T004\n  deprecated: false\n- caption: Few-NERD extraction under decomposition modes.\n  label: tab:sdgd_results\n  location:\n    section: sdgd_negative\n  cells:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\n      F1=0.292'\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\n  id: T005\n  deprecated: false\nfigures:\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\n  label: fig:count_curves\n  location:\n    section: results\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: 'Panel (a): recall 0.72->0.418'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 'Panel (b): accuracy 0.857->0.504'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 'Panel (b): count_40=0.588'\n  id: F001\n  deprecated: false\n- caption: BCS effect scaling with pool size\n  label: fig:bcs_scaling\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=9.1pp\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 40-rel delta=33.3pp (80-pool subset)\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=31.2pp\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: LLaMA 80-rel delta=27.1pp\n  id: F002\n  deprecated: false\n- caption: Error taxonomy by BCS bin\n  label: fig:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: 'NER: IntraSub 0%->49.4%'\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: 'RE: IntraSub 0%->32.3%'\n  id: F003\n  deprecated: false\n_completeness:\n  coverage: 32/42\n  claims: 39\n  tables: 5\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 32\n    tier3: 10\n    tierX: 0\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 135,
        "oldLines": 9,
        "newStart": 135,
        "newLines": 8,
        "lines": [
          "     metric: CIs exclude zero for both",
          "     tier: 1",
          "   deprecated: false",
          "-- text: Third, confusability effects amplify with schema scale. In BCS-controlled",
          "-    FewRel experiments, switching from low-confusability to high-confusability type",
          "-    batches reduces accuracy by 9.1 percentage poi",
          "+- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy",
          "+    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)",
          "   type: quantitative",
          "   location:",
          "     section: introduction"
        ]
      },
      {
        "oldStart": 148,
        "oldLines": 7,
        "newStart": 147,
        "newLines": 7,
        "lines": [
          "     metric: 16-rel BCS effect delta=-9.1pp",
          "     tier: 1",
          "   - exp_id: exp_fewrel_formal_80rel",
          "-    metric: 80-rel BCS effect delta=-31.2pp, amplification 3.4x",
          "+    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute gap",
          "     tier: 1",
          "   deprecated: false",
          " - text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Edit · `toolu_01Lzn8TyzvK5fE3KSGXC5im3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "old_string": "- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that confusability\n    effects amplify $3.4$ as schema size gro\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 3.4x amplification (80-rel vs 16-rel)\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false",
  "new_string": "- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy\n    relationship is consistent across schema sizes (slope permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS--accuracy slope consistent across pools, permutation p=0.436\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "8e9eef7f-c43b-4173-ad22-5a2ee378eb38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTybdQ8YyYX3TB9epBkDLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 71888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1101
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

_source line 86 · 2026-05-16T02:42:51.058Z_

<details><summary>↩ Tool result · `toolu_01Lzn8TyzvK5fE3KSGXC5im3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "6d92ec27-4711-4f03-b8eb-7f495b625bc3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
    "oldString": "- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that confusability\n    effects amplify $3.4$ as schema size gro\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 3.4x amplification (80-rel vs 16-rel)\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false",
    "newString": "- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy\n    relationship is consistent across schema sizes (slope permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS--accuracy slope consistent across pools, permutation p=0.436\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false",
    "originalFile": "paper:\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free\n    LLM Information Extraction?\n  version: 3\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\n  source: manual mapping from registry + paper_framing.md\nclaims:\n- text: 'Training-free LLM information extraction---prompting models with target schemas\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\n    drops from 0.72 to 0.42 with 64 candidate '\n  type: quantitative\n  location:\n    section: abstract\n    context: result_statement\n  id: C001\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall count_1=0.720, count_64=0.418\n    tier: 1\n  deprecated: false\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\n    overlap between types and design two complementary experimental paradigms: count\n    cu'\n  type: methodological\n  location:\n    section: abstract\n    context: finding_statement\n  id: C002\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\n    tier: 1\n  deprecated: false\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\n    recall as candidate types increase, and'\n  type: quantitative\n  location:\n    section: conclusion\n    context: result_statement\n  id: C003\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: 'Channel 1: recall 0.72->0.418'\n    tier: 1\n  - exp_id: exp007_error_taxonomy\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub vs BCS rho=0.954\n    tier: 1\n  deprecated: false\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\n    capability, native structured JSON output support, and the practical advantage\n    that the FP8-quantized 32B model fits on a\n  type: quantitative\n  location:\n    section: experimental_setup\n    context: result_statement\n  id: C004\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\n    tier: 2\n  deprecated: false\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\n  type: methodological\n  location:\n    section: experimental_setup\n    context: finding_statement\n  id: C005\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\n    tier: 1\n  deprecated: false\n- text: Channel~1\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C006\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418 monotonic decline\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: accuracy 0.857->0.504 monotonic decline\n    tier: 1\n  deprecated: false\n- text: Channel~2\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C007\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS-controlled delta=-31.2pp\n    tier: 1\n  deprecated: false\n- text: Training-free LLM information extraction---prompting a large language model\n    with a target schema and asking it to extract structured information without any\n    task-specific fine-tuning---enables rapid d\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C008\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: background framing, supported by all experiments\n    tier: 3\n  deprecated: false\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\n    similarity between type pairs corre\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C009\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CIs exclude zero for both\n    tier: 1\n  deprecated: false\n- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy\n    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute gap\n    tier: 1\n  deprecated: false\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\n    between mean BCS and per-type er\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C011\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\n    into different batches, yet every decomp\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C012\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\n    tier: 1\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: v1 sdgd_zero F1=0.251, also below baseline\n    tier: 1\n  deprecated: false\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that confusability\n    effects amplify $3.4$ as schema size gro\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 3.4x amplification (80-rel vs 16-rel)\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\n    semantic overlap between types using embedding cosine similarity, and its batch\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C014\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: SCS validated as proxy for empirical confusion\n    tier: 2\n  deprecated: false\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\n    embedding models, while identifying a centrality confound that invalidates per-type\n    aggrega\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C015\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN centrality confound (per-type positive)\n    tier: 1\n  deprecated: false\n- text: 95\\\\% CI\n  type: quantitative\n  location:\n    section: results\n    context: bold\n  id: C016\n  evidence:\n  - exp_id: bootstrap_ci_analysis\n    metric: 7 CIs all exclude null\n    tier: 1\n  deprecated: false\n- text: Recall declines monotonically from 0.72 at count${\\\\,=\\\\,1$ to 0.42 at count${\\\\,=\\\\,64$,\n    a 42\\\\% relative drop. Precision moves in the opposite direction, rising from\n    0.11 to 0.52, reflecting a shift from\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C017\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418, precision 0.105->0.52\n    tier: 1\n  deprecated: false\n- text: Accuracy drops monotonically from 85.7\\\\% at count${\\\\,=\\\\,1$ to 50.4\\\\% at\n    count${\\\\,=\\\\,80$, a near-halving when the model must discriminate among all 80\n    relation types simultaneously.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C018\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\n    tier: 1\n  deprecated: false\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\,=\\\\,1$\n    to 0.247 at count${\\\\,=\\\\,44$. This reversal arises from three properties of the\n    MAVEN setup: (i)~trigger-level relaxed'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C019\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\n    tier: 1\n  deprecated: false\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\%$, meaning pairwise confusability\n    explains roughly 1.5\\\\% of the variance in type confusion. Other factors---entity\n    frequency, prompt position effects lost-'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C020\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN pairwise r=0.129, r2=1.66%\n    tier: 1\n  deprecated: false\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\n    and MiniLM yields $ = 0.144$ ($p\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C021\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\n    tier: 1\n  deprecated: false\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\n    types; high-BCS batches contain maximally similar types. The confusability gap\n    widens from 9.1\\\\,pp at 16 relations to 31.2\\\\\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C022\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\n    tier: 1\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\n    tier: 1\n  deprecated: false\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\n    this gap to 31.2\\\\,pp (95\\\\% CI: [17.7, 42.'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C023\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=-31.2pp\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\n    tier: 1\n  deprecated: false\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C024\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\n      flat)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\n    tier: 1\n  deprecated: false\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\n    with BCS in both tasks: NER IntraSub rises from 0\\\\% (solo) to 49.4\\\\% (high BCS)\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C025\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub rho=1.0 (p<0.001)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub rho=0.954 (p<1e-6)\n    tier: 1\n  deprecated: false\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\,=\\\\,6$, high-BCS\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\n    versus $1.7$ under random batching. At\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C026\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\n    tier: 1\n  deprecated: false\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C027\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\n    the values in Table~tab:pairwise. The problem'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C028\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [0.104, 0.156]\n    tier: 1\n  deprecated: false\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\n    0.02$, $n = 63$), in the expected negative direc\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C029\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\n    tier: 1\n  deprecated: false\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\n    F1\\\\,=\\\\,0.445 (P\\\\,=\\\\,0.563, R\\\\,=\\\\,0.368).  SDGD obtains F1\\\\,=\\\\,0.251 (P\\\\,=\\\\,0.210,\n    R\\\\,=\\\\,0.314), a 44\\\\% relative drop.  Rand\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C030\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\n    tier: 1\n  deprecated: false\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\n    versus 0.563).  The mechanism is straightfo'\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C031\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\n    tier: 1\n  deprecated: false\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\n    retains only the highest-scoring candidate fo\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C032\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\n    tier: 1\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\ntables:\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\n    model used for SCS/BCS computation.\n  label: tab:datasets\n  location:\n    section: experimental_setup\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: Few-NERD 66 types\n  - exp_id: exp-004\n    metric: MAVEN 168 event types, 77993 train mentions\n  - exp_id: exp_fewrel_formal_80rel\n    metric: FewRel 80 relations\n  id: T001\n  deprecated: false\n- caption: Pairwise SCS--confusion correlation.\n  label: tab:pairwise\n  location:\n    section: results\n  cells:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n  - exp_id: bootstrap_ci_analysis\n    metric: bootstrap CIs for both\n  id: T002\n  deprecated: false\n- caption: BCS-controlled FewRel accuracy.\n  label: tab:bcs_controlled\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: delta=-9.1pp'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\n  - exp_id: bootstrap_ci_analysis\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\n  id: T003\n  deprecated: false\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\n  label: tab:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\n  id: T004\n  deprecated: false\n- caption: Few-NERD extraction under decomposition modes.\n  label: tab:sdgd_results\n  location:\n    section: sdgd_negative\n  cells:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\n      F1=0.292'\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\n  id: T005\n  deprecated: false\nfigures:\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\n  label: fig:count_curves\n  location:\n    section: results\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: 'Panel (a): recall 0.72->0.418'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 'Panel (b): accuracy 0.857->0.504'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 'Panel (b): count_40=0.588'\n  id: F001\n  deprecated: false\n- caption: BCS effect scaling with pool size\n  label: fig:bcs_scaling\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=9.1pp\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 40-rel delta=33.3pp (80-pool subset)\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=31.2pp\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: LLaMA 80-rel delta=27.1pp\n  id: F002\n  deprecated: false\n- caption: Error taxonomy by BCS bin\n  label: fig:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: 'NER: IntraSub 0%->49.4%'\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: 'RE: IntraSub 0%->32.3%'\n  id: F003\n  deprecated: false\n_completeness:\n  coverage: 32/42\n  claims: 39\n  tables: 5\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 32\n    tier3: 10\n    tierX: 0\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 180,
        "oldLines": 8,
        "newStart": 180,
        "newLines": 8,
        "lines": [
          "     tier: 1",
          "   deprecated: false",
          " - text: Cross-task controlled experiments. We present BCS-controlled experiments with",
          "-    bootstrap confidence intervals on three datasets, establishing that confusability",
          "-    effects amplify $3.4$ as schema size gro",
          "+    bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy",
          "+    relationship is consistent across schema sizes (slope permutation p = 0.44)",
          "   type: quantitative",
          "   location:",
          "     section: introduction"
        ]
      },
      {
        "oldStart": 189,
        "oldLines": 7,
        "newStart": 189,
        "newLines": 7,
        "lines": [
          "   id: C013",
          "   evidence:",
          "   - exp_id: exp_fewrel_formal_80rel",
          "-    metric: 3.4x amplification (80-rel vs 16-rel)",
          "+    metric: BCS--accuracy slope consistent across pools, permutation p=0.436",
          "     tier: 1",
          "   - exp_id: bootstrap_ci_analysis",
          "     metric: FewRel count_8 delta CI [17.7, 42.7]"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Edit · `toolu_017C91oxm6oJGHcRjR6f6B5Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "old_string": "  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027",
  "new_string": "  text: 80-pool→16-sub slope = -0.401, CI [-0.701, -0.069], r = -0.221, p = 0.027"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "b7009b02-a045-4217-9185-02e18f2cae18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTybdQ8YyYX3TB9epBkDLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 71888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1101
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

_source line 88 · 2026-05-16T02:42:53.331Z_

<details><summary>↩ Tool result · `toolu_017C91oxm6oJGHcRjR6f6B5Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "50f6dc3d-4d1f-4ae9-9527-823cb9316ed0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
    "oldString": "  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027",
    "newString": "  text: 80-pool→16-sub slope = -0.401, CI [-0.701, -0.069], r = -0.221, p = 0.027",
    "originalFile": "paper:\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free\n    LLM Information Extraction?\n  version: 3\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\n  source: manual mapping from registry + paper_framing.md\nclaims:\n- text: 'Training-free LLM information extraction---prompting models with target schemas\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\n    drops from 0.72 to 0.42 with 64 candidate '\n  type: quantitative\n  location:\n    section: abstract\n    context: result_statement\n  id: C001\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall count_1=0.720, count_64=0.418\n    tier: 1\n  deprecated: false\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\n    overlap between types and design two complementary experimental paradigms: count\n    cu'\n  type: methodological\n  location:\n    section: abstract\n    context: finding_statement\n  id: C002\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\n    tier: 1\n  deprecated: false\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\n    recall as candidate types increase, and'\n  type: quantitative\n  location:\n    section: conclusion\n    context: result_statement\n  id: C003\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: 'Channel 1: recall 0.72->0.418'\n    tier: 1\n  - exp_id: exp007_error_taxonomy\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub vs BCS rho=0.954\n    tier: 1\n  deprecated: false\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\n    capability, native structured JSON output support, and the practical advantage\n    that the FP8-quantized 32B model fits on a\n  type: quantitative\n  location:\n    section: experimental_setup\n    context: result_statement\n  id: C004\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\n    tier: 2\n  deprecated: false\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\n  type: methodological\n  location:\n    section: experimental_setup\n    context: finding_statement\n  id: C005\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\n    tier: 1\n  deprecated: false\n- text: Channel~1\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C006\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418 monotonic decline\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: accuracy 0.857->0.504 monotonic decline\n    tier: 1\n  deprecated: false\n- text: Channel~2\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C007\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS-controlled delta=-31.2pp\n    tier: 1\n  deprecated: false\n- text: Training-free LLM information extraction---prompting a large language model\n    with a target schema and asking it to extract structured information without any\n    task-specific fine-tuning---enables rapid d\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C008\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: background framing, supported by all experiments\n    tier: 3\n  deprecated: false\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\n    similarity between type pairs corre\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C009\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CIs exclude zero for both\n    tier: 1\n  deprecated: false\n- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy\n    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute gap\n    tier: 1\n  deprecated: false\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\n    between mean BCS and per-type er\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C011\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\n    into different batches, yet every decomp\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C012\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\n    tier: 1\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: v1 sdgd_zero F1=0.251, also below baseline\n    tier: 1\n  deprecated: false\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy\n    relationship is consistent across schema sizes (slope permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS--accuracy slope consistent across pools, permutation p=0.436\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\n    semantic overlap between types using embedding cosine similarity, and its batch\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C014\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: SCS validated as proxy for empirical confusion\n    tier: 2\n  deprecated: false\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\n    embedding models, while identifying a centrality confound that invalidates per-type\n    aggrega\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C015\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN centrality confound (per-type positive)\n    tier: 1\n  deprecated: false\n- text: 95\\\\% CI\n  type: quantitative\n  location:\n    section: results\n    context: bold\n  id: C016\n  evidence:\n  - exp_id: bootstrap_ci_analysis\n    metric: 7 CIs all exclude null\n    tier: 1\n  deprecated: false\n- text: Recall declines monotonically from 0.72 at count${\\\\,=\\\\,1$ to 0.42 at count${\\\\,=\\\\,64$,\n    a 42\\\\% relative drop. Precision moves in the opposite direction, rising from\n    0.11 to 0.52, reflecting a shift from\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C017\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418, precision 0.105->0.52\n    tier: 1\n  deprecated: false\n- text: Accuracy drops monotonically from 85.7\\\\% at count${\\\\,=\\\\,1$ to 50.4\\\\% at\n    count${\\\\,=\\\\,80$, a near-halving when the model must discriminate among all 80\n    relation types simultaneously.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C018\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\n    tier: 1\n  deprecated: false\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\,=\\\\,1$\n    to 0.247 at count${\\\\,=\\\\,44$. This reversal arises from three properties of the\n    MAVEN setup: (i)~trigger-level relaxed'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C019\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\n    tier: 1\n  deprecated: false\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\%$, meaning pairwise confusability\n    explains roughly 1.5\\\\% of the variance in type confusion. Other factors---entity\n    frequency, prompt position effects lost-'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C020\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN pairwise r=0.129, r2=1.66%\n    tier: 1\n  deprecated: false\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\n    and MiniLM yields $ = 0.144$ ($p\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C021\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\n    tier: 1\n  deprecated: false\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\n    types; high-BCS batches contain maximally similar types. The confusability gap\n    widens from 9.1\\\\,pp at 16 relations to 31.2\\\\\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C022\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\n    tier: 1\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\n    tier: 1\n  deprecated: false\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\n    this gap to 31.2\\\\,pp (95\\\\% CI: [17.7, 42.'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C023\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=-31.2pp\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\n    tier: 1\n  deprecated: false\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C024\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\n      flat)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\n    tier: 1\n  deprecated: false\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\n    with BCS in both tasks: NER IntraSub rises from 0\\\\% (solo) to 49.4\\\\% (high BCS)\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C025\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub rho=1.0 (p<0.001)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub rho=0.954 (p<1e-6)\n    tier: 1\n  deprecated: false\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\,=\\\\,6$, high-BCS\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\n    versus $1.7$ under random batching. At\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C026\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\n    tier: 1\n  deprecated: false\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C027\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\n    the values in Table~tab:pairwise. The problem'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C028\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [0.104, 0.156]\n    tier: 1\n  deprecated: false\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\n    0.02$, $n = 63$), in the expected negative direc\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C029\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\n    tier: 1\n  deprecated: false\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\n    F1\\\\,=\\\\,0.445 (P\\\\,=\\\\,0.563, R\\\\,=\\\\,0.368).  SDGD obtains F1\\\\,=\\\\,0.251 (P\\\\,=\\\\,0.210,\n    R\\\\,=\\\\,0.314), a 44\\\\% relative drop.  Rand\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C030\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\n    tier: 1\n  deprecated: false\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\n    versus 0.563).  The mechanism is straightfo'\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C031\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\n    tier: 1\n  deprecated: false\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\n    retains only the highest-scoring candidate fo\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C032\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\n    tier: 1\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\ntables:\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\n    model used for SCS/BCS computation.\n  label: tab:datasets\n  location:\n    section: experimental_setup\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: Few-NERD 66 types\n  - exp_id: exp-004\n    metric: MAVEN 168 event types, 77993 train mentions\n  - exp_id: exp_fewrel_formal_80rel\n    metric: FewRel 80 relations\n  id: T001\n  deprecated: false\n- caption: Pairwise SCS--confusion correlation.\n  label: tab:pairwise\n  location:\n    section: results\n  cells:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n  - exp_id: bootstrap_ci_analysis\n    metric: bootstrap CIs for both\n  id: T002\n  deprecated: false\n- caption: BCS-controlled FewRel accuracy.\n  label: tab:bcs_controlled\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: delta=-9.1pp'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\n  - exp_id: bootstrap_ci_analysis\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\n  id: T003\n  deprecated: false\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\n  label: tab:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\n  id: T004\n  deprecated: false\n- caption: Few-NERD extraction under decomposition modes.\n  label: tab:sdgd_results\n  location:\n    section: sdgd_negative\n  cells:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\n      F1=0.292'\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\n  id: T005\n  deprecated: false\nfigures:\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\n  label: fig:count_curves\n  location:\n    section: results\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: 'Panel (a): recall 0.72->0.418'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 'Panel (b): accuracy 0.857->0.504'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 'Panel (b): count_40=0.588'\n  id: F001\n  deprecated: false\n- caption: BCS effect scaling with pool size\n  label: fig:bcs_scaling\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=9.1pp\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 40-rel delta=33.3pp (80-pool subset)\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=31.2pp\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: LLaMA 80-rel delta=27.1pp\n  id: F002\n  deprecated: false\n- caption: Error taxonomy by BCS bin\n  label: fig:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: 'NER: IntraSub 0%->49.4%'\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: 'RE: IntraSub 0%->32.3%'\n  id: F003\n  deprecated: false\n_completeness:\n  coverage: 32/42\n  claims: 39\n  tables: 5\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 32\n    tier3: 10\n    tierX: 0\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 475,
        "oldLines": 7,
        "newStart": 475,
        "newLines": 7,
        "lines": [
          "     section: results",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: 80-pool→16-sub slope = -0.401, CI [-0.694, -0.057], r = -0.221, p = 0.027",
          "+  text: 80-pool→16-sub slope = -0.401, CI [-0.701, -0.069], r = -0.221, p = 0.027",
          "   type: quantitative",
          "   evidence: []",
          "   decisions: []"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Edit · `toolu_01VU7FPUKPvNZTiAr1UZYhpN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "old_string": "  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12",
  "new_string": "  text: Independent 16-rel slope = -0.449, CI [-0.552, -0.346], r = -0.637, p < 1e-12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "8d08b229-e0da-42d0-8b51-a1a04fcd1257",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTybdQ8YyYX3TB9epBkDLM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 71888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1101
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

_source line 90 · 2026-05-16T02:42:54.924Z_

<details><summary>↩ Tool result · `toolu_01VU7FPUKPvNZTiAr1UZYhpN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "5fe4cc63-0df3-4aee-a10a-4abaa3c10748",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
    "oldString": "  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12",
    "newString": "  text: Independent 16-rel slope = -0.449, CI [-0.552, -0.346], r = -0.637, p < 1e-12",
    "originalFile": "paper:\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free\n    LLM Information Extraction?\n  version: 3\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\n  source: manual mapping from registry + paper_framing.md\nclaims:\n- text: 'Training-free LLM information extraction---prompting models with target schemas\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\n    drops from 0.72 to 0.42 with 64 candidate '\n  type: quantitative\n  location:\n    section: abstract\n    context: result_statement\n  id: C001\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall count_1=0.720, count_64=0.418\n    tier: 1\n  deprecated: false\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\n    overlap between types and design two complementary experimental paradigms: count\n    cu'\n  type: methodological\n  location:\n    section: abstract\n    context: finding_statement\n  id: C002\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\n    tier: 1\n  deprecated: false\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\n    recall as candidate types increase, and'\n  type: quantitative\n  location:\n    section: conclusion\n    context: result_statement\n  id: C003\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: 'Channel 1: recall 0.72->0.418'\n    tier: 1\n  - exp_id: exp007_error_taxonomy\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub vs BCS rho=0.954\n    tier: 1\n  deprecated: false\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\n    capability, native structured JSON output support, and the practical advantage\n    that the FP8-quantized 32B model fits on a\n  type: quantitative\n  location:\n    section: experimental_setup\n    context: result_statement\n  id: C004\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\n    tier: 2\n  deprecated: false\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\n  type: methodological\n  location:\n    section: experimental_setup\n    context: finding_statement\n  id: C005\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\n    tier: 1\n  deprecated: false\n- text: Channel~1\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C006\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418 monotonic decline\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: accuracy 0.857->0.504 monotonic decline\n    tier: 1\n  deprecated: false\n- text: Channel~2\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C007\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS-controlled delta=-31.2pp\n    tier: 1\n  deprecated: false\n- text: Training-free LLM information extraction---prompting a large language model\n    with a target schema and asking it to extract structured information without any\n    task-specific fine-tuning---enables rapid d\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C008\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: background framing, supported by all experiments\n    tier: 3\n  deprecated: false\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\n    similarity between type pairs corre\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C009\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CIs exclude zero for both\n    tier: 1\n  deprecated: false\n- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy\n    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute gap\n    tier: 1\n  deprecated: false\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\n    between mean BCS and per-type er\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C011\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\n    into different batches, yet every decomp\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C012\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\n    tier: 1\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: v1 sdgd_zero F1=0.251, also below baseline\n    tier: 1\n  deprecated: false\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy\n    relationship is consistent across schema sizes (slope permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS--accuracy slope consistent across pools, permutation p=0.436\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\n    semantic overlap between types using embedding cosine similarity, and its batch\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C014\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: SCS validated as proxy for empirical confusion\n    tier: 2\n  deprecated: false\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\n    embedding models, while identifying a centrality confound that invalidates per-type\n    aggrega\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C015\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN centrality confound (per-type positive)\n    tier: 1\n  deprecated: false\n- text: 95\\\\% CI\n  type: quantitative\n  location:\n    section: results\n    context: bold\n  id: C016\n  evidence:\n  - exp_id: bootstrap_ci_analysis\n    metric: 7 CIs all exclude null\n    tier: 1\n  deprecated: false\n- text: Recall declines monotonically from 0.72 at count${\\\\,=\\\\,1$ to 0.42 at count${\\\\,=\\\\,64$,\n    a 42\\\\% relative drop. Precision moves in the opposite direction, rising from\n    0.11 to 0.52, reflecting a shift from\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C017\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418, precision 0.105->0.52\n    tier: 1\n  deprecated: false\n- text: Accuracy drops monotonically from 85.7\\\\% at count${\\\\,=\\\\,1$ to 50.4\\\\% at\n    count${\\\\,=\\\\,80$, a near-halving when the model must discriminate among all 80\n    relation types simultaneously.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C018\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\n    tier: 1\n  deprecated: false\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\,=\\\\,1$\n    to 0.247 at count${\\\\,=\\\\,44$. This reversal arises from three properties of the\n    MAVEN setup: (i)~trigger-level relaxed'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C019\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\n    tier: 1\n  deprecated: false\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\%$, meaning pairwise confusability\n    explains roughly 1.5\\\\% of the variance in type confusion. Other factors---entity\n    frequency, prompt position effects lost-'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C020\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN pairwise r=0.129, r2=1.66%\n    tier: 1\n  deprecated: false\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\n    and MiniLM yields $ = 0.144$ ($p\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C021\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\n    tier: 1\n  deprecated: false\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\n    types; high-BCS batches contain maximally similar types. The confusability gap\n    widens from 9.1\\\\,pp at 16 relations to 31.2\\\\\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C022\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\n    tier: 1\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\n    tier: 1\n  deprecated: false\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\n    this gap to 31.2\\\\,pp (95\\\\% CI: [17.7, 42.'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C023\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=-31.2pp\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\n    tier: 1\n  deprecated: false\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C024\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\n      flat)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\n    tier: 1\n  deprecated: false\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\n    with BCS in both tasks: NER IntraSub rises from 0\\\\% (solo) to 49.4\\\\% (high BCS)\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C025\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub rho=1.0 (p<0.001)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub rho=0.954 (p<1e-6)\n    tier: 1\n  deprecated: false\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\,=\\\\,6$, high-BCS\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\n    versus $1.7$ under random batching. At\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C026\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\n    tier: 1\n  deprecated: false\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C027\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\n    the values in Table~tab:pairwise. The problem'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C028\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [0.104, 0.156]\n    tier: 1\n  deprecated: false\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\n    0.02$, $n = 63$), in the expected negative direc\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C029\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\n    tier: 1\n  deprecated: false\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\n    F1\\\\,=\\\\,0.445 (P\\\\,=\\\\,0.563, R\\\\,=\\\\,0.368).  SDGD obtains F1\\\\,=\\\\,0.251 (P\\\\,=\\\\,0.210,\n    R\\\\,=\\\\,0.314), a 44\\\\% relative drop.  Rand\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C030\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\n    tier: 1\n  deprecated: false\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\n    versus 0.563).  The mechanism is straightfo'\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C031\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\n    tier: 1\n  deprecated: false\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\n    retains only the highest-scoring candidate fo\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C032\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\n    tier: 1\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub slope = -0.401, CI [-0.701, -0.069], r = -0.221, p = 0.027\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\ntables:\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\n    model used for SCS/BCS computation.\n  label: tab:datasets\n  location:\n    section: experimental_setup\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: Few-NERD 66 types\n  - exp_id: exp-004\n    metric: MAVEN 168 event types, 77993 train mentions\n  - exp_id: exp_fewrel_formal_80rel\n    metric: FewRel 80 relations\n  id: T001\n  deprecated: false\n- caption: Pairwise SCS--confusion correlation.\n  label: tab:pairwise\n  location:\n    section: results\n  cells:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n  - exp_id: bootstrap_ci_analysis\n    metric: bootstrap CIs for both\n  id: T002\n  deprecated: false\n- caption: BCS-controlled FewRel accuracy.\n  label: tab:bcs_controlled\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: delta=-9.1pp'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\n  - exp_id: bootstrap_ci_analysis\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\n  id: T003\n  deprecated: false\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\n  label: tab:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\n  id: T004\n  deprecated: false\n- caption: Few-NERD extraction under decomposition modes.\n  label: tab:sdgd_results\n  location:\n    section: sdgd_negative\n  cells:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\n      F1=0.292'\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\n  id: T005\n  deprecated: false\nfigures:\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\n  label: fig:count_curves\n  location:\n    section: results\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: 'Panel (a): recall 0.72->0.418'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 'Panel (b): accuracy 0.857->0.504'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 'Panel (b): count_40=0.588'\n  id: F001\n  deprecated: false\n- caption: BCS effect scaling with pool size\n  label: fig:bcs_scaling\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=9.1pp\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 40-rel delta=33.3pp (80-pool subset)\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=31.2pp\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: LLaMA 80-rel delta=27.1pp\n  id: F002\n  deprecated: false\n- caption: Error taxonomy by BCS bin\n  label: fig:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: 'NER: IntraSub 0%->49.4%'\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: 'RE: IntraSub 0%->32.3%'\n  id: F003\n  deprecated: false\n_completeness:\n  coverage: 32/42\n  claims: 39\n  tables: 5\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 32\n    tier3: 10\n    tierX: 0\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 485,
        "oldLines": 7,
        "newStart": 485,
        "newLines": 7,
        "lines": [
          "     section: results",
          "     paragraph: 0",
          "     sentence: 0",
          "-  text: Independent 16-rel slope = -0.449, CI [-0.549, -0.345], r = -0.637, p < 1e-12",
          "+  text: Independent 16-rel slope = -0.449, CI [-0.552, -0.346], r = -0.637, p < 1e-12",
          "   type: quantitative",
          "   evidence: []",
          "   decisions: []"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Edit · `toolu_018HqBNP79Y5DSZdaMsimkz7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "old_string": "  id: T005\n  deprecated: false\nfigures:",
  "new_string": "  id: T005\n  deprecated: false\n- caption: Three-way BCS--accuracy analysis on FewRel (regression slope, quartile delta,\n    permutation test).\n  label: tab:within_pool\n  location:\n    section: results\n  cells:\n  - exp_id: three_way_comparison\n    metric: 'Independent 16-rel: slope=-0.449, CI [-0.552, -0.346], r=-0.637'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: '80-pool→16-sub: slope=-0.401, CI [-0.701, -0.069], r=-0.221, p=0.027'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: 'Full 80-rel: slope=-0.151, CI [-0.930, +0.657], underpowered'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: 'Permutation test (16-rel vs 80-pool slopes): p=0.436'\n    source: artifacts/three_way_comparison/results_unified.json\n  id: T006\n  deprecated: false\nfigures:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "a3b9f9c4-1b9c-4466-b759-aa3196ed9c84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJ2CUavnmtxM2rDGAaH7Gh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 72989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2021
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

_source line 92 · 2026-05-16T02:43:07.013Z_

<details><summary>↩ Tool result · `toolu_018HqBNP79Y5DSZdaMsimkz7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "0e2490f6-b602-46fa-9bd8-4cbd271ff4ff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
    "oldString": "  id: T005\n  deprecated: false\nfigures:",
    "newString": "  id: T005\n  deprecated: false\n- caption: Three-way BCS--accuracy analysis on FewRel (regression slope, quartile delta,\n    permutation test).\n  label: tab:within_pool\n  location:\n    section: results\n  cells:\n  - exp_id: three_way_comparison\n    metric: 'Independent 16-rel: slope=-0.449, CI [-0.552, -0.346], r=-0.637'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: '80-pool→16-sub: slope=-0.401, CI [-0.701, -0.069], r=-0.221, p=0.027'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: 'Full 80-rel: slope=-0.151, CI [-0.930, +0.657], underpowered'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: 'Permutation test (16-rel vs 80-pool slopes): p=0.436'\n    source: artifacts/three_way_comparison/results_unified.json\n  id: T006\n  deprecated: false\nfigures:",
    "originalFile": "paper:\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free\n    LLM Information Extraction?\n  version: 3\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\n  source: manual mapping from registry + paper_framing.md\nclaims:\n- text: 'Training-free LLM information extraction---prompting models with target schemas\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\n    drops from 0.72 to 0.42 with 64 candidate '\n  type: quantitative\n  location:\n    section: abstract\n    context: result_statement\n  id: C001\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall count_1=0.720, count_64=0.418\n    tier: 1\n  deprecated: false\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\n    overlap between types and design two complementary experimental paradigms: count\n    cu'\n  type: methodological\n  location:\n    section: abstract\n    context: finding_statement\n  id: C002\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\n    tier: 1\n  deprecated: false\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\n    recall as candidate types increase, and'\n  type: quantitative\n  location:\n    section: conclusion\n    context: result_statement\n  id: C003\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: 'Channel 1: recall 0.72->0.418'\n    tier: 1\n  - exp_id: exp007_error_taxonomy\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub vs BCS rho=0.954\n    tier: 1\n  deprecated: false\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\n    capability, native structured JSON output support, and the practical advantage\n    that the FP8-quantized 32B model fits on a\n  type: quantitative\n  location:\n    section: experimental_setup\n    context: result_statement\n  id: C004\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\n    tier: 2\n  deprecated: false\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\n  type: methodological\n  location:\n    section: experimental_setup\n    context: finding_statement\n  id: C005\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\n    tier: 1\n  deprecated: false\n- text: Channel~1\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C006\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418 monotonic decline\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: accuracy 0.857->0.504 monotonic decline\n    tier: 1\n  deprecated: false\n- text: Channel~2\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C007\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS-controlled delta=-31.2pp\n    tier: 1\n  deprecated: false\n- text: Training-free LLM information extraction---prompting a large language model\n    with a target schema and asking it to extract structured information without any\n    task-specific fine-tuning---enables rapid d\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C008\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: background framing, supported by all experiments\n    tier: 3\n  deprecated: false\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\n    similarity between type pairs corre\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C009\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CIs exclude zero for both\n    tier: 1\n  deprecated: false\n- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy\n    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute gap\n    tier: 1\n  deprecated: false\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\n    between mean BCS and per-type er\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C011\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\n    into different batches, yet every decomp\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C012\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\n    tier: 1\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: v1 sdgd_zero F1=0.251, also below baseline\n    tier: 1\n  deprecated: false\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy\n    relationship is consistent across schema sizes (slope permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS--accuracy slope consistent across pools, permutation p=0.436\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\n    semantic overlap between types using embedding cosine similarity, and its batch\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C014\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: SCS validated as proxy for empirical confusion\n    tier: 2\n  deprecated: false\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\n    embedding models, while identifying a centrality confound that invalidates per-type\n    aggrega\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C015\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN centrality confound (per-type positive)\n    tier: 1\n  deprecated: false\n- text: 95\\\\% CI\n  type: quantitative\n  location:\n    section: results\n    context: bold\n  id: C016\n  evidence:\n  - exp_id: bootstrap_ci_analysis\n    metric: 7 CIs all exclude null\n    tier: 1\n  deprecated: false\n- text: Recall declines monotonically from 0.72 at count${\\\\,=\\\\,1$ to 0.42 at count${\\\\,=\\\\,64$,\n    a 42\\\\% relative drop. Precision moves in the opposite direction, rising from\n    0.11 to 0.52, reflecting a shift from\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C017\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418, precision 0.105->0.52\n    tier: 1\n  deprecated: false\n- text: Accuracy drops monotonically from 85.7\\\\% at count${\\\\,=\\\\,1$ to 50.4\\\\% at\n    count${\\\\,=\\\\,80$, a near-halving when the model must discriminate among all 80\n    relation types simultaneously.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C018\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\n    tier: 1\n  deprecated: false\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\,=\\\\,1$\n    to 0.247 at count${\\\\,=\\\\,44$. This reversal arises from three properties of the\n    MAVEN setup: (i)~trigger-level relaxed'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C019\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\n    tier: 1\n  deprecated: false\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\%$, meaning pairwise confusability\n    explains roughly 1.5\\\\% of the variance in type confusion. Other factors---entity\n    frequency, prompt position effects lost-'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C020\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN pairwise r=0.129, r2=1.66%\n    tier: 1\n  deprecated: false\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\n    and MiniLM yields $ = 0.144$ ($p\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C021\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\n    tier: 1\n  deprecated: false\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\n    types; high-BCS batches contain maximally similar types. The confusability gap\n    widens from 9.1\\\\,pp at 16 relations to 31.2\\\\\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C022\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\n    tier: 1\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\n    tier: 1\n  deprecated: false\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\n    this gap to 31.2\\\\,pp (95\\\\% CI: [17.7, 42.'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C023\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=-31.2pp\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\n    tier: 1\n  deprecated: false\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C024\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\n      flat)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\n    tier: 1\n  deprecated: false\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\n    with BCS in both tasks: NER IntraSub rises from 0\\\\% (solo) to 49.4\\\\% (high BCS)\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C025\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub rho=1.0 (p<0.001)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub rho=0.954 (p<1e-6)\n    tier: 1\n  deprecated: false\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\,=\\\\,6$, high-BCS\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\n    versus $1.7$ under random batching. At\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C026\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\n    tier: 1\n  deprecated: false\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C027\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\n    the values in Table~tab:pairwise. The problem'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C028\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [0.104, 0.156]\n    tier: 1\n  deprecated: false\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\n    0.02$, $n = 63$), in the expected negative direc\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C029\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\n    tier: 1\n  deprecated: false\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\n    F1\\\\,=\\\\,0.445 (P\\\\,=\\\\,0.563, R\\\\,=\\\\,0.368).  SDGD obtains F1\\\\,=\\\\,0.251 (P\\\\,=\\\\,0.210,\n    R\\\\,=\\\\,0.314), a 44\\\\% relative drop.  Rand\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C030\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\n    tier: 1\n  deprecated: false\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\n    versus 0.563).  The mechanism is straightfo'\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C031\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\n    tier: 1\n  deprecated: false\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\n    retains only the highest-scoring candidate fo\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C032\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\n    tier: 1\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub slope = -0.401, CI [-0.701, -0.069], r = -0.221, p = 0.027\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Independent 16-rel slope = -0.449, CI [-0.552, -0.346], r = -0.637, p < 1e-12\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\ntables:\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\n    model used for SCS/BCS computation.\n  label: tab:datasets\n  location:\n    section: experimental_setup\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: Few-NERD 66 types\n  - exp_id: exp-004\n    metric: MAVEN 168 event types, 77993 train mentions\n  - exp_id: exp_fewrel_formal_80rel\n    metric: FewRel 80 relations\n  id: T001\n  deprecated: false\n- caption: Pairwise SCS--confusion correlation.\n  label: tab:pairwise\n  location:\n    section: results\n  cells:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n  - exp_id: bootstrap_ci_analysis\n    metric: bootstrap CIs for both\n  id: T002\n  deprecated: false\n- caption: BCS-controlled FewRel accuracy.\n  label: tab:bcs_controlled\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: delta=-9.1pp'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\n  - exp_id: bootstrap_ci_analysis\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\n  id: T003\n  deprecated: false\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\n  label: tab:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\n  id: T004\n  deprecated: false\n- caption: Few-NERD extraction under decomposition modes.\n  label: tab:sdgd_results\n  location:\n    section: sdgd_negative\n  cells:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\n      F1=0.292'\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\n  id: T005\n  deprecated: false\nfigures:\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\n  label: fig:count_curves\n  location:\n    section: results\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: 'Panel (a): recall 0.72->0.418'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 'Panel (b): accuracy 0.857->0.504'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 'Panel (b): count_40=0.588'\n  id: F001\n  deprecated: false\n- caption: BCS effect scaling with pool size\n  label: fig:bcs_scaling\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=9.1pp\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 40-rel delta=33.3pp (80-pool subset)\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=31.2pp\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: LLaMA 80-rel delta=27.1pp\n  id: F002\n  deprecated: false\n- caption: Error taxonomy by BCS bin\n  label: fig:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: 'NER: IntraSub 0%->49.4%'\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: 'RE: IntraSub 0%->32.3%'\n  id: F003\n  deprecated: false\n_completeness:\n  coverage: 32/42\n  claims: 39\n  tables: 5\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 32\n    tier3: 10\n    tierX: 0\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 609,
        "oldLines": 6,
        "newStart": 609,
        "newLines": 26,
        "lines": [
          "     metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'",
          "   id: T005",
          "   deprecated: false",
          "+- caption: Three-way BCS--accuracy analysis on FewRel (regression slope, quartile delta,",
          "+    permutation test).",
          "+  label: tab:within_pool",
          "+  location:",
          "+    section: results",
          "+  cells:",
          "+  - exp_id: three_way_comparison",
          "+    metric: 'Independent 16-rel: slope=-0.449, CI [-0.552, -0.346], r=-0.637'",
          "+    source: artifacts/three_way_comparison/results_unified.json",
          "+  - exp_id: three_way_comparison",
          "+    metric: '80-pool→16-sub: slope=-0.401, CI [-0.701, -0.069], r=-0.221, p=0.027'",
          "+    source: artifacts/three_way_comparison/results_unified.json",
          "+  - exp_id: three_way_comparison",
          "+    metric: 'Full 80-rel: slope=-0.151, CI [-0.930, +0.657], underpowered'",
          "+    source: artifacts/three_way_comparison/results_unified.json",
          "+  - exp_id: three_way_comparison",
          "+    metric: 'Permutation test (16-rel vs 80-pool slopes): p=0.436'",
          "+    source: artifacts/three_way_comparison/results_unified.json",
          "+  id: T006",
          "+  deprecated: false",
          " figures:",
          " - caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)",
          "   label: fig:count_curves"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Edit · `toolu_01H1Kn439JYxRemndKSaAD8V`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
  "old_string": "  tables: 5",
  "new_string": "  tables: 6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "7c7afe3d-c667-4dc4-9e1e-ad648c17a5b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJ2CUavnmtxM2rDGAaH7Gh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 72989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2021
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

_source line 94 · 2026-05-16T02:43:07.719Z_

<details><summary>↩ Tool result · `toolu_01H1Kn439JYxRemndKSaAD8V`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "0ba206e2-2ed2-4e42-a9c3-4a38521b9625",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml",
    "oldString": "  tables: 5",
    "newString": "  tables: 6",
    "originalFile": "paper:\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free\n    LLM Information Extraction?\n  version: 3\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\n  source: manual mapping from registry + paper_framing.md\nclaims:\n- text: 'Training-free LLM information extraction---prompting models with target schemas\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\n    drops from 0.72 to 0.42 with 64 candidate '\n  type: quantitative\n  location:\n    section: abstract\n    context: result_statement\n  id: C001\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall count_1=0.720, count_64=0.418\n    tier: 1\n  deprecated: false\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\n    overlap between types and design two complementary experimental paradigms: count\n    cu'\n  type: methodological\n  location:\n    section: abstract\n    context: finding_statement\n  id: C002\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\n    tier: 1\n  deprecated: false\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\n    recall as candidate types increase, and'\n  type: quantitative\n  location:\n    section: conclusion\n    context: result_statement\n  id: C003\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: 'Channel 1: recall 0.72->0.418'\n    tier: 1\n  - exp_id: exp007_error_taxonomy\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub vs BCS rho=0.954\n    tier: 1\n  deprecated: false\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\n    capability, native structured JSON output support, and the practical advantage\n    that the FP8-quantized 32B model fits on a\n  type: quantitative\n  location:\n    section: experimental_setup\n    context: result_statement\n  id: C004\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\n    tier: 2\n  deprecated: false\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\n  type: methodological\n  location:\n    section: experimental_setup\n    context: finding_statement\n  id: C005\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\n    tier: 1\n  deprecated: false\n- text: Channel~1\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C006\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418 monotonic decline\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: accuracy 0.857->0.504 monotonic decline\n    tier: 1\n  deprecated: false\n- text: Channel~2\n  type: quantitative\n  location:\n    section: introduction\n    context: bold\n  id: C007\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS-controlled delta=-31.2pp\n    tier: 1\n  deprecated: false\n- text: Training-free LLM information extraction---prompting a large language model\n    with a target schema and asking it to extract structured information without any\n    task-specific fine-tuning---enables rapid d\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C008\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: background framing, supported by all experiments\n    tier: 3\n  deprecated: false\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\n    similarity between type pairs corre\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C009\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CIs exclude zero for both\n    tier: 1\n  deprecated: false\n- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy\n    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C010\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel BCS effect delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute gap\n    tier: 1\n  deprecated: false\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\n    between mean BCS and per-type er\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C011\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\n    into different batches, yet every decomp\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C012\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\n    tier: 1\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: v1 sdgd_zero F1=0.251, also below baseline\n    tier: 1\n  deprecated: false\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\n    bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy\n    relationship is consistent across schema sizes (slope permutation p = 0.44)\n  type: quantitative\n  location:\n    section: introduction\n    context: result_statement\n  id: C013\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: BCS--accuracy slope consistent across pools, permutation p=0.436\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: FewRel count_8 delta CI [17.7, 42.7]\n    tier: 1\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\n    tier: 1\n  deprecated: false\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\n    semantic overlap between types using embedding cosine similarity, and its batch\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C014\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: SCS validated as proxy for empirical confusion\n    tier: 2\n  deprecated: false\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\n    embedding models, while identifying a centrality confound that invalidates per-type\n    aggrega\n  type: methodological\n  location:\n    section: introduction\n    context: finding_statement\n  id: C015\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN centrality confound (per-type positive)\n    tier: 1\n  deprecated: false\n- text: 95\\\\% CI\n  type: quantitative\n  location:\n    section: results\n    context: bold\n  id: C016\n  evidence:\n  - exp_id: bootstrap_ci_analysis\n    metric: 7 CIs all exclude null\n    tier: 1\n  deprecated: false\n- text: Recall declines monotonically from 0.72 at count${\\\\,=\\\\,1$ to 0.42 at count${\\\\,=\\\\,64$,\n    a 42\\\\% relative drop. Precision moves in the opposite direction, rising from\n    0.11 to 0.52, reflecting a shift from\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C017\n  evidence:\n  - exp_id: exp001_count_baseline\n    metric: recall 0.72->0.418, precision 0.105->0.52\n    tier: 1\n  deprecated: false\n- text: Accuracy drops monotonically from 85.7\\\\% at count${\\\\,=\\\\,1$ to 50.4\\\\% at\n    count${\\\\,=\\\\,80$, a near-halving when the model must discriminate among all 80\n    relation types simultaneously.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C018\n  evidence:\n  - exp_id: exp_fewrel_formal_80rel\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\n    tier: 1\n  deprecated: false\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\,=\\\\,1$\n    to 0.247 at count${\\\\,=\\\\,44$. This reversal arises from three properties of the\n    MAVEN setup: (i)~trigger-level relaxed'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C019\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\n    tier: 1\n  deprecated: false\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\%$, meaning pairwise confusability\n    explains roughly 1.5\\\\% of the variance in type confusion. Other factors---entity\n    frequency, prompt position effects lost-'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C020\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\n    tier: 1\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN pairwise r=0.129, r2=1.66%\n    tier: 1\n  deprecated: false\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\n    and MiniLM yields $ = 0.144$ ($p\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C021\n  evidence:\n  - exp_id: exp015_scs_validation\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\n    tier: 1\n  deprecated: false\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\n    types; high-BCS batches contain maximally similar types. The confusability gap\n    widens from 9.1\\\\,pp at 16 relations to 31.2\\\\\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C022\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\n    tier: 1\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\n    tier: 1\n  deprecated: false\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\n    this gap to 31.2\\\\,pp (95\\\\% CI: [17.7, 42.'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C023\n  evidence:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=-9.1pp\n    tier: 1\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=-31.2pp\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\n    tier: 1\n  deprecated: false\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C024\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\n      flat)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\n    tier: 1\n  deprecated: false\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\n    with BCS in both tasks: NER IntraSub rises from 0\\\\% (solo) to 49.4\\\\% (high BCS)\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C025\n  evidence:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub rho=1.0 (p<0.001)\n    tier: 1\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub rho=0.954 (p<1e-6)\n    tier: 1\n  deprecated: false\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\,=\\\\,6$, high-BCS\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\n    versus $1.7$ under random batching. At\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C026\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\n    tier: 1\n  deprecated: false\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C027\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\n    tier: 1\n  deprecated: false\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\n    the values in Table~tab:pairwise. The problem'\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C028\n  evidence:\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129\n    tier: 1\n  - exp_id: bootstrap_ci_analysis\n    metric: CI [0.104, 0.156]\n    tier: 1\n  deprecated: false\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\n    0.02$, $n = 63$), in the expected negative direc\n  type: quantitative\n  location:\n    section: results\n    context: result_statement\n  id: C029\n  evidence:\n  - exp_id: exp002_confusability_controlled\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\n    tier: 1\n  deprecated: false\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\n    F1\\\\,=\\\\,0.445 (P\\\\,=\\\\,0.563, R\\\\,=\\\\,0.368).  SDGD obtains F1\\\\,=\\\\,0.251 (P\\\\,=\\\\,0.210,\n    R\\\\,=\\\\,0.314), a 44\\\\% relative drop.  Rand\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C030\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\n    tier: 1\n  deprecated: false\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\n    versus 0.563).  The mechanism is straightfo'\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C031\n  evidence:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\n    tier: 1\n  deprecated: false\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\n    retains only the highest-scoring candidate fo\n  type: quantitative\n  location:\n    section: sdgd_negative\n    context: result_statement\n  id: C032\n  evidence:\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\n    tier: 1\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub slope = -0.401, CI [-0.701, -0.069], r = -0.221, p = 0.027\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Independent 16-rel slope = -0.449, CI [-0.552, -0.346], r = -0.637, p < 1e-12\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\ntables:\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\n    model used for SCS/BCS computation.\n  label: tab:datasets\n  location:\n    section: experimental_setup\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: Few-NERD 66 types\n  - exp_id: exp-004\n    metric: MAVEN 168 event types, 77993 train mentions\n  - exp_id: exp_fewrel_formal_80rel\n    metric: FewRel 80 relations\n  id: T001\n  deprecated: false\n- caption: Pairwise SCS--confusion correlation.\n  label: tab:pairwise\n  location:\n    section: results\n  cells:\n  - exp_id: exp002_confusability_controlled\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\n  - exp_id: exp004_maven_bcs\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\n  - exp_id: bootstrap_ci_analysis\n    metric: bootstrap CIs for both\n  id: T002\n  deprecated: false\n- caption: BCS-controlled FewRel accuracy.\n  label: tab:bcs_controlled\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: '16-rel: delta=-9.1pp'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\n  - exp_id: bootstrap_ci_analysis\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\n  id: T003\n  deprecated: false\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\n  label: tab:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\n  id: T004\n  deprecated: false\n- caption: Few-NERD extraction under decomposition modes.\n  label: tab:sdgd_results\n  location:\n    section: sdgd_negative\n  cells:\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\n      F1=0.292'\n  - exp_id: exp008_sdgd_v2_fewnerd\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\n  id: T005\n  deprecated: false\n- caption: Three-way BCS--accuracy analysis on FewRel (regression slope, quartile delta,\n    permutation test).\n  label: tab:within_pool\n  location:\n    section: results\n  cells:\n  - exp_id: three_way_comparison\n    metric: 'Independent 16-rel: slope=-0.449, CI [-0.552, -0.346], r=-0.637'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: '80-pool→16-sub: slope=-0.401, CI [-0.701, -0.069], r=-0.221, p=0.027'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: 'Full 80-rel: slope=-0.151, CI [-0.930, +0.657], underpowered'\n    source: artifacts/three_way_comparison/results_unified.json\n  - exp_id: three_way_comparison\n    metric: 'Permutation test (16-rel vs 80-pool slopes): p=0.436'\n    source: artifacts/three_way_comparison/results_unified.json\n  id: T006\n  deprecated: false\nfigures:\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\n  label: fig:count_curves\n  location:\n    section: results\n  cells:\n  - exp_id: exp001_count_baseline\n    metric: 'Panel (a): recall 0.72->0.418'\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 'Panel (b): accuracy 0.857->0.504'\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 'Panel (b): count_40=0.588'\n  id: F001\n  deprecated: false\n- caption: BCS effect scaling with pool size\n  label: fig:bcs_scaling\n  location:\n    section: results\n  cells:\n  - exp_id: exp_fewrel_formal\n    metric: 16-rel delta=9.1pp\n  - exp_id: exp_fewrel_40rel_r4\n    metric: 40-rel delta=33.3pp (80-pool subset)\n  - exp_id: exp_fewrel_formal_80rel\n    metric: 80-rel delta=31.2pp\n  - exp_id: exp012_llama_fewrel_ch2\n    metric: LLaMA 80-rel delta=27.1pp\n  id: F002\n  deprecated: false\n- caption: Error taxonomy by BCS bin\n  label: fig:error_taxonomy\n  location:\n    section: results\n  cells:\n  - exp_id: exp007_error_taxonomy\n    metric: 'NER: IntraSub 0%->49.4%'\n  - exp_id: exp016_fewrel_error_taxonomy\n    metric: 'RE: IntraSub 0%->32.3%'\n  id: F003\n  deprecated: false\n_completeness:\n  coverage: 32/42\n  claims: 39\n  tables: 5\n  figures: 3\n  tier_counts:\n    tier1: 0\n    tier2: 32\n    tier3: 10\n    tierX: 0\n  last_checked: '2026-05-16T02:22:29.529421+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 672,
        "oldLines": 7,
        "newStart": 672,
        "newLines": 7,
        "lines": [
          " _completeness:",
          "   coverage: 32/42",
          "   claims: 39",
          "-  tables: 5",
          "+  tables: 6",
          "   figures: 3",
          "   tier_counts:",
          "     tier1: 0"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 95_

全部完成。汇总如下：

---

## 1. 编译验证

- **状态**: 通过
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf` (13页, 370KB)
- **错误**: 无
- **Warnings**: 仅 overfull/underfull hbox (可忽略) 和 `h` float → `ht` (可忽略)
- **Table within_pool 渲染**: 左侧 Regression (Slope/CI/r/p)，右侧 Quartile (Δ/CI)，底部 permutation p=0.436 脚注 — 结构正确
- **Caption**: 明确提及 "The full 80-rel condition (n=25) is underpowered for both metrics"

## 2. 交叉一致性检查

| 检查项 | 状态 | 详情 |
|--------|------|------|
| abstract 数值 vs results | 通过 | NER 0.72→0.42, RE 85.7%→50.4%, permutation p=0.44 (0.436 rounded), Δ 31.2/9.1pp, Llama r=0.725/Δ=-27pp |
| introduction 数值 vs results | 通过 | r=0.112–0.129, permutation p=0.44, merge amplification F1=0.32 vs 0.45 |
| main.tex limitations vs results | 通过 | Llama -43pp/r=0.725, CH2 Δ=-27.1/-23.9pp, floor≈0.51, slope -0.401, permutation p=0.436 |
| "3.4×" BCS amplification | 通过 | 所有 .tex 文件中已完全清除 |
| "amplification" 用法 | 通过 | 仅保留 "merge amplification"（SDGD 概念）和 "stable rather than amplifying"（否定形式） |
| 旧 CI "8.62" / "0.16" | 通过 | 无残留 |
| slope 数值一致性 (-0.449, -0.401, p=0.436) | 通过 | table + body text 一致 |
| count_40 描述 (C001约束) | 通过 | 明确标注 "40-relation subsets sampled from the 80-relation pool, not an independent schema" |

## 3. Provenance 更新

已完成以下修改：

- **C010**: 文本从 "amplify with schema scale / 3.4x" 更新为 "robust across schema sizes, slopes consistent (permutation p=0.44)"
- **C013**: 文本从 "amplify $3.4$" 更新为 "consistent across schema sizes (slope permutation p=0.44)"；evidence metric 同步更新
- **C033**: CI 从 [-0.694, -0.057] 更正为 [-0.701, -0.069]（对齐论文表格）
- **C034**: CI 从 [-0.549, -0.345] 更正为 [-0.552, -0.346]（对齐论文表格）
- **T006**: 新增 tab:within_pool 表条目，data source = `artifacts/three_way_comparison/results_unified.json`
- **_completeness.tables**: 5 → 6

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "uuid": "4a5ead4e-6003-4490-a19e-9754584fa866",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qrVM7YKoBeotEq4VmRUS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 756,
      "cache_read_input_tokens": 75010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 756
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

_source line 96_

全部完成。汇总如下：

---

## 1. 编译验证

- **状态**: 通过
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf` (13页, 370KB)
- **错误**: 无
- **Warnings**: 仅 overfull/underfull hbox (可忽略) 和 `h` float → `ht` (可忽略)
- **Table within_pool 渲染**: 左侧 Regression (Slope/CI/r/p)，右侧 Quartile (Δ/CI)，底部 permutation p=0.436 脚注 — 结构正确
- **Caption**: 明确提及 "The full 80-rel condition (n=25) is underpowered for both metrics"

## 2. 交叉一致性检查

| 检查项 | 状态 | 详情 |
|--------|------|------|
| abstract 数值 vs results | 通过 | NER 0.72→0.42, RE 85.7%→50.4%, permutation p=0.44 (0.436 rounded), Δ 31.2/9.1pp, Llama r=0.725/Δ=-27pp |
| introduction 数值 vs results | 通过 | r=0.112–0.129, permutation p=0.44, merge amplification F1=0.32 vs 0.45 |
| main.tex limitations vs results | 通过 | Llama -43pp/r=0.725, CH2 Δ=-27.1/-23.9pp, floor≈0.51, slope -0.401, permutation p=0.436 |
| "3.4×" BCS amplification | 通过 | 所有 .tex 文件中已完全清除 |
| "amplification" 用法 | 通过 | 仅保留 "merge amplification"（SDGD 概念）和 "stable rather than amplifying"（否定形式） |
| 旧 CI "8.62" / "0.16" | 通过 | 无残留 |
| slope 数值一致性 (-0.449, -0.401, p=0.436) | 通过 | table + body text 一致 |
| count_40 描述 (C001约束) | 通过 | 明确标注 "40-relation subsets sampled from the 80-relation pool, not an independent schema" |

## 3. Provenance 更新

已完成以下修改：

- **C010**: 文本从 "amplify with schema scale / 3.4x" 更新为 "robust across schema sizes, slopes consistent (permutation p=0.44)"
- **C013**: 文本从 "amplify $3.4$" 更新为 "consistent across schema sizes (slope permutation p=0.44)"；evidence metric 同步更新
- **C033**: CI 从 [-0.694, -0.057] 更正为 [-0.701, -0.069]（对齐论文表格）
- **C034**: CI 从 [-0.549, -0.345] 更正为 [-0.552, -0.346]（对齐论文表格）
- **T006**: 新增 tab:within_pool 表条目，data source = `artifacts/three_way_comparison/results_unified.json`
- **_completeness.tables**: 5 → 6

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 292931,
  "duration_api_ms": 291120,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "9c09c2cd-1b27-407c-a972-63bebddcdc4c",
  "total_cost_usd": 1.16057925,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 63925,
    "cache_read_input_tokens": 867712,
    "output_tokens": 13011,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 63925,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 932,
        "cache_read_input_tokens": 75010,
        "cache_creation_input_tokens": 756,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 756
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1737,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001817,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 13011,
      "cacheReadInputTokens": 867712,
      "cacheCreationInputTokens": 63925,
      "webSearchRequests": 0,
      "costUSD": 1.15876225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f3091f75-d7d3-465f-a2c7-a780851c1b67"
}
```

</details>

---

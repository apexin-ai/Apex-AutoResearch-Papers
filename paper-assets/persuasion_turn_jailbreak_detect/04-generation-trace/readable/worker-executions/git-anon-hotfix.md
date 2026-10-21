# git anon hotfix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_git_anon-hotfix_20260525T091904.log`
- **Structured JSON:** [`c89429eec15991e01b3d.json`](../../sessions/c8/c89429eec15991e01b3d.json)

## Before a recorded user message

73 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
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
    "mcp__agent-ml-research__clone_repo",
    "mcp__agent-ml-research__list_repo_tree",
    "mcp__agent-ml-research__poll_secret_request",
    "mcp__agent-ml-research__read_repo_file",
    "mcp__agent-ml-research__request_secret",
    "mcp__agent-ml-research__search_repo",
    "mcp__agent-ml-research__sync_code_to_remote"
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
  "uuid": "b8e077de-95da-41a6-9303-f8003595849f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/memory/"
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
    "resetsAt": 1779709800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4ea2e20f-a685-4f36-bc47-a881be3c5934",
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to fix an anonymous repository by:
1. Getting a GitHub PAT token
2. Cloning the anonymous repo
3. Copying latest .tex and .bib files
4. Commenting out missing figure references
5. Verifying anonymity
6. Force pushing

Let me start by requesting the secret.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "41925eeb-524d-41d6-91d9-43f306c406dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YDZf3a8DLDm4U8AgybyJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13040,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13040
      },
      "output_tokens": 23,
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

开始执行匿名仓库热修复。先获取 PAT。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "d62db926-8e04-442c-9165-78dfddfad805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YDZf3a8DLDm4U8AgybyJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13040,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13040
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PmDf5XbDxKdEpNn3ZnoLTB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__request_secret",
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
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "0bc0f100-b7ad-4df8-9f5f-eb11374addf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YDZf3a8DLDm4U8AgybyJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13040,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13040
      },
      "output_tokens": 23,
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

_source line 7 · 2026-05-25T09:19:26.376Z_

<details><summary>↩ Tool result · `toolu_01PmDf5XbDxKdEpNn3ZnoLTB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__request_secret"
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
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "2d27f91b-c4f6-4ea4-b27d-8b4e19786ae7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__request_secret"
    ],
    "query": "select:mcp__agent-ml-research__request_secret",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_secret · `toolu_01AGwk4P1ocnFQyRsYodaoCB`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "key_id": "github_anon_pat",
  "purpose": "Clone and push hotfix to anonymous review repo: sync latest tex files + comment out missing figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "750c1ca8-cdf5-442e-8f4f-ed5a993fa8b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZmjmvgcpgSZkw2uhUzMvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 24881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 439
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

_source line 9 · 2026-05-25T09:19:34.943Z_

<details><summary>↩ Tool result · `toolu_01AGwk4P1ocnFQyRsYodaoCB`</summary>

```text
{"result":"{\"status\": \"pending_approval\", \"request_id\": \"secret_req_github_anon_pat_1779700770\", \"key_id\": \"github_anon_pat\", \"routed_to_director\": false, \"message\": \"已发送审批卡片到飞书A群。等待批准后调用 poll_secret_request('secret_req_github_anon_pat_1779700770', 'persuasion_turn_jailbreak_detect') 获取密钥。\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "bcbf3893-9564-45b9-8533-a8e6db8037ef",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending_approval\\\", \\\"request_id\\\": \\\"secret_req_github_anon_pat_1779700770\\\", \\\"key_id\\\": \\\"github_anon_pat\\\", \\\"routed_to_director\\\": false, \\\"message\\\": \\\"已发送审批卡片到飞书A群。等待批准后调用 poll_secret_request('secret_req_github_anon_pat_1779700770', 'persuasion_turn_jailbreak_detect') 获取密钥。\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending_approval\", \"request_id\": \"secret_req_github_anon_pat_1779700770\", \"key_id\": \"github_anon_pat\", \"routed_to_director\": false, \"message\": \"已发送审批卡片到飞书A群。等待批准后调用 poll_secret_request('secret_req_github_anon_pat_1779700770', 'persuasion_turn_jailbreak_detect') 获取密钥。\"}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

等待审批，轮询获取密钥。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "75f12dec-4302-49c0-8856-54f6159b0302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVgGZh9yH8myUPM41scdCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 25320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
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

_source line 11_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0184jrw3es6P5t9mcUBjF8zQ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__poll_secret_request",
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
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "cf114d4d-bab5-4f8d-bc9c-246fce66b060",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVgGZh9yH8myUPM41scdCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 25320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
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

_source line 12 · 2026-05-25T09:19:39.404Z_

<details><summary>↩ Tool result · `toolu_0184jrw3es6P5t9mcUBjF8zQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__poll_secret_request"
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
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "b0a67d00-9ebc-46be-b936-8af3ca55486d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__poll_secret_request"
    ],
    "query": "select:mcp__agent-ml-research__poll_secret_request",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_01WbrZtY5E7ouPvKAPHehCGa`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "a73c8c30-48b0-4713-9642-775c39484267",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yvGe6prE24nDM88THK3EM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 25603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 307
      },
      "output_tokens": 5,
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

_source line 14 · 2026-05-25T09:19:43.814Z_

<details><summary>↩ Tool result · `toolu_01WbrZtY5E7ouPvKAPHehCGa`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "13a16f5f-ea49-439c-add8-7eb24b0af8b4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

审批还在等待中，稍后再试。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "6074eab8-c7a8-4696-9c3d-5682956d953e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyiaJD4qJf76kDmnUAHaef",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 25910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 148
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_01HpALvL9thuG9hmBipVJTm1`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "4000a026-5a66-453c-b508-76e3c7ac1fc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyiaJD4qJf76kDmnUAHaef",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 25910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 148
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

_source line 17 · 2026-05-25T09:19:47.911Z_

<details><summary>↩ Tool result · `toolu_01HpALvL9thuG9hmBipVJTm1`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "ade7ae95-abd0-4748-b021-e7829fde237d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

仍在等待审批，继续轮询。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "924b0f8a-375b-437d-aa9a-aa5827cb625e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Shhbm7QhYsHPAz5dQyCfVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 26058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
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

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_01PnW8BjWDUDFMCA6wqE8PYd`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "9acf885e-dc48-49b2-83d6-2f7778131b9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Shhbm7QhYsHPAz5dQyCfVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 26058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
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

_source line 20 · 2026-05-25T09:19:55.318Z_

<details><summary>↩ Tool result · `toolu_01PnW8BjWDUDFMCA6wqE8PYd`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "103f01a7-3340-406b-aadf-231892a621b0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_01PQrXJMabTniB54uskU9VTi`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "08f842a0-9d27-4195-bb63-71b5c5a98c10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHcrgrddjZDA6dax9SyH8T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 26218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 264
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

_source line 22 · 2026-05-25T09:20:00.063Z_

<details><summary>↩ Tool result · `toolu_01PQrXJMabTniB54uskU9VTi`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "98d0f114-9118-40d4-9fbf-3b79210ea784",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_015Vcp5YmXxYH46QjPXuBY4i`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "0adc5dfc-87bc-456a-a243-c0e49badaf60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015V1ieMinAwhuKyUyc2viCo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 26482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
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

_source line 24 · 2026-05-25T09:20:09.708Z_

<details><summary>↩ Tool result · `toolu_015Vcp5YmXxYH46QjPXuBY4i`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "fd06fd38-e0bb-4d0a-a8e2-84153f017884",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_018abBh8apTtnoPqbnMFBA88`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "839e60c7-dcfe-4d6a-8cdf-1662fbc6a991",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dbb95M8SfRy3yg7Ewwu3DZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 26627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
      },
      "output_tokens": 72,
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

_source line 26 · 2026-05-25T09:20:14.970Z_

<details><summary>↩ Tool result · `toolu_018abBh8apTtnoPqbnMFBA88`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "ffac5e66-374f-4695-8053-3aea290b6e0e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_013bdAWQczpub5hgKDB2aoqb`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "e5ac579a-32ae-4f99-b5b5-dd62d670373e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016T4HGDXH8DEwvxEsrkkzab",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 26772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
      },
      "output_tokens": 72,
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

_source line 28 · 2026-05-25T09:20:22.806Z_

<details><summary>↩ Tool result · `toolu_013bdAWQczpub5hgKDB2aoqb`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "91fc18e1-7ddf-4179-86a2-276746615f81",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_016YfrLMc1gYnA37qXbuqaRd`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "28ca4c93-5f5c-4940-85a3-89e76549b66a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MM6yagkxrKm6jWL4e9Go35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 26917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
      },
      "output_tokens": 72,
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

_source line 30 · 2026-05-25T09:20:25.636Z_

<details><summary>↩ Tool result · `toolu_016YfrLMc1gYnA37qXbuqaRd`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "1345772b-9aed-497e-aded-aafadc635b6b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_01CiwM1HjTkFDd7LgshGRUS9`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "2d6e3764-a36e-4a77-8ecb-c03e2c2ef4eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YTEKgXVJmrZZAcvgnvNs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 27062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
      },
      "output_tokens": 72,
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

_source line 32 · 2026-05-25T09:20:27.900Z_

<details><summary>↩ Tool result · `toolu_01CiwM1HjTkFDd7LgshGRUS9`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "6e419df8-b1c6-4df8-b04b-0217651e6008",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_01Xq8Jba5FkpNhQJ6VRM7SvP`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "84d75ebd-7ebe-4c88-8656-2fa4d4219c09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvRFULJw4iEBkZaAcvEt26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 27207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
      },
      "output_tokens": 72,
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

_source line 34 · 2026-05-25T09:20:30.411Z_

<details><summary>↩ Tool result · `toolu_01Xq8Jba5FkpNhQJ6VRM7SvP`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "b1f067b7-e9d9-490d-a59a-77b8aa551178",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_01GtBBkGUifqi17pu9BoNtbw`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "f8dada5e-5f8e-4820-829f-38a702c45978",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtSmskzqrtmoDmNj88EBzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 27352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
      },
      "output_tokens": 72,
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

_source line 36 · 2026-05-25T09:20:32.884Z_

<details><summary>↩ Tool result · `toolu_01GtBBkGUifqi17pu9BoNtbw`</summary>

```text
{"result":"{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "3136abc0-9f01-4e43-a557-635deb4ded64",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"pending\\\", \\\"message\\\": \\\"等待用户审批...\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"pending\", \"message\": \"等待用户审批...\"}"
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__poll_secret_request · `toolu_01Q7trvcaJ8P1cm8dGe9ayHm`</summary>

```json
{
  "request_id": "secret_req_github_anon_pat_1779700770",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "0e9d6142-1da4-43e5-9d16-623ddf263eba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkWc2hm2HPeR438MJuenmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 27497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
      },
      "output_tokens": 72,
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

_source line 38 · 2026-05-25T09:20:40.449Z_

<details><summary>↩ Tool result · `toolu_01Q7trvcaJ8P1cm8dGe9ayHm`</summary>

```text
{"result":"{\"status\": \"approved\", \"key_id\": \"github_anon_pat\", \"value\": \"[REDACTED_GITHUB_TOKEN]\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "4f87bdd1-9b95-457c-a6bf-3b5dc73ebaa6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"status\\\": \\\"approved\\\", \\\"key_id\\\": \\\"github_anon_pat\\\", \\\"value\\\": \\\"[REDACTED_GITHUB_TOKEN]\\\"}\"}",
    "structuredContent": {
      "result": "{\"status\": \"approved\", \"key_id\": \"github_anon_pat\", \"value\": \"[REDACTED_GITHUB_TOKEN]\"}"
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
Got the PAT. Now I need to:
1. Clone the repo
2. Copy latest tex/bib files
3. Comment out missing figures
4. Verify
5. Anonymity scan
6. Commit and push

I must be careful NOT to expose the PAT in any output. Let me proceed step by step.

First, let me clone the repo and also check what tex files exist locally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "dec4eef4-4115-4b3c-8408-08cbdfeeafa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXUSXZzLuXkdgwE2B7DgSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 27642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

PAT 已获取。开始 Step 1: Clone 仓库 + 查看本地 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "d2610fa1-f169-4da5-a69c-8ed754750ada",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXUSXZzLuXkdgwE2B7DgSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 27642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01KTnh3wzv4sAkdwZkg8dYP6`</summary>

```json
{
  "command": "rm -rf /tmp/anon_hotfix && git clone \"https://[REDACTED]@github.com/anonymous-nlp-2026/persuasion_turn_jailbreak_detect.git\" /tmp/anon_hotfix 2>&1 | grep -v 'ghp_\\|caoxiaoyu' && cd /tmp/anon_hotfix && git config user.name \"Anonymous\" && git config user.email \"anonymous@anonymous.invalid\" && echo \"CLONE OK\"",
  "description": "Clone anonymous repo (filtering PAT from output)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "37deec98-94be-4bed-a46c-aaf5c645d8a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXUSXZzLuXkdgwE2B7DgSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 27642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 42_

<details open><summary>🔧 Tool call — Glob · `toolu_01KQK3mBCuM79gi54dfp4XX3`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "678a1c9a-9647-4f66-b84f-85295d58a4bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXUSXZzLuXkdgwE2B7DgSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 27642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 43_

<details open><summary>🔧 Tool call — Glob · `toolu_012sndDRuqaKhMoQK1x86Z1X`</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "d7140876-9776-4759-ab1d-29bceb663c84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXUSXZzLuXkdgwE2B7DgSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 27642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 44 · 2026-05-25T09:20:53.817Z_

<details><summary>↩ Tool result · `toolu_01KTnh3wzv4sAkdwZkg8dYP6`</summary>

```text
Cloning into '/tmp/anon_hotfix'...
CLONE OK
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "b99b0863-4144-4b59-a5a6-2377c6c73c31",
  "tool_use_result": {
    "stdout": "Cloning into '/tmp/anon_hotfix'...\nCLONE OK",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T09:20:53.845Z_

<details><summary>↩ Tool result · `toolu_01KQK3mBCuM79gi54dfp4XX3`</summary>

```text
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/checklist.tex
docs/paper/appendix.tex
docs/paper/conclusion.tex
docs/paper/method.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "18b07904-aec0-4222-a69b-611269b6cb83",
  "tool_use_result": {
    "filenames": [
      "docs/paper/main.tex",
      "docs/paper/introduction.tex",
      "docs/paper/related_work.tex",
      "docs/paper/abstract.tex",
      "docs/paper/checklist.tex",
      "docs/paper/appendix.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/method.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 19,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-25T09:20:53.848Z_

<details><summary>↩ Tool result · `toolu_012sndDRuqaKhMoQK1x86Z1X`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "a47fe59f-f2cb-40f5-bb49-6e8f3b8763df",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 18,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 47_

Clone 成功。Step 2: 复制 tex 和 bib 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "e5813437-a0e9-4be8-9df1-7b447203f690",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsWdVsRZAtBhKPYoFwEF5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 27832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 878
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

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_011iA87topAPLT9bU98yt3QV`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/*.tex /tmp/anon_hotfix/docs/paper/ && cp /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/*.bib /tmp/anon_hotfix/docs/paper/ 2>/dev/null; echo \"COPY DONE\" && ls -la /tmp/anon_hotfix/docs/paper/*.tex /tmp/anon_hotfix/docs/paper/*.bib",
  "description": "Copy latest tex and bib files to anon repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "45fce05c-e430-4cc4-8f76-5d61e6922418",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsWdVsRZAtBhKPYoFwEF5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 27832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 878
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

_source line 49 · 2026-05-25T09:21:00.014Z_

<details><summary>↩ Tool result · `toolu_011iA87topAPLT9bU98yt3QV`</summary>

```text
COPY DONE
-rw-r--r-- 1 ubuntu ubuntu  1456 May 25 09:20 /tmp/anon_hotfix/docs/paper/abstract.tex
-rw-r--r-- 1 ubuntu ubuntu 64331 May 25 09:20 /tmp/anon_hotfix/docs/paper/appendix.tex
-rw-r--r-- 1 ubuntu ubuntu  3396 May 25 09:20 /tmp/anon_hotfix/docs/paper/checklist.tex
-rw-r--r-- 1 ubuntu ubuntu  4511 May 25 09:20 /tmp/anon_hotfix/docs/paper/conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu 17308 May 25 09:20 /tmp/anon_hotfix/docs/paper/experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  5084 May 25 09:20 /tmp/anon_hotfix/docs/paper/introduction.tex
-rw-r--r-- 1 ubuntu ubuntu   751 May 25 09:20 /tmp/anon_hotfix/docs/paper/main.tex
-rw-r--r-- 1 ubuntu ubuntu  5670 May 25 09:20 /tmp/anon_hotfix/docs/paper/method.tex
-rw-r--r-- 1 ubuntu ubuntu 34959 May 25 09:20 /tmp/anon_hotfix/docs/paper/references.bib
-rw-r--r-- 1 ubuntu ubuntu  3817 May 25 09:20 /tmp/anon_hotfix/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "62c1416f-cf9e-4d9c-814b-e69abcdd4b4d",
  "tool_use_result": {
    "stdout": "COPY DONE\n-rw-r--r-- 1 ubuntu ubuntu  1456 May 25 09:20 /tmp/anon_hotfix/docs/paper/abstract.tex\n-rw-r--r-- 1 ubuntu ubuntu 64331 May 25 09:20 /tmp/anon_hotfix/docs/paper/appendix.tex\n-rw-r--r-- 1 ubuntu ubuntu  3396 May 25 09:20 /tmp/anon_hotfix/docs/paper/checklist.tex\n-rw-r--r-- 1 ubuntu ubuntu  4511 May 25 09:20 /tmp/anon_hotfix/docs/paper/conclusion.tex\n-rw-r--r-- 1 ubuntu ubuntu 17308 May 25 09:20 /tmp/anon_hotfix/docs/paper/experiments.tex\n-rw-r--r-- 1 ubuntu ubuntu  5084 May 25 09:20 /tmp/anon_hotfix/docs/paper/introduction.tex\n-rw-r--r-- 1 ubuntu ubuntu   751 May 25 09:20 /tmp/anon_hotfix/docs/paper/main.tex\n-rw-r--r-- 1 ubuntu ubuntu  5670 May 25 09:20 /tmp/anon_hotfix/docs/paper/method.tex\n-rw-r--r-- 1 ubuntu ubuntu 34959 May 25 09:20 /tmp/anon_hotfix/docs/paper/references.bib\n-rw-r--r-- 1 ubuntu ubuntu  3817 May 25 09:20 /tmp/anon_hotfix/docs/paper/related_work.tex",
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

_source line 50_

Step 3: 查找并注释掉缺失图片引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "c10a87fe-ed9f-43a0-a05e-820bdecdd30e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKQKw8cGoBdRT4gKkxxBZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 28710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 697
      },
      "output_tokens": 6,
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

_source line 51_

<details open><summary>🔧 Tool call — Grep · `toolu_012nkzRYZYTfu8fwUEU1eKJP`</summary>

```json
{
  "pattern": "includegraphics.*(cka_heatmap|embedding_tsne)",
  "path": "/tmp/anon_hotfix/docs/paper/appendix.tex",
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
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "bdcf9467-f4bb-42a7-95eb-aa1c63fb253c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKQKw8cGoBdRT4gKkxxBZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 28710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 697
      },
      "output_tokens": 6,
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

_source line 52 · 2026-05-25T09:21:03.727Z_

<details><summary>↩ Tool result · `toolu_012nkzRYZYTfu8fwUEU1eKJP`</summary>

```text
186:\includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}
198:\includegraphics[width=\columnwidth]{figures/paper/embedding_tsne.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "219201d0-4e60-4e6f-ad35-a2db1a26e25e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "186:\\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}\n198:\\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 53_

找到两行。读取上下文确认后精确编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "4e4c27bc-9373-4be0-bcb7-f4aea125e074",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkZVMTN9W353T2WMAsQjUG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 29407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 221
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

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01H3Rf9tDt26HsPbv9ZYzeA7`</summary>

```json
{
  "file_path": "/tmp/anon_hotfix/docs/paper/appendix.tex",
  "offset": 184,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "5fd79f46-f629-40b3-9e93-6e67484a4f99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkZVMTN9W353T2WMAsQjUG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 29407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 221
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

_source line 55 · 2026-05-25T09:21:07.349Z_

<details><summary>↩ Tool result · `toolu_01H3Rf9tDt26HsPbv9ZYzeA7`</summary>

```text
184	\begin{figure}[t]
185	\centering
186	\includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}
187	\caption{Centered CKA similarity~\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\ 9-class block shows distinct geometries (CKA $\leq$ 0.2 on RoBERTa OOD).}
188	\label{fig:cka_heatmap}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "7d0c15e3-146b-480b-be84-aa3ec9ffe72b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/anon_hotfix/docs/paper/appendix.tex",
      "content": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}\n\\caption{Centered CKA similarity~\\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\\ 9-class block shows distinct geometries (CKA $\\leq$ 0.2 on RoBERTa OOD).}\n\\label{fig:cka_heatmap}",
      "numLines": 5,
      "startLine": 184,
      "totalLines": 961
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_016YLb7Erbszd3viHEXMTrqC`</summary>

```json
{
  "file_path": "/tmp/anon_hotfix/docs/paper/appendix.tex",
  "offset": 196,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "0f3065fb-bc6d-4f6e-a34b-118788f99f65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkZVMTN9W353T2WMAsQjUG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 29407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 221
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

_source line 57 · 2026-05-25T09:21:07.813Z_

<details><summary>↩ Tool result · `toolu_016YLb7Erbszd3viHEXMTrqC`</summary>

```text
196	\begin{figure}[ht]
197	\centering
198	\includegraphics[width=\columnwidth]{figures/paper/embedding_tsne.pdf}
199	\caption{t-SNE visualization of mean-pooled \texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}
200	\label{fig:tsne}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "6991caf0-978e-4490-bbdd-ed57ccd4d760",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/anon_hotfix/docs/paper/appendix.tex",
      "content": "\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}\n\\caption{t-SNE visualization of mean-pooled \\texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}\n\\label{fig:tsne}",
      "numLines": 5,
      "startLine": 196,
      "totalLines": 961
    }
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_019hmj2AQyvd1Lp4QmLvgWwQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/tmp/anon_hotfix/docs/paper/appendix.tex",
  "old_string": "\\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}",
  "new_string": "% \\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "a0a701aa-401f-420c-a6e5-e8f759579605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oEnXhCATMsdW1Pc1QyNZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 29628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 574
      },
      "output_tokens": 62,
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

_source line 59 · 2026-05-25T09:21:11.594Z_

<details><summary>↩ Tool result · `toolu_019hmj2AQyvd1Lp4QmLvgWwQ`</summary>

```text
The file /tmp/anon_hotfix/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "9b4118b7-50ca-4292-bf55-90b85341d53a",
  "tool_use_result": {
    "filePath": "/tmp/anon_hotfix/docs/paper/appendix.tex",
    "oldString": "\\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}",
    "newString": "% \\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}",
    "originalFile": "% appendix.tex — Supplementary material\n\n\\appendix\n\n\\section{LLM-as-Judge Baseline}\n\\label{sec:llm_judge}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}\n\\label{tab:llm_judge}\n\\begin{tabular}{@{}lcccr@{}}\n\\toprule\n\\textbf{Method} & DD & AA & IID & Unparse. \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Zero-shot}} \\\\[2pt]\nGPT-5.5 & -- & -- & .383 & 30--47\\% \\\\\nQwen3-8B & .244 & .244 & .100 & 0\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{3-shot}} \\\\[2pt]\nQwen3-8B & .566 & .652 & -- & 0\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Trained classifier}} \\\\[2pt]\n9-class (ours) & \\textbf{.994} & \\textbf{.972} & \\textbf{1.000} & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.\nOn IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\\% of responses are unparseable.\nQwen3-8B performs worse (IID F1 = 0.100).\nOn OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.\nEven with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\\geq$ 0.972.\nThe poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.\n\n\\section{Full Cross-Attack Results by Prefix}\n\\label{sec:full_prefix}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}\n\\label{tab:full_prefix}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{IID (Crescendo)}} \\\\[2pt]\n9-class (ours) & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\nMLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\\\\nVanilla DeBERTa & .968$\\pm$.033 & .978$\\pm$.016 & .987$\\pm$.000 & .982$\\pm$.014 & 1.000$\\pm$.000 \\\\\nTF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (Deceptive Delight)}} \\\\[2pt]\n9-class (ours) & .990$\\pm$.013 & .981$\\pm$.013 & .972$\\pm$.026 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nBinary & .994$\\pm$.009 & .994$\\pm$.009 & .984$\\pm$.008 & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\nScrambled & .997$\\pm$.005 & .981$\\pm$.026 & .975$\\pm$.029 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nMLM-only & .973$\\pm$.019 & .993$\\pm$.009 & .997$\\pm$.005 & .997$\\pm$.005 & .914$\\pm$.115 \\\\\nVanilla DeBERTa & .628$\\pm$.038 & .479$\\pm$.038 & .389$\\pm$.027 & .351$\\pm$.030 & .312$\\pm$.026 \\\\\nTF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (FITD)}} \\\\[2pt]\n9-class (ours) & 1.000$\\pm$.000 & .997$\\pm$.005 & -- & -- & 1.000$\\pm$.000 \\\\\nVanilla DeBERTa & .954$\\pm$.039 & .952$\\pm$.061 & -- & -- & .994$\\pm$.009 \\\\\nTF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{ActorAttack Full Results}\n\\label{sec:actorattack_full}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}\n\\label{tab:actorattack_full}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{DeBERTa-v3}} \\\\[2pt]\nBinary & .788$\\pm$.020 & \\textbf{.935$\\pm$.018} & \\textbf{.976$\\pm$.005} & \\textbf{.995$\\pm$.005} & \\textbf{.990$\\pm$.008} \\\\\n9-class & .773$\\pm$.041 & .855$\\pm$.048 & .921$\\pm$.046 & .966$\\pm$.028 & .972$\\pm$.026 \\\\\nScrambled & .652$\\pm$.034 & .804$\\pm$.053 & .854$\\pm$.046 & .910$\\pm$.052 & .951$\\pm$.043 \\\\\nMLM-only & .736$\\pm$.150 & .909$\\pm$.058 & .945$\\pm$.039 & .929$\\pm$.033 & .893$\\pm$.080 \\\\\nWiki MLM & .656$\\pm$.224 & .672$\\pm$.252 & .693$\\pm$.280 & .689$\\pm$.285 & .686$\\pm$.297 \\\\\nTopic & .513$\\pm$.077 & .580$\\pm$.109 & .565$\\pm$.100 & .615$\\pm$.111 & .625$\\pm$.141 \\\\\nVanilla & .337$\\pm$.049 & .306$\\pm$.026 & .284$\\pm$.011 & .262$\\pm$.006 & .258$\\pm$.000 \\\\\nTF-IDF LR & .633 & .730 & .571 & .242 & .261 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RoBERTa}} \\\\[2pt]\n9-class & \\textbf{.738$\\pm$.033} & .805$\\pm$.033 & .884$\\pm$.066 & .925$\\pm$.066 & .939$\\pm$.046 \\\\\nMLM & .633$\\pm$.133 & .665$\\pm$.150 & .713$\\pm$.174 & .719$\\pm$.184 & .730$\\pm$.201 \\\\\nVanilla & .410$\\pm$.126 & .425$\\pm$.143 & .432$\\pm$.144 & .466$\\pm$.144 & .466$\\pm$.163 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:actorattack_full} reveals three distinct prefix-length patterns. The 9-class model improves monotonically from $K$=1 to Full (+20\\,pp), consistent with cumulative evidence accumulation across turns. Vanilla DeBERTa \\emph{decreases} with more turns (0.337 at $K$=1 to 0.258 at Full), suggesting that additional attack turns push representations further into benign embedding regions. MLM peaks at $K$=3 (0.945) then declines to 0.893 at Full, indicating that unsupervised domain exposure captures early-turn patterns but is unstable under extended sequences.\n\n\\subsection{Error Analysis}\n\\label{app:aa_error}\n\nPer-sample majority vote across 3 seeds yields 98.3\\% accuracy on ActorAttack OOD (2 false negatives, 0 false positives). No sample is misclassified by all three seeds; all 7 seed-specific errors are false negatives concentrated in shorter conversations (3--6 turns). On these 7 error samples, vanilla achieves 0/3 correct votes per sample, while 9-class majority vote correctly classifies 5/7, confirming that domain adaptation provides robust per-sample coverage even where individual seeds fail.\n\n\\section{Perturbation Robustness}\n\\label{sec:perturbation_full}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\\Delta$: F1 degradation (pp). Classification-supervised variants achieve zero degradation at full length; this pattern does not generalize to ActorAttack.}\n\\label{tab:perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & $\\Delta$ Full & $\\Delta$ $K$=1 & $\\Delta$ $K$=2 & $\\Delta$ $K$=3 \\\\\n\\midrule\n9-class (ours) & \\textbf{0.0} & \\textbf{$-$2.6} & \\textbf{0.0} & \\textbf{0.0} \\\\\nScrambled & \\textbf{0.0} & $-$5.3 & $-$2.6 & \\textbf{0.0} \\\\\nBinary & \\textbf{0.0} & $-$9.2 & $-$2.6 & \\textbf{0.0} \\\\\n\\midrule\nTF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\\\\nMLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\\\\nTopic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \\textbf{0.0} \\\\\n\\midrule\nWikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\\\\nVanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation} shows perturbation behavior on IID data.\nClassification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.\nModels without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\\sim$12\\,pp.\nMcNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\\leq$7 discordant pairs, statistical power is limited.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\\pm$std where available.}\n\\label{tab:ood_perturbation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & Clean Full & Pert.\\ Full & $\\Delta$ Full & $\\Delta$ $K$=1 \\\\\n\\midrule\n9-class & .994$\\pm$.005 & 1.000$\\pm$.000 & +0.6 & +0.6 \\\\\nBinary & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 0.0 & +0.6 \\\\\nScrambled & .994$\\pm$.005 & 1.000$\\pm$.000 & +0.6 & $-$0.3 \\\\\n\\midrule\nJB MLM & .914$\\pm$.115 & .941 & +2.7 & 0.0 \\\\\nWiki MLM$^{*}$ & .904$\\pm$.115 & .872 & $-$3.3 & $-$3.2 \\\\\nVanilla$^{\\dagger}$ & .312$\\pm$.026 & .339$\\pm$.055 & +2.7 & $-$6.8$\\pm$1.1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\\,pp; other seeds show 0.0\\,pp change.\\\\$^{\\dagger}$Vanilla $\\Delta$ Full = +2.7\\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}\n\\end{table}\n\nOn OOD DD, the IID pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\\ vanilla significance ($p < 0.001$, 49--78 discordant pairs).\nOn OOD ActorAttack, domain-adapted variants degrade substantially (9-class $\\Delta$\\,=\\,$-$20.4$\\pm$13.5\\,pp, MLM $-$35.3\\,pp), but perturbation narrows rather than closes the adapted vs.\\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\\ vanilla 0.248 (McNemar $p < 0.001$).\nDomain specificity also manifests: Wikipedia MLM degrades by $\\sim$12\\,pp while jailbreak-domain MLM degrades by only 2.6\\,pp.\n\n\\section{Strategy Trajectory Analysis}\n\\label{sec:strategy_full}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}\n\\caption{Persuasion strategy transition count matrices for three attack families, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}\n\\label{fig:strategy_heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:strategy_heatmap} shows transition count matrices for three attack families.\nCrescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545); this reflects its gradual escalation design.\nFITD conversations show a markedly sparser pattern (541 transitions), with Role$\\to$Obfuscation (161) as the dominant transition, consistent with FITD's commitment-consistency exploitation~\\citep{cialdini2001influence}.\nDD conversations span 5 active source strategies (565 transitions), with Emotion$\\to$Obfuscation (129) as the dominant transition, aligning with DD's design of embedding harmful content within emotionally engaging contexts~\\citep{deceptivedelight2024}.\n\n\\section{Centered CKA Heatmaps}\n\\label{sec:cka_heatmap}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}\n\\caption{Centered CKA similarity~\\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\\ 9-class block shows distinct geometries (CKA $\\leq$ 0.2 on RoBERTa OOD).}\n\\label{fig:cka_heatmap}\n\\end{figure}\n\n\\section{Embedding Space Visualization}\n\\label{app:tsne}\n\nFigure~\\ref{fig:tsne} visualizes mean-pooled \\texttt{[CLS]} embeddings via t-SNE for three representative variants (Vanilla, JB-MLM, 9-Class) on DD OOD and ActorAttack. Vanilla embeddings show dispersed jailbreak clusters with ambiguous decision boundaries, while domain-adapted variants (JB-MLM, 9-Class) produce tighter, more separable clusters. JB-MLM achieves the clearest bimodal separation on both evaluation sets, consistent with its superior detection performance.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}\n\\caption{t-SNE visualization of mean-pooled \\texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}\n\\label{fig:tsne}\n\\end{figure}\n\n\\section{Cross-LLM Validation}\n\\label{app:cross_llm}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Cross-LLM validation (F1, full conversation). All models are trained on Qwen3-8B data; conditions vary the source of jailbreak (JB) and benign (ben.) conversations at inference. Values are evaluated under a matched 50-sample subset protocol and differ from Table~\\ref{tab:evidence_hierarchy}, which uses the full evaluation set.}\n\\label{tab:cross_llm}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n& \\multicolumn{3}{c}{\\textit{DD Full}} & \\multicolumn{3}{c}{\\textit{AA Full}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Condition} & Van. & MLM & 9-cl. & Van. & MLM & 9-cl. \\\\\n\\midrule\nQwen JB + Qwen ben. & .312 & .914 & .997 & .258 & .893 & .972 \\\\\nLlama JB + Llama ben. & .261 & .282 & .433 & .261 & .368 & .321 \\\\\nLlama JB + Qwen ben. & .302 & .778$^{*}$ & 1.000 & .302 & .903 & .801 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$High seed variance (std = 0.306): seed 456 outlier (F1 = 0.345); remaining two seeds achieve F1 $\\geq$ 0.97.}\n\\end{table}\n\nTable~\\ref{tab:cross_llm} shows three inference conditions. When both jailbreak and benign text come from Llama (row~2), all variants collapse (F1 = 0.26--0.43), but this conflates two sources of distribution shift: unfamiliar jailbreak patterns and unfamiliar benign text. Row~3 isolates jailbreak transferability by pairing Llama jailbreaks with the original Qwen benign distribution. Under this condition, 9-class recovers to F1 = 1.000 on DD and 0.801 on ActorAttack, and JB-MLM reaches 0.903 on ActorAttack. The contrast between rows~2 and~3 shows that the dominant failure mode in row~2 is benign distribution mismatch (false positives from unfamiliar benign text), not inability to recognize cross-LLM jailbreak patterns. Vanilla remains at 0.26--0.31 across all conditions, further confirming that encoders without DAPT lack OOD detection capability regardless of the LLM source. The residual degradation on ActorAttack (0.801 vs.\\ 0.972) reflects genuine cross-LLM variation in structurally complex attack patterns.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Error decomposition for DD Full cross-LLM conditions (matched 50-sample subsets). TP rate is identical across benign conditions; the F1 collapse in the Llama-only condition (Table~\\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text.}\n\\label{tab:cross_llm_error}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Metric} & Van. & MLM & 9-cl. \\\\\n\\midrule\nTP rate (Llama JB) & 0.0\\% & 68.0\\% & 100.0\\% \\\\\nFP rate (Llama ben.) & 29.3\\% & 88.0\\% & 90.0\\% \\\\\nFP rate (Qwen ben.) & 0.0\\% & 0.9\\% & 0.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_llm_error} decomposes DD Full F1 into true positive and false positive rates. TP rates are identical regardless of the benign source: domain-adapted models detect Llama-generated jailbreaks at the same rate whether evaluated against Qwen or Llama benign text. The F1 collapse in the full Llama condition (Table~\\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text (FP rate: 88--90\\% on Llama vs.\\ 0--0.9\\% on Qwen for adapted variants). The model implicitly treats non-Qwen text style as a jailbreak indicator, a spurious correlation from single-LLM training data. This failure reflects a data diversity limitation, not a methodological one; mixed-LLM training (Table~\\ref{tab:mixed_llm}) partially addresses this confound.\n\n\\section{Mixed-LLM Training Results}\n\\label{app:mixed_llm}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Mixed-LLM training (250 Qwen + 250 Llama conversations, 3-seed mean$\\pm$std where available). ToxicChat evaluated on balanced set (408 conversations).}\n\\label{tab:mixed_llm}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Variant} & Mixed & DD OOD & AA OOD & FITD OOD & ToxicChat \\\\\n\\midrule\n9-class & \\textbf{.996$\\pm$.006} & \\textbf{.818$\\pm$.096} & \\textbf{.504$\\pm$.107} & \\textbf{.997$\\pm$.005} & \\textbf{.550$\\pm$.052} \\\\\nMLM & .681$\\pm$.226 & .289$\\pm$.101 & .258$\\pm$.075 & .679$\\pm$.188 & .256$\\pm$.053 \\\\\nVanilla & .802$\\pm$.010 & .291$\\pm$.065 & .389$\\pm$.073 & .867$\\pm$.022 & .356$\\pm$.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:mixed_llm} reports detection performance when training on a mixed corpus of Qwen3-8B and Llama-3.1-8B conversations. Classification-based DAPT (9-class) maintains the strongest DD OOD performance (0.818$\\pm$0.096), outperforming both vanilla (0.291$\\pm$0.065) and MLM (0.289$\\pm$0.101) by 53\\,pp. ActorAttack remains challenging under mixed-LLM conditions (9-class F1\\,=\\,0.504$\\pm$0.107), suggesting structurally complex attacks require larger or more diverse training data. ToxicChat performance shows no significant improvement over single-source training (0.550$\\pm$0.052 vs.\\ 0.596$\\pm$0.087; Section~\\ref{sec:human_data}), consistent with ToxicChat being zero-shot single-turn transfer rather than a standard OOD benchmark.\n\n\\section{Dataset Scale Validation}\n\\label{app:scale_validation}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Dataset scale validation (1{,}000 Qwen conversations, 3-seed mean$\\pm$std). IID results omitted due to train/test overlap (71\\% of original test set present in expanded training data).}\n\\label{tab:scale_validation}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Variant} & DD OOD & AA OOD \\\\\n\\midrule\n9-class & \\textbf{.889$\\pm$.041} & \\textbf{.913$\\pm$.041} \\\\\nMLM & .338$\\pm$.010 & .351$\\pm$.018 \\\\\nVanilla & .326$\\pm$.000 & .508$\\pm$.085 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale_validation} validates robustness to dataset scale by doubling the training corpus from 500 to 1{,}000 conversations with new topic seeds. The hierarchy 9-class $\\gg$ MLM $\\approx$ vanilla holds at 2$\\times$ scale: classification-based DAPT maintains 40--56\\,pp advantage over vanilla, while MLM provides no improvement over vanilla on either attack family (DD: 0.338 vs.\\ 0.326; AA: 0.351 vs.\\ 0.508).\n\nThe performance decline at 1{,}000 conversations may reflect distributional heterogeneity introduced by diverse topic seeds: the additional conversations broaden the training distribution, potentially diluting the concentrated attack-relevant features that smaller, more homogeneous datasets preserve. IID evaluation was precluded by train/test overlap in the expanded dataset (71\\%), limiting analysis to OOD metrics. Human-data validation also degrades under scaled training (ToxicChat F1: 0.596 $\\to$ 0.341), suggesting the expanded distribution shifts representations away from features useful for both synthetic OOD and human data.\n\n\\section{RoBERTa-large DAPT Learning Rate Control}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{RoBERTa-large (355M) DAPT learning rate control on OOD Full (3-seed mean$\\pm$std). Reducing the learning rate worsens both DD and AA, ruling out over-adaptation as the cause of the regression in Table~\\ref{tab:cross_encoder}.}\n\\label{tab:roberta_large_lr}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Config} & DD Full & AA Full \\\\\n\\midrule\nVanilla (no DAPT) & .927$\\pm$.036 & 1.000$\\pm$.000 \\\\\n9-class, LR=$2 \\times 10^{-5}$ & .987$\\pm$.004 & .946$\\pm$.057 \\\\\n9-class, LR=$1 \\times 10^{-5}$ & .948$\\pm$.034 & .781$\\pm$.054 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nReducing the DAPT learning rate from $2 \\times 10^{-5}$ to $1 \\times 10^{-5}$ worsens both DD and AA performance, which rules out over-adaptation as the cause of the regression observed in Table~\\ref{tab:cross_encoder}. An MLM-only variant (without classification) produces the same pattern (AA Full = 0.874$\\pm$0.014); representation drift from continued pretraining, not classification-specific bias, is the underlying cause. Domain-adaptive fine-tuning narrows the representation space of a sufficiently large encoder and reduces its inherent OOD generalization ability.\n\n\\section{TOST Equivalence Sensitivity Analysis}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{TOST equivalence test (scrambled vs.\\ 9-class, $\\delta$=5\\,pp, 10 seeds). $p < 0.05$ confirms equivalence within $\\pm\\delta$.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Dataset} & $p$ & $d$ & Equivalent? \\\\\n\\midrule\nDD OOD & $2.06 \\times 10^{-9}$ & $-$0.136 & \\checkmark \\\\\nFITD OOD & $\\approx 0$ & 0.000 & \\checkmark \\\\\nActorAttack & .183 & 0.440 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn our 80-sample test set, $\\delta = 5$\\,pp corresponds to $\\approx$4 additional missed attacks. We choose $\\delta$\\,=\\,5\\,pp as a conservative threshold; equivalence holds even at $\\delta$\\,=\\,3\\,pp on DD ($p < 0.001$, $n$\\,=\\,10) and FITD ($p \\approx 0$). With 10 seeds at $\\delta$\\,=\\,5\\,pp, DD and FITD confirm formal equivalence ($p < 10^{-8}$, $|d| \\leq 0.14$), demonstrating that label correctness is not a detection factor for template attacks. On ActorAttack, the mean gap is 3.0\\,pp with moderate effect size ($d$\\,=\\,0.44); TOST does not confirm equivalence ($p$\\,=\\,0.183), indicating that strategy-diverse attacks retain some sensitivity to label quality.\n\n\\section{Partition Robustness and Topic Failure Analysis}\n\\label{app:random_partition}\n\\label{app:topic_failure}\n\n\\subsection{Random Binary Partition Robustness}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{OOD F1 for 10 random binary partitions of the 9 strategy labels (each partition randomly assigns strategies to group A or B). All partitions use identical Stage-1 DAPT and Stage-2 GRU training; only the binary label mapping differs. Seed 42 (3 runs).}\n\\label{tab:random_partition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Partition} & \\textbf{Group A} & \\textbf{IID} & \\textbf{DD OOD} & \\textbf{AA OOD} \\\\\n\\midrule\n0 & \\{0,2,4,5,7\\} & 1.000 & 1.000 & 1.000 \\\\\n1 & \\{1,3,5,6,8\\} & 1.000 & 1.000 & 1.000 \\\\\n2 & \\{0,1,3,7,8\\} & 1.000 & 1.000 & 1.000 \\\\\n3 & \\{2,4,5,6,7\\} & 1.000 & 1.000 & 1.000 \\\\\n4 & \\{0,1,2,6,8\\} & 1.000 & 1.000 & 1.000 \\\\\n5 & \\{0,3,4,7,8\\} & 1.000 & 1.000 & 1.000 \\\\\n6 & \\{1,2,3,5,6\\} & 1.000 & 1.000 & 1.000 \\\\\n7 & \\{1,4,6,7\\}   & 1.000 & 1.000 & 0.636 \\\\\n8 & \\{0,2,3,4,8\\} & 1.000 & 1.000 & 1.000 \\\\\n9 & \\{0,1,5,7,8\\} & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\nMean$\\pm$Std &  & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 0.964$\\pm$.109 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll 10 partitions achieve perfect IID and DD OOD detection regardless of how the 9 strategy labels are split into two groups. On ActorAttack, 9/10 partitions achieve F1\\,=\\,1.000; the sole outlier (partition~7, AA F1\\,=\\,0.636) uses a 4/5 split that isolates a specific strategy cluster. The near-universal success confirms that domain-relevant binary classification---not specific label semantics---drives cross-attack generalization on template attacks. The AA outlier is consistent with the complexity-dependent boundary observed in Section~\\ref{sec:decomposition}: structurally complex attacks are sensitive to specific partition choices while template attacks are not.\n\n\\subsection{Topic Classification Failure Analysis}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Per-turn Fisher ratio (mean across all dimensions) and silhouette score between jailbreak and benign turn embeddings (\\texttt{[CLS]} representations). Higher values indicate greater per-turn separability.}\n\\label{tab:topic_failure}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Fisher (mean)} & \\textbf{Silhouette} \\\\\n\\midrule\nVanilla  & IID test & 0.118 & 0.034 \\\\\nVanilla  & DD OOD  & 0.401 & 0.411 \\\\\nVanilla  & AA OOD  & 0.408 & 0.330 \\\\\n\\midrule\n9-class DAPT & IID test & 0.073 & 0.048 \\\\\n9-class DAPT & DD OOD  & 0.200 & 0.079 \\\\\n9-class DAPT & AA OOD  & 0.832 & 0.301 \\\\\n\\midrule\nTopic DAPT & IID test & 0.108 & 0.076 \\\\\nTopic DAPT & DD OOD  & 0.653 & 0.274 \\\\\nTopic DAPT & AA OOD  & 0.311 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTopic DAPT achieves \\emph{higher} per-turn Fisher separability than 9-class DAPT on IID and DD (0.653 vs.\\ 0.200 on DD) yet produces far worse conversation-level detection (F1\\,=\\,0.541 vs.\\ 0.994). This rules out per-turn separability destruction as the failure mechanism. The 9-class model instead greatly expands the embedding space (centroid $L_2$ distance 7.5--27.6 vs.\\ 0.9--1.1 for vanilla) while distributing both classes broadly, creating richer representation geometry that the downstream GRU exploits over the turn sequence. Topic classification teaches features that separate turns individually but are temporally inconsistent across a conversation---high per-turn separability does not guarantee that the GRU can learn a stable conversation-level decision boundary.\n\n\\section{Reproducibility Details}\n\\label{sec:reproducibility}\n\n\\paragraph{Stage-1 training.}\nAll variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \\times 10^{-5}$, AdamW optimizer ($\\beta_1$=0.9, $\\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\\% of steps, batch size 16, and 4 epochs. MLM variants use 15\\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).\n\n\\paragraph{Stage-2 training.}\nThe BiGRU has hidden dimension 256, 2 layers, and dropout 0.3 (bidirectional, so output dimension 512). The MLP classifier has layers $512 \\to 256 \\to 2$ with ReLU activation. Training uses learning rate $1 \\times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.\n\n\\paragraph{Data generation.}\nJailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.\n\n\\paragraph{Strategy annotation.}\nEach user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. All generation and annotation prompts, the full dataset, and training code are available at \\url{https://github.com/anonymous-nlp-2026/persuasion_turn_jailbreak_detect}.\n\n\\paragraph{Adversarial paraphrasing.}\nThe paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.\n\n\\paragraph{Cross-checkpoint variance.}\nTo disentangle Stage-1 from Stage-2 variance, we evaluate three independently trained 9-class DAPT checkpoints (seeds 42, 123, 456) with a fixed downstream BiGRU seed (42). Results: IID F1\\,=\\,1.000$\\pm$0.000, DD OOD\\,=\\,0.926$\\pm$0.026, AA OOD\\,=\\,0.935$\\pm$0.013. Stage-1 training is stable (OOD std\\,$\\leq$\\,2.6\\,pp), confirming that the variance reported in the main paper is not dominated by Stage-1 initialization.\n\n\\section{End-to-End Fine-Tuning Upper Bound}\n\\label{app:e2e}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Frozen probing vs.\\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\\pm$std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\\ref{tab:main_results}--\\ref{tab:evidence_hierarchy}); Table~\\ref{tab:frozen_verify} uses independently trained checkpoints, yielding higher frozen accuracy (DD\\,=\\,.997, AA\\,=\\,.972) and a narrower E2E gap ($\\leq$2.5\\,pp).}\n\\label{tab:e2e}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Config} & IID & DD OOD & AA OOD \\\\\n\\midrule\nFrozen probing & 1.000$\\pm$.000 & .994$\\pm$.005 & .939$\\pm$.047 \\\\\nE2E fine-tuning & 1.000$\\pm$.000 & 1.000$\\pm$.000 & \\textbf{.997$\\pm$.005} \\\\\n\\midrule\n$\\Delta$ & .000 & +.006 & +.058 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnd-to-end fine-tuning unfreezes the Stage-1 encoder during Stage-2 BiGRU training, allowing gradient flow through the full pipeline. On IID and OOD DD, the two configurations are indistinguishable; on structurally complex ActorAttack, E2E recovers +5.8\\,pp. The modest gain confirms that frozen probing captures the vast majority of discriminative information encoded by Stage-1 DAPT, and that the remaining OOD gap in the frozen setting reflects downstream optimization constraints rather than missing representational capacity.\n\n\\section{Real-World False Positive Rate}\n\\label{app:wildchat_fpr}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{False positive rate (\\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\\pm$std.}\n\\label{tab:wildchat_fpr}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & Seed 42 & Seed 123 & Seed 456 & Mean$\\pm$Std \\\\\n\\midrule\n9-class & 66.8 & 61.1 & 76.5 & 68.1$\\pm$6.4 \\\\\nMLM & 36.7 & 64.6 & 32.3 & 44.5$\\pm$14.3 \\\\\nVanilla & 47.3 & 42.5 & 54.4 & 48.1$\\pm$4.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:wildchat_fpr} evaluates false positive rates on 226 WildChat benign multi-turn conversations from real GPT-3.5 users (avg 7.4 turns). All variants produce FPR far exceeding deployable thresholds: 9-class is worst at 68.1\\%, followed by vanilla (48.1\\%) and MLM (44.5\\%). Domain adaptation \\emph{increases} FPR relative to vanilla (+20\\,pp for 9-class), indicating that continued pretraining amplifies dependence on the training benign distribution. This is consistent with the cross-LLM false positive spike (Table~\\ref{tab:cross_llm_error}): models trained on synthetic Qwen3-8B benign text implicitly treat unfamiliar conversational styles as jailbreak indicators. High MLM seed variance (std\\,=\\,14.3\\%) suggests that unsupervised pretraining is particularly unstable under benign distribution shift. Deployment requires per-domain benign calibration or mixed-source benign training data.\n\n\\paragraph{Post-hoc calibration.}\nROC AUC\\,=\\,0.700$\\pm$0.054 indicates insufficient discrimination between WildChat benign and jailbreak conversations at the representation level. At TPR$\\geq$95\\%, the optimal threshold still yields FPR\\,=\\,62.7\\%, far above deployable levels. Temperature scaling cannot improve this trade-off, as ROC curves are invariant to monotonic score transforms. The AUC ceiling reflects genuine domain shift: WildChat benign and jailbreak representations overlap substantially, and no post-hoc calibration can overcome this; in-domain benign adaptation is required.\n\n\\paragraph{Second benign source: OASST2.}\n\\label{app:oasst2}\n\nTo test whether benign-side shift generalizes beyond WildChat, we evaluate on 200 benign multi-turn conversations from OpenAssistant OASST2~\\citep{kopf2023openassistant}---a crowdsourced dataset of real human conversations, distinct from WildChat (GPT-3.5 user logs) in both authorship and topic distribution.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{OASST2 benign adaptation curve: FPR on 200 OASST2 benign conversations and OOD jailbreak detection F1 as a function of $N$ OASST2 conversations added to training. Seed 42. Compare WildChat (Table~\\ref{tab:wildchat_fpr}): FPR reaches 0\\% at $N$\\,=\\,10.}\n\\label{tab:oasst2_curve}\n\\begin{tabular}{@{}rccccc@{}}\n\\toprule\n$N$ & FPR (\\%) & IID F1 & DD F1 & AA F1 & FITD F1 \\\\\n\\midrule\n0 & 57.5 & -- & -- & -- & -- \\\\\n10 & 20.5 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n25 & \\textbf{1.5} & 1.000 & 1.000 & 0.953 & 1.000 \\\\\n50 & \\textbf{0.5} & 1.000 & 1.000 & 0.990 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBaseline FPR on OASST2 (57.5\\%) is comparable to WildChat (68.1\\%), confirming that benign-side shift is not source-specific but a general consequence of synthetic-only benign training. The adaptation curve follows the same pattern---monotonic FPR reduction with preserved OOD detection---but requires more samples: 25 conversations reduce FPR to 1.5\\% (vs.\\ 0\\% at $N$\\,=\\,10 for WildChat), and 50 conversations reach 0.5\\%. The slower convergence likely reflects greater distributional distance between crowdsourced OASST2 conversations and the synthetic training distribution compared to WildChat's GPT-3.5 user logs.\n\n\\subsection{Estimated Dual-OOD Detection Performance}\n\\label{app:dual_ood}\n\nThe OOD detection F1 reported in the main paper evaluates attack-side OOD with IID benign examples (FPR\\,=\\,0), providing an upper bound. To estimate performance when \\emph{both} attack and benign inputs are OOD, we combine per-seed attack recall (from OOD evaluation) with per-seed benign FPR (from WildChat/OASST2 experiments), assuming independence between attack detection and benign false positives. For each seed, we compute binary detection F1 from the resulting TP, FP, FN counts on the OOD test composition (80 jailbreak + 38 benign).\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Estimated dual-OOD binary detection F1 under different benign conditions (3-seed mean$\\pm$std). Attack recall held fixed from OOD evaluation; only benign FPR varies. IID row corresponds to the benign-IID upper bound (FPR\\,=\\,0).}\n\\label{tab:dual_ood}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Benign condition} & DD OOD F1 & AA OOD F1 \\\\\n\\midrule\nIID (FPR\\,=\\,0) & .994$\\pm$.009 & .981$\\pm$.019 \\\\\nWildChat, no adapt & .855$\\pm$.020 & .842$\\pm$.012 \\\\\nOASST2, no adapt & .874$\\pm$.009 & .861$\\pm$.018 \\\\\nWildChat + 10-shot & .994$\\pm$.009 & .981$\\pm$.019 \\\\\nOASST2 + 25-shot & .991$\\pm$.009 & .978$\\pm$.018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithout benign adaptation, dual-OOD F1 drops by 13--14\\,pp (DD: $.994 \\to .855$; AA: $.981 \\to .842$), driven entirely by false positives on OOD benign inputs. After few-shot adaptation---10 WildChat or 25 OASST2 conversations---dual-OOD F1 recovers to within 0.3\\,pp of the IID upper bound, confirming that the lightweight adaptation procedure (Section~\\ref{sec:benign_shift}) effectively closes the benign distribution gap without compromising attack-side performance.\n\n\\section{BERT-base Proxy Baseline}\n\\label{app:bert_proxy}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{BERT-base-uncased (110M) frozen probing without DAPT, matching DeepContext's encoder family~\\citep{deepcontext2026}. 3-seed mean$\\pm$std. DeBERTa-v3 results from Table~\\ref{tab:cross_encoder} for comparison.}\n\\label{tab:bert_proxy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Encoder} & IID & DD OOD & AA OOD \\\\\n\\midrule\nBERT-base (110M), no DAPT & .996$\\pm$.006 & .318$\\pm$.031 & .275$\\pm$.027 \\\\\nDeBERTa-v3 (184M), no DAPT & 1.000$\\pm$.000 & .312$\\pm$.043 & .258$\\pm$.000 \\\\\nDeBERTa-v3 (184M), 9-class & 1.000$\\pm$.000 & .994$\\pm$.005 & .939$\\pm$.047 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:bert_proxy} compares BERT-base-uncased (110M parameters, matching DeepContext's encoder) against DeBERTa-v3-base (184M), both without domain-adaptive pretraining. The two vanilla encoders achieve comparable OOD performance (DD: 0.318 vs.\\ 0.312; AA: 0.275 vs.\\ 0.258), despite a 1.7$\\times$ parameter difference and different pretraining procedures. Both collapse on OOD evaluation while 9-class DAPT recovers to 0.994 (DD) and 0.939 (AA). This confirms that cross-attack generalization is driven by domain adaptation, not encoder architecture or capacity at this scale.\n\n\\section{Confidence Calibration}\n\\label{app:calibration}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Expected calibration error (ECE, 10 bins) for 9-class and vanilla on IID and OOD evaluation (3-seed mean$\\pm$std). Lower is better.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Variant} & IID & DD OOD & AA OOD \\\\\n\\midrule\n9-class & $\\approx$0.000 & 0.143$\\pm$0.053 & 0.116$\\pm$0.053 \\\\\nVanilla & 0.009$\\pm$0.007 & 0.669$\\pm$0.004 & 0.504$\\pm$0.066 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 9-class model achieves substantially lower ECE than vanilla on OOD data (0.12--0.14 vs.\\ 0.50--0.67), indicating that domain adaptation improves not only discriminative performance but also confidence calibration. IID calibration is near-perfect for both variants. The residual OOD ECE (0.12--0.14) suggests that temperature scaling could further improve deployment reliability.\n\n\\subsection{ToxicChat False Positive Confidence}\n\\label{app:confidence}\n\nOn ToxicChat, 9-class false positives are overwhelmingly high-confidence: 70.2\\% of majority-vote FPs exceed $p > 0.9$ (median 0.999), compared to 58.8\\% for JB-MLM (median 0.933). Per-seed analysis is more extreme---94--98\\% of single-model 9-class FPs are high-confidence (median 1.0), with the borderline fraction (25\\%) in majority vote arising from cross-seed disagreement rather than individual model uncertainty. This confirms that the 9-class ToxicChat FPR reflects systematic feature misalignment---classification DAPT shifts benign text into the jailbreak region with high confidence---rather than boundary ambiguity.\n\n\\section{Frozen Probing Verification}\n\\label{app:frozen_verify}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Frozen probing vs.\\ end-to-end (E2E) fine-tuning (3-seed mean$\\pm$std). 9-class: primary DAPT checkpoints; MLM: matched MLM control checkpoints. Frozen probing trains only BiGRU+MLP on frozen DAPT embeddings.}\n\\label{tab:frozen_verify}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Config} & IID & DD OOD & AA OOD & FITD OOD \\\\\n\\midrule\nFrozen 9-class & 1.000$\\pm$.000 & .997$\\pm$.005 & .972$\\pm$.026 & 1.000$\\pm$.000 \\\\\nFrozen MLM & .982$\\pm$.016 & .993$\\pm$.009 & .941$\\pm$.037 & .987$\\pm$.009 \\\\\nE2E 9-class & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .997$\\pm$.005 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:frozen_verify} compares frozen probing across DAPT objectives and against end-to-end fine-tuning. On easy OOD (DD, FITD), frozen MLM and frozen 9-class representations perform comparably ($\\Delta \\leq 1.3$\\,pp). On hard OOD (ActorAttack), 9-class retains a modest advantage (0.972 vs.\\ 0.941, $\\Delta$\\,=\\,3.1\\,pp) with lower variance ($\\sigma$\\,=\\,0.026 vs.\\ 0.037). Both far exceed vanilla encoders ($\\leq$0.318; Table~\\ref{tab:bert_proxy}). The E2E advantage over frozen 9-class is $\\leq$2.5\\,pp, confirming that Stage-1 representation quality is the primary source of OOD generalization.\n\nA striking asymmetry emerges when comparing frozen probing to the full pipeline (Table~\\ref{tab:evidence_hierarchy}): MLM frozen representations \\emph{outperform} the full MLM pipeline on AA OOD (0.941 vs.\\ 0.893), while 9-class frozen exactly matches its full pipeline (0.972 vs.\\ 0.972). This indicates that MLM's cross-seed instability originates in Stage-2 BiGRU training rather than Stage-1 DAPT: the MLM encoder produces adequate representations that are then degraded by unstable downstream optimization. Classification DAPT, by contrast, produces representations that remain robust through Stage-2 training, explaining its consistently lower variance (Table~\\ref{tab:evidence_hierarchy}).\n\nThis two-level structure (DAPT vs.\\ no-DAPT producing a representation quality leap of +70\\,pp; classification vs.\\ MLM DAPT producing a stability difference) is consistent with two further observations: $\\lambda$=0 matches $\\lambda > 0$ during E2E fine-tuning (Table~\\ref{tab:lambda}), and mean pooling matches BiGRU under E2E (Table~\\ref{tab:temporal}). Once DAPT representations are strong, downstream configuration details have minimal impact.\n\n\\subsection{Single-Turn Truncation Analysis}\n\\label{app:truncated}\n\nTo isolate whether the ToxicChat evidence-hierarchy reversal (Section~\\ref{sec:discussion}) reflects multi-turn structural dependence, we truncate each synthetic test conversation to its last user turn and re-evaluate both 9-class and JB-MLM models (3-seed mean).\n\n\\begin{table}[h]\n\\centering\n\\caption{Full-conversation vs.\\ last-turn-only F1 (3-seed mean). Truncation widens the 9-class advantage, ruling out multi-turn structure as the driver of the ToxicChat reversal.}\n\\label{tab:truncated}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Mode} & \\textbf{9-class} & \\textbf{JB-MLM} \\\\\n\\midrule\nIID & Full & 1.000 & .983 \\\\\nIID & Last turn & .991 & .894 \\\\\n\\midrule\nDD OOD & Full & .997 & .993 \\\\\nDD OOD & Last turn & .942 & .924 \\\\\n\\midrule\nAA OOD & Full & .972 & .941 \\\\\nAA OOD & Last turn & .978 & .927 \\\\\n\\midrule\nFITD OOD & Full & 1.000 & .987 \\\\\nFITD OOD & Last turn & 1.000 & .927 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize Mean $\\Delta$ (9-class $-$ MLM): Full +1.6\\,pp, Last turn +6.0\\,pp. 9-class advantage widens under truncation across all families, indicating the reversal on ToxicChat is driven by distributional differences between synthetic and human text, not by multi-turn structural dependence.}\n\\end{table}\n\n\\paragraph{Representation geometry analysis.}\n\\label{app:representation}\n\nTo characterize the mechanism behind classification DAPT's robustness, we analyze Stage-1 representations across all seven DeBERTa-v3-base variants (seed 42). We extract \\texttt{[CLS]} embeddings from 150 test conversations (50 IID + 50 DD OOD + 50 AA OOD) and compute three metrics.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Representation geometry and class separability across Stage-1 variants. PR: participation ratio (effective dimensionality of the embedding space). Fisher ratio: inter-class distance$^2$ / sum of intra-class variances. Weight $\\Delta$: L2 distance from pretrained weights (relative to pretrained norm).}\n\\label{tab:representation}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Variant} & \\textbf{PR} & \\textbf{Fisher} & \\textbf{Wt.\\ $\\Delta$ (\\%)} \\\\\n\\midrule\nVanilla & 31.9 & $<$0.001 & 0.000 \\\\\nWiki-MLM & 25.0 & $<$0.001 & 0.221 \\\\\nJB-MLM & 24.6 & $<$0.001 & 0.256 \\\\\nTopic & 14.5 & 0.012 & 0.371 \\\\\nScrambled & 7.8 & 2.60 & 0.283 \\\\\n9-class & 9.4 & 4.47 & 0.303 \\\\\nBinary & 3.7 & 19.7 & 0.239 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nClassification variants compress representations into 2--9 effective dimensions (vs.\\ 25--32 for MLM/vanilla) while increasing Fisher ratio by 3--5 orders of magnitude. Weight distances from pretrained are comparable across all variants ($\\sim$0.2--0.4\\%), indicating that the mechanism is representational restructuring rather than parameter-space regularization. Scrambled labels produce similar compression (PR\\,=\\,7.8, Fisher\\,=\\,2.6), confirming that the classification objective structure---not label semantics---drives discriminative compression.\n\n\\paragraph{Layer-wise localization.}\n\\label{app:layerwise}\n\nTo determine \\emph{where} discriminative compression occurs, we compute PR and Fisher ratio at every DeBERTa-v3-base layer (0--12) for four variants (9-class, scrambled, JB-MLM, vanilla) using the same 236-sample evaluation set (seed 42).\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig_layerwise_representation.pdf}\n\\caption{Layer-wise representation analysis. (a)~Participation ratio: classification variants (9-class, scrambled) show sharp dimensional collapse at layers 9--10 (PR\\,$\\approx$\\,1.5--2.9) while vanilla/JB-MLM maintain high dimensionality (PR\\,$\\approx$\\,7--10). (b)~Fisher ratio (log scale): class separability diverges from layer 8, with 9-class peaking at 10.9 (layer 10) vs.\\ vanilla 0.73 (15$\\times$).}\n\\label{fig:layerwise}\n\\end{figure}\n\nLayers 0--7 show no systematic divergence across variants (Fisher\\,$<$\\,2.1 for all; PR tracks similar oscillation patterns), consistent with \\citet{maennel2020random}'s finding that early layers learn label-independent features. From layer 8 onward, classification-supervised variants diverge sharply: 9-class Fisher rises from 3.2 (layer 8) to 10.9 (layer 10, peak), while vanilla remains below 1.5 throughout. Simultaneously, 9-class PR drops from 3.4 to 1.5 at layer 10---a 6.6$\\times$ compression relative to vanilla (PR\\,=\\,9.7). JB-MLM tracks vanilla across all layers (Fisher\\,$\\leq$\\,3.3, PR\\,$\\geq$\\,1.4), confirming that MLM does not induce discriminative restructuring. Scrambled labels exhibit the same late-layer pattern (Fisher peaks at 7.9, layer 12; PR drops to 1.5, layer 12), reinforcing that any classification signal---regardless of label semantics---triggers late-layer compression.\n\n\\paragraph{Discriminative subspace probe.}\n\\label{app:discriminative_probe}\n\nTo test whether the compressed subspace is \\emph{sufficient} for OOD detection, we project layer-10 \\texttt{[CLS]} representations onto the top-$k$ SVD components and train a logistic regression probe (3 seeds, sklearn default). Controls: random $k$-dimensional projections (10 random bases, mean reported) and vanilla/MLM models under identical projection.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Discriminative subspace probe: OOD F1 when projecting layer-10 representations onto top-$k$ SVD components vs.\\ random $k$-dimensional projections. 9-class top-3 achieves perfect AA detection with 3/768 dimensions; MLM fails even with all 768.}\n\\label{tab:discriminative_probe}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Projection} & DD & AA & FITD \\\\\n\\midrule\n9-class & top-3 & 1.000 & \\textbf{1.000} & 1.000 \\\\\n9-class & top-5 & 1.000 & 1.000 & 1.000 \\\\\n9-class & random-3 & 1.000 & 0.928$\\pm$.129 & 1.000 \\\\\n9-class & random-5 & 1.000 & 0.952 & 1.000 \\\\\n9-class & full-768 & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\nscrambled & top-3 & 1.000 & 0.962 & 1.000 \\\\\nscrambled & random-3 & 0.981 & 0.766 & 0.987 \\\\\n\\midrule\nJB-MLM & top-3 & 1.000 & 0.618 & 1.000 \\\\\nJB-MLM & full-768 & 1.000 & 0.636 & 1.000 \\\\\nJB-MLM & random-5 & 0.685 & 0.584 & 0.744 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings establish a link between compression and generalization (Table~\\ref{tab:discriminative_probe}). First, 9-class top-3 achieves perfect ActorAttack detection (F1\\,=\\,1.000) using only 3 of 768 dimensions---all discriminative information resides in the compressed subspace. Second, random 3-dimensional projections degrade to 0.928 on AA, confirming that the specific SVD directions matter. Third, JB-MLM reaches only 0.636 on AA even with all 768 dimensions, demonstrating that without classification-induced compression, the representation lacks the structure needed for cross-attack generalization. DD and FITD are near-ceiling for all models, making ActorAttack the critical test.\nSVD directions computed on IID training data only (without OOD test exposure) yield equal or higher F1 than all-data SVD (AA: 0.947 vs.\\ 0.904), confirming the subspace is not an artifact of test-set leakage.\n\n\\paragraph{SVD necessity ablation.}\n\\label{app:svd_necessity}\n\nThe probe above establishes \\emph{sufficiency}: 3 SVD dimensions carry enough information. To test \\emph{necessity}, we project \\emph{out} the top-3 SVD directions from full 768-dimensional 9-class \\texttt{[CLS]} embeddings and re-run BiGRU classification on OOD data (3 seeds). A random-3 removal control verifies that the effect is specific to the discriminative subspace. The top-3 directions explain 89.8\\% of training-set variance.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{SVD necessity ablation: OOD F1 after projecting out top-3 vs.\\ random-3 SVD directions from 9-class layer-10 embeddings (3-seed mean$\\pm$std).}\n\\label{tab:svd_necessity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Condition} & DD OOD & FITD OOD & AA OOD \\\\\n\\midrule\nOriginal 768-dim & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .994$\\pm$.005 \\\\\nRemove top-3 SVD & .831$\\pm$.064 & 1.000$\\pm$.000 & .938$\\pm$.011 \\\\\nRemove random-3 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .994$\\pm$.005 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nRemoving top-3 SVD directions degrades DD detection by 17\\,pp (F1: $1.0 \\to 0.831$) and AA by 5.6\\,pp ($0.994 \\to 0.938$), while random-3 removal has zero effect. FITD is unaffected by either ablation, indicating its discriminative information is more distributed. Combined with the sufficiency result (Table~\\ref{tab:discriminative_probe}), the top-3 SVD directions are both sufficient and necessary for DD detection, sufficient but partially redundant for AA, and sufficient but not necessary for FITD.\n\n\\section{Temporal Aggregation Comparison}\n\\label{app:temporal}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Temporal aggregation comparison: mean pooling vs.\\ BiGRU under frozen and end-to-end (E2E) settings (3-seed mean$\\pm$std). Primary 9-class DAPT checkpoints.}\n\\label{tab:temporal}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Setting} & \\textbf{Aggregator} & DD OOD & AA OOD \\\\\n\\midrule\n\\multirow{2}{*}{Frozen} & BiGRU & .997$\\pm$.005 & .972$\\pm$.026 \\\\\n& Mean pooling & .991$\\pm$.013 & .962$\\pm$.015 \\\\\n\\midrule\n\\multirow{2}{*}{E2E} & BiGRU & 1.000$\\pm$.000 & .997$\\pm$.005 \\\\\n& Mean pooling & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:temporal} compares BiGRU and mean pooling under both frozen and E2E settings. Under frozen probing (the main paper's pipeline), BiGRU provides a marginal advantage on ActorAttack (+1.0\\,pp) with overlapping confidence intervals, consistent with the main text finding that temporal order is not a core detection factor ($|\\Delta| < 1$\\,pp under turn shuffling; Section~\\ref{sec:decomposition}). Under E2E fine-tuning, the difference vanishes entirely: mean pooling saturates all benchmarks at F1\\,=\\,1.000. The choice of frozen BiGRU in the main pipeline reflects a design trade-off: it enables representation-level analysis (CKA, t-SNE) that E2E would confound, while sacrificing $\\leq$1\\,pp on the hardest OOD set.\n\n\\section{Length Stratification Analysis}\n\\label{app:length}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Jailbreak recall by conversation length bin on OOD evaluation (3-seed majority vote). Benign conversations span 12--20 turns; jailbreak conversations span 3--10 turns.}\n\\label{tab:length}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Variant} & 1--3 turns & 4--6 turns & 7--10 turns \\\\\n\\midrule\n\\multirow{2}{*}{DD OOD} & 9-class & --- & 100.0\\% & 99.4\\% \\\\\n& Vanilla & --- & $\\leq$2.6\\% & $\\leq$1.7\\% \\\\\n\\midrule\n\\multirow{2}{*}{AA OOD} & 9-class & 93.3\\% & 95.6\\% & 100.0\\% \\\\\n& Vanilla & 0.0\\% & $\\leq$2.6\\% & 0.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:length} stratifies jailbreak recall by conversation length. The 9-class model shows no systematic degradation: ActorAttack recall increases monotonically from 93.3\\% (1--3 turns) to 100\\% (7--10 turns), and DD recall is near-perfect across all bins.\n\n\\paragraph{Length confound.}\nBenign conversations (12--20 turns) and jailbreak conversations (3--10 turns) have zero length overlap in the OOD evaluation sets, raising the concern that the model discriminates by conversation length rather than content. Three observations argue against this interpretation:\n(1)~Vanilla DeBERTa has access to identical length information via the BiGRU but achieves recall $\\leq$2.6\\% across all bins; length alone is insufficient without domain-adapted representations.\n(2)~At prefix $K$=1, where all conversations are length-equalized, 9-class still achieves F1\\,=\\,0.773$\\pm$0.041 on ActorAttack (Table~\\ref{tab:actorattack_full}), demonstrating content-based detection independent of length.\n(3)~The model is trained on IID data (Crescendo) and cannot learn OOD-specific length distributions; generalization to unseen length patterns must rely on content features that transfer across attack families.\n\n\\paragraph{Direct empirical verification.}\n\\label{app:length_independence}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Turn-count independence verification (9-class DeBERTa-v3-base, same checkpoint as Table~\\ref{tab:main_results}, 3 seeds). Evaluated on the full OOD test set (80 jailbreak + 75 benign conversations) rather than the balanced subset used in Table~\\ref{tab:main_results}. Part~A: FPR on test benign truncated to $K$ user turns (all seeds FPR\\,=\\,0). Part~B: WildChat FPR by turn-count bucket (mean$\\pm$std). Part~C: jailbreak detection (F1) after padding with benign turns to 15+ total turns (mean$\\pm$std where available).}\n\\label{tab:length_independence}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n& \\textbf{Condition} & \\textbf{FPR / F1} & $n$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Part A: Benign truncation (test set)}} \\\\[2pt]\n& Original (12--20 turns) & FPR = .000 & 38 \\\\\n& Truncated $K$=3 & FPR = .000 & 38 \\\\\n& Truncated $K$=5 & FPR = .000 & 38 \\\\\n& Truncated $K$=8 & FPR = .000 & 38 \\\\\n& Truncated $K$=10$^{*}$ & FPR = .000 & 38 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Part B: WildChat FPR by turn count}} \\\\[2pt]\n& Short (3--10 turns) & FPR = .770$\\pm$.105 & 196 \\\\\n& Medium (11--15 turns) & FPR = .942$\\pm$.054 & 23 \\\\\n& Long (16+ turns) & FPR = .857$\\pm$.117 & 7 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Part C: Jailbreak padding to 15+ turns}} \\\\[2pt]\n& DD original & F1 = .996 & 80 \\\\\n& DD padded & F1 = .971 ($\\Delta$=$-$2.5\\,pp) & 80 \\\\\n& AA original & F1 = .963 & 80 \\\\\n& AA padded & F1 = .383$\\pm$.261 ($\\Delta$=$-$57.9\\,pp) & 80 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$$K$=10 did not truncate any conversation (test benign max $\\sim$8 user turns).}\n\\end{table}\n\nTruncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut. $K$=3 and $K$=5 are the effective control conditions where all 38 conversations were truncated; $K$=10 exceeds the maximum test benign length and serves as a no-op control.\n\nWildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \\emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\\,=\\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.\n\nPadding jailbreak conversations with benign turns (Part~C) reveals an asymmetry: DD detection is resilient ($\\Delta$=$-$2.5\\,pp), but ActorAttack collapses ($\\Delta$=$-$57.9\\,pp). Padding experiments append benign turns \\emph{after} the complete attack sequence; in practice, adversaries would not dilute their own successful attacks. The collapse nonetheless exposes BiGRU temporal aggregation as vulnerable to attention dilution on subtle attack signals, a limitation discussed in Section~\\ref{sec:limitations}.\n\n\\section{Inference Efficiency}\n\\label{app:efficiency}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Inference efficiency comparison. DeBERTa+BiGRU and TF-IDF+LR measured on IID test (76 conversations, avg 8.3 turns, single A100). LLM latency from separate OOD evaluation (118 conversations); cross-condition comparison is indicative only.}\n\\label{tab:efficiency}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrcr@{}}\n\\toprule\n\\textbf{Method} & Latency (ms) & Params & VRAM \\\\\n\\midrule\nTF-IDF+LR & 0.43$\\pm$0.05 & $\\sim$10K & CPU \\\\\nDeBERTa+BiGRU (ours) & 12.1$\\pm$1.2 & 186.7M & 862\\,MB \\\\\nQwen3-8B 3-shot$^{\\dagger}$ & $\\sim$5{,}200 & 8B & $\\sim$16\\,GB \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{-2pt}\n{\\footnotesize $^{\\dagger}$Qwen3-8B latency from OOD evaluation (DD/AA, 118 conversations); not directly comparable to encoder latency measured on IID test.}\n\\end{table}\n\nTable~\\ref{tab:efficiency} compares inference cost. On matched data (IID test), DeBERTa+BiGRU processes a conversation in 12.1\\,ms, 28$\\times$ slower than TF-IDF (0.43\\,ms), but this speed gap purchases +71\\,pp on ActorAttack (F1\\,=\\,0.972 vs.\\ 0.261; Table~\\ref{tab:evidence_hierarchy}). LLM-as-judge approaches are orders of magnitude slower ($\\sim$5.2\\,s per conversation for Qwen3-8B 3-shot) while achieving substantially lower OOD detection (DD\\,=\\,0.566, AA\\,=\\,0.652; Table~\\ref{tab:llm_judge}). Zero-shot Qwen3-8B achieves F1\\,=\\,0.0 on DD OOD because it predicts all conversations as benign (Table~\\ref{tab:llm_judge}). The full DeBERTa+BiGRU pipeline requires 862\\,MB GPU memory, enabling deployment on consumer hardware. The 24.3$\\times$ speedup reported in the main text derives from a matched-condition comparison (DisPeD 13.12\\,ms vs.\\ Qwen3-8B 318.53\\,ms on the same GPU and data); the larger gap in Table~\\ref{tab:efficiency} reflects different hardware conditions and evaluation sets.\n\n\\section{Data Efficiency}\n\\label{app:data_efficiency}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Data efficiency of 9-class DAPT (3-seed mean$\\pm$std, sample std with $n{-}1$ divisor) and vanilla baseline (seed 42 only). $N$ = total training conversations (balanced jailbreak/benign).}\n\\label{tab:data_efficiency}\n\\begin{tabular}{@{}rlccc@{}}\n\\toprule\n$N$ & \\textbf{Variant} & IID & DD OOD & AA OOD \\\\\n\\midrule\n50 & 9-class & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .969$\\pm$.037 \\\\\n125 & 9-class & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .975$\\pm$.019 \\\\\n250 & 9-class & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .975$\\pm$.035 \\\\\n350 & 9-class & 1.000$\\pm$.000 & .978$\\pm$.030 & .972$\\pm$.033 \\\\\n\\midrule\n50 & Vanilla & .646 & .529 & .234 \\\\\n125 & Vanilla & .532 & .244 & .244 \\\\\n250 & Vanilla & .987 & .365 & .502 \\\\\n350 & Vanilla & 1.000 & .360 & .489 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:data_efficiency} shows that 9-class DAPT reaches near-saturation performance with as few as 50 conversations (25 jailbreak + 25 benign): AA OOD F1\\,=\\,0.969$\\pm$0.037, already surpassing vanilla at full training size ($N$=350, AA\\,=\\,0.489) by 48\\,pp using only 14\\% of the data. DD OOD is perfectly solved at all training sizes. Vanilla performance is noisy across $N$ (single seed); the consistent pattern is that vanilla never exceeds DD\\,=\\,0.53 or AA\\,=\\,0.50 regardless of training size, while 9-class maintains AA\\,$\\geq$\\,0.969 at all $N$. Seed 456 is systematically lower across all $N$ values, contributing most of the cross-seed variance; this is consistent with the initialization sensitivity observed in the main results.\n\n\\section{Auxiliary Loss Weight Ablation}\n\\label{app:lambda}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Effect of auxiliary persuasion loss weight $\\lambda$ during Stage-2 E2E fine-tuning (seed 42). Stage-1 DAPT encoder is identical across all rows; only the Stage-2 loss $L = L_{\\text{binary}} + \\lambda \\cdot L_{\\text{strategy}}$ varies.}\n\\label{tab:lambda}\n\\begin{tabular}{@{}rcccc@{}}\n\\toprule\n$\\lambda$ & IID & DD OOD & FITD OOD & AA OOD \\\\\n\\midrule\n0 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n0.1 & 1.000 & 1.000 & 1.000 & .990 \\\\\n0.5 & 1.000 & 1.000 & 1.000 & .981 \\\\\n1.0 & 1.000 & 1.000 & 1.000 & .981 \\\\\n2.0 & 1.000 & 1.000 & 1.000 & .944 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDuring Stage-2 E2E fine-tuning, the auxiliary persuasion loss weight $\\lambda$ has limited impact on detection (Table~\\ref{tab:lambda}): the maximum AA OOD gap across all $\\lambda$ values is 5.6\\,pp (single seed), comparable to the cross-seed variance ($\\sim$6\\,pp) observed in the main results. All configurations converge to perfect validation F1 within epoch 1, indicating that DAPT representations already encode sufficient discriminative features for downstream classification (Section~\\ref{app:frozen_verify}). The value of persuasion strategy classification lies in Stage-1 DAPT, where it shapes encoder representations that transfer across attack families, not in the Stage-2 auxiliary loss.\n\n\\section{OOD Strategy Prediction Analysis}\n\\label{app:strategy_pred}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{OOD strategy prediction accuracy (jailbreak turns only) and detection rate for the 9-class model (3-seed mean). $r$: Pearson correlation between per-strategy prediction accuracy and per-strategy detection rate.}\n\\label{tab:strategy_pred}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Dataset} & Strat.\\ Acc.\\ & Det.\\ Rate & Missed (per seed) & $r$ \\\\\n\\midrule\nDD OOD & 50.1\\% & 99.6\\% & 0 / 0 / 1 & $\\sim$0.45 \\\\\nAA OOD & 50.1\\% & 96.2\\% & 1 / 7 / 1 & $\\sim$0.24 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:strategy_pred} reports OOD strategy prediction accuracy alongside detection rates. Strategy prediction accuracy is substantially above random (50.1\\% vs.\\ 11.1\\% chance for 9 classes) and positively correlated with detection success ($r \\approx 0.24$--0.45), but strategy prediction is not the detection mechanism: frozen probing with a randomly initialized strategy head (Appendix~\\ref{app:frozen_verify}) achieves 97.2\\% AA OOD detection, and $\\lambda$=0 (no strategy loss) matches or exceeds $\\lambda > 0$ during E2E fine-tuning (Table~\\ref{tab:lambda}). The classification objective shapes representations during Stage-1 DAPT training; at inference, strategy predictions are a byproduct of those representations, not a driver of detection.\n\n\\section{Cross-Seed Ensemble}\n\\label{app:ensemble}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Majority vote ensemble (3 seeds) vs.\\ single-seed mean on OOD Full. ``Fixed'' = samples corrected by ensemble; ``Broke'' = samples corrupted by ensemble.}\n\\label{tab:ensemble}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & DD single$\\to$ens. & AA single$\\to$ens. & Fixed & Broke \\\\\n\\midrule\n9-class & .997$\\to$\\textbf{1.000} & .972$\\to$\\textbf{.981} & 5 & 0 \\\\\nMLM & .914$\\to$\\textbf{1.000} & .897$\\to$\\textbf{.953} & 26 & 0 \\\\\nVanilla & .258$\\to$.258 & .258$\\to$.258 & 0 & 0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:ensemble} shows that majority vote never corrupts correct predictions (Broke\\,=\\,0 for all variants). MLM benefits most from ensembling (+8.6\\,pp DD, +6.0\\,pp AA), because its per-seed errors are complementary: each seed fails on different samples, and the majority corrects these. This further exposes MLM's seed instability: its individual seeds are unreliable, but their errors are uncorrelated. By contrast, 9-class seeds are already highly consistent (std\\,$\\leq$\\,0.026), leaving minimal room for ensemble improvement (+0.3--0.9\\,pp). Vanilla errors are systematic (all seeds fail on the same OOD samples), so ensembling provides no benefit.\n\n\\subsection{Seed-Level F1 Comparisons}\n\\label{app:seed_level}\n\nTo verify that cross-seed pooling does not mask inconsistent pairwise orderings, Table~\\ref{tab:seed_level} reports per-seed F1 for all variants on OOD DD and ActorAttack at full conversation length. The overall evidence hierarchy is maintained across seeds, with 9-class and binary consistently outperforming MLM; scrambled shows one reversal on AA (seed 42).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-seed F1 on OOD Full for key variants (seeds 42, 123, 456). The relative ordering is consistent across seeds.}\n\\label{tab:seed_level}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n& \\multicolumn{3}{c}{DD-Full} & \\multicolumn{3}{c}{AA-Full} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Variant} & s42 & s123 & s456 & s42 & s123 & s456 \\\\\n\\midrule\n9-class & 1.000 & 1.000 & .990 & .990 & .935 & .990 \\\\\nBinary & 1.000 & 1.000 & 1.000 & .981 & .990 & 1.000 \\\\\nScrambled & .990 & 1.000 & 1.000 & .891 & .990 & .971 \\\\\nMLM-only & 1.000 & .990 & .751 & .971 & .925 & .784 \\\\\nVanilla & .285 & .305 & .348 & .258 & .258 & .258 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 183,
        "oldLines": 7,
        "newStart": 183,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{figure}[t]",
          " \\centering",
          "-\\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}",
          "+% \\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}",
          " \\caption{Centered CKA similarity~\\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\\ 9-class block shows distinct geometries (CKA $\\leq$ 0.2 on RoBERTa OOD).}",
          " \\label{fig:cka_heatmap}",
          " \\end{figure}"
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01D3GGU1XNQT1TSvf87rq5qi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/tmp/anon_hotfix/docs/paper/appendix.tex",
  "old_string": "\\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}",
  "new_string": "% \\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "a9024fae-bf1d-4618-a0f3-fc63f937a62b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oEnXhCATMsdW1Pc1QyNZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 29628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 574
      },
      "output_tokens": 62,
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

_source line 61 · 2026-05-25T09:21:12.479Z_

<details><summary>↩ Tool result · `toolu_01D3GGU1XNQT1TSvf87rq5qi`</summary>

```text
The file /tmp/anon_hotfix/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "ea6e0abd-75ec-40a3-b317-e020df33aa9f",
  "tool_use_result": {
    "filePath": "/tmp/anon_hotfix/docs/paper/appendix.tex",
    "oldString": "\\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}",
    "newString": "% \\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}",
    "originalFile": "% appendix.tex — Supplementary material\n\n\\appendix\n\n\\section{LLM-as-Judge Baseline}\n\\label{sec:llm_judge}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}\n\\label{tab:llm_judge}\n\\begin{tabular}{@{}lcccr@{}}\n\\toprule\n\\textbf{Method} & DD & AA & IID & Unparse. \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Zero-shot}} \\\\[2pt]\nGPT-5.5 & -- & -- & .383 & 30--47\\% \\\\\nQwen3-8B & .244 & .244 & .100 & 0\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{3-shot}} \\\\[2pt]\nQwen3-8B & .566 & .652 & -- & 0\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Trained classifier}} \\\\[2pt]\n9-class (ours) & \\textbf{.994} & \\textbf{.972} & \\textbf{1.000} & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.\nOn IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\\% of responses are unparseable.\nQwen3-8B performs worse (IID F1 = 0.100).\nOn OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.\nEven with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\\geq$ 0.972.\nThe poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.\n\n\\section{Full Cross-Attack Results by Prefix}\n\\label{sec:full_prefix}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}\n\\label{tab:full_prefix}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{IID (Crescendo)}} \\\\[2pt]\n9-class (ours) & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\nMLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\\\\nVanilla DeBERTa & .968$\\pm$.033 & .978$\\pm$.016 & .987$\\pm$.000 & .982$\\pm$.014 & 1.000$\\pm$.000 \\\\\nTF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (Deceptive Delight)}} \\\\[2pt]\n9-class (ours) & .990$\\pm$.013 & .981$\\pm$.013 & .972$\\pm$.026 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nBinary & .994$\\pm$.009 & .994$\\pm$.009 & .984$\\pm$.008 & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\nScrambled & .997$\\pm$.005 & .981$\\pm$.026 & .975$\\pm$.029 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nMLM-only & .973$\\pm$.019 & .993$\\pm$.009 & .997$\\pm$.005 & .997$\\pm$.005 & .914$\\pm$.115 \\\\\nVanilla DeBERTa & .628$\\pm$.038 & .479$\\pm$.038 & .389$\\pm$.027 & .351$\\pm$.030 & .312$\\pm$.026 \\\\\nTF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (FITD)}} \\\\[2pt]\n9-class (ours) & 1.000$\\pm$.000 & .997$\\pm$.005 & -- & -- & 1.000$\\pm$.000 \\\\\nVanilla DeBERTa & .954$\\pm$.039 & .952$\\pm$.061 & -- & -- & .994$\\pm$.009 \\\\\nTF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{ActorAttack Full Results}\n\\label{sec:actorattack_full}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}\n\\label{tab:actorattack_full}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{DeBERTa-v3}} \\\\[2pt]\nBinary & .788$\\pm$.020 & \\textbf{.935$\\pm$.018} & \\textbf{.976$\\pm$.005} & \\textbf{.995$\\pm$.005} & \\textbf{.990$\\pm$.008} \\\\\n9-class & .773$\\pm$.041 & .855$\\pm$.048 & .921$\\pm$.046 & .966$\\pm$.028 & .972$\\pm$.026 \\\\\nScrambled & .652$\\pm$.034 & .804$\\pm$.053 & .854$\\pm$.046 & .910$\\pm$.052 & .951$\\pm$.043 \\\\\nMLM-only & .736$\\pm$.150 & .909$\\pm$.058 & .945$\\pm$.039 & .929$\\pm$.033 & .893$\\pm$.080 \\\\\nWiki MLM & .656$\\pm$.224 & .672$\\pm$.252 & .693$\\pm$.280 & .689$\\pm$.285 & .686$\\pm$.297 \\\\\nTopic & .513$\\pm$.077 & .580$\\pm$.109 & .565$\\pm$.100 & .615$\\pm$.111 & .625$\\pm$.141 \\\\\nVanilla & .337$\\pm$.049 & .306$\\pm$.026 & .284$\\pm$.011 & .262$\\pm$.006 & .258$\\pm$.000 \\\\\nTF-IDF LR & .633 & .730 & .571 & .242 & .261 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RoBERTa}} \\\\[2pt]\n9-class & \\textbf{.738$\\pm$.033} & .805$\\pm$.033 & .884$\\pm$.066 & .925$\\pm$.066 & .939$\\pm$.046 \\\\\nMLM & .633$\\pm$.133 & .665$\\pm$.150 & .713$\\pm$.174 & .719$\\pm$.184 & .730$\\pm$.201 \\\\\nVanilla & .410$\\pm$.126 & .425$\\pm$.143 & .432$\\pm$.144 & .466$\\pm$.144 & .466$\\pm$.163 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:actorattack_full} reveals three distinct prefix-length patterns. The 9-class model improves monotonically from $K$=1 to Full (+20\\,pp), consistent with cumulative evidence accumulation across turns. Vanilla DeBERTa \\emph{decreases} with more turns (0.337 at $K$=1 to 0.258 at Full), suggesting that additional attack turns push representations further into benign embedding regions. MLM peaks at $K$=3 (0.945) then declines to 0.893 at Full, indicating that unsupervised domain exposure captures early-turn patterns but is unstable under extended sequences.\n\n\\subsection{Error Analysis}\n\\label{app:aa_error}\n\nPer-sample majority vote across 3 seeds yields 98.3\\% accuracy on ActorAttack OOD (2 false negatives, 0 false positives). No sample is misclassified by all three seeds; all 7 seed-specific errors are false negatives concentrated in shorter conversations (3--6 turns). On these 7 error samples, vanilla achieves 0/3 correct votes per sample, while 9-class majority vote correctly classifies 5/7, confirming that domain adaptation provides robust per-sample coverage even where individual seeds fail.\n\n\\section{Perturbation Robustness}\n\\label{sec:perturbation_full}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\\Delta$: F1 degradation (pp). Classification-supervised variants achieve zero degradation at full length; this pattern does not generalize to ActorAttack.}\n\\label{tab:perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & $\\Delta$ Full & $\\Delta$ $K$=1 & $\\Delta$ $K$=2 & $\\Delta$ $K$=3 \\\\\n\\midrule\n9-class (ours) & \\textbf{0.0} & \\textbf{$-$2.6} & \\textbf{0.0} & \\textbf{0.0} \\\\\nScrambled & \\textbf{0.0} & $-$5.3 & $-$2.6 & \\textbf{0.0} \\\\\nBinary & \\textbf{0.0} & $-$9.2 & $-$2.6 & \\textbf{0.0} \\\\\n\\midrule\nTF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\\\\nMLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\\\\nTopic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \\textbf{0.0} \\\\\n\\midrule\nWikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\\\\nVanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation} shows perturbation behavior on IID data.\nClassification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.\nModels without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\\sim$12\\,pp.\nMcNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\\leq$7 discordant pairs, statistical power is limited.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\\pm$std where available.}\n\\label{tab:ood_perturbation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & Clean Full & Pert.\\ Full & $\\Delta$ Full & $\\Delta$ $K$=1 \\\\\n\\midrule\n9-class & .994$\\pm$.005 & 1.000$\\pm$.000 & +0.6 & +0.6 \\\\\nBinary & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 0.0 & +0.6 \\\\\nScrambled & .994$\\pm$.005 & 1.000$\\pm$.000 & +0.6 & $-$0.3 \\\\\n\\midrule\nJB MLM & .914$\\pm$.115 & .941 & +2.7 & 0.0 \\\\\nWiki MLM$^{*}$ & .904$\\pm$.115 & .872 & $-$3.3 & $-$3.2 \\\\\nVanilla$^{\\dagger}$ & .312$\\pm$.026 & .339$\\pm$.055 & +2.7 & $-$6.8$\\pm$1.1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\\,pp; other seeds show 0.0\\,pp change.\\\\$^{\\dagger}$Vanilla $\\Delta$ Full = +2.7\\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}\n\\end{table}\n\nOn OOD DD, the IID pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\\ vanilla significance ($p < 0.001$, 49--78 discordant pairs).\nOn OOD ActorAttack, domain-adapted variants degrade substantially (9-class $\\Delta$\\,=\\,$-$20.4$\\pm$13.5\\,pp, MLM $-$35.3\\,pp), but perturbation narrows rather than closes the adapted vs.\\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\\ vanilla 0.248 (McNemar $p < 0.001$).\nDomain specificity also manifests: Wikipedia MLM degrades by $\\sim$12\\,pp while jailbreak-domain MLM degrades by only 2.6\\,pp.\n\n\\section{Strategy Trajectory Analysis}\n\\label{sec:strategy_full}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}\n\\caption{Persuasion strategy transition count matrices for three attack families, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}\n\\label{fig:strategy_heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:strategy_heatmap} shows transition count matrices for three attack families.\nCrescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545); this reflects its gradual escalation design.\nFITD conversations show a markedly sparser pattern (541 transitions), with Role$\\to$Obfuscation (161) as the dominant transition, consistent with FITD's commitment-consistency exploitation~\\citep{cialdini2001influence}.\nDD conversations span 5 active source strategies (565 transitions), with Emotion$\\to$Obfuscation (129) as the dominant transition, aligning with DD's design of embedding harmful content within emotionally engaging contexts~\\citep{deceptivedelight2024}.\n\n\\section{Centered CKA Heatmaps}\n\\label{sec:cka_heatmap}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}\n\\caption{Centered CKA similarity~\\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\\ 9-class block shows distinct geometries (CKA $\\leq$ 0.2 on RoBERTa OOD).}\n\\label{fig:cka_heatmap}\n\\end{figure}\n\n\\section{Embedding Space Visualization}\n\\label{app:tsne}\n\nFigure~\\ref{fig:tsne} visualizes mean-pooled \\texttt{[CLS]} embeddings via t-SNE for three representative variants (Vanilla, JB-MLM, 9-Class) on DD OOD and ActorAttack. Vanilla embeddings show dispersed jailbreak clusters with ambiguous decision boundaries, while domain-adapted variants (JB-MLM, 9-Class) produce tighter, more separable clusters. JB-MLM achieves the clearest bimodal separation on both evaluation sets, consistent with its superior detection performance.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}\n\\caption{t-SNE visualization of mean-pooled \\texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}\n\\label{fig:tsne}\n\\end{figure}\n\n\\section{Cross-LLM Validation}\n\\label{app:cross_llm}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Cross-LLM validation (F1, full conversation). All models are trained on Qwen3-8B data; conditions vary the source of jailbreak (JB) and benign (ben.) conversations at inference. Values are evaluated under a matched 50-sample subset protocol and differ from Table~\\ref{tab:evidence_hierarchy}, which uses the full evaluation set.}\n\\label{tab:cross_llm}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n& \\multicolumn{3}{c}{\\textit{DD Full}} & \\multicolumn{3}{c}{\\textit{AA Full}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Condition} & Van. & MLM & 9-cl. & Van. & MLM & 9-cl. \\\\\n\\midrule\nQwen JB + Qwen ben. & .312 & .914 & .997 & .258 & .893 & .972 \\\\\nLlama JB + Llama ben. & .261 & .282 & .433 & .261 & .368 & .321 \\\\\nLlama JB + Qwen ben. & .302 & .778$^{*}$ & 1.000 & .302 & .903 & .801 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$High seed variance (std = 0.306): seed 456 outlier (F1 = 0.345); remaining two seeds achieve F1 $\\geq$ 0.97.}\n\\end{table}\n\nTable~\\ref{tab:cross_llm} shows three inference conditions. When both jailbreak and benign text come from Llama (row~2), all variants collapse (F1 = 0.26--0.43), but this conflates two sources of distribution shift: unfamiliar jailbreak patterns and unfamiliar benign text. Row~3 isolates jailbreak transferability by pairing Llama jailbreaks with the original Qwen benign distribution. Under this condition, 9-class recovers to F1 = 1.000 on DD and 0.801 on ActorAttack, and JB-MLM reaches 0.903 on ActorAttack. The contrast between rows~2 and~3 shows that the dominant failure mode in row~2 is benign distribution mismatch (false positives from unfamiliar benign text), not inability to recognize cross-LLM jailbreak patterns. Vanilla remains at 0.26--0.31 across all conditions, further confirming that encoders without DAPT lack OOD detection capability regardless of the LLM source. The residual degradation on ActorAttack (0.801 vs.\\ 0.972) reflects genuine cross-LLM variation in structurally complex attack patterns.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Error decomposition for DD Full cross-LLM conditions (matched 50-sample subsets). TP rate is identical across benign conditions; the F1 collapse in the Llama-only condition (Table~\\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text.}\n\\label{tab:cross_llm_error}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Metric} & Van. & MLM & 9-cl. \\\\\n\\midrule\nTP rate (Llama JB) & 0.0\\% & 68.0\\% & 100.0\\% \\\\\nFP rate (Llama ben.) & 29.3\\% & 88.0\\% & 90.0\\% \\\\\nFP rate (Qwen ben.) & 0.0\\% & 0.9\\% & 0.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_llm_error} decomposes DD Full F1 into true positive and false positive rates. TP rates are identical regardless of the benign source: domain-adapted models detect Llama-generated jailbreaks at the same rate whether evaluated against Qwen or Llama benign text. The F1 collapse in the full Llama condition (Table~\\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text (FP rate: 88--90\\% on Llama vs.\\ 0--0.9\\% on Qwen for adapted variants). The model implicitly treats non-Qwen text style as a jailbreak indicator, a spurious correlation from single-LLM training data. This failure reflects a data diversity limitation, not a methodological one; mixed-LLM training (Table~\\ref{tab:mixed_llm}) partially addresses this confound.\n\n\\section{Mixed-LLM Training Results}\n\\label{app:mixed_llm}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Mixed-LLM training (250 Qwen + 250 Llama conversations, 3-seed mean$\\pm$std where available). ToxicChat evaluated on balanced set (408 conversations).}\n\\label{tab:mixed_llm}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Variant} & Mixed & DD OOD & AA OOD & FITD OOD & ToxicChat \\\\\n\\midrule\n9-class & \\textbf{.996$\\pm$.006} & \\textbf{.818$\\pm$.096} & \\textbf{.504$\\pm$.107} & \\textbf{.997$\\pm$.005} & \\textbf{.550$\\pm$.052} \\\\\nMLM & .681$\\pm$.226 & .289$\\pm$.101 & .258$\\pm$.075 & .679$\\pm$.188 & .256$\\pm$.053 \\\\\nVanilla & .802$\\pm$.010 & .291$\\pm$.065 & .389$\\pm$.073 & .867$\\pm$.022 & .356$\\pm$.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:mixed_llm} reports detection performance when training on a mixed corpus of Qwen3-8B and Llama-3.1-8B conversations. Classification-based DAPT (9-class) maintains the strongest DD OOD performance (0.818$\\pm$0.096), outperforming both vanilla (0.291$\\pm$0.065) and MLM (0.289$\\pm$0.101) by 53\\,pp. ActorAttack remains challenging under mixed-LLM conditions (9-class F1\\,=\\,0.504$\\pm$0.107), suggesting structurally complex attacks require larger or more diverse training data. ToxicChat performance shows no significant improvement over single-source training (0.550$\\pm$0.052 vs.\\ 0.596$\\pm$0.087; Section~\\ref{sec:human_data}), consistent with ToxicChat being zero-shot single-turn transfer rather than a standard OOD benchmark.\n\n\\section{Dataset Scale Validation}\n\\label{app:scale_validation}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Dataset scale validation (1{,}000 Qwen conversations, 3-seed mean$\\pm$std). IID results omitted due to train/test overlap (71\\% of original test set present in expanded training data).}\n\\label{tab:scale_validation}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Variant} & DD OOD & AA OOD \\\\\n\\midrule\n9-class & \\textbf{.889$\\pm$.041} & \\textbf{.913$\\pm$.041} \\\\\nMLM & .338$\\pm$.010 & .351$\\pm$.018 \\\\\nVanilla & .326$\\pm$.000 & .508$\\pm$.085 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale_validation} validates robustness to dataset scale by doubling the training corpus from 500 to 1{,}000 conversations with new topic seeds. The hierarchy 9-class $\\gg$ MLM $\\approx$ vanilla holds at 2$\\times$ scale: classification-based DAPT maintains 40--56\\,pp advantage over vanilla, while MLM provides no improvement over vanilla on either attack family (DD: 0.338 vs.\\ 0.326; AA: 0.351 vs.\\ 0.508).\n\nThe performance decline at 1{,}000 conversations may reflect distributional heterogeneity introduced by diverse topic seeds: the additional conversations broaden the training distribution, potentially diluting the concentrated attack-relevant features that smaller, more homogeneous datasets preserve. IID evaluation was precluded by train/test overlap in the expanded dataset (71\\%), limiting analysis to OOD metrics. Human-data validation also degrades under scaled training (ToxicChat F1: 0.596 $\\to$ 0.341), suggesting the expanded distribution shifts representations away from features useful for both synthetic OOD and human data.\n\n\\section{RoBERTa-large DAPT Learning Rate Control}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{RoBERTa-large (355M) DAPT learning rate control on OOD Full (3-seed mean$\\pm$std). Reducing the learning rate worsens both DD and AA, ruling out over-adaptation as the cause of the regression in Table~\\ref{tab:cross_encoder}.}\n\\label{tab:roberta_large_lr}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Config} & DD Full & AA Full \\\\\n\\midrule\nVanilla (no DAPT) & .927$\\pm$.036 & 1.000$\\pm$.000 \\\\\n9-class, LR=$2 \\times 10^{-5}$ & .987$\\pm$.004 & .946$\\pm$.057 \\\\\n9-class, LR=$1 \\times 10^{-5}$ & .948$\\pm$.034 & .781$\\pm$.054 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nReducing the DAPT learning rate from $2 \\times 10^{-5}$ to $1 \\times 10^{-5}$ worsens both DD and AA performance, which rules out over-adaptation as the cause of the regression observed in Table~\\ref{tab:cross_encoder}. An MLM-only variant (without classification) produces the same pattern (AA Full = 0.874$\\pm$0.014); representation drift from continued pretraining, not classification-specific bias, is the underlying cause. Domain-adaptive fine-tuning narrows the representation space of a sufficiently large encoder and reduces its inherent OOD generalization ability.\n\n\\section{TOST Equivalence Sensitivity Analysis}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{TOST equivalence test (scrambled vs.\\ 9-class, $\\delta$=5\\,pp, 10 seeds). $p < 0.05$ confirms equivalence within $\\pm\\delta$.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Dataset} & $p$ & $d$ & Equivalent? \\\\\n\\midrule\nDD OOD & $2.06 \\times 10^{-9}$ & $-$0.136 & \\checkmark \\\\\nFITD OOD & $\\approx 0$ & 0.000 & \\checkmark \\\\\nActorAttack & .183 & 0.440 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn our 80-sample test set, $\\delta = 5$\\,pp corresponds to $\\approx$4 additional missed attacks. We choose $\\delta$\\,=\\,5\\,pp as a conservative threshold; equivalence holds even at $\\delta$\\,=\\,3\\,pp on DD ($p < 0.001$, $n$\\,=\\,10) and FITD ($p \\approx 0$). With 10 seeds at $\\delta$\\,=\\,5\\,pp, DD and FITD confirm formal equivalence ($p < 10^{-8}$, $|d| \\leq 0.14$), demonstrating that label correctness is not a detection factor for template attacks. On ActorAttack, the mean gap is 3.0\\,pp with moderate effect size ($d$\\,=\\,0.44); TOST does not confirm equivalence ($p$\\,=\\,0.183), indicating that strategy-diverse attacks retain some sensitivity to label quality.\n\n\\section{Partition Robustness and Topic Failure Analysis}\n\\label{app:random_partition}\n\\label{app:topic_failure}\n\n\\subsection{Random Binary Partition Robustness}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{OOD F1 for 10 random binary partitions of the 9 strategy labels (each partition randomly assigns strategies to group A or B). All partitions use identical Stage-1 DAPT and Stage-2 GRU training; only the binary label mapping differs. Seed 42 (3 runs).}\n\\label{tab:random_partition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Partition} & \\textbf{Group A} & \\textbf{IID} & \\textbf{DD OOD} & \\textbf{AA OOD} \\\\\n\\midrule\n0 & \\{0,2,4,5,7\\} & 1.000 & 1.000 & 1.000 \\\\\n1 & \\{1,3,5,6,8\\} & 1.000 & 1.000 & 1.000 \\\\\n2 & \\{0,1,3,7,8\\} & 1.000 & 1.000 & 1.000 \\\\\n3 & \\{2,4,5,6,7\\} & 1.000 & 1.000 & 1.000 \\\\\n4 & \\{0,1,2,6,8\\} & 1.000 & 1.000 & 1.000 \\\\\n5 & \\{0,3,4,7,8\\} & 1.000 & 1.000 & 1.000 \\\\\n6 & \\{1,2,3,5,6\\} & 1.000 & 1.000 & 1.000 \\\\\n7 & \\{1,4,6,7\\}   & 1.000 & 1.000 & 0.636 \\\\\n8 & \\{0,2,3,4,8\\} & 1.000 & 1.000 & 1.000 \\\\\n9 & \\{0,1,5,7,8\\} & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\nMean$\\pm$Std &  & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 0.964$\\pm$.109 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll 10 partitions achieve perfect IID and DD OOD detection regardless of how the 9 strategy labels are split into two groups. On ActorAttack, 9/10 partitions achieve F1\\,=\\,1.000; the sole outlier (partition~7, AA F1\\,=\\,0.636) uses a 4/5 split that isolates a specific strategy cluster. The near-universal success confirms that domain-relevant binary classification---not specific label semantics---drives cross-attack generalization on template attacks. The AA outlier is consistent with the complexity-dependent boundary observed in Section~\\ref{sec:decomposition}: structurally complex attacks are sensitive to specific partition choices while template attacks are not.\n\n\\subsection{Topic Classification Failure Analysis}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Per-turn Fisher ratio (mean across all dimensions) and silhouette score between jailbreak and benign turn embeddings (\\texttt{[CLS]} representations). Higher values indicate greater per-turn separability.}\n\\label{tab:topic_failure}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Fisher (mean)} & \\textbf{Silhouette} \\\\\n\\midrule\nVanilla  & IID test & 0.118 & 0.034 \\\\\nVanilla  & DD OOD  & 0.401 & 0.411 \\\\\nVanilla  & AA OOD  & 0.408 & 0.330 \\\\\n\\midrule\n9-class DAPT & IID test & 0.073 & 0.048 \\\\\n9-class DAPT & DD OOD  & 0.200 & 0.079 \\\\\n9-class DAPT & AA OOD  & 0.832 & 0.301 \\\\\n\\midrule\nTopic DAPT & IID test & 0.108 & 0.076 \\\\\nTopic DAPT & DD OOD  & 0.653 & 0.274 \\\\\nTopic DAPT & AA OOD  & 0.311 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTopic DAPT achieves \\emph{higher} per-turn Fisher separability than 9-class DAPT on IID and DD (0.653 vs.\\ 0.200 on DD) yet produces far worse conversation-level detection (F1\\,=\\,0.541 vs.\\ 0.994). This rules out per-turn separability destruction as the failure mechanism. The 9-class model instead greatly expands the embedding space (centroid $L_2$ distance 7.5--27.6 vs.\\ 0.9--1.1 for vanilla) while distributing both classes broadly, creating richer representation geometry that the downstream GRU exploits over the turn sequence. Topic classification teaches features that separate turns individually but are temporally inconsistent across a conversation---high per-turn separability does not guarantee that the GRU can learn a stable conversation-level decision boundary.\n\n\\section{Reproducibility Details}\n\\label{sec:reproducibility}\n\n\\paragraph{Stage-1 training.}\nAll variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \\times 10^{-5}$, AdamW optimizer ($\\beta_1$=0.9, $\\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\\% of steps, batch size 16, and 4 epochs. MLM variants use 15\\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).\n\n\\paragraph{Stage-2 training.}\nThe BiGRU has hidden dimension 256, 2 layers, and dropout 0.3 (bidirectional, so output dimension 512). The MLP classifier has layers $512 \\to 256 \\to 2$ with ReLU activation. Training uses learning rate $1 \\times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.\n\n\\paragraph{Data generation.}\nJailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.\n\n\\paragraph{Strategy annotation.}\nEach user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. All generation and annotation prompts, the full dataset, and training code are available at \\url{https://github.com/anonymous-nlp-2026/persuasion_turn_jailbreak_detect}.\n\n\\paragraph{Adversarial paraphrasing.}\nThe paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.\n\n\\paragraph{Cross-checkpoint variance.}\nTo disentangle Stage-1 from Stage-2 variance, we evaluate three independently trained 9-class DAPT checkpoints (seeds 42, 123, 456) with a fixed downstream BiGRU seed (42). Results: IID F1\\,=\\,1.000$\\pm$0.000, DD OOD\\,=\\,0.926$\\pm$0.026, AA OOD\\,=\\,0.935$\\pm$0.013. Stage-1 training is stable (OOD std\\,$\\leq$\\,2.6\\,pp), confirming that the variance reported in the main paper is not dominated by Stage-1 initialization.\n\n\\section{End-to-End Fine-Tuning Upper Bound}\n\\label{app:e2e}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Frozen probing vs.\\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\\pm$std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\\ref{tab:main_results}--\\ref{tab:evidence_hierarchy}); Table~\\ref{tab:frozen_verify} uses independently trained checkpoints, yielding higher frozen accuracy (DD\\,=\\,.997, AA\\,=\\,.972) and a narrower E2E gap ($\\leq$2.5\\,pp).}\n\\label{tab:e2e}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Config} & IID & DD OOD & AA OOD \\\\\n\\midrule\nFrozen probing & 1.000$\\pm$.000 & .994$\\pm$.005 & .939$\\pm$.047 \\\\\nE2E fine-tuning & 1.000$\\pm$.000 & 1.000$\\pm$.000 & \\textbf{.997$\\pm$.005} \\\\\n\\midrule\n$\\Delta$ & .000 & +.006 & +.058 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnd-to-end fine-tuning unfreezes the Stage-1 encoder during Stage-2 BiGRU training, allowing gradient flow through the full pipeline. On IID and OOD DD, the two configurations are indistinguishable; on structurally complex ActorAttack, E2E recovers +5.8\\,pp. The modest gain confirms that frozen probing captures the vast majority of discriminative information encoded by Stage-1 DAPT, and that the remaining OOD gap in the frozen setting reflects downstream optimization constraints rather than missing representational capacity.\n\n\\section{Real-World False Positive Rate}\n\\label{app:wildchat_fpr}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{False positive rate (\\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\\pm$std.}\n\\label{tab:wildchat_fpr}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & Seed 42 & Seed 123 & Seed 456 & Mean$\\pm$Std \\\\\n\\midrule\n9-class & 66.8 & 61.1 & 76.5 & 68.1$\\pm$6.4 \\\\\nMLM & 36.7 & 64.6 & 32.3 & 44.5$\\pm$14.3 \\\\\nVanilla & 47.3 & 42.5 & 54.4 & 48.1$\\pm$4.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:wildchat_fpr} evaluates false positive rates on 226 WildChat benign multi-turn conversations from real GPT-3.5 users (avg 7.4 turns). All variants produce FPR far exceeding deployable thresholds: 9-class is worst at 68.1\\%, followed by vanilla (48.1\\%) and MLM (44.5\\%). Domain adaptation \\emph{increases} FPR relative to vanilla (+20\\,pp for 9-class), indicating that continued pretraining amplifies dependence on the training benign distribution. This is consistent with the cross-LLM false positive spike (Table~\\ref{tab:cross_llm_error}): models trained on synthetic Qwen3-8B benign text implicitly treat unfamiliar conversational styles as jailbreak indicators. High MLM seed variance (std\\,=\\,14.3\\%) suggests that unsupervised pretraining is particularly unstable under benign distribution shift. Deployment requires per-domain benign calibration or mixed-source benign training data.\n\n\\paragraph{Post-hoc calibration.}\nROC AUC\\,=\\,0.700$\\pm$0.054 indicates insufficient discrimination between WildChat benign and jailbreak conversations at the representation level. At TPR$\\geq$95\\%, the optimal threshold still yields FPR\\,=\\,62.7\\%, far above deployable levels. Temperature scaling cannot improve this trade-off, as ROC curves are invariant to monotonic score transforms. The AUC ceiling reflects genuine domain shift: WildChat benign and jailbreak representations overlap substantially, and no post-hoc calibration can overcome this; in-domain benign adaptation is required.\n\n\\paragraph{Second benign source: OASST2.}\n\\label{app:oasst2}\n\nTo test whether benign-side shift generalizes beyond WildChat, we evaluate on 200 benign multi-turn conversations from OpenAssistant OASST2~\\citep{kopf2023openassistant}---a crowdsourced dataset of real human conversations, distinct from WildChat (GPT-3.5 user logs) in both authorship and topic distribution.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{OASST2 benign adaptation curve: FPR on 200 OASST2 benign conversations and OOD jailbreak detection F1 as a function of $N$ OASST2 conversations added to training. Seed 42. Compare WildChat (Table~\\ref{tab:wildchat_fpr}): FPR reaches 0\\% at $N$\\,=\\,10.}\n\\label{tab:oasst2_curve}\n\\begin{tabular}{@{}rccccc@{}}\n\\toprule\n$N$ & FPR (\\%) & IID F1 & DD F1 & AA F1 & FITD F1 \\\\\n\\midrule\n0 & 57.5 & -- & -- & -- & -- \\\\\n10 & 20.5 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n25 & \\textbf{1.5} & 1.000 & 1.000 & 0.953 & 1.000 \\\\\n50 & \\textbf{0.5} & 1.000 & 1.000 & 0.990 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBaseline FPR on OASST2 (57.5\\%) is comparable to WildChat (68.1\\%), confirming that benign-side shift is not source-specific but a general consequence of synthetic-only benign training. The adaptation curve follows the same pattern---monotonic FPR reduction with preserved OOD detection---but requires more samples: 25 conversations reduce FPR to 1.5\\% (vs.\\ 0\\% at $N$\\,=\\,10 for WildChat), and 50 conversations reach 0.5\\%. The slower convergence likely reflects greater distributional distance between crowdsourced OASST2 conversations and the synthetic training distribution compared to WildChat's GPT-3.5 user logs.\n\n\\subsection{Estimated Dual-OOD Detection Performance}\n\\label{app:dual_ood}\n\nThe OOD detection F1 reported in the main paper evaluates attack-side OOD with IID benign examples (FPR\\,=\\,0), providing an upper bound. To estimate performance when \\emph{both} attack and benign inputs are OOD, we combine per-seed attack recall (from OOD evaluation) with per-seed benign FPR (from WildChat/OASST2 experiments), assuming independence between attack detection and benign false positives. For each seed, we compute binary detection F1 from the resulting TP, FP, FN counts on the OOD test composition (80 jailbreak + 38 benign).\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Estimated dual-OOD binary detection F1 under different benign conditions (3-seed mean$\\pm$std). Attack recall held fixed from OOD evaluation; only benign FPR varies. IID row corresponds to the benign-IID upper bound (FPR\\,=\\,0).}\n\\label{tab:dual_ood}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Benign condition} & DD OOD F1 & AA OOD F1 \\\\\n\\midrule\nIID (FPR\\,=\\,0) & .994$\\pm$.009 & .981$\\pm$.019 \\\\\nWildChat, no adapt & .855$\\pm$.020 & .842$\\pm$.012 \\\\\nOASST2, no adapt & .874$\\pm$.009 & .861$\\pm$.018 \\\\\nWildChat + 10-shot & .994$\\pm$.009 & .981$\\pm$.019 \\\\\nOASST2 + 25-shot & .991$\\pm$.009 & .978$\\pm$.018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithout benign adaptation, dual-OOD F1 drops by 13--14\\,pp (DD: $.994 \\to .855$; AA: $.981 \\to .842$), driven entirely by false positives on OOD benign inputs. After few-shot adaptation---10 WildChat or 25 OASST2 conversations---dual-OOD F1 recovers to within 0.3\\,pp of the IID upper bound, confirming that the lightweight adaptation procedure (Section~\\ref{sec:benign_shift}) effectively closes the benign distribution gap without compromising attack-side performance.\n\n\\section{BERT-base Proxy Baseline}\n\\label{app:bert_proxy}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{BERT-base-uncased (110M) frozen probing without DAPT, matching DeepContext's encoder family~\\citep{deepcontext2026}. 3-seed mean$\\pm$std. DeBERTa-v3 results from Table~\\ref{tab:cross_encoder} for comparison.}\n\\label{tab:bert_proxy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Encoder} & IID & DD OOD & AA OOD \\\\\n\\midrule\nBERT-base (110M), no DAPT & .996$\\pm$.006 & .318$\\pm$.031 & .275$\\pm$.027 \\\\\nDeBERTa-v3 (184M), no DAPT & 1.000$\\pm$.000 & .312$\\pm$.043 & .258$\\pm$.000 \\\\\nDeBERTa-v3 (184M), 9-class & 1.000$\\pm$.000 & .994$\\pm$.005 & .939$\\pm$.047 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:bert_proxy} compares BERT-base-uncased (110M parameters, matching DeepContext's encoder) against DeBERTa-v3-base (184M), both without domain-adaptive pretraining. The two vanilla encoders achieve comparable OOD performance (DD: 0.318 vs.\\ 0.312; AA: 0.275 vs.\\ 0.258), despite a 1.7$\\times$ parameter difference and different pretraining procedures. Both collapse on OOD evaluation while 9-class DAPT recovers to 0.994 (DD) and 0.939 (AA). This confirms that cross-attack generalization is driven by domain adaptation, not encoder architecture or capacity at this scale.\n\n\\section{Confidence Calibration}\n\\label{app:calibration}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Expected calibration error (ECE, 10 bins) for 9-class and vanilla on IID and OOD evaluation (3-seed mean$\\pm$std). Lower is better.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Variant} & IID & DD OOD & AA OOD \\\\\n\\midrule\n9-class & $\\approx$0.000 & 0.143$\\pm$0.053 & 0.116$\\pm$0.053 \\\\\nVanilla & 0.009$\\pm$0.007 & 0.669$\\pm$0.004 & 0.504$\\pm$0.066 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 9-class model achieves substantially lower ECE than vanilla on OOD data (0.12--0.14 vs.\\ 0.50--0.67), indicating that domain adaptation improves not only discriminative performance but also confidence calibration. IID calibration is near-perfect for both variants. The residual OOD ECE (0.12--0.14) suggests that temperature scaling could further improve deployment reliability.\n\n\\subsection{ToxicChat False Positive Confidence}\n\\label{app:confidence}\n\nOn ToxicChat, 9-class false positives are overwhelmingly high-confidence: 70.2\\% of majority-vote FPs exceed $p > 0.9$ (median 0.999), compared to 58.8\\% for JB-MLM (median 0.933). Per-seed analysis is more extreme---94--98\\% of single-model 9-class FPs are high-confidence (median 1.0), with the borderline fraction (25\\%) in majority vote arising from cross-seed disagreement rather than individual model uncertainty. This confirms that the 9-class ToxicChat FPR reflects systematic feature misalignment---classification DAPT shifts benign text into the jailbreak region with high confidence---rather than boundary ambiguity.\n\n\\section{Frozen Probing Verification}\n\\label{app:frozen_verify}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Frozen probing vs.\\ end-to-end (E2E) fine-tuning (3-seed mean$\\pm$std). 9-class: primary DAPT checkpoints; MLM: matched MLM control checkpoints. Frozen probing trains only BiGRU+MLP on frozen DAPT embeddings.}\n\\label{tab:frozen_verify}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Config} & IID & DD OOD & AA OOD & FITD OOD \\\\\n\\midrule\nFrozen 9-class & 1.000$\\pm$.000 & .997$\\pm$.005 & .972$\\pm$.026 & 1.000$\\pm$.000 \\\\\nFrozen MLM & .982$\\pm$.016 & .993$\\pm$.009 & .941$\\pm$.037 & .987$\\pm$.009 \\\\\nE2E 9-class & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .997$\\pm$.005 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:frozen_verify} compares frozen probing across DAPT objectives and against end-to-end fine-tuning. On easy OOD (DD, FITD), frozen MLM and frozen 9-class representations perform comparably ($\\Delta \\leq 1.3$\\,pp). On hard OOD (ActorAttack), 9-class retains a modest advantage (0.972 vs.\\ 0.941, $\\Delta$\\,=\\,3.1\\,pp) with lower variance ($\\sigma$\\,=\\,0.026 vs.\\ 0.037). Both far exceed vanilla encoders ($\\leq$0.318; Table~\\ref{tab:bert_proxy}). The E2E advantage over frozen 9-class is $\\leq$2.5\\,pp, confirming that Stage-1 representation quality is the primary source of OOD generalization.\n\nA striking asymmetry emerges when comparing frozen probing to the full pipeline (Table~\\ref{tab:evidence_hierarchy}): MLM frozen representations \\emph{outperform} the full MLM pipeline on AA OOD (0.941 vs.\\ 0.893), while 9-class frozen exactly matches its full pipeline (0.972 vs.\\ 0.972). This indicates that MLM's cross-seed instability originates in Stage-2 BiGRU training rather than Stage-1 DAPT: the MLM encoder produces adequate representations that are then degraded by unstable downstream optimization. Classification DAPT, by contrast, produces representations that remain robust through Stage-2 training, explaining its consistently lower variance (Table~\\ref{tab:evidence_hierarchy}).\n\nThis two-level structure (DAPT vs.\\ no-DAPT producing a representation quality leap of +70\\,pp; classification vs.\\ MLM DAPT producing a stability difference) is consistent with two further observations: $\\lambda$=0 matches $\\lambda > 0$ during E2E fine-tuning (Table~\\ref{tab:lambda}), and mean pooling matches BiGRU under E2E (Table~\\ref{tab:temporal}). Once DAPT representations are strong, downstream configuration details have minimal impact.\n\n\\subsection{Single-Turn Truncation Analysis}\n\\label{app:truncated}\n\nTo isolate whether the ToxicChat evidence-hierarchy reversal (Section~\\ref{sec:discussion}) reflects multi-turn structural dependence, we truncate each synthetic test conversation to its last user turn and re-evaluate both 9-class and JB-MLM models (3-seed mean).\n\n\\begin{table}[h]\n\\centering\n\\caption{Full-conversation vs.\\ last-turn-only F1 (3-seed mean). Truncation widens the 9-class advantage, ruling out multi-turn structure as the driver of the ToxicChat reversal.}\n\\label{tab:truncated}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Mode} & \\textbf{9-class} & \\textbf{JB-MLM} \\\\\n\\midrule\nIID & Full & 1.000 & .983 \\\\\nIID & Last turn & .991 & .894 \\\\\n\\midrule\nDD OOD & Full & .997 & .993 \\\\\nDD OOD & Last turn & .942 & .924 \\\\\n\\midrule\nAA OOD & Full & .972 & .941 \\\\\nAA OOD & Last turn & .978 & .927 \\\\\n\\midrule\nFITD OOD & Full & 1.000 & .987 \\\\\nFITD OOD & Last turn & 1.000 & .927 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize Mean $\\Delta$ (9-class $-$ MLM): Full +1.6\\,pp, Last turn +6.0\\,pp. 9-class advantage widens under truncation across all families, indicating the reversal on ToxicChat is driven by distributional differences between synthetic and human text, not by multi-turn structural dependence.}\n\\end{table}\n\n\\paragraph{Representation geometry analysis.}\n\\label{app:representation}\n\nTo characterize the mechanism behind classification DAPT's robustness, we analyze Stage-1 representations across all seven DeBERTa-v3-base variants (seed 42). We extract \\texttt{[CLS]} embeddings from 150 test conversations (50 IID + 50 DD OOD + 50 AA OOD) and compute three metrics.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Representation geometry and class separability across Stage-1 variants. PR: participation ratio (effective dimensionality of the embedding space). Fisher ratio: inter-class distance$^2$ / sum of intra-class variances. Weight $\\Delta$: L2 distance from pretrained weights (relative to pretrained norm).}\n\\label{tab:representation}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Variant} & \\textbf{PR} & \\textbf{Fisher} & \\textbf{Wt.\\ $\\Delta$ (\\%)} \\\\\n\\midrule\nVanilla & 31.9 & $<$0.001 & 0.000 \\\\\nWiki-MLM & 25.0 & $<$0.001 & 0.221 \\\\\nJB-MLM & 24.6 & $<$0.001 & 0.256 \\\\\nTopic & 14.5 & 0.012 & 0.371 \\\\\nScrambled & 7.8 & 2.60 & 0.283 \\\\\n9-class & 9.4 & 4.47 & 0.303 \\\\\nBinary & 3.7 & 19.7 & 0.239 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nClassification variants compress representations into 2--9 effective dimensions (vs.\\ 25--32 for MLM/vanilla) while increasing Fisher ratio by 3--5 orders of magnitude. Weight distances from pretrained are comparable across all variants ($\\sim$0.2--0.4\\%), indicating that the mechanism is representational restructuring rather than parameter-space regularization. Scrambled labels produce similar compression (PR\\,=\\,7.8, Fisher\\,=\\,2.6), confirming that the classification objective structure---not label semantics---drives discriminative compression.\n\n\\paragraph{Layer-wise localization.}\n\\label{app:layerwise}\n\nTo determine \\emph{where} discriminative compression occurs, we compute PR and Fisher ratio at every DeBERTa-v3-base layer (0--12) for four variants (9-class, scrambled, JB-MLM, vanilla) using the same 236-sample evaluation set (seed 42).\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig_layerwise_representation.pdf}\n\\caption{Layer-wise representation analysis. (a)~Participation ratio: classification variants (9-class, scrambled) show sharp dimensional collapse at layers 9--10 (PR\\,$\\approx$\\,1.5--2.9) while vanilla/JB-MLM maintain high dimensionality (PR\\,$\\approx$\\,7--10). (b)~Fisher ratio (log scale): class separability diverges from layer 8, with 9-class peaking at 10.9 (layer 10) vs.\\ vanilla 0.73 (15$\\times$).}\n\\label{fig:layerwise}\n\\end{figure}\n\nLayers 0--7 show no systematic divergence across variants (Fisher\\,$<$\\,2.1 for all; PR tracks similar oscillation patterns), consistent with \\citet{maennel2020random}'s finding that early layers learn label-independent features. From layer 8 onward, classification-supervised variants diverge sharply: 9-class Fisher rises from 3.2 (layer 8) to 10.9 (layer 10, peak), while vanilla remains below 1.5 throughout. Simultaneously, 9-class PR drops from 3.4 to 1.5 at layer 10---a 6.6$\\times$ compression relative to vanilla (PR\\,=\\,9.7). JB-MLM tracks vanilla across all layers (Fisher\\,$\\leq$\\,3.3, PR\\,$\\geq$\\,1.4), confirming that MLM does not induce discriminative restructuring. Scrambled labels exhibit the same late-layer pattern (Fisher peaks at 7.9, layer 12; PR drops to 1.5, layer 12), reinforcing that any classification signal---regardless of label semantics---triggers late-layer compression.\n\n\\paragraph{Discriminative subspace probe.}\n\\label{app:discriminative_probe}\n\nTo test whether the compressed subspace is \\emph{sufficient} for OOD detection, we project layer-10 \\texttt{[CLS]} representations onto the top-$k$ SVD components and train a logistic regression probe (3 seeds, sklearn default). Controls: random $k$-dimensional projections (10 random bases, mean reported) and vanilla/MLM models under identical projection.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Discriminative subspace probe: OOD F1 when projecting layer-10 representations onto top-$k$ SVD components vs.\\ random $k$-dimensional projections. 9-class top-3 achieves perfect AA detection with 3/768 dimensions; MLM fails even with all 768.}\n\\label{tab:discriminative_probe}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Projection} & DD & AA & FITD \\\\\n\\midrule\n9-class & top-3 & 1.000 & \\textbf{1.000} & 1.000 \\\\\n9-class & top-5 & 1.000 & 1.000 & 1.000 \\\\\n9-class & random-3 & 1.000 & 0.928$\\pm$.129 & 1.000 \\\\\n9-class & random-5 & 1.000 & 0.952 & 1.000 \\\\\n9-class & full-768 & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\nscrambled & top-3 & 1.000 & 0.962 & 1.000 \\\\\nscrambled & random-3 & 0.981 & 0.766 & 0.987 \\\\\n\\midrule\nJB-MLM & top-3 & 1.000 & 0.618 & 1.000 \\\\\nJB-MLM & full-768 & 1.000 & 0.636 & 1.000 \\\\\nJB-MLM & random-5 & 0.685 & 0.584 & 0.744 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings establish a link between compression and generalization (Table~\\ref{tab:discriminative_probe}). First, 9-class top-3 achieves perfect ActorAttack detection (F1\\,=\\,1.000) using only 3 of 768 dimensions---all discriminative information resides in the compressed subspace. Second, random 3-dimensional projections degrade to 0.928 on AA, confirming that the specific SVD directions matter. Third, JB-MLM reaches only 0.636 on AA even with all 768 dimensions, demonstrating that without classification-induced compression, the representation lacks the structure needed for cross-attack generalization. DD and FITD are near-ceiling for all models, making ActorAttack the critical test.\nSVD directions computed on IID training data only (without OOD test exposure) yield equal or higher F1 than all-data SVD (AA: 0.947 vs.\\ 0.904), confirming the subspace is not an artifact of test-set leakage.\n\n\\paragraph{SVD necessity ablation.}\n\\label{app:svd_necessity}\n\nThe probe above establishes \\emph{sufficiency}: 3 SVD dimensions carry enough information. To test \\emph{necessity}, we project \\emph{out} the top-3 SVD directions from full 768-dimensional 9-class \\texttt{[CLS]} embeddings and re-run BiGRU classification on OOD data (3 seeds). A random-3 removal control verifies that the effect is specific to the discriminative subspace. The top-3 directions explain 89.8\\% of training-set variance.\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{SVD necessity ablation: OOD F1 after projecting out top-3 vs.\\ random-3 SVD directions from 9-class layer-10 embeddings (3-seed mean$\\pm$std).}\n\\label{tab:svd_necessity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Condition} & DD OOD & FITD OOD & AA OOD \\\\\n\\midrule\nOriginal 768-dim & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .994$\\pm$.005 \\\\\nRemove top-3 SVD & .831$\\pm$.064 & 1.000$\\pm$.000 & .938$\\pm$.011 \\\\\nRemove random-3 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .994$\\pm$.005 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nRemoving top-3 SVD directions degrades DD detection by 17\\,pp (F1: $1.0 \\to 0.831$) and AA by 5.6\\,pp ($0.994 \\to 0.938$), while random-3 removal has zero effect. FITD is unaffected by either ablation, indicating its discriminative information is more distributed. Combined with the sufficiency result (Table~\\ref{tab:discriminative_probe}), the top-3 SVD directions are both sufficient and necessary for DD detection, sufficient but partially redundant for AA, and sufficient but not necessary for FITD.\n\n\\section{Temporal Aggregation Comparison}\n\\label{app:temporal}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Temporal aggregation comparison: mean pooling vs.\\ BiGRU under frozen and end-to-end (E2E) settings (3-seed mean$\\pm$std). Primary 9-class DAPT checkpoints.}\n\\label{tab:temporal}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Setting} & \\textbf{Aggregator} & DD OOD & AA OOD \\\\\n\\midrule\n\\multirow{2}{*}{Frozen} & BiGRU & .997$\\pm$.005 & .972$\\pm$.026 \\\\\n& Mean pooling & .991$\\pm$.013 & .962$\\pm$.015 \\\\\n\\midrule\n\\multirow{2}{*}{E2E} & BiGRU & 1.000$\\pm$.000 & .997$\\pm$.005 \\\\\n& Mean pooling & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:temporal} compares BiGRU and mean pooling under both frozen and E2E settings. Under frozen probing (the main paper's pipeline), BiGRU provides a marginal advantage on ActorAttack (+1.0\\,pp) with overlapping confidence intervals, consistent with the main text finding that temporal order is not a core detection factor ($|\\Delta| < 1$\\,pp under turn shuffling; Section~\\ref{sec:decomposition}). Under E2E fine-tuning, the difference vanishes entirely: mean pooling saturates all benchmarks at F1\\,=\\,1.000. The choice of frozen BiGRU in the main pipeline reflects a design trade-off: it enables representation-level analysis (CKA, t-SNE) that E2E would confound, while sacrificing $\\leq$1\\,pp on the hardest OOD set.\n\n\\section{Length Stratification Analysis}\n\\label{app:length}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Jailbreak recall by conversation length bin on OOD evaluation (3-seed majority vote). Benign conversations span 12--20 turns; jailbreak conversations span 3--10 turns.}\n\\label{tab:length}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Variant} & 1--3 turns & 4--6 turns & 7--10 turns \\\\\n\\midrule\n\\multirow{2}{*}{DD OOD} & 9-class & --- & 100.0\\% & 99.4\\% \\\\\n& Vanilla & --- & $\\leq$2.6\\% & $\\leq$1.7\\% \\\\\n\\midrule\n\\multirow{2}{*}{AA OOD} & 9-class & 93.3\\% & 95.6\\% & 100.0\\% \\\\\n& Vanilla & 0.0\\% & $\\leq$2.6\\% & 0.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:length} stratifies jailbreak recall by conversation length. The 9-class model shows no systematic degradation: ActorAttack recall increases monotonically from 93.3\\% (1--3 turns) to 100\\% (7--10 turns), and DD recall is near-perfect across all bins.\n\n\\paragraph{Length confound.}\nBenign conversations (12--20 turns) and jailbreak conversations (3--10 turns) have zero length overlap in the OOD evaluation sets, raising the concern that the model discriminates by conversation length rather than content. Three observations argue against this interpretation:\n(1)~Vanilla DeBERTa has access to identical length information via the BiGRU but achieves recall $\\leq$2.6\\% across all bins; length alone is insufficient without domain-adapted representations.\n(2)~At prefix $K$=1, where all conversations are length-equalized, 9-class still achieves F1\\,=\\,0.773$\\pm$0.041 on ActorAttack (Table~\\ref{tab:actorattack_full}), demonstrating content-based detection independent of length.\n(3)~The model is trained on IID data (Crescendo) and cannot learn OOD-specific length distributions; generalization to unseen length patterns must rely on content features that transfer across attack families.\n\n\\paragraph{Direct empirical verification.}\n\\label{app:length_independence}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Turn-count independence verification (9-class DeBERTa-v3-base, same checkpoint as Table~\\ref{tab:main_results}, 3 seeds). Evaluated on the full OOD test set (80 jailbreak + 75 benign conversations) rather than the balanced subset used in Table~\\ref{tab:main_results}. Part~A: FPR on test benign truncated to $K$ user turns (all seeds FPR\\,=\\,0). Part~B: WildChat FPR by turn-count bucket (mean$\\pm$std). Part~C: jailbreak detection (F1) after padding with benign turns to 15+ total turns (mean$\\pm$std where available).}\n\\label{tab:length_independence}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n& \\textbf{Condition} & \\textbf{FPR / F1} & $n$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Part A: Benign truncation (test set)}} \\\\[2pt]\n& Original (12--20 turns) & FPR = .000 & 38 \\\\\n& Truncated $K$=3 & FPR = .000 & 38 \\\\\n& Truncated $K$=5 & FPR = .000 & 38 \\\\\n& Truncated $K$=8 & FPR = .000 & 38 \\\\\n& Truncated $K$=10$^{*}$ & FPR = .000 & 38 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Part B: WildChat FPR by turn count}} \\\\[2pt]\n& Short (3--10 turns) & FPR = .770$\\pm$.105 & 196 \\\\\n& Medium (11--15 turns) & FPR = .942$\\pm$.054 & 23 \\\\\n& Long (16+ turns) & FPR = .857$\\pm$.117 & 7 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Part C: Jailbreak padding to 15+ turns}} \\\\[2pt]\n& DD original & F1 = .996 & 80 \\\\\n& DD padded & F1 = .971 ($\\Delta$=$-$2.5\\,pp) & 80 \\\\\n& AA original & F1 = .963 & 80 \\\\\n& AA padded & F1 = .383$\\pm$.261 ($\\Delta$=$-$57.9\\,pp) & 80 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$$K$=10 did not truncate any conversation (test benign max $\\sim$8 user turns).}\n\\end{table}\n\nTruncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut. $K$=3 and $K$=5 are the effective control conditions where all 38 conversations were truncated; $K$=10 exceeds the maximum test benign length and serves as a no-op control.\n\nWildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \\emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\\,=\\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.\n\nPadding jailbreak conversations with benign turns (Part~C) reveals an asymmetry: DD detection is resilient ($\\Delta$=$-$2.5\\,pp), but ActorAttack collapses ($\\Delta$=$-$57.9\\,pp). Padding experiments append benign turns \\emph{after} the complete attack sequence; in practice, adversaries would not dilute their own successful attacks. The collapse nonetheless exposes BiGRU temporal aggregation as vulnerable to attention dilution on subtle attack signals, a limitation discussed in Section~\\ref{sec:limitations}.\n\n\\section{Inference Efficiency}\n\\label{app:efficiency}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Inference efficiency comparison. DeBERTa+BiGRU and TF-IDF+LR measured on IID test (76 conversations, avg 8.3 turns, single A100). LLM latency from separate OOD evaluation (118 conversations); cross-condition comparison is indicative only.}\n\\label{tab:efficiency}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrcr@{}}\n\\toprule\n\\textbf{Method} & Latency (ms) & Params & VRAM \\\\\n\\midrule\nTF-IDF+LR & 0.43$\\pm$0.05 & $\\sim$10K & CPU \\\\\nDeBERTa+BiGRU (ours) & 12.1$\\pm$1.2 & 186.7M & 862\\,MB \\\\\nQwen3-8B 3-shot$^{\\dagger}$ & $\\sim$5{,}200 & 8B & $\\sim$16\\,GB \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{-2pt}\n{\\footnotesize $^{\\dagger}$Qwen3-8B latency from OOD evaluation (DD/AA, 118 conversations); not directly comparable to encoder latency measured on IID test.}\n\\end{table}\n\nTable~\\ref{tab:efficiency} compares inference cost. On matched data (IID test), DeBERTa+BiGRU processes a conversation in 12.1\\,ms, 28$\\times$ slower than TF-IDF (0.43\\,ms), but this speed gap purchases +71\\,pp on ActorAttack (F1\\,=\\,0.972 vs.\\ 0.261; Table~\\ref{tab:evidence_hierarchy}). LLM-as-judge approaches are orders of magnitude slower ($\\sim$5.2\\,s per conversation for Qwen3-8B 3-shot) while achieving substantially lower OOD detection (DD\\,=\\,0.566, AA\\,=\\,0.652; Table~\\ref{tab:llm_judge}). Zero-shot Qwen3-8B achieves F1\\,=\\,0.0 on DD OOD because it predicts all conversations as benign (Table~\\ref{tab:llm_judge}). The full DeBERTa+BiGRU pipeline requires 862\\,MB GPU memory, enabling deployment on consumer hardware. The 24.3$\\times$ speedup reported in the main text derives from a matched-condition comparison (DisPeD 13.12\\,ms vs.\\ Qwen3-8B 318.53\\,ms on the same GPU and data); the larger gap in Table~\\ref{tab:efficiency} reflects different hardware conditions and evaluation sets.\n\n\\section{Data Efficiency}\n\\label{app:data_efficiency}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Data efficiency of 9-class DAPT (3-seed mean$\\pm$std, sample std with $n{-}1$ divisor) and vanilla baseline (seed 42 only). $N$ = total training conversations (balanced jailbreak/benign).}\n\\label{tab:data_efficiency}\n\\begin{tabular}{@{}rlccc@{}}\n\\toprule\n$N$ & \\textbf{Variant} & IID & DD OOD & AA OOD \\\\\n\\midrule\n50 & 9-class & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .969$\\pm$.037 \\\\\n125 & 9-class & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .975$\\pm$.019 \\\\\n250 & 9-class & 1.000$\\pm$.000 & 1.000$\\pm$.000 & .975$\\pm$.035 \\\\\n350 & 9-class & 1.000$\\pm$.000 & .978$\\pm$.030 & .972$\\pm$.033 \\\\\n\\midrule\n50 & Vanilla & .646 & .529 & .234 \\\\\n125 & Vanilla & .532 & .244 & .244 \\\\\n250 & Vanilla & .987 & .365 & .502 \\\\\n350 & Vanilla & 1.000 & .360 & .489 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:data_efficiency} shows that 9-class DAPT reaches near-saturation performance with as few as 50 conversations (25 jailbreak + 25 benign): AA OOD F1\\,=\\,0.969$\\pm$0.037, already surpassing vanilla at full training size ($N$=350, AA\\,=\\,0.489) by 48\\,pp using only 14\\% of the data. DD OOD is perfectly solved at all training sizes. Vanilla performance is noisy across $N$ (single seed); the consistent pattern is that vanilla never exceeds DD\\,=\\,0.53 or AA\\,=\\,0.50 regardless of training size, while 9-class maintains AA\\,$\\geq$\\,0.969 at all $N$. Seed 456 is systematically lower across all $N$ values, contributing most of the cross-seed variance; this is consistent with the initialization sensitivity observed in the main results.\n\n\\section{Auxiliary Loss Weight Ablation}\n\\label{app:lambda}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Effect of auxiliary persuasion loss weight $\\lambda$ during Stage-2 E2E fine-tuning (seed 42). Stage-1 DAPT encoder is identical across all rows; only the Stage-2 loss $L = L_{\\text{binary}} + \\lambda \\cdot L_{\\text{strategy}}$ varies.}\n\\label{tab:lambda}\n\\begin{tabular}{@{}rcccc@{}}\n\\toprule\n$\\lambda$ & IID & DD OOD & FITD OOD & AA OOD \\\\\n\\midrule\n0 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n0.1 & 1.000 & 1.000 & 1.000 & .990 \\\\\n0.5 & 1.000 & 1.000 & 1.000 & .981 \\\\\n1.0 & 1.000 & 1.000 & 1.000 & .981 \\\\\n2.0 & 1.000 & 1.000 & 1.000 & .944 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDuring Stage-2 E2E fine-tuning, the auxiliary persuasion loss weight $\\lambda$ has limited impact on detection (Table~\\ref{tab:lambda}): the maximum AA OOD gap across all $\\lambda$ values is 5.6\\,pp (single seed), comparable to the cross-seed variance ($\\sim$6\\,pp) observed in the main results. All configurations converge to perfect validation F1 within epoch 1, indicating that DAPT representations already encode sufficient discriminative features for downstream classification (Section~\\ref{app:frozen_verify}). The value of persuasion strategy classification lies in Stage-1 DAPT, where it shapes encoder representations that transfer across attack families, not in the Stage-2 auxiliary loss.\n\n\\section{OOD Strategy Prediction Analysis}\n\\label{app:strategy_pred}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{OOD strategy prediction accuracy (jailbreak turns only) and detection rate for the 9-class model (3-seed mean). $r$: Pearson correlation between per-strategy prediction accuracy and per-strategy detection rate.}\n\\label{tab:strategy_pred}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Dataset} & Strat.\\ Acc.\\ & Det.\\ Rate & Missed (per seed) & $r$ \\\\\n\\midrule\nDD OOD & 50.1\\% & 99.6\\% & 0 / 0 / 1 & $\\sim$0.45 \\\\\nAA OOD & 50.1\\% & 96.2\\% & 1 / 7 / 1 & $\\sim$0.24 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:strategy_pred} reports OOD strategy prediction accuracy alongside detection rates. Strategy prediction accuracy is substantially above random (50.1\\% vs.\\ 11.1\\% chance for 9 classes) and positively correlated with detection success ($r \\approx 0.24$--0.45), but strategy prediction is not the detection mechanism: frozen probing with a randomly initialized strategy head (Appendix~\\ref{app:frozen_verify}) achieves 97.2\\% AA OOD detection, and $\\lambda$=0 (no strategy loss) matches or exceeds $\\lambda > 0$ during E2E fine-tuning (Table~\\ref{tab:lambda}). The classification objective shapes representations during Stage-1 DAPT training; at inference, strategy predictions are a byproduct of those representations, not a driver of detection.\n\n\\section{Cross-Seed Ensemble}\n\\label{app:ensemble}\n\n\\begin{table}[ht]\n\\centering\n\\footnotesize\n\\caption{Majority vote ensemble (3 seeds) vs.\\ single-seed mean on OOD Full. ``Fixed'' = samples corrected by ensemble; ``Broke'' = samples corrupted by ensemble.}\n\\label{tab:ensemble}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & DD single$\\to$ens. & AA single$\\to$ens. & Fixed & Broke \\\\\n\\midrule\n9-class & .997$\\to$\\textbf{1.000} & .972$\\to$\\textbf{.981} & 5 & 0 \\\\\nMLM & .914$\\to$\\textbf{1.000} & .897$\\to$\\textbf{.953} & 26 & 0 \\\\\nVanilla & .258$\\to$.258 & .258$\\to$.258 & 0 & 0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:ensemble} shows that majority vote never corrupts correct predictions (Broke\\,=\\,0 for all variants). MLM benefits most from ensembling (+8.6\\,pp DD, +6.0\\,pp AA), because its per-seed errors are complementary: each seed fails on different samples, and the majority corrects these. This further exposes MLM's seed instability: its individual seeds are unreliable, but their errors are uncorrelated. By contrast, 9-class seeds are already highly consistent (std\\,$\\leq$\\,0.026), leaving minimal room for ensemble improvement (+0.3--0.9\\,pp). Vanilla errors are systematic (all seeds fail on the same OOD samples), so ensembling provides no benefit.\n\n\\subsection{Seed-Level F1 Comparisons}\n\\label{app:seed_level}\n\nTo verify that cross-seed pooling does not mask inconsistent pairwise orderings, Table~\\ref{tab:seed_level} reports per-seed F1 for all variants on OOD DD and ActorAttack at full conversation length. The overall evidence hierarchy is maintained across seeds, with 9-class and binary consistently outperforming MLM; scrambled shows one reversal on AA (seed 42).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-seed F1 on OOD Full for key variants (seeds 42, 123, 456). The relative ordering is consistent across seeds.}\n\\label{tab:seed_level}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n& \\multicolumn{3}{c}{DD-Full} & \\multicolumn{3}{c}{AA-Full} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Variant} & s42 & s123 & s456 & s42 & s123 & s456 \\\\\n\\midrule\n9-class & 1.000 & 1.000 & .990 & .990 & .935 & .990 \\\\\nBinary & 1.000 & 1.000 & 1.000 & .981 & .990 & 1.000 \\\\\nScrambled & .990 & 1.000 & 1.000 & .891 & .990 & .971 \\\\\nMLM-only & 1.000 & .990 & .751 & .971 & .925 & .784 \\\\\nVanilla & .285 & .305 & .348 & .258 & .258 & .258 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 195,
        "oldLines": 7,
        "newStart": 195,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{figure}[ht]",
          " \\centering",
          "-\\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}",
          "+% \\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}",
          " \\caption{t-SNE visualization of mean-pooled \\texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}",
          " \\label{fig:tsne}",
          " \\end{figure}"
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

_source line 62_

Step 4: 验证注释生效 + Step 5: 匿名性扫描。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "8cd7c117-6f4f-4004-bbfb-5699f718785c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3yPsChRHSkQtEPTbeBdtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 30202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01J3TnMc4iuBPvkGbK5o97N4`</summary>

```json
{
  "command": "cd /tmp/anon_hotfix && grep -n 'includegraphics.*cka_heatmap\\|includegraphics.*embedding_tsne' docs/paper/appendix.tex",
  "description": "Verify commented-out lines start with %"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "42a3a44b-5763-4501-8e08-37d7bdfb8918",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3yPsChRHSkQtEPTbeBdtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 30202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
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

_source line 64 · 2026-05-25T09:21:17.101Z_

<details><summary>↩ Tool result · `toolu_01J3TnMc4iuBPvkGbK5o97N4`</summary>

```text
186:% \includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}
198:% \includegraphics[width=\columnwidth]{figures/paper/embedding_tsne.pdf}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "8073868c-aae1-4981-a656-78a2a068e218",
  "tool_use_result": {
    "stdout": "186:% \\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}\n198:% \\includegraphics[width=\\columnwidth]{figures/paper/embedding_tsne.pdf}",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_012jcswvDvGwCsVETvR3boBW`</summary>

```json
{
  "command": "cd /tmp/anon_hotfix && grep -rn 'westd\\|autodl\\|agent-ml-research\\|/home/ubuntu\\|/root/' docs/paper/*.tex || echo \"CLEAN\"",
  "description": "Anonymity scan for server/path leaks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "3515757a-5ce9-44a6-a829-a99fba6b0a7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3yPsChRHSkQtEPTbeBdtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 30202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
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

_source line 66 · 2026-05-25T09:21:19.500Z_

<details><summary>↩ Tool result · `toolu_012jcswvDvGwCsVETvR3boBW`</summary>

```text
CLEAN
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "4e60398b-7cc0-4436-a49b-5a9666ba15ad",
  "tool_use_result": {
    "stdout": "CLEAN",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_017NMi4umcQGHFqCxfKoTnek`</summary>

```json
{
  "command": "cd /tmp/anon_hotfix && grep -rin 'junwei\\|xiaoyu\\|caoxiaoyu' docs/paper/*.tex docs/paper/*.bib || echo \"CLEAN\"",
  "description": "Anonymity scan for author names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "0883159e-1eee-492b-9b79-622dbc1e9a24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3yPsChRHSkQtEPTbeBdtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 30202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
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

_source line 68 · 2026-05-25T09:21:20.544Z_

<details><summary>↩ Tool result · `toolu_017NMi4umcQGHFqCxfKoTnek`</summary>

```text
CLEAN
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "5056bbca-63bc-437b-ab3f-cece29db88f1",
  "tool_use_result": {
    "stdout": "CLEAN",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 69_

验证通过，匿名性清洁。Step 6: Commit + Force Push。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "d5985254-c751-40c8-af46-26eb12ade22c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g1VfnfuJN3BrQD8uUCCsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 30632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 732
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

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01ShA7YtcRVrkX3xb6USa35t`</summary>

```json
{
  "command": "cd /tmp/anon_hotfix && git add -A && git diff --cached --stat && git commit -m \"Hotfix: sync latest tex + comment out missing figures\" && git push --force origin main 2>&1 | grep -v 'ghp_\\|caoxiaoyu' | tail -5 && git log --oneline -1",
  "description": "Commit and force push hotfix to anonymous repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "0856b3a1-c6f2-4f96-bd30-b3e1cdc26caf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g1VfnfuJN3BrQD8uUCCsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 30632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 732
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

_source line 71 · 2026-05-25T09:21:27.639Z_

<details><summary>↩ Tool result · `toolu_01ShA7YtcRVrkX3xb6USa35t`</summary>

```text
 docs/paper/appendix.tex | 22 ++++++++++------------
 1 file changed, 10 insertions(+), 12 deletions(-)
[main ca1229f] Hotfix: sync latest tex + comment out missing figures
 1 file changed, 10 insertions(+), 12 deletions(-)
To https://github.com/anonymous-nlp-2026/persuasion_turn_jailbreak_detect.git
   d74a515..ca1229f  main -> main
ca1229f Hotfix: sync latest tex + comment out missing figures
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "0f36c6b3-5de0-496d-bd87-5c707caabea3",
  "tool_use_result": {
    "stdout": " docs/paper/appendix.tex | 22 ++++++++++------------\n 1 file changed, 10 insertions(+), 12 deletions(-)\n[main ca1229f] Hotfix: sync latest tex + comment out missing figures\n 1 file changed, 10 insertions(+), 12 deletions(-)\nTo https://github.com/anonymous-nlp-2026/persuasion_turn_jailbreak_detect.git\n   d74a515..ca1229f  main -> main\nca1229f Hotfix: sync latest tex + comment out missing figures",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 72_

完成。产出汇报：

1. **复制的文件**: 9 个 tex（main/abstract/introduction/related_work/method/experiments/conclusion/appendix/checklist）+ 1 个 bib（references.bib）
2. **注释的行**:
   - L186: `\includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}` → 加 `%` 注释
   - L198: `\includegraphics[width=\columnwidth]{figures/paper/embedding_tsne.pdf}` → 加 `%` 注释
3. **验证结果**: grep 确认两行均以 `%` 开头
4. **匿名性扫描**: CLEAN（无服务器路径泄露，无作者姓名泄露）
5. **Commit hash**: `ca1229f`
6. **Push**: 成功（main → main, non-fast-forward push completed）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "uuid": "14f98ce2-a4a7-4017-ae2b-4f66b234a4b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoUYTdzKy141Evb5Nkt1QH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 377,
      "cache_read_input_tokens": 31364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 377
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

_source line 73_

完成。产出汇报：

1. **复制的文件**: 9 个 tex（main/abstract/introduction/related_work/method/experiments/conclusion/appendix/checklist）+ 1 个 bib（references.bib）
2. **注释的行**:
   - L186: `\includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}` → 加 `%` 注释
   - L198: `\includegraphics[width=\columnwidth]{figures/paper/embedding_tsne.pdf}` → 加 `%` 注释
3. **验证结果**: grep 确认两行均以 `%` 开头
4. **匿名性扫描**: CLEAN（无服务器路径泄露，无作者姓名泄露）
5. **Commit hash**: `ca1229f`
6. **Push**: 成功（main → main, non-fast-forward push completed）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 139510,
  "duration_api_ms": 134198,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "a9e165fc-7620-4d0e-a78a-a5baa8750d3d",
  "total_cost_usd": 0.535416,
  "usage": {
    "input_tokens": 29,
    "cache_creation_input_tokens": 19900,
    "cache_read_input_tokens": 617164,
    "output_tokens": 4009,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19900,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 254,
        "cache_read_input_tokens": 31364,
        "cache_creation_input_tokens": 377,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 377
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1999,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0020889999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 29,
      "outputTokens": 4009,
      "cacheReadInputTokens": 617164,
      "cacheCreationInputTokens": 19900,
      "webSearchRequests": 0,
      "costUSD": 0.533327,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "db200594-6c00-4720-af5e-be7534e8c3f8"
}
```

</details>

---
